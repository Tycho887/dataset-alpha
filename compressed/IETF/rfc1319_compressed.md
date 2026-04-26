# RFC 1319: The MD2 Message-Digest Algorithm
**Source**: Network Working Group | **Version**: April 1992 | **Date**: April 1992 | **Type**: Informative  
**Original**: https://tools.ietf.org/html/rfc1319 (IETF)

## Scope (Summary)
This document specifies the MD2 message-digest algorithm, which produces a 128-bit "fingerprint" from a message of arbitrary length. MD2 is intended for digital signature applications where secure compression is needed before signing with a public-key cryptosystem (e.g., RSA). The algorithm is provided for non-commercial Internet Privacy-Enhanced Mail.

## Normative References
- [1] Linn, J., "Privacy Enhancement for Internet Electronic Mail: Part I – Message Encipherment and Authentication Procedures", RFC 1113, August 1989.
- [2] Kent, S., and J. Linn, "Privacy Enhancement for Internet Electronic Mail: Part II – Certificate-Based Key Management", RFC 1114, August 1989.
- [3] Linn, J., "Privacy Enhancement for Internet Electronic Mail: Part III – Algorithms, Modes, and Identifiers", RFC 1115, August 1989.
- [4] CCITT Recommendation X.509 (1988), "The Directory – Authentication Framework".

## Definitions and Abbreviations
- **byte**: an eight-bit quantity.
- **x_i**: denotes "x sub i". If subscript is an expression, surround in braces: x_{i+1}.
- **x^i**: x to the i-th power (exponent).
- **X xor Y**: bit-wise XOR of X and Y.

## Algorithm Description

### Step 1. Append Padding Bytes
- **Requirement**: The message shall be padded so that its length (in bytes) is congruent to 0 modulo 16.
- **Method**: "i" bytes of value "i" shall be appended until the padded message length is a multiple of 16. At least one byte and at most 16 bytes are appended.
- **Result**: The padded message is M[0 ... N-1] where N is a multiple of 16.

### Step 2. Append Checksum
- **Requirement**: A 16-byte checksum of the message shall be appended.
- **Permutation table S[0..255]**: A 256-byte "random" permutation constructed from the digits of pi (given in appendix).
- **Algorithm**:
  1. Clear checksum C[0..15] to 0.
  2. Set L = 0.
  3. For each 16-byte block i (0 to N/16-1):
     - For j = 0 to 15:
       - c = M[i*16+j]
       - C[j] = S[c xor L]
       - L = C[j]
- **Result**: Checksum C[0..15] is appended. Let M[0..N'-1] be the padded message plus checksum (N' = N + 16).

### Step 3. Initialize MD Buffer
- **Requirement**: A 48-byte buffer X shall be initialized to zero.

### Step 4. Process Message in 16-Byte Blocks
- **Requirement**: Process each 16-byte block of the message (including checksum) using the same permutation S from Step 2.
- **Algorithm**:
  - For each block i (0 to N'/16-1):
    1. Copy block i into X[16..31] and set X[32..47] = X[16..31] xor X[0..15].
    2. Set t = 0.
    3. Do 18 rounds (j = 0 to 17):
       - For k = 0 to 47: t = X[k] ^= S[t]
       - t = (t + j) mod 256.

### Step 5. Output
- **Requirement**: The 128-bit (16-byte) message digest is X[0..15].

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The message shall be padded so that its length is congruent to 0 modulo 16, using i bytes of value i. | shall | §3.1 |
| R2 | A 16-byte checksum shall be computed using the permutation table S and appended. | shall | §3.2 |
| R3 | The MD buffer X (48 bytes) shall be initialized to zero. | shall | §3.3 |
| R4 | Each 16-byte block (including checksum) shall be processed using the permutation S across 18 rounds. | shall | §3.4 |
| R5 | The message digest output shall be X[0..15]. | shall | §3.5 |

## Informative Annexes (Condensed)

- **Appendix A – Reference Implementation**: Contains C source code (`global.h`, `md2.h`, `md2c.c`, `mddriver.c`) from RSAREF. The implementation defines MD2_CTX structure, functions MD2Init, MD2Update, MD2Final, and includes the PI_SUBST permutation table. The driver compiles for MD2, MD4, or MD5. A test suite provides expected hex digests for seven strings.
- **Security Considerations**: The security level is considered sufficient for high-security hybrid digital signature schemes based on MD2 and a public-key cryptosystem.