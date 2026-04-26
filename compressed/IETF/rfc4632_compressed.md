# RFC 4632: Classless Inter-domain Routing (CIDR): The Internet Address Assignment and Aggregation Plan
**Source**: IETF - BCP 122 | **Version**: Original (obsoletes RFC 1519) | **Date**: August 2006 | **Type**: Best Current Practice
**Original**: https://datatracker.ietf.org/doc/html/rfc4632

## Scope (Summary)
This document specifies the strategy for assigning 32-bit IPv4 address blocks using classless prefixes (CIDR) to conserve address space and limit the growth of global routing state. It obsoletes RFC 1519 and updates the community on deployment experience over twelve years.

## Normative References
- [RFC791] Postel, J., "Internet Protocol", STD 5, RFC 791, September 1981.

## Definitions and Abbreviations
- **CIDR**: Classless Inter-domain Routing – a method for allocating and routing IPv4 addresses without regard to the classful A/B/C boundaries.
- **Prefix**: A block of IPv4 addresses expressed as an address followed by a slash and a prefix length (e.g., 192.168.0.0/16). The prefix length indicates the number of significant bits in the network portion.
- **Classless**: Refers to the ability to use any prefix length (0–32) instead of being limited to /8, /16, or /24 legacy classes.
- **Longest-match**: Forwarding rule where the most specific (longest) prefix is used when multiple routes match a destination.
- **Aggregate**: A single route that covers a block of addresses, combining multiple more-specific routes.
- **More-specific**: A route with a longer prefix length that falls within an aggregate.
- **IANA**: Internet Assigned Numbers Authority.
- **RIR**: Regional Internet Registry (e.g., RIPE NCC, ARIN, APNIC).
- **ISP/LIR**: Internet Service Provider / Local Internet Registry.

## 1. Introduction (Condensed)
This memo discusses address assignment for the 32-bit IPv4 space to conserve addresses and limit routing table growth. It obsoletes [RFC1519] and updates the community on deployment results. As defined, the plan does not require renumbering of legacy Class C space ("the swamp") nor does it mandate renumbering when changing providers, though renumbering is encouraged.

## 2. History and Problem Description (Condensed)
The original 1980s classful addressing (Class A, B, C) assumed three network sizes. By the early 1990s, three problems emerged:
1. Exhaustion of Class B space.
2. Exponential growth of routing tables.
3. Eventual exhaustion of the 32-bit IPv4 address space.

The IETF ROAD group was formed, leading to [RFC1338] and later [RFC1519] (CIDR). CIDR provides a mechanism to slow routing table growth and address consumption but does not solve long-term address exhaustion.

## 3. Classless Addressing as a Solution
### 3.1 Basic Concept and Prefix Notation
A prefix is written as an IPv4 address followed by "/" and a decimal length (0-32). Examples:
- Legacy Class B 172.16.0.0 becomes 172.16.0.0/16.
- Legacy Class C 192.168.99.0 becomes 192.168.99.0/24.

The following table (non-normative) shows all prefix sizes:

| notation       | addrs/block | # blocks   | notes               |
|----------------|-------------|------------|---------------------|
| n.n.n.n/32     | 1           | 4294967296 | host route          |
| n.n.n.x/31     | 2           | 2147483648 | p2p link [RFC3021]  |
| n.n.n.x/30     | 4           | 1073741824 |                     |
| ...            | ...         | ...        |                     |
| n.n.n.0/24     | 256         | 16777216   | legacy Class C      |
| n.n.x.0/23     | 512         | 8388608    |                     |
| ...            | ...         | ...        |                     |
| n.n.0.0/16     | 65536       | 65536      | legacy Class B      |
| n.x.0.0/15     | 131072      | 32768      |                     |
| ...            | ...         | ...        |                     |
| n.0.0.0/8      | 16777216    | 256        | legacy Class A      |
| x.0.0.0/7      | 33554432    | 128        |                     |
| ...            | ...         | ...        |                     |
| 0.0.0.0/0      | 4294967296  | 1          | default route       |

**Note**: The terms *allocate* (delegation for further sub-delegation) and *assign* (direct use) have specific meanings in the registry system. This description is not intended as direction to IANA.

## 4. Address Assignment and Routing Aggregation
### 4.1 Aggregation Efficiency and Limitations
- Aggregation works best when an end site uses address space from its single provider; the provider advertises an aggregate covering the customer.
- **Multi-homing** reduces aggregation efficiency because the site must be explicitly advertised by each provider. The cost is similar to pre-CIDR.
- **Changing providers without renumbering** creates a "hole" in the old provider's aggregate. The new provider must advertise the more-specific prefix. It is *recommended* that the site eventually renumber into the new provider's space, using mechanisms such as DHCP ([RFC2131]).
- Some efficiency can be regained by allocating a contiguous power-of-two block to a multi-homed site, so it appears as a single prefix.
- Second-level aggregation may occur if multi-homed providers share a common upstream.

### 4.2 Distributed Assignment of Address Space
Originally centralized at the NIC, address assignment became hierarchical: IANA → RIRs → LIRs/ISPs → customers. This allowed aggregation along provider topologies. The delegation is bit-aligned (e.g., /8 blocks to RIRs). Routing information for multi-homed organizations must still be known by higher levels.

## 5. Routing Implementation Considerations
### 5.1 Rules for Route Advertisement
1. **Longest-match forwarding**: Destinations that are multi-homed relative to a routing domain *must* be explicitly announced (cannot be summarized).
2. **Aggregate discard**: A router generating an aggregate *must* discard packets matching the aggregate but not any more-specific route (next hop should be null destination). Prevents forwarding loops.

   Additionally:
   - The default route 0.0.0.0/0 *MUST* be accepted by all implementations.
   - This default *should only* be advertised when explicitly configured, never as a non-configured option.

### 5.2 How the Rules Work
Rule #1 ensures consistent forwarding: multi-homed networks are always explicitly advertised by each provider. Rule #2 prevents loops: if a child network loses connectivity to part of its aggregate, traffic from the parent must not be forwarded back via the less-specific route; a discard route is installed. The default route is a special case: a network must not follow the default for destinations matching its own aggregated advertisements.

### 5.3 A Note on Prefix Filter Formats
Route filters *must* support explicit prefix lengths or masks. Example filter using prefix notation:
```
accept 172.16.0.0/16
accept 172.25.0.0/16
accept 172.31.0.0/16
deny 10.2.0.0/16
accept 10.0.0.0/8
```
Implementations *must* allow matching a prefix and all more-specific prefixes with the same bit pattern.

### 5.4 Responsibility for and Configuration of Aggregation
- The AS holding a prefix has sole responsibility for aggregating those prefixes.
- Aggregation may be delegated to another AS (e.g., customer to provider), but proxy aggregation (without explicit agreement) is strongly discouraged because it can cause unintended traffic shifts.
- Configuration is typically a few lines defining the block to aggregate. Dynamic aggregate routes should be added when at least one component is reachable and withdrawn only when all components become unreachable, to avoid route flapping.

### 5.5 Route Propagation and Routing Protocol Considerations
Transit networks *must* use internal BGP (iBGP) to carry routes learned from other providers, both within and through their networks, to ensure proper path propagation and loop prevention.

## 6. Example of New Address Assignments and Routing (Condensed)
Section 6 provides a detailed example of provider PA allocating /21 to /23 blocks to customers, including multi-homed sites (C4, C5) and a re-homed site (C7). PA advertises: its aggregate (10.24.0.0/13), C4 (10.24.12.0/22), and C7 (10.32.0.0/20). PB advertises its aggregate (10.32.0.0/13) plus C4 secondary and C5 primary. The diagnosis of a C7 outage is discussed: traffic will be dropped by PB's less-specific aggregate.

## 7. Domain Name Service Considerations (Condensed)
Address-to-name translation (IN-ADDR.ARPA) was affected because it delegates on octet boundaries. Techniques for non-octet-aligned blocks are described in [RFC2317].

## 8. Transition to a Long-Term Solution (Condensed)
CIDR was a short-term solution; it does not change the fundamental architecture. It delays but does not eliminate the need for a long-term solution.

## 9. Analysis of CIDR's Effect on Global Routing State (Condensed)
The CIDR Report tracks BGP table growth. Early exponential growth (late 1980s-1994) dropped after BGP4 deployment and CIDR aggregation. Linear growth followed through 1999, then another exponential phase due to the dot-com bubble and increased multi-homing. The "CIDR Police" effort in 2001 flattened growth, but exponential growth resumed in 2004 due to de-aggregation for traffic engineering and lack of consistent configuration advice. As of 2005, ~75,000 base aggregate entries and 85,000 more-specific entries exist.

## 10. Conclusions and Recommendations (Condensed)
CIDR combined with BGP4 solved the immediate crisis. The current system carries approximately 160,000 routes, many for local problems. Further education on aggregation, better multi-homing technology, and traffic engineering without additional routing state are needed. Without these, aggregation remains the only scaling tool.

## 11. Status Updates to CIDR Documents
This memo obsoletes and requests reclassification as Historic the following RFCs:
- RFC 1467, RFC 1481, RFC 1482, RFC 1517, RFC 1518, RFC 1520, RFC 1817, RFC 1878, RFC 2036.

## 12. Security Considerations (Condensed)
CIDR introduces two security concerns: (1) traffic hijacking via more-specific prefix advertisement; (2) denial-of-service attacks by flooding routing tables with many routes. Mitigation requires trust relationships, route filters, and limits on accepted prefix lengths and number of routes. These are not new with CIDR but may be exacerbated by configuration complexity.

## Requirements Summary
| ID  | Requirement | Type | Reference |
|-----|-------------|------|-----------|
| R1  | Forwarding in the Internet is done on a longest-match basis. This implies that destinations that are multi-homed relative to a routing domain must always be explicitly announced into that routing domain (i.e., they cannot be summarized). | must | Section 5.1 Rule 1 |
| R2  | A router that generates an aggregate route for multiple, more-specific routes must discard packets that match the aggregate route, but not any of the more-specific routes. In other words, the "next hop" for the aggregate route should be the null destination. | must (first part), should (second) | Section 5.1 Rule 2 |
| R3  | The degenerate route to prefix 0.0.0.0/0 is used as a default route and MUST be accepted by all implementations. | must | Section 5.1 |
| R4  | This route should only be advertised to another routing domain when a router is explicitly configured to do so, never as a non-configured, "default" option. | should | Section 5.1 |
| R5  | Systems that process route announcements must be able to verify that information that they receive is acceptable according to policy rules. | must | Section 5.3 |
| R6  | Implementations that filter route advertisements must allow masks or prefix lengths in filter elements. | must | Section 5.3 |
| R7  | Under normal circumstances, a routing domain (or "Autonomous System") that has been allocated or assigned a set of prefixes has sole responsibility for aggregation of those prefixes. | shall | Section 5.4 |
| R8  | Transit networks must use internal BGP (iBGP) for carrying routes learned from other providers both within and through their networks. | must | Section 5.5 |
| R9  | It is recommended that an organization that changes service providers plan eventually to migrate its network into a prefix assigned from its new provider's address space. | should | Section 4.1 |
| R10 | It is recommended that mechanisms to facilitate migration, such as DHCP, be deployed wherever possible. | should | Section 4.1 |
| R11 | The assignment of prefixes is intended to roughly follow the underlying Internet topology so that aggregation can be used to facilitate scaling of the global routing system. | (intent, non-normative) | Section 4.2 |

## Informative Annexes (Condensed)
- **Section 6 Example**: Illustrates provider-to-customer delegation, multi-homing, and re-homing scenarios; shows how route advertisements work and how diagnostic tools may confuse.
- **Section 9 Analysis**: Historical BGP table growth trends; explains exponential, linear, and recent exponential phases; attributes to dot-com boom, CIDR Police, and de-aggregation.
- **Section 11 Status Updates**: Lists obsolete RFCs (1467, 1481, 1482, etc.) that are now historic.