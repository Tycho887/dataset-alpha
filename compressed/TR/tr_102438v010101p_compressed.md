# ETSI TR 102 438 V1.1.1: Electronic Signatures and Infrastructures (ESI); Application of Electronic Signature Standards in Europe
**Source**: ETSI TC ESI | **Version**: V1.1.1 | **Date**: March 2006 | **Type**: Technical Report (Informative)
**Original**: ETSI deliverable (http://www.etsi.org)

## Scope (Summary)
This Technical Report presents the results of STF 288 to harmonise the use of electronic signature standards across Europe. It monitors initiatives in e‑invoicing, e‑procurement, e‑authentication, e‑registered mail and smart card standards (CEN/TC 224), assessing applicability of existing ESI standards and recommending harmonisation. Where other bodies’ activities were already closed, reports are attached as annexes summarising their deliverables.

## Normative References
- [1] Directive 1999/93/EC (Electronic Signatures Directive)
- [2] Directive 2001/115/EC (VAT Invoicing)
- [3] ETSI TS 101 456: Policy requirements for CAs issuing qualified certificates
- [4] ETSI TS 102 042: Policy requirements for CAs issuing public key certificates
- [5] ETSI TS 101 862: Qualified certificate profile
- [6] ETSI TS 101 733: CMS Advanced Electronic Signatures (CAdES)
- [7] ETSI TS 101 903: XML Advanced Electronic Signatures (XAdES)
- [8] ETSI TS 102 280: X.509 V.3 Certificate Profile for Certificates Issued to Natural Persons
- [9] CWA 15264‑1: Architecture for a European interoperable eID system within a smart card infrastructure
- [10] CWA 15264‑2: Best Practice Manual for card scheme operators exploiting a multi‑application card scheme incorporating interoperable IAS services
- [11] CWA 15264‑3: User Requirements for a European interoperable eID system within a smart card infrastructure
- [12]‑[21] ISO/IEC 10536‑1/2/3, ISO/IEC 14443‑1/2/3/4, ISO/IEC 15693‑1/2/3 (contactless card standards)
- [22] Sixth VAT Directive 77/388/EEC
- [23] Commission Recommendation 1994/820/EC on EDI
- [24] Commission Decision of 14 July 2003 on recognised standards for electronic signature products
- [25] CWA 14890‑1: Application Interface for smart cards used as Secure Signature Creation Devices – Part 1: Basic requirements
- [26] CWA 14890‑2: Part 2: Additional Services
- [27] IETF RFC 3647: Certificate Policy and CPS Framework
- [28] CEN EN 1332‑4: Coding of user requirements for people with special needs
- [29] CWA 13987‑1: Smart Card Systems – Interoperable Citizen Services – Extended User Related Information
- [30]‑[33] CWA 14167‑1/2/3/4: Security Requirements for Trustworthy Systems Managing Certificates
- [34] CWA 14169: Secure Signature‑creation devices “EAL 4+”
- [35] CWA 14170: Security requirements for signature creation applications
- [36] CWA 14355: Guidelines for the implementation of Secure Signature‑Creation Devices
- [37]‑[38] CWA 14890‑1/2 (duplicate of [25]‑[26])
- [39] ISO/IEC 14443: Contactless proximity cards
- [40] ISO/IEC 15693: Contactless vicinity cards

## Definitions and Abbreviations
### Definitions (selected)
- **advanced electronic signature**: as per Directive 1999/93/EC – uniquely linked, capable of identifying, created under sole control, linked to data so any change detectable.
- **certificate**: public key plus info rendered unforgeable by CA’s private key (X.509).
- **certification authority**: authority trusted to create and assign certificates; a CSP.
- **certificate policy**: named set of rules indicating applicability of certificate (X.509).
- **certification practice statement**: practices of CA in issuing certificates (RFC 3647).
- **Certification‑Service‑Provider (CSP)**: entity who issues certificates or provides other electronic signature services.
- **EDI**: transfer of commercial information using agreed formats (94/820/EC).
- **Electronic Invoice**: invoices sent by electronic means.
- **electronic signature**: data in electronic form attached/logically associated serving as authentication method (Directive 1999/93/EC).
- **Porvoo Group**: international network promoting transnational interoperable electronic identity based on PKI and eID cards.
- **qualified certificate**: certificate meeting Annex I requirements and provided by CSP fulfilling Annex II (Directive 1999/93/EC).
- **Qualified Certificate Policy (QCP)**: certificate policy incorporating Annex I and II requirements.
- **qualified electronic signature**: advanced electronic signature based on qualified certificate and created by SSCD (Art. 5.1).
- **secure‑signature‑creation device (SSCD)**: device meeting Annex III requirements.
- **signature‑creation data**: unique data (e.g., private key) used by signatory to create electronic signature.
- **UN/CEFACT**: UN body for trade facilitation and electronic business.

### Abbreviations
- AdES – Advanced Electronic Signature; ASP – Application Service Provider; CA – Certification Authority; CAdES – CMS Advanced Electronic Signatures; CEN – Comité Européen de Normalisation; CPS – Certification Practice Statement; CRL – Certificate Revocation List; DCSSI – Direction Centrale de la Sécurité des Systèmes d’Information; EbXML – Electronic business using eXtensible Markup Language; EDIFACT – Electronic Data Interchange For Administration, Commerce and Transport; EESSI – European Electronic Signature Standardisation Initiative; ERP – Enterprise Resource Planning; ESI – Electronic Signatures and Infrastructures; HSM – Hardware Security Module; IAS – Identity, Authentication, Electronic Signature; OASIS – Organization for the Advancement of Structured Information Standards; OCSP – On‑line Certificate Status Protocol; PKI – Public Key Infrastructure; QCP – Qualified Certificate Policy; PP – Protection Profile; SCA – Signature Creation Application; SSCD – Secure Signature Creation Device; VAN – Value Added Network; XAdES – XML Advanced Electronic Signatures.

## 4 Monitored Bodies and Workshops
List of bodies and their deliverables:
1. e‑Invoicing (clause 5): CEN/ISSS e‑Invoicing Focus Group and CEN/ISSS Workshop on eInvoicing.
2. e‑Procurement (clause 6): CEN/ISSS Workshop on eProcurement (CWA 15236).
3. e‑Registered mail (clause 7): UPU Electronic PostMark and Italian PEC.
4. e‑Authentication (clause 8): CEN/ISSS Workshop on e‑Authentication → CWA 15264 parts 1‑3 and strategic vision document.
5. CEN/TC 224 Machine Readable Cards (clause 9): transformation of nine CWAs into ENs (WG16 and WG17).

## 5 e‑Invoicing
### 5.1 CEN/ISSS e‑Invoicing Focus Group
- **Purpose**: EC requested CEN/ISSS overview on standardisation issues for electronic invoicing under Directive 2001/115/EC.
- **Final report** (end 2003): analyses standards relevant to e‑Invoicing and VAT. Summary in Annex A.
- **Key recommendation**: establish "Electronic Invoices Forum Europe" to link national fora.

### 5.2 CEN/ISSS Workshop on "Interoperability of Electronic Invoices in the European Union"
#### 5.2.1 Workshop purpose
- Mandate M339 from DG Enterprise to support implementation of Directive 2001/115/EC.
- **Objective**: Intra‑EU transmission, storage of electronic invoices; produce CWA by mid 2006.

#### 5.2.2 Workshop organisation
- Kick‑off 9 Feb 2005. Four subjects: EDI, Electronic signature, Storage, Modelling.
- **Tasks**:
  1. EDI and Business standards (update 1994/820/EC, core components, identifiers, code sets).
  2. Electronic Signature for eInvoices (companies signatures, multi‑tier communications, authentication).
  3. Overall work items (archiving guidelines, authorities, service providers).
  4. e‑Invoicing model.

#### 5.2.3 Applicability of existing ESI standards
- Formal liaison between ETSI TC ESI and CEN WS. ETSI representative in Task 2.1.
- TS 101 903 (XAdES) and TS 101 733 (CAdES) will be referenced in annex but **not recommended** due to perceived complexity by eInvoice community.

#### 5.2.4 Report on electronic signature related matters
##### 5.2.4.1 Introduction
- Directive 2001/115/EC allows advanced electronic signatures, EDI, or other electronic means for authenticity and integrity.
- **Storage**: invoices must be kept 4‑10 years depending on law.

##### 5.2.4.2 ETSI relevant CEN WS matters
- CWA will have parts on electronic signatures and storage.
- **Security measures**: simpler signature format allowed if storage organisation is reliable (inverse relationship). XAdES/CAdES referenced but not mandated.

##### 5.2.4.3 EDI vs. electronic signatures
- Different viewpoints. Proposed solution: electronic signature per se provides security; EDI requires agreements; usage of advanced electronic signatures can guarantee authenticity and integrity.

##### 5.2.4.4 eInvoices storage vs. electronic signatures
- If reliable storage organisation, no need for full ES‑A format; otherwise use ES‑A.

#### 5.2.5 Any recommendations
- Close attention to Task 2 (AdES and corporate signatures).
- Time‑Marking can replace Time‑Stamping if audit log is reference, but may be more costly.

## 6 e‑Procurement
### 6.1 Context
- CEN/ISSS Workshop on eProcurement launched Oct 2003, closed Feb 2005.
- **Output**: CWA 15236: "Analysis of standardization requirements and standardization gaps for eProcurement in Europe".

### 6.2 Outcome of the workshop
- CWA 15236 approved (95 pages).

### 6.3 Main content of CWA 15236
#### 6.3.1 The main phases of e‑Procurement
- e‑Tendering, e‑Ordering, e‑Despatching, e‑Invoicing.

#### 6.3.2 The relationship with the EESSI work
- **Non‑repudiation**: Addressed by Directive 1999/93/EC and TS 101 456. ESI standards are not the only way.
- **Authentication**: TS 102 042, eInvoicing Focus Group, eAuthentication WS.
- **Time stamping**: TS 102 023, needs review for eProcurement.
- **Role attributes**: TS 101 158, need further specification.
- **Signature policies**: Need for signature policies for contracting authorities.
- **XML signatures**: XAdES (TS 101 903) for XML signatures.

#### 6.3.3 The recommendations
- **Electronic signatures**: need harmonised evaluation criteria, TSL profile, CSP requirements, authentication, delegation/multiple signatures.
- **Signature policy**: Identify requirements for coordinated signature policy.

### 6.4 Opinion on the outcome of the workshop
- Security aspects not addressed per phase. Confidentiality in tendering is important. Role identification missing. **Multiple signatures on same document** still to be addressed.

## 7 e‑Registered mail
### 7.1 UPU EPM
#### 7.1.1 UPU Electronic PostMark Overview
- UPU EPM standard (s43) provides services for email preservation: verification, time‑stamping, logs, optional encryption.
- Supports non‑repudiation of origin, submission, delivery, receipt.
- Claims support for CMS and XMLDSig signatures, RFC 3161 time‑stamping, OCSP, ES‑C format (TS 101 733/903).
- Aligning with OASIS DSS.

#### 7.1.2 Recommendations
- EPM provides use case for electronic signature requirements.

### 7.2 Posta Elettronica Certificata – PEC in Italy
- **Purpose**: Provide e‑mail with same services as registered mail.
- **Basic functions**: sender authentication, virus checking, transport envelope with signed receipts, servers keep logs (30 months), daily timestamping.
- **Signatures**: Advanced signatures via HSM, basic AdES (security provided by organisational means).
- **Mandatory for Public Administrations from 16 May 2007**.
- No restrictions on evidence exhibition (subject to data protection).

## 8 e‑Authentication
### 8.1 Overview of the CEN WS activity and their technical approach
- CEN WS on e‑Authentication: kick‑off Apr 2003, finalized Feb 2005.
- **Deliverables**:
  1. "Towards an electronic ID for the European Citizen, a strategic vision"
  2. CWA 15264‑1: Architecture for interoperable eID system within smart card infrastructure
  3. CWA 15264‑2: Best Practice Manual for card scheme operators
  4. CWA 15264‑3: User Requirements for interoperable eID system
- **Key recommendations from strategic vision**:
  1. Smart card based eID as European infrastructure.
  2. Legal system for cross‑border acceptance.
  3. Encourage expert participation.
  4. European pilot project.
  5. European coordination on eID.
- **Comments**: Focus on eAuthentication, not QES; room to differentiate content commitment vs authentication signatures.

### 8.2 Applicability of existing ESI standards
- TS 101 862 and TS 102 280 referenced.
- **Unaccepted comments on keyUsage (nonRepudiation vs authentication) and SHA‑1 algorithm** (decision to comply with OSCIE Volume 4, Part 1).

### 8.3 Any recommendations
- No direct recommendations for closed WS.
- **Suggest ETSI ESI monitor other CEN Workshops**, particularly keyUsage, SHA‑1, signature format profiles, trust‑service provider identification.

## 9 CEN/TC 224 Machine Readable Cards
### 9.1 Context
- CEN transferred maintenance of nine CWAs related to electronic signatures to CEN/TC 224.
- **CWAs**: CWA 14167‑1/2/3/4, 14169, 14170, 14355, 14890‑1/2.

### 9.2 Outcome of TC 224 meeting in Munich (Apr 2005)
- Created WG16 (Application Interface for smart cards used as SSCD) and WG17 (Protection Profiles in context of electronic signatures).

### 9.3 TC 224 WG16
- **Objective**: Transform CWA 14890‑1/2 into EN 14890‑1/2.
- **Issues noted**:
  - Scope now includes authentication and confidentiality, not just SSCD.
  - Confusion between electronic signatures and digital signatures.
  - Distinction between trusted and untrusted environments unclear.
  - No separation between certificates for non‑repudiation and authentication.
  - **Different PINs required for non‑repudiation and authentication**.
  - Biometrics: secure messaging mandatory, but unclear if biometric alone can activate private key.
  - Key pair generation and certificate linkage unclear.
  - Update of certificates unspecified.
  - New SM protocol for contactless cards (Diffie‑Hellman).

### 9.4 TC 224 WG17
- **Objective**: Develop and maintain European Standards for Protection Profiles (PP) under Common Criteria v3 for electronic signature products.
- **Priority 1**:
  1. PP based on CWA 14169 (SSCD)
  2. PP based on FR DCSSI PP and CWA 14170 (SCA)
  3. PP for Identification and Authentication services (aligned with WG15/16)
- **Priority 2** (deferred): PPs based on CWA 14167, TR based on CWA 14355.
- **Liaison**: Franco Ruggieri as liaison between WG17 and ETSI ESI.
- **Opinion**: Ambitious program with limited participants; need for changes and improvements to input documents.

## Requirements Summary
*Note: This document is a Technical Report (informative). No normative “shall” requirements are introduced. The following are key recommendations and observations extracted from the report.*

| ID | Recommendation / Observation | Type | Reference |
|----|-----------------------------|------|-----------|
| R1 | CEN WS on eInvoicing should reference XAdES/CAdES but not mandate them due to complexity. | informative | 5.2.3 |
| R2 | For eInvoicing, simpler signature formats are acceptable if storage organisation is reliable. | informative | 5.2.4.2 |
| R3 | In eProcurement, multiple signatures on same document and signature policies for contracting authorities are needed. | informative | 6.3.3, 6.4 |
| R4 | UPU EPM provides a use case for electronic signature requirements. | informative | 7.1.2 |
| R5 | ETSI ESI should monitor CEN Workshops on keyUsage, SHA‑1, signature format profiles, trust‑service provider identification. | informative | 8.3 |
| R6 | For smart card eID, different PINs **shall** be used for non‑repudiation and authentication (WG16 opinion). | informative (opinion) | 9.3 |
| R7 | CEN/TC 224 WG17 will develop PPs for SSCD, SCA and I&A services under CC v3. | informative | 9.4 |

## Informative Annexes (Condensed)
### Annex A: CEN/ISSS e‑Invoicing Focus Group
- Final report (2003) analyses standardisation issues for e‑Invoicing under Directive 2001/115/EC.
- **Main conclusions**: Business and tax administrations need standardised approach; interoperability issues hinder harmonisation.
- **Recommendations**: Update 1994/820/EC, create ebXML core components, allow identifiers, develop code sets, broaden EDI definition.
- **Electronic signature**: Care not to restrict to natural persons; allow re‑signing by intermediaries; further work on authentication.
- **Storage**: Allow storage in non‑Member State if conditions met; remote audit access.

### Annex B: CEN/ISSS Workshop on Electronic Authentication
- **Part 1 (Architecture) – CWA 15264‑1**: Defines interoperability architecture for smart‑card based eID/eAuthentication in eGovernment. 4‑entity trust model, roles, processes (primary/secondary), interfaces (IOP#1‑#5), security requirements. Common requirements: support different security profiles, secure cardholder ID, authentication, electronic signature.
- **Part 2 (Best Practice Manual) – CWA 15264‑2**: For card scheme operators. Risk analysis, policy management, legal/contractual issues, privacy code of conduct, business case analysis, peer support mechanisms (e.g., Porvoo Group).
- **Part 3 (User Requirements) – CWA 15264‑3**: User interactions with smartcard‑based eID systems. General principles (intuitive, non‑intrusive, consistent). Cardholder authentication using PIN or biometrics. Electronic signature services. Process flows (registration, biometric enrolment, card issue/withdrawal, authentication, signing, renewal, lost/stolen).
- **Strategic vision document**: Summarises drivers and inhibitors for pan‑European eID. Recommends smart card based ID with digital signature and biometrics. Minimum requirements: eID system functionalities, authentication levels (identification, medium, high, non‑repudiation). Standardisation gaps in biometrics and combination of technologies.