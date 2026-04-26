# ETSI TS 119 511: Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for trust service providers providing long-term preservation of digital signatures or general data using digital signature techniques
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2025-10 | **Type**: Normative
**Original**: RTS/ESI-0019511v121

## Scope (Summary)
Specifies policy and security requirements for trust service providers offering long-term preservation of digital signatures and general data (signed or unsigned) using digital signature techniques. Supports qualified preservation service for qualified electronic signatures/seals under Regulation (EU) No 910/2014. Covers preservation of signature validity over long periods and proof of existence of digital objects.

## Normative References
- [1] ETSI EN 319 401: General Policy Requirements for Trust Service Providers
- [2] ETSI TS 119 612: Trusted Lists
- [3] ISO/IEC 15408 (parts 1-3): Evaluation criteria for IT security
- [4] ISO/IEC 19790: Security requirements for cryptographic modules
- [5] FIPS PUB 140-2 (2001): Security Requirements for Cryptographic Modules
- [6] FIPS PUB 140-3 (2019): Security Requirements for Cryptographic Modules
- [7] ETSI TS 119 172-4: Signature applicability rules (validation policy) for European qualified electronic signatures/seals using trusted lists
- [8] IETF RFC 3161: Time-Stamp Protocol (TSP)
- [9] IETF RFC 5816: ESSCertIDv2 Update for RFC 3161
- [10] IETF RFC 4998: Evidence Record Syntax (ERS)
- [11] IETF RFC 6283: XML Evidence Record Syntax (XMLERS)

## Definitions and Abbreviations
- **preservation evidence**: Evidence produced by the preservation service demonstrating that preservation goals are met for a given preservation object.
- **preservation evidence policy**: Set of rules specifying requirements and internal process to generate or validate preservation evidence.
- **preservation goal**: One of: extending validity status of digital signatures, providing proofs of existence over long periods, or augmenting externally provided preservation evidences.
- **preservation period**: For [WST], duration during which the service preserves submitted objects and associated evidences.
- **preservation profile**: Uniquely identified set of implementation details for a preservation storage model and one or more goals.
- **preservation service provider (PSP)**: Trust service provider providing preservation service.
- **preservation storage model**: With Storage [WST], With Temporary Storage [WTS], Without Storage [WOS].
- **EU qualified preservation service**: Meets requirements for qualified preservation service for qualified electronic signatures/seals under Regulation (EU) 910/2014.
- Abbreviations: AUG (augmentation goal), OVR (overall), PDS (preservation of digital signatures), PGD (preservation of general data), POC (preservation object container), PO (preservation object), PSP (preservation service provider), SubDO (submission data object), TSA (time-stamping authority), WOS (without storage), WST (with storage), WTS (with temporary storage).

## General Concepts
### 4.1 Preservation Storage Models
#### 4.1.1 Overview
Three models:
- **WST**: Service stores submitted data and derived preservation objects. Evidences and objects delivered on request.
- **WTS**: Data stored temporarily until evidence produced. Evidences stored for retention period.
- **WOS**: Data not stored; evidences produced synchronously and returned in response.

#### 4.1.2 [WST] With Storage
- Service stores SubDO and derived POs, produces evidences per selected preservation profile.
- Client receives preservation object identifier; can retrieve evidences/POs, request deletion.
- Deletion of preservation evidence requires deletion of corresponding SubDOs.
- Allows new versions of POs via difference specification.
- May contact external TSPs for validation data.

#### 4.1.3 [WTS] With Temporary Storage
- Temporarily stores SubDO or hash values until evidence asynchronously produced.
- Evidences retrievable during preservation evidence retention period.

#### 4.1.4 [WOS] Without Storage
- Produces evidences synchronously; no storage of data or evidences.

### 4.2 Functional Goals
- **[PGD]**: Proof of existence of general data over long periods.
- **[PDS]**: Preservation of ability to validate digital signature and maintain validity status (collects and protects validation data).
- **[PDS+PGD]**: Combined.
- **[AUG]**: Augmentation of submitted preservation evidences (client submits evidence to be augmented).

### 4.3 Preservation Service Applicable Documentation
#### 4.3.1 Preservation Service Practice Statement
- Developed, implemented, enforced, updated by PSP.
- Describes operation; recipients include auditors, subscribers, relying parties.

#### 4.3.2 Preservation Service Policy
- Describes what is offered.
- OID for conformance: `itu-t(0) identified-organization(4) etsi(0) pres-service-policies(19511) policy-identifiers(1) main (1)` for basic; `qualified (2)` for annex A.
- Mandatory to identify supported policies.

#### 4.3.3 Preservation Schemes and Profiles
- Preservation scheme: generic procedures per storage model and goals.
- Preservation profile: implementation details; uniquely identifiable (URI/OID + version).

#### 4.3.4 Preservation Evidence Policy
- Referenced by preservation profile; contains creation and validation rules.

#### 4.3.5 Signature Validation Policy
- For [PDS], describes rules for obtaining validation data.

### 4.4 Expected Evidence Duration
- For [WTS][WOS]: duration during which evidence can be used.
- Depends on key validity, certificate validity, revocation availability, cryptographic strength.

### 4.5 Preservation Period
- For [WST]: duration of storage; defined by duration, legal requirements, or date.

## Risk Assessment
- **OVR-5-01**: Requirements of ETSI EN 319 401, clause 5 shall apply.

## Policies and Practices
### 6.1 Preservation Service Practice Statement
- **OVR-6.1-01**: Requirements of EN 319 401, clause 6.1 shall apply.
- **OVR-6.1-02**: PSP should list or reference supported preservation service policies.
- **OVR-6.1-03**: PS shall list supported preservation profiles.
- **OVR-6.1-04**: PS shall state how preservation goals are achieved.
- **OVR-6.1-05**: PS shall define availability of SubDO and evidences.
- **OVR-6.1-06**: PS shall identify obligations of external organizations.
- **OVR-6.1-07 [WST]**: Details on requesting export-import packages.
- **OVR-6.1-08 [WST]**: Specify production methods of export-import packages.
- **OVR-6.1-09 [WST]**: Specify what happens to data at end of preservation period.

### 6.2 Terms and Conditions
- **OVR-6.2-01**: Requirements of EN 319 401, clause 6.2 shall apply.
- **OVR-6.2-02**: List supported preservation service policies.
- **OVR-6.2-03**: State where to find information on supported preservation profiles.
- **OVR-6.2-04 [CONDITIONAL]**: If submitter takes role in preservation process, describe conditions and responsibilities.
- **OVR-6.2-05 [WST]**: State how export-import request can be made.
- **OVR-6.2-06 [PDS]**: State strategy when unable to collect all validation data.
- **OVR-6.2-07 [CONDITIONAL]**: If hash values may be used in hash-tree-renewal, state that PSP not liable for correspondence.
- **OVR-6.2-08 [CONDITIONAL]**: If only hash values provided, state that preservation only on submitted objects and proof limited to hash algorithm strength.

### 6.3 Information Security Policy
- **OVR-6.3-01**: Requirements of EN 319 401, clause 6.3 shall apply.

### 6.4 Preservation Profiles
- **OVR-6.4-01**: Support at least one preservation profile.
- **OVR-6.4-02**: May support more than one.
- **OVR-6.4-03**: Uniquely identified.
- **OVR-6.4-04**: A preservation profile shall contain:
  - a) Unique identifier.
  - b) Supported operations of preservation protocol, including input formats, and conditional output formats.
  - c) Set of applicable policies: reference to preservation evidence policy, and [PDS][PDS+PGD] conditional reference to signature validation policy.
  - d) Validity period (start date, optional end date).
  - e) Preservation storage model (WST, WTS, WOS).
  - f) Preservation goals (PDS, PGD, AUG, combination).
  - g) All supported evidence formats.
  - h) May contain specification reference.
  - i) Shall contain or refer to human-readable description.
  - j) May contain identifier for preservation scheme.
- **OVR-6.4-05 [WTS]**: Shall contain preservation evidence retention period.
- **OVR-6.4-06 [WTS][WOS]**: Should contain expected evidence duration.
- **OVR-6.4-07 [WTS][WOS]**: Expected evidence duration shall be based on estimation of cryptographic algorithm suitability.
- **OVR-6.4-08 [WTS][WOS]**: Should be based on ETSI TS 119 312.
- **OVR-6.4-09**: Supported preservation profiles shall be available online.
- **OVR-6.4-10**: Make publicly available all profiles currently or previously supported.
- **OVR-6.4-11 [WST]**: Same profile shall apply during whole preservation period.
- **OVR-6.4-12 [WTS]**: Same profile shall apply during whole preservation evidence retention period.
- **OVR-6.4-13**: Profile should not change over time; dynamic aspects outside profile.
- **OVR-6.4-14**: Referenced policies may change; all versions shall be publicly available with clear applicability.

### 6.5 Preservation Evidence Policy
- **OVR-6.5-01**: May be human-readable.
- **OVR-6.5-02 [CONDITIONAL]**: If multiple formats/languages, state which takes precedence.
- **OVR-6.5-03**: Shall contain description of how evidence is created, including cryptographic algorithms.
- **OVR-6.5-04**: Algorithms should be chosen per ETSI TS 119 312.
- **OVR-6.5-05**: Shall contain description of which TSPs may be used.
- **OVR-6.5-06**: Shall contain how evidence can be validated, including trust anchors for signatures and timestamps.
- **OVR-6.5-07 [WST][WTS]**: Shall state how evidence is augmented.
- **OVR-6.5-08**: Shall describe format.
- **OVR-6.5-09**: Shall state if evidence contains explicit information of applicable preservation service, policy, or profile.

### 6.6 Signature Validation Policy
- **OVR-6.6-01**: May be human-readable.
- **OVR-6.6-02 [CONDITIONAL]**: If multiple formats/languages, state which takes precedence.
- **OVR-6.6-03 [CONDITIONAL]**: If present, shall state strategy for selecting validation material (trust anchors, validation model).

### 6.7 Subscriber Agreement
- **OVR-6.7-01**: Provide subscriber agreement including acceptance of terms and conditions.
- **OVR-6.7-02 [CONDITIONAL]**: If notification protocol provided, state whether and how subscriber wishes to be notified.
- **OVR-6.7-03 [CONDITIONAL]**: Update agreement each time a notification method is added/removed.
- **OVR-6.7-04 [WTS][WST]**: State who has right to access POs including SubDOs and evidences.
- **OVR-6.7-05 [WTS][WST]**: State who has right to request traces.

## PSP Management and Operation
### 7.1 Internal Organization
- **OVR-7.1-01**: Requirements of EN 319 401, clause 7.1 shall apply.

### 7.2 Human Resources
- **OVR-7.2-01**: Requirements of EN 319 401, clause 7.2 shall apply.

### 7.3 Asset Management
- **OVR-7.3-01**: Requirements of EN 319 401, clause 7.3 shall apply.

### 7.4 Access Control
- **OVR-7.4-01**: Requirements of EN 319 401, clause 7.4 shall apply.

### 7.5 Cryptographic Controls
- **OVR-7.5-01**: Requirements of EN 319 401, clause 7.5 shall apply.
- **OVR-7.5-02**: PSP shall ensure timestamps used come from TSA following state-of-the-art practices (preferably conforming to ETSI EN 319 421).
- **OVR-7.5-03**: Should use timestamps verifiable with CRLs/OCSP responses including reason code.
- **OVR-7.5-04 [CONDITIONAL]**: When PSP signs part of preservation evidence, should select signing certificate from CA implementing EN 319 411-1 or -2.
- **OVR-7.5-05 [CONDITIONAL]**: Private signing key shall be held in secure cryptographic device meeting EAL4+ (ISO/IEC 15408, EUCC) or ISO/IEC 19790/FIPS 140-2 level 3 or FIPS 140-3 level 3.
- **OVR-7.5-06 [CONDITIONAL]**: Preferred compliance with 7.5-05 a).
- **OVR-7.5-07 [CONDITIONAL]**: Backup copies of private keys shall be protected for integrity and confidentiality by the device before external storage.

### 7.6 Physical and Environmental Security
- **OVR-7.6-01**: Requirements of EN 319 401, clause 7.6 shall apply.

### 7.7 Operation Security
- **OVR-7.7-01**: Requirements of EN 319 401, clause 7.7 shall apply.

### 7.8 Network Security
- **OVR-7.8-01**: Requirements of EN 319 401, clause 7.8 shall apply.
- **OVR-7.8-02 [WST]**: Preservation service shall be integrated such that storage access changing content only by the service.

### 7.9 Incident Management
- **OVR-7.9-01**: Requirements of EN 319 401, clause 7.9 shall apply.

### 7.10 Collection of Evidence
- **OVR-7.10-01**: Requirements of EN 319 401, clause 7.10 shall apply.
- **OVR-7.10-02**: Implement event logs for later proofs.

### 7.11 Business Continuity Management
- **OVR-7.11-01**: Requirements of EN 319 401, clause 7.11 shall apply.

### 7.12 TSP Termination and Termination Plans
- **OVR-7.12-01**: Requirements of EN 319 401, clause 7.12 shall apply.
- **OVR-7.12-02 [WST]**: Termination plan shall include what happens to stored POs.

### 7.13 Compliance
- **OVR-7.13-01**: Requirements of EN 319 401, clause 7.13 shall apply.

### 7.14 Cryptographic Monitoring
- **OVR-7.14-01**: For each active profile, monitor strength of every used algorithm. If algorithm becomes less secure or certificate expires, update evidence policy or create new profile.
- **OVR-7.14-02 [WST][CONDITIONAL]**: If algorithm becomes less secure or certificate expires, evidence shall be augmented per new version of evidence policy during preservation period.
- **OVR-7.14-03**: Should consider ETSI TS 119 312.

### 7.15 Augmentation of Preservation Evidences
- **OVR-7.15-01 [WST]**: Ensure evidence can be used to achieve goal during preservation period.
- **OVR-7.15-02 [WTS]**: Ensure evidence can be used during preservation evidence retention period.
- **OVR-7.15-03 [WST][WTS]**: Augment before evidence cannot be used anymore.

### 7.16 Export-Import Package
- **OVR-7.16-01 [WST]**: Shall allow request of export-import package containing preserved data, evidences, and validation info.
- **OVR-7.16-02 [WST]**: Should use standardized format (e.g., ETSI TS 119 512 or TR-ESOR-M.3).
- **OVR-7.16-03 [WST]**: Delivered only to authorized legal/natural person.
- **OVR-7.16-04 [WST]**: Keep records of all released packages including date and selection criteria.

### 7.17 Supply Chain
- **OVR-7.17-01**: Requirements of EN 319 401, clause 7.14 shall apply.

## Operational and Notification Protocols
### 8.1 Preservation Protocol
- **PRP-8.1-01**: Communication channel shall be secured; client authentication and data confidentiality ensured.
- **PRP-8.1-02**: Should use protocol defined in ETSI TS 119 512.
- **PRP-8.1-03**: Protocols protected against unauthorized usage.
- **PRP-8.1-04**: Allow retrieval of info on currently and previously supported profiles.
- **PRP-8.1-05**: Allow submission of SubDO under a specific profile; return either preservation object identifier or immediate evidence (synchronous mode).
- **PRP-8.1-06**: May allow retrieval of traces for a specific preservation object identifier.
- **PRP-8.1-07**: May allow search for preservation objects and retrieve identifiers.
- **PRP-8.1-08**: May allow submission of evidence and POs for validation and receive report.
- **PRP-8.1-09 [CONDITIONAL]**: If search allowed, may include filter functionality.
- **PRP-8.1-10 [WST]**: Allow retrieval of evidences and/or POs.
- **PRP-8.1-11 [WST]**: Allow deletion of stored POs; deletion of preservation evidence requires deletion of corresponding SubDO.
- **PRP-8.1-12 [WST]**: POs can only be deleted before end of preservation period with justification; logged.
- **PRP-8.1-13 [WST]**: Should allow request of set of identifiers.
- **PRP-8.1-14 [WST]**: May allow new version of POC (delta).
- **PRP-8.1-15 [WTS]**: Allow retrieval of asynchronously produced evidences.

### 8.2 Notification Protocol
- **OVR-8.2-01**: May define notification protocol to send messages to subscribers.
- **OVR-8.2-02 [CONDITIONAL]**: If notification protocol provided, when evidence policy becomes insecure, notify subscribers possibly using the profile.
- **OVR-8.2-03 [CONDITIONAL]**: If changes in reference elements influence profile, notify subscribers.

## Preservation Process
### 9.1 Storage of Preserved Data and Evidences
- **OVR-9.1-01 [WOS][WTS]**: Should not store data after evidence creation.
- **OVR-9.1-02 [WOS][WTS][CONDITIONAL]**: If stored, state reasons in terms and conditions.
- **OVR-9.1-03 [WTS]**: Shall not store evidence longer than indicated in practice statement.

### 9.2 Preservation Evidences
- **OVR-9.2-01 [CONDITIONAL]**: If time-stamp token used, shall conform to IETF RFC 3161 and RFC 5816.
- **OVR-9.2-02**: Should conform to ETSI EN 319 422.
- **OVR-9.2-03 [CONDITIONAL]**: If evidence record used, shall conform to IETF RFC 4998 or 6283.
- **OVR-9.2-04 [CONDITIONAL]**: If evidence policy cannot be identified from context, include in evidence.
- **OVR-9.2-05 [CONDITIONAL]**: If included, should be cryptographically protected.

### 9.3 Preservation of Digital Signatures
- **OVR-9.3-01 [PDS][PDS+PGD][CONDITIONAL]**: If validation data not submitted by client, service shall make best efforts to collect and verify per signature validation policy.
- **OVR-9.3-02 [PDS][PDS+PGD][CONDITIONAL]**: If validation data submitted, should verify and collect appropriate data if not appropriate.
- **OVR-9.3-03 [PDS]**: To extend ability to validate, shall provide proof of existence of signature and validation data using digital signature techniques.
- **OVR-9.3-04 [PDS+PGD]**: Shall provide proof of existence of signature, validation data, and signed data.
- **OVR-9.3-05 [PDS][PDS+PGD][CONDITIONAL]**: For detached signature, may allow only hash value of signed data.
- **OVR-9.3-06**: Shall indicate hash function identifiers in profile.
- **OVR-9.3-07**: Shall treat hash value as general data linked to signature.
- **OVR-9.3-08**: Shall verify hash values match length per algorithm identifier.

## Annex A (Normative): Qualified Preservation Service for QES as per Article 34 of Regulation (EU) No 910/2014
- **OVR-A-01 [PDS][PDS+PGD]**: All requirements untagged or tagged as [PDS] or [PDS+PGD] from clauses 5-9 shall apply.
- **OVR-A-02 [PDS][PDS+PGD]**: Shall preserve all information needed to check qualification status of signature/seal that would not be publicly available until end of preservation period.
- **OVR-A-02A [PDS][PDS+PGD]**: Shall ensure that at any time, preserved information when input to clause 4.4 of ETSI TS 119 172-4 clearly determines whether signature/seal was technically suitable to implement EU qualified electronic signature/seal at time of preservation.
- **OVR-A-03 [PDS][PDS+PGD]**: Timestamps should be from qualified TSA.
- **OVR-A-04**: Preservation service shall have one service digital identifier as defined in clause 5.5.3 of ETSI TS 119 612 to uniquely identify service within EUMS trusted list.

## Annex B (Informative): Mapping of Requirements to Regulation (EU) No 910/2014
Provides mapping of Article 24.2 (a)-(j) requirements to clauses in this document, and Article 34.1 to clauses 7.14, 7.15, 9.2, 9.3, OVR-A-02. Summarized: The qualified trust service provider requirements are covered by clauses on personnel (7.2), risk management (7.1), terms (6.2), trustworthy systems (7.7, 8.1), data storage (7.13, 7.2, 7.5), anti-forgery (7.6, 7.7), logging (7.10, 7.11), termination (7.12), and data protection (7.13). Preservation requirements covered by cryptographic monitoring and augmentation.

## Annex C (Informative): Differences and Relationships Between an Archival Service and a Preservation Service
Describes three stages of archival (current, semi-current, historical) vs preservation (with/without/temporary storage). A preservation service uses digital signature techniques for proof of existence; an archival service may use audit. A preservation service can be part of an archival service. A preservation service with storage may use an archival service for storage.

## Annex D (Informative): Cryptographic Threats and Countermeasures
Outlines three risk categories: collision attacks on hash functions (mitigated by re-signing with stronger algorithms or using multiple hash algorithms), attacks on signature algorithm/key length (mitigated by time-stamping prior to compromise), and risks from signing key revocation (mitigated by capturing revocation information in protection evidence). Countermeasures include time-stamp renewal and hash tree renewal.

## Annex E (Informative): Change History
Lists changes from version 1.1.2 to 1.2.1: adding eIDAS amendment note, supply chain section, clarification that only [PDS] or [PDS+PGD] apply for qualified preservation, mandatory requirement to ETSI TS 119 172-4, move of that reference to normative, definition of secure cryptographic device, update HSM requirements to include EUCC and FIPS PUB 140-3, correction of reference number.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| OVR-5-01 | Risk assessment requirements from EN 319 401 clause 5 shall apply. | shall | Clause 5 |
| OVR-6.1-01 | Requirements from EN 319 401 clause 6.1 shall apply. | shall | 6.1 |
| OVR-6.1-02 | Should list or reference supported preservation service policies. | should | 6.1 |
| OVR-6.1-03 | Shall list supported preservation profiles. | shall | 6.1 |
| OVR-6.1-04 | Shall state how preservation goals are achieved. | shall | 6.1 |
| OVR-6.1-05 | Shall define availability of SubDO and evidences. | shall | 6.1 |
| OVR-6.1-06 | Shall identify obligations of external organizations. | shall | 6.1 |
| OVR-6.1-07 [WST] | Shall state details on export-import package request. | shall | 6.1 |
| OVR-6.1-08 [WST] | Shall specify production methods of export-import packages. | shall | 6.1 |
| OVR-6.1-09 [WST] | Shall specify what happens to data at end of preservation period. | shall | 6.1 |
| OVR-6.2-01 | Requirements from EN 319 401 clause 6.2 shall apply. | shall | 6.2 |
| OVR-6.2-02 | Shall list supported preservation service policies in terms and conditions. | shall | 6.2 |
| OVR-6.2-03 | Shall state where to find info on supported profiles. | shall | 6.2 |
| OVR-6.2-04 [COND] | If submitter takes role, describe conditions and responsibilities. | shall | 6.2 |
| OVR-6.2-05 [WST] | Shall state how export-import request can be made. | shall | 6.2 |
| OVR-6.2-06 [PDS] | Shall state strategy when unable to collect all validation data. | shall | 6.2 |
| OVR-6.2-07 [COND] | If hash-tree-renewal, state PSP not liable for correspondence. | shall | 6.2 |
| OVR-6.2-08 [COND] | If only hashes provided, state limitations. | shall | 6.2 |
| OVR-6.3-01 | Requirements from EN 319 401 clause 6.3 shall apply. | shall | 6.3 |
| OVR-6.4-01 | Support at least one preservation profile. | shall | 6.4 |
| OVR-6.4-02 | May support more than one. | may | 6.4 |
| OVR-6.4-03 | Uniquely identified. | shall | 6.4 |
| OVR-6.4-04 | Profile shall contain specific items a)-j). | shall | 6.4 |
| OVR-6.4-05 [WTS] | Shall contain preservation evidence retention period. | shall | 6.4 |
| OVR-6.4-06 [WTS][WOS] | Should contain expected evidence duration. | should | 6.4 |
| OVR-6.4-07 [WTS][WOS] | Expected evidence duration based on algorithm suitability. | shall | 6.4 |
| OVR-6.4-08 [WTS][WOS] | Should be based on TS 119 312. | should | 6.4 |
| OVR-6.4-09 | Profiles available online. | shall | 6.4 |
| OVR-6.4-10 | Make publicly available all supported profiles. | shall | 6.4 |
| OVR-6.4-11 [WST] | Same profile during whole preservation period. | shall | 6.4 |
| OVR-6.4-12 [WTS] | Same profile during whole retention period. | shall | 6.4 |
| OVR-6.4-13 | Profile should not change; dynamic aspects outside. | should | 6.4 |
| OVR-6.4-14 | Referenced policies may change; all versions publicly available. | shall | 6.4 |
| OVR-6.5-01 | Preservation evidence policy may be human-readable. | may | 6.5 |
| OVR-6.5-02 [COND] | If multiple, state precedence. | shall | 6.5 |
| OVR-6.5-03 | Shall describe creation including algorithms. | shall | 6.5 |
| OVR-6.5-04 | Algorithms should be per TS 119 312. | should | 6.5 |
| OVR-6.5-05 | Shall contain description of which TSPs may be used. | shall | 6.5 |
| OVR-6.5-06 | Shall contain validation instructions including trust anchors. | shall | 6.5 |
| OVR-6.5-07 [WST][WTS] | Shall state how evidence is augmented. | shall | 6.5 |
| OVR-6.5-08 | Shall describe format. | shall | 6.5 |
| OVR-6.5-09 | Shall state if evidence contains explicit info of service/policy/profile. | shall | 6.5 |
| OVR-6.6-01 | Signature validation policy may be human-readable. | may | 6.6 |
| OVR-6.6-02 [COND] | If multiple, state precedence. | shall | 6.6 |
| OVR-6.6-03 [COND] | If present, state strategy for validation material. | shall | 6.6 |
| OVR-6.7-01 | Provide subscriber agreement. | shall | 6.7 |
| OVR-6.7-02 [COND] | If notification protocol, state subscriber preferences. | shall | 6.7 |
| OVR-6.7-03 [COND] | Update agreement on notification changes. | shall | 6.7 |
| OVR-6.7-04 [WTS][WST] | State access rights to POs. | shall | 6.7 |
| OVR-6.7-05 [WTS][WST] | State right to request traces. | shall | 6.7 |
| OVR-7.1-01 | Requirements from EN 319 401 clause 7.1 shall apply. | shall | 7.1 |
| OVR-7.2-01 | Requirements from EN 319 401 clause 7.2 shall apply. | shall | 7.2 |
| OVR-7.3-01 | Requirements from EN 319 401 clause 7.3 shall apply. | shall | 7.3 |
| OVR-7.4-01 | Requirements from EN 319 401 clause 7.4 shall apply. | shall | 7.4 |
| OVR-7.5-01 | Requirements from EN 319 401 clause 7.5 shall apply. | shall | 7.5 |
| OVR-7.5-02 | Timestamps from TSA following state-of-the-art. | shall | 7.5 |
| OVR-7.5-03 | Timestamps verifiable with CRL/OCSP including reason code. | should | 7.5 |
| OVR-7.5-04 [COND] | When PSP signs, signing certificate from CA implementing EN 319 411-1/-2. | should | 7.5 |
| OVR-7.5-05 [COND] | Private key in secure device meeting EAL4+ or equivalent. | shall | 7.5 |
| OVR-7.5-06 [COND] | Preferred per 7.5-05 a). | should | 7.5 |
| OVR-7.5-07 [COND] | Backup copies protected by device. | shall | 7.5 |
| OVR-7.6-01 | Requirements from EN 319 401 clause 7.6 shall apply. | shall | 7.6 |
| OVR-7.7-01 | Requirements from EN 319 401 clause 7.7 shall apply. | shall | 7.7 |
| OVR-7.8-01 | Requirements from EN 319 401 clause 7.8 shall apply. | shall | 7.8 |
| OVR-7.8-02 [WST] | Storage access only by service. | shall | 7.8 |
| OVR-7.9-01 | Requirements from EN 319 401 clause 7.9 shall apply. | shall | 7.9 |
| OVR-7.10-01 | Requirements from EN 319 401 clause 7.10 shall apply. | shall | 7.10 |
| OVR-7.10-02 | Implement event logs. | shall | 7.10 |
| OVR-7.11-01 | Requirements from EN 319 401 clause 7.11 shall apply. | shall | 7.11 |
| OVR-7.12-01 | Requirements from EN 319 401 clause 7.12 shall apply. | shall | 7.12 |
| OVR-7.12-02 [WST] | Termination plan includes stored POs. | shall | 7.12 |
| OVR-7.13-01 | Requirements from EN 319 401 clause 7.13 shall apply. | shall | 7.13 |
| OVR-7.14-01 | Monitor algorithm strength; update profile if needed. | shall | 7.14 |
| OVR-7.14-02 [WST][COND] | Augment evidence if algorithm becomes weak. | shall | 7.14 |
| OVR-7.14-03 | Should consider TS 119 312. | should | 7.14 |
| OVR-7.15-01 [WST] | Ensure evidence usable during preservation period. | shall | 7.15 |
| OVR-7.15-02 [WTS] | Ensure evidence usable during retention period. | shall | 7.15 |
| OVR-7.15-03 [WST][WTS] | Augment before evidence becomes unusable. | shall | 7.15 |
| OVR-7.16-01 [WST] | Allow export-import package request. | shall | 7.16 |
| OVR-7.16-02 [WST] | Should use standardized format. | should | 7.16 |
| OVR-7.16-03 [WST] | Deliver only to authorized person. | shall | 7.16 |
| OVR-7.16-04 [WST] | Keep records of released packages. | shall | 7.16 |
| OVR-7.17-01 | Requirements from EN 319 401 clause 7.14 shall apply. | shall | 7.17 |
| PRP-8.1-01 | Secure communication channel. | shall | 8.1 |
| PRP-8.1-02 | Should use TS 119 512 protocol. | should | 8.1 |
| PRP-8.1-03 | Protect against unauthorized usage. | shall | 8.1 |
| PRP-8.1-04 | Allow retrieval of profile info. | shall | 8.1 |
| PRP-8.1-05 | Allow submission under profile; return identifier or immediate evidence. | shall | 8.1 |
| PRP-8.1-06 | May allow retrieval of traces. | may | 8.1 |
| PRP-8.1-07 | May allow search. | may | 8.1 |
| PRP-8.1-08 | May allow evidence validation. | may | 8.1 |
| PRP-8.1-09 [COND] | If search, may include filter. | may | 8.1 |
| PRP-8.1-10 [WST] | Allow retrieval of evidences/POs. | shall | 8.1 |
| PRP-8.1-11 [WST] | Allow deletion; deletion of evidence deletes SubDO. | shall | 8.1 |
| PRP-8.1-12 [WST] | Deletion before end requires justification and logging. | shall | 8.1 |
| PRP-8.1-13 [WST] | Should allow request of identifiers. | should | 8.1 |
| PRP-8.1-14 [WST] | May allow new version of POC (delta). | may | 8.1 |
| PRP-8.1-15 [WTS] | Allow retrieval of asynchronously produced evidences. | shall | 8.1 |
| OVR-8.2-01 | May define notification protocol. | may | 8.2 |
| OVR-8.2-02 [COND] | Notify subscribers if evidence policy becomes insecure. | shall | 8.2 |
| OVR-8.2-03 [COND] | Notify on changes influencing profile. | shall | 8.2 |
| OVR-9.1-01 [WOS][WTS] | Should not store data after evidence creation. | should | 9.1 |
| OVR-9.1-02 [WOS][WTS][COND] | If stored, state reasons. | shall | 9.1 |
| OVR-9.1-03 [WTS] | Shall not store evidence longer than stated. | shall | 9.1 |
| OVR-9.2-01 [COND] | If timestamp, conform to RFC 3161/5816. | shall | 9.2 |
| OVR-9.2-02 | Should conform to EN 319 422. | should | 9.2 |
| OVR-9.2-03 [COND] | If evidence record, conform to RFC 4998 or 6283. | shall | 9.2 |
| OVR-9.2-04 [COND] | If policy not known, include in evidence. | should | 9.2 |
| OVR-9.2-05 [COND] | If included, cryptographically protected. | should | 9.2 |
| OVR-9.3-01 [PDS][PDS+PGD][COND] | Collect and verify validation data if not submitted. | shall | 9.3 |
| OVR-9.3-02 [PDS][PDS+PGD][COND] | Verify submitted validation data. | should | 9.3 |
| OVR-9.3-03 [PDS] | Provide proof of existence of signature and validation data. | shall | 9.3 |
| OVR-9.3-04 [PDS+PGD] | Provide proof of existence of signed data as well. | shall | 9.3 |
| OVR-9.3-05 [PDS][PDS+PGD][COND] | May allow only hash of signed data for detached signature. | may | 9.3 |
| OVR-9.3-06 | Indicate allowed hash function identifiers in profile. | shall | 9.3 |
| OVR-9.3-07 | Treat hash as general data linked to signature. | shall | 9.3 |
| OVR-9.3-08 | Verify hash length matches algorithm identifier. | shall | 9.3 |
| OVR-A-01 [PDS][PDS+PGD] | All requirements from clauses 5-9 apply. | shall | Annex A |
| OVR-A-02 [PDS][PDS+PGD] | Preserve qualification status info not publicly available. | shall | Annex A |
| OVR-A-02A [PDS][PDS+PGD] | Ensure output of TS 119 172-4 clause 4.4 clearly determines technical suitability. | shall | Annex A |
| OVR-A-03 [PDS][PDS+PGD] | Timestamps should be from qualified TSA. | should | Annex A |
| OVR-A-04 | Have service digital identifier per TS 119 612. | shall | Annex A |