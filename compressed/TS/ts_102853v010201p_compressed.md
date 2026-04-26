# ETSI TS 102 853 V1.2.1: Electronic Signatures and Infrastructures (ESI); Signature validation procedures and policies
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2014-12 | **Type**: Normative
**Original**: RTS/ESI-0002853v121

## Scope (Summary)
This Technical Specification specifies procedures for determining the technical validity of electronic signatures based on a set of validation constraints. It defines algorithms for validating basic signatures (AdES-BES/EPES), time-stamped signatures (AdES-T), and long-term validation (LTV) forms (e.g., AdES-A, PAdES-LTV). The scope does not cover whether a signature is accepted legally by a relying party.

## Normative References
- [1] ETSI TS 101 903 (V1.4.2): XML Advanced Electronic Signatures (XAdES)
- [2] ETSI TS 101 733 (V2.1.1): CMS Advanced Electronic Signatures (CAdES)
- [3] ETSI TS 102 231: Provision of harmonized Trust-service status Information
- [4] IETF RFC 5280: Internet X.509 Public Key Infrastructure Certificate and CRL Profile
- [5] ETSI TS 101 862: Qualified certificate Profile
- [6] ISO/IEC 9594-8:2014: Public-key and attribute certificate frameworks
- [7] ETSI TS 101 456: Policy requirements for CAs issuing qualified certificates
- [8] ETSI TS 102 042: Policy requirements for CAs issuing public key certificates
- [9] Directive 1999/93/EC on a Community framework for electronic signatures
- [10] W3C Recommendation (2008): XML Signature Syntax and Processing
- [11] IETF RFC 3161: Time-Stamp Protocol (TSP)
- [12] ETSI TS 102 778-1: PAdES Overview
- [13] ETSI TS 102 778-3: PAdES BES and EPES Profiles
- [14] ETSI TS 102 778-4: PAdES LTV Profile
- [15] ETSI TS 102 778-5: PAdES for XML Content
- [16] IETF RFC 5652: Cryptographic Message Syntax (CMS)
- [17] IETF RFC 4998: Evidence Record Syntax (ERS)
- [18] ETSI TS 103 171: XAdES Baseline Profile
- [19] ETSI TS 103 172: PAdES Baseline Profile
- [20] ETSI TS 103 173: CAdES Baseline Profile

## Definitions and Abbreviations
- **Advanced Electronic Signature (AdES)**: electronic signature meeting requirements of [9]: uniquely linked to signatory, capable of identifying signatory, created using means under sole control, linked to data to detect changes.
- **Certificate path (chain) validation**: process of checking that a certificate path is valid.
- **Certificate validation**: process of checking that a certificate or certificate path is valid.
- **Constraints**: abstract formulation of rules, values, ranges, and computation results against which a Signature can be validated.
- **Data to be signed**: data (document or parts) and signature attributes bound together.
- **Driving Application (DA)**: application that calls the SVA to validate signatures.
- **Long Term Validation (LTV)**: ability to validate signatures many years after signing, despite expired/revoked certificates or broken algorithms.
- **Proof Of Existence (POE)**: evidence that an object existed at a specific date/time.
- **Signature policy**: set of rules for creation and validation of an electronic signature.
- **Signature type**: specific format for encoding an advanced electronic signature.
- **Signature validation**: process of checking that a signature is valid, including certificate validation and signature verification.
- **Signature Validation Application (SVA)**: application implementing signature validation processes.
- **Signature validation policy**: set of rules (constraints) specifying how to validate the signature.
- **Signature verification**: checking the cryptographic value using signature verification data.
- **Signed data object(s)**: document(s) or parts for which an electronic signature has been generated.
- **Validation constraint**: criterion applied by SVA when validating a signature.
- **Validation data**: additional data (certificates, CRLs, OCSP, time-stamps) needed to validate the signature.
- **Verifier**: entity that wants to validate/verify a signature.
- **Abbreviations**: AdES, BES, CA, CAdES, CRL, CV, DA, EPES, ERS, ISC, LTV, OCSP, PAdES, POE, SAV, SVA, TA, TSA, TSL, TST, VCI, XAdES, XCV, XL, etc. (see clause 3.2 for full list).

## 4 Introduction to Signature Validation
- SVA validates signature against constraints and outputs validation report with status (VALID, INVALID, INDETERMINATE) and additional data.
- Constraints may override required checks; SVA shall report such overrides.
- Prior to processing, SVA **shall** check signature format conformance; non-conformance results in INVALID/FORMAT_FAILURE.
- SVA output is processed by DA; recommended behavior: VALID → consider valid; INVALID/INDETERMINATE → do not consider valid.
- Validation algorithm is presented for clarity; conformant implementations **shall** provide functionally equivalent behavior but need not follow the same steps.
- Constraints may originate from signature content, local configuration, or formal policies.

### 4.1 Status Indication
- **VALID**: signature technically valid (cryptographically, certificate trustworthy, constraints met).
- **INVALID**: failure of at least one consideration. Subcodes: REVOKED, HASH_FAILURE, SIG_CRYPTO_FAILURE, SIG_CONSTRAINTS_FAILURE, CHAIN_CONSTRAINTS_FAILURE, CRYPTO_CONSTRAINTS_FAILURE, EXPIRED, NOT_YET_VALID, FORMAT_FAILURE, POLICY_PROCESSING_ERROR, UNKNOWN_COMMITMENT_TYPE, TIMESTAMP_ORDER_FAILURE, GENERIC.
- **INDETERMINATE**: insufficient information. Subcodes: NO_SIGNER_CERTIFICATE_FOUND, NO_CERTIFICATE_CHAIN_FOUND, REVOKED_NO_POE, REVOKED_CA_NO_POE, OUT_OF_BOUNDS_NO_POE, CRYPTO_CONSTRAINTS_FAILURE_NO_POE, NO_POE, TRY_LATER, NO_POLICY, SIGNED_DATA_NOT_FOUND, GENERIC.
- Conformant SVA: same inputs → same result (VALID/INVALID) or INDETERMINATE; additional validation data may change INDETERMINATE to determined status.

### 4.2 Validation Constraints
- Defined via formal policies, configuration, or implementation.
- Types: X.509 certificate path validation constraints, certificate meta-data constraints, cryptographic constraints, signature element constraints (see Annex A).
- SVA **shall** check all constraints prescribed; if policy disables a check, SVA shall report it.

### 4.3 X.509 Certificate Meta-Data
- Additional information about certificates, CRLs, OCSP (e.g., qualified status, SSCD). May be derived from TSL, certificate content, or local configuration.

### 4.4 Trust Management
- Out of scope; XCV builds on trust anchors. DA selects trust anchors (e.g., from trusted root stores, TSLs).

### 4.5 Revocation Freshness
- Freshness: maximum accepted difference between issuance date of revocation info and current time (or past validation time). Figure 1 and 2 illustrate.

## 5 Basic Building Blocks
- Five building blocks: ISC, VCI, XCV, CV, SAV. Figure 3 shows relationship.

### 5.1 Identification of the Signer's Certificate (ISC)
- **Inputs**: signature (mandatory), signer certificate (optional).
- **Outputs**: signer's certificate on success; INDETERMINATE/NO_SIGNER_CERTIFICATE_FOUND on failure.
- **Processing**: Use signing certificate reference attribute (e.g., xades:SigningCertificate, ESS-signing-certificate). Check digest match against retrieved certificate. For XAdES, CAdES, PAdES specific rules in clauses 5.1.4.1–5.1.4.3. Format failure if no match.

### 5.2 Validation Context Initialization (VCI)
- **Inputs**: signature (mandatory), policies, TSLs, local config (optional).
- **Outputs**: X.509 validation parameters, certificate meta-data, chain/cryptographic/signature constraints.
- **Processing**: If policy is referenced, retrieve and verify using digest; if unknown → INVALID/UNKNOWN_COMMITMENT_TYPE; if inaccessible → INVALID/POLICY_PROCESSING_ERROR; if no policy identified → INDETERMINATE/NO_POLICY.
- Commitment type indication processing (XAdES: check ObjectReference elements).

### 5.3 X.509 Certificate Validation (XCV)
- **Inputs**: signature, signer certificate, X.509 parameters, meta-data, constraints.
- **Outputs**: VALID, or INDETERMINATE with subcode (NO_CERTIFICATE_CHAIN_FOUND, OUT_OF_BOUNDS_NO_POE, REVOKED_NO_POE, CRYPTO_CONSTRAINTS_FAILURE_NO_POE) or INVALID (CHAIN_CONSTRAINTS_FAILURE).
- **Processing**: 
  1) Check current time in validity range; if not → INDETERMINATE/OUT_OF_BOUNDS_NO_POE.
  2) Build prospective certificate chain from trust anchors.
  3) Run certification path validation per RFC 5280 with revocation checking; handle revocation/freshness cases per clause 5.3.4 steps 3a–3f.
  4) Apply chain constraints; if fail → INVALID/CHAIN_CONSTRAINTS_FAILURE.
  5) Apply cryptographic constraints; if fail → INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE.
  6) Return VALID with chain.

### 5.4 Cryptographic Verification (CV)
- **Inputs**: signature, signer certificate, optional chain and signed data.
- **Outputs**: VALID, or INVALID (HASH_FAILURE, SIG_CRYPTO_FAILURE) or INDETERMINATE (SIGNED_DATA_NOT_FOUND).
- **Processing**: 
  1) Obtain signed data objects.
  2) Check hash integrity; if fail → INVALID/HASH_FAILURE.
  3) Verify cryptographic signature; if fail → INVALID/SIG_CRYPTO_FAILURE.

### 5.5 Signature Acceptance Validation (SAV)
- **Inputs**: signature, CV output, cryptographic/signature constraints.
- **Outputs**: VALID, INVALID/SIG_CONSTRAINTS_FAILURE, INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE.
- **Processing**: Check each constraint; if algorithm/key size no longer reliable → INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE; if constraint fails → INVALID/SIG_CONSTRAINTS_FAILURE.
- Sub-clauses 5.5.4.1–5.5.4.8 specify processing of specific attributes: signing certificate reference, claimed signing time, signed data format, production place, time-stamps on data, countersignatures, signer attributes/roles.

## 6 Basic Validation Process (AdES-BES/EPES)
- **Inputs**: signature, signed data, signer certificate, TSLs, policies, local config.
- **Outputs**: status (VALID, INVALID, INDETERMINATE) with report.
- **Processing**:
  1) ISC → if INDETERMINATE → terminate.
  2) VCI → if failure → terminate with appropriate code.
  3) XCV → if INDETERMINATE/REVOKED_NO_POE: check content-time-stamp; if after revocation → INVALID/REVOKED; otherwise INDETERMINATE. If INDETERMINATE/OUT_OF_BOUNDS_NO_POE: check content-time-stamp; if after expiration → INVALID/EXPIRED; otherwise INDETERMINATE. Other INDETERMINATE → terminate.
  4) CV → if failure → terminate.
  5) SAV → if INDETERMINATE/CRYPTO_CONSTRAINTS_FAILURE_NO_POE on signature value: check content-time-stamp; if algorithms still reliable at token time → INVALID/CRYPTO_CONSTRAINTS_FAILURE; otherwise INDETERMINATE.
  6) Return VALID with report.

## 7 Validation Process for Time-Stamps
- Treats RFC 3161 TST as CAdES-BES.
- **Inputs**: TST, optional TSLs, policies, config, TSA certificate.
- **Processing**:
  1) Validate TST as BES signature (clause 6) with TSA trust anchors.
  2) Extract TSTInfo data (generation time, message imprint).

## 8 Validation Process for AdES-T
- **Inputs**: signature, signed data, etc.
- **Processing**:
  1) Initialize set of signature time-stamp tokens and best-signature-time = current time.
  2) Run BES validation (clause 6); if VALID or INDETERMINATE (REVOKED_NO_POE, OUT_OF_BOUNDS_NO_POE, CRYPTO_CONSTRAINTS_FAILURE_NO_POE) → continue.
  3) Time-mark verification (out of scope).
  4) Validate each signature time-stamp: message imprint check, then clause 7; on VALID, update best-signature-time.
  5) Compare times: if REVOKED_NO_POE and revocation time is after best-signature-time → continue; if OUT_OF_BOUNDS_NO_POE and best-signature-time before notBefore → INVALID/NOT_YET_VALID; if CRYPTO_CONSTRAINTS_FAILURE_NO_POE and algorithms reliable at best-signature-time → continue; check time-stamp order → if fail → INVALID/TIMESTAMP_ORDER_FAILURE.
  6) Handle time-stamp delay constraint if specified.
  7) Return VALID.

## 9 Validation of LTV Forms
- Validates CAdES-A, XAdES-A, PAdES-LTV, and intermediate forms.
- Uses concept of Proof Of Existence (POE) and control-time sliding.

### 9.1 POE Concept
- POE: evidence that an object existed at a past time (e.g., time-stamp on object).

### 9.2 Additional Building Blocks

#### 9.2.1 Past Certificate Validation
- Validates certificate at a past date using POEs and sliding control-time.
- **Processing**:
  1) Build prospective certificate chain.
  2) Run certification path validation at a date in intersection of validity intervals (without revocation checking).
  3) Perform control-time sliding process (clause 9.2.2).
  4) Apply chain constraints.
  5) Return VALID with chain and control-time, or INDETERMINATE.

#### 9.2.2 Control-Time Sliding Process
- **Inputs**: chain, POEs, cryptographic constraints.
- **Processing**: 
  1) Initialize control-time = current time.
  2) For each certificate in chain (starting from trust anchor):
     a) Find revocation info issued before control-time.
     b) Check POE for certificate and revocation info at/before control-time.
     c) If revoked → set control-time = revocation date; if not revoked and not fresh → set control-time = issuance date of revocation info; otherwise unchanged.
     d) Apply cryptographic constraints; if fail → set control-time to lower bound.
  3) Terminate with VALID and control-time.

#### 9.2.3 POE Extraction
- Derives POEs from validated time-stamps (direct/indirect). Methods for different attribute types (signature time-stamp, archive time-stamp, long-term-validation attribute, PDF document time-stamp). See clauses 9.2.3.4.1–9.2.3.4.6.

#### 9.2.4 Past Signature Validation Process
- Uses past certificate validation and POEs to resolve INDETERMINATE status.
- **Processing**:
  1) Past certificate validation; if VALID with control-time → next step.
  2) If POE of signature value at/before control-time:
     - For REVOKED_NO_POE/REVOKED_CA_NO_POE → return VALID.
     - For OUT_OF_BOUNDS_NO_POE: if POE before notBefore → INVALID/NOT_YET_VALID; else VALID.
     - For CRYPTO_CONSTRAINTS_FAILURE_NO_POE: if each algorithm has POE before expiry → VALID.
  3) Otherwise return current status.

### 9.3 Long Term Validation Process
- **Inputs**: signature, signed data, TSLs, policies, config, initial POEs, signer certificate.
- **Processing**:
  1) Initialize POEs with current objects.
  2) Run AdES-T validation (clause 8). If VALID and LTV constraints required → continue; if INDETERMINATE (REVOKED_NO_POE, etc.) → continue; otherwise fail.
  3) Process long-term-validation attributes (if any) from last to first: validate time-stamp, extract POEs, if fail and not mandatory → ignore; else fail.
  4) Process archive-time-stamps from last to first similarly.
  5) Process time-stamps on references from last to first.
  6) Process time-stamps on references and signature value from last to first.
  7) Process signature time-stamps from last to first.
  8) Past signature validation: if VALID → return VALID; else fail.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | SVA shall check signature format conformance before processing. | shall | Cl.4 |
| R2 | SVA shall report any overridden checks due to policy. | shall | Cl.4 |
| R3 | SVA shall output indication of policy/constraints used. | shall | Cl.4.1 |
| R4 | Signer's certificate identification shall use digest matching in signing certificate reference. | shall | Cl.5.1.4 |
| R5 | VCI shall return appropriate error if policy inaccessible or unknown. | shall | Cl.5.2.4 |
| R6 | XCV shall include revocation checking for each certificate in chain. | shall | Cl.5.3.4 |
| R7 | CV shall verify signature cryptographic value using signer's public key. | shall | Cl.5.4.4 |
| R8 | SAV shall check all signature/cryptographic constraints; report failures. | shall | Cl.5.5 |
| R9 | Basic validation process shall follow steps in clause 6.4. | shall | Cl.6.4 |
| R10 | AdES-T validation shall process signature time-stamps to determine best-signature-time. | shall | Cl.8.4 |
| R11 | LTV validation shall use past certificate validation and control-time sliding. | shall | Cl.9.2-9.3 |
| R12 | Conformant implementation shall provide functionally equivalent behavior to algorithms. | shall | Cl.4 |

## Informative Annexes (Condensed)
- **Annex A (Validation Constraints)**: Lists categories of constraints (X.509 path, meta-data, cryptographic, signature elements) with references to RFC 5280, ETSI TRs, etc. No new requirements.
- **Annex B (Certificate Meta-Data)**: Describes types of meta-data (e.g., qualified status, SSCD) that DA may provide to SVA to avoid INDETERMINATE results.
- **Annex C (Validation Examples)**: Three examples (revoked signer certificate, revoked CA, LTV) walking through algorithms with timelines and expected outputs. Demonstrates how POEs and time-stamps resolve INDETERMINATE status.
- **Annex D (Validation Process vs. Conformance Levels)**: Maps validation processes to conformance levels (ST, T, LT, LTA) defined in baseline profiles. LTV process covers all levels.