# ETSI TS 102 918 V1.3.1: Electronic Signatures and Infrastructures (ESI); Associated Signature Containers (ASiC)
**Source**: ETSI Technical Committee ESI | **Version**: V1.3.1 | **Date**: June 2013 | **Type**: Normative
**Original**: ETSI TS 102 918 V1.3.1 (2013-06) – full document available at http://www.etsi.org

## Scope (Summary)
This Technical Specification defines container structures (based on ZIP) to bind one or more signed objects (documents, XML, multimedia, etc.) with detached advanced electronic signatures (CAdES, XAdES) or time‑stamp tokens (RFC 3161) into a single digital container. It specifies two container types: Simple (ASiC‑S) for a single data object, and Extended (ASiC‑E) for multiple objects with flexible signing. The specification addresses interoperability with existing ZIP‑based formats (OCF, ODF, UCF) and mandates no external data references. Protection of archived documents and long‑term verification are out of scope.

## Normative References
- [1] ETSI TS 101 733: CAdES
- [2] ETSI TS 101 903: XAdES
- [3] IETF RFC 3161: Time‑Stamp Protocol (TSP)
- [4] Void
- [5] ISO 32000‑1:2008: PDF 1.7
- [6] Void
- [7] IDPF: EPUB Open Container Format (OCF)
- [8] PKWARE .ZIP Application Note
- [9] OASIS: Open Document Format for Office Applications (OpenDocument) v1.2 Part 3: Packages
- [10] W3C: XML Signature Syntax and Processing
- [11] IETF RFC 4288: Media Type Specifications and Registration Procedures
- [12] IETF RFC 3986: URI: Generic Syntax
- [13] ETSI TS 101 861: Time stamping profile

## Informative References
- [i.1] Adobe Universal Container Format (UCF)
- [i.2] ISO 15489‑1: Records management
- [i.3] Directive 1999/93/EC on electronic signatures
- [i.4] OASIS Guidelines for Conformance Clauses
- [i.5] Void

## Definitions and Abbreviations
### Definitions
- **conformance clause**: statement providing a high‑level description of what is required for conformance
- **container**: file holding data objects with manifest, metadata, and associated signatures under a specified hierarchy
- **data object**: digital information to which AdES and/or time‑stamping apply
- **metadata**: data describing context, content, structure, and management of data objects over time
- **ZIP**: data object conformant to [8]

### Abbreviations
- **AdES**: Advanced Electronic Signature
- **ASiC**: Associated Signature Container
- **OCF**: OEBPS Container Format (see [7])
- **ODF**: Open Document Format (see [9])
- **OEBPS**: Open eBook Publication Structure
- **UCF**: Universal Container Format (see [i.1])

## 4 Introduction to Associated Signature Containers (Informative)
### 4.1 Requirements addressed
Detached signatures need to be associated with signed data to prevent separation; the same applies to time‑stamp tokens. ASiC provides a standardized container to bind data objects with AdES or time‑stamps, enabling interchange and interoperability.

### 4.2 Main features
- **Basic structure**: ZIP‑based with a root folder and a `META-INF` folder for metadata and signatures. Signatures are detached so integrity is preserved when data objects are extracted.
- **Container types**:
  - **ASiC‑S (Simple)**: single data object + one signature structure (CAdES, XAdES, or TST). Supports parallel signatures.
  - **ASiC‑E (Extended)**: multiple data objects, each can be signed by one or more signature structures. Compatible with OCF, UDF, ODF.
- Parallel signatures and subsequent addition (without invalidation) are supported.
- Based on CAdES [1], XAdES [2], and time‑stamp tokens conformant to [13].
- Does not address long‑term verification archive time‑stamp attributes.

### 4.3 Compliance with external specifications
ASiC‑E can be used with OCF, UCF, ODF metadata elements (e.g., `mimetype`, `container.xml`, `manifest.xml`, `metadata.xml`, `*signatures*.xml`). See informative Annex C for cross‑reference.

## 5 Associated Signature Simple form (ASiC‑S)
### 5.1 General Requirements
- **Shall** use ZIP format [8] per structure in 5.2.2.
- Implementations **may** support only one signature/time‑stamp type (CAdES, XAdES, or RFC 3161).

### 5.2 Detailed format for ASiC‑S
#### 5.2.1 Media type identification
1. File extension: **`.asics`** (or **`.scs`** on 3‑char‑limit systems; **`.zip`** for manual handling).
2. Mime type: **`application/vnd.etsi.asic‑s+zip`** (or original mimetype of signed data object).
3. Archive comment field: if present, **shall** be `"mimetype="` followed by the mime type defined above (same as in item 1 of 5.2.2 if present).

#### 5.2.2 Contents of the container
1. Optional **`mimetype`** (per Annex A.1). If file extension does not imply ASiC, **shall** be present and first option in 5.2.1 item 2 **shall** apply.
2. **Signed data object** at root level. It **shall** be the only data object at root (besides optionally `mimetype`). Can itself be a container (ZIP, ASiC, OCF, ODF, UCF).
3. **META-INF folder** containing one of:
   - a) **`timestamp.tst`**: binary TimeStampToken [3] over the entire data object.
   - b) **`signature.p7s`**: detached CAdES signature. Multiple parallel/counter signatures allowed in one CAdES structure.
   - c) **`signatures.xml`**: root element `<asic:XAdESSignatures>` (per A.5) containing one or more detached `ds:Signature` elements conformant to XAdES. For ASiC‑S, `<ds:Reference>` **shall** reference the data object per A.6. If URI absent, implied reference. Canonicalization **shall** keep `ds:Signature` as child of `<asic:XAdESSignatures>`.
- Other application‑specific metadata may be added in META‑INF.

### 5.3 Mime type correlation check
If `mimetype` is present, conformant implementations **shall** check consistency with 5.2.1 item 2 and 5.2.2 item 1.

## 6 Associated Signature Extended form (ASiC‑E)
### 6.1 General Requirement of ASiC‑E
- **Shall** use ZIP [8].
- Implementations **may** support only one form type (CAdES, time‑stamp token, or XAdES) per clauses 7.2.1–7.2.3.

### 6.2 Detailed format for ASiC‑E with XAdES
#### 6.2.1 Media type identification
1. File extension: **`.asice`** (or **`.sce`**).
2. Mime type: **`application/vnd.etsi.asic‑e+zip`**.
3. Archive comment: if present, **shall** be as described.

#### 6.2.2 Contents of Container
1. Optional **`mimetype`** (per A.1). If file extension does not imply a supported container, **shall** be present.
2. One or more **`*signatures*.xml`** under `META-INF/` containing XAdES signatures. Signed objects may be referenced directly via `<ds:Reference>` or indirectly via `<ds:Manifest>` (per 6.2.4).
3. Root element of each signature file **shall** be one of:
   - a) `<asic:XAdESSignatures>` (recommended)
   - b) `<document-signatures>` [9]
   - c) `<signatures>` [7]
   - d) any other element (including `ds:Signature` itself) – allowed for legacy.
   - All root elements in a given container **should** be the same. Canonicalization **shall** keep `ds:Signature` as child of root element.
4. Other optional metadata in META‑INF:
   - a) `container.xml` – well‑formed per [7]; identifies root data objects.
   - b) `manifest.xml` – well‑formed per [9].
   - c) `metadata.xml` – well‑formed per [7].

#### 6.2.3 Informative example
Direct `ds:Reference` usage is preferred; `ds:Manifest` requires special attention (see 6.2.4).

#### 6.2.4 XAdES use in ASiC‑E with XAdES
- Rules of A.6 **shall** apply.
- `ds:Reference` **should** be used in preference to `ds:Manifest`.
- If `ds:Manifest` is used, the following restrictions **shall** apply:
  1. The `ds:Manifest` containing `ds:Reference` elements **shall** be signed (referenced in `ds:SignedInfo`).
  2. `ds:Manifest` elements **shall not** chain other `ds:Manifest`.
  3. Applications claiming compliance **shall** raise a warning on digest mismatch in any `ds:Manifest` child, even if cryptographic verification succeeds.
  4. An `Id` attribute **should** be used for referencing `ds:Manifest`.

### 6.3 Detailed format for ASiC‑E with CAdES and Time Stamp Tokens
#### 6.3.1 Media type identification
Same as 6.2.1 (`.asice`, mime type `application/vnd.etsi.asic‑e+zip`).

#### 6.3.2 Contents of Container
1. Optional `mimetype`.
2. Any number of data objects, arbitrarily structured in folders.
3. At least one **`META-INF/ASiCManifest*.xml`** per A.4 **shall** be present.
4. For each such manifest, a corresponding signature or time‑stamp token **shall** be present:
   - a) `META-INF/*signature*.p7s` (CAdES [1])
   - b) `META-INF/*timestamp*.tst` (RFC 3161 [3])
- Conformant implementations **shall**:
  1. Verify the signature/time‑stamp.
  2. Verify signed content conforms to A.4.
  3. Raise an error on digest mismatch in any `asic:DataObjectReference` even if cryptographic verification succeeds.
- No specific contentInfo OID defined.

### 6.4 Mime type correlation check
If `mimetype` present, conformant implementations **shall** check consistency with 6.2.1 item 2 and 6.2.2 item 1. Also, if manifest objects contain mimetype of referenced object, implementations **shall** check coherence.

## 7 Conformance requirements
An implementation can claim conformance to ASiC if it supports at least one of the following Conformance Clauses. Explicit reference to supported clauses may be used to profile implementations.

### 7.1 ASiC‑S conformance
#### 7.1.1 ASiC‑S CAdES Conformance Clause
**Shall** meet requirements of clauses 5.1, 5.2.1, 5.2.2 items 1, 2, and 3b. Verifying implementations **shall** support 5.3.

#### 7.1.2 ASiC‑S XAdES Conformance Clause
**Shall** meet requirements of clauses 5.1, 5.2.1, 5.2.2 items 1, 2, and 3c. Verifying implementations **shall** support 5.3.

#### 7.1.3 ASiC‑S Time‑stamp token Conformance Clause
**Shall** meet requirements of clauses 5.1, 5.2.1, 5.2.2 items 1, 2, and 3a. Verifying implementations **shall** support 5.3.

### 7.2 ASiC‑E conformance
#### 7.2.1 ASiC‑E XAdES Conformance Clause
**Shall** meet requirements of clauses 6.1, 6.2.1, 6.2.2. Additionally:
- **Shall** support at least one media type identification from 6.2.1 (both items 1 and 2 **should** be supported).
- **Shall** support at least one of the content from 6.2.2 item 4a or 4b.
- Verifying implementations **shall** support 6.4.

#### 7.2.2 ASiC‑E CAdES Conformance Clause
**Shall** meet requirements of clauses 6.1, 6.3.1, 6.3.2 (exclude 6.3.2 item 4b unless also claiming ASiC‑E Time‑stamp). Verifying implementations **shall** support 6.4. **Shall** support at least one media type identification from 6.3.1 (both items 1 and 2 **should** be supported).

#### 7.2.3 ASiC‑E Time‑stamp token Conformance Clause
**Shall** meet requirements of clauses 6.1, 6.3.1, 6.3.2 (exclude 6.3.2 item 4a unless also claiming ASiC‑E CAdES). Verifying implementations **shall** support 6.4. **Shall** support at least one media type identification from 6.3.1 (both items 1 and 2 **should** be supported).

#### 7.2.4 ASiC‑E other container Conformance Clause
Implementations claiming this clause **shall** also claim conformance to an external container specification. They **shall** support clauses 6.1 and 6.2.2 items 2 and 3, which have precedence over external requirements. Additional requirements from clause 6 apply if not contradictory.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 (ASiC‑S Gen) | ZIP format shall be used per 5.2.2 structure. | shall | 5.1 |
| R2 (ASiC‑S Mimetype) | If file extension does not imply ASiC, mimetype shall be present and first option of 5.2.1 item 2 shall apply. | shall | 5.2.2 item 1 |
| R3 (ASiC‑S Signed Object) | Signed data object shall be the only data object at root level (except mimetype). | shall | 5.2.2 item 2 |
| R4 (ASiC‑S XAdES Reference) | For XAdES, ds:Reference shall reference data object per A.6; if URI absent, implied reference. | shall | 5.2.2 item 3c |
| R5 (ASiC‑S Canonicalization) | Canonicalization shall keep ds:Signature as child of asic:XAdESSignatures. | shall | 5.2.2 item 3c |
| R6 (ASiC‑S Mime Check) | Conformant implementations shall check mimetype consistency. | shall | 5.3 |
| R7 (ASiC‑E Gen) | ZIP format shall be used. | shall | 6.1 |
| R8 (ASiC‑E XAdES Root) | Root element of signature files shall be one of four allowed types. | shall | 6.2.2 item 3 |
| R9 (ASiC‑E XAdES Canonicalization) | Canonicalization shall keep ds:Signature as child of root element. | shall | 6.2.2 item 3 |
| R10 (ASiC‑E XAdES Manifest) | If ds:Manifest used, it shall be signed; no chaining of manifests; warning on digest mismatch; Id attribute should be used. | shall/should | 6.2.4 items 1‑4 |
| R11 (ASiC‑E CAdES/TST) | At least one META-INF/ASiCManifest*.xml shall be present. | shall | 6.3.2 item 3 |
| R12 (ASiC‑E CAdES/TST Sign) | For each manifest, a corresponding signature.p7s or timestamp.tst shall be present. | shall | 6.3.2 item 4 |
| R13 (ASiC‑E CAdES/TST Verify) | Implementations shall verify signature/time‑stamp, check A.4 conformance, and raise error on digest mismatch. | shall | 6.3.2 (verification requirements) |
| R14 (ASiC‑E Mime Check) | Conformant implementations shall check mimetype consistency. | shall | 6.4 |
| R15 (A.1 Mimetype) | Mimetype shall not be compressed or encrypted; shall be first in archive; no extra fields; compression method zero; specific octet values. | shall | A.1 |
| R16 (A.6 Referencing) | References to data objects inside container shall be relative URIs; base URI is root directory; no external references allowed. | shall | A.6 items 1‑3 |

## Normative Annexes
### Annex A – ASiC metadata specification and data naming and referencing
- **A.1 Mimetype**: Must be first, uncompressed, no extra fields; used for magic number support.
- **A.2 MIME registrations**: Defines `application/vnd.etsi.asic‑s+zip` and `application/vnd.etsi.asic‑e+zip` with extensions `.asics`/`.scs` and `.asice`/`.sce` respectively, plus `application/vnd.etsi.timestamp‑token` with `.tst`.
- **A.3 XML Schema**: Namespace `http://uri.etsi.org/02918/v1.2.1#`. Schema file attached to specification; hash values provided.
- **A.4 ASiCManifest content**: Root element `<asic:ASiCManifest>` containing `<asic:SigReference>` (URI and MimeType), one or more `<asic:DataObjectReference>` (URI, MimeType, optional Rootfile, plus ds:DigestMethod and ds:DigestValue), and optional `<asic:ASiCManifestExtensions>` with `<asic:Extension>` elements.
- **A.5 XAdESSignatures content**: Root element `<asic:XAdESSignatures>` containing one or more `<ds:Signature>` elements (detached XAdES signatures).
- **A.6 Naming and referencing data within ASiC**: References to data objects inside container must be relative URIs; base URI is root directory; no external references allowed; for implementations claiming external specs, their referencing rules prevail.

## Informative Annexes (Condensed)
- **Annex B (Informative) – Example Application to Specific File Formats**: Provides examples for ASiC‑S (PDF with CAdES, document time‑stamp, signature of a nested ZIP) and ASiC‑E (with XAdES signing two XML files; with CAdES/time‑stamp for workflow where two XML documents are signed and later PDF versions are time‑stamped). Detailed XML excerpts show container structures and manifest content.
- **Annex C (Informative) – Container metadata information cross reference**: Table comparing metadata elements (mimetype, manifest, metadata, container, signatures) across ASiC‑E with XAdES, OCF, ODF, and UCF.
- **Annex D (Informative) – Bibliography**: Lists W3C XSLT 2.0, OASIS RELAX NG, and ETSI Drafting Rules.