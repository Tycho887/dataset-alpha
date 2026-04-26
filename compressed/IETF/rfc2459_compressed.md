# RFC 2459: Internet X.509 Public Key Infrastructure Certificate and CRL Profile
**Source**: IETF / Standards Track | **Version**: RFC 2459 | **Date**: January 1999 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc2459

## Scope (Summary)
This document profiles the X.509 v3 certificate and X.509 v2 CRL for use in the Internet. It describes certificate and CRL formats, standard extensions, a required set of extensions, certificate path validation, and algorithm support (RSA, DSA, Diffie-Hellman). ASN.1 modules and examples are provided.

## Normative References
- [X.509] ITU-T Rec. X.509 (1997)
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC 1422] Kent, S., "Privacy Enhancement for Internet Electronic Mail: Part II: Certificate-Based Key Management", RFC 1422, February 1993.
- [X.501] ITU-T Rec. X.501 (1993)
- [X.520] ITU-T Rec. X.520 (1993)
- [X.208] CCITT Rec. X.208 (1988)
- [RFC 2313] Kaliski, B., "PKCS #1: RSA Encryption Version 1.5", RFC 2313, March 1998.
- [FIPS 180-1] FIPS PUB 180-1, Secure Hash Standard, 17 April 1995.
- [FIPS 186] FIPS PUB 186, Digital Signature Standard, 18 May 1994.
- [RFC 791] Postel, J., "Internet Protocol", STD 5, RFC 791, September 1981.
- [RFC 822] Crocker, D., "Standard for the format of ARPA Internet text messages", STD 11, RFC 822, August 1982.
- [RFC 1034] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- [RFC 1319] Kaliski, B., "The MD2 Message-Digest Algorithm", RFC 1319, April 1992.
- [RFC 1321] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [RFC 1519] Fuller, V., et al., "Classless Inter-Domain Routing (CIDR)", RFC 1519, September 1993.
- [RFC 1738] Berners-Lee, T., et al., "Uniform Resource Locators (URL)", RFC 1738, December 1994.
- [RFC 1778] Howes, T., et al., "The String Representation of Standard Attribute Syntaxes", RFC 1778, March 1995.
- [RFC 1883] Deering, S. and R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", RFC 1883, December 1995.
- [RFC 2247] Kille, S., et al., "Using Domains in LDAP/X.500 Distinguished Names", RFC 2247, January 1998.
- [X9.55] ANSI X9.55-1995.
- [X9.42] ANSI X9.42-199x (Working Draft, December 1997).

## Definitions and Abbreviations
- **CA**: Certification Authority
- **CRL**: Certificate Revocation List
- **PKI**: Public Key Infrastructure
- **ASN.1**: Abstract Syntax Notation One
- **DER**: Distinguished Encoding Rules
- **OID**: Object Identifier
- **RDN**: Relative Distinguished Name
- **Critical Extension**: An extension marked critical that MUST be recognized and processed; if unrecognized, the certificate or CRL MUST be rejected.
- **End Entity**: User of PKI certificates and/or the subject of a certificate.
- **RA**: Registration Authority (optional entity to which a CA delegates certain management functions).
- **Repository**: System that stores certificates and CRLs.
- **Certification Path**: A sequence of certificates from a trusted CA to an end entity.

## 1. Introduction (Informative – condensed)
This specification profiles X.509 v3 certificates and X.509 v2 CRLs for the Internet PKI. It defines required extensions, path validation procedures, and algorithm support. Four appendices provide ASN.1 modules (1988 and 1993 syntax), notes, and examples. The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are interpreted as described in RFC 2119.

## 2. Requirements and Assumptions (Informative – condensed)
Goal: Facilitate use of X.509 certificates in Internet applications (WWW, email, user authentication, IPsec). This profile defines a common baseline; specialized communities may supplement or replace it. Certificate users should review the CA’s certificate policy before relying on services. No legally binding rules are prescribed. The profile supports low-bandwidth, offline connectivity, and does not assume X.500 Directory deployment. It supports deterministic identification, authentication, access control, and authorization. User expectations: minimal configuration responsibility, explicit usage constraints, and sensible default validation. Administrator expectations: bounded choices to reduce risk of CA mistakes.

## 3. Overview of Approach (Informative – condensed)
Architectural model includes end entities, CAs, RAs, and repositories. X.509 v3 certificates bind public keys to subjects via a digital signature from a trusted CA. Certificate chains (certification paths) are required when the relying party does not directly trust the issuing CA. This profile supports flexible architectures (paths may start with any trusted CA, name constraints may be used, policy extensions replace the PCA concept). Revocation is via CRLs – periodic signed lists of revoked certificate serial numbers. CRLs may be distributed via untrusted channels. On-line revocation methods are alternative options (defined in other PKIX specs). Operational protocols (LDAP, HTTP, FTP, X.500) and management protocols (registration, initialization, certification, key pair recovery, update, revocation request, cross-certification) are referenced but not defined in this document.

## 4. Certificate and Certificate Extensions Profile
### 4.1 Basic Certificate Fields
#### 4.1.1 Certificate Fields
- **tbsCertificate**: Contains subject/issuer names, public key, validity, and optional extensions.
- **signatureAlgorithm**: Algorithm identifier for CA’s signing algorithm; MUST match the `signature` field in tbsCertificate.
- **signatureValue**: Digital signature computed on DER-encoded tbsCertificate.

#### 4.1.2 TBSCertificate
| Field | Requirement | Reference |
|-------|-------------|-----------|
| Version | When extensions used, use v3 (value 2). SHOULD accept any version; MUST recognize v3. | 4.1.2.1 |
| Serial Number | Integer unique per CA (issuer name + serial number identify unique certificate). | 4.1.2.2 |
| Signature | Algorithm identifier (same as Certificate signatureAlgorithm). Parameters depend on algorithm. | 4.1.2.3 |
| Issuer | Non-empty distinguished name. Encoding rules: after Dec 31, 2003 MUST use UTF8String for DirectoryString; before, options: PrintableString if sufficient, else BMPString, else UTF8String. TeletexString and UniversalString for backward compatibility. MUST support country, organization, organizational-unit, dnQualifier, state/province, common name. SHOULD support locality, title, surname, given name, initials, generation qualifier. MUST support domainComponent (RFC 2247). Name comparison rules: attribute values in different types assumed different; PrintableString case-insensitive; other types case-sensitive. | 4.1.2.4 |
| Validity | Time interval when CA warrants certificate status. Dates through 2049: UTCTime; 2050+: GeneralizedTime. UTCTime: YYMMDDHHMMSSZ; YY>=50 → 19YY, YY<50 → 20YY. GeneralizedTime: YYYYMMDDHHMMSSZ; no fractional seconds. | 4.1.2.5 |
| Subject | Entity associated with public key. If CA (basicConstraints cA=TRUE), subject MUST be non-empty DN matching issuer field of issued certificates. If subject only in subjectAltName, subject MUST be empty sequence and subjectAltName MUST be critical. DN MUST be unique per CA. Encoding rules same as issuer. Legacy emailAddress attribute deprecated; use rfc822Name in subjectAltName. | 4.1.2.6 |
| Subject Public Key Info | Contains public key and algorithm identifier (see section 7.3). | 4.1.2.7 |
| Unique Identifiers | SHOULD NOT use; SHOULD be capable of parsing. | 4.1.2.8 |
| Extensions | Only if version 3. | 4.1.2.9 |

### 4.2 Standard Certificate Extensions
All extensions defined under OID arc `id-ce` (2.5.29). The following must be supported by conforming CAs: key identifiers (4.2.1.1, 4.2.1.2), basic constraints (4.2.1.10), key usage (4.2.1.3), certificate policies (4.2.1.5). If subject empty, subjectAltName (4.2.1.7) must be supported. Applications must recognize critical extensions: key usage, certificate policies, subjectAltName, basic constraints, name constraints, policy constraints, extended key usage. Applications recommended to support authority and subject key identifier.

#### 4.2.1.1 Authority Key Identifier
- OID: id-ce 35 (2.5.29.35)
- **Requirement**: keyIdentifier MUST be included in all certificates (except self-signed). SHOULD be derived from public key or unique generation method. MUST NOT be marked critical.

#### 4.2.1.2 Subject Key Identifier
- OID: id-ce 14 (2.5.29.14)
- **Requirement**: MUST appear in all CA certificates (cA=TRUE); value MUST match key identifier in Authority Key Identifier of issued certificates. SHOULD be derived from public key. SHOULD be included in end entity certificates. MUST NOT be marked critical.

#### 4.2.1.3 Key Usage
- OID: id-ce 15 (2.5.29.15)
- **Requirement**: When used, SHOULD be marked critical. Bits: digitalSignature (0), nonRepudiation (1), keyEncipherment (2), dataEncipherment (3), keyAgreement (4), keyCertSign (5), cRLSign (6), encipherOnly (7), decipherOnly (8). keyCertSign only in CA certificates. encipherOnly/decipherOnly only meaningful if keyAgreement set.

#### 4.2.1.4 Private Key Usage Period
- OID: id-ce 16 (2.5.29.16)
- **Requirement**: RECOMMENDED against use. CAs MUST NOT generate certificates with critical private key usage period extensions. If used, at least one component (notBefore/notAfter) present.

#### 4.2.1.5 Certificate Policies
- OID: id-ce 32 (2.5.29.32)
- **Requirement**: RECOMMENDED that policy information terms consist only of OID. If qualifiers used, strongly recommended to use CPS Pointer (id-qt-cps) and User Notice (id-qt-unotice). CPSuri is IA5String; UserNotice may have noticeRef and/or explicitText (max 200 chars). Applications SHOULD display user notices. If critical, software MUST interpret it or reject certificate.

#### 4.2.1.6 Policy Mappings
- OID: id-ce 33 (2.5.29.33)
- **Requirement**: Used in CA certificates. MUST be non-critical.

#### 4.2.1.7 Subject Alternative Name
- OID: id-ce 17 (2.5.29.17)
- **Requirement**: If subject empty, subjectAltName MUST be present and critical. If present, sequence MUST contain at least one entry; no empty GeneralName fields. Internet mail address: rfc822Name (addr-spec per RFC 822). IP address: OCTET STRING in network byte order; IPv4: 4 octets, IPv6: 16 octets. DNS name: dNSName (IA5String) in preferred name syntax; not case-sensitive; empty string not permitted. URI: uniformResourceIdentifier (IA5String), non-relative URL per RFC 1738. Comparison: scheme and host case-insensitive, remainder case-sensitive. Wildcards not addressed by this profile.

#### 4.2.1.8 Issuer Alternative Name
- OID: id-ce 18 (2.5.29.18)
- **Requirement**: Encoding same as subjectAltName. SHOULD NOT be marked critical.

#### 4.2.1.9 Subject Directory Attributes
- OID: id-ce 9 (2.5.29.9)
- **Requirement**: Not recommended; MUST be non-critical.

#### 4.2.1.10 Basic Constraints
- OID: id-ce 19 (2.5.29.19)
- **Requirement**: MUST appear as critical in all CA certificates. SHOULD NOT appear in end entity certificates. pathLenConstraint: if present, must be >= 0; gives max number of following CA certificates. If absent, no limit.

#### 4.2.1.11 Name Constraints
- OID: id-ce 30 (2.5.29.30)
- **Requirement**: MUST be used only in CA certificates. MUST be critical. Permitted and excluded subtrees specified. If no name of type in certificate, certificate acceptable. URI constraint: host part; leading period indicates domain. Internet mail: mailbox, host, or domain. DNS: expressed as foo.bar.com; any subdomain satisfies. For legacy rfc822Name in subject DN, constraint applies to EmailAddress attribute. directoryName: must compare DN attributes (at least as specified in 4.1.2.4). iPAddress: for IPv4 8 octets (CIDR style), for IPv6 32 octets.

#### 4.2.1.12 Policy Constraints
- OID: id-ce 36 (2.5.29.36)
- **Requirement**: May be critical or non-critical. At least one of requireExplicitPolicy or inhibitPolicyMapping MUST be present. If requireExplicitPolicy present, value indicates number of additional certificates before explicit policy required. If inhibitPolicyMapping present, value indicates number of additional certificates before policy mapping prohibited.

#### 4.2.1.13 Extended Key Usage
- OID: id-ce 37 (2.5.29.37)
- **Requirement**: May be critical or non-critical. If critical, certificate MUST be used only for indicated purposes. If non-critical, advisory. If both key usage and extended key usage are critical, both must be consistent; if no purpose consistent, certificate MUST NOT be used. Defined purposes: id-kp-serverAuth (1), id-kp-clientAuth (2), id-kp-codeSigning (3), id-kp-emailProtection (4), id-kp-timeStamping (8).

#### 4.2.1.14 CRL Distribution Points
- OID: id-ce 31 (2.5.29.31)
- **Requirement**: SHOULD be non-critical. CAs and applications RECOMMENDED to support. If distributionPoint contains URI, pointer to current CRL. If distributionPoint omits reasons, CRL includes revocations for all reasons. If omits cRLIssuer, CRL issued by same CA.

### 4.2.2 Private Internet Extensions
- OID arc: id-pe (id-pkix 1).

#### 4.2.2.1 Authority Information Access
- OID: id-pe 1 (1.3.6.1.5.5.7.1.1)
- **Requirement**: MUST be non-critical. Defines accessMethod and accessLocation. id-ad-caIssuers (id-ad 2) indicates location of CA certificates. accessLocation: if http, ftp, ldap → uniformResourceIdentifier; if dap → directoryName; if email → rfc822Name.

## 5. CRL and CRL Extensions Profile
### 5.1 CRL Fields
CertificateList ::= SEQUENCE { tbsCertList, signatureAlgorithm, signatureValue }

**Requirement**: Conforming CAs that issue CRLs MUST issue version 2 CRLs, MUST include nextUpdate, CRL number extension (5.2.3), and authority key identifier extension (5.2.1). Conforming applications MUST process version 1 and 2 CRLs.

#### 5.1.2 TBSCertList
| Field | Requirement | Reference |
|-------|-------------|-----------|
| Version | If extensions used, MUST be present and specify v2 (value 1). | 5.1.2.1 |
| Signature | Algorithm identifier (same as CertificateList signatureAlgorithm). | 5.1.2.2 |
| Issuer Name | X.500 DN, encoding rules same as certificate issuer field. | 5.1.2.3 |
| This Update | UTCTime for dates through 2049; GeneralizedTime for 2050+. | 5.1.2.4 |
| Next Update | REQUIRED to be included. Encoding same as thisUpdate. | 5.1.2.5 |
| Revoked Certificates | List of serial numbers and revocation dates; optional CRL entry extensions. | 5.1.2.6 |
| Extensions | Only if version 2; SEQUENCE of one or more CRL extensions. | 5.1.2.7 |

### 5.2 CRL Extensions
**Requirement**: Conforming CAs MUST include authority key identifier (5.2.1) and CRL number (5.2.3) in all CRLs.

#### 5.2.1 Authority Key Identifier
- OID: id-ce 35. CAs MUST use key identifier method and include this extension in all CRLs.

#### 5.2.2 Issuer Alternative Name
- OID: id-ce 18. SHOULD NOT be marked critical.

#### 5.2.3 CRL Number
- OID: id-ce 20. MUST include in all CRLs; monotonically increasing integer.

#### 5.2.4 Delta CRL Indicator
- OID: id-ce 27. Critical extension identifying delta-CRL. BaseCRLNumber identifies base CRL. If delta-CRL issued, CA MUST also issue complete CRL. CRLNumber of delta and complete CRL MUST be identical.

#### 5.2.5 Issuing Distribution Point
- OID: id-ce 28. Critical extension. Identifies CRL distribution point; indicates if covers end entity only, CA only, or limited reasons. Conforming implementations not required to support this extension. If URI, pointer to current CRL.

### 5.3 CRL Entry Extensions
All CRL entry extensions are non-critical. CAs SHOULD include reason codes (5.3.1) and invalidity dates (5.3.3) when available.

#### 5.3.1 Reason Code
- OID: id-ce 21. CAs strongly encouraged to include meaningful codes; SHOULD omit rather than use unspecified (0). Codes: unspecified (0), keyCompromise (1), cACompromise (2), affiliationChanged (3), superseded (4), cessationOfOperation (5), certificateHold (6), removeFromCRL (8).

#### 5.3.2 Hold Instruction Code
- OID: id-ce 23. Conforming applications MUST recognize: id-holdinstruction-callissuer (reject or call issuer), id-holdinstruction-reject (must reject). id-holdinstruction-none deprecated.

#### 5.3.3 Invalidity Date
- OID: id-ce 24. Date when private key compromised or certificate became invalid; may precede revocation date in CRL entry. MUST be GeneralizedTime in Zulu.

#### 5.3.4 Certificate Issuer
- OID: id-ce 29. Used in indirect CRLs. If present, always critical. RECOMMENDED that implementations recognize it.

## 6. Certification Path Validation
### 6.1 Basic Path Validation
- **Requirement**: Conforming implementations need not implement this algorithm but MUST be functionally equivalent.
- Inputs: certification path (n certificates), initial policy identifiers, current date/time, time T for validity determination.
- State variables: acceptable policy set (initial "any-policy"), constrained subtrees (unbounded), excluded subtrees (empty), explicit policy (n+1), policy mapping (n+1).
- For each certificate i=1..n:
  - (a) Verify basic info: signature, validity period (includes T), revocation status, name chaining.
  - (b) Subject name/subjectAltName consistent with constrained subtrees.
  - (c) Consistent with excluded subtrees.
  - (d) Policy info consistent with initial policy set: if explicit policy <= i, policy identifier must be in initial set; if policy mapping <= i, policy may not be mapped.
  - (e) Policy info consistent with acceptable policy set: intersection of certificate policies and acceptable policy set non-null.
  - (g) Intersection of acceptable policy set and initial policy set non-null.
  - (h) Process any critical extension.
  - (i) Verify certificate is CA certificate.
  - (j) If permittedSubtrees present, set constrained subtrees to intersection.
  - (k) If excludedSubtrees present, set excluded subtrees to union.
  - (l) If policy constraints extension, modify explicit policy and policy mapping accordingly.
  - (m) If key usage critical, ensure keyCertSign set.
- If any check fails, terminate with failure. If all pass on end-entity certificate, success with policy qualifiers.

### 6.2 Extending Path Validation
- For multiple trusted CAs, provide set of self-signed certificates.
- For PEM compatibility, additional input: list of PCA names and expected position; if recognized PCA found, assume SubordinateToCA constraint.

## 7. Algorithm Support
### 7.1 One-way Hash Functions
- SHA-1 preferred; MD2 (for PEM compatibility) and MD5 (legacy) included. MD2 and MD5 use discouraged for new applications.

### 7.2 Signature Algorithms
- Algorithm identifiers:
  - md2WithRSAEncryption (1.2.840.113549.1.1.2) – parameters NULL
  - md5WithRSAEncryption (1.2.840.113549.1.1.4) – parameters NULL
  - sha1WithRSAEncryption (1.2.840.113549.1.1.5) – parameters NULL
  - id-dsa-with-sha1 (1.2.840.10040.4.3) – parameters omitted (SEQUENCE of one OID)
- DSA signature value encoded as Dss-Sig-Value: SEQUENCE { r INTEGER, s INTEGER }

### 7.3 Subject Public Key Algorithms
#### 7.3.1 RSA Keys
- OID rsaEncryption (1.2.840.113549.1.1.1); parameters NULL.
- Public key encoded as RSAPublicKey: SEQUENCE { modulus INTEGER, publicExponent INTEGER }
- Key usage: any combination of digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment; for CAs also keyCertSign, cRLSign. RECOMMENDED that if keyCertSign or cRLSign present, keyEncipherment and dataEncipherment not present.

#### 7.3.2 Diffie-Hellman Key Exchange Key
- OID dhpublicnumber (1.2.840.10046.2.1); parameters DomainParameters (p, g, q, optional j, validationParms). Public key: DHPublicKey ::= INTEGER (y = g^x mod p).
- Key usage: keyAgreement, encipherOnly, decipherOnly; at most one of encipherOnly/decipherOnly.

#### 7.3.3 DSA Signature Keys
- OID id-dsa (1.2.840.10040.4.1); optional parameters Dss-Parms (p, q, g). If omitted, subject's DSA parameters from issuing CA (if CA signed with DSA) or from other means; if omitted and CA signed with non-DSA, clients MUST reject. Public key: DSAPublicKey ::= INTEGER (Y).
- Key usage: digitalSignature, nonRepudiation (end entity); also keyCertSign, cRLSign (CA).

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Certificate version 3 (value 2) when extensions used. | shall | 4.1.2.1 |
| R2 | Serial number MUST be unique per CA. | MUST | 4.1.2.2 |
| R3 | Issuer field MUST contain non-empty DN. | MUST | 4.1.2.4 |
| R4 | After Dec 31, 2003, DirectoryString encoding MUST be UTF8String for new certificates. | MUST | 4.1.2.4 |
| R5 | CAs MUST choose PrintableString if sufficient, else BMPString, else UTF8String before Dec 31, 2003. | MUST | 4.1.2.4 |
| R6 | Conforming implementations MUST be prepared to receive issuer names with set of attribute types (country, organization, organizational-unit, dnQualifier, state/province, common name). | MUST | 4.1.2.4 |
| R7 | Conforming implementations SHOULD be prepared to receive locality, title, surname, given name, initials, generation qualifier. | SHOULD | 4.1.2.4 |
| R8 | Certificate validity dates through 2049 MUST be UTCTime; 2050 or later MUST be GeneralizedTime. | MUST | 4.1.2.5 |
| R9 | UTCTime MUST be expressed Greenwich Mean Time (Z) and MUST include seconds (YYMMDDHHMMSSZ). | MUST | 4.1.2.5.1 |
| R10 | GeneralizedTime MUST be expressed GMT (Z), include seconds, and NO fractional seconds. | MUST | 4.1.2.5.2 |
| R11 | If subject is CA (basicConstraints cA=TRUE), subject field MUST be non-empty DN matching issuer field in issued certificates. | MUST | 4.1.2.6 |
| R12 | If subject naming only in subjectAltName, subject MUST be empty and subjectAltName MUST be critical. | MUST | 4.1.2.6 |
| R13 | CAs conforming to this profile SHOULD NOT generate certificates with unique identifiers. | SHOULD NOT | 4.1.2.8 |
| R14 | If v3 certificate, extensions field is SEQUENCE of one or more extensions. | – | 4.1.2.9 |
| R15 | Authority Key Identifier keyIdentifier MUST be included in all certificates (except self-signed). | MUST | 4.2.1.1 |
| R16 | Authority Key Identifier MUST NOT be marked critical. | MUST NOT | 4.2.1.1 |
| R17 | Subject Key Identifier MUST appear in all CA certificates (cA=TRUE). | MUST | 4.2.1.2 |
| R18 | Subject Key Identifier SHOULD be included in all end entity certificates. | SHOULD | 4.2.1.2 |
| R19 | Subject Key Identifier MUST NOT be marked critical. | MUST NOT | 4.2.1.2 |
| R20 | Key usage extension, when used, SHOULD be marked critical. | SHOULD | 4.2.1.3 |
| R21 | keyCertSign bit may only be asserted in CA certificates. | may | 4.2.1.3 |
| R22 | Private Key Usage Period: CAs MUST NOT generate certificates with critical extension. | MUST NOT | 4.2.1.4 |
| R23 | Private Key Usage Period: if used, at least one component present. | MUST | 4.2.1.4 |
| R24 | Certificate Policies extension: if critical, path validation software MUST interpret it or reject certificate. | MUST | 4.2.1.5 |
| R25 | Policy Mappings MUST be non-critical. | MUST | 4.2.1.6 |
| R26 | SubjectAltName: if subject empty, subjectAltName MUST be present and critical. | MUST | 4.2.1.7 |
| R27 | SubjectAltName: sequence MUST contain at least one entry; no empty GeneralName fields. | MUST | 4.2.1.7 |
| R28 | IssuerAltName SHOULD NOT be marked critical. | SHOULD NOT | 4.2.1.8 |
| R29 | Basic Constraints MUST appear as critical in all CA certificates. | MUST | 4.2.1.10 |
| R30 | Basic Constraints SHOULD NOT appear in end entity certificates. | SHOULD NOT | 4.2.1.10 |
| R31 | Name Constraints MUST be critical and used only in CA certificates. | MUST | 4.2.1.11 |
| R32 | Policy Constraints: at least one of requireExplicitPolicy or inhibitPolicyMapping MUST be present. | MUST | 4.2.1.12 |
| R33 | If extended key usage critical, certificate MUST be used only for indicated purposes. | MUST | 4.2.1.13 |
| R34 | If both key usage and extended key usage critical, both MUST be consistent; if no consistent purpose, certificate MUST NOT be used. | MUST | 4.2.1.13 |
| R35 | CRL Distribution Points extension SHOULD be non-critical. | SHOULD | 4.2.1.14 |
| R36 | Authority Information Access extension MUST be non-critical. | MUST | 4.2.2.1 |
| R37 | Conforming CAs that issue CRLs MUST issue version 2 CRLs. | MUST | 5 |
| R38 | Conforming CAs that issue CRLs MUST include nextUpdate, CRL number extension, and authority key identifier extension. | MUST | 5 |
| R39 | CRL version: if extensions used, field MUST be present and specify v2. | MUST | 5.1.2.1 |
| R40 | This Update: UTCTime for dates through 2049; GeneralizedTime for 2050+. | MUST | 5.1.2.4 |
| R41 | Next Update: REQUIRED to be included; encoding same as thisUpdate. | MUST | 5.1.2.5 |
| R42 | CRL Number extension MUST be included in all CRLs. | MUST | 5.2.3 |
| R43 | Authority Key Identifier extension MUST be included in all CRLs. | MUST | 5.2.1 |
| R44 | Delta CRL Indicator: if delta-CRL issued, CA MUST also issue complete CRL; CRLNumbers MUST be identical. | MUST | 5.2.4 |
| R45 | Issuing Distribution Point extension is critical. | – | 5.2.5 |
| R46 | CRL entry extensions: reason code (5.3.1) and invalidity date (5.3.3) SHOULD be included when available. | SHOULD | 5.3 |
| R47 | Hold instruction codes: applications MUST recognize id-holdinstruction-callissuer and id-holdinstruction-reject. | MUST | 5.3.2 |
| R48 | Certificate Issuer extension (if used) is always critical. | always | 5.3.4 |
| R49 | Path validation: implementations MUST be functionally equivalent to algorithm in 6.1. | MUST | 6.1 |
| R50 | Algorithm support: if implemented, must follow specifications in Section 7. | MUST | 7 |

## Informative Annexes (Condensed)
- **Appendix A**: ASN.1 Structures and OIDs (1988 Syntax) – Contains explicit and implicitly tagged modules for certificates, CRLs, extensions, and algorithms. Non-normative but authoritative for encoding.
- **Appendix B**: 1993 ASN.1 Structures and OIDs – Same content using 1993 ASN.1 syntax (includes information object classes). Provided as a service; Appendix A takes precedence in case of conflict.
- **Appendix C**: ASN.1 Notes – Explains SEQUENCE SIZE (1..MAX), INTEGER (0..MAX), and character string types (PrintableString, TeletexString, UniversalString, UTF8String). Useful for implementers.
- **Appendix D**: Examples – Hex dumps of conforming certificates (self-signed CA, end-entity DSA, end-entity RSA) and a CRL with annotation. Provided to aid understanding.
- **Appendix E**: Authors' Addresses – Contact information for Russell Housley, Warwick Ford, Tim Polk, David Solo.
- **Appendix F**: Full Copyright Statement – The Internet Society (1999); all rights reserved; permits copying and derivative works for standards development.