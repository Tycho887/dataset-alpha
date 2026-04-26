# RFC 9525: Service Identity in TLS
**Source**: IETF | **Version**: Standards Track | **Date**: November 2023 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/info/rfc9525

## Scope (Summary)
This document specifies procedures for representing and verifying the identity of application services in TLS, DTLS, QUIC, and related protocols using PKIX certificates. It obsoletes RFC 6125.

## Normative References
- [PKIX] – RFC 5280  
- [DNS-CONCEPTS] – RFC 1034  
- [DNS-SRV] – RFC 2782  
- [DNS-WILDCARDS] – RFC 4592  
- [IDNA-DEFS] – RFC 5890  
- [IDNA-PROTO] – RFC 5891  
- [IPv4] – RFC 791  
- [IPv6] – RFC 4291  
- [LDAP-DN] – RFC 4514  
- [RFC2119] – BCP 14  
- [RFC8174] – BCP 14  
- [SRVNAME] – RFC 4985  
- [TLS-REC] – RFC 9325  
- [URI] – STD 66, RFC 3986

## Definitions and Abbreviations
- **DNS-ID**: A subjectAltName entry of type dNSName (RFC 5280).  
- **IP-ID**: A subjectAltName entry of type iPAddress (RFC 5280).  
- **SRV-ID**: A subjectAltName entry of type otherName with name form SRVName (RFC 4985).  
- **URI-ID**: A subjectAltName entry of type uniformResourceIdentifier (RFC 5280).  
- **PKIX**: Internet Public Key Infrastructure using X.509 (RFC 5280).  
- **presented identifier**: An identifier in a PKIX certificate presented by a server.  
- **reference identifier**: An identifier expected by the client, constructed from source domain and optionally application service type.  
- **source domain**: The FQDN that a client expects in the certificate.  
- **subjectAltName entry**: An identifier in the subjectAltName extension.  
- **application service type**: Formal identifier (URI scheme, DNS SRV Service, ALPN ID).  
- **RDN**: Relative Distinguished Name (RFC 4514).

## 1. Introduction
### 1.1 Motivation
Client verifies that server’s presented certificate matches its reference identity using the rules defined herein.

### 1.2 Applicability
Does not supersede PKIX certificate issuance/validation. Addresses only leaf server certificate name forms, not certification path.

### 1.3 Overview of Recommendations
- Only check DNS domain names via dNSName subjectAltName.  
- Allow more specific types: uniformResourceIdentifier, iPAddress, SRVName.  
- Wildcard only as complete left-most label.  
- Do not use Common Name (CN) for identity.

### 1.4 Scope
#### In Scope
- TLS, DTLS, and QUIC using PKIX certificates.  
- Identities in X.509 certificates or derived credentials (e.g., DANE, delegated credentials).

#### Out of Scope
- Security protocols other than TLS/DTLS/QUIC.  
- Non-PKIX certificates.  
- Client identities.  
- Identification using other than domain name, IP address, or SRV service name.  
- CA policies.  
- DNS resolution process.  
- User interface issues.

### 1.5 Terminology
(see Definitions and Abbreviations above)

## 2. Identifying Application Services
- DNS-ID, IP-ID, SRV-ID, URI-ID are the identifier types.  
- Common Name RDN **MUST NOT** be used to identify a service.  
- Other RDNs within subjectName **MUST NOT** be used.  
- Protocol specifications **MUST** specify which identifiers are mandatory to implement.  
- Protocol specifications **SHOULD** provide operational guidance when necessary.  
- An IP address resulting from a DNS query is indirect; use of indirect IP-IDs is out of scope.

## 3. Designing Application Protocols
- A specification **MAY** choose to allow only one identifier type.  
- If technology does not use DNS SRV records, specification **MUST** state that SRV-ID is not supported.  
- If technology does not use URIs, specification **MUST** state that URI-ID is not supported.  
- A technology **MAY** disallow wildcard certificates; if so, specification **MUST** state that wildcard certificates are not supported.

## 4. Representing Server Identity
### 4.1 Rules
1. Certificate **MUST** include at least one identifier.  
2. Certificate **SHOULD** include a DNS-ID.  
3. If relevant specification stipulates SRV-ID, certificate **SHOULD** include an SRV-ID.  
4. If relevant specification stipulates URI-ID, certificate **SHOULD** include a URI-ID; scheme **MUST** be that of the protocol; “host” component **MUST** be the FQDN; application protocol specification **MUST** specify acceptable URI schemes.  
5. Certificate **MAY** contain more than one DNS-ID, SRV-ID, URI-ID, or IP-ID.  
6. Certificate **MAY** include other application-specific identifiers (out of scope for this document).

### 4.2 Examples
(condensed: examples illustrate typical combinations of DNS-ID, IP-ID, SRV-ID, URI-ID for web, email, SIP, XMPP services)

## 5. Requesting Server Certificates
- Service providers **SHOULD** request certificates with as few identifiers as necessary.  
- **SHOULD** request certificates including all required/recommended identifier types for the application service type.  
- If used for a single application service type, **SHOULD** request DNS-ID/IP-ID or, if appropriate, SRV-ID/URI-ID.  
- If used for any type, **SHOULD** request only DNS-IDs or IP-IDs.  
- If offering multiple types and wishing to limit applicability using SRV-IDs/URI-IDs, **SHOULD** request multiple certificates (except for application service type bundles like email).

## 6. Verifying Service Identity
### 6.1 Constructing a List of Reference Identifiers
#### 6.1.1 Rules
- Client **MUST** construct list of reference identifiers independently of server presented identifiers.  
- Reference identifiers derived from source domain and optionally application service type.  
- If server for service type typically associated with URI, reference identifier **SHOULD** be a URI-ID.  
- If typically discovered via DNS SRV, reference identifier **SHOULD** be an SRV-ID.  
- If reference is an IP address, reference identifier is an IP-ID.  
- In absence of more specific, reference identifier is a DNS-ID.  
- Intermediate values from DNS resolution are not reference identifiers and **MUST NOT** be treated as such.

#### 6.1.2 Examples
(condensed: examples for HTTPS, IMAPS, SIP, XMPP showing appropriate reference identifiers)

### 6.2 Preparing to Seek a Match
- Client splits reference identifiers into components: domain name or IP address and optionally application service type.  
- For DNS-ID: used directly as DNS domain name.  
- For IP-ID: exactly match iPAddress octets; no partial matching.  
- For SRV-ID: DNS domain name = Name, service type = Service.  
- For URI-ID: DNS domain name = “reg-name” part of “host”, service type = scheme.  
- If domain name, client **MUST** match DNS name per Section 6.3.  
- If IP address, client **MUST** match IP address per Section 6.4.  
- If application service type present, **MUST** match per Section 6.5.

### 6.3 Matching the DNS Domain Name Portion
- For non-IDN: **MUST** use case-insensitive ASCII comparison of labels.  
- For IDN: **MUST** convert U-labels to A-labels; compare as case-insensitive ASCII.  
- If wildcard supported, client **MUST** match presented identifier with wildcard "*" only if:
  1. Only one wildcard character.  
  2. Wildcard appears only as complete content of the left-most label.  
- If requirements not met, presented identifier is invalid and **MUST** be ignored.  
- Wildcard matches only one label in reference identifier.

### 6.4 Matching an IP Address Portion
- **MUST** use octet-for-octet comparison of the iPAddress bytes.  
- For IP address in URI-ID: parse “host” as IPv6address or IPv4address; compare resulting octets.

### 6.5 Matching the Application Service Type Portion
- SRV-ID: application service name **MUST** be matched case-insensitively (underscore "_" is part of name).  
- URI-ID: scheme name **MUST** be matched case-insensitively (colon ":" is separator).

### 6.6 Outcome
- If match found: client **MUST** use matched reference identifier as validated identity.  
- If no match:  
  - Automated application: **SHOULD** terminate with bad certificate error; application **MAY** provide config setting to disable but **MUST NOT** disable by default.  
  - Human-controlled client: **SHOULD** inform user and automatically terminate; **MAY** give advanced users option to proceed after caution (force user to view entire certification path).  
  - Application **MAY** present ability to accept certificate for subsequent connections (pinning); such pinning **SHOULD NOT** restrict to only that certificate; local policy for static pinning **SHOULD** be prior configuration.

## Security Considerations (Condensed)
- **Wildcard Certificates (7.1)**: Wildcards vouch for any single-label hostname; restrict to only one wildcard as left-most label; application protocols may disallow wildcards entirely.  
- **Uniform Resource Identifiers (7.2)**: URI-ID must include “scheme” and “host” matching “reg-name”; other components ignored.  
- **Internationalized Domain Names (7.3)**: Matching on A-labels only; visual confusion is a UI concern.  
- **IP Addresses (7.4)**: SNI only conveys domain names; clients with IP-ID cannot use SNI; IPv4 text may be misinterpreted as FQDN.  
- **Multiple Presented Identifiers (7.5)**: Multiple names in certificate share risk; mitigate by limiting names and using strong TLS configuration.  
- **Multiple Reference Identifiers (7.6)**: CA name constraints may not cover all identifier types; client should ensure constraints apply to all acceptable types.  
- **Certificate Trust (7.7)**: Trusting a CA means trusting all its certificates; additional checks (e.g., block lists) are the responsibility of the application protocol or client.

## IANA Considerations
This document has no IANA actions.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Common Name RDN MUST NOT be used to identify a service. | MUST | Section 2 |
| R2 | Other RDNs within subjectName MUST NOT be used. | MUST | Section 2 |
| R3 | Protocol specifications MUST specify mandatory identifiers. | MUST | Section 2 |
| R4 | Protocol specifications SHOULD provide operational guidance. | SHOULD | Section 2 |
| R5 | If technology does not use DNS SRV, MUST state SRV-ID not supported. | MUST | Section 3 |
| R6 | If technology does not use URIs, MUST state URI-ID not supported. | MUST | Section 3 |
| R7 | If disallowing wildcards, MUST state wildcard certificates not supported. | MUST | Section 3 |
| R8 | Certificate MUST include at least one identifier. | MUST | Section 4.1 Rule 1 |
| R9 | Certificate SHOULD include a DNS-ID. | SHOULD | Section 4.1 Rule 2 |
| R10 | If relevant spec stipulates SRV-ID, certificate SHOULD include it. | SHOULD | Section 4.1 Rule 3 |
| R11 | If URI-ID included, scheme MUST be that of protocol; host MUST be FQDN; spec MUST specify acceptable schemes. | MUST | Section 4.1 Rule 4 |
| R12 | Certificate MAY contain multiple DNS-IDs, SRV-IDs, URI-IDs, or IP-IDs. | MAY | Section 4.1 Rule 5 |
| R13 | Service providers SHOULD request certificates with as few identifiers as necessary. | SHOULD | Section 5 |
| R14 | Service providers SHOULD request certificates including all required/recommended identifier types. | SHOULD | Section 5 |
| R15 | If used for single type, SHOULD request DNS-ID/IP-ID or appropriate SRV-ID/URI-ID. | SHOULD | Section 5 |
| R16 | If used for any type, SHOULD request only DNS-IDs or IP-IDs. | SHOULD | Section 5 |
| R17 | If offering multiple types and limiting via SRV-ID/URI-ID, SHOULD request multiple certificates (except email bundles). | SHOULD | Section 5 |
| R18 | Client MUST construct reference identifiers independently of presented identifiers. | MUST | Section 6.1.1 |
| R19 | Intermediate values from DNS resolution are not reference identifiers and MUST NOT be treated as such. | MUST | Section 6.1.1 |
| R20 | For non-IDN, DNS matching MUST use case-insensitive ASCII comparison. | MUST | Section 6.3 |
| R21 | For IDN, MUST convert U-labels to A-labels; compare as case-insensitive ASCII. | MUST | Section 6.3 |
| R22 | If wildcard supported, MUST match only if one wildcard as complete left-most label; otherwise invalid and MUST be ignored. | MUST | Section 6.3 |
| R23 | IP-ID matching MUST be octet-for-octet comparison. | MUST | Section 6.4 |
| R24 | SRV-ID application service name MUST be matched case-insensitively. | MUST | Section 6.5 |
| R25 | URI-ID scheme name MUST be matched case-insensitively. | MUST | Section 6.5 |
| R26 | If match found, client MUST use matched reference identifier as validated identity. | MUST | Section 6.6 |
| R27 | If no match, automated application SHOULD terminate with bad certificate error. | SHOULD | Section 6.6 |
| R28 | Automated application MAY provide config setting to disable but MUST NOT disable by default. | MUST | Section 6.6 |
| R29 | Human-controlled client SHOULD inform user and automatically terminate. | SHOULD | Section 6.6 |
| R30 | Human-controlled client MAY give advanced users option to proceed after caution. | MAY | Section 6.6 |
| R31 | Ad hoc pinning SHOULD NOT restrict to only that certificate. | SHOULD | Section 6.6 |
| R32 | Local policy for static pinning SHOULD be prior configuration. | SHOULD | Section 6.6 |

## Informative Annexes (Condensed)
- **Appendix A. Changes from RFC 6125**: Removed CN-ID; wildcard only as left-most label; updated pinning guidance; added IP-ID; shortened title.