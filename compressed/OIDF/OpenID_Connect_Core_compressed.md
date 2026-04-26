# Final: OpenID Connect Core 1.0 incorporating errata set 2
**Source**: OpenID Foundation | **Version**: 1.0 with errata set 2 | **Date**: December 15, 2023 | **Type**: Normative  
**Original**: [https://openid.net/specs/openid-connect-core-1_0.html](https://openid.net/specs/openid-connect-core-1_0.html)

## Scope (Summary)
Defines core OpenID Connect functionality: authentication on top of OAuth 2.0 and communication of End-User information via Claims. Covers three flows (Authorization Code, Implicit, Hybrid), ID Token structure, Claims, request objects, Self-Issued OPs, and security/privacy considerations.

## Normative References
- OAuth 2.0 [RFC6749]
- OAuth 2.0 Bearer Token Usage [RFC6750]
- JSON Web Token (JWT) [JWT]
- JSON Web Signature (JWS) [JWS]
- JSON Web Encryption (JWE) [JWE]
- JSON Web Algorithms (JWA) [JWA]
- OAuth 2.0 Multiple Response Type Encoding Practices [OAuth.Responses]
- OpenID Connect Discovery 1.0 [OpenID.Discovery]
- OpenID Connect Dynamic Client Registration 1.0 [OpenID.Registration]
- RFC 2119 (key words), RFC 3986 (URI), RFC 5646 (language tags), RFC 6125 (TLS), RFC 6749, RFC 6750, RFC 6819 (threat model), RFC 8176 (AMR), RFC 8259 (JSON), RFC 8996/9325 (TLS), ISO 29115

## Definitions and Abbreviations
- **Authentication**: Process to achieve confidence in binding between Entity and Identity.
- **Authentication Request**: OAuth 2.0 Authorization Request using OpenID Connect extension parameters and scopes.
- **Authorization Code Flow**: OAuth 2.0 flow with Authorization Code from Authorization Endpoint, tokens from Token Endpoint.
- **Implicit Flow**: All tokens returned from Authorization Endpoint; Token Endpoint not used.
- **Hybrid Flow**: Authorization Code from Authorization Endpoint; some tokens from Authorization Endpoint, others from Token Endpoint.
- **ID Token**: JWT containing Claims about the Authentication event.
- **OpenID Provider (OP)**: Authorization Server capable of authenticating End-User and providing Claims.
- **Relying Party (RP)**: OAuth 2.0 Client requiring End-User Authentication and Claims.
- **Claim**: Piece of information asserted about an Entity.
- **Subject Identifier (sub)**: Locally unique and never reassigned identifier within the Issuer for the End-User.
- **Request Object**: JWT containing request parameters.
- **Request URI**: URL referencing a resource containing a Request Object.
- **Self-Issued OpenID Provider**: Personal, self-hosted OP issuing self-signed ID Tokens.
- **UserInfo Endpoint**: Protected Resource returning Claims about authenticated End-User.

## 1. Introduction
OpenID Connect 1.0 is a simple identity layer on top of OAuth 2.0. It enables Clients to verify End-User identity based on authentication performed by an Authorization Server and to obtain basic profile information. Implements authentication as an extension to OAuth 2.0 authorization by including the `openid` scope value. OPs and RPs correspond to OAuth 2.0 Authorization Servers and Clients respectively.

### 1.1. Requirements Notation and Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.
- All uses of JWS and JWE utilize the Compact Serialization; JSON Serializations are not used.

### 1.2. Terminology
[Definitions as listed above and cross-referenced to OAuth 2.0, JWT, JWS, etc. All capitalized terms in the specification reference these definitions.]

### 1.3. Overview
Protocol steps: RP sends Authentication Request to OP; OP authenticates End-User and obtains authorization; OP responds with ID Token and usually Access Token; RP requests UserInfo with Access Token; UserInfo Endpoint returns Claims.

## 2. ID Token
- **ID Token**: JWT containing Claims about the Authentication of an End-User.
- **Claims**: `iss` (REQUIRED, Issuer Identifier, https scheme), `sub` (REQUIRED, Subject Identifier, ≤255 ASCII chars, case-sensitive), `aud` (REQUIRED, audience, must contain RP's `client_id`), `exp` (REQUIRED, expiration time, MUST NOT be accepted after), `iat` (REQUIRED, issued at).
- `auth_time`: Time of authentication; REQUIRED when `max_age` requested or as Essential Claim; otherwise OPTIONAL.
- `nonce`: String to associate Client session with ID Token and mitigate replay attacks. If present in Request, OP MUST include `nonce` Claim with same value. Clients MUST verify equality.
- `acr`: OPTIONAL Authentication Context Class Reference. Value "0" indicates no confidence.
- `amr`: OPTIONAL Authentication Methods References (JSON array of strings).
- `azp`: OPTIONAL Authorized party, if present MUST contain OAuth 2.0 Client ID.
- ID Tokens MUST be signed using JWS; optionally signed then encrypted (Nested JWT). MUST NOT use `none` alg unless Authorization Code Flow and Client explicitly requested `none` at Registration. SHOULD NOT use `x5u`, `x5c`, `jku`, `jwk` Header Parameters; keys communicated via Discovery/Registration.

## 3. Authentication
Three flows: Authorization Code Flow (`response_type=code`), Implicit Flow (`response_type=id_token token` or `id_token`), Hybrid Flow (`code id_token`, `code token`, `code id_token token`).

### 3.1. Authorization Code Flow
All tokens returned from Token Endpoint. Steps: Prepare Authentication Request, send to Authorization Server, authenticate End-User, obtain consent, return Authorization Code, exchange at Token Endpoint for ID Token and Access Token.

#### 3.1.2. Authorization Endpoint
- Communication MUST utilize TLS.
- **Authentication Request**: Uses OAuth 2.0 parameters: `scope` (REQUIRED, must contain `openid`), `response_type` (REQUIRED, `code`), `client_id` (REQUIRED), `redirect_uri` (REQUIRED, MUST exactly match pre-registered URI, SHOULD use `https`), `state` (RECOMMENDED).
- OpenID Connect parameters: `nonce` (OPTIONAL, sufficient entropy), `display` (OPTIONAL, values: `page`, `popup`, `touch`, `wap`), `prompt` (OPTIONAL, values: `none`, `login`, `consent`, `select_account`; if `none` with any other error), `max_age` (OPTIONAL, if used ID Token MUST include `auth_time`), `ui_locales`, `id_token_hint`, `login_hint`, `acr_values`.
- **Validation**: MUST validate OAuth 2.0 parameters, verify `scope` contains `openid`, verify REQUIRED parameters, if `sub` requested with specific value only respond if identified End-User has active session or authenticated, `id_token_hint` issuer validated. SHOULD ignore unrecognized parameters.
- **Authentication**: MUST reauthenticate if `prompt=login`; MUST NOT interact if `prompt=none`; MUST employ CSRF/clickjacking protections.
- **Consent**: MUST obtain authorization decision; may be interactive or pre-established.
- **Successful Response**: Returns `code` and `state` as query parameters (unless different Response Mode).
- **Error Response**: Defined error codes: `interaction_required`, `login_required`, `account_selection_required`, `consent_required`, `invalid_request_uri`, `invalid_request_object`, `request_not_supported`, `request_uri_not_supported`, `registration_not_supported`. Error response parameters: `error` (REQUIRED), `error_description` (OPTIONAL), `error_uri` (OPTIONAL), `state` (REQUIRED if included).
- **Response Validation**: Client MUST validate per RFC 6749 sections 4.1.2 and 10.12.

#### 3.1.3. Token Endpoint
- Communication MUST utilize TLS.
- **Token Request**: Uses `grant_type=authorization_code`, confidential clients MUST authenticate per Section 9. Parameters sent via HTTP POST with Form Serialization.
- **Validation**: Authenticate client, ensure Authorization Code issued to authenticated client, verify code valid and not reused, `redirect_uri` identical to initial request, code issued in response to OpenID Connect request.
- **Successful Response**: Includes `access_token`, `token_type` (MUST be `Bearer` unless negotiated), `id_token` (REQUIRED). `Cache-Control: no-store` MUST be included.
- **Token Error Response**: Per Section 5.2 of OAuth 2.0, HTTP 400 with JSON body.
- **Response Validation**: Validate per RFC 6749, ID Token per 3.1.3.7, Access Token per 3.1.3.8.
- **ID Token (Auth Code Flow)**: Additional Claims: `at_hash` (OPTIONAL, Access Token hash).
- **ID Token Validation**: If encrypted, decrypt using keys specified at Registration. Issuer MUST match OP's Issuer Identifier. `aud` MUST contain RP's `client_id`. If ID Token received via direct communication, TLS server validation MAY validate issuer instead of signature. Signature MUST be verified using keys from OP. `alg` SHOULD default to `RS256` or algorithm sent in Registration. If MAC-based algorithm, key is UTF-8 of `client_secret`. Current time MUST be before `exp`. `iat` acceptable range client-specific. If nonce sent, `nonce` Claim MUST be present and match. `acr` and `auth_time` checks per client policy.
- **Access Token Validation**: If `at_hash` present, Client MAY validate as for Implicit Flow (Section 3.2.2.9).

### 3.2. Implicit Flow
All tokens from Authorization Endpoint; Token Endpoint not used. Steps: Prepare request, send, authenticate, consent, receive ID Token and optionally Access Token.

#### 3.2.2. Authorization Endpoint
- **Authentication Request**: As per Section 3.1.2.1 with `response_type` = `id_token token` or `id_token`. `redirect_uri` MUST NOT use `http` unless native app with localhost/loopback. `nonce` REQUIRED.
- **Validation**: Same as Authorization Code Flow (Section 3.1.2.2).
- **Authentication, Consent**: Same as Code Flow.
- **Successful Response**: Parameters added to fragment component. Returns `access_token` (unless `response_type=id_token`), `token_type` (MUST be `Bearer` unless negotiated), `id_token` (REQUIRED), `state` (REQUIRED if present in request), `expires_in` (OPTIONAL). No `code` returned.
- **Error Response**: Parameters returned in fragment component.
- **Fragment Handling**: Client must parse fragment encoded values and pass to processing logic.
- **Response Validation**: Verify per [OAuth.Responses] Section 5, RFC 6749 Sections 4.2.2 and 10.12, ID Token per 3.2.2.11, Access Token per 3.2.2.9 (if applicable).
- **Access Token Validation**: Hash ASCII of `access_token` with algorithm from ID Token JOSE Header; take leftmost half, base64url-encode; must match `at_hash`.
- **ID Token**: `nonce` REQUIRED. `at_hash` REQUIRED if `access_token` returned (i.e., `id_token token`); otherwise OPTIONAL.
- **ID Token Validation**: Validate signature per JWS using algorithm in JOSE Header. Verify `nonce` matches Authentication Request value. Check replay attacks.

### 3.3. Hybrid Flow
Some tokens from Authorization Endpoint, others from Token Endpoint.

#### 3.3.2. Authorization Endpoint
- **Authentication Request**: As per Section 3.1.2.1 with `response_type` = `code id_token`, `code token`, or `code id_token token`. `nonce` REQUIRED if `code id_token` or `code id_token token`; OPTIONAL for `code token`.
- **Validation, Authentication, Consent**: Same as Code Flow.
- **Successful Response**: As per Implicit Flow but `code` always returned. `access_token` returned when `code token` or `code id_token token`; `id_token` returned when `code id_token` or `code id_token token`.
- **Error Response**: Fragment component.
- **Fragment Handling**: Same as Implicit.
- **Response Validation**: Verify per [OAuth.Responses] Section 5, RFC 6749, ID Token per 3.3.2.12, Access Token per 3.3.2.9, Authorization Code per 3.3.2.10.
- **Access Token Validation**: Same as Implicit (3.2.2.9).
- **Authorization Code Validation**: Hash ASCII of `code` with algorithm from ID Token JOSE Header; compare to `c_hash` (if present).
- **ID Token (from Auth Endpoint)**: `nonce` MUST be included if `nonce` in request. `at_hash` REQUIRED if `access_token` returned (i.e., `code id_token token`); otherwise OPTIONAL. `c_hash` REQUIRED if `code` returned (i.e., `code id_token` or `code id_token token`); otherwise OPTIONAL.
- **ID Token Validation**: Same as Implicit (3.2.2.11).

#### 3.3.3. Token Endpoint
- **Token Request, Validation, Response, Error**: Same as Authorization Code Flow.
- **ID Token (from Token Endpoint)**: Same as from Auth Endpoint with these exceptions: `iss` and `sub` MUST be identical in both ID Tokens if both returned. All Authentication event Claims SHOULD be present in both. End-User Claims if present in both SHOULD have same values. `at_hash` and `c_hash` MAY be omitted.
- **ID Token Validation**: Same as Authorization Code Flow (3.1.3.7).
- **Access Token**: If returned from both endpoints, values MAY be same or different.
- **Access Token Validation**: Same as Authorization Code Flow (3.1.3.8).

## 4. Initiating Login from a Third Party
- RP supports `initiate_login_uri` Registration parameter. Initiator redirects to that URI with `iss` (REQUIRED, OP Issuer Identifier, https), `login_hint` (OPTIONAL), `target_link_uri` (OPTIONAL, RP MUST verify to prevent open redirect). Parameters can be GET or POST. Clients SHOULD use frame busting to prevent clickjacking.

## 5. Claims
### 5.1. Standard Claims
Table of Claims: `sub`, `name`, `given_name`, `family_name`, `middle_name`, `nickname`, `preferred_username`, `profile`, `picture`, `website`, `email`, `email_verified`, `gender`, `birthdate`, `zoneinfo`, `locale`, `phone_number`, `phone_number_verified`, `address`, `updated_at`. Each with type and description. `email` MUST conform to RFC 5322 addr-spec. `phone_number` RECOMMENDED to be E.164. `address` is JSON object per Section 5.1.1.

### 5.2. Claims Languages and Scripts
- Claim Names MAY include BCP47 language tags delimited by `#`. E.g., `family_name#ja-Kana-JP`. RECOMMENDED to use registered case. Case-insensitive interpretation of tags. `claims_locales` request parameter enables preferred languages. OPs SHOULD match requested locales.

### 5.3. UserInfo Endpoint
- Communication MUST utilize TLS. MUST support HTTP GET and POST. MUST accept Bearer Tokens per RFC 6750. SHOULD support CORS.

#### 5.3.1. UserInfo Request
- Access Token sent as Bearer Token (header field recommended).

#### 5.3.2. Successful UserInfo Response
- Claims returned as JSON object (unless signed/encrypted). `sub` MUST always be returned. `sub` in UserInfo MUST exactly match `sub` in ID Token; otherwise values MUST NOT be used. Content-Type SHOULD be `application/json`; if JWT, `application/jwt`. If signed and encrypted, MUST be signed then encrypted.

#### 5.3.3. UserInfo Error Response
- Per Section 3 of RFC 6750 (e.g., 401 with WWW-Authenticate).

#### 5.3.4. UserInfo Response Validation
- Verify OP via TLS certificate check per RFC 6125. Decrypt if encrypted. Validate signature if signed.

### 5.4. Requesting Claims using Scope Values
- Scopes: `profile`, `email`, `address`, `phone` – each requests specific set of standard Claims. Claims returned from UserInfo Endpoint when Access Token issued; if no Access Token (e.g., `id_token` response_type), returned in ID Token.

### 5.5. Requesting Claims using "claims" Parameter
- `claims` parameter: JSON object with `userinfo` and `id_token` members. Each member lists individual Claims with optional `essential` (boolean), `value`, `values`. Support OPTIONAL.

#### 5.5.1. Individual Claims Requests
- For each Claim: `null` – default (Voluntary); JSON Object with `essential` (false default), `value`, `values`. `sub` mismatch MUST cause authentication failure. `acr` requested as Essential with specific values: Authorization Server MUST return matching `acr` or treat as failed authentication.

#### 5.5.2. Languages and Scripts for Individual Claims
- Language tags in Claim Names as per Section 5.2.

### 5.6. Claim Types
- Normal (directly asserted, MUST support). Aggregated and Distributed (OPTIONAL, using `_claim_names` and `_claim_sources`).

### 5.7. Claim Stability and Uniqueness
- Only `sub` (together with `iss`) provides stable unique identifier. Other Claims (`email`, `phone_number`, etc.) MUST NOT be used as unique identifiers.

## 6. Passing Request Parameters as JWTs
- `request` parameter: Request Object (JWT containing request parameters). `request_uri` parameter: URL referencing Request Object. Both OPTIONAL; if one used, other MUST NOT be used. Support indicates OP capabilities.

### 6.1. Passing a Request Object by Value
- Request Object may be signed/unsigned/encrypted. If signed, SHOULD contain `iss` (Client ID) and `aud` (OP Issuer). If both signed and encrypted, MUST sign then encrypt. `request` and `request_uri` MUST NOT be inside Request Object. `response_type`, `client_id` MUST also be passed as OAuth 2.0 parameters and must match. `scope` must contain `openid` in OAuth 2.0 parameters.

### 6.2. Passing a Request Object by Reference
- `request_uri` URL MUST use `https` unless signed verifiably. Servers MAY cache; if contents change, URI SHOULD include SHA-256 hash fragment. Entire URI SHOULD NOT exceed 512 ASCII characters.

### 6.3. Validating JWT-Based Requests
- Encrypted Request Object: decrypt per JWE. Signed Request Object: validate signature against key for `client_id`. Assembly: parameters from Request Object take precedence over OAuth 2.0 parameters. Then validate per flow.

## 7. Self-Issued OpenID Provider
- Uses Issuer Identifier `https://self-issued.me`. Authorization Endpoint URI `openid:`. No dynamic registration; treat as if registered with `client_id` = `redirect_uri`.

### 7.3. Self-Issued OP Request
- `response_type` = `id_token`. `client_id` = `redirect_uri`. Entire URL ≤ 2048 ASCII characters.

### 7.4. Self-Issued OP Response
- `iss` = `https://self-issued.me`. `sub_jwk` (REQUIRED) contains public key in JWK format. `sub` = base64url of SHA-256 thumbprint of key. No Access Token; all Claims in ID Token.

### 7.5. Self-Issued ID Token Validation
- Validate `iss`, `aud` (must contain `redirect_uri`), signature using `sub_jwk` key, `sub` matches thumbprint. `exp`, `iat`, `nonce` checks.

## 8. Subject Identifier Types
- `public`: same `sub` for all Clients (default). `pairwise`: different `sub` per Client to prevent correlation. OP Discovery must list supported types. Client may indicate preferred via `subject_type` Registration.

### 8.1. Pairwise Identifier Algorithm
- MUST calculate unique `sub` per Sector Identifier. Value MUST NOT be reversible by any party other than OP. Algorithm must be deterministic. Uses `sector_identifier_uri` or host component of `redirect_uri`. Example methods: SHA-256(sector_identifier || local_account_id || salt), AES-128 encryption, or GUID store.

## 9. Client Authentication
- Methods: `client_secret_basic` (default), `client_secret_post`, `client_secret_jwt`, `private_key_jwt`, `none`. JWT-based methods require `iss`, `sub`, `aud`, `jti`, `exp` (REQUIRED); `iat` OPTIONAL. Sent as `client_assertion` with `client_assertion_type` = `urn:ietf:params:oauth:client-assertion-type:jwt-bearer`.

## 10. Signatures and Encryption
- ID Token, UserInfo Response, Request Object, Client Authentication JWT can be signed (JWS) and/or encrypted (JWE). If both, MUST sign then encrypt (Nested JWT). OP advertises supported algorithms in Discovery; RP declares via Registration.

### 10.1. Signing
- Asymmetric: `alg` per JWA, private key linked to public key in JWK Set. `kid` required if multiple keys. Symmetric: MAC key = UTF-8 of `client_secret`. Symmetric signatures MUST NOT be used by public Clients.

### 10.2. Encryption
- Asymmetric RSA/ECDH-ES: encrypt with recipient's public key. Symmetric: key derived from `client_secret` by truncating SHA-2 hash. Symmetric encryption MUST NOT be used by public Clients.

## 11. Offline Access
- `offline_access` scope requests Refresh Token for offline access. `prompt=consent` MUST be used unless other conditions. OP MUST ensure consent; MUST ignore request if response_type not returning Authorization Code; MUST ignore if Access Token transmitted through User Agent (Implicit/Hybrid). Always obtain consent for offline access.

## 12. Using Refresh Tokens
- Token Request with `grant_type=refresh_token`. Client MUST authenticate. Successful response may include new ID Token with same `iss`, `sub`, `aud`; `iat` new; `auth_time` original; SHOULD NOT have `nonce`; otherwise same rules.

## 13. Serializations
- Query String, Form, JSON. Described syntax; not all methods applicable for all messages.

## 14. String Operations
- Comparisons: remove JSON escaping, no Unicode normalization, code-point equality. Space-delimited lists: single ASCII space (0x20).

## 15. Implementation Considerations
### 15.1. Mandatory for All OPs
- Signing ID Tokens with RS256 (unless only Code Flow and `none` allowed). Support `prompt`, `display`, `ui_locales`, `claims_locales`, `auth_time` when requested, `max_age`, `acr_values`.

### 15.2. Mandatory for Dynamic OPs
- Support `id_token`, `code`, `id_token token` Response Types. Discovery, Dynamic Registration, UserInfo Endpoint (if issue Access Tokens), publish bare JWK keys, support `request_uri`.

### 15.3. Discovery and Registration
- Should implement Discovery and Dynamic Registration for unanticipated interactions.

### 15.4. Mandatory for RPs
- RP must implement features marked REQUIRED/MUST when used.

## 16. Security Considerations
- Summaries of threats: request disclosure, server masquerading, token manufacture/modification, access token disclosure, server response disclosure/repudiation, request repudiation, access token redirect, token reuse, authorization code eavesdropping, token substitution, timing attack, crypto attacks, signing/encryption order, issuer identifier handling, implicit flow threats, TLS requirements (MUST support, MUST use TLS with confidentiality/integrity, server certificate check per RFC 6125), lifetimes of tokens, symmetric key entropy, need for signed/encrypted requests, HTTP 307 redirects MUST NOT be used, custom URI schemes on iOS vulnerabilities.

## 17. Privacy Considerations
- PII handling, data access monitoring, correlation (use PPID), offline access consent.

## 18. IANA Considerations
- Registrations for JWT Claims (standard Claims, `azp`, `nonce`, `auth_time`, `at_hash`, `c_hash`, `acr`, `amr`, `sub_jwk`, `_claim_names`, `_claim_sources`), OAuth Parameters (various request/response parameters), OAuth Extensions Errors (defined error codes), URI Scheme `openid`.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | ID Token MUST be signed using JWS; MAY be signed then encrypted. | MUST | Section 2 |
| R2 | ID Token MUST NOT use `none` alg unless Authorization Code Flow and Client explicitly requested. | MUST | Section 2 |
| R3 | `iss` in ID Token MUST be case-sensitive URL using `https` scheme. | MUST | Section 2 |
| R4 | `sub` in ID Token MUST NOT exceed 255 ASCII characters. | MUST | Section 2 |
| R5 | `aud` in ID Token MUST contain RP's `client_id`. | MUST | Section 2 |
| R6 | Authorization Server MUST include `nonce` Claim in ID Token if nonce sent in request. | MUST | Section 2 |
| R7 | Client MUST verify `nonce` Claim equals value in Authentication Request. | MUST | Section 2 |
| R8 | Authentication Request MUST include `openid` scope value. | MUST | Section 3.1.2.1 |
| R9 | Communication with Authorization Endpoint MUST utilize TLS. | MUST | Section 3.1.2 |
| R10 | `redirect_uri` MUST exactly match pre-registered value (Simple String Comparison). | MUST | Section 3.1.2.1 |
| R11 | OP MUST validate all OAuth 2.0 parameters. | MUST | Section 3.1.2.2 |
| R12 | If `prompt=none`, OP MUST NOT display any UI; MUST return error if not already authenticated. | MUST | Section 3.1.2.3 |
| R13 | Successful Token Response MUST include `id_token`. | MUST | Section 3.1.3.3 |
| R14 | `token_type` in Token Response MUST be `Bearer` unless negotiated. | MUST | Section 3.1.3.3 |
| R15 | Token Response MUST include `Cache-Control: no-store`. | MUST | Section 3.1.3.3 |
| R16 | Client MUST validate ID Token signature using keys from OP. | MUST | Section 3.1.3.7 |
| R17 | Current time MUST be before `exp` in ID Token. | MUST | Section 3.1.3.7 |
| R18 | In Implicit Flow, `nonce` is REQUIRED in Authentication Request. | MUST | Section 3.2.2.1 |
| R19 | In Implicit Flow, `redirect_uri` MUST NOT use `http` unless native app with localhost/loopback. | MUST | Section 3.2.2.1 |
| R20 | Authorization Code returned in Hybrid Flow MUST be validated via `c_hash`. | SHOULD | Section 3.3.2.10 |
| R21 | `sub` in UserInfo Response MUST exactly match `sub` in ID Token; otherwise MUST NOT use UserInfo. | MUST | Section 5.3.2 |
| R22 | `sub` and `iss` are the only reliable stable identifiers. Other Claims MUST NOT be used as unique identifiers. | MUST | Section 5.7 |
| R23 | In Self-Issued OP, `iss` MUST be `https://self-issued.me`. | MUST | Section 7.5 |
| R24 | In Self-Issued OP, `sub` MUST be base64url of SHA-256 thumbprint of `sub_jwk` key. | MUST | Section 7.4 |
| R25 | Client authentication using `client_secret_jwt` or `private_key_jwt` MUST include `iss`, `sub`, `aud`, `jti`, `exp`. | MUST | Section 9 |
| R26 | Symmetric signing/encryption MUST NOT be used by public Clients. | MUST | Section 10.1, 10.2 |
| R27 | When both signing and encryption, MUST sign then encrypt (Nested JWT). | MUST | Section 10 |
| R28 | Offline access request MUST include `prompt=consent` unless other conditions. | MUST | Section 11 |
| R29 | Offline access MUST be ignored if Access Token transmitted through User Agent. | MUST | Section 11 |
| R30 | TLS MUST be used for all communications; server certificate check MUST be performed per RFC 6125. | MUST | Section 16.17 |
| R31 | HTTP 307 redirects MUST NOT be used for redirecting to Redirection URI. | MUST | Section 16.22 |
| R32 | Comparisons of JSON strings MUST NOT apply Unicode normalization; code-point equality. | MUST | Section 14 |

## Informative Annexes (Condensed)
- **Appendix A. Authorization Examples**: Non-normative examples of requests and responses for each `response_type` value, including decoded ID Token Claims and RSA key used. Illustrates protocol flow.
- **Appendix B. Acknowledgements**: Lists contributors to the specification, including those from OpenID Authentication 2.0 and additional individuals from various organizations.
- **Appendix C. Notices**: Copyright and licensing information from the OpenID Foundation; no warranty; intellectual property policy reference.