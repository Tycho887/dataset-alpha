# RFC 4647: Matching of Language Tags
**Source**: IETF | **Version**: BCP 47 | **Date**: September 2006 | **Type**: Best Current Practice
**Original**: https://datatracker.ietf.org/doc/html/rfc4647

## Scope (Summary)
Defines the syntax for language ranges (identifiers used in language preference lists) and specifies three matching schemes (basic filtering, extended filtering, lookup) to compare language tags against user preferences. This document, with RFC 4646, replaces RFC 3066 (and RFC 1766).

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2277] Alvestrand, H., "IETF Policy on Character Sets and Languages", BCP 18, RFC 2277, January 1998.
- [RFC4234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [RFC4646] Phillips, A., Ed., and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 4646, September 2006.

## Definitions and Abbreviations
- **Language range**: A sequence of subtags (alphanumeric or wildcard '*') used to specify a set of language tags. Types: basic language range and extended language range.
- **Basic language range**: Syntax identical to an [RFC3066] language tag or the single character '*'. ABNF: `language-range = (1*8ALPHA *("-" 1*8alphanum)) / "*"` (digits allowed; see [RFC2616errata]).
- **Extended language range**: Allows wildcard '*' in any position to match any sequence of subtags. ABNF: `extended-language-range = (1*8ALPHA / "*") *("-" (1*8alphanum / "*"))`. Wildcards outside first position are ignored by Extended Filtering.
- **Language priority list**: A prioritized or weighted list of language ranges (e.g., "en, fr, zh-Hant"). Syntax defined by the protocol using it.
- **Filtering**: Matching scheme that produces zero or more matching language tags.
- **Lookup**: Matching scheme that produces exactly one match (the best matching tag) for a given request; falls back by progressive truncation.
- **Wildcard**: The character '*' (%x2A), matches any sequence of subtags; meaning varies by range type.
- **Singleton**: A single letter or digit subtag (including private-use 'x').

## The Language Range (Section 2)
- Language range subtags MUST be sequences of ASCII alphanumeric characters or the wildcard '*'.
- Language tags and ranges MUST be treated as case-insensitive; matching MUST be case-insensitive.

### 2.1 Basic Language Range
- Defined by ABNF: `language-range = (1*8ALPHA *("-" 1*8alphanum)) / "*"`
- No requirement for well-formedness or validation against IANA registry; ill-formed ranges will probably not match.

### 2.2 Extended Language Range
- Defined by ABNF: `extended-language-range = (1*8ALPHA / "*") *("-" (1*8alphanum / "*"))`
- Wildcard '*' can occur in any position; outside first position it is ignored by Extended Filtering.
- Presence or absence of wildcards does not imply a certain number of subtags in matching tags.

### 2.3 The Language Priority List
- Prioritized or weighted list of language ranges (e.g., Accept-Language header).
- This document does not define the syntax; protocols define it.
- Examples shown as comma-separated quoted sequence: "en, fr, zh-Hant".

## Types of Matching (Section 3)
- **MUST** clearly indicate the matching mechanism used.
- Two types: filtering (zero or more results) and lookup (exactly one result).

### 3.1 Choosing a Matching Scheme
Three schemes defined:
1. **Basic Filtering** (§3.3.1): uses basic language ranges.
2. **Extended Filtering** (§3.3.2): uses extended language ranges.
3. **Lookup** (§3.4): uses basic language ranges; returns single best match.

### 3.2 Implementation Considerations
- Protocol using matching MUST specify:
  - Type(s) of matching used.
  - Whether operation returns single result (lookup) or set (filtering).
  - For lookup: default behavior when no match found.
- Validation against IANA Subtag Registry not required; canonicalization encouraged but with caution (e.g., "art-lojban" -> "jbo" would lose original tag).
- Applications receiving extended ranges MUST either: map to basic (remove wildcards except leading '*'), reject invalid basic ranges, or treat as basic (ignores them).
- Pre-processing/configuration options allowed (e.g., mapping subtags).

### 3.3 Filtering
- Each language range is least specific acceptable match; matching tags have equal or greater number of subtags.
- Non-wildcard subtags in range must appear in matching tags.
- Results MAY be unordered.

#### 3.3.1 Basic Filtering
- Language range matches a tag if case-insensitive exact equality or exact prefix followed by '-' (e.g., "de-de" matches "de-DE-1996", not "de-Deva").
- The range "*" matches any tag; protocol MAY define special semantics.
- Identical to matching described in [RFC3066] Section 2.5.

#### 3.3.2 Extended Filtering
- Algorithm to determine match:
  1. Split range and tag into subtag lists on hyphen.
  2. Compare first subtags; if mismatch, fail.
  3. While range has more subtags:
     - If current range subtag is '*', skip to next in range.
     - If tag list exhausted, fail.
     - If subtags match, advance both.
     - If tag subtag is singleton (including 'x'), fail.
     - Otherwise advance tag subtag.
  4. When range list exhausted, match succeeds.
- Selects tags with same initial subtags and any intermediate subtags not in range (e.g., "de-*-DE" matches "de-Latn-DE").

### 3.4 Lookup
- Each language range is most specific acceptable match; truncation from end until match found.
- Single-letter or digit subtags (including 'x' and extension subtags) are removed together with their closest trailing subtag.
- Example fallback: "zh-Hant-CN-x-private1-private2" -> "zh-Hant-CN" -> "zh-Hant" -> "zh" -> default.
- The range "*" is skipped unless it is the only range; then default is returned.
- Protocols that accept extended language ranges MUST define behavior when multiple tags match (e.g., map to basic ranges, ASCII order).

#### 3.4.1 Default Values
- Protocol MUST define defaulting behavior when no tag matches (e.g., return item with no language tag, empty string, specific tag "i-default", error, etc.).
- Progressive search MUST process each language range before calculating default.
- Default MAY be configurable; if a default range is used, it is treated as appended to the end of the language priority list.

## Other Considerations (Section 4)

### 4.1 Choosing Language Ranges
- Users SHOULD select well-formed, valid language tags (per RFC 4646) as ranges.
- Canonicalization encouraged; include deprecated forms if needed.
- For filtering, fewer subtags widen match; for lookup, unnecessary subtags may cause suboptimal fallback.
- Users SHOULD avoid subtags that add no distinguishing value; script subtags SHOULD NOT be used for languages with Suppress-Script field.
- Extensions and private-use subtags SHOULD be avoided in ranges.

### 4.2 Meaning of Language Tags and Ranges
- Meanings identical to language tags (RFC 4646 §4.2) with wildcard '*' representing any sequence.

### 4.3 Considerations for Private-Use Subtags
- Private agreement required; great caution SHOULD be used in general interchange.
- Matching private-use tags can result in unpredictable content.

### 4.4 Length Considerations for Language Ranges
- Same restrictions as language tags (RFC 4646 §4.3).

## Security Considerations (Section 5)
- Language ranges can reveal nationality or be used for tracking.
- Evaluation of threat and countermeasures left to applications/protocols.

## Character Set Considerations (Section 6)
- Allowed characters (A-Z, a-z, 0-9, HYPHEN-MINUS, ASTERISK) are present in most character sets.

## References (Section 7)
- Normative: RFC 2119, RFC 2277, RFC 4234, RFC 4646.
- Informative: RFC 1766, RFC 2616, RFC 2616errata, RFC 3066, RFC 3282, XML10.

## Informative Annexes (Condensed)
- **Appendix A: Acknowledgements**: Lists numerous contributors including editors and those who contributed to precursor RFCs (1766, 3066). Special thanks to Harald Alvestrand.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Language range subtags MUST be alphanumeric or wildcard '*'; matching case-insensitive. | MUST | §2 |
| R2 | Basic language range ABNF: `language-range = (1*8ALPHA *("-" 1*8alphanum)) / "*"` | MUST | §2.1 |
| R3 | Extended language range ABNF: `extended-language-range = (1*8ALPHA / "*") *("-" (1*8alphanum / "*"))` | MUST | §2.2 |
| R4 | Protocol MUST specify matching type, result type (filter/lookup), and default for lookup. | MUST | §3.2 |
| R5 | Filtering: each range is least specific; non-wildcard subtags must appear in matching tags. | MUST | §3.3 |
| R6 | Basic Filtering: range matches tag if exact equality or prefix followed by '-'. | MUST | §3.3.1 |
| R7 | Extended Filtering algorithm as defined in §3.3.2. | MUST | §3.3.2 |
| R8 | Lookup: progressive truncation from end; singletons removed with closest trailing subtag. | MUST | §3.4 |
| R9 | Protocol using lookup MUST define default behavior when no match. | MUST | §3.4.1 |
| R10 | Applications receiving extended ranges MUST choose mapping, rejection, or basic treatment. | MUST | §3.2 |
| R11 | Users SHOULD select well-formed, valid language tags as ranges. | SHOULD | §4.1 |
| R12 | Users SHOULD avoid subtags that add no distinguishing value; script subtags SHOULD NOT be used for languages with Suppress-Script. | SHOULD | §4.1 |
| R13 | Private-use subtags: great caution SHOULD be used; prior arrangement required. | SHOULD | §4.3 |
| R14 | Implementations MAY canonicalize tags/ranges using Preferred-Value from registry. | MAY | §3.2, §4.1 |