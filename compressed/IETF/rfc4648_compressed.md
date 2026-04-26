# RFC 4648: The Base16, Base32, and Base64 Data Encodings
**Source**: IETF | **Version**: Obsoletes RFC 3548 | **Date**: October 2006 | **Type**: Standards Track
**Original**: https://datatracker.ietf.org/doc/rfc4648/

## Scope (Summary)
This document defines the Base16, Base32, and Base64 encoding schemes for representing arbitrary binary data as ASCII strings. It clarifies encoding rules, padding, line feeds, non-alphabet characters, alphabets, and canonical encoding to reduce ambiguity and improve interoperability.

## Normative References
- [1] Cerf, V., "ASCII format for network interchange", RFC 20, October 1969.
- [2] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **base64**: The Base 64 encoding described in Section 4, using the alphabet from Table 1.
- **base64url**: The URL and filename safe variant (Table 2) from Section 5; not the same as base64.
- **base32**: The Base 32 encoding described in Section 6 (Table 3); case-insensitive.
- **base32hex**: Extended Hex Base 32 alphabet (Table 4) from Section 7; preserves sort order.
- **base16 / hex**: Standard case-insensitive hex encoding (Table 5), Section 8.
- **pad character**: "=" used to indicate that additional zero bits were added to complete a quantum.
- **canonical encoding**: Encoded data where pad bits are set to zero and all rules are followed.

## Implementation Discrepancies

### 3.1 Line Feeds in Encoded Data
- **MUST NOT** add line feeds to base-encoded data unless the referring specification explicitly directs adding line feeds after a specific number of characters.

### 3.2 Padding of Encoded Data
- **MUST** include appropriate pad characters ("=") at the end of encoded data unless the referring specification explicitly states otherwise. Base16 does not require padding.

### 3.3 Interpretation of Non-Alphabet Characters in Encoded Data
- **MUST** reject encoded data containing characters outside the base alphabet, unless the referring specification explicitly states otherwise (e.g., MIME may ignore non-alphabet characters). Specifications **MAY** ignore pad characters if present before the end, and **MAY** ignore excess pad characters.

### 3.4 Choosing the Alphabet
- Discusses human confusion (0/O, 1/l/I), encoding constraints (e.g., "/" in URLs), and legacy text tools. No universal alphabet; this document defines common ones.

### 3.5 Canonical Encoding
- Pad bits **MUST** be set to zero by conforming encoders. Decoders **MAY** reject encodings where pad bits are non-zero.

## Base 64 Encoding (Section 4)
- Referred to as "base64". Uses 65-character subset (A–Z, a–z, 0–9, +, /, =). Encodes 3 input octets into 4 output characters. Padding rules:
  1. Integral multiple of 24 bits → no padding.
  2. Exactly 8 bits → 2 characters + "==".
  3. Exactly 16 bits → 3 characters + "=".
- Alphabet: Table 1 (A=0 … / = 63, pad = '=').

## Base 64 Encoding with URL and Filename Safe Alphabet (Section 5)
- Referred to as "base64url". Same as base64 except 62nd and 63rd characters are "-" (minus) and "_" (underline) instead of "+" and "/". Pad character "=" may be percent-encoded in URIs, or omitted if length is known (see Section 3.2).

## Base 32 Encoding (Section 6)
- Referred to as "base32". Uses 33-character subset (A–Z, 2–7, =). Encodes 5 input octets into 8 output characters. Padding rules:
  1. Integral multiple of 40 bits → no padding.
  2. Exactly 8 bits → 2 characters + 6 "=".
  3. Exactly 16 bits → 4 characters + 4 "=".
  4. Exactly 24 bits → 5 characters + 3 "=".
  5. Exactly 32 bits → 7 characters + 1 "=".
- Alphabet: Table 3 (0=A, 1=B, … 7=H, 8=I, 9=J … 31=7, pad='=').

## Base 32 Encoding with Extended Hex Alphabet (Section 7)
- Referred to as "base32hex". Same as base32 but alphabet is 0–9, A–V (Table 4). Preserves sort order when compared bit-wise.

## Base 16 Encoding (Section 8)
- Referred to as "base16" or "hex". Uses 16 characters (0–9, A–F). Encodes 1 octet into 2 characters. No padding needed.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST NOT add line feeds unless explicitly directed. | MUST | Section 3.1 |
| R2 | Implementations MUST include appropriate pad characters unless explicitly stated otherwise. | MUST | Section 3.2 |
| R3 | Implementations MUST reject data with characters outside the base alphabet unless explicitly stated otherwise. | MUST | Section 3.3 |
| R4 | Specifications MAY ignore non-alphabet characters (e.g., CRLF) and MAY ignore extra pad characters. | MAY | Section 3.3 |
| R5 | Pad bits MUST be set to zero by conforming encoders. | MUST | Section 3.5 |
| R6 | Decoders MAY reject encodings where pad bits have not been set to zero. | MAY | Section 3.5 |
| R7 | Base16 encoding requires no padding. | - | Section 8 |
| R8 | Base64 and base32 encodings require padding per rules in Sections 4 and 6. | MUST | Sections 4, 6 |

## Informative Annexes (Condensed)
- **Annex (Section 9)**: Illustrations and examples showing bit mapping for base64 and base32, plus worked encoding examples (0x14fb9c03d97e → "FPucA9l+" etc.).
- **Annex (Section 10)**: Test vectors for all encodings with sample strings ("f", "fo", "foo", "foob", "fooba", "foobar") confirming correct padding and output.
- **Annex (Section 11)**: Reference ISO C99 implementation available at http://josefsson.org/base-encoding/ (non-normative).
- **Annex (Section 12)**: Security considerations – implementations must avoid buffer overflow; ignoring non-alphabet characters creates covert channel; base encoding does not provide confidentiality; base encoding adds no entropy but provides signature for cryptanalysis.
- **Annex (Section 13)**: Changes since RFC 3548 (added base32hex, referenced IMAP, fixed example, added test vectors, security consideration, typo fixes).
- **Annex (Section 14)**: Acknowledgements.
- **Annex (Section 15)**: Copying conditions (author grants irrevocable permission for reuse, no misleading info).
- **Annex (Section 16.2)**: Informative references (RFC 1421, 2045, 2440, 4033, 2938, 3501, 3986; Internet Drafts by Laurie et al. and Myers; mailing list post by Wilcox-O'Hearn).

## Security Considerations (Summary)
- Care needed to avoid buffer overflow and NUL character issues.
- Ignoring non-alphabet characters creates covert channel; recommended practice is to reject.
- Case insensitivity of base16/base32 can leak information.
- Non-significant bits in padding may leak information or cause failures.
- Base encoding does not provide confidentiality; passwords must not be considered hidden.
- Base encoding provides a signature for cryptanalysis (characteristic probability distribution).