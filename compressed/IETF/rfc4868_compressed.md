# RFC 4868: Using HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 with IPsec
**Source**: IETF | **Version**: Standards Track | **Date**: May 2007 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc4868/

## Scope (Summary)
This specification defines the use of HMAC with SHA-256/384/512 for data origin authentication, integrity verification, and as Pseudo-Random Functions (PRFs) in IPsec (AH, ESP, IKE, IKEv2). Truncated authentication variants (HMAC-SHA-256-128, -384-192, -512-256) and untruncated PRF variants (PRF-HMAC-SHA-256/384/512) are specified.

## Normative References
- [AH] Kent, S., "IP Authentication Header", RFC 4302, December 2005.
- [ARCH] Kent, S. and K. Seo, "Security Architecture for the Internet Protocol", RFC 4301, December 2005.
- [ESP] Kent, S., "IP Encapsulating Security Payload (ESP)", RFC 4303, December 2005.
- [HMAC] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [HMAC-SHA1] Madsen, C. and R. Glenn, "The Use of HMAC-SHA-1-96 within ESP and AH", RFC 2404, November 1998.
- [HMAC-TEST] Nystrom, M., "Identifiers and Test Vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512", RFC 4231, December 2005.
- [IKE] Harkins, D. and D. Carrel, "The Internet Key Exchange (IKE)", RFC 2409, November 1998.
- [IKEv2] Kaufman, C., "Internet Key Exchange (IKEv2) Protocol", RFC 4306, December 2005.
- [SHA2-1] NIST, "FIPS PUB 180-2 'Specifications for the Secure Hash Standard'", 2004 FEB.
- [SHA256+] Eastlake, D. and T. Hansen, "US Secure Hash Algorithms (SHA and HMAC-SHA)", RFC 4634, July 2006.

## Definitions and Abbreviations
- **Block size**: Size of data block the underlying hash algorithm operates upon: for SHA-256, 512 bits; for SHA-384 and SHA-512, 1024 bits.
- **Output length**: Size of hash value produced by the underlying hash algorithm: SHA-256=256 bits, SHA-384=384 bits, SHA-512=512 bits.
- **Authenticator length**: Size of the authenticator in bits after truncation (half the output length for authentication variants).
- **HMAC-SHA-256+ algorithms**: Collective term for HMAC-SHA-256-128, HMAC-SHA-384-192, HMAC-SHA-512-256, PRF-HMAC-SHA-256, PRF-HMAC-SHA-384, PRF-HMAC-SHA-512.

## 1. Introduction
Specifies use of SHA-256/384/512 with HMAC for IPsec data origin authentication and integrity verification (truncated to half the output length) and as PRFs (untruncated) for IKE and IKEv2. Security is based on unpredictable secret keys known only to sender and recipient.

## 2. The HMAC-SHA-256+ Algorithms
Describes characteristics for IPsec usage based on [SHA2-1], [HMAC], and [SHA256+].

### 2.1. Keying Material
Requirements differ for authentication vs PRF usage.

#### 2.1.1. Data Origin Authentication and Integrity Verification Usage
- **R1**: When used as an integrity/authentication algorithm, a fixed key length equal to the output length of the hash function (SHA-256: 256 bits, SHA-384: 384 bits, SHA-512: 512 bits) **MUST** be supported.
- **R2**: Key lengths other than the output length of the associated hash function **MUST NOT** be supported (to ensure interoperability and security per [HMAC] recommendations).

#### 2.1.2. Pseudo-Random Function (PRF) Usage
When used as a PRF with IKE or IKEv2, the key length is variable. Handling rules (from [HMAC]):
- If key length equals block size, use as-is.
- If key is shorter than block size, pad on the right with zero bits to block size. [HMAC] strongly discourages key length less than output length.
- If key is longer than block size, compute hash over the key and treat resulting output as HMAC key (will be less than block size, then zero-padded).

#### 2.1.3. Randomness and Key Strength
- **R3**: A strong pseudo-random function **MUST** be used to generate the key for HMAC-SHA-256+. (No published weak keys at time of writing.)

#### 2.1.4. Key Distribution
Key distribution mechanism **must** ensure unique keys allocated and distributed only to participating parties (per [ARCH]).

#### 2.1.5. Refreshing Keys
Periodic key refreshment is a fundamental security practice (per [HMAC]). Specific lifetimes depend on threat model and key strength.

### 2.2. Padding
No additional padding beyond that specified in [SHA2-1] is required. No implicit packet padding as defined in [AH] is required.

### 2.3. Truncation
- **R4**: When used as a data origin authentication and integrity verification algorithm in ESP, AH, IKE, or IKEv2, a truncated value using the first nnn/2 bits (half the algorithm output size) **MUST** be supported.
- **R5**: No other authenticator value lengths are supported by this specification.
Upon sending, truncated value stored in authenticator field. Upon receipt, full nnn-bit value computed and first nnn/2 bits compared. Truncation length corresponds to birthday attack bound; minimizes additional wire bits.

### 2.4. Using HMAC-SHA-256+ as PRFs in IKE and IKEv2
PRF-HMAC-SHA-256/384/512 are identical to their authentication counterparts except variable-length keys are permitted and truncation is NOT performed.

### 2.5. Interactions with ESP, IKE, or IKEv2 Cipher Mechanisms
No known issues preclude use with any specific cipher algorithm.

### 2.6. HMAC-SHA-256+ Parameter Summary
Table summarizing block size, output length, truncation length, key length, and algorithm type for each variant:

| Algorithm ID | Block Size (bits) | Output Length (bits) | Truncation Length (bits) | Key Length (bits) | Algorithm Type |
|---|---|---|---|---|---|
| HMAC-SHA-256-128 | 512 | 256 | 128 | 256 | auth/integ |
| HMAC-SHA-384-192 | 1024 | 384 | 192 | 384 | auth/integ |
| HMAC-SHA-512-256 | 1024 | 512 | 256 | 512 | auth/integ |
| PRF-HMAC-SHA-256 | 512 | 256 | (none) | variable | PRF |
| PRF-HMAC-SHA-384 | 1024 | 384 | (none) | variable | PRF |
| PRF-HMAC-SHA-512 | 1024 | 512 | (none) | variable | PRF |

### 2.7. Test Vectors (Informative)
- **PRF Test Vectors**: Six test cases (PRF-1 through PRF-6) for each PRF variant, borrowed from RFC 4231. Keys and data as ASCII strings or hex; computed HMAC values provided.
- **Authenticator Test Vectors**: Four test cases each for HMAC-SHA-256-128 (AUTH256-1 to 4), HMAC-SHA-384-192 (AUTH384-1 to 4), and HMAC-SHA-512-256 (AUTH512-1 to 4). Both full PRF output and truncated authenticator values given.

## 3. Security Considerations
Security of HMAC-SHA-256+ algorithms based on underlying hash strength and HMAC construct. No practical attacks known. Correctness of implementation, key management, and secret key strength are critical.

### 3.1. HMAC Key Length vs Truncation Length
- Probability of guessing correct MAC value (adversary with no key knowledge) depends on truncated output length (1 in 2^128 for 128-bit truncation). HMAC-SHA-256-128 and HMAC-SHA1-96 provide similar security under this attack.
- Against passive key guessing attacks, longer key lengths (256, 384, 512 bits) provide proportionally greater security than HMAC-SHA1-96 (160-bit key).

## 4. IANA Considerations
IANA has assigned the following identifiers:

**IKE Phase 1 hash algorithm attributes:**
- SHA2-256: 4
- SHA2-384: 5
- SHA2-512: 6

**IKE Phase 2 authentication algorithm identifiers:**
- HMAC-SHA2-256: 5
- HMAC-SHA2-384: 6
- HMAC-SHA2-512: 7

**IKEv2 PRF transform identifiers (type 2):**
- PRF_HMAC_SHA2_256: 5
- PRF_HMAC_SHA2_384: 6
- PRF_HMAC_SHA2_512: 7

**IKEv2 integrity transform identifiers (type 3):**
- AUTH_HMAC_SHA2_256_128: 12
- AUTH_HMAC_SHA2_384_192: 13
- AUTH_HMAC_SHA2_512_256: 14

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Fixed key length equal to hash output length MUST be supported for authentication/integrity algorithms. | shall | Section 2.1.1 |
| R2 | Key lengths other than output length MUST NOT be supported for authentication/integrity. | shall | Section 2.1.1 |
| R3 | Strong pseudo-random function MUST be used to generate HMAC-SHA-256+ keys. | shall | Section 2.1.3 |
| R4 | Truncated value using first nnn/2 bits MUST be supported for authentication/integrity. | shall | Section 2.3 |
| R5 | No other authenticator value lengths are supported. | shall | Section 2.3 |

## Informative Annexes (Condensed)
- **Test Vectors (Section 2.7)**: Provides PRF and authenticator test vectors for each algorithm to assist implementation verification. Keys, data, and expected outputs (hex and ASCII) are given. Reference implementations in [SHA256+].
- **Acknowledgements**: Borrowed text from [HMAC-SHA1] and [HMAC-TEST]; thanks to Hugo Krawczyk, Russ Housley, Steve Bellovin.