# RFC 2631: Diffie-Hellman Key Agreement Method
**Source**: IETF Network Working Group | **Version**: Standards Track, June 1999 | **Date**: June 1999 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc2631

## Scope (Summary)
This document standardizes a Diffie-Hellman key agreement method based on ANSI X9.42, enabling two parties to compute a shared secret (ZZ) and convert it into symmetric keying material. The recipient must have a certificate; the originator may use a static or ephemeral key pair.

## Normative References
- [RFC2119]: "Key words for use in RFCs to Indicate Requirement Levels"
- [CMS]: RFC 2630 – Cryptographic Message Syntax
- [FIPS-180]: Secure Hash Standard (SHA-1)
- [FIPS-186]: Digital Signature Standard
- [X942]: ANSI draft – Agreement Of Symmetric Keys Using Diffie-Hellman and MQV Algorithms

## Definitions and Abbreviations
- **ZZ**: Shared secret number computed as `g^(xa * xb) mod p`.
- **p**: Large prime, p = qj + 1.
- **q**: Large prime divisor of p-1, at least 160 bits.
- **g**: Generator of subgroup of order q, `g = h^{(p-1)/q} mod p`.
- **KEK**: Key-encryption key derived from ZZ.
- **CEK**: Content-encryption key (wrapped by KEK).
- **OtherInfo**: DER-encoded structure containing KeySpecificInfo, optional partyAInfo, and suppPubInfo.
- **partyAInfo**: Random 512-bit string provided by sender, used to diversify KEKs.
- **counter**: 32-bit number, starts at 1, incremented per KM block.

## 1. Introduction
Diffie-Hellman key agreement (as per ANSI X9.42) allows two parties to agree on a shared secret, convertible into keying material for symmetric algorithms.

### 1.1. Requirements Terminology
Keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

## 2. Overview Of Method
Both parties have key pairs; combining private and public keys yields ZZ, which is converted into a KEK to wrap a CEK.

### 2.1. Key Agreement
- **2.1.1. Generation of ZZ**:  
  `ZZ = g^(xb * xa) mod p` = `(yb^xa) mod p = (ya^xb) mod p`.  
  Leading zeros MUST be preserved, so ZZ occupies as many octets as p.
- **2.1.2. Generation of Keying Material**:  
  `KM = SHA-1(ZZ || OtherInfo)`.  
  OtherInfo is DER-encoded SEQUENCE (KeySpecificInfo, optional partyAInfo, suppPubInfo).  
  `KeySpecificInfo ::= SEQUENCE { algorithm OBJECT IDENTIFIER, counter OCTET STRING (4 bytes) }`.  
  `counter` initial value = 1 (00 00 00 01 hex), incremented per KM block.  
  `partyAInfo`: if provided, MUST contain 512 bits.  
  `suppPubInfo`: length of KEK in bits (32-bit network byte order).  
  KM blocks concatenated left-to-right.  
  Effective key space limited by ZZ size; partyAInfo MUST be used in Static-Static mode, MAY appear in Ephemeral-Static mode.
- **2.1.3. KEK Computation**:  
  For 3DES (192 bits): run algorithm twice (counter=1 and counter=2), then parity adjust.  
  For RC2-128: run once (counter=1), use leftmost 128 bits.  
  For RC2-40: run once, use leftmost 40 bits.
- **2.1.4. Keylengths for common algorithms**:  
  - 3-key 3DES: 192 bits  
  - RC2-128: 128 bits  
  - RC2-40: 40 bits
- **2.1.5. Public Key Validation**:  
  The following algorithm MAY be used:  
  1. Verify y is in [2, p-1].  
  2. Compute y^q mod p; if result == 1, key is valid; otherwise invalid.  
  Primary purpose: prevent small subgroup attack.
- **2.1.6. Example 1** (condensed):  
  Shows ZZ to 3DES KEK generation; two SHA-1 invocations with counter 1 and 2 produce 20-byte outputs, concatenated to form 192-bit key.
- **2.1.7. Example 2** (condensed):  
  Shows ZZ to RC2-128 KEK generation with partyAInfo; single SHA-1 invocation yields 20 bytes; leftmost 16 bytes used as key.

### 2.2. Key and Parameter Requirements
- Group parameters must be of form p = qj + 1 (q prime, j ≥ 2).
- Private key x MUST be in [2, q-2], randomly generated.
- m (length of q) MUST be ≥ 160 bits; p MUST be at least 512 bits.
- **2.2.1. Group Parameter Generation** (SHOULD use algorithm from Section 2.2.1):  
  - **2.2.1.1. Generation of p, q**: Detailed algorithm using SHA-1, seed, and primality tests. Steps 1–20.
  - **2.2.1.2. Generation of g**: Algorithm from FIPS-186: j = (p-1)/q; pick h (1 < h < p-1), g = h^j mod p; if g=1 repeat.
- **2.2.2. Group Parameter Validation** (MAY use):  
  Two checks:  
  1. Verify p = qj + 1.  
  2. Verify that FIPS-186 generation with given seed and pgenCounter yields p.

### 2.3. Ephemeral-Static Mode
- Recipient has static certified key; sender generates new key pair per message.
- If sender key is freshly generated, partyAInfo MAY be omitted.  
- If same ephemeral key is reused (cached), partyAInfo MUST be used for each message.  
- All implementations MUST implement Ephemeral-Static mode.  
- To resist small subgroup attacks, recipient SHOULD perform validation (Section 2.1.5).  
- MAY omit check if opponent cannot determine decryption success/failure.

### 2.4. Static-Static Mode
- Both sender and recipient have static certified keys.
- Since ZZ is constant, partyAInfo MUST be used (different per message).
- Implementations MAY implement Static-Static mode.
- To prevent small subgroup attacks, both parties SHOULD either validate (Section 2.1.5) or verify CA validation.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Leading zeros in ZZ MUST be preserved; ZZ occupies as many octets as p. | MUST | 2.1.1 |
| R2 | If partyAInfo is provided, it MUST contain 512 bits. | MUST | 2.1.2 |
| R3 | partyAInfo MUST be used in Static-Static mode. | MUST | 2.1.2, 2.4 |
| R4 | partyAInfo MAY appear in Ephemeral-Static mode. | MAY | 2.1.2 |
| R5 | Private key x MUST be in [2, q-2]. | MUST | 2.2 |
| R6 | m (bit length of q) MUST be ≥ 160 bits. | MUST | 2.2 |
| R7 | p MUST be at least 512 bits. | MUST | 2.2 |
| R8 | Group parameters SHOULD be generated using the algorithm in Section 2.2.1. | SHOULD | 2.2.1 |
| R9 | Ephemeral-Static mode MUST be implemented. | MUST | 2.3 |
| R10 | If same ephemeral key is reused, partyAInfo MUST be used for each message. | MUST | 2.3 |
| R11 | In Ephemeral-Static mode, recipient SHOULD perform public key validation (Section 2.1.5). | SHOULD | 2.3 |
| R12 | Static-Static mode MAY be implemented. | MAY | 2.4 |
| R13 | In Static-Static mode, both parties SHOULD perform public key validation or verify CA validation. | SHOULD | 2.4 |

## Security Considerations (Condensed)
- All security depends on private key secrecy; disclosure or loss compromises all messages.
- Static keys are vulnerable to small subgroup attacks; Sections 2.3 and 2.4 prescribe countermeasures.
- Security level depends on symmetric key length, prime q size (2^(m/2)), and prime p size (subexponential). Balanced system recommended; overall security limited by lowest level.

## Informative Annexes (Condensed)
- **Example 1 (2.1.6)**: ZZ 20 bytes → 3DES KEK via two SHA-1 computations; outputs concatenated and parity adjusted.
- **Example 2 (2.1.7)**: ZZ 20 bytes → RC2-128 KEK with partyAInfo; single SHA-1 yields 20 bytes, leftmost 16 used.
- **Acknowledgements**: Based on ANSI X9F1 work; thanks to contributors.
- **References**: [CMS], [FIPS-46-1], [FIPS-81], [FIPS-180], [FIPS-186], [P1363], [PKIX], [LAW98], [LL97], [RFC2119], [X942].