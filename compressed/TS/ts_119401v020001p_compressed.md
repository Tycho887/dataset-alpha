# ETSI TS 119 401: General Policy Requirements for Trust Service Providers
**Source**: ETSI Technical Committee ESI | **Version**: V2.0.1 | **Date**: 2015-07 | **Type**: Normative Technical Specification
**Original**: Reference RTS/ESI-0019401-TS

## Scope
This document specifies baseline policy requirements on the operation and management practices of Trust Service Providers (TSPs) regardless of the type of service provided (e.g., certificate issuance, timestamping, signature validation, e-delivery). It does not specify assessment procedures (see ETSI TS 119 403).

## Normative References
None (no normative references cited). The document relies on informative references only.

## Definitions and Abbreviations
### Definitions
- **Coordinated Universal Time (UTC)**: time scale based on the second as defined in Recommendation ITU-R TF.460-6 [i.11]
- **relying party**: natural or legal person that relies upon an electronic identification or a trust service (includes parties verifying a digital signature using a public key certificate)
- **subscriber**: legal or natural person bound by agreement with a trust service provider to any subscriber obligations
- **trust service**: electronic service which enhances trust and confidence in electronic transactions (typically but not necessarily using cryptographic techniques or involving confidential material)
- **trust service policy**: set of rules that indicates the applicability of a trust service to a particular community and/or class of application with common security requirements
- **trust service practice statement**: statement of the practices that a TSP employs in providing a trust service
- **trust service provider (TSP)**: entity which provides one or more trust services

### Abbreviations
- CA: Certification Authority
- IP: Internet Protocol
- IT: Information Technology
- TSP: Trust Service Provider
- UTC: Coordinated Universal Time

## 4 Overview (Informative Summary)
Trust services include (but are not limited to) issuance of public key certificates, registration, timestamping, long-term preservation, e-delivery, and signature validation. Requirements are expressed as security objectives followed by specific controls. No restriction on charging for services.

## 5 Risk Assessment (Normative)
- **R01**: The TSP **shall** carry out a risk assessment to identify, analyse, and evaluate trust service risks.
- **R02**: The TSP **shall** select appropriate risk treatment measures; level of security **shall** be commensurate to the degree of risk.
- **R03**: The TSP **shall** determine all security requirements and operational procedures necessary to implement the chosen risk treatment options, documented in the information security policy and trust service practice statement.
- **R04**: The risk assessment **shall** be regularly reviewed and revised.

## 6 Policies and Practices
### 6.1 Trust Service Practice (TSP) Statement
- **R05**: The TSP **shall** specify the set of policies and practices appropriate for the services it provides; **shall** be approved by management, published, and communicated.
- **R06**: The TSP **shall** have a statement of the practices and procedures for the trust service provided.
- **R07(a)**: The TSP **shall** have a statement of practices and procedures used to address all requirements for the applicable TSP policy.
- **R07(b)**: The practice statement **shall** identify obligations of external organizations supporting TSP services, including applicable policies and practices.
- **R07(c)**: The TSP **shall** make available to subscribers and relying parties its practice statement and other relevant documentation to assess conformance.
- **R07(d)**: The TSP **shall** have a management body with overall responsibility and final authority for approving the practice statement.
- **R07(e)**: TSP management **shall** implement the practices.
- **R07(f)**: The TSP **shall** define a review process for practices, including responsibilities for maintaining the practice statement.
- **R07(g)**: The TSP **shall** notify changes intended in its practice statement and, following approval, make the revised statement immediately available.
- **R07(h)**: The TSP **shall** state in its practices the provisions made for termination of service (as per clause 7.11).

### 6.2 Terms and Conditions
- **R08**: TSP **shall** make terms and conditions available to all subscribers and relying parties.
- **R09**: Terms and conditions **shall** specify for each trust service policy supported:
  - (a) the trust service policy applied;
  - (b) any limitations on use of the service (e.g., expected lifetime of certificates);
  - (c) subscriber's obligations, if any;
  - (d) information for relying parties (e.g., how to verify token, limitations on validity period);
  - (e) period of retention of event logs;
  - (f) limitations of liability;
  - (g) limitations on use including damages exceeding such limitations;
  - (h) applicable legal system;
  - (i) procedures for complaints and dispute settlement;
  - (j) whether the service has been assessed as conformant with policy, and if so through which scheme;
  - (k) TSP contact information.
- **R10**: Customers **shall** be informed about limitations in advance.
- **R11**: Terms and conditions **shall** be made available through a durable means of communication, in a readily understandable language. May be transmitted electronically.

### 6.3 Information Security Policy
- **R12**: The TSP **shall** define an information security policy approved by management, setting out the organization’s approach to managing information security.
- **R13(a)**: The policy **shall** be documented, implemented, and maintained, including security controls and operating procedures for TSP facilities, systems, and information assets. The TSP **shall** publish and communicate to all impacted employees.
- **R13(b)**: The TSP **shall** retain overall responsibility for conformance even when functionality is outsourced; **shall** define outsourcer liability and ensure outsourcers are bound to implement required controls.
- **R13(c)**: The information security policy and inventory of assets **shall** be reviewed at planned intervals or on significant changes; changes impacting security level **shall** be approved by high-level management. TSP systems **shall** be regularly checked for violations of security policies.
- **R13(d)**: Management security policy **shall** be documented, implemented, and maintained including security controls and operating procedures.

## 7 TSP Management and Operation
### 7.1 Internal Organization
#### 7.1.1 Organization Reliability
- **R14**: The TSP organization **shall** be reliable.
- **R15(a)**: Trust service practices **shall** be non-discriminatory.
- **R15(b)**: The TSP **shall** make services accessible to all applicants whose activities fall within its declared field of operation and who agree to abide by obligations.
- **R15(c)**: The TSP **shall** maintain sufficient financial resources and/or obtain appropriate liability insurance in accordance with national law.
- **R15(d)**: The TSP **shall** have financial stability and resources to operate in conformity with this policy.
- **R15(e)**: The TSP **shall** have policies and procedures for resolution of complaints and disputes.
- **R15(f)**: The TSP **shall** have a documented agreement and contractual relationship for subcontracting, outsourcing, or other third-party arrangements.

#### 7.1.2 Segregation of Duties
- **R16**: Conflicting duties and areas of responsibility **shall** be segregated to reduce unauthorized or unintentional modification or misuse of TSP assets.

### 7.2 Human Resources
- **R17**: The TSP **shall** ensure employees and contractors support trustworthiness of operations.
- **R18(a)**: The TSP **shall** employ staff and subcontractors with necessary expertise, reliability, experience, qualifications, and training on security and data protection.
- **R18(b)**: (Should) Personnel should fulfil "expert knowledge, experience and qualifications" through formal training, actual experience, or combination; should include regular (at least every 12 months) updates on threats and security practices.
- **R18(c)**: Appropriate disciplinary sanctions **shall** be applied to personnel violating TSP policies or procedures.
- **R18(d)**: Security roles and responsibilities **shall** be documented in job descriptions; trusted roles **shall** be clearly identified, named by management, and accepted by management and the person.
- **R18(e)**: TSP personnel (temporary and permanent) **shall** have job descriptions from viewpoint of roles with segregation of duties and least privilege, determining position sensitivity, background screening, training, and awareness.
- **R18(f)**: Personnel **shall** exercise administrative and management procedures in line with TSP’s information security management procedures.
- **R18(g)**: Managerial personnel **shall** possess experience or training on trust service provided, familiarity with security procedures, and experience with information security and risk assessment.
- **R18(h)**: All TSP personnel in trusted roles **shall** be free from conflicts of interest that might prejudice impartiality.
- **R18(i)**: Trusted roles **shall** include: Security Officers (overall responsibility for implementing security practices), System Administrators (install, configure, maintain), System Operators (daily operation, backup/recovery), System Auditors (view archives/logs).
- **R18(j)**: Personnel **shall** be formally appointed to trusted roles by senior management, requiring least privilege when accessing or configuring access privileges.
- **R18(k)**: Personnel **shall not** have access to trusted functions until any necessary checks are completed.

### 7.3 Asset Management
#### 7.3.1 General Requirements
- **R19**: The TSP **shall** ensure appropriate level of protection of its assets including information assets.
- **R20**: The TSP **shall** maintain an inventory of all information assets and assign classification consistent with risk assessment.

#### 7.3.2 Media Handling
- **R21**: All media **shall** be handled securely per information classification scheme. Media containing sensitive data **shall** be securely disposed of when no longer required.

### 7.4 Access Control
- **R22**: TSP system access **shall** be limited to authorized individuals.
- **R23(a)**: Controls (e.g., firewalls) **shall** protect internal network domains from unauthorized access; firewalls should prevent protocols/accesses not required.
- **R23(b)**: The TSP **shall** administer user access (operators, administrators, system auditors) including account management and timely modification/removal.
- **R23(c)**: Access to information and application system functions **shall** be restricted per access control policy; TSP system **shall** provide sufficient computer security controls for separation of trusted roles, particularly restricting use of system utility programs.
- **R23(d)**: TSP personnel **shall** be identified and authenticated before using critical applications related to the service.
- **R23(e)**: TSP personnel **shall** be accountable for their activities (e.g., by event logs).
- **R23(f)**: Sensitive data **shall** be protected against being revealed through re-used storage objects.

### 7.5 Cryptographic Controls
- **R24**: Appropriate security controls **shall** be in place for management of any cryptographic keys and devices throughout their lifecycle.

### 7.6 Physical and Environmental Security
- **R25**: The TSP **shall** control physical access to components whose security is critical to service provision and minimize risks.
- **R26(a)**: Physical access to critical components **shall** be limited to authorized individuals.
- **R26(b)**: Controls **shall** be implemented to avoid loss, damage, compromise of assets, and interruption to business.
- **R26(c)**: Controls **shall** be implemented to avoid compromise or theft of information and processing facilities.
- **R26(d)**: Critical components **shall** be located in a protected security perimeter with physical protection against intrusion, access controls, and intrusion detection alarms.

### 7.7 Operation Security
- **R27**: The TSP **shall** use trustworthy systems and products protected against modification; ensure technical security and reliability.
- **R28(a)**: Security requirements analysis **shall** be carried out at design/specification stage of any systems development to ensure security is built in.
- **R28(b)**: Change control procedures **shall** be applied for releases, modifications, and emergency fixes of operational software.
- **R28(c)**: Integrity of TSP systems and information **shall** be protected against viruses, malicious and unauthorized software.
- **R28(d)**: Media used within TSP systems **shall** be securely handled to protect from damage, theft, unauthorized access, and obsolescence.
- **R28(e)**: Media management procedures **shall** protect against obsolescence and deterioration during retention period.
- **R28(f)**: Procedures **shall** be established and implemented for all trusted and administrative roles impacting service provision.
- **R28(g)**: The TSP **shall** specify and apply procedures for ensuring security patches are applied within a reasonable time; patch may not be applied if it introduces additional vulnerabilities or instabilities outweighing benefits; reason for not applying **shall** be documented.

### 7.8 Network Security
- **R29**: The TSP **shall** protect its network and systems from attack.
- **R30(a)**: The TSP **shall** segment systems into networks/zones based on risk assessment; **shall** apply same security controls to all systems in the same zone.
- **R30(b)**: The TSP **shall** restrict access and communications between zones to those necessary; unneeded connections/services **shall** be disabled; rule set **shall** be reviewed regularly.
- **R30(c)**: The TSP **shall** maintain critical system elements (e.g., Root CA) in a secured zone.
- **R30(d)**: A dedicated network for administration **shall** be established, separated from operational network; administration systems **shall not** be used for non-administrative purposes.
- **R30(e)**: Test and production platforms **shall** be separated from each other and from development.
- **R30(f)**: Communication between distinct trustworthy systems **shall** be through trusted channels logically distinct from other channels, with assured identification and data protection.
- **R30(g)**: If external availability is required, external network connection to the internet **shall** be redundant to ensure availability (may use two different connections to one or more providers).
- **R30(h)**: The TSP **shall** undergo or perform regular vulnerability scans on public and private IP addresses; evidence of scan performance by qualified entity **shall** be recorded.
- **R30(i)**: The TSP **shall** undergo penetration tests at set-up and after significant infrastructure/application upgrades; evidence **shall** be recorded.

### 7.9 Incident Management
- **R31**: System activities concerning access, use, and service requests **shall** be monitored.
- **R32(b)**: Abnormal system activities indicating potential security violation (including intrusion) **shall** be detected and reported as alarms.
- **R32(c)**: TSP IT systems **shall** monitor: (i) start-up/shutdown of logging functions; (ii) availability and utilization of needed services.
- **R32(d)**: The TSP **shall** act in timely and coordinated manner to respond to incidents and limit impact; **shall** appoint trusted role personnel to follow up on alerts.
- **R32(e)**: The TSP **shall** establish procedures to notify appropriate parties of any breach of security or loss of integrity having significant impact (in line with applicable regulatory rules, e.g., Regulation (EU) 910/2014 Art. 19.2).
- **R32(f)**: Where breach is likely to adversely affect a natural or legal person, the TSP **shall** notify the person without undue delay.
- **R32(g)**: Audit logs **shall** be monitored or reviewed regularly to identify malicious activity; automatic mechanisms **shall** be implemented to process logs and alert personnel.
- **R32(h)**: The TSP **shall** remediate critical vulnerabilities within a reasonable period; if not possible, **shall** create/implement mitigation plan or document factual basis for determination that remediation is not required.
- **R32(i)**: Incident reporting and response procedures **shall** be employed to minimize damage.

### 7.10 Collection of Evidence
- **R33**: The TSP **shall** record and keep accessible for an appropriate period (including after cessation) all relevant information concerning data issued/received, for legal proceedings and service continuity.
- **R34(a)**: Confidentiality and integrity of current and archived records **shall** be maintained.
- **R34(b)**: Records **shall** be completely and confidentially archived in accordance with disclosed business practices.
- **R34(c)**: Records **shall** be made available if required for legal proceedings.
- **R34(d)**: Precise time of significant TSP environmental, key management, and clock synchronization events **shall** be recorded; time used **shall** be synchronized with UTC at least once a day.
- **R34(e)**: Records **shall** be held for a period after expiration of signing keys or trust service token as appropriate, as notified in TSP disclosure statement.
- **R34(f)**: Events **shall** be logged so they cannot be easily deleted or destroyed within the required retention period (e.g., write-only media, off-site backup).

### 7.11 Business Continuity Management
- **R35**: In the event of a disaster (including compromise of private signing key or trust service credentials), operations **shall** be restored as soon as possible.
- **R36**: The TSP **shall** define and maintain a continuity plan to enact in case of a disaster.

### 7.12 TSP Termination and Termination Plans
- **R37**: Potential disruptions to subscribers and relying parties **shall** be minimized as a result of cessation of TSP’s services; continued maintenance of information required to verify correctness **shall** be provided.
- **R38(a)**: The TSP **shall** have an up-to-date termination plan.
- **R38(b)**: Before termination: (i) TSP **shall** inform all subscribers and entities with agreements, and make information available to relying parties; (ii) TSP **shall** terminate authorization of subcontractors; (iii) TSP **shall** transfer obligations to a reliable party for maintaining information necessary for evidence of operation (unless no such information held); (iv) TSP private keys (including backups) **shall** be destroyed or withdrawn in unrecoverable manner; (v) where possible, TSP should make arrangements to transfer service provision to another TSP.
- **R38(c)**: The TSP **shall** have an arrangement to cover costs to fulfil these minimum requirements in case of bankruptcy or inability to cover costs.
- **R38(d)**: The TSP **shall** state in its practices the provisions for termination, including notification of affected entities and transferring obligations.
- **R38(e)**: The TSP **shall** maintain or transfer to a reliable party its obligations to make available its public key or trust service tokens to relying parties for a reasonable period.

### 7.13 Compliance
- **R39**: The TSP **shall** ensure it operates in a legal and trustworthy manner.
- **R40(a)**: The TSP **shall** provide evidence on how it meets applicable legal requirements.
- **R40(b)**: Trust services and end-user products **shall** be made accessible for persons with disabilities; applicable standards (e.g., ETSI EN 301 549) should be taken into account.
- **R40(c)**: Appropriate technical and organizational measures **shall** be taken against unauthorized/unlawful processing of personal data and against accidental loss or destruction of personal data.

## Requirements Summary
| ID | Requirement (condensed) | Type | Reference |
|---|---|---|---|
| R01 | Carry out risk assessment | shall | 5 |
| R02 | Select risk treatment measures commensurate to risk | shall | 5 |
| R03 | Determine security requirements and operational procedures based on risk treatment | shall | 5 |
| R04 | Regularly review and revise risk assessment | shall | 5 |
| R05 | Specify policies and practices, approved by management, published | shall | 6.1 |
| R06 | Have a practice statement | shall | 6.1 |
| R07 | Address all requirements for applicable policy | shall | 6.1(a) |
| R07b | Identify obligations of external organizations | shall | 6.1(b) |
| R07c | Make practice statement available to subscribers/relying parties | shall | 6.1(c) |
| R07d | Management body with final authority for approval | shall | 6.1(d) |
| R07e | Management implements practices | shall | 6.1(e) |
| R07f | Define review process for practices | shall | 6.1(f) |
| R07g | Notify and publish changes to practice statement | shall | 6.1(g) |
| R07h | State termination provisions in practices | shall | 6.1(h) |
| R08 | Make terms and conditions available | shall | 6.2 |
| R09 | Terms specify content per policy (13 items a-k) | shall | 6.2 a-k |
| R10 | Inform customers about limitations in advance | shall | 6.2 |
| R11 | Terms via durable means, understandable language | shall | 6.2 |
| R12 | Define information security policy approved by management | shall | 6.3 |
| R13a | Document, implement, maintain security policy; publish and communicate | shall | 6.3(a) |
| R13b | Retain responsibility for outsourced functions; define outsourcer liability | shall | 6.3(b) |
| R13c | Review policy and asset inventory at planned intervals; approve changes; check for violations | shall | 6.3(c) |
| R13d | Document, implement, maintain management security policy | shall | 6.3(d) |
| R14 | Organization shall be reliable | shall | 7.1.1 |
| R15a | Practices non-discriminatory | shall | 7.1.1(a) |
| R15b | Accessible to all within field | shall | 7.1.1(b) |
| R15c | Sufficient financial resources/liability insurance per national law | shall | 7.1.1(c) |
| R15d | Financial stability and resources | shall | 7.1.1(d) |
| R15e | Policies for complaints/disputes | shall | 7.1.1(e) |
| R15f | Documented agreement for third-party arrangements | shall | 7.1.1(f) |
| R16 | Segregate conflicting duties | shall | 7.1.2 |
| R17 | Ensure employees/contractors support trustworthiness | shall | 7.2 |
| R18a | Employ qualified, trained staff/subcontractors | shall | 7.2(a) |
| R18c | Apply disciplinary sanctions for violations | shall | 7.2(c) |
| R18d | Document security roles; identify trusted roles | shall | 7.2(d) |
| R18e | Job descriptions with segregation of duties, least privilege, background screening | shall | 7.2(e) |
| R18f | Personnel follow security management procedures | shall | 7.2(f) |
| R18g | Managerial personnel shall have experience/training | shall | 7.2(g) |
| R18h | No conflict of interest in trusted roles | shall | 7.2(h) |
| R18i | Trusted roles defined (Security Officer, System Admin, Operator, Auditor) | shall | 7.2(i) |
| R18j | Formal appointment to trusted roles; least privilege | shall | 7.2(j) |
| R18k | No access to trusted functions until checks complete | shall | 7.2(k) |
| R19 | Appropriate protection of assets | shall | 7.3.1 |
| R20 | Maintain inventory and classification of assets | shall | 7.3.1 |
| R21 | Secure media handling; dispose sensitive media securely | shall | 7.3.2 |
| R22 | Limit system access to authorized individuals | shall | 7.4 |
| R23a | Firewalls to protect internal network | shall | 7.4(a) |
| R23b | Administer user access; timely modification/removal | shall | 7.4(b) |
| R23c | Restrict access per policy; separation of trusted roles; restrict system utilities | shall | 7.4(c) |
| R23d | Identify and authenticate personnel for critical applications | shall | 7.4(d) |
| R23e | Accountability for activities (event logs) | shall | 7.4(e) |
| R23f | Protect sensitive data from re-used storage objects | shall | 7.4(f) |
| R24 | Security controls for cryptographic keys/devices throughout lifecycle | shall | 7.5 |
| R25 | Control physical access to critical components | shall | 7.6 |
| R26a | Limit physical access to authorized individuals | shall | 7.6(a) |
| R26b | Controls to avoid loss/damage/compromise | shall | 7.6(b) |
| R26c | Controls to avoid compromise/theft | shall | 7.6(c) |
| R26d | Critical components in protected security perimeter with intrusion detection | shall | 7.6(d) |
| R27 | Use trustworthy systems protected against modification | shall | 7.7 |
| R28a | Security requirements analysis at design stage | shall | 7.7(a) |
| R28b | Change control for software releases/patches | shall | 7.7(b) |
| R28c | Protect integrity against malicious software | shall | 7.7(c) |
| R28d | Secure media handling | shall | 7.7(d) |
| R28e | Media management against obsolescence during retention | shall | 7.7(e) |
| R28f | Procedures for trusted/administrative roles | shall | 7.7(f) |
| R28g | Apply security patches within reasonable time; document if not applied | shall | 7.7(g) |
| R29 | Protect network and systems from attack | shall | 7.8 |
| R30a | Segment systems into zones per risk; same controls per zone | shall | 7.8(a) |
| R30b | Restrict inter-zone communications; disable unneeded; review rules | shall | 7.8(b) |
| R30c | Maintain critical systems in secured zone | shall | 7.8(c) |
| R30d | Dedicated administration network separated from operational | shall | 7.8(d) |
| R30e | Separate test, production, development | shall | 7.8(e) |
| R30f | Trusted channels with distinct identification and data protection | shall | 7.8(f) |
| R30g | Redundant external internet connection for availability | shall | 7.8(g) |
| R30h | Regular vulnerability scans; record evidence | shall | 7.8(h) |
| R30i | Penetration tests at setup and after significant changes; record evidence | shall | 7.8(i) |
| R31 | Monitor system activities | shall | 7.9 |
| R32b | Detect and report abnormal activities as alarms | shall | 7.9(b) |
| R32c | Monitor logging functions and service availability/utilization | shall | 7.9(c) |
| R32d | Timely response to incidents; appoint trusted role for alerts | shall | 7.9(d) |
| R32e | Notify appropriate parties of significant breaches (per regulation) | shall | 7.9(e) |
| R32f | Notify affected persons of breach without undue delay | shall | 7.9(f) |
| R32g | Monitor/review audit logs; implement automatic processing | shall | 7.9(g) |
| R32h | Remediate critical vulnerabilities; if not, implement mitigation or document | shall | 7.9(h) |
| R32i | Incident reporting to minimize damage | shall | 7.9(i) |
| R33 | Record and keep accessible all relevant info for legal and continuity | shall | 7.10 |
| R34a | Maintain confidentiality and integrity of records | shall | 7.10(a) |
| R34b | Archive records completely and confidentially per business practices | shall | 7.10(b) |
| R34c | Make records available for legal proceedings | shall | 7.10(c) |
| R34d | Record precise time of significant events; synchronize with UTC daily | shall | 7.10(d) |
| R34e | Hold records for period after expiry of keys/tokens as notified | shall | 7.10(e) |
| R34f | Log events to prevent easy deletion during retention | shall | 7.10(f) |
| R35 | Restore operations after disaster as soon as possible | shall | 7.11 |
| R36 | Define and maintain business continuity plan | shall | 7.11 |
| R37 | Minimize disruption due to termination; maintain verification info | shall | 7.12 |
| R38a | Maintain up-to-date termination plan | shall | 7.12(a) |
| R38b(i) | Inform subscribers and other entities of termination | shall | 7.12(b)(i) |
| R38b(ii) | Terminate subcontractor authorization | shall | 7.12(b)(ii) |
| R38b(iii) | Transfer obligations for maintaining evidence to reliable party | shall | 7.12(b)(iii) |
| R38b(iv) | Destroy private keys irrecoverably | shall | 7.12(b)(iv) |
| R38c | Arrange to cover termination costs in bankruptcy | shall | 7.12(c) |
| R38d | State termination provisions in practices (notification and transfer) | shall | 7.12(d) |
| R38e | Maintain or transfer obligation to make public key/tokens available | shall | 7.12(e) |
| R39 | Operate legally and trustworthily | shall | 7.13 |
| R40a | Provide evidence of meeting legal requirements | shall | 7.13(a) |
| R40b | Make services accessible for persons with disabilities | shall | 7.13(b) |
| R40c | Protect personal data from unauthorized processing and loss | shall | 7.13(c) |

## Informative Annexes (Condensed)
- **Annex A (Bibliography)**: Lists additional references: ISO/IEC 27001:2013 and CA/Browser Forum Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates. These are not normative but provide further guidance.