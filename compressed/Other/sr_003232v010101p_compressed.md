# ETSI SR 003 232: Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles (PAdES); Printable Representations of Electronic Signatures
**Source**: ETSI | **Version**: V1.1.1 | **Date**: February 2011 | **Type**: Informative  
**Original**: DSR/ESI-000113, available at http://www.etsi.org

## Scope (Summary)
Discusses techniques for printable representations of advanced electronic signature (AdES) signature values in PDFs, focusing on alphanumeric strings or bar codes. The printable signature value provides a “secured fingerprint” to match a printed document to its electronic original; it does not replace electronic validation. This SR is informative and may form the basis of a future ETSI specification.

## References
### Normative references
None.

### Informative references
- [i.1] ISO 32000-1: “Document management – Portable document format – Part 1: PDF 1.7”
- [i.2] ETSI TS 102 778-1: “Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles; Part 1: PadES Overview”
- [i.3] ETSI TS 102 778-4: “Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles; Part 4: PAdES Long Term – PAdES LTV Profile”
- [i.4] ETSI TS 102 778-6: “Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles; Part 6: Visual Representations of Electronic Signatures”
- [i.5] Directive 1999/93/EC on a Community framework for electronic signatures
- [i.6] IETF RFC 3852 (2004): “Cryptographic Message Syntax (CMS)”
- [i.7] ISO 19005-1:2005: “Document management – Electronic document file format for long-term preservation – Part 1: Use of PDF 1.4 (PDF/A-1)”
- [i.8] ETSI TS 102 778 (all parts): “Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles”

## Definitions and Abbreviations
- **PDF Signature**: binary data object based on CMS (RFC 3852 [i.6]) containing a digital signature placed within a PDF document as specified in ISO 32000-1 [i.1], clause 12.8.
- **printable signature value**: printable representation of, or derived from, the AdES signature value, e.g., alphanumeric string or bar code.
- **signature appearance**: visual representation of the human act of signing placed within a PDF at signing time and linked to an AdES.
- **signature dictionary**: PDF data structure (type dictionary) per ISO 32000-1 [i.1] clause 12.8.1, Table 252 containing all information about the Digital Signature.
- **signature verification representation**: visual representation of the verification of an AdES.
- **signer**: entity that creates an electronic signature.
- **verifier**: entity that validates an electronic signature.
- **AdES**: Advanced Electronic Signature (as per Directive 1999/93 [i.5]).
- **CMS**: Cryptographic Message Syntax (RFC 3852 [i.6]).
- **PAdES**: PDF Advanced Electronic Signature.
- **PDF**: Portable Document Format.

## 4 The printable representation of an AdES signature value
The AdES signature value is a sequence of bytes used to prove integrity and authenticate the signer. A printable form may be required to provide reliable proof of equivalence between an electronic document and its printed version. The printable signature value may include a digest of the signature value. Common practice is to embed the value as alphanumeric encoded text or a 2D barcode. Because the signature covers all visible content (“what you see is what you sign”), adding the printable value after signing must be done without invalidating the signature. Interoperability requires common understanding of:
- Digest algorithm (if a digest is applied).
- Encoding mechanism (e.g., Base64, barcode symbology).
- Storage location of the actual certificate and revocation information.

### 4.1 Methods of Display
#### 4.1.1 Alphanumeric Strings
- **Description**: The digest/hash of the document (or signature) is converted to an alphanumeric string using Base64 or ASCII85 and added to page content, typically as part of explanatory text.
- **Properties**: Simple to compute; space determined by hash length and font; readable by humans and (with guidance) by machines.

#### 4.1.2 Barcodes
- **Description**: An optical machine-readable representation using a specific symbology (1D or 2D). Options: encode the digest/hash into a 1D barcode (Figure 1), or encode page content (textual data or variable field values) into a 2D barcode (Figure 2). Larger data increases barcode size.
- **Dynamic computation**: PDF supports barcode form fields (AcroForm or XFA) computed at display time rather than signing time (PDF 1.5+, compatible with PDF/A-2 but not PDF/A-1).

### 4.2 Scope of Printable Signature
- **Constraint**: Standard AdES for PDF (ISO 32000-1 [i.1], PAdES [i.8]) apply to the whole PDF document when signed, including all graphics and layout. No mechanism exists to select parts of the PDF for signing or to restrict signatures to textual content only.
- **Consequence**: The same restrictions apply to printable signatures; the entire PDF (including graphics and formatting) is used to derive the printable signature. Verification of a printable signature reference is only possible with the original digital document.

### 4.3 Where does the actual certificate live?
- **Problem**: Signing modifies the document by embedding the certificate, signature value, and revocation information, changing the hash before vs. after signing.
- **Alternative**: Use a detached signature (certificate not embedded in PDF). Store signature data on a server with a reference in the visual representation. However, this makes the PDF not self-contained, requiring network access for verification and problematic for offline and long-term archiving.

### 4.4 Use of incremental updates
- **Mechanism**: PDF incremental updates (ISO 32000-1 [i.1], clause 7.5.6) allow adding new or changed objects at the end of the document without invalidating the signature hash.
- **Page content vs. annotations**: Adding the printable representation as standard page content will cause a conforming reader to show the document as changed (invalidating the signature). Using **annotations** (ISO 32000-1 [i.1], clause 12.5) to add information on a top layer **does not invalidate the signature**. Therefore, the use of annotations is **strongly recommended** in workflows involving embedded signatures.

### 4.5 Use of Document Timestamps
- **Definition**: TS 102 778-4 [i.3] defines a special signature that uses only a secure timestamp (no full certificate). It can act as a secure “wrapper” around the original document, its signature, and the incremental update containing the printable representation. Recommended in embedded signature workflows.
- **Legal effect**: The document timestamp signature has no legal meaning but proves that the document was signed at a specific time and has not been modified since.
- **Visual appearance**: Incorporating a timestamp time in the appearance is problematic for the same reason as signature value display; the same techniques (incremental updates, annotations) may be used to address this.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| None | This document is informative and contains no normative requirements. All statements are descriptive or advisory (may, should, recommended). | – | – |

## Informative Annexes (Condensed)
- **Intellectual Property Rights**: Standard ETSI IPR disclaimer; no investigation performed; no guarantee re essential IPRs beyond those disclosed.
- **Foreword**: SR produced by ETSI TC ESI.
- **Introduction**: Electronic signatures are essential for trust in electronic business. TS 102 778-6 covers visual representations of signatures; this SR addresses additional points for printable signature values when a signed PDF is printed. It discusses issues and potential solutions.
- **History**: Published February 2011.