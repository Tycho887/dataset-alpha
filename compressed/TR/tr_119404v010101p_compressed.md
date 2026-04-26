# ETSI TR 119 404: Electronic Signatures and Infrastructures (ESI); NIS2 and its impact on eIDAS standards
**Source**: ETSI Technical Committee Electronic Signatures and Infrastructures (ESI) | **Version**: V1.1.1 | **Date**: 2023-02 | **Type**: Informative  
**Original**: [URL: https://www.etsi.org/deliver/etsi_tr/119400_119499/119404/01.01.01_60/tr_119404v010101p.pdf](https://www.etsi.org/deliver/etsi_tr/119400_119499/119404/01.01.01_60/tr_119404v010101p.pdf)

## Scope (Summary)
This document outlines the main requirements of the NIS2 Directive (EU 2022/2555), analyses them against existing cybersecurity provisions in ETSI EN 319 401 (General Policy Requirements for Trust Service Providers), considers the use of ISO 27002 (2013 and 2022 editions), and establishes a methodology for aligning other ETSI standards with NIS2.

## Normative References
Not applicable (the present document contains no normative references).

## Informative References
- [i.1] Directive (EU) 2016/1148 (NIS1)
- [i.2] Directive (EU) 2022/2555 (NIS2)
- [i.3] Regulation (EU) No 910/2014 (eIDAS1)
- [i.4] Proposal for a Regulation amending Regulation (EU) No 910/2014 (eIDAS2)
- [i.5] ISO 27002:2013
- [i.6] ISO 27002:2022
- [i.7] ETSI EN 319 401
- [i.8] ISO/IEC 27005
- [i.9] ISO/IEC 27000

## Definitions and Abbreviations
### Terms
- **cybersecurity**: activities necessary to protect network and information systems, the users of such systems, and other persons affected by cyber threats
- **cyber threat**: potential circumstance, event or action that could damage, disrupt or otherwise adversely impact network and information systems, the users of such systems and other persons
- **impact**: harm that may be suffered when a threat compromises an information asset
- **incident**: any event compromising the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, network and information systems
- **incident handling**: any actions and procedures aiming to prevent, detect, analyse, and contain or to respond to and recover from an incident
- **large-scale cybersecurity incident**: incident whose disruption exceeds a Member State's capacity to respond to it or with a significant impact on at least two Member States
- **near miss**: event that could have compromised the availability, authenticity, integrity or confidentiality of stored, transmitted or processed data or of the services offered by, or accessible via, network and information systems, but was successfully prevented from transpiring or did not materialise
- **qualified trust service provider**: trust service provider who provides one or more qualified trust services and is granted the qualified status by the supervisory body (as defined in eIDAS2 [i.4])
- **risk**: potential for loss or disruption caused by an incident and is to be expressed as a combination of the magnitude of such loss or disruption and the likelihood of occurrence of that incident
- **risk analysis**: process of estimating the likelihood that an event will create an impact and includes as necessary components, the foreseeability of a threat, the expected effectiveness of Safeguards, and an evaluated result
- **risk assessment**: comprehensive project that evaluates the potential for harm to occur within a scope of information assets, controls, and threats
- **risk management**: process for analysing, mitigating, overseeing, and reducing risk
- **security of network and information systems**: ability of network and information systems to resist, at a given level of confidence, any event that may compromise the availability, authenticity, integrity or confidentiality of stored or transmitted or processed data or of the services offered by, or accessible via, those network and information systems
- **significant cyber threat**: cyber threat which, based on its technical characteristics, can be assumed to have the potential to severely impact the network and information systems of an entity or its users by causing considerable material or non-material losses
- **trust service**: an electronic service normally provided for remuneration which consists of issuing, validating, creating, preserving, managing, or attesting (as defined in eIDAS2 [i.4])
- **trust service provider**: natural or a legal person who provides one or more trust services either as a qualified or as a non-qualified trust service provider (as defined in eIDAS2 [i.4])
- **vulnerability**: weakness, susceptibility or flaw of ICT products or ICT services that can be exploited by a cyber threat

### Abbreviations
- **eIDAS1**: Regulation (EU) No 910/2014 [i.3]
- **eIDAS2**: Proposal for a Regulation [i.4]
- **NIS1**: Directive (EU) 2016/1148 [i.1]
- **NIS2**: Directive (EU) 2022/2555 [i.2]
- **QTSP**: Qualified Trust Service Provider
- **TSP**: Trust Service Provider

## 4 Overview
### 4.1 Introduction
NIS2 [i.2] includes TSPs within its scope and the eIDAS2 Regulation refers to NIS2 for security requirements. The division between eIDAS2 (directly applicable) and NIS2 (requiring national transposition) creates risks of fragmentation and potential duplicated supervision for QTSPs providing cross-border services. This document analyses IT and cybersecurity requirements for TSPs to propose harmonised solutions.

### 4.2 General obligations under the NIS2 Directive
TSPs are subject to the following general obligations:
- **Article 3(4)**: Provision of entity information (name, address, contact details, IP ranges, sector, list of Member States where services are provided) to competent authorities.
- **Cybersecurity risk management and critical supply chain** (Arts. 20–24)
- **European cybersecurity certification scheme** (Art. 24): Member States may require certified ICT products/services; Commission may adopt implementing acts.
- **Standardisation** (Art. 25): Member States encouraged to use European/international standards; ENISA to advise.
- **Reporting and information-sharing** (Arts. 2, 26, 27): Incidents with significant impact; voluntary sharing of threat information.
- **Supervisory and enforcement measures** (Arts. 32, 33)
- Additional obligations: National cybersecurity strategy (Art. 7), coordinated vulnerability disclosure (Art. 12), crisis management and CSIRT cooperation (Arts. 9–19).

## 5 Provisions related to eIDAS and Trust Service Providers: eIDAS2
### 5.1 Introduction
NIS2 applies to all TSPs regardless of size (Arts. 2.1, 2.2). QTSPs are considered essential entities (Art. 3.1.b, Annex I, 8. Digital infrastructure – Trust service providers); non-qualified TSPs are important entities. eIDAS2 sets out:
- **Articles 17 and 18**: Cooperation between eIDAS and NIS2 supervisory authorities.
- **Article 19a**: Non-qualified TSPs must comply with NIS2 Article 21, including risk management measures (registration, procedural checks, service management).
- **Amendment of Article 20**: QTSP audits must cover both eIDAS and NIS2 Article 21; failure may lead to withdrawal of qualified status.
- **Paragraph in Article 21**: eIDAS supervisory body shall request NIS2 competent authorities to supervise; outcome within two months; qualified status granted within three months after notification.

### 5.2 Risk of fragmentation of the internal market
Recitals 4 and 5 of NIS2 acknowledge divergences causing fragmentation. To avoid this, the Directive proposes:
- Implementing acts by the Commission; or
- Sector-specific Union legal acts considered equivalent.
For TSPs, Recital 84 notes a high degree of harmonisation should be facilitated by an implementing act.

### 5.3 Risk assessment and risk management
TSPs must take all appropriate and proportionate measures to manage risks to their services, including physical protection. Requirements for QTSPs under eIDAS Article 24 continue to apply.

### 5.4 Cybersecurity risk-management measures
#### 5.4.1 Risk mitigation and cybersecurity measures
Based on an all-hazards approach, NIS2 mandates measures to protect network/information systems and their physical environment (e.g., theft, fire, flood, power failures). Measures must address:
- Criticality of the entity
- Risks (including societal)
- Size of the entity
- Likelihood and severity of incidents
Security measures should align with ISO/IEC 27000 family standards. Recital 93 states NIS2 obligations are complementary to eIDAS requirements.

#### 5.4.2 Cyber hygiene policies, cybersecurity awareness, and innovative technology
NIS2 requires TSPs to establish cyber hygiene policies including zero-trust principles, software updates, device configuration, network segmentation, identity and access management, user awareness, and staff training (Art. 21.2.g). ENISA monitors national policies.

#### 5.4.3 Supply chain
NIS2 requires TSPs to assess and manage supply chain risks, including relationships with direct suppliers and service providers (recital 85). ETSI EN 319 401 [i.7] partially covers this but needs further development. Relevant references: ISO/IEC 27002:2022 [i.6] sections 5.19–5.22, MITRE, NSA, NIST.

### 5.5 Supervision
Recital 94 of NIS2 suggests that Member States assign the role of competent NIS2 authorities for TSPs to the eIDAS supervisory bodies to ensure continuity and leverage existing expertise. Close cooperation between supervisory authorities is expected.

## 6 TSPs' NIS2 Cybersecurity obligations
### 6.1 Analysis of NIS2 vs ETSI EN 319 401 controls
**Table 1** maps NIS2 requirements to existing ETSI EN 319 401 [i.7] clauses and indicates whether the requirement is fully, partially, or not met, and where further development is needed.

| Domain | Sub-domains | NIS2 Directive | ETSI EN 319 401 [i.7] | NIS2 Requirement met by ETSI EN 319 401 [i.7] |
|---|---|---|---|---|
| Risk analysis | | 21.2.a) risk analysis | 5 Risk Assessment | Partial (non-normative reference to ISO/IEC 27005) |
| Information system security policies | | 21.2.a) information system security policy | 6.3 Information security policy | Fully |
| ISMS policies and procedures | | 21.2.f) policies and procedures to assess effectiveness | Controls and policies in clause 7 | Need cross-links |
| Organization reliability | | | 7.1.1 | Additional to NIS2 |
| Segregation of duties | | | 7.1.2 | Additional to NIS2 |
| Human resources | General | 21.2.i) human resources security, access control, asset management | 7.2 Human resources | Fully |
| | Training and awareness | 21.2.g) basic cyber hygiene, training | REQ-7.2-02, etc. | Fully |
| Asset management | General | 21.2.e) security in acquisition, development, maintenance; vulnerability handling | 7.3.1 General | Fully |
| | Media handling | | 7.3.2 | Additional to NIS2 |
| | Vulnerability management | 21.2.e) vulnerability handling | Included but not specific topic | Need cross-links |
| Access control | | 21.2.i) …; 21.2.j) multi-factor authentication | 7.4 Access control | Need development |
| Cryptographic controls | | 21.2.g) policies on cryptography | 7.5 Cryptographic controls | Fully |
| Physical and environmental security | | Recital 93: physical protection | 7.6 | Included |
| Supply chain security | | 21.2.d) supply chain, including direct suppliers | REQ-6.3-05, etc. | Partially |
| Operation security | | | 7.7 | Additional to NIS2 |
| Network security | | 21.2.e) security in network acquisition | 7.8 Network security | Fully |
| Incident management | | 21.2.b) incident handling | 7.9 Incident management | Fully |
| | Reporting | NIS2 (CERT) and eIDAS | Included but not specific | Need cross-links |
| Collection of evidence | | | 7.10 | Additional to NIS2 |
| Business continuity management | | 21.2.c) business continuity | 7.11 Business continuity management | Fully |
| Compliance | | | 7.13 | Additional to NIS2 |

### 6.2 ETSI EN 319 401 and ISO/IEC 27002 control mapping
**Table 2** provides a mapping from ETSI EN 319 401 clauses to ISO/IEC 27002:2013 and 27002:2022 controls.

| ETSI EN 319 401 [i.7] reference | ISO/IEC 27002:2013 [i.5] | ISO/IEC 27002:2022 [i.6] |
|---|---|---|
| 5 Risk Assessment | | |
| 6.3 Information security policy | Clause 5.1.1 | 5.1 Policies for information security |
| 7.1.1 Organization reliability | 5.2 | 5.2 Information security roles and responsibilities |
| 7.1.2 Segregation of duties | 5.3 | 5.3 Segregation of duties |
| 7.2 Human resources | Clauses 6.1.1, 6.1.2, 7, 7.2.1, 7.2.3 | 5.4, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7 |
| REQ-7.2-02, etc. | 6.3 | 6.3 |
| 7.3.1 General requirements | Clauses 8, 8.1.1 | 5.9, 5.10, 5.11, 5.8, 8.26, 8.7, 8.8, 8.9, 8.15, 8.16, 8.17, 8.18, 8.19 |
| 7.3.2 Media handling | 8.3 | 7.10 |
| 7.4 Access control | 9 | 5.15, 5.16, 5.17, 5.18, 8.2, 8.3, 8.4, 8.5, 8.18 |
| 7.5 Cryptographic controls | 10 | 8.24 |
| 7.6 Physical and environmental security | 11, 11.1 | 7.1–7.9, 8.1 |
| (Supply chain – not in EN 319 401) | | 5.19, 5.20, 5.21, 5.22, 5.23 |
| 7.7 Operation security | 12, 14, 15 | 5.37, 8.6, 8.31, 8.32 |
| 7.8 Network security | | 8.20, 8.21, 8.22, 8.23 |
| 7.9 Incident management | 16 | 5.24, 5.25, 5.26, 5.27, 5.28, 6.8 |
| 7.10 Collection of evidence | | 5.28 |
| 7.11 Business continuity management | 17 | 8.13, 5.29, 5.30 |
| 7.13 Compliance | | 5.31, 5.32, 5.33, 5.34, 5.35 |

## 7 Methodology in Aligning ETSI Standards with NIS2
ETSI EN 319 401 [i.7] structure will be maintained as far as possible to minimise impact on other standards. A mapping table (similar to Table 1, likely placed in an annex) will map NIS2 requirements to ETSI EN 319 401 clauses. New requirements (e.g., supply chain) will be inserted into the existing clause structure. Existing trust service standards will not be changed unless absolutely necessary; additional requirements applicable under NIS2 will be clearly identified.

## Requirements Summary
None (this is a Technical Report with no normative requirements).

## Informative Annexes (Condensed)
No annexes are present in the provided text. The document includes only the main body and history.

---
**History**: V1.1.1 published February 2023.