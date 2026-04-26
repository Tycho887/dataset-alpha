# ETSI TR 102 458 V1.1.1: Electronic Signatures and Infrastructures (ESI); Mapping Comparison Matrix between the US Federal Bridge CA Certificate Policy and the European Qualified Certificate Policy (TS 101 456)
**Source**: ETSI TC ESI | **Version**: V1.1.1 | **Date**: April 2006 | **Type**: Technical Report (Informative)
**Original**: DTR/ESI-000033

## Scope (Summary)
This Technical Report compares the US Federal Bridge Certification Authority (FBCA) Certificate Policy (Version 2, 2005) at the Medium assurance level (including Medium Hardware and Medium – Commercial Best Practices) with the European Qualified Certificate Policy (QCP) as specified in ETSI TS 101 456. The mapping identifies the degree of alignment between FBCA CP stipulations and QCP requirements to facilitate cross-certification assessments. It is the reverse of an earlier FBCA mapping from QCP to FBCA CP.

## Normative References
- [1] Directive 1999/93/EC (EU Electronic Signatures Directive)
- [2] ETSI TS 101 456: "Policy requirements for certification authorities issuing qualified certificates"
- [3] X.509 Certificate Policy For The Federal Bridge Certification Authority (FBCA CP) – Version 2, September 13, 2005
- [4] ETSI Federal PKI CPWG Mapping Comparison Matrix (FBCA v1 ↔ QCP TS 101 456 V1.2.1) – under revision
- [5] Template for Cross-Certifying Memorandum of Agreement (MoA)
- [6] US Government PKI – Cross Certification Criteria and Methodology, Version 1.2, June 2005
- [7] ITU-T Recommendation X.509 (Public-key and attribute certificate frameworks)
- [8] IETF RFC 3647: "Certificate Policy and Certification Practices Framework"

## Definitions and Abbreviations
- **certificate policy (CP)**: named set of rules indicating applicability of a certificate to a particular community/class of application (see ITU-T X.509)
- **Entity CA**: CA acting on behalf of an Entity, under its operational control (FBCA CP)
- **qualified certificate**: certificate meeting annex I of Directive [1] and provided by a CSP fulfilling annex II requirements
- **Qualified Certificate Policy (QCP)**: QCP public + SSCD: a policy for qualified certificates requiring secure signature-creation devices (TS 101 456)
- **subject**: entity identified in a certificate as the holder of the private key
- **Subscriber**: (FBCA CP) entity whose name appears as subject, uses its key and certificate in accordance with CP, and does not issue certificates; (QCP) entity subscribing on behalf of one or more subjects
- **The Directive**: Directive 1999/93/EC
- **Abbreviations**: CA, CP, FBCA, IETF, MoA, OID, PKI, QCP

## 4 PKI Summaries
### 4.1 QCP
The QCP is a certificate policy framework for Qualified Certificates issued to the public in compliance with Annexes I and II of Directive 1999/93/EC. Qualified certificates support electronic signatures that satisfy the requirements of a hand-written signature (Article 5.1). Adoption is not mandatory; several Directive-compliant CAs have adopted QCP.

### 4.2 FBCA CP
The FBCA CP defines seven certificate policies for five assurance levels (Rudimentary, Basic, Medium, Medium Hardware, High) to facilitate interoperability among Entity PKI domains in a peer-to-peer fashion. The FBCA issues certificates only to Principal CAs designated by Entities. Use of FBCA CP OIDs outside the Federal PKI Policy Authority is at the using party's risk. The CP is consistent with IETF RFC 3647 and governed by applicable Federal law.

## 5 Mapping the FBCA CP to the QCP
### 5.1 Comparative Evaluation Terms
The mapping uses the same seven terms as the FBCA’s opposite mapping [4]:
- **Exceeds**: Higher assurance than QCP requirement.
- **Equivalent**: Exactly the same assurance.
- **Comparable**: Comparable level of assurance.
- **Partial**: Comparable but does not address entire QCP requirement.
- **Not Comparable**: Lower assurance.
- **Missing**: No comparable content.
- **N/A**: Mapping not appropriate.
- **Shaded**: QCP does not address the topic.

### 5.2 Summary Assessment
The table below shows the overall degree of alignment for each QCP clause. “Overall Match” values are taken from clause 5.3 detailed assessment.

| QCP Clause | FBCA CP Reference | Comparison Rating |
|---|---|---|
| 5.3 Applicability | 1.4.1 | COMPARABLE |
| 5.4 Conformance | 8, 8.5, MoA (IV.A.2) | EQUIVALENT |
| 6.1 CA obligations | MoA (IV.D) | COMPARABLE |
| 6.2 Subscriber obligations | 6.1.1.2, 7.1.3, 9.6.3 | COMPARABLE |
| 6.3 Relying party obligations | 4.9.6, 4.5.2 | COMPARABLE |
| 6.4 Liability | 9.8 | POINT OF NOTE 1 |
| 7.1 Certification practice statement | 1.5.3 | COMPARABLE |
| 7.2.1 CA key generation | 5.1.1, 5.1.2.1, 6.1.1.1, 6.1.5, 6.1.6, 6.3.2 | POINT OF NOTE 2 |
| 7.2.2 CA key storage, backup, recovery | 6.2.1, 6.2.4.1 | POINT OF NOTE 2 |
| 7.2.3 CA public key distribution | 6.1.4 | EQUIVALENT |
| 7.2.4 Key escrow | 6.2.3.1, 6.2.3.3 | EQUIVALENT |
| 7.2.5 CA key usage | 6.1.7, 5.1.2.1 | EQUIVALENT |
| 7.2.6 End of CA key life cycle | 6.2.9, 6.2.10 | POINT OF NOTE 3 |
| 7.2.7 Cryptographic hardware lifecycle | 5.1.2.1, 6.2.9 | COMPARABLE |
| 7.2.8 CA provided subject key management | 6.1.1.2, 6.1.1.3, 6.1.5, 6.1.6 | COMPARABLE |
| 7.2.9 SSCD preparation | 6.1.1.2, 6.1.2, 6.2.8, 6.2.9, 6.2.10 | COMPARABLE |
| 7.3.1 Subject registration | 3.2.1, 3.2.3.1, 3.2.3.2, 3.2.3.3, 9.6.3 | EQUIVALENT |
| 7.3.2 Certificate renewal, rekey, update | 4.6, 4.7, 4.8, 3.3.1 | COMPARABLE |
| 7.3.3 Certificate generation | 7.1, 4.3, 3.2.1, 6.1.2, 3.1.5, 9.4, 3.2.3.1, 6.7 | COMPARABLE |
| 7.3.4 Dissemination of terms and conditions | 9.6.3 | COMPARABLE, POINT OF NOTE 4 |
| 7.3.5 Certificate dissemination | 2.2.1, 2.2.2, 2.3, 2.4 | COMPARABLE, POINT OF NOTE 4 |
| 7.3.6 Certificate revocation and suspension | 2.2.1, 2.4, 3.4, 4.9, 4.9.1, 4.9.2, 4.9.3, 4.9.5, 4.9.7, 4.9.9, 4.9.13, 5.7.4 | COMPARABLE, POINT OF NOTE 4, 8, 9 |
| 7.4.1 Security management | 1.3.1.6, 1.3.2, 1.3.5, 1.4.1, 1.5.1, 6.6.2, 8, 8.3 | COMPARABLE, POINT OF NOTE 5 |
| 7.4.2 Asset classification and management | General – policy targeted at specific information needs | COMPARABLE, POINT OF NOTE 5 |
| 7.4.3 Personnel security | 5.2.1, 5.2.4, 5.3.1, 5.3.3, 5.3.4, 5.3.7, 5.3.8 | COMPARABLE |
| 7.4.4 Physical and environmental security | 5.1 | COMPARABLE |
| 7.4.5 Operations management | 6.6.1, 5.4.2, 5.4.8, 5.1.2.1, 5.2.1, 5.1.6, 5.5.3, 6.2.4, 4.8.4, 5.4.2, 5.4.8, 5.7.1, MoA, 5.4.6 | COMPARABLE, POINT OF NOTE 4, 10 |
| 7.4.6 System access management | 6.7, 6.5.1, 5.1.2.1, 6.6.2, 2.4 | COMPARABLE |
| 7.4.7 Trustworthy systems deployment | 6.6.1, 6.6.2 | EQUIVALENT |
| 7.4.8 Business continuity and incident handling | 5.7.4, 5.1.8, 5.7.3 | COMPARABLE |
| 7.4.9 CA termination | 5.8 | POINT OF NOTE 6 |
| 7.4.10 Compliance with legal requirements | 9.4 | COMPARABLE, POINT OF NOTE 5, 8 |
| 7.4.11 Recording of information | 5.5, 4.6.2 | COMPARABLE |
| 7.5 Organizational | 1.1.5, cross cert criteria [6], 1.3.1.1, 1.3.1.2, 9.6.1, 9.1.3, 5.2.1 | COMPARABLE |

### 5.2.2 Points of Note (Condensed)
1. **Liability (QCP 6.4)**: Specific legal advice should be sought regarding liability under Article 6 of the EU Directive [1] and US commercial/governmental liability.  
2. **CA key generation/storage (QCP 7.2.1, 7.2.2)**: FBCA Medium assurance currently requires FIPS 140-1 Level 2 (QCP requires Level 3). The FBCA policy committee is moving to Level 3; most Entity CAs already use Level 3.  
3. **End of CA key life cycle (QCP 7.2.6)**: FBCA CP does not address CA key destruction; under investigation.  
4. **Service levels (QCP 7.3.4, 7.3.5, 7.3.6, 7.4.5)**: FBCA does not directly address subscriber/relying party service levels where security is unaffected (e.g., notification of revocation status change). US E-Authentication programme may add references.  
5. **Security management and asset classification (QCP 7.4.1, 7.4.2, 7.4.10)**: FBCA CP does not require formal risk assessment or asset classification, but audit against the CP ensures comparable security. EU Data Protection not applicable to US; personal information exchange considered unnecessary beyond certificate content.  
6. **CA termination (QCP 7.4.9)**: FBCA lacks requirements for maintaining revocation information after termination; under investigation.  
7. **Algorithm compromise (QCP 7.4.8, Annex A)**: FBCA Policy Authority will revise policy in real time; see Annex A memo.  
8. **Subscriber notification for revocation (QCP 7.3.6)**: Under investigation by Federal PKI.  
9. **Suspension (QCP 7.3.6)**: Handling of suspension for Entity CAs unspecified.  
10. **Incident response (QCP 7.4.5)**: FBCA requires log review at least every two months, but specific timely response measures unclear.

### Requirements Summary (Key Equivalences and Deviations)
| ID | Requirement Area | Type | Reference | Rating | Comments |
|---|---|---|---|---|---|
| R1 | Conformance to CP | shall | QCP 5.4 | EQUIVALENT | FBCA audit mechanism + MoA provisions match QCP conformance requirements. |
| R2 | Key escrow prohibition | shall | QCP 7.2.4 | EQUIVALENT | FBCA CP explicitly prohibits escrow of CA and subscriber signature keys. |
| R3 | CA key usage | shall | QCP 7.2.5 | EQUIVALENT | Rules enforced via X.509 key usage extensions and physical controls. |
| R4 | Subject registration | shall | QCP 7.3.1 | EQUIVALENT | FBCA in-person identity proofing and verification processes align. |
| R5 | Trustworthy systems deployment | shall | QCP 7.4.7 | EQUIVALENT | FBCA requires formal development, change control, and dedicated CA hardware/software. |
| R6 | Cryptographic module strength (CA keys) | shall | QCP 7.2.1, 7.2.2 | POINT OF NOTE | FBCA Medium requires FIPS 140-2 Level 2 (vs QCP Level 3); upgrade planned. |
| R7 | CA key destruction | shall | QCP 7.2.6 | POINT OF NOTE | FBCA does not specify CA key destruction; subscriber key destruction is covered. |
| R8 | Service availability (repository/revocation) | should | QCP 7.3.5, 7.3.6 | COMPARABLE | FBCA provides 24/7 for FBCA directory but Entity repository availability not mandated. |
| R9 | Suspension | may | QCP 7.3.6 | POINT OF NOTE | FBCA prohibits suspension; Entity CA handling unspecified. |

## Informative Annexes (Condensed)
- **Annex A: Memo from Chair, U.S. Federal PKI Policy Authority (Nov 25, 2005)**: In the event of algorithm compromise, the Policy Authority will immediately revise its policy documents to remove the failed algorithm and require a new secure algorithm. This real-time policy enforcement capability is relevant to mapping requirements for algorithm compromise handling (QCP 7.4.8). 

--- 

*Note: This compressed version preserves all normative references, definitions, and key mapping results. The full detailed assessment (clause 5.3) contains exhaustive per-requirement comparisons and is available in the original document.*