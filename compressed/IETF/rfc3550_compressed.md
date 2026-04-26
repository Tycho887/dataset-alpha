# RFC 3550: RTP: A Transport Protocol for Real-Time Applications
**Source**: IETF | **Version**: Standards Track, Obsoletes RFC 1889 | **Date**: July 2003 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc3550/

## Scope (Summary)
This document specifies the real-time transport protocol (RTP), which provides end-to-end delivery services for data with real-time characteristics (e.g., interactive audio/video). RTP includes payload type identification, sequence numbering, timestamping, and delivery monitoring. It is augmented by the RTP Control Protocol (RTCP) for monitoring data delivery, identification, and minimal control. RTP does not guarantee quality-of-service or resource reservation.

## Normative References
1. RFC 3551 – RTP Profile for Audio and Video Conferences with Minimal Control
2. BCP 14, RFC 2119 – Key words for use in RFCs (MUST, SHOULD, etc.)
3. STD 5, RFC 791 – Internet Protocol
4. RFC 1305 – Network Time Protocol (Version 3)
5. RFC 2279 – UTF-8, a Transformation Format of ISO 10646
6. STD 13, RFC 1034 – Domain Names – Concepts and Facilities
7. STD 13, RFC 1035 – Domain Names – Implementation and Specification
8. STD 3, RFC 1123 – Requirements for Internet Hosts – Application and Support
9. RFC 2822 – Internet Message Format

## Definitions and Abbreviations
- **RTP payload**: Data transported by RTP in a packet (e.g., audio samples, compressed video).
- **RTP packet**: A data packet consisting of fixed RTP header, possibly empty CSRC list, and payload.
- **RTCP packet**: A control packet with fixed header and structured elements; multiple RTCP packets can form a compound RTCP packet.
- **Port**: Abstraction used by transport protocols to distinguish among multiple destinations within a host.
- **Transport address**: Combination of network address and port (e.g., IP address + UDP port).
- **RTP media type**: Collection of payload types that can be carried within a single RTP session.
- **Multimedia session**: Set of concurrent RTP sessions among a common group of participants (e.g., audio + video).
- **RTP session**: Association among participants communicating with RTP; each session maintains a separate SSRC identifier space.
- **Synchronization source (SSRC)**: Source of a stream of RTP packets, identified by a 32-bit SSRC identifier; all packets from an SSRC share same timing and sequence number space.
- **Contributing source (CSRC)**: Source that contributed to a mixed stream produced by an RTP mixer; listed in CSRC list.
- **End system**: Application generating or consuming RTP content.
- **Mixer**: Intermediate system that receives RTP packets, possibly changes data format, combines them, and forwards a new RTP packet.
- **Translator**: Intermediate system that forwards RTP packets with SSRC identifier intact (e.g., encoding conversion, multicast-to-unicast replication).
- **Monitor**: Application that receives RTCP packets to estimate quality of service; may be third-party.
- **Non-RTP means**: Protocols/mechanisms outside RTP (e.g., SIP, H.323, SDP, RTSP) for distribution of addresses, keys, dynamic payload type mappings.

## Byte Order, Alignment, and Time Format
- All integer fields in network byte order (big-endian).
- Header data aligned to natural length (16-bit fields on even offsets, 32-bit on 4-byte boundaries).
- Wallclock time uses NTP timestamp format (64-bit fixed-point, seconds since 0h UTC 1 Jan 1900). Some fields use middle 32 bits.
- NTP not required; other time sources may be used.
- RTP uses NTP timestamps for synchronization, but only differences between pairs are used.

## 5. RTP Data Transfer Protocol

### 5.1 RTP Fixed Header Fields
```
    0                   1                   2                   3
    0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |V=2|P|X|  CC   |M|     PT      |       sequence number         |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |                           timestamp                           |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
   |           synchronization source (SSRC) identifier            |
   +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
   |            contributing source (CSRC) identifiers             |
   |                             ....                              |
   +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
- **version (V)**: 2 bits, value 2 for this spec.
- **padding (P)**: 1 bit; if set, packet contains padding octets at end; last octet of padding gives count of padding octets (including itself).
- **extension (X)**: 1 bit; if set, fixed header MUST be followed by exactly one header extension (Section 5.3.1).
- **CSRC count (CC)**: 4 bits, number of CSRC identifiers following fixed header.
- **marker (M)**: 1 bit; interpretation defined by profile; MAY define additional marker bits.
- **payload type (PT)**: 7 bits; identifies RTP payload format; MAY be dynamically defined via non-RTP means; SHOULD NOT be used for multiplexing separate media streams. A receiver MUST ignore packets with unknown payload types.
- **sequence number**: 16 bits; increments by one per packet; used for loss detection and ordering. Initial value SHOULD be random (unpredictable) to make known-plaintext attacks more difficult.
- **timestamp**: 32 bits; sampling instant of first octet in RTP data packet. Clock MUST increment monotonically and linearly; resolution MUST be sufficient for desired synchronization accuracy. Initial value SHOULD be random.
- **SSRC**: 32 bits; identifies synchronization source; SHOULD be chosen randomly with intent of global uniqueness within session. Implementations MUST detect and resolve collisions (Section 8). If a source changes its source transport address, it MUST choose a new SSRC identifier.
- **CSRC list**: 0 to 15 items, 32 bits each; identifies contributing sources for payload; inserted by mixers.

### 5.2 Multiplexing RTP Sessions
- Each medium (audio, video) SHOULD be carried in separate RTP session with its own destination transport address.
- Separate audio and video SHOULD NOT be carried in single RTP session; demultiplexing by payload type or SSRC is not allowed (problems listed: encoding changes, timing spaces, RTCP limitations, mixing, network path/resource allocation).
- Multiplexing multiple related sources of same medium in one RTP session using different SSRC is normal for multicast.

### 5.3 Profile-Specific Modifications to RTP Header
- Marker bit and payload type field may be redefined by profile; one marker bit SHOULD be in most significant bit of octet.
- Additional information for payload format (e.g., video header) SHOULD be carried in payload section.
- Additional functionality needed for class of applications SHOULD be defined as fixed fields following SSRC (after first 12 octets).

#### 5.3.1 RTP Header Extension
- If X bit = 1, variable-length header extension MUST be appended after CSRC list.
- Extension contains 16-bit length field (count of 32-bit words, excluding 4-octet extension header; zero is valid).
- Only one extension per packet.
- First 16 bits of extension are profile-specific (for distinguishing identifiers/parameters).
- This mechanism is intended for limited use; profile-specific fixed extensions and payload headers are preferred.

## 6. RTP Control Protocol – RTCP

- RTCP performs four functions:
  1. Feedback on quality of data distribution (sender/receiver reports).
  2. Persistent transport-level identifier (CNAME) for each RTP source.
  3. Rate control to scale to large numbers of participants.
  4. Optional: minimal session control information (e.g., participant ID).
- Functions 1–3 SHOULD be used in all environments, especially IP multicast.
- Transmission of RTCP MAY be controlled separately for senders and receivers (e.g., for unidirectional links).

### 6.1 RTCP Packet Format
- RTCP packet types: SR (200), RR (201), SDES (202), BYE (203), APP (204).
- Compound RTCP packet: multiple RTCP packets concatenated; first packet MUST be SR or RR; each compound packet MUST include a report packet and SDES CNAME (except when split for partial encryption).
- All RTCP packets MUST be sent in a compound packet of at least two individual packets.
- Format: encryption prefix (random 32-bit if encrypted), SR/RR, additional RRs if needed, SDES with CNAME, then BYE/APP (BYE SHOULD be last for given SSRC/CSRC).
- An individual participant SHOULD send only one compound RTCP packet per report interval.
- If compound packet exceeds MTU, SHOULD be segmented into multiple shorter compound packets, each beginning with SR or RR.
- Implementations SHOULD ignore unknown RTCP packet types.

### 6.2 RTCP Transmission Interval
- Session bandwidth parameter supplied by session management; all participants MUST use same value.
- Control traffic SHOULD be limited to 5% of session bandwidth; 1/4 of RTCP bandwidth SHOULD be dedicated to data senders.
- Profile MAY specify separate bandwidth parameters for senders (S) and receivers (R); default recommended: 1.25% and 3.75%.
- Minimum interval between compound RTCP packets SHOULD be 5 seconds; MAY be scaled inversely proportional to session bandwidth for active senders in multicast, and for unicast sessions.
- Delay before first RTCP packet SHOULD be half the minimum interval.
- Algorithm in Section 6.3 and Appendix A.7 calculates interval; includes randomization, timer reconsideration, reverse reconsideration.

#### 6.2.1 Maintaining Number of Session Members
- New sites added when heard; entries SHOULD be created in table indexed by SSRC/CSRC.
- New entries MAY be considered not valid until multiple packets or CNAME received.
- Entries SHOULD be marked as BYE received and deleted after delay.
- Participant MAY mark another site inactive if no packet received for 5 RTCP report intervals (recommended).
- For very large sessions, SSRC sampling MAY be used to reduce storage.
- Algorithm SHOULD NOT substantially underestimate group size, though MAY overestimate.

### 6.3 RTCP Packet Send and Receive Rules
- Implementation in multicast/multipoint unicast MUST meet Section 6.2 requirements; MAY use algorithm in Section 6.3 or equivalent.
- Two-party unicast SHOULD use randomization but MAY omit timer reconsideration and reverse reconsideration.
- State required: tp, tc, tn, pmembers, members, senders, rtcp_bw, we_sent, avg_rtcp_size, initial.

#### 6.3.1 Computing the RTCP Transmission Interval
- If senders <= 25% of members: senders use C = avg_rtcp_size / (0.25 * rtcp_bw), n = senders; receivers use C = avg_rtcp_size / (0.75 * rtcp_bw), n = receivers. If senders > 25%, both use C = avg_rtcp_size / rtcp_bw, n = members.
- If initial, Tmin = 2.5 s, else 5 s.
- Deterministic interval Td = max(Tmin, n*C).
- Actual interval T uniformly distributed between 0.5 and 1.5 times Td.
- Divide by 1.21828 to compensate for timer reconsideration.

#### 6.3.2 Initialization
- Join: tp=0, tc=0, senders=0, pmembers=1, members=1, we_sent=false, rtcp_bw = specified fraction, initial=true, avg_rtcp_size = probable size of first RTCP packet.
- Compute T, schedule first packet at tn = T. Add own SSRC to member table.

#### 6.3.3 Receiving RTP or Non-BYE RTCP Packet
- Add SSRC to member table if new; update members after validation. Same for CSRC.
- Add to sender table if new RTP packet.
- Update avg_rtcp_size: avg_rtcp_size = (1/16)*packet_size + (15/16)*avg_rtcp_size.

#### 6.3.4 Receiving RTCP BYE Packet
- Remove SSRC from member and sender tables; update members and senders.
- If members drops below pmembers, execute reverse reconsideration: tn = tc + (members/pmembers)*(tn - tc); tp = tc - (members/pmembers)*(tc - tp); reschedule at tn; pmembers = members.

#### 6.3.5 Timing Out an SSRC
- Compute deterministic interval Td for receiver (we_sent=false). Time out any member not heard since tc - 5*Td.
- Remove from member list; update members.
- Time out sender if not sent RTP since tc - 2T; remove from sender list; update senders.
- If any members timed out, perform reverse reconsideration.
- MUST check at least once per RTCP transmission interval.

#### 6.3.6 Expiration of Transmission Timer
- Compute T (including randomization). If tp+T <= tc, transmit RTCP packet; set tp=tc; compute new T; set tn = tc+T; schedule timer. Else tn = tp+T; schedule timer.
- Set pmembers = members; if transmitted, set initial=false; update avg_rtcp_size.

#### 6.3.7 Transmitting a BYE Packet
- If members > 50: reset tp=tc, members=pmembers=1, initial=1, we_sent=false, senders=0, avg_rtcp_size = size of compound BYE; compute T; schedule BYE at tn = tc+T.
- On receiving BYE, increment members by 1; do not increment for other packets; update avg_rtcp_size only for BYE.
- Transmission follows regular rules.
- If members <= 50, MAY send BYE immediately or use backoff algorithm.
- A participant that never sent RTP or RTCP MUST NOT send BYE.

#### 6.3.8 Updating we_sent
- Set to true when RTP packet sent; add self to sender table. Perform reverse reconsideration.
- Remove self from sender table if no RTP transmitted within tc - 2T.

#### 6.3.9 Allocation of Source Description Bandwidth
- No more than 20% of RTCP bandwidth per participant SHOULD be used for additional SDES items beyond CNAME.
- Additional SDES items SHOULD be assigned bandwidth fractions statically based on utility.
- When multiple RTP sessions are bound via common CNAME, extra SDES info MAY be sent in only one session.

### 6.4 Sender and Receiver Reports
- SR (type 200) includes sender info (20 bytes); RR (type 201) does not.
- Both include zero or more reception report blocks (max 31 per packet); additional RR packets stacked if needed.
- Reports SHOULD select subsets round-robin over intervals if too many sources.

#### 6.4.1 SR: Sender Report RTCP Packet
Header fields: V=2, P, RC (5 bits), PT=200, length, SSRC of sender.
Sender info: NTP timestamp (64 bits), RTP timestamp (32 bits), sender's packet count (32 bits), sender's octet count (32 bits). Counts SHOULD be reset if SSRC changes.
Reception report block (for each source):
- SSRC_n (32 bits)
- fraction lost (8 bits)
- cumulative number of packets lost (24 bits, signed)
- extended highest sequence number received (32 bits)
- interarrival jitter (32 bits)
- last SR timestamp (LSR) (32 bits)
- delay since last SR (DLSR) (32 bits, 1/65536 seconds)
- Jitter calculation MUST conform to formula in spec.

#### 6.4.2 RR: Receiver Report RTCP Packet
Same as SR except PT=201 and no sender info.

#### 6.4.3 Extending Sender and Receiver Reports
- Profile SHOULD define profile-specific extensions if additional regular information needed; prefer this over new RTCP packet type.
- Extension follows reception report blocks.

#### 6.4.4 Analyzing Sender and Receiver Reports
- Cumulative counts allow short/long term measurements.
- Fraction lost provides short-term measurement.
- Interarrival jitter tracks transient congestion.
- Jitter calculation MUST be same formula across all receivers.
- Variation in packet transmission delay affects jitter but subtracts out in comparative use.

### 6.5 SDES: Source Description RTCP Packet
- Structure: header, chunks (SSRC/CSRC + list of SDES items). Each item: 8-bit type, 8-bit length, text (UTF-8). Items not individually padded; list terminated by one or more null octets; pad to 32-bit boundary.
- Only CNAME is mandatory; other items optional.
- New SDES types registered with IANA.

#### 6.5.1 CNAME: Canonical End-Point Identifier
- type=1; format "user@host" or "host" if no user; host = fully qualified domain name or ASCII numeric address. SHOULD be algorithmically derived, not entered manually.
- CNAME MUST be included; SHOULD be unique among session participants; SHOULD be fixed for binding across media tools.
- If private network addresses used, applications MAY provide means to configure unique CNAME; translator responsible for translating if needed.

#### 6.5.2 NAME: User Name
- type=2; real name. SHOULD NOT be relied upon for uniqueness.

#### 6.5.3 EMAIL: Electronic Mail Address
- type=3; format RFC 2822.

#### 6.5.4 PHONE: Phone Number
- type=4; format "+..." (plus sign replacing international access code).

#### 6.5.5 LOC: Geographic User Location
- type=5; format and content MAY be prescribed by profile.

#### 6.5.6 TOOL: Application or Tool Name
- type=6; name and version.

#### 6.5.7 NOTE: Notice/Status
- type=7; transient messages; SHOULD NOT be included routinely; SHOULD NOT be auto-generated.
- When inactive, continue transmitting a few times with zero-length string; receivers SHOULD consider inactive if not received for small multiple of repetition rate.

#### 6.5.8 PRIV: Private Extensions
- type=8; prefix length (8 bits) + prefix string + value string; prefix should be kept short; not registered with IANA; if useful, assign regular SDES type.

### 6.6 BYE: Goodbye RTCP Packet
- type=203; indicates one or more sources no longer active; source count (SC) in header.
- Optionally includes reason for leaving (length + text).
- If received by mixer, mixer SHOULD forward unchanged; mixer shutting down SHOULD send BYE listing all handled sources plus own SSRC.

### 6.7 APP: Application-Defined RTCP Packet
- type=204; for experimental use; unrecognized names SHOULD be ignored.
- After testing, RECOMMENDED to redefine without subtype and name and register with IANA.

## 7. RTP Translators and Mixers

### 7.1 General Description
- To avoid loops: connected clouds MUST be distinct in at least one parameter (protocol, address, port) or isolated; no parallel translators unless sources partitioned.
- All end systems sharing same SSRC space; SSRC identifiers MUST be unique.
- Translator: forwards RTP packets with SSRC intact; may modify payload, timestamp, sequence numbers.
- Mixer: marks packets with own SSRC; SHOULD insert original SSRCs into CSRC list; mixer that is also a contributing source SHOULD include own SSRC in CSRC list.
- For some applications it MAY be acceptable for mixer not to list CSRCs, but risk of loop detection.

### 7.2 RTCP Processing in Translators
- Translator that does not modify data MAY forward RTCP unchanged.
- Translator that transforms payload MUST modify SR/RR accordingly; MUST NOT simply forward.
- SHOULD NOT aggregate SR/RR from different sources into one packet.
- Translator does not require own SSRC but MAY allocate one for reports.
- SDES CNAMEs MUST be forwarded for collision detection.
- BYE forwarded unchanged; translator ceasing forwarding SHOULD send BYE to each cloud.

### 7.3 RTCP Processing in Mixers
- Mixer generates own SR for mixed stream; does not pass through sender info.
- Generates own reception reports for sources in each cloud; sends only to that cloud.
- SDES CNAMEs MUST be forwarded; mixer MUST send own CNAME.
- BYE MUST be forwarded; mixer shutting down SHOULD send BYE.
- APP handling is application-specific.

### 7.4 Cascaded Mixers
- Second mixer SHOULD build CSRC list using CSRCs from already-mixed packets and SSRCs from unmixed packets. If >15, remainder excluded.

## 8. SSRC Identifier Allocation and Use

- SSRC is random 32-bit number; required to be globally unique within an RTP session.
- Not sufficient to use local network address; multiple sources on one host would conflict.
- Use random() with careful initialization; example in Appendix A.6.

### 8.1 Probability of Collision
- For N=1000 simultaneous start, probability ~10^-4; for one new source joining, ~2*10^-7.
- Further reduced if new source receives packets from others before first transmission and checks for conflict.

### 8.2 Collision Resolution and Loop Detection
- If a source discovers another using same SSRC, it MUST send RTCP BYE for old identifier and choose new random one.
- If receiver discovers collision between two other sources, it MAY keep packets from one.
- Loops detected by same SSRC but different source transport address or different CNAME.
- Implementation MUST include algorithm similar to that described (pseudocode). It keeps table indexed by SSRC, stores source transport addresses. On collision:
  - If not own SSRC: abort processing; optionally count collision/loop.
  - If own SSRC and address in conflicting list: count loop; ignore packet.
  - Else: log collision, create conflicting address entry, send BYE with old SSRC, choose new SSRC.
- When new SSRC chosen, SHOULD check table for existing use; if found, MUST generate another candidate.
- All mixers and translators MUST implement loop detection to break loops.
- If extreme loop, end systems MAY cease transmission; error condition SHOULD be indicated; transmission MAY be retried after long random time (order of minutes).

### 8.3 Use with Layered Encodings
- Single SSRC identifier space SHOULD be used across sessions of all layers; base (core) layer SHOULD be used for allocation and collision resolution.
- When collision resolved, transmit RTCP BYE on only base layer but change SSRC in all layers.

## 9. Security

- Default encryption algorithm is DES in CBC mode (as per RFC 1423), with padding indicated by P bit.
- Implementations SHOULD support DES as default; it is RECOMMENDED to use stronger algorithms (e.g., Triple-DES).
- RTP confidentiality: encrypt entire unit; for RTCP prepend 32-bit random number; for RTP use random sequence number and timestamp offsets.
- For RTCP, implementation MAY split compound packet into encrypted and clear parts (e.g., encrypt SDES, leave RR clear); CNAME required in only one part; same SDES info SHOULD NOT be in both.
- Presence of encryption confirmed by header/payload validity checks (Appendices A.1, A.2).
- Profiles MAY define additional payload types for encrypted encodings.
- Authentication and message integrity not defined at RTP level; expected from lower layers.

## 10. Congestion Control
- Congestion control SHOULD be defined in each RTP profile as appropriate.
- Some profiles may require data rate adaptation based on RTCP feedback; others may rely on engineering.

## 11. RTP over Network and Transport Protocols
- RTP SHOULD use even destination port; RTCP SHOULD use next higher (odd). If explicit separate parameters given, MAY disregard even/odd/consecutive but still encouraged. RTP and RTCP port numbers MUST NOT be same.
- In unicast session, both participants MAY use same port pair. Participant MUST NOT assume source port can be used as destination port.
- RTCP SR packets MUST be sent to port specified for RTCP reception by other participant.
- For layered encodings: data port = P + 2n, control port = P + 2n + 1; IP multicast addresses MUST be distinct.
- RTP data packets rely on underlying protocol for length indication.
- If underlying protocol provides continuous octet stream, encapsulation with framing MUST be defined.
- Profile MAY specify framing method to carry multiple RTP packets in one lower-layer unit.

## 12. Summary of Protocol Constants

### 12.1 RTCP Packet Types
- SR: 200, RR: 201, SDES: 202, BYE: 203, APP: 204. Values chosen to allow header validity checking.

### 12.2 SDES Types
- END: 0, CNAME: 1, NAME: 2, EMAIL: 3, PHONE: 4, LOC: 5, TOOL: 6, NOTE: 7, PRIV: 8.

## 13. RTP Profiles and Payload Format Specifications
- A complete specification requires profile and payload format documents.
- Profile defines: possible RTP header modifications, payload types and mappings, header additions/extensions, RTCP packet types, report interval constants, SR/RR extensions, SDES usage, security, congestion control, underlying protocol, transport mapping, encapsulation.
- Not required to have new profile for every application; extend existing.

## 14. Security Considerations
- Same liabilities as underlying protocols; IP multicast provides no privacy.
- Use of security mechanisms (Section 9) is important.
- Translators/mixers behind firewalls must follow firewall security principles.

## 15. IANA Considerations
- New RTCP packet types and SDES types must be documented in RFC or other permanent reference; registration requires designated expert.
- Profile names should be registered in form "RTP/xxx".

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | RTP version field MUST be 2. | MUST | 5.1 |
| R2 | If X bit is set, fixed header MUST be followed by exactly one header extension. | MUST | 5.1 |
| R3 | A receiver MUST ignore packets with payload types it does not understand. | MUST | 5.1 |
| R4 | Initial value of sequence number SHOULD be random (unpredictable). | SHOULD | 5.1 |
| R5 | Timestamp clock MUST increment monotonically and linearly. | MUST | 5.1 |
| R6 | SSRC identifier SHOULD be chosen randomly. | SHOULD | 5.1 |
| R7 | All RTP implementations MUST be prepared to detect and resolve SSRC collisions. | MUST | 5.1, 8.2 |
| R8 | If a source changes its source transport address, it MUST choose a new SSRC identifier. | MUST | 5.1 |
| R9 | Separate audio and video streams SHOULD NOT be carried in a single RTP session. | SHOULD | 5.2 |
| R10 | First RTCP packet in compound packet MUST be a report packet (SR or RR). | MUST | 6.1 |
| R11 | Each compound RTCP packet MUST include an SDES CNAME (except when split for partial encryption). | MUST | 6.1 |
| R12 | All RTCP packets MUST be sent in a compound packet of at least two individual packets. | MUST | 6.1 |
| R13 | The underlying protocol MUST provide multiplexing of data and control packets. | MUST | 6 |
| R14 | All participants MUST use the same value for session bandwidth. | MUST | 6.2 |
| R15 | It is RECOMMENDED that the RTCP fraction of session bandwidth be fixed at 5%. | RECOMMENDED | 6.2 |
| R16 | It is RECOMMENDED that 1/4 of RTCP bandwidth be dedicated to data senders. | RECOMMENDED | 6.2 |
| R17 | All participants MUST use same constants for RTCP interval calculation. | MUST | 6.2 |
| R18 | RECOMMENDED value for fixed minimum RTCP interval is 5 seconds. | RECOMMENDED | 6.2 |
| R19 | Profile MAY specify that control traffic bandwidth may be separate parameter. | MAY | 6.2 |
| R20 | Turning off RTCP reception reports is NOT RECOMMENDED. | NOT RECOMMENDED | 6.2 |
| R21 | RTCP transmission interval SHOULD also have a lower bound. | SHOULD | 6.2 |
| R22 | At application startup, a delay SHOULD be imposed before first compound RTCP packet. | SHOULD | 6.2 |
| R23 | Implementations in multicast/multipoint unicast MUST meet Section 6.2 requirements. | MUST | 6.3 |
| R24 | If received RTCP BYE reduces members below pmembers, reverse reconsideration SHOULD be performed. | SHOULD | 6.3.4 |
| R25 | Participant MUST check for timeouts at least once per RTCP transmission interval. | MUST | 6.3.5 |
| R26 | If members > 50 when leaving, MUST execute BYE backoff algorithm. | MUST | 6.3.7 |
| R27 | Participant that never sent RTP or RTCP MUST NOT send BYE. | MUST | 6.3.7 |
| R28 | No more than 20% of RTCP bandwidth per participant SHOULD be used for additional SDES items. | SHOULD | 6.3.9 |
| R29 | Jitter calculation MUST conform to the specified formula. | MUST | 6.4.1, 6.4.4 |
| R30 | Reception reports SHOULD NOT carry over statistics when source changes SSRC due to collision. | SHOULD | 6.4.1 |
| R31 | CNAME item MUST be included in SDES. | MUST | 6.5.1 |
| R32 | CNAME identifier SHOULD be unique among all participants within one RTP session. | SHOULD | 6.5.1 |
| R33 | CNAME SHOULD be fixed for a participant across related RTP sessions. | SHOULD | 6.5.1 |
| R34 | CNAME SHOULD be derived algorithmically, not manually entered. | SHOULD | 6.5.1 |
| R35 | CNAME format SHOULD be "user@host" or "host". | SHOULD | 6.5.1 |
| R36 | NAME value SHOULD NOT be relied upon for uniqueness. | SHOULD NOT | 6.5.2 |
| R37 | NOTE item SHOULD NOT be included routinely by all participants. | SHOULD NOT | 6.5.7 |
| R38 | NOTE item SHOULD NOT be automatically generated. | SHOULD NOT | 6.5.7 |
| R39 | BYE packet received by mixer, mixer SHOULD forward unchanged. | SHOULD | 6.6 |
| R40 | Mixer shutting down SHOULD send BYE listing all handled sources plus own SSRC. | SHOULD | 6.6 |
| R41 | APP packets with unrecognized names SHOULD be ignored. | SHOULD | 6.7 |
| R42 | Each cloud connected by translators/mixers MUST be distinct in at least one parameter or isolated. | MUST | 7.1 |
| R43 | All SSRC identifiers among end systems sharing translators/mixers MUST be unique. | MUST | 7.1 |
| R44 | All data packets forwarded by mixer MUST be marked with mixer's own SSRC. | MUST | 7.1 |
| R45 | Mixer SHOULD insert SSRC identifiers of original sources into CSRC list. | SHOULD | 7.1 |
| R46 | Mixer that is also contributing source SHOULD explicitly include its own SSRC in CSRC list. | SHOULD | 7.1 |
| R47 | Translator MUST assign new sequence numbers if multiple packets re-encoded into one or vice versa. | MUST | 7.1 |
| R48 | Translator that transforms payload MUST modify SR/RR accordingly; MUST NOT simply forward. | MUST | 7.2 |
| R49 | Translator SHOULD NOT aggregate SR/RR packets from different sources into one packet. | SHOULD | 7.2 |
| R50 | CNAMEs MUST be forwarded by translators and mixers for SSRC collision detection. | MUST | 7.2, 7.3 |
| R51 | Mixer MUST forward BYE packets. | MUST | 7.3 |
| R52 | Second mixer in cascade SHOULD build CSRC list using CSRCs from already-mixed packets and SSRCs from unmixed. | SHOULD | 7.4 |
| R53 | If source discovers collision, MUST send RTCP BYE for old SSRC and choose new random one. | MUST | 8.2 |
| R54 | Implementation MUST include algorithm similar to Section 8.2 for collision resolution and loop detection. | MUST | 8.2 |
| R55 | When new SSRC chosen after collision, candidate SHOULD first be looked up in source identifier table; if already in use, another MUST be generated. | SHOULD/MUST | 8.2 |
| R56 | All mixers and translators MUST implement loop detection algorithm like that in Section 8.2. | MUST | 8.2 |
| R57 | For layered encodings, single SSRC space SHOULD be used across layers; base layer SHOULD be used for allocation and collision resolution. | SHOULD | 8.3 |
| R58 | Implementations that support encryption per Section 9 SHOULD always support DES in CBC mode as default. | SHOULD | 9.1 |
| R59 | For RTCP encryption, 32-bit random number redrawn for each unit MUST be prepended. | MUST | 9.1 |
| R60 | Congestion control SHOULD be defined in each RTP profile as appropriate. | SHOULD | 10 |
| R61 | RTP SHOULD use even destination port; RTCP SHOULD use next higher (odd). | SHOULD | 11 |
| R62 | RTP and RTCP port numbers MUST NOT be the same. | MUST | 11 |
| R63 | In unicast session, participant MUST NOT assume source port of incoming RTP/RTCP can be used as destination port for outgoing. | MUST | 11 |
| R64 | RTCP SR packets MUST be sent to port specified for RTCP reception by other participant. | MUST | 11 |
| R65 | For layered encodings, port numbers MUST be distinct; data port = P+2n, control = P+2n+1. | MUST (distinct) | 11 |
| R66 | If RTP carried over continuous octet stream, encapsulation with framing MUST be defined. | MUST | 11 |
| R67 | Payload types 72 and 73 are reserved (to avoid confusion with SR/RR in header validation). | (Reserved) | 12 |
| R68 | Profile MUST specify RTP timestamp clock rate for each payload type. | MUST | 13 |
| R69 | Profile SHOULD specify constants for RTCP interval calculation. | SHOULD | 13 |
| R70 | Profile SHOULD specify congestion control behavior. | SHOULD | 13 |
| R71 | New RTCP packet types and SDES types must be documented in RFC or other permanent reference; registration requires designated expert. | (IANA) | 15 |

## Informative Annexes (Condensed)
- **Appendix A – Algorithms**: Provides example C code for RTP header validity checks (A.1), RTCP header validity checks (A.2), determining packets expected/lost (A.3), generating/parsing SDES (A.4, A.5), random identifier generation (A.6), RTCP transmission interval computation (A.7), and interarrival jitter estimation (A.8). These are informative implementations; alternative methods allowed.
- **Appendix B – Changes from RFC 1889**: Lists changes: enhanced RTCP timer algorithm (reconsideration, reverse reconsideration), BYE flood control, removal of state retention for long partitions, scaling to large sessions via SSRC sampling, optional separate RTCP bandwidth parameters, relaxed minimum interval and initial delay, new congestion control section, clarified port conventions, relaxed SSRC change requirement, corrected pseudocode and various clarifications. No wire protocol changes.