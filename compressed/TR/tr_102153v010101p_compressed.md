# ETSI TR 102 153: Electronic Signatures and Infrastructures (ESI); Pre-study on certificate profiles
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2003-02 | **Type**: Technical Report (Informative)
**Original**: ETSI, 650 Route des Lucioles, F-06921 Sophia Antipolis Cedex - FRANCE

## Scope
This pre-study investigates major sources of incompatibility among existing certificate profiles (qualified and authentication certificates) and assesses whether a normative task to further profile certificate formats is feasible and meaningful. It concludes that more rigid profiles are necessary for interoperability and proposes a strategy and implementation phases.

## Normative References
- [1] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures.
- [2] IETF RFC 3279: "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", April 2002.
- [3] IETF RFC 3280: "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", April 2002.
- [4] IETF RFC 3039: "Internet X.509 Public Key Infrastructure - Qualified Certificates Profile", January 2001.
- [5] ISO/IEC 9594-8: "Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks", 2001.
- [6] ETSI TS 101 862: "Qualified certificate profile".
- [7] IETF RFC 2459: "Internet X.509 Public Key Infrastructure Certificate and CRL Profile".

## Definitions and Abbreviations
### Definitions
- **Authentication certificate**: Public Key Certificate (PKC) intended for use in an electronic signature serving as a method of authentication (Directive [1], article 2.1).
- **Certification Authority (CA)**: Authority trusted by one or more users to create and assign public key certificates.
- **Public Key Certificate (PKC)**: Data structure containing the public key of an end-entity and other information, digitally signed with the private key of the CA that issued it.
- **Qualified Certificate**: PKC that conforms to Directive [1] annex I and is issued by a CA conforming to annex II of the same Directive.

### Abbreviations
| Abbreviation | Full term |
|---|---|
| CA | Certification Authority |
| CRL | Certificate Revocation List |
| CSP | Certificate Service Provider |
| EESSI | European Electronic Signature Standardization Initiative |
| EIC | Electronic Identity Certificates |
| EID | Electronic Identity Document |
| IETF | Internet Engineering Task Force |
| ISO | International Organization for Standardization |
| PKC | Public Key Certificate |
| PKI | Public Key Infrastructure |
| PKIX | Public Key Infrastructure X.509 based |
| QC | Qualified Certificate |
| ToR | Terms of Reference |

## 4 Implications from the Requirements of the Directive
Directive [1] recitals (5), (7), and (10) stress the need for interoperability to ensure free movement within the internal market and build trust in electronic signatures. Interoperability pillars include: certificate profile, signature formats, certificate status information, CSP status information, and time stamping. Both qualified and non-qualified certificates (Article 5) face interoperability issues, but this study focuses on two types: certificates for qualified signatures and authentication certificates (peer entity authentication and data origin authentication).

## 5 Documents Scrutinized
The following profiles were analysed (see original table for full details):
- A-Trust (Austria)
- FINEID S4-1, S4-2 (Finland)
- Common ISIS-MTT (Germany)
- Svensk Standard (Sweden)
- SmartTrust (Sweden)
- Italian pre-Directive profile (Italy)
*(Other profiles were considered but not exhaustively examined after sufficient evidence of incompatibility was found.)*

## 6 Analysis Outcomes
### 6.1 Profile Comparison
The following table summarises key characteristics and discrepancies among the examined certificate profiles. *(Only major differences are shown; the original contains full detail.)*

| Field / Extension | ISIS-MTT | A-Trust | Svensk Standard | SmartTrust | FINEID | Italian pre-Directive |
|---|---|---|---|---|---|---|
| **SerialNumber max length** | 20 octets | 16 bytes | 8 bytes | 16 bytes | 8 bytes | 20 octets (RFC 2459) |
| **Signature Algorithm** | SHA1withRSA (RIPEMD-160 optional) | SHA1withRSA | MD5withRSA | SHA1withRSAEncryption | SHA1withRSAEncryption | SHA1withRSAEncryption |
| **Issuer DN** | MUST: countryName, organizationName; SHOULD: commonName, organizationalUnitName | countryName, organizationName, commonName | countryName, organizationName, commonName | countryName, organizationName, commonName | countryName, organizationName, commonName | As per RFC 2459 |
| **Subject DN** | MUST: commonName, countryName, surname, givenName, serialNumber | title, surname, givenName, commonName, serialNumber | countryName, surname, givenName, commonName, serialNumber | countryName, surname, givenName, commonName, serialNumber | countryName, surname, givenName, serialNumber | countryName, surname, givenName, commonName, serialNumber; commonName includes fiscal code |
| **SubjectKeyIdentifier** | SHA-1 hash of public key | 4-bit type field + least sig. 60 bits of SHA-1 | same as A-Trust | same as A-Trust | same as A-Trust | No preference (RFC 2459) |
| **KeyUsage** | NonRepudiation (signature); digitalSignature (auth.); keyEncipherment (encryption) | NonRepudiation; optionally digitalSignature | NonRepudiation or digitalSignature+keyEncipherment | NonRepudiation | NonRepudiation; authentication + encipherment separate certificates | NonRepudiation + authentication+encipherment (three key pairs) |
| **BasicConstraints** | cA=false, non-critical | cA=false, non-critical | cA=false, non-critical | cA=false, non-critical | cA=false, non-critical | Not used in end-entity certs |
| **CertificatePolicies** | mandatory policyIdentifier, optional policyQualifiers | mandatory policyIdentifier+policyQualifiers | mandatory policyIdentifier+policyQualifiers | mandatory policyIdentifier+policyQualifiers | mandatory policyIdentifier+policyQualifiers | mandatory policyIdentifier+CPS URL |
| **CRLDistributionPoints** | distributionPoint, non-critical | distributionPoint, non-critical | distributionPoint, non-critical | distributionPoint, non-critical | distributionPoint, non-critical | Mandatory CRL access URL |
| **ExtKeyUsage** | critical/non-critical | emailProtection (removing) | SHALL NOT be used | SHOULD NOT appear | - | Not defined |
| **SubjectDirectoryAttributes** | SHOULD NOT be used | optional | SHALL NOT be used | forbidden | - | Not addressed |
| **QcStatements (private)** | Optional | optional | critical | optional | qcCompliance mandatory | Not present |
| **AuthorityInfoAccess** | If OCSP, MUST contain URL | non-critical | non-critical | non-critical | - | Not present |
| **Cardnumber** | optional | optional | - | - | - | Not present |
| **BiometricData** | optional | optional | - | - | - | Not present |

### 6.2 Profiles Inconsistencies
**Severity levels**: 1 = outright incompatibility; 2 = difficult for verification applications; 3 = minor.

| # | Inconsistency | Sev. | Comments |
|---|---|---|---|
| 1 | CertificateSerialNumber field length | 3 | Ranges 8–20 bytes; easily handled but uniformity preferred. |
| 2 | Allowed Signature Algorithms | 1 | All support SHA1withRSA, but two accept RIPEMD-160 and one accepts MD5. MD5 is discouraged; RIPEMD-160 has limited use (RFC 3279). Proposed: avoid MD5 and RIPEMD-160. |
| 3 | Issuer | 2 | CommonName is required by many profiles but RFC 3039 says additional attributes MAY be present but SHOULD NOT be necessary. Risk of incompatibility unless modified. |
| 4 | Subject | 1 | Wide variation in inclusion of commonName, serialNumber, etc. Likely non-interoperability. |
| 5 | KeyIdentifier (Subject and Authority) | 2 | 5 profiles use one calculation method, 1 uses another, 1 has no preference. Single method preferable. |
| 6 | BasicConstraints | 3 | Specifying cA=false is unnecessary (default). Skipping it simplifies handling. |
| 7 | KeyUsage | 1 | Different approaches: some define only nonRepudiation; others combine authentication/encryption; SSL/TLS client auth may conflict. Further investigation needed. |
| 8 | SubjectDirectoryAttributes | 1 | Forbidden in two profiles, discouraged in another, but needed for attributes like dateOfBirth, placeOfBirth. Further investigation needed. |
| 9 | Private extensions | 3 | Still immature; no definite assessment possible. |

### 6.2.2 Comments on the Findings
Major concerns: non-full interoperability among certificates and questionable choices (especially authentication certificate profiles). Both may cause problems in cross-border signed document exchange and mutual recognition of electronic identification. Thorough investigation across EU Member States is recommended.

## 7 Proposed Strategy and Implementation Phases
A task force shall be charged with developing certificate profiles that:
1. Achieve acceptance and consensus throughout Europe.
2. Leave open only options that do not cause interoperability issues of severity >3.
3. Meet recognized specifications: ISO/IEC 9594-8 (2001), RFC 3039, RFC 3279, RFC 3280, TS 101 862.
4. Achieve consensus on best-practice formats.

Implementation specifications:
- Team members must have political clout, diplomatic skill, and technical knowledge. EESSI SG may be involved.
- Interoperability issues likely arise from misunderstanding of existing standards, not the standards themselves. Joint investigation with national bodies required.
- If amendments to standards are needed, they must achieve consensus before being proposed to IETF PKIX.
- New/revised profiles shall be defined, achieve TC ESI consensus, then be submitted for approval to involved bodies.
- A harmonized phase-in/phase-out plan will be worked out with all relevant bodies.
- The outcome shall be a new ETSI Technical Specification.

## Requirements Summary
| ID | Requirement/Recommendation | Type | Reference |
|---|---|---|---|
| R1 | More rigid certificate profiles are necessary for interoperability. | Recommendation | Section 7 |
| R2 | Discourage use of RIPEMD-160 and avoid MD5. | Recommendation | Inconsistency #2 |
| R3 | Single method for keyIdentifier calculation is highly preferable. | Recommendation | Inconsistency #5 |
| R4 | Investigate proper combined use of nonRepudiation and digitalSignature. | Recommendation | Inconsistency #7 |
| R5 | SubjectDirectoryAttributes to store additional user information (e.g., dateOfBirth) should be allowed and harmonised. | Recommendation | Inconsistency #8 |
| R6 | A task force shall develop certificate profiles meeting the stated criteria. | Shall (for task force) | Section 7 |
| R7 | Phase-in/phase-out plan shall be agreed with all Member States bodies. | Shall | Section 7 |
| R8 | Outcome shall be a new ETSI Technical Specification. | Shall | Section 7 |

## Annexes (Informative, Condensed)
- **Annex A: Participation to the task**: Lists volunteers (name, country, organization) who contributed to the study (see original for full table).