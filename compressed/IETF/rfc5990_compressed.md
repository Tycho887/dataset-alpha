# RFC 5990: Use of the RSA-KEM Key Transport Algorithm in the Cryptographic Message Syntax (CMS)
**Source**: IETF | **Version**: Standards Track | **Date**: September 2010 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc5990

## Scope (Summary)
This document specifies conventions for using the RSA-KEM key transport algorithm with the Cryptographic Message Syntax (CMS). RSA-KEM provides a one-pass mechanism for transporting keying data using a recipient's RSA public key, with tighter security proof than PKCS#1 v1.5. The ASN.1 syntax aligns with ANS X9.44.

## Normative References
- [3DES-WRAP] RFC 3217
- [AES-WRAP] RFC 3394
- [ANS-X9.44] ASC X9F1, ANS X9.44:2007
- [ANS-X9.63] ANS X9.63-2002
- [CAMELLIA] RFC 3657
- [CMS] RFC 5652
- [CMSALGS] RFC 3370
- [FIPS-180-3] NIST FIPS 180-3
- [MSG] RFC 5751
- [PROFILE] RFC 5280
- [STDWORDS] RFC 2119

## Definitions and Abbreviations
- **RSA-KEM**: RSA Key Encapsulation Mechanism – a key transport algorithm.
- **KEM**: Key encapsulation mechanism (steps 1-3 of algorithm).
- **KEK**: Key-encrypting key derived from the random integer.
- **KDF**: Key derivation function (e.g., KDF2, KDF3).
- **Wrap**: Symmetric key-wrapping scheme (e.g., AES-Wrap).
- **EK**: Encrypted keying data = ciphertext C || wrapped keying data WK.
- **nLen**: Length in bytes of RSA modulus n.
- **kekLen**: Length in bytes of the KEK.
- **GenericHybridParameters**: ASN.1 structure identifying KEM and DEM.

## Introduction
- RSA-KEM is a one-pass (store-and-forward) mechanism for transporting keying data using the recipient's RSA public key.
- **Previous approaches** (e.g., PKCS#1 v1.5) format/pad keying data and encrypt integer m; RSA-KEM encrypts a random integer z and uses symmetric key-wrapping.
- **Higher security assurance** because input to RSA is random and independent of keying data, providing tight security proof in random oracle model.
- **Benefits**: public-key operations separate from symmetric operations; keying data length bounded only by symmetric key-wrapping scheme.
- Algorithm specified in Appendix A; ASN.1 syntax in Appendix B.
- Object identifier: **id-rsa-kem** (different from id-ac-generic-hybrid used in earlier ANS X9.44 drafts).

### 1.1 Conventions Used in This Document
- Key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL" are to be interpreted as described in RFC 2119.

## 2. Use in CMS
- RSA-KEM **MAY** be employed for one or more recipients in the CMS enveloped-data content type (Section 6 of [CMS]), where the keying data is the CMS content-encryption key.

### 2.1 Underlying Components
- **MUST** support at least:
  - KDF3 (per [ANS-X9.44]) based on SHA-256 (per [FIPS-180-3]) – instantiation of Concatenation KDF defined in [NIST-SP800-56A].
  - AES-Wrap-128 (AES Key Wrap with 128-bit KEK, per [AES-WRAP]).
- **SHOULD** also support:
  - KDF2 (per [ANS-X9.44]) based on SHA-1 (also specified in [ANS-X9.63]).
  - Camellia key wrap algorithm ([CAMELLIA]) if Camellia is supported as content-encryption cipher.
  - Triple-DES Key Wrap ([3DES-WRAP]) if Triple-DES is supported.
- **MAY** support other underlying components.
- When AES or Camellia used: data block 128 bits, key sizes 128/192/256; Triple-DES: data block 64 bits, key sizes 112/168.

### 2.2 RecipientInfo Conventions
- RecipientInfo alternative **MUST** be **KeyTransRecipientInfo**.
- Field values:
  - `keyEncryptionAlgorithm.algorithm` **MUST** be **id-rsa-kem**.
  - `keyEncryptionAlgorithm.parameters` **MUST** be a value of type **GenericHybridParameters** identifying RSA-KEM.
  - `encryptedKey` **MUST** be the encrypted keying data output by the algorithm (content-encryption key).

### 2.3 Certificate Conventions
- Augments RFC 5280 [PROFILE].
- Recipient **MAY** identify public key using rsaEncryption OID (same as PKCS#1 v1.5). Acceptance of RSA-KEM with this key not indicated by identifier; **MAY** be signaled via SMIME Capabilities.
- If recipient wishes to **only** employ RSA-KEM with given public key, **MUST** identify using **id-rsa-kem** OID.
  - In SubjectPublicKeyInfo algorithm field, **SHALL** omit parameters (AlgorithmIdentifier SEQUENCE of one component).
- RSA public key encoded using RSAPublicKey type: `SEQUENCE { modulus INTEGER, publicExponent INTEGER }`.
- If keyUsage extension present with id-rsa-kem OID, **MUST** contain value `keyEncipherment`. `dataEncipherment` **SHOULD NOT** be present.
- Good cryptographic practice: single key pair used in only one scheme.

### 2.4 SMIMECapabilities Attribute Conventions
- **MAY** include SMIMECapabilities signed attribute announcing support for RSA-KEM.
- SMIMECapability SEQUENCE **MUST** include id-rsa-kem OID in capabilityID field and **MUST** include GenericHybridParameters value in parameters field.

## 3. Security Considerations
- RSA-KEM recommended for new CMS applications as replacement for PKCS#1 v1.5 (vulnerable to chosen-ciphertext attacks). RSAES-OAEP also proposed; RSA-KEM has tighter security proof but slightly longer encrypted keying data.
- Security tightly related to difficulty of RSA problem or breaking symmetric key-wrapping scheme (assuming KDF as random oracle).
- RSA key size and components selected consistent with desired symmetric security level.
- Security levels (NIST SP 800-57):
  - 80-bit: RSA ≥1024 bits; hash ≥SHA-1; wrap: AES, Triple-DES, or Camellia.
  - 112-bit: RSA ≥2048 bits; hash ≥SHA-224; wrap: same.
  - 128-bit: RSA ≥3072 bits; hash ≥SHA-256; wrap: AES or Camellia.
- AES/Camellia Key Wrap **MAY** be used at all levels; use does not require 128-bit security for other components.
- Implementations **MUST** protect RSA private key and content-encryption key.
- Random number generator **SHOULD** have comparable security level.
- Implementations **SHOULD NOT** reveal intermediate values via side channels.
- Good cryptographic practice: single RSA key pair used in only one scheme. Combined use **NOT RECOMMENDED**.
- RSA key pair used for RSA-KEM **SHOULD NOT** also be used for digital signatures, other key establishment schemes, data encryption, or with more than one set of underlying algorithm components.
- Parties **MAY** formalize assurance through implementation validation (e.g., NIST CMVP).

## 4. IANA Considerations
- All OIDs assigned in other documents except ASN.1 module identifier and id-rsa-kem, assigned in this document.
- Module object identifiers delegated by RSA Data Security Inc. to S/MIME WG; upon WG closure, transferred to IANA.

## 5. Acknowledgements
- Contributions from ASC X9F1, Russ Housley, Blake Ramsdell, Jim Schaad, Magnus Nystrom, Bob Griffin, John Linn.

## 6. References
- Normative and informative references listed (see original for full list).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | RSA-KEM algorithm **MAY** be employed for one or more recipients in CMS enveloped-data type. | may | §2 |
| R2 | CMS implementation supporting RSA-KEM **MUST** support KDF3 based on SHA-256 and AES-Wrap-128. | shall | §2.1 |
| R3 | Implementation **SHOULD** also support KDF2 based on SHA-1, Camellia Key Wrap (if Camellia used), Triple-DES Key Wrap (if Triple-DES used). | should | §2.1 |
| R4 | Implementation **MAY** support other underlying components. | may | §2.1 |
| R5 | RecipientInfo alternative **MUST** be KeyTransRecipientInfo. | shall | §2.2 |
| R6 | keyEncryptionAlgorithm.algorithm **MUST** be id-rsa-kem. | shall | §2.2 |
| R7 | keyEncryptionAlgorithm.parameters **MUST** be GenericHybridParameters. | shall | §2.2 |
| R8 | encryptedKey **MUST** be output of algorithm (content-encryption key). | shall | §2.2 |
| R9 | Recipient **MAY** identify public key using rsaEncryption OID. | may | §2.3 |
| R10 | If recipient wishes to use RSA-KEM only with a given public key, **MUST** use id-rsa-kem OID. | shall | §2.3 |
| R11 | When id-rsa-kem appears in SubjectPublicKeyInfo algorithm field, parameters **SHALL** be omitted. | shall | §2.3 |
| R12 | If keyUsage extension present with id-rsa-kem, **MUST** contain keyEncipherment. | shall | §2.3 |
| R13 | dataEncipherment in keyUsage **SHOULD NOT** be present. | should-not | §2.3 |
| R14 | SMIMECapability SEQUENCE for RSA-KEM **MUST** include id-rsa-kem and GenericHybridParameters. | shall | §2.4 |
| R15 | Implementations **MUST** protect RSA private key and content-encryption key. | shall | §3 |
| R16 | Random number generator **SHOULD** have comparable security level. | should | §3 |
| R17 | Implementations **SHOULD NOT** reveal intermediate values via side channels. | should-not | §3 |
| R18 | Combined use of RSA key pair for multiple purposes **NOT RECOMMENDED**. | not-recommended | §3 |
| R19 | RSA key pair used for RSA-KEM **SHOULD NOT** also be used for digital signatures, other key establishment, data encryption, or with more than one set of underlying components. | should-not | §3 |
| R20 | Parties **MAY** formalize assurance through implementation validation. | may | §3 |

## Appendix A: RSA-KEM Key Transport Algorithm (Normative)

- One-pass store-and-forward mechanism.
- Underlying components: KDF (key derivation function) and Wrap (symmetric key-wrapping scheme). Length of keying data **MUST** be among lengths supported by Wrap (e.g., AES/Camellia Key Wraps require multiple of 8 bytes, at least 16 bytes). Usage/formatting outside scope.

### A.2 Sender's Operations
Let (n,e) be recipient's RSA public key. Let nLen = byte length of modulus n.
1. Generate random integer z uniformly in [0, n-1]. Convert to byte string Z length nLen, big-endian.
2. c = z^e mod n; convert c to byte string C length nLen.
3. Derive KEK = KDF(Z, kekLen).
4. WK = Wrap(KEK, K) where K is keying data.
5. EK = C || WK.
6. Output EK.
- **NOTE**: random integer z **MUST** be generated independently for each encryption.

### A.3 Recipient's Operations
Let (n,d) be private key. nLen as before.
1. Separate EK into C (first nLen bytes) and WK. If EK length < nLen, output "decryption error" and stop.
2. Convert C to integer c; z = c^d mod n. If c not in [0, n-1], output "decryption error" and stop.
3. Convert z to byte string Z length nLen.
4. Derive KEK = KDF(Z, kekLen).
5. K = Unwrap(KEK, WK). If error, output "decryption error".
6. Output K.
- **NOTE**: Implementations **SHOULD NOT** reveal information about z, Z, exponentiation steps, conversion, or KDF via side channels. Observable behavior **SHOULD** be same for all in-range C. Integer z, string Z, intermediates **MUST** be securely deleted when no longer needed.

## Appendix B: ASN.1 Syntax (Normative)

- Extends ANS X9.44 generic hybrid cipher syntax.
- OID prefixes defined (is18033-2, nistAlgorithm, pkcs-1, x9-44).
- **id-rsa-kem**: `{ iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 14 }`
- When used in AlgorithmIdentifier, parameters **MUST** be GenericHybridParameters. In SubjectPublicKeyInfo, parameters **MUST** be absent.
- GenericHybridParameters: SEQUENCE { kem KeyEncapsulationMechanism, dem DataEncapsulationMechanism }.
- id-kem-rsa: `{ is18033-2 key-encapsulation-mechanism(2) rsa(4) }`.
- RsaKemParameters: SEQUENCE { keyDerivationFunction KeyDerivationFunction, keyLength KeyLength (INTEGER)}.
- KeyDerivationFunction for alignment **MUST** be KDF2 or KDF3, but other KDFs **MAY** be used with CMS.
- DataEncapsulationMechanism: for alignment **MUST** be X9-approved symmetric key-wrapping, but others **MAY** be used.
- Key derivation function OIDs: id-kdf-kdf2, id-kdf-kdf3 (with hash function parameter). Hash functions: SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.
- Implementation **SHOULD** generate algorithm identifiers without parameters and **MUST** accept either without or with NULL parameters for SHA OIDs.
- Symmetric key-wrapping OIDs: id-aes128-Wrap, id-aes192-Wrap, id-aes256-Wrap (no parameters); id-alg-CMS3DESwrap (NULL parameter); id-camellia128-Wrap, id-camellia192-Wrap, id-camellia256-Wrap (no parameters).
- ASN.1 module defined in Appendix B.3 (CMS-RSA-KEM). Provides full type definitions.
- Examples of DER encodings for typical component combinations provided in Appendix B.4 (preserved as informative).

## Informative Annexes (Condensed)
- **Appendix A**: Provides full normative specification of the RSA-KEM algorithm operations for sender and recipient, including underlying components and error handling.
- **Appendix B**: Provides normative ASN.1 syntax, object identifiers, and module definition; includes example DER encodings for typical parameter sets.