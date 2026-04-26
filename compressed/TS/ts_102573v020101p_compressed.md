# ETSI TS 102 573: Electronic Signatures and Infrastructures (ESI); Policy requirements for trust service providers signing and/or storing data objects
**Source**: ETSI | **Version**: V2.1.1 | **Date**: April 2012 | **Type**: Normative (Technical Specification)

## Scope (Summary)
This document specifies policy requirements for Trusted Service Providers (TSP) that electronically sign and/or store data objects on behalf of customers (or for themselves). It addresses regulatory requirements for producing and reliably keeping electronic data objects, including fiscally relevant ones, using Advanced Electronic Signatures (AdES) or Qualified Electronic Signatures (QES). The policies are based on commonly acceptable practices across EU Member States and are intended for use by independent assessors.

## Normative References
- [1] CEN CWA 14169: "Secure signature-creation devices 'EAL 4+'"
- [2] CEN CWA 15579: "E-invoices and digital signatures"
- [3] CEN CWA 15580: "Storage of Electronic Invoices"
- [4] ISO/IEC 27002: "Information technology - Security techniques - Code of practice for information security management"
- [5] ISO/IEC 27001: "Information technology - Security techniques - Information security management systems - Requirements"
- [6] ISO/IEC 15408 (parts 1–3): "Evaluation criteria for IT security"
- [7] Directive 95/46/EC: Data protection
- [8] Directive 1999/93/EC: Electronic signatures
- [9] Council Directive 2006/112/EC (as amended by 2010/45/EU): VAT
- [10] Council Directive 2001/115/EC: Invoicing amendments
- [11] ETSI TS 101 456: Policy requirements for CAs issuing qualified certificates
- [12] ETSI TS 102 042: Policy requirements for CAs issuing public key certificates
- [13] ETSI TS 102 176-1: Algorithms and Parameters for Secure Electronic Signatures
- [14] ETSI TS 102 734: Profiles of CMS Advanced Electronic Signatures (CAdES)
- [15] ETSI TS 102 904: Profiles of XML Advanced Electronic Signatures (XAdES)
- [16] ETSI TS 101 733: CMS Advanced Electronic Signatures (CAdES)
- [17] ETSI TS 101 903: XML Advanced Electronic Signatures (XAdES)
- [18] CEN CWA 14170: Security requirements for signature creation applications
- [19] ETSI TS 102 778: PDF Advanced Electronic Signature Profiles
- [20] ETSI TS 102 918: Associated Signature Containers (ASiC)

## Definitions and Abbreviations
- **Advanced electronic signature**: Electronic signature per Art. 5 No. 2 of Directive 1999/93/EC [8].
- **Commonly acceptable practices**: Practices for TSPs signing/storing fiscally relevant data recognized as acceptable by authorities in several EU nations.
- **Electronic invoices**: Invoices sent electronically as defined in Directive 2006/112/EC [9].
- **Extended policy requirements (N+)**: Normalized requirements plus use of Secure Signature Creation Device and Qualified Certificate (i.e., qualified electronic signatures).
- **Fiscally relevant data**: Financial data of a taxable person or company that may need to be exhibited to a regulatory authority.
- **Fiscally relevant data object**: Data object containing fiscally relevant data.
- **Normalized policy requirements (N)**: Equivalent quality to Directive 1999/93/EC [8], employing advanced electronic signatures.
- **Qualified electronic signature**: Advanced signature based on a qualified certificate and created by a secure-signature-creation device ([8]).
- **Qualified certificate**: Certificate meeting Annex I of [8] issued by a CSP fulfilling Annex II.
- **Secure signature creation device**: Device meeting Annex III of [8].
- **Signature creation data**: Unique data (e.g., private keys) used to create an electronic signature.
- **Statement of applicability**: Document describing controls selected for the TSP's ISMS per ISO/IEC 27001 [5].
- **Trading partner**: Taxable person exchanging legally relevant data objects with the TSP's user.
- **Abbreviations**: AdES, CA, CAP, CEN, CMS, CRL, CWA, DPSP, EAL, EU, EUMS, ISMS, ISO, N, N+, QES, TLS, TSP, VAT, WORM, XBRL, XML.

## Notation
- Requirements without marking: mandatory.
- `[CONDITIONAL]` with `[N]` or `[N+]`: applicable only if that policy class is chosen.
- `[CHOICE]` with `[N]` or `[N+]`: selection based on policy class.

## 5 General Concepts (Condensed)
5.1 Requires an ISO/IEC 27001 [5] conformant ISMS (or recognized alternative) to apply controls. No requirement for a specific information security policy format.
5.2.1 Fiscally relevant data objects include VAT invoices (Directive 2006/112/EC [9]).
5.2.2 Basic model: fiscally relevant data input → signing & storage → retrieval for reporting/audit.
5.2.3 TSPs should follow commonly acceptable practices identified in TR 102 572 [i.2]. Art. 233 of Directive 2006/112/EC allows taxable persons to choose mechanisms to ensure authenticity/integrity; AdES/QES are examples but not mandatory.
5.3 Two policy classes: Normalized (N) and Extended (N+, QES).
5.4 Applicable to TSPs, organizations signing/storing for themselves, and independent service providers.
5.5 Conformance requirements: TSP must demonstrate meeting obligations (clause 6), implement controls from annexes A and B, and produce a Statement of Applicability as per ISO/IEC 27001 [5].

## 6 Obligations
### 6.1 Trust service providers obligations
- **R1**: The TSP shall ensure all requirements in annexes A and B are implemented as applicable.
- **R2**: The TSP has responsibility for conformance even when sub-contractors are used.
- **R3**: The TSP shall provide trust services in line with service agreements and applicable legislation.
- **R4**: The TSP shall obtain necessary legal authorizations from subscribers to sign and/or store data objects on their behalf. (See note for two implementation methods.)

### 6.2 Trust service providers organizational requirements
The TSP shall ensure its organization is reliable regarding:
- Issuing data objects in name/behalf of taxable persons.
- Electronically keeping issued data objects as per agreements.

**TSP general requirements:**
- Legal entity; adequate liability coverage; financial stability; ability to transfer service if needed; complaint/dispute resolution policy; proper agreements for subcontracting/outsourcing.
**Issuance and storage:**
- Independence of decisions; documented impartial structure.

### 6.3 Subscriber obligations
The TSP shall oblige the subscriber to:
- Ensure accuracy/legal compliance of submitted data objects.
- Submit only in required formats (SS.3.5).
- Submit accurate registration data.
- Ensure security of keys/security tokens.
- Apply notified security measures when accessing storage.
- Agree that signatures are made with TSP's key or (if applicable) user's key.

### 6.4 Information for trading partner
Terms shall include notice that:
- Relying party shall verify signed data object validity (certificate status, limitations).
- Shall abide by security measures for accessing TSP storage.

### 6.5 Information for auditor/regulatory/tax authorities
Authorities should be notified that they should:
- Verify validity of signed data objects (certificate status, limitations).
- Apply security measures when accessing storage.

## Annex A (normative): Objectives and controls - signature and storage

| ID | Requirement | Type | Reference |
|---|---|---|---|
| SS.1.1.1 | If electronic data objects are signed, the signature shall be at least an Advanced Electronic Signature. [CONDITIONAL] [N+]: shall be created using a Secure Signature Creation Device and supported by a Qualified Certificate. | shall | A, SS.1.1.1 |
| SS.1.2.1 | Electronically signed fiscally relevant data objects shall be supported by certificates issued by CAs operating under policies as per TS 102 042 [12] (NCP) [CHOICE N] or TS 101 456 [11] (qualified) [N+]. | shall (with choice) | A, SS.1.2.1 |
| SS.1.3.1 | Security controls shall be applied to signing keys suitable to ensure security. [CHOICE N] [N+]: key in secure signature creation device meeting CWA 14169 [1] or EAL 4+ per ISO/IEC 15408 [6]. | shall (with choice) | A, SS.1.3.1 |
| SS.1.3.2 | Where TSP holds keys on behalf of individuals, the TSP shall ensure the signing key is under sole control of the owner. | shall | A, SS.1.3.2 |
| SS.1.3.3 | Where a signing key held by the TSP belongs to a legal person, the TSP should ensure signatures can be issued only under control of authorized users. | should | A, SS.1.3.3 |
| SS.1.4.1 | Subject’s registration shall be performed in line with TS 102 042 [12] (N) or TS 101 456 [11] (N+). | shall (with choice) | A, SS.1.4.1 |
| SS.1.5.1 | Revocation shall be requested in a timely manner by an authorized subject. Certificate revocation shall be performed in line with TS 102 042 [12] (N) or TS 101 456 [11] (N+). | shall (with choice) | A, SS.1.5.1 |
| SS.2.1 | Signature verifiability shall be ensured for entire storage period (technical and/or organizational measures). | shall | A, SS.2.1 |
| SS.3.1.1 | Access shall be allowed to authorized parties (company officials, tax authorities). | shall | A, SS.3.1.1 |
| SS.3.1.2 | Where electronic remote access is legally required, it should be implemented securely; characteristics shall be complied with if legislation specifies them. | should/shall | A, SS.3.1.2 |
| SS.3.2.1 | An appropriate class of signature shall be used (see SS.1.1). | shall | A, SS.3.2.1 |
| SS.3.2.2 | The maintenance of that signature over the storage period (see SS.2.) shall be ensured. | shall | A, SS.3.2.2 |
| SS.3.2.3 | Mechanisms to detect loss or surreptitious addition of data objects shall be used. | shall | A, SS.3.2.3 |
| SS.3.3.1 | The original data object format (or legally valid derived format) shall be ensured as readable. | shall | A, SS.3.3.1 |
| SS.3.3.2 | Where risk of obsolescence, affected data objects shall be reliably copied; an independent trusted assertion should attest correspondence. | shall/should | A, SS.3.3.2 |
| SS.3.4.1 | Media shall be suitable for required period; timely copy if risk of unreadability. For signed objects depending on media integrity, copying shall include appropriate controls. | shall | A, SS.3.4.1 |
| SS.3.5.1 | Data objects shall be produced in a format that prevents undetected changes (e.g., malicious code). Users should be notified of unreliable formats. | shall/should | A, SS.3.5.1 |
| SS.3.5.2 | If XML, either include style sheets in signature calculation or use standard syntax with defined semantics. | shall | A, SS.3.5.2 |
| SS.3.5.3 | Data objects shall be stored in original format if free of malicious code. | shall | A, SS.3.5.3 |
| SS.3.5.4 | Where original format lacks reliability, store in suitable format instead of (or in addition to) original; reliable assertion should be available. | shall (with should) | A, SS.3.5.4 |
| SS.3.6.1 | Storage must be physically or logically separated between owners to maintain confidentiality. | must | A, SS.3.6.1 |
| SS.4.1 | Submission to authorities should use secure channels; if legislation specifies ways, shall comply. | should/shall | A, SS.4.1 |
| SS.4.2 | To prevent unnoticed corruption: [N] AdES shall be used; [N+] QES shall be used. | shall (with choice) | A, SS.4.2 |
| SS.4.3 | Controls from SS.2 shall be provided alongside submitted data object where possible and necessary. | shall | A, SS.4.3 |
| SS.5.1 | Correspondence between analog originals and digital images should be ensured; process in line with best practice. | should | A, SS.5.1 |
| SS.5.2 | Where necessary, digital version should be associated with an assertion on correspondence; signed to protect authenticity/integrity. | should | A, SS.5.2 |

## Annex B (normative): Objectives and controls - information security management

Requirements additional to ISO/IEC 27001 [5], annex A:

| ID | Requirement | Type | Reference |
|---|---|---|---|
| A.5.1.SS1 | A reliable Security Policy should be in force and enforced by the TSP. | should | B, A.5.1.SS1 |
| A.6.2.SS1 | Suitable stipulations shall be in force with outsourcing organizations specifying duties and responsibilities. | shall | B, A.6.2.SS1 |
| A.7.2.SS1 | All private signing keys shall be treated as sensitive and protected by special measures (see SS.1.3). | shall | B, A.7.2.SS1 |
| A.7.2.SS2 | Data objects should be treated as company confidential unless indicated otherwise. | should | B, A.7.2.SS2 |
| A.8.1.SS1 | Personnel in trusted roles should be informed in writing of duties and accept them in writing. | should | B, A.8.1.SS1 |
| A.8.2.SS1 | TSP personnel in trusted roles shall be suitably equipped and educated on tasks and consequences of misbehavior. | shall | B, A.8.2.SS1 |
| A.8.3.SS1 | Personnel shall be informed of confidentiality duties after termination. | shall | B, A.8.3.SS1 |
| A.8.3.SS2 | For leaving personnel, company equipment shall be returned and privileges withdrawn unless otherwise specified. | shall | B, A.8.3.SS2 |
| A.9.1.SS1 | Systems for issuing/storing data objects shall be located in secured areas; access limited to authorized officers (preferably dual control) and logged. | shall | B, A.9.1.SS1 |
| A.9.2.SS1 | Suitable measures shall be established to protect equipment and ensure service continuity. | shall | B, A.9.2.SS1 |
| A.10.1.SS1 | Clear and detailed procedures shall be defined for trusted roles with assigned responsibilities and segregation of duties. | shall | B, A.10.1.SS1 |
| A.10.1.SS2 | Trusted roles include Security Officers, System Administrators, System Operators, System Auditors. | (informative) | B, A.10.1.SS2 |
| A.10.2.SS1 | Outsourcing party shall verify third-party compliance with obligations (preliminary assessment, monitoring, auditing). | shall | B, A.10.2.SS1 |
| A.10.3.SS1 | TSPs should plan processing capacity to meet peak periods and commitments. | should | B, A.10.3.SS1 |
| A.10.5.SS1 | Should arrange backup storage and recovery plan. | should | B, A.10.5.SS1 |
| A.10.6.SS1 | Networks shall be protected to prevent unauthorized insertion/deletion or disclosure. | shall | B, A.10.6.SS1 |
| A.10.7.SS1 | Media protection shall be enforced during entire handling process. | shall | B, A.10.7.SS1 |
| A.10.8.SS1 | Data should be securely exchanged between systems and parties. | should | B, A.10.8.SS1 |
| A.11.2.SS1 | Rigid measures shall be implemented for user authorization management (registration to deregistration and authentication). | shall | B, A.11.2.SS1 |
| A.11.3.SS1 | Users shall be made aware in writing of responsibilities and need to prevent unauthorized access. | shall | B, A.11.3.SS1 |
| A.11.4.SS1 | Organizations with online connections shall have processes to manage and monitor access authorizations to networked services. | shall | B, A.11.4.SS1 |
| A.11.5.SS1 | Logs shall be suitably protected and inspected. | shall | B, A.11.5.SS1 |
| A.11.5.SS2 | Access control to operating systems should be carefully implemented. | should | B, A.11.5.SS2 |
| A.11.6.SS1 | ISO/IEC 27001 controls A.11.6.1 for storage and A.11.6.2 for signing keys should be applied (or equivalent). | should | B, A.11.6.SS1 |
| A.12.2.SS1 | Strict controls shall be implemented for signing and storing procedures, including bulk signing. | shall | B, A.12.2.SS1 |
| A.12.3.SS1 | Where sensitive data protection requires encryption, key management shall be enforced. | shall | B, A.12.3.SS1 |
| A.12.5.SS1 | Applications shall be developed, tested, installed under clear quality assurance procedures. | shall | B, A.12.5.SS1 |
| A.14.1.SS1 | Requirements for TSP service continuity shall be specified in a Service Level Agreement. | shall | B, A.14.1.SS1 |
| A.15.1.SS1 | Where cross-border validity is sought, abide by all involved countries' legislation/regulations. | shall | B, A.15.1.SS1 |
| A.15.2.SS1 | Security Policy compliance shall be met. | shall | B, A.15.2.SS1 |
| A.15.3.SS1 | An appropriate auditing process shall be in place. | shall | B, A.15.3.SS1 |

## Informative Annexes (Condensed)
- **Annex C (Change history)**: Summarizes changes from v1.1.1 to v2.1.1: typographical corrections; term "document/information" changed to "data object"; scope broadened to all data objects (not only fiscally relevant); added PDF Signatures and Associated Signature Container references; restructured introduction and fiscally relevant clauses; added references to TS 101 533-1 [i.3] and TR 101 533-2 [i.4].