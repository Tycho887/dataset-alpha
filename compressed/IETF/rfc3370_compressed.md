# RFC 3370: Cryptographic Message Syntax (CMS) Algorithms
**Source**: IETF (Standards Track) | **Version**: RFC 3370 (obsoletes RFC 2630, RFC 3211) | **Date**: August 2002 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc3370.txt

## Scope (Summary)
This document specifies the conventions for using common cryptographic algorithms with the Cryptographic Message Syntax (CMS) for digital signing, digesting, authentication, and encryption. Implementations that choose to support any algorithm described MUST do so exactly as specified.

## Normative References
- [3DES] ANSI X9.52-1998
- [CERTALGS] RFC 3279
- [CMS] RFC 3269
- [DES] ANSI X3.106, 1983
- [DH-X9.42] RFC 2631
- [DSS] FIPS Pub 186
- [HMAC] RFC 2104
- [MD5] RFC 1321
- [MMA] RFC 3218
- [MODES] FIPS Pub 81
- [NEWPKCS#1] RFC 2437
- [OLDCMS] RFC 2630
- [PKCS#1] RFC 2437
- [PKCS#5] RFC 2898
- [PROFILE] RFC 3280
- [RANDOM] RFC 1750
- [RC2] RFC 2268
- [SHA1] FIPS Pub 180-1
- [STDWORDS] BCP 14, RFC 2119
- [WRAP] RFC 3217
- [X.208-88] CCITT X.208
- [X.209-88] CCITT X.209

## Definitions and Abbreviations
- **CMS**: Cryptographic Message Syntax
- **ASN.1**: Abstract Syntax Notation One
- **BER**: Basic Encoding Rules
- **SHA-1**: Secure Hash Algorithm 1 (FIPS 180-1)
- **MD5**: Message Digest Algorithm 5 (RFC 1321)
- **DSA**: Digital Signature Algorithm (FIPS 186)
- **RSA**: Rivest-Shamir-Adleman (PKCS #1 v1.5)
- **3DES**: Triple Data Encryption Algorithm (ANSI X9.52)
- **RC2**: Rivest Cipher 2 (RFC 2268)
- **HMAC**: Keyed-Hashing for Message Authentication (RFC 2104)
- **PBKDF2**: Password-Based Key Derivation Function 2 (RFC 2898)
- **IV**: Initialization Vector
- **CBC**: Cipher Block Chaining
- **KEK**: Key-Encryption Key
- **CEK**: Content-Encryption Key
- **MAC**: Message Authentication Code
- **OID**: Object Identifier
- **E-S D-H**: Ephemeral-Static Diffie-Hellman
- **S-S D-H**: Static-Static Diffie-Hellman

## 1 Introduction
- The CMS [CMS] is used for signing, digesting, authenticating, or encrypting arbitrary messages. This document describes the use of common algorithms with the CMS.
- **R1**: If an implementation supports one of the algorithms discussed, it MUST do so as described in this document.
- CMS values are generated using ASN.1 with BER-encoding.
- **R2**: Algorithm identifiers (including OIDs) identify algorithms; parameters are specified via ASN.1 structures where needed.

### 1.1 Changes Since RFC 2630
- This document obsoletes Section 12 of RFC 2630. RFC 3369 obsoletes the rest. Separation allows independent updates.

### 1.2 Terminology
- **R3**: The key words MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, RECOMMENDED, and MAY are to be interpreted as described in [STDWORDS].

## 2 Message Digest Algorithms
- Digest algorithm identifiers are used in SignedData.digestAlgorithms, SignerInfo.digestAlgorithm, DigestedData.digestAlgorithm, AuthenticatedData.digestAlgorithm.
- Digest values are located in DigestedData.digest and the Message Digest authenticated attribute.

### 2.1 SHA-1
- **OID**: `sha-1 { iso(1) identified-organization(3) oiw(14) secsig(3) algorithm(2) 26 }`
- **Parameter encoding**: The correct encoding is to omit the parameters field.
  - **R4**: Implementations MUST handle a SHA-1 AlgorithmIdentifier with a NULL parameters field (if present).
  - **R5**: Implementations MUST accept SHA-1 AlgorithmIdentifiers with absent parameters.
  - **R6**: Implementations MUST accept SHA-1 AlgorithmIdentifiers with NULL parameters.
  - **R7**: Implementations SHOULD generate SHA-1 AlgorithmIdentifiers with absent parameters.

### 2.2 MD5
- **OID**: `md5 { iso(1) member-body(2) us(840) rsadsi(113549) digestAlgorithm(2) 5 }`
- **R8**: The AlgorithmIdentifier parameters field MUST be present and MUST contain NULL.
- **R9**: Implementations MAY accept MD5 AlgorithmIdentifiers with absent parameters as well as NULL parameters.

## 3 Signature Algorithms
- Signature algorithm identifiers in SignerInfo.signatureAlgorithm (SignedData and countersignatures).
- Signature values in SignerInfo.signature field.

### 3.1 DSA
- **R10**: DSA MUST be used with the SHA-1 message digest algorithm.
- **Public key OID**: `id-dsa { iso(1) member-body(2) us(840) x9-57(10040) x9cm(4) 1 }`
- DSA parameters (p, q, g) are optional in certificates; if present, MUST be encoded as `Dss-Parms`.
- Public key (Y) encoded as `INTEGER` (`Dss-Pub-Key`).
- **Signature OID**: `id-dsa-with-sha1 { iso(1) member-body(2) us(840) x9-57(10040) x9cm(4) 3 }`
- **R11**: When `id-dsa-with-sha1` is used, the AlgorithmIdentifier parameters field MUST be absent.
- Signature values (r, s) encoded as `Dss-Sig-Value { r INTEGER, s INTEGER }`.

### 3.2 RSA (PKCS #1 v1.5)
- Defined in RFC 2437; uses SHA-1 or MD5.
- **Public key OID**: `rsaEncryption { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 1 }`
- **R12**: When `rsaEncryption` is used, AlgorithmIdentifier parameters MUST be NULL.
- Public key encoded as `RSAPublicKey { modulus INTEGER, publicExponent INTEGER }`.
- **R13**: CMS implementations including RSA signature MUST also implement SHA-1.
- **R14**: Such implementations SHOULD also support MD5.
- **R15**: CMS implementations that include RSA signature MUST support the `rsaEncryption` signature value algorithm identifier.
- **R16**: MAY support algorithm identifiers that specify both RSA and the digest algorithm (e.g., `sha1WithRSAEncryption`, `md5WithRSAEncryption`).
- **R17**: When `rsaEncryption`, `sha1WithRSAEncryption`, or `md5WithRSAEncryption` are used, the AlgorithmIdentifier parameters MUST be NULL.
- Signature value is a single value used directly.

## 4 Key Management Algorithms
- Key management techniques: key agreement, key transport, previously distributed symmetric KEKs, and passwords.

### 4.1 Key Agreement Algorithms
- **R18**: When key agreement is supported, a key-encryption algorithm MUST be provided for each content-encryption algorithm.
- Key wrap algorithms for Triple-DES and RC2 are described in RFC 3217.
- **R19**: For key agreement of RC2 KEKs, 128 bits MUST be generated as input to key expansion (RC2 effective key).

#### 4.1.1 X9.42 Ephemeral-Static Diffie-Hellman
- **EnvelopedData KeyAgreeRecipientInfo fields**:
  - version MUST be 3.
  - originator MUST be the originatorKey alternative. The algorithm field MUST contain `dh-public-number` with absent parameters. The publicKey contains the sender's ephemeral public key.
  - ukm: MAY be present or absent. CMS implementations MUST support ukm absent; SHOULD support ukm present.
  - keyEncryptionAlgorithm MUST be `id-alg-ESDH`. The parameter field is `KeyWrapAlgorithm` and MUST be present.
    - OID `id-alg-ESDH { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 5 }`.
  - recipientEncryptedKeys: Each `KeyAgreeRecipientIdentifier` MUST contain either `issuerAndSerialNumber` or `RecipientKeyIdentifier`. The `EncryptedKey` MUST contain the CEK encrypted with the pairwise key-encryption key using the specified `KeyWrapAlgorithm`.

#### 4.1.2 X9.42 Static-Static Diffie-Hellman
- **EnvelopedData/AuthenticatedData KeyAgreeRecipientInfo fields**:
  - version MUST be 3.
  - originator MUST be `issuerAndSerialNumber` or `subjectKeyIdentifier`. The originator's certificate subject public key MUST contain `dh-public-number`.
  - ukm MUST be present.
  - keyEncryptionAlgorithm MUST be `id-alg-SSDH`. The parameter field is `KeyWrapAlgorithm` and MUST be present.
    - OID `id-alg-SSDH { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 10 }`.
  - recipientEncryptedKeys: same as E-S DH; `EncryptedKey` MUST contain the CEK encrypted with the pairwise key-encryption key.

### 4.2 Key Transport Algorithms
- Key transport algorithm identifiers in `KeyTransRecipientInfo.keyEncryptionAlgorithm`.
- Encrypted CEK in `KeyTransRecipientInfo.encryptedKey`.

#### 4.2.1 RSA (PKCS #1 v1.5)
- **OID**: `rsaEncryption { ... }`.
- **R20**: The AlgorithmIdentifier parameters MUST be present and MUST contain NULL.
- **R21**: When using Triple-DES CEK, implementations MUST adjust parity bits for each DES key prior to RSA encryption.
- Note: Known vulnerability (adaptive chosen ciphertext); see Security Considerations and RFC 3218.

### 4.3 Symmetric Key-Encryption Key Algorithms
- **R22**: When RC2 is supported, RC2 128-bit keys MUST be used as KEKs and MUST be used with `RC2ParameterVersion` set to 58.
- CMS implementation MAY support mixed key-encryption and content-encryption algorithms.

#### 4.3.1 Triple-DES Key Wrap
- **OID**: `id-alg-CMS3DESwrap { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 6 }`
- **R23**: The AlgorithmIdentifier parameter MUST be NULL.
- Key wrap/unwrap algorithms per RFC 3217 sections 3.1 and 3.2.

#### 4.3.2 RC2 Key Wrap
- **OID**: `id-alg-CMSRC2wrap { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 7 }`
- **R24**: The AlgorithmIdentifier parameter MUST be `RC2wrapParameter` (i.e., `RC2ParameterVersion`).
- RC2 effective-key-bits encoding: 40 → 160, 64 → 120, 128 → 58. (Note: 160 encoded as two octets 00 A0.)
- **R25**: RC2 128-bit keys MUST be used as KEKs with version 58.
- Key wrap/unwrap algorithms per RFC 3217 sections 4.1 and 4.2.

### 4.4 Key Derivation Algorithms
- Used for password-based key management.

#### 4.4.1 PBKDF2
- **OID**: `id-PBKDF2 { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-5(5) 12 }`
- **R26**: The AlgorithmIdentifier parameter MUST be `PBKDF2-params`.
- `PBKDF2-params` SEQUENCE: salt (specified OCTET STRING or otherSource), iterationCount (1..MAX), keyLength (1..MAX) OPTIONAL, prf (default hMAC-SHA1).
- **R27**: Within PBKDF2-params, the salt MUST use the specified OCTET STRING.

## 5 Content Encryption Algorithms
- Content encryption algorithm identifiers in `EnvelopedData.EncryptedContentInfo.contentEncryptionAlgorithm` and `EncryptedData.EncryptedContentInfo.contentEncryptionAlgorithm`.
- Used to encipher content in the encryptedContent fields.

### 5.1 Triple-DES CBC
- **OID**: `des-ede3-cbc { iso(1) member-body(2) us(840) rsadsi(113549) encryptionAlgorithm(3) 7 }`
- Three-Key or Two-Key Triple-DES; same OID.
- **R28**: The AlgorithmIdentifier parameters MUST be present and MUST contain a `CBCParameter` (IV, exactly 8 octets).
- `CBCParameter ::= IV`, `IV ::= OCTET STRING` (exactly 8 octets).

### 5.2 RC2 CBC
- **OID**: `rc2-cbc { iso(1) member-body(2) us(840) rsadsi(113549) encryptionAlgorithm(3) 2 }`
- **R29**: The AlgorithmIdentifier parameters MUST be present and MUST contain `RC2CBCParameter` (sequence of rc2ParameterVersion INTEGER and iv OCTET STRING exactly 8 octets).
- rc2ParameterVersion encoding same as RC2 key wrap (40→160, 64→120, 128→58).

## 6 Message Authentication Code Algorithms
- MAC algorithm identifiers in `AuthenticatedData.macAlgorithm`.
- MAC values in `AuthenticatedData.mac`.

### 6.1 HMAC with SHA-1
- **OID**: `hMAC-SHA1 { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) 8 1 2 }`
- **R30**: The AlgorithmIdentifier parameters field is OPTIONAL. If present, MUST contain NULL.
- **R31**: Implementations MUST accept HMAC with SHA-1 AlgorithmIdentifiers with absent parameters.
- **R32**: Implementations MUST accept HMAC with SHA-1 AlgorithmIdentifiers with NULL parameters.
- **R33**: Implementations SHOULD generate HMAC with SHA-1 AlgorithmIdentifiers with absent parameters.

## 7 ASN.1 Module
Full ASN.1 module (normative) is provided in the document. Key types and OIDs are defined; implementations must conform to this module. See RFC 3370 Section 7 for complete syntax.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations supporting algorithms must do so exactly as specified. | shall | Section 1 |
| R2 | Algorithm identifiers include OID; parameters via ASN.1 if needed. | shall | Section 1 |
| R3 | RFC 2119 key words apply. | shall | Section 1.2 |
| R4 | SHA-1: handle NULL parameters if present. | must | Section 2.1 |
| R5 | SHA-1: accept absent parameters. | must | Section 2.1 |
| R6 | SHA-1: accept NULL parameters. | must | Section 2.1 |
| R7 | SHA-1: generate absent parameters. | should | Section 2.1 |
| R8 | MD5: parameters MUST be present and NULL. | must | Section 2.2 |
| R9 | MD5: MAY accept absent or NULL parameters. | may | Section 2.2 |
| R10 | DSA MUST use SHA-1. | must | Section 3.1 |
| R11 | DSA signature identifier parameters MUST be absent. | must | Section 3.1 |
| R12 | RSA public key identifier parameters MUST be NULL. | must | Section 3.2 |
| R13 | RSA signature implementations MUST implement SHA-1. | must | Section 3.2 |
| R14 | RSA implementations SHOULD support MD5. | should | Section 3.2 |
| R15 | RSA signature values MUST support rsaEncryption identifier. | must | Section 3.2 |
| R16 | MAY support combined identifiers like sha1WithRSAEncryption. | may | Section 3.2 |
| R17 | RSA encryption/signature identifiers parameters MUST be NULL. | must | Section 3.2 |
| R18 | Key agreement requires a key-encryption algorithm per CEK. | must | Section 4.1 |
| R19 | RC2 KEK generation: 128 bits MUST be input for key expansion. | must | Section 4.1 |
| R20 | RSA key transport parameters MUST be present and NULL. | must | Section 4.2.1 |
| R21 | Triple-DES CEK: adjust parity before RSA encryption. | must | Section 4.2.1 |
| R22 | RC2 KEK: 128-bit keys with version 58. | must | Section 4.3 |
| R23 | Triple-DES key wrap parameters MUST be NULL. | must | Section 4.3.1 |
| R24 | RC2 key wrap parameters MUST be RC2wrapParameter. | must | Section 4.3.2 |
| R25 | RC2 KEK: 128-bit keys with version 58. | must | Section 4.3.2 |
| R26 | PBKDF2 parameters MUST be PBKDF2-params. | must | Section 4.4.1 |
| R27 | PBKDF2 salt MUST use specified OCTET STRING. | must | Section 4.4.1 |
| R28 | Triple-DES CBC parameters MUST be present and contain IV. | must | Section 5.1 |
| R29 | RC2 CBC parameters MUST be present and contain RC2CBCParameter. | must | Section 5.2 |
| R30 | HMAC-SHA1: parameters OPTIONAL; if present NULL. | must | Section 6.1 |
| R31 | HMAC-SHA1: accept absent parameters. | must | Section 6.1 |
| R32 | HMAC-SHA1: accept NULL parameters. | must | Section 6.1 |
| R33 | HMAC-SHA1: generate absent parameters. | should | Section 6.1 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 9)**: Provides essential warnings: protect private keys (signer, key management, KEK, CEK); compromise leads to masquerade or disclosure. Key management for message-authentication keys must provide authentication (e.g., Static-Static Diffie-Hellman with certificates; RSA and E-S DH do not). Random generation critical; use quality PRNGs per RFC 1750 and FIPS 186 Appendix 3. When KEK and CEK algorithms differ, effective security equals the weaker algorithm. Key wrap algorithms (RFC 3217) reviewed only for Triple-DES and RC2; additional key wraps needed for other ciphers. Algorithm strength degrades over time; modular implementation recommended. RSA (PKCS #1 v1.5) vulnerable to adaptive chosen ciphertext attacks; more feasible in interactive environments than store-and-forward. PKCS #1 v2.0 OAEP recommended for confidentiality; support for OAEP likely in future version. See RFC 3218 for countermeasures.
- **Acknowledgments (Section 10)**: Thanks to S/MIME Working Group members; list of contributors.
- **Full Copyright Statement (Section 12)**: Standard IETF copyright; unlimited distribution with attribution; modifications only for standards development or translation.