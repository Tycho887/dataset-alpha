# ETSI TS 102 734 V1.1.1: Electronic Signatures and Infrastructures; Profiles of CMS Advanced Electronic Signatures based on TS 101 733 (CAdES)
**Source**: ETSI | **Version**: V1.1.1 | **Date**: February 2007 | **Type**: Normative (Technical Specification)
**Original**: http://www.etsi.org (PDF version)

## Scope (Summary)
Profiles the use of CAdES (TS 101 733) for CMS‑based advanced electronic signatures in e‑Invoicing, e‑Government, and a baseline for other application areas. Does not repeat base requirements but maximises interoperability by selecting a common set of options.

## Normative References
- [1] ETSI TS 101 733 V1.7.3: "CMS Advanced Electronic Signatures (CAdES)"
- [2] IETF RFC 3852: "Cryptographic Message Syntax (CMS)"
- [3] IETF RFC 2634: "Enhanced Security Services for S/MIME"
- [4] draft-ietf-smime-escertid-01 (Oct 2006): "ESS Update: Adding CertID Algorithm Agility"
- [5] ITU‑T X.509 / ISO/IEC 9594-8
- [6] IETF RFC 3280: "Internet X.509 PKI Certificate and CRL Profile"
- [7] CEN Workshop Agreement 15579 (to be published): "E‑invoices and digital signatures"
- [8] IETF RFC 2560: "X.509 Internet PKI Online Certificate Status Protocol – OCSP"
- [9] ETSI TS 102 176-1 V1.2.1: "Algorithms and Parameters for Secure Electronic Signatures; Part 1: Hash functions and asymmetric algorithms"
- [10] CEN Workshop Agreement 14171 (2004): "General guidelines for electronic signature verification"

## Definitions and Abbreviations
### Definitions
- **generator**: party that creates or adds attributes to a signature (may be signatory or verifier/maintainer).
- **long term signatures**: signatures expected to be verified beyond the signer’s certificate expiration date and possibly beyond the CA’s certificate expiration.
- **protocol element**: element of the protocol that may include data and/or procedural elements.
- **service element**: element of service that may be provided using one or more protocol elements.
- **short term signatures**: signatures verified for a period not extending beyond the signer’s certificate expiration.
- **verifier**: entity that validates or verifies an electronic signature.
- **shall**: absolute requirement.
- **should**: recommended; valid reasons may justify non‑compliance.
- **may**: permissible course of action.

### Abbreviations
CA, CAdES, CEN, CMS, CRL, CWA, ESS, OCSP, TSP, TST.

## General Requirements
### 4.1 Algorithm requirements
Implementers **should** take into account TS 102 176‑1 [9] for algorithm and key length selection.

### 4.2 Compliance requirements
Requirements are defined in three categories (Table 1):

| Identifier | Generator | Verifier |
|------------|-----------|----------|
| **M** | shall include | shall process |
| **R** | should include | shall process if present |
| **O** | may include | may process or ignore |

For services that may be implemented by different protocol elements, the categories follow Tables 2–4 (mandatory/recommended/optional service with choices). The overall compliance statements for each profile are given in clauses 5–7. Optional elements not specified in the present document are treated as **O** for both generator and verifier.

## 5 CAdES Profile for e‑Invoicing
*Systems claiming compliance shall meet requirements of clauses 5.1, 5.2, 5.3, 5.5. Long‑term support additionally requires clause 5.4.*

### 5.1 Elements defined in CMS
| Element | CMS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: signature** | – | M | M | |
| Enveloping with data | 5.2 | R | R | |
| Detached Signature | 5.2 | O | R | |
| **Service: signer identifier** | 5.3 | M | M | |
| issuerAndSerialNumber | 5.3 | R | R | |
| subjectKeyIdentifier | 5.3 | O | O | |
| ContentType | 11.1 | M | M | |
| Message digest | 11.2 | M | M | |
| signing‑time | 11.3 | O | O | |
| counterSignature | 11.4 | O | O | (a) |
| SignerInfos (parallel) | 5.3 | O | O | (a) |

**Additional requirements:**
- (a) Use of countersignatures or parallel signatures **should** be agreed upon beforehand between generator and verifier.

### 5.2 Elements defined in ESS
| Element | ESS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: protection of signing certificate** | – | M | M | |
| ESS signing‑certificate | [3] 5.4 | R | R | (a) |
| ESS signing‑certificate v2 | [4] 3 | O | R | (a) |

- (a) Generators **should** migrate to signing‑certificate v2 due to SHA‑1 lifetime guidance in TS 102 176‑1 [9].

### 5.3 Additional attributes defined in CAdES
| Element | CAdES Ref | Generator | Verifier | Notes |
|---------|-----------|-----------|----------|-------|
| **Service: Trusted signing time** | – | R | R | |
| signature‑time‑stamp | 6.1.1 | R | R | |
| Time‑mark | 4.4 | O | O | |
*NOTE: Signature time‑stamp assists in distinguishing valid/invalid signatures when certificate is revoked.*

### 5.4 Additional attributes (long term)
*Applicable only to systems managing long term signatures. See CWA 14171 [10] for further details.*

#### 5.4.1 Certificate references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| complete‑certificate‑references | 6.2.1 | R | R | |

#### 5.4.2 Revocation status references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: complete revocation status references** | 6.2.2 | R | R | |
| complete‑revocation‑references.crlidss | 6.2.2 | O | R | (a) |
| complete‑revocation‑references.ocspids | 6.2.2 | O | R | (a) |
*NOTE 1: Generator recommended to use this service, verifier shall handle both CRL and OCSP.*  
*NOTE 2: Attribute should be generated after grace period.*  
*NOTE 3: Requires CRLs [5] or OCSP [8].*  
- (a) Revocation status information **shall** encompass the time of signing.

#### 5.4.3 Certificate values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: certificate values** | – | R | R | |
| certificate‑values | 6.3.3 | O | O | |
| Certificates maintained by CA or other trusted service | – | O | O | (a) |
- (a) If CA or trusted service is relied upon to keep certificates, no need to include them; agreement required.

#### 5.4.4 Revocation status values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: revocation status values** | – | R | R | |
| revocation‑values.crlVals | 6.3.4 | O | O | (a) |
| revocation‑Values.ocspVals | 6.3.4 | O | O | (a) |
| Revocation status values maintained by CA/trusted service | – | O | O | (a),(b) |
- (a) Verifier **should** process CRL and OCSP regardless of source.
- (b) If CA/trusted service is trusted, no need to include revocation data; agreement required.

#### 5.4.5 Archive time‑stamp
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| archive‑time‑stamp | 6.4.1 | O | O | (a) |
- (a) Verifier requirement becomes **R** if no alternative technical/organisational mechanisms exist for long‑term validity.

### 5.5 Other standards
#### 5.5.1 X.509 Certificates
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| X.509 Certificate Profile | RFC 3280 [6] | M | M | 1 |
*NOTE 1: ETSI also defines TS 101 862 and TS 102 280.*  
*NOTE 2: RFC 3280 is a profile of X.509 [5].*

#### 5.5.2 Certificate key usage for e‑Invoicing
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| Certificate extended Key Usage id‑kp‑eInvoicing (non‑critical) | CWA [7] 5.7.2 | R | O | *NOTE: Fault in 2006 version – refer to revised CWA.* |

#### 5.5.3 Naming
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| Certificate Subject.Organization | [7] 5.7 | R | R | (a) |
| Certificate Subject.CommonName | [7] 5.7 | R | O | (b),(c) |
| Certificate Subject.OrganizationalUnit | [7] 5.7 | O | O | (d) |
- (a) Subject organization **should** identify the issuing organisation.
- (b) If signed by a human, Subject CommonName **should** identify the physical person.
- (c) If signed by a system, Subject CommonName **should** identify that system (e.g., domain name).
- (d) Where multiple departments issue independently, Subject OrganizationalUnit **should** identify the department.

## 6 CAdES Profile for e‑Government
*Systems claiming compliance shall meet clauses 6.1, 6.2, 6.3, 6.5. Long‑term support additionally requires clause 6.4.*

### 6.1 Elements defined in CMS
| Element | CMS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: signature** | – | M | M | |
| Enveloping with data | 5.2 | R | R | |
| Detached Signature | 5.2 | O | R | |
| **Service: signer identifier** | 5.3 | M | M | |
| issuerAndSerialNumber | 5.3 | R | R | |
| subjectKeyIdentifier | 5.3 | O | O | |
| ContentType | 11.1 | M | M | |
| Message digest | 11.2 | M | M | |
| signing‑time | 11.3 | O | O | |
| counterSignature | 11.4 | O | R | (a) |
| SignerInfos (parallel) | 5.3 | O | R | (a) |
- (a) Same agreement requirement as e‑Invoicing.

### 6.2 Elements defined in ESS
| Element | ESS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: protection of signing certificate** | – | M | M | |
| ESS signing‑certificate | [3] 5.4 | R | R | (a) |
| ESS signing‑certificate v2 | [4] 4 | O | R | (a) |
- (a) Same migration advice as e‑Invoicing.

### 6.3 Additional attributes defined in CAdES
| Element | CAdES Ref | Generator | Verifier | Notes |
|---------|-----------|-----------|----------|-------|
| **Service: Trusted signing time** | – | R | R | |
| signature‑time‑stamp | 6.6.1 | O | R | 1 |
| Time‑mark | 4.4 | O | O | 2 |
*NOTE 1: Signature time‑stamp assists in revocation validation.*  
*NOTE 2: Governmental agencies may act as trusted storage providers, making TST chain unnecessary (time‑mark).*

### 6.4 Additional attributes (long term)
*Applicable only to long‑term signature management.*

#### 6.4.1 Certificate references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| complete‑certificate‑references | 6.2.1 | R | R | |

#### 6.4.2 Revocation status references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: complete revocation status references** | 6.2.2 | R | R | |
| complete‑revocation‑references.crlidss | 6.2.2 | O | R | (a) |
| complete‑revocation‑references.ocspids | 6.2.2 | O | R | (a) |
*(Same notes 1–3 and requirement (a) as e‑Invoicing.)*

#### 6.4.3 Certificate values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: certificate values** | – | R | R | |
| certificate‑values | 6.3.3 | O | O | |
| Certificates maintained by CA/trusted service | – | O | O | (a) |
- (a) Same as e‑Invoicing.

#### 6.4.4 Revocation status values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: revocation status values** | – | R | R | |
| revocation‑values.crlVals | 6.3.4 | O | O | (a) |
| revocation‑Values.ocspVals | 6.3.4 | O | O | (a) |
| Revocation status values maintained by CA/trusted service | – | O | O | (a),(b) |
*(Same notes and requirements as e‑Invoicing.)*

#### 6.4.5 Archive time‑stamp
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| archive‑time‑stamp | 6.4.1 | O | O | (a) |
- (a) Becomes **R** if no alternative mechanisms.

### 6.5 Other standards
#### 6.5.1 X.509 Certificates
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| X.509 Certificate Profile | RFC 3280 [6] | M | M | 1 |
*(Same notes as e‑Invoicing.)*

## 7 CAdES Baseline Profile
*Systems claiming compliance shall meet clauses 7.1, 7.2, 7.3, 7.5. Long‑term support additionally requires clause 7.4.*

### 7.1 Elements defined in CMS
| Element | CMS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: signature** | – | M | M | |
| Enveloping with data | 5.2 | R | R | |
| Detached Signature | 5.2 | O | R | |
| **Service: signer identifier** | 5.3 | M | M | |
| issuerAndSerialNumber | 5.3 | R | R | |
| subjectKeyIdentifier | 5.3 | O | O | |
| ContentType | 11.1 | M | M | |
| Message digest | 11.2 | M | M | |
| signing‑time | 11.3 | O | O | |
| counterSignature | 11.4 | O | O | (a) |
| SignerInfos (parallel) | 5.3 | O | O | (a) |
- (a) Same agreement requirement as previous profiles.

### 7.2 Elements defined in ESS
| Element | ESS Ref | Generator | Verifier | Notes |
|---------|---------|-----------|----------|-------|
| **Service: protection of signing certificate** | – | M | M | |
| ESS signing‑certificate | [3] 5.4 | R | R | (a) |
| ESS signing‑certificate v2 | [4] 4 | O | R | (a) |
- (a) Same migration advice.

### 7.3 Additional attributes defined in CAdES
| Element | CAdES Ref | Generator | Verifier | Notes |
|---------|-----------|-----------|----------|-------|
| signature‑time‑stamp | 6.6.1 | O | O | *NOTE: Assists in revocation case.* |

### 7.4 Additional attributes (long term)
*Applicable only to long‑term signature management.*

#### 7.4.1 Certificate references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| complete‑certificate‑references | 6.2.1 | R | R | |

#### 7.4.2 Revocation status references
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: complete revocation status references** | 6.2.2 | R | R | |
| complete‑revocation‑references.crlidss | 6.2.2 | O | R | (a) |
| complete‑revocation‑references.ocspids | 6.2.2 | O | R | (a) |
*(Same notes 1–3 and requirement (a) as previous profiles.)*

#### 7.4.3 Certificate values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: certificate values** | – | R | R | |
| certificate‑values | 6.3.3 | O | O | |
| Certificates maintained by CA/trusted service | – | O | O | (a) |
- (a) Same as e‑Invoicing.

#### 7.4.4 Revocation status values
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| **Service: revocation status values** | – | R | R | |
| revocation‑values.crlVals | 6.3.4 | O | O | (a) |
| revocation‑Values.ocspVals | 6.3.4 | O | O | (a) |
| Revocation status values maintained by CA/trusted service | – | O | O | (a),(b) |
*(Same notes and requirements as e‑Invoicing.)*

#### 7.4.5 Archive time‑stamp
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| archive‑time‑stamp | 6.4.1 | O | O | (a) |
- (a) Becomes **R** if no alternative mechanisms.

### 7.5 Other standards
#### 7.5.1 X.509 Certificates
| Element | Ref | Generator | Verifier | Notes |
|---------|-----|-----------|----------|-------|
| X.509 Certificate Profile | RFC 3280 [6] | M | M | 1 |
*(Same notes as e‑Invoicing.)*

## Requirements Summary
The following table summarises the compliance categories used throughout the document. Detailed requirements are given in the tables above.

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| M | Generator **shall** include; Verifier **shall** process | shall | All clauses |
| R | Generator **should** include; Verifier **shall** process if present | should | All clauses |
| O | Generator **may** include; Verifier **may** process or ignore | may | All clauses |
| Service classifications | For services with choices, see Tables 2–4 in clause 4.2 | – | Clause 4.2 |

## Informative Annexes (Condensed)
- **Annex A (Bibliography)**: Lists ETSI TS 101 862 (Qualified certificate profile) and TS 102 280 (X.509 V.3 Certificate Profile for Natural Persons). These provide additional certificate profiles for reference.