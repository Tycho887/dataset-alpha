# RFC 7539: ChaCha20 and Poly1305 for IETF Protocols
**Source**: IRTF (Crypto Forum Research Group) | **Version**: Informational | **Date**: May 2015 | **Type**: Informative
**Original**: http://www.rfc-editor.org/info/rfc7539

## Scope (Summary)
Defines the ChaCha20 stream cipher, the Poly1305 authenticator, and their composition as an AEAD algorithm (AEAD_CHACHA20_POLY1305), serving as a stable reference for IETF protocols. Does not introduce new crypto; reflects CFRG consensus.

## Normative References
- [ChaCha] Bernstein, D., "ChaCha, a variant of Salsa20", January 2008
- [Poly1305] Bernstein, D., "The Poly1305-AES message-authentication code", March 2005
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997

## Definitions and Abbreviations
- **ChaCha20**: 20-round variant of the ChaCha stream cipher, using 256-bit key.
- **Poly1305**: One-time authenticator producing a 16-byte tag, using a 256-bit one-time key.
- **AEAD**: Authenticated Encryption with Associated Data.
- **Quarter Round (QR)**: Basic operation on four 32-bit words involving addition, XOR, and rotation.
- **Clamping**: Modification of the Poly1305 key 'r' by clearing certain bits.
- **PRF**: Pseudorandom Function.
- **AAD**: Additional Authenticated Data.

## 1. Introduction
- Purpose: Provide stable reference for ChaCha20 and Poly1305 in IETF protocols.
- ChaCha20 is faster than AES in software-only implementations (~3x on platforms without AES hardware) and not sensitive to timing attacks (see Section 4).
- Poly1305 is a high-speed MAC; straightforward implementation.
- AEAD_CHACHA20_POLY1305 combines both as an AEAD algorithm (Section 2.8).
- These algorithms have undergone rigorous analysis (referenced papers).

### 1.1. Conventions Used in This Document
- **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are interpreted as described in [RFC2119].
- The ChaCha state is described as a 4x4 matrix of 32-bit words.
- "ChaCha20" and "ChaCha" are used interchangeably (20 rounds).

## 2. The Algorithms
### 2.1. The ChaCha Quarter Round
- Quarter Round (QR) operates on four 32-bit unsigned integers a,b,c,d:
  1. a += b; d ^= a; d <<<= 16;
  2. c += d; b ^= c; b <<<= 12;
  3. a += b; d ^= a; d <<<= 8;
  4. c += d; b ^= c; b <<<= 7;
  - "+": addition modulo 2^32; "^": XOR; "<<< n": left rotation by n bits.

#### 2.1.1. Test Vector for the ChaCha Quarter Round
- Input: a=0x11111111, b=0x01020304, c=0x9b8d6f43, d=0x01234567
- Output: a=0xea2a92f4, b=0xcb1cf8ce, c=0x4581472e, d=0x5881c4bb

### 2.2. A Quarter Round on the ChaCha State
- QR indices: QUARTERROUND(x,y,z,w) operates on the state vector at those positions.
- Example: QUARTERROUND(2,7,8,13) (part of diagonal round).

#### 2.2.1. Test Vector for Quarter Round on State
- Input state provided; after QR(2,7,8,13) only positions 2,7,8,13 change.

### 2.3. The ChaCha20 Block Function
- Inputs: 256-bit key (8 little-endian 32-bit words), 96-bit nonce (3 words), 32-bit block counter.
- Output: 64 bytes.
- State initialization: constants (0x61707865, 0x3320646e, 0x79622d32, 0x6b206574), key (words 4-11), block count (word 12), nonce (words 13-15).
- 20 rounds alternating column and diagonal rounds; each round = 4 quarter rounds.
- After rounds, add original input words, serialize in little-endian order.

#### 2.3.1. Pseudocode
- `inner_block(state)`: performs 8 quarter rounds.
- `chacha20_block(key, counter, nonce)`: initializes state, runs 10 iterations of inner_block, adds initial state, returns serialized result.

#### 2.3.2. Test Vector
- Provided: key, nonce, block count=1, resulting keystream block.

### 2.4. The ChaCha20 Encryption Algorithm
- Stream cipher: calls block function incrementally with same key and nonce, XORs keystream with plaintext.
- Inputs: 256-bit key, 32-bit initial counter, 96-bit nonce, arbitrary-length plaintext.
- Output: ciphertext of same length.
- Decryption: same process XOR ciphertext with keystream.
- Specific protocols MAY require padding.

#### 2.4.1. Pseudocode
- `chacha20_encrypt(key, counter, nonce, plaintext)`: loops over 64-byte blocks, XORs with keystream; handles partial final block.

#### 2.4.2. Example and Test Vector
- Provided: key, nonce, counter=1, plaintext "Sunscreen...", resulting ciphertext.

### 2.5. The Poly1305 Algorithm
- One-time authenticator: takes 32-byte one-time key and message, produces 16-byte tag.
- Key partitioned into r (16 bytes) and s (16 bytes). r must be clamped:
  - r[3], r[7], r[11], r[15] top four bits clear (<16)
  - r[4], r[8], r[12] bottom two bits clear (divisible by 4)
- Clamping code provided.
- Algorithm: message divided into 16-byte blocks (last may be shorter). For each block: read as little-endian, add 2^(8*block_len) (i.e., append 0x01), add to accumulator, multiply by r, reduce modulo prime P = 2^130-5. Finally add s, serialize 128 bits.

#### 2.5.1. Pseudocode
- `clamp(r)`
- `poly1305_mac(msg, key)`: uses r, s; accumulator modulo p.

#### 2.5.2. Example and Test Vector
- Provided: key material, message "Cryptographic Forum Research Group", resulting tag.

### 2.6. Generating the Poly1305 Key Using ChaCha20
- One-time key generated pseudorandomly using ChaCha20 block function with session integrity key.
- Parameters: key=256-bit MAC key, block counter=0, nonce unique per invocation (MAY be 96-bit; if 64-bit, first 32 bits set to constant, e.g., 0).
- After chacha20_block, take first 256 bits of serialized state: first 128 bits form r (clamped), next 128 bits s.
- Protocols that specify Poly1305 as standalone MAC MUST allocate 256-bit integrity key.

#### 2.6.1. Pseudocode
- `poly1305_key_gen(key, nonce)`: returns first 32 bytes of block.

#### 2.6.2. Test Vector
- Provided: key, nonce, resulting 32-byte one-time key.

### 2.7. A Pseudorandom Function for Crypto Suites based on ChaCha/Poly1305
- Poly1305 is NOT suitable as PRF (key reuse prohibited, biased).
- ChaCha20 keystream could be used but not compliant with IKEv2 requirements.
- This document does not specify a PRF; recommends using PRF_HMAC_SHA2_256 (see [RFC4868]).

### 2.8. AEAD Construction
- AEAD_CHACHA20_POLY1305: uses 256-bit key, 96-bit nonce, arbitrary-length plaintext and AAD.
- Process:
  1. Generate Poly1305 one-time key using ChaCha20 with key and nonce (Section 2.6).
  2. Encrypt plaintext using ChaCha20 (key, nonce, initial counter=1).
  3. Authenticate concatenation: AAD | pad16(AAD) | ciphertext | pad16(ciphertext) | 64-bit AAD length | 64-bit ciphertext length.
  - Output: ciphertext (same length as plaintext) and 128-bit tag.
- Decryption: apply ChaCha20 encryption to ciphertext (produces plaintext), compute tag over AAD and ciphertext, compare tags (MUST use constant-time comparison).
- Maximum plaintext size: ~256 GB (due to 32-bit block counter). Ciphertext length field limits to 2^64 bytes.
- Parameters per RFC 5116: K_LEN=32, P_MAX≈256 GB, A_MAX=2^64-1, N_MIN=N_MAX=12, C_MAX=P_MAX+16.

#### 2.8.1. Pseudocode
- `chacha20_aead_encrypt(aad, key, iv, constant, plaintext)`: constructs nonce, generates key, encrypts, builds mac_data, returns tag.

#### 2.8.2. Example and Test Vector
- Provided: plaintext, AAD, key, IV, constant, resulting ciphertext and tag.

## 3. Implementation Advice
- For ChaCha20 block function, copy state before rounds to avoid recreating each block (saves ~5.5% cycles).
- For Poly1305, do not use generic big number library; use constant-time implementations (e.g., NaCl, poly1305-donna).

## 4. Security Considerations
- ChaCha20 provides 256-bit security.
- Poly1305 provides SUF-CMA with forgery probability ~1-(n/2^102) per 16n-byte message after 2^64 legitimate messages.
- **Nonce uniqueness is critical**: repeating nonce reveals XOR of plaintexts. Counters or LFSRs acceptable; encrypting a counter with a 64-bit cipher is acceptable, but truncation of 128/256-bit cipher may repeat.
- Poly1305 key MUST be unpredictable to attackers. Pseudorandom generation (e.g., ChaCha20) is acceptable.
- Implement ChaCha20 in constant time (additions, XORs, rotations) to avoid side-channel. Poly1305 must also be constant-time; naive big-number arithmetic may leak timing.
- Tag comparison MUST use constant-time function (e.g., not memcmp).

## 5. IANA Considerations
- IANA assigned numeric ID 29 in AEAD Parameters registry for "AEAD_CHACHA20_POLY1305", referencing this document.

## 6. References
### 6.1. Normative References
- [ChaCha] (see above)
- [Poly1305] (see above)
- [RFC2119] (see above)

### 6.2. Informative References
- [AE] Bellare & Namprempre, 2008
- [Cache-Collisions] Bonneau & Mironov, 2006
- [FIPS-197] NIST, 2001
- [LatinDances] Aumasson et al., 2007
- [LatinDances2] Ishiguro et al., 2012
- [NaCl] Bernstein et al., 2012
- [Poly1305_Donna] Floodyberry, 2014
- [Procter] Procter, 2014
- [RFC4868] Kelly & Frankel, 2007
- [RFC5116] McGrew, 2008
- [RFC7296] Kaufman et al., 2014
- [SP800-67] NIST, 2012
- [Standby-Cipher] McGrew et al., 2013 (Work in Progress)
- [Zhenqing2012] Zhenqing et al., 2012

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Poly1305 key 'r' MUST be clamped before use: clear top four bits of indices 3,7,11,15 and bottom two bits of indices 4,8,12. | must | Section 2.5 |
| R2 | Poly1305 key 's' MUST be unpredictable (e.g., pseudorandomly generated). | must | Security Considerations |
| R3 | Nonce for ChaCha20/Poly1305 MUST be unique per invocation with the same key; reuse violates security. | must | Security Considerations |
| R4 | For AEAD decryption, tag comparison MUST be constant-time to prevent timing attacks. | must | Security Considerations |
| R5 | ChaCha20 implementation SHOULD be constant-time (additions, XORs, rotations) to avoid side-channel leakage. | should | Section 4 |
| R6 | Poly1305 arithmetic SHOULD be implemented in constant time (use specialized libraries like NaCl or poly1305-donna). | should | Section 3, Section 4 |
| R7 | When generating Poly1305 key using ChaCha20, the nonce MUST be unique per invocation; a counter is a good method. | must | Section 2.6 |
| R8 | For IETF protocols using standalone Poly1305, 256 bits MUST be allocated for the integrity key. | must | Section 2.6 |
| R9 | Protocols with non-96-bit nonces MUST define transformation to 96-bit nonce for AEAD. | must | Section 2.8 |
| R10 | The AEAD plaintext maximum size is limited to 2^32-1 blocks (≈256 GB) due to block counter field. | informative | Section 2.8 |

## Informative Annexes (Condensed)
- **Appendix A – Additional Test Vectors**: Provides multiple test vectors for ChaCha20 block function, encryption, Poly1305 MAC (including edge cases with zero r, overflow, partial reduction), Poly1305 key generation, and AEAD decryption example. These are for verification of implementations.
- **Appendix B – Performance Measurements**: Shows ChaCha20-Poly1305 is ~3x faster than AES-128-GCM on ARM chips (e.g., OMAP 4460: 75.3 MB/s vs 24.1 MB/s), but slower on x86 with AES-NI (~500 MB/s vs 900 MB/s). Table provided.
- **Acknowledgements**: Credits to Daniel J. Bernstein (inventor), Adam Langley (AEAD design), and many reviewers including Robert Ransom, Watson Ladd, Niels Moller (for efficient AEAD), Ilari Liusvaara (test vectors), Gordon Procter (security analysis).