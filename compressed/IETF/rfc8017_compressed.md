# RFC 8017: PKCS #1: RSA Cryptography Specifications Version 2.2
**Source**: IETF | **Version**: 2.2 | **Date**: November 2016 | **Type**: Informational
**Original**: http://www.rfc-editor.org/info/rfc8017

## Scope (Summary)
Provides recommendations for RSA-based public-key cryptography, covering cryptographic primitives, encryption and signature schemes with appendix, and ASN.1 syntax for keys and scheme identification. Supersedes PKCS #1 v2.1 (RFC 3447).

## Normative References
- [GARNER] Garner, H., "The Residue Number System", IRE Trans. Electronic Computers, EC-8(2), 140-147, 1959.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, 1997.
- [RSA] Rivest, R., Shamir, A., and L. Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems", CACM, 21(2), 120-126, 1978.

## Definitions and Abbreviations
- **c**: ciphertext representative (integer 0..n-1)
- **C**: ciphertext (octet string)
- **d**: RSA private exponent
- **dP/dQ**: CRT exponents for p and q
- **e**: RSA public exponent
- **EM**: encoded message (octet string)
- **emBits/emLen**: intended length in bits/octets of EM
- **Hash**: hash function; **hLen**: output length of Hash
- **k**: octet length of RSA modulus n
- **K**: RSA private key
- **L**: optional label (octet string) in RSAES-OAEP
- **m**: message representative (integer 0..n-1)
- **M**: message (octet string)
- **MGF**: mask generation function; **mgfSeed**: seed for MGF
- **n**: RSA modulus, product of u≥2 distinct odd primes
- **(n, e)**: RSA public key
- **p, q**: first two prime factors of n
- **qInv**: CRT coefficient (q * qInv ≡ 1 mod p)
- **r_i**: prime factors of n (r_1=p, r_2=q)
- **s**: signature representative (integer)
- **S**: signature (octet string)
- **sLen**: length of salt in EMSA-PSS
- **u**: number of prime factors (u≥2)
- **λ(n)**: LCM(r₁-1, ..., r_u-1)
- **∥**: concatenation
- **⊕**: bit-wise XOR
- **≡**: congruence

## Cryptographic Primitives (Section 5)

### 5.1 Encryption and Decryption Primitives
### 5.1.1 RSAEP
**RSAEP((n, e), m)** → c
- **Shall**: If m not between 0 and n-1, output "message representative out of range".
- **Shall**: c = m^e mod n.

### 5.1.2 RSADP
**RSADP(K, c)** → m
- **Shall**: If c not between 0 and n-1, output "ciphertext representative out of range".
- **Shall**: Compute m via CRT or direct exponentiation as specified.

### 5.2 Signature and Verification Primitives
### 5.2.1 RSASP1
**RSASP1(K, m)** → s
- **Shall**: If m not between 0 and n-1, output "message representative out of range".
- **Shall**: Compute s = m^d mod n (or CRT).

### 5.2.2 RSAVP1
**RSAVP1((n, e), s)** → m
- **Shall**: If s not between 0 and n-1, output "signature representative out of range".
- **Shall**: m = s^e mod n.

## Encryption Schemes (Section 7)

### 7.1 RSAES-OAEP
**RSAES-OAEP-ENCRYPT((n, e), M, L)** → C
- **Shall**: If length(L) > hash input limitation, output "label too long".
- **Shall**: If mLen > k - 2hLen - 2, output "message too long".
- **Shall**: Apply EME-OAEP encoding (Steps 2a-2i) then RSAEP.
- **Shall**: Output ciphertext C of length k octets.

**RSAES-OAEP-DECRYPT(K, C, L)** → M
- **Shall**: If length(L) > limitation or C length ≠ k or k < 2hLen+2, output "decryption error".
- **Shall**: Apply RSADP, then EME-OAEP decoding.
- **Shall**: If decoding fails (e.g., Y≠0, lHash mismatch), output "decryption error". **Note**: Error conditions must not be distinguishable.

### 7.2 RSAES-PKCS1-v1_5
**RSAES-PKCS1-V1_5-ENCRYPT((n, e), M)** → C
- **Shall**: If mLen > k - 11, output "message too long".
- **Shall**: Generate PS of k - mLen - 3 nonzero pseudorandom octets.
- **Shall**: EM = 0x00 || 0x02 || PS || 0x00 || M, then RSAEP.

**RSAES-PKCS1-V1_5-DECRYPT(K, C)** → M
- **Shall**: If C length ≠ k or k < 11, output "decryption error".
- **Shall**: Apply RSADP, then decode EM. If first octet ≠ 0x00, second ≠ 0x02, no 0x00 separator, or PS length < 8, output "decryption error".
- **Note**: Error conditions must not be distinguishable.

## Signature Schemes with Appendix (Section 8)

### 8.1 RSASSA-PSS
**RSASSA-PSS-SIGN(K, M)** → S
- **Shall**: Apply EMSA-PSS-ENCODE(M, modBits-1); if "message too long" or "encoding error", propagate.
- **Shall**: Convert EM to integer m, then RSASP1; output S = I2OSP(s, k).

**RSASSA-PSS-VERIFY((n, e), M, S)** → "valid"/"invalid"
- **Shall**: If S length ≠ k, output "invalid".
- **Shall**: Apply RSAVP1, then EMSA-PSS-VERIFY.

### 8.2 RSASSA-PKCS1-v1_5
**RSASSA-PKCS1-V1_5-SIGN(K, M)** → S
- **Shall**: Apply EMSA-PKCS1-v1_5-ENCODE(M, k). If encoding error, propagate.
- **Shall**: Then RSASP1.

**RSASSA-PKCS1-V1_5-VERIFY((n, e), M, S)** → "valid"/"invalid"
- **Shall**: If S length ≠ k, output "invalid".
- **Shall**: Recover EM via RSAVP1; recompute EM' by encoding M; if EM == EM', output "valid", else "invalid".

## Encoding Methods (Section 9)

### 9.1 EMSA-PSS
**EMSA-PSS-ENCODE(M, emBits)** → EM
- **Shall**: If M length > hash input limit, "message too long".
- **Shall**: mHash = Hash(M). If emLen < hLen + sLen + 2, "encoding error".
- **Shall**: Generate random salt of length sLen.
- **Shall**: M' = 0x00…00 (8 octets) || mHash || salt; H = Hash(M').
- **Shall**: DB = PS (zero octets) || 0x01 || salt; dbMask = MGF(H, emLen-hLen-1); maskedDB = DB ⊕ dbMask.
- **Shall**: Set leftmost (8emLen - emBits) bits of maskedDB to zero.
- **Shall**: EM = maskedDB || H || 0xbc.

**EMSA-PSS-VERIFY(M, EM, emBits)** → "consistent"/"inconsistent"
- **Shall**: If M length > hash limit, "inconsistent".
- **Shall**: mHash = Hash(M); if emLen < hLen+sLen+2 or last octet ≠ 0xbc or leftmost bits not zero, "inconsistent".
- **Shall**: Recompute dbMask, DB; verify PS zero, 0x01, then recompute H' and compare.

### 9.2 EMSA-PKCS1-v1_5
**EMSA-PKCS1-V1_5-ENCODE(M, emLen)** → EM
- **Shall**: H = Hash(M). Encode DigestInfo (DER) as T.
- **Shall**: If emLen < tLen + 11, "intended encoded message length too short".
- **Shall**: PS = emLen - tLen - 3 octets of 0xFF.
- **Shall**: EM = 0x00 || 0x01 || PS || 0x00 || T.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | RSAEP: output c = m^e mod n, if m in [0, n-1] | shall | §5.1.1 |
| R2 | RSADP: output m via CRT or direct, if c in [0, n-1] | shall | §5.1.2 |
| R3 | RSASP1: output s = m^d mod n (or CRT) | shall | §5.2.1 |
| R4 | RSAVP1: output m = s^e mod n | shall | §5.2.2 |
| R5 | RSAES-OAEP encryption: apply EME-OAEP then RSAEP | shall | §7.1.1 |
| R6 | RSAES-OAEP decryption: error indistinguishability | shall | §7.1.2 |
| R7 | RSAES-PKCS1-v1_5 encryption: use nonzero PS of length ≥ 8 | shall | §7.2.1 |
| R8 | RSAES-PKCS1-v1_5 decryption: error indistinguishability | shall | §7.2.2 |
| R9 | RSASSA-PSS: use EMSA-PSS with modBits-1 | shall | §8.1.1 |
| R10 | RSASSA-PSS verification: compare after EMSA-PSS-VERIFY | shall | §8.1.2 |
| R11 | RSASSA-PKCS1-v1_5: encode with DigestInfo DER | shall | §8.2.1 |
| R12 | EMSA-PSS encoding: random salt, trailer 0xbc | shall | §9.1.1 |
| R13 | EMSA-PKCS1-v1_5 encoding: PS of 0xFF | shall | §9.2 |
| R14 | Hash function parameters: omitted or NULL; exceptions in DigestInfo | must | §B.1 |
| R15 | RSASSA-PSS recommended: MGF based on same hash | recommended | §8.1 |
| R16 | New applications: use RSAES-OAEP and RSASSA-PSS | required | §§7, 8 |

## Informative Annexes (Condensed)
- **Appendix A (ASN.1 Syntax)**: Defines RSAPublicKey, RSAPrivateKey (with multi-prime support), and OIDs for schemes (RSAES-OAEP, RSAES-PKCS1-v1_5, RSASSA-PSS, RSASSA-PKCS1-v1_5). Includes parameters for OAEP and PSS. Backward compatible.
- **Appendix B (Supporting Techniques)**: Lists nine hash functions (MD2, MD5, SHA-1, SHA-2 family). Recommends SHA-224/256/384/512/512-224/512-256 for new apps; MD2/MD5/SHA-1 only for legacy. Defines MGF1 mask generation function based on a hash.
- **Appendix C (ASN.1 Module)**: Complete ASN.1 module with all definitions and OIDs.
- **Appendix D (Revision History)**: Summarizes versions from 1.0 to 2.2; v2.2 added SHA-224, SHA-512/224, SHA-512/256.
- **Appendix E (About PKCS)**: Describes origin and role of PKCS standards.