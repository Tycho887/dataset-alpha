# ETSI TS 102 904: Profiles of XML Advanced Electronic Signatures based on TS 101 903 (XAdES)
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2007-02 | **Type**: Normative
**Original**: Full text of ETSI TS 102 904 V1.1.1

## Scope (Summary)
Defines three profiles of XAdES (TS 101 903) signatures to maximise interoperability: e-Invoicing, e-Government, and a baseline for other areas. Profiles specify requirements for generators and verifiers. Optional elements not specified remain optional.

## Normative References
- [1] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)".
- [2] W3C-IETF: "XML-Signature Syntax and Processing", Feb. 2002.
- [3] ITU-T X.509 / ISO/IEC 9594-8.
- [4] IETF RFC 3280: "Internet X.509 PKI Certificate and CRL Profile".
- [5] CEN Workshop Agreement 15579 (2006) – e-invoices and digital signatures.
- [6] IETF RFC 2560: "Online Certificate Status Protocol - OCSP".
- [7] ETSI TS 102 176-1: "Algorithms and Parameters for Secure Electronic Signatures; Part 1".
- [8] CEN Workshop Agreement 14171 (2004): "General guidelines for electronic signature verification".

## Definitions and Abbreviations
- **generator**: party that creates or adds attributes to a signature (may be signatory or maintainer).
- **long term signatures**: signatures expected to be verified beyond signer's cert expiration.
- **protocol element**: element of protocol that may include data and/or procedure elements.
- **service element**: element of service provided using one or more protocol elements.
- **short term signatures**: signatures verified within signer's certificate validity period.
- **verifier**: entity that validates or verifies an electronic signature.
- **may**: permissible within limits of the document.
- **shall**: absolute requirement.
- **should**: recommended, but alternatives possible with understanding.
- **CA**: Certification Authority
- **CRL**: Certificate Revocation List
- **OCSP**: Online Certificate Status Protocol
- **TSP**: Trusted Service Provider
- **TST**: Time-Stamp Token
- **XAdES**: XML Advanced Electronic Signatures
- **XML SIG**: XML Digital Signature

## General Requirements

### 4.1 Algorithm Requirements
Implementers **should** take into account TS 102 176‑1 [7] for algorithm and key length selection.

### 4.2 Compliance Requirements
Profiles define requirements for generator and verifier using categories (Table 1):

| Identifier | Generator | Verifier |
|------------|-----------|----------|
| M (Mandatory) | **shall** include | **shall** process |
| R (Recommended) | **should** include | **shall** process if present |
| O (Optional) | **may** include | **may** process or ignore |

For services with multiple protocol element choices, Tables 2–4 define combined semantics (M/R/O for service + R/O for protocol element). Systems claiming a profile **shall** comply with applicable clauses (e.g., clause 5.1–5.3, 5.5 for e-Invoicing; additionally 5.4 for long term). Optional elements not specified are treated as O. Profiles may be affected by national regulations.

## 5 XAdES Profile for e-Invoicing

### 5.1 Elements defined in XML SIG

#### 5.1.1 Placement of the signature
| Service/Protocol | Ref | Generator | Verifier | Notes |
|-----------------|----|-----------|----------|-------|
| Service: signature | – | M | M | |
| Enveloping Signature | [2] clause 10.0 | O | R | |
| Enveloped Signature | [2] clause 10.0 | O | R | |
| Detached Signature | [2] clause 10.0 | O | R | |

### 5.2 Profile of elements in Basic XAdES form (XAdES-BES)

#### 5.2.1 ds:KeyInfo and xades:SigningCertificate
Service: Identifying signer and validation key and securing the signing certificate – M on both.
- **ds:KeyInfo/X509Data/X509Certificate** present AND signed by signature: Generator R, Verifier R.
- **xades:SigningCertificate** present: Generator O, Verifier R.  
  *Additional requirement a)*: Verifier **must** check signing certificate matches that referenced in `xades:SigningCertificate` per XAdES.

#### 5.2.2 Signing Time
- `xades:SigningTime`: Generator O, Verifier O.

#### 5.2.3 Countersignatures
Service: counter signing – Generator O, Verifier O.
- `ds:Reference` Type profiled to `http://uri.etsi.org/01903#CountersignedSignature`: O/O.
- `xades:CounterSignature`: O/O.  
  *Additional requirement a)*: Use **should** be agreed upon beforehand between generator and verifier.

### 5.3 Additional attributes defined in XAdES

#### 5.3.1 Signature time-stamp / time-mark
Service: Trusted signing time – Generator R, Verifier R.
- `xades:SignatureTimeStamp`: Generator R, Verifier R.
- Time-mark (clause 4.4.3.1): Generator O, Verifier O.  
  Note: Helps distinguish valid/invalid signatures if signer cert revoked.

### 5.4 Additional attributes defined in XAdES for long term signatures
Only applicable to systems managing long term signatures.

#### 5.4.1 Certificate references
- `xades:CompleteCertificateReferences`: Generator R, Verifier R.

#### 5.4.2 Revocation status references
Service: complete revocation status references – Generator R, Verifier R.
- `xades:CompleteRevocationReferences/CRLRefs`: Generator O, Verifier R.
- `xades:CompleteRevocationReferences/OCSPRefs`: Generator O, Verifier R.  
  Note 1: Generator recommended to use CRLs or OCSP; verifier should handle both.  
  Note 2: Should wait until end of grace period before generating.  
  *Add req a)*: Revocation status information **shall** encompass time of signing.

#### 5.4.3 Certificate values
Service: certificate values – Generator R, Verifier R.
- `xades:CertificateValues`: Generator O, Verifier O.
- Certificates maintained by CA or other trusted service: O/O.  
  *Add req a)*: If CA/trusted service is trusted to keep revocation info for archiving period, no need to hold within signature (prior agreement needed).

#### 5.4.4 Revocation status values
Service: revocation status values – Generator R, Verifier R.
- `xades:CertificateValues/CRLValues`: Generator O, Verifier O.
- `xades:CertificateValues/OCSPValues`: Generator O, Verifier O.
- Revocation status values maintained by CA or other trusted service: O/O.  
  *Add req a)*: Verifier **should** process both CRL and OCSP regardless of source.  
  *Add req b)*: Same as certificate values a) regarding trusted service.

#### 5.4.5 Archive time-stamp
- `xades:ArchiveTimeStamp`: Generator O, Verifier O.  
  *Add req a)*: Verifier requirement becomes R if no alternative technical/organisational mechanisms to maintain validity over storage period.

### 5.5 Other standards

#### 5.5.1 X.509 Certificates
- X.509 Certificate Profile per RFC 3280 [4]: Generator M, Verifier M.  
  Notes: ETSI has TS 101 862 and TS 102 280.

#### 5.5.2 Certificate key usage for e-Invoicing
- Certificate extended key usage `id-kp-eInvoicing` (non-critical): Generator R, Verifier O. Ref: CWA 15579 [5] clause 5.7.2.

#### 5.5.3 Naming
- Certificate Subject.Organization: Generator R, Verifier R. (Organization issuing invoice.)
- Certificate Subject.CommonName: Generator R, Verifier O. (If signed by human, should identify person; if system, should identify system via domain name.)
- Certificate Subject.OrganizationalUnit: Generator O, Verifier O. (Should identify department if multiple departments issue invoices.)

## 6 XAdES Profile for e-Government

### 6.1 Elements defined in XML SIG (same as 5.1.1)
Table 21 identical to Table 6.

### 6.2 Profile of elements in Basic XAdES form

#### 6.2.1 ds:KeyInfo and xades:SigningCertificate (identical to 5.2.1)
Table 22 same as Table 7.

#### 6.2.2 Signing Time (identical to 5.2.2)
Table 23 same as Table 8.

#### 6.2.3 Countersignatures
Service: counter signing – Generator O, Verifier R (different from e-Invoicing where Verifier O).  
- `ds:Reference` Type: O/R.  
- `xades:CounterSignature`: O/R.  
  Additional requirement a) same as before.

### 6.3 Additional attributes defined in XAdES

#### 6.3.1 Signature time-stamp / time-mark
Service: Trusted signing time – Generator R, Verifier R.
- `xades:SignatureTimeStamp`: Generator O, Verifier R. (e-Invoicing had R/R)
- Time-mark: Generator O, Verifier O.  
  Note: Governmental agencies may act as trusted storage providers, eliminating need for TST.

### 6.4 Additional attributes defined in XAdES for long term signatures
Same structure as 5.4, identical tables (26–30) with same requirements:  
- Certificate references: R/R  
- Revocation status references: R/R (choices O/R)  
- Certificate values: R/R (choices O/O)  
- Revocation status values: R/R (choices O/O)  
- Archive time-stamp: O/O (verifier becomes R if no alternative)  
All notes and additional requirements identical.

### 6.5 Other standards

#### 6.5.1 X.509 Certificates (identical to 5.5.1)
Table 31 same as Table 16.

## 7 XAdES Baseline Profile

### 7.1 Elements defined in XML SIG (identical to 5.1.1)
Table 32 same as Table 6.

### 7.2 Profile of elements in Basic XAdES form

#### 7.2.1 ds:KeyInfo and xades:SigningCertificate (identical to 5.2.1)
Table 33 same as Table 7.

#### 7.2.2 Signing Time (identical)
Table 34 same.

#### 7.2.3 Countersignatures (same as 5.2.3: O/O)
Table 35 same as Table 9.

### 7.3 Additional attributes defined in XAdES

#### 7.3.1 Signature time-stamp / time-mark
- `xades:SignatureTimeStamp`: Generator O, Verifier O (different from R/R in other profiles).  
  Note same as before.

### 7.4 Additional attributes defined in XAdES for long term signatures
Identical structure to 5.4 (Tables 37–41) with same requirements:  
- Certificate references: R/R  
- Revocation status references: R/R (choices O/R)  
- Certificate values: R/R (choices O/O)  
- Revocation status values: R/R (choices O/O)  
- Archive time-stamp: O/O (verifier becomes R if no alternative)  
All notes and additional requirements identical.

### 7.5 Other standards
Note: Generators and verifiers recommended to support CRLs for interoperability.

#### 7.5.1 X.509 Certificates (identical)
Table 42 same as Table 16.

## Requirements Summary
Due to the volume of requirements, a full summary table is omitted here; each requirement is captured in the tables above with normative language preserved.

## Informative Annexes (Condensed)
- **Annex A (Bibliography)**: Lists ETSI TS 101 862 (Qualified certificate profile) and ETSI TS 102 280 (Certificate profile for natural persons) as additional references.