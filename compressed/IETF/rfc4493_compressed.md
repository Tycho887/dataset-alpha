# RFC 4493: The AES-CMAC Algorithm
**Source**: IETF Network Working Group | **Version**: Informational | **Date**: June 2006 | **Type**: Informative
**Original**: https://tools.ietf.org/html/rfc4493

## Scope (Summary)
This memo specifies the AES-CMAC authentication algorithm, which is a Cipher-based Message Authentication Code (CMAC) using the 128-bit Advanced Encryption Standard (AES). It is equivalent to the One-Key CBC MAC1 (OMAC1) and provides data integrity and authentication for messages of arbitrary length.

## Normative References
- [NIST-CMAC] NIST SP 800-38B, "Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication", May 2005.
- [NIST-AES] NIST FIPS 197, "Advanced Encryption Standard (AES)", November 2001.
- [RFC4086] Eastlake, D., et al., "Randomness Requirements for Security", BCP 106, RFC 4086, June 2005.

## Definitions and Abbreviations
- **x || y**: Concatenation of strings x and y.
- **x XOR y**: Bit-wise exclusive-OR of equal-length strings.
- **ceil(x)**: Smallest integer ≥ x.
- **x << 1**: Left-shift by 1 bit (MSB discarded, zero inserted at LSB).
- **0^n**: String of n zero-bits.
- **MSB(x)**: Most-significant bit of x.
- **padding(x)**: Pads x with a single '1' followed by zeros to reach 128 bits.
- **Key (K)**: 128-bit key for AES-128.
- **First subkey (K1)**: 128-bit subkey derived from K via Generate_Subkey().
- **Second subkey (K2)**: 128-bit subkey derived from K via Generate_Subkey().
- **Message (M)**: Data to be authenticated; length denoted by len (octets), may be null.
- **AES-128(K,M)**: 128-bit ciphertext of AES-128 with key K and message M.
- **MAC (T)**: 128-bit output of AES-CMAC; may be truncated.
- **MAC length**: Default 128 bits; truncation possible in most significant bits first order; must be fixed before communication and not changed during key lifetime.

## 1. Introduction
AES-CMAC is a keyed hash function based on AES, equivalent to OMAC1. It provides stronger assurance than checksums, detecting intentional data modifications. It is appropriate where AES is more readily available than a hash function (e.g., compared to HMAC). This memo specifies AES-CMAC with AES-128.

## 2. Specification of AES-CMAC

### 2.1 Basic Definitions
*(Covered in Definitions section above)*

### 2.2 Overview
- AES-CMAC uses the basic CBC-MAC with two cases:
  - **Case (a)**: If message length is a positive multiple of 128 bits, the last block M_n is XORed with K1 before final encryption.
  - **Case (b)**: Otherwise, the last block is padded with 10^i, then XORed with K2 before final encryption.
- Output is 128-bit MAC T.

### 2.3 Subkey Generation Algorithm - Generate_Subkey()
**Input**: K (128-bit key)  
**Output**: K1, K2 (128-bit subkeys)  

- **Step 1**: L := AES-128(K, const_Zero) where const_Zero = 0x00000000000000000000000000000000.
- **Step 2**: If MSB(L) == 0 then K1 := L << 1; else K1 := (L << 1) XOR const_Rb, where const_Rb = 0x00000000000000000000000000000087.
- **Step 3**: If MSB(K1) == 0 then K2 := K1 << 1; else K2 := (K1 << 1) XOR const_Rb.
- **Step 4**: Return (K1, K2).

### 2.4 MAC Generation Algorithm - AES-CMAC()
**Input**: K (128-bit key), M (message), len (message length in octets)  
**Output**: T (128-bit MAC)  

- **Step 1**: (K1, K2) := Generate_Subkey(K).
- **Step 2**: n := ceil(len / 16). If n == 0 then set n = 1, flag = false.
- **Step 3**: If len mod 16 == 0 then flag = true (complete last block); else flag = false.
- **Step 4**: If flag true, M_last := M_n XOR K1; else M_last := padding(M_n) XOR K2.
- **Step 5**: X := const_Zero.
- **Step 6**: For i = 1 to n-1: Y := X XOR M_i; X := AES-128(K,Y). Then Y := M_last XOR X; T := AES-128(K,Y).
- **Step 7**: Return T. If truncation is needed, take most significant bits first.

> **Note**: At least a 64-bit MAC should be used as protection against guessing attacks.

### 2.5 MAC Verification Algorithm - Verify_MAC()
**Input**: K, M, len, T' (received MAC)  
**Output**: VALID or INVALID  

- **Step 1**: T* := AES-CMAC(K, M, len).
- **Step 2**: If T* == T' then return VALID; else return INVALID.
- If INVALID, message is definitely not authentic. If VALID, assurance is provided but not absolute.

## 3. Security Considerations
- AES-CMAC security relies on the strength of AES and the secrecy of K.
- **Secret key shall be generated** meeting pseudo-randomness requirements of RFC 4086.
- **Secret key should be kept safe.**
- If used properly, AES-CMAC provides authentication and integrity consistent with best current practice.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Last block shall be XORed with K1 if message length is positive multiple of block size; otherwise padded and XORed with K2. | shall | 2.2, 2.4 Step 4 |
| R2 | MAC length must be specified before communication starts and must not be changed during key lifetime. | must | 2.1 |
| R3 | At least a 64-bit MAC should be used. | should | 2.4 (NIST-CMAC) |
| R4 | Secret key shall be generated per RFC 4086 randomness requirements. | shall | 3 |
| R5 | Secret key should be kept safe. | should | 3 |

## Informative Annexes (Condensed)

### Appendix A. Test Code
A C source implementation is provided to verify correctness against the test vectors in Section 4. It is not intended for commercial use. The code implements `generate_subkey()`, `padding()`, `AES_CMAC()`, and utility functions.

### Section 4. Test Vectors
Four test examples are given: (1) len=0, (2) len=16, (3) len=40, (4) len=64, along with subkey generation outputs. These match the NIST SP 800-38B test vectors.

### Section 5. Acknowledgement
Portions borrowed from NIST-CMAC; thanks to OMAC1 authors, SP 800-38B author, Russ Housley, Alfred Hoenes. Funding from US Army and NSF grants.

### Section 6.2 Informative References
- [RFC-HMAC] RFC 2104 (HMAC)
- [OMAC1a, OMAC1b] Iwata and Kurosawa, OMAC specification
- [XCBCa, XCBCb] Black and Rogaway, XCBC constructions