# RFC 8007: Content Delivery Network Interconnection (CDNI) Control Interface / Triggers
**Source**: IETF Standards Track | **Version**: RFC 8007 | **Date**: December 2016 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc8007

## Scope (Summary)
This document defines the CDNI Control Interface / Triggers (CI/T), which allows an upstream CDN (uCDN) to request that a downstream CDN (dCDN) pre-position, invalidate, or purge metadata or content, and to monitor the status of those activities. It builds on HTTP/1.1 and uses JSON encoding.

## Normative References
- [RFC1930] Guidelines for creation, selection, and registration of an Autonomous System (AS)
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC2818] HTTP Over TLS
- [RFC3986] Uniform Resource Identifier (URI): Generic Syntax
- [RFC5226] Guidelines for Writing an IANA Considerations Section in RFCs
- [RFC6707] Content Distribution Network Interconnection (CDNI) Problem Statement
- [RFC7159] The JavaScript Object Notation (JSON) Data Interchange Format
- [RFC7230] Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- [RFC7231] HTTP/1.1: Semantics and Content
- [RFC7232] HTTP/1.1: Conditional Requests
- [RFC7525] Recommendations for Secure Use of Transport Layer Security (TLS) and DTLS
- [RFC8006] Content Delivery Network Interconnection (CDNI) Metadata

## Definitions and Abbreviations
- **uCDN**: upstream CDN
- **dCDN**: downstream CDN
- **CDN PID**: a string of the form "AS&lt;number&gt;:&lt;qualifier&gt;", e.g., "AS64496:0", uniquely identifying a CDN provider.
- **Trigger Specification**: JSON object describing the type of trigger and the data to act upon.
- **Trigger Status Resource**: a resource in the dCDN tracking the status of a trigger command.
- **Trigger Collection**: a resource listing trigger status resources.
- **CI/T Command**: a JSON object sent from uCDN to dCDN, either a Trigger Command or a Cancel Command.
- **Content Collection IDentifier (ccid)**: a grouping of content as defined in RFC 8006.
- **PatternMatch**: a JSON object with a pattern (with wildcards * and ?) and optional flags for case sensitivity and query string matching.

## 2. Model for CDNI Triggers
- **CI/T Commands** are requests from uCDN to dCDN. Types: **preposition** (fetch metadata/content), **invalidate** (revalidate before reuse), **purge** (delete). Also **Cancel** commands.
- **dCDN** offers a web service; uCDN POSTs a command to a trigger collection; dCDN creates a Trigger Status Resource and returns its URI in a 201 response.
- dCDN maintains collections of Trigger Status Resources per uCDN, with filtered views (pending, active, complete, failed).
- **Figure 1** (informative) shows basic message flow: POST → 201 Location, then GET to poll status.

### 2.1. Timing of Triggered Activity
- Timing under dCDN's control.
- **Invalidate and purge commands MUST be applied to all data acquired before the command was accepted.** dCDN SHOULD NOT apply them to data acquired after.
- If uCDN wishes to invalidate/purge then immediately pre-position, it SHOULD ensure the prior command completes first.

### 2.2. Scope of Triggered Activity
- Commands can operate on multiple URLs.
- **In diamond configurations**, a dCDN MUST allow each uCDN that may have supplied content to act on it via CI/T. In all other cases, dCDN MUST reject CI/T Commands from a uCDN attempting to act on another uCDN's content (e.g., HTTP 403).
- Examples of diamond inefficiencies are described (informative).

### 2.3. Trigger Results
- Status states: pending, active, complete, processed, failed, canceling, cancelled.
- **CI/T Trigger Command MUST NOT be reported as "complete" until all actions completed successfully.** Errors MUST be enumerated.
- In a cascade, an intermediate CDN MUST forward commands to its dCDNs and MUST NOT report "complete" until all dCDNs report "complete" (or appropriate aggregated status). Canceled commands MUST be reported as "cancelling" until all downstream report final.

## 3. Collections of Trigger Status Resources
- **dCDN MUST make a collection of all Trigger Status Resources for each uCDN** (not visible to other uCDNs).
- dCDN MAY maintain filtered collections: **Pending, Active, Complete, Failed**. If implemented, MUST include links in the main collection.
- To trigger or cancel, uCDN POSTs to the main collection.

## 4. CDNI Trigger Interface
- Based on HTTP. dCDN MUST support GET, HEAD, POST, DELETE (RFC 7231). JSON representation MUST be supported (MIME type "application/cdni" with ptype parameter).
- URIs are dCDN-controlled; uCDN MUST NOT assume structure.
- dCDN SHOULD use HTTP caching (ETags) and Cache-Control to indicate polling frequency.

### 4.1. Creating Triggers
- uCDN POSTs a CI/T Command to the trigger collection.
- dCDN validates: if malformed or unauthorized, MUST respond with 4xx or create a "failed" Trigger Status Resource.
- On acceptance: **MUST create Trigger Status Resource, return 201 with Location header**. SHOULD include the resource body.
- Once created, URI MUST NOT be reused.
- dCDN SHOULD track progress; if not possible, MUST set status "processed" and add to complete collection.
- If command results in no activity, status MUST be "processed" or "complete".
- uCDN can cancel or delete but MUST NOT modify (dCDN MUST reject PUT/POST to individual resources with 405).

### 4.2. Checking Status
- Two methods: poll collection (Section 4.2.1) or poll individual resource (Section 4.2.2). SHOULD use ETags.

### 4.3. Canceling Triggers
- uCDN POSTs a CI/T Cancel Command to the main collection (with "cancel" array of URIs).
- dCDN MUST respond appropriately: 200 (if canceled), 202 (if accepted but still active), 501 (if not supported).
- Cancellation of pending/active/processed is optional-to-implement; status changes to "cancelling" then "cancelled". Completed/failed MUST NOT be changed to "cancelled".

### 4.4. Deleting Triggers
- uCDN can HTTP DELETE a Trigger Status Resource.
- If pending, dCDN SHOULD NOT start processing; if active/processed, SHOULD stop. No guarantee.
- References MUST be removed from all collections; further GETs SHOULD be rejected with HTTP error.

### 4.5. Expiry of Trigger Status Resources
- dCDN MAY auto-delete after some time. **MUST report the retention period** via "staleresourcetime" in the main collection.
- **RECOMMENDED** retention at least 24 hours. uCDN polling interval SHOULD be less than that.

### 4.6. Loop Detection and Prevention
- Each CDN appends its CDN PID to a "cdn-path" array in every command it originates or cascades.
- **dCDN MUST check cdn-path and reject any command containing its own PID**. Transit CDNs MUST NOT cascade to a dCDN already listed.
- CDN PID format: "AS&lt;number&gt;:&lt;qualifier&gt;". SHOULD be consistent with RI interface (RFC 7975) if implemented.

### 4.7. Error Handling
- Rejection via HTTP status codes (400, 403, 404).
- For accepted commands, errors reported in "errors" property of Trigger Status Resource (array of Error Descriptions).
- Handling of offline surrogates: invalidate may be reported complete (surrogates MUST revalidate when back online); preposition/purge may be reported processed; otherwise keep pending/active until acted upon or cancelled.

### 4.8. Content URLs
- If URLs are transformed by intermediate CDN, MUST similarly transform URLs in CI/T Commands.
- **CDNs MUST ignore URL scheme (HTTP/HTTPS) when comparing URLs** for invalidate/purge.

## 5. CI/T Object Properties and Encoding
- All objects use JSON with MIME type "application/cdni" and appropriate ptype.
- Names lowercase. Unrecognized name/value pairs SHOULD be ignored and passed through.

### 5.1. CI/T Objects
#### 5.1.1. CI/T Commands
- ptype=ci-trigger-command.
- Contains exactly one of "trigger" (Trigger Specification) or "cancel" (array of URLs). MUST include "cdn-path" (array of CDN PIDs).

#### 5.1.2. Trigger Status Resources
- ptype=ci-trigger-status.
- Includes "trigger" (Trigger Specification), "ctime", "mtime" (Absolute Time), optional "etime", "status" (Trigger Status), optional "errors" (array of Error Descriptions).

#### 5.1.3. Trigger Collections
- ptype=ci-trigger-collection.
- Contains "triggers" (array of URLs), optional "staleresourcetime", links to filtered collections (if implemented), optional "cdn-id" in main collection.

### 5.2. Properties of CI/T Objects
#### 5.2.1. Trigger Specification
- JSON object with "type", and at least one of "metadata.urls", "content.urls", "content.ccid", "metadata.patterns", "content.patterns".
- Patterns are PatternMatch objects; patterns not allowed for preposition.

#### 5.2.2. Trigger Type
- Defined in IANA registry. Values: "preposition", "invalidate", "purge".
- dCDN MUST reject unknown types with "failed" status and error "eunsupported".

#### 5.2.3. Trigger Status
- Values: "pending", "active", "complete", "processed", "failed", "cancelling", "cancelled".

#### 5.2.4. PatternMatch
- Object with "pattern" (string using wildcards * and ?, escape $), optional "case-sensitive" (default false), optional "match-query-string" (default false).

#### 5.2.5. Absolute Time
- JSON number: seconds since UNIX epoch (1970-01-01T00:00:00Z).

#### 5.2.6. Error Description
- Contains "error" (Error Code), at least one of "metadata.urls", "content.urls", "metadata.patterns", "content.patterns", optional "description".

#### 5.2.7. Error Code
- Defined in IANA registry. Values: "emeta", "econtent", "eperm", "ereject", "ecdn", "ecanceled", "eunsupported".
- Unknown codes MUST be treated as fatal and request not retried.

## 6. Examples (Condensed)
Section 6 provides illustrative HTTP requests and responses for creating triggers (preposition, invalidate), examining collections, polling with ETags, deleting, and error reporting. All examples use JSON as defined. URIs are examples only; uCDN MUST NOT depend on structure.

## 7. IANA Considerations
- Three new CDNI Payload Types registered: ci-trigger-command, ci-trigger-status, ci-trigger-collection.
- New registry: "CDNI CI/T Trigger Types" (RFC Required policy). Initial values: preposition, invalidate, purge.
- New registry: "CDNI CI/T Error Codes" (Specification Required). Initial values: emeta, econtent, eperm, ereject, ecdn, ecanceled, eunsupported.

## 8. Security Considerations
- Attacks could reveal future content popularity or catalog changes.
- dCDN MUST restrict actions to the uCDN's own data.
- **MUST support TLS (HTTPS) with mutual authentication**; TLS MUST be used unless alternate security (e.g., IPsec) is in place. Follow [RFC7525].
- HTTP requests for another CDN's data MUST be rejected (403/404).
- Denial-of-service: dCDN should consider rate-limiting or batch processing.
- No end-user privacy concerns. Commercially sensitive information is protected via TLS and access control.

## 9. References
See Normative References list above and Informative References in the original document.

## Informative Annexes (Condensed)
- **Appendix A**: Non-normative formalization of JSON objects using CDDL. Provides concise grammar for all CI/T object types, properties, and enumerations.