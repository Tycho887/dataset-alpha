# ETSI TR 119 460: Survey of technologies and regulatory requirements for identity proofing for trust service subjects
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2021-02 | **Type**: Informative Technical Report
**Original**: https://www.etsi.org/standards-search

## Scope (Summary)
This Technical Report presents the results of a survey on technologies, legislations, specifications, guidelines and standards related to identity proofing. It collects and analyses information to identify trends and select relevant elements for the future normative specification ETSI DTS/ESI-0019461 on policy and security requirements for trust service components providing identity proofing.

## Normative References
- None (normative references are not applicable in this TR).

## Informative References (Key)
- [i.1] Regulation (EU) 910/2014 (eIDAS)
- [i.3] Commission Implementing Regulation (EU) 2015/1502 (assurance levels for eID means)
- [i.10] ETSI EN 319 411-1 (certificate issuance)
- [i.16] ISO/IEC 29003 (identity proofing)
- [i.30] ISO/IEC 29115 (entity authentication assurance framework)
- [i.36] NIST SP 800-63-3 (Digital Identity Guidelines)
- [i.43] NIST SP 800-63A (Enrollment and Identity Proofing)
- [i.64] BSI TR-03147 (Assurance Level Assessment for Identity Verification)
- [i.74] FATF Digital Identity Guidance (March 2020)
- [i.82] NISTIR 8202 (Blockchain Technology Overview)
- [i.84] Decentralized Identifiers (DIDs) v1.0 (W3C)
- [i.85] OpenID Connect for Identity Assurance (eKYC Project)
- Full list of 141 references in original document.

## Definitions and Abbreviations
- **identity proofing**: process by which a (trust) service provider collects and validates information about an applicant and verifies that so collected and validated information actually belongs to the applicant.
- **identity evidence**: information or documentation provided by the applicant to support the claimed identity.
- **Identity Assurance Level (IAL)**: degree of confidence that the applicant's claimed identity is their real identity.
- **attribute validation**: part of identity proofing process that involves determining that an evidence is genuine and the information it contains is accurate.
- **binding**: step of identity proofing process that involves confirming that the validated identity relates to the applicant being identity-proofed.
- **authoritative source**: any source that can be relied upon to provide accurate data, evidence to prove identity.
- Full list of terms and abbreviations in original document (clause 3).

## 4 Study Methodology
### 4.1 Introduction
ID-proofing is defined as a three-step process following FATF and NIST guidance: (1) attribute and evidence collection, (2) attribute and evidence validation, (3) binding ID attributes with applicant. Factors include purpose, technical/procedural criteria, and legal context.

### 4.2 Method for Analysing Received Info
Analysis stages: (a) reading sheets using the methodology per source, (b) cross-source analysis for trends/gaps, (c) conclusions for future developments. Information collected from national agencies, vendors, TSPs, research, existing specifications, and eIDAS revision consultation. Stakeholders contacted via email; vendors and TSPs received questionnaires (Annexes B, C).

### 4.2.3 General Methodology
Step 1: Attribute and evidence collection – identity attributes, type of evidence, type of presentation (digital representation, extracted from eID document, transmitted as eID), communication channels.
Step 2: Attribute and evidence validation – genuineness and validity checks, security features, external source queries, technical standards.
Step 3: Binding – technologies for binding protocol, remote liveliness detection, biometric factors, applicable regulatory constraints, anti-fraud processes.
Additionally, process requirements analysed: what needs to be done, how, security levels, compliance measures, auditing.

## 5 Information Collected on Existing ID-Proofing Processes and Models
### 5.1 Introduction
47 documents analysed through reading sheets, classified by origin. Feedback from stakeholders and information on eIDAS revision also included.
A basic principle: States are competent authorities for identity matters; international and EU regulations leave room for variations.

### 5.2 International and National Legal Frameworks, Standards and Good Practices
#### 5.2.0 General
States have vested interest in identity; eIDAS regulation leaves significant room for variations in implementation, especially for identity proofing.

#### 5.2.1 EU
##### 5.2.1.1 ETSI EN 319 411 (Certificate issuance)
- **Attribute collection**: For natural persons: full name, date and place of birth. For legal persons: full name, legal status, registration info.
- **Type of evidence**: direct evidence or attestation from an appropriate and authorized source.
- **Attribute validation**: left to the RA; documentation must come from an appropriate and authorized source.
- **Binding**: LCP – no specific requirement; NCP – physical presence or means providing equivalent assurance; QCP – equivalent assurance must be proven.
- **Process**: TSP must verify identity and accuracy of certificate request. Independence requirement: subscriber and TSP must be separate entities.
- **Security levels**: LCP, NCP, QCP (with CA/B forum PTC adding details).
- **Conclusion**: Well specifies what to validate but not how beyond physical presence or equivalent.

##### 5.2.1.2 ETSI EN 319 521 (Registered delivery)
- **Attribute collection**: left to ERDSP.
- **Validation and binding**: physical presence or remote using eID means with substantial/high assurance, or by NCP certificate, or other nationally recognized methods with equivalent assurance.
- **Security**: references ETSI EN 319 401.

##### 5.2.1.3 EN 419 241-1 / ETSI TS 119 431-1 (Remote QSCD)
- **Purpose**: user enrolment for remote signing – identity proofing crucial for sole control of signing key.
- **Attribute collection**: not specified; references ETSI EN 319 411-1 for guidance.
- **Binding**: mapping between applicant and certificate required.
- **Process**: references CIR 1502 for identification.
- **Conclusion**: identity proofing not central but crucial; references to other standards insufficiently detailed.

##### 5.2.1.4 Regulation 2019/1157 (Security of identity cards)
- **Attributes**: per ICAO 9303: full name, sex, nationality, date of birth, document number, expiry date, signature, portrait, plus fingerprints in secure storage medium.
- **Binding**: applicant must appear in person at least once.
- **Process**: security features; biometric data stored securely and only until issuance (max 90 days).
- **Conclusion**: defines attributes, responsibility of issuing states; identity proofing can use these attributes.

##### 5.2.1.5 CIR EU 2015/1501 (Interoperability framework)
- **Minimum data set for natural persons**: current family name(s), first name(s), date of birth, unique identifier.
- **Additional**: names at birth, place of birth, current address, gender.
- **For legal persons**: current legal name, unique identifier; additional: address, VAT, tax reference, etc.
- **Process**: secure network for exchange, data privacy, integrity, authenticity; references ISO/IEC 27001.

##### 5.2.1.6 CIR (EU) 2015/1502 (Assurance levels for eID means)
- **Attribute evidence**: from authoritative sources; no specific attributes listed (see CIR 1501).
- **Validation** (Natural persons):
  - Low: evidence assumed genuine or exists per authoritative source.
  - Substantial: evidence checked to be genuine; steps to minimize risk.
  - High: evidence checked to be valid per authoritative source; photo/biometric evidence recognized by Member State.
- **Binding** (Natural persons):
  - Low: may be assumed same.
  - Substantial: person verified to be in possession of evidence.
  - High: applicant identified through comparison of physical characteristic with authoritative source.
- **Process**: also covers issuance, delivery, activation, authentication requirements.
- **Conclusion**: extremely relevant – provides significantly more detail than currently exists for trust services.

##### 5.2.1.7 Guidance for application of LoA supporting eIDAS
- **Purpose**: line-by-line commentary of CIR 1502; non-binding but part of eIDAS environment.
- **Validation**: detailed LoA-tiered checks for physical and electronic evidence; suggests automatic checks via digital signatures or online verification.
- **Binding**: outcome-based test: false-match/false positive rate; for remote high LoA, resistance against high attack potential required.
- **Process**: references ISO standards; does not prescribe compliance measures.
- **Conclusion**: highly relevant but currently under review.

##### 5.2.1.8 ENISA Report: eIDAS COMPLIANT eID SOLUTIONS
- **Trends**: more mobile eID means, increasing biometric use; need for standards for remote identification processes.
- **Recommendations**: use international databases (PRADO, SIS, Interpol) for document validation; professionally trained agent for physical or picture-based verification.
- **Security considerations**: single biometric modality weaknesses; behavioural biometrics not yet permitted for eID authentication factors per CIR 1502.

#### 5.2.2 International
##### 5.2.2.1 UNCITRAL Draft Provisions on identity management and trust services
- **Purpose**: facilitate international recognition of digital ID and trust services; replicates eIDAS structure.
- **Conclusion**: limited use for this study; indication of possible international law development.

##### 5.2.2.2 ISO/IEC 29115 (Entity authentication assurance framework)
- **Levels**: four LoA; LoA4 requires local processing (personal appearance).
- **Enrolment phase**: application, identity proofing, verification, record-keeping.
- **Conclusion**: outdated for LoA4; consider 3-level approach as in ISO/IEC 29003.

##### 5.2.2.3 ISO/IEC 29003 (Identity proofing)
- **Levels**: LoIP 1 (low), 2 (moderate), 3 (high).
- **Process**: collect proofing information, determine veracity, bind subject to claimed attributes.
- **Conclusion**: good source for definitions, concepts, policy requirements.

##### 5.2.2.4 ISO/IEC 30107 (Biometric presentation attack detection)
- **Framework**: part 1 – framework; part 2 – data formats; part 3 – testing and reporting; part 4 – mobile profile.
- **Relevance**: important when biometric mechanisms used in identity proofing.

##### 5.2.2.5 CA/Browser Forum requirements
- **Types**: Baseline Requirements (BR), Extended Validation (EV), Code Signing.
- **Attribute collection**: for individuals: government-issued photo ID; for organizations: documentation from government agency, reliable data source, site visit, or attestation letter.
- **Validation**: inspect documents for alteration; evaluate reliability of data sources.
- **Binding**: for EV, face-to-face with notary/lawyer/accountant; for Code Signing, photo of applicant holding ID or webcam verification.
- **Conclusion**: very detailed, especially for legal persons; source of inspiration but may be too complex.

#### 5.2.3 National
##### 5.2.3.1 UK Guidance on Identity Proofing and Authentication (Good Practice Guides 43-46, 53)
- **Scoring system**: evidence scored 1-5 based on uniqueness, security features, issuance process.
- **Process**: five parts: evidence of claimed identity, check genuineness/validity, check existence over time, check fraud risk, check identity belongs to applicant.
- **Confidence levels**: low, medium, high, very high.
- **Binding**: includes suggestions for biometric matching, use of authoritative sources.
- **Conclusion**: modular approach, reusable across organizations.

##### 5.2.3.2 Draft BSI 8626 (Online user identification systems)
- **Process**: holistic approach covering functional, organizational, technical aspects.
- **Attribute collection**: sufficient to uniquely identify applicant; given/family names and DOB appear required.
- **Validation**: determine evidence likely genuine/valid; mitigate risks from fabricated, duplicated, or altered evidence.
- **Binding**: knowledge-based or physical/biometric verification; detailed guidance for biometric verification.
- **Conclusion**: useful, but currently a proposal under review; lacks specific thresholds for assurance levels.

##### 5.2.3.3 NIST SP 800-63 Series (Digital Identity)
- **Components**: IAL (identity proofing), AAL (authentication), FAL (federation).
- **IAL levels**:
  - IAL1: self-assertion.
  - IAL2: real-world existence verified.
  - IAL3: physical presence (or supervised remote).
- **Evidence strength**: 5 levels (unacceptable, weak, fair, strong, superior).
- **Process**: CSP must collect biometric sample at proofing; detailed requirements for remote in-person proofing.
- **Conclusion**: almost a full specification for identity proofing services; includes risk management, privacy, and log/tracing requirements.

##### 5.2.3.4 BSI TR-03147 (Germany – Identity Verification Assessment)
- **Levels**: Normal, Substantial, High (mapped to eIDAS LoA).
- **Validation**: check authenticity, validity, lost/stolen, security features.
- **Binding**: comparison of person with ID document; requires multifactor authentication from two categories.
- **Process**: ISMS per ISO/IEC 27001 required; FAR predefined (0.1% for biometric threshold).
- **Conclusion**: threat/risk-based approach; detailed specifications.

##### 5.2.3.5 Romania – Communication for QWTSP
- **Remote video identification**: must be certified by accredited EU auditor; responsibility rests with QTSP and auditor.
- **Binding**: options per eIDAS Article 24: physical presence, remote using eID means (physical presence previously ensured), by qualified certificate, or other nationally recognized methods with equivalent assurance.
- **Conclusion**: limited detail; indicates national practice.

##### 5.2.3.6 France – ANSSI Référentiel d'exigences de sécurité
- **LoA Substantial**: remote verification of identity document acceptable if technical/organizational measures reduce risk to at least equal physical presentation.
- **Acceptable remote methods**: 1) visual inspection with high-quality image (400 DPI), 2) chip reading with cryptographic verification, 3) machine-readable data with cryptographic verification.
- **LoA High**: only methods 2 and 3.
- **Binding**: false positive rate and resistance to attacks as outcome-based criteria.
- **Conclusion**: relevant, but unpublished and subject to changes.

##### 5.2.3.7 Germany – BNetzA 126/2017 (Video identification for telecommunications)
- **Process**: real-time end-to-end encrypted video chat; explicit consent recorded.
- **Validation**: check document security features (holograms, microprinting, etc.); at least three features from different categories must match.
- **Binding**: random movements, psychological questions, TAN verification.
- **Record retention**: 5 years.
- **Conclusion**: detailed requirements for remote video identification in telecom sector.

##### 5.2.3.8 Germany – BNtAg 208/1018 (eIDAS video identification for trust services)
- **Endorsement**: video identification usable for qualified certificates until 12/2021; must detect manipulation of video image, document, or person.
- **Conclusion**: high-level endorsement; not comprehensive.

### 5.3 Banking and Financial Services
#### 5.3.1 G20 Digital Identity Onboarding
- **Process**: registration, validation, verification, vetting/risk assessment, issuance, authentication.
- **Conclusion**: case study for developing countries; technology neutral.

#### 5.3.2 BITS Norway – Requirements for secure digital verification of identity
- **Process**: client-side app (mobile, kiosk) reads document (NFC or optical); server-side application analyses document genuineness.
- **Binding**: facial biometrics compare selfie with document photo.
- **Profiles**: different strength levels for financial, public, private sectors.
- **Conclusion**: very relevant – specifies remote verification sufficient for eIDAS substantial (optical) or high (NFC).

### 5.4 Services Subject to AML Rules
#### 5.4.1 AMLD5
- **Attribute collection and validation**: not specified; defines obligations but leaves discretion to Member States.
- **Acceptance of eID**: reference to eIDAS and nationally regulated remote processes.
- **Conclusion**: limited guidance on identity proofing; fragmentation across EU.

#### 5.4.2 EC Report on Existing Remote On-Boarding Solutions in the Banking Sector
- **Attribute collection**: includes consideration of documents with high security features or biometric data.
- **Validation**: against authoritative sources like PRADO; checks for forgery, validity, check-digits.
- **Binding**: live chat, biometric facial recognition, built-in tamper detection.
- **Process**: 8 typical customer journeys; each assessed for authenticity, validity, identity checks.
- **Conclusion**: useful listing of methods and risk assessments; not binding.

#### 5.4.3 EC Report on Portable KYC/CDD Solutions
- **Attribute-based LoA-rated framework**: core attributes (date of birth, given/family name, nationality, etc.); additional KYC attributes.
- **Validation**: basic checks for all LoAs; advanced checks (including security element validation) for substantial/high.
- **Conclusion**: proposal only; no regulatory impact.

#### 5.4.4 FATF Digital Identity Guidance
- **Principle-based**: risk-based approach; absence of face-to-face no longer automatically higher risk.
- **Binding**: liveness detection, photo comparison, enrolment code sent to verified phone.
- **Conclusion**: recognizes identity proofing by single or multiple IDSPs; focuses on financial inclusion.

#### 5.4.5 National Bank of Belgium – Comments and Recommendations
- **Attribute collection**: for natural persons: last name, first name, date/place of birth, address; for legal persons: corporate name, registered office, directors.
- **Evidence**: identity card, passport, eIDAS eID means; innovative solutions allowed after documented risk analysis.
- **Validation**: check against reliable independent sources; electronic verification with chip signature verification recommended.
- **Binding**: visual check for face-to-face; additional measures for remote.
- **Conclusion**: well-structured policy for financial institutions; relevant for documentation and authoritative source selection.

#### 5.4.6 Spain – SEPBLAC Video Identification Procedures
- **Assisted process**: trained verifier guides client; request consent, capture photo of document and face, random gestures for liveness.
- **Unassisted process**: automated steps; recording reviewed a posteriori.
- **Requirements**: technical controls for authenticity, validity, integrity; measures against fake documents; real-time streaming; device verification.
- **Conclusion**: both assisted and unassisted procedures approved.

#### 5.4.7 Italy – Bank of Italy Provision on AML Customer Due Diligence
- **Attribute collection**: identity document, registration data for legal persons.
- **Validation**: verify authenticity and validity; in case of doubt consult prevention system.
- **Binding**: for remote, additional checks like welcome call, bank transfer confirmation.
- **Conclusion**: includes both assisted and non-assisted video ID procedures.

#### 5.4.8 Italy – IVASS Act 44/2019 (Insurance sector AML)
- **Attribute collection**: name, surname, place/date of birth; legal entity details.
- **Validation**: similar to Bank of Italy.
- **Binding**: audio/video encryption; color video, clear audio; personnel must have defined procedure.
- **Conclusion**: specific to insurance sector.

#### 5.4.9 Germany – BaFin Circular 03/2017 on Video Identification
- **Document requirements**: machine-readable zone, sufficient optical security features (at least three from different categories).
- **Validity check**: date of issue and expiry, plausibility.
- **Binding**: real-time video with random gestures; TAN verification.
- **Conclusion**: detailed for AML compliance; similar to BNetzA.

### 5.5 SSI and Blockchain
#### 5.5.1 SSI eIDAS Legal Report
- **Scenarios**: use of eIDAS eID/qualified certs to issue verifiable credentials; eIDAS bridge; verifiable IDs as eIDAS means; qualified certificates as DID+VC; extend eIDAS notification to verifiable attestations.
- **Conclusion**: provides bridges between SSI and eIDAS; not focused on identity proofing process itself.

#### 5.5.2 NISTIR 8202 – Blockchain Technology Overview
- **Identity management**: blockchain not designed as standalone identity management; links between real identities and private keys made outside blockchain.
- **Conclusion**: useful to understand technology; not directly relevant for identity proofing.

#### 5.5.3 ILNAS White Paper on Blockchain and DLT
- **Use case**: identity attestations stored on ledger; user shares with service providers.
- **Process**: initial registration, consent, login, attribute sharing, contract signing.
- **Conclusion**: interesting but not detailed on identity proofing.

#### 5.5.4 Decentralized Identifiers (DIDs) v1.0
- **Architecture**: DIDs, DID documents, DID methods, verifiable data registries.
- **Design goals**: decentralization, control, privacy, security, proof-based, discoverability, interoperability, portability, simplicity, extensibility.
- **Binding**: verification of control via cryptographic keys.
- **Conclusion**: technical specification for identifiers; identity proofing external to DID system.

### 5.6 Tools and Technical Requirements
#### 5.6.1 Face Recognition – NIST FRVT
- **Performance tests**: 127 algorithms from 45 vendors; large accuracy gains since 2013 due to neural networks.
- **Key metrics**: false acceptance, false rejection rates.
- **Conclusion**: relevant for biometric binding, but no process requirements.

#### 5.6.2 OpenID Connect – eKYC Project (Identity Assurance)
- **Specifications**: transfer of ID attributes and metadata (trust framework, issuance/expiry date, source, verification method).
- **Attribute collection**: initial set (name, given name, birthday, place of birth, address).
- **Evidence types**: id_document, utility_bill, eIDAS eID, qualified electronic signature.
- **Conclusion**: critical for attribute propagation; focuses on trust framework assertion, not full identity proofing.

#### 5.6.3 Document Validation Tools
##### 5.6.3.1 PRADO
- **Public database**: authentic travel and identity documents from EU Member States, Iceland, Norway, Switzerland.
- **Use**: check security features, promote common terminology.
- **Conclusion**: useful for document genuineness check.

##### 5.6.3.2 Machine Readable Documents – ICAO 9303
- **Specifications**: machine-readable travel documents; defines data elements, security features.
- **Binding**: electronic chip with biometrics (facial image, fingerprints).
- **Conclusion**: foundation for identity document verification.

#### 5.6.4 FIDO Alliance White Paper: Using FIDO with eIDAS Services
- **Purpose**: use FIDO2 for authentication in eIDAS QTSPs and eID schemes.
- **Attribute collection**: not directly addressed.
- **Validation**: FIDO authenticators can provide strong authentication.
- **Conclusion**: relevant for binding and authentication after identity proofing.

### 5.7 Main Feedback from Vendors and TSP
- **TSP**: practical concerns about remote identity proofing; need for harmonised requirements.
- **Vendors**: provided technical solutions; diversity in approaches.

### 5.8 On-Going Initiatives: Current Trends in EU Regulatory Requirements
- **Know Your Customer (KYC)**: ongoing evolution towards digital onboarding.
- **eIDAS Regulation revision**: consultation underway; likely to include more detailed identity proofing requirements.

## 6 Analysis
### 6.1 Introduction
Analysis based on the three-step methodology.

### 6.2 ID Proofing Process
#### 6.2.1 Introduction
Process defined as collection, validation, binding.

#### 6.2.2 Findings
- Most documents follow similar structure.
- Levels of assurance are common (low, substantial, high) but with different names.
- Remote identity proofing increasingly accepted.

### 6.3 Findings Applicable to Each Step of ID Proofing Process
#### 6.3.1 Attribute and Evidence Collection
##### 6.3.2.1 Customary ID Attributes Collected
- **Natural person**: full name, date of birth, place of birth, nationality, address (often mandatory).
- **Legal person**: legal name, legal form, registration number, address, unique identifier.
- **Individuals acting on behalf of legal entities**: as natural person plus proof of authority.

##### 6.3.2.2 Type of Evidence
- Trusted/authoritative sources: government registries, official databases (e.g., PRADO), notified eID schemes.
- Document types: passport, national ID card, driving licence, residence permit, birth certificate.
- Requirement: photo and/or biometrics for higher assurance.

##### 6.3.2.3 Type of Presentation
- Digital representation (scan/photo/video) – captured remotely or on-premises.
- Digitally extracted from electronic ID document (NFC chip).
- Transmitted in purely digital form (eID, SSI).
- Communication channels: secure (TLS, encryption), real-time for video.

#### 6.3.3 Attribute Validation
##### 6.3.3.2 Findings
- Security features: holograms, UV/IR features, microprinting, machine-readable zone (MRZ).
- For electronic documents: cryptographic verification of signatures on chip.
- Validity checks: expiry date, lost/stolen status via authoritative sources.
- For high LoA: multiple checks, biometric comparison with authoritative source.

#### 6.4 Attribute Binding
- Technologies: facial recognition, liveness detection, knowledge-based questions, TAN, biometric matching.
- Remote liveness detection increasingly required.
- Use of biometrics and presentation attack detection (ISO/IEC 30107) recommended.
- Privacy considerations (GDPR).

#### 6.5 Security Requirements
##### 6.5.2.1 Security of Identity Proofing Service
- Relationship to trust services: identity proofing may be subcontracted.
- Requirements from ETSI standards (EN 319 401): ISMS, organizational, HR, network security.
- Other documents: ISO/IEC 27001, NIST SP 800-63.

##### 6.5.2.2 Security of Identity Proofing Means
- Use of identity documents: must have robust security features.
- Provision of photo by applicant: ensure not tampered.
- Biometrics: liveness detection, presentation attack detection.
- Remote video interview: real-time, encrypted, with agent control.
- Remote reading of chip: cryptographic verification.
- Remote optical reading: high-resolution, security feature check.

## 7 Conclusions
- The survey shows a wide diversity of identity proofing practices.
- Common elements: three-step process, level of assurance concept, acceptance of remote methods.
- Gaps: lack of specific standards for trust service identity proofing; reliance on "equivalent to physical presence" without clear metrics.
- The future ETSI DTS/ESI-0019461 should define policy and security requirements addressing these gaps, harmonising with eIDAS and international frameworks.

## Requirements Summary
| ID | Requirement (Summary) | Type | Reference |
|---|---|---|---|
| R1 | Identity proofing process shall consist of attribute collection, attribute validation, and binding. | shall | Clause 4.2.3 |
| R2 | For natural persons, at minimum full name, date of birth, and place of birth shall be collected. | shall | Clause 6.3.2.1.1 |
| R3 | For legal persons, legal name, legal form, and registration number shall be collected. | shall | Clause 6.3.2.1.2 |
| R4 | Evidence shall be from an authoritative source. | shall | Clause 5.2.1.1 |
| R5 | For high LoA, biometric comparison with an authoritative source is required. | shall | Clause 5.2.1.6 |
| R6 | Remote identity proofing must include liveness detection and presentation attack detection. | shall | Clause 6.4 |
| R7 | Records of identity proofing shall be retained and protected. | shall | Clause 5.4.5.5 |

## Informative Annexes (Condensed)
- **Annex A (CEN and ISO standards)**: Lists relevant standards from SC17 (cards), SC27 (security), SC37 (biometrics), and CEN/TC224 (personal identification). Provides a comprehensive reference for standardization work.
- **Annex B (Vendors Questionnaire)**: Contains the questionnaire sent to vendors; includes questions on attribute collection, validation methods, biometrics, and technical solutions. Responses summarized in clause 5.7.
- **Annex C (TSP Questionnaire)**: Similar questionnaire for trust service providers, focusing on operational aspects and compliance.

**History**: Document produced by ETSI TC ESI; approved in 2021.