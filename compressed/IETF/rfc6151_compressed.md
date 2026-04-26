# RFC 6151: Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms
**Source**: IETF | **Version**: Informational | **Date**: March 2011 | **Type**: Informational
**Original**: https://www.rfc-editor.org/rfc/rfc6151

## Scope (Summary)
This document updates the security considerations for the MD5 message digest algorithm (RFC 1321) and for HMAC-MD5 (RFC 2104, RFC 2202). It summarizes known cryptographic attacks and provides guidance on the continued use of MD5 and HMAC-MD5.

## Normative References
None. All references are informative.

## Definitions and Abbreviations
- **MD5**: Message Digest Algorithm 5, producing a 128-bit hash.
- **HMAC**: Keyed-Hashing for Message Authentication.
- **HMAC-MD5**: HMAC using MD5 as the underlying hash function.
- **Collision resistance**: Property that it is computationally infeasible to find two distinct inputs that produce the same hash output.
- **Pre-image resistance**: Property that given a hash output, it is computationally infeasible to find any input that hashes to that output.
- **Second pre-image resistance**: Property that given an input and its hash, it is computationally infeasible to find a different input with the same hash.

## Security Considerations

### 1. Introduction
- MD5 was published in RFC 1321 (1992). Collision attacks have rendered MD5 unacceptable where collision resistance is required.
- HMAC security depends on the underlying hash function. This document updates [HMAC] and [HMAC-MD5] security considerations.
- **Requirement**: Applications and protocols **must** clearly state in their security considerations what security services (if any) are expected from the MD5 checksum. Any use of MD5 **must** clearly state expected security services.
- Where MD5 checksum is used solely for error detection (integrity against errors), it remains acceptable.

### 2. Security Considerations
- MD5 no longer acceptable where collision resistance is required (e.g., digital signatures).
- **Requirement**: MD5 **must not** be used for digital signatures.
- It is not urgent to stop using MD5 in other ways (e.g., HMAC-MD5), but new protocol designs **should not** employ HMAC-MD5.
- Alternatives: HMAC-SHA256 [HMAC][HMAC-SHA256] and [AES-CMAC] (when AES is more available than a hash).

#### 2.1. Collision Resistance
- Significant collision attacks demonstrated: from 2004 (Wang et al.) to 2007 (Stevens: collisions in 10 seconds on 2.6GHz Pentium4).
- Collision attacks applied to X.509 certificates (2007–2009).
- Collision attacks also applied to APOP (POP) authentication (Leurent, 2007).
- **Conclusion**: Sufficient reason to eliminate MD5 where collision resistance is required.

#### 2.2. Pre-Image and Second Pre-Image Resistance
- Best known pre-image attack (Sasaki & Aoki, 2009): complexity 2^123.4 (still high).
- No practical vulnerability from pre-image attacks.

#### 2.3. HMAC
- Attacks on HMAC-MD5: partial key recovery on NMAC-MD5 (related-key, not applicable to HMAC-MD5); distinguishing-H attack (2^97 queries, probability 0.87) does not recover inner key; forgery not demonstrated.
- **Guidance**: HMAC-MD5 may still be used in existing protocols; it is not urgent to remove.
- **Requirement**: For new protocol designs, ciphersuites with HMAC-MD5 **should not** be included. Alternatives as above.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Applications and protocols using MD5 **must** clearly state expected security services from MD5. | must | Section 1 |
| R2 | MD5 **must not** be used for digital signatures. | must | Section 2 |
| R3 | New protocol designs **should not** employ HMAC-MD5. | should | Section 2, 2.3 |
| R4 | New protocol designs **should not** include ciphersuites with HMAC-MD5. | should | Section 2.3 |
| R5 | Where MD5 checksum is used solely for error protection, it is still acceptable. | may (permissive) | Section 1 |

## Informative Annexes (Condensed)
All references are informative. Key documents cited for attack history and alternatives:
- [MD5]: RFC 1321 (original MD5 specification)
- [HMAC]: RFC 2104 (HMAC specification)
- [HMAC-MD5]: RFC 2202 (test cases for HMAC-MD5)
- [HMAC-SHA256]: RFC 4231 (identifiers and test vectors for HMAC-SHA-224/256/384/512)
- [AES-CMAC]: RFC 4493 (AES-CMAC algorithm)
- [HASH-Attack]: RFC 4270 (attacks on cryptographic hashes in Internet protocols)
- [SP800-57], [SP800-131]: NIST recommendations on key management and algorithm transitioning.
- Attack papers: [denBBO1993], [DOB1995], [WFLY2004], [WAYU2005], [KLIM2006], [STEV2007], [SLdeW2007], [SSALMOdeW2009], [SLdeW2009], [LEUR2007], [SAAO2009], [COYI2006], [FLN2007], [WYWZZ2009] – detailed in original RFC.