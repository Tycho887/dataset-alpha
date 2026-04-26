# RFC 8018: PKCS #5: Password-Based Cryptography Specification Version 2.1
**Source**: IETF | **Version**: 2.1 | **Date**: January 2017 | **Type**: Informational  
**Original**: http://www.rfc-editor.org/info/rfc8018  
**Obsoletes**: RFC 2898

## Scope (Summary)
This document provides recommendations for the implementation of password-based cryptography, covering key derivation functions (PBKDF1, PBKDF2), encryption schemes (PBES1, PBES2), message authentication schemes (PBMAC1), and ASN.1 syntax identifying the techniques. It represents a republication of PKCS #5 v2.1 from RSA Laboratories’ Public-Key Cryptography Standards (PKCS) series; change control is transferred to the IETF.

## Normative References
- [NIST46] FIPS PUB 46-3, Data Encryption Standard, 1999
- [NIST81] FIPS PUB 81, DES Modes of Operation, 1980
- [NIST180] FIPS PUB 180-4, Secure Hash Standard (SHS), 2015
- [NIST197] FIPS PUB 197, Advance Encryption Standard (AES), 2001
- [NIST198] FIPS PUB 198-1, The Keyed-Hash Message Authentication Code (HMAC), 2008
- [NISTSP63] NIST SP 800-63-2, Electronic Authentication Guideline, 2013
- [NISTSP132] NIST SP 800-132, Recommendation for Password-Based Key Derivation, Part 1, 2010
- [ANSIX952] ANSI X9.52, Triple Data Encryption Algorithm Modes of Operation, 1998
- [RFC1319] MD2 Message-Digest Algorithm
- [RFC1321] MD5 Message-Digest Algorithm
- [RFC1423] PEM Algorithms, Modes, and Identifiers
- [RFC2104] HMAC: Keyed-Hashing for Message Authentication
- [RFC2268] Description of the RC2 Encryption Algorithm
- [RFC2898] PKCS #5 Version 2.0 (obsoleted)
- [RFC3629] UTF-8, STD 63
- [RFC5652] Cryptographic Message Syntax (CMS)
- [RFC5958] Asymmetric Key Packages
- [RFC6149] MD2 to Historic Status
- [RFC6151] Updated Security Considerations for MD5 and HMAC-MD5
- [RFC6194] Security Considerations for SHA-0 and SHA-1
- [ISO8824-1] ASN.1 – Specification of Basic Notation
- [ISO8824-2] ASN.1 – Information Object Specification
- [ISO8824-3] ASN.1 – Constraint Specification
- [ISO8824-4] ASN.1 – Parameterization of ASN.1 Specifications
- [PKCS5_15] PKCS #5 v1.5, 1993
- [PKCS5_21] PKCS #5 v2.1, 2012
- [RC5] The RC5 Encryption Algorithm (FSE 1994)
- [RFC2040] RC5, RC5-CBC, RC5-CBC-Pad, RC5-CTS Algorithms

## Definitions and Abbreviations
| Symbol | Meaning |
|--------|---------|
| C       | ciphertext, an octet string |
| c       | iteration count, a positive integer |
| DK      | derived key, an octet string |
| dkLen   | length in octets of derived key, positive integer |
| EM      | encoded message, an octet string |
| Hash    | underlying hash function |
| hLen    | length in octets of pseudorandom function output |
| l       | length in blocks of derived key |
| IV      | initialization vector, an octet string |
| K       | encryption key, an octet string |
| KDF     | key derivation function |
| M       | message, an octet string |
| P       | password, an octet string |
| PRF     | underlying pseudorandom function |
| PS      | padding string, an octet string |
| psLen   | length in octets of padding string |
| S       | salt, an octet string |
| T       | message authentication code, an octet string |
| \xor    | bit-wise exclusive-or |
| \|\|    | octet length operator or concatenation |
| <i..j>  | substring extraction operator |

## Overview (Section 3)
Password-based cryptography processes a password (octet string, arbitrary length; ASCII/UTF-8 recommended) with a salt and iteration count to produce a key. Salt prevents precomputation and collisions; iteration count increases cost of exhaustive search. Key derivation functions (PBKDF) are modular and can be used for encryption and message authentication. Different keys can be derived from a single password by varying the salt.

## Salt and Iteration Count (Section 4)
### 4.1 Salt
- **Salt benefits**: (1) Large set of keys per password prevents precomputation (2^64 keys for 64-bit salt). (2) Key collisions unlikely until ~2^32 keys.
- **Recommendation**: Salt shall be at least eight octets (64 bits) long. If different uses of the same key derived from the same password are a concern, the salt **should** contain data distinguishing between operations (e.g., purpose octet). If no RNG available, deterministic alternative `S = KDF(P, M)` but **not recommended** when M is from a small space.

### 4.2 Iteration Count
- **Effect**: Increases security strength by `log2(c)` bits.
- **Requirement**: The iteration count **shall** be selected as large as possible while remaining acceptable for users. A minimum iteration count of 1,000 is recommended. For critical keys or powerful systems, 10,000,000 may be appropriate (per [NISTSP132]).

## Key Derivation Functions (Section 5)
### 5.1 PBKDF1 (for compatibility, not recommended for new applications)
- **Hash**: **shall** be MD2, MD5, or SHA-1.
- **Output**: dkLen ≤ 16 octets for MD2/MD5, ≤ 20 for SHA-1.
- **Algorithm**:  
  `T_1 = Hash(P || S)`; `T_i = Hash(T_{i-1})` for i=2..c; `DK = T_c<0..dkLen-1>`

### 5.2 PBKDF2 (recommended for new applications)
- **PRF**: e.g., HMAC-SHA-1/2 (see Appendix B.1). hLen = output length.
- **Input**: P, S, c, dkLen. dkLen ≤ (2^32 - 1) × hLen.
- **Algorithm**:
  - Let `l = CEIL(dkLen / hLen)`, `r = dkLen - (l-1)*hLen`.
  - For each block i=1..l: `T_i = F(P, S, c, i)` where  
    `F(P, S, c, i) = U_1 xor U_2 xor ... xor U_c`  
    with `U_1 = PRF(P, S || INT(i))`, `U_j = PRF(P, U_{j-1})` for j=2..c.
  - `DK = T_1 || T_2 || ... || T_l<0..r-1>`.
- **Note**: Recursion prevents parallelism; XOR reduces degeneracy.

## Encryption Schemes (Section 6)
### 6.1 PBES1 (compatibility only)
- **Uses PBKDF1** with DES or RC2 in CBC mode.
- **Encryption**:
  1. Select 8-octet salt S and iteration count c.
  2. `DK = PBKDF1(P, S, c, 16)`.
  3. `K = DK<0..7>`, `IV = DK<8..15>`.
  4. Pad M to multiple of 8 using RFC 1423 padding: for `|M| mod 8 = r`, add (8-r) octets each of value (8-r).
  5. Encrypt EM with DES or RC2-CBC under K, IV.
- **Decryption**: Reverse steps; check padding integrity.

### 6.2 PBES2 (recommended)
- **Uses PBKDF2** with an underlying encryption scheme (e.g., AES-CBC-Pad, see Appendix B.2).
- **Encryption**:
  1. Select S, c, dkLen for underlying scheme.
  2. `DK = PBKDF2(P, S, c, dkLen)`.
  3. Encrypt M with underlying scheme under DK (details per scheme).
- **Decryption**: Obtain S, c, dkLen, derive DK, decrypt.

## Message Authentication Schemes (Section 7)
### 7.1 PBMAC1
- **Uses PBKDF2** with an underlying MAC scheme (e.g., HMAC-SHA-1/2, see Appendix B.3).
- **Generation**:
  1. Select S, c, dkLen.
  2. `DK = PBKDF2(P, S, c, dkLen)`.
  3. Compute MAC on M under DK → T.
- **Verification**: Compute MAC and compare; output "correct" or "incorrect".

## Security Considerations (Section 8)
- Offline password search is possible; use well-chosen passwords per [NISTSP63].
- Different uses for the same password **should** derive different keys (via salt or structured salt).
- For security considerations of MD2, MD5, SHA-1, see [RFC6149], [RFC6151], [RFC6194].

## Requirements Summary
| ID  | Requirement                                                                                     | Type     | Reference                   |
|-----|-------------------------------------------------------------------------------------------------|----------|-----------------------------|
| R1  | PBKDF1 hash function **shall** be MD2, MD5, or SHA-1.                                           | shall    | Section 5.1                 |
| R2  | PBKDF1 derived key length **shall not** exceed 16 octets for MD2/MD5 or 20 for SHA-1.           | shall    | Section 5.1                 |
| R3  | PBKDF2 output length **shall** be ≤ (2^32-1) × hLen.                                            | shall    | Section 5.2                 |
| R4  | PBKDF2 PRF **shall** be a pseudorandom function (e.g., HMAC-SHA-1/2).                           | shall    | Section 5.2, Appendix B.1   |
| R5  | PBES1 underlying block cipher **shall** be DES or RC2 in CBC mode.                              | shall    | Section 6.1                 |
| R6  | PBES2 key derivation function **shall** be PBKDF2.                                              | shall    | Section 6.2                 |
| R7  | PBMAC1 key derivation function **shall** be PBKDF2.                                             | shall    | Section 7.1                 |
| R8  | Salt **should** be at least eight octets (64 bits).                                             | should   | Section 4.1                 |
| R9  | Iteration count **shall** be as large as possible; minimum 1,000 recommended.                   | shall/should | Section 4.2, [NISTSP132] |
| R10 | PBES2-params **shall** include keyDerivationFunc and encryptionScheme AlgorithmIdentifiers.      | shall    | Appendix A.4                |
| R11 | PBMAC1-params **shall** include keyDerivationFunc and messageAuthScheme AlgorithmIdentifiers.    | shall    | Appendix A.5                |
| R12 | PBKDF2-params salt **shall** be either `specified OCTET STRING` or `otherSource AlgorithmIdentifier`. | shall | Appendix A.2             |
| R13 | PBKDF2-params default PRF **shall** be `algid-hmacWithSHA1` (HMAC-SHA-1).                      | shall    | Appendix A.2                |

## Informative Annexes (Condensed)
- **Appendix A – ASN.1 Syntax**: Defines OIDs and structures for all schemes.  
  - PBKDF2-params includes salt (specified or otherSource), iterationCount, optional keyLength, prf default HMAC-SHA1.  
  - PBES1 uses PBEParameter (salt 8 octets, iterationCount).  
  - PBES2-params contains keyDerivationFunc (id-PBKDF2) and encryptionScheme.  
  - PBMAC1-params similar with messageAuthScheme.
- **Appendix B – Supporting Techniques**:  
  - **PRFs**: HMAC-SHA-1, HMAC-SHA-2 (SHA-224/256/384/512/512-224/512-256).  
  - **Encryption schemes**: DES-CBC-Pad, DES-EDE3-CBC-Pad, RC2-CBC-Pad, RC5-CBC-Pad, AES-CBC-Pad (128,192,256).  
  - **MAC schemes**: HMAC-SHA-1, HMAC-SHA-2. All with OIDs.  
  - Note: DES, DES-EDE3, RC2 are legacy; AES-CBC-Pad is the recommended example for PBES2.
- **Appendix C – ASN.1 Module**: Complete ASN.1 module `PKCS5v2-1` defining `AlgorithmIdentifier`, `PBKDF2-params`, `PBES2-params`, `PBMAC1-params`, and all OID assignments.
- **Appendix D – Revision History**: V1.0‑1.4 (initial), V1.5 (editorial), V2.0 (major: PBES2, PBMAC1, independent KDFs), V2.1 (AES/CBC, HMAC‑SHA‑2, updated references, security considerations for MD2/MD5/SHA‑1).
- **Appendix E – About PKCS**: PKCS series published by RSA Laboratories since 1991; further development via IETF.