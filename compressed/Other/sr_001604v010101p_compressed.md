# ETSI SR 001 604 V1.1.1: Rationalised Framework for Electronic Signature Standardisation
**Source**: ETSI/CEN | **Version**: V1.1.1 | **Date**: 2012-07 | **Type**: Informative Special Report
**Original**: http://www.etsi.org/deliver/etsi_sr/001600_001699/001604/01.01.01_60/sr_001604v010101p.pdf

## Scope (Summary)
This document establishes a rationalised framework for electronic signature (eSignature) standardisation within the context of Directive 1999/93/EC and its possible revision. It provides an inventory of existing standards, a target rationalised structure, a gap analysis, and a future work plan.

## Normative References
Not applicable.

## Definitions and Abbreviations
### Definitions (from Directive 1999/93/EC)
- **advanced electronic signature**: electronic signature meeting requirements: (a) uniquely linked to signatory; (b) capable of identifying signatory; (c) created using means under signatory's sole control; (d) linked to data so any subsequent change is detectable.
- **certificate**: electronic attestation linking signature verification data to an entity/person and confirming identity.
- **certification service provider (CSP)**: entity/person who issues certificates or provides other services related to electronic signatures.
- **certificate validation**: process of checking that a certificate or certificate path is valid.
- **electronic signature (eSignature)**: data in electronic form attached to or logically associated with other electronic data serving as a method of authentication.
- **qualified certificate**: certificate meeting Annex I of Directive 1999/93/EC provided by a CSP fulfilling Annex II.
- **qualified electronic signature (QES)**: advanced electronic signature based on a qualified certificate and created by a secure signature creation device.
- **secure signature creation device (SSCD)**: device meeting Annex III of Directive 1999/93/EC.
- **signatory**: person who holds a signature creation device.
- **signature creation data**: unique data (e.g., private keys) used by signatory to create an electronic signature.
- **signature creation device**: configured software/hardware used to implement signature-creation data.
- **signature validation**: process of checking signature validity including certificate validation and signature verification.
- **signature verification**: process of checking the cryptographic value of a signature using verification data.
- **signature verification data**: data (e.g., public keys) used to verify an electronic signature.
- **signature verification device**: configured software/hardware used to implement signature-verification data.

### Additional Definitions
- **Data Preservation Service Provider (DPSP)**: Trust Application Service Provider providing secure digital storage for a defined period.
- **registered e-mail**: enhanced e-mail providing evidence of submission and delivery.
- **registered electronic delivery**: enhanced electronic delivery providing evidence of handling.
- **registered electronic delivery service provider**: trust application service provider offering registered electronic delivery services.
- **registered e-mail service provider**: trust application service provider offering registered e-mail services.
- **signature generation service provider (SGSP)**: trust service provider providing remote management of signatory's signature creation device and generation of electronic signatures.
- **signature policy**: set of rules for creation and validation of electronic signatures defining technical and procedural requirements for a particular business need.
- **signature validation service provider (SVSP)**: trust service provider offering signature validation services.
- **time-stamping service provider (TSSP)**: trust service provider issuing time-stamp tokens.
- **time-stamp token**: data object binding a datum to a particular time.
- **trust application service provider (TASP)**: trust service provider operating a value added Trust Service based on electronic signatures.
- **trust service**: electronic service enhancing trust and confidence in electronic transactions.
- **trust service provider (TSP)**: entity providing one or more electronic trust services.
- **trust service status list (TSL)**: list of trust service status information protected for authenticity and integrity.
- **trust service status list provider (TSSLP)**: trust service provider issuing a TSL.
- **trust service token**: physical or binary object generated/issued as a result of a Trust Service.
- **trusted list (TL)**: profile of TSL that is the national supervision/accreditation status list of certification services.

### Abbreviations
AdES, AdES QC, ANSSI, API, ASiC, BES, BSI, CA, CAB Forum, CAdES, CD, CEN, CMS, CRL, CSP, CWA, DIS, DPS, DPSP, DSS, E-CODEX, EESSI, EN, EPES, ETSI, HSM, HTTP, IAS, IDPF, ISO, LoA, LTV, MTM, NFC, OCSP, OASIS, OEBPS, PAdES, PKC, PEPPOL, PP, QC, QES, RED, REM, REM-MD, SCA, SGSP, SOGIS, SR, SSCD, S/MIME, SMTP, SOAP, SPOCS, SSL, SVA, SVSP, TASP, TC, TOE, TEE, TL, TR, TS, TSL, TSP, TSP PKC, TSP QC, TSSLP, TSSP, UPU, USB, WI, XAdES, XSL, XML, XMLDSig

## 4 Inventory
An inventory of existing standardisation and publicly available specifications (standards, regulatory specs, national/sector) has been collected. The detailed data is available as a separate Excel/PDF download from the ETSI/CEN Electronic Signature Standards website.

## 5 Rationalised Structure for Electronic Signature Standardisation Documents

### 5.1 Introduction
#### 5.1.1 Objectives
- Allow business stakeholders to easily implement and use eSignature products/services.
- Facilitate mutual recognition and cross-border interoperability.
- Simplify standards, reduce unnecessary options, avoid diverging interpretations.
- Target clear status of European Norm.
- Facilitate global presentation and access to standards.

#### 5.1.2 Approach
Central focus on creation and validation of eSignatures, relying on third-party services (certificate issuers, time-stamping, etc.). The structure provides guidance from two viewpoints: Signature Creation/Validation (for businesses) and Trust Service Provider (for providers). Simplification, reduction of options, and cross-border interoperability are key.

### 5.2 Electronic Signature Standardisation Classification Scheme
#### 5.2.1 Functional Areas
1. **Signature Creation & Validation**: rules, formats, packaging, protection profiles.
2. **Signature Creation & Other Related Devices**: SSCDs, TSP devices, authentication devices.
3. **Cryptographic Suites**: algorithms, key generation, hash functions.
4. **TSPs Supporting eSignatures**: TSPs issuing certificates (qualified/non-qualified), time-stamping, signature generation, signature validation.
5. **Trust Application Service Providers**: registered e-mail, e-delivery, data preservation.
6. **Trust Service Status Lists Providers**: TSL and Trusted Lists.

#### 5.2.2 Document Types
1. Guidance (non-normative)
2. Policy & Security Requirements (including protection profiles)
3. Technical Specifications (formats, protocols, APIs)
4. Conformity Assessment (rules for assessment)
5. Testing Compliance & Interoperability (test suites, tools)

#### 5.2.3 Rationalised Structure with Sub-Areas
Areas 1,2,4,5 have sub-areas (e.g., CAdES, XAdES, PAdES for area 1; SSCD/other SCDs for area 2; TSP issuing certificates, TSSP, SGSP, SVSP for area 4; REM, DPSP for area 5). Each sub-area has its own set of the five document types.

#### 5.2.4 Numbering Scheme
Format: `DD L19 xxx-z`
- DD: deliverable type (SR, TS, TR, EN)
- L: 0,1,2,3 for ETSI; 4 for CEN
- 19: eSignature series
- xxx: area (0-6), sub-area, document type
- -z: multi-part

#### 5.2.5 Possible Extension to incorporate IAS
May add area for electronic Identification/Authentication, extend existing areas, and add necessary sub-areas. Document type classification remains applicable.

### 5.3 Rationalised Structure by Area
This section defines the planned documents for each area. Below is a consolidated summary.

#### 5.3.1 Generic
- **TR 19 000**: Rationalised structure for Electronic Signature Standardisation (framework document, based on this SR).

#### 5.3.2 Signature Creation & Validation
| Sub-area | Guidance | Policy & Security | Technical Specs | Conformity Assessment | Testing Compliance & Interop |
|----------|----------|------------------|----------------|----------------------|------------------------------|
| Generic | TR 19 100 Business Driven Guidance | EN 19 101 Policy & Security Req; EN 19 111 Protection Profiles | EN 19 102 Procedures; EN 19 172 Signature Policies | EN 19 103 Conformity Assessment | TS 19 104 General |
| CAdES | - | - | EN 19 122 CAdES (multi-part) | - | TS 19 124 CAdES Testing |
| XAdES | - | - | EN 19 132 XAdES | - | TS 19 134 XAdES Testing |
| PAdES | - | - | EN 19 142 PAdES | - | TS 19 144 PAdES Testing |
| Mobile | - | - | EN 19 152 AdES in Mobile | - | TS 19 154 Mobile Testing |
| ASiC | - | - | EN 19 162 ASiC | - | TS 19 164 ASiC Testing |
| Signature Policies | - | - | EN 19 172 (multi-part) | - | TS 19 174 Policies Testing |

#### 5.3.3 Signature Creation & Other Related Devices
| Sub-area | Guidance | Policy & Security | Technical Specs | Conformity Assessment | Testing |
|----------|----------|------------------|----------------|----------------------|---------|
| Generic | TR 19 200 Business Driven Guidance | - | - | - | - |
| SSCD | - | EN 19 211 Protection Profiles (multi-part) | EN 19 212 Application Interfaces | - | - |
| TSP Systems (certificates) | - | EN 19 221 Security Req for Trustworthy Systems | - | - | - |
| TSP Time-stamping | - | EN 19 231 Security Req for TSS | - | - | - |
| TSP Server Signing | - | EN 19 241 Security Req for SGSP | - | - | - |
| Authentication Device | - | EN 19 251 Protection Profiles | - | - | - |
| Generic Conformity | - | - | - | EN 19 203 Conformity Assessment | - |

#### 5.3.4 Cryptographic Suites
| Sub-area | Guidance | Technical Specs |
|----------|----------|----------------|
| Generic | TR 19 300 Business Driven Guidance | TS 19 312 Cryptographic Suites |
| Testing | - | - |

#### 5.3.5 TSPs Supporting Electronic Signatures
| Sub-area | Guidance | Policy & Security | Technical Specs | Conformity Assessment |
|----------|----------|------------------|----------------|----------------------|
| Generic | TR 19 400 Business Driven Guidance | EN 19 401 General Policy Req | - | EN 19 403 General Conformity Assessment Guidance |
| TSP Issuing Certificates | - | EN 19 411 Policy Req (multi-part) | EN 19 412 Profiles | EN 19 413 Conformity Assessment |
| TSP Time-Stamping | - | EN 19 421 Policy Req | EN 19 422 Profiles | EN 19 423 Conformity Assessment |
| TSP Signature Generation | - | EN 19 431 Policy Req | EN 19 432 Profiles | EN 19 433 Conformity Assessment |
| TSP Signature Validation | - | EN 19 441 Policy Req | EN 19 442 Profiles | EN 19 443 Conformity Assessment |

#### 5.3.6 Trust Application Service Providers
| Sub-area | Guidance | Policy & Security | Technical Specs | Conformity Assessment | Testing |
|----------|----------|------------------|----------------|----------------------|---------|
| Generic | TR 19 500 Business Driven Guidance; SR 19 530 Study on e-Delivery | - | - | - | TS 19 504 General Testing Req |
| REM | - | EN 19 511 Policy & Security Req | EN 19 512 REM Services | EN 19 513 Conformity Assessment | TS 19 514 REM Testing |
| Data Preservation | - | EN 19 521 Policy & Security Req | EN 19 522 Data Preservation Services | SR 19 523 Conformity Assessment | - |

#### 5.3.7 Trust Service Status Lists Providers
| Sub-area | Guidance | Policy & Security | Technical Specs | Conformity Assessment | Testing |
|----------|----------|------------------|----------------|----------------------|---------|
| Generic | TR 19 600 Business Driven Guidance | EN 19 601 General Policy Req | EN 19 602 TSL Format | EN 19 603 General Conformity Assessment | TS 19 604 General Testing |
| Trusted Lists | - | EN 19 611 Policy Req | EN 19 612 Trusted List Format | EN 19 613 Conformity Assessment | TS 19 614 Trusted List Testing |

## 6 Gap Analysis & Work Plan

### 6.1 Methodology
A table per document shows degree scope met (1-5) and work plan tasks with timescale T0 = September 2012.

### 6.2 Analysis and Work Plan by Area
Summarised below.

#### 6.2.1 Generic
- **TR 19 000**: Partially met; produce from current document. **Start T0, complete T0+12**.

#### 6.2.2 Signature Creation & Validation
- **TR 19 100**: Inputs exist (TR 102045, CROBIES). New TR. T0+12.
- **EN 19 101**: Inputs exist; new EN. T0+24.
- **EN 19 111**: Nearly met; progression from EN 14170. 2013.
- **EN 19 102**: Partially met; new EN. T0+18.
- **EN 19 122**: Nearly met; progression and updates. T0+24.
- **EN 19 132**: Partially met; significant revision for XML Sig versions. T0+24.
- **EN 19 142**: Nearly met; progression and new e-Invoicing profile. T0+24.
- **EN 19 152**: Inputs exist; new EN. T0+24.
- **EN 19 162**: Partially met; progression. T0+24.
- **EN 19 172**: Inputs exist; new EN. T0+24.
- **EN 19 103**: Little basis; new EN. T0+24.
- **TS 19 104**: Little basis; new TS. T0+24.
- **TS 19 124**: Partially met; from existing. T0+24.
- **TS 19 134**: Partially met; from existing and new. T0+24.
- **TS 19 144**: Little basis; new TS. T0+24.
- **TS 19 154**: Little basis; study. T0+24.
- **TS 19 164**: Partially met; from existing. T0+24.
- **TS 19 174**: Little basis; new TS. T0+24.

#### 6.2.3 Signature Creation Devices
- **TR 19 200**: Little basis; new TR. T0+12.
- **EN 19 211**: Nearly met; progression from EN 14169. 2013.
- **EN 19 221**: Nearly met; progression from TS 14167. T0+2+18.
- **EN 19 231**: Partially met; new PP and EN. T0+24+18.
- **EN 19 241**: Nearly met; progression from TS 14167-5. T0+24+18.
- **EN 19 251**: Nearly met; progression from EN 16248. T0+24+18.
- **EN 19 212**: Inputs exist; significant revision. T0+24+18.
- **EN 19 203**: Partially met; significant revision. T0+12+18.

#### 6.2.4 Cryptographic Suites
- **TR 19 300**: Little basis; new TR. T0+12.
- **TS 19 312**: Partially met; significant revision from TS 102176. T0+12.

#### 6.2.5 TSP Supporting Electronic Signatures
- **TR 19 400**: Little basis; new TR. T0+12.
- **EN 19 401**: Nearly met; progression from quick fix. Q1 2013.
- **EN 19 411**: Partially met; progression and new sub-parts. T0+24.
- **EN 19 421**: Partially met; progression from TS 102023. T0+24.
- **EN 19 431**: Inputs exist; new EN. T0+24.
- **EN 19 441**: Inputs exist; new EN. T0+24.
- **EN 19 412**: Partially met; progression and new parts. T0+24.
- **EN 19 422**: Nearly met; progression from TS 101861. T0+18.
- **EN 19 432**: Inputs exist; new EN. T0+24.
- **EN 19 442**: Inputs exist; new EN. T0+24.
- **EN 19 403**: Nearly met; progression. T0+24.
- **EN 19 413**: Partially met; new EN. T0+24.
- **EN 19 423**: Partially met; new EN. T0+24.
- **EN 19 433**: Little basis; new EN. T0+24.
- **EN 19 443**: Partially met; new EN. T0+24.

#### 6.2.6 Trust Application Service Providers
- **TR 19 500**: Little basis; new TR. T0+12.
- **SR 19 530**: Inputs exist; new SR. T0+12.
- **EN 19 511**: Inputs exist; new EN. T0+24.
- **EN 19 521**: Partially met; new EN. T0+18.
- **EN 19 512**: Scope fully met; progression. T0+12.
- **EN 19 522**: Inputs exist; study first. T0+12.
- **EN 19 513**: Inputs exist; new EN. T0+24.
- **EN 19 523**: Inputs exist; new EN. T0+24.
- **TS 19 504**: Inputs exist; new TS. T0+12.
- **TS 19 514**: Inputs exist; new TS. T0+12.

#### 6.2.7 Trust Service Status List Providers
- **TR 19 600**: Little basis; new TR. T0+12.
- **EN 19 601**: Inputs exist; new EN. T0+24.
- **EN 19 611**: Inputs exist; new EN. T0+24.
- **EN 19 602**: Nearly met; new EN. T0+18.
- **EN 19 612**: Nearly met; new EN. T0+18.
- **EN 19 603**: Inputs exist; new EN. T0+27.
- **EN 19 613**: Inputs exist; new EN. T0+27.
- **TS 19 604**: Inputs exist; new TS. T0+12.
- **TS 19 614**: Nearly met; new TS. T0+6.

### 6.3 General Conclusions
Work plan execution (Phase 2) aims to meet rationalisation objectives: business guidance, mutual recognition, simplification, European Norm status, global presentation. Conformity assessment and testing facilities will be completed within two years after T0. The website www.e-signatures-standards.eu will be updated regularly.

## Informative Annexes (Condensed)
- **Annex A (Discussion on TSP and CSP Concept)**: Clarifies that TSP is broader than CSP (from Directive). CSP covers both TSPs supporting eSignatures and Trust Application Service Providers. TSP also includes services not related to eSignatures.
- **Annex B (Initial Guidance on Matching Output of Business Requirements Analysis to Electronic Signature Standards from Signature Creation/Validation Viewpoint)**: Proposes phased approach: identify eSignature business factors (application-related, legal, actor-related, other parameters) and map them to appropriate standards. Factors include data type, workflow, signature legal level, durability, etc. This annex is basis for future guidance (TR 19 100).
- **Annex C (Migration Strategy)**: Proposes assigning new numbers under the 19xxx scheme; existing documents will be renumbered via empty documents referencing new versions.
- **Annex D (Inventory)**: Contained in separate archive file `sr_001604v010101p0.zip`.