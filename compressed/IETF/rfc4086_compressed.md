# RFC 4086: Randomness Requirements for Security
**Source**: IETF (Internet Engineering Task Force) | **Version**: BCP 106 | **Date**: June 2005 | **Type**: Best Current Practice (Normative)
**Original**: https://datatracker.ietf.org/doc/html/rfc4086

## Scope (Summary)
This document provides guidance for generating unpredictable secret quantities (passwords, cryptographic keys, etc.) for security applications. It emphasizes the need for entropy from physical sources, describes de-skewing and mixing techniques to improve randomness, and recommends cryptographically strong pseudo-random number generators for extending seed material.

## Normative References
- [AES]: "Specification of the Advanced Encryption Standard (AES)", FIPS 197, November 2001.
- [DES]: "Data Encryption Standard", FIPS 46-3, October 1999.
- [SHA*]: "Secure Hash Standard", FIPS 180-2, August 2002.
- [MD4]: Rivest, R., "The MD4 Message-Digest Algorithm", RFC 1320, April 1992.
- [MD5]: Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [DSS]: "Digital Signature Standard (DSS)", FIPS 186-2, January 2000.
- [X9.82]: "Random Number Generation", ANSI X9F1, Work in Progress.
- [RFC2104]: Krawczyk et al., "HMAC: Keyed-Hashing for Message Authentication", February 1997.

## Definitions and Abbreviations
- **Entropy**: Measure of unpredictability (in bits); Shannon entropy or min-entropy are used. Min-entropy = -log₂(max pᵢ).
- **De-skewing**: Techniques to remove bias or correlation from a bit stream (e.g., parity, von Neumann mapping, compression).
- **Mixing function**: Algorithm that combines inputs to produce output where each bit depends on all inputs (e.g., AES, SHA, HMAC).
- **Pseudo-random number generator (PRNG)**: Algorithm to extend a seed with sufficient entropy into a longer unpredictable sequence.
- **Cryptographically strong sequence**: PRNG where future values cannot be predicted from past values.
- **Seed**: Initial secret value with sufficient entropy used to initialize a PRNG.
- **Min-entropy**: Most conservative entropy measure; -log₂(max probability of any value).
- **Renyi entropy**: Continuous spectrum of entropies; r=1 is Shannon, r=∞ is min-entropy.

## General Requirements
- **Section 2**: Secret quantities must be unguessable by an adversary. The amount of uncertainty (information) determines the search space.
- **R1 (shall)**: The probability of an adversary guessing a secret must be acceptably low, based on application.
- **R2 (should)**: Use min-entropy (most conservative) for cryptographic evaluation.
- **R3 (shall not)**: Statistical randomness tests are NOT sufficient for security; predictability matters more than distribution.
- **R4 (should)**: Avoid using constant sequences or predictable sources (e.g., clocks, serial numbers) without careful mixing.

## Entropy Sources
### 3.1 Volume Required
- **R5 (should)**: A few hundred bits of seed material (e.g., 200 bits) is enough for most high-security systems; can be generated slowly.
### 3.2 Existing Hardware Can Be Used For Randomness
- **R6 (may)**: Sound/video input, disk drive timing, ring oscillators, or noisy diodes provide entropy.
- **R7 (should)**: When using sound/video, combine with compression for de-skewing; verify against hardware failure.
- **R8 (should)**: Disk seek-time jitter can produce >10,000 bits/second; ignore cache hits.
### 3.3 Ring Oscillator Sources
- **R9 (should)**: Use odd number of rings to avoid synchronous locking; XOR outputs; de-skew heavily.
- **R10 (should)**: Isolate rings from each other and from clocked circuits.
### 3.4 Problems with Clocks and Serial Numbers
- **R11 (should not)**: Do not rely solely on system clocks or serial numbers; they provide far fewer bits of unpredictability than expected.
### 3.5 Timing and Value of External Events
- **R12 (may)**: Measure mouse movement, keystrokes, network packet timings; but consider adversarial manipulation and buffering.
### 3.6 Non-hardware Sources of Randomness
- **R13 (should)**: Use multiple uncorrelated inputs with a strong mixing function to overcome weakness in any single source.
- **R14 (should)**: Conservative estimates: inter-keystroke intervals or key codes provide at most a few bits only when unique.

## De-skewing
### 4.1 Using Stream Parity to De-Skew
- **R15 (may)**: Parity of N bits can approach uniform distribution; N > log(2d)/log(2E) for given skew E and tolerance d.
### 4.2 Using Transition Mappings to De-Skew (von Neumann)
- **R16 (should)**: Examine non-overlapping pairs; discard 00/11, map 01→0, 10→1. Removes bias but requires more input bits.
### 4.3 Using FFT to De-Skew
- **R17 (may)**: Fourier transform can discard strong correlations; theoretically sound.
### 4.4 Using Compression to De-Skew
- **R18 (should-not)**: Only a rough method; skip beginning of compressed output due to predictable headers.

## Mixing
### 5.1 A Trivial Mixing Function (XOR)
- **R19 (should-not)**: XOR only improves eccentricity if inputs are uncorrelated; correlated inputs (e.g., two clocks) can produce zero output.
### 5.2 Stronger Mixing Functions
- **R20 (should)**: Use cryptographically strong functions like AES, SHA-1/2, HMAC to combine inputs.
- **R21 (should)**: When using AES for mixing, use full feedback (OFB/CBC-MAC) rather than partial feedback to avoid cycle reduction.
- **R22 (should)**: Use hash functions for variable-length input; block ciphers need padding.
### 5.3 Using S-Boxes for Mixing
- **R23 (may)**: S-boxes with bent functions can concentrate entropy.
### 5.4 Diffie-Hellman as a Mixing Function
- **R24 (should-not)**: Not recommended due to computational cost and potential exposure of one party's secret.
### 5.5 Using a Mixing Function to Stretch Random Bits
- **R25 (shall)**: Cannot stretch entropy; output entropy ≤ input entropy. Additional bits from mixing with constants add no new unpredictability.
### 5.6 Other Factors in Choosing a Mixing Function
- **R26 (should)**: Prefer AES or SHA*; MD4 and MD5 have known weaknesses (collisions).

## Pseudo-random Number Generators
### 6.1 Some Bad Ideas
- **R27 (shall not)**: Do not rely on complex manipulation of limited seed (e.g., system clock alone).
- **R28 (shall not)**: Do not select from public databases (e.g., Usenet, CD-ROMs) – adversary can reproduce selection.
- **R29 (shall not)**: Do not use traditional PRNGs (linear congruential, shift register) for security; they are predictable.
### 6.2 Cryptographically Strong Sequences
- **R30 (should)**: Use OFB/CTR mode with a secure block cipher or hash-based sequence; do not reveal full generator state.
- **R31 (should)**: Use only a few bits per iteration (e.g., low-order bits) to make prediction harder.
- **R32 (may)**: Consider Blum Blum Shub generator; provably secure assuming factoring is hard. Use only low-order log₂(log₂(s_i)) bits.
### 6.3 Entropy Pool Techniques
- **R33 (should)**: Maintain a pool with strong mixing (e.g., hash) and estimate entropy; save/restore pool across reboots.
- **R34 (should)**: Debit entropy estimate as bits are extracted.

## Randomness Generation Examples and Standards
### 7.1 Complete Randomness Generators
- **7.1.1 US DoD Password Generation**: Use DES in OFB mode with inputs from system clock, IDs, interrupts, counters, and random typed characters.
- **7.1.2 /dev/random Device**: Kernel pool stirred via polynomial; input from keyboard, disk, mouse; output via SHA-1 hash; /dev/random blocks when entropy low; /dev/urandom does not block (risk: invertible hash).
- **7.1.3 Windows CryptGenRandom**: Uses SHA-1 to combine seed with system data, then RC4 stream; updates seed state.
### 7.2 Generators Assuming a Source of Entropy
- **7.2.1 X9.82 Pseudo-Random Number Generation**: HMAC-based generator; state K and V; initialization with entropy; generate bits by HMAC(K,V), update K and V after extraction. (Prohibits >2^35 bits per request.)
- **7.2.2 X9.17 Key Generation**: Uses DES with secret key k, seed s₀, and time t; produces 64-bit keys gₙ via double encryption.
- **7.2.3 DSS Pseudo-random Number Generation**: FIPS 186-2+ Change Notice 1; uses SHA-1 or DES to produce 160-bit values from 512-bit XKEY.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Probability of guessing secret must be acceptably low. | shall | Section 2 |
| R2 | Use min-entropy for cryptographic evaluation. | should | Section 2 |
| R3 | Statistical tests alone are insufficient for security. | shall not | Section 2 |
| R4 | Avoid constant or predictable sequences. | should | Section 2 |
| R5 | A few hundred bits of seed material is sufficient. | should | Section 3.1 |
| R6 | Existing hardware (sound, disk, ring oscillators) may be used. | may | Section 3.2, 3.3 |
| R7 | Combine sound/video with compression; check for failures. | should | Section 3.2.1 |
| R8 | Disk seek-time jitter can be used; ignore cache hits. | should | Section 3.2.2 |
| R9 | Use odd number of ring oscillators; isolate from clocks. | should | Section 3.3 |
| R10 | De-skew ring oscillator outputs heavily. | should | Section 3.3 |
| R11 | Do not rely solely on clocks or serial numbers. | should not | Section 3.4 |
| R12 | External events may be used; consider manipulation and buffering. | may | Section 3.5 |
| R13 | Use multiple uncorrelated inputs with strong mixing. | should | Section 3.6 |
| R14 | Conservative estimates for keystroke intervals: few bits only when unique. | should | Section 3.6 |
| R15 | Parity de-skew can approach uniformity with enough bits. | may | Section 4.1 |
| R16 | Use von Neumann mapping for bias removal (non-overlapping pairs). | should | Section 4.2 |
| R17 | FFT de-skew may be used. | may | Section 4.3 |
| R18 | Compression de-skew is rough; skip beginning of output. | should not | Section 4.4 |
| R19 | XOR mixing only effective if inputs uncorrelated. | should not | Section 5.1 |
| R20 | Use strong mixing functions (AES, SHA, HMAC). | should | Section 5.2 |
| R21 | Use full feedback (not partial) with block ciphers. | should | Section 5.2 |
| R22 | Use hash functions for variable-length input. | should | Section 5.2 |
| R23 | S-boxes may be used for mixing. | may | Section 5.3 |
| R24 | Diffie-Hellman not recommended as mixing function. | should not | Section 5.4 |
| R25 | Cannot stretch entropy; output randomness ≤ input randomness. | shall | Section 5.5 |
| R26 | Prefer AES or SHA*; MD4/MD5 have known weaknesses. | should | Section 5.6 |
| R27 | Do not rely on complex manipulation of limited seed. | shall not | Section 6.1.1 |
| R28 | Do not select from public databases. | shall not | Section 6.1.2 |
| R29 | Do not use traditional PRNGs for security. | shall not | Section 6.1.3 |
| R30 | Use cryptographically strong sequences (OFB, CTR, HMAC). | should | Section 6.2 |
| R31 | Reveal only a few bits per iteration. | should | Section 6.2 |
| R32 | Blum Blum Shub may be used; use only low-order bits. | may | Section 6.2.2 |
| R33 | Maintain entropy pool with strong mixing; save/restore. | should | Section 6.3 |
| R34 | Debit entropy estimate when extracting bits. | should | Section 6.3 |
| R35 | Use DoD method for password generation (DES OFB with multiple inputs). | may | Section 7.1.1 |
| R36 | Use /dev/random for long-term keys; /dev/urandom for session keys when blocking is unacceptable. | should | Section 7.1.2 |
| R37 | Use Windows CryptGenRandom with appropriate API. | may | Section 7.1.3 |
| R38 | Use X9.82 HMAC-based generator (draft). | should | Section 7.2.1 |
| R39 | Use X9.17 key generation for DES keys. | may | Section 7.2.2 |
| R40 | Use DSS pseudo-random generator (FIPS 186-2+CN1). | may | Section 7.2.3 |

## Informative Annexes (Condensed)
- **Appendix A: Changes from RFC 1750**: Added ring oscillator sources, AES/SHA emphasis, entropy pool techniques, /dev/random, CryptGenRandom, X9.82, min-entropy discussion, and extensive restructuring.
- **Examples of Randomness Required (Section 8)**: Password generation: 29 bits of entropy for 1:1000 guess probability in a year under reasonable attack rates; very high-security symmetric key: minimum 90-96 bits (2004), with meet-in-the-middle attack doubling to 192 bits. Key length recommendations from [KeyStudy] and [ORMAN].
- **Security Considerations (Section 10)**: The entire document addresses generation of unguessable quantities for security.