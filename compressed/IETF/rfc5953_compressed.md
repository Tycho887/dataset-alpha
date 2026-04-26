# RFC 5953: Transport Layer Security (TLS) Transport Model for the Simple Network Management Protocol (SNMP)
**Source**: IETF | **Version**: Standards Track | **Date**: August 2010 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/info/rfc5953

## Scope (Summary)
Defines the TLS Transport Model (TLSTM) for SNMP, using TLS/TCP and DTLS/UDP to provide authentication, integrity, and privacy. Specifies how TLSTM integrates into the Transport Subsystem, elements of procedure, and a MIB module for management.

## Normative References
- RFC 2119 (Key words)
- RFC 2578, RFC 2579, RFC 2580 (SMIv2)
- RFC 3411, RFC 3413, RFC 3414, RFC 3415, RFC 3418 (SNMPv3 Framework)
- RFC 3490 (IDNA)
- RFC 3584 (Coexistence)
- RFC 4347 (DTLS)
- RFC 4366 (TLS Extensions)
- RFC 5246 (TLS 1.2)
- RFC 5280 (X.509 PKI)
- RFC 5590 (Transport Subsystem)
- RFC 5591 (Transport Security Model)
- RFC 5952 (IPv6 Text Representation)

## Definitions and Abbreviations
- **(D)TLS**: Both TLS and DTLS protocols, referred to collectively when no distinction is needed.
- **TLSTM**: TLS Transport Model defined in this document.
- **tmSecurityName**: Human-readable name representing the authenticated identity for a session; MUST be constant during a TLSTM session.
- **tmSessionID / tlstmSessionID**: Unique session identifier for a (D)TLS connection; MUST not change during the session.
- **tmStateReference**: Cache for transport-specific state, passed between Dispatcher and Transport Model.
- **Session**: Secure association between two TLSTM instances permitting transmission of one or more SNMP messages.
- **Principal**: The “who” on whose behalf processing takes place.
- **Client/Server**: Client actively opens (D)TLS connection; server passively listens.
- **SnmpTLSAddress**: Textual convention for IPv4/IPv6/hostname and port.
- **SnmpTLSFingerprint**: OCTET STRING containing a hash algorithm identifier (from IANA TLS HashAlgorithm) followed by the fingerprint value.

## Normative Requirements

### 1. General
- **(1.1)** The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in RFC 2119.

### 3. How the TLSTM Fits into the Transport Subsystem
- **(3.1.1)** TLSTM MUST support authentication of both server and client (X.509 certificates).
- **(3.1.1)** TLSTM MUST support message encryption (privacy).
- **(3.1.2)** When an application requests a security level, the TLSTM MUST ensure the (D)TLS connection provides security at least as high as requested. NULL integrity and encryption algorithms MUST NOT be used for authentication or privacy.
- **(3.1.3)** Each unique combination of transportDomain, transportAddress, tmSecurityName, and requestedSecurityLevel MUST have a locally chosen unique tlstmSessionID for each active session.
- **(3.1.3)** tlstmSessionID MUST NOT change during the entire session and MUST uniquely identify a single session.

### 4. Elements of the Model
- **(4.1)** TLSTM implementations are REQUIRED to support X.509 certificates.
- **(4.1.1)** Trusted public keys (CA or self-signed) MUST be installed via a trusted out-of-band mechanism, and their authenticity MUST be verified before access is granted.
- **(4.1.1)** Deployments SHOULD map the “subjectAltName” component of X.509 certificates to tmSecurityNames.
- **(4.2)** (D)TLS MUST negotiate a cipher_suite that uses X.509 certificates for authentication, and MUST authenticate both client and server.
- **(4.2)** TLS renegotiation with different certificates MUST NOT be done. Implementations MUST either disable renegotiation completely (RECOMMENDED) or present the same certificate during renegotiation (and verify the other end did the same).
- **(4.2)** For DTLS over UDP, each SNMP message MUST be placed in a single UDP datagram; it MAY be split to multiple DTLS records.
- **(4.2)** The DTLS server implementation MUST support DTLS cookies; enabling by default is RECOMMENDED.
- **(4.2)** For DTLS, replay protection MUST be used.

### 5. Elements of Procedure
- **(5.1.1)** Demultiplexing of incoming packets into separate DTLS sessions MUST be implemented.
- **(5.1.1)** When establishing a new DTLS session, implementations MUST use a different UDP source port number for each active connection to a remote IP/port combination.
- **(5.1.2)** tlstmSessionID MUST be unique for the (D)TLS connection and MUST NOT be reused until all references are released.
- **(5.1.2)** The procedures in Section 5.3.2 MUST be performed before continuing beyond step 1.
- **(5.2)** If tmStateReference does not contain required values, increment snmpTlstmSessionInvalidCaches, discard message, return error.
- **(5.2)** If tmSameSecurity is true and tmSessionID is undefined or session closed, increment snmpTlstmSessionNoSessions, discard message, return error.
- **(5.2)** If tmSameSecurity is false and tmSessionID refers to a closed session, implementation SHOULD open a new session.
- **(5.3.1)** The client selects the appropriate certificate and cipher_suites based on tmSecurityName and tmRequestedSecurityLevel. The security capabilities provided by (D)TLS MUST be at least as high as tmRequestedSecurityLevel.
- **(5.3.1)** The (D)TLS client MUST verify the server’s presented certificate. The client MUST NOT transmit SNMP messages until the server certificate is authenticated and the TLS connection is fully established.
- **(5.3.1)** If verification fails, session establishment MUST fail, snmpTlstmSessionInvalidServerCertificates incremented.
- **(5.3.2)** The (D)TLS server MUST request and expect a certificate from the client and MUST NOT accept SNMP messages until the client certificate is authenticated.
- **(5.3.2)** If any verification fails, session establishment MUST fail, snmpTlstmSessionInvalidClientCertificates incremented.
- **(5.4)** Closing a session MUST include sending a close_notify TLS Alert.

### 6. MIB Module
- **(6.1)** MIB module provides textual conventions, statistical counters, notifications, and configuration tables.
- **(6.2)** Defines SnmpTLSAddress and SnmpTLSFingerprint textual conventions.
- **(6.4)** Configuration tables extend SNMP-TARGET-MIB for (D)TLS certificate usage, and a mapping table for incoming client certificates to tmSecurityNames.
- **(6.4.1)** Notifications defined: snmpTlstmServerCertificateUnknown, snmpTlstmServerInvalidCertificate.

### 7. MIB Module Definition
- The full ASN.1 definition is provided. Key objects:
  - **snmpTLSTCPDomain** (OID snmpDomains 8) and **snmpDTLSUDPDomain** (snmpDomains 9).
  - **SnmpTLSAddress** syntax: OCTET STRING (1..255) – IPv4/IPv6/hostname + port.
  - **SnmpTLSFingerprint** syntax: OCTET STRING (0..255) – hash algorithm ID + fingerprint.
  - **snmpTlstmCertToTSNTable**: Mapping table from certificate to tmSecurityName. Rows prioritized by snmpTlstmCertToTSNID. Matching rules: fingerprint match to presented certificate or to a trusted CA certificate used in path validation. If no valid match, connection MUST be closed and SNMP messages MUST NOT be accepted.
  - **snmpTlstmParamsTable**: Extends snmpTargetParamsTable with a client certificate fingerprint.
  - **snmpTlstmAddrTable**: Extends snmpTargetAddrTable with server certificate fingerprint or identity for verification. Verification MUST be performed as described.

### 8. Operational Considerations
- **(8.1)** Implementations SHOULD provide graceful session termination and SHOULD detect “broken” sessions.
- **(8.2)** Servers that support multiple principals at a port SHOULD use Server Name Indication (RFC 4366).
- **(8.3)** Implementations are RECOMMENDED to support contextEngineID discovery (RFC 5343).

### 9. Security Considerations
- **(9.1)** Access control MUST be enforced by an access control subsystem (e.g., VACM). Both ends MUST check the presented certificate.
- **(9.1)** The instructions in the DESCRIPTION clause of snmpTlstmCertToTSNTable MUST be followed exactly.
- **(9.2.1)** TLSTM clients and servers MUST NOT use SSL 2.0.
- **(9.2.2)** Use of Perfect Forward Secrecy is RECOMMENDED.
- **(9.3)** It is RECOMMENDED that only SNMPv3 messages using TSM be sent over TLSTM. Using non-transport-aware Security Models is NOT RECOMMENDED.
- **(9.4)** The MIB module objects with MAX-ACCESS read-write/read-create are sensitive; SET operations require proper authentication and encryption. Access control (SNMPv3 with crypto) is RECOMMENDED.

### 10. IANA Considerations
- Assigned port numbers: snmptls (10161/tcp), snmpdtls (10161/udp), snmptls-trap (10162/tcp), snmpdtls-trap (10162/udp).
- Assigned SMI numbers under snmpDomains (8,9) and mib-2 (198).
- Registry prefixes: “tls” for snmpTLSTCPDomain, “dtls” for snmpDTLSUDPDomain.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | TLSTM MUST support authentication of both server and client via X.509 certificates. | shall | 3.1.1 |
| R2 | TLSTM MUST support message encryption. | shall | 3.1.1 |
| R3 | The (D)TLS connection MUST provide security at least as high as the requested security level. NULL integrity/encryption algorithms MUST NOT be used for auth or privacy. | shall | 3.1.2 |
| R4 | Each unique combination of transportDomain, transportAddress, tmSecurityName, and requestedSecurityLevel MUST have a unique tlstmSessionID. | shall | 3.1.3 |
| R5 | tlstmSessionID MUST NOT change during the session and MUST uniquely identify a single session. | shall | 3.1.3 |
| R6 | Implementations MUST support X.509 certificates. | shall | 4.1 |
| R7 | Trusted public keys MUST be installed via a trusted out-of-band mechanism and verified before access. | shall | 4.1.1 |
| R8 | (D)TLS MUST negotiate a cipher_suite using X.509 certificates and MUST authenticate both sides. | shall | 4.2 |
| R9 | TLS renegotiation with different certificates MUST NOT be done (disable renegotiation or use same cert). | shall | 4.2 |
| R10 | For DTLS over UDP, each SNMP message MUST be in a single UDP datagram. | shall | 4.2 |
| R11 | DTLS server MUST support DTLS cookies; enabling by default RECOMMENDED. | shall (MUST) | 4.2 |
| R12 | DTLS replay protection MUST be used. | shall | 4.2 |
| R13 | Demultiplexing of incoming DTLS packets MUST be implemented (either in DTLS or TLSTM). | shall | 5.1.1 |
| R14 | For DTLS, use different UDP source port per active connection to same remote IP/port. | shall | 5.1.1 |
| R15 | tlstmSessionID MUST be unique and not reused until all references released. | shall | 5.1.2 |
| R16 | Procedures in Section 5.3.2 MUST be performed before continuing in 5.1.2. | shall | 5.1.2 |
| R17 | If tmStateReference is invalid, increment snmpTlstmSessionInvalidCaches, discard message, return error. | shall | 5.2 |
| R18 | If tmSameSecurity true and no valid session, increment snmpTlstmSessionNoSessions, discard, return error. | shall | 5.2 |
| R19 | Client MUST verify server certificate before transmitting SNMP messages. | shall | 5.3.1 |
| R20 | Session establishment MUST fail if verification fails. | shall | 5.3.1/5.3.2 |
| R21 | Server MUST request and expect client certificate; MUST NOT accept SNMP messages until authenticated. | shall | 5.3.2 |
| R22 | Closing session MUST include close_notify alert. | shall | 5.4 |
| R23 | snmpTlstmCertToTSNTable mapping rules: if no valid match, connection MUST be closed. | shall | 7 |
| R24 | TLSTM MUST NOT use SSL 2.0. | shall | 9.2.1 |

## Informative Annexes (Condensed)
- **Appendix A. Target and Notification Configuration Example**: Provides example MIB rows for configuring notification originator, simple tmSecurityName derivation using subjectAltName (snmpTlstmCertSANAny), and table-driven mapping (snmpTlstmCertSpecified). These illustrate typical deployment procedures but are non-normative.