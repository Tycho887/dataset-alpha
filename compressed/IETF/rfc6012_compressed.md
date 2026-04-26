# RFC 6012: Datagram Transport Layer Security (DTLS) Transport Mapping for Syslog
**Source**: IETF | **Version**: Standards Track | **Date**: October 2010 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc6012

## Scope (Summary)
This document defines the transport of syslog messages over the Datagram Transport Layer Security (DTLS) protocol, providing secure connectionless transport over UDP and optionally over DCCP. It specifies protocol elements, security policies, congestion control, and IANA assignments.

## Normative References
- [RFC0768] User Datagram Protocol
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC4340] Datagram Congestion Control Protocol (DCCP)
- [RFC4347] Datagram Transport Layer Security (DTLS)
- [RFC5234] Augmented BNF for Syntax Specifications: ABNF
- [RFC5238] DTLS over DCCP
- [RFC5246] The Transport Layer Security (TLS) Protocol Version 1.2
- [RFC5280] Internet X.509 Public Key Infrastructure Certificate and CRL Profile
- [RFC5424] The Syslog Protocol
- [RFC5425] TLS Transport Mapping for Syslog
- [RFC5426] Transmission of Syslog Messages over UDP
- [RFC5746] TLS Renegotiation Indication Extension

## Definitions and Abbreviations
- **originator**: generates syslog content to be carried in a message (from [RFC5424]).
- **collector**: gathers syslog content for further analysis.
- **relay**: forwards messages, accepting from originators or other relays, sending to collectors or other relays.
- **transport sender**: passes syslog messages to a specific transport protocol.
- **transport receiver**: takes syslog messages from a specific transport protocol.
- **DTLS client**: application that can initiate a DTLS Client Hello to a server.
- **DTLS server**: application that can receive a DTLS Client Hello and reply with a Server Hello.
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL**: interpreted as per [RFC2119].

## 1. Introduction (Condensed)
This document defines syslog over DTLS over UDP and syslog over DTLS over DCCP. DTLS provides secure datagram transport. The syslog protocol [RFC5424] is designed to run over different transports.

## 2. Terminology
(Definitions as above in the Definitions section.)

## 3. Security Requirements for Syslog
The security requirements from Section 2 of [RFC5425] apply. Additionally, denial-of-service attacks via spoofed IP sources during DTLS handshake are considered.

## 4. Using DTLS to Secure Syslog
DTLS counters primary threats (confidentiality, integrity, authentication, replay, DoS) on a hop-by-hop basis. The authenticated identity of the transport sender is not necessarily related to the HOSTNAME field; for origin authentication, [RFC5848] may be used.

## 5. Protocol Elements
### 5.1. Transport
- Implementations **MUST** support DTLS over UDP, **SHOULD** support DTLS over DCCP [RFC5238].
- Session multiplexing is provided by address/port combination.
- DTLS records may be reordered; ordering is not assured over UDP.
- Syslog over DTLS over TCP **MUST NOT** be used; use [RFC5425] for TLS over TCP.

### 5.2. Port and Service Code Assignment
- Transport sender is always DTLS client; receiver is always DTLS server.
- Default port: UDP and DCCP port 6514 (syslog-tls).
- Service code SYLG (1398361159) assigned for DCCP.

### 5.3. Initiation
- Transport sender initiates DTLS connection by sending Client Hello.
- **MUST** support DTLS denial-of-service countermeasures (Hello Verify Request with cookie).
- Transport sender **MUST NOT** send syslog messages before DTLS handshake completes.
- **MUST** support DTLS 1.0 [RFC4347] and mandatory cipher suite TLS_RSA_WITH_AES_128_CBC_SHA [RFC5246].
- If additional cipher suites are supported, **MUST NOT** negotiate NULL integrity or authentication algorithms.
- Where privacy is **REQUIRED**, cipher suite with non-NULL encryption **must** be negotiated; otherwise, NULL encryption may be advantageous (see [RFC5424] Section 8).

#### 5.3.1. Certificate-Based Authentication
- Both transport sender (DTLS client) and receiver (DTLS server) **MUST** implement certificate-based authentication (validate certificate and verify private key possession via DTLS).
- Methods for certificate validation from Sections 4.2.1 and 4.2.2 of [RFC5425] **SHALL** be implemented.
- Both **MUST** provide means to generate a key pair and self-signed certificate.
- Both **SHOULD** provide mechanisms to record the certificate or fingerprint for correlation with data.

### 5.4. Sending Data
- All syslog messages **MUST** be sent as DTLS "application data".
- Multiple messages may be in one DTLS record, or one message in multiple records.
- ABNF for APPLICATION-DATA: `1*SYSLOG-FRAME`, where `SYSLOG-FRAME = MSG-LEN SP SYSLOG-MSG`, etc.

#### 5.4.1. Message Size
- Transport receiver **MUST** use message length to delimit syslog message.
- No upper limit per se, but DTLS record **MUST NOT** span multiple datagrams.
- For UDP: see [RFC5426] Section 3.2. For DCCP: implementer **SHOULD** determine max record size per [RFC4340].
- Message size **SHOULD NOT** exceed DTLS max record size (2^14 bytes).
- Transport receiver **MUST** process messages up to 2048 octets; **SHOULD** process up to 8192 octets.
- See Appendix A.2 of [RFC5424] for fragmentation guidance.

### 5.5. Closure
- Transport sender **MUST** close DTLS connection when no more messages expected; **MUST** send DTLS close_notify before closing.
- Transport sender (DTLS client) **MAY** not wait for receiver's close_notify.
- Transport receiver **MUST** reply with close_notify after receiving sender's close_notify.
- Transport receiver **MAY** close idle connection; **MUST** attempt to exchange close_notify alerts with sender before closing.
- Unprepared receivers **MAY** close after sending close_notify.
- Note: close_notify alerts are not retransmitted and may be lost.

## 6. Congestion Control
- Syslog over DTLS over DCCP is **RECOMMENDED** over UDP when available (DCCP provides congestion control).
- Implementations of sysover DCCP **MUST** support CCID 3; **SHOULD** support CCID 2.
- Congestion control considerations from Section 4.3 of [RFC5426] apply to syslog over DTLS over UDP.

## 7. Security Policies
- Security policies are the same as in [RFC5425]; all normative requirements of Section 5 of [RFC5425] apply.

## 8. IANA Considerations
- UDP and DCCP port 6514 assigned as syslog-tls for syslog over DTLS.
- DCCP service code SYLG (1398361159) assigned.

## 9. Security Considerations
- References: [RFC4347], [RFC5246], [RFC5425], [RFC5280].
- **9.1 DTLS Renegotiation**: **RECOMMENDED** to disable renegotiation; if allowed, [RFC5746] **MUST** be followed, and identity must not change during renegotiation.
- **9.2 Message Loss**: Transport is unreliable; loss possible. [RFC5424] recommends tls/tcp for lossless streams; signed syslog [RFC5848] can detect loss.
- **9.3 Private Key Generation**: Use adequate random number generators (see [RFC4086]).
- **9.4 Trust Anchor Installation and Storage**: Care required; fingerprint mechanism (Section 5.3.1) can verify correct installation. Trust anchor information must be securely stored.

## 10. Acknowledgements
Condensed: Thanks to Wes Hardaker, Pasi Eronen, David Harrington, Chris Lonvick, Eliot Lear, Anton Okmyanskiy, Juergen Schoenwaelder, Richard Graveman, syslog WG, and IESG for review and suggestions.

## 11. References
(Already listed in Normative References; Informative References: [RFC2914], [RFC4086], [RFC5405], [RFC5848].)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations **MUST** support DTLS over UDP | shall | Section 5.1 |
| R2 | Implementations **SHOULD** support DTLS over DCCP | should | Section 5.1 |
| R3 | Syslog over DTLS over TCP **MUST NOT** be used | shall | Section 5.1 |
| R4 | Transport sender **MUST** support DTLS DoS countermeasures | shall | Section 5.3 |
| R5 | Transport sender **MUST NOT** send syslog before DTLS handshake completes | shall | Section 5.3 |
| R6 | **MUST** support DTLS 1.0 and mandatory cipher suite TLS_RSA_WITH_AES_128_CBC_SHA | shall | Section 5.3 |
| R7 | If additional cipher suites are supported, **MUST NOT** negotiate NULL integrity/authentication | shall | Section 5.3 |
| R8 | Both sender and receiver **MUST** implement certificate-based authentication | shall | Section 5.3.1 |
| R9 | Certificate validation methods from [RFC5425] Sections 4.2.1-4.2.2 **SHALL** be implemented | shall | Section 5.3.1 |
| R10 | Both **MUST** provide means to generate key pair and self-signed certificate | shall | Section 5.3.1 |
| R11 | Both **SHOULD** record certificate/fingerprint for identity correlation | should | Section 5.3.1 |
| R12 | All syslog messages **MUST** be sent as DTLS application data | shall | Section 5.4 |
| R13 | Transport receiver **MUST** use message length to delimit syslog message | shall | Section 5.4.1 |
| R14 | DTLS record **MUST NOT** span multiple datagrams | shall | Section 5.4.1 |
| R15 | Message size **SHOULD NOT** exceed DTLS max record size (2^14 bytes) | should | Section 5.4.1 |
| R16 | Transport receiver **MUST** process messages up to 2048 octets | shall | Section 5.4.1 |
| R17 | Transport receiver **SHOULD** process messages up to 8192 octets | should | Section 5.4.1 |
| R18 | Transport sender **MUST** close DTLS connection and send close_notify when no more messages | shall | Section 5.5 |
| R19 | Transport receiver **MUST** reply with close_notify after receiving sender's close_notify | shall | Section 5.5 |
| R20 | Transport receiver **MUST** attempt to exchange close_notify alerts before closing idle connection | shall | Section 5.5 |
| R21 | Syslog over DTLS over DCCP is **RECOMMENDED** over UDP | should | Section 6 |
| R22 | Implementations over DCCP **MUST** support CCID 3; **SHOULD** support CCID 2 | shall/should | Section 6 |
| R23 | Security policies of [RFC5425] Section 5 apply | shall | Section 7 |
| R24 | If renegotiation allowed, [RFC5746] **MUST** be followed and identity unchanged | shall | Section 9.1 |
| R25 | **RECOMMENDED** to disable DTLS renegotiation | should | Section 9.1 |

## Informative Sections (Condensed)
- **Introduction**: Summarizes purpose: syslog over DTLS over UDP and DCCP.
- **Using DTLS**: Lists threats countered; hop-by-hop security; note on origin authentication.
- **Initiation DoS**: Describes cookie exchange; no new normative text.
- **Certificate generation**: Informative guidance on self-signed certificates.
- **Closure loss**: Alerts not retransmitted; informative.
- **Congestion Control**: Rationale for DCCP preference; informative guidance.
- **IANA Considerations**: Factual assignment of port and service code.
- **Security Considerations (9.2-9.4)**: Informative discussion on message loss, random number generation, trust anchor storage.
- **Acknowledgements**: List of contributors.