# RFC 3454: Preparation of Internationalized Strings ("stringprep")
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: December 2002 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc3454

## Scope (Summary)
This document specifies a framework for preparing Unicode text strings (stringprep) to increase the likelihood that string input and comparison work consistently for typical users worldwide. It defines processing rules (mapping, normalization, prohibition, bidirectional checking) and provides base tables; protocols MUST create profiles that select among these options.

## Normative References
- [UAX15] Unicode Normalization Forms, Version 3.2.0
- [Unicode3.2] The Unicode Standard, Version 3.2.0
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **Stringprep**: A framework for preparing strings that uses mapping, normalization, prohibition, and optional bidi checking.
- **Profile**: A protocol-specific selection of stringprep options (mapping tables, normalization, prohibited characters, bidi handling).
- **Stored strings**: Strings used in protocol identifiers or named entities (e.g., names in certificates, DNS name parts).
- **Queries**: Strings used to match against stored strings (e.g., user input for lookups).
- **Bidi**: Bidirectional text (characters with right-to-left or left-to-right display).
- **RandALCat character**: A character with Unicode bidirectional category "R" or "AL".
- **LCat character**: A character with Unicode bidirectional category "L".
- **AO, MN, D, U**: Categories for code points: Allowed Output, Mapped to Nothing/Normalized, Disallowed, Unassigned.

## 1. Introduction
- Stringprep processes a single string of input characters to an output string, or returns an error if prohibited characters appear.
- Profiles cannot account for all spelling variations (e.g., theatre vs. theater, simplified vs. traditional Chinese).
- Profiles MUST NOT "correct" character standards.

### 1.1 Terminology
- Key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) as per RFC 2119.
- Character names use Unicode 3.2 notation.

### 1.2 Using stringprep in protocols
- A profile MUST include: intended applicability, character repertoire, mapping tables used, any additional mappings, normalization used, prohibited output tables, bidi testing used, and any additional prohibitions.
- Stringprep profiles MUST be registered with IANA; IESG reviews each.
- The repertoire for this version is Unicode 3.2.
- The unassigned code point list in Appendix A MUST be used; discrepancies resolved by Appendix A.

## 2. Preparation Overview
Steps MUST be performed in order: 1) Map, 2) Normalize (optional), 3) Prohibit, 4) Check bidi (optional). Mappings can be one-to-none, one-to-one, etc.

## 3. Mapping
- Each character must be checked against a mapping table.
- Tables come from Appendix B (B.1, B.2, B.3). Mapped characters are not re-scanned.

### 3.1 Commonly mapped to nothing
- Characters are deleted (e.g., SOFT HYPHEN, ZERO WIDTH SPACE, VARIATION SELECTORS). Full list in Table B.1.

### 3.2 Case folding
- For case-insensitive comparison, profiles SHOULD use Table B.2 (with NFKC) or B.3 (without normalization).
- Mapping is from uppercase to lowercase.
- Profiles SHOULD use [UTR21] CaseFolding.txt for additional folding.

## 4. Normalization
- Optionally normalize using Unicode normalization form KC (NFKC).
- Profiles MUST NOT use form C; if normalization is used, MUST be NFKC.
- Normalization must be based on the version of Unicode specified in the profile.
- IETF relies on stability of normalization; updates must be considered carefully.

## 5. Prohibited Output
- Strings must be checked for prohibited code points before emission.
- A profile MAY use all or some tables from Appendix C.
- Tables are authoritative over section descriptions.

### 5.1 Space characters
- Prohibited spaces include ASCII SPACE, NO-BREAK SPACE, OGHAM SPACE MARK, various EN/EM spaces, ZERO WIDTH SPACE, etc. (Tables C.1.1, C.1.2).

### 5.2 Control characters
- Control characters (ASCII control, DEL, non-ASCII controls like ARABIC END OF AYAH, ZERO WIDTH JOINER, etc.) are prohibited (Tables C.2.1, C.2.2).

### 5.3 Private use
- Private use code points (planes 0, 15, 16) are prohibited (Table C.3).

### 5.4 Non-character code points
- Non-character code points (e.g., FDD0-FDEF, FFFE-FFFF, and others) are prohibited (Table C.4).

### 5.5 Surrogate codes
- Surrogate codes (D800-DFFF) are prohibited.

### 5.6 Inappropriate for plain text
- Characters like INTERLINEAR ANNOTATION ANCHOR, OBJECT REPLACEMENT CHARACTER, REPLACEMENT CHARACTER are prohibited.

### 5.7 Inappropriate for canonical representation
- Ideographic description characters (2FF0-2FFB) are prohibited.

### 5.8 Change display properties or are deprecated
- Characters that can change display order (e.g., LEFT-TO-RIGHT MARK, RIGHT-TO-LEFT MARK, directional overrides) are prohibited.

### 5.9 Tagging characters
- LANGUAGE TAG and TAGGING CHARACTERS (E0020-E007F) are prohibited.

## 6. Bidirectional Characters
- A profile MAY specify bidi handling; if so, all three requirements MUST be met:
  1) Prohibit characters in Section 5.8.
  2) If any RandALCat character present, string MUST NOT contain any LCat character.
  3) If any RandALCat character present, first and last characters MUST be RandALCat.
- Tables D.1 (R/AL characters) and D.2 (L characters) are used.

## 7. Unassigned Code Points in Stringprep Profiles
- **Stored strings** MUST NOT contain unassigned code points.
- **Queries** MAY contain unassigned code points.
- Categories: AO (Allowed), MN (Mapped/Normalized), D (Disallowed), U (Unassigned).
- A profile must list unassigned code points; subsequent versions MUST NOT change category of existing AO, MN, D code points.
- The versioning scheme ensures backward compatibility: stored strings prepared with newver will not change when processed with oldver.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Steps MUST be performed in order: Map, Normalize, Prohibit, Check bidi. | MUST | Section 2 |
| R2 | Each character MUST be checked against a mapping table. | MUST | Section 3 |
| R3 | Mapping tables in Appendix B MUST be used; discrepancies resolved by appendix. | MUST | Section 3 |
| R4 | If normalization is used, MUST be NFKC. | MUST | Section 4 |
| R5 | Prohibited output MUST be checked before emission (tables in Appendix C). | MUST | Section 5 |
| R6 | If bidi handling specified, all three requirements (5.8 prohibition, no LCat if RandALCat, first/last RandALCat) MUST be met. | MUST | Section 6 |
| R7 | Stored strings MUST NOT contain unassigned code points. | MUST | Section 7 |
| R8 | Profiles MUST include all specified components (1.2 list). | MUST | Section 1.2 |
| R9 | Profiles MUST be registered with IANA and reviewed by IESG. | MUST | Section 10 |

## Informative Annexes (Condensed)
- **Annex A (Unicode Repertoires)**: Defines repertoire as Unicode 3.2; contains full list of unassigned code points (Table A.1) which MUST be used.
- **Annex B (Mapping Tables)**: Contains three tables: B.1 (commonly mapped to nothing), B.2 (case folding with NFKC), B.3 (case folding without normalization). These are normative.
- **Annex C (Prohibition Tables)**: Contains tables C.1–C.9 for prohibited characters: spaces, controls, private use, non-characters, surrogates, inappropriate plain text, canonical representation, display properties, tagging. Normative.
- **Annex D (Bidirectional Tables)**: Contains Table D.1 (R/AL characters) and D.2 (L characters). Used if profile specifies bidi handling.