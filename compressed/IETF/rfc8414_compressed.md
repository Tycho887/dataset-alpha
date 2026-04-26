# RFC 8414: OAuth 2.0 Authorization Server Metadata
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: June 2018 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc8414

## Scope (Summary)
This specification defines a metadata format for OAuth 2.0 authorization servers, enabling clients to discover endpoint locations, capabilities, and public keys. The metadata is retrieved as a JSON document from a well-known location (default: `/.well-known/oauth-authorization-server`), and may also be provided as a signed JWT.

## Normative References
- [BCP195] Sheffer, Y., Holz, R., and P. Saint-Andre, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525, May 2015
- [IANA.OAuth.Parameters] IANA, "OAuth Parameters"
- [JWE] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, May 2015
- [JWK] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015
- [JWS] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015
- [JWT] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, May 2015
- [OAuth.Post] Jones, M. and B. Campbell, "OAuth 2.0 Form Post Response Mode", April 2015
- [OAuth.Responses] de Medeiros, B., et al., "OAuth 2.0 Multiple Response Type Encoding Practices", February 2014
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008
- [RFC5646] Phillips, A., Ed. and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009
- [RFC5785] Nottingham, M. and E. Hammer-Lahav, "Defining Well-Known Uniform Resource Identifiers (URIs)", RFC 5785, April 2010
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity...", RFC 6125, March 2011
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012
- [RFC7009] Lodderstedt, T., et al., "OAuth 2.0 Token Revocation", RFC 7009, August 2013
- [RFC7033] Jones, P., et al., "WebFinger", RFC 7033, September 2013
- [RFC7591] Richer, J., et al., "OAuth 2.0 Dynamic Client Registration Protocol", RFC 7591, July 2015
- [RFC7636] Sakimura, N., et al., "Proof Key for Code Exchange by OAuth Public Clients", RFC 7636, September 2015
- [RFC7662] Richer, J., Ed., "OAuth 2.0 Token Introspection", RFC 7662, October 2015
- [RFC8126] Cotton, M., et al., "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 8126, June 2017
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017
- [UNICODE] The Unicode Consortium, "The Unicode Standard"
- [USA15] Davis, M., Ed. and K. Whistler, Ed., "Unicode Normalization Forms", Unicode Standard Annex #15, May 2018

## Definitions and Abbreviations
- **Access Token**, **Authorization Code**, **Authorization Endpoint**, **Authorization Grant**, **Authorization Server**, **Client**, **Client Authentication**, **Client Identifier**, **Client Secret**, **Grant Type**, **Protected Resource**, **Redirection URI**, **Refresh Token**, **Resource Owner**, **Resource Server**, **Response Type**, **Token Endpoint**: as defined in OAuth 2.0 [RFC6749].
- **Claim Name**, **Claim Value**, **JSON Web Token (JWT)**: as defined in JWT [RFC7519].
- **Response Mode**: as defined in OAuth 2.0 Multiple Response Type Encoding Practices [OAuth.Responses].

## 1. Introduction (Condensed)
Generalizes OpenID Connect Discovery metadata for general OAuth 2.0 use. Metadata is retrieved from a well-known HTTPS location as a JSON document (Section 3). Can be self-asserted or signed JWT. Client selection of authorization server is out of scope.

### 1.1. Requirements Notation and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in BCP 14 [RFC2119] [RFC8174]. JWS and JWE use Compact Serialization only.

## 2. Authorization Server Metadata
Authorization servers may have metadata describing configuration. The following metadata values are defined (see also Requirements Summary table):

- **issuer** (REQUIRED): The authorization server's issuer identifier, URL using "https", no query or fragment. Used to prevent mix-up attacks.
- **authorization_endpoint** (REQUIRED unless no grant types use it): URL of authorization endpoint [RFC6749].
- **token_endpoint** (REQUIRED unless only implicit grant): URL of token endpoint.
- **jwks_uri** (OPTIONAL): URL of JWK Set document; MUST use "https". JWK Set MAY include encryption keys; if both signing and encryption keys present, a "use" parameter REQUIRED for all keys.
- **registration_endpoint** (OPTIONAL): URL of Dynamic Client Registration endpoint [RFC7591].
- **scopes_supported** (RECOMMENDED): JSON array of supported scope values.
- **response_types_supported** (REQUIRED): JSON array of supported response_type values (same as [RFC7591]).
- **response_modes_supported** (OPTIONAL): JSON array of supported response_mode values; default: "["query", "fragment"]".
- **grant_types_supported** (OPTIONAL): JSON array of grant type values; default: "["authorization_code", "implicit"]".
- **token_endpoint_auth_methods_supported** (OPTIONAL): JSON array of client authentication methods; default: "client_secret_basic".
- **token_endpoint_auth_signing_alg_values_supported** (OPTIONAL): JSON array of JWS signing algorithms for "private_key_jwt" and "client_secret_jwt"; MUST be present if those methods are listed; SHOULD support "RS256"; value "none" MUST NOT be used.
- **service_documentation** (OPTIONAL): URL of human-readable developer information.
- **ui_locales_supported** (OPTIONAL): JSON array of BCP 47 language tags.
- **op_policy_uri** (OPTIONAL): URL for client data usage policy.
- **op_tos_uri** (OPTIONAL): URL for terms of service.
- **revocation_endpoint** (OPTIONAL): URL of revocation endpoint [RFC7009].
- **revocation_endpoint_auth_methods_supported** (OPTIONAL): JSON array of client authentication methods; default: "client_secret_basic".
- **revocation_endpoint_auth_signing_alg_values_supported** (OPTIONAL): JWS signing algorithms for revocation endpoint; MUST be present if "private_key_jwt" or "client_secret_jwt" listed; "none" MUST NOT be used.
- **introspection_endpoint** (OPTIONAL): URL of introspection endpoint [RFC7662].
- **introspection_endpoint_auth_methods_supported** (OPTIONAL): JSON array of client authentication methods; if omitted, supported methods MUST be determined by other means.
- **introspection_endpoint_auth_signing_alg_values_supported** (OPTIONAL): JWS signing algorithms for introspection; MUST be present if "private_key_jwt" or "client_secret_jwt" listed; "none" MUST NOT be used.
- **code_challenge_methods_supported** (OPTIONAL): JSON array of PKCE challenge methods [RFC7636]; if omitted, does not support PKCE.

Additional metadata parameters MAY be defined by other specifications (e.g., OpenID Connect Discovery).

### 2.1. Signed Authorization Server Metadata
Metadata values MAY also be provided as a `signed_metadata` value, a JWT asserting metadata values. The JWT MUST be signed or MACed using JWS and MUST contain an "iss" claim. If consumer supports signed metadata, values conveyed in the signed JWT MUST take precedence over plain JSON values. The `signed_metadata` member is OPTIONAL and SHOULD NOT appear as a claim in the JWT.

## 3. Obtaining Authorization Server Metadata
Authorization servers supporting metadata MUST make a JSON document (as per Section 2) available at a path formed by inserting `/.well-known/oauth-authorization-server` into the issuer identifier between host and path components. This path MUST use "https". Different applications MAY register and use different well-known URI suffixes. An OAuth 2.0 application using this specification MUST specify what well-known URI suffix it will use.

### 3.1. Authorization Server Metadata Request
Query using HTTP GET. Examples for issuer without path and with path are given. Path components enable multiple issuers per host.

### 3.2. Authorization Server Metadata Response
Successful response MUST use HTTP 200 OK and return a JSON object with `application/json` content type containing metadata claims. Claims with zero elements MUST be omitted. An error response uses applicable HTTP status code.

### 3.3. Authorization Server Metadata Validation
The `issuer` value in the response MUST be identical to the issuer identifier used for the request; if not, the data MUST NOT be used.

## 4. String Operations
Unicode string comparisons MUST be performed as follows: 1) Remove JSON escaping, 2) Do NOT apply Unicode normalization, 3) Compare code point by code point. Equivalent to Section 8.3 of [RFC8259].

## 5. Compatibility Notes (Informative)
Identifiers like `/.well-known/openid-configuration`, `op_policy_uri`, `op_tos_uri` originated from OpenID Connect but refer to general OAuth 2.0 features. The transformation of issuer to metadata location differs from OpenID Connect Discovery when a path component exists; this specification inserts before the path, while OpenID appends after. For legacy compatibility when using `openid-configuration`, clients should first try the new location, then fall back to the old location.

## 6. Security Considerations
### 6.1. TLS Requirements
Implementations MUST support TLS. Authorization server MUST support TLS 1.2 [RFC5246] and MAY support additional mechanisms. Client MUST perform TLS/SSL server certificate check per RFC 6125. Confidentiality protection MUST be applied using TLS with a ciphersuite that provides confidentiality and integrity.

### 6.2. Impersonation Attacks
TLS certificate checking MUST be performed by client (Section 6.1). The client MUST ensure the issuer identifier URL matches the `issuer` metadata value to prevent impersonation via forged metadata.

### 6.3. Publishing Metadata in a Standard Format
Publishing in standard format aids both legitimate clients and attackers; same defenses apply as with ad hoc publishing.

### 6.4. Protected Resources
Secure determination of appropriate protected resources is out of scope. Application dependent.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | The authorization server's issuer identifier MUST be provided. | shall | Section 2 - issuer |
| R2 | Authorization endpoint URL MUST be provided unless no grant types use it. | shall | Section 2 - authorization_endpoint |
| R3 | Token endpoint URL MUST be provided unless only implicit grant is supported. | shall | Section 2 - token_endpoint |
| R4 | jwks_uri URL MUST use "https" scheme. | shall | Section 2 - jwks_uri |
| R5 | If both signing and encryption keys are in the JWK Set, a "use" parameter is REQUIRED for all keys. | shall | Section 2 - jwks_uri |
| R6 | response_types_supported MUST be provided. | shall | Section 2 - response_types_supported |
| R7 | token_endpoint_auth_signing_alg_values_supported MUST be present if "private_key_jwt" or "client_secret_jwt" are listed. | shall | Section 2 |
| R8 | The JWS algorithm "none" MUST NOT be used for token endpoint authentication signing. | shall | Section 2 |
| R9 | Signed metadata MUST be digitally signed or MACed using JWS and MUST contain "iss" claim. | shall | Section 2.1 |
| R10 | If consumer supports signed metadata, signed metadata values MUST take precedence over plain JSON. | shall | Section 2.1 |
| R11 | Authorization server metadata MUST be made available at the well-known path derived from the issuer identifier. | shall | Section 3 |
| R12 | The well-known path MUST use "https" scheme. | shall | Section 3 |
| R13 | An OAuth 2.0 application using this specification MUST specify what well-known URI suffix it will use. | shall | Section 3 |
| R14 | Successful metadata response MUST use HTTP 200 OK and "application/json". | shall | Section 3.2 |
| R15 | Claims with zero elements MUST be omitted. | shall | Section 3.2 |
| R16 | The "issuer" value in response MUST be identical to the issuer identifier used. If not, data MUST NOT be used. | shall | Section 3.3 |
| R17 | String comparisons MUST be performed per Section 4 (no normalization, code point equality). | shall | Section 4 |
| R18 | Implementations MUST support TLS. | shall | Section 6.1 |
| R19 | Authorization server MUST support TLS 1.2. | shall | Section 6.1 |
| R20 | Client MUST perform TLS/SSL server certificate check per RFC 6125. | shall | Section 6.1 |
| R21 | Confidentiality protection MUST be applied using TLS with confidentiality and integrity ciphersuite. | shall | Section 6.1 |
| R22 | TLS certificate checking MUST be performed by client when making metadata request. | shall | Section 6.2 |
| R23 | Client MUST ensure the issuer identifier URL exactly matches the "issuer" metadata value. | shall | Section 6.2 |
| R24 | Revocation endpoint auth_signing_alg_values_supported MUST be present if "private_key_jwt" or "client_secret_jwt" are listed; "none" MUST NOT be used. | shall | Section 2 - revocation |
| R25 | Introspection endpoint auth_signing_alg_values_supported MUST be present if "private_key_jwt" or "client_secret_jwt" are listed; "none" MUST NOT be used. | shall | Section 2 - introspection |

## IANA Considerations (Condensed)
### 7.1 OAuth Authorization Server Metadata Registry
Established by this specification. Registration based on Specification Required [RFC8126] with two-week review on oauth-ext-review@ietf.org. Designated Experts must ensure metadata names use only printable ASCII (except '"' and '\') or define exact Unicode sequences.

#### 7.1.1 Registration Template
- Metadata Name, Description, Change Controller, Specification Document(s)

#### 7.1.2 Initial Registry Contents
Includes all metadata members defined in Section 2 (issuer, authorization_endpoint, token_endpoint, jwks_uri, registration_endpoint, scopes_supported, response_types_supported, response_modes_supported, grant_types_supported, token_endpoint_auth_methods_supported, token_endpoint_auth_signing_alg_values_supported, service_documentation, ui_locales_supported, op_policy_uri, op_tos_uri, revocation_endpoint, revocation_endpoint_auth_methods_supported, revocation_endpoint_auth_signing_alg_values_supported, introspection_endpoint, introspection_endpoint_auth_methods_supported, introspection_endpoint_auth_signing_alg_values_supported, code_challenge_methods_supported, signed_metadata). Change Controller: IESG.

### 7.2 Updated Registration Instructions
Adds instructions for Designated Experts of "OAuth Access Token Types" and "OAuth Token Endpoint Authentication Methods" registries to reject duplicate values across registries.

### 7.3 Well-Known URI Registry
Registers suffix "oauth-authorization-server". Change Controller: IESG. Specification document: Section 3 of RFC 8414.

## Informative Annexes (Condensed)
- **Compatibility Notes (Section 5)**: Explains that identifiers from OpenID Connect are used for general OAuth 2.0 features; provides migration guidance for legacy deployments.
- **Security Considerations (Section 6.3-6.4)**: Warns that standard format helps attackers but same defenses apply; secure determination of protected resources is application-specific.
- **IANA Registration Process (Section 7)**: Detailed procedure for registering new metadata names, including requirement for printable ASCII or defined Unicode sequences.