# RFC 7662: OAuth 2.0 Token Introspection
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track, October 2015 | **Date**: October 2015 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7662

## Scope (Summary)
Defines a protocol for a protected resource to query an OAuth 2.0 authorization server to determine the active state of an OAuth 2.0 token and to obtain meta-information about the token, such as scopes, client ID, and authorization context.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels"
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs"
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2"
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)"
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework"
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage"
- [RFC7009] Lodderstedt, T., et al., "OAuth 2.0 Token Revocation"
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format"
- [RFC7231] Fielding, R., Ed. and J. Reschke, Ed., "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content"
- [RFC7519] Jones, M., et al., "JSON Web Token (JWT)"
- [W3C.REC-html5-20141028] Hickson, I., et al., "HTML5"

## Definitions and Abbreviations
- **Token Introspection**: The act of inquiring about the current state of an OAuth 2.0 token through use of the network protocol defined in this document.
- **Introspection Endpoint**: The OAuth 2.0 endpoint through which the token introspection operation is accomplished.
- **Access token, authorization endpoint, authorization grant, authorization server, client, client identifier, protected resource, refresh token, resource owner, resource server, token endpoint**: As defined by OAuth 2.0 [RFC6749].
- **Claim names, claim values**: As defined by JSON Web Token (JWT) [RFC7519].

## Introspection Endpoint
### 2.1 Introspection Request
- **R001**: The protected resource calls the introspection endpoint using an HTTP POST request with parameters sent as `application/x-www-form-urlencoded`. [Section 2.1]
- **R002**: The `token` parameter is REQUIRED. For access tokens, this is the `access_token` value; for refresh tokens, the `refresh_token` value. [Section 2.1]
- **R003**: The `token_type_hint` parameter is OPTIONAL. If the server is unable to locate the token using the given hint, it MUST extend its search across all supported token types. An authorization server MAY ignore this parameter. [Section 2.1]
- **R004**: The introspection endpoint MAY accept other OPTIONAL parameters (e.g., client IP address) to provide further context. [Section 2.1]
- **R005**: The endpoint MUST require some form of authorization (client authentication per [RFC6749] or a separate OAuth 2.0 access token like bearer token [RFC6750]). [Section 2.1]

### 2.2 Introspection Response
- **R006**: The server responds with a JSON object in `application/json` format. [Section 2.2]
- **R007**: The `active` member is REQUIRED (Boolean indicator). A `true` value generally indicates the token was issued, not revoked, and is within its validity window. [Section 2.2]
- **R008**: The following members are OPTIONAL: `scope` (space-separated string), `client_id`, `username`, `token_type`, `exp`, `iat`, `nbf`, `sub`, `aud`, `iss`, `jti`. [Section 2.2]
- **R009**: Implementations MAY extend the response with their own service-specific names. Names intended for cross-domain use MUST be registered in the "OAuth Token Introspection Response" registry (Section 3.1). [Section 2.2]
- **R010**: The authorization server MAY respond differently to different protected resources (e.g., limit returned scopes). [Section 2.2]
- **R011**: The response MAY be cached by the protected resource. If the response contains an `exp` parameter, the response MUST NOT be cached beyond that time. [Section 2.2, Section 4]
- **R012**: If the introspection call is properly authorized but the token is inactive, does not exist, or the protected resource is not allowed to introspect it, the authorization server MUST return an introspection response with `"active": false`. The server SHOULD NOT include any additional information about an inactive token. [Section 2.2]

### 2.3 Error Response
- **R013**: If the protected resource uses OAuth 2.0 client credentials to authenticate and they are invalid, the authorization server responds with HTTP 401 (Unauthorized). [Section 2.3]
- **R014**: If the protected resource uses an OAuth 2.0 bearer token and it is invalid or has insufficient privileges, the server responds with HTTP 401 as per [RFC6750]. [Section 2.3]
- **R015**: A properly formed query for an inactive token is not an error; the server MUST return `active: false` as per Section 2.2. [Section 2.3]

## IANA Considerations
### 3.1 OAuth Token Introspection Response Registry
- **Registrations**: Registered by Specification Required [RFC5226] after review on the oauth-ext-review@ietf.org list. Designated Experts approve or deny requests. Names must not match registered names in a case-insensitive manner and should align with definitions in the JSON Web Token Claims registry. [Section 3.1, 3.1.1]
- **Initial Registry Contents**: Lists standard response members (`active`, `username`, `client_id`, `scope`, `token_type`, `exp`, `iat`, `nbf`, `sub`, `aud`, `iss`, `jti`) with descriptions and reference to Section 2.2 of this document. [Section 3.1.2]

## Security Considerations
- **R016**: The authorization server MUST perform all applicable checks against a token's state: expiration, validity period, revocation, signature, and audience (if applicable). [Section 4]
- **R017**: The introspection endpoint MUST be protected by transport-layer security; the server MUST support TLS 1.2 [RFC5246] and MAY support additional mechanisms. [Section 4]
- **R018**: The client or protected resource MUST perform a TLS/SSL server certificate check as per [RFC6125]. [Section 4]
- **R019**: To prevent token scanning attacks, the authorization server MUST require authentication of protected resources and SHOULD require them to be specifically authorized. [Section 4]
- **R020**: The server MAY disallow HTTP GET on the introspection endpoint and require HTTP POST to prevent token leakage in logs. [Section 4]
- **R021**: An introspection response for an inactive token SHOULD NOT contain any additional claims beyond `"active": false`. [Section 4]
- **R022**: If the response contains `exp`, it MUST NOT be cached beyond that time. [Section 4]

## Privacy Considerations
- **R023**: When the introspection response contains privacy-sensitive information (e.g., user identifiers), measures MUST be taken to prevent disclosure to unintended parties (e.g., using opaque identifiers, returning different identifiers to each protected resource). [Section 5]
- **R024**: Omitting privacy-sensitive information is the simplest mitigation. [Section 5]

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R001 | Use HTTP POST with `application/x-www-form-urlencoded` for introspection requests. | shall | Section 2.1 |
| R002 | Provide `token` parameter (REQUIRED); value is the token string. | shall | Section 2.1 |
| R003 | `token_type_hint` is OPTIONAL; if hint fails, server MUST search all types; MAY ignore hint. | shall/may | Section 2.1 |
| R004 | Endpoint MAY accept other OPTIONAL parameters for context. | may | Section 2.1 |
| R005 | Endpoint MUST require authentication (client credentials or OAuth access token). | shall | Section 2.1 |
| R006 | Response is JSON in `application/json`. | shall | Section 2.2 |
| R007 | `active` member REQUIRED (Boolean). | shall | Section 2.2 |
| R008 | Additional optional members: `scope`, `client_id`, `username`, `token_type`, `exp`, `iat`, `nbf`, `sub`, `aud`, `iss`, `jti`. | optional | Section 2.2 |
| R009 | Service-specific extension names intended for cross-domain use MUST be registered. | shall | Section 2.2 |
| R010 | Server MAY respond differently to different protected resources (e.g., limit scopes). | may | Section 2.2 |
| R011 | Response MAY be cached; MUST NOT be cached beyond `exp` if present. | may/shall | Section 2.2, 4 |
| R012 | For inactive or disallowed token, return `active: false`; SHOULD NOT include extra info. | shall/should | Section 2.2 |
| R013 | Invalid client credentials → HTTP 401. | shall | Section 2.3 |
| R014 | Invalid/insufficient bearer token for introspection → HTTP 401. | shall | Section 2.3 |
| R015 | Inactive token is not an error; return `active: false`. | shall | Section 2.3 |
| R016 | Authorization server MUST perform all applicable token state checks (expiration, revocation, signature, etc.). | shall | Section 4 |
| R017 | Server MUST support TLS 1.2, MAY support additional mechanisms. | shall/may | Section 4 |
| R018 | Client MUST perform TLS server certificate check per RFC6125. | shall | Section 4 |
| R019 | Server MUST require authentication of protected resources; SHOULD require specific authorization. | shall/should | Section 4 |
| R020 | Server MAY disallow GET, require POST at introspection endpoint. | may | Section 4 |
| R021 | Inactive token response SHOULD NOT contain extra claims beyond `active: false`. | should | Section 4 |
| R022 | If response contains `exp`, MUST NOT cache beyond that. | shall | Section 4 |
| R023 | Privacy-sensitive info in response MUST be protected (e.g., opaque identifiers). | shall | Section 5 |
| R024 | Omitting privacy-sensitive info is simplest mitigation. | should | Section 5 |

## Informative Annexes (Condensed)
- **Appendix A. Use with Proof-of-Possession Tokens**: Describes that for proof-of-possession tokens, the protected resource would have only a token identifier and a cryptographic signature; the introspection endpoint could be used to obtain key information for signature validation. The details are outside this specification and will be defined in an extension.