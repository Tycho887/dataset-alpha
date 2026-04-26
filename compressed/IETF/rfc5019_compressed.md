# RFC 5019: The Lightweight Online Certificate Status Protocol (OCSP) Profile for High-Volume Environments
**Source**: IETF | **Version**: Standards Track | **Date**: September 2007 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc5019/

## Scope (Summary)
This document defines a profile of OCSP (RFC 2560) addressing scalability for high-volume Public Key Infrastructure (PKI) environments and lightweight scenarios (e.g., mobile, constrained devices). It specifies message profiles, transport via HTTP, and caching recommendations to reduce bandwidth and client-side processing, with normative requirements for both clients and responders.

## Normative References
- [HTTP] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [OCSP] Myers, M., et al., "X.509 Internet Public Key Infrastructure: Online Certificate Status Protocol - OCSP", RFC 2560, June 1999.
- [PKIX] Housley, R., et al., "Internet Public Key Infrastructure - Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- [TLS] Dierks, T. and E. Rescorla, "The Transport Layer Security Protocol Version 1.1", RFC 4346, April 2006.
- [TLSEXT] Blake-Wilson, S., et al., "Transport Layer Security (TLS) Extensions", RFC 4366, April 2006.

## Definitions and Abbreviations
- **OCSP**: Online Certificate Status Protocol (RFC 2560)
- **OCSP responder**: Server that returns certificate status
- **AIA**: authorityInfoAccess extension
- **CRLDP**: cRLDistributionPoints extension
- **NTP**: Network Time Protocol
- **OID**: Object Identifier

## 1. Introduction (Informative)
OCSP is used for certificate status checking (revocation only). Existing deployments often require real-time responses, but high-volume environments (e.g., millions of certificates) and constrained clients (mobile, low bandwidth) need scalability. This profile enables OCSP response pre-production, reduced message size, and caching, permitting interoperability with full OCSP (RFC 2560) clients when out-of-band capability signaling is unavailable.

### 1.1. Requirements Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119].

## 2. OCSP Message Profile

### 2.1. OCSP Request Profile

#### 2.1.1. OCSPRequest Structure
- **R1**: OCSPRequests conformant to this profile MUST include only one Request in the OCSPRequest.RequestList structure.
- **R2**: Clients MUST use SHA1 as the hashing algorithm for CertID.issuerNameHash and CertID.issuerKeyHash.
- **R3**: Clients MUST NOT include the singleRequestExtensions structure.
- **R4**: Clients SHOULD NOT include the requestExtensions structure. If included, this profile RECOMMENDS it contain only the nonce extension (id-pkix-ocsp-nonce). See Section 4 for nonce use in high-volume environments.

#### 2.1.2. Signed OCSPRequests
- **R5**: Clients SHOULD NOT send signed OCSPRequests. Responders MAY ignore the signature on OCSPRequests.
- **R6**: If the OCSPRequest is signed, the client SHALL specify its name in the OCSPRequest.requestorName field; otherwise, clients SHOULD NOT include the requestorName field.
- **R7**: OCSP servers MUST be prepared to receive unsigned OCSP requests that contain the requestorName field, but must realize that the provided value is not authenticated.

### 2.2. OCSP Response Profile

#### 2.2.1. OCSPResponse Structure
- **R8**: Responders MUST generate a BasicOCSPResponse as identified by the id-pkix-ocsp-basic OID.
- **R9**: Clients MUST be able to parse and accept a BasicOCSPResponse.
- **R10**: OCSPResponses conformant to this profile SHOULD include only one SingleResponse in the ResponseData.responses structure, but MAY include additional SingleResponse elements if necessary.
- **R11**: The responder SHOULD NOT include responseExtensions. Clients MUST ignore unrecognized non-critical responseExtensions (per [OCSP]).
- **R12**: If a responder cannot respond to a request containing an unsupported option (e.g., nonce), it SHOULD return the most complete response it can (e.g., without nonce).
- **R13**: Clients SHOULD attempt to process a response even if it does not include a nonce. See Section 4 for freshness validation.
- **R14**: Responders that cannot handle unsupported options MAY forward the request to a capable OCSP responder.
- **R15**: The responder MAY include the singleResponse.singleResponse extensions structure.

#### 2.2.2. Signed OCSPResponses
- **R16**: Clients MUST validate the signature on the returned OCSPResponse.
- **R17**: If signed by a delegate CA, a valid responder certificate MUST be referenced in the BasicOCSPResponse.certs structure.
- **R18**: It is RECOMMENDED that the OCSP responder's certificate contain the id-pkix-ocsp-nocheck extension (per [OCSP]), and that it include neither AIA nor CRLDP extensions. The responder's signing certificate SHOULD be short-lived and renewed regularly.
- **R19**: Clients MUST be able to identify OCSP responder certificates using both byName and byKey choices.
- **R20**: Responders SHOULD use byKey to reduce response size in bandwidth-constrained scenarios.

#### 2.2.3. OCSPResponseStatus Values
- **R21**: When authoritative records are unavailable, the responder MUST return an OCSPResponseStatus of "unauthorized". This extends RFC 2560: "unauthorized" also covers cases where the server is not capable of responding authoritatively (e.g., pre-produced responses, expired certificate records removed).
- **R22**: Responders MAY remove status records of expired certificates to bound database growth; subsequent requests result in "unauthorized".

#### 2.2.4. thisUpdate, nextUpdate, and producedAt
- **R23**: When pre-producing responses, the responder MUST set thisUpdate, nextUpdate, and producedAt as follows:
  - thisUpdate: time at which the status is known to be correct.
  - nextUpdate: time at or before which newer information will be available. Responders MUST always include this value (to aid caching).
  - producedAt: time at which the OCSP response was signed.
- **R24**: ASN.1-encoded GeneralizedTime values MUST be expressed in Zulu (GMT) and MUST include seconds (YYYYMMDDHHMMSSZ). Fractional seconds MUST NOT be used.

## 3. Client Behavior

### 3.1. OCSP Responder Discovery
- **R25**: Clients MUST support the authorityInfoAccess extension (per [PKIX]) and MUST recognize the id-ad-ocsp access method.
- **R26**: If a certificate contains both AIA (OCSP) and CRLDP (CRL), the client SHOULD attempt to contact the OCSP responder first. Clients MAY retrieve the CRL if no OCSPResponse is received after a locally configured timeout and retries.

### 3.2. Sending an OCSP Request
- **R27**: Applications MUST verify the signature of signed data before asking an OCSP client to check certificate status. If invalid or unverifiable, an OCSP check MUST NOT be requested.
- **R28**: An application MUST validate the signature on certificates in a chain before requesting an OCSP check. If invalid or unverifiable, the check MUST NOT be requested.
- **R29**: Clients SHOULD NOT make a request to check the status of expired certificates.

## 4. Ensuring an OCSPResponse Is Fresh
- **R30**: To ensure freshness using time-based mechanisms, both clients and responders MUST have access to an accurate source of time.
- **R31**: Because clients SHOULD NOT include requestExtensions (Section 2.1), clients MUST be able to determine freshness based on an accurate source of time.
- **R32**: Clients that include a nonce in the request SHOULD NOT reject a corresponding OCSPResponse solely on the basis of the nonexistent expected nonce, but MUST fall back to time-based validation.
- **R33**: Clients that do not include a nonce MUST ignore any nonce present in the response.
- **R34**: Clients MUST check for the existence of the nextUpdate field and MUST ensure the current time (GMT, per Section 2.2.4) falls between thisUpdate and nextUpdate. If absent, the client MUST reject the response.
- **R35**: If nextUpdate is present, the client MUST ensure it is not earlier than the current time. If later, the client MUST reject the response as stale. Clients MAY allow a small tolerance for clock differences.

## 5. Transport Profile
- **R36**: The OCSP responder MUST support requests and responses over HTTP.
- **R37**: When sending requests ≤255 bytes total (including scheme, server, base64-encoded request), clients MUST use the GET method (to enable caching). Larger requests SHOULD use POST.
- **R38**: Clients MUST follow A.1.1 of [OCSP] when constructing messages.
- **R39**: For GET, clients MUST base64 encode the OCSPRequest, append to the URI from AIA extension, and properly URL-encode. CR/LF MUST NOT be included.
- **R40**: In response to cachable requests (containing nextUpdate), the responder will include HTTP headers: content-type: application/ocsp-response, content-length, last-modified (producedAt), ETag, expires (nextUpdate), cache-control: max-age=<n>, public, no-transform, must-revalidate, date.

## 6. Caching Recommendations

### 6.1. Caching at the Client
- **R41**: Clients MUST locally cache authoritative OCSP responses (signature validated, status 'successful').
- **R42**: Responders MAY indicate when to fetch updated responses using cache-control:max-age directive. Clients SHOULD fetch on or after max-age. Responders MUST refresh the OCSP response before max-age.

### 6.2. HTTP Proxies
- **R43**: Responders SHOULD set HTTP headers to allow intelligent proxy caching: date, last-modified (thisUpdate), expires (nextUpdate), ETag (RECOMMENDED: ASCII HEX of SHA1 hash of OCSPResponse), cache-control (max-age, public, no-transform, must-revalidate).
- **R44**: OCSP responders MUST NOT include "Pragma: no-cache", "Cache-Control: no-cache", or "Cache-Control: no-store" in authoritative responses.
- **R45**: OCSP responders SHOULD include one or more of these headers in non-authoritative responses.
- **R46**: OCSP clients MUST NOT include a no-cache header in requests unless encountering an expired response possibly due to a proxy caching stale data; then they SHOULD resend with "Pragma: no-cache" or "Cache-Control: no-cache".

### 6.3. Caching at Servers
- **R47**: This profile RECOMMENDS that both TLS clients and servers implement the certificate status request extension mechanism for TLS (per [TLSEXT] Section 3.6).

## 7. Security Considerations

### 7.1. Replay Attacks
- **R48**: To mitigate replay attacks, clients MUST have access to an accurate source of time and ensure responses are sufficiently fresh.
- **R49**: If a client can determine the server supports nonces, it MUST reject a reply without an expected nonce. Otherwise, clients SHOULD NOT reject solely on missing nonce but fall back to time validation.

### 7.2. Man-in-the-Middle Attacks
- **R50**: Clients MUST ensure they are communicating with an authorized responder per [OCSP] Section 4.2.2.2.

### 7.3. Impersonation Attacks
- (Informative summary: signed responses authenticate responder; proper validation required.)

### 7.4. Denial-of-Service Attacks
- (Informative: use unsigned requests may increase attack surface; responders should consider rate limiting.)

### 7.5. Modification of HTTP Headers
- **R51**: Clients SHOULD use HTTP header values (Sections 5, 6) for caching guidance only and ultimately rely on signed OCSPResponse values. Clients SHOULD NOT rely on cached responses beyond nextUpdate.

### 7.6. Request Authentication and Authorization
- (Informative: unsigned requests imply implicit access; alternative mechanisms for environments requiring authorization.)

## Informative Annexes (Condensed)
- **Appendix A. Example OCSP Messages**: Provides ASN.1 hex dumps of a sample OCSP request and response demonstrating the structures conforming to this profile. The examples show SHA1 hash, single request/response, and signing with an OCSP responder certificate containing ocspNoCheck extension.

## Requirements Summary (Key Normative Requirements)
| ID  | Requirement (excerpt) | Type   | Reference |
|-----|------------------------|--------|-----------|
| R1  | Only one Request in RequestList | MUST  | 2.1.1 |
| R2  | Use SHA1 for issuerNameHash and issuerKeyHash | MUST  | 2.1.1 |
| R3  | Do not include singleRequestExtensions | MUST NOT | 2.1.1 |
| R4  | SHOULD NOT include requestExtensions; if included, RECOMMEND only nonce | SHOULD NOT / REC | 2.1.1 |
| R5  | SHOULD NOT send signed requests; responders MAY ignore signature | SHOULD NOT / MAY | 2.1.2 |
| R6  | If signed, SHALL specify requestorName | SHALL | 2.1.2 |
| R7  | Servers MUST accept unsigned requests with requestorName (unauthenticated) | MUST | 2.1.2 |
| R8  | Generate BasicOCSPResponse | MUST | 2.2.1 |
| R9  | Clients MUST parse BasicOCSPResponse | MUST | 2.2.1 |
| R10 | SHOULD include one SingleResponse; MAY add more | SHOULD / MAY | 2.2.1 |
| R11 | Responder SHOULD NOT include responseExtensions; clients MUST ignore unrecognized non-critical | SHOULD NOT / MUST | 2.2.1 |
| R12 | Return most complete response if unsupported option | SHOULD | 2.2.1 |
| R13 | Clients SHOULD process response without nonce | SHOULD | 2.2.1 |
| R14 | Responders MAY forward request | MAY | 2.2.1 |
| R15 | MAY include singleResponse extensions | MAY | 2.2.1 |
| R16 | Clients MUST validate signature on response | MUST | 2.2.2 |
| R17 | Delegate signature: valid responder cert MUST be in certs | MUST | 2.2.2 |
| R18 | RECOMMEND responder cert has ocsp-nocheck and no AIA/CRLDP; SHOULD be short-lived | REC / SHOULD | 2.2.2 |
| R19 | Clients MUST support both byName and byKey | MUST | 2.2.2 |
| R20 | Responders SHOULD use byKey | SHOULD | 2.2.2 |
| R21 | Unauthorized response when no authoritative record | MUST | 2.2.3 |
| R22 | Responders MAY remove expired cert records | MAY | 2.2.3 |
| R23 | Set thisUpdate, nextUpdate, producedAt correctly; MUST always include nextUpdate | MUST | 2.2.4 |
| R24 | GeneralizedTime in GMT with seconds, no fractions | MUST | 2.2.4 |
| R25 | Support AIA extension; recognize id-ad-ocsp | MUST | 3.1 |
| R26 | Prefer OCSP over CRL; MAY fallback | SHOULD / MAY | 3.1 |
| R27 | Verify signature before OCSP check | MUST | 3.2 |
| R28 | Verify certificate chain signature before OCSP check | MUST | 3.2 |
| R29 | SHOULD NOT check expired certificates | SHOULD NOT | 3.2 |
| R30 | Both client and responder MUST have accurate time | MUST | 4 |
| R31 | Clients MUST determine freshness from time (since requestExtensions not sent) | MUST | 4 |
| R32 | Nonce-using clients SHOULD NOT reject on missing nonce; MUST fallback to time | SHOULD NOT / MUST | 4 |
| R33 | If no nonce in request, MUST ignore nonce in response | MUST | 4 |
| R34 | Check nextUpdate exists; current time between thisUpdate and nextUpdate; reject if absent | MUST | 4 |
| R35 | nextUpdate not earlier than current time; reject if later; MAY allow tolerance | MUST / MAY | 4 |
| R36 | Must support HTTP requests/responses | MUST | 5 |
| R37 | Use GET for requests ≤255 bytes; POST for larger | MUST / SHOULD | 5 |
| R38 | Follow [OCSP] A.1.1 for GET/POST | MUST | 5 |
| R39 | Base64 encode, append to URI, URL-encode; no CR/LF | MUST | 5 |
| R40 | Include specific HTTP headers for cachable responses (normative language: "will include") | (normative) | 5 |
| R41 | Clients MUST locally cache authoritative responses | MUST | 6.1 |
| R42 | Responders MUST refresh before max-age; clients SHOULD fetch after | MUST / SHOULD | 6.1 |
| R43 | Responders SHOULD set headers as described | SHOULD | 6.2 |
| R44 | MUST NOT include no-cache/no-store in authoritative responses | MUST NOT | 6.2 |
| R45 | SHOULD include those headers in non-authoritative | SHOULD | 6.2 |
| R46 | Clients MUST NOT include no-cache unless needed; then SHOULD bypass | MUST NOT / SHOULD | 6.2 |
| R47 | RECOMMEND implementing TLS cert status request extension | REC | 6.3 |
| R48 | Clients MUST have accurate time to mitigate replay | MUST | 7.1 |
| R49 | If server known to support nonces, reject missing nonce; else fallback to time | MUST / SHOULD NOT | 7.1 |
| R50 | Clients MUST ensure authorized responder per [OCSP] | MUST | 7.2 |
| R51 | Clients SHOULD use HTTP headers only for caching guidance; not rely beyond nextUpdate | SHOULD / SHOULD NOT | 7.5 |