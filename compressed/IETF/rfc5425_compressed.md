# RFC 5425: Transport Layer Security (TLS) Transport Mapping for Syslog
**Source**: IETF (Internet Engineering Task Force) | **Version**: Standards Track | **Date**: March 2009 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc5425

## Scope (Summary)
This document specifies the use of Transport Layer Security (TLS) to provide a secure connection for transporting syslog messages. It defines protocol elements, port assignment, authentication methods, and security policies to counter masquerade, modification, and disclosure threats.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [RFC5424] Gerhards, R., "The Syslog Protocol", RFC 5424, March 2009.

## Definitions and Abbreviations
- **Originator**: entity generating syslog content to be carried in a message.
- **Collector**: entity gathering syslog content for further analysis.
- **Relay**: entity forwarding messages from originators or other relays to collectors or other relays.
- **Transport Sender**: entity passing syslog messages to a specific transport protocol.
- **Transport Receiver**: entity taking syslog messages from a specific transport protocol.
- **TLS Client**: application that can initiate a TLS connection by sending a Client Hello to a server.
- **TLS Server**: application that can receive a Client Hello from a client and reply with a Server Hello.
- The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

## 1. Introduction
This document describes the use of TLS [RFC5246] to provide a secure connection for the transport of syslog [RFC5424] messages. It describes security threats to syslog and how TLS can be used to counter such threats.

## 2. Security Requirements for Syslog (Condensed)
Syslog messages may traverse untrusted networks. Primary threats: Masquerade (unauthorized sender/receiver), Modification (in-transit message alteration), Disclosure (unauthorized reading). Secondary threat: Message stream modification (deletion, replay, reordering) – not addressed by this transport. Threats considered of lesser importance and not addressed: Denial of Service, Traffic Analysis.

## 3. Using TLS to Secure Syslog (Condensed)
TLS provides confidentiality (to counter disclosure), integrity-checking (hop-by-hop against modification), and server/mutual authentication (to counter masquerade). Note: TLS secures transport hop-by-hop only and does not authenticate syslog message origin; when needed, use signed syslog [SYS-SIGN].

## 4. Protocol Elements

### 4.1. Port Assignment
- A syslog transport sender is always a TLS client; a transport receiver is always a TLS server.
- **Default port**: TCP 6514 for syslog over TLS.

### 4.2. Initiation
- The transport sender **should** initiate a connection to the transport receiver and then send the TLS Client Hello to begin the handshake.
- When finished, the transport sender **MAY** send the first syslog message.
- **Implementations MUST support TLS 1.2 [RFC5246] and are REQUIRED to support the mandatory to implement cipher suite: TLS_RSA_WITH_AES_128_CBC_SHA.** This document applies to future TLS versions; then the mandatory cipher suite of that version **MUST** be supported.

#### 4.2.1. Certificate-Based Authentication
- Both syslog transport sender (TLS client) and receiver (TLS server) **MUST implement certificate-based authentication**. This consists of validating the certificate and verifying that the peer has the corresponding private key (performed by TLS).
- The following methods for certificate validation **SHALL** be implemented:
  - **Certification path validation**: Configured with trust anchors (root CA certificates) per [RFC5280]. Useful with PKI.
  - **End-entity certificate matching**: Configured with information to identify valid end-entity certificates of authorized peers (can be self-signed). **Implementations MUST support certificate fingerprints (Section 4.2.2) and MAY allow other formats (e.g., DER-encoded certificate)**.
- Both transport receiver and sender **MUST provide means to generate a key pair and self-signed certificate** if not available otherwise.
- Both **SHOULD provide mechanisms to record the end-entity certificate** for correlating with sent/received data.

#### 4.2.2. Certificate Fingerprints
- Both client and server **MUST make the certificate fingerprints available through a management interface**. Algorithm labels from IANA "Hash Function Textual Names" [RFC4572].
- Fingerprint generation: hash of DER-encoded certificate using a cryptographically strong algorithm, converted to colon-separated uppercase hex bytes, prepended with hash function label and colon.
- **Implementations MUST support SHA-1 as the hash algorithm and use the ASCII label "sha-1"**.
- Example: `sha-1:E1:2D:53:2B:7C:6B:8A:29:A2:76:C8:64:36:0B:08:4B:7A:F1:9E:9D`
- During validation, the hash from the fingerprint is compared against the hash of the received certificate.

#### 4.2.3. Cryptographic Level
- Syslog applications **SHOULD** be implemented to permit administrators to select cryptographic level and authentication options as a matter of local policy.
- Session resumption: security parameters of resumed session **SHOULD** be checked against the requested session’s requirements.

### 4.3. Sending Data
- **All syslog messages MUST be sent as TLS "application data".**
- Application data is defined with ABNF (see text). Message length is the octet count of the SYSLOG-MSG in the SYSLOG-FRAME.
- **A transport receiver MUST use the message length to delimit a syslog message.**
- **MUST be able to process messages with length up to and including 2048 octets.** Transport receivers **SHOULD** be able to process messages with lengths up to and including 8192 octets.

### 4.4. Closure
- **A transport sender MUST close the associated TLS connection if no more syslog messages are expected.**
- **MUST send a TLS close_notify alert before closing the connection.**
- A transport sender (TLS client) **MAY** choose not to wait for the receiver’s close_notify and close connection (incomplete close).
- Once the transport receiver gets a close_notify from the sender, **it MUST reply with a close_notify** unless it knows the connection is already closed.
- When no data is received for a long time, a transport receiver **MAY** close the connection. The receiver (TLS server) **MUST attempt to initiate an exchange of close_notify alerts** with the sender before closing. Receivers unprepared for more data **MAY** close after sending close_notify (incomplete close).

## 5. Security Policies
- **If the peer does not meet the requirements of the security policy, the TLS handshake MUST be aborted with an appropriate TLS alert.**

### 5.1. End-Entity Certificate Based Authorization
- Configure with information to identify valid end-entity certificates of authorized peers.
- **Implementations MUST support specifying authorized peers using certificate fingerprints** (Sections 4.2.1 and 4.2.2).

### 5.2. Subject Name Authorization
- **Implementations MUST support certification path validation [RFC5280].**
- **MUST support specifying authorized peers using locally configured host names and matching the name against the certificate as follows:**
  - **MUST support matching the locally configured host name against a dNSName in the subjectAltName extension.**
  - **SHOULD support checking the name against the common name portion of the subject distinguished name.**
  - Wildcard '*' allowed as left-most DNS label in dNSName (and in common name if used). Matches any left-most label. e.g., *.example.com matches a.example.com and b.example.com but not example.com or a.b.example.com.
  - **Implementations MUST support wildcards in certificates as specified above, but MAY provide a configuration option to disable them.**
  - Locally configured names **MAY** contain wildcard characters; types may be more flexible than in subject names.
  - Internationalized domain names must be converted to ACE format for comparisons [RFC5280].
  - **Implementations MAY support matching a locally configured IP address against an iPAddress in subjectAltName** (converted to octet string per RFC5280).

### 5.3. Unauthenticated Transport Sender
- Transport receiver skips sender authentication (no client certificate request or accepts any certificate). Does not protect against sender masquerade. **Generally NOT RECOMMENDED.**

### 5.4. Unauthenticated Transport Receiver
- Transport sender skips receiver authentication. Does not protect against receiver masquerade, leaving data vulnerable to disclosure and modification. **Generally NOT RECOMMENDED.**

### 5.5. Unauthenticated Transport Receiver and Sender
- Both skip authentication. Does not protect against any threats. **NOT RECOMMENDED.**

## 6. Security Considerations
### 6.1. Authentication and Authorization Policies
- Threats are mitigated only if both transport sender and receiver are properly authenticated and authorized (Sections 5.1 and 5.2). **These are the RECOMMENDED configurations for a default policy.**
- If receiver does not authenticate sender: may accept data from attacker; increases vulnerability to denial of service, resource consumption; **NOT RECOMMENDED.**
- If sender does not authenticate receiver: may send sensitive data to attacker; data sent **SHOULD** be limited to non-valuable data (difficult in practice); **NOT RECOMMENDED.**
- Forgoing authentication on both sides allows man-in-the-middle, masquerade, etc.; **NOT RECOMMENDED.**

### 6.2. Name Validation
- The subject name should be locally configured; obtaining names through other means (e.g., DNS lookup) introduces vulnerabilities.

### 6.3. Reliability
- No application-layer acknowledgments. TCP retransmissions provide some protection, but if connection breaks, sender cannot always know which messages were successfully delivered.

## 7. IANA Considerations
- **Port**: TCP 6514 assigned in "Registered Port Numbers" with keyword "syslog-tls".

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Transport sender is TLS client; receiver is TLS server. | shall | Section 4.1 |
| R2 | Implementations MUST support TLS 1.2 and MUST support mandatory cipher suite TLS_RSA_WITH_AES_128_CBC_SHA. | shall | Section 4.2 |
| R3 | Both sender and receiver MUST implement certificate-based authentication. | shall | Section 4.2.1 |
| R4 | Both methods for certificate validation (certification path and end-entity matching) SHALL be implemented. | shall | Section 4.2.1 |
| R5 | Implementations MUST support certificate fingerprints (SHA-1). | must | Section 4.2.1, 4.2.2 |
| R6 | Both MUST provide means to generate key pair and self-signed certificate. | must | Section 4.2.1 |
| R7 | Both SHOULD provide mechanisms to record end-entity certificate. | should | Section 4.2.1 |
| R8 | Both client and server MUST make certificate fingerprints available via management interface. | must | Section 4.2.2 |
| R9 | Implementations MUST use SHA-1 as hash algorithm for fingerprints with label "sha-1". | must | Section 4.2.2 |
| R10 | All syslog messages MUST be sent as TLS application data. | must | Section 4.3 |
| R11 | Transport receiver MUST use message length to delimit syslog messages. | must | Section 4.3.1 |
| R12 | Transport receiver MUST be able to process messages up to 2048 octets; SHOULD up to 8192 octets. | must/should | Section 4.3.1 |
| R13 | Transport sender MUST close TLS connection if no more messages expected, MUST send close_notify before closing. | must | Section 4.4 |
| R14 | Transport receiver receiving close_notify MUST reply with close_notify unless connection already closed. | must | Section 4.4 |
| R15 | Transport receiver closing after idle MUST attempt exchange of close_notify alerts. | must | Section 4.4 |
| R16 | If peer does not meet security policy, TLS handshake MUST be aborted with appropriate alert. | must | Section 5 |
| R17 | Implementations MUST support specifying authorized peers using certificate fingerprints. | must | Section 5.1 |
| R18 | MUST support certification path validation [RFC5280] and specifying authorized peers using locally configured host names with matching rules (dNSName, common name, wildcards). | must | Section 5.2 |
| R19 | MUST support wildcard '*' in dNSName as left-most label. | must | Section 5.2 |
| R20 | Locally configured names MAY contain wildcard; types may be flexible. | may | Section 5.2 |
| R21 | Internationalized domain names must be converted to ACE format. | must | Section 5.2 |
| R22 | Implementations MAY support matching IP address against iPAddress in subjectAltName. | may | Section 5.2 |
| R23 | Use of unauthenticated sender (Section 5.3) generally NOT RECOMMENDED. | not recommended | Section 5.3 |
| R24 | Use of unauthenticated receiver (Section 5.4) generally NOT RECOMMENDED. | not recommended | Section 5.4 |
| R25 | Unauthenticated both sides NOT RECOMMENDED. | not recommended | Section 5.5 |

## Informative Annexes (Condensed)
- **[Appendix - Security Threats]**: Primary threats (masquerade, modification, disclosure) and secondary threat (message stream modification) are described in Section 2. These are essential context for understanding the need for TLS.
- **[Appendix - Session Resumption]**: Permitted; security parameters **SHOULD** be checked against requested session requirements (Section 4.2.3).
- **[Informative References]**: [RFC4572] (hash function names) and [SYS-SIGN] (work in progress on signed syslog) are provided as background.