# RFC 4033: DNS Security Introduction and Requirements
**Source**: IETF | **Version**: Standards Track | **Date**: March 2005 | **Type**: Normative
**Original**: (No path provided; RFC 4033)

## Scope (Summary)
This document introduces the Domain Name System Security Extensions (DNSSEC), which provide data origin authentication and data integrity for DNS data. It describes the capabilities and limitations of these extensions, defines key terms, and outlines the interrelationships among the documents that collectively specify DNSSEC.

## Normative References
- [RFC1034] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- [RFC1035] Mockapetris, P., "Domain names - implementation and specification", STD 13, RFC 1035, November 1987.
- [RFC2535] Eastlake 3rd, D., "Domain Name System Security Extensions", RFC 2535, March 1999.
- [RFC2671] Vixie, P., "Extension Mechanisms for DNS (EDNS0)", RFC 2671, August 1999.
- [RFC3225] Conrad, D., "Indicating Resolver Support of DNSSEC", RFC 3225, December 2001.
- [RFC3226] Gudmundsson, O., "DNSSEC and IPv6 A6 aware server/resolver message size requirements", RFC 3226, December 2001.
- [RFC3445] Massey, D. and S. Rose, "Limiting the Scope of the KEY Resource Record (RR)", RFC 3445, December 2002.
- [RFC4034] Arends, R., Austein, R., Larson, M., Massey, D., and S. Rose, "Resource Records for DNS Security Extensions", RFC 4034, March 2005.
- [RFC4035] Arends, R., Austein, R., Larson, M., Massey, D., and S. Rose, "Protocol Modifications for the DNS Security Extensions", RFC 4035, March 2005.

## Definitions and Abbreviations
- **Authentication Chain**: An alternating sequence of DNSKEY RRsets and DS RRsets forms a chain of signed data, with each link vouching for the next.
- **Authentication Key**: A public key that a security-aware resolver has verified and can therefore use to authenticate data.
- **Authoritative RRset**: Within a zone, an RRset is authoritative if its owner name lies at or below the zone apex and at or above delegation cuts (with exceptions for parental NSEC and DS RRsets).
- **Delegation Point**: The name at the parental side of a zone cut (e.g., foo.example in the example zone).
- **Island of Security**: A signed, delegated zone that does not have an authentication chain from its delegating parent (i.e., no DS RR in the parent).
- **Key Signing Key (KSK)**: An authentication key whose corresponding private key is used to sign one or more other authentication keys (typically ZSKs) for a zone.
- **Non-Validating Security-Aware Stub Resolver**: A security-aware stub resolver that trusts one or more security-aware recursive name servers to perform validation on its behalf.
- **Non-Validating Stub Resolver**: A less tedious term for a non-validating security-aware stub resolver.
- **Security-Aware Name Server**: An entity that understands DNSSEC, supports EDNS0, the DO bit, and the new RR types and header bits.
- **Security-Aware Recursive Name Server**: An entity that acts as both a security-aware name server and a security-aware resolver.
- **Security-Aware Resolver**: An entity that sends DNS queries with EDNS0 support and the DO bit, capable of using DNSSEC RR types and header bits.
- **Security-Aware Stub Resolver**: A stub resolver with enough understanding of DNSSEC to provide additional services; may be validating or non-validating.
- **Security-Oblivious \<anything\>**: Anything that is not security-aware.
- **Signed Zone**: A zone whose RRsets are signed and that contains properly constructed DNSKEY, RRSIG, NSEC, and (optionally) DS records.
- **Trust Anchor**: A configured DNSKEY RR or DS RR hash that a validating resolver uses as a starting point for building the authentication chain.
- **Unsigned Zone**: A zone that is not signed.
- **Validating Security-Aware Stub Resolver**: A security-aware stub resolver that performs signature validation on its own rather than trusting an upstream recursive name server.
- **Validating Stub Resolver**: A less tedious term for a validating security-aware stub resolver.
- **Zone Apex**: The name at the child's side of a zone cut (as opposed to delegation point).
- **Zone Signing Key (ZSK)**: An authentication key whose corresponding private key is used to sign zone data.

## Services Provided by DNS Security
### 3.1 Data Origin Authentication and Data Integrity
- DNSSEC provides authentication by associating digital signatures with DNS RRsets via the RRSIG RR.
- A security-aware resolver can learn a zone's public key either by configured trust anchor or by normal DNS resolution using the DNSKEY RR.
- Security-aware resolvers authenticate zone information by forming an authentication chain from a newly learned public key back to a previously known authentication key.
- **Delegation Signer (DS) RR**: Simplifies signing delegations across organizational boundaries; resides in the parent zone and indicates the public key(s) used to sign the child zone's DNSKEY RRset.
- Typical authentication chain: DNSKEY -> [DS -> DNSKEY]* -> RRset.
- **Local Policy**: Authenticating keys and data is ultimately a matter of local policy, which may extend or override protocol extensions.

### 3.2 Authenticating Name and Type Non-Existence
- The NSEC RR allows a security-aware resolver to authenticate a negative reply for name or type non-existence.
- NSEC chains explicitly describe gaps between domain names and list types present at existing names; each NSEC RR is signed using the mechanisms of Section 3.1.

## Services Not Provided by DNS Security
- DNSSEC does **not** provide confidentiality, access control lists, or differentiation between inquirers.
- DNSSEC provides **no** protection against denial of service attacks; it introduces new cryptographic denial-of-service vectors.
- DNSSEC does **not** protect zone transfers or dynamic update; message authentication schemes (e.g., [RFC2845], [RFC2931]) address those.

## Scope of the DNSSEC Document Set and Last Hop Issues
- A validating resolver can determine four states:
  - **Secure**: Trust anchor, chain of trust, all signatures verified.
  - **Insecure**: Trust anchor, chain of trust, signed proof of non-existence of a DS record at some delegation point.
  - **Bogus**: Trust anchor and secure delegation, but response fails validation.
  - **Indeterminate**: No trust anchor indicating security; default mode.
- This specification defines signaling of bogus data via RCODE=2 (Server Failure) and of secure data via the AD bit. It does **not** define a format for detailed error signaling; this is a topic for future work.

## Resolver Considerations (Section 6)
- **R1**: A security-aware resolver **must** be able to perform cryptographic functions necessary to verify digital signatures using at least the mandatory-to-implement algorithm(s).
- **R2**: A security-aware resolver **must** be capable of forming an authentication chain from a newly learned zone back to an authentication key.
- **R3**: A security-aware resolver **should** be configured with at least one trust anchor.
- **R4**: A security-aware resolver **should** take a signature's validation period into consideration when determining the TTL of cached data, avoiding caching beyond signature validity.
- **R5**: A security-aware resolver that is part of a recursive name server **shall** pay careful attention to the CD bit to avoid blocking valid signatures (see [RFC4035]).

## Stub Resolver Considerations (Section 7)
- **R6**: For a security-oblivious stub resolver to rely on DNSSEC, it **must** trust both the recursive name servers and the communication channels to them.
- **R7**: A security-aware stub resolver that trusts its recursive name servers and channel **may** use the AD bit as a hint about validated data.
- **R8**: A validating stub resolver **can** set the CD bit in queries to perform its own signature validation.

## Zone Considerations (Section 8)
- **R9**: A signed zone **will** contain additional records: RRSIG, DNSKEY, DS, and NSEC.
- **R10**: Signed zone requires regular maintenance to ensure each RRset has a current valid RRSIG RR.
- **R11**: Re-signing any RRset **must** increment the zone's SOA serial number and re-sign the SOA RRset, potentially triggering NOTIFY and zone transfers.

### 8.1 TTL Values vs. RRSIG Validity Period
- TTL defines cache coherency; RRSIG inception/expiration define signature validity.
- Validity period cannot be extended by TTL; resolver may use time before signature expiration as an upper bound for cache TTL.

## Name Server Considerations (Section 9)
- **R12**: A security-aware name server **should** include appropriate DNSSEC records (RRSIG, DNSKEY, DS, NSEC) in responses to queries with the DO bit set, subject to message size limits.
- **R13**: A security-aware name server **must** support the EDNS "sender's UDP payload" mechanism to handle increased message sizes.
- **R14**: If possible, private keys **should** be kept offline; for dynamic update zones, the ZSK private key **must** be kept online.
- **R15**: Zone maintenance operations (e.g., transfers) **shall** use additional mechanisms (TSIG, SIG(0), IPsec) for integrity.

## DNS Security Document Family (Section 10)
- **DNSSEC protocol document set**: RFC 4033 (this), RFC 4034 (Resource Records), RFC 4035 (Protocol Modifications).
- **Digital Signature Algorithm Specification** documents: describe implementation of specific algorithms per DNSSEC format.
- **Transaction Authentication Protocol** documents: cover DNS message authentication (TSIG, SIG(0)).
- **New Security Uses** documents: propose use of DNSSEC for other security purposes (e.g., [RFC2538]).

## IANA Considerations (Section 11)
- This overview introduces no IANA considerations. See [RFC4034] for IANA considerations.

## Security Considerations (Section 12)
- DNSSEC provides data origin authentication and integrity but has limitations:
  - All zones along the authentication chain must be signed; security-aware resolvers cannot verify unsigned zones or through non-security-aware intermediaries.
  - Non-validating stub resolvers are vulnerable to attacks on recursive name servers and channels; channel security is recommended.
  - DNSSEC does **not** protect against denial of service; it introduces new cryptographic resource consumption attacks.
  - DNSSEC does **not** provide confidentiality.
  - NSEC chains allow zone enumeration.
  - DNSSEC adds complexity, creating opportunities for implementation bugs and misconfigurations that may render legitimate zones unreachable.
  - DNSSEC does **not** protect unsigned non-authoritative data at zone cuts (glue, NS RRs); other mechanisms must protect zone transfers.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Security-aware resolver **must** be able to perform cryptographic functions for at least mandatory algorithms. | must | Section 6 |
| R2 | Security-aware resolver **must** be capable of forming an authentication chain. | must | Section 6 |
| R3 | Security-aware resolver **should** be configured with at least one trust anchor. | should | Section 6 |
| R4 | Security-aware resolver **should** consider signature validity period when caching TTL. | should | Section 6 |
| R5 | Security-aware resolver in recursive server **shall** handle CD bit to avoid blocking valid signatures. | shall | Section 6, per [RFC4035] |
| R6 | Security-oblivious stub resolver relying on DNSSEC **must** trust recursive name servers and channels. | must | Section 7 |
| R7 | Security-aware stub resolver **may** use AD bit as hint. | may | Section 7 |
| R8 | Validating stub resolver **can** set CD bit for own validation. | (permissive) | Section 7 |
| R9 | Signed zone **will** contain RRSIG, DNSKEY, DS, NSEC records. | (descriptive) | Section 8 |
| R10 | Signed zone **requires** regular maintenance for current RRSIG RRs. | (shall implied) | Section 8.2 |
| R11 | Re-signing any RRset **must** increment SOA serial and re-sign SOA. | must | Section 8.2 |
| R12 | Security-aware name server **should** include DNSSEC records in responses with DO bit. | should | Section 9 |
| R13 | Security-aware name server **must** support EDNS "sender's UDP payload". | must | Section 9 |
| R14 | Private keys **should** be kept offline; online for dynamic update zones. | should/must | Section 9 |
| R15 | Zone transfers **shall** use TSIG, SIG(0), or IPsec. | shall | Section 9 |

## Informative Annexes (Condensed)
- **(Section 13 Acknowledgements)**: The document acknowledges contributions from the DNS Extensions Working Group over a decade, listing many individuals.
- **(Informative References)**: Lists related RFCs (e.g., [RFC2136], [RFC2181], [RFC2308], [RFC2538], [RFC2845], [RFC2931], [RFC3007], etc.) that provide background but are not normative for the core DNSSEC specification.