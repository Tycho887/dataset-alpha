# RFC 2560: X.509 Internet Public Key Infrastructure – Online Certificate Status Protocol – OCSP
**Source**: IETF | **Version**: Standards Track | **Date**: June 1999 | **Type**: Normative  
**Original**: [RFC 2560](https://tools.ietf.org/html/rfc2560)

## Scope (Summary)
This document specifies the Online Certificate Status Protocol (OCSP), which enables applications to determine the revocation state of an identified digital certificate without requiring CRLs. OCSP provides more timely revocation information and additional status data. The protocol defines request/response exchanges between a client and a responder, including signed responses and error handling.

## Normative References
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels (BCP 14, March 1997)
- [RFC2459] – Internet X.509 Public Key Infrastructure Certificate and CRL Profile (January 1999)
- [X.690] – ITU-T X.690 | ISO/IEC 8825-1:1995, ASN.1 encoding rules (BER, CER, DER)
- [HTTP] – RFC 2068, Hypertext Transfer Protocol – HTTP/1.1 (January 1997)
- [URL] – RFC 1738, Uniform Resource Locators (URL) (December 1994)

## Definitions and Abbreviations
- **OCSP**: Online Certificate Status Protocol.
- **OCSP client**: Application that issues status requests to an OCSP responder.
- **OCSP responder**: Server that receives requests and returns signed responses.
- **CA**: Certification Authority that issues certificates.
- **Authorized Responder** (CA Designated Responder): Entity holding a certificate issued by the CA with `extendedKeyUsage` including `id-kp-OCSPSigning`.
- **Trusted Responder**: Responder whose public key is directly trusted by the requester.
- **Request**: `OCSPRequest` ASN.1 structure containing target certificate identifier.
- **Response**: `OCSPResponse` ASN.1 structure, with `responseBytes` of type `id-pkix-ocsp-basic` (BasicOCSPResponse).
- **certStatus**: One of `good`, `revoked`, or `unknown`.
- **thisUpdate**: Time at which status is known to be correct.
- **nextUpdate**: Time at or before which newer information will be available.
- **producedAt**: Time at which the OCSP responder signed the response.
- **nonce**: Cryptographic binding to prevent replay attacks.
- **archive cutoff**: Date obtained by subtracting retention interval from `producedAt`.
- **id-pkix-ocsp**: OID `{id-ad-ocsp}`.
- **id-pkix-ocsp-basic**: OID `{id-pkix-ocsp 1}`.
- **id-kp-OCSPSigning**: OID `{id-kp 9}`.
- **id-pkix-ocsp-nocheck**: OID `{id-pkix-ocsp 5}`.

## 1. Abstract
[Covered in Scope above.]

## 2. Protocol Overview
OCSP enables applications to determine revocation state without CRLs. An OCSP client issues a request to a responder and suspends acceptance of the certificate until receiving a definitive signed response.

### 2.1 Request
An OCSP request contains: protocol version, service request, target certificate identifier, and optional extensions. The responder checks if the request is well‑formed, if service is configured, and if needed info is present; otherwise, it returns an error.

### 2.2 Response
All definitive responses SHALL be digitally signed. The signing key MUST belong to: the issuing CA, a Trusted Responder, or an Authorized Responder. A definitive response includes: version, responder name, per‑certificate responses, optional extensions, signature algorithm OID, and signature.
Per‑certificate response includes: certificate identifier, status value (`good`, `revoked`, `unknown`), validity interval, and optional extensions.
- **good**: Positive response; certificate not revoked (but may not have been issued or be in validity period).
- **revoked**: Certificate revoked (permanently or on hold).
- **unknown**: Responder does not know about the certificate.

### 2.3 Exception Cases
Unsigned error messages may be returned:
- `malformedRequest` (1)
- `internalError` (2)
- `tryLater` (3)
- `sigRequired` (5)
- `unauthorized` (6)

### 2.4 Semantics of thisUpdate, nextUpdate, producedAt
- **thisUpdate**: Time status is known correct.
- **nextUpdate**: Time before which newer info will be available (if absent, newer info is always available).
- **producedAt**: Time responder signed response.

### 2.5 Response Pre-production
Responders MAY pre‑produce signed responses. `thisUpdate` SHALL reflect when status was known correct; `nextUpdate` reflects when newer info will be available; `producedAt` reflects production time.

### 2.6 OCSP Signature Authority Delegation
Explicit delegation: The CA issues a certificate with `id-kp-OCSPSigning` in `extendedKeyUsage`. This certificate MUST be issued directly to the responder by the cognizant CA.

### 2.7 CA Key Compromise
If a responder knows a CA’s private key is compromised, it MAY return `revoked` for all certificates issued by that CA.

## 3. Functional Requirements

### 3.1 Certificate Content
CAs SHALL provide the capability to include the `AuthorityInfoAccess` extension (per [RFC2459] section 4.2.2.1) in certificates. If they support OCSP, they MUST include a `uniformResourceIndicator` URI for `accessLocation` and OID `id-ad-ocsp` for `accessMethod`.

### 3.2 Signed Response Acceptance Requirements
Prior to accepting, OCSP clients SHALL confirm:
1. The certificate identifier in the response matches the request.
2. The signature is valid.
3. The signer’s identity matches the intended recipient.
4. The signer is currently authorized.
5. `thisUpdate` is sufficiently recent.
6. When available, `nextUpdate` is greater than current time.

## 4. Detailed Protocol
ASN.1 imports from [RFC2459]. Data to be signed is DER‑encoded. EXPLICIT tagging is default.

### 4.1 Requests

#### 4.1.1 Request Syntax
```asn1
OCSPRequest     ::= SEQUENCE {
    tbsRequest              TBSRequest,
    optionalSignature [0]   EXPLICIT Signature OPTIONAL }

TBSRequest      ::= SEQUENCE {
    version         [0]     EXPLICIT Version DEFAULT v1,
    requestorName   [1]     EXPLICIT GeneralName OPTIONAL,
    requestList             SEQUENCE OF Request,
    requestExtensions [2]   EXPLICIT Extensions OPTIONAL }

Signature       ::= SEQUENCE {
    signatureAlgorithm  AlgorithmIdentifier,
    signature           BIT STRING,
    certs           [0] EXPLICIT SEQUENCE OF Certificate OPTIONAL }

Version         ::= INTEGER { v1(0) }

Request         ::= SEQUENCE {
    reqCert                 CertID,
    singleRequestExtensions [0] EXPLICIT Extensions OPTIONAL }

CertID          ::= SEQUENCE {
    hashAlgorithm   AlgorithmIdentifier,
    issuerNameHash  OCTET STRING, -- Hash of Issuer's DN (DER)
    issuerKeyHash   OCTET STRING, -- Hash of Issuer's public key (value only)
    serialNumber    CertificateSerialNumber }
```

#### 4.1.2 Notes on Request Syntax
- Using hash of public key avoids name collisions.
- Support for any extension is OPTIONAL; critical flag SHOULD NOT be set.
- Unrecognized extensions MUST be ignored (unless critical and not understood).
- Requestor MAY sign the request; signature computed over `tbsRequest`. If signed, `requestorName` SHALL be specified; certificates MAY be included.

### 4.2 Response Syntax

#### 4.2.1 ASN.1 Specification of OCSP Response
```asn1
OCSPResponse ::= SEQUENCE {
    responseStatus       OCSPResponseStatus,
    responseBytes   [0]  EXPLICIT ResponseBytes OPTIONAL }

OCSPResponseStatus ::= ENUMERATED {
    successful(0), malformedRequest(1), internalError(2), tryLater(3),
    sigRequired(5), unauthorized(6) }

ResponseBytes ::= SEQUENCE {
    responseType   OBJECT IDENTIFIER,
    response       OCTET STRING }

id-pkix-ocsp-basic OBJECT IDENTIFIER ::= { id-pkix-ocsp 1 }

BasicOCSPResponse ::= SEQUENCE {
    tbsResponseData      ResponseData,
    signatureAlgorithm   AlgorithmIdentifier,
    signature            BIT STRING,
    certs            [0] EXPLICIT SEQUENCE OF Certificate OPTIONAL }

ResponseData ::= SEQUENCE {
    version            [0] EXPLICIT Version DEFAULT v1,
    responderID            ResponderID,
    producedAt             GeneralizedTime,
    responses              SEQUENCE OF SingleResponse,
    responseExtensions [1] EXPLICIT Extensions OPTIONAL }

ResponderID ::= CHOICE {
    byName [1] Name,
    byKey  [2] KeyHash }

KeyHash ::= OCTET STRING -- SHA-1 hash of responder's public key

SingleResponse ::= SEQUENCE {
    certID               CertID,
    certStatus           CertStatus,
    thisUpdate           GeneralizedTime,
    nextUpdate      [0]  EXPLICIT GeneralizedTime OPTIONAL,
    singleExtensions [1] EXPLICIT Extensions OPTIONAL }

CertStatus ::= CHOICE {
    good    [0] IMPLICIT NULL,
    revoked [1] IMPLICIT RevokedInfo,
    unknown [2] IMPLICIT UnknownInfo }

RevokedInfo ::= SEQUENCE {
    revocationTime       GeneralizedTime,
    revocationReason [0] EXPLICIT CRLReason OPTIONAL }

UnknownInfo ::= NULL
```

OCSP responders SHALL be capable of producing id-pkix-ocsp-basic responses; clients SHALL be capable of receiving and processing them. The `response` SHALL be DER‑encoded `BasicOCSPResponse`. Signature SHALL be computed on hash of DER‑encoded `ResponseData`.

#### 4.2.2 Notes on OCSP Responses

##### 4.2.2.1 Time
Responses with `nextUpdate` earlier than local time SHOULD be considered unreliable. Responses with `thisUpdate` later than local time SHOULD be considered unreliable. No `nextUpdate` is equivalent to CRL without nextUpdate.

##### 4.2.2.2 Authorized Responders
The signing key SHALL be either the CA’s key or explicitly delegated via `id-kp-OCSPSigning` in the responder’s certificate. This certificate MUST be issued directly by the CA. Systems MUST detect and enforce use of `id-kp-OCSPSigning`. They MUST reject the response if the signing certificate fails one of:
1. Matches local configuration for the certificate in question; or
2. Is the CA certificate; or
3. Contains `id-kp-OCSPSigning` and is issued by the CA.

###### 4.2.2.2.1 Revocation Checking of an Authorized Responder
CAs may choose one of three ways:
- Include `id-pkix-ocsp-nocheck` extension (SHOULD be non‑critical, value NULL) – trust for lifetime of responder certificate.
- Specify CRL Distribution Points or Authority Information Access.
- No method specified – left to client’s local policy.

### 4.3 Mandatory and Optional Cryptographic Algorithms
Clients SHALL process DSA signatures per [RFC2459] section 7.2.2. Clients SHOULD process RSA signatures per [RFC2459] section 7.2.1. Responders SHALL support SHA1.

### 4.4 Extensions
Support for all extensions is OPTIONAL. For each, syntax and processing defined.

#### 4.4.1 Nonce
```asn1
id-pkix-ocsp-nonce OBJECT IDENTIFIER ::= { id-pkix-ocsp 2 }
```
Binds request/response to prevent replay attacks.

#### 4.4.2 CRL References
```asn1
id-pkix-ocsp-crl OBJECT IDENTIFIER ::= { id-pkix-ocsp 3 }
CrlID ::= SEQUENCE {
    crlUrl  [0] EXPLICIT IA5String OPTIONAL,
    crlNum  [1] EXPLICIT INTEGER OPTIONAL,
    crlTime [2] EXPLICIT GeneralizedTime OPTIONAL }
```
Indicates which CRL contains revocation information.

#### 4.4.3 Acceptable Response Types
```asn1
id-pkix-ocsp-response OBJECT IDENTIFIER ::= { id-pkix-ocsp 4 }
AcceptableResponses ::= SEQUENCE OF OBJECT IDENTIFIER
```
Client uses in `requestExtensions` to specify acceptable response OIDs.

#### 4.4.4 Archive Cutoff
```asn1
id-pkix-ocsp-archive-cutoff OBJECT IDENTIFIER ::= { id-pkix-ocsp 6 }
ArchiveCutoff ::= GeneralizedTime
```
Optional extension for historical proof. Value = producedAt minus retention interval.

#### 4.4.5 CRL Entry Extensions
All CRL Entry Extensions from [RFC2459] section 5.3 are supported as `singleExtensions`.

#### 4.4.6 Service Locator
```asn1
id-pkix-ocsp-service-locator OBJECT IDENTIFIER ::= { id-pkix-ocsp 7 }
ServiceLocator ::= SEQUENCE {
    issuer  Name,
    locator AuthorityInfoAccessSyntax OPTIONAL }
```
Used to route requests to authoritative responder.

## 5. Security Considerations
- Fallback to CRL if connection to OCSP cannot be obtained.
- Denial of service from unsigned error responses and signature computation load.
- Precomputed responses allow replay attacks if old good response is replayed before expiration but after revocation.
- Requests lack responder identification, allowing replay to multiple responders.
- HTTP caching may cause unexpected results; implementors should assess cache reliability.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | OCSP responders MUST support id-pkix-ocsp-basic response type. | MUST | 4.2.1 |
| R2 | OCSP clients MUST support id-pkix-ocsp-basic response type. | MUST | 4.2.1 |
| R3 | All definitive response messages SHALL be digitally signed. | SHALL | 2.2 |
| R4 | Signing key MUST belong to CA, Trusted Responder, or Authorized Responder. | MUST | 2.2 |
| R5 | Authorized Responder certificate MUST be issued directly by the cognizant CA. | MUST | 2.6, 4.2.2.2 |
| R6 | CA delegation SHALL be designated by inclusion of id-kp-OCSPSigning in extendedKeyUsage. | SHALL | 4.2.2.2 |
| R7 | OCSP clients SHALL confirm six acceptance criteria before accepting signed response. | SHALL | 3.2 |
| R8 | CAs SHALL provide capability to include AuthorityInfoAccess extension. | SHALL | 3.1 |
| R9 | CAs supporting OCSP MUST include uri accessLocation and OID id-ad-ocsp. | MUST | 3.1 |
| R10 | For signed requests, requestorName SHALL be specified. | SHALL | 4.1.2 |
| R11 | Responders SHALL support SHA1 hashing algorithm. | SHALL | 4.3 |
| R12 | Clients SHALL process DSA signatures; SHOULD process RSA signatures. | SHALL/SHOULD | 4.3 |
| R13 | Unrecognized request extensions with critical flag not set MUST be ignored; if critical and not understood, ignored. | MUST | 4.1.2 |
| R14 | The signature SHALL be computed on hash of DER‑encoded ResponseData. | SHALL | 4.2.1 |
| R15 | The value of `response` in ResponseBytes SHALL be the DER encoding of BasicOCSPResponse. | SHALL | 4.2.1 |
| R16 | Pre‑produced responses SHALL reflect correct time in thisUpdate. | SHALL | 2.5 |

## Informative Annexes (Condensed)
- **Appendix A (OCSP over HTTP)**: Defines HTTP transport. Requests may use GET (if small, <255 bytes) or POST. GET: `GET {url}/{base64url}`. POST: Content‑Type `application/ocsp-request`, body DER. Response: Content‑Type `application/ocsp-response`, body DER. HTTP caching and TLS/SSL may be used.
- **Appendix B (OCSP in ASN.1)**: Complete ASN.1 module with all definitions, object identifiers, and imports from [RFC2459] authentication framework and PKIX modules.
- **Appendix C (MIME Registrations)**: Registers `application/ocsp-request` (file extension .ORQ) and `application/ocsp-response` (file extension .ORS). Both binary; no required parameters. Security considerations note optional signing for requests and mandatory signing for responses.