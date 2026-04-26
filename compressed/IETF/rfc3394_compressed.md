# RFC 3394: Advanced Encryption Standard (AES) Key Wrap Algorithm
**Source**: Internet Society (IETF) | **Version**: Informational | **Date**: September 2002 | **Type**: Informational  
**Original**: https://tools.ietf.org/html/rfc3394

## Scope (Summary)
This document makes the AES Key Wrap algorithm available to the Internet community. It defines a method to securely encrypt plaintext key data (plaintext) using the AES cipher as a primitive, producing ciphertext longer than the AES block size (128 bits). The algorithm provides integrity protection through an initial value (IV) check.

## Normative References
- **AES**: National Institute of Standards and Technology. FIPS Pub 197: Advanced Encryption Standard (AES). 26 November 2001.
- **AES-WRAP**: National Institute of Standards and Technology. AES Key Wrap Specification. 17 November 2001. [http://csrc.nist.gov/encryption/kms/key-wrap.pdf]

## Definitions and Abbreviations
- **AES(K, W)**: Encrypt W using AES codebook with key K
- **AES⁻¹(K, W)**: Decrypt W using AES codebook with key K
- **MSB(j, W)**: Most significant j bits of W
- **LSB(j, W)**: Least significant j bits of W
- **B1 ^ B2**: Bitwise exclusive OR (XOR) of B1 and B2
- **B1 | B2**: Concatenation of B1 and B2
- **K**: Key-encryption key (KEK)
- **n**: Number of 64-bit key data blocks (n ≥ 2)
- **s**: Number of steps in wrapping, s = 6n
- **P[i]**: i-th plaintext key data block (64-bit)
- **C[i]**: i-th ciphertext data block (64-bit)
- **A**: 64-bit integrity check register
- **R[i]**: Array of 64-bit registers (i = 0..n)
- **A[t], R[i][t]**: Contents after encryption step t
- **IV**: 64-bit initial value used during wrapping

## Key Wrap Algorithm

### Key Wrap (Section 2.2.1)
- **Inputs**: Plaintext n × 64-bit values {P₁,…,Pₙ}; Key K (KEK)
- **Outputs**: Ciphertext (n+1) × 64-bit values {C₀,…,Cₙ}
- **Procedure** (shifting description):
  1. Set A[0] = IV (see 2.2.3). For i=1..n: R[0][i] = P[i]
  2. For t=1..s (s=6n): A[t] = MSB(64, AES(K, A[t-1] | R[t-1][1])) ^ t ; for i=1..n-1: R[t][i] = R[t-1][i+1]; R[t][n] = LSB(64, AES(K, A[t-1] | R[t-1][1]))
  3. Output: C[0] = A[s]; for i=1..n: C[i] = R[s][i]
- **Alternative indexing description** (in-place): Same results; uses nested loops j=0..5, i=1..n with B = AES(K, A | R[i]), A = MSB(64, B) ^ t where t = n*j+i, R[i] = LSB(64, B).

### Key Unwrap (Section 2.2.2)
- **Inputs**: Ciphertext (n+1) × 64-bit values {C₀,…,Cₙ}; Key K (KEK)
- **Outputs**: Plaintext n × 64-bit values {P₁,…,Pₙ} or error
- **Procedure** (shifting):
  1. A[s] = C[0]; for i=1..n: R[s][i] = C[i] (s=6n)
  2. For t=s..1: A[t-1] = MSB(64, AES⁻¹(K, (A[t] ^ t) | R[t][n])); R[t-1][1] = LSB(64, AES⁻¹(K, (A[t]^t) | R[t][n])); for i=2..n: R[t-1][i] = R[t][i-1]
  3. If A[0] equals the expected IV → output P[i] = R[0][i]; else return an error.
- **Alternative indexing description** (in-place): Use j=5..0, i=n..1 with B = AES⁻¹(K, (A ^ t) | R[i]) where t = n*j+i, A = MSB(64,B), R[i] = LSB(64,B). Then check IV.

### Key Data Integrity – Initial Value (Section 2.2.3)
- The initial value (IV) is assigned to A[0] at the start of wrapping and verified at the end of unwrapping. If the recovered A[0] matches the expected value, the key is accepted; otherwise, the unwrapping algorithm MUST return an error and MUST NOT return any key data.
- **Default IV** (Section 2.2.3.1): `A[0] = IV = 0xA6A6A6A6A6A6A6A6`. This provides a strong integrity check: probability of undetected corruption is 2⁻⁶⁴.
- **Alternative Initial Values** (Section 2.2.3.2): May be defined by NIST for broader integrity scope or non-standard key data. Implementations that are not application-specific require flexibility in setting/testing the IV.

## Object Identifiers (Section 3)
- NIST assigned OIDs for the key wrap with default IV, per KEK AES key size:
  - `id-aes128-wrap`: { joint-iso-itu-t(2) country(16) us(840) organization(1) gov(101) csor(3) nistAlgorithm(4) 1 aes 5 }
  - `id-aes192-wrap`: { aes 25 }
  - `id-aes256-wrap`: { aes 45 }

## Test Vectors (Section 4)
The document provides six test vectors using the index-based implementation. Each includes input, wrap/unwrap steps, and output. Vectors cover:
- 128-bit key data with 128/192/256-bit KEK
- 192-bit key data with 192/256-bit KEK
- 256-bit key data with 256-bit KEK
All vectors are included verbatim in the original for conformance testing; they are not reproduced here due to space, but must be used for validation.

## Security Considerations (Section 5)
- The integrity check provides 2⁻⁶⁴ probability of undetected corruption. If unwrapping produces an unexpected A[0], the implementation MUST return an error and MUST NOT return any key data.
- The KEK must be protected from disclosure. Compromise of the KEK may result in disclosure of all key data protected with that KEK.

## Informative Annexes (Condensed)
- **Test Vectors (Section 4)**: Six examples demonstrating wrap and unwrap for various key sizes. These are informative and serve as conformance checks.
- **Acknowledgments (Section 7)**: Most text derived from NIST’s AES-WRAP document.
- **Full Copyright Statement (Section 9)**: Standard IETF copyright; document provided "AS IS".

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The key wrap algorithm must operate on 64-bit blocks; plaintext must be n blocks (n ≥ 2). | shall | Section 2 |
| R2 | The KEK must be a valid AES key (128, 192, or 256 bits). | shall | Section 1 |
| R3 | During unwrap, if A[0] does not equal the expected IV, the algorithm MUST return an error and MUST NOT return any key data. | mandatory | Section 2.2.3, 5 |
| R4 | The default IV is 0xA6A6A6A6A6A6A6A6. | shall | Section 2.2.3.1 |
| R5 | Implementations must protect the KEK from disclosure. | mandatory | Section 5 |
| R6 | The key wrap and unwrap procedures must follow the specified steps (shifting or indexing) to produce correct output. | shall | Sections 2.2.1, 2.2.2 |