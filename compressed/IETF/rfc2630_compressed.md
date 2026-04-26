# RFC 2630: Cryptographic Message Syntax
**Source**: IETF Network Working Group | **Version**: 1.0 | **Date**: June 1999 | **Type**: Standards Track
**Original**: https://tools.ietf.org/html/rfc2630

## Scope (Summary)
This document defines the Cryptographic Message Syntax (CMS) used to digitally sign, digest, authenticate, or encrypt arbitrary messages. CMS is derived from PKCS #7 v1.5 (RFC 2315) with backward compatibility; changes accommodate attribute certificates and key agreement techniques.

## Normative References
- [PKCS#1] RFC 2313: PKCS #1: RSA Encryption, Version 1.5
- [PKCS#7] RFC 2315: PKCS #7: Cryptographic Message Syntax, Version 1.5
- [PKCS#9] PKCS #9: Selected Attribute Types, Version 1.1
- [X.509-88] CCITT Recommendation X.509: The Directory – Authentication Framework, 1988
- [X.509-97] ITU-T Recommendation X.509: The Directory – Authentication Framework, 1997
- [DH-X9.42] RFC 2631: Diffie-Hellman Key Agreement Method
- [ESS] RFC 2634: Enhanced Security Services for S/MIME
- [MSG] RFC 2633: S/MIME Version 3 Message Specification
- [PROFILE] RFC 2459: Internet X.509 Public Key Infrastructure: Certificate and CRL Profile

Full list in original References section.

## Definitions and Abbreviations
- **ContentInfo**: ASN.1 type that encapsulates a content type identifier and content.
- **CMSVersion**: INTEGER { v0(0), v1(1), v2(2), v3(3), v4(4) } – syntax version number.
- **ContentType**: OBJECT IDENTIFIER identifying the type of content.
- **DigestAlgorithmIdentifier**: AlgorithmIdentifier for message digest algorithms.
- **SignatureAlgorithmIdentifier**: AlgorithmIdentifier for signature algorithms.
- **KeyEncryptionAlgorithmIdentifier**: AlgorithmIdentifier for key encryption algorithms.
- **ContentEncryptionAlgorithmIdentifier**: AlgorithmIdentifier for content encryption algorithms.
- **MessageAuthenticationCodeAlgorithm**: AlgorithmIdentifier for MAC algorithms.
- **SignerIdentifier**: CHOICE of IssuerAndSerialNumber or SubjectKeyIdentifier.
- **RecipientInfo**: CHOICE of KeyTransRecipientInfo, KeyAgreeRecipientInfo, or KEKRecipientInfo.
- **EncryptedKey**: OCTET STRING – the encrypted content-encryption key.
- **OtherKeyAttribute**: SEQUENCE with keyAttrId OID and optional keyAttr.
- **UserKeyingMaterial**: OCTET STRING – used in key agreement.

Additional types defined in Section 10.

## General Syntax (§3)
- **ContentInfo**:
  ```
  ContentInfo ::= SEQUENCE {
    contentType ContentType,
    content [0] EXPLICIT ANY DEFINED BY contentType
  }
  ```
- contentType OID uniquely identifies the content type. Content types defined: data, signed-data, enveloped-data, digested-data, encrypted-data, authenticated-data.

## Data Content Type (§4)
- OID: `id-data` = 1.2.840.113549.1.7.1
- Refers to arbitrary octet strings; no internal structure required.

## Signed-data Content Type (§5)
- OID: `id-signedData` = 1.2.840.113549.1.7.2
- **SignedData**:
  ```
  SignedData ::= SEQUENCE {
    version CMSVersion,
    digestAlgorithms DigestAlgorithmIdentifiers,
    encapContentInfo EncapsulatedContentInfo,
    certificates [0] IMPLICIT CertificateSet OPTIONAL,
    crls [1] IMPLICIT CertificateRevocationLists OPTIONAL,
    signerInfos SignerInfos
  }
  ```
  - version: 1 if no attribute certificates, content type id-data, all SignerInfo version 1; else 3.
  - digestAlgorithms: SET OF DigestAlgorithmIdentifier listing all algorithms used.
  - encapContentInfo: EncapsulatedContentInfo (eContentType, optional eContent).
  - certificates: set of certificates (CertificateChoices – X.509, PKCS#6, attribute certificates). May be absent.
  - crls: set of CRLs. Optional.
  - signerInfos: SET OF SignerInfo (one per signer).
- **EncapsulatedContentInfo**:
  ```
  EncapsulatedContentInfo ::= SEQUENCE {
    eContentType ContentType,
    eContent [0] EXPLICIT OCTET STRING OPTIONAL
  }
  ```
  - eContent absent allows external signatures.
- **SignerInfo**:
  ```
  SignerInfo ::= SEQUENCE {
    version CMSVersion,
    sid SignerIdentifier,
    digestAlgorithm DigestAlgorithmIdentifier,
    signedAttrs [0] IMPLICIT SignedAttributes OPTIONAL,
    signatureAlgorithm SignatureAlgorithmIdentifier,
    signature SignatureValue,
    unsignedAttrs [1] IMPLICIT UnsignedAttributes OPTIONAL
  }
  ```
  - version: 1 if sid is issuerAndSerialNumber; 3 if subjectKeyIdentifier.
  - sid: SignerIdentifier (issuerAndSerialNumber or subjectKeyIdentifier).
  - signedAttrs: must be DER encoded; if present, must include content-type and message-digest attributes (unless countersignature).
  - signedAttrs calculation: when present, message digest is computed on DER encoding of SignedAttributes (using EXPLICIT SET OF tag, not IMPLICIT [0]).
  - unsignedAttrs: optional, e.g., countersignature.
- **Message Digest Calculation Process** (§5.4):
  - Input is octets of eContent (no tag/length). If signedAttrs absent, digest of eContent. If present, digest of DER of SignedAttributes.
- **Signature Generation** (§5.5): signatureAlgorithm OID and signature value.
- **Signature Verification** (§5.6): Recipient obtains signer's public key; must compute message digest; for signedAttrs, must verify messageDigest attribute matches.

## Enveloped-data Content Type (§6)
- OID: `id-envelopedData` = 1.2.840.113549.1.7.3
- **EnvelopedData**:
  ```
  EnvelopedData ::= SEQUENCE {
    version CMSVersion,
    originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
    recipientInfos RecipientInfos,
    encryptedContentInfo EncryptedContentInfo,
    unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL
  }
  ```
  - version: 0 if originatorInfo absent, all RecipientInfo version 0, unprotectedAttrs absent; else 2.
  - originatorInfo: optional, contains certs and crls.
  - recipientInfos: SET OF RecipientInfo (at least one).
  - encryptedContentInfo: EncryptedContentInfo (contentType, contentEncryptionAlgorithm, optional encryptedContent).
  - unprotectedAttrs: optional SET OF Attribute.
- **RecipientInfo**: CHOICE of:
  - **KeyTransRecipientInfo** (§6.2.1):
    ```
    KeyTransRecipientInfo ::= SEQUENCE {
      version CMSVersion,  -- 0 or 2
      rid RecipientIdentifier,
      keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier,
      encryptedKey EncryptedKey
    }
    ```
    - version: 0 if rid is issuerAndSerialNumber; 2 if subjectKeyIdentifier.
  - **KeyAgreeRecipientInfo** (§6.2.2):
    ```
    KeyAgreeRecipientInfo ::= SEQUENCE {
      version CMSVersion,  -- always 3
      originator [0] EXPLICIT OriginatorIdentifierOrKey,
      ukm [1] EXPLICIT UserKeyingMaterial OPTIONAL,
      keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier,
      recipientEncryptedKeys RecipientEncryptedKeys
    }
    ```
    - originator: CHOICE of issuerAndSerialNumber, subjectKeyIdentifier, or originatorKey (algorithm + publicKey).
    - ukm: optional.
    - keyEncryptionAlgorithm includes KeyWrapAlgorithm parameter.
    - recipientEncryptedKeys: SEQUENCE OF RecipientEncryptedKey (rid + encryptedKey).
    - KeyAgreeRecipientIdentifier: CHOICE of issuerAndSerialNumber or RecipientKeyIdentifier (subjectKeyIdentifier, date, other).
  - **KEKRecipientInfo** (§6.2.3):
    ```
    KEKRecipientInfo ::= SEQUENCE {
      version CMSVersion,  -- always 4
      kekid KEKIdentifier,
      keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier,
      encryptedKey EncryptedKey
    }
    ```
    - KEKIdentifier: keyIdentifier, optional date, optional other.
- **Content-encryption Process** (§6.3): Random CEK generated; padding appended to make input a multiple of block size; encrypted with CEK.
- **Key-encryption Process** (§6.4): CEK encrypted for each recipient using one of three techniques.

## Digested-data Content Type (§7)
- OID: `id-digestedData` = 1.2.840.113549.1.7.5
- **DigestedData**:
  ```
  DigestedData ::= SEQUENCE {
    version CMSVersion,
    digestAlgorithm DigestAlgorithmIdentifier,
    encapContentInfo EncapsulatedContentInfo,
    digest Digest
  }
  ```
  - version: 0 if encapsulated content type is id-data; else 2.
  - digest: OCTET STRING, result of message digesting (same as §5.4 without signed attributes).

## Encrypted-data Content Type (§8)
- OID: `id-encryptedData` = 1.2.840.113549.1.7.6
- **EncryptedData**:
  ```
  EncryptedData ::= SEQUENCE {
    version CMSVersion,
    encryptedContentInfo EncryptedContentInfo,
    unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL
  }
  ```
  - version: 0 if unprotectedAttrs absent; else 2.
  - encryptedContentInfo same as §6.1.

## Authenticated-data Content Type (§9)
- OID: `id-ct-authData` = 1.2.840.113549.1.9.16.1.2
- **AuthenticatedData**:
  ```
  AuthenticatedData ::= SEQUENCE {
    version CMSVersion,  -- always 0
    originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
    recipientInfos RecipientInfos,
    macAlgorithm MessageAuthenticationCodeAlgorithm,
    digestAlgorithm [1] DigestAlgorithmIdentifier OPTIONAL,
    encapContentInfo EncapsulatedContentInfo,
    authenticatedAttributes [2] IMPLICIT AuthAttributes OPTIONAL,
    mac MessageAuthenticationCode,
    unauthenticatedAttributes [3] IMPLICIT UnauthAttributes OPTIONAL
  }
  ```
  - version: 0.
  - macAlgorithm: identifies MAC algorithm.
  - digestAlgorithm: optional; if present, authenticatedAttributes must be present.
  - authenticatedAttributes: optional; if present must include content-type and message-digest attributes.
  - mac: OCTET STRING.
  - unauthenticatedAttributes: optional.
- **MAC Generation** (§9.2):
  - If authenticatedAttributes absent: input is eContent OCTET (no tag/length).
  - If present: input is DER encoding of authenticatedAttributes (using EXPLICIT SET OF tag). Message digest computed on eContent; then input to MAC is authenticatedAttributes value.
- **MAC Verification** (§9.3): Recipient must compute MAC and compare; if authenticatedAttributes present, also verify message-digest.

## Useful Types (§10)
### Algorithm Identifier Types (§10.1)
- DigestAlgorithmIdentifier, SignatureAlgorithmIdentifier, KeyEncryptionAlgorithmIdentifier, ContentEncryptionAlgorithmIdentifier, MessageAuthenticationCodeAlgorithm: all defined as AlgorithmIdentifier.
### Other Useful Types (§10.2)
- **CertificateRevocationLists**: SET OF CertificateList.
- **CertificateChoices**: CHOICE of Certificate, extendedCertificate (obsolete), attrCert.
- **CertificateSet**: SET OF CertificateChoices.
- **IssuerAndSerialNumber**: SEQUENCE of issuer Name and serialNumber CertificateSerialNumber.
- **CMSVersion**: INTEGER { v0(0), v1(1), v2(2), v3(3), v4(4) }.
- **UserKeyingMaterial**: OCTET STRING.
- **OtherKeyAttribute**: SEQUENCE { keyAttrId OID, keyAttr ANY DEFINED BY keyAttrId OPTIONAL }.

## Useful Attributes (§11)
- **Content Type** (§11.1): OID `id-contentType` = 1.2.840.113549.1.9.3. Must be signed or authenticated attribute; single value; must not appear multiple times.
- **Message Digest** (§11.2): OID `id-messageDigest` = 1.2.840.113549.1.9.4. Must be signed or authenticated attribute; single value; required if any signed/authenticated attributes present.
- **Signing Time** (§11.3): OID `id-signingTime` = 1.2.840.113549.1.9.5. Signed attribute only. UTCTime for years 1950-2049, GeneralizedTime otherwise; must be Zulu; include seconds. No multiple instances.
- **Countersignature** (§11.4): OID `id-countersignature` = 1.2.840.113549.1.9.6. Unsigned attribute only; value is SignerInfo; may appear multiple times. Input to message digest is signatureValue of original SignerInfo.

## Supported Algorithms (§12)
### Digest Algorithms (§12.1)
- **Must implement**: SHA‑1 (OID 1.3.14.3.2.26). Parameters optional, if present NULL.
- **Should implement**: MD5 (OID 1.2.840.113549.2.5). Parameters must be NULL.
### Signature Algorithms (§12.2)
- **Must implement**: DSA with SHA‑1 (OID 1.2.840.10040.4.3). Parameters absent.
- **May implement**: RSA (OID 1.2.840.113549.1.1.1) with SHA‑1 or MD5.
### Key Management Algorithms (§12.3)
- **Key Agreement**: Must include X9.42 Ephemeral-Static Diffie-Hellman (OID `dh-public-number` 1.2.840.10046.2.1). KeyEncryptionAlgorithm uses `id-alg-ESDH` (OID 1.2.840.113549.1.9.16.3.5) with KeyWrapAlgorithm parameter.
- **Key Transport**: Should include RSA (OID 1.2.840.113549.1.1.1). Must include transport of Triple‑DES keys; should include RC2. Parameters must be NULL.
- **Symmetric Key-Encryption Keys**: May include; if so, must include Triple‑DES key wrap (OID `id-alg-CMS3DESwrap` 1.2.840.113549.1.9.16.3.6) and should include RC2 key wrap (OID `id-alg-CMSRC2wrap` 1.2.840.113549.1.9.16.3.7). RC2 key‑encryption keys must be 128-bit (rc2ParameterVersion = 58).
### Content Encryption Algorithms (§12.4)
- **Must implement**: Triple‑DES CBC (OID 1.2.840.113549.3.7). Parameters: IV (8 octets).
- **Should implement**: RC2 CBC (OID 1.2.840.113549.3.2). Parameters: RC2CBCParameter (rc2ParameterVersion + IV 8 octets).
### Message Authentication Code Algorithms (§12.5)
- **Must implement** (if authenticatedData supported): HMAC with SHA‑1 (OID 1.3.6.1.5.5.8.1.2). Parameters absent.
### Key Wrap Algorithms (§12.6)
- **Triple‑DES Key Wrap** (§12.6.2): Compute checksum using SHA‑1 (first 8 octets). Wrap structure: CEK (24 octets) || ICV (8 octets). Encrypt in CBC with random IV, then reverse octets, then encrypt again with fixed IV 0x4adda22c79e82105. Unwrap described in §12.6.3.
- **RC2 Key Wrap** (§12.6.4): Prepend length octet, pad to multiple of 8, compute checksum, wrap similarly. Unwrap in §12.6.5.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Implementations must support ContentInfo, data, signed-data, and enveloped-data content types. | must | §2 |
| R2 | Signed attributes and authenticated attributes must be DER encoded. | must | §2 |
| R3 | SignedData version shall be 1 (if no attr certs, id-data, all SignerInfo v1) or 3 otherwise. | shall | §5.1 |
| R4 | SignerInfo version shall be 1 if issuerAndSerialNumber, 3 if subjectKeyIdentifier. | shall | §5.3 |
| R5 | If signedAttributes present, they must contain content-type and message-digest attributes (except countersignature). | must | §5.3 |
| R6 | EnvelopedData version shall be 0 (if no originatorInfo, all RecipientInfo v0, no unprotectedAttrs) or 2 otherwise. | shall | §6.1 |
| R7 | KeyTransRecipientInfo version shall be 0 (issuerAndSerialNumber) or 2 (subjectKeyIdentifier). | shall | §6.2.1 |
| R8 | KeyAgreeRecipientInfo version shall always be 3. | shall | §6.2.2 |
| R9 | KEKRecipientInfo version shall always be 4. | shall | §6.2.3 |
| R10 | DigestedData version shall be 0 (if id-data) or 2 otherwise. | shall | §7 |
| R11 | EncryptedData version shall be 0 (if no unprotectedAttrs) or 2 otherwise. | shall | §8 |
| R12 | AuthenticatedData version shall be 0. | shall | §9.1 |
| R13 | If authenticatedAttributes present, digestAlgorithm must also be present. | must | §9.1 |
| R14 | If authenticatedAttributes present, content-type and message-digest attributes must be included. | must | §9.1 |
| R15 | Digest algorithms: must implement SHA‑1, should implement MD5. | must/should | §12.1 |
| R16 | Signature algorithms: must implement DSA with SHA‑1, may implement RSA. | must/may | §12.2 |
| R17 | Key agreement: must implement X9.42 Ephemeral-Static Diffie-Hellman. | must | §12.3.1 |
| R18 | Key transport: should implement RSA; must support Triple‑DES content-encryption keys. | should/must | §12.3.2 |
| R19 | Content encryption: must implement Triple‑DES CBC; should implement RC2 CBC. | must/should | §12.4 |
| R20 | MAC algorithm (if supporting authenticatedData): must implement HMAC with SHA‑1. | must | §12.5 |
| R21 | Content-encryption key must be randomly generated. | must | §6.3, Security Considerations |
| R22 | Key-encryption algorithm should be as strong as or stronger than content-encryption algorithm. | should | Security Considerations |

## Informative Annexes (Condensed)
- **Appendix A: ASN.1 Module** – Provides full ASN.1 definitions for all CMS types, including ContentInfo, SignedData, EnvelopedData, DigestedData, EncryptedData, AuthenticatedData, RecipientInfo, SignerInfo, attribute types, algorithm identifiers, and parameter types. Also includes obsolete ExtendedCertificate from PKCS#6.
- **Security Considerations** – Emphasizes protection of private keys, random generation of keys/IVs, strength alignment between key management and content encryption, vulnerability of PKCS#1 v1.5 to adaptive chosen ciphertext attacks (mitigation via OAEP recommended in interactive environments), and the need for modular algorithm support.