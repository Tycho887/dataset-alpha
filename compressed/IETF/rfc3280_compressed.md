# RFC 3280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
**Source**: IETF | **Version**: Standards Track | **Date**: April 2002 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc3280

## Scope (Summary)
This document profiles the X.509 v3 certificate and X.509 v2 CRL for use in the Internet. It describes certificate and CRL formats, standard extensions, two Internet-specific extensions (authority info access, subject info access), required extensions, certification path validation algorithm, CRL validation, and ASN.1 modules. It obsoletes RFC 2459.

## Normative References
- [PKIXALGS] Bassham, L., Polk, W. and R. Housley, "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation Lists (CRL) Profile", RFC 3279, April 2002.
- [X.509] ITU-T Recommendation X.509 (1997 E): Information Technology - Open Systems Interconnection - The Directory: Authentication Framework, June 1997.
- [X.501] ITU-T Recommendation X.501: Information Technology - Open Systems Interconnection - The Directory: Models, 1993.
- [X.520] ITU-T Recommendation X.520: Information Technology - Open Systems Interconnection - The Directory: Selected Attribute Types, 1993.
- [X.660] ITU-T Recommendation X.660 Information Technology - ASN.1 encoding rules: Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER), 1997.
- [X.690] ITU-T Recommendation X.690 Information Technology - Open Systems Interconnection - Procedures for the operation of OSI Registration Authorities: General procedures, 1992.
- [X9.55] ANSI X9.55-1995, Public Key Cryptography For The Financial Services Industry: Extensions To Public Key Certificates And Certificate Revocation Lists, 8 December, 1995.
- [RFC 791] Postel, J., "Internet Protocol", STD 5, RFC 791, September 1981.
- [RFC 822] Crocker, D., "Standard for the format of ARPA Internet text messages", STD 11, RFC 822, August 1982.
- [RFC 1034] Mockapetris, P., "Domain Names - Concepts and Facilities", STD 13, RFC 1034, November 1987.
- [RFC 1422] Kent, S., "Privacy Enhancement for Internet Electronic Mail: Part II: Certificate-Based Key Management," RFC 1422, February 1993.
- [RFC 1510] Kohl, J. and C. Neuman, "The Kerberos Network Authentication Service (V5)," RFC 1510, September 1993.
- [RFC 1519] Fuller, V., T. Li, J. Yu and K. Varadhan, "Classless Inter-Domain Routing (CIDR): An Address Assignment and Aggregation Strategy", RFC 1519, September 1993.
- [RFC 1738] Berners-Lee, T., L. Masinter and M. McCahill, "Uniform Resource Locators (URL)", RFC 1738, December 1994.
- [RFC 1778] Howes, T., S. Kille, W. Yeong and C. Robbins, "The String Representation of Standard Attribute Syntaxes," RFC 1778, March 1995.
- [RFC 1883] Deering, S. and R. Hinden. "Internet Protocol, Version 6 (IPv6) Specification", RFC 1883, December 1995.
- [RFC 2044] Yergeau, F., "UTF-8, a transformation format of Unicode and ISO 10646", RFC 2044, October 1996.
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC 2247] Kille, S., M. Wahl, A. Grimstad, R. Huber and S. Sataluri, "Using Domains in LDAP/X.500 Distinguished Names", RFC 2247, January 1998.
- [RFC 2252] Wahl, M., A. Coulbeck, T. Howes and S. Kille, "Lightweight Directory Access Protocol (v3): Attribute Syntax Definitions", RFC 2252, December 1997.
- [RFC 2277] Alvestrand, H., "IETF Policy on Character Sets and Languages", BCP 18, RFC 2277, January 1998.
- [RFC 2279] Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 2279, January 1998.
- [RFC 2560] Myers, M., R. Ankney, A. Malpani, S. Galperin and C. Adams, "Online Certificate Status Protocol - OCSP", June 1999.
- [ISO 10646] ISO/IEC 10646-1:1993. Universal Multiple-Octet Coded Character Set (UCS) -- Part 1: Architecture and Basic Multilingual Plane.
- [PKIXTSA] Adams, C., Cain, P., Pinkas, D. and R. Zuccherato, "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)", RFC 3161, August 2001.

## Definitions and Abbreviations
- **end entity**: user of PKI certificates and/or end user system that is the subject of a certificate.
- **CA**: certification authority.
- **RA**: registration authority, i.e., an optional system to which a CA delegates certain management functions.
- **CRL issuer**: an optional system to which a CA delegates the publication of certificate revocation lists.
- **repository**: a system or collection of distributed systems that stores certificates and CRLs and serves as a means of distributing these certificates and CRLs to end entities.
- **PKI**: Public Key Infrastructure.
- **PEM**: Privacy Enhanced Mail.
- **PCA**: Policy Certification Authority.
- **IPRA**: Internet Policy Registration Authority.
- **OCSP**: Online Certificate Status Protocol.
- **ASN.1**: Abstract Syntax Notation One.
- **DER**: Distinguished Encoding Rules.
- **OID**: Object Identifier.
- **DN**: Distinguished Name.
- **CRL**: Certificate Revocation List.
- **delta CRL**: A CRL that only lists changes since a base CRL.
- **base CRL**: The complete CRL referenced by a delta CRL.
- **self-issued certificate**: A certificate where the subject and issuer distinguished names are identical and non-empty.
- **relying party**: The entity that uses a certificate to verify signatures or encrypt data.
- **trust anchor**: A CA that is trusted by the relying party.
- **certification path**: A chain of certificates from a trust anchor to an end entity certificate.
- **valid_policy_tree**: A tree data structure used in path validation to track valid certificate policies.

Abbreviations: PKI, CA, RA, CRL, PCA, IPRA, OCSP, ASN.1, DER, OID, DN, URI, URL, LDAP, FTP, HTTP, IPsec, WWW, RFC, BCP, IETF, ITU-T, ISO, IEC, ANSI, DSA, RSA, SHA-1, MD5, SSL, TLS, CIDR, MIME, etc. are defined in the text.

## 2 Requirements and Assumptions
### 2.1 Communication and Topology
This profile supports users without high bandwidth, real-time IP connectivity, or high connection availability. Allows for firewall or filtered communication. Does not assume deployment of X.500 Directory or LDAP; any distribution means may be used.

### 2.2 Acceptability Criteria
Goal: meet needs of deterministic, automated identification, authentication, access control, and authorization.

### 2.3 User Expectations
Users include readers/writers of email, WWW browsers, servers, IPsec key managers. Manifest in minimal user configuration responsibility, explicit platform usage constraints, certification path constraints, sensible automation.

### 2.4 Administrator Expectations
Structure to support CA operators; unbounded choices increase risk of compromise and complicate software.

## 3 Overview of Approach
### 3.1 X.509 Version 3 Certificate
- Certificates bind public key values to subjects via trusted CA digital signature.
- Certificate has limited valid lifetime; distribution via untrusted communications and servers.
- ITU-T X.509 defines standard certificate format. v3 extends v2 with additional extension fields.
- ISO/IEC, ITU-T, ANSI X9 developed standard extensions for subject identification, key attributes, policy, path constraints.
- This profile specifies a subset for Internet use.

### 3.2 Certification Paths and Trust
- Certification path: chain of certificates from trust anchor to end entity.
- With X.509 v3, policy and constraint extensions allow flexible architecture without strict hierarchy or name subordination rule.
- Policy extensions and mappings replace PCA concept.

### 3.3 Revocation
- CRL: time-stamped, signed list of revoked certificates, published periodically by CA.
- Revoked certificate identified by serial number.
- Entry MUST NOT be removed until it appears on one regularly scheduled CRL issued beyond the revoked certificate's validity period.
- CRL distribution may use untrusted servers.
- On-line revocation (e.g., OCSP) may reduce latency.

### 3.4 Operational Protocols
Protocols for delivering certificates and CRLs (LDAP, HTTP, FTP, X.500) defined in other PKIX specs.

### 3.5 Management Protocols
Functions: registration, initialization, certification, key pair recovery, key pair update, revocation request, cross-certification. On-line or off-line methods possible.

## 4 Certificate and Certificate Extensions Profile
### 4.1 Basic Certificate Fields
- **Certificate syntax**: SEQUENCE of tbsCertificate, signatureAlgorithm, signatureValue.
- **TBSCertificate**: SEQUENCE { version, serialNumber, signature, issuer, validity, subject, subjectPublicKeyInfo, optional unique identifiers, extensions }.
- **Version**: If extensions present, MUST be 3 (value 2). Conforming implementations MUST recognize v3.
- **Serial number**: MUST be positive integer, unique per CA, non-negative, <=20 octets. Users MUST handle up to 20 octets.
- **Signature field**: algorithm identifier; MUST be same as signatureAlgorithm.
- **Issuer**: MUST contain non-empty DN. Encoding: after Dec 31, 2003 MUST use UTF8String (except name rollover and matching issuer/subject). Conforming implementations MUST be prepared for specified attribute types (country, organization, organizational-unit, distinguished name qualifier, state/province, common name, serial number). RECOMMENDS support for locality, title, surname, given name, initials, pseudonym, generation qualifier. MUST be prepared for domainComponent attribute.
- **Name comparison rules**: (a) different encoding types assumed different; (b) non-PrintableString case sensitive; (c) PrintableString case insensitive; (d) white space normalization for PrintableString.
- **Validity**: SEQUENCE of notBefore and notAfter. Dates through 2049 as UTCTime, 2050+ as GeneralizedTime. UTCTime MUST be Zulu, with seconds (YYMMDDHHMMSSZ). GeneralizedTime MUST be Zulu, include seconds, no fractional seconds.
- **Subject**: If CA (basicConstraints cA=TRUE) then subject field MUST be non-empty DN matching issuer field in all certificates issued by that CA. If CRL issuer (keyUsage cRLSign), similar. If subject identity only in subjectAltName, subject MUST be empty and subjectAltName critical. DN MUST be unique per CA.
- **SubjectPublicKeyInfo**: carries public key and algorithm identifier per [PKIXALGS].
- **Unique identifiers**: MUST NOT appear if version 1; RECOMMENDS not used; conforming CAs SHOULD NOT generate; applications SHOULD be capable of parsing.
- **Extensions**: MUST appear only if version 3.

### 4.2 Certificate Extensions
- Extension includes OID, critical boolean, extnValue. A certificate MUST NOT include more than one instance of a particular extension.
- Conforming CAs MUST support: key identifiers (4.2.1.1,4.2.1.2), basic constraints (4.2.1.10), key usage (4.2.1.3), certificate policies (4.2.1.5). If CA issues with empty subject, MUST support subjectAltName (4.2.1.7). Support for others OPTIONAL.
- Conforming applications MUST recognize: key usage, certificate policies, subjectAltName, basic constraints, name constraints, policy constraints, extended key usage, inhibit any-policy. SHOULD recognize authority/subject key identifiers, policy mapping.

#### 4.2.1 Standard Extensions (id-ce arc: joint-iso-ccitt 2 5 29)
##### 4.2.1.1 Authority Key Identifier (id-ce 35)
- MUST be included in all certificates generated by conforming CAs (except self-signed). KeyIdentifier MUST be used. SHOULD be derived from public key. MUST NOT be marked critical.
- ASN.1: `AuthorityKeyIdentifier ::= SEQUENCE { keyIdentifier [0] KeyIdentifier OPTIONAL, authorityCertIssuer [1] GeneralNames OPTIONAL, authorityCertSerialNumber [2] CertificateSerialNumber OPTIONAL }`

##### 4.2.1.2 Subject Key Identifier (id-ce 14)
- MUST appear in all conforming CA certificates (cA=TRUE). SHOULD be included in end entity certificates. SHOULD be derived from public key. MUST NOT be marked critical.
- ASN.1: `SubjectKeyIdentifier ::= KeyIdentifier`

##### 4.2.1.3 Key Usage (id-ce 15)
- MUST appear in certificates used to validate signatures on other certificates or CRLs. SHOULD be marked critical. If keyCertSign asserted, basicConstraints cA MUST also be asserted. If cRLSign asserted in CRL issuer certificate.
- ASN.1: `KeyUsage ::= BIT STRING { digitalSignature (0), nonRepudiation (1), keyEncipherment (2), dataEncipherment (3), keyAgreement (4), keyCertSign (5), cRLSign (6), encipherOnly (7), decipherOnly (8) }`

##### 4.2.1.4 Private Key Usage Period (id-ce 16)
- SHOULD NOT be used. CAs MUST NOT generate certificates with critical private key usage period. If used, MUST be non-critical and at least one component present.

##### 4.2.1.5 Certificate Policies (id-ce 32)
- Contains sequence of PolicyInformation. anyPolicy OID = {2 5 29 32 0}. RECOMMENDS policy info consist of only OID. Qualifiers: CPS Pointer (id-qt-cps, URI) and User Notice (id-qt-unotice, with noticeRef or explicitText). If extension critical, path validation MUST interpret or reject.
- For anyPolicy, qualifiers limited to those identified.

##### 4.2.1.6 Policy Mappings (id-ce 33)
- For CA certificates. Pairs issuerDomainPolicy and subjectDomainPolicy. SHOULD also appear in certificate policies extension. Policies SHOULD NOT map to/from anyPolicy. MUST be non-critical.

##### 4.2.1.7 Subject Alternative Name (id-ce 17)
- Provides additional identities. If only identity is alternative name, subject MUST be empty and extension critical. Semantics: rfc822Name, dNSName, iPAddress, uniformResourceIdentifier, otherName, etc. MUST be properly formatted. Wildcards not addressed. If present, MUST contain at least one entry; empty GeneralName fields not permitted.

##### 4.2.1.8 Issuer Alternative Name (id-ce 18)
- SHOULD NOT be marked critical.

##### 4.2.1.9 Subject Directory Attributes (id-ce 9)
- MUST be non-critical.

##### 4.2.1.10 Basic Constraints (id-ce 19)
- MUST appear as critical in all CA certificates that contain public keys used to validate digital signatures on certificates. cA boolean indicates subject is CA. If cA not asserted, keyCertSign MUST NOT be asserted. pathLenConstraint gives maximum number of non-self-issued intermediate certificates. MUST be >=0.
- ASN.1: `BasicConstraints ::= SEQUENCE { cA BOOLEAN DEFAULT FALSE, pathLenConstraint INTEGER (0..MAX) OPTIONAL }`

##### 4.2.1.11 Name Constraints (id-ce 30)
- MUST be used only in CA certificates. MUST be critical. Permitted and excluded subtrees. For URIs, constraint on host part. For Internet mail addresses, specify mailbox, host, or domain. DNS name restrictions applied by adding to left. For directoryName, comparison per section 4.1.2.4. iPAddress uses CIDR encoding.

##### 4.2.1.12 Policy Constraints (id-ce 36)
- For CA certificates. Two fields: requireExplicitPolicy and inhibitPolicyMapping. At least one MUST be present. May be critical or non-critical.

##### 4.2.1.13 Extended Key Usage (id-ce 37)
- Indicates purposes beyond key usage. May be critical or non-critical. If present, certificate MUST only be used for indicated purposes. If anyExtendedKeyUsage present, extension SHOULD NOT be critical.
- Defined key purposes: serverAuth, clientAuth, codeSigning, emailProtection, timeStamping, OCSPsigning.

##### 4.2.1.14 CRL Distribution Points (id-ce 31)
- SHOULD be non-critical. DistributionPoint includes distributionPoint, reasons, cRLIssuer. If distributionPoint omitted, cRLIssuer MUST be present. If certificate issuer not CRL issuer, cRLIssuer MUST be present.

##### 4.2.1.15 Inhibit Any-Policy (id-ce 54)
- MUST be critical. Indicates number of additional certificates before anyPolicy not considered explicit match.

##### 4.2.1.16 Freshest CRL (id-ce 46)
- Also called Delta CRL Distribution Point. MUST be non-critical.

#### 4.2.2 Private Internet Extensions
##### 4.2.2.1 Authority Information Access (id-pe 1)
- Indicates how to access CA information and services. MUST be non-critical. AccessDescription: accessMethod OID and accessLocation GeneralName. Defined access methods: id-ad-caIssuers and id-ad-ocsp.

##### 4.2.2.2 Subject Information Access (id-pe 11)
- For subject of certificate. MUST be non-critical. Defined methods: id-ad-caRepository and id-ad-timeStamping.

## 5 CRL and CRL Extensions Profile
- Conforming CAs not required to issue CRLs if other status mechanisms provided. When CRLs issued, MUST be version 2, include nextUpdate, CRL number, authority key identifier.
- Conforming applications that support CRLs REQUIRED to process v1 and v2 complete CRLs for all certificates by one CA. NOT REQUIRED to support delta, indirect, or scoped CRLs.

### 5.1 CRL Fields
- **CertificateList**: SEQUENCE { tbsCertList, signatureAlgorithm, signatureValue }.
- **TBSCertList**: SEQUENCE { version, signature, issuer, thisUpdate, nextUpdate, optional revokedCertificates, optional crlExtensions }.

#### 5.1.1 CertificateList Fields
##### 5.1.1.1 tbsCertList: Sequence containing issuer, issue dates, optional revoked list, optional extensions.
##### 5.1.1.2 signatureAlgorithm: same as in tbsCertList.
##### 5.1.1.3 signatureValue: digital signature on DER-encoded tbsCertList. CAs may use same or different keys for signing certificates and CRLs. Applications MUST support validation when same key, SHOULD support when different keys.

#### 5.1.2 Certificate List "To Be Signed"
- **version**: if extensions present, MUST be v2 (1).
- **signature**: same as signatureAlgorithm.
- **issuer name**: MUST contain X.500 DN, encoding rules per section 4.1.2.4.
- **thisUpdate**: issue date; UTCTime for dates through 2049, GeneralizedTime for 2050+.
- **nextUpdate**: MUST be included in all CRLs issued by conforming CRL issuers. Encoding same as thisUpdate.
- **revoked certificates**: if none, MUST be absent. List serial numbers, revocation date, optional entry extensions.
- **extensions**: only if version 2.

### 5.2 CRL Extensions
- Conforming CRL issuers REQUIRED to include authority key identifier and CRL number.

#### 5.2.1 Authority Key Identifier
- MUST use key identifier method. MUST include in all CRLs.

#### 5.2.2 Issuer Alternative Name
- SHOULD NOT be marked critical. Syntax per 4.2.1.8.

#### 5.2.3 CRL Number
- MUST be included in all CRLs. Monotonically increasing sequence number per scope and issuer. If delta CRLs and complete CRLs share scope, they share numbering sequence. Simultaneous issuance same number. MUST NOT use numbers longer than 20 octets.

#### 5.2.4 Delta CRL Indicator (id-ce 27)
- Critical. Identifies CRL as delta CRL. Contains BaseCRLNumber. Delta CRL scope MUST match base CRL scope. Combination conditions defined. CRL issuers MUST ensure accurate construction.

#### 5.2.5 Issuing Distribution Point (id-ce 28)
- Critical. Identifies scope, indicates which certificates covered, reason codes. If distributionPoint field absent, CRL covers all revoked unexpired certificates. indirectCRL boolean if scope includes certificates from other issuers.

#### 5.2.6 Freshest CRL (id-ce 46)
- Non-critical. Identifies delta CRL location for this complete CRL. MUST NOT appear in delta CRLs.

### 5.3 CRL Entry Extensions
- All non-critical. Support optional. CRL issuers SHOULD include reason codes and invalidity dates when available.

#### 5.3.1 Reason Code (id-ce 21)
- Non-critical. Strongly encouraged to include. SHOULD omit rather than use unspecified (0).

#### 5.3.2 Hold Instruction Code (id-ce 23)
- Non-critical. Defined: id-holdinstruction-callissuer, id-holdinstruction-reject. Conforming applications MUST recognize these.

#### 5.3.3 Invalidity Date (id-ce 24)
- Non-critical. Date of known/suspected compromise. GeneralizedTime, Zulu.

#### 5.3.4 Certificate Issuer (id-ce 29)
- For indirect CRLs. MUST be critical if used. RECOMMENDS implementations recognize.

## 6 Certification Path Validation
- Based on X.509 algorithm. Conforming implementations MUST provide equivalent external behavior.
- Algorithm inputs: prospective path (length n), current date/time, user-initial-policy-set, trust anchor information, initial-policy-mapping-inhibit, initial-explicit-policy, initial-any-policy-inhibit.
- Trust anchor may be any CA; selection is a matter of policy.

### 6.1 Basic Path Validation
- Steps: initialization, basic certificate processing for each certificate i, preparation for i+1, wrap-up.
- Initialization state variables: valid_policy_tree, permitted_subtrees, excluded_subtrees, explicit_policy, inhibit_any-policy, policy_mapping, working_public_key_algorithm, working_public_key, working_public_key_parameters, working_issuer_name, max_path_length.
- Basic processing: verify signature, validity period, not revoked, issuer name match; check name constraints; process policy extensions; verify explicit_policy condition.
- Preparation: process policy maps, update working variables, update constraints, decrement counters.
- Wrap-up: final checks, compute intersection with user-initial-policy-set.
- If explicit_policy >0 or valid_policy_tree not NULL, path succeeds.

### 6.2 Extending Path Validation
- May support multiple trust anchors, apply additional constraints, or emulate PEM PCA rules.

### 6.3 CRL Validation
- Steps to determine revocation status using CRLs.
- Inputs: certificate, use-deltas boolean.
- State variables: reasons_mask, cert_status, interim_reasons_mask.
- For each DP, obtain CRLs, verify issuer and scope, compute reasons mask, validate signatures, search for certificate.
- If certificate found on delta CRL, use that reason; if not, check complete CRL. removeFromCRL sets status to UNREVOKED.
- If reasons_mask covers all reasons or status determined, return status; else try other CRLs; if still undetermined, return UNDETERMINED.

## 7 References
Listed in Normative References section above.

## 8 Intellectual Property Rights
- IETF has been notified of intellectual property rights. No position taken.

## 9 Security Considerations
- Certificates and CRLs are signed; integrity not needed. Unrestricted access to certificates/CRLs has no security implications.
- CA/RA validation procedures affect assurance. Use of single key pair for signature and other purposes strongly discouraged.
- Private key protection is critical. CA compromise could be catastrophic. CA SHOULD maintain secure backup.
- Freshness of revocation information affects assurance. CAs SHOULD take care when using delta CRLs.
- Trust anchor selection is important; out-of-band distribution.
- Implementation quality matters.
- Key lengths and hash algorithms must be strong.
- Inconsistent name comparison rules can lead to acceptance of invalid paths or rejection of valid ones. CAs MUST encode DN identically in subject and issuer fields.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Certificate version MUST be 3 if extensions present | SHALL | 4.1.2.1 |
| R2 | Serial number MUST be positive integer, unique per CA, non-negative, <=20 octets | SHALL | 4.1.2.2 |
| R3 | Issuer field MUST contain non-empty DN | SHALL | 4.1.2.4 |
| R4 | After Dec 31, 2003, DirectoryString MUST be UTF8String (except as noted) | SHALL | 4.1.2.4 |
| R5 | Validity dates through 2049 MUST be UTCTime; 2050+ MUST be GeneralizedTime; both Zulu with seconds | SHALL | 4.1.2.5 |
| R6 | Subject field for CA or CRL issuer with non-empty DN matching issuer | SHALL | 4.1.2.6 |
| R7 | If only subjectAltName, subject MUST be empty and extension critical | SHALL | 4.1.2.6 |
| R8 | Authority key identifier MUST be included in all CA-generated certificates (except self-signed) | SHALL | 4.2.1.1 |
| R9 | Subject key identifier MUST appear in all conforming CA certificates | SHALL | 4.2.1.2 |
| R10 | Key usage extension MUST appear in certificates used to validate signatures on other certificates/CRLs | SHALL | 4.2.1.3 |
| R11 | Basic constraints MUST appear as critical in CA certificates used for certificate signature validation | SHALL | 4.2.1.10 |
| R12 | Name constraints extension MUST be critical and used only in CA certificates | SHALL | 4.2.1.11 |
| R13 | Policy constraints extension MUST contain at least one field | SHALL | 4.2.1.12 |
| R14 | Inhibit any-policy extension MUST be critical | SHALL | 4.2.1.15 |
| R15 | Authority information access extension MUST be non-critical | SHALL | 4.2.2.1 |
| R16 | Subject information access extension MUST be non-critical | SHALL | 4.2.2.2 |
| R17 | CRLs when issued MUST be version 2, include nextUpdate, CRL number, authority key identifier | SHALL | 5 |
| R18 | CRL nextUpdate MUST be included | SHALL | 5.1.2.5 |
| R19 | CRL number extension MUST be included in all CRLs | SHALL | 5.2.3 |
| R20 | Authority key identifier MUST be included in all CRLs | SHALL | 5.2.1 |
| R21 | Delta CRL indicator MUST be critical if used | SHALL | 5.2.4 |
| R22 | Issuing distribution point MUST be critical if used | SHALL | 5.2.5 |
| R23 | Certificate issuer CRL entry extension MUST be critical if used | SHALL | 5.3.4 |

## Informative Annexes (Condensed)
- **Appendix A: ASN.1 Structures and OIDs**: Provides two ASN.1 modules (explicitly and implicitly tagged, 1988 syntax) defining all data structures and OIDs used in the profile. Includes naming attributes, certificate and CRL structures, extensions, and upper bounds.
- **Appendix B: ASN.1 Notes**: Clarifies encoding of serial numbers (non-negative), TeletexString, UTF8String, OID support (arc elements < 2^28, string length up to 100 chars, max 20 elements), handling of unknown elements in non-critical extensions.
- **Appendix C: Examples**: Annotated hex dumps of a DSA self-signed CA certificate, a DSA end entity certificate, an RSA end entity certificate, and a CRL. Illustrates conforming certificate and CRL encoding.