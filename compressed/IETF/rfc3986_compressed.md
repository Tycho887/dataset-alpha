# RFC 3986: Uniform Resource Identifier (URI): Generic Syntax
**Source**: Internet Engineering Task Force (IETF) | **Version**: STD 66 | **Date**: January 2005 | **Type**: Standards Track (Normative)
**Original**: https://tools.ietf.org/html/rfc3986

## Scope (Summary)
Defines the generic syntax for Uniform Resource Identifiers (URIs), a compact sequence of characters that identifies an abstract or physical resource. Specifies a parsing algorithm for URI references (including relative references), normalization/comparison methods, and security considerations. Does not define individual URI schemes; those are defined by separate specifications.

## Normative References
- [ASCII] ANSI X3.4-1986, "Coded Character Set -- 7-bit American Standard Code for Information Interchange"
- [RFC2234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 2234, November 1997.
- [STD63] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [UCS] ISO/IEC 10646:2003, "Information Technology - Universal Multiple-Octet Coded Character Set (UCS)"

## Definitions and Abbreviations
- **URI**: Uniform Resource Identifier, an identifier consisting of a sequence of characters matching the `<URI>` syntax rule (Section 3).
- **URI Reference**: A URI or a relative reference (Section 4.1). Often used generically.
- **Percent-encoding**: Mechanism for representing a data octet as "%" followed by two hexadecimal digits (Section 2.1).
- **Reserved characters**: Characters that may serve as delimiters: gen-delims (`: / ? # [ ] @`) and sub-delims (`! $ & ' ( ) * + , ; =`) (Section 2.2).
- **Unreserved characters**: Characters allowed without special purpose: ALPHA, DIGIT, `-`, `.`, `_`, `~` (Section 2.3).
- **Scheme**: The first component of a URI, a name referring to a specification for assigning identifiers (Section 3.1).
- **Authority**: An optional hierarchical element for a naming authority, consisting of optional userinfo, host, and port (Section 3.2).
- **Path**: A hierarchical sequence of segments terminated by `?` or `#` or end of URI (Section 3.3).
- **Query**: Non-hierarchical data following `?` (Section 3.4).
- **Fragment**: Secondary identification following `#` (Section 3.5).
- **Relative Reference**: A URI reference that does not contain a scheme, expressed relative to a base URI (Section 4.2).

## 1. Introduction
- URI syntax derived from World Wide Web initiative (RFC 1630). This document obsoletes RFC 2396, RFC 2732, and updates RFC 1738.
- URI characteristics: **Uniform** (allows reuse across contexts), **Resource** (anything that can be identified), **Identifier** (distinguishes resource from others).
- The generic syntax is a superset of all URI schemes; scheme-specific semantics are postponed until needed.
- URI, URL, URN: A URI can be a locator (URL) or a name (URN). The term "URI" is preferred over "URL" or "URN" for generality.

### 1.2 Design Considerations
- **Transcription**: URI must consist of characters easily entered from a keyboard (limited set). Percent-encoding allows non-ASCII characters.
- **Separation of Identification from Interaction**: URI provides identification, not access. "Resolution" determines access mechanism; "dereference" performs an action.
- **Hierarchical Identifiers**: Use of `/`, `?`, `#` to delimit components. Allows relative referencing.

## 2. Characters
- URI characters are encoded as octets for transport; no specific character encoding mandated by this spec.
- ABNF terminals are based on US-ASCII codepoints.

### 2.1 Percent-Encoding
- pct-encoded = "%" HEXDIG HEXDIG
- Uppercase hex digits are equivalent to lowercase. Producers and normalizers **should** use uppercase.

### 2.2 Reserved Characters
- reserved = gen-delims / sub-delims
- Characters in the reserved set are protected from normalization. If data conflicts with a reserved character's purpose as delimiter, the data **must** be percent-encoded.
- If a reserved character is found and no delimiting role is known, it **must** be interpreted as representing that US-ASCII character.

### 2.3 Unreserved Characters
- unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
- URIs differing in replacement of an unreserved character with its percent-encoded form are equivalent. Percent-encoded unreserved octets **should** be decoded by normalizers.

### 2.4 When to Encode or Decode
- Percent-encoding occurs during URI production. Once produced, URI is always in percent-encoded form.
- When dereferencing, components must be parsed and separated before decoding, except unreserved octets.
- "%" must be encoded as "%25" to appear as data. Implementations **must not** percent-encode or decode the same string more than once.

### 2.5 Identifying Data
- Multiple character encodings are involved in URI production and transmission. An unreserved character is interpreted as its US-ASCII octet.
- For textual data from the Universal Character Set, encode as UTF-8, then percent-encode octets not in unreserved set (e.g., LATIN CAPITAL LETTER A WITH GRAVE → "%C3%80").

## 3. Syntax Components
- URI = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
- hier-part = "//" authority path-abempty / path-absolute / path-rootless / path-empty
- Scheme and path are required; path may be empty. When authority is present, path must be empty or begin with "/". When authority absent, path cannot begin with "//".

### 3.1 Scheme
- scheme = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
- Case-insensitive; canonical form is lowercase. Documents specifying schemes **must** use lowercase letters. Implementations **should** accept uppercase but **should** produce lowercase.
- Scheme specifications **must** define syntax so that all strings match `<absolute-URI>` grammar. Violations **should** be flagged as errors.

### 3.2 Authority
- authority = [ userinfo "@" ] host [ ":" port ]
- Authority is preceded by "//" and terminated by next "/", "?", "#", or end.
- Producers and normalizers **should** omit ":" delimiter if port is empty.
- If authority present, path must be empty or begin with "/".

#### 3.2.1 User Information
- userinfo = *( unreserved / pct-encoded / sub-delims / ":" )
- Use of "user:password" format is deprecated. Applications **should not** render clear text after first colon; **may** choose to ignore or reject such data; **should** reject storage in unencrypted form.
- Rendering of userinfo **should** be distinguished from rest of URI (to prevent semantic attacks).

#### 3.2.2 Host
- host = IP-literal / IPv4address / reg-name
- Case-insensitive. First-match-wins: if matches IPv4address, treat as IPv4 literal.
- **IP-literal**: `[ IPv6address / IPvFuture ]` - version flag "v" indicates future formats. If a version flag is unknown, application **should** return error "address mechanism not supported".
- **IPv4address**: dotted-decimal four octets (0-255). Only this form allowed.
- **reg-name**: *( unreserved / pct-encoded / sub-delims ) – intended for lookup in local registry (e.g., DNS). Non-ASCII names must be encoded as UTF-8 then percent-encoded. For IDN, must use IDNA encoding (RFC 3490) before DNS lookup. URI producers **should** use DNS-conformant names, ≤255 characters.

#### 3.2.3 Port
- port = *DIGIT
- If port is empty or equals scheme's default, producers and normalizers **should** omit it.

### 3.3 Path
- path = path-abempty / path-absolute / path-noscheme / path-rootless / path-empty
- Dot-segments "." and ".." are interpreted during relative reference resolution and removed.
- Path segments are opaque except for dot-segments and subcomponent delimiters.

### 3.4 Query
- query = *( pchar / "/" / "?" )
- The "?" character and "/" may represent data; caution with legacy implementations.

### 3.5 Fragment
- fragment = *( pchar / "/" / "?" )
- Fragment semantics are defined by the media type of the primary resource. Fragment identifiers are independent of URI scheme; not used in scheme-specific processing.
- Fragment identifier is separated from URI before dereference.

## 4. Usage
### 4.1 URI Reference
- URI-reference = URI / relative-ref
- Parsed first into components; if prefix does not match scheme syntax, treated as relative reference.

### 4.2 Relative Reference
- relative-ref = relative-part [ "?" query ] [ "#" fragment ]
- Types: network-path (starts "//"), absolute-path (starts "/"), relative-path (starts with segment).
- First segment of relative-path reference cannot contain ":" (would be mistaken for scheme). Prepend "./" if needed.

### 4.3 Absolute URI
- absolute-URI = scheme ":" hier-part [ "?" query ]
- Used for contexts that forbid fragments. Scheme specifications **must** define syntax matching `<absolute-URI>`.

### 4.4 Same-Document Reference
- When a URI reference (aside from fragment) is identical to the base URI, it is a same-document reference; dereference should not result in a new retrieval.

### 4.5 Suffix Reference
- Informal use of authority+path (e.g., "www.example.com/path"). Should be avoided; never used where long-term references are expected.

## 5. Reference Resolution
This section defines the algorithm to convert a URI reference to a target URI (matching `<URI>` syntax).

### 5.1 Establishing a Base URI
- Base URI must conform to `<absolute-URI>`. Established in order of precedence:
  1. Base URI embedded in content (e.g., `<base>` in HTML)
  2. Base URI from encapsulating entity (e.g., MIME message)
  3. Base URI from retrieval URI (last URI used to retrieve representation)
  4. Default base URI (application-dependent)

### 5.2 Relative Resolution Algorithm
1. Parse base URI into components.
2. Transform reference using pseudocode (Section 5.2.2):
   - If reference has a scheme (and not backward-compatible override), use absolute: move scheme, authority, path (remove dot-segments), query.
   - Else if reference has authority, use base scheme, reference authority, path (remove dot-segments), reference query.
   - Else (path may be relative):
     - If reference path empty: inherit base path; if reference has query use it, else base query.
     - If reference path starts with "/": use reference path (remove dot-segments).
     - Else: merge base path with reference path, then remove dot-segments.
   - Fragment from reference.
3. Merge paths: if base authority present and base path empty, result = "/" + reference path; else append reference path to everything after last "/" in base path.
4. Remove dot-segments: iterate to remove "." and ".." segments algorithmically (Section 5.2.4).

### 5.3 Component Recomposition
- Rebuild URI string by appending scheme, ":", "//", authority, path, "?", query, "#", fragment as defined.

### 5.4 Resolution Examples
Base URI: `http://a/b/c/d;p?q`
- `"g"` → `http://a/b/c/g`
- `"../g"` → `http://a/b/g`
- `"//g"` → `http://g`
- `"?y"` → `http://a/b/c/d;p?y`
- `"../../../../g"` → `http://a/g` (cannot go above root)
- `"/./g"` → `http://a/g`
- `"http:g"` may be treated as absolute or relative for backward compatibility.

## 6. Normalization and Comparison
- URI equivalence is based on string comparison, possibly augmented by scheme-specific rules. False negatives are minimized; false positives avoided.
- **Comparison Ladder** (increasing complexity):
  1. **Simple String Comparison**: identical strings are equivalent.
  2. **Syntax-Based Normalization**: case normalization (scheme and host to lowercase; percent-encoding hex digits to uppercase), percent-encoding normalization (decode unreserved octets), path segment normalization (remove dot-segments).
  3. **Scheme-Based Normalization**: e.g., default port omission, empty path to "/" for http.
  4. **Protocol-Based Normalization**: e.g., treating a URI that redirects to another as equivalent.

## 7. Security Considerations
- **Reliability and Consistency**: No guarantee of resource persistence.
- **Malicious Construction**: Avoid dereferencing URIs with well-known port numbers (0-1023) unless protocol compatible. Percent-encodings of CR/LF must not be decoded before transmission.
- **Back-End Transcoding**: Decode percent-encodings only after parsing components; reject %00 if not expected; beware of file system special names.
- **Rare IP Address Formats**: Only dotted-decimal allowed in syntax; platform routines may accept octal/hex variants – filter numerically.
- **Sensitive Information**: Password in userinfo is deprecated and should be considered an error.
- **Semantic Attacks**: Userinfo before host can be used to mislead. User agents **should** render userinfo distinctly.

## 8. IANA Considerations
- URI scheme names are registered per BCP 35. No IANA actions required by this document.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | A URI must match the syntax rule `<URI>` defined in Section 3. | shall | Section 1.1, 3 |
| R2 | Percent-encoded octets must be encoded as "%" followed by two uppercase hex digits; producers and normalizers should use uppercase. | shall/should | Section 2.1 |
| R3 | Characters in the reserved set must be percent-encoded if they conflict with a delimiting purpose; otherwise interpreted as US-ASCII. | shall (must) | Section 2.2 |
| R4 | Unreserved characters may appear without encoding; percent-encoded unreserved octets should be decoded by normalizers. | should | Section 2.3 |
| R5 | Implementations must not percent-encode or decode the same string more than once. | must | Section 2.4 |
| R6 | Scheme names are case-insensitive; documents specifying schemes must use lowercase. | must | Section 3.1 |
| R7 | Implementations should accept uppercase scheme names but should produce lowercase. | should | Section 3.1 |
| R8 | When authority is present, path must be empty or begin with "/". When authority absent, path cannot begin with "//". | must | Section 3.3 |
| R9 | Use of "user:password" in userinfo is deprecated; applications should not render clear text after first colon, should reject unencrypted storage. | should | Section 3.2.1 |
| R10 | Host subcomponent is case-insensitive. Use first-match-wins to distinguish IPv4address from registered name. | shall | Section 3.2.2 |
| R11 | Non-ASCII registered names must be encoded as UTF-8 then percent-encoded; for DNS resolution, must use IDNA encoding. | must | Section 3.2.2 |
| R12 | Port may be omitted if empty or equal to scheme default; producers and normalizers should omit. | should | Section 3.2.3 |
| R13 | A base URI must conform to `<absolute-URI>` syntax. | must | Section 5.1 |
| R14 | Relative references must be transformed to target URI using the algorithm in Section 5.2. | must | Section 5.2 |
| R15 | URI normalizers should apply syntax-based normalization: case normalization, percent-encoding normalization, removal of dot-segments. | should | Section 6.2.2 |
| R16 | Security: Percent-encodings of CR and LF must not be decoded before transmission across protocol. | must | Section 7.2 |
| R17 | Security: Applications must split URI into components before decoding percent-encodings. | must | Section 7.3 |

## Informative Annexes (Condensed)

- **Annex A (Collected ABNF for URI)**: Full normative grammar for URI, URI-reference, absolute-URI, relative-ref, and all subcomponents. (See attached ABNF block below.)
- **Annex B (Parsing with Regular Expression)**: Provides a regular expression to extract URI components: `^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?`. Maps subexpressions to scheme, authority, path, query, fragment.
- **Annex C (Delimiting URI in Context)**: Recommends using angle brackets `<...>` to delimit URIs in plain text. Whitespace around line breaks should be ignored; hyphens at line breaks require caution.
- **Annex D (Changes from RFC 2396)**: Lists additions (IPv6 literal syntax, new ABNF for IPv6address, normalization section) and modifications (switch to ABNF per RFC 2234, deprecation of obsolete rules, correction of relative resolution algorithm).

### ABNF (Collected from Appendix A)
```
URI           = scheme ":" hier-part [ "?" query ] [ "#" fragment ]
hier-part     = "//" authority path-abempty
              / path-absolute
              / path-rootless
              / path-empty
URI-reference = URI / relative-ref
absolute-URI  = scheme ":" hier-part [ "?" query ]
relative-ref  = relative-part [ "?" query ] [ "#" fragment ]
relative-part = "//" authority path-abempty
              / path-absolute
              / path-noscheme
              / path-empty
scheme        = ALPHA *( ALPHA / DIGIT / "+" / "-" / "." )
authority     = [ userinfo "@" ] host [ ":" port ]
userinfo      = *( unreserved / pct-encoded / sub-delims / ":" )
host          = IP-literal / IPv4address / reg-name
port          = *DIGIT
IP-literal    = "[" ( IPv6address / IPvFuture  ) "]"
IPvFuture     = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )
IPv6address   = ... (full ABNF in RFC)
h16           = 1*4HEXDIG
ls32          = ( h16 ":" h16 ) / IPv4address
IPv4address   = dec-octet "." dec-octet "." dec-octet "." dec-octet
dec-octet     = DIGIT / %x31-39 DIGIT / "1" 2DIGIT / "2" %x30-34 DIGIT / "25" %x30-35
reg-name      = *( unreserved / pct-encoded / sub-delims )
path          = ... (five alternatives)
pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"
query         = *( pchar / "/" / "?" )
fragment      = *( pchar / "/" / "?" )
pct-encoded   = "%" HEXDIG HEXDIG
unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
reserved      = gen-delims / sub-delims
gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
sub-delims    = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="