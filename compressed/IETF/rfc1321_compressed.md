# RFC 1321: The MD5 Message-Digest Algorithm
**Source**: Network Working Group / R. Rivest | **Version**: April 1992 | **Date**: April 1992 | **Type**: Informative (not an Internet standard)
**Original**: https://datatracker.ietf.org/doc/html/rfc1321

## Scope (Summary)
This document describes the MD5 message‑digest algorithm, which produces a 128‑bit fingerprint of an arbitrary‑length input. It is intended for digital signature applications and is an extension of MD4.

## Normative References
- [1] Rivest, R., “The MD4 Message Digest Algorithm”, RFC 1320, April 1992.
- [2] Rivest, R., “The MD4 message digest algorithm”, in A.J. Menezes and S.A. Vanstone, editors, Advances in Cryptology – CRYPTO ’90 Proceedings, pages 303–311, Springer‑Verlag, 1991.
- [3] CCITT Recommendation X.509 (1988), “The Directory – Authentication Framework.”

## Definitions and Abbreviations
- **word**: 32‑bit quantity.
- **byte**: eight‑bit quantity.
- **b‑bit message**: input message of arbitrary non‑negative length.
- **M[0…N‑1]**: words of the padded message, where N is a multiple of 16.
- **F, G, H, I**: auxiliary functions defined in Section 3.4.
- **T[1…64]**: 64‑element table derived from the sine function (see appendix).
- **MD5_CTX**: structure holding state (A, B, C, D), bit‑count, and input buffer.

## Algorithm Description (Normative Requirements)

### Step 1 – Append Padding Bits
- **R‑MD5‑1.1**: The message shall be padded so that its length (in bits) is congruent to 448 modulo 512. Padding is always performed.
- **R‑MD5‑1.2**: Padding shall consist of a single “1” bit, followed by “0” bits until the length reaches 448 mod 512. At least one bit and at most 512 bits are appended.

### Step 2 – Append Length
- **R‑MD5‑2.1**: A 64‑bit representation of the original message length b (before padding) shall be appended to the result of Step 1. If b > 2^64, only the low‑order 64 bits are used.
- **R‑MD5‑2.2**: The 64 bits shall be appended as two 32‑bit words, low‑order word first.
- **R‑MD5‑2.3**: After this step, the message length shall be an exact multiple of 512 bits (16 words). Denote the words as M[0…N‑1], N multiple of 16.

### Step 3 – Initialize MD Buffer
- **R‑MD5‑3.1**: A four‑word buffer (A, B, C, D) shall be initialized to the following hexadecimal values (low‑order bytes first):
  - A: 0x67452301
  - B: 0xefcdab89
  - C: 0x98badcfe
  - D: 0x10325476

### Step 4 – Process Message in 16‑Word Blocks
- **R‑MD5‑4.1**: Define four auxiliary functions (each takes three 32‑bit words, returns one 32‑bit word):
  - F(X,Y,Z) = XY v not(X) Z
  - G(X,Y,Z) = XZ v Y not(Z)
  - H(X,Y,Z) = X xor Y xor Z
  - I(X,Y,Z) = Y xor (X v not(Z))
- **R‑MD5‑4.2**: Use a 64‑element table T[1…64] where T[i] = floor(2^32 × |sin(i)|), i in radians. The table is given in the appendix.
- **R‑MD5‑4.3**: For each 16‑word block i (0 to N/16‑1):
  1. Copy block i into X[0…15].
  2. Save A = AA, B = BB, C = CC, D = DD.
  3. Perform four rounds of 16 operations each (rounds 1–4), using the [abcd k s i] notation defined in the text. The exact operations are specified in the source code (see Annex A.3).
  4. Update registers: A = A + AA, B = B + BB, C = C + CC, D = D + DD.

### Step 5 – Output
- **R‑MD5‑5.1**: The message digest shall be the concatenation of A, B, C, D, beginning with the low‑order byte of A and ending with the high‑order byte of D.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R‑MD5‑1.1 | Padded length congruent to 448 mod 512, always performed | shall | Section 3.1 |
| R‑MD5‑1.2 | Padding bits: 1 followed by 0s | shall | Section 3.1 |
| R‑MD5‑2.1 | Append 64‑bit representation of original length (low‑order if >2^64) | shall | Section 3.2 |
| R‑MD5‑2.2 | Append length as two 32‑bit words, low‑order first | shall | Section 3.2 |
| R‑MD5‑2.3 | Resulting message length multiple of 512 bits (16 words) | shall | Section 3.2 |
| R‑MD5‑3.1 | Buffer initialization to given hex values | shall | Section 3.3 |
| R‑MD5‑4.1 | Define F, G, H, I as specified | shall | Section 3.4 |
| R‑MD5‑4.2 | Use T table from sine function | shall | Section 3.4 |
| R‑MD5‑4.3 | Process each 16‑word block as described (four rounds) | shall | Section 3.4 |
| R‑MD5‑5.1 | Output digest as concatenation of A, B, C, D, low‑order byte first | shall | Section 3.5 |

## Informative Annexes (Condensed)
- **Appendix A – Reference Implementation**: Contains files `global.h`, `md5.h`, `md5c.c`, and `mddriver.c` from RSAREF. The implementation is portable; optimization suggestions (e.g., using typecast on little‑endian platforms) are noted. The source code provides the exact constants, shift amounts, and operation sequences for rounds 1–4. A test suite is included; expected outputs are given for seven test strings.

## Security Considerations
The level of security described is considered sufficient for implementing hybrid digital‑signature schemes based on MD5 and a public‑key cryptosystem. However, the document notes that further security analysis is justified, as with any new proposal.