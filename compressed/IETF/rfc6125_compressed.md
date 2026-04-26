# RFC 6125: Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)
**Source**: IETF | **Version**: Standards Track | **Date**: March 2011 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc6125

## Scope (Summary)
This document specifies procedures for representing and verifying the identity of application services in PKIX certificates used with TLS/DTLS. It applies only to fully qualified DNS domain names and PKIX-based systems, and does not supersede RFC 5280 (PKIX) or existing application protocol specifications.

## Normative References
- [DNS-CONCEPTS] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- [DNS-SRV] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [IDNA-DEFS] Klensin, J., "Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework", RFC 5890, August 2010.
- [IDNA-PROTO] Klensin, J., "Internationalized Domain Names in Applications (IDNA): Protocol", RFC 5891, August 2010.
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [LDAP-DN] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names", RFC 4514, June 2006.
- [PKIX] Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [SRVNAME] Santesson, S., "Internet X.509 Public Key Infrastructure Subject Alternative Name for Expression of Service Name", RFC 4985, August 2007.
- [URI] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.

## Definitions and Abbreviations
- **application service**: A service on the Internet enabling clients to connect for information retrieval/upload, communication, or network access.
- **application service provider**: Organization/individual hosting an application service.
- **application service type**: Formal identifier for the application protocol (e.g., URI scheme or DNS SRV Service label).
- **attribute-type-and-value pair**: ASN.1-based RDN construction, building block of Distinguished Names.
- **automated client**: Software agent not directly controlled by a human user.
- **delegated domain**: Domain explicitly configured for communication (by user or admin).
- **derived domain**: Domain automatically derived from source domain (e.g., via DNS SRV lookup).
- **identifier**: Instance of an identifier type presented by server or referenced by client.
- **identifier types**: CN-ID, DNS-ID, SRV-ID, URI-ID (as defined in Section 1.8).
- **interactive client**: Software directly controlled by a human user.
- **pinning**: Caching a name association between certificate and reference identifier after user acceptance of mismatch.
- **PKIX**: Internet Public Key Infrastructure using X.509 as defined in RFC 5280.
- **PKIX certificate**: X.509v3 certificate generated in PKIX context.
- **presented identifier**: Identifier in server's PKIX certificate.
- **reference identifier**: Identifier constructed from source domain and optionally application service type for matching.
- **source domain**: FQDN that client expects in certificate.
- **subjectAltName entry**: Identifier in subjectAltName extension.
- **subjectAltName extension**: PKIX extension binding identifiers to subject.
- **subject field**: Certificate field identifying entity associated with public key.
- **subject name**: Name(s) in subject field and/or subjectAltName.
- **TLS client/server**: Roles in TLS negotiation.

## 1. Introduction
### 1.1 Motivation
Many application protocols use PKIX certificates with TLS. Divergent identity representation/verification rules caused confusion. This document codifies secure procedures for implementation and deployment of PKIX-based authentication.

### 1.2 Audience
Primary: application protocol designers. Secondary: CAs, service providers, client developers.

### 1.3 How to Read This Document
- **Protocol designers**: Section 3 (checklist).
- **CAs**: Section 4 (representation of server identity).
- **Service providers**: Section 5 (requesting certificates).
- **Implementers**: Section 6 (verification).
Terminology (1.8), naming (2), scope (1.7) provide background.

### 1.4 Applicability
Does not supersede [PKIX]. Addresses only leaf end-entity server certificate name forms. Does not supersede existing application protocol specifications.

### 1.5 Overview of Recommendations
- Move away from using Common Name for domain names.
- Use subjectAltName dNSName (DNS-ID).
- Use more specific subjectAltName types (SRV-ID, URI-ID) where appropriate.
- Move away from wildcard certificates (e.g., *.example.com).

### 1.6 Generalization from Current Technologies
Generalizes best practices from IMAP, POP3, HTTP, LDAP, SMTP, XMPP, NNTP, NETCONF, Syslog, SIP, SNMP, GIST.

### 1.7 Scope
#### 1.7.1 In Scope
Service identities associated with FQDNs, TLS/DTLS, PKIX-based systems.

#### 1.7.2 Out of Scope
Client/end-user identities, identifiers other than FQDNs, security protocols other than TLS/DTLS/SSL, non-PKIX systems, CA policies, DNS resolution, user interface issues.

### 1.8 Terminology (Definitions above)

## 2. Naming of Application Services
### 2.1 Naming Application Services
Names based on DNS domain name, optionally supplemented by application service type. Identifier types taxonomy: CN-ID (direct, unrestricted), DNS-ID (direct, unrestricted), SRV-ID (direct or indirect, restricted), URI-ID (direct, restricted).

### 2.2 DNS Domain Names
Two forms:
1. Traditional domain name (LDH labels).
2. Internationalized domain name (contains U-labels or A-labels).

### 2.3 Subject Naming in PKIX Certificates
Subject field is an X.501 Name; subjectAltName extension can contain multiple identifier types. CN-ID is deprecated; preference for subjectAltName entries. RDNs are unordered; order in string representation may vary.

#### 2.3.1 Implementation Notes
Confusion may arise from different renderings. This specification avoids "most specific" terminology; instead uses "CN-ID" defined as RDN with exactly one CN attribute.

## 3. Designing Application Protocols (Checklist)
- If using DNS SRV records: consider recommending SRV-ID.
- If using URIs: consider recommending URI-ID.
- If need backward compatibility: consider CN-ID as fallback.
- If need wildcard: specify exact location (complete left-most label).

## 4. Representing Server Identity
### 4.1 Rules (for Certification Authorities)
1. Certificate **SHOULD** include DNS-ID as baseline.
2. If technology stipulates SRV-ID, certificate **SHOULD** include SRV-ID.
3. If technology stipulates URI-ID, certificate **SHOULD** include URI-ID. Scheme **SHALL** be protocol scheme; host component **SHALL** be FQDN. Reusing specification **MUST** specify acceptable URI schemes.
4. Certificate **MAY** include other application-specific identifiers defined before [SRVNAME].
5. Certificate **SHOULD NOT** include CN-ID unless explicitly encouraged by reusing specification.
6. Certificate **MAY** contain >1 DNS-ID, SRV-ID, URI-ID but **SHOULD NOT** contain >1 CN-ID.
7. Unless allowed by reusing specification, DNS domain name portion **SHOULD NOT** contain wildcard '*' as complete left-most label or fragment.

### 4.2 Examples
- Website: DNS-ID "www.example.com", optional CN-ID.
- IMAP email: SRV-IDs "_imap.example.net", "_imaps.example.net"; DNS-IDs "example.net", "mail.example.net"; optional CN-IDs.
- SIP VoIP: URI-ID "sip:voice.example.edu"; DNS-ID "voice.example.edu"; optional CN-ID.
- XMPP IM: SRV-IDs "_xmpp-client.im.example.org", "_xmpp-server.im.example.org"; DNS-ID "im.example.org"; XmppAddr; optional CN-ID.

## 5. Requesting Server Certificates
- Encourage certificates with all required/recommended identifier types.
- If certificate may be used for any service, request only DNS-ID.
- If for single service, request DNS-ID and optionally SRV-ID or URI-ID.
- If offering multiple services, request separate certificates per service.

## 6. Verifying Service Identity
### 6.1 Overview
Steps: 1) Construct reference identifiers. 2) Server provides certificate. 3) Check each reference against presented identifiers. 4) Match source domain and optionally application service type.

### 6.2 Constructing List of Reference Identifiers
#### 6.2.1 Rules
- **MUST** construct list independently of presented identifiers.
- Inputs must yield source domain and optionally service type. Extracted data **MUST** be securely parsed.
- Each reference identifier **SHOULD** be based on source domain, **SHOULD NOT** on derived domain (except via pinning).
- List **SHOULD** include DNS-ID.
- If service discovered via DNS SRV, list **SHOULD** include SRV-ID.
- If service associated with URI for security, list **SHOULD** include URI-ID.
- List **MAY** include CN-ID for backward compatibility.
- **MUST NOT** check RDNs other than CN.

#### 6.2.2 Examples
- HTTPS browser: DNS-ID "www.example.com", CN-ID fallback.
- IMAPS client: SRV-ID "_imaps.example.net", DNS-IDs "example.net", "mail.example.net", CN-IDs fallback.
- SIP VoIP: URI-ID "sip:voice.example.edu".
- XMPP IM: SRV-ID "_xmpp-client.im.example.org", DNS-ID "im.example.org", XmppAddr.

### 6.3 Preparing to Seek a Match
- Search fails if all reference identifiers exhausted.
- Search succeeds on first match; **SHOULD** stop.
- **MUST NOT** seek match for CN-ID if presented identifiers include DNS-ID, SRV-ID, URI-ID, or application-specific types.
- Split reference identifier into DNS domain name portion and application service type portion as appropriate.

### 6.4 Matching the DNS Domain Name Portion
#### 6.4.1 Traditional Domain Names
Case-insensitive ASCII comparison per [DNS-CASE]. Each label must match, except as supplemented by wildcard rule.

#### 6.4.2 Internationalized Domain Names
Convert U-labels to A-labels; compare as case-insensitive ASCII per [IDNA-PROTO].

#### 6.4.3 Wildcard Certificates
- **MAY** match presented identifier with wildcard '*'.
- **SHOULD NOT** match if wildcard not in left-most label.
- If wildcard only character in left-most label, **SHOULD NOT** compare beyond left-most label of reference identifier.
- **MAY** match if wildcard not only character; **SHOULD NOT** attempt match if embedded in A-label or U-label.

#### 6.4.4 Common Names
Only check CN-ID as last resort if no DNS-ID, SRV-ID, URI-ID, or application-specific types present. Comparison rules same as for DNS domain name.

### 6.5 Matching Application Service Type Portion
#### 6.5.1 SRV-ID
Service name matched case-insensitively; "_" prefix not included.

#### 6.5.2 URI-ID
Scheme name matched case-insensitively; ":" separator not included.

### 6.6 Outcome
#### 6.6.1 Case #1: Match Found
Service identity check succeeded. **MUST** use matched reference identifier as validated identity.

#### 6.6.2 Case #2: No Match, Pinned Certificate
If certificate pinned to a reference identifier (as per Section 1.8) and presented certificate matches pinned certificate (including context), identity check succeeds.

#### 6.6.3 Case #3: No Match, No Pinned Certificate
Proceed as per Section 6.6.4.

#### 6.6.4 Fallback
- Interactive client: **SHOULD** inform user and terminate with bad certificate error.
- Automated client: **SHOULD** terminate with error and log; **MAY** have configuration to disable but **MUST** enable by default.

## 7. Security Considerations
### 7.1 Pinned Certificates
Cached name association **MUST** account for certificate, trust chain, source domain, service type, derived domain, port, and context.

### 7.2 Wildcard Certificates
Wildcard certificates are discouraged due to security risks: they vouch for all hostnames in domain, have ambiguous location rules, and no specification for internationalized domain names. Reusing specifications may allow wildcards for backward compatibility.

### 7.3 Internationalized Domain Names
Can introduce visually similar characters (confusables).

### 7.4 Multiple Identifiers
Multiple DNS-IDs, SRV-IDs, URI-IDs allowed; multiple CN-IDs discouraged. Use of TLS Server Name Indication (SNI) extension recommended for multi-domain support.

## 8. Contributors
Shumon Huque, RL 'Bob' Morgan, Kurt Zeilenga.

## 9. Acknowledgements
Thanks to numerous individuals (listed).

## 10. References
### 10.1 Normative References
(Listed above in Normative References section.)

### 10.2 Informative References
[ABNF], [DNS-CASE], [DNSSEC], [DTLS], [Defeating-SSL], [EMAIL-SRV], [EV-CERTS], [GIST], [HTTP], [HTTP-TLS], [HTTPSbytes], [IDNA2003], [IMAP], [IP], [IPSEC], [IPv6], [LDAP], [LDAP-AUTH], [LDAP-SCHEMA], [LDAP-TLS], [NAPTR], [NETCONF], [NETCONF-SSH], [NETCONF-TLS], [NNTP], [NNTP-TLS], [OCSP], [OPENPGP], [PKIX-OLD], [POP3], [PRIVATE], [S-NAPTR], [SECTERMS], [SIP], [SIP-CERTS], [SIP-SIPS], [SMTP], [SMTP-AUTH], [SMTP-TLS], [SNMP], [SNMP-TLS], [SYSLOG], [SYSLOG-DTLS], [SYSLOG-TLS], [TLS], [TLS-EXT], [US-ASCII], [USINGTLS], [WSC-UI], [X.500], [X.501], [X.509], [X.520], [X.690], [XMPP], [XMPP-OLD].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Certificate SHOULD include DNS-ID as baseline. | SHOULD | Section 4.1 Rule 1 |
| R2 | If technology stipulates SRV-ID, certificate SHOULD include SRV-ID. | SHOULD | Section 4.1 Rule 2 |
| R3 | If technology stipulates URI-ID, certificate SHOULD include URI-ID. Scheme SHALL be protocol scheme; host component SHALL be FQDN. Reusing specification MUST specify acceptable URI schemes. | SHOULD/SHALL/MUST | Section 4.1 Rule 3 |
| R4 | Certificate MAY include other application-specific identifiers defined before [SRVNAME]. | MAY | Section 4.1 Rule 4 |
| R5 | Certificate SHOULD NOT include CN-ID unless explicitly encouraged by reusing specification. | SHOULD NOT | Section 4.1 Rule 5 |
| R6 | Certificate MAY contain >1 DNS-ID, SRV-ID, URI-ID but SHOULD NOT contain >1 CN-ID. | MAY/SHOULD NOT | Section 4.1 Rule 6 |
| R7 | DNS domain name portion SHOULD NOT contain wildcard '*' unless allowed by reusing specification. | SHOULD NOT | Section 4.1 Rule 7 |
| R8 | Client MUST construct reference identifiers independently of presented identifiers. | MUST | Section 6.2.1 |
| R9 | Reference identifier SHOULD be based on source domain, SHOULD NOT on derived domain (except via pinning). | SHOULD/SHOULD NOT | Section 6.2.1 |
| R10 | Client SHOULD include DNS-ID in reference identifier list. | SHOULD | Section 6.2.1 |
| R11 | If service discovered via DNS SRV, client SHOULD include SRV-ID. | SHOULD | Section 6.2.1 |
| R12 | If service associated with URI for security, client SHOULD include URI-ID. | SHOULD | Section 6.2.1 |
| R13 | Client MAY include CN-ID for backward compatibility. | MAY | Section 6.2.1 |
| R14 | Client MUST NOT check RDNs other than CN. | MUST NOT | Section 6.2.1 |
| R15 | Client MUST NOT seek match for CN-ID if presented identifiers include DNS-ID, SRV-ID, URI-ID, or application-specific types. | MUST NOT | Section 6.3 |
| R16 | DNS domain name matching: case-insensitive ASCII for traditional; convert U-labels to A-labels for internationalized. | MUST | Section 6.4.1, 6.4.2 |
| R17 | Wildcard matching rules: SHOULD NOT match if wildcard not in left-most label; if wildcard only character, SHOULD NOT compare beyond left-most label; MAY match if wildcard not only character; SHOULD NOT attempt if embedded in A/U-label. | SHOULD NOT/MAY | Section 6.4.3 |
| R18 | CN-ID only checked as last resort if no DNS-ID, SRV-ID, URI-ID, or application-specific types. Comparison same as DNS domain name. | MAY/MUST | Section 6.4.4 |
| R19 | SRV-ID service name matched case-insensitively. | MUST | Section 6.5.1 |
| R20 | URI-ID scheme name matched case-insensitively. | MUST | Section 6.5.2 |
| R21 | On match found, client MUST use matched reference identifier as validated identity. | MUST | Section 6.6.1 |
| R22 | On no match and pinned certificate matching context, identity check succeeds. | (implied) | Section 6.6.2 |
| R23 | On no match and no pin, interactive client SHOULD inform user and terminate; automated client SHOULD terminate and log error (MAY disable but MUST enable by default). | SHOULD/MAY/MUST | Section 6.6.4 |
| R24 | Service providers SHOULD request certificates with appropriate identifier types; discouraged from requesting single certificate with multiple SRV-IDs/URI-IDs for different service types. | SHOULD | Section 5 |

## Informative Annexes (Condensed)
- **Appendix A: Sample Text**: Provides example text from XMPP specification reusing RFC 6125. XMPP mandates DNS-ID and SRV-ID support, encourages XmppAddr for backward compatibility, allows wildcard as complete left-most label.
- **Appendix B: Prior Art**: Compiles identity verification rules from 11 application protocol specifications (IMAP/POP3/ACAP, HTTP, LDAP, SMTP, XMPP, NNTP, NETCONF, Syslog, SIP, SNMP, GIST). These inform the generalized recommendations but are not superseded.