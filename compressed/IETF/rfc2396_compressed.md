# RFC 2396: Uniform Resource Identifiers (URI): Generic Syntax
**Source**: Internet Society (IETF) | **Version**: August 1998 | **Date**: August 1998 | **Type**: Standards Track  
**Original**: https://tools.ietf.org/html/rfc2396

## Scope (Summary)
Defines the generic syntax of URI (both absolute and relative forms), including a grammar that is a superset of all valid URI, enabling scheme-independent parsing. Revises and replaces RFC 1738 and RFC 1808.

## Normative References
- [RFC1738] Berners-Lee, T., Masinter, L., and M. McCahill, "Uniform Resource Locators (URL)", RFC 1738, December 1994 (updated by this document).
- [RFC1808] Fielding, R., "Relative Uniform Resource Locators", RFC 1808, June 1995 (updated by this document).
- [RFC1034] Mockapetris, P., "Domain Names – Concepts and Facilities", STD 13, RFC 1034, November 1987.
- [RFC1123] Braden, R., "Requirements for Internet Hosts – Application and Support", STD 3, RFC 1123, October 1989.
- [RFC822] Crocker, D., "Standard for the Format of ARPA Internet Text Messages", STD 11, RFC 822, August 1982.
- [RFC2046] Freed, N., and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996.
- [RFC2110] Palme, J., and A. Hopmann, "MIME E-mail Encapsulation of Aggregate Documents, such as HTML (MHTML)", RFC 2110, March 1997.
- [RFC2141] Moats, R., "URN Syntax", RFC 2141, May 1997.
- [ASCII] ANSI X3.4-1986, "Coded Character Set – 7-bit American Standard Code for Information Interchange".
- [UTF-8] Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 2279, January 1998.

## Definitions and Abbreviations
- **URI (Uniform Resource Identifier)**: A compact string of characters for identifying an abstract or physical resource.
- **URL (Uniform Resource Locator)**: Subset of URI that identify resources via a representation of their primary access mechanism (e.g., network location).
- **URN (Uniform Resource Name)**: Subset of URI required to remain globally unique and persistent even when the resource ceases to exist.
- **Scheme**: The first component of an absolute URI, defining the semantics for the remainder; name begins with an alpha character (see Section 3.1).
- **Authority**: The hierarchical element for a naming authority, typically an Internet-based server or registry (see Section 3.2).
- **Path**: Contains data specific to the authority (or scheme) identifying the resource (see Section 3.3).
- **Query**: A string of information to be interpreted by the resource (see Section 3.4).
- **Fragment**: Additional reference information attached to a URI reference, separated by "#" (see Section 4.1).
- **Reserved**: Characters used as delimiters within a URI: ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" | "$" | ",".
- **Unreserved**: Characters allowed in a URI without reserved purpose: alphanum | mark ("-" | "_" | "." | "!" | "~" | "*" | "'" | "(" | ")").
- **Escaped**: Encoding of an octet as a percent character "%" followed by two hexadecimal digits (e.g., "%20").
- **relativeURI**: A shortened form of absoluteURI, missing a prefix, with special path components "." and ".." when resolving (Section 5).
- **URI-reference**: An absolute or relative URI optionally followed by a fragment identifier.

## Section 1: Introduction
- URI provide a simple and extensible means for identifying a resource; syntax derived from RFC 1630.
- This document updates and merges RFC 1738 and RFC 1808.
- Does not discuss characters outside US-ASCII; recommendations in a separate document.

## Section 1.2: URI, URL, and URN
- **Must** distinguish: URI can be a locator, a name, or both.
- URL subset identifies resources via access mechanism; URN subset is globally unique and persistent.
- URI scheme (Section 3.1) defines the namespace and may further restrict syntax and semantics.

## Section 1.3: Example URI
(Informative – summarized) Examples of common URI: ftp, gopher, http, mailto, news, telnet.

## Section 1.4: Hierarchical URI and Relative Forms
- Some URI schemes support hierarchical naming with "/" delimiter.
- This document defines a scheme-independent relative form of URI reference (Section 5).

## Section 1.5: URI Transcribability
- URI consists of a limited set of characters (letters, digits, special chars) for global transcribability.
- Design goal: able to be typed from a non-network source.

## Section 1.6: Syntax Notation and Common Elements
- Uses BNF-like grammar as per RFC 822, with "|" for alternatives, "[]" for optional, "*" for repetitions.
- Grammar is defined in terms of characters, not octets.
- Common definitions: alpha, lowalpha, upalpha, digit, alphanum.

## Section 2: URI Characters and Escape Sequences
### 2.1 URI and non-ASCII Characters
- URI is a sequence of characters, not octets.
- A character-to-octet mapping is scheme-dependent.
- A second translation from octets to characters is defined by a 'charset'.
- No provision within generic URI syntax to identify charset; individual schemes may define.

### 2.2 Reserved Characters
- **Must** escape data characters that conflict with reserved purpose.
- Reserved: ";", "/", "?", ":", "@", "&", "=", "+", "$", ",".
- Characters reserved in a given URI component are defined by that component.

### 2.3 Unreserved Characters
- Unreserved: alphanum | mark.
- **Should not** escape unreserved characters unless necessary.

### 2.4 Escape Sequences
- **Must** escape data that does not have an unreserved representation.
#### 2.4.1 Escaped Encoding
- Escaped: "%" hex hex.
#### 2.4.2 When to Escape and Unescape
- Escaping/unescaping a completed URI **may** change semantics; only safe when creating from components.
- The "%" character **must** be escaped as "%25" to be used as data.
- **Should** not double‑escape or double‑unescape.
#### 2.4.3 Excluded US-ASCII Characters
- Control characters (00-1F, 7F) excluded.
- Space excluded.
- Delimiters "<", ">", "#", "%", '"' excluded.
- Unwise characters: "{" "}" "|" "\" "^" "[" "]" "`" excluded.

## Section 3: URI Syntactic Components
- Absolute URI: `<scheme>:<scheme-specific-part>`.
- Generic URI: `<scheme>://<authority><path>?<query>`.
- BNF:
  ```
  absoluteURI = scheme ":" ( hier_part | opaque_part )
  hier_part   = ( net_path | abs_path ) [ "?" query ]
  opaque_part = uric_no_slash *uric
  ```

### 3.1 Scheme Component
- Scheme name: begins with alpha, followed by alpha, digit, "+", "-", ".".
- Treat upper‑ and lower‑case as equivalent.
- Relative URI references **do not** begin with a scheme name.

### 3.2 Authority Component
- Preceded by "//", terminated by "/", "?", or end of URI.
- Characters ";", ":", "@", "?", "/" reserved within authority.
- Authority types: server or reg_name.
#### 3.2.1 Registry-based Naming Authority
- `reg_name = 1*( unreserved | escaped | "$" | "," | ";" | ":" | "@" | "&" | "=" | "+" )`
#### 3.2.2 Server-based Naming Authority
- `server = [ [ userinfo "@" ] hostport ]`
- userinfo: user and optional password – **NOT RECOMMENDED** (security risk).
- hostport: host [ ":" port ]; host = hostname | IPv4address; port = *digit.
- Hostnames per RFC 1034/1123.
- IPv6 literal not supported.

### 3.3 Path Component
- `path = [ abs_path | opaque_part ]`
- Path segments separated by "/"; segment may contain parameters separated by ";".
- Characters "/", ";", "=", "?" reserved within a segment.

### 3.4 Query Component
- `query = *uric`
- Characters ";", "/", "?", ":", "@", "&", "=", "+", ",", "$" reserved within query.

## Section 4: URI References
- `URI-reference = [ absoluteURI | relativeURI ] [ "#" fragment ]`
- Fragment identifier is additional reference information for the user agent after retrieval; not part of the URI.
- Semantics of fragment depends on media type of retrieved data.

### 4.1 Fragment Identifier
- Fragment **must** conform to URI character restrictions.
- Media types may define additional structure.

### 4.2 Same-document References
- Empty URI reference → current document.
- Reference with only fragment → identified fragment; **should not** cause additional retrieval.

### 4.3 Parsing a URI Reference
- Greedy algorithm: leftmost matching rule soaks up as much as possible.
- Authority component wins over path beginning with "//".

## Section 5: Relative URI References
- Allows document trees to be partially independent of location and access scheme.
- `relativeURI = ( net_path | abs_path | rel_path ) [ "?" query ]`
- rel_path: ";" and "@" allowed.
- Special path segments "." and ".." have meaning only when resolving relative‑path references.
- Authors **should** avoid colon as first segment of relative path (e.g., "this:that") – use "./this:that".

### 5.1 Establishing a Base URI
- Base URI must be known to parser.
- Precedence in order:
  1. Base URI embedded in document content (e.g., HTML BASE element).
  2. Base URI of encapsulating entity (message, document, or none).
  3. URI used to retrieve entity (last URI after redirects).
  4. Default base URI (application‑dependent).

### 5.2 Resolving Relative References to Absolute Form
- Algorithm described step‑by‑step (paraphrase):
  1. Parse reference into components (scheme, authority, path, query, fragment).
  2. If path empty and scheme, authority, query undefined → reference to current document; done.
  3. If scheme defined → absolute URI; done.
  4. If authority defined → network‑path; go to step 7.
  5. If path begins with "/" → absolute‑path; go to step 7.
  6. Else relative‑path: merge with base URI path using "." and ".." removal steps.
  7. Recombine components: `scheme + ":" + "//" + authority + path + "?" + query + "#" + fragment`.
- Exception: implementation **may** work around misformed relative references that prefix same scheme as base URI (backwards compatibility).

## Section 6: URI Normalization and Equivalence
- Rules are scheme‑dependent.
- For common syntax: scheme and hostname are case‑insensitive; default port elision is equivalent.

## Section 7: Security Considerations
- No general guarantee that a URL continues to locate the same resource.
- Constructing URLs with non‑default ports may cause unintended operations (e.g., gopher → SMTP).
- **Must** not unescape escaped delimiters (CR, LF) before transmission.
- **Strongly strongly NOT RECOMMENDED** to include passwords in userinfo (clear‑text risk).

## Additional Informative Sections (Condensed)
- **Section 8 – Acknowledgments**: Credits contributors.
- **Section 9 – References**: Normative and informative references (listed above).
- **Section 10 – Authors' Addresses**: Contact information for T. Berners‑Lee, R. Fielding, L. Masinter.

## Requirements Summary (Normative)
| ID  | Requirement | Type | Reference |
|-----|------------|------|-----------|
| R1  | Data character conflicting with reserved purpose must be escaped. | shall | Section 2.2 |
| R2  | Percent character used as data must be escaped as "%25". | shall | Section 2.4.2 |
| R3  | URI scheme names must begin with an alpha character. | shall | Section 3.1 |
| R4  | Upper‑ and lower‑case scheme names are equivalent. | shall | Section 3.1 |
| R5  | The userinfo format "user:password" is NOT RECOMMENDED. | should not | Section 3.2.2 |
| R6  | Fragment identifier must conform to URI character set restrictions. | shall | Section 4.1 |
| R7  | An empty URI reference refers to the current document; traversal should not cause additional retrieval. | should | Section 4.2 |
| R8  | When resolving relative references, the greedy algorithm (leftmost match) shall be used for authority vs. path disambiguation. | shall | Section 4.3 |
| R9  | Relative‑path segments "." and ".." are only special during resolution (Section 5.2). | shall | Section 5 |
| R10 | Base URI must be known for relative URI references; precedence defined in Section 5.1. | shall | Section 5.1 |
| R11 | The relative path resolution algorithm (step 6) must be followed for merging paths. | shall | Section 5.2 |
| R12 | Escaped delimiters (CR, LF) shall not be unescaped before transmission. | shall | Section 7 |
| R13 | Passwords within userinfo are strongly disrecommended. | should not | Section 7 |

## Informative Annexes (Condensed)
- **Appendix A – Collected BNF for URI**: Consolidates all grammar rules into one formal BNF definition.
- **Appendix B – Parsing a URI Reference with a Regular Expression**: Provides a POSIX regex for decomposing URI references into components.
- **Appendix C – Examples of Resolving Relative URI References**: Lists normal and abnormal resolution examples with base URI `http://a/b/c/d;p?q`.
- **Appendix D – Embedding the Base URI in HTML Documents**: Illustrates use of HTML `<BASE>` element (informative example).
- **Appendix E – Recommendations for Delimiting URI in Context**: Recommends using angle‑brackets or double‑quotes around URI in plain text; whitespace handling guidelines.
- **Appendix F – Abbreviated URLs**: Describes shortened references (e.g., `www.w3.org/Addressing/`) used in traditional media; not for relative URL contexts.
- **Appendix G – Summary of Non‑editorial Changes**: Lists modifications from RFC 1738 and RFC 1808 (additions, clarifications, BNF fixes).
- **Appendix H – Full Copyright Statement**: Standard IETF copyright notice.