# RFC 7157: IPv6 Multihoming without Network Address Translation
**Source**: IETF | **Version**: Informational | **Date**: March 2014 | **Type**: Informational  
**Original**: http://www.rfc-editor.org/info/rfc7157

## Scope (Summary)
This document analyzes use cases of IPv6 multihoming for hosts and small networks that do not meet minimum IPv6 allocation criteria, describes functional requirements, and identifies problems with source address selection, next-hop selection, and DNS recursive name server selection. It concludes that DHCPv6-based solutions are suitable to solve multihoming issues, but NPTv6 may be required as an intermediate solution.

## Normative References
- [RFC4191] Draves, R. and D. Thaler, "Default Router Preferences and More-Specific Routes", RFC 4191, November 2005.
- [RFC4861] Narten, T., et al., "Neighbor Discovery for IP version 6 (IPv6)", RFC 4861, September 2007.
- [RFC6296] Wasserman, M. and F. Baker, "IPv6-to-IPv6 Network Prefix Translation", RFC 6296, June 2011.
- [RFC6724] Thaler, D., et al., "Default Address Selection for Internet Protocol Version 6 (IPv6)", RFC 6724, September 2012.
- [RFC6731] Savolainen, T., et al., "Improved Recursive DNS Server Selection for Multi-Interfaced Nodes", RFC 6731, December 2012.
- [RFC7078] Matsumoto, A., et al., "Distributing Address Selection Policy Using DHCPv6", RFC 7078, January 2014.

## Definitions and Abbreviations
- **NPTv6**: IPv6-to-IPv6 Network Prefix Translation as described in [RFC6296].
- **NAPT**: Network Address Port Translation as described in [RFC3022]. (Often pronounced "NAT" or written as "NAT".)
- **MHMP**: Multihomed with multi-prefix. A host implementation supporting source address selection policy, next hop selection, and DNS selection policy as described in this document.
- **Split-horizon DNS**: DNS configuration where responses differ based on source address; acknowledged but not condoned.

## 1. Introduction
- **Problem**: IPv6 provides globally unique addresses, but multihoming in IPv6 may require NAT (NPTv6) due to multiple upstream networks assigning different prefixes. IPv4 uses NAPT for multihoming; IPv6 should avoid NAT to preserve end-to-end transparency.
- **Goals**: Avoid NPTv6 as long-term solution; refine IPv6 specifications to resolve multihoming problems. Issues include source address selection, next-hop selection, and DNS resolution when multiple routers or prefixes exist.

## 2. Terminology
- (See Definitions above)

## 3. IPv6 Multihomed Network Scenarios
### 3.1 Classification of Network Scenarios for Multihomed Host
- **Scenario 1**: Two or more routers on a single link, each connecting to different service provider networks. Host receives multiple prefixes and DNS servers. (Figure 1)
- **Scenario 2**: Single gateway router connects to two or more upstream providers. Host sees one default router but multiple prefixes. (Figure 2)
- **Scenario 3**: Host has multiple active interfaces, each connected to a different router/provider. (Figure 3)

### 3.2 Multihomed Network Environment
- In IPv4, gateway router with NAPT solves multihoming. In IPv6, host may incorrectly resolve next-hop, source address, or DNS server, leading to connectivity impairment.

### 3.3 Problem Statement
- **All scenarios**: Host may use wrong source address (discarded by ingress filtering), wrong default router (traffic dropped), or wrong DNS server (incorrect responses).
- **Scenario 1**: Source address selection non-deterministic; host selects one default router only.
- **Scenario 2**: Source address selection non-deterministic; gateway router may not know which network to send traffic.
- **Scenario 3**: Host lacks information to direct traffic; selects one default router.

## 4. Requirements
### 4.1 End-to-End Transparency
- The IPv6 multihoming solution **should strive to avoid NPTv6** to achieve end-to-end transparency. NAT traversal mechanisms (e.g., ICE) should not be mandatory.

### 4.2 Scalability
- The solution **must** be able to manage a large number of sites/nodes (e.g., residential services with thousands of sites). Periodic signaling to each site may affect edge system performance.

## 5. Problem Analysis
### 5.1 Source Address Selection
- Current [RFC6724] rules may not deterministically select correct source address. [RFC7078] proposes DHCPv6-based policy table distribution.
- **Requirement**: Host must support solution for Scenarios 1 and 2; Scenario 3 may rely on next-hop solution. **Network's DHCP server and DHCP-forwarding routers must also support Address Selection option [RFC7078].**

### 5.2 Next Hop Selection
- Host or gateway may select wrong default router. [RFC4191] provides link-specific preferences but not per-host configuration. DHCPv6-based route distribution is preferred over routing protocols.
- **Requirement**: Host must support solution for Scenarios 1 and 3; GW router for Scenario 2.

### 5.3 DNS Recursive Name Server Selection
- Querying wrong DNS server may fail for private namespaces (split-horizon). [RFC6731] proposes DHCPv6 option for domain-specific DNS server selection.
- **Requirement**: Host must support solution for all scenarios; GW router for Scenario 2. **Network's DHCP server and DHCP-forwarding routers must also support [RFC6731].**

## 6. Implementation Approach
### 6.1 Source Address Selection
- Proactive approaches (policy table distribution via DHCPv6 [RFC7078]) are appropriate. Advantage: network administrator's policy directly propagated.

### 6.2 Next Hop Selection
- Policy propagation (routing information or source-prefix/next-hop pairs) via DHCPv6 or RA extensions. DHCPv6 has advantage of relay functionality and common use.

### 6.3 DNS Recursive Name Server Selection
- Policy-based approach [RFC6731] conveys pairs of DNS server addresses and domain suffixes via DHCP option. Home gateway can act as DNS cache and distribute queries accordingly.

### 6.4 Other Algorithms Available in RFCs
- Shim6 [RFC5533] and HIP [RFC5206] are noted but operational experience is insufficient for recommendation.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The IPv6 multihoming solution should strive to avoid NPTv6 to achieve end-to-end transparency. | should | Section 4.1 |
| R2 | The solution must be able to manage a large number of sites/nodes; periodic signaling may affect performance. | must | Section 4.2 |
| R3 | Host must support source address selection solution for Scenarios 1 and 2. | must | Section 5.1 |
| R4 | Network's DHCP server and DHCP-forwarding routers must support Address Selection option [RFC7078]. | must | Section 5.1 |
| R5 | Host must support next-hop selection solution for Scenarios 1 and 3; GW router for Scenario 2. | must | Section 5.2 |
| R6 | Host must support DNS recursive name server selection solution for all scenarios; GW router for Scenario 2. | must | Section 5.3 |
| R7 | Network's DHCP server and DHCP-forwarding routers must support [RFC6731] for DNS server selection. | must | Section 5.3 |

## Informative Annexes (Condensed)
- **Section 7: Considerations for MHMP Deployment**: Describes handling of non-MHMP hosts (NPTv6 as last resort), coexistence (identifying hosts and assigning single or multiple prefixes), and policy collision (prioritization rules needed; future work required).
- **Section 8: Security Considerations**: Identifies threats on policy receiver and distributor sides. Unauthorized policy may lead to session hijack, DoS, privacy leaks. Mitigations include ingress filtering, DNSSEC, secure channels, and limiting DHCP usage to local links.
- **Section 9: Contributors**: List of contributors and acknowledgments.