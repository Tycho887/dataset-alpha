# ETSI TR 102 572 V1.1.1: Best Practices for handling electronic signatures and signed data for digital accounting
**Source**: ETSI | **Version**: V1.1.1 | **Date**: July 2007 | **Type**: Technical Report (Informative)
**Original**: Reference DTR/ESI-000046

## Scope (Summary)
This Technical Report identifies a set of practices for signing and storing fiscally relevant documents (e.g., e-invoices) using Advanced Electronic Signatures, based on a survey of practices in France, Germany, Italy, Spain, and the UK. It defines Minimum Identified Practices (MinIP), Maximum Identified Practices (MaxIP), and Commonly Acceptable Practices for Trust Service Providers (CAP-TSP). The practices are structured according to ISO/IEC 27001 controls, with additional signing/storage-specific controls.

## Normative References
- [1] CWA 15579: "E-invoices and digital signatures"
- [2] CWA 15580: "Storage of Electronic Invoices"
- [3] ISO/IEC 17799: "Information technology - Security techniques - Code of practice for information security management"
- [4] ISO/IEC 27001: "Information technology - Security techniques - Information security management systems - Requirements"
- [5] Directive 1999/93/EC (Electronic Signature Directive)
- [6] Council Directive 2001/115/EC (VAT e-invoicing)
- [7] ETSI TS 102 042: "Policy requirements for certification authorities issuing public key certificates"
- [8] ETSI TS 102 734: "Profiles of CMS Advanced Electronic Signatures based on TS 101 733 (CAdES)"
- [9] ETSI TS 102 904: "Profiles of XML Advanced Electronic Signatures based on TS 101 903 (XAdES)"
- [10] CWA 14169: "Secure signature-creation devices 'EAL 4+'"
- [11] Directive 95/46/EC (Data Protection)
- [12] ISO/IEC 15408: "Evaluation criteria for IT security"
- [13] ETSI TS 101 733: "CMS Advanced Electronic Signatures (CAdES)"
- [14] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)"
- [15] CWA 14170: "Security requirements for signature creation applications"
- [16] ETSI TS 101 862: "Qualified Certificate profile"
- [17] ETSI TS 101 456: "Policy requirements for certification authorities issuing qualified certificates"
- References from France, Germany, Italy, Spain, UK, and International Organisations (see original document for full list)

## Definitions and Abbreviations
### Definitions
- **Advanced Electronic Signature (AdES)**: electronic signature which is uniquely linked to the sender, is capable of identifying the signatory, is created using means that the signatory can maintain under his sole control, and is linked to the data to which it relates in such a manner that any subsequent change of the data is detectable (Directive 1999/93/EC Article 2 No. 2)
- **Commonly Acceptable Practices (CAP)**: practices for Trust Service Providers signing and/or storing data relevant for accounting (i.e., fiscally relevant data) which may be recognized as acceptable by authorities in several EU nations
- **electronic invoices**: invoices sent by electronic means as defined in Directive 2001/115/EC
- **fiscally relevant data**: data relevant to financial accounting related to the taxable person or company (book-keeping, invoicing, payroll, investment, etc.)
- **fiscally relevant document**: document or record containing fiscally relevant data
- **Maximum Identified Practices (MaxIP)**: most stringent practices identified for the signing and storage of fiscally relevant documents
- **Minimum Identified Practices (MinIP)**: least stringent practices identified for the signing and storage of fiscally relevant documents
- **Qualified Electronic Signature (QES)**: advanced electronic signature based on a qualified certificate and created by a secure-signature-creation device (Directive 1999/93/EC)
- **Secure Signature Creation Device (SSCD)**: signature-creation device meeting the requirements laid down in Annex III of Directive 1999/93/EC
- **Signature Creation Data (SCD)**: unique data (e.g., codes or private cryptographic keys) used by the signatory to create an electronic signature
- **statement of applicability**: documented statement describing the control objectives and controls relevant and applicable to the TSP's ISMS (ISO/IEC 27001)

### Abbreviations
- AdES, AFNOR, BPR, CA, CAP, CAP-TSP, CC, CNIPA, CRL, EDI, EUMS, FAT, HSM, IGAE, ISACA, ISMS, ITSEC, LDAP, MaxIP, MINEFI, MinIP, QES, SCD, SSCD, SSL, TIFF, TLS, TSP, VAT, WORM, XBRL, XML

## 4 General concepts
### 4.1 Basic Model
A trading party uses services to sign and store invoices, purchase orders, and other fiscally relevant documents, then passes them to trading partners. Stored information may be retrieved for VAT reports, commercial reports, and audits. Documents are protected using electronic signatures as required by national regulations.

### 4.2 VAT invoices and other fiscally relevant documents
The study covers a range of fiscally relevant documents. VAT invoicing is the area with the most harmonization (Directive 2001/115/EC). This document is most applicable to e-invoicing.

### 4.3 Minimum and maximum identified practices
Based on a survey of five EU states. Because of different regulatory frameworks, a single set of practices cannot cover all. Instead, the document defines:
- **MinIP**: least stringent practices meeting basic legal provisions for free circulation.
- **MaxIP**: most stringent practices acceptable across Europe.

### 4.4 Pan European model
Two parties trade under their own regulations but must consider pan-European requirements (see Figure 2 in original).

### 4.5 Trusted Service Providers (TSPs)
A TSP can support several trading parties in a single country. Trading documents are signed/stored by the TSP; reports remain the responsibility of the trading parties.

### 4.6 Commonly Acceptable Practices (CAP) for TSPs
CAP are defined for pan-European trade supported by TSPs. They may also be used as a basis for national practices or for self-practices.

## 5 Practices identified
### 5.1 Signature and storage requirements
#### 5.1.1 Signature
##### 5.1.1.1 Class of electronic signature
**Objective**: To employ a class of electronic signature that assures authenticity and integrity, and where applicable commitment to content, over the lifetime of individual fiscally relevant documents.
- **MaxIP**: Fiscally relevant documents, when electronically signed, **should** be signed with a Qualified Electronic Signature.
- **MinIP**: Invoices, where electronically signed, **should** be signed by an Advanced Electronic Signature (see Directive 2001/115/EC Article 2.2). Other fiscally relevant documents **may** be signed by an Advanced Electronic Signature.
- **CAP-TSP**: If fiscally relevant electronic documents are signed, the signature **should** be at least an Advanced Electronic Signature (Directive 1999/93/EC). Recommended signature formats: TS 102 734 (CAdES) or TS 102 904 (XAdES); if not fully sufficient, use TS 101 733 or TS 101 903.

##### 5.1.1.2 Certification
**Objective**: To obtain certificate from authority who can reliably certify public key and maintain revocation status information.
- **MaxIP**: Fiscally relevant documents, when electronically signed, **should** be supported by a qualified certificate. The CA issuing the qualified certificate **may** be accredited.
- **MinIP**: Fiscally relevant documents, when electronically signed, **should** be supported by a certificate issued by a CA that, if not qualified as per Directive 1999/93/EC, **should** at least meet some recognized policy requirements (e.g., TS 102 042) or be approved by a nationally recognized scheme.
- **CAP-TSP**: Electronically signed fiscally relevant documents **should** be supported by:
  1) a qualified certificate issued by a CA which **may** be accredited as per Article 3(2) of Directive 1999/93/EC; or
  2) a certificate issued by a CA operating under certificate policies as per TS 102 042 (NCP type) or nationally recognized reliable practices.

##### 5.1.1.3 Signature creation data
**Objective**: To ensure that the private signing key is kept secure.
- **MaxIP**: To sign fiscally relevant documents, signing keys **should** be kept in an SSCD certified per CWA 14169.
- **MinIP**: Security controls are applied to signing keys suitable to ensure that the signatory can maintain them under his sole control.
- **CAP-TSP**:
  1) Where a Qualified Electronic Signature is required, or where a hardware signature creation device is used, the signing key **should** be held in an SSCD certified per CWA 14169, or in a high security module certified to CC EAL4 or ITSEC E3 (or comparable criteria recognized in an EUMS).
  2) Where an Advanced Electronic Signature is used, security controls **should** be applied to ensure the signatory maintains sole control. In particular:
     a) where a TSP holds keys on behalf of its users, the TSP **should** ensure signing keys can be only used by their owners.
     b) where a signing key held by the TSP belongs to a legal person, the TSP **should** ensure that signatures can be issued only by users explicitly authorized to act for the company.
  **NOTE**: Where legally allowed, signing keys can also be used by persons explicitly delegated by their owners, including the TSP.

##### 5.1.1.4 Certificate subject's registration
**Objective**: To ensure the certificate holder's correct registration.
- **MaxIP**: Subjects' registration **should** be based on their secure identification, where applicable via legally valid or commonly accepted identity documents (e.g., passports, identity cards, driving licences, etc.) and supported by documentation specifying their roles and signing powers (e.g., maximum transaction values) as well as authorization to act for the taxable person.
- **MinIP**: Where a qualified certificate is used, its subjects' registration management **should** be deemed acceptable by other EUMS countries. Where non-qualified certificates are used, an agreement on their usage and registration procedures **should** exist between the issuing CA's country and the receiving organization's country.
- **CAP-TSP**: Same as MaxIP.

##### 5.1.1.5 Certificate revocation
**Objective**: To ensure that when required only authorized persons can request revocation of a certificate and that revocation is carried in a timely manner.
- **MaxIP**: Revocation **should** be requested in a timely manner by an authorized subject (certificate owner, subscriber, or other specifically authorized person), authenticated (could include electronic secure identification). The CA or delegate **should** ensure timely processing and suitable publication of revoked certificate status (e.g., CRL).
- **MinIP**: Where a qualified certificate is used, its revocation management **should** be deemed acceptable by other EUMS countries. Where non-qualified certificates are used, an agreement on revocation procedures **should** exist between the issuing CA's country and the receiving organization's country.
- **CAP-TSP**: Same as MaxIP.

#### 5.1.2 Maintenance of signature over storage period
**Objective**: To ensure that the electronic signatures are maintained such that their validity can be verified for the entire storage period.
- **MaxIP**: Signature verifiability **should** be ensured for the entire storage period. Can be implemented by technical or organizational measures or a combination:
  - **Technical**: All information required for signature verification (certificate path, revocation information) and a trusted time-stamp **should** be stored for the same period as the signed document, preserving integrity. If storage period exceeds assured cryptographic strength, additional integrity mechanisms (e.g., archive time-stamps per TS 101 733 or TS 101 903, or WORM media) **should** be applied.
  - **Organizational**: Storage kept by a trusted organization that can prove signature was verified before acceptance per generally recognized procedures.
  - **Combination**: Where organizational measures provide equivalent reliability, some technical procedures **may** be waived.
- **MinIP**: If a signed document is kept for the required period in conformity with regulations in the EUMS where it is located, it **should** be accepted in any other EUMS.
- **CAP-TSP**: Same as MaxIP.

#### 5.1.3 Storage
##### 5.1.3.1 Authorized access
**Objective**: To make documents securely available to authorized parties (company officers, auditors, tax authority) as required by applicable legislation.
- **MaxIP**: Access **should** be allowed to related company officials, tax authority inspectors, and other legally authorized authorities. Where electronic remote access is legally required, it **should** be implemented securely (e.g., user password and TLS over Internet) with authenticated remote user and server, and protected integrity and confidentiality.
- **MinIP**: Access **should** be allowed at least to authorized company officers and authorized authorities (e.g., tax agency inspectors). No remote access required.
- **CAP-TSP**: Access **should** be allowed to company officials and authorized authorities. Where remote access is legally required, it **should** be reliably secure (e.g., user password and SSL/TLS over Internet) with authenticated parties and protected communications.

##### 5.1.3.2 Authenticity and integrity
**Objective**: To maintain authenticity of origin and integrity of fiscally relevant data held in storage, detecting loss or unauthorized addition.
- **MaxIP**: Authenticity and integrity **should** be ensured by:
  - appropriate class of signature (clause 5.1.1.1);
  - maintenance of that signature over storage period (clause 5.1.2);
  - mechanisms to detect loss or unauthorized addition of documents.
- **MinIP**: Where signed, authenticity and integrity **should** be ensured by technical measures recognized as valid in the company's country (e.g., compliance with ISO/IEC 17799). For e-invoices, storage **should** abide by country rules that may require storage of data guaranteeing authenticity and integrity as per Directive 2001/115/EC.
- **CAP-TSP**: Same as MaxIP.

##### 5.1.3.3 Readability
**Objective**: To ensure documents remain human or machine readable over the storage period.
- **MaxIP**: Original document format (or another suitable legally valid format derived under trusted supervision) **should** be ensured readable by the storing organization, e.g., by storing related visualising software before it becomes unavailable. If necessary, required hardware and environmental software **should** be stored as well. If a document/viewer system becomes obsolete, all affected documents **should** be reliably copied keeping semantics unchanged, with an independent trusted assertion attesting content correspondence.
- **MinIP**: No specific requirement, but the storing organization is liable for any lack of readability. Documents **should** be exhibited on paper and/or electronically.
- **CAP-TSP**: Original format (or another suitable format reliably derived) **should** be ensured readable, e.g., by storing visualising software and hardware before obsolescence. If obsolete, documents **should** be reliably copied with an independent trusted assertion.

##### 5.1.3.4 Storage media type
**Objective**: To ensure media can withstand time and possible deterioration.
- **MaxIP**: Media and readers **should** be able to withstand the required storage time. If risk of unreadability due to obsolescence or degradation, content **should** be timely copied onto another suitable media. If integrity depends on media (e.g., WORM), copying **should** include controls (e.g., trusted third parties) to maintain integrity.
- **MinIP**: No specific requirement, but the storing organization **may** be liable for document loss due to media deterioration. No specific media type required, provided organizational measures are in place to timely copy content of unreliable media with assurance that content is unchanged.
- **CAP-TSP**: Same as MaxIP (but "where possible").

##### 5.1.3.5 Documents format
**Objective**: To ensure documents are kept in a format that prevents changes to presentation or automatic processing results.
- **MaxIP**: Fiscally relevant documents **should** be produced in a format preventing any change not detected by integrity controls (e.g., malicious code in macros, scripts, hidden code). Users **should** be made aware of unreliable formats (CWA 14170 clause 8.6). If XML is used, either acceptable style sheets referenced and included in signature calculation, or a standard syntax with fully defined semantics (e.g., XBRL) is recommended. Documents **should** be stored in original format if void of malicious code; otherwise, a suitable format **should** be stored instead (or additionally) with a reliable assertion on content correspondence.
- **MinIP**: No specific requirement, but the issuing organization **may** be liable for future changes in presentation.
- **CAP-TSP**: Same as MaxIP.

##### 5.1.3.6 Requirements on separation and confidentiality
**Objective**: To ensure electronic data related to different owner organizations are stored and archived separately.
- **MaxIP**: Storage **should** provide clear separation between different owners to prevent compromise of confidentiality. If storing data for different taxable persons, storage **should** be clearly separated, e.g., by marking data with owner identifier, restricting access, different storage areas/media/locations.
- **MinIP**: Storage of each owner's information **should** ensure confidentiality.
- **CAP-TSP**: Storage **should** be clearly physically or logically separated between owners to prevent compromise of confidentiality. Same examples as MaxIP.

#### 5.1.4 Reporting to and exchanges with authorities
**Objective**: To ensure fiscally relevant documents are reported/exchanged with authorities in a secure manner (integrity and source security).
**NOTE**: Submission is generally the responsibility of the taxable person.
- **MaxIP**: Documents **should** be submitted by secure electronic means, signed at least with an Advanced Electronic Signature (or Qualified where required). Measures from clause 5.1.2 **should** also be provided where possible. Secure channels (e.g., TLS) **should** additionally be used.
- **MinIP**: Secure submission of signed reports **should** use secure channels (e.g., password and TLS over Internet).
- **CAP-TSP**: Submission **should** require secure channels with authenticated parties and protected communications (e.g., user password and TLS over Internet). Advanced Electronic Signatures (or Qualified) **should** also be used. Controls from clause 5.1.2 **should** be provided where possible.

#### 5.1.5 Conversion of paper originals to digital formats
**Objective**: To ensure that when fiscally relevant documents originally in paper (or other non-digital formats) are converted, their content is preserved without change.
- **MaxIP**: Correspondence between paper and digital image **should** be ensured. This requires an assertion (even electronic) by a trusted person who either carries out conversion or later compares. The digital image and assertion **should** be signed to protect authenticity and integrity.
- **MinIP**: Correspondence **should** be ensured. Where rules do not exist, a process meeting suitable standards (e.g., ISO/IEC 17799) **should** ensure content is not altered during transformation.
- **CAP-TSP**: Correspondence **should** be ensured. Where rules do not exist, a process in line with best practice (ISO/IEC 17799 or, where applicable, assessed per ISO/IEC 27001) **should** ensure content matches. Where required by country rules or identified from ISMS, the digital version **should** be associated with an assertion (e.g., electronically signed addendum) on correspondence issued by a trusted person. The assertion can be explicit or implicit. The digital image and assertion **should** be signed.

### 5.2 Information security management
The following clauses are based on annex A of ISO/IEC 27001 and ISO/IEC 17799. The organization's ISMS **should** be assessed as conformant to ISO/IEC 27001 or at least operated on ISO/IEC 17799 or equivalent guidance.
- **MaxIP**: IT systems of organizations issuing and storing fiscally relevant electronic documents **should** incorporate controls complying with ISO 27001 annex A as identified in its statement of applicability. Conformance assessment/certification of the ISMS per ISO/IEC 27001 is also recommended, unless applicable regulations ensure an equivalent trust level.
- **MinIP**: No special provision in addition to applicable regulations. However, it is wished that any organization implementing an ISMS develops and maintains it based on ISO/IEC 27001, ISO/IEC 2700x series, or nationally developed guidance.
- **CAP-TSP**: Unless applicable regulations specify requirements, IT systems **should** implement an ISMS in line with ISO/IEC 27001 (e.g., according to ISO/IEC 17799). Conformance assessment/certification per ISO/IEC 27001 is also recommended, unless equivalent trust level is achieved.

#### 5.2.1 Risk analysis
Risk analysis **shall** be performed initially and repeated regularly to identify, quantify, and prioritize risks against acceptance criteria and objectives (ISO/IEC 17799 clause 4).

#### 5.2.2 Security policy
##### 5.2.2.1 Information security policy
**Objective**: To provide management direction and support for information security.
- **MaxIP**: Reliable security policy **should** be in force and enforced by the company issuing and storing fiscally relevant electronically signed documents.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

#### 5.2.3 Organizing information security
##### 5.2.3.1 Internal organization
**Objective**: To manage information security within the organization.
- **MaxIP**: ISO/IEC 17799 controls in clause 6.1 **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.3.2 External parties
**Objective**: To maintain security of information and processing facilities accessed, processed, communicated to, or managed by external parties.
- **MaxIP**: Suitable stipulations **should** be in force between service providers and outsourcing organizations, clearly specifying duties and responsibilities. ISO/IEC 17799 clause 6.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

#### 5.2.4 Asset management
##### 5.2.4.1 Responsibility for assets
**Objective**: To achieve and maintain appropriate protection of organizational assets.
- **MaxIP**: All sensitive assets **should** have a specific accountable owner. ISO/IEC 17799 clause 7.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.4.2 Information classification
**Objective**: To ensure information receives an appropriate level of protection.
- **MaxIP**: Signing material **should** be treated as addressed by Directive 1999/93/EC. Fiscal electronic documents issuance and storage assets, including personal data, **should** be inventoried and classified according to secrecy level even if no specific legal classification is required. Fiscally relevant documents **should** be treated as company confidential unless indicated otherwise. ISO/IEC 17799 clause 7.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: All private signing keys **should** be treated as sensitive and protected by special measures (see clause 5.1.1.3). Fiscally relevant documents **should** be treated as company confidential unless indicated otherwise (see clause 5.1.3.6). ISO/IEC 17799 clause 7.2 controls **should** be implemented.

#### 5.2.5 Human resources security
##### 5.2.5.1 Prior to employment
**Objective**: To ensure employees, contractors, and third party users understand responsibilities, are suitable for roles, and reduce risk of theft, fraud, or misuse.
- **MaxIP**: Candidate screening **should** be performed in accordance with applicable legislation, capable to assess suitability. Personnel covering sensitive roles **should** be clearly informed in writing of their duties and responsibilities and accept in writing. ISO/IEC 17799 clause 8.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.5.2 During employment
**Objective**: To ensure awareness of security threats, responsibilities, and reduce human error.
- **MaxIP**: Personnel, including involved managers, **should** be suitably equipped, educated, and informed on task duties and consequences of misbehaviour. ISO/IEC 17799 clause 8.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP (applied to TSP personnel in trusted roles).

##### 5.2.5.3 Termination or change of employment
**Objective**: To ensure orderly exit or change.
- **MaxIP**: Personnel **should** be informed of confidentiality duties even after termination, and on consequences of non-compliance. All company equipment **should** be returned and privileges withdrawn unless otherwise specified. ISO/IEC 17799 clause 8.3 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP (applied to personnel in trusted roles).

#### 5.2.6 Physical and environmental security
##### 5.2.6.1 Secure areas
**Objective**: To prevent unauthorized physical access, damage, and interference.
- **MaxIP**: Systems for issuing and storing fiscally relevant documents **should** be located in secured areas. Access to premises **should** be limited to duly authorized officers, preferably in dual control regime, and logged. ISO/IEC 17799 clause 9.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.6.2 Equipment
**Objective**: To prevent loss, damage, theft, compromise, and interruption.
- **MaxIP**: Equipment **should** be protected to prevent compromise, unauthorized data insertion, and denial of service. Information to be kept for legally required time **should** not be held in a single copy. Suitable measures against accidents and incidents **should** be in place. ISO/IEC 17799 clause 9.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Suitable measures **should** be established to protect TSP signing and storage assets; continuity measures **should** be in place. ISO/IEC 17799 clause 9.2 controls **should** be implemented.

#### 5.2.7 Communications and operations management
##### 5.2.7.1 Operational procedures and responsibilities
**Objective**: To ensure correct and secure operation of information processing facilities.
- **MaxIP**: Precise responsibilities **should** be assigned and clear procedures defined. Segregation of duties regarding key activities is paramount. ISO/IEC 17799 clause 10.1 controls **should** be implemented (change management, separation of development/test/operational environments, segregation of duties).
- **MinIP**: No special provisions.
- **CAP-TSP**: Clear procedures **should** be defined for TSP trusted roles, with precise responsibilities and segregation of duties. Trusted roles include Security Officers, System Administrators, System Operators, System Auditors. ISO/IEC 17799 clause 10.1 controls **should** be implemented.

##### 5.2.7.2 Third party service delivery management
**Objective**: To maintain appropriate level of information security and service delivery in line with third party agreements.
- **MaxIP**: Outsourcing does not relieve the principal party from responsibility; they **should** ensure outsourcers comply with all obligations. ISO/IEC 17799 clause 10.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: The outsourcing party **should** verify that third parties comply with obligations (preliminary assessment, service agreements, monitoring, on-site auditing). ISO/IEC 17799 clause 10.2 controls **should** be implemented.

##### 5.2.7.3 System planning and acceptance
**Objective**: To minimize risk of systems failures.
- **MaxIP**: Fiscal document issuing organizations **should** plan processing capacity to meet peak periods and commitments. ISO/IEC 17799 clause 10.3 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP, with capacity planning assessed by balancing cost, penalties, insurance, loss of image/customer base.

##### 5.2.7.4 Protection against malicious and mobile code
**Objective**: To protect integrity of software and information.
- **MaxIP**: Macros and hidden code that could surreptitiously change document presentation **should** be absent. If users cannot reliably ascertain absence, all macros and hidden code **should** be removed. ISO/IEC 17799 clause 10.4 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: See clause 5.1.3.5 for malicious code in documents. ISO/IEC 17799 clause 10.4 controls **should** be implemented.

##### 5.2.7.5 Back-up
**Objective**: To maintain integrity and availability of information and processing facilities.
- **MaxIP**: Organizations **should** arrange physical, processing, personnel structure to meet exhibition requirements even in case of accidents. This **should** imply back-up storage sites and a recovery plan. ISO/IEC 17799 clause 10.5 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Exhibition requirements **should** be fulfilled even in case of accidents, implying back-up storage sites and recovery plan. Sizing **may** be balanced between cost, penalties, intangible assets.

##### 5.2.7.6 Network security management
**Objective**: To ensure protection of information in networks and supporting infrastructure.
- **MaxIP**: Networks regarding fiscal documents **should** be protected to prevent unauthorized data insertion/deletion or disclosure. ISO/IEC 17799 clause 10.6 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.7.7 Media handling
**Objective**: To prevent unauthorized disclosure, modification, removal, destruction, or interruption.
- **MaxIP**: Media protection **should** be enforced during entire handling process (purchase, delivery, storage, installation, disposal) to ensure integrity and prevent hidden code insertion or compromise of confidentiality. ISO/IEC 17799 clause 10.7 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Media protection **should** be enforced to ensure integrity and confidentiality up to authorized disposal. ISO/IEC 17799 clause 10.7 controls **should** be implemented.

##### 5.2.7.8 Exchange of information
**Objective**: To maintain security of information exchanged within an organization and with external entities.
- **MaxIP**: Information **should** be securely exchanged between system components, document issuer and customers, and customers' counterparts (all communications facilities). ISO/IEC 17799 clause 10.8 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Fiscally relevant information **should** be securely exchanged between all systems components and parties. ISO/IEC 17799 clause 10.8 controls **should** be implemented.

##### 5.2.7.9 Electronic commerce services
**Objective**: To ensure security of electronic commerce services and their secure use.
- **MaxIP**: ISO/IEC 17799 clause 10.9 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: When e-commerce is managed by the organization on behalf of customers, the information flow **should** be managed in secure mode. ISO/IEC 17799 clause 10.9 controls **should** be implemented.

##### 5.2.7.10 Monitoring
**Objective**: To detect unauthorized information processing activities.
- **MaxIP**: Auditing/monitoring is paramount for a trusted organization. ISO/IEC 17799 clause 10.10 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Suitable auditing/monitoring is paramount. ISO/IEC 17799 clause 10.10 controls **should** be implemented.

#### 5.2.8 Access control
##### 5.2.8.1 Business Requirement for Access Control
**Objective**: To control access to information.
- **MaxIP**: ISO/IEC 17799 clause 11.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.8.2 User access management
**Objective**: To ensure authorized user access and prevent unauthorized access.
- **MaxIP**: Organizations issuing and storing fiscal documents on behalf of customers **should** implement rigid measures to manage the entire process of authorizing users, from registration to deregistration, including authentication management. ISO/IEC 17799 clause 11.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Rigid measures **should** be implemented for user authorization from registration to deregistration. ISO/IEC 17799 clause 11.2 controls **should** be implemented.

##### 5.2.8.3 User responsibilities
**Objective**: To prevent unauthorized user access, compromise, or theft.
- **MaxIP**: External and internal authorized users **should** be made aware in writing of their responsibilities and the need for cooperation to prevent unauthorized accesses. Clean desk policy **should** be enforced where applicable. ISO/IEC 17799 clause 11.3 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.8.4 Network access control
**Objective**: To prevent unauthorized access to networked services.
- **MaxIP**: Organizations with online connections **should** have processes to manage and monitor access authorizations. ISO/IEC 17799 clause 11.4 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.8.5 Operating system access control
**Objective**: To prevent unauthorized access to operating systems.
- **MaxIP**: Access control **should** be carefully implemented to prevent unauthorized access to key resources. Where possible, operating systems verified to a suitable level of security criteria (e.g., ISO/IEC 15408) **should** be adopted. Logs **should** be carefully inspected. ISO/IEC 17799 clause 11.5 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Access control **should** be carefully implemented. Logs **should** be carefully protected and inspected. ISO/IEC 17799 clause 11.5 controls **should** be implemented.

##### 5.2.8.6 Application and information access control
**Objective**: To prevent unauthorized access to information held in application systems.
- **MaxIP**: An organization handling and processing fiscally relevant documents on behalf of third parties **should** have a process to manage the entire cycle of strongly authenticating users accessing information and applications. ISO/IEC 17799 clause 11.6.1 (storage) and 11.6.2 (signing keys) **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP (authenticating users accessing information and related applications).

##### 5.2.8.7 Mobile computing and teleworking
**Objective**: To ensure information security when using mobile computing and teleworking facilities.
- **MaxIP**: Mobile computing is highly prone to attacks; if adopted, ISO/IEC 17799 clause 11.7 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: If mobile computing is adopted, its risks **should** be carefully evaluated and countered. ISO/IEC 17799 clause 11.7 controls **should** be implemented.

#### 5.2.9 Information systems acquisition, development and maintenance
##### 5.2.9.1 Security requirements of information systems
**Objective**: To ensure security is an integral part of information systems.
- **MaxIP**: Security requirements **should** be identified and agreed prior to development and/or implementation. ISO/IEC 17799 clause 12.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.9.2 Correct processing in applications
**Objective**: To prevent errors, loss, unauthorized modification, or misuse.
- **MaxIP**: Strict controls **should** be implemented for procedures issuing (especially bulk) and storing fiscal documents. ISO/IEC 17799 clause 12.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Strict controls **should** be implemented for signing and storing fiscally relevant documents including bulk signing. ISO/IEC 17799 clause 12.2 controls **should** be implemented.

##### 5.2.9.3 Cryptographic controls
**Objective**: To protect confidentiality, authenticity, or integrity by cryptographic means.
- **MaxIP**: In countries where sensitive data protection (Directive 95/46/EC) requires encryption, key management is necessary in addition to signing requirements. ISO/IEC 17799 clause 12.3 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.9.4 Security of system files
**Objective**: To ensure security of system files.
- **MaxIP**: ISO/IEC 17799 clause 12.4 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.9.5 Security in development and support processes
**Objective**: To maintain security of application system software and information.
- **MaxIP**: Applications **should** be developed, tested, and put into operation according to clearly defined security procedures. ISO/IEC 17799 clause 12.5 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Applications **should** be developed, tested, and operated according to clearly defined quality assurance procedures. ISO/IEC 17799 clause 12.5 controls **should** be implemented.

##### 5.2.9.6 Technical vulnerability management
**Objective**: To reduce risks from exploitation of published technical vulnerabilities.
- **MaxIP**: The organization **should** have a regular process to monitor published vulnerabilities and timely upgrade security measures. ISO/IEC 17799 clause 12.6 control **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

#### 5.2.10 Information security incident management
##### 5.2.10.1 Reporting information security events and weaknesses
**Objective**: To ensure events and weaknesses are communicated in a manner allowing timely corrective action.
- **MaxIP**: Even if not legally required, it is highly recommended to set in place suitable incident reporting and management procedures and policies involving internal and external officers and users. ISO/IEC 17799 clause 13.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: The TSP **should** have in place suitable incident reporting and management procedures and policies. ISO/IEC 17799 clause 13.1 controls **should** be implemented.

##### 5.2.10.2 Management of information security incidents and improvements
**Objective**: To ensure consistent and effective approach to incident management.
- **MaxIP**: Managing incidents and improving the ISMS is highly recommended. ISO/IEC 17799 clause 13.2 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: The TSP **should** have suitable incident management procedures and policies. ISO/IEC 17799 clause 13.2 controls **should** be implemented.

#### 5.2.11 Business continuity management
##### 5.2.11.1 Information security aspects of business continuity management
**Objective**: To counteract interruptions and protect critical processes from major failures or disasters, ensuring timely resumption.
- **MaxIP**: The same rationale as clause 5.2.7.3 MaxIP applies. A suitable Business Continuity Plan **should** be carefully evaluated taking into account benefits, costs, penalties, insurance, loss of image/customer base. ISO/IEC 17799 clause 14.1 controls **should** be implemented.
- **MinIP**: No special provisions.
- **CAP-TSP**: To meet fiscal deadlines and exhibit documents when necessary, a suitable Business Continuity Plan **should** be carefully evaluated, addressed by a Service Level Agreement. ISO/IEC 17799 clause 14.1 controls **should** be implemented.

#### 5.2.12 Compliance
##### 5.2.12.1 Compliance with legal requirements
**Objective**: To avoid breaches of law, statutory, regulatory, or contractual obligations.
- **MaxIP**: Compliance with the law is required. Where cross-border document validity is sought, it **may** be necessary to abide by all involved countries' legislation/regulations.
- **MinIP**: Minimum goal: abide by the organization's country of residence's legislation/regulation.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.12.2 Compliance with security policies and standards and technical compliance
**Objective**: To ensure compliance of systems with organizational security policies and standards.
- **MaxIP**: Security Policy compliance **should** be met. ISO/IEC 17799 clause 15.2 controls **should** be implemented. Where legislation/regulations are applicable, they prevail, but ISO/IEC 27001 annex A provisions (via ISO/IEC 17799) **should** be used to fill gaps.
- **MinIP**: No special provisions.
- **CAP-TSP**: Same as MaxIP.

##### 5.2.12.3 Information systems audit considerations
**Objective**: To maximize effectiveness and minimize interference to/from the audit process.
- **MaxIP**: Auditing according to generally recognized methods is indispensable to ensure continuous trustworthiness, even if no specific legal requirement exists. ISO/IEC 17799 clauses 15.3.1–15.3.2 controls **should** be implemented.
- **MinIP**: No special provision in addition to country legislation. However, it is wished that any organization implementing an ISMS develops and maintains it based on ISO/IEC 17799, ISO/IEC 2700x series, or nationally developed guidance.
- **CAP-TSP**: Even if no specific legal requirement, an appropriate auditing process **should** be in place. ISO/IEC 17799 clauses 15.3.1–15.3.2 controls **should** be implemented.

## Annex A: Country details (Condensed)
The following summaries are based on the survey of France (FR), Germany (DE), Italy (IT), Spain (SP), and United Kingdom (UK). For each subclause, the country-specific practices are keyed to MinIP/MaxIP/CAP.

### A.1 Signature and storage requirements
#### A.1.1 Signature
##### A.1.1.1 Class of electronic signature
- **DE**: Electronic invoices require Advanced Electronic Signature with qualified certificate.
- **FR**: Advanced Electronic Signature required; qualified certificate not mandatory.
- **IT**: Qualified Electronic Signature required for all signed fiscally relevant documents (except customs declarations using Article 5(2) signature).
- **SP**: E-invoices require Advanced Electronic Signature with qualified certificate. BPR uses PKCS#7 with qualified certificates; IGAE requires XAdES-BES with qualified certificates.
- **UK**: No legal requirement for advanced electronic signatures.

##### A.1.1.2 Certification
- **DE**: All CAs have accreditation; qualified certificates required for e-invoices. General accounting principles refer to "adequate" security.
- **FR**: Certificates not necessarily qualified for e-invoices; company certificates accepted. VAT e-declaration requires certificates from "reference Certificate Authority" (MINEFI recognized).
- **IT**: Qualified CAs (per Directive 1999/93/EC Article 3(3)) necessary; all qualified CAs also accredited by CNIPA.
- **SP**: BPR defines different certification policies. IGAE uses qualified certificates aligned with TS 101 862. AEAT recognizes certain certificate types.
- **UK**: tScheme is the recognized scheme for trustworthy CAs; Webtrust also acceptable.

##### A.1.1.3 Signature creation data
- **DE**: Qualified signatures require SSCD (smartcard or token; HSM not accepted unless evaluated as SSCD).
- **FR**: No obligation for HSM; private key under exclusive control of signatory. SSCD required for QES.
- **IT**: QES required, so CC EAL4 or ITSEC E3 certified SSCD/HSM is used.
- **SP**: BPR requires key generation at register office or using office facilities; password-protected cryptographic card. IGAE plans cryptographic cards. E-invoices require secure signature creation device (per RD 1496/2003).
- **UK**: No special requirements.

##### A.1.1.4 Certificate subject's registration
- **DE**: Qualified certificates for e-invoices require proper identification of natural person by RA/CA.
- **FR**: MINEFI recognized CAs follow "PC-Type" certification policy template, consistent with TS 101 456.
- **IT**: Detailed identity and attribute verification at registration; accreditation evaluates Registration procedures.
- **SP**: BPR requires identity card; other trusted documents for roles and values. IGAE requires identity card or similar; registration can be done electronically using the certificate.
- **UK**: No special requirements.

##### A.1.1.5 Certificate revocation
- **DE**: Qualified certificates require CA to update revocation list; CRL available online or at intervals free of charge.
- **FR**: MINEFI CAs follow "PC-Type" template; certificates cannot be suspended; revocation requesters are specified.
- **IT**: Detailed requirements on revocation requesters authentication and authorization; accreditation evaluates revocation.
- **SP**: BPR defines revocation procedures; revocation requested at designated offices; electronic request in high urgency. CRLs publicly available via Web and LDAP.
- **UK**: No special requirements.

#### A.1.2 Maintenance of signature over storage period
- **DE**: For e-invoices and general data, authenticity and integrity must be verified; certificates need not be valid at inspection time.
- **FR**: Recipient must verify certificate validity upon receipt and during storage; invoice, signature, and certificate stored in original version. No requirement for verification over storage period.
- **IT**: Every 15 days (e-invoices) or yearly, a file of digests of all stored documents is created, signed with QES and time-stamped. Signed file and TST entrusted to Tax Authority. TSTs kept on non-modifiable media for at least 5 years.
- **SP**: Corporate accounts stored for 5 years. BPR verifies signature and signs/time-stamps a notification proving certificate validity at that time. For e-invoices, storage must ensure readability and availability of signature data and mechanisms (RD 1496/2003).
- **UK**: No special requirements.

#### A.1.3 Storage
##### A.1.3.1 Authorized access
- **DE**: Accounts available to tax inspectors on request (remote access not required; access via CD, DVD, WORM, etc.). Storage must support data protection.
- **FR**: Documents must be made available to government on request in clear language (on screen, electronic media, or paper).
- **IT**: Tax authority inspectors have right to access any fiscally relevant document, including by telematic means; data must be accessible via indexed searches.
- **SP**: BPR performs access control; book accounts accessible to owners and Spanish Tax Agency. Annual accounts accessible to registered persons after fee payment; recent law makes information accessible to any public servant and notary.
- **UK**: Accounts available to tax inspectors on request; storage supports data protection.

##### A.1.3.2 Authenticity and integrity
- **DE**: For e-invoices, documents and testimonials of authenticity (e.g., QES) are stored. For general data, documentation of procedures and log files must be stored.
- **FR**: Use of advanced electronic signature ensures integrity; all data stored in original format. EDI also allowed.
- **IT**: Integrity ensured by QES and measures in clause A.1.2 (maintenance of signature).
- **SP**: Documents signed before submission via SSL. IGAE integrity ensured by signatures and access control. E-invoices integrity ensured by signatures or EDI.
- **UK**: VAT invoices may be protected by any mechanism that imposes satisfactory control over authenticity and integrity; supporting data must be accurate and complete. Other mechanisms allowed besides AdES.

##### A.1.3.3 Readability
- **DE**: Readability means data not corrupted or damaged; data may be machine-readable or human-readable. PDF/TIFF not allowed as sole archive format; machine-readability must be guaranteed for tax inspection.
- **FR**: Electronic invoices defined as structured messages readable by computer; must be stored in original format; transposition to paper on request.
- **IT**: Documents must be in "un-modifiable" format (no macro or hidden code). If unreadable, convert to another format with trusted person attesting correspondence.
- **SP**: Readability of annual and book accounts preserved (TIFF or text specified by BOE). BPR detects malicious code in incoming documents. E-invoices readability preserved in original format.
- **UK**: Invoices must be accessible and readable throughout storage period.

##### A.1.3.4 Storage media type
- **DE**: Storage media can be optical or other electronic (e.g., CD-Rom, DVD, disks with FAT file system). No specific technology; medium should not allow changes.
- **FR**: Messages kept in original format on numeric support for at least six years; thereafter company's choice of support. Hardware/software changes require conversion to maintain compatibility.
- **IT**: Document must be legible at all times; person in charge verifies readability at most every five years; if media become unreadable, timely copy onto suitable media.
- **SP**: BPR storage media must satisfy readability requirements.
- **UK**: Invoices must be accessible and readable throughout storage period.

##### A.1.3.5 Documents format
- **DE**: No specific format required; fiscally relevant electronic documents must be protected against loss of integrity. Machine-readable format preferred for digital tax inspection.
- **FR**: Electronic invoice is a structured message (XML, PDF, but not Word, Excel).
- **IT**: Electronically signed documents must have no macros or hidden code.
- **SP**: Annual and book accounts formats (TIFF, text) specified by BOE; work on XBRL starting. IGAE formats also specified.
- **UK**: XML preferred for tax reports; no restrictions on VAT invoices.

##### A.1.3.6 Separation and confidentiality of stored data
- **DE**: Storage must be clearly separated between companies (e.g., different storage media).
- **FR**: Same company can store information of several companies using separate means; common storage not conforming to law.
- **IT**: No specification for service providers; relevant decree requires chronological order and no solution of continuity per tax period, and search functions.
- **SP**: BPR and IGAE keep documents from each entity separated.
- **UK**: No special provisions; information generally treated as company confidential.

#### A.1.4 Reporting to and exchanging data with authorities
- **DE**: Access granted to tax authorities via remote access; data stored on unchangeable medium.
- **FR**: VAT declaration by electronic means; digitally signed if via WEB; secure channel (HTTPS) with client certificate authentication.
- **IT**: Annual accounting reports deposited at Chamber of Commerce solely in electronic format, signed with QES. Other documents entrusted to authority as per clause A.1.2. Customs declarations use Article 5(2) signature.
- **SP**: Companies submit book and annual accounts to Business Registry yearly via SSL; documents signed with SCR certificate. Public agencies submit signed expenses dossiers via secure channels.
- **UK**: Submission of accounting reports protected using SSL with password or authentication certificate.

#### A.1.5 Conversion of paper originals to digital formats
- **DE**: Scanned paper documents must match electronic data.
- **FR**: Copy must be exact and durable reproduction; verification at creation time. Scanned paper invoice cannot be considered original.
- **IT**: Paper documents can be transformed into electronic format via scanning; correspondence ensured via QES (by storage person if not unique copy; by notary/public officer if unique copy).
- **SP**: No general regulation; scanned documents allowed by BPR if electronically signed. External audit reports require original even if scanned.
- **UK**: No special provisions.

### A.2 Information security management
Country details for each subclause of clause 5.2 are summarized in the original document (Annex A, clauses A.2.1 to A.2.11). Key points:
- **DE**: IT Grundschutz Manual is referenced; accredited CAs have additional measures. Segregation of duties important.
- **FR**: AFNOR standards (Z42-013, Z43-400) often followed. PRIS templates for certification policies. Data protection law 2004-801 applies.
- **IT**: No general ISP requirement; CNIPA Deliberation 11/2004 on substitutive conservation. QCAs and REM providers have specific rules.
- **SP**: BPR has defined security policy aligned with Personal Data Protection Law; IGAE follows security policy defined by coordination committee. Both align with ISO/IEC 17799 in intention.
- **UK**: No special provisions beyond ISO/IEC 17799 applicability.

## Requirements Summary
Due to the large number of requirements, a full table is not included here. Each subclause in clause 5 contains explicit **shall**, **should**, **may** statements for MaxIP, MinIP, and CAP-TSP. Refer to the structured list above for the exact normative language.

## Informative Annexes (Condensed)
- **Annex A: Country details** – Provides detailed country-specific practices for France, Germany, Italy, Spain, and the UK for each subclause of clause 5. These details form the basis of the MinIP, MaxIP, and CAP-TSP practices identified in the main body. Key differences include mandatory QES (IT, DE for invoices), varying certification requirements, signature creation device specifications, storage media rules, and information security management approaches.