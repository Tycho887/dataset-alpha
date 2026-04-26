# RFC 2437: PKCS #1: RSA Cryptography Specifications Version 2.0
**Source**: RSA Laboratories | **Version**: 2.0 | **Date**: October 1998 | **Type**: Informational  
**Original**: https://tools.ietf.org/html/rfc2437

## Scope (Summary)
This document provides recommendations for the implementation of public‑key cryptography based on the RSA algorithm, covering cryptographic primitives (encryption/decryption and signature/verification), encryption schemes (RSAES‑OAEP and RSAES‑PKCS1‑v1_5), a signature scheme with appendix (RSASSA‑PKCS1‑v1_5), and ASN.1 syntax for representing keys and identifying schemes.

## Normative References
- [1] ANSI X9.44: Key Management Using Reversible Public Key Cryptography (work in progress)
- [2] M. Bellare and P. Rogaway, *Optimal Asymmetric Encryption – How to Encrypt with RSA*, Eurocrypt ’94
- [6] CCITT Recommendation X.509 (1988)
- [14] IEEE P1363: Standard Specifications for Public Key Cryptography (draft)
- [15] Kaliski, B., “The MD2 Message-Digest Algorithm”, RFC 1319, April 1992
- [16] NIST FIPS PUB 180-1: Secure Hash Standard, April 1994
- [17] Rivest, R., “The MD5 Message-Digest Algorithm”, RFC 1321, April 1992
- [18] R. Rivest, A. Shamir, L. Adleman, *A Method for Obtaining Digital Signatures and Public-Key Cryptosystems*, CACM 21(2), 1978
- [20] RSA Laboratories, PKCS #1 v1.5, November 1993
- [21] RSA Laboratories, PKCS #7 v1.5, November 1993
- [22] RSA Laboratories, PKCS #8 v1.2, November 1993
- [23] RSA Laboratories, PKCS #12 v1.0 (work in progress)

## Definitions and Abbreviations
- **(n, e)**: RSA public key
- **c**: ciphertext representative (integer 0..n-1)
- **C**: ciphertext (octet string)
- **d**: private exponent
- **dP, dQ**: CRT exponents (d mod (p‑1), d mod (q‑1))
- **e**: public exponent
- **EM**: encoded message (octet string)
- **emLen**: intended length in octets of an encoded message
- **H**: hash value
- **Hash**: hash function
- **hLen**: output length in octets of Hash
- **K**: RSA private key
- **k**: length in octets of the modulus
- **l**: intended length of octet string
- **lcm**: least common multiple
- **m**: message representative (integer 0..n-1)
- **M**: message (octet string)
- **MGF**: mask generation function
- **n**: modulus
- **P**: encoding parameters (octet string)
- **p, q**: prime factors of n
- **qInv**: CRT coefficient (q⁻¹ mod p)
- **s**: signature representative (integer 0..n-1)
- **S**: signature (octet string)
- **x**: nonnegative integer
- **X**: octet string corresponding to x
- **\xor**: bitwise exclusive‑or
- **\lambda(n)**: lcm(p‑1, q‑1)
- **||**: concatenation operator
- **||.||**: octet length operator

## 3. Key Types
### 3.1 RSA Public Key
- **Definition**: An RSA public key consists of two components:
  - **n**: the modulus (nonnegative integer)
  - **e**: the public exponent (nonnegative integer)
- **Validity**: In a valid RSA public key, n is the product of two odd primes p and q, and e is an integer between 3 and n‑1 satisfying gcd(e, λ(n)) = 1, where λ(n) = lcm(p‑1, q‑1).
- **Interchange syntax**: Section 11.1.1 provides a recommended ASN.1 syntax; internal representation may differ.

### 3.2 RSA Private Key
- Two representations:
  1. **(n, d)**: modulus and private exponent.
  2. **(p, q, dP, dQ, qInv)**: CRT components.
- **Validity**:
  - For representation 1: ed ≡ 1 (mod λ(n)), where e is the corresponding public exponent.
  - For representation 2: e·dP ≡ 1 (mod p‑1), e·dQ ≡ 1 (mod q‑1), q·qInv ≡ 1 (mod p).
- **Interchange syntax**: Section 11.1.2 provides a recommended ASN.1 syntax that includes both representations; internal representation may differ.

## 4. Data Conversion Primitives
### 4.1 I2OSP (Integer‑to‑Octet‑String Primitive)
- **I2OSP(x, l)**: Converts nonnegative integer x to an octet string of length l.
- **Steps**:
  1. If x ≥ 256^l, output “integer too large” and stop.
  2. Write x in base 256: x = x_{l-1}256^{l-1} + … + x_0.
  3. Output X₁ X₂ … X_l where X_i has value x_{l-i}.

### 4.2 OS2IP (Octet‑String‑to‑Integer Primitive)
- **OS2IP(X)**: Converts octet string X to a nonnegative integer.
- **Steps**:
  1. Let X₁ X₂ … X_l be the octets; assign x_{l-i} = X_i.
  2. Compute x = Σ x_{l-i}·256^{l-i}.
  3. Output x.

## 5. Cryptographic Primitives
### 5.1 Encryption and Decryption Primitives
#### 5.1.1 RSAEP (RSA Encryption Primitive)
- **Input**: (n, e), m (message representative, 0 ≤ m < n)
- **Output**: c = m^e mod n (ciphertext representative); or “message representative out of range”
- **Assumption**: public key is valid
- **Step**: If m not in [0, n‑1], output error; else c = m^e mod n.

#### 5.1.2 RSADP (RSA Decryption Primitive)
- **Input**: K (private key in one of two forms), c (ciphertext representative, 0 ≤ c < n)
- **Output**: m (message representative); or “ciphertext representative out of range”
- **Assumption**: private key is valid
- **Steps**:
  1. If c not in [0, n‑1], output error.
  2. If K is (n, d): m = c^d mod n.
  3. If K is (p, q, dP, dQ, qInv):
     - m₁ = c^dP mod p
     - m₂ = c^dQ mod q
     - h = qInv·(m₁ – m₂) mod p
     - m = m₂ + h·q
  4. Output m.

### 5.2 Signature and Verification Primitives
#### 5.2.1 RSASP1 (RSA Signature Primitive)
- **Input**: K (private key), m (message representative, 0 ≤ m < n)
- **Output**: s (signature representative); or “message representative out of range”
- **Steps**: Identical to RSADP but outputs s.

#### 5.2.2 RSAVP1 (RSA Verification Primitive)
- **Input**: (n, e), s (signature representative, 0 ≤ s < n)
- **Output**: m = s^e mod n; or “invalid”
- **Steps**: If s not in [0, n‑1], output “invalid”; else m = s^e mod n.

## 6. Overview of Schemes
- A scheme combines cryptographic primitives with other techniques.
- Two types in this document: encryption schemes and signature schemes with appendix.
- Operations assume valid keys; key management is outside scope.

## 7. Encryption Schemes
### 7.1 RSAES‑OAEP
- **Combines**: RSAEP/RSADP with EME‑OAEP encoding (Section 9.1.1).
- **Message length limit**: up to k – 2 – 2hLen octets.
- **Security**: provides “plaintext‑aware encryption” (computationally infeasible to obtain full/partial information or generate valid ciphertext without knowing message); chosen‑ciphertext attack ineffective.
- **Note**: Should not be used in a protocol that also uses RSAES‑PKCS1‑v1_5 (risk of adaptive chosen‑ciphertext attack).

#### 7.1.1 Encryption Operation
- **RSAES‑OAEP‑ENCRYPT((n, e), M, P)**: produces ciphertext C of length k.
- **Steps**:
  1. EM = EME‑OAEP‑ENCODE(M, P, k‑1) – if “message too long”, stop.
  2. m = OS2IP(EM)
  3. c = RSAEP((n, e), m)
  4. C = I2OSP(c, k)
  5. Output C.

#### 7.1.2 Decryption Operation
- **RSAES‑OAEP‑DECRYPT(K, C, P)**: produces message M.
- **Steps**:
  1. If length(C) ≠ k, output “decryption error”.
  2. c = OS2IP(C)
  3. m = RSADP(K, c) – if error, output “decryption error”.
  4. EM = I2OSP(m, k‑1) – if “integer too large”, output “decryption error”.
  5. M = EME‑OAEP‑DECODE(EM, P) – if “decoding error”, output “decryption error”.
  6. Output M.
- **Important**: error messages in steps 4 and 5 must be identical to prevent chosen‑ciphertext attacks.

### 7.2 RSAES‑PKCS1‑v1_5
- **Combines**: RSAEP/RSADP with EME‑PKCS1‑v1_5 encoding.
- **Message length limit**: up to k‑11 octets.
- **Security**: Not plaintext‑aware; countermeasures (e.g., structure, rigorous conformance checking, consolidated error messages) recommended against [4] chosen‑ciphertext attack.
- **Recommendations**: Pseudorandom octets should be independently generated for each encryption; PS must be at least 8 octets; use small messages to thwart Coppersmith et al. attacks.

#### 7.2.1 Encryption Operation
- **RSAES‑PKCS1‑V1_5‑ENCRYPT((n, e), M)**: produces ciphertext C.
- **Steps**:
  1. EM = EME‑PKCS1‑V1_5‑ENCODE(M, k‑1) – if “message too long”, stop.
  2. m = OS2IP(EM)
  3. c = RSAEP((n, e), m)
  4. C = I2OSP(c, k)
  5. Output C.

#### 7.2.2 Decryption Operation
- **RSAES‑PKCS1‑V1_5‑DECRYPT(K, C)**: produces message M.
- **Steps**:
  1. If length(C) ≠ k, output “decryption error”.
  2. c = OS2IP(C)
  3. m = RSADP((n, d), c) – if error, “decryption error”.
  4. EM = I2OSP(m, k‑1) – if error, “decryption error”.
  5. M = EME‑PKCS1‑V1_5‑DECODE(EM) – if error, “decryption error”.
  6. Output M.
- **Note**: Only one type of error message must be output.

## 8. Signature Schemes with Appendix
### 8.1 RSASSA‑PKCS1‑v1_5
- **Combines**: RSASP1/RSAVP1 with EMSA‑PKCS1‑v1_5 encoding.
- **Message length**: unrestricted or limited by hash function.
- **Security**: computationally infeasible to forge signatures; hash function identifier embedded in encoding.

#### 8.1.1 Signature Generation
- **RSASSA‑PKCS1‑V1_5‑SIGN(K, M)**: produces signature S of length k.
- **Steps**:
  1. EM = EMSA‑PKCS1‑V1_5‑ENCODE(M, k‑1) – if “message too long”, stop; if “intended encoded message length too short”, output “modulus too short”.
  2. m = OS2IP(EM)
  3. s = RSASP1(K, m)
  4. S = I2OSP(s, k)
  5. Output S.

#### 8.1.2 Signature Verification
- **RSASSA‑PKCS1‑V1_5‑VERIFY((n, e), M, S)**: outputs “valid signature”, “invalid signature”, “message too long”, or “modulus too short”.
- **Steps**:
  1. If length(S) ≠ k, output “invalid signature”.
  2. s = OS2IP(S)
  3. m = RSAVP1((n, e), s) – if “invalid”, output “invalid signature”.
  4. EM = I2OSP(m, k‑1) – if error, “invalid signature”.
  5. EM’ = EMSA‑PKCS1‑V1_5‑ENCODE(M, k‑1) – if error, output corresponding error.
  6. Compare EM and EM’; if equal, “valid signature”, else “invalid signature”.

## 9. Encoding Methods
### 9.1 Encoding Methods for Encryption
#### 9.1.1 EME‑OAEP
- **Parameterized by**: Hash and MGF.
- **Encoding operation (EME‑OAEP‑ENCODE)**:
  - Input: M, P, emLen (≥ 2hLen+1).
  - Steps: check lengths, generate pHash = Hash(P), construct DB = pHash || PS (zeros) || 01 || M, generate random seed, compute maskedDB = DB ⊕ MGF(seed, emLen‑hLen), maskedSeed = seed ⊕ MGF(maskedDB, hLen), output maskedSeed || maskedDB.
  - Output: EM of length emLen; or “message too long” / “parameter string too long”.
- **Decoding operation (EME‑OAEP‑DECODE)**:
  - Input: EM (≥ 2hLen+1), P.
  - Steps: check length, separate maskedSeed and maskedDB, recover seed and DB, verify pHash and separator 01, output M or “decoding error”.
- **Note**: pHash = Hash(P); default P is empty string.

#### 9.1.2 EME‑PKCS1‑v1_5
- **Encoding operation (EME‑PKCS1‑V1_5‑ENCODE)**:
  - Input: M (length ≤ emLen‑10), emLen.
  - Steps: generate PS of length emLen‑||M||‑2 pseudorandom nonzero octets (≥ 8), output EM = 02 || PS || 00 || M.
  - Output: EM; or “message too long”.
- **Decoding operation (EME‑PKCS1‑V1_5‑DECODE)**:
  - Input: EM (length ≥ 10).
  - Steps: separate EM as 02 || PS || 00 || M; check first octet is 02, existence of 00, PS length ≥ 8; output M or “decoding error”.

### 9.2 Encoding Methods for Signatures with Appendix
#### 9.2.1 EMSA‑PKCS1‑v1_5
- **Encoding operation (EMSA‑PKCS1‑V1_5‑ENCODE)**:
  - Input: M, emLen (≥ ||T|| + 10).
  - Steps: compute H = Hash(M); encode DigestInfo (see Section 11) including algorithm ID and hash value as DER T; generate PS of emLen‑||T||‑2 FF octets (≥ 8); output EM = 01 || PS || 00 || T.
  - Output: EM; or “message too long” or “intended encoded message length too short”.

## 10. Auxiliary Functions
### 10.1 Hash Functions
- **Properties**: deterministic, collision‑resistant; should also be one‑way.
- **Recommended**:
  - For EME‑OAEP: SHA‑1 only.
  - For EMSA‑PKCS1‑v1_5: SHA‑1 for new applications; MD2 and MD5 for compatibility.
- **Note**: MD4 is no longer allowed due to cryptanalytic advances.

### 10.2 Mask Generation Functions
- **Properties**: deterministic, pseudorandom output.
#### 10.2.1 MGF1
- **Input**: Z (seed), l (desired length, ≤ 2^32·hLen).
- **Steps**:
  1. If l > 2^32·hLen, output “mask too long”.
  2. Initialize T empty.
  3. For counter = 0 to ⌈l/hLen⌉‑1: C = I2OSP(counter,4); T = T || Hash(Z || C).
  4. Output first l octets of T as mask.

## 11. ASN.1 Syntax
### 11.1 Key Representation
- **Object Identifier**: rsaEncryption = {pkcs‑1 1}; parameters field shall be NULL.
#### 11.1.1 Public‑key Syntax
- **RSAPublicKey** ::= SEQUENCE { modulus INTEGER (n), publicExponent INTEGER (e) }
#### 11.1.2 Private‑key Syntax
- **RSAPrivateKey** ::= SEQUENCE {
    version Version (shall be 0 for this version),
    modulus INTEGER (n),
    publicExponent INTEGER (e),
    privateExponent INTEGER (d),
    prime1 INTEGER (p),
    prime2 INTEGER (q),
    exponent1 INTEGER (d mod (p‑1)),
    exponent2 INTEGER (d mod (q‑1)),
    coefficient INTEGER (q⁻¹ mod p) }

### 11.2 Scheme Identification
#### 11.2.1 Syntax for RSAES‑OAEP
- **OID**: id‑RSAES‑OAEP = {pkcs‑1 7}
- **Parameters** (RSAES‑OAEP‑params): SEQUENCE { hashFunc [0] AlgorithmIdentifier (default SHA‑1), maskGenFunc [1] AlgorithmIdentifier (default MGF1‑SHA‑1), pSourceFunc [2] AlgorithmIdentifier (default pSpecifiedEmpty) }
- **Default**: SHA‑1, MGF1 with SHA‑1, empty encoding parameters.
- **Requirements**:
  - hashFunc OID shall be in oaepDigestAlgorithms (only id‑sha1); parameters shall be NULL.
  - maskGenFunc OID shall be in pkcs1MGFAlgorithms (only id‑mgf1); parameters shall be AlgorithmIdentifier with hash OID from oaepDigestAlgorithms.
  - pSourceFunc OID shall be in pkcs1pSourceAlgorithms (only id‑pSpecified); parameters shall be OCTET STRING containing encoding parameters.

#### 11.2.2 Syntax for RSAES‑PKCS1‑v1_5
- **OID**: rsaEncryption = {pkcs‑1 1}; parameters field shall be NULL.

#### 11.2.3 Syntax for RSASSA‑PKCS1‑v1_5
- **OID** depends on hash:
  - MD2: md2WithRSAEncryption = {pkcs‑1 2}
  - MD5: md5WithRSAEncryption = {pkcs‑1 4}
  - SHA‑1: sha1WithRSAEncryption = {pkcs‑1 5}
- **Parameters field shall be NULL**.
- **DigestInfo** for EMSA‑PKCS1‑v1_5: SEQUENCE { digestAlgorithm AlgorithmIdentifier, digest OCTET STRING }

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | In a valid RSA public key, the modulus n shall be a product of two odd primes p and q, and the public exponent e shall be an integer between 3 and n‑1 satisfying gcd(e, λ(n)) = 1. | validity | Section 3.1 |
| R2 | In a valid RSA private key (first representation), the private exponent d shall satisfy ed ≡ 1 (mod λ(n)). | validity | Section 3.2 |
| R3 | In a valid RSA private key (second representation), dP, dQ, qInv shall satisfy e·dP ≡ 1 (mod p‑1), e·dQ ≡ 1 (mod q‑1), q·qInv ≡ 1 (mod p). | validity | Section 3.2 |
| R4 | I2OSP shall output “integer too large” if x ≥ 256^l. | shall | Section 4.1, Step 1 |
| R5 | RSAEP: If the message representative m is not between 0 and n‑1, output “message representative out of range”. | shall | Section 5.1.1, Step 1 |
| R6 | RSADP: If the ciphertext representative c is not between 0 and n‑1, output “ciphertext representative out of range”. | shall | Section 5.1.2, Step 1 |
| R7 | RSASP1: If the message representative m is not between 0 and n‑1, output “message representative out of range”. | shall | Section 5.2.1, Step 1 |
| R8 | RSAVP1: If the signature representative s is not between 0 and n‑1, output “invalid”. | shall | Section 5.2.2, Step 1 |
| R9 | In RSAES‑OAEP decryption, error messages in steps 4 and 5 shall be identical. | shall | Section 7.1.2, Note |
| R10 | In RSAES‑PKCS1‑v1_5, the padding string PS shall be at least 8 octets. | shall | Section 7.2, Note (construction) |
| R11 | In EMSA‑PKCS1‑v1_5, the encoded message length shall be at least ||T|| + 10. | requirement | Section 9.2.1, Step 3 |
| R12 | For the OID rsaEncryption, the parameters field in an AlgorithmIdentifier shall be NULL. | shall | Section 11.1 |
| R13 | In RSASSA‑PKCS1‑v1_5, the parameters field in the AlgorithmIdentifier shall be NULL. | shall | Section 11.2.3 |
| R14 | In RSAES‑OAEP parameters, the hashFunc OID shall be in oaepDigestAlgorithms, the maskGenFunc OID shall be in pkcs1MGFAlgorithms, and the pSourceFunc OID shall be in pkcs1pSourceAlgorithms. | shall | Section 11.2.1 |
| R15 | The version field in RSAPrivateKey shall be 0 for this version. | shall | Section 11.1.2 |

## Informative Annexes (Condensed)
- **Security Considerations**: Discussed throughout the document.
- **Acknowledgements**: Based on RSA Laboratories contribution; must acknowledge RSA Data Security, Inc. when using text.
- **Patent Statement**: RSA patent (US 4,405,829) is held by MIT with exclusive sub‑licensing to RSA Data Security, Inc. Licenses available on reasonable and non‑discriminatory terms. The Internet Society takes no position on validity.
- **Revision History**: Versions 1.0–1.3 distributed to PKCS participants; v1.4 initial public release; v1.5 added MD4; v2.0 introduces RSAES‑OAEP, drops MD4, and updates structure.
- **Full Copyright Statement**: Copyright (C) The Internet Society (1998). All Rights Reserved. Permission to copy and distribute with copyright notice.