# RFC 9728: OAuth 2.0 Protected Resource Metadata
**Source**: IETF | **Version**: Standards Track | **Date**: April 2025 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9728

## Scope (Summary)
This document defines a JSON-based metadata format that OAuth 2.0 clients and authorization servers can use to discover the capabilities, supported scopes, token presentation methods, and authorization server relationships of an OAuth 2.0 protected resource. Metadata is retrieved from a well-known URL derived from the resource’s HTTPS resource identifier, and may be self-asserted or signed as a JWT.

## Normative References
- [BCP195] – TLS recommendations (RFC 8996, RFC 9325)
- [BCP47] – Language tags (RFC 4647, RFC 5646)
- [JWA] RFC 7518 – JSON Web Algorithms
- [JWE] RFC 7516 – JSON Web Encryption
- [JWK] RFC 7517 – JSON Web Key
- [JWS] RFC 7515 – JSON Web Signature
- [JWT] RFC 7519 – JSON Web Token
- [RFC2119] BCP 14 – Key words for requirement levels
- [RFC6749] – OAuth 2.0 Authorization Framework
- [RFC6750] – Bearer Token Usage
- [RFC7591] – OAuth 2.0 Dynamic Client Registration
- [RFC8126] – IANA Guidelines
- [RFC8174] – Ambiguity of Uppercase vs Lowercase
- [RFC8259] – JSON
- [RFC8414] – OAuth 2.0 Authorization Server Metadata
- [RFC8615] – Well-Known URIs
- [RFC8705] – Mutual-TLS Client Certificate-Bound Access Tokens
- [RFC8707] – Resource Indicators for OAuth 2.0
- [RFC9110] – HTTP Semantics
- [RFC9111] – HTTP Caching
- [RFC9396] – Rich Authorization Requests
- [RFC9449] – DPoP
- [RFC9525] – Service Identity in TLS
- [UNICODE] – Unicode Standard
- [USA15] – Unicode Normalization Forms

## Definitions and Abbreviations
- **Access Token**: as defined in [RFC6749]
- **Authorization Server**: as defined in [RFC6749]
- **Client**: as defined in [RFC6749]
- **Client Authentication**: as defined in [RFC6749]
- **Client Identifier**: as defined in [RFC6749]
- **Protected Resource**: as defined in [RFC6749]
- **Resource Server**: as defined in [RFC6749]
- **Claim Name**: as defined in [JWT]
- **JSON Web Token (JWT)**: as defined in [JWT]
- **Resource Identifier**: URL using https scheme, no fragment component; SHOULD NOT include a query component (per Section 2 of [RFC8707]). Used to derive the well-known metadata URL.

## 1. Introduction (Condensed)
This spec parallels OAuth Dynamic Client Registration [RFC7591] and Authorization Server Metadata [RFC8414]. The client discovers the resource server’s metadata from a well-known location (Section 3). The metadata can be self-asserted or signed as a JWT (Section 2.2). Metadata includes scopes, token presentation methods, and authorization server list. Section 5 describes using WWW-Authenticate to dynamically inform clients of metadata URL.

### 1.1 Requirements Notation
Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL – as per BCP 14 [RFC2119][RFC8174] when in all capitals. JWS/JWE use Compact Serialization only.

## 2. Protected Resource Metadata
### 2.1 Human-Readable Resource Metadata
Human-readable fields (resource_name, resource_documentation, resource_tos_uri, resource_policy_uri) MAY be internationalized using language tags appended with `#` (e.g., `resource_name#en`). It is RECOMMENDED to include an un-tagged value in addition to language-specific ones. Un‑tagged values MUST be used as-is; no assumptions about language/script. Language tags SHOULD be used with minimal specificity per [BCP47] and interpreted case-insensitively.

### 2.2 Signed Protected Resource Metadata
- Metadata MAY also be provided as a `signed_metadata` value: a JWT containing metadata parameters as claims.
- The JWT MUST be signed or MACed using JWS, and MUST contain an `iss` claim.
- If the consumer supports signed metadata, signed values MUST take precedence over plain JSON values.
- `signed_metadata` SHOULD NOT appear as a claim inside the JWT; it is RECOMMENDED to reject such metadata.

### Requirements from Section 2
- **[R1] resource (REQUIRED)**: The protected resource’s resource identifier URL.
- **[R2] authorization_servers (OPTIONAL)**: JSON array of authorization server issuer identifiers [RFC8414].
- **[R3] jwks_uri (OPTIONAL)**: URL of the JWK Set; MUST use https scheme. When both signing and encryption keys are present, `use` parameter REQUIRED for all keys.
- **[R4] scopes_supported (RECOMMENDED)**: JSON array of scope values for this resource.
- **[R5] bearer_methods_supported (OPTIONAL)**: JSON array of bearer token methods defined in [RFC6750]. Allowed: `["header","body","query"]`. Empty array indicates no bearer methods supported.
- **[R6] resource_signing_alg_values_supported (OPTIONAL)**: JSON array of JWS signing algorithms. `none` MUST NOT be used.
- **[R7] resource_name (RECOMMENDED)**: Human-readable name.
- **[R8] resource_documentation (OPTIONAL)**: URL to developer documentation.
- **[R9] resource_policy_uri (OPTIONAL)**: URL to usage policy.
- **[R10] resource_tos_uri (OPTIONAL)**: URL to terms of service.
- **[R11] tls_client_certificate_bound_access_tokens (OPTIONAL)**: Boolean default false.
- **[R12] authorization_details_types_supported (OPTIONAL)**: JSON array of authorization details type values [RFC9396].
- **[R13] dpop_signing_alg_values_supported (OPTIONAL)**: JSON array of JWS alg values for DPoP validation [RFC9449].
- **[R14] dpop_bound_access_tokens_required (OPTIONAL)**: Boolean default false.
- Additional metadata MAY be used.

## 3. Obtaining Protected Resource Metadata
- Protected resources supporting metadata MUST make a JSON document available at a URL formed by inserting `/.well-known/oauth-protected-resource` (or a registered application‑specific suffix) between the host and path/query of the resource identifier.
- Default well-known suffix: `oauth-protected-resource`. MUST be registered in the Well-Known URIs registry.
- The OAuth 2.0 application using this spec MUST specify which well‑known URI suffix it uses.

### 3.1 Metadata Request
- MUST use HTTP GET. Examples in Section 3.1.

### 3.2 Metadata Response
- Successful response: 200 OK, `application/json`, JSON object containing metadata parameters from Section 2.
- Unrecognized metadata MUST be ignored.
- Error response: appropriate HTTP status code.

### 3.3 Metadata Validation
- **[R15]**: The `resource` value returned MUST be identical to the resource identifier used to derive the metadata URL. If not identical, MUST NOT use the data.
- **[R16]**: If metadata retrieved from a URL returned via WWW-Authenticate `resource_metadata`, the `resource` value MUST be identical to the URL the client used to make the request. If not identical, MUST NOT use the data.
- Signed metadata: MUST validate that signature is from a trusted issuer. If invalid or untrusted, SHOULD treat as error.

## 4. Authorization Server Metadata
- New AS metadata parameter `protected_resources` (OPTIONAL): JSON array of resource identifiers for OAuth protected resources usable with this AS.
- Cross‑check lists with protected resource metadata when both enumerable.

## 5. Use of WWW-Authenticate for Protected Resource Metadata
### 5.1 WWW-Authenticate Response
- New WWW-Authenticate parameter `resource_metadata`: URL of the protected resource metadata.
- MAY be used with any auth scheme (Bearer, DPoP, etc.).
- Example: `WWW-Authenticate: Bearer resource_metadata="https://resource.example.com/.well-known/oauth-protected-resource"`

### 5.2 Changes to Resource Metadata
- Protected resource MAY return new WWW-Authenticate challenge with updated metadata URL.
- Client SHOULD retrieve updated metadata and use new values after validation.

### 5.3 Client Identifier and Client Authentication
- Out of scope. Client may use dynamic registration [RFC7591] or future extensions.

### 5.4 Compatibility with Other Authentication Methods
- Resource servers MAY return multiple WWW-Authenticate headers for different schemes.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | resource parameter MUST be present and equal to resource identifier | shall | Section 2 |
| R2 | authorization_servers parameter OPTIONAL | may | Section 2 |
| R3 | jwks_uri URL MUST use https | shall | Section 2 |
| R4 | scopes_supported RECOMMENDED | should | Section 2 |
| R5 | bearer_methods_supported OPTIONAL | may | Section 2 |
| R6 | resource_signing_alg_values_supported MUST NOT include "none" | shall not | Section 2 |
| R7 | resource_name RECOMMENDED | should | Section 2 |
| R8 | resource_documentation OPTIONAL | may | Section 2 |
| R9 | resource_policy_uri OPTIONAL | may | Section 2 |
| R10 | resource_tos_uri OPTIONAL | may | Section 2 |
| R11 | tls_client_certificate_bound_access_tokens defaults false | may | Section 2 |
| R12 | authorization_details_types_supported OPTIONAL | may | Section 2 |
| R13 | dpop_signing_alg_values_supported OPTIONAL | may | Section 2 |
| R14 | dpop_bound_access_tokens_required defaults false | may | Section 2 |
| R15 | Metadata validation: resource value MUST match request URL | shall | Section 3.3 |
| R16 | If via WWW-Authenticate, resource value MUST match request URL | shall | Section 3.3 |
| R17 | Protected resources supporting metadata MUST publish at well-known URL | shall | Section 3 |
| R18 | String comparisons MUST be code-point equality without normalization | shall | Section 6 |
| R19 | TLS MUST be supported per BCP195 | shall | Section 7.1 |
| R20 | Client MUST perform TLS certificate checking per RFC9525 | shall | Section 7.3 |
| R21 | Signed metadata MUST be signed or MACed with JWS | shall | Section 2.2 |
| R22 | Signed metadata MUST contain iss claim | shall | Section 2.2 |
| R23 | Signed metadata values take precedence over plain JSON (if supported) | shall | Section 2.2 |
| R24 | WWW-Authenticate resource_metadata MAY be used | may | Section 5.1 |
| R25 | Client SHOULD retrieve updated metadata when new challenge received | should | Section 5.2 |
| R26 | client SHOULD request audience-restricted tokens via RFC8707 | should | Section 7.4 |
| R27 | Authorization server SHOULD support audience-restricted tokens | should | Section 7.4 |
| R28 | Implementations SHOULD interpret language tags case-insensitively | should | Section 2.1 |

## Security Considerations (Condensed)
- **TLS**: MUST support TLS per BCP195 (Section 7.1)
- **Scopes**: client SHOULD request minimal scopes (per RFC9700) (Section 7.2)
- **Impersonation**: TLS certificate check per RFC9525; validate resource value (Section 7.3)
- **Audience-restricted tokens**: RECOMMENDED to use RFC8707 to prevent token reuse (Section 7.4)
- **Standard format**: same defenses as ad hoc metadata (Section 7.5)
- **Authorization servers**: cross-check lists; secure determination out of scope (Section 7.6)
- **SSRF**: client SHOULD block requests to internal IPs (Section 7.7)
- **Phishing**: reduce risk via UI best practices, domain display, origin-bound authenticators (Section 7.8)
- **Unsigned vs signed metadata**: unsigned relies on TLS; signed adds issuer trust (Section 7.9)
- **Caching**: honor HTTP caching directives (Section 7.10)

## IANA Considerations (Condensed)
### 8.1 OAuth Protected Resource Metadata Registry
- New registry managed by IETF. Registration via Specification Required [RFC8126].
- Review by designated experts for uniqueness, general applicability.
- Initial registrations for all parameters in Section 2 and `signed_metadata` in Section 2.2 (listed in Section 8.1.2).

### 8.2 OAuth Authorization Server Metadata Registry
- Added `protected_resources` (Section 4)

### 8.3 Well-Known URIs Registry
- Registered `oauth-protected-resource` (permanent, Section 3)

## Informative Annexes (Condensed)
- **Acknowledgements**: Thanks to IETF OAuth WG, multiple contributors.
- **Authors' Addresses**: Michael B. Jones, Phil Hunt, Aaron Parecki.