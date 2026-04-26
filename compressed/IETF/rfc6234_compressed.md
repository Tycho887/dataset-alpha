# RFC 6234: US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)
**Source**: IETF (Internet Engineering Task Force) | **Version**: Informational, Obsoletes RFC 4634, Updates RFC 3174 | **Date**: May 2011 | **Type**: Informational
**Original**: https://www.rfc-editor.org/info/rfc6234

## Scope (Summary)
This document provides specifications and open source C code for the US Federal Information Processing Standard (FIPS) Secure Hash Algorithms SHA-224, SHA-256, SHA-384, and SHA-512 (SHA-1 is specified in RFC 3174). It also includes code for HMAC (RFC 2104) and HKDF (RFC 5869) based on these SHA algorithms. The text is adapted from FIPS 180-2.

## Normative References
- [RFC2104] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [RFC5869] Krawczyk, H. and P. Eronen, "HMAC-based Extract-and-Expand Key Derivation Function (HKDF)", RFC 5869, May 2010.
- [SHS] "Secure Hash Standard", US NIST, FIPS 180-3, http://csrc.nist.gov/publications/fips/fips180-3/fips180-3_final.pdf
- [US-ASCII] ANSI X3.4, "USA Standard Code for Information Interchange", 1968.

## Informative References
- [RFC3174] Eastlake 3rd, D. and P. Jones, "US Secure Hash Algorithm 1 (SHA1)", RFC 3174, September 2001.
- [RFC3874] Housley, R., "A 224-bit One-way Hash Function: SHA-224", RFC 3874, September 2004.
- [RFC4055] Schaad, J., Kaliski, B., and R. Housley, "Additional Algorithms and Identifiers for RSA Cryptography for use in the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 4055, June 2005.
- [RFC4086] Eastlake 3rd, D., Schiller, J., and S. Crocker, "Randomness Requirements for Security", BCP 106, RFC 4086, June 2005.
- [RFC4634] Eastlake 3rd, D. and T. Hansen, "US Secure Hash Algorithms (SHA and HMAC-SHA)", RFC 4634, July 2006.
- [RFC6194] Polk, T., Chen, L., Turner, S., and P. Hoffman, "Security Considerations for the SHA-0 and SHA-1 Message-Digest Algorithms", RFC 6194, March 2011.
- [SHAVS] "The Secure Hash Algorithm Validation System (SHAVS)", http://csrc.nist.gov/groups/STM/cavp/documents/shs/SHAVS.pdf, July 2004.

## Definitions and Abbreviations
- **hex digit**: element of {0,1,...,9,A,...,F}, representing a 4-bit string.
- **word**: 32-bit or 64-bit string, represented as 8 or 16 hex digits. Big-endian convention used.
- **block**: 512-bit (SHA-224, SHA-256) or 1024-bit (SHA-384, SHA-512) string.
- **SHR^n(x)**: right shift of w-bit word x by n bits (0 ≤ n < w).
- **ROTR^n(x)**: circular right shift of w-bit word x by n bits.
- **ROTL^n(x)**: circular left shift of w-bit word x by n bits.
- **CH(x,y,z)**: (x AND y) XOR ((NOT x) AND z).
- **MAJ(x,y,z)**: (x AND y) XOR (x AND z) XOR (y AND z).
- **BSIG0(x)**: ROTR^2(x) XOR ROTR^13(x) XOR ROTR^22(x) (32-bit) or ROTR^28(x) XOR ROTR^34(x) XOR ROTR^39(x) (64-bit).
- **BSIG1(x)**: ROTR^6(x) XOR ROTR^11(x) XOR ROTR^25(x) (32-bit) or ROTR^14(x) XOR ROTR^18(x) XOR ROTR^41(x) (64-bit).
- **SSIG0(x)**: ROTR^7(x) XOR ROTR^18(x) XOR SHR^3(x) (32-bit) or ROTR^1(x) XOR ROTR^8(x) XOR SHR^7(x) (64-bit).
- **SSIG1(x)**: ROTR^17(x) XOR ROTR^19(x) XOR SHR^10(x) (32-bit) or ROTR^19(x) XOR ROTR^61(x) XOR SHR^6(x) (64-bit).
- **Message Digest**: output of the hash function, length 224, 256, 384, or 512 bits depending on algorithm.
- **HMAC**: Hashed Message Authentication Code as defined in [RFC2104].
- **HKDF**: HMAC-based Extract-and-Expand Key Derivation Function as defined in [RFC5869].
- **ASN.1 OIDs**: Object Identifiers for SHA algorithms (see Section 1).

## 1. Overview of Contents
This document includes specifications for SHA-224, SHA-256, SHA-384, SHA-512, and C code implementing these algorithms, SHA-based HMAC, and HKDF. Specifications for HMAC and HKDF are not included here; refer to [RFC2104] and [RFC5869]. This document obsoletes [RFC4634] and updates [RFC3174].

ASN.1 OIDs for SHA algorithms:
- id-sha1: {1 3 14 3 2 26}
- id-sha224: {2 16 840 1 101 3 4 2 4}
- id-sha256: {2 16 840 1 101 3 4 2 1}
- id-sha384: {2 16 840 1 101 3 4 2 2}
- id-sha512: {2 16 840 1 101 3 4 2 3}

## 2. Notation for Bit Strings and Integers
No additional requirements beyond definitions above.

## 3. Operations on Words
Bitwise operations (AND, OR, XOR, NOT), addition modulo 2^w, and shift/rotate operations are defined as above.

## 4. Message Padding and Parsing
### 4.1. SHA-224 and SHA-256
- **Input**: message of length L bits, L < 2^64.
- **Padding shall be** performed as follows:
  - a. Append "1".
  - b. Append K "0"s where K is smallest non-negative integer such that (L + 1 + K) mod 512 = 448.
  - c. Append 64-bit block representing L in binary (big-endian).
- After padding, total length is multiple of 512 bits.

### 4.2. SHA-384 and SHA-512
- **Input**: message of length L bits, L < 2^128.
- **Padding shall be** performed as follows:
  - a. Append "1".
  - b. Append K "0"s where K is smallest non-negative integer such that (L + 1 + K) mod 1024 = 896.
  - c. Append 128-bit block representing L in binary.
- After padding, total length is multiple of 1024 bits.

## 5. Functions and Constants Used
### 5.1. SHA-224 and SHA-256
- Logical functions CH, MAJ, BSIG0, BSIG1, SSIG0, SSIG1 defined on 32-bit words (see Definitions).
- Constants K0..K63: first 32 bits of fractional parts of cube roots of first 64 primes (hex values listed in Section 5.1).

### 5.2. SHA-384 and SHA-512
- Logical functions CH, MAJ, BSIG0, BSIG1, SSIG0, SSIG1 defined on 64-bit words (see Definitions).
- Constants K0..K79: first 64 bits of fractional parts of cube roots of first 80 primes (hex values listed in Section 5.2).

## 6. Computing the Message Digest
### 6.1. SHA-224 and SHA-256 Initialization
- **SHA-224 initial hash value H(0)**: eight 32-bit words as given in Section 6.1.
- **SHA-256 initial hash value H(0)**: eight 32-bit words as square roots of first eight primes (Section 6.1).

### 6.2. SHA-224 and SHA-256 Processing
- Message M padded as per Section 4.1, parsed into 512-bit blocks.
- For each block i:
  1. Prepare message schedule Wt (t=0..63):
     - t=0..15: Wt = M(i)t
     - t=16..63: Wt = SSIG1(W(t-2)) + W(t-7) + SSIG0(W(t-15)) + W(t-16)
  2. Initialize working variables a,b,c,d,e,f,g,h from H(i-1).
  3. Main hash computation (t=0..63):
     - T1 = h + BSIG1(e) + CH(e,f,g) + Kt + Wt
     - T2 = BSIG0(a) + MAJ(a,b,c)
     - Update a,b,c,d,e,f,g,h as per step 3.
  4. Compute intermediate hash H(i): add working variables to H(i-1).
- Final output: concatenation of H(N)0..H(N)7 for SHA-256; omit H(N)7 for SHA-224.

### 6.3. SHA-384 and SHA-512 Initialization
- **SHA-384 initial hash value H(0)**: eight 64-bit words from square roots of 9th through 16th primes (Section 6.3).
- **SHA-512 initial hash value H(0)**: eight 64-bit words from square roots of first eight primes (Section 6.3).

### 6.4. SHA-384 and SHA-512 Processing
- Message M padded as per Section 4.2, parsed into 1024-bit blocks.
- For each block i (t=0..79):
  1. Prepare message schedule Wt (t=0..15: M(i)t; t=16..79: Wt = SSIG1(W(t-2)) + W(t-7) + SSIG0(W(t-15)) + W(t-16).
  2. Initialize working variables.
  3. Main hash computation (t=0..79) using 64-bit operations (same structure as 6.2).
  4. Compute intermediate hash.
- Final output: concatenation of H(N)0..H(N)7 for SHA-512; omit H(N)6 and H(N)7 for SHA-384.

## 7. HKDF- and SHA-Based HMACs
### 7.1. SHA-Based HMACs
- HMAC as per [RFC2104] using any SHA algorithm.
- Sample code in Section 8.3 allows arbitrary bit-length input.

### 7.2. HKDF
- HKDF as per [RFC5869] based on HMAC.
- Sample code in Section 8.4.

## 8. C Code for SHAs, HMAC, and HKDF
The code is provided as a demonstration implementation. It includes:
- Header files: sha.h (declarations), stdint-example.h (if <stdint.h> unavailable), sha-private.h (internal macros).
- Source files: sha1.c (SHA-1), sha224-256.c (SHA-224 and SHA-256), sha384-512.c (SHA-384 and SHA-512), usha.c (unified interface).
- HMAC code (hmac.c) and HKDF code (hkdf.c).
- Test driver (shatest.c) exercising standard tests from FIPS 180-3, HMAC RFCs, and HKDF RFC 5869.

Functions return one of: shaSuccess(0), shaNull(1), shaInputTooLong(2), shaStateError(3), shaBadParam(4).

### 8.1. Header Files (Summary)
- Definitions of context structures (SHA1Context, SHA256Context, SHA512Context, USHAContext, HMACContext, HKDFContext) and function prototypes.
- Enum SHAversion: SHA1, SHA224, SHA256, SHA384, SHA512.
- Constants for hash sizes and block sizes.

### 8.2. SHA Code (Sections 8.2.1–8.2.4)
- Implements SHA-1, SHA-224/256, SHA-384/512 using the algorithms specified in Sections 4–6.
- Includes functions: Reset, Input, FinalBits, Result.
- USHAReset, USHAInput, USHAFinalBits, USHAResult provide unified interface.

### 8.3. HMAC Code (hmac.c)
- Implements hmac, hmacReset, hmacInput, hmacFinalBits, hmacResult as per [RFC2104].

### 8.4. HKDF Code (hkdf.c)
- Implements hkdf, hkdfExtract, hkdfExpand, hkdfReset, hkdfInput, hkdfFinalBits, hkdfResult as per [RFC5869].

### 8.5. Test Driver (shatest.c)
- Exercises all algorithms with predefined test vectors and random tests.
- Assumes ASCII character set; runtime check warns otherwise.

## 9. Security Considerations
This document provides open source access to FIPS Secure Hash Algorithms, HMAC, and HKDF. No independent security assertion is made. See [RFC6194] for SHA-1 security considerations.

## 10. Acknowledgements
Thanks to Alfred Hoenes, Jan Andres, James Carlson, Russ Housley, Tero Kivinen, Juergen Quittek, and Sean Turner for corrections and improvements.

## Appendix: Changes from RFC 4634
- Added HKDF code and text.
- Fixed errata: corrected error return values, updated code to handle up to 2^128 bits for SHA-384/512, added run-time ASCII check.
- Updated boilerplate to simplified BSD license.
- Replaced MIT getopt with new code.
- Added references to [RFC6194].
- Various editorial improvements.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | Message padding for SHA-224/256 shall append a '1', then '0's to reach 448 mod 512, then 64-bit length. | shall | Section 4.1 |
| R2 | Message padding for SHA-384/512 shall append a '1', then '0's to reach 896 mod 1024, then 128-bit length. | shall | Section 4.2 |
| R3 | SHA-224 and SHA-256 use the same logical functions and constants on 32-bit words. | shall | Section 5.1 |
| R4 | SHA-384 and SHA-512 use the same logical functions and constants on 64-bit words. | shall | Section 5.2 |
| R5 | SHA-224 and SHA-256 use the same processing steps; differ only in initial hash and final truncation. | shall | Section 6.2 |
| R6 | SHA-384 and SHA-512 use the same processing steps; differ only in initial hash and final truncation. | shall | Section 6.4 |
| R7 | HMAC shall be computed as per [RFC2104] using any SHA algorithm. | shall | Section 7.1 |
| R8 | HKDF shall be computed as per [RFC5869] based on HMAC. | shall | Section 7.2 |
| R9 | The provided C code must be used only according to the Simplified BSD License. | may | Section 8, Copyright |

## Informative Annexes (Condensed)
- **Appendix: Changes from RFC 4634**: Summarizes corrections including error handling, bit length limits, code updates, and license changes. No normative effect.
- **ASN.1 OIDs**: Informative list of Object Identifiers for SHA algorithms from [RFC4055].
- **Code Listings (Sections 8.1–8.5)**: Provided as open source reference implementations. May be freely used per Simplified BSD License.