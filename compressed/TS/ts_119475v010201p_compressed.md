# ETSI TS 119 475: Electronic Signatures and Trust Infrastructures (ESI); Relying party attributes supporting EUDI Wallet user's authorization decisions
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2026-03 | **Type**: Normative  
**Original**: [Available from ETSI Search & Browse Standards]

## Scope (Summary)
Defines policy and profile requirements for wallet‑relying party registration certificates (WRPRC) used to convey authorizations, entitlements, and intended purposes of wallet‑relying parties (WRPs) interacting with the European Digital Identity Wallet (EUDIW), in accordance with eIDAS Regulation (EU) No 910/2014 [i.1] and Commission Implementing Regulation (EU) 2025/848 [i.2]. Specifies mapping of WRP identification attributes between WRPAC and WRPRC, and recommendations for coordination between their providers.

## Normative References
- [1] ETSI EN 319 412‑1 – Certificate Profiles; Part 1: Overview and common data structures
- [2] ETSI EN 319 412‑2 – Certificate Profiles; Part 2: Certificates issued to natural persons
- [3] ETSI EN 319 412‑3 – Certificate Profiles; Part 3: Certificates issued to legal persons
- [4] ETSI EN 319 411‑1 – Policy and security requirements for TSPs issuing certificates; Part 1: General requirements
- [5] IETF RFC 5280 – Internet X.509 PKI Certificate and CRL Profile
- [6] IETF RFC 7519 – JSON Web Token (JWT)
- [7] IETF RFC 8392 – CBOR Web Token (CWT)
- [8] ISO 3166‑1 – Country codes
- [9] IETF RFC 5646 – Tags for Identifying Languages
- [10] ITU‑T X.520 – Selected attribute types
- [11] IETF RFC 5322 – Internet Message Format
- [12] IETF RFC 5341 – tel URI Parameter Registry
- [13] IETF RFC 8820 – URI Design and Ownership
- [14] IETF RFC 8089 – "file" URI Scheme
- [15] ISO 639:2023 – Codes for individual languages
- [16] ISO 8601‑1:2019 – Date and time representation
- [17] ETSI TS 119 411‑8 – Access Certificate Policy for EUDI Wallet Relying Parties
- [18] ETSI TS 119 182‑1 – JAdES digital signatures; Part 1
- [19] IETF RFC 9052 – CBOR Object Signing and Encryption (COSE)
- [20] IETF RFC 9360 – COSE: Header Parameters for Carrying and Referencing X.509 Certificates

## Definitions and Abbreviations
- **European digital identity wallet**: As defined in eIDAS Regulation [i.1]
- **National register of wallet‑relying parties**: Electronic register used by a Member State to publish information on registered WRPs (CIR (EU) 2025/848 [i.2])
- **Provider of WRPAC**: Natural/legal person mandated by a Member State to issue WRPACs (trust service provider)
- **Provider of WRPRC**: Natural/legal person mandated to issue WRPRCs (trust service provider)
- **Registrar of WRPs**: Body responsible for maintaining the list of registered WRPs
- **Wallet‑relying party (WRP)**: Relying party relying on wallet units for service provision
- **WRPAC**: Wallet‑relying party access certificate – certificate for electronic seals/signatures authenticating the WRP
- **WRPRC**: Wallet‑relying party registration certificate – data object describing intended use and requested attributes
- **Abbreviations**: CIR (Commission Implementing Regulation), CWT, DCQL, EAA, EUDIW, JWT, LEI, QTSP, TSP, VAT, WRP, WRPAC, WRPRC

## 4 General Concepts
### 4.1 Wallet‑Relying Parties Certificates
Two certificate types defined in CIR (EU) 2025/848 [i.2]:
- **WRPAC**: Issued exclusively to registered WRPs. Used for authentication and to ensure request integrity. Policy requirements for providers defined in ETSI TS 119 411‑8 [17].
- **WRPRC**: Where mandated by a Member State, provides information from national register including intended use and requested attributes. Complies with Annex V of [i.2]. All certificates issued by providers authorized under EU/national law and listed on trusted lists.

### 4.2 Wallet‑Relying Party Roles
Roles represent formal entitlements assigned to WRPs, expressed in WRPRCs (see Annex A for OIDs/URIs). EU‑level entitlements:
- Service_Provider, QEAA_Provider, Non_Q_EAA_Provider, PUB_EAA_Provider, PID_Provider, QCert_for_ESeal_Provider, QCert_for_ESig_Provider, rQSealCDs_Provider, rQSigCDs_Provider, ESig_ESeal_Creation_Provider.
Sub‑entitlements may be defined (e.g., payment service providers in A.3.1).

### 4.3 Wallet‑Relying Party Access Certificates (WRPACs)
Used to authenticate WRPs. Issued by authorized trust service providers. The present document does not define WRPAC policy (see ETSI TS 119 411‑8 [17]). WRPACs are X.509 certificates associated with a private key.

### 4.4 Wallet‑Relying Party Registration Certificates (WRPRCs)
Structured data objects describing intended use and attribute access scope. Formatted as signed JWT or CWT, signed with AdES B‑B. Trust service provider obligations defined in clause 6.

### 4.5 Registration and Access Certificate Relation
WRPAC and WRPRC are linked via the WRP identifier. WRPRC issuance should be based on WRPAC data. For intermediated transactions, the intermediary presents its own WRPAC; the WRPRC identifies the final WRP and includes intermediary indication (Annex I point 14 of [i.2]).

### 4.6 Certificate Issuance
#### 4.6.1 General Provisions
Each Member State maintains a national register with human‑readable and machine‑readable interfaces. Registrar processes applications. At least one provider of WRPAC authorized; WRPRC providers may be authorized separately.

#### 4.6.2 WRPAC and WRPRC Policies
Providers must be authorized/designated per Article 4(1) of [i.2]. Policy requirements for WRPRC in clause 6; for WRPAC in ETSI TS 119 411‑8 [17].

#### 4.6.3 Identity Proofing of WRPs
Before registration, registrar performs identity proofing per Article 6 of [i.2] and ETSI TS 119 461 [i.11]. Delegation allowed. WRPRC issuance does not require full identity proofing per issuance; it relies on prior verification. National register is authoritative source.

## 5 Certificate Profile Requirements
### 5.1 WRP Identification Attributes Matching
- **GEN‑5.1.1‑01**: WRPRC **shall** include identification attributes of WRP matching WRPAC.
- **GEN‑5.1.1‑02**: Before issuing, provider **shall** verify that identifier in WRPAC matches an identifier in WRPRC.
- **GEN‑5.1.1‑03**: If other attributes differ, linkage **shall** rely solely on matching identifier.
- **GEN‑5.1.1‑04**: If multiple identifiers in WRPRC, at least one **shall** correspond to identifier in WRPAC.

**5.1.2 Legal person mapping** – Table 1 maps register attributes (tradeName, legalName, identifier, country, etc.) to WRPAC and WRPRC fields.
- **GEN‑5.1.2‑01**: Table applies if certificate issued to legal person.
- **GEN‑5.1.2‑02**: If tradeName absent, commonName **shall** follow ETSI EN 319 412‑3 [3] LEG‑4.2.1‑8.

**5.1.3 Legal person semantic identifier mapping**
- **GEN‑5.1.3‑01**: organizationIdentifier **shall** follow ETSI EN 319 412‑1 [1] clause 5.1.4.
- **GEN‑5.1.3‑02**: Three initial characters **shall** follow Table 2 mapping (EOR, LEI, NTR, VAT, EXC).
- **GEN‑5.1.3‑03**: Identifier in WRPRC `sub` **shall** follow the same semantics.

**5.1.4 Natural person mapping** – Table 3.
- **GEN‑5.1.4‑01**: Table applies if certificate issued to natural person.
- **GEN‑5.1.4‑02**: If tradeName absent, commonName **shall** follow ETSI EN 319 412‑2 [2] NAT‑4.2.4‑15.

**5.1.5 Natural person semantic identifier mapping**
- **GEN‑5.1.5‑01**: serialNumber **shall** follow ETSI EN 319 412‑1 [1] clause 5.1.3.
- **GEN‑5.1.5‑02**: Three initial characters **shall** follow Table 4 (VATIN/TIN -> TIN).
- **GEN‑5.1.5‑03**: Identifier in WRPRC `sub` **shall** follow the same semantics.

### 5.2 WRPRC Profile Requirements
#### 5.2.1 Format
- **GEN‑5.2.1‑01**: **shall** be JWT [6] or CWT [7].
- **GEN‑5.2.1‑02**: **shall** comply with Annex V paragraph 3 of CIR (EU) 2025/848 [i.2].
- **GEN‑5.2.1‑03**: **shall** be signed by the provider of WRPRC.
- **GEN‑5.2.1‑04**: JWT **shall** be signed with JAdES B‑B [18].
- **GEN‑5.2.1‑05**: CWT **shall** be signed with AdES per RFC 9052 [19] and RFC 9360 [20].

#### 5.2.2 JWT Header Attributes
- **GEN‑5.2.2‑01**: Header **shall** include fields per Table 5: `typ` = rc‑wrp+jwt, `alg`, `x5c`.

#### 5.2.3 CWT Header Attributes
- **GEN‑5.2.3‑01**: Header **shall** include fields per Table 6: `typ` = rc‑wrp+cwt, `alg`, `x5chain`.

#### 5.2.4 Payload Attributes
- **GEN‑5.2.4‑01**: Payload **shall** include all fields provided by registry per Table 7 (name, sub_ln, sub_gn, sub_fn, sub, country, registry_uri, srv_description, entitlements, privacy_policy, info_uri, support_uri, supervisory_authority, policy_id, certificate_policy, iat, status).
- **GEN‑5.2.4‑02**: `sub` **shall** include identifier per clause 5.1.2/5.1.4 and match registered identifier.
- **GEN‑5.2.4‑03**: `entitlements` **shall** include at least one from Annex A.2.
- **GEN‑5.2.4‑04**: If entitlement includes Annex A.3 identifiers, it **shall** also include at least one from A.3.1.
- **GEN‑5.2.4‑05**: For attestation provider roles, payload **should** include `provides_attestations` per Table 8.
- **GEN‑5.2.4‑06**: For service provider, payload **shall** include `credentials` and `purpose` per Table 9.
- **GEN‑5.2.4‑07**: Payload **may** include optional fields per Table 10 (public_body, exp, intermediary).
- **GEN‑5.2.4‑08**: `exp` **shall** be ≤ 12 months after `iat`.
- **GEN‑5.2.4‑09**: If intermediary used, WRPRC **shall** include `act.sub` matching intermediary’s semantic identifier.

## 6 Policy Requirements for WRPRC
### 6.1 General Provisions
- **OVR‑6.1.1‑01**: General requirements of ETSI EN 319 411‑1 [4] clause 5.1 **shall** apply.
- **OVR‑6.1.2‑01**: Certification practice statement requirements of [4] clause 5.2 **shall** apply.
- **OVR‑6.1.2‑02**: If provider also issues WRPAC, it **shall** follow ETSI TS 119 411‑8 [17].
- **OVR‑6.1.3‑01**: WRPRC **shall** include certificate policy identifier: `0.4.0.19475.3.1`.
- **OVR‑6.1.3‑02**: Policy **shall** be referenced in each WRPRC in machine‑ and human‑readable format.
- **OVR‑6.1.4‑01/02**: Participants requirements of [4] clause 5.4 **shall** apply; provider **shall** include clear description of PKI hierarchy.
- **OVR‑6.2.1‑01**: Publication and repository responsibilities of [4] clause 6.1 **shall** apply.

### 6.2 Trust Service Providers Practice
#### 6.2.2 Identification and Authentication
- **REG‑6.2.2.1‑01**: Naming per clause 5.
- **REG‑6.2.2.2‑01**: Provider **shall** verify WRP listed in national register at issuance.
- **REG‑6.2.2.2‑02**: **shall** ensure information matches national register.
- **REG‑6.2.2.2‑03**: **shall** ensure WRP holds at least one valid WRPAC.
- **REG‑6.2.2.2‑04**: If registrar provides rules, provider **shall** comply.
- **REG‑6.2.2.2‑05**: If request from registrar, provider **may** rely on registrar’s identity proofing.
- **REG‑6.2.2.2‑06**: Provider **may** provide identity proofing for registrar.
- **REV‑6.2.2.3‑01**: Revocation request identification per [4] clause 6.2.4 **shall** apply.
- **REV‑6.2.2.3‑02/03/04**: Procedures for revocation and notifications **shall** be established.
- **REG‑6.2.2.3‑05/06/07/08**: Revocation requests only from registrar, WRP, or competent authority; authentication required; audit logs; processing without undue delay.

#### 6.2.3 Certificate Life‑Cycle
- **REG‑6.2.3.1‑01**: Application per [4] clause 6.3.1 **shall** apply.
- **REG‑6.2.3.2‑01**: Processing per [4] clause 6.3.2 **shall** apply.
- **GEN‑6.2.3.3‑01**: Issuance per [4] clauses GEN‑6.3.3‑01, -02, -05 **shall** apply.
- **OVR‑6.2.3.4‑01**: Acceptance per [4] clause 6.3.4 **shall** apply.
- **REG‑6.2.3.6‑01**: Before renewal, repeat verification of WRP attributes.
- **REV‑6.2.3.9‑01**: Revocation/suspension per [4] clause 6.3.9 **shall** apply.
- **REV‑6.2.3.9‑02/03/04/05/06/07**: Provider **shall** implement monitoring, receive updates from registrar, revoke on suspension/cancellation, provide revocation interface, allow descriptive reasons, revoke without delay when changes occur.
- **CSS‑6.2.3.10‑01**: Status services per [4] clause 6.3.10 **shall** apply.
- **CSS‑6.2.3.10‑02/03/04/05**: Status list publicly accessible, stable endpoint, update without delay, compression if used.
- **OVR‑6.2.4‑01**: Facility/management controls per [4] clause 6.4 **shall** apply.
- **OVR‑6.2.5‑01**: Technical security controls per [4] clause 6.5 **shall** apply.
- **GEN‑6.2.6.1‑01/02/03/04/05/06**: WRPRC **shall** comply with clause 5.2 profile, include policy id, unique identifier, status field with idx and uri, uniqueness, verifiable status list.
- **REV‑6.2.6.2‑01/02/03/04/05**: Status list **shall** support offline verification, compact array, each WRPRC referenced, semantics valid/revoked, signed.
- **OVR‑6.2.8‑01**: Business/legal matters per [4] clause 6.8 **shall** apply.
- **OVR‑6.2.9‑01**: Other provisions per [4] clause 6.9 **shall** apply.

## Annex A (Normative): WRP Identifiers
### A.1 OID Identifier
`id‑etsi‑wrpa‑entitlement = { itu-t(0) identified-organization(4) etsi(0) eudiwrpa(19475) entitlement(1) }`

### A.2 WRP Entitlement Identifiers
| Entitlement | Description | OID (id-etsi-wrpa-entitlement.X) | URI |
|-------------|-------------|----------------------------------|-----|
| Service_Provider | General service provider | 1 | https://uri.etsi.org/19475/Entitlement/Service_Provider |
| QEAA_Provider | Qualified TSP issuing QEAA | 2 | …/QEAA_Provider |
| Non_Q_EAA_Provider | TSP issuing non‑qualified EAA | 3 | …/Non_Q_EAA_Provider |
| PUB_EAA_Provider | Public sector body issuing EAA from authentic sources | 4 | …/PUB_EAA_Provider |
| PID_Provider | Provider of person identification data | 5 | …/PID_Provider |
| QCert_for_ESeal_Provider | QTSP issuing qualified e‑seal certificates | 6 | …/QCert_for_ESeal_Provider |
| QCert_for_ESig_Provider | QTSP issuing qualified e‑signature certificates | 7 | …/QCert_for_ESig_Provider |
| rQSealCDs_Provider | QTSP managing remote qualified e‑seal creation devices | 8 | …/rQSealCDs_Provider |
| rQSigCDs_Provider | QTSP managing remote qualified e‑signature creation devices | 9 | …/rQSigCDs_Provider |
| ESig_ESeal_Creation_Provider | Non‑qualified provider for remote signature/seal creation | 10 | …/ESig_ESeal_Creation_Provider |

### A.3 Service Provider Sub‑entitlements
#### A.3.1 Payment Service Provider Identifiers
- Account Servicing PSP: https://uri.etsi.org/19475/SubEntitlement/psp/psp-as
- Payment Initiation Service Provider: …/psp-pi
- Account Information Service Provider: …/psp-ai
- Payment Service Provider issuing card‑based instruments: …/psp-ic
- Unspecified PSP: …/psp/unspecified

## Annex B (Normative): Wallet‑Relying Party Attributes
### B.2 Attribute Classes
| Class | Key Attributes | Reference to CIR (EU) 2025/848 Annex I |
|-------|----------------|----------------------------------------|
| WalletRelyingParty | tradeName, supportURI, srvDescription, intendedUse, isPSB, entitlement, providesAttestations, supervisoryAuthority, registryURI, usesIntermediary | Points 2,7,8,9,10,11,12,13,14 |
| LegalEntity | legalPerson/naturalPerson (exclusive), identifier, postalAddress, country, email, phone, infoURI | Points 1,3,4,5,6,7 |
| LegalPerson | legalName, establishedBylaw (with Law class) | Point 1 |
| NaturalPerson | givenName, familyName, dateOfBirth, placeOfBirth | Point 1 |
| Identifier | type (URI from defined list), identifier | Point 3 |
| MultiLangString | lang (ISO 639), content | – |
| IntendedUse | purpose, privacyPolicy, createdAt, revokedAt, credential, intendedUseIdentifier | Points 8,9,10 |
| Policy | type (URI), policyURI | – |
| Credential | format, meta, claim | Points 9,13 |
| Claim | path, values | – |
| Law | lang, legalBasis | – |

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | WRPRC **shall** include identification attributes of WRP matching those in WRPAC | shall | GEN‑5.1.1‑01 |
| R2 | WRPRC **shall** be formatted as signed JWT or CWT and comply with Annex V of CIR 2025/848 | shall | GEN‑5.2.1‑01, -02 |
| R3 | WRPRC payload **shall** include all fields provided by registry as per Table 7 | shall | GEN‑5.2.4‑01 |
| R4 | Provider **shall** verify WRP is listed in national register and holds a valid WRPAC at issuance | shall | REG‑6.2.2.2‑01, -03 |
| R5 | Revocation requests **shall** only be accepted from registrar, WRP (if permitted), or competent authority | shall | REG‑6.2.2.3‑05 |
| R6 | Status list **shall** be publicly available, protected by digital signature, and support valid/revoked semantics | shall | CSS‑6.2.3.10‑02, REV‑6.2.6.2‑01/04/05 |

## Informative Annexes (Condensed)
- **Annex C (Registration Certificate example)**: Provides a decoded JWT example showing all mandatory and optional fields (name, sub, entitlements, status, credentials, intermediary, etc.) as an illustration of the WRPRC payload.
- **Annex D (WRP registration use cases)**: Describes four models for interaction between registrar and WRP certificate provider: Integrated (same entity), Registrar‑initiated issuance, RP‑initiated issuance post‑registration, and Provider‑assisted registration. Each model explains roles and responsibilities.
- **Annex E (Regulatory requirements for WRP certificate providers)**: Summarizes the legal basis for WRPAC and WRPRC attributes per CIR (EU) 2025/848 Annexes I, IV, V. Includes a comparison table (Table E.1) and a table of identification attributes (Table E.2). Explains that WRPRC is always presented with WRPAC; if no WRPRC, wallet retrieves data from national register.
- **Annex F (Change history)**: Lists versions: V1.1.1 (September 2025), V1.2.1 (January 2026) with editorial corrections.