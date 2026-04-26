# RFC 6960: X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: June 2013 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6960

## Scope (Summary)
Specifies the Online Certificate Status Protocol (OCSP) to determine the current revocation status of digital certificates without requiring Certificate Revocation Lists (CRLs). Provides timely status information and optional extensions. Obsoletes RFC 2560 and RFC 6277; updates RFC 5912.

## Normative References
- RFC 2119: Key words for requirement levels
- RFC 2616: HTTP/1.1
- RFC 3279: Algorithms and Identifiers for PKIX (SHA-1, DSA)
- RFC 3986: URI Generic Syntax
- RFC 4055: Additional RSA Algorithms for PKIX
- RFC 5280: PKIX Certificate and CRL Profile
- RFC 5751: S/MIME Version 3.2 Message Specification
- RFC 6277: OCSP Algorithm Agility
- X.690: ASN.1 encoding rules (BER, CER, DER)

## Definitions and Abbreviations
- **OCSP**: Online Certificate Status Protocol
- **CRL**: Certificate Revocation List
- **CA**: Certificate Authority
- **OCSPRequest**: The request message (ASN.1, signed optionally)
- **OCSPResponse**: The response message (ASN.1, signed)
- **TBSRequest**: To-be-signed request data
- **BasicOCSPResponse**: The mandatory response type
- **CertID**: Certificate identifier (hashAlgorithm, issuerNameHash, issuerKeyHash, serialNumber)
- **ResponderID**: Name or hash of public key of responder
- **SingleResponse**: Status for one certificate (good / revoked / unknown)
- **thisUpdate**: Most recent time status known correct
- **nextUpdate**: Time at or before newer info available
- **producedAt**: Time response was signed
- **revocationTime**: Time of revocation or hold
- **id-pkix-ocsp-basic**: OID for basic response type
- **id-kp-OCSPSigning**: Extended key usage for OCSP signing delegation

## 1. Introduction
Protocol for real-time certificate status checking without CRLs. Key changes from RFC 2560:
- Extended "revoked" state to cover non-issued certificates (§2.2)
- "unauthorized" error for unserved/unauthorized queries (§2.3)
- Responses may include status for certificates not in request (§4.2.1, §4.2.2.3)
- Clarified Authorized Responder (§4.2.2.2)
- Mandatory algorithm changes: RSA with SHA-256 must be supported; RSA with SHA-1 and DSA with SHA-1 should be supported (§4.3)
- Nonce extension ASN.1 syntax added (§4.4.1)
- Preferred Signature Algorithms extension (§4.4.7)
- Extended Revoked Definition extension (§4.4.8)
- New ASN.1 modules for 2008 syntax (§B.2)

### 1.1 Requirements Language
Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per RFC 2119).

## 2. Protocol Overview
OCSP client sends request to responder; responder returns signed status. Three response states: good, revoked, unknown (plus extended use for non-issued certificates).

### 2.1 Request
Request contains: protocol version (v1), service request, target certificate identifiers, optional extensions.

Responder checks: well-formed request, ability to service, sufficient information. On failure, returns error message; on success, definitive signed response.

### 2.2 Response
All definitive responses SHALL be digitally signed. Signing key MUST belong to: issuing CA, Trusted Responder, or Authorized Responder (specially marked certificate).

Response per certificate: target identifier, status (good/revoked/unknown), validity interval, optional extensions.

- **good**: positive response – no revocation of requested serial number within validity interval (does not guarantee issuance or validity at response time).
- **revoked**: certificate revoked temporarily (certificateHold) or permanently. MAY also indicate non-issued certificate (unknown to CA). When used for non-issued certificates, MUST include extended revoked definition extension (§4.4.8), with revocation reason certificateHold (6), revocationTime 1970-01-01, and no CRL references or CRL entry extensions.
- **unknown**: responder has no knowledge (unrecognized issuer).

Note: revoked means reject; unknown allows client to try other sources.

### 2.3 Exception Cases
Unsigned error responses:
- malformedRequest (1)
- internalError (2)
- tryLater (3)
- sigRequired (5)
- unauthorized (6) – also for unauthorized client or incapable server (cf. RFC 5019 §2.2.3)

### 2.4 Semantics of Time Fields
- **thisUpdate**: most recent time status correct
- **nextUpdate**: time at or before newer info available
- **producedAt**: time response signed
- **revocationTime**: time of revocation or hold

### 2.5 Response Pre-Production
Responders MAY pre-produce signed responses. thisUpdate reflects time status correct; nextUpdate reflects future availability; producedAt reflects signing time.

### 2.6 OCSP Signature Authority Delegation
CA explicitly delegates signing by issuing a certificate with extended key usage id-kp-OCSPSigning (OID 1.3.6.1.5.5.7.3.9). Certificate MUST be issued directly by CA.

### 2.7 CA Key Compromise
If responder knows CA's private key compromised, it MAY return "revoked" for all certificates issued by that CA.

## 3. Functional Requirements
### 3.1 Certificate Content
CAs SHALL provide capability to include authority information access extension (per RFC 5280 §4.2.2.1) with accessMethod = id-ad-ocsp and accessLocation = URI. Alternatively, local configuration allowed.

### 3.2 Signed Response Acceptance Requirements
OCSP clients SHALL confirm before accepting response:
1. Certificate in response matches request.
2. Signature is valid.
3. Signer identity matches intended recipient.
4. Signer is currently authorized for the certificate.
5. thisUpdate is sufficiently recent.
6. nextUpdate (when present) is greater than current time.

## 4. Details of the Protocol
ASN.1 syntax imports from RFC 5280. DER encoding used for signature input. EXPLICIT tagging default.

### 4.1 Request Syntax
#### 4.1.1 ASN.1 Specification
```
OCSPRequest ::= SEQUENCE { tbsRequest TBSRequest, optionalSignature [0] EXPLICIT Signature OPTIONAL }
TBSRequest ::= SEQUENCE { version [0] EXPLICIT Version DEFAULT v1, requestorName [1] EXPLICIT GeneralName OPTIONAL, requestList SEQUENCE OF Request, requestExtensions [2] EXPLICIT Extensions OPTIONAL }
Request ::= SEQUENCE { reqCert CertID, singleRequestExtensions [0] EXPLICIT Extensions OPTIONAL }
CertID ::= SEQUENCE { hashAlgorithm AlgorithmIdentifier, issuerNameHash OCTET STRING, issuerKeyHash OCTET STRING, serialNumber CertificateSerialNumber }
Signature ::= SEQUENCE { signatureAlgorithm AlgorithmIdentifier, signature BIT STRING, certs [0] EXPLICIT SEQUENCE OF Certificate OPTIONAL }
Version ::= INTEGER { v1(0) }
```

#### 4.1.2 Notes
- issuerKeyHash: hash over value (excluding tag and length) of subjectPublicKey in issuer's certificate.
- Optional request signing: signature over tbsRequest; requestorName MUST be present when signed; certs field MAY contain helper certificates.
- Extensions MAY be included; critical flag SHOULD NOT be set; unrecognized critical extensions MUST be ignored; unrecognized non-critical extensions ignored.

### 4.2 Response Syntax
#### 4.2.1 ASN.1 Specification
```
OCSPResponse ::= SEQUENCE { responseStatus OCSPResponseStatus, responseBytes [0] EXPLICIT ResponseBytes OPTIONAL }
OCSPResponseStatus ::= ENUMERATED { successful(0), malformedRequest(1), internalError(2), tryLater(3), sigRequired(5), unauthorized(6) }
ResponseBytes ::= SEQUENCE { responseType OBJECT IDENTIFIER, response OCTET STRING }
BasicOCSPResponse ::= SEQUENCE { tbsResponseData ResponseData, signatureAlgorithm AlgorithmIdentifier, signature BIT STRING, certs [0] EXPLICIT SEQUENCE OF Certificate OPTIONAL }
ResponseData ::= SEQUENCE { version [0] EXPLICIT Version DEFAULT v1, responderID ResponderID, producedAt GeneralizedTime, responses SEQUENCE OF SingleResponse, responseExtensions [1] EXPLICIT Extensions OPTIONAL }
ResponderID ::= CHOICE { byName [1] Name, byKey [2] KeyHash }
KeyHash ::= OCTET STRING -- SHA-1 hash of responder's public key
SingleResponse ::= SEQUENCE { certID CertID, certStatus CertStatus, thisUpdate GeneralizedTime, nextUpdate [0] EXPLICIT GeneralizedTime OPTIONAL, singleExtensions [1] EXPLICIT Extensions OPTIONAL }
CertStatus ::= CHOICE { good [0] IMPLICIT NULL, revoked [1] IMPLICIT RevokedInfo, unknown [2] IMPLICIT UnknownInfo }
RevokedInfo ::= SEQUENCE { revocationTime GeneralizedTime, revocationReason [0] EXPLICIT CRLReason OPTIONAL }
UnknownInfo ::= NULL
```
OCSP responders SHALL produce id-pkix-ocsp-basic responses; clients SHALL receive/process that type.

#### 4.2.2 Notes
##### 4.2.2.1 Time
- Responses with nextUpdate earlier than local system time SHOULD be considered unreliable.
- Responses with thisUpdate later than local system time SHOULD be considered unreliable.
- If nextUpdate absent, responder indicates newer revocation info always available.

##### 4.2.2.2 Authorized Responders
- CA MUST either sign responses itself or explicitly designate authority via id-kp-OCSPSigning extended key usage in responder's certificate. Certificate MUST be issued directly by CA (preferably with same issuing key).
- Clients MUST reject response if signing certificate does not meet one of: local config, is the CA's certificate, or has id-kp-OCSPSigning and issued by the CA.
- For backward compatibility with RFC 2560, different issuing key allowed but strongly discouraged.

##### 4.2.2.2.1 Revocation Checking of Authorized Responder
- Option 1: Include id-pkix-ocsp-nocheck extension (non-critical, NULL value). CA should issue short-lived certificate.
- Option 2: Specify CRL distribution points or authority information access for revocation checking.
- Option 3: No method specified; client local policy decides.

##### 4.2.2.3 Basic Response
- ResponseData version MUST be v1 (0).
- ResponderID MUST correspond to signing certificate.
- Response MUST include SingleResponse for each requested certificate. SHOULD NOT include additional SingleResponse except for pre-generation optimization (per RFC 5019 §2.2.1).

### 4.3 Mandatory and Optional Cryptographic Algorithms
Clients MUST be capable of processing responses signed with RSA and SHA-256 (sha256WithRSAEncryption, RFC 4055). Clients SHOULD also be capable of RSA with SHA-1 (sha1WithRSAEncryption, RFC 3279) and DSA with SHA-1 (id-dsa-with-sha1, RFC 3279). Clients MAY support other algorithms.

### 4.4 Extensions
All extensions optional. Syntax details follow.

| Extension | OID | Location | Description |
|-----------|-----|----------|-------------|
| Nonce | id-pkix-ocsp-nonce (2) | requestExtensions or responseExtensions | OCTET STRING; binds request/response to prevent replay |
| CRL References | id-pkix-ocsp-crl (3) | singleExtensions | CrlID: URL, CRL number, or creation time |
| Acceptable Response Types | id-pkix-ocsp-response (4) | requestExtensions | SEQUENCE OF OID; client can accept e.g., id-pkix-ocsp-basic |
| Archive Cutoff | id-pkix-ocsp-archive-cutoff (6) | singleExtensions | GeneralizedTime; cutoff = producedAt minus retention interval |
| CRL Entry Extensions | per RFC 5280 §5.3 | singleExtensions | All CRL entry extensions supported |
| Service Locator | id-pkix-ocsp-service-locator (7) | singleRequestExtensions | Name + AuthorityInfoAccessSyntax; for routing requests |
| Preferred Signature Algorithms | id-pkix-ocsp-pref-sig-algs (8) | requestExtensions | Sequence of (sigIdentifier AlgorithmIdentifier, pubKeyAlgIdentifier OPTIONAL) |
| Extended Revoked Definition | id-pkix-ocsp-extended-revoke (9) | responseExtensions | NULL; indicates responder supports §2.2 extended "revoked" for non-issued certs |

#### 4.4.1 Nonce
```
id-pkix-ocsp-nonce OBJECT IDENTIFIER ::= { id-pkix-ocsp 2 }
Nonce ::= OCTET STRING
```

#### 4.4.2 CRL References
```
id-pkix-ocsp-crl OBJECT IDENTIFIER ::= { id-pkix-ocsp 3 }
CrlID ::= SEQUENCE { crlUrl [0] IA5String OPTIONAL, crlNum [1] INTEGER OPTIONAL, crlTime [2] GeneralizedTime OPTIONAL }
```

#### 4.4.3 Acceptable Response Types
```
id-pkix-ocsp-response OBJECT IDENTIFIER ::= { id-pkix-ocsp 4 }
AcceptableResponses ::= SEQUENCE OF OBJECT IDENTIFIER
```
OCSP responders SHALL be capable of id-pkix-ocsp-basic; clients SHALL receive/process it.

#### 4.4.4 Archive Cutoff
```
id-pkix-ocsp-archive-cutoff OBJECT IDENTIFIER ::= { id-pkix-ocsp 6 }
ArchiveCutoff ::= GeneralizedTime
```

#### 4.4.5 CRL Entry Extensions
All CRL entry extensions from RFC 5280 §5.3 are supported as singleExtensions.

#### 4.4.6 Service Locator
```
id-pkix-ocsp-service-locator OBJECT IDENTIFIER ::= { id-pkix-ocsp 7 }
ServiceLocator ::= SEQUENCE { issuer Name, locator AuthorityInfoAccessSyntax OPTIONAL }
```

#### 4.4.7 Preferred Signature Algorithms
Client MAY include extension; server selects algorithm based on priority: 1) client's preferred list, 2) issuer's CRL signing algorithm, 3) request signing algorithm, 4) out-of-band default, 5) mandatory/recommended algorithm for OCSP version. Responder SHOULD use lowest-numbered selection that is supported and secure.

For static pre-generated responses, use historical data to choose algorithm.

#### 4.4.8 Extended Revoked Definition
```
id-pkix-ocsp-extended-revoke OBJECT IDENTIFIER ::= { id-pkix-ocsp 9 }
```
MUST be present in response when "revoked" for non-issued certificates; MAY be present otherwise. Value NULL. MUST NOT be marked critical. MUST be in responseExtensions (not singleExtensions).

## 5. Security Considerations
- Fallback to CRL processing if OCSP connection fails.
- Denial of service: signed responses consume resources; unsigned errors allow false errors.
- Precomputed responses enable replay attacks; evaluate risk vs benefit.
- Requests lack target responder; can be replayed to multiple responders.
- HTTP caching faults possible.
- For non-issued certificates, use certificateHold reason and random serial numbers to prevent guessing.

### 5.1 Preferred Signature Algorithms
- Signing algorithm SHOULD be at least as secure as original certificate's.
- Client MUST NOT specify insecure algorithms; server MUST NOT sign with insecure algorithms.
- Man-in-the-middle downgrade attack not significant because server must use strong algorithms and client can reject weak responses.
- Denial of service attack surface slightly increased.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Definitive responses SHALL be digitally signed. | shall | §2.2 |
| R2 | Signing key MUST belong to CA, Trusted Responder, or Authorized Responder. | must | §2.2 |
| R3 | "revoked" response for non-issued certificates MUST include extended revoked definition extension. | must | §2.2, §4.4.8 |
| R4 | For non-issued certificates, SingleResponse MUST specify reason certificateHold, revocationTime 1970-01-01, and no CRL references/entry extensions. | must | §2.2 |
| R5 | CAs SHALL provide authority information access with id-ad-ocsp. | shall | §3.1 |
| R6 | Clients SHALL confirm response: cert match, valid signature, authorized signer, current thisUpdate, nextUpdate > current time. | shall | §3.2 |
| R7 | Clients MUST be capable of RSA+SHA-256. | must | §4.3 |
| R8 | Clients SHOULD be capable of RSA+SHA-1 and DSA+SHA-1. | should | §4.3 |
| R9 | OCSP responders SHALL produce id-pkix-ocsp-basic responses; clients SHALL receive/process that type. | shall | §4.2.1, §4.4.3 |
| R10 | Unrecognized critical extensions MUST be ignored. | must | §4.1.2 |
| R11 | RequestorName MUST be present in signed requests. | must | §4.1.2 |
| R12 | ResponderID MUST correspond to signing certificate. | must | §4.2.2.3 |
| R13 | Response MUST include SingleResponse for each requested certificate; SHOULD NOT include extra unless pre-generation optimization. | must, should | §4.2.2.3 |
| R14 | Certificate for Authorized Responder MUST be issued directly by CA and include id-kp-OCSPSigning. | must | §2.6, §4.2.2.2 |
| R15 | Client MUST reject response if signing certificate does not meet acceptance criteria. | must | §4.2.2.2 |
| R16 | For delegation, CA SHOULD use same issuing key as for certificate being checked. | should | §4.2.2.2 |
| R17 | Extended revoked definition extension MUST NOT be marked critical. | must not | §4.4.8 |
| R18 | Extended revoked definition extension when present MUST be in responseExtensions, not singleExtensions. | must | §4.4.8 |
| R19 | Client MUST NOT specify insecure preferred algorithms. | must not | §5.1.1 |
| R20 | Responder MUST NOT sign with insecure algorithms even if client requests. | must not | §5.1.1 |

## Informative Annexes (Condensed)
- **Appendix A: OCSP over HTTP**: Defines request/response formatting using GET or POST methods. GET for small requests (<255 bytes) to enable caching; POST otherwise. Content-Type for request: application/ocsp-request; for response: application/ocsp-response. Response body is DER-encoded OCSPResponse. Provides HTTP header handling.
- **Appendix B: ASN.1 Modules**:
  - B.1: Normative ASN.1 module using 1998 syntax, replacing modules in RFC 2560 and RFC 6277.
  - B.2: Informative ASN.1 module using 2008 syntax, updating RFC 5912. Includes definitions for all OCSP constructs and extensions.
- **Appendix C: MIME Registrations**: Registers media types application/ocsp-request (file extension .ORQ) and application/ocsp-response (file extension .ORS) for OCSP messages over HTTP. Includes security considerations (request may be signed; response is signed).