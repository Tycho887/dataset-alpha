# RFC 5645: Update to the Language Subtag Registry
**Source**: IETF | **Version**: Informational | **Date**: September 2009 | **Type**: Informational
**Original**: https://datatracker.ietf.org/doc/rfc5645/

## Scope (Summary)
This memo defines the procedure used to update the IANA Language Subtag Registry, in conjunction with the publication of RFC 5646, for use in forming tags for identifying languages. It describes the addition of approximately 7,500 new language subtags (based on ISO 639-3 and ISO 639-5) and seven new region subtags (based on ISO 3166-1 exceptionally reserved codes), plus modifications to existing entries and deprecation of certain grandfathered and redundant tags.

## Normative References
- [ISO639-3] "ISO 639‑3:2007. Codes for the representation of names of languages - Part 3: Alpha-3 code for comprehensive coverage of languages", February 2007.
- [ISO639-5] "ISO 639‑5:2008. Codes for the representation of names of languages -- Part 5: Alpha-3 code for language families and groups", May 2008.
- [RFC5646] Phillips, A., Ed. and M. Davis, Ed., "Tags for Identifying Languages", RFC 5646, September 2009.
- [iso-639-3_20090210] ISO 639-3 Code Set, February 2009.
- [iso-639-3_Name_Index_20090210] ISO 639-3 Language Names Index, February 2009.
- [iso-639-3-macrolanguages_20090120] ISO 639-3 Macrolanguage Mappings, January 2009.
- [iso639-5.tab.txt] ISO 639-5 code list, Tab-delimited text, February 2009.

## Definitions and Abbreviations
- **Grandfathered tag**: A complete tag registered under RFC 1766 or RFC 3066 that remains valid and cannot be generated from a valid combination of subtags.
- **Redundant tag**: A complete tag registered under RFC 1766 or RFC 3066 that remains valid but can be generated from a valid combination of subtags.
- **Extended language subtag (extlang)**: A subtag that extends a primary language subtag, used for languages encompassed by a macrolanguage or for sign languages.
- **Macrolanguage**: A language code that encompasses multiple individual languages, as defined in ISO 639-3.
- **Preferred-Value**: The subtag or tag that should be used in place of a deprecated subtag or tag.

## Updating the Registry

### 2.1. Starting Point
- The version of the Language Subtag Registry current at the time of IESG approval of this memo served as the starting point.
- Source data for ISO 639‑3: three files from the Registration Authority (version in place on February 24, 2009).
- Source data for ISO 639‑5: one file from the Registration Authority (version in place on February 24, 2009).
- Language code elements already retired in all source standards prior to IESG approval were not considered.
- File‑Date, Added, and Deprecated dates were set to a date as near as practical to the date of IESG approval.

### 2.2. New Language Subtags
- **Rule**: For each language in ISO 639‑3 not already represented by a language subtag in the registry, a new language subtag shall be added using the ISO 639‑3 code element as the Subtag field and using each non‑inverted ISO 639‑3 name as a separate Description field. The reference name shall be the first Description.
- **Extlang**: If the language is encompassed by one of the macrolanguages 'ar', 'kok', 'ms', 'sw', 'uz', or 'zh' (as per macrolanguage file), an extended language subtag shall be added with the macrolanguage's primary subtag as the Prefix. These macrolanguage subtags were determined by the LTRU Working Group to have been used to represent a single dominant language as well as the macrolanguage.
- **Sign languages**: If the language name includes the word "Sign", an extended language subtag shall be added with Prefix "sgn".
- **Preferred-Value**: All extended language subtags shall have a Preferred‑Value equal to the corresponding primary language subtag.
- **Macrolanguage field**: If the language is encompassed by a macrolanguage, a Macrolanguage field shall be added with the value of the macrolanguage subtag. (No Macrolanguage field for sign language subtags.)
- **Scope**: If the language has Scope 'M' (Macrolanguage) in the ISO 639‑3 data, Scope "macrolanguage" shall be added; if Scope 'S' (Special), Scope "special" shall be added. Most languages (Scope 'I') shall not be assigned a Scope.
- **ISO 639‑5**: For each language in iso639-5.tab.txt not already represented, a new language subtag shall be added using the code element as Subtag and the English name as Description, with Scope "collection".
- **Order**: All subtags shall be added in alphabetical order within each type: 2‑letter language subtags first, then 3‑letter language subtags, then extlang subtags. Existing records may be moved to achieve this order.

### 2.3. Modified Language Subtags
- **Description fields**: For each language in ISO 639‑3 already represented, Description fields shall be added to reflect all non‑inverted names from the Name Index. Existing Description fields that are inverted or are a strict subset of ISO 639‑3 information shall be deleted.
- **Order**: The reference name from ISO 639‑3 shall be first, followed by other ISO 639‑3 names in the order presented, then any other existing names. This may cause reordering even without new values.
- **Macrolanguage field**: For languages encompassed by a macrolanguage in ISO 639‑3, a Macrolanguage field shall be added.
- **ISO 639‑5 adjustments**: For languages already represented, the Description shall be adjusted to match the English name in iso639-5.tab.txt. Inverted names shall be rearranged to remove inversion. Scope "collection" shall be assigned. Existing subtags identified by the ISO 639‑3 Registration Authority as representing collections shall also be assigned Scope "collection".
- **Scope "private‑use"**: The record with Subtag 'qaa..qtz' shall have Scope "private‑use". Its Description was changed from "PRIVATE USE" to "Private use". Similar capitalization for script and region private‑use subtags.

### 2.4. New Region Subtags
- **Exceptionally reserved codes**: RFC 5646 expands region subtags to include ISO 3166‑1 exceptionally reserved code elements. Nine such codes existed at time of IESG approval.
- **Exclusions**:
  - 'FX' (Metropolitan France) was already present (deprecated with Preferred‑Value "FR").
  - 'UK' (United Kingdom) was not added because it shares the same UN M.49 code (826) as existing subtag 'GB', per RFC 5646 Section 3.4 item 15(D): a new region subtag shall not be added if it carries the same meaning as an existing region subtag.

### 2.5. Grandfathered and Redundant Tags
- **Reclassification**: Adding new subtags caused some grandfathered tags to become composable; they were reclassified as redundant and deprecated with a generative tag as Preferred‑Value.
  - Deprecated with Preferred‑Value: `zh-cmn` → `cmn`, `zh-cmn-Hans` → `cmn-Hans`, `zh-cmn-Hant` → `cmn-Hant`, `zh-gan` → `gan`, `zh-wuu` → `wuu`, `zh-yue` → `yue`.
- **Deprecated grandfathered tags with Preferred‑Value**:
  - `i-ami` → `ami`, `i-bnn` → `bnn`, `i-pwn` → `pwn`, `i-tao` → `tao`, `i-tay` → `tay`, `i-tsu` → `tsu`, `zh-hakka` → `hak`, `zh-min-nan` → `nan`, `zh-xiang` → `hns`.
  - `zh-min` (no Preferred‑Value) – deprecated because it represents a class of Chinese languages not useful as a tag; the ISO 639‑3 code element 'min' is Minangkabau, unrelated.
- **Sign language tags deprecated with Preferred‑Value** (list of 21 tags, e.g., `sgn-US` → `ase`).
- **No change** to Description fields of grandfathered/redundant tags. The sign language tags remain an exception to the principle of deriving meaning from component subtags.
- **Comments field**: Previous comments of the form "replaced by ISO code xxx" were deleted as duplicating Preferred‑Value. No other Comments fields were changed.

### 2.6. Preferred‑Value Changes
- **Update chain**: Preferred‑Value fields for `i-hak` (changed from `zh-hakka` to `hak`) and `zh-guoyu` (changed from `zh-cmn` to `cmn`) were updated so consumers need not follow a chain of Preferred‑Values.

### 2.7. Additional Changes
- **Script subtags**: Description fields containing alternative names (e.g., "Han (Hanzi, Kanji, Hanja)") were split into multiple Description fields. Parenthetical explanatory material was left unchanged.
- **Region subtags**: No splitting applicable because ISO 3166‑1 and UN M.49 do not provide freely available alternative names.
- **Inverted names**: Description fields in inverted form for script and region subtags were rearranged (e.g., "Korea, Republic of" → "Republic of Korea").
- **Capitalization**: Subtag fields for `sgn-BE-fr`, `sgn-BE-nl`, `sgn-CH-de`, and `yi-latn` were modified to conform to RFC 5646 Section 2.1.1 (no effect on validity or meaning). Description for subtag 'sgn' was capitalized to "Sign languages".
- **Deprecated date correction**: Region subtag TP date corrected from 2002‑11‑15 to 2002‑05‑20 to fix a clerical error.
- **Field ordering**: Order of fields within records was adjusted to match RFC 5646 Section 3.1.2 (not required; may not persist).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | For each new ISO 639‑3 language, a language subtag shall be added using the code element and non‑inverted names. | shall | Section 2.2 |
| R2 | Extended language subtags shall be added for languages encompassed by specified macrolanguages or containing "Sign". | shall | Section 2.2 |
| R3 | All extended language subtags shall have a Preferred‑Value equal to the primary language subtag. | shall | Section 2.2 |
| R4 | Macrolanguage field shall be added for languages encompassed by a macrolanguage (except sign languages). | shall | Section 2.2 |
| R5 | Scope "macrolanguage", "special", or "collection" shall be added as appropriate per ISO 639‑3/5 data. | shall | Section 2.2 |
| R6 | For existing ISO 639‑3 language subtags, Description fields shall be updated to reflect non‑inverted names; inverted or subset descriptions shall be deleted. | shall | Section 2.3 |
| R7 | For existing ISO 639‑5 language subtags, Description shall match the English name; inverted names shall be rearranged; Scope "collection" shall be assigned. | shall | Section 2.3 |
| R8 | New region subtags based on ISO 3166‑1 exceptionally reserved codes shall not be added if they carry the same meaning as an existing region subtag. | shall | Section 2.4 (RFC 5646 §3.4) |
| R9 | Grandfathered tags that become composable shall be reclassified as redundant and deprecated with a generative Preferred‑Value. | shall | Section 2.5 |
| R10 | Preferred‑Value fields may be updated to eliminate chains of references. | must | Section 2.6 |
| R11 | Script subtag Description fields containing alternative names shall be split into multiple fields; inverted names shall be rearranged. | shall | Section 2.7 |
| R12 | Capitalization of grandfathered tag subtag fields shall be modified to conform to RFC 5646 §2.1.1. | shall | Section 2.7 |
| R13 | Field order within records shall be adjusted to match RFC 5646 §3.1.2 (not required). | should | Section 2.7 |

## Informative Annexes (Condensed)
- **Appendix A: Acknowledgements**: This memo is a collaborative work of the LTRU Working Group. Key contributors include Stephane Bortzmeyer, John Cowan, Mark Davis, Martin Duerst, Frank Ellermann, Debbie Garside, Kent Karlsson, Gerard Lang, Addison Phillips, Randy Presuhn, and CE Whitehead.