# RFC 3513: Internet Protocol Version 6 (IPv6) Addressing Architecture
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: April 2003 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3513

## Scope (Summary)
This specification defines the addressing architecture of IPv6, including the addressing model, text representations of addresses, definitions of unicast, anycast, and multicast addresses, and the required addresses for IPv6 nodes.

## Normative References
- [IPV6] Deering, S. and R. Hinden, "Internet Protocol, Version 6 (IPv6) Specification", RFC 2460, December 1998.
- [RFC2026] Bradner, S., "The Internet Standards Process -- Revision 3", BCP 9, RFC 2026, October 1996.

## Definitions and Abbreviations
- **Unicast**: An identifier for a single interface. A packet sent to a unicast address is delivered to the interface identified by that address.
- **Anycast**: An identifier for a set of interfaces (typically on different nodes). A packet sent to an anycast address is delivered to one of the interfaces (the "nearest" according to routing protocol distance).
- **Multicast**: An identifier for a set of interfaces. A packet sent to a multicast address is delivered to all interfaces identified by that address.
- **Interface ID**: The lower portion of a unicast address used to identify an interface on a link.
- **Subnet prefix**: The leftmost contiguous bits of an address that comprise the prefix.
- **Modified EUI-64 format**: Interface identifier format derived from IEEE EUI-64 by inverting the universal/local bit.

## 1. Introduction
This specification defines the IPv6 addressing architecture, including basic formats for unicast, anycast, and multicast addresses. (Informative: Acknowledges contributors.)

## 2. IPv6 Addressing
IPv6 addresses are 128-bit identifiers for interfaces or sets of interfaces. Three types: unicast, anycast, multicast. No broadcast addresses in IPv6.

- **Unicast**: single interface.
- **Anycast**: set of interfaces; delivered to nearest one.
- **Multicast**: set of interfaces; delivered to all.
- All zeros and all ones are legal values unless specifically excluded.

### 2.1 Addressing Model
- IPv6 addresses are assigned to interfaces, not nodes.
- All interfaces **must** have at least one link-local unicast address.
- A single interface may have multiple IPv6 addresses of any type or scope.
- Exception: A unicast address or set of unicast addresses may be assigned to multiple physical interfaces if the implementation treats them as one interface (e.g., for load-sharing).
- A subnet prefix is associated with one link; multiple subnet prefixes may be assigned to the same link.

### 2.2 Text Representation of Addresses
Three conventional forms:
1. Preferred: `x:x:x:x:x:x:x:x` (hexadecimal 16-bit pieces). Leading zeros may be omitted, but at least one numeral per field.
2. Compressed zeros: `::` indicates one or more groups of 16 zero bits. Can appear only once. Can compress leading or trailing zeros.
3. Mixed IPv4/IPv6: `x:x:x:x:x:x:d.d.d.d` where `d` are decimal IPv4 octets.

Examples provided in text.

### 2.3 Text Representation of Address Prefixes
Notation: `ipv6-address/prefix-length` where `prefix-length` is decimal number of leftmost contiguous bits.
- Examples of legal and illegal representations given.
- When combining node address and subnet prefix: `node-address/prefix-length`.

### 2.4 Address Type Identification
Type identified by high-order bits:

| Address type         | Binary prefix        | IPv6 notation | Section |
|----------------------|----------------------|---------------|---------|
| Unspecified          | 00...0 (128 bits)    | ::/128        | 2.5.2   |
| Loopback             | 00...1 (128 bits)    | ::1/128       | 2.5.3   |
| Multicast            | 11111111             | FF00::/8      | 2.7     |
| Link-local unicast   | 1111111010           | FE80::/10     | 2.5.6   |
| Site-local unicast   | 1111111011           | FEC0::/10     | 2.5.6   |
| Global unicast       | everything else      | --            | 2.5.4   |

- Anycast addresses are not syntactically distinguishable from unicast.
- Implementations **must** treat all addresses not starting with the above prefixes as global unicast, unless future specification redefines subranges.

### 2.5 Unicast Addresses
IPv6 unicast addresses are aggregable with arbitrary prefix length. Types: global, site-local, link-local, special-purpose (e.g., embedded IPv4, NSAP). Nodes may see addresses as flat or structured (subnet prefix + interface ID). Routers may have knowledge of hierarchical boundaries.

#### 2.5.1 Interface Identifiers
- Used to identify interfaces on a link. **Required** to be unique within a subnet prefix.
- **Recommended** not to assign the same interface identifier to different nodes on a link.
- For all unicast addresses except those starting with binary 000, Interface IDs **must** be 64 bits and constructed in Modified EUI-64 format.
- Modified EUI-64 format: invert the "u" (universal/local) bit. u=1 indicates global scope, u=0 indicates local scope.
- Details of forming interface identifiers are defined in specific "IPv6 over <link>" specifications.
- The use of the universal/local bit allows future technology development for globally-scoped identifiers.

#### 2.5.2 The Unspecified Address
- Address `::` (128 zeros). **Must never** be assigned to any node. Indicates absence of an address.
- **Must not** be used as destination address or in Routing Headers.
- **Must never** be forwarded by an IPv6 router as source address.

#### 2.5.3 The Loopback Address
- Address `::1`. Used by a node to send a packet to itself. **May never** be assigned to any physical interface.
- Has link-local scope. Treated as unicast address of a virtual loopback interface.
- **Must not** be used as source address for packets sent outside a single node.
- **Must never** be sent outside a single node as destination; **must never** be forwarded by a router; **must** be dropped if received on an interface.

#### 2.5.4 Global Unicast Addresses
General format: `global routing prefix | subnet ID | interface ID`. The global routing prefix is assigned to a site; subnet ID identifies a link.
- For addresses not starting with binary 000, interface ID **must** be 64 bits (n+m=64).
- Global unicast addresses starting with binary 000 have no constraint on interface ID size or structure (e.g., embedded IPv4, NSAP).

#### 2.5.5 IPv6 Addresses with Embedded IPv4 Addresses
- **IPv4-compatible IPv6 address**: 80 bits of zeros, 16 bits of zeros, 32-bit IPv4 address. The IPv4 address **must** be globally-unique unicast.
- **IPv4-mapped IPv6 address**: 80 bits of zeros, 16 bits of ones (FFFF), 32-bit IPv4 address.

#### 2.5.6 Local-Use IPv6 Unicast Addresses
Two types:
- **Link-Local**: prefix `1111111010` + 54 zero bits + 64-bit interface ID. Designed for single-link use (autoconfiguration, neighbor discovery). **Routers must not** forward packets with link-local source or destination to other links.
- **Site-Local**: prefix `1111111011` + 54-bit subnet ID + 64-bit interface ID. Designed for intra-site use without global prefix. **Routers must not** forward packets with site-local source or destination outside the site.

### 2.6 Anycast Addresses
- Assigned to more than one interface. Packet delivered to the "nearest" interface according to routing distance.
- Allocated from unicast address space; syntactically indistinguishable. Nodes assigned anycast address **must be explicitly configured** to know it is anycast.
- For any anycast address, there is a longest prefix P identifying the topological region containing all interfaces. Within region P, the anycast address **must** be maintained as a separate routing entry (host route). Outside region P, it may be aggregated.
- If P is null (no topological locality), the anycast address **must** be maintained as separate entry throughout the entire internet (severe scaling limit).
- Expected uses: identifying routers of a service provider, routers on a subnet, or entry into a routing domain.
- Restrictions:
  - **An anycast address must not be used as the source address of an IPv6 packet.**
  - **An anycast address must not be assigned to an IPv6 host; it may be assigned to an IPv6 router only.**

#### 2.6.1 Required Anycast Address
- **Subnet-Router anycast address**: `subnet prefix | 0` (all zeros in interface ID field). Syntactically same as unicast address with interface ID zero.
- Packets sent to this address are delivered to one router on the subnet.
- All routers **must** support Subnet-Router anycast addresses for subnets to which they have interfaces.

### 2.7 Multicast Addresses
Format: `11111111 | flgs (4 bits) | scop (4 bits) | group ID (112 bits)`.
- **flgs**: high-order 3 bits reserved, **must** be 0. T bit: 0 = permanently-assigned (IANA), 1 = transient.
- **scop** (4-bit scope values):
  - 0: reserved
  - 1: interface-local
  - 2: link-local
  - 3: reserved
  - 4: admin-local
  - 5: site-local
  - 6-9: (unassigned)
  - A-D: (unassigned)
  - E: global scope
  - F: reserved
- **group ID**: identifies the multicast group within the scope.
- Permanent multicast addresses have meaning independent of scope. Transient addresses are significant only within the given scope.
- **Multicast addresses must not be used as source addresses in IPv6 packets or appear in any Routing header.**
- **Routers must not forward any multicast packets beyond the scope indicated by the scop field.**
- **Nodes must not originate a packet to a multicast address with scop = 0; if received, must be silently dropped.**
- Nodes **should not** originate packets with scop = F; if sent or received, treat as global scope (E).

#### 2.7.1 Pre-Defined Multicast Addresses
- Reserved multicast addresses: `FF00::` through `FF0F::` (group ID 0). **Shall never** be assigned to any multicast group.
- All Nodes Addresses: `FF01::1` (interface-local), `FF02::1` (link-local).
- All Routers Addresses: `FF01::2`, `FF02::2` (interface-local and link-local), `FF05::2` (site-local).
- Solicited-Node Address: formed by taking low-order 24 bits of a unicast or anycast address and appending to prefix `FF02:0:0:0:0:1:FF00::/104`. Range: `FF02:0:0:0:0:1:FF00:0000` to `FF02:0:0:0:0:1:FFFF:FFFF`. A node **must** compute and join the associated solicited-node multicast address for every unicast and anycast address it is assigned.

### 2.8 A Node's Required Addresses
A host **must** recognize:
- Its required Link-Local Address for each interface.
- Any additional configured Unicast and Anycast Addresses.
- The loopback address.
- The All-Nodes Multicast Addresses (section 2.7.1).
- The Solicited-Node Multicast Address for each its unicast and anycast addresses.
- Multicast addresses of other groups it belongs to.

A router **must**, in addition to the above, recognize:
- The Subnet-Router Anycast Addresses for all interfaces it acts as a router.
- All other Anycast Addresses with which it is configured.
- The All-Routers Multicast Addresses (section 2.7.1).

## 3. Security Considerations
IPv6 addressing does not have direct impact on infrastructure security. Authentication is defined in [AUTH] (informative reference).

## 4. IANA Considerations
(Informative: The initial IPv6 address space allocation table and notes are provided, including reserved ranges, NSAP, global unicast (prefix 001), link-local, site-local, multicast. IANA should limit allocation to addresses starting with binary 001; rest (~85%) is reserved.)

## Requirements Summary
| ID  | Requirement                                                                                                 | Type   | Reference          |
|-----|-------------------------------------------------------------------------------------------------------------|--------|--------------------|
| R1  | All interfaces must have at least one link-local unicast address.                                           | must   | Section 2.1        |
| R2  | Interface IDs must be unique within a subnet prefix.                                                        | must   | Section 2.5.1      |
| R3  | For unicast addresses not starting with binary 000, Interface IDs must be 64 bits and in Modified EUI-64 format. | must   | Section 2.5.1      |
| R4  | The unspecified address must never be assigned to any node.                                                 | must   | Section 2.5.2      |
| R5  | The unspecified address must not be used as destination or in Routing Headers.                              | must   | Section 2.5.2      |
| R6  | An IPv6 packet with source address unspecified must never be forwarded by a router.                         | must   | Section 2.5.2      |
| R7  | The loopback address must never be assigned to any physical interface.                                      | must   | Section 2.5.3      |
| R8  | The loopback address must not be used as source for packets sent outside a single node.                     | must   | Section 2.5.3      |
| R9  | A packet with destination loopback must never be sent outside a single node and must never be forwarded.    | must   | Section 2.5.3      |
| R10 | Routers must not forward packets with link-local source or destination addresses to other links.            | must   | Section 2.5.6      |
| R11 | Routers must not forward packets with site-local source or destination addresses outside the site.          | must   | Section 2.5.6      |
| R12 | Anycast addresses must not be used as source addresses.                                                     | must   | Section 2.6        |
| R13 | Anycast addresses must not be assigned to an IPv6 host; only routers.                                       | must   | Section 2.6        |
| R14 | All routers must support Subnet-Router anycast addresses for their subnets.                                 | must   | Section 2.6.1      |
| R15 | Multicast addresses must not be used as source addresses or appear in Routing headers.                      | must   | Section 2.7        |
| R16 | Routers must not forward multicast packets beyond the scope indicated.                                      | must   | Section 2.7        |
| R17 | Nodes must not originate packets with scop=0; if received, must be silently dropped.                        | must   | Section 2.7        |
| R18 | A node must compute and join the solicited-node multicast address for each unicast/anycast address.         | must   | Section 2.7.1      |
| R19 | A host must recognize its link-local, other configured addresses, loopback, All-Nodes, solicited-node, and group multicast addresses. | must   | Section 2.8        |
| R20 | A router must additionally recognize subnet-router anycast, any other anycast, and All-Routers multicast addresses. | must   | Section 2.8        |

## Informative Annexes (Condensed)
- **Appendix A: Creating Modified EUI-64 format Interface IDs**: Provides methods for forming interface identifiers from IEEE EUI-64 (invert u-bit), IEEE 48-bit MAC (insert 0xFF and 0xFE), other link identifiers (zero-fill left), and links without identifiers (use global ID from another interface or create local-scope unique ID). Strongly recommends collision detection.
- **Appendix B: Changes from RFC 2373**: Lists clarifications, format changes (site-local subnet ID lengthened to 54 bits), removal of some sections, addition of IANA section, corrected references, and minor text clarifications.