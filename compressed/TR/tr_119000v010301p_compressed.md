# ETSI TR 119 000: The framework for standardization of digital signatures and trust services; Overview
**Source**: ETSI | **Version**: V1.3.1 | **Date**: 2023-05 | **Type**: Informative (Technical Report)
**Original**: [ETSI TR 119 000 V1.3.1](https://www.etsi.org/deliver/etsi_tr/119000_119099/119000/01.03.01_60/tr_119000v010301p.pdf)

## Scope (Summary)
This document describes the general structure for ETSI/CEN digital signature and trust services standardization, identifying six functional areas of standardization and a list of existing and potential future standards in each area. It provides an overview of the framework, including a classification scheme, numbering scheme, and business guidance entry points.

## Normative References
None (normative references are not applicable in this TR).

## Definitions and Abbreviations
- **Terms**: For the purposes of the present document, the terms given in ETSI TR 119 001 [i.5] apply.
- **Abbreviations**: For the purposes of the present document, the abbreviations given in ETSI TR 119 001 [i.5] apply.

## Framework Overview

### 4.1 Classification Scheme
The framework is organized around **6 functional areas** and **6 document types**.

#### 4.1.1 Functional Areas
1. **Signature creation & validation** – standards for creation and validation of digital signatures, including policy, signature formats (CAdES, XAdES, PAdES, JAdES, CB-AdES), signature containers (ASiC), signature policies, and protection profiles.
2. **Signature creation and other related devices** – standards for secure/qualified signature creation devices (SSCD/QSCD), devices for TSPs, TSAs, signing servers, authentication devices.
3. **Cryptographic suites** – standards for cryptographic algorithms and suites used in digital signatures and time-stamps.
4. **Trust service providers (TSPs) supporting digital signatures and related services** – TSPs issuing certificates, time-stamping, signature generation/validation, remote signing, identity proofing.
5. **Trust application service providers** – value-added services using digital signatures: registered electronic delivery, registered electronic mail, long-term preservation.
6. **Trust service status (list) providers** – standards for trust service status lists and trusted lists (e.g., eIDAS trusted lists).

An additional **area 0** groups introductory documents (e.g., this TR) and studies.

#### 4.1.2 Document Types
1. **Guidance** – business-driven guidance (non-normative).
2. **Policy & security requirements** – normative requirements for services and systems, including protection profiles.
3. **Technical specifications** – technical requirements (formats, protocols, algorithms, profiles).
4. **Conformity assessment** – requirements for assessing conformity to specifications.
5. **Testing conformance & interoperability** – test suites and specifications for interoperability testing.
6. **Sector specific requirements** – profiles for particular business sectors (e.g., banking).

#### 4.1.3 Structure with Sub-areas
Each functional area is divided into sub-areas addressing specific types of products, services, or technologies (e.g., within area 1: CAdES, XAdES, PAdES, JAdES, ASiC, mobile environments).

#### 4.1.4 Numbering Scheme
Format: `DD L19 xxx-z`
- `DD` = deliverable type (SR, TS, TR, EN)
- `L` = organization: 4 for CEN, 0-3 for ETSI
- `019` = SR, `119` = TS/TR, `219` = ES/EG, `319` = EN, `419` = CEN TR/TS/EN
- `19` = series for digital signatures and trust services
- `xxx` = serial number: first digit = area (0-6), second = sub-area, third = document type (0-5)
- `-z` = part number

#### 4.1.5 Guidance Documents and Business Scoping
Stakeholders should first describe their business domain, process, and perform risk assessment. Guidance documents then drive selection of standards and options per area:

- **Area 1**: ETSI TR 119 100 [i.31] – Guidance on signature creation and validation.
- **Area 2**: TR 419 200 [i.83] – Guidance on signature creation devices.
- **Area 3**: ETSI TR 119 300 [i.32] – Guidance on cryptographic suites.
- **Area 4**: ETSI TR 119 400 [i.33] – Guidance on TSPs supporting digital signatures.
- **Area 5**: ETSI TR 119 500 [i.34] – Guidance on trust application service providers.
- **Area 6**: ETSI TR 119 600 [i.35] – Guidance on trust service status list providers.

### 4.2 The Framework by Area (Summarized)

#### 4.2.1 Introductory Documents (Area 0)
| Document | Description |
|----------|-------------|
| ETSI TR 119 000 | This document (overview of framework). |
| ETSI SR 019 020 | Standards for AdES in mobile environments. |
| TR 419 030 | Best practices for SMEs. |
| TR 419 040 | Guidelines for citizens. |
| ETSI SR 019 050 | Rationalized framework for electronic registered delivery. |
| ETSI TR 119 001 | Definitions and abbreviations used across the framework. |

#### 4.2.2 Signature Creation & Validation (Area 1)
**Guidance**: ETSI TR 119 100 [i.31] – business-driven guidance.

**Policy & Security Requirements**: ETSI TS 119 101 [i.117] – requirements for signature creation and validation applications.

**Technical Specifications**:
- **Procedures**: EN 319 102-1 (creation & validation) [i.40], TS 119 102-2 (validation report) [i.41].
- **CAdES**: EN 319 122-1 (baseline) [i.42], EN 319 122-2 (extended) [i.43], TS 119 122-3 (ERS incorporation) [i.113].
- **XAdES**: EN 319 132-1 (baseline) [i.47], EN 319 132-2 (extended) [i.48], TS 119 132-3 (ERS) [i.50].
- **PAdES**: EN 319 142-1 (baseline) [i.45], EN 319 142-2 (additional profiles) [i.46], TS 119 142-3 (Document Time-stamp) [i.49].
- **CB-AdES**: TS 119 152 [i.114] – CBOR baseline (under development).
- **ASiC**: EN 319 162-1 (baseline) [i.51], EN 319 162-2 (additional) [i.52].
- **Signature Policies**: TS 119 172-1 (human-readable), -2 (XML), -3 (ASN.1), -4 (validation policy for eIDAS) [i.53]-[i.56].
- **JAdES**: TS 119 182-1 (baseline) [i.57].
- **AdES URI**: TS 119 192 [i.58].

**Testing Conformance & Interoperability**: Multi-part TR/TS for CAdES (124 series), XAdES (134), PAdES (144), ASiC (164) – each with overview TR and TS for interoperability and conformance.

#### 4.2.3 Signature Creation and Other Related Devices (Area 2)
**Guidance**: TR 419 200 [i.83]; TR 419 210 [i.84] (applicability to eIDAS).

**Policy & Security Requirements** (Protection Profiles):
- EN 419 211 [i.85] – SSCD protection profiles (parts 1-6).
- TS/EN 419 221 [i.86] – TSP cryptographic module protection profiles (parts 1-6).
- EN 419 231 [i.87] – Time-stamping system protection profile.
- EN 419 241 [i.88] – Server signing security requirements (parts 1-2).
- EN 419 251 [i.89] – Authentication device protection profiles.
- TS 419 261 [i.90] – Security requirements for systems managing certificates.

**Technical Specifications**: EN 419 212 [i.91] – Application interface for secure elements (IAS) (parts 1-5).

**Conformity Assessment**: Via Common Criteria (ISO/IEC 15408) [i.30].

#### 4.2.4 Cryptographic Suites (Area 3)
**Guidance**: ETSI TR 119 300 [i.32].

**Technical Specifications**:
- TS 119 312 [i.135] – cryptographic suites (recommended algorithms, based on SOG-IS).
- TS 119 322 [i.136] – machine-readable schema for algorithm catalogues.

#### 4.2.5 TSPs Supporting Digital Signatures and Related Services (Area 4)
**Guidance**: ETSI TR 119 400 [i.33].

**Policy & Security Requirements**:
- EN 319 401 [i.73] – general policy requirements for TSPs.
- EN 319 411-1 (general) [i.68], -2 (EU qualified) [i.69]; TR 119 411-4 (checklist) [i.124], -5 (web browser/EU trust coexistence) [i.125].
- EN 319 421 [i.126] – time-stamping TSP policy.
- TS 119 431-1 [i.115] – remote QSCD/SCDev; -2 [i.116] – AdES signature creation support.
- TS 119 441 [i.118] – signature validation service policy.
- TS 119 461 [i.120] – identity proofing requirements.

**Technical Specifications**:
- EN 319 412 (parts 1-5) – certificate profiles [i.63]-[i.67].
- EN 319 422 [i.121] – time-stamping protocol and token profile.
- TS 119 432 [i.122] – remote signature creation protocols.
- TS 119 442 [i.123] – signature validation service protocols.

**Conformity Assessment**:
- EN 319 403-1 [i.59] – general CAB requirements.
- TS 119 403-2 [i.60] – additional for publicly-trusted certificates.
- TS 119 403-3 [i.61] – additional for EU qualified TSPs.

**Sector Specific**:
- TS 119 495 [i.62] – certificate profiles and TSP policy for Open Banking (PSD2).

#### 4.2.6 Trust Application Service Providers (Area 5)
**Guidance**: ETSI TR 119 500 [i.34]; SR 019 510 [i.70] (preservation scoping); TR 119 530 [i.71] (REM interoperability feasibility).

**Policy & Security Requirements**:
- TS 119 511 [i.72] – long-term preservation (digital signatures and general data).
- EN 319 521 [i.74] – electronic registered delivery service providers (ERDSP).
- EN 319 531 [i.75] – registered electronic mail service providers (REMSP).

**Technical Specifications**:
- TS 119 512 [i.76] – protocols for long-term preservation.
- EN 319 522 (parts 1-4) [i.127]-[i.130] – electronic registered delivery services (framework, semantics, formats, bindings).
- EN 319 532 (parts 1-4) [i.131]-[i.134] – registered electronic mail services (framework, semantics, formats, interoperability profiles).

**Testing Conformance & Interoperability**:
- TS 119 524 (parts 1-2) [i.77][i.78] – ERDS testing.
- TS 119 534 (parts 1-2) [i.79][i.80] – REM testing.

#### 4.2.7 Trust Service Status Lists Providers (Area 6)
**Guidance**: ETSI TR 119 600 [i.35].

**Technical Specifications**:
- TS 119 612 [i.44] – trusted lists (referenced by EU secondary legislation).

**Testing Conformance & Interoperability**:
- TS 119 614-1 [i.81] – conformance testing of XML representation of trusted lists.

**Sector Specific**:
- TS 119 615 [i.82] – procedures for using and interpreting EU Member States national trusted lists.

## Key Informative References (Selected)
- [i.1] Regulation (EU) 910/2014 (eIDAS).
- [i.5] ETSI TR 119 001 – definitions and abbreviations.
- [i.31] ETSI TR 119 100 – guidance on signature creation and validation.
- [i.32] ETSI TR 119 300 – guidance on cryptographic suites.
- [i.33] ETSI TR 119 400 – guidance for TSPs.
- [i.34] ETSI TR 119 500 – guidance for trust application service providers.
- [i.35] ETSI TR 119 600 – guidance for trust service status list providers.
- [i.40] ETSI EN 319 102-1 – procedures for creation and validation.
- [i.42] ETSI EN 319 122-1 – CAdES baseline.
- [i.45] ETSI EN 319 142-1 – PAdES baseline.
- [i.47] ETSI EN 319 132-1 – XAdES baseline.
- [i.51] ETSI EN 319 162-1 – ASiC baseline.
- [i.57] ETSI TS 119 182-1 – JAdES.
- [i.68] ETSI EN 319 411-1 – certificate issuance general.
- [i.73] ETSI EN 319 401 – general policy requirements for TSPs.
- [i.117] ETSI TS 119 101 – signature creation/validation applications.
- [i.135] ETSI TS 119 312 – cryptographic suites.
- [i.44] ETSI TS 119 612 – trusted lists.

(Full list of 136 informative references is provided in the original document.)

## History
| Version | Date | Publication |
|---------|------|-------------|
| V1.1.1 | September 2015 | Publication |
| V1.2.1 | April 2016 | Publication |
| V1.3.1 | May 2023 | Publication |