# RFC 3218: Preventing the Million Message Attack on Cryptographic Message Syntax
**Source**: IETF | **Version**: Informational | **Date**: January 2002 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc3218

## Scope (Summary)
This document describes countermeasures to resist the Million Message Attack (MMA) against PKCS-1 v1.5 encryption as used in CMS, focusing on automated servers (e.g., mail list agents). It recommends careful error checking, random filling of invalid CEKs, and notes OAEP as a future upgrade path.

## Normative References
- [CMS] Housley, R., "Cryptographic Message Syntax", RFC 2630, June 1999.
- [MMA] Bleichenbacher, D., "Chosen Ciphertext Attacks against Protocols based on RSA Encryption Standard PKCS #1", Advances in Cryptology – CRYPTO 98.
- [MMAUPDATE] D. Bleichenbacher, B. Kaliski, and J. Staddon, "Recent Results on PKCS #1: RSA Encryption Standard", RSA Laboratories' Bulletin #7, June 26, 1998.
- [OAEP] Bellare, M., Rogaway, P., "Optimal Asymmetric Encryption Padding", Advances in Cryptology – Eurocrypt 94.
- [PKCS-1-v1.5] Kaliski, B., "PKCS #1: RSA Encryption, Version 1.5.", RFC 2313, March 1998.
- [PKCS-1-v2] Kaliski, B., "PKCS #1: RSA Encryption, Version 2.0", RFC 2347, October 1998.

## Definitions and Abbreviations
- **CEK**: Content-encryption key, a symmetric key wrapped inside the RSA-encrypted block.
- **MMA**: Million Message Attack, an adaptive chosen ciphertext attack against PKCS-1 padding.
- **OAEP**: Optimal Asymmetric Encryption Padding, an alternative padding scheme immune to MMA.
- **PKCS-1**: Public-Key Cryptography Standard #1, describes RSA encryption padding (v1.5 and v2).
- **Oracle**: A program that answers queries using secret information (here, the private key).

## 1. Introduction
- When RSA encrypting a CEK in CMS, the data must be padded to the modulus length (512–2048 bits) using PKCS-1 v1.5.
- The MMA (described in [MMA]) recovers a single plaintext ciphertext block by submitting many transformed ciphertexts to an oracle and observing whether the decrypted block appears PKCS-1 formatted.
- The attack requires an automated victim willing to process millions of messages; mail list agents are the most likely CMS targets.

## 2. Overview of PKCS-1
- RSA encryption maps a message (e.g., CEK) into an integer less than the modulus.
- The encryption block (same length as modulus) consists of:  
  `[0 | 2 | non-zero random bytes | 0 | message]`
- The first two bytes are 0x00 and 0x02 (block type for encryption). Padding bytes are non-zero random; a zero byte separates padding from message.
- The block is converted to an integer in big-endian form.
- In CMS, the message is a random CEK of 8–32 bytes.
- At least 8 bytes of non-zero padding are required; this prevents verification of message guesses.

### 2.1. The Million Message Attack
- Attacker captures ciphertext C, then computes C' = C*(S^e) mod n for chosen integers S.
- Upon decryption, C' yields M'. If M' starts with 0x00 0x02, it appears PKCS-1 formatted.
- The attacker uses the oracle’s response (error or success) to narrow possible values of M.
- Typically requires about 2^20 messages.

### 2.2. Applicability
- MMA requires an automated victim (no human reads millions of messages).
- The attacker must distinguish between:
  1. M' improperly formatted.
  2. M' properly formatted but CEK invalid (wrong length, etc.).
  3. M' properly formatted, CEK appears OK but integrity check fails.
  4. M' properly formatted, no integrity check and CBC padding by chance verifies (≈1/32 probability).
  5. M' properly formatted with correct CEK (extremely improbable).
- If the victim returns different errors for each case, the attack is possible. Timing differences may also reveal the case.

#### 2.2.1. Note on Block Cipher Padding
- [CMS] specifies padding with bytes containing the padding length (e.g., three bytes of 0x03 for a 5‑byte block).
- Implementation behavior affects attack: simple truncation yields ~1/32 false positive rate; full verification yields ~1/255.

### 2.3. Countermeasures

#### 2.3.1. Careful Checking
- **[Recommendation]**: Check CEK length and parity bits (if available), and **respond identically** to all errors.
- This increases the workfactor but does not eliminate the attack entirely; however, combining padding, length, and parity checking makes the attack impractical.

#### 2.3.2. Random Filling
- **[Recommendation]**: When an improperly formatted message is detected, the victim **should substitute a randomly generated CEK** (cryptographically random) and continue processing.
- This prevents the attacker from distinguishing failure cases via error messages or timing (random generation is negligible time).
- **[Recommendation]**: If the PKCS-1 check occurs at a layer where CEK length is unknown, also randomize CEKs that are wrong length or otherwise invalid when processed at the upper layer.
- **[Critical Warning]**: Do **not** use a fixed CEK; the attacker could encrypt a CMS message with that fixed key and detect that formatting was bad.

#### 2.3.3. OAEP
- OAEP (see [OAEP], [PKCS-1-v2]) is immune to MMA but incompatible with PKCS-1 v1.5.
- **[Statement]**: "Implementations of S/MIME and CMS must therefore continue to use PKCS-1 for the foreseeable future if they wish to communicate with current widely deployed implementations."
- OAEP is being specified for use with AES keys in CMS, providing an upgrade path.

### 2.4. Security Considerations
- The entire document addresses avoiding the MMA when performing PKCS-1 decryption with RSA.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | When an improperly formatted PKCS-1 block is detected, substitute a randomly generated CEK (cryptographically random) of appropriate length and continue processing. | should | Section 2.3.2 |
| R2 | If PKCS-1 check occurs before CEK length is known, also randomize CEKs that are wrong length or improperly formatted when processed at the layer that knows the length. | should | Section 2.3.2 |
| R3 | Do not use a fixed CEK as a substitute; use a cryptographically random one. | must-not (mistake) | Section 2.3.2 |
| R4 | Respond identically to all failure cases (misformatted, wrong length, integrity failure) to prevent timing/error differentiation. | should | Section 2.3.1 |
| R5 | Use OAEP when possible (future upgrade path) to achieve immunity to MMA. | informative | Section 2.3.3 |

## Informative Annexes (Condensed)
- **Note on Block Cipher Padding (2.2.1)**: Explains that if the receiver only truncates based on the final padding byte, false positive probability is ~1/32; if all bytes are verified, probability is ~1/255. This affects the attacker’s ability to distinguish cases.