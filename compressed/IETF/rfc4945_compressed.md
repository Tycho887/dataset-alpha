# RFC 4945: The Internet IP Security PKI Profile of IKEv1/ISAKMP, IKEv2, and PKIX
**Source**: IETF | **Version**: Standards Track | **Date**: August 2007 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4945

## Scope (Summary)
This document defines a profile of IKE (v1 and v2) and PKIX for using PKI technology in IPsec. It specifies requirements for certificate usage, identification payloads, certificate request/response payloads, and X.509 certificate profiles to ensure interoperability.

## Normative References
- [1] Harkins, D. and D. Carrel, "The Internet Key Exchange (IKE)", RFC 2409, November 1998.
- [2] Maughan, D., Schneider, M., and M. Schertler, "Internet Security Association and Key Management Protocol (ISAKMP)", RFC 2408, November 1998.
- [3] Kaufman, C., "Internet Key Exchange (IKEv2) Protocol", RFC 4306, December 2005.
- [4] Kent, S. and R. Atkinson, "Security Architecture for the Internet Protocol", RFC 2401, November 1998.
- [5] Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- [6] Piper, D., "The Internet IP Security Domain of Interpretation for ISAKMP", RFC 2407, November 1998.
- [7] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [8] Postel, J., "Internet Protocol", STD 5, RFC 791, September 1981.
- [9] Nystrom, M. and B. Kaliski, "PKCS #10: Certification Request Syntax Specification Version 1.7", RFC 2986, November 2000.

## Definitions and Abbreviations
- **Peer source address**: The source address in packets from a peer. May differ from any addresses asserted as the "identity".
- **FQDN**: Fully qualified domain name.
- **ID_USER_FQDN**: Referred to as ID_RFC822_ADDR in IKEv2; both referred to as ID_USER_FQDN in this document.
- **The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL"** are as defined in RFC 2119.

## 3. Use of Certificates in RFC 2401 and IKEv1/ISAKMP

### 3.1. Identification Payload
- **General**: Implementations SHOULD populate ID with identity information from the end-entity certificate. The only exception is when ID contains the peer source address (single address, not subnet/range).
- **Verification**: All implementations MUST verify that ID contents correspond to keying material demonstrably held by the peer. Failure may result in insecure policy.
- **ID Type Support Table**:
  - ID_IPV4_ADDR / ID_IPV6_ADDR: MUST support send; SubjectAltName iPAddress; MUST match; SPD lookup: exact match (MUST), substring/wildcard MAY.
  - FQDN: MUST support send; SubjectAltName dNSName; MUST match; SPD lookup: exact (MUST), substring MAY.
  - USER_FQDN: MUST support send; SubjectAltName rfc822Name; MUST match; SPD lookup: exact (MUST), substring MAY.
  - IP range: MUST NOT send.
  - DN: MUST support send; entire Subject; MUST match (binary); SPD MUST support any combination of C, CN, O, OU.
  - GN: MUST NOT send.
  - KEY_ID: out of scope.
- **Matching**: Recipients MUST be able to perform exact SPD matching on ID contents; SHOULD be default. Substring/wildcard MAY be configurable.
- **Recommendation**: FQDN and USER_FQDN are RECOMMENDED over IP addresses.

#### 3.1.1. ID_IPV4_ADDR and ID_IPV6_ADDR
- **Encoding**: MUST be network byte order; IPv4 exactly 4 octets, IPv6 exactly 16 octets.
- **Avoidance**: SHOULD NOT populate ID with IP addresses due to NAT traversal and IP verification issues.
- **Verification**: MUST verify ID matches iPAddress in SubjectAltName (binary comparison); default enabled. Mismatch MUST abort SA setup; SHOULD be auditable.
- **Source IP verification**: MUST verify ID matches source IP in IP header (outermost by default if no config); default enabled. Mismatch MUST abort; SHOULD be auditable.
- **Configuration**: MAY provide option to skip verification, but MUST be off by default.
- **Transitive**: If both defaults enabled, peer source IP matches iPAddress in cert.
- **Policy lookup**: MAY use source IP from header, but MUST still verify ID.

#### 3.1.2. ID_FQDN
- **Support**: MUST support; SHOULD NOT use DNS to map FQDN to IP unless secure (e.g., DNSSEC).
- **Verification**: MUST verify ID matches dNSName in SubjectAltName (case-insensitive string comparison); default enabled. Mismatch MUST abort SA; SHOULD be auditable.
- **Substring/wildcard**: MUST NOT be used for this comparison.
- **Policy lookup**: MAY support substring/wildcard/regex in SPD.

#### 3.1.3. ID_USER_FQDN
- **Support**: MUST support; SHOULD NOT use DNS to map FQDN portion to IP unless secure.
- **Verification**: MUST verify ID matches rfc822Name in SubjectAltName (case-insensitive); default enabled. Mismatch MUST abort SA; SHOULD be auditable.
- **Policy lookup**: MAY support substring/wildcard/regex in SPD.

#### 3.1.4. ID_IPV4_ADDR_SUBNET, ID_IPV6_ADDR_SUBNET, ID_IPV4_ADDR_RANGE, ID_IPV6_ADDR_RANGE
- **Note**: RFC 3779 defines ipAddrBlock extension; use in IKE is experimental.

#### 3.1.5. ID_DER_ASN1_DN
- **Support**: MUST support receiving; MUST be capable of generating.
- **Generating**: MUST populate ID with Subject from end-entity certificate; binary comparison must succeed.
- **Empty Subject**: MUST NOT populate ID if Subject is empty.
- **SPD matching**: MUST support bitwise comparison of entire DN; MUST also support matching any combination of C, CN, O, OU. MAY support additional attributes and substring/wildcard.

#### 3.1.6. ID_DER_ASN1_GN
- **Prohibition**: MUST NOT generate.

#### 3.1.7. ID_KEY_ID
- **Out of scope**: Used for pre-shared keys.

#### 3.1.8. Selecting an Identity from a Certificate
- **Multiple identities**: MUST support certificates with multiple identities (Subject + SubjectAltName, or multiple in SubjectAltName).
- **Choice**: Populate ID with identity likely used in peer's policy (e.g., FQDN, USER_FQDN). In absence of config, local matter.

#### 3.1.9. Subject for DN Only
- **FQDN**: If intended for ID matching, MUST be in dNSName of SubjectAltName; MUST NOT put FQDN in Subject.
- **Other info**: FQDN, USER_FQDN, or IP in Subject MUST NOT be interpreted as identity for ID matching or policy lookup.

#### 3.1.10. Binding Identity to Policy
- **Selection**: Sender should select most appropriate identity from cert; recipient MUST use sent ID as first key for policy selection.
- **Most specific policy**: MUST use most specific policy if overlapping (de-correlation RECOMMENDED over forbidding overlaps).
- **Fallback**: If policy not found with sent ID, recipient MAY use other identities in certificate.

### 3.2. Certificate Request Payload

#### 3.2.1. Certificate Type
- **Relevant types**: X.509 Certificate - Signature; Revocation Lists (CRL/ARL); PKCS #7 wrapped X.509 certificate.
- **Other types**: Out of scope (X.509 Key Exchange, PGP, DNS Signed Key, Kerberos, SPKI, X.509 Attribute).

#### 3.2.2. X.509 Certificate - Signature
- **Usage**: Requests end-entity certificate used for signing.

#### 3.2.3. Revocation Lists (CRL and ARL)
- **Out-of-band**: SHOULD NOT generate CERTREQ with CRL/ARL type. If generated, MUST NOT require response; recipient MAY ignore.
- **CDP/AIA**: Revocation info SHOULD be pointed via CRLDistributionPoints or AuthorityInfoAccess extensions (see Section 5). Implementations SHOULD be able to process and retrieve revocation material from URLs.
- **Configuration**: MUST have ability to configure validation checking per CA. Acquisition SHOULD occur out-of-band of IKE.

#### 3.2.4. PKCS #7 wrapped X.509 certificate
- **Deprecation**: SHOULD NOT require CERTREQs with this type. Receivers MAY treat as synonymous with "X.509 Certificate - Signature".

#### 3.2.5. Location of Certificate Request Payloads
- **IKEv1 Main Mode**: CERTREQ MUST be in messages 4 and 5.

#### 3.2.6. Presence or Absence of Certificate Request Payloads
- **Requirement**: If in-band exchange is desired, MUST send at least one CERTREQ. If no CERTREQ sent, SHOULD NOT expect CERT payloads.

#### 3.2.7. Certificate Requests

##### 3.2.7.1. Specifying Certification Authorities
- **Content**: SHOULD generate CERTREQ for every trust anchor deemed trusted. SHOULD populate Certificate Authority field with Subject of trust anchor (binary comparison).
- **Response**: MUST respond with at least end-entity certificate corresponding to CA in CERTREQ, unless out-of-band configured. MAY send additional certificates.
- **Heuristics**: When multiple end-entity certs to different trust anchors, SHOULD use local heuristics to determine most appropriate CA for CERTREQ.

##### 3.2.7.2. Empty Certification Authority Field
- **General**: SHOULD generate non-empty Certificate Authority field. MAY generate empty under special conditions.
- **Use case**: When responder cannot determine which CA to request (e.g., unknown source IP, many trust anchors). Responder SHOULD first check SPD, then default CAs. If still ambiguous, SHOULD have config option to send empty CERTREQ or terminate with error.
- **Receiving**: Empty CA field means send any/all end-entity certificates regardless of trust anchor.
- **After empty CERTREQ**: If responder receives certificate chaining to unsupported or unconfigured CA, MUST treat as error and abort SA; SHOULD be auditable.
- **Recommendation**: Both options (empty CERTREQ and termination) SHOULD be presented to administrators.

#### 3.2.8. Robustness

##### 3.2.8.1. Unrecognized or Unsupported Certificate Types
- MUST be able to deal with such CERTREQs. MAY treat as supported type with empty CA, depending on local policy.

##### 3.2.8.2. Undecodable Certification Authority Fields
- MUST be able to deal. MAY ignore such payloads.

##### 3.2.8.3. Ordering of Certificate Request Payloads
- MUST NOT assume ordering.

#### 3.2.9. Optimizations

##### 3.2.9.1. Duplicate Certificate Request Payloads
- SHOULD NOT send duplicate CERTREQs.

##### 3.2.9.2. Name Lowest 'Common' Certification Authorities
- MAY send CERTREQ specifying cached end-entity certificates as hints, in addition to normal trust anchor CERTREQs. Recipient MAY elide certificates based on hints. If optimization is used, implementation MUST recognize when end-entity cert has changed and retry without optimization if necessary.

### 3.3. Certificate Payload

#### 3.3.1. Certificate Type
- Same relevant types as CERTREQ: X.509 Certificate - Signature; Revocation Lists (CRL/ARL); PKCS #7 wrapped X.509 certificate.

#### 3.3.2. X.509 Certificate - Signature
- Contains a certificate used for signing.

#### 3.3.3. Revocation Lists (CRL and ARL)
- SHOULD NOT send in IKE. See Section 3.2.3.

#### 3.3.4. PKCS #7 Wrapped X.509 Certificate
- SHOULD NOT generate; SHOULD accept (some implementations generate). Note: may violate ISAKMP's single certificate per payload requirement.

#### 3.3.5. Location of Certificate Payloads
- **IKEv1 Main Mode**: CERT MUST be in messages 5 and 6.

#### 3.3.6. Certificate Payloads Not Mandatory
- If no CERTREQ received, SHOULD NOT send CERTs unless explicitly configured to interoperate with non-compliant implementations. Such proactive sending MUST NOT be default.
- If local policy expects out-of-band certificates, SHOULD ignore CERTREQ messages.
- May terminate exchange if CERTREQ contains only unrecognized CAs to avoid DoS.

#### 3.3.7. Response to Multiple Certification Authority Proposals
- MAY respond with end-entity certificate that chains to any CA identity provided.

#### 3.3.8. Using Local Keying Materials
- MAY skip parsing if same keying materials are cached.

#### 3.3.9. Multiple End-Entity Certificates
- SHOULD NOT send multiple end-entity certs; recipients SHOULD NOT be expected to iterate.
- If multiple sent, they MUST have the same public key.

#### 3.3.10. Robustness

##### 3.3.10.1. Unrecognized or Unsupported Certificate Types
- MUST be able to deal; MAY discard.

##### 3.3.10.2. Undecodable Certificate Data Fields
- MUST be able to deal; MAY discard.

##### 3.3.10.3. Ordering of Certificate Payloads
- MUST NOT assume ordering.

##### 3.3.10.4. Duplicate Certificate Payloads
- MUST support receiving multiple identical CERTs.

##### 3.3.10.5. Irrelevant Certificates
- MUST be prepared to receive irrelevant certs/CRLs; MAY discard.
- MAY send irrelevant certs (e.g., to limit identity leakage). SHOULD NOT send multiple end-entity certs.

#### 3.3.11. Optimizations

##### 3.3.11.1. Duplicate Certificate Payloads
- SHOULD NOT send duplicate CERTs.

##### 3.3.11.2. Send Lowest 'Common' Certificates
- When multiple CERTREQ with different CAs, MAY send shortest chain; SHOULD always send end-entity certificate.

##### 3.3.11.3. Ignore Duplicate Certificate Payloads
- MAY recognize and SHOULD discard duplicates.

##### 3.3.11.4. Hash Payload
- IKEv1 optional Hash Payload: SHOULD include when public key is in a certificate.

## 4. Use of Certificates in RFC 4301 and IKEv2

### 4.1. Identification Payload
- **PAD**: Peer Authorization Database (RFC 4301) provides formal model for binding identity to policy.
- **IDr payload**: IKEv2 adds optional IDr in second exchange. Responder MAY send IDr in third exchange; initiator MUST be able to receive a different type than sent.

### 4.2. Certificate Request Payload

#### 4.2.1. Revocation Lists (CRL and ARL)
- IKEv2 does not support CERT payloads >64K; see Section 3.2.3.

##### 4.2.1.1. IKEv2's Hash and URL of X.509 certificate
- If implementation supports URL lookups, may send HTTP_CERT_LOOKUP_SUPPORTED notification. Sender MUST support http scheme.

##### 4.2.1.2. Location of Certificate Request Payloads
- CERTREQ MUST be in messages 2 and 3.

### 4.3. Certificate Payload

#### 4.3.1. IKEv2's Hash and URL of X.509 Certificate
- Implementation sending HTTP_CERT_LOOKUP_SUPPORTED MUST support http scheme; MAY support ftp; MUST NOT require specific url-path; SHOULD support user-name, password, port in URL.
- Examples of mandatory http forms; ftp example: `ftp://ftp.example.com/pub/certificate.cer`

#### 4.3.2. Location of Certificate Payloads
- CERT MUST be in messages 3 and 4.

#### 4.3.3. Ordering of Certificate Payloads
- MUST NOT assume ordering except the first CERT contains the end-entity certificate used for authentication.

## 5. Certificate Profile for IKEv1/ISAKMP and IKEv2

### 5.1. X.509 Certificates
- **Conformance**: MUST conform to PKIX [5] except where specified.
- **Configuration knobs**: MAY be provided to disable required checks, but all checks MUST be enabled by default.

#### 5.1.1. Versions
- **Version 3 required**: Required extensions necessitate Version 3 for all but self-signed trust anchors. MAY reject V1 and V2 otherwise.

#### 5.1.2. Subject
- **CA implementation**: MUST support at least CN, C, O, OU attributes; SHOULD be configurable per certificate.
- **IKE processing**: See Section 3.1.5 for SPD matching.

##### 5.1.2.1. Empty Subject Name
- MUST accept empty Subject (identity in SubjectAltName).

##### 5.1.2.2. Specifying Hosts not FQDN in Subject
- Use commonName attribute.

##### 5.1.2.3. EmailAddress
- MUST NOT use emailAddress in X.500 distinguished names.

#### 5.1.3. X.509 Certificate Extensions
- **Mandatory recognition**: MUST recognize KeyUsage, SubjectAltName, BasicConstraints.
- **Criticality**: SHOULD generate with criticality as per PKIX; MAY ignore criticality bit for supported extensions; MUST process unsupported critical extensions (reject). See table.

##### 5.1.3.1. AuthorityKeyIdentifier and SubjectKeyIdentifier
- SHOULD NOT assume support. CA should not generate overly complex hierarchies.

##### 5.1.3.2. KeyUsage
- If KeyUsage present, digitalSignature or nonRepudiation MUST be set (may be both). Otherwise, continue.

##### 5.1.3.3. PrivateKeyUsagePeriod
- CA MUST NOT generate; IKE SHOULD ignore if present.

##### 5.1.3.4. CertificatePolicies
- CA SHOULD NOT mark critical. Relaying party that can process SHOULD NOT reject.

##### 5.1.3.5. PolicyMappings
- CA SHOULD NOT mark critical.

##### 5.1.3.6. SubjectAltName
- For ID types FQDN, USER_FQDN, IPV4_ADDR, IPV6_ADDR, cert MUST have corresponding SubjectAltName with same data.
- SHOULD generate only rfc822Name, dNSName, iPAddress.
- SHOULD NOT assume support for other GeneralName choices.

###### 5.1.3.6.1. dNSName
- If ID is FQDN, dNSName MUST match (case-insensitive). MUST NOT contain wildcards; MAY treat as invalid.
- SHOULD NOT assume DNS resolution; failure to resolve not an error.

###### 5.1.3.6.2. iPAddress
- If ID is IPV4_ADDR/IPV6_ADDR, iPAddress MUST match. CIDR prohibited in SubjectAltName.

###### 5.1.3.6.3. rfc822Name
- If ID is USER_FQDN, rfc822Name MUST match. SHOULD NOT assume valid email address.

##### 5.1.3.7. IssuerAltName
- CA SHOULD NOT assume support; not for display.

##### 5.1.3.8. SubjectDirectoryAttributes
- IKE MAY ignore when non-critical.

##### 5.1.3.9. BasicConstraints
- CA certs MUST contain this extension, critical. IKE SHOULD reject CA certs without it; backwards compatibility MAY be configurable, but default MUST reject.

##### 5.1.3.10. NameConstraints
- CA SHOULD NOT generate due to interoperability.

##### 5.1.3.11. PolicyConstraints
- CA SHOULD NOT generate.

##### 5.1.3.12. ExtendedKeyUsage
- CA SHOULD NOT include EKU for IKE. Historical IPsec EKU values deprecated.
- Defines id-kp-ipsecIKE (OID 1.3.6.1.5.5.7.3.17). If EKU present, must contain id-kp-ipsecIKE or anyExtendedKeyUsage; otherwise reject.

##### 5.1.3.13. CRLDistributionPoints
- CA SHOULD issue certs with populated CDP.
- IKE MUST support validating CDP vs IssuingDistributionPoint to prevent substitution.
- CDPs SHOULD be resolvable.

##### 5.1.3.14. InhibitAnyPolicy
- CA SHOULD NOT generate.

##### 5.1.3.15. FreshestCRL
- IKE MUST NOT assume presence; delta CRLs not widely supported.

##### 5.1.3.16. AuthorityInfoAccess
- SHOULD support (for OCSP).

##### 5.1.3.17. SubjectInfoAccess
- No known use for IPsec; SHOULD ignore.

### 5.2. X.509 Certificate Revocation Lists

- **Revocation checking**: MUST use certificate revocation information; SHOULD support CRLs unless non-CRL methods are sole method.
- **Deployments**: SHOULD populate CDP.
- **Configuration**: MAY provide option to disable revocation, but MUST be off by default.

#### 5.2.1. Multiple Sources of Certificate Revocation Information
- Act conservatively: if any trusted source reports revoked, MUST consider revoked.

#### 5.2.2. X.509 Certificate Revocation List Extensions

##### 5.2.2.1. AuthorityKeyIdentifier
- CA SHOULD NOT assume support; avoid complex hierarchies.

##### 5.2.2.2. IssuerAltName
- CA SHOULD NOT assume support.

##### 5.2.2.3. CRLNumber
- Issuers MUST include in all CRLs.

##### 5.2.2.4. DeltaCRLIndicator
- If unsupported, MUST reject CRL with DeltaCRLIndicator (critical) and use base CRL if available.
- **Recommendation**: NOT to issue delta CRLs at this time due to insecure implementations.

##### 5.2.2.5. IssuingDistributionPoint
- If used, distributionPointName in CDP MUST be identical to distributionPoint in IssuingDistributionPoint.

##### 5.2.2.6. FreshestCRL
- RECOMMENDS not populating (used for delta CRLs).

### 5.3. Strength of Signature Hashing Algorithms
- MUST be able to validate with RSA-with-SHA1 and RSA-with-MD5.
- SHOULD support sha256WithRSAEncryption (PKCS#1 v1.5) as soon as possible.

## 6. Configuration Data Exchange Conventions

- **Format**: Base64 [19] encoded with delimiters as specified.
- **Line handling**: MUST support arbitrary leading/trailing whitespace, arbitrary line lengths (SHOULD <76 chars), and LF/CR/CRLF line endings.

### 6.1. Certificates
```
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
```

### 6.2. CRLs and ARLs
```
-----BEGIN CRL-----
-----END CRL-----
```

### 6.3. Public Keys
- Two forms: certificates (as above) and raw keys (SubjectPublicKeyInfo).
- Raw key delimiter:
```
-----BEGIN PUBLIC KEY-----
-----END PUBLIC KEY-----
```

### 6.4. PKCS#10 Certificate Signing Requests
```
-----BEGIN CERTIFICATE REQUEST-----
-----END CERTIFICATE REQUEST-----
```

## 7. Security Considerations

### 7.1. Certificate Request Payload
- CERTREQ contents not encrypted; may leak private information. Empty CA option may reduce leakage at performance cost.

### 7.2. IKEv1 Main Mode
- CERTs may be included in any message; using privacy-protected messages (5 and 6) recommended.
- Responding with CERTs in unprotected messages (e.g., message 2) violates identity protection.

### 7.3. Disabling Certificate Checks
- Any config option to simplify/modify/disable verification MUST default to "enabled". Appropriate to warn users when disabling.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | ID SHOULD be populated with identity from end-entity cert. | SHOULD | Section 3.1 |
| R2 | All implementations MUST verify ID corresponds to peer's keying material. | MUST | Section 3.1 |
| R3 | Implementations MUST support exact matching of ID to SPD entry. | MUST | Section 3.1 |
| R4 | When sending IPV4_ADDR/IPV6_ADDR, implementation MUST verify ID matches iPAddress in cert (binary). Default enabled. | MUST | Section 3.1.1 |
| R5 | When sending IP address type, implementation MUST verify ID matches source IP in header. Default enabled. | MUST | Section 3.1.1 |
| R6 | Mismatch in IP or source IP verification MUST abort SA setup. | MUST | Section 3.1.1 |
| R7 | Configuration option to skip IP verification MUST be off by default. | MUST | Section 3.1.1 |
| R8 | When sending FQDN, MUST verify ID matches dNSName (case-insensitive). Default enabled. | MUST | Section 3.1.2 |
| R9 | Substring/wildcard MUST NOT be used for FQDN comparison. | MUST | Section 3.1.2 |
| R10 | When sending USER_FQDN, MUST verify ID matches rfc822Name (case-insensitive). Default enabled. | MUST | Section 3.1.3 |
| R11 | When sending DN, MUST populate ID with entire Subject; binary comparison must succeed. | MUST | Section 3.1.5 |
| R12 | Implementations MUST support at least C, CN, O, OU for SPD matching. | MUST | Section 3.1.5 |
| R13 | Implementations MUST NOT generate ID_DER_ASN1_GN. | MUST | Section 3.1.6 |
| R14 | If FQDN intended for ID matching, MUST be in dNSName, not Subject. | MUST | Section 3.1.9 |
| R15 | In IKEv1 Main Mode, CERTREQ MUST be in messages 4 and 5. | MUST | Section 3.2.5 |
| R16 | If in-band cert exchange desired, MUST send at least one CERTREQ. | MUST | Section 3.2.6 |
| R17 | When responding to CERTREQ, MUST send at least end-entity cert corresponding to CA, unless out-of-band. | MUST | Section 3.2.7.1 |
| R18 | Empty CA CERTREQ allowed; after receiving empty, responder MUST abort SA if cert chains to unsupported CA. | MUST | Section 3.2.7.2 |
| R19 | Implementations MUST be able to handle unrecognized/unsupported CERTREQ types. | MUST | Section 3.2.8.1 |
| R20 | Implementations MUST NOT assume ordering of CERTREQ or CERT payloads. | MUST | Sections 3.2.8.3, 3.3.10.3 |
| R21 | In IKEv1 Main Mode, CERT MUST be in messages 5 and 6. | MUST | Section 3.3.5 |
| R22 | If no CERTREQ received, SHOULD NOT send CERTs (unless explicitly configured for non-compliant peers). | SHOULD | Section 3.3.6 |
| R23 | Multiple end-entity certs if sent MUST have same public key. | MUST | Section 3.3.9 |
| R24 | Implementations MUST support receiving duplicate CERTs. | MUST | Section 3.3.10.4 |
| R25 | For IKEv2, CERTREQ MUST be in messages 2 and 3. | MUST | Section 4.2.1.2 |
| R26 | For IKEv2, CERT MUST be in messages 3 and 4. | MUST | Section 4.3.2 |
| R27 | For IKEv2, first CERT must contain end-entity cert. | MUST | Section 4.3.3 |
| R28 | Implementations MUST conform to PKIX certificate profile except where specified. | MUST | Section 5.1 |
| R29 | All certificate checks MUST be enabled by default. | MUST | Section 5.1 |
| R30 | CA implementations MUST include BasicConstraints extension in CA certs (critical). | MUST (CA) | Section 5.1.3.9 |
| R31 | For IKE, if KeyUsage present, digitalSignature or nonRepudiation MUST be set. | MUST | Section 5.1.3.2 |
| R32 | For IKE, if EKU present, must contain id-kp-ipsecIKE or anyExtendedKeyUsage. | MUST | Section 5.1.3.12 |
| R33 | IKE implementations MUST use revocation information; SHOULD support CRLs. | MUST/SHOULD | Section 5.2 |
| R34 | CA issuers MUST include CRLNumber extension in all CRLs. | MUST | Section 5.2.2.3 |
| R35 | Implementations MUST be able to validate RSA-with-SHA1 and RSA-with-MD5. | MUST | Section 5.3 |
| R36 | Implementations MUST support Base64 certificate/CRL/key exchange with specified delimiters. | MUST | Section 6 |

## Informative Annexes (Condensed)

- **Appendix A. The Possible Dangers of Delta CRLs**: Describes insecure implementations that incorrectly process delta CRLs, potentially missing revocation checking. Recommends against issuing delta CRLs until implementations are fixed.

- **Appendix B. More on Empty CERTREQs**: Explains the common convention that an empty CERTREQ means "send any certificate". Provides justification and example scenarios where initiator must have local policy to choose correct certificate when multiple are available.