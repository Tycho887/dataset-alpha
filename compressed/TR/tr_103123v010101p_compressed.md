# ETSI TR 103 123: Guidance for Auditors and CSPs on ETSI TS 102 042 for Issuing Publicly-Trusted TLS/SSL Certificates
**Source**: ETSI ESI | **Version**: V1.1.1 | **Date**: 2012-11 | **Type**: Informative (Technical Report)
**Original**: [ETSI TR 103 123](https://www.etsi.org/deliver/etsi_tr/103100_103199/103123/01.01.01_60/tr_103123v010101p.pdf)

## Scope (Summary)
This Technical Report provides guidance for auditors and Certification Authorities (CAs) on assessing CAs that issue publicly-trusted TLS/SSL certificates against ETSI TS 102 042 and the CA/Browser Forum Baseline Requirements (BRG). It clarifies how requirements from both documents apply to Domain Validation (DVC) and Organizational Validation (OVC) certificates. Annex A contains an assessment checklist; Annex B suggests an audit report framework.

## Normative References
- Not applicable (this document is informative; normative references are in TS 102 042 and BRG).

## Informative References
- [i.1] ETSI TS 102 042: Policy requirements for certification authorities issuing public key certificates.
- [i.2] CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates (BRG).
- [i.3] ETSI TS 101 456: Policy requirements for CAs issuing qualified certificates.
- [i.4] ETSI TS 102 176‑1: Algorithms and Parameters for Secure Electronic Signatures - Part 1: Hash functions and asymmetric algorithms.
- [i.5] IETF RFC 3647: Internet X.509 Public Key Infrastructure - Certificate Policy and Certification Practices Framework.
- [i.6] ISO/IEC 27001: Information security management systems - Requirements.
- [i.7] ISO/IEC 27002: Code of practice for information security management.
- [i.8] IETF RFC 5246: The Transport Layer Security Protocol, Version 1.2.
- [i.9] ETSI TS 103 090: Conformity Assessment for Trust Service Providers issuing Extended Validation Certificates.
- [i.10] ETSI TS 119 403: Trust Service Provider Conformity Assessment - General Requirements and Guidance.
- [i.11] CA/Browser Forum: Network and Certificate System Security Requirements (NetSec-CAB).
- [i.12] CA/Browser Forum: Guidelines for The Issuance and Management of Extended Validation Certificates (EVCG).

## Definitions and Abbreviations
- **BRG**: Baseline Requirements Guidelines (CA/Browser Forum).
- **CA**: Certification Authority.
- **CAB**: Certificate Authority/Browser.
- **CM**: Cryptographic Module.
- **CP**: Certificate Policy.
- **CPS**: Certification Practice Statement.
- **CRL**: Certificate Revocation List.
- **CSP**: Certification Service Provider (used synonymously with CA).
- **DVC**: Domain Validation Certificate.
- **DVCP**: Domain Validation Certificate Policy.
- **EVCG**: Extended Validation Certificate Guidelines.
- **NCP**: Normalized Certificate Policy.
- **NetSec-CAB**: Network Security Requirements - CA/Browser Forum.
- **OCSP**: Online Certificate Status Protocol.
- **OID**: Object Identifier.
- **OVC**: Organizational Validation Certificate.
- **OVCP**: Organizational Validation Certificate Policy.
- **PTC**: Publicly-Trusted Certificate (used synonymously with DVC and OVC).
- **PTC-BR**: Publicly-Trusted Certificate Policy - Baseline Requirements (used synonymously with DVCP and OVCP).
- **SSL**: Secure Socket Layer.
- **TLS**: Transport Layer Security.
- **TSP**: Trust Service Provider (used synonymously with CA).

## 4 Overview
The document guides auditors to assess CA compliance with TS 102 042 and BRG. Auditors **should** ascertain that provisions in corresponding clauses are complied with. Additional auditor provisions may apply.

## 5 Policies for Issuing Publicly-Trusted Certificates
### 5.1 Overview
Relevant policies for PTC (DVC/OVC):
1. **DVCP**: NCP enhanced with BRG requirements for domain validation.
2. **OVCP**: NCP enhanced with BRG requirements for organizational validation.

Auditors **should**:
- Check that policy documentation (CP/CPS) is in line with PTC-BR requirements.
- Verify OIDs of issued certificates correspond to the stated policy.

### 5.2 Identification
CA **shall** include policy identifier(s) in terms and conditions. OIDs may include:
- `itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) dvcp (6)`
- `itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ovcp (7)`

*(TS 102 042 clause 5.2 f) and g); BRG section 8.2)*

### 5.3 User Community and Applicability
Auditors **should** verify that the certificate’s primary purpose (as stated in CP/CPS) meets TS 102 042 clause 5.3.2 and BRG section 8.1.

### 5.4 Conformance
- **(a)** Conformity assessment **should** follow TS 103 090 (based on TS 119 403) and BRG sections 17.1–17.6.
- **(b)** Auditors **should** check regular quality assessment self-audits per BRG section 17.6.
- **(c)** Auditors **should** verify delegated third-party requirements per BRG section 14.2.

## 6 Obligations, Warranties and Liability
### 6.1 CA Obligations and Warranties
- Auditors **should** verify that CP/CPS covers PTC-BR requirements.
- Auditors **should** verify CPS, subscriber agreements, and third-party contracts per TS 102 042 clause 6.1 and BRG sections 7.1.2, 14.2.

### 6.2 Subscriber Obligations
- Auditors **should** verify subscriber agreements address TS 102 042 clause 6.2 a), b), c), d), h), i), j).
  - For **clause 6.2 i) and j)** (compromise of private key/CA): verify procedures to discontinue certificate usage upon CA compromise.
- Also consider: TS 102 042 clauses 7.3.1 m), 7.3.4; BRG section 10.3; revocation per TS 102 042 clause 7.3.6; algorithms/key sizes per BRG Appendix A (prevails over TS 102 176‑1 Annex A in case of conflict).

### 6.3 Information for Relying Parties
- Auditors **should** verify CA’s terms and conditions (clause 7.3.4):
  - Include revocation/suspension policy.
  - Provide contact details for incidents, questions, complaints.
  - Published on company website and available.
- Also check BRG section 13.1.2 (problem reporting and response capability).

### 6.4 Liability
- Auditors **should** verify procedures for minimum liability, insurance coverage, etc.
- Check disclaimers/limitations comply with applicable laws per BRG section 18.

## 7 Requirements on CA Practice
> *The CA **shall** implement the controls that meet the following requirements.*

### 7.1 Certification Practice Statement (CPS)
Auditors **should** verify:
- (a) CPS addresses all requirements of applicable PTC policy (TS 102 042 clause 7.1).
- (b) CPS includes BRG section 8.2.1 requirements.
- (c) Identification of policy/practice documents and obligations on external organizations/subcontractors (TS 102 042 clause 7.1 c)).
- (d) CPS and relevant documentation publicly available 24x7 (BRG section 8.2.2).
- (e) CA hierarchy.
- (f) CA commitment to BRG (section 8.3).
- (g) Senior management responsibility for implementation (TS 102 042 clause 7.1 g)).
- (h) Compliance with BRG sections 8.2.1, 8.2.2, 8.3.

### 7.2 Public Key Infrastructure – Key Management Life Cycle
#### 7.2.1 CA Key Generation
- Auditors **should** verify auditor’s report on key generation ceremony (BRG section 17.7).
- Certificate signing algorithms **shall** comply with TS 102 176‑1 and Appendix A of BRG (BRG prevails in conflict).
- Use of cryptographic device per TS 102 042 clause 7.2.1 b) sub-items iii, iv, v.
- Key generation audited per TS 102 042 clause 7.2.1 a) and c).
- Documentation per BRG Appendix A (1), (2) and 17.7.

#### 7.2.2 CA Key Storage, Backup and Recovery
- Auditors **should** verify CA private keys remain confidential and integral using cryptographic device per TS 102 042 clause 7.2.2 a) sub-items iii, iv, v and BRG section 16.6.
- Verify backup/recovery procedures per TS 102 042 clause 7.2.2 c), d); if backed up outside secure device, protect per clause 7.2.2 b).
- Compliance reports exist.

#### 7.2.3 CA Public Key Distribution
- Auditors **should** check that CA verifies correct certificate used by browser software before confirming distribution to supplier.

#### 7.2.4 Key Escrow
- Not applicable (publicly-trusted TLS/SSL certificates not escrowed).

#### 7.2.5 CA Key Usage
- Auditors **should** check CA private keys not used inappropriately (TS 102 042 clause 7.2.5).

#### 7.2.6 End of CA Key Life Cycle
- Auditors **should** check CA private signing keys not used beyond life cycle (TS 102 042 clause 7.2.6); recording of events per BRG section 15.2 (1)(a).

#### 7.2.7 Life Cycle Management of Cryptographic Hardware
- Auditors **should** verify security of cryptographic hardware throughout lifecycle (TS 102 042 clause 7.2.7); recording per BRG section 15.2 (1)(b).

#### 7.2.8 CA Provided Subject Key Management Services
- If applicable, auditors **should** check subject keys generated securely and secrecy assured (BRG section 10.2.4).
- Algorithms/key sizes per BRG Appendix A (prevails over TS 102 176‑1 Annex A in conflict).

#### 7.2.9 Secure User Devices Preparation
- Not applicable.

### 7.3 Public Key Infrastructure – Certificate Management Life Cycle
#### 7.3.1 Subject Registration
> *The CA **shall** ensure that evidence of subscriber’s and subject’s identification and accuracy of names and associated data are either properly examined or concluded through attestations, and that certificate requests are accurate, authorized, and complete.*

Auditors **should**:
- Verify CSP registration procedures follow BRG sections 10 and 11 and TS 102 042 clause 7.3.1 items a), c), d), h), i), j), k), l), m), n), p), q).
- Information from previous registration **shall** meet BRG section 11.
- Check applicant registration records per TS 102 042 clause 7.3.1 j).
- Records retained at least 7 years after certificate validity ends (BRG section 15.3.2).
- Check CA warranties per BRG section 7.1.

#### 7.3.2 Certificate Renewal, Rekey and Update
> *The CA **shall** ensure that requests for certificates issued to a previously registered subject are complete, accurate, and duly authorized.*

Auditors **should** check procedures per TS 102 042 clause 7.3.2 and BRG section 15.2 (2).

#### 7.3.3 Certificate Generation
> *The CA **shall** ensure that it issues certificates securely to maintain their authenticity.*

- Auditors **should** check procedures per TS 102 042 clause 7.3.3 and BRG section 9.
- Root CA certificates **shall** meet BRG section 12.
- Certificate content **should** be checked against BRG Appendix B.

#### 7.3.4 Dissemination of Terms and Conditions
> *The CA **shall** ensure that terms and conditions are made available to subscribers and relying parties.*

Auditors **should** check per BRG section 10.3 and TS 102 042 clause 7.3.4.

#### 7.3.5 Certificate Dissemination
> *The CA **shall** ensure that certificates are made available as necessary.*
Auditors **should** check per TS 102 042 clause 7.3.5.

#### 7.3.6 Certificate Revocation and Suspension
> *The CA **shall** ensure that certificates are revoked in a timely manner based on authorized and validated requests.*

Auditors **should** verify:
- Revocation procedures follow BRG sections 13.1, 13.2 and TS 102 042 clause 7.3.6.
- CRL/OCSP entries not removed until expiration of revoked certificate (BRG section 13.2).
- 24x7 acceptance and response to revocation/suspension (BRG section 13.1).
- 24x7 online repository for status checking (BRG section 13.2).
- Revocation events per BRG section 13.1.
- Problem reporting and response capability (BRG section 13.1).

### 7.4 CA Management and Operation
> *Auditors **should** check that the CA has implemented, documented, and tested the requirements specified in NetSec-CAB [i.11].*

#### 7.4.1 Security Management
- Auditors **should** review implementation of an information security management system (e.g., ISO/IEC 27001/27002).
- Administrative and management security procedures per BRG sections 14.2, 16 and TS 102 042 clause 7.4.1.

#### 7.4.2 Asset Classification and Management
- Auditors **should** check assets and information receive appropriate protection per TS 102 042 clause 7.4.2.

#### 7.4.3 Personnel Security
> *The CA **shall** ensure that personnel and hiring practices enhance trustworthiness.*

Auditors **should** check:
- Documented procedure to assign trusted roles.
- Responsibilities, tasks, separation of duties documented and implemented.
- Only trusted roles have access to security/high security zones.
- Least privilege principle for employees/contractors.
- Unique credential for system authentication.
- Disable all privileged access within 24 hours upon termination.
- Trusted role follows up on critical security event alerts.
- Human review of logs every 30 days and integrity validation.
*(from BRG section 14.1 and TS 102 042 clause 7.4.3)*

#### 7.4.4 Physical and Environmental Security
> *The CA **shall** ensure physical access to critical services is controlled and risks minimized.*

Auditors **should** check:
- Certificate systems segmented into networks/zones based on functional, logical, physical relationship.
- Root CA maintained in high security zone, offline or air-gapped.
*(per TS 102 042 clause 7.4.4 and BRG section 16.5(1))*

#### 7.4.5 Operations Management
> *The CA **shall** ensure systems are secure and correctly operated with minimal risk of failure.*

Auditors **should** check:
- Multi-factor authentication implemented where supported.
- Detection/prevention controls against viruses and malware.
- Monitoring and reporting of security-related configuration changes.
- Logs maintained, archived, retained per legislation and business practices.
- Timely acquisition of security problem information (e.g., from CSIRTs).
- Prevention of media obsolescence (test media before decay).
- Timely installation of security patches (within 6 months).
- Definition of "security incident" for staff guidance.
- Periodic (e.g., yearly) reporting to management.
*(per TS 102 042 clause 7.4.5 and BRG sections 15.2, 16.5(4)(5))*

#### 7.4.6 System Access Management
> *The CA **shall** ensure that system access is limited to properly authorized individuals.*

Auditors **should** verify (per TS 102 042 clause 7.4.6):
- Same security controls to all systems co-located in same zone.
- CA systems maintained in secure zone.
- Security support systems configured to protect communications.
- Network controllers (firewalls) configured to support only necessary services; use of security baselines.
- Weekly review of system configurations.
- Only trusted roles granted administration access; up-to-date list of persons and access levels.
- Trusted roles log out/lock workstations when not in use; inactivity time-outs.
- System accounts reviewed every 90 days; deactivate unnecessary.
- Automated mechanism to process logs and alert personnel.
- Account lockout after no more than five failed attempts.
- Annual penetration test (or after upgrades) by independent skilled entity.
- Procedure to remediate/mitigate critical vulnerabilities within 96 hours.

#### 7.4.7 Trustworthy Systems Deployment and Maintenance
> *The CA **shall** use trustworthy systems and products protected against modification.*

Auditors **should** check per TS 102 042 clause 7.4.7 and BRG section 16.5(2).

#### 7.4.8 Business Continuity Management and Incident Handling
> *The CA **shall** ensure in the event of a disaster (including CA private key compromise), operations are restored as soon as possible.*

Auditors **should** check existence of a business continuity plan covering private key compromise per TS 102 042 clause 7.4.8 and BRG section 16.4.

#### 7.4.9 CA Termination
> *The CA **shall** ensure potential disruptions to subscribers and relying parties are minimized and records continued for legal proceedings.*

Auditors **should** check procedures per TS 102 042 clause 7.4.9.

#### 7.4.10 Compliance with Legal Requirements
> *The CA **shall** ensure compliance with legal requirements.*

Auditors **should** check per TS 102 042 clause 7.4.10 (including Data Protection Directive) and BRG section 8.1.

#### 7.4.11 Recording of Information Concerning Certificates
> *The CA **shall** ensure all relevant information concerning a certificate is recorded for an appropriate period, especially for legal proceedings.*

- Auditors **should** check records retained per BRG section 15 and TS 102 042 clauses 7.4.11, 7.3.1.
- Records **must** be retained at least 7 years after certificate ceases to be valid (BRG section 15.3). National legal requirements also apply.

### 7.5 Organizational
> *The CA **shall** ensure that its organization is reliable.*

Auditors **should** check per TS 102 042 clause 7.5.

### 7.6 Additional Requirements
#### 7.6.1 Testing
Auditors **should** check availability of testing web pages per BRG Appendix C.

#### 7.6.2 Cross Certificates
Auditors **should** check disclosure of all Cross Certificates per BRG section 8.4.

## 8 Framework for the Definition of Other Certificate Policies
### 8.1 Certificate Policy Management
> *The authority issuing the certificate policy **shall** ensure the policy is effective.*
Auditors **should** check per TS 102 042 clause 8.1.

### 8.2 Additional Requirements
> *Subscribers and relying parties **shall** be informed as part of implementing clause 7.3.4.*
Auditors **should** check per TS 102 042 clause 8.2.

### 8.3 Conformance
> *The CA **shall** only claim conformance to the present document and the applicable certificate policy.*
Auditors **should** check that the CA claims conformance to TS 102 042 and BRG.

---

## Requirements Summary (Key “shall” statements from TS 102 042 and BRG referenced)

| ID | Requirement (from TS 102 042 / BRG) | Type | Reference |
|---|---|---|---|
| R1 | CA **shall** include policy identifier(s) in terms and conditions. | shall | TS 102 042 5.2 |
| R2 | CA **shall** implement controls meeting requirements in Section 7. | shall | TS 102 042 7 (intro) |
| R3 | CA **shall** ensure evidence of subscriber/subject identification is examined and certificate requests are accurate, authorized, complete. | shall | TS 102 042 7.3.1 |
| R4 | CA **shall** ensure requests for certificates to previously registered subjects are complete, accurate, authorized. | shall | TS 102 042 7.3.2 |
| R5 | CA **shall** issue certificates securely to maintain their authenticity. | shall | TS 102 042 7.3.3 |
| R6 | CA **shall** ensure terms and conditions are made available to subscribers and relying parties. | shall | TS 102 042 7.3.4 |
| R7 | CA **shall** ensure certificates are made available as necessary. | shall | TS 102 042 7.3.5 |
| R8 | CA **shall** ensure certificates are revoked in a timely manner based on authorized requests. | shall | TS 102 042 7.3.6 |
| R9 | CA **shall** ensure CA private keys remain confidential and integral (key storage). | shall | TS 102 042 7.2.2 |
| R10 | CA **shall** ensure CA private signing keys not used beyond end of life cycle. | shall | TS 102 042 7.2.6 |
| R11 | CA **shall** ensure security of cryptographic hardware throughout lifecycle. | shall | TS 102 042 7.2.7 |
| R12 | CA **shall** ensure subject keys (if generated by CA) are generated securely and secrecy assured. | shall | TS 102 042 7.2.8 |
| R13 | CA **shall** ensure administrative/management procedures adequate and recognized. | shall | TS 102 042 7.4.1 |
| R14 | CA **shall** ensure assets and information receive appropriate protection. | shall | TS 102 042 7.4.2 |
| R15 | CA **shall** ensure personnel/hiring practices enhance trustworthiness. | shall | TS 102 042 7.4.3 |
| R16 | CA **shall** ensure physical access to critical services controlled and risks minimized. | shall | TS 102 042 7.4.4 |
| R17 | CA **shall** ensure systems secure and correctly operated with minimal risk. | shall | TS 102 042 7.4.5 |
| R18 | CA **shall** ensure system access limited to properly authorized individuals. | shall | TS 102 042 7.4.6 |
| R19 | CA **shall** use trustworthy systems and products protected against modification. | shall | TS 102 042 7.4.7 |
| R20 | CA **shall** ensure in event of disaster operations restored as soon as possible. | shall | TS 102 042 7.4.8 |
| R21 | CA **shall** ensure potential disruptions minimized on cessation of services and records maintained. | shall | TS 102 042 7.4.9 |
| R22 | CA **shall** ensure compliance with legal requirements. | shall | TS 102 042 7.4.10 |
| R23 | CA **shall** ensure all relevant certificate information recorded for appropriate period. | shall | TS 102 042 7.4.11 |
| R24 | CA **shall** ensure its organization is reliable. | shall | TS 102 042 7.5 |
| R25 | Policy authority **shall** ensure policy is effective. | shall | TS 102 042 8.1 |
| R26 | Subscribers/rlying parties **shall** be informed (as part of 7.3.4). | shall | TS 102 042 8.2 |
| R27 | CA **shall** only claim conformance to the document and applicable policy. | shall | TS 102 042 8.3 |

## Informative Annexes (Condensed)
- **Annex A (Assessment Guidance Checklist)**: Provides a tabular checklist mapping each clause of this TR to TS 102 042 and BRG requirements, with guidance for auditors. It includes a findings column for recording compliance (OK/Not OK). The checklist covers clauses 5.1 through 8.3. Auditors may reproduce the checklist freely for audit purposes.

- **Annex B (Audit Report Framework)**: Suggests topics for inclusion in the final audit report, such as: statutory environment, list of documents submitted/evaluated, auditor’s statement on audit conditions, overall compliance evaluation, detailed per-clause evaluation (verified/not verified, outcomes with severity levels 1–3, recommendations), and suggested next audit date. The guidance is non-binding but aims to facilitate cross-evaluation of CAs.