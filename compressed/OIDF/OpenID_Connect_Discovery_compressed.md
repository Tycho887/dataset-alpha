# OpenID Connect Discovery 1.0 incorporating errata set 2
**Source**: OpenID Foundation | **Version**: 1.0 (incorporating errata set 2) | **Date**: December 15, 2023 | **Type**: Normative
**Original**: OpenID Connect Discovery 1.0 – Final specification

## Scope (Summary)
Defines a mechanism for an OpenID Connect Relying Party (RP) to discover the End-User's OpenID Provider (OP) using WebFinger [RFC7033] and obtain OP configuration metadata (including OAuth 2.0 endpoint locations) from a well-known location.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3986] Berners-Lee, T., Fielding, R., L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC5322] Resnick, P., Ed., "Internet Message Format", RFC 5322, October 2008.
- [RFC5646] Phillips, A., Ed., M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- [RFC5785] Nottingham, M., E. Hammer-Lahav, "Defining Well-Known Uniform Resource Identifiers (URIs)", RFC 5785, April 2010.
- [RFC6125] Saint-Andre, P., J. Hodges, "Representation and Verification of Domain-Based Application Service Identity...", RFC 6125, March 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [RFC7033] Jones, P., Salgueiro, G., Jones, M., J. Smarr, "WebFinger", RFC 7033, September 2013.
- [RFC7565] Saint-Andre, P., "The 'acct' URI Scheme", RFC 7565, May 2015.
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017.
- [RFC8996] Moriarty, K., S. Farrell, "Deprecating TLS 1.0 and TLS 1.1", BCP 195, RFC 8996, March 2021.
- [RFC9325] Sheffer, Y., Saint-Andre, P., T. Fossati, "Recommendations for Secure Use of TLS and DTLS", BCP 195, RFC 9325, November 2022.
- [JWS] Jones, M., Bradley, J., N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015.
- [JWE] Jones, M., J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, May 2015.
- [JWK] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015.
- [JWT] Jones, M., Bradley, J., N. Sakimura, "JSON Web Token (JWT)", RFC 7519, May 2015.
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015.
- [OpenID.Core] Sakimura, N., Bradley, J., Jones, M., de Medeiros, B., C. Mortimore, "OpenID Connect Core 1.0", December 2023.
- [OpenID.Registration] Sakimura, N., Bradley, J., M. Jones, "OpenID Connect Dynamic Client Registration 1.0", December 2023.
- [OAuth.Responses] de Medeiros, B., Ed., Scurtescu, M., Tarjan, P., M. Jones, "OAuth 2.0 Multiple Response Type Encoding Practices", February 2014.
- [CORS] Opera Software ASA, "Cross-Origin Resource Sharing", July 2010.
- [UNICODE] The Unicode Consortium, "The Unicode Standard".
- [USA15] Whistler, K., "Unicode Normalization Forms", Unicode Standard Annex 15, August 2023.

## Definitions and Abbreviations
- **Authorization Code, Authorization Endpoint, Authorization Server, Client, Client Authentication, Client Secret, Grant Type, Response Type, Token Endpoint**: As defined by [RFC6749].
- **Claim Name, Claim Value, JSON Web Token (JWT)**: As defined by [JWT].
- **Terms from OpenID Connect Core 1.0** [OpenID.Core] and **OAuth 2.0 Multiple Response Type Encoding Practices** [OAuth.Responses].
- **Resource**: Entity that is the target of a request in WebFinger.
- **Host**: Server where a WebFinger service is hosted.
- **Identifier**: Value that uniquely characterizes an Entity in a specific context. Examples: URLs, e-mail addresses.
- **Issuer**: The OpenID Provider's identifier (URL using https scheme with no query/fragment).
- **OP**: OpenID Provider.
- **RP**: Relying Party.
- **TLS**: Transport Layer Security.
- **CORS**: Cross-Origin Resource Sharing.
- **JWS/JWE/JWK/JWA**: As per respective RFCs.

## 1. Introduction
OpenID Connect 1.0 is an identity layer on top of OAuth 2.0 [RFC6749]. This specification defines discovery mechanisms for an RP to locate the OP and obtain its configuration. Discovery uses WebFinger [RFC7033] to find the OP (Section 2) and then retrieves a JSON metadata document (Section 4). Previous versions: [OpenID.Discovery.Errata1], [OpenID.Discovery.Final].

### 1.1. Requirements Notation and Conventions
- Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL – per RFC 2119.
- In .txt versions, quoted values are literal; quotes MUST NOT be used in protocol messages.
- All JWS/JWE structures use Compact Serialization only; JSON Serialization not used.

### 1.2. Terminology
- Defined terms from [RFC6749], [JWT], [OpenID.Core], [OAuth.Responses] apply.
- Additionally defines: Resource, Host, Identifier. These definitions are normative.

## 2. OpenID Provider Issuer Discovery
- Discovery is OPTIONAL; if RP knows Issuer location out-of-band, skip to Section 4.
- Uses WebFinger [RFC7033] with:
  - `resource`: Identifier for target End-User.
  - `host`: Server hosting WebFinger.
  - `rel`: URI identifying service type. OpenID Connect uses `http://openid.net/specs/connect/1.0/issuer`.
- Steps:
  1. End-User supplies an Identifier to RP. Any Web input form MUST employ CSRF prevention [OWASP.CSRF].
  2. RP applies normalization (Section 2.1) to determine `resource` and `host`.
  3. RP makes HTTP GET to Host's WebFinger endpoint with `resource` parameter; use of `rel` parameter RECOMMENDED.
  4. All WebFinger communication MUST use TLS (see Section 7.1).
  5. WebFinger endpoint SHOULD support CORS for JavaScript clients.
  6. Issuer location returned in WebFinger response as `href` value of a `links` array element with `rel` as above.
  7. Returned Issuer MUST be a URI [RFC3986] with scheme `https`, host, optionally port and path, no query or fragment. No relationship assumed between user input and resulting Issuer.

### 2.1. Identifier Normalization
- Purpose: Determine normalized `resource` and `host` values for WebFinger.
- User input Identifier SHOULD be a URL or URI relative reference [RFC3986]. MUST include authority component. Normalization rules MAY be extended for other identifier types (e.g., telephone numbers, XRIs).

#### 2.1.1. User Input Identifier Types
- Identifiers starting with XRI symbols ('=', '@', '!') are RESERVED; processing out of scope.
- All other Identifiers MUST be treated as URI in one of three forms per [RFC3986]: `scheme "://" authority path-abempty [ "?" query ] [ "#" fragment ]` or `authority path-abempty [ "?" query ] [ "#" fragment ]` or `scheme ":" path-rootless`.
- NOTE: `userinfo@host` is treated as an `acct` URI [RFC7565], not full email address.

#### 2.1.2. Normalization Steps
- For string without scheme: interpret as `[userinfo "@"] host [":" port] path-abempty [ "?" query ] [ "#" fragment ]`.
  - If userinfo and host present, no scheme, path, query, port, fragment: assume `acct` scheme, prefix `acct:`.
  - Otherwise: assume `https` scheme, prefix `https://`.
- For input with explicit scheme (`acct`, `https`): no normalization performed.
- Fragment component MUST be stripped.
- WebFinger Resource = resulting URI; Host = authority component.

### 2.2. Non-Normative Examples
- 2.2.1: E-mail syntax (joe@example.com) → resource: `acct:joe@example.com`, host: example.com. Sample request/response.
- 2.2.2: URL syntax (https://example.com/joe) → resource: same, host: example.com.
- 2.2.3: Hostname:port (example.com:8080) → resource: `https://example.com:8080/`, host: example.com:8080.
- 2.2.4: acct URI (acct:juliet%40capulet.example@shopping.example.com) → resource: as given, host: shopping.example.com. NOTE: local accounts with email syntax: e.g., `acct:joe%40example.com@example.org`; End-Users MAY input `joe@example.com@example.org`.

## 3. OpenID Provider Metadata
- Metadata describing OP configuration. All values below are normative.
- **issuer** – REQUIRED. URL using https with no query/fragment. Must match WebFinger and `iss` in ID Tokens.
- **authorization_endpoint** – REQUIRED. URL of OP's OAuth 2.0 Authorization Endpoint [OpenID.Core]. MUST use https.
- **token_endpoint** – URL of OAuth 2.0 Token Endpoint. REQUIRED unless only Implicit Flow. MUST use https.
- **userinfo_endpoint** – RECOMMENDED. URL of UserInfo Endpoint. MUST use https.
- **jwks_uri** – REQUIRED. URL of OP's JWK Set [JWK]. MUST use https. Contains signing keys; encryption keys MAY be included. Use parameter REQUIRED for each key. Using same key for both signatures and encryption NOT RECOMMENDED. `x5c` MAY be used but bare key values MUST be present and match. JWK Set MUST NOT contain private/symmetric keys.
- **registration_endpoint** – RECOMMENDED. URL of Dynamic Client Registration Endpoint [OpenID.Registration]. MUST use https.
- **scopes_supported** – RECOMMENDED. JSON array of supported OAuth 2.0 scopes. MUST support `openid`. Those defined in [OpenID.Core] SHOULD be listed if supported.
- **response_types_supported** – REQUIRED. JSON array of supported `response_type` values. Dynamic OPs MUST support `code`, `id_token`, `id_token token`.
- **response_modes_supported** – OPTIONAL. JSON array of supported `response_mode`. Default: `["query", "fragment"]` for Dynamic OPs.
- **grant_types_supported** – OPTIONAL. JSON array of supported Grant Types. Dynamic OPs MUST support `authorization_code` and `implicit`. Default: `["authorization_code", "implicit"]`.
- **acr_values_supported** – OPTIONAL. JSON array of supported ACR values.
- **subject_types_supported** – REQUIRED. JSON array. Valid: `pairwise`, `public`.
- **id_token_signing_alg_values_supported** – REQUIRED. JSON array of JWS `alg` values for ID Token. `RS256` MUST be included. `none` MAY be supported but MUST NOT be used unless no ID Token from Authorization Endpoint.
- **id_token_encryption_alg_values_supported** – OPTIONAL. JSON array of JWE `alg` values for ID Token.
- **id_token_encryption_enc_values_supported** – OPTIONAL. JSON array of JWE `enc` values.
- **userinfo_signing_alg_values_supported** – OPTIONAL. JWS `alg` values for UserInfo Endpoint. `none` MAY be included.
- **userinfo_encryption_alg_values_supported** – OPTIONAL.
- **userinfo_encryption_enc_values_supported** – OPTIONAL.
- **request_object_signing_alg_values_supported** – OPTIONAL. JWS `alg` values for Request Objects. Servers SHOULD support `none` and `RS256`.
- **request_object_encryption_alg_values_supported** – OPTIONAL.
- **request_object_encryption_enc_values_supported** – OPTIONAL.
- **token_endpoint_auth_methods_supported** – OPTIONAL. JSON array of Client Authentication methods: `client_secret_post`, `client_secret_basic`, `client_secret_jwt`, `private_key_jwt`. Default: `client_secret_basic`.
- **token_endpoint_auth_signing_alg_values_supported** – OPTIONAL. JWS `alg` values for Client authentication JWT. Servers SHOULD support `RS256`. `none` MUST NOT be used.
- **display_values_supported** – OPTIONAL. JSON array of `display` parameter values.
- **claim_types_supported** – OPTIONAL. JSON array of Claim Types: `normal`, `aggregated`, `distributed`. Default: only `normal`.
- **claims_supported** – RECOMMENDED. JSON array of Claim Names that OP MAY supply.
- **service_documentation** – OPTIONAL. URL with human-readable info.
- **claims_locales_supported** – OPTIONAL. JSON array of BCP 47 language tags.
- **ui_locales_supported** – OPTIONAL. JSON array of BCP 47 language tags for UI.
- **claims_parameter_supported** – OPTIONAL. Boolean. Default: `false`.
- **request_parameter_supported** – OPTIONAL. Boolean. Default: `false`.
- **request_uri_parameter_supported** – OPTIONAL. Boolean. Default: `true`.
- **require_request_uri_registration** – OPTIONAL. Boolean. Default: `false`.
- **op_policy_uri** – OPTIONAL. URL for OP's policy. Registration process SHOULD display.
- **op_tos_uri** – OPTIONAL. URL for terms of service. Registration process SHOULD display.
- Token Endpoint, UserInfo Endpoint, jwks_uri, Registration Endpoint, and any other endpoints directly accessed by Clients SHOULD support CORS. Authorization Endpoint: CORS NOT RECOMMENDED.
- Additional metadata parameters MAY be used (e.g., OpenID Connect Session Management 1.0).

## 4. Obtaining OpenID Provider Configuration Information
- OPs supporting Discovery MUST make a JSON document available at `/.well-known/openid-configuration` appended to the Issuer. For Issuer with path components, remove trailing `/` before appending. Uses per [RFC5785] but also allows multiple issuers per host.
- Document MUST be JSON with `application/json` content type.
- Endpoint SHOULD support CORS.

### 4.1. OpenID Provider Configuration Request
- Use HTTP GET to the path. Examples:
  - Issuer `https://example.com`: `GET /.well-known/openid-configuration`
  - Issuer `https://example.com/issuer1`: `GET /issuer1/.well-known/openid-configuration`

### 4.2. OpenID Provider Configuration Response
- Successful response: 200 OK, JSON object with members from Section 3 (subset). Other Claims MAY be returned. Arrays for multiple values; zero-element arrays MUST be omitted.
- Non-normative example in spec.

### 4.3. OpenID Provider Configuration Validation
- `issuer` value MUST match exactly the Issuer URL used as prefix to retrieve config. Must also match `iss` in ID Tokens.
- If validation fails, operations using the failed information MUST be aborted and MUST NOT be used.

## 5. String Operations
- When comparing JSON strings to known values:
  - Remove any JSON escaping to get Unicode code points.
  - Unicode Normalization MUST NOT be applied.
  - Compare code point by code point.

## 6. Implementation Considerations
- All REQUIRED features (MUST) must be implemented by RPs and OPs supporting Discovery. No other considerations.

### 6.1. Compatibility Notes
- Potential issues previously described in original version have been addressed.

## 7. Security Considerations
### 7.1. TLS Requirements
- Implementations MUST support TLS. Follow guidance in BCP 195 [RFC8996][RFC9325].
- Confidentiality and integrity protection MUST be applied using TLS with appropriate ciphersuite.
- TLS server certificate check MUST be performed per [RFC6125].

### 7.2. Impersonation Attacks
- TLS certificate checking MUST be performed by RP when making Configuration Request.
- Check that server certificate is valid for Issuer URL to prevent man-in-middle and DNS attacks.
- RP MUST ensure that the Issuer URL used for Configuration Request exactly matches `issuer` Claim in metadata and `iss` Claim in ID Tokens from that Issuer.

## 8. IANA Considerations
### 8.1. Well-Known URI Registry
- URI suffix: `openid-configuration`; Change controller: OpenID Foundation Artifact Binding Working Group.

### 8.2. OAuth Authorization Server Metadata Registry
- Registers metadata names: userinfo_endpoint, acr_values_supported, subject_types_supported, id_token_signing_alg_values_supported, id_token_encryption_alg_values_supported, id_token_encryption_enc_values_supported, userinfo_signing_alg_values_supported, userinfo_encryption_alg_values_supported, userinfo_encryption_enc_values_supported, request_object_signing_alg_values_supported, request_object_encryption_alg_values_supported, request_object_encryption_enc_values_supported, display_values_supported, claim_types_supported, claims_supported, claims_locales_supported, claims_parameter_supported, request_parameter_supported, request_uri_parameter_supported, require_request_uri_registration. All with change controller OpenID Foundation Artifact Binding Working Group.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Input forms for Issuer discovery MUST employ CSRF prevention. | MUST | Section 2 |
| R2 | All WebFinger communication MUST use TLS as per Section 7.1. | MUST | Section 2 |
| R3 | The WebFinger endpoint SHOULD support CORS. | SHOULD | Section 2 |
| R4 | Returned Issuer MUST be a URI with scheme `https`, host, optionally port and path, no query/fragment. | MUST | Section 2 |
| R5 | User input Identifier MUST include authority component. | MUST | Section 2.1 |
| R6 | Fragment component MUST be stripped from normalized URI. | MUST | Section 2.1.2 |
| R7 | OP metadata `issuer` is REQUIRED; `authorization_endpoint` REQUIRED; `jwks_uri` REQUIRED; `response_types_supported` REQUIRED; `subject_types_supported` REQUIRED; `id_token_signing_alg_values_supported` REQUIRED (RS256 MUST be included). | MUST | Section 3 |
| R8 | `token_endpoint` REQUIRED unless only Implicit Flow. | MUST | Section 3 |
| R9 | `scopes_supported` MUST include `openid`. | MUST | Section 3 |
| R10 | Dynamic OPs MUST support `code`, `id_token`, `id_token token` response types. | MUST | Section 3 |
| R11 | Dynamic OPs MUST support `authorization_code` and `implicit` grant types. | MUST | Section 3 |
| R12 | `none` in `id_token_signing_alg_values_supported` MUST NOT be used unless no ID Token from Authorization Endpoint. | MUST (conditional) | Section 3 |
| R13 | `none` in `token_endpoint_auth_signing_alg_values_supported` MUST NOT be used. | MUST | Section 3 |
| R14 | Using same key for both signatures and encryption is NOT RECOMMENDED. | NOT RECOMMENDED | Section 3 |
| R15 | JWK Set MUST NOT contain private or symmetric keys. | MUST | Section 3 |
| R16 | OP must make JSON document available at `/.well-known/openid-configuration`. | MUST | Section 4 |
| R17 | Configuration response MUST use 200 OK and `application/json`. | MUST | Section 4.2 |
| R18 | `issuer` value in response MUST match Issuer URL used to retrieve config and `iss` in ID Tokens. | MUST | Section 4.3 |
| R19 | String comparisons MUST be code point to code point without Unicode normalization. | MUST | Section 5 |
| R20 | Implementations MUST support TLS. | MUST | Section 7.1 |
| R21 | TLS certificate check MUST be performed per RFC 6125. | MUST | Section 7.1 |
| R22 | RP MUST ensure Issuer URL matches `issuer` Claim and `iss` in ID Tokens. | MUST | Section 7.2 |

## Informative Annexes (Condensed)
- **Appendix A: Acknowledgements**: Lists contributors; no normative content.
- **Appendix B: Notices**: Copyright 2023 OpenID Foundation; grants non-exclusive license for development and implementation of the specification; disclaims warranties; references IPR policy.