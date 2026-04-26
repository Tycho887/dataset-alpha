# RFC 791: Internet Protocol
**Source**: DARPA Internet Program | **Version**: Replaces RFC 760 | **Date**: September 1981 | **Type**: Normative
**Original**: RFC 791 (prepared by USC/ISI for DARPA)

## Scope (Summary)
Defines the Internet Protocol (IP) for transmitting datagrams across interconnected packet-switched networks. It specifies addressing, fragmentation, and basic service mechanisms (Type of Service, Time to Live, Options, Header Checksum). IP is a best-effort, connectionless datagram service without end-to-end reliability, flow control, or sequencing.

## Normative References
- [1] Cerf, V., "The Catenet Model for Internetworking," IEN 48, July 1978.
- [2] BBN Report 1822, "Specification for the Interconnection of a Host and an IMP," Revised May 1978.
- [3] Postel, J., "Internet Control Message Protocol," RFC 792, September 1981.
- [4] Shoch, J., "Inter-Network Naming, Addressing, and Routing," COMPCON, Fall 1978.
- [5] Postel, J., "Address Mappings," RFC 796, September 1981.
- [6] Shoch, J., "Packet Fragmentation in Inter-Network Protocols," Computer Networks, v.3, n.1, February 1979.
- [7] Strazisar, V., "How to Build a Gateway", IEN 109, August 1979.
- [8] Postel, J., "Service Mappings," RFC 795, September 1981.
- [9] Postel, J., "Assigned Numbers," RFC 790, September 1981.

## Definitions and Abbreviations
- **Datagram**: Unit of data exchanged between internet modules, including internet header.
- **Fragment**: A portion of a datagram with an internet header.
- **Internet Address**: 32-bit address (Network field + Local Address field).
- **IHL**: Internet Header Length in 32-bit words (minimum 5).
- **MF**: More Fragments flag (bit 2 of Flags).
- **DF**: Don't Fragment flag (bit 1 of Flags).
- **TTL**: Time to Live (8-bit field, maximum lifetime 255 seconds).
- **TOS**: Type of Service (8-bit field: precedence, D, T, R bits).
- **ICMP**: Internet Control Message Protocol (RFC 792).
- **GGP**: Gateway to Gateway Protocol.
- **TCP, UDP, TFTP**: Higher-level protocols.
- **MTU**: Maximum Transmission Unit of a network.
- **NFB**: Number of Fragment Blocks (8-octet units).

## 1. Introduction
### 1.1 Motivation
IP designed for interconnected packet-switched networks. Transmits datagrams from source to destination hosts (fixed-length addresses). Provides fragmentation and reassembly for "small packet" networks.

### 1.2 Scope
Limited to delivering datagrams over interconnected systems. No end-to-end reliability, flow control, or sequencing. May capitalize on underlying network services for QoS.

### 1.3 Interfaces
Called by host-to-host protocols (e.g., TCP). Calls local network protocols to transmit datagram to next gateway or destination. Example: TCP module supplies address and parameters; IP module creates datagram and invokes local net interface.

### 1.4 Operation
Two basic functions: addressing and fragmentation. Internet modules in hosts and gateways share common rules for addresses and fragmentation. No connections or logical circuits. Key mechanisms:
- **Type of Service**: indicates desired quality (abstract parameters: precedence, delay, throughput, reliability).
- **Time to Live**: upper bound on datagram lifetime; if zero, destroyed.
- **Options**: control functions (timestamps, security, special routing). Must be implemented by all IP modules.
- **Header Checksum**: verification of header integrity; datagram discarded on failure.
IP provides no error control for data, no acknowledgments, no retransmissions, no flow control. Errors reported via ICMP.

## 2. Overview
### 2.1 Relation to Other Protocols
IP interfaces between higher-level (TCP, UDP, etc.) and local network protocols.

### 2.2 Model of Operation
Scenario: Sending application calls internet module with destination address. IP creates datagram, sends to local net. Datagram traverses networks via gateways (each gateway forwards based on internet address). At destination, IP passes data to application.

### 2.3 Function Description
#### Addressing
- Names, addresses, routes distinguished. Addresses are 32-bit, consisting of network number and local address (called "rest").
- Three classes: A (high bit 0, 7 net, 24 host), B (10, 14 net, 16 host), C (110, 21 net, 8 host). Extended addressing (111) reserved.
- A single host may have multiple internet addresses (multi-homing). Mapping to local net addresses must allow this.

#### Fragmentation
- Necessary when datagram must traverse a network with smaller MTU.
- "Don't Fragment" flag prohibits fragmentation; such datagrams discarded if cannot be delivered.
- Fragments identified by **Identification**, **Fragment Offset** (in 8-octet units), and **More Fragments** flag.
- Procedure for splitting and reassembly specified (see Section 3.2 for pseudocode).

### 2.4 Gateways
Implement IP to forward datagrams between networks. Also implement GGP for routing coordination. Higher-level protocols not needed in gateways.

## 3. Specification
### 3.1 Internet Header Format
Fields (32-bit words):
- **Version** (4 bits): Must be 4.
- **IHL** (4 bits): Header length in 32-bit words; minimum valid value 5.
- **Type of Service** (8 bits): 3 bits precedence, 1 bit each for D (delay), T (throughput), R (reliability), 2 bits reserved (must be zero). Precedence values: 111 Network Control, 110 Internetwork Control, 101 CRITIC/ECP, 100 Flash Override, 011 Flash, 010 Immediate, 001 Priority, 000 Routine.
- **Total Length** (16 bits): Length of datagram in octets, up to 65,535. All hosts must accept datagrams up to 576 octets.
- **Identification** (16 bits): Assigned by sender to aid reassembly.
- **Flags** (3 bits): Bit 0 reserved (must be zero), Bit 1 DF (Don't Fragment), Bit 2 MF (More Fragments).
- **Fragment Offset** (13 bits): Offset in 8-octet units (first fragment offset zero).
- **Time to Live** (8 bits): Maximum time in seconds; decremented at each processing point by at least 1. If zero, datagram destroyed.
- **Protocol** (8 bits): Next level protocol (values from [9]).
- **Header Checksum** (16 bits): 1's complement of 1's complement sum of all 16-bit words in header.
- **Source Address** (32 bits).
- **Destination Address** (32 bits).
- **Options** (variable): Must be implemented by all IP modules. Two format cases: single option-type octet, or option-type + length + data. Option type: 1 bit copied flag, 2 bits class, 5 bits number. Defined options:
    - End of Option List (type 0): terminates options.
    - No Operation (type 1): alignment.
    - Security (type 130, length 11): carries Security (16 bits), Compartments (16 bits), Handling Restrictions (16 bits), TCC (24 bits). Must be copied on fragmentation.
    - Loose Source and Record Route (type 131): source route with intermediate gateways allowed. Must be copied on fragmentation.
    - Strict Source and Record Route (type 137): source route with direct next hop only. Must be copied on fragmentation.
    - Record Route (type 7): records addresses of gateways. Not copied on fragmentation; first fragment only.
    - Stream ID (type 136, length 4): carries SATNET stream identifier. Must be copied on fragmentation.
    - Internet Timestamp (type 68): records timestamps (with optional address). Not copied on fragmentation; first fragment only.
- **Padding**: variable zeros to align header to 32-bit boundary.

### 3.2 Discussion
General robustness principle: implementations must be conservative in sending, liberal in receiving.

#### Addressing (details)
- Address formats: Class A (0 + 7 net + 24 host), B (10 + 14 + 16), C (110 + 21 + 8), escape (111) reserved.
- Network field zero reserved for "this network" (used in ICMP). Extended addressing undefined.
- Local address must allow multiple internet addresses per physical host and multiple physical interfaces.

#### Fragmentation and Reassembly (normative rules)
- Every internet module must be able to forward a datagram of 68 octets without fragmentation.
- Every internet destination must be able to receive a datagram of 576 octets (whole or fragments).
- Data portion must be split on 8-octet boundaries.
- Fields affected by fragmentation: options, MF flag, fragment offset, IHL, total length, checksum.
- If DF=1, fragmentation prohibited; datagram discarded if too large.
- Pseudocode for fragmentation and reassembly provided (not normative but illustrative; exact algorithm not mandatory as long as behavior matches).

#### Identification
- Must be unique for source-destination-protocol triple for the time the datagram is alive in the internet.
- Sender may use per-destination table or simply unique identifiers (65,536 values). Higher-level protocols (e.g., TCP) may choose identifier to aid retransmission.

#### Type of Service
- Abstract parameters: precedence, delay, throughput, reliability. Mapped to actual network service parameters. Example mapping to ARPANET given.

#### Time to Live
- Set by sender as maximum lifetime. Must be decreased by at least 1 at each processing point. Maximum TTL is 255 seconds (4.25 minutes). Used to bound datagram lifetime for reliable connection protocols.

#### Options
- Optional in each datagram but required in implementations: every internet module must be able to parse every option.
- Security option is required if classified/restricted/compartmented traffic is to be passed.

#### Checksum
- Recpmputed if header changes (e.g., TTL, options, fragmentation). Only protects header, not data.

#### Errors
- Reported via ICMP messages [3].

### 3.3 Interfaces
Functional interface to IP via SEND and RECV calls. Parameters:
- SEND: (src, dst, prot, TOS, TTL, BufPTR, len, Id, DF, opt => result)
- RECV: (BufPTR, prot => result, src, dst, TOS, len, opt)
- Source address must be one of the legal addresses for the host.
- On datagram arrival, if no RECV pending, user is notified; if user does not exist, ICMP error sent.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All hosts must be prepared to accept datagrams of up to 576 octets (whole or fragments). | must | Section 3.1 (Total Length) |
| R2 | Every internet module must be able to forward a datagram of 68 octets without further fragmentation. | must | Section 3.2 (Fragmentation) |
| R3 | Every internet destination must be able to receive a datagram of 576 octets either in one piece or in fragments to be reassembled. | must | Section 3.2 (Fragmentation) |
| R4 | Options must be implemented by all IP modules (hosts and gateways). | must | Section 3.1 (Options) |
| R5 | If the Don't Fragment flag (DF) is set, internet fragmentation of the datagram is NOT permitted. | shall (prohibition) | Section 3.2 (Fragmentation) |
| R6 | The Time to Live (TTL) field must be decreased by at least one at each point the internet header is processed. | must | Section 3.2 (TTL) |
| R7 | The header checksum must be recomputed if the internet header is changed. | must | Section 3.2 (Checksum) |
| R8 | The Security option must be copied on fragmentation. | must | Section 3.1 (Security option) |
| R9 | The Loose Source and Record Route option must be copied on fragmentation. | must | Section 3.1 (LSRR) |
| R10 | The Strict Source and Record Route option must be copied on fragmentation. | must | Section 3.1 (SSRR) |
| R11 | The Record Route option must not be copied on fragmentation; it appears only in the first fragment. | (normative) | Section 3.1 (Record Route) |
| R12 | The Internet Timestamp option must not be copied on fragmentation; it appears only in the first fragment. | (normative) | Section 3.1 (Timestamp) |
| R13 | The Version field must be 4 for this specification. | must | Section 3.1 |
| R14 | The IHL field must have a minimum value of 5 for a correct header. | (normative) | Section 3.1 |
| R15 | Bit 0 of the Flags field is reserved and must be zero. | must | Section 3.1 |
| R16 | Fragments must be broken on 8-octet boundaries. | must | Section 3.2 |
| R17 | The Identification field must be unique for the source-destination-protocol triple for the lifetime of the datagram. | must | Section 3.2 (Identification) |
| R18 | The source address supplied in a SEND call must be a legal address for the sending host. | must | Section 3.3 |
| R19 | Every internet module must be able to act on every option. | must | Section 3.2 (Options) |
| R20 | The Security option is required if classified, restricted, or compartmented traffic is to be passed. | (normative when applicable) | Section 3.2 (Options) |

## Informative Annexes (Condensed)
- **Appendix A: Examples & Scenarios**: Illustrates header format with minimal datagram (21 octets), moderate datagram (472 octets) and its fragmentation into two fragments (276 and 216 octets), and a datagram with options. Demonstrates correct field values in each case.
- **Appendix B: Data Transmission Order**: Specifies that octets are transmitted in network byte order (big-endian, most significant octet first). Bits within an octet are transmitted most significant first. Multi-octet fields use the same order.
- **Glossary**: Defines key terms (see Definitions and Abbreviations above).
- **References**: Lists all cited documents (see Normative References above).