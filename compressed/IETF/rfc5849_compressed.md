# RFC 5849: The OAuth 1.0 Protocol
**Source**: IETF | **Version**: 1.0 | **Date**: April 2010 | **Type**: Informational
**Original**: http://www.rfc-editor.org/info/rfc5849

## Scope (Summary)
This document specifies the OAuth 1.0 protocol for delegated access to protected resources. It defines a redirection-based authorization process enabling end-users to grant third-party clients access to their server-hosted resources without sharing credentials, and a method for making authenticated HTTP requests using two sets of credentials (client and token).

## Normative References
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies", RFC 2045, November 1996.
- [RFC2104] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2616] Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L., Leach, P., and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC2617] Franks, J., Hallam-Baker, P., Hostetler, J., Lawrence, S., Leach, P., Luotonen, A., and L. Stewart, "HTTP Authentication: Basic and Digest Access Authentication", RFC 2617, June 1999.
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
- [RFC3447] Jonsson, J. and B. Kaliski, "Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1", RFC 3447, February 2003.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [W3C.REC-html40-19980424] Hors, A., Raggett, D., and I. Jacobs, "HTML 4.0 Specification", World Wide Web Consortium Recommendation REC-html40-19980424, April 1998.

## Definitions and Abbreviations
- **client**: An HTTP client (per [RFC2616]) capable of making OAuth-authenticated requests (Section 3).
- **server**: An HTTP server (per [RFC2616]) capable of accepting OAuth-authenticated requests (Section 3).
- **protected resource**: An access-restricted resource obtainable from the server using an OAuth-authenticated request.
- **resource owner**: An entity capable of accessing and controlling protected resources by using credentials to authenticate with the server.
- **credentials**: A pair of a unique identifier and a matching shared secret. Three classes: client, temporary, and token.
- **token**: A unique identifier issued by the server and used by the client to associate authenticated requests with the resource owner. Tokens have a matching shared-secret.

**Mapping from original community terms**: Consumer → client; Service Provider → server; User → resource owner; Consumer Key and Secret → client credentials; Request Token and Secret → temporary credentials; Access Token and Secret → token credentials.

## 1. Introduction (Condensed)
OAuth enables delegated access to protected resources. It introduces a third role (resource owner) to the traditional client-server model. The protocol consists of two parts: (1) a redirection-based user-agent process for end-users to authorize clients, and (2) a method for making authenticated HTTP requests using two sets of credentials (client and token). This specification documents OAuth Core 1.0 Revision A with errata corrections and editorial clarifications. The use of OAuth with any transport protocol other than HTTP [RFC2616] is undefined.

## 2. Redirection-Based Authorization
OAuth uses tokens to represent authorization granted to the client by the resource owner. This section defines a redirection-based method using three steps:

1. Client obtains temporary credentials from the server.
2. Resource owner authorizes the server to grant client access.
3. Client uses temporary credentials to request token credentials.

The server MUST revoke temporary credentials after a single use. It is RECOMMENDED that temporary credentials have a limited lifetime. Servers SHOULD enable resource owners to revoke token credentials.

The server must advertise three endpoints: Temporary Credential Request, Resource Owner Authorization, and Token Request. The URIs MAY include a query component, but the query MUST NOT contain any parameters beginning with "oauth_". Clients should not assume size limits for tokens.

### 2.1. Temporary Credentials
The client obtains temporary credentials by making an authenticated (Section 3) HTTP POST request to the Temporary Credential Request endpoint (unless another method is advertised). The request MUST include the REQUIRED parameter `oauth_callback` (an absolute URI for redirection after authorization; if no callback, MUST be "oob"). The client authenticates using only client credentials; the `oauth_token` parameter MAY be omitted and the token secret MUST be empty string.

**Security**: The server MUST require a transport-layer mechanism (e.g., TLS, SSL) because credentials are transmitted in plain text in the HTTP response.

The server MUST verify the request (Section 3.2) and respond with temporary credentials in the HTTP response body using `application/x-www-form-urlencoded` with a 200 status code. The response contains REQUIRED parameters: `oauth_token`, `oauth_token_secret`, and `oauth_callback_confirmed` (MUST be "true").

### 2.2. Resource Owner Authorization
Before requesting token credentials, the client MUST send the user to the server to authorize the request. The client constructs a request URI by adding the REQUIRED `oauth_token` parameter (temporary credentials identifier) to the Resource Owner Authorization endpoint URI. Servers MAY declare `oauth_token` as OPTIONAL if they provide alternative means. The request MUST use HTTP GET.

The server MUST verify the identity of the resource owner. It SHOULD present information about the client and indicate if the information has been verified. After authorization, the server MUST generate a verification code (unguessable value) and redirect the resource owner to the callback URI (if provided) with REQUIRED parameters `oauth_token` and `oauth_verifier`. If no callback, the server SHOULD display the verification code and instruct manual entry.

### 2.3. Token Credentials
The client obtains token credentials by making an authenticated (Section 3) HTTP POST request to the Token Request endpoint (unless another method advertised). The request MUST include the REQUIRED parameter `oauth_verifier`. The client authenticates using client credentials and temporary credentials (substituted for token credentials). The server MUST require a transport-layer mechanism (TLS/SSL).

The server MUST verify the request (Section 3.2), ensure authorization, check that temporary credentials are not expired or reused, and verify the verification code. If valid, the server responds with token credentials in `application/x-www-form-urlencoded` format with a 200 status code, including REQUIRED parameters `oauth_token` and `oauth_token_secret`. The server must retain the scope, duration, and other attributes approved by the resource owner.

## 3. Authenticated Requests
OAuth provides a method for including two sets of credentials in authenticated HTTP requests: client credentials and token credentials. This section defines how to make and verify requests, including signature methods.

### 3.1. Making Requests
An authenticated request includes protocol parameters with names beginning with "oauth_". The client assigns values to REQUIRED parameters (unless specified otherwise):

- `oauth_consumer_key`: client identifier
- `oauth_token`: token value (MAY be omitted if no token)
- `oauth_signature_method`: name of signature method (Section 3.4)
- `oauth_timestamp`: timestamp (Section 3.3) – MAY be omitted for "PLAINTEXT"
- `oauth_nonce`: nonce (Section 3.3) – MAY be omitted for "PLAINTEXT"
- `oauth_version`: OPTIONAL; if present, MUST be "1.0"

The parameters are added using one transmission method (Section 3.5). Each parameter MUST NOT appear more than once. The client calculates `oauth_signature` and adds it. Then sends the request.

### 3.2. Verifying Requests
Servers MUST validate by:
- Recalculating signature and comparing to `oauth_signature`
- If using "HMAC-SHA1" or "RSA-SHA1", ensuring nonce/timestamp/token combination has not been used before (MAY reject stale timestamps)
- If token present, verifying scope and status of authorization
- If `oauth_version` present, ensuring value is "1.0"

On failure, server SHOULD respond with appropriate HTTP status code. 400 (Bad Request) for unsupported parameters, missing parameters, duplicates. 401 (Unauthorized) for invalid credentials, invalid token, invalid signature, or used nonce.

### 3.3. Nonce and Timestamp
Timestamp MUST be a positive integer, expressed in seconds since Unix epoch (unless otherwise documented). Nonce is a random string unique across all requests with the same timestamp, client credentials, and token combination. Servers MAY restrict the time period for old timestamps to avoid infinite nonce storage.

### 3.4. Signature
OAuth provides three signature methods: "HMAC-SHA1", "RSA-SHA1", and "PLAINTEXT". The client declares the method via `oauth_signature_method`. Servers may define custom methods.

#### 3.4.1. Signature Base String
Used by "HMAC-SHA1" and "RSA-SHA1". Constructed by concatenating:
1. HTTP request method in uppercase (encoded if custom)
2. "&"
3. Base string URI (Section 3.4.1.2) encoded
4. "&"
5. Request parameters normalized (Section 3.4.1.3.2) encoded

#### 3.4.1.2. Base String URI
Construct an "http" or "https" URI from scheme, authority, path. Scheme and host MUST be lowercase. Port included if non-default; excluded if default (80 for HTTP, 443 for HTTPS).

#### 3.4.1.3. Request Parameters
Parameters from query, Authorization header, and entity-body (only if single-part, form-encoded, and Content-Type set to application/x-www-form-urlencoded) are collected. The `oauth_signature` parameter is excluded.

#### 3.4.1.3.2. Parameters Normalization
1. Encode each name and value per Section 3.6.
2. Sort by name (using ascending byte value ordering); if same name, sort by value.
3. Concatenate name and value with "=".
4. Join pairs with "&".

#### 3.4.2. HMAC-SHA1
`digest = HMAC-SHA1(key, text)`. `text` is signature base string. `key` is concatenation of encoded client shared-secret, "&", and encoded token shared-secret. `digest` is base64-encoded per [RFC2045] and used as `oauth_signature`.

#### 3.4.3. RSA-SHA1
Uses RSASSA-PKCS1-v1_5 with SHA-1. Client MUST have established RSA public key. `S = RSASSA-PKCS1-V1_5-SIGN(K, M)` where K is client's RSA private key, M is signature base string. S is base64-encoded. Server verifies with RSA public key.

#### 3.4.4. PLAINTEXT
No signature algorithm. MUST be used with transport-layer security (TLS/SSL). `oauth_signature` is concatenation of encoded client shared-secret, "&", and encoded token shared-secret.

### 3.5. Parameter Transmission
Protocol parameters (with "oauth_" prefix) SHALL be included in exactly one of the following locations (in order of preference):

1. HTTP "Authorization" header field (auth-scheme "OAuth") – Section 3.5.1
2. HTTP request entity-body (form-encoded) – Section 3.5.2
3. HTTP request URI query – Section 3.5.3

#### 3.5.1. Authorization Header
Parameters encoded per Section 3.6. Each parameter name, "=", quoted string value (MAY be empty). Parameters separated by ",". OPTIONAL "realm" per [RFC2617]. Servers MAY indicate support via "WWW-Authenticate" header.

#### 3.5.2. Form-Encoded Body
Only if entity-body is single-part, form-encoded, and Content-Type is application/x-www-form-urlencoded. Protocol parameters SHOULD be appended after request-specific parameters separated by "&".

#### 3.5.3. Request URI Query
Parameters added as query component per [RFC3986]. Other query parameters allowed; protocol parameters SHOULD be appended after request-specific parameters.

### 3.6. Percent Encoding
Used for signature base string and Authorization header. Text values first encoded as UTF-8 octets, then percent-encoded: unreserved characters (ALPHA, DIGIT, "-", ".", "_", "~") MUST NOT be encoded; all others MUST be encoded; hexadecimal characters MUST be uppercase. This differs from `application/x-www-form-urlencoded` (e.g., space as "%20", not "+").

## 4. Security Considerations (Condensed)
Key security considerations from the specification:

- **RSA-SHA1**: Relies solely on secrecy of client's private key.
- **Confidentiality**: OAuth does not guarantee request confidentiality; use transport-layer security for sensitive data.
- **Spoofing**: No server authentication; use TLS to verify server identity.
- **Proxying/Caching**: Without Authorization header, caches may fail to protect authenticated content. Servers not using Authorization header should use Cache-Control.
- **Plaintext Storage**: Secrets must be stored in plaintext for signature computation; servers must protect them from unauthorized access.
- **Secrecy of Client Credentials**: Client credentials may be exposed in desktop apps; servers should not rely solely on them.
- **Phishing**: Redirecting users for authorization may enable phishing; servers should educate users and provide authenticity verification.
- **Scoping**: Protocol does not provide access scoping; servers should implement granular access controls.
- **Entropy of Secrets**: Use long, random secrets to resist brute-force attacks. Use cryptographically secure PRNGs.
- **Denial-of-Service**: Tracking nonces and signature verification may be exploited; implementers should consider resource exhaustion.
- **SHA-1 Attacks**: Known weaknesses in SHA-1 may affect "RSA-SHA1" more than "HMAC-SHA1". Servers should assess risk.
- **Signature Base String Limitations**: Does not cover entire request; use additional protections for excluded elements.
- **CSRF**: Servers should implement CSRF prevention on authorization endpoints. Clients should prevent CSRF on callback URIs.
- **UI Redress (Clickjacking)**: Servers should use frame-busting, require JavaScript, or re-authenticate.
- **Automatic Processing of Repeat Authorizations**: May exacerbate credential theft risks; servers may limit token scope; clients should protect credentials.

## Appendix A. Differences from the Community Edition (Condensed)
- Changed TLS/SSL requirement from SHOULD to MUST for "PLAINTEXT" and for requesting temporary/token credentials.
- Adjusted nonce uniqueness to be per token/timestamp/client combination.
- Removed requirement that timestamps be non-decreasing.
- Made nonce/timestamp OPTIONAL for "PLAINTEXT".
- Extended signature base string to include entity-body parameters for non-POST methods and query parameters for non-GET methods.
- Corrected encoding instructions to avoid double-encoding.
- Allowed omitting empty `oauth_token` parameter.
- Permitted empty `oauth_token` in temporary credentials request.
- Removed restrictions on additional "oauth_" parameters.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R01 | Server MUST revoke temporary credentials after single use | MUST | Section 2 |
| R02 | Temporary credentials SHOULD have limited lifetime | SHOULD | Section 2 |
| R03 | Servers SHOULD enable resource owners to revoke token credentials | SHOULD | Section 2 |
| R04 | Temporary Credential Request endpoint URI query MUST NOT contain parameters beginning with "oauth_" | MUST | Section 2 |
| R05 | Client MUST include `oauth_callback` in temporary credentials request; if no callback, MUST be "oob" | MUST | Section 2.1 |
| R06 | Server MUST require transport-layer mechanism for temporary and token credential requests | MUST | Sections 2.1, 2.3 |
| R07 | Server MUST verify temporary credentials request per Section 3.2 | MUST | Section 2.1 |
| R08 | Response to temporary credentials request MUST include `oauth_token`, `oauth_token_secret`, and `oauth_callback_confirmed` set to "true" | MUST | Section 2.1 |
| R09 | Client MUST send user to server for authorization before requesting token credentials | MUST | Section 2.2 |
| R10 | Client MUST use HTTP GET for Resource Owner Authorization request | MUST | Section 2.2 |
| R11 | Server MUST verify identity of resource owner | MUST | Section 2.2 |
| R12 | Server MUST generate verification code and redirect with `oauth_token` and `oauth_verifier` | MUST | Section 2.2 |
| R13 | Client MUST include `oauth_verifier` when requesting token credentials | MUST | Section 2.3 |
| R14 | Server MUST verify token request: check authorization, temporary credentials validity, verification code | MUST | Section 2.3 |
| R15 | Response to token request MUST include `oauth_token` and `oauth_token_secret` | MUST | Section 2.3 |
| R16 | Client MUST assign values to `oauth_consumer_key`, `oauth_signature_method`, `oauth_timestamp` (unless PLAINTEXT), `oauth_nonce` (unless PLAINTEXT); `oauth_token` MAY be omitted | MUST/MAY | Section 3.1 |
| R17 | `oauth_version` if present MUST be "1.0" | MUST | Section 3.1 |
| R18 | Each protocol parameter MUST NOT appear more than once per request | MUST | Section 3.1 |
| R19 | Servers MUST recalculate signature and compare | MUST | Section 3.2 |
| R20 | Timestamp MUST be a positive integer | MUST | Section 3.3 |
| R21 | Nonce MUST be unique across requests with same timestamp, client credentials, token | MUST | Section 3.3 |
| R22 | PLAINTEXT signature method MUST be used with transport-layer security | MUST | Section 3.4.4 |
| R23 | Protocol parameters SHALL be included in exactly one of: Authorization header, form-encoded body, or URI query | SHALL | Section 3.5 |
| R24 | Percent encoding: unreserved characters MUST NOT be encoded; others MUST be encoded; hex characters MUST be uppercase | MUST | Section 3.6 |

## Informative Annexes (Condensed)
- **Example (Section 1.2)**: Illustrates the full OAuth flow with a photo printing service scenario, showing HTTP requests and responses. Retained for context.
- **Acknowledgments (Section 5)**: Lists contributors to the specification.
- **Differences from Community Edition (Appendix A)**: Describes errata corrections, mainly tightening security requirements and clarifying parameter handling.