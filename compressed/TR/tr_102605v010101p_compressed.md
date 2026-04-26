# ETSI TR 102 605 V1.1.1 (2007-09): Electronic Signatures and Infrastructures (ESI); Registered E-Mail
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2007-09 | **Type**: Technical Report (Informative)
**Original**: https://www.etsi.org/deliver/etsi_tr/102600_102699/102605/01.01.01_60/tr_102605v010101p.pdf

## Scope (Summary)
This Technical Report summarizes a survey of existing and prospective Registered E-Mail (REM) systems in Europe, with the aim of identifying requirements for future standardization. It covers market status, legal/regulatory frameworks, services, system architectures, security features, policies, and existing related standards.

## Normative References (Informative)
- Universal Postal Union S43-3: "Secured Electronic Postal Services Interface Specification"
- CEN TS 15130: "Postal Services - DPM infrastructure - Messaging supporting DPM applications"
- OASIS Committee Specification Electronic PostMark (EPM): Profile of OASIS Digital Signature Service Version 1.0
- ISO/IEC 13888 (Parts 1 to 3): "Information Technology Security Techniques Non repudiation"
- ISO/IEC 27001: "Information technology Security techniques Information security management systems - Requirements"
- Directive 97/67/EC (EU Postal Services Directive)
- IETF RFC 3852: "Cryptographic Message Syntax (CMS)"
- ETSI TS 101 733: "CMS Advanced Electronic Signatures (CAdES)"
- ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)"
- W3C/IETF Recommendation: "XML-Signature Syntax and Processing"
- W3C Recommendation (SOAP) version 1.2
- IETF RFC 4510: "Lightweight Directory Access Protocol (LDAP)"
- ITU-R Recommendation TF.460-4: "Standard frequency and time-signal emissions"
- ETSI TS 101 861: "Time stamping profile"
- ETSI TS 102 231: "Provision of harmonized Trust-service status information"

## Definitions and Abbreviations
- **Registered E-Mail (REM)**: enhanced form of mail transmitted by electronic means (e-mail) which provides evidence relating to the handling of an e-mail including proof of submission and delivery.
- **AdES**: Advanced Electronic Signature
- **AFNOR**: Association Française de NORmalisation (French standards body)
- **CA**: Certification Authority
- **CAdES**: CMS Advanced Electronic Signatures
- **CEN**: Comité Européen de Normalisation
- **CMS**: Cryptographic Message Syntax
- **CNIPA**: Centro Nazionale per l'Informatica nella Pubblica Amministrazione (Italian governmental body for REM)
- **EPCM**: Electronic Postal Certification Mark
- **HTTPS**: Hypertext Transfer Protocol over SSL or TLS
- **LDAP**: Lightweight Directory Access Protocol
- **PEC**: Posta Elettronica Certificata (Italian REM)
- **PKI**: Public Key Infrastructure
- **QES**: Qualified Electronic Signature
- **TLS**: Transport Layer Security
- **TST**: Time-Stamp Token
- **UPU**: Universal Postal Union
- **XAdES**: XML Advanced Electronic Signature
- **XML**: eXtensible Markup Language

## 5 Market

### 5.1 Specific Conclusions on Market
- Significant interest across Europe: at least 10 European nations have services existing or planned, with an existing user community of >500,000 and potential community of 100 million.
- 14 respondents reported REM services already in operation; 3 more being deployed; 5 planned. 7 products already deployed.
- Business areas include public administration, banking, insurance, postal services, e-procurement.

## 6 Regulations and Legal Validity

### 6.3 Specific Conclusions on Regulation and Legal Validity
- Three classes of legal basis: specific REM legislation (Italy, France, Belgium); public administration notarizations (Spain, Sweden); general electronic signature/contractual legislation (others).
- **Evidential services should be provided by a third party independent from other actors or with public notarization functions.** Time-stamping services should be provided by a trusted independent third party.
- Internal control policies must be implemented by all entities producing evidence.

## 7 Services

### 7.5 Specific Conclusions on Services
- Core evidence services (almost universally required): evidence of message origin authentication, submission, delivery, and non-delivery.
- Other services (e.g., evidence of exchange between providers, notification of availability, message opened/viewed) are commonly supported.
- Support for external connections to physical post or non-REM e-mail is limited but should be considered in future standardization.
- Archival services and maintenance of signatures over long term are important; recommendation to use XAdES/CAdES.

## 8 REM System Overviews

### 8.3.1 REM Relevant Entities (Generic Model)
- **Sender**, **Recipient**, **REM Transport Provider** (may be one or multiple), **Evidence Provider** (may be separate or merged), **Evidence Verifier**, **Intermediary**, **Optional Mail Service Providers** (traditional e-mail, physical mail), **Security Service Providers**.
- Evidence flow: evidence is generally signed (AdES or QES) and time-stamped.

### 8.3.2–8.3.5 Specific Model Adaptations
- **AFNOR model**: independent evidence provider; no sender/recipient registration required.
- **Italian (CNIPA) model**: REM providers also serve as evidence providers; full legal validity per law; use of CNIPA-issued certificates.
- **UPU ECPM model**: evidence issuance, storage, verification by Postal Administrations; cross-border interoperability not yet addressed.
- **Critical Path model**: centralized mail repository; senders registered; recipients can be unregistered; evidence signed by REM provider.

## 9 Services within REM

### 9.1.4 Specific Conclusions on Availability of Evidence
- Core evidence services (submission, delivery, non-delivery, error notifications) are almost always provided automatically.
- Complementary services (transmission, acceptance, opening) are provided in ~2/3 of cases, either automatically or on request.
- Evidence is typically carried as XML attachments, S/MIME p7s, or other formats.

### 9.2.3 Specific Conclusions on Message Identification
- Unique message identifier allocated by sender or sender's REM provider is nearly universally required.
- Message identifier is the preferred referencing mechanism in notifications.

### 9.3.1 Specific Conclusions on E-mail Clients
- Widespread use of multiple client types (Outlook, webmail, etc.). Standardization could facilitate integration.

### 9.4.1 Specific Conclusions on External Interfaces
- ~1/3 of respondents provide interface to non-REM e-mail; fewer to physical post.

### 9.5.1 Specific Conclusions on Use of Independent Services
- Outsourcing is common; time-stamping is the most outsourced service.

## 10 Security Features

### 10.1.1 Specific Conclusions on Authentication of Parties
- Authentication of sender to provider and recipient to provider is common (2/3 of cases), using cryptographic devices or secured password.
- Authentication between REM providers is rare.

### 10.2.1 Specific Conclusions on Authentication of Evidence
- When evidence is provided, it is almost always supported by an advanced or qualified electronic signature (AdES/QES) AND a time-mark or time-stamp.
- No significant preference between AdES and QES, or between time-mark and time-stamp.

### 10.3.1 Specific Conclusions on Signature Formats
- S/MIME and CMS are prevalent, but XMLDSig, CAdES, XAdES are also used. REM solutions should support multiple signature formats.

### 10.4.1 Specific Conclusions on Time-stamping and Time-marking
- RFC 3161 timestamps are most common; other formats (e.g., XML) exist. Solutions should accommodate multiple time-stamp formats.
- Time-marking is used by some systems.
- Preferred synchronization: UTC per ITU-R TF.460-4.

### 10.5.1 Specific Conclusions on Security Protocols
- SSL/TLS is dominant; other protocols (SOAP/WSS, etc.) should not be excluded.

### 10.6.1 Specific Conclusions on Supporting Services
- Common: LDAP, X.509 CA, CRLs, OCSP, digital signing servers. Trust model is hierarchical.

## 11 Policies and Practices

### 11.1.1 Specific Conclusions on Registration
- Sender registration often required; recipient registration can be optional.
- Registration may involve face-to-face or remote authentication.

### 11.2.1 Specific Conclusions on Security Management
- Most systems operate under defined security policies; about half use ISO/IEC 27001-based ISMS.

### 11.3.1.1 Security of Signing Device
- HSMs, smart cards, and software keys are used. Certification to FIPS 140-2 (levels 1–4) or Common Criteria (EAL4+) is common.

## 12 Related Standards Activities

### 12.4 Specific Conclusions on Related Standards Activities
- AFNOR Z 74-600 defines evidence structure and security policy for REM.
- UPU EPCM standards (S43-3, CEN TS 15130) are relevant but currently limited to national postal implementations and do not fully cover open REM interoperability.

## 13 Conclusions and Recommendations

### 13.1 General Conclusions
1. Significant existing deployment and large potential market.
2. Three classes of legislation: specific, public notarization, general.
3. Evidence services must be provided by independent parties with trusted controls.
4. Core evidence: origin authentication, submission, delivery, non-delivery.
5. Support for evidence at all message handling stages may be required.
6. Confidentiality, anti-virus, anti-spam are important adjuncts.
7. Limited external connections currently, but implications for future standardization.
8. Broad range of architectures; a generic architecture is needed.
9. XML encoding of evidence is common but not exclusive.
10. Unique message identifier should be allocated by sender or sender's REM provider.
11. Various email clients are used; outsourcing is common.
12. Authentication often via password over SSL/TLS or cryptographic device.
13. Evidence signed with AdES/QES plus time-mark/stamp.
14. Both XMLDSig and CMS signatures are used.
15. Evidence often provided automatically.
16. Timestamps mostly RFC 3161, synchronized to UTC.
17. ISO/IEC 27001-based ISMS in several systems.
18. Diverse signing devices with certification.
19. EPCM standards exist but are not fully applicable to open REM.

### 13.2 Recommendations Regarding Work Plan for Next Phase
- **Purpose**: Establish standards for signed evidence in support of REM.
- **Motivation**: Ensure consistency, interoperability, and user portability.
- **Impact of non-standardization**: Inconsistency, vendor lock-in, lack of interoperability.
- **Proposed Deliverables**:
  1. **Architecture for signed evidence in REM**: includes architectural elements, examples, use of digital signatures, time-stamping, data requirements, message flows, interconnection, web/email interfaces.
  2. **Data requirements and formats for signed evidence**: definition of functional content, syntaxes (XML, ASN.1, PDF).
  3. **Policy requirements for trust service providers supporting REM**: obligations of parties, ISO/IEC 27001-based requirements, internal controls, audit requirements.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Evidence should be provided by a third party independent of the other actors. | should | Clause 6.3, 13.1(3) |
| R2 | Time-stamping services should be provided by a trusted independent third party. | should | Clause 6.3 |
| R3 | Evidence services should include at minimum: message origin authentication, submission, delivery, non-delivery. | should | Clause 7.5, 13.1(4) |
| R4 | A unique message identifier must be allocated by the sender or sender's REM provider. | should (consensus) | Clause 9.2.3 |
| R5 | Evidence should be supported by an advanced or qualified electronic signature and a time-mark or time-stamp. | should | Clause 10.2.1 |
| R6 | Systems should operate under a defined security policy, preferably based on ISO/IEC 27001. | should | Clause 11.2.1, 13.2 |
| R7 | Future standardization shall address architecture, data formats, and policy requirements for REM. | shall (by ETSI) | Clause 13.2 |

## Informative Annexes (Condensed)
- **Annex A – Main Approaches**: Summarizes de jure/de facto standards and implementations. Key standards: AFNOR Z 74-600 (independent evidence provider, no registration required), Italian PEC (legal validity per law, CNIPA accreditation), UPU EPCM (Postal Administration-based evidence). Key implementations include Austrian delivery, French hybrid, Spanish UPM-ACEPTA, MAP/FNMT, Bankinter, CCN, Swiss IncaMail, Norwegian eNotarius, worldwide PxMail and Critical Path.
- **Annex B – Survey Questionnaire**: The full questionnaire used for data collection, covering organizational info, implementation status, services, regulations, service provision model, technical details, security policies.
- **Annex C – Acknowledgements**: List of 39 contributing organizations.