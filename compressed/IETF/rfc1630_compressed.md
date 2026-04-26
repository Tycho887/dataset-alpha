# RFC 1630: Universal Resource Identifiers in WWW
**Source**: Network Working Group (T. Berners-Lee, CERN) | **Version**: June 1994 | **Date**: June 1994 | **Type**: Informational
**Original**: http://info.cern.ch/hypertext/WWW/Addressing/URL/URI_Overview.html

## Scope (Summary)
This document defines the syntax used by the World-Wide Web initiative to encode names and addresses of objects on the Internet, establishing a universal set of Resource Identifiers (URIs). It provides a reference point for Uniform Resource Locators (URLs) and Uniform Resource Names (URNs) discussions, documenting existing practice without specifying an Internet standard.

## Normative References
- STD 11, RFC 822 – Standard for ARPA Internet Text Messages (Crocker, 1982)
- STD 9, RFC 959 – File Transfer Protocol (FTP) (Postel & Reynolds, 1985)
- RFC 1036 – Standard for Interchange of USENET messages (Horton & Adams, 1987)
- RFC 977 – Network News Transfer Protocol (NNTP) (Kantor & Lapsley, 1986)
- STD 13, RFC 1034 – Domain Names – Concepts and Facilities (Mockapetris, 1987)
- ISO-10163 – Search and Retrieve Application Protocol Specification for OSI
- Alvarez et al., “Notes on the Internet Gopher Protocol”, 1991; Davis et al., “WAIS Interface Protocol”, 1990; Neuman, “Prospero: A Tool for Organizing Internet Resources”, 1992
- Sollins & Masinter, “Requirements for URNs”, Work in Progress
- Kunze, “Requirements for URLs”, Work in Progress

## Definitions and Abbreviations
- **URI (Universal Resource Identifier)**: A member of the universal set of names in registered name spaces and addresses referring to registered protocols or name spaces.
- **URL (Uniform Resource Locator)**: A form of URI which expresses an address that maps onto an access algorithm using network protocols.
- **URN (Uniform Resource Name)**: A space of more persistent names (under development; subject of IETF working group).
- **Reserved Characters**: Characters with special meaning in URI syntax (% / # ? ; : space, etc.)
- **Unsafe Characters**: Characters such as spaces, control characters, national variant set characters, and all 8-bit characters beyond DEL (7F hex) that shall not be used unencoded in canonical form.

## General URI Syntax (Normative)

### URI Production
- `fragmentaddress := uri [ # fragmentid ]`
- `uri := scheme : path [ ? search ]`
- `scheme := ialpha`
- `path := void | xpalphas [ / path ]`
- `search := xalphas [ + search ]`
- `fragmentid := xalphas`

Where `xalpha` includes alpha, digit, safe characters ($ - _ @ . &), extra characters (! * " ' ( ) ,), and escape sequences (`% hex hex`). `ialpha` is alpha followed by optional xalphas.

### Reserved Characters and Their Uses
- **Percent sign (`%`)**: Escape character; never allowed for anything else. `%` must always be encoded when representing itself.
- **Slash (`/`)**: Reserved for delimiting hierarchical substrings. Significance: left segment is closer to root.
- **Hash (`#`)**: Delimits fragment identifier from object URI.
- **Question mark (`?`)**: Delimits boundary between URI of a queryable object and query words. Plus sign (`+`) within query string is shorthand for space; real plus signs must be encoded.
- **Asterisk (`*`) and exclamation mark (`!`)**: Reserved for scheme-specific significance.

### Encoding Reserved Characters
- **Conventional URI Encoding**: Characters not allowed in URI may be represented by `%` followed by two hexadecimal digits (0-9, A-F) giving the ISO Latin 1 code. Character codes other than those allowed shall not be used unencoded.
- **Reduced/Increased Safe Character Sets**: Encoding may be applied to unsafe characters; reserved characters must NEVER be encoded/unencoded in this way.
- **Percent sign intended as such must always be encoded**. Sequences starting with `%` not followed by two hex digits are reserved for future extension.

### Partial (Relative) URI Form
- If scheme parts differ, absolute URI must be given. Otherwise, rules for relative resolution:
  - If partial URI starts with >0 consecutive slashes, prepend context URI up to (but not including) the first occurrence of exactly the same number of consecutive slashes.
  - Otherwise, remove the last segment of context path and append partial URI.
  - Recursively remove `./` and `xxx/../` path segments.

### Fragment Identifiers
- Fragment syntax and semantics defined by application or content type; allowed characters defined in BNF. Void fragment or missing `#` means URI refers to whole object.

## Specific URI Schemes
### HTTP
- Scheme `http:`. Path is transparent to client; server handles de-reference. Search part sent as part of HTTP command. Fragment ID not sent with request. Spaces and control characters must be escaped for transmission.
### FTP
- Scheme `ftp:`. Default user `anonymous`, password user’s email address. Path segments map to CWD commands; final segment to RETR. Optional `;type=<type-code>` suffix for transfer type. Stream mode always used.
### Gopher
- Scheme `gopher:`. Includes type code (single character) and selector string (with trailing CR LF omitted). Slashes in selector may not imply hierarchy.
### Mailto
- `mailto: xalphas @ hostname` – RFC 822 addr-spec. `%` used for encoding requires `%25`
### News
- `news: groupart` – location-independent; uses NNTP. Message identifiers distinguished by `@`. Not suitable as URN due to expiry.
### Telnet, rlogin, tn3270
- Represent interactive sessions; `telnet://login`
### WAIS
- `wais://hostport/database` for index, `wais://hostport/database/wtype/wpath` for documents. Encoded fields in wpath.
### File
- `file://host/path` – local file access with host part; `localhost` indicates local machine. Void host equivalent to `localhost`.
### MID and CID
- `mid: addr-spec` – references RFC 822 Message-ID; `cid: content-identifier` – references MIME body part. `cid` only meaningful within same MIME message.

## Registration of Naming Schemes
- New schemes may be introduced with a registered prefix. Experimental prefixes must start with `x-`. `urn:` reserved for future persistent name scheme.
- IANA proposed as registration authority. Submission must include retrieval algorithm and demonstrate utility, e.g., via gateway.

## Security Considerations
Security issues are not discussed in this memo.

## BNF Summary (Condensed)
### Generic URI BNF (see document for full)
- `xalpha := alpha | digit | safe | extra | escape`
- `safe := $ | - | _ | @ | . | &`
- `extra := ! | * | " | ' | ( | ) | ,`
- `escape := % hex hex`
- `reserved := = | ; | / | # | ? | : | space`
- `national` and `punctuation` characters not allowed in URIs.

### Specific URL BNF (non-exhaustive list)
- `prefixedurl := u r l : url`
- `url := httpaddress | ftpaddress | newsaddress | nntpaddress | prosperoaddress | telnetaddress | gopheraddress | waisaddress | mailtoaddress | midaddress | cidaddress`
- Each scheme expanded according to BNF productions in document (Sections 2.2 and 2.3 of original).

**Note**: The BNF productions are normative; refer to original document for complete formal syntax. The `path` element is defined recursively with `segment [ / path ]`, and `search` uses `+` as concatenation.

## Informative Annexes (Condensed)
- **Design Criteria and Choices (Section 3)**: Explains rationale for extensibility (left-to-right prefix), completeness (encoding binary in hex/base64), and printability (7-bit ASCII with escape character `%`). The safe set and escaping scheme were chosen for canonical representation and transport robustness.
- **Related Work (References)**: Lists key specifications and papers that influenced the URI design, including FTP, HTTP, Gopher, WAIS, Prospero, NNTP, and URN requirements.