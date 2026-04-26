# RFC 2518: HTTP Extensions for Distributed Authoring – WEBDAV
**Source**: IETF – Network Working Group | **Version**: Standards Track, February 1999 | **Date**: February 1999 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc2518

## Scope (Summary)
Defines a set of methods, headers, and content-types ancillary to HTTP/1.1 for managing resource properties, creating and managing resource collections, namespace manipulation (COPY/MOVE), and resource locking (collision avoidance). Intended for remote web content authoring.

## Normative References
- [RFC2068] – HTTP/1.1
- [RFC2119] – Key words for requirement levels (MUST, SHOULD, etc.)
- [RFC2396] – URI Generic Syntax
- [RFC1766] – Language tags
- [RFC2277] – IETF Character Set Policy
- [RFC2069] – Digest Access Authentication
- [REC-XML] – XML 1.0 (W3C)
- [REC-XML-NAMES] – Namespaces in XML (W3C)
- [ISO-639] – Language codes
- [ISO-8601] – Date and time format
- [ISO-11578] – UUID specification
- [RFC2141] – URN Syntax
- [UTF-8] – RFC 2279

## Definitions and Abbreviations
- **URI/URL**: Uniform Resource Identifier/Locator, defined in [RFC2396].
- **Collection**: A resource containing a set of member URIs meeting requirements in Section 5.
- **Member URI**: A URI that is a member of a collection.
- **Internal Member URI**: A member URI immediately relative to the collection's URI (Section 5.2).
- **Property**: A name/value pair describing a resource.
- **Live Property**: Server-enforced semantics and syntax (e.g., `getcontentlength`).
- **Dead Property**: Client-managed semantics; server records value verbatim.
- **Null Resource**: A resource that responds 404 to all HTTP/1.1 or DAV methods except PUT, MKCOL, OPTIONS, LOCK. MUST NOT appear as a member of its parent collection.
- **Lock Token**: A state token URI identifying a particular lock. MUST be unique across all resources for all time.
- **OpaqueLockToken-URI**: Lock token scheme using UUIDs: `"opaquelocktoken:" UUID [Extension]`.

## Data Model for Resource Properties (Section 4)
- Properties are name/value pairs; names identify syntax/semantics.
- Two categories: live (server-enforced) and dead (client-enforced).
- Property values expressed in XML MUST be well-formed.
- Names are universally unique URIs (using XML namespace mechanism).
- No hierarchical properties recognized.
- Same property cannot be defined twice on a resource.
- **Media Independent Links**: A special property value (Section 12.4) connecting resources of any media type via source/destination URIs.

### Properties and HTTP Headers (4.3)
- Existing HTTP headers are inefficient for many properties; propfind/proppatch mechanisms allow selective retrieval/setting.

## Collections of Web Resources (Section 5)

### HTTP URL Namespace Model (5.1)
- Hierarchical namespace delimited by "/".
- A consistent namespace requires that for every URL there exists a collection containing it as an internal member (except root).
- Neither HTTP/1.1 nor WebDAV require full consistency, but certain methods prohibit inconsistencies.
- Resources MAY be identified by multiple URIs.

### Collection Resources (5.2)
- A collection's state includes a list of internal member URIs and properties; may have additional state (e.g., GET entity).
- Internal member URI MUST be immediately relative to the collection's base URI.
- Same internal member URI MUST NOT appear more than once.
- For WebDAV compliant resources A and B with URIs U and V where U is immediately relative to V, B MUST be a collection with U as internal member.
- Collection MAY list non-WebDAV compliant children, but not required.
- A WebDAV compliant resource with no compliant children is not required to be a collection.
- Trailing slash convention: requests without trailing "/" SHOULD receive a Content-Location header with the trailing "/".
- A resource MAY be a collection but not WebDAV compliant (i.e., supports collection behavior without all WebDAV methods). It may return `DAV:resourcetype` with value `DAV:collection` but MUST NOT return DAV header with "1".

### Creation and Retrieval (5.3)
- MKCOL method used for collection creation (not PUT/POST) to avoid unintended modifications or access control issues.

### Source Resources and Output Resources (5.4)
- Some resources have source (persistent state) separate from output (GET entity). Source URIs may be stored in a link of type `DAV:source` (Section 13.10).
- Source link values are not guaranteed correct; servers may not allow client setting.

## Locking (Section 6)

### Exclusive vs. Shared Locks (6.1)
- Exclusive lock: single principal.
- Shared lock: multiple principals can hold; used for collaboration without excluding others.

### Required Support (6.2)
- Server not required to support locking; if it does, may support any combination of exclusive/shared locks for any access types.

### Lock Tokens (6.3)
- Lock token = URI, unique across all resources for all time.
- `opaquelocktoken` scheme (UUID-based) meets uniqueness.
- Resources may return any URI scheme meeting uniqueness.
- Lock token provides no special access rights; enforcement based on authentication.

### opaquelocktoken Scheme (6.4)
- `OpaqueLockToken-URI = "opaquelocktoken:" UUID [Extension]`
- UUID generated per [ISO-11578]; extension must ensure uniqueness.
- Node field generation without IEEE 802 address (Section 6.4.1): use cryptographic quality random number or hash of system-specific randomness sources.

### Lock Capability Discovery (6.5)
- Server lock support is optional; client may discover via `supportedlock` property.
- Any resource supporting LOCK MUST support `supportedlock`.

### Active Lock Discovery (6.6)
- `lockdiscovery` property lists outstanding locks.
- Any resource supporting LOCK MUST support `lockdiscovery`.

### Usage Considerations (6.7)
- Locking cannot guarantee prevention of lost updates (e.g., non-WebDAV clients).
- Servers may reduce overwrites by requiring locks for modification.
- WebDAV clients should use lock/retrieve/write/unlock sequence.
- HTTP/1.1 clients should use If-Match with ETags.

## Write Lock (Section 7)

### Methods Restricted (7.1)
- Write lock prevents a principal without the lock from successfully executing: PUT, POST, PROPPATCH, LOCK, UNLOCK, MOVE, DELETE, MKCOL on the locked resource.
- GET and other methods unaffected.

### Lock Tokens (7.2)
- Successful exclusive/shared write lock request MUST generate a unique lock token per principal.

### Properties (7.3)
- Those without write lock may not alter properties. Live properties may still change due to schema requirements.

### Null Resources (7.4)
- Write lock on null resource (lock-null) responds 404/405 to all but PUT, MKCOL, OPTIONS, PROPFIND, LOCK, UNLOCK.
- Lock-null resource MUST appear in parent collection and have mandatory DAV properties.
- After successful PUT/MKCOL, resource ceases lock-null state.
- If unlocked without such method, returns to null state.

### Collections (7.5)
- Write lock on collection prevents addition/removal of member URIs by non-lock owners.
- If lock request on collection with conflicting locks on member URIs, MUST fail with 423 (Locked).
- New resources added as internal members of a locked collection automatically become part of the lock.

### If Request Header (7.6)
- Lock token MUST be submitted in If header for all locked resources a method may interact with; otherwise method MUST fail.

### COPY/MOVE (7.7)
- COPY MUST NOT duplicate write locks from source to destination (unless locked destination collection).
- MOVE MUST NOT move write lock with the resource; resource may be added to lock at destination as per Section 7.5.

### Refreshing Write Locks (7.8)
- Client MUST NOT submit the same lock request twice.
- LOCK method with If header but no body refreshes the lock (timers reset).
- Server may return different Timeout on refresh.

## HTTP Methods for Distributed Authoring (Section 8)
All DAV compliant clients/resources MUST use XML parsers compliant with [REC-XML]. All XML in requests/responses MUST be well-formed.

### 8.1 PROPFIND
- Retrieves properties of resource (and members if collection).
- ALL compliant resources MUST support PROPFIND and propfind element.
- Depth: "0", "1", "infinity" supported; default = infinity.
- Client may submit propfind XML to request specific properties, all properties, or property names. Empty body = all properties.
- Server MUST return a multistatus XML element (content type text/xml or application/xml).
- Errors on retrieving a property MUST be noted in response (e.g., 404 for non-existent).
- Results of PROPFIND SHOULD NOT be cached.
- For collections, response MUST include a response element for each member URI (flat list, order insignificant).
- For allprop/propname, if principal lacks right to know property existence, it should be silently excluded.

### 8.2 PROPPATCH
- Processes instructions to set/remove properties.
- ALL compliant resources MUST support PROPPATCH and propertyupdate, set, remove elements.
- Instructions processed in order; all must succeed or none (rollback).
- Request body MUST contain propertyupdate element.
- Status codes used with 207: 200 (OK), 403 (Forbidden), 409 (Conflict – e.g., read-only property), 423 (Locked), 507 (Insufficient Storage).

### 8.3 MKCOL
- Create new collection at Request-URI. MUST fail if resource is non-null.
- Ancestors MUST exist (else 409 Conflict).
- Without request body, new collection SHOULD have no members.
- If server does not support request body media type, MUST respond 415.
- Responses MUST NOT be cached (non-idempotent).
- Status codes: 201 (Created), 403 (Forbidden – server disallows or parent cannot accept), 405 (Method Not Allowed – resource exists), 409 (Conflict), 415, 507.

### 8.4 GET, HEAD for Collections
- Semantics unchanged; GET may return index.html, human-readable view, etc. No correlation to membership required.

### 8.5 POST for Collections
- Semantics unchanged (function determined by server).

### 8.6 DELETE
- **Non-collection**: Server MUST remove any URI from collections containing it.
- **Collections**: MUST act as "Depth: infinity"; client MUST NOT submit other depth. Delete collection and all member URIs. If any member cannot be deleted, ancestors MUST NOT be deleted to maintain namespace consistency. Response: 207 Multi-Status if error on member; 424 and 204 SHOULD NOT be in 207.

### 8.7 PUT
- **Non-collection**: Replaces GET entity; properties may be recomputed but not otherwise affected. Creation requires parent collection exist (else 409).
- **Collections**: Not defined; use MKCOL.

### 8.8 COPY
- Creates duplicate of source at Destination header (MUST be present).
- All compliant resources MUST support COPY.
- **Properties**: Live properties SHOULD be duplicated as live; if not possible, value copied as dead property. `propertybehavior` element can specify requirements.
- **Collections**: Without Depth header, acts as "infinity". Depth "0" copies collection and properties but not members. Headers (except Destination) applied to all sub-resources. Server MUST skip a subtree on error but continue others. Error on non-Request-URI resource returns 207. 424 and 201/204 SHOULD NOT be in 207.
- **Overwrite**: If Overwrite header is "T", DELETE destination first. If "F", fail if destination non-null.
- Status codes: 201, 204, 403, 409, 412 (Precondition Failed – property liveness or Overwrite=F with non-null), 423, 502, 507.

### 8.9 MOVE
- Logical equivalent of COPY + consistency maintenance + DELETE, atomic.
- Destination header MUST be present; same COPY property behavior.
- All compliant resources MUST support MOVE.
- **Collections**: Act as "Depth: infinity"; client MUST NOT submit other depth. Error on subtree: skip and continue others. Response 207 for error on non-Request-URI.
- **Overwrite**: Same as COPY.
- Status codes: 201, 204, 403, 409, 412, 423 (source or destination locked), 502.

### 8.10 LOCK
- Creates lock specified by lockinfo XML element on Request-URI.
- Request SHOULD have owner XML element (unless refresh).
- Lock method request MAY have Timeout header.
- Clients MUST assume locks may disappear at any time.
- Response MUST contain lockdiscovery property in a prop XML element.
- Successful new lock: Lock-Token response header MUST be included (not for refresh).
- **Effect on properties and collections**: Lock scope includes entire state (body and properties). For collections, also affects member addition/removal.
- **Replicated resources**: Lock request MUST fail if cannot be honored by all URIs of the resource.
- **Depth**: "0" or "infinity" only. If depth infinity and cannot lock all, return 409 with multistatus. Partial success not allowed.
- No Depth header acts as "infinity".
- **Interaction**: Successful DELETE of resource removes all its locks.
- **Compatibility table**: Shared+True, Exclusive+? (see Table in spec)
- Status codes: 200 (OK with lockdiscovery), 412 (Precondition Failed – lock token not enforceable), 423 (Locked).

### 8.11 UNLOCK
- Removes lock identified by Lock-Token request header from Request-URI and all resources in lock.
- If cannot unlock all, MUST fail.
- Any resource supporting LOCK MUST support UNLOCK.

## HTTP Headers for Distributed Authoring (Section 9)

### 9.1 DAV Header
- `DAV = "DAV" ":" "1" ["," "2"] ["," 1#extend]`
- All compliant resources MUST return DAV header on OPTIONS responses.
- Value lists compliance classes (class 1, class 2).

### 9.2 Depth Header
- `Depth = "Depth" ":" ("0" | "1" | "infinity")`
- Used with methods on resources with potential internal members.
- Supported only if method definition explicitly provides.
- Default behavior per method; clients MUST NOT rely on order or atomicity.
- Headers applied to all resources in scope unless otherwise defined.
- Lock token must be submitted in If header for locked resources within scope.
- Depth header ignored for resources without internal children.
- Illegal Depth value returns 400 (Bad Request).

### 9.3 Destination Header
- `Destination = "Destination" ":" absoluteURI`
- Used with COPY and MOVE.

### 9.4 If Header
- `If = "If" ":" ( 1*No-tag-list | 1*Tagged-list)`
- Intended to function like If-Match for state tokens (e.g., lock tokens) and ETags.
- All compliant resources MUST honor If header.
- If the state of the resource does not match any of the specified state lists, request MUST fail with 412 (Precondition Failed).
- **No-tag-list**: Applies to each resource the method is applied to.
- **Tagged-list**: Scopes list to a specific resource. Same URI MUST NOT appear more than once.
- **not production**: Reverses matching value.
- **Matching function**: exact match for state token; entity tag matches resource's ETag.
- **Non-DAV compliant proxies**: Use Cache-Control: no-cache (HTTP/1.1) or Pragma: no-cache (HTTP/1.0).

### 9.5 Lock-Token Header
- Request: used with UNLOCK to identify lock to remove.
- Response: used with LOCK to indicate lock token created.

### 9.6 Overwrite Header
- `Overwrite = "Overwrite" ":" ("T" | "F")`
- For COPY/MOVE: "F" prevents operation if destination non-null.
- Default if absent: "T". Missing "T" header? Actually says treat as "T".
- Method MUST fail with 412 if not performed due to Overwrite=F.
- All compliant resources MUST support Overwrite header.

### 9.7 Status-URI Response Header
- May be used with 102 (Processing) to inform client of status of a method.

### 9.8 Timeout Request Header
- `TimeOut = "Timeout" ":" 1#TimeType`
- TimeType: "Second-" DAVTimeOutVal, "Infinite", or Extend.
- Client may include in LOCK requests; server not required to honor.
- Client MUST NOT submit Timeout with non-LOCK methods.
- Multiple entries indicate preferences (order of preference).
- Response values MUST use Second, Infinite, or a TimeType client indicated.
- Timeout counter SHOULD be restarted on any method from lock owner.
- If timeout expires, server SHOULD act as if UNLOCK was executed.
- Client MUST NOT assume lock lost just because timeout expired.

## Status Code Extensions to HTTP/1.1 (Section 10)
- **102 Processing**: Interim response for long-running requests; server SHOULD return if method takes >20 seconds.
- **207 Multi-Status**: Provides status for multiple independent operations.
- **422 Unprocessable Entity**: Syntactically correct but semantically erroneous XML.
- **423 Locked**: Source or destination resource is locked.
- **424 Failed Dependency**: Method could not be performed because a depended action failed.
- **507 Insufficient Storage**: Server unable to store representation for completion; temporary condition.

## Multi-Status Response (Section 11)
- Default 207 body is text/xml or application/xml containing multistatus element, which contains response elements with status codes (200-500 series; 100 series SHOULD NOT be recorded).

## XML Element Definitions (Section 12)
- All elements defined with namespace DAV: (unless otherwise noted).
- Key elements: activelock, locktoken, timeout, collection, href, link (src, dst), lockentry, lockinfo, lockscope (exclusive, shared), locktype (write), multistatus (response, propstat, status, responsedescription), owner, prop, propertybehavior (keepalive, omit), propertyupdate (remove, set), propfind (allprop, propname, prop).
- Complete DTD in Appendix 1.

## DAV Properties (Section 13)
- Property names are also XML element names.
- Mandatory properties for compliant resources: creationdate, displayname, getcontentlanguage, getcontentlength, getcontenttype, getetag, getlastmodified, lockdiscovery, resourcetype, source, supportedlock.
- Each property defined with namespace, purpose, description, value format.

## Instructions for Processing XML in DAV (Section 14)
- All compliant resources MUST ignore any unknown XML element and all its children while processing a DAV method.
- This also applies to clients processing property values (unless schema declares otherwise).
- Exception: setting dead properties – server MUST record unknown XML elements.
- Exception: when XML is content type of entity body (e.g., PUT).
- DAV server MUST accept XML as text/xml or application/xml; client MUST accept either.

## DAV Compliance Classes (Section 15)
- All compliant resources MUST comply with [RFC2068].
- **Class 1**: Meets all "MUST" requirements in all sections. Returns "1" in DAV header.
- **Class 2**: Meets class 1 requirements plus supports LOCK, supportedlock, lockdiscovery, Timeout response header, Lock-Token request header. SHOULD support Timeout request header and owner XML element. Returns "1" and "2" in DAV header.

## Internationalization Considerations (Section 16)
- Complies with IETF Character Set Policy [RFC2277].
- Human-readable fields encoded using XML (UTF-8 minimum, language tagging via xml:lang).
- WebDAV applications MUST support character set tagging/encoding and language tagging of XML.
- Property names are URIs; applications should provide human-readable display names.
- Error status codes include short English description; internationalized apps should ignore and use locale-specific messages.

## Security Considerations (Section 17)
- All HTTP/1.1 and XML security considerations apply.
- **Authentication**: Basic authentication MUST NOT be used unless connection secure (e.g., TLS). WebDAV MUST support Digest authentication [RFC2069].
- **Denial of Service**: Attacks via large files, recursive operations, many connections.
- **Security through Obscurity**: PROPFIND eliminates obscurity; use access control.
- **Privacy**: lock owner information in lockdiscovery should be access-controlled; user agents should control contact info sent.
- **Properties**: Access control should separate read access to body and properties.
- **Source Link**: Reduces security of hiding script sources; caution with remote authoring.
- **XML External Entities**: Untrustworthy; may modify DTD, expose security risks, cause scalability problems.
- **Lock Tokens**: UUIDs may expose IEEE 802 address; use alternate node generation (Section 6.4.1) to avoid risks.

## IANA Considerations (Section 18)
- IANA to reserve URI namespaces starting with "DAV:" and "opaquelocktoken:" for this and related specifications.

## Informative Annexes (Condensed)
- **Appendix 1 – WebDAV Document Type Definition**: DTD for all XML elements defined in Sections 12 and 13.
- **Appendix 2 – ISO 8601 Date and Time Profile**: Defines a profile of ISO 8601 for creationdate property, with BNF for date-time, full-date, full-time, etc.
- **Appendix 3 – Notes on Processing XML Elements**: Clarifies empty XML elements (<A/> vs <A> </A>) and provides examples of illegal XML processing (e.g., containing both allprop and propname in propfind) and handling unknown elements.
- **Appendix 4 – XML Namespaces for WebDAV**: All compliant systems MUST support XML namespaces [REC-XML-NAMES]. A qualified name is interpreted as a URI constructed by appending the LocalPart to the namespace name URI. Examples illustrate semantic identity despite different prefixes.

## Requirements Summary
| ID | Requirement (condensed) | Type | Reference |
|---|---|---|---|
| R1 | Property values in XML MUST be well-formed | MUST | 4.4 |
| R2 | Internal member URI MUST be immediately relative to collection URI | MUST | 5.2 |
| R3 | If resource A has URI immediately relative to B, B MUST be a collection containing A | MUST | 5.2 |
| R4 | MKCOL MUST fail if Request-URI is non-null | MUST | 8.3.1 |
| R5 | PROPFIND all compliant resources MUST support | MUST | 8.1 |
| R6 | PROPFIND MUST support Depth 0, 1, infinity | MUST | 8.1 |
| R7 | PROPPATCH all compliant resources MUST support | MUST | 8.3? Actually 8.2 |
| R8 | COPY all compliant resources MUST support | MUST | 8.8 |
| R9 | MOVE all compliant resources MUST support | MUST | 8.9 |
| R10 | LOCK method requires lockinfo XML, response includes lockdiscovery | MUST | 8.10 |
| R11 | UNLOCK all compliant resources supporting LOCK MUST support | MUST | 8.11 |
| R12 | DAV header returned on all OPTIONS responses | MUST | 9.1 |
| R13 | If header honored by all compliant resources | MUST | 9.4 |
| R14 | Overwrite header supported by all compliant resources | MUST | 9.6 |
| R15 | Ignoring unknown XML elements in DAV methods | MUST | 14 |
| R16 | Servers MUST accept XML as text/xml or application/xml | MUST | 14 |
| R17 | Basic authentication MUST NOT be used unless connection secure | MUST | 17.1 |
| R18 | WebDAV applications MUST support Digest authentication | MUST | 17.1 |
| R19 | All compliant resources MUST support XML namespace extensions [REC-XML-NAMES] | MUST | Appendix 4 |