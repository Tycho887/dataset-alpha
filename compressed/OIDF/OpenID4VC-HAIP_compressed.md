# OpenID4VC High Assurance Interoperability Profile 1.0
**Source**: OpenID Foundation Digital Credentials Protocols Working Group | **Version**: 1.0 | **Date**: 24 December 2025 | **Type**: Final Specification
**Original**: [openid4vc-high-assurance-interoperability-profile-1_0](openid4vc-high-assurance-interoperability-profile-1_0) (latest), [final](openid4vc-high-assurance-interoperability-profile-1_0-final)

## Scope (Summary)
This specification defines a profile of OpenID for Verifiable Credentials (OpenID4VCI, OpenID4VP) combined with IETF SD-JWT VC and ISO mdoc credential formats, selecting features and defining requirements for interoperability among Issuers, Wallets, and Verifiers requiring high security and privacy. It aims to achieve authenticity of claims, holder authentication, and protection of credential data, but does not cover all eIDAS Level of Assurance High requirements.

## Normative References
- [FAPI2_Security_Profile]: Fett, D., Tonge, D., Heenan, J., "FAPI 2.0 Security Profile", 22 February 2025, <https://openid.net/specs/fapi-security-profile-2_0.html>
- [I-D.ietf-oauth-sd-jwt-vc]: Terbu, O., Fett, D., Campbell, B., "SD-JWT-based Verifiable Credentials (SD-JWT VC)", Work in Progress, draft-ietf-oauth-sd-jwt-vc-13, 6 November 2025, <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-sd-jwt-vc-13>
- [I-D.ietf-oauth-status-list]: Looker, T., Bastian, P., Bormann, C., "Token Status List (TSL)", Work in Progress, draft-ietf-oauth-status-list-14, 10 December 2025, <https://datatracker.ietf.org/doc/html/draft-ietf-oauth-status-list-14>
- [ISO.18013-5]: ISO/IEC 18013-5:2021 Personal identification — ISO-compliant driving license Part 5: Mobile driving license (mDL) application, 2021, <https://www.iso.org/standard/69084.html>
- [ISO.18013-5.second.edition]: ISO/IEC 18013-5:xxxx edition 2, <https://www.iso.org/standard/91081.html>
- [OIDF.OID4VCI]: Lodderstedt, T., Yasuda, K., Looker, T., Bastian, P., "OpenID for Verifiable Credential Issuance 1.0", 16 September 2025, <https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html>
- [OIDF.OID4VP]: Terbu, O., Lodderstedt, T., Yasuda, K., Fett, D., Heenan, J., "OpenID for Verifiable Presentations 1.0", 9 July 2025, <https://openid.net/specs/openid-4-verifiable-presentations-1_0.html>
- [OIDF.ekyc-ida]: Fett, D., Haine, M., Pulido, A., Lehmann, K., Koiwai, K., "OpenID Connect for Identity Assurance 1.0", 1 October 2024, <https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html>
- [RFC2119]: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC7515]: Jones, M., et al., "JSON Web Signature (JWS)", RFC 7515, May 2015
- [RFC7516]: Jones, M., Hildebrand, J., "JSON Web Encryption (JWE)", RFC 7516, May 2015
- [RFC7517]: Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015
- [RFC7518]: Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015
- [RFC7636]: Sakimura, N., et al., "Proof Key for Code Exchange by OAuth Public Clients", RFC 7636, September 2015
- [RFC7800]: Jones, M., et al., "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)", RFC 7800, April 2016
- [RFC8174]: Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017
- [RFC8414]: Jones, M., et al., "OAuth 2.0 Authorization Server Metadata", RFC 8414, June 2018
- [RFC9101]: Sakimura, N., et al., "The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)", RFC 9101, August 2015
- [RFC9126]: Lodderstedt, T., et al., "OAuth 2.0 Pushed Authorization Requests", RFC 9126, September 2021
- [RFC9207]: Meyer zu Selhausen, K., Fett, D., "OAuth 2.0 Authorization Server Issuer Identification", RFC 9207, March 2022
- [RFC9449]: Fett, D., et al., "OAuth 2.0 Demonstrating Proof of Possession (DPoP)", RFC 9449, September 2023
- [RFC9901]: Fett, D., Yasuda, K., Campbell, B., "Selective Disclosure for JSON Web Tokens", RFC 9901, November 2025

## Definitions and Abbreviations
- **Holder**, **Issuer**, **Verifier**, **Wallet**, **Wallet Attestation**, **Credential Type**, **Verifiable Credential**: As defined in [OIDF.OID4VCI] and [OIDF.OID4VP].
- **Ecosystem**: A group of Issuers, Wallets and Verifiers that have a common set of rules by which they operate.
- Other abbreviations: SD-JWT VC (Selective Disclosure JWT-based Verifiable Credentials), mdoc (mobile document), DCQL (Data Collection Query Language), DC API (Digital Credentials API), PAR (Pushed Authorization Requests), DPoP (Demonstrating Proof of Possession), JAR (JWT-Secured Authorization Request), MSO (Mobile Security Object), KB-JWT (Key Binding JWT).

## 1. Introduction
This specification enables interoperable issuance and presentation of Verifiable Credentials with high security and privacy. It is an interoperability profile for various industries and regulatory environments. Key properties include:
- **Authenticity of claims** via secure issuance, credential protection, and trustworthy Issuer information.
- **Holder authentication** via key binding and Claim-based Binding.
- *Note*: Does not define holder authentication mechanisms or policies; technical means only.
- *Note*: Does not fully meet eIDAS Level of Assurance High; additional measures needed.

Profiles: OpenID4VCI for issuance, OpenID4VP for presentation; credential formats: IETF SD-JWT VC and ISO mdoc.

### 1.1 Target Audience/Usage
Implementers requiring high security and privacy, e.g., eIDAS 2.0, California DMV, OWF, IDunion, GAIN, Japanese Trusted Web project.

### 1.2 Errata Revisions
Latest revision: `openid4vc-high-assurance-interoperability-profile-1_0`; final approved: `openid4vc-high-assurance-interoperability-profile-1_0-final`.

### 1.3 Requirements Notation and Conventions
Key words (MUST, SHALL, etc.) are interpreted per BCP 14 [RFC2119][RFC8174] when in all capitals.

## 2. Terminology
(Definitions as above in Definitions section.)

## 3. Scope
This specification enables:
- Issuance via OpenID4VCI
- Presentation via OpenID4VP with redirects
- Presentation via OpenID4VP with W3C Digital Credentials API

Implementation MUST comply with all requirements for each chosen flow, plus non-flow-specific sections.
For each flow, at least one credential profile from Section 6 (IETF SD-JWT VC or ISO mdoc) MUST be supported.
Parameters optional in profiled specs remain optional unless stated.
Profiles define: Wallet Attestation and Key Attestation (OpenID4VCI); status management, key binding, issuer key resolution (SD-JWT VC).
OpenID4VP can be remote or in-person.

### 3.1 Assumptions
- Issuer uses Wallet features defined herein.
- Mechanisms exist for Verifier/Wallet/Issuer capability discovery.

### 3.2 Additional Scenarios
Non-exhaustive: combined issuance (SD-JWT VC + mdoc), issuer-initiated and wallet-initiated issuance, with or without cryptographic holder binding.

### 3.3 Standards Requirements
Profiled standards: OpenID4VCI, OpenID4VP, W3C Digital Credentials API, SD-JWT VC, ISO/IEC 18013-5. Underlying standards also apply.

### 3.4 Out of Scope
- Trust management (X.509 PKI used but establishment out of scope).
- Offline presentation (e.g., BLE).

## 4. OpenID for Verifiable Credential Issuance
When implementing OpenID4VCI, both Wallet and Credential Issuer:
- MUST support authorization code flow.
- MUST support at least one credential format from Section 6. Ecosystems SHOULD indicate required formats.
- MUST comply with [FAPI2_Security_Profile] applicable provisions, including PKCE with S256, PAR (where applicable), `iss` value in Authorization response.
  - Sender-constrained access tokens: MUST support DPoP [RFC9449].
  - Client authentication: Wallet Attestation (Section 4.4.1) can be used.
  - PAR: Only required when using Authorization Endpoint per OID4VCI Section 5.
  - Cryptography: Section 7 overrides FAPI2 Section 5.4.1 clause 1.
- Ecosystems SHOULD indicate support for Issuer-initiated/Wallet-initiated issuance. If Issuer-initiated, Credential Offer per OID4VCI Section 4.1 MUST be used.
- If batch issuance supported, Wallet SHOULD use it; Issuer MUST indicate via `batch_credential_issuance` metadata.
- Additional requirements: Sections 7 and 8.

### 4.1 Issuer Metadata
- Authorization Server MUST support metadata per [RFC8414].
- Credential Issuer MUST support metadata retrieval per OID4VCI Section 12.2.2; metadata MUST include `scope` for every Credential Configuration.
- Signed Credential Issuer Metadata (OID4VCI Section 11.2.3) MUST be supported by Wallet and Issuer when Ecosystem requires higher Issuer Authentication. Key resolution via `x5c` JOSE header [RFC7515]; trust anchor certificate MUST NOT be in `x5c`; signing certificate MUST NOT be self-signed.
- Wallets rendering images from metadata MUST support SVG and PNG formats, images via data URIs and HTTPS URLs.
- If Issuer supports key binding (`cryptographic_binding_methods_supported` present), `nonce_endpoint` MUST be present.

### 4.2 Credential Offer
- Grant type `authorization_code` MUST be supported.
- Issuer MUST include scope value for Wallet to identify Credential Type; Wallet MUST use that scope in Authorization parameter.
- Custom URL scheme `haip-vci://` MAY be supported; other schemes MAY be used per Ecosystem agreement.
- Issuer and Wallet MUST support Credential Offer in same-device and cross-device flows.

### 4.3 Authorization Endpoint
- Wallets MUST authenticate at PAR endpoint using same rules as Section 4.4 for token endpoint.
- MUST use `scope` parameter to communicate Credential Type(s); scope value maps to a specific Credential Type.

### 4.4 Token Endpoint
- Refresh tokens RECOMMENDED for credential refresh (OID4VCI Section 13.5). Issuers SHOULD consider refresh token lifetime; usage after >1 year NOT RECOMMENDED.

#### 4.4.1 Wallet Attestation
- Wallets MUST use, Issuers MUST require OAuth2 Client authentication at supported endpoints.
- Ecosystems desiring interoperability on Wallet Attestations SHOULD require format in OID4VCI Appendix E. Additional rules:
  - `x5c` JOSE header MUST include public key certificate and optionally trust chain excluding trust anchor.
  - Wallet Attestations MUST NOT be reused across Issuers; MUST NOT introduce unique identifier per Wallet instance; `sub` claim must be shared by all instances of that wallet implementation.
  - If applicable, `client_id` in PAR request MUST equal `sub` value in client attestation JWT.
  - Wallets MUST perform client authentication with Wallet Attestation at all OAuth2 endpoints that support it.
- Ecosystems MAY choose other formats.

### 4.5 Credential Endpoint
#### 4.5.1 Key Attestation
- Wallets MUST support key attestations. Ecosystems desiring interoperability SHOULD require format in OID4VCI Appendix D, with proof types:
  - `jwt` using `key_attestation`
  - `attestation`
- Rules when using Appendix D format:
  - Public key used to validate signature MUST be in `x5c` JOSE header.
  - Trust anchor certificate MUST NOT be in `x5c`.
  - Signing certificate MUST NOT be self-signed.
  - Certificate profiles out of scope.
- Ecosystems MAY choose other formats (define new proof type or expand `jwt`).
- If batch issuance with cryptographic holder binding required, all public keys in Credential Request SHOULD be attested within a single key attestation.

## 5. OpenID for Verifiable Presentations
Requirements for all presentation flows:
- Wallet and Verifier MUST support at least one credential format from Section 6. Ecosystems SHOULD indicate required formats.
- Response type MUST be `vp_token`.
- For signed requests, Verifier MUST use and Wallet MUST accept Client Identifier Prefix `x509_hash` (OID4VP Section 5.9.3). Trust anchor certificate MUST NOT be in `x5c`; signing certificate MUST NOT be self-signed; certificate profiles out of scope.
- DCQL query and response MUST be used (OID4VP Section 6).
- Response encryption MUST be performed per OID4VP Section 8.3. JWE `alg` header MUST be `ECDH-ES` with `P-256` curve. JWE `enc` values `A128GCM` and `A256GCM` MUST be supported by Verifiers; Wallets MUST support at least one; if both, Wallet SHOULD use `A256GCM`. Verifiers MUST list both in `encrypted_response_enc_values_supported`.
- Verifiers MUST supply ephemeral encryption public keys per OID4VP Section 8.3.
- Authority Key Identifier (`aki`)-based Trusted Authority Query (`trusted_authorities`) for DCQL MUST be supported.
- Additional requirements in Sections 5.1–5.3, 7, 8.

### 5.1 OpenID4VP via Redirects
- Custom URL scheme `haip-vp://` MAY be supported; other schemes MAY be used.
- Signed Authorization Requests MUST use JAR [RFC9101] with `request_uri` parameter.
- Response encryption MUST use `direct_post.jwt` response mode (OID4VP Section 8.3); security considerations in OID4VP Section 14.3 MUST be applied.
- Verifiers and Wallets MUST support same-device flow. Verifiers RECOMMENDED to use only same-device unless no session binding needed (e.g., proximity). If same-device:
  - Verifiers MUST include `redirect_uri` in HTTP response to Wallet's POST to `response_uri`.
  - Wallets MUST follow redirect to `redirect_uri`.
  - Verifiers MUST reject presentations if Wallet does not follow redirect or redirect arrives in different user session.

### 5.2 OpenID4VP via W3C Digital Credentials API
- Wallet MUST support Wallet Invocation via W3C DC API or equivalent platform API; Verifier MUST use it.
- Wallet MUST support Response Mode `dc_api.jwt`; Verifier MUST use it.
- Verifier and Wallet MUST use OID4VP Appendix A for OpenID4VP over DC API.
- Wallet MUST support unsigned, signed, and multi-signed requests (OID4VP Appendices A.3.1, A.3.2); Verifier MUST support at least one.

### 5.3 Requirements specific to Credential Formats
#### 5.3.1 ISO mdocs
- Credential Format identifier MUST be `mso_mdoc`.
- Multiple mdocs returned separately in separate `DeviceResponse` instances each matching respective DCQL query; `vp_token` contains multiple instances.
- Issuer MAY include MSO revocation mechanism; when doing so, MUST use one defined in ISO/IEC 18013-5 edition 2.

#### 5.3.2 IETF SD-JWT VC
- Credential Format identifier MUST be `dc+sd-jwt`.

## 6. OpenID4VC Credential Format Profiles
Profiles:
- IETF SD-JWT VC (Section 6.1) with references: OID4VCI Appendix A.3, OID4VP Appendix B.3.
- ISO mdoc: OID4VCI Appendix A.2, OID4VP Appendix B.2.

### 6.1 IETF SD-JWT VC Profile
Additional requirements for SD-JWT VC:
- Compact serialization MUST be supported [RFC9901]; JSON serialization MAY be supported.
- Issuers RECOMMENDED to limit validity period; when doing so, MUST use `exp` and/or `status` claim.
- `cnf` claim MUST conform to [I-D.ietf-oauth-sd-jwt-vc]; MUST include JWK `jwk` member if cryptographic holder binding required.
- `status` claim, if present, MUST contain `status_list` per [I-D.ietf-oauth-status-list].
- Public key for Status List Token signature MUST be in `x5c` JOSE header; trust anchor not included; signing cert not self-signed.
- Each Credential MUST have unique, unpredictable status list index.
- *Note*: For verification status and identity assurance, [OIDF.ekyc-ida] syntax SHOULD be used; jurisdiction/Ecosystem decides.
- *Note*: Subject identifier (`sub`) MAY be used; no binding to `cnf` required.
- *Note*: Expiration not always desired (e.g., diploma); left to Issuer/body.

#### 6.1.1 Issuer identification and key resolution
- X.509 certificate-based key resolution MUST be supported by all entities (Issuer, Wallet, Verifier). SD-JWT VC MUST contain issuer's signing certificate and trust chain in `x5c` JOSE header; trust anchor not included; signing cert not self-signed.

#### 6.1.1.1 Cryptographic Holder Binding between VC and VP
- If credential has cryptographic holder binding, a KB-JWT MUST always be present when presenting an SD-JWT VC.

## 7. Requirements for Digital Signatures
All entities MUST support ECDSA with P-256 and SHA-256 (JOSE `ES256`; COSE `-7` or `-9` as applicable) for validating:
- Issuers: Wallet Attestations (including PoP) when using OID4VCI Appendix E; Key Attestations when using Appendix D; `jwt` proof type.
- Verifiers: VP signature (KB-JWT or `deviceSignature` CBOR); status info of VC or Wallet Attestation.
- Wallets: signed presentation requests; signed Issuer metadata.
- Ecosystem profiles MAY mandate additional crypto suites.
- Each entity SHOULD make explicit in metadata which other algorithms/key types supported.

## 8. Hash Algorithms
- SHA-256 MUST be supported by all entities for digests in SD-JWT VC and ISO mdoc.
- Ecosystem profiles MAY mandate additional hash algorithms; each entity SHOULD make metadata explicit.

## 9. Implementation Considerations
### 9.1 Requirements for browser/OS support
Some flows (e.g., DC API) depend on platform support; implementers may not be able to support due to factors beyond control. Optional prerequisites (e.g., custom URL schemes) allow alternative mechanisms.

### 9.2 Interoperable Key Attestations
Wallet implementations using Appendix D format may need a transformation service; this may impact availability/performance. Mitigation: create keys and obtain attestations in advance.

### 9.3 Ecosystem Implementation Considerations
Extension points: flows, presentation method, credential format, signed Issuer metadata, Credential Offer method, key/wallet attestation format, X.509 certificate profiles, additional crypto/hash suites.

#### 9.3.1 Non-normative Examples
- **Example 1 (Baseline interoperability)**: Both presentation and issuance; no additional crypto; wallets support both mdoc and sd-jwt-vc; unsigned Issuer metadata; `haip-vci://` and `haip-vp://` schemes; Appendix D & E formats; DC API fallback. Maximizes interoperability but increases wallet burden and potential privacy/security issues.
- **Example 2 (ISO/IEC 18013-5 compatibility)**: Presentation only; only mdoc format; `haip-vp://` scheme; Reader Authentication Certificate profile per 18013-5; Verifier supports all Curve 1 and hash algorithms from 18013-5. Ensures compatibility at increased verifier cost.

### 9.4 Pre-Final Specifications
This specification uses drafts (SD-JWT VC draft -13, Token Status List draft -14). Breaking changes not expected; if occur, implementations should continue using referenced versions unless updated by a profile.

## 10. Security Considerations
Security considerations from underlying specs apply (OID4VCI Section 13, OID4VP Sections 14 and A.5). Implementation must be complete and correct; conformance testing tools available at OpenID Foundation.

### 10.2 Key sizes
Implementers must ensure appropriate key sizes per NIST, BSI, or ECCG guidance.

## 11. Privacy Considerations
Privacy considerations from underlying specs apply (OID4VCI Section 15, OID4VP Sections 15 and A.6).

### 11.1 Interoperable Key Attestations
Backend service for key attestation transformation MUST be designed with privacy (e.g., stateless, no user identifier binding).

## 12. Normative References
(Listed in Normative References section above.)

## 13. Informative References
- [BSI.TR-02102-1] Federal Office for Information Security (BSI), "Cryptographic Mechanisms: Recommendations and Key Lengths", January 2025.
- [ECCG.ACM2] European Cybersecurity Certification Group, "Agreed Cryptographic Mechanisms 2.0", April 2025.
- [ETSI.TL] ETSI TS 119 612 V2.4.1, "Electronic Signatures and Trust Infrastructures; Trusted Lists", August 2025.
- [IANA.URI.Schemes] IANA, "Uniform Resource Identifier (URI) Schemes".
- [NIST.SP.800-131A] Barker, E., Roginsky, A., "NIST SP 800-131A: Transitioning the Use of Cryptographic Algorithms and Key Lengths", March 2019.
- [NIST.SP.800-57] Barker, E., "NIST SP 800-57 Part 1: Recommendation for Key Management: Part 1 – General", May 2020.
- [eIDAS2.0] EU Regulation 2024/1183, April 2024.
- [w3c.digital_credentials_api] Caceres, M., et al., "Digital Credentials API", 8 December 2025.

## Appendix A: IANA Considerations
Two URI schemes registered: `haip-vci://` (for issuance) and `haip-vp://` (for presentation). Permanent status; contact OpenID Foundation Digital Credentials Protocols WG.

## Appendix B: Acknowledgements
Thanks to many contributors (list omitted for brevity; see original document).

## Appendix C: Notices
Copyright © 2025 The OpenID Foundation. License granted for implementation and development. No warranties; patent promise per OIDF policy.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST comply with all requirements for chosen flows plus non-flow-specific sections. | MUST | Section 3 |
| R2 | For each flow, at least one credential profile from Section 6 MUST be supported. | MUST | Section 3 |
| R3 | Issuance: Authorization code flow MUST be supported. | MUST | Section 4 |
| R4 | Issuance: MUST comply with FAPI2 Security Profile applicable provisions. | MUST | Section 4 |
| R5 | Issuance: Sender-constrained access tokens MUST support DPoP. | MUST | Section 4 |
| R6 | Issuance: Wallet Attestation MUST be used at client authentication endpoints. | MUST | Section 4.4.1 |
| R7 | Issuance: Wallet Attestations MUST NOT be reused across Issuers. | MUST | Section 4.4.1 |
| R8 | Issuance: Wallet Attestation `sub` claim must be shared by all instances of wallet implementation. | MUST | Section 4.4.1 |
| R9 | Issuance: Key attestations MUST be supported by Wallets. | MUST | Section 4.5.1 |
| R10 | Presentation: Response type MUST be `vp_token`. | MUST | Section 5 |
| R11 | Presentation: For signed requests, Verifier MUST use and Wallet MUST accept `x509_hash` Client Identifier Prefix. | MUST | Section 5 |
| R12 | Presentation: DCQL query and response MUST be used. | MUST | Section 5 |
| R13 | Presentation: Response encryption MUST be performed per OID4VP Section 8.3 with JWE `alg` ECDH-ES P-256. | MUST | Section 5 |
| R14 | Presentation: `aki`-based Trusted Authority Query MUST be supported. | MUST | Section 5 |
| R15 | Presentation (redirect): Signed Authorization Requests MUST use JAR with `request_uri`. | MUST | Section 5.1 |
| R16 | Presentation (redirect): Response encryption MUST use `direct_post.jwt`; same-device flow MUST be supported. | MUST | Section 5.1 |
| R17 | Presentation (DC API): Wallet MUST support Wallet Invocation via DC API; Verifier MUST use it. | MUST | Section 5.2 |
| R18 | Presentation (DC API): Wallet MUST support unsigned, signed, multi-signed requests. | MUST | Section 5.2 |
| R19 | SD-JWT VC: Compact serialization MUST be supported; `cnf` claim MUST conform. | MUST | Section 6.1 |
| R20 | SD-JWT VC: `status` claim (if present) MUST contain `status_list`. | MUST | Section 6.1 |
| R21 | SD-JWT VC: X.509 certificate-based key resolution MUST be supported. | MUST | Section 6.1.1 |
| R22 | SD-JWT VC: If cryptographic holder binding, KB-JWT MUST be present in presentation. | MUST | Section 6.1.1.1 |
| R23 | Digital signatures: All entities MUST support ECDSA P-256 SHA-256. | MUST | Section 7 |
| R24 | Hash algorithms: SHA-256 MUST be supported by all entities. | MUST | Section 8 |