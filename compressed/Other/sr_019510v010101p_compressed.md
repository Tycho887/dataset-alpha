# ETSI SR 019 510: Electronic Signatures and Infrastructures (ESI); Scoping study and framework for standardization of long-term data preservation services, including preservation of/with digital signatures
**Source**: ETSI | **Version**: V1.1.1 (2017-05) | **Date**: May 2017 | **Type**: Special Report (Informative)
**Original**: Provided as text (ETSI SR 019 510)

## Scope (Summary)
Provides a scoping study for long-term data preservation services, covering two main cases: (1) preservation of the validity status of digital signatures (and associated signed data) using time-stamps, evidence records, etc.; and (2) preservation of the integrity of bits of digital objects (signed or not) using digital signature techniques. Also includes an inventory of existing standards and a proposal for a framework of standards.

## Normative References
None. (Clause 2.1 states: "Normative references are not applicable in the present document.")

## Definitions and Abbreviations
### Definitions (Clause 3.1)
- **blob**: data object, manifested physically as a bytestream.
- **container**: data object containing a sequence of data objects and related metadata and an optional manifest.
- **data object**: actual binary/octet data being operated on (transformed, digested, or signed) by an application.
- **(data) preservation service**: service to which data objects are submitted to achieve specified preservation goals over the long-term which at least include proof of integrity and proof of existence and which can maintain the validity status of digital signatures.
- **evidence record**: unit of data, which can be used to prove the existence of a data object or data object group at a certain time (see IETF RFC 4998, IETF RFC 6283, ETSI TS 119 122-3).
- **long-term**: over technological changes such as crypto algorithms, key sizes or hash functions or of storage technology (does not include a change of the document formats).
- **manifest**: additional data object in a preservation object container (POC) referring to the PDOs or additional information and metadata in the POC.
- **media type**: method to label arbitrary content, carried by MIME or other protocols (see IETF RFC 6838).
- **metadata**: data about other data (see ISO 14721:2012 for examples).
- **preservation data object**: original data object to be preserved or metadata provided by the submitter or added by the preservation service.
- **preservation data unit**: preservation data object (or a part of it) which is subject to at least one preservation goal.
- **preservation evidence**: data that can be used to demonstrate that the various preservation goals (e.g. proof of integrity or proof of existence) are met for the preserved data objects.
- **preservation goal**: one of the following objectives achieved during the preservation time frame: proof of integrity, proof of existence, availability, maintenance of validity status of a digital signature or time assertion, confidentiality, authenticity of the submitter, identification of the DPSP.
- **preservation mechanism**: mechanism used to preserve data objects (the present document concentrates on those based on digital signature techniques).
- **preservation object container**: container object or a logical association comprising one or more preservation data objects.
- **preservation policy**: set of rules, applicable to the PDOs that defines at least the preservation mechanisms applied and the internal processes applied to achieve the preservation goals.
- **preservation scheme**: defined (set of) preservation mechanism(s) selected to implement an identified (set of) preservation goal(s) for a given PDO type.
- **preservation time frame**: if not indefinite, duration during which the preservation is to be applied.
- **proof of existence**: evidence that proves that an object existed at a specific date/time.
- **proof of integrity**: evidence that proves the accuracy and completeness of an object.
- **provider**: provider of data preservation service.
- **submitter**: subject that sends the POC to the preservation service.

### Abbreviations (Clause 3.2)
- **DPSP**: Data Preservation Service Provider
- **DMS**: Documentation Management System
- **ER**: Evidence Record
- **ERS**: Evidence Record Syntax (according to IETF RFC 4998 or IETF RFC 6283)
- **ERMS**: Electronic Records Management System
- **LTPP**: Long-Term Preservation Policy
- **PDO**: Preservation Data Object
- **PDU**: Preservation Data Unit
- **POC**: Preservation Object Container
- **POCID**: Unique Identifier of a submitted POC
- **RMS**: Record Management System
- **TST**: Time-Stamp Token
- **TSU**: Time-Stamp Unit

## Basic Models for Long-Term Data Preservation Services (Clause 4)

### 4.1 General Terms
- The document targets preservation of data objects submitted to a preservation service.
- Long-term preservation spans technological changes (crypto algorithms, storage technologies) but not document format changes.
- Minimum preservation goals: integrity and proof of existence; optionally availability.
- Two main cases of digital objects to be preserved: digital signatures (for maintaining validity status) and generic digital objects.
- Additional goals: identification of DPSP, non-repudiation of submission, data confidentiality.
- Preservation data object (PDO) can include main data or metadata added by service. Multiple PDOs can be combined in a Preservation Object Container (POC).
- Preservation data unit (PDU) is a PDO (or part) subject to at least one preservation goal.
- Submitter sends POC; POCID is returned when service is with storage.
- Preservation evidence is data proving preservation goals.
- Preservation scheme is set of mechanisms selected; executed according to a preservation policy.

### 4.2 Preservation with Storage
- Operations identified: **DEPOSIT** (submit POC, return POCID and optionally preservation evidence), **RETRIEVE** (retrieve POC and/or evidence), **RETRIEVE PROOF** (obtain evidence only), **RETRIEVE TRACE OF OPERATIONS** (optional), **UPDATE STORED ELEMENTS** (optional, creates new version), **DELETE** (authorized deletion), **MONITOR** (internal, triggers augmentation), **AUGMENTATION** (internal, extends validity).
- Storage may require encryption, integrity protection, and redundancy.

### 4.3 Preservation without Storage
- Client stores POC; service augments and returns updated POC via **AUGMENTATION** method.
- Client responsible for storage and knowing when to resubmit.
- **MONITOR** (internal) also applies.

### 4.4 Validation
- Validation of digital signatures or time assertions may be internal or external.
- Validation processes defined in other standards (e.g., ETSI EN 319 102-1 for AdES, evidence records).
- Validation useful for: (1) validating preservation evidences, (2) collecting elements needed to preserve validity status of signature.
- Validation based on a signature validation policy (e.g., ETSI TS 119 172-4 for qualified signatures).

### 4.5 Elements to be Considered in Preservation Monitoring
#### 4.5.1 Monitoring Strength of Hash Functions and Cryptographic Algorithms
- Preservation service must monitor hash and cryptographic algorithms used by itself or by signatures/time-assertions in preserved objects.
- Depends on AdES level (Basic Signature, Signature with Time, Signatures providing Long-Term Availability and Integrity of Validation Material).
- For evidence records, monitor the TST of the last ArchiveTimeStamp and the hash algorithm in the last hash tree.
- Two hash functions may be used in a TST (one for external data, one for digital signature). Different renewal strategies needed if one becomes weak.
- Monitoring should be continuous and part of security management.

#### 4.5.2 Monitoring Revocation Status of Certificates
- All necessary revocation information must be collected as long as possible and preserved (e.g., covered by a TST).
- Availability limited: CA may not provide revocation info after certificate expiry; qualified TSPs must provide after expiry (per Regulation (EU) No 910/2014).
- Reason code in revocation (e.g., keyCompromise, cACompromise) should be present. If missing, assume worst.
- Key compromise possible only if key still exists; best practice to destroy key after usage period.
- TST valid as long as private key not compromised; protected by applying new TST before cannot be validated.
- Need to demonstrate that certificates in certification path were not revoked for keyCompromise/cACompromise at time of new TST.

### 4.6 Consideration of Different Policies
#### 4.6.1 Signature Creation Policy
- States rules applied to create signature; can indicate trust anchor.

#### 4.6.2 Signature Augmentation Policy
- States rules applied to augment signature (e.g., which TSUs used). Useful for validation.

#### 4.6.3 Signature Validation Policy
- States rules applied to validate signature; ensures same result in later validations.

### 4.7 Basic Preservation Techniques
#### 4.7.1 Time-Stamps
- Protects all data input to message imprint; proves existence before time indicated, as long as algorithms suitable and certificate trustworthy/not revoked.

#### 4.7.2 AdES Digital Signatures
- Internal mechanisms for long-term verifiability. Four signature phases lifecycle (see ETSI EN 319 102-1):
  - **Basic Signature**: valid until signing certificate expired/revoked.
  - **Signature with Time**: includes proof of existence (usually TST).
  - **Signatures with Long-Term Validation Material**: includes certificates and revocation info.
  - **Signatures providing Long-Term Availability and Integrity of Validation Material**: re-computes hash with specific algorithm and protects with new TST.
- Each AdES format (CAdES, XAdES, PAdES) provides baseline levels (B-LTA) and extended levels (E-A, E-LTV). ASiC containers also support ERS.

#### 4.7.3 ERS (Evidence Record Syntax)
- Uses Merkle tree to protect multiple documents/groups with a single TST.
- Two renewal methods: **Timestamp Renewal** (when hash algorithm still strong but signature algorithm weak) and **Hash-Tree Renewal** (when hash algorithm becomes weak).
- Supports reduced hash tree for individual extraction.

#### 4.7.4 Other Techniques
- List not exhaustive. Academic proposals (e.g., blockchain) exist, but not covered.

#### 4.7.5 Advantages and Disadvantages
- Time-stamp: easy but no long-term strategy alone.
- AdES self-contained, interoperable, but needs one TST per signature.
- ASiC containers combine different PDOs, but require unzipping and manifest checks.
- ERS reduces number of TSTs via hash trees, but extracted evidence loses batch advantage.

### 4.8 (Long-term) Preservation Policy (LTPP)
- Provided by preservation service. Must be available over long-term in stable, integrity-protected format.
- Main purposes: disclose accepted input formats, conditions triggering addition of evidence, conditions allowing validation.
- Should have unique identifier (e.g., OID) and be retrievable.
- Data that may be part of LTPP description:
  1. Identification (e.g., OID).
  2. Location (e.g., URL).
  3. Scheme on which based.
  4. Defining organization.
  5. Activation date.
  6. For with storage: monitoring aspects (hash collision strength, crypto algorithm strength); actions triggered.
  7. For with storage: data collected at receipt.
  8. For with storage: events triggering actions.
  9. Format of preservation evidence returned.
  10. For without storage: data collected during augmentation.
  11. Validation policy for evidence.
  12. Events that may trigger policy update.

## Examples of Different Preservation Schemes (Clause 5)

### 5.1 Long-term Preservation of POC via Evidence Records without storage
- Input POC. If not covered by ER: validate signatures, collect missing validation data, create ER. If already covered: augment ER (Timestamp Renewal or Hash-Tree Renewal). Return POC with (augmented) ER.

### 5.2 Long-term Preservation of POC via Evidence Records with storage
- Input POC (e.g., ASiC). Store internally; compute evidences for one or more POCs at predefined intervals. Internal monitoring triggers augmentation. Original signature file never changed.

### 5.3 Long-term Preservation of AdES Digital Signatures using augmentation of the signature without storage
- Input signature (and detached signed document or its hash). Steps:
  1. If basic signature, add signature time-stamp.
  2. Validate signature to retrieve missing validation material.
  3. Add missing validation material, compute hash of original document and signature, create TST, add to signature.
  4. Return augmented signature.

### 5.4 Long-term Preservation of AdES Digital Signatures using augmentation of the signature with storage
#### 5.4.1 General approach
- As 5.3 steps 1-3, then store. Internal monitor triggers re-augmentation before: (a) TST signing certificate expiry (shell model), (b) crypto/hash algorithm becomes weak. On request, return augmented signature (and optionally original).

#### 5.4.2 Special case using time-stamps with a long lifespan
- Uses HSM with properties: TSU key cannot be backed up/exported/imported, private key auto-zeroized after validity period. Allows less frequent augmentation. Validation material collected but not added until needed.

### 5.5 Long-term AdES preservation with storage based on a validation report
- Service requests signed validation report from trusted service. Instead of augmenting original signature, augments signature of validation report. Stores document and report. Original signature never changed.

### 5.6 Qualified electronic signature/seal relying on long-term availability of validation data
- For advanced signatures based on qualified certificates, successively time-stamp covering original signed data and previous TSTs when algorithms become weak. Assumes validation data for qualified CAs available until end of preservation timeframe.

## Proposal of Framework of Standards for Data Preservation (Clause 6)

### 6.1 General
- Two categories: with storage and without storage. May apply to preservation of qualified signatures/seals, digital signatures, or data.
- First priority: Technical Specifications, later possible transposition into ENs.

### 6.2 Policy & Security Requirements for Trust Service Providers providing long-term data preservation services
- Document will identify common and specific requirements for each service category.
- Distinguish families:
  1. Policy for preservation service preserving validity of digital signatures.
  2. Policy for qualified preservation service for qualified electronic signatures/seals (Regulation (EU) No 910/2014).
  3. Policy for preservation service preserving data objects using signature techniques.
- Covers services with/without storage. Does not cover user signing with own key (assumes already signed or TSP signs).
- Builds on ETSI EN 319 401. Does not cover data object format (except signature techniques).

### 6.3 Protocols for Trust Service Providers providing long-term data preservation services
- Aim: interoperability.
- First goal: identify operations between client and server (with/without storage). Case with storage maps to OAIS (see Annex A).
- Second goal: operations when transferring evidences between services.
- Third goal: define protocols generically.
- Final goal: define data objects and transport protocols (XML/SOAP or JSON/REST).
- Possible data objects: electronic signatures (CAdES, XAdES, PAdES), ASiC containers, ERS, CRLs/OCSP responses, certification paths, time-stamp tokens.

### 6.4 Protection Profiles for Devices supporting data preservation service
- Protection Profiles (PPs) may be considered for trustworthy systems (e.g., for time-stamping, evidence records, monitoring). Usage can facilitate proof of requirement fulfillment.
- May be multipart, falls under CEN TC 224/WG 17.

### 6.5 Relation to Other Standards
- ETSI TS 101 533-1 [i.2] (based on ETSI TS 102 573 [i.6]) is outdated (based on Directive 1999/93/EC, does not consider EN 319 401, only signatures, includes signature process). Should be replaced by new documents.
- ETSI TR 101 533-2 [i.3] covers assessment; general assessment covered by ETSI EN 319 403 [i.22].

### 6.6 Updates of Current Standards
- Current signature format documents (EN 319 122-1, EN 319 132-1, EN 319 142-1) do not allow specifying augmentation policy used during archival format update. Might be useful to add.
- For ERS, similar information could be useful.

## Requirements Summary
This document is a Special Report; it does not define normative requirements. It provides study and framework proposal. Therefore, no requirements table is applicable.

## Informative Annexes (Condensed)

- **Annex A: Relationships between ETSI preservation services and OAIS archives**: Maps ETSI preservation operations (DEPOSIT, RETRIEVE, AUGMENT, etc.) to OAIS Functional Model (Ingest, Archival Storage, Data Management, Access, Preservation Planning, Administration). Also maps ETSI Preservation Information Package (POC) to OAIS Information Package (AIP) through an AIP-Adapter, using tables for elements like Content Information, Preservation Description Information, Packaging Information, etc.

- **Annex B: Catalogue of existing standards**: Lists international/European standards (ISO, IETF, ETSI) and EU national standards (France AFNOR NF Z 42-020, Germany BSI TR-03125) relevant to preservation. Provides brief summaries of each, including ISO 14533-1, ISO 14641-1, ISO/IEC 27040, ISO 14721 (OAIS), ISO 15489, ISO 19005 (PDF/A), IETF RFC 4810 (archive requirements), IETF RFC 4998/6283 (ERS), ETSI EN 319 122-1/2 (CAdES), EN 319 132-1/2 (XAdES), EN 319 142-1/2 (PAdES), EN 319 162-1/2 (ASiC), TS 101 533-1/2, TR 101 533-2, TS 102 573. National standards: French AFNOR NF Z 42-020 (Digital Vault Component functions) and German BSI TR-03125 (TR-ESOR) with its architecture and interface specifications.

- **Annex C: Introduction to the Evidence Record Syntax (ERS)**: Describes ASN.1 ERS (RFC 4998) and XML ERS (RFC 6283). Explains ArchiveTimeStamp structure, hash tree construction, reduced hash tree for proof. Covers augmentation via Timestamp Renewal and Hash-Tree Renewal, including inclusion of validation data.

- **Annex D: Bibliography**: Lists additional references (ETSI TR 119 000, ISO 30300, BSI TR-03112, DIN standards, METS, VERS) not used in main document but relevant.