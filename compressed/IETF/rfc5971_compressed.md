# RFC 5971: GIST: General Internet Signalling Transport
**Source**: IETF (Internet Engineering Task Force) | **Version**: 1 | **Date**: October 2010 | **Type**: Experimental
**Original**: https://www.rfc-editor.org/rfc/rfc5971

## Scope (Summary)
This document specifies the General Internet Signalling Transport (GIST), an NSIS Transport Layer Protocol (NTLP) that routes and transports per-flow signalling messages along the data path. GIST manages internal state and configures underlying transport (UDP, TCP) and security (TLS) protocols to provide common messaging services for diverse signalling applications, without handling signalling application state itself.

## Normative References
- RFC 2119 (Key words for requirement levels)
- RFC 1122 (Host Requirements)
- RFC 1812 (IPv4 Router Requirements)
- RFC 2460 (IPv6 Specification)
- RFC 2474 (Diffserv Field)
- RFC 2765 (SIIT)
- RFC 5280 (X.509 PKI)
- RFC 3692 (Experimental Numbers)
- RFC 5226 (IANA Guidelines)
- RFC 5234 (ABNF)
- RFC 5978 (NSIS Protocol Family Extensibility)

## Definitions and Abbreviations
- **Data Flow**: Set of packets identified by fixed header fields; unidirectional.
- **Session**: Application-layer exchange for which state is manipulated; identified by Session Identifier (SID) (128-bit opaque value).
- **Session Identifier (SID)**: 128-bit opaque identifier.
- **Querying Node**: Initiates handshake to discover adjacent peer.
- **Responding Node**: Responds to handshake, becoming adjacent peer.
- **Datagram Mode (D-mode)**: Messaging without transport layer state; uses UDP encapsulation.
- **Connection Mode (C-mode)**: Messaging using point-to-point messaging associations (MAs); supports reliability, security.
- **Messaging Association (MA)**: Single connection between adjacent GIST peers; bidirectional; may use transport and security protocols.
- **Message Routing Method (MRM)**: Algorithm for discovering signalling route.
- **Message Routing Information (MRI)**: Data used to route a signalling message; includes flow source/destination addresses, protocol, ports.
- **Router Alert Option (RAO)**: IP option for packet interception.
- **Transfer Attributes**: Requirements for message delivery (reliability, security, local processing).
- **NSLP Identifier (NSLPID)**: 16-bit IANA-assigned identifier for signalling application.
- **Stack-Proposal**: List of protocol profiles for MA setup.
- **Stack-Configuration-Data (SCD)**: Contains MA-Hold-Time and protocol options.
- **Query-Cookie / Responder-Cookie**: Variable-length bit strings for security (return routability, DoS protection).
- **Authorised Peer Database (APD)**: Abstract construct for peer authorisation.
- **Network Layer Information (NLI)**: Includes Peer-Identity, Interface-Address, RS-validity-time, IP-TTL.

## Design Overview
### Overall Design Approach
- GIST uses existing transport (UDP, TCP) and security (TLS) protocols under a common messaging layer.
- GIST does not handle application state; it provides routing and transport services to NSLPs.
- Two main functions: routing (determine adjacent peer) and transport (deliver messages).
- For routing, GIST uses a three-way handshake (Query/Response/Confirm) that probes the network.
- For transport, D-mode (UDP, minimal capability) and C-mode (TCP/TLS for reliability, security, congestion control).

### Modes and Messaging Associations
- **D-mode**: Used for small, infrequent messages without security. Query-mode (Q-mode) for probing without routing state.
- **C-mode**: Used for reliable, secure, or large messages; uses MAs over TCP/TLS.
- Mixing modes along path is allowed.
- MA setup triggered by handshake; MAs are reused for multiple flows and NSLPs.

### Message Routing Methods (MRMs)
- Baseline: path-coupled (signalling follows data flow).
- Other MRMs: predictive routing, NAT address reservations.
- Each MRM defines MRI format, Q-mode encapsulation, validation checks, route change detection.

### GIST Messages
- Six message types: Query, Response, Confirm, Data, Error, MA-Hello.
- All application data carried as NSLP payloads in these messages.
- Handshake (Query/Response/Confirm) sets up routing state and MAs.

### GIST Peering Relationships
- Created by handshake; nodes host NSLP decide to peer.
- Peering can change on refresh due to rerouting or policy changes.

### Signalling Sessions
- SID used to associate messages with a session; must be cryptographically random.
- Routing state keyed by (MRI, SID, NSLPID).

### Security Services
- Two goals: protect GIST state (DoS prevention) and secure NSLP transport.
- Cookie exchange and return routability check protect handshake.
- C-mode uses TLS for channel security; mutual authentication recommended.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Message with GIST hop count of zero MUST be rejected with "Hop Limit Exceeded" error. | MUST | Section 4.3.1 |
| R2 | GIST hop count MUST be decremented by one before next stage. | MUST | Section 4.3.1 |
| R3 | If message arrives on association not matching MRI/NSLPID/SID, MUST reject with "Incorrectly Delivered Message". | MUST | Section 4.3.2 |
| R4 | If no routing state for MRI/SID/NSLPID, message MUST be dropped or rejected with error. | MUST | Section 4.3.2 |
| R5 | Messages with size exceeding Path MTU or 576 bytes (if unknown) MUST be sent over C-mode. | MUST | Section 4.3.3 |
| R6 | Reliable messages with same SID MUST be delivered in order. | MUST | Section 4.1.2 |
| R7 | Signalling applications MUST choose SIDs cryptographically random. | MUST | Section 4.1.3 |
| R8 | In C-mode, for reliable delivery, GIST MUST NOT distribute messages for same session over multiple MAs in parallel. | MUST | Section 4.3.3 |
| R9 | If no appropriate MA exists, message is queued while creating one; if creation fails, error indicated. | MUST | Section 4.3.3 |
| R10 | Query message MUST be sent in Q-mode encapsulation. | MUST | Section 5.1 |
| R11 | Response MUST be sent in D-mode if no existing MA is reused; if reused, in C-mode. | MUST | Section 5.1 |
| R12 | Confirm MUST be sent in C-mode if MA is used; if no MA, in D-mode. | MUST | Section 5.1 |
| R13 | MA-Hello MUST be sent only in C-mode. | MUST | Section 5.1 |
| R14 | For forwards-TCP, support is REQUIRED; Querying node opens connection. | MUST | Section 5.7.2 |
| R15 | For TLS with TCP, support is REQUIRED; Querying node acts as TLS client. | MUST | Section 5.7.3 |
| R16 | TLS implementations MUST NOT negotiate versions prior to TLS1.0; MUST use highest supported. | MUST | Section 5.7.3 |
| R17 | After TLS authentication, node MUST check peer identity against APD; if no match, MA torn down. | MUST | Section 5.7.3.1, 4.4.2 |
| R18 | Error messages MUST NOT generate further error messages. | MUST | Section 5.6 |
| R19 | Error messages MUST NOT be retransmitted explicitly. | MUST | Section 5.6 |
| R20 | When MA is torn down, any associated routing state MUST be deleted. | MUST | Section 4.4.2 |
| R21 | APD entries modified/deleted require re-validation of existing MAs and routing state. | MUST | Section 4.4.2 |
| R22 | Query-Cookie MUST be live, unpredictable, easily validated, unique per handshake. | MUST | Section 8.5 |
| R23 | Responder-Cookie MUST be live, lightweight to generate, simple to validate, bound to routing state. | MUST | Section 8.5 |
| R24 | D-mode retransmissions MUST use binary exponential backoff with initial T1=500ms, max T2=64*T1. | MUST | Section 5.3.3 |
| R25 | Rate control for D-mode SHOULD use token bucket; mean rate no more than 5% of lowest-speed interface. | SHOULD | Section 5.3.3 |
| R26 | For path-coupled MRM, Q-mode downstream encapsulation: destination = flow dest addr; source = flow source addr (S=0) by default; RAO included. | MUST | Section 5.8.1.2 |
| R27 | Upstream Q-mode: destination SHOULD be flow source addr; source SHOULD be signalling node addr (S=1); IP TTL MUST be 255. | SHOULD/MUST | Section 5.8.1.3 |
| R28 | For Loose-End MRM, Q-mode encapsulation: destination = MRI dest addr; source = MRI source addr by default; RAO included. | MUST | Section 5.8.2.2 |

## Formal Protocol Specification (State Machines)
The protocol is defined via four cooperating state machines: Node-SM, Querying-SM, Responding-SM, and MA-SM. Key transitions:
- **Node-SM**: Processes incoming messages; creates Querying-SM or Responding-SM as needed.
- **Querying-SM**: States: Awaiting Response, Established, Awaiting Refresh. Sends Query, waits for Response, then sends Confirm if required.
- **Responding-SM**: States: Awaiting Confirm, Established, Awaiting Refresh. Sends Response, waits for Confirm.
- **MA-SM**: States: Awaiting Connection, Connected, Idle. Manages transport/security setup and keepalive via MA-Hello.

## Route Changes and Local Repair
- GIST detects route changes via local triggers, extended topology info, C-mode monitoring, data plane monitoring, or probing.
- Routing state classified as Bad, Tentative, Good.
- Local repair initiated by Querying node; signalling applications may use SII-Handle for explicit routing.

## NAT Traversal
- Legacy NAT detection: if IP source address differs from interface-address in NLI, error returned.
- GIST-aware NATs use NAT-Traversal object in messages with C=1.
- NAT translates MRI, NLI, SCD; endpoints use translated MRI from object for routing state.

## Security Considerations
- Message confidentiality/integrity via TLS in C-mode.
- Peer authentication via TLS certificates or pre-shared keys.
- Routing state integrity protected by return routability cookies and SID segregation.
- DoS prevention: stateless cookie generation, rate limiting, delayed state installation.
- Downgrade attacks prevented by echoing Stack-Proposal in Confirm.
- Residual threats: on-path attackers, unilateral authentication (only mutual provides full security).

## IANA Considerations (Summary)
- UDP port 270 assigned for Q-mode encapsulation.
- New registries: NSLPIDs (0 reserved), GIST Message Types (0-5 defined), Object Types (0-10 defined), MRM IDs (0=Path-Coupled, 1=Loose-End), MA-Protocol-IDs (0 reserved, 1=Forwards-TCP, 2=TLS), Error Codes/Subcodes (1-12 defined), Additional Information Types (1-4 defined).
- Allocation policies: IETF Review, Expert Review, Specification Required for various ranges.

## Informative Annexes (Condensed)
- **Appendix A (Bit-Level Formats)**: Provides normative formats for common header, TLV objects (MRI, SID, NLI, Stack-Proposal, SCD, Cookies, Hello-ID, NAT-Traversal, NSLP-Data, Error Object). Details error classes and subcode definitions.
- **Appendix B (API)**: Abstract API between GIST and NSLPs including SendMessage, RecvMessage, MessageStatus, NetworkNotification, SetStateLifetime, InvalidateRoutingState. Non-normative but clarifies interface.
- **Appendix C (Deployment Issues with RAO)**: Discusses IPv4 RAO implementation problems; suggests alternatives (no RAO, tunnelling) and notes IPv6 RAO better defined.
- **Appendix D (Example Routing State Table and Handshake)**: Shows example scenario with two NSLPs and handshake sequence including Stack-Proposal and SCD exchange.