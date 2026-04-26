# RFC 2781: UTF-16, an encoding of ISO 10646
**Source**: Internet Engineering Task Force (IETF) | **Version**: Informational | **Date**: February 2000 | **Type**: Informational
**Original**: https://www.rfc-editor.org/rfc/rfc2781.txt

## Scope (Summary)
This document defines the UTF‑16 encoding of Unicode/ISO 10646, specifies its serialization as an octet stream for Internet transmission, and registers three MIME charset parameter values: UTF‑16BE, UTF‑16LE, and UTF‑16.

## Normative References
- RFC 2119 (BCP 14) – Key words for use in RFCs to Indicate Requirement Levels (MUST/SHOULD/MAY)
- BCP 18 (RFC 2277) – IETF Policy on Character Sets and Languages
- BCP 19 (RFC 2278) – IANA Charset Registration Procedures
- Unicode Standard 3.0
- ISO/IEC 10646‑1:1993 + Amendments (UTF‑16 defined in Annex Q, Amendment 1)
- UTF‑8 (RFC 2279)

## Definitions and Abbreviations
- **Character value**: The Unicode scalar value (UCS‑4) assigned to a character, shown in hexadecimal.
- **UTF‑16**: Encoding where characters ≤ 0xFFFF use one 16‑bit integer; characters 0x10000–0x10FFFF use a surrogate pair (high surrogate 0xD800–0xDBFF followed by low surrogate 0xDC00–0xDFFF).
- **BOM (Byte Order Mark)**: The character U+FEFF (ZERO WIDTH NON‑BREAKING SPACE) used at the beginning of a UTF‑16 stream to indicate endianness.
- **Big‑endian (BE)**: Higher‑order octet first in serialization.
- **Little‑endian (LE)**: Lower‑order octet first in serialization.
- **Surrogate pair**: Two 16‑bit integers that encode a character outside the BMP.

## 1. Introduction
Describes the purpose, background, and motivation for UTF‑16 in the Internet context.

## 2. UTF‑16 Definition
### 2.1 Encoding UTF‑16
- **Rule for U ≤ 0x10FFFF**:
  1. If U < 0x10000, encode as a single 16‑bit unsigned integer.
  2. If U ≥ 0x10000, compute U' = U – 0x10000 (≤ 0xFFFFF).
  3. Set W1 = 0xD800 | (high 10 bits of U') and W2 = 0xDC00 | (low 10 bits of U').
  4. Output W1 then W2.

### 2.2 Decoding UTF‑16
- **Single character decoding**:
  1. If W1 is not in surrogate range (0xD800–0xDFFF), U = W1.
  2. If W1 ∈ [0xD800, 0xDBFF] and W2 ∈ [0xDC00, 0xDFFF], construct U' from low 10 bits of W1 and W2, then U = U' + 0x10000.
  3. Otherwise, an error occurs. Error recovery is not specified; the decoder MAY set U to W1 to aid diagnosis.

## 3. Labelling UTF‑16 Text
### 3.1 Big‑endian vs Little‑endian
- Big‑endian: high‑order octet first. Little‑endian: low‑order octet first.

### 3.2 Byte Order Mark (BOM)
- U+FEFF at the start of a stream may serve as an encoding signature: 0xFE 0xFF → BE; 0xFF 0xFE → LE.
- **MUST** interpret U+FEFF at any other position as zero‑width non‑breaking space, **NOT** as BOM.
- An initial U+FEFF **MAY** be interpreted as a zero‑width non‑breaking space; it is not always a BOM.

### 3.3 Choosing a Label
- **SHOULD** label as "UTF‑16BE" or "UTF‑16LE" when the serialization order is known.
- **MUST** serialize UTF‑16BE in big‑endian order; **MUST NOT** prepend a BOM.
- **MUST** serialize UTF‑16LE in little‑endian order; **MUST NOT** prepend a BOM.
- **MUST** label as "UTF‑16" when the order is unknown; **SHOULD** ensure text starts with 0xFEFF.
- Exception: Document formats that mandate a BOM require the "UTF‑16" label only.

## 4. Interpreting Text Labels
### 4.1 UTF‑16BE
- Text labelled UTF‑16BE is always big‑endian. A BOM does not affect deserialization; 0xFF 0xFE is an error.

### 4.2 UTF‑16LE
- Text labelled UTF‑16LE is always little‑endian. A BOM does not affect deserialization; 0xFE 0xFF is an error.

### 4.3 UTF‑16
- The serialization order is determined by the first two octets:
  - 0xFE 0xFF → big‑endian
  - 0xFF 0xFE → little‑endian
  - Otherwise, **SHOULD** interpret as big‑endian.
- Applications **MUST** read at least the first two octets to determine the serialization order.
- Applications **MUST NOT** assume the order without checking for a BOM.
- Applications **MUST** be able to interpret both big‑endian and little‑endian text.

## 5. Examples
(Informative) Shows octet sequences for the string "=Ra" (where Ra = U+12345) under each labelling.

## 6. Versions of the Standards
Summarises that ISO 10646 and Unicode evolve additively, except for the "Korean mess" (Amendment 5) which moved the Hangul block incompatibly. Future incompatible changes may affect MIME charset labeling.

## 7. IANA Considerations
Registers the three charsets using templates in Appendix A.

## 8. Security Considerations
- Processors must handle undefined characters without allowing attacker harm.
- Must be vigilant against control characters that reprogram terminals or execute embedded code.
- Must handle illegal UTF‑16 sequences (e.g., unpaired surrogates) securely.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Character values < 0x10000 encoded as single 16‑bit integer | Must | Section 2.1 |
| R2 | Character values 0x10000–0x10FFFF encoded as two 16‑bit surrogates (0xD800–0xDBFF, 0xDC00–0xDFFF) | Must | Section 2.1 |
| R3 | Decoding: errors may be handled by setting U to W1 for diagnostic aid | May | Section 2.2 |
| R4 | BOM at non‑first position MUST be interpreted as ZWNBSP, not as byte‑order mark | Must | Section 3.2 |
| R5 | Initial 0xFEFF MAY be interpreted as ZWNBSP (not always a BOM) | May | Section 3.2 |
| R6 | When serialization order is known, SHOULD label as UTF‑16BE or UTF‑16LE | Should | Section 3.3 |
| R7 | UTF‑16BE text MUST be serialized big‑endian; MUST NOT prepend BOM | Must | Section 3.3 |
| R8 | UTF‑16LE text MUST be serialized little‑endian; MUST NOT prepend BOM | Must | Section 3.3 |
| R9 | When serialization order is unknown, MUST label as UTF‑16; SHOULD start with 0xFEFF | Must / Should | Section 3.3 |
| R10 | Interpret UTF‑16BE text as big‑endian (BOM does not affect) | Must | Section 4.1 |
| R11 | Interpret UTF‑16LE text as little‑endian (BOM does not affect) | Must | Section 4.2 |
| R12 | For UTF‑16, read first two octets to determine order; if no BOM, SHOULD treat as big‑endian | Must / Should | Section 4.3 |
| R13 | Applications processing UTF‑16 MUST be able to interpret both big‑endian and little‑endian | Must | Section 4.3 |
| R14 | Applications MUST NOT assume serialization order without checking first two octets for a BOM | Must | Section 4.3 |

## Informative Annexes (Condensed)
- **Annex A – Charset Registrations**: Provides registration templates for UTF‑16BE, UTF‑16LE, and UTF‑16. All three are **NOT** suitable for use under the MIME "text" top‑level type (except HTTP via section 19.4.2 of RFC 2616). The labels are version‑independent; they refer generically to ISO/IEC 10646. The "Korean mess" is noted as an incompatible change, but the label remains aligned with post‑Amendment 5 versions.
  - A.1: UTF‑16BE registration – contact Paul Hoffman and Francois Yergeau.
  - A.2: UTF‑16LE registration – same contacts.
  - A.3: UTF‑16 registration – same contacts.