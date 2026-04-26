# RFC 3610: Counter with CBC-MAC (CCM)
**Source**: IETF (Network Working Group) | **Version**: Informational | **Date**: September 2003 | **Type**: Informative
**Original**: [https://datatracker.ietf.org/doc/rfc3610/](https://datatracker.ietf.org/doc/rfc3610/)

## Scope (Summary)
This document specifies Counter with CBC-MAC (CCM), a generic authenticated encryption block cipher mode for use with 128-bit block ciphers (e.g., AES). It defines authentication and encryption procedures, parameter choices, and security constraints.

## Normative References
- [STDWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **CCM**: Counter with CBC-MAC
- **AES**: Advanced Encryption Standard
- **M**: Size of authentication field (octets); valid: 4, 6, 8, 10, 12, 14, 16
- **L**: Size of length field (octets); valid: 2 to 8 (L=1 reserved)
- **Nonce N**: 15‑L octets; MUST be unique within scope of a given key
- **m**: message to authenticate and encrypt; length l(m) < 2^(8L) octets
- **a**: additional authenticated data; length l(a) < 2^64 octets
- **K**: block cipher key
- **T**: authentication field (MAC)
- **U**: encrypted authentication value
- **B_0, B_1, ..., B_n**: blocks for CBC-MAC
- **A_i**: counter blocks for encryption
- **S_i**: key stream blocks
- **Adata**: flag bit indicating presence of a
- **Flags**: first byte of B_0 and A_i

## 1. Introduction
CCM is a generic authenticated encryption block cipher mode defined for 128‑bit block ciphers only. Design principles can be applied to other block sizes but require separate specifications.

### 1.1. Conventions Used In This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [STDWORDS].

## 2. CCM Mode Specification
Two parameter choices: **M** (authentication field size) and **L** (length field size). Valid M: 4, 6, 8, 10, 12, 14, 16 octets. Valid L: 2 to 8 octets (L=1 reserved). Encoding:

| Name | Description | Size | Encoding |
|------|-------------|------|----------|
| M | Number of octets in authentication field | 3 bits | (M-2)/2 |
| L | Number of octets in length field | 3 bits | L-1 |

### 2.1. Inputs
Four inputs required:
1. Encryption key K (suitable for block cipher).
2. Nonce N of 15‑L octets. Within scope of any key K, the nonce value **MUST** be unique. Using the same nonce for two different messages encrypted with the same key destroys security.
3. Message m (string of l(m) octets, 0 ≤ l(m) < 2^(8L)).
4. Additional authenticated data a (string of l(a) octets, 0 ≤ l(a) < 2^64). Authenticated but not encrypted. May be zero length.

### 2.2. Authentication (CBC-MAC)
Compute authentication field T via CBC-MAC over blocks B_0, B_1, …, B_n.

**B_0 Format** (16 octets):
- Octets 0: Flags
- Octets 1..15‑L: Nonce N
- Octets 16‑L..15: l(m) (most‑significant‑byte first)

**Flags field in B_0**:
- Bit 7: Reserved (always zero)
- Bit 6: Adata (0 if l(a)=0, 1 otherwise)
- Bits 5..3: M' = (M-2)/2. Must not have value zero.
- Bits 2..0: L' = L-1 (zero reserved)

If l(a)>0, encode l(a) using one of three forms:
- 0 < l(a) < 2^16‑2^8: two octets encoding l(a)
- 2^16‑2^8 ≤ l(a) < 2^32: six octets (0xFF, 0xFE, four octets l(a))
- 2^32 ≤ l(a) < 2^64: ten octets (0xFF, 0xFF, eight octets l(a))

Then append a padded to 16‑octet blocks. Append message blocks (padded). Result is blocks B_0…B_n.

CBC-MAC computation:
```
X_1 := E(K, B_0)
X_i+1 := E(K, X_i XOR B_i)  for i = 1, …, n
T := first-M-bytes(X_n+1)
```

### 2.3. Encryption (CTR Mode)
Key stream blocks:
```
S_i := E(K, A_i)   for i = 0, 1, 2, …
```
**A_i Format**:
- Octets 0: Flags (bits 7,6 reserved, zero; bits 5..3 zero; bits 2..0 = L')
- Octets 1..15‑L: Nonce N
- Octets 16‑L..15: Counter i (most‑significant‑byte first)

Message encrypted by XORing with first l(m) octets of concatenation of S_1, S_2, S_3, … (S_0 not used for message).

Authentication value U: first‑M‑bytes of (T XOR S_0).

### 2.4. Output
c = encrypted message concatenated with U.

### 2.5. Decryption and Authentication Checking
Decryption requires K, N, a, c. Recompute key stream to recover m and T. Recompute CBC‑MAC and verify T. If T is not correct, the receiver **MUST NOT** reveal any information except that T is incorrect. The receiver **MUST NOT** reveal the decrypted message, T, or any other information.

### 2.6. Restrictions
- Total number of block cipher encryption operations in CBC‑MAC and encryption together **MUST NOT** exceed 2^61 per key (≈16 million TB). The sender **MUST** ensure this limit. Receivers that do not expect to decrypt the same message twice **MAY** check this limit.
- The recipient **MUST** verify the CBC‑MAC before releasing any information such as plaintext. If verification fails, the receiver **MUST** destroy all information except that verification failed.

## 3. Security Proof (Informative)
Jakob Jonsson developed a security proof of CCM [PROOF] presented at SAC 2002. The proof shows CCM provides confidentiality and authenticity in line with OCB mode.

## 4. Rationale (Condensed)
The L parameter balances nonce size and maximum message size. M trades message expansion against forgery probability (M≥8 recommended). CBC‑MAC blocks encode all inputs uniquely. CTR encryption is straightforward; encrypting T prevents CBC‑MAC collision attacks. Using the same key for both functions is safe because all A_i blocks differ from B_0 and from each other. Hardware implementation is simplified by aligning authentication and encryption blocks.

## 5. Nonce Suggestions (Condensed)
Nonces must be unique per key. Sequential message numbers are common. To mitigate precomputation attacks (effective against 128‑bit keys), use a larger key (e.g., 256‑bit) or include random bytes / Ethernet address in the nonce.

## 6. Efficiency and Performance (Condensed)
Performance depends on block cipher speed. For large packets, CCM speed is roughly equal to CBC encryption. Empty message with no additional authenticated data requires 2 block cipher operations. Each block of additional authenticated data adds 1 operation; each message block adds 2. CCM achieves minimal message expansion (only authentication bits). Encryption and decryption use only the block cipher encryption function (saves code/hardware size). In hardware, CCM can compute MAC and encryption in a single pass, but requires message length known in advance.

## 7. Summary of Properties (Condensed)
- Security Function: authenticated encryption
- Error Propagation: none
- Synchronization: same nonce used by sender and receiver
- Parallelizability: encryption parallelizable, authentication not
- Keying Material: one key
- Counter/IV/Nonce: counter and nonce part of counter block
- Memory: requires block cipher state, plaintext, ciphertext (expanded), per‑packet counter (≤ L octets)
- Pre‑processing: key stream can be precomputed, authentication cannot
- Message Length: octet‑aligned, up to 2^(8L) octets; additional authenticated data up to 2^64 octets
- Ciphertext Expansion: 4, 6, 8, 10, 12, 14, or 16 octets (depending on M)

## 8. Test Vectors (Summary)
24 test vectors using AES‑128 with 13‑octet nonce and M either 8 or 10 octets. Each vector includes key, nonce, input (header + message), CBC‑MAC intermediate steps, CTR blocks, and final authenticated ciphertext. Provided as reference for implementations.

## 10. Security Considerations
- CCM is secure against attackers limited to 2^128 steps if key K is ≥ 256 bits. Generic precomputation attacks limit theoretical strength to 2^(n/2) for n‑bit keys.
- Smaller key sizes (e.g., 128 bits) require precautions (e.g., random nonce components) to hinder precomputation.
- Authentication strength limited by M.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | Within the scope of any encryption key K, the nonce value MUST be unique. | MUST | Section 2.1 (Inputs) |
| R2 | The receiver MUST NOT reveal any information except the fact that T is incorrect when T verification fails. | MUST | Section 2.5 |
| R3 | The receiver MUST NOT reveal the decrypted message, the value T, or any other information upon T verification failure. | MUST | Section 2.5 |
| R4 | The sender MUST ensure that total block cipher encryption operations (CBC‑MAC + encryption) do not exceed 2^61 per key. | MUST | Section 2.6 |
| R5 | Recipients that do not expect to decrypt the same message twice MAY check the 2^61 operation limit. | MAY | Section 2.6 |
| R6 | The recipient MUST verify the CBC‑MAC before releasing any information such as the plaintext. | MUST | Section 2.6 |
| R7 | If CBC‑MAC verification fails, the receiver MUST destroy all information except that verification failed. | MUST | Section 2.6 |
| R8 | The M' field (3 bits) MUST NOT have a value of zero. | MUST | Section 2.2 (Flags) |
| R9 | The Reserved bits in the Flags fields (B_0 and A_i) MUST be set to zero. | MUST | Sections 2.2, 2.3 |

## Informative Annexes (Condensed)
- **Annex 9. Intellectual Property Statements**: Authors release any IP rights to CCM to the public domain; no known patents cover CCM.
- **Annex 11. References**: Lists normative (RFC 2119) and informative (AES, ESP, MAC, MODES, OCB, PROOF, earlier CCM paper) references.
- **Annex 12. Acknowledgement**: Thanks to RSA Laboratories for supporting development.
- **Annex 14. Full Copyright Statement**: Standard IETF copyright and disclaimer notice.