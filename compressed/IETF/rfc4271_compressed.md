# RFC 4271: A Border Gateway Protocol 4 (BGP-4)
**Source**: IETF | **Version**: Standards Track | **Date**: January 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc4271/

## Scope (Summary)
This document specifies the Border Gateway Protocol version 4 (BGP-4), an inter-Autonomous System routing protocol. It defines message formats, path attributes, error handling, a finite state machine, route selection and dissemination, and mechanisms for Classless Inter-Domain Routing (CIDR) support and route aggregation.

## Normative References
- [RFC791] – Internet Protocol (STD 5)
- [RFC793] – Transmission Control Protocol (STD 7)
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels
- [RFC2385] – Protection of BGP Sessions via the TCP MD5 Signature Option
- [RFC2434] – Guidelines for Writing an IANA Considerations Section in RFCs

## Definitions and Abbreviations
- **Adj-RIB-In**: Unprocessed routing information advertised to the local BGP speaker by its peers.
- **Adj-RIB-Out**: Routes for advertisement to specific peers via UPDATE messages.
- **Autonomous System (AS)**: A set of routers under a single technical administration with a coherent interior routing plan.
- **BGP Identifier**: A 4-octet unsigned integer set to an IP address assigned to the BGP speaker, same for all interfaces and peers.
- **BGP speaker**: A router that implements BGP.
- **EBGP**: External BGP (connection between peers in different ASes).
- **External peer**: Peer in a different AS.
- **Feasible route**: An advertised route available for use by the recipient.
- **IBGP**: Internal BGP (connection between peers in the same AS).
- **Internal peer**: Peer in the same AS.
- **IGP**: Interior Gateway Protocol.
- **Loc-RIB**: Routes selected by the local BGP speaker's Decision Process.
- **NLRI**: Network Layer Reachability Information.
- **Route**: A unit of information pairing a set of destinations (IP prefix) with path attributes.
- **RIB**: Routing Information Base.
- **Unfeasible route**: A previously advertised feasible route no longer available.

## Introduction
- BGP is an inter-AS routing protocol exchanging network reachability information including AS path lists to enable loop-free routing and policy enforcement.
- BGP-4 supports CIDR by advertising IP prefixes, eliminating network class concepts, and allowing route and AS path aggregation.
- BGP supports only destination-based forwarding; policies not conforming to this paradigm cannot be enforced.

## Summary of Operation
### Routes: Advertisement and Storage
- Routes are advertised in UPDATE messages; multiple routes with same path attributes can be included in one message.
- Routes stored in Adj-RIBs-In, Loc-RIB, Adj-RIBs-Out.
- Routes can be withdrawn via (a) WITHDRAWN ROUTES field, (b) replacement route, or (c) closing the connection.
- Changing attributes: advertise replacement route with new attributes and same prefix.

### Routing Information Base
- Adj-RIBs-In: input from peers.
- Loc-RIB: selected routes (next hop MUST be resolvable via Routing Table).
- Adj-RIBs-Out: routes selected for advertisement.
- Implementation may use single copy with pointers; three copies not required.
- Routing Table accumulates routes from all sources; whether to install BGP route is local policy.

## Message Formats
### Message Header Format
- Fixed-size 19-octet header: Marker (16 octets, MUST be all ones), Length (2 octets, min 19, max 4096), Type (1 octet).
- Type codes: 1-OPEN, 2-UPDATE, 3-NOTIFICATION, 4-KEEPALIVE.
- Multi-octet fields in network byte order.

### OPEN Message Format
- Fields: Version (1 octet, current 4), My Autonomous System (2 octets), Hold Time (2 octets, MUST be >=3 seconds or zero), BGP Identifier (4 octets), Optional Parameters Length (1 octet), Optional Parameters.
- Minimum length: 29 octets.
- Hold Timer: calculated as smaller of configured and received Hold Time; MUST be zero or >=3 seconds; implementation MAY reject.

### UPDATE Message Format
- Fields: Withdrawn Routes Length (2 octets), Withdrawn Routes (variable), Total Path Attribute Length (2 octets), Path Attributes (variable), Network Layer Reachability Information (variable).
- Withdrawn Routes: list of <length, prefix> tuples; each prefix encoded with length in bits.
- Path Attributes: variable-length sequence of triples <attribute type, attribute length, attribute value>.
- Attribute Type: 2 octets (Flags + Type Code). Flags: Optional (bit0), Transitive (bit1), Partial (bit2), Extended Length (bit3). Unused bits MUST be zero when sent, ignored when received.
- Defined Type Codes: ORIGIN (1), AS_PATH (2), NEXT_HOP (3), MULTI_EXIT_DISC (4), LOCAL_PREF (5), ATOMIC_AGGREGATE (6), AGGREGATOR (7).
- NLRI: list of <length, prefix> tuples; length implicit from message length minus fixed fields.
- Minimum UPDATE length: 23 octets.
- An UPDATE message advertises at most one set of path attributes, may advertise multiple destinations sharing them.
- An UPDATE message may simultaneously advertise new routes and withdraw routes; SHOULD NOT include same prefix in Withdrawn Routes and NLRI (but MUST be able to process).
- UPDATE with only withdrawn routes does not include Path Attributes or NLRI.

### KEEPALIVE Message Format
- Consists only of BGP header (19 octets).
- Sent frequently to prevent Hold Timer expiration; maximum interval is one third of Hold Time; MUST NOT be sent more than once per second.
- If Hold Time interval is zero, periodic KEEPALIVE MUST NOT be sent.

### NOTIFICATION Message Format
- Fields: Error Code (1 octet), Error Subcode (1 octet), Data (variable).
- Error Codes: 1-Message Header Error, 2-OPEN Message Error, 3-UPDATE Message Error, 4-Hold Timer Expired, 5-Finite State Machine Error, 6-Cease.
- Minimum length: 21 octets.
- Connection closed immediately after sending.

## Path Attributes
- Categories: Well-known mandatory, Well-known discretionary, Optional transitive, Optional non-transitive.
- BGP implementations MUST recognize all well-known attributes.
- Mandatory attributes (ORIGIN, AS_PATH, NEXT_HOP) MUST be included in every UPDATE with NLRI.
- Well-known discretionary attributes (e.g., LOCAL_PREF, ATOMIC_AGGREGATE) MAY be sent.
- Optional transitive attributes: if unrecognized, SHOULD be accepted and passed along with Partial bit set; recognized transitive attributes must be passed.
- Optional non-transitive attributes: unrecognized MUST be quietly ignored.
- Sender SHOULD order attributes in ascending type code; receiver MUST handle out-of-order.
- Same attribute type cannot appear more than once per UPDATE.

### ORIGIN
- Well-known mandatory. Values: 0 (IGP), 1 (EGP), 2 (INCOMPLETE). Generated by originating speaker; SHOULD NOT be changed.

### AS_PATH
- Well-known mandatory. Composed of path segments: AS_SET (type 1) or AS_SEQUENCE (type 2).
- When advertising to internal peer: SHALL NOT modify AS_PATH.
- When advertising to external peer: prepend own AS as last element of AS_SEQUENCE (or new segment if overflow).
- Originating speaker: includes own AS in AS_SEQUENCE to external peers; empty AS_PATH to internal peers.
- Local system MAY include multiple instances of own AS (controlled by configuration).

### NEXT_HOP
- Well-known mandatory. Defines IP address of next-hop router.
- Internal peer: SHOULD NOT modify unless configured; locally-originated routes use interface address of reachable router.
- External peer (one hop away): may use third-party or first-party NEXT_HOP; default is IP address used for BGP connection.
- External peer (multihop): may propagate NEXT_HOP or default to interface address.
- MUST be able to disable third-party NEXT_HOP for imperfectly bridged media.
- Route originated by local speaker SHALL NOT be advertised with peer's address as NEXT_HOP; SHALL NOT install route with self as next hop.
- Immediate next-hop determined by recursive lookup in Routing Table.

### MULTI_EXIT_DISC
- Optional non-transitive; 4-octet unsigned metric.
- Used to discriminate among multiple entry points to same neighboring AS; lower metric SHOULD be preferred.
- Received over EBGP: MAY be propagated over IBGP; MUST NOT be propagated to other ASes.
- BGP speaker MUST implement mechanism to remove or alter MULTI_EXIT_DISC prior to decision phases 1 and 2.

### LOCAL_PREF
- Well-known attribute; SHALL be included in all UPDATE messages to internal peers.
- Degree of preference calculated from local policy; higher value MUST be preferred.
- MUST NOT be sent to external peers (except BGP Confederations); if received from external peer, MUST be ignored.

### ATOMIC_AGGREGATE
- Well-known discretionary; length 0.
- When aggregating routes and dropping AS_SET, SHOULD include this attribute.
- Receiver SHOULD NOT remove it; MUST NOT de-aggregate (make NLRI more specific).

### AGGREGATOR
- Optional transitive; contains last AS number (2 octets) and IP address (4 octets) of aggregating speaker.
- IP address SHOULD be same as BGP Identifier.

## BGP Error Handling
- Error detected → send NOTIFICATION with appropriate code and subcode, close BGP connection.
- "BGP connection is closed": TCP closed, Adj-RIB-In cleared, resources deallocated; Loc-RIB entries marked invalid; system recalculates best routes and sends updates/withdrawals.

### Message Header Error Handling
- Error Code: Message Header Error.
- Subcodes: 1-Connection Not Synchronized (Marker not all ones), 2-Bad Message Length (Length <19 or >4096 or invalid for message type), 3-Bad Message Type.
- Data field includes erroneous Length or Type as appropriate.

### OPEN Message Error Handling
- Error Code: OPEN Message Error.
- Subcodes: 1-Unsupported Version Number, 2-Bad Peer AS, 3-Bad BGP Identifier, 4-Unsupported Optional Parameter, 5-Deprecated, 6-Unacceptable Hold Time.
- Data for version error: 2-octet largest locally-supported version less than peer's bid, or smallest locally-supported if greater.
- Unacceptable Hold Time: MUST reject 1 or 2 seconds; MAY reject any.

### UPDATE Message Error Handling
- Error Code: UPDATE Message Error.
- Subcodes: 1-Malformed Attribute List, 2-Unrecognized Well-known Attribute, 3-Missing Well-known Attribute, 4-Attribute Flags Error, 5-Attribute Length Error, 6-Invalid ORIGIN Attribute, 7-Deprecated, 8-Invalid NEXT_HOP Attribute, 9-Optional Attribute Error, 10-Invalid Network Field, 11-Malformed AS_PATH.
- Data field contains erroneous attribute where applicable.
- NEXT_HOP syntactic: MUST be valid IP host address. Semantic: MUST NOT be receiver's IP; for EBGP one-hop, MUST be sender's IP or share common subnet.
- If NEXT_HOP semantically incorrect, error SHOULD be logged, route SHOULD be ignored; NOTIFICATION SHOULD NOT be sent.
- If AS_PATH leftmost AS (for external peer) not equal to peer's AS, set Malformed AS_PATH.
- UPDATE with correct attributes but no NLRI is valid.

### NOTIFICATION Message Error Handling
- Errors in received NOTIFICATION: notice and log locally; no NOTIFICATION sent back.

### Hold Timer Expired Error Handling
- If no KEEPALIVE/UPDATE/NOTIFICATION received within Hold Time, send NOTIFICATION with Hold Timer Expired and close connection.

### Finite State Machine Error Handling
- Unexpected events → send NOTIFICATION with Finite State Machine Error.

### Cease
- Peer MAY close connection at any time by sending NOTIFICATION with Cease, but MUST NOT when fatal error exists.
- BGP speaker MAY configure upper bound on number of prefixes accepted; if exceeded, either discard prefixes or close connection with Cease NOTIFICATION.

### BGP Connection Collision Detection
- Collision occurs when two connections between same pair of speakers exist with swapped source/destination IPs.
- Preservation rule: retain connection initiated by speaker with higher BGP Identifier.
- Upon receiving OPEN, examine connections in OpenConfirm (and optionally OpenSent) state; if collision exists, compare BGP Identifiers; lower identifier's system closes existing connection (if in OpenConfirm) or new connection (if OPEN message is from higher identifier).
- Collision with Established state: close new connection unless configured otherwise.
- Connection closed by sending Cease NOTIFICATION.

## BGP Version Negotiation
- Peers MAY attempt multiple opens starting with highest supported version.
- If open fails with Unsupported Version Number error, peers can determine highest common version.
- Future versions MUST retain OPEN and NOTIFICATION message formats.

## BGP Finite State Machine (FSM)
- Conceptual FSM defined; implementations must exhibit same externally visible behavior.
- Mandatory session attributes: State, ConnectRetryCounter, ConnectRetryTimer, ConnectRetryTime, HoldTimer, HoldTime, KeepaliveTimer, KeepaliveTime.
- Optional session attributes (e.g., AllowAutomaticStart, DelayOpen, DampPeerOscillations, PassiveTcpEstablishment) enable additional FSM functionality.

### Events for the BGP FSM
- Events grouped: Administrative Events (1-8), Timer Events (9-13), TCP Connection-Based Events (14-18), BGP Message-Based Events (19-28).
- Key events: ManualStart, ManualStop, AutomaticStart, ConnectRetryTimer_Expires, HoldTimer_Expires, KeepaliveTimer_Expires, TcpConnection_Valid, TcpConnectionConfirmed, TcpConnectionFails, BGPOpen, BGPOpen with DelayOpenTimer running, KeepAliveMsg, UpdateMsg, etc.

### FSM States
- **Idle**: Refuse connections; resources deallocated. On ManualStart/AutomaticStart: initialize resources, start ConnectRetryTimer, initiate TCP connection, listen, go to Connect. On ManualStart/AutomaticStart with PassiveTcpEstablishment: go to Active.
- **Connect**: Waiting for TCP completion. On success: if DelayOpen TRUE, stay in Connect; else send OPEN, set HoldTimer to large value (4 min), go to OpenSent. On failure: if DelayOpenTimer running, go to Active; else go to Idle.
- **Active**: Listening for TCP connection. On success: similar handling as Connect. On failure: restart ConnectRetryTimer, go to Idle.
- **OpenSent**: Waiting for OPEN message. On valid OPEN: send KEEPALIVE, set HoldTimer negotiated, go to OpenConfirm. On error: send NOTIFICATION, go to Idle.
- **OpenConfirm**: Waiting for KEEPALIVE or NOTIFICATION. On KEEPALIVE: restart HoldTimer, go to Established. On HoldTimer_Expires: send NOTIFICATION, go to Idle.
- **Established**: Can exchange UPDATE, NOTIFICATION, KEEPALIVE. On UPDATE: process, restart HoldTimer. On error: send NOTIFICATION, go to Idle.

### FSM Actions
- Detailed state transitions with events and actions for each state (as per RFC text, preserved in requirements below).

## UPDATE Message Handling
- Only received in Established state.
- Unrecognized optional non-transitive attributes: quietly ignored.
- Unrecognized optional transitive attributes: Partial bit set to 1, retained for propagation.
- Withdrawn routes: remove from Adj-RIB-In, run Decision Process.
- Feasible route: if NLRI identical to existing, replace; else add.

### Decision Process
- Three phases: Phase 1 (degree of preference), Phase 2 (route selection), Phase 3 (route dissemination).
- Phase 1: For routes from internal peers, LOCAL_PREF or local policy; from external peers, compute degree based on policy, use as LOCAL_PREF for IBGP readvertisement.
- Phase 2: Select best route per destination; exclude unresolvable routes (NEXT_HOP not resolvable) and routes with AS loop. Tie-breaking: smallest AS_PATH length, lowest origin, lowest MULTI_EXIT_DISC (comparable only within same neighboring AS), prefer EBGP over IBGP, lowest IGP cost to NEXT_HOP, lowest BGP Identifier, lowest peer address.
- Phase 3: Install selected routes in Loc-RIB; update Adj-RIBs-Out per policy; run Update-Send process.

### Update-Send Process
- Advertise newly installed routes and withdrawals; SHOULD NOT advertise same route again.
- Internal peer updates: not re-distributed to other internal peers (unless Route Reflector).
- If UPDATE message size limit exceeded, route MUST NOT be advertised; error may be logged.

### Controlling Routing Traffic Overhead
- MinRouteAdvertisementIntervalTimer: minimum interval between advertisements to same common set of destinations; per-peer timer. For internal peers, SHOULD be shorter or not apply.
- MinASOriginationIntervalTimer: minimum interval between advertisements of changes within local AS.
- Defaults: EBGP 30 seconds, IBGP 5 seconds.

### Aggregation
- Rules for aggregating path attributes: NEXT_HOP, ORIGIN, AS_PATH, ATOMIC_AGGREGATE, AGGREGATOR.
- Routes with different MULTI_EXIT_DISC SHALL NOT be aggregated.
- Detailed AS_PATH aggregation algorithm specified.

## BGP Timers
- Mandatory timers: ConnectRetryTimer (default 120s), HoldTimer (default 90s, large value 4 min), KeepaliveTimer (default 1/3 HoldTime), MinASOriginationIntervalTimer (default 15s), MinRouteAdvertisementIntervalTimer (EBGP 30s, IBGP 5s).
- Optional timers: DelayOpenTimer, IdleHoldTimer.
- HoldTimer MUST be configurable per-peer; other timers MAY be configurable.
- Jitter SHOULD be applied to MinASOriginationIntervalTimer, KeepaliveTimer, MinRouteAdvertisementIntervalTimer, ConnectRetryTimer (random factor 0.75 to 1.0).

## Informative Annexes (Condensed)
- **Annex A**: Comparison with RFC 1771 – Lists technical changes including deprecations, new features (TCP MD5, Route Reflectors, Confederations), clarifications (NEXT_HOP types, tie-breaking, frequency of advertisements).
- **Annex B**: Comparison with RFC 1267 – BGP-4 adds IP prefix concept, CIDR support, new attributes (LOCAL_PREF, ATOMIC_AGGREGATE, AGGREGATOR), Hold Timer negotiation, renaming INTER_AS_METRIC to MULTI_EXIT_DISC.
- **Annex C**: Comparison with RFC 1163 – Adds BGP Identifier for collision detection, removes restriction on NEXT_HOP being within same AS.
- **Annex D**: Comparison with RFC 1105 – Major message format changes, removal of Up/Down/Horizontal relations, addition of Hold Time field to OPEN.
- **Annex E**: TCP Options – BGP messages SHOULD use TCP PUSH; DSCP field bits 0-2 SHOULD be set to 110; implementations MUST support TCP MD5 [RFC2385].
- **Annex F**: Implementation Recommendations – Includes multiple networks per message (highly recommended), reducing route flapping (combine withdraw and update), optional path attribute ordering and AS_SET sorting, version negotiation control, and complex AS_PATH aggregation algorithm.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The Marker field MUST be set to all ones. | MUST | Section 4.1 |
| R2 | The Length field MUST be at least 19 and no greater than 4096. | MUST | Section 4.1 |
| R3 | Hold Time MUST be either zero or at least three seconds. | MUST | Section 4.2 |
| R4 | KEEPALIVE messages MUST NOT be sent more frequently than one per second. | MUST | Section 4.4 |
| R5 | BGP implementations MUST recognize all well-known attributes. | MUST | Section 5 |
| R6 | Well-known mandatory attributes (ORIGIN, AS_PATH, NEXT_HOP) MUST be included in every UPDATE message that contains NLRI. | MUST | Section 5 |
| R7 | When a BGP speaker advertises a route to an internal peer, it SHALL NOT modify the AS_PATH attribute. | SHALL NOT | Section 5.1.2 |
| R8 | The LOCAL_PREF attribute SHALL be included in all UPDATE messages sent to internal peers. | SHALL | Section 5.1.5 |
| R9 | A BGP speaker MUST NOT include LOCAL_PREF in UPDATE messages sent to external peers (except Confederations). | MUST NOT | Section 5.1.5 |
| R10 | If a path with an unrecognized transitive optional attribute is accepted and passed, the Partial bit MUST be set to 1. | MUST | Section 5 |
| R11 | The NEXT_HOP attribute MUST be a valid IP host address; it MUST NOT be the IP address of the receiving speaker. | MUST | Section 6.3 |
| R12 | A BGP speaker SHALL NOT install a route with itself as the next hop. | SHALL NOT | Section 5.1.3 |
| R13 | Upon detection of an error, a NOTIFICATION message with the appropriate Error Code MUST be sent, and the BGP connection closed. | MUST | Section 6 |
| R14 | BGP MUST maintain a separate FSM for each configured peer. | MUST | Section 8.2.1 |
| R15 | If the HoldTimer expires, the local system MUST send a NOTIFICATION with Hold Timer Expired and close the connection. | MUST | Section 6.5 |
| R16 | Routes with unresolvable NEXT_HOP MUST be excluded from Phase 2 decision. | MUST | Section 9.1.2 |
| R17 | The MinRouteAdvertisementIntervalTimer MUST be observed between advertisements to the same common set of destinations. | MUST | Section 9.2.1.1 |
| R18 | Routes with different MULTI_EXIT_DISC attributes SHALL NOT be aggregated. | SHALL NOT | Section 9.2.2.2 |
| R19 | A BGP speaker SHALL calculate the degree of preference for each external route and include it in IBGP readvertisement as LOCAL_PREF. | SHALL | Section 9.1.1 |
| R20 | An UPDATE message with correct path attributes but no NLRI SHALL be treated as valid. | SHALL | Section 6.3 |