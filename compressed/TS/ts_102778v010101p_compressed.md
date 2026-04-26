# ETSI TS 102 778 V1.1.1: Electronic Signatures and Infrastructures (ESI); PDF Advanced Electronic Signature Profiles; CMS Profile based on ISO 32000-1
**Source**: ETSI | **Version**: V1.1.1 | **Date**: April 2009 | **Type**: Normative Technical Specification
**Original**: http://www.etsi.org (DTS/ESI-000063)

## Scope (Summary)
This document profiles the use of PDF digital signatures as specified in ISO 32000-1 [1] and based on CMS [i.2], for any application area where PDF is used. It aims to maximize interoperability of CMS-based electronic signatures in various business areas, without repeating base requirements of referenced standards. Clause 4 provides an informative description; clause 5 specifies normative conformance requirements.

## Normative References
- [1] ISO 32000-1 (2008): "Document Management - Portable Document Format - PDF 1.7"
- [2] IETF RFC 2315: "PKCS #7: Cryptographic Message Syntax, Version 1.5"
- [3] ITU-T Recommendation X.509 / ISO/IEC 9594-8: "Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks"
- [4] IETF RFC 3280: "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile"
- [5] IETF RFC 2560: "X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP"
- [6] IETF RFC 3161: "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)"
- [7] ETSI TS 102 176-1: "Electronic Signatures and Infrastructures (ESI); Algorithms and Parameters for Secure Electronic Signatures; Part 1: Hash functions and asymmetric algorithms"
- [8] ISO 19005-1 (2005): "Document management - Electronic document file format for long-term preservation -- Part 1: Use of PDF 1.4 (PDF/A-1)"

## Definitions and Abbreviations
### Definitions
- **certification signature**: Signature used in conjunction with modification detection permissions (MDP) as defined by ISO 32000-1 [1], clause 12.8.2.2
- **conforming reader**: Software application able to read and process PDF files conformant to ISO 32000-1 [1]
- **may**: Means that a course of action is permissible within this profile.
- **PDF serial signature**: Signature workflow where subsequent signers sign the document plus the previous signature and any modifications (e.g., form fill-in)
- **PDF signature**: DER-encoded PKCS#7 binary data object containing a digital signature and other information necessary for verification (e.g., signer's certificate, revocation information)
- **seed value dictionary**: PDF data structure (type dictionary, per ISO 32000-1 [1] clause 12.7.4.5 table 234) that constrains properties of a signature applied to a specific signature field
- **shall**: Absolute requirement of this profile; must be strictly followed for conformance.
- **should**: Among several possibilities, one is recommended as particularly suitable; full implications must be understood before deviating.
- **signature dictionary**: PDF data structure (type dictionary, per ISO 32000-1 [1] clause 12.8.1 table 252) containing all information about the digital signature.

### Abbreviations
- CAdES: CMS Advanced Electronic Signatures (per TS 101 733 [i.1])
- CMS: Cryptographic Message Syntax
- CRL: Certificate Revocation List
- MDP: Modification Detection Permissions
- OCSP: Online Certificate Status Protocol
- PDF: Portable Document Format

## 4 Description of Profile for CMS Signatures in PDF (Informative)

### 4.1 Introduction
This profile specifies a PDF signature per ISO 32000-1:2008 [1] with additional restrictions to improve interoperability.

### 4.2 Features
- Signature encoded in CMS per PKCS #7 1.5 (RFC 2315 [2]).
- Supports serial signatures.
- Optionally includes signature time-stamp.
- Optionally includes revocation information.
- Signature protects document integrity and authenticates signatory.
- Optionally includes reasons, location, contact info.
- "Legal content attestation" can indicate PDF capabilities affecting the signed document (e.g., JavaScript).

### 4.3 PDF Signatures
- Digital signatures in ISO 32000-1 [1] support adding a signature immediately, providing a placeholder, or checking validity.
- The signature and optional info are in a signature dictionary (ISO 32000-1 [1] clause 12.8.1 table 252).
- The digest is computed over a range of file bytes; the range **shall** be the entire file, including signature dictionary but excluding the PDF Signature itself (ByteRange entry). (Normative from ISO 32000-1 recommendation.)
- The PDF Signature (DER-encoded PKCS#7 binary data object) **shall** be in the Contents entry. The PKCS#7 object **shall** conform to RFC 2315 [2] and include signer's X.509 [3] certificate.
- Only PKCS#7 (not PKCS#1) is allowed per this profile.
- Timestamping and revocation information **should** be included (per ISO 32000-1 recommendation). Revocation info and chain certificates **shall** be captured and validated before completing signature creation. Revocation info **shall** be a signed attribute.
- Inclusion of RFC 3281 [i.3] attribute certificates is not recommended (reduces interoperability).

### 4.4 Signature Types
- Certification signatures: work with MDP (ISO 32000-1 clause 12.8.4) to allow limited modifications.
- Usage Rights (ISO 32000-1 clause 12.8.2.3): enhance document with additional workflow rights.

### 4.5 Handlers
- Filter and SubFilter define the signature handler. Only SubFilter values adbe.pkcs7.detached and adbe.pkcs7.sha1 (per ISO 32000-1 clause 12.8.3.3.1) **shall** be used for compliance.
- Algorithm list per ISO 32000-1 table 257; guidance on algorithm choices in TS 102 176-1 [7]; SHA-1 is being phased out.

### 4.6 PDF Serial Signatures
- Only a single signer (single "SignerInfo" structure) **shall** be in any PDF signature.
- Multiple signers: each signature has its own dictionary and ByteRange. Subsequent signers sign document plus previous signatures. Verification is per signature, aggregate result gives final status.

### 4.7 Signature Validation
When verifying signatures, a conforming reader **shall**:
1. Verify document digest matches signature (ISO 32000-1 clause 12.8.1).
2. Validate certificate path per RFC 3280 [4] at time indicated by timestamp or trusted signing time; revocation checked per clause 4.9.

### 4.8 Time Stamping
- A timestamp from a trusted server **should** be applied immediately after signature creation to reflect signing time.
- Timestamp process per RFC 3161 [6]. If embedded, **shall** be as described in ISO 32000-1 clause 12.8.3.3.1.

### 4.9 Revocation Checking
- Conforming reader **should** embed revocation info (signed attribute adbe-revocationInfoArchival) before completing signature.
- When validating, a conforming reader **may** ignore embedded revocation info in favor of its own policies.
- Methods: CRL [4] or OCSP [5].

### 4.10 Seed Values and Signature Policies
- Seed value dictionary (ISO 32000-1 clause 12.7.4.5 table 234) sets rules for the signature (e.g., digest method, revocation, timestamping). Seed values that would require violation of this profile **shall not** be used.

### 4.11 ISO 19005-1:2005 (PDF/A-1)
- PDF/A-1 [8] (based on PDF 1.4) is for long-term archiving; lacks embedded revocation and timestamping. Not forbidden, but PDF/A-1 readers may not process them.
- PDF/A-2 (expected 2010) will be based on ISO 32000-1 and support full signature features.

## 5 Requirements of Profile for CMS Signatures in PDF (Normative)

### 5.1 Requirements from clause 4.3 (PDF Signatures)
- a) Signature info **shall** be embedded in the document; ByteRange **shall** cover entire file excluding the PDF Signature itself.
- b) PDF Signature (DER-encoded PKCS#7) **shall** be placed in Contents entry of signature dictionary.
- c) PKCS#7 object **shall** conform to RFC 2315 [2] and **shall** include signer's X.509 signing certificate.
- d) Timestamp and revocation info **should** be included; revocation info and certificate chain **shall** be captured and validated before completing signature creation.
- e) If revocation info present, it **shall** be a signed attribute.
- f) Use of attribute certificates (RFC 3281) is **not recommended**.

### 5.2 Requirements from clause 4.5 (Handlers)
- a) Only SubFilter values adbe.pkcs7.detached and adbe.pkcs7.sha1 **shall** be used.

### 5.3 Requirements from clause 4.6 (PDF Serial Signatures)
- a) Only a single signer (single "SignerInfo") **shall** appear in any PDF signature.

### 5.4 Requirements from clause 4.7 (Signature Validation)
- a) When verifying signatures, a conforming reader **shall** perform the steps in clause 4.7.

### 5.5 Requirements from clause 4.8 (Time Stamping)
- a) A trusted timestamp **should** be applied immediately after signature creation.
- b) If timestamp embedded, it **shall** be as described in ISO 32000-1 clause 12.8.3.3.1.

### 5.6 Requirements from clause 4.9 (Revocation Checking)
- a) A conforming reader **may** ignore embedded revocation info per its own policies.

### 5.7 Requirements from clause 4.10 (Seed Values and Signature Policies)
- a) Seed values that would require violation of this profile **shall not** be used.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | ByteRange shall cover entire file except the PDF Signature itself. | shall | 5.1.a, 4.3 |
| R2 | PDF Signature shall be DER-encoded PKCS#7 in Contents entry. | shall | 5.1.b, 4.3 |
| R3 | PKCS#7 object shall conform to RFC 2315 and include signer's certificate. | shall | 5.1.c, 4.3 |
| R4 | Revocation info and certificate chain shall be captured and validated before signature completion. | shall | 5.1.d, 4.3 |
| R5 | Revocation info shall be a signed attribute (if present). | shall | 5.1.e, 4.3 |
| R6 | Only SubFilter adbe.pkcs7.detached or adbe.pkcs7.sha1 shall be used. | shall | 5.2.a, 4.5 |
| R7 | Only a single SignerInfo per PDF signature. | shall | 5.3.a, 4.6 |
| R8 | Signature validation shall follow steps in clause 4.7. | shall | 5.4.a, 4.7 |
| R9 | Timestamp shall be embedded per ISO 32000-1 clause 12.8.3.3.1 (if used). | shall | 5.5.b, 4.8 |
| R10 | Seed values shall not require violation of this profile. | shall | 5.7.a, 4.10 |
| R11 | Timestamp should be applied immediately after signature creation. | should | 5.5.a, 4.8 |
| R12 | Revocation info should be embedded. | should | 5.1.d (first part), 4.3, 4.9 |
| R13 | Use of attribute certificates is not recommended. | not recommended | 5.1.f, 4.3 |
| R14 | Conforming reader may ignore embedded revocation info per own policies. | may | 5.6.a, 4.9 |