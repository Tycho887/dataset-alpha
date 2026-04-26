# RFC 2821: Simple Mail Transfer Protocol
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: April 2001 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc2821 (or RFC 2821)

## Scope (Summary)
This document specifies the Simple Mail Transfer Protocol (SMTP) for transferring mail reliably and efficiently over the Internet. It consolidates and clarifies RFC 821, RFC 974, RFC 1123, and material from the SMTP Extension mechanisms (RFC 1869), and obsoletes RFC 821 and RFC 974. The protocol is independent of the transmission subsystem and requires only a reliable ordered data stream channel.

## Normative References
- RFC 821 (obsoleted)
- RFC 974 (obsoleted)
- RFC 1123
- RFC 1035
- RFC 1869
- RFC 2822
- RFC 2234
- Other referenced RFCs as listed in Section 9.

## Definitions and Abbreviations
- **MUST/REQUIRED/SHALL**: absolute requirement of the specification.
- **MUST NOT/SHALL NOT**: absolute prohibition.
- **SHOULD/RECOMMENDED**: may be ignored only after understanding implications.
- **SHOULD NOT/NOT RECOMMENDED**: behavior acceptable only after careful consideration.
- **MAY/OPTIONAL**: truly optional; implementations must interoperate with or without the option.
- **Mail Object**: consists of an envelope (originator, recipients, optional extensions) and content (headers and body).
- **SMTP Client**: the sending host (previously SMTP-sender).
- **SMTP Server**: the receiving host (previously SMTP-receiver).
- **Mail Transfer Agent (MTA)**: provides mail transport service.
- **Mail User Agent (MUA)**: source/target of mail.
- **Host**: computer system attached to the Internet running SMTP.
- **Domain / Domain Name**: fully-qualified domain name (FQDN) consisting of dot-separated labels; local aliases MUST NOT appear in SMTP transactions.
- **Buffer and State Table**: virtual constructs modeling the stateful session.
- **Lines**: commands and data transmitted in lines terminated by <CRLF> (CR hex 0D followed by LF hex 0A).
- **Originator, Delivery, Relay, Gateway Systems**: four types of SMTP systems defined by role.
- **Mailbox and Address**: "local-part@domain"; local-part MUST be interpreted only by the host specified in the domain.
- **Reply**: acknowledgment from server to client; numeric code followed by text.

## 1. Introduction
SMTP transfers mail reliably and efficiently across networks. It uses reliable ordered data streams, typically over TCP. SMTP can relay mail across networks using MX records (see Section 5). A message may pass through intermediate relay or gateway hosts.

## 2. The SMTP Model
### 2.1 Basic Structure
- SMTP client establishes a two-way transmission channel to SMTP server.
- Client transfers mail to one or more servers or reports failure.
- Fully-capable implementations MUST support queuing, retrying, and alternate address functions.
- Server accepts responsibility for delivering or properly reporting failure.

### 2.2 The Extension Model
- **2.2.1 Background**: EHLO command supersedes HELO; servers MUST support EHLO even without extensions; clients SHOULD use EHLO preferentially.
- **2.2.2 Definition and Registration of Extensions**: IANA maintains registry; each extension must be defined in a standards-track or IESG-approved experimental document. Keywords starting with "X" are for bilateral agreements and MUST NOT be registered. Non-"X" keywords MUST correspond to registered extensions.

### 2.3 Terminology
*(Definitions provided above)*

### 2.4 General Syntax Principles and Transaction Model
- Commands and replies have rigid syntax; commands begin with verb, replies with three-digit code.
- Verbs and argument values (except mailbox local-part) are case-insensitive; local-part MUST be treated as case sensitive.
- SMTP clients MUST NOT transmit bare CR or LF characters except as <CRLF> line terminators.
- Unextended SMTP provides seven-bit transport; high-order bits MUST be cleared unless 8BITMIME extension negotiated.
- Originators MUST NOT transmit messages with high-order bit set without successful negotiation.
- Servers MAY clear high-order bit or reject invalid messages.
- Envelope commands MUST be US-ASCII; receiving systems SHOULD reject non-ASCII commands with 500 syntax error.

## 3. The SMTP Procedures: An Overview
### 3.1 Session Initiation
- Server sends greeting (220) or may reject with 554 (then MUST wait for QUIT and respond 503 to intervening commands).

### 3.2 Client Initiation
- Client sends EHLO (or HELO) identifying itself with its domain name.

### 3.3 Mail Transactions
- Steps: MAIL (sender identification) → RCPT (recipient) → DATA (message).
- **MAIL FROM:<reverse-path>**: starts transaction, resets state; server returns 250 or error (550/553).
- **RCPT TO:<forward-path>**: identifies recipient; can be repeated; server returns 250, 251, or error (550, etc.). If no MAIL precedes RCPT, server MUST return 503.
- **DATA**: server returns 354, then receives message lines until <CRLF>.<CRLF>. After data, server returns 250 OK or error (554, etc.).
- Servers SHOULD NOT reject messages based on RFC 822 header defects; MUST NOT reject due to mismatched Resent-fields.

### 3.4 Forwarding for Address Correction or Updating
- Servers MAY forward silently (250) or inform sender (251/551). If 251/551 used, server MUST NOT assume client will update addresses.
- Servers MUST provide configuration to disable address disclosure via 251/551.

### 3.5 Commands for Debugging Addresses
- **VRFY**: verifies user/mailbox; response (250) MUST include mailbox in pointed brackets.
- **EXPN**: expands mailing list; multiline response with mailboxes.
- Implementations SHOULD support VRFY and EXPN; MAY disable for security.
- A server MUST NOT return 250 unless address actually verified; otherwise return 252 or 502/500.
- Reply code 252 SHOULD be used when address appears valid but cannot be verified in real time.

### 3.6 Domains
- Only resolvable FQDNs permitted in SMTP. Exceptions: EHLO command may use host primary name or address literal; "postmaster" may be used without domain qualification.

### 3.7 Relaying
- Clients SHOULD NOT generate explicit source routes; servers MAY decline relays or strip routes.
- If server accepts relay responsibility but later cannot deliver, it MUST send undeliverable notification to originator (using null reverse-path for notifications).
- Servers MUST NOT send notifications about problems with notification messages.

### 3.8 Mail Gatewaying
- Gateways between mail environments MAY rewrite header fields when necessary.
- Gateways MUST prepend Received: line and MUST NOT alter existing Received: lines.
- Gateways SHOULD accept all valid address formats from Internet side.
- Gateways MUST ensure header addresses satisfy RFC 822 syntax with FQDNs.

### 3.9 Terminating Sessions and Connections
- Client sends QUIT; server responds 221 and closes.
- Server MUST NOT close connection except after QUIT or upon detecting need to shut down (421 response).
- Clients experiencing connection close SHOULD treat as 451 temporary error.

### 3.10 Mailing Lists and Aliases
- Hosts SHOULD support alias and list expansion. For lists, envelope return address MUST be changed to list administrator.
- Servers SHOULD simply use expanded addresses; discarding originator address is discouraged.

## 4. The SMTP Specifications
### 4.1 SMTP Commands
#### 4.1.1 Command Semantics and Syntax
- **EHLO/HELO**: argument is client's FQDN or address literal; servers MUST support HELO.
- **MAIL**: initiates transaction; reverse-path may be null for notification messages.
- **RCPT**: forward-path; clients SHOULD NOT generate source routes; servers MUST recognize but SHOULD strip.
- **DATA**: lines terminated by <CRLF>; end of data is <CRLF>.<CRLF>; servers MUST NOT accept lines ending only in <LF>.
- **RSET**: aborts transaction, clears buffers.
- **VRFY, EXPN, HELP, NOOP, QUIT**: as specified.

#### 4.1.2 Command Argument Syntax
- Reverse-path and forward-path syntax; source routes (A-d-l) MUST BE accepted, SHOULD NOT be generated, SHOULD be ignored.
- Local-part may be Dot-string or Quoted-string; hosts SHOULD avoid requiring quoted-string or case-sensitive local-parts.
- Non-ASCII characters and control characters MUST NOT be used in mailbox names in SMTP commands.

#### 4.1.3 Address Literals
- IPv4: [123.255.37.2]; IPv6: [IPv6:...].

#### 4.1.4 Order of Commands
- Session MUST be initialized with EHLO (or HELO) before mail transaction.
- EHLO may be issued later, resetting state as RSET.
- NOOP, HELP, EXPN, VRFY, RSET may be used at any time.
- MAIL begins transaction; then RCPT(s), then DATA; RSET or new EHLO can abort.
- QUIT must be last command.

#### 4.1.5 Private-use Commands
- Commands starting with "X" may be used bilaterally; server returns 500 if not recognized.

### 4.2 SMTP Replies
- Every command generates exactly one reply.
- Reply codes: 1yz (preliminary), 2yz (success), 3yz (intermediate), 4yz (transient failure), 5yz (permanent failure).
- Second digit: x0z syntax, x1z info, x2z connections, x5z mail system.
- Multiline replies: each line except last begins with code and hyphen.

#### 4.2.2 Reply Codes by Function Groups
- Full list provided in document; key codes: 220, 221, 250, 251, 252, 354, 421, 450-452, 500-504, 550-554.

#### 4.2.5 Reply Codes After DATA
- Positive completion (2yz) after DATA: server accepts responsibility for delivery or notification.
- Permanent error (5yz): server MUST NOT attempt delivery; client retains responsibility.

### 4.3 Sequencing of Commands and Replies
- Alternating dialogue; recipient MUST wait for response before further commands (unless pipelining extension).
- Sequence tables for each command (e.g., EHLO: S:250, E:504/550).

### 4.4 Trace Information
- Server MUST insert Received line at beginning of message content.
- Received line includes FROM (host from EHLO and IP), BY, optional ID/FOR.
- Servers MUST prepend, not change existing lines; MUST use four-digit years.
- Final delivery server inserts Return-path line (from MAIL reverse-path) at start of message data.
- Gateways SHOULD insert Return-path and delete existing ones as appropriate.

### 4.5 Additional Implementation Issues
#### 4.5.1 Minimum Implementation
- Required commands: EHLO, HELO, MAIL, RCPT, DATA, RSET, NOOP, QUIT, VRFY.
- "postmaster" mailbox MUST be supported (case-insensitive) for any domain served; also RCPT TO:<Postmaster> (no domain).

#### 4.5.2 Transparency
- Client inserts extra period at start of line if line begins with period.
- Server removes leading period if line has more characters; single period indicates end of data.

#### 4.5.3 Sizes and Timeouts
- **Size limits**: local-part 64 chars, domain 255, path 256, command line 512, reply line 512, text line 1000, message content at least 64K octets, recipients buffer at least 100.
- Server MUST reject fewer than 100 RCPT with 452 (or 552 as temporary).
- Timeouts: initial 220: 5 min; MAIL/RCPT: 5 min; DATA initiation: 2 min; data block: 3 min; DATA termination: 10 min. Server SHOULD have 5 min timeout awaiting next command.

#### 4.5.4 Retry Strategies
- Sender MUST delay retry; interval at least 30 min; give-up at least 4-5 days.
- Client SHOULD use multi-recipient optimization (one DATA per set of RCPT for same server).
- Server SHOULD support multiple concurrent incoming connections.

#### 4.5.5 Messages with a null reverse-path
- Notifications (DSN, MDN) MUST use null reverse-path.
- Other messages SHOULD use non-null reverse-path.
- Systems SHOULD NOT reply to messages with null reverse-path.

## 5. Address Resolution and Mail Handling
- DNS lookup MUST be performed to resolve domain: first MX records; if none, A record as implicit MX with preference 0.
- If MX found, MUST NOT use A records unless located via MX.
- If MX none usable, report error.
- Client MUST be able to try multiple addresses; SHOULD try at least two.
- Multiple MX records sorted by preference; lower numbers preferred; same preference randomized.
- Multihomed hosts: try IP addresses in order presented.
- Relay host MUST discard its own records from MX list before trying.

## 6. Problem Detection and Handling
### 6.1 Reliable Delivery and Replies by Email
- After accepting message (250 after DATA), server MUST deliver or send notification.
- Notification MUST use null reverse-path; recipient is envelope return path; if null, no notification sent.

### 6.2 Loop Detection
- Servers MUST have provisions for detecting trivial loops; threshold at least 100 Received entries.

### 6.3 Compensating for Irregularities
- Originating SMTP server MAY add message-id, date/time, correct addresses to FQDN.
- Relay SMTP servers MUST NOT perform such fixes.

## 7. Security Considerations
### 7.1 Mail Security and Spoofing
- SMTP mail is inherently insecure; only end-to-end methods (digital signatures) provide authentication.

### 7.2 "Blind" Copies
- SMTP clients and servers SHOULD NOT copy full RCPT set into headers; may send each BCC as separate transaction.

### 7.3 VRFY, EXPN, and Security
- Sites MAY disable VRFY/EXPN; if disabled, MUST return 252.
- Returning 250 with only syntax check violates rule.

### 7.4 Information Disclosure in Announcements
- Implementations SHOULD provide option to disclose type/version for debugging.

### 7.5 Information Disclosure in Trace Fields
- Sites with name disclosure concerns should be aware; FOR clause should be used with caution.

### 7.6 Information Disclosure in Message Forwarding
- Use of 251/551 may disclose sensitive information; configure appropriately.

### 7.7 Scope of Operation of SMTP Servers
- Servers may refuse mail for operational reasons; SHOULD provide capability to limit relay to known sources.

## 8. IANA Considerations
IANA maintains three registries:
1. SMTP service extensions and associated keywords (not starting with "X").
2. Tags for domain literals beyond IPv4/IPv6.
3. Link and protocol identifiers for Received header "via"/"with".

## Normative Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Servers MUST support EHLO even without extensions. | shall | 2.2.1, 4.1.1.1 |
| R2 | Clients SHOULD use EHLO preferentially. | should | 2.2.1 |
| R3 | Non-"X" EHLO keywords MUST correspond to registered extensions. | shall | 2.2.2 |
| R4 | Local-part MUST be treated as case sensitive. | shall | 2.4 |
| R5 | SMTP clients MUST NOT transmit bare CR or LF. | shall | 2.3.7 |
| R6 | Commands MUST use US-ASCII; receiving servers SHOULD reject non-ASCII. | shall/should | 2.4 |
| R7 | MAIL command resets state; if not acceptable, server MUST return permanent or temporary error. | shall | 3.3 |
| R8 | If no MAIL before RCPT, server MUST return 503. | shall | 3.3 |
| R9 | DATA: if no 354, client MUST NOT send message data. | shall | 3.3 |
| R10 | Servers MUST NOT reject messages due to header defects. | shall | 3.3 |
| R11 | Reverse-path may be null for notifications; MUST be set to null for notification messages. | shall | 3.7, 4.5.5 |
| R12 | Gateways MUST prepend Received line and MUST NOT alter existing ones. | shall | 3.8.2 |
| R13 | Server MUST NOT close connection except after QUIT or 421. | shall | 3.9 |
| R14 | Minimum implementation MUST include EHLO, HELO, MAIL, RCPT, DATA, RSET, NOOP, QUIT, VRFY. | shall | 4.5.1 |
| R15 | "postmaster" mailbox MUST be supported for any served domain. | shall | 4.5.1 |
| R16 | Server MUST accept at least 100 RCPT commands per transaction; reject additional with 452. | shall | 4.5.3.1 |
| R17 | Per-command timeouts: initial 220: 5 min; MAIL/RCPT: 5 min; DATA initiation: 2 min; data block: 3 min; DATA termination: 10 min. | should | 4.5.3.2 |
| R18 | Sender MUST delay retry; interval at least 30 min; give-up at least 4-5 days. | shall/should | 4.5.4.1 |
| R19 | Notification messages MUST use null reverse-path. | shall | 4.5.5, 6.1 |
| R20 | DNS lookup MUST resolve domain via MX or A. | shall | 5 |
| R21 | If MX found, SMTP systems MUST NOT use A records unless via MX. | shall | 5 |
| R22 | Client MUST be able to try multiple addresses; SHOULD try at least two. | shall/should | 5 |
| R23 | Server MUST have loop detection; threshold at least 100 Received. | shall | 6.2 |
| R24 | Relay servers MUST NOT perform message fixes; originating servers MAY. | shall | 6.3 |
| R25 | VRFY/EXPN: server MUST NOT return 250 unless actually verified; else 252 or 502/500. | shall | 3.5.3, 7.3 |

## Informative Annexes (Condensed)
- **Appendix A – TCP Transport Service**: 8-bit bytes, high-order bit cleared for ASCII.
- **Appendix B – Generating SMTP Commands from RFC 822 Headers**: Recommendations for deriving MAIL/RCPT from To/Cc/Bcc; includes caution about gatewaying.
- **Appendix C – Source Routes**: Historical use now deprecated; clients SHOULD NOT generate; servers MUST accept but SHOULD strip.
- **Appendix D – Scenarios**: Examples of typical, aborted, relayed, and verifying transactions.
- **Appendix E – Other Gateway Issues**: Gateways should preserve layering; shortcuts cause information loss.
- **Appendix F – Deprecated Features**: TURN, source routing, HELO, #-literals, two-digit years, SEND/SOML/SAML are deprecated or MUST NOT be used.