# ETSI TS 101 456: Policy requirements for certification authorities issuing qualified certificates
**Source**: ETSI | **Version**: V1.4.3 | **Date**: 2007-05 | **Type**: Normative
**Original**: ETSI TS 101 456 V1.4.3 (2007-05)

## Scope (Summary)
This Technical Specification specifies policy requirements for Certification Authorities (CAs) issuing qualified certificates (as defined in Directive 1999/93/EC). It defines two qualified certificate policies (QCP public + SSCD and QCP public) and a framework for other qualified certificate policies. Requirements cover CA operation, management practices, and services including registration, certificate generation, dissemination, revocation management, and optionally subject device provision.

## Normative References
- [1] Directive 1999/93/EC of the European Parliament and of the Council on a Community framework for electronic signatures.
- [2] IETF RFC 3647 (2003): "Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework".
- [3] ITU-T Recommendation X.509 (2000)/ISO/IEC 9594-8 (2001): "Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks".
- [4] Directive 95/46/EC of the European Parliament and of the Council on the protection of individuals with regard to the processing of personal data.
- [5] FIPS PUB 140-2 (2001): "Security Requirements For Cryptographic Modules".
- [6] ETSI TS 101 862: "Qualified certificate profile".
- [7] ISO/IEC 15408 (2005) (parts 1 to 3): "Information technology - Security techniques - Evaluation criteria for IT security".
- [8] CEN Workshop Agreement 14167-1: "Security Requirements for Trustworthy Systems Managing Certificates for Electronic Signatures - Part 1: System Security Requirements".
- [9] CEN Workshop Agreement 14167-2: "Cryptographic Module for CSP signing operations with backup – Protection profile (CMCSOB-PP)".
- [10] CEN Workshop Agreement 14167-3: "Cryptographic module for CSP key generation services – Protection profile (CMCKG-PP)".
- [11] CEN Workshop Agreement 14167-4: "Cryptographic module for CSP signing operations – Protection profile (CMCSO PP)".
- [12] Council Directive 93/13/EEC on unfair terms in consumer contracts.
- [13] ISO/IEC 17799 (2005): "Information technology - Security techniques - Code of practice for information security management".
- [14] ETSI TS 102 158: "Policy requirements for Certification Service Providers issuing attribute certificates usable with Qualified certificates".

## Definitions and Abbreviations
- **advanced electronic signature**: electronic signature uniquely linked to the signatory, capable of identifying the signatory, created using means under sole control, and linked to data so any subsequent change is detectable (Directive 1999/93/EC [1]).
- **attribute**: information bound to an entity specifying a characteristic.
- **certificate**: public key of a user, together with other information, rendered unforgeable by encipherment with the private key of the certification authority which issued it (see ITU-T X.509 [3]).
- **certification authority (CA)**: authority trusted by one or more users to create and assign certificates (see ITU-T X.509 [3]).
- **certificate policy (CP)**: named set of rules indicating the applicability of a certificate to a particular community and/or class of application with common security requirements (see ITU-T X.509 [3]).
- **certification practice statement (CPS)**: statement of the practices which a CA employs in issuing, managing, revoking, and renewing or re-keying certificates (see RFC 3647 [2]).
- **Certificate Revocation List (CRL)**: signed list indicating a set of certificates no longer considered valid (see ITU-T X.509 [3]).
- **Certification-Service-Provider (CSP)**: entity or legal/natural person who issues certificates or provides other services related to electronic signatures (see Directive 1999/93/EC [1]).
- **electronic signature**: data in electronic form attached to or logically associated with other electronic data which serve as a method of authentication (see Directive 1999/93/EC [1]).
- **qualified certificate**: certificate meeting requirements of Annex I of Directive 1999/93/EC [1] and provided by a CSP fulfilling Annex II requirements.
- **Qualified Certificate Policy (QCP)**: certificate policy incorporating requirements of Annex I and II of Directive 1999/93/EC [1].
- **qualified electronic signature**: advanced electronic signature based on a qualified certificate and created by a secure-signature-creation device (article 5.1 of Directive 1999/93/EC [1]).
- **relying party**: recipient of a certificate who acts in reliance on that certificate and/or digital signatures verified using that certificate (see RFC 3647 [2]).
- **signature-creation data**: unique data (e.g., private keys) used to create an electronic signature (see Directive 1999/93/EC [1]).
- **signature-creation device**: configured software or hardware used to implement the signature-creation data (see Directive 1999/93/EC [1]).
- **secure-signature-creation device (SSCD)**: signature-creation device meeting requirements of Annex III of Directive 1999/93/EC [1].
- **signature-verification data**: data (e.g., public keys) used for verifying an electronic signature (see Directive 1999/93/EC [1]).
- **subject**: entity identified in a certificate as the holder of the private key associated with the public key given in the certificate.
- **subscriber**: entity subscribing with a CA on behalf of one or more subjects.
- **Abbreviations**: CA, CPS, CRL, CSP, PDS, PKI, QCP, RSA, SSCD.

## 4 General concepts
### 4.1 Certification authority
- CA is trusted to create and assign certificates, has overall responsibility for certification services (clause 4.2), identified as issuer in certificate. CA may subcontract parts but maintains overall responsibility and liability (see Directive [1]).

### 4.2 Certification services
Services: Registration, Certificate generation, Dissemination, Revocation management, Revocation status, and optionally Subject device provision. Subdivision for clarification only.

### 4.3 Certificate policy and certification practice statement
- CP states "what is to be adhered to", CPS states "how it is adhered to". The document specifies CPs for qualified certificates. If policy changes affecting applicability, identifier should be changed.
- CP is less specific than CPS. CPS details how CA meets CP requirements.
- CP is defined independently of operating environment; CPS is tailored.
- CA may issue terms and conditions, including PKI Disclosure Statement (PDS).

### 4.4 Subscriber and subject
- Subscriber contracts with CA; subject is individual authenticated by private key. They may be same entity.

## 5 Introduction to qualified certificate policies
### 5.1 Overview
- Two QCPs: QCP public + SSCD and QCP public. Clauses 6 and 7 apply to both unless indicated.
- Clause 8 provides framework for other QCPs.

### 5.2 Identification
- QCP public + SSCD OID: itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(1456) policy-identifiers(1) qcp-public-with-sscd (1)
- QCP public OID: itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(1456) policy-identifiers(1) qcp-public (2)
- CA shall include policy identifier in certificate and in terms and conditions.

### 5.3 User Community and applicability
#### 5.3.1 QCP public + SSCD
- For certificates: meeting Annex I, issued by CA fulfilling Annex II, for use only with SSCDs meeting Annex III, issued to public. May support qualified electronic signatures under article 5.1.

#### 5.3.2 QCP public
- For certificates: meeting Annex I, issued by CA fulfilling Annex II, issued to public. May support electronic signatures under article 5.2.

### 5.4 Conformance
#### 5.4.1 General
- CA shall only use policy identifier if claiming conformance and making evidence available; or has current assessment by competent independent party; shall cease use if non-conformant significantly affects ability to meet requirements until remedied; compliance checked regularly and after major changes.

#### 5.4.2 QCP public + SSCD
- CA must demonstrate: meets obligations in clause 6.1; implements controls meeting clause 7.

#### 5.4.3 QCP public
- CA must demonstrate: meets clause 6.1; implements clause 7 excluding 7.2.9 and 6.2(e) and (f).

## 6 Obligations and liability
### 6.1 Certification authority obligations
- CA shall implement all applicable requirements per selected policy (see 5.4.2, 5.4.3, 8.4). Responsible for conformance even if subcontracted. Shall provide services consistent with CPS.

### 6.2 Subscriber obligations
- CA shall oblige subscriber through agreement (see 7.3.1(i)) to: submit accurate info; use key only for signatures; avoid unauthorized use; generate keys using recognized algorithms and key lengths if self-generated; maintain private key under subject's sole control; (QCP public + SSCD only) use only with SSCD and generate keys within SSCD; notify CA of loss/compromise/changes; discontinue use of compromised key; not use certificate if CA compromised.

### 6.3 Information for relying parties
- Terms and conditions shall include notice to verify validity/suspension/revocation using current status info; take account of limitations; take other precautions.

### 6.4 Liability
- CAs issuing qualified certificates to public are liable as per article 6 of Directive [1].

## 7 Requirements on CA practice
- CA shall implement controls meeting requirements. Applicable to both QCPs except where indicated.

### 7.1 Certification Practice Statement (CPS)
- CA shall demonstrate reliability (Annex II(a)). CPS shall identify obligations of external organizations; make CPS available; disclose terms and conditions; have high-level management approval; ensure proper implementation; define review process; give due notice of changes; document signature algorithms.

### 7.2 Public key infrastructure - Key management life cycle
#### 7.2.1 Certification authority key generation
- CA keys generated in controlled circumstances: physically secure environment, dual control, minimal personnel. Device must meet FIPS 140-2 level 3 or higher, or CWA 14167-2/3/4, or be trustworthy system assured to EAL 4+ per ISO/IEC 15408. Algorithm and key length recognized as fit. New key generated before expiration.

#### 7.2.2 Certification authority key storage, backup and recovery
- CA private key held and used in secure cryptographic device (as per 7.2.1(b)). Backed up with dual control, same or greater security.

#### 7.2.3 Certification authority public key distribution
- Integrity and authenticity maintained during distribution. Public keys made available in manner assuring integrity and authentic origin.

#### 7.2.4 Key escrow
- Subject private signing keys shall not be held in escrow (Annex II(j)).

#### 7.2.5 Certification authority key usage
- CA signing keys may be used for other certificates and revocation info as long as requirements not violated. Used only within physically secure premises.

#### 7.2.6 End of CA key life cycle
- All copies of CA private keys destroyed or put beyond use.

#### 7.2.7 Life cycle management of cryptographic hardware used to sign certificates
- Hardware not tampered during shipment/storage; installation/backup/recovery require dual control; hardware functioning correctly; keys destroyed upon device retirement.

#### 7.2.8 CA provided subject key management services
- If CA generates subject keys: use recognized algorithm and key length; generate and store securely; deliver with secrecy and integrity; delete all copies after delivery.

#### 7.2.9 Secure-signature-creation device preparation
- Not applicable to QCP public. If CA issues SSCD: preparation securely controlled; device securely stored and distributed; deactivation/reactivation controlled; activation data prepared/distributed separately from device.

### 7.3 Public key infrastructure - Certificate Management life cycle
#### 7.3.1 Subject registration
- CA shall inform subscriber of terms before agreement (Annex II(k)). Verify identity and attributes by appropriate means in national law. Record all info used. Subscriber must provide contact address. Signed agreement recorded including obligations, consent to record, certificate publication consent. Records retained for period as indicated.

#### 7.3.2 Certificate renewal, rekey and update
- Check existence and validity of old certificate; if new terms, communicate and agree; if changed attributes or revocation, re-verify. Issue new certificate only if cryptographic security still sufficient and no indication of compromise.

#### 7.3.3 Certificate generation
- Certificates shall contain all elements of Annex I of Directive. Take measures against forgery; securely link issuance to registration; ensure uniqueness of distinguished name within CA domain; protect confidentiality and integrity of registration data; verify identity of external registration service providers.

#### 7.3.4 Dissemination of Terms and Conditions
- CA shall make terms and conditions available to subscribers and relying parties, including: policy being applied, limitations, subscriber obligations, validation requirements, liability limitations, record retention periods, dispute procedures, applicable legal system, and conformance information. Information shall be durable and understandable.

#### 7.3.5 Certificate dissemination
- Upon generation, certificate available to subscriber/subject. Certificates available for retrieval only with subject consent. Terms available 24/7; best efforts to minimize downtime.

#### 7.3.6 Certificate revocation and suspension
- Document procedures in CPS. Process revocation requests timely. Authenticate requests. Status may be suspended while confirming; not kept suspended longer than necessary. Inform subject of status change. Once revoked, not reinstated. CRLs published at least daily, signed, with next update time. Revocation management and status info available 24/7. Integrity and authenticity protected. Status info publicly available.

### 7.4 CA management and operation
#### 7.4.1 Security management
- Carry out risk assessment; retain responsibility for outsourced functions; management provide direction on information security; maintain quality/security management system; document security controls and procedures.

#### 7.4.2 Asset classification and management
- Maintain inventory of information assets; assign classification consistent with risk analysis.

#### 7.4.3 Personnel security
- Employ sufficient qualified personnel; apply disciplinary sanctions; document security roles; trusted roles include Security Officers, System Administrators, System Operators, System Auditors. Personnel appointed formally; not appoint person with serious crime conviction. Free from conflicting interests.

#### 7.4.4 Physical and environmental security
- Limit physical access to critical services; controls to avoid loss/damage/compromise; operate in physically secure environment; clearly defined security perimeters; address access control, natural disaster, fire, utilities, etc.

#### 7.4.5 Operations management
- Protect integrity against viruses; minimize damage via incident response; secure media handling; procedures for all roles; capacity monitoring; timely incident reporting; audit logs at startup; monitor logs; separate CA security operations.

#### 7.4.6 System Access Management
- Protect internal network with controls (e.g., firewalls); protect sensitive data on networks; manage user accounts; restrict access per role; identify and authenticate personnel; accountability via logging; protect against reuse of storage objects; continuous monitoring and alarm facilities.

#### 7.4.7 Trustworthy Systems Deployment and Maintenance
- Carry out security analysis at design stage; change control procedures for software.

#### 7.4.8 Business continuity management and incident handling
- Define and maintain continuity plan; back up CA data; perform backup/restore by trusted roles; address CA private key compromise as disaster; in case of compromise, inform all affected parties; if algorithm compromise, inform and revoke affected certificates.

#### 7.4.9 CA termination
- Inform subscribers and relying parties; terminate subcontractor authorizations; transfer obligations for maintaining records; destroy or withdraw CA private keys. Arrange for costs if bankrupt. State provisions in practices.

#### 7.4.10 Compliance with Legal Requirements
- Meet statutory requirements; comply with Data Protection Directive (95/46/EC); take measures against unauthorized processing; protect information from disclosure without agreement or legal authorization.

#### 7.4.11 Recording of Information Concerning Qualified Certificates
- Maintain confidentiality and integrity of records; archive completely and confidentially; make available for legal proceedings; record precise time of events; hold records for appropriate period; log all events relating to registration, key life-cycle, certificate life-cycle, subject device provision, revocation.

### 7.5 Organizational
- CA organization reliable: non-discriminatory policies; accessible services; legal entity; adequate arrangements for liability; financial stability; complaint resolution procedures; contractual agreements for subcontracting; parts concerned with certificate generation and revocation management independent; documented structure safeguarding impartiality.

## 8 Framework for the definition of other qualified certificate policies
- Not applicable to QCP public or QCP public + SSCD.

### 8.1 Qualified certificate policy management
- Policy shall identify basis policy and variances; body with authority for policy; risk assessment; approval and modification process; policy supported by CPS; make policy available; revisions available; policy shall incorporate requirements of clauses 6 and 7 with exclusions; unique OID.

### 8.2 Exclusions for non public QCPs
- Not required to apply: liability as defined in clause 6.3; independence of providers (7.5(h),(i)); public dissemination (7.3.5(f)); public revocation status (7.3.6(k)).

### 8.3 Additional requirements
- Inform subscribers/relying parties if not public and exclusions apply; whether SSCD required; how policy adds/constrains requirements.

### 8.4 Conformance
- Similar conformance provisions as clause 5.4.1. Must demonstrate meeting clause 6.1; controls meeting clause 7 (excluding 7.2.9 if no SSCD, and exclusions per 8.2 if not public); policy meets clause 8.1; additional requirements.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CA shall implement all requirements applicable to selected QCP. | shall | 6.1 |
| R2 | CA shall make CPS available to subscribers and relying parties. | shall | 7.1(c) |
| R3 | CA signing keys shall be generated in physically secure environment under dual control. | shall | 7.2.1(a) |
| R4 | CA private key shall be held and used in secure cryptographic device meeting FIPS 140-2 level 3 or higher, or equivalent. | shall | 7.2.2(a) |
| R5 | Subject private signing keys shall not be escrowed. | shall | 7.2.4 |
| R6 | Certificates shall contain all elements of Annex I of Directive [1]. | shall | 7.3.3(a) |
| R7 | Revocation status information shall be available 24/7; maximum delay of 1 day. | shall | 7.3.6(g), (h) |
| R8 | CA shall carry out risk assessment and regularly review. | shall | 7.4.1(a) |
| R9 | CA shall comply with Data Protection Directive. | shall | 7.4.10(b) |
| R10 | CA shall log all events relating to key and certificate life-cycle. | shall | 7.4.11(k), (l) |

## Informative Annexes (Condensed)
- **Annex A (Potential liability)**: Provides conceptual framework on liability of CAs (based on article 6 of Directive) and subscribers. Discusses negligence, reliance, limitations, and liability under national law.
- **Annex B (Model PKI disclosure statement)**: Proposes a model PDS to assist CAs in meeting disclosure requirements (clause 7.3.4). Includes table mapping statement types to specific requirements.
- **Annex C (Directive cross-reference)**: Table mapping Annex II requirements of Directive to corresponding clauses in the present document.
- **Annex D (IETF RFC 3647/RFC 2527 cross-reference)**: Two tables showing relationships between RFC 3647/RFC 2527 sections and policy references in the present document.
- **Annex E (Revisions since version 1.2.1 and 1.3.1)**: Lists additional, updated, clarified, and editorial changes made in this version.
- **Annex F (Bibliography)**: Lists additional reference documents (TTP.NL parts, ITU-T, ISO/IEC, ANSI, CEN, Directive 97/7/EC, NIST SP 800-78, ETSI TS 102 176-1).