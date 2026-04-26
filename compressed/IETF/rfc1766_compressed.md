# RFC 1766: Tags for the Identification of Languages
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: March 1995 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc1766

## Scope (Summary)
This document specifies a language tag for identifying the language used in an information object. It also defines a Content-Language header for use in RFC 822-like headers (MIME body parts, Web documents) and a new parameter (`differences`) for Multipart/Alternative to aid in language-based selection.

## Normative References
- [ISO 639] ISO 639:1988 (E/F) – Code for the representation of names of languages
- [ISO 3166] ISO 3166:1988 (E/F) – Codes for the representation of names of countries
- [RFC 1521] Borenstein, N., and N. Freed, "MIME Part One: Mechanisms for Specifying and Describing the Format of Internet Message Bodies", RFC 1521, September 1993
- [RFC 1327] Kille, S., "Mapping between X.400(1988) / ISO 10021 and RFC 822", RFC 1327, May 1992

## Definitions and Abbreviations
- **Language Tag**: A token composed of one or more parts: a primary language tag and a (possibly empty) series of subtags, syntactically defined as `Language-Tag = Primary-tag *( "-" Subtag )`, where `Primary-tag = 1*8ALPHA` and `Subtag = 1*8ALPHA`. Whitespace not allowed; case-insensitive.
- **Content-Language Header**: Used to indicate the language(s) of content in RFC-822-like headers. Syntax: `Language-Header = "Content-Language" ":" 1#Language-tag`.
- **Differences Parameter**: A parameter to Multipart/Alternative whose value is one or more of `Content-Type`, `Content-Language` (or other registered headers), indicating which headers distinguish alternatives.

## 2. The Language Tag
### 2.1. Predefined Registrations
- All 2-letter primary tags: interpreted according to ISO 639.
- Primary tag `"i"`: reserved for IANA-defined registrations.
- Primary tag `"x"`: reserved for private use; subtags of `"x"` shall not be registered by IANA.
- Other values cannot be assigned except by updating this standard.
- First subtag:
  - All 2-letter codes: interpreted as ISO 3166 alpha-2 country codes.
  - Codes of 3 to 8 letters: may be registered with IANA by anyone who needs it (see Section 5).
- Second and subsequent subtags: any value can be registered.
- **Note 1**: Language tags are case-insensitive; convention: language names in lower case, country codes in upper case (recommended but not enforced).
- **Note 2**: ISO 639 registration authority is Infoterm (address given). ISO 3166 maintenance agency is DIN (address given). Country codes AA, QM-QZ, XA-XZ, ZZ are reserved by ISO 3166 as user-assigned codes.

### 2.2. Meaning of the Language Tag
- The language tag always defines a language as spoken/written by human beings for communication. Computer languages are explicitly excluded.
- There is **no guaranteed relationship** between languages whose tags start with the same series of subtags; they are **not guaranteed to be mutually comprehensible**.
- Applications **shall always treat language tags as a single token**; division into main tag and subtags is an administrative mechanism, not a navigation aid.
- Relationship between tag and information is defined by the context standard. Examples:
  - Single object: the set of languages required for complete comprehension.
  - Aggregation (e.g., libraries): languages used inside components.
  - Alternatives (e.g., MIME multipart/alternative): a hint that material is in several languages; user must inspect alternatives.
  - Possible use in SGML DTD: e.g., `<LANG FR>...</LANG>` to allow dictionary lookup.

## 3. The Content-Language Header
- Syntax: `Content-Language: 1#Language-tag` (comma-separated list allowed). Whitespace and parenthesized comments allowed.
- Examples:
  - `Content-Language: no-nynorsk, no-bokmaal` (Norwegian official document with parallel text)
  - `Content-Language: en-cockney` (voice recording from London docks)
  - `Content-Language: i-sami-no` (Sami, no ISO 639 code)
  - `Content-Language: en, fr` (English-French dictionary)
  - `Content-Language: en, fr, de, da, el, it` (EC document)
  - `Content-Language: x-klingon` (Star Trek excerpt)

## 4. Use of Content-Language with Multipart/Alternative
- When using Multipart/Alternative, a Content-Language header **shall** be placed on each body part, and a summary Content-Language header on the Multipart/Alternative itself.

### 4.1. The `differences` Parameter to Multipart/Alternative
- A new parameter `Differences` is defined. Its value is one or more of `Content-Type`, `Content-Language` (or other registered headers). Default if not present: `Differences=Content-Type`.
- The intent: MIME readers can use these headers to intelligently choose which body part to present based on user preferences.
- Further values can be registered with IANA; they must be the name of a header defined in a published RFC.
- **Note**: Headers not beginning with "Content-" are generally ignored in body parts (per RFC 1521 section 7.2).
- The mechanism for deciding which body part to present is outside the scope of this document.
- Example provided in the document (French/German/English alternatives).

## 5. IANA Registration Procedure for Language Tags
- Any language tag **must** start with an existing tag and extend it.
- The LANGUAGE TAG REGISTRATION FORM (included in the document) **shall** be used by anyone wanting to use a tag not defined by ISO or IANA.
- The form **must** be sent to <ietf-types@uninett.no> for a 2-week review period before submitting to IANA.
- After the 2-week period, the language tag reviewer (appointed by IETF Applications Area Director) either forwards the request to IANA@ISI.EDU or rejects it due to significant objections.
- Decisions may be appealed to the IESG.
- All registered forms are available online at `ftp://ftp.isi.edu/in-notes/iana/assignments/languages/`.

## 6. Security Considerations
- Security issues are **not discussed** in this memo.

## 7. Character Set Considerations
- Codes **may always be expressed** using US-ASCII repertoire (a-z), present in most character sets.
- The issue of deciding rendering based on language tag is **not addressed**; it is thought impossible to make such a decision correctly in all cases without means of switching language mid-text.

## 8. Acknowledgements
- (Non-normative list of contributors)

## 9. Author's Address
- Harald Tveit Alvestrand, UNINETT, Norway. Email: Harald.T.Alvestrand@uninett.no

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The language tag shall be composed of a primary tag and optional subtags. | shall | Section 2 |
| R2 | Whitespace is not allowed within the tag. | shall | Section 2 |
| R3 | All tags shall be treated as case insensitive; capitalization conventions do not carry meaning. | shall | Section 2 |
| R4 | 2-letter primary tags shall be interpreted according to ISO 639. | shall | Section 2 |
| R5 | The value "i" is reserved for IANA-defined registrations. | shall | Section 2 |
| R6 | The value "x" is reserved for private use; subtags of "x" shall not be registered by IANA. | shall | Section 2 |
| R7 | Other values cannot be assigned except by updating this standard. | shall | Section 2 |
| R8 | In the first subtag, 2-letter codes shall be interpreted as ISO 3166 alpha-2 country codes. | shall | Section 2 |
| R9 | Codes of 3 to 8 letters in the first subtag may be registered with IANA. | may | Section 2 |
| R10 | In the second and subsequent subtags, any value can be registered. | may | Section 2 |
| R11 | Applications shall always treat language tags as a single token. | shall | Section 2.1 |
| R12 | When using Multipart/Alternative, a Content-Language header shall be put on each body part and a summary on the container. | shall | Section 4 |
| R13 | The `differences` parameter value shall be one or more of Content-Type, Content-Language, or other registered headers. | shall | Section 4.1 |
| R14 | If not present, Differences=Content-Type is assumed. | shall | Section 4.1 |
| R15 | Any language tag must start with an existing tag and extend it. | must | Section 5 |
| R16 | The registration form must be sent for a 2-week review period before submitting to IANA. | must | Section 5 |
| R17 | All registered forms are available online in the specified directory. | shall | Section 5 |

## Informative Annexes (Condensed)
- **Section 2 Notes**: Provide addresses of ISO 639 and ISO 3166 maintenance agencies; mention recent additions to ISO 639 (ug, iu, za, he, yi, id). These are informative background.
- **Section 3.1 Examples**: Illustrate usage of the Content-Language header; none of the subtags have been assigned (informative only).
- **Section 4.1 Example**: Demonstrates multipart/alternative with language differences; purely illustrative.
- **Acknowledgements, Author's Address, References**: Standard metadata; references are normative, acknowledgements are informative.