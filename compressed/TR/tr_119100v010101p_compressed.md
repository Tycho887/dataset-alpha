# ETSI TR 119 100 V1.1.1 (2016-03): Electronic Signatures and Infrastructures (ESI); Guidance on the use of standards for signature creation and validation
**Source**: ETSI | **Version**: V1.1.1 | **Date**: March 2016 | **Type**: Technical Report (Informative)
**Original**: http://www.etsi.org/standards-search (Reference DTR/ESI-0019100)

## Scope
Provides a business‑driven guided process for implementing generation and validation of digital signatures in electronic business processes. Starting from business/risk analysis, stakeholders are guided to select the appropriate standards and options for digital signature creation and validation. Target audience: enterprise/business process architects, application architects, developers, and signature policy issuers.

## Normative References
Not applicable.

## Informative References (selected)
- [i.1] ETSI TR 119 000: Framework for standardization of signatures: overview
- [i.2] ETSI EN 319 122-1: CAdES digital signatures – Part 1: Building blocks and baseline signatures
- [i.3] ETSI EN 319 122-2: CAdES digital signatures – Part 2: Extended CAdES signatures
- [i.4] ETSI EN 319 132-1: XAdES digital signatures – Part 1: Building blocks and baseline signatures
- [i.5] ETSI EN 319 132-2: XAdES digital signatures – Part 2: Extended XAdES signatures
- [i.6] ETSI EN 319 142-1: PAdES digital signatures – Part 1: Building blocks and baseline signatures
- [i.7] ETSI EN 319 142-2: PAdES digital signatures – Part 2: Additional PAdES signatures profiles
- [i.8] ETSI EN 319 162-1: ASiC – Part 1: Building blocks and baseline containers
- [i.9] ETSI EN 319 162-2: ASiC – Part 2: Additional ASiC containers
- [i.10] ETSI EN 319 102 (all parts): Procedures for Creation and Validation of AdES Digital Signatures
- [i.11] ETSI TS 119 101: Policy and security requirements for applications for signature creation and signature validation
- [i.17] ETSI TS 119 172-1: Signature Policies – Part 1: Building blocks and table of contents for human readable signature policy documents
- [i.26] Regulation (EU) No 910/2014 (eIDAS)
- [i.28] ETSI TR 119 300: Guidance on the use of standards for Cryptographic Suites
- [i.29] ETSI TS 119 312: Cryptographic Suites
- [i.35] IETF RFC 5280: Internet X.509 PKI Certificate and CRL Profile
- [i.36] ETSI TR 119 001: Framework for standardization of signatures; Definitions and abbreviations
- [i.37] W3C Recommendation: XML Signature Syntax and Processing Version 1.1
- [i.52] IETF RFC 3161: Internet X.509 PKI Time-Stamp Protocol (TSP)

## Definitions and Abbreviations
For the purposes of the present document, the terms and definitions given in ETSI TR 119 001 [i.36] and the following apply:
- **advanced electronic signature/seal**: As defined in Regulation (EU) No 910/2014 [i.26]
- **business scoping parameter**: specific parameter scoped in the light of the business process(s) where digital signatures or trust services are to be implemented, which implementers need to take into consideration for appropriately addressing the related business requirements in their implementation
- **CAdES signature**: digital signature that satisfies the requirements specified within ETSI EN 319 122-1 [i.2] or ETSI EN 319 122-2 [i.3]
- **claimed signing time**: time of signing claimed by the signer which on its own does not provide independent evidence of the actual signing time
- **(signature) commitment type**: signer-selected indication of the exact implication of a digital signature
- **data object**: actual binary/octet data being operated on (transformed, digested, or signed) by an application
- **digital signature**: data appended to, or a cryptographic transformation of a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery e.g. by the recipient
- **digital signature value**: result of the cryptographic transformation of a data unit that allows a recipient of the data unit to prove the source and integrity of the data unit and protect against forgery e.g. by the recipient
- **detached (digital) signature**: digital signature that, with respect to the signed data object, is neither enveloping nor enveloped
- **enveloped (digital) signature**: digital signature embedded within the signed data object
- **enveloping (digital) signature**: digital signature embedding the signed data object
- **evidence**: information that can be used to resolve a dispute about various aspects of authenticity of archived data objects
- **evidence record**: unit of data, which can be used to prove the existence of an archived data object or an archived data object group at a certain time
- **legacy ASiC container**: legacy ASiC 102 918 container or legacy ASiC baseline container
- **legacy CAdES signature**: legacy CAdES 101 733 signature or legacy CAdES baseline signature
- **legacy PAdES signature**: legacy PAdES 102 778 signature or legacy PAdES baseline signature
- **legacy XAdES signature**: legacy XAdES 101 903 signature or legacy XAdES baseline signature
- **PAdES signature**: digital signature that satisfies the requirements specified within ETSI EN 319 142-1 [i.6] or ETSI EN 319 142-2 [i.7]
- **PDF serial signature**: specific digital signature where the second (and subsequent) signers of a PDF not only sign the document but also the signature of the previous signer and any modification that can also have taken place (e.g. form fill-in)
- **PDF signature**: DER-encoded binary data object based on PKCS #7 (IETF RFC 2315) or CMS (IETF RFC 5652) or related syntax containing a digital signature and other information necessary to validate the digital signature such as the signer's certificate along with any supplied revocation information placed within a PDF document structure
- **proof of existence**: evidence that proves that an object existed at a specific date/time
- **qualified electronic signature/seal**: As defined in Regulation (EU) No 910/2014 [i.26]
- **qualified electronic signature/seal creation device**: As specified in Regulation (EU) No 910/2014 [i.26]
- **secure cryptographic device**: device which holds the user's private key, protects this key against compromise and performs signing or decryption functions on behalf of the user
- **signature attribute**: signature property
- **signature augmentation**: process of incorporating to a digital signature information aiming to maintain the validity of that signature over the long term
- **signature augmentation policy**: set of rules, applicable to one or more digital signatures, that defines the technical and procedural requirements for their augmentation, in order to meet a particular business need, and under which the digital signature(s) can be determined to be conformant
- **signature creation application**: application within the signature creation system, complementing the signature creation device, that creates a signature data object
- **signature creation device**: configured software or hardware used to implement the signature creation data and to create a digital signature value
- **signature creation policy**: set of rules, applicable to one or more digital signatures, that defines the technical and procedural requirements for their creation
- **signature policy**: signature creation policy, signature augmentation policy, signature validation policy or any combination thereof
- **signature policy authority**: entity responsible for the drafting, registering, maintaining, issuing and updating of a signature policy
- **signature policy document**: document expressing one or more signature policies in a human readable form
- **signature validation**: process of verifying and confirming that a digital signature is valid
- **signature verification**: process of checking the cryptographic value of a signature using signature verification data
- **signer**: entity being the creator of a digital signature
- **time assertion**: time-stamp token or an evidence record
- **time-stamp**: data in electronic form which binds other electronic data to a particular time establishing evidence that these data existed at that time
- **XAdES signature**: digital signature that satisfies the requirements specified within ETSI EN 319 132-1 [i.4] or ETSI EN 319 132-2 [i.5]

**Abbreviations**: ASiC, ASN.1, BPMN, BSP, CA, CMS, CRL, DA, DER, DSS, DTBS, DTBSR, EC, ETSI CTI, IN MI, ISMS, ISO, OCSP, ODF, OID, PKI, POE, QES, S/MIME, SAML, SCA, SCDev, SCS, SHA, SVA, TL, TSA, TSP, UML, URI, VRI, XFA, XML, XMP.

## 4 Introduction to the guided implementation process

### 4.1 How to use the present document
- Part of a series of guidance documents on selection of standards and options for digital signatures/trust services.
- Proposes a business‑driven guided process for implementing generation and validation of digital signatures.
- Addresses digital signature generation, validation, and augmentation; other areas (cryptographic devices, suites, TSPs) are out of scope but references are provided.
- Reading suggestions per profile: 
  - Enterprise/business process architects and managers: read up to clause 7.
  - Application architects, developers, signature policy issuers: read the whole document.

### 4.2 Overview of the guided implementation process
- **Phase 1 (pre‑requisite)**: Business analysis and risk assessment – capture requirements for digital signature implementation.
- **Phase 2**: Elaborate policy and security requirements into control objectives and controls (refer to ETSI TS 119 101 [i.11] and CEN EN 419 111 [i.12]-[i.16]).
- **Phase 3**: Analyse business scoping parameters (BSPs) – inherent to the business process, legal/regulatory framework, actors, and other sources.
- **Phase 4**: Technical decisions – select formats, contents, levels, procedures, and protection profiles. Document decisions via signature policy documents (ETSI TS 119 172-1 [i.17]).
- Catalysing tools (conformance testing, interoperability) are available (clause 9).
- Evaluation processes (clause 10) may be required for compliance.
- The process is iterative.

## 5 Analysing the Business Requirements
- A complete business analysis, including risk assessment, is essential.
- The present document does not provide further recommendations on methods (UML, BPMN may be used) but signals existence of tools.
- Risk assessment should identify risks that digital signatures can mitigate and risks induced by their use.

## 6 Managing the policy and security requirements
- Tasks: identification of requirements from various sources (legal/regulatory, ISMS, signature generation/validation, development), specification of objectives, selection of controls.
- ETSI TS 119 101 [i.11] should be used for this phase.

## 7 Business scoping parameters

### 7.1 Introduction
BSPs are grouped into:
1. Mainly related to the business process (clause 7.2).
2. Mainly influenced by legal/regulatory framework (clause 7.3).
3. Mainly related to actors (clause 7.4).
4. Other (clause 7.5).

### 7.2 BSPs mainly related with the business process
#### 7.2.1 Introduction
Parameters impact selection of standards for generation, formats, contents, placement, longevity, resilience, and validation.

#### 7.2.2 BSP (a): Workflow (sequencing and timing)
- **Multiple signatures**: distinguish parallel, serial, and counter‑signatures.
- **Counter‑signatures**: special serial signatures; consider relative position, meaning of counter‑signature, validation requirements, and whether counter‑signer signs only the previous signature or also the data object(s).
- **Timing and sequencing**: identify constraints on timing/order of signature generation. If proof of generation before a certain time is required, use time assertions (e.g., time‑stamping). Consider level of assurance for timing evidence (BSP (h)).

#### 7.2.3 BSP (b): Data Object(s) to be signed
- Identify nature/format (binary, XML, PDF, etc.) and whether whole or parts signed.
- Decision on signature syntax (CAdES, XAdES, PAdES) depends on business process specifics, not solely on data format.

#### 7.2.4 BSP (c): Relationships of signatures with signed data object(s) and signature(s)
- Number of data objects per signature (one or more).
- Relative position: enveloped, enveloping, detached. Consider native mechanisms of each format.
- For multiple signed data objects, consider use of referencing mechanisms (e.g., signed ds:Manifest in XAdES) for partial failure handling.

#### 7.2.5 BSP (d): Targeted community
- Identify community rules that may influence signature formats and profiles.

#### 7.2.6 BSP (e): Allocation of responsibility of signatures validation and augmentation
- Responsibility can be assigned to relying party, trusted validation services, or counter‑signing parties (mandatory validation before counter‑signing).
- Also identify augmentation requirements as signatures move through the process.

### 7.3 BSPs mainly influenced by legal/regulatory framework

#### 7.3.2 BSP (f): Legal Effect of the signatures
- Specifies required legal effect (e.g., qualified, advanced, etc. under eIDAS [i.26]).
- Impacts assurance level for authentication, certificate/TSP policies, signature creation device class, trust model.

#### 7.3.3 BSP (g): Commitment assumed by signer
- Describe purpose and precise nature of each signature.
- Commitment type can be explicit (via commitment type indication) or implicit from context.
- Explicit commitment types are defined in signature policies or registered.

#### 7.3.4 BSP (h): Level of assurance of timing evidences
- Distinguish claimed signing time vs. trusted time evidence (time‑stamp tokens, evidence records).
- When trusted time evidence is required, consider qualification of time‑stamp tokens and what they timestamp.

#### 7.3.5 BSP (i): Formalities of signing
- Requirements on the "ceremony of signing" (e.g., WYSIWYS, informed consent, clear expression of will).
- Impact on user interface design and selection of protection profiles.

#### 7.3.6 BSP (j): Longevity and resilience to change
- Identify signatures that require re‑validation after a period, and the required time period.
- Longevity impacts use of time‑stamping, validation material inclusion, and periodic re‑time‑stamping.

#### 7.3.7 BSP (k): Archival
- Requirements on archiving signed data objects, signatures, and validation material together or separately.
- Must be considered in early design stages.

### 7.4 BSPs mainly related to the actors

#### 7.4.1 BSP (l): Identity (and roles/attributes) of the signer
- Identify signer types, identification rules, roles/attributes, and proof of authority.
- Role may be more important than identity (e.g., "Sales Director").

#### 7.4.2 BSP (m): Level of assurance required for the authentication of the signer
- Specify quality level of certificate (e.g., qualified, issued by accredited CA, etc.).

#### 7.4.3 BSP (n): Signature creation devices
- Identify requirements on signature creation devices (e.g., sole control, qualified device).

### 7.5 Other BSPs

#### 7.5.2 BSP (o): Other information to be included within the signatures
- Possible attributes: signature production place, claimed signing time, content time‑stamp, indication of signed data object(s) format.

#### 7.5.3 BSP (p): Cryptographic suites
- Specify robustness requirements; refer to ETSI TR 119 300 [i.28] and ETSI TS 119 312 [i.29].

#### 7.5.4 BSP (q): Technological environment
- Consider mobile/distributed environments; may impact signature format and use of specific services/standards.

## 8 Selecting the most appropriate standards, options, and technical mechanisms

### 8.1 Introduction
Three digital signature formats: CAdES, XAdES, PAdES. Plus ASiC container for packaging detached signatures and data objects. Prefixes for XML namespaces are defined in Table 1.

### 8.2 Format of signatures: CAdES, XAdES or PAdES
#### 8.2.1 Introduction
Format choice depends on business process. PAdES signatures can be built on CAdES, CMS, or XAdES. Acronyms for PAdES subtypes are defined.

#### 8.2.2 Format of the document
- XML documents → XAdES natural.
- PDF documents → PAdES-NoXML.
- ASN.1 encoded objects → CAdES.
- Other binary formats: both XAdES and CAdES work. Additional considerations in subsequent clauses may justify an alternative.

#### 8.2.3 Relative placement of signatures and signed data objects
- Enveloped: PAdES-NoXML is by nature enveloped; CAdES can be embedded in ASN.1 structures; XAdES can be embedded in XML documents.
- Enveloping: CAdES (via encapContentInfo); XAdES (via ds:Object).
- Detached: XAdES uses URI references; CAdES requires external specification (e.g., ASiC).
- Simultaneous multiple positions: XAdES supports all three at once.

#### 8.2.4 Number of signatures and signed data objects
- One document – one signature: all formats handle well.
- One document – multiple signatures: PAdES-NoXML only serial (signs previous signatures); CAdES supports parallel and countersignatures; XAdES supports arbitrary combinations via XML Signature mechanisms. ASiC can package parallel XAdES signatures.
- One signature – multiple data objects: XAdES native; CAdES requires additional techniques (MIME, ASiC). PAdES-NoXML only signs PDF container.

### 8.3 A container for packaging together signatures and detached signed data objects
- ASiC containers (EN 319 162-1 [i.8] and EN 319 162-2 [i.9]) hold detached XAdES or CAdES signatures and their data objects.
- ASiC Simple (ASiC-S) for one document signed by several detached signatures.
- ASiC Extended (ASiC-E) for multiple data objects; allows selective signing.
- CAdES signatures in ASiC-E use ASiCManifest file to reference and digest data objects.
- XAdES signatures use native ds:Reference.

### 8.4 Baseline or extended/additional?
- Baseline signatures (CAdES, XAdES, PAdES, ASiC) minimize options for maximal interoperability.
- Extended/additional provide more optionality.
- Implementers should first check if baseline suffices; if not, use extended/additional specifications.

### 8.5 Selecting the proper quality of the signature
- To meet legal requirements (e.g., eIDAS), ensure that signing device, certificate issuance, independent assurance, cryptographic suite, signature application, longevity, desired protection level, and independent assurance on level are all fulfilled.

### 8.6 Mapping formalities of signing to the electronic domain
- Ensure signing environment satisfies the characteristics listed in clause 7.3.5.

### 8.7 Satisfying timing and sequencing requirements
#### 8.7.1 Sequencing
- **Counter‑signatures**: XAdES – embedded via xades:CounterSignature or detached via Type attribute. CAdES – countersignature unsigned attribute signs the signature field. PAdES-NoXML – serial signatures; counter‑signature attribute not allowed. PAdES-XML uses xades:CounterSignature.

#### 8.7.2 Timing
- **Time‑stamping signed data objects before signing**: XAdES – xades:AllDataObjectsTimeStamp or xades:IndividualDataObjectsTimeStamp signed properties. CAdES – content‑time‑stamp signed attribute. PAdES – Document Time‑Stamp dictionary for PDF; PAdES-XML uses XAdES properties.
- **Claimed signing time**: XAdES – xades:SigningTime signed property. CAdES – signing‑time signed attribute. PAdES-OnCAdES – M entry in signature dictionary. PAdES-XML-EMB – xades:SigningTime. PAdES-XML-XFA – CreateDate in XMP.
- **Time‑stamp token on signature value**: See clause 8.11.2 for details.

### 8.8 Including indication of commitments assumed by the signer
- XAdES – xades:CommitmentTypeIndication signed property (URIs).
- CAdES – commitment‑type‑indication signed attribute (OIDs).
- Annex B of ETSI TS 119 172-1 [i.17] provides pre‑defined pairs.
- PAdES-CMS – Reason entry in signature dictionary.
- PAdES-E-BES – Reason or commitment‑type‑indication (exclusive).
- PAdES-OnCAdES – Reason or commitment‑type‑indication (if signature‑policy‑identifier present, use commitment‑type‑indication).
- PAdES-XML-EMB – xades:CommitmentTypeIndication.
- PAdES-XML-XFA – description (Dublin Core) or xades:CommitmentTypeIndication if signature‑policy‑identifier present.

### 8.9 Including and protecting indication of signer's identity, signer's roles and/or attributes
#### 8.9.1 Signer's identity
- All ETSI formats except PAdES-CMS protect signer's certificate or its digest.
- XAdES baseline – xades:SigningCertificateV2 signed property. Extended – also can embed certificate in ds:KeyInfo and sign it.
- CAdES – ESS‑signing‑certificate or ESS‑signing‑certificate‑v2.
- PAdES-CMS – not mandated. PAdES-OnCAdES – mandatory. PAdES-XML – either embed certificate in ds:KeyInfo and cover by signature, or use xades:SigningCertificateV2.

#### 8.9.2 Signer's roles and/or attributes
- XAdES – xades:SignerRoleV2 signed property (claimed, certified, signed assertions).
- CAdES – signer‑attributes‑v2 signed attribute.
- PAdES-CMS – attribute certificates not allowed. PAdES-OnCAdES – use signer‑attribute‑v2. PAdES-XML – xades:SignerRoleV2.

### 8.10 Including additional signed information
#### 8.10.2 Signature policy indication
- XAdES – xades:SignaturePolicyIdentifier signed property. CAdES – signature‑policy‑identifier signed attribute.
- PAdES-OnCAdES – use signature‑policy‑identifier. PAdES-XML – xades:SignaturePolicyIdentifier.

#### 8.10.3 Indication of signed data object format
- XAdES – xades:DataObjectFormat signed property.
- CAdES – content‑hints and mime‑type signed attributes.
- PAdES-NoXML – not allowed. PAdES-XML – can use xades:DataObjectFormat.

#### 8.10.4 Indication of signature production place
- XAdES – xades:SignatureProductionPlaceV2. CAdES – signer‑location signed attribute.
- PAdES-OnCAdES – Location entry in signature dictionary. PAdES-XML – xades:SignatureProductionPlaceV2.

### 8.11 Supporting signatures lifecycle
#### 8.11.1 Introduction
- Augmentation adds unsigned attributes/properties after generation.
- Necessary for long‑term validity where certificates expire/algorithms break.

#### 8.11.2 Including time‑stamp tokens on the digital signature value
- See clause 8.7.2.4 (details on signature time‑stamp containers). To extend longevity, protect the signature time‑stamp with another time‑stamp.

#### 8.11.3 Including references to validation data
##### 8.11.3.1 Rationale
- References to CA certificates, revocation data, attribute certificates, time‑stamp certificates can be stored externally or embedded. References contain digest values for unambiguous identification.

##### 8.11.3.2 References to certificates
- XAdES – xadesv141:CompleteCertificateRefsV2, xadesv141:AttributeCertificateRefsV2.
- CAdES – complete‑certificate‑references, attribute‑certificate‑references.

##### 8.11.3.3 References to certificate status data
- XAdES – xades:CompleteRevocationRefs, xades:AttributeRevocationRefs.
- CAdES – complete‑revocation‑references, attribute‑revocation‑references.
- PAdES does not use such references (self‑contained).

#### 8.11.4 Time‑stamping references to validation data
- Protects against CA key compromise. Two container types:
  1. Time‑stamp on signature value, existing time‑stamp(s), and references (SigAndRefsTimeStamp).
  2. Time‑stamp on references only (RefsOnlyTimeStamp).
- XAdES – xadesv141:SigAndRefsTimeStampV2, xadesv141:RefsOnlyTimeStampV2.
- CAdES – CAdES‑C‑time‑stamp, time‑stamped‑certs‑crls‑references.
- Guidance: use SigAndRefsTimeStamp when OCSP responses used; RefsOnlyTimeStamp for CRLs.

#### 8.11.5 Enlarging longevity and resilience to change
##### 8.11.5.1 Introduction
- Steps: incorporate missing validation material, then generate a new time‑stamp token (archive time‑stamp) using a (possibly stronger) algorithm to protect all material.
- Result is signatures with long‑term availability and integrity of validation data (e.g., *‑B‑LTA, *‑E‑A).

##### 8.11.5.2 Incorporating containers for validation material
- CAdES – embed certificates and CRLs in SignedData.certificates and SignedData.crls fields. Legacy containers (certificate‑values, revocation‑values, long‑term‑validation) may be present.
- XAdES – xades:CertificateValues, xades:RevocationValues, xades:AttrAuthoritiesCertValues, xades:AttributeRevocationValues; xadesv141:TimeStampValidationData for time‑stamp certificates.
- PAdES – DSS dictionary (single container for all signatures), optional VRI dictionary per signature.

##### 8.11.5.3 Archive time‑stamp tokens
- CAdES – archive‑time‑stamp‑v3 unsigned attribute. Legacy containers: timeStamp field in long‑term‑validation, older OIDs.
- XAdES – xadesv141:ArchiveTimeStamp unsigned property. Legacy: xades:ArchiveTimeStamp.
- PAdES – Document Time‑Stamp dictionary (time‑stamps entire document including signatures).
- For CAdES, ats‑hash‑index‑v3 attribute identifies which components are covered by the archive time‑stamp, solving ASN.1 SET ordering issues.

#### 8.11.6 Digital signatures lifecycle
##### 8.11.6.1 Generation, validation and augmentation
- Illustrates lifecycles of XAdES signatures through figures (2‑8) showing signer, verifier, arbitrator augmenting signatures with time‑stamps, references, validation material, and archive time‑stamps.
- Key concepts: POE (Proof of Existence), Past Certificate Validation.

##### 8.11.6.2 Lifecycle and levels of digital signatures
- Baseline levels: *‑B‑B (basic), *‑B‑T (with time), *‑B‑LT (long‑term validation material), *‑B‑LTA (long‑term availability/integrity).
- Extended levels: *‑E‑BES, *‑E‑EPES, *‑E‑T, *‑E‑C, *‑E‑X, *‑E‑X‑Long, *‑E‑X‑L, *‑E‑A.
- PAdES additional levels: PAdES-E-BES, PAdES-E-PES, PAdES-E-LTV.
- Diagrams (Figures 9‑12) show examples of each level.

##### 8.11.6.3‑8.11.6.4 Transitions between levels
- Baseline: sequential from B‑B to B‑LTA.
- Extended: multiple paths (Figures 13‑14) showing possible augmentations from E‑EPES/BES to E‑A via intermediate levels. Augmentation steps are defined by mandatory/optional inclusion of specific attributes/properties.

##### 8.11.7 ASiC containers lifecycle
- ASiC-S containers: level determined by embedded signature level.
- ASiC-E containers with CAdES signatures: augmentations require addition of ASiCArchiveManifest file and a time‑stamp token file (IETF RFC 3161 [i.52]) instead of archive‑time‑stamp‑v3 in CAdES.
- Figures 15‑21 illustrate transitions for ASiC-S and ASiC-E containers.

### 8.12 Selecting proper Signature Creation Devices
- Out of scope; refer to CEN TR 419 200 [i.27] (area 2 of Rationalized Framework).

### 8.13 Selecting proper cryptographic suites
- Out of scope; refer to ETSI TR 119 300 [i.28] and ETSI TS 119 312 [i.29].

### 8.14 Signature generation, augmentation and validation applications
#### 8.14.1 Introduction
- Key documents: CEN EN 419 111 [i.12] (Protection Profiles), ETSI EN 319 102-1 [i.10] (Procedures), ETSI TS 119 101 [i.11] (Security Requirements).

#### 8.14.2 Selecting the suitable Protection Profile
- SCA implementers read CEN EN 419 111-2 [i.13] (core PP) and CEN EN 419 111-3 [i.14] (extensions).
- SVA implementers read CEN EN 419 111-4 [i.15] (core PP) and CEN EN 419 111-5 [i.16] (extensions).

#### 8.14.3 Implementing the signature generation and augmentation processes
- ETSI EN 319 102-1 [i.10] specifies generation/augmentation procedures in a format‑agnostic way.
- ETSI TS 119 101 [i.11] provides security requirements for SCA.

#### 8.14.4 Implementing the signature validation process
- ETSI EN 319 102-1 [i.10] defines validation algorithm including handling of expired certificates, broken algorithms, and POE.
- Algorithm outputs TOTAL‑PASSED, TOTAL‑FAILED, or INDETERMINATE.
- Validation uses constraints from policies, configuration, or DA.
- Procedure includes Basic Validation, Time‑stamp Validation, and Long‑term Validation (using POE extraction, Past Certificate Validation, etc.).

## 9 Signature creation and validation catalysing toolkit
### 9.2 Technical Specifications
- 4 parts per format: overview, interoperability test suites (positive, negative, cross‑validation), conformance test assertions.
- Documents: ETSI TS 119 124 [i.22] (CAdES), TS 119 134 [i.23] (XAdES), TS 119 144 [i.24] (PAdES), TS 119 164 [i.25] (ASiC).
- CEN EN 419 103 [i.21] specifies general requirements for testing.

### 9.3 Conformance testing software tools
- Freely available at ETSI Signature Conformance checkers webpage.
- Perform all test assertions; provide trace information for time‑stamp imprint computations.

### 9.4 Interoperability test events
- ETSI CTI Portal for Digital Signatures supports remote interoperability events.
- Contains test suites, signature repositories, automatic interoperability matrices, conformance tools.
- Benefits: ascertain conformance, interoperability, identify specification errors/ambiguities.

## 10 Evaluation processes
- Implementers should be prepared for evaluation of their applications against:
  - Selected signature formats/levels.
  - Procedures (EN 319 102 [i.10]).
  - Protection Profiles (CEN EN 419 111 [i.12]).
  - Policy requirements (TS 119 101 [i.11]).
- Refer to CEN EN 419 103 [i.21] for evaluation process details.

## 11 Corollary: the process within the context of the Standardization Framework
- Figure 22 maps each phase of the process to existing area 1 documents (e.g., TR 119 100 for guidance, TS 119 101 for requirements, EN 319 102 for procedures, EN 319 1x2 for formats, TS 119 172 for signature policies).

## Annex A: Securing signed detached objects in XAdES signatures in the long term
### A.1 Introduction
- XAdES signs detached objects via ds:Reference in ds:SignedInfo or via signed ds:Manifest.
- Both can be secured long‑term.

### A.2 Securing detached objects signed with ds:SignedInfo
- When archive time‑stamp is added, the message imprint computation includes the processing of each ds:Reference (retrieval and transforms). If the digest algorithm becomes weak, a new archive time‑stamp with a stronger algorithm will detect substitution.

### A.3 Detached objects signed with signed ds:Manifest
#### A.3.1 The initial situation
- For objects signed via ds:Manifest, the message imprint of archive time‑stamp includes the canonicalized Manifest element (which contains digests), not the actual objects. This makes it vulnerable to substitution if the digest algorithm is broken (as shown in Figure A.2).

#### A.3.2 The problem
- If a weak digest algorithm (Dig1) is used, an attacker can replace a detached object with a fake object having the same Dig1 hash, and the archive time‑stamp will still verify.

#### A.3.3 The solution: xadesv141:RenewedDigests element
- Before the algorithm breaks, incorporate xadesv141:RenewedDigests unsigned property with renewed digest values (computed with a stronger algorithm Dig2) for each detached object signed via Manifest.
- Then add a new archive time‑stamp. Its message imprint includes the RenewedDigests property.
- Future validation compares the fresh digest (using Dig2) of the retrieved object against the stored renewed digest; mismatch indicates substitution.

## Annex B: Bibliography
- Lists CROBIES WP 5-1 and Directive 2006/123/EC for additional context.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementers **should** perform a business analysis and risk assessment before implementing digital signatures. | should | Clause 5 |
| R2 | Implementers **should** use ETSI TS 119 101 [i.11] for managing policy and security requirements. | should | Clause 6 |
| R3 | Implementers **should** identify and document business scoping parameters (BSPs) from the business process, legal/regulatory framework, actors, and other sources. | should | Clause 7 |
| R4 | When selecting signature format, implementers **should** consider the business process specifics (format of data objects, placement, cardinality, etc.). | should | Clause 8.2 |
| R5 | For detached signatures, implementers **should** consider using ASiC containers (ETSI EN 319 162-1 [i.8] and [i.9]) to package signatures and data objects. | should | Clause 8.3 |
| R6 | Implementers **should** first check if baseline signatures/containers suffice; if yes, use them; otherwise use extended/additional specifications. | should | Clause 8.4 |
| R7 | For legal quality (e.g., qualified electronic signatures), implementers **shall** ensure signing device, certificate, assurance, cryptographic suite, application, longevity, and protection level meet legal requirements. | shall | Clause 8.5 (implicit from requirement to meet eIDAS) |
| R8 | Commitment type **shall** be indicated using the format‑specific signed attribute/property. | shall | Clause 8.8 |
| R9 | Signer's certificate (or its digest) **shall** be protected by the signature (except PAdES-CMS). | shall | Clause 8.9.1 |
| R10 | For long‑term signatures, implementers **should** incorporate signature time‑stamp, references to validation data, validation material, and archive time‑stamps as per the lifecycle transitions. | should | Clause 8.11 |
| R11 | When augmenting ASiC-E containers with CAdES signatures to long‑term level, implementers **shall** use ASiCArchiveManifest and IETF RFC 3161 time‑stamp token files instead of archive‑time‑stamp‑v3. | shall | Clause 8.11.7 |
| R12 | To secure detached objects signed via ds:Manifest against digest algorithm break, implementers **should** use xadesv141:RenewedDigests. | should | Annex A.3.3 |
| R13 | Implementers **should** use conformance testing tools and participate in interoperability events to validate their implementations. | should | Clause 9 |