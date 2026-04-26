# RFC 6265: HTTP State Management Mechanism
**Source**: IETF | **Version**: Standards Track | **Date**: April 2011 | **Type**: Normative  
**Obsoletes**: RFC 2965 | **Status**: Proposed Standard  
**Original**: [http://www.rfc-editor.org/info/rfc6265](http://www.rfc-editor.org/info/rfc6265)

## Scope (Summary)
This document defines the HTTP Cookie and Set-Cookie header fields for state management. It establishes normative requirements for servers generating cookies and user agents processing them, superseding RFC 2109 and RFC 2965.

## Normative References
- [RFC1034] – DOMAIN NAMES - CONCEPTS AND FACILITIES (STD 13)
- [RFC1123] – Requirements for Internet Hosts – Application and Support (STD 3)
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- [RFC2616] – Hypertext Transfer Protocol – HTTP/1.1
- [RFC3490] – Internationalizing Domain Names in Applications (IDNA)
- [RFC4790] – Internet Application Protocol Collation Registry
- [RFC5234] – Augmented BNF for Syntax Specifications: ABNF (STD 68)
- [RFC5890] – Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework
- [USASCII] – ANSI X3.4-1986

## Definitions and Abbreviations
- **canonicalized host name**: Result of converting each domain label to A-label (per [RFC5890]) and concatenating with %x2E (".").
- **case-insensitively match**: Equivalent under i;ascii-casemap collation [RFC4790].
- **cookie-attribute-list**: List of attribute-name/attribute-value pairs from parsing Set-Cookie.
- **cookie-date**: Date-time format used for Expires attribute.
- **cookie-name, cookie-value**: Name and value of a cookie.
- **cookie-path**: Path scope of a cookie.
- **cookie-store**: Internal storage for cookies.
- **default-path**: Computed from request-uri path (see §5.1.4).
- **domain-attribute**: Value of the Domain attribute in a Set-Cookie header.
- **domain-match**: Condition where a string is identical to a domain string or where the domain string is a suffix, preceded by a dot, and the string is a hostname (not IP address).
- **expiry-time**: The date/time when a cookie expires.
- **host-only-flag**: Indicates cookie is only sent to the origin host.
- **http-only-flag**: Indicates cookie is inaccessible to non-HTTP APIs.
- **non-HTTP API**: Any API not part of HTTP protocol (e.g., JavaScript document.cookie).
- **path-match**: Condition where cookie-path equals request-path, or is a prefix ending in "/", or prefix and next character is "/".
- **persistent-flag**: Indicates cookie survives session end.
- **request-host**: The hostname in the HTTP request URI.
- **request-uri**: Defined in [RFC2616] §5.1.2.
- **secure-only-flag**: Indicates cookie must be sent only over secure channels.
- **set-cookie-string**: Value of Set-Cookie header field.
- **string**: Sequence of non-NUL octets.
- **user agent**: Client that sends HTTP requests and receives responses.

## 2. Conventions

### 2.1 Conformance Criteria
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL** per [RFC2119].
- Algorithm steps phrased in the imperative carry the force of the introductory keyword.

### 2.2 Syntax Notation
- ABNF per [RFC5234]. Core rules: ALPHA, CR, CRLF, CTLs, DIGIT, DQUOTE, HEXDIG, LF, NUL, OCTET, SP, HTAB, CHAR, VCHAR, WSP.
- **OWS** = *( [ obs-fold ] WSP ), SHOULD be a single SP.
- **obs-fold** = CRLF

### 2.3 Terminology
- Terms "user agent, client, server, proxy, origin server" as in [RFC2616] §1.3.
- **request-host**: Hostname known by user agent for request.
- **request-uri**: From [RFC2616] §5.1.2.
- **case-insensitively match**: Per [RFC4790].
- **string**: Sequence of non-NUL octets.

## 3. Overview
- Origin server includes **Set-Cookie** header in HTTP response to store state.
- User agent returns **Cookie** header in subsequent requests within scope.
- **Origin servers MAY** send Set-Cookie with any response. **User agents MAY** ignore Set-Cookie in 100-level responses, **MUST process** in others (including 4xx/5xx).
- Multiple Set-Cookie headers per response allowed.
- Presence of Cookie or Set-Cookie does not preclude HTTP caching.
- **Origin servers SHOULD NOT** fold multiple Set-Cookie header fields into one.

### 3.1 Examples (Informative)
- Example: `Set-Cookie: SID=31d4d96e407aad42`
- Scoped with Path and Domain: `Set-Cookie: SID=31d4d96e407aad42; Path=/; Domain=example.com`
- Multiple cookies: `Set-Cookie: SID=...; Path=/; Secure; HttpOnly` and `Set-Cookie: lang=en-US; Path=/; Domain=example.com`
- Expiration: `Set-Cookie: lang=en-US; Expires=Wed, 09 Jun 2021 10:18:14 GMT`
- Removal: `Set-Cookie: lang=; Expires=Sun, 06 Nov 1994 08:49:37 GMT`

## 4. Server Requirements

### 4.1 Set-Cookie

#### 4.1.1 Syntax
- **Servers SHOULD NOT** send Set-Cookie headers violating the grammar.
- ABNF:
  ```
  set-cookie-header = "Set-Cookie:" SP set-cookie-string
  set-cookie-string = cookie-pair *( ";" SP cookie-av )
  cookie-pair       = cookie-name "=" cookie-value
  cookie-name       = token
  cookie-value      = *cookie-octet / ( DQUOTE *cookie-octet DQUOTE )
  token             = <from [RFC2616] §2.2>
  cookie-av         = expires-av / max-age-av / domain-av /
                      path-av / secure-av / httponly-av / extension-av
  expires-av        = "Expires=" sane-cookie-date
                    (sane-cookie-date = rfc1123-date per [RFC2616] §3.3.1)
  max-age-av        = "Max-Age=" non-zero-digit *DIGIT
  non-zero-digit    = %x31-39
  domain-av         = "Domain=" domain-value  (subdomain per [RFC1034] §3.5, enhanced by [RFC1123] §2.1)
  path-av           = "Path=" path-value  (any CHAR except CTLs or ";")
  secure-av         = "Secure"
  httponly-av       = "HttpOnly"
  extension-av      = any CHAR except CTLs or ";"
  ```
- **Servers SHOULD** encode arbitrary data (e.g., Base64 [RFC4648]).
- **Servers SHOULD NOT** produce two attributes with same name in same set-cookie-string.
- **Servers SHOULD NOT** include multiple Set-Cookie headers with same cookie-name in same response.
- Concurrent responses create race condition.
- **NOTE**: Servers SHOULD use four-digit years in rfc1123-date.
- **NOTE**: Some systems may have date handling bugs post-2038.

#### 4.1.2 Semantics (Non-Normative)
- Summarized: User agent stores cookie with attributes; returns applicable non-expired cookies.
- New cookie with same name, domain, path evicts old.
- Default: cookie returned only to origin server, expires at end of session.
- Unrecognized attributes ignored (cookie not rejected).

##### 4.1.2.1 The Expires Attribute
- Indicates maximum lifetime as date/time.
- User agent not required to retain until that date.

##### 4.1.2.2 The Max-Age Attribute
- Indicates maximum lifetime in seconds.
- User agent not required to retain for duration.
- **NOTE**: Some user agents ignore Max-Age.
- If both Max-Age and Expires present, Max-Age takes precedence.
- If neither, cookie retained until session end (user-agent defined).

##### 4.1.2.3 The Domain Attribute
- Specifies hosts that receive cookie. Example: "example.com" includes subdomains.
- Leading dot ignored; trailing dot causes ignore.
- If omitted, cookie returned only to origin server.
- **WARNING**: Some user agents treat absent Domain as current host, erroneously sending to subdomains.
- User agent rejects cookie if Domain does not include origin server.
- **NOTE**: User agents may reject public suffixes (e.g., "com", "co.uk").

##### 4.1.2.4 The Path Attribute
- Limits scope to paths. Default: directory of request-uri.
- Cookie included if request-uri path matches or is subdirectory ("/" as separator).
- Path attribute cannot be relied upon for security.

##### 4.1.2.5 The Secure Attribute
- Limits scope to secure channels (e.g., TLS).
- Protects confidentiality only; active attacker can overwrite from insecure channel.

##### 4.1.2.6 The HttpOnly Attribute
- Limits scope to HTTP requests; inaccessible to non-HTTP APIs.
- Independent of Secure attribute.

### 4.2 Cookie

#### 4.2.1 Syntax
- **Cookie header** sent to origin server, conforming to:
  ```
  cookie-header = "Cookie:" OWS cookie-string OWS
  cookie-string = cookie-pair *( ";" SP cookie-pair )
  ```

#### 4.2.2 Semantics
- Each cookie-pair contains name and value from received Set-Cookie.
- Attributes not returned.
- Semantics of individual cookies application-defined.
- **Servers SHOULD NOT** rely on serialization order, especially for cookies with same name.

## 5. User Agent Requirements

### 5.1 Subcomponent Algorithms

#### 5.1.1 Dates
- **User agent MUST** use algorithm equivalent to parse cookie-date.
- Grammar: `cookie-date = *delimiter date-token-list *delimiter`
- Process tokens sequentially for time, day-of-month, month, year.
- Year handling: 70-99 → +1900; 0-69 → +2000.
- Fail if incomplete, day<1 or >31, year<1601, hour>23, minute>59, second>59.
- Leap seconds not representable.

#### 5.1.2 Canonicalized Host Names
- Convert host name to domain labels; convert NR-LDH labels to A-labels per [RFC5890] (or punycode per [RFC3490]).
- Concatenate with ".".

#### 5.1.3 Domain Matching
- String domain-matches domain string if identical, or if domain string is suffix preceded by "." and string is hostname.

#### 5.1.4 Paths and Path-Match
- Compute default-path:
  1. Let uri-path be path portion of request-uri.
  2. If empty or not starting with "/", output "/".
  3. If only one "/", output "/".
  4. Otherwise, output up to but excluding right-most "/".
- Path-match:
  - cookie-path == request-path, or
  - cookie-path is prefix ending with "/", or
  - cookie-path is prefix and next character in request-path is "/".

### 5.2 The Set-Cookie Header
- **User agent MAY** ignore entire Set-Cookie header (e.g., third-party blocking).
- If not ignored, **MUST** parse field-value as set-cookie-string using algorithm:
  1. Split by first ";" into name-value-pair and unparsed-attributes.
  2. If no "=" in name-value-pair, ignore.
  3. Split name-value-pair at first "=" into name string and value string.
  4. Remove leading/trailing WSP from name and value.
  5. If name string empty, ignore.
  6. Cookie-name = name string; cookie-value = value string.
- Parse unparsed-attributes:
  - While not empty, consume attribute name and value (split by "="), remove WSP, process per attribute type.
  - Unrecognized attributes ignored.
- After parsing, user agent "receives a cookie" with name, value, and attribute list.

#### 5.2.1 The Expires Attribute
- If attribute-name case-insensitively matches "Expires":
  - Parse attribute-value as cookie-date.
  - If parse fails, ignore cookie-av.
  - If expiry-time beyond representable, **MAY** replace with last representable date.
  - If before earliest, **MAY** replace with earliest.
  - Append attribute with name Expires and value expiry-time.

#### 5.2.2 The Max-Age Attribute
- If matches "Max-Age":
  - If first character not DIGIT or "-", ignore.
  - If remainder contains non-DIGIT, ignore.
  - Let delta-seconds be integer.
  - If <=0, expiry-time = earliest representable.
  - Else, expiry-time = current time + delta-seconds.
  - Append attribute with name Max-Age and value expiry-time.

#### 5.2.3 The Domain Attribute
- If matches "Domain":
  - If attribute-value empty, behavior undefined; **SHOULD** ignore cookie-av.
  - If first char is ".", cookie-domain = value without leading dot; else entire value.
  - Convert to lower case.
  - Append attribute with name Domain and value cookie-domain.

#### 5.2.4 The Path Attribute
- If matches "Path":
  - If attribute-value empty or not starting with "/", cookie-path = default-path.
  - Else cookie-path = attribute-value.
  - Append attribute.

#### 5.2.5 The Secure Attribute
- If matches "Secure", append attribute with empty value.

#### 5.2.6 The HttpOnly Attribute
- If matches "HttpOnly", append attribute with empty value.

### 5.3 Storage Model
- Store per cookie: name, value, expiry-time, domain, path, creation-time, last-access-time, persistent-flag, host-only-flag, secure-only-flag, http-only-flag.
- When receiving cookie from request-uri with name, value, and attribute list:
  1. **MAY** ignore cookie entirely.
  2. Create new cookie with name, value, set creation-time and last-access-time to now.
  3. Determine expiry:
     - If Max-Age present: persistent-flag = true, expiry-time = last Max-Age attribute value.
     - Else if Expires present (and no Max-Age): persistent-flag = true, expiry-time = last Expires value.
     - Else: persistent-flag = false, expiry-time = latest representable.
  4. Determine domain-attribute:
     - If Domain present: domain-attribute = last Domain value.
     - Else: empty string.
  5. If user agent configured to reject public suffixes:
     - If domain-attribute is a public suffix:
       - If domain-attribute == canonicalized request-host: set domain-attribute = empty string.
       - Else: ignore cookie entirely.
     - **NOTE**: User agents **SHOULD** use up-to-date public suffix list (e.g., publicsuffix.org).
  6. If domain-attribute non-empty:
     - If request-host does not domain-match domain-attribute: ignore cookie.
     - Else: host-only-flag = false, cookie's domain = domain-attribute.
   - Else: host-only-flag = true, cookie's domain = canonicalized request-host.
  7. If Path attribute present: cookie's path = last Path value.
     - Else: cookie's path = default-path of request-uri.
  8. If Secure attribute present: secure-only-flag = true; else false.
  9. If HttpOnly attribute present: http-only-flag = true; else false.
  10. If received from non-HTTP API and http-only-flag set: ignore.
  11. If cookie store contains cookie with same name, domain, path:
       - Let old-cookie be that cookie.
       - If new cookie from non-HTTP API and old-cookie's http-only-flag set: ignore new cookie.
       - Update new cookie's creation-time to old-cookie's creation-time.
       - Remove old-cookie.
  12. Insert new cookie into store.
- Expired cookie: expiry date in past. **User agent MUST** evict expired cookies at any time.
- **User agent MAY** remove excess cookies:
  - If number per domain exceeds implementation-defined bound (e.g., 50).
  - If total exceeds bound (e.g., 3000).
- When removing excess, evict in priority:
  1. Expired cookies.
  2. Cookies from domains with more than predetermined number.
  3. All cookies.
- If same priority, evict earliest last-access-time first.
- When session ends, **user agent MUST** remove all cookies with persistent-flag = false.

### 5.4 The Cookie Header
- **User agent MUST NOT** attach more than one Cookie header to a request.
- **MAY** omit Cookie header entirely (e.g., third-party requests).
- If attached, **MUST** send cookie-string as value.
- Compute cookie-string:
  1. Let cookie-list be cookies from store that satisfy:
     - Host-only-flag true and request-host == cookie's domain; OR host-only-flag false and request-host domain-matches cookie's domain.
     - Request-uri path path-matches cookie's path.
     - If secure-only-flag true, request-uri scheme must be "secure" (as defined by user agent, e.g., https).
     - If http-only-flag true, exclude if generating for non-HTTP API.
  2. **SHOULD** sort by: longer paths first; if equal length, earlier creation-time first.
  3. Update last-access-time of each cookie in list.
  4. Serialize: for each cookie, output name + "=" + value; separate with "; ".
- **NOTE**: cookie-string is sequence of octets; may try UTF-8 for presentation.

## 6. Implementation Considerations

### 6.1 Limits
- General-use user agents **SHOULD** provide at least:
  - 4096 bytes per cookie (name + value + attributes)
  - 50 cookies per domain
  - 3000 cookies total
- Servers **SHOULD** use as few and small cookies as possible.
- Servers **SHOULD** gracefully degrade if cookies not returned.

### 6.2 Application Programming Interfaces
- String-based APIs to cookies are error-prone. Platforms **should** provide semantic APIs (e.g., accepting Date objects).

### 6.3 IDNA Dependency and Migration
- **User agents SHOULD** implement IDNA2008 [RFC5890] and **MAY** implement [UTS46] or [RFC5895] for transition.
- If not implementing IDNA2008, **MUST** implement IDNA2003 [RFC3490].

## 7. Privacy Considerations
- Cookies can facilitate tracking. Third-party cookies are especially concerning.
- **User agents SHOULD** provide mechanisms to manage cookies (delete by period or domain). **SHOULD** provide mechanism to disable cookies.
- When cookies disabled: **MUST NOT** include Cookie header; **MUST NOT** process Set-Cookie headers.
- If persistent storage prevented, **MUST** treat all received cookies as persistent-flag = false.
- **Servers SHOULD** set reasonable expiration periods; not gratuitously long.

## 8. Security Considerations

### 8.1 Overview
- Cookies rely on ambient authority for authentication, vulnerable to cross-site request forgery [CSRF].
- Transport-layer encryption insufficient; cookies have inherent vulnerabilities.

### 8.2 Ambient Authority
- Cookies separate designation (URLs) from authorization (cookies), allowing CSRF attacks.
- Server operators should consider entangling designation and authorization via URLs as capabilities.

### 8.3 Clear Text
- Unless over secure channel, cookies transmitted in clear; eavesdropper can read, intermediary can alter, client can alter.
- **Servers SHOULD** encrypt and sign cookie contents.
- For higher security, **SHOULD** use cookies only over secure channels and **SHOULD** set Secure attribute for every cookie.

### 8.4 Session Identifiers
- Use nonce in cookie; limits damage if leaked.
- Avoid session fixation: server **SHOULD** reject session identifiers from unexpected sources.

### 8.5 Weak Confidentiality
- Cookies not isolated by port (same host, different ports see same cookies).
- Not isolated by scheme (e.g., ftp can access cookies).
- Path isolation not guaranteed via non-HTTP APIs.

### 8.6 Weak Integrity
- Sibling domains can overwrite each other's cookies (via Domain attribute).
- Path attribute does not provide integrity; server **SHOULD NOT** run mutually distrusting services on different paths of same host.
- Active network attacker can inject Set-Cookie over HTTP to overwrite HTTPS cookies.
- Encryption/signing mitigates but does not prevent replay.
- Attacker can force cookie eviction by storing many cookies.

### 8.7 Reliance on DNS
- Cookie security relies on DNS integrity; if DNS compromised, cookie protocol may fail.

## 9. IANA Considerations
- Permanent registrations updated:
  - **Cookie**: standard, [RFC6265 §5.4]
  - **Set-Cookie**: standard, [RFC6265 §5.2]
  - **Cookie2**: obsoleted, [RFC2965]
  - **Set-Cookie2**: obsoleted, [RFC2965]

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Servers SHOULD NOT send Set-Cookie headers violating grammar | SHOULD NOT | §4.1.1 |
| R2 | Servers SHOULD encode arbitrary data in cookie-value | SHOULD | §4.1.1 |
| R3 | Servers SHOULD NOT produce two attributes with same name in one set-cookie-string | SHOULD NOT | §4.1.1 |
| R4 | Servers SHOULD NOT include multiple Set-Cookie with same cookie-name in same response | SHOULD NOT | §4.1.1 |
| R5 | User agents MUST process Set-Cookie in responses (except 1xx) | MUST | §3 |
| R6 | User agents MUST NOT attach more than one Cookie header per request | MUST NOT | §5.4 |
| R7 | User agents MUST evict expired cookies at any time | MUST | §5.3 |
| R8 | User agents MUST remove all cookies with persistent-flag=false at session end | MUST | §5.3 |
| R9 | User agents MUST use algorithm equivalent to parse set-cookie-string | MUST | §5.2 |
| R10 | User agents MUST use algorithm equivalent to compute cookie-string | MUST | §5.4 |
| R11 | User agents SHOULD sort cookie-list by path length then creation-time | SHOULD | §5.4 |
| R12 | User agents SHOULD provide mechanisms to manage and disable cookies | SHOULD | §7.2 |
| R13 | Servers SHOULD encrypt and sign cookie contents | SHOULD | §8.3 |
| R14 | Servers SHOULD set Secure attribute for cookies over secure channels | SHOULD | §8.3 |

## Informative Annexes (Condensed)
- **Annex A. Acknowledgements**: Lists contributors and reviewers; no normative content.