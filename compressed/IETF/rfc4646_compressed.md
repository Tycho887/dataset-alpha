# RFC 4646: Tags for Identifying Languages
**Source**: IETF (Internet Engineering Task Force) | **Version**: BCP 47 | **Date**: September 2006 | **Type**: Normative (Best Current Practice)
**Original**: https://datatracker.ietf.org/doc/rfc4646/ (obsoletes RFC 3066, which obsoleted RFC 1766)

## Scope (Summary)
This document specifies the structure, content, construction, and semantics of language tags for identifying human languages (including spoken, written, signed, or otherwise signaled) for communication purposes. It also defines IANA registration procedures for subtags, private-use mechanisms, and an extension framework.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC4234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [ISO639-1] ISO 639-1:2002, Codes for the representation of names of languages -- Part 1: Alpha-2 code.
- [ISO639-2] ISO 639-2:1998, Codes for the representation of names of languages -- Part 2: Alpha-3 code.
- [ISO15924] ISO 15924:2004, Codes for the representation of names of scripts.
- [ISO3166-1] ISO 3166-1:1997, Codes for the representation of names of countries and their subdivisions -- Part 1: Country codes.
- [UN_M.49] United Nations, "Standard Country or Area Codes for Statistical Use", Revision 4, June 1999.
- [RFC2026] Bradner, S., "The Internet Standards Process -- Revision 3", BCP 9, RFC 2026, October 1996.
- [RFC2028] Hovey, R. and S. Bradner, "The Organizations Involved in the IETF Standards Process", BCP 11, RFC 2028, October 1996.
- [RFC2434] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 2434, October 1998.
- [RFC2860] Carpenter, B., Baker, F., and M. Roberts, "Memorandum of Understanding Concerning the Technical Work of the Internet Assigned Numbers Authority", RFC 2860, June 2000.
- [RFC3339] Klyne, G., Ed. and C. Newman, "Date and Time on the Internet: Timestamps", RFC 3339, July 2002.
- [ISO10646] ISO/IEC 10646:2003, Information technology -- Universal Multiple-Octet Coded Character Set (UCS).
- [ISO646] ISO/IEC 646:1991, Information technology -- ISO 7-bit coded character set for information interchange.
- [RFC4645] Ewell, D., Ed., "Initial Language Subtag Registry", RFC 4645, September 2006. (Companion document.)
- [RFC4647] Phillips, A., Ed. and M. Davis, Ed., "Matching of Language Tags", BCP 47, RFC 4647, September 2006.

## Definitions and Abbreviations
- **Language Tag**: A sequence of subtags used to identify a language.
- **Subtag**: A component of a language tag, separated by hyphens.
- **Primary Language Subtag**: The first subtag in a tag (except for private-use or grandfathered tags). Must be from ISO 639-1 (2-letter), ISO 639-2 (3-letter), or registered (5-8 characters).
- **Extended Language Subtag (extlang)**: Reserved for future ISO 639-3 use; not yet allowed.
- **Script Subtag**: Indicates writing system (4 letters, from ISO 15924).
- **Region Subtag**: Indicates country/region (2 letters from ISO 3166-1 or 3 digits from UN M.49).
- **Variant Subtag**: Indicates additional variation (5-8 characters starting with letter, or 4+ starting with digit). Registered in IANA.
- **Extension Subtag**: Introduced by a singleton (single character) other than 'x', used for future extensions.
- **Private Use Subtag**: Introduced by singleton 'x'; meaning defined by private agreement.
- **Grandfathered Tags**: Tags registered under RFC 1766 or RFC 3066 that contain subtags not defined in the subtag registry.
- **Redundant Tags**: Tags from RFC 3066 that can be formed using the subtags defined in this document.
- **Well-formed Processor**: Checks ABNF conformance and singleton non-repetition.
- **Validating Processor**: Checks well-formedness plus validity of all subtags against a specific registry date, prefix constraints for variants/extlangs.
- **IANA Language Subtag Registry**: Machine-readable file of all valid subtags.
- **ABNF**: Augmented Backus-Naur Form (RFC 4234).

## 1. Introduction
Human languages need identification for content negotiation, processing (e.g., spell-checking, speech synthesis), and labeling. This document specifies language tags, a registration function, private-use values, and future extensions. It replaces RFC 3066. The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

## 2. The Language Tag

### 2.1. Syntax
- Language tags consist of subtags separated by hyphens. Syntax in ABNF:
  ```abnf
  Language-Tag  = langtag / privateuse / grandfathered
  langtag       = (language ["-" script] ["-" region] *("-" variant) *("-" extension) ["-" privateuse])
  language      = (2*3ALPHA [extlang]) / 4ALPHA / 5*8ALPHA
  extlang       = *3("-" 3ALPHA)     ; reserved
  script        = 4ALPHA             ; ISO 15924
  region        = 2ALPHA / 3DIGIT    ; ISO 3166 / UN M.49
  variant       = 5*8alphanum / (DIGIT 3alphanum)
  extension     = singleton 1*("-" (2*8alphanum))
  singleton     = %x41-57 / %x59-5A / %x61-77 / %x79-7A / DIGIT  ; except 'x'
  privateuse    = ("x"/"X") 1*("-" (1*8alphanum))
  grandfathered = 1*3ALPHA 1*2("-" (2*8alphanum))
  alphanum      = (ALPHA / DIGIT)
  ```
- **Case insensitivity**: Tags and subtags are case-insensitive; conventions exist but **MUST NOT** carry meaning. Recommended formatting: two-letter region uppercase, four-letter script titlecase, others lowercase.

### 2.2. Language Subtag Sources and Interpretation
- The IANA Language Subtag Registry is the source for valid subtags. Subtags are grouped by type; each type has unique length/position restrictions.

#### 2.2.1. Primary Language Subtag (First subtag)
1. Two-character subtags: from ISO 639-1.
2. Three-character subtags: from ISO 639-2.
3. 'qaa'–'qtz': reserved for private use (ISO 639-2 private use codes).
4. Four-character subtags: reserved for future standardization.
5. 5–8 character subtags: registered via Section 3.5 (discouraged; prefer ISO 639).
6. 'x' as primary subtag indicates entirely private use; all following subtags are private.
7. 'i' used in some grandfathered tags.
8. Other values **MUST NOT** be assigned except by revision of this document.
- If a language has both ISO 639-1 and ISO 639-2 codes, only the ISO 639-1 code is registered.
- If ISO 639-2/T and ISO 639-2/B differ, only Terminology code is registered.
- If ISO 639-1 later assigns a two-character code for a language that had a three-character code, the two-character code **MUST NOT** be registered (to maintain stability).

#### 2.2.2. Extended Language Subtags (Reserved)
- Three-letter subtags immediately after primary language, reserved for future ISO 639-3.
- **MUST NOT** be registered or used now. Syntax described for forward compatibility.
- If future records appear, they **MUST** include exactly one 'Prefix' field.

#### 2.2.3. Script Subtag (4 letters, ISO 15924)
- **MUST** immediately follow language and extlang subtags, before region and variants.
- Private use: 'Qaaa'–'Qabx'.
- Script subtags **MUST NOT** be registered via Section 3.5; variants may be used.
- At most one script subtag per tag. **SHOULD** be omitted when the primary language's record includes a 'Suppress-Script' field for that script.

#### 2.2.4. Region Subtag (2 letters ISO 3166 or 3 digits UN M.49)
- **MUST** follow language, extlang, script; precede all others.
- Only UN M.49 codes for macro-geographical (continental) sub-regions are registered.
- UN M.49 codes for economic groupings or other groupings **MUST NOT** be registered.
- UN numeric codes for countries with ambiguous ISO 3166 codes may be registered per Section 3.4 and 3.5.
- At most one region subtag per tag; may be omitted.
- Private use: 'AA', 'QM'–'QZ', 'XA'–'XZ', 'ZZ'.

#### 2.2.5. Variant Subtags (Registered variations)
- Not from external standards; registered via Section 3.5.
- **MUST** follow language, script, region; precede extensions/private use.
- More than one variant allowed.
- Length: starting with letter -> 5+ characters; digit -> 4+ characters.
- May have 'Prefix' fields indicating suitable language tag prefixes.

#### 2.2.6. Extension Subtags
- Introduced by a singleton (letter/digit except 'x').
- **MUST** follow at least a primary language subtag.
- Each singleton **MUST** appear at most once per tag (except in private use).
- Each subtag: 2-8 characters, letters/digits.
- **SHOULD** be canonicalized per Section 4.4 if multiple extensions exist.

#### 2.2.7. Private Use Subtags
- Introduced by singleton 'x'.
- **MUST** conform to ABNF.
- **MUST** appear after all defined subtags.
- Tag may consist solely of private use subtags.
- **NOT RECOMMENDED** where alternatives exist.

#### 2.2.8. Preexisting RFC 3066 Registrations
- All existing RFC 3066 tags remain valid, maintained as "grandfathered" or "redundant" in the registry.
- Grandfathered tags contain subtags not defined in the subtag registry; redundant tags consist entirely of defined subtags.

#### 2.2.9. Classes of Conformance
- **Well-formed processor** **MUST**:
  - Check ABNF conformance (including grandfathered).
  - Check singleton non-repetition (except 'x').
- **Validating processor** **MUST**:
  - Check well-formedness.
  - Specify registry date for validation.
  - Check that all language, script, region, variant subtags are valid in IANA registry as of that date.
  - Specify supported extension RFCs (including version/date).
  - For variants/extlangs with Prefix fields: check tag matches at least one prefix (all subtags in prefix appear in tag).

## 3. Registry Format and Maintenance

### 3.1. Format of the IANA Language Subtag Registry
- Machine-readable text file using record-jar format.
- Each record fields: Type (language, extlang, script, region, variant, grandfathered, redundant), Subtag or Tag, Description, Added.
- Optional: Preferred-Value, Deprecated, Prefix, Comments, Suppress-Script.
- Case conventions: script subtags titlecase, region subtags uppercase, others lowercase.
- Descriptions are non-normative; at least one in Latin script.

### 3.2. Language Subtag Reviewer
- Appointed by IESG, moderates ietf-languages list, processes registrations.
- Decisions may be appealed to IESG.

### 3.3. Maintenance of the Registry
- Language Subtag Reviewer **MUST** update registry when ISO 639/15924/3166/UN M.49 assign or withdraw codes.
- Redundant and grandfathered tags are permanent; new entries of those types **MUST NOT** be added; existing **MUST NOT** be removed.
- Grandfathered records may be converted to redundant if all component subtags become valid.

### 3.4. Stability of IANA Registry Entries
- Fields Type, Subtag, Tag, Added, Deprecated, Preferred-Value **MUST NOT** be changed.
- Description may be broadened but not invalidate existing tags.
- Prefix may be added to variant records via registration; may be broadened but not narrowed or removed.
- Comments may be added/changed/removed.
- Suppress-Script may be added/removed via registration.
- Withdrawn ISO codes remain valid; a 'Deprecated' field is added; if replacement exists, 'Preferred-Value' added.
- Reassigned codes that conflict with existing subtags **MUST NOT** be entered; alternative subtags may be registered.

### 3.5. Registration Procedure for Subtags
- Only language and variant subtags may be registered independently.
- Registration form sent to ietf-languages@iana.org for 2-week review.
- Language Subtag Reviewer forwards to IANA or rejects with reasons.
- Registrations are permanent and stable.
- Variant registrations **SHOULD** include at least one 'Prefix' field.
- Extended language subtags are reserved and not yet registerable.

### 3.6. Possibilities for Registration
- Primary language subtags for languages not in ISO 639 (must first attempt ISO 639 registration; rejection by ISO 639 makes future IANA registration very unlikely).
- Variant subtags for dialects, orthographies, etc.
- Addition of fields to existing records (Description, Comments, Deprecated, Prefix, Suppress-Script).
- Updates reflecting ISO standard changes.

### 3.7. Extensions and Extensions Registry
- Extensions are introduced by singletons other than 'x'.
- Assigned via IETF Consensus (RFC required).
- RFC **MUST** define: canonical representation, internet-available specification, royalty-free license, versioning, stability, registration form.
- IANA maintains a registry of allocated singletons.

### 3.8. Initialization of the Registries
- Initial Language Subtag Registry from RFC 4645.
- IANA publishes as described.
- Pending RFC 3066 registrations may be completed under old rules at reviewer's discretion.
- New submissions using RFC 3066 forms after adoption rejected.
- Extension Registry initialized with placeholder.

## 4. Formation and Processing of Language Tags

### 4.1. Choice of Language Tag
- **STRONGLY RECOMMENDED** to use same tag for same language for interoperability.
- Follow Prefix and Suppress-Script fields.
- Script subtag **SHOULD** be omitted unless it adds distinguishing information.
- If a subtag has a 'Preferred-Value' field, use that value.
- 'und' (Undetermined) **SHOULD NOT** be used for labeling content; may be used in protocols requiring a tag.
- 'mul' (Multiple) **SHOULD NOT** be used unless protocol requires separate tags.
- Same variant subtag **SHOULD NOT** be repeated.

### 4.2. Meaning of the Language Tag
- Meaning depends on context: single object, aggregation, alternatives, markup.
- Tags containing a tag as a prefix are more specific (e.g., "zh-Hant-TW" more specific than "zh-Hant").
- Languages sharing prefix are not guaranteed mutually intelligible.

### 4.3. Length Considerations
- No fixed upper limit on tag length.
- Implementations **SHOULD NOT** truncate unless changing meaning or buffer limit.
- Protocols **MUST** allow at least 33 characters; **SHOULD** allow at least 42 characters.
- Derivation: 42 = language (3) + extlangs (4+4+4) + script (5) + region (4) + variant (9+9) = 42.

### 4.3.2. Truncation of Language Tags
- **MUST** remove subtags from the right, including hyphens, until fit.
- If tag ends with a singleton, remove that and preceding hyphen.

### 4.4. Canonicalization of Language Tags
- **SHOULD** be in canonical form:
  1. Well-formed per §2.1 and §2.2.
  2. Region subtags with Preferred-Value **SHOULD** be replaced.
  3. Redundant/grandfathered tags with Preferred-Value **MUST** be replaced.
  4. Other subtags with Preferred-Value **MUST** be replaced.
  5. Multiple extensions ordered case-insensitively by singleton.
- Case regularization optional (uppercase region, titlecase script, lowercase others).

### 4.5. Considerations for Private Use Subtags
- **MUST** conform to ABNF.
- No meaning outside private agreement.
- **SHOULD NOT** be used where alternatives exist or for general interchange.

## 5. IANA Considerations
- Registry initialized per RFC 4645.
- IANA **SHALL** maintain registries per procedures in this document.
- Records inserted/modified only by Language Subtag Reviewer, with new File-Date.
- Extension registry: at most 35 records, updates by IESG or maintaining authority.

## 6. Security Considerations
- Language tags may reveal sender's nationality; be aware of surveillance risks.
- Tag does not prevent homograph attacks.
- Guard against buffer overflow (no length limit; see §4.3).
- Do not mechanically depend on online availability of extension specs (DoS prevention).

## 7. Character Set Considerations
- Tags use only A-Z, a-z, 0-9, hyphen.
- Rendering based on language tag is not addressed.

## 8. Changes from RFC 3066
- Added ABNF for subtag identification without registry.
- Added well-formed vs. validating processor classes.
- Replaced language tag registry with subtag registry.
- Guarantees stability: once valid, always valid.
- Allows generative use of ISO 15924 scripts and UN M.49 regions.
- Added variant subtags.
- Defined private use tags from ISO 639/15924/3166.
- Added extension mechanism.
- Reserved extended language subtags for future ISO 639-3.
- Added canonicalization rules.

## 9. References
### 9.1. Normative References
(Listed in full above in Normative References section.)

### 9.2. Informative References
- [RFC1766], [RFC2047], [RFC2231], [RFC2781], [RFC3066], [RFC3552], [RFC4645], [RFC4647], [Unicode], [XML10], [XMLSchema], [iso639.prin], [record-jar].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Language tags MUST conform to ABNF in §2.1. | MUST | 2.1 |
| R2 | Case distinctions MUST NOT be taken to carry meaning. | MUST | 2.1 |
| R3 | Two-character subtags MUST come from ISO 639-1. | MUST | 2.2.1.1 |
| R4 | Three-character subtags MUST come from ISO 639-2. | MUST | 2.2.1.2 |
| R5 | Primary language subtags of 5-8 characters MUST be registered per §3.5. | MUST | 2.2.1.5 |
| R6 | If ISO 639-1 later assigns a code for a language already having a 3-character code, the 2-character code MUST NOT be registered. | MUST | 2.2.1 (note) |
| R7 | Extended language subtags MUST NOT be registered or used. | MUST | 2.2.2.4 |
| R8 | Extended language subtags MUST immediately follow primary subtag. | MUST | 2.2.2.2 |
| R9 | Script subtags MUST immediately follow language and extended language. | MUST | 2.2.3.2 |
| R10 | Script subtags MUST NOT be registered via §3.5. | MUST | 2.2.3.4 |
| R11 | At most one script subtag per tag. | MUST | 2.2.3.5 |
| R12 | Script subtag SHOULD be omitted if primary language has Suppress-Script. | SHOULD | 2.2.3.5 |
| R13 | Region subtags MUST follow language, extended language, script. | MUST | 2.2.4.1 |
| R14 | Two-letter region subtags MUST be from ISO 3166-1. | MUST | 2.2.4.2 |
| R15 | Three-digit region subtags MUST be from UN M.49 per rules. | MUST | 2.2.4.3 |
| R16 | UN numeric codes for economic groupings MUST NOT be registered. | MUST | 2.2.4.3.B |
| R17 | At most one region subtag per tag. | MUST | 2.2.4.5 |
| R18 | Variant subtags MUST be registered per §3.5 before use. | MUST | 2.2.5.4 |
| R19 | Variant subtags beginning with letter MUST be at least 5 characters. | MUST | 2.2.5.4.1 |
| R20 | Variant subtags beginning with digit MUST be at least 4 characters. | MUST | 2.2.5.4.2 |
| R21 | Extensions MUST follow language, script, region, variant subtags. | MUST | 2.2.6.9 |
| R22 | Singleton subtags (other than 'x') MUST appear at most once per tag. | MUST | 2.2.6.4 |
| R23 | Each singleton MUST be followed by at least one extension subtag. | MUST | 2.2.6.8 |
| R24 | Private use subtags MUST conform to ABNF. | MUST | 2.2.7.2 |
| R25 | Private use subtags MUST follow all defined subtags. | MUST | 2.2.7.3 |
| R26 | Private use subtags NOT RECOMMENDED where alternatives exist. | NOT RECOMMENDED | 2.2.7.6 |
| R27 | Well-formed processor MUST check ABNF and singleton non-repetition. | MUST | 2.2.9 |
| R28 | Validating processor MUST check well-formedness, specify registry date, validate all subtags, check prefixes for variants/extlangs. | MUST | 2.2.9 |
| R29 | New records of type 'grandfathered' or 'redundant' MUST NOT be added. | MUST | 3.3 |
| R30 | Fields Type, Subtag, Tag, Added, Deprecated, Preferred-Value MUST NOT be changed after creation. | MUST | 3.4.1 |
| R31 | If a tag/subtag has Preferred-Value, that value SHOULD be used. | SHOULD | 4.1.3 |
| R32 | Script subtag SHOULD NOT be used unless it adds distinguishing info. | SHOULD | 4.1.2 |
| R33 | Truncation MUST remove complete subtags from right, including hyphen, and if ends with singleton remove that too. | MUST | 4.3.2 |
| R34 | Canonical form: redundant/grandfathered tags with Preferred-Value MUST be replaced. | MUST | 4.4.3 |
| R35 | Other subtags with Preferred-Value MUST be replaced. | MUST | 4.4.4 |
| R36 | Extensions ordered case-insensitively by singleton. | MUST (canonicalization) | 4.4.5 |
| R37 | Registration of singletons for extensions via IETF Consensus (RFC). | MUST | 3.7 |
| R38 | Extension RFC MUST meet conditions: public domain/royalty-free, versioned, stable, etc. | MUST | 3.7 |
| R39 | Language Subtag Reviewer MUST evaluate changes from ISO standards and update registry. | MUST | 3.3 |
| R40 | Subtags must not conflict with existing subtags when adding ISO-derived codes. | MUST | 3.4.10 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgements**: Lists contributors to RFCs 1766, 3066, and this document, including editors and past Language Tag Reviewers.
- **Appendix B. Examples of Language Tags (Informative)**: Provides examples of valid tags (e.g., "de", "zh-Hant", "sr-Latn-CS", "es-419", private use "x-whatever") and invalid tags (e.g., "de-419-DE"). Also notes that extended language subtags are examples only and not yet valid.