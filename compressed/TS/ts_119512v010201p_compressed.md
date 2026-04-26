# ETSI TS 119 512 V1.2.1 (2023-05)
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2023-05 | **Type**: Technical Specification (Normative)
**Original**: https://www.etsi.org/deliver/etsi_ts/119500_119599/119512/

## Scope (Summary)
This document specifies protocols for trust service providers (TSPs) offering long-term preservation of digital signatures and general data using digital signature techniques. It complements ETSI TS 119 511 and defines a preservation protocol with operations (RetrieveInfo, PreservePO, RetrievePO, DeletePO, UpdatePOC, RetrieveTrace, ValidateEvidence, Search), system architecture, storage models (with storage, with temporary storage, without storage), preservation goals (Preservation of General Data PGD, Preservation of Digital Signatures PDS, Augmentation AUG), and profiles. Bindings to SOAP/XML and REST/JSON are provided.

## Normative References
- [1] ETSI EN 319 162-1: "Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC Baseline containers"
- [2] IETF RFC 3986: "Uniform Resource Identifier (URI): Generic Syntax"
- [3] IETF RFC 4998: "Evidence Record Syntax (ERS)"
- [4] IETF RFC 6283: "Extensible Markup Language Evidence Record Syntax (XMLERS)"
- [5] OASIS: "Digital Signature Service Core Protocols, Elements, and Bindings Version 2.0"
- [6] OASIS: "Digital Signature Service Metadata Version 1.0"
- [7] Recommendation ITU-T X.680 (2021): "Information technology - Abstract Syntax Notation One (ASN.1): Specification of basic notation"

## Definitions and Abbreviations
- **preservation service**: service capable of extending the validity status of a digital signature over long periods and/or providing proofs of existence of data over long periods.
- **preservation goal**: one of PGD, PDS, or AUG.
- **preservation storage model**: WithStorage (WST), WithTemporaryStorage (WTS), WithoutStorage (WOS).
- **preservation profile**: uniquely identified set of implementation details (see clause 5.4.7).
- **preservation evidence**: evidence produced by the service to demonstrate preservation goals.
- **preservation object (PO)**: typed data object submitted to or retrieved from the service.
- **preservation object container (POC)**: container holding a set of data objects and metadata.
- **POID**: unique identifier for a set of submitted preservation objects.
- **Evidence Record**: unit of data proving existence at a certain time (RFC 4998/6283).
- **Abbreviations**: PGD, PDS, AUG, WST, WTS, WOS, PO, POC, POID, SubDO, ERS, XAIP, ASiC, TSA, ValS, CSA, JSON, XML, SOAP, REST.

## 4 General Aspects
### 4.1 System Architecture
Preservation service provides a preservation interface (clause 5). It may use an external Time-Stamping Authority (TSA) or signature creation service (SigS) and optionally a Validation Service (ValS) or directly collect certificate status information from a Certificate Status Authority (CSA). Three storage model variants exist (clause 4.3). The notification interface (client callback) is not specified in this document.

### 4.2 Preservation Goals
Three goals defined by URIs:
- `http://uri.etsi.org/19512/goal/pgd` – Preservation of General Data (proof of existence).
- `http://uri.etsi.org/19512/goal/pds` – Preservation of Digital Signatures (extend validity).
- `http://uri.etsi.org/19512/goal/aug` – Augmentation of submitted evidences.

### 4.3 Storage Models
#### 4.3.1 Preservation With Storage (WST)
Service stores SubDOs and produced evidences. Supports export/import. Model value: `WithStorage`.

#### 4.3.2 Preservation With Temporary Storage (WTS)
Service stores SubDOs temporarily only to create evidence; evidences stored for limited retrieval. Client may submit full data or hash values. Model value: `WithTemporaryStorage`.

#### 4.3.3 Preservation Without Storage (WOS)
Service does not store SubDOs; evidences produced synchronously. Client may submit hash values. Model value: `WithoutStorage`.

### 4.4 Preservation Schemes, Profile and Policies
A preservation scheme defines general approach (Annex F). Profiles (machine-readable) implement schemes and contain references to policies (evidence creation, signature validation). Profiles are described by `Profile` elements (clause 5.4.7) and retrieved via `RetrieveInfo`.

## 5 Technical Specification of Protocol
### 5.1 Introduction and Overview
Operations: RetrieveInfo, PreservePO, RetrievePO, DeletePO, UpdatePOC (optional), RetrieveTrace (optional), ValidateEvidence (optional), Search (optional). Specifications use generic semantics then XML and JSON syntax.

### 5.2 Discovery of Supported Preservation Profiles
The preservation service **shall** support the `RetrieveInfo` operation to allow clients to retrieve supported profiles (clause 5.3.2).

### 5.3 Operation Requests and Responses
#### 5.3.1 Basic Types: Request and Response (components from OASIS DSS-X Core 2.0)
- **Request**: optional `OptionalInputs`, optional `RequestID` string. When present, service **shall** return `RequestID` in response.
- **Response**: optional `OptionalOutputs`, mandatory `Result` (with major/minor status codes), optional `RequestID`.

#### 5.3.2 RetrieveInfo
- **RetrieveInfoRequest**: extends Request; optional `Profile` (URI) and optional `Status` (active/inactive). If `Status` omitted, only active profiles returned.
- **RetrieveInfoResponse**: extends Response; zero or more `Profile` elements. Error codes include `noPermission`, `internalError`, `parameterError`, `notSupported`.

#### 5.3.3 PreservePO
- **PreservePORequest**: extends Request; mandatory `Profile` (URI), zero or more `PO` elements (clause 5.4.5).
- **PreservePOResponse**: extends Response; optional `POID` (string) – returned after successful call if service provides storage or supports RetrieveTrace; zero or more `PO` elements. For WOS, evidence returned synchronously in `PO`. Error codes include `noPermission`, `internalError`, `parameterError`, `transferError`, `noSpaceError`, `notSupported`, `unknownPOFormat`, `POFormatError`, `externalServiceUnavailable`, `warning/lowSpace`.

#### 5.3.4 RetrievePO (Conditional)
- **RetrievePORequest**: extends Request; mandatory `POID`; optional `VersionID` (zero or more strings, "all" for all versions); optional `SubjectOfRetrieval` (default `POwithEmbeddedEvidence`); optional `POFormat` and `EvidenceFormat` (URIs). Only for WST or WTS.
- **RetrievePOResponse**: extends Response; zero or more `PO` elements. Error codes include `unknownPOID`, `unknownVersionID`, `unknownPOFormat`, `unknownEvidenceFormat`, `warning/requestOnlyPartlySuccessful`.

#### 5.3.5 DeletePO (Conditional)
- **DeletePORequest**: extends Request; mandatory `POID`; optional `Mode` (DeletionMode: `OnlySubDOs` or `SubDOsAndEvidence`, default `SubDOsAndEvidence`); optional `ClaimedRequestorName` and `Reason`. Only for WST.
- **DeletePOResponse**: extends Response. Error codes include `unknownPOID`, `unknownMode`.

#### 5.3.6 UpdatePOC (Optional)
- **UpdatePOCRequest**: extends Request; mandatory `POID`; mandatory one or more `DeltaPOC` (PO elements). For sophisticated versioning, single DeltaPOC with format supporting versioning (Annex E); otherwise multiple DeltaPOC added simply.
- **UpdatePOCResponse**: extends Response; optional `VersionID` (string, sequential e.g., v1,v2). Error codes include `unknownDeltaPOCType`, `DeltaPOCInternalProblem`.

#### 5.3.7 RetrieveTrace (Optional)
- **RetrieveTraceRequest**: extends Request; mandatory `POID`.
- **RetrieveTraceResponse**: extends Response; mandatory `Trace` element (clause 5.4.10). Error codes include `unknownPOID`.

#### 5.3.8 ValidateEvidence (Optional)
- **ValidateEvidenceRequest**: extends Request; mandatory `Evidence` (clause 5.4.4); optional zero or more `PO`.
- **ValidateEvidenceResponse**: extends Response; optional `ValidationReport` (POType), optional `ProofOfExistence` (dateTime). Error codes include `notSupported`.

#### 5.3.9 Search (Optional)
- **SearchRequest**: extends Request; mandatory `Filter` string (query language defined in Profile).
- **SearchResponse**: extends Response; zero or more `POID` elements. Error codes include `notSupported`.

### 5.4 Components for Operations
#### 5.4.2 DeletionMode
**Values**: `OnlySubDOs`, `SubDOsAndEvidence`. XML/JSON simple type.

#### 5.4.3 Event
**Sub-components**: `Time` (dateTime), `Subject` (string), `Operation` (string); optional `Object`, `Detail`.

#### 5.4.4 Evidence
Extends PO (clause 5.4.5). **Mandatory**: `FormatId` (URI). Additional optional: `POID`, `VersionID`. Value: binaryData or xmlData.

#### 5.4.5 PO (Preservation Object)
**Mandatory**: value (binaryData or xmlData). **Optional**: `FormatId`, `MimeType`, `PronomId`, `ID`, `RelatedObjects`.

#### 5.4.6 PreservationStorageModel
**Values**: `WithStorage`, `WithTemporaryStorage`, `WithoutStorage`.

#### 5.4.7 Profile
**Mandatory sub-components**: `ProfileIdentifier` (URI), `Operation` (one or more, per OASIS DSS Metadata), `Policy` (one or two: `http://uri.etsi.org/19512/policy/preservation-evidence` and optionally `http://uri.etsi.org/19512/policy/signature-validation`), `ProfileValidityPeriod` (ValidFrom, optional ValidUntil), `PreservationStorageModel`, `PreservationGoal` (one or more URIs from clause 4.2), `EvidenceFormat` (one or more FormatType).
**Optional**: `Specification` (URIs), `Description` (InternationalString), `SchemeIdentifier` (URI), `ExpectedEvidenceDuration` (duration), `PreservationEvidenceRetentionPeriod` (duration, required for WTS), `Extension`.

#### 5.4.8 Status
**Values**: `active`, `inactive`.

#### 5.4.9 SubjectOfRetrieval
**Values**: `PO`, `Evidence`, `POwithEmbeddedEvidence`, `POwithDetachedEvidence`.

#### 5.4.10 Trace
Contains zero or more `Event` elements.

### 5.5 Components for ASiC Extensions
#### 5.5.2 Extensions for ASiCManifest
- **ContainerID**: `POID` (mandatory), optional `VersionID`. Should not be critical.
- **PreservationPeriod**: date. Should not be critical.
- **PreservationSubmitter**: string. Should not be critical.
- **IsUpdatedVersionOf**: URI. Should not be critical.
- **CanonicalizationMethod**: per XMLDSIG. **Should be critical** because missing canonicalization invalidates evidences.
- **ValidationReport**: POType. Should not be critical.

#### 5.5.3 Extensions for DataObjectReference
- **IsMetaDataOf**: URI. Should not be critical.

### 5.6 Components for Other Preservation Object Formats
#### 5.6.1 DigestList
Used in WTS for submitting hash values. **Sub-components**: `DigestMethod` (string with OID URI), one or more `DigestValue` (base64), optional `Evidence` (to be augmented).

## 6 Requirements for Preservation Object Data Formats
### 6.1 General Aspects
- An admissible format **shall** be documented in a permanent, publicly available specification for interoperability.
- Format **shall** be identified by a URI (FormatId).
- Only formats defined in Annex B (normative) should be used for interoperability.

### 6.2 Specific Requirements for Preservation Object Containers
A preservation object container **shall** satisfy:
1. Allow storage of one or more data objects.
2. May allow additional attributes (e.g., metadata, transformation indication).
3. **Shall** allow storage of one or more preservation evidence objects protecting a defined set of data objects.
4. May contain an identifier for addressing within the service.
5. May support versioning (Annex E).
6. May support privacy-friendly mode (hash values instead of original data).
7. May support inclusion of validation reports.

## 7 Requirements for Preservation Schemes
A preservation scheme specification **shall**:
1. Be documented in a permanent, publicly available specification.
2. Be identified by a URI.
3. Specify the applicable preservation storage model.
4. Specify the set of supported preservation goals.
5. Specify mandatory and optional operations.
6. Describe the process for generating and validating preservation evidences.
7. Describe how augmentation of evidences occurs.
8. May specify formats of input/output and transformations.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Preservation service shall support RetrieveInfo operation. | shall | 5.2, 5.3.2 |
| R2 | RequestID if present in request shall be returned in response. | shall | 5.3.1.1.1, 5.3.1.2.1 |
| R3 | RetrieveInfo request shall extend Request; optional Profile, Status. | shall | 5.3.2.1.1 |
| R4 | RetrieveInfoResponse shall extend Response. | shall | 5.3.2.2.1 |
| R5 | PreservePO request shall contain Profile (URI) and may contain PO elements. | shall | 5.3.3.1.1 |
| R6 | PreservePOResponse shall return POID if service provides storage or supports RetrieveTrace. | shall | 5.3.3.2.1 |
| R7 | RetrievePO request shall contain POID. | shall | 5.3.4.1.1 |
| R8 | RetrievePOResponse shall extend Response. | shall | 5.3.4.2.1 |
| R9 | DeletePO request shall contain POID. | shall | 5.3.5.1.1 |
| R10 | DeletePOResponse shall extend Response. | shall | 5.3.5.2 |
| R11 | UpdatePOC request shall contain POID and at least one DeltaPOC. | shall | 5.3.6.1.1 |
| R12 | UpdatePOCResponse may contain VersionID. | may | 5.3.6.2.1 |
| R13 | RetrieveTrace request shall contain POID. | shall | 5.3.7.1.1 |
| R14 | RetrieveTraceResponse shall contain Trace element. | shall | 5.3.7.2.1 |
| R15 | ValidateEvidence request shall contain Evidence; may contain PO. | shall | 5.3.8.1.1 |
| R16 | ValidateEvidenceResponse may contain ValidationReport and ProofOfExistence. | may | 5.3.8.2.1 |
| R17 | Search request may contain Filter. | shall | 5.3.9.1.1 |
| R18 | SearchResponse may contain POID elements. | may | 5.3.9.2.1 |
| R19 | DeletionMode values: OnlySubDOs, SubDOsAndEvidence. | shall | 5.4.2.1 |
| R20 | Event component shall contain Time, Subject, Operation. | shall | 5.4.3.1 |
| R21 | Evidence component shall contain FormatId. | shall | 5.4.4.1 |
| R22 | PO component shall contain value (binaryData or xmlData). | shall | 5.4.5.1 |
| R23 | Profile shall contain ProfileIdentifier, Operation, Policy, ProfileValidityPeriod, PreservationStorageModel, PreservationGoal, EvidenceFormat. | shall | 5.4.7.1 |
| R24 | PreservationStorageModel values: WithStorage, WithTemporaryStorage, WithoutStorage. | shall | 5.4.6.1 |
| R25 | Status values: active, inactive. | shall | 5.4.8.1 |
| R26 | SubjectOfRetrieval values: PO, Evidence, POwithEmbeddedEvidence, POwithDetachedEvidence. | shall | 5.4.9.1 |
| R27 | Trace contains zero or more Event. | may | 5.4.10.1 |
| R28 | ASiC extensions: ContainerID, PreservationPeriod, PreservationSubmitter, IsUpdatedVersionOf, CanonicalizationMethod, ValidationReport. Criticality as specified. | shall | 5.5.2 |
| R29 | IsMetaDataOf extension for DataObjectReference. | may | 5.5.3.1 |
| R30 | DigestList component: DigestMethod mandatory, DigestValue one or more, optional Evidence. | shall | 5.6.1.1 |
| R31 | Preservation object data format shall be identified by URI and documented publicly. | shall | 6.1 |
| R32 | Preservation object container shall satisfy seven requirements (list in 6.2). | shall | 6.2 |
| R33 | Preservation scheme specification shall meet eight general requirements (list in 7). | shall | 7 |

## Preservation Schemes (Annex F – Normative)
### F.1 Preservation Scheme with Storage based on Evidence Records
- **Identifier**: `http://uri.etsi.org/19512/scheme/pds+pgd+aug+wst+ers`
- **Goals**: PDS, PGD, AUG.
- **Storage Model**: WithStorage.
- **Mandatory Operations**: PreservePO, RetrievePO, DeletePO.
- **Optional**: UpdatePOC, RetrieveTrace, ValidateEvidence, Search.
- **Evidence Format**: `urn:ietf:rfc:4998` and/or `urn:ietf:rfc:6283`.
- **Evidence Generation**: For SubDOwithDS, signature validation and collection of validation material; then hashed and inserted into Merkle hash-tree with initial archive time-stamp. For SubDOwoDS, direct hashing.
- **Augmentation**: Time-stamp or hash-tree renewals based on cryptographic monitoring (e.g., ETSI TS 119 312).

### F.2 Preservation Scheme with Temporary Storage based on Evidence Records
- **Identifier**: `http://uri.etsi.org/19512/scheme/pgd+wts+ers`
- **Goals**: PGD (mandatory), AUG (optional).
- **Storage Model**: WithTemporaryStorage.
- **Mandatory Operations**: PreservePO (may allow DigestList), RetrievePO (returns evidence record).
- **Optional**: RetrieveTrace, ValidateEvidence.
- **Evidence Format**: same as F.1.
- **Evidence Generation**: DigestList digest values added to hash-tree; evidence retrievable within retention period.
- **Augmentation**: If optional Evidence element in DigestList, service performs renewal.

### F.3 Preservation Scheme with Signature Augmentation and With Storage
- **Identifier**: `http://uri.etsi.org/19512/scheme/pds+wst+aug`
- **Goals**: PDS (mandatory), AUG (optional).
- **Storage Model**: WithStorage.
- **Mandatory Operations**: PreservePO, RetrievePO, DeletePO.
- **Optional**: RetrieveTrace, ValidateEvidence, Search.
- **Evidence Format**: Signature-specific archive time-stamps: CAdES (http://uri.etsi.org/ades/CAdES/archive-time-stamp-v3), XAdES (http://uri.etsi.org/ades/XAdES/ArchiveTimeStamp), PAdES (http://uri.etsi.org/ades/PAdES/document-time-stamp).
- **Evidence Generation**: Service ensures all validation data available, adds to signature, protects with signature-format-specific time-stamp.

### F.4 Preservation Scheme with Signature Augmentation and Without Storage
- **Identifier**: `http://uri.etsi.org/19512/scheme/pds+wos+aug`
- **Goals**: PDS (mandatory), AUG (optional).
- **Storage Model**: WithoutStorage.
- **Mandatory Operations**: PreservePO.
- **Optional**: RetrieveTrace, ValidateEvidence.
- **Evidence Format**: same as F.3.
- **Evidence Generation**: Same as F.3 but synchronous.

## Informative Annexes (Condensed)
- **Annex A (normative)**: Defines preservation object formats: submission (CAdES, XAdES, PAdES, ASiC-E, XAIP, DigestList), evidence (time-stamp token, ERS, archive time-stamps), additional input/output (ASiC-ERS, XAIP). Each format is identified by a URI.
- **Annex E (informative)**: Versioning of a Preservation Object Container. Describes how UpdatePOC creates new logical versions via DeltaPOC, allowing addition, modification, or deletion of objects without altering previous versions. Example with XAIP-based POC.
- **Annex G (informative)**: Data structure for backup or migration of preservation services with storage. Defines `EvidenceExchange` component containing full hash-trees, evidence info, and objects to support seamless migration between services.
- **Annex H (normative)**: Attributes for preservation evidences: `preservation-service-identifier`, `preservation-evidence-policy`, `preservation-profile`. Each shall be a URI, inserted in evidence records (ASN.1 for RFC 4998, XML for RFC 6283).
- **Annex I (normative)**: ASN.1 syntax for the attributes defined in Annex H. Module `ETSI-Preservation-Attributes` with OIDs.
- **Annex J (informative)**: Change history (V1.1.2 corrections, V1.2.1 corrections and clarifications).