# RFC 4055: Additional Algorithms and Identifiers for RSA Cryptography for use in the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: June 2005 | **Type**: Normative
**Original**: RFC 4055 (Schaad, Kaliski, Housley)

## Scope (Summary)
This document supplements RFC 3279 and RFC 3280 by specifying conventions for using RSASSA-PSS signature algorithm, RSAES-OAEP key transport algorithm, and additional one-way hash functions (SHA-224, SHA-256, SHA-384, SHA-512) with PKCS #1 v1.5 signature algorithm in Internet X.509 PKI certificates and CRLs. It defines encoding formats, algorithm identifiers, and parameter structures.

## Normative References
- [P1v1.5] Kaliski, B., "PKCS #1: RSA Encryption Version 1.5", RFC 2313, March 1998.
- [P1v2.1] Jonsson, J. and B. Kaliski, "PKCS #1: RSA Cryptography Specifications Version 2.1", RFC 3447, February 2003.
- [PROFILE] Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- [SHA2] NIST FIPS 180-2: Secure Hash Standard, 1 August 2002.
- [SHA224] Housley, R., "A 224-bit One-way Hash Function: SHA-224", RFC 3874, September 2004.
- [STDWORDS] Bradner, S., "Key Words for Use in RFCs to Indicate Requirement Levels", RFC 2119, March 1997.
- [X.208-88] CCITT Recommendation X.208: Specification of Abstract Syntax Notation One (ASN.1), 1988.
- [X.209-88] CCITT Recommendation X.209: Specification of Basic Encoding Rules for ASN.1, 1988.
- [X.509-88] CCITT Recommendation X.509: The Directory - Authentication Framework, 1988.

## Definitions and Abbreviations
- **RSASSA-PSS**: RSA Probabilistic Signature Scheme (PKCS #1 v2.1)
- **RSAES-OAEP**: RSA Encryption Scheme - Optimal Asymmetric Encryption Padding (PKCS #1 v2.1)
- **MGF1**: Mask Generation Function 1 (PKCS #1 v2.1)
- **HashAlgorithm**: AlgorithmIdentifier for one-way hash functions (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512)
- **MaskGenAlgorithm**: AlgorithmIdentifier for mask generation function (only MGF1 supported)
- **pSourceFunc**: Source of encoding parameters P for RSAES-OAEP
- **RSAPublicKey**: ASN.1 SEQUENCE { modulus INTEGER, publicExponent INTEGER }
- **rsaEncryption**: OID { pkcs-1 1 } for generic RSA public keys
- **id-RSASSA-PSS**: OID { pkcs-1 10 } for RSASSA-PSS restricted keys
- **id-RSAES-OAEP**: OID { pkcs-1 7 } for RSAES-OAEP restricted keys

## 1. Introduction
(Covered in Scope)

### 1.1. Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

### 1.2. RSA Public Keys
- **R1**: When the RSA private key owner does not wish to limit use, `rsaEncryption` OID MUST be used in algorithm field; parameters field MUST contain NULL.
- **R2**: When limiting to RSASSA-PSS only, `id-RSASSA-PSS` OID MUST be used; if parameters present, MUST be RSASSA-PSS-params.
- **R3**: When limiting to RSAES-OAEP only, `id-RSAES-OAEP` OID MUST be used; if parameters present, MUST be RSAES-OAEP-params.
- **R4**: RSA public key MUST be encoded using RSAPublicKey type.
- **R5**: If keyUsage extension present with `id-RSASSA-PSS` in end-entity certificate, MUST contain one or both of: nonRepudiation, digitalSignature.
- **R6**: If keyUsage present with `id-RSASSA-PSS` in CA certificate, MUST contain one or more of: nonRepudiation, digitalSignature, keyCertSign, cRLSign.
- **R7**: When certificate conveys RSA public key with `id-RSASSA-PSS`, certificate user MUST only use key for RSASSA-PSS operations; if RSASSA-PSS-params present, MUST use the hash, MGF, and trailer field from parameters.
- **R8**: If keyUsage extension present with `id-RSAES-OAEP`, MUST contain only keyEncipherment and/or dataEncipherment; both SHOULD NOT be present.
- **R9**: When certificate conveys RSA public key with `id-RSAES-OAEP`, user MUST only use key for RSAES-OAEP operations; if RSAES-OAEP-params present, MUST use hash and MGF from parameters.

## 2. Common Functions

### 2.1. One-way Hash Functions
- **R10**: Implementations MUST accept both NULL and absent parameters as legal and equivalent encodings for SHA-1, SHA-224, SHA-256, SHA-384, SHA-512.
- **R11**: When used with RSASSA-PSS and RSAES-OAEP, the hash algorithm identifiers are defined with NULL parameters (e.g., sha1Identifier = { id-sha1, NULL }).
- OIDs defined: id-sha1, id-sha224, id-sha256, id-sha384, id-sha512.

### 2.2. Mask Generation Functions
- **R12**: Only MGF1 is supported; identified by id-mgf1 { pkcs-1 8 }.
- **R13**: Parameters field with id-mgf1 MUST contain a HashAlgorithm identifier.
- **R14**: Implementations MUST support default value sha1Identifier for MGF1; MAY support other four.
- Pre-defined identifiers: mgf1SHA1Identifier, mgf1SHA224Identifier, mgf1SHA256Identifier, mgf1SHA384Identifier, mgf1SHA512Identifier.

## 3. RSASSA-PSS Signature Algorithm

### 3.1. RSASSA-PSS Public Keys
- **R15**: When id-RSASSA-PSS used in AlgorithmIdentifier, parameters MUST employ RSASSA-PSS-params syntax. Parameters may be absent or present in subjectPublicKeyInfo; MUST be present in signature algorithm identifier.
- **R16**: CAs that issue certificates with id-RSASSA-PSS SHOULD require parameters in subjectPublicKeyInfo if cA boolean is set; MAY require for end-entity.
- **R17**: CAs using RSASSA-PSS for signing certificates SHOULD include RSASSA-PSS-params in their own subjectPublicKeyInfo; MUST include RSASSA-PSS-params in signatureAlgorithm parameters in TBSCertificate/TBSCertList.
- **R18**: Entities validating RSASSA-PSS signatures MUST support SHA-1; MAY support other hashes in Section 2.1.
- RSASSA-PSS-params structure:
  - hashAlgorithm [0] DEFAULT sha1Identifier
  - maskGenAlgorithm [1] DEFAULT mgf1SHA1Identifier
  - saltLength [2] DEFAULT 20
  - trailerField [3] DEFAULT 1 (MUST be 1; others not supported)
- **R19**: Implementations that perform signature generation MUST omit hashAlgorithm field when SHA-1 is used.
- **R20**: Implementations that perform signature validation MUST recognize both sha1Identifier and absent hashAlgorithm field as SHA-1.
- **R21**: It is strongly RECOMMENDED that underlying hash for MGF1 be same as hashAlgorithm.
- **R22**: Implementations that perform signature generation MUST omit maskGenAlgorithm field when MGF1 with SHA-1 is used.
- **R23**: Implementations MUST accept both absent field and explicit mgf1SHA1Identifier for maskGenAlgorithm.
- **R24**: saltLength recommended to be number of octets in hash value; may vary per signature.
- **R25**: trailerField MUST be 1; generation MUST omit field (value 1); validation MUST accept present with value 1 or absent.

### 3.2. RSASSA-PSS Signature Values
- **R26**: Signature value is octet string same length as RSA modulus n.
- **R27**: To convert to bit string for certificates/CRLs: most significant bit of first octet becomes first bit, etc.

### 3.3. RSASSA-PSS Signature Parameter Validation
- **R28**: Three scenarios:
  1. Key identified by rsaEncryption: no parameter validation needed.
  2. Key identified by id-RSASSA-PSS with absent parameters: no parameter validation needed.
  3. Key identified by id-RSASSA-PSS with present parameters: all parameters in signature algorithm identifier MUST match those in key structure except saltLength, which MUST be greater or equal.

## 4. RSAES-OAEP Key Transport Algorithm

### 4.1. RSAES-OAEP Public Keys
- **R29**: Conforming CAs and applications MUST support RSAES-OAEP with SHA-1; MAY support other hashes.
- **R30**: CAs issuing certificates with id-RSAES-OAEP SHOULD require presence of parameters in subjectPublicKeyInfo for all certificates.
- **R31**: Entities using certificate with id-RSAES-OAEP and absent parameters SHOULD use default parameters.
- **R32**: Entities using certificate with rsaEncryption SHOULD use default RSAES-OAEP parameters.
- **R33**: When id-RSAES-OAEP used in AlgorithmIdentifier, parameters MUST employ RSAES-OAEP-params syntax. Parameters may be absent or present in subjectPublicKeyInfo; MUST be present in encryption algorithm identifier.
- RSAES-OAEP-params structure:
  - hashFunc [0] DEFAULT sha1Identifier
  - maskGenFunc [1] DEFAULT mgf1SHA1Identifier
  - pSourceFunc [2] DEFAULT pSpecifiedEmptyIdentifier (id-pSpecified with zero-length OCTET STRING)
- **R34**: Implementations that perform encryption MUST omit hashFunc when SHA-1 used; decryption MUST recognize both sha1Identifier and absent hashFunc.
- **R35**: It is strongly RECOMMENDED underlying hash for maskGenFunc be same as hashFunc.
- **R36**: Implementations that perform encryption MUST omit maskGenFunc when MGF1 with SHA-1 used; decryption MUST accept both absent and mgf1SHA1Identifier.
- **R37**: Implementations MUST represent encoding parameters P by algorithm identifier id-pSpecified; default is zero-length string.
- **R38**: Implementations that perform encryption MUST omit pSourceFunc when zero-length P used; decryption MUST recognize both id-pSpecified and absent pSourceFunc as zero-length P.
- **R39**: Compliant implementations MUST NOT use any value other than id-pSpecified for pSourceFunc.

## 5. PKCS #1 Version 1.5 Signature Algorithm
- **R40**: When using SHA-224, SHA-256, SHA-384, or SHA-512 with PKCS #1 v1.5 signature, the respective OIDs (sha224WithRSAEncryption { pkcs-1 14 }, etc.) MUST be used.
- **R41**: When these OIDs appear in AlgorithmIdentifier, parameters MUST be NULL; implementations MUST accept absent parameters as well.
- RSASSA-PSS is preferred over PKCS #1 v1.5 signature; transition recommended.

## 6. ASN.1 Module
(Full module provided in document; includes definitions for OIDs, constants, algorithm identifiers, RSASSA-PSS-params, RSAES-OAEP-params, RSAPublicKey. Normative ASN.1.)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | rsaEncryption OID with NULL parameters for unrestricted RSA keys | MUST | §1.2 |
| R2 | id-RSASSA-PSS OID with RSASSA-PSS-params when restricting to RSASSA-PSS | MUST | §1.2 |
| R3 | id-RSAES-OAEP OID with RSAES-OAEP-params when restricting to RSAES-OAEP | MUST | §1.2 |
| R4 | RSA public key encoded as RSAPublicKey | MUST | §1.2 |
| R5 | keyUsage for id-RSASSA-PSS end-entity: nonRepudiation and/or digitalSignature | MUST | §1.2 |
| R6 | keyUsage for id-RSASSA-PSS CA: one or more of nonRepudiation, digitalSignature, keyCertSign, cRLSign | MUST | §1.2 |
| R7 | Certificate user must perform RSASSA-PSS with parameters from key if present | MUST | §1.2 |
| R8 | keyUsage for id-RSAES-OAEP: only keyEncipherment and/or dataEncipherment; both SHOULD NOT be present | MUST/SHOULD | §1.2 |
| R9 | Certificate user must perform RSAES-OAEP with parameters from key if present | MUST | §1.2 |
| R10 | Accept both NULL and absent parameters for SHA OIDs | MUST | §2.1 |
| R11 | Hash algorithm identifiers defined with NULL parameters | (definition) | §2.1 |
| R12 | Only MGF1 supported for RSASSA-PSS and RSAES-OAEP | MUST | §2.2 |
| R13 | MGF1 parameters must contain HashAlgorithm | MUST | §2.2 |
| R14 | Support default MGF1 SHA-1; MAY support other | MUST/MAY | §2.2 |
| R15 | id-RSASSA-PSS params must be RSASSA-PSS-params; present in signature algorithm | MUST | §3.1 |
| R16 | CAs SHOULD require parameters in subjectPublicKeyInfo if cA; MAY for end-entity | SHOULD/MAY | §3.1 |
| R17 | CAs signing with RSASSA-PSS: include params in own subjectPublicKeyInfo SHOULD; in TBSCertificate/TBSCertList MUST | SHOULD/MUST | §3.1 |
| R18 | Validators must support SHA-1; MAY support others | MUST/MAY | §3.1 |
| R19 | Omit hashAlgorithm when SHA-1 in generation | MUST | §3.1 |
| R20 | Recognize both sha1Identifier and absent for SHA-1 in validation | MUST | §3.1 |
| R21 | Strongly recommend same hash for MGF1 | RECOMMENDED | §3.1 |
| R22 | Omit maskGenAlgorithm when MGF1 with SHA-1 in generation | MUST | §3.1 |
| R23 | Accept both absent and explicit mgf1SHA1Identifier | MUST | §3.1 |
| R24 | saltLength recommended = hash output length | (recommendation) | §3.1 |
| R25 | trailerField must be 1; omit in generation; accept present 1 or absent | MUST | §3.1 |
| R26 | Signature value octet string length = modulus length | (specification) | §3.2 |
| R27 | Convert to bit string: MSB first | SHALL | §3.2 |
| R28 | Parameter validation rules for three scenarios | (see §3.3) | §3.3 |
| R29 | Support RSAES-OAEP with SHA-1; MAY support others | MUST/MAY | §4 |
| R30 | CAs SHOULD require parameters for id-RSAES-OAEP | SHOULD | §4.1 |
| R31 | Use default params if absent in certificate with id-RSAES-OAEP | SHOULD | §4.1 |
| R32 | Use default params if using rsaEncryption | SHOULD | §4.1 |
| R33 | id-RSAES-OAEP params must be RSAES-OAEP-params; present in encryption algorithm identifier | MUST | §4.1 |
| R34 | Omit hashFunc when SHA-1 in encryption; recognize both in decryption | MUST | §4.1 |
| R35 | Strongly recommend same hash for maskGenFunc | RECOMMENDED | §4.1 |
| R36 | Omit maskGenFunc when MGF1 with SHA-1 in encryption; accept both in decryption | MUST | §4.1 |
| R37 | Represent P with id-pSpecified; default empty string | MUST | §4.1 |
| R38 | Omit pSourceFunc when empty P in encryption; recognize both in decryption | MUST | §4.1 |
| R39 | Do not use other than id-pSpecified for pSourceFunc | MUST NOT | §4.1 |
| R40 | Use appropriate OID for SHA-224/256/384/512 with PKCS#1 v1.5 | MUST | §5 |
| R41 | Parameters MUST be NULL for those OIDs; accept absent | MUST | §5 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 8)**: Protects RSA private key; uses adequate PRNG; recommends against using same RSA key pair for multiple schemes (avoids cross-scheme vulnerabilities). Emphasizes using same hash for hashAlgorithm and maskGenAlgorithm in both RSASSA-PSS and RSAES-OAEP. Notes SHA-1 collision attack (2^69) reduces security; suggests SHA-256/384/512 for higher security. Recommends 1024-bit RSA public keys currently supported, with transition to 2048-bit and SHA-256 by end of 2007. The NIST guideline suggests 80-bit security adequate until 2010-2015. The ASN.1 module includes identifiers for all five hashes.
- **IANA Considerations (Section 9)**: All OIDs used are assigned in PKCS or by NIST; no further IANA action needed.