# RFC 9068: JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens
**Source**: IETF | **Version**: Standards Track | **Date**: October 2021 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9068

## Scope (Summary)
This specification defines a standardized profile for issuing OAuth 2.0 access tokens in JSON Web Token (JWT) format, enabling interoperable issuance and consumption across different authorization servers and resource servers.

## Normative References
- [OpenID.Core]: Sakimura, N., et al., "OpenID Connect Core 1.0 incorporating errata set 1", November 2014.
- [OpenID.Discovery]: Sakimura, N., et al., "OpenID Connect Discovery 1.0 incorporating errata set 1", November 2014.
- [RFC2046]: Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", 1996.
- [RFC2119]: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, 1997.
- [RFC6749]: Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", 2012.
- [RFC6838]: Freed, N., et al., "Media Type Specifications and Registration Procedures", BCP 13, 2013.
- [RFC7515]: Jones, M., et al., "JSON Web Signature (JWS)", 2015.
- [RFC7518]: Jones, M., "JSON Web Algorithms (JWA)", 2015.
- [RFC7519]: Jones, M., et al., "JSON Web Token (JWT)", 2015.
- [RFC7643]: Hunt, P., Ed., et al., "System for Cross-domain Identity Management: Core Schema", 2015.
- [RFC8174]: Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, 2017.
- [RFC8414]: Jones, M., et al., "OAuth 2.0 Authorization Server Metadata", 2018.
- [RFC8693]: Jones, M., et al., "OAuth 2.0 Token Exchange", 2020.
- [RFC8707]: Campbell, B., et al., "Resource Indicators for OAuth 2.0", 2020.
- [RFC8725]: Sheffer, Y., et al., "JSON Web Token Best Current Practices", BCP 225, 2020.

## Definitions and Abbreviations
- **JWT access token**: An OAuth 2.0 access token encoded in JWT format and complying with the requirements described in this specification.
- **access token, refresh token, authorization server, resource server, authorization endpoint, authorization request, authorization response, token endpoint, grant type, access token request, access token response, client**: As defined in [RFC6749].
- **RS256**: Algorithm as defined in [RFC7518].

## 1.1. Requirements Notation and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals.

## 2. JWT Access Token Header and Data Structure

### 2.1. Header
- **R1**: JWT access tokens MUST be signed.
- **R2**: JWT access tokens MUST NOT use "none" as the signing algorithm.
- **R3**: Authorization servers and resource servers conforming to this specification MUST include RS256 among their supported signature algorithms.
- **R4**: JWT access tokens MUST include "application/at+jwt" media type in the "typ" header parameter. Per [RFC7515], it is RECOMMENDED that the "application/" prefix be omitted; therefore, the "typ" value used SHOULD be "at+jwt".
- Use of asymmetric cryptography is RECOMMENDED (simplifies validation key acquisition, see Section 4).

### 2.2. Data Structure
The following claims are REQUIRED: **iss**, **exp**, **aud**, **sub**, **client_id**, **iat**, **jti**.
- **iss** (REQUIRED) – as defined in Section 4.1.1 of [RFC7519].
- **exp** (REQUIRED) – as defined in Section 4.1.4 of [RFC7519].
- **aud** (REQUIRED) – as defined in Section 4.1.3 of [RFC7519]; see Section 3 for determination.
- **sub** (REQUIRED) – as defined in Section 4.1.2 of [RFC7519]; in resource-owner grants, SHOULD correspond to the resource owner subject identifier; in client credentials grants, SHOULD correspond to an identifier the authorization server uses to indicate the client application. See Sections 5 and 6.
- **client_id** (REQUIRED) – as defined in Section 4.3 of [RFC8693].
- **iat** (REQUIRED) – as defined in Section 4.1.6 of [RFC7519]; identifies the time at which the JWT access token was issued.
- **jti** (REQUIRED) – as defined in Section 4.1.7 of [RFC7519].

#### 2.2.1. Authentication Information Claims
MAY be issued in grants involving resource owner. Their values are fixed across all access tokens deriving from a given authorization response.
- **auth_time** (OPTIONAL) – as defined in Section 2 of [OpenID.Core].
- **acr** (OPTIONAL) – as defined in Section 2 of [OpenID.Core].
- **amr** (OPTIONAL) – as defined in Section 2 of [OpenID.Core].

#### 2.2.2. Identity Claims
- Any additional identity attribute whose semantic is well described by an entry in the JWT IANA registry SHOULD be encoded using the corresponding claim name, including claims from Section 5.1 of [OpenID.Core].
- Authorization servers MAY return arbitrary attributes not defined in any specification, as long as claim names are collision resistant or tokens are for private subsystems (see Sections 4.2 and 4.3 of [RFC7519]).
- Authorization servers including resource owner attributes MUST verify privacy requirements (Section 6).

#### 2.2.3. Authorization Claims
- **R5**: If an authorization request includes a scope parameter, the issued JWT access token SHOULD include a "scope" claim as defined in Section 4.2 of [RFC8693].
- All individual scope strings in the "scope" claim MUST have meaning for the resources indicated in the "aud" claim.

##### 2.2.3.1. Claims for Authorization Outside of Delegation Scenarios
- Authorization servers wanting to include attributes such as roles, groups, entitlements SHOULD use the "groups", "roles", and "entitlements" attributes of the "User" resource schema defined by Section 4.1.2 of [RFC7643] as claim types.
- Authorization servers SHOULD encode claim values according to [RFC7643].
- Section 7.2.1 registers these attributes as claims in the JWT IANA registry.

## 3. Requesting a JWT Access Token
- An authorization server can issue a JWT access token in response to any authorization grant defined by [RFC6749] and extensions that result in an access token.
- **R6**: If the request includes a "resource" parameter (per [RFC8707]), the resulting JWT access token "aud" claim SHOULD have the same value as the "resource" parameter.
- **R7**: The authorization server MUST NOT issue a JWT access token if the authorization granted would be ambiguous.
- **R8**: If the request does not include a "resource" parameter, the authorization server MUST use a default resource indicator in the "aud" claim.
- **R9**: If a "scope" parameter is present, the authorization server SHOULD use it to infer the value of the default resource indicator. If scope values refer to different default resource indicators, the authorization server SHOULD reject the request with "invalid_scope" as described in Section 4.1.2.1 of [RFC6749].

## 4. Validating JWT Access Tokens
- It is RECOMMENDED that authorization servers sign JWT access tokens with an asymmetric algorithm.
- Authorization servers SHOULD use OAuth 2.0 Authorization Server Metadata [RFC8414] to advertise signing keys via "jwks_uri" and issuer via "issuer". OpenID Connect discovery MAY be used. If both are supported, values MUST be consistent.
- Resources servers receiving a JWT access token MUST validate as follows:
  - **R10**: MUST verify that the "typ" header value is "at+jwt" or "application/at+jwt"; reject any other value.
  - **R11**: If encrypted, decrypt using keys negotiated at registration; if not encrypted when encryption was expected, SHOULD reject.
  - **R12**: The issuer identifier MUST exactly match the "iss" claim.
  - **R13**: MUST validate that the "aud" claim contains a resource indicator corresponding to the resource server; reject if not.
  - **R14**: MUST validate the signature per [RFC7515] using the algorithm specified in "alg" Header Parameter. MUST reject any JWT with "alg" value "none". MUST use keys provided by the authorization server.
  - **R15**: Current time MUST be before "exp" value (implementers MAY provide small leeway for clock skew).
- **R16**: Resource servers MUST handle errors as described in Section 3.1 of [RFC6750]; on any validation failure, error code "invalid_token" MUST be included.
- If JWT access token includes authorization claims (Section 2.2.3), resource server SHOULD use them with other contextual information to decide authorization.

## 5. Security Considerations
- The explicit typing (typ="at+jwt") prevents confusion with OpenID Connect ID Tokens.
- **R17**: To prevent cross-JWT confusion, authorization servers MUST use a distinct identifier as "aud" claim value to uniquely identify access tokens issued by the same issuer for distinct resources (see [RFC8725] Section 2.8).
- Authorization servers should prevent clients from affecting the "sub" claim in ways that could confuse resource servers (e.g., client_id as sub in client credentials grant; prevent arbitrary client_id selection).
- Authorization servers should use care when requests lead to ambiguous authorization grants (e.g., multiple resource indicators; ensure each scope maps unambiguously to a resource in "aud").
- Authorization servers cannot rely on different keys for signing ID Tokens vs JWT access tokens as a security method; resource servers accept any key from discovery.

## 6. Privacy Considerations
- **R18**: The client MUST NOT inspect the content of the access token; token format may change at any time.
- Authorization servers must consider that token content is visible to clients; take steps to prevent privacy violations.
- Possible measures: encrypting the token, encrypting sensitive claims, omitting sensitive claims, not using this profile, or falling back to opaque tokens.
- The content is eventually accessible to the resource server; ensure proper entitlement (e.g., user consent) for non-mandatory claims.
- "sub" claim correlation: Authorization servers should populate "sub" according to privacy impact assessment. To prevent tracking across resource servers, use distinct "sub" values per resource server. To prevent correlation within a resource server, assign different "sub" and "jti" for each token; client should obtain a new token per call.

## 7. IANA Considerations

### 7.1. Media Type Registration
- **application/at+jwt** registered in the "Media Types" registry.
- Encoding: Base64url-encoded values separated by periods.

### 7.2. Claims Registration
The following attributes from [RFC7643] are registered as JWT claims:
- **roles** (Claim Name: roles, Description: Roles, Specification: Section 4.1.2 of [RFC7643] and Section 2.2.3.1 of RFC 9068)
- **groups** (Claim Name: groups, Description: Groups)
- **entitlements** (Claim Name: entitlements, Description: Entitlements)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | JWT access tokens MUST be signed. | shall | Section 2.1 |
| R2 | JWT access tokens MUST NOT use "none" algorithm. | shall | Section 2.1 |
| R3 | Authorization and resource servers MUST support RS256. | shall | Section 2.1 |
| R4 | JWT access tokens MUST include "typ" header with "at+jwt" (or "application/at+jwt"). | shall | Section 2.1 |
| R5 | If authorization request includes "scope", JWT access token SHOULD include "scope" claim. | should | Section 2.2.3 |
| R6 | If request includes "resource", "aud" SHOULD equal resource. | should | Section 3 |
| R7 | Authorization server MUST NOT issue JWT access token if authorization ambiguous. | shall | Section 3 |
| R8 | If no "resource" parameter, MUST use default resource indicator in "aud". | shall | Section 3 |
| R9 | If "scope" refers to different default resource indicators, SHOULD reject with "invalid_scope". | should | Section 3 |
| R10 | Resource server MUST verify "typ" header is "at+jwt" or "application/at+jwt". | shall | Section 4 |
| R11 | If encrypted and expected, resource server SHOULD reject if not encrypted. | should | Section 4 |
| R12 | Resource server MUST validate that "iss" matches expected issuer. | shall | Section 4 |
| R13 | Resource server MUST validate that "aud" contains its identifier. | shall | Section 4 |
| R14 | Resource server MUST validate signature and reject "alg" = "none". | shall | Section 4 |
| R15 | Resource server MUST verify "exp" is in the future. | shall | Section 4 |
| R16 | On validation failure, resource server MUST use error "invalid_token" per RFC6750. | shall | Section 4 |
| R17 | Authorization server MUST use distinct "aud" values to prevent cross-JWT confusion. | shall | Section 5 |
| R18 | Client MUST NOT inspect access token content. | shall | Section 6 |

## Informative Annexes (Condensed)
- **Acknowledgements**: The specification benefited from sample tokens provided by IdentityServer, Ping Identity, Microsoft, and Okta. Contributions from John Bradley, Brian Campbell, Vladimir Dzhuvinov, Torsten Lodderstedt, Nat Sakimura, Hannes Tschofenig, and many others. Reviews by Roman Danyliw, Joseph Salowey, Roni Even, Francesca Palomini, Lars Eggert, Murray Kucherawy, Roberto Polli, Martin Duke, Benjamin Kaduk.