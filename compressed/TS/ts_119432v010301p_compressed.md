# ETSI TS 119 432: Protocols for remote digital signature creation
**Source**: ETSI TC ESI | **Version**: V1.3.1 | **Date**: 2026-03 | **Type**: Technical Specification (Normative)
**Original**: RTS/ESI-0019432v131

## Scope (Summary)
Specifies protocols and interfaces for remote digital signature creation (AdES and digital signature values) where the signing key is held in a remote shared service. Covers distributed signature creation, authentication/authorization, and APIs based on CSC API and OASIS DSS-X. Includes profiles for EUDIW-based flows. Does not cover local signing or mandatory binding.

## Normative References
- [1] Cloud Signature Consortium Standard (v2.2.0.0): "Architectures and protocols for remote signature applications"
- [2] CSC Standard (v1.0.0): "Data model for remote signature applications"
- [3] CSC Standard (v1.0.0): "CSC data model bindings"
- [4] OASIS: "Digital Signature Service Core Protocols, Elements, and Bindings Version 2.0"
- [5] OASIS: "Digital Signature Service Metadata Version 1.0"
- [6] EN 419 241-1: "Trustworthy Systems Supporting Server Signing - Part 1: General System Security Requirements"
- [7] IETF RFC 8446: TLS 1.3
- [8] IETF RFC 7515: JSON Web Signature (JWS)
- [9] W3C: "XML Signature Syntax and Processing Version 1"
- [10] OpenID Foundation: "FAPI 2.0 Security Profile"
- [11] IETF RFC 7591: OAuth 2.0 Dynamic Client Registration Protocol
- [12] IETF RFC 7517: JSON Web Key (JWK)
- [13] OpenID Connect Relying Party Metadata Choices 1.0 (draft 04)
- [14] IETF RFC 7636: Proof Key for Code Exchange (PKCE)
- [15] IETF RFC 8414: OAuth 2.0 Authorization Server Metadata
- [16] IETF RFC 9110: HTTP Semantics
- [17] IETF RFC 6749: The OAuth 2.0 Authorization Framework
- [18] IETF RFC 9126: OAuth 2.0 Pushed Authorization Requests (PAR)
- [19] IETF RFC 6750: Bearer Token Usage
- [20] FIDO Alliance: CTAP
- [21] OpenID Connect Core 1.0 (errata set 2)
- [22] OpenID for Verifiable Presentations 1.0
- [23] W3C: "Digital Credentials, W3C Working Draft", 18 December 2025
- [24] IETF RFC 9207: OAuth 2.0 Authorization Server Issuer Identification
- [25] IETF RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)
- [26] IETF RFC 8725: JSON Web Token Best Current Practices
- [27] OASIS: SAML 2.0 Assertions and Protocols
- [28] OASIS: SAML 2.0 Profiles
- [29] IETF RFC 7522: SAML 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants
- [30] W3C: Web Authentication (WebAuthn) Level 3
- [31] IETF RFC 9101: JWT-Secured Authorization Request (JAR)

## Definitions and Abbreviations
Key terms (see clause 3.1):
- **AdES (digital) signature**: CAdES, PAdES, or XAdES signature.
- **Driving application (DA)**: Application that uses a SCASC or SSASC service to create a signature.
- **Relying party (RP)**: Entity that requests remote signature creation and relies on the result.
- **Remote signature creation device**: Used remotely from signer; provides control of signing operation on signer's behalf.
- **Server signing application (SSA)**: Application using a remote signature creation device to create a digital signature value.
- **Signature activation data (SAD)**: Data used to control a signature operation with high confidence under sole control of signer.
- **Signature activation module (SAM)**: Software using SAD to guarantee sole control.
- **Signature creation application (SCA)**: Creates AdES digital signature, relies on SCDev for signature value.
- **Signature creation device (SCDev)**: Configured software/hardware implementing signature creation data.
- **Signature creation service (SCS)**: TSP service implementing SCA and/or SSA.
- **Signing credential**: Set of signing key and corresponding certificate.
- **User agent**: Software acting on behalf of resource owner (signer) interacting with authorization server and DA.

Abbreviations (clause 3.3): API, AS, CSC, DA, DCQL, DPoP, DSS-X, DTBS, DTBSF, DTBSR, EUDIW, FAPI, JAR, JWS, JWT, OAuth, OIDC, OpenID4VP, OTP, PAR, PKCE, QES, QSCD, QTSP, RAR, RP, SAD, SAM, SCA, SCAL1/2, SCASC, SCDev, SCS, SCSP, SDO, SIC, SSA, SSASC, TSP, VP, WUA, etc.

## 4 Signature creation process, service decomposition
### 4.1 Process steps and data elements
- Figure 1 (derived from EN 319 102-1) shows process steps: SD -> SDR -> DTBS -> DTBSF -> DTBSR -> DSV -> SDO.
- Remote signature creation decomposes these steps across components.

### 4.2 Service main components and interfaces
- **SSASC**: Supports digital signature value creation. Input: DTBSR, output: DSV.
- **SCASC**: Supports AdES digital signature creation. Interacts with SSASC for DSV creation.
- **SCS**: TSP service implementing SCA and/or SSA.

### 4.3 Signature Creation Application
- **4.3.1**: Hashing of SD (SDR) can be done locally or by SCASC.
- **4.3.2**: DTBS composition and formatting create DTBSF from SDR and signed attributes.
- **4.3.3**: DTBS preparation: SCASC creates DTBSF, calculates hash, sends DTBSR to SSASC.
- **4.3.4**: SDO composer constructs final AdES format (enveloped/enveloping/detached).

### 4.4 Server Signing Application
- **4.4.1.1**: SSASC uses SCDev and secure authorization/activation process.
- **4.4.1.2 Signature activation**:
  - **SCAL1**: Low confidence; basic authentication; key activation can remain for a period.
  - **SCAL2**: High confidence; SAM enforces sole control via SAD; signature activation protocol.
- **4.4.1.3**: Signature creation performed by remote SCDev.

## 5 Authentication and authorization
### 5.1 Introduction
- Any driving application **shall** be authenticated when invoking a signature creation service. User authorization required for signature creation.

### 5.2 Service authorization
- **5.2.1**: DA **shall** adopt any available authorization mechanism from SCS.
- **5.2.2 HTTP Basic/Digest**:
  - Basic **should not** be used for qualified signatures; may be deprecated.
  - auth/login and auth/revoke APIs per CSC API [1] clause 11.2 and 11.3 **shall** apply.
- **5.2.3 OAuth 2.0**:
  - SCS may use OAuth 2.0. JWT **shall** be signed with strong algorithms.
  - oauth2/authorize, oauth2/pushed_authorize, oauth2/token, oauth2/revoke APIs per CSC API [1] clauses 8.2.2-8.2.5 **shall** apply.
  - PKCE, PAR, JAR are recommended.
- **5.2.4 Other mechanisms**: mTLS, HMAC, JWT assertions, SAML, SSH, challenge-response with QSCD, FIDO2/Passkey – alternatives considered.

### 5.3 Signatures creation authorization
- **5.3.1**: Two levels: SCAL1, SCAL2 (as per EN 419 241-1).
- **5.3.2 SCSP-managed authorization**:
  - credentials/authorize, credentials/authorizeCheck, credentials/extendTransaction, credentials/getChallenge APIs (CSC API [1] clauses 11.8-11.11) **shall** apply.
- **5.3.3 OAuth2-based authorization**:
  - oauth2/authorize, oauth2/pushed_authorize, oauth2/token, oauth2/revoke APIs (CSC API [1] clauses 8.2.2-8.2.5) **shall** apply for signatures authorization.

### 5.4 Credential creation authorization
- CSC API [1] only supports OAuth 2.0.
- oauth2/authorize, oauth2/pushed_authorize, oauth2/token, credentials/create APIs **shall** apply (clauses 8.2.2-8.2.4, 11.4).
- Subject data may be provided via RAR, access token claims, or token introspection.

### 5.5 Credential deletion authorization
- Requires authorization from credential owner or trusted DA. SCSP **should** inform owner.
- APIs: oauth2/authorize, oauth2/token, credentials/delete per CSC API [1] clauses 8.2.2, 8.2.4, 11.5.

## 6 Architectures and use cases for server signing
### 6.1 Introduction
- Architectural models based on credential protection and authorization mechanism. Governance remains with SCSP.

### 6.2 Credential protected by SCSP-managed authorization
- Flows in Figures 7-9: use credentials/authorize and signatures/signHash or signatures/signDoc.
- **Note**: Explicit authorization collects factors in DA environment; not suitable for SCAL2.

### 6.3 Credential protected by OAuth2
- Use OAuth2 authorization server. Flows in Figures 10-11.
- Signing credential selected via credentialID or signatureQualifier.

### 6.4 EUDIW architectures
- **6.4.1**: EUDIW can serve as authentication/authorization layer or as mediator (DA/SCA).
- **6.4.2**: EUDIW as auth/authz layer (Figures 12-19):
  - Key steps: document/hash transmission, signature authorization via EUDIW, signature creation request to QTSP, return of signed data.
  - Use OpenID4VP with custom URL scheme (openid4vp://) or Digital Credentials API.
  - Transaction data type identifier for QES approval: `https://cloudsignatureconsortium.org/2025/qes-approval`.
- **6.4.3**: EUDIW participating in signature creation process (Figures 20-22):
  - EUDIW coordinates AdES creation via SCASC (may be part of EUDIW or backend).
  - WRP registration and trust establishment required.
  - Presentation request includes data to be signed.
- **6.4.4 EUDIW registration and authentication**:
  - Authorization servers **shall** implement FAPI 2.0 and RFC 7591.
  - EUDIW **shall** register dynamically providing redirect_uris, jwks (including WUA public key), token_endpoint_auth_method=private_key_jwt, grant_types, response_types, software_statement.
  - EUDIW **shall** use Authorization Code Flow with PKCE, PAR with signed JAR.
  - EUDIW **shall** use DPoP for sender-constrained tokens.
  - SCS **should** accept DPoP proofs and **shall** validate them.
- **6.4.5 DA/SCA registration**:
  - Authorization server **shall** implement FAPI 2.0 and RFC 7591.
  - DA/SCA **shall** register with similar metadata, including client registration certificate.
  - Static registration also allowed for closed ecosystems.

## 7 Remote signatures creation service API
### 7.1 Introduction
- API based on CSC API [1] with additional components defined in tables.
- Tables use presence: M (mandatory), O (optional), C (conditional).

### 7.2 Service information API
- **shall** apply CSC API [1] clause 11.1.
- Response adds `oauth2FAPIsupport` boolean if FAPI 2.0 is supported.

### 7.3 Credentials list API
- **shall** apply CSC API [1] clause 11.6. Parameter `onlyValid` need not be supported.

### 7.4 Credentials info API
- **may** be implemented per CSC API [1] clause 11.7.

### 7.5 Hash(es) signing API
- **shall** apply CSC API [1] clause 11.13. Only synchronous mode **shall** be supported (parameters operationMode, validity_period, response_uri not needed).

### 7.6 Document(s) signing API
- **shall** be applied and **should** be implemented per CSC API [1] clause 11.14. Only synchronous mode; signature_format values "C", "X", "J" and conformance_level "AdES-B", "AdES-T", "AdES-LT", "AdES-LTA" need not be supported.

### 7.7 Signature(s) creation polling API
- **needs not be supported** unless asynchronous mode supported. If supported, apply CSC API [1] clause 11.15.

### 7.8 Credentials creation API
- **shall** apply CSC API [1] clause 11.4.
- SCS **shall** support subjectData parameter and also receiving subject data via RAR or access token claims.
- Standard OIDC claims **shall** be collected: given_name, family_name, gender, birthdate, address:country. Additional claims **should** or **may** be collected.

### 7.9 Credentials deletion API
- **shall** be applied and **may** be implemented per CSC API [1] clause 11.5. Output: HTTP 204.

## 8 Remote signatures creation service API based on OASIS DSS-X
### 8.1 Introduction and General Provisions
- DSS-X profile of the present document. HTTP POST binding recommended. TLS **should** supply security base layer.
- Service metadata **shall** provide details on authentication/authorization mechanisms per clauses 8.2 and 8.3.

### 8.2 Service information API
- Metadata per OASIS DSS-X [5] clause 3.2 and discovery per clause 4 of [5] **shall** apply.

### 8.3 Credentials list API
- DSS-X does not provide specific API; AuthInfo element can supply general info. Service metadata **shall** indicate supported approaches for signer certificate exposure.

### 8.4 Credentials info API
- See clause 8.3.

### 8.5 Hash(es) signing API
- SignRequest with DocumentHash variant **shall** apply. KeySelector component **shall** apply when signing key not implicit.

### 8.6 Document(s) signing API
- SignRequest with Document variant **shall** apply; TransformedData variant admissible. KeySelector **shall** apply when needed.

### 8.7 Signature(s) creation polling API
- PendingRequest element **shall** apply for asynchronous polling.

### 8.8 Credentials creation API
- Not applicable in DSS-X profile; certificate creation is implicit in SignRequest for short-term certificates.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Driving application shall be authenticated when invoking SCS. | shall | 5.1 |
| R2 | DA shall adopt any authorization mechanism available from SCS. | shall | 5.2.1 |
| R3 | auth/login, auth/revoke APIs (CSC API clauses 11.2, 11.3) shall apply. | shall | 5.2.2 |
| R4 | oauth2/authorize, oauth2/pushed_authorize, oauth2/token, oauth2/revoke APIs (CSC 8.2.2-8.2.5) shall apply for OAuth 2.0. | shall | 5.2.3, 5.3.3 |
| R5 | JWT shall be signed with strong algorithms; SCS shall trust issuer's public key securely. | shall | 5.2.3 |
| R6 | credentials/authorize, credentials/authorizeCheck, credentials/extendTransaction, credentials/getChallenge APIs (CSC 11.8-11.11) shall apply for SCSP-managed authorization. | shall | 5.3.2 |
| R7 | Authorization servers shall implement FAPI 2.0 Security Profile and RFC 7591 for EUDIW registration. | shall | 6.4.4.2, 6.4.5.2 |
| R8 | EUDIW shall register dynamically with required metadata (redirect_uris, jwks including WUA public key, token_endpoint_auth_method=private_key_jwt, etc.). | shall | 6.4.4.2 |
| R9 | EUDIW shall use Authorization Code Flow with PKCE, PAR with signed JAR. | shall | 6.4.4.3 |
| R10 | EUDIW shall use DPoP for sender-constrained tokens; SCS shall validate DPoP proofs. | shall | 6.4.4.4 |
| R11 | SCS API info, credentials/list, hash signing, document signing, credential creation APIs (clauses 7.2-7.6, 7.8) shall be applied as specified. | shall | 7 |
| R12 | Document signing API should be implemented (shall for synchronous). | shall/should | 7.6.1 |
| R13 | Credentials deletion API shall be applied and may be implemented. | shall/may | 7.9.1 |
| R14 | For DSS-X profile: SignRequest with DocumentHash or Document variants shall apply; KeySelector shall apply when needed. | shall | 8.5, 8.6 |
| R15 | Service metadata shall be provided per OASIS DSS-X Metadata [5]. | shall | 8.2.1 |
| R16 | In Annex A: RP shall use OpenID4VP with response_type=vp_token; format identifier shall be https://cloudsignatureconsortium.org/2025/x509; transaction_data type shall be https://cloudsignatureconsortium.org/2025/qes. | shall | A.3, A.6.2, A.6.3, A.6.4 |
| R17 | In Annex B: SCSP shall use OpenID4VP; transaction_data type for approval shall be https://cloudsignatureconsortium.org/2025/qes-approval; qesApprovalRequest shall include signatureCreationApproval. | shall | B.4, B.5, B.6.2 |
| R18 | In Annex C: authentication/authorization should be performed outside SCS using high-assurance mechanisms; authorization tokens should embed DTBS hashes, credential IDs, signature parameters; FAPI 2.0 should be adopted for EUDIW clients; all SCS API calls should be authenticated with OAuth access tokens. | should | C.2-C.7 |

## Informative Annexes (Condensed)
- **Annex A (normative)**: OpenID4VP EUDIW-centric signing flow profile. Defines how RP requests QES from EUDIW via OpenID4VP using dcql_query and transaction_data (qesRequest). Profile covers request construction, response handling (inline or out-of-band), security/privacy requirements, and conformance checklist for RP.
- **Annex B (normative)**: EUDIW QES creation approval profile. Specifies how QTSP's remote SCS requests approval from EUDIW using OpenID4VP. Defines qesApprovalRequest and qesApproval data structures, including signatureCreationApproval for document digests. Covers verification and authorization at AS/SAM.
- **Annex C (normative)**: Specific recommendations for qualified signatures/seals creation. Provides formal recommendations for separation of responsibilities, strong binding between consent and DTBS, use of FAPI 2.0 for EUDIW clients, and SCS API security (OAuth access tokens, DPoP, nonce validation).
- **Annex D (informative)**: Change history summarizing versions 1.1.1, 1.1.2, 1.2.13, and 1.3.1 with CR descriptions.