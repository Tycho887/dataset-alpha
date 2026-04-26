# RFC 3629: UTF-8, a transformation format of ISO 10646
**Source**: IETF (Standards Track, STD 63) | **Version**: RFC 3629 | **Date**: November 2003 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc3629

## Scope (Summary)
Defines UTF-8, a one-octet encoding of ISO/IEC 10646 (UCS) preserving full US-ASCII compatibility. Obsoletes RFC 2279.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [ISO.10646] ISO/IEC Standard 10646 (2000/2001/2002 amendments).
- [UNICODE] The Unicode Standard, Version 4.0 (Addison-Wesley, 2003).

## Definitions and Abbreviations
- **UTF-8**: A character encoding form using sequences of 1 to 4 octets for characters U+0000..U+10FFFF (UTF-16 accessible range).
- **UCS**: Universal Character Set defined by ISO/IEC 10646.
- **BOM**: Byte Order Mark (U+FEFF) when used as a signature.
- **U+HHHH**: Notation for UCS characters (4–6 hex digits).
- **MUST / SHALL / SHOULD / MAY**: As per RFC2119.

## 3. UTF-8 Definition
- **Encoding**: 
  - Characters U+0000–U+007F: single octet `0xxxxxxx`.
  - Characters U+0080–U+07FF: two octets `110xxxxx 10xxxxxx`.
  - Characters U+0800–U+FFFF: three octets `1110xxxx 10xxxxxx 10xxxxxx`.
  - Characters U+10000–U+10FFFF: four octets `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`.
- **Prohibited**: Encoding character numbers U+D800–U+DFFF (UTF-16 surrogates) is prohibited.
- **Encoding procedure** (steps 1–3): Determine octet count, prepare high-order bits, fill bits from character number.
- **Decoding procedure** (steps 1–3): Initialize binary number, identify bits, distribute bits.
- **MUST protect against invalid sequences**: e.g., overlong sequences or surrogate pairs. See Security Considerations.

## 4. Syntax of UTF-8 Byte Sequences
- ABNF grammar (derived from Unicode):
  ```
  UTF8-octets = *( UTF8-char )
  UTF8-char   = UTF8-1 / UTF8-2 / UTF8-3 / UTF8-4
  UTF8-1      = %x00-7F
  UTF8-2      = %xC2-DF UTF8-tail
  UTF8-3      = %xE0 %xA0-BF UTF8-tail / %xE1-EC 2( UTF8-tail ) /
                %xED %x80-9F UTF8-tail / %xEE-EF 2( UTF8-tail )
  UTF8-4      = %xF0 %x90-BF 2( UTF8-tail ) / %xF1-F3 3( UTF8-tail ) /
                %xF4 %x80-8F 2( UTF8-tail )
  UTF8-tail   = %x80-BF
  ```
- Note: authoritative definition is in [UNICODE]; this grammar is informative.

## 5. Versions of the Standards
- New versions add characters except for the incompatible "Korean mess" (Amendment 5, Movement of Hangul block). Incompatible changes are pledged never to occur again.
- MIME charset label "UTF-8" is version-independent (see Section 8).

## 6. Byte Order Mark (BOM)
- **U+FEFF** (ZERO WIDTH NO-BREAK SPACE) may be used as a signature at stream start, encoded as `EF BB BF`.
- **When not at stream start**: MUST be interpreted as zero-width non-breaking space.
- **Stripping**: RECOMMENDED to avoid stripping without good reason; ignore when appropriate.
- **Protocol restrictions**:
  - A protocol SHOULD forbid use of U+FEFF as a signature for protocol elements mandated to be always UTF-8.
  - A protocol SHOULD also forbid use as signature when encoding identification mechanisms exist and implementations can always use them properly.
  - A protocol SHOULD NOT forbid use as signature when no encoding identification mechanisms exist or implementations cannot always use them properly.
  - When forbidden, any initial U+FEFF MUST be interpreted as a zero-width non-breaking space.
  - When not forbidden, implementations SHOULD be prepared to handle a signature and react appropriately.

## 7. Examples
- Illustrative hex-encoded sequences provided for various character strings (A<NOT IDENTICAL TO><ALPHA>., Korean "hangugeo", Japanese "nihongo", Chinese character U+233B4 with BOM).

## 8. MIME Registration
- Charset parameter: "UTF-8", suitable for text media types.
- Version-independent label, referring to all versions after Amendment 5 (Korean block). No incompatible changes expected.

## 9. IANA Considerations
- IANA charset registry entry for UTF-8 updated to point to this memo.

## 10. Security Considerations
- **Invalid sequences**: MUST NOT decode illegal octet sequences (e.g., overlong NUL `C0 80`, surrogate pairs). Attackers may exploit incautious parsers.
- **Buffer overflow**: When encoding, character numbers MUST be limited to U+10FFFF; 5- and 6-byte sequences are NOT valid UTF-8.
- **Unicode normalization**: Multiple character sequences for the same visual string (e.g., precomposed vs. decomposed) may affect security decisions (string matching, identifiers). Use Unicode Normalization Forms (UAX15).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Encoding character numbers between U+D800 and U+DFFF is prohibited. | MUST NOT | Section 3 |
| R2 | Decoding implementations MUST protect against invalid sequences. | MUST | Section 3 |
| R3 | When U+FEFF appears at any position other than stream start, it MUST be interpreted as zero-width non-breaking space, NOT as signature. | MUST | Section 6 |
| R4 | When protocol forbids U+FEFF as signature, any initial U+FEFF MUST be interpreted as zero-width non-breaking space. | MUST | Section 6 |
| R5 | When protocol does not forbid U+FEFF as signature, implementations SHOULD be prepared to handle a signature. | SHOULD | Section 6 |
| R6 | Protocol SHOULD forbid U+FEFF as signature for protocol elements always UTF-8. | SHOULD | Section 6 |
| R7 | Protocol SHOULD also forbid U+FEFF as signature when encoding identification mechanisms exist and are properly usable. | SHOULD | Section 6 |
| R8 | Protocol SHOULD NOT forbid U+FEFF as signature when no encoding identification mechanisms exist or when ban is unenforceable. | SHOULD NOT | Section 6 |
| R9 | Character numbers in UTF-8 encoding MUST be limited to U+10FFFF. | MUST | Section 10 |

## Informative Annexes (Condensed)
- **Section 2 (Notational conventions)**: Defines RFC2119 keywords and U+HHHH notation.
- **Section 5 (Versions)**: Describes the "Korean mess" and commitment to no future incompatible changes.
- **Section 11 (Acknowledgements)**: List of contributors.
- **Section 12 (Changes from RFC 2279)**: Summary of modifications (restricted range, Unicode normative, BOM section, ABNF, security expansion).
- **Section 14-18**: References (informative), IP statement, author address, full copyright.