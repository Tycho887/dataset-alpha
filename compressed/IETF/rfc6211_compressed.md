# RFC 6211: Cryptographic Message Syntax (CMS) Algorithm Identifier Protection Attribute
**Source**: IETF | **Version**: Standards Track | **Date**: April 2011 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc6211

## Scope (Summary)
Defines a new CMS signed/authenticated attribute that duplicates algorithm identifiers (digest, signature, MAC) so they are protected by the signature or authentication process, preventing algorithm substitution attacks.

## Normative References
- [ASN.1-2008]: ITU-T Recommendations X.680, X.681, X.682, X.683 (2008)
- [CMS]: RFC 5652 (Cryptographic Message Syntax, September 2009)
- [ESS-BASE]: RFC 2634 (Enhanced Security Services for S/MIME, June 1999)
- [RFC2119]: RFC 2119 (Key words for use in RFCs, March 1997)
- [RFC5035]: RFC 5035 (ESS Update: Adding CertID Algorithm Agility, August 2007)
- [RFC5912]: RFC 5912 (New ASN.1 Modules for PKIX, June 2010)

## Definitions and Abbreviations
- **CMSAlgorithmProtection**: ASN.1 SEQUENCE containing digestAlgorithm, and either signatureAlgorithm or macAlgorithm.
- **aa-cmsAlgorithmProtection**: Attribute OID { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) 52 }.
- **Algorithm substitution attack**: Changing the algorithm or its parameters to alter signature verification outcome.
- **DER**: Distinguished Encoding Rules.
- **MUST, SHALL, SHOULD, MAY, etc.**: As defined in RFC 2119.

## 1. Introduction (Background)
- CMS is vulnerable to algorithm substitution attacks because algorithm identifiers in SignerInfo are not directly protected by the signature.
- Unlike X.509 certificates, where `TBSCertificate.signature` protects the algorithm, CMS lacks such protection.
- Existing implicit protections (e.g., RSA PKCS#1 v1.5 encodes hash inside signature; DSA tied to SHA-1) are insufficient with new algorithms (e.g., RSA-PSS, SHA-3).
- Countersigning does not protect against algorithm substitution attacks as it signs the signature value, not the algorithm identifiers.
- Analysis of SignerInfo fields: `version` unprotected but harmless; `sid` can be protected via SigningCertificateV2 attribute; `digestAlgorithm` and `signatureAlgorithm` only indirectly protected; `signedAttrs` protected; `unsignedAttrs` unprotected.
- This attribute explicitly protects `digestAlgorithm`, `signatureAlgorithm`, and `macAlgorithm` fields.

## 2. Attribute Structure
- The attribute is of type `CMSAlgorithmProtection` (SEQUENCE).
- OID: `id-aa-CMSAlgorithmProtection` = {1.2.840.113549.1.9.52}
- Fields:
  - `digestAlgorithm`: Copy of `SignerInfo.digestAlgorithm` or `AuthenticatedData.digestAlgorithm` with parameters.
  - `signatureAlgorithm`: Copy of `SignerInfo.signatureAlgorithm` (only present in signed attributes).
  - `macAlgorithm`: Copy of `AuthenticatedData.macAlgorithm` (only present in authenticated attributes).
- **Constraint**: Exactly one of `signatureAlgorithm` or `macAlgorithm` SHALL be present (WITH COMPONENTS clause).
- **Constraint**: The attribute MUST have a single attribute value (MUST NOT be zero or multiple).
- **Constraint**: The attribute MUST be a signed attribute (in SignerInfo.signedAttrs) or authenticated attribute (in AuthenticatedData.authAttrs); MUST NOT be unsigned/unauthenticated/unprotected.
- **Constraint**: There MUST be only one instance of this attribute per `SignedAttributes` or `AuthAttributes` set.

## 3. Verification Process
### 3.1. Common Rules
- **Comparison**: A field with a default value MUST compare as identical regardless of encoding (defaulted or explicit). Binary compare of encoded bytes is insufficient.
- **NULL parameters**: For algorithms like SHA-1, some implementations include NULL in ASN.1 encoding, others omit; implementers must decide equality. (Corner case unlikely as same implementation produces both ends.)

### 3.2. Signed Data Verification Changes
- If a CMS validator supports this attribute, the following additional steps MUST be performed:
  1. Compare `SignerInfo.digestAlgorithm` to attribute's `digestAlgorithm`. If not the same (modulo encoding), signature validation MUST fail.
  2. Compare `SignerInfo.signatureAlgorithm` to attribute's `signatureAlgorithm`. If not the same (modulo encoding), signature validation MUST fail.

### 3.3. Authenticated Data Verification Changes
- If a CMS validator supports this attribute, the following additional steps MUST be performed:
  1. Compare `AuthenticatedData.digestAlgorithm` to attribute's `digestAlgorithm`. If not the same (modulo encoding), authentication MUST fail.
  2. Compare `AuthenticatedData.macAlgorithm` to attribute's `macAlgorithm`. If not the same (modulo encoding), authentication MUST fail.

## 4. IANA Considerations
- All identifiers assigned from the S/MIME OID arc; no new registrations.

## 5. Security Considerations
- Addresses algorithm substitution attacks; no known exploit at time of writing.
- Attribute provides no security if placed in unsigned/unauthenticated location.
- Prevents substitution of weaker algorithms or parameter modification (e.g., changing initial hash value as in RFC 6210).

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Exactly one of `signatureAlgorithm` or `macAlgorithm` SHALL be present. | SHALL | Section 2 (ASN.1 constraint) |
| R2 | An algorithm protection attribute MUST have a single attribute value (MUST NOT be zero or multiple). | MUST | Section 2 |
| R3 | The attribute MUST be a signed attribute or authenticated attribute; MUST NOT be unsigned/unauthenticated/unprotected. | MUST | Section 2 |
| R4 | There MUST be only one instance of the algorithm protection attribute per `SignedAttributes` or `AuthAttributes` set. | MUST | Section 2 |
| R5 | When comparing algorithm fields, a field with a default value MUST compare as identical regardless of encoding. | MUST | Section 3 |
| R6 | For SignedData: If the validator supports this attribute, it MUST compare `SignerInfo.digestAlgorithm` to attribute's `digestAlgorithm`; if not same (modulo encoding), signature validation MUST fail. | MUST | Section 3.1 |
| R7 | For SignedData: If the validator supports this attribute, it MUST compare `SignerInfo.signatureAlgorithm` to attribute's `signatureAlgorithm`; if not same (modulo encoding), signature validation MUST fail. | MUST | Section 3.1 |
| R8 | For AuthenticatedData: If the validator supports this attribute, it MUST compare `AuthenticatedData.digestAlgorithm` to attribute's `digestAlgorithm`; if not same (modulo encoding), authentication MUST fail. | MUST | Section 3.2 |
| R9 | For AuthenticatedData: If the validator supports this attribute, it MUST compare `AuthenticatedData.macAlgorithm` to attribute's `macAlgorithm`; if not same (modulo encoding), authentication MUST fail. | MUST | Section 3.2 |

## Informative Annexes (Condensed)
- **Appendix A: 2008 ASN.1 Module**: Contains the ASN.1 module (`CMSAlgorithmProtectionAttribute`) using 2008 ASN.1 definitions and imports from [CMS] and [RFC5912]. Defines the `aa-cmsAlgorithmProtection` attribute and the `CMSAlgorithmProtection` SEQUENCE type with the WITH COMPONENTS constraint. This module is to be added to `SignedAttributesSet` and `AuthAttributeSet` in CMS.