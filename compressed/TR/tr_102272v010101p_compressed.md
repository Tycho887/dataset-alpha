# ETSI TR 102 272: Electronic Signatures and Infrastructures (ESI); ASN.1 format for signature policies
**Source**: ETSI | **Version**: V1.1.1 | **Date**: December 2003 | **Type**: Technical Report (informative, contains normative clauses)
**Original**: http://www.etsi.org/deliver/etsi_tr/102200_102299/102272/01.01.01_60/tr_102272v010101p.pdf

## Scope (Summary)
Covers components of a signature policy as defined in TS 101 733 v1 and older versions. Specifies a structured format using ASN.1 syntax and DER encoding for machine‑processable signature policies.

## Normative References
- [1] ITU‑T X.509 (1997) | ISO/IEC 9594-8 (1998)
- [2] ITU‑T X.208 (1988) (withdrawn)
- [3] ITU‑T X.690 (2002) | ISO/IEC 8825-1 (2002) (BER/CER/DER)
- [4] ITU‑T F.1 (1998)
- [5] IETF RFC 3494 (LDAP)
- [6] IETF RFC 3280 (2002) (PKIX Certificate and CRL Profile)
- [7] IETF RFC 2560 (1999) (OCSP)
- [8] IETF RFC 3369 (CMS)
- [9] IETF RFC 2634 (1999) (Enhanced Security Services for S/MIME)
- [10] ISO 7498-2 (1989)
- [11] ISO/IEC 13888-1 (1997) (Non‑repudiation)
- [12] ITU‑T X.400 (1999)
- [13] ITU‑T X.500 (2001)
- [14] ITU‑T X.501 (2001)
- [15] IETF RFC 2587 (1999) (LDAPv2 Schema)
- [16] ITU‑T X.680 (2002) | ISO/IEC 8824-1 (2002) (ASN.1 specification)
- [17] IETF RFC 2450 (Proposed TLA and NLA Assignment Rule)

## Definitions and Abbreviations
- **signature policy**: set of rules for creation and validation of an electronic signature, under which the signature can be determined to be valid.
- **signature validation policy**: part of the signature policy specifying technical requirements on signer and verifier.
- **signature policy issuer**: entity defining technical and procedural requirements for a particular business need.
- **signer**: entity that creates an electronic signature.
- **verifier**: entity that validates an electronic signature.
- **arbitrator**: may be used to arbitrate disputes.
- **Certificate Authority (CA)**: trusted authority to create and assign certificates.
- **Attribute Authority (AA)**: authority issuing attribute certificates.
- **Time‑Stamping Authority (TSA)**: trusted third party creating time‑stamp tokens.
- **Trusted Service Provider (TSP)**: entity providing trust‑related information.
- **cautionary period**: period after signing time that verifier **shall** wait to get high assurance of key validity and revocation notification.
- **digital signature**: data appended to, or cryptographic transformation of, a data unit allowing proof of source and integrity.
- **public key certificate**: unforgeable data binding a public key to a user, signed by the issuing CA.
- **valid electronic signature**: signature that passes validation according to a signature validation policy.
- **RSA**: Rivest‑Shamir‑Adleman cryptography.
- **Abbreviations**: AA, API, ARL, ASN.1, CA, CAD, CMS, CRL, DER, ES, ES‑T, MIME, OCSP, OID, PKIX, RSA, SHA‑1, TSA, TSP, URI, URL, XML.

## 4 Signature Policy Overview
- **Signature Policy**: set of rules for creation and validation; may be explicitly identified (by a globally unique reference bound in the signature) or implied by context.
- Policy **shall** include: rules for functionality (signature validation policy), implied certificate policies, environment rules (e.g., CAD).
- Signature Validation Policy includes rules for use of TSPs (CA, AA, TSA) and definition of required signature components.
- Explicit policy must have a unique binary encoded value; various syntaxes possible (ASN.1, XML), but a definitive form with unique hash exists.

## 5 Signature Policy Specification in Informal Free Text Form
- Policy **must** be identifiable and include: unambiguous algorithm identifier, hash value.
- **Signature Policy Information** should include:
  - **Signature Policy Identifier** (unique OID, version‑specific).
  - **Date of Issue**.
  - **Signature Policy Issuer** (body responsible; signer/verifier **shall** authenticate origin if trust is required).
  - **Field of Application** (general legal/contract/application contexts).
  - Optional **Signature Policy Extensions**.
- **Signature Validation Policy** should include:
  - **Signing Period** (start, optional end).
  - **Common Rules** (rules common to all commitment types).
  - **Commitment Rules** (per‑commitment‑type rules).
  - Optional **Extensions**.
- Both Common and Commitment Rules contain:
  - **Signer Rules** and **Verifier Rules**.
  - **Trust Conditions** for signing certificate, time‑stamping, attributes.
  - Optional **Algorithm Constraints** and **Extensions**.
- If rules are present in Common Rules, they **shall not** be present in Commitment Rules. If Signer Rules, Verifier Rules, Signing Cert Trust Conditions, Timestamp Trust Conditions are absent from Common Rules, they **shall** be present in each Commitment Rule.
- **Signer Rules**: identify external/internal signed data hash, mandated signed/unsigned attributes (by OID), whether signer certificate or full path is provided.
- **Verifier Rules**: identify unsigned attributes that **shall** be added by verifier if absent.
- **Certificate Requirements** (used in trust conditions): trust point (self‑signed cert), path length constraint, acceptable certificate policies, naming constraints, policy constraints.
- **Revocation Requirements**: specify checks on end certificate and CA certificates using CRLs, OCSP, delta‑CRLs, or other mechanisms. Checks **shall** be done after cautionary period.
- **Time‑Stamp Trust Condition**: includes trust trees, revocation, naming constraints, caution period, maximum acceptable time delay.
- **Attribute Trust Condition**: if absent, certified attributes may not be considered valid. Includes attribute mandatory flag, how certified (claimed/certified/either), trust trees, revocation, constraints on attribute types/values.
- **Algorithm Constraints**: optional; specify signing algorithms and minimum key lengths for signer, issuer of end‑entity/CA/AA/TSA certificates.

## 6 Signature Policy Specification in ASN.1
- **Shall** be identifiable by an OID and have unique DER encoding so that a single hash value can be computed.
- **Overall ASN.1 Structure**:
  - `SignaturePolicy` SEQUENCE: `signPolicyHashAlg` (AlgorithmIdentifier), `signPolicyInfo` (SignPolicyInfo), optional `signPolicyHash` (OCTET STRING).
  - `SignPolicyInfo` SEQUENCE: `signPolicyIdentifier` (OID), `dateOfIssue` (GeneralizedTime), `policyIssuerName` (GeneralNames), `fieldOfApplication` (DirectoryString), `signatureValidationPolicy` (SignatureValidationPolicy), optional `signPolExtensions`.

### 6.2 Signature Validation Policy
- `SignatureValidationPolicy` SEQUENCE: `signingPeriod` (SigningPeriod), `commonRules` (CommonRules), `commitmentRules` (CommitmentRules), optional `signPolExtensions`.
- `SigningPeriod` SEQUENCE: `notBefore` (GeneralizedTime), optional `notAfter` (GeneralizedTime).

### 6.3 Common Rules
- `CommonRules` SEQUENCE with optional fields: [`0`] signerAndVeriferRules, [`1`] signingCertTrustCondition, [`2`] timeStampTrustCondition, [`3`] attributeTrustCondition, [`4`] algorithmConstraintSet, [`5`] signPolExtensions.
- If a field is present in CommonRules, it **shall not** be present in any CommitmentRule. If signerAndVeriferRules, signingCertTrustCondition, or timeStampTrustCondition are absent from CommonRules, they **shall** be present in each CommitmentRule.

### 6.4 Commitment Rules
- `CommitmentRules` SEQUENCE OF `CommitmentRule`.
- `CommitmentRule` SEQUENCE: `selCommitmentTypes` (SelectedCommitmentTypes), optional fields as in CommonRules.
- `SelectedCommitmentTypes` SEQUENCE OF CHOICE: `empty` (NULL) or `recognizedCommitmentType` (CommitmentType). If "empty", rule applies when commitment type is not present. Otherwise, signature **shall** contain a commitment type that fits one listed.
- `CommitmentType` SEQUENCE: `identifier` (CommitmentTypeIdentifier), optional `fieldOfApplication`, optional `semantics`.

### 6.5 Signer and Verifier Rules
- `SignerAndVerifierRules` SEQUENCE: `signerRules`, `verifierRules`.
- **SignerRules** SEQUENCE: optional `externalSignedData` (BOOLEAN), `mandatedSignedAttr` (CMSAttrs), `mandatedUnsignedAttr` (CMSAttrs), [`0`] `mandatedCertificateRef` (default `signerOnly`), [`1`] `mandatedCertificateInfo` (default `none`), [`2`] optional `signPolExtensions`.
  - `CertRefReq` ENUMERATED: `signerOnly` (1), `fullPath` (2).
  - `CertInfoReq` ENUMERATED: `none` (0), `signerOnly` (1), `fullPath` (2).
- **VerifierRules** SEQUENCE: `mandatedUnsignedAttr` (CMSAttrs), optional `signPolExtensions`.

### 6.6 Certificate and Revocation Requirements
- **CertificateTrustTrees** SEQUENCE OF `CertificateTrustPoint`.
- `CertificateTrustPoint` SEQUENCE: `trustpoint` (Certificate), optional `pathLenConstraint` (0..MAX, zero means only trustpoint and end‑entity), optional `acceptablePolicySet` (if absent "any policy"), optional `nameConstraints`, optional `policyConstraints`.
- `NameConstraints` SEQUENCE: optional `permittedSubtrees`, optional `excludedSubtrees`.
- `PolicyConstraints` SEQUENCE: optional `requireExplicitPolicy`, optional `inhibitPolicyMapping` (both SkipCerts 0..MAX).
- **CertRevReq** SEQUENCE: `endCertRevReq` (RevReq), [`0`] `caCerts` (RevReq).
- `RevReq` SEQUENCE: `enuRevReq` (EnuRevReq), optional `exRevReq`.
- `EnuRevReq` ENUMERATED: `clrCheck` (0), `ocspCheck` (1), `bothCheck` (2), `eitherCheck` (3), `noCheck` (4), `other` (5).

### 6.7 Signing Certificate Trust Conditions
- `SigningCertTrustCondition` SEQUENCE: `signerTrustTrees` (CertificateTrustTrees), `signerRevReq` (CertRevReq).

### 6.8 Time-stamp Trust Conditions
- `TimestampTrustCondition` SEQUENCE: optional [`0`] `ttsCertificateTrustTrees`, [`1`] `ttsRevReq`, [`2`] `ttsNameConstraints`, [`3`] `cautionPeriod` (DeltaTime), [`4`] `signatureTimestampDelay` (DeltaTime).
- `DeltaTime` SEQUENCE: `deltaSeconds`, `deltaMinutes`, `deltaHours`, `deltaDays` all INTEGER.
- If `ttsCertificateTrustTrees` absent, same rules as `certificateTrustCondition` apply.
- Revocation checks **shall** be carried out once cautionary period is over.
- If signature timestamp is later than signing‑time attribute by more than `signatureTimestampDelay`, signature **shall** be considered invalid.

### 6.9 Attribute Trust Conditions
- If `attributeTrustCondition` absent, certified attributes may not be considered valid.
- `AttributeTrustCondition` SEQUENCE: `attributeMandated` (BOOLEAN), `howCertAttribute` (HowCertAttribute), optional [`0`] `attrCertificateTrustTrees`, [`1`] `attrRevReq`, [`2`] `attributeConstraints`.
- `HowCertAttribute` ENUMERATED: `claimedAttribute` (0), `certifiedAttribtes` (1), `either` (2).
- `AttributeConstraints` SEQUENCE: optional `attributeTypeConstraints`, optional `attributeValueConstraints`.

### 6.10 Algorithm Constraints
- `AlgorithmConstraintSet` SEQUENCE: optional [`0`] signerAlgorithmConstraints, [`1`] eeCertAlgorithmConstraints, [`2`] caCertAlgorithmConstraints, [`3`] aaCertAlgorithmConstraints, [`4`] tsaCertAlgorithmConstraints.
- Each `AlgorithmConstraints` SEQUENCE OF `AlgAndLength`.
- `AlgAndLength` SEQUENCE: `algID` (OID), optional `minKeyLength` (INTEGER bits), optional `other` (SignPolExtensions).

### 6.11 Signature Policy Extensions
- Extensions may be added to any of the structures. Defined using `SignPolExtensions` (SEQUENCE OF `SignPolExtn`).
- `SignPolExtn` SEQUENCE: `extnID` (OID), `extnValue` (OCTET STRING containing DER‑encoded extension).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Signature Policy shall be identifiable by an OID. | shall | Clause 6 intro |
| R2 | Signature Policy shall have a unique DER encoding. | shall | Clause 6 intro |
| R3 | The signer and verifier shall re‑calculate and check the signPolicyHash whenever the policy is passed. | shall | Clause 6.1 |
| R4 | If a field is present in CommonRules, it shall not be present in any CommitmentRule. | shall | Clause 6.3 |
| R5 | If signerAndVeriferRules, signingCertTrustCondition, or timeStampTrustCondition are absent from CommonRules, they shall be present in each CommitmentRule. | shall | Clause 6.3 |
| R6 | The electronic signature shall contain a commitment type indication that shall fit one of the commitment types listed in the CommitmentRule (unless SelectedCommitmentTypes is "empty"). | shall | Clause 6.4 |
| R7 | A specific commitment type identifier shall not appear in more than one commitment rule. | shall | Clause 6.4 |
| R8 | The mandatedSignedAttr field shall include OIDs for all signed attributes required by the present document and additional attributes required by this policy. | shall | Clause 6.5.1 |
| R9 | The mandatedUnsignedAttr field shall include OIDs for all unsigned attributes required by the present document and additional attributes required by this policy. | shall | Clause 6.5.1 |
| R10 | If signature timestamp delay exceeds signatureTimestampDelay, the signature shall be considered invalid. | shall | Clause 6.8 |
| R11 | The extnID field shall contain the OID for the extension; the extnValue field shall contain the DER‑encoded value. | shall | Clause 6.11 |
| R12 | The signer/verifier shall authenticate the origin of the signature policy as coming from the identified issuer if trust is required. | shall | Clause 5 (policyIssuerName) |
| R13 | For an explicit signature policy, the signer shall include the hash of the signature policy. | shall | Annex B.1 |
| R14 | The signer and verifier shall apply the rules specified by the identified policy when validating the signature. | shall | Annex B.1 |
| R15 | The verifier shall wait the cautionary period before checking revocation status. | shall | Clause 6.8, Annex B.5.3 |

## Annexes (Condensed)

### Annex A: ASN.1 Modules
- **A.1**: Full ASN.1 module using X.208 (1988) syntax. Defines all structures from clause 6, including `SignaturePolicy`, `CommitmentRule`, `SignerRules`, `CertificateTrustPoint`, `EnuRevReq`, etc. This module has precedence over A.2 in case of conflict.
- **A.2**: Equivalent module using X.680 (2002) syntax. Identical definitions; A.1 takes precedence.

### Annex B: What is a Signature Policy and Signature Validation Policy (Informative)
- **B.0**: Explains the relationship between signature policy, electronic signature, and legal framework. Policy may be explicit (OID + hash) or implicit. The document defines an ASN.1 structure for machine‑processable policies.
- **B.1 Identification of signature policy**: Signer includes signed attribute specifying explicit or implicit policy. For explicit, signer **shall** include hash. Policy may have qualifiers (URL, user notice). If absent, no legal significance.
- **B.2 General signature policy information**: Should include Policy OID, date of issue, issuer name, signing period, field of application.
- **B.3 Recognized commitment types**: Policy may recognize one or more commitment types; each includes OID and qualifier. Only recognized types allowed.
- **B.4 Rules for use of certification authorities**: Trust points and certificate path constraints (policy constraints, naming constraints). Certification path must exist between signer’s certificate and a trust point.
- **B.5 Rules for time‑stamping**: Timestamp must prove signature existed before certificate expiry/revocation. Describes cautionary period and timestamp delay.
- **B.6 Revocation rules**: Policy defines minimum checks (CRLs, OCSP) to be carried out after cautionary period.
- **B.7 Rules for roles**: Supported as claimed or certified (via attribute certificates). Trust points for AAs may differ from CAs.
- **B.8 Rules for verification data**: Specifies required signed/unsigned attributes for signer and additional data for verifier.
- **B.9 Algorithm constraints and key lengths**: Identifies allowed hashing, public‑key algorithms and minimum key lengths for all relevant parties.
- **B.10 Other signature policy rules**: May include environment‑specific rules (human‑readable or processable).
- **B.11 Signature policy protection**: Source of policy must be authenticated (e.g., by electronic signatures). The OID, hash algorithm, and hash value **shall** be included in the electronic signature. The policy must have a single binary encoded form producing one hash.

### Annex C: Bibliography
(Informative list of referenced standards, including ETSI TS 101 733, TS 101 903, TS 101 861, IETF RFCs on PKIX, CMS, etc., and European Directive 1999/93/EC.)