# RFC 8707: Resource Indicators for OAuth 2.0
**Source**: IETF | **Version**: Standards Track | **Date**: February 2020 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc8707

## Scope (Summary)
This document defines an extension to OAuth 2.0 that allows a client to explicitly signal to the authorization server the protected resource(s) to which it is requesting access, enabling audience-restricted tokens and improved security.

## Normative References
- [IANA.OAuth.Parameters] IANA, "OAuth Parameters"
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017

## Definitions and Abbreviations
- **access token, refresh token, authorization server, resource server, authorization endpoint, authorization request, authorization response, token endpoint, grant type, access token request, access token response, client**: As defined in [RFC6749].

## 2. Resource Parameter
- **resource**: Parameter indicating the target service or resource to which access is being requested. Its value **MUST** be an absolute URI (Section 4.3 of [RFC3986]). The URI **MUST NOT** include a fragment component. It **SHOULD NOT** include a query component, but recognition that some cases necessitate it. Multiple resource parameters **MAY** be used to indicate multiple target resources.
- **invalid_target**: Error code for authorization server to indicate the requested resource is invalid, missing, unknown, or malformed.
- **Audience Restriction**: The authorization server **SHOULD** audience-restrict issued access tokens to the resource(s) indicated by the "resource" parameter. Audience restrictions can be communicated in JWTs [RFC7519] with the "aud" claim and in Token Introspection [RFC7662] responses.
- **Client Guidance**: The client **SHOULD** provide the most specific URI possible; **SHOULD** use the base URI of the API unless specific knowledge dictates otherwise.

### 2.1. Authorization Request
- **Usage**: When used in an authorization request to the authorization endpoint, indicates the protected resource(s) to which access is requested.
- **JWT Representation**: For a JWT-based authorization request (e.g., JWT Secured Authorization Request [JWT-SAR]), a single "resource" parameter is a JSON string; multiple values are a JSON array.
- **Omission**: If the client omits the "resource" parameter, the authorization server **MAY** process with no specific resource or with a predefined default. Alternatively, the authorization server **MAY** require the parameter and **MAY** fail requests with an "invalid_target" error.
- **Error Handling**: If the authorization server fails to parse the provided value(s) or does not consider the resource(s) acceptable, it **should** reject with an "invalid_target" error and **can** provide additional information via "error_description".

### 2.2. Access Token Request
- **Usage**: When used on an access token request to the token endpoint (for all grant types), indicates the target service or protected resource where the client intends to use the requested access token.
- **Acceptable Resources**: The authorization server determines acceptable resources at its sole discretion based on local policy. For "refresh_token" or "authorization_code" grants, policy may limit resources to those originally granted.
- **Combined with Scope**: The client can indicate desired target services via "resource" and desired scope via "scope". Semantics: token with requested scope usable at all requested target services (cartesian product). The authorization server **should** downscope the token to what each resource needs to process.
- **Scope Response**: As per Section 5.1 of [RFC6749], the authorization server **must** indicate the token's effective scope in the "scope" response parameter when it differs from the requested scope.

## 3. Security Considerations (Condensed)
- Audience-restricted tokens prevent token redirect. Using the "resource" parameter enables the authorization server to apply appropriate audience restrictions.
- For multi-tenant servers, use a specific resource URI including tenant-identifying portions (e.g., path component) to avoid cross-tenant attacks.
- Using multiple "resource" parameters (multiple audiences) is discouraged; such tokens are usable at multiple resources and require high trust between parties. The authorization server may be unwilling to fulfill such requests.
- When feasible, the "resource" parameter should correspond to the network-addressable location of the protected resource to allow client validation. If an abstract identifier is used, the client must validate out-of-band that the network endpoint is the intended audience.

## 4. Privacy Considerations (Condensed)
- Use of the resource parameter may allow more granular tracking of user and client behavior compared to deployments not using it, particularly when access token introspection is not used.

## 5. IANA Considerations (Normative Updates)
### 5.1. OAuth Parameters Registration
- **Parameter name**: resource
- **Usage location**: authorization request, token request
- **Change controller**: IESG
- **Specification document**: RFC 8707

### 5.2. OAuth Extensions Error Registration
- **Error name**: invalid_target
- **Usage location**: implicit grant error response, token error response
- **Related protocol extension**: resource parameter
- **Change controller**: IESG
- **Specification document**: RFC 8707

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | "resource" parameter value MUST be an absolute URI (Section 4.3 of [RFC3986]). | MUST | Section 2 |
| R2 | "resource" parameter value MUST NOT include a fragment component. | MUST | Section 2 |
| R3 | "resource" parameter value SHOULD NOT include a query component. | SHOULD | Section 2 |
| R4 | Multiple "resource" parameters MAY be used to indicate multiple target resources. | MAY | Section 2 |
| R5 | Authorization server SHOULD audience-restrict issued access tokens to the indicated resource(s). | SHOULD | Section 2 |
| R6 | Client SHOULD provide the most specific URI possible. | SHOULD | Section 2 |
| R7 | Client SHOULD use the base URI of the API as the "resource" parameter value unless specific knowledge dictates otherwise. | SHOULD | Section 2 |
| R8 | If the client omits "resource", the authorization server MAY process with no specific resource or MAY require and fail with "invalid_target". | MAY | Section 2.1 |
| R9 | Error code "invalid_target" to indicate invalid, missing, unknown, or malformed resource. | (normative) | Section 2 |
| R10 | In access token request, "resource" indicates target service; authorization server determines acceptability at its sole discretion. | (normative) | Section 2.2 |
| R11 | For "refresh_token" or "authorization_code" grants, authorization server may limit acceptable resources to those originally granted. | (normative) | Section 2.2 |
| R12 | Authorization server SHOULD downscope access token scope to what each resource needs. | SHOULD | Section 2.2 |
| R13 | Authorization server MUST indicate effective scope in "scope" response parameter when different from requested. | MUST | Section 2.2 (per [RFC6749]) |

## Informative Annexes (Condensed)
- **Examples (Figures 1–6)**: Illustrate use of "resource" in implicit flow, code flow, access token requests/responses, and refresh token requests/responses. These are non-normative examples showing exact HTTP requests and JSON responses with audience-restricted tokens.
- **Acknowledgements**: Lists contributors including chairs, area directors, and individuals providing feedback.