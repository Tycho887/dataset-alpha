# RFC 7518: JSON Web Algorithms (JWA)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc7518

## Scope (Summary)
This specification registers cryptographic algorithms and identifiers for use with JSON Web Signature (JWS), JSON Web Encryption (JWE), and JSON Web Key (JWK). It defines several IANA registries for these identifiers and describes semantics and operations specific to these algorithms and key types.

## Normative References
- [JWS] RFC 7515
- [JWE] RFC 7516
- [JWK] RFC 7517
- [RFC2119] Key words for requirement levels
- [RFC2104] HMAC
- [RFC3447] PKCS #1 (RSA)
- [RFC3394] AES Key Wrap
- [RFC2898] PBKDF2
- [RFC4868] HMAC-SHA-256/384/512 with IPsec
- [SHS] FIPS PUB 180-4
- [DSS] FIPS PUB 186-4
- [AES] FIPS PUB 197
- [NIST.800-38A] AES CBC
- [NIST.800-38D] AES GCM
- [NIST.800-56A] Concat KDF
- [SEC1] Elliptic Curve Cryptography
- [RFC3629] UTF-8
- [RFC20] ASCII
- [RFC4949] Internet Security Glossary

## Definitions and Abbreviations
- **Base64url Encoding**: per Section 2 of [JWS]
- **Base64urlUInt**: representation of a positive integer as base64url encoding of minimal unsigned big-endian octet sequence (zero represented as BASE64URL(single zero-valued octet), "AA")
- **Content Encryption Key (CEK)**: key used to encrypt plaintext (JWE)
- **Direct Encryption**: symmetric key used directly as CEK
- **Direct Key Agreement**: key agreement result used directly as CEK
- **JWE Authentication Tag**: output of authenticated encryption
- **JWE Ciphertext**: encrypted content
- **JWE Encrypted Key**: encrypted CEK
- **JWE Initialization Vector (IV)**: per algorithm
- **JWE Protected Header**: JOSE Header that is MACed or signed
- **JWK**: JSON Web Key
- **JWS**: JSON Web Signature
- **Key Agreement with Key Wrapping**: key agreement result used to wrap CEK
- **Key Encryption**: asymmetric encryption of CEK
- **Key Wrapping**: symmetric encryption of CEK
- **MAC**: Message Authentication Code
- **Unsecured JWS**: JWS with "alg":"none"

## 1. Introduction
- Goal: register algorithms and identifiers in IANA registries so that JWS, JWE, JWK remain unchanged as algorithm sets evolve.
- Names are short for compact representations.

### 1.1. Notational Conventions
- The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in [RFC2119].
- BASE64URL(OCTETS) denotes base64url encoding per [JWS].
- UTF8(STRING) denotes UTF-8 octets.
- ASCII(STRING) denotes ASCII octets.
- A || B denotes concatenation.

## 2. Terminology
- (Definitions extracted from [JWS], [JWE], [JWK], [RFC4949] – see Definitions above.)

## 3. Cryptographic Algorithms for Digital Signatures and MACs
JWS uses algorithms to sign or MAC the JWS Protected Header and JWS Payload.

### 3.1. "alg" Header Parameter Values for JWS
Table of values with Implementation Requirements (Required, Recommended, Optional). Key entries:
- HS256: Required
- RS256: Recommended
- ES256: Recommended+
- none: Optional
- Others: Optional

See Appendix A.1 for cross-reference.

### 3.2. HMAC with SHA-2 Functions (HS256, HS384, HS512)
- **Requirement**: A key of the same size as hash output (or larger) **MUST** be used.
- HMAC SHA-256 computed per [RFC2104] using JWS Signing Input as text.
- HMAC output is JWS Signature.
- **Validation**: Computed HMAC compared to base64url-decoded signature in constant-time manner.
- SHA-384 and SHA-512 performed identically with corresponding key sizes and result lengths.

### 3.3. Digital Signature with RSASSA-PKCS1-v1_5 (RS256, RS384, RS512)
- **Requirement**: Key size of 2048 bits or larger **MUST** be used.
- Signature generated using RSASSA-PKCS1-v1_5-SIGN with SHA-256 (etc.) per [RFC3447].
- Validation: RSASSA-PKCS1-v1_5-VERIFY.

### 3.4. Digital Signature with ECDSA (ES256, ES384, ES512)
- Uses curves P-256, P-384, P-521 with corresponding SHA hashes.
- **Signature generation**: Output (R,S) as unsigned integers; each converted to big-endian octet sequence of fixed length (32, 48, or 66 octets) and concatenated.
- **Validation**: Signature length must be exactly 64, 96, or 132 octets; split into R and S; verify.

### 3.5. Digital Signature with RSASSA-PSS (PS256, PS384, PS512)
- Uses same hash for RSASSA-PSS and MGF1. Salt size = hash output size.
- **Key size requirement**: 2048 bits or larger **MUST** be used.
- Generated using RSASSA-PSS-SIGN; verified using RSASSA-PSS-VERIFY.

### 3.6. Using the Algorithm "none"
- **Requirement**: Unsecured JWS uses empty octet sequence as JWS Signature.
- **Recipients MUST** verify that JWS Signature is empty octet sequence.
- **Implementations** supporting Unsecured JWS **MUST NOT** accept such objects by default; application must explicitly signal per-object acceptance.
- **Applications MUST NOT** signal acceptance at global level to mitigate downgrade attacks.

## 4. Cryptographic Algorithms for Key Management
JWE uses algorithms to encrypt or determine the CEK.

### 4.1. "alg" Header Parameter Values for JWE
Table with Implementation Requirements. Includes:
- RSA1_5: Recommended- (key size >=2048 bits)
- RSA-OAEP: Recommended+ (key size >=2048 bits)
- RSA-OAEP-256: Optional
- A128KW, A256KW: Recommended
- A192KW: Optional
- dir: Recommended
- ECDH-ES: Recommended+
- ECDH-ES+A128KW, ECDH-ES+A256KW: Recommended
- A128GCMKW, A192GCMKW, A256GCMKW: Optional
- PBES2-HS256+A128KW, etc.: Optional

### 4.2. Key Encryption with RSAES-PKCS1-v1_5 (RSA1_5)
- **Requirement**: Key size 2048 bits or larger **MUST** be used.

### 4.3. Key Encryption with RSAES OAEP (RSA-OAEP, RSA-OAEP-256)
- Two variants: default parameters (SHA-1, MGF1 with SHA-1) and with SHA-256/MGF1 with SHA-256.
- **Requirement**: Key size 2048 bits or larger **MUST** be used.

### 4.4. Key Wrapping with AES Key Wrap (A128KW, A192KW, A256KW)
- Uses default initial value per [RFC3394].

### 4.5. Direct Encryption with a Shared Symmetric Key (dir)
- Shared symmetric key used directly as CEK. JWE Encrypted Key is empty octet sequence.

### 4.6. Key Agreement with ECDH-ES
Two modes: Direct Key Agreement (ECDH-ES) and Key Agreement with Key Wrapping (ECDH-ES+A128KW, etc.)
- **Requirement**: A new ephemeral public key **MUST** be generated for each key agreement operation.
- Concat KDF per [NIST.800-56A] with SHA-256 as digest.
- Parameters: Z, keydatalen, AlgorithmID (ASCII of "enc" or "alg"), PartyUInfo (if "apu" present, base64url decoded), PartyVInfo (if "apv" present), SuppPubInfo (keydatalen as 32-bit big-endian), SuppPrivInfo (empty).
- Header Parameters: "epk", "apu", "apv" (optional but must be understood if used).

#### 4.6.1. Header Parameters
- **"epk"**: Ephemeral public key as JWK public key. **MUST** be present and understood.
- **"apu"**: PartyUInfo, optional, base64url-encoded. **MUST** be understood if present.
- **"apv"**: PartyVInfo, optional, base64url-encoded. **MUST** be understood if present.

### 4.7. Key Encryption with AES GCM (A128GCMKW, A192GCMKW, A256GCMKW)
- **Requirement**: IV size 96 bits **REQUIRED**.
- Additional Authenticated Data = empty octet string.
- Authentication Tag size = 128 bits.
- Header Parameters: "iv" (96-bit base64url), "tag" (128-bit base64url). Both **MUST** be present and understood.

### 4.8. Key Encryption with PBES2 (PBES2-HS256+A128KW, etc.)
- Uses PBKDF2 per [RFC2898] with HMAC SHA-2 as PRF and AES Key Wrap for encryption.
- Password: if text, UTF-8 encoding **MUST** be used.
- Salt: "p2s" (base64url) concatenated with 0x00 and UTF8(alg). Salt input **MUST** be 8 or more octets, generated randomly per operation.
- Header Parameters: "p2s" (salt input), "p2c" (iteration count as positive integer). Both **MUST** be present and understood.
- **Recommended**: minimum iteration count of 1000.

## 5. Cryptographic Algorithms for Content Encryption

### 5.1. "enc" Header Parameter Values for JWE
Table:
- A128CBC-HS256: Required
- A192CBC-HS384: Optional
- A256CBC-HS512: Required
- A128GCM: Recommended
- A192GCM: Optional
- A256GCM: Recommended

### 5.2. AES_CBC_HMAC_SHA2 Algorithms
Composite authenticated encryption: AES-CBC with PKCS#7 padding + HMAC.

#### 5.2.1. Conventions
- CBC-PKCS7-ENC(X,P) denotes AES-CBC encryption with PKCS#7 padding using key X.
- MAC(Y,M) denotes HMAC application.

#### 5.2.2. Generic Algorithm
- **Encryption**:
  1. Derive MAC_KEY and ENC_KEY from K (MAC_KEY = initial MAC_KEY_LEN octets, ENC_KEY = final ENC_KEY_LEN octets).
  2. IV is 128-bit random/pseudorandom.
  3. Ciphertext E = CBC-PKCS7-ENC(ENC_KEY, P).
  4. AL = 64-bit big-endian number of bits in A.
  5. MAC over A || IV || E || AL using MAC_KEY; output M; first T_LEN octets = T.
  6. Output E and T.
- **Decryption**:
  1. Derive MAC_KEY and ENC_KEY as above.
  2. Compute HMAC on A || IV || E || AL; compare with T. If not identical, discard and return FAIL.
  3. Decrypt E using ENC_KEY and IV; remove PKCS#7 padding; return plaintext.

#### 5.2.3. AES_128_CBC_HMAC_SHA_256
- K = 32 octets, ENC_KEY_LEN = 16, MAC_KEY_LEN = 16, SHA-256, T_LEN = 16.

#### 5.2.4. AES_192_CBC_HMAC_SHA_384
- K = 48 octets, ENC_KEY_LEN = 24, MAC_KEY_LEN = 24, SHA-384, T_LEN = 24.

#### 5.2.5. AES_256_CBC_HMAC_SHA_512
- K = 64 octets, ENC_KEY_LEN = 32, MAC_KEY_LEN = 32, SHA-512, T_LEN = 32.

### 5.3. Content Encryption with AES GCM
- **Requirement**: IV size 96 bits **REQUIRED**.
- **Requirement**: Authentication Tag size 128 bits **MUST** be used regardless of key size.

## 6. Cryptographic Algorithms for Keys

### 6.1. "kty" Parameter Values
- EC: Recommended+
- RSA: Required
- oct: Required

### 6.2. Parameters for Elliptic Curve Keys
- Public key: "crv", "x", "y" **MUST** be present.
- Private key: additionally "d" **MUST** be present.
- Curves: P-256, P-384, P-521 only (no point compression).
- Values represented as base64url of big-endian octet strings of full coordinate size.

### 6.3. Parameters for RSA Keys
- Public key: "n", "e" **MUST** be present.
- Private key: "d" **REQUIRED**. Other parameters ("p","q","dp","dq","qi","oth") **SHOULD** be included; if any except "oth" present, all must be present except "oth" (only when more than two primes).
- "oth": array of objects with "r","d","t". If consumer does not support multi-prime keys and sees "oth", **MUST NOT** use the key.

### 6.4. Parameters for Symmetric Keys
- "k":"Key Value" as base64url of octet sequence.
- **SHOULD** include "alg" unless determined otherwise.

## 7. IANA Considerations
- Registries: JSON Web Signature and Encryption Algorithms, Header Parameter Names, JWE Compression Algorithms, JWK Types, JWK Parameters, JWK Elliptic Curve.
- Registration procedure: Specification Required after three-week review on jose-reg-review@ietf.org, with Designated Experts.
- Templates and initial contents provided in full.

## 8. Security Considerations (Condensed)
- Cryptographic agility required; algorithms weaken over time.
- Key lifetimes must follow NIST SP 800-57.
- RSAES-PKCS1-v1_5: included for interoperability; keys with low public exponent must not be used.
- AES GCM: same key must not be used more than 2^32 times; IV must never repeat.
- Unsecured JWS: must only be accepted per-object; global acceptance prohibited.
- Denial-of-Service: enforce key size limits.
- Key material reuse not recommended.
- Passwords: use high entropy; PBKDF2 iteration count should be at least 1000; password length recommendations given.
- Key entropy and random values per [JWS].
- Differences between digital signatures and MACs per [JWS].
- Matching algorithm strengths per [JWE].
- Adaptive chosen-ciphertext attacks per [JWE].
- Timing attacks per [JWS] and [JWE].
- RSA private key representations and blinding per [JWK].

## 9. Internationalization Considerations
- **Recommendation**: Applications should perform steps in [PRECIS] to prepare user-supplied passwords before PBKDF2.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Key of same size as hash output or larger MUST be used with HMAC SHA-2 | Shall | Section 3.2 |
| R2 | Key size of 2048 bits or larger MUST be used with RSASSA-PKCS1-v1_5, RSAES-OAEP, RSAES-PKCS1-v1_5, RSASSA-PSS | Shall | Sections 3.3, 3.5, 4.2, 4.3 |
| R3 | JWS with "none" MUST use empty octet as signature; recipients MUST verify | Shall | Section 3.6 |
| R4 | Unsecured JWS MUST NOT be accepted by default; MUST be per-object | Shall | Section 3.6 |
| R5 | New ephemeral public key MUST be generated for each ECDH-ES operation | Shall | Section 4.6 |
| R6 | AES GCM IV size MUST be 96 bits; Authentication Tag size MUST be 128 bits | Shall | Sections 4.7, 5.3 |
| R7 | AES GCM key must not be used more than 2^32 times; IV must not repeat | Shall | Section 8.4 |
| R8 | PBES2 salt input MUST be 8 or more octets, generated randomly per operation | Shall | Section 4.8.1.1 |
| R9 | RSA private key "d" is REQUIRED; other private parameters SHOULD be present; if any present, all must be present (except "oth") | Must / Should | Section 6.3.2 |
| R10 | Elliptic Curve public keys MUST include "crv","x","y"; private keys MUST include "d" | Shall | Section 6.2 |
| R11 | HMAC comparison MUST be done in constant-time manner | Shall | Section 3.2 |

## Informative Annexes (Condensed)
- **Appendix A: Algorithm Identifier Cross-Reference**: Maps JWA algorithm identifiers to XML DSIG, XML Encryption, Java JCA, and OID equivalents. Useful for interoperability.
- **Appendix B: Test Cases for AES_CBC_HMAC_SHA2 Algorithms**: Provides hexadecimal test vectors (K, MAC_KEY, ENC_KEY, P, IV, A, AL, E, M, T) for AES_128_CBC_HMAC_SHA_256, AES_192_CBC_HMAC_SHA_384, and AES_256_CBC_HMAC_SHA_512.
- **Appendix C: Example ECDH-ES Key Agreement Computation**: Illustrates ECDH-ES with Concat KDF to derive a 128-bit AES GCM key using Alice's ephemeral key and Bob's static key; includes full example of algorithms ("ECDH-ES", "A128GCM") and resulting derived key.