# ETSI TS 119 441 V1.3.1: Policy requirements for TSP providing signature validation services
**Source**: ETSI/ESI | **Version**: 1.3.1 | **Date**: 2025-10 | **Type**: Normative
**Original**: [ETSI TS 119 441 V1.3.1](https://www.etsi.org/deliver/etsi_ts/119400_119499/119441/01.03.01_60/)

## Scope (Summary)
This Technical Specification specifies policy and security requirements for Signature Validation Services (SVS) operated by a Trust Service Provider (TSP), based on ETSI EN 319 401. It covers validation of digital signatures (including advanced and qualified electronic signatures/seals as per Regulation (EU) No 910/2014) and is aimed at both qualified and non-qualified trust services. It does not cover other signature services (creation, augmentation, preservation) or user interfaces (annex D provides recommendations).

## Normative References
- [1] ETSI TS 119 101: "Policy and security requirements for applications for signature creation and signature validation"
- [2] ETSI EN 319 401: "General Policy Requirements for Trust Service Providers"
- [3] ETSI EN 319 102-1: "Procedures for Creation and Validation of AdES Digital Signatures; Part 1: Creation and Validation"
- [4] ISO/IEC 15408 parts 1 to 3
- [5] ISO/IEC 19790
- [6] FIPS PUB 140-2 (2001)
- [7] FIPS PUB 140-3 (2019)
- [8] ETSI TS 119 172-4: "Signature Policies; Part 4: Signature applicability rules (validation policy) for European qualified electronic signatures/seals using trusted lists"
- [9] ETSI EN 319 411-1: "Policy and security requirements for TSP issuing certificates; Part 1: General requirements"

## Definitions and Abbreviations
- **Signature Validation Service (SVS)**: validation service provided by a TSP that validates digital signatures and produces a validation report.
- **Qualified Validation Service for qualified electronic signatures/seals**: as defined in Regulation (EU) No 910/2014, Articles 33 and 40.
- **Signature Validation Application (SVA)**: application that validates a signature against a signature validation policy.
- **Signature Validation Policy**: set of validation constraints processed by the SVA.
- **Signature Validation Report (SVR)**: comprehensive report of the validation process.
- **Proof of Existence (PoE)**: evidence that a signature existed at a certain time.
- Abbreviations: DA (Driving Application), QES (Qualified Electronic Signature/Seal), QSVSP (Qualified Signature Validation Service Provider), SVP (Signature Validation Protocol), SVSP (Signature Validation Service Provider), SVSServ (Signature Validation Service Server), TSP (Trust Service Provider).

## General Concepts

### 4.1 General Policy Requirements Concepts
Incorporates ETSI EN 319 401 [2] requirements by reference and adds SVSP-specific requirements.

### 4.2 SVS Applicable Documentation
- **4.2.1 SVS Practice Statements** – developed, implemented, enforced, and updated by the SVSP; describes how the service is operated.
- **4.2.2 SVS Policy** – describes what is offered; may include OIDs:
  - `itu-t(0) identified-organization(4) etsi(0) val-service-policies(19441) policy-identifiers(1) main (1)` for generic conformance.
  - `itu-t(0) identified-organization(4) etsi(0) val-service-policies(19441) policy-identifiers(1) qualified (2)` for qualified service (including annex B).
- **4.2.3 Terms and Conditions** – specific to SVSP, issued to subscribers and relying parties.
- **4.2.4 Other documents** – signature validation policy (input to SVA) and signature applicability rules (out of scope).

### 4.3 SVS Components and Process
- **Actors**: SVSP, subscriber, user, signer, signer’s TSPs, other TSPs, trusted lists.
- **Architecture**: Signature Validation Client (SVC) and Signature Validation Service Server (SVSServ) implementing SVP and SVA.
- **Process**:
  1. Client submits signed document(s) (SD) or digest(s) and optional validation constraints.
  2. SVSServ performs validation against a signature validation policy (default or client-provided, with conflict resolution).
  3. Output validation response containing report.
  4. Client presents report.

## 5 Risk Assessment
- **OVR-5-01**: The requirements specified in ETSI EN 319 401 [2], clause 5 shall apply.

## 6 Policies and Practices

### 6.1 SVS Practice Statement
- **OVR-6.1-01**: EN 319 401 [2], clause 6.1 shall apply.
- **OVR-6.1-02**: Should be structured per annex A.
- **OVR-6.1-03**: Shall list or reference supported SVS policies.
- **OVR-6.1-04**: Shall identify obligations of external organizations supporting services.

### 6.2 Terms and Conditions
- **OVR-6.2-01**: EN 319 401 [2], clause 6.2 shall apply.
- **OVR-6.2-02**: Shall list or reference supported SVS policies.
- **OVR-6.2-03**: May refer to OIDs from clause 4.2.2.
- **OVR-6.2-03a** [conditional]: If using other OID, the referenced policy shall comply with clause 9.
- **OVR-6.2-04**: Referred SVS policies shall be available to subscriber.
- **OVR-6.2-05** [conditional]: If policy not owned by SVSP, it shall be publicly available.
- **OVR-6.2-06** [conditional]: If not stand-alone, indicate where info is found.
- **OVR-6.1-07**: Terms or referred SVS policy shall list supported signature validation policies.
- **OVR-6.2-08**: Shall describe service options (SDO verification, certificate selection, multiple signatures, validation policy selection, input parameters, supported signature formats).
- **OVR-6.2-09**: Shall document handling of expired/obsolete elements.
- **OVR-6.2-10** [conditional]: When client provides/selects validation policy, describe behavior for conflicts, incomplete policies, inability to process, conditions for ignoring client policy.
- **OVR-6.2-11**: Shall state what is considered PoE.
- **OVR-6.2-12**: Shall indicate rights, obligations, or disclaim responsibilities of actors per clause 4.3.1.
- **OVR-6.2-13** [conditional]: If client computes hash, describe conditions and limitations.
- **OVR-6.2-14**: Shall state which validation algorithm is applied.

### 6.3 Information Security Policy
- **OVR-6.3-01**: EN 319 401 [2], clause 6.3 shall apply.
- **OVR-6.3-02**: Security policy shall document security and privacy controls to protect personal data.

## 7 SVS Management and Operation

### 7.1 Internal Organization
- **OVR-7.1-01**: EN 319 401 [2], clause 7.1 shall apply.

### 7.2 Human Resources
- **OVR-7.2-01**: EN 319 401 [2], clause 7.2 shall apply.

### 7.3 Asset Management
- **OVR-7.3-01**: EN 319 401 [2], clause 7.3 shall apply.

### 7.4 Access Control
- **OVR-7.4-01**: EN 319 401 [2], clause 7.4 shall apply.

### 7.5 Cryptographic Controls
- **OVR-7.5-01**: EN 319 401 [2], clause 7.5 shall apply.
- **OVR-7.5-02**: Void.
- **OVR-7.5-02A** [conditional]: When reports are signed, SVSP public signing certificate shall be issued by a trustworthy CA compliant with NCP+ certificate policy (ETSI EN 319 411-1 [9]).
- **OVR-7.5-03** [conditional]: Private key shall be held in a secure cryptographic device meeting EAL4+ (ISO/IEC 15408, EUCC) or ISO/IEC 19790/FIPS PUB 140-2 level 3 / FIPS PUB 140-3 level 3.
- **OVR-7.5-04** [conditional]: Should be as per OVR-7.5-03 a).
- **OVR-7.5-05** [conditional]: Backup copies of private key shall be protected for integrity and confidentiality by the secure cryptographic device.

### 7.6 Physical and Environmental Security
- **OVR-7.6-01**: EN 319 401 [2], clause 7.6 shall apply.
- **OVR-7.6-02**: Requirement from ETSI TS 119 101 [1], clause 5.2, GSM 1.4 shall apply to SVA.

### 7.7 Operation Security
- **OVR-7.7-01**: EN 319 401 [2], clause 7.7 shall apply.
- **OVR-7.7-02**: Void.
- **OVR-7.7-02A**: SVA shall use application environment maintained with up-to-date security fixes.
- **OVR-7.7-03**: ETSI TS 119 101 [1], clause 5.2, GSM 1.3 shall apply to SVA.
- **OVR-7.7-04**: ETSI TS 119 101 [1], clause 5.2, GSM 2.4 shall apply to SVA.

### 7.8 Network Security
- **OVR-7.8-01**: EN 319 401 [2], clause 7.8 shall apply.
- **OVR-7.8-02** [conditional]: If remote access to systems storing/processing confidential data is allowed, a policy rule shall be adopted and described.
- **OVR-7.8-03** [conditional]: If remote access allowed, appropriate security measures shall be implemented.

### 7.9 Incident Management
- **OVR-7.9-01**: EN 319 401 [2], clause 7.9 shall apply.

### 7.10 Collection of Evidence
- **OVR-7.10-01**: EN 319 401 [2], clause 7.10 shall apply.
- **OVR-7.10-02**: SVSP shall implement event logs for later proofs.
- **OVR-7.10-03**: Any signature validation shall be logged, possibly with subscriber identification.
- **OVR-7.10-04**: Event logs shall be marked with time.
- **OVR-7.10-05**: Frequency, retention, protection, backup, archiving, vulnerability assessment of logs shall be documented in SVS practice statement.
- **OVR-7.10-06**: Implementation shall take applicable privacy requirements into account.
- **OVR-7.10-07**: Event logs should include type, success/failure, identifier of origin.

### 7.11 Business Continuity Management
- **OVR-7.11-01**: EN 319 401 [2], clause 7.11 shall apply.
- **OVR-7.11-02**: Best reasonable efforts shall be undertaken to keep service available as per SLA.
- **OVR-7.11-03**: Measures should be implemented to avoid interruption by third parties or unintentional interruptions.
- **OVR-7.11-04** [conditional]: If reports are signed and expected long-term, SVSP should select signing certificate from CA with clear termination plan.
- **OVR-7.11-05** [conditional]: If reports are signed and long-term, SVSP should select trusted PoE sources (e.g., qualified TSA).

### 7.12 SVS Provisioning Termination and Termination Plans
- **OVR-7.12-01**: EN 319 401 [2], clause 7.12 shall apply.

### 7.13 Compliance and Legal Requirements
- **OVR-7.13-01**: EN 319 401 [2], clause 7.13 shall apply.
- **OVR-7.13-02**: When personal data processed by third party, appropriate agreement shall be made.
- **OVR-7.13-03**: SVSP shall NOT store SD after processing when not necessary.
- **OVR-7.13-04**: SVSP shall have overall responsibility for meeting requirements even when sub-contractors are used.

### 7.14 Supply Chain
- **OVR-7.14-01**: EN 319 401 [2], clause 7.14 shall apply.

## 8 Signature Validation Service Technical Requirements

### 8.1 Signature Validation Process
- **VPR-8.1-01**: Validation process shall comply with ETSI EN 319 102-1 [3].
- **VPR-8.1-02**: Minimal set of constraints may be further specified.
- **VPR-8.1-03**: Shall output status indication and report per signature.
- **VPR-8.1-04**: Status shall be TOTAL-PASSED, TOTAL-FAILED, or INDETERMINATE.
- **VPR-8.1-05**: SVS shall support at least one signature validation policy always available as input.
- **VPR-8.1-06**: May accept several sources of validation policy.
- **VPR-8.1-07**: SVA shall comply with ETSI TS 119 101 [1], clause 7.4, SIA 1 to SIA 4.
- **VPR-8.1-08**: Validation process shall ensure policy used corresponds to strategy defined in SVS policy/terms.
- **VPR-8.1-09**: Strategy principles:
  - [conditional] When client provides policy, SVSP should use it as far as possible.
  - [conditional] When no client policy, SVSP shall use its own.
  - [conditional] When client policy incomplete, SVSP shall complete to reach minimum set.
  - [conditional] When conflict, SVSP shall have process to determine precedence.
- **VPR-8.1-10** [conditional]: When SVSP computes hash, it shall confirm integrity of SD/attribute.
- **VPR-8.1-11** [conditional]: When validating qualified electronic signatures/seals under Regulation (EU) No 910/2014, shall follow ETSI TS 119 172-4 [8].
- **VPR-8.1-12**: For same input, service shall have same output.
- **VPR-8.1-13**: May accept different PoE elements.

### 8.2 Signature Validation Protocol
- **SVP-8.2-01**: Protocol should conform to ETSI TS 119 442 [i.12].
- **SVP-8.2-02** [conditional]: When providing both detailed report and status, shall ensure consistency.
- **SVP-8.2-03**: Response shall bear OID of SVS policy.

### 8.3 Interfaces
#### 8.3.1 Communication Channel
- **SVP-8.3.1-01**: Channel shall be secured; SVSP shall be authenticated; confidentiality ensured.
- **SVP-8.3.1-02**: SVSP may securely authenticate client.

### 8.4 Signature Validation Report
- **SVR-8.4-01**: Shall output status and report providing details of technical validation.
- **SVR-8.4-02**: Report should conform to ETSI TS 119 102-2 [i.3].
- **SVR-8.4-03**: Report shall indicate one of three statuses.
- **SVR-8.4-04**: Report shall report sub-indications as per EN 319 102-1.
- **SVR-8.4-05**: Report shall report on each processed constraint, including implicit ones.
- **SVR-8.4-06** [conditional]: When validated against well-identified policy, report may bear identifier of policy.
- **SVR-8.4-07** [conditional]: When policy not completely processed, report shall report ignored/overridden constraints.
- **SVR-8.4-08**: Report shall bear identity of SVSP.
- **SVR-8.4-09** [conditional]: When following TS 119 102-2, report shall bear "Validator Information".
- **SVR-8.4-10**: Report shall report signer's identity.
- **SVR-8.4-11**: Report shall report on any signed attributes.
- **SVR-8.4-12**: Report shall bear validation process information with identifier indicating process used.
- **SVR-8.4-13** [conditional]: When timestamps present, report should report on timestamp quality.
- **SVR-8.4-14**: Report shall indicate if SVSP did not compute hash but relied on client computation.
- **SVR-8.4-15**: Report shall indicate origin of each PoE.
- **SVR-8.4-16**: Report should bear validation report signature (SVSP's digital signature).
- **SVR-8.4-17** [conditional]: If signed, format and target should conform to TS 119 102-2.
- **SVR-8.4-18** [conditional]: If signed, signature may be basic; no need for timestamp or augmentation.
- **SVR-8.4-19** [conditional]: When report presented via webpage, SVSP shall be authenticated within TLS session.

## 9 Framework for Definition of Validation Service Policies Built on a Trust Service Policy Defined in the Present Document
- **OVR-9-01**: Void.
- **OVR-9-01a**: Shall identify which trust service policy from the present document it adopts as basis.
- **OVR-9-02** [conditional]: Shall identify any variances.
- **OVR-9-03** [conditional]: Subscribers shall be informed of additions/constraints.
- **OVR-9-04** [conditional]: There shall be a body with final authority for specifying and approving policy.
- **OVR-9-05** [conditional]: Risk assessment shall be carried out.
- **OVR-9-06** [conditional]: Policy shall be approved and modified according to defined review process.
- **OVR-9-07** [conditional]: Defined review process shall ensure policy is supported by practice statements.
- **OVR-9-08** [conditional]: TSP shall make supported policies available to user community.
- **OVR-9-09** [conditional]: Revisions shall be made available to subscribers.
- **OVR-9-10** [conditional]: Unique object identifier (OID or URI) shall be obtained for the policy.

## Annexes

### Annex A (informative): Table of Contents for SVS Practice Statements
Provides a recommended structure for SVS practice statements, covering introduction (TSP ID, supported policies, components, definitions), trust service management & operation (internal organization, HR, asset management, access control, cryptographic controls, physical security, operations, network security, incident management, evidence collection, business continuity, termination, compliance, supply chain), and signature validation service design (process, protocol, interfaces, report requirements).

### Annex B (normative): Qualified Validation Service for QES as per Article 33 of Regulation (EU) No 910/2014
- **VPR-B-01**: If QSVSP, all requirements from clauses 5 to 9 shall apply.
- **VPR-B-02**: Shall comply with ETSI TS 119 172-4 [8].
- **OVR-B-03**: Shall test service to demonstrate correct implementation.
- **OVR-B-04**: Tests shall check different use-cases, positive and negative.
- **SVR-B-05**: Validation report shall bear SVSP's digital signature.
- **SVR-B-06**: Report shall be provided in an automated, machine-processable manner.
- **SVR-B-07** [conditional]: When presented via webpage, SVSP should be authenticated via TLS with cert under EN 319 411-2 [i.17] and EN 319 412-4 [i.18].
- **SVR-B-08**: When timestamps present, report shall indicate if qualified.
- **SVR-B-09**: Identity info per SVR-8.4-08/09 shall be under certificate bearing SVSP name as in official statutes.
- **OVR-B-10**: May use qualified service policy OID from clause 4.2.2.
- **VPR-B-11**: SVSP should control hash computation.
- **VPR-B-12**: Signature validation policy shall be clearly identified as for qualified electronic signatures/seals.
- **SVR-B-13**: Report shall indicate whether signature is EU qualified.
- **VPR-B-14**: Report shall allow relying party to detect security relevant issues.
- **VPR-B-15**: Report should comply with ETSI TS 119 102-2 [i.3].
- **VPR-B-16**: When reports signed, SVSP public signing certificate should be issued in compliance with EN 319 411-2 [i.17].

### Annex C (informative): Mapping to Regulation (EU) No 910/2014
Maps requirements of Articles 24.2, 32.1, 32.2, 33.1, and 40 of the Regulation to specific clauses in the present document. Covers qualified TSP requirements, validation conditions, automated result, correct result, and detection of security issues.

### Annex D (informative): Recommendations on User Interface
If user interface is part of SVS, it should (conditional) present result clearly, provide summary and full report, display signer identity, signature validation policy identifier, commitment type, and conform to ETSI TS 119 101 [1] clause 5.1 requirements.

### Annex E (informative): Checklist
A self-assessment or conformity assessment checklist for TSPs offering signature validation services, provided in accompanying spreadsheet `Annex-to-TS_119441_v131.xlsx`.

### Annex F (informative): Validation of Validation Report Signature
Explains that signature on validation report is simpler than complex signature validation; basic verification suffices. The report signature is for integrity and origin, not requiring the same level of complexity. Long-term preservation of validation reports is out of scope.

### Annex G (informative): Change History
Summarizes changes from version 1.1.1 to 1.3.1, including clarifications, updated references, new requirements (e.g., mandatory security policy, software integrity, OID in response, positive/negative testing for QSVSP), and editorial updates.

## Requirements Summary Table
| ID | Requirement (condensed) | Type | Reference |
|---|---|---|---|
| OVR-5-01 | Risk assessment per EN 319 401 clause 5 | shall | 5 |
| OVR-6.1-01 | Practice statement per EN 319 401 clause 6.1 | shall | 6.1 |
| OVR-6.1-03 | List supported SVS policies | shall | 6.1 |
| OVR-6.1-04 | Identify obligations of external orgs | shall | 6.1 |
| OVR-6.2-01 | Terms per EN 319 401 clause 6.2 | shall | 6.2 |
| OVR-6.2-02 | List supported SVS policies | shall | 6.2 |
| OVR-6.2-04 | Referred policies available to subscriber | shall | 6.2 |
| OVR-6.2-07 | List supported signature validation policies | shall | 6.2 |
| OVR-6.2-08 | Describe service options | shall | 6.2 |
| OVR-6.2-09 | Document handling of expired/obsolete elements | shall | 6.2 |
| OVR-6.2-10 | [conditional] Describe behavior when client provides policy | shall | 6.2 |
| OVR-6.2-11 | State what is PoE | shall | 6.2 |
| OVR-6.2-12 | Indicate rights/obligations of actors | shall | 6.2 |
| OVR-6.2-13 | [conditional] If client computes hash, describe conditions | shall | 6.2 |
| OVR-6.2-14 | State validation algorithm | shall | 6.2 |
| OVR-6.3-02 | Security policy document personal data controls | shall | 6.3 |
| OVR-7.1-01 | Internal organization per EN 319 401 clause 7.1 | shall | 7.1 |
| OVR-7.2-01 | HR per EN 319 401 clause 7.2 | shall | 7.2 |
| OVR-7.3-01 | Asset management per EN 319 401 clause 7.3 | shall | 7.3 |
| OVR-7.4-01 | Access control per EN 319 401 clause 7.4 | shall | 7.4 |
| OVR-7.5-01 | Cryptographic controls per EN 319 401 clause 7.5 | shall | 7.5 |
| OVR-7.5-02A | [conditional] Certificate for signing reports under NCP+ | shall | 7.5 |
| OVR-7.5-03 | [conditional] Private key in secure cryptographic device | shall | 7.5 |
| OVR-7.5-05 | [conditional] Backup key protection | shall | 7.5 |
| OVR-7.6-01 | Physical security per EN 319 401 clause 7.6 | shall | 7.6 |
| OVR-7.6-02 | GSM 1.4 from TS 119 101 applies to SVA | shall | 7.6 |
| OVR-7.7-01 | Operation security per EN 319 401 clause 7.7 | shall | 7.7 |
| OVR-7.7-02A | Maintain SVA application environment with security fixes | shall | 7.7 |
| OVR-7.7-03 | GSM 1.3 from TS 119 101 applies to SVA | shall | 7.7 |
| OVR-7.7-04 | GSM 2.4 from TS 119 101 applies to SVA | shall | 7.7 |
| OVR-7.8-01 | Network security per EN 319 401 clause 7.8 | shall | 7.8 |
| OVR-7.8-02 | [conditional] Remote access formal policy | shall | 7.8 |
| OVR-7.8-03 | [conditional] Remote access security measures | shall | 7.8 |
| OVR-7.9-01 | Incident management per EN 319 401 clause 7.9 | shall | 7.9 |
| OVR-7.10-01 | Evidence collection per EN 319 401 clause 7.10 | shall | 7.10 |
| OVR-7.10-02 | Implement event logs | shall | 7.10 |
| OVR-7.10-03 | Log all validations | shall | 7.10 |
| OVR-7.10-04 | Logs with time | shall | 7.10 |
| OVR-7.10-05 | Document log management in practice statement | shall | 7.10 |
| OVR-7.10-06 | Consider privacy requirements | shall | 7.10 |
| OVR-7.11-01 | Business continuity per EN 319 401 clause 7.11 | shall | 7.11 |
| OVR-7.11-02 | Best reasonable efforts for availability | shall | 7.11 |
| OVR-7.12-01 | Termination per EN 319 401 clause 7.12 | shall | 7.12 |
| OVR-7.13-01 | Compliance per EN 319 401 clause 7.13 | shall | 7.13 |
| OVR-7.13-02 | Agreement with third-party processors of personal data | shall | 7.13 |
| OVR-7.13-03 | NOT store SD after processing | shall | 7.13 |
| OVR-7.13-04 | Overall responsibility even with sub-contractors | shall | 7.13 |
| OVR-7.14-01 | Supply chain per EN 319 401 clause 7.14 | shall | 7.14 |
| VPR-8.1-01 | Validation process comply with EN 319 102-1 | shall | 8.1 |
| VPR-8.1-03 | Output status and report per signature | shall | 8.1 |
| VPR-8.1-04 | Status: TOTAL-PASSED/FAILED/INDETERMINATE | shall | 8.1 |
| VPR-8.1-05 | Support at least one validation policy always available | shall | 8.1 |
| VPR-8.1-07 | SVA comply with TS 119 101 SIA 1-4 | shall | 8.1 |
| VPR-8.1-08 | Policy used matches documented strategy | shall | 8.1 |
| VPR-8.1-09 | Strategy principles for policy selection | shall | 8.1 |
| VPR-8.1-10 | [conditional] SVSP computes hash: confirm integrity | shall | 8.1 |
| VPR-8.1-11 | [conditional] Validate qualified signatures: follow TS 119 172-4 | shall | 8.1 |
| VPR-8.1-12 | Same output for same input | shall | 8.1 |
| SVP-8.2-03 | Response bears OID of SVS policy | shall | 8.2 |
| SVP-8.3.1-01 | Communication channel secured | shall | 8.3.1 |
| SVR-8.4-01 | Output status and detailed report | shall | 8.4 |
| SVR-8.4-03 | Status from EN 319 102-1 | shall | 8.4 |
| SVR-8.4-04 | Report sub-indications | shall | 8.4 |
| SVR-8.4-05 | Report all processed constraints | shall | 8.4 |
| SVR-8.4-07 | [conditional] Report ignored/overridden constraints | shall | 8.4 |
| SVR-8.4-08 | Report bears SVSP identity | shall | 8.4 |
| SVR-8.4-09 | [conditional] Validator Information if TS 119 102-2 | shall | 8.4 |
| SVR-8.4-10 | Report signer's identity | shall | 8.4 |
| SVR-8.4-11 | Report signed attributes | shall | 8.4 |
| SVR-8.4-12 | Report validation process information | shall | 8.4 |
| SVR-8.4-14 | Indicate if hash not computed by SVSP | shall | 8.4 |
| SVR-8.4-15 | Indicate origin of each PoE | shall | 8.4 |
| SVR-8.4-19 | [conditional] Webpage: TLS authentication | shall | 8.4 |
| OVR-9-01a | Identify adopted trust service policy | shall | 9 |
| OVR-9-02 | [conditional] Identify variances | shall | 9 |
| OVR-9-03 | [conditional] Inform subscribers of additions/constraints | shall | 9 |
| OVR-9-04 | [conditional] Policy management authority | shall | 9 |
| OVR-9-05 | [conditional] Risk assessment | shall | 9 |
| OVR-9-06 | [conditional] Approved and modified per review process | shall | 9 |
| OVR-9-07 | [conditional] Review process ensures policy support | shall | 9 |
| OVR-9-08 | [conditional] Make policies available | shall | 9 |
| OVR-9-09 | [conditional] Revisions to subscribers | shall | 9 |
| OVR-9-10 | [conditional] Obtain OID/URI | shall | 9 |
| VPR-B-01 | [conditional] QSVSP: all clauses 5-9 apply | shall | B |
| VPR-B-02 | [conditional] Comply with TS 119 172-4 | shall | B |
| OVR-B-03 | [conditional] Test service | shall | B |
| OVR-B-04 | [conditional] Positive and negative tests | shall | B |
| SVR-B-05 | [conditional] Report digitally signed | shall | B |
| SVR-B-06 | [conditional] Automated machine-processable report | shall | B |
| SVR-B-08 | [conditional] Report if timestamp qualified | shall | B |
| SVR-B-09 | [conditional] Identity under certificate | shall | B |
| VPR-B-12 | [conditional] Validation policy identified for qualified sigs | shall | B |
| SVR-B-13 | [conditional] Report indicates EU qualified | shall | B |
| VPR-B-14 | [conditional] Report allows detection of security issues | shall | B |