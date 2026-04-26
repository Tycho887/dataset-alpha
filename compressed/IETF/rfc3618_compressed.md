# RFC 3618: Multicast Source Discovery Protocol (MSDP)
**Source**: IETF Network Working Group | **Version**: Experimental | **Date**: October 2003 | **Type**: Normative (Experimental)
**Original**: https://tools.ietf.org/html/rfc3618

## Scope (Summary)
This document defines the Multicast Source Discovery Protocol (MSDP), an experimental protocol that connects multiple Protocol Independent Multicast Sparse-Mode (PIM-SM) domains. MSDP allows each domain to use its own Rendezvous Point (RP) and discover multicast sources from other domains without third-party dependencies. The protocol uses TCP for control message exchange and a flood-and-join mechanism.

## Normative References
- [RFC1142] OSI IS-IS Intra-domain Routing Protocol
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- [RFC2328] OSPF Version 2 (STD 54)
- [RFC2362] Protocol Independent Multicast - Sparse Mode (PIM-SM)
- [RFC2365] Administratively Scoped IP Multicast (BCP 23)
- [RFC2385] Protection of BGP Sessions via the TCP MD5 Signature Option
- [RFC2434] Guidelines for Writing an IANA Considerations Section in RFCs (BCP 26)
- [RFC2858] Multiprotocol Extensions for BGP-4
- [RFC3446] Anycast Rendezvous Point (RP) Mechanism using PIM and MSDP

## Informative References
- [DEPLOY] MSDP Deployment Scenarios (Work in Progress, July 2003)
- [RFC2104] HMAC: Keyed-Hashing for Message Authentication
- [RFC2202] Test Cases for HMAC-MD5 and HMAC-SHA-1

## Definitions and Abbreviations
- **MSDP**: Multicast Source Discovery Protocol
- **PIM-SM**: Protocol Independent Multicast – Sparse Mode
- **RP**: Rendezvous Point
- **SA**: Source-Active message
- **MRIB**: Multicast RPF Routing Information Base
- **Peer-RPF**: Reverse Path Forwarding check applied to MSDP peers based on the RP address in the SA message
- **Mesh-group**: A fully meshed set of MSDP peers that reduces SA flooding within a domain

## 1. Introduction
- MSDP connects multiple PIM-SM domains using independent RPs.
- Advantages: no third-party resource dependencies on domain RP; receiver-only domains get data without global group membership advertisement.
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in [RFC2119].

## 2. Overview
- MSDP-speaking routers form TCP peerings; each domain has one or more connections to the virtual MSDP topology.
- Purpose: allow domains to discover multicast sources from other domains. Receivers use PIM-SM source-tree building for inter-domain data delivery.

## 3. Procedure
- When an RP first learns of a new sender (e.g., via PIM Register), it constructs an SA message containing: source address, group address, and RP address. It sends the SA to its MSDP peers.
- **Requirement**: An RP that is not a DR on a shared network MUST NOT originate SAs for directly connected sources on that shared network; it should only originate in response to Register messages from the DR.
- SA forwarding uses peer-RPF flooding: the MRIB determines the RPF peer towards the originating RP. SAs received from a non-RPF peer are dropped. Otherwise, the message is forwarded to all peers except the one from which it was received.
- When an MSDP peer that is also an RP for its own domain receives a new SA, it checks for local (*,G) state with non-empty outgoing interface list. If present, it triggers an (S,G) join towards the data source.
- **Requirement**: If an RP receives a PIM Join for a new group G, it SHOULD trigger an (S,G) join for each active (S,G) in its SA cache.

## 4. Caching
- **R1**: An MSDP speaker MUST cache SA messages.
- Caching allows pacing and reduces join latency.
- The SA-cache is used to reduce storms: do not forward SAs unless they are new or already in cache; advertise from cache at a period of no more than twice per SA-Advertisement-Timer interval and not less than once per period.

## 5. Timers
### 5.1 SA-Advertisement-Timer
- **R2**: [SA-Advertisement-Period] MUST be 60 seconds.
- **R3**: An RP MUST NOT send more than one periodic SA for a given (S,G) within an SA Advertisement interval.
- Originating RP SHOULD trigger an SA as soon as it receives data from an internal source for the first time (may be in addition to the periodic message).

### 5.2 SA-Advertisement-Timer Processing
- **R4**: An RP MUST spread the generation of periodic SA messages over its reporting interval.
- When the timer expires, the RP resets it to [SA-Advertisement-Period] and begins advertising active sources.
- Packets: pack active sources until maximum size is reached or no more sources; repeat until all sources advertised.
- **SHOULD**: send all cached SA messages when a connection is established.
- Timer deleted when MSDP process is de-configured.

### 5.3 SA Cache Timeout (SA-State Timer)
- Each SA cache entry has an associate SA-State Timer.
- Timer started when (S,G)-SA is received; reset to [SG-State-Period] if another (S,G)-SA is received before expiry.
- **R5**: [SG-State-Period] MUST NOT be less than [SA-Advertisement-Period] + [SA-Hold-Down-Period].

### 5.4 Peer Hold Timer
- Initialized to [HoldTime-Period] upon transport connection establishment.
- Reset to [HoldTime-Period] upon receipt of any MSDP message.
- Deleted when transport connection is closed.
- **R6**: [HoldTime-Period] MUST be at least three seconds. Recommended value: 75 seconds.

### 5.5 KeepAlive Timer
- After connection established, each side sends a KeepAlive message and sets a KeepAlive timer.
- If timer expires, send KeepAlive message and restart timer.
- Timer set to [KeepAlive-Period] when peer comes up; reset each time a message is sent; deleted when connection closed.
- **R7**: [KeepAlive-Period] MUST be less than [HoldTime-Period] and MUST be at least one second. Recommended value: 60 seconds.

### 5.6 ConnectRetry Timer
- Used by the MSDP peer with the lower IP address to transition from INACTIVE to CONNECTING.
- One timer per peer. [ConnectRetry-Period] SHOULD be set to 30 seconds.
- When active open attempted, timer initialized to [ConnectRetry-Period]; on expiry, retry connection and reset timer.
- Timer deleted upon transition to ESTABLISHED or peer de-configuration.

## 6. Intermediate MSDP Peers
- Intermediate MSDP speakers do not originate periodic SA messages for sources in other domains.
- **R8**: An RP MUST only originate an SA for a source that would register to it.
- **R9**: Only RPs MAY originate SA messages.
- Intermediate speakers MAY forward SA messages.

## 7. SA Filtering and Policy
- RPs may filter sources in SA messages for policy or state reduction.
- **R10**: Transit MSDP peers SHOULD NOT filter SA messages; doing so may break the flood-and-join model.
- Policy should be expressed using MBGP [RFC2858]. Exception: at administrative scope boundaries.
- **R11**: An SA message for a (S,G) MUST NOT be sent to peers on the other side of an administrative scope boundary for G.

## 8. Encapsulated Data Packets
- An RP MAY encapsulate multicast data from the source in SA messages.
- An interested RP that decapsulates SHOULD forward as if a PIM Register encapsulated packet was received (drop if already receiving on interface toward source; otherwise if outgoing interface list non-null, forward).
- **R12**: When doing data encapsulation, an implementation MUST bound the time during which packets are encapsulated.
- **SHOULD**: encapsulate at least the first packet to support bursty sources.

## 9. Other Scenarios
- MSDP can be used within a routing domain (e.g., Anycast RPs) for multiple RPs for same group ranges.

## 10. MSDP Peer-RPF Forwarding
### 10.1 Definitions
#### 10.1.1 Multicast RPF Routing Information Base (MRIB)
- The multicast topology table, typically derived from unicast routing or multiprotocol BGP [RFC2858].

#### 10.1.2 Peer-RPF Route
- The route chosen by the MRIB for a given address; used to select the peer from which an SA is accepted.

#### 10.1.3 Peer-RPF Forwarding Rules
- An SA message originated by R and received by X from N is accepted if and only if N is the peer-RPF neighbor for X. Otherwise discarded.
- Peer-RPF neighbor selection (deterministic, first match):
  1. If N == R (direct peering).
  2. If N is the eBGP NEXT_HOP of the Peer-RPF route for R.
  3. If the Peer-RPF route for R is learned via distance-vector/path-vector (e.g., BGP, RIP, DVMRP) and N is the neighbor that advertised that route (i.e., iBGP advertiser or IGP next-hop for link-state protocols).
  4. If multiple MSDP peers reside in the closest AS in the best path towards R, the peer with the highest IP address is the RPF peer.
  5. If N is statically configured as the RPF peer for R.
- **R13**: MSDP peers not in state ESTABLISHED are not eligible for peer RPF consideration.

### 10.2 MSDP mesh-group semantics
- A mesh-group is a fully meshed set of MSDP peers used to reduce SA flooding.
- **Rules**:
  1. If a member R of mesh-group M receives an SA from another member of M, R accepts it and forwards it to all peers NOT in M. R MUST NOT forward to other members of M.
  2. If R receives an SA from a non-member (and it passes peer-RPF check), R forwards the SA to all members of M and to any other peers.

## 11. MSDP Connection State Machine
- Uses TCP on port 639. The peer with the higher IP address listens; the lower IP address actively connects.
- State transitions: DISABLED → INACTIVE → LISTEN/CONNECTING → ESTABLISHED.
- Events and actions are defined (see §11.1-11.4).

## 12. Packet Formats
- MSDP messages are in TLV format. Maximum TLV length: 9192 octets.
- **R14**: If a TLV is received with length exceeding maximum, it SHOULD be accepted; additional data SHOULD be ignored; session not reset.
- **R15**: All reserved fields MUST be transmitted as zeros and ignored on receipt.

### 12.1 MSDP TLV format
- Type (8 bits), Length (16 bits), Value (variable). Length field includes Type and Length.

### 12.2 Defined TLVs
- Type 1: IPv4 Source-Active
- Type 2: IPv4 Source-Active Request
- Type 3: IPv4 Source-Active Response
- Type 4: KeepAlive (3 octets)
- Type 5: Reserved (previously Notification)
- Types 6, 7: MSDP traceroute (not described in this memo)

#### 12.2.1 IPv4 Source-Active TLV
- Maximum size 9192 octets (excluding TCP/IP/layer-2 headers).
- Fields: Type=1, Length (x+y), Entry Count, RP Address, Reserved (must be zero), Sprefix Len (MUST be 32), Group Address, Source Address.
- **R16**: If multiple (S,G) entries present, only the last entry may have encapsulated data; it must reflect source/destination addresses in the encapsulated IP header.

#### 12.2.2 KeepAlive TLV
- Sent if no MSDP messages sent within [KeepAlive-Period] seconds.
- Length = 3 octets.

## 13. MSDP Error Handling
- **R17**: If an MSDP message is received with a TLV format error, the session SHOULD be reset with that peer.
- **R18**: Messages with other errors (e.g., unrecognized type) SHOULD be silently discarded; the session SHOULD NOT be reset.

## 14. SA Data Encapsulation
- TCP encapsulation of data in SA messages MAY be supported for backwards compatibility.

## 15. Applicability Statement
### 15.1 Between PIM Domains
- One-to-one peerings using deterministic peer-RPF; no mesh-groups. Scale similar to BGP (hundreds of peerings).

### 15.2 Between Anycast-RPs
- Within a domain using mesh-groups (2-10 peers). External peerings may also exist.

## 16. Intellectual Property
- Standard IPR disclaimer (no specific requirements).

## 17. Acknowledgments
- List of contributors (informative).

## 18. Security Considerations
- **R19**: An MSDP implementation MUST implement Keyed MD5 [RFC2385] to secure control messages.
- **R20**: MUST be capable of interoperating with peers that do not support Keyed MD5.
- **R21**: If one side is configured with Keyed MD5 and the other is not, the connection SHOULD NOT be established.
- **SHOULD**: Use SA filters and limits to mitigate state explosion (access lists, rate-limits).
- **Ought to**: Follow-on work should use stronger integrity (HMAC-SHA1).

## 19. IANA Considerations
- Namespace: "MSDP TLV Values". IANA manages.
- **Allocation rules**: Values 8-200 require IESG Approval or Standards Action [RFC2434]; values 201-255 are experimental.

## 20. References
- Normative and Informative references as listed above.

## 21. Editors' Addresses
- Bill Fenner (AT&T Labs – Research)
- David Meyer (email)

## 22. Full Copyright Statement
- Standard IETF copyright.

---

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | MSDP speaker MUST cache SA messages | MUST | Section 4 |
| R2 | SA-Advertisement-Period MUST be 60 seconds | MUST | Section 5.1 |
| R3 | RP MUST NOT send more than one periodic SA per (S,G) within an SA interval | MUST | Section 5.1 |
| R4 | RP MUST spread periodic SA generation over reporting interval | MUST | Section 5.2 |
| R5 | SG-State-Period MUST NOT be less than SA-Advertisement-Period + SA-Hold-Down-Period | MUST | Section 5.3 |
| R6 | HoldTime-Period MUST be at least 3 seconds (recommended 75) | MUST | Section 5.4 |
| R7 | KeepAlive-Period MUST be less than HoldTime-Period and at least 1 second (recommended 60) | MUST | Section 5.5 |
| R8 | RP MUST only originate SA for source that would register to it | MUST | Section 6 |
| R9 | Only RPs MAY originate SA messages | MAY | Section 6 |
| R10 | Transit MSDP peers SHOULD NOT filter SA messages | SHOULD NOT | Section 7 |
| R11 | SA MUST NOT be sent across administrative scope boundary for G | MUST NOT | Section 7 |
| R12 | Data encapsulation time MUST be bounded | MUST | Section 8 |
| R13 | Peers not in ESTABLISHED state not eligible for peer RPF | MUST | Section 10.1.3 |
| R14 | If TLV length exceeds max, SHOULD accept; SHOULD ignore extra data; session not reset | SHOULD | Section 12 |
| R15 | Reserved fields MUST be transmitted as zeros and ignored | MUST | Section 12.2.1 |
| R16 | If multiple entries and encapsulated data, only last entry may have it; must reflect IP header | MUST | Section 12.2.1 |
| R17 | TLV format errors: session SHOULD be reset | SHOULD | Section 13 |
| R18 | Unrecognized type code: SHOULD silently discard, session SHOULD NOT be reset | SHOULD | Section 13 |
| R19 | MUST implement Keyed MD5 to secure control messages | MUST | Section 18 |
| R20 | MUST be capable of interop with peers not supporting Keyed MD5 | MUST | Section 18 |
| R21 | If one side configured with Keyed MD5 and other not, connection SHOULD NOT be established | SHOULD NOT | Section 18 |

## Informative Annexes (Condensed)
- **Section 16 (Intellectual Property)**: Standard IETF IPR disclaimer.
- **Section 17 (Acknowledgments)**: Lists contributors to the specification.
- **Section 22 (Full Copyright)**: Standard IETF copyright notice with perpetual limited permissions.