# ETSI TR 102 923 V1.1.1: PDF Advanced Electronic Signatures (PAdES); Usage and implementation guidelines
**Source**: ETSI | **Version**: V1.1.1 | **Date**: July 2010 | **Type**: Informative (Technical Report)
**Original**: [ETSI TR 102 923 V1.1.1 (2010-07)](http://www.etsi.org)

## Scope (Summary)
Provides guidance on expected usage and implementation of PAdES signatures for securing PDF documents. This is an informative document; no mandatory requirements are specified, only recommendations and suggestions for correct usage and implementation details.

## Normative References
- Not applicable.

## Informative References
- [i.1] Adobe XFA: "XML Forms Architecture (XFA) Specification".
- [i.2] Directive 1999/93/EC of the European Parliament and of the Council on a Community framework for Electronic Signatures.
- [i.3] ETSI TS 101 733: "CMS Advanced Electronic Signatures (CAdES)".
- [i.4] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)".
- [i.5] OASIS-DSSX: "Profile for comprehensive multi-signature verification reports for OASIS Digital Signature Services. Committee Draft Version 1.0".
- [i.6] ISO 32000-1: "Document management - Portable document format - Part 1: PDF 1.7".
- [i.7] ETSI TS 102 778-1: PAdES Overview.
- [i.8] ETSI TS 102 778-2: PAdES Basic - Profile based on ISO 32000-1.
- [i.9] ETSI TS 102 778-3: PAdES Enhanced - PAdES-BES and PAdES-EPES Profiles.
- [i.10] ETSI TS 102 778-4: PAdES Long Term - PAdES LTV Profile.
- [i.11] ETSI TS 102 778-5: PAdES for XML Content - Profiles for XAdES signatures.
- [i.12] ETSI TS 102 778-6: Visual Representations of Electronic Signatures.
- [i.13] IETF RFC 3852 (2004): "Cryptographic Message Syntax (CMS)".
- [i.14] IETF RFC 3709: "Internet X.509 Public Key Infrastructure: Logotypes in X.509 Certificates".
- [i.15] IETF RFC 3739: "Internet X.509 Public Key Infrastructure: Qualified Certificates Profile".
- [i.16] ETSI TS 102 779: (Reference to multi-component KPI – note: original document contains a suspect reference, kept as-is).
- [i.17] IETF RFC 3161: "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)".

## Definitions and Abbreviations

### Definitions
- **Conforming signature handler**: Software application that performs digital signature operations in conformance with ISO 32000-1 [i.6] and the appropriate PAdES profile.
- **PDF serial signature**: Workflow where subsequent signers sign the document plus previous signatures and any modifications (e.g., form fill-in).
- **PDF signature**: Binary data object based on CMS (RFC 3852 [i.13]) placed within a PDF document as per ISO 32000-1 [i.6], clause 12.8.
- **Signature dictionary**: PDF data structure (type dictionary) as per ISO 32000-1 [i.6], clause 12.8.1, table 252.
- **Signer**: Entity that creates an electronic signature.
- **Validation data**: Data used by a verifier to determine signature validity (e.g., certificates, CRLs, OCSP responses).
- **Verifier**: Entity that validates an electronic signature.

### Abbreviations
- **AdES**: Advanced Electronic Signatures
- **CAdES**: CMS Advanced Electronic Signature (see TS 101 733 [i.3])
- **CMS**: Cryptographic Message Syntax (RFC 3852 [i.13])
- **CRL**: Certificate Revocation List
- **DSS**: Document Security Store
- **ESI**: Electronic Signatures and Infrastructure
- **LTV**: Long Term Validation
- **OCSP**: Online Certificate Status Protocol
- **PAdES**: PDF Advanced Electronic Signature
- **PAdES-BES**: PAdES Basic Electronic Signature
- **PAdES-EPES**: PAdES Explicit Policy Electronic Signature
- **PDF**: Portable Document Format
- **XAdES**: XML Advanced Electronic Signatures (see TS 101 903 [i.4])
- **XFA**: XML Forms Architecture
- **XML**: eXtensible Markup Language

## Background: PAdES' historical context (Condensed)
ETSI ESI TC defined a framework for AdES in three syntaxes: ASN.1 (CAdES), PDF (PAdES), and XML (XAdES). PAdES extends PDF signatures with signed properties and long-term validation features, bridging the gap to CAdES/XAdES.

## Using PAdES

### Parts of PAdES specification (Summary)
PAdES comprises 6 parts:
1. **TS 102 778-1 [i.7]**: Overview framework.
2. **TS 102 778-2 [i.8]**: PAdES Basic – profile of ISO 32000-1 signatures; supports serial signatures, optional reason/location/contact info, recommends signature time‑stamp and revocation info.
3. **TS 102 778-3 [i.9]**: PAdES Enhanced – PAdES-BES and PAdES-EPES profiles; uses CAdES-BES/EPES with signed attributes (signing certificate, policy identifier, etc.).
4. **TS 102 778-4 [i.10]**: PAdES Long Term (LTV) – adds DSS and Document Timestamp PDF objects for long-term validation.
5. **TS 102 778-5 [i.11]**: PAdES for XML Content – profiles for XAdES signatures on XML embedded in PDF or on XFA forms.
6. **TS 102 778-6 [i.12]**: Visual Representations – requirements and recommendations for signature appearance and verification representation.

### PAdES, ISO 32000-1, CAdES and XAdES
PAdES is fully compatible with ISO 32000-1 [i.6]; part 2 profiles ISO 32000-1. PAdES builds on existing PDF reader installed base. Supports Advanced Electronic Signatures compliant with EU Directive 1999/93 and long‑term validation.

### Selecting the right PAdES Profile
- **PAdES Part 2**: When compatibility with ISO 32000-1 readers is paramount and no need for explicit policy or long-term.
- **PAdES Part 3**: When explicit policy reference or CAdES signed attributes are needed, but no long-term requirement.
- **PAdES Part 4**: When long-term validation is required; uses CAdES signatures plus DSS and Document Timestamp.
- **PAdES Part 5 (XAdES-based)**:
  - **XAdES-Signed-Object-And-PDF Packaged**: XML signed with XAdES, then embedded in PDF.
  - **XAdES-XFA-Signed**: XFA forms signed with XAdES.

### PAdES types vs. CAdES/XAdES types (Table 1 summarised)
| PAdES Profile | Equivalent CAdES/XAdES Forms | Notes |
|---|---|---|
| PAdES-BES (Part 3) | CAdES-BES, CAdES-T | With or without signature time-stamp |
| PAdES-EPES (Part 3) | CAdES-EPES, CAdES-T | Includes explicit policy |
| PAdES-LTV (Part 4) without doc timestamp | Extended CAdES-C (values instead of references) | Self-contained document |
| PAdES-LTV with doc timestamp | Extended CAdES-X, CAdES-X-L, CAdES-A | Values, document time-stamp |
| Part 5 profiles for XAdES embedded in PDF | Supports all XAdES forms (–BES to –A) | Extraction/embedding required for evolution |
| Part 5 profiles for XAdES on XFA | Supports XAdES-B, -EPES, -T; LTV via DSS | Uses DSS and Document Timestamp |

### PAdES and CMS (PAdES Part 2)
- Signatures are regular CMS signatures per ISO 32000-1 [i.6], with constraints (e.g., only DER-encoded PKCS#7, no PKCS#1).
- **Optional features**:
  - Signature time-stamp (as per ISO 32000-1 clause 12.8.3.3.1).
  - Revocation information (adbe-revocationInfoArchival signed attribute).
  - Reason, Location, ContactInfo (signature dictionary entries).
  - Legal content attestation.

### PAdES Part 3 and CAdES
- Signatures encoded as CAdES-BES, CAdES-EPES, or CAdES-T (depending on signed attributes).
- **Signed attributes used**:
  - ESS signing-certificate (recommended).
  - Signature-policy-identifier (optional, makes it EPES).
  - Commitment-type-indication (optional, only with policy).
  - Content-time-stamp (optional).
  - Signer-attributes (optional).
- **Attributes NOT used**: signing-time, content-reference, content-identifier, content-hints, signed-location (replaced by PDF dictionary entries), counter-signature.
- **Unsigned attributes**: signature-time-stamp (recommended).
- SubFilter set to `ETSI.CAdES.detached`.
- ByteRange covers entire file except signature value.

### PAdES Part 4 and CAdES
- Adds two new PDF container objects: **Document Security Store (DSS)** and **Document Time-stamp**.
- DSS contains all validation data (certificates, CRLs, OCSP) for any signature, plus optional VRI dictionaries per signature.
- Document Time-stamp (Type `DocTimeStamp`, SubFilter `ETSI.RFC3161`) time‑stamps the whole document except itself.
- Supports repeating addition of document time‑stamps to maintain validity over time.
- No references to validation material (unlike CAdES-X) to simplify implementation.
- Functional equivalence to CAdES-C, -X, -X-L, -A but with values instead of references.

### PAdES and XAdES (PAdES Part 5)
- Two scenarios:
  1. **XAdES-Signed-Object-And-PDF Packaged**: XML signed with XAdES, then embedded in PDF. Evolution requires extraction and re-embedding.
  2. **XAdES-XFA-Signed**: XAdES signatures on XFA forms; LTV evolution uses DSS and Document Timestamp (same as Part 4).

### PAdES Part 6
- Specifies visual representation of signature appearance (at signing time) and verification results.
- Aims for consistency between appearance and verification to help human users detect fraudulent names.
- Uses certificate images (RFC 3709 [i.14]) or handwritten signature images (RFC 3739 [i.15]) when available.
- Verification representation should be hierarchical, separate from document content.

## Implementing PAdES

### Implementing PAdES Part 2
- **Profile of ISO 32000-1**: Only DER-encoded PKCS#7 in Contents entry.
- **Serial signatures allowed** (chain of signatures each signing previous ones and document). Parallel signatures NOT allowed.
- **Signature time-stamp**: Recommended to include as soon as possible after signing. Embedded per ISO 32000-1 clause 12.8.3.3.1.
- **Revocation information at signing**: Signer should validate and embed revocation info via `adbe-revocationInfoArchival` signed attribute. Verifier may ignore embedded data.
- **Signature validation**: Conforming handler checks validity at time indicated by signature time-stamp (or other trusted time). May ignore embedded revocation info.

### Implementing PAdES Part 3
- **Features provided**: protection of signing certificate; signed attributes (claimed signing time, policy, reason, commitment, signer location, signer attributes, content time‑stamp); unsigned attribute signature‑time‑stamp.
- **Signature dictionary**: SubFilter = `ETSI.CAdES.detached`; no Cert entry; ByteRange covers whole file except signature.
- **Handling of signed attributes**: Uses PDF dictionary entries for signing time (M), location (Location), reason (Reason) instead of CAdES attributes. Commitment-type-indication only used if signature-policy-identifier present.
- **Signature Policy vs. Seed Values**: Policy is general endorsement rules; seed values are workflow constraints. Signature Policy OID can be added to seed value dictionary via optional entries (`SignaturePolicyOID`, `SignaturePolicyCommitmentType`).
- **Signature validation**: Verification time determined by trusted signing time or current time. Warning if certificate revoked after signing time but valid at signing.
- **Time-stamp on signed content**: `content-time-stamp` protects the data signed (ByteRange).

### Implementing PAdES Part 4
- **Long-term achieved by**:
  - Adding DSS (certificates, CRLs, OCSP) and Document Timestamp.
  - Validation data added after verification.
  - Document Timestamp proves existence at a time.
  - Process repeated with new document time‑stamps before previous one’s certificate expires.
- **DSS**:
  - Contains all validation data for any signature in the document.
  - Optional VRI dictionaries link validation data to specific signatures (via SHA1 digest of signature).
- **Document Timestamp**:
  - Type `DocTimeStamp`, SubFilter `ETSI.RFC3161`.
  - Added at end; timestamps all document except its own Content entry.
  - Recurrent addition: before adding new timestamp, validation data for previous timestamp must be added.
- **Validation process**: Validate outermost document timestamp at current time, then inner timestamps at the time of the enclosing timestamp, finally signature at innermost timestamp time.
- **No references**: Only values stored, to improve interoperability and avoid failure cases.

### Implementing PAdES Part 5

#### Profiles for XAdES-signed XML documents embedded in PDF containers
- **Basic Profile**:
  - Allows serial and parallel signatures.
  - XAdES-signed XML must embed all signed data objects or have valid `ds:Reference`.
  - XAdES properties: recommends `SigningCertificate`; allows `SigningTime`, `SignaturePolicyIdentifier`, `SignatureProductionPlace`, `SignerRole`, `SignedDataObjectFormat`, `CommitmentTypeIndication`, `AllDataObjectsTimeStamp`, `IndividualDataObjectsTimeStamp`; allows `SignatureTimeStamp` unsigned property.
  - Supports countersignatures (serial) and parallel signatures if all XAdES signatures embedded.
  - **Warning**: Approval signatures on embedding PDF will be invalidated if XAdES signature is upgraded. Certification signatures with DocMDP allow changes.
- **Long Term Profile**:
  - Upgrade by extracting, evolving XAdES (adding unsigned properties), re‑embedding.
  - Validation: outermost `ArchiveTimeStamp` at current time; inner ones at previous timestamp time; signature at innermost timestamp.

#### Profiles for XAdES signatures on XFA forms
- **Basic Profile**:
  - XAdES-BES, -EPES, -T signatures.
  - Signs `xades:SignedProperties` and `ds:SignatureProperties` (includes claiming signing time and reasons per XFA).
  - Allows serial/parallel signatures using XAdES mechanisms.
  - Recommends `SigningCertificate`; allows other signed properties; bans `SigningTime` (use XFA’s `CreateDate`).
- **Long Term Profile**:
  - Uses DSS and VRI dictionaries (same as Part 4).
  - VRI key: base-16-encoded SHA1 of canonicalized `ds:Signature` (exclusive canonicalization).
  - Validation: similar cascade (outermost archive timestamp at current time, inner at previous, signature at innermost).

### Implementing PAdES Part 6
- **Signature appearance**:
  - Should include certificate images (RFC 3709) or handwritten signature images (RFC 3739) if available.
  - Otherwise, use common name (CN) and organization (O) from certificate.
  - Should avoid multiple content streams for different verification states.
- **Signature verification representation**:
  - Display in a separate window/frame, not modifiable by document content.
  - Hierarchical: top level shows result and identity (similar to appearance), lower levels show detailed validation info (time‑stamps, OCSP, etc.).
  - Identity includes CN, O (always displayed), logo, handwritten signature, trusted CA friendly name.
  - Detailed representation may be based on OASIS verification reports [i.5].

## Requirements Summary (Key Recommendations)

| ID | Recommendation | Type | Reference |
|---|---|---|---|
| R1 | PAdES Part 2: Signature time-stamp should be included as soon as possible after signing. | should | Clause 6.1.2 |
| R2 | PAdES Part 2: Signer should validate and embed revocation information before signing. | should | Clause 6.1.3 |
| R3 | PAdES Part 2: Conforming signature handler may ignore embedded revocation info in favor of its own. | may | Clause 6.1.4 |
| R4 | PAdES Part 3: Use `ETSI.CAdES.detached` SubFilter. | mandatory | Clause 6.2.2 |
| R5 | PAdES Part 3: Signature policy OID may be added to seed value dictionary via `SignaturePolicyOID` entry. | optional | Clause 6.2.4 |
| R6 | PAdES Part 3: Verification time determined by trusted signing time or current time; warning if revocation after signing. | informative | Clause 6.2.5 |
| R7 | PAdES Part 4: Validation material added after verification; document timestamp proves existence. | mandatory | Clause 6.3.1 |
| R8 | PAdES Part 4: Before adding new document timestamp, all validation data for previous timestamp must be added. | mandatory | Clause 6.3.3.2 |
| R9 | PAdES Part 4: Validate outermost document timestamp at current time, inner timestamps at enclosing timestamp time. | recommended | Clause 6.3.4 |
| R10 | PAdES Part 5 (Basic Profile for XML): Allows serial/parallel signatures; recommends `SigningCertificate`. | recommended | Clause 6.4.1.1.3 |
| R11 | PAdES Part 5 (XFA): Uses XFA’s `CreateDate` instead of `SigningTime`. | mandatory | Clause 6.4.2.1.3 |
| R12 | PAdES Part 6: Signature appearance should use certificate images when available. | should | Clause 6.5.1 |
| R13 | PAdES Part 6: Verification representation must be displayed in a separate, non-modifiable window. | mandatory | Clause 6.5.3 |

## Informative Annexes (Condensed)
- **Annexes**: Not present in the original document; the document itself is a Technical Report (informative). Additional FAQ information available at www.padesfaq.net.