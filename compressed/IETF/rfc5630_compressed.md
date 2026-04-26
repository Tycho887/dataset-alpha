# RFC 5630: The Use of the SIPS URI Scheme in the Session Initiation Protocol (SIP)
**Source**: IETF | **Version**: Standards Track | **Date**: October 2009 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc5630

## Scope (Summary)
Provides clarifications, guidelines, and normative changes to SIP concerning the SIPS URI scheme. Deprecates the “last-hop exception” for TLS, mandates that SIPS requires TLS on every hop between UAC and remote UAS, and defines rules for URI scheme handling in registrations, routing, and dialogs.

## Normative References
- [RFC2119] – Key words for requirement levels
- [RFC3261] – SIP: Session Initiation Protocol
- [RFC5246] – TLS Protocol Version 1.2
- [RFC5626] – Managing Client-Initiated Connections in SIP

## Definitions and Abbreviations
- **SIPS URI**: A URI with scheme “sips” indicating that the resource be contacted securely using TLS on each hop.
- **TLS**: Transport Layer Security (RFC 5246)
- **UAC/UAS**: User Agent Client / User Agent Server
- **AOR**: Address of Record
- **GRUU**: Globally Routable User Agent URI (RFC 5627)
- **“MUST”, “SHOULD”, “MAY”** etc. as per RFC 2119

## 1. Introduction
The meaning and usage of SIPS and TLS were underspecified in RFC 3261. This document provides clarifications and normative changes.

## 2. Terminology
Key words are as defined in RFC 2119.

## 3. Background (Condensed)
### 3.1 Models for TLS in SIP
- **Server-Provided Certificate** (section 3.1.1): Only server provides certificate; UA initiates TLS and keeps connection alive. RFC 5626 supports NAT/firewall traversal.
- **Mutual Authentication** (section 3.1.2): Both sides provide certificates; suitable for server-to-server but impractical for many UAs due to certificate infrastructure.
- **Using TLS with SIP instead of SIPS** (section 3.1.3): SIPS is strictly “TLS-only”; SIP over TLS is “best-effort”. Using TLS with SIP URIs is simpler and allows fallback.
- **transport=tls and TLS Via parameter** (section 3.1.4): Deprecated in RFC 3261; not used in this specification.

### 3.2 Detection of Hop-by-Hop Security
A SIPS Request-URI does not guarantee end-to-end TLS; UAS can inspect Via, History-Info, or use S/MIME/SIP Identity. Retargeting from SIP to SIPS can mislead.

### 3.3 Problems with SIPS in RFC 3261
The “last-hop exception” allowed Proxy B to use policy-based (non-TLS) last hop. This was flawed and is deprecated. New model requires TLS on all hops to the UAS.

## 4. Overview of Operations (Condensed)
SIPS means TLS on every hop from UAC to remote UAS (no last-hop exception). SIPS does not provide end-to-end security guarantee; it is a request that the resource be contacted securely. SIPS URIs can appear in multiple header fields (Contact, Route, Record-Route, Path, etc.). A SIP URI and a SIPS URI with same user@domain refer to the same resource, but scheme switching is restricted.

### 4.1 Routing
Proxies MUST NOT downgrade SIPS to SIP or upgrade SIP to SIPS. If a UAS registers with a SIPS Contact, a request to sips:AOR goes to that Contact; a request to sip:AOR is forwarded with a SIP Request-URI (scheme replaced) over TLS. If only a SIP Contact exists, requests to sips:AOR fail (480 “SIPS Not Allowed”).

## 5. Normative Requirements
### 5.1 General User Agent Behavior
#### 5.1.1 UAC Behavior
- UAC MUST NOT change a SIPS URI to a SIP URI.
- If Request-URI or top Route contains SIPS, Contact MUST be SIPS (RFC 3261).
- Upon receiving 416 or 480 with warn-code 380, UAC MUST NOT automatically replace SIPS with SIP; SHOULD get user confirmation.
- If route set is not empty and UAC uses SIPS Request-URI, it MUST change any SIP Route entries to SIPS.
- If UAC uses SIP Request-URI but top Route is SIPS with lr, it MUST send over TLS with SIP Request-URI; if top Route is SIPS without lr, MUST use SIPS Request-URI.
- UAs MUST NOT use transport=tls.

##### 5.1.1.1 Registration
- To be reachable with SIPS, UA MUST register with a SIPS Contact.
- If not wanting SIPS, UA MUST register with a SIP Contact.
- Registering with SIPS Contact implies binding of both SIPS and SIP Contacts; UA MUST NOT include both SIP and SIPS versions of same Contact; SHOULD NOT register both separately.
- If all Contacts are SIPS, REGISTER MUST use SIPS AORs in From/To; otherwise, MUST use SIP AORs.

##### 5.1.1.2 SIPS in a Dialog
- If initial request used SIP Request-URI and top Route is not SIPS, UAC MUST use SIP Contact (even if sent over TLS).
- On target refresh, if original used SIPS Request-URI, Contact MUST be SIPS.

##### 5.1.1.3 Derived Dialogs and Transactions
- MUST NOT result in effective downgrading of SIPS to SIP without explicit authorization (e.g., REFER, Replaces, Join). SHOULD warn user.

##### 5.1.1.4 GRUU
- When GRUU assigned, both SIP and SIPS GRUUs are assigned. If Contact in REGISTER is SIP, SIP GRUU returned; if SIPS, SIPS GRUU returned.
- If wrong scheme received, UAC SHOULD treat as proper scheme.

#### 5.1.2 UAS Behavior
- UAS MUST NOT change SIPS to SIP.
- In dialog-creating response, if Request-URI or top Record-Route/Contact was SIPS, response Contact MUST be SIPS (RFC 3261).
- If UAS does not wish SIPS, MUST respond 480 with warn-code 380.
- If UAS requires SIPS and receives SIP request, MUST reject with 480 and warn-code 381.
- On target refresh, Contact MUST be SIPS if original used SIPS.
- UASs MUST NOT use transport=tls.

### 5.2 Registrar Behavior
- Registrar MUST consider SIP and SIPS AORs with same user@domain as equivalent.
- Registrar MUST accept SIPS Contact only if Request-URI, Contacts, and all Path URIs are SIPS; otherwise reject REGISTER with 400.
- If UA registered with SIPS Contact, returned service route (RFC 3608) SHOULD be SIP URIs if both SIP and SIPS allowed; MUST be SIPS URIs if only SIPS allowed.

#### 5.2.1 GRUU
- Registrar MUST assign both SIP and SIPS GRUUs. Return SIP GRUU if Contact is SIP; SIPS GRUU if SIPS.

### 5.3 Proxy Behavior
- Proxy MUST NOT use last-hop exception. When forwarding a SIPS Request-URI, MUST forward to a SIPS Request-URI. If target registered with SIP Contact, MUST NOT forward; reject with 480 and warn-code 380.
- Proxy SHOULD forward SIP Request-URI over TLS when possible.
- When receiving SIP Request-URI, proxy MUST NOT forward to SIPS Request-URI. If target registered with SIPS Contact, proxy MUST replace scheme to SIP and forward over TLS. May reject with 480 and warn-code 381 if not capable or policy.
- If URIs inconsistent (e.g., SIPS Request-URI but SIP Contact), proxy SHOULD reject with 400.
- RECOMMENDED to use RFC 5626 for UACs without certificates.
- If proxy receives 3XX with SIP Contact (or 416/480 with warn-code 380) while using SIPS, MUST NOT recurse; forward best response.
- If proxy receives 3XX with SIPS Contact (or 480 with warn-code 381) while using SIP, MUST NOT recurse.
- Proxies MUST NOT use transport=tls.

### 5.4 Redirect Server Behavior
- When SIP Request-URI received, redirect MAY return SIP or SIPS Contact. If target registered with SIPS Contact, SHOULD return SIPS if TLS usable; if SIP Contact, MUST return SIP.
- When SIPS Request-URI received, redirect MAY return SIP or SIPS Contact. If target registered with SIPS Contact, SHOULD return SIPS; if SIP Contact, MUST return SIP. If not redirecting, MAY reject with 480 (SIPS Not Allowed).
- If URIs inconsistent, redirect SHOULD use 400.
- Redirect servers MUST NOT use transport=tls.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | UAC MUST NOT change SIPS to SIP | MUST | 5.1.1 |
| R2 | If SIPS in Req-URI or top Route, Contact MUST be SIPS | MUST | 5.1.1, RFC 3261 |
| R3 | UAC MUST NOT automatically replace SIPS with SIP after 416/480(380) | MUST | 5.1.1 |
| R4 | UAC using SIPS Req-URI MUST change SIP Route entries to SIPS | MUST | 5.1.1 |
| R5 | UAC with SIP Req-URI and top Route=SIPS(lr) MUST send over TLS | MUST | 5.1.1 |
| R6 | UAs MUST NOT use transport=tls | MUST | 5.1.1 |
| R7 | UA wishing SIPS reachability MUST register with SIPS Contact | MUST | 5.1.1.1 |
| R8 | UA not wanting SIPS MUST register with SIP Contact | MUST | 5.1.1.1 |
| R9 | REGISTER with SIPS Contact: MUST NOT include both SIP and SIPS versions of same Contact | MUST | 5.1.1.1 |
| R10 | If all Contacts SIPS, From/To MUST be SIPS AORs; else MUST be SIP AORs | MUST | 5.1.1.1 |
| R11 | In dialog initiating request with SIP Req-URI and no SIPS top Route, Contact MUST be SIP | MUST | 5.1.1.2 |
| R12 | On target refresh, if original used SIPS, Contact MUST be SIPS | MUST | 5.1.1.2, 5.1.2 |
| R13 | Derived dialogs MUST NOT downgrade SIPS to SIP without authorization | MUST | 5.1.1.3 |
| R14 | UAS MUST NOT change SIPS to SIP | MUST | 5.1.2 |
| R15 | Response Contact MUST be SIPS if request had SIPS Req-URI, top Record-Route, or Contact | MUST | 5.1.2 (RFC 3261) |
| R16 | UAS not wanting SIPS MUST reject with 480 (SIPS Not Allowed) | MUST | 5.1.2 |
| R17 | UAS requiring SIPS on SIP request MUST reject with 480 (SIPS Required) | MUST | 5.1.2 |
| R18 | Registrar MUST consider SIP and SIPS AORs equivalent | MUST | 5.2 |
| R19 | Registrar MUST accept SIPS Contact only if all URIs are SIPS; else 400 | MUST | 5.2 |
| R20 | Registrar returning service route: if UA registered with SIPS Contact, service route MUST be SIP URIs to allow both schemes, or SIPS URIs for SIPS-only | MUST | 5.2 |
| R21 | Registrar MUST assign both SIP and SIPS GRUUs | MUST | 5.2.1 |
| R22 | Registrar MUST return SIP GRUU if Contact= SIP; SIPS GRUU if Contact= SIPS | MUST | 5.2.1 |
| R23 | Proxy MUST NOT use last-hop exception | MUST | 5.3 |
| R24 | Proxy forwarding SIPS Req-URI MUST forward to SIPS Req-URI | MUST | 5.3 |
| R25 | If target registered with SIP Contact, proxy MUST NOT forward SIPS request; reject 480 | MUST | 5.3 |
| R26 | Proxy SHOULD forward SIP requests over TLS when possible | SHOULD | 5.3 |
| R27 | Proxy receiving SIP Req-URI MUST NOT forward to SIPS Req-URI | MUST | 5.3 |
| R28 | Proxy forwarding SIP request to UAS with SIPS Contact MUST replace scheme to SIP and forward over TLS | MUST | 5.3 |
| R29 | Proxy may reject with 480 (SIPS Required) if unable/ policy | MAY | 5.3 |
| R30 | Proxy SHOULD reject with 400 if URIs inconsistent | SHOULD | 5.3 |
| R31 | Proxy MUST NOT recurse on 3XX with SIP Contact (or 416/480-380) when using SIPS | MUST | 5.3 |
| R32 | Proxy MUST NOT recurse on 3XX with SIPS Contact (or 480-381) when using SIP | MUST | 5.3 |
| R33 | Proxies MUST NOT use transport=tls | MUST | 5.3 |
| R34 | Redirect server: SIP Req-URI may redirect to SIP or SIPS; if target registered SIPS Contact, SHOULD return SIPS; if SIP Contact, MUST return SIP | MUST/SHOULD | 5.4 |
| R35 | Redirect server: SIPS Req-URI may redirect to SIP or SIPS; if target registered SIPS Contact, SHOULD return SIPS; if SIP Contact, MUST return SIP | MUST/SHOULD | 5.4 |
| R36 | Redirect server MUST NOT recurse on inconsistent URIs; SHOULD use 400 | SHOULD | 5.4 |
| R37 | Redirect servers MUST NOT use transport=tls | MUST | 5.4 |
| R38 | UAC SHOULD get user confirmation before re-attempting with SIP after 480(380) | SHOULD | 5.1.1 |
| R39 | UAC SHOULD treat wrong GRUU scheme as proper scheme | SHOULD | 5.1.1.4 |
| R40 | UAS SHOULD include Warning header (380/381) when rejecting | SHOULD | 5.1.2 |
| R41 | Proxy SHOULD include Warning header (380/381) when rejecting | SHOULD | 5.3 |
| R42 | Proxy RECOMMENDED to use RFC 5626 for outbound | RECOMMENDED | 5.3 |
| R43 | Derived dialogs SHOULD NOT downgrade SIPS without authorization | SHOULD | 5.1.1.3 |

## 6. Call Flows (Condensed)
Provides three example flows using topology with Bob’s PC and phone, Alice’s proxy. Illustrates registration (SIP vs SIPS Contact), calling Bob’s SIPS AOR (routed only to phone), calling Bob’s SIP AOR (forked to both, phone answers), and calling Bob’s SIP AOR using TLS (identical to second but all Via are TLS). Demonstrates scheme replacement rules and TLS usage.

## 7. Further Considerations (Condensed)
Discusses complications: Record-Route absence, TLS mutual vs server-side authentication, and the importance of RFC 5626 for NAT traversal. SIPS requires TLS connectivity; certificate validation may limit applicability.

## 8. Security Considerations
The document itself primarily addresses security. Deprecation of last-hop exception closes a vulnerability. Section 26.4.4 of RFC 3261 applies as modified by Appendix A.

## 9. IANA Considerations
Registers two new warning codes:
- **380** – SIPS Not Allowed
- **381** – SIPS Required

## Appendix A. Bug Fixes for RFC 3261 (Normative Corrections)
- Section 8.1.3.5: Retry with SIP URI MUST NOT be automatic if original used SIPS.
- Section 10.2.1: REGISTER with SIPS AOR in To MUST have only SIPS Contacts.
- Section 16.7 (Record-Route): Second paragraph deleted.
- Section 19.1: Rewording to clarify TLS on each hop.
- Section 20.43: Replace “session description” with “SIP”; replace “390” with “380”.
- Section 26.2.2: SIPS scheme signifies each hop secured with TLS.
- Section 26.4.4: Several changes: only last sentence of first paragraph replaced; third paragraph first sentence replaced; fourth paragraph deleted; fifth paragraph last sentence reworded to prefer RFC 4474.
- Section 27.2: Remove phrase about SDP failure; replace “390” with “380”.