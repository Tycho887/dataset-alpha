# OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
**Source**: OpenID Foundation | **Version**: 1.0 incorporating errata set 2 | **Date**: December 15, 2023 | **Type**: Normative
**Original**: [Document text provided]

## Scope (Summary)
This specification defines how an OpenID Connect Relying Party (Client) can dynamically register with an OpenID Provider (Authorization Server) by providing its metadata and obtaining an OAuth 2.0 Client ID and other necessary information. It covers registration endpoints, client metadata, and management of registration information.

## Normative References
- [RFC2119] Bradner, S., “Key words for use in RFCs to Indicate Requirement Levels,” March 1997.
- [RFC3629] Yergeau, F., “UTF-8, a transformation format of ISO 10646,” November 2003.
- [RFC3986] Berners-Lee, T., et al., “Uniform Resource Identifier (URI): Generic Syntax,” January 2005.
- [RFC5646] Phillips, A., et al., “Tags for Identifying Languages,” September 2009.
- [RFC6125] Saint-Andre, P., et al., “Representation and Verification of Domain-Based Application Service Identity …,” March 2011.
- [RFC6749] Hardt, D., Ed., “The OAuth 2.0 Authorization Framework,” October 2012.
- [RFC6750] Jones, M., et al., “The OAuth 2.0 Authorization Framework: Bearer Token Usage,” October 2012.
- [RFC7231] Fielding, R., et al., “Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content,” June 2014.
- [RFC8259] Bray, T., Ed., “The JavaScript Object Notation (JSON) Data Interchange Format,” December 2017.
- [RFC8996] Moriarty, K., et al., “Deprecating TLS 1.0 and TLS 1.1,” March 2021.
- [RFC9325] Sheffer, Y., et al., “Recommendations for Secure Use of TLS and DTLS,” November 2022.
- [JWA] Jones, M., “JSON Web Algorithms (JWA),” RFC 7518, May 2015.
- [JWE] Jones, M., et al., “JSON Web Encryption (JWE),” RFC 7516, May 2015.
- [JWK] Jones, M., “JSON Web Key (JWK),” RFC 7517, May 2015.
- [JWS] Jones, M., et al., “JSON Web Signature (JWS),” RFC 7515, May 2015.
- [JWT] Jones, M., et al., “JSON Web Token (JWT),” RFC 7519, May 2015.
- [OpenID.Core] Sakimura, N., et al., “OpenID Connect Core 1.0,” December 2023.
- [OpenID.Discovery] Sakimura, N., et al., “OpenID Connect Discovery 1.0,” December 2023.
- [CORS] Opera Software ASA, “Cross-Origin Resource Sharing,” July 2010.
- [IANA.OAuth.Parameters] IANA, “OAuth Parameters.”
- [UNICODE] The Unicode Consortium, “The Unicode Standard.”
- [USA15] Whistler, K., “Unicode Normalization Forms,” August 2023.

## Informative References
- [OpenID.RPInitiated] Jones, M., et al., “OpenID Connect RP-Initiated Logout 1.0,” September 2022.
- [RFC7591] Richer, J., Ed., et al., “OAuth 2.0 Dynamic Client Registration Protocol,” July 2015.
- [RFC7592] Richer, J., Ed., et al., “OAuth 2.0 Dynamic Client Registration Management Protocol,” July 2015.

## Definitions and Abbreviations
- **Client Registration Endpoint**: OAuth 2.0 Protected Resource through which a Client can be registered at an Authorization Server.
- **Client Configuration Endpoint**: OAuth 2.0 Endpoint through which registration information for a registered Client can be managed. Its URL is returned in the Client Information Response.
- **Registration Access Token**: OAuth 2.0 Bearer Token issued by the Authorization Server through the Client Registration Endpoint, used to authenticate the caller when accessing the Client’s registration information at the Client Configuration Endpoint.
- **Initial Access Token**: OAuth 2.0 Access Token optionally issued by an Authorization Server granting access to its Client Registration Endpoint (contents out of scope).
- Terms from OAuth 2.0 [RFC6749], JWT [JWT], and OpenID Connect Core [OpenID.Core] apply.

## Introduction
### 1.1 Requirements Notation and Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as per RFC 2119.
- In the .txt version, quoted values are literal; in the HTML version, fixed-width font indicates literals.
- All uses of JWS and JWE in this specification utilize JWS/JWE Compact Serialization only (JSON Serialization not used).

## 1.2 Terminology
Terms defined in OAuth 2.0, JWT, JWS (Base64url Encoding), and OpenID Connect Core 1.0 apply. Additional terms defined above.

## 2. Client Metadata
Client Metadata values are used as input to registration requests and as output in responses.

### REQUIRED
- **redirect_uris**: Array of Redirection URI values. One MUST exactly match the `redirect_uri` parameter value in each Authorization Request, per Simple String Comparison (RFC 3986 Section 6.2.1).

### OPTIONAL (with defaults)
- **response_types**: JSON array of OAuth 2.0 `response_type` values; default `["code"]`.
- **grant_types**: JSON array of OAuth 2.0 Grant Types; default `["authorization_code"]`. Table maps `response_type` to `grant_types`.
  - `code` → `authorization_code`
  - `id_token`, `id_token token` → `implicit`
  - `code id_token`, `code token`, `code id_token token` → `authorization_code, implicit`
- **application_type**: `"web"` (default) or `"native"`.
  - Web Clients using Implicit Grant MUST use `https` scheme for redirect_uris; MUST NOT use `localhost`.
  - Native Clients MUST use custom URI schemes or loopback http URIs (localhost, 127.0.0.1, [::1]).
  - Authorization Servers MAY impose additional constraints on Native Clients and MAY reject http redirect_uris except loopback.
- **contacts**: Array of e-mail addresses.
- **client_name**: Human-readable name; may be localized per Section 2.1.
- **logo_uri**: URL to logo image; SHOULD display to End-User; MUST point to valid image.
- **client_uri**: URL of home page; MUST point to valid web page; SHOULD display.
- **policy_uri**: URL explaining profile data usage; MUST point to valid web page; SHOULD display.
- **tos_uri**: URL for terms of service; MUST point to valid web page; SHOULD display.
- **jwks_uri**: URL for Client's JWK Set document; MUST use `https` scheme; for signing/encryption keys.
  - JWK Set MAY contain X.509 representations; MUST NOT contain private or symmetric keys.
- **jwks**: Client's JWK Set by value (for clients unable to host jwks_uri).
  - If jwks_uri is usable, MUST NOT use jwks.
  - jwks and jwks_uri MUST NOT be used together.
  - JWK Set MUST NOT contain private or symmetric keys.
- **sector_identifier_uri**: URL using `https` scheme referencing JSON array of redirect_uri values for pairwise subject calculation.
- **subject_type**: `"pairwise"` or `"public"`.
- **id_token_signed_response_alg**: JWS `alg` for signing ID Token; default `RS256`; `none` NOT allowed unless no ID Token returned from Authorization Endpoint.
- **id_token_encrypted_response_alg**: JWE `alg` for encrypting ID Token; default no encryption.
- **id_token_encrypted_response_enc**: JWE `enc`; default `A128CBC-HS256` if alg specified; `id_token_encrypted_response_alg` MUST also be provided.
- **userinfo_signed_response_alg**: JWS `alg` for signing UserInfo Responses; default no signing (UTF-8 JSON).
- **userinfo_encrypted_response_alg**: JWE `alg` for encrypting UserInfo Responses; default no encryption.
- **userinfo_encrypted_response_enc**: JWE `enc`; default `A128CBC-HS256`; MUST provide alg if included.
- **request_object_signing_alg**: JWS `alg` for signing Request Objects; Servers SHOULD support RS256; `none` MAY be used; default any algorithm allowed.
- **request_object_encryption_alg**: JWE `alg` for encrypting Request Objects; default not declaring.
- **request_object_encryption_enc**: JWE `enc`; default `A128CBC-HS256`; MUST provide alg.
- **token_endpoint_auth_method**: Client authentication method for Token Endpoint; options: `client_secret_post`, `client_secret_basic`, `client_secret_jwt`, `private_key_jwt`, `none`; default `client_secret_basic`.
- **token_endpoint_auth_signing_alg**: JWS `alg` for signing JWT at Token Endpoint for `private_key_jwt` and `client_secret_jwt`; Servers SHOULD support RS256; `none` MUST NOT be used; default any algorithm allowed.
- **default_max_age**: Default Maximum Authentication Age in seconds; `max_age` overrides.
- **require_auth_time**: Boolean; if `true`, `auth_time` Claim REQUIRED in ID Token; default `false`.
- **default_acr_values**: Array of default ACR values in order of preference; overridden by `acr_values` parameter or individual claim request.
- **initiate_login_uri**: URI using `https` scheme for third-party login initiation; MUST accept GET and POST; Client MUST understand `login_hint` and `iss`; SHOULD support `target_link_uri`.
- **request_uris**: Array of pre-registered `request_uri` values; MUST use `https` unless signed verifiably. OPs may require pre-registration; for mutable content, SHOULD include base64url-encoded SHA-256 hash fragment.
- Additional Client Metadata parameters MAY be used (e.g., from [OpenID.RPInitiated]).

### 2.1 Metadata Languages and Scripts
- Human-readable values (e.g., `client_name`, `tos_uri`, `policy_uri`, `logo_uri`, `client_uri`) MAY be localized using language tags appended with `#` (e.g., `client_name#ja-Jpan-JP`), following syntax in [OpenID.Core] Section 5.2.
- If sent without language tag, no assumptions about language or script; string used as-is. RECOMMENDED to provide values suitable for display on wide variety of systems.

## 3. Client Registration Endpoint
- OAuth 2.0 Protected Resource for requesting new Client registration.
- OP MAY require an Initial Access Token (out of scope).
- SHOULD support CORS/other methods for browser-based Clients.
- To support open Dynamic Registration, SHOULD accept requests without Access Tokens; MAY rate-limit.
- If Initial Access Token required, MUST accept it per OAuth 2.0 Bearer Token Usage [RFC6750].

### 3.1 Client Registration Request
- HTTP POST to Client Registration Endpoint with `Content-Type: application/json` and Client Metadata as top-level JSON members.
- Authorization Server assigns unique Client Identifier, optionally Client Secret, and associates Metadata. MAY provision defaults for omitted items.
- Example request provided.

### 3.2 Client Registration Response
- HTTP 201 Created, JSON document containing:
  - **client_id**: REQUIRED, unique Client Identifier.
  - **client_secret**: OPTIONAL, unique per Client; used for Token Endpoint authentication and key derivation.
  - **registration_access_token**: OPTIONAL, for subsequent operations at Client Configuration Endpoint.
  - **registration_client_uri**: OPTIONAL, URL using `https` scheme; MUST be provided together with registration_access_token.
  - **client_id_issued_at**: OPTIONAL, time of issue (seconds since epoch).
  - **client_secret_expires_at**: REQUIRED if `client_secret` issued; 0 if never expires.
- Authorization Server MAY reject or replace field values (except `redirect_uris`) and MUST include them in response. MAY ignore unknown fields.
- Example response provided.

### 3.3 Client Registration Error Response
- OAuth errors per Section 3 of [RFC6750].
- Registration errors: HTTP 400, JSON object with `error` and `error_description`.
- Defined error codes: `invalid_redirect_uri`, `invalid_client_metadata`. Others MAY be used.
- Example error response provided.

## 4. Client Configuration Endpoint
- OAuth 2.0 Protected Resource for viewing/updating registered Client information.
- Client MUST use Registration Access Token as Bearer Token [RFC6750].
- SHOULD support CORS. Only HTTP GET method defined in this specification.

### 4.1 Forming the Client Configuration Endpoint URL
- Provided by Authorization Server in `registration_client_uri` element; Client MUST use as given.
- RECOMMENDED to construct URL by combining Client Registration Endpoint URL and Client ID (path or query parameter).
- Server MUST match request to Client to which Registration Access Token was issued.

### 4.2 Client Read Request
- HTTP GET to Client Configuration Endpoint with Registration Access Token. SHOULD be idempotent.
- Example request provided.

### 4.3 Client Read Response
- HTTP 200 OK, JSON document containing all registered Metadata (including any updates). `registration_access_token` and `registration_client_uri` need not be included unless updated.
- Example response provided.

### 4.4 Client Read Error Response
- If Registration Access Token invalid: error per [RFC6750].
- If Client does not exist or invalid: HTTP 401 Unauthorized.
- If no permission: HTTP 403 Forbidden.
- MUST NOT return HTTP 404 to inhibit brute force.
- Example error response provided.

## 5. `sector_identifier_uri` Validation
- Value MUST be `https` URL referencing JSON file containing array of `redirect_uri` values.
- All values in `redirect_uris` MUST be included in that array, otherwise registration fails.
- Validation at registration time only; OP need not retain or revalidate later.
- Example provided.

## 6. String Operations
- When comparing JSON strings (e.g., `client_id`), perform: remove JSON escaping → Unicode code points. Unicode normalization MUST NOT be applied. Perform code point equality comparison.

## 7. Validation
- If any validation fails, aborted operations requiring that information MUST be aborted; such information MUST NOT be used.

## 8. Implementation Considerations
- All required features (MUST) in this specification must be implemented.
- Compatible with OAuth 2.0 Dynamic Client Registration Protocol [RFC7591]; MAY use additional metadata like `software_statement`.
- For Update operations, see [RFC7592] (experimental).

### 8.1 Compatibility Notes
- Potential compatibility issues from original version have been addressed.

### 8.2 Implementation Notes on Stateless Dynamic Client Registration
- Enables Client to obtain Client ID without server storing state; e.g., encode registration info into `client_id`.
- Read operations may not be possible; no Client Configuration Endpoint or Registration Access Token would be returned.

## 9. Security Considerations
- All communication with Registration Endpoint MUST use TLS (see Section 9.3).

### 9.1 Impersonation
- RPs could use legitimate RP's logo; OP should mitigate phishing: check domain of logo/site vs. registered redirect URIs; warn against untrusted RPs.
- OP should check `logo_uri` and `policy_uri` have same host as `redirect_uris`.

### 9.2 Native Code Leakage
- On iOS, multiple apps can register same custom URI scheme, causing nondeterministic delivery. Solution expected from IETF OAuth WG.

### 9.3 TLS Requirements
- Implementations MUST support TLS. Follow guidance in BCP 195 [RFC8996][RFC9325].
- Confidentiality protection MUST be applied using TLS with ciphersuite providing confidentiality and integrity.
- TLS server certificate check MUST be performed per RFC 6125.

## 10. IANA Considerations
### 10.1 OAuth Dynamic Client Registration Metadata Registration
Metadata names registered: `application_type`, `sector_identifier_uri`, `subject_type`, `id_token_signed_response_alg`, `id_token_encrypted_response_alg`, `id_token_encrypted_response_enc`, `userinfo_signed_response_alg`, `userinfo_encrypted_response_alg`, `userinfo_encrypted_response_enc`, `request_object_signing_alg`, `request_object_encryption_alg`, `request_object_encryption_enc`, `token_endpoint_auth_signing_alg`, `default_max_age`, `require_auth_time`, `default_acr_values`, `initiate_login_uri`, `request_uris`. All with Change Controller: OpenID Foundation Artifact Binding Working Group, specification document Section 2.

### 10.2 OAuth Token Endpoint Authentication Methods Registration
Methods registered: `client_secret_jwt`, `private_key_jwt`. Specification document Section 9 of [OpenID.Core].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | `redirect_uris` MUST be provided and one MUST exactly match Authorization Request `redirect_uri` | shall | Section 2 |
| R2 | Web Clients using Implicit Grant MUST use `https` scheme for `redirect_uris`; MUST NOT use localhost | shall | Section 2 (application_type) |
| R3 | Native Clients MUST use custom URI schemes or loopback http URIs | shall | Section 2 (application_type) |
| R4 | Authorization Server MUST verify all registered `redirect_uris` conform to constraints | shall | Section 2 |
| R5 | `jwks_uri` MUST use `https` scheme | shall | Section 2 |
| R6 | If client can use `jwks_uri`, it MUST NOT use `jwks` | shall | Section 2 |
| R7 | `jwks_uri` and `jwks` MUST NOT be used together | shall | Section 2 |
| R8 | JWK Set MUST NOT contain private or symmetric keys | shall | Section 2 |
| R9 | `sector_identifier_uri` MUST be `https` URL referencing JSON array of `redirect_uri` values | shall | Section 5 |
| R10 | All `redirect_uris` MUST be in the array, else registration fails | shall | Section 5 |
| R11 | String comparisons MUST be code point equality without normalization | shall | Section 6 |
| R12 | All communication with Registration Endpoint MUST use TLS | shall | Section 9 |
| R13 | TLS confidentiality and integrity protection MUST be applied | shall | Section 9.3 |
| R14 | TLS server certificate check MUST be performed per RFC 6125 | shall | Section 9.3 |
| R15 | `id_token_signed_response_alg` value `none` MUST NOT be used unless no ID Token from Authorization Endpoint | shall | Section 2 |
| R16 | `token_endpoint_auth_signing_alg` value `none` MUST NOT be used | shall | Section 2 |
| R17 | If `id_token_encrypted_response_enc` included, `id_token_encrypted_response_alg` MUST also be provided | shall | Section 2 |
| R18 | If `userinfo_encrypted_response_enc` included, `userinfo_encrypted_response_alg` MUST also be provided | shall | Section 2 |
| R19 | If `request_object_encryption_enc` included, `request_object_encryption_alg` MUST also be provided | shall | Section 2 |
| R20 | Client MUST use `registration_client_uri` as given; MUST NOT construct from pieces | shall | Section 4.1 |
| R21 | Authorization Server MUST provide `registration_client_uri` together with `registration_access_token` | shall | Section 3.2 |
| R22 | `registration_client_uri` MUST use `https` scheme | shall | Section 3.2 |
| R23 | `client_secret` MUST NOT be assigned to multiple Clients | shall | Section 3.2 |
| R24 | Client MUST use Registration Access Token in all calls to Client Configuration Endpoint | shall | Section 4 |
| R25 | If Registration Access Token invalid, server MUST respond with error per [RFC6750] | shall | Section 4.4 |
| R26 | If Client does not exist or invalid, server MUST respond with HTTP 401 | shall | Section 4.4 |
| R27 | If no permission, server MUST return HTTP 403 | shall | Section 4.4 |
| R28 | Endpoints MUST NOT return HTTP 404 | shall | Section 4.4 |
| R29 | OPs can require `request_uri` values be pre-registered | may | Section 2 |

## Informative Annexes (Condensed)
- **Appendix A - Acknowledgements**: Lists contributors including Amanda Anganes, John Bradley, Brian Campbell, Vladimir Dzhuvinov, George Fletcher, Roland Hedberg, Edmund Jay, Michael B. Jones, Torsten Lodderstedt, Justin Richer, Nat Sakimura.
- **Appendix B - Notices**: Copyright (c) 2023 The OpenID Foundation. Grants non-exclusive, royalty-free license to reproduce, prepare derivative works, distribute, perform, and display this specification for developing specifications and implementations. Disclaims warranties. Patent promise policy applies.