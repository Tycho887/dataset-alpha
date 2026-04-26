# ETSI TS 102 023 V1.2.2: Policy requirements for time-stamping authorities
**Source**: ETSI | **Version**: V1.2.2 | **Date**: 2008-10 | **Type**: Normative
**Original**: http://www.etsi.org

## Scope (Summary)
Specifies policy requirements for the operation and management practices of Time‑stamping Authorities (TSAs). Primarily for time-stamping services supporting qualified electronic signatures (EU Directive 1999/93/EC) but applicable to any use requiring proof of existence before a given time. Based on public key cryptography, certificates, and reliable UTC time sources.

## Normative References
- [1] ITU-R TF.460-5 (1997): Standard-frequency and time-signal emissions
- [2] ITU-R TF.536-1 (1998): Time scale notations
- [3] Directive 95/46/EC (Data Protection)
- [4] FIPS PUB 140-1 (1994): Security Requirements for Cryptographic Modules
- [5] ISO/IEC 15408 (1999) parts 1-3: Evaluation criteria for IT security
- [6] CEN Workshop Agreement 14167-2: Protection Profile for CSP Signing Operations
- [7] ISO/IEC 17799: Code of practice for information security management
- [8] ITU-R TF.460-4: Standard-frequency and time-signal emissions

## Definitions and Abbreviations
- **Coordinated Universal Time (UTC)**: Time scale based on the second as defined in ITU-R TF.460-5
- **relying party**: Recipient of a time‑stamp token who relies on it
- **subscriber**: Entity requiring TSA services that has agreed to its terms and conditions
- **time‑stamp policy**: Named set of rules indicating applicability of a time‑stamp token to a community/class of application
- **time‑stamp token**: Data object binding a representation of a datum to a particular time, establishing evidence of existence before that time
- **Time‑Stamping Authority (TSA)**: Authority that issues time‑stamp tokens
- **Time‑Stamping Unit (TSU)**: Set of hardware/software managed as a unit with a single signing key active at a time
- **TSA Disclosure statement**: Statements about policies/practices requiring emphasis or disclosure
- **TSA practice statement**: Statement of practices employed in issuing time‑stamp tokens
- **TSA system**: Composition of IT products supporting time‑stamping services
- **UTC(k)**: Time scale realized by laboratory "k" kept close to UTC (±100 ns, see ITU-R TF.536-1)
- **Abbreviations**: BIPM, GMT, IERS, IT, TAI, TSA, TST, TSU, UTC

## 4 General Concepts
### 4.1 Time‑stamping services
Decomposed into *time‑stamping provision* (generates tokens) and *time‑stamping management* (monitors/controls). This subdivision is for clarity only.

### 4.2 Time‑Stamping Authority (TSA)
Trusted authority issuing time‑stamp tokens. Responsible for one or more TSUs. May subcontract but retains overall responsibility. TSA is a certification‑service‑provider under EU Directive 1999/93/EC.

### 4.3 Subscriber
May be organization (responsible for end‑users) or individual end‑user.

### 4.4 Time‑stamp policy and TSA practice statement
- Policy states "what to adhere to"; practice statement states "how it is adhered to".
- Policy is less specific; practice statement is detailed, tailored to the TSA’s environment.
- Policy may be defined by user; practice statement always by provider.

## 5 Time‑stamp Policies
### 5.1 Overview
Defines requirements for a baseline time‑stamp policy for TSAs issuing tokens with **accuracy of 1 second or better**.
- A TSA may define its own enhanced policy that **shall** incorporate or further constrain these requirements.
- If accuracy better than 1 s is provided, it **shall** be indicated in disclosure statement and in each token.

### 5.2 Identification
Object‑identifier of baseline policy: `itu-t(0) identified-organization(4) etsi(0) time-stamp-policy(02023) policy-identifiers(1) baseline-ts-policy(1)`
TSA **shall** include this identifier in disclosure statement when claiming conformance.

### 5.3 User Community and applicability
Aimed at time‑stamping qualified electronic signatures for long‑term validity, but generally applicable.

### 5.4 Conformance
TSA **shall** use the policy identifier in time‑stamp tokens (or define own policy that incorporates/constrains these requirements) if:
- a) claims conformance and makes evidence available; or
- b) has been assessed conformant by independent party.
Conformant TSA **must** demonstrate:
- c) meets obligations of clause 6.1;
- d) implements controls meeting clause 7.

## 6 Obligations and Liability
### 6.1 TSA obligations
#### 6.1.1 General
- TSA **shall** implement all applicable requirements of clause 7.
- TSA **shall** ensure conformance even if functions are subcontracted.
- TSA **shall** adhere to additional obligations in the time‑stamp policy.
- TSA **shall** provide services consistent with its practice statement.

#### 6.1.2 TSA obligations towards subscribers
TSA **shall** meet its claims (availability, accuracy) as given in terms and conditions.

### 6.2 Subscriber obligations
No specific obligations beyond TSA’s terms and conditions.
*Note: advisable to verify token signature and key integrity.*

### 6.3 Relying party obligations
Terms **shall** include obligation that relying party **shall**:
- a) verify token signature and that private key not compromised until verification time;
- b) consider any usage limitations indicated by policy;
- c) consider other precautions in agreements.

### 6.4 Liability
No specific requirement; TSA may disclaim/limit liability unless otherwise stipulated by applicable law.

## 7 Requirements on TSA Practices
TSA **shall** implement controls meeting the following requirements. Requirements are stated as security objectives followed by specific controls.

### 7.1 Practice and Disclosure Statements
#### 7.1.1 TSA Practice statement
- a) **shall** carry out risk assessment.
- b) **shall** have statement of practices addressing all policy requirements.
- c) practice statement **shall** identify obligations of external organizations.
- d) **shall** make practice statement and relevant docs available to subscribers/relying parties.
- e) **shall** disclose terms and conditions per clause 7.1.2.
- f) **shall** have high‑level management body approving practice statement.
- g) senior management **shall** ensure proper implementation.
- h) **shall** define review process.
- i) **shall** give due notice of changes and make revised statement available.

#### 7.1.2 TSA disclosure Statement
TSA **shall** disclose terms and conditions, specifying for each policy:
- a) contact info
- b) policy identifier
- c) at least one hashing algorithm
- d) expected lifetime of signature used to sign token
- e) accuracy of time w.r.t. UTC
- f) limitations on use
- g) subscriber obligations (if any)
- h) relying party obligations (clause 6.3)
- i) verification instructions and limitations on validity period
- j) retention period for event logs
- k) applicable legal system (including national law requirements)
- l) limitations of liability
- m) complaints/dispute procedures
- n) if assessed conformant, by which independent body
Information **shall** be available through durable means, in readily understandable language.

### 7.2 Key Management Life Cycle
#### 7.2.1 TSA key generation
- a) generation **shall** be in physically secured environment, under dual control, by trusted roles.
- b) generation **shall** be within cryptographic module meeting FIPS PUB 140‑1 level 3, CEN 14167‑2, or ISO/IEC 15408 EAL 4+.
- c) algorithm and key length **shall** be fit for purpose (see TS 102 176‑1).

#### 7.2.2 TSU private key protection
- a) key **shall** be held and used within cryptographic module meeting same criteria as 7.2.1b.
- b) if backed up, copying/storage/recovery **shall** be under dual control in physically secured environment.
- c) backup copies **shall** be protected for confidentiality before storage.

#### 7.2.3 TSU public key Distribution
- a) public keys **shall** be made available via public key certificate.
- b) certificate **shall** be issued by a CA operating under a certificate policy of equivalent or higher security.

#### 7.2.4 Rekeying TSU’s Key
Lifetime of TSU certificate **shall not** be longer than period for which algorithm/key length is fit for purpose.

#### 7.2.5 End of TSU key life cycle
- a) procedures **shall** ensure new key when current expires.
- b) private keys **shall** be destroyed such that they cannot be retrieved.
- c) token generation system **SHALL** reject attempts to issue tokens if key has expired.

#### 7.2.6 Life cycle management of cryptographic module
- a) **shall** prevent tampering during shipment.
- b) **shall** prevent tampering during storage.
- c) installation/activation/duplication **shall** be under dual control in physically secured environment.
- d) **shall** ensure module functions correctly.
- e) keys **shall** be erased upon device retirement.

### 7.3 Time‑stamping
#### 7.3.1 Time‑stamp token
- a) **shall** include policy identifier.
- b) **shall** have unique identifier.
- c) time values **shall** be traceable to at least one UTC(k) laboratory.
- d) time **shall** be synchronized with UTC within declared accuracy.
- e) if clock detected out of accuracy, tokens **shall not** be issued.
- f) **shall** include representation (e.g., hash) of datum.
- g) **shall** be signed with key generated exclusively for this purpose.
- h) **shall** include: country identifier (if applicable), TSA identifier, TSU identifier.

#### 7.3.2 Clock Synchronization with UTC
- a) calibration **shall** maintain clocks within declared accuracy.
- b) clocks **shall** be protected against threats causing undetected change.
- c) TSA **shall** detect if time drifts/jumps out of sync.
- d) leap second handling **shall** occur during last minute of scheduled day; record **shall** be maintained of exact time.

### 7.4 TSA Management and Operation
#### 7.4.1 Security management
- a) TSA **shall** retain responsibility for all aspects, even if outsourced; responsibilities of third parties **shall** be defined.
- b) management **shall** provide direction via a high‑level steering forum; **shall** publish/communicate security policy.
- c) information security infrastructure **shall** be maintained; changes impacting security **shall** be approved.
- d) security controls and operating procedures **shall** be documented, implemented, maintained.
- e) security **shall** be maintained when functions are outsourced.

#### 7.4.2 Asset classification and management
- a) **shall** maintain inventory and assign protection classification consistent with risk analysis.

#### 7.4.3 Personnel security
- a) **shall** employ personnel with expert knowledge/experience/qualifications.
- b) security roles **shall** be documented in job descriptions; trusted roles identified.
- c) job descriptions **shall** reflect separation of duties and least privilege.
- d) personnel **shall** exercise procedures in line with security management.
- Additional for management:
  - e) managerial personnel **shall** possess knowledge of time‑stamping, digital signatures, UTC synchronization, security procedures, risk assessment.
  - f) trusted roles **shall** be free from conflict of interest.
  - g) trusted roles include Security Officers, System Administrators, System Operators, System Auditors.
  - h) personnel **shall** be formally appointed to trusted roles by senior management.
  - i) **shall** not appoint anyone known to have conviction for serious crime; checks completed before access.

#### 7.4.4 Physical and environmental security
- a) physical access **shall** be limited to authorized individuals; controls **shall** avoid loss/damage/compromise; theft/interruption.
- b) access controls **shall** be applied to cryptographic module per 7.2.1/7.2.2.
- Additional for management:
  - facilities **shall** be operated in physically protected environment.
  - achieve protection through defined security perimeters; shared premises outside.
  - controls **shall** address physical access, natural disasters, fire, utilities, collapse, leaks, theft, disaster recovery.
  - **shall** protect against unauthorized removal of equipment/media/software.

#### 7.4.5 Operations management
- a) integrity **shall** be protected against viruses/malware.
- b) incident reporting/response **shall** minimize damage.
- c) media **shall** be handled securely.
- d) procedures **shall** be established for all trusted/administrative roles.
- e) media handling: **shall** be secure per classification; sensitive data securely disposed.
- f) capacity **shall** be monitored and projections made.
- g) TSA **shall** respond quickly to incidents; all incidents reported ASAP.
- Additional for management:
  - h) TSA security operations **shall** be separated from other operations.

#### 7.4.6 System Access Management
- a) controls (e.g., firewalls) **shall** protect internal networks from unauthorized access.
- b) **shall** ensure effective administration of user access.
- c) access **shall** be restricted per policy; system **shall** provide separation of trusted roles; utility programs restricted.
- d) personnel **shall** be identified/authenticated before using critical applications.
- e) personnel **shall** be accountable (event logs).
- Additional for management:
  - f) local network components **shall** be in physically secure environment; configurations periodically audited.
  - g) continuous monitoring/alarm facilities **shall** detect/register/react to unauthorized access attempts.

#### 7.4.7 Trustworthy Systems Deployment and Maintenance
- a) security requirements analysis **shall** be carried out at design stage.
- b) change control procedures **shall** be applied for software releases/modifications/fixes.

#### 7.4.8 Compromise of TSA Services
- a) disaster recovery plan **shall** address compromise or loss of calibration.
- b) in case of compromise/loss, TSA **shall** make description available to subscribers/relying parties.
- c) TSU **shall not** issue tokens until recovery steps taken.
- d) in major compromise, TSA **shall** make info available to identify affected tokens (unless privacy/security breach).

#### 7.4.9 TSA termination
- a) before termination **shall**:
  - notify subscribers/relying parties
  - terminate subcontractor authorizations
  - transfer obligations for event logs/audit archives to reliable party for reasonable period
  - maintain or transfer public key/certificate availability for reasonable period
  - destroy private keys
- b) **shall** have arrangement to cover costs if bankrupt/otherwise unable.
- c) practices **shall** state provisions for termination.
- d) **shall** revoke TSU certificates.

#### 7.4.10 Compliance with Legal Requirements
- a) **shall** meet European Data Protection Directive [3] (national implementations).
- b) **shall** take technical/organisational measures against unauthorized processing and accidental loss.
- c) user information **shall** be protected from disclosure unless agreed or required by law.

#### 7.4.11 Recording of information concerning operation of time‑stamping service
- a) events/data to be logged **shall** be documented.
- b) confidentiality/integrity of records **shall** be maintained.
- c) records **shall** be archived confidentially per disclosed practices.
- d) records **shall** be made available for legal proceedings.
- e) precise time of significant events **shall** be recorded.
- f) records **shall** be held for period appropriate for legal evidence (as notified in disclosure statement).
- g) logs **shall** be protected from easy deletion/destruction.
- h) subscriber information **shall** be kept confidential unless agreed.
- Additional for key management:
  - i) all key life‑cycle events **shall** be logged.
  - j) all certificate life‑cycle events **shall** be logged.
- Additional for clock sync:
  - k) all synchronisation events **shall** be logged (including normal recalibration).
  - l) all loss‑of‑sync detection events **shall** be logged.

### 7.5 Organizational
- a) policies/procedures **shall** be non‑discriminatory.
- b) services **shall** be accessible to all applicants within declared field who agree to obligations.
- c) TSA **shall** be a legal entity under national law.
- d) TSA **shall** have quality/information security management system appropriate for services.
- e) TSA **shall** have adequate arrangements to cover liabilities.
- f) TSA **shall** have financial stability/resources to operate in conformity with policy.
- g) **shall** employ sufficient personnel with necessary education/training/knowledge/experience.
- h) **shall** have policies/procedures for complaints/disputes.
- i) **shall** have documented agreement/contract when subcontracting/outsourcing.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | TSA shall implement all applicable requirements of clause 7 | shall | 6.1.1 |
| R2 | TSA shall use policy identifier in tokens when claiming conformance | shall | 5.2, 5.4 |
| R3 | Key generation shall be in physically secured environment, dual control | shall | 7.2.1a |
| R4 | TSU private key held in cryptographic module meeting specified standards | shall | 7.2.2a |
| R5 | Public key distributed via certificate from CA with equivalent security | shall | 7.2.3 |
| R6 | Token shall include policy identifier, unique ID, traceable time, hash, digital signature | shall | 7.3.1a‑g |
| R7 | Clock synchronized with UTC within declared accuracy; if out, tokens not issued | shall | 7.3.2a‑c, 7.3.1e |
| R8 | TSA shall disclose terms per clause 7.1.2 via durable means | shall | 7.1.2 |
| R9 | TSA shall have risk assessment, practice statement, management approval | shall | 7.1.1a‑f |
| R10 | TSA shall ensure conformance even when subcontracted | shall | 6.1.1 |
| R11 | Relying party shall verify token signature and key status | shall | 6.3 |
| R12 | TSA shall log all significant events per 7.4.11 | shall | 7.4.11 |

## Informative Annexes (Condensed)
- **Annex A (Potential liability)**: Liability arises from contract or statutory law. Consumer protections (e.g., Unfair Contract Terms Directive) may limit TSA’s ability to limit liability. Otherwise, TSA may disclaim warranties.
- **Annex B (Model TSA disclosure statement)**: Provides a structured template for TSAs to disclose terms. Includes sections: entire agreement, contact info, token types/usage, reliance limits, subscriber obligations, public key status, warranty/liability, agreements, privacy, refund, applicable law/complaints, audit.
- **Annex C (Coordinated Universal Time)**: Explains UTC as the global time standard (successor to GMT), based on atomic time (TAI) with leap seconds inserted by IERS to keep within 0.9s of UT1. UTC(k) are local realizations by national labs.
- **Annex D (Long term verification of time‑stamp tokens)**: Verification beyond certificate validity may be possible if TSU key not compromised, hash collision‑free, and signature algorithm still secure. Limitations may be mitigated by re‑time‑stamping or secure storage. Supports use of time‑marking as alternative.
- **Annex E (Possible implementation architectures)**: Describes managed time‑stamping service (hosted TSU remotely managed by TSA) and selective alternative quality (different TSUs provide different algorithms/accuracies; quality parameters may be requested).
- **Annex F (Bibliography)**: Lists additional references: EU distance contracts directive, algorithms guidance, ISO/IEC 14516 (TTP guidelines), ISO/IEC TR 13335 series (IT security management).