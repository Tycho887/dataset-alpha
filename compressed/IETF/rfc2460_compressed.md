# RFC 2460: Internet Protocol, Version 6 (IPv6) Specification
**Source**: IETF – Network Working Group | **Version**: RFC 2460 (Obsoletes RFC 1883) | **Date**: December 1998 | **Type**: Normative (Standards Track)  
**Original**: [RFC 2460](https://tools.ietf.org/html/rfc2460)

## Scope (Summary)
Specifies version 6 of the Internet Protocol (IPv6), including the basic header, extension headers, packet size requirements, semantics of flow labels and traffic classes, and effects on upper-layer protocols. IPv6 expands addressing to 128 bits, simplifies the header, improves support for extensions and options, introduces flow labeling, and supports authentication and privacy capabilities.

## Normative References
- [RFC-791] – Internet Protocol, STD 5
- [RFC-1661] – The Point-to-Point Protocol (PPP), STD 51
- [RFC-1700] – Assigned Numbers, STD 2
- [RFC-1981] – Path MTU Discovery for IP version 6
- [RFC-2401] – Security Architecture for the Internet Protocol
- [RFC-2402] – IP Authentication Header
- [RFC-2406] – IP Encapsulating Security Protocol (ESP)
- [ICMPv6] – ICMP for IPv6, RFC 2463
- [ADDRARCH] – IP Version 6 Addressing Architecture, RFC 2373

## Definitions and Abbreviations
- **node**: a device that implements IPv6.
- **router**: a node that forwards IPv6 packets not explicitly addressed to itself.
- **host**: any node that is not a router.
- **upper layer**: a protocol layer immediately above IPv6 (e.g., TCP, UDP, ICMP, OSPF, or tunneled protocols).
- **link**: a communication facility or medium over which nodes communicate at the link layer (e.g., Ethernet, PPP, ATM).
- **neighbors**: nodes attached to the same link.
- **interface**: a node’s attachment to a link.
- **address**: an IPv6-layer identifier for an interface or set of interfaces.
- **packet**: an IPv6 header plus payload.
- **link MTU**: the maximum transmission unit (in octets) that can be conveyed over a link.
- **path MTU**: the minimum link MTU of all links in a path between source and destination.

## IPv6 Header Format
- **Version**: 4-bit, value = 6.
- **Traffic Class**: 8-bit; see Section 7.
- **Flow Label**: 20-bit; see Section 6.
- **Payload Length**: 16-bit unsigned integer. Length of IPv6 payload (including extension headers) in octets.
- **Next Header**: 8-bit selector. Identifies type of header immediately following IPv6 header (uses same values as IPv4 Protocol field [RFC-1700]).
- **Hop Limit**: 8-bit unsigned integer. Decremented by 1 by each forwarding node; packet discarded if decremented to zero.
- **Source Address**: 128-bit address of originator [ADDRARCH].
- **Destination Address**: 128-bit address of intended recipient (may be modified by Routing header) [ADDRARCH].

## IPv6 Extension Headers
Extension headers are placed between IPv6 header and upper-layer header. Each identified by a distinct Next Header value. Extension headers **must** be processed strictly in the order they appear; a receiver **must not** scan ahead. The Hop-by-Hop Options header is the exception and **must** be examined by every node along the path; it **must** immediately follow the IPv6 header (Next Header = 0 in IPv6 header). If a node encounters an unrecognized Next Header value, it **should** discard the packet and send an ICMP Parameter Problem (Code 1) to the source. The same action **should** be taken if Next Header = 0 appears in any header other than IPv6. Each extension header is an integer multiple of 8 octets; multi-octet fields are aligned on natural boundaries.

A full IPv6 implementation includes: Hop-by-Hop Options, Routing (Type 0), Fragment, Destination Options, Authentication [RFC-2402], Encapsulating Security Payload [RFC-2406].

### Extension Header Order
When multiple extension headers are used, it is **recommended** they appear in this order:
1. IPv6 header
2. Hop-by-Hop Options header
3. Destination Options header (for options to be processed by first destination and subsequent Routing header destinations)
4. Routing header
5. Fragment header
6. Authentication header ([RFC-2406] provides additional ordering recommendations)
7. Encapsulating Security Payload header
8. Destination Options header (for options to be processed only by final destination)
9. Upper-layer header

Each extension header **should** occur at most once, except Destination Options (at most twice). IPv6 nodes **must** accept and attempt to process extension headers in any order and any number of times, except Hop-by-Hop Options **must** appear immediately after an IPv6 header. Sources are **strongly advised** to adhere to the above order.

### Options
Hop-by-Hop Options and Destination Options headers carry TLV-encoded options:
- **Option Type**: 8-bit identifier. Highest-order two bits specify action if unrecognized:
  - `00`: skip and continue.
  - `01`: discard packet.
  - `10`: discard packet and send ICMP Parameter Problem (Code 2) to source (regardless of multicast destination).
  - `11`: discard packet and send ICMP Parameter Problem (Code 2) to source only if destination is not multicast.
- Third-highest bit: `0` = Option Data does not change en-route; `1` = may change. When Authentication header present, data that may change **must** be treated as zero-valued octets for authentication.
- Options are identified by full 8-bit Option Type, not just low-order 5 bits.
- Same numbering space for both headers, but a specification may restrict use.
- **Alignment requirements** specified as `xn+y`.
- **Pad1 option** (Type 0): inserts one octet of padding.
- **PadN option** (Type 1): inserts two or more octets of padding; Opt Data Len = N-2, data zeros.
- These padding options **must** be recognized by all IPv6 implementations.

### Hop-by-Hop Options Header
- Next Header = 0 in IPv6 header.
- Format: Next Header, Hdr Ext Len, Options (variable, multiple of 8 octets).
- Only defined hop-by-hop options in this document: Pad1 and PadN.

### Routing Header
- Next Header = 43.
- Format: Next Header, Hdr Ext Len, Routing Type, Segments Left, type-specific data.
- If Routing Type unrecognized and Segments Left = 0, node **must** ignore header and proceed. If Segments Left non-zero, node **must** discard packet and send ICMP Parameter Problem (Code 0) to source.
- If after processing Routing header a packet is too large for next-hop link MTU, node **must** discard and send ICMP Packet Too Big.
- **Type 0 Routing header**: Routing Type = 0. Contains Reserved (32-bit, zero on transmit, ignored on receive) and Address[1..n]. Multicast addresses **must not** appear in Type 0 Routing header or in IPv6 Destination Address of a packet carrying it.
- Processing algorithm for Type 0 (pseudocode preserved in source):
  - If Segments Left = 0, proceed to next header.
  - Else if Hdr Ext Len is odd, send ICMP Parameter Problem (Code 0) and discard.
  - Else compute n = Hdr Ext Len / 2. If Segments Left > n, send ICMP Parameter Problem and discard.
  - Else decrement Segments Left, compute index i = n - Segments Left. If Address[i] or IPv6 Destination Address is multicast, discard.
  - Else swap IPv6 Destination Address and Address[i]; if Hop Limit ≤ 1, send ICMP Time Exceeded and discard; else decrement Hop Limit and resubmit packet.

### Fragment Header
- Next Header = 44.
- Format: Next Header, Reserved (8-bit), Fragment Offset (13-bit, in 8-octet units), Res (2-bit), M flag (1-bit, 1=more fragments, 0=last), Identification (32-bit).
- Used by source to send packet larger than path MTU. Fragmentation **only at source** (not routers).
- The original packet is divided into Unfragmentable Part (headers up to Routing/Hop-by-Hop) and Fragmentable Part.
- Fragment packets consist of: Unfragmentable Part (with modified Payload Length and Next Header=44), Fragment header with Next Header of first fragmentable header, offset, M flag, and Identification.
- Identification **must** be different from any other recently fragmented packet with same source and destination addresses. A simple 32-bit wrap-around counter is acceptable.
- At destination, reassembly rules:
  - Only fragments with same Source Address, Destination Address, and Identification are reassembled.
  - Unfragmentable Part from first fragment (Offset=0) is used; Next Header from first fragment's Fragment header; Payload Length computed from last fragment.
  - Fragment header is not present in reassembled packet.
- Error conditions:
  - If reassembly not completed within 60 seconds of first fragment arrival, **must** abandon and discard fragments; if first fragment received, **should** send ICMP Time Exceeded.
  - If fragment length not a multiple of 8 octets and M flag=1, **must** discard and **should** send ICMP Parameter Problem (Code 0) pointing to Payload Length.
  - If fragment length/offset would cause reassembled packet > 65535 octets, **must** discard and **should** send ICMP Parameter Problem (Code 0) pointing to Fragment Offset.
  - Differences in preceding headers or Next Header values among fragments are not considered errors; only Offset zero fragment's headers are retained.

### Destination Options Header
- Next Header = 60.
- Format: Next Header, Hdr Ext Len, Options.
- Only defined destination options: Pad1 and PadN.
- Two ways to encode optional destination information: as an option in Destination Options header or as a separate extension header. Choice depends on desired action for unrecognized information:
  - If discard + ICMP only if unicast destination, can be either (using Option Type high bits 11).
  - If other action desired, **must** be encoded as an option with appropriate high bits (00, 01, or 10).

### No Next Header
- Next Header value 59 indicates nothing follows. If Payload Length indicates octets beyond a header with Next Header = 59, those octets **must** be ignored and passed on unchanged if forwarded.

## Packet Size Issues
- Every link **must** have MTU ≥ 1280 octets. Links with configurable MTU (e.g., PPP) **must** be configured to MTU ≥ 1280; it is **recommended** ≥ 1500 octets.
- Each node **must** be able to accept packets as large as the link MTU.
- IPv6 nodes are **strongly recommended** to implement Path MTU Discovery [RFC-1981]. Minimal implementations may restrict sending to ≤ 1280 octets.
- To send a packet larger than path MTU, source may use Fragment header. Fragmentation is **discouraged** in applications that can adjust to path MTU.
- A node **must** be able to accept fragmented packets reassembled to at least 1500 octets. Applications depending on fragmentation should not send reassembled packets > 1500 octets without assurance of destination capability.
- If a node receives an ICMP Packet Too Big reporting a Next-Hop MTU < 1280 (due to IPv6-to-IPv4 translation), it is **not required** to reduce packet size below 1280, but **must** include a Fragment header in subsequent packets.

## Flow Labels
- The 20-bit Flow Label field may be used by source to label packets of a flow for special handling (experimental at time of writing).
- Nodes that do not support Flow Label **must** set the field to zero when originating, pass unchanged when forwarding, and ignore when receiving.
- **Appendix A** describes intended semantics (see condensed version below).

## Traffic Classes
- The 8-bit Traffic Class field is for identifying different classes/priorities. Detailed definitions provided in separate documents.
- Requirements:
  - The service interface **must** allow upper-layer protocols to supply Traffic Class bits; default **must** be zero.
  - Nodes supporting a specific use may change bits in packets they originate, forward, or receive. Nodes **should** ignore and leave unchanged bits they do not support.
  - An upper-layer protocol **must not** assume received Traffic Class bits equal those sent.

## Upper-Layer Protocol Issues

### Upper-Layer Checksums
- Protocols including IP addresses in checksum (e.g., TCP, UDP) **must** use 128-bit IPv6 addresses. The pseudo-header includes Source Address, Destination Address (final destination if Routing header present), Upper-Layer Packet Length, zero, and Next Header.
- **UDP**: checksum is **not optional** for IPv6. Originating node **must** compute checksum; if zero, set to 0xFFFF. Receivers **must** discard UDP packets with zero checksum and **should** log error.
- ICMPv6 includes the pseudo-header in its checksum (Next Header = 58).

### Maximum Packet Lifetime
- IPv6 nodes are **not required** to enforce maximum packet lifetime (unlike IPv4). Upper-layer protocols relying on internet-layer lifetime should provide own mechanisms.

### Maximum Upper-Layer Payload Size
- When computing maximum payload (e.g., TCP MSS), upper-layer protocols **must** account for larger IPv6 header. Minimum IPv6 header is 40 octets vs 20 for IPv4. For TCP over IPv6, MSS = max packet size - 60 octets.

### Responding to Packets Carrying Routing Headers
- Response packets **must not** include a Routing header derived by reversing a received Routing header UNLESS the integrity and authenticity of the received Source Address and Routing header have been verified (e.g., via Authentication header).
- Allowed responses:
  - No Routing header.
  - Routing header not derived by reversal.
  - Routing header derived by reversal only if integrity/authenticity verified.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Extension headers must be processed in order of appearance; receiver must not scan ahead. | **must** | Section 4 |
| R2 | Hop-by-Hop Options header must immediately follow IPv6 header. | **must** | Section 4 |
| R3 | If unrecognized Next Header encountered, node should discard and send ICMP Parameter Problem (Code 1). | **should** | Section 4 |
| R4 | Each extension header must be integer multiple of 8 octets; multi-octet fields aligned naturally. | **must** | Section 4 |
| R5 | Nodes must accept and attempt to process extension headers in any order and any number of times (except Hop-by-Hop). | **must** | Section 4.1 |
| R6 | Sources should adhere to recommended extension header order. | **should** | Section 4.1 |
| R7 | Unrecognized Option Type in Hop-by-Hop or Destination Options: action per high-order two bits. | **must** (per encoding) | Section 4.2 |
| R8 | Pad1 and PadN options must be recognized by all IPv6 implementations. | **must** | Section 4.2 |
| R9 | Routing header: if Segments Left = 0 and unrecognized Routing Type, node must ignore and proceed. | **must** | Section 4.4 |
| R10 | Routing header: if Segments Left ≠ 0 and unrecognized Routing Type, node must discard and send ICMP Parameter Problem. | **must** | Section 4.4 |
| R11 | Routing header: if packet too big for next hop, node must discard and send ICMP Packet Too Big. | **must** | Section 4.4 |
| R12 | Type 0 Routing header: multicast addresses must not appear in Routing header or IPv6 Destination Address of packet. | **must** | Section 4.4 |
| R13 | Fragment Identification must be unique for recently fragmented packets with same source/destination. | **must** | Section 4.5 |
| R14 | Reassembly must be abandoned after 60 seconds; first fragment triggers ICMP Time Exceeded. | **must** / **should** | Section 4.5 |
| R15 | If fragment length not multiple of 8 octets and M=1, fragment must be discarded and ICMP Parameter Problem sent. | **must** / **should** | Section 4.5 |
| R16 | If fragment would cause reassembled packet > 65535 octets, fragment must be discarded and ICMP Parameter Problem sent. | **must** / **should** | Section 4.5 |
| R17 | Link MTU must be ≥ 1280 octets. | **must** | Section 5 |
| R18 | Nodes must accept packets up to link MTU. | **must** | Section 5 |
| R19 | Node must be able to accept fragmented packets reassembled to at least 1500 octets. | **must** | Section 5 |
| R20 | Node receiving ICMP Packet Too Big with MTU < 1280 must include Fragment header in subsequent packets. | **must** | Section 5 |
| R21 | Non-supporting nodes must set Flow Label to zero, pass unchanged, and ignore. | **must** | Section 6 |
| R22 | Service interface must allow upper-layer protocol to supply Traffic Class; default zero. | **must** | Section 7 |
| R23 | UDP checksum must be computed by origin; receivers must discard zero checksum. | **must** | Section 8.1 |
| R24 | Response packets must not reverse Routing header unless authenticated. | **must** | Section 8.4 |
| R25 | Upper-layer payload size calculation must account for larger IPv6 header. | **must** | Section 8.3 |

## Informative Annexes (Condensed)
- **Appendix A – Semantics and Usage of the Flow Label Field**: Describes flows as sequences of packets from a source to a destination with non-zero flow labels. Flow labels must be chosen pseudo-randomly from 1 to 0xFFFFF. All packets in a flow must have same source, destination, flow label, and (if present) Hop-by-Hop Options and Routing header contents (excluding Next Header). Maximum lifetime of flow-handling state must be specified by the establishing mechanism. Source must not reuse flow label within that lifetime. Node restart must avoid reuse until expiry. No requirement that most packets belong to flows.
- **Appendix B – Formatting Guidelines for Options**: Recommends ordering option fields from smallest to largest with no interior padding, then deriving alignment requirement from largest field (max 8 octets). Provides examples for options with 8+4 octet fields and 4+2+1 octet fields, including use of Pad1/PadN to achieve alignment and header length multiple of 8 octets.