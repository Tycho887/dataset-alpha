# ETSI SR 003 186 V2.1.1: Electronic Signatures and Infrastructures (ESI) – Testing interoperability and conformity activities to be run during the implementation and promotion of the framework of digital signatures
**Source**: ETSI | **Version**: V2.1.1 | **Date**: April 2016 | **Type**: Special Report  
**Original**: [Not provided]

## Scope (Summary)
This document details a proposal for ETSI activities related to testing conformance and interoperability, performed in parallel with the building up and promotion of the Rationalized Framework for Electronic Signature Standardization (ETSI TR 119 000). It identifies critical deliverables (European Standards and Technical Specifications) that benefit from testing events, proposes a scheduling of events for interoperability and conformance testing, and defines the development and deployment plan for conformity testing tools. The document covers the period Q4 2015 to Q4 2016.

## Normative References
Not applicable.

## Informative References (Selected)
- [i.1] ETSI TR 119 000: "The framework for standardization of signatures: overview"
- [i.2] CEN CWA 16408: "Testing Framework for Global eBusiness Interoperability Test Beds (GITB)"
- [i.3] OASIS Standard: "Test Assertions Model Version 1.0"
- [i.4] Commission Decision 2011/130/EU
- [i.5] Commission Decision 2009/767/EC
- [i.6] Commission Decision 2010/425/EU
- [i.7] ETSI TS 119 312: "Cryptographic Suites"
- [i.8] ETSI TS 101 733: "CMS Advanced Electronic Signatures (CAdES)"
- [i.10] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)"
- [i.11] ETSI TS 103 171: "XAdES Baseline Profile"
- [i.13] ETSI TS 102 778-2: "PDF Advanced Electronic Signature Profiles; Part 2: PAdES Basic"
- [i.14] ETSI TS 102 778-3: "PAdES Enhanced - PAdES-BES and PAdES-EPES Profiles"
- [i.15] ETSI TS 102 778-4: "PAdES Long Term - PAdES LTV Profile"
- [i.16] ETSI TS 102 778-5: "PAdES for XML Content"
- [i.18] ETSI TS 102 918: "Associated Signature Containers (ASiC)"
- [i.20] ETSI TS 119 612: "Trusted Lists"
- [i.21] ETSI TS 102 231: "Provision of harmonized Trust-service status information"
- [i.22] ETSI TS 102 853: "Signature validation procedures and policies"
- [i.23] ETSI EN 319 412-2: "Certificate Profile for certificates issued to natural persons"
- [i.24] ETSI EN 319 412-3: "Certificate Profile for certificates issued to legal persons"
- [i.25] ETSI EN 319 412-5: "QCStatements"
- [i.28] ETSI TS 119 134 (all parts): "XAdES Testing Compliance & Interoperability"
- [i.29] ETSI TS 119 144 (all parts): "PAdES Testing Compliance & Interoperability"
- [i.30] ETSI TS 119 164 (all parts): "ASiC Testing Compliance & Interoperability"
- [i.31] ETSI TS 119 164-2: "Test Suite for ASiC interoperability test events"
- [i.32] IETF RFC 3161: "Internet X.509 Public Key Infrastructure Time-Stamp Protocol"
- [i.33] IETF RFC 3281: "An Internet Attribute Certificate Profile for Authorization"
- [i.34] ETSI EN 319 122-1: "CAdES digital signatures; Part 1: Building blocks and baseline signatures"
- [i.35] ETSI EN 319 122-2: "Extended CAdES signatures"
- [i.36] ETSI EN 319 132-1: "XAdES digital signatures; Part 1: Building blocks and baseline signatures"
- [i.37] ETSI EN 319 132-2: "Extended XAdES signatures"
- [i.38] ETSI EN 319 142-1: "PAdES digital signatures; Part 1: Building blocks and baseline signatures"
- [i.39] ETSI EN 319 142-2: "Additional PAdES signatures profiles"
- [i.40] ETSI EN 319 162-1: "Associated Signature Containers (ASiC); Part 1: Building blocks and baseline containers"
- [i.41] ETSI EN 319 162-2: "Additional ASiC containers"
- [i.42] Directive 2014/24/EU on public procurement
- [i.43] IETF RFC 4998: "Evidence Record Syntax (ERS)"
- [i.44] IETF RFC 6283: "Extensible Markup Language Evidence Record Syntax (XMLERS)"
- [i.45] Commission Implementing Decision (EU) 2015/1506
- [i.46] ETSI EN 319 102-1: "Procedures for Creation and Validation of AdES Digital Signatures; Part 1: Creation and Validation"
- [i.47] ETSI TS 119 124 (all parts): "CAdES digital signatures Testing Conformance and Interoperability"
- [i.48] ETSI TS 119 614: "Test suites and tests specifications for Technical Conformity & Interoperability Testing of Trusted Lists"

## Definitions and Abbreviations

### Definitions
- **conformance testing**: process of verifying that a single implementation conforms to the individual requirements of one or more standards or specifications or profiles.
- **interoperability testing**: process for verifying that several implementations can interoperate while conforming to one or more standards or specifications or profiles (derived from CEN CWA 16408 [i.2]).
- **Plugfest**: interoperability testing event about a standard or a profile where the participants test each other their implementations.
- **Plugtests™**: testing events developed and hosted by ETSI where participants can test interoperability or conformance of implementations.
- **profile**: agreed upon subset or interpretation of one or more norms or technical specifications, intended to achieve interoperability while adapting to specific needs of a user community or purpose (derived from CEN CWA 16408 [i.2]).
- **test assertion**: testable or measurable expression for evaluating the adherence of an implementation to one or more normative statements in a specification, in a way that can be measured or tested (derived from OASIS Standard [i.3]).

### Abbreviations
- ASN: Abstract Syntax Notation
- EUMS: European Union Member State
- FTB: Final draft for Technical Body approval
- LDAP: Lightweight Directory Access Protocol
- OJ: Official Journal
- PKI: Public Key Infrastructure
- PTS: Publication of the Technical Specification
- RFC: Request For Comment
- SPR: Stable Draft for Public Review
- TC: Test Case
- TSA: Time Stamping Authority
- XSLT: eXtensible Stylesheet Language Transformations

## 4 Technical Approach and Methodology for Conformance and Interoperability Testing

### 4.1 Introduction
- Conformance testing verifies that a single implementation meets individual requirements of a standard. It is unit testing, methodical but limited in scope.
- Interoperability testing verifies that multiple implementations can interoperate. It is system testing, complementary to conformance.
- Both are essential for achieving interoperability, and plugfests (ETSI Plugtests) are cost-effective ways to test both.

### 4.2 Gathering Inputs
- Inputs: past Plugtests, critical deliverables of the Framework ETSI TR 119 000 [i.1], ongoing standardization activities.
- Aim: identify standards that benefit from testing events and plan development of conformity testing tools.
- External works considered: CEN CWA 16408 [i.2] and OASIS Test Assertions [i.3].

### 4.3 Standards to be Targeted by Testing Events – Criteria
- **Criteria**: relevance of standards to the framework and expected stakeholder eagerness to participate.
- Standards meeting criteria:
  - Signature formats (CAdES, XAdES, PAdES, ASiC) in support of Commission Decisions [i.4], [i.45].
  - Trusted list management (ETSI TS 119 612 [i.20]) in support of [i.5], [i.6].
  - Electronic Delivery and other TASPs/TSPs (future regulation).
  - Electronic procurement and business (Directive 2014/24/EU [i.42]).
- At present, only the first two groups are mature enough for a complete plan. Others will be reconsidered in future releases.

### 4.4 Criteria to Identify the Scope of Testing Events
- A testing event scope is defined by: (1) format tested; (2) specific part of standard (core, baseline, other profiles); (3) type of tests (interoperability or conformance); (4) supporting PKI(s) (simple, complex, real EUMS Trusted Lists); (5) test suites.
- Experience shows that testing multiple formats in one event is difficult; each event shall focus on a single format.
- Scheduling may include different testing event components on the same format to allow effective testing.

### 4.5 Rules to Identify Priorities in Testing Event Scheduling
Priority is given to specifications matching:
- long time since last event on the same format (see Annex A);
- presence of new substantial features in the specification not tested before;
- availability of new features during ongoing development;
- updates to test suites and availability of related testing tools.

## 5 Standards Targeted for Testing and Testing Specifications

### 5.1 Identification of Standards that Benefit from Conformance and Interoperability Testing Events
Table 1 (summarized):
- **CAdES** (ETSI EN 319 122-1 [i.34], EN 319 122-2 [i.35]): Last Plugtest June 2015; major changes include new Archive Time Stamp attribute (archive-time-stamp-v3 with ats-hash-index-v3), new signer attributes (signer-attributes-v2, claimed-SAML-assertion), new signature-policy-store attribute. Future events should test final ENs and archive-time-stamp-v3 with multiple attribute values.
- **XAdES** (ETSI TS 101 903 [i.10], draft EN 319 132-1 [i.36], EN 319 132-2 [i.37]): Last Plugtest October 2015; major changes include management of signed ds:Manifest elements, new RenewedDigests element, new properties (substituting SigningCertificate, SignerRole, etc.), new SignaturePolicyStore. Future events should test new attributes and definitive ENs.
- **PAdES** (ETSI EN 319 142-1 [i.38], EN 319 142-2 [i.39]): Last Plugtest May 2015; major changes include new signer-attributes-v2 in CMS data, clarification of DSS and DTS fields.
- **ASiC** (ETSI EN 319 162-1 [i.40], EN 319 162-2 [i.41]): Last Plugtest June 2016; major changes include long term attributes and use of Evidence Records (RFC 4998, RFC 6283).
- **Procedures for Signature Creation and Validation** (ETSI EN 319 102-1 [i.46], ETSI TS 102 853 [i.22]): Future events should consider EN 319 102-1 in place of TS 102 853, and certificate profiles EN 319 412-2 [i.23], EN 319 412-3 [i.24], EN 319 412-5 [i.25]. Evidence Records when applicable.

### 5.2 List of Technical Specifications for Testing Conformance and Interoperability

#### 5.2.0 Introduction
The following TSs define test suites for interoperability and conformance. Test execution may require cryptographic algorithms; selection should consider ETSI TS 119 312 [i.7].

#### 5.2.1 CAdES Testing Conformance and Interoperability
- **ETSI TS 119 124** [i.47]:
  - Part 2: Test suites for interoperability of CAdES baseline signatures.
  - Part 3: Test suites for interoperability of extended CAdES signatures.
  - Part 4: Specifications for conformance of CAdES baseline signatures.
  - Part 5: Specifications for conformance of extended CAdES signatures.

#### 5.2.2 XAdES Testing Conformance and Interoperability
- **ETSI TS 119 134** [i.28]:
  - Part 2: Test suites for interoperability of XAdES baseline signatures.
  - Part 3: Test suites for interoperability of extended XAdES signatures.
  - Part 4: Specifications for conformance of XAdES baseline signatures.
  - Part 5: Specifications for conformance of extended XAdES signatures.

#### 5.2.3 PAdES Testing Conformance and Interoperability
- **ETSI TS 119 144** [i.29]:
  - Part 2: Reviewed test suites for interoperability of PAdES baseline signatures.
  - Part 3: Test suites for interoperability of additional PAdES signatures.
  - Part 4: Specifications for conformance of PAdES baseline signatures.
  - Part 5: Specifications for conformance of additional PAdES signatures.

#### 5.2.4 ASiC Testing Conformance and Interoperability
- **ETSI TS 119 164** [i.30]:
  - Part 2: Reviewed test suites for interoperability of ASiC baseline containers.
  - Part 3: Test suites for interoperability of ASiC extended containers.
  - Part 4: Specifications for conformance of ASiC baseline containers.
  - Part 5: Reviewed specifications for conformance of ASiC extended containers.

#### 5.2.5 Testing Conformance of Trusted Lists
- **ETSI TS 119 614-2** [i.48]: Specifications for testing compliance of XML representation of Trusted Lists.

## 6 Planning of Identified Activities

### 6.1 Proposed Scheduling and Scoping of Testing Events
Table 2 (summarized):
| Targeted Spec | Proposed Date | Supporting PKIs | Interoperability | Conformance |
|---------------|---------------|-----------------|------------------|--------------|
| eSignature Validation | April 2016 | EUMS Trusted Lists conformant to ETSI TS 119 612 [i.20] | Validation per ETSI EN 319 102-1 [i.46] | Conformance checking against EN 319 122-1, 319 132-1, 319 142-1, 319 162-1 and previous versions |
| CAdES | November 2016 | Simple PKI and more complex PKI | Test cases from previous events + TC on ETSI EN 319 122 [i.34][i.35] including Evidence Records | – |
| ASiC | June 2016 | Simple PKI and more complex PKI | Test cases from previous events + TC on ETSI EN 319 162 including Evidence Records | – |

Detailed schedule:
1. **E-Signature Validation Plugtest** (March 2016): Interoperability event on validation of XAdES, PAdES, CAdES, ASiC signatures between Member States, relying on Member States' Trusted Lists and ETSI EN 319 102-1 [i.46].
2. **ASiC Plugtest** (June 2016): Remote interoperability and conformance testing on baseline and extended ASiC containers per ETSI EN 319 162 [i.40][i.41] and test specification ETSI TS 119 164-2 [i.31].
3. **CAdES Plugtest** (November 2016): Remote interoperability and conformance testing on CAdES baseline and extended signatures per ETSI EN 319 122-1 [i.34], EN 319 122-2 [i.35], and new TS including Evidence Records, according to draft EN 319 102-1 [i.46].

### 6.2 Planning for the Production of Technical Specifications for Testing Conformance and Interoperability

#### 6.2.0 Introduction
Deliverable milestones:
- **SPR** (Stable Draft for TB Review): Ready for ETSI ESI member comments.
- **FTB** (Final Draft for Technical Body approval): Ready for final approval.
- **PTS** (Publication as TS): Published after editorial check.

All TSs will be aligned to the new ENs (ETSI EN 319 122, EN 319 132, EN 319 142, EN 319 162) and the latest TS 119 612 [i.20] for Trusted Lists.

#### 6.2.1 Deliverable D1: Stable Draft for TB Review (SPR) – 30 March 2016
- **ETSI TS 119 124** [i.47] (CAdES):
  - Part 2: Test suites covering interoperability with simple PKIs, negative test cases, signature lifecycle (generation, augmentation, arbitration), interoperability with complex PKIs (uncomplete) and real PKIs based on EU Trusted Lists (uncomplete).
  - Part 3: Similar coverage for extended CAdES.
  - Part 4: Complete set of test assertions for conformance of baseline CAdES.
  - Part 5: Uncomplete set of test assertions for conformance of extended CAdES.
- **ETSI TS 119 164** [i.30] (ASiC):
  - Part 2: Updated test suites for interoperability of ASiC including long term attributes with simple PKIs.
  - Part 3: Test suites for interoperability of baseline ASiC containers covering four conformance levels.
  - Part 4: Complete set of test assertions for ASiC core specification.
  - Part 5: Complete set of test assertions for ASiC baseline profile (four conformance levels).
- **ETSI TS 119 614** [i.48] (Trusted Lists):
  - Part 2: Specifications for testing conformance of XML representation – test assertions covering EU Trusted Lists only (not non-EU).
- **ETSI TS 119 144** [i.29] (PAdES):
  - Part 2: Test suites for interoperability of baseline PAdES (similar coverage as CAdES).
  - Part 3: Test suites for interoperability of additional PAdES.
  - Part 4: Complete test assertions for baseline PAdES.
  - Part 5: Uncomplete test assertions for additional PAdES.
- **ETSI TS 119 134** [i.28] (XAdES):
  - Part 2: Test suites for interoperability of baseline XAdES.
  - Part 3: Test suites for interoperability of extended XAdES.
  - Part 4: Complete test assertions for baseline XAdES.
  - Part 5: Uncomplete test assertions for extended XAdES.

#### 6.2.2 Deliverables D2: Final Draft for Approval (FTB) – 30 April 2016
All TSs completed and amended according to comments received from ETSI ESI TB members, ready for final approval.

#### 6.2.3 Deliverables D3: Publication (PTS) – 30 June 2016
All TSs published two months after approval.

### 6.3 Production Plan for Conformity Testing Tools Development
Table 3 (summarized):
| Milestone | Type | Due Date | Format/Spec | Details |
|-----------|------|----------|-------------|---------|
| Xtool-M1 | Internal milestone | Beginning October 2015 | XAdES | XAdES Conformance Checker (XAdESCC): complete conformance checks for baseline and extended signatures (without distributed qualified properties). Ready for XAdES test event. |
| Xtool-M2 | Internal milestone | End March 2016 | XAdES | Complete XAdESCC: add conformance checks for extended signatures with distributed qualified properties. |
| Ctool-M1 | Internal milestone | Mid March 2016 | CAdES | CAdES Conformance Checker (CAdESCC): complete checks for baseline signatures and part of extended (no LTV attribute check). |
| Ctool-M2 | Internal milestone | Mid April 2016 | CAdES | Complete CAdESCC. |
| Ptool-M1 | Internal milestone | End March 2016 | PAdES | PAdES Conformance Checker (PAdESCC): complete checks for baseline signatures and part of additional profiles based on CAdES. |
| Ptool-M2 | Internal milestone | End April 2016 | PAdES | Complete PAdESCC. |
| Atool-M1 | Internal milestone | Mid May 2016 | ASiC | ASiC Conformance Checker (ASiCCC): complete checks for baseline containers with baseline signatures and part of additional containers. |
| Atool-M2 | Internal milestone | End May 2016 | ASiC | Complete ASiCCC. |
| Ttool-M1 | Internal milestone | End May 2016 | Trusted Lists | Consolidated but uncomplete version of Trusted Lists Conformance Checker (TLCC). |
| Ttool-M2 | Internal milestone | End June 2016 | Trusted Lists | Complete TLCC. |

## Requirements Summary (Key Planning Milestones)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | All TSs for testing conformance and interoperability will be published by 30 June 2016. | will (planning) | Clauses 6.2.1–6.2.3 |
| R2 | XAdES Conformance Checker (complete) will be ready by end March 2016. | will (planning) | Table 3, Xtool-M2 |
| R3 | CAdES Conformance Checker (complete) will be ready by mid April 2016. | will (planning) | Table 3, Ctool-M2 |
| R4 | PAdES Conformance Checker (complete) will be ready by end April 2016. | will (planning) | Table 3, Ptool-M2 |
| R5 | ASiC Conformance Checker (complete) will be ready by end May 2016. | will (planning) | Table 3, Atool-M2 |
| R6 | Trusted Lists Conformance Checker (complete) will be ready by end June 2016. | will (planning) | Table 3, Ttool-M2 |
| R7 | E-Signature Validation Plugtest will be held in March 2016. | will (planning) | Clause 6.1 |
| R8 | ASiC Plugtest will be held in June 2016. | will (planning) | Clause 6.1 |
| R9 | CAdES Plugtest will be held in November 2016. | will (planning) | Clause 6.1 |

## Informative Annexes (Condensed)

### Annex A: History of ETSI/ESI Plugtests
Summarizes 10 interoperability Plugtests events from 2003 to 2012: initial face-to-face events (XAdES 2003, joint PKI-XAdES 2004), then remote events (XAdES 2008, 2009, 2010, 2012; CAdES combined 2009, 2010; PAdES 2011; ASiC 2012; TSL 2009). Provides participation numbers and outcomes (specification updates). Also notes ETSI's continued work on TSL testing in cooperation with the European Commission.

### Annex B: ETSI/ESI Plugtests
Describes the remote plugtest portal architecture: public part (event info, registration) and private part (common area with conducting info, cryptographic material, online PKI services, attribute certificate issuance; signature-specific area with test case definition language, test cases pages, individual verification reports, upload/download pages, test data directory). Details the four types of interoperability tests: (1) Generation and Cross-verification (positive), (2) Only Verification (negative), (3) Upgrade and Arbitration, (4) Signature Conformance Checking tools. Includes step-by-step procedures for each test type.

### Annex C: Bibliography
Lists additional references not cited in the main text: ETSI TS 103 173 (CAdES Baseline Profile), ISO 32000-1, ETSI TS 103 172 (PAdES Baseline Profile), ETSI TS 103 174 (ASiC Baseline Profile), ETSI TR 102 038 (XML format for signature policies), ETSI TR 102 272 (ASN.1 format for signature policies).