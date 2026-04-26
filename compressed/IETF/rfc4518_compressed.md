# RFC 4518: Lightweight Directory Access Protocol (LDAP): Internationalized String Preparation
**Source**: IETF (Standards Track) | **Version**: June 2006 | **Date**: June 2006 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc4518

## Scope (Summary)
Defines precise string preparation algorithms for character-based matching rules used in LDAP (e.g., caseIgnoreMatch) to resolve interoperability and security issues arising from underspecified Unicode handling.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3454] Hoffman, P. and M. Blanchet, "Preparation of Internationalized Strings ("stringprep")", RFC 3454, December 2002.
- [RFC4510] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map", RFC 4510, June 2006.
- [RFC4517] Legg, S., Ed., "Lightweight Directory Access Protocol (LDAP): Syntaxes and Matching Rules", RFC 4517, June 2006.
- [Unicode] The Unicode Consortium, "The Unicode Standard, Version 3.2.0" (as amended by UAX #27 and #28).
- [UAX15] Davis, M. and M. Duerst, "Unicode Standard Annex #15: Unicode Normalization Forms, Version 3.2.0", March 2002.
- [X.680] ITU-T, "Abstract Syntax Notation One (ASN.1) - Specification of Basic Notation", X.680(2002) (also ISO/IEC 8824-1:2002).

## Definitions and Abbreviations
- **Combining mark**: Any Unicode code point with mark property (Mn, Mc, Me) – see Appendix A for definitive list.
- **Space** (for Section 2.6): The SPACE (U+0020) code point followed by no combining marks.
- **Hyphen** (for Section 2.6.3): One of the following code points followed by no combining marks: U+002D, U+058A, U+2010, U+2011, U+2212, U+FE63, U+FF0D.

## 1. Introduction
### 1.1. Background
LDAP matching rules (e.g., caseIgnoreMatch) determine whether a presented value matches an attribute value. Underspecified Unicode handling in X.520 caused interoperability problems.

### 1.2. X.500 String Matching Rules
X.520 definitions (e.g., caseIgnoreMatch) are inadequate for Unicode (universalString). Lack of precise specification leads to security vulnerabilities (e.g., certificate chain validation). This document defines precise algorithms.

### 1.3. Relationship to "stringprep"
Algorithms are based on RFC 3454 stringprep with two additional steps: transcoding to Unicode before stringprep; and insignificant character handling after stringprep. Steps: Transcode, Map, Normalize, Prohibit, Check Bidi, Insignificant Character Handling.

### 1.4. Relationship to the LDAP Technical Specification
This document is an integral part of the LDAP technical specification [RFC4510], obsoleting [RFC3377].

### 1.5. Relationship to X.500
Algorithms are based on "Internationalized String Matching Rules for X.500" [XMATCH] proposal.

### 1.6. Conventions and Terms
Key words as in BCP 14 [RFC2119]: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL.

## 2. String Preparation
The following six-step process SHALL be applied to each presented and attribute value in preparation for character string matching rule evaluation. Failure in any step causes the assertion to evaluate to Undefined. Character repertoire: Unicode 3.2.

Implementations MAY use alternative processes that produce consistent behavior.

### 2.1. Transcode
- **PrintableString**: transcoded directly to Unicode.
- **UniversalString, UTF8String, bmpString**: need not be transcoded (already Unicode-based).
- **TeletexString**: transcoded to Unicode; mapping is a local matter. Use of TeletexString is NOT RECOMMENDED.

### 2.2. Map
- Map to nothing: SOFT HYPHEN (U+00AD), MONGOLIAN TODO SOFT HYPHEN (U+1806), COMBINING GRAPHEME JOINER (U+034F), VARIATION SELECTORS (U+180B-180D, FF00-FE0F), OBJECT REPLACEMENT CHARACTER (U+FFFC).
- Map to SPACE (U+0020): CHARACTER TABULATION (U+0009), LINE FEED (U+000A), LINE TABULATION (U+000B), FORM FEED (U+000C), CARRIAGE RETURN (U+000D), NEXT LINE (U+0085).
- Map to nothing: all other control code points (C0, C1, and Cf codes listed, e.g., U+0000-0008, 000E-001F, 007F-0084, 0086-009F, 06DD, 070F, 180E, 200C-200F, 202A-202E, 2060-2063, 206A-206F, FEFF, FFF9-FFFB, 1D173-1D17A, E0001, E0020-E007F).
- Map to nothing: ZERO WIDTH SPACE (U+200B).
- Map to SPACE: all other Separator property code points (U+0020, 00A0, 1680, 2000-200A, 2028-2029, 202F, 205F, 3000).
- For case ignore, numeric, and stored prefix string matching rules: case fold per B.2 of [RFC3454].

### 2.3. Normalize
Input string to be normalized to Unicode Form KC (compatibility composed) as per [UAX15].

### 2.4. Prohibit
Prohibited code points (step fails if any present):
- All Unassigned code points (Table A.1 of [RFC3454]).
- Characters that change display properties or are deprecated (Table C.8 of [RFC3454]).
- Private Use code points (Table C.3 of [RFC3454]).
- All non-character code points (Table C.4 of [RFC3454]).
- Surrogate codes (Table C.5 of [RFC3454]).
- REPLACEMENT CHARACTER (U+FFFD).

### 2.5. Check Bidi
Bidirectional characters are ignored (no prohibition or handling in this algorithm).

### 2.6. Insignificant Character Handling
Modification depends on the matching rule.

#### 2.6.1. Insignificant Space Handling (Case Ignore and Exact Matching)
- **Space** defined as SPACE (U+0020) followed by no combining marks.
- **Attribute values and non-substring assertion values**:
  - If string contains no non-space character: output is exactly two SPACEs.
  - Otherwise: string starts with exactly one SPACE, ends with exactly one SPACE, and any inner non-empty space sequence replaced with exactly two SPACEs.
- **Substring assertion values**:
  - If string contains no non-space characters: output is exactly one SPACE.
  - Otherwise: adjust beginning/end per substring type (initial, any, final) to have exactly one SPACE at relevant boundaries.

#### 2.6.2. numericString Insignificant Character Handling
- **Space** defined as above.
- All spaces are removed (e.g., "123 456" becomes "123456").

#### 2.6.3. telephoneNumber Insignificant Character Handling
- **Hyphen** defined as list of hyphen-like characters (U+002D, U+058A, U+2010, U+2011, U+2212, U+FE63, U+FF0D) followed by no combining marks.
- **Space** defined as above.
- All hyphens and spaces are removed.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The six-step process SHALL be applied to each presented and attribute value. | SHALL | Section 2 |
| R2 | Failure in any step causes the assertion to evaluate to Undefined. | SHALL | Section 2 |
| R3 | Use of TeletexString is NOT RECOMMENDED. | NOT RECOMMENDED | Section 2.1 |
| R4 | Input string SHALL be normalized to Unicode Form KC. | SHALL | Section 2.3 |
| R5 | All prohibited code points cause step failure (see list). | SHALL | Section 2.4 |
| R6 | Insignificant space handling for case ignore/exact matching as defined in 2.6.1. | SHALL | Section 2.6.1 |
| R7 | All spaces removed for numericString matching. | SHALL | Section 2.6.2 |
| R8 | All hyphens and spaces removed for telephoneNumber matching. | SHALL | Section 2.6.3 |

## Informative Annexes (Condensed)
- **Appendix A (Combining Marks – Normative)**: Definitive list of code points with Mn, Mc, Me properties from Unicode data files.
- **Appendix B (Substrings Matching – Non-normative)**: Explains rationale for the space handling algorithm in 2.6.1; addresses edge cases such as leading/trailing spaces in substrings and sub-partitioning failures (e.g., `(CN=foo\20*\20bar)` vs `"foo<SPACE><SPACE>bar"`). The chosen algorithm ensures that insignificant spaces are handled correctly across substring assertions while accepting minor anomalies with no practical impact.

## Security Considerations
Security considerations from RFC 3454 generally apply.

## Acknowledgements
Based on stringprep [RFC3454] by Paul Hoffman and Marc Blanchet. Additional guidance from Unicode standards. Product of IETF LDAPBIS Working Group.