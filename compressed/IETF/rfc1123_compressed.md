# RFC 1123: Requirements for Internet Hosts -- Application and Support
**Source**: Internet Engineering Task Force (IETF) | **Version**: RFC 1123 | **Date**: October 1989 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc1123

## Scope (Summary)
This RFC defines and discusses the requirements for Internet host software for the application and support protocol layers. It incorporates by reference, amends, corrects, and supplements the primary protocol standards for Telnet, FTP, TFTP, SMTP, DNS, host initialization, and network management. Its companion RFC 1122 covers the communication protocol layers (link, IP, transport).

## Normative References
- [INTRO:1] "Requirements for Internet Hosts -- Communication Layers", RFC 1122, October 1989.
- [INTRO:5] "Assigned Numbers", RFC 1010, May 1987 (latest version).
- [TELNET:1] "Telnet Protocol Specification", RFC 854, May 1983.
- [TELNET:2] "Telnet Option Specification", RFC 855, May 1983.
- [TELNET:10] "Telnet Terminal-Type Option", RFC 1091, February 1989.
- [FTP:1] "File Transfer Protocol", RFC 959, October 1985.
- [TFTP:1] "The TFTP Protocol Revision 2", RFC 783, June 1981.
- [SMTP:1] "Simple Mail Transfer Protocol", RFC 821, August 1982.
- [SMTP:2] "Standard For The Format of ARPA Internet Text Messages", RFC 822, August 1982.
- [SMTP:3] "Mail Routing and the Domain System", RFC 974, January 1986.
- [DNS:1] "Domain Names - Concepts and Facilities", RFC 1034, November 1987.
- [DNS:2] "Domain Names - Implementation and Specification", RFC 1035, November 1987.
- [BOOT:2] "Bootstrap Protocol (BOOTP)", RFC 951, September 1985.
- [BOOT:3] "BOOTP Vendor Information Extensions", RFC 1084, December 1988.
- [MGT:4] "A Simple Network Management Protocol", RFC 1098, April 1989.
- [MGT:5] "The Common Management Information Services and Protocol over TCP/IP", RFC 1095, April 1989.

## Definitions and Abbreviations
- **Segment**: The unit of end-to-end transmission in the TCP protocol; consists of a TCP header followed by application data.
- **Message**: Used by some application layer protocols (e.g., SMTP) for an application data unit.
- **Datagram**: The unit of end-to-end transmission in the UDP protocol.
- **Multihomed**: A host with multiple IP addresses to connected networks.

## 1. Introduction (Summary)
- This document is one of a pair (with RFC 1122) defining host requirements.
- **Robustness Principle**: "Be liberal in what you accept, and conservative in what you send" (Section 1.2.2).
- **Error Logging**: Hosts SHOULD include facilities for logging erroneous or strange protocol events, with diagnostic information (Section 1.2.3).
- **Configuration**: Parameters MUST be configurable; defaults MUST implement the official protocol (Section 1.2.4).

## 2. General Issues
### 2.1 Host Names and Numbers
- **MUST**: Support host names beginning with a letter or digit (relaxation of RFC 952).
- **MUST**: Handle host names up to 63 characters; **SHOULD** handle up to 255 characters.
- **SHOULD**: Allow user to enter either a host domain name or dotted-decimal IP address; check syntactically for dotted-decimal before DNS lookup.

### 2.2 Using Domain Name Service
- **MUST**: Translate host domain names to IP addresses as described in Section 6.1 (DNS).
- **MUST**: Cope with soft error conditions; wait reasonable interval between retries; allow for outages of hours/days.
- **SHOULD NOT**: Rely on WKS records to confirm service presence; simply attempt to use the service.

### 2.3 Applications on Multihomed Hosts
- **SHOULD**: Be prepared to try multiple addresses from the list returned for a remote multihomed host.
- **SHOULD**: For UDP response, set IP source address to the specific destination address of the request datagram.
- **SHOULD**: For multiple TCP connections to same client, use same local IP address.

### 2.4 Type-of-Service
- **MUST**: Select appropriate TOS values; these values MUST be configurable.
- **MUST**: Set undefined TOS bits to zero.

### 2.5 General Application Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| G1 | Support host name beginning with digit | MUST | §2.1 |
| G2 | Host names up to 63 characters | MUST | §2.1 |
| G3 | Host names up to 255 characters | SHOULD | §2.1 |
| G4 | Support dotted-decimal host numbers | SHOULD | §2.1 |
| G5 | Check syntactically for dotted-decimal first | SHOULD | §2.1 |
| G6 | Map domain names per §6.1 | MUST | §2.2 |
| G7 | Cope with soft DNS errors | MUST | §2.2 |
| G8 | Reasonable interval between retries | MUST | §2.2 |
| G9 | Allow for long outages | MUST | §2.2 |
| G10 | Expect WKS records to be available | MUST NOT (reverse) | §2.2 |
| G11 | Try multiple addresses for remote multihomed host | SHOULD | §2.3 |
| G12 | UDP reply src addr = specific dest of request | SHOULD | §2.3 |
| G13 | Use same IP addr for related TCP connections | SHOULD | §2.3 |
| G14 | Specify appropriate TOS values | MUST | §2.4 |
| G15 | TOS values configurable | MUST | §2.4 |
| G16 | Unused TOS bits zero | MUST | §2.4 |

## 3. Remote Login – TELNET Protocol
### 3.1 Introduction
Telnet uses a single TCP connection; normal data stream is 7-bit ASCII with escape sequences; defines NVT (Network Virtual Terminal) mode.

### 3.2 Protocol Walk-Through
#### 3.2.1 Option Negotiation
- **MUST**: Include option negotiation and subnegotiation machinery (RFC 855).
- **MUST**: Carefully follow RFC 854 to avoid negotiation loops.
- **MUST**: Refuse unsupported options (reply WONT/DONT).
- **SHOULD**: Option negotiation continue to function throughout connection lifetime.
- **MUST**: Default to and support an NVT if all option negotiations fail.

#### 3.2.2 Telnet Go-Ahead Function
- **MUST**: Server that never sends GA command MUST negotiate Suppress Go Ahead (WILL Suppress Go Ahead).
- **MUST**: Always accept negotiation of Suppress Go Ahead.
- **MAY**: Ignore GA commands when driving full-duplex terminal.

#### 3.2.3 Control Functions
- **MUST**: Support AO, AYT, DM, IP, NOP, SB, SE.
- **MAY**: Support EOR, EC, EL, and Break.
- **MUST**: Be able to receive and ignore any unsupported control functions.

#### 3.2.4 Telnet "Synch" Signal
- **MUST**: On receiving TCP urgent data, discard all data except Telnet commands until DM (and end of urgent) is reached.
- **SHOULD**: User Telnet send Synch sequence (IAC IP IAC DM) after IP.
- **MAY**: Server Telnet send Synch back upon receiving IP.
- **MUST**: Server send Synch upon receiving AO.
- **SHOULD**: User Telnet have capability to flush output when sending IP.

#### 3.2.5 NVT Printer and Keyboard
- **SHOULD NOT**: Send characters with high-order bit 1.
- **MUST NOT**: Send high-order bit as parity bit.
- **SHOULD**: Negotiate binary mode if passing high-order bit to applications.

#### 3.2.6 Telnet Command Structure
- **MUST**: Double IAC (value 255) when sent as data.

#### 3.2.7 Telnet Binary Option
- **MUST**: Still scan for IAC characters; obey embedded Telnet commands; double IAC bytes.
- **MUST NOT**: Do character processing (e.g., CR -> CR NUL or CR LF); no end-of-line convention in binary mode.

#### 3.2.8 Telnet Terminal-Type Option
- **MUST**: Use official terminal type names from Assigned Numbers (RFC 1010) when available.
- **MUST**: Accept any terminal type name.

### 3.3 Specific Issues
#### 3.3.1 Telnet End-of-Line Convention
- **MUST**: Server Telnet treat CR LF as same as local end-of-line key.
- **MUST**: On ASCII server, CR LF and CR NUL have same effect as pressing CR.
- **MUST**: User Telnet be able to send CR LF, CR NUL, and LF.
- **SHOULD**: User Telnet on ASCII host have user-controllable mode to send CR LF or CR NUL; CR LF is default.
- **MUST**: For non-interactive data (e.g., server output), use CR LF.

#### 3.3.2 Data Entry Terminals (Informative)
- Native DET mode can be entered via Binary option and EOR option for record delimiting.

#### 3.3.3 Option Requirements
- **MUST**: Support Binary and Suppress Go Ahead options.
- **SHOULD**: Support Echo, Status, End-of-Record, and Extended Options List.
- **SHOULD**: Support Window Size option if local OS provides corresponding capability.

#### 3.3.4 Option Initiation
- **SHOULD**: Server initiate negotiation of terminal interaction mode.
- **SHOULD**: Client provide means for users to enable/disable initiation of option negotiation.

#### 3.3.5 Telnet Linemode Option (Informative)
- New option (LINEMODE) proposed for client-side character processing; expected to be implemented.

### 3.4 Telnet/User Interface
- **SHOULD**: Be able to send/receive any 7-bit ASCII character.
- **SHOULD**: Bypass local OS special character interpretations where possible.
- **MUST**: Reserve escape character; **SHOULD** be user selectable.
- **MAY**: Provide escape mechanism for entering arbitrary 8-bit values in binary mode.
- **MUST**: Provide user capability to enter IP, AO, AYT; **SHOULD** provide EC, EL, Break.
- **SHOULD**: Report TCP connection errors to user.
- **SHOULD**: Allow optional non-default contact port number.
- **SHOULD**: Provide user ability to specify whether output flushed when IP sent; provide way to manually restore output if server fails.

### 3.5 Telnet Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| T1 | Implement option negotiation | MUST | §3.2.1 |
| T2 | Avoid negotiation loops | MUST | §3.2.1 |
| T3 | Refuse unsupported options | MUST | §3.2.1 |
| T4 | Default to NVT | MUST | §3.2.1 |
| T5 | Non-GA server negotiate SUPPRESS-GA | MUST | §3.2.2 |
| T6 | Accept SUPPRESS-GA | MUST | §3.2.2 |
| T7 | Support SE,NOP,DM,IP,AO,AYT,SB | MUST | §3.2.3 |
| T8 | Ignore unsupported control functions | MUST | §3.2.3 |
| T9 | Discard urgent data up to DM | MUST | §3.2.4 |
| T10 | User send Synch after IP, AO, AYT | SHOULD | §3.2.4 |
| T11 | Server reply Synch to AO | MUST | §3.2.4 |
| T12 | Send high-order bit in NVT mode | SHOULD (not) | §3.2.5 |
| T13 | Double IAC data byte | MUST | §3.2.6, §3.2.7 |
| T14 | CR LF/CR NUL same effect on ASCII server | MUST | §3.3.1 |
| T15 | User send CR LF, CR NUL, LF | MUST | §3.3.1 |
| T16 | Default EOL: CR LF | SHOULD | §3.3.1 |
| T17 | Support Binary, Suppress-GA | MUST | §3.3.3 |
| T18 | Support Echo, Status, EOR, Ext-Opt-List | SHOULD | §3.3.3 |
| T19 | Server initiate mode negotiations | SHOULD | §3.3.4 |
| T20 | User can enable/disable init negotiations | SHOULD | §3.3.4 |
| T21 | User input IP, AO, AYT | MUST | §3.4.2 |
| T22 | User input EC, EL, Break | SHOULD | §3.4.2 |
| T23 | Report TCP errors to user | SHOULD | §3.4.3 |
| T24 | Optional non-default contact port | SHOULD | §3.4.4 |
| T25 | Can spec output flushed when IP sent | SHOULD | §3.4.5 |
| T26 | Can manually restore output mode | SHOULD | §3.4.5 |

## 4. File Transfer
### 4.1 File Transfer Protocol – FTP
#### 4.1.1 Introduction
- FTP uses separate TCP connections for control and data.
- Minimum implementation is defined as larger than RFC 959.

#### 4.1.2 Protocol Walk-Through
- **MUST**: Support TYPE I (IMAGE) and TYPE L 8.
- **SHOULD**: Implement TYPE T identical to TYPE N if host makes no distinction.
- **NOT RECOMMENDED**: Page structure; if implemented, MUST use defined format.
- **SHOULD**: Data structure transformations between record-structure and file-structure be invertible where possible.
- **SHOULD**: User-FTP send PORT command for stream mode before each transfer.
- **MUST**: Server-FTP implement PASV.
- **MUST**: New PASV before each third-party transfer.
- **MUST**: NLST response contain simple list of legal pathnames usable as arguments for RETR.
- **SHOULD**: LIST/NLST data use implied TYPE AN (or EN for EBCDIC).
- **SHOULD**: Use SITE command for non-standard features.
- **MUST**: STOU return actual file name in 125/150 message (format: "125 FILE: pppp" or "150 FILE: pppp").
- **MUST NOT**: Assume correspondence between TCP READ boundaries and Telnet EOL sequences on control connection.
- **MUST**: Server send correctly formatted replies.
- **SHOULD**: Use defined reply codes; if ambiguous between 4xx and 5xx, prefer 4xx for temporary failures.
- **SHOULD**: User-FTP generally use only highest-order digit for procedural decisions.
- **MUST**: User-FTP handle multi-line replies; recover if limit exceeded.
- **SHOULD** NOT: Interpret 421 specially; detect closing of control connection.
- **MUST**: For multihomed server, default data port use same IP address as control connection.
- **MUST**: User-FTP send no Telnet controls except SYNCH and IP on control connection; MUST NOT negotiate Telnet options.
- **MUST**: Server-FTP be capable of accepting/refusing Telnet negotiations.
- **MUST**: Minimum command set: USER, PASS, ACCT, PORT, PASV, TYPE, MODE, STRU, RETR, STOR, APPE, RNFR, RNTO, DELE, CWD, CDUP, RMD, MKD, PWD, LIST, NLST, SYST, STAT, HELP, NOOP, QUIT.
- **MUST**: Support TYPE AN, IMAGE, LOCAL 8; Mode Stream; Structure File (and Record if host supports record-structure).

#### 4.1.3 Specific Issues
- **SHOULD**: Recognize both RFC-959 and experimental (X) forms of directory commands.
- **SHOULD**: Server-FTP have configurable idle timeout; default at least 5 minutes.
- **Concurrency**: Minimal server must be prepared to accept/defer STAT or ABOR during data transfer.
- **Restart**: Corrected description; two new reply codes (554, 555) defined.

#### 4.1.4 FTP/User Interface
- **MUST**: Support remote pathnames as arbitrary character strings (all printing ASCII plus space).
- **MUST**: Implement "QUOTE" command that passes string to server and displays responses.
- **SHOULD**: Display full text of error replies; have "verbose" mode.
- **SHOULD**: Be forgiving of missing/unexpected replies to maintain synchronization.

#### 4.1.5 FTP Requirements Summary (selected)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| F1 | Support TYPE I and TYPE L 8 | MUST | §4.1.2.1 |
| F2 | Implement PASV | MUST | §4.1.2.6 |
| F3 | STOU return pathname as specified | MUST | §4.1.2.9 |
| F4 | Server send only correct reply format | MUST | §4.1.2.11 |
| F5 | User handle multi-line replies | MUST | §4.1.2.11 |
| F6 | Default data port same IP as ctl conn | MUST | §4.1.2.12 |
| F7 | User NOT negotiate Telnet options | MUST | §4.1.2.12 |
| F8 | Handle X directory commands | SHOULD | §4.1.3.1 |
| F9 | Idle timeout configurable | SHOULD | §4.1.3.2 |
| F10 | Support minimum command set | MUST | §4.1.2.13 |
| F11 | Arbitrary pathnames | MUST | §4.1.4.1 |
| F12 | Implement "QUOTE" | MUST | §4.1.4.2 |

### 4.2 Trivial File Transfer Protocol – TFTP
#### 4.2.1 Introduction
- TFTP provides simple stop-and-wait reliable delivery over UDP.
- Important for network booting.

#### 4.2.2 Protocol Walk-Through
- **SHOULD NOT**: Support transfer mode "mail".
- **Note**: UDP Length field incorrectly defined; includes header length.

#### 4.2.3 Specific Issues
- **MUST**: Implement fix for Sorcerer's Apprentice Syndrome: sender must not resend DATA on receipt of duplicate ACK.
- **MUST**: Use adaptive timeout (e.g., exponential backoff).
- **Extensions**: None standardized.
- **SHOULD**: Include configurable access control over allowed pathnames.
- **SHOULD**: Silently ignore broadcast requests.

#### 4.2.4 TFTP Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| TF1 | Fix Sorcerer's Apprentice Syndrome | MUST | §4.2.3.1 |
| TF2 | Support netascii and octet transfer modes | MUST | RFC 783 |
| TF3 | Not support mail mode | SHOULD | §4.2.2.1 |
| TF4 | Use adaptive timeout | MUST | §4.2.3.2 |
| TF5 | Configurable access control | SHOULD | §4.2.3.4 |
| TF6 | Silently ignore broadcast request | SHOULD | §4.2.3.5 |

## 5. Electronic Mail – SMTP and RFC 822
### 5.1 Introduction
- SMTP (RFC 821) transmits messages in RFC 822 format.
- Domain Name System (DNS) has changed address formats and routing.

### 5.2 Protocol Walk-Through
#### 5.2.1 The SMTP Model
- Distinguish between User Agent and Message Transfer Agent (MTA).
- SMTP envelope (MAIL FROM, RCPT TO) is separate from message header.

#### 5.2.2 Canonicalization
- **MUST**: Domain names in MAIL and RCPT commands be fully-qualified principal names or domain literals (no nicknames, abbreviations, CNAMEs).

#### 5.2.3 VRFY and EXPN Commands
- **MUST**: Implement VRFY; **SHOULD**: Implement EXPN (overrides RFC 821).
- **MAY**: Disable VRFY/EXPN via configuration.
- **New reply code 252**: Cannot VRFY but will take message and attempt delivery.

#### 5.2.4 SEND, SOML, SAML Commands
- **MAY**: Implement.

#### 5.2.5 HELO Command
- **MUST**: Ensure HELO parameter is a valid principal host domain name for the client.
- **MAY**: Verify HELO parameter; **MUST NOT** refuse message on verification failure.

#### 5.2.6 Mail Relay
- **SHOULD NOT**: Alter existing header fields (except add Received: line).
- **SHOULD NOT**: Send explicit source route ("@...:") in RCPT TO.
- **MUST**: Accept explicit source route syntax in envelope; **MAY** implement relay; if not, **SHOULD** attempt delivery directly.

#### 5.2.7 RCPT Command
- **MUST**: Support reserved mailbox "Postmaster".
- **MAY**: Verify RCPT parameters as they arrive, but MUST NOT delay response beyond reasonable time.

#### 5.2.8 DATA Command
- **MUST**: Insert Received: line at beginning of message.
- FOR field MAY contain list of <path> entries.
- **MUST NOT**: Change a previously added Received: line.
- **MUST**: Pass MAIL FROM: address from envelope for final delivery or gatewaying.

#### 5.2.9 Command Syntax
- **MUST**: Support empty reverse path ("MAIL FROM:<>").

#### 5.2.10 SMTP Replies
- **SHOULD**: Send only reply codes listed in RFC 821 or this document; use text from RFC 821 when appropriate.
- **MUST**: Determine actions only by reply code, not text (except 251/551).

#### 5.2.11 Transparency
- **MUST**: Always add and delete periods to ensure message transparency.

#### 5.2.12 WKS Use in MX Processing
- **SHOULD NOT**: Use WKS records in MX processing (deprecated).

#### 5.2.13 RFC 822 Message Specification
- **MAY**: Support Content-Type field (RFC 1049).

#### 5.2.14 Date and Time Specification
- **SHOULD**: Use 4-digit years.
- **SHOULD**: Use numeric timezones; **MUST** accept either notation; timezone names must match RFC 822 exactly.

#### 5.2.15 RFC 822 Syntax Change
- **Definition of mailbox**: phrase before route-addr is now OPTIONAL.

#### 5.2.17 Domain Literals
- **MUST**: Accept and parse dotted-decimal domain literals.
- **MUST**: Recognize domain literal for own IP addresses.

#### 5.2.18 Common Address Formatting Errors
- **MUST**: Accept all valid RFC 822 address formats; **MUST NOT** generate illegal syntax.
- **MUST**: Fully-qualify domain names in header address fields.

#### 5.2.19 Explicit Source Routes
- **SHOULD NOT**: Create RFC 822 header with explicit source route; **MUST** accept such headers.

### 5.3 Specific Issues
#### 5.3.1 SMTP Queueing Strategies
- **MUST**: Include timeouts on all activities.
- **MUST**: Never send error messages in response to error messages.
- **Sending Strategy**:
  - **MUST**: Queue and periodically retry messages after soft failure.
  - **SHOULD**: Delay retry at least 30 minutes; retry at least 4-5 days.
  - **MUST**: Configurable retry parameters.
  - **SHOULD**: Keep list of unreachable hosts rather than retrying each queued item separately.
  - **SHOULD**: Use multiple RCPT commands before DATA when delivering to multiple users on same host.
- **Receiving Strategy**:
  - **SHOULD**: Keep pending listen on SMTP port at all times.

#### 5.3.2 Timeouts in SMTP
- **SHOULD**: Use per-command timeouts.
- **SHOULD**: Be easily reconfigurable.
- Recommended minima: Initial 220 msg: 5 min; MAIL: 5 min; RCPT: 5 min; DATA Initiation: 2 min; Data Block: 3 min; DATA Termination: 10 min.
- Receiver **SHOULD** have timeout of at least 5 minutes while awaiting next command.

#### 5.3.3 Reliable Mail Receipt
- **MUST NOT**: Lose message after acceptance.
- **MUST**: Send error notification message (with null return path) for delivery failures after acceptance.
- **MUST**: Minimize response time to final "." (per RFC 1047).

#### 5.3.4 Reliable Mail Transmission
- **MUST**: Try alternate addresses in order of preference (MX, multihoming).
- **SHOULD**: Try at least two addresses.
- **MAY**: Configurable limit on number of alternates.
- **SHOULD**: Pick random among equal-preference MX records for load spreading.

#### 5.3.5 Domain Name Support
- **MUST**: Include DNS support; **MUST** support MX records.

#### 5.3.6 Mailing Lists and Aliases
- **SHOULD**: Support both alias and list expansion.
- For lists, **MUST** change envelope return address to list administrator; message header unchanged.

#### 5.3.7 Mail Gatewaying
- **MAY**: Rewrite header fields when necessary.
- **MUST**: Prepend Received: line; **MUST NOT** alter existing Received: line.
- **SHOULD**: Accept all valid address formats on Internet side.
- **MUST**: Ensure header fields forwarded into Internet meet RFC 822 syntax.
- **SHOULD**: Deliver error messages to envelope return path (not From: field).
- **SHOULD**: Set envelope return path from foreign error return address.

#### 5.3.8 Maximum Message Size
- **MUST**: Be able to send/receive at least 64K bytes.

### 5.4 SMTP Requirements Summary (selected)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| M1 | Canonicalized domain names in MAIL/RCPT | MUST | §5.2.2 |
| M2 | Implement VRFY | MUST | §5.2.3 |
| M3 | Implement EXPN | SHOULD | §5.2.3 |
| M4 | HELO with valid principal hostname | MUST | §5.2.5 |
| M5 | Support Postmaster | MUST | §5.2.7 |
| M6 | Add Received: line | MUST | §5.2.8 |
| M7 | Pass Return-Path info on final delivery | MUST | §5.2.8 |
| M8 | Support empty reverse path | MUST | §5.2.9 |
| M9 | Determine actions by reply code only | MUST | §5.2.10 |
| M10 | Ensure transparency (dot-stuffing) | MUST | §5.2.11 |
| M11 | Accept dotted-decimal domain literals | MUST | §5.2.17 |
| M12 | Retry messages after soft failure | MUST | §5.3.1.1 |
| M13 | Use per-command timeouts | SHOULD | §5.3.2 |
| M14 | Try alternate addresses in order | MUST | §5.3.4 |
| M15 | Support MX records | MUST | §5.3.5 |
| M16 | Send error notifications with null return path | MUST | §5.3.3 |
| M17 | Fully-qualified domain names in header | MUST | §5.2.18 |
| M18 | Send/recv at least 64KB | MUST | §5.3.8 |

## 6. Support Services
### 6.1 Domain Name Translation
#### 6.1.1 Introduction
- **MUST**: Implement DNS resolver for host name-to-address and address-to-name conversion.
- **MAY**: Also support local host table.

#### 6.1.2 Protocol Walk-Through
- **MUST**: Handle RRs with zero TTL (return but not cache).
- **SHOULD NOT**: Use QCLASS=* unless requesting data from more than one class; use QCLASS=IN for Internet class.
- **MUST**: Zero unused fields in query/response.
- **MUST**: Name servers use compression in responses.
- **MUST NOT**: Include configuration hints in responses.

#### 6.1.3 Specific Issues
##### 6.1.3.1 Resolver Implementation
- **SHOULD**: Be able to multiplex concurrent requests.
- **Full-service resolver**:
  - **MUST**: Implement local caching with timeout.
  - **SHOULD**: Be configurable with multiple root servers and local domain servers.
- **Stub resolver**:
  - **MUST**: Be able to direct requests to redundant recursive servers.
  - **MAY**: Implement caching with timeout.

##### 6.1.3.2 Transport Protocols
- **MUST**: Support UDP for queries.
- **SHOULD**: Support TCP; send UDP first; if truncated, try TCP.
- **MUST**: DNS servers service UDP queries; **SHOULD** service TCP.
- **MUST NOT**: Use truncated responses as if complete.
- **MUST**: Use TCP for zone transfers.
- **MUST**: Have sufficient concurrency to process UDP while awaiting TCP responses.

##### 6.1.3.3 Efficient Resource Usage
- **MUST**: Implement retransmission controls with finite bounds.
- **MUST**: Give up after several retries and return soft error.
- **SHOULD**: Cache temporary failures with timeout of minutes.
- **SHOULD**: Cache negative responses.
- **SHOULD**: Use exponential backoff with bounds for retries.
- **SHOULD**: Handle Source Quench by reducing query rate.

##### 6.1.3.4 Multihomed Hosts
- **SHOULD**: Rank/sort addresses using network preference list.

##### 6.1.3.5 Extensibility
- **MUST**: Support all well-known, class-independent formats.
- **SHOULD**: Minimize trauma of new types.

##### 6.1.3.6 Status of RR Types
- **MUST**: Be able to load all RR types except MD, MF from configuration files.
- **MUST NOT**: Implement MD and MF.

##### 6.1.3.7 Robustness
- **MUST**: Continue to provide service for reachable part of name space when root servers unreachable.

##### 6.1.3.8 Local Host Table
- Informative: may be used as backup; DDN NIC host table available.

#### 6.1.4 DNS User Interface
- **MUST**: Provide interface for all applications to DNS.
- **MUST**: Basic interface support request for all info of a specific type/class; return info, hard error, or soft error.
- **MAY**: Provide other tailored interfaces; **MUST** provide interface for name<->address translation.
- **Abbreviation facilities**:
  - **MUST**: Provide convention for denoting complete name (trailing dot).
  - **MUST**: Expand abbreviation exactly once in context.
  - **Search list**: **SHOULD** be possible for administrator to disable.
  - **MUST**: Prevent excessive root queries (by negative caching or requiring interior dots).

#### 6.1.5 DNS Requirements Summary (selected)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| D1 | Implement DNS name-to-address conversion | MUST | §6.1.1 |
| D2 | Implement DNS address-to-name conversion | MUST | §6.1.1 |
| D3 | Handle zero TTL RR | MUST | §6.1.2.1 |
| D4 | Use compression in responses | MUST | §6.1.2.4 |
| D5 | Not include config hints in responses | MUST | §6.1.2.5 |
| D6 | Support UDP queries | MUST | §6.1.3.2 |
| D7 | Support TCP queries | SHOULD | §6.1.3.2 |
| D8 | Use TCP for zone transfers | MUST | §6.1.3.2 |
| D9 | Implement retransmission controls | MUST | §6.1.3.3 |
| D10 | Give soft error after retries | MUST | §6.1.3.3 |
| D11 | Cache temporary failures | SHOULD | §6.1.3.3 |
| D12 | Cache negative responses | SHOULD | §6.1.3.3 |
| D13 | Sort multiple addresses by preference | SHOULD | §6.1.3.4 |
| D14 | Support all well-known class-indep types | MUST | §6.1.3.5 |
| D15 | Operate when root servers unavailable | MUST | §6.1.3.7 |
| D16 | Provide DNS interface to all apps | MUST | §6.1.4.2 |
| D17 | Convention for complete name | MUST | §6.1.4.3 |

### 6.2 Host Initialization
#### 6.2.1 Introduction
- Two phases: configure IP layer, then load system code.
- **Dynamic configuration** recommended even for diskful hosts.

#### 6.2.2 Requirements
- **Suggested**: Use BOOTP (RFC 951) with Vendor Extensions (RFC 1084) for dynamic configuration.
- **RECOMMENDED**: Supply address mask via BOOTP.
- **Loading phase**: Suggest TFTP between addresses established by BOOTP.
- **SHOULD NOT**: Use TFTP to broadcast address.

### 6.3 Remote Management
#### 6.3.1 Introduction
- **SHOULD**: Include an agent for SNMP (RFC 1098) or CMOT (RFC 1095).
- **SHOULD**: Implement relevant MIB variables from standard MIB (RFC 1066).

#### 6.3.2 Protocol Walk-Through
- **MUST**: Implement System, Interfaces, Address Translation, IP, ICMP, TCP, UDP groups.
- Specific host interpretations:
  - icmpOutRedirects: MUST be zero.
  - icmpOutAddrMaskReps: MUST be zero unless authoritative.
  - ipFragOKs etc: MUST be zero if host does not fragment.
- ipRoutingTable: metrics normally meaningless.
- Future MIB expansion expected for applications.

#### 6.3.3 Management Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| MG1 | Support SNMP or CMOT agent | SHOULD | §6.3.1 |
| MG2 | Implement specified MIB objects | SHOULD | §6.3.1 |

## Informative Annexes (Condensed)
- **Security Considerations**: Security issues mentioned in TFTP (access control, broadcast), SMTP VRFY/EXPN, HELO, DATA (Received: line). Full discussion beyond this RFC.
- **Acknowledgments**: Extensive contributions from IETF Host Requirements Working Group and many individuals.

*End of document.*