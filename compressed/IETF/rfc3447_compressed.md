# RFC 3447: Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1
**Source**: RSA Laboratories (via IETF) | **Version**: 2.1 | **Date**: February 2003 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc3447

## Scope (Summary)
This document defines RSA public-key cryptography primitives, encryption schemes (RSAES-OAEP, RSAES-PKCS1-v1_5), signature schemes with appendix (RSASSA-PSS, RSASSA-PKCS1-v1_5), and ASN.1 syntax for keys and scheme identification. It supersedes PKCS #1 v2.0 (RFC 2437) and is compatible with IEEE 1363-2000.

## Normative References
- ANSI X9.44 (Draft D2)
- IEEE Std 1363-2000
- IEEE P1363a Draft
- NIST FIPS 180-1 (SHA-1), Draft FIPS 180-2 (SHA-256/384/512)
- RFC 1319 (MD2), RFC 1321 (MD5)
- PKCS #7, #8, #12
- [3] Bellare & Rogaway, OAEP
- [4][5] Bellare & Rogaway, PSS
- [37] Handbook of Applied Cryptography
- [42] RSA Original Paper
- Other references cited in text.

## Definitions and Abbreviations
- **c, C**: ciphertext representative (int), ciphertext (octet string)
- **d**: RSA private exponent
- **d_i, dP, dQ**: CRT exponents for additional factors, p, q
- **e**: RSA public exponent
- **EM**: encoded message (octet string)
- **emBits, emLen**: length in bits/octets of EM
- **GCD**: greatest common divisor
- **Hash**: hash function; **hLen**: output length in octets
- **k**: length in octets of RSA modulus n
- **K**: RSA private key
- **L**: optional label (octet string) for RSAES-OAEP
- **LCM**: least common multiple
- **m, M**: message representative (int), message (octet string)
- **MGF**: mask generation function; **mgfSeed**: seed; **maskLen**: output length
- **n**: RSA modulus (product of u primes)
- **(n, e)**: RSA public key
- **p, q**: first two prime factors
- **qInv**: CRT coefficient (inverse of q mod p)
- **r_i**: prime factors (i=3..u)
- **s, S**: signature representative (int), signature (octet string)
- **sLen**: salt length (EMSA-PSS)
- **u**: number of prime factors (≥2)
- **0x**: hexadecimal prefix
- **\lambda(n)**: LCM(r_1-1,...,r_u-1)
- **\xor**: bitwise XOR
- **\ceil**: ceiling function
- **||**: concatenation
- **==**: congruence (mod n)

## 3. Key Types
### 3.1 RSA Public Key
- **Components**: `n` (modulus, product of u distinct odd primes, u≥2) and `e` (public exponent, 3..n-1, GCD(e, λ(n))=1).
- **Syntax**: RSAPublicKey ::= SEQUENCE { modulus INTEGER, publicExponent INTEGER }.

### 3.2 RSA Private Key
- Two representations:
  1. `(n, d)` where `e * d ≡ 1 (mod λ(n))`.
  2. Quintuple `(p, q, dP, dQ, qInv)` plus optional triplets `(r_i, d_i, t_i)` for i=3..u. Conditions:
     - `e * dP ≡ 1 (mod p-1)`, `e * dQ ≡ 1 (mod q-1)`
     - `q * qInv ≡ 1 (mod p)`
     - For i≥3: `e * d_i ≡ 1 (mod r_i-1)`, `R_i * t_i ≡ 1 (mod r_i)` where `R_i = r_1 * ... * r_(i-1)`.
- **Syntax**: RSAPrivateKey (version 0 or 1, otherPrimeInfos for multi-prime).

## 4. Data Conversion Primitives
### 4.1 I2OSP (Integer-to-Octet-String)
- **I2OSP(x, xLen)**: Convert integer x ≥ 0 to octet string of length xLen. Error "integer too large" if x ≥ 256^xLen.
  - Steps: write x in base 256, produce octets.

### 4.2 OS2IP (Octet-String-to-Integer)
- **OS2IP(X)**: Convert octet string X to nonnegative integer x.
  - Steps: interpret octets as base-256 digits.

## 5. Cryptographic Primitives
### 5.1 Encryption/Decryption: RSAEP / RSADP
- **RSAEP((n,e), m)**: Output `c = m^e mod n`. Error if m not in [0,n-1].
- **RSADP(K, c)**: Output m = c^d mod n (first form) or via CRT (second form using m_1, m_2, h, m). Error if c not in [0,n-1].

### 5.2 Signature/Verification: RSASP1 / RSAVP1
- **RSASP1(K, m)**: Output `s = m^d mod n` or CRT equivalent. Error if m not in [0,n-1].
- **RSAVP1((n,e), s)**: Output `m = s^e mod n`. Error if s not in [0,n-1].

## 6. Overview of Schemes
- Schemes combine primitives with encoding methods. This document specifies encryption (RSAES-OAEP, RSAES-PKCS1-v1_5) and signature with appendix (RSASSA-PSS, RSASSA-PKCS1-v1_5).
- **Recommendation**: Use given key pair in only one scheme. New applications should prefer RSAES-OAEP and RSASSA-PSS.

## 7. Encryption Schemes
### 7.1 RSAES-OAEP
- **Parameters**: Hash, MGF. Label L default empty string.
- **Message length**: ≤ k - 2hLen - 2 octets.
- **Security**: Provably secure against CCA2 under RSA assumption (random oracle model). See security notes.
- **RSAES-OAEP-ENCRYPT((n,e), M, L)**:
  1. Check lengths: L ≤ hash input limit; mLen ≤ k-2hLen-2.
  2. EME-OAEP encoding: generate lHash = Hash(L); PS = zero octets; DB = lHash || PS || 0x01 || M; seed random; dbMask = MGF(seed, k-hLen-1); maskedDB = DB XOR dbMask; seedMask = MGF(maskedDB, hLen); maskedSeed = seed XOR seedMask; EM = 0x00 || maskedSeed || maskedDB.
  3. RSA encryption: m = OS2IP(EM); c = RSAEP((n,e), m); C = I2OSP(c, k).
- **RSAES-OAEP-DECRYPT(K, C, L)**:
  1. Length checks.
  2. RSA decryption: c = OS2IP(C); m = RSADP(K, c); EM = I2OSP(m, k).
  3. EME-OAEP decoding: separate Y, maskedSeed, maskedDB; recover seed, DB; separate lHash', PS, M; error if Y≠0, lHash'≠lHash, or no 0x01 separator.
  4. Output M. **Note**: Handle errors uniformly to prevent side-channel attacks.

### 7.2 RSAES-PKCS1-v1_5 (for compatibility, not recommended for new apps)
- **Message length**: ≤ k - 11 octets.
- **RSAES-PKCS1-V1_5-ENCRYPT((n,e), M)**:
  1. Check mLen ≤ k-11.
  2. EME-PKCS1-v1_5: PS = pseudo-random nonzero octets (≥8); EM = 0x00 || 0x02 || PS || 0x00 || M.
  3. RSA encryption as above.
- **RSAES-PKCS1-V1_5-DECRYPT(K, C)**:
  1. Length check (k≥11).
  2. RSA decryption to EM.
  3. Decode: EM = 0x00 || 0x02 || PS || 0x00 || M; error if format not matched or PS<8 octets.
  4. Output M. **Note**: Prevent timing/error-message leakage.

## 8. Signature Schemes with Appendix
### 8.1 RSASSA-PSS (recommended for new apps)
- **Parameters**: Hash, MGF, salt length (sLen). Defaults: SHA-1, MGF1 with SHA-1, sLen=20.
- **Message length**: limited only by hash input limit.
- **Security**: Provably secure (tight reduction to RSA inversion) assuming hash and MGF are random oracles.
- **RSASSA-PSS-SIGN(K, M)**:
  1. Encode: EM = EMSA-PSS-ENCODE(M, modBits-1). (modBits = bit length of n)
  2. RSA signature: m = OS2IP(EM); s = RSASP1(K, m); S = I2OSP(s, k).
- **RSASSA-PSS-VERIFY((n,e), M, S)**:
  1. Check signature length = k.
  2. RSA verification: s = OS2IP(S); m = RSAVP1((n,e), s); EM = I2OSP(m, emLen).
  3. EMSA-PSS verification: Result = EMSA-PSS-VERIFY(M, EM, modBits-1).
  4. Output "valid" if consistent.

### 8.2 RSASSA-PKCS1-v1_5 (compatibility, gradual transition to PSS)
- **Parameters**: Hash (one of MD2, MD5, SHA-1, SHA-256, SHA-384, SHA-512). OID selection.
- **RSASSA-PKCS1-V1_5-SIGN(K, M)**:
  1. Encode: EM = EMSA-PKCS1-V1_5-ENCODE(M, k).
  2. RSA signature as above.
- **RSASSA-PKCS1-V1_5-VERIFY((n,e), M, S)**:
  1. Check S length = k.
  2. RSA verification to get EM.
  3. Encode M to EM' (same encoding).
  4. Compare EM and EM'; output "valid" if match.

## 9. Encoding Methods for Signatures
### 9.1 EMSA-PSS (Probabilistic)
- **EMSA-PSS-ENCODE(M, emBits)**: emBits ≥ 8hLen+8sLen+9
  1. mHash = Hash(M). Error if message too long.
  2. Check emLen ≥ hLen+sLen+2.
  3. Generate random salt of length sLen.
  4. M' = 8 zero octets || mHash || salt.
  5. H = Hash(M').
  6. PS = zero octets (emLen - sLen - hLen - 2).
  7. DB = PS || 0x01 || salt.
  8. dbMask = MGF(H, emLen - hLen - 1).
  9. maskedDB = DB XOR dbMask; set leftmost bits to zero (to meet emBits).
  10. EM = maskedDB || H || 0xbc.
- **EMSA-PSS-VERIFY(M, EM, emBits)**:
  1. mHash = Hash(M); check lengths.
  2. Check last octet = 0xbc; extract maskedDB and H.
  3. Zero bit check on maskedDB.
  4. Compute dbMask, DB, zero bits.
  5. Verify PS (all zeros until 0x01), extract salt.
  6. Compute M' and H'; compare H' with H. Output "consistent" if equal.

### 9.2 EMSA-PKCS1-v1_5 (Deterministic)
- **EMSA-PKCS1-V1_5-ENCODE(M, emLen)**: emLen ≥ tLen + 11 (tLen = length of DER-encoded DigestInfo)
  1. H = Hash(M). Error if message too long.
  2. Encode DigestInfo (SEQUENCE of digestAlgorithm and digest OCTET STRING) using DER. T = DER encoding, tLen.
  3. Check emLen ≥ tLen + 11.
  4. PS = (emLen - tLen - 3) octets of 0xff (≥8).
  5. EM = 0x00 || 0x01 || PS || 0x00 || T.
- **Notes**: For compatibility, BER encodings may be accepted (but DER recommended). Hash OIDs given in Appendix A.2.4.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | RSA public key: n product of u distinct odd primes, e in [3,n-1], GCD(e, λ(n))=1 | shall | 3.1 |
| R2 | RSA private key (first rep): n same as public, d positive < n, e*d ≡ 1 mod λ(n) | shall | 3.2 |
| R3 | RSA private key (second rep): p,q,dP,dQ,qInv correct; for i≥3: r_i,d_i,t_i correct | shall | 3.2 |
| R4 | I2OSP: error if x ≥ 256^xLen | shall | 4.1 |
| R5 | RSAEP: error if m not in [0,n-1] | shall | 5.1.1 |
| R6 | RSADP: error if c not in [0,n-1] | shall | 5.1.2 |
| R7 | RSASP1: error if m not in [0,n-1] | shall | 5.2.1 |
| R8 | RSAVP1: error if s not in [0,n-1] | shall | 5.2.2 |
| R9 | RSAES-OAEP: encrypt only if mLen ≤ k-2hLen-2 | shall | 7.1.1 |
| R10 | RSAES-OAEP: decoding must check Y, lHash, PS structure; error "decryption error" | shall | 7.1.2 |
| R11 | RSAES-OAEP: error handling must be indistinguishable | shall (note) | 7.1.2 |
| R12 | RSAES-PKCS1-v1_5: encrypt only if mLen ≤ k-11; PS non-zero, ≥8 octets | shall | 7.2.1 |
| R13 | RSAES-PKCS1-v1_5: decrypt must check PS length and structure; error "decryption error" | shall | 7.2.2 |
| R14 | RSASSA-PSS: EM produced by EMSA-PSS-ENCODE with emBits = modBits-1 | shall | 8.1.1 |
| R15 | RSASSA-PSS: verification via EMSA-PSS-VERIFY | shall | 8.1.2 |
| R16 | RSASSA-PKCS1-v1_5: EM produced by EMSA-PKCS1-V1_5-ENCODE with emLen = k | shall | 8.2.1 |
| R17 | RSASSA-PKCS1-v1_5: verification compares EM with re-encoded EM' | shall | 8.2.2 |
| R18 | EMSA-PSS: encode steps: mHash, random salt, M' construction, DB, mask, EM ends with 0xbc | shall | 9.1.1 |
| R19 | EMSA-PSS: verify steps: check trailer 0xbc, zero bits, salt extraction, H comparison | shall | 9.1.2 |
| R20 | EMSA-PKCS1-v1_5: encode includes DER-encoded DigestInfo; PS 0xff; prefix 0x00,0x01 | shall | 9.2 |
| R21 | RSA private key ASN.1: version 0 unless multi-prime; otherPrimeInfos present only if version 1 | shall | A.1.2 |
| R22 | RSAES-OAEP params: defaults SHA-1, MGF1SHA1, empty label | shall (defaults) | A.2.1 |
| R23 | RSASSA-PSS params: defaults SHA-1, MGF1SHA1, saltLength=20, trailerField=1 | shall (defaults) | A.2.3 |
| R24 | MGF1: output length ≤ 2^32 * hLen; uses counter in I2OSP | shall | B.2.1 |

## Informative Annexes (Condensed)
- **A. ASN.1 Syntax**: Defines RSAPublicKey, RSAPrivateKey (including multi-prime), and OIDs for scheme identification (RSAES-OAEP, RSASSA-PSS, PKCS1-v1_5). Parameter structures specify hash, MGF, and label/salt.
- **B. Supporting Techniques**: Lists hash functions (MD2, MD5, SHA-1, SHA-256, SHA-384, SHA-512) and MGF1. Recommends SHA-1 or SHA-2 for new apps; MD2/MD5 for legacy only.
- **C. ASN.1 Module**: Complete ASN.1 definition in PKCS-1 module.
- **D. Intellectual Property**: RSA patent expired; multi-prime patent (5,848,159); UC patent pending on PSS (freely licensed for IEEE).
- **E. Revision History**: Versions 1.0-1.5, 2.0, 2.1; key changes include addition of OAEP, PSS, multi-prime.
- **F. References**: 50 cited works.
- **G. About PKCS**: Overview of PKCS series and contact info.
- **H. Corrections During RFC Publication**: Three technical corrections listed (e.g., AlgorithmIdentifier parameters for SHA).