# ETSI TS 119 541: Electronic Signatures and Trust Infrastructures (ESI); Policy and security requirements for Smart Contracts using Electronic Ledgers
**Source**: ETSI | **Version**: V1.1.1 | **Date**: October 2025 | **Type**: Normative
**Original**: https://www.etsi.org/deliver/etsi_ts/119500_119599/119541/01.01.01_60/ts_119541v010101p.pdf

## Scope (Summary)
This Technical Specification specifies policy and security requirements for Smart Contracts (SCs) using Electronic Ledgers as defined in Regulation (EU) 910/2014 amended by Regulation (EU) 2024/1183, and with other trustworthy tools, extending provisions from ETSI EN 319 401 and TS 18264.
The present document applies the structure of ETSI EN 319 401 to the SC context; references to TSP in that standard shall be read as “SC Provider”.

## Normative References
- [1] ETSI EN 319 401: "Electronic Signatures and Trust Infrastructures (ESI); General Policy Requirements for Trust Service Providers".
- [2] TS 18264: "Policy and security requirements on trust services on electronic ledgers" (CEN/CENELEC).
- [3] ETSI EN 319 403-1: "Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment; Part 1: Requirements for conformity assessment bodies assessing Trust Service Providers".
- [4] ISO 23257:2022: "Blockchain and distributed ledger technologies — Reference architecture".
- [5] ETSI TS 119 542: "Electronic Signatures and Trust Infrastructures (ESI); Use of EU Digital Identity Wallets and electronic signatures for identification with smart contracts".

## Definitions and Abbreviations
- **governance**: action or manner of governing the Smart Contract and its stakeholders
- **policy**: course or principle of action adopted or proposed by an organization or individual
- **trustworthy**: able to be relied on as honest or truthful
- **Abbreviations**: CA, CIA, CRA, DPIA, ENISA, GDPR, NIS2, SBOM, SC, T&C, TSP, URL, VM

## 4 Policy framework introduction
The present document extends ETSI TR 119 540 [i.1] specifying requirements for SCs using Electronic Ledgers over the lifecycle: SC Provision, SC Deployment, SC Execution.
The SC provider shall be determined by the responsibility it holds towards users.
The SC provider shall be responsible for making sure the Smart Contract works correctly and reliably.
Core Policy defines requirements for SC Provider (clauses 7, 8), SC Program Publisher (clause 8.2), and SC Language Publisher (clause 8.3). Electronic Ledger provider requirements are covered by TS 18264 [2].
If the same legal entity provides SC and TSP services, conformance can be certified together under EN 319 403-1 [3].

## 5 Risk Assessment
REQ-5-01: The SC provider shall carry out a risk assessment to identify, analyse and evaluate risks taking into account business and technical issues, in particular addressing the supply chain issues as in clause 8.
REQ-5-02: The SC provider shall select the appropriate risk treatment measures, taking account of the risk assessment results. The risk treatment measures shall ensure that the level of security is commensurate to the degree of risk.
REQ-5-03: The SC provider shall determine all security requirements and operational procedures necessary to implement the risk treatment measures chosen, as documented in clauses 6, 7 and 8.
REQ-5-04: The risk assessment shall be regularly reviewed and revised.
REQ-5-05: The responsible entity of the SC provider (e.g. a specified SC provider management role) shall approve the risk assessment and accept the residual risk identified.
REQ-5-05a: The responsible entity shall be identifiable using methods defined in ETSI TS 119 542 [5].
REQ-5-06: The SC provider shall perform a DPIA as outlined in GDPR [i.14], Article 35.

## 6 SC provider Policies and practices
### 6.1 SC provider Service Practice statement
REQ-6.1-01: The SC provider shall specify the set of policies and practices appropriate for the SC services it is providing.
REQ-6.1-02: The set of policies and practices shall be approved by a responsible entity of the SC provider, published and communicated to employees and external parties as relevant.
REQ-6.1-02a: The responsible entity shall be identifiable using methods defined in ETSI TS 119 542 [5].

### 6.2 Terms and Conditions
REQ-6.2-01: The SC provider shall make the terms and conditions regarding its services available to all SC users and relying parties.
REQ-6.2-02: Terms and conditions shall specify: a) SC policy applied; b) limitations on use; c) obligations of each stakeholder; d) information for relying parties; e) retention period of event logs; f) limitations of liability; g) applicable legal system; h) complaints and dispute settlement; i) conformity assessment; j) contact information; k) availability undertakings.
REQ-6.2-03: Parties relying on service shall be informed of precise terms and conditions before entering into a contractual relationship.
REQ-6.2-04: Terms and conditions shall be made available through a durable means of communication.
REQ-6.2-05: Terms and conditions shall be available in a readily understandable language.
REQ-6.2-06: Terms and conditions may be transmitted electronically.
REQ-6.2-07: Terms and conditions shall make clear how obligations from GDPR, in particular Article 16 (Right to rectification) and Article 17 (Right to erasure), are addressed where data is stored on an Electronic Ledger.
REQ-6.2-08: The SC publisher shall ensure and record that the deployment policy meets the requirements for deployment in the SC Legal Text.

### 6.3 Information security policy
REQ-6.3-01: The SC provider shall define a network and information security policy approved by management, covering ten points (business strategy, objectives, continual improvement, resources, communication, roles, documentation retention, topic-specific policies, monitoring indicators, date of approval).
REQ-6.3-02: Changes to the information security policy shall be communicated to third parties where applicable.
REQ-6.3-03: The policy shall be documented, implemented, maintained, and reviewed at least annually or when significant incidents/ changes occur.
REQ-6.3-04: The SC provider shall establish procedures to notify important changes in service provision to appropriate parties.
REQ-6.3-05: The SC provider shall publish and communicate the information security policy to all impacted employees.
REQ-6.3-06: The policy and asset inventory shall be reviewed at planned intervals or upon significant changes.
REQ-6.3-07: Any changes impacting level of security shall be approved by the management body.
REQ-6.3-08: Configuration of systems shall be regularly checked for changes violating security policies.
REQ-6.3-09: The maximum interval between checks shall be documented in the trust service practice statement.

## 7 SC provider management and operation
### 7.1 Internal organization
The provisions of ETSI EN 319 401 [1], clause 7.1 apply.
### 7.2 Human resources
The provisions of ETSI EN 319 401 [1], clause 7.2 apply.
### 7.3 Asset management
General, inventory, and storage media handling per ETSI EN 319 401 [1] clauses 7.3.1–7.3.3. Where an Electronic Ledger is used, TS 18264 [2] applies.
### 7.4 Access control
The provisions of ETSI EN 319 401 [1], clause 7.4 apply.
### 7.5 Cryptographic controls
The provisions of ETSI EN 319 401 [1], clause 7.5 apply. Due consideration shall be given to crypto-agility.
### 7.6 Physical and environmental security
The provisions of ETSI EN 319 401 [1], clause 7.6 apply.
### 7.7 Operation security
The provisions of ETSI EN 319 401 [1], clause 7.7 apply.
### 7.8 Network security
The provisions of ETSI EN 319 401 [1], clause 7.8 apply. See also NIS2 [i.6] and CRA [i.5].
### 7.9 Vulnerabilities and Incident management
- **7.9.1 Monitoring and logging**: Provisions of ETSI EN 319 401 [1], clause 7.9.1 apply, with notes on compliance with NIS2 and CRA.
- **7.9.2 Incident response**: Provisions of ETSI EN 319 401 [1], clause 7.9.2 apply, with suggested extensions from CRA clause C.2.
- **7.9.3 Reporting**: Provisions of ETSI EN 319 401 [1], clause 7.9.3 apply.
- **7.9.4 Event assessment and classification**: Provisions of ETSI EN 319 401 [1], clause 7.9.4 apply.
- **7.9.5 Post-incident reviews**: Provisions of ETSI EN 319 401 [1], clause 7.9.5 apply.
### 7.10 Collection of evidence
The provisions of ETSI EN 319 401 [1], clause 7.10 apply.
### 7.11 Business continuity management
General, back up, and crisis management per ETSI EN 319 401 [1] clauses 7.11.1–7.11.3 apply.
### 7.12 Termination and termination plans
The provisions of ETSI EN 319 401 [1], clause 7.12 apply.
### 7.13 Compliance
The provisions of ETSI EN 319 401 [1], clause 7.13 apply. See also Annex B for audit requirements.

## 8 SC Provider and SC Supply Chain Requirements
### 8.1 General
The provisions of ETSI EN 319 401 [1], clause 7.14 apply.
### 8.2 SC Publisher
REQ-8.2-1: The provisions of clause 5 apply to the SC publisher.
REQ-8.2-2: The SC publisher shall specify the set of policies and practices for development of the SC.
REQ-8.2-3: The SC publisher shall ensure policies and practices are applied by the SC development team.
REQ-8.2-4: The SC publisher shall ensure SC meets GDPR requirements, including any use of Electronic Ledgers.
REQ-8.2-5: SC policies and practices shall ensure that the employed SC Compiler and SC VM come from a recognized compiler conforming to the SC Language.
### 8.3 SC Language Publisher and Supporting Tools Publishers
REQ-8.3-1: The SC Language Publisher shall specify the language with well-defined semantics and syntax.
REQ-8.3-2: The publisher of any SC language software tool (e.g. compiler, virtual machine) shall ensure it conforms to the SC Language from an identified publisher.
### 8.4 SC Provider
REQ-8.4-1: The SC provider shall ensure the Smart Contract has been designed to offer access control mechanisms and a very high degree of robustness to avoid functional errors and to withstand manipulation by third parties.
REQ-8.4-2: The SC provider shall ensure a mechanism exists to terminate continued execution of transactions and that the Smart Contract includes internal functions to reset, stop, or interrupt operation.
REQ-8.4-3: The SC provider shall ensure that when a Smart Contract has to be terminated/deactivated, transactional data, logic, and code can be archived for auditability.
REQ-8.4-4: The SC provider shall ensure consistency with the terms of the data sharing agreement that the Smart Contract executes, by ensuring the agreement in natural language can be mapped to byte-code and virtual machine environment.
### 8.5 Electronic Ledger Provider(s)
REQ-8.5-1: Electronic Ledger Provider(s) shall apply requirements of ETSI EN 319 401 as appropriate.
REQ-8.5-2: Electronic Ledger Provider(s) shall protect records to meet objectives defined in Regulation 910/2014 as amended (Article 3(52)).
REQ-8.5-3: Electronic Ledger Provider(s) shall be independently assessed against a common policy.
REQ-8.5-4: The security practices recommended in TS 18264 [2] shall apply.
REQ-8.5-5: Electronic Ledgers in the context of Smart Contracts shall meet requirements of TS 18264 and: a) created/managed by one or more providers; b) establish origin of data records; c) ensure unique sequential chronological ordering; d) record data such that any subsequent change is immediately detectable.

## Annex A (normative): Security framework and requirements
### A.1 Security analysis and justifications
Five security objectives derived from Data Act definition: (1) automated execution reflects agreement, (2) correct identification of parties, (3) integrity and chronological ordering, (4) non-repudiation, (5) privacy. Parties must be bound to eIDAS2 governance. Smart contracts must be transparent and explicable.
### A.2 Confidentiality, Integrity, Availability (CIA)
- **Confidentiality**: No specific requirement for full secrecy; parties may be pseudonymous. Native ledger mechanisms should be enabled.
- **Integrity**: Executable elements shall not be modifiable without evidence; each record stored in the ledger shall be protected against unauthorized modification.
- **Availability**: Includes identification, authentication, and access control; availability assured by ledger persistence.
### A.3 Non-repudiation requirements
Parties shall not be able to deny actions. All entries and state changes shall be strongly linked to an identifiable party, securely timestamped, and part of the immutable ledger.
### A.4 GDPR risk and obligations
A DPIA shall be performed per Article 35 of GDPR. If personal data is processed, the SC provider shall identify Data Controller and Data Processor. Data Controller = SC Provider; Data Processor = SC itself. Conflicts with right to erasure/rectification should be addressed in T&Cs and by avoiding storage of personal data where practical.

## Annex B (informative): Audit requirements
Audit requirements per ETSI EN 319 403-1 [3] apply, with substitution of TSP references to SC context. Audit teams shall have demonstrable knowledge of legal, technical, and risk factors of Smart Contracts.

## Annex C (informative): CRA essential requirements and impact on SC
Maps essential requirements from Cyber Resilience Act (CRA) [i.5] Annex I to SC context. Covers secure design, vulnerability handling, updates, access control, confidentiality, integrity, availability, etc. Also maps vulnerability handling requirements (C.2) to SC context, noting that SBOMs and coordinated vulnerability disclosure apply.

## Annex D (informative): Bibliography
Lists additional references: ETSI EN 319 521, TS 119 411-5, EN 319 411-2.

## Requirements Summary
| ID | Requirement (abbreviated) | Type | Reference |
|---|---|---|---|
| REQ-5-01 | Risk assessment shall be performed including supply chain. | shall | 5 |
| REQ-5-02 | Select risk treatment commensurate to risk. | shall | 5 |
| REQ-5-03 | Determine security requirements and operational procedures. | shall | 5 |
| REQ-5-04 | Risk assessment regularly reviewed. | shall | 5 |
| REQ-5-05 | Responsible entity approves risk assessment. | shall | 5 |
| REQ-5-05a | Entity identifiable per TS 119 542. | shall | 5 |
| REQ-5-06 | Perform DPIA per GDPR Art. 35. | shall | 5 |
| REQ-6.1-01 | Specify policies and practices. | shall | 6.1 |
| REQ-6.1-02 | Approved, published, communicated. | shall | 6.1 |
| REQ-6.1-02a | Entity identifiable per TS 119 542. | shall | 6.1 |
| REQ-6.2-01 | T&Cs available to all users. | shall | 6.2 |
| REQ-6.2-02 | T&Cs specify listed items (a–k). | shall | 6.2 |
| REQ-6.2-03 | Relying parties informed before contract. | shall | 6.2 |
| REQ-6.2-04 | Durable means of communication. | shall | 6.2 |
| REQ-6.2-05 | Readily understandable language. | shall | 6.2 |
| REQ-6.2-06 | May be transmitted electronically. | may | 6.2 |
| REQ-6.2-07 | Address GDPR Art. 16/17. | shall | 6.2 |
| REQ-6.2-08 | Deployment policy meets SC Legal Text. | shall | 6.2 |
| REQ-6.3-01 | Define information security policy with 10 points. | shall | 6.3 |
| REQ-6.3-02 | Communicate changes to third parties. | shall | 6.3 |
| REQ-6.3-03 | Policy documented, implemented, reviewed annually. | shall | 6.3 |
| REQ-6.3-04 | Procedures for important changes. | shall | 6.3 |
| REQ-6.3-05 | Publish and communicate to employees. | shall | 6.3 |
| REQ-6.3-06 | Review policy and inventory at planned intervals. | shall | 6.3 |
| REQ-6.3-07 | Changes impacting security approved by management. | shall | 6.3 |
| REQ-6.3-08 | Regular configuration checks. | shall | 6.3 |
| REQ-6.3-09 | Maximum interval documented. | shall | 6.3 |
| REQ-8.2-1 | Clause 5 applies to SC publisher. | shall | 8.2 |
| REQ-8.2-2 | Specify policies and practices for development. | shall | 8.2 |
| REQ-8.2-3 | Ensure applied by development team. | shall | 8.2 |
| REQ-8.2-4 | Ensure GDPR compliance. | shall | 8.2 |
| REQ-8.2-5 | Ensure compiler/VM conform to language. | shall | 8.2 |
| REQ-8.3-1 | Language publisher specifies well-defined semantics/syntax. | shall | 8.3 |
| REQ-8.3-2 | Tool publishers ensure conformance to SC Language. | shall | 8.3 |
| REQ-8.4-1 | SC designed with access control and robustness. | shall | 8.4 |
| REQ-8.4-2 | Mechanism to terminate execution. | shall | 8.4 |
| REQ-8.4-3 | Archival on termination for auditability. | shall | 8.4 |
| REQ-8.4-4 | Ensure consistency with data sharing agreement and mapping to byte-code. | shall | 8.4 |
| REQ-8.5-1 | Electronic Ledger Providers apply EN 319 401. | shall | 8.5 |
| REQ-8.5-2 | Protect records per eIDAS2 Art. 3(52). | shall | 8.5 |
| REQ-8.5-3 | Independently assessed against common policy. | shall | 8.5 |
| REQ-8.5-4 | Security practices of TS 18264 shall apply. | shall | 8.5 |
| REQ-8.5-5 | Meet TS 18264 plus five specific requirements (a–e). | shall | 8.5 |