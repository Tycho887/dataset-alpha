# RFC 1918: Address Allocation for Private Internets
**Source**: IETF (Internet Engineering Task Force) | **Version**: Best Current Practice (BCP 5) | **Date**: February 1996 | **Type**: Normative (Best Current Practice)
**Original**: https://datatracker.ietf.org/doc/html/rfc1918

## Scope (Summary)
Defines address allocation for private internets, reserving three IP address blocks (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) for use within enterprises not requiring direct Internet connectivity. Specifies operational constraints to prevent leakage of private addresses onto the public Internet.

## Normative References
- [RFC1466] Gerich, E., "Guidelines for Management of IP Address Space", May 1993.
- [RFC1518] Rekhter, Y. and T. Li, "An Architecture for IP Address Allocation with CIDR", September 1993.
- [RFC1519] Fuller, V., Li, T., Yu, J., and K. Varadhan, "Classless Inter-Domain Routing (CIDR): an Address Assignment and Aggregation Strategy", September 1993.

## Definitions and Abbreviations
- **Enterprise**: An entity autonomously operating a network using TCP/IP, determining its own addressing plan and address assignments.
- **Private hosts**: Hosts that do not require network layer access outside the enterprise (Category 1 and 2). They may use IP addresses unambiguous within the enterprise but ambiguous between enterprises.
- **Public hosts**: Hosts that need network layer access outside the enterprise (Category 3); require globally unambiguous IP addresses.
- **Private address space**: IP address ranges reserved by IANA for private internets: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.
- **24-bit block**: 10.0.0.0/8 (pre-CIDR class A).
- **20-bit block**: 172.16.0.0/12 (16 contiguous class B networks).
- **16-bit block**: 192.168.0.0/16 (256 contiguous class C networks).

## 1. Introduction (Summary)
The allocation permits full network layer connectivity among all hosts inside an enterprise and among public hosts of different enterprises. Cost: potential renumbering between public and private.

## 2. Motivation (Condensed)
Due to IPv4 address exhaustion and routing table growth, globally unique address space is increasingly scarce. Enterprises may partition hosts into three categories:
- **Category 1**: no external access.
- **Category 2**: limited external access via mediating gateways (e.g., application layer gateways).
- **Category 3**: need full external IP connectivity (require globally unique addresses).

Private hosts (categories 1 and 2) can use non-unique addresses. Examples include airport displays, bank internal workstations, internal networks behind gateways, router interfaces.

## 3. Private Address Space (Normative)

### Reserved Blocks
- **10.0.0.0/8**: 10.0.0.0 – 10.255.255.255 (24-bit block)
- **172.16.0.0/12**: 172.16.0.0 – 172.31.255.255 (20-bit block)
- **192.168.0.0/16**: 192.168.0.0 – 192.168.255.255 (16-bit block)

### Usage Rules
- **R1**: An enterprise may use addresses from these blocks without coordination with IANA or an Internet registry.
- **R2**: Any enterprise that needs globally unique address space must obtain such addresses from an Internet registry.
- **R3**: An enterprise that requests IP addresses for its external connectivity will never be assigned addresses from these blocks.
- **R4**: Private hosts cannot have IP connectivity to any host outside of the enterprise; they may access external services via mediating gateways (e.g., application layer gateways).
- **R5**: Routing information about private networks shall not be propagated on inter-enterprise links.
- **R6**: Packets with private source or destination addresses should not be forwarded across such links.
- **R7**: Routers in networks not using private address space, especially those of Internet service providers, are expected to be configured to reject (filter out) routing information about private networks. If such a router receives such information, the rejection shall not be treated as a routing protocol error.
- **R8**: Indirect references to private addresses (e.g., DNS Resource Records) should be contained within the enterprise. Internet service providers should take measures to prevent such leakage.

## 4. Advantages and Disadvantages (Informative Summary)
**Advantages**: Conserves globally unique address space; gives enterprises more flexibility and address space for internal design; avoids address clashes when later connecting to the Internet.  
**Disadvantages**: May require renumbering when connecting to the Internet or merging private internets. Renumbering cost can be mitigated by tools like DHCP [see PIER Working Group].

## 5. Operational Considerations (Normative Guidance)
- **R9**: It is strongly recommended that routers connecting enterprises to external networks be set up with appropriate packet and routing filters at both ends of the link to prevent leakage.
- **R10**: An enterprise should filter any private networks from inbound routing information to protect itself from ambiguous routing.
- **R11**: To minimize risk when two organizations using private addresses later wish to establish IP connectivity, it is strongly recommended that an organization using private IP addresses choose randomly from the reserved pool of private addresses when allocating sub-blocks.
- **R12**: If an enterprise uses private address space, DNS clients outside the enterprise should not see private addresses. One method: run two authority servers – one public (filtered) and one private (full data).

Additional guidance:
- Use the 24-bit block (10.0.0.0/8) if subnetting scheme permits; otherwise use 16-bit or 20-bit blocks.
- Avoid mixing public and private addresses on the same physical medium without careful design.

## 6. Security Considerations
Security issues are not addressed in this memo.

## 7. Conclusion (Informative)
Large enterprises need only a small block of globally unique addresses; the Internet benefits through conservation, enterprises benefit from flexibility. Renumbering may be required as connectivity needs change.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | An enterprise may use private address blocks without coordination with IANA or registry. | may | Section 3 |
| R2 | Enterprise needing globally unique addresses must obtain from Internet registry. | must | Section 3 |
| R3 | Enterprise requesting addresses for external connectivity will never be assigned private blocks. | will not | Section 3 |
| R4 | Private hosts cannot have IP connectivity outside enterprise; may use mediating gateways. | cannot | Section 3 |
| R5 | Routing information about private networks shall not be propagated on inter-enterprise links. | shall not | Section 3 |
| R6 | Packets with private addresses should not be forwarded across inter-enterprise links. | should not | Section 3 |
| R7 | Routers (especially ISPs) are expected to reject routing info about private networks; rejection shall not be treated as protocol error. | shall / expected | Section 3 |
| R8 | Indirect references to private addresses should be contained within enterprise; ISPs should prevent leakage. | should | Section 3 |
| R9 | It is strongly recommended to set up packet and routing filters at border routers to prevent leakage. | strongly recommended | Section 5 |
| R10 | Enterprises should filter inbound routing info for private networks to avoid ambiguity. | should | Section 5 |
| R11 | Organizations using private addresses should choose randomly from reserved pool to minimize conflict when cooperating. | strongly recommended | Section 5 |
| R12 | DNS clients outside enterprise should not see private addresses; use split DNS. | should | Section 5 |

## Informative Annexes (Condensed)
No formal annexes. Informative sections 4, 5, and 7 are summarized above. Section 5 also provides practical design recommendations (e.g., separate subnets for public/private hosts, use of 24-bit block for growth).