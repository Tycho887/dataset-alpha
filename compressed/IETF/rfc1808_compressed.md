# RFC 1808: Relative Uniform Resource Locators
**Source**: IETF | **Version**: RFC 1808 | **Date**: June 1995 | **Type**: Standards Track (Normative)
**Original**: https://tools.ietf.org/html/rfc1808

## Scope (Summary)
This document defines the syntax and semantics for relative Uniform Resource Locators (URLs): a compact representation of a resource location relative to an absolute base URL. It specifies parsing, base URL establishment, and resolution algorithms.

## Normative References
- [1] Berners-Lee, T., "Universal Resource Identifiers in WWW...", RFC 1630, June 1994.
- [2] Berners-Lee, T., Masinter, L., and M. McCahill, Editors, "Uniform Resource Locators (URL)", RFC 1738, December 1994.
- [3] Berners-Lee T., and D. Connolly, "HyperText Markup Language Specification -- 2.0", February 1995.
- [4] Borenstein, N., and N. Freed, "MIME...", RFC 1521, September 1993.
- [5] Crocker, D., "Standard for the Format of ARPA Internet Text Messages", STD 11, RFC 822, August 1982.
- [6] Kunze, J., "Functional Recommendations for Internet Resource Locators", RFC 1736, February 1995.

## Definitions and Abbreviations
- **URL**: Uniform Resource Locator, compact representation of location and access method for a resource.
- **relative URL**: compact representation of location relative to an absolute base URL.
- **base URL**: absolute URL against which a relative reference is applied.
- **generic-RL syntax**: `<scheme>://<net_loc>/<path>;<params>?<query>#<fragment>`
- **net_loc**: network location and login information (per RFC 1738 §3.1).
- **path**: URL path (per RFC 1738 §3.1).
- **params**: object parameters (e.g., `;type=a`, per RFC 1738 §3.2.2).
- **query**: query information (per RFC 1738 §3.3).
- **fragment**: fragment identifier; not considered part of the URL (§2.4.1).
- **escape**: `%` hex hex.
- **pchar**: `uchar | ":" | "@" | "&" | "="`.

## 1. Introduction (Summary)
Relative URLs allow embedding of resource references that inherit context (scheme, network location, path) from a base document, reducing redundancy and enabling portable document trees. This document defines the syntax and resolution algorithm, complementing RFC 1738.

## 2. Relative URL Syntax
### 2.1 URL Syntactic Components
The generic-RL syntax consists of six components:
```
<scheme>://<net_loc>/<path>;<params>?<query>#<fragment>
```
Each except `<scheme>` may be absent. The fragment identifier (including `#`) is not part of the URL but **must** be recognized. If both `<params>` and `<query>` are present, `<query>` **must** occur after `<params>`.

- **scheme**: per RFC 1738 §2.1.
- **"//" net_loc**: per RFC 1738 §3.1.
- **"/" path**: per RFC 1738 §3.1.
- **";" params**: e.g., `;type=a` as in RFC 1738 §3.2.2.
- **"?" query**: per RFC 1738 §3.3.
- **"#" fragment**: fragment identifier.

### 2.2 BNF for Relative URLs (Normative)
```bnf
URL         = ( absoluteURL | relativeURL ) [ "#" fragment ]
absoluteURL = generic-RL | ( scheme ":" *( uchar | reserved ) )
generic-RL  = scheme ":" relativeURL
relativeURL = net_path | abs_path | rel_path
net_path    = "//" net_loc [ abs_path ]
abs_path    = "/"  rel_path
rel_path    = [ path ] [ ";" params ] [ "?" query ]
path        = fsegment *( "/" segment )
fsegment    = 1*pchar
segment     =  *pchar
params      = param *( ";" param )
param       = *( pchar | "/" )
scheme      = 1*( alpha | digit | "+" | "-" | "." )
net_loc     = *( pchar | ";" | "?" )
query       = *( uchar | reserved )
fragment    = *( uchar | reserved )
pchar       = uchar | ":" | "@" | "&" | "="
uchar       = unreserved | escape
unreserved  = alpha | digit | safe | extra
escape      = "%" hex hex
hex         = digit | "A" | "B" | "C" | "D" | "E" | "F" | "a" | "b" | "c" | "d" | "e" | "f"
alpha       = lowalpha | hialpha
lowalpha    = "a".."z"
hialpha     = "A".."Z"
digit       = "0".."9"
safe        = "$" | "-" | "_" | "." | "+"
extra       = "!" | "*" | "'" | "(" | ")" | ","
national    = "{" | "}" | "|" | "\" | "^" | "~" | "[" | "]" | "`"
reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "="
punctuation = "<" | ">" | "#" | "%" | <">
```

### 2.3 Specific Schemes and Syntactic Categories
- **Never used with relative URLs**: mailto, news, telnet.
- **May be used if base URL follows generic-RL**: gopher, prospero, wais.
- **Always parseable with generic-RL**: file, ftp, http, nntp.
- **Note**: RFC 1738’s allowance of `?` in ftp/file paths is believed to be an error. Semicolon `;` in http paths has semantics defined by this document for `<params>`.
- **Recommendation (normative)**: New schemes intended for relative URLs **should** be designed to be parsable via generic-RL syntax. A description of allowed relative forms **should** be included when a new scheme is registered (per RFC 1738 §4).

### 2.4 Parsing a URL
Rules applied in order:

#### 2.4.1 Parsing the Fragment Identifier
If parse string contains `#`, substring after first `#` is `<fragment>` (empty if `#` last char or absent). Remove matched substring including `#`. **Parsers must be able to recognize and set aside fragment identifiers.**

#### 2.4.2 Parsing the Scheme
If parse string contains `:` after first character and before any character not allowed in scheme name (alphanumeric, `+`, `.`, `-`), `<scheme>` is substring up to first colon. Remove those characters and colon.

#### 2.4.3 Parsing the Network Location/Login
If parse string begins with `//`, substring after `//` up to next `/` (or end) is `<net_loc>`. Remove `//` and `<net_loc>`.

#### 2.4.4 Parsing the Query Information
If parse string contains `?`, substring after first `?` is `<query>` (empty if `?` last char or absent). Remove substring including `?`.

#### 2.4.5 Parsing the Parameters
If parse string contains `;`, substring after first `;` is `<params>` (empty if `;` last char or absent). Remove substring including `;`.

#### 2.4.6 Parsing the Path
Remaining parse string is `<path>` and preceding slash (if any). **The parser must remember whether a slash was present** to differentiate relative vs absolute paths.

## 3. Establishing a Base URL
The base URL **must** be known for relative URLs to be meaningful. Established in order of precedence (innermost highest):

### 3.1 Base URL within Document Content
- Embedded in content (e.g., HTML `<BASE>` element, see Informative Annex).
- For messages, recommended header format: `Base: <URL:absoluteURL>` (case-insensitive, whitespace ignored).

### 3.2 Base URL from the Encapsulating Entity
If no embedded base URL, base URL is that of the encapsulating entity (e.g., MIME composite). Composite entities can redefine base URL for their parts recursively.

### 3.3 Base URL from the Retrieval URL
If no embedded or encapsulating base URL, the URL used to retrieve the document (last URL after redirection) **shall** be considered the base URL.

### 3.4 Default Base URL
If none apply, base URL is empty string; all embedded URLs **must** be absolute. Distributors of a document containing relative URLs **must** ensure the base URL can be established.

## 4. Resolving Relative URLs
Algorithm to resolve relative URL to absolute form given valid base URL:

1. **Establish base URL** per §3. If base URL is empty, embedded URL is absolute; done.
2. **Parse** both URLs per §2.4.
   a) If embedded URL entirely empty → inherit entire base URL; done.
   b) If embedded URL starts with scheme name → absolute; done.
   c) Otherwise → inherit scheme from base URL.
3. If embedded URL’s `<net_loc>` non-empty → go to step 7. Else inherit `<net_loc>` from base URL.
4. If embedded URL path preceded by `/` → not relative; go to step 7.
5. If embedded URL path empty (and not preceded by `/`):
   - Inherit base URL path.
   - If embedded URL’s `<params>` non-empty → go to step 7; else inherit base URL `<params>`.
   - If embedded URL’s `<query>` non-empty → go to step 7; else inherit base URL `<query>`.
6. Remove last segment of base URL path (rightmost `/`), append embedded URL’s path. Then apply dot-segment removal in order:
   a) Remove all `./` (`.` as complete segment).
   b) If path ends with `.`, remove that `.`.
   c) Remove all `<segment>/../` iteratively from leftmost, where `<segment>` != `..`.
   d) If path ends with `<segment>/..`, remove that.
7. **Recombine** components into absolute URL.

**Parameters do not affect path resolution. Fragment identifiers are only inherited from base URL when embedded URL is entirely empty.**

## 5. Examples and Recommended Practice
Base URL: `<URL:http://a/b/c/d;p?q#f>`

### 5.1 Normal Examples (Informative)
| Relative URL | Absolute Result |
|---|---|
| `g:h` | `g:h` |
| `g` | `http://a/b/c/g` |
| `./g` | `http://a/b/c/g` |
| `/g` | `http://a/g` |
| `//g` | `http://g` |
| `?y` | `http://a/b/c/d;p?y` |
| `;x` | `http://a/b/c/d;x` |
| `#s` | `http://a/b/c/d;p?q#s` |
| `.` | `http://a/b/c/` |
| `..` | `http://a/b/` |
| `../g` | `http://a/b/g` |
| `../../g` | `http://a/g` |

### 5.2 Abnormal Examples (Informative)
| Relative URL | Absolute Result | Note |
|---|---|---|
| `<>` (empty) | `http://a/b/c/d;p?q#f` | Inherits full base |
| `../../../g` | `http://a/../g` | Cannot go above root |
| `/./g` | `http://a/./g` | `.` is not special in absolute path |
| `http:g` | `http:g` | (loophole) Avoid |

### 5.3 Recommended Practice
- Authors **should** avoid colon as first component of relative path (e.g., `this:that`); use `./this:that` or escape colon (`this%3Athat`).
- The `;type=d` parameter **should not** be used in contexts allowing relative URLs.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Systems supporting relative URLs must be able to recognize them during URL parsing. | **must** | §2 |
| R2 | New schemes intended for relative URLs should be designed to be parsable via generic-RL syntax. | **should** | §2.3 |
| R3 | Base URL must be known for relative URLs to be usable. | **must** (implied) | §3 |
| R4 | The retrieval URL (last after redirection) shall be the base URL if no other base is set. | **shall** | §3.3 |
| R5 | Distributors of documents with relative URLs must ensure the base URL can be established. | **must** | §3.4 |
| R6 | Parsers must recognize and set aside fragment identifiers. | **must** | §2.4.1 |
| R7 | Parser must remember presence of preceding slash to differentiate relative/absolute paths. | **must** | §2.4.6 |
| R8 | Embedded URL inherits scheme from base URL if no scheme present. | (normative) | Step 2c |
| R9 | Embedded URL inherits net_loc from base URL if its own is empty. | (normative) | Step 3 |
| R10 | Params do not affect path resolution. | (normative) | §4 |
| R11 | Fragment identifiers are inherited only when embedded URL is entirely empty. | (normative) | §4 |
| R12 | Authors should avoid colon as first component of relative path; use `./this:that` or escape. | **should** | §5.3 |
| R13 | The `;type=d` parameter should not be used with relative URLs. | **should** | §5.3 |

## Security Considerations
No security considerations in use or parsing of relative URLs. Once resolved to absolute form, same considerations as RFC 1738 apply.

## Informative Annexes (Condensed)
- **Appendix – Embedding the Base URL in HTML**: HTML defines a `<BASE>` element in `HEAD` with an `HREF` attribute (absolute URL) to set the base URL for resolving relative URLs. Example provided. This appendix is descriptive and not part of the specification.