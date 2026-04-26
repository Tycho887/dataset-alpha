# ETSI TS 101 903 V1.4.2: XML Advanced Electronic Signatures (XAdES)
**Source**: ETSI | **Version**: V1.4.2 | **Date**: 2010-12 | **Type**: Normative
**Original**: ETSI TS 101 903 V1.4.2 (2010-12)

## Scope (Summary)
Defines XML formats for advanced electronic signatures that remain valid over long periods, are compliant with the European Directive, and incorporate additional useful information (e.g., time-stamps, signature policies, validation data). Builds on XMLDSIG and uses time-stamps or trusted records for long-term validity and non-repudiation.

## Normative References
- [1] ETSI TS 101 733 (CAdES)
- [2] IETF RFC 3852 (CMS)
- [3] W3C Recommendation: XML-Signature Syntax and Processing
- [4] W3C XML Schema Part 1: Structures
- [5] W3C XML Schema Part 2: Datatypes
- [6] ITU-T X.509
- [7] W3C XML 1.0
- [8] IETF RFC 2560 (OCSP)
- [9] IETF RFC 2119 (key words)
- [10] IETF RFC 3161 (TSP)
- [11] IETF RFC 5280 (PKIX)
- [12] ETSI TS 101 903 V1.3.2 (earlier XAdES)

## Definitions and Abbreviations
- **Signer**: entity that creates the electronic signature.
- **Verifier**: entity that verifies the electronic signature.
- **Trusted Service Provider (TSP)**: entity that helps build trust (e.g., CA, TSA, CRL issuer).
- **Signature Policy**: set of rules for creation/validation of an electronic signature.
- **XAdES-BES**: Basic Electronic Signature.
- **XAdES-EPES**: Explicit Policy based Electronic Signature.
- **XAdES-T**: with Time-stamp.
- **XAdES-C**: Complete validation data references.
- **XAdES-X**: eXtended validation data.
- **XAdES-X-L**: eXtended long.
- **XAdES-A**: Archival.
- **TSA**: Time-Stamping Authority.

## Overview (Clause 4)
### Major Parties
Signer, Verifier, TSPs, Arbitrator.

### Signature Policy
May be explicitly identified or implied. Policy ensures consistency of validation.

### Signature Properties
- **SignedProperties**: SignedSignatureProperties (SigningTime, SigningCertificate, SignaturePolicyIdentifier, SignatureProductionPlace, SignerRole) and SignedDataObjectProperties (DataObjectFormat, CommitmentTypeIndication, AllDataObjectsTimeStamp, IndividualDataObjectsTimeStamp).
- **UnsignedProperties**: UnsignedSignatureProperties (CounterSignature, SignatureTimeStamp, CompleteCertificateRefs, CompleteRevocationRefs, SigAndRefsTimeStamp, RefsOnlyTimeStamp, CertificateValues, RevocationValues, ArchiveTimeStamp, etc.) and UnsignedDataObjectProperties.

### Signature Forms
- **XAdES-BES**: Minimum format. MUST include either SigningCertificate signed property OR ds:KeyInfo with signing certificate referenced. MAY include other signed/unsigned properties.
- **XAdES-EPES**: Extends XAdES-BES with SignaturePolicyIdentifier signed property.
- **XAdES-T**: Adds SignatureTimeStamp (or time-mark) for trusted time.
- **XAdES-C**: Adds CompleteCertificateRefs and CompleteRevocationRefs (and attribute refs if present).
- **Extended forms**: XAdES-X, XAdES-X-L, XAdES-A (see Annex B).

## Syntax Overview (Clause 6)
### QualifyingProperties Element
Container for all qualifying properties. Target attribute MUST reference the ds:Signature Id. SignedProperties MUST be covered by a ds:Reference with Type="http://uri.etsi.org/01903#SignedProperties".

### Incorporating Properties
- Direct: QualifyingProperties inside ds:Object.
- Indirect: QualifyingPropertiesReference element referencing an external QualifyingProperties.

## Qualifying Properties Syntax (Clause 7)
### Auxiliary Types
- **AnyType**, **ObjectIdentifierType**, **EncapsulatedPKIDataType** (base-64 encoded PKI data).
- **GenericTimeStampType** (abstract), **XAdESTimeStampType** (for XAdES signatures), **OtherTimeStampType** (for external data). Include mechanism for explicit identification.

### Signed Properties (Clause 7.2)
- **SigningTime**: xsd:dateTime. At most one SHALL appear.
- **SigningCertificate**: CertIDList with CertDigest and IssuerSerial. Must reference signing certificate; SHA-256 etc.
- **SignaturePolicyIdentifier**: either SignaturePolicyId (with SigPolicyId, SigPolicyHash, optional Transforms/Qualifiers) or SignaturePolicyImplied.
- **CounterSignature**: ds:Signature referencing the ds:SignatureValue of the embedding signature. Unsigned.
- **DataObjectFormat**: required ObjectReference to ds:Reference. At least one of Description, ObjectIdentifier, MimeType.
- **CommitmentTypeIndication**: CommitmentTypeId, ObjectReference/AllSignedDataObjects, optional qualifiers.
- **SignatureProductionPlace**: city, state, etc. At most one.
- **SignerRole**: ClaimedRoles (AnyType) and/or CertifiedRoles (EncapsulatedPKIDataType).
- **AllDataObjectsTimeStamp**: implicit; covers all ds:Reference elements except SignedProperties.
- **IndividualDataObjectsTimeStamp**: explicit Include mechanism for selected references.

### SignatureTimeStamp (Clause 7.3)
Unsigned; covers ds:SignatureValue. Implicit mechanism. At most one? Actually MAY appear multiple times.

### Validation Data References (Clause 7.4)
- **CompleteCertificateRefs**: CertIDList of CA certs. At most one, SHALL NOT be empty.
- **CompleteRevocationRefs**: CRLRefs, OCSPRefs, OtherRefs. At most one.
- **AttributeCertificateRefs**, **AttributeRevocationRefs**: similar for attribute certs.

### Time-stamps on References (Clause 7.5)
- **SigAndRefsTimeStamp**: covers ds:SignatureValue, SignatureTimeStamp, CompleteCertificateRefs, CompleteRevocationRefs (and attribute refs). Implicit if same parent, else explicit.
- **RefsOnlyTimeStamp**: covers only refs.

### Validation Data Values (Clause 7.6)
- **CertificateValues**: EncapsulatedX509Certificate or OtherCertificate.
- **RevocationValues**: CRLValues, OCSPValues, OtherValues.
- **AttrAuthoritiesCertValues**, **AttributeRevocationValues**: for attribute certs.

### ArchiveTimeStamp (Clause 7.7)
Deprecated; replaced by xadesv141:ArchiveTimeStamp. SHALL NOT be generated.

## New Unsigned Properties (Clause 8 – XAdESv1.4.1)
Namespace: `http://uri.etsi.org/01903/v1.4.1#`

### xadesv141:TimeStampValidationData
Optional container for validation data for time-stamp tokens. Contains CertificateValues and RevocationValues. URI attribute MAY reference the time-stamp container.

### xadesv141:ArchiveTimeStamp
Replaces old ArchiveTimeStamp. Covers signed refs, ds:SignedInfo, ds:SignatureValue, ds:KeyInfo, unsigned properties, and other ds:Object elements. Implicit or explicit. Must include CertificateValues and RevocationValues if not already present.

## Conformance Requirements (Clause 9)
### 9.1 XAdES-BES
A system supporting signers SHALL support generation of ds:Signature as per XMLDSIG and at least one of: SigningCertificate signed property OR ds:KeyInfo with signing certificate and referencing it.

### 9.2 XAdES-EPES
Additionally SHALL support SignaturePolicyIdentifier signed property.

### 9.3 Verification Using Time-stamping
SHALL support verification of XAdES-BES, SignatureTimeStamp, CompleteCertificateRefs, CompleteRevocationRefs, X.509 PKCs, and either CRLs or OCSP.

### 9.4 Verification Using Secure Records
SHALL support verification of XAdES-BES, CompleteCertificateRefs, CompleteRevocationRefs, maintaining an undetectable record of signature and first validation time, plus PKCs and CRLs/OCSP.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | XAdES-BES SHALL include either SigningCertificate or ds:KeyInfo with signing certificate signed | SHALL | 9.1, 4.4.1 |
| R2 | SigningCertificate SHALL contain CertDigest and IssuerSerial | SHALL | 7.2.2 |
| R3 | SignaturePolicyIdentifier SHALL be present in XAdES-EPES | SHALL | 9.2, 4.4.2 |
| R4 | SignatureTimeStamp unsigned property SHALL cover ds:SignatureValue | SHALL | 7.3 |
| R5 | CompleteCertificateRefs SHALL reference CA certificates used | SHALL | 7.4.1 |
| R6 | CompleteRevocationRefs SHALL reference revocation data used | SHALL | 7.4.2 |
| R7 | xadesv141:ArchiveTimeStamp SHALL cover signature and validation data | SHALL | 8.2 |
| R8 | Old ArchiveTimeStamp SHALL NOT be generated | SHALL | 7.7 |
| R9 | SignedProperties MUST be referenced by a ds:Reference with Type attribute | MUST | 6.3.1 |
| R10 | QualifyingProperties Target attribute MUST refer to ds:Signature Id | MUST | 6.2 |
| R11 | Verifier SHALL support at least one of CRL or OCSP for verification | SHALL | 9.3, 9.4 |

## Informative Annexes (Condensed)
- **Annex A**: Defines terms (Data Object, Signature, Transform, Attribute Certificate).
- **Annex B**: Describes extended forms: XAdES-X, XAdES-X-L, XAdES-A (archival). XAdES-A includes multiple time-stamps and validation data.
- **Annex C**: Discusses multiple signatures and countersignatures.
- **Annex D**: Normative schema definitions (XAdES.xsd and XAdESv141.xsd) provided in full.
- **Annex E**: Lists changes from V1.4.1: fixed attribute name "UR" to "URI", fixed element name "ArchiveTimeStampV2" to "ArchiveTimeStamp", and fixes from V1.3.2.
- **Annex F**: Examples of direct and indirect incorporation of qualifying properties.
- **Annex G**: Detailed verification procedures for each property, including checks on time-stamp tokens.
- **Annex H**: Versioning rules: namespace kept for backward compatibility; new properties in new namespace.
- **Annex I**: Bibliography of referenced documents.