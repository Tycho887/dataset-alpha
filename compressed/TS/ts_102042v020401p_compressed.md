# ETSI TS 102 042 V2.4.1 (2013-02)
**Source**: ETSI | **Version**: V2.4.1 | **Date**: 2013-02 | **Type**: Normative
**Original**: ETSI TS 102 042, Electronic Signatures and Infrastructures (ESI); Policy requirements for certification authorities issuing public key certificates

## Scope (Summary)
This document specifies policy requirements for Certification Authorities (CAs) issuing public key certificates, including Extended Validation Certificates (EVC) and Publicly trusted TLS/SSL certificates (PTC). It defines six reference certificate policies (LCP, NCP, NCP+, EVCP, EVCP+, DVCP, OVCP) and a framework for defining others, covering operation and management practices to provide confidence in certificates supporting cryptographic mechanisms.

## Normative References
- [1] CENELEC EN 45011: General requirements for bodies operating product certification systems
- [2] FIPS PUB 140-1: Security Requirements for Cryptographic Modules
- [3] FIPS PUB 140-2 (2001): Security Requirements for Cryptographic Modules
- [4] ISO/IEC 15408 (parts 1 to 3): Evaluation criteria for IT security
- [5] CWA 14167-1: Security Requirements for Trustworthy Systems Managing Certificates – Part 1
- [6] CWA 14167-2 (2004): Cryptographic Module for CSP signing operations with backup – Protection profile
- [7] CWA 14167-3 (2004): Cryptographic module for CSP key generation services protection profile
- [8] CWA 14167-4 (2004): Cryptographic module for CSP signing operations – Protection profile
- [9] ISO/IEC 9594-8/Recommendation ITU-T X.509
- [10] ISO/IEC 17021: Conformity assessment – Requirements for bodies providing audit and certification of management systems
- [11] ISO/IEC 27002 (2005): Code of practice for information security management
- [12] IETF RFC 3647: Certificate Policy and Certification Practices Framework
- [13] ETSI TS 102 158: Policy requirements for Certification Service Providers issuing attribute certificates
- [14] ETSI TS 102 176-1: Algorithms and Parameters for Secure Electronic Signatures; Part 1
- [15] ETSI TS 101 456: Policy requirements for certification authorities issuing qualified certificates
- [16] CA/Browser Forum: Guidelines for The Issuance and Management of Extended Validation Certificates version 1.3
- [17] IETF RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile
- [18] IETF RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- [19] CA/Browser Forum: Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates
- [20] CA/Browser Forum: Network and Certificate System Security Requirements

## Definitions and Abbreviations
- **certificate**: public key of a user, together with some other information, rendered un-forgeable by encipherment with the private key of the certification authority which issued it
- **certificate policy**: named set of rules that indicates the applicability of a certificate to a particular community and/or class of application with common security requirements
- **Certification Authority (CA)**: authority trusted by one or more users to create and assign certificates
- **certification practice statement (CPS)**: statement of the practices which a CA employs in issuing, managing, revoking, and renewing or re-keying certificates
- **EV certificate (EVC)**: certificate issued and maintained in compliance with EVCP or EVCP+
- **EVCP**: NCP enhanced to incorporate requirements in EVCG [16]
- **EVCP+**: EVCP requiring use of a secure user device
- **LCP**: Lightweight Certificate Policy (less onerous quality)
- **NCP**: Normalized Certificate Policy (quality equivalent to qualified certificate policy, no secure user device required)
- **NCP+**: NCP requiring use of a secure user device
- **DVC**: Domain Validation Certificate (identifies subject only by domain name)
- **DVCP**: NCP enhanced incorporating requirements of BRG [19] for domain validated certificates
- **OVC**: Organizational Validation Certificate (includes validated organizational identity)
- **OVCP**: NCP enhanced incorporating BRG [19] for organizational validated certificates
- **PTC**: Publicly-trusted Certificate (trust anchor distribution in widely-available application software)
- **PTC-BR**: publicly trusted certificates incorporating BRG [19] (includes OVCP and DVCP)
- **relying party**: recipient of a certificate who acts in reliance on that certificate and/or digital signatures verified using that certificate
- **secure user device**: device holding user's private key, protects against compromise, performs signing/decryption functions
- **subject**: entity identified in a certificate as holder of private key
- **subscriber**: entity subscribing with a CA on behalf of one or more subjects
- **Abbreviations**: BRG, CA, CAB, CPS, CRL, DNS, EAL, EV, IT, LCP, MLA, NCP, OCSP, PDS, PKI, RA, TLS/SSL

## Notation
- Unmarked clauses: mandatory requirements strictly to be followed.
- [CONDITIONAL]: requirements applicable if relevant to services offered.
- Markings like [LCP], [NCP], [NCP+], [EVCP], [EVCP+], [PTC-BR], [DVCP], [OVCP] indicate applicability to specific policies.
- [NCPetc] denotes NCP and all policies derived from NCP.
- [CHOICE] indicates multiple options; subsequent marking indicates applicable quality.
- Text copied from EVCG [16] and BRG [19] is italicised in the original.

## 5 Introduction to Certificate Policies
### 5.1 Overview
- Defines seven certificate policies: NCP, NCP+, LCP, EVCP, EVCP+, DVCP, OVCP.
- **NCP**: same quality as QCP (TS 101 456) but without legal constraints of Electronic Signature Directive; no secure user device required.
- **NCP+**: same quality as QCP but requires secure user device.
- **LCP**: less demanding policy requirements.
- **EVCP**: includes NCP requirements plus additional provisions from EVCG [16] section 7.1.2 for EVC.
- **EVCP+**: includes NCP+ requirements plus additional provisions from EVCG [16] for EVC with secure user device.
- **DVCP**: NCP enhanced with BRG [19] requirements for domain validation certificates.
- **OVCP**: NCP enhanced with BRG [19] requirements for organizational validation certificates.

### 5.2 Identification
- **NCP OID**: `itu-t(0) identified-organization(4) etsi(0) other-certificate-policies(2042) policy-identifiers(1) ncp (1)`
- **NCP+ OID**: `... ncpplus (2)`
- **LCP OID**: `... lcp (3)`
- **EVCP OID**: `... evcp (4)`
- **EVCP+ OID**: `... evcpplus (5)`
- **DVCP OID**: `... dvcp (6)`
- **OVCP OID**: `... ovcp (7)`
- Including one of these OIDs in a certificate claims conformance to that policy.

### 5.3 User Community and Applicability
- NCP, NCP+, LCP: no constraints on user community.
- **5.3.1 EV Certificates**: Purpose per EVCG [16] section 6: establish identity of legal entity controlling website, enable encrypted communications, identify source of executable code. Secondary: help address phishing, malware. Excluded: focus on identity, not behavior.
- **5.3.2 Publicly Trusted Certificates-Baseline Requirements**: PTC-BR certificates are for identifying web servers accessed via TLS/SSL.

### 5.4 Conformance
- **5.4.1 Conformance claim**: The CA shall only claim conformance if:
  - (a) It claims conformance and makes available evidence (e.g., auditor report) on request.
  - (b) It has a current assessment by a competent independent party; results available on request.
  - (c) If later shown to be significantly non-conformant, shall cease issuing certificates using the identifiers until conformant or remedy within reasonable period. (Internal/testing certificates allowed.)
  - (d) Compliance checked regularly and after major changes.
  - (e) [EVCP], [EVCP+], [PTC-BR]: CA and its Root CA shall complete point-in-time readiness assessment and period-in-time supervisory audit at least every year before issuing EVC/PTC.
- **5.4.2 Conformance requirements**: A conformant CA shall demonstrate:
  - (a) it meets obligations in clause 6.1;
  - (b) it has implemented controls meeting requirements of clause 7 as applicable to selected policy.

## 6 Obligations, Warranties and Liability
### 6.1 Certification authority obligations and warranties
- The CA shall ensure all requirements in clause 7 are implemented as applicable.
- The CA is responsible for conformance even when functions are subcontracted.
- The CA shall provide all services consistent with its CPS.

### 6.2 Subscriber obligations
- The CA shall oblige the subscriber through agreement (see 7.3.1 m) to:
  - (a) submit accurate and complete information;
  - (b) use key pair only in accordance with limitations;
  - (c) exercise reasonable care to avoid unauthorized use of private key;
  - (d) [CONDITIONAL] if subscriber/subject generates keys: use recognized algorithms and key lengths fit for purpose;
  - (e) [CONDITIONAL] if generating keys for signing, maintain private key under subject’s sole control;
  - (f) [NCP+] only use private key with secure user device;
  - (g) [NCP+] [CONDITIONAL] if keys generated under subscriber/subject, generate within secure user device;
  - (h) notify CA without reasonable delay of loss, theft, compromise, or inaccuracy/change to certificate content;
  - (i) immediately and permanently discontinue use upon compromise;
  - (j) ensure certificate not used if CA is compromised.

### 6.3 Information for relying parties
- Terms and conditions shall include notice that relying party shall:
  - (a) verify validity, suspension, or revocation using current revocation status information;
  - (b) take account of limitations on usage indicated in certificate or terms;
  - (c) take any other precautions.

### 6.4 Liability
- The CA shall specify disclaimers/limitations in accordance with applicable laws.
- [EVCP/EVCP+]: refer to EVCG [16] section 7.1.3.
- [PTC-BR]: refer to BRG [19] section 18.

## 7 Requirements on CA Practice
- The CA shall implement controls meeting the following requirements.
- Includes services: registration, certificate generation, dissemination, revocation management, revocation status, and optionally subject device provision.
- No restriction on charging.

### 7.1 Certification practice statement
- The CA shall have a CPS.
  - (a) CPS shall address all requirements of applicable policy.
  - (b) [EVCP/EVCP+]: CPS shall include items 1 and 3 from EVCG [16] sections 7.1.2 and 15.1.
  - (c) CPS shall identify obligations of external organizations.
  - (d) CPS and relevant documentation made available to subscribers and relying parties, and to assess conformance;
    - (1) to subscribers and relying parties;
    - (2) [EVCP/EVCP+]: as per EVCG [16] section 6.2.1 item 1 c);
    - (3) [PTC-BR]: as per BRG [19] section 8.2.2.
  - (e) Disclose terms and conditions per clause 7.3.4.
  - (f) High-level management body final authority for approving CPS.
  - (g) Senior management responsible for proper implementation.
  - (h) Define review process for CPS.
  - (i) Give due notice of changes; revised CPS immediately available.
  - (j) Document algorithms and parameters.
  - (k) [EVCP/EVCP+]: CA SHALL address EVCG [16] sections 7.1.3 and 15.2.
  - (l) [PTC-BR]: CA SHALL address BRG [19] sections 8.2.1, 8.2.2, and 8.3.

### 7.2 Public key infrastructure – Key management life cycle
#### 7.2.1 Certification authority key generation
- CA keys generated in controlled circumstances.
  - (a) Key generation in physically secured environment (7.4.4) by trusted roles (7.4.3) under dual control; minimal authorized personnel.
  - (b) [CHOICE]:
    - [LCP]: in product/application/device meeting FIPS 140-1/2 level 2+ or trustworthy system EAL 3+.
    - [NCPetc]: in device meeting FIPS 140-1/2 level 3+ or CWA 14167-2/3/4, or trustworthy system EAL 4+.
  - (c) Use algorithm recognized as fit for CA's signing purposes.
  - (d) Key length/algorithm fit for purpose. [EVCP/EVCP+]: EVCG appendix A applies. [PTC-BR]: BRG appendix A applies.
  - (e) Before CA signing key expiration, generate new key pair and apply actions to avoid disruption.
  - (f) [EVCP/EVCP+]: EVCG section 14.1.5 applies; for code signing, appendix H.
  - (g) [PTC-BR]: BRG section 17.7 applies.

#### 7.2.2 Certification authority key storage, backup and recovery
- CA private keys kept confidential and integral.
  - (a) [CHOICE]:
    - [LCP]: held and used in product/application/device meeting FIPS 140-1/2 level 2+ or EAL 3+.
    - [NCPetc]: held in secure cryptographic device meeting FIPS 140-1/2 level 3+ or CWA 14167-2/3/4 or EAL 4+.
  - (b) [CHOICE]:
    - [LCP]: when outside signature-creation device, secrecy ensured (physical security or encryption).
    - [NCPetc]: protected to same level as provided by signature creation device.
  - (c) Backed up, stored, recovered only by trusted roles under dual control in physically secured environment; minimal authorized personnel.
  - (d) Backup copies subject to same or greater security controls.
  - (e) If stored in hardware module, access controls prevent accessibility outside module.

#### 7.2.3 Certification authority public key distribution
- Integrity and authenticity maintained during distribution.
  - (a) CA public keys made available in manner assuring integrity and authenticating origin (e.g., self-signed certificate with additional measures like fingerprint checking).

#### 7.2.4 Key escrow
- (a) [CONDITIONAL] If subject's key for electronic signatures per Directive 1999/93/EC, CA shall not hold private signing keys for backup decryption.
- (b) [CONDITIONAL] If copy kept, CA shall ensure secrecy and only available to appropriately authorized persons.

#### 7.2.5 Certification authority key usage
- CA private signing keys not used inappropriately.
  - (a) CA signing key used for certificate generation and/or revocation status information shall not be used for any other purpose.
  - (b) Certificate signing keys only used within physically secure premises.

#### 7.2.6 End of CA key life cycle
- CA private keys not used beyond end of life.
  - (a) Use limited to compatible hash, signature algorithm, and key length per current practice (7.2.1 d).
  - (b) All copies of CA private signing keys destroyed or put beyond use at end of life.

#### 7.2.7 Life cycle management of cryptographic hardware used to sign certificates
- [NCPetc]: CA shall ensure security of cryptographic device throughout lifecycle.
  - (a) Not tampered during shipment.
  - (b) Not tampered while stored.
  - (c) Installation, activation, back-up, recovery require simultaneous control of at least two trusted employees.
  - (d) Functioning correctly.
  - (e) CA private keys destroyed upon device retirement (only physical instance).

#### 7.2.8 CA provided subject key management services
- [CONDITIONAL] If CA generates subject's keys:
  - (a) Generated using algorithm recognized as fit for uses identified.
  - (b) Key length/algorithm fit for purpose. [EVCP/EVCP+]: guidance from EVCG appendix A shall not override a) and b). [PTC-BR]: guidance from BRG appendix A.
  - (c) Generated and stored securely before delivery.
  - (d) Delivered to subject with secrecy and integrity. [PTC-BR]: BRG section 10.2.4 applies.
  - (e) [CONDITIONAL] If no copy required, private key can be maintained under subject's sole control; CA copies destroyed.

#### 7.2.9 Secure user device preparation
- [NCP+] and [EVCP+]: If CA issues secure user device, carried out securely.
  - For EV code signing, follow EVCG appendix H item 10.
  - [CONDITIONAL] If issuing:
    - (a) Securely controlled preparation.
    - (b) Securely stored and distributed.
    - (c) Deactivation/reactivation securely controlled.
    - (d) Activation data (e.g., PIN) prepared and distributed separately from device.

### 7.3 Public key infrastructure – Certificate management life cycle
#### 7.3.1 Subject registration
- CA shall ensure evidence of identification and accuracy properly examined.
  - (a) Before contract, inform subscriber of terms (7.3.4).
  - (b) [CONDITIONAL] If subject is person and not subscriber, subject informed of obligations.
  - (c) Communication through durable means, readily understandable language.
  - (d) Collect direct evidence or attestation of identity and attributes. [EVCP/EVCP+]: guidance from EVCG section 10. [PTC-BR]: guidance from BRG section 11.
  - (e) [CHOICE]:
    - [LCP]: No requirement.
    - [NCPetc]: For physical person, evidence checked directly or indirectly with equivalent assurance to physical presence.
  - (f) [CONDITIONAL] If subject is physical person: full name, date/place of birth or nationally recognized identity document.
  - (g) [CONDITIONAL] If physical person associated with legal person: full name, date/birth/identity, full name and legal status of legal person, registration info, evidence of association.
  - (h) [CONDITIONAL] If subject is organizational entity: full name (with EV guidance from EVCG sections 10.2-10.6; OVC: BRG section 11.2) and nationally recognized registration.
  - (i) [CONDITIONAL] If device/system operated by organizational entity: identifier (e.g., domain name) with EV/BRG guidance, full name of entity, nationally recognized identity number.
  - (j) Record all information necessary to verify identity and attributes.
  - (k) If subscriber and subject separate, evidence of subscriber's authority to act for subject. [EVCP/EVCP+]: EVCG section 10.7. [PTC-BR]: BRG sections 11.2.1, 11.2.2.
  - (l) Subscriber provides physical address or contact attributes. [EVCP/EVCP+]: EVCG section 10.4. [PTC-BR]: BRG section 11.2.1.
  - (m) Record signed agreement including: obligations, secure user device if required, consent to record keeping, publication conditions, confirmation of correctness.
    - [EVCP/EVCP+]: EVCG sections 10.8, 10.9.
    - [PTC-BR]: BRG section 10.3.2.
  - (n) Records retained for period indicated and as necessary for legal proceedings. [EVCP/EVCP+]: EVCG 13.2.2. [PTC-BR]: BRG 15.3.2.
  - (o) [CONDITIONAL] If key pair not generated by CA, certificate request ensures subject has possession of private key.
  - (p) Adhere to applicable data protection legislation.
  - (q) Verification policy only capture evidence sufficient for intended use.
  - (r) [EVCP/EVCP+]: CA shall abide by EVCG section 10.11.1; acceptable methods per 10.11.2.
  - (s) [EVCP/EVCP+]: Dual control per EVCG 12.1.3.
  - (t) [EVCP/EVCP+]: Subscriber satisfies EVCG 7.2.
  - (u) [EVCP/EVCP+]: Certificate requests obtain info per EVCG 9.2.
  - (v) [PTC-BR]: BRG sections 10.1, 10.2, 11.3-11.6 apply.
  - (w) [EVCP/EVCP+]: EVCG 6.2.1 items 1) and 2) apply.
  - (x) [PTC-BR]: BRG section 7.1 applies.

#### 7.3.2 Certificate renewal, rekey and update
- Requests complete, accurate, and authorized.
  - (a) Check existence and validity of certificate to be renewed; verify identity/attributes still valid.
  - (b) If terms changed, communicate and obtain agreement per 7.3.1 a), b), c), m).
  - (c) If names/attributes changed or previous revoked, registration info verified, recorded, agreed per 7.3.1 d)-l).
  - (d) New certificate using previously certified public key only if cryptographic security sufficient and no compromise indication.

#### 7.3.3 Certificate generation
- Certificates issued securely to maintain authenticity.
  - (a) Certificates shall include per X.509 and RFC 5280: CA identification and country; subject name or pseudonym; specific attribute if relevant; public key; validity period; serial number; CA electronic signature; limitations on use and value if applicable.
    - [EVCP/EVCP+]: EVCG sections 8.1, 8.2, 8.3; appendix B for SSL/TLS; appendix H for code signing.
    - [PTC-BR]: BRG section 9; appendix B for extensions.
  - (b) CA shall take measures against forgery; if generating private keys, guarantee confidentiality.
  - (c) Procedure of issuing certificate securely linked to registration or renewal.
  - (d) [CONDITIONAL] If CA generated key:
    - i) procedure securely linked to key generation;
    - ii) [LCP, NCPetc] private key securely passed to subject;
    - iii) [NCP+] secure user device securely passed.
  - (e) Distinguished name never re-assigned.
  - (f) Confidentiality and integrity of registration data protected.
  - (g) Verify registration data exchanged with recognized providers.
  - (h) Certificate issuance by root CA requires individual authorized by CA personnel management. [PTC-BR]: BRG section 12 applies.

#### 7.3.4 Dissemination of terms and conditions
- Terms and conditions made available to subscribers and relying parties.
  - (a) Include: policy applied; limitations on use; subscriber obligations (6.2); validation info; liability disclaimers; registration info retention period; event log retention period; complaints/dispute procedures; applicable legal system; conformance assessment scheme.
  - (b) Information available through durable means, readily understandable.

#### 7.3.5 Certificate dissemination
- Certificates available as necessary.
  - (a) Upon generation, complete certificate available to subscriber/subject.
  - (b) Retrieval only with subject's consent.
  - (c) Terms and conditions available to relying parties.
  - (d) Terms readily identifiable for a given certificate.
  - (e) [CHOICE]:
    - [LCP]: as specified in CPS.
    - [NCPetc]: 24/7 availability; upon failure, best endeavours to restore within maximum period in CPS.
  - (f) [CONDITIONAL] If issuing to public, publicly and internationally available.

#### 7.3.6 Certificate revocation and suspension
- Certificates revoked in timely manner based on authorized requests.
  - (a) Document procedures in CPS: who may submit, how, confirmation requirements, suspension reasons, revocation status mechanism, maximum delay between request and availability of status:
    - [LCP]: 72 hours;
    - [NCPetc]: 24 hours.
  - (b) Requests processed on receipt. [EVCP/EVCP+]: EVCG 9.3.2(5), 9.3.3(5). [PTC-BR]: BRG 10.3.2(5).
  - (c) [EVCP/EVCP+]: EVCG 11.2.1, 11.3.3. [PTC-BR]: BRG 13.1, 13.1.4.
  - (d) Requests authenticated and from authorized source.
  - (e) Suspension only while confirming; not longer than necessary.
  - (f) Subject/subscriber informed of change of status.
  - (g) Once definitively revoked, not reinstated.
  - (h) [CHOICE]:
    - [LCP]: CRLs published at least every 72 hours.
    - [NCPetc]: CRLs published at least every 24 hours.
    - [EVCP/EVCP+]: EVCG 11.1.1 items 1 and 2.
    - [PTC-BR]: BRG 13.2.
  - (i) If CRLs sole means: each states next scheduled issue; new CRL may be published before; CRL signed by CA or designated authority.
  - (j) [CHOICE]:
    - [LCP]: revocation status available as per CPS.
    - [NCPetc]: 24/7; best endeavours to restore within max period in CPS.
    - [EVCP/EVCP+]: EVCG 11.1.1.
    - [PTC-BR]: BRG 13.2.
  - (k) [EVCP/EVCP+]: EVCG 11.1.1.
  - (l) [EVCP/EVCP+]: EVCG 11.1.2.
  - (m) Response time: [EVCP/EVCP+]: EVCG 11.1.3. [PTC-BR]: BRG 13.2.3.
  - (n) Integrity and authenticity of status information protected.
  - (o) [CONDITIONAL] If issuing to public, publicly and internationally available.
  - (p) Includes status of certificates at least until expiry.
  - (q) For code signing, EV code signing: follow EVCG appendix H item 13.

### 7.4 CA management and operation
- Requirements from NetSec-CAB [20] apply.

#### 7.4.1 Security management
- Administrative and management procedures adequate.
  - (a) Carry out risk assessment, regularly reviewed. [EVCP/EVCP+]: EVCG 13.3.2. [PTC-BR]: BRG 16.2.
  - (b) CA retains responsibility even if outsourced; third parties bound to controls.
  - (c) Management provides direction on information security through high-level steering forum.
  - (d) System(s) for quality and information security management.
  - (e) Information security infrastructure maintained; changes approved by management forum.
  - (f) Security controls and operating procedures documented, implemented, maintained.
  - (g) Security maintained when functions outsourced.
  - (h) [EVCP/EVCP+]: EVCG 13.3.
  - (i) [PTC-BR]: BRG 14.2 and 16.

#### 7.4.2 Asset classification and management
- (a) Maintain inventory of information assets; assign classification consistent with risk analysis.

#### 7.4.3 Personnel security
- (a) Sufficient personnel with expert knowledge, experience, qualifications. [EVCP/EVCP+]: EVCG 12.1.1. [PTC-BR]: BRG 14.1.2.
  - (b) Disciplinary sanctions for violations.
  - (c) Security roles documented in job descriptions; trusted roles identified.
  - (d) Job descriptions defined from separation of duties and least privilege.
  - (e) Personnel exercise administrative and management procedures in line with security management.
  - (f) Managerial personnel with experience/training in electronic signature technology and security.
  - (g) Trusted roles free from conflicting interests.
  - (h) Trusted roles include: Security Officers, System Administrators, System Operators, System Auditors.
  - (i) Formal appointment to trusted roles by senior management.
  - (j) No appointment of persons known to have serious crime conviction affecting suitability; checks completed before access.
    - [EVCP/EVCP+]: EVCG 12.1.1(2)(D).
  - (k) [EVCP/EVCP+]: EVCG 12.1.2, 12.1.3.
  - (l) [PTC-BR]: BRG 14.1.

#### 7.4.4 Physical and environmental security
- (a) Physical access to critical services limited to authorized individuals.
  - (b) Controls to avoid loss, damage, compromise, interruption.
  - (c) Controls to avoid compromise or theft.
  - (d) Facilities for certificate generation, subject device preparation, revocation management in environment protecting from unauthorized access.
  - (e) Persons in secure area not left without oversight.
  - (f) Clear security perimeters around these services; no shared premises inside.
  - (g) Physical and environmental controls address access, natural disaster, fire, utilities failure, structure collapse, theft, etc.
  - (h) Controls against unauthorized off-site removal.
  - (i) [EVCP/EVCP+]: EVCG 13.3.3.
  - (j) [PTC-BR]: BRG 16.5.

#### 7.4.5 Operations management
- (a) Integrity protected against viruses, malicious and unauthorized software.
  - (b) Incident reporting and response procedures minimize damage.
  - (c) Media securely handled.
  - (d) Media management protects against obsolescence and deterioration.
  - (e) Procedures for all trusted and administrative roles.
  - (f) [PTC-BR]: BRG 16.5.
  - (g) Media handled per classification; sensitive data disposed securely.
  - (h) [CHOICE]:
    - [LCP]: no requirement.
    - [NCPetc]: capacity monitoring and forecasting.
  - (i) Timely and coordinated incident response; incidents reported as soon as possible.
  - (j) Audit processes invoked at system start up, cease only at shutdown.
  - (k) Audit logs monitored/reviewed regularly. [EVCP/EVCP+]: EVCG 11.2, 11.3.3. [PTC-BR]: BRG 15.2.
  - (l) CA security operations separated from normal operations.

#### 7.4.6 System access management
- (a) Controls (e.g., firewalls) protecting internal network from external domains.
  - (b) Sensitive data protected against unauthorized access or modification; protected when exchanged over insecure networks.
  - (c) Effective administration of user access, including account management, auditing, timely modification/removal.
  - (d) Access restricted per policy; separation of trusted roles; system utility programs restricted; access only as necessary.
  - (e) CA personnel identified and authenticated before using critical applications.
  - (f) Accountability through event logs. [EVCP/EVCP+]: EVCG 13.2.1.
  - (g) Sensitive data protected from revealing through re-used storage objects.
  - (h) [EVCP/EVCP+]: EVCG 13.1 item C.
  - (i) Local network components kept in physically secure environment; configurations periodically audited.
  - (j) Continuous monitoring and alarm facilities for unauthorized/irregular attempts.
  - (k) Dissemination application enforces access control on adding/deleting/modifying certificates.
  - (l) Continuous monitoring and alarm for revocation management.
  - (m) Revocation status application enforces access control on modifying status.

#### 7.4.7 Trustworthy systems deployment and maintenance
- (a) Analysis of security requirements at design and requirements stage.
  - (b) Change control procedures for releases, modifications, emergency fixes.

#### 7.4.8 Business continuity management and incident handling
- (a) Define and maintain a continuity plan.
  - (b) Backup and store CA systems data in safe places for timely recovery.
  - (c) Backup/restore performed by relevant trusted roles.
  - (d) Business continuity plan addresses compromise or suspected compromise of CA private signing key.
  - (e) After disaster, take steps to avoid repetition.
  - (f) In case of compromise, provide: inform subscribers, entities with agreements, relying parties and CAs; indicate certificates and revocation status information may no longer be valid.
  - (g) If algorithm becomes insufficient: inform subscribers and relying parties; revoke affected certificates.

#### 7.4.9 CA termination
- (a) Before termination:
    - i) inform subscribers, entities with agreements, relying parties, CAs; make information available;
    - ii) terminate subcontractor authorizations;
    - iii) transfer obligations for maintaining records (registration, revocation, event logs) for their respective periods;
    - iv) destroy or withdraw private keys per 7.2.6.
  - (b) Arrangement to cover costs in case of bankruptcy or inability.
  - (c) State in practices provisions for termination: notification, transfer of obligations, handling revocation status for unexpired certificates.

#### 7.4.10 Compliance with legal requirements
- (a) Meet statutory requirements for protecting records.
  - (b) Meet applicable data protection legislation (e.g., Directive 95/46/EC).
  - (c) Appropriate technical and organizational measures against unauthorized processing, accidental loss/destruction.
  - (d) User information protected from disclosure without consent or legal authorization.

#### 7.4.11 Recording of information concerning certificates
- (a) Confidentiality and integrity of records maintained.
  - (b) Records completely and confidentially archived per disclosed practices.
  - (c) Records available for legal proceedings subject/data protection; subject/subscriber access to their info.
  - (d) Precise time of significant events recorded.
  - (e) Records held per terms and conditions (7.3.4) and applicable legislation. [EVCP/EVCP+]: EVCG 13.2.1, 13.2.2. [PTC-BR]: BRG 15.3.
  - (f) Events logged in a way not easily deleted/destroyed within holding period.
  - (g) Specific events and data to be logged documented. [EVCP/EVCP+]: EVCG 13.1. [PTC-BR]: BRG 15.1, 15.2.
  - (h) All registration events logged.
  - (i) Registration information recorded: type of documents, identification data, storage location, choices in agreement, identity of acceptor, validation method, name of receiving CA/RA.
  - (j) Privacy of subject information maintained.
  - (k) Log all events relating to CA key lifecycle.
  - (l) Log all events relating to certificate lifecycle.
  - (m) Log all events relating to key lifecycle for keys managed by CA.
  - (n) If applicable, log events relating to secure user device preparation.
  - (o) Log all revocation requests/reports and resulting action.

### 7.5 Organizational
- (a) Policies and procedures non-discriminatory.
  - (b) Services accessible to all applicants within declared field.
  - (c) CA is a legal entity per national law.
  - (d) Adequate arrangements to cover liabilities.
  - (e) Financial stability and resources to operate conformantly.
  - (f) Policies for resolution of complaints and disputes.
  - (g) Properly documented agreement for subcontracting/outsourcing.
  - (h) Parts of CA concerned with certificate generation and revocation management independent in decisions; senior staff free from pressures.
  - (i) Documented structure safeguarding impartiality.

### 7.6 Additional requirements
#### 7.6.1 Additional testing
- CA shall provide options for third parties to check and test certificates. [PTC-BR]: BRG appendix C applies.

#### 7.6.2 Cross certificates
- CA shall disclose all cross certificates that identify the CA as subject. [PTC-BR]: BRG section 8.4 applies.

## 8 Framework for the definition of other certificate policies
### 8.1 Certificate policy management
- (a) Identify which policies defined here it adopts as basis, plus variances.
  - (b) Body with final authority for specifying/approving the policy.
  - (c) Risk assessment for stated community and applicability.
  - (d) Approval and modification per defined review process.
  - (e) Defined review process to ensure policy supported by CPS.
  - (f) Make policy available to user community.
  - (g) Revisions made available to subscribers and relying parties.
  - (h) Policy incorporates or constrains all requirements of clauses 6 and 7.
  - (i) Unique object identifier obtained per X.509.

### 8.2 Additional requirements
- Subscribers and relying parties informed of ways specific policy adds to or constrains requirements.
  - [EVCP/EVCP+]: for code signing, EVCG appendix J applies.

### 8.3 Conformance
- Only claim conformance if:
  - (a) Claims conformance and makes evidence available; or
  - (b) Current assessment by independent party, results available;
  - (c) If later shown significantly non-conformant, cease issuing until conformant or remedy;
  - (d) Compliance checked regularly and after major changes.
- A conformant CA shall demonstrate:
  - (e) meets obligations (6.1);
  - (f) implemented controls meeting clause 7;
  - (g) uses certificate policy meeting 8.1;
  - (h) implemented controls meeting additional policy requirements;
  - (i) meets additional requirements of 8.2;
  - (j) [EVCP/EVCP+]: meets EVCG [16];
  - (k) [PTC-BR]: meets BRG [19].

## Informative Annexes (Condensed)
- **Annex A (Significant differences to TS 101 456)**: This document extends TS 101 456 from qualified certificates to general public key certificates, defines NCP/NCP+ (equivalent quality without legal constraints), LCP (less onerous), and adds EVCP/EVCP+/DVCP/OVCP. Differences in scope, specific qualified certificate requirements removed, alternative quality/functionality options added.
- **Annex B (Model PKI disclosure statement)**: Provides a model structure for a PKI Disclosure Statement (PDS) to assist CAs in disclosing key policy elements to users in a simplified manner. Includes statement types such as CA contact, certificate type/validation, reliance limits, subscriber obligations, etc.
- **Annex C (IETF RFC 3647 cross reference)**: Maps clauses of this document to sections of RFC 3647 to assist users familiar with that framework.
- **Annex D (Revisions made since previous versions)**: Summarizes changes between V1.1.1 and V2.4.1, including additions (EVC requirements), updates (key generation, registration), and clarifications.
- **Annex E (normative) (Auditors qualification)**: Specifies requirements for bodies auditing conformance: shall be accredited per ISO/IEC 17021 or EN 45011, have competence per TS 119 403 or equivalent, and confirm examination against this document and TS 119 403, considering CA/Browser Forum Requirements.

## Requirements Summary
This table captures all normative "shall" requirements from the document. Due to length, only key requirements are shown; the main body above contains the full detail.

| ID | Requirement (Excerpt) | Type | Reference |
|---|---|---|---|
| R1 | CA shall only claim conformance if it makes available evidence or has current assessment by independent party. | shall | 5.4.1 |
| R2 | CA shall ensure all requirements in clause 7 are implemented as applicable. | shall | 6.1 |
| R3 | CA shall oblige subscriber to submit accurate information, exercise care, notify compromise, etc. | shall | 6.2 |
| R4 | CA shall include in terms notice for relying parties to verify revocation status, consider limitations, etc. | shall | 6.3 |
| R5 | CA shall specify disclaimers/limitations of liability per applicable laws. | shall | 6.4 |
| R6 | CA shall have a CPS addressing all requirements of applicable policy. | shall | 7.1 |
| R7 | CA keys shall be generated in controlled circumstances (physically secured, dual control). | shall | 7.2.1 |
| R8 | CA private signing key shall be held and used in secure cryptographic device meeting specified level. | shall | 7.2.2 |
| R9 | CA shall not hold subject's private signing keys for backup decryption if for electronic signatures. | shall | 7.2.4 |
| R10 | CA signing key shall not be used for other purposes; only within physically secure premises. | shall | 7.2.5 |
| R11 | CA private keys shall be destroyed or put beyond use at end of life. | shall | 7.2.6 |
| R12 | [NCPetc] CA shall ensure security of cryptographic device throughout lifecycle. | shall | 7.2.7 |
| R13 | If CA generates subject keys, they shall be generated securely, delivered securely, and copies destroyed if not needed. | shall | 7.2.8 |
| R14 | [NCP+/EVCP+] If issuing secure user device, it shall be securely controlled, stored, distributed; activation data separate. | shall | 7.2.9 |
| R15 | CA shall ensure evidence of identity properly examined; record information; signed agreement. | shall | 7.3.1 |
| R16 | CA shall ensure requests for renewal/rekey are complete, accurate, authorized. | shall | 7.3.2 |
| R17 | Certificates shall include required fields per X.509/RFC 5280. | shall | 7.3.3 |
| R18 | Terms and conditions shall be made available per 7.3.4. | shall | 7.3.4 |
| R19 | Certificates shall be available to subscriber upon generation; retrieval only with consent. | shall | 7.3.5 |
| R20 | CA shall document revocation procedures; process requests timely; publish CRLs per frequency. | shall | 7.3.6 |
| R21 | CA shall carry out risk assessment, retain responsibility, maintain security infrastructure. | shall | 7.4.1 |
| R22 | CA shall maintain inventory of information assets with classification. | shall | 7.4.2 |
| R23 | CA shall employ sufficient qualified personnel; apply disciplinary sanctions; define trusted roles. | shall | 7.4.3 |
| R24 | Physical access to critical services shall be limited; physical protection implemented. | shall | 7.4.4 |
| R25 | CA shall protect systems against malware; implement incident response; monitor audit logs. | shall | 7.4.5 |
| R26 | System access shall be limited to authorized individuals; sensitive data protected. | shall | 7.4.6 |
| R27 | Security analysis at design stage; change control procedures. | shall | 7.4.7 |
| R28 | Business continuity plan shall be defined and maintained; back up CA systems data. | shall | 7.4.8 |
| R29 | CA shall inform affected parties before termination; transfer obligations; destroy private keys. | shall | 7.4.9 |
| R30 | CA shall comply with legal requirements, data protection, protect records. | shall | 7.4.10 |
| R31 | All relevant information concerning certificates shall be recorded and archived securely. | shall | 7.4.11 |
| R32 | CA policies shall be non-discriminatory; CA is legal entity; financial stability; impartiality. | shall | 7.5 |
| R33 | CA shall provide testing options; disclose cross certificates. | shall | 7.6 |
| R34 | Authority issuing certificate policy shall follow framework in clause 8. | shall | 8.1 |
| R35 | Conformance claims shall meet requirements of 8.3. | shall | 8.3 |

Note: This summary is not exhaustive; the full normative text in the document governs.