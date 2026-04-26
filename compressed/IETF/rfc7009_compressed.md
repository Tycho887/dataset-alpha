# RFC 7009: OAuth 2.0 Token Revocation
**Source**: IETF | **Version**: Standards Track | **Date**: August 2013 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc7009

## Scope (Summary)
This specification defines a token revocation endpoint for OAuth 2.0 authorization servers, enabling clients to invalidate previously issued refresh or access tokens. Revocation may also cascade to related tokens and the underlying authorization grant.

## Normative References
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- [RFC5226] – Guidelines for Writing an IANA Considerations Section in RFCs (BCP 26)
- [RFC5246] – The Transport Layer Security (TLS) Protocol Version 1.2
- [RFC6749] – The OAuth 2.0 Authorization Framework

## Definitions and Abbreviations
- **token**: A string representing an authorization grant issued by the resource owner to the client (per RFC6749).
- **access_token**: An access token as defined in RFC6749 Section 1.4.
- **refresh_token**: A refresh token as defined in RFC6749 Section 1.5.
- **token_type_hint**: Optional parameter indicating the type of token submitted for revocation.

## 1. Introduction
The OAuth 2.0 core specification (RFC6749) defines ways to obtain tokens. This supplement provides a mechanism to revoke refresh and access tokens. Revocation invalidates the actual token and, if applicable, other tokens based on the same authorization grant, enabling cleanup of security credentials and improved user experience.

### 1.1. Requirements Language
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2. Token Revocation
- **R1**: Implementations **MUST** support revocation of refresh tokens.
- **R2**: Implementations **SHOULD** support revocation of access tokens.
- **R3**: The client requests revocation by making an HTTP POST request to the token revocation endpoint URL.
- **R4**: The revocation endpoint URL **MUST** conform to the rules in RFC6749 Section 3.1.
- **R5**: Clients **MUST** verify the URL is an HTTPS URL.
- **R6**: The authorization server **MUST** use TLS (RFC5246) in a version compliant with RFC6749 Section 1.6.
- **R7**: If the host is also reachable over HTTP, the server **SHOULD** offer a revocation service at the HTTP URI but **MUST NOT** publish it as a token revocation endpoint.

### 2.1. Revocation Request
- **token** (REQUIRED): The token to be revoked.
- **token_type_hint** (OPTIONAL): A hint about the token type. Values: `access_token` or `refresh_token`. If the server cannot locate the token using the hint, it **MUST** extend its search across all supported token types. The server **MAY** ignore this parameter.
- The client includes its authentication credentials as described in RFC6749 Section 2.3.

- **R8**: The authorization server first validates client credentials; if they fail, the request is refused and an error is returned.
- **R9**: The server then invalidates the token immediately; the token cannot be used after revocation.
- **R10**: Clients **must not** try to use the token after receipt of an HTTP 200 response.
- **R11**: If the token is a refresh token and the server supports access token revocation, the server **SHOULD** also invalidate all access tokens based on the same authorization grant.
- **R12**: If the token is an access token, the server **MAY** revoke the respective refresh token.

### 2.2. Revocation Response
- **R13**: The authorization server responds with HTTP status code 200 if the token has been revoked successfully or if the client submitted an invalid token.
- The response body content is ignored by the client.
- An invalid token type hint value is ignored and does not influence the response.

#### 2.2.1. Error Response
- Error format conforms to RFC6749 Section 5.2.
- Additional error code: `unsupported_token_type` – the server does not support revocation of the presented token type.
- **R14**: If the server responds with HTTP 503, the client **must** assume the token still exists and **may** retry after a reasonable delay; server **may** include a `Retry-After` header.

### 2.3. Cross-Origin Support
- The revocation endpoint **MAY** support CORS (W3C.WD-cors-20120403) for user-agent-based applications.
- **MAY** also offer JSONP via GET requests with an optional `callback` parameter.

## 3. Implementation Note (Informative)
Access tokens may be self-contained (stateless) or referential (requiring server lookup). Revocation capability depends on token style. For self-contained tokens, immediate revocation may require non-standard backend interaction; short-lived tokens with refresh are an alternative design.

## 4. IANA Considerations
### 4.1. OAuth Extensions Error Registration
Registers `unsupported_token_type` error value for revocation endpoint.

### 4.1.2. OAuth Token Type Hints Registry
Establishes a new registry for `token_type_hint` values. Registration requires Specification Required (RFC5226) with review on oauth-ext-review@ietf.org.

#### 4.1.2.2. Initial Registry Contents

| Hint Value     | Change Controller | Reference |
|----------------|-------------------|-----------|
| `access_token` | IETF              | RFC 7009  |
| `refresh_token`| IETF              | RFC 7009  |

## 5. Security Considerations
- If the server does not support access token revocation, access tokens are not immediately invalidated when the refresh token is revoked – deployments must account for this in risk analysis.
- Revocation reduces abuse of abandoned tokens; see RFC6749 Section 10 and RFC6819 for broader security discussion.
- **R15**: Appropriate countermeasures against denial-of-service attacks **MUST** be applied to the revocation endpoint (see RFC6819 Section 4.4.1.11).
- **R16**: Care **MUST** be taken to prevent malicious clients from exploiting invalid token type hints to launch DoS.
- **R17**: Clients **MUST** authenticate the revocation endpoint (e.g., certificate validation) to detect counterfeit endpoints.
- Token guessing attack is mitigated because token must belong to the requesting client and valid client credentials are required.

## Requirements Summary
| ID  | Requirement | Type | Reference |
|-----|-------------|------|-----------|
| R1  | Implementations MUST support revocation of refresh tokens. | shall | Section 2 |
| R2  | Implementations SHOULD support revocation of access tokens. | should | Section 2 |
| R3  | Client makes HTTP POST to token revocation endpoint URL. | shall | Section 2 |
| R4  | Revocation endpoint URL MUST conform to RFC6749 Section 3.1. | shall | Section 2 |
| R5  | Clients MUST verify URL is HTTPS. | shall | Section 2 |
| R6  | Authorization server MUST use TLS (RFC5246) per RFC6749 Section 1.6. | shall | Section 2 |
| R7  | Server SHOULD offer revocation at HTTP URI but MUST NOT publish as endpoint. | shall/should | Section 2 |
| R8  | Server validates client credentials; request refused if invalid. | shall | Section 2.1 |
| R9  | Token invalidated immediately; cannot be used after revocation. | shall | Section 2.1 |
| R10 | Clients must not use token after HTTP 200 response. | must (normative) | Section 2.1 |
| R11 | If refresh token revoked, server SHOULD invalidate all access tokens on same grant. | should | Section 2.1 |
| R12 | If access token revoked, server MAY revoke refresh token. | may | Section 2.1 |
| R13 | Server responds with HTTP 200 on successful revocation or invalid token. | shall | Section 2.2 |
| R14 | On HTTP 503, client must assume token exists and may retry; server may include Retry-After. | must/may | Section 2.2.1 |
| R15 | DoS countermeasures MUST be applied to revocation endpoint (per RFC6819). | shall | Section 5 |
| R16 | Care MUST be taken to prevent DoS via invalid token type hints. | shall | Section 5 |
| R17 | Clients MUST authenticate the revocation endpoint. | shall | Section 5 |

## Informative Annexes (Condensed)
- **Annex A (Implementation Note)**: Discusses token styles (self-contained vs. referential) and their impact on revocation capabilities; recommends short-lived access tokens with refresh for practical revocation.
- **Annex B (Security Considerations)**: Highlights risks of incomplete revocation cascading, token guessing, and DoS; provides normative requirements to mitigate threats.