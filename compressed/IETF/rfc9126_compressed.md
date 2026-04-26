# RFC 9126: OAuth 2.0 Pushed Authorization Requests
**Source**: IETF | **Version**: Standards Track | **Date**: September 2021 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9126

## Scope (Summary)
Defines the pushed authorization request (PAR) endpoint, allowing OAuth 2.0 clients to push authorization request payloads directly to the authorization server via a direct request, receiving a request URI used as a reference in a subsequent authorization request. This enhances security by providing confidentiality, integrity, and early client authentication.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017
- [RFC8414] Jones, M., Sakimura, N., and J. Bradley, "OAuth 2.0 Authorization Server Metadata", RFC 8414, June 2018
- [RFC9101] Sakimura, N., Bradley, J., and M. Jones, "The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)", RFC 9101, August 2021

## Definitions and Abbreviations
- **Access token**: As defined in [RFC6749]
- **Authorization server**: As defined in [RFC6749]
- **Authorization endpoint**: As defined in [RFC6749]
- **Authorization request**: As defined in [RFC6749]
- **Token endpoint**: As defined in [RFC6749]
- **Client**: As defined in [RFC6749]
- **PAR**: Pushed Authorization Request
- **JAR**: JWT-Secured Authorization Request [RFC9101]
- **Request Object**: A JWT as defined in [RFC9101]
- **Request URI**: A URI referencing the pushed authorization request data, bound to the client and single-use per authorization request

## Pushed Authorization Request Endpoint
### 2.1 Request
- The PAR endpoint accepts HTTP POST requests with `application/x-www-form-urlencoded` body using UTF-8 encoding (Appendix B of [RFC6749]). The endpoint URL **MUST** use the `https` scheme.
- Authorization servers supporting PAR **SHOULD** include the endpoint URL in metadata via `pushed_authorization_request_endpoint` (Section 5).
- The endpoint accepts authorization request parameters as defined in [RFC6749] and all applicable extensions (e.g., PKCE [RFC7636], Resource Indicators [RFC8707], OIDC [OIDC]). It **MAY** also accept a JWT Request Object per Section 3.
- Client authentication rules from [RFC6749] for token endpoint apply; `token_endpoint_auth_method` client metadata indicates the method. The `token_endpoint_auth_methods_supported` server metadata lists supported methods.
- To resolve audience ambiguity for JWT client assertions, the issuer identifier URL [RFC8414] **SHOULD** be used as audience. The authorization server **MUST** accept its issuer identifier, token endpoint URL, or PAR endpoint URL as audience values.
- The client sends parameters directly to the PAR endpoint; `request_uri` **MUST NOT** be provided.
- Client authentication parameters (e.g., `client_secret`, `client_assertion`) are used only for authentication; `client_id` is required.
- The authorization server **MUST** process as follows:
    1. Authenticate the client as at token endpoint (Section 2.3 of [RFC6749]).
    2. Reject if `request_uri` is provided.
    3. Validate the pushed request as it would an authorization request sent to the authorization endpoint (e.g., check redirect URI, scope). The server **MAY** omit validation steps it cannot perform at this stage, but **MUST** perform them at the authorization endpoint.

### 2.2 Successful Response
- The server **MUST** generate a request URI and respond with HTTP 201 and JSON body containing:
  - `request_uri`: A single-use reference to the request data. Its format is at server discretion but **MUST** contain cryptographically strong random part (per Section 10.10 of [RFC6749]). **MUST** be bound to the client.
  - `expires_in`: Lifetime in seconds as a positive integer (recommended 5-600 seconds).
- Example response: `{"request_uri": "urn:ietf:params:oauth:request_uri:6esc_11ACC5bwc014ltc14eY22c", "expires_in": 60}`

### 2.3 Error Response
- Error response uses same format as token endpoint errors (Section 5.2 of [RFC6749]) using appropriate error codes from Section 4.1.2.1 of [RFC6749] or extensions. For cases where Section 4.1.2.1 prohibits redirect, use `invalid_request`.
- If client is required to use signed Request Objects (per server policy or [RFC9101] Section 10.5), the server **MUST** only accept requests per Section 3 and **MUST** refuse others with HTTP 400 and `invalid_request`.
- Additional HTTP status codes: 405 (Method Not Allowed), 413 (Payload Too Large), 429 (Too Many Requests).

### 2.4 Management of Client Redirect URIs
- The exact matching requirement for `redirect_uri` **MAY** be relaxed for authenticated clients using PAR. The server **MAY** allow such clients to specify unregistered redirect URIs, subject to server restrictions (e.g., required prefix, only varying query parameter).
- This is possible because the server authenticates the client before the authorization process starts, thus ensuring interaction with the legitimate client.

## The "request" Request Parameter (Section 3)
- Clients **MAY** use the `request` parameter as defined in JAR [RFC9101] to push a Request Object JWT.
- Processing, signing, and encryption rules from JAR apply. Only client authentication parameters and `request` are sent in the form body; all authorization request parameters **MUST** appear as claims in the JWT.
- The authorization server **MUST** additionally:
    1. Decrypt the Request Object if applicable (JAR Section 6.1).
    2. Validate the signature (JAR Section 6.2).
    3. Reject if authenticated `client_id` does not match `client_id` claim in the Request Object. Server **MAY** require `iss` claim to match `client_id`.

## Authorization Request (Section 4)
- The client uses the `request_uri` to build an authorization request as per [RFC9101]; example: `GET /authorize?client_id=...&request_uri=...`
- The client **MUST** only use a `request_uri` value once. Servers **SHOULD** treat as one-time use but **MAY** allow for user reloading/refreshing. An expired `request_uri` **MUST** be rejected.
- The server **MUST** validate the authorization request as usual, but **MAY** omit validation steps already performed when pushed, provided it can verify the request was pushed and policy unchanged.
- Server policy **MAY** require PAR as the only means to pass authorization request data; in that case, the server will refuse requests without a `request_uri` obtained from the PAR endpoint, using `invalid_request`.

## Authorization Server Metadata (Section 5)
- `pushed_authorization_request_endpoint`: URL of the PAR endpoint.
- `require_pushed_authorization_requests`: Boolean (default false) indicating if the server accepts authorization request data only via PAR.

## Client Metadata (Section 6)
- `require_pushed_authorization_requests`: Boolean (default false) indicating that the client is required to use PAR to initiate authorization requests.

## Security Considerations
### 7.1 Request URI Guessing
- Server **MUST** ensure request URI entropy as per JAR [RFC9101], Section 10.2, clause (d).

### 7.2 Open Redirection
- Server **MUST** only accept new redirect URIs in pushed requests from authenticated clients.

### 7.3 Request Object Replay
- Server **SHOULD** make request URIs one-time use.

### 7.4 Client Policy Change
- Server **SHOULD** check request parameters against client policy when processing the authorization request.

### 7.5 Request URI Swapping
- Clients **SHOULD** use PKCE [RFC7636], unique `state` parameter [RFC6749], or OIDC `nonce` parameter [OIDC] in the pushed Request Object to prevent swapping attacks.

## Privacy Considerations
- Using PAR improves privacy by passing authorization request data directly between client and server over a secure connection in the HTTP body, rather than in the URL query component that passes through the user agent in the clear.

## IANA Considerations
- **Authorization Server Metadata**: Registered `pushed_authorization_request_endpoint` and `require_pushed_authorization_requests`.
- **Dynamic Client Registration Metadata**: Registered `require_pushed_authorization_requests`.
- **OAuth URI**: Registered `urn:ietf:params:oauth:request_uri:` sub-namespace.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | PAR endpoint URL MUST use https | shall | Section 2 |
| R2 | Authorization servers SHOULD include PAR endpoint URL in metadata | should | Section 2 |
| R3 | request_uri MUST NOT be provided in pushed request | shall | Section 2.1 |
| R4 | Server MUST authenticate client as for token endpoint | shall | Section 2.1 |
| R5 | Server MUST reject if request_uri provided | shall | Section 2.1 |
| R6 | Server MUST validate pushed request as for authorization endpoint (with possible omissions) | shall | Section 2.1 |
| R7 | Server MUST generate request URI on success with HTTP 201 | shall | Section 2.2 |
| R8 | request_uri MUST contain cryptographically strong random part | shall | Section 2.2 |
| R9 | request_uri MUST be bound to the client | shall | Section 2.2 |
| R10 | Server MUST use error format from token endpoint | shall | Section 2.3 |
| R11 | If signed Request Object required, server MUST accept only that and refuse others with 400 invalid_request | shall | Section 2.3 |
| R12 | Client MUST use request_uri only once | shall | Section 4 |
| R13 | Expired request_uri MUST be rejected | shall | Section 4 |
| R14 | Server MUST validate authorization request arising from PAR | shall | Section 4 |
| R15 | Server MAY require PAR as only means (policy) | may | Section 4 |
| R16 | For JWT audience, server MUST accept its issuer, token endpoint, or PAR endpoint | shall | Section 2 |
| R17 | Server MUST check authenticated client_id matches Request Object client_id if present | shall | Section 3 |
| R18 | Server SHOULD make request URIs one-time use | should | Section 2.2, 7.3 |
| R19 | Server MUST only accept new redirect URIs from authenticated clients | shall | Section 7.2 |
| R20 | Client SHOULD use PKCE/state/nonce to prevent request URI swapping | should | Section 7.5 |

## Informative Annexes (Condensed)
- **Security BCP and OAuth 2.1**: [OAUTH-SECURITY-TOPICS] and [OAUTH-V2] are informative references that recommend exact redirect URI matching, which PAR may relax for authenticated clients.
- **OIDC and Discovery**: [OIDC] and [OIDC.Disco] are informative references for OpenID Connect extensions that may be used with PAR (e.g., nonce, metadata).
- **Examples**: Sections 1.1 and 2.1 provide illustrative examples of PAR request/response flows; these are non-normative.