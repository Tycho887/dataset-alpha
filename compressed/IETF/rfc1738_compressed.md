# RFC 1738: Uniform Resource Locators (URL)
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: December 1994 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc1738

## Scope (Summary)
Defines the syntax and semantics of Uniform Resource Locators (URLs) — compact string representations for location and access of resources via the Internet.

## Normative References
- RFC 959: File Transfer Protocol (FTP)
- RFC 1034: Domain Names – Concepts and Facilities
- RFC 1036: Standard for Interchange of USENET Messages
- RFC 1123: Requirements for Internet Hosts – Application and Support
- RFC 1436: The Internet Gopher Protocol
- RFC 1625: WAIS over Z39.50-1988
- RFC 1630: Universal Resource Identifiers in WWW
- RFC 822: Standard for the Format of ARPA Internet Text Messages
- RFC 977: Network News Transfer Protocol
- ANSI X3.4-1986: US-ASCII coded character set

## Definitions and Abbreviations
- **URL (Uniform Resource Locator)**: A compact string representation for a resource available via the Internet.
- **Scheme**: The protocol or method used to access the resource (e.g., ftp, http). Scheme names consist of `[a-z]`, digits, `+`, `.`, `-`. Interpreters **must** treat uppercase as equivalent to lowercase.
- **Scheme-specific part**: The part of the URL after the colon, interpreted according to the scheme.
- **Reserved characters**: `;`, `/`, `?`, `:`, `@`, `=`, `&` – may have special meaning within a scheme.
- **Unsafe characters**: Space, `<`, `>`, `"`, `#`, `%`, `{`, `}`, `|`, `\`, `^`, `~`, `[`, `]`, `` ` `` – **must** always be encoded.
- **Unreserved characters**: Alphanumerics, `$`, `-`, `_`, `.`, `+`, `!`, `*`, `'`, `(`, `)`, `,`.
- **Encoding**: Percent-encoding using `%` followed by two hex digits (hexadecimal representation of the octet). Letters `A-F` or `a-f` allowed.

## General URL Syntax

### Main Parts (Section 2.1)
- General form: `<scheme>:<scheme-specific-part>`
- Scheme names: **must** consist of allowed characters; uppercase **must** be treated as equivalent to lowercase.

### Character Encoding (Section 2.2)
- **Octets must be encoded** if:
  - They have no corresponding graphic character in US-ASCII (octets 80-FF, control characters 00-1F, 7F).
  - The corresponding character is **unsafe** (as defined above).
  - The character is **reserved** within the scheme (see reserved list).
- **Only** alphanumerics, safe characters (`$-_.+!*'(),`), and reserved characters used for their reserved purpose may be used unencoded.
- Characters not required to be encoded (including alphanumerics) **may** be encoded within the scheme-specific part as long as not used for a reserved purpose.

### Hierarchical Schemes and Relative Links (Section 2.3)
- Some schemes (ftp, http, file) are hierarchical; components separated by `/`.

## Specific Schemes

### Common Internet Scheme Syntax (Section 3.1)
- For IP-based protocols:
  `//<user>:<password>@<host>:<port>/<url-path>`
- **Rules**:
  - `user` and `password` are optional; any `:`, `@`, `/` within them **must** be encoded.
  - `host`: fully qualified domain name or IP address (four decimal groups separated by `.`).
  - `port`: decimal number; if omitted, colon is omitted.
  - `url-path`: scheme-specific; the `/` before it is not part of the path.

### FTP Scheme (Section 3.2)
- **Syntax**: `ftp://<login>/<cwd1>/.../<cwdN>/<name>;type=<typecode>`
- Default port: 21.
- **User and password** (Section 3.2.1):
  - If omitted and server requests, use anonymous: user `anonymous`, password = end user's email address.
  - If username supplied without password and server requests, client **should** request password from user.
- **url-path** (Section 3.2.2): sequence of CWD commands then TYPE and RETR (or NLST if typecode = `d`). Characters `/` and `;` in names **must** be encoded.
- **Typecode** (Section 3.2.3): Optional `;type=a|i|d`. If omitted, client **must** guess appropriate mode.
- **Hierarchy** (Section 3.2.4): The `/` in URL does not imply Unix file system.
- **Optimization** (Section 3.2.5): Reliable algorithm for multiple retrievals is to disconnect and reestablish control connection; no common hierarchical model.

### HTTP Scheme (Section 3.3)
- **Syntax**: `http://<host>:<port>/<path>?<searchpart>`
- Default port: 80. No user or password allowed.
- Within `<path>` and `<searchpart>`, `/`, `;`, `?` are reserved.
- `<path>` and `/` may be omitted if neither `<path>` nor `<searchpart>` present.

### Gopher Scheme (Section 3.4)
- **Syntax**: `gopher://<host>:<port>/<gopher-path>`
  - `<gopher-path>`: `<gophertype><selector>` or with `%09<search>` and optionally `%09<gopher+_string>`.
- Default port: 70. If `<gopher-path>` empty, default gophertype = `1`.
- **No reserved characters** within `<gopher-path>`.
- Search engines (3.4.2): selector followed by encoded tab and search string.
- Gopher+ (3.4.3–3.4.9): Additional `%09` and Gopher+ string for attributes, alternate views, electronic forms. Specific syntax for attributes (`!` or `$`), views (`+<view_name>%20<language_name>`), forms (`+%091%0D%0A...`).

### MAILTO Scheme (Section 3.5)
- **Syntax**: `mailto:<rfc822-addr-spec>`
- No reserved characters. Percent sign `%` in RFC 822 addresses **must** be encoded.
- Does not designate a data object; no direct access.

### NEWS Scheme (Section 3.6)
- **Syntax**: `news:<newsgroup-name>` or `news:<message-id>`
- `<message-id>`: `unique@full_domain_name` (without angle brackets). Distinguishable by `@`.
- `<newsgroup-name>` = `*` refers to all groups.
- **Location-independent**; insufficient for single resource location.

### NNTP Scheme (Section 3.7)
- **Syntax**: `nntp://<host>:<port>/<newsgroup-name>/<article-number>`
- Default port: 119. Designates unique location; not globally accessible (most servers local-only). Preferred: news: form.

### TELNET Scheme (Section 3.8)
- **Syntax**: `telnet://<user>:<password>@<host>:<port>/`
- Default port: 23. Final `/` may be omitted.
- User and password are advisory only; does not designate a data object.

### WAIS Scheme (Section 3.9)
- Three forms:
  - `wais://<host>:<port>/<database>` (database)
  - `...?<search>` (search)
  - `.../<wtype>/<wpath>` (document)
- Default port: 210.
- `<wpath>` is WAIS document-id, treated opaquely.

### FILE Scheme (Section 3.10)
- **Syntax**: `file://<host>/<path>`
- `<host>` may be `localhost` or empty (interpreted as current machine).
- Does not specify Internet protocol; limited utility in network protocols.

### PROSPERO Scheme (Section 3.11)
- **Syntax**: `prospero://<host>:<port>/<hsoname>;<field>=<value>`
- Default port: 1525. No username/password.
- `<hsoname>` is host-specific object name, opaque; semicolons reserved.
- Slashes may appear but no hierarchical significance guaranteed.
- Fields and values may be appended with `;`.

## Registration of New Schemes (Section 4)
- Experimental schemes **must** use prefix `x-`.
- IANA maintains registry of URL schemes. Submission **must** include access algorithm and syntax.
- Schemes **must** have demonstrable utility and operability (e.g., via gateway).
- The following scheme names are reserved for future definition: afs, mid, cid, nfs, tn3270, mailserver, z39.50.

## BNF for Specific URL Schemes (Section 5)
Full BNF provided in original (pages 17–20). Key definitions: `genericurl`, `scheme`, `schemepart`, `login`, `host`, `user`, `password`, `urlpath`, plus scheme-specific productions for ftp, file, http, gopher, mailto, news, nntp, telnet, wais, prospero. Character classes: `lowalpha`, `hialpha`, `alpha`, `digit`, `safe`, `extra`, `national`, `punctuation`, `reserved`, `hex`, `escape`, `unreserved`, `uchar`, `xchar`.

## Security Considerations (Section 6)
- URL scheme itself not a security threat. No guarantee that a URL continues to point to the same object.
- Risk: URL can be constructed to cause harmful remote operation (e.g., specifying non-default port to invoke different protocol). Caution **should** be used with non-default port numbers, especially in reserved space.
- Embedded encoded delimiters (e.g., CR/LF) **must not** be unencoded before transmission to avoid simulating extra operations.
- URLs containing passwords that should be secret are **unwise**.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Scheme names: treat uppercase as equivalent to lowercase. | shall | §2.1 |
| R2 | Octets with no US-ASCII graphic, control characters (00-1F, 7F), unsafe characters, and reserved characters must be encoded. | must | §2.2 |
| R3 | Unsafe characters must always be encoded. | must | §2.2 |
| R4 | Within user/password field in common syntax, `:`, `@`, `/` must be encoded. | must | §3.1 |
| R5 | FTP: If no user/password supplied and server requests, use anonymous with user `anonymous` and password as end user's email. | must | §3.2.1 |
| R6 | FTP: If username supplied without password and server requests password, client should request password from user. | should | §3.2.1 |
| R7 | FTP: Characters `/` and `;` in names/CWD components must be encoded. | must | §3.2.2 |
| R8 | FTP: If `;type` omitted, client must guess appropriate mode. | must | §3.2.3 |
| R9 | MAILTO: Percent sign in RFC 822 addresses must be encoded. | must | §3.5 |
| R10 | New schemes using prefix `x-` are reserved for experimental purposes. | must | §4 |
| R11 | New scheme submission to IANA must include access algorithm and syntax. | must | §4 |
| R12 | New schemes must have demonstrable utility and operability. | must | §4 |
| R13 | Embedded CR/LF in URLs must not be unencoded before transmission. | must | §6 |

## Informative Annexes (Condensed)
- **Appendix: Recommendations for URLs in Context**: Provides guidelines for distinguishing URLs from other text. Recommends prefix `URL:` and delimiting with angle brackets `< >`. Line breaks should be ignored; extra whitespace added for line wrapping should be ignored. Hyphens at line breaks require caution because typesetters may introduce erroneous hyphens.
- **Security Considerations (Section 6)**: Already covered above; this section is also informative in nature.
- **References and Acknowledgments**: Full list of 20 references and acknowledgments to contributors.