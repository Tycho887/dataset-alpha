# RFC 3161: Internet X.509 Public Key Infrastructure – Time-Stamp Protocol (TSP)
**Source**: IETF | **Version**: Standards Track | **Date**: August 2001 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc3161

## Scope (Summary)
Defines the format of requests sent to a Time Stamping Authority (TSA) and the responses returned, along with security-relevant operational requirements for TSAs. The protocol supports proof-of-existence for a datum at a specific time and can be used as a building block for non-repudiation services.

## Normative References
- [RFC2119] – Key words for requirement levels (BCP 14)
- [RFC2246] – TLS Protocol v1.0
- [RFC2459] – Internet X.509 PKI Certificate and CRL Profile
- [RFC2510] – Certificate Management Protocols (CMP)
- [CMS] – Cryptographic Message Syntax (RFC 2630)
- [ESS] – Enhanced Security Services for S/MIME (RFC 2634)
- [ISONR] – ISO/IEC 10181-5 Non-Repudiation Framework
- [DSS] – Digital Signature Standard (FIPS 186)
- [MD5] – RFC 1321
- [SHA1] – FIPS 180-1

## Definitions and Abbreviations
- **TSA**: Time Stamping Authority; a Trusted Third Party that creates time-stamp tokens.
- **TimeStampToken (TST)**: A signed data structure (ContentInfo encapsulating SignedData with eContentType id-ct-TSTInfo) containing TSTInfo.
- **TimeStampReq**: The request message from a client to a TSA.
- **TimeStampResp**: The response message from a TSA, containing a status and optionally a TimeStampToken.
- **MessageImprint**: The hash of the datum to be time-stamped, consisting of AlgorithmIdentifier and OCTET STRING.
- **nonce**: A large random number used to verify timeliness of the response.
- **GenTime**: UTC time of token creation, expressed as GeneralizedTime.
- **Accuracy**: Time deviation around genTime, specified in seconds, milliseconds, micros.
- **ordering**: Boolean indicating whether all tokens from the same TSA can be ordered based on genTime regardless of accuracy.
- **ESSCertID**: Certificate identifier used in SigningCertificate attribute.
- **Key words**: MUST, MUST NOT, REQUIRED, SHALL, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per RFC2119).
- **Valid request**: A request that can be decoded correctly, conforms to Section 2.4, and is from a supported TSA subscriber.

## 2. The TSA
The TSA is a TTP that creates time-stamp tokens to indicate that a datum existed at a particular point in time.

### 2.1. Requirements of the TSA
The TSA is **REQUIRED** to:

1. Use a trustworthy source of time.
2. Include a trustworthy time value for each time-stamp token.
3. Include a unique integer for each newly generated time-stamp token.
4. Produce a time-stamp token upon receiving a valid request from the requester, when it is possible.
5. Include within each time-stamp token an identifier to uniquely indicate the security policy under which the token was created.
6. Only time-stamp a hash representation of the datum (a data imprint associated with a one-way collision resistant hash-function uniquely identified by an OID).
7. Examine the OID of the hash function and verify that the hash value length is consistent with the hash algorithm.
8. Not examine the imprint being time-stamped in any way (other than to check its length, as specified in bullet 7).
9. Not include any identification of the requesting entity in the time-stamp tokens.
10. Sign each time-stamp token using a key generated exclusively for this purpose and have this property indicated on the corresponding certificate.
11. Include additional information in the time-stamp token, if asked by the requester using the extensions field, only for extensions that are supported by the TSA. If not possible, the TSA **SHALL** respond with an error message.

### 2.2. TSA Transactions
- Requesting entity sends TimeStampReq; TSA responds with TimeStampResp.
- Upon receiving response, requester **SHALL**:
  - Verify status error; if no error, verify fields of TimeStampToken and digital signature.
  - Verify that what was time-stamped matches the request (data imprint, hash algorithm OID, correct certificate identifier).
  - Verify timeliness: either compare genTime against a local trusted time reference, or verify nonce value. If any verification fails, TimeStampToken **SHALL** be rejected.
- Then **SHOULD** check TSA certificate status (e.g., CRL) and policy field for acceptability.

### 2.3. Identification of the TSA
- TSA **MUST** sign each time-stamp message with a key reserved specifically for that purpose.
- TSA **MAY** have distinct private keys (e.g., for different policies, algorithms, key sizes).
- The corresponding certificate **MUST** contain exactly one instance of extended key usage extension with KeyPurposeID id-kp-timeStamping (critical).
- OID: `id-kp-timeStamping OBJECT IDENTIFIER ::= {iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) kp (3) timestamping (8)}`.

### 2.4. Request and Response Formats

#### 2.4.1. Request Format
- **TimeStampReq** ::= SEQUENCE { version (INTEGER v1(1)), messageImprint (MessageImprint), reqPolicy (TSAPolicyId OPTIONAL), nonce (INTEGER OPTIONAL), certReq (BOOLEAN DEFAULT FALSE), extensions ([0] IMPLICIT Extensions OPTIONAL) }
- **MessageImprint** ::= SEQUENCE { hashAlgorithm (AlgorithmIdentifier), hashedMessage (OCTET STRING) }
  - hashAlgorithm **SHOULD** be a known one-way collision resistant hash algorithm.
  - TSA **SHOULD** check if hash algorithm is "sufficient"; if not recognized or weak, **SHOULD** refuse with pkiStatusInfo 'bad_alg'.
- **reqPolicy**: if present, indicates desired TSA policy (TSAPolicyId OID).
- **nonce**: if included, same value **MUST** be in response; otherwise response rejected.
- **certReq**: if TRUE, TSA's certificate referenced by ESSCertID **MUST** be provided in certificates field of SignedData; if FALSE or absent, certificates field **MUST NOT** be present.
- **extensions**: if an extension is not recognized by the TSA, server **SHALL NOT** issue a token and **SHALL** return failure (unacceptedExtension).
- The time-stamp request does not identify the requester. Alternate identification/authentication means (e.g., CMS, TLS) may be used if needed.

#### 2.4.2. Response Format
- **TimeStampResp** ::= SEQUENCE { status (PKIStatusInfo), timeStampToken (TimeStampToken OPTIONAL) }
- **PKIStatusInfo** ::= SEQUENCE { status (PKIStatus), statusString (PKIFreeText OPTIONAL), failInfo (PKIFailureInfo OPTIONAL) }
- **PKIStatus** ::= INTEGER { granted (0), grantedWithMods (1), rejection (2), waiting (3), revocationWarning (4), revocationNotification (5) }
  - When status = 0 or 1, TimeStampToken **MUST** be present; otherwise **MUST NOT**.
  - Compliant servers **SHOULD NOT** produce other values; compliant clients **MUST** generate error for unknown values.
- **PKIFailureInfo** ::= BIT STRING { badAlg (0), badRequest (2), badDataFormat (5), timeNotAvailable (14), unacceptedPolicy (15), unacceptedExtension (16), addInfoNotAvailable (17), systemFailure (25) }
  - Only these values **SHALL** be supported.
- **statusString** MAY include reason text.
- **TimeStampToken** ::= ContentInfo (contentType id-signedData, content SignedData)
  - eContentType = `id-ct-TSTInfo OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) ct(1) 4}`
  - eContent **SHALL** be DER-encoded TSTInfo.
  - Token **MUST NOT** contain any signatures other than TSA's signature.
  - TSA certificate identifier (ESSCertID) **MUST** be included as a signerInfo attribute inside a SigningCertificate attribute.
- **TSTInfo** ::= SEQUENCE { version (INTEGER v1(1)), policy (TSAPolicyId), messageImprint (MessageImprint – same as in TimeStampReq), serialNumber (INTEGER – up to 160 bits), genTime (GeneralizedTime), accuracy (Accuracy OPTIONAL), ordering (BOOLEAN DEFAULT FALSE), nonce (INTEGER OPTIONAL – present if in req, same value), tsa ([0] GeneralName OPTIONAL), extensions ([1] IMPLICIT Extensions OPTIONAL) }
  - Conforming time-stamping servers **MUST** be able to provide version 1 tokens.
  - Among optional fields, only nonce **MUST** be supported.
  - Conforming requesters **MUST** be able to recognize version 1 tokens with all optional fields present, but not mandated to understand semantics of any extension.
  - policy field: if present in request, **MUST** have same value; otherwise error (unacceptedPolicy).
  - messageImprint: must match similar field in request, provided hash size matches algorithm.
  - serialNumber: unique per TSA, preserved even after interruption.
  - genTime: UTC time, expressed as GeneralizedTime with mandatory seconds; may include fractional seconds. Encoding must follow X.690 DER restrictions: terminates with "Z", decimal point "." if fractional, omit trailing zeros.
  - Accuracy: SEQUENCE { seconds INTEGER OPTIONAL, millis [0] INTEGER (1..999) OPTIONAL, micros [1] INTEGER (1..999) OPTIONAL }. Missing fields default to zero.
  - ordering: if false, ordering possible only if genTime difference > sum of accuracies. If true, tokens from same TSA can always be ordered based on genTime.
  - nonce: must equal request value if present.
  - tsa: if present, must correspond to one of subject names in the certificate used to verify token.
  - extensions: generic mechanism for future additions.

## 3. Transports
No mandatory transport mechanism; optional mechanisms described.

### 3.1. E-mail Transport
- MIME types: `application/timestamp-query` and `application/timestamp-reply`, base64-encoded ASN.1 DER.
- File extensions: `.TSQ` (query) and `.TSR` (reply) recommended when saved.

### 3.2. File Based Protocol
- Files must contain only DER encoding of one TSA message (no extraneous header/trailer).
- Recommended extensions: `.tsq` (request) and `.tsr` (response).

### 3.3. Socket Based Protocol (TCP port 318)
- Protocol defined with direct messages `tsaMsg`, polling messages (`pollReq`, `pollRep`, `negPollRep`, `partialMsgRep`, `finalMsgRep`, `errorMsgRep`).
- Message format: length (32-bit), flag (8-bit), value.
- Supports asynchronous polling with `time-to-check-back` parameter.

### 3.4. HTTP Transport
- MIME objects with content types `application/timestamp-query` and `application/timestamp-reply`.
- Server **MUST** respond with valid response or HTTP error.

## 4. Security Considerations
1. If TSA ceases operation (key not compromised), certificate **SHALL** be revoked with reasonCode unspecified(0), affiliationChanged(3), superseded(4), or cessationOfOperation(5). Tokens before revocation remain valid. If reasonCode absent, all tokens signed with that key considered invalid.
2. If TSA private key compromised, certificate **SHALL** be revoked; reasonCode should be keyCompromise(1). All tokens signed with that key cannot be trusted.
3. TSA signing key **MUST** be of sufficient length for long lifetime; tokens should be re-time-stamped or notarized later to renew trust.
4. Client using only nonce should be concerned about response delay; responses exceeding acceptable period should be considered suspect.
5. Multiple tokens on same data with same hash algorithm produce identical message imprints, allowing inference that time-stamps refer to same data.
6. Replay detection: use of nonce is **RECOMMENDED**. Alternative: local clock and moving time window to detect duplicate hashes.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | TSA must use trustworthy time source | shall | 2.1(1) |
| R2 | TSA must include trustworthy time value in each token | shall | 2.1(2) |
| R3 | TSA must include unique integer per token | shall | 2.1(3) |
| R4 | TSA must produce token upon valid request when possible | shall | 2.1(4) |
| R5 | TSA must include policy identifier in token | shall | 2.1(5) |
| R6 | TSA must only time-stamp hash representation with one-way collision resistant hash | shall | 2.1(6) |
| R7 | TSA must examine OID and verify hash length consistency | shall | 2.1(7) |
| R8 | TSA must not examine imprint (except length check) | shall | 2.1(8) |
| R9 | TSA must not include requester identity in token | shall | 2.1(9) |
| R10 | TSA must sign token with key exclusively for time-stamping; property indicated in certificate | shall | 2.1(10) |
| R11 | TSA must include supported extensions if requested; otherwise respond with error | shall | 2.1(11) |
| R12 | TSA must not produce token for unrecognized extensions | shall | 2.4.1 |
| R13 | Requester must verify status, fields, signature, timeliness of response; reject if any fail | shall | 2.2 |
| R14 | TSA certificate must have extended key usage id-kp-timeStamping (critical) | must | 2.3 |
| R15 | TSA must use key reserved for time-stamping | must | 2.3 |
| R16 | Response token must not contain signatures other than TSA's | must | 2.4.2 |
| R17 | eContent must be DER-encoded TSTInfo | shall | 2.4.2 |
| R18 | Token must include ESSCertID in SigningCertificate attribute | must | 2.4.2 |
| R19 | TSA must support version 1 tokens | must | 2.4.2 |
| R20 | Requester must be able to recognize version 1 tokens with all optional fields | must | 2.4.2 |
| R21 | Policy field in token must match request if present | must | 2.4.2 |
| R22 | serialNumber must be unique per TSA | must | 2.4.2 |
| R23 | nonce field must be present if in request and have same value | must | 2.4.2 |
| R24 | GeneralizedTime must include seconds; encoding must follow X.690 DER | must | 2.4.2 |
| R25 | TSA must respond with valid response or HTTP error over HTTP | must | 3.4 |
| R26 | TSA certificate revocation for cessation must use reasonCode unspecified, affiliationChanged, superseded, or cessationOfOperation | shall | 4(1) |
| R27 | TSA certificate revocation for key compromise must use reasonCode keyCompromise if present | shall | 4(2) |
| R28 | TSA must use private key of sufficient length | must | 4(3) |

## Informative Annexes (Condensed)
- **Annex A – Signature Time-stamp attribute using CMS**: Defines an unsigned attribute `id-aa-timeStampToken` (OID) of type `SignatureTimeStampToken`, which is a `TimeStampToken`. The `messageImprint` is a hash of the `signature` field within `SignerInfo`.
- **Annex B – Placing a Signature At a Particular Point in Time**: Describes a procedure to time-stamp a digital signature soon after signing. Verification involves checking the TST applies to the signature, retrieving the time from the TST, verifying the signer's certificate was valid and not revoked at that time.
- **Annex C – ASN.1 Module using 1988 Syntax**: Provides complete ASN.1 definitions for `TimeStampReq`, `TimeStampResp`, `PKIStatusInfo`, `PKIStatus`, `PKIFailureInfo`, `TimeStampToken`, `TSTInfo`, `Accuracy`, and OIDs.
- **Annex D – Access descriptors for Time-Stamping**: Describes use of Subject Information Access (SIA) extension in TSA certificates with `id-ad-timeStamping` OID to indicate contact method (e.g., HTTP URL). Informative; will be superseded by future PKIX profile.