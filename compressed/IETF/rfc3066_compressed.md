# RFC 3066: Tags for the Identification of Languages
**Source**: IETF (Internet Engineering Task Force) | **Version**: BCP 47 | **Date**: January 2001 | **Type**: Normative (Best Current Practice)
**Original**: https://tools.ietf.org/html/rfc3066 (obsoletes RFC 1766)

## Scope (Summary)
This document specifies a language tag mechanism for identifying human languages used in information objects. It defines the syntax of language tags, how to interpret subtags from ISO 639 and ISO 3166, how to register new tags with IANA, and a language-range construct for matching tags.

## Normative References
- [ISO 639] ISO 639:1988 – Code for representation of names of languages (and ISO 639-1:2000)
- [ISO 639-2] ISO 639-2:1998 – Codes for representation of names of languages – Part 2: Alpha-3 code
- [ISO 3166] ISO 3166:1988 – Codes for representation of names of countries
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC 2234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF"
- [RFC 2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1"
- [RFC 2860] Carpenter, B., et al., "Memorandum of Understanding Concerning the Technical Work of IANA"
- [RFC 2026] Bradner, S., "The Internet Standards Process -- Revision 3"
- [RFC 2028] Hovey, R. and S. Bradner, "The Organizations Involved in the IETF Standards Process"

## Definitions and Abbreviations
- **Language-Tag**: Composed of a primary subtag and zero or more subsequent subtags, separated by hyphens. Syntax: `Primary-subtag *( "-" Subtag )` with `Primary-subtag = 1*8ALPHA` and `Subtag = 1*8(ALPHA / DIGIT)`. Tags are case-insensitive.
- **Primary-subtag**: The first subtag of a language tag; interpreted based on its length: 2 letters → ISO 639; 3 letters → ISO 639-2; "i" → IANA-registered; "x" → private use.
- **Subtag**: Any subsequent tag component; 2-letter second subtags are ISO 3166 country codes; 3-8 letter second subtags may be IANA-registered.
- **Language-range**: A language tag or "*"; used for matching. Matches if exactly equal or a prefix where next character is "-". "*" matches any tag.
- **IANA**: Internet Assigned Numbers Authority
- **UND**: ISO 639 code for "Undetermined"
- **MUL**: ISO 639 code for "Multiple languages"
- **RA-JAC**: ISO 639 Registration Authority Joint Advisory Committee

## 1. Introduction
Language identification is needed for presentation, processing (e.g., spell-check, speech synthesis), and multilingual content. This document defines an identifier mechanism, a registration function, and a matching construct. The keywords MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted as per [RFC 2119].

## 2. The Language Tag

### 2.1 Language Tag Syntax
- **Syntax**: `Language-Tag = Primary-subtag *( "-" Subtag )` as per ABNF in RFC 2234.
- **Primary-subtag**: 1 to 8 letters (A-Z, a-z).
- **Subtag**: 1 to 8 letters or digits (A-Z, a-z, 0-9).
- Tags are case-insensitive; conventions exist but carry no meaning.

### 2.2 Language Tag Sources
- The namespace is administered by IANA per Section 3.
- **Primary subtag rules**:
  - 2-letter → ISO 639 (or subsequent assignments).
  - 3-letter → ISO 639-2 (or subsequent assignments).
  - "i" reserved for IANA-defined registrations.
  - "x" reserved for private use; subtags of "x" shall not be registered.
  - Other values not assigned except by revision of this standard.
- **Second subtag rules**:
  - 2-letter → ISO 3166 alpha-2 country code.
  - 3 to 8 letters → may be IANA-registered per Section 5.
  - 1-letter → not allowed except after revision.
- Third and subsequent subtags have no rules beyond syntax.
- Tags formed solely from codes assigned interpretations in this section do not need IANA registration.
- Examples: en-US (country), en-scouse (dialect), i-tsolyani (unlisted language), sgn-US-MA (region).
- **ISO 3166 user-assigned codes (AA, QM-QZ, XA-XZ, ZZ) MUST NOT be used.**

### 2.3 Choice of Language Tag
- Interoperability best served by using the same tag for the same language across all documents.
- If application requirements deviate, the protocol specification MUST specify how the procedure varies.
- **Rules**:
  1. Use the most precise tagging known and useful.
  2. **MUST** use ISO 639-1 2-character code if available; otherwise use ISO 639-2.
  3. If ISO 639-2/T (Terminology) and ISO 639-2/B (Bibliographic) differ, **MUST** use Terminology code.
  4. If both IANA-registered (i-something) and ISO tag exist, **MUST** use ISO tag; IANA tag SHOULD be deprecated.
  5. **SHOULD NOT** use UND unless forced; omitting tag is preferred.
  6. **SHOULD NOT** use MUL if protocol allows multiple languages (e.g., Content-Language header).
- Note: RA-JAC policy states no new 2-letter code added to ISO 639-1 unless a 3-letter code added simultaneously to ISO 639-2, and no language with 3-letter code at publication of ISO 639-1 shall get 2-letter code later.

### 2.4 Meaning of the Language Tag
- Defines a language as spoken/written/signed by human beings. Computer languages excluded.
- No guaranteed mutual intelligibility between tags sharing prefixes.
- Examples of usage:
  - Single object: set of languages required for complete comprehension.
  - Aggregation: languages used within components.
  - Alternatives (e.g., multipart/alternative): hint that content is available in multiple languages.
  - In markup: language info added per part; e.g., `<span lang="FR">`.

### 2.5 Language-Range
- **language-range** = language-tag / "*"
- Matches exactly or prefix where first character after prefix is "-".
- "*" matches any tag; protocols may define additional semantics (e.g., HTTP/1.1).
- Prefix matching does not imply that understanding a language tag implies understanding all its prefix-based variants.

## 3. IANA Registration Procedure
- **MUST** be used for tags not given interpretation in Section 2.2 or previously registered.
- **MAY** also be used to register info about tags defined by this document (e.g., sgn-US).
- Tags with first subtag "x" need not and cannot be registered.
- **Process**:
  1. Fill out registration form (requester name/email, tag, English name, native name, reference to published description, any other relevant info).
  2. Send to `ietf-languages@iana.org` for 2-week review period.
  3. After two weeks, language tag reviewer (appointed by IETF Applications Area Director) forwards to IANA or rejects due to significant objections.
  4. Applicant may modify and resubmit; restarts 2-week comment period.
  5. Decisions appealable to IESG per RFC 2026 and RFC 2028.
- Registered forms online at `http://www.iana.org/numbers.html` under "languages".
- **Updates** follow same procedure; reviewer decides about new registrant updates.
- **No deletion** – deprecated tags add remark "DEPRECATED: use <new code> instead".
- Purpose of "published description" is to aid verification; reviewer decides sufficiency.

## 4. Security Considerations
- Language ranges in content negotiation may reveal nationality, potential surveillance target.
- This is a general visibility issue; evaluation and countermeasures left to each application protocol.

## 5. Character Set Considerations
- Tags use characters A-Z, a-z, 0-9, hyphen, present in most character sets.
- Rendering decisions based on language tag are not addressed; may require language switching definitions.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Use ISO 639-1 2-character code if available; otherwise use ISO 639-2. | MUST | Section 2.3(2) |
| R2 | If ISO 639-2/T and ISO 639-2/B differ, use Terminology code. | MUST | Section 2.3(3) |
| R3 | If both IANA-registered and ISO tag exist, use ISO tag; deprecate IANA tag. | MUST (use ISO) / SHOULD (deprecate) | Section 2.3(4) |
| R4 | Do not use ISO 3166 user-assigned codes (AA, QM-QZ, XA-XZ, ZZ) in language tags. | MUST NOT | Section 2.2 |
| R5 | Use the most precise tagging known and useful. | (Guidance) | Section 2.3(1) |
| R6 | SHOULD NOT use UND unless forced; omitting tag is preferred. | SHOULD NOT | Section 2.3(5) |
| R7 | SHOULD NOT use MUL if protocol allows multiple languages. | SHOULD NOT | Section 2.3(6) |
| R8 | Registration procedure must be used for tags not covered by Section 2.2 or prior registration. | MUST | Section 3 |
| R9 | Tags with first subtag "x" need not and cannot be registered. | (Exemption) | Section 3 |
| R10 | Language tags are case-insensitive. | (Interpretation) | Section 2.1 |

## Informative Annexes (Condensed)
- **Appendix A: Language Tag Reference Material**: The Library of Congress maintains ISO 639-2 list at `http://www.loc.gov/standards/iso639-2/langhome.html`. IANA registration forms at `http://www.iana.org/numbers.html` under "languages". ISO 3166 Maintenance Agency at `http://www.din.de/gremien/nas/nabd/iso3166ma/`.
- **Appendix B: Changes from RFC 1766**: Updated mailing list, author address, added language-range, ISO 639-2 use, Library of Congress reference, new examples, additional form field, update procedure, changed to BCP, removed Content-Language header definition, added permitted character numbers.