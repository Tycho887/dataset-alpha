# OpenID4VC High Assurance Interoperability Profile 1.0
**Source**: OpenID Foundation Digital Credentials Protocols Workgroup | **Version**: 1.0 | **Date**: 24 December 2025 | **Type**: Normative Interoperability Profile
**Original**: openid4vc-high-assurance-interoperability-profile-1_0

## Scope (Summary)
This specification profiles OpenID4VCI, OpenID4VP, SD-JWT VC, and ISO mdoc to enable interoperable issuance and presentation of Verifiable Credentials for high-assurance use cases. It defines mandatory features for Issuers, Wallets, and Verifiers to achieve strong authenticity of claims and holder authentication.

## Normative References
- [FAPI2_Security_Profile]: Fett, D., Tonge, D., Heenan, J., "FAPI 2.0 Security Profile", 22 February 2025
- [I-D.ietf-oauth-sd-jwt-vc]: Terbu, O., Fett, D., Campbell, B., "SD-JWT-based Verifiable Credentials (SD-JWT VC)", draft-ietf-oauth-sd-jwt-vc-13
- [I-D.ietf-oauth-status-list]: Looker, T., Bastian, P., Bormann, C., "Token Status List (TSL)", draft-ietf-oauth-status-list-14
- [ISO.18013-5]: ISO/IEC 18013-5:2021
- [ISO.18013-5.second.edition]: ISO/IEC 18013-5 edition 2
- [OIDF.OID4VCI]: Lodderstedt et al., "OpenID for Verifiable Credential Issuance 1.0", 16 September 2025
- [OIDF.OID4VP]: Terbu et al., "OpenID for Verifiable Presentations 1.0", 9 July 2025
- [OIDF.ekyc-ida]: "OpenID Connect for Identity Assurance 1.0", 1 October 2024
- [RFC2119]: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14
- [RFC7515]: JSON Web Signature (JWS)
- [RFC7516]: JSON Web Encryption (JWE)
- [RFC7517]: JSON Web Key (JWK)
- [RFC7518]: JSON Web Algorithms (JWA)
- [RFC7636]: Proof Key for Code Exchange (PKCE)
- [RFC7800]: Proof-of-Possession Key Semantics for JWTs
- [RFC8174]: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [RFC8414]: OAuth 2.0 Authorization Server Metadata
- [RFC9101]: JWT-Secured Authorization Request (JAR)
- [RFC9126]: OAuth 2.0 Pushed Authorization Requests (PAR)
- [RFC9207]: OAuth 2.0 Authorization Server Issuer Identification
- [RFC9449]: OAuth 2.0 Demonstrating Proof of Possession (DPoP)
- [RFC9901]: Selective Disclosure for JSON Web Tokens
- [w3c.digital_credentials_api]: Caceres et al., "Digital Credentials API", 8 December 2025
- (Informative references: BSI.TR-02102-1, ECCG.ACM2, ETSI.TL, IANA.URI.Schemes, NIST.SP.800-131A, NIST.SP.800-57, eIDAS2.0)

## Definitions and Abbreviations
- **Holder**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Issuer**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Verifier**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Wallet**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Wallet Attestation**: As defined in OIDF.OID4VCI.
- **Credential Type**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Verifiable Credential**: As defined in OIDF.OID4VCI and OIDF.OID4VP.
- **Ecosystem**: A group of Issuers, Wallets, and Verifiers that have a common set of rules by which they operate.

## Introduction (Condensed)
This specification selects features from OpenID4VCI, OpenID4VP, SD-JWT VC, and ISO mdoc to ensure interoperability for high-assurance use cases. It aims for authenticity of claims and holder authentication. The scope includes secure issuance, credential protection, and Verifier access to Issuer trust information. Holder binding and claim-based binding are supported. This profile does not meet all eIDAS LoA High requirements; additional measures are needed.

## Section 1: Introduction (Target Audience, Errata)
- Target audience: implementers needing high security/privacy (e.g., eIDAS 2.0, CA DMV, OWF, IDunion, GAIN, Japanese Trusted Web).
- Errata revisions published at openid4vc-high-assurance-interoperability-profile-1_0; final at -final.

## Section 2: Terminology
- Uses terms as per [OIDF.OID4VCI] and [OIDF.OID4VP].
- **Ecosystem** defined as above.

## Section 3: Scope
- This specification enables: (1) Issuance using OpenID4VCI, (2) Presentation using OpenID4VP with redirects, (3) Presentation using OpenID4VP with W3C Digital Credentials API.
- Implementations MUST comply with all requirements for a chosen flow, and non-flow-specific requirements.
- For each flow, at least one of the Credential Format Profiles (Section 6) MUST be supported: IETF SD-JWT VC or ISO mdoc.
- Optional parameters in profiled specs remain optional unless stated otherwise.
- Profiles: OpenID4VCI defines Wallet Attestation and Key Attestation; SD-JWT VC profile defines status management, key binding, issuer key resolution, issuer identification.
- Assumptions: Issuer uses Wallet features defined herein; mechanisms exist for capability discovery.
- Additional scenarios: Combined issuance of SD-JWT VC and ISO mdoc; issuer-initiated and wallet-initiated issuance; issuance/presentation with/without cryptographic holder binding.
- Out of scope: Trust management, offline presentation protocols.

## Section 4: OpenID for Verifiable Credential Issuance
### 4.1 General Requirements
- Wallet and Credential Issuer MUST support authorization code flow.
- MUST support at least one Credential Format Profile (Section 6). Ecosystems SHOULD indicate required formats.
- MUST comply with FAPI2_Security_Profile provisions applicable here, including PKCE with S256, PAR (where applicable), and `iss` value in authorization response.
- Sender-constrained access token: MUST support DPoP (RFC9449).
- Client authentication: Wallet Attestation (Section 4.4.1) can be used.
- PAR only required when using Authorization Endpoint per OpenID4VCI Section 5.
- Cryptography: Section 7 overrides FAPI2 5.4.1 clause 1.
- Ecosystems SHOULD indicate whether Issuer-initiated or Wallet-initiated issuance is needed. If Issuer-initiated, MUST use Credential Offer per OpenID4VCI Section 4.1.
- If batch issuance supported, Wallet SHOULD use it; Issuer MUST indicate via `batch_credential_issuance` metadata.

### 4.2 Issuer Metadata
- Authorization Server MUST support metadata per RFC8414.
- Credential Issuer MUST support metadata retrieval per OpenID4VCI Section 12.2.2; metadata MUST include scope for every Credential Configuration.
- If Ecosystem requires higher Issuer authentication, signed Credential Issuer Metadata (OpenID4VCI Section 11.2.3) MUST be supported by Wallet and Issuer. Key resolution using `x5c` JOSE header; trust anchor certificate MUST NOT be included; signing certificate MUST NOT be self-signed.
- Wallets rendering images from metadata MUST support SVG and PNG for both data URIs and HTTPS URLs.
- If Issuer supports configurations requiring key binding, `nonce_endpoint` MUST be present in metadata.

### 4.3 Credential Offer
- Grant type `authorization_code` MUST be supported.
- Issuer MUST include scope value to identify Credential Type; Wallet MUST use that scope.
- Custom URL scheme `haip-vci://` MAY be supported; other schemes per ecosystem.
- Issuer and Wallet MUST support Credential Offer in both same-device and cross-device flows.

### 4.4 Authorization Endpoint
- Wallets MUST authenticate at PAR endpoint using same rules as token endpoint (Section 4.4).
- MUST use `scope` parameter to communicate Credential Type(s).

### 4.5 Token Endpoint
- Refresh tokens: RECOMMENDED for credential refresh. Issuers SHOULD consider refresh token lifetime.

#### 4.5.1 Wallet Attestation
- Wallets MUST use and Issuers MUST require OAuth2 Client authentication at applicable endpoints.
- Ecosystems desiring wallet-issuer interoperability on Wallet Attestation level SHOULD require format in OpenID4VCI Appendix E. Additional ecosystem-specific claims may be defined.
- When using Appendix E format: public key certificate and chain (excluding trust anchor) MUST be in `x5c` JOSE header of Client Attestation JWT.
- Wallet Attestations MUST NOT be reused across different Issuers. MUST NOT introduce unique identifier per Wallet instance. Subject claim MUST be shared by all instances of same wallet implementation.
- If applicable, `client_id` in PAR MUST equal `sub` value in client attestation JWT.
- Wallets MUST perform client authentication with Wallet Attestation at OAuth2 endpoints that support client authentication.

### 4.6 Credential Endpoint
#### 4.6.1 Key Attestation
- Wallets MUST support key attestations. Ecosystems desiring interoperability on key attestation level SHOULD require format in OpenID4VCI Appendix D, with proof types `jwt` using `key_attestation` or `attestation`.
- When using Appendix D: public key used to validate attestation MUST be in `x5c` JOSE header; trust anchor certificate MUST NOT be included; signing certificate MUST NOT be self-signed. Certificate profiles out of scope.
- If batch issuance and cryptographic holder binding required, all public keys SHOULD be attested in a single key attestation.

## Section 5: OpenID for Verifiable Presentations
- Wallet and Verifier MUST support at least one Credential Format Profile (Section 6): SD-JWT VC or ISO mdoc.
- Response type MUST be `vp_token`.
- For signed requests: Verifier MUST use and Wallet MUST accept Client Identifier Prefix `x509_hash` (OpenID4VP Section 5.9.3). Trust anchor cert MUST NOT be in `x5c`; signing cert MUST NOT be self-signed.
- DCQL query and response MUST be used (OpenID4VP Section 6).
- Response encryption MUST be performed per OpenID4VP Section 8.3. JWE `alg` MUST be `ECDH-ES` with P-256; `enc` values `A128GCM` and `A256GCM` MUST be supported by Verifiers; Wallets MUST support at least one; if both, SHOULD use `A256GCM`. Verifiers MUST list both `enc_values` in metadata.
- Verifiers MUST supply ephemeral encryption keys per Authorization Request.
- AKI-based Trusted Authority Query (`trusted_authorities`) for DCQL MUST be supported.

### 5.1 OpenID for Verifiable Presentations via Redirects
- Custom URL scheme `haip-vp://` MAY be supported by Wallet and Verifier.
- Signed Authorization Requests MUST be used via JAR with `request_uri`.
- Response mode `direct_post.jwt` MUST be used. Security considerations (OpenID4VP Section 14.3) MUST be applied.
- Verifiers and Wallets MUST support same-device flow. Verifiers RECOMMENDED to use only same-device unless no session binding needed.
- If same-device: Verifiers MUST include `redirect_uri` in HTTP response; Wallets MUST follow redirect; Verifiers MUST reject if redirect not followed or different session.

### 5.2 OpenID for Verifiable Presentations via W3C Digital Credentials API
- Wallet MUST support Wallet Invocation via W3C Digital Credentials API or equivalent. Verifier MUST use that.
- Wallet MUST support Response Mode `dc_api.jwt`; Verifier MUST use it.
- Verifier and Wallet MUST use OpenID4VP Appendix A.
- Wallet MUST support unsigned, signed, and multi-signed requests (Appendices A.3.1, A.3.2). Verifier MUST support at least one.

### 5.3 Requirements Specific to Credential Formats
#### ISO mdoc
- Credential Format identifier MUST be `mso_mdoc`.
- Multiple mdocs returned: each in separate DeviceResponse, matching DCQL query; `vp_token` contains multiple instances.
- Issuer MAY include MSO revocation mechanism; if so, MUST use ISO/IEC 18013-5 mechanisms.

#### IETF SD-JWT VC
- Credential Format identifier MUST be `dc+sd-jwt`.

## Section 6: OpenID4VC Credential Format Profiles
- SD-JWT VC profile: appendices A.3 (issuance) and B.3 (presentation) from OIDF specs, with additional requirements in 6.1.
- ISO mdoc profile: appendices A.2 and B.2.

### 6.1 IETF SD-JWT VC Profile
- Compact serialization MUST be supported; JSON MAY be supported.
- RECOMMENDED that Issuers limit validity; if so, MUST use `exp` and/or `status` claims.
- `cnf` claim MUST conform to SD-JWT VC spec; if key binding required, MUST include JWK in `jwk` member.
- `status` claim, if present, MUST contain `status_list` per [I-D.ietf-oauth-status-list].
- Public key for Status List Token signature MUST be in `x5c` JOSE header; trust anchor MUST NOT be included; signing cert MUST NOT be self-signed.
- Each Credential MUST have unique, unpredictable status list index.

#### 6.1.1 Issuer Identification and Key Resolution
- X.509 certificate-based key resolution MUST be supported by all entities (Issuer, Wallet, Verifier).
- SD-JWT VC MUST contain issuer's signing certificate and trust chain in `x5c` JOSE header. Trust anchor MUST NOT be included; signing cert MUST NOT be self-signed.

#### 6.1.1.1 Cryptographic Holder Binding between VC and VP
- If credential has cryptographic holder binding, a KB-JWT MUST always be present when presenting.

## Section 7: Requirements for Digital Signatures
- All entities MUST support ECDSA with P-256 and SHA-256 (JOSE ES256; COSE -7/-9) for validating:
  - Issuers: Wallet Attestations (if Appendix E), Key Attestations (if Appendix D), `jwt` proof type.
  - Verifiers: VP signature (KB-JWT or deviceSignature), status information.
  - Wallets: signed presentation requests, signed Issuer metadata.
- Ecosystem profiles MAY mandate additional suites. Each entity SHOULD make supported algorithms explicit in metadata.

## Section 8: Hash Algorithms
- SHA-256 MUST be supported by all entities for digests in SD-JWT VC and ISO mdoc.
- Ecosystem profiles MAY mandate additional hash algorithms. Each entity SHOULD indicate supported algorithms in metadata.

## Section 9: Implementation Considerations (Informative, Condensed)
- 9.1: Some flows depend on browser/OS support (e.g., W3C Digital Credentials API); implementers must handle unavailability.
- 9.2: Key attestations may require transformation services; can pre-create keys.
- 9.3: Ecosystems define extensions: flows, credential formats, signed metadata, offer carriage, attestation formats, certificate profiles, crypto suites.
- 9.3.1: Non-normative examples (Baseline Interoperability using both sd-jwt and mdoc, haip schemes; Compatibility with ISO 18013-5 using only mdoc).
- 9.4: Pre-final specifications: SD-JWT VC draft -13, Token Status List draft -14. Implementations should use these versions until updated.

## Section 10: Security Considerations (Condensed)
- Refer to OIDF specs for security. Conformance testing tools available from OpenID Foundation. Key sizes should follow NIST/BSI/ECCG guidance.

## Section 11: Privacy Considerations (Condensed)
- Refer to OIDF specs. For interoperable key attestations, backend transformation services MUST be designed with privacy (e.g., stateless, no user identifier binding).

## Annexes (Condensed)
- **Appendix A: IANA Considerations** – Registers URI schemes `haip-vci` and `haip-vp` for wallet invocation in issuance and presentation.
- **Appendix B: Acknowledgements** – Lists contributors.
- **Appendix C: Notices** – Copyright OpenID Foundation; license for reproduction and implementation; patent promise.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Support at least one credential format (SD-JWT VC or ISO mdoc) for each flow | MUST | Section 3 |
| R2 | Support authorization code flow for issuance | MUST | Section 4 |
| R3 | Comply with FAPI2 Security Profile applicable provisions (PKCE, PAR, iss) | MUST | Section 4 |
| R4 | Support DPoP for sender-constrained access tokens | MUST | Section 4.1 |
| R5 | Use Wallet Attestation for client authentication (if ecosystem requires) | MUST/REQUIRED (by Issuer) | Section 4.4.1 |
| R6 | Wallet Attestations: include x5c, not reuse across Issuers, not unique per instance | MUST | Section 4.4.1 |
| R7 | Support key attestations (Appendix D format as base) | MUST (Wallet) | Section 4.5.1 |
| R8 | For presentation: response type vp_token, use DCQL, response encryption with ECDH-ES/P-256 and A128GCM/A256GCM | MUST | Section 5 |
| R9 | Support x509_hash Client Identifier Prefix for signed requests | MUST (Verifier) / MUST (Wallet accept) | Section 5 |
| R10 | Support W3C Digital Credentials API flow (if chosen) | MUST (Wallet) | Section 5.2 |
| R11 | For signed requests: use JAR with request_uri, direct_post.jwt response mode | MUST | Section 5.1 |
| R12 | For same-device redirect flow: include and follow redirect_uri | MUST | Section 5.1 |
| R13 | Support compact serialization for SD-JWT VC; use RFC9901 | MUST | Section 6.1 |
| R14 | Use exp/status claims if validity limited; cnf with jwk if key binding | MUST | Section 6.1 |
| R15 | Support X.509 certificate-based key resolution for SD-JWT VC issuer signature | MUST (all entities) | Section 6.1.1 |
| R16 | Present KB-JWT if credential has cryptographic holder binding | MUST | Section 6.1.1.1 |
| R17 | Support ECDSA P-256 SHA-256 (ES256) for digital signatures | MUST (all entities) | Section 7 |
| R18 | Support SHA-256 for hash digests | MUST (all entities) | Section 8 |