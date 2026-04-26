# openid-4-verifiable-credential-issuance-1_0: OpenID for Verifiable Credential Issuance 1.0
**Source**: OpenID Foundation Digital Credentials Protocols | **Version**: 1.0 (Final) | **Date**: 16 September 2025 | **Type**: Normative
**Original**: https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html (see also errata revision at openid-4-verifiable-credential-issuance-1_0)

## Scope (Summary)
This specification defines an OAuth 2.0 protected API for the issuance of Verifiable Credentials (VCs) of any format (e.g., SD-JWT VC, ISO mdoc, W3C VCDM). It extends OAuth 2.0 with a new grant type (Pre-Authorized Code), authorization details type `openid_credential`, and several new endpoints to support credential offer, batch issuance, deferred issuance, nonce, and notification. The API allows binding credentials to cryptographic keys and supports multiple proof types.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC6749] Hardt, D., "The OAuth 2.0 Authorization Framework", RFC 6749
- [RFC7515] Jones, M. et al., "JSON Web Signature (JWS)", RFC 7515
- [RFC7516] Jones, M. & Hildebrand, J., "JSON Web Encryption (JWE)", RFC 7516
- [RFC7519] Jones, M. et al., "JSON Web Token (JWT)", RFC 7519
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174
- [RFC8414] Jones, M. et al., "OAuth 2.0 Authorization Server Metadata", RFC 8414
- [RFC9396] Lodderstedt, T. et al., "OAuth 2.0 Rich Authorization Requests", RFC 9396
- [RFC9449] Fett, D. et al., "OAuth 2.0 Demonstrating Proof of Possession (DPoP)", RFC 9449
- [OpenID.Core] Sakimura, N. et al., "OpenID Connect Core 1.0"
- [I-D.ietf-oauth-sd-jwt-vc] Terbu, O. et al., "SD-JWT-based Verifiable Credentials (SD-JWT VC)", draft -11
- [ISO.18013-5] ISO/IEC 18013-5:2021, "Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application"
- [VC_DATA] Sporny, M. et al., "Verifiable Credentials Data Model 1.1"
- … (full list in §16 of original)

## Definitions and Abbreviations
- **Credential (Verifiable Credential)**: Instance of a Credential Configuration with a particular Credential Dataset, signed by an Issuer and cryptographically verifiable.
- **Credential Configuration**: Issuer's description of a particular kind of Credential, including format, metadata, and issuance parameters.
- **Credential Format**: Data model used to create and represent credential information (e.g., `jwt_vc_json`, `mso_mdoc`, `dc+sd-jwt`).
- **Credential Format Profile**: Set of parameters specific to a Credential Format.
- **Credential Issuer (Issuer)**: Entity that issues VCs; acts as OAuth 2.0 Resource Server and optionally as Authorization Server.
- **Holder**: Entity that receives and controls VCs for presentation.
- **Verifier**: Entity that requests, receives, and validates Presentations.
- **Wallet**: Entity used by Holder to manage VCs and keys; acts as OAuth 2.0 Client.
- **Cryptographic Holder Binding**: Proof of possession of private key corresponding to public key in credential.
- **Deferred Credential Issuance**: Issuance after a period, not directly in response to the credential request.
- **Pre-Authorized Code**: Code representing issuer's authorization for a Wallet to obtain Credentials (used in Pre-Authorized Code Flow).
- **Transaction Code (tx_code)**: Code sent via second channel to bind Pre-Authorized Code to a transaction.
- **c_nonce**: Fresh nonce value used in proofs for replay protection.

## Normative Sections

### 3. Overview
#### 3.1 Credential Issuer
- **Mandatory Endpoint**: Credential Endpoint (§8). Single request may issue one or more credentials of same format and dataset.
- **Optional Endpoints**: Nonce Endpoint (§7), Deferred Credential Endpoint (§9), Credential Offer (§4), Notification Endpoint (§11).
- **Metadata**: Published via `credential_configurations_supported` (§12.2.4).

#### 3.2 OAuth 2.0
- New Grant Type: `urn:ietf:params:oauth:grant-type:pre-authorized_code` (§4.1.1).
- New authorization details type: `openid_credential` (§5.1.1).
- New Client metadata: `credential_offer_endpoint` (§12.1).
- New Authorization request parameter: `issuer_state` (§5.1.3).

#### 3.3 Core Concepts
- Batch issuance: In a single request, issued credentials MUST share same Credential Format and Credential Dataset, but SHOULD contain different Cryptographic Data.
- To issue credentials of different formats/datasets, multiple requests MUST be sent.
- Identifying credentials throughout flow: see §3.3.4.

### 4. Credential Offer Endpoint
#### 4.1 Credential Offer
- Credential Offer object can be sent by value (`credential_offer`) or by reference (`credential_offer_uri`). Exactly one MUST be present.
- `credential_offer_uri` MUST be an HTTPS URL referencing a JSON object.
- For security considerations see §13.5.

#### 4.1.1 Credential Offer Parameters
- `credential_issuer`: REQUIRED. URL of Issuer.
- `credential_configuration_ids`: REQUIRED. Non-empty array of unique strings referencing `credential_configurations_supported` keys.
- `grants`: OPTIONAL. Object indicating supported grant types, each with parameters:
  - Grant `authorization_code`: optional `issuer_state`, optional `authorization_server`.
  - Grant `urn:ietf:params:oauth:grant-type:pre-authorized_code`: REQUIRED `pre-authorized_code` (short-lived, single-use), optional `tx_code` object.
- Additional parameters MAY be defined; unrecognized parameters MUST be ignored.
- `tx_code` sub-parameters: `input_mode` (numeric/text), `length`, `description` (≤300 chars).

### 5. Authorization Endpoint
- Use as per RFC6749. SHOULD follow BCP240.
- For `authorization_code` grant, RECOMMENDED to use PKCE and PAR.

#### 5.1 Authorization Request
- Two methods: `authorization_details` (type `openid_credential`) or `scope`.
- **Using authorization_details**: `type` REQUIRED set to `openid_credential`; `credential_configuration_id` REQUIRED; `claims` OPTIONAL.
- **Using scope**: scope values from `credential_configurations_supported` metadata. Unknown scope values MUST be ignored. If both `scope` and `authorization_details` request same credential, `authorization_details` takes precedence.
- `issuer_state`: OPTIONAL, used to pass state from Credential Offer.

#### 5.1.4 Pushed Authorization Request
- RECOMMENDED.

#### 5.2 Successful Authorization Response
- As per RFC6749.

#### 5.3 Authorization Error Response
- As per RFC6749.

### 6. Token Endpoint
#### 6.1 Token Request
- Extension parameters for Pre-Authorized Code Flow: `pre-authorized_code` (REQUIRED if grant type is `urn:ietf:params:oauth:grant-type:pre-authorized_code`), `tx_code` (OPTIONAL, but MUST be present if `tx_code` object was in Credential Offer).
- Client authentication: for Pre-Authorized Code Grant, authentication is OPTIONAL; `client_id` only needed if client authentication relies on it.
- If Token Request contains `authorization_details` with `openid_credential` and Issuer metadata has `authorization_servers`, the object MUST contain `locations` with the issuer identifier.
- When Pre-Authorized Grant is used, RECOMMENDED to issue an Access Token valid only for offered credentials.
- Unrecognized parameters MUST be ignored.

#### 6.1.1 Request Credential Issuance using authorization_details Parameter
- May be used in Token Request to request specific credential configuration in both flows.

#### 6.2 Successful Token Response
- Additional parameters: `authorization_details` (REQUIRED if used in Authorization or Token Request; OPTIONAL if scope used) – contains `credential_identifiers` (REQUIRED array of strings, each identifying a Credential Dataset).
- Unrecognized parameters MUST be ignored.

#### 6.3 Token Error Response
- Additional clarifications for `invalid_request`, `invalid_grant`, `invalid_client`.

### 7. Nonce Endpoint
- Credential Issuer that requires `c_nonce` MUST offer Nonce Endpoint.
- **Nonce Request**: HTTP POST to URL in `nonce_endpoint`. Unprotected resource.
- **Nonce Response**: 2xx with `c_nonce` (REQUIRED string, unpredictable). Response MUST be uncacheable (`Cache-Control: no-store`).

### 8. Credential Endpoint
- REQUIRED. Communication MUST use TLS.
- Issues one or more credentials of same Credential Configuration and Dataset.

#### 8.1 Binding the Issued Credential
- SHOULD be cryptographically bound to End-User identifier.
- Options: key binding via proof types (jwt, di_vp, attestation).

#### 8.2 Credential Request
- Parameters:
  - `credential_identifier`: REQUIRED if `authorization_details` returned from Token Response; MUST NOT be used with `credential_configuration_id`.
  - `credential_configuration_id`: REQUIRED if `credential_identifiers` not returned; MUST NOT be used with `credential_identifier`.
  - `proofs`: OPTIONAL object containing exactly one proof type parameter (array of proofs). MUST be present if `proof_types_supported` in Issuer metadata.
  - `credential_response_encryption`: OPTIONAL object with `jwk`, `enc`, `zip`.
- Proofs MUST incorporate Issuer Identifier (aud) and, if Nonce Endpoint present, `c_nonce` (nonce claim).
- Additional parameters MAY be defined; Issuer MUST ignore unrecognized.
- Encryption: see §10.

#### 8.3 Credential Response
- Immediate: HTTP 200 with `credentials` array (each object has `credential`).
- Deferred: HTTP 202 with `transaction_id` and `interval`.
- Notification: optional `notification_id`.
- Additional parameters MAY be defined; Wallet MUST ignore unrecognized.

#### 8.3.1 Credential Error Response
- For payload errors: use error codes `invalid_credential_request`, `unknown_credential_configuration`, `unknown_credential_identifier`, `invalid_proof`, `invalid_nonce`, `invalid_encryption_parameters`, `credential_request_denied`. These take precedence over `invalid_request`.

### 9. Deferred Credential Endpoint
- OPTIONAL. Must be accessed with valid Access Token.
- **Deferred Credential Request**: HTTP POST with `transaction_id` (REQUIRED), optional `credential_response_encryption`.
- Issuer MUST invalidate `transaction_id` after successful issuance.
- **Deferred Credential Response**: HTTP 200 with `credentials` or HTTP 202 with `transaction_id` and `interval`.
- **Error**: additional error code `invalid_transaction_id`.

### 10. Encrypted Credential Requests and Responses
- Message contents encoded as JWT (media type `application/jwt`).
- Public key selection based on `kty`, `use`, `alg`, etc. `alg` MUST be present; `kid` if available.
- If `zip` specified, compression before encryption.
- If encryption required and received unencrypted, SHOULD be rejected.

### 11. Notification Endpoint
- OPTIONAL. Wallet sends POST with `notification_id` and `event` (one of `credential_accepted`, `credential_failure`, `credential_deleted`). Optional `event_description`.
- Issuer responds with 2xx (204 RECOMMENDED).
- Errors: `invalid_notification_id`, `invalid_notification_request`.

### 12. Metadata
#### 12.1 Client Metadata
- New optional parameter: `credential_offer_endpoint`.
- Custom URL scheme: `openid-credential-offer://`.

#### 12.2 Credential Issuer Metadata
- **Credential Issuer Identifier**: case sensitive HTTPS URL.
- **Retrieval**: `/.well-known/openid-credential-issuer` path.
- Metadata can be unsigned (application/json) or signed JWT (application/jwt). Issuer MUST support unsigned.
- Signed metadata: `typ` = `openidvci-issuer-metadata+jwt`, `sub` REQUIRED, `iat` REQUIRED.
- Parameters: `credential_issuer` (REQUIRED), `authorization_servers` (OPTIONAL), `credential_endpoint` (REQUIRED), `nonce_endpoint` (OPTIONAL), `deferred_credential_endpoint` (OPTIONAL), `notification_endpoint` (OPTIONAL), `credential_request_encryption` (OPTIONAL), `credential_response_encryption` (OPTIONAL), `batch_credential_issuance` (OPTIONAL), `display` (OPTIONAL), `credential_configurations_supported` (REQUIRED).

#### 12.3 OAuth 2.0 Authorization Server Metadata
- New parameter: `pre-authorized_grant_anonymous_access_supported` (OPTIONAL boolean; default false).

### 13. Security Considerations
- Formal security analysis performed on previous revision.
- Implementers SHOULD follow BCP240 and RECOMMENDED to follow FAPI2 Security Profile where applicable.
- For native app Wallets, use Wallet Attestations (§E) instead of private_key_jwt or MTLS. Use DPoP for sender-constrained tokens.
- Key attestation and client authentication to establish trust between Wallet and Issuer.
- Split-architecture wallets: sensitive tokens MUST NOT be passed through untrusted server components.
- Credential Offer: Wallet MUST NOT trust parameter values; must perform same validation.
- Pre-Authorized Code replay prevention: Transaction Code recommended.
- Transaction Code phishing: Wallet RECOMMENDED to interact with trusted issuers only.
- Proof replay: `c_nonce` parameter is main defense. RECOMMENDED to use Nonce Endpoint.
- TLS: MUST follow BCP195; server certificate check per RFC6125.
- Long-lived Access Tokens (>5 min) MUST NOT be issued unless sender-constrained; Bearer tokens stored securely.
- Application-layer encryption: additional protection but does not mitigate access token theft.

### 14. Implementation Considerations
- Claims-based holder binding for non-cryptographic binding.
- Bearer credentials: allowed for low-assurance use cases.
- Multiple accesses to Credential Endpoint: Issuer may return same or updated credential; SHOULD NOT revoke previously issued credentials solely due to subsequent request.
- Binding between Credential Issuer Identifier and issuer identifier in credential: use Well-Known DID or `credential_issuer` claim.
- Refreshing: either using Refresh Token (Wallet-initiated) or re-issuance.
- Batch issuing: Issuer determines number of credentials.
- Pre-Final Specifications: implementers should use specific draft versions listed (OpenID Federation 1.0 -43, SD-JWT VC -11, Attestation-Based Client Auth -07, Token Status List -12) unless updated by profile.

### 15. Privacy Considerations
- Obtain End-User consent.
- Minimum disclosure: support selective disclosure or issue separate credentials per claim.
- Minimize storage of signed credentials; log carefully.
- Correlation: avoid unique values; randomize or round time-related information.
- Credential Offer: per RFC9101 privacy considerations.
- Authorization Request: avoid sensitive information in parameters.
- Wallet Attestation subject: SHOULD be shared across instances (not unique identifier).
- Identifying the Credential Issuer: use common issuer or group signature to avoid leakage.
- Identifying the Wallet: SHOULD require user interaction before fetching credential_offer_uri.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A Credential Issuer MUST support the Credential Endpoint. | shall | §8 |
| R2 | Credential Requests for different Credential Formats or Datasets MUST be sent via multiple requests. | shall | §3.3.2 |
| R3 | The `proofs` parameter MUST be present if `proof_types_supported` is present in Issuer metadata. | shall | §8.2 |
| R4 | The `c_nonce` value MUST be unpredictable. | shall | §7.2 |
| R5 | Pre-Authorized Code MUST be short-lived and single-use. | shall | §4.1.1 |
| R6 | If `tx_code` object present in Credential Offer, the Token Request MUST include `tx_code`. | shall | §6.1 |
| R7 | Unrecognized parameters in Credential Offer, Authorization Request, Token Request, Credential Response, Deferred Credential Response MUST be ignored. | shall | Multiple sections |
| R8 | Long-lived Access Tokens (>5 min) MUST NOT be issued unless sender-constrained. | shall | §13.10 |
| R9 | Communication with Credential Endpoint, Deferred Credential Endpoint, and Metadata retrieval MUST use TLS. | shall | §8, §9, §12.2.2 |
| R10 | Signed metadata JWT MUST NOT use `alg` `none` or symmetric algorithm. | shall | §12.2.3 |
| R11 | The `credential_issuer` metadata value MUST match the identifier used in the well-known path. | shall | §12.2.4 |
| R12 | The `credential_offer` and `credential_offer_uri` parameters MUST NOT both be present. | shall | §4.1 |
| R13 | Wallet MUST NOT accept credentials solely because of a Credential Offer; all protocol steps must be performed. | shall | §13.5 |
| R14 | Credential Issuers SHOULD support encryption of requests and responses when indicated. | should | §10 |
| R15 | It is RECOMMENDED to use PKCE and Pushed Authorization Requests for Authorization Code Flow. | should | §5 |
| R16 | DPoP is RECOMMENDED for sender-constrained access tokens. | should | §13.2 |

## Informative Annexes (Condensed)
- **Annex A (Credential Format Profiles)**: Defines format-specific parameters for `jwt_vc_json`, `ldp_vc`, `jwt_vc_json-ld`, `mso_mdoc`, and `dc+sd-jwt`. Each includes format identifier, metadata requirements, authorization details example, and credential response encoding.
- **Annex B (Claims Description)**: Defines structure for claims path pointers and display properties used in Authorization Details and Issuer Metadata. Processing rules handle repeated or contradictory descriptions.
- **Annex C (Claims Path Pointer)**: Specifies how to point to claims in JSON and ISO mdoc credentials using arrays of strings, nulls, and integers.
- **Annex D (Key Attestations)**: Defines JWT-based format for attesting cryptographic keys. Includes parameters `attested_keys`, `key_storage`, `user_authentication`, etc. Attack potential resistance levels from ISO 18045.
- **Annex E (Wallet Attestations in JWT format)**: Defines a client authentication mechanism for native app Wallets, based on OAuth Attestation-Based Client Authentication. Includes claims `wallet_name`, `wallet_link`, `status`.
- **Annex F (Proof Types)**: Defines `jwt`, `di_vp`, and `attestation` proof types. Each specifies required JOSE headers and JWT body claims (e.g., `typ`, `alg`, `kid`, `aud`, `nonce`). Verification checks listed.
- **Annex G (IANA Considerations)**: Registers new URIs, OAuth parameters, metadata parameters, well-known URI, and media types (`application/openid4vci-proof+jwt`, `application/key-attestation+jwt`, `application/openidvci-issuer-metadata+jwt`, URI scheme `openid-credential-offer`).
- **Annex H (Use Cases)**: Non-exhaustive examples: same-device credential offer, cross-device with pre-submitted info, cross-device deferred, wallet-initiated during presentation, wallet-initiated after installation.
- **Annex I (Additional Examples)**: Provides signed Credential Issuer Metadata JWT and signed Wallet Attestation JWT.
- **Annex J (Acknowledgements)**: Lists contributors.
- **Annex K (Notices)**: Copyright and license information for the OpenID Foundation.