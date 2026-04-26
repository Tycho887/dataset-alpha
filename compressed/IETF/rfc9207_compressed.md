# RFC 9207: OAuth 2.0 Authorization Server Issuer Identification
**Source**: IETF | **Version**: Standards Track | **Date**: March 2022 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9207

## Scope (Summary)
Defines a new parameter `iss` for OAuth authorization responses (including error responses) to explicitly include the authorization server’s issuer identifier, providing a countermeasure against mix-up attacks for clients interacting with multiple authorization servers.

## Normative References
- [RFC2119] – Key words for requirement levels
- [RFC3986] – URI generic syntax
- [RFC6749] – OAuth 2.0 Authorization Framework
- [RFC8174] – Ambiguity of uppercase vs lowercase in RFC 2119
- [RFC8414] – OAuth 2.0 Authorization Server Metadata

## Definitions and Abbreviations
- **iss**: A new parameter in the authorization response containing the issuer identifier of the authorization server.
- **issuer identifier**: As defined by [RFC8414], a URL using the "https" scheme without query or fragment components.
- **mix-up attack**: An attack class where an attacker-controlled authorization server tricks the client into sending credentials (authorization codes or access tokens) to the wrong server.
- **authorization response**: As defined in [RFC6749] Section 4.1.2, including error responses.
- **Client**: As defined in [RFC6749].

## 1. Introduction
### 1.1. Conventions and Terminology
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when they appear in all capitals.

## 2. Response Parameter `iss`
- **Requirement (R1)**: In authorization responses to the client, including error responses, an authorization server supporting this specification **MUST** indicate its identity by including the `iss` parameter in the response.
- **Requirement (R2)**: The `iss` parameter value **MUST** be the issuer identifier of the authorization server that created the authorization response, as defined in [RFC8414]. Its value **MUST** be a URL that uses the "https" scheme without any query or fragment components.

### 2.1. Example Authorization Response
*(Informative – shown in original document)*

### 2.2. Example Error Response
*(Informative – shown in original document)*

### 2.3. Providing the Issuer Identifier
- **Requirement (R3)**: Authorization servers supporting this specification **MUST** provide their issuer identifier to enable clients to validate the `iss` parameter effectively.
- For servers publishing metadata per [RFC8414]:
  - **Requirement (R4)**: The issuer identifier included in the server's metadata value `issuer` **MUST** be identical to the `iss` parameter's value.
  - **Requirement (R5)**: The server **MUST** indicate its support for the `iss` parameter by setting the metadata parameter `authorization_response_iss_parameter_supported` (defined in Section 3) to `true`.
- **Permissive**: Authorization servers **MAY** additionally provide the issuer identifier to clients by any other mechanism (outside scope).

### 2.4. Validating the Issuer Identifier
- **Requirement (R6)**: Clients that support this specification **MUST** extract the value of the `iss` parameter from authorization responses they receive if the parameter is present.
- **Requirement (R7)**: Clients **MUST** then decode the value from its `application/x-www-form-urlencoded` form according to Appendix B of [RFC6749] and compare the result to the issuer identifier of the authorization server where the authorization request was sent to.
- **Requirement (R8)**: This comparison **MUST** use simple string comparison as defined in Section 6.2.1 of [RFC3986].
- **Requirement (R9)**: If the value does not match the expected issuer identifier, clients **MUST** reject the authorization response and **MUST NOT** proceed with the authorization grant. For error responses, clients **MUST NOT** assume that the error originates from the intended authorization server.
- **Requirement (R10)**: Clients that interact with authorization servers supporting OAuth metadata [RFC8414] **MUST** compare the `iss` parameter value to the `issuer` value in the server's metadata document. If OAuth metadata is not used, clients **MUST** use deployment-specific ways (e.g., static configuration) to decide if the returned `iss` value is expected.
- **Requirement (R11)**: If clients interact with both authorization servers supporting and not supporting this specification, clients **MUST** retain state about whether each authorization server supports the `iss` parameter.
- **Requirement (R12)**: Clients **MUST** reject authorization responses without the `iss` parameter from authorization servers that do support the parameter according to the client's configuration.
- **Requirement (R13)**: Clients **SHOULD** discard authorization responses with the `iss` parameter from authorization servers that do not indicate their support for the parameter. (May accept by local policy/configuration.)
- **Permissive**: Clients **MAY** accept authorization responses without `iss` or reject them and exclusively support servers that provide `iss` (by local policy/configuration).
- **Requirement (R14)**: In OpenID Connect [OIDC.Core] flows where an ID Token is returned from the authorization endpoint, the value in the `iss` parameter **MUST** always be identical to the `iss` claim in the ID Token.
- **Existing rule**: Per [RFC6749] Section 4.1.2, clients that do not support this specification **MUST** ignore the unrecognized `iss` parameter.
- **Note**: When JARM is used, an additional `iss` parameter outside the JWT is not necessary.

## 3. Authorization Server Metadata
- New metadata parameter: `authorization_response_iss_parameter_supported`
  - **Boolean** parameter. If omitted, default value is `false`.
  - Indicates whether the authorization server provides the `iss` parameter in the authorization response as defined in Section 2.

## 4. Security Considerations
- **Requirement (R15)**: Clients **MUST** validate the `iss` parameter precisely as described in Section 2.4 and **MUST NOT** allow multiple authorization servers to use the same issuer identifier.
- **Requirement (R16)**: When authorization server details can be manually configured, the client **MUST** ensure accepted `iss` values are unique for each authorization server.
- The `iss` parameter helps the client decide if an authorization server "expects" to be used with a certain token endpoint and other endpoints.
- The issuer identifier in the authorization response is not cryptographically protected against tampering; however, in mix-up attacks, tampering would give direct access to the authorization code, so integrity protection is not necessary for this defense.
- **Permissive**: When an authorization response already includes an issuer identifier by other means (e.g., OpenID Connect ID Token or JARM), and it is validated as per Section 2.4, use and verification of the `iss` parameter is not necessary and **MAY** be omitted.
- **Requirement (R17)**: If a client receives an authorization response containing multiple issuer identifiers, the client **MUST** reject the response if these identifiers do not match.
- Mix-up attacks are relevant only to clients interacting with multiple authorization servers; clients with a single server should consider future support.

## 5. IANA Considerations
### 5.1. OAuth Authorization Server Metadata
- Registered `authorization_response_iss_parameter_supported` in the "OAuth Authorization Server Metadata" registry per [RFC8414].

### 5.2. OAuth Parameters Registration
- Updated the `iss` entry in the "OAuth Parameters" registry to include usage in authorization request and response, with specification documents: Section 2 of RFC 9207, [RFC9101], and Section 4.1.1 of [RFC7519].

## Requirements Summary
| ID  | Requirement (condensed) | Type    | Reference       |
|-----|--------------------------|---------|-----------------|
| R1  | AS MUST include `iss` in authorization responses (including errors). | MUST | Section 2       |
| R2  | `iss` value MUST be "https" URL without query/fragment, per issuer identifier definition. | MUST | Section 2       |
| R3  | AS MUST provide issuer identifier to clients. | MUST | Section 2.3     |
| R4  | Metadata `issuer` MUST equal `iss` parameter value. | MUST | Section 2.3     |
| R5  | AS MUST set `authorization_response_iss_parameter_supported` to `true` in metadata. | MUST | Section 2.3     |
| R6  | Client MUST extract `iss` value if present. | MUST | Section 2.4     |
| R7  | Client MUST decode and compare to expected issuer identifier. | MUST | Section 2.4     |
| R8  | Comparison MUST use simple string comparison per [RFC3986] 6.2.1. | MUST | Section 2.4     |
| R9  | Non‑match: client MUST reject response, MUST NOT proceed with grant. | MUST | Section 2.4     |
| R10 | Client MUST compare to metadata `issuer` if OAuth metadata used; else use deployment‑specific. | MUST | Section 2.4     |
| R11 | Client MUST retain state per authorization server regarding `iss` support. | MUST | Section 2.4     |
| R12 | Client MUST reject responses without `iss` from servers known to support it. | MUST | Section 2.4     |
| R13 | Client SHOULD discard responses with `iss` from servers not indicating support. | SHOULD | Section 2.4   |
| R14 | In OpenID Connect, `iss` parameter MUST equal ID Token `iss` claim. | MUST | Section 2.4     |
| R15 | Client MUST validate `iss` as described; MUST NOT reuse same issuer ID for multiple AS. | MUST | Section 4       |
| R16 | In manual configuration, ensure unique `iss` values per AS. | MUST | Section 4       |
| R17 | Multiple issuer identifiers in a response MUST match; else reject. | MUST | Section 4       |

## Informative Annexes (Condensed)
- **IANA Considerations**: The document registers the metadata parameter `authorization_response_iss_parameter_supported` and updates the `iss` parameter in the OAuth Parameters registry.
- **Acknowledgements**: Thanks to Brian Campbell, Roman Danyliw, Vladimir Dzhuvinov, Joseph Heenan, Takahiko Kawasaki, Torsten Lodderstedt, Christian Mainka, Vladislav Mladenov, Warren Parad, Aaron Parecki, and Rifaat Shekh‑Yusef.
- **References**: All normative and informative references are listed in the original document; key ones are captured in the Normative References section above.