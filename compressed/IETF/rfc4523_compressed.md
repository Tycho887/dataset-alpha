# RFC 4523: Lightweight Directory Access Protocol (LDAP) Schema Definitions for X.509 Certificates
**Source**: IETF (Standards Track) | **Version**: June 2006 | **Date**: June 2006 | **Type**: Normative  
**Original**: [RFC 4523](https://www.rfc-editor.org/rfc/rfc4523)

## Scope (Summary)
Defines LDAP schema (attribute types, matching rules, syntaxes, object classes) for representing X.509 certificates, certificate revocation lists, cross-certificate pairs, and related security information as specified in ITU-T X.509 and X.521. Replaces schema definitions from RFCs 2252, 2256, and 2587.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3641] Legg, S., "Generic String Encoding Rules (GSER) for ASN.1 Types", RFC 3641, October 2003.
- [RFC4510] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map", RFC 4510, June 2006.
- [RFC4512] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Directory Information Models", RFC 4512, June 2006.
- [RFC4522] Legg, S., "Lightweight Directory Access Protocol (LDAP): The Binary Encoding Option", RFC 4522, June 2006.
- [X.509] ITU-T, "The Directory: Authentication Framework", X.509(2000).
- [X.521] ITU-T, "The Directory: Selected Object Classes", X.521(2000).
- [X.690] ITU-T, "Specification of ASN.1 encoding rules: Basic Encoding Rules (BER), Canonical Encoding Rules (CER), and Distinguished Encoding Rules (DER)", X.690(2002).

## Definitions and Abbreviations
- **Certificate**: X.509 certificate (syntax OID 1.3.6.1.4.1.1466.115.121.1.8)
- **CertificateList**: X.509 CRL (syntax OID 1.3.6.1.4.1.1466.115.121.1.9)
- **CertificatePair**: X.509 certificate pair (syntax OID 1.3.6.1.4.1.1466.115.121.1.10)
- **SupportedAlgorithm**: X.509 supported algorithm (syntax OID 1.3.6.1.4.1.1466.115.121.1.49)
- **CertificateExactAssertion**: GSER encoding for exact match (syntax OID 1.3.6.1.1.15.1)
- **CertificateAssertion**: GSER encoding for match (syntax OID 1.3.6.1.1.15.2)
- **CertificatePairExactAssertion**: GSER (1.3.6.1.1.15.3)
- **CertificatePairAssertion**: GSER (1.3.6.1.1.15.4)
- **CertificateListExactAssertion**: GSER (1.3.6.1.1.15.5)
- **CertificateListAssertion**: GSER (1.3.6.1.1.15.6)
- **AlgorithmIdentifier**: GSER (1.3.6.1.1.15.7)
- **DER**: Distinguished Encoding Rules [X.690]
- **GSER**: Generic String Encoding Rules [RFC3641]
- **ABNF**: Augmented Backus-Naur Form [RFC4234]

## 1. Introduction
- This document provides LDAP schema definitions for a subset of elements from X.509 and X.521. It obsoletes RFCs 2252, 2256, and 2587.
- Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per BCP 14 [RFC2119]).
- Schema definitions use LDAP description formats [RFC4512].

## 2. Syntaxes

### 2.1. Certificate
- **OID**: 1.3.6.1.4.1.1466.115.121.1.8 DESC 'X.509 Certificate'
- Values of this syntax:
  - SHOULD be DER-encoded.
  - MUST only be transferred using `;binary` transfer option [RFC4522] (e.g., `userCertificate;binary`).
  - MUST be preserved as presented (digitally signed data).

### 2.2. CertificateList
- **OID**: 1.3.6.1.4.1.1466.115.121.1.9 DESC 'X.509 Certificate List'
- Values:
  - SHOULD be DER-encoded.
  - MUST only use `;binary` (e.g., `certificateRevocationList;binary`).
  - MUST be preserved as presented.

### 2.3. CertificatePair
- **OID**: 1.3.6.1.4.1.1466.115.121.1.10 DESC 'X.509 Certificate Pair'
- Values:
  - SHOULD be DER-encoded.
  - MUST only use `;binary` (e.g., `crossCertificatePair;binary`).
  - MUST be preserved as presented.

### 2.4. SupportedAlgorithm
- **OID**: 1.3.6.1.4.1.1466.115.121.1.49 DESC 'X.509 Supported Algorithm'
- Values:
  - SHOULD be DER-encoded.
  - MUST only use `;binary` (e.g., `supportedAlgorithms;binary`).
  - MUST be preserved as presented.

### 2.5. CertificateExactAssertion
- **OID**: 1.3.6.1.1.15.1 DESC 'X.509 Certificate Exact Assertion'
- MUST be GSER-encoded. See Appendix A.1 for ABNF.

### 2.6. CertificateAssertion
- **OID**: 1.3.6.1.1.15.2 DESC 'X.509 Certificate Assertion'
- MUST be GSER-encoded. See Appendix A.2 for ABNF.

### 2.7. CertificatePairExactAssertion
- **OID**: 1.3.6.1.1.15.3 DESC 'X.509 Certificate Pair Exact Assertion'
- MUST be GSER-encoded. See Appendix A.3 for ABNF.

### 2.8. CertificatePairAssertion
- **OID**: 1.3.6.1.1.15.4 DESC 'X.509 Certificate Pair Assertion'
- MUST be GSER-encoded. See Appendix A.4 for ABNF.

### 2.9. CertificateListExactAssertion
- **OID**: 1.3.6.1.1.15.5 DESC 'X.509 Certificate List Exact Assertion'
- MUST be GSER-encoded. See Appendix A.5 for ABNF.

### 2.10. CertificateListAssertion
- **OID**: 1.3.6.1.1.15.6 DESC 'X.509 Certificate List Assertion'
- MUST be GSER-encoded. See Appendix A.6 for ABNF.

### 2.11. AlgorithmIdentifier
- **OID**: 1.3.6.1.1.15.7 DESC 'X.509 Algorithm Identifier'
- MUST be GSER-encoded. See Appendix A.7 for ABNF.

## 3. Matching Rules
All matching rules are intended to act in accordance with their X.500 counterparts.

### 3.1. certificateExactMatch
- **OID**: 2.5.13.34 NAME 'certificateExactMatch' SYNTAX 1.3.6.1.1.15.1
- Compares presented exact assertion with attribute value of certificate syntax (per X.509 clause 11.3.1).

### 3.2. certificateMatch
- **OID**: 2.5.13.35 NAME 'certificateMatch' SYNTAX 1.3.6.1.1.15.2
- Compares presented assertion with attribute value of certificate syntax (per X.509 clause 11.3.2).

### 3.3. certificatePairExactMatch
- **OID**: 2.5.13.36 NAME 'certificatePairExactMatch' SYNTAX 1.3.6.1.1.15.3
- Compares presented exact assertion with attribute value of certificate pair syntax (per X.509 clause 11.3.3).

### 3.4. certificatePairMatch
- **OID**: 2.5.13.37 NAME 'certificatePairMatch' SYNTAX 1.3.6.1.1.15.4
- Compares presented assertion with attribute value of certificate pair syntax (per X.509 clause 11.3.4).

### 3.5. certificateListExactMatch
- **OID**: 2.5.13.38 NAME 'certificateListExactMatch' SYNTAX 1.3.6.1.1.15.5
- Compares presented exact assertion with attribute value of certificate pair syntax (sic; should be certificate list syntax) (per X.509 clause 11.3.5).

### 3.6. certificateListMatch
- **OID**: 2.5.13.39 NAME 'certificateListMatch' SYNTAX 1.3.6.1.1.15.6
- Compares presented assertion with attribute value of certificate pair syntax (sic; should be certificate list syntax) (per X.509 clause 11.3.6).

### 3.7. algorithmIdentifierMatch
- **OID**: 2.5.13.40 NAME 'algorithmIdentifier' (sic: typo 'mating rule') SYNTAX 1.3.6.1.1.15.7
- Compares presented algorithm identifier with attribute value of supported algorithm (per X.509 clause 11.3.7).

## 4. Attribute Types
All attribute types MUST use `;binary` transfer option for their values (per syntax requirements).

### 4.1. userCertificate
- **OID**: 2.5.4.36 NAME 'userCertificate' DESC 'X.509 user certificate' EQUALITY certificateExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.8
- Holds X.509 certificates issued to the user (per X.509 clause 11.2.1). Transferred as `userCertificate;binary`.

### 4.2. cACertificate
- **OID**: 2.5.4.37 NAME 'cACertificate' DESC 'X.509 CA certificate' EQUALITY certificateExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.8
- Holds X.509 certificates issued to the CA (per X.509 clause 11.2.2). Transferred as `cACertificate;binary`.

### 4.3. crossCertificatePair
- **OID**: 2.5.4.40 NAME 'crossCertificatePair' DESC 'X.509 cross certificate pair' EQUALITY certificatePairExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.10
- Holds X.509 certificate pair (per X.509 clause 11.2.3). Transferred as `crossCertificatePair;binary`.

### 4.4. certificateRevocationList
- **OID**: 2.5.4.39 NAME 'certificateRevocationList' DESC 'X.509 certificate revocation list' EQUALITY certificateListExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.9
- Holds CRLs (per X.509 clause 11.2.4). Transferred as `certificateRevocationList;binary`.

### 4.5. authorityRevocationList
- **OID**: 2.5.4.38 NAME 'authorityRevocationList' DESC 'X.509 authority revocation list' EQUALITY certificateListExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.9
- Holds CRLs (per X.509 clause 11.2.5). Transferred as `authorityRevocationList;binary`.

### 4.6. deltaRevocationList
- **OID**: 2.5.4.53 NAME 'deltaRevocationList' DESC 'X.509 delta revocation list' EQUALITY certificateListExactMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.9
- Holds CRLs (per X.509 clause 11.2.6). MUST be transferred as `deltaRevocationList;binary`.

### 4.7. supportedAlgorithms
- **OID**: 2.5.4.52 NAME 'supportedAlgorithms' DESC 'X.509 supported algorithms' EQUALITY algorithmIdentifierMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.49
- Holds supported algorithms (per X.509 clause 11.2.7). MUST be transferred as `supportedAlgorithms;binary`.

## 5. Object Classes

### 5.1. pkiUser
- **OID**: 2.5.6.21 NAME 'pkiUser' SUP top AUXILIARY MAY userCertificate
- For objects that may be subject to certificates (per X.509 clause 11.1.1).

### 5.2. pkiCA
- **OID**: 2.5.6.22 NAME 'pkiCA' SUP top AUXILIARY MAY (cACertificate $ certificateRevocationList $ authorityRevocationList $ crossCertificatePair)
- For objects acting as certificate authorities (per X.509 clause 11.1.2).

### 5.3. cRLDistributionPoint
- **OID**: 2.5.6.19 NAME 'cRLDistributionPoint' SUP top STRUCTURAL MUST cn MAY (certificateRevocationList $ authorityRevocationList $ deltaRevocationList)
- For objects acting as CRL distribution points (per X.509 clause 11.1.3).

### 5.4. deltaCRL
- **OID**: 2.5.6.23 NAME 'deltaCRL' SUP top AUXILIARY MAY deltaRevocationList
- For entries holding delta revocation lists (per X.509 clause 11.1.4).

### 5.5. strongAuthenticationUser
- **OID**: 2.5.6.15 NAME 'strongAuthenticationUser' SUP top AUXILIARY MUST userCertificate
- For objects participating in certificate-based authentication (per X.521 clause 6.15). **Deprecated** in favor of pkiUser.

### 5.6. userSecurityInformation
- **OID**: 2.5.6.18 NAME 'userSecurityInformation' SUP top AUXILIARY MAY supportedAlgorithms
- For additional security information (per X.521 clause 6.16).

### 5.7. certificationAuthority
- **OID**: 2.5.6.16 NAME 'certificationAuthority' SUP top AUXILIARY MUST (authorityRevocationList $ certificateRevocationList $ cACertificate) MAY crossCertificatePair
- For objects acting as CAs (per X.521 clause 6.17). **Deprecated** in favor of pkiCA.

### 5.8. certificationAuthority-V2
- **OID**: 2.5.6.16.2 NAME 'certificationAuthority-V2' SUP certificationAuthority AUXILIARY MAY deltaRevocationList
- Version 2 of certificationAuthority (per X.521 clause 6.18). **Deprecated** in favor of pkiCA.

## 6. Security Considerations
- General certificate considerations [RFC3280] and LDAP security considerations [RFC4510] apply.
- Signed certificate elements only protect integrity of signed data; without LDAP data integrity protections (e.g., IPsec), clients and servers cannot assure request/response integrity. Use authentication and data integrity services in LDAP [RFC4513][RFC4511].

## 7. IANA Considerations
- Object identifier registration for LDAP OID 1.3.6.1.1.15.x (see section 7.1).
- Updated LDAP descriptor registry for all attribute types, matching rules, and object classes defined in this document (see table in section 7.2).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Certificate, CertificateList, CertificatePair, SupportedAlgorithm values MUST only be transferred using `;binary` option | MUST (transfer) | Section 2.1-2.4 |
| R2 | Certificate, CertificateList, CertificatePair, SupportedAlgorithm values MUST be preserved as presented (digitally signed) | MUST (preservation) | Section 2.1-2.4 |
| R3 | Certificate, CertificateList, CertificatePair, SupportedAlgorithm values SHOULD be DER-encoded | SHOULD (encoding) | Section 2.1-2.4 |
| R4 | Assertion syntaxes (CertificateExactAssertion, etc.) MUST be GSER-encoded | MUST (encoding) | Sections 2.5-2.11 |
| R5 | Attribute types userCertificate, cACertificate, crossCertificatePair, certificateRevocationList, authorityRevocationList MUST be transferred using `;binary` | MUST (transfer) | Section 4.1-4.5 |
| R6 | Attribute types deltaRevocationList and supportedAlgorithms MUST be transferred using `;binary` | MUST (transfer) | Section 4.6-4.7 |
| R7 | Object class cRLDistributionPoint MUST have cn | MUST (attribute) | Section 5.3 |
| R8 | Object class strongAuthenticationUser MUST have userCertificate | MUST (attribute) | Section 5.5 |
| R9 | Object class certificationAuthority MUST have authorityRevocationList, certificateRevocationList, cACertificate | MUST (attributes) | Section 5.7 |

## Informative Annexes (Condensed)
- **Appendix A**: Provides ABNF grammars (informative) for GSER-based LDAP-specific encodings of assertion syntaxes and algorithm identifier. Sub-annexes A.1–A.7 correspond to sections 2.5–2.11. Each grammar defines the exact representation per [RFC4234] and [RFC3642].