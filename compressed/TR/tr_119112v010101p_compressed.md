# ETSI TR 119 112 V1.1.1: Electronic Signatures and Infrastructures (ESI); Most significant differences between AdES/ASiC ENs and previous TSs
**Source**: ETSI | **Version**: V1.1.1 | **Date**: April 2019 | **Type**: Informative Technical Report
**Original**: Published by ETSI, available at https://www.etsi.org/deliver/etsi_tr/119100_119199/119112/01.01.01_60/tr_119112v010101p.pdf

## Scope (Summary)
The present document summarizes the most relevant differences between:
- CAdES signatures in EN 319 122-1/-2 vs. previous TS 101 733 and TS 103 173,
- PAdES signatures in EN 319 142-1/-2 vs. previous TS 102 778 parts and TS 103 172,
- XAdES signatures in EN 319 132-1/-2 vs. previous TS 101 903 and TS 103 171,
- ASiC containers in EN 319 162-1/-2 vs. previous TS 102 918 and TS 103 174.

## References
### Normative References
Normative references are not applicable in the present document.

### Informative References (Key references cited in text)
- [i.1] ETSI EN 319 132-1 (V1.1.1): XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures
- [i.2] ETSI EN 319 122-1 (V1.1.1): CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures
- [i.3] ETSI TS 101 733 (V2.2.1): CMS Advanced Electronic Signatures (CAdES)
- [i.4] ETSI TS 103 173 (V2.2.1): CAdES Baseline Profile
- [i.5] ETSI EN 319 132-2 (V1.1.1): XAdES digital signatures; Part 2: Extended XAdES signatures
- [i.6] ETSI TS 101 903 (V1.4.2): XML Advanced Electronic Signatures (XAdES)
- [i.7] ETSI TS 103 171 (V2.1.1): XAdES Baseline Profile
- [i.8] ETSI EN 319 142-1 (V1.1.1): PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures
- [i.9] ETSI EN 319 142-2 (V1.1.1): PAdES digital signatures; Part 2: Additional PAdES signatures profiles
- [i.10] to [i.15] ETSI TS 102 778 parts (V1.1.1 to V1.1.2): PDF Advanced Electronic Signature Profiles
- [i.16] ETSI TS 103 172 (V2.2.2): PAdES Baseline Profile
- [i.17] ETSI EN 319 162-1 (V1.1.1): Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers
- [i.18] ETSI EN 319 162-2 (V1.1.1): Associated Signature Containers (ASiC); Part 2: Additional ASiC containers
- [i.19] ETSI TS 102 918 (V1.3.1): Associated Signature Containers (ASiC)
- [i.20] ETSI TS 103 174 (V2.2.1): ASiC Baseline Profile
- [i.21] ISO 32000-1: Document management – Portable document format – Part 1: PDF 1.7
- [i.22] IETF RFC 4998: Evidence Record Syntax (ERS)
- [i.23] IETF RFC 6283: Extensible Markup Language Evidence Record Syntax (XMLERS)
- [i.24] IETF RFC 5652: Cryptographic Message Syntax (CMS)
- [i.25] IETF RFC 5035: Enhanced Security Services (ESS) Update: Adding CertID Algorithm Agility
- [i.26] ETSI EN 319 122-2: Extended CAdES signatures
- [i.27] Commission Implementing Decision (EU) 2015/1506
- [i.28] W3C Recommendation: XML Signature Syntax and Processing Version 1.1

## Definitions and Abbreviations
- Terms: For the purposes of the present document, the terms given in ETSI EN 319 122-1 [i.2], ETSI EN 319 132-1 [i.1] and ETSI EN 319 162-1 [i.17] apply.
- Symbols: Void.
- Abbreviations: For the purposes of the present document, the abbreviations given in ETSI EN 319 122-1 [i.2], ETSI EN 319 132-1 [i.1] and ETSI EN 319 162-1 [i.17] apply.

## 4 Main differences for CAdES digital signatures

### 4.1 Introduction
Compared to ETSI TS 101 733 [i.3] and TS 103 173 [i.4], EN 319 122-1 [i.2] and EN 319 122-2 [i.26] implemented:
1. New attributes substituting previously defined ones
2. New attributes with new semantics
3. Clarification of attribute semantics
4. Deprecation of attributes
5. Two new sets of signature levels: baseline (EN 319 122-1) and extended (EN 319 122-2)
6. Redistribution of material

### 4.2 New attributes substituting previously defined ones
Table 1 (condensed):
| New attribute (EN 319 122-1) | Replaces (TS 101 733) | Reason |
|---|---|---|
| signer-attributes-v2 | signer-attributes | Add signed assertions and any attribute certificate format |
| signature-policy-store | (none) | Allow full signature policy document for self-contained longevity |
| ats-hash-index-v3 | ats-hash-index | Allow addition of values after time-stamping by archive-time-stamp-v3 |
| SigPolicyQualifierInfo in signature-policy-identifier | SigPolicyQualifierInfo in signature-policy-identifier | Add third qualifier: technical specification identifier |

**Note**: These attributes are not part of signature formats mentioned in EU Commission Decision 2015/1506 [i.27].

### 4.3 Clarification of attributes semantics
Semantics clarified for: certificate-values, revocation-values, complete-certificate-references, complete-revocation-references, attribute-certificate-references, attribute-revocation-references (see Annex A.1 of EN 319 122-1). Additionally, EN 319 122-1 and -2 clearly state that `IssuerSerial` in `ESS signing-certificate-v2` is only a hint; the digest is the binding. This was not stated in previous TSs.

**Note**: These attributes are not part of signature formats mentioned in EU Commission Decision 2015/1506 [i.27].

### 4.4 Deprecated attributes
Deprecated by EN 319 122-1: `other-signing-certificate`, `signer-attributes`, `archive-time-stamp` (ATSv2), `long-term-validation`, `ats-hash-index`, `time-mark`.

**Note**: These attributes are not part of signature formats mentioned in EU Commission Decision 2015/1506 [i.27].

### 4.5 Two new sets of levels
- CAdES is now a trademark for CMS-based signatures with attributes from EN 319 122-1.
- EN 319 122-1 defines baseline levels: CAdES-B-B, -T, -LT, -LTA (replacing TS 103 173 levels).
- EN 319 122-2 defines extended levels: CAdES-E-B, -EPES, -C, -X, -X-Long, -X-L, -A (replacing TS 101 733 levels).
- CAdES-LTA-Level and extended levels are not mentioned in EU Decision 2015/1506 [i.27].

Correspondence tables (Table 4 and 5) preserved in original.

## 5 Main differences for XAdES digital signatures

### 5.1 Introduction
Namespaces (Table 6) preserved. Compared to TS 101 903 [i.6] and TS 103 171 [i.7], EN 319 132-1 [i.1] and EN 319 132-2 [i.5] implemented:
1. New qualifying properties substituting previously defined ones (due to deprecation of `ds:X509IssuerSerial`)
2. New qualifying properties with new semantics
3. Clarification of semantics
4. Two new sets of signature levels
5. Redistribution of material

### 5.2 New qualifying properties substituting previously defined ones
Table 7: New properties replacing TS 101 903 properties due to `ds:X509IssuerSerial` deprecation:
- `xades:SigningCertificateV2` replaces `xades:SigningCertificate`
- `xadesv141:CompleteCertificateRefsV2` replaces `xades:CompleteCertificateRefs`
- `xadesv141:AttributeCertificateRefsV2` replaces `xades:AttributeCertificateRefs`
- `xadesv141:SigAndRefsTimeStampV2` replaces `xades:SigAndRefsTimeStamp`
- `xadesv141:RefsOnlyTimeStampV2` replaces `xades:RefsOnlyTimeStamp`
- `xades:SignatureProductionPlaceV2` replaces `xades:SignatureProductionPlace`

These properties replace `ds:X509IssuerSerial` with `xades:IssuerSerialV2` (base-64 DER-encoded). EN 319 132-1 clearly states this is only a hint; the digest is the binding. This was not stated in previous TSs.

Table 8: Additional new properties:
- `xades:SignatureProductionPlaceV2`: adds street address
- `xades:SignerRoleV2`: replaces `xades:SignerRole`; adds signed assertions and any attribute certificate format
- `xadesv141:SignaturePolicyStore`: new, allows full document
- `xadesv141:RenewedDigests`: new, for countering digest break risk by using different algorithm

### 5.3 Clarification of qualifying properties semantics
Semantics clarified for: `xades:CertificateValues`, `RevocationValues`, `AttrAuthoritiesCertValues`, `AttributeRevocationValues`, `CompleteRevocationRefs`, `AttributeRevocationRefs`.

### 5.4 Two new sets of levels
- XAdES is now a trademark for XML signatures with properties from EN 319 132-1.
- EN 319 132-1 defines baseline levels: XAdES-B-B, -T, -LT, -LTA (replacing TS 103 171 levels).
- EN 319 132-2 defines extended levels: XAdES-E-B, -EPES, -C, -X, -X-Long, -X-L, -A (replacing TS 101 903 levels).
- Correspondence tables (Table 10 and 11) preserved in original.

## 6 Main differences for PAdES digital signatures

### 6.1 Introduction
Compared to TS 102 778 [i.10] to [i.15] and TS 103 172 [i.16], EN 319 142-1 [i.8] and EN 319 142-2 [i.9] implemented:
1. New attributes substituting previously defined ones
2. Clarification of attributes usage and encoding
3. Deprecation of attributes
4. Two new sets of signature levels
5. Redistribution of material (TS 102 778-1 and -6 contents not included in the ENs)

### 6.2 New attributes substituting previously defined ones
Table 12: New attribute `signer-attributes-v2` (replaces `signer-attributes` from TS 101 733) – adds signed assertions and any attribute certificate format.

### 6.3 Clarification of attributes usage and encoding
Semantics clarified for: `Filter`, `Location`, `Name`, `ContactInfo`, `Reason`, `commitment-type-indication`, and DSS/VRI dictionary entries (`Certs`, `OCSPs`, `CRLs`, `Cert`, `CRL`, `OCSP`).

### 6.4 Deprecated attributes
Deprecated by EN 319 142-1: `signer-attributes`, `time-mark`.

### 6.5 Two new sets of levels
- PAdES is now a trademark for PDF signatures with alternative encoding equivalent to CAdES (EN 319 122-1 attributes).
- EN 319 142-1 defines baseline levels: PAdES-B-B, -T, -LT, -LTA (replacing TS 103 172 levels).
- EN 319 142-2 defines extended levels: CMS Signatures in PDF, PAdES-E-BES, -EPES, -LTV (replacing TS 102 778 levels).
- PAdES-LTA-Level and extended levels are not mentioned in EU Decision 2015/1506 [i.27].

## 7 Main differences for ASiC containers

### 7.1 Introduction
Compared to TS 102 918 [i.19] and TS 103 174 [i.20], EN 319 162-1 [i.17] and EN 319 162-2 [i.18] implemented:
1. Updated references to CAdES ENs (instead of TS 101 733) and XAdES ENs (instead of TS 101 903)
2. Two new sets of container levels
3. Reduction of baseline container types from 6 to 3 (the other 3 moved to additional profiles)
4. Support of IETF RFC 4998 [i.22] and RFC 6283 [i.23] evidence records
5. New ASiC Manifest files for long term availability
6. Clarification of text to eliminate ambiguities

### 7.2 Two new sets of container levels
- EN 319 162-1 defines baseline containers (ASiC-S and ASiC-E with various signature levels) – correspond to TS 103 174 levels (Table 17).
- EN 319 162-2 defines additional containers – correspond to TS 102 918 levels (Table 18).
- TS 103 174 is referenced by EU Commission Decision 2015/1506 [i.27].

### 7.3 Evidence records
- Building blocks use "Time Assertion" to encompass both time stamp tokens and evidence records (RFC 4998/6283).
- Evidence records supported in ASiC manifest files.
- EN 319 162-2 extends baseline profiles with time stamp tokens to include evidence records.

### 7.4 New ASiC Manifest files for long term availability
- `ASiCArchiveManifest` protects long term time stamp tokens.
- `ASiCEvidenceRecordManifest` references files for evidence records, enabling LTA equivalent for containers with time assertions.

## Informative Annexes (Condensed)
The present document does not contain separate annexes. All differences are provided in the main clauses above. The original document includes a history table (publication date V1.1.1 April 2019).