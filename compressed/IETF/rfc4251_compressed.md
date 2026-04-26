# RFC 4251: The Secure Shell (SSH) Protocol Architecture
**Source**: IETF | **Version**: Standards Track | **Date**: January 2006 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/html/rfc4251

## Scope (Summary)
This document describes the architecture of the SSH protocol, which provides secure remote login and other secure network services over an insecure network. It defines three major components: the Transport Layer Protocol, the User Authentication Protocol, and the Connection Protocol. It also specifies notation, data type representations, algorithm naming, message numbering, IANA considerations, and comprehensive security considerations.

## Normative References
- [SSH-TRANS] Ylonen, T. and C. Lonvick, Ed., "The Secure Shell (SSH) Transport Layer Protocol", RFC 4253, January 2006.
- [SSH-USERAUTH] Ylonen, T. and C. Lonvick, Ed., "The Secure Shell (SSH) Authentication Protocol", RFC 4252, January 2006.
- [SSH-CONNECT] Ylonen, T. and C. Lonvick, Ed., "The Secure Shell (SSH) Connection Protocol", RFC 4254, January 2006.
- [SSH-NUMBERS] Lehtinen, S. and C. Lonvick, Ed., "The Secure Shell (SSH) Protocol Assigned Numbers", RFC 4250, January 2006.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2434] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 2434, October 1998.
- [RFC3066] Alvestrand, H., "Tags for the Identification of Languages", BCP 47, RFC 3066, January 2001.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.

## Definitions and Abbreviations
- **byte**: An arbitrary 8-bit value (octet). Fixed-length data is written `byte[n]`.
- **boolean**: Stored as a single byte; 0 = FALSE, 1 = TRUE. Non-zero values interpreted as TRUE; applications MUST NOT store values other than 0 and 1.
- **uint32**: 32-bit unsigned integer in network byte order (4 bytes).
- **uint64**: 64-bit unsigned integer in network byte order (8 bytes).
- **string**: Arbitrary length binary string; stored as uint32 length followed by that many bytes. Used for text (US-ASCII for internal names, ISO-10646 UTF-8 for user-visible text).
- **mpint**: Multiple-precision integer in two's complement format, stored as a string (MSB first). Negative numbers have MSB of first byte set; positive numbers with MSB set must be preceded by a zero byte.
- **name-list**: A string containing a comma-separated list of names (each US-ASCII, non-empty, no comma). Terminating null character MUST NOT be used.
- **SSH**: Secure Shell.
- **PFS**: Perfect Forward Secrecy.

## Contributors
(Informative – see original document for full list.) Key contributors: Tatu Ylonen, Tero Kivinen, Timo J. Rinne, Sami Lehtinen, Markku-Juhani O. Saarinen, Darren Moffat, and many others.

## Conventions Used in This Document
- The keywords **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in [RFC2119].
- The keywords **PRIVATE USE**, **HIERARCHICAL ALLOCATION**, **FIRST COME FIRST SERVED**, **EXPERT REVIEW**, **SPECIFICATION REQUIRED**, **IESG APPROVAL**, **IETF CONSENSUS**, and **STANDARDS ACTION** are to be interpreted as described in [RFC2434].
- Protocol fields appear in single quotes; example: `'data'`. Values appear in double quotes; example: `"foo"`.

## Architecture
### Host Keys
- Each server host **SHOULD** have a host key. Hosts **MAY** have multiple host keys using different algorithms. Multiple hosts **MAY** share the same host key.
- If a host has keys, it **MUST** have at least one key that uses each REQUIRED public key algorithm (DSS [FIPS-186-2]).
- The server host key is used during key exchange to verify the server identity. The client must have a priori knowledge of the server's public host key.
- Two trust models:
  1. Local database associating host name with public host key.
  2. Certification by a trusted CA.
- First-connection option: the protocol allows not checking the association, but such connections are vulnerable to man-in-the-middle attacks. Implementations **SHOULD NOT** normally allow such connections by default.
- Implementations **SHOULD** try to make the best effort to check host keys. Example strategy: accept without checking on first connection, save key, and compare on future connections.
- Implementations **MAY** provide additional methods for verifying host keys (e.g., SHA-1 fingerprint).
- All implementations **SHOULD** provide an option not to accept host keys that cannot be verified.

### Extensibility
- All implementations **MUST** support a minimal set of algorithms to ensure interoperability.
- Algorithm and method identifiers are textual names. DNS-based names (format `name@domain`) allow local extensions.
- Additional algorithms, methods, formats, and extension protocols can be defined in separate documents.

### Policy Issues
- The following policy issues **SHOULD** be addressed in configuration mechanisms:
  - Encryption, integrity, and compression algorithms, separately for each direction. The policy **MUST** specify the preferred algorithm (e.g., first listed).
  - Public key algorithms and key exchange method for host authentication.
  - Authentication methods required by the server for each user. Server policy **MAY** require multiple authentication.
  - Operations allowed using the connection protocol. The policy **SHOULD NOT** allow the server to start sessions or run commands on the client machine, and **MUST NOT** allow connections to the authentication agent unless forwarding has been requested.

### Security Properties
- Primary goal: improve security on the Internet, even at cost of absolute security.
- All algorithms are well-known, used with cryptographically sound key sizes.
- All algorithms are negotiated; if broken, switching is easy without modifying base protocol.
- Verification of server host key may be left out (NOT RECOMMENDED) to ease deployment.

### Localization and Character Set Support
- Character set for data **MUST** be explicitly specified. ISO-10646 UTF-8 is used where applicable. Language tag field may be provided.
- Interactive session character set determined by terminal emulation type (e.g., "vt100").
- Internal names (algorithms, protocols) must be US-ASCII.
- Client and server user names **MUST** be encoded using ISO-10646 UTF-8. Bit-wise binary comparison is **RECOMMENDED**.
- Textual messages **SHOULD** be minimized; when present, **SHOULD** be configurable; a numerical code may fetch localized message.

## Data Type Representations Used in the SSH Protocols
- **byte**: arbitrary 8-bit value. Fixed-length arrays: `byte[n]`.
- **boolean**: single byte (0=FALSE, 1=TRUE). Non-zero values **MUST** be interpreted as TRUE; applications **MUST NOT** store values other than 0 and 1.
- **uint32**: 32-bit unsigned integer (network byte order).
- **uint64**: 64-bit unsigned integer (network byte order).
- **string**: uint32 length followed by bytes. Terminating null **SHOULD NOT** normally be stored.
- **mpint**: multiple precision integer stored as a string (MSB first, two's complement). Positive numbers with MSB set **MUST** be preceded by a zero byte. Unnecessary leading bytes (0 or 255) **MUST NOT** be included. Zero **MUST** be stored as a string with zero bytes.
- **name-list**: comma-separated list of names stored as a string; each name **MUST** be non-empty, **MUST NOT** contain comma, **MUST** be US-ASCII. Terminating null characters **MUST NOT** be used. Order may be significant depending on context.

## Algorithm and Method Naming
- All algorithm and method identifiers **MUST** be printable US-ASCII, non-empty, no longer than 64 characters, case-sensitive.
- Two formats:
  1. Names without "@" are reserved for IETF consensus (e.g., "3des-cbc"). They **MUST NOT** contain "@", comma, whitespace, control characters, or DEL. Registered names are case-sensitive, ≤64 chars.
  2. Names with "@" are locally defined extensions: format `name@domainname`. Part before "@" is not specified but **MUST** be printable US-ASCII, no comma, whitespace, control characters, or DEL. Only one "@" allowed. Domain part **MUST** be a valid, fully qualified domain name controlled by the defining organization.

## Message Numbers
- Range 1–255, allocated as follows:
  - 1–19: Transport layer generic (disconnect, ignore, debug, etc.)
  - 20–29: Algorithm negotiation
  - 30–49: Key exchange method specific (reusable for different methods)
  - 50–59: User authentication generic
  - 60–79: User authentication method specific
  - 80–89: Connection protocol generic
  - 90–127: Channel related messages
  - 128–191: Reserved for client protocols
  - 192–255: Local extensions

## IANA Considerations
- Allocation of names in the following categories is assigned by IETF CONSENSUS: Service Names (Authentication Methods, Connection Protocol Channel/Global/Channel Request Names), Key Exchange Method Names, Assigned Algorithm Names (Encryption, MAC, Public Key, Compression).
- These names **MUST** be printable US-ASCII, no "@", comma, whitespace, control characters, or DEL. Case-sensitive, ≤64 chars.
- Names with "@" are locally defined extensions not controlled by IANA.
- Each category has a separate namespace; using the same name in multiple categories **SHOULD** be avoided to minimize confusion.
- Message numbers 0–191 allocated by IETF CONSENSUS; numbers 192–255 are PRIVATE USE.

## Security Considerations
### Pseudo-Random Number Generation
- All random numbers should be of good quality. If pseudo-random, the generator must be cryptographically secure and proper entropy added. [RFC4086] offers suggestions. Prefer refusing to run the protocol over using insufficient entropy.

### Control Character Filtering
- When displaying text (error/debug messages), client software **SHOULD** replace any control characters (except tab, carriage return, newline) with safe sequences to avoid terminal control character attacks.

### Transport
#### Confidentiality
- The "none" cipher is for debugging and **SHOULD NOT** be used except for that purpose.
- Implementations should check current literature for cipher strengths and **SHOULD** recommend stronger ciphers to users.
- CBC mode attacks may be mitigated by inserting packets containing `SSH_MSG_IGNORE`. If no unsent packets await transmission, a packet containing `SSH_MSG_IGNORE` **SHOULD** be sent.

#### Data Integrity
- Implementers **SHOULD** be wary of exposing the "none" MAC for any purpose other than debugging. Users and administrators **SHOULD** be explicitly warned when the "none" MAC is enabled.
- Rekeying **SHOULD** happen after at most 2^28 packets (smallest packet 16 bytes, rekey after one gigabyte).

#### Replay
- Peers **MUST** rekey before a wrap of the sequence numbers to prevent replay.

#### Man-in-the-middle
- If the offered host key does not match the cached key, the user **SHOULD** be given a warning. It is **RECOMMENDED** that the warning provide sufficient information for an informed decision.
- Using the protocol without reliable association of host and host keys is inherently insecure and **NOT RECOMMENDED**.
- Implementers **SHOULD** provide recommendations for secure distribution of host key fingerprints (e.g., secured web pages, physical media).

#### Denial of Service
- If transmission errors or message manipulation occur, the connection **SHOULD** be re-established.
- Implementers **SHOULD** provide features to make DoS more difficult (e.g., allowing connections only from known clients).

#### Covert Channels
- (Informative) Protocol not designed to eliminate covert channels.

#### Forward Secrecy
- (Informative) Diffie-Hellman key exchanges may provide perfect forward secrecy.

#### Ordering of Key Exchange Methods
- It is **RECOMMENDED** that algorithms be sorted by cryptographic strength, strongest first.

#### Traffic Analysis
- Implementers should use `SSH_MSG_IGNORE` and random padding to thwart traffic analysis.

### Authentication Protocol
- The server may go into a sleep period after repeated unsuccessful authentication attempts. Care should be taken to avoid self-denial of service.

#### Weak Transport
- If the transport layer does not provide confidentiality, authentication methods that rely on secret data **SHOULD** be disabled.
- If it does not provide strong integrity protection, requests to change authentication data (e.g., password change) **SHOULD** be disabled.

#### Debug Messages
- It is **RECOMMENDED** that debug messages be initially disabled at deployment and require an active decision by an administrator to enable. It is **RECOMMENDED** that a warning be presented when enabling debug messages.

#### Local Security Policy
- The implementer **MUST** ensure that credentials validate the professed user and that local policy permits access. Where local security policy exists, it **MUST** be applied and enforced correctly.

#### Public Key Authentication
- (Informative) Assumes client host not compromised; passphrases on private keys mitigate risk.

#### Password Authentication
- (Informative) Assumes server not compromised; alternative authentication methods (e.g., public key) mitigate vulnerability.

#### Host-Based Authentication
- (Informative) Assumes client not compromised; no mitigation other than combination with another method.

### Connection Protocol
#### End Point Security
- If server compromised, all sessions are compromised. If client compromised, services exposed are vulnerable. Implementers **SHOULD** provide mechanisms for administrators to control which services are exposed (e.g., port forwarding targets, interactive shell, subsystems).

#### Proxy Forwarding
- Proxy forwarding (SMTP, POP3, HTTP) may violate site security policies by tunneling through firewalls. Implementers **SHOULD** provide administrative mechanisms to control proxy forwarding functionality.

#### X11 Forwarding
- It is **RECOMMENDED** that X11 display implementations default to allow the display to open only over local IPC.
- It is **RECOMMENDED** that SSH server implementations supporting X11 forwarding default to allow the display to open only over local IPC.
- Implementers of X11 forwarding **SHOULD** implement the magic cookie access-checking spoofing mechanism as described in [SSH-CONNECT].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Each server host SHOULD have a host key. | SHOULD | §4.1 |
| R2 | If a host has keys, it MUST have at least one key using each REQUIRED public key algorithm (DSS). | MUST | §4.1 |
| R3 | Implementations SHOULD NOT normally allow connections without checking host key by default. | SHOULD | §4.1 |
| R4 | Implementations SHOULD try to make best effort to check host keys. | SHOULD | §4.1 |
| R5 | Implementations SHOULD provide an option not to accept host keys that cannot be verified. | SHOULD | §4.1 |
| R6 | All implementations MUST support a minimal set of algorithms. | MUST | §4.2 |
| R7 | The policy MUST specify the preferred algorithm (first listed). | MUST | §4.3 |
| R8 | Policy SHOULD NOT allow server to start sessions on client; MUST NOT allow connections to agent unless forwarding requested. | SHOULD/MUST | §4.3 |
| R9 | Character set for data MUST be explicitly specified; ISO-10646 UTF-8 used. | MUST | §4.5 |
| R10 | User names MUST be encoded using ISO-10646 UTF-8; bit-wise comparison RECOMMENDED. | MUST/RECOMMENDED | §4.5 |
| R11 | boolean values: applications MUST NOT store values other than 0 and 1. | MUST | §5 |
| R12 | mpint: positive numbers with MSB set MUST be preceded by a zero byte. Unnecessary leading bytes MUST NOT be included. Zero MUST be stored as string with zero bytes. | MUST | §5 |
| R13 | name-list: terminating null characters MUST NOT be used. | MUST | §5 |
| R14 | Algorithm/method identifiers MUST be printable US-ASCII, non-empty, ≤64 chars, case-sensitive. | MUST | §6 |
| R15 | Registered names (without @) MUST NOT contain "@", comma, whitespace, control chars, or DEL. | MUST | §6 |
| R16 | Local extension names (with @) MUST have only one "@"; domain part MUST be valid FQDN. | MUST | §6 |
| R17 | IANA-assigned names (various categories) MUST be printable US-ASCII, no "@", comma, etc. Case-sensitive, ≤64 chars. | MUST | §8 |
| R18 | Using same name in multiple categories SHOULD be avoided. | SHOULD | §8 |
| R19 | The "none" cipher SHOULD NOT be used except for debugging. | SHOULD | §9.3.1 |
| R20 | If no unsent packets, a packet containing SSH_MSG_IGNORE SHOULD be sent to mitigate CBC attack. | SHOULD | §9.3.1 |
| R21 | Implementers SHOULD be wary of exposing "none" MAC for non-debugging; users SHOULD be warned when "none" MAC enabled. | SHOULD | §9.3.2 |
| R22 | Rekeying SHOULD happen after at most 2^28 packets. | SHOULD | §9.3.2 |
| R23 | Peers MUST rekey before wrap of sequence numbers. | MUST | §9.3.3 |
| R24 | If offered host key does not match cached key, user SHOULD be given warning. | SHOULD | §9.3.4 |
| R25 | Association of host and host key is NOT RECOMMENDED to be skipped. | NOT RECOMMENDED | §9.3.4 |
| R26 | Connection SHOULD be re-established after errors/manipulation. | SHOULD | §9.3.5 |
| R27 | Implementers SHOULD provide features to mitigate DoS. | SHOULD | §9.3.5 |
| R28 | Key exchange algorithms sorted by cryptographic strength is RECOMMENDED. | RECOMMENDED | §9.3.8 |
| R29 | If transport lacks confidentiality, authentication methods relying on secret data SHOULD be disabled. | SHOULD | §9.4.1 |
| R30 | If transport lacks strong integrity, requests to change auth data SHOULD be disabled. | SHOULD | §9.4.1 |
| R31 | Debug messages RECOMMENDED to be initially disabled; require admin action to enable; warning RECOMMENDED when enabling. | RECOMMENDED | §9.4.2 |
| R32 | Implementer MUST ensure credentials validate user and local policy permits access; local policy MUST be applied and enforced. | MUST | §9.4.3 |
| R33 | Implementers SHOULD provide mechanisms to control exposed services (port forwarding, shell, subsystems). | SHOULD | §9.5.1 |
| R34 | Implementers SHOULD provide administrative mechanism to control proxy forwarding. | SHOULD | §9.5.2 |
| R35 | X11 display implementations RECOMMENDED to default to local IPC only. | RECOMMENDED | §9.5.3 |
| R36 | SSH server implementations supporting X11 forwarding RECOMMENDED to default to local IPC only. | RECOMMENDED | §9.5.3 |
| R37 | Implementers of X11 forwarding SHOULD implement magic cookie spoofing as per [SSH-CONNECT]. | SHOULD | §9.5.3 |

## Informative Annexes (Condensed)
- **[Section 2 – Contributors]**: Lists major contributors and acknowledgees; omitted for brevity.
- **[Section 9 – Security Considerations]**: The entire Security Considerations section (including subsections 9.1–9.5.3) is normative in part but also contains extensive explanatory and advisory material. Key normative requirements are extracted above in the Requirements Summary and in the Security Considerations subsections. The informative content describes attack scenarios, mitigations, and design rationale. Refer to original document for full discussion.