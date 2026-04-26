# ETSI TR 119 400 V1.1.1 (2016-03): Guidance on the use of standards for trust service providers supporting digital signatures and related services
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2016-03 | **Type**: Informative (Technical Report)
**Original**: http://www.etsi.org/standards-search

## Scope (Summary)
This document provides guidance on selecting standards and options for trust service providers (TSPs) supporting digital signatures and related services (area 4 of ETSI TR 119 000). It describes business scoping parameters and how to identify relevant standards for a given business context.

## Normative References
- Not applicable.

## Informative References
- [i.1] Regulation (EU) No 910/2014 (eIDAS)
- [i.2] ETSI TR 119 000: "Framework for standardization of signatures: overview"
- [i.3] ETSI TR 119 100: "Guidance on signature creation and validation"
- [i.4] ETSI EN 319 401: "General policy requirements for trust service providers"
- [i.5] ETSI EN 319 411-1: "Policy and security requirements for TSPs issuing certificates; Part 1: General"
- [i.6] ETSI EN 319 411-2: "Policy and security requirements for TSPs issuing EU qualified certificates"
- [i.7] ETSI EN 319 421: "Policy and Security Requirements for TSPs issuing Time-Stamps"
- [i.8] ETSI EN 319 412-1: "Certificate Profiles; Part 1: Overview and common data structures"
- [i.9] ETSI EN 319 412-2: "Certificate Profile for certificates issued to natural persons"
- [i.10] ETSI EN 319 412-3: "Certificate Profile for certificates issued to legal persons"
- [i.11] ETSI EN 319 412-4: "Certificate Profile for web site certificates"
- [i.12] ETSI EN 319 412-5: "QCStatements"
- [i.13] ETSI EN 319 422: "Time-stamping protocol and time-stamp token profiles"
- [i.14] ETSI EN 319 403: "Trust Service Provider Conformity Assessment"
- [i.15] ETSI EN 319 122 (all parts): "CAdES digital signatures"
- [i.16] ETSI EN 319 132 (all parts): "XAdES digital signatures"
- [i.17] ETSI EN 319 142 (all parts): "PAdES digital signatures"
- [i.18] ETSI EN 319 162 (all parts): "Associated Signature Containers (ASiC)"
- [i.19] ISO 15408: "Common Criteria"
- [i.20] ITU-T X.509 / ISO/IEC 9594-8
- [i.21] IETF RFC 3161: "Time-Stamp Protocol"
- [i.22] IETF RFC 5246: "TLS v1.2"
- [i.23] ETSI SR 019 020: "Standards for AdES digital signatures in mobile and distributed environments"
- [i.24] ETSI TR 119 500: "Guidance on trust application service providers"
- [i.25] ETSI TR 119 001: "Definitions and abbreviations"
- [i.26] CA/Browser Forum: "Extended Validation Certificates Guidelines"
- [i.27] CA/Browser Forum: "Baseline Requirements for Publicly-Trusted Certificates"
- [i.28] ISO/IEC 27002: "Code of practice for information security management"
- [i.29] IETF RFC 5816: "ESSCertIDv2 Update for RFC 3161"

## Definitions and Abbreviations
### Definitions
For the purposes of the present document, terms and definitions in ETSI TR 119 001 [i.25] apply, plus:
- **EU qualified trust service provider**: TSP that meets requirements for qualified TSPs laid down in Regulation (EU) No 910/2014 [i.1].

### Abbreviations
- **CA**: Certification Authority
- **TLS**: Transport Layer Security (as per IETF RFC 5246)
- **SSL**: Secure Socket Layer (note: newer version is TLS)

## 4 Introduction to trust services and trust service providers
### 4.1 What is a trust service and trust service provider
A trust service enhances trust and confidence in electronic transactions. A TSP (third party) provides information (e.g., a key) in the form of a trust service token, plus associated management services. The concept generalises the earlier concept of a certification authority. Regulation (EU) No 910/2014 [i.1] defines a special class of "qualified trust service provider". Standards identified in this document aim at EU qualified TSPs but are compatible with international requirements (e.g., CA/Browser Forum).

### 4.2 Types of trust service provider
#### 4.2.1 TSP issuing certificates
A certification authority (CA) issues public key certificates binding a public key with identity. Different classes provide alternative legal compliance and identity types. EU qualified certificates are defined for electronic signatures, seals, and web site authentication. Standards address certificates for:
- Digital signatures (used with CAdES, XAdES, PAdES, ASiC)
- Web site authentication (TLS/SSL, meeting CA/Browser Forum requirements)

#### 4.2.2 TSP issuing time-stamps
Time-stamping services prove existence of data at a particular time, used to enhance security of digital signatures and protect document authenticity/integrity.

#### 4.2.3 Other potential trust services
- Signature generation services (for remote users)
- Signature validation services
(NOTE: These are currently not addressed in this document.)

#### 4.2.4 Other trust services outside scope
Limited to trust services supporting digital signatures and web site authentication. Some standards (e.g., EN 319 401, EN 319 403) can be applied to other services, e.g., e-delivery (see TR 119 500).

## 5 Aspects of trust services requiring standardization
### 5.1 Policy & security requirements
TSP trustworthiness requires meeting recognized best practices; for EU qualified TSPs, additionally meeting legislation. Standards describe requirements on TSP policies and practices, including standard trust service policy identifiers. Security of system components is assured via evaluation criteria (e.g., ISO 15408).

### 5.2 Certificate and time-stamp profiles
Trust service tokens (certificates, time-stamps) need to include required information and be encoded understandably. Base standards (X.509, RFC 3161/RFC 5816) have options; profiles specify choices for particular usages (e.g., EU qualified certificates for natural persons).

### 5.3 Conformity assessment
Independent conformity assessment bodies (CABs) audit TSPs against standard criteria. Standards outline CAB capabilities and assessment methods. Conformity assessment is required for formal recognition by legal entities (e.g., supervisory bodies under eIDAS), commercial organizations, or associations (e.g., CA/Browser Forum).

### 5.4 Testing technical conformance and interoperability
Interoperability/conformance testing of trust service tokens is part of wider digital signature interoperability tests (see TR 119 100).

## 6 Selection process
### 6.1 Basis for selection of standards
Process from TR 119 000 clause 4.2.6 applied to TSP area:
1. Identify basic characteristics of trust service:
   - TSP support for digital signatures (requires certificates, may require time-stamps)
   - TSP support for web site authentication (requires certificates)
   - TSP support for archival through time-stamping (requires time-stamps)
2. For digital signatures, derive customer requirements (e.g., legal effect, timing, longevity) from TR 119 100.
3. Based on legal effect, determine if TSP must be EU Qualified.
4. If certificates required, establish if natural or legal person.

### 6.2 Business scoping parameters for TSP standards
Key parameters:
a) Legal effect: EU Qualified or general recognized security level
b) Trust service required: issuing certificate or time-stamp
c) If issuing certificate: identity type (natural person or legal person/organization)
d) If issuing certificate: purpose (digital signature or web site authentication)

## 7 Selecting the most appropriate standards
Standards selected based on business scoping parameters:
a) **Policy requirements document**:
   - TSP issuing certificates, general legal effect: EN 319 411-1 [i.5] (references EN 319 401, CA/Browser Forum guidelines)
   - TSP issuing certificates, EU Qualified: EN 319 411-2 [i.6] (references EN 319 411-1)
   - TSP issuing time-stamps (any legal effect): EN 319 421 [i.7]
b) **Certificate or time-stamp profile**:
   - Certificates for digital signatures, natural persons: EN 319 412-2 [i.9]
   - Certificates for digital signatures, legal persons: EN 319 412-3 [i.10]
   - Certificates for web sites: EN 319 412-4 [i.11]
   - If EU Qualified: EN 319 412-5 [i.12] (QCStatements)
   - Time-stamps: EN 319 422 [i.13]
c) **Conformity assessment**: audit by a CAB complying with EN 319 403 [i.14].

### Table 1: Selection of standards
| Standard | Topic | Issuing certificate (General) | Issuing certificate (EU Qualified) | Issuing time-stamp (General) | Issuing time-stamp (EU Qualified) |
|---|---|---|---|---|---|
| | | Nat DigSig | Nat Web | Leg DigSig | Leg Web | Nat DigSig | Nat Web | Leg DigSig | Leg Web | | |
| EN 319 401 [i.4] | General policy requirements for TSPs | X | X | X | X | X | X | X | X | X | X |
| EN 319 411-1 [i.5] | General policy and security for TSP issuing certs | X | X | X | X | | | | | | |
| EN 319 411-2 [i.6] | Policy and security for EU qualified certs | | | | | X | X | X | X | | |
| EN 319 421 [i.7] | Policy and security for TSPs issuing time-stamps | | | | | | | | | X | X |
| EN 319 412-2 [i.9] | Cert profile – natural persons | X | | | | X | | | | | |
| EN 319 412-3 [i.10] | Cert profile – legal persons | | | X | | | | X | | | |
| EN 319 412-4 [i.11] | Cert profile – web site | | X | | X | | X | | X | | |
| EN 319 412-5 [i.12] | QCStatements | | | | | X | X | X | X | | |
| EN 319 422 [i.13] | Time-stamping protocol and token profiles | | | | | | | | | X | X |
| EN 319 403 [i.14] | TSP Conformity Assessment | X | X | X | X | X | X | X | X | X | X |

(Note: X indicates applicable. See original document for full notes.)

### Figure 1: Relationships between standards
(Figure omitted in text compression; refer to original document for visual representation.)

## Annex A: Clarification of requirements in TSP Standards
**ETSI EN 319 401 [i.4], clause 7.13 b)**: Requires TSP services be accessible to persons with disabilities. In line with eIDAS Article 15, this clause shall be applied "where feasible".

## Requirements Summary
This document is informative (guidance) and contains no normative requirements. The table above summarizes the selection of standards for each scenario.

## Informative Annexes (Condensed)
- **Annex A**: Clarifies that EN 319 401 clause 7.13 b) (accessibility for persons with disabilities) is to be applied "where feasible" in accordance with eIDAS Article 15.