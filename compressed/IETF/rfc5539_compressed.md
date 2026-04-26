# RFC 5539: NETCONF over Transport Layer Security (TLS)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2009 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc5539/

## Scope (Summary)
This document defines how to secure NETCONF [RFC4741] exchanges using TLS [RFC5246], providing certificate-based mutual authentication, integrity, confidentiality, and reliable sequenced data delivery. It specifies connection initiation, closure, endpoint identification, and security considerations for NETCONF over TLS.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC4741] Enns, R., "NETCONF Configuration Protocol", RFC 4741, December 2006.
- [RFC4742] Wasserman, M. and T. Goddard, "Using the NETCONF Configuration Protocol over Secure SHell (SSH)", RFC 4742, December 2006.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5280] Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.

## Definitions and Abbreviations
- **TLS**: Transport Layer Security protocol [RFC5246].
- **NETCONF**: Network Configuration Protocol [RFC4741].
- **Client/Server**: The two ends of the TLS connection. The client actively opens the TLS connection; the server passively listens.
- **Manager/Agent**: The two ends of the NETCONF session. The manager issues RPC commands; the agent replies. When using this mapping, the client is always the manager and the server is always the agent.
- **Delimiter sequence**: The character sequence "]]>]]>" as defined in [RFC4742].

## 1. Introduction (Informative Content Condensed)
NETCONF requires a persistent connection with integrity, confidentiality, peer authentication, and reliable data delivery. This document defines a mapping of NETCONF over TLS using certificate-based mutual authentication and key derivation, leveraging TLS ciphersuite negotiation and capabilities. The client (manager) opens the TLS connection; the server (agent) listens.

## 1.1. Conventions Used
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119.

## 2. NETCONF over TLS
NETCONF operates transparently on top of TLS. Defines how NETCONF is used within a TLS session.

### 2.1. Connection Initiation
- The NETCONF manager MUST act as the TLS client.
- It MUST connect to the server passively listening on TCP port 6513.
- It MUST send TLS ClientHello to begin the TLS handshake.
- After handshake, client and server MAY exchange NETCONF data: client sends complete XML documents containing `<rpc>` elements; server responds with `<rpc-reply>` elements.
- Client MAY create event notification subscriptions [RFC5277]; server replies and may send notifications.
- All NETCONF messages MUST be sent as TLS "application data". Multiple messages may be in one TLS record; a message may span multiple records.
- The delimiter sequence "]]>]]>" (from RFC4742) MUST be sent after each XML document by both peers.
- Implementations MUST ensure this sequence never appears inside a NETCONF message (including attributes, comments, processing instructions).
- Implementation MAY implement any TLS ciphersuite providing certificate-based mutual authentication [RFC5246].
- Server MUST support certificate-based client authentication.
- Implementations MUST support TLS 1.2 [RFC5246] and MUST support the mandatory-to-implement ciphersuite TLS_RSA_WITH_AES_128_CBC_SHA.
- If future TLS versions apply, the mandatory-to-implement ciphersuite for that version MUST be supported.

### 2.2. Connection Closure
- TLS client (NETCONF manager) MUST close the TLS connection if no further RPC commands are expected.
- It MUST send a TLS close_notify alert before closing.
- The client MAY choose not to wait for the server's close_notify, generating an incomplete close.
- Once the TLS server receives a close_notify from the client, it MUST reply with a close_notify unless it is aware the connection is already closed (e.g., by TCP).
- A NETCONF peer MAY close the connection after a long idle period.
- The peer MUST attempt to exchange close_notify alerts before closing; the sender unprepared to receive more data MAY close after sending close_notify, generating an incomplete close.

## 3. Endpoint Authentication and Identification

### 3.1. Server Identity
- During TLS negotiation, the client MUST examine the server certificate to determine if it meets expectations.
- MUST check the server hostname against the server's identity in the certificate to prevent man-in-the-middle attacks.
- Matching rules:
  - Client MUST use the hostname it used to open the connection (or the TLS "server_name" extension). Must NOT use insecure remote sources (e.g., insecure DNS). CNAME canonicalization is not done.
  - If subjectAltName of type dNSName exists, it MUST be used as the source of server identity.
  - Matching is case-insensitive.
  - A "*" wildcard MAY be used as the leftmost name component (e.g., *.example.com matches a.example.com, but not example.com).
  - If multiple names exist, a match with any is acceptable.
- If match fails, client MUST either ask for explicit user confirmation or terminate the connection and indicate identity suspect.
- Clients MUST verify the binding between server identity and public key. SHOULD implement RFC 5280 Section 6 algorithm, MAY supplement with equivalent methods.
- If client has external information on expected server identity, hostname check MAY be omitted.

### 3.2. Client Identity
- The server MUST verify client identity using certificate-based authentication according to local policy before any configuration or state data is exchanged.

## 4. Security Considerations (condensed informative)
- Security considerations from [RFC5246] and [RFC4741] apply.
- Third-party authentication (e.g., AAA) is not supported in this version; BEEP or SSH may be used if needed.
- Implementations MUST ensure the delimiter sequence never appears in NETCONF messages to prevent DoS attacks. Sender should warn if found; receiver must silently discard the message and stop the session.
- No new security issues beyond [RFC4742].

## 5. IANA Considerations
- IANA assigned TCP port 6513 with name "netconf-tls" for NETCONF over TLS (reference: RFC 5539). Details provided.

## 6. Acknowledgements (informative - condensed)
- Text derived in part from RFC 4642. Thanks to multiple reviewers and working group members.

## 7. Contributor's Address (informative - omitted per rules as non-normative)

## 8. References (listed in Normative and Informative sections above)

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | NETCONF manager MUST act as TLS client. | MUST | Section 2.1 |
| R2 | Client MUST connect to server on TCP port 6513. | MUST | Section 2.1 |
| R3 | Client MUST send TLS ClientHello. | MUST | Section 2.1 |
| R4 | After handshake, client and server MAY exchange NETCONF data. | MAY | Section 2.1 |
| R5 | Client MAY create event notification subscriptions. | MAY | Section 2.1 |
| R6 | All NETCONF messages MUST be sent as TLS application data. | MUST | Section 2.1 |
| R7 | Delimiter sequence "]]>]]>" MUST be sent after each XML document. | MUST | Section 2.1 |
| R8 | Implementations MUST ensure delimiter never appears in NETCONF messages. | MUST | Section 2.1 |
| R9 | Implementation MAY implement any TLS ciphersuite with certificate-based mutual auth. | MAY | Section 2.1 |
| R10 | Server MUST support certificate-based client authentication. | MUST | Section 2.1 |
| R11 | Implementations MUST support TLS 1.2 and mandatory ciphersuite (TLS_RSA_WITH_AES_128_CBC_SHA). | MUST | Section 2.1 |
| R12 | For future TLS versions, mandatory ciphersuite for that version MUST be supported. | MUST | Section 2.1 |
| R13 | TLS client MUST close connection if no further RPC commands expected. | MUST | Section 2.2 |
| R14 | Client MUST send close_notify before closing. | MUST | Section 2.2 |
| R15 | Server receiving close_notify MUST reply unless connection already closed. | MUST | Section 2.2 |
| R16 | NETCONF peer MAY close connection after idle time. | MAY | Section 2.2 |
| R17 | Peer MUST attempt close_notify exchange before closing. | MUST | Section 2.2 |
| R18 | Sender unprepared to receive more data MAY close after sending close_notify. | MAY | Section 2.2 |
| R19 | Client MUST examine server certificate for hostname match. | MUST | Section 3.1 |
| R20 | If subjectAltName dNSName present, MUST be used for identity. | MUST | Section 3.1 |
| R21 | Matching is case-insensitive. | MUST (implicit) | Section 3.1 |
| R22 | Wildcard "*" MAY be used as leftmost component. | MAY | Section 3.1 |
| R23 | If multiple names, any match acceptable. | MUST (implicit) | Section 3.1 |
| R24 | On match failure, client MUST ask user confirmation or terminate. | MUST | Section 3.1 |
| R25 | Clients MUST verify binding between server identity and public key. | MUST | Section 3.1 |
| R26 | Clients SHOULD implement RFC 5280 Section 6 algorithm; MAY supplement. | SHOULD/MAY | Section 3.1 |
| R27 | Hostname check MAY be omitted if external info on expected identity exists. | MAY | Section 3.1 |
| R28 | Server MUST verify client identity with certificate-based authentication per local policy before exchanging data. | MUST | Section 3.2 |
| R29 | Implementations MUST ensure delimiter sequence never appears in messages; receiver must discard and stop session. | MUST | Section 4 |

## Informative Annexes (Condensed)
- **Annex A (not present)**: N/A