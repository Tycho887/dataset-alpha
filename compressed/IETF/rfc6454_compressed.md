# RFC 6454: The Web Origin Concept
**Source**: IETF | **Version**: Standards Track | **Date**: December 2011 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6454

## Scope (Summary)
This document defines the concept of a web "origin" as a scheme/host/port tuple used for security isolation in user agents. It specifies how to determine the origin of a URI, compare origins, serialize origins to Unicode and ASCII strings, and defines the HTTP `Origin` header field.

## Normative References
- [RFC20] Cerf, V., "ASCII format for network interchange", RFC 20, October 1969.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC3864] Klyne, G., et al., "Registration Procedures for Message Header Fields", BCP 90, RFC 3864, September 2004.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC4790] Newman, C., et al., "Internet Application Protocol Collation Registry", RFC 4790, March 2007.
- [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5890] Klensin, J., "Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework", RFC 5890, August 2010.
- [RFC5891] Klensin, J., "Internationalized Domain Names in Applications (IDNA): Protocol", RFC 5891, August 2010.
- [Unicode6] The Unicode Consortium, "The Unicode Standard, Version 6.0.0", 2011.

## Definitions and Abbreviations
- **User agent, client, server, proxy, origin server**: As defined in HTTP/1.1 ([RFC2616], Section 1.3).
- **Globally unique identifier**: A value different from all other previously existing values (e.g., a sufficiently long random string or a monotonically increasing local counter).
- **Origin**: A triple (scheme, host, port) used to group URIs into protection domains (Section 3.2).
- **Same-origin**: Two URIs are same-origin if their origins are identical (Section 5).
- **ASCII serialization**: String form of an origin as `scheme "://" host [ ":" port ]` with lowercase scheme and host, and port included only if not default (Section 6.2).
- **Unicode serialization**: Like ASCII but with IDNA U-label conversion for host (Section 6.1).

## Section 3: Principles of the Same-Origin Policy

### 3.1 Trust
- **Trust by URI**: Documents grant privileges to resources via URIs (e.g., `<script src="...">` trusts integrity; form `action="..."` trusts confidentiality).
- **Pitfall (3.1.1)**: Ensure important trust distinctions (e.g., TLS vs non-TLS) are visible in URI schemes; otherwise documents cannot selectively prefer secure channels.

### 3.2 Origin
- URIs with the same scheme, host, and port belong to the same origin. (Examples in 3.2.1)
- Including scheme is essential to separate http and https. Host should be fully qualified, not top-level domain only.

### 3.3 Authority
- **Authority granted by media type**: Passive content (e.g., images) carries no authority; active content (e.g., HTML) carries the origin’s full authority.
- **Pitfall (3.3.1)**: New platform features should not grant authority based on media type; must avoid content sniffing that elevates low-authority types.

### 3.4 Policy
- **Object Access (3.4.1)**: Most APIs are same-origin only. Exceptions (e.g., postMessage) must be designed carefully.
- **Network Access (3.4.2)**: Reading from other origins generally forbidden. Sending allowed via limited protocols (e.g., HTTP without custom headers). Cross-origin sharing (CORS) can opt in per origin.
- **Pitfall (3.4.3)**: Cross-origin interactions invite security issues; privileges should be granted/withheld per origin, not per resource.

### 3.5 Conclusion
The same-origin policy uses URIs to designate trust, groups URIs into origins, grants authority based on media type, and isolates origins with limited cross-origin access.

## Section 4: Origin of a URI

- **Algorithm to compute origin**:
  1. If the URI does not use a hierarchical element as a naming authority ([RFC3986], Section 3.2) or is not absolute, generate and return a fresh globally unique identifier.
     - NOTE: Multiple invocations may return different values; typically computed once per document.
  2. Let `uri-scheme` be the scheme component, converted to lowercase.
  3. If the implementation does not support the protocol given by `uri-scheme`, generate and return a fresh globally unique identifier.
  4. If `uri-scheme` is "file", the implementation MAY return an implementation-defined value.
  5. Let `uri-host` be the host component, converted to lowercase using the i;ascii-casemap collation ([RFC4790]).
     - NOTE: Assumes IDNA processing has already converted non-ASCII labels to A-labels.
  6. If there is no port component, let `uri-port` be the default port for the protocol; otherwise, let `uri-port` be the port component.
  7. Return the triple (uri-scheme, uri-host, uri-port).

## Section 5: Comparing Origins
- Two origins are "the same" if and only if they are identical. For triples: same scheme, host, and port. A globally unique identifier origin is never same as a triple origin.
- Two URIs are same-origin if their origins are the same. (A URI may not be same-origin with itself, e.g., data URI.)

## Section 6: Serializing Origins

### 6.1 Unicode Serialization
- If origin is not a triple, return the string "null".
- Otherwise: result = scheme + "://" + host (each component: if A-label, use U-label; otherwise verbatim) + optional ":" + port if not default.

### 6.2 ASCII Serialization
- If origin is not a triple, return "null".
- Otherwise: result = scheme + "://" + host (as is, lowercase) + optional ":" + port if not default.

## Section 7: The HTTP Origin Header Field

### 7.1 Syntax
- `origin = "Origin:" OWS origin-list-or-null OWS`
- `origin-list-or-null = %x6E %x75 %x6C %x6C ("null") / origin-list`
- `origin-list = serialized-origin *( SP serialized-origin )`
- `serialized-origin = scheme "://" host [ ":" port ]` (scheme, host, port from RFC 3986)

### 7.2 Semantics
- Indicates the origin(s) that caused the request (as defined by the triggering API). The user agent MAY list all contributing origins (e.g., after redirects).

### 7.3 User Agent Requirements
- **MAY** include an Origin header in any HTTP request.
- **MUST NOT** include more than one Origin header in any HTTP request.
- **MUST** send the value "null" in the Origin header when issuing an HTTP request from a "privacy-sensitive" context.
- When generating an Origin header, each `serialized-origin` **MUST** be the ASCII serialization of an origin. No two consecutive `serialized-origin` productions may be identical (do not generate the second).

## Section 8: Security Considerations (Condensed)
- **8.1 Reliance on DNS**: The same-origin policy depends on DNS for schemes like http; https uses certificates for verification; chrome-extension uses public keys.
- **8.2 Divergent Units of Isolation**: Older technologies (e.g., cookies) may use different isolation units (e.g., registry-controlled domains). This is **NOT RECOMMENDED** because registry-controlled domain lists are incomplete and URI-scheme-dependent.
- **8.3 Ambient Authority**: Authority is based on URI, not object designation, which can lead to cross-site scripting vulnerabilities.
- **8.4 IDNA Dependency**: IDNA algorithm changes may redraw security boundaries and create or remove isolation between entities.

## Section 9: IANA Considerations
- The `Origin` header field has been registered in the permanent message header field registry as per [RFC3864]: Header field name: Origin, Applicable protocol: http, Status: standard, Author/Change controller: IETF, Specification document: this RFC (Section 7).

## Requirements Summary

| ID | Requirement Text | Type | Reference |
|---|---|---|---|
| R1 | If the URI does not use a hierarchical element as a naming authority or is not absolute, generate a fresh globally unique identifier and return that value. | MUST | Section 4 step 1 |
| R2 | If the implementation doesn't support the protocol, generate a fresh globally unique identifier and return that value. | MUST (implied by algorithm) | Section 4 step 3 |
| R3 | For "file" scheme, the implementation MAY return an implementation-defined value. | MAY | Section 4 step 4 |
| R4 | Convert scheme and host to lowercase (host using i;ascii-casemap). | MUST (implied by algorithm) | Section 4 steps 2,5 |
| R5 | Use default port if no port component; otherwise use provided port. | MUST (implied by algorithm) | Section 4 step 6 |
| R6 | Two origins are the same if and only if they have identical schemes, hosts, and ports (for triples). | MUST (definition) | Section 5 |
| R7 | Unicode serialization: if not a triple, return "null". Otherwise scheme + "://" + U-label host + optional port. | MUST (algorithm) | Section 6.1 |
| R8 | ASCII serialization: if not a triple, return "null". Otherwise scheme + "://" + host + optional port. | MUST (algorithm) | Section 6.2 |
| R9 | The user agent MAY include an Origin header in any HTTP request. | MAY | Section 7.3 |
| R10 | The user agent MUST NOT include more than one Origin header. | MUST NOT | Section 7.3 |
| R11 | When issuing an HTTP request from a privacy-sensitive context, the user agent MUST send "null" as the Origin value. | MUST | Section 7.3 |
| R12 | Each serialized-origin in Origin header MUST be the ASCII serialization of an origin. | MUST | Section 7.3 |
| R13 | No two consecutive serialized-origin values in Origin header may be identical. If they would be, the user agent MUST NOT generate the second. | MUST NOT | Section 7.3 |

## Informative Annexes (Condensed)
- **Appendix A (Acknowledgements)**: Thanks to reviewers listed for valuable feedback.