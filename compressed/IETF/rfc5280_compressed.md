# RFC 5280: Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
**Source**: IETF | **Version**: Standards Track (Obsoletes RFC 3280, 4325, 4630) | **Date**: May 2008 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc5280

## Scope (Summary)
This memo profiles X.509 v3 certificates and X.509 v2 CRLs for Internet use, defining format, semantics, extensions, and certification path validation procedures. It specifies required certificate and CRL fields, standard extensions (e.g., key usage, basic constraints, name constraints), Internet-specific extensions (authority/subject information access), and an algorithm for path validation.

## Normative References
- [RFC791] (IP)
- [RFC1034] (Domain Names)
- [RFC1123] (Host Requirements)
- [RFC2119] (Key words)
- [RFC2460] (IPv6)
- [RFC2585] (PKI Operational Protocols: FTP/HTTP)
- [RFC2616] (HTTP/1.1)
- [RFC2797] (CMS Messages)
- [RFC2821] (SMTP)
- [RFC3279] (Algorithms and Identifiers)
- [RFC3454] (Stringprep)
- [RFC3490] (IDNA)
- [RFC3629] (UTF-8)
- [RFC3986] (URI Generic Syntax)
- [RFC3987] (IRIs)
- [RFC4055] (Additional RSA Algorithms)
- [RFC4516] (LDAP URL)
- [RFC4518] (String Preparation)
- [RFC4523] (LDAP X.509 Schema)
- [RFC4632] (CIDR)
- [X.680] (ASN.1)
- [X.690] (BER/CER/DER)

## Definitions and Abbreviations
- **end entity**: user of PKI certificates and/or end user system that is the subject of a certificate.
- **CA**: certification authority.
- **RA**: registration authority (optional, delegated by CA).
- **CRL issuer**: system that generates and signs CRLs.
- **repository**: system storing certificates and CRLs for distribution.
- **Certificate Revocation List (CRL)**: a signed data structure listing revoked certificates.
- **OCSP**: Online Certificate Status Protocol ([RFC2560]).
- **PKIX**: Public Key Infrastructure using X.509.
- **Self-issued certificate**: certificate where issuer and subject DNs match (by Section 7.1 rules).
- **Self-signed certificate**: self-issued where the signature can be verified by the certificate's own public key.
- **Cross-certificate**: CA certificate where issuer and subject are different entities.
- **Delta CRL**: CRL that only lists changes since a base CRL.
- **Indirect CRL**: CRL issued by an entity that may include certificates issued by other CAs.
- **Key usage bits**: digitalSignature (0), nonRepudiation (1), keyEncipherment (2), dataEncipherment (3), keyAgreement (4), keyCertSign (5), cRLSign (6), encipherOnly (7), decipherOnly (8).
- **GeneralName**: CHOICE including otherName, rfc822Name, dNSName, x400Address, directoryName, ediPartyName, uniformResourceIdentifier, iPAddress, registeredID.

## 1. Introduction
This specification profiles X.509 v3 certificates and X.509 v2 CRLs for the Internet PKI. Sections 2 and 3 describe requirements and architectural model. Section 4 profiles v3 certificates (basic fields, extensions). Section 5 profiles v2 CRLs (fields, extensions). Section 6 specifies certification path validation. Section 7 defines internationalized name processing rules. Appendices contain ASN.1 modules and examples. This document obsoletes RFC 3280, RFC 4325, RFC 4630, with changes summarized (internationalized names, legacy encoding conditions, policy mappings marking, etc.). The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119].

## 2. Requirements and Assumptions
Goal: facilitate use of X.509 certificates in Internet applications (WWW, email, user auth, IPsec). Profile promotes interoperable certificate management. Users should review CA certificate policy. Communication topology supports low-bandwidth, firewalls. No assumption of X.500 or LDAP directory. Acceptability criteria: support deterministic identification, authentication, access control. Users: limited sophistication – minimal configuration responsibility. Administrators: unbounded choices complicate software; profile limits choices.

### 2.1. Communication and Topology
Supports users without high bandwidth, real-time IP connectivity, or high connection availability. Profile allows firewalled communication. Directory deployment not assumed.

### 2.2. Acceptability Criteria
Services determine attributes and ancillary control information (policy data, constraints).

### 2.3. User Expectations
Minimal user configuration; explicit platform usage constraints; certification path constraints; applications automate validation.

### 2.4. Administrator Expectations
Unbounded choices increase risk of mistakes; software complexity reduced by limiting options.

## 3. Overview of Approach
Architectural model: end entities, CAs, RAs, CRL issuers, repositories. CAs responsible for revocation status (OCSP, CRLs, or other). CA may delegate CRL issuance.

### 3.1. X.509 Version 3 Certificate
Binds public key to subject via CA digital signature. Certificate has limited validity. V3 extends v2 with extension fields. Standard and private extensions defined.

### 3.2. Certification Paths and Trust
Paths consist of multiple certificates ending at a trust anchor. This profile supports flexible architecture: certification paths may start from any trusted CA, name constraints optional, policy extensions replace PCA concept. Certificate classes: CA certificates (cross, self-issued, self-signed) and end entity certificates.

### 3.3. Revocation
CRL method: CA periodically issues signed CRL listing revoked serial numbers. CRL distribution untrusted. Limitation: latency equals CRL issue period. Online revocation (OCSP) reduces latency but requires trust in validation service.

### 3.4. Operational Protocols
LLDAP, HTTP, FTP, X.500 for certificate and CRL delivery. Defined in other PKIX specifications.

### 3.5. Management Protocols
On-line interactions: registration, initialization, certification, key pair recovery, key pair update, revocation request, cross-certification. Off-line methods also possible.

## 4. Certificate and Certificate Extensions Profile
Profiles X.509 v3 certificate format and extensions for Internet PKI. Uses 1988 ASN.1 syntax; encoded certificates equivalent to 1997 syntax.

### 4.1. Basic Certificate Fields
```
Certificate ::= SEQUENCE {
    tbsCertificate       TBSCertificate,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}
```
- **tbsCertificate**: contains subject, issuer, public key, validity, version, serial number, optional extensions.
- **signatureAlgorithm**: algorithm identifier (must match signature field in TBSCertificate). [RFC3279], [RFC4055], [RFC4491] list supported algorithms; other MAY be supported.
- **signatureValue**: digital signature computed on DER-encoded tbsCertificate.

#### 4.1.1. Certificate Fields
Three required fields as above.

##### 4.1.1.1. tbsCertificate
Detailed in Section 4.1.2.

##### 4.1.1.2. signatureAlgorithm
Algorithm identifier (OID + optional parameters). MUST match signature field in TBSCertificate (Section 4.1.2.3).

##### 4.1.1.3. signatureValue
Digital signature on DER-encoded tbsCertificate.

#### 4.1.2. TBSCertificate
```
TBSCertificate ::= SEQUENCE {
    version         [0] EXPLICIT Version DEFAULT v1,
    serialNumber    CertificateSerialNumber,
    signature       AlgorithmIdentifier,
    issuer          Name,
    validity        Validity,
    subject         Name,
    subjectPublicKeyInfo SubjectPublicKeyInfo,
    issuerUniqueID  [1] IMPLICIT UniqueIdentifier OPTIONAL,
    subjectUniqueID [2] IMPLICIT UniqueIdentifier OPTIONAL,
    extensions      [3] EXPLICIT Extensions OPTIONAL
}
```
##### 4.1.2.1. Version
MUST be v3 (value 2) when extensions used. Version 2 SHOULD be used if UniqueIdentifier present but no extensions. Version 1 default if only basic fields. Conforming implementations MUST recognize v3. Generation of v2 not expected.

##### 4.1.2.2. Serial Number
MUST be positive integer assigned by CA, unique for each certificate. CAs MUST force non-negative. Certificate users MUST handle up to 20 octets. CAs MUST NOT use longer than 20 octets. Users SHOULD gracefully handle negative or zero serial numbers.

##### 4.1.2.3. Signature
Algorithm identifier of signature algorithm. MUST match signatureAlgorithm field in Certificate. Parameters vary per algorithm.

##### 4.1.2.4. Issuer
MUST contain non-empty distinguished name (DN). Name defined as RDNSequence. DirectoryString: CAs MUST use PrintableString or UTF8String, with exceptions for legacy (TeletexString, BMPString, UniversalString) to preserve backward compatibility. Conforming implementations MUST be prepared to receive: country, organization, organizationalUnit, dnQualifier, stateOrProvinceName, commonName, serialNumber. SHOULD be prepared for: locality, title, surname, givenName, initials, pseudonym, generationQualifier. MUST be prepared for domainComponent attribute ([RFC4519]). Name chaining for path validation: matching rules per Section 7.1. Self-issued if issuer and subject match.

##### 4.1.2.5. Validity
Time interval: notBefore to notAfter inclusive. CAs MUST encode through 2049 as UTCTime, 2050+ as GeneralizedTime. Conforming apps MUST process both. For no well-defined expiration, notAfter SHOULD be GeneralizedTime 99991231235959Z. If issuer cannot maintain status until notAfter, MUST ensure no valid certification path exists after termination.

###### 4.1.2.5.1. UTCTime
MUST be expressed in Zulu, include seconds (YYMMDDHHMMSSZ). Year interpretation: YY >= 50 -> 19YY; YY < 50 -> 20YY.

###### 4.1.2.5.2. GeneralizedTime
MUST be in Zulu, include seconds (YYYYMMDDHHMMSSZ). MUST NOT include fractional seconds.

##### 4.1.2.6. Subject
Identifies entity associated with public key. MAY be in subject field and/or subjectAltName. If subject is CA (cA TRUE), subject MUST be non-empty DN matching issuer field in certificates issued by that CA. If subject is CRL issuer (cRLSign TRUE), subject MUST be non-empty DN matching issuer field in CRLs. If only subjectAltName, subject MUST be empty sequence and subjectAltName critical. Where non-empty, MUST be X.500 DN, unique per CA. Implementation requirements same as issuer field. CAs MUST use PrintableString or UTF8String except when subject is CA/CRL issuer (use same encoding as in issued certs/CRLs) or for backward compatibility (TeletexString, BMPString, UniversalString MAY be used for previously established names). Legacy emailAddress attribute in subject DN deprecated; use rfc822Name in subjectAltName.

##### 4.1.2.7. Subject Public Key Info
Carries public key and algorithm identifier. Supported algorithms in [RFC3279], [RFC4055], [RFC4491].

##### 4.1.2.8. Unique Identifiers
MUST NOT appear in v1; MUST only appear if v2 or v3. Conforming CAs MUST NOT generate certificates with unique identifiers. Applications SHOULD parse but no processing required.

##### 4.1.2.9. Extensions
MUST only appear in v3. SEQUENCE of one or more extensions per Section 4.2.

### 4.2. Certificate Extensions
Extensions may be critical or non-critical. Critical unrecognized extension causes rejection. Non-critical may be ignored if unrecognized. Conforming CAs MUST support: key identifiers, basic constraints, key usage, certificate policies. If empty subject, MUST support subject alternative name. Conforming applications MUST recognize: key usage, certificate policies, subject alternative name, basic constraints, name constraints, policy constraints, extended key usage, inhibit anyPolicy. SHOULD recognize authority/subject key identifier and policy mappings.

#### 4.2.1. Standard Extensions (id-ce arc: {joint-iso-ccitt(2) ds(5) 29})
##### 4.2.1.1. Authority Key Identifier
Identifies public key used to sign certificate. MUST include keyIdentifier in all certificates from conforming CAs (except self-signed). keyIdentifier SHOULD be derived from public key. Conforming CAs MUST mark non-critical. OID: id-ce 35.

##### 4.2.1.2. Subject Key Identifier
Identifies certificates containing a particular public key. MUST appear in all CA certificates (cA TRUE). Value MUST match key identifier in authorityKeyIdentifier of issued certificates. SHOULD be derived from public key. For end entity certificates, SHOULD be included. Non-critical. OID: id-ce 14.

##### 4.2.1.3. Key Usage
Defines purpose of key. Conforming CAs MUST include in certificates used to validate signatures on other certs or CRLs. SHOULD mark critical. Bits: digitalSignature (0), nonRepudiation (1), keyEncipherment (2), dataEncipherment (3), keyAgreement (4), keyCertSign (5), cRLSign (6), encipherOnly (7), decipherOnly (8). If keyCertSign asserted, cA bit in basicConstraints MUST be asserted. At least one bit MUST be set. OID: id-ce 15.

##### 4.2.1.4. Certificate Policies
Sequence of policy OIDs and optional qualifiers. Special anyPolicy OID ({2 5 29 32 0}) allowed. Applications compare to acceptable policy list. RECOMMENDED that policies consist only of OID; qualifiers limited to CPS Pointer and User Notice. User notice: noticeRef or explicitText (UTF8String, max 200 chars). Conforming CAs SHOULD NOT use noticeRef. OID: id-ce 32.

##### 4.2.1.5. Policy Mappings
Used in CA certificates; maps issuerDomainPolicy to subjectDomainPolicy. Mapped policies SHOULD appear in certificate policies extension. MUST NOT map to/from anyPolicy. Conforming CAs SHOULD mark critical. OID: id-ce 33.

##### 4.2.1.6. Subject Alternative Name
Allows additional identities (rfc822Name, dNSName, iPAddress, URI, etc.). If only identity, subject DN MUST be empty and subjectAltName critical. rfc822Name format: "Local-part@Domain" per RFC 2821. iPAddress: network byte order (4 octets IPv4, 16 octets IPv6). dNSName: preferred name syntax per RFC 1034/1123, no case significance. URI: MUST NOT be relative, must include scheme and authority. Wildcard semantics not defined. Conforming CAs MUST NOT include empty GeneralName fields. OID: id-ce 17.

##### 4.2.1.7. Issuer Alternative Name
Same encoding as subjectAltName. Not used in path validation. Conforming CAs SHOULD mark non-critical. OID: id-ce 18.

##### 4.2.1.8. Subject Directory Attributes
Sequence of attributes (e.g., nationality). MUST be non-critical. OID: id-ce 9.

##### 4.2.1.9. Basic Constraints
Indicates if subject is CA and maximum path length. cA boolean: if not asserted, keyCertSign MUST NOT be set. If extension absent in v3, public key MUST NOT verify certificate signatures. pathLenConstraint: maximum number of non-self-issued intermediate CA certs after this one. Conforming CAs MUST include in all CA certs that are used to validate signatures on certificates; MUST mark critical. MAY appear in end entity. OID: id-ce 19.

##### 4.2.1.10. Name Constraints
MUST appear only in CA certificates. Defines permitted and excluded name subtrees. Restrictions apply to subject DN and subjectAltName. Self-issued certificates exempt (except final cert). Conforming CAs MUST mark critical; SHOULD NOT constrain x400Address, ediPartyName, registeredID. MUST NOT be empty sequence. Applications MUST be able to process constraints on directoryName; SHOULD be able on rfc822Name, uniformResourceIdentifier, dNSName, iPAddress. For URIs, constraint applies to host part; for email, may specify mailbox, host, or domain (leading period). DNS name constraints: construct by adding labels to left. directoryName constraints require DN comparison per Section 7.1. iPAddress constraints: encode with CIDR style (8 octets IPv4, 32 IPv6). OID: id-ce 30.

##### 4.2.1.11. Policy Constraints
Used in CA certificates. Two fields: requireExplicitPolicy (number of additional certs before explicit policy required) and inhibitPolicyMapping (number of additional certs before policy mapping inhibited). Conforming CAs MUST mark critical. MUST NOT be empty sequence. OID: id-ce 36.

##### 4.2.1.12. Extended Key Usage
Indicates one or more purposes in addition to key usage. Usually end entity. MAY be critical or non-critical. If present, certificate MUST only be used for indicated purposes. May include anyExtendedKeyUsage. If both key usage and extended key usage present, both MUST be independently satisfied. Defined OIDs: serverAuth, clientAuth, codeSigning, emailProtection, timeStamping, OCSPSigning. OID: id-ce 37.

##### 4.2.1.13. CRL Distribution Points
Identifies how to obtain CRL. SHOULD be non-critical. DistributionPoint: distributionPoint, reasons, cRLIssuer. At least distributionPoint or cRLIssuer MUST be present. If issuer = CRL issuer, omit cRLIssuer and include distributionPoint. DistributionPointName can be fullName (GeneralNames) or nameRelativeToCRLIssuer. URI semantics: pointer to CRL (DER encoded). LDAP URI must include dn and attrdesc. Reasons field omitted implies all reasons. This profile recommends against segmenting by reason code. Conforming CA must include at least one DP covering all reasons. OID: id-ce 31.

##### 4.2.1.14. Inhibit anyPolicy
Used in CA certificates; indicates number of additional non-self-issued certificates before anyPolicy is no longer considered an explicit match. Conforming CAs MUST mark critical. OID: id-ce 54.

##### 4.2.1.15. Freshest CRL (Delta CRL Distribution Point)
Identifies how to obtain delta CRL. MUST be non-critical. Same syntax as CRLDistributionPoints. OID: id-ce 46.

#### 4.2.2. Private Internet Extensions (id-pe arc: {id-pkix 1})
##### 4.2.2.1. Authority Information Access
Indicates how to access information about certificate issuer. May include CA issuers (id-ad-caIssuers) and OCSP responder (id-ad-ocsp). Non-critical. Each AccessDescription: accessMethod OID, accessLocation GeneralName. For caIssuers, may specify directoryName or URI (LDAP, HTTP, FTP). HTTP/FTP URIs must point to DER-encoded cert or certs-only CMS message. At least one instance SHOULD be HTTP or LDAP URI. OID: id-pe 1.

##### 4.2.2.2. Subject Information Access
Access information about the subject. For CAs: repository (id-ad-caRepository). For end entities: services (e.g., timestamping). Non-critical. Same syntax. At least one instance SHOULD be HTTP or LDAP URI. OID: id-pe 11.

## 5. CRL and CRL Extensions Profile
Profiles X.509 v2 CRL. CRL issuer may be CA or authorized entity. CRL scope: set of certificates that could appear on CRL. Indirect CRL: includes certificates from multiple CAs. Delta CRL: lists changes since a base CRL; scope must match base CRL. Conforming CAs: when CRLs issued, MUST be v2, include nextUpdate, CRL number extension, authority key identifier extension. Conforming apps REQUIRED to process v1 and v2 complete CRLs for one CA.

### 5.1. CRL Fields
```
CertificateList ::= SEQUENCE {
    tbsCertList          TBSCertList,
    signatureAlgorithm   AlgorithmIdentifier,
    signatureValue       BIT STRING
}
TBSCertList ::= SEQUENCE {
    version             Version OPTIONAL, -- if present, MUST be v2
    signature           AlgorithmIdentifier,
    issuer              Name,
    thisUpdate          Time,
    nextUpdate          Time OPTIONAL,
    revokedCertificates SEQUENCE OF SEQUENCE {
        userCertificate    CertificateSerialNumber,
        revocationDate     Time,
        crlEntryExtensions Extensions OPTIONAL
    } OPTIONAL,
    crlExtensions       [0] EXPLICIT Extensions OPTIONAL
}
```
#### 5.1.1. CertificateList Fields
##### 5.1.1.1. tbsCertList
Contains issuer, dates, revoked list, extensions.

##### 5.1.1.2. signatureAlgorithm
Algorithm identifier; MUST match signature field in tbsCertList.

##### 5.1.1.3. signatureValue
Digital signature on DER-encoded tbsCertList. CAs may use same or different keys for cert and CRL signing. Applications MUST support validation when same key used; SHOULD support when different keys.

#### 5.1.2. TBSCertList Fields
##### 5.1.2.1. Version
Required if extensions used; MUST be v2 (value 1).

##### 5.1.2.2. Signature
Algorithm identifier; MUST match signatureAlgorithm.

##### 5.1.2.3. Issuer Name
Must be non-empty X.500 DN. Encoding rules per Section 4.1.2.4.

##### 5.1.2.4. This Update
Issue date. Encode as UTCTime through 2049, GeneralizedTime from 2050.

##### 5.1.2.5. Next Update
Date by which next CRL will be issued. Conforming CRL issuers MUST include this field. Same encoding rules.

##### 5.1.2.6. Revoked Certificates
List absent if no revocations. Each entry: serial number, revocation date, optional CRL entry extensions (Section 5.3).

##### 5.1.2.7. Extensions
Only if version 2.

### 5.2. CRL Extensions
#### 5.2.1. Authority Key Identifier
MUST be included in all CRLs by conforming CRL issuers, using key identifier method. Syntax per Section 4.2.1.1.

#### 5.2.2. Issuer Alternative Name
Additional identities for issuer. SHOULD be non-critical. Syntax per Section 4.2.1.7.

#### 5.2.3. CRL Number
Monotonically increasing sequence number for given scope and issuer. MUST be included, non-critical. If delta CRLs used, share numbering with complete CRLs. CRL numbers MUST be different if thisUpdate differs. Validators MUST handle up to 20 octets; issuers MUST NOT exceed 20 octets. OID: id-ce 20.

#### 5.2.4. Delta CRL Indicator
Critical extension identifying delta CRL. Contains BaseCRLNumber (CRL number of referenced base complete CRL). Delta CRL scope must match base. CRL issuer must use same private key for delta and complete CRLs. Delta CRL lists changes since base. Conditions for combination of complete and delta CRLs (same issuer, same scope, base CRL number <= complete CRL number < delta CRL number). Application MUST be able to construct current complete CRL by combining previous complete and current delta. OID: id-ce 27.

#### 5.2.5. Issuing Distribution Point
Critical extension identifying CRL distribution point and scope. Indicates if covers end entity only (onlyContainsUserCerts), CA only (onlyContainsCACerts), attribute only (onlyContainsAttributeCerts), or limited reason codes. Conforming CRL issuers MUST set onlyContainsAttributeCerts FALSE. Must not issue CRL where all four booleans false and no distributionPoint or onlySomeReasons. OID: id-ce 28.

#### 5.2.6. Freshest CRL (Delta CRL Distribution Point)
Non-critical extension in complete CRL to locate delta CRLs. Only distributionPoint field meaningful; reasons and cRLIssuer MUST be omitted. OID: id-ce 46.

#### 5.2.7. Authority Information Access
Non-critical CRL extension. MUST include at least one AccessDescription with id-ad-caIssuers. Access method types other than id-ad-caIssuers MUST NOT be included. At least one SHOULD be HTTP or LDAP URI.

### 5.3. CRL Entry Extensions
#### 5.3.1. Reason Code
Non-critical. Identifies revocation reason. SHOULD be meaningful; SHOULD be absent rather than unspecified (0). removeFromCRL (8) only in delta CRLs. OID: id-ce 21.

#### 5.3.2. Invalidity Date
Non-critical. Date when private key compromised or certificate became invalid. Must be in GeneralizedTime, Zulu, without fractional seconds. OID: id-ce 24.

#### 5.3.3. Certificate Issuer
Non-critical but RECOMMENDED to be critical? Actually: "CRL issuers MUST mark this extension as critical". Identifies certificate issuer for indirect CRL entries. Defaults to CRL issuer for first entry if absent; subsequent entries default to preceding. Must include DN from certificate's issuer field. OID: id-ce 29.

## 6. Certification Path Validation
Describes algorithm for validating certification paths. Conforming implementations need not implement exactly but must give equivalent external behavior.

### 6.1. Basic Path Validation
Four steps: initialization, basic certificate processing, preparation for next certificate, wrap-up.

**Inputs:**
- prospective certification path of length n
- current date/time
- user-initial-policy-set (set of acceptable policy OIDs)
- trust anchor info (issuer name, public key algorithm, public key, optionally parameters)
- initial-policy-mapping-inhibit (boolean)
- initial-explicit-policy (boolean)
- initial-any-policy-inhibit (boolean)
- initial-permitted-subtrees (sets per name type)
- initial-excluded-subtrees (sets per name type)

**Eleven state variables:** valid_policy_tree, permitted_subtrees, excluded_subtrees, explicit_policy, inhibit_anyPolicy, policy_mapping, working_public_key_algorithm, working_public_key, working_public_key_parameters, working_issuer_name, max_path_length.

#### 6.1.3. Basic Certificate Processing (for each certificate i)
(a) Verify signature, validity, not revoked, issuer name matches working_issuer_name.
(b) (If not self-issued) verify subject names within permitted_subtrees.
(c) (If not self-issued) verify subject names not in excluded_subtrees.
(d) Process policy information (if policies extension present and valid_policy_tree not NULL).
(e) If policy extension not present, set valid_policy_tree to NULL.
(f) Verify explicit_policy > 0 or valid_policy_tree not NULL.

#### 6.1.4. Preparation for Certificate i+1
(a) If policy mappings present, verify no anyPolicy mapping.
(b) Update valid_policy_tree based on mappings.
(c) Set working_issuer_name to subject.
(d) Set working_public_key.
(e)-(f) Update parameters.
(g) Update permitted/excluded subtrees from name constraints.
(h) Decrement counters if not self-issued.
(i)-(j) Process policy constraints and inhibitAnyPolicy.
(k) Verify basicConstraints (cA TRUE) for v3.
(l) Decrement max_path_length if not self-issued.
(m) Apply pathLenConstraint.
(n) Verify keyCertSign if key usage present.
(o) Process other critical extensions.

#### 6.1.5. Wrap-Up
(a) Decrement explicit_policy.
(b)-(e) Update working keys.
(g) Calculate intersection of valid_policy_tree with user-initial-policy-set.

**Outputs:** success indication, valid_policy_tree, working keys.

### 6.2. Using the Path Validation Algorithm
Selection of trusted CAs is local. Inputs may reflect application-specific requirements. Implementation may augment algorithm but at least must meet minimum conditions.

### 6.3. CRL Validation
Steps to determine revocation status when CRLs are used. Requires certificate, use-deltas boolean, and local CRL cache. State variables: reasons_mask, cert_status, interim_reasons_mask. Process each distribution point and corresponding CRLs until all reasons covered or cert_status determined.

## 7. Processing Rules for Internationalized Names
### 7.1. Internationalized Names in Distinguished Names
Conforming implementations MUST use LDAP StringPrep ([RFC4518]) for comparison of PrintableString or UTF8String attributes. Steps: mapping (including case folding), normalization, prohibition, check bidi, Insignificant Character Removal (white space compression). Comparisons treat attributes with same type and normalized value as match. Two DNs match if same number of RDNs and each RDN matches in order.

### 7.2. Internationalized Domain Names in GeneralName
Domain names MUST be converted to ACE format per RFC 3490 (ToASCII, UseSTD3ASCIIRules, AllowUnassigned NOT set). Comparison: case-insensitive exact match on entire name. For name constraints, label-by-label case-insensitive match. Display: ToUnicode conversion.

### 7.3. Internationalized Domain Names in Distinguished Names
Each domainComponent attribute represents one label. Must use ToASCII conversion. Comparison: case-insensitive exact match.

### 7.4. Internationalized Resource Identifiers
IRIs must be mapped to URIs per RFC 3987 (NFC normalization, step 2). Before comparison: (1) convert IDNs to ACE, (2) normalize scheme and host to lowercase, (3) percent-encoding normalization, (4) path segment normalization, (5) scheme-based normalization for ldap, http, https, ftp. Comparison: case-sensitive exact match.

### 7.5. Internationalized Electronic Mail Addresses
Host-part with IDN must be converted to ACE. Two addresses match if local-part exact match and host-part case-insensitive ASCII comparison.

## 8. Security Considerations
- Certificates and CRLs digitally signed; no extra integrity needed.
- CA/RA validation procedures affect assurance; relying parties should review CPS.
- Separate key pairs for signature and key management recommended.
- Private key protection critical; CA key compromise catastrophic.
- Loss of CA key problematic; secure backup needed.
- Timeliness of revocation affects assurance.
- Path validation depends on trusted CA public keys; secure distribution critical.
- Weak cryptographic algorithms limit utility.
- Inconsistent name comparison rules can break path validation.
- CAs must encode DNs identically in issuer/subject fields for chaining.
- Name constraints for DNs must be identically encoded.
- Constraining one name form does not protect others.
- Use of https URIs in extensions may cause circular dependencies.
- Self-issued certificates support key rollover.
- Legacy TeletexString encoding using Latin1String may cause false comparisons.
- Visual similarity of strings can mislead users; issuers and relying parties must be aware.

## 9. IANA Considerations
No IANA actions needed; OIDs delegated to PKIX Working Group.

## 10. Acknowledgments
Warwick Ford, Matt Crawford, Tom Gindin, Steve Hanna, Stephen Henson, Paul Hoffman, Takashi Ito, Denis Pinkas, Wen-Cheng Wang.

## 11. References
Normative and Informative references as listed.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Certificate version MUST be 3 when extensions present | shall | 4.1.2.1 |
| R2 | Serial number MUST be positive integer, unique per CA, non-negative | shall | 4.1.2.2 |
| R3 | Serial number MUST NOT exceed 20 octets | shall | 4.1.2.2 |
| R4 | Issuer field MUST contain non-empty DN | shall | 4.1.2.4 |
| R5 | CAs MUST use PrintableString or UTF8String for DirectoryString (exceptions allowed) | shall | 4.1.2.4 |
| R6 | UTCTime MUST be expressed in Zulu with seconds | shall | 4.1.2.5.1 |
| R7 | GeneralizedTime MUST be in Zulu with seconds, no fractional seconds | shall | 4.1.2.5.2 |
| R8 | Subject field MUST be populated with non-empty DN if subject is CA or CRL issuer | shall | 4.1.2.6 |
| R9 | If subjectAltName used without subject DN, subject MUST be empty and subjectAltName critical | shall | 4.1.2.6 |
| R10 | CAs MUST NOT generate certificates with unique identifiers | shall | 4.1.2.8 |
| R11 | Authority key identifier MUST be included in all certificates (except self-signed) | shall | 4.2.1.1 |
| R12 | Authority key identifier MUST be non-critical | shall | 4.2.1.1 |
| R13 | Subject key identifier MUST appear in all CA certificates (cA=TRUE) | shall | 4.2.1.2 |
| R14 | Subject key identifier MUST be non-critical | shall | 4.2.1.2 |
| R15 | CAs MUST include key usage extension in certificates used to validate cert or CRL signatures | shall | 4.2.1.3 |
| R16 | Key usage SHOULD be marked critical when present | should | 4.2.1.3 |
| R17 | If keyCertSign bit asserted, cA bit in basic constraints MUST be asserted | shall | 4.2.1.3 |
| R18 | Policy OID MUST NOT appear more than once in certificate policies extension | shall | 4.2.1.4 |
| R19 | Conforming CAs MUST include basic constraints in all CA certs used for signature validation; MUST mark critical | shall | 4.2.1.9 |
| R20 | Name constraints extension MUST be marked critical | shall | 4.2.1.10 |
| R21 | Name constraints MUST NOT be empty sequence | shall | 4.2.1.10 |
| R22 | Policy constraints extension MUST be marked critical | shall | 4.2.1.11 |
| R23 | Policy constraints MUST NOT be empty sequence | shall | 4.2.1.11 |
| R24 | Inhibit anyPolicy MUST be marked critical | shall | 4.2.1.14 |
| R25 | Authority information access extension MUST be non-critical | shall | 4.2.2.1 |
| R26 | Subject information access extension MUST be non-critical | shall | 4.2.2.2 |
| R27 | When CRLs issued, CRLs MUST be v2, include nextUpdate, CRL number, authority key identifier | shall | 5 |
| R28 | CRL number extension MUST be included, non-critical | shall | 5.2.3 |
| R29 | Delta CRL indicator extension MUST be critical | shall | 5.2.4 |
| R30 | Freshest CRL extension in CRL MUST be non-critical, MUST NOT appear in delta CRLs | shall | 5.2.6 |
| R31 | Authority information access CRL extension MUST be non-critical; MUST include at least one id-ad-caIssuers | shall | 5.2.7 |
| R32 | Certificate issuer entry extension MUST be marked critical | shall | 5.3.3 |
| R33 | Basic certificate processing: verify signature, validity, revocation, issuer name | shall | 6.1.3(a) |
| R34 | If certificate policies extension absent, set valid_policy_tree to NULL | shall | 6.1.3(e) |
| R35 | Conforming implementations MUST use LDAP StringPrep for DN comparison of PrintableString/UTF8String | shall | 7.1 |
| R36 | IDNs in dNSName MUST be converted to ACE per RFC 3490 (ToASCII, UseSTD3ASCIIRules) | shall | 7.2 |
| R37 | URIs for comparison MUST be normalized per Section 7.4 | shall | 7.4 |
| R38 | Email host-part with IDN MUST be converted to ACE | shall | 7.5 |

## Informative Annexes (Condensed)
- **Appendix A. Pseudo-ASN.1 Structures and OIDs**: Contains two ASN.1 modules (explicitly and implicitly tagged) defining all data structures, OIDs, attribute types, and upper bounds used in the specification. Not normative but essential for implementation.
- **Appendix B. ASN.1 Notes**: Provides guidance on serial number encoding (non-negative leading '00' octet if necessary), SEQUENCE SIZE constraints, PrintableString limitations, handling of BIT STRING trailing zeros, use of UniversalString, UTF8String, parameterized types, DEFAULT value encoding, OID limits (elements < 2^28, up to 20 elements, string up to 100 bytes), and extensibility rules for ignoring unknown elements in non-critical extensions.
- **Appendix C. Examples**: Four annotated hex dumps: (C.1) RSA self-signed CA certificate, (C.2) RSA end entity certificate, (C.3) DSA end entity certificate with parameters, (C.4) CRL containing one revoked entry. Demonstrates conformance to the profile.