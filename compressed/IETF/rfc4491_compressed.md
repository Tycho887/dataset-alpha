# RFC 4491: Using the GOST R 34.10-94, GOST R 34.10-2001, and GOST R 34.11-94 Algorithms with the Internet X.509 Public Key Infrastructure Certificate and CRL Profile
**Source**: IETF (Standards Track) | **Version**: 1 | **Date**: May 2006 | **Type**: Normative (Updates RFC 3279)
**Original**: https://www.rfc-editor.org/rfc/rfc4491

## Scope (Summary)
This document supplements RFC 3279 by specifying encoding formats, identifiers, and parameter formats for the GOST R 34.10-94, GOST R 34.10-2001 digital signature algorithms, VKO key derivation algorithms, and GOST R 34.11-94 hash function for use in Internet X.509 PKI certificates and CRLs. It defines the contents of signatureAlgorithm, signatureValue, signature, and subjectPublicKeyInfo fields.

## Normative References
- [GOST28147] "Cryptographic Protection for Data Processing System", GOST 28147-89, 1989 (Russian)
- [GOST3431195] GOST 34.311-95, Council for Standardization, EASC, Minsk, 1995 (Russian)
- [GOST3431095] GOST 34.310-95, EASC, Minsk, 1995 (Russian)
- [GOST3431004] GOST 34.310-2004, EASC, Minsk, 2004 (Russian)
- [GOSTR341094] GOST R 34.10-94, Government Committee of Russia for Standards, 1994 (Russian)
- [GOSTR341001] GOST R 34.10-2001, Government Committee of Russia for Standards, 2001 (Russian)
- [GOSTR341194] GOST R 34.11-94, Government Committee of Russia for Standards, 1994 (Russian)
- [CPALGS] Popov, V., Kurepkin, I., and S. Leontiev, "Additional Cryptographic Algorithms for Use with GOST 28147-89, GOST R 34.10-94, GOST R 34.10-2001, and GOST R 34.11-94 Algorithms", RFC 4357, January 2006
- [PKALGS] Bassham, L., Polk, W., and R. Housley, "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3279, April 2002
- [PROFILE] Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002
- [X.660] ITU-T Recommendation X.660, 1997
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997

## Definitions and Abbreviations
- **GOST R 34.10-94**: Signature algorithm based on discrete logarithms (256-bit numbers r', s)
- **GOST R 34.10-2001**: Signature algorithm based on elliptic curves (256-bit numbers r, s)
- **GOST R 34.11-94**: One-way hash function producing 256-bit hash value
- **VKO GOST R 34.10-94 / VKO GOST R 34.10-2001**: Key derivation algorithms (see [CPALGS])
- **id-GostR3411-94-with-GostR3410-94**: OID 1.2.643.2.2.4
- **id-GostR3411-94-with-GostR3410-2001**: OID 1.2.643.2.2.3
- **id-GostR3410-94**: OID 1.2.643.2.2.20
- **id-GostR3410-2001**: OID 1.2.643.2.2.19
- **working_public_key_parameters**: variable as per RFC 3280 Section 6.1

## Algorithm Support
- CAs/applications MUST support at least one of the specified public key and signature algorithms.
- One-way hash function GOST R 34.11-94 MUST always be used with parameter set identified by id-GostR3411-94-CryptoProParamSet (see [CPALGS] Section 8.2).

### 2.1 One-Way Hash Function GOST R 34.11-94
- **Hash function**: Produces 256-bit hash value. Specification in [GOSTR341194].
- **Requirement**: MUST always use parameter set id-GostR3411-94-CryptoProParamSet.

### 2.2 Signature Algorithms
- CAs MAY use GOST R 34.10-94 or GOST R 34.10-2001.
- **Requirement**: MUST always be used with GOST R 34.11-94 hash function.

#### 2.2.1 Signature Algorithm GOST R 34.10-94
- **OID**: id-GostR3411-94-with-GostR3410-94 (1.2.643.2.2.4)
- **AlgorithmIdentifier encoding**: SHALL omit parameters field (SEQUENCE of only OID).
- **Signature value**: 64-octet string: first 32 octets big-endian s, second 32 octets big-endian r'.
- **Conversion to bit string**: Most significant bit of first octet becomes first bit of bit string. Use same order.

#### 2.2.2 Signature Algorithm GOST R 34.10-2001
- **OID**: id-GostR3411-94-with-GostR3410-2001 (1.2.643.2.2.3)
- **AlgorithmIdentifier encoding**: SHALL omit parameters field.
- **Signature value**: 64-octet string: first 32 octets big-endian s, second 32 octets big-endian r.
- **Conversion**: MUST use process in section 2.2.1.

### 2.3 Subject Public Key Algorithms
- **Key usage recommendation**: Use of same key for signature and key derivation NOT RECOMMENDED. Intended application MAY be indicated in keyUsage extension (see [PROFILE] Section 4.2.1.3).

#### 2.3.1 GOST R 34.10-94 Keys
- **OID**: id-GostR3410-94 (1.2.643.2.2.20)
- **SubjectPublicKeyInfo algorithm field**: MUST be set to id-GostR3410-94.
- **AlgorithmIdentifier parameters**: MAY omit or set to NULL; otherwise MUST have structure:
  ```
  GostR3410-94-PublicKeyParameters ::= SEQUENCE {
      publicKeyParamSet OBJECT IDENTIFIER,
      digestParamSet OBJECT IDENTIFIER,
      encryptionParamSet OBJECT IDENTIFIER DEFAULT id-Gost28147-89-CryptoPro-A-ParamSet
  }
  ```
  - publicKeyParamSet: public key parameters identifier for GOST R 34.10-94 (see [CPALGS] Section 8.3)
  - digestParamSet: parameters identifier for GOST R 34.11-94 (see [CPALGS] Section 8.2)
  - encryptionParamSet: parameters identifier for GOST 28147-89 (see [CPALGS] Section 8.1)
- **Absence of parameters**: SHALL be processed as per RFC 3280 Section 6.1 (inherited from issuer). When working_public_key_parameters is null, certificate and any signature verifiable on it SHALL be rejected.
- **Public key encoding**: MUST be ASN.1 DER encoded as OCTET STRING, used as contents of subjectPublicKey (BIT STRING).
  - GostR3410-94-PublicKey ::= OCTET STRING -- public key Y
  - MUST contain 128 octets little-endian representation of Y = a^x mod p.
- **Padding recommendation**: RECOMMENDED to pad BIT STRING with zeroes up to 1048 bits (131 octets) on decoding.

- **keyUsage extension for end-entity certificates**:
  - MAY include: digitalSignature; nonRepudiation; keyEncipherment; keyAgreement.
  - If keyAgreement or keyEncipherment present, MAY also include encipherOnly; decipherOnly.
  - MUST NOT assert both encipherOnly and decipherOnly.

- **keyUsage extension for CA/CRL signer certificates**:
  - MAY include: digitalSignature; nonRepudiation; keyCertSign; cRLSign.

#### 2.3.2 GOST R 34.10-2001 Keys
- **OID**: id-GostR3410-2001 (1.2.643.2.2.19)
- **SubjectPublicKeyInfo algorithm field**: MUST be set to id-GostR3410-2001.
- **AlgorithmIdentifier parameters**: MAY omit or set to NULL; otherwise MUST have structure:
  ```
  GostR3410-2001-PublicKeyParameters ::= SEQUENCE {
      publicKeyParamSet OBJECT IDENTIFIER,
      digestParamSet OBJECT IDENTIFIER,
      encryptionParamSet OBJECT IDENTIFIER DEFAULT id-Gost28147-89-CryptoPro-A-ParamSet
  }
  ```
  - publicKeyParamSet: for GOST R 34.10-2001 (see [CPALGS] Section 8.4)
  - digestParamSet: for GOST R 34.11-94 (see [CPALGS] Section 8.2)
  - encryptionParamSet: for GOST 28147-89 (see [CPALGS] Section 8.1)
- **Absence of parameters**: SHALL be processed as per RFC 3280 Section 6.1; same rejection rule.
- **Public key encoding**: MUST be ASN.1 DER encoded as OCTET STRING, used as subjectPublicKey.
  - GostR3410-2001-PublicKey ::= OCTET STRING -- public key point Q = (x,y)
  - MUST contain 64 octets: first 32 octets little-endian x, second 32 octets little-endian y (binary representation <y>256||<x>256 from [GOSTR341001] ch. 5.3).
- **Padding recommendation**: RECOMMENDED to pad BIT STRING with zeroes up to 528 bits (66 octets) on decoding.
- **keyUsage constraints**: Same as in Section 2.3.1.

## Security Considerations
- **Application verification**: RECOMMENDED to verify signature values and public keys conform to [GOSTR341001, GOSTR341094] standards before use.
- **Digital signature as wet signature analogue (Russian Federal Law)**: Certificate MUST contain critical keyUsage extension, and keyUsage MUST NOT include keyEncipherment and keyAgreement.
- **Private key validity**: RECOMMENDED that private key for creating signatures is not used beyond its allowed validity period (typically 15 months for both algorithms).
- **Parameter security**: See Security Considerations in [CPALGS].

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CAs/applications MUST support at least one specified public key and signature algorithm. | MUST | Section 2 |
| R2 | GOST R 34.11-94 hash function MUST always be used with parameter set id-GostR3411-94-CryptoProParamSet. | MUST | Section 2.1.1 |
| R3 | Signature algorithms GOST R 34.10-94/2001 MUST always be used with GOST R 34.11-94. | MUST | Section 2.2 |
| R4 | For id-GostR3411-94-with-GostR3410-94 AlgorithmIdentifier, parameters field SHALL be omitted. | SHALL | Section 2.2.1 |
| R5 | Signature value conversion from octet string to bit string: most significant bit of first octet becomes first bit, etc. | SHALL | Section 2.2.1 |
| R6 | For id-GostR3411-94-with-GostR3410-2001 AlgorithmIdentifier, parameters field SHALL be omitted. | SHALL | Section 2.2.2 |
| R7 | Signature value conversion for GOST R 34.10-2001 MUST use process from Section 2.2.1. | MUST | Section 2.2.2 |
| R8 | SubjectPublicKeyInfo.algorithm field for GOST R 34.10-94 keys MUST be id-GostR3410-94. | MUST | Section 2.3.1 |
| R9 | Parameters for GOST R 34.10-94 AlgorithmIdentifier: MAY omit or set to NULL; otherwise MUST be GostR3410-94-PublicKeyParameters. | MUST/MAY | Section 2.3.1 |
| R10 | Absence of parameters SHALL be processed as per RFC 3280 Section 6.1; if working_public_key_parameters is null, certificate SHALL be rejected. | SHALL | Section 2.3.1 |
| R11 | GOST R 34.10-94 public key MUST be DER encoded as OCTET STRING (128 octets, little-endian Y). | MUST | Section 2.3.1 |
| R12 | keyUsage extension for end-entity GOST R 34.10-94: MAY include digitalSignature, nonRepudiation, keyEncipherment, keyAgreement; if keyAgreement/encipherment, MAY include encipherOnly/decipherOnly; MUST NOT assert both encipherOnly and decipherOnly. | MAY/MUST NOT | Section 2.3.1 |
| R13 | keyUsage for CA/CRL signer with GOST R 34.10-94: MAY include digitalSignature, nonRepudiation, keyCertSign, cRLSign. | MAY | Section 2.3.1 |
| R14 | SubjectPublicKeyInfo.algorithm field for GOST R 34.10-2001 keys MUST be id-GostR3410-2001. | MUST | Section 2.3.2 |
| R15 | Parameters for GOST R 34.10-2001 AlgorithmIdentifier: MAY omit or set to NULL; otherwise MUST be GostR3410-2001-PublicKeyParameters. | MUST/MAY | Section 2.3.2 |
| R16 | Absence of parameters SHALL be processed as per RFC 3280 Section 6.1; same rejection. | SHALL | Section 2.3.2 |
| R17 | GOST R 34.10-2001 public key MUST be DER encoded as OCTET STRING (64 octets: little-endian x, little-endian y). | MUST | Section 2.3.2 |
| R18 | keyUsage constraints for GOST R 34.10-2001 are same as for 34.10-94 (Section 2.3.1). | MUST | Section 2.3.2 |
| R19 | For certificates used as wet signature analogue per Russian Federal Law: keyUsage MUST be critical and MUST NOT include keyEncipherment/keyAgreement. | MUST | Section 3 |

## Informative Annexes (Condensed)
- **Section 4.1 Example (GOST R 34.10-94 Certificate)**: Provides a PEM-encoded certificate and hex dump showing structure, signature values r' and s.
- **Section 4.2 Example (GOST R 34.10-2001 Certificate)**: Provides PEM-encoded certificate and hex dump showing public key x, y, private key d, and signature values r, s.
- **Section 5 Acknowledgements**: Document created per "Russian Cryptographic Software Compatibility Agreement" with multiple organizations. Thanks to Microsoft Russia, RSA Security Russia/Demos, RSA Security Inc, Baltimore Technology, Peter Gutmann, Russ Housley, Vasilij Sakharov, Grigorij Chudov, Prikhodko Dmitriy.
- **Section 6.2 Informative References**: [Schneier95] Applied Cryptography, Second Edition; [RFEDSL] Russian Federal Electronic Digital Signature Law; [CMS] RFC 3852.