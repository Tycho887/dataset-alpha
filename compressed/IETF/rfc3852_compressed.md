# RFC 3852: Cryptographic Message Syntax (CMS)
**Source**: IETF | **Version**: Standards Track | **Date**: July 2004 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc3852

## Scope (Summary)
This document specifies the Cryptographic Message Syntax (CMS) for digitally signing, digesting, authenticating, or encrypting arbitrary message content. It defines encapsulation syntax supporting digital signatures, encryption, multiple encapsulations, nested envelopes, and arbitrary attributes (e.g., signing time).

## Normative References
- [ACPROFILE] RFC 3281 – Attribute Certificate Profile
- [PROFILE] RFC 3280 – X.509 PKI Certificate and CRL Profile
- [STDWORDS] RFC 2119 – Key Words
- [X.208-88] CCITT X.208: ASN.1 (1988)
- [X.209-88] CCITT X.209: BER (1988)
- [X.501-88] CCITT X.501: Directory Models (1988)
- [X.509-88] CCITT X.509: Authentication Framework (1988)
- [X.509-97] ITU-T X.509: Authentication Framework (1997)
- [X.509-00] ITU-T X.509: Authentication Framework (2000)

## Definitions and Abbreviations
- **CMS**: Cryptographic Message Syntax
- **BER**: Basic Encoding Rules
- **DER**: Distinguished Encoding Rules
- **MAC**: Message Authentication Code
- **CRL**: Certificate Revocation List
- **UKM**: User Keying Material
- **ACv1/ACv2**: Version 1/2 Attribute Certificate
- **KEM**: Key Encryption Mechanism
- **OID**: Object Identifier
- **AlgorithmIdentifier**: ASN.1 type used for all algorithms (per X.509)
- **ContentType**: ASN.1 type = OBJECT IDENTIFIER
- **CertificateSet**: SET OF CertificateChoices
- **RevocationInfoChoices**: SET OF RevocationInfoChoice (CRL or other)

## 1. Introduction
- CMS provides encapsulation syntax for data protection: digital signatures, encryption, nesting, arbitrary attributes (e.g., signing time, countersignatures).
- Supports certificate-based key management (e.g., PKIX) and algorithm-independent key management.
- CMS values are ASN.1 encoded using BER; typically represented as octet strings. Does not address transmission encoding for unreliable email systems.
- **Evolution**: Derived from PKCS#7 v1.5 (RFC 2315). RFC 2630 added key agreement and symmetric key-encryption keys. RFC 3369 added password-based key management and extension mechanism. This document obsoletes RFC 3369, adds extension mechanism for certificate/revocation formats, and clarifies countersignature.

### 1.2 Terminology
- **MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL** per RFC 2119.

### 1.3 Version Numbers
- Each major data structure includes a version number (first item) to avoid ASN.1 decode errors. Implementations may not check version until decode error.
- Lowest version number supporting the generated syntax is used.

## 2. General Overview
- Defines one protection content: **ContentInfo**.
- Defines six content types: **data, signed-data, enveloped-data, digested-data, encrypted-data, authenticated-data**.
- **Mandatory to implement**: ContentInfo, data, signed-data, enveloped-data. Others MAY be implemented.
- Design philosophy: single-pass processing using indefinite-length BER encoding.
- **Signed attributes and authenticated attributes require DER encoding** (the only data types requiring DER).

## 3. General Syntax (ContentInfo)
- **OID**: `id-ct-contentInfo` {1 2 840 113549 1 9 16 1 6}
- **Syntax**:
  ```asn1
  ContentInfo ::= SEQUENCE {
    contentType ContentType,
    content [0] EXPLICIT ANY DEFINED BY contentType }
  ```
- **contentType**: OID identifying the content type.
- **content**: The associated content. For new content types, SHOULD NOT be a CHOICE type.

## 4. Data Content Type
- **OID**: `id-data` {1 2 840 113549 1 7 1}
- Refers to arbitrary octet strings (e.g., ASCII text). Interpretation left to application.
- S/MIME uses id-data for MIME encoded content (RFC 2311, RFC 3851).
- Generally encapsulated in signed-data, enveloped-data, digested-data, encrypted-data, or authenticated-data.

## 5. Signed-data Content Type
- **OID**: `id-signedData` {1 2 840 113549 1 7 2}
- Consists of content of any type + zero or more signature values. Any number of signers in parallel.
- **Construction steps**:
  1. For each signer: compute message digest on content (or content + signed attributes) using signer-specific digest algorithm.
  2. Digitally sign message digest with signer's private key.
  3. Collect signature and signer-specific info into **SignerInfo**. Collect certificates/CRLs.
  4. Collect digest algorithms, SignerInfos, and content into **SignedData**.
- **Recipient**: independently computes message digest, verifies signature using signer's public key (referenced by issuer+serial or subjectKeyIdentifier).

### 5.1 SignedData Type
```asn1
SignedData ::= SEQUENCE {
  version CMSVersion,
  digestAlgorithms DigestAlgorithmIdentifiers,
  encapContentInfo EncapsulatedContentInfo,
  certificates [0] IMPLICIT CertificateSet OPTIONAL,
  crls [1] IMPLICIT RevocationInfoChoices OPTIONAL,
  signerInfos SignerInfos }
```
- **Version**: Assigned as:
  - 5 if any certificates or CRLs of type "other" are present.
  - 4 if any version 2 attribute certificates present.
  - 3 if any version 1 attribute certificates present OR any SignerInfo version 3 OR eContentType other than id-data.
  - 1 otherwise.
- **digestAlgorithms**: SET OF DigestAlgorithmIdentifier; MAY be zero; listing all digest algorithms used by signers facilitates one-pass verification. Implementations MAY fail to validate signatures using algorithms not in this set.
- **encapContentInfo**: signed content (see 5.2).
- **certificates**: Collection of certificates; may be more or less than needed. The signer's certificate MAY be included. Version 1 attribute certificates strongly discouraged.
- **crls**: Collection of revocation status; may be more or less than needed. CRLs are primary source.
- **signerInfos**: Per-signer info. All implementations MUST gracefully handle unimplemented versions and signature algorithms.

### 5.2 EncapsulatedContentInfo Type
```asn1
EncapsulatedContentInfo ::= SEQUENCE {
  eContentType ContentType,
  eContent [0] EXPLICIT OCTET STRING OPTIONAL }
```
- **eContentType**: OID uniquely specifying content type.
- **eContent**: Content as OCTET STRING; need not be DER encoded.
- Optional omission of eContent for "external signatures". In degenerate case (no signers), eContentType MUST be id-data and eContent MUST be omitted.

### 5.2.1 Compatibility with PKCS#7
- PKCS#7 content field is `[0] EXPLICIT ANY DEFINED BY contentType OPTIONAL` (not OCTET STRING). S/MIME v2 and v3 are compatible because they both wrap MIME content in an OCTET STRING. For non-Data types (e.g., RFC 2634 signed receipt), incompatibility exists: CMS computes digest over entire OCTET STRING value; PKCS#7 over only content value (excluding tag/length).
- **Backward compatibility strategy for processing**: If CMS decode fails, attempt PKCS#7 decode.
- **For creation**: Examine eContentType, adjust expected DER encoding. Example: Microsoft Authenticode (OID 1.3.6.1.4.1.311.2.1.4) uses DER encoded Authenticode signing info.

### 5.3 SignerInfo Type
```asn1
SignerInfo ::= SEQUENCE {
  version CMSVersion,
  sid SignerIdentifier,
  digestAlgorithm DigestAlgorithmIdentifier,
  signedAttrs [0] IMPLICIT SignedAttributes OPTIONAL,
  signatureAlgorithm SignatureAlgorithmIdentifier,
  signature SignatureValue,
  unsignedAttrs [1] IMPLICIT UnsignedAttributes OPTIONAL }
```
- **SignerIdentifier** ::= CHOICE { issuerAndSerialNumber, subjectKeyIdentifier [0] }.
- **version**: 1 if issuerAndSerialNumber; 3 if subjectKeyIdentifier.
- **sid**: signer's certificate identifier. Implementations MUST support reception of both forms. When generating, MAY use one consistently or mix. subjectKeyIdentifier MUST be used for non-X.509 certificates.
- **digestAlgorithm**: Identifies message digest algorithm. SHOULD be among digestAlgorithms in SignedData. Implementations MAY fail to validate if not in set.
- **signedAttrs**: Optional, but MUST be present if eContentType is not id-data. Must be DER encoded. Must contain at minimum:
  - content-type attribute (value = eContentType)
  - message-digest attribute (value = digest of content)
  - (content-type attribute MUST NOT be used in countersignature unsigned attribute.)
- **signatureAlgorithm**: Identifies signature algorithm.
- **signature**: OCTET STRING result of signature.
- **unsignedAttrs**: Optional; countersignature attribute defined in section 11.4.
- **Attribute** ::= SEQUENCE { attrType OID, attrValues SET OF AttributeValue }.

### 5.4 Message Digest Calculation Process
- Initial input: value octets of encapContentInfo eContent OCTET STRING (not tag/length).
- If signedAttrs absent: result is digest of those octets.
- If signedAttrs present: result is digest of DER encoding of the EXPLICIT SET OF value (not the IMPLICIT [0] tag) of the SignedAttributes. The DER encoding includes the SET OF tag, length, and content octets. Since it must contain content-type and message-digest, these are indirectly included.

### 5.5 Signature Generation Process
- Input: result of digest calculation + signer's private key. Algorithm identified by signatureAlgorithm. Signature value encoded as OCTET STRING.

### 5.6 Signature Verification Process
- Input: result of digest calculation + signer's public key. Recipient MAY obtain public key from certificates field or other means. Selection/validation of public key based on certification path validation (beyond scope).
- **Recipient MUST NOT rely on any message digest values computed by originator.** If signedAttrs present, recipient MUST recalculate content digest and compare to messageDigest attribute. For signature to be valid, the values MUST match.
- If signedAttrs present, content-type attribute value MUST match encapContentInfo eContentType.

## 6. Enveloped-data Content Type
- **OID**: `id-envelopedData` {1 2 840 113549 1 7 3}
- Consists of encrypted content of any type + encrypted content-encryption keys for one or more recipients.
- **Construction steps**:
  1. Randomly generate content-encryption key.
  2. Encrypt content-encryption key for each recipient using key transport, key agreement, symmetric key-encryption keys, or passwords.
  3. Collect encrypted key and recipient info into **RecipientInfo**.
  4. Encrypt content with content-encryption key (pad if needed).
  5. Collect RecipientInfos and encrypted content into **EnvelopedData**.
- Recipient decrypts one encrypted content-encryption key, then uses it to decrypt content.

### 6.1 EnvelopedData Type
```asn1
EnvelopedData ::= SEQUENCE {
  version CMSVersion,
  originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
  recipientInfos RecipientInfos,
  encryptedContentInfo EncryptedContentInfo,
  unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL }
```
- **Version**: Assigned as:
  - 4 if originatorInfo present with any certificates/CRLs of type "other".
  - 3 if originatorInfo present with version 2 attribute certificates OR any RecInfo includes pwri or ori.
  - 0 if originatorInfo absent OR unprotectedAttrs absent OR all RecInfo version 0.
  - 2 otherwise.
- **originatorInfo**: Optional; contains certs and CRLs for key management.
- **recipientInfos**: SET SIZE (1..MAX) OF RecipientInfo.
- **encryptedContentInfo**: Identifies content type, encryption algorithm, and encrypted content (optional).
- **unprotectedAttrs**: Optional attributes not encrypted. Useful attributes defined in Section 11.
- Fields ordered for single-pass processing (recipientInfos before encryptedContentInfo).

### 6.2 RecipientInfo Type
```asn1
RecipientInfo ::= CHOICE {
  ktri KeyTransRecipientInfo,
  kari [1] KeyAgreeRecipientInfo,
  kekri [2] KEKRecipientInfo,
  pwri [3] PasswordRecipientInfo,
  ori [4] OtherRecipientInfo }
```
- **Implementations MUST support ktri, kari, kekri.** MAY support pwri and ori.
- All implementations MUST gracefully handle unimplemented alternatives, versions, and ori types.
- **EncryptedKey** ::= OCTET STRING.

#### 6.2.1 KeyTransRecipientInfo
- Transfers CEK to one recipient using key transport.
- **Version**: 0 if rid is issuerAndSerialNumber; 2 if rid is subjectKeyIdentifier.
- **rid**: RecipientIdentifier CHOICE (issuerAndSerialNumber or subjectKeyIdentifier). Recipient certificate must contain key transport public key (keyEncipherment bit if X.509 v3).
- **keyEncryptionAlgorithm**: Identifies algorithm and parameters.
- **encryptedKey**: Result of encrypting CEK.
- Implementations MUST support both rid alternatives for receiving; MUST support at least one for sending.

#### 6.2.2 KeyAgreeRecipientInfo
- Transfers CEK to one or more recipients using same key agreement algorithm and domain parameters.
- **version**: MUST be 3.
- **originator**: CHOICE of issuerAndSerialNumber, subjectKeyIdentifier, or originatorKey (algorithm + public key). OriginatorKey permits anonymity. Implementations MUST support all three.
- **ukm**: Optional UserKeyingMaterial. Implementations MUST accept ukm; if not supporting algorithms that use UKMs, gracefully handle.
- **keyEncryptionAlgorithm**: Identifies algorithm/parameters for encrypting CEK with pairwise key.
- **recipientEncryptedKeys**: SEQUENCE OF RecipientEncryptedKey (each with rid and encryptedKey). rid = KeyAgreeRecipientIdentifier (issuerAndSerialNumber or RecipientKeyIdentifier). Recipient certificate must contain key agreement public key (keyAgreement bit if X.509 v3). Implementations MUST support both rid alternatives.
- **RecipientKeyIdentifier**: Contains subjectKeyIdentifier, optional date, optional other.

#### 6.2.3 KEKRecipientInfo
- Transfers CEK using previously distributed symmetric key-encryption key.
- **version**: MUST be 4.
- **kekid**: KEKIdentifier (keyIdentifier, optional date, optional other).
- **keyEncryptionAlgorithm**: Identifies algorithm.
- **encryptedKey**: Encrypted CEK.

#### 6.2.4 PasswordRecipientInfo
- Transfers CEK using password or shared secret.
- **version**: MUST be 0.
- **keyDerivationAlgorithm**: Optional; if absent, key-encryption key from external source (e.g., smart card).
- **keyEncryptionAlgorithm**: Identifies encryption algorithm.
- **encryptedKey**: Encrypted CEK.
- Per RFC 3211.

#### 6.2.5 OtherRecipientInfo
- For future key management techniques.
- **oriType**: OID identifying technique.
- **oriValue**: Protocol data elements defined by oriType.

### 6.3 Content-encryption Process
- Randomly generate CEK. Pad data if block size >1 using method: pad with k-(lth mod k) octets each with that value (e.g., 01, 02 02, ..., k k ... k). Padding always added; unambiguously removable if k < 256.

### 6.4 Key-encryption Process
- Input to key-encryption algorithm is the value of the CEK (octet string). Any key management technique can be used per recipient.

## 7. Digested-data Content Type
- **OID**: `id-digestedData` {1 2 840 113549 1 7 5}
- Provides content integrity; typically used as input to enveloped-data.
- **Construction**:
  1. Compute message digest on content.
  2. Collect digest algorithm, content, and digest into **DigestedData**.
- Recipient verifies by comparing computed digest.

```asn1
DigestedData ::= SEQUENCE {
  version CMSVersion,
  digestAlgorithm DigestAlgorithmIdentifier,
  encapContentInfo EncapsulatedContentInfo,
  digest Digest }
```
- **Version**: 0 if encapsulated content type is id-data; 2 otherwise.
- **digestAlgorithm**: Identifies digest algorithm.
- **encapContentInfo**: Content to be digested (as in 5.2).
- **digest**: Result of digest.
- Order facilitates single-pass processing.

## 8. Encrypted-data Content Type
- **OID**: `id-encryptedData` {1 2 840 113549 1 7 6}
- Encrypted content without recipients or encrypted CEKs; keys managed by other means.
- Typical application: local storage encryption with password-derived key.

```asn1
EncryptedData ::= SEQUENCE {
  version CMSVersion,
  encryptedContentInfo EncryptedContentInfo,
  unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL }
```
- **Version**: 2 if unprotectedAttrs present; 0 if absent.
- **encryptedContentInfo**: As defined in 6.1.
- **unprotectedAttrs**: Optional attributes not encrypted.

## 9. Authenticated-data Content Type
- **OID**: `id-ct-authData` {1 2 840 113549 1 9 16 1 2}
- Provides integrity using MAC; supports arbitrary number of recipients.
- **Construction**:
  1. Randomly generate message-authentication key.
  2. Encrypt it for each recipient (using RecipientInfo).
  3. For each recipient, collect into RecipientInfo.
  4. Compute MAC on content (or content + authenticated attributes) using authentication key.

### 9.1 AuthenticatedData Type
```asn1
AuthenticatedData ::= SEQUENCE {
  version CMSVersion,
  originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
  recipientInfos RecipientInfos,
  macAlgorithm MessageAuthenticationCodeAlgorithm,
  digestAlgorithm [1] DigestAlgorithmIdentifier OPTIONAL,
  encapContentInfo EncapsulatedContentInfo,
  authAttrs [2] IMPLICIT AuthAttributes OPTIONAL,
  mac MessageAuthenticationCode,
  unauthAttrs [3] IMPLICIT UnauthAttributes OPTIONAL }
```
- **Version**: Assigned as:
  - 3 if originatorInfo present with certificates/CRLs of type "other".
  - 1 if originatorInfo present with version 2 attribute certificates.
  - 0 otherwise.
- **originatorInfo**: Optional, as in EnvelopedData.
- **recipientInfos**: At least one.
- **macAlgorithm**: Identifies MAC algorithm and parameters.
- **digestAlgorithm**: Optional; if present, authAttrs MUST also be present.
- **encapContentInfo**: Content to be authenticated.
- **authAttrs**: Optional. If eContentType is not id-data, authAttrs MUST be present. If present, digestAlgorithm MUST also be present. AuthAttributes MUST be DER encoded. Must contain at minimum:
  - content-type attribute (value = eContentType)
  - message-digest attribute (value = digest of content)
- **mac**: OCTET STRING.
- **unauthAttrs**: Optional; currently no defined attributes.

### 9.2 MAC Generation
- If authAttrs absent: input to MAC is value octets of eContent OCTET STRING (not tag/length).
- If authAttrs present: input to MAC is DER encoding of authAttrs (EXPLICIT SET OF tag, not IMPLICIT [2] tag).
- **Message digest calculation** (when authAttrs present): initial input is value octets of eContent. Result used to compute message-digest attribute.
- MAC algorithm identified by macAlgorithm; value encoded as OCTET STRING.

### 9.3 MAC Verification
- Input: data as per 9.2 + authentication key.
- **Recipient MUST NOT rely on any MAC or message digest values computed by originator.**
- For authentication to succeed, computed MAC must match mac field. If authAttrs present, computed content digest must match message-digest attribute.
- If authAttrs present, content-type attribute value MUST match encapContentInfo eContentType.

## 10. Useful Types

### 10.1 Algorithm Identifier Types
All use AlgorithmIdentifier from X.509.
- **DigestAlgorithmIdentifier** ::= AlgorithmIdentifier (e.g., SHA-1)
- **SignatureAlgorithmIdentifier** ::= AlgorithmIdentifier (e.g., RSA, DSA)
- **KeyEncryptionAlgorithmIdentifier** ::= AlgorithmIdentifier (for key transport, agreement, symmetric, password-derived)
- **ContentEncryptionAlgorithmIdentifier** ::= AlgorithmIdentifier (e.g., Triple-DES, RC2)
- **MessageAuthenticationCodeAlgorithm** ::= AlgorithmIdentifier (e.g., DES-MAC, HMAC-SHA-1)
- **KeyDerivationAlgorithmIdentifier** ::= AlgorithmIdentifier (per RFC 3211)

### 10.2 Other Useful Types
- **RevocationInfoChoices**: SET OF RevocationInfoChoice (crl or other [implicit 1] OtherRevocationInfoFormat). Supports OCSP Responses.
- **CertificateChoices**: CHOICE { certificate (X.509), extendedCertificate (obsolete), v1AttrCert (obsolete), v2AttrCert, other }. Use of PKCS#6 and ACv1 SHOULD NOT be used.
- **CertificateSet**: SET OF CertificateChoices.
- **IssuerAndSerialNumber** ::= SEQUENCE { issuer Name, serialNumber INTEGER }
- **CMSVersion** ::= INTEGER { v0(0), v1(1), v2(2), v3(3), v4(4), v5(5) }
- **UserKeyingMaterial** ::= OCTET STRING
- **OtherKeyAttribute** ::= SEQUENCE { keyAttrId OID, keyAttr ANY DEFINED BY keyAttrId OPTIONAL }

## 11. Useful Attributes

### 11.1 Content Type
- **OID**: `id-contentType` {1 2 840 113549 1 9 3}
- Must be a signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected.
- Attribute value: OBJECT IDENTIFIER (single value).
- In SignedAttributes/AuthAttributes: MUST NOT include multiple instances.

### 11.2 Message Digest
- **OID**: `id-messageDigest` {1 2 840 113549 1 9 4}
- Value: OCTET STRING (single value).
- Must be a signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected.
- Must be present when any signed/authenticated attributes are present.
- In SignedAttributes/AuthAttributes: MUST include only one instance.

### 11.3 Signing Time
- **OID**: `id-signingTime` {1 2 840 113549 1 9 5}
- Value: Time (CHOICE of UTCTime or GeneralizedTime).
- Must be a signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected.
- **Encoding rules**: Dates 1950-2049 use UTCTime (YYMMDDHHMMSSZ). Other dates use GeneralizedTime (YYYYMMDDHHMMSSZ). UTCTime: YY>=50 means 19YY, YY<50 means 20YY. Both MUST use Coordinated Universal Time, include seconds. GeneralizedTime MUST NOT include fractional seconds.
- Single attribute value; MUST NOT have multiple instances.
- No correctness guarantee; acceptance is recipient's discretion.

### 11.4 Countersignature
- **OID**: `id-countersignature` {1 2 840 113549 1 9 6}
- Value: SignerInfo (one or more values).
- Must be an unsigned attribute; MUST NOT be signed, authenticated, unauthenticated, or unprotected.
- Countersigns the contents octets of the signature OCTET STRING (not tag/length).
- **Rules**:
  - signedAttributes of Countersignature MUST NOT contain content-type attribute.
  - signedAttributes MAY contain other attributes, but MUST contain message-digest if any other attributes present.
  - Input to digest: contents octets of DER encoding of the signatureValue field of the SignerInfo being countersigned.
- Multiple instances allowed in UnsignedAttributes.
- Can be nested (countersign a countersignature).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementation MUST implement ContentInfo, data, signed-data, and enveloped-data content types. | MUST | §2 |
| R2 | Content type of EncapsulatedContentInfo being signed MUST be id-data when no signers present. | MUST | §5.2 |
| R3 | If signedAttrs present in SignerInfo, it MUST contain content-type and message-digest attributes. | MUST | §5.3 |
| R4 | SignedAttributes MUST be DER encoded. | MUST | §5.3 |
| R5 | Content-type attribute MUST NOT be used as part of a countersignature unsigned attribute. | MUST | §5.3, §11.1 |
| R6 | Recipient MUST NOT rely on any message digest values computed by originator. | MUST | §5.6 |
| R7 | If signedAttrs present, content-type attribute value MUST match SignedData encapContentInfo eContentType. | MUST | §5.6 |
| R8 | Implementation MUST support both issuerAndSerialNumber and subjectKeyIdentifier forms of SignerIdentifier for reception. | MUST | §5.3 |
| R9 | subjectKeyIdentifier MUST be used to refer to a public key in a non-X.509 certificate. | MUST | §5.3 |
| R10 | Implementation MUST support key transport, key agreement, and previously distributed symmetric key-encryption keys (ktri, kari, kekri). | MUST | §6.2 |
| R11 | For KeyTransRecipientInfo, if rid is subjectKeyIdentifier, version MUST be 2. | MUST | §6.2.1 |
| R12 | For KeyAgreeRecipientInfo, version MUST be 3. | MUST | §6.2.2 |
| R13 | For KEKRecipientInfo, version MUST be 4. | MUST | §6.2.3 |
| R14 | For PasswordRecipientInfo, version MUST be 0. | MUST | §6.2.4 |
| R15 | Implementation MUST accept KeyAgreeRecipientInfo with ukm field. | MUST | §6.2.2 |
| R16 | Implementation MUST support all three originator alternatives for KeyAgreeRecipientInfo. | MUST | §6.2.2 |
| R17 | Implementation MUST support both rid alternatives for KeyAgreeRecipientInfo. | MUST | §6.2.2 |
| R18 | Implementation MUST support both rid alternatives for KeyTransRecipientInfo for reception; at least one for sending. | MUST | §6.2.1 |
| R19 | Content-encryption key MUST be randomly generated. | MUST | §6.3 |
| R20 | Padding algorithm defined if block size >1: pad with k-(lth mod k) octets of value k-(lth mod k). Padding always applied. | MUST | §6.3 |
| R21 | DigestedData version: 0 if id-data; else 2. | MUST | §7 |
| R22 | EncryptedData version: 2 if unprotectedAttrs present; else 0. | MUST | §8 |
| R23 | If authAttrs present in AuthenticatedData, digestAlgorithm MUST also be present. | MUST | §9.1 |
| R24 | If authAttrs present, it MUST contain content-type and message-digest attributes. | MUST | §9.1 |
| R25 | AuthAttributes MUST be DER encoded. | MUST | §9.1 |
| R26 | Recipient MUST NOT rely on any MAC or message digest values computed by originator. | MUST | §9.3 |
| R27 | If authAttrs present, content-type attribute value MUST match AuthenticatedData encapContentInfo eContentType. | MUST | §9.3 |
| R28 | Content-type and message-digest attributes MUST be signed or authenticated attributes; MUST NOT be unsigned, unauthenticated, or unprotected. | MUST | §11.1, §11.2 |
| R29 | Content-type attribute MUST have single attribute value. | MUST | §11.1 |
| R30 | Message-digest attribute MUST have single attribute value. | MUST | §11.2 |
| R31 | Signing-time attribute MUST be signed or authenticated; MUST NOT be unsigned/unauthenticated/unprotected. | MUST | §11.3 |
| R32 | SigningTime: dates 1950-2049 encoded as UTCTime; others as GeneralizedTime. Both MUST include seconds. | MUST | §11.3 |
| R33 | Countersignature MUST be unsigned attribute; MUST NOT be signed/authenticated/unauthenticated/unprotected. | MUST | §11.4 |
| R34 | Countersignature signedAttributes MUST NOT contain content-type attribute. | MUST | §11.4 |
| R35 | Countersignature signedAttributes MUST contain message-digest if any other attributes present. | MUST | §11.4 |
| R36 | Implementation MUST gracefully handle unimplemented versions of SignerInfo, unimplemented signature algorithms, unimplemented RecipientInfo alternatives, unimplemented or unknown ori alternatives. | MUST | §5.1, §6.2, §6.2.5 |
| R37 | The use of version 1 attribute certificates is strongly discouraged. | SHOULD NOT | §5.1, §10.2.2 |
| R38 | PKCS#6 extended certificates and ACv1 SHOULD NOT be used. | SHOULD NOT | §10.2.2 |
| R39 | Message digest algorithm SHOULD be among those listed in digestAlgorithms field of SignedData. | SHOULD | §5.3 |
| R40 | Implementation MAY fail to validate signatures using digest algorithm not in the set. | MAY | §5.1, §5.3 |
| R41 | Implementation MAY support password-based key management (pwri) and any other key management (ori). | MAY | §6.2 |

## Informative Annexes (Condensed)
- **§13.2 Informative References**: Lists RFCs and standards for context (CMS1, CMS2, CMSALG, ESS, MSAC, MSG, OCSP, OLDMSG, PKCS#6, PKCS#7, PKCS#9, PWRI, RANDOM). No normative requirements.
- **§14 Security Considerations**: Discusses protection of private keys, key management keys, CEKs, MAC keys; random number generation; algorithm strength; countersignature risks. Implementers must ensure key-encryption algorithms are as strong or stronger than content-encryption algorithms; must use adequate PRNG.
- **§15 Acknowledgments**: Contributions from IETF S/MIME WG members.
- **§16 Author's Address**: Russell Housley, Vigil Security.
- **§17 Full Copyright Notice**: Standard IETF copyright.

## ASN.1 Modules
- **§12.1**: CMS ASN.1 module (CryptographicMessageSyntax2004) with full definitions.
- **§12.2**: Version 1 Attribute Certificate module (AttributeCertificateVersion1) – deprecated.