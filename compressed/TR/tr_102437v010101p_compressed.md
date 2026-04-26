# ETSI TR 102 437: Guidance on TS 101 456 (Policy Requirements for certification authorities issuing qualified certificates)
**Source**: ETSI Security (SEC) | **Version**: V1.1.1 | **Date**: 2006-10 | **Type**: Technical Report (Guidance)
**Original**: http://www.etsi.org – ETSI TR 102 437

## Scope (Summary)
This Technical Report provides guidance on interpreting the requirements of TS 101 456 (V1.4.1) for bodies that supervise, approve, or accredit CAs, assessors, certification service providers, and other interested parties. It facilitates assessors in evaluating CA compliance and CAs in implementing TS 101 456 requirements. The original text of TS 101 456 is quoted verbatim in italics.

## Normative References
- Directive 1999/93/EC on a Community framework for electronic signatures ("the Directive")
- IETF RFC 3647 (2003): Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework
- ITU-T X.509 (2000) | ISO/IEC 9594-8 (2001)
- Directive 95/46/EC on data protection
- FIPS PUB 140-2 (2001); FIPS 140-1 acceptable as valid alternative
- ETSI TS 101 862: Qualified certificate profile
- ISO/IEC 15408 (2005) (parts 1-3)
- CEN Workshop Agreement 14167-1, -2, -3, -4
- Directive 93/13/EEC on unfair terms in consumer contracts
- ISO/IEC 17799 (2005)
- ETSI TS 102 158: Policy requirements for attribute certificates
- ETSI TS 101 456 (V1.4.1)
- ETSI TS 102 176-1 and TS 102 176-2
- CWA 14172-2 and CWA 14172-3
- IETF RFC 2119, RFC 4210, RFC 4211
- PKCS #5 v2.0
- TTP.NL Parts 1, 2, 3
- "Scheme approval profiles for Trust Service Providers"
- ITU-T X.843 | ISO/IEC 15945, X.842 | ISO/IEC 14516
- ISO/IEC TR 13335-1 to -4
- ANSI X9.79, X9.17
- Commission Decision 2000/709/EC
- NIST SP 800-57
- CWA 14169

## Definitions and Abbreviations
- **Definitions**: Terms defined in TS 101 456 apply. See clause 4 for general concepts.
- **Abbreviations**: TS 101 456 abbreviations apply, plus: **CM** – Cryptographic module.
- **Additional terms**: This TR uses "should" for guidance (not mandatory). Requirements derived from TS 101 456 are indicated as "SHALL".

## 4 General Concepts
Refer to TS 101 456. Guidance on CA assessment: see CWA 14172-2 section 3.4 for requirements on independent bodies, assessors, and assessment teams.

**Best practice**: At least one assessor must have knowledge of legislative/regulatory requirements and legal compliance. Separate assessments of service components require availability of reports and verification of compliance.

## 5 Introduction to Qualified Certificate Policies
### 5.1 Overview
- **Qualified certificate policies** (QCPs) defined in TS 101 456:
  1. QCP public + SSCD (for use with secure-signature-creation devices)
  2. QCP public (without SSCD requirement)
- Clause 8 defines framework for other QCPs (closed groups or enhanced policies).

**Guidance**: "Public" interpreted per national legislation. CA considered issuing to public if certificates not restricted by voluntary private law agreements.

### 5.2 Identification
- **OID for QCP public + SSCD**: `itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(1456) policy-identifiers(1) qcp-public-with-sscd (1)`
- **OID for QCP public**: `itu-t(0) identified-organization(4) etsi(0) qualified-certificate-policies(1456) policy-identifiers(1) qcp-public (2)`
- CA must include OID in certificate and terms & conditions.

**Guidance (TS 101 456)**: An `esi4-qcStatement-1` extension SHOULD be present for certificates before July 2005, SHALL be present after. Assessors should verify implementation after June 2005.

**Additional Guidance**: If CA adopts QCP+SSCD or QCP public, corresponding OID must be included in certificates.

### 5.3 User Community and Applicability
#### 5.3.1 QCP public + SSCD
- Certificates meet Annex I of Directive, issued by CA complying with Annex II, used only with SSCD meeting Annex III, issued to the public.
- Supports electronic signatures legally equivalent to hand-written signatures (Art. 5.1).

#### 5.3.2 QCP public
- Same as above but without SSCD requirement.
- Supports electronic signatures not denied legal effectiveness (Art. 5.2).

### 5.4 Conformance
#### 5.4.1 General
- CA shall use policy identifier only if:
  a) Claims conformance and provides evidence on request (e.g., auditor report, may be internal but without hierarchical relationship); or
  b) Has current independent assessment; results made available on request; or
  c) If non-conformant significantly affects ability to meet Directive requirements, shall cease issuing and remedy within reasonable period.

**Guidance**: Certificates for testing allowed even if non-conformant, provided not made available for other uses.

**Additional Guidance**: Conformance checked annually; full reassessment first after 3 years then every 4 years. CA should keep history of security incidents.

#### 5.4.2 QCP public + SSCD
Conformant CA must demonstrate: a) Obligations per clause 6.1; b) Controls meeting all clause 7 requirements.

#### 5.4.3 QCP public
Same as above, but exclude clause 7.2.9 and subscriber obligations 6.2(e) and (f).

**Additional Guidance**: Transition from TS 101 456 V1.2.1 to V1.4.1 considered equivalent; assessment against latest version at next full reassessment.

## 6 Obligations and Liability
### 6.1 Certification Authority Obligations
- CA shall implement all applicable requirements of clause 7.
- CA responsible for conformance even when subcontracting.
- CA shall provide services consistent with CPS.

**Additional Guidance**: When subcontracted, CA must demonstrate conformance (e.g., through contracts and third-party reports). When not subcontracted, define process descriptions.

### 6.2 Subscriber Obligations
CA shall oblige subscriber (via agreement) to:
- a) Submit accurate and complete registration information.
- b) Use key pair only for electronic signatures and within limitations.
- c) Exercise reasonable care to avoid unauthorized use of private key.
- d) If subscriber/subject generates keys: use fit algorithm and key length; subject's private key under sole control.
- e) (For QCP public+SSCD) Use only with SSCD.
- f) (For QCP public+SSCD) Keys generated within SSCD.
- g) Notify CA without reasonable delay of loss, theft, compromise, or changes.
- h) Immediately discontinue use upon compromise.
- i) Discontinue use if CA compromised.

**Additional Guidance**: Assessor should check contracts; reasonable delay defined; use of SSCD must be tested and certified by Notified Bodies.

### 6.3 Information for Relying Parties
Terms & conditions must include notice that relying party shall:
- a) Verify validity/suspension/revocation using current status.
- b) Consider usage limitations.
- c) Take other prescribed precautions.

**Guidance (TS 101 456)**: Revocation information may have up to 1 day delay. Parties who "reasonably rely" are those to whom an object signed with certificate is relevant.

### 6.4 Liability
CAs liable per Article 6 of Directive. Shall not add clauses contrary to that liability.

**Additional Guidance**: Assessor should verify liability clauses comply with applicable law consistent with Article 6.

## 7 Requirements on CA Practice
### 7.1 Certification Practice Statement
- a) CA shall have CPS addressing all QCP requirements.
- b) CPS shall identify obligations of external organizations.
- c) CPS and relevant documentation available to subscribers and relying parties.
- d) Terms & conditions disclosed per 7.3.4.
- e) High-level management body approves CPS.
- f) Senior management ensures proper implementation.
- g) Review process defined, responsibilities maintained.
- h) Notice of CPS changes given; revised CPS made available.
- i) Document signature algorithms and parameters.

**Additional Guidance**: CPS completeness; recommendation to structure per RFC 3647.

### 7.2 Public Key Infrastructure – Key Management Life Cycle
#### 7.2.1 Certification Authority Key Generation
- CA keys generated in physically secure environment, by trusted roles under dual control, minimal personnel.
- Key generation device must meet FIPS 140-2 level 3 or higher, or CWA 14167-2/3/4, or CC EAL 4+.
- Algorithm and key length fit for purpose.
- Generate new key pair before expiration; avoid disruption.

**Additional Guidance**: Document root key ceremony; test script; third-party opinion; verify cryptographic module certification.

#### 7.2.2 CA Key Storage, Backup and Recovery
- CA private signing key held and used in secure device (FIPS 140-2 level 3+, CWA, or CC EAL4+).
- When outside device, same level of protection.
- Backup only by trusted roles, dual control, physically secure.
- Backup copies subject to same or greater security.
- Keys in hardware module not accessible outside.

**Additional Guidance**: Backup security; export of private key under random key of at least 90 bits.

#### 7.2.3 CA Public Key Distribution
- Public key distributed with integrity and authenticity (e.g., self-signed certificate with additional verification, fingerprint publication).

**Additional Guidance**: Use of CD-ROM, WORM, published hash; verify cryptographic correctness.

#### 7.2.4 Key Escrow
- Subject private signing keys shall not be held in backup decryption capability (key escrow) – per Annex II(j).

#### 7.2.5 CA Key Usage
- CA signing key may also sign CRLs and other certificate types; shall only be used within physically secure premises.

**Additional Guidance**: Key usage limited to certificate signing and CRL signing; not for other services.

#### 7.2.6 End of CA Key Life Cycle
- All copies of CA private signing keys destroyed or put beyond use.

**Additional Guidance**: Detailed script, dual control, destruction report and archive.

#### 7.2.7 Life Cycle Management of Cryptographic Hardware
- CA shall ensure hardware not tampered during shipment/storage; activation/backup/recovery under dual control; functioning correctly; keys destroyed upon retirement.

**Additional Guidance**: "No lone" zone; testing; event logging.

#### 7.2.8 CA Provided Subject Key Management Services
- If CA generates subject keys: algorithm and key length fit for purpose; generated and stored securely; delivered with secrecy/integrity; copies destroyed after delivery.

#### 7.2.9 Secure-Signature-Creation Device Preparation
- **Not applicable for QCP public**.
- If CA issues SSCD: secure preparation, storage, distribution; deactivation/reactivation controlled; activation data separate from device.
- Protection profile CWA 14169 can be used.

### 7.3 PKI – Certificate Management Life Cycle
#### 7.3.1 Subject Registration
- Before contract, inform subscriber of terms and conditions via durable means and understandable language.
- Verify identity by appropriate means (physical or equivalent assurance); record all verification information.
- Subject evidence: full name, date/place of birth or national identity number.
- For association with legal person: additional evidence of legal status and association.
- Subscriber must provide contact address.
- Signed agreement recorded including subscriber obligations, consent to record keeping, publication conditions.
- Records retained per applicable law.

**Additional Guidance**: "Appropriate means" includes verification against valid ID; indirect verification must provide equivalent assurance.

#### 7.3.2 Certificate Renewal, Rekey and Update
- Check existing certificate validity and identity/attribute validity.
- If terms changed, communicate and obtain agreement.
- If attributes changed or previous revoked, re-verify.
- New certificate with same public key only if cryptographic security still sufficient and no compromise indication.

#### 7.3.3 Certificate Generation
- Certificates meet Annex I requirements: indication as qualified, CA identification, name/pseudonym, specific attributes, signature-verification data, validity period, identity code, advanced signature, limitations.
- Take measures against forgery; keep confidentiality during key generation.
- Securely link certificate generation to registration/renewal/rekey.
- Ensure uniqueness of distinguished name.
- Protect registration data confidentiality/integrity during exchange.
- Authenticate registration service providers.

#### 7.3.4 Dissemination of Terms and Conditions
- Make available to subscribers and relying parties: QCP applied, limitations, subscriber obligations, validation info, liability limitations, record retention periods, complaint procedures, legal system, conformance status.
- Available via durable means, readily understandable.
- Model PKI Disclosure Statement (PDS) may be used.

#### 7.3.5 Certificate Dissemination
- Upon generation, certificate available to subscriber/subject.
- Certificates available for retrieval only with subject's consent.
- Terms and conditions readily identifiable.
- Information available 24/7; maximum downtime specified in CPS.
- Publicly and internationally available.

#### 7.3.6 Certificate Revocation and Suspension
- Document revocation procedures in CPS: who may request, how, confirmation requirements, suspension reasons, mechanism, maximum delay (at most 1 day).
- Process revocation requests on receipt; authenticate and check authorization.
- Suspension only as long as necessary to confirm status.
- Inform subject/subscriber of change.
- Once definitively revoked, not reinstated.
- CRLs published at least daily; state next issue time; signed by CA.
- Revocation management services 24/7; maximum downtime in CPS.
- Revocation status information 24/7, integrity and authenticity protected, publicly internationally available, until certificate expiry.

**Additional Guidance**: The 1-day delay includes entire process; logging required; authentication via passphrase/PIN, signed document, or physical presence.

### 7.4 CA Management and Operation
#### 7.4.1 Security Management
- Carry out risk assessment; regularly reviewed.
- Retain responsibility even if outsourced; define third-party responsibilities.
- High-level steering forum for information security policy.
- System for quality and information security management.
- Maintain security infrastructure; changes approved by management.
- Document security controls and operating procedures.
- Maintain security when functions outsourced.

**Additional Guidance**: Formal ISMS; information security officer; regular internal audits; risk analysis annually.

#### 7.4.2 Asset Classification and Management
- Maintain inventory of information assets; assign classification based on risk analysis.
- Security controls for assets consistent with classification.

**Additional Guidance**: Define classification methodology (CIA); document ownership; mark assets when possible.

#### 7.4.3 Personnel Security
- Employ sufficient qualified personnel; formal training and credentials.
- Disciplinary sanctions for policy violations.
- Document security roles; identify trusted roles.
- Job descriptions define separation of duties and least privilege.
- Personnel in trusted roles free from conflicting interests.
- Trusted roles: Security Officers, System Administrators, Operators, Auditors.
- Formal appointment to trusted roles by senior management.
- No person with conviction for serious crime; checks before granting access.

**Additional Guidance**: Signed confidentiality statements; independence statements; periodic review of trustworthiness.

#### 7.4.4 Physical and Environmental Security
- Limit physical access to facilities for certificate generation, SSCD preparation, revocation management.
- Control to avoid loss, damage, theft, interruption.
- Physically secure environment; no lone zone; security perimeters.
- Address natural disaster, fire, utilities failure, etc.
- Equipment/media not taken off-site without authorization.

**Additional Guidance**: Document security zones; access control systems; regular review.

#### 7.4.5 Operations Management
- Protect systems from viruses, malicious software.
- Minimize damage via incident reporting and response.
- Secure media handling; protect against obsolescence.
- Document procedures for trusted and administrative roles.
- Monitor capacity; ensure processing power and storage.
- Incident response timely; audit logs monitored regularly.

**Additional Guidance**: Security operations separated from normal operations; procedures for all critical operations.

#### 7.4.6 System Access Management
- Implement firewalls to protect internal network.
- Protect sensitive data (e.g., registration) from unauthorized access; use encryption when exchanged over insecure networks.
- Effective user account management; timely modification/removal.
- Restrict access per access control policy; separate roles.
- Identify and authenticate personnel before using critical applications.
- Accountability via event logs.
- Protect against re-used storage objects.
- Monitor and alarm for unauthorized access.

#### 7.4.7 Trustworthy Systems Deployment and Maintenance
- Use trustworthy systems protected against modification (e.g., CWA 14167-1 or CC protection profiles).
- Security requirements analysis at design stage.
- Change control for software.

**Additional Guidance**: Hardening of systems; regular monitoring; logging.

#### 7.4.8 Business Continuity Management and Incident Handling
- Define and maintain continuity plan for disaster (including key compromise).
- Back up CA systems data necessary to resume operations; store safely.
- Back-up/restore performed by trusted roles.
- CA key compromise treated as disaster; inform subscribers, relying parties, other CAs; indicate certificates/revocation status may be invalid.
- Algorithm compromise: inform all; revoke affected certificates.

**Additional Guidance**: Plan should specify timeframes; notification mechanisms (email, website, hotline).

#### 7.4.9 CA Termination
- Before termination: inform affected parties; terminate subcontractors; transfer obligations for records; destroy private keys.
- Arrangement to cover costs if bankrupt.
- State termination provisions in practices.

#### 7.4.10 Compliance with Legal Requirements
- Meet statutory requirements for records protection.
- Comply with Data Protection Directive; take technical/organizational measures against unauthorized processing.
- Protect user information from disclosure without consent or legal authorization.

#### 7.4.11 Recording of Information Concerning Qualified Certificates
- Maintain confidentiality and integrity of records.
- Archive completely and confidentially.
- Records available for legal proceedings; subject has access.
- Record precise time of significant events.
- Hold records for period required by applicable law.
- Event logs not easily deleted/destroyed.
- Document specific events to be logged.
- Log all registration events, key life-cycle events, certificate life-cycle events, SSCD preparation, revocation requests.

### 7.5 Organizational
- Policies non-discriminatory.
- Services accessible to all applicants within field.
- CA is a legal entity.
- Adequate arrangements to cover liabilities.
- Financial stability and resources.
- Policies for complaints and dispute resolution.
- Documented agreements for subcontracting/outsourcing.
- Certificate generation and revocation management independent from other organizations; documented structure safeguards impartiality.

**Additional Guidance**: Independence includes freedom from commercial, financial pressures. Registration authorities not required to be independent.

## 8 Framework for Other Qualified Certificate Policies
### 8.1 Policy Management
- Policy must identify basis and variances; body with authority; risk assessment; review process; CPS support; availability to users; obtain unique OID.

### 8.2 Exclusions for Non-Public QCPs
- May exclude: liability per 6.3, independence per 7.5(h)-(i), public dissemination per 7.3.5(f), public revocation status per 7.3.6(k).

### 8.3 Additional Requirements
- Inform subscribers/relying parties if policy not public, exclusions, whether SSCD required, how policy adds to or constrains.

### 8.4 Conformance
- Same conformance options as 5.4.1 (claim, independent assessment, non-conformance remedy).
- Compliance checked regularly and on major changes.
- Conformant CA must meet obligations 6.1, controls in clause 7 (excluding 7.2.9 if no SSCD, and exclusions for non-public), use policy meeting 8.1, implement additional requirements, and meet 8.3.

**Additional Guidance**: Annual checks; full reassessment every 4 years; history of incidents.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CA shall include OID in certificates and terms & conditions | SHALL | 5.2 |
| R2 | CA shall only use policy identifier if claiming conformance or assessed | SHALL | 5.4.1 |
| R3 | CA shall cease issuing if non-conformant significantly affects Directive compliance | SHALL | 5.4.1(c) |
| R4 | CA shall ensure subscriber obligations via agreement | SHALL | 6.2 |
| R5 | CA shall provide terms & conditions to relying parties | SHALL | 6.3, 7.3.4 |
| R6 | CA shall implement all clause 7 controls (with applicable exclusions) | SHALL | 7 |
| R7 | CA shall have CPS | SHALL | 7.1 |
| R8 | CA keys generated in physically secure environment, dual control, qualified device | SHALL | 7.2.1 |
| R9 | CA private signing key stored in secure device; backup under dual control | SHALL | 7.2.2 |
| R10 | Subject private keys shall not be escrowed | SHALL | 7.2.4 |
| R11 | CA signing key used only for certificate/CRL signing within secure premises | SHALL | 7.2.5 |
| R12 | All copies of CA private keys destroyed at end of life | SHALL | 7.2.6 |
| R13 | Cryptographic hardware lifecycle protected; dual control for activation | SHALL | 7.2.7 |
| R14 | Subject keys if CA-generated: fit algorithm, secure delivery, no copies | SHALL | 7.2.8 |
| R15 | SSCD preparation controlled, secure distribution, activation data separate | SHALL | 7.2.9 (if applicable) |
| R16 | Subject identity verified by appropriate means; evidence recorded | SHALL | 7.3.1 |
| R17 | Certificate content per Annex I | SHALL | 7.3.3 |
| R18 | Certificate distinguished name unique | SHALL | 7.3.3(e) |
| R19 | Terms & conditions disseminated; revocation procedure with ≤1 day delay | SHALL | 7.3.4, 7.3.6 |
| R20 | Certificate dissemination with subject consent; 24/7 availability | SHALL | 7.3.5 |
| R21 | Revocation service 24/7; CRL publish at least daily; status info publicly available | SHALL | 7.3.6 |
| R22 | Risk assessment performed and regularly reviewed | SHALL | 7.4.1 |
| R23 | Asset inventory and classification | SHALL | 7.4.2 |
| R24 | Personnel in trusted roles free from conflict; background checks | SHALL | 7.4.3 |
| R25 | Physical security perimeters; no lone zone | SHALL | 7.4.4 |
| R26 | Incident reporting and response procedures | SHALL | 7.4.5 |
| R27 | Network perimeter controls; sensitive data encryption | SHALL | 7.4.6 |
| R28 | Trustworthy systems used; security requirements at design | SHALL | 7.4.7 |
| R29 | Business continuity plan; key compromise as disaster | SHALL | 7.4.8 |
| R30 | CA termination: inform, transfer records, destroy keys, cost arrangement | SHALL | 7.4.9 |
| R31 | Compliance with data protection and legal requirements | SHALL | 7.4.10 |
| R32 | Records confidentiality, integrity, retention per law; event logging | SHALL | 7.4.11 |
| R33 | Policies non-discriminatory; CA legal entity; financial stability | SHALL | 7.5 |
| R34 | Independence of certificate generation and revocation from other organizations | SHALL | 7.5(h)-(i) |
| R35 | For non-public QCPs: additional policy management requirements | SHALL | 8 |

## Informative Annexes (Condensed)
- **Annex A (Liability)**: Provides further guidance on liability obligations under Article 6 of the Directive. (Referenced in clause 6.4)
- **Annex B (Model PKI Disclosure Statement)**: A model for communicating terms and conditions to subscribers and relying parties. (Referenced in clauses 7.3.1 and 7.3.4)
- **Annex C (Bibliography)**: Lists additional guidance documents (e.g., ISO standards, other CWA). Not reproduced here.
- **Annex D (Cross-reference list)**: Maps TS 101 456 requirements to RFC 2527/3647 framework for CPS structure. (Referenced in 7.1, best practice)