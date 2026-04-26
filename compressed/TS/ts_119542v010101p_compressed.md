# ETSI TS 119 542: Use of EU Digital Identity Wallets and electronic signatures for identification with Smart Contracts
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2025-10 | **Type**: Normative Technical Specification
**Original**: DTS/ESI-0019542

## Scope (Summary)
Specifies the use of EU Digital Identity Wallets and advanced/qualified electronic signatures/seals (implemented as digital signatures) conforming to eIDAS (Regulation (EU) No 910/2014 as amended by [i.3]) for identification of natural or legal persons across Smart Contract lifecycle phases, addressing needs from ETSI TR 119 540 [i.1].

## Normative References
- [1] ETSI EN 319 162-1: ASiC; Part 1: Building blocks and ASiC baseline containers
- [2] ETSI EN 319 132-1: XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures
- [3] ETSI EN 319 122-1: CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures
- [4] ETSI EN 319 102-1: Procedures for Creation and Validation of AdES Digital Signatures; Part 1: Creation and Validation
- [5] ETSI TS 119 102-2: Procedures for Creation and Validation of AdES Digital Signatures; Part 2: Signature Validation Report
- [6] ETSI TS 119 182-1: JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures
- [7] W3C® Recommendation 11 April 2013: XML Signature Syntax and Processing. Version 1.1

## Informative References
- [i.1] ETSI TR 119 540: Standardisation requirements for Smart Contracts based on electronic ledgers
- [i.2] ISO/IEC 18013-5:2021: Personal identification — ISO-compliant driving licence — Part 5: Mobile driving licence (mDL) application
- [i.3] Regulation (EU) 2024/1183 (eIDAS amendment, establishing European Digital Identity Framework)
- [i.4] ETSI TS 119 472-2: Profiles for Electronic Attestation of Attributes; Part 2: Profiles for EAA/PID Presentations to Relying Party
- [i.5] Commission Implementing Regulation (EU) 2024/2977 (rules for person identification data and electronic attestations for EUDI Wallets)

## Definitions and Abbreviations
- **Terms**: Per ETSI TR 119 540 [i.1] (no additional terms defined).
- **Abbreviations**: ASiC (Associated Signature Container), CMS, EAA (Electronic Attestation of Attributes), eIDAS (electronic IDentification, Authentication and trust Services – as per Regulation 910/2014 amended by 2024/1183), EUDI (EUropean Digital Identity), ISO, JSON, JWS, MIME, OID, PID (Personal Identification Data), SC (Smart Contract), SCP (Smart Contract Provider), SPO (Service Provision Option), VM (Virtual Machine), XML.

## Modal Verbs Terminology
In this document, "shall", "shall not", "should", "should not", "may", "need not", "will", "will not", "can", "cannot" are interpreted per clause 3.2 of ETSI Drafting Rules. "must" and "must not" are not allowed except in direct citation.

## 4 Roles, objects and signatories in Smart Contracts lifecycle

- The Smart Contract life cycle has three phases: Production, Deployment, Execution.
- The following objects **shall be signed** by designated entities:

| Phase | Object | Signatory |
|-------|--------|-----------|
| Production | SC Language Specification + SC Language Specification Policy | SC Language Publisher |
| Production | SC Compiler + SC Compiler Specification Policy | SC Compiler Publisher |
| Production | SC Virtual Machine + SC Virtual Machine Policy | SC Virtual Machine Publisher |
| Production | SC Package (source code, byte code, policies, legal text, documentation) | SC Publisher |
| Production | Evidence of agreement by SC parties (each party signs acceptance of SC terms and SC Provider terms) | Each SC party |
| Deployment | Validation report of ASiC-E container (from SC Publisher) | SC Deployer |
| Deployment | Evidence of Smart Contract deployment | SC Deployer |
| Execution | Signed execution report (after SC execution) | SC Provider |

- The SC Deployer **shall** validate the ASiC-E container before deployment.
- The SC Provider **shall** validate the signature on the deployment evidence before any execution.
- The SC Provider and SC User **shall** authenticate each other before each execution.

## 5 AdES signatures profiles

### 5.1 Introduction
- If several detached data objects need to be signed, ASiC-E containers with CAdES or XAdES **shall** be used.
- Otherwise standalone CAdES, JAdES, or XAdES **shall** be used.
- This clause defines profiles for (C/J/X)AdES signatures (standalone or inside ASiC-E). These profiles **shall** be referenced in clauses 6, 9, and 10.
- JAdES inclusion in ASiC containers is not yet standardized (NOTE 1).

### 5.2 Tables for defining AdES profiles
Tables contain these columns: `<AdES signature type> components/services`, `Presence`, `Cardinality`, `Additional notes and requirements`. The meaning of presence values and cardinality are defined. Absence of a component means "shall not be present" (cardinality 0). Mandatory base components are always present. Non-mentioned optional components may be present unless forbidden.

### 5.3 Profiles for standalone (C/J/X)AdES-B-B
Table 1 defines profiles for CAdES-B-B, JAdES-B-B, XAdES-B-B (standalone). Key requirements:
- ds:KeyInfo/X509Data, SignedData.certificates, x5c: **shall be present**, cardinality 1.
- content-type, message-digest, CanonicalizationMethod: **shall be present**.
- SigningTime, SigningCertificateV2, signing-time, iat, signing-certificate-v2: **shall be present**.
- CommitmentTypeIndication: **may be present** (≥0 for XAdES, 0 or 1 for CAdES).
- SignaturePolicyIdentifier: **may be present** (0 or 1).
- Service "signing properties, SC Byte Code and binding with SC Package": **shall be present**.
- SPO ds:Reference: **shall be present**, cardinality N+1.
- EncapContentInfo.econtentType: **shall be present** (CAdES).
- Payload: **shall be present** (JAdES).
- DataObjectFormat: conditioned presence (≥0), with Description, MimeType, Encoding, ObjectReference as specified.

### 5.4 Profiles for standalone (C/J/X)AdES-B-LTA
Table 2 defines components to be added to the B-B profiles to become B-LTA:
- SignatureTimeStamp (sigTst): **shall be present**, cardinality 1.
- CertificateValues (xVals), AnyValidationData (anyValData), AttrAuthoritiesCertValues (axVals), RevocationValues (rVals), AttributeRevocationValues (arVals): conditioned presence (0 or 1 or ≥0).
- Service "revocation values in long-term validation": **shall be provided**.
- Service "Incorporation of validation data for electronic time-stamps": **shall be provided**.
- ArchiveTimeStamp (namespace v1.4.1): **shall be present**, cardinality ≥1.
- RenewedDigestsV2: conditioned presence (≥0).

### 5.5 Profiles for (C/X)AdES-B-B signatures included in an ASiC-E container
Table 3 defines profiles for signatures inside ASiC-E (for several detached data objects). N = number of signed files.
- ds:KeyInfo/X509Data, SignedData.certificates: **shall be present**, cardinality 1.
- content-type, message-digest, CanonicalizationMethod: **shall be present**.
- ds:Reference: **shall be present**, cardinality N+1.
- SigningTime, SigningCertificateV2: **shall be present**.
- DataObjectFormat: **shall be present**, cardinality N.
- CommitmentTypeIndication: **may be present** with constraints (XAdES: ≥0 and ≤N; CAdES: 0 or 1).
- SignaturePolicyIdentifier, cms-algorithm-protection: **may be present**.

### 5.6 Profile for XAdES-B-LTA long-term signatures included in an ASiC-E container
Table 4 defines profile for XAdES-B-LTA inside ASiC-E (long-term). Requirements similar to Tables 3 and 2 combined, with specific cardinalities. Notably:
- DataObjectFormat: **shall be present**, cardinality N, with Description, MimeType, ObjectReference required; Encoding optional; ObjectIdentifier **shall not be present**.
- CommitmentTypeIndication: **may be present**, cardinality 1.
- SignatureTimeStamp: **shall be present**.
- CertificateValues, AnyValidationData, AttrAuthoritiesCertValues, RevocationValues, AttributeRevocationValues: conditioned presence.
- Service for validation data of time-stamps: **shall be provided**.
- ArchiveTimeStamp: **shall be present**, cardinality ≥1.
- RenewedDigestsV2: conditioned presence.

## 6 ASiC containers profiles

### 6.1 Introduction
When multiple data objects need to be signed and detached, ASiC-E containers with CAdES or XAdES signatures **shall** be used. This clause specifies general ASiC-E requirements referenced by other clauses.

### 6.2 Profile for ASiC-E containers for short-term signatures
#### 6.2.1 General requirements
- ASiC-E container **shall** be as per ETSI EN 319 162-1 [1], with CAdES or XAdES signatures.

#### 6.2.2 Signing with XAdES
- **signatures.xml** file in META-INF: root element `asic:XAdESSignatures` containing one `ds:Signature` (profile per clause 5.5).
- XAdES signature: non-distributed, with ds:Reference for each SC package file plus one for SignedProperties. Signature **shall** be XAdES-B-B per Table 3.

#### 6.2.3 Signing with CAdES
- **signature.p7s** file in META-INF (CAdES signature on SC Package).
- **ASiCManifest.xml** in META-INF: root `ASiCManifest` with one `SigReference` referencing signature.p7s; data object references for each SC package file with digest and MimeType.
- CAdES signature: one SignerInfo, **shall** be CAdES-B-B per Table 3.

### 6.3 Profile for ASiC-E containers for long-term signatures
#### 6.3.1 General requirements
Long-term preservation **shall** be achieved either by:
1) preservation trust service preserving electronic seals/signatures; or
2) augmentation per clause 4.4.5 of EN 319 162-1 [1].

#### 6.3.2 Signing with XAdES
- Long-term availability/integrity by adding unsigned qualifying properties per EN 319 162-1 [1] clause 4.4.5.
- XAdES signature **shall** be XAdES-B-LTA per Table 4.

#### 6.3.3 Signing with CAdES
- Long-term by adding one `ASiCArchiveManifest` file for each time-stamp token added to the ASiC container.

## 7 Requirements on identity validation

### 7.1 Introduction
Validation of electronic identities may be done by:
1) validating standalone AdES signatures or ASiC-E containers; or
2) using the EUDI Wallet per Article 5a of [i.3] to request/present EAAs/PIDs.

### 7.2 Validation based on digital signatures
#### 7.2.1 Requirements on validation of digital signatures
- Validation **shall** be performed per ETSI EN 319 102-1 [4].

#### 7.2.2 Requirements on generation of signed validation reports
- Validating entities **should** generate validation reports per ETSI TS 119 102-2 [5] and sign with standalone AdES-B-B per Table 1.

### 7.3 Validation based on EUDI Wallet
- Entities **should** use protocol per ETSI TS 119 472-2 [i.4] for requesting/presenting EAAs/PIDs.
- For natural persons, **should** support mandatory PID attributes per Table 1 of Commission Implementing Regulation (EU) 2024/2977 [i.5] Annex a.
- For legal persons, **should** support mandatory PID attributes per Table 3 of same Annex.
- Entities **should** support ISO/IEC 18013-5 [i.2] for interfacing to the Wallet.

## 8 Requirements for Production phase

### 8.1 Introduction
Providers of SC languages, compilers, and VMs **shall** identify themselves by signing their products using standalone AdES (per clause 5.3) or ASiC-E (per clause 6.2). Long-term may be ensured per clause 6.3 or via preservation trust service.

### 8.2 Identification of SC Languages, SC Compilers and SC Virtual Machines providers
#### 8.2.1 General requirements
Providers **shall** sign their deliverables. ASiC-E containers, if used, **shall** have a child folder named according to pattern: "SCL-<publisher identifier>" (for language), "SCC-<publisher identifier>" (for compiler), "SCVM-<publisher identifier>" (for VM). Identifier encoded per bullet b) of clause 4.2 of EN 319 162-1 [1].

#### 8.2.2 Identifying the SC Language Publisher
- **Shall** sign SC language specification and SC Language Specification Policy.

#### 8.2.3 Identifying the SC Compiler Publisher
- **Shall** sign SC Compiler and SC Compiler Policy.

#### 8.2.4 Identifying the SC Virtual Machine Publisher
- **Shall** sign SC Virtual Machine and SC VM Policy.

### 8.3 Identification of SC Publisher
- **Shall** generate an ASiC-E container per clause 6.2 enclosing the SC package.
- Container **shall** have a child folder "SC-<SC Identifier>" containing the SC package files (e.g., source code, byte code, legal text, documentation).
- Long-term **shall** be ensured either by preservation trust service or augmentation per clause 6.3.

### 8.4 Identification of SC parties
- Each party agreeing the SC **shall** sign acceptance of SC terms with AdES-B-B per Table 1.
- Each party **shall** sign acceptance of SC Provider terms with AdES-B-B per Table 1.
- Long-term of these signatures **shall** be ensured either by preservation trust service or augmentation per clause 5.4.

## 9 Requirements for Deployment phase

### 9.1 Validation of the ASiC-E enclosing the SC package by the SC Deployer
- SC Deployer **shall** validate the ASiC-E container per clause 7.2.1.
- After validation, SC Deployer **shall** generate and sign a validation report per clause 7.2.2 with AdES-B-B per Table 1.

### 9.2 Evidence of SC Deployment signed by the SC Deployer
#### 9.2.1 Signature on deployed Smart Contract
- If validation succeeds, SC Deployer **shall** deploy the Smart Contract and generate a SC Deployment Evidence, which **shall** be an AdES-B-B signature (CAdES, JAdES, or XAdES) per Table 1.
- The signature **shall** indirectly sign the SC, be bound to the SC Package via a binding file (clause 9.2.2), and be placed in the same folder as the deployed SC with extensions .p7m (CAdES), .json (JAdES), or .xml (XAdES).

#### 9.2.2 SC Package binding file
- **Shall** be a Multipart MIME object with as many parts as files in the SC Package, all type Text/Plain.
- Content-Description of first part: global locator of the ASiC container (out of scope for specification).
- Each part: first line = local filename (inside "SC-<SC Identifier>"), second line = digest algorithm OID, third line = base64-encoded digest value.

#### 9.2.3 Signing with CAdES signature
- `encapContentInfo.eContentType` **shall** be OID `id-aa-ets-sc-package-signature` (0.4.0.128.19542.1).
- `encapContentInfo.eContent` **shall** be a multipart MIME object with N+1 parts:
  - First part: Content-Description "SC digest", first line = URI of deployed SC, second line = digest OID, third line = base64 digest.
  - Remaining N parts: binding file parts as in clause 9.2.2.

#### 9.2.4 Signing with JAdES signature
- Payload **shall** be the same multipart MIME object (as for CAdES) base64url-encoded.

#### 9.2.5 Signing with XAdES signature
- **Shall** have 3 `ds:Reference` elements:
  1. Signed properties.
  2. Smart Contract file (URI attribute allowing retrieval within Electronic Ledger).
  3. An enveloped `ds:Object` containing the SC Package binding file base64-encoded.
- Thus indirectly signs detached SC and SC Package files.

## 10 Requirements for the SC Execution phase

### 10.1 Introduction
- Before first execution, SC Provider **shall** validate the SC Deployment Evidence (clause 10.2).
- Before every execution, SC Provider and SC User **shall** mutually authenticate (clause 10.3).
- After execution, SC Provider **shall** generate and sign an execution report (clause 10.4).

### 10.2 Requirements for validation of the signed SC Deployment evidence
- SC Provider **shall** validate the deployment evidence per clause 7.2.1 and generate a signed validation report per clause 7.2.2.

### 10.3 Requirements for validation of electronic identities of SC Provider and SC User
- Mutual authentication **shall** occur before execution.

**If using EUDI Wallet:**
1. SC Provider requests EAA/PID presentation from SC User; SC User presents per clause 7.3.
2. SC Provider generates and signs an identity validation report (standalone AdES-B-B per Table 1).
3. SC User authenticates SC Provider by validating that signed report.

**If using digital signatures:**
1. SC User generates a standalone AdES-B-B per Table 1.
2. SC Provider validates that signature per clause 7.2.1.
3. SC Provider generates and signs a validation report per clause 7.2.2.
4. SC User authenticates SC Provider by validating that signed report.

### 10.4 Requirements on the signed execution report by the SC Provider
- After SC execution, SC Provider **shall** sign an execution report with standalone AdES-B-B per Table 1.
- The report **shall** include details of the requesting user whose identity was validated.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | SC Language Publisher shall sign SC Language Specification and Policy. | shall | 8.2.2 |
| R2 | SC Compiler Publisher shall sign SC Compiler and Policy. | shall | 8.2.3 |
| R3 | SC Virtual Machine Publisher shall sign SC VM and Policy. | shall | 8.2.4 |
| R4 | SC Publisher shall generate an ASiC-E container enclosing the SC package. | shall | 8.3 |
| R5 | SC parties shall sign acceptance of SC terms and SC Provider terms with AdES-B-B. | shall | 8.4 |
| R6 | SC Deployer shall validate the ASiC-E container and sign a validation report. | shall | 9.1 |
| R7 | SC Deployer shall sign the Smart Contract deployment evidence with AdES-B-B and bind to SC Package. | shall | 9.2.1 |
| R8 | SC Provider shall validate SC deployment evidence before first execution. | shall | 10.2 |
| R9 | SC Provider and SC User shall mutually authenticate before each execution. | shall | 10.3 |
| R10 | SC Provider shall sign an execution report after SC execution. | shall | 10.4 |
| R11 | Validation of digital signatures shall be performed per EN 319 102-1. | shall | 7.2.1 |
| R12 | Validation reports should be generated per TS 119 102-2 and signed with AdES-B-B. | should | 7.2.2 |
| R13 | When using EUDI Wallet, entities should use protocol per TS 119 472-2. | should | 7.3 |
| R14 | For long-term preservation of ASiC-E containers, use preservation trust service or augmentation. | shall | 6.3.1, 8.3, 8.4 |
| R15 | Profiles for AdES signatures (Tables 1-4) shall be followed as referenced. | shall | 5.3, 5.4, 5.5, 5.6 |

## Informative Annexes (Condensed)
- **Table 1 (Clause 5.3)**: Defines profiles for standalone (C/J/X)AdES-B-B signatures. Key components like KeyInfo, SigningTime, SigningCertificateV2 are mandatory; CommitmentTypeIndication and SignaturePolicyIdentifier are optional.
- **Table 2 (Clause 5.4)**: Lists components to add to B-B to become B-LTA for long-term standalone signatures: timestamps, certificate/revocation values, archive timestamps.
- **Table 3 (Clause 5.5)**: Profiles for (C/X)AdES-B-B signatures inside ASiC-E containers for signing multiple detached files. Similar to standalone but with DataObjectFormat mandatory for each file.
- **Table 4 (Clause 5.6)**: Profile for XAdES-B-LTA inside ASiC-E for long-term signatures, combining B-B and LTA requirements.
- **Clause 9.2.2**: Multipart MIME binding file structure to link deployment signature to SC Package.
- **Clause 9.2.3**: OID for smart contract package signature and detailed structure of CAdES signature leveraging multipart MIME.