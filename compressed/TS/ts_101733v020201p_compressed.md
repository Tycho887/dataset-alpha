# ETSI TS 101 733: CMS Advanced Electronic Signatures (CAdES)
**Source**: ETSI | **Version**: V2.2.1 | **Date**: 2013-04 | **Type**: Normative  
**Original**: http://www.etsi.org/deliver/etsi_ts/101700_101799/101733/02.02.01_60/ts_101733v020201p.pdf

## Scope (Summary)
Defines CMS-based advanced electronic signature formats (CAdES), including basic, explicit policy, time-stamped, complete validation data, extended, archive, and long-term forms. Specifies use of Trusted Service Providers and archival data to support long-term validity and arbitration. Builds on RFC 3852 (CMS), X.509, RFC 3280 (PKIX), RFC 3161 (TSP).

## Normative References
- [1] ITU-T X.509 (2008)/ISO/IEC 9594-8 (2008)
- [2] IETF RFC 3280 (2002) – Internet X.509 PKI Certificate and CRL Profile
- [3] IETF RFC 2560 (1999) – OCSP
- [4] IETF RFC 3852 (2004) – CMS
- [5] IETF RFC 2634 (1999) – Enhanced Security Services for S/MIME
- [6] IETF RFC 2045 (1996) – MIME Part One
- [7] IETF RFC 3161 (2001) – TSP
- [8] ITU-T X.680 (2008) – ASN.1 Notation
- [9] ITU-T X.501 (2008)/ISO/IEC 9594-1 (2008)
- [10] IETF RFC 3370 (2002) – CMS Algorithms
- [11] ITU-T F.1 – Public Telegram Service
- [12] ITU-T X.500
- [13] IETF RFC 3281 (2002) – Attribute Certificate Profile
- [14] ITU-T X.208 (1988) – ASN.1 (withdrawn)
- [15] IETF RFC 5035 (2007) – ESS Update: Adding CertID Algorithm Agility
- [16] IETF RFC 4998 (2007) – Evidence Record Syntax (ERS)

## Definitions and Abbreviations
- **arbitrator**: Entity that arbitrates disputes between signer and verifier.
- **CAdES-BES**: CAdES Basic Electronic Signature – minimum format with mandatory signed attributes.
- **CAdES-EPES**: CAdES Explicit Policy-based Electronic Signature – includes signature policy identifier.
- **CAdES-T**: CAdES with Time – includes time-stamp token or time-mark.
- **CAdES-C**: CAdES with Complete validation data references – includes complete certificate and revocation references.
- **CAdES-X**: Extended forms (Type 1, Type 2, Long) – adds time-stamps over validation data and/or certificate/revocation values.
- **CAdES-A**: Archival form – adds archive-time-stamp (ATSv2 or ATSv3).
- **CAdES-LT**: Long-Term form – adds long-term-validation attribute.
- **signature policy**: Set of rules for creation and validation of an electronic signature.
- **Time-Stamping Authority (TSA)**: Trusted third party that creates time-stamp tokens.
- **validation data**: Additional data (certificates, CRLs, OCSP responses, time-stamps) used to validate an ES.
- Abbreviations: AA, AARL, ACRL, API, ASN.1, CA, CARL, CMS, CRL, DSA, EC, ECDSA, ES, ESS, MIME, OCSP, OID, PKC, PKIX, RA, RSA, SHA, TSP, TST, TSU, URI, URL, XAdES, XMLDSIG.

## Overview
### Major Parties
- Signer, Verifier, Trusted Service Providers (CA, RA, CRL Issuer, OCSP Responder, TSA, Signature Policy Issuer), Arbitrator.

### Signature Policies
- Used to establish technical consistency; may be explicit (CAdES-EPES) or implied.

### Electronic Signature Formats
- **CAdES-BES**: Mandatory signed attributes: content-type, message-digest, and signing-certificate (or signing-certificate-v2). May include optional attributes (signing-time, content-hints, commitment-type-indication, signer-location, signer-attributes, content-time-stamp, mime-type). Unsigned attributes: countersignature.
- **CAdES-EPES**: Adds signature-policy-identifier as signed attribute.

### Formats with Validation Data
- **CAdES-T**: Adds signature-time-stamp attribute (unsigned) or time-mark.
- **CAdES-C**: Adds complete-certificate-references and complete-revocation-references (unsigned).
- **Extended forms (CAdES-X)**: CAdES-X Long (adds certificate-values, revocation-values), CAdES-X Type 1 (adds CAdES-C-time-stamp), CAdES-X Type 2 (adds time-stamped-certs-crls-references).
- **CAdES-A**: Adds archive-time-stamp (ATSv2) or archive-time-stamp-v3 (ATSv3). ATSv3 required for new archive time-stamps; ATSv2 for backward compatibility.
- **CAdES-LT**: Adds long-term-validation attribute (unsigned). Deprecated for signatures without existing long-term-validation attribute.

## Electronic Signature Attributes (Clause 5)
### General Syntax
- Uses CMS (RFC 3852) content types. Id-data recommended with MIME encoding.

### SignedData Type
- At least one SignerInfo present. signedAttrs shall contain content-type, message-digest, and signing-certificate or signing-certificate-v2.

### Mandatory Attributes
- **content-type** (OID id-contentType)
- **message-digest** (OID id-messageDigest)
- **signing-certificate** (if SHA-1) or **signing-certificate-v2** (other hash algorithms) – one and only one shall be present. The identified certificate shall match the signer's public key.

### Additional Mandatory for CAdES-EPES
- **signature-policy-identifier**: Signed attribute. Contains SignaturePolicyIdentifier (choice of SignaturePolicyId or SignaturePolicyImplied). Mandates a reference to the signature policy.

### Optional Attributes from CMS
- signing-time, countersignature (unsigned).

### Optional Attributes from ESS
- content-reference, content-identifier, content-hints.

### Additional Optional Attributes Defined in This Document
- **commitment-type-indication**: Signed. Indicates commitment type (proofOfOrigin, proofOfReceipt, etc.).
- **signer-location**: Signed. Geographical location.
- **signer-attributes**: Signed. Claimed or certified attributes.
- **content-time-stamp**: Signed. Time-stamp of content before signing.
- **mime-type**: Signed. Indicates mime-type of signed data. Only one instance allowed; shall not be used in countersignature.

### Support for Multiple Signatures
- **Independent**: Separate SignerInfo structures.
- **Embedded**: Via countersignature unsigned attribute.

## Additional Electronic Signature Validation Attributes (Clause 6)
All unsigned attributes.
### signature-time-stamp (CAdES-T)
- TimeStampToken over the signature value. May have multiple instances.

### Complete Validation Data (CAdES-C)
- **complete-certificate-references** (OID id-aa-ets-certificateRefs): References to CA certificates (excluding signer's certificate). Only one instance.
- **complete-revocation-references** (OID id-aa-ets-revocationRefs): References to CRLs and/or OCSP responses. One per certificate reference. At least one of CRL or OCSP for all but trust anchor.
- Optional: attribute-certificate-references, attribute-revocation-references.

### Extended Validation Data (CAdES-X)
- **CAdES-C-time-stamp** (Type 1): TimeStampToken over hash of signature value, time-stamp attribute, and complete references.
- **time-stamped-certs-crls-references** (Type 2): TimeStampToken over hash of complete references only.
- **certificate-values**: Contains actual certificates.
- **revocation-values**: Contains actual CRLs and OCSP responses.

### Archive Validation Data (CAdES-A)
- **archive-time-stamp (ATSv2)**: TimeStampToken over hash of encapContentInfo, external content (if detached), certificates, crls, and all SignerInfo including signed and unsigned attributes. Several instances allowed.
- **ats-hash-index**: Unsigned attribute of the archive-time-stamp-v3. Contains hash indices of certificates, crls, and unsigned attributes.
- **archive-time-stamp-v3 (ATSv3)**: TimeStampToken over concatenation of eContentType, hash of signed data, version/sid/digestAlgorithm/signedAttrs/signatureAlgorithm/signature from SignerInfo, and ATSHashIndex. Required for new archive time-stamps.

### Long-Term Validation Data (CAdES-LT)
- **long-term-validation**: Unsigned attribute. Contains PoE date, optional PoE (TimeStampToken or EvidenceRecord), extra certificates and revocation objects. Uses tree-hashing for SET elements. Deprecated for new signatures; use ATSv3 instead.

## Other Standard Data Structures (Clause 7)
- X.509 v3 certificates per RFC 3280.
- X.509 v2 CRLs per RFC 3280.
- OCSP responses per RFC 2560.
- TimeStampToken per RFC 3161 and profiled in TS 101 861.
- Names: Distinguished names required for CAs, AAs, TSAs. SubjectAltName may be used for end entities.
- Attribute certificates per RFC 3281.
- Evidence records per RFC 4998.

## Conformance Requirements (Clause 8)
- Signer shall implement CAdES-BES or CAdES-EPES.
- Verifier shall implement verification of CAdES-BES or CAdES-EPES up to CAdES-C (including time-stamp or time-mark, complete references, certificates, CRLs/OCSP). Extended and archive forms are optional.
- Verification with time-stamping: shall support signature-time-stamp, complete-certificate-references, complete-revocation-references, PKCs, either CRLs or OCSP.
- Verification using secure records: same but with secure audit trail for time-mark.
- Optional attributes: inclusion supported only to the extent that signature is verifiable; semantics may be unsupported unless specified by signature policy.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CAdES-BES shall include content-type, message-digest, and one of signing-certificate or signing-certificate-v2. | shall | 5.7, 8.1 |
| R2 | For CAdES-EPES, signature-policy-identifier shall be present as signed attribute. | shall | 5.8, 8.2 |
| R3 | The signedAttrs field of SignerInfo shall contain the mandatory attributes. | shall | 5.6 |
| R4 | The signing certificate shall be identified in the sequence; certificate hash must match used certificate. | shall | 5.7.3 |
| R5 | For CAdES-T, a signature-time-stamp or time-mark must be associated. | shall | 4.4.1, 6.1 |
| R6 | For CAdES-C, complete-certificate-references and complete-revocation-references shall be present. | shall | 6.2 |
| R7 | Only one instance of complete-certificate-references and complete-revocation-references per signature. | shall | 6.2.1, 6.2.2 |
| R8 | For CAdES-A, systems claiming conformance shall generate archive time-stamps using ATSv3. | shall | 4.4.4 |
| R9 | The archive-time-stamp-v3 shall include ats-hash-index as an unsigned attribute. | shall | 6.4.3 |
| R10 | The ats-hash-index shall be the only attribute of that type in the archive-time-stamp-v3. | shall | 6.4.2 |
| R11 | For CAdES-LT, use is deprecated unless already present; once added, only other long-term-validation attributes may be added. | shall (deprecated) | 6.5.1 |
| R12 | Implementations shall support signing-certificate and signing-certificate-v2 in timestamp tokens. | shall | 7.4 |
| R13 | Verifier shall support verification of CAdES-BES or CAdES-EPES and at least one of CRL or OCSP. | shall | 8.3, 8.4 |
| R14 | Degenerate case with no signers is not valid. | shall | 5.4 |

## Informative Annexes (Condensed)
- **Annex A (normative)**: ASN.1 definitions for all new syntax (X.208 and X.680 modules). Provides complete definitions for attributes, signature policy, archive time-stamps, long-term validation, etc.
- **Annex B (informative)**: Illustrates extended forms (CAdES-X Long, Type 1, Type 2, Archive, Long-Term) with required attributes and example validation sequences.
- **Annex C (informative)**: Rationale for components: signature policy, commitment type, certificate identification, roles, location, signing time, content format, validation data (CRLs, OCSP, certification paths, time-stamping, archive, mutual recognition, TSA compromise). Explains use of grace periods.
- **Annex D (informative)**: Operational and management protocols for TSPs: certificate retrieval (LDAP), CRL retrieval (LDAP), OCSP, time-stamping (RFC 3161), revocation request (RFC 4210).
- **Annex E (informative)**: Security considerations: private key protection, algorithm modularity to accommodate weakening.
- **Annex F (informative)**: Use of MIME and S/MIME structures for encoding signed data (application/pkcs7-mime and multipart/signed).
- **Annex G (informative)**: Relationship to EU Directive 1999/93/EC and EESSI; explains how CAdES meets advanced and qualified electronic signature requirements.
- **Annex H (informative)**: APIs for generation/verification (IDUP-GSS-API, CORBA Security). Includes token framing with OID id-etsi-es-IDUP-Mechanism-v1.
- **Annex I (informative)**: Cryptographic algorithms (SHA-1, DSA, RSA, general references to ISO/IEC and ANSI standards).
- **Annex J (informative)**: Guidance on naming – allocation, access to registration information, naming schemes for individuals and employees.
- **Annex K (informative)**: Time-stamp hash calculation – tables identifying ASN.1 components used in message imprint for various time-stamp types.
- **Annex L (informative)**: Changes from previous versions (up to V2.2.1).
- **Annex M (informative)**: Bibliography (additional references).