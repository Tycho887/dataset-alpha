# ETSI TR 102 040 V1.3.1: Electronic Signatures and Infrastructures (ESI); International Harmonization of Policy Requirements for CAs issuing Certificates
**Source**: ETSI | **Version**: V1.3.1 | **Date**: 2005-03 | **Type**: Informative
**Original**: https://www.etsi.org/deliver/etsi_tr/102000_102099/102040/01.03.01_60/tr_102040v010301p.pdf

## Scope (Summary)
This Technical Report presents ongoing work to harmonize ETSI Technical Specifications on policy requirements for certification authorities (TS 101 456 and TS 102 042) with internationally recognized standards. The aim is to identify a way forward to meet the requirements of the European Electronic Signature Directive 1999/93/EC while operating within an internationally harmonized certificate policy framework to facilitate cross-recognition between PKI policy environments.

## Normative References
- [1] ETSI TS 101 456: "Policy requirements for certification authorities issuing qualified certificates"
- [2] ETSI TS 102 042: "Policy requirements for certification authorities issuing public key certificates"
- [3] IETF RFC 2527: "Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework" (obsoleted by RFC 3647)
- [4] IETF RFC 3647: "Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework" (obsoletes RFC 2527)
- [5] ISO/IEC 14516: "Information technology - Security techniques - Guidelines for the use and management of Trusted Third Party services"
- [6] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures
- [7] American Bar Association: "PKI Assessment Guidelines (PAG)"
- [8] ANSI X9.79: "Financial Services Public Key Infrastructure (PKI) Policy and Practices Framework"
- [9] ISO/DIS 21188: "Public key infrastructure for financial services - Practices and policy framework"
- [10] CEN CWA 14172-1: "EESSI Conformity Assessment Guidance Part 1 - General"
- [11] CEN CWA 14172-2: "EESSI Conformity Assessment Guidance - Part 2: Certification Authority services and processes"
- [12] ITU-T Recommendation X.509 (2000) | ISO/IEC 9594-8 (2001): "Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks"
- [13] CEN CWA 14167-1: "Security Requirements for Trustworthy Systems Managing Certificates for Electronic Signatures - Part 1: System Security Requirements"
- [14] ISO 15782-1: "Certificate management for financial services - Part 1: Public key certificates"

## Definitions and Abbreviations
### Definitions
- **certificate**: public key of a user, together with some other information, rendered un-forgeable by encipherment with the private key of the certification authority which issued it (see ITU-T Recommendation X.509 | ISO/IEC 9594-8 [12]).
- **certificate policy**: named set of rules that indicates the applicability of a certificate to a particular community and/or class of application with common security requirements (see ITU-T Recommendation X.509 | ISO/IEC 9594-8 [12]).
- **certification authority**: authority trusted by one or more users to create and assign certificates (see ITU-T Recommendation X.509 | ISO/IEC 9594-8 [12]).
- **certification practice statement**: statement of the practices which a certification authority employs in issuing certificates (see RFC 3647 [4]).

### Abbreviations
- ABA: American Bar Association
- AICPA: American Institute of Certified Public Accountants
- ANSI: American National Standards Institute
- APEC: Asia-Pacific Economic Community
- CA: Certification Authority
- CEN: Comité Européen de Normalisation
- CICA: Canadian Institute of Chartered Accountants
- EESSI: European Electronic Signature Standardization Initiative
- eSTG: eSecurity Task Group
- FPKI: Federal Public Key Infrastructure
- IETF: Internet Engineering Task Force
- ISC: Information Security Committee
- ISO: International Organization for Standardization
- ISSS: Information Society Standardisation System
- PAG: PKI Assessment Guidelines (see [7])
- PKI: Public Key Infrastructure
- PKIX: Public Key Infrastructure X.509 based
- QCP: Qualified Certificate Policy (see [1])
- WPISP: Working Party on Information Security and Privacy

## 4 Objective
The major objective is achieving harmonization between internationally recognized policies (not constrained by the European legal framework) and CA policy requirements that meet the European electronic signature Directive 1999/93/EC [6]. Specific aims:
- Ensure European CAs have at least equal recognition in the wider international marketplace.
- Ensure certification systems accredited under internationally recognized standards can also meet the security and management requirements of European approval schemes.
- Achieve a simple relationship between the structure and requirements of ETSI documents and other internationally recognized standards.

## 5 Relevant Activities
### 5.1 Introduction
Identifies activities most closely related to TS 101 456 (ETSI QCP) and TS 102 042 that are already aligned with these ETSI specifications.

### 5.2 IETF PKIX Policy and Practices Framework
- IETF PKIX published RFC 2527 [3] (March 1999) providing a structure for certificate policies and CPS.
- Revised as RFC 3647 [4] (November 2003) with significant changes in recommended structure; adopted by Federal PKI and APEC.
- ETSI QCP developed around RFC 2527/3647; mapping annex in TS 101 456. Most international schemes are based on these RFCs.

### 5.3 ABA PKI Assessment Guidelines
- ABA ISC produced the PKI Assessment Guidelines (PAG) [7] (2003) providing general legal perspective, not specific requirements.
- Includes limited guidance on European legislation.

### 5.4 US Federal PKI
- US Federal PKI (FPKI) based on a Bridge CA with a Federal Bridge CA Certificate Policy.
- ETSI ESI and US FPKI developed a mapping document; on July 7, 2004, US GSA declared the ETSI QCP "fundamentally comparable to the USPKI Federal Bridge Certification Authority (FBCA) Certificate Policy at the medium assurance level".
- Comparability achieved also considering CEN CWAs 14167-1 [13], 14172-1 [10], 14172-2 [11].
- Future work suggested on opposite mapping for recognition of US CAs in Europe.

### 5.5 APEC TEL eSTG
- eSecurity Task Group of APEC TEL works on security of information infrastructure and interoperability of authentication schemes.
- Produced "Guidelines for Schemes to Issue Certificates Capable of Being Used in Cross Jurisdiction eCommerce" based on analysis of policies including ETSI QCP.
- Table 1 lists compared schemes: Australia Gatekeeper Grade 2, Type 2; Canada Government of Canada PKI Medium; EU ETSI QCP; Hong Kong Recognized certificate; Singapore Licensed CA; US FBCA Medium.
- APEC model near completion includes nearly all ETSI proposed amendments; direct analysis still necessary.

### 5.6 ANSI X9.79 - PKI Policy and Practices Framework
- ANSI X9.79 [8] (annex B) includes PKI policy requirements similar to TS 101 456; used as starting point for TS 101 456 and TS 102 042.
- Does not mandate specific requirements; leaves selection to CA.
- Adopted as basis for AICPA/CICA WebTrust Program for CAs.

### 5.7 ISO TC68 - PKI Policy and Practices Framework
- ISO/DIS 21188 [9] based on ANSI X9.79; European members requested alignment with Directive 1999/93/EC and TS 101 456.
- Published as Committee Draft October 2002; progressed to DIS end of 2004; likely ISO standard end of 2005.
- Directed at financial sector with less broad applicability; PKI systems could conform to both ISO standard and ETSI QCP but not directly equivalent; ETSI avoided unnecessary divergence.

### 5.8 OECD
- OECD WPISP looking at authentication around cross-border electronic transactions; ETSI provided a note on harmonized approval criteria for Trust Service Providers; activity uncertain.

## 6 Recommendations
- ETSI ESI has been active in international harmonization and successful in maximizing alignment with ETSI QCP.
- All schemes are broadly similar to ETSI QCP, based on RFC 2527/3647; policy requirements often directly equivalent.
- Differences remain due to differing aims and administrative environments.
- Adoption of RFC 3647 by many organizations; mapping current QCP to RFC 3647-based documents is complex; RFC 3647 introduces additional security requirements. Future work suggested on ETSI QCP to mirror RFC 3647 better.
- Lack of specific auditing requirements in TS 101 456 was addressed by adding CEN CWA 14172-2 or comparable national voluntary accreditation schemes; other EESSI specifications needed.
- Cross-recognition requires detailed element-by-element analysis (as done in FPKI-ETSI QCP mapping).
- APEC nearing completion of guidelines; impact yet to be seen.
- Continuation of harmonization effort on detailed analysis is suggested, especially completing inverse mapping between TS 101 456 and US Federal PKI.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| (Not applicable – this is a Technical Report, not a normative specification.) | | | |

## Informative Annexes (Condensed)
- **Annex A: Letter from US on Mapping to US Federal PKI**: Contains official correspondence stating that the ETSI QCP is fundamentally comparable to the US FBCA Certificate Policy at medium assurance. (The full text of the letter is included in the original document but is not reproduced here.)
- **History**: Document history: V1.1.1 (March 2002), V1.2.1 (February 2004), V1.3.1 (March 2005) – all publications.