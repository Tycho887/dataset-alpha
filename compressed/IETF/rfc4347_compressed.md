# RFC 4347: Datagram Transport Layer Security (DTLS) Version 1.0
**Source**: IETF | **Version**: 1.0 | **Date**: April 2006 | **Type**: Standards Track
**Original**: https://tools.ietf.org/html/rfc4347

## Scope (Summary)
This document specifies Version 1.0 of the Datagram Transport Layer Security (DTLS) protocol. DTLS provides communications privacy for datagram protocols, preserving datagram semantics (unreliable, unordered delivery) while offering equivalent security guarantees to TLS. It is designed as a minimal set of changes to TLS 1.1 to operate over unreliable transports such as UDP.

## Normative References
- RFC 1191: Path MTU discovery
- RFC 1981: Path MTU Discovery for IPv6
- RFC 2401: Security Architecture for the Internet Protocol
- RFC 2988: Computing TCP's Retransmission Timer
- RFC 793 (STD 7): Transmission Control Protocol (TCP)
- RFC 4346: TLS Protocol Version 1.1
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels

## Definitions and Abbreviations
- **DTLS**: Datagram Transport Layer Security
- **TLS**: Transport Layer Security
- **Record Layer**: The layer that carries protected application data and handshake messages.
- **Handshake Message**: A message that is part of the DTLS handshake protocol, including ClientHello, ServerHello, etc.
- **Flight**: A group of handshake messages that are sent as a unit (monolithic for timeout/retransmission).
- **EPOCH**: A counter incremented on each cipher state change (ChangeCipherSpec).
- **Sequence Number**: A 48-bit explicit number in each record, used for MAC and anti-replay.
- **Message Sequence Number (message_seq)**: A 16-bit number assigned to each handshake message within a handshake.
- **Fragment Offset/Length**: Fields in handshake header for fragmentation/reassembly.
- **Cookie**: A stateless token used in HelloVerifyRequest for DoS protection.
- **PMTU**: Path Maximum Transmission Unit

## 1. Introduction (Condensed)
DTLS extends TLS 1.1 to work over unreliable datagram transports (e.g., UDP). TLS requires reliable ordered delivery; DTLS adds explicit sequence numbers, retransmission timers, handshake fragmentation, and a cookie exchange for DoS resilience. The goal is to minimize changes to TLS to maximize code reuse.

## 2. Usage Model (Condensed)
DTLS runs in application space, requires no kernel modifications. It preserves datagram semantics for payload data; it does not compensate for lost or reordered traffic. Applications such as streaming media, VoIP, and online gaming can use DTLS transparently.

## 3. Overview of DTLS (Condensed)
DTLS is constructed as "TLS over datagram". Two main issues:
1. **Traffic encryption layer**: Records are not independent (CBC chaining, implicit sequence numbers). Fix: add explicit CBC state (from TLS 1.1) and explicit 48-bit sequence numbers.
2. **Handshake layer**: Assumes reliable delivery. Fix: retransmission timers for packet loss, sequence numbers for reordering, fragmentation for large messages.
Replay detection is optional, using a sliding window (same as IPsec AH/ESP).

### 3.1 Loss-Insensitive Messaging
- **Requirement**: Cryptographic context (CBC state, stream cipher key stream) MUST NOT be chained between records (use explicit IV from TLS 1.1).
- **Requirement**: Anti-replay and reordering protection uses explicit sequence numbers in MAC calculation.

### 3.2 Providing Reliability for Handshake
- **Packet Loss**: DTLS uses a simple retransmission timer. The client retransmits ClientHello if no HelloVerifyRequest/ServerHello is received. The server also retransmits its flight if timer expires.
- **Reordering**: Each handshake message has a unique `message_seq`. Messages received out of sequence are queued until preceding messages arrive.
- **Message Size**: Handshake messages may be fragmented over multiple DTLS records using `fragment_offset` and `fragment_length`.

### 3.3 Replay Detection (Informative)
DTLS optionally supports record replay detection using a bitmap window. Records too old or previously received are silently discarded. Feature is optional; duplication can occur due to routing errors.

## 4. Differences from TLS
DTLS is presented as a series of deltas from TLS 1.1. The following subsections detail the changes.

### 4.1 Record Layer
- **DTLSPlaintext structure** (new fields in bold):
  ```c
  struct {
    ContentType type;
    ProtocolVersion version;
    uint16 epoch;            // New
    uint48 sequence_number;  // New
    uint16 length;
    opaque fragment[DTLSPlaintext.length];
  } DTLSPlaintext;
  ```
- **version**: DTLS 1.0 uses {254,255}. This is the one's complement of DTLS 1.0 version number to distinguish from TLS.
- **epoch**: Counter incremented on every cipher state change (ChangeCipherSpec). MUST NOT allow epoch reuse within two times TCP maximum segment lifetime.
- **sequence_number**: Explicit sequence number. Reset to zero after each ChangeCipherSpec.
- **length**: MUST not exceed 2^14 bytes.

#### 4.1.1 Transport Layer Mapping
- **[R1]**: Each DTLS record MUST fit within a single datagram.
- **[R2]**: To avoid IP fragmentation, DTLS implementations SHOULD determine the MTU and send records smaller than the MTU.
- **[R3]**: DTLS implementations SHOULD provide a way for applications to determine PMTU (or maximum application datagram size = PMTU minus DTLS overhead).
- **[R4]**: If application attempts to send a record larger than MTU, DTLS implementation SHOULD generate an error.
- Multiple DTLS records may be placed in a single datagram; first byte of datagram MUST be the beginning of a record. Records MUST NOT span datagrams.
- No association identifiers in DTLS records; multiplexing via host/port (UDP).
- When carried over transports with their own sequence numbers (e.g., DCCP), both DTLS and transport sequence numbers are present.

##### 4.1.1.1 PMTU Discovery
- **[R5]**: PMTU SHOULD be initialized from the interface MTU.
- **[R6]**: On receipt of ICMP "Datagram Too Big", DTLS implementation should decrease PMTU estimate accordingly.
- **[R7]**: DTLS implementation SHOULD allow application to occasionally reset PMTU estimate.
- **[R8]**: DTLS implementation SHOULD allow applications to control DF bit.
- **[R9]**: For IPv6, RFC 1981 procedures SHOULD be followed.
- **[R10]**: Handshake messages should be sent with DF set.
- **[R11]**: DTLS implementations SHOULD back off handshake packet size during retransmit backoff (e.g., after 3 retransmits, fragment the message).

#### 4.1.2 Record Payload Protection

##### 4.1.2.1 MAC
- MAC computation uses 64-bit value: epoch (16 bits) concatenated with sequence_number (48 bits).
- MAC uses on-the-wire version number {254,255} for DTLS 1.0.
- **[R12]**: In DTLS, MAC errors MAY simply discard the offending record and continue. (Contrast with TLS which must terminate.)
- **[R13]**: DTLS implementations SHOULD silently discard data with bad MACs.
- **[R14]**: If DTLS implementation chooses to generate an alert for invalid MAC, it MUST generate `bad_record_mac` alert with level `fatal` and terminate connection state.

##### 4.1.2.2 Null or Standard Stream Cipher
- **[R15]**: RC4 MUST NOT be used with DTLS (cannot be randomly accessed).

##### 4.1.2.3 Block Cipher
- DTLS block cipher encryption/decryption is identical to TLS 1.1.

##### 4.1.2.4 New Cipher Suites
- **[R16]**: Upon registration, new TLS cipher suites MUST indicate whether they are suitable for DTLS usage and describe any adaptations.

##### 4.1.2.5 Anti-replay
- **[R17]**: Sequence number verification SHOULD be performed using a sliding window procedure (borrowed from RFC 2402).
- Receiver packet counter MUST be initialized to zero at session establishment.
- **[R18]**: Receiver MUST verify no duplicate sequence number within the session; SHOULD be the first check.
- **[R19]**: A minimum window size of 32 MUST be supported; window size of 64 is preferred and SHOULD be default.
- Receiver MAY choose a larger window size.
- MAC validation MUST succeed before updating the receive window.

### 4.2 The DTLS Handshake Protocol
Three principal changes:
1. Stateless cookie exchange for DoS.
2. Modified handshake header to handle loss, reordering, fragmentation.
3. Retransmission timers.

#### 4.2.1 Denial of Service Countermeasures
- **Cookie exchange**: Server MAY respond to ClientHello with HelloVerifyRequest containing a stateless cookie.
- **[R20]**: Client MUST retransmit ClientHello with the cookie added.
- **[R21]**: In the first ClientHello, cookie field is empty (zero length).
- **[R22]**: The HelloVerifyRequest message type is `hello_verify_request(3)`.
- **[R23]**: When responding to a HelloVerifyRequest, client MUST use same parameter values (version, random, session_id, cipher_suites, compression_method) as in original ClientHello.
- **[R24]**: Server SHOULD use those values to generate cookie; MUST use same version number as in ServerHello.
- **[R25]**: Upon receipt of ServerHello, client MUST verify that server version values match.
- **[R26]**: DTLS server SHOULD generate cookies verifiable without retaining per-client state (e.g., HMAC(Secret, Client-IP, Client-Parameters)).
- **[R27]**: DTLS servers SHOULD perform a cookie exchange whenever a new handshake is performed. Default SHOULD be to perform exchange. MAY be configured not to if amplification not a problem.
- **[R28]**: Server MAY choose not to do cookie exchange for session resumption.
- **[R29]**: Clients MUST be prepared to do a cookie exchange with every handshake.
- If HelloVerifyRequest used, initial ClientHello and HelloVerifyRequest are not included in Finished MAC.

#### 4.2.2 Handshake Message Format
- Modified header (new fields bold):
  ```c
  struct {
    HandshakeType msg_type;
    uint24 length;
    uint16 message_seq;           // New
    uint24 fragment_offset;       // New
    uint24 fragment_length;       // New
    select (HandshakeType) { ... } body;
  } Handshake;
  ```
- First message each side sends in each handshake has `message_seq = 0`.
- Each new message increments `message_seq` by one; retransmitted messages reuse same `message_seq`.
- Implementations maintain `next_receive_seq` counter; initialized to zero.
- **[R30]**: If received message sequence number < `next_receive_seq`, message MUST be discarded.
- **[R31]**: If sequence number > `next_receive_seq`, implementation SHOULD queue the message (MAY discard as space tradeoff).
- When sequence matches `next_receive_seq`, counter incremented and message processed.

#### 4.2.3 Message Fragmentation and Reassembly
- **[R32]**: Sender divides large handshake message into contiguous ranges not larger than maximum handshake fragment size; ranges MUST NOT overlap.
- **[R33]**: Each fragment uses same `message_seq` as original; `fragment_offset` and `fragment_length` identify the fragment; `length` field remains original message length.
- **[R34]**: Receiver MUST buffer fragments until entire handshake message is available.
- **[R35]**: DTLS implementations MUST be able to handle overlapping fragment ranges (to allow retransmission with smaller fragment sizes).
- Multiple handshake messages may be placed in same DTLS record if they are part of the same flight.

#### 4.2.4 Timeout and Retransmission
- DTLS uses a state machine with states: PREPARING, SENDING, WAITING, FINISHED.
- Clients start in PREPARING, servers in WAITING with empty buffers and no timer.
- Transition rules:
  - PREPARING → SENDING: after buffering next flight.
  - SENDING → WAITING: after sending, set retransmit timer.
  - SENDING → FINISHED: if this is last flight (no more messages expected).
  - WAITING → SENDING: on timer expiry or receipt of a retransmitted flight from peer (resend flight and reset timer).
  - WAITING → PREPARING: when next flight (not final) is received.
  - WAITING → FINISHED: when final flight is received.
  - FINISHED → PREPARING: when server wants rehandshake (sends HelloRequest) or client receives HelloRequest.
- Partial reads (partial messages or only some messages in flight) do not cause state transitions or timer resets.

##### 4.2.4.1 Timer Values
- **[R36]**: Implementations SHOULD use initial timer value of 1 second (minimum from RFC 2988) and double value at each retransmission, up to no less than RFC 2988 maximum of 60 seconds.
- **[R37]**: Implementations SHOULD retain current timer value until a transmission without loss occurs, then may reset to initial value.
- **[R38]**: After long idleness (≥ 10× current timer value), implementations may reset timer to initial value.

#### 4.2.5 ChangeCipherSpec
- ChangeCipherSpec MUST be treated as part of the same flight as its associated Finished message for timeout/retransmission.

#### 4.2.6 Finished Messages
- Finished MAC MUST be computed as if each handshake message had been sent as a single fragment.
- Initial ClientHello and HelloVerifyRequest (if cookie exchange used) MUST NOT be included in Finished MAC.

#### 4.2.7 Alert Messages
- Alert messages are NOT retransmitted even during handshake.
- **[R39]**: DTLS implementation SHOULD generate a new alert if offending record is received again (e.g., retransmitted handshake message).
- **[R40]**: Implementations SHOULD detect persistent bad messages and terminate local connection state.

### 4.3 Summary of new syntax (Informative - provided in full but condensed here)
- Record Layer structs (DTLSPlaintext, DTLSCompressed, DTLSCiphertext) as shown in 4.1.
- HandshakeType enum adds `hello_verify_request(3)`.
- Handshake struct adds fields as shown in 4.2.2.
- ClientHello adds cookie field.
- HelloVerifyRequest structure defined.

## Requirements Summary
| ID  | Requirement Summary | Normative Level | Reference |
|-----|-------------------|----------------|-----------|
| R1  | Each DTLS record MUST fit within a single datagram. | MUST | 4.1.1 |
| R2  | Implementations SHOULD determine MTU and send records smaller than MTU. | SHOULD | 4.1.1 |
| R3  | Implementations SHOULD provide way for applications to determine PMTU. | SHOULD | 4.1.1 |
| R4  | If application sends record > MTU, implementation SHOULD generate error. | SHOULD | 4.1.1 |
| R5  | PMTU SHOULD be initialized from interface MTU. | SHOULD | 4.1.1.1 |
| R6  | On ICMP Datagram Too Big, decrease PMTU estimate. | should (recommended) | 4.1.1.1 |
| R7  | Implementation SHOULD allow application to reset PMTU estimate. | SHOULD | 4.1.1.1 |
| R8  | Implementation SHOULD allow applications to control DF bit. | SHOULD | 4.1.1.1 |
| R9  | For IPv6, RFC 1981 procedures SHOULD be followed. | SHOULD | 4.1.1.1 |
| R10 | Handshake messages should be sent with DF set. | should | 4.1.1.1 |
| R11 | Implementations SHOULD back off handshake packet size during retransmit backoff. | SHOULD | 4.1.1.1 |
| R12 | MAC errors MAY discard offending record and continue. | MAY | 4.1.2.1 |
| R13 | Implementations SHOULD silently discard data with bad MACs. | SHOULD | 4.1.2.1 |
| R14 | If alert for invalid MAC, MUST use bad_record_mac with level fatal and terminate. | MUST | 4.1.2.1 |
| R15 | RC4 MUST NOT be used with DTLS. | MUST NOT | 4.1.2.2 |
| R16 | New cipher suites MUST indicate suitability for DTLS. | MUST | 4.1.2.4 |
| R17 | Sequence number verification SHOULD use sliding window. | SHOULD | 4.1.2.5 |
| R18 | Receiver MUST verify no duplicate sequence number; SHOULD be first check. | MUST/SHOULD | 4.1.2.5 |
| R19 | Minimum window size of 32 MUST be supported; 64 is preferred and SHOULD be default. | MUST/SHOULD | 4.1.2.5 |
| R20 | Client MUST retransmit ClientHello with cookie when receiving HelloVerifyRequest. | MUST | 4.2.1 |
| R21 | First ClientHello cookie field empty. | (implied) | 4.2.1 |
| R22 | HelloVerifyRequest message type is hello_verify_request(3). | - | 4.2.1 |
| R23 | Client MUST use same parameters in retransmitted ClientHello. | MUST | 4.2.1 |
| R24 | Server SHOULD use those parameters for cookie; MUST use same version as ServerHello. | SHOULD/MUST | 4.2.1 |
| R25 | Client MUST verify server version values match upon ServerHello. | MUST | 4.2.1 |
| R26 | Server SHOULD generate cookies without retaining per-client state. | SHOULD | 4.2.1 |
| R27 | Servers SHOULD perform cookie exchange for new handshakes; default exchange SHOULD be performed. | SHOULD | 4.2.1 |
| R28 | Server MAY choose not to do cookie exchange for session resumption. | MAY | 4.2.1 |
| R29 | Clients MUST be prepared to do cookie exchange with every handshake. | MUST | 4.2.1 |
| R30 | If received sequence number < next_receive_seq, message MUST be discarded. | MUST | 4.2.2 |
| R31 | If sequence number > next_receive_seq, implementation SHOULD queue message. | SHOULD | 4.2.2 |
| R32 | Sender divides large handshake message into contiguous non-overlapping ranges. | MUST (implied) | 4.2.3 |
| R33 | Fragments use same message_seq, proper offset/length. | (implied) | 4.2.3 |
| R34 | Receiver MUST buffer fragments until complete message. | MUST | 4.2.3 |
| R35 | Implementations MUST handle overlapping fragment ranges. | MUST | 4.2.3 |
| R36 | Initial timer value SHOULD be 1 second, double each retransmission up to 60s. | SHOULD | 4.2.4.1 |
| R37 | Implementations SHOULD retain timer value until loss-free transmission. | SHOULD | 4.2.4.1 |
| R38 | After long idleness, may reset timer to initial. | MAY | 4.2.4.1 |
| R39 | Implementation SHOULD generate new alert if offending record received again. | SHOULD | 4.2.7 |
| R40 | Implementation SHOULD detect persistent bad messages and terminate connection. | SHOULD | 4.2.7 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 5)**: Most considerations are same as TLS 1.1 (Appendices D,E,F). Primary additional concern is denial of service; cookie exchange recommended. Servers not using cookie exchange may be used as amplifiers. Clients MUST be prepared for cookie exchange.
- **Acknowledgements (Section 6)**: Thanks to various contributors.
- **IANA Considerations (Section 7)**: No new registries; new handshake message type `hello_verify_request(3)` assigned from TLS HandshakeType registry.