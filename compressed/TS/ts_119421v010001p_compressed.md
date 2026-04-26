# ETSI TS 119 421 V1.0.1: Policy and Security Requirements for Trust Service Providers issuing Time-Stamps
**Source**: ETSI | **Version**: V1.0.1 | **Date**: 2015-07 | **Type**: Normative  
**Original**: [ETSI TS 119 421 (2015-07)]

## Scope (Summary)
Specifies policy and security requirements for the operation and management practices of Trust Service Providers (TSPs) issuing time-stamps. These time-stamps support digital signatures or any application requiring proof that data existed before a particular time. The document may be used by independent bodies for conformance assessment. Not specified: protocols (see IETF RFC 3161 profiled in ETSI TS 119 422), assessment methods, information for assessors, or assessor requirements.

## Normative References
- [1] Recommendation ITU-R TF.460-6 (2002): "Standard-frequency and time-signal emissions"
- [2] ISO/IEC 19790:2006: "Information technology -- Security techniques -- Security requirements for cryptographic modules"
- [3] ISO/IEC 15408 (1999) (parts 1 to 3): "Information technology -- Security techniques -- Evaluation criteria for IT security"
- [4] ETSI TS 119 401: "Electronic Signatures and Infrastructures (ESI); General Policy Requirements for Trust Service Providers"
- [5] ETSI TS 119 422: "Electronic Signatures and Infrastructures (ESI); Time-stamping protocol and time-stamp profiles"

## Definitions and Abbreviations
- **Coordinated Universal Time (UTC)**: time scale based on the second as defined in Recommendation ITU-R TF.460-6 [1]
- **relying party**: recipient of a time-stamp who relies on that time-stamp
- **subscriber**: legal or natural person to whom a time-stamp is issued and who is bound to any subscriber obligations
- **time-stamp**: data in electronic form which binds other electronic data to a particular time establishing evidence that these data existed at that time
- **time-stamp policy**: named set of rules that indicates the applicability of a time-stamp to a particular community and/or class of application with common security requirements (a specific type of trust service policy as defined in ETSI TS 119 401 [4])
- **trust service**: electronic service that enhances trust and confidence in electronic transactions
- **Trust Service Provider (TSP)**: entity which provides one or more trust services
- **Time-Stamping Authority (TSA)**: TSP which issues time-stamps using one or more time-stamping units
- **Time-Stamping Unit (TSU)**: set of hardware and software which is managed as a unit and has a single time-stamp signing key active at a time
- **TSA Disclosure statement**: set of statements about the policies and practices of a TSA that particularly require emphasis or disclosure to subscribers and relying parties
- **TSA practice statement**: statement of the practices that a TSA employs in issuing time-stamp (a specific type of trust service practice statement as defined in ETSI TS 119 401 [4])
- **TSA system**: composition of IT products and components organized to support the provision of time-stamping services
- **UTC(k)**: time scale realized by the laboratory "k" and kept in close agreement with UTC, with the goal to reach ±100 ns.

Abbreviations: BIPM, BTSP, CA, GMT, IERS, IT, TAI, TSA, TSP, TSU, UTC.

## General Concepts
### 4.1 General policy requirements concepts
References ETSI TS 119 401 [4] for generic policy requirements. Policy requirements based on public key cryptography, certificates, and reliable time sources.

### 4.2 Time-stamping services
Broken into component services: Time-stamping provision (generates time-stamps) and Time-stamping management (monitors and controls service).

### 4.3 Time-Stamping Authority (TSA)
A TSP providing time-stamping services to the public. Overall responsibility for provision and operation of one or more TSUs. TSA may subcontract but retains overall responsibility.

### 4.4 Subscriber
Obligations: If subscriber is an organization, it comprises end-users; organization held responsible for end-user obligations.

### 4.5 Time-stamp policy and TSA practice statement
Time-stamp policy is a Trust Service Policy; TSA Practice Statement is a Trust Service Practice Statement. The present document specifies a time-stamp policy (BTSP). TSAs specify in practice statements how requirements are met.

## Introduction to time-stamp policies and general requirements
### 5.1 General
Policy requirements defined for a best practices time-stamp policy (BTSP) for TSAs issuing time-stamps supported by public key certificates, with accuracy of 1 second or better. A TSA may define its own policy enhancing this; such policy **shall** incorporate or further constrain these requirements. If accuracy better than 1 second is provided, accuracy **shall** be indicated in TSA's disclosure statement and in each time-stamp.

### 5.2 Identification
Identifier for BTSP: itu-t(0) identified-organization(4) etsi(0) time-stamp-policy(2023) policy-identifiers(1) baseline-ts-policy (1). By including this OID in a time-stamp, TSA claims conformance. TSA **shall** include identifier in disclosure statement. When using own identifier, TSA **shall** indicate the ETSI identifier (BTSP) being supported.

### 5.3 User community and applicability
#### 5.3.1 Best practices time-stamp policy
Aimed at meeting time-stamp requirements for long term validity but generally applicable.

## Policies and practices
### 6.1 Risk assessment
Requirements from ETSI TS 119 401 [4], clause 5 **shall** apply.

### 6.2 Trust Service Practice Statement
Requirements from ETSI TS 119 401 [4], clause 6.1 **shall** apply. Additionally, statement **shall** specify for each policy:
- a) at least one hashing algorithm
- b) accuracy of time with respect to UTC
- c) any limitations on use
- d) subscriber obligations (clause 6.5.2)
- e) relying party obligations (clause 6.6)
- f) information on how to verify time-stamp and any limitations on validity period
- g) any claim to meet national law requirements

TSA **should** include availability of service. Model TSA disclosure statement in annex B may be used.

### 6.3 Terms and conditions
General obligations from ETSI TS 119 401 [4], clause 6.2 **shall** apply.

### 6.4 Information security policy
Requirements from ETSI TS 119 401 [4], clause 6.3 **shall** apply.

### 6.5 TSA obligations
#### 6.5.1 General
TSA **shall** adhere to any additional obligations indicated in the time-stamp.

#### 6.5.2 TSA obligations towards subscribers
No specific obligations beyond TSA-specific requirements in terms and conditions.

### 6.6 Information for relying parties
Terms and conditions **shall** include obligation on relying party to:
- a) verify that time-stamp has been correctly signed and private key not compromised until time of verification (note: during TSU certificate validity, check revocation; beyond validity, see annex D)
- b) take into account any limitations on usage indicated by policy
- c) take into account any other prescribed precautions

## TSA management and operation
### 7.1 Introduction
Policy requirements not meant to restrict charging. Requirements given in terms of security objectives and controls.

### 7.2 Internal organization
Requirements from ETSI TS 119 401 [4], clause 7.1 **shall** apply. Additional:
- a) TSA **shall** be a legal entity according to national law
- b) TSA **shall** have systems for quality and information security management appropriate for its services
- c) **Shall** employ sufficient personnel with necessary education, training, technical knowledge and experience

### 7.3 Personnel security
Requirements from ETSI TS 119 401 [4], clause 7.2 **shall** apply.

### 7.4 Asset management
Requirements from ETSI TS 119 401 [4], clause 7.3 **shall** apply.

### 7.5 Access control
Requirements from ETSI TS 119 401 [4], clause 7.4 **shall** apply.

### 7.6 Cryptographic controls
#### 7.6.1 General
Requirements from ETSI TS 119 401 [4], clause 7.5 **shall** apply.

#### 7.6.2 TSU key generation
- a) Generation **shall** be in physically secured environment by trusted roles under at least dual control
- b) Generation **shall** be within a cryptographic module meeting ISO/IEC 19790 level 3 or higher, or trustworthy system assured to EAL 4 or higher per ISO/IEC 15408, based on risk analysis
- c) Algorithm, key length and signature algorithm **shall** be recognized by national supervisory body or in accordance with state of art as fit for purpose
- d) TSU signing key **should** not be imported into different cryptographic modules

#### 7.6.3 TSU private key protection
Private keys **shall** remain confidential and integrity maintained:
- a) **Shall** be held and used within a cryptographic module meeting ISO/IEC 19790 level 3 or higher, or EAL 4 or higher per ISO/IEC 15408
- b) If backed up, **shall** be copied, stored and recovered only by trusted roles using dual control in physically secured environment
- c) Backup copies **shall** be protected for integrity and confidentiality by the cryptographic module before storing outside

#### 7.6.4 TSU public key certificate
TSA **shall** guarantee integrity and authenticity of TSU public keys:
- a) **Shall** be made available in a public key certificate
- b) Certificate **should** be issued by a CA operating under ETSI TS 119 411-1 [i.11]
- c) TSU **shall not** issue time-stamp before its public key certificate is loaded

When obtaining certificate, TSA **should** verify correct signing.

#### 7.6.5 Rekeying TSU's key
Life-time of TSU certificate **shall not** be longer than period for which chosen algorithm and key length is recognized as fit for purpose.

#### 7.6.6 Life cycle management of signing cryptographic hardware
- a) Cryptographic hardware **shall not** be tampered with during shipment
- b) **Shall not** be tampered with when stored
- c) Installation, activation and duplication of keys **shall** be done only by trusted roles using dual control in physically secured environment
- d) Private keys **shall** be erased upon device retirement such that recovery is practically impossible

#### 7.6.7 End of TSU key life cycle
TSA **shall** define an expiration date for TSU's keys, **shall not** be longer than end of validity of public key certificate. Date **should** consider recommended key sizes from ETSI TS 119 312 [i.7]; validity of signing key **should** be reduced to allow verification over time. Expiration may be defined at initialization or via private key usage period. TSU private signing keys **shall not** be used beyond end of life cycle. Operational procedures **shall** ensure new key put in place when key expires. Private keys, copies, **shall** be destroyed.

### 7.7 Time-stamping
#### 7.7.1 Time-stamp issuance
Time-stamps **shall** conform to profile in ETSI TS 119 422 [5]. **Shall** be issued securely with correct time:
- a) Time values **shall** be traceable to UTC(k) laboratory
- b) Time **shall** be synchronized with UTC within declared accuracy
- c) If clock detected out of stated accuracy, time-stamps **shall not** be issued
- d) Time-stamp **shall** be signed using a key generated exclusively for this purpose
- e) Generation system **shall** reject attempts if signing private key expired

#### 7.7.2 Clock synchronization with UTC
TSA clock **shall** be synchronized with UTC within declared accuracy:
- a) Calibration maintained to avoid drift outside declared accuracy
- b) Declared accuracy **shall** be 1 second or better
- c) Clocks **shall** be protected against threats causing undetected change
- d) TSA **shall** detect drifts or jumps out of synchronization
- e) If detected, TSU **shall** stop time-stamp issuance
- f) Synchronization **shall** be maintained when a leap second occurs; change occurs during last minute of scheduled day; record maintained of exact time

### 7.8 Physical and environmental security
Requirements from ETSI TS 119 401 [4], clause 7.6 **shall** apply. Additional:
- a) Access controls applied to cryptographic module per clause 7.6
- b) Time-stamping management facilities **shall** be operated in physically and logically protected environment; every entry subject to independent oversight; non-authorised persons accompanied; entry/exit logged; physical barriers defined; shared premises outside perimeter; policy addresses physical access, natural disasters, fire, utilities failure, theft, disaster recovery; equipment, media, software protected from unauthorized off-site removal

### 7.9 Operation security
Requirements from ETSI TS 119 401 [4], clause 7.7 **shall** apply. Additional:
- a) Capacity demands **shall** be monitored and future projections made

### 7.10 Network security
Requirements from ETSI TS 119 401 [4], clause 7.8 **shall** apply. Additional:
- a) TSA **shall** maintain and protect all TSU systems in a secure zone
- b) TSA **shall** configure TSU systems by removing/disabling unused accounts, applications, services, protocols, ports
- c) Only trusted roles **shall** access secure zones and high security zones

### 7.11 Incident management
Requirements from ETSI TS 119 401 [4], clause 7.9 **shall** apply.

### 7.12 Collection of evidence
Requirements from ETSI TS 119 401 [4], clause 7.10 **shall** apply. Additional:
- a) Records concerning all events relating to life-cycle of TSU keys **shall** be logged
- b) Records concerning life-cycle of TSU certificates **shall** be logged
- c) Records of all events relating to clock synchronization **shall** be logged
- d) Records of detection of loss of synchronization **shall** be logged

### 7.13 Business continuity management
Requirements from ETSI TS 119 401 [4], clause 7.11 **shall** apply. Additional:
- a) Disaster recovery plan **shall** address compromise or suspected compromise of TSU private keys or loss of calibration affecting issued time-stamps
- b) In case of compromise or loss of calibration, TSA **shall** make available description to subscribers and relying parties
- c) In case of compromise or loss of calibration, TSU **shall not** issue time-stamps until recovery steps taken
- d) In case of major compromise, TSA **shall** make available information to identify affected time-stamps unless it breaches privacy or security

### 7.14 TSA termination and termination plans
Requirements from ETSI TS 119 401 [4], clause 7.12 **shall** apply. Additional:
- a) When terminating, TSA **shall** revoke TSU certificates

### 7.15 Compliance
Requirements from ETSI TS 119 401 [4], clause 7.12 **shall** apply.

## Additional requirements for Regulation (EU) No 910/2014
### 8.1 TSU public key certificate
When a time-stamp is claimed to be a qualified electronic time-stamp per Regulation (EU) No 910/2014, TSU public key certificate **should** be issued by a CA operating under ETSI TS 119 411-2 [i.12] certificate policy. (Note: ETSI TS 119 411-2 incorporates ETSI TS 119 411-1. Relying party expected to use Trusted List to establish qualification; qcStatement "esi4-qtstStatement-1" may be used.)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | TSA shall be a legal entity. | shall | 7.2(a) |
| R2 | TSU key generation shall be under dual control in physically secured environment. | shall | 7.6.2(a) |
| R3 | TSU private keys shall be used in cryptographic module meeting ISO 19790 level 3 or EAL4+. | shall | 7.6.3(a) |
| R4 | Time-stamps shall conform to ETSI TS 119 422 profile. | shall | 7.7.1 |
| R5 | Time values shall be traceable to UTC(k) laboratory. | shall | 7.7.1(a) |
| R6 | Accuracy shall be 1 second or better. | shall | 7.7.2(b) |
| R7 | TSU shall stop issuance if clock drifts out of synchronization. | shall | 7.7.2(e) |
| R8 | Time-stamp shall be signed using key generated exclusively for this purpose. | shall | 7.7.1(d) |
| R9 | TSA shall detect drifts or jumps out of synchronization. | shall | 7.7.2(d) |
| R10 | Private key expiration date shall be defined; keys not used beyond life cycle. | shall | 7.6.7 |

## Informative Annexes (Condensed)
- **Annex A (Potential liability)**: Liability derives from contract or statutory law; consumer protections (Directive 93/13/EEC) may constrain liability limitation.
- **Annex B (Model TSA disclosure statement)**: Provides a template for TSA disclosure statements with sections on entire agreement, contact info, time-stamp types, reliance limits, subscriber obligations, TSU certificate status, warranty/liability, applicable agreements, privacy, refund, applicable law/complaints, and trust marks/audit.
- **Annex C (Coordinated Universal Time)**: UTC is maintained by BIPM with IERS, based on TAI with integer offset; full definition in ITU-R TF.460-6.
- **Annex D (Long term verification of time-stamps)**: Verification beyond certificate validity is possible if private key not compromised, hash algorithms collision-free, signature algorithm secure. May be maintained via additional time-stamp or secure storage.
- **Annex E (Regulation (EU) No 910/2014 cross-reference)**: Maps requirements for qualified electronic time-stamps under Regulation (EU) No 910/2014 to BTSP clauses (Articles 42 and 24).
- **Annex F (Possible implementation architectures)**: Describes managed time-stamping service (hosted TSUs remotely managed by TSA) and selective alternative quality (different TSUs for different algorithm/accuracy combinations).
- **Annex G (Major changes from ETSI TS 102 023)**: Significant updates include referencing ETSI TS 119 401, updated definitions, disclosure statement, key generation/protection references, new requirements (e.g. no time-stamp issuance before certificate loaded), clock synchronization drift detection.
- **Annex H (Conformity Assessment Check list)**: A spreadsheet file accompanies the document for assessment; includes requirements from this TS and ETSI TS 119 401. ETSI grants free reproduction for intended purposes.