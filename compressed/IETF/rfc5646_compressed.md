# RFC 5646: Tags for Identifying Languages
**Source**: IETF | **Version**: BCP 47 (Obsoletes RFC 4646) | **Date**: September 2009 | **Type**: Normative (BCP)
**Original**: [RFC 5646](https://tools.ietf.org/html/rfc5646)

## Scope (Summary)
This document defines the structure, content, construction, and semantics of language tags used to indicate the language of an information object. It also specifies how to register values for language tags and create user-defined extensions for private interchange. This document, together with RFC 4647, comprises BCP 47.

## Normative References
- ISO 15924:2004 (Script codes)
- ISO 3166-1:2006 (Country codes)
- ISO 639-1:2002 (Alpha-2 language codes)
- ISO 639-2:1998 (Alpha-3 language codes)
- ISO 639-3:2007 (Comprehensive language codes)
- ISO 639-5:2008 (Language families/groups)
- ISO/IEC 646:1991 (ASCII)
- RFC 2026, RFC 2119, RFC 2277, RFC 3339, RFC 4647, RFC 5226, RFC 5234
- [SpecialCasing] Unicode SpecialCasing.txt
- [UAX14] Unicode Line Breaking Properties
- [UN_M.49] Standard Country or Area Codes for Statistical Use
- [Unicode] Unicode Standard 5.0

## Definitions and Abbreviations
- **Tag**: A complete language tag (e.g., "sr-Latn-RS")
- **Subtag**: A segment of a tag delimited by hyphen (e.g., 'zh', 'Hant', 'CN')
- **Code**: A value from an external standard used as a subtag
- **Primary Language Subtag**: First subtag; identifies the language (2-8 letters, or 'x', 'i')
- **Extended Language Subtag**: 3-letter subtag (from ISO 639-3) used with a prefix; preferred form is standalone primary
- **Script Subtag**: 4-letter subtag from ISO 15924 (e.g., 'Latn')
- **Region Subtag**: 2-letter (ISO 3166-1) or 3-digit (UN M.49) (e.g., 'US', '419')
- **Variant Subtag**: 5-8 chars (letter-start) or 4-8 chars (digit-start); registered
- **Extension Subtag**: Introduced by singleton (except 'x'); defined by RFC
- **Private Use Subtag**: Introduced by 'x' or using private-use codes from ISO
- **Grandfathered**: Tags registered under RFC 3066 that are listed in ABNF (regular/irregular)
- **Redundant**: Previously registered tags now composable from subtags
- **Well-formed**: Tag conforms to ABNF (Section 2.1)
- **Valid**: Well-formed, with all primary/extlang/script/region/variant subtags in IANA registry, no duplicate variants/singletons
- **Canonical Form**: No extlang subtags; preferred values applied; extensions in ASCII order
- **Extlang Form**: Canonical form with extlang prefix prepended if applicable

## 1. Introduction
Language tags identify the language used in content or user preferences. They enable appropriate processing (e.g., spell-checking, speech synthesis). This document specifies the language tag mechanism, registration for values, private use, and extensions. Key words (MUST, SHOULD, etc.) are as RFC 2119.

## 2. The Language Tag
### 2.1 Syntax
A language tag is a sequence of subtags separated by hyphens. The ABNF (Figure 1) defines:
- **Language-Tag** = langtag / privateuse / grandfathered
- **langtag** = language ["-" script] ["-" region] *("-" variant) *("-" extension) ["-" privateuse]
- Subtags: primary language (2*3ALPHA, 4ALPHA, 5*8ALPHA), extlang (3ALPHA *2("-" 3ALPHA) – permanently reserved beyond first), script (4ALPHA), region (2ALPHA / 3DIGIT), variant (5*8alphanum or DIGIT 3alphanum), extension (singleton 1*("-" (2*8alphanum))), privateuse ("x" 1*("-" (1*8alphanum)))
- Grandfathered tags are fixed lists: irregular (e.g., "en-GB-oed") and regular (e.g., "art-lojban")
- All subtags max 8 characters; whitespace not allowed; tags are case-insensitive.

#### 2.1.1 Formatting
- Case-insensitive; conventional capitalization: lowercase for language, titlecase for script, uppercase for region, lowercase for extensions/private.
- RECOMMENDED format: registry case. Implementers SHOULD use locale-neutral casing to avoid non-ASCII (e.g., Turkish 'i').

### 2.2 Subtag Sources and Interpretation
IANA maintains the Language Subtag Registry. Definitions: Tag, Subtag, Code. Subtags are type-identifiable by length/position.

#### 2.2.1 Primary Language Subtag
- First subtag, cannot be omitted except for 'x' (private) or 'i' (grandfathered).
- Two-character: ISO 639-1; three-character: ISO 639-2, -3, -5. Range 'qaa'-'qtz' reserved for private use.
- If a 2-char code is later added for a language with a 3-char code, the 2-char MUST NOT be registered (stability).
- Four-char reserved; 5-8 char via registration (discouraged).

#### 2.2.2 Extended Language Subtags
- Three-letter subtags from ISO 639-3; used only with a 'Prefix' (the macrolanguage).
- Each extlang has an identical primary language subtag; primary is RECOMMENDED.
- Extlang record MUST have exactly one 'Prefix' and MUST have 'Preferred-Value' identical to Subtag.
- Only one extlang allowed in a tag (second and third positions permanently reserved).

#### 2.2.3 Script Subtag
- Four letters from ISO 15924; follows primary/extlang, precedes all others.
- Range 'Qaaa'-'Qabx' reserved for private use.
- At most one script subtag; SHOULD be omitted when not distinguishing or when primary language has 'Suppress-Script' field.

#### 2.2.4 Region Subtag
- Two letters (ISO 3166-1, exceptionally reserved codes except 'UK' are registered) or three digits (UN M.49).
- Private use ranges: 'AA', 'QM'-'QZ', 'XA'-'XZ', 'ZZ'.
- UN M.49 macro-geographical codes MUST be registered; economic/other groupings MUST NOT.
- When ISO 3166-1 recycles a code, the UN M.49 code MUST be used for the original meaning.
- At most one region subtag.

#### 2.2.5 Variant Subtags
- Registered with IANA; not from external standard (though may reference one).
- Length: letter-start min 5, digit-start min 4.
- MUST NOT be duplicate in a tag.
- May have 'Prefix' fields indicating appropriate language prefixes.
- Variants sharing a prefix are usually mutually exclusive.

#### 2.2.6 Extension Subtags
- Introduced by singleton (except 'x'); allocated via RFC (IETF Review).
- Must follow primary language at minimum (e.g., "de-a-value").
- Each singleton appears at most once per tag.
- Extension subtags 2-8 chars; case-insensitive, lowercase normalized.
- At least one extension subtag after singleton.
- Semantics defined by extension's specification.
- Multiple extensions SHOULD be in ASCII order.

#### 2.2.7 Private Use Subtags
- Introduced by 'x'; follow all other subtags.
- Conform to subtag format (letters/digits, ≤8 chars).
- Meaning by private agreement only.
- NOT RECOMMENDED where alternatives exist.
- Also available: private use codes from ISO 639, ISO 15924, ISO 3166 (distinct from 'x' sequences).

#### 2.2.8 Grandfathered and Redundant Registrations
- Tags registered under RFC 3066 remain valid.
- Redundant tags: composable from subtags; type 'redundant'.
- Grandfathered: regular (match langtag production) or irregular (do not match).
- Many superseded; their record contains 'Preferred-Value'.

#### 2.2.9 Classes of Conformance
- **Well-formed**: conforms to ABNF.
- **Valid**: well-formed + all subtags in IANA registry (as of a date) + no duplicate variants/singletons; either grandfathered or subtag-derived.
- Validity depends on registry date.
- Tags valid under RFC 3066 are still well-formed and valid.
- Private use sequences must not use unregistered subtags outside 'x' or private use ranges.

## 3. Registry Format and Maintenance
IANA Language Subtag Registry contains all valid subtags. Format: record-jar with UTF-8 encoding, NFC normalization.

### 3.1 Format of IANA Language Subtag Registry
#### 3.1.1 File Format
- Records separated by "%%".
- Fields: field-name : field-body (folded at 72 bytes).
- ASCII printable except where noted.
- Ranges indicated by "..".
- Dates: full-date per RFC 3339.

#### 3.1.2 Record and Field Definitions
Three record types: File-Date, Subtag, Tag.
- Required fields per record: Type (language/extlang/script/region/variant/grandfathered/redundant), either Subtag or Tag, Description, Added.
- Optional fields: Deprecated, Preferred-Value, Prefix, Suppress-Script, Macrolanguage, Scope, Comments.

#### 3.1.3 Type Field
Values: language, extlang, script, region, variant, grandfathered, redundant.

#### 3.1.4 Subtag and Tag Fields
- Subtag: lowercase for language/extlang/variant/private; titlecase for script; uppercase for region.
- Tag: formatted per Section 2.1.1.

#### 3.1.5 Description Field
- At least one Latin-script description; may have multiple in any script.
- Used for identification; not necessarily native names.
- Descriptions must be unique within record type (with exception for deprecated equivalents).
- First description for 'language' should match ISO 639-3 Reference Name where possible.

#### 3.1.6 Deprecated Field
- Date of deprecation; if no Preferred-Value, no replacement.
- May be added/changed/removed via maintenance.

#### 3.1.7 Preferred-Value Field
- Maps to modern equivalent.
- For extlang: maps to primary language subtag.
- For non-extlang: must appear with Deprecated.
- Changes reflect source standard updates.

#### 3.1.8 Prefix Field
- Required for extlang; optional for variant.
- Indicates appropriate prefix language tag.
- For variant: may be added (broadening), but not to variants without existing prefix.
- Must not create conflicts.

#### 3.1.9 Suppress-Script Field
- Indicates script that adds no distinguishing value for that language.
- Only in language/extlang records.
- If omitted, script may be used.

#### 3.1.10 Macrolanguage Field
- Contains macrolanguage primary subtag (from ISO 639-3).
- Only in language/extlang records.

#### 3.1.11 Scope Field
- Values: macrolanguage, collection, special, private-use.
- Only in language/extlang records; omitted means individual language.

#### 3.1.12 Comments Field
- Additional information; may be changed via registration; no stability guarantee.

### 3.2 Language Subtag Reviewer
- Appointed by IESG; moderates ietf-languages list; performs maintenance.
- Decisions appealable to IESG.

### 3.3 Maintenance of the Registry
- Changes from ISO standards: Language Subtag Reviewer evaluates and follows registration process.
- Each change requires its own registration form.

### 3.4 Stability of IANA Registry Entries
- Fields Type, Subtag, Tag, Added MUST NOT change.
- Preferred-Value and Deprecated may be added/altered/removed to reflect standard changes.
- Description may be broadened but not invalidate existing tags.
- Prefix for variant may be added/modified (broadening only), never removed.
- Prefix for extlang MUST NOT change.
- Comments may be changed.
- Suppress-Script may be added/removed.
- Macrolanguage and Scope may be added/removed per ISO 639.
- Primary/extlang codes from ISO 639: entered per rules (e.g., no 2-char code if 3-char already exists).
- Reassigned codes: remain valid; new meaning may broaden but not narrow.
- Redundant/grandfathered list is permanent and immutable.

### 3.5 Registration Procedure for Subtags
- Only 'language' and 'variant' may be independently registered. Others via maintenance.
- Registration form sent to ietf-languages@iana.org; two-week review period.
- Language Subtag Reviewer accepts/rejects/extends; decisions appealable.
- Modified forms must be sent at least one week before IANA submission.
- Registration is permanent.

### 3.6 Possibilities for Registration
- Primary language: for languages not in ISO 639 (discouraged; must first attempt ISO registration).
- Variant: for dialects, orthographies, etc.
- Informational fields: Description, Comments, Deprecated, Preferred-Value, Suppress-Script, Macrolanguage, Prefix.
- ISO standard updates.

### 3.7 Extensions and the Extensions Registry
- Extensions introduced by singletons (except 'x') are assigned via RFC (IETF Review).
- Specification must meet criteria: reference this document, follow ABNF, specify canonical representation, be versioned, stable, free, etc.
- IANA maintains Extensions Registry (record-jar format).
- Extension authorities must maintain contact info.

### 3.8 Update of the Language Subtag Registry
- RFC 5645 described the initial update. Pending registrations from RFC 4646 completed under this document.

### 3.9 Applicability of the Subtag Registry
- Not sole source for UIs; does not provide relationships, fallback, or overlap info.

## 4. Formation and Processing of Language Tags
### 4.1 Choice of Language Tag
- Tag content wisely; use as precise as justified, follow Prefix and Suppress-Script.
- Script subtag SHOULD not be used unless distinguishing; never for unwritten content.
- Use Preferred-Value when available.
- Use individual language subtags in preference to collections (e.g., 'gem').
- Special codes ('mul', 'und', 'zxx', 'mis') used sparingly.
- Variant subtags ordered per Prefix fields; general-purpose variants last.
- Grandfathered "i-default" used only for default language content.

#### 4.1.1 Tagging Encompassed Languages
- Use encompassed language subtag (e.g., 'crk' over 'cr' for Plains Cree).
- Either macrolanguage or encompassed may be used.

#### 4.1.2 Using Extended Language Subtags
- Primary language subtag SHOULD be used (e.g., 'cmn' over 'zh-cmn').
- Extlang form available for compatibility.
- Macrolanguage may still be used.

### 4.2 Meaning of the Language Tag
- Meaning relates to subtags; does not guarantee content specifics.
- Validity does not guarantee real-world usage.
- Tags do not depend on context; relationship with content varies.

### 4.3 Lists of Languages
- A single content item may have multiple language tags (e.g., multipart, metadata).

### 4.4 Length Considerations
- No upper limit on tag length.
- Implementations may refuse to store tags exceeding a specified length; MUST support at least 35 characters.
- Truncation MUST remove rightmost subtags entirely, including hyphens; if ends with singleton, remove that as well.

### 4.5 Canonicalization of Language Tags
- Steps: order extensions, replace grandfathered/redundant with Preferred-Value, replace subtag with Preferred-Value.
- Canonical form has no extlang subtags.
- Extlang form: canonicalize then prepend prefix if applicable.
- Case normalization is optional.

### 4.6 Considerations for Private Use Subtags
- Private use subtags have no meaning outside private agreement.
- Private use codes from ISO (e.g., 'Qaaa', 'AA') are RECOMMENDED over 'x' sequences for public interchange.

## 5. IANA Considerations
### 5.1 Language Subtag Registry
- IANA updated per RFC 5645. Future: insert/modify records per Language Subtag Reviewer; archive forms; announce changes to ietf-languages-announcements@iana.org.

### 5.2 Extensions Registry
- IANA inserts records per IESG request; updates contact info per maintaining authority.

## 6. Security Considerations
- Language tags may reveal sender's nationality; application protocols should evaluate threat (see BCP 72).
- Tags do not indicate content script; do not provide homograph protection.
- Implementations must guard against buffer overflow (tag length unlimited).
- Dependency on registries may enable denial-of-service; use conditional GET for updates.

## 7. Character Set Considerations
- Tags use ASCII characters only; may be used in other encodings (e.g., UTF-16).
- Rendering based on language tag may improve font selection.

## 8. Changes from RFC 4646
- Added ISO 639-3 and ISO 639-5 codes; permanently reserved extlang positions.
- ABNF updated: grandfathered tags now listed explicitly; 'grandfathered' production removed.
- Added "collection" scope; clarified capitalization rules; added Suppress-Script modification possibility.
- Modified requirements for Description uniqueness, well-formedness, variant duplication.

## 9. References
- Normative: ISO standards, RFCs, Unicode.
- Informative: RFC 1766, 2046, 2616, 3066, 3282, 3552, 3629, 4645, 5645, CLDR, UTS35, etc.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Language tags MUST use only characters A-Z, a-z, 0-9, hyphen | shall | Section 2.1 |
| R2 | Tags are case-insensitive; conventional capitalization RECOMMENDED | shall & should | Section 2.1.1 |
| R3 | Primary language subtag must be first (except 'x', 'i') | shall | Section 2.2.1 |
| R4 | If a 2-char code exists for a language, only that code is used; 3-char codes not added later | must not | Section 2.2.1 |
| R5 | Extended language subtag MUST have exactly one Prefix and identical Preferred-Value | shall | Section 2.2.2 |
| R6 | Script subtag SHOULD be omitted when not distinguishing | should | Section 2.2.3 |
| R7 | Region subtag MUST be unique; MAY be omitted | shall & may | Section 2.2.4 |
| R8 | Variant subtags MUST be registered, meet length constraints, and not duplicate | shall | Section 2.2.5 |
| R9 | Extension singleton MUST not be repeated in a tag | shall | Section 2.2.6 |
| R10 | Private use subtags MUST follow all other subtags; not recommended for general interchange | shall & should | Section 2.2.7 |
| R11 | A tag is valid if well-formed, subtags in registry, no duplicates | shall | Section 2.2.9 |
| R12 | Registry fields Type, Subtag, Tag, Added MUST NOT change | shall | Section 3.4 |
| R13 | Registration form requires two-week review period | shall | Section 3.5 |
| R14 | Implementation MUST support at least 35-character tags | shall | Section 4.4.1 |
| R15 | Truncation MUST remove complete subtags from right | shall | Section 4.4.2 |
| R16 | Canonicalization MUST apply Preferred-Value and order extensions | shall | Section 4.5 |
| R17 | Private use subtags SHOULD use ISO private use codes over 'x' sequences | should | Section 4.6 |

## Informative Annexes (Condensed)
- **Appendix A (Examples)**: Illustrates various tag types: simple, script, region, variant, private use, extensions, invalid examples.
- **Appendix B (Registration Forms)**: Examples of completed forms for variant subtags 'biske' and 'tarask'.
- **Appendix C (Acknowledgements)**: Lists contributors to the document, including editors, reviewers, and earlier RFC authors.