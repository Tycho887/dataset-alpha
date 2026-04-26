# ETSI TR 102 047 V1.2.1: International Harmonization of Electronic Signature Formats
**Source**: ETSI Technical Committee Electronic Signatures and Infrastructures (ESI) | **Version**: V1.2.1 | **Date**: 2005-03 | **Type**: Informative (Technical Report)
**Original**: RTR/ESI-000028, keywords: e-commerce, electronic signature, digital, security

## Scope (Summary)
This Technical Report presents results of ongoing work to harmonize ETSI TS 101 733 (CMS-based electronic signatures) and TS 101 903 (XAdES) with other internationally recognized standards and related activities, aiming to meet Directive 1999/93/EC requirements for advanced electronic signatures while maximizing international interoperability.

## Normative References
- [1] ETSI TS 101 733: "Electronic Signatures and Infrastructures (ESI); Electronic Signature Formats"
- [2] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)"
- [3] IETF RFC 3369: "Cryptographic Message Syntax"
- [4] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999
- [5] W3C Recommendation/IETF RFC 3275: "XML-Signature Syntax and Processing"
- [6] IETF RFC 3126: "Electronic Signature Formats for long term electronic signatures" (equivalent to TS 101 733)
- [7] W3C Note: "XML Advanced Electronic Signatures (XAdES)" (equivalent to TS 101 903)
- [8] oasis-dss-1.0-core-spec-cd-02: "Digital Signature Service Core Protocols, Elements, and Bindings"
- [9] ETSI TR 102 047: "International Harmonization of Electronic Signature Formats" (this document)

## Definitions and Abbreviations
- **Definitions**: For the purposes of the present document, the terms and definitions given in TS 101 733 [1] and TS 101 903 [2] apply.
- **Abbreviations**:
  - **ASN.1**: Abstract Syntax Notation (number) 1
  - **CMS**: Cryptographic Message Syntax
  - **CRL**: Certificate Revocation List
  - **DSS**: Digital Signature Services
  - **DSS-TC**: Digital Signature Services Technical Committee
  - **DTD**: Document Type Definition
  - **EPM**: Electronic Post Mark
  - **IETF**: Internet Engineering Task Force
  - **OASIS**: Organization for the Advancement of Structured Information Standards
  - **OCSP**: Online Certificate Status Provider
  - **TC**: Technical Committee
  - **URI**: Uniform Resource Identifier
  - **W3C**: World Wide Web Consortium
  - **XAdES**: XML Advanced Electronic Signatures
  - **XML**: eXtended Markup Language
  - **XMLDSIG**: XML-Signature Syntax and Processing

## 4 Objective
- **Objective**: The major objective of international harmonization is to maximize interoperability between electronic signatures in line with Directive 1999/93/EC [4] and other electronic signature systems.

## 5 International basis of European electronic signature formats
- **Basis**: ETSI specifications are based on existing internationally recognized standards.

### 5.1 TS 101 733 and IETF RFC 2630
- IETF RFC 3369 [3] defines basic CMS components; TS 101 733 [1] extends it by:
  - Defining ASN.1 types for attributes required for long-term validity, common use cases, and European Directive compliance.
  - Proposing advanced electronic signature forms based on those types.
  - Providing rationale for each new type.
- Additions to CMS: signing time, time-stamps, commitment type, signature place, signature policy identifier, signer role, countersignatures, validation data (certificates, CRLs, OCSP responses).
- A new version of TS 101 733 [1] published December 2003 addressing external comments.

### 5.2 TS 101 903 and W3C XML signatures
- W3C/IETF XMLDSIG [5] provides basic XML signature components; TS 101 903 [2] (XAdES) extends it by:
  - Taxonomy of additional elements for long-term validity, common use cases, and Directive compliance.
  - XML schema definitions for new properties.
  - Two incorporation methods: direct or by reference using XMLDSIG mechanisms.
  - Specific XAdES signature forms combining defined elements.
- XML structures cover similar information to clause 5.1.
- TS 101 903 [2] reviewed after external comments and first XAdES interoperability event; new version published first half of 2004.

## 6 Further harmonization activities

### 6.1 IETF RFC 3126
- ETSI TC ESI submitted TS 101 733 [1] to IETF as informational RFC 3126 [6] (technically identical), increasing international visibility.
- Updated draft to replace RFC 3126 in line with new TS 101 733 produced, but progress halted due to IPR issues after IETF IPR rule changes.

### 6.2 W3C Note and joint working group
- After TS 101 903 [2] issued, W3C Note [7] produced to attract attention; implementations growing.
- Discussions with W3C on updating the Note and other XML signature activities led to proposal for a joint W3C/ETSI group on advanced XML signatures.

### 6.3 OASIS Digital Signature Services (DSS)
- OASIS DSS-TC formed in 2002 to develop techniques for digital signature processing, including web service interfaces for creation, verification, and proof of creation within key validity period.
- **Developments**:
  - Core protocol for creation/verification web services with policy control.
  - XML-based protocol for cryptographic time-stamps.
  - Profiles for specific use cases: time-stamping, asynchronous operation, code signing, entity seal, Electronic Post Mark (EPM), German signature law, policy-wise operation, XAdES [2].
  - Profiles planned: signature gateway, court filing, electronic notaries, web security services.
- OASIS time-stamping profile and XML token format being incorporated into ANSI X9.95.
- **XAdES profile**: covers lifecycle of XAdES signatures including creation, validation (with optional update via unsigned properties), archival form properties, re-validation.
- Overlap with EPM and German signature profiles (use of time-stamping and XAdES forms).
- Committee Drafts agreed; trial implementations planned.
- Two ETSI TC ESI members co-chair the DSS-TC and lead XAdES profiling.

## 7 Recommendations
- **Recommendation 1**: Continue feeding revisions of TS 101 733 [1] and TS 101 903 [2] into IETF and W3C for publication to maintain harmonization. (should)
- **Recommendation 2**: Maintain close links with OASIS DSS TC to ensure their web services work continues to incorporate support for TS 101 903 [2]. (should)
- **Recommendation 3**: Maintain close ties with W3C and, if possible, set up a joint group to continue work on electronic signature formats. (should)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Continue feeding revisions of TS 101 733 [1] and TS 101 903 [2] into IETF and W3C for publication. | should (recommended) | Clause 7 |
| R2 | Maintain close links with OASIS DSS TC to ensure support for TS 101 903 [2]. | should (recommended) | Clause 7 |
| R3 | Maintain close ties with W3C and consider joint group on electronic signature formats. | should (recommended) | Clause 7 |

## Annex A: Further technical details of OASIS DSS (Condensed)
### A.1 OASIS DSS Core Protocol
- Latest version (v30) of Core Protocol [8] approved as Committee Draft after improvements:
  - Capability to include schema of signed documents for ID type attribute identification.
  - Support for `<ds:Manifest>` processing.
  - Clarified semantics of `<dss:ReturnSigningTime>` / `<dss:SigningTime>`.
  - Enhanced `<dss:ClaimedIdentity>` element with supporting information (SAML, X509 certificate).
- Ballot open to progress v30 to Committee Draft.

### A.2 OASIS DSS XAdES-related protocols
- Two new versions of "XAdES Profiles of the OASIS Digital Signature Service" (latest v6) produced since last report.
- Contains:
  - Abstract profile for generation and verification/update protocols of advanced electronic signatures (both CMS [1] and XAdES [2]).
  - Two concrete profiles:
    1. For TS 101 733 [1] generation and verification/update.
    2. For XAdES generation and verification/update.
- Key features:
  - Generation protocols allow client to request signed properties: SigningTime, CommitmentTypeIndication, SignatureProductionPlace, SignerRole, DataObjectFormat, DataObjectTimeStamp (XAdES also IndividualDataObjectTimeStamp).
  - For some properties, client provides values; for others, uses URI identifying signature form.
  - Verification protocols accept XAdES/CMS signatures and allow server to add unsigned properties, returning evolved forms (e.g., XAdES-T to XAdES-C/X).
- Profile and others being voted for Committee Draft status.