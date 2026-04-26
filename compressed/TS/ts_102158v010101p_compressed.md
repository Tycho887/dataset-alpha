# ETSI TS 102 158 V1.1.1: Electronic Signatures and Infrastructures (ESI); Policy requirements for Certification Service Providers issuing attribute certificates usable with Qualified certificates
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2003-10 | **Type**: Normative
**Original**: http://www.etsi.org

## Scope (Summary)
Specifies policy requirements for Attribute Authorities (AAs) issuing Attribute Certificates (ACs) used in support of Qualified Electronic Signatures (Directive 1999/93/EC). Defines two AC policies for public issuance and a framework for other policies. Covers attribute registration, AC acquisition, generation, dissemination, revocation management, and revocation status.

## Normative References
- [1] Directive 1999/93/EC (Electronic signatures)
- [2] ITU-T X.509 (2000)|ISO/IEC 9594-8 (2001)
- [3] Directive 95/46/EC (Data protection)
- [4] IETF RFC 3280 (April 2002)
- [5] ISO/IEC 15408 (parts 1–3)
- [6] CEN Workshop Agreement 14167-2
- [7] Directive 93/13/EEC (Unfair contract terms)
- [8] CEN Workshop Agreement 14167-1
- [9] CEN Workshop Agreement 14167-3

## Definitions and Abbreviations
- **attribute**: information bounded to an entity specifying a characteristic (e.g., group membership, role)
- **Attribute Authority (AA)**: authority trusted to create and sign Attribute Certificates
- **Attribute Certificate (AC)**: digitally signed data structure containing a set of attributes for an end-entity
- **Attribute Certificate Policy (ACP)**: named set of rules indicating applicability of an AC
- **AC validity period**: time during which an AC is deemed valid
- **attribute certification period**: time during which ACs including a given attribute will be provided
- **Attribute Certification Disclosure Statement (ACDS)**: simplified document supplementing ACP and ACPS to assist users in trust decisions
- **Attribute Certification Practice Statement (ACPS)**: statement of practices employed by an AA
- **Attribute Granting Authority (AGA)**: authoritative source of an attribute (formerly AIA)
- **Certification Authority (CA)**: authority trusted to create and assign Public Key Certificates
- **Certification-Service-Provider (CSP)**: entity issuing certificates or providing related services (Directive 1999/93/EC)
- **electronic signature**: data in electronic form attached/logically associated with other data serving as authentication method
- **group membership**: state of being a member of a group (e.g., club, company, organization)
- **Public Key Certificate (PKC)**: unforgeable public key with other information signed by CA
- **Qualified Certificate (QC)**: PKC conforming to Annex I of Directive 1999/93/EC, issued by CA meeting Annex II
- **qualified electronic signature**: advanced electronic signature based on QC, created by SSCD (Article 5.1)
- **role**: function, position, or status in an organization, society, or relationship
- **relying party**: recipient of a certificate acting on reliance
- **subject**: entity identified in an AC as holder of the attributes
- **subscriber**: entity subscribing with an AA (may be subject or AGA)

## 4 General concepts
### 4.1 Certified attributes
- Attributes shall be verified before granting (clauses 7.2.1 p, 7.2.2 c) to ensure the individual was entitled to claim the attribute at time of registration.
- AA is responsible for correct attribution.

### 4.2 Attribute Authority
- AA is a CSP (Directive 1999/93/EC) issuing ACs.
- AA retains overall responsibility even if services are subcontracted; key used to generate ACs is identified as belonging to AA.

### 4.3 Attribute certification services
- Decomposed into: Attribute registration, AC Acquisition, AC generation, Dissemination, Attribute revocation management, AC revocation status.
- Diagram shows interrelationship: subscriber → registration; subject → acquisition; subject also fetches from dissemination; revocation requests → revocation management → revocation status → relying party.

### 4.4 Attribute certificate policy and attribute certification practice statement
- ACP states "what is to be adhered to"; ACPS states "how it is adhered to".
- ACP is less detailed; ACPS is tailored to AA’s environment.
- AA may issue terms and conditions (compliant with Directive 93/13/EEC). ACDS summarizes essential information.

### 4.5 Subscriber and subject
- Distinction: subscriber contracts with AA; subject is entity to whom AC applies.
- When subscriber ≠ subject (e.g., employer-employee), subscriber acts on behalf of subject. AGA can be subscriber.

### 4.6 Attribute semantics
- Semantics may be defined in standards (e.g., ISO OID) or locally by organizations; local use may be restricted to a close community. Interpreting requires combining issuing authority identifier with attribute definition.

## 5 Introduction to Attribute Certificate policies
### 5.1 Overview
- ACP is a named set of rules indicating applicability.
- Two AC policies specified for use with qualified certificates.

### 5.2 Identification
- **Policy 1**: Subject as subscriber → OID: `itu-t(0) identified-organization(4) etsi(0) attribute-certificate-policies(2158) ac-policy-identifiers(1) subject-as-subscriber(1)`. Only attributes registered by the subject shall be placed in the AC.
- **Policy 2**: AGA as subscriber → OID: `itu-t(0) identified-organization(4) etsi(0) attribute-certificate-policies(2158) ac-policy-identifiers(1) aga-as-subscriber(2)`. Only attributes registered by AGAs shall be placed.
- AA may support both policies.

### 5.3 User community and applicability
- ACs under these policies may support electronic signatures satisfying Article 5.1 of Directive 1999/93/EC.

### 5.4 Conformance
- AA shall only use policy identifiers if:
  - a) claims conformance and makes evidence available on request; or
  - b) has been assessed conformant by a competent independent party.

## 6 Obligations and liability
### 6.1 Attribute authority obligations
- AA shall implement all requirements in clause 7 as applicable to the AC policy.
- AA responsible for conformance even when functions are subcontracted.
- AA shall provide services consistent with its ACPS.

### 6.2 Subscriber obligations
- AA shall oblige subscriber through agreement (clause 7.2.3.1 a)) to:
  - a) submit accurate and complete information;
  - b) notify AA without unreasonable delay of inaccuracy or changes.
- NOTE: Subscribers may incur liability for delay.

### 6.3 Subject obligations
- AA shall oblige subscriber to agree that subject shall:
  - use AC solely for specified usage;
  - notify subscriber without unreasonable delay of inaccuracies or change in attribute ownership.

### 6.4 Information for relying parties
- ACDS shall include notice that to reasonably rely, relying party shall:
  - a) verify validity, suspension, or revocation using current revocation status;
  - b) consider any limitations on usage communicated in AC or terms;
  - c) take other prescribed precautions.
- AA must ensure any limitations governing reliance or liability are clearly brought to attention.

### 6.5 Liability
- Liability applies to parties who "reasonably rely". AA shall specify liabilities in ACPS (see annex B for details). Disclaimers subject to national law.

## 7 Requirements on AA practice
- AA shall implement controls meeting the following requirements. Requirements indicated as security objectives followed by specific controls where necessary.

### 7.1 Attribute Certification practice statements
- AA shall demonstrate reliability. In particular:
  - a) Have ACPS for each supported AC policy.
  - b) Identify obligations of external organizations.
  - c) Make ACPS and relevant documentation available.
  - d) Disclose terms and conditions (clause 7.2.3.1).
  - e) High-level management body approves ACPS.
  - f) Senior management responsible for proper implementation.
  - g) Define review process for ACPS.
  - h) Give notice of changes; revised ACPS immediately available.
  - i) Specify in ACPS details of verification practices and sources used to grant attributes.
  - j) Specify attribute certification validity periods.
  - k) Specify support (or not) of revocation, and procedures if supported.
  - l) Specify whether attributes can be individually acquired or together; if multiple, procedure to be followed.
  - m) Specify whether and how subject can delegate attributes.

### 7.2 Attribute management life cycle
#### 7.2.1 Subject and attribute initial registration
- AA shall ensure:
  - 1) Subject is rightful owner of PKC referenced.
  - 2) Subjects, subscribers or authorized persons know revocation procedure.
- In particular:
  - a) Before contractual relationship, provide terms and conditions (clause 7.1.2).
  - b) Communicate via durable means in understandable language.
  - c) Verify subject’s right to attributes.
  - d) Verify identity directly or indirectly with evidence: full name, date/place of birth, other distinguishing attributes.
  - e) If indirect, means providing equivalent assurance to physical presence.
  - f) Subject and subscriber provide physical address or contact attributes.
  - g) Record all information used for verification.
  - h) Inform subscriber how subject receives ACs.
  - i) Record signed agreement including obligations, consents, publication conditions, confirmation of correctness, and relevant terms.
  - j) Retain records for period indicated and for legal proceedings.
  - k) Adhere to national data protection legislation.
  - l) Protect confidentiality and integrity of registration data.
  - m) If external registration providers used, verify identity and data exchange.
  - n) Provide sufficient info on revocation means.
  - o) Ensure subjects’ attributes are properly verified.
  - p) Verify at registration time that individual entitled to attribute.
  - q) Record all verification information.
  - r) Ensure subject consents to AC issuance.
  - s) Record acceptance to obtain ACs.

#### 7.2.2 Attribute renewal
- When attribute certification period expires, new registration may occur. AA shall ensure:
  - a) Communicate any changed terms and obtain agreement per 7.2.1 a,b,j.
  - b) Verify and record changed info per 7.2.1 c) to i).
  - c) Check subject is rightful PKC owner and entitled to requested attributes.
  - d) Verify and update address information.
  - e) Record all verification info.
  - f) Retain records for period indicated or longer if legal proceeding.
  - g) Protect confidentiality/integrity of registration data.
  - h) Verify identity of external registration providers.
  - i) Verify attributes by appropriate means.
  - j) Record all verification info.
  - k) Record signed agreement with subscriber including consents and confirmation.
  - l) Ensure subject consents to granted attributes.

#### 7.2.3 Dissemination of Terms and Conditions
##### 7.2.3.1 Terms and Conditions for subscribers and subjects
- AA shall ensure terms and conditions are available to subscribers, subjects, and relying parties. In particular:
  - a) Make available ACP/ACPS and any applicable terms including:
    1) policy identifier(s);
    2) clear description of each attribute type;
    3) list of documents needed to prove right to attribute;
    4) how attribute represented in AC;
    5) limitations on use;
    6) subscriber/subject obligations (clause 6.2);
    7) how ACs provided;
    8) revocation handling;
    9) validation information including revocation status;
   10) disclaimers/limitations of liability;
   11) retention period for registration info;
   12) retention period for event logs;
   13) complaints/dispute settlement procedures;
   14) governing laws;
   15) conformance certification and scheme.
  - b) Information available via durable means, understandable language.

#### 7.2.4 Attribute Certificate acquisition
- AA shall ensure requests for ACs for previously registered subjects are authorized. In particular:
  - a) Issue AC containing info per annex A.
  - b) Issue AC only to legitimate PKC holder.
  - c) Allow subscribers/subjects to specify attributes when multiple are available.

#### 7.2.5 Attribute Certificate dissemination
- ACs shall be available for retrieval by relying parties only with subscriber’s consent.
- Information shall be publicly and internationally available.

#### 7.2.6 Attribute Certificate generation
- AA shall ensure ACs are issued securely. In particular:
  - a) AC generation service shall generate ACs with fields per annex A; AC profiles included in ACP/ACPS.
  - b) Only accept AC requests originating from within AA and per procedures.

#### 7.2.7 Attribute and AC revocation and suspension
- AA shall ensure timely revocation based on authorized requests. In particular:
  - a) Document in ACPS procedures including: who may submit; how; confirmation requirements; reasons for suspension; mechanism; maximum delay.
  - b) Nominate individuals/authorities entitled to ask for revocation.
  - c) Process revocation requests on receipt.
  - d) Authenticate and check requests originate from authorized source.
  - e) Optionally suspend AC while confirming revocation; not suspended longer than necessary.
  - f) Inform subject/subscriber of change of status.
  - g) Once definitively revoked, AC shall not be reinstated.
  - h) If ACRLs used, publish at least daily; each ACRL states time limit for next issuance; signed by AA or designated authority.
  - i) Attribute revocation management service available at least during business hours; best endeavours to avoid unavailability beyond maximum specified in ACPS.
  - j) AC revocation status information available 24/7; best endeavours.
  - k) Protect integrity and authenticity of status info.
  - l) Revocation status info publicly and internationally available.

### 7.3 Attribute Authority keys management life cycle
#### 7.3.1 Attribute Authority keys generation
- AA signing keys may be for signing ACs, ACRLs, or OCSP responses. Different keys should be used for each purpose.
- In particular:
  - a) Key generation in physically secured environment, dual control, minimal authorized personnel.
  - b) Generated within device meeting CEN WA 14167-1, -3, or trustworthy system assured to EAL4+ (ISO/IEC 15408).
  - c) Use recognized algorithm.
  - d) Select key length recognized fit for purpose.

#### 7.3.2 Attribute Authority keys storage, backup and recovery
- AA private keys shall remain confidential and maintain integrity. In particular:
  - a) Private signing key held and used in secure cryptographic device meeting CEN WA 14167-1, -2, or EAL4+.
  - b) Access controls prevent key exposure outside device.
  - c) If backed up, protect encrypted with algorithm/ key-length capable of withstanding attacks for residual life.
  - d) Backup/recovery only by trusted roles, dual control, physically secured.
  - e) Backup copies subject to same or greater security.
  - f) If stored in backup security module, access controls prevent unauthorized use; activation only under dual control.

#### 7.3.3 Attribute Authority public keys distribution
- AA shall ensure integrity and authenticity of public keys during distribution. In particular:
  - a) Public keys made available in manner assuring integrity and authenticating origin (e.g., PKCs signed by CA).

#### 7.3.4 Attribute authority keys usage
- AA shall ensure private signing keys not used inappropriately. In particular:
  - a) Signing keys for ACs shall not be used for other purposes except signing ACRLs/OCSP responses.
  - b) Only used within physically secure premises.

#### 7.3.5 End of AA key life cycle
- All copies of private signing keys shall be destroyed so they cannot be retrieved.

#### 7.3.6 Life cycle management of cryptographic hardware used to sign ACs, ACRLs or OCSP responses
- AA shall ensure:
  - a) Hardware not tampered during shipment.
  - b) Not tampered while stored.
  - c) Installation/activation requires dual control.
  - d) Key generation, activation, backup, recovery requires dual control.
  - e) Hardware functioning correctly.
  - f) Private keys destroyed on device retirement.

### 7.4 AA management and operation
#### 7.4.1 Security management
- AA shall ensure adequate administrative/management procedures. In particular:
  - a) Risk assessment.
  - b) Retain responsibility for outsourced functions; define third-party controls.
  - c) Management provides information security direction through high-level forum.
  - d) Maintain security infrastructure; changes approved by management forum.
  - e) Document, implement, maintain security controls and operating procedures.
  - f) Maintain security when functions outsourced.

#### 7.4.2 Asset classification and management
- AA shall maintain inventory of information assets and classify protection requirements based on risk analysis.

#### 7.4.3 Personnel security
- AA shall employ personnel with expert knowledge, experience, qualifications.
  - a) [already stated]
  - b) Document security roles; identify trusted roles.
  - c) Job descriptions define separation of duties and least privilege; AA personnel commit to confidentiality and data protection.
  - d) Personnel exercise procedures in line with security management.
  - e) Managerial personnel possess expertise in electronic signature technology and security.
  - f) All AA personnel in trusted roles free from conflicting interests (e.g., not involved in AGA activities).
  - g) Trusted roles include Security Officers, System Administrators, System Operators, System Auditors.
  - h) Formal appointment to trusted roles by senior management.
  - i) Do not appoint persons known to have conviction for serious crime; personnel not access trusted functions until checks completed.

#### 7.4.4 Physical and environmental security
- AA shall control physical access and minimize risks. In particular:
  - a) Physical access to critical services limited to authorized individuals.
  - b) Controls to avoid loss/damage/compromise and interruption.
  - c) Controls to avoid compromise/theft.
  - e) AC generation and revocation management facilities physically protected; defined security perimeters; no sharing with other organizations (except PKC issuance/management).
  - g) Physical and environmental security policy addresses access control, natural disasters, fire, utilities, etc.
  - h) Controls against off-site removal without authorization.

#### 7.4.5 Operations management
- AA shall ensure system security and correct operation. In particular:
  - a) Protect against viruses, malicious software.
  - b) Minimize damage via incident reporting/response.
  - c) Secure handling of media.
  - d) Establish procedures for all trusted/administrative roles.
  - e) Media handled per classification scheme; sensitive data securely disposed.
  - f) Monitor capacity demands; project future capacity.
  - g) Act timely to incidents; report as soon as possible.
  - h) AA security operations separated from normal operations.

#### 7.4.6 System Access management
- AA shall limit access to authorized individuals. In particular:
  - a) Implement controls (e.g., firewalls) to protect internal networks.
  - b) Protect sensitive data when exchanged over insecure networks.
  - c) Effective administration of user access (account management, auditing, timely modification/removal).
  - d) Access to information and application functions restricted; separation of trusted roles.
  - e) AA personnel identified and authenticated before using critical applications.
  - f) Accountability via event logs.
  - g) Protect sensitive data from being revealed through re-used storage objects.
  - h) Local network components physically secure; configurations audited.
  - i) Continuous monitoring and alarm facilities for unauthorized access attempts.
  - j) AC acquisition service enforces access control on subjects.
  - k) Dissemination application enforces access control on adding/deleting ACs.
  - l) Revocation management application enforces access control.
  - m) Revocation status provision application enforces access control.

#### 7.4.7 Trustworthy Systems deployment and maintenance
- AA shall use trustworthy systems protected against modification. In particular:
  - a) Security requirements analysis at design stage.
  - b) Change control procedures for software releases, modifications, emergency fixes.

#### 7.4.8 Business continuity management and incident handling
- AA shall ensure operations restored as soon as possible after disaster, including key compromise. In particular:
  - a) Business continuity plan addresses AA private key compromise.
  - b) In case of compromise, AA shall inform subscribers, relying parties, AGAs; indicate ACs and revocation status may no longer be valid.

#### 7.4.9 AA termination
- AA shall minimize disruption and maintain records for legal proceedings. In particular:
  - a) Before termination: inform all affected entities; terminate subcontractor authorizations; transfer obligations for records; destroy private keys.
  - b) Arrange to cover costs if bankrupt.
  - c) State in practices provisions for termination including notification, transfer, and handling revocation status.
  - d) Continue data protection and confidentiality; databases remain confidential and only disclosed to designated recipients.

#### 7.4.10 Compliance with Legal requirements
- AA shall ensure legal compliance. In particular:
  - a) Protect records from loss, destruction, falsification.
  - b) Meet requirements of Directive 95/46/EC as implemented nationally.
  - c) Take technical/organizational measures against unauthorized/unlawful processing and accidental loss.
  - d) Protect user information from disclosure without agreement, court order, or legal authorization.

#### 7.4.11 Recording of information concerning Attribute Certificates
- AA shall record relevant information for appropriate period, especially for legal evidence. In particular:
  - a) Maintain confidentiality/integrity of current and archived records.
  - b) Archive completely and confidentially per disclosed practices.
  - c) Records available for legal proceedings; subject (and subscriber within data protection constraints) have access.
  - d) Record precise time of significant events.
  - e) Hold records for period appropriate for legal evidence (see notes on statute of limitations).
  - f) Log events so not easily deleted/destroyed.
  - g) Document specific events and data to log.
  - h) Log all registration events including renewal requests.
  - i) Record registration information: documents presented, unique IDs, storage location of copies, choices, identity of entity accepting application, validation methods, names of receiving AA/RA.
  - j) Maintain privacy of subject information.
  - k) Log all events relating to AA keys and PKC life-cycle.
  - l) Log all events relating to AC life-cycle.
  - m) Log all revocation/suspension requests and resulting actions.

### 7.5 Organizational
- AA shall ensure organization is reliable. In particular:
  - a) Policies non-discriminatory.
  - b) Services accessible to all applicants within declared field.
  - c) AA is legal entity under national law.
  - d) Has quality/information security management systems.
  - e) Adequate coverage for liabilities.
  - f) Financial stability and resources.
  - g) Sufficient personnel with necessary education, training, knowledge, experience.
  - h) Policies for complaint/dispute resolution.
  - i) Proper agreement/contractual relationship for subcontracting.
  - j) AC generation and revocation management parts independent from other organizations; senior staff free from pressures.
  - k) Documented structure safeguarding impartiality.

## 8 Framework for the definition of other Attribute Certificate policies
### 8.1 Attribute Certificate policy management
- AA shall ensure policy effective. In particular:
  - a) Body (e.g., policy management authority) with final authority for specifying/approving policy.
  - b) Risk assessment to determine security requirements.
  - c) Policy approved/modified per defined review process.
  - d) Review process ensures policies supported by ACPS.
  - e) Make policies available to subscribers/relying parties.
  - f) Revisions made available.
  - g) Policy shall incorporate/constrain all requirements of clauses 6 and 7 with exclusions indicated; present document prevails in conflict.
  - h) Obtain unique OID per ITU-T X.509.

### 8.2 Exclusions for AC not issued to the public
- Attributes Certificates not issued to the public need not apply:
  - a) Liability (clause 6.3).
  - b) Independence of certificate generation/revocation management providers (clauses 7.5 j,k).
  - c) Public dissemination (clause 7.3.5 f).
  - d) Public availability of revocation status (clause 7.3.6 k).
- NOTE: An AA is not considered offering to the public if restricted to voluntary private law agreements.

### 8.3 Additional requirements
- Subscribers and relying parties shall be informed:
  - a) If policy not for public use and which exclusions apply.
  - b) Ways in which specific policy adds/constrains requirements.

### 8.4 Conformance
- AA shall only claim conformance if:
  - a) Claims conformance to an identified policy and makes evidence available; or
  - b) Assessed conformant by independent party.
- Conformant AA must demonstrate:
  - c) Meets obligations (clause 6.1).
  - d) Implements controls per clause 7 (excluding exclusions if not public).
  - e) Uses policy meeting clause 8.1.

## Requirements Summary (Selected Key Requirements)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Attributes shall be verified before granting; individual entitled at time of registration. | shall | 4.1, 7.2.1 p |
| R2 | AA retains overall responsibility even if services subcontracted. | shall | 4.2 |
| R3 | AA shall make its ACPS and relevant documentation available. | shall | 7.1 c |
| R4 | AA shall verify subject’s identity and attributes; record all verification information. | shall | 7.2.1 d-g, o-q |
| R5 | AC shall contain information per Annex A (normative). | shall | 7.2.4 a |
| R6 | ACs shall be revoked in a timely manner based on authorized requests. | shall | 7.2.7 |
| R7 | AA private keys shall be generated in controlled circumstances, dual control, secure device. | shall | 7.3.1 |
| R8 | AA private keys shall remain confidential and maintain integrity. | shall | 7.3.2 |
| R9 | AA shall ensure business continuity plan addresses key compromise. | shall | 7.4.8 |
| R10 | Records concerning Attribute Certificates shall be retained for appropriate period for legal evidence. | shall | 7.4.11 e |

## Informative Annexes (Condensed)
- **Annex A (normative)**: Specifies minimum fields for AC: policy identifier, CSP identification and state, subject attributes (as in linked QC), unambiguous link to QC, validity period, unique serial number, advanced electronic signature of issuer.
- **Annex B (informative)**: Discusses liability assertions for AAs. Notes Directive 1999/93/EC does not specify liability for AAs; suggests projection of Article 6 liability (accuracy, revocation) to AAs. Explores limitations (per transaction, aggregate, per AC/QC) and need for clear documentation in ACPS.
- **Annex C (informative)**: Provides model AC disclosure statement (PDS) structure with statement types: AA contact info, AC type/validation/usage, reliance limits, obligations, status checking, warranty/disclaimer, applicable agreements, privacy policy, refund policy, applicable law/complaints, and AA licenses/audit.
- **Annex D (informative)**: Bibliography includes TTP.NL, BSI IT-Grundschutz, ISO/IEC 17799, ITU-T X.843, ISO/IEC 14516, ISO/IEC TR 13335, ISO/TS 17090, ANSI X9.79, CEN Workshop Agreements, ETSI TRs, IETF RFCs on PKIX and AC profiles.