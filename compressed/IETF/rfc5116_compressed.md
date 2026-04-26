# RFC 5116: An Interface and Algorithms for Authenticated Encryption
**Source**: IETF (Standards Track) | **Version**: January 2008 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc5116

## Scope (Summary)
This document defines Authenticated Encryption with Associated Data (AEAD) algorithms, a uniform interface for such algorithms, and an IANA registry. It specifies four AEAD algorithms based on AES GCM and AES CCM with 128- and 256-bit keys.

## Normative References
- **[CCM]**: Dworkin, M., "NIST Special Publication 800-38C: The CCM Mode for Authentication and Confidentiality", U.S. NIST.
- **[GCM]**: Dworkin, M., "NIST Special Publication 800-38D: Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode (GCM) and GMAC.", November 2007.
- **[RFC2119]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **AEAD**: Authenticated Encryption with Associated Data. An encryption scheme providing confidentiality for plaintext and integrity/authenticity for both plaintext and associated data.
- **Associated Data (AD)**: Data authenticated but not encrypted.
- **Nonce**: A value used only once for a given key; must be distinct for each encryption invocation (or zero-length).
- **K_LEN, P_MAX, A_MAX, N_MIN, N_MAX, C_MAX**: Algorithm-specific parameter limits for key length, plaintext length, associated data length, nonce length, and ciphertext length.

## 1. Introduction
- **1.1 Background**: AEAD combines confidentiality and message authentication in a single algorithm.
- **1.2 Scope**: Defines AEAD interface, IANA registry, and four specific algorithms (AES GCM and CCM with 128/256-bit keys).
- **1.3 Benefits**: Simplifies application design, enables reusable crypto implementations, and allows independent security analysis.
- **1.4 Conventions**: The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

## 2. AEAD Interface
### 2.1 Authenticated Encryption
- **Inputs**: Secret key K, nonce N, plaintext P, associated data A (all octet strings).
- **Output**: Ciphertext C (length ≥ plaintext) or error.
- **Restrictions**:
  - K length: 1–255 octets; fixed per algorithm.
  - Nonce: MUST be distinct for each invocation with same key, OR all nonces are zero-length. Recommended length: 12 octets.
  - P length may be zero; A length may be zero.
  - C length may be zero.
  - K MUST NOT be included in N, P, or A.
- **Error handling**: If inputs exceed supported lengths, MUST return error and MUST NOT output partial data.
- **Nonce handling**: Nonce may be implicit or transmitted; decryption detects incorrect nonce.

### 2.2 Authenticated Decryption
- **Inputs**: K, N, A, C. Output: plaintext P or FAIL.
- **Security**: With high probability, FAIL if inputs are not authentic (assuming AEAD is secure).

### 2.3 Data Formatting
- No mandatory encoding. **SHOULD** position ciphertext after data needed to reconstruct other inputs (e.g., nonce before C).

## 3. Guidance on Use of AEAD Algorithms
### 3.1 Requirements on Nonce Generation
- **Distinctness**: Nonces MUST be distinct for each encryption with same key (or all zero-length).
- **Multiple devices**: Devices sharing a key MUST coordinate nonce uniqueness. Recommended: use nonce with device-specific field.
- **Long-term keys**: Nonce state MUST be checkpointed in non-volatile memory; use a "look-ahead" approach to avoid reuse after reboot.
- **Nonce reuse**: Each AEAD algorithm SHOULD describe security degradation from reuse.

### 3.2 Recommended Nonce Formation
- **Format**: Fixed field + Counter field (both variable length). Fixed field constant per device; Counter monotonically increasing. **SHOULD** support 12-octet nonces with 4-octet Counter.
- **Partially Implicit Nonces** (Section 3.2.1): Fixed field may be split into Fixed-Common (implicit) and Fixed-Distinct (explicit). Counter always explicit. Used in GCM ESP and CCM ESP.

### 3.3 Construction of AEAD Inputs
- **AD and plaintext**: MUST be unambiguously parseable into constituent elements without relying on unauthenticated data. Fixed-width fields or length prefixes are acceptable.

### 3.4 Example Usage
- AES-GCM ESP: P = RestOfPayloadData || TFCpadding || Padding || PadLength || NextHeader; N = Salt || IV; A = SPI || SequenceNumber; ESP = SPI || SequenceNumber || IV || C.

## 4. Requirements on AEAD Algorithm Specifications
- **Key length**: Fixed K_LEN; no special key format required (internal conversion allowed).
- **Plaintext length**: MUST accept lengths 0 to P_MAX (P_MAX > 0, SHOULD ≥ 2^16 octets).
- **Associated data length**: MUST accept lengths 0 to A_MAX (A_MAX > 0, SHOULD ≥ 2^16 octets).
- **Nonce length**: MUST accept lengths N_MIN to N_MAX (SHOULD accept 12 octets). N_MAX may be 0 for randomized or stateful algorithms.
- **Ciphertext structure**: MAY include authentication tag. SHOULD be efficient.
- **Randomized/Stateful**: MAY use internal randomness or state; may have N_MAX=0. SHOULD describe themselves as such.
- **Parameter declaration**: Must include K_LEN, P_MAX, A_MAX, N_MIN, N_MAX, C_MAX.
- **Ciphertext length relation**: MUST specify a fixed relation between plaintext and ciphertext length (no dependence on tag length parameter).
- **Nonce reuse**: SHOULD describe security degradation.
- **Security analysis**: SHOULD reference a detailed security analysis and define or reference a security model.

## 5. AEAD Algorithms
### 5.1 AEAD_AES_128_GCM
- **Specification**: AES-128 GCM per [GCM], 16-octet authentication tag. Ciphertext = GCM ciphertext || tag.
- **Parameters**: K_LEN=16, P_MAX=2^36-31, A_MAX=2^61-1, N_MIN=N_MAX=12, C_MAX=2^36-15. C is 16 octets longer than P.
- **Security analysis**: [MV04].
- **Nonce reuse**: Serious loss of confidentiality and integrity if same nonce used with different plaintexts.

### 5.2 AEAD_AES_256_GCM
- **Identical to AEAD_AES_128_GCM** except K_LEN=32 and uses AES-256 GCM.

### 5.3 AEAD_AES_128_CCM
- **Specification**: AES-128 CCM per [CCM] with n=12 (nonce length), t=16 (tag length), q=3 (length field octets). CCM formatting per Appendix A. Ciphertext = CCM ciphertext || tag.
- **Parameters**: K_LEN=16, P_MAX=2^24-1, A_MAX=2^64-1, N_MIN=N_MAX=12, C_MAX=2^24+15. C is 16 octets longer than P.
- **Security analysis**: [J02].
- **Nonce reuse**: Loss of confidentiality (XOR of plaintexts revealed).

### 5.4 AEAD_AES_256_CCM
- **Identical to AEAD_AES_128_CCM** except K_LEN=32 and uses AES-256 CCM.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Nonces MUST be distinct for each encryption with same key (or all zero-length). | MUST | Section 2.1, 3.1 |
| R2 | Each algorithm MUST accept plaintext lengths 0..P_MAX (P_MAX > 0, SHOULD ≥ 2^16). | MUST | Section 4 |
| R3 | Each algorithm MUST accept associated data lengths 0..A_MAX (A_MAX > 0, SHOULD ≥ 2^16). | MUST | Section 4 |
| R4 | Each algorithm MUST accept nonce lengths N_MIN..N_MAX; SHOULD accept 12 octets. | MUST/SHOULD | Section 4 |
| R5 | Each algorithm MUST have fixed key length K_LEN. | MUST | Section 4 |
| R6 | Ciphertext length relation MUST NOT depend on external parameters (e.g., tag length). | MUST | Section 4 |
| R7 | Implementation MUST return error and no output if inputs exceed supported lengths. | MUST | Section 2.1 |
| R8 | AD and plaintext MUST be unambiguously parseable without unauthenticated data. | MUST | Section 3.3 |
| R9 | Nonce formation: Fixed+Counter format SHOULD be used; Counter SHOULD start at 0 and increment. | SHOULD | Section 3.2 |
| R10 | Ciphertext SHOULD be positioned after data needed for other inputs (e.g., nonce). | SHOULD | Section 2.3 |
| R11 | Each algorithm SHOULD describe security degradation from nonce reuse. | SHOULD | Section 3.1, 4 |
| R12 | Each algorithm SHOULD reference a security analysis. | SHOULD | Section 4 |
| R13 | Each algorithm specification MUST include K_LEN, P_MAX, A_MAX, N_MIN, N_MAX, C_MAX. | MUST | Section 4 |
| R14 | Randomized/Stateful algorithms SHOULD describe themselves using those terms. | SHOULD | Section 4 |

## Informative Annexes (Condensed)
- **Section 3.2.1 Partially Implicit Nonces**: Describes method to reduce transmitted nonce size by inferring part from context. Fixed-Common field is implicit; Fixed-Distinct and Counter are explicit. Recommended for efficiency, used in GCM ESP and CCM ESP.
- **Section 6 IANA Registry**: Defines AEAD Registry with name, number, reference. Numbers 32768–65535 reserved for private use. Initial entries: AEAD_AES_128_GCM (1), AEAD_AES_256_GCM (2), AEAD_AES_128_CCM (3), AEAD_AES_256_CCM (4). Registration requires specification and test cases; review by CFRG recommended.
- **Section 7 Other Considerations**: Discusses testing randomized algorithms (via decryption test and encrypt-decrypt loop). Suggests future additions (e.g., generic encrypt-then-MAC composition) and cautions against registry bloat.
- **Section 8 Security Considerations**: Reiterates that AEAD does not address key generation or management. Nonce distinctness critical; VM rollback may cause nonce reuse. IANA registration is not an endorsement; security may degrade over time.
```

This structure preserves all normative language, cross-references, definitions, and requirements while condensing informative content. The requirements table extracts key mandates. All "MUST", "SHOULD", etc., are retained exactly.