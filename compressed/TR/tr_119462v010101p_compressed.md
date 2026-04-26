# ETSI TR 119 462 V1.1.1: Wallet interfaces for trust services and signing
**Source**: ETSI | **Version**: V1.1.1 | **Date**: March 2026 | **Type**: Informative Technical Report
**Original**: DTR/ESI-0019462

## Scope (Summary)
This Technical Report provides an overview and analysis of interfaces enabling interactions between the European Digital Identity Wallet (EUDIW) and trust service providers, covering identity proofing, attribute issuance, electronic signature creation (local and remote), and other trust services. It identifies existing specifications, highlights gaps, and points to areas for further standardization to ensure secure, interoperable implementations.

## Normative References
Not applicable (the present document is informative).

## Definitions and Abbreviations
- **Certification Authority (CA)**: authority trusted by one or more users to create and assign certificates (see ETSI TS 319 411‑1 [i.11]).
- **EUDIW**: European Digital Identity Wallet.
- **PID**: Person Identification Data.
- **EAA**: Electronic Attestation of Attributes.
- **QES**: Qualified Electronic Signature.
- **QSeal**: Qualified Electronic Seal.
- **QTSP**: Qualified Trust Service Provider.
- **SCSP**: Signature Creation Service Provider.
- **SCA**: Signature Creation Application.
- **SAD**: Signature Activation Data.
- **WSCD**: Wallet Secure Cryptographic Device.
- **WUA**: Wallet Unit Attestation.
- Other abbreviations as defined in ETSI TS 119 401 [i.10], ETSI TS 119 431‑1 [i.12], ETSI TS 119 431‑2 [i.13], ETSI TS 119 471 [i.14].

## 4 General Concepts

### 4.1 Digital Identity Wallet

#### 4.1.1 European Digital Identity Wallet
The EUDIW is an electronic identification means under an EU‑recognized scheme enabling users to manage identity data and interact with trust services online/offline. Per Article 5a(4)(a) of eIDAS Regulation [i.1], the user may securely request, obtain, select, combine, store, delete, share, and present PID and EAAs under sole control; authenticate to relying parties with selective disclosure; and create QES/QSeal. Interaction with TSPs covers identity proofing, EAA issuance, and remote signature/seal creation.

#### 4.1.2 Digital Identity Wallet basic architectural components
Main components per ARF [i.4]: Wallet Unit (WU), Wallet Secure Cryptographic Device (WSCD), Wallet Secure Cryptographic Application (WSCA), PID Provider, EAA Providers, Signature Creation Service Provider (SCSP), and Presentation/Access Interfaces.

### 4.2 Wallet interfaces

#### 4.2.1 Interfaces defined in eIDAS Regulation
Table 1 (condensed):

| Interface | Description | Article | ARF Ref |
|-----------|-------------|---------|---------|
| EUDIW ↔ TSP (Issuance) | Issuance of PID, (Q)EAA, certificates | Art 5a(5)(a)(i) | 4.6.5, 6.6.2, Annex A.2.3 |
| EUDIW ↔ RP (Request/Validation) | RP requests/validates PID/EAA | Art 5a(5)(a)(ii) | 6.6.3.6 |
| EUDIW → RP (Presentation/Sharing) | Presentation with selective disclosure | Art 5a(5)(a)(iii) | 6.6.3, OIA_01, OIA_05-06 |
| EUDIW → UI (Trust Mark & Consent) | Display EU Trust Mark, consent | Art 5a(5)(a)(iv) | 6.5.3.6, DASH_09(b) |
| EUDIW ↔ Onboarding Source | Secure onboarding with high‑assurance eID | Art 5a(5)(a)(v) | 6.6.2.6, ISSU_05 |
| EUDIW ↔ EUDIW (P2P) | Secure peer‑to‑peer data sharing | Art 5a(5)(a)(vi) | 6.6.4 |
| EUDIW → RP (RP Authentication) | Authenticate and validate RP | Art 5a(5)(a)(vii‑viii) | 6.6.3.2 |
| EUDIW → Authorities (Erasure) | Erasure requests and reports | Art 5a(5)(a)(ix‑x) | 6.6.3.13 |
| EUDIW → Signature/Seal Provider | Create QES/QSeal | Art 5a(a)(xi) | 2.4, 3.9, Annex A.2.3 |
| EUDIW ← User | Verify authenticity/validity | Art 5a(8)(a) | 6.5.2.2 |

#### 4.2.2 Interfaces defined in Commission Implementing Regulations (CIRs)
Table 2 (condensed):

| Interface | Description | CIR Article | ARF Ref |
|-----------|-------------|-------------|---------|
| EUDIW ← PID/EAA Provider | Issue PID/EAA with revocation support | CIR 2024/2977 Art 3‑5 | 6.6.2, 6.6.5.4 |
| EUDIW → PID/EAA Provider | Provide WUA before credential issuance | CIR 2024/2977 Art 3 | 6.6.2.3.1 |
| EUDIW ↔ WSCD | Use secure cryptographic hardware | CIR 2024/2979 Art 4‑6 | 4.3.2, 4.5 |
| EUDIW ↔ RP | Authenticate RP, selective disclosure, offline sharing | CIR 2024/2982 Art 5; CIR 2024/2979 Art 8‑10 | 4.2.4, 6.6.3.2 |
| EUDIW Logging | Log all transactions with RP/TSP | CIR 2024/2979 Art 9 | Annex 2 Topic 19 |
| EUDIW Disclosure Control | Enforce embedded policies | CIR 2024/2979 Art 10 | 6.6.2.7 |
| EUDIW ↔ QES/QSeal Engines | Generate qualified signatures/seals | CIR 2024/2979 Art 11‑12 | 2.4, 4.3.3 |
| EUDIW ← RP | Verify RP registration & request | CIR 2025/848; CIR 2024/2982 Art 3 | 6.4.2, 6.4.3 |
| EUDIW ← Intermediaries | Display intermediary, enforce transparency | CIR 2025/848; CIR 2024/2982 Art 3 | 3.11, 6.6.3.4 |

#### 4.2.3 Interfaces defined in ARF
Table 3 (condensed):

| Interface Name | Description | External Actor | Standards/References |
|----------------|-------------|----------------|----------------------|
| Request & Receive PID | Identity proofing, PID issuance | PID Provider | ARF 3.4, Annex 2 Topic 10; CIR 2024/2977; ISO 18013‑5; SD‑JWT VC; OpenID4VCI |
| Request & Receive EAA/QEAA | Attestation attributes | (Q)EAA Provider | ARF 3.6, 3.8, Topics 10,12; OpenID4VCI; SD‑JWT VC; W3C VCDM |
| Request & Receive PuBEAA | Public‑sector EAAs | Public body EAASP | Similar as above |
| Signature/Seal Creation Request | Invoke QES via WSCD or remote QSCD | SCSP/QTSP | ARF 3.9, Topic 16; CSC API; ETSI signature format standards; EN 419 241‑1; ETSI TS 119 431‑1/‑2 |
| Relying Party Authentication & Consent | Authenticate RP, collect consent | Relying Party | ARF 6.6.3.2, Topic 6; ISO 18013‑5; OpenID4VP |
| Revocation and Validity Checking | Check status of PID/EAA | Revocation/Validation Services | ARF 6.6.3.7, Topic 7; ETSI EN 319 411‑1/‑2 |

Other interfaces (Wallet Provider, User Interface, Secure Cryptographic Interface, WSCA‑to‑WSCD) are not specified in this document.

### 4.3 Wallet interfaces for trust services
Table 4 (requirements for TSPs interacting with EUDIW):

| Requirement | Description | ARF Source |
|-------------|-------------|------------|
| User Identification | TSPs shall identify holder using PID and/or EAA. | 6.6.2, 6.6.3 |
| User Consent | All issuance/signing/delivery based on explicit user consent collected via EUDIW. | 5.6.2, 6.6.3.5, Annex 2 Topic 6 |
| Interoperable and Secure Interfaces | TSPs shall support standard protocols (OpenID4VP, OpenID4VCI, ISO 18013‑5) with mutual auth, selective disclosure, device binding. | 4.4.3.4, 5.6.1, 5.6.2, 5.3.2‑5.3.4 |
| Validation of EUDIW and Device | TSPs shall verify Wallet Unit Attestation (WUA) before issuing credentials. Attestations bound to WSCD where applicable. | 6.6.2.3, 6.6.2.4, Annex 2 Topics 9,10 |
| EAA Delivery and Cryptographic Binding | EAAs/certificates delivered securely, bound to user/device via cryptographic references. | 6.6.2.3.3, 5.6.2, 6.6.2.6 |
| Revocation and Status Management | TSPs shall provide revocation/suspension mechanisms. EUDIW queries status securely. | 6.6.5.4, Annex 2 Topic 7 |
| Audit, Logging, and Notifications | Interactions logged. TSPs report events to authorities per CIR 2024/2980, 2025/848. | 6.6.3.13, Annex 2 Topic 19, CIR 2024/2979 Art 9 |
| Trust Framework Participation | TSPs listed in national/European trust lists. | 3.5, 6.3.2.2‑6.3.2.4, 6.4.2‑6.4.3 |

Table 5 (primary interfaces EUDIW ↔ TSP):

| ID | Name | Description | Clause | Supporting Standards |
|----|------|-------------|--------|---------------------|
| IN_RP_1 | Online authentication interface | TSP acting as RP requests PID/EAA for identity validation or attribute request. | 5.2 | ETSI TS 119 461, 119 472‑1/‑2 |
| IN_RP_2 | Request for signature interface | RP initializes signing process, receives SCA & authentication info. | 5.3 | ETSI TS 119 472‑1/‑2, 119 432, EN 319 102‑1 |
| IN_TSP_1 | New attributes EAA handover | TSP issuing EAA during handover. | 6.4 | ETSI TS 119 472‑3 |
| IN_TSP_2 | Remote signature creation | Enables signature creation with remote service. | 7.4 | EN 319 102‑1, TS 119 431‑2, TS 119 432 |
| IN_TSP_3 | New certificate handover | Handover of signature certificate. | 7.5 | TS 119 432 |
| IN_QSCD_LOCAL | Local signature creation | Signature creation with local keys. | 7.4 | Out of scope |
| IN_SCA | Signature creation process | Handling signing attributes and certificate to SCA. | 7.3 | EN 319 102‑1 |

### 4.4 Wallet interfaces for signature creation
The EUDIW supports QES/QSeal via local QSCD or remote QSCD operated by QTSP. Key requirements: support secure user authentication, ensure qualified certificate bound to QSCD, support PAdES (mandatory) and optionally XAdES, CAdES, JAdES, ASiC. Signature initiation involves user preview, consent, and confirmation. Models: full SCA integration, redirection to external SCA, EUDIW as SIC for SAD generation (SCAL2 per EN 419 241‑1), EUDIW as authentication component.

## 5 Interface for authentication and identification

### 5.1 Identity proofing
QTSPs shall verify identity (and specific attributes) of natural/legal person before issuing qualified certificate or qualified EAA. Supporting standards: ETSI TS 119 461 [i.40] (identity proofing), ETSI TS 119 472‑1 [i.41] (EAA profile).

### 5.2 Interface for online identification and authentication
This interface enables a Relying Party (RP), which may also be a TSP, to request and receive PID/EAA from the EUDIW for identity validation or attribute‑based access. Core pattern:
- **Request**: RP sends authenticated presentation request.
- **Authentication**: EUDIW authenticates RP Instance; user informed.
- **Consent**: EUDIW displays purpose, legal basis, data categories, RP identity.
- **Presentation**: Upon approval, EUDIW returns requested attributes with selective disclosure.

Per ARF [i.4], OpenID4VP [i.26] is the preferred protocol (based on OAuth 2.0 RFC 6749, adapted for Verifiable Credentials). Key components: Presentation Request (signed JSON), Verifiable Presentation (JWT/SD‑JWT VC), Response Binding.

Security and Privacy Measures:
- Mutual Authentication: RP uses WRP certificate (CIR 2025/848).
- User Consent: EUDIW **shall** obtain explicit consent before presenting data.
- Selective Disclosure: Supported via SD‑JWT or mDL containers.
- Audit and Logging: All presentations logged (CIR 2024/2979 Art 9).

Supporting standards: ETSI TS 119 472‑1, 119 472‑2, OpenID4VP, ETSI TS 119 411‑8, ETSI TS 119 475.

### 5.3 Interface for request for signature
This interface allows an RP to initiate a digital signature request via the EUDIW. It does **not** perform the signature itself but initiates the workflow. It reuses the OpenID4VP‑based request structure from clause 5.2, adding signature‑specific elements: signature metadata (e.g., document hash, document ID), signature policy references (e.g., AdES type, legal value), optional request for qualified signature creation via remote or local QSCD. Depending on deployment, may pass signed metadata to external SCA or activate internal SCA module.

Supporting standards: ETSI TS 119 472‑2, OpenID4VP, ETSI TS 119 432, EN 319 102‑1, CSC API [i.32].

## 6 Interface for EAA issuance

### 6.1 Interface description
The EUDIW ↔ TSP (issuing EAAs) interface relies on OpenID4VCI [i.25] profiled for high assurance (HAIP [i.24]), extended for EUDIW requirements: Wallet Unit Attestation (WUA), signed Issuer Metadata, binding to wallet‑controlled keys. Supports Authorization Code Flow and Pre‑Authorized Code Flow. Profile and interface specified in ETSI TS 119 472‑3 [i.43]; formats in ETSI TS 119 472‑1 [i.41]. Building blocks include:
- Issuer Metadata (signed JWS with x5c, credential configuration, access certificate chain).
- Flows: Credential Offer, Pushed Authorization Request, Token Request, Credential Request/Response, Notification.
- Support for EAA formats including X.509 Attribute Certificate‑based EAAs.

Related standards: ETSI TS 119 471 (EAASP policy/security), ETSI EN 319 411‑1/‑2 (certification policies), ETSI TS 119 411‑8 (Access Certificates), ETSI TS 119 475 (Registration Certificates), ISO/IEC 23220‑3 (issuance phase).

### 6.2 Wallet user identification
User identification and attribute validation shall be performed per clause 5. The TSP **may** leverage previously issued attributes and, where necessary, obtain additional attributes from authoritative sources. Presentations via clauses 5.1 and 5.2 **may** be used before issuance.

### 6.3 Issuer discovery
Discovery via Issuer Metadata (JWS) retrieved and validated by the wallet. The protected header carries the issuer's access certificate chain (x5c); the body enumerates supported credential configurations, formats, and optional registration certificate information (issuer_info). This enables the wallet to authenticate the issuer and prepare correct requests. Supporting standards: OpenID4VCI [i.25], HAIP [i.24], ETSI TS 119 472‑3 [i.43].

### 6.4 Electronic Attestation of Attribute issuance
Issuance follows OpenID4VCI [i.25] profile, supporting Authorization Code and Pre‑Authorized Code flows. For issuer‑started process, Credential Offer sent to EUDIW, then PAR, Authorization Request, Token Request, Credential Request (proving possession of keys to which EAAs will be bound).

### 6.5 Electronic Attestation of Attribute lifecycle management
- Revocation and status: Signalled via EAA format mechanisms and ecosystem policies. Wallets shall process status and embedded disclosure policies (EDP) when presenting.
- Renewal and refresh: Refresh tokens **may** be used subject to issuer risk assessment. Issuers **should** evaluate attribute sensitivity before enabling refresh.

Supporting standards: ETSI TS 119 471 [i.14], ETSI TS 119 472‑3 [i.43], OpenID4VCI [i.25], HAIP [i.24] (recommends refresh token usage).

## 7 Interfaces for the creation of an electronic signature

### 7.1 Interface components

#### 7.1.1 Functional model
Uses Signature Creation Environment (SCE) model per EN 319 102‑1 [i.16]: signer, Driving Application (DA), Signature Creation System (SCS) comprising Signature Creation Application (SCA) and Signature Creation Device (SCDev). Figure 1 shows data flow between EUDIW and SCE. Four basic functions (can be implemented via multiple interactions or single interaction, often using EAA Presentation):
- **A**: Signing initiation
- **B**: Signature attributes
- **C**: Signature activation
- **D**: Identity data

Detailed analysis of extensions in Annex B.

### 7.2 Signing initiation interface
The signer, using the EUDIW, provides the DA with instructions for selecting signing method (choice of SCA). The DA prepares the document and initiates signing flow with SCA. If SCA preselected, initiation may be implicit. Supporting standards: OpenID4VP [i.26] (transaction data), ETSI TS 119 432 [i.15].

### 7.3 Signature attributes interface
The signer, using the EUDIW, provides signature attributes to the SCA, which collects and assembles them with SD(R) and certificate identifier into DTBS. ETSI TS 119 479‑3 [i.45] (under development) addresses EAA within AdES signatures. Supporting standards: OpenID4VP, ETSI TS 119 472‑1/‑2, ETSI TS 119 412‑6.

### 7.4 Signature activation interface
The signer authenticates to the SCA using the EUDIW; the SCA then initiates Signature Activation with the SSA controlling SCDev. The EUDIW acts as SIC and runs SAP with SAM to generate SAD, which SAM verifies to enable SCDev. Supporting standards: OpenID4VP, ETSI TS 119 432, ETSI TS 119 431‑1/‑2, CSC API [i.32].

### 7.5 Identity data interface
EUDIW provides signer's identity data for just‑in‑time certificate issuance (e.g., one‑time signing key). Interfaces described in clauses 5.2 and 5.3. Supporting standards: ETSI TS 119 431‑1/‑2, ETSI TS 119 461.

## 8 Wallet interface for other trust services

### 8.1 General provisions
Trust services **shall** use EUDIW for user identification and authentication, utilizing PID or specific EAAs. Levels of Assurance may vary. Trust services **may** define and issue their own EAAs for authentication. Annex A provides open list of use cases.

## Requirements Summary
*Note: As this is an informative Technical Report, there are no normative "shall" requirements except where referenced from other standards. Key "shall" statements within this document (derived from ARF, eIDAS, CIRs) are captured above. Below is a summary of the main interface requirements.*

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | EUDIW shall support issuance interface for PID, (Q)EAA, certificates. | Derived from eIDAS Art 5a(5)(a)(i) | Clause 4.2.1 |
| R2 | EUDIW shall obtain explicit user consent before presenting any data. | Derived from eIDAS Art 5a(5)(a)(iv) and ARF 6.6.3.5 | Clause 5.2 |
| R3 | TSPs shall verify Wallet Unit Attestation (WUA) before issuing credentials. | Derived from ARF 6.6.2.3, 6.6.2.4 | Clause 4.3 |
| R4 | EUDIW shall support PAdES signature format (mandatory); XAdES, CAdES, JAdES, ASiC optional. | Derived from clause 4.4 | Clause 4.4 |
| R5 | EUDIW shall log all transactions with RP/TSP. | CIR 2024/2979 Art 9 | Clause 4.2.2 |
| R6 | EUDIW shall authenticateRP before data sharing. | eIDAS Art 5a(5)(a)(vii‑viii) | Clause 4.2.1 |
| R7 | TSPs shall provide revocation/suspension mechanisms for EAAs and certificates. | ARF 6.6.5.4, Annex 2 Topic 7 | Clause 4.3 |
| R8 | Issuance interface shall use OpenID4VCI profiled for high assurance (HAIP). | Clause 6.1 | Clause 6 |
| R9 | Remote signature activation shall generate SAD compliant with ETSI TS 119 431‑1. | Clause B.1.4 | Annex B |
| R10 | EUDIW acting as SIC shall generate SAD or facilitate authentication per EN 419 241‑1 SCAL2. | Clause B.1.4 | Annex B |

## Informative Annexes (Condensed)

### Annex A: List of use cases for the interaction of the EUDIW with trust services
- **A.1**: EAAs enable authentication/authorization to specific trust services (e.g., time‑stamping, payment for certificate issuance).
- **A.2**: Initiation of Registered Delivery Service (RDS) – EUDIW holder as receiver: EAAs initialize the process.
- **A.3**: Initiation of RDS – EUDIW holder as sender: EAAs initialize the process for sending.

### Annex B: Analysis of optional extensions supporting digital signature creation with EUDIW
- **B.1.1‑B.1.5**: Describes functional model, four interfaces (signing initiation, signature attributes, signature activation, identity data), generic scenarios, and four remote signature creation models: WalletApp_SADGen (EUDIW generates SAD directly), RemoteApp_SADGen (SCA remote, EUDIW generates SAD), WalletApp_Auth (EUDIW authenticates to Auth Server, SAD generated externally), RemoteApp_Auth (both SCA and Auth Server remote). Each model includes supporting component interactions and standards.
- **B.2.1‑B.2.6**: Covers certificate issuance for remote signature: local keys, long‑term certificates with EUDIW authentication, one‑time signing key based on short‑term certificates (identity data provided by EUDIW). Specifies certificate information in EAA (SC_EAA), EAA as authenticator, and inclusion of EAA as signing attribute in AdES signatures (EUROPEAN DIGITAL IDENTITY WALLET can provide EAAs to SCA acting as RP). Standards referenced: ETSI TS 119 431‑1/‑2, EN 319 411‑1/‑2, ETSI TS 119 472‑1/‑2, OpenID4VP.