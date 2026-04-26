# RFC 5752: Multiple Signatures in Cryptographic Message Syntax (CMS)
**Source**: IETF | **Version**: Standards Track | **Date**: January 2010 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc5752

## Scope (Summary)
Defines the multiple-signatures signed attribute to allow a signer to convey multiple `SignerInfo` objects while protecting against downgrade attacks (removal of “strong” signatures). The attribute provides a pointer to all of the signer’s other `SignerInfo` structures and must be included in each `SignerInfo`. This document specifies generation and processing rules and may assist during algorithm migration.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [CMS] Housley, R., "Cryptographic Message Syntax (CMS)", RFC 5652, September 2009.
- [PROFILE] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [SMIME-CERT] Ramsdell, B. and S. Turner, "Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.2 Certificate Handling", RFC 5750, January 2010.
- [SMIME-MSG] Ramsdell, B. and S. Turner, "Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.2 Message Specification", RFC 5751, January 2010.
- [ESS] Hoffman, P., Ed., "Enhanced Security Services for S/MIME", RFC 2634, June 1999.
- [ESSCertID] Schaad, J., "Enhanced Security Services (ESS) Update: Adding CertID Algorithm Agility", RFC 5035, August 2007.

## Definitions and Abbreviations
- **id-aa-multipleSignatures**: OID for the multiple-signatures attribute: `{ iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) id-aa(2) 51 }`.
- **MultipleSignatures**: ASN.1 SEQUENCE containing `bodyHashAlg`, `signAlg`, `signAttrsHash`, and optional `cert` (ESSCertIDv2).
  - `bodyHashAlg`: `DigestAlgorithmIdentifier` for the referenced attribute.
  - `signAlg`: `SignatureAlgorithmIdentifier` for the referenced attribute.
  - `signAttrsHash`: SEQUENCE with `algID` (MUST match digest algorithm of the `SignerInfo` containing this attribute) and `hash` (hash of `signedAttrs`).
  - `cert`: OPTIONAL, MUST be present if fields in other multiple-signatures attributes are the same.
- **SignAttrsHash**: ASN.1 SEQUENCE with `algID` (DigestAlgorithmIdentifier) and `hash` (OCTET STRING).
- **Key Words**: “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, “OPTIONAL” as per [RFC2119].

## 1. Introduction
The Cryptographic Message Syntax (CMS; see [CMS]) defines `SignerInfo` to provide data for verifying a signer’s digital signature. Multiple `SignerInfo` objects can be included for multiple signers or multiple algorithms. An attacker could remove all but the weakest `SignerInfo` if a hash/signature algorithm is broken. The multiple-signatures attribute includes a pointer to all the signer’s `SignerInfo` structures, so removal of any `SignerInfo` is detectable. This attribute is not a countersignature; it points to parallel signatures by the same signer.

## 2. Rationale
Protects against downgrade attacks by making removal of a SignerInfo detectable. Examples of relying parties (weak-only, strong-only, both) and how they may process signatures with and without the attribute. Local policy MAY dictate that removal of the ‘strong’ algorithm results in an invalid signature.

### 2.1. Attribute Design Requirements
1. Use CMS attribute structure.
2. Computable before any signatures are applied.
3. Contain enough information to identify individual SignerInfo objects.
4. Resist collision, preimage, and second preimage attacks.

## 3. Multiple Signature Indication
The multiple-signatures attribute MUST be a signed attribute. The number of attribute values in a SignerInfo equals the number of signatures applied by the signer minus one. This attribute is multi-valued; there MAY be more than one `AttributeValue`. The OID is `id-aa-multipleSignatures`. The value is of type `MultipleSignatures` (see Definitions). Example: For three signatures, each SignerInfo contains two attribute values pointing to the other two.

## 4. Message Generation and Processing

### 4.1. SignedData Type
- The signer MUST indicate the CMS version.
- The signer SHOULD include the digest algorithm in `SignedData.digestAlgorithms` if not already present.
- The signer MUST include the `encapContentInfo` (same for all signers in this SignedData).
- The signer SHOULD add certificates sufficient for certificate paths.
- The signer MAY include CRLs.
- The signer MUST:
  - Retain the existing `signerInfo` objects.
  - Include their own `signerInfo` object(s).

### 4.2. EncapsulatedContentInfo Type
Procedures as specified in Section 5.2 of [CMS].

### 4.3. SignerInfo Type
Procedures as per Section 4.4.1 of [CMS] with the addition:
- The signer MUST include the multiple-signatures attribute in `signedAttrs`.

### 4.4. Message Digest Calculation Process

#### 4.4.1. multiple-signatures Signed Attribute Generation
1. All other signed attributes are placed in respective SignerInfo structures, but signatures are not yet computed.
2. Multiple-signatures attributes are added to each SignerInfo with `SignAttrsHash.hash` containing a zero-length octet string.
3. The correct `SignAttrsHash.hash` value is computed for each SignerInfo.
4. After all hash values are computed, the correct values are placed into their respective `SignAttrsHash.hash` fields.

#### 4.4.2. Message Digest Calculation Process
Remaining procedures as specified in Section 5.4 of [CMS].

### 4.5. Signature Generation Process
Procedures as specified in Section 5.5 of [CMS].

### 4.6. Signature Verification Process
Procedures as per Section 5.6 of [CMS] with addition:
- If the SignedData signerInfo includes the multiple-signatures attribute, the attribute values must be calculated as described in Section 4.4.1.
- For every SignerInfo considered present for a given signer, the number of `MultipleSignatures AttributeValue(s)` present MUST equal the number of SignerInfo objects for that signer minus one.
- The hash value in each `MultipleSignatures AttributeValue` MUST match the output of the message digest calculation from Section 4.4.1 for each SignerInfo.

## 5. Signature Evaluation Processing (Non-normative)
Recommended processing when multiple SignerInfo objects exist (single or nested SignedData):
1. Evaluate each SignerInfo object independently (math, public key validation, local policy).
2. Combine results of SignerInfo at the same level (by signer group).
3. Combine results of nested SignedData objects.

Default processing:
- Group SignerInfo by signer.
- Take best result per signer.
- Take worst result across signers for the SignedData.
Application and local policy may modify steps.

## 6. Security Considerations
- Security of hash and signature algorithms used applies.
- If hashing and signing are by different entities, the signing entity must ensure the hash is from a trustworthy source. Multiple hashes using different algorithms can mitigate.
- This attribute cannot be relied upon if all algorithms used are “cracked”; verifier cannot determine a collision that satisfies all algorithms.
- Local policy and application context affect signature validity.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The multiple-signatures attribute MUST be a signed attribute. | shall | Section 3 |
| R2 | Number of MultipleSignatures attribute values in a SignerInfo equals number of signatures applied by signer less one. | shall | Section 3 |
| R3 | In SignedData generation, signer MUST retain existing signerInfo and include theirs. | shall | Section 4.1 |
| R4 | Signer MUST include multiple-signatures attribute in signedAttrs. | shall | Section 4.3 |
| R5 | For verification, number of MultipleSignatures attribute values MUST equal number of SignerInfo for that signer minus one and hash MUST match. | shall | Section 4.6 |
| R6 | cert field MUST be present if fields in other multiple-signatures attributes are the same. | shall | Section 3 |
| R7 | The signer SHOULD include digest algorithm in SignedData.digestAlgorithms if not present. | should | Section 4.1 |
| R8 | The signer MAY include CRLs. | may | Section 4.1 |
| R9 | There MAY be more than one AttributeValue for multiple-signatures. | may | Section 3 |

## Informative Annexes (Condensed)
- **Appendix A. ASN.1 Module**: Normative ASN.1 specification for `MultipleSignatures-2008` module, including imports from [CMS] and [ESSCertID]. Defines types `MultipleSignatures` and `SignAttrsHash`.
- **Appendix B. Background**: Informative. Enumerates locations in CMS where hashes are used (body hash and signed attributes hash) and describes collision, preimage, and second preimage resistance requirements for different attacker scenarios (Alice, Bob, Mallory). Notes that hashing signed attributes is more structured and harder to attack than body hashing. Highlights risk of accepting hash values from third parties and how time stamp services can add unpredictability.

## Appendix A. ASN.1 Module (Normative)
```asn1
MultipleSignatures-2008
  { iso(1) member-body(2) us(840) rsadsi(113549)
    pkcs(1) pkcs9(9) smime(16) modules(0)
    id-mod-multipleSig-2008(34) }

DEFINITIONS IMPLICIT TAGS ::=

BEGIN

-- EXPORTS All

IMPORTS

  DigestAlgorithmIdentifier, SignatureAlgorithmIdentifier
    FROM CryptographicMessageSyntax2004
      { iso(1) member-body(2) us(840) rsadsi(113549)
        pkcs(1) pkcs9(9) smime(16) modules(0) cms-2004(24) }

  ESSCertIDv2
    FROM ExtendedSecurityServices-2006
      { iso(1) member-body(2) us(840) rsadsi(113549)
        pkcs(1) pkcs9(9) smime(16) modules(0) id-mod-ess-2006(30) }
;

-- Section 3.0

id-aa-multipleSignatures OBJECT IDENTIFIER ::= { iso(1) member-body(2)
us(840) rsadsi(113549) pkcs(1) pkcs9(9) id-aa(2) 51 }

MultipleSignatures ::= SEQUENCE {
  bodyHashAlg     DigestAlgorithmIdentifier,
  signAlg         SignatureAlgorithmIdentifier,
  signAttrsHash   SignAttrsHash,
  cert            ESSCertIDv2 OPTIONAL }

SignAttrsHash ::= SEQUENCE {
  algID            DigestAlgorithmIdentifier,
  hash             OCTET STRING }

END