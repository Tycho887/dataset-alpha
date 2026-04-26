# OpenID Connect Core 1.0 incorporating errata set 2
**Source**: OpenID Foundation | **Version**: 1.0 | **Date**: December 15, 2023 | **Type**: Normative
**Original**: [https://openid.net/specs/openid-connect-core-1_0.html](https://openid.net/specs/openid-connect-core-1_0.html)

## Scope (Summary)
OpenID Connect 1.0 is an identity layer on top of OAuth 2.0 enabling Clients to verify End-User identity via authentication by an Authorization Server. This specification defines core authentication mechanisms, ID Token usage, Claims communication, and security/privacy considerations.

## Normative References
- [RFC6749]: The OAuth 2.0 Authorization Framework
- [RFC6750]: OAuth 2.0 Bearer Token Usage
- [JWT]: JSON Web Token (RFC7519)
- [JWS]: JSON Web Signature (RFC7515)
- [JWE]: JSON Web Encryption (RFC7516)
- [JWA]: JSON Web Algorithms (RFC7518)
- [OAuth.Responses]: OAuth 2.0 Multiple Response Type Encoding Practices
- [OpenID.Discovery]: OpenID Connect Discovery 1.0
- [OpenID.Registration]: OpenID Connect Dynamic Client Registration 1.0
- [RFC2119]: Key words for use in RFCs to Indicate Requirement Levels
- [RFC3986]: URI Generic Syntax
- [RFC5646]: Tags for Identifying Languages
- [RFC6125]: Representation and Verification of Domain-Based Application Service Identity within PKIX
- [RFC6819]: OAuth 2.0 Threat Model and Security Considerations
- [RFC8259]: JSON Data Interchange Format
- [RFC9325]: Recommendations for Secure Use of TLS
- (Full list in original document)

## Definitions and Abbreviations
- **Authentication**: Process to achieve sufficient confidence in binding between Entity and presented Identity.
- **Authentication Request**: OAuth 2.0 Authorization Request using OpenID Connect parameters to request End-User authentication.
- **Authorization Code Flow**: OAuth 2.0 flow where Authorization Code is returned from Authorization Endpoint, all tokens from Token Endpoint.
- **Claim**: Piece of information asserted about an Entity.
- **Claim Type**: Syntax for representing a Claim Value (Normal, Aggregated, Distributed).
- **End-User**: Human participant.
- **Hybrid Flow**: OAuth 2.0 flow where Authorization Code and some tokens from Authorization Endpoint, others from Token Endpoint.
- **ID Token**: JWT containing Claims about Authentication event.
- **Implicit Flow**: OAuth 2.0 flow where all tokens from Authorization Endpoint, no Token Endpoint or Authorization Code.
- **Issuer Identifier**: Case-sensitive URL using https scheme identifying the Issuer.
- **OpenID Provider (OP)**: OAuth 2.0 Authorization Server capable of authenticating End-User and providing Claims.
- **Relying Party (RP)**: OAuth 2.0 Client requiring End-User Authentication and Claims.
- **Subject Identifier**: Locally unique and never reassigned identifier for End-User within Issuer.
- **UserInfo Endpoint**: Protected Resource returning authorized Claims about End-User when presented with Access Token.
- (Additional terms in original Section 1.2)

## 1. Introduction
OpenID Connect is an identity layer on OAuth 2.0 (RFC6749). It enables Clients to verify End-User identity based on authentication by an Authorization Server, and to obtain basic profile information. This specification defines core functionality: authentication over OAuth 2.0 and use of Claims. Background references OAuth 2.0 and Bearer Token Usage. OAuth 2.0 Clients using OpenID Connect are Relying Parties (RPs); OAuth 2.0 Authorization Servers implementing OpenID Connect are OpenID Providers (OPs). Configuration information normally obtained via Discovery; credentials via Dynamic Registration.

### 1.1 Requirements Notation and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119. All uses of JWS and JWE utilize Compact Serialization; JSON Serialization is not used.

## 2. ID Token
The ID Token is a JWT containing Claims about Authentication. It includes the following Claims:
- `iss` (REQUIRED): Issuer Identifier. Case-sensitive URL using https scheme.
- `sub` (REQUIRED): Subject Identifier. Locally unique and never reassigned within Issuer. MUST NOT exceed 255 ASCII characters. Case-sensitive string.
- `aud` (REQUIRED): Audience(s). MUST contain the client_id of the RP as an audience value. May be array or single string.
- `exp` (REQUIRED): Expiration time on or after which ID Token MUST NOT be accepted. Current date/time MUST be before expiration.
- `iat` (REQUIRED): Time at which JWT was issued.
- `auth_time`: Time of End-User authentication. REQUIRED when `max_age` is requested or `auth_time` requested as Essential Claim.
- `nonce`: String value to associate Client session with ID Token, mitigate replay attacks. If present in Authentication Request, Authorization Servers MUST include nonce Claim with same value. Clients MUST verify nonce Claim equals sent value.
- `acr` (OPTIONAL): Authentication Context Class Reference. "0" indicates no confidence meeting ISO/IEC 29115 level 1.
- `amr` (OPTIONAL): Authentication Methods References. Array of strings.
- `azp` (OPTIONAL): Authorized party. If present, MUST contain OAuth 2.0 Client ID of this party.

ID Tokens MUST be signed using JWS, optionally signed then encrypted (Nested JWT). MUST NOT use `none` as `alg` unless Response Type returns no ID Token from Authorization Endpoint and Client explicitly requested `none` at Registration. SHOULD NOT use `x5u`, `x5c`, `jku`, or `jwk` Header Parameters; keys communicated via Discovery and Registration.

## 3. Authentication
OpenID Connect performs authentication; result returned in ID Token. Three flows: Authorization Code Flow (response_type=code), Implicit Flow (response_type=id_token or id_token token), Hybrid Flow (other response_type values from OAuth.Responses). Flow determined by `response_type`.

### 3.1 Authorization Code Flow
All tokens from Token Endpoint. Suitable for Clients that securely maintain Client Secret.

#### 3.1.1 Steps
1. Client prepares Authentication Request.
2. Client sends request to Authorization Server.
3. Authorization Server Authenticates End-User.
4. Authorization Server obtains End-User Consent/Authorization.
5. Authorization Server sends End-User back to Client with Authorization Code.
6. Client requests response using Authorization Code at Token Endpoint.
7. Client receives ID Token and Access Token.
8. Client validates ID Token and retrieves Subject Identifier.

#### 3.1.2 Authorization Endpoint
Communication MUST utilize TLS. Supports HTTP GET and POST.

##### 3.1.2.1 Authentication Request
Parameters:
- `scope` (REQUIRED): MUST contain `openid` scope value.
- `response_type` (REQUIRED): `code` for this flow.
- `client_id` (REQUIRED): OAuth 2.0 Client Identifier.
- `redirect_uri` (REQUIRED): MUST exactly match one of pre-registered Redirection URIs (RFC3986 section 6.2.1 simple string comparison). SHOULD use https scheme; may use http for confidential clients or native apps with localhost/127.0.0.1/[::1].
- `state` (RECOMMENDED): Opaque value for CSRF mitigation.
- `response_mode` (OPTIONAL): NOT RECOMMENDED when default mode.
- `nonce` (OPTIONAL): String value to associate Client session with ID Token. MUST have sufficient entropy.
- `display` (OPTIONAL): `page`, `popup`, `touch`, `wap`.
- `prompt` (OPTIONAL): `none`, `login`, `consent`, `select_account`. Space-delimited list.
- `max_age` (OPTIONAL): Maximum Authentication Age in seconds. If elapsed time greater, OP MUST re-authenticate. If used, ID Token MUST include `auth_time`.
- `ui_locales` (OPTIONAL): Preferred languages (BCP47).
- `id_token_hint` (OPTIONAL): Previously issued ID Token as hint.
- `login_hint` (OPTIONAL): Hint about login identifier.
- `acr_values` (OPTIONAL): Requested Authentication Context Class Reference values.

##### 3.1.2.2 Authentication Request Validation
Authorization Server MUST validate OAuth 2.0 parameters, verify `scope` includes `openid`, verify REQUIRED parameters. If `sub` requested with specific value, only send positive response if End-User identified by that `sub` has active session or is authenticated. MUST NOT reply with ID Token or Access Token for different user.

##### 3.1.2.3 Authorization Server Authenticates End-User
Attempts to Authenticate or determine if already authenticated. MUST attempt to authenticate if not already authenticated, or if `prompt=login`. MUST NOT interact with End-User if `prompt=none`; return error if not already authenticated.

##### 3.1.2.4 Authorization Server Obtains End-User Consent/Authorization
MUST obtain authorization decision before releasing information.

##### 3.1.2.5 Successful Authentication Response
Returns Authorization Code as query parameter in redirect_uri.

##### 3.1.2.6 Authentication Error Response
Error codes include `interaction_required`, `login_required`, `account_selection_required`, `consent_required`, `invalid_request_uri`, `invalid_request_object`, `request_not_supported`, `request_uri_not_supported`, `registration_not_supported`.

#### 3.1.3 Token Endpoint
Communication MUST utilize TLS.

##### 3.1.3.1 Token Request
Uses grant_type=authorization_code. Confidential clients MUST authenticate.

##### 3.1.3.2 Token Request Validation
Authorization Server MUST authenticate client, ensure code issued to authenticated client, verify code valid and not previously used, ensure redirect_uri parameter identical to initial request, verify code issued in response to OpenID Connect Authentication Request.

##### 3.1.3.3 Successful Token Response
Includes `id_token` (REQUIRED). `token_type` MUST be `Bearer`. Response MUST include Cache-Control: no-store.

##### 3.1.3.7 ID Token Validation
- If encrypted, decrypt using keys specified during Registration.
- Issuer Identifier MUST exactly match `iss` Claim.
- Client MUST validate `aud` contains its client_id.
- If `azp` present, client SHOULD verify its client_id is Claim Value.
- If received via direct communication (TLS), TLS server validation MAY be used to validate issuer in place of signature. For other ID Tokens, MUST validate signature using JWS with algorithm specified in JWT `alg` Header Parameter. SHOULD use default RS256.
- For MAC-based algorithms, use octets of UTF-8 representation of `client_secret` as key.
- Current time MUST be before `exp`.
- If nonce was sent, `nonce` Claim MUST be present and checked.
- If `acr` requested, client SHOULD check asserted value.
- If `auth_time` requested, client SHOULD check and request re-authentication if too much time elapsed.

### 3.2 Implicit Flow
All tokens from Authorization Endpoint; no Token Endpoint.

#### 3.2.1 Steps
1. Client prepares Authentication Request.
2. Client sends request to Authorization Server.
3. Authorization Server Authenticates End-User.
4. Authorization Server obtains Consent/Authorization.
5. Authorization Server sends End-User back to Client with ID Token and optionally Access Token.
6. Client validates ID Token.

#### 3.2.2.1 Authentication Request
`response_type` is `id_token token` or `id_token`. `redirect_uri` MUST NOT use http unless native app with localhost/127.0.0.1/[::1]. `nonce` is REQUIRED.

#### 3.2.2.5 Successful Authentication Response
Parameters returned in fragment component of Redirection URI unless different Response Mode. Includes `access_token` (if not `id_token` only), `token_type` (MUST be Bearer), `id_token` (REQUIRED), `state` (REQUIRED if sent), `expires_in` (OPTIONAL).

#### 3.2.2.11 ID Token Validation
Signature MUST be validated. Nonce MUST be checked. Client SHOULD check nonce for replay attacks.

### 3.3 Hybrid Flow
Some tokens from Authorization Endpoint, others from Token Endpoint.

#### 3.3.1 Steps
Similar to Authorization Code Flow but includes parameters from Authorization Endpoint.

#### 3.3.2.1 Authentication Request
`response_type` is `code id_token`, `code token`, or `code id_token token`. `nonce` REQUIRED for `code id_token` or `code id_token token`, OPTIONAL for `code token`.

#### 3.3.2.11 ID Token (Authorization Endpoint)
When nonce present, MUST include nonce. `at_hash` REQUIRED for `code id_token token`, OPTIONAL otherwise. `c_hash` REQUIRED for `code id_token` and `code id_token token`.

#### 3.3.3.6 ID Token (Token Endpoint)
If ID Token returned from both endpoints, `iss` and `sub` MUST be identical. Claims about Authentication event SHOULD be present in both. `at_hash` and `c_hash` MAY be omitted from Token Endpoint ID Token.

## 4. Initiating Login from a Third Party
Third party redirects to RP's login initiation endpoint with `iss` (REQUIRED, https URL) and optionally `login_hint`, `target_link_uri`. RP MUST verify `target_link_uri` to prevent open redirector. Clients SHOULD employ frame busting to prevent clickjacking.

## 5. Claims

### 5.1 Standard Claims
Defines standard Claims including `sub`, `name`, `given_name`, `family_name`, `email`, `email_verified`, `phone_number`, `address`, etc. (See Table 1 in original.)

### 5.1.1 Address Claim
JSON structure with `formatted`, `street_address`, `locality`, `region`, `postal_code`, `country`.

### 5.3 UserInfo Endpoint
Protected Resource returning Claims about authenticated End-User. Communication MUST use TLS. MUST support HTTP GET and POST. MUST accept Access Tokens as Bearer Token. SHOULD support CORS.

#### 5.3.1 UserInfo Request
Access Token sent as Bearer Token, RECOMMENDED to use Authorization header.

#### 5.3.2 Successful UserInfo Response
Claims returned as JSON object. `sub` MUST always be returned. `sub` in UserInfo Response MUST exactly match `sub` in ID Token; if not, UserInfo Response MUST NOT be used. Response MUST use JSON Serialization unless different format specified. Content-type `application/json` if plain JSON; `application/jwt` if signed/encrypted. If signed, MUST contain `iss` and `aud` Claims.

#### 5.3.4 UserInfo Response Validation
Client MUST verify intended OP via TLS server certificate check. If signed, SHOULD validate signature.

### 5.4 Requesting Claims using Scope Values
Scope values `profile`, `email`, `address`, `phone` request corresponding sets of Claims. Claims returned from UserInfo Endpoint if Access Token issued; otherwise in ID Token.

### 5.5 Requesting Claims using the "claims" Request Parameter
Optional parameter. JSON object with `userinfo` and/or `id_token` members. Claims can be requested as Essential (`essential: true`) with specific `value` or `values`. If supported, Authorization Server MUST return matching `acr` when requested as Essential.

### 5.6 Claim Types
- Normal Claims: Directly asserted by OP.
- Aggregated Claims: Asserted by another Claims Provider, returned by OP (OPTIONAL).
- Distributed Claims: Returned as references (OPTIONAL).

### 5.7 Claim Stability and Uniqueness
Only `sub` and `iss` from ID Token together guarantee stable identifier. Other Claims MUST NOT be used as unique identifiers.

## 6. Passing Request Parameters as JWTs
`request` and `request_uri` parameters allow signed/encrypted requests. Support is OPTIONAL; OP returns error if not supported.

### 6.1 Request Object by Value
JWT containing request parameters. If signed, SHOULD contain `iss` and `aud`. May be encrypted. `response_type` and `client_id` MUST be passed also as OAuth 2.0 parameters. `scope` MUST always include `openid`.

### 6.2 Request Object by Reference
`request_uri` URL referencing a JWT. URL MUST use https unless signed verifiably. Servers MAY cache. SHA-256 hash of contents SHOULD be included as fragment. Entire URI SHOULD NOT exceed 512 ASCII characters.

### 6.3 Validating JWT-Based Requests
Additional validation steps: decrypt if encrypted, validate signature, assemble parameters.

## 7. Self-Issued OpenID Provider
Self-Issued OPs use Issuer Identifier `https://self-issued.me`. No dynamic registration needed.

### 7.1 Discovery
Static discovery: authorization_endpoint `openid:`, response_types `["id_token"]`, subject_types `["pairwise"]`, ID Token signing algorithms `["RS256"]`.

### 7.2 Registration
Client uses `redirect_uri` as client_id.

#### 7.2.1 Registration Request Parameter
`registration` parameter provides client metadata (e.g., `policy_uri`, `tos_uri`, `logo_uri`).

### 7.3 Self-Issued OP Request
Authorization Endpoint URI is `openid:`. `response_type` must be `id_token`. Client_id is redirect_uri. Entire URL MUST NOT exceed 2048 ASCII characters.

### 7.4 Self-Issued OP Response
Contains `sub_jwk` (REQUIRED) – public key in JWK format. `iss` is `https://self-issued.me`. `sub` is base64url-encoded thumbprint of `sub_jwk` key.

### 7.5 Self-Issued ID Token Validation
- `iss` must be `https://self-issued.me`.
- `aud` must contain redirect_uri.
- Signature validated with key from `sub_jwk`.
- `sub` must be thumbprint of `sub_jwk`.
- `nonce` must match.

## 8. Subject Identifier Types
Two types: `public` (same `sub` to all Clients) and `pairwise` (different `sub` per Client to prevent correlation). OP lists supported types in Discovery.

### 8.1 Pairwise Identifier Algorithm
OP calculates unique `sub` per Sector Identifier using deterministic algorithm (e.g., SHA-256(sector_identifier || local_account_id || salt)). If `sector_identifier_uri` provided, host component of that URL is Sector Identifier.

## 9. Client Authentication
Methods: `client_secret_basic`, `client_secret_post`, `client_secret_jwt`, `private_key_jwt`, `none`. Default is `client_secret_basic`. For JWT methods, JWT must contain `iss`, `sub`, `aud`, `jti`, `exp`.

## 10. Signatures and Encryption
ID Token, UserInfo Response, Request Object, Client Authentication JWT can be signed and/or encrypted. When both, MUST sign then encrypt (Nested JWT).

### 10.1 Signing
Asymmetric: algorithm from JWA; private key associated with public key in sender's JWK Set. Symmetric: MAC algorithm uses `client_secret` as key; MUST NOT be used by public Clients.

#### 10.1.1 Rotation of Asymmetric Signing Keys
Signer publishes keys in JWK Set, uses `kid` in JOSE Header. Verifier re-retrieves JWK Set when unfamiliar `kid` encountered. Retain decommissioned keys for reasonable period.

### 10.2 Encryption
Asymmetric RSA or EC uses recipient's public key. Symmetric encryption derived from `client_secret`; MUST NOT be used by public Clients.

#### 10.2.1 Rotation of Asymmetric Encryption Keys
Recipient publishes new keys at `jwks_uri`, removes decommissioned. Cache-Control header aids transition.

## 11. Offline Access
Scope `offline_access` requests Refresh Token for offline access. `prompt=consent` MUST be used unless other conditions permit. OP MUST always obtain consent for offline access. MUST ignore `offline_access` if response_type does not return Authorization Code.

## 12. Using Refresh Tokens
Client authenticates to Token Endpoint. Successful response may include ID Token with same `iss`, `sub`, `aud`, and `auth_time` as original. SHOULD NOT have `nonce`. If ID Token returned, `iat` represents issue time.

## 13. Serializations
Three methods: Query String (GET), Form (POST), JSON (response bodies).

## 14. String Operations
Comparisons of JSON strings MUST be Unicode code point equality comparison, no normalization.

## 15. Implementation Considerations

### 15.1 Mandatory for All OPs
- Signing ID Tokens with RS256 (unless only Token Endpoint and `none` allowed).
- Support `prompt`, `display`, `ui_locales`, `claims_locales` (at least no error), `auth_time`, `max_age`, `acr_values` (at least no error).

### 15.2 Mandatory for Dynamic OPs
- Support `id_token` Response Type; if not Self-Issued also `code` and `id_token token`.
- Support Discovery, Dynamic Registration, UserInfo Endpoint (if issuing Access Tokens).
- Publish public keys as bare JWK.
- Support `request_uri`.

### 15.3 Discovery and Registration
If supporting unanticipated interactions, SHOULD implement Discovery and Dynamic Registration.

### 15.4 Mandatory for RPs
Features described as REQUIRED or MUST are mandatory when used. OPTIONAL features need not be used.

### 15.5 Implementation Notes
- Authorization Code may encode state.
- Nonce should include per-session state, unguessable.
- For Implicit/Hybrid, URI fragment handling: JavaScript parses fragment and POSTs to server.

## 16. Security Considerations
- TLS mandatory.
- Tokens should be signed to prevent modification.
- Access Tokens should be audience and scope restricted.
- Validate signatures, avoid timing attacks.
- Implicit Flow threats: Access Token in fragment, protected between OP and User Agent, but could be captured in infected User Agent.
- Use of nonce prevents replay.
- HTTP 307 redirects MUST NOT be used for Redirection URI; HTTP 303 preferred.
- Custom URI schemes on iOS: multiple apps can register; no fool-proof mitigation.

## 17. Privacy Considerations
- End-User consent for PII release should be obtained.
- Data access monitoring SHOULD be provided.
- Pairwise pseudonymous identifiers SHOULD be considered to prevent correlation.
- Offline access requires explicit consent.

## 18. IANA Considerations
Registers Claims, OAuth parameters, error codes, and the `openid` URI scheme (see original for details).

## 19. References
Normative and informative references as listed.

## Informative Annexes (Condensed)
- **Appendix A – Authorization Examples**: Shows non-normative examples for each `response_type` value (`code`, `id_token`, `id_token token`, `code id_token`, `code token`, `code id_token token`) with corresponding requests and ID Token contents. Includes RSA key used for validation.
- **Appendix B – Acknowledgements**: Lists contributors to the specification.
- **Appendix C – Notices**: Copyright and license information from OpenID Foundation.

## Requirements Summary (Key Normative Requirements)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | ID Token `iss` MUST be case-sensitive URL using https scheme | shall | Section 2 |
| R2 | ID Token `sub` MUST NOT exceed 255 ASCII characters | shall | Section 2 |
| R3 | ID Token `aud` MUST contain OAuth 2.0 client_id of RP | shall | Section 2 |
| R4 | ID Token `exp` – current date/time MUST be before expiration | shall | Section 2 |
| R5 | Authorization Request `scope` MUST contain `openid` | shall | 3.1.2.1 |
| R6 | Communication with Authorization Endpoint MUST utilize TLS | shall | 3.1.2 |
| R7 | Authorization Server MUST authenticate Client if issued Client Credentials | shall | 3.1.3.2 |
| R8 | ID Token MUST be signed using JWS (unless specific exceptions) | shall | Section 2 |
| R9 | Client MUST validate ID Token signature using keys provided by Issuer | shall | 3.1.3.7 |
| R10 | UserInfo Response `sub` MUST match ID Token `sub` | shall | 5.3.2 |
| R11 | self-issued ID Token `iss` MUST be `https://self-issued.me` | shall | 7.5 |
| R12 | Pairwise Subject Identifier algorithm MUST be deterministic and not reversible | shall | 8.1 |
| R13 | TLS server certificate check MUST be performed | shall | 16.17 |
| R14 | HTTP 307 redirects MUST NOT be used for Redirection URI | shall | 16.22 |
| R15 | Offline access request MUST include `prompt=consent` unless other conditions | shall | 11 |

(Note: This table is not exhaustive; all normative statements in the specification must be followed.)