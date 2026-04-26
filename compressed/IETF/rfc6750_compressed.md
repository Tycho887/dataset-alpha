# RFC 6750: The OAuth 2.0 Authorization Framework: Bearer Token Usage
**Source**: IETF | **Version**: Standards Track | **Date**: October 2012 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6750

## Scope (Summary)
Defines methods for using bearer tokens in HTTP requests to access OAuth 2.0 protected resources. Describes three ways to transmit bearer tokens (Authorization header, form-encoded body, URI query) and the resource server’s WWW-Authenticate error responses. Mandates TLS for all token transport.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2246] Dierks, T. and C. Allen, "The TLS Protocol Version 1.0", RFC 2246, January 1999.
- [RFC2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC2617] Franks, J., et al., "HTTP Authentication: Basic and Digest Access Authentication", RFC 2617, June 1999.
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [RFC6265] Barth, A., "HTTP State Management Mechanism", RFC 6265, April 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [USASCII] American National Standards Institute, "Coded Character Set -- 7-bit American Standard Code for Information Interchange", ANSI X3.4, 1986.
- [W3C.REC-html401-19991224] Raggett, D., et al., "HTML 4.01 Specification", W3C REC, December 1999.
- [W3C.REC-webarch-20041215] Jacobs, I. and N. Walsh, "Architecture of the World Wide Web, Volume One", W3C REC, December 2004.

## Definitions and Abbreviations
- **Bearer Token**: A security token with the property that any party in possession of the token (a "bearer") can use the token in any way that any other party in possession of it can. Using a bearer token does not require a bearer to prove possession of cryptographic key material (proof-of-possession).
- **Other terms**: As defined in "The OAuth 2.0 Authorization Framework" [RFC6749] (e.g., access token, authorization server, resource server, client, resource owner).

## 1. Introduction
### 1.1. Notational Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.
- ABNF notation per RFC 5234, with rules from RFC 2617 (auth-param, auth-scheme) and RFC 3986 (URI-reference).
- Unless otherwise noted, all protocol parameter names and values are case sensitive.

### 1.2. Terminology
- **Bearer Token**: [definition above]

### 1.3. Overview
- Abstract OAuth 2.0 flow (Figure 1) consists of steps:
  - (A) Authorization Request, (B) Authorization Grant, (C) Authorization Grant to Authorization Server, (D) Access Token, (E) Access Token to Resource Server, (F) Protected Resource.
- Steps (E) and (F) are specified in this document, plus semantic requirements on the access token returned in step (D).

## 2. Authenticated Requests
- **Clients MUST NOT use more than one method to transmit the token in each request.**

### 2.1. Authorization Request Header Field
- **Syntax**: `credentials = "Bearer" 1*SP b64token` where `b64token = 1*( ALPHA / DIGIT / "-" / "." / "_" / "~" / "+" / "/" ) *"="`.
- Example:
  ```
  GET /resource HTTP/1.1
  Host: server.example.com
  Authorization: Bearer mF_9.B5f-4.1JqM
  ```
- **Normative**: Clients SHOULD use the "Authorization" request header field with the "Bearer" scheme. Resource servers MUST support this method.

### 2.2. Form-Encoded Body Parameter
- **Conditions** (all MUST be met): Content-Type set to `application/x-www-form-urlencoded`; entity-body follows HTML 4.01 encoding; request entity-body is single-part; content consists entirely of ASCII; HTTP method MUST NOT be GET (i.e., POST, etc.).
- **Parameter**: `access_token` in request-body, separated by `&` from other parameters.
- Example:
  ```
  POST /resource HTTP/1.1
  Host: server.example.com
  Content-Type: application/x-www-form-urlencoded
  access_token=mF_9.B5f-4.1JqM
  ```
- **Normative**: SHOULD NOT be used except where browsers lack access to Authorization header. Resource servers MAY support this method.

### 2.3. URI Query Parameter
- **Parameter**: `access_token` in the query component of the request URI.
- Example:
  ```
  GET /resource?access_token=mF_9.B5f-4.1JqM HTTP/1.1
  Host: server.example.com
  ```
- **Normative**: Clients using this method SHOULD also send a `Cache-Control: no-store` header. Server success responses (2XX) SHOULD contain `Cache-Control: private`.
- **Security warning**: SHOULD NOT be used unless impossible to use Authorization header or body. Resource servers MAY support this method.
- **Note**: Method is included for documentation; its use is not recommended due to security deficiencies and reserved query parameter name.

## 3. The WWW-Authenticate Response Header Field
- **Resource server MUST** include the HTTP `WWW-Authenticate` response header when the request lacks authentication credentials or the access token does not enable access. It MAY include it in other conditions.
- **auth-scheme**: MUST be `Bearer`.
- **auth-param attributes**:
  - `realm` (MAY appear, MUST NOT appear more than once)
  - `scope` (OPTIONAL, space-delimited list of case-sensitive scope values; MUST NOT appear more than once; intended for programmatic use)
  - `error` (SHOULD include if access token failed authentication)
  - `error_description` (MAY include, human-readable, not for end-user)
  - `error_uri` (MAY include, absolute URI for human-readable error page)
  - `error`, `error_description`, `error_uri` MUST NOT appear more than once.
- **Character restrictions**: scope values: `%x21 / %x23-5B / %x5D-7E` plus `%x20` delimiter. error and error_description: `%x20-21 / %x23-5B / %x5D-7E`. error_uri: must conform to URI-reference syntax (`%x21 / %x23-5B / %x5D-7E`).
- Examples:
  - No authentication: `HTTP/1.1 401 Unauthorized` with `WWW-Authenticate: Bearer realm="example"`
  - Expired token: `HTTP/1.1 401 Unauthorized` with `WWW-Authenticate: Bearer realm="example", error="invalid_token", error_description="The access token expired"`

### 3.1. Error Codes
- **invalid_request**: Missing required parameter, unsupported parameter or value, repeated parameter, multiple token methods, or otherwise malformed. Resource server SHOULD respond with HTTP 400 (Bad Request).
- **invalid_token**: Access token expired, revoked, malformed, or invalid. Resource SHOULD respond with HTTP 401 (Unauthorized). Client MAY request a new token.
- **insufficient_scope**: Request requires higher privileges. Resource server SHOULD respond with HTTP 403 (Forbidden) and MAY include `scope` attribute with required scope.
- If request lacks any authentication information, resource server SHOULD NOT include an error code or error information.

## 4. Example Access Token Response (Informative)
- Typical OAuth 2.0 response:
  ```
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache

  {
    "access_token":"mF_9.B5f-4.1JqM",
    "token_type":"Bearer",
    "expires_in":3600,
    "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA"
  }
  ```

## 5. Security Considerations
### 5.1. Security Threats (Summary)
- Token manufacture/modification, token disclosure, token redirect, token replay.

### 5.2. Threat Mitigation (Condensed with preserved normative statements)
- Token integrity protection MUST be sufficient to prevent modification (digital signature, MAC, or reference).
- Authorization server MUST include audience (identity of intended recipients) in token to prevent redirect. Restricting scope is RECOMMENDED.
- Authorization server MUST implement TLS. At time of writing, TLS 1.0 most widely deployed; TLS 1.2 most recent.
- Confidentiality protection MUST be applied using TLS with ciphersuite providing confidentiality and integrity. TLS is mandatory to implement and to use.
- If client cannot observe token contents, token encryption MUST be applied in addition to TLS.
- Client MUST validate TLS certificate chain when making requests to protected resources (including CRL).
- Bearer tokens MUST NOT be stored in cookies that can be sent in the clear.
- In deployments with load balancers terminating TLS, sufficient measures MUST be employed to ensure confidentiality of token between front-end and back-end servers (e.g., token encryption).
- Token lifetime MUST be limited (e.g., validity time field). Short-lived tokens (one hour or less) reduce impact.
- Client MUST verify identity of resource server per RFC 2818 Section 3.1 when presenting token.

### 5.3. Summary of Recommendations
- **Safeguard bearer tokens**: Client implementations MUST ensure bearer tokens are not leaked to unintended parties.
- **Validate TLS certificate chains**: Client MUST validate TLS certificate chain when making requests to protected resources.
- **Always use TLS (https)**: Clients MUST always use TLS (https) or equivalent transport security when making requests with bearer tokens.
- **Don't store bearer tokens in cookies**: Implementations MUST NOT store bearer tokens within cookies that can be sent in the clear. If stored, MUST take precautions against CSRF.
- **Issue short-lived bearer tokens**: Token servers SHOULD issue short-lived (one hour or less) bearer tokens, particularly in browser or leak-prone environments.
- **Issue scoped bearer tokens**: Token servers SHOULD issue bearer tokens containing an audience restriction.
- **Don't pass bearer tokens in page URLs**: Bearer tokens SHOULD NOT be passed in page URLs; SHOULD be passed in HTTP headers or message bodies with confidentiality measures.

## 6. IANA Considerations (Condensed)
### 6.1. OAuth Access Token Type Registration
- **Type name**: Bearer
- **HTTP Authentication Scheme**: Bearer
- **Change controller**: IETF
- **Specification**: RFC 6750

### 6.2. OAuth Extensions Error Registration
- **invalid_request**: Used in resource access error response; related to Bearer access token type.
- **invalid_token**: Used in resource access error response; related to Bearer access token type.
- **insufficient_scope**: Used in resource access error response; related to Bearer access token type.

## 7. References
- **Normative**: As listed above.
- **Informative**: [HTTP-AUTH], [NIST800-63], [OMAP], [OpenID.Messages] – see original RFC for details.

## Appendix A. Acknowledgements (Condensed)
- Contributors from OAuth community, WRAP community, and OAuth Working Group. David Recordon created preliminary version; Michael B. Jones authored first version and all subsequent versions. Many individuals contributed ideas and wording.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Clients MUST NOT use more than one method to transmit the token in each request. | MUST | Section 2 |
| R2 | Clients SHOULD use the "Authorization" request header field with the "Bearer" scheme. | SHOULD | Section 2.1 |
| R3 | Resource servers MUST support the Authorization header method. | MUST | Section 2.1 |
| R4 | Clients MUST NOT use form-encoded body unless all conditions (Content-Type, single-part, ASCII, method not GET) are met. | MUST | Section 2.2 |
| R5 | Resource servers SHOULD NOT use form-encoded body except when browsers lack Authorization header. | SHOULD | Section 2.2 |
| R6 | Resource servers MAY support form-encoded body method. | MAY | Section 2.2 |
| R7 | Clients using URI query parameter method SHOULD send Cache-Control: no-store. | SHOULD | Section 2.3 |
| R8 | Server success responses to URI query method requests SHOULD contain Cache-Control: private. | SHOULD | Section 2.3 |
| R9 | URI query method SHOULD NOT be used unless impossible to use Authorization header or body. | SHOULD | Section 2.3 |
| R10 | Resource servers MAY support URI query method. | MAY | Section 2.3 |
| R11 | Resource server MUST include WWW-Authenticate header when request lacks authentication or token does not enable access. | MUST | Section 3 |
| R12 | All challenges MUST use auth-scheme "Bearer". | MUST | Section 3 |
| R13 | realm attribute MUST NOT appear more than once. | MUST | Section 3 |
| R14 | scope attribute is OPTIONAL, MUST NOT appear more than once. | OPTIONAL / MUST | Section 3 |
| R15 | error, error_description, error_uri attributes MUST NOT appear more than once. | MUST | Section 3 |
| R16 | Resource server SHOULD include error attribute when token fails authentication. | SHOULD | Section 3 |
| R17 | Resource server SHOULD respond with HTTP 400 for invalid_request. | SHOULD | Section 3.1 |
| R18 | Resource SHOULD respond with HTTP 401 for invalid_token. | SHOULD | Section 3.1 |
| R19 | Resource server SHOULD respond with HTTP 403 for insufficient_scope. | SHOULD | Section 3.1 |
| R20 | Resource server SHOULD NOT include error code if request lacks authentication. | SHOULD | Section 3.1 |
| R21 | Token integrity protection MUST be sufficient to prevent modification. | MUST | Section 5.2 |
| R22 | Authorization server MUST implement TLS. | MUST | Section 5.2 |
| R23 | Confidentiality protection MUST be applied using TLS with ciphersuite providing confidentiality and integrity. | MUST | Section 5.2 |
| R24 | Client MUST validate TLS certificate chain when making requests to protected resources (including CRL). | MUST | Section 5.2 |
| R25 | Bearer tokens MUST NOT be stored in cookies that can be sent in the clear. | MUST | Section 5.2 |
| R26 | In load-balanced deployments, sufficient measures MUST be employed for token confidentiality between front-end and back-end (e.g., token encryption). | MUST | Section 5.2 |
| R27 | Token lifetime MUST be limited (e.g., validity time field). | MUST | Section 5.2 |
| R28 | Client MUST verify identity of resource server per RFC 2818 Sec 3.1 when presenting token. | MUST | Section 5.2 |
| R29 | Client implementations MUST ensure bearer tokens are not leaked to unintended parties. | MUST | Section 5.3 |
| R30 | Clients MUST always use TLS (https) or equivalent transport security when making requests with bearer tokens. | MUST | Section 5.3 |
| R31 | Implementations MUST NOT store bearer tokens within cookies that can be sent in the clear. | MUST | Section 5.3 |
| R32 | Token servers SHOULD issue short-lived (one hour or less) bearer tokens. | SHOULD | Section 5.3 |
| R33 | Token servers SHOULD issue bearer tokens containing an audience restriction. | SHOULD | Section 5.3 |
| R34 | Bearer tokens SHOULD NOT be passed in page URLs; SHOULD be passed in HTTP headers or message bodies with confidentiality measures. | SHOULD | Section 5.3 |