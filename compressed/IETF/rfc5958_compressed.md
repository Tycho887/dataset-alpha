# RFC 5958: Asymmetric Key Packages
**Source**: IETF | **Version**: Standards Track | **Date**: August 2010 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc5958

## Scope (Summary)
Defines the syntax for private-key information (OneAsymmetricKey) and a CMS content type (AsymmetricKeyPackage) for transferring plaintext asymmetric keys. Obsoletes RFC 5208 (PKCS #8 v1.2).

## Normative References
- [RFC2119](https://tools.ietf.org/html/rfc2119) – Key words for use in RFCs
- [RFC4648](https://tools.ietf.org/html/rfc4648) – Base16, Base32, and Base64 Data Encodings
- [RFC5652](https://tools.ietf.org/html/rfc5652) – Cryptographic Message Syntax (CMS)
- [RFC5911](https://tools.ietf.org/html/rfc5911) – New ASN.1 Modules for CMS and S/MIME
- [RFC5912](https://tools.ietf.org/html/rfc5912) – New ASN.1 Modules for PKIX
- [X.680](https://www.itu.int/rec/T-REC-X.680) – ASN.1
- [X.681](https://www.itu.int/rec/T-REC-X.681) – ASN.1 Information Object Specification
- [X.682](https://www.itu.int/rec/T-REC-X.682) – ASN.1 Constraint Specification
- [X.683](https://www.itu.int/rec/T-REC-X.683) – ASN.1 Parameterization
- [X.690](https://www.itu.int/rec/T-REC-X.690) – ASN.1 encoding rules (BER, CER, DER)

## Definitions and Abbreviations
- **AsymmetricKeyPackage**: SEQUENCE SIZE (1..MAX) OF OneAsymmetricKey; CMS content type for transferring keys.
- **OneAsymmetricKey**: SEQUENCE containing version, privateKeyAlgorithm, privateKey, optional attributes, optional publicKey. Renamed from PrivateKeyInfo [RFC5208].
- **PrivateKeyInfo**: Alias for OneAsymmetricKey (backwards compatible).
- **EncryptedPrivateKeyInfo**: SEQUENCE of encryptionAlgorithm and encryptedData.
- **Version**: INTEGER { v1(0), v2(1) }. If publicKey present → v2, else v1.
- **PrivateKeyAlgorithmIdentifier**: AlgorithmIdentifier restricted to PUBLIC-KEY and PrivateKeyAlgorithms.
- **PrivateKey**: OCTET STRING (content algorithm-specific).
- **PublicKey**: BIT STRING (optional, content algorithm-specific).
- **Attributes**: SET OF Attribute { OneAsymmetricKeyAttributes } (open set, may support [RFC2985]).
- **EncryptionAlgorithmIdentifier**: AlgorithmIdentifier restricted to CONTENT-ENCRYPTION and KeyEncryptionAlgorithms.
- **EncryptedData**: OCTET STRING (encrypted PrivateKeyInfo).

## 1. Introduction
Defines syntax for private-key information and CMS content type. CMS can digitally sign, digest, authenticate, or encrypt the content type. Obsoletes PKCS #8 v1.2 [RFC5208].

### 1.1. Requirements Terminology
The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

### 1.2. ASN.1 Syntax Notation
Key package defined using ASN.1 [X.680], [X.681], [X.682], [X.683].

### 1.3. Summary of Updates to RFC 5208
- Renamed PrivateKeyInfo to OneAsymmetricKey to reflect addition of publicKey field.
- Defined Asymmetric Key Package CMS content type.
- Removed redundant IMPLICIT from attributes.
- Added publicKey to OneAsymmetricKey; updated version number.
- Added that PKCS #9 attributes may be supported; added discussion of compatibility with other private-key formats.
- Added requirements for encoding rule set; changed imports to [RFC5912], [RFC5911]; replaced ALGORITHM-IDENTIFIER with ALGORITHM.
- Registers application/pkcs8 media type and .p8 file extension.

## 2. Asymmetric Key Package CMS Content Type
- **ct-asymmetric-key-package**: OID { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) dod(2) infosec(1) formats(2) key-package-content-types(78) 5 }.
- **AsymmetricKeyPackage** ::= SEQUENCE OF OneAsymmetricKey (at least 1).
- **OneAsymmetricKey** fields (normative):
  - **version**: if publicKey present → v2, else v1.
  - **privateKeyAlgorithm**: identifies algorithm; OID and optional parameters.
  - **privateKey**: OCTET STRING; interpretation per algorithm registration (e.g., DSA: INTEGER, RSA: RSAPrivateKey, ECC: ECPrivateKey).
  - **attributes** [0] OPTIONAL: information corresponding to public key; constrained by OneAsymmetricKeyAttributes; may support attributes from [RFC2985].
  - **publicKey** [1] OPTIONAL: BIT STRING; structure depends on algorithm (e.g., DSA: INTEGER, RSA: included in RSAPrivateKey, ECC: included in ECPrivateKey).
- **Encoding**: Generators SHOULD use DER [X.690]; receivers MUST support BER [X.690] (which includes DER).

## 3. Encrypted Private Key Info
- **EncryptedPrivateKeyInfo** ::= SEQUENCE {
    encryptionAlgorithm  EncryptionAlgorithmIdentifier,
    encryptedData        EncryptedData }
- **EncryptionAlgorithmIdentifier**: AlgorithmIdentifier restricted to CONTENT-ENCRYPTION and KeyEncryptionAlgorithms.
- **EncryptedData**: OCTET STRING (encrypted PrivateKeyInfo).
- **Encryption process** (normative steps):
  1. Encode PrivateKeyInfo (SHOULD use DER; receivers MUST support BER).
  2. Encrypt resulting octet string with secret key.

## 4. Protecting the AsymmetricKeyPackage
CMS protecting content types [RFC5652], [RFC5083] can be used:
- **SignedData**: digital signature.
- **EncryptedData**: symmetric encryption (pre-shared key).
- **EnvelopedData**: symmetric encryption (key management similar to EnvelopedData).
- **AuthenticatedData**: MAC protection.
- **AuthEnvelopedData**: authenticated encryption.

## 5. Other Private-Key Format Considerations
- **PKCS #12 (P12)**: Carries OneAsymmetricKey/PrivateKeyInfo in keyBag; EncryptedPrivateKeyInfo in pkcs8ShroudedKeyBag. File extensions .pfx and .p12 interchangeable.
- **Microsoft .pvk**: Proprietary; not interchangeable with P12, but conversion tools exist.
- **Extraction**: Remove outer ContentInfo and any protecting layers (SignedData, etc.). Removing security layers invalidates signatures and may expose key.
- **PEM encoding**: Base64 of DER-encoded EncryptedPrivateKeyInfo between `-----BEGIN ENCRYPTED PRIVATE KEY-----`/`-----END ENCRYPTED PRIVATE KEY-----`; similarly for PrivateKeyInfo with `-----BEGIN PRIVATE KEY-----`. File extension .pem when PEM-encoded; .p8 for binary DER.

## 6. Security Considerations
- Disclosure of private-key material can lead to masquerades.
- Encryption algorithm MUST be as strong as the key it protects.
- Asymmetric key package contents are not protected; may be combined with security protocol.

## 7. IANA Considerations
- OIDs for CMS content type (DoD arc) and ASN.1 module (RSADSI/SMIME arc) registered – no further IANA action.
- **Media subtype application/pkcs8** registered:
  - Type: application; Subtype: pkcs8.
  - Required parameters: None; Optional: None.
  - Encoding: binary.
  - Security considerations: Carries private key; see Section 6.
  - Interoperability: Object MUST be DER-encoded PrivateKeyInfo.
  - Published spec: RFC 5958.
  - File extension: .p8.
  - Change controller: IESG.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Generators SHOULD use DER, receivers MUST support BER for AsymmetricKeyPackage encoding. | SHOULD / MUST | Section 2 |
| R2 | EncryptedPrivateKeyInfo shall have ASN.1 type EncryptedPrivateKeyInfo. | SHALL | Section 3 |
| R3 | Generators SHOULD use DER, receivers MUST support BER for private-key information encoding in encryption step. | SHOULD / MUST | Section 3 |
| R4 | The PKCS #8 object in application/pkcs8 media type MUST be DER-encoded PrivateKeyInfo. | MUST | Section 7.1 |
| R5 | If publicKey is present in OneAsymmetricKey, version MUST be v2; otherwise version SHOULD be v1. | MUST / SHOULD | Section 2 (ASN.1 comment) |
| R6 | Encryption algorithm MUST be as strong as the key it protects. | MUST | Section 6 |
| R7 | AsymmetricKeyPackage MAY be encapsulated in one or more CMS protecting content types. | MAY | Section 2 |
| R8 | Attributes from [RFC2985] MAY be supported. | MAY | Section 2 |

## Informative Annexes (Condensed)
- **Appendix A (ASN.1 Module)**: Normative ASN.1 definitions (AsymmetricKeyPackageModuleV1) using IMPLICIT TAGS. Exports all. Includes ct-asymmetric-key-package, OneAsymmetricKey, PrivateKeyInfo, EncryptedPrivateKeyInfo, and supporting object sets (PrivateKeyAlgorithms, KeyEncryptionAlgorithms). An alternate constrained representation is shown but commented out.
- **Acknowledgements**: Thanks to Burt Kaliski, Jim Randall, Pasi Eronen, Roni Even, Alfred Hoenes, Russ Housley, Jim Schaad, Carl Wallace.