# ETSI TS 102 280 V1.1.1: X.509 V.3 Certificate Profile for Certificates Issued to Natural Persons
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2004-03 | **Type**: Normative Technical Specification
**Original**: [ETSI TS 102 280 V1.1.1 (2004-03)]

## Scope (Summary)
Defines a common profile for ITU-T X.509 v3 certificates issued to natural persons, enabling interoperability for qualified electronic signatures, peer entity authentication, and data authentication. Profiles are based on RFC 3280, RFC 3739, and TS 101 862; excludes application/protocol-specific content (e.g., IPsec, S/MIME).

## Normative References
- [1] Directive 1999/93/EC (Electronic Signatures)
- [2] ITU-T X.509 / ISO/IEC 9594-8
- [3] IETF RFC 3280: Internet X.509 PKI Certificate and CRL Profile
- [4] IETF RFC 3739: Qualified Certificates Profile
- [5] ETSI TS 101 862: Qualified Certificate profile
- [6] IETF RFC 2119: Key words for Requirement Levels
- [7] IETF RFC 3279: Algorithms and Identifiers for X.509 PKI
- [8] ETSI SR 002 176: Algorithms and Parameters for Secure Electronic Signatures
- [9] IETF RFC 2616: HTTP/1.1
- [10] IETF RFC 2255: LDAP URL Format
- [11] IETF RFC 2560: Online Certificate Status Protocol - OCSP
- [12] IEEE 802.1x: Port Based Network Access Control
- [13] RFC 2459 (superseded by RFC 3280, referenced in annex)

## Abbreviations
CA – Certification Authority  
CRL – Certificate Revocation List  
DS – Digital Signature  
KEA – Key Encipherment or Agreement  
NR – Non-Repudiation  
OCSP – Online Certificate Status Protocol  
OID – Object Identifier  

## Terminology
Key words (MUST, SHALL, SHOULD, MAY, etc.) as per RFC 2119 [6].

## 4 Document Structure and Terminology
### 4.1 Document Structure
- Clause 5 contains profiling requirements (normative). Does not repeat base requirements from referenced standards.
- Annex A (informative) lists important requirements from referenced standards for convenience.

### 4.2 Terminology
Interpretation per RFC 2119.

## 5 Profile Requirements
### 5.1 Generic Requirements
- All certificate fields and extensions SHALL comply with RFC 3280, RFC 3739, and TS 101 862 except as amended herein.
- "No specific requirements" means no additional beyond those standards.
- In case of discrepancy, this document is normative.

### 5.2 Basic Certificate Fields
#### 5.2.1 Version
- SHALL be X.509 v3 certificates.

#### 5.2.2 Serial number
- No specific requirements.

#### 5.2.3 Signature
- Algorithm SHALL be per RFC 3279 and SR 002 176.
- Strongly RECOMMENDED to use sha1WithRSAEncryption for maximum interoperability.

#### 5.2.4 Issuer
- Identity SHALL use an appropriate subset of: countryName, organizationName, organizationalUnitName (multiple allowed), stateOrProvinceName, localityName, commonName, serialNumber, domainComponent.
- Additional attributes MAY be present but SHOULD NOT be necessary to identify the issuing organization.
- countryName and organizationName SHALL be present.
- organizationName SHALL contain full registered name; countryName SHALL contain country of registration.
- domainComponent attributes indicating a different country than countryName are disregarded for determining country of registration.

#### 5.2.5 Validity
- No specific requirements.

#### 5.2.6 Subject
- SHALL contain an appropriate subset of: domainComponent, countryName, commonName, surname, givenName, serialNumber, title, organizationName, organizationalUnitName, stateOrProvinceName, localityName.
- Other attributes MAY be present but SHALL NOT be necessary to distinguish the subject name within the issuer domain.
- SHALL include at least one of: Choice I: commonName; Choice II: givenName and surname.

#### 5.2.7 Subject Public Key Info
- SHALL be per RFC 3279 and SR 002 176.
- Strongly RECOMMENDED to use rsaEncryption for maximum interoperability.

### 5.3 X.509 Version 2 Certificate Fields
- Issuer and Subject Unique Identifier SHALL NOT be present.

### 5.4 Standard Certificate Extensions
#### 5.4.1 Authority Key Identifier
- SHALL be present, containing a key identifier for the issuing CA's public key.

#### 5.4.2 Subject Key Identifier
- No specific requirements.

#### 5.4.3 Key Usage
- Named types (bits):

| Type | NR (bit 1) | DS (bit 0) | KEA (bit 2 or 4) |
|------|------------|------------|------------------|
| A    | X          |            |                  |
| B    | X          | X          |                  |
| C    |            | X          |                  |
| D    |            | X          | X                |
| E    |            |            | X                |

- For certificates validating commitment to signed content (e.g., electronic signatures on agreements/transactions), key usage SHALL be limited to type A or B (NR bit set). RECOMMENDED to use type A only.
- For all other certificates, SHALL be limited to type C, D, or E.
- If a Qualified Certificate per TS 101 862, SHALL be limited to type A, B, or C.
- (Security note on combining NR with other bits is preserved in condensed form below.)

#### 5.4.4 Private Key Usage Period
- No specific requirements.

#### 5.4.5 Certificate Policies
- SHOULD NOT be marked critical.

#### 5.4.6 Policy Mappings
- Not applicable to end entity certificates.

#### 5.4.7 Subject Alternative Name
- SHALL NOT be marked critical.

#### 5.4.8 Issuer Alternative Name
- SHALL NOT be marked critical.

#### 5.4.9 Subject Directory Attributes
- If present, SHALL NOT store any identification attributes listed in clause 5.2.6.

#### 5.4.10 Basic Constraints
- No specific requirements.

#### 5.4.11 Name Constraints
- Not applicable to end entity certificates.

#### 5.4.12 Policy Constraints
- Not applicable to end entity certificates.

#### 5.4.13 Extended Key Usage
- SHALL NOT be marked critical.

#### 5.4.14 CRL Distribution Points
- SHALL be present.
- At least one reference to a publicly available CRL SHALL be present.
- At least one reference SHALL use http:// or ldap:// scheme.
- SHALL NOT be marked critical.
- CAs MAY support OCSP in addition.

#### 5.4.15 Inhibit any-policy
- Not applicable to end entity certificates.

#### 5.4.16 Freshest CRL
- No specific requirements.

### 5.5 RFC 3280 Internet Certificate Extensions
#### 5.5.1 Authority Information Access
- SHOULD include an accessMethod OID id-ad-caIssuers with at least one accessLocation specifying a valid CA certificate of the issuing CA.
- At least one accessLocation SHOULD use http://.
- MAY be ignored for self-signed root CA certificates.

#### 5.5.2 Subject Information Access
- No specific requirements.

### 5.6 RFC 3739 Certificate Extensions
#### 5.6.1 Biometric Information
- No specific requirements.

#### 5.6.2 Qualified Certificate Statement
- Certificates declared as Qualified Certificates SHALL comply with TS 101 862.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Certificates SHALL be X.509 v3 | shall | 5.2.1 |
| R2 | Signature algorithm per RFC 3279 and SR 002 176 | shall | 5.2.3 |
| R3 | Issuer field SHALL include countryName and organizationName; organizationName SHALL be full registered name | shall | 5.2.4 |
| R4 | Subject field SHALL include at least commonName or (givenName and surname) | shall | 5.2.6 |
| R5 | Version 2 unique identifiers SHALL NOT be present | shall | 5.3 |
| R6 | Authority key identifier extension SHALL be present | shall | 5.4.1 |
| R7 | Key usage restricted per type definitions for commitment or others | shall | 5.4.3 |
| R8 | CRL distribution points extension SHALL be present with at least one HTTP or LDAP reference | shall | 5.4.14 |
| R9 | For Qualified Certificates, key usage limited to type A, B, or C | shall | 5.4.3 |
| R10 | Certificate policies extension SHOULD NOT be critical | should | 5.4.5 |
| R11 | Subject/Issuer alternative name SHALL NOT be critical | shall | 5.4.7-8 |
| R12 | Subject directory attributes SHALL NOT store identification attributes from 5.2.6 | shall | 5.4.9 |
| R13 | Authority Information Access SHOULD include id-ad-caIssuers with HTTP location | should | 5.5.1 |
| R14 | Qualified Certificate statement per TS 101 862 | shall | 5.6.2 |
| R15 | Policy mappings, name constraints, policy constraints, inhibit any-policy not applicable to end entity | – | 5.4.6, 5.4.11-12, 5.4.15 |

## Informative Annexes (Condensed)
- **Annex A (informative)**: Lists important requirements from referenced standards (RFC 3280, RFC 3739, RFC 3279, TS 101 862) for convenience. Provides exact requirement text for serial number, signature algorithm, issuer/subject encoding, validity date encoding, public key OIDs, authority/subject key identifier, key usage rules, certificate policies, policy mappings, subject alternative name, subject directory attributes, basic constraints, name constraints, policy constraints, CRL distribution points, inhibit any-policy, freshest CRL, authority information access (including OCSP), subject information access, biometric information, and qualified certificate statement. Referenced standards are necessary for full understanding.