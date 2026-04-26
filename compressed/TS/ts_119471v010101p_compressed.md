# ETSI TS 119 471 V1.1.1: Policy and Security requirements for Providers of Electronic Attestation of Attributes Services
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2025-05 | **Type**: Normative (Technical Specification)
**Original**: https://www.etsi.org/deliver/etsi_ts/119400_119499/119471/01.01.01_60/ts_119471v010101p.pdf

## Scope (Summary)
This document specifies policy and security requirements for Electronic Attestation of Attributes (EAA) trust service providers (EAASPs) and their services, covering issuance and validation of EAA.

## Normative References
- [1] ETSI EN 319 401: "Electronic Signatures and Trust Infrastructures (ESI); General Policy Requirements for Trust Service Providers"

## Definitions and Abbreviations
(Selected key terms; see original for full list)
- **attribute**: characteristic, quality, right or permission of a natural or legal person or of an object (eIDAS [i.1])
- **attestation of attributes validation**: process of verifying and confirming that an attestation of attributes is valid
- **authentic source**: repository or system, under public or private responsibility, that contains and provides attributes considered as a primary source or recognised as authentic (eIDAS [i.1])
- **Electronic Attestation of Attributes (EAA)**: attestation in electronic form that allows the authentication of attributes (eIDAS [i.1])
- **electronic attestation of attributes policy (EAAP)**: set of rules indicating applicability of an EAA to a particular community/class with common requirements
- **electronic attestation of attributes practice statement (EAASPS)**: statement of practices employed by an EAASP in providing a trust service (per EN 319 401 [1])
- **electronic attestation of attributes service policy (EAASPol)**: set of rules for EAA service with common controls and security requirements
- **Electronic Attestation of Attributes Service Provider (EAASP)**: natural or legal person providing EAA services (qualified or non-qualified)
- **Qualified Electronic Attestation of Attributes (QEAA)**: EAA issued by a qualified TSP meeting Annex V of eIDAS [i.1]
- **Wallet Unit**: specific setup of the wallet solution for an individual user (per CIR (EU) 2024/2977 Article 2.2 [i.3])
- **Abbreviations**: EAA, EAAP, EAAS, EAASP, EAASPol, EUDIW, PID, QEAA, QEAASP, WSCD, WUA, etc. (see original clause 3.3)

**Notation**:
- REQ-EAASP-<clause>-<num>: non‑qualified provider
- REQ-QEAASP-<clause>-<num>: qualified provider
- REQ-EAAS-<clause>-<num>: service

## 4 EAA Trust Services

### 4.1 Overview
An EAASP is a trusted third‑party that issues and/or validates attributes, vouching for accuracy, validity, and timeliness against authentic/other sources.

### 4.2 EAA Issuance Services

#### 4.2.1 Initiation

##### 4.2.1.1 General
- **REQ-EAASP-4.2.1.1-01**: When issuing an EAA, the EAASP **shall** verify identity and specific attributes of the EAA Subject and/or EAA Subscriber per EAASPol.
- **REQ-EAASP-4.2.1.1-02**: EAASP **shall** verify request contains all necessary info: (a) subject = subscriber; (b) if different, additional verification; (c) attribute‑subject correspondence.
- **REQ-EAASP-4.2.1.1-03 [CONDITIONAL]**: If subject ≠ subscriber, EAASP **shall** obtain evidence of right to act on behalf.
- **REQ-EAASP-4.2.1.1-04 [CONDITIONAL]**: If validation against authentic source, EAASP **shall** verify identity of that source.
- **REQ-EAASP-4.2.1.1-05 [CONDITIONAL]**: When attributes listed in Annex VI require authentic source consultation and secure access system exists, EAASP **should** verify authenticity by at least electronic means.

##### 4.2.1.2 EUDIW Specific
- **REQ-EAASP-4.2.1.2-01 [CONDITIONAL]**: If supporting OpenID4VCI, EAASP **should** support attestation issuance interface compliant with OpenID4VCI or equivalent.
- **REQ-EAASP-4.2.1.2-02**: EAASP **shall** implement mechanisms to authenticate Wallet Units before issuing EAA.
- **REQ-EAASP-4.2.1.2-03**: EAASP **shall** validate that the WSCD of the Wallet Unit complies with required security level.

#### 4.2.2 EAA Issuance

##### 4.2.2.1 General
- **REQ-EAASP-4.2.2.1-01**: EAASP **shall** request only minimum data necessary (data minimization).
- **REQ-EAASP-4.2.2.1-02**: EAASP **shall** ensure minimum set of attributes acquired per EAAP.
- **REQ-EAASP-4.2.2.1-03**: EAASP **shall** verify attributes against one or more authentic/not authentic sources as stated in EAAP.
- **REQ-EAASP-4.2.2.1-04**: EAASP **shall** define attributes to be verified by content and nature of EAA per EAAP.
- **REQ-EAASP-4.2.2.1-05**: EAASP **shall not** verify identity attributes not necessary for issuance.
- **REQ-EAASP-4.2.2.1-06**: EAASP **shall** issue EAA securely to maintain authenticity and integrity.
- **REQ-EAASP-4.2.2.1-07**: EAASP **shall** take measures against forgery.
- **REQ-EAAS-4.2.2.1-08**: EAAS **shall** be able to authenticate itself to subject and issuance means.
- **REQ-EAASP-4.2.2.1-09**: EAASP **shall** issue EAA in conformance with claimed EAASPol and EAAP.
- **REQ-EAASP-4.2.2.1-10 [CONDITIONAL]**: If status service supported, EAAS policy **shall** indicate revocation information URL and identifier/index.

##### 4.2.2.2 Verification of attributes against authentic sources
- **REQ-QEAASP-4.2.2.2-01**: QEAASP **shall** verify authenticity of attributes against relevant authentic source at national level or via designated intermediaries.
- **REQ-QEAASP-4.2.2.2-02**: Verification **shall** be as required by EAAP.
- **REQ-QEAASP-4.2.2.2-03**: Verification **should** if possible be carried out electronically.

##### 4.2.2.3 EUDIW Specific
- **REQ-EAASP-4.2.2.3-01**: Before issuance to EUDIW, EAASP **shall** verify and validate PID/LPID from Wallet Unit.
- **REQ-EAASP-4.2.2.3-02**: EAASP **shall** authenticate to EUDIW using mutual authentication with access certificate issued by a qualified CA.
- **REQ-EAASP-4.2.2.3-03**: EAASP **shall** validate whether EUDIW instance is revoked or suspended.
- **REQ-EAASP-4.2.2.3-04 [CONDITIONAL]**: When wallet binding, EAASP **shall** verify WSCD has proven possession of private key and attestation private key.
- **REQ-EAASP-4.2.2.3-05 [CONDITIONAL]**: When binding includes association of two or more keys protected by same WSCD, EAASP **should** verify keys are associated.
- **REQ-EAASP-4.2.2.3-06 [CONDITIONAL]**: If wallet binding required by EAAP, EAASP **shall** implement device binding cryptographically.
- **REQ-EAASP-4.2.2.3-07**: EAASP **shall** verify WUA signature, accept only trust anchors in Wallet Provider Trusted List(s), verify EUDIW Provider is present, authenticate and validate WUA using registered trust anchors, verify WUA not revoked.
- **REQ-EAASP-4.2.2.3-08 [CONDITIONAL]**: When using OpenID4VCI or equivalent, EAASP **shall** include its access certificate in client metadata.
- **REQ-EAASP-4.2.2.3-09**: EAASP **shall** implement measures to mitigate user linkability, including limited‑validity or once‑only attestations as per policy.
- **REQ-EAASP-4.2.2.3-10**: EAASP **shall** support selective disclosure of attributes.
- **REQ-EAASP-4.2.2.3-11**: EAASP **shall** support at least one linkability‑mitigation mechanism: limited‑time, once‑only, rotating‑batch, or per‑Relying Party attestations.
- **REQ-EAASP-4.2.2.3-12 [CONDITIONAL]**: When applicable, EAASP **shall** implement device binding to prevent cloning.
- **REQ-EAASP-4.2.2.3-13**: EAASP **shall** support batch issuance when requested.
- **REQ-EAASP-4.2.2.3-14 [CONDITIONAL]**: EAASP **shall** ensure EAA compatible with proximity and remote presentation flows.
- **REQ-EAASP-4.2.2.3-15**: EAASP **may** include embedded disclosure policy in EAA.
- **REQ-EAASP-4.2.2.3-16**: EAASP **shall** implement mechanisms for re‑issuance upon Wallet Unit request.
- **REQ-EAASP-4.2.2.3-17**: Each EAA **shall** contain unique, cryptographically independent elements to prevent tracking.
- **REQ-EAASP-4.2.2.3-18**: Technical validity period **shall** consider security and privacy implications (user tracking risk).
- **REQ-EAASP-4.2.2.3-19**: Data element identifier and attribute value **should** be encoded per relevant rulebook (e.g., PID, mDL); ISO 23220-2 [i.2] where no rulebook exists.

#### 4.2.3 EAA Usage

##### 4.2.3.1 General
- **REQ-EAASP-4.2.3.1-01**: EAASP **shall** include in practice statement and terms at least: (a) obligation to provide accurate info; (b) limitations on use; (c) prohibition of unauthorized use.
- **REQ-EAASP-4.2.3.1-02 [CONDITIONAL]**: When subscriber acts on behalf of another, EAASP **shall** ensure subject has sole control unless national legislation or EAASPol states otherwise.

##### 4.2.3.2 EUDIW Specific
- **REQ-EAASP-4.2.3.2-01**: EAASP **shall** ensure EAAs can be presented in proximity flows (supervised/unsupervised) and remote flows (same‑device/cross‑device).

#### 4.2.4 EAA Renewal

##### 4.2.4.1 General
- **REQ-EAAS-4.2.4.1-01**: Renewal requests **shall** follow the EAAS practice statement process.
- **REQ-EAASP-4.2.4.1-02**: EAASP **shall** check validity of EAA to be renewed and that identity/attribute info is still valid.

##### 4.2.4.2 EUDIW Specific
- **REQ-EAASP-4.2.4.2-03 [CONDITIONAL]**: EAASP **shall** enable initiation by EUDIW Instance of secured session for re‑issuance.

#### 4.2.5 EAA Revocation

##### 4.2.5.1 General
- **REQ-EAASP-4.2.5.1-01**: EAASP **shall** follow its policies and practices when revoking.
- **REQ-EAASP-4.2.5.1-02**: EAASP **shall** revoke based on authorized/validated requests as soon as possible, max delay 24 hours after request.
- **REQ-EAASP-4.2.5.1-03**: Revocation process **shall** always be under EAASP's control.
- **REQ-EAASP-4.2.5.1-04**: EAASP issuing short‑term EAA **shall** describe explicitly in practice statement which EAAs cannot be revoked.
- **REQ-EAASP-4.2.5.1-05**: EAASP **shall** revoke any non‑expired EAA when: (a) error, fraud, or request; (b) non‑compliant with practice statement/policy; (c) changes impacting validity; (d) security incident.
- **REQ-EAASP-4.2.5.1-06**: EAASP **shall** inform subscriber/subject of revocation when possible.
- **REQ-EAAS-4.2.5.1-07**: Once revoked, EAA **shall not** be reinstated.
- **REQ-EAAS-4.2.5.1-08**: Revocation applies from that time to all instances.

##### 4.2.5.2 EUDIW Specific
- **REQ-EAASP-4.2.5.2-01**: EAASP **shall** implement at least one: status list (bit/group bits) or revocation list.
- **REQ-EAASP-4.2.5.2-02**: EAASP **shall** maintain and publish necessary info for verification (trust anchors, lists).
- **REQ-EAASP-4.2.5.2-03**: EAASP **shall** provide mechanism for Wallet Unit to check revocation status without contacting EAASP at presentation time.
- **REQ-EAASP-4.2.5.2-04 [CONDITIONAL]**: If Wallet Provider suspends/revokes Wallet Unit, EAASP **shall** immediately revoke respective EAAs.
- **REQ-EAASP-4.2.5.2-05**: When EAA valid longer than 24 hours, EAASP **shall** include URL and identifier/index for status.
- **REQ-EAASP-4.2.5.2-06**: For EAAs valid less than 24 hours, EAASP **may** omit revocation info if stated in practice statement.
- **REQ-EAASP-4.2.5.2-07 [CONDITIONAL]**: When batch issuance, revocation of one EAA results in revocation of all in that batch.

### 4.3 EAA Validation Services

#### 4.3.1 General
- **REQ-EAASP-4.3.1-01 [CONDITIONAL]**: If EAA‑policy requires status service, EAASP **shall** provide info/services for checking validity status.
  - **REQ-EAASP-4.3.1-02**: Revocation info **shall** be available 24/7; upon failure, best endeavours to limit unavailability as per practice statement.
  - **REQ-EAASP-4.3.1-03**: EAASP **shall** ensure integrity and authenticity of status info.
  - **REQ-EAASP-4.3.1-04**: Status info **shall** cover at least until EAA expiry.
  - **REQ-EAASP-4.3.1-05**: EAASP **shall** make status info publicly and internationally available.
- **REQ-QEAASP-4.3.1-06**: QEAASP **shall** have no information regarding usage of (Q)EAAs when status check performed.

#### 4.3.2 EUDIW Specific
- **REQ-EAASP-4.3.2-01**: EAASP **shall** publish trust anchors in a Trusted List accessible to Relying Parties.
- **REQ-EAASP-4.3.2-02**: EAASP **shall** support validation in proximity and remote flows.
- **REQ-EAASP-4.3.2-03**: EAASP **shall** support at least one attestation format: ISO/IEC 18013-5 [i.12] or SD-JWT VC.
- **REQ-EAASP-4.3.2-04**: EAASP **shall** provide mechanisms for Relying Parties to verify device binding.
- **REQ-EAASP-4.3.2-05**: EAASP **shall** support verification of combined presentations of attributes from multiple EAAs.
- **REQ-EAASP-4.3.2-06**: EAASP **shall** provide validation mechanisms that can verify WSCD signs at required LoA.

## 5 Risk Assessment
- **REQ-EAASP-5-01**: All requirements from ETSI EN 319 401 [1], clause 5 **shall** apply.

## 6 General Provision on Policies and Practices

### 6.1 EAAS Practice Statement

#### 6.1.1 General
- **REQ-EAASP-6.1.1-01**: All requirements from ETSI EN 319 401 [1], clause 6.1 **shall** apply.
  - **REQ-EAASP-6.1-02**: EAASP **should** document revocation mechanism in practice statement.

#### 6.1.2 EUDIW Specific
- **REQ-EAASP-6.1.2-01**: EAASP **shall** document in practice statement how it addresses Attestation Provider linkability risk.

### 6.2 Terms and Conditions
- **REQ-EAASP-6.2-01**: All requirements from ETSI EN 319 401 [1], clause 6.2 **shall** apply.
  - **REQ-EAASP-6.2-02**: Terms **shall** include elements from EN 319 401 REQ-6.2-02 and indication of service acceptance.
  - **REQ-EAASP-6.2.4-03**: EAASP **shall** record agreement with subscriber.
  - **REQ-EAASP-6.2.4-04**: Agreement **shall** involve explicit acceptance by a wilful act supportable by evidence.
  - **REQ-EAASP-6.2.4-05**: EAASP **shall** obtain prior consent from subscriber/subject, when possible, for personal data use/storage.
  - **REQ-EAASP-6.2.4-06**: Records **shall** be retained for period indicated in terms.

### 6.3 Information Security Policy
- **REQ-EAASP-6.3-01**: All requirements from ETSI EN 319 401 [1], clause 6.3 **shall** apply.

### 6.4 EAA Policy
(Informative description preserved: EAA policy defines rules for a specific community/class, may include attribute schema, verification mechanisms, data formats, proof mechanisms, etc. See original for details.)

## 7 EAASP Management and Operation

### 7.1 Internal Organization

#### 7.1.1 Organization Reliability
- **REQ-EAASP-7.1.1-01**: All requirements from ETSI EN 319 401 [1], clause 7.1.1 **shall** apply.
  - **REQ-EAASP-7.1.1-02**: Parts concerned with issuance and revocation **shall** be independent in decisions.
  - **REQ-EAASP-7.1.1-03**: Senior executive/staff in trusted roles **shall** be free from pressures influencing trust.
  - **REQ-EAASP-7.1.1-04**: Parts concerned **shall** have documented structure safeguarding impartiality.

#### 7.1.2 Segregation of Duties
- **REQ-EAASP-7.1.2-01**: All requirements from ETSI EN 319 401 [1], clause 7.1.2 **shall** apply.

### 7.2 Human Resources
- **REQ-EAASP-7.2-01**: All requirements from ETSI EN 319 401 [1], clause 7.2 **shall** apply.

### 7.3 Asset Management
- **REQ-EAASP-7.3-01**: All requirements from ETSI EN 319 401 [1], clause 7.3 **shall** apply.

### 7.4 Access Control
- **REQ-EAASP-7.4-01**: All requirements from ETSI EN 319 401 [1], clause 7.4 **shall** apply.
  - **REQ-EAASP-7.4-02**: Multi‑factor authentication **shall** be enforced for accounts capable of causing EAA issuance.
  - **REQ-EAASP-7.4-03**: Continuous monitoring and alarm facilities **shall** be provided.
  - **REQ-EAASP-7.4-04**: All authentication attempts/failures **shall** be monitored and logged.

### 7.5 Cryptographic Controls

#### 7.5.1 General
- **REQ-EAASP-7.5.1-01**: All requirements from ETSI EN 319 401 [1], clause 7.5 **shall** apply.

#### 7.5.2 Key Pair Generation and Installation
- **REQ-EAASP-7.5.2-01 [CONDITIONAL]**: If generating keys for signing, EAASP **shall** generate securely and keep private key secret.
  - **REQ-EAASP-7.5.2-02**: Generation in physically secured environment by personnel in trusted roles.
  - **REQ-EAASP-7.5.2-03**: Creation under at least dual control.
  - **REQ-EAASP-7.5.2-04**: Minimise number of authorised personnel.
  - **REQ-EAASP-7.5.2-05**: Use algorithm from ETSI TS 119 312 [i.10].
  - **REQ-EAASP-7.5.2-06**: Select key length/algorithm specified for EAA signing.
- **REQ-EAASP-7.5.2-07 [CONDITIONAL]**: Documented procedure for key generation.
- **REQ-EAASP-7.5.2-08 [CONDITIONAL]**: Report demonstrating ceremony followed procedure and ensured integrity/confidentiality.
- **REQ-EAASP-7.5.2-09 [CONDITIONAL]**: Report includes: roles, functions, responsibilities, evidence, date, inventory (unique ID, algorithm, size, fingerprint, device ID, settings).
- **REQ-EAASP-7.5.2-10 [CONDITIONAL]**: If keys from another TSP, ensure compliance with above and document.

#### 7.5.3 EAAS Key Protection and Cryptographic Module Engineering Controls
- **REQ-EAASP-7.5.3-01 [CONDITIONAL]**: Key pairs generated within secure cryptographic device functioning as trustworthy system.
  - **REQ-EAASP-7.5.3-02**: Either EAL4+ under ISO/IEC 15408-1 [i.6] or equivalent, or ISO/IEC 19790 [i.7] / FIPS 140-2 [i.8] Level 3 / FIPS 140-3 [i.9] Level 3.
  - **REQ-EAASP-7.5.3-03**: Operate device in certified configuration or equivalent.
  - **REQ-EAASP-7.5.3-04**: Store and use private signing key within compliant device.
  - **REQ-EAASP-7.5.3-05 [CONDITIONAL]**: If keys generated on QSCD from QTSP, verify compliance.
  - **REQ-EAASP-7.5.3-06 [CONDITIONAL]**: When private key outside device, protect to same level.
  - **REQ-EAASP-7.5.3-07 [CONDITIONAL]**: Backup/storage/recovery using dual control in physically secured environment.
  - **REQ-EAASP-7.5.3-08 [CONDITIONAL]**: Same or higher security for copies.
  - **REQ-EAASP-7.5.3-09 [CONDITIONAL]**: Access controls to keep keys inaccessible outside device.
  - **REQ-EAASP-7.5.3-10 [CONDITIONAL]**: Protect device against tampering during shipment/storage.
  - **REQ-EAASP-7.5.3-11 [CONDITIONAL]**: Destroy private signing keys when retiring device.

#### 7.5.4 Other Aspects of Key Pair Management
- **REQ-EAASP-7.5.4-01 [CONDITIONAL]**: Use private signing keys appropriately.
  - **REQ-EAASP-7.5.4-02**: Stop using keys at end of life cycle.
  - **REQ-EAASP-7.5.4-03**: Use only for EAA issuance and issuing revocation status info.
  - **REQ-EAASP-7.5.4-04**: Use only within physically secure premises.

#### 7.5.5 EUDIW Specific
- **REQ-EAASP-7.5.5-01**: Implement device binding cryptographically to WSCD.
- **REQ-EAASP-7.5.5-02**: Verify public key in EAA is associated with private key protected by WSCD.
- **REQ-EAASP-7.5.5-03**: Implement cryptographic protocols supporting selective disclosure.
- **REQ-EAASP-7.5.5-04**: Ensure mechanisms support verification of combined presentation from multiple EAAs belonging to same user.
- **REQ-EAASP-7.5.5-05**: Implement controls mitigating Relying Party and Attestation Provider linkability.
- **REQ-EAASP-7.5.5-06**: Maintain controls for access certificate and private keys security.
- **REQ-EAASP-7.5.5-07**: When batch issuance, support use of cryptographically independent EAAs.

### 7.6 Physical and Environmental Security
- **REQ-EAASP-7.6-01**: All requirements from ETSI EN 319 401 [1], clause 7.6 **shall** apply.

### 7.7 Operation Security
- **REQ-EAASP-7.7-01**: All requirements from ETSI EN 319 401 [1], clause 7.7 **shall** apply.
  - **REQ-EAASP-7.7-02**: Monitor capacity demands and future requirements to ensure adequate processing power and storage.

### 7.8 Network Security
- **REQ-EAASP-7.8-01**: All requirements from ETSI EN 319 401 [1], clause 7.8 **shall** apply.
  - **REQ-EAASP-7.8-02**: Maintain systems in at least a secure zone; implement security procedure protecting systems and communications.
  - **REQ-EAASP-7.8-03**: Remove/disable unused accounts, services, protocols, ports.
  - **REQ-EAASP-7.8-04**: Use secure encrypted channels for attribute data.

### 7.9 Vulnerabilities and Incident Management
- **REQ-EAASP-7.9-01**: All requirements from ETSI EN 319 401 [1], clause 7.9 **shall** apply.

### 7.10 Collection of Evidence for EAASP Internal Services
- **REQ-EAASP-7.10-01**: All requirements from ETSI EN 319 401 [1], clause 7.10 **shall** apply.
  - **REQ-EAASP-7.10-02**: Evidence of issuance process **shall** be collected and securely archived.
  - **REQ-EAASP-7.10-03**: All security events logged (policy changes, system start/stop, crashes, firewall/router activity, access attempts).
  - **REQ-EAASP-7.10-04**: Registration events including renewal requests logged.
  - **REQ-EAASP-7.10-05**: Document how recorded information is accessible.
  - **REQ-EAASP-7.10-06**: Log all EAA life‑cycle events.
  - **REQ-EAASP-7.10-07**: Log all revocation requests/reports and resulting action.
  - **REQ-EAASP-7.10-08**: Document retention period in practice statements and indicate handover through termination plan.

### 7.11 Business Continuity Management

#### 7.11.1 General
- **REQ-EAASP-7.11.1-01**: All requirements from ETSI EN 319 401 [1], clause 7.11 **shall** apply.

#### 7.11.2 Back Up
- **REQ-EAASP-7.11.2-01**: Systems data to resume operations **shall** be backed up and stored in safe (preferably remote) places.
- **REQ-EAASP-7.11.2-02**: Back‑up copies of essential info/software **should** be taken regularly.
- **REQ-EAASP-7.11.2-03**: Adequate facilities **should** be provided to recover after disaster/media failure.
- **REQ-EAASP-7.11.2-04**: Back‑up arrangements **should** be regularly tested.
- **REQ-EAASP-7.11.2-05**: Backup/restore functions **shall** be performed by relevant trusted roles.

#### 7.11.3 Crisis Management
- **REQ-EAASP-7.11.3-01**: After disaster, take steps to avoid repetition where practical.
- **REQ-EAASP-7.11.3-02**: Inform subscribers/subjects, relying parties, other TSPs of compromise.
- **REQ-EAASP-7.11.3-03**: Revoke any issued EAA when compromise is known.

### 7.12 EAASP and EAAS Termination and Termination Plans
- **REQ-EAASP-7.12-01**: All requirements from ETSI EN 319 401 [1], clause 7.12 **shall** apply.
  - **REQ-EAASP-7.12-02**: After EAA validity ceases, retain: (a) log of all EAA life‑cycle events; (b) attestation issuance evidence.
- **REQ-EAASP-7.12-03**: Retention period defined per national legislation.

### 7.13 Compliance
- **REQ-EAASP-7.13-01**: All requirements from ETSI EN 319 401 [1], clause 7.13 **shall** apply.
  - **REQ-EAASP-7.13-02**: Enable privacy‑preserving techniques for subject/subscriber data.
  - **REQ-EAASP-7.13-03**: Protect confidentiality/integrity of registration data.
  - **REQ-EAASP-7.13-04**: Implement data minimization in EAA Policy.
  - **REQ-EAASP-7.13-05**: Not track/link/correlate transactions post‑issuance unless authorized.
  - **REQ-EAASP-7.13-06**: Keep attributes/metadata logically separate from other data.
  - **REQ-EAASP-7.13-07**: Not export personal data to other services unless authorized.
  - **REQ-EAASP-7.13-08**: Systems designed to log minimal info sufficient for security/audit but not user tracking.

### 7.14 Supply Chain
- **REQ-EAASP-7.14-01**: All requirements from ETSI EN 319 401 [1], clause 7.14 **shall** apply.

## Requirements Summary
(Selected key requirements; full list in original with IDs)

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Verify identity and attributes of EAA Subject/Subscriber per EAASPol | shall | REQ-EAASP-4.2.1.1-01 |
| R2 | Request only minimum data necessary | shall | REQ-EAASP-4.2.2.1-01 |
| R3 | Verify attributes against authentic sources as per EAAP for qualified providers | shall | REQ-QEAASP-4.2.2.2-01 |
| R4 | Implement mechanisms to authenticate Wallet Units | shall | REQ-EAASP-4.2.1.2-02 |
| R5 | Support selective disclosure | shall | REQ-EAASP-4.2.2.3-10 |
| R6 | At least one linkability mitigation mechanism | shall | REQ-EAASP-4.2.2.3-11 |
| R7 | Device binding (if required by EAAP) | shall | REQ-EAASP-4.2.2.3-06 |
| R8 | Revoke within 24 hours of valid request | shall | REQ-EAASP-4.2.5.1-02 |
| R9 | Revoke non‑expired EAA under conditions | shall | REQ-EAASP-4.2.5.1-05 |
| R10 | Provide status info 24/7 | shall | REQ-EAASP-4.3.1-02 |
| R11 | Multi‑factor authentication for issuance accounts | shall | REQ-EAASP-7.4-02 |
| R12 | Generate key pair under dual control | shall | REQ-EAASP-7.5.2-03 |
| R13 | Use secure cryptographic device meeting EAL4+ or equivalent | shall | REQ-EAASP-7.5.3-01/-02 |
| R14 | Log all EAA life‑cycle events | shall | REQ-EAASP-7.10-06 |
| R15 | Privacy‑preserving techniques | shall | REQ-EAASP-7.13-02 |
| ... | (Additional requirements as per full text) | | |

## Informative Annexes (Condensed)
- **Informative References (clause 2.2)**: Documents useful for implementation, including eIDAS Regulation [i.1], ISO/IEC TS 23220-2 [i.2], CIR (EU) 2024/2977 [i.3], OpenID4VCI [i.4], EU ARF [i.5], security evaluation frameworks (ISO/IEC 15408-1 [i.6], ISO/IEC 19790 [i.7], FIPS 140-2/3 [i.8][i.9]), ETSI TS 119 312 [i.10], EN 319 411-1 [i.11], ISO/IEC 18013-5 [i.12]. Purpose: to aid understanding and implementation, not normative.
```
This markdown preserves all normative requirements, cross-references, and structural hierarchy while removing boilerplate and condensing explanatory text. The document header is included as this is the first (and only) chunk. The requirements summary table provides a quick overview; the full requirement text is in the clauses. Informative annexes section is condensed to a brief description of the informative references.