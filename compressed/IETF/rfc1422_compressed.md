# RFC 1422: Privacy Enhancement for Internet Electronic Mail: Part II: Certificate-Based Key Management
**Source**: IAB IRTF PSRG, IETF PEM | **Version**: RFC 1422 (obsoletes RFC 1114) | **Date**: February 1993 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc1422

## Scope (Summary)
This document defines a key management architecture and infrastructure based on public-key certificates to provide keying information for Privacy Enhanced Mail (PEM) and other protocols. It establishes a single root certification authority (IPRA), Policy Certification Authorities (PCAs), and Certification Authorities (CAs), with procedures for certificate issuance, revocation, and validation.

## Normative References
- CCITT Recommendation X.411 (1988), "Message Handling Systems: Message Transfer System"
- CCITT Recommendation X.509 (1988), "The Directory - Authentication Framework"
- CCITT Recommendation X.520 (1988), "The Directory - Selected Attribute Types"
- RFC 1421, "Privacy Enhancement for Internet Electronic Mail: Part I: Message Encryption and Authentication Procedures"
- RFC 1423, "Privacy Enhancement for Internet Electronic Mail: Part III: Algorithms, Modes, and Identifiers"
- RFC 1424, "Privacy Enhancement for Internet Electronic Mail: Part IV: Notary, Co-Issuer, CRL-Storing and CRL-Retrieving Services"
- RFC 1417, "NADF Standing Documents: A Brief Overview"
- RFC 1255, "A Naming Scheme for c=US"
- NIST SP 500-183 (1990)

## Definitions and Abbreviations
- **Public-key certificate (certificate)**: A data structure containing the subject name, public component, issuer name, validity period, and signature, binding the public component to the subject.
- **Certificate Revocation List (CRL)**: A time-stamped list of revoked certificates issued by a CA.
- **Distinguished Name (DN)**: An X.500 directory name used to identify subjects and issuers.
- **IPRA**: Internet Policy Registration Authority – the root of the certification hierarchy.
- **PCA**: Policy Certification Authority – a CA certified by the IPRA that defines and publishes its certification policies.
- **CA**: Certification Authority – an entity certified by a PCA that issues certificates to users or subordinate CAs.
- **UA**: User Agent – software that processes PEM messages.
- **MIC**: Message Integrity Code – a hash value used for integrity and authentication.
- **DEK**: Data Encryption Key – a symmetric key used to encrypt message content.
- **CIC**: Certificate Integrity Check – hash algorithm used for signature verification.
- **RSA**: A public-key cryptosystem (patented in the US) anticipated as the primary signature algorithm.
- **PERSONA CA**: A CA that issues certificates without vouching for the subject's identity, for anonymity.
- **Residential CA**: A CA that issues certificates to users independent of organizational affiliation.

## 1. Executive Summary (Condensed)
This document defines the key management infrastructure for PEM, based on X.509 but adding a single root (IPRA), PCAs with published policies, and a certification hierarchy. It addresses the need for uniform automated validation, simple authentication, and near-term operation without ubiquitous X.500 directories. The RSA algorithm is expected to be the primary signature algorithm; licensing arrangements are noted.

## 2. Overview of Approach (Condensed)
Public-key certificates bind a user's public component to its DN, signed by an issuer. Certificates are validated recursively up to the IPRA root. They are used in PEM for encrypting DEKs and verifying MICs. CRLs are checked to ensure certificates are not revoked. The originator may include its full certification path in the message header.

## 3. Architecture
### 3.1 Scope and Restrictions
The architecture defines procedures for registering CAs and users, generating certificates and CRLs. It imposes a certification hierarchy with the IPRA at the root, followed by PCAs, then CAs. The hierarchy is largely isomorphic to the X.500 naming hierarchy, except that the IPRA forms the root and PCAs define policy subtrees. Only PCAs are certified by the IPRA; each CA's certification path traces to a PCA. If a CA is certified by multiple PCAs, each certificate must contain a distinct public component. This architecture is a compatible subset of X.509.

### 3.2 Relation to X.509 Architecture
The document interprets X.509 certificate mechanisms for PEM, using a subset of X.509 that adds policy semantics. (Informative)

### 3.3 Certificate Definition
A certificate contains:
1. version (default 0 for 1988)
2. serial number
3. signature (algorithm ID and parameters)
4. issuer name (DN)
5. validity period (start and end UTCT time)
6. subject name (DN)
7. subject public key (algorithm ID and key data)

#### 3.3.1 Version Number
The initial version is 0 (1988). PEM implementations **should** accept later versions endorsed by CCITT/ISO.

#### 3.3.2 Serial Number
An issuer **must** ensure that no two distinct certificates with the same issuer DN have the same serial number. This applies even when certification is distributed or the same issuer DN is certified under different PCAs. All PEM UA implementations **must** process serial numbers at least 128 bits in length; size-independent support is encouraged.

#### 3.3.3 Signature
Specifies the algorithm used by the issuer to sign the certificate. The signature is validated to ensure integrity. RFC 1423 defines algorithm IDs.

#### 3.3.4 Subject Name
The subject DN is the identity bound to the public key. If already registered in an X.500 directory, that DN is used.

#### 3.3.5 Issuer Name
The issuer DN identifies the CA that signed the certificate. If an issuer is certified by multiple PCAs, different certificates may contain different public components; in such cases, validation may require trying multiple public components.

#### 3.3.6 Validity Period
Contains start and end UTCT times. Duration may vary per user. Times **should** be expressed in Zulu (GMT) with granularity no finer than minutes.

#### 3.3.7 Subject Public Key
Carries the public component, algorithm ID, and parameters. Algorithm identifiers are specified in RFC 1423.

### 3.4 Roles and Responsibilities
#### 3.4.1 Users and User Agents
##### 3.4.1.1 Generating and Protecting Component Pairs
The UA **must** protect the private component from disclosure. It is recommended that users generate their own key pairs using secure software. The private component **must not** be accessible to any certification authority. Users may possess multiple certificates with the same or different public components; the UA **should** support this.

##### 3.4.1.2 User Registration
User registration is a local matter subject to CA and PCA policies. The user **must** provide its public component and distinguished name to the CA. The CA validates identity according to PCA policy.

##### 3.4.1.3 CRL Management
CRL management is local but critical. Every PEM UA **must** provide a facility for requesting CRLs from a database (accessed via email per RFC 1424). The UA **must** include a configuration parameter for mailbox addresses from which CRLs may be retrieved. Every PEM UA **must** be capable of processing CRLs distributed via PEM messages (RFC 1421). CRLs received **must** be validated before processing against cached certificates. The UA **must** retain CRLs from the IPRA, PCAs, and CAs to screen incoming messages.

##### 3.4.1.4 Facilitating Interoperation
Every PEM UA **must** be capable of including a full originator certification path (user's certificate and all superior certificates back to the IPRA) in a PEM message. The UA **may** send less than a full path, but **must** provide a user capability to force transmission of a full certification path.

#### 3.4.2 The Internet Policy Registration Authority (IPRA)
The IPRA is the root of the certification hierarchy, operated under the Internet Society. It certifies only PCAs.

##### 3.4.2.1 PCA Registration
Each PCA **must** file a policy statement with the IPRA, which will be published as an informational RFC. A signed copy (MIC-ONLY message) will be available via email. Authorization is signified by publication and issuance of a certificate. Each PCA **must** execute a legal agreement and pay a fee. The IPRA will take reasonable precautions to verify PCA DNs.

##### 3.4.2.2 Ensuring Uniqueness of Distinguished Names
No two distinct entities **must** have the same DN. The IPRA will maintain databases (hashed DN, public key, PCA DN, timestamp) to detect potential duplicates. PCAs **must** query the database before certifying a CA. The database ensures uniqueness of (CA DN hash + public component) pairs. PCAs **must** resolve conflicts. For residential CAs, duplicate DNs are tolerated temporarily, but they **must** use the database and coordinate to avoid duplicate serial numbers.

##### 3.4.2.3 Accuracy of Distinguished Names
The IPRA will make reasonable efforts to verify PCA DNs. Each PCA is expected to make a good faith effort to verify CA DNs and ensure consistency with national standards.

##### 3.4.2.4 Distinguished Name Conventions
The IPRA certifies only PCAs; PCAs certify only CAs; CAs issue certificates for users or subordinate CAs. Subject DNs in certificates issued by a CA **must** be subordinate to the issuer's DN (unless cross-certificates). DN attributes **should** have printable representations.

##### 3.4.2.5 CRL Management
Every PCA and CA **must** issue a CRL upon inception. The IPRA will maintain a CRL for PCAs, updated monthly. Each PCA **must** provide robust database access to CRLs for its domain. CRLs will be accessible via email (RFC 1424).

##### 3.4.2.6 Public Key Algorithm Licensing Issues
The IPRA will not grant licenses for signature algorithms; it will obtain licenses for itself. Each PCA **must** represent that it has obtained any required licenses (e.g., RSA in the US) for its operations.

#### 3.4.3 Policy Certification Authorities (PCAs)
A PCA's policy statement **must** address:
1. PCA Identity (DN, contact info, effective date/duration)
2. PCA Scope (types of CAs: organizational, residential, PERSONA; whether PCA operates CAs directly)
3. PCA Security & Privacy (technical and procedural measures for key generation/protection, privacy of collected information)
4. Certification Policy (procedures for verifying CA identity/right to DN, requirements for user identity validation, DN conflict resolution procedures, maximum validity intervals)
5. CRL Management (frequency of scheduled CRLs, constraints on CA CRL issuance, mailbox for CRL submission and queries)
6. Naming Conventions (any additional DN conventions)
7. Business Issues (legal agreements, fees)
8. Other (any additional relevant topics)

#### 3.4.4 Certification Authorities (CAs)
CAs **must** maintain a database of certified DNs and avoid duplicate certification. The private component of a CA **must** be afforded high security.

##### 3.4.4.1 Organizational CAs
CAs representing organizations certify entities with organizational affiliation. Subject DN must be subordinate to issuer DN.

##### 3.4.4.2 Residential CAs
Residential CAs certify users without organizational affiliation. Duplicate CA DNs are tolerated temporarily; they **must** use the IPRA's conflict detection database and coordinate to avoid duplicate serial numbers.

##### 3.4.4.3 PERSONA CAs
PERSONA CAs issue certificates without vouching for identity. Subject DN is a form of organizational user certificate, not residential. The CA **must** ensure it does not issue duplicate subject DNs. The CA **must** establish procedures for revocation by the certificate holder.

##### 3.4.4.4 CA Responsibilities for CRL Management
Each CA **must** maintain a CRL containing entries for all revoked certificates it issued. Each PCA **must** maintain a CRL for revoked CA certificates in its domain. Each CA **must** supply its current CRL to its PCA in accordance with PCA rules.

### 3.5 Certificate Revocation
#### 3.5.1 X.509 CRLs
Primary reasons for revocation: private component compromise or change of user affiliation. The PEM architecture adds a "next scheduled issue date" to CRLs. A CA **must** issue a new CRL on or before the next scheduled date, even if no changes.

#### 3.5.2 PEM CRL Format
A CRL contains:
1. signature
2. issuer DN
3. last update (UTCT time)
4. next update (UTCT time)
5. revoked certificates (sequence of serial number and revocation date)

Revocation date indicates when the CA formally acknowledged the report.

### 3.6 Certificate Validation
#### 3.6.1 Validation Basics
Every UA **must** contain the public component of the IPRA. PCA certificates **must not** be automatically cached; the user **must** explicitly direct caching. Validation begins with verifying the signature using the issuer's public component, recursively up to the IPRA. It is recommended that each PCA sign certificates for all CAs in its domain to allow rapid termination.

#### 3.6.2 Display of Certificate Validation Data
PEM implementations **must** provide a means to bind native mail system identifiers to DNs. For human users, the full DN of the originator **should** be displayed. The essential requirement is that the ultimate recipient can ascertain the identity based on PEM certification, not unauthenticated information. Every PEM implementation **must** provide a user with the ability to display the full certification path for any certificate upon demand.

#### 3.6.3 Validation Procedure Details
Every PEM implementation **must** perform the following validation steps for every public component used in submitting an ENCRYPTED message or delivering any PEM message:
- Construct a certification path to the IPRA's public component.
- Check validity interval for every certificate in the path; at minimum, warn the user if any certificate fails.
- Check each certificate against the current CRL from the issuer; if the UA does not have access to the current CRL, the user **must** be warned.
- If any revoked certificates are encountered in the path, warn the user (recommended to require positive response).
- Subject DN of every certificate **must** be subordinate to the issuer DN, except if the issuer is the IPRA or a PCA. Non-compliant certificates are invalid and **must** be rejected; the user **must** be notified of this fatal error.
- Certificate caches **must** retain serial number, validity interval, and all certificate information.
- For non-human processes, PEM implementations **must** provide parameters to specify whether validation succeeds/fails under warning conditions.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | An issuer must ensure no two distinct certificates with the same issuer DN have the same serial number. | shall | Section 3.3.2 |
| R2 | All PEM UA implementations must be capable of processing serial numbers at least 128 bits in length. | shall | Section 3.3.2 |
| R3 | Every PEM UA must provide a facility for requesting CRLs from a database. | shall | Section 3.4.1.3 |
| R4 | The UA must include a configuration parameter specifying one or more mailbox addresses from which CRLs may be retrieved. | shall | Section 3.4.1.3 |
| R5 | Every PEM UA must be capable of processing CRLs distributed via PEM messages. | shall | Section 3.4.1.3 |
| R6 | CRLs received must be validated before being processed against cached certificates. | shall | Section 3.4.1.3 |
| R7 | The UA must retain CRLs from IPRA, PCAs, and CAs to screen incoming messages. | shall | Section 3.4.1.3 |
| R8 | Every PEM UA must be capable of including a full originator certification path in a PEM message. | shall | Section 3.4.1.4 |
| R9 | A UA providing optimization of certification path must also provide a user capability to force transmission of a full path. | shall | Section 3.4.1.4 |
| R10 | The IPRA will certify only PCAs. | shall | Section 3.4.2 |
| R11 | Each PCA must file a policy statement published as an informational RFC. | shall | Section 3.4.2.1 |
| R12 | Each PCA must execute a legal agreement and pay a fee. | shall | Section 3.4.2.1 |
| R13 | No two distinct entities must have the same DN. | shall | Section 3.4.2.2 |
| R14 | PCAs must query the IPRA database before certifying a CA to detect DN conflicts. | shall | Section 3.4.2.2 |
| R15 | PCAs must resolve DN conflicts when database indicates potential duplicates. | shall | Section 3.4.2.2 |
| R16 | Each PCA must represent that it has obtained any required licenses for signature algorithms. | shall | Section 3.4.2.6 |
| R17 | The PCA policy statement must address the eight specified topics. | shall | Section 3.4.3 |
| R18 | CAs must maintain a database of certified DNs and avoid duplicate certification. | shall | Section 3.4.4 |
| R19 | The private component of a CA must be afforded high security. | shall | Section 3.4.4 |
| R20 | Subject DNs in certificates issued by a CA must be subordinate to issuer DN (except IPRA/PCA). | shall | Section 3.4.2.4, 3.4.4.1 |
| R21 | Residential CAs must employ the IPRA's DN conflict detection database and coordinate to avoid duplicate serial numbers. | shall | Section 3.4.4.2 |
| R22 | PERSONA CAs must ensure they do not issue duplicate subject DNs. | shall | Section 3.4.4.3 |
| R23 | PERSONA CAs must establish procedures for revocation by certificate holder. | shall | Section 3.4.4.3 |
| R24 | Each CA must maintain a CRL containing entries for all revoked certificates it issued. | shall | Section 3.4.4.4 |
| R25 | Each CA must supply its current CRL to its PCA. | shall | Section 3.4.4.4 |
| R26 | Each PCA must maintain a CRL for revoked CA certificates in its domain. | shall | Section 3.4.4.4 |
| R27 | A CA must issue a new CRL on or before the next scheduled date, even if no changes. | shall | Section 3.5.1 |
| R28 | Every UA must contain the public component of the IPRA as the root for certificate validation. | shall | Section 3.6.1 |
| R29 | PCA certificates must not be automatically cached; user must explicitly direct caching. | shall | Section 3.6.1 |
| R30 | Every PEM implementation must provide a user with the ability to display the full certification path for any certificate upon demand. | shall | Section 3.6.2 |
| R31 | Every PEM implementation must perform validation steps for every public component (ENCRYPTED message submission and all PEM message delivery). | shall | Section 3.6.3 |
| R32 | Certificate caches must retain serial number, validity interval, and all certificate information. | shall | Section 3.6.3 |
| R33 | For non-human processes, PEM implementations must provide parameters to specify whether validation succeeds/fails under warning conditions. | shall | Section 3.6.3 |
| R34 | Subject DN of every certificate must be subordinate to the issuer DN, except IPRA or PCA. Non-compliant certificates are invalid and must be rejected; user must be notified. | shall | Section 3.6.3 |
| R35 | The UA must at minimum warn the user if any certificate in the path fails validity interval check. | shall | Section 3.6.3 |
| R36 | If UA does not have access to current CRL for any certificate in the path, user must be warned. | shall | Section 3.6.3 |

## Informative Annexes (Condensed)
- **Appendix A: ASN.1 Syntax for Certificates and CRLs**: Provides the ASN.1 definitions for `Certificate` and `CertificateRevocationList` structures as used in PEM. The certificate includes version, serial number, signature, issuer, validity, subject, and subjectPublicKeyInfo. The CRL includes signature, issuer, lastUpdate, nextUpdate, and revokedCertificates sequence. Distinguished encoding rules (DER) must be applied before signing.
- **Patent Statement**: Notes that PEM relies on patented public key encryption (RSA, Diffie-Hellman, etc.). Public Key Partners (PKP) has granted assurance of reasonable, nondiscriminatory licensing terms, documented in RFC 1170.
- **Security Considerations**: Entire document is about security.