# RFC 2617: HTTP Authentication: Basic and Digest Access Authentication
**Source**: IETF - Standards Track | **Version**: Final | **Date**: June 1999 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc2617

## Scope (Summary)
This document defines the HTTP authentication framework, the Basic authentication scheme (cleartext password), and the Digest Access Authentication scheme (cryptographic hash-based). Digest provides password verification without sending the password in cleartext and includes optional integrity protection. The document obsoletes RFC 2069.

## Normative References
- [1] Berners-Lee, T., et al., "Hypertext Transfer Protocol -- HTTP/1.0", RFC 1945, May 1996.
- [2] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [3] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [4] Freed, N. and N. Borenstein, "MIME Part One", RFC 2045, November 1996.
- [5] Dierks, T. and C. Allen, "The TLS Protocol, Version 1.0", RFC 2246, January 1999.
- [6] Franks, J., et al., "An Extension to HTTP : Digest Access Authentication", RFC 2069, January 1997.
- [7] Berners-Lee, T., et al., "Uniform Resource Identifiers (URI): Generic Syntax", RFC 2396, August 1998.

## Definitions and Abbreviations
- **auth-scheme**: token identifying the authentication scheme (case-insensitive).
- **auth-param**: token "=" (token | quoted-string).
- **challenge**: auth-scheme 1*SP 1#auth-param.
- **credentials**: auth-scheme #auth-param.
- **realm**: "realm" "=" realm-value (case-insensitive directive, case-sensitive value). Required for all challenges.
- **protection space**: defined by (realm, canonical root URL). Allows partitioning of resources.
- **nonce**: server-specified data string, opaque to client.
- **cnonce**: client nonce value.
- **opaque**: server-specified string returned unchanged by client.
- **stale**: flag indicating nonce is invalid but credentials are valid.
- **algorithm**: "MD5", "MD5-sess", or token (default "MD5").
- **qop**: quality of protection: "auth", "auth-int", or token.
- **H(data)**: MD5(data) for MD5 and MD5-sess algorithms.
- **KD(secret, data)**: H(concat(secret, ":", data)).
- **MD5-sess**: algorithm for efficient third-party authentication.
- **LHEX**: hex digits 0-9, a-f.
- **nc-value**: 8 hex digits indicating request count for a given nonce.

## 1 Access Authentication

### 1.1 Reliance on the HTTP/1.1 Specification
- Uses augmented BNF from [2] and relies on non-terminals and other aspects of the HTTP/1.1 specification.

### 1.2 Access Authentication Framework
- **HTTP provides challenge-response mechanism** that MAY be used by a server to challenge a client and by a client to provide authentication information.
- **auth-scheme** = token; **auth-param** = token "=" ( token | quoted-string ).
- **401 Unauthorized** response MUST include a WWW-Authenticate header with at least one challenge.
- **407 Proxy Authentication Required** response MUST include a Proxy-Authenticate header with at least one challenge.
- **challenge** = auth-scheme 1*SP 1#auth-param.
- **realm** = "realm" "=" realm-value (quoted-string). Required for all challenges.
- **User agent** MAY include Authorization header after receiving 401.
- **Client** MAY include Proxy-Authorization header after receiving 407.
- **Credentials** = auth-scheme #auth-param.
- **User agent MUST choose** the strongest auth-scheme it understands from the challenges. *(Note: many browsers only recognize Basic; servers should only include Basic if minimally acceptable.)*
- **Protection space**: credentials MAY be reused for all requests within the same protection space for a period determined by scheme/parameters.
- **Server SHOULD return 401** if credentials not accepted; MUST include WWW-Authenticate with (possibly new) challenge.
- **Proxy SHOULD return 407** if credentials not accepted; MUST include Proxy-Authenticate with (possibly new) challenge.
- **Proxies MUST be transparent** regarding user agent authentication by origin servers (forward WWW-Authenticate and Authorization untouched). Proxy-Authenticate and Proxy-Authorization are hop-by-hop headers (section 13.5.1 of [2]).

## 2 Basic Authentication Scheme
- **challenge** = "Basic" realm.
- **credentials** = "Basic" basic-credentials.
- **basic-credentials** = base64 encoding of user-pass (userid:password).
- **user-pass** = userid ":" password.
- **Userids** might be case sensitive.
- **Client SHOULD assume** that all paths at or deeper than the last symbolic element in the Request-URI path are within the protection space of the Basic realm.
- **Client MAY preemptively send** Authorization header for resources in that space without another challenge.
- **Security**: passwords sent in cleartext (base64 encoded). SHOULD NOT be used without enhancements to protect sensitive information. Vulnerable to spoofing by counterfeit servers.

## 3 Digest Access Authentication Scheme

### 3.1 Introduction
#### 3.1.1 Purpose
- Avoids sending password in cleartext. Not intended as complete security solution; no message encryption.

#### 3.1.2 Overall Operation
- Server challenges with a nonce. Response contains a checksum (default MD5) of username, password, nonce, HTTP method, and requested URI. Password never sent in clear.

#### 3.1.3 Representation of digest values
- MD5 128-bit digest represented as 32 ASCII hex digits (0-9, a-f). Most significant to least significant, 4 bits per character.

#### 3.1.4 Limitations
- Password-based system. Not as secure as Kerberos or client-side private-key schemes. Better than Basic, telnet, ftp.

### 3.2 Specification of Digest Headers

#### 3.2.1 The WWW-Authenticate Response Header
- **challenge** = "Digest" digest-challenge.
- **digest-challenge** = 1#( realm | [ domain ] | nonce | [ opaque ] | [ stale ] | [ algorithm ] | [ qop-options ] | [auth-param] ).
- **domain**: quoted space-separated list of URIs defining protection space. If abs_path, relative to canonical root URL. If omitted, client should assume all URIs on server. Not meaningful in Proxy-Authenticate.
- **nonce**: server-specified data string, should be uniquely generated per 401 response. Recommended base64 or hexadecimal. Example construction: base64(time-stamp H(time-stamp ":" ETag ":" private-key)). Nonce is opaque to client.
- **opaque**: string returned unchanged by client.
- **stale**: flag. If TRUE (case-insensitive), client may retry with new encrypted response without reprompting for username/password. Server SHOULD set stale=TRUE only if nonce invalid but digest valid.
- **algorithm**: "MD5", "MD5-sess", or token. Default "MD5". If not understood, challenge SHOULD be ignored.
- **qop-options**: optional but SHOULD be used. Quoted string of tokens "auth", "auth-int", or token. Unrecognized options MUST be ignored.
- **auth-param**: for future extensions; unrecognized directives MUST be ignored.

#### 3.2.2 The Authorization Request Header
- **credentials** = "Digest" digest-response.
- **digest-response** = 1#( username | realm | nonce | digest-uri | response | [ algorithm ] | [cnonce] | [opaque] | [message-qop] | [nonce-count] | [auth-param] ).
- **username** = "username" "=" username-value (quoted-string).
- **digest-uri** = "uri" "=" digest-uri-value (request-uri as in HTTP/1.1).
- **message-qop** = "qop" "=" qop-value.
- **cnonce** = "cnonce" "=" cnonce-value. MUST be specified if qop sent; MUST NOT be specified if qop not sent.
- **nonce-count** = "nc" "=" nc-value (8 hex digits). MUST be specified if qop sent; MUST NOT be specified if qop not sent.
- **response** = "response" "=" request-digest (32 hex digits).
- If directives improper or missing, proper response is 400 Bad Request.
- If request-digest invalid, login failure should be logged (possible attack).

##### 3.2.2.1 Request-Digest
- With qop="auth" or "auth-int":
  `request-digest = <"> < KD ( H(A1), unq(nonce-value) ":" nc-value ":" unq(cnonce-value) ":" unq(qop-value) ":" H(A2) ) <">`
- Without qop (RFC 2069 compatibility):
  `request-digest = <"> < KD ( H(A1), unq(nonce-value) ":" H(A2) ) <">`

##### 3.2.2.2 A1
- If algorithm="MD5" or unspecified:
  `A1 = unq(username-value) ":" unq(realm-value) ":" passwd`
- If algorithm="MD5-sess":
  `A1 = H( unq(username-value) ":" unq(realm-value) ":" passwd ) ":" unq(nonce-value) ":" unq(cnonce-value)`
  Calculated only on first request after challenge. Creates session key.

##### 3.2.2.3 A2
- If qop="auth" or unspecified:
  `A2 = Method ":" digest-uri-value`
- If qop="auth-int":
  `A2 = Method ":" digest-uri-value ":" H(entity-body)`

##### 3.2.2.4 Directive values and quoted-string
- No white space allowed in strings to which H() is applied unless present in quoted strings or entity body. A1 example: `Mufasa:myhost@testrealm.com:Circle Of Life` (colons adjacent, spaces inside password preserved). For qop=auth-int, H(entity-body) computed before transfer encoding.

##### 3.2.2.5 Various considerations
- **Method** is the HTTP request method (section 5.1.1 of [2]).
- **request-uri** MUST agree with Request-URI.
- **Server MUST assure** resource designated by "uri" directive same as Request-Line; if not, SHOULD return 400 Bad Request.
- **Shared caches**: MUST NOT return response with Authorization header unless "must-revalidate" or "public" Cache-Control directive present. See section 13.7 and 14.9 of [2].

#### 3.2.3 The Authentication-Info Header
- Used by server to communicate successful authentication info.
- `AuthenticationInfo = "Authentication-Info" ":" auth-info`
- `auth-info = 1#(nextnonce | [ message-qop ] | [ response-auth ] | [ cnonce ] | [nonce-count])`
- **nextnonce**: server wishes client to use for future authentication. Client SHOULD use it for next request; failure may result in re-authentication with stale=TRUE.
- **message-qop**: server SHOULD use same value as client request.
- **response-auth** (rspauth): supports mutual authentication. Calculation: same as request-digest except A2 = ":" digest-uri-value (if qop=auth or unspecified) or ":" digest-uri-value ":" H(entity-body) (if qop=auth-int). cnonce and nc-values MUST be from the client request to which this response corresponds. response-auth, cnonce, and nonce-count MUST be present if qop=auth or auth-int.
- Allowed in trailer of chunked transfer-coded message.

### 3.3 Digest Operation
- Server verifies by computing same digest and comparing to request-digest.
- Server need not know cleartext password; H(A1) suffices.
- Authentication session lasts until client receives new WWW-Authenticate challenge.
- Client should remember username, password, nonce, nonce count, opaque.
- Preemptive Authorization possible; server may accept old nonce or return stale=TRUE.
- Opaque may be used to transport session state.

### 3.4 Security Protocol Negotiation
- Client SHOULD fail gracefully if server specifies only schemes it cannot handle.

### 3.5 Example
- (Informative) Demonstrates 401 response and Authorization header. Condensed: server sends challenge with nonce, qop, opaque; client responds with username, realm, nonce, uri, qop, nc, cnonce, response, opaque.

### 3.6 Proxy-Authentication and Proxy-Authorization
- Digest may be used for proxy authentication via Proxy-Authenticate and Proxy-Authorization headers (per sections 10.33, 10.34 of [2]).
- Proxy must issue 407 with Proxy-Authenticate (same format as WWW-Authenticate).
- Client/proxy re-issues request with Proxy-Authorization (same as Authorization).
- Server sends Proxy-Authentication-Info (same as Authentication-Info).

## 4 Security Considerations

### 4.1 Authentication of Clients using Basic Authentication
- Basic is not secure; password transmitted in cleartext. SHOULD NOT be used without enhancements to protect sensitive information.
- Even for identification, risks arise if users choose own passwords and reuse them elsewhere.
- Vulnerable to spoofing by counterfeit servers. Servers SHOULD guard against counterfeiting via gateways/CGI scripts.

### 4.2 Authentication of Clients using Digest Authentication
- Not strong compared to public key mechanisms, but significantly stronger than CRAM-MD5.
- No confidentiality beyond password protection.
- Only limited integrity (qop=auth-int) for parts used in digest calculation.
- Many needs require TLS or SHTTP.

### 4.3 Limited Use Nonce Values
- Server can restrict nonce to client, resource, time, or usage count. Strengthens replay protection but may impact performance and pipelining.

### 4.4 Comparison of Digest with Basic Authentication
- Both weak, but Digest prevents password exposure to eavesdropper. Replay limited to specific request.

### 4.5 Replay Attacks
- Replay usually pointless for GET (URI already known). For POST/PUT, server must use limited-use nonces or qop=auth-int.
- Server may digest client IP, timestamp, ETag, private key in nonce to resist replay.

### 4.6 Weakness Created by Multiple Authentication Schemes
- **User agent MUST choose strongest scheme it understands**.
- *Note: Many browsers only recognize Basic; servers should only include Basic if it is minimally acceptable.*
- Overall strength limited by weakest offered scheme.

### 4.7 Online dictionary attacks
- Attacker can test nonce/response pairs against dictionary. Mitigation: disallow dictionary words as passwords.

### 4.8 Man in the Middle
- MITM can add weak schemes or replace with Basic. User agents should consider visual indication of scheme or remember strongest used and warn before weaker.
- Hostile proxy may spoof requests.

### 4.9 Chosen plaintext attacks
- MITM can choose nonce. Countermeasure: client SHOULD use cnonce directive.

### 4.10 Precomputed dictionary attacks
- Chosen plaintext allows precomputation of response dictionary. Countermeasure: use cnonce.

### 4.11 Batch brute force attacks
- Similar to above; cnonce reduces risk.

### 4.12 Spoofing by Counterfeit Servers
- More difficult with Digest but client must demand Digest. Visual indication of scheme helps.

### 4.13 Storing passwords
- Server stores H(A1) (username:realm:password hash) per realm. If compromised, attacker gains access to documents in that realm but not cleartext passwords. Realm should be unique (include hostname).
- Password file must be protected as if it contained cleartext.

### 4.14 Summary
- Digest is weak by modern standards but far superior to Basic. Implementation quality varies; servers may use one-time nonces or limited-lifetime nonces as needed.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | 401 response MUST include WWW-Authenticate with at least one challenge | MUST | 1.2 |
| R2 | 407 response MUST include Proxy-Authenticate with at least one challenge | MUST | 1.2 |
| R3 | User agent MUST choose strongest auth-scheme it understands | MUST | 1.2, 4.6 |
| R4 | Server SHOULD return 401 if credentials not accepted; MUST include (possibly new) challenge | SHOULD, MUST | 1.2 |
| R5 | Proxy SHOULD return 407 if credentials not accepted; MUST include (possibly new) challenge | SHOULD, MUST | 1.2 |
| R6 | Proxies MUST be transparent regarding origin server authentication (forward headers untouched) | MUST | 1.2 |
| R7 | Basic authentication SHOULD NOT be used without enhancements to protect sensitive information | SHOULD NOT | 4.1 |
| R8 | Digest qop-options directive SHOULD be used by all compliant implementations | SHOULD | 3.2.1 |
| R9 | Unrecognized qop-options MUST be ignored | MUST | 3.2.1 |
| R10 | Unrecognized auth-param in challenge MUST be ignored | MUST | 3.2.1 |
| R11 | Unrecognized directives in digest-response MUST be ignored | MUST | 3.2.2 |
| R12 | cnonce MUST be specified if qop sent; MUST NOT be specified if qop not sent | MUST/MUST NOT | 3.2.2 |
| R13 | nonce-count MUST be specified if qop sent; MUST NOT be specified if qop not sent | MUST/MUST NOT | 3.2.2 |
| R14 | If request-digest invalid, login failure should be logged | should | 3.2.2 |
| R15 | Server MUST assure "uri" directive same as Request-Line; if not, SHOULD return 400 | MUST, SHOULD | 3.2.2.5 |
| R16 | Shared cache MUST NOT return response with Authorization header unless "must-revalidate" or "public" Cache-Control | MUST | 3.2.2.5, 13.7 [2] |
| R17 | Server SHOULD use same qop in Authentication-Info as client request | SHOULD | 3.2.3 |
| R18 | response-auth, cnonce, nonce-count MUST be present in Authentication-Info if qop=auth or qop=auth-int | MUST | 3.2.3 |
| R19 | Client SHOULD use nextnonce for next request | SHOULD | 3.2.3 |
| R20 | Client SHOULD fail gracefully if server specifies unsupported schemes | SHOULD | 3.4 |
| R21 | Server SHOULD guard against counterfeiting by gateways/CGI scripts | SHOULD | 4.1 |
| R22 | Basic authentication SHOULD NOT be used without enhancements to protect sensitive information | SHOULD NOT | 4.1 |

## Informative Annexes (Condensed)
- **Annex - Sample Implementation (Section 5)**: Provides C code for calculating HA1, request-digest, and response-digest using RFC 1321 MD5. Includes test program producing values from the example in section 3.5. This is non-normative.
- **Annex - Full Copyright Statement (Section 9)**: Standard IETF copyright notice allowing reproduction and derivative works for standards development, provided copyright notice retained.