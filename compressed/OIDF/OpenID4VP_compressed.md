# OpenID for Verifiable Presentations 1.0
**Source**: OpenID Foundation Digital Credentials Protocols Working Group | **Version**: 1.0 | **Date**: 9 July 2025 | **Type**: Final
**Original**: https://openid.net/specs/openid-4-verifiable-presentations-1_0.html

## Scope
This specification defines a protocol on top of OAuth 2.0 for requesting and presenting Verifiable Credentials and Presentations, supporting any credential format (e.g., W3C VCDM, ISO mdoc, SD-JWT VC). It introduces the `vp_token` response type, Digital Credentials Query Language (DCQL), and mechanisms for same-device and cross-device flows, including use with the Digital Credentials API.

## Normative References
- [RFC2119] – Key words for use in RFCs
- [RFC6749] – OAuth 2.0 Authorization Framework
- [RFC7515] – JSON Web Signature (JWS)
- [RFC7516] – JSON Web Encryption (JWE)
- [RFC7519] – JSON Web Token (JWT)
- [RFC7591] – OAuth 2.0 Dynamic Client Registration
- [RFC8414] – OAuth 2.0 Authorization Server Metadata
- [RFC9101] – JWT-Secured Authorization Request (JAR)
- [RFC9700] – Best Current Practice for OAuth 2.0 Security
- [OpenID.Core] – OpenID Connect Core 1.0
- [SIOPv2] – Self-Issued OpenID Provider V2
- [VC_DATA] – Verifiable Credentials Data Model 1.1
- [ISO.18013-5] – ISO mdoc
- [I-D.ietf-oauth-sd-jwt-vc] – SD-JWT VC
- [W3C.Digital_Credentials_API] – Digital Credentials API

## Definitions and Abbreviations
- **Verifiable Credential (VC)**: An Issuer-signed Credential whose authenticity can be cryptographically verified.
- **Verifiable Presentation (VP)**: A Presentation with a cryptographic proof of Holder Binding.
- **Holder**: Entity that receives and presents Credentials.
- **Verifier**: Entity that requests, receives, and validates Presentations (OAuth 2.0 Client).
- **Wallet**: Entity used by Holder to manage Credentials.
- **VP Token**: Artifact containing one or more Presentations returned in an Authorization Response.
- **DCQL**: Digital Credentials Query Language – JSON query language for requesting Presentations.
- **Client Identifier Prefix**: String prefix in `client_id` indicating how to interpret the Client Identifier.
- **Response Mode `direct_post`**: Sends Authorization Response via HTTP POST to a Verifier endpoint.
- **Cryptographic Holder Binding**: Proof of possession of private key corresponding to a public key in the Credential.
- **Biometrics-based/Claims-based Holder Binding**: Alternative binding mechanisms.
- **Credential Format Identifier**: Identifies a specific Credential Format (e.g., `dc+sd-jwt`, `mso_mdoc`, `jwt_vc_json`, `ldp_vc`).
- **Transaction Data**: Data binding user identification/authentication to transaction authorization.

## Authorization Request
### New Parameters
- **`dcql_query`**: JSON object containing DCQL query. MUST be present if no `scope` representing DCQL query is present.
- **`client_metadata`**: OPTIONAL JSON object with Verifier metadata (e.g., `jwks`, `encrypted_response_enc_values_supported`, `vp_formats_supported`).
- **`request_uri_method`**: OPTIONAL. Values `get` (default) or `post`. When `post`, Wallet MAY send HTTP POST to `request_uri` with `wallet_metadata` and `wallet_nonce`.
- **`transaction_data`**: OPTIONAL array of base64url-encoded JSON objects with `type` and `credential_ids`.
- **`verifier_info`**: OPTIONAL array of attestations about the Verifier (format, data, credential_ids).

### Existing Parameters
- **`nonce`**: REQUIRED. Case-sensitive string for replay protection; fresh random value per request.
- **`scope`**: OPTIONAL. May alias a DCQL query.
- **`response_mode`**: REQUIRED. Values include `fragment`, `direct_post`, `dc_api`, `dc_api.jwt`, `direct_post.jwt`.
- **`client_id`**: REQUIRED. May include Client Identifier Prefix.
- **`state`**: REQUIRED under conditions (see Section 5.3) when Presentations without Holder Binding are requested; otherwise OPTIONAL.

### Response Type `vp_token`
When `response_type=vp_token`, response MUST include `vp_token` parameter. Default Response Mode is `fragment`. The `vp_token` is returned in the Authorization Response.

### Client Identifier Prefix and Verifier Metadata Management
- **Syntax**: `<client_id_prefix>:<orig_client_id>`.
- **Defined Prefixes**: `redirect_uri`, `openid_federation`, `decentralized_identifier`, `verifier_attestation`, `x509_san_dns`, `x509_hash`, `origin` (reserved for DC API).
- **Fallback**: If no `:` present, treat as pre-registered client.
- **Processing**: Wallet MUST use prefix to determine authentication and metadata retrieval rules.

### Request URI Method `post`
- Wallet sends HTTP POST to `request_uri` with `wallet_metadata` (OPTIONAL) and `wallet_nonce` (OPTIONAL).
- Verifier responds with `application/oauth-authz-req+jwt` containing signed/encrypted Request Object.
- Wallet MUST validate `wallet_nonce` if sent.

## Response
### VP Token Structure
JSON-encoded object with keys = `id` from DCQL Credential Query, values = arrays of Presentations. When `multiple` is false, array MUST contain exactly one Presentation.

### Response Mode `direct_post`
- Wallet sends HTTP POST to `response_uri` with Authorization Response parameters.
- Verifier responds with 200 and JSON object containing `redirect_uri` (OPTIONAL).
- `redirect_uri` MUST include fresh random value for session protection.

### Encrypted Responses
- Use unsigned encrypted JWT (JWE) for Authorization Response.
- Public key from `client_metadata` `jwks`. JWE `alg` from JWK `alg`, `enc` from `encrypted_response_enc_values_supported` (default `A128GCM`).
- Response Mode `direct_post.jwt` adds `response` parameter containing JWT.

### Error Response
- Additional error codes: `vp_formats_not_supported`, `invalid_request_uri_method`, `invalid_transaction_data`, `wallet_unavailable`.

## Digital Credentials Query Language (DCQL)
### Top-level Properties
- **`credentials`**: REQUIRED array of Credential Queries.
- **`credential_sets`**: OPTIONAL array of Credential Set Queries.

### Credential Query
- **`id`**: REQUIRED string (alphanumeric, underscore, hyphen).
- **`format`**: REQUIRED Credential Format Identifier.
- **`multiple`**: OPTIONAL boolean (default false).
- **`meta`**: REQUIRED object (format-specific, e.g., `vct_values`, `doctype_value`, `type_values`).
- **`trusted_authorities`**: OPTIONAL array of trusted authority queries.
- **`require_cryptographic_holder_binding`**: OPTIONAL boolean (default true).
- **`claims`**: OPTIONAL array of Claims Queries.
- **`claim_sets`**: OPTIONAL array of claim set options (used with `claims`).

### Credential Set Query
- **`options`**: REQUIRED array of arrays of Credential Query IDs.
- **`required`**: OPTIONAL boolean (default true).

### Claims Query
- **`id`**: OPTIONAL (REQUIRED if `claim_sets` present).
- **`path`**: REQUIRED array representing claims path pointer.
- **`values`**: OPTIONAL array of expected values (Wallet SHOULD return only if match; Verifier MUST NOT rely on it for security).
- For ISO mdoc, CBOR values converted to JSON for matching.

### Selecting Claims and Credentials
- Wallet MUST NOT disclose claims not selected.
- If `claim_sets` present, Wallet SHOULD return first satisfiable option.
- If `credential_sets` present, Wallet MUST satisfy all required sets; non-required are optional.
- If Wallet cannot deliver all required Credentials, MUST NOT return any.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Authorization Request MUST include `nonce` with fresh random value | MUST | Section 5.2 |
| R2 | Verifier MUST include `typ` header `oauth-authz-req+jwt` in Request Objects | MUST | Section 5 |
| R3 | Wallet MUST NOT process Request Objects without `typ` header `oauth-authz-req+jwt` | MUST | Section 5 |
| R4 | `dcql_query` or `scope` representing DCQL query MUST be present, not both | MUST | Section 5.1 |
| R5 | When `multiple` is false or omitted, `vp_token` array MUST contain exactly one Presentation | MUST | Section 8.1 |
| R6 | Wallet MUST ignore unrecognized parameters except `transaction_data` which MUST be rejected | MUST | Section 5 |
| R7 | Verifier MUST create fresh random `nonce` per request, store with session | MUST | Section 5.2 |
| R8 | For Presentations without Holder Binding, if `state` is required, Verifier MUST include it | MUST | Section 5.3 |
| R9 | Wallet MUST use full Client Identifier including prefix in responses | MUST | Section 14.8 |
| R10 | Verifier MUST validate Holder Binding including `client_id` and `nonce` binding | MUST | Section 14.1.2 |
| R11 | Wallet MUST link every Verifiable Presentation to `client_id` and `nonce` | MUST | Section 14.1.2 |
| R12 | When `request_uri_method=post`, Verifier MUST respond with signed/encrypted Request Object | MUST | Section 5.10.1 |
| R13 | Wallet MUST validate `wallet_nonce` if sent in POST request | MUST | Section 5.10.1 |
| R14 | Wallet MUST NOT accept `origin` Client Identifier Prefix in requests | MUST | Appendix A.2 |
| R15 | For DC API, audience for response MUST be `origin:<Origin>` | MUST | Appendix A.4 |
| R16 | For mdoc over redirects, `SessionTranscript` defined with `OpenID4VPHandover` | MUST | Appendix B.2.6.1 |
| R17 | For mdoc over DC API, `SessionTranscript` defined with `OpenID4VPDCAPIHandover` | MUST | Appendix B.2.6.2 |
| R18 | Implementations MUST follow BCP195 TLS requirements | MUST | Section 14.6 |
| R19 | Verifier MUST NOT rely on Wallet for constraint enforcement | MUST | Section 14.9 |

## Security Considerations (Condensed)
- **Replay Prevention**: Holder Binding proof MUST bind to `client_id` and `nonce`. Verifier MUST verify binding.
- **Presentations without Holder Binding**: Verifier accepts replay risk; MUST use `state` for binding.
- **Session Fixation**: Response Mode `direct_post` with `redirect_uri` including response code mitigates attacks.
- **TLS**: MUST follow BCP195.
- **Incorrect Implementations**: Use conformance testing tools from OpenID Foundation.
- **Always Use Full Client Identifier**: To avoid confusion attacks.

## Privacy Considerations (Condensed)
- **User Consent**: Wallet SHOULD obtain explicit, informed consent.
- **Selective Disclosure**: DCQL supports minimal disclosure; Wallet MUST NOT disclose unsolicited claims.
- **DCQL Value Matching**: Must not leak information about claim values to Verifier.
- **Error Responses**: SHOULD avoid leaking sensitive information; over DC API, Wallet SHOULD NOT return protocol errors without user interaction.
- **Trust in Issuers**: Mechanisms like `aki`, `etsi_tl`, `openid_federation` may require online resolution; privacy risks from data leakage.

## Normative References (Abbreviated)
- BCP195, DID-Core, I-D.ietf-jose-fully-specified-algorithms, I-D.ietf-oauth-sd-jwt-vc, I-D.ietf-oauth-selective-disclosure-jwt, JSON-LD, OAuth.Responses, OpenID.Core, OpenID.Federation, OpenID4VCI, RFC2119, RFC3986, RFC5280, RFC6125, RFC6749, RFC7515, RFC7516, RFC7517, RFC7518, RFC7519, RFC7591, RFC7638, RFC7800, RFC8174, RFC8414, SIOPv2, W3C.Digital_Credentials_API.

## Informative Annexes (Condensed)
- **Appendix A – OpenID4VP over the Digital Credentials API**: Defines protocol value format `openid4vp-v1-<request-type>`, request parameters (unsigned/signed/multisigned), response handling, and security considerations specific to DC API.
- **Appendix B – Credential Format Specific Parameters**: Defines format identifiers and metadata for `jwt_vc_json`, `ldp_vc`, `mso_mdoc`, `dc+sd-jwt`. Includes examples and format-specific processing rules.
- **Appendix C – Combining with SIOPv2**: Shows how to use `response_type=vp_token id_token` for combined credential presentation and authentication.
- **Appendix D – DCQL Examples**: Illustrates queries for mdoc, multiple credentials, claim sets, and value matching.
- **Appendix E – IANA Considerations**: Registers new parameters, error codes, metadata, media type `application/verifier-attestation+jwt`, URI scheme `openid4vp`.
- **Appendix F – Acknowledgements**: Lists contributors.
- **Appendix G – Notices**: Copyright and IPR policy.