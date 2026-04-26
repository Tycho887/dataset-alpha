# ETSI TR 101 564 V1.1.1: Guidance on ETSI TS 102 042 for Issuing Extended Validation Certificates for Auditors and CSPs
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2011-09 | **Type**: Technical Report (Informative)
**Original**: [Not provided]

## Scope (Summary)
Provides guidance for assessment of Certification Authorities (CAs) issuing Extended Validation (EV) Certificates, based on ETSI TS 102 042 [i.1] and the CAB Forum Extended Validation Guidelines (EVCG) [i.2]. Intended for auditors and CAs to understand conformance requirements for EV SSL/TLS, code signing, and other applications.

## Informative References
- [i.1] ETSI TS 102 042: Policy requirements for certification authorities issuing public key certificates
- [i.2] Guidelines for The Issuance and Management of Extended Validation Certificates, CA Browser Forum
- [i.3] ETSI TS 101 456 (qualified certificates)
- [i.4] ETSI TS 102 176-1 (algorithms and parameters)
- [i.5] IETF RFC 3647 (PKI CP/CPS framework)
- [i.6] ETSI TS 102 023 (time-stamping policy)
- [i.7] ISO/IEC 27001 (ISMS requirements)
- [i.8] ISO/IEC 27002 (ISMS code of practice)

## Definitions and Abbreviations
Terms defined in TS 102 042 [i.1] and EVCG [i.2] apply.
- **CA**: Certification Authority
- **CAB**: Certification Authority/Browser Forum
- **CM**: Cryptographic Module
- **CP**: Certificate Policy
- **CPS**: Certification Practice Statement
- **CRL**: Certificate Revocation List
- **CSP**: Certification Service Provider (synonymous with CA in this document)
- **EV**: Extended Validation
- **EVC**: Extended Validation Certificate
- **EVCG**: Extended Validation Certificate Guidelines
- **EVCP**: Extended Validation Certificate Policy
- **EVCP+**: Enhanced Extended Validation Certificate Policy
- **NCP**: Normalized Certificate Policy
- **NCP+**: Extended Normalized Certificate Policy
- **OCSP**: Online Certificate Status Protocol
- **OID**: Object Identifier
- **PKI**: Public Key Infrastructure
- **SSL**: Secure Sockets Layer
- **TLS**: Transport Layer Security
- **TSA**: Time Stamping Authority

## 4 Overview
Auditors shall assess compliance of CSP/CA with TS 102 042 [i.1] and EVCG [i.2] clauses. Additional provisions may be specified. The document provides guidance for each clause.

## 5 Policies for issuing extended validation certificates
### 5.1 Overview
The TS 102 042 [i.1] policies relevant to EVC are:
- **EVCP**: Includes all NCP requirements plus additional provisions from EVCG [i.2] for EVC issue, usage, and maintenance.
- **EVCP+**: Includes all NCP+ requirements enhanced with provisions for secure user device when EVC owner must operate using a secure device.
- **Auditor check**: Verify available policy documentation (CP or CPS) aligns with EVCP/EVCP+ and verify EV cert OID.

### 5.2 Identification
The OIDs for EVCP and EVCP+ are specified in TS 102 042 [i.1] clause 5.2 (items d and e). The CA shall include identifier(s) for supported policies in terms and conditions. **Auditor check**: Certificate either identifies EVC policies or a certificate policy incorporating EVCG [i.2] section 8.2 requirements.

### 5.3 User Community and Applicability
Policy requirements apply to EV Certificates as per EVCG [i.2] section 6.1. **Auditor check**: Primary purpose stated in CP relates to that in EVCG [i.2] section 6.1.

### 5.4 Conformance
Requirements and guidance on conformity assessment to be addressed in a separate document.

## 6 Obligations and liability
### 6.1 Certification authority obligations
**Auditor check**: Verify CP covers EVCP/EVCP+. Verify CPS, subscriber agreements, and third-party contracts against TS 102 042 [i.1] clause 6.1 and EVCG [i.2] sections 6.2 and 12.2.

### 6.2 Subscriber obligations
**Auditor check**: Verify subscriber agreements address TS 102 042 [i.1] clause 6.2 items a), b), c), d), h), i). For code signing, refer to EVCG [i.2] Appendix G item 7 and Appendix H item 12. Verify procedures for key compromise (clause 6.2 j)). Consider requirements from TS 102 042 [i.1] clauses 7.3.1 m), 7.3.4; EVCG [i.2] sections 9.3.2, 9.3.3; revocation per clause 7.3.6. For algorithms and key sizes (item d), EVCG [i.2] Appendix A prevails over TS 102 176-1 [i.4] in case of conflict.

### 6.3 Information for Relying parties
**Auditor check**: Verify terms and conditions (see 7.3.4) include revocation/suspension policy, reporting/investigation procedures, contact details, and publication on company website. Check EVCG [i.2] section 11.1 (EVC status checking) and section 11.3 (problem reporting and response capability).

### 6.4 Liability
**Auditor check**: Verify procedures for minimum liability/insurance coverage per EVCG [i.2] section 7.1.3 (minimum assets coverage) and section 15.2 (limitations liability). Auditor may consider equivalent minimum cover in local currency.

## 7 Requirements on CA practice
The CA shall implement controls meeting the following requirements. The document covers registration, certificate generation, dissemination, revocation management, and revocation status (clause 4.2).

### 7.1 Certification practice statement
**Auditor check**:
- a) CPS addressing all requirements of applicable EV certificate policy per TS 102 042 [i.1] clause 7.1.
- b) CPS includes EVCG [i.2] section 7.1.2 item 3.
- c) Identification of policy/practice documents and obligations on external organizations/subcontractors (including RAs) per EVCG [i.2] sections 7.1.2(2), 15.1 and TS 102 042 [i.1] clause 7.1 c).
- d) Availability of CPS and relevant documentation for conformance assessment (EVCG [i.2] section 6.2.1 item 1c). Public disclosure 24x7 per EVCG [i.2] section 11.1.1.
- e) CAs and EV issuing CA hierarchy.
- f) CA's commitment to EVCG [i.2].
- g) Documentation of algorithms and parameters per EVCG [i.2] Appendix A and TS 102 176-1 [i.4] (Appendix A prevails in conflict).
- h) Processes for managing and reviewing CPS.
- i) EVCG [i.2] sections 7.1.3 (insurance) and 15.2 (liability).

### 7.2 Public key infrastructure - Key management life cycle
#### 7.2.1 Certification authority key generation
**Auditor check**: Verify CA Auditor's report on key generation ceremony per EVCG [i.2] section 14.1.5. Certificate signing algorithms must comply with TS 102 176-1 [i.4] and EVCG [i.2] Appendix A (Appendix A prevails in conflict). Use of cryptographic device per TS 102 042 [i.1] clause 7.2.1 b) sub-items iii, iv, or v. Check CA key generation per clause 7.2.1 a) and c). For EV code signing, check EVCG [i.2] Appendix H.

#### 7.2.2 Certification authority key storage, backup and recovery
**Auditor check**: Ensure CA private keys remain confidential and maintain integrity through cryptographic device per TS 102 042 [i.1] clause 7.2.2 a) sub-items iii, iv, or v. Verify backup/recovery procedures per clause 7.2.2 c) and d). If backed up outside secure device, protect per clause 7.2.2 b).

#### 7.2.3 Certification authority public key distribution
**Auditor check**: Where possible, CA ensures correct certificate is used by web browser software prior to confirming distribution of root certificates.

#### 7.2.4 Key escrow
Not applicable (EV certificates not expected to be escrowed).

#### 7.2.5 Certification authority key usage
**Auditor check**: Ensure CA private keys not used inappropriately per TS 102 042 [i.1] clause 7.2.5.

#### 7.2.6 End of CA key life cycle
**Auditor check**: Ensure CA private signing keys not used beyond life cycle per TS 102 042 [i.1] clause 7.2.6, and recording of life cycle events per EVCG [i.2] section 13.1 (2)(A)(i). Algorithms per TS 102 176-1 [i.4] and EVCG [i.2] Appendix A (Appendix A prevails).

#### 7.2.7 Life cycle management of cryptographic hardware used to sign certificates
**Auditor check**: Ensure CSP has properly checked security of cryptographic hardware throughout lifecycle per TS 102 042 [i.1] clause 7.2.7 and recording per EVCG [i.2] section 13.1 (2)(A)(ii).

#### 7.2.8 CA provided subject key management services
If applicable, **auditor check**: Ensure subject keys generated securely and secrecy of private key assured. Algorithms and key sizes per EVCG [i.2] Appendix A and TS 102 176-1 [i.4] (Appendix A prevails).

#### 7.2.9 Secure user devices preparation
**Auditor check**: If CA issues secure user device, ensure it is carried out securely per TS 102 042 [i.1] clause 7.2.9. For EV code signing, follow EVCG [i.2] Appendix H item 10.

### 7.3 Public key infrastructure - Certificate Management life cycle
#### 7.3.1 Subject registration
The CA shall ensure evidence of subscriber/subject identification and accuracy of names and associated data are properly examined or concluded through attestations. **Auditor check**: Verify CSP registration procedures follow EVCG [i.2] sections 7.2, 9.1, 9.2, 10 and TS 102 042 [i.1] clause 7.3.1 items a), c), m), n), p), q). Note Appendices D, E, F. Information from previous registration per EVCG [i.2] section 10.13. Check applicant registration records per clause 7.3.1 item j. Records retained at least 7 years after EV Certificate ceases to be valid per EVCG [i.2] section 13.2.2. Dual control in validation per section 12.1.3.

#### 7.3.2 Certificate renewal, rekey and update
**Auditor check**: Ensure requests for certificates to previously registered subjects are complete, accurate, and authorized per TS 102 042 [i.1] clause 7.3.2 and EVCG [i.2] section 13.1 (B)(i).

#### 7.3.3 Certificate generation
**Auditor check**: Ensure CA issues certificates securely to maintain authenticity per TS 102 042 [i.1] clause 7.3.3 and EVCG [i.2] section 8. For SSL, check content per Appendix B; for code signing, per Appendix H(3).

#### 7.3.4 Dissemination of Terms and Conditions
**Auditor check**: Ensure CA's terms and conditions are made available to subscribers and relying parties per EVCG [i.2] section 10.7.3(8)(C) and TS 102 042 [i.1] clause 7.3.4.

#### 7.3.5 Certificate dissemination
**Auditor check**: Ensure certificates are made available as necessary per EVCG [i.2] section 10.7.3(8)(C) and TS 102 042 [i.1] clause 7.3.5.

#### 7.3.6 Certificate revocation and suspension
**Auditor check**:
- Revocation procedures follow EVCG [i.2] sections 11.1, 11.2 and TS 102 042 [i.1] clause 7.3.6.
- Revocation entries on CRL/OCSP not removed until expiration date of revoked EVC.
- CA can accept/respond to revocation/suspension requests 24x7 per EVCG [i.2] section 11.2.1.
- Online 24x7 repository for automatic status checking per section 11.1.1.
- Revocation events per section 11.2.2.
- Problem reporting/response capability per section 11.3.
- For code signing, per Appendix H item 13.

### 7.4 CA management and operation
#### 7.4.1 Security management
**Auditor check**: Review if CA has implemented and documented an ISMS (see ISO/IEC 27001 [i.7] and 27002 [i.8]). Check administrative and management security procedures per EVCG [i.2] section 13.3 and TS 102 042 [i.1] clause 7.4.1.

#### 7.4.2 Asset classification and management
**Auditor check**: Ensure CA assets and information receive appropriate protection per EVCG [i.2] section 13.3 and TS 102 042 [i.1] clause 7.4.2.

#### 7.4.3 Personnel security
**Auditor check**: Ensure personnel and hiring practices enhance trustworthiness per EVCG [i.2] section 12.1 and TS 102 042 [i.1] clause 7.4.3.

#### 7.4.4 Physical and environmental security
**Auditor check**: Physical access to critical services controlled, physical risks minimized per TS 102 042 [i.1] clause 7.4.4 and EVCG [i.2] section 13.3.3.

#### 7.4.5 Operations management
**Auditor check**: CA systems secure and correctly operated with minimal risk of failure per TS 102 042 [i.1] clause 7.4.5 and EVCG [i.2] section 13.2.1.

#### 7.4.6 System Access Management
**Auditor check**: CA system access limited to properly authorized individuals per TS 102 042 [i.1] clause 7.4.6 and EVCG [i.2] section 13.1(C)(i).

#### 7.4.7 Trustworthy systems deployment and maintenance
**Auditor check**: CA shall use trustworthy systems and products protected against modification per TS 102 042 [i.1] clause 7.4.7.

#### 7.4.8 Business continuity management and incident handling
**Auditor check**: Business continuity plan exists covering compromise of CA private signing key and restoration as soon as possible per TS 102 042 [i.1] clause 7.4.8 and EVCG [i.2] section 13.3.3.

#### 7.4.9 CA termination
**Auditor check**: Procedures minimize disruption to subscribers/relying parties and ensure continued maintenance of records for legal proceedings per TS 102 042 [i.1] clause 7.4.9 and EVCG [i.2] section 13.3.3.

#### 7.4.10 Compliance with Legal Requirements
**Auditor check**: CA compliance with legal requirements, including Data Protection Directive, per TS 102 042 [i.1] clause 7.4.10 and EVCG [i.2] section 15.

#### 7.4.11 Recording of information concerning certificates
**Auditor check**: All relevant information recorded for appropriate period, especially for evidence of certification for legal proceedings. Records retained at least 7 years after EV Certificate ceases to be valid per EVCG [i.2] section 13. National legal requirements also considered.

### 7.5 Organizational
**Auditor check**: Ensure organization is reliable per TS 102 042 [i.1] clause 7.5 and EVCG [i.2] section 15.2.

## 8 Additional EV Requirements
### 8.1 Time-stamping
Where CSP provides time-stamping for EV code signing, **auditor check** TSA applies requirements in EVCG [i.2] Appendix I. Also consider TS 102 023 [i.6] requirements.

### 8.2 Code signing Authority
Where CSP provides code signing with EV code signing, **auditor check** TSA applies requirements in EVCG [i.2] Appendix J.

## Informative Annexes (Condensed)
- **Annex A (Assessment Guidance Checklist)**: A detailed table replicating all auditor checks from clauses 5-8 in proforma format. It cross-references TS 102 042 and EVCG requirements and provides columns for findings. Purpose: enable auditors to systematically record compliance status (OK/Not OK) during assessment.
- **Annex B (Audit Report Framework)**: Provides suggested structure for final audit report. Topics include: statutory environment, list of CSP documents reviewed, statement on audit conditions, overall compliance evaluation (fully/partially/not compliant), clause-by-clause findings with severity levels (1-3), and recommendations for remediation. Next audit date range also suggested.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CA shall include identifier(s) for certificate policy in terms and conditions. | shall | Clause 5.2; TS 102 042 5.2; EVCG 8.2 |
| R2 | CP shall address EVCP or EVCP+ requirements. | shall | Clause 6.1; TS 102 042 6.1; EVCG 6.2,12.2 |
| R3 | Subscriber obligations shall meet TS 102 042 6.2 a)-d), h), i). | shall | Clause 6.2; TS 102 042 6.2; EVCG 9.3.2,9.3.3 |
| R4 | CA shall provide terms and conditions with revocation/suspension policy and reporting. | shall | Clause 6.3; EVCG 11.1,11.3 |
| R5 | CA shall ensure minimum liability/insurance per EVCG. | shall | Clause 6.4; EVCG 7.1.3,15.2 |
| R6 | CA shall have CPS addressing all EV certificate policy requirements. | shall | Clause 7.1; TS 102 042 7.1; EVCG 7.1.2 |
| R7 | CA key generation shall use cryptographic device per TS 102 042 7.2.1 b) iii-v. | shall | Clause 7.2.1; TS 102 042 7.2.1; EVCG 14.1.5 |
| R8 | CA private keys shall remain confidential and maintain integrity. | shall | Clause 7.2.2; TS 102 042 7.2.2 |
| R9 | CA shall not use private keys inappropriately. | shall | Clause 7.2.5; TS 102 042 7.2.5 |
| R10 | CA shall not use private signing keys beyond life cycle. | shall | Clause 7.2.6; TS 102 042 7.2.6; EVCG 13.1(2)(A)(i) |
| R11 | CA shall ensure security of cryptographic hardware throughout lifecycle. | shall | Clause 7.2.7; TS 102 042 7.2.7; EVCG 13.1(2)(A)(ii) |
| R12 | Subject registration shall follow EVCG sections 7.2,9.1,9.2,10 and TS 102 042 7.3.1. | shall | Clause 7.3.1; TS 102 042 7.3.1; EVCG 7.2,9.1,9.2,10 |
| R13 | Records of EV certificates retained at least 7 years after validity ceases. | shall | Clause 7.3.1; EVCG 13.2.2 |
| R14 | Certificate renewal/rekey/update shall be complete, accurate, authorized. | shall | Clause 7.3.2; TS 102 042 7.3.2; EVCG 13.1(B)(i) |
| R15 | Certificate generation shall maintain authenticity. | shall | Clause 7.3.3; TS 102 042 7.3.3; EVCG 8 |
| R16 | Terms and conditions shall be made available to subscribers and relying parties. | shall | Clause 7.3.4; TS 102 042 7.3.4; EVCG 10.7.3(8)(C) |
| R17 | Certificates shall be made available as necessary. | shall | Clause 7.3.5; TS 102 042 7.3.5; EVCG 10.7.3(8)(C) |
| R18 | Revocation procedures shall follow EVCG 11.1,11.2 and TS 102 042 7.3.6. | shall | Clause 7.3.6; EVCG 11.1,11.2; TS 102 042 7.3.6 |
| R19 | CA shall accept revocation/suspension requests 24x7. | shall | Clause 7.3.6; EVCG 11.2.1 |
| R20 | CA shall use trustworthy systems protected against modification. | shall | Clause 7.4.7; TS 102 042 7.4.7 |
| R21 | Business continuity plan shall exist covering CA key compromise. | shall | Clause 7.4.8; TS 102 042 7.4.8; EVCG 13.3.3 |
| R22 | CA termination procedures shall minimize disruption and maintain records. | shall | Clause 7.4.9; TS 102 042 7.4.9; EVCG 13.3.3 |
| R23 | CA shall comply with legal requirements including Data Protection Directive. | shall | Clause 7.4.10; TS 102 042 7.4.10; EVCG 15 |
| R24 | All relevant certificate information shall be recorded for appropriate period. | shall | Clause 7.4.11; TS 102 042 7.4.11; EVCG 13 |
| R25 | Organization shall be reliable. | shall | Clause 7.5; TS 102 042 7.5; EVCG 15.2 |
| R26 | For EV code signing, TSA shall apply EVCG Appendix I and consider TS 102 023. | should | Clause 8.1; EVCG Appendix I; TS 102 023 |
| R27 | For EV code signing, TSA shall apply EVCG Appendix J. | should | Clause 8.2; EVCG Appendix J |