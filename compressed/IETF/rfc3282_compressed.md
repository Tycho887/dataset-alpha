# RFC 3282: Content Language Headers
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: May 2002 | **Type**: Normative
**Obsoletes**: RFC 1766

## Scope (Summary)
This document defines a "Content-language:" header for RFC 822‑like headers (e.g., MIME body parts, Web documents) to indicate language(s) of content, and an "Accept-Language:" header for indicating a user's language preferences.

## Normative References
- [TAGS] BCP 47, RFC 3066 (Tags for the Identification of Languages)
- [RFC 2119] Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- [RFC 2234] Augmented BNF for Syntax Specifications: ABNF
- [RFC 2616] Hypertext Transfer Protocol -- HTTP/1.1
- [RFC 2822] Internet Message Format
- [ISO 639], [ISO 639-2], [ISO 3166], [ISO 15924] (informative references)
- [RFC 2045–2049] MIME series (informative)

## Definitions and Abbreviations
- **Language-Tag**: as defined in [TAGS]
- **Language-range**: as defined in [TAGS]
- **qvalue**: a quality value between 0 and 1 (with up to 3 decimal places) per HTTP/1.1 [RFC 2616]
- **CFWS**: Commented folding whitespace as per RFC 2822
- **WSP**: Whitespace

## 2. The Content-Language header
### 2.1 Syntax (Normative)
- **Content-Language header**: `Content-Language = "Content-Language" ":" 1#Language-tag` (RFC 822 EBNF)
- **Strict ABNF (RFC 2234)**:
  ```
  Content-Language = "Content-Language" ":" [CFWS] Language-List
  Language-List = Language-Tag [CFWS] *("," [CFWS] Language-Tag [CFWS])
  ```
- **Obsolete syntax** (MUST be accepted, MUST NOT be generated):
  ```
  obs-content-language = "Content-Language" *WSP ":" [CFWS] Language-List
  ```
- **Conforming implementations MUST accept the obs-content-language syntax, but MUST NOT generate it; all generated headers MUST conform to the Content-Language syntax.**

### 2.2 Examples (Informative – condensed)
- List of examples for language tags (en-scouse, i-mingo, en/fr, da/de/el/en/fr/it, i-klingon) illustrating various usages. The full examples can be found in the original document.

## 3. The Accept-Language header
### 3.1 Syntax (Normative)
- **Accept-Language header** (RFC 822 EBNF):
  ```
  Accept-Language = "Accept-Language" ":" 1#( language-range [ ";" "q" "=" qvalue ] )
  ```
- **Strict ABNF**:
  ```
  Accept-Language = "Accept-Language:" [CFWS] language-q *( "," [CFWS] language-q )
  language-q = language-range [";" [CFWS] "q=" qvalue] [CFWS]
  qvalue = ( "0" [ "." 0*3DIGIT ] ) / ( "1" [ "." 0*3("0") ] )
  ```
- **Obsolete syntax** (MUST be accepted, MUST NOT be generated):
  ```
  obs-accept-language = "Accept-Language" *WSP ":" [CFWS] obs-language-q *( "," [CFWS] obs-language-q ) [CFWS]
  obs-language-q = language-range [ [CFWS] ";" [CFWS] "q" [CFWS] "=" qvalue ]
  ```
- **Conforming implementations MUST accept the obs-accept-language syntax, but MUST NOT generate it; all generated messages MUST conform to the Accept-Language syntax.**

### 3.2 Priority and Quality Values
- If no Q values are given, language-ranges are ordered from most to least preferred (leftmost highest priority). This extends HTTP/1.1 rules per current practice.
- If Q values are given, evaluation follows HTTP/1.1 [RFC 2616].

## 4. Security Considerations
- Language ranges in content negotiation may reveal the sender's nationality, potentially enabling surveillance. This is a general information leakage problem. The threat magnitude and countermeasures are application‑protocol specific.

## 5. Character Set Considerations
- This specification adds no new considerations beyond those in [TAGS].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST accept `obs-content-language` syntax | shall | Section 2 |
| R2 | Implementations MUST NOT generate `obs-content-language` syntax | shall not | Section 2 |
| R3 | All generated Content-Language headers MUST conform to the Content-Language syntax | shall | Section 2 |
| R4 | Implementations MUST accept `obs-accept-language` syntax | shall | Section 3.1 |
| R5 | Implementations MUST NOT generate `obs-accept-language` syntax | shall not | Section 3.1 |
| R6 | All generated Accept-Language headers MUST conform to the Accept-Language syntax | shall | Section 3.1 |
| R7 | When no Q values are given, language-ranges are in priority order (leftmost highest) | should | Section 3.2 |

## Informative Annexes (Condensed)
- **Appendix A: Changes from RFC 1766**: Language tag definitions were moved to RFC 3066. The `differences` parameter for `multipart/alternative` was removed due to lack of implementations. The ABNF for Content-Language was updated to RFC 2234 syntax.
- **Acknowledgements**: Thanks to many contributors, with special mention to Michael Everson (language tag reviewer) and Bruce Lilly (ABNF review).