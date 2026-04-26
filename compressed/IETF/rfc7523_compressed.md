# RFC 7523: JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7523

## Scope (Summary)
This specification defines the use of a JSON Web Token (JWT) Bearer Token as a means for requesting an OAuth 2.0 access token as well as for client authentication.

## Normative References
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518
- [JWT] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159
- [RFC7521] Campbell, B., Mortimore, C., Jones, M., and Y. Goland, "Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants", RFC 7521

## Definitions and Abbreviations
- **JWT**: JSON Web Token, a JSON-based security token encoding enabling identity and security information to be shared across security domains.
- **Authorization Grant**: Intermediate credentials representing resource owner authorization, used by a client to obtain an access token.
- **Bearer Token**: A security token that the bearer can use to access protected resources.
- All other terms are as defined in [RFC6749], [RFC7521], and [JWT].

## 1. Introduction (Condensed)
JWTs enable identity and security information sharing across domains. This specification profiles the OAuth Assertion Framework [RFC7521] to define an extension grant type using a JWT Bearer Token for requesting an access token and for client authentication. It is similar to the SAML 2.0 Profile [RFC7522] but adapted for JWT semantics.

### 1.1. Notational Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119 [RFC2119].
- Unless otherwise noted, all protocol parameter names and values are case sensitive.

### 1.2. Terminology
All terms are as defined in [RFC6749], [RFC7521], and [JWT].

## 2. HTTP Parameter Bindings for Transporting Assertions
This section defines specific parameters and treatments for JWT Bearer Tokens, based on the framework in [RFC7521].

### 2.1. Using JWTs as Authorization Grants
- **grant_type** value: `urn:ietf:params:oauth:grant-type:jwt-bearer`
- **assertion** parameter: MUST contain a single JWT.
- **scope** parameter may be used as defined in [RFC7521].
- Authentication of the client is optional; `client_id` only needed when reliant client authentication is used.

### 2.2. Using JWTs for Client Authentication
- **client_assertion_type** value: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
- **client_assertion** parameter: Contains a single JWT. MUST NOT contain more than one JWT.

## 3. JWT Format and Processing Requirements
The authorization server MUST validate the JWT according to the criteria below. Additional restrictions and policy are at the discretion of the authorization server.

1. **iss (issuer)**: MUST contain a unique identifier for the entity that issued the JWT. In the absence of an application profile specifying otherwise, compliant applications MUST compare issuer values using the Simple String Comparison method defined in Section 6.2.1 of RFC 3986 [RFC3986].
2. **sub (subject)**: MUST identify the principal that is the subject of the JWT. Two cases:
   - A. For authorization grant: typically identifies the authorized accessor (resource owner or delegate), may be a pseudonymous identifier.
   - B. For client authentication: MUST be the `client_id` of the OAuth client.
3. **aud (audience)**: MUST contain a value identifying the authorization server as an intended audience. The token endpoint URL MAY be used. The authorization server MUST reject any JWT that does not contain its own identity as the intended audience. In the absence of an application profile specifying otherwise, compliant applications MUST compare the audience values using the Simple String Comparison method defined in Section 6.2.1 of RFC 3986 [RFC3986].
4. **exp (expiration time)**: MUST limit the time window. The authorization server MUST reject any JWT with an expiration time that has passed, subject to allowable clock skew. The server may reject JWTs with an `exp` value that is unreasonably far in the future.
5. **nbf (not before)**: MAY identify the time before which the token MUST NOT be accepted for processing.
6. **iat (issued at)**: MAY identify the time at which the JWT was issued. The server may reject JWTs with an `iat` value that is unreasonably far in the past.
7. **jti (JWT ID)**: MAY provide a unique identifier. The server MAY ensure JWTs are not replayed by maintaining the set of used `jti` values for the length of time the JWT would be considered valid based on the applicable `exp`.
8. The JWT MAY contain other claims.
9. The JWT MUST be digitally signed or have a MAC applied by the issuer. The server MUST reject JWTs with invalid signature or MAC.
10. The server MUST reject a JWT that is not valid in all other respects per [JWT].

### 3.1. Authorization Grant Processing
- JWT authorization grants may be used with or without client authentication or identification. Whether client authentication is needed is policy at the discretion of the server. However, if client credentials are present, the server MUST validate them.
- If the JWT is not valid or not within its validity time window, the server constructs an error response as defined in OAuth 2.0 [RFC6749] with `error` parameter `invalid_grant`. The server MAY include additional information using `error_description` or `error_uri`.

### 3.2. Client Authentication Processing
- If the client JWT is not valid, the server constructs an error response as defined in OAuth 2.0 [RFC6749] with `error` parameter `invalid_client`. The server MAY include additional information using `error_description` or `error_uri`.

## 4. Authorization Grant Example (Condensed)
An example JWT with `iss`, `sub`, `aud`, `nbf`, `exp`, and an additional claim, signed with ES256 using a key identified by `kid` "16". The corresponding HTTP request demonstrates how to present the JWT as an authorization grant.

## 5. Interoperability Considerations (Condensed)
Agreement on identifiers, keys, and endpoints (issuer, audience, token endpoint, signature key, one-time use, maximum lifetime, subject/claim requirements) is required. Such exchange is out of scope; additional profiles may constrain these values. The `RS256` algorithm [JWA] is mandatory-to-implement for this profile.

## 6. Security Considerations (Condensed)
All security considerations from [RFC7521], [RFC6749], and [JWT] apply. No mandatory replay protection is specified; implementations may employ it at their discretion.

## 7. Privacy Considerations (Condensed)
JWTs may contain sensitive information; should be transmitted over TLS. To prevent disclosure to clients, the JWT should be encrypted to the authorization server. Deployments should minimize claims; the `sub` claim can be anonymous or pseudonymous as per [RFC7521] Section 6.3.1.

## 8. IANA Considerations
### 8.1. Sub-Namespace Registration: `urn:ietf:params:oauth:grant-type:jwt-bearer`
- **URN**: `urn:ietf:params:oauth:grant-type:jwt-bearer`
- **Common Name**: JWT Bearer Token Grant Type Profile for OAuth 2.0
- **Change Controller**: IESG
- **Specification Document**: RFC 7523

### 8.2. Sub-Namespace Registration: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
- **URN**: `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`
- **Common Name**: JWT Bearer Token Profile for OAuth 2.0 Client Authentication
- **Change Controller**: IESG
- **Specification Document**: RFC 7523

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The value of the "grant_type" MUST be "urn:ietf:params:oauth:grant-type:jwt-bearer" when using JWTs as authorization grants. | MUST | Section 2.1 |
| R2 | The value of the "assertion" parameter MUST contain a single JWT. | MUST | Section 2.1 |
| R3 | The value of the "client_assertion_type" MUST be "urn:ietf:params:oauth:client-assertion-type:jwt-bearer" when using JWTs for client authentication. | MUST | Section 2.2 |
| R4 | The value of the "client_assertion" parameter MUST contain a single JWT and MUST NOT contain more than one. | MUST | Section 2.2 |
| R5 | The JWT MUST contain an "iss" claim. Compliant applications MUST compare issuer values using Simple String Comparison per RFC 3986 sec 6.2.1 unless otherwise specified. | MUST | Section 3 requirement 1 |
| R6 | The JWT MUST contain a "sub" claim. For client authentication, the subject MUST be the "client_id". | MUST | Section 3 requirement 2 |
| R7 | The JWT MUST contain an "aud" claim that identifies the authorization server as intended audience. The authorization server MUST reject any JWT not containing its own identity as audience. Compliant applications MUST compare audience values using Simple String Comparison per RFC 3986 sec 6.2.1 unless otherwise specified. | MUST | Section 3 requirement 3 |
| R8 | The JWT MUST contain an "exp" claim. The authorization server MUST reject any JWT with an expiration time that has passed. | MUST | Section 3 requirement 4 |
| R9 | The JWT MUST be digitally signed or have a MAC applied by the issuer. The authorization server MUST reject JWTs with an invalid signature or MAC. | MUST | Section 3 requirement 9 |
| R10 | The authorization server MUST reject a JWT that is not valid in all other respects per [JWT]. | MUST | Section 3 requirement 10 |
| R11 | If client credentials are present in the request, the authorization server MUST validate them. | MUST | Section 3.1 |
| R12 | If the JWT is not valid for an authorization grant, the authorization server MUST use the "invalid_grant" error code. | MUST | Section 3.1 |
| R13 | If the client JWT is not valid for client authentication, the authorization server MUST use the "invalid_client" error code. | MUST | Section 3.2 |
| R14 | The authorization server MAY reject JWTs with an "exp" value unreasonably far in the future. | MAY | Section 3 requirement 4 |
| R15 | The authorization server MAY reject JWTs with an "iat" value unreasonably far in the past. | MAY | Section 3 requirement 6 |
| R16 | The authorization server MAY ensure that JWTs are not replayed by maintaining the set of used "jti" values. | MAY | Section 3 requirement 7 |
| R17 | The "RS256" algorithm is mandatory-to-implement for this profile. | MUST (implement) | Section 5 |
| R18 | The JWT MAY contain an "nbf" claim. | MAY | Section 3 requirement 5 |
| R19 | The JWT MAY contain an "iat" claim. | MAY | Section 3 requirement 6 |
| R20 | The JWT MAY contain a "jti" claim. | MAY | Section 3 requirement 7 |
| R21 | The JWT MAY contain other claims. | MAY | Section 3 requirement 8 |