# RFC 3682: The Generalized TTL Security Mechanism (GTSM)
**Source**: IETF, Network Working Group | **Version**: Experimental | **Date**: February 2004 | **Type**: Experimental
**Original**: https://datatracker.ietf.org/doc/rfc3682/

## Scope
GTSM protects router TCP/IP control planes from CPU-utilization-based attacks using the packet's TTL (IPv4) or Hop Limit (IPv6). It is most effective for directly connected peers but can provide limited protection for multi-hop sessions. GTSM is not directly applicable to protocols employing flooding mechanisms.

## Normative References
- [RFC791] Postel, J., "Internet Protocol Specification", STD 5, RFC 791, September 1981.
- [RFC1771] Rekhter, Y. and T. Li (Editors), "A Border Gateway Protocol (BGP-4)", RFC 1771, March 1995.
- [RFC1772] Rekhter, Y. and P. Gross, "Application of the Border Gateway Protocol in the Internet", RFC 1772, March 1995.
- [RFC2003] Perkins, C., "IP Encapsulation with IP", RFC 2003, October 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2385] Heffernan, A., "Protection of BGP Sessions via the TCP MD5 Signature Option", RFC 2385, August 1998.
- [RFC2461] Narten, T., Nordmark, E. and W. Simpson, "Neighbor Discovery for IP Version 6 (IPv6)", RFC 2461, December 1998.
- [RFC2784] Farinacci, D., "Generic Routing Encapsulation (GRE)", RFC 2784, March 2000.
- [RFC2842] Chandra, R. and J. Scudder, "Capabilities Advertisement with BGP-4", RFC 2842, May 2000.
- [RFC2893] Gilligan, R. and E. Nordmark, "Transition Mechanisms for IPv6 Hosts and Routers", RFC 2893, August 2000.
- [RFC3032] Rosen, E., Tappan, D., Fedorkow, G., Rekhter, Y., Farinacci, D., Li, T. and A. Conta, "MPLS Label Stack Encoding", RFC 3032, January 2001.
- [RFC3036] Andersson, L., Doolan, P., Feldman, N., Fredette, A. and B. Thomas, "LDP Specification", RFC 3036, January 2001.
- [RFC3392] Chandra, R. and J. Scudder, "Capabilities Advertisement with BGP-4", RFC 3392, November 2002.

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119.

## Definitions and Abbreviations
- **GTSM**: Generalized TTL Security Mechanism.
- **TTL**: Time to Live (IPv4) or Hop Limit (IPv6); used interchangeably in this document.
- **RP**: Route Processor.
- **ACL**: Access Control List (receive path ACL designed to control which packets are allowed to the RP).
- **DoS**: Denial of Service.

## 1. Introduction (Summary)
GTSM is designed to protect a router’s TCP/IP-based control plane from CPU-utilization-based attacks. It is based on the fact that the vast majority of protocol peerings are between adjacent routers, and that TTL spoofing is nearly impossible. The mechanism applies equally to IPv4 TTL and IPv6 Hop Limit.

## 2. Assumptions Underlying GTSM
- **(i)** The vast majority of protocol peerings are between adjacent routers.
- **(ii)** Many providers ingress filter packets with their own loopback addresses as source.
- **(iii)** Use of GTSM is **OPTIONAL** and can be configured on a per-peer (group) basis.
- **(iv)** The router supports classifying traffic into interesting/control and not-control queues.
- **(v)** Both peer routers implement GTSM.

### 2.1. GTSM Negotiation
- GTSM **MUST** be manually configured between protocol peers. No automatic capability negotiation is assumed or defined.

### 2.2. Assumptions on Attack Sophistication
- Attackers can send valid-looking control traffic (source/destination of configured peers). Each router in the path decrements TTL properly. GTSM sets outbound TTL to 255 and rejects packets from configured peers that do not have an inbound TTL of 255. GTSM can be disabled for route-servers and other multi-hop peerings.

## 3. GTSM Procedure
- **GTSM SHOULD NOT be enabled by default.**
- **(i)** If GTSM is enabled:
  - **(a)** For directly connected routers:
    - **Set the outbound TTL for the protocol connection to 255.**
    - **Update the receive path ACL to only allow protocol packets with the correct `<source, destination, TTL>` tuple.** The TTL must be either 255 (directly connected) or *255 - (configured-range-of-acceptable-hops)* (multi-hop). **Any directly connected check MUST be disabled for such peerings.**
  - **(b)** If the inbound TTL is not as expected (directly connected or multi-hop range), the packet **MUST NOT be processed**. It is placed into a low priority queue, logged, and/or silently discarded. **An ICMP message MUST NOT be generated.**
- **(ii)** If GTSM is not enabled, normal protocol behavior is followed.

### 3.1. Multi-hop Scenarios
- The expected TTL value is set to *255 - (configured-range-of-acceptable-hops)*. This provides a qualitatively lower degree of security. An implementation **MAY** provide **OPTIONAL** support for multi-hop GTSM.

#### 3.1.1. Intra-domain Protocol Handling
- In general, GTSM is not used for intra-domain protocol peers or adjacencies. iBGP peers can be protected by filtering at the network edge for packets with source addresses of loopbacks used for intra-domain peering. Current best practice is to further protect such peers with an MD5 signature [RFC2385].

## 4. Security Considerations (Condensed)
- **TTL Spoofing**: A TTL of 255 is non-trivial to spoof from non-directly connected locations, assuming no routers in the path are compromised and tunnels are not used.
- **Tunneled Packets**: Tunneling (IP-in-IP, GRE, IPv6-in-IPv4, MPLS) can allow spoofing of the TTL or make it impossible to achieve a TTL of 255 at the peer. Specific handling:
  - IP-in-IP: The inner header TTL can be set arbitrarily; RFC 2003 specifies that when encapsulating, inner TTL is decremented by one if forwarding, else unchanged. So a TTL of 255 may be delivered to the decapsulator.
  - MPLS: When labels are used, the TTL may be decremented by at least one (e.g., PHP), resulting in a maximum egress TTL of 254, causing the GTSM check to fail.
- **Multi-Hop Sessions**: GTSM is less effective for multi-hop sessions and is an OPTIONAL extension in such cases. Cryptographic protection (e.g., S-BGP) may be required.

## 5. IANA Considerations
This document creates no new requirements on IANA namespaces.

## Requirements Summary

| ID  | Requirement | Type | Reference |
|-----|-------------|------|-----------|
| R1  | GTSM SHOULD NOT be enabled by default. | SHOULD NOT | Section 3 |
| R2  | If GTSM is enabled, set outbound TTL for protocol connection to 255. | SHALL (implied) | Section 3(i)(a) |
| R3  | Update receive path ACL to only allow packets with correct `<source, destination, TTL>` tuple. TTL must be 255 or 255-(configured-range). | MUST | Section 3(i)(a) |
| R4  | Directly connected check MUST be disabled for multi-hop peerings. | MUST | Section 3(i)(a) |
| R5  | If inbound TTL is not as expected, packet is NOT processed; placed in low priority queue, logged/discarded. An ICMP message MUST NOT be generated. | MUST NOT | Section 3(i)(b) |
| R6  | GTSM MUST be manually configured; no automatic negotiation. | MUST | Section 2.1 |
| R7  | GTSM is OPTIONAL and can be configured on a per-peer (group) basis. | OPTIONAL | Section 2(iii) |
| R8  | Multi-hop GTSM is OPTIONAL; expected TTL = 255-(configured-range). Implementation MAY provide OPTIONAL support. | MAY/OPTIONAL | Section 3.1, 5.3 |

## Informative Annexes (Condensed)
- **Acknowledgments**: The use of TTL to protect BGP originated with Paul Traina, Jon Stewart, Ryan McDowell, and others. Feedback from Steve Bellovin, Jay Borkenhagen, Randy Bush, Vern Paxson, Pekka Savola, Robert Raszuk, and David Ward.
- **Authors' Addresses**: Vijay Gill (vijay@umbc.edu), John Heasley (heas@shrubbery.net), David Meyer (dmm@1-4-5.net).
- **Full Copyright Statement**: Copyright (C) The Internet Society (2004). Reproduction and distribution permitted under standard IETF rules.