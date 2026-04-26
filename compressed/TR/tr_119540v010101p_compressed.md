# ETSI TR 119 540: Standardization requirements for Smart Contracts based on Electronic Ledgers
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2025-10 | **Type**: Technical Report (Informative)
**Original**: ETSI TR 119 540, available from ETSI deliver repository

## Scope (Summary)
The present document defines standardization issues for Smart Contracts, as defined in Data Act [i.1], and based on Electronic Ledgers as defined by eIDAS2 [i.2]. It presents a novel Chain of Trust addressing the role of all entities in building, deploying, and executing a Smart Contract on an Electronic Ledger, identifying critical points where governance, safety, security, and identity are required. It serves as a scoping study for the development of ETSI TS 119 541 [i.12] and ETSI TS 119 542 [i.16].

## Normative References
None applicable in this Technical Report.

## Informative References (Selected)
- [i.1] Regulation (EU) 2023/2854 (Data Act)
- [i.2] Regulation (EU) 2024/1183 (eIDAS2)
- [i.3] ISO 22739:2024 (Blockchain and DLT vocabulary)
- [i.4] ETSI TR 119 001 (Definitions and abbreviations for ESI)
- [i.5] ISO/IEC 15408 (Common Criteria)
- [i.6] Regulation (EU) No 910/2014 (eIDAS)
- [i.7] Regulation (EU) 2016/679 (GDPR)
- [i.12] ETSI TS 119 541 (Policy and security requirements for SC using EL)
- [i.16] ETSI TS 119 542 (Use of EUDI Wallets and e-signatures with SC)
- [i.20] UNCITRAL Model Law on Automated Contracting
- [i.24] Rocq theorem prover
- [i.25] Isabelle theorem prover
- [i.26] Lean theorem prover
- [i.27] X. Leroy: Formal verification of a realistic compiler
- [i.28] CEN-CENELEC White Paper 2018
- [i.29] ITU-T F.751.0 (Requirements for DLS)
- [i.30] ITU-T F.751.8 (Technical framework for DLT to cope with regulation)
- [i.31] ITU-T X.1401 (Security threats to DLT)
- [i.32] ITU-T X.1402 (Security framework for DLT)
- [i.33] ITU-T X.1403 (Security guidelines for DLT for decentralized identity)
- [i.34] ITU-T X.1412 (Security requirements for SC management based on DLT)
- [i.35] to [i.65] ETSI ISG PDL deliverables (various)
- [i.66] ISO/IEC 22123-2 (Cloud computing vocabulary)
- [i.67] IEEE 1934-2018 (Fog computing)
- [i.68] Regulation (EU) 2019/881 (Cybersecurity Act)
- [i.69] Commission Implementing Regulation (EU) 2024/482 (EUCC scheme)
- [i.70] ISO/IEC 24760-1 (Identity management framework)
- [i.71] ISO/IEC 29115 (Entity authentication assurance)
- [i.72] Ethereum ERC-721 (NFT Standard)
- [i.73] ISO 20022 (Financial industry message scheme)

## Definitions and Abbreviations
### Terms (from Clause 3.1, preserved verbatim where normative)
- **algorithm**: set of rules and non-ambiguous procedures to solve a class of problems
- **Chain of Trust**: trust needs of legal or natural persons, as used in Regulation (EU) 2024/1183 [i.2], and of the relationships existing among them
- **Deontic Logic**: philosophical logic concerned with obligation, permission, optional, etc.
- **distributed ledger**: ledger that is shared across a set of DLT nodes and synchronized using a consensus mechanism (per ISO 22739 [i.3]). NOTE: A distributed ledger is a special kind of Electronic Ledger.
- **Electronic Ledger**: sequence of electronic data records, ensuring integrity and accurate chronological ordering (per Article 3(52) of [i.2])
- **Qualified Electronic Ledger**: Electronic Ledger provided by a QTSP meeting requirements in Article 45l of [i.2]
- **SC Byte Code**: computer program, written in SC Byte Code Language, executed on a SC VM, produced by compiling SC Source Code
- **SC Byte Code Language**: domain specific language for executing Smart Contracts
- **SC Compiler**: computer program translating SC Source Code into semantically equivalent SC Byte Code (should be open source)
- **SC Compiler Policy, Publisher, Team**: defined entities responsible for SC Compiler
- **SC Deployer, Deployer Policy**: entities responsible for putting SC Byte Code into Electronic Ledger
- **SC Development Policy, Team**: entities producing SC Package
- **SC Documentation**: documentary information supporting the Smart Contract
- **SC Execution Report**: signed evidence of Smart Contract execution
- **SC Language**: domain specific language for defining Smart Contracts
- **SC Language Publisher, Specification, Specification Team, Specification Policy**: entities and artifacts for SC Language
- **SC Legal Team, Legal Text**: entities and legal text attached to SC Source/Byte Code assessing legal basis, requirements, etc. SC Legal Text should refer to SC Compiler and SC VM.
- **SC Oracle**: entity producing external data to Smart Contract to trigger transactions
- **SC Package**: set of files (SC Source Code, SC Byte Code, SC Legal Text, SC Documentation) signed by SC Publisher
- **SC Provider**: legal/natural person responsible for providing and executing a Smart Contract to a SC User
- **SC Provider Policy**: policy governing SC Provider behavior
- **SC Publisher**: entity signing SC Legal Text, Source Code, Byte Code, and Documentation
- **SC Publisher Policy**: policy governing SC Publisher behavior
- **SC Source Code**: computer program in SC Source Code Language defining Smart Contract behavior
- **SC User**: legal/natural person using Smart Contract services provided by SC Provider
- **SC Virtual Machine**: computer program executing SC Byte Code producing records for Electronic Ledger (should be open source)
- **SC Virtual Machine Policy, Team, Publisher**: entities for SC VM
- **Smart Contract**: computer program used for automated execution of an agreement or part thereof, using sequence of electronic data records ensuring integrity and chronological ordering (per Data Act [i.1] Article 2(39)). NOTE: This definition is more general than ISO 22739 [i.3] definition.
- **Smart Legal Contract**: Smart Contract with legal relevance obtained by embedding or pointing a SC Legal Text

### Abbreviations
| Abbr | Full form |
|------|-----------|
| AdES | Advanced Electronic Signature |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| ARF | Architecture and Reference Framework |
| CA | Certificate Authority |
| DAG | Directed Acyclic Graph |
| dAPP | distributed Application |
| DID | Decentralized Identity |
| DLT | Distributed Ledger Technology |
| DPoS | Delegated Proof-of-Stake |
| EAA | Electronic Attestations of Attributes |
| EBSI | European Blockchain Services Infrastructure |
| eID | electronic Identification |
| eIDAS | electronic IDentification, Authentication and trust Services |
| ENISA | European Union Agency for Cybersecurity |
| EU | European Union |
| EUDI(W) | European Digital Identity (Wallet) |
| EVM | Ethereum Virtual Machine |
| GDPR | General Data Protection Regulation |
| HSM | Hardware Security Module |
| INATBA | International Association for Trusted Blockchain Applications |
| IoT | Internet of Things |
| IPFS | InterPlanetary File System |
| ISO | International Organization for Standardization |
| KYC | Know Your Customer |
| NFC | Near Field Communication |
| NFT | Non-Fungible Token |
| NIS2 | Directive (EU) 2022/2555 |
| PDL | Permissioned Distributed Ledger |
| PID | Person Identification Data |
| PIN | Personal Identification Number |
| PKI | Public Key Infrastructure |
| PoS | Proof of Stake |
| PoW | Proof of Work |
| QEAA | Qualified Electronic Attestations of Attributes |
| QES | Qualified Electronic Signature |
| QSeal | Qualified Electronic Seal |
| QTSP | Qualified Trust Service Provider |
| SC | Smart Contract |
| SIM | Subscriber Identity Module |
| SPV | Simplified Payment Verification |
| TSP | Trust Service Provider |
| UNCITRAL | United Nations Commission on International Trade Law |
| UTXO | Unspent Transaction Output |
| VM | Virtual Machine |

## 4. Smart Contracts related regulation, standardization and initiatives
### 4.1 Essential Overview
Reviews all relevant EU Regulations, Standards, Projects, and activities involving Smart Contracts and Electronic Ledgers. For each, provides: Essential Overview, Terminology, Chain of Trust.

### 4.2 Regulations
#### 4.2.1 Data Act (Regulation (EU) 2023/2854)
- **Essential Overview**: Smart Contract definition: "computer program used for automated execution of an agreement or part thereof, using sequence of electronic data records ensuring integrity and accurate chronological ordering". Key objectives: automated execution, party identification, integrity, non-repudiation, privacy.
- **Terminology**: Smart Contracts, Electronic Ledgers.
- **Chain of Trust**: Agnostic.

#### 4.2.2 eIDAS2 (Regulation (EU) 2024/1183)
- **Essential Overview**: Defines Electronic Ledger (Art. 3(52)) and Qualified Electronic Ledger (Art. 3(53) and Art. 45l). Legal effects: data records in a qualified ledger enjoy presumption of unique sequential chronological ordering and integrity. eIDAS2 does not address Smart Contracts directly but Smart Contracts may use Electronic Ledgers.
- **Terminology**: Electronic Ledgers.
- **Chain of Trust**: Agnostic (may change in forthcoming Implementing Acts).

#### 4.2.3 GDPR (Regulation (EU) 2016/679)
- **Essential Overview**: Smart Contracts can support GDPR compliance via automated consent management, tamper-proof tracking, transparency.
- **Terminology**: Not applicable.
- **Chain of Trust**: Agnostic.

#### 4.2.4 UNCITRAL Model Law on Automated Contracting
- **Essential Overview**: Provides legal framework for automation in international contracts, including Smart Contracts and machine-to-machine transactions.
- **Terminology**: Smart Contracts.
- **Chain of Trust**: Agnostic.

### 4.3 Standardization
#### 4.3.1 ISO/TC 307
- **Essential Overview**: Standardization of blockchain and DLT. Produced ISO 22739 (vocabulary), ISO/TS 23635 (governance guidelines), ISO 23257 (reference architecture), ISO 24332 (records management).
- **Terminology**: Smart Contracts and distributed ledgers as per ISO 22739.
- **Chain of Trust**: Agnostic; ISO/TS 23635 discusses trust requirements on (qualified) DLT systems.

#### 4.3.2 CEN/CENELEC/JTC 19
- **Essential Overview**: Adopted ISO TC 307 vocabulary into European Framework. Working on policy and security requirements for trust services providing ledger services.
- **Terminology**: Distributed ledgers and Smart Contracts as per ISO 22739.
- **Chain of Trust**: Agnostic.

#### 4.3.3 ETSI ISG PDL (now ETSI TC DATA)
- **Essential Overview**: Produced many deliverables on permissioned distributed ledgers, Smart Contracts, interoperability, trust, identity, governance. Focus on open ecosystem and regulatory compliance.
- **Terminology**: Electronic Ledgers, distributed ledgers, Smart Contracts as per ISO 22739.
- **Chain of Trust**: Agnostic (will change within ETSI TC DATA).

#### 4.3.4 ITU-T X-Series Recommendations (Study Group 17)
- **Essential Overview**: Standards include F.751.0 (Requirements for DLS), F.751.8 (Technical framework for DLT to cope with regulation), X.1401 (security threats), X.1402 (security framework), X.1403 (security for decentralized identity), X.1412 (security requirements for Smart Contract management).
- **Terminology**: distributed ledgers per F.751.0, Smart Contracts per X.1412.
- **Chain of Trust**: Agnostic; X.1412 contains intuitions on security requirements.

#### 4.3.5 IEEE SA P2418
- **Essential Overview**: Working on blockchain and DLT standards; no published documents at time of writing.
- **Terminology**: None.
- **Chain of Trust**: None.

### 4.4 Projects, Programs and Initiatives
#### 4.4.1 Digital Europe Program
- **Essential Overview**: Funds projects on eIDAS, EUDI Wallet, distributed ledgers, Smart Contracts (e.g., EBSI VECTOR, OnePass, Blockstand, Seeblock).
- **Terminology**: Smart Contracts and distributed ledgers as per ISO 22739.
- **Chain of Trust**: Agnostic.

#### 4.4.2 European Blockchain Services Infrastructure (EBSI)
- **Essential Overview**: EU/EFTA blockchain infrastructure run by member states. Provides framework for verifiable credentials, DID methods, timestamps, API. Currently no Smart Contracts support, but announced deployment possible in March 2025.
- **Terminology**: Smart Contracts and distributed ledgers as per ISO 22739.
- **Chain of Trust**: Agnostic.

#### 4.4.3 European Digital Identity Wallet (EUDI Wallet)
- **Essential Overview**: Core of eIDAS2. Secure, user-centric digital identity solution storing PID, QEAA, EAA, etc. Infrastructure includes Wallet Providers, PID Providers, EAA Providers, Relying Parties. Smart Contracts can automate and enhance security, privacy, roles, trustworthiness.
- **Terminology**: Smart Contracts, SC Provider, SC Publisher.
- **Chain of Trust**: Agnostic.

### 4.5 Others
#### 4.5.1 eIDAS Toolbox – Architecture and Reference Framework (ARF)
- **Essential Overview**: Technical architecture, standards, guidelines for EUDI Wallet implementation.
- **Terminology**: Smart Contracts, Electronic Ledger.
- **Chain of Trust**: Agnostic.

#### 4.5.2 INATBA
- **Essential Overview**: Global forum for DLT developers and users to interact with regulators.
- **Terminology**: Smart Contracts and distributed ledgers as per ISO 22739.
- **Chain of Trust**: Agnostic.

#### 4.5.3 ENISA: Digital Identity Standards
- **Essential Overview**: Comprehensive analysis of standardization requirements for digital identity, covering identity management, trust services, authentication. Recommends continued development of robust digital identity standards. Identity issues in Smart Contracts will be studied in future.
- **Terminology**: Smart Contracts, Electronic Ledger.
- **Chain of Trust**: Agnostic.

## 5. A Chain of Trust in support of Smart Contracts and Electronic Ledgers
### 5.1 Essential Overview
Describes processes for building, deploying, and executing a Smart Contract on an Electronic Ledger. Formally identifies all actors, artifacts, hardware, networks, tools emphasizing critical points for governance, safety, security, identity. **Chain of Trust** occurs at multiple abstraction levels:
- SC Language entities
- SC Tools (compiler, virtual machine)
- SC Legal entities
- SC Published entities
- Electronic Ledger
- Underlying networks
- Hardware (not treated)

Key finding: To satisfy European rules for transparency and accountability, actors must be identifiable per Data Act and eIDAS2. Smart Contracts must be strictly governed to give legal value (Smart Legal Contract). Electronic Ledgers should be permissioned (independent of centralized/distributed implementation). Advanced Electronic Signatures and Qualified Electronic Seals are essential for traceability, authentication, compliance. Common Criteria (ISO/IEC 15408) with appropriate EAL levels is recommended. The Chain of Trust requires validation/identification of tools at each stage: software (authors, compilers, VM), hardware, networks. Smart Contracts can be classified as requiring substantial or high-level assurance per Cybersecurity Act.

### 5.2 SC main entities
#### 5.2.1 Essential Overview (Table 1: The Chain of Trust V1)
| # | Entity | Interacts with | Result produced | Identification needs | Assurance needs |
|---|--------|----------------|-----------------|----------------------|-----------------|
| 1 | SC Language Specification Team | SC Language Publisher | SC Language Specification, SC Language Specification Policy | Signed by SC Language Publisher | Correctness of syntax/semantics; respect of policy |
| 2 | SC Compiler Team | SC Language Publisher | SC Compiler, SC Compiler Policy | Signed by SC Compiler Publisher | Semantic preservation against SC Language Specification; respect of compiler policy |
| 3 | SC Virtual Machine Team | SC Language Publisher | SC Virtual Machine, SC Virtual Machine Policy | Signed by SC Virtual Machine Publisher | Semantic preservation; respect of VM policy |
| 4 | SC Development Team, SC Legal Team | SC Publisher | SC Package (SC Byte Code, Source Code, Legal Text, Documentation); SC Development Policy | Signed by SC Publisher | Assurance that SC package meets SC Development Policy; identified by SC Publisher; employed compiler/VM from reputable publishers |
| 5 | SC Publisher | SC Provider | SC Package | Mutual identification | Assurance that SC Package comes from SC Publisher |
| 6 | SC Provider | SC Deployer | Evidence of legal terms of SC Deployer | Mutual identification | Assurance of legal terms |
| 7 | SC Deployer | Electronic Ledger | Electronic Transaction containing SC Package | Identified by Electronic Ledger | Assurance that SC Package comes from SC Deployer |
| 8 | SC User | SC Provider | Agreement of legal terms; SC User inputs | Mutual identification | Evidence of SC Legal Text; agreement of SC Provider terms; truthfulness of inputs |
| 9 | SC Provider | Electronic Ledger, SC Oracle | Electronic Transaction with inputs | Identified by Electronic Ledger | Assurance of truthfulness of inputs and transactions |

#### 5.2.2 SC Language Specification
Semantics must be unambiguous and comprehensive. Formal methods recommended to verify correctness and security.

#### 5.2.3 SC Compiler
Translates SC Source Code to SC Byte Code. Compatibility between language definitions, compilers, byte codes, virtual machines is capital. Lack of regulation can lead to discrepancies and vulnerabilities. Uniform compiler standards are beneficial.

#### 5.2.4 SC Virtual Machine
Pivotal for execution. Different VMs (EVM, Sealevel) operate under different principles. Standardization needed.

#### 5.2.5 Computer assisted software tools to assess correctness, safety, and security
Formal verification tools (Rocq, Isabelle, Lean) can formally verify SC Languages, Compilers, VMs, and Smart Contracts. Common Criteria evaluation adds security assurance. ITU-T F.751.8 advocates formal methods.

#### 5.2.6 SC Legal Text, Certification of Smart Contract, Agreements
- **Essential Overview**: Translating certified SC Legal Text into Smart Legal Contract requires collaboration of lawyers (SC Legal Team) and engineers (SC Development Team). Formal tools with Deontic Logic libraries help. Reversing translation (bytecode to legal text) is important for legal review.
- **SC Legal Text** includes: legal context, data protection provisions, requirements on SC Deployer Policy, requirements for SC Provider (use of SC Language tools, Electronic Ledger, verification of SC User identities), license terms.
- **Certification of Smart Contract by SC Publisher**: SC Publisher should certify all elements (Legal Text, Source Code, Byte Code, Documentation) based on conformance to SC Development Policy.
- **Verification of legal agreement**:
  - **a) Deployment**: SC Deployer should ensure all elements certified by identified SC Publisher; provide successful validation report; record confirmation that SC Deployer Policy meets legal requirements.
  - **b) Provision**: Before execution, SC Provider should validate SC Publisher signature, confirm SC Provider Policy meets requirements in SC Legal Text, and record in Electronic Ledger.
  - **c) User license terms and conditions**: SC Provider should provide SC User with copy of license.
  - **d) Execution**: SC Provider should record validation of SC User identity and acceptance of license terms; after execution, provide SC Execution Report.

### 5.3 Distributed ledger technology (DLT)
#### 5.3.1 Essential Overview
Highlights gap between legal definitions (Electronic Ledger, Smart Contract) and existing DLT solutions. Chain of Trust should fill this gap.

#### 5.3.2 Permissioned or permissionless
Permissioned: restricted access, authorized participants. Permissionless: open to anyone.

#### 5.3.3 Public or Private
Public: full transparency. Private: access limited to authorized users.

#### 5.3.4 Data structures used to implement a distributed ledger
Summarizes state of the art: Linked List, Merkle Tree, DAG, Patricia Trie, Heap, Bloom Filter, Block Structure, Account Trie, UTXO Set, State Trie, Transaction Pool, Sparse Merkle Trie. Each has specific advantages and examples (Bitcoin, Ethereum, IOTA, etc.).

#### 5.3.5 On-chain and off-chain transaction data solutions
On-chain: stored directly on ledger (e.g., ETH transactions, ERC-721). Off-chain: stored outside (e.g., IPFS, Lightning Network, Plasma, Optimistic Rollups).

### 5.4 Digital trust elements in Smart Contracts
#### 5.4.1 Essential Overview
Aims to understand gap between legal and real solutions. Chain of Trust should fill this gap.

#### 5.4.2 Identification, authentication
- Identity and Access Control: unique identity, role-based access, time-bound.
- Lifecycle Management: planning, design, coding, deployment, ownership, access control.
- Security and Privacy: trusted execution environment, private channels.
- Auditable Libraries: verifiable, approved by governance.
- Enforceability: self-executable, enforceable across jurisdictions.

#### 5.4.3 Electronic signatures and seals
Defines types: Electronic Signature, Advanced Electronic Signature, Qualified Electronic Signature, Electronic Seal, Advanced Electronic Seal, Qualified Electronic Seal. Electronic signatures confirm identity and intent of natural persons; electronic seals ensure authenticity and integrity of documents from legal persons. Methods: PKI, HSM, Smart Card, Digital Signature Software, mobile-ID. Successful validation of signatures should be recorded.

#### 5.4.4 Electronic identity
- **Essential overview**: Per eIDAS2, electronic identification uses person identification data uniquely representing natural or legal persons. Assurance levels (low, substantial, high). Successful validation should be recorded.
- **Electronic identity in a mobile network**: SIM/eSIM as secure storage, mobile device as interface. Benefits: convenience, security, widespread adoption, legal validity. Currently mobile identity schemes far from eIDAS2 compliance.

#### 5.4.5 Distributed ledgers
Prominent DLTs: Hyperledger Fabric, Corda, Quorum, Ethereum, Ripple, IOTA, EOSIO, Stellar, EBSI. Each has specific consensus mechanisms, features, use cases, and standards compliance.

### 5.5 Deployment and Execution of Smart Contracts and Smart Legal Contracts
#### 5.5.1 Essential Overview
Regulations allow flexible deployment/execution environments. Chain of Trust should fill the gap between generic code and legal requirements.

#### 5.5.2 to 5.5.7 Systems
- **Centralized**: compatible with Chain of Trust.
- **Decentralized**: no formal evidence of full compatibility.
- **Distributed**: can be compatible.
- **Peer-to-peer**: no evidence of compatibility.
- **Cloud**: can be compatible.
- **Fog**: can be compatible.

### 5.6 Legal issues in Smart Legal Contracts
#### 5.6.1 Essential Overview
Smart Legal Contract needs validation through legal-tech tools (SC Legal Text). Freedom of form principle applies. Standards needed to map stakeholders.

#### 5.6.2 Legal parties
Standards needed to map correct stakeholders (coders, lawyers) in public environments.

#### 5.6.3 Certified code translation and evidences
TechLawyer (lawyer with CS skills) should discern between code with and without legal relevance. Chain of Trust steps:
- "Plain English" Smart Contract: translation reducing misinterpretation risk.
- "Flow chart" Smart Contract Logic: standards to decant plain English logic to script.
- "Annotations and Code": annotations in code for coherence and interpretation.
- Evidence generation and long-term preservation: ledgers and qualified archiving for digital forensics.

### 5.7 Environmental and sustainability models of Smart Contracts
Not treated in this document.

### 5.8 Underlying networks to support deployment and execution
Per eIDAS2 recital 49, EUDI Wallet providers need fair access to mobile device components (NFC, secure elements). Underlying networks (mobile network operators) can become QTSPs to ensure high trustworthiness. Network infrastructure critical for accessibility and trust.

## 6. Synthetizing the Chain of Trust as a roadmap for ETSI TS 119 541 and ETSI TS 119 542
### 6.1 Essential Overview
Summarizes issues from Clause 5 to be translated into formal requirements in the two technical specifications. Notes:
- Certification of specifications, SC Compiler, SC VM should be specified.
- Requirements for identification and seals on SC Byte Code, signatures on Smart Contract and Electronic Ledger, identification of SC caller.

### 6.2 Electronic identity issues
Standardized electronic identity schemes should be selected for Smart Contracts; guidance for migration of legacy systems.

### 6.3 Cybersecurity issues
TSPs for Electronic Ledgers must meet NIS2 Directive. ETSI EN 319 401 defines general security policy. Example: Bybit hack 2025 would not be possible with Chain of Trust.

### 6.4 Privacy issues
eIDAS signatures allow pseudonyms; eIDAS2 wallets support selective disclosure (ETSI TR 119 476). Non-repudiation must be balanced with privacy. Off-chain secure records can be used.

### 6.5 Governance and Audit issues
Three areas:
1. eIDAS2 requirements for Electronic Ledgers: integrity, chronological ordering; for Qualified Electronic Ledgers: QTSP management, origin, uniqueness, immediate change detection.
2. Multiple QTSPs: common policy and supervision.
3. Smart Contract requirements: secure execution environment; trustworthy computer program.

Governance regime includes community governance permissioning, code signing certificates (CA/Browser Baseline). ETSI TC ESI, ETSI TC DATA, CEN JTC 19, ISO/TS 23635, ITU-T X.1403 provide relevant frameworks.

### 6.6 Programming tools issues
SC Language Specification Team, SC Compiler Team, SC VM Team, SC Language Publisher, SC Compiler Publisher, SC VM Publisher should cooperate. SC Developer Team, SC Legal Team, SC Publisher should cooperate. SC Byte Code should be sealed by SC Language Publisher. ETSI TS 119 542 should specify requirements for identification of SC caller and signed declaration of acceptance.

Formal verification: Publishers should ensure consistency, automated testing, error reporting, security audits.

### 6.7 (Smart) legal issues
- Legal Compliance: SC Publisher ensures compliance.
- Contract-to-Code Translation: accurate translation.
- Audit: immutable audit trail.
- Reverse Engineering: extraction of legal documents.
- Dispute Resolution Integration: automatic or semi-automatic.

### 6.8 Data sharing issues
- Data Privacy: encryption and access control.
- Data Integrity: tamper detection.
- Interoperability: standard data formats and protocols.
- Scalability: handle large volumes.
- Compliance: GDPR, etc.

### 6.9 Decentralized execution issues
- Performance, Reliability, Scalability, Fail-Safe Mechanisms, Auditability.

### 6.10 Interoperability issues
- Cross-Platform Compatibility, Data Standardization, Protocol Support, API Integration, Security.

### 6.11 Networks issues
- Pervasiveness, Reliability, Trustworthiness endorsement, Security, Decentralization, Scalability, Redundancy, Low Latency.

### 6.12 Open-source vs. Closed-source issues
Open-source allows distributed governance; closed-source requires ex ante assessment. Both can be valid if properly governed.

## 7. Conclusions
The Chain of Trust V1 is a first attempt to list interactions between entities, results produced, identification and assurance needs. It will be translated into formal requirements in ETSI TS 119 541 and ETSI TS 119 542.

## Informative Annexes (Condensed)
- **Annex A: An example of the Chain of Trust** – Presents four figures (A.1 to A.4) showing a fine-grained implementation of the Chain of Trust for distributed ledgers: SC Language design, Smart Legal Contract design, deployment, and execution.
- **Annex B: Chain of Trust: Architectural Elements (schematic)** – Figure B.1 depicts the architectural elements of the Chain of Trust.
- **Annex C: Comparative overview of definitions** – Tables comparing legal definitions (Data Act, eIDAS2) and technical definitions (ISO 22739) for Smart Contract, Electronic Ledger, distributed ledger.
- **Annex D: Change history** – Lists document versions and major changes from February 2024 to October 2025.

## Requirements Summary
*(Note: This TR does not contain normative requirements; it identifies issues to be translated into formal requirements in [i.12] and [i.16]. The table below summarizes key normative-style statements from the Chain of Trust and governance clauses.)*

| ID | Requirement (normative language preserved) | Type | Reference |
|----|--------------------------------------------|------|-----------|
| R1 | The semantics of SC Language shall be unambiguous and comprehensive. | shall | Clause 5.2.2 |
| R2 | SC Compiler should be open source. | should | Clause 3.1 (SC Compiler definition) |
| R3 | SC Virtual Machine should be open source. | should | Clause 3.1 (SC Virtual Machine definition) |
| R4 | The SC Publisher should certify all elements of the Smart Contract (SC Legal Text, Source Code, Byte Code, Documentation) based on conformance to SC Development Policy. | should | Clause 5.2.6.3 |
| R5 | Before deployment, SC Deployer shall ensure all elements have been certified by an identified SC Publisher. | shall | Clause 5.2.6.4(a) |
| R6 | Before execution, SC Provider shall validate SC Publisher signature at least against SC Byte Code and record validation report in the Electronic Ledger. | shall | Clause 5.2.6.4(b) |
| R7 | SC Provider shall confirm that SC Provider Policy meets requirements in SC Legal Text and record this in the Electronic Ledger. | shall | Clause 5.2.6.4(b) |
| R8 | Before execution, SC Provider shall provide SC User with a copy of the license terms and record validation of SC User identity and acceptance. | shall | Clause 5.2.6.4(c) |
| R9 | After execution, SC Provider shall provide a SC Execution Report. | shall | Clause 5.2.6.4(d) |
| R10 | SC Language Specification, SC Compiler Policy, and SC Virtual Machine Policy should be open access. | should | Clause 3.1 (definitions) |
| R11 | SC Compiler and SC Virtual Machine should ensure semantic preservation against SC Language Specification. | should | Table 1 |
| R12 | Smart Contracts should be strictly governed to give legal value (Smart Legal Contract). | should | Clause 5.1 |
| R13 | Electronic Ledgers should be permissioned (independent of centralization/distribution). | should | Clause 5.1 |
| R14 | TSPs for Electronic Ledgers shall meet NIS2 Directive requirements. | shall | Clause 6.3 |
| R15 | Qualified Electronic Ledgers shall: be created/managed by one or more QTSPs; establish origin of records; ensure unique sequential chronological ordering; record data so that any change is immediately detectable. | shall | eIDAS2 [i.2] Art. 45l |
| R16 | SC Language Publisher, SC Compiler Publisher, and SC Virtual Machine Publisher should ensure consistency, automated testing, error reporting, and security audits. | should | Clause 6.6 |