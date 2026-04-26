# RFC 6839: Additional Media Type Structured Syntax Suffixes
**Source**: IETF | **Version**: Informational | **Date**: January 2013 | **Type**: Informative
**Original**: http://www.rfc-editor.org/info/rfc6839

## Scope (Summary)
Defines and registers the "+json", "+ber", "+der", "+fastinfoset", "+wbxml", and "+zip" structured syntax suffixes for media type names, and provides a registration form for the "+xml" suffix per [RFC6838]. These suffixes allow media types whose representation follows a known structured syntax (e.g., JSON, BER, DER) to be identified as such, enabling generic processing when media-type-specific semantics are not required.

## Normative References
- [RFC4627] Crockford, D., "The application/json Media Type for JavaScript Object Notation (JSON)", RFC 4627, July 2006.
- [ITU.X690.2008] ITU-T Recommendation X.690 | ISO/IEC 8825-1 (2008), "ASN.1 encoding rules: Specification of basic encoding Rules (BER), Canonical encoding rules (CER) and Distinguished encoding rules (DER)", November 2008.
- [ITU.X891.2005] ITU-T Recommendation X.891 | ISO/IEC 24824-1 (2007), "Generic applications of ASN.1: Fast infoset", May 2005.
- [WBXML] Open Mobile Alliance, "Binary XML Content Format Specification", OMA WAP-192-WBXML-20010725-a, July 2001.
- [ZIP] PKWARE, Inc., "APPNOTE.TXT - .ZIP File Format Specification", Version 6.3.2, September 2007.
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies", RFC 2045, November 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3023] Murata, M., St. Laurent, S., and D. Kohn, "XML Media Types", RFC 3023, January 2001.

## Definitions and Abbreviations
- **Structured Syntax Suffix**: A suffix added to a media type name (e.g., "+json") that indicates the underlying representation follows a specific syntax (e.g., JSON, XML).
- **BER**: Basic Encoding Rules (ITU-T X.690)
- **DER**: Distinguished Encoding Rules (ITU-T X.690)

## Structured Syntax Suffix Definitions

### 3.1. The +json Structured Syntax Suffix
- **Name**: JavaScript Object Notation (JSON)
- **+suffix**: +json
- **References**: [RFC4627]
- **Encoding considerations**: JSON allowed in UTF-8 (8bit compatible per [RFC2045]), UTF-16, or UTF-32 (binary per [RFC2045]).
- **Fragment identifier considerations**: Syntax and semantics for +json **SHOULD** be as specified for "application/json". For a specific "xxx/yyy+json", process as follows:
    - If defined in +json and resolves per +json rules → process as +json.
    - If defined in +json but does not resolve per +json rules → process as "xxx/yyy+json".
    - If not defined in +json → process as "xxx/yyy+json".
- **Interoperability considerations**: n/a
- **Security considerations**: See [RFC4627].
- **Contact**: Apps Area Working Group (apps-discuss@ietf.org)
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

### 3.2. The +ber Structured Syntax Suffix
- **Name**: Basic Encoding Rules (BER) transfer syntax
- **+suffix**: +ber
- **References**: [ITU.X690.2008]
- **Encoding considerations**: BER is a binary encoding.
- **Fragment identifier considerations**: No fragment identification syntax defined for +ber at publication. Processing rules follow the same three-case logic as +json (replacing +json with +ber).
- **Interoperability considerations**: n/a
- **Security considerations**: 
    - Each individual +ber media type may have additional security considerations.
    - BER type-length-value structure can cause buffer overruns; arbitrary nesting may cause stack overflows. Interpreters **SHOULD** guard against these.
- **Contact**: Apps Area Working Group
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

### 3.3. The +der Structured Syntax Suffix
- Identical structure to +ber, with "DER" substituted. **+suffix**: +der. References: [ITU.X690.2008]. Encoding: binary. Fragment identifier considerations: same three-case logic. Security considerations: same as +ber.

### 3.4. The +fastinfoset Structured Syntax Suffix
- **Name**: Fast Infoset document format
- **+suffix**: +fastinfoset
- **References**: [ITU.X891.2005]
- **Encoding considerations**: Binary encoding; binary, quoted-printable, and base64 Content-Transfer-Encodings are suitable.
- **Fragment identifier considerations**: **SHOULD** be as specified for "application/fastinfoset". Three-case logic similar to +json.
- **Security considerations**: No inherent security considerations; individual media types may add their own.
- **Contact**: Apps Area Working Group
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

### 3.5. The +wbxml Structured Syntax Suffix
- **Name**: WAP Binary XML (WBXML) document format
- **+suffix**: +wbxml
- **References**: [WBXML]
- **Encoding considerations**: Binary encoding.
- **Fragment identifier considerations**: **SHOULD** be as specified for "application/vnd.wap.wbxml". Three-case logic.
- **Security considerations**: No inherent security considerations; individual media types may add their own.
- **Contact**: Apps Area Working Group
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

### 3.6. The +zip Structured Syntax Suffix
- **Name**: ZIP file storage and transfer format
- **+suffix**: +zip
- **References**: [ZIP]
- **Encoding considerations**: Binary encoding.
- **Fragment identifier considerations**: **SHOULD** be as specified for "application/zip". Three-case logic.
- **Security considerations**: ZIP supports two encryption forms (Strong Encryption and AES 128/192/256-bit). Individual media types may add own.
- **Contact**: Apps Area Working Group
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

### 4.1. The +xml Structured Syntax Suffix (Registration per RFC3023 and [RFC6838])
- **Name**: Extensible Markup Language (XML)
- **+suffix**: +xml
- **References**: [RFC3023]
- **Encoding considerations**: XML allowed in 7-bit and 8-bit encodings. UTF-8 is 8bit compatible; UTF-16/32 are binary per [RFC2045].
- **Fragment identifier considerations**: **SHOULD** be as specified for "application/xml" (see [RFC3023] Sections 5 and 7). Three-case logic.
- **Interoperability considerations**: See [RFC3023].
- **Security considerations**: See [RFC3023].
- **Contact**: Apps Area Working Group
- **Author/Change controller**: Apps Area Working Group; IESG has change control.

## Security Considerations (Summary)
- Each suffix’s security considerations are given in its registration form (Sections 3 and 4). Updates to +suffix registrations **SHOULD** be reviewed for impact on existing xxx/yyy+<suffix> media types.
- Introducing new fragment identifier processing rules or changing existing ones may break existing registrations and create interoperability/security issues. Care must be taken to avoid conflicts between generic +suffix rules and media-type-specific rules.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | +json suffix **MAY** be used with any media type whose representation follows that established for "application/json". | MAY | Sec 3.1 |
| R2 | Fragment identifier syntax for +json **SHOULD** be as specified for "application/json". | SHOULD | Sec 3.1 |
| R3 | For +json, fragment identifier processing: if defined in +json and resolves per +json rules → process as +json; if defined but does not resolve → process as specific media type; if not defined → process as specific media type. | SHOULD | Sec 3.1 |
| R4 | +ber suffix **MAY** be used with any media type whose representation follows BER transfer syntax. | MAY | Sec 3.2 |
| R5 | +der suffix **MAY** be used with any media type whose representation follows DER transfer syntax. | MAY | Sec 3.3 |
| R6 | +fastinfoset suffix **MAY** be used with any media type whose representation follows that established for "application/fastinfoset". | MAY | Sec 3.4 |
| R7 | Fragment identifier syntax for +fastinfoset **SHOULD** be as specified for "application/fastinfoset". | SHOULD | Sec 3.4 |
| R8 | +wbxml suffix **MAY** be used with any media type whose representation follows that established for "application/vnd.wap.wbxml". | MAY | Sec 3.5 |
| R9 | +zip suffix **MAY** be used with any media type whose representation follows that established for "application/zip". | MAY | Sec 3.6 |
| R10 | +xml suffix registration **SHALL** reflect info from [RFC3023] with added fragment identifier considerations. | SHALL | Sec 4.1 |
| R11 | Fragment identifier syntax for +xml **SHOULD** be as specified for "application/xml" (sections 5 and 7 of RFC3023). | SHOULD | Sec 4.1 |
| R12 | When updating a +suffix registration, existing xxx/yyy+<suffix> media types **SHOULD** be reviewed for adverse effects. | SHOULD | Sec 5 |
| R13 | When updating fragment identifier rules for a specific media type, **SHOULD** avoid conflicts with generic +suffix rules. | SHOULD | Sec 5 |

## Informative Annexes (Condensed)
- **Section 2 – When to Use These Structured Syntax Suffixes**: Suffixes are appropriate when the media type identifies semantics, but the suffix allows generic processing of the underlying representation when no special handling is needed and no special knowledge is required beyond what is needed for any example of that representation.
- **Section 5 – Security Considerations (further notes)**: Updates to +suffix fragment identifier rules can break existing registrations; careful review is required.
- **Section 6.2 – Informative References**: [RFC6838] (Media Type Specifications and Registration Procedures), [FRAGID-BP] (Best Practices for Fragment Identifiers), [XML-MEDIATYPES] (Work in Progress updating RFC3023).