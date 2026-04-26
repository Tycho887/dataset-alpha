# RFC 3023: XML Media Types
**Source**: IETF (Standards Track) | **Version**: Obsoletes RFC 2376, Updates RFC 2048 | **Date**: January 2001 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc3023/

## Scope (Summary)
This document standardizes five MIME media types for XML entities (text/xml, application/xml, text/xml-external-parsed-entity, application/xml-external-parsed-entity, application/xml-dtd) and a naming convention using the '+xml' suffix for XML-based media types. It also addresses charset handling, byte order marks (BOM), fragment identifiers, base URIs, and security considerations.

## Normative References
- [XML] Bray, T., et al., "Extensible Markup Language (XML) 1.0 (Second Edition)", W3C Recommendation REC-xml, October 2000.
- [RFC2045] Freed, N. and N. Borenstein, "MIME Part One: Format of Internet Message Bodies", RFC 2045.
- [RFC2046] Freed, N. and N. Borenstein, "MIME Part Two: Media Types", RFC 2046.
- [RFC2048] Freed, N., et al., "MIME Part Four: Registration Procedures", RFC 2048.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119.
- [RFC2279] Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 2279.
- [RFC2396] Berners-Lee, T., et al., "Uniform Resource Identifiers (URI): Generic Syntax", RFC 2396.
- [RFC2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616.
- [RFC2781] Hoffman, P. and F. Yergeau, "UTF-16, an encoding of ISO 10646", RFC 2781.
- [RFC1874] Levinson, E., "SGML Media Types", RFC 1874.
- [RFC2518] Goland, Y., et al., "HTTP Extensions for Distributed Authoring -- WEBDAV", RFC 2518.
- [RFC2703] Klyne, G., "Protocol-independent Content Negotiation Framework", RFC 2703.
- [ASCII] "US-ASCII", ANSI X3.4-1986.
- [ISO8859] ISO-8859-1:1987.

## Definitions and Abbreviations
- **XML MIME entity**: An XML entity encapsulated in a MIME entity (per RFC 2045 entity definition vs. XML entity definition).
- **UTF-16 family**: The charsets "utf-16", "utf-16le", and "utf-16be" as defined in RFC 2781.
- **BOM**: Byte Order Mark (0xFE 0xFF or 0xFF 0xFE) used for UTF-16.
- **Key words (RFC 2119)**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL.
- **Document entity**: An XML document entity.
- **External DTD subset**: Part of a DTD stored externally.
- **External parsed entity**: An XML entity that is parsed and referenced.
- **External parameter entity**: A parameter entity used in DTDs.

## 3. XML Media Types
### 3.1 Text/xml Registration
- **Type**: text
- **Subtype**: xml
- **Mandatory parameters**: none
- **Optional parameters**: charset (STRONGLY RECOMMENDED; recommended value "utf-8" for general use, "utf-16" over HTTP)
- **Charset handling**: If omitted, default is "us-ascii" (even over HTTP). Charset parameter is authoritative; recipients SHOULD preserve charset info if not UTF-8/UTF-16.
- **Encoding considerations**: MAY use quoted-printable or base64 for 7-bit transports; UTF-16 allowed only over HTTP; HTTP no Content-Transfer-Encoding needed.
- **Security considerations**: See Section 10.
- **Interoperability**: XML interoperable across WebDAV and authoring tools; validating processors recommended.
- **Published specification**: XML 1.0 (Second Edition) [XML].
- **Applications**: Web user agents, WebDAV clients/servers, XML authoring tools.
- **Magic number(s)**: None; often begins with hex 3C 3F 78 6D 6C ("<?xml") for ASCII-compatible charsets, or BOM + "<?xml" for UTF-16.
- **File extension(s)**: .xml
- **Macintosh File Type Code(s)**: "TEXT"
- **Intended usage**: COMMON

### 3.2 Application/xml Registration
- **Type**: application
- **Subtype**: xml
- **Optional parameters**: charset (STRONGLY RECOMMENDED; recommended "utf-8" and "utf-16")
- **Charset handling**: If omitted, XML processors MUST follow XML 1.0 Section 4.3.3; MIME processors SHOULD NOT assume a default. Charset parameter authoritative; same storage caution as 3.1.
- **Encoding considerations**: For 7-bit or 8-bit clean transports, must encode (base64 for UTF-16); binary clean (HTTP) no encoding.
- **Security considerations**: See Section 10.
- **Interoperability**: Same as 3.1.
- **Published specification**: Same as 3.1.
- **Applications**: Same as 3.1.
- **Additional information**: Same as 3.1.
- **Intended usage**: COMMON

### 3.3 Text/xml-external-parsed-entity Registration
- **Type**: text
- **Subtype**: xml-external-parsed-entity
- **Optional parameters**: charset (handled same as text/xml, Section 3.1)
- **Encoding considerations**: Same as 3.1.
- **Security considerations**: See Section 10.
- **Interoperability**: External parsed entities are as interoperable as XML documents but lack standalone declarations/DTDs; use of separate content type enhances interoperability.
- **Published specification**: Same as 3.1.
- **Applications**: Same as 3.1.
- **File extension(s)**: .xml or .ent
- **Macintosh File Type Code(s)**: "TEXT"
- **Intended usage**: COMMON

### 3.4 Application/xml-external-parsed-entity Registration
- **Type**: application
- **Subtype**: xml-external-parsed-entity
- **Optional parameters**: charset (handled same as application/xml, Section 3.2)
- **Encoding considerations**: Same as 3.2.
- **Security considerations**: See Section 10.
- **Interoperability**: Same as 3.3.
- **Published specification**: Same as 3.1.
- **Applications**: Same as 3.1.
- **File extension(s)**: .xml or .ent
- **Macintosh File Type Code(s)**: "TEXT"
- **Intended usage**: COMMON

### 3.5 Application/xml-dtd Registration
- **Type**: application
- **Subtype**: xml-dtd
- **Optional parameters**: charset (handled same as application/xml, Section 3.2)
- **Encoding considerations**: Same as 3.2.
- **Security considerations**: See Section 10.
- **Interoperability**: DTDs interoperable with DTD authoring tools and XML browsers.
- **Published specification**: Same as 3.1.
- **Applications**: DTD authoring tools, XML browsers.
- **File extension(s)**: .dtd or .mod
- **Macintosh File Type Code(s)**: "TEXT"
- **Intended usage**: COMMON

### 3.6 Summary of Charset Rules
- **For text/* types (including text/xml, text/xml-external-parsed-entity, and text-based XML types using this spec)**:
  - Charset parameter strongly recommended.
  - Default when omitted: "us-ascii" (HTTP default overridden).
  - Encoding declaration irrelevant; when saving, correct encoding declaration SHOULD be inserted.
- **For application/* types (including application/xml, application/xml-external-parsed-entity, application/xml-dtd, and non-text XML types using this spec)**:
  - Charset parameter strongly recommended; if present, takes precedence.
  - If omitted, XML processors MUST follow XML 1.0 Section 4.3.3.
  - Encoding declaration may be used.

## 4. The Byte Order Mark (BOM) and Conversions to/from the UTF-16 Charset
- UTF-16 XML MIME entities MUST begin with a BOM (0xFE 0xFF or 0xFF 0xFE). The BOM is not part of the markup/data.
- When converting from UTF-16 to non-Unicode, MUST strip BOM; when converting to UTF-16, MUST add BOM.
- For "utf-16le" and "utf-16be": BOM is prohibited; MUST NOT begin with BOM, but SHOULD contain an encoding declaration. Conversion from/to "utf-16" must strip/add BOM.

## 5. Fragment Identifiers
- Semantics of fragment identifiers (after “#”) depend on media type. No established specifications define identifiers for XML media types; current work in W3C on XPointer (http://www.w3.org/TR/xptr).

## 6. The Base URI
- Relative URI references depend on base URI (precedence order: embedded base URI, encapsulating MIME entity base URI, retrieval URI, application default). No established mechanism for embedding base URI in XML; W3C XML Base Proposed Recommendation (http://www.w3.org/TR/xmlbase).

## 7. A Naming Convention for XML-Based Media Types
- **Convention**: New XML-based media types SHOULD use '+xml' suffix (e.g., application/foo+xml). This enables generic XML processing (browsing, editing, fragment identification, linking, searching, storage, well-formedness checking).
- **Exceptions**: Types that do not use '+xml' will be opaque to generic XML processors; registrants SHOULD use convention unless compelling reason not to.
- **HTTP Accept header**: MUST NOT use pattern "*/*+xml" (Section 14.1 of RFC 2616). Content negotiation via RFC 2703 may be used.
- **Registration process**: Updated from RFC 2048; registrars for IETF tree and other trees SHOULD follow convention. Media subtypes that are not XML MUST NOT use '+xml' suffix.

### 7.1 Referencing
- New XML-based types under "text" SHOULD define charset/encoding as "Same as text/xml as specified in RFC 3023".
- Under other top-level types: "Same as application/xml as specified in RFC 3023".
- Use of charset parameter strongly recommended.
- Security considerations SHOULD reference RFC 3023 plus type-specific.
- SHOULD reference RFC 3023 for magic numbers, fragment identifiers, base URIs, BOM.
- MAY reference text/xml registration for interoperability considerations.

## 8. Examples (Summarized)
- **8.1-8.5**: Examples illustrate correct and incorrect usage of charset parameters for text/xml and application/xml, including UTF-8, UTF-16, UTF-16BE, ISO-2022-KR, omitted charset.
- **8.6-8.14**: Examples for application/xml, application/xml-external-parsed-entity, and application/xml-dtd with various charsets.
- **8.16-8.19**: Examples of XML-based media types using '+xml' suffix: application/mathml+xml, application/xslt+xml, application/rdf+xml, image/svg+xml. Note: these types were not yet registered; convention SHOULD be followed after registration.
- **8.20**: INCONSISTENT EXAMPLE: charset parameter in header differs from encoding declaration; MIME/XML processors MUST treat header as authoritative. Processors MUST NOT label conflicting charset info.

## 9. IANA Considerations
- This document updates RFC 2048 registration process for XML-based MIME types (see Section 7).

## 10. Security Considerations (Condensed)
- XML inherits security considerations from SGML (RFC 1874). XML MIME entities may contain commands, execute unauthorized operations.
- External resources (CSS, XSLT, DTDs) can be insecure; modification of shared resources can cause attacks (e.g., whiteout attack, entity spoofing).
- Use of digital signatures (xmldsig) may ameliorate risks.
- Security varies by domain (e.g., medical records vs. library metadata). XML can contain escape sequences that alter display processor environment; display processors SHOULD filter or reset settings.
- Recursive entity expansions are prohibited by XML; non-recursive expansions may cause resource exhaustion.
- XML parameter marshalling requires case-by-case security review.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The charset parameter for text/xml, if omitted, default is "us-ascii". | MUST | Section 3.1 (Optional parameters) |
| R2 | For application/xml, if charset parameter omitted, XML processors MUST follow XML 1.0 Section 4.3.3. | MUST | Section 3.2 (Optional parameters) |
| R3 | UTF-16 XML MIME entities MUST begin with a BOM. | MUST | Section 4 |
| R4 | When converting from UTF-16 to non-Unicode, MUST strip BOM; when converting to UTF-16, MUST add BOM. | MUST | Section 4 |
| R5 | For "utf-16le" and "utf-16be", XML MIME entities MUST NOT begin with the BOM. | MUST | Section 4 |
| R6 | New XML-based media types SHOULD use '+xml' suffix. | SHOULD | Section 7 |
| R7 | HTTP Accept header MUST NOT use pattern "*/*+xml". | MUST NOT | Section 7 |
| R8 | Media subtypes that do not represent XML MIME entities MUST NOT use '+xml' suffix. | MUST NOT | Section 7 |
| R9 | Registrations for new XML-based types under "text" SHOULD reference charset/encoding rules of text/xml from RFC 3023. | SHOULD | Section 7.1 |
| R10 | Processors generating XML MIME entities MUST NOT label conflicting charset information in MIME Content-Type and XML declaration. | MUST NOT | Section 8.20 |
| R11 | application/xml and text/xml MUST NOT be used for external parameter entities or external DTD subsets. | MUST NOT | Section 3 |
| R12 | External parsed entities SHOULD be labeled as text/xml-external-parsed-entity or application/xml-external-parsed-entity. | SHOULD | Section 3 |

## Informative Annexes (Condensed)
- **Appendix A**: Explains rationale for '+xml' suffix over alternatives (e.g., using a parameter, new subtree, top-level MIME type, sniffing, conneg). Conclusion: suffix provides maximum functionality with minimum interoperability issues.
- **Appendix B**: Changes from RFC 2376: added external parsed entity and DTD media types, prohibition of using text/xml/application/xml for those, added utf-16le/be, added '+xml' naming convention.
- **Appendix C**: Acknowledgements to contributors of the ietf-xml-mime mailing list.