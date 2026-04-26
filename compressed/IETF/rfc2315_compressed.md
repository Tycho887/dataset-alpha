# RFC 2315: PKCS #7: Cryptographic Message Syntax Version 1.5
**Source**: IETF (Informational) | **Version**: 1.5 | **Date**: March 1998 | **Type**: Informational  
**Original**: https://datatracker.ietf.org/doc/html/rfc2315

## Scope (Summary)
Defines a general syntax for data that may have cryptography applied (digital signatures, digital envelopes). Supports recursion (nesting), arbitrary attributes (e.g., signing time), countersignatures, and a degenerate case for disseminating certificates and CRLs. Compatible with Privacy-Enhanced Mail (PEM).

## Normative References
- FIPS PUB 46-1 (DES, January 1988)
- PKCS #1 (RSA Encryption, Version 1.5, November 1993)
- PKCS #6 (Extended-Certificate Syntax, Version 1.5, November 1993)
- PKCS #9 (Selected Attribute Types, Version 1.1, November 1993)
- RFC 1421 (PEM Part I: Message Encryption and Authentication Procedures, February 1993)
- RFC 1422 (PEM Part II: Certificate-Based Key Management, February 1993)
- RFC 1423 (PEM Part III: Algorithms, Modes, and Identifiers, February 1993)
- RFC 1424 (PEM Part IV: Key Certification and Related Services, February 1993)
- RFC 1319 (MD2 Message-Digest Algorithm, April 1992)
- RFC 1321 (MD5 Message-Digest Algorithm, April 1992)
- X.208 (ASN.1 Specification, 1988)
- X.209 (Basic Encoding Rules for ASN.1, 1988)
- X.500 (Directory: Overview, 1988)
- X.501 (Directory: Models, 1988)
- X.509 (Directory: Authentication Framework, 1988)
- [NIST91] NIST SP 500-202 (Stable Implementation Agreements for OSI Protocols, Version 5, Edition 1, Part 12, December 1991)
- [RSA78] Rivest, Shamir, Adleman, "A method for obtaining digital signatures and public-key cryptosystems," CACM 21(2):120-126, February 1978.

## Definitions and Abbreviations
- **AlgorithmIdentifier**: Type that identifies an algorithm (by OID) and associated parameters (X.509).
- **ASN.1**: Abstract Syntax Notation One (X.208).
- **Attribute**: Type with attribute type (OID) and one or more values (X.501).
- **BER**: Basic Encoding Rules (X.209).
- **Certificate**: Type binding an entity’s distinguished name to a public key with a digital signature (X.509). Contains issuer name, serial number, signature algorithm, validity period.
- **CertificateSerialNumber**: Type uniquely identifying a certificate among those signed by a particular issuer (X.509).
- **CertificateRevocationList (CRL)**: Type with issuer name, issue time, next update, list of revoked serial numbers (RFC 1422).
- **DER**: Distinguished Encoding Rules for ASN.1 (X.509, Section 8.7).
- **DES**: Data Encryption Standard (FIPS PUB 46-1).
- **desCBC**: Object identifier for DES in CBC mode ([NIST91]).
- **ExtendedCertificate**: X.509 certificate plus attributes, collectively signed by issuer (PKCS #6).
- **MD2**: RSA’s MD2 message-digest algorithm (RFC 1319).
- **md2**: Object identifier for MD2 (RFC 1319).
- **MD5**: RSA’s MD5 message-digest algorithm (RFC 1321).
- **md5**: Object identifier for MD5 (RFC 1321).
- **Name**: Type uniquely identifying objects in X.500 directory (X.501).
- **PEM**: Internet Privacy-Enhanced Mail (RFCs 1421-1424).
- **RSA**: RSA public-key cryptosystem ([RSA78]).
- **rsaEncryption**: Object identifier for RSA encryption (PKCS #1).

**Symbols and abbreviations**: None defined in this document.

## General Overview (Section 5)
- The syntax supports six content types: data, signedData, envelopedData, signedAndEnvelopedData, digestedData, encryptedData.
- Content types are either **base** (data) or **enhanced** (the other five, which encapsulate other content via recursion).
- Enhanced types can be prepared in a single pass using indefinite-length BER encoding; processed in a single pass in any BER encoding.
- DER encoding required for signed-data, signed-and-enveloped-data, and digested-data; may require an extra pass when inner content is not data.

## Useful Types (Section 6)
### 6.1 CertificateRevocationLists
```
CertificateRevocationLists ::= SET OF CertificateRevocationList
```
Set of CRLs; may be more or fewer than necessary.

### 6.2 ContentEncryptionAlgorithmIdentifier
```
ContentEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
```
Identifies a content-encryption algorithm (e.g., DES). Encryption/decryption operations.

### 6.3 DigestAlgorithmIdentifier
```
DigestAlgorithmIdentifier ::= AlgorithmIdentifier
```
Identifies a message-digest algorithm (e.g., MD2, MD5).

### 6.4 DigestEncryptionAlgorithmIdentifier
```
DigestEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
```
Identifies a digest-encryption algorithm (e.g., rsaEncryption). Encryption/decryption operations.

### 6.5 ExtendedCertificateOrCertificate
```
ExtendedCertificateOrCertificate ::= CHOICE {
    certificate Certificate,  -- X.509
    extendedCertificate [0] IMPLICIT ExtendedCertificate }
```
Either X.509 or PKCS #6 extended certificate.

### 6.6 ExtendedCertificatesAndCertificates
```
ExtendedCertificatesAndCertificates ::= SET OF ExtendedCertificateOrCertificate
```
Set of certificates; intended to contain chains from a root CA to signers, but may be more or fewer.

### 6.7 IssuerAndSerialNumber
```
IssuerAndSerialNumber ::= SEQUENCE {
    issuer Name,
    serialNumber CertificateSerialNumber }
```
Identifies a certificate by issuer distinguished name and serial number.

### 6.8 KeyEncryptionAlgorithmIdentifier
```
KeyEncryptionAlgorithmIdentifier ::= AlgorithmIdentifier
```
Identifies a key-encryption algorithm (e.g., rsaEncryption). Encryption/decryption of content-encryption keys.

### 6.9 Version
```
Version ::= INTEGER
```
Syntax version number for compatibility.

## General Syntax (Section 7)
- **ContentInfo** is the top-level ASN.1 type for exchanged content:
```
ContentInfo ::= SEQUENCE {
    contentType ContentType,
    content [0] EXPLICIT ANY DEFINED BY contentType OPTIONAL }
ContentType ::= OBJECT IDENTIFIER
```
- Fields:
  - `contentType`: OID indicating type (six defined in Section 14).
  - `content`: Optional; if absent, intended value supplied by other means. Type determined by OID.
- Notes:
  1. Type determined uniquely by OID; must not be CHOICE.
  2. When inner content of signed-data, signed-and-enveloped-data, or digested-data: message digest computed on contents octets of DER encoding of `content` field.
     When inner content of enveloped-data or signed-and-enveloped-data: content-encryption applied to contents octets of definite-length BER encoding of `content` field.
  3. Optional omission of `content` enables external signatures.

## Data Content Type (Section 8)
- **Data** is just an octet string:
```
Data ::= OCTET STRING
```
- Intended to refer to arbitrary octet strings; interpretation left to application.

## Signed-data Content Type (Section 9)
- Consists of content of any type and encrypted message digests for zero or more signers. Degenerate case (no signers) disseminates certificates and CRLs.
- Construction steps:
  1. For each signer: compute message digest on content (with signer-specific algorithm); if authenticated attributes present, digest them along with content.
  2. Encrypt digest and associated info with signer’s private key.
  3. Collect encrypted digest and other info into SignerInfo.
  4. Collect message-digest algorithms, SignerInfo values, certificates, CRLs into SignedData.
- Verification: decrypt encrypted digest with signer’s public key, compare to independently computed digest.

### 9.1 SignedData Type
```
SignedData ::= SEQUENCE {
    version Version,
    digestAlgorithms DigestAlgorithmIdentifiers,
    contentInfo ContentInfo,
    certificates [0] IMPLICIT ExtendedCertificatesAndCertificates OPTIONAL,
    crls [1] IMPLICIT CertificateRevocationLists OPTIONAL,
    signerInfos SignerInfos }
DigestAlgorithmIdentifiers ::= SET OF DigestAlgorithmIdentifier
SignerInfos ::= SET OF SignerInfo
```
- Fields:
  - `version`: **shall** be 1 for this version.
  - `digestAlgorithms`: collection of message-digest algorithm identifiers (any number, including zero).
  - `contentInfo`: content being signed.
  - `certificates`: set of certificates (PKCS #6 extended or X.509); intended to contain chains to signers.
  - `crls`: set of CRLs.
  - `signerInfos`: collection of per-signer information (any number, including zero).
- Notes:
  - DigestAlgorithms before contentInfo and signerInfos after enables single-pass processing.
  - Version 1 differs from version 0: allows zero signers and crls field.
  - In degenerate case (no signers), recommended that content type be data and content field omitted.

### 9.2 SignerInfo Type
```
SignerInfo ::= SEQUENCE {
    version Version,
    issuerAndSerialNumber IssuerAndSerialNumber,
    digestAlgorithm DigestAlgorithmIdentifier,
    authenticatedAttributes [0] IMPLICIT Attributes OPTIONAL,
    digestEncryptionAlgorithm DigestEncryptionAlgorithmIdentifier,
    encryptedDigest EncryptedDigest,
    unauthenticatedAttributes [1] IMPLICIT Attributes OPTIONAL }
EncryptedDigest ::= OCTET STRING
```
- Fields:
  - `version`: **shall** be 1.
  - `issuerAndSerialNumber`: identifies signer’s certificate.
  - `digestAlgorithm`: algorithm for content and authenticated attributes.
  - `authenticatedAttributes`: optional, but **must** be present if content type being signed is not data. If present, **must** contain at least:
    1. PKCS #9 content-type attribute (value = content type).
    2. PKCS #9 message-digest attribute (value = message digest of content).
  - `digestEncryptionAlgorithm`: algorithm for encrypting digest with private key.
  - `encryptedDigest`: result of encryption.
  - `unauthenticatedAttributes`: optional, not signed.
- Notes:
  - Recommendation: omit authenticatedAttributes when content type is data and no other authenticated attributes (PEM compatibility).
  - Version 1 differs from version 0 in digest-encryption process (only PEM-compatible processes differ).

### 9.3 Message-digesting Process
- Initial input: contents octets of DER encoding of `content` field of ContentInfo being signed (only contents octets, not identifier or length).
- When `authenticatedAttributes` absent: result is message digest of content.
- When present: result is message digest of complete DER encoding of the Attributes value (SET OF tag, length, contents). The Attributes value must contain content type and message digest of content.
- Identifier and length octets are protected indirectly: content type included in authenticated attributes or implied by PEM mode.

### 9.4 Digest-encryption Process
- Input: result of message-digesting process and digest algorithm identifier – BER encoded as DigestInfo:
```
DigestInfo ::= SEQUENCE {
    digestAlgorithm DigestAlgorithmIdentifier,
    digest Digest }
Digest ::= OCTET STRING
```
- Encrypt DigestInfo with signer’s private key.
- Notes:
  - Differs from PKCS #1: signatures are octet strings, not bit strings.
  - Typically 30 or fewer octets; RSA with key ≥ 328 bits can encrypt in one block.
  - Including digestAlgorithm limits damage from compromise of one digest algorithm.

### 9.5 Compatibility with Privacy-Enhanced Mail
- MIC-ONLY/MIC-CLEAR compatible when: content type data, no authenticated attributes, digest algorithm md2 or md5, digest-encryption algorithm rsaEncryption. Encrypted message digest matches PEM.

## Enveloped-data Content Type (Section 10)
- Consists of encrypted content and encrypted content-encryption keys for one or more recipients (digital envelopes).
- Construction:
  1. Generate random content-encryption key.
  2. For each recipient: encrypt key with recipient’s public key.
  3. Collect encrypted key and other info into RecipientInfo.
  4. Encrypt content with content-encryption key.
  5. Collect RecipientInfo values and encrypted content into EnvelopedData.
- Recipient opens envelope: decrypt encrypted key with private key, then decrypt content.

### 10.1 EnvelopedData Type
```
EnvelopedData ::= SEQUENCE {
    version Version,
    recipientInfos RecipientInfos,
    encryptedContentInfo EncryptedContentInfo }
RecipientInfos ::= SET OF RecipientInfo
EncryptedContentInfo ::= SEQUENCE {
    contentType ContentType,
    contentEncryptionAlgorithm ContentEncryptionAlgorithmIdentifier,
    encryptedContent [0] IMPLICIT EncryptedContent OPTIONAL }
EncryptedContent ::= OCTET STRING
```
- Fields:
  - `version`: **shall** be 0 for this version.
  - `recipientInfos`: collection of per-recipient info; **must** have at least one element.
  - `encryptedContentInfo`: contentType, contentEncryptionAlgorithm, encryptedContent (optional if supplied by other means).
- Note: order enables single-pass processing.

### 10.2 RecipientInfo Type
```
RecipientInfo ::= SEQUENCE {
    version Version,
    issuerAndSerialNumber IssuerAndSerialNumber,
    keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier,
    encryptedKey EncryptedKey }
EncryptedKey ::= OCTET STRING
```
- Fields:
  - `version`: **shall** be 0.
  - `issuerAndSerialNumber`: identifies recipient’s certificate.
  - `keyEncryptionAlgorithm`: algorithm for encrypting content-encryption key with recipient’s public key.
  - `encryptedKey`: result of encryption.

### 10.3 Content-encryption Process
- Input: contents octets of definite-length BER encoding of `content` field (not identifier or length). Only contents octets encrypted.
- When content type is data: just data value encrypted (compatible with PEM).
- Padding: for algorithms requiring input length multiple of k octets, pad with k - (l mod k) octets of value k - (l mod k). (Well-defined for k < 256.)

### 10.4 Key-encryption Process
- Input: value of content-encryption key (octet string) supplied to recipient’s key-encryption algorithm.

## Signed-and-enveloped-data Content Type (Section 11)
- Combines signed and enveloped data: encrypted content, encrypted keys, doubly encrypted message digests (first encrypted with signer’s private key, then with content-encryption key).
- Construction steps summarized; similar to signed-data and enveloped-data with double encryption.
- Note: The sequential combination of signed-data and enveloped-data is generally preferable except for compatibility with PEM ENCRYPTED process type.

### 11.1 SignedAndEnvelopedData Type
```
SignedAndEnvelopedData ::= SEQUENCE {
    version Version,
    recipientInfos RecipientInfos,
    digestAlgorithms DigestAlgorithmIdentifiers,
    encryptedContentInfo EncryptedContentInfo,
    certificates [0] IMPLICIT ExtendedCertificatesAndCertificates OPTIONAL,
    crls [1] IMPLICIT CertificateRevocationLists OPTIONAL,
    signerInfos SignerInfos }
```
- Fields:
  - `version`: **shall** be 1.
  - `recipientInfos`: **must** have at least one element.
  - `digestAlgorithms`: collection (as in Section 9). Message-digesting process without authenticated attributes.
  - `encryptedContentInfo`: as in Section 10.
  - `certificates`, `crls`: as in Section 9.
  - `signerInfos`: **must** have at least one element; `encryptedDigest` is doubly encrypted.
- Notes: order enables single-pass processing. Version 1 adds crls field; version 0 also acceptable.

### 11.2 Digest-encryption Process
- Two steps: (1) encrypt input (DigestInfo) with signer’s private key; (2) encrypt result with content-encryption key (no DER between steps). Padding may be needed per Section 10.3.
- Compatible with PEM ENCRYPTED process type.

### 11.3 Compatibility with Privacy-Enhanced Mail
- Compatible when: content type data, digest algorithm md2 or md5, content-encryption DES CBC, digest-encryption rsaEncryption, key-encryption rsaEncryption. Doubly encrypted digest and encrypted key match PEM.

## Digested-data Content Type (Section 12)
- Consists of content and its message digest (integrity).
```
DigestedData ::= SEQUENCE {
    version Version,
    digestAlgorithm DigestAlgorithmIdentifier,
    contentInfo ContentInfo,
    digest Digest }
```
- Fields:
  - `version`: **shall** be 0.
  - `digestAlgorithm`: algorithm used.
  - `contentInfo`: content being digested.
  - `digest`: result of message-digesting process (same as Section 9 with no authenticated attributes).
- Note: order enables single-pass processing.

## Encrypted-data Content Type (Section 13)
- Consists of encrypted content without recipients or encrypted keys; key management is external.
```
EncryptedData ::= SEQUENCE {
    version Version,
    encryptedContentInfo EncryptedContentInfo }
```
- Fields:
  - `version`: **shall** be 0.
  - `encryptedContentInfo`: as in Section 10.

## Object Identifiers (Section 14)
- pkcs-7 OID: `{ iso(1) member-body(2) US(840) rsadsi(113549) pkcs(1) 7 }`
- Content type OIDs (under pkcs-7):
  - data: `{ pkcs-7 1 }`
  - signedData: `{ pkcs-7 2 }`
  - envelopedData: `{ pkcs-7 3 }`
  - signedAndEnvelopedData: `{ pkcs-7 4 }`
  - digestedData: `{ pkcs-7 5 }`
  - encryptedData: `{ pkcs-7 6 }`
- Used in contentType field of ContentInfo; content field type corresponds to Data, SignedData, etc.

## Security Considerations
- Security issues are discussed throughout the memo.

## Revision History (Condensed)
- Versions 1.0-1.3: internal drafts (February-March 1991).
- Version 1.4: June 3, 1991 initial public release (NIST/OSI SEC-SIG-91-22).
- Version 1.5: March 1998; substantive changes:
  - Added CertificateRevocationLists type.
  - Revised SignedData syntax: allows CRL dissemination, zero signers.
  - Revised SignerInfo syntax: PEM-compatible digest-encryption per RFC 1423.
  - Clarified DER encoding of authenticatedAttributes.
  - Added padding method for content-encryption.
  - Revised SignedAndEnvelopedData syntax: allows CRLs.
  - Added Encrypted-data content type.
  - Added encryptedData OID.
  - Editorial changes.

## Requirements Summary
| ID  | Requirement | Type   | Reference         |
|-----|-------------|--------|-------------------|
| R1  | ContentInfo.contentType shall be an OBJECT IDENTIFIER | shall | Section 7 |
| R2  | SignedData.version shall be 1 | shall | Section 9.1 |
| R3  | SignerInfo.version shall be 1 | shall | Section 9.2 |
| R4  | If authenticatedAttributes present, must contain content-type and message-digest attributes | must | Section 9.2 |
| R5  | EnvelopedData.version shall be 0 | shall | Section 10.1 |
| R6  | recipientInfos must have at least one element | must | Section 10.1 |
| R7  | RecipientInfo.version shall be 0 | shall | Section 10.2 |
| R8  | SignedAndEnvelopedData.version shall be 1 | shall | Section 11.1 |
| R9  | recipientInfos and signerInfos must each have at least one element | must | Section 11.1 |
| R10 | DigestedData.version shall be 0 | shall | Section 12 |
| R11 | EncryptedData.version shall be 0 | shall | Section 13 |
| R12 | Content-encryption padding: pad with k - (l mod k) octets of value k - (l mod k) | shall | Section 10.3 |

*Note: "must" in original text is interpreted as normative requirement. "shall" is explicit.*