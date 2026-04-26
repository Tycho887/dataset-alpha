# RFC 2104: HMAC: Keyed-Hashing for Message Authentication
**Source**: Internet Engineering Task Force (IETF) | **Version**: RFC 2104 | **Date**: February 1997 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc2104

## Scope (Summary)
This document defines HMAC, a mechanism for message authentication using any iterative cryptographic hash function (e.g., MD5, SHA‑1) combined with a secret shared key. The cryptographic strength of HMAC depends on the properties of the underlying hash function.

## Normative References
- [MD5] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [SHA] NIST, FIPS PUB 180-1: Secure Hash Standard, April 1995.
- [RIPEMD] H. Dobbertin, A. Bosselaers, B. Preneel, "RIPEMD-160: A strengthened version of RIPEMD", Fast Software Encryption, LNCS Vol 1039, pp. 71-82.
- [ANSI] ANSI X9.9, "American National Standard for Financial Institution Message Authentication (Wholesale)", 1981/1986.
- [BCK1] M. Bellare, R. Canetti, H. Krawczyk, "Keyed Hash Functions and Message Authentication", Crypto'96.
- [PV] B. Preneel, P. van Oorschot, "Building fast MACs from hash functions", CRYPTO'95.

## Definitions and Abbreviations
- **HMAC**: Keyed‑Hashing for Message Authentication, a MAC mechanism based on cryptographic hash functions.
- **H**: A generic iterative cryptographic hash function (e.g., MD5, SHA‑1).
- **B**: Byte‑length of the blocks on which H iterates (e.g., B=64 for MD5 and SHA‑1).
- **L**: Byte‑length of hash outputs (L=16 for MD5, L=20 for SHA‑1).
- **ipad**: The byte 0x36 repeated B times (inner padding).
- **opad**: The byte 0x5C repeated B times (outer padding).
- **K**: Secret authentication key (length ≤ B bytes; keys > B are first hashed to L bytes).
- **text**: The data stream to be authenticated.

## Section 1: Introduction
HMAC provides integrity verification based on a secret key shared between two parties. The construction:
- Uses available hash functions without modification.
- Preserves hash performance.
- Handles keys simply.
- Is based on well‑understood cryptographic analysis.
- Allows easy replacement of the underlying hash function.

Specific instantiations (e.g., HMAC‑SHA1, HMAC‑MD5, HMAC‑RIPEMD) are defined by choosing H.

## Section 2: Definition of HMAC
The HMAC algorithm computes:

`HMAC(K, text) = H( (K XOR opad) || H( (K XOR ipad) || text ) )`

### Steps (normative procedure):
1. Append zeros to K to create a B‑byte string.
2. XOR the B‑byte string with ipad.
3. Append `text` to the result of step (2).
4. Apply H to the stream from step (3) (inner hash).
5. XOR the original B‑byte string with opad.
6. Append the inner hash result (L bytes) to the result of step (5).
7. Apply H to the stream from step (6) and output the result.

## Section 3: Keys
- Keys can be of any length. Keys longer than B bytes are first hashed using H.
- **Strongly discouraged**: keys shorter than L bytes, as this would decrease security strength.
- Keys longer than L bytes are acceptable but do not significantly increase strength (unless the key's randomness is weak).
- **Recommendation**: Keys need to be chosen at random (or using a cryptographically strong pseudo‑random generator seeded with a random seed), and **periodically refreshed**.

## Section 4: Implementation Note
HMAC can be implemented without modifying the hash function code by using the predefined initial value IV. Performance can be improved by precomputing the compression function outputs for `(K XOR ipad)` and `(K XOR opad)` only once per key. The stored intermediate values must be protected as secret keys. This optimization does not affect interoperability.

## Section 5: Truncated Output
- Applications **may** truncate the HMAC output to t leftmost bits.
- **Recommendation**: t should be not less than half the length of the hash output (to match the birthday attack bound) and **not less than 80 bits**.
- Notation: `HMAC-H-t` denotes HMAC using hash function H with t bits of output (e.g., HMAC-SHA1-80). If t is not specified, all hash bits are output.

## Section 6: Security
- Security depends on the collision resistance of H (with a secret, random IV) and the message‑authentication property of the compression function.
- Two important properties:
  1. The construction is independent of hash function details; H can be replaced.
  2. Message authentication has a “transient” effect – a broken scheme affects only future authentications, not past ones.
- The strongest known attack (birthday attack) is totally impractical for reasonable hash functions. For example, with MD5 (128‑bit output) an attacker would need ~2^64 chosen‑plaintext tags, which is infeasible.
- A correct implementation, random keys, secure key exchange, frequent key refreshment, and good key secrecy are essential.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Keys longer than B bytes shall first be hashed using H. | shall | Section 2 |
| R2 | Keys less than L bytes are strongly discouraged. | recommendation | Section 3 |
| R3 | Keys shall be chosen at random and periodically refreshed. | recommendation | Section 3 |
| R4 | If output is truncated, t shall be at least half the hash output length and at least 80 bits. | recommendation | Section 5 |
| R5 | Implementation may precompute compression function outputs for (K XOR ipad) and (K XOR opad) for performance; stored values must be protected as secret keys. | shall (must protect) | Section 4 |

## Informative Annexes (Condensed)
- **Appendix – Sample Code**: Provides C code implementing HMAC‑MD5, including functions for padding and the two‑pass hash structure. The code demonstrates the algorithm using the MD5 library.
- **Test Vectors**: Lists three test cases (key, data, expected digest) to verify HMAC‑MD5 implementations:
  1. Key 0x0b…0b (16 bytes), data “Hi There” → digest 0x9294…9d
  2. Key “Jefe”, data “what do ya want for nothing?” → digest 0x750c…38
  3. Key 0xAA…AA (16 bytes), data 0xDD…DD (50 bytes) → digest 0x56be…f6
- **Acknowledgments**: Credits contributors and reviewers.
- **References**: Full citations for all works referenced in the document.