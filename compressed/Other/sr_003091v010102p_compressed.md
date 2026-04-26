# ETSI SR 003 091 V1.1.2: Electronic Signatures and Infrastructures (ESI); Recommendations on Governance and Audit Regime for CAB Forum Extended Validation and Baseline Certificates
**Source**: ETSI | **Version**: V1.1.2 | **Date**: March 2013 | **Type**: Informative (Special Report)
**Original**: https://www.etsi.org/deliver/etsi_sr/003000_003099/003091/01.01.02_60/sr_003091v010102p.pdf

## Scope (Summary)
The present document recommends a Governance and Audit Regime for CAB Forum Extended Validation (EV) and Baseline certificates based on ETSI specifications (TS 102 042, TS 119 403, TR 101 564, TR 103 123). It also recommends an interim approach where the full audit and governance infrastructure does not exist.

## Normative References
- Not applicable.

## Informative References
- [i.1] ETSI TS 102 042: "Electronic Signatures and Infrastructures (ESI); Policy requirements for certification authorities issuing public key certificates".
- [i.2] CA/Browser Forum: "Guidelines For The Issuance And Management Of Extended Validation Certificates".
- [i.3] CA/Browser Forum: "Baseline Requirements for the Issuance and Management of Publicly-Trusted Certificates".
- [i.4] ETSI TR 101 564: "Electronic Signatures and Infrastructures (ESI); Guidance on ETSI TS 102 042 for Issuing Extended Validation Certificates for Auditors and CSPs".
- [i.5] ETSI TS 119 403: "Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment - General requirements and guidance".
- [i.6] Regulation (EC) No 765/2008 of the European Parliament and of the Council of 9 July 2008.
- [i.7] ISO/IEC 17021: "Conformity assessment - Requirements for bodies providing audit and certification of management systems".
- [i.8] EN 45011: "General requirements for bodies operating product certification systems (ISO/IEC Guide 65:1996)".
- [i.9] ISO DIS 17065: "Conformity assessment -- Requirements for bodies certifying products, processes and services".
- [i.10] Recommendation ITU-T X.509.
- [i.11] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999.
- [i.12] ISO 32000: "Document management -- Portable document format".
- [i.13] ISO 27001: "Information technology -- Security techniques -- Information security management systems -- Requirements".
- [i.14] ETSI TR 103 123: "Electronic Signatures and Infrastructures (ESI); Guidance for Auditors and CSPs on ETSI TS 102 042 for Issuing Publicly-Trusted TLS/SSL Certificates".

## Definitions and Abbreviations
- Terms and abbreviations as given in TS 102 042 [i.1] and TS 119 403 [i.5] apply.

## 4 Basis for EV and Baseline Audit

### 4.1 EV Audit
- **[R1]**: An audit **shall** be carried out on Certification Authorities issuing Extended Validation Certificates.
- **[R2]**: It **should** be based on the checklist given in annex A of TR 101 564 [i.4] (which combines TS 102 042 [i.1] and CAB Forum EV Guidelines [i.2]).
- **Note**: Base documents **should** be used as reference in case of uncertainty.

### 4.2 Baseline Audit
- **[R3]**: An audit **shall** be carried out on Certification Authorities issuing SSL Baseline Certificates.
- **[R4]**: It **should** be based on the checklist given in annex A of TR 103 123 [i.14] (which combines TS 102 042 [i.1] and CAB Forum Baseline Requirements [i.3]).
- **Note**: Base documents **should** be used as reference in case of uncertainty.

## 5 Audit Process/Conformity Assessment
- **[R5]**: The audit **should** be carried out by a conformity assessment body (CAB) accredited by the national accreditation body in the sense of Article 4 of Regulation (EC) No 765/2008 [i.6] (members of EA).
- **[R6]**: The conformity assessment body **should** have an accreditation certificate for assessments against TS 102 042 [i.1], CAB Forum EV Guidelines [i.2], and CAB Forum Baseline Requirements [i.3].
- **[R7]**: The assessment **should** be performed in line with procedures defined in TS 119 403 [i.5].
- **Interim (R8)**: In the absence of an accreditation scheme, a body accredited against ISO 27001 [i.13] may be considered sufficient provided it can demonstrate auditors have necessary qualifications per TS 119 403 [i.5] clause 6.2 (PKI knowledge, X.509, identity registration).
- **[R9]**: Where possible, the audit **should** be in line with TS 119 403 [i.5]; otherwise at least in line with ISO/IEC 17021 [i.7] or EN 45011 [i.8] (under revision as ISO/IEC DIS 17065 [i.9]).
- **[R10]**: An audit report **should** be produced (suggested content in TR 101 564 [i.4] annex B). Based on it, the CAB **should** publish a conformity certificate including at minimum the names of CA and audited certification service, the relevant specification ([i.1] and [i.2] or [i.3]), the certificate policy (e.g. EVCP), and the geographical location (address) of the CA's headquarter.
- **[R11]**: An audit **should** be carried out at least every 3 years or upon major change to the CA. Surveillance activities are required on an annual basis.

## 6 Assessment Status Notification
- **[R12]**: Per ISO 17021 [i.7] and EN 45011 [i.8], CABs **shall** make publically accessible (or provide on request) a directory of valid conformity assessments.
- **[R13]**: Where a notification scheme exists in line with TS 119 403 [i.5], the scheme operator **should** require national CABs to send results of conformity assessments; the operator **should** publish all results in a single list as described in TS 119 403 [i.5].
- **[R14]**: In the absence of such a notification scheme, a conformity certification **should** be published by the CAB only, preferably in PDF format protected by its digital signatures per ISO 32000 [i.12]. CABs **should** also inform ETSI ESI secretariat of the publication location for linking from the ETSI web page.
- **Note**: Application providers may establish their own trusted root lists; requirements of their programs (e.g. Microsoft, Mozilla, Opera, Apple, Google, Oracle, Adobe) should be taken into account.

## 7 Governance
- **[R15]**: The competence of the CAB **should** be accredited by a National Accreditation body coordinated through EA and regulated under Regulation (EC) No 765/2008 [i.6].
- **[R16]**: Where a national or international TSP notification scheme exists in line with TS 119 403 [i.5], the scheme operator **should** be responsible for its notifications.
- **Short term (R17)**: Each CAB may be responsible for applying its own policy for notifying its own conformity assessments in line with its accreditation.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | An audit shall be carried out on CAs issuing EV certificates. | shall | 4.1 |
| R2 | The EV audit should be based on TR 101 564 Annex A checklist. | should | 4.1 |
| R3 | An audit shall be carried out on CAs issuing SSL Baseline certificates. | shall | 4.2 |
| R4 | The Baseline audit should be based on TR 103 123 Annex A checklist. | should | 4.2 |
| R5 | Audit should be by a CAB accredited under Regulation 765/2008. | should | 5 |
| R6 | CAB should have accreditation for TS 102 042, EV Guidelines, Baseline Requirements. | should | 5 |
| R7 | Assessment should be performed per TS 119 403 procedures. | should | 5 |
| R8 | In absence of accreditation, ISO 27001 accredited body may be sufficient with qualified auditors. | may | 5 |
| R9 | Audit should be in line with TS 119 403; otherwise at least ISO/IEC 17021 or EN 45011. | should | 5 |
| R10 | Audit report and certificate with minimum content shall be published. | should (report) / shall (certificate) | 5 |
| R11 | Audit every 3 years or upon major change; annual surveillance. | should | 5 |
| R12 | CABs shall make directory of valid assessments publicly accessible. | shall | 6 |
| R13 | Scheme operator should publish single list of results if scheme exists. | should | 6 |
| R14 | If no scheme, CAB should publish certificate in PDF with digital signature and inform ETSI. | should | 6 |
| R15 | CAB competence should be accredited by national body under Regulation 765/2008. | should | 7 |
| R16 | Scheme operator should be responsible for notifications if scheme exists. | should | 7 |
| R17 | Short-term: CAB may apply own policy for notifications. | may | 7 |

## Informative Annexes (Condensed)
- **Annex A (Bibliography)**: Lists ETSI TS 103 090 ("Conformity Assessment for Trust Service Providers issuing Extended Validation Certificates") as a related document.