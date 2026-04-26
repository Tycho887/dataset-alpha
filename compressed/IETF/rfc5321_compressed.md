# RFC 5321: Simple Mail Transfer Protocol
**Source**: IETF | **Version**: Standards Track | **Date**: October 2008 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc5321

## Scope (Summary)
This document specifies the basic protocol for Internet electronic mail transport, consolidating and clarifying RFC 821, RFC 974, RFC 1123, and RFC 2821. It covers SMTP extension mechanisms and best practices, including use as a mail submission protocol, but does not detail specific extensions. SMTP transfers mail reliably and efficiently over a reliable ordered data stream channel, typically TCP.

## Normative References
- [1] Postel, J., "Simple Mail Transfer Protocol", STD 10, RFC 821, August 1982.
- [2] Mockapetris, P., "Domain names - implementation and specification", STD 13, RFC 1035, November 1987.
- [3] Braden, R., "Requirements for Internet Hosts - Application and Support", STD 3, RFC 1123, October 1989.
- [4] Resnick, P., "Internet Message Format", RFC 5322, October 2008.
- [5] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [6] American National Standards Institute, "USA Code for Information Interchange", ANSI X3.4-1968, 1968.
- [7] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [8] Hinden, R. and S. Deering, "IP Version 6 Addressing Architecture", RFC 4291, February 2006.
- [9] Newman, C., "ESMTP and LMTP Transmission Types Registration", RFC 3848, July 2004.
- [10] Klensin, J., Freed, N., and K. Moore, "SMTP Service Extension for Message Size Declaration", STD 10, RFC 1870, November 1995.
- [11] Klyne, G., Nottingham, M., and J. Mogul, "Registration Procedures for Message Header Fields", BCP 90, RFC 3864, September 2004.

## Definitions and Abbreviations
- **SMTP**: Simple Mail Transfer Protocol.
- **SMTP client**: The sending SMTP process (formerly SMTP-sender).
- **SMTP server**: The receiving SMTP process (formerly SMTP-receiver).
- **Mail object**: Contains an envelope and content (header + body).
- **Envelope**: Originator address, recipient addresses, optional extension material.
- **Content**: Header section and body; textual, US-ASCII repertoire.
- **MTA**: Mail Transfer Agent (SMTP server/client).
- **MUA**: Mail User Agent.
- **Domain name**: Fully-qualified domain name (FQDN); local aliases MUST NOT appear in SMTP.
- **Host**: Computer system supporting SMTP, known by names SHOULD NOT be identified by address literals.
- **Line**: Zero or more characters terminated by <CRLF>.
- **Reverse-path**: Sender mailbox (from MAIL command).
- **Forward-path**: Recipient mailbox (from RCPT command).
- **Relay**: SMTP system that receives mail and transmits it without modification (except trace) to another SMTP server.
- **Gateway**: SMTP system that bridges different transport environments, may transform messages.
- **Mailbox**: Depository for mail; address typically "local-part@domain".
- **EHLO**: Extended HELLO, used to initiate session and request service extensions.
- **HELO**: HELLO, the older initiation command.

## 1. Introduction
### 1.1 Transport of Electronic Mail
- **Objective**: Transfer mail reliably and efficiently.
- SMTP is independent of transmission subsystem, requires a reliable ordered data stream channel.
- Capable of relaying across multiple networks; MX records identify next-hop destinations.

### 1.2 History and Context for This Document
- Consolidates, updates, clarifies RFC 821, RFC 1035, RFC 974, RFC 1123, RFC 1869, RFC 2821.
- Supersedes technically when differs from earlier documents.
- Also contains information for use as "mail submission" protocol; RFC 4409 is now preferred for submission.

### 1.3 Document Conventions
- Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL – interpreted as per RFC 2119. Each use is a conformance requirement.

## 2. The SMTP Model
### 2.1 Basic Structure
- SMTP client establishes two-way transmission channel to SMTP server.
- Client transfers mail messages to one or more SMTP servers or reports failure.
- Server may be ultimate destination or relay/gateway.
- After success response at end of mail data, server MUST accept responsibility for delivery or proper failure reporting.
- Mail transaction: series of commands (MAIL, RCPT, DATA) and replies.
- Encourages one copy of data for all recipients at same destination.
- DNS MX records used to select intermediate hosts.

### 2.2 The Extension Model
#### 2.2.1 Background
- Contemporary SMTP implementations MUST support basic extension mechanisms.
- Servers MUST support EHLO (even without extensions); clients SHOULD preferentially use EHLO.
- Support HELO as fallback.

#### 2.2.2 Definition and Registration of Extensions
- IANA maintains registry of SMTP service extensions.
- Each extension must be defined in a Standards-Track or IESG-approved Experimental RFC.
- Definition must include: textual name, EHLO keyword, syntax/parameters, additional verbs, MAIL/RCPT parameters, description of behavior, increment to command length.
- EHLO keywords starting with "X" are local bilateral; MUST NOT be used in registered extensions.
- Non-"X" keywords MUST correspond to registered extensions.
- Conforming server MUST NOT offer non-"X" keywords not in registered extension.

#### 2.2.3 Special Issues with Extensions
- Extensions can change minimum limits, character set, etc.
- If intermediate system finds next hop does not support required extension, it MAY requeue and try later or alternate MX.
- Timeout to fall back to unextended format SHOULD be less than normal bounce timeout.

### 2.3 SMTP Terminology
#### 2.3.1 Mail Objects
- Mail object: envelope and content.
- Envelope: originator address, recipient addresses, optional extension material.
- Content: header section and body; textual US-ASCII; extensions may relax for body.

#### 2.3.2 Senders and Receivers
- Use "SMTP client" and "SMTP server" throughout; "receiver" and "sender" used for clarity in relay context.

#### 2.3.3 Mail Agents and Message Stores
- SMTP servers/clients act as Mail Transfer Agents (MTAs).
- MUAs are sources and targets; boundaries may be blurred.

#### 2.3.4 Host
- Computer system attached to Internet supporting SMTP.
- Hosts SHOULD NOT be identified by numerical addresses (address literals).

#### 2.3.5 Domain Names
- Domain names consist of labels (letters, digits, hyphens from ASCII).
- Only resolvable, fully-qualified domain names (FQDNs) permitted in SMTP.
- Two exceptions: EHLO command argument (may be address literal if no name) and reserved mailbox "postmaster" may be used without domain.

#### 2.3.6 Buffer and State Table
- SMTP sessions are stateful; model includes virtual buffer and state table.

#### 2.3.7 Commands and Replies
- Commands and data are lines terminated by <CRLF>.
- Reply: numeric completion code (3 digits) plus text.

#### 2.3.8 Lines
- Lines terminated by <CRLF>. Conforming implementations MUST NOT recognize other terminators.
- Bare CR or LF only as part of <CRLF>; client MUST NOT transmit bare CR/LF.

#### 2.3.9 Message Content and Mail Data
- Interchangeable terms for material after DATA acceptance until end of data.

#### 2.3.10 Originator, Delivery, Relay, and Gateway Systems
- Four types: originating, delivery, relay, gateway.
- Firewalls that rewrite addresses are considered gateways.

#### 2.3.11 Mailbox and Address
- Address: character string identifying user or depository.
- Mailbox: depository. Usually "local-part@domain".
- local-part MUST be interpreted only by the domain host.

### 2.4 General Syntax Principles and Transaction Model
- Commands and replies have rigid syntax.
- Verbs and argument values not case sensitive, except mailbox local-part (MUST be treated as case sensitive).
- Commands composed of ASCII characters; unextended SMTP provides 7-bit transport.
- Originating SMTP client that has not negotiated an extension MUST NOT transmit messages with high-order bit set.
- Receiving SMTP servers MAY clear high-order bit or reject.
- 8-bit transmission allowed via 8BITMIME extension; 8BITMIME SHOULD be supported but MUST NOT be used for unrestricted 8-bit.
- Senders MUST NOT send envelope commands in non-US-ASCII; receiving systems SHOULD reject with "500 syntax error".

## 3. The SMTP Procedures: An Overview
### 3.1 Session Initiation
- Client opens connection; server responds with opening message (220).
- Server MAY include software/version information; MAY provide for disabling if security concerns.
- Server MAY reject session with 554 instead of 220; MUST wait for QUIT before closing.

### 3.2 Client Initiation
- Client normally sends EHLO; older systems may use HELO.
- Servers MUST NOT return extended response to HELO.
- If EHLO returns "command not recognized", client SHOULD fall back to HELO.

### 3.3 Mail Transactions
- Three steps: MAIL, one or more RCPT, DATA.
- **MAIL FROM:<reverse-path> [parameters] <CRLF>**: Starts new transaction, resets state. Returns 250 OK or error (550/553). Server MUST return permanent/temporary indication.
- **RCPT TO:<forward-path> [parameters] <CRLF>**: Identifies recipient. Returns 250 OK if accepted, 550 if not deliverable.
- **DATA <CRLF>**: Initiates transfer of message text. Server returns 354, then accepts lines until end-of-data (line containing only "."). After end-of-data, server returns 250 OK.
- Spaces not permitted on either side of colon in MAIL FROM or RCPT TO.
- Server MAY return 503 or 554 in response to DATA if no MAIL or no RCPT.
- Client MUST NOT send data unless 354 received.
- Server SHOULD NOT reject messages based on perceived RFC 822/MIME defects; MUST NOT reject based on Resent-header mismatches.

### 3.4 Forwarding for Address Correction or Updating
- Servers MAY forward messages with address change; MAY use 251 code for update, or "silently" with 250.
- If 251 used, server MUST NOT assume client will update.
- Servers MAY reject with 551 (address update) or 550 (no info).
- Implementations SHOULD provide configuration to disable 251/551 if undesired.

### 3.5 Commands for Debugging Addresses
#### 3.5.1 Overview
- VRFY to verify user name; EXPN to expand mailing list.
- Implementations SHOULD support VRFY and EXPN.
- VRFY success response MUST include mailbox (<local-part@domain>).
- EXPN success response MUST give mailboxes on list.
- Ambiguous VRFY: server MAY note ambiguity or list alternatives.
- EXPN: one mailbox per line.
- VRFY/EXPN MUST include at least recognition of local mailboxes; SHOULD accept "local-part@domain".
- Reply for VRFY of mailing list: positive if delivery to everyone, else error.

#### 3.5.2 VRFY Normal Response
- Reply MUST include <Mailbox> in <local-part@domain> form (FQDN). Addresses SHOULD appear in pointed brackets.
- VRFY and EXPN MUST return only valid domain addresses usable in RCPT.
- Paths (source routes) MUST NOT be returned.
- Server SHOULD support both commands; MAY disable for security.
- If EXPN supported, MUST list in EHLO response; VRFY MAY be listed.

#### 3.5.3 Meaning of VRFY or EXPN Success Response
- Server MUST NOT return 250 unless actually verified address; otherwise 502 or 500.
- If address appears valid but cannot verify in real time, return 252.
- Implementations SHOULD be more aggressive about verification for VRFY.

#### 3.5.4 Semantics and Applications of EXPN
- EXPN useful for debugging mailing lists. Mail systems SHOULD NOT attempt source expansion for duplicate elimination.

### 3.6 Relaying and Mail Routing
#### 3.6.1 Source Routes and Relaying
- SMTP clients SHOULD NOT generate explicit source routes. Servers MAY decline to relay or accept source routes; SHOULD ignore route information and send to final destination.
- SMTP clients MUST NOT generate invalid source routes or depend on serial name resolution.

#### 3.6.2 Mail eXchange Records and Relaying
- Relay server usually target of DNS MX record. If accepts relay, becomes client and sends mail to next SMTP server.
- If declines for policy, SHOULD return 550.
- Server MAY attempt to verify return path but not defined here.

#### 3.6.3 Message Submission Servers as Relays
- Limited-capability clients often send all mail to a single server. Standardized submission protocol (RFC 4409) supersedes SMTP for this role.
- If relay later finds destination incorrect, MUST construct undeliverable notification to originator.
- Notification MUST use null reverse-path in MAIL command.
- Relay SMTP MUST NOT inspect or act upon header or body except to add Received header and optionally detect looping.

### 3.7 Mail Gatewaying
#### 3.7.1 Header Fields in Gatewaying
- Header fields MAY be rewritten when gatewaying; may require inspecting message body.
- When folding envelope info into header, create new fields? Not recommended.

#### 3.7.2 Received Lines in Gatewaying
- Gateway MUST prepend Received line, MUST NOT alter existing Received lines.
- Receiving systems MUST NOT reject mail based on trace header format; SHOULD be robust.

#### 3.7.3 Addresses in Gatewaying
- Gateway SHOULD accept all valid address formats. Generated addresses MUST conform to standards.

#### 3.7.4 Other Header Fields in Gatewaying
- Gateway MUST ensure all header fields meet Internet mail requirements (RFC 5322). All addresses must be FQDN. Translation algorithm SHOULD ensure error messages from foreign environment are sent to envelope reverse-path.

#### 3.7.5 Envelopes in Gatewaying
- When forwarding into Internet, gateway SHOULD set envelope return path from foreign error address if available; default to originator's address.

### 3.8 Terminating Sessions and Connections
- Connection terminated when client sends QUIT; server responds with 221, then closes.
- Server MUST NOT intentionally close connection under normal circumstances except after QUIT, shutdown (421), or timeout.
- Server that closes connections in response to unknown commands is in violation.
- Server forcibly shut down SHOULD attempt to send 421 before exiting.

### 3.9 Mailing Lists and Aliases
#### 3.9.1 Alias
- Expansion: replace pseudo-mailbox with each expanded address, leave other envelope and body unchanged. Deliver/forward to each.

#### 3.9.2 List
- Redistribution: replace pseudo-mailbox, change return address to list administrator. Different from alias by change to backward-pointing address.
- Lists that perform extensive modifications should be viewed as MUAs.

## 4. The SMTP Specifications
### 4.1 SMTP Commands
#### 4.1.1 Command Semantics and Syntax
- Commands: character strings terminated by <CRLF>. Alphabetic characters terminated by <SP> if parameters follow.
- Receivers SHOULD tolerate trailing whitespace before <CRLF>.
- Several commands (RSET, DATA, QUIT) do not permit parameters. Clients MUST NOT send; servers SHOULD reject.

##### 4.1.1.1 Extended HELLO (EHLO) or HELLO (HELO)
- Identifies client. Argument: FQDN of client, or address literal if no meaningful domain.
- SMTP servers identify themselves in greeting and response.
- Client SHOULD start with EHLO. If server does not support extensions, it will error.
- Client MUST issue HELO or EHLO before starting mail transaction.
- EHLO response is multiline with keywords and optional parameters.
- EHLO response MUST contain keywords for all non-required commands (except private-use). Private-use MAY be listed.

##### 4.1.1.2 MAIL (MAIL)
- Initiates mail transaction. Argument: reverse-path (sender mailbox). MAY include optional parameters from extensions.
- Clears all buffers and inserts reverse-path.
- Syntax: `MAIL FROM:Reverse-path [SP Mail-parameters] CRLF`

##### 4.1.1.3 RECIPIENT (RCPT)
- Identifies individual recipient. Multiple RCPT commands.
- Forward-path: destination mailbox. Sending systems SHOULD NOT generate source route. Receiving systems MUST recognize source route syntax but SHOULD strip it.
- Relay hosts SHOULD strip or ignore source routes; names MUST NOT be copied into reverse-path.
- Appends forward-path to buffer.
- Syntax: `RCPT TO:(<Postmaster@Domain> / <Postmaster> / Forward-path) [SP Rcpt-parameters] CRLF`
- "Postmaster" case-insensitive.

##### 4.1.1.4 DATA (DATA)
- Server normally returns 354, then treats lines following as mail data.
- Mail data may contain any ASCII; control characters SHOULD be avoided.
- Terminated by line containing only period: `<CRLF>.<CRLF>`.
- Server MUST NOT treat `<LF>.<LF>` as end-of-data.
- After end-of-data, server processes and returns 250 OK or failure. On 250, server takes full responsibility.
- Receiver inserts trace record (Received line) at top of mail data.

##### 4.1.1.5 RESET (RSET)
- Aborts current mail transaction. Discards stored sender, recipients, mail data. Clears buffers and state.
- Server MUST send "250 OK" to RSET with no arguments.
- Server MUST NOT close connection as result of RSET.

##### 4.1.1.6 VERIFY (VRFY)
- Asks receiver to confirm argument identifies user or mailbox. Returns info per Section 3.5.
- No effect on buffers.
- Syntax: `VRFY SP String CRLF`

##### 4.1.1.7 EXPAND (EXPN)
- Asks receiver to confirm argument identifies mailing list and return membership. Multiline reply.
- No effect on buffers.

##### 4.1.1.8 HELP (HELP)
- Server sends helpful information. May take argument.
- SHOULD support HELP without arguments, MAY with arguments.

##### 4.1.1.9 NOOP (NOOP)
- No action; receiver sends "250 OK".
- No effect on buffers.

##### 4.1.1.10 QUIT (QUIT)
- Server MUST send "221 OK" reply, then close transmission channel.
- Server MUST NOT close until it receives and replies to QUIT.
- Client MUST NOT close until it sends QUIT and SHOULD wait for reply.
- If connection closed prematurely, server MUST cancel pending transaction, act as if temporary error.

##### 4.1.1.11 Mail-Parameter and Rcpt-Parameter Error Responses
- If server does not recognize or implement parameters, return 555.
- If temporarily unable to accommodate, return 455.

#### 4.1.2 Command Argument Syntax
- Formal ABNF provided for Reverse-path, Forward-path, Path, Domain, Mailbox, etc.
- Local-part case-sensitive. For maximum interoperability, hosts SHOULD avoid requiring quoted-string or case-sensitive local-parts.
- Systems MUST NOT define mailboxes requiring non-ASCII or control characters in SMTP commands.
- Characters outside ALPHA, DIGIT, hyphen MUST NOT appear in domain name labels for SMTP. Server MUST reject with 501.

#### 4.1.3 Address Literals
- Allowed when host not known to DNS. Forms: IPv4 (e.g., [123.255.37.2]), IPv6 (e.g., [IPv6:...]), or other standardized tags.
- Standardized-tag MUST be specified in Standards-Track RFC and registered with IANA.

#### 4.1.4 Order of Commands
- Session initialized with EHLO/HELO. SMTP server SHOULD accept non-mail commands without initialization.
- EHLO may be issued later; server MUST clear buffers and reset state as if RSET.
- If EHLO not acceptable, return 501, 500, 502, or 550; server stays in same state.
- MAIL begins transaction. Followed by one or more RCPT, then DATA. Must be in that order.
- Transaction may be aborted by RSET, new EHLO, or QUIT.
- MAIL MUST NOT be sent if transaction already open.
- If transaction beginning command argument not acceptable, 501 failure; server stays in same state.
- QUIT must be last command in session.

#### 4.1.5 Private-Use Commands
- Commands starting with "X" may be used by bilateral agreement. Server that does not recognize replies "500 Command not recognized".
- Non-"X" commands MUST conform to Section 2.2.2.

### 4.2 SMTP Replies
- Every command generates exactly one reply.
- Reply: three-digit code + text. Code for automata, text for humans.
- Exceptions: 220, 221, 251, 421, 551 have machine-parsed text.
- Multiline reply format: code-hyphen for all but last line, code-space for last.
- Server SHOULD send only codes listed; client MUST determine actions by code, not text (except 251, 551, 220, 221, 421).
- Server MUST NOT send reply codes with first digit other than 2,3,4,5. Clients treat out-of-range as fatal.

#### 4.2.1 Reply Code Severities and Theory
- First digit: 2yz (success), 3yz (intermediate), 4yz (transient failure), 5yz (permanent failure).
- Second digit: x0z (syntax), x1z (information), x2z (connections), x5z (mail system).
- Third digit: finer gradation.

#### 4.2.2 Reply Codes by Function Groups
- Listing of codes 500-555 with meanings.

#### 4.2.3 Reply Codes in Numeric Order
- Listing of codes 211-555 in numeric order.

#### 4.2.4 Reply Code 502
- Use when command recognized but not implemented. If not recognized, use 500.
- Extended SMTP systems MUST NOT list capabilities for which they return 502/500.

#### 4.2.5 Reply Codes after DATA and the Subsequent <CRLF>.<CRLF>
- 2yz after DATA: server accepts responsibility for delivery or failure notification.
- 4yz after DATA: server MUST NOT retry; client retains responsibility.
- 5yz after DATA: server MUST NOT retry; client SHOULD NOT retry without user review.

### 4.3 Sequencing of Commands and Replies
#### 4.3.1 Sequencing Overview
- Alternating dialogue; sender MUST wait for response before further commands (unless extensions allow pipelining).
- Sender SHOULD wait for greeting before sending commands.

#### 4.3.2 Command-Reply Sequences
- Listing of possible replies for each command (EHLO, MAIL, RCPT, DATA, RSET, VRFY, EXPN, HELP, NOOP, QUIT) with success/error codes.
- Any command can return 500, 501, 421.

### 4.4 Trace Information
- When SMTP server receives message for delivery/processing, it MUST insert Received line at beginning of content.
- From clause: SHOULD contain both source host name from EHLO and IP address from TCP connection.
- ID clause may contain "@".
- If For clause appears, it MUST contain exactly one <path>.
- An Internet mail program MUST NOT change or delete existing Received lines. Servers MUST prepend, MUST NOT change order.
- Servers SHOULD use explicit offsets in dates, local time with offset.
- When final delivery, server inserts Return-Path line at beginning of mail data.
- Return-path preserves reverse-path from MAIL command. Exactly one SHOULD be present at delivery.
- A message-originating SMTP system SHOULD NOT send message already containing Return-path.
- Relay servers MUST NOT inspect message data for Return-path.
- Final delivery MAY remove existing Return-path before adding its own.
- If only partially successful after DATA, server MUST return OK then compose undeliverable notification. Use null reverse-path.

### 4.5 Additional Implementation Issues
#### 4.5.1 Minimum Implementation
- Required commands: EHLO, HELO, MAIL, RCPT, DATA, RSET, NOOP, QUIT, VRFY.
- Any system supporting relaying/delivery MUST support reserved mailbox "postmaster" as case-insensitive local name. RCPT TO:<Postmaster> (no domain) MUST be supported.
- SMTP systems SHOULD make reasonable effort to accept mail to Postmaster; blocking SHOULD be narrowly tailored.

#### 4.5.2 Transparency
- To allow period at start of line in mail data: client checks first character; if period, inserts extra period. Server checks; if line is single period, end-of-data; if first character is period and others, delete it.
- All ASCII characters to be delivered. If transformations necessary for local storage, MUST be reversible, especially for relayed mail.

#### 4.5.3 Sizes and Timeouts
##### 4.5.3.1 Size Limits and Minimums
- Local-part: max 64 octets.
- Domain: max 255 octets.
- Path (reverse/forward): max 256 octets.
- Command line: max 512 octets.
- Reply line: max 512 octets.
- Text line: max 1000 octets (excluding transparency dot).
- Message content: MUST be at least 64K octets. Server SHOULD implement SIZE extension.
- Recipients buffer: minimum 100 recipients. Rejection with fewer is violation.
- Server imposing limit MUST reject additional addresses orderly; client SHOULD be prepared to transmit in 100-recipient chunks.
- Error codes: 500 (line too long), 501 (path too long), 452 (too many recipients), 552 (too much mail data).
- Correct code for "too many recipients" is 452; clients SHOULD treat 552 as temporary.

##### 4.5.3.2 Timeouts
- Client MUST provide timeout mechanism; per-command timeouts.
- Minimum per-command timeouts SHOULD be:
  - Initial 220 message: 5 minutes
  - MAIL command: 5 minutes
  - RCPT command: 5 minutes
  - DATA initiation (wait for 354): 2 minutes
  - Data block (each TCP SEND): 3 minutes
  - DATA termination (wait for 250): 10 minutes
  - Server timeout (awaiting next command): 5 minutes

#### 4.5.4 Retry Strategies
##### 4.5.4.1 Sending Strategy
- Queuing strategy MUST include per-command timeouts. MUST NOT send error messages in response to error messages.
- Sender MUST delay retrying; retry interval SHOULD be at least 30 minutes; more sophisticated strategies beneficial.
- Retries continue until delivered or sender gives up; give-up time at least 4-5 days.
- Parameters MUST be configurable.
- Client SHOULD keep list of unreachable hosts.
- A single copy of message SHOULD be transmitted for multiple recipients at same server.
- Client MAY support multiple concurrent outgoing transactions.

##### 4.5.4.2 Receiving Strategy
- Server SHOULD keep pending listen on port 25 at all times. Some limit MAY be imposed, but servers that cannot handle more than one transaction are not in conformance.

#### 4.5.5 Messages with a Null Reverse-Path
- Required for non-delivery notifications, DSNs, MDNs. Sent to reverse-path of previous message.
- All other types of messages SHOULD be sent with valid, non-null reverse-path.
- Automated email processors SHOULD NOT reply to messages with null reverse-path, and SHOULD NOT add or change reverse-path when forwarding.

## 5. Address Resolution and Mail Handling
### 5.1 Locating the Target Host
- Once domain identified, DNS lookup MUST be performed. Names expected to be FQDNs.
- SMTP servers for initial submission SHOULD NOT make FQDN inferences; relay MUST NOT.
- Lookup first attempts MX record. If CNAME, process resulting name. If non-existent domain error, report error. If temporary error, queue and retry. If empty list of MX, treat as implicit MX with preference 0 pointing to that host.
- If MX records present, MUST NOT use address RRs for that name unless located using MX. Implicit MX only if no MX records.
- MX data field MUST contain domain name; query for that domain MUST return at least one address RR. CNAME not allowed.
- SMTP client MUST try (and retry) each alternate address in list until success. SHOULD try at least two.
- MX preference: lower numbers more preferred. If same preference, sender MUST randomize.
- If multihomed, resolver must order addresses; sender MUST try in order.
- If SMTP server is designated MX, it MAY relay, deliver, or hand off. If relay, MUST sort MX records, discard those matching its own names/addresses at same or higher preference. If no records left, error and return as undeliverable.

### 5.2 IPv6 and MX Records
- Host domains may contain A (IPv4) and AAAA (IPv6) RRs. Appropriate actions depend on local circumstances; designers should study procedures and provide mechanisms for operational tuning.

## 6. Problem Detection and Handling
### 6.1 Reliable Delivery and Replies by Email
- After accepting mail (250 OK to DATA), server takes responsibility. MUST NOT lose message for frivolous reasons.
- If delivery failure after acceptance, server MUST formulate and mail notification with null reverse-path. Recipient MUST be address from envelope return path (or Return-Path). If that address is null, MUST NOT send notification.
- If explicit source route, strip down to final hop.
- Server MUST seek to minimize response time to final <CRLF>.<CRLF> to avoid duplicates.

### 6.2 Unwanted, Unsolicited, and "Attack" Messages
- Principles of delivery over rejection are strained by volume of undesired mail. Dropping mail without notification is permitted but extremely dangerous; should be considered only with high confidence of serious fraud.
- If rejecting for hostile content, bounce SHOULD NOT be sent unless confident of useful delivery.

### 6.3 Loop Detection
- Counting Received header fields is effective. Server using this SHOULD use threshold of at least 100.
- Servers MUST contain provisions for detecting and stopping trivial loops.

### 6.4 Compensating for Irregularities
- Changes to message MAY be applied by originating SMTP server or submission server: addition of Message-ID, Date, time zone; correction of addresses to FQDN.
- These changes MUST NOT be applied by relay servers.
- Properly operating clients supplying correct information are preferred.

## 7. Security Considerations
### 7.1 Mail Security and Spoofing
- SMTP is inherently insecure. End-to-end methods (digital signatures) are real security.
- Transport-level authentication improves situation but remains inherently weaker.
- Efforts to prevent users from setting envelope return path and header From fields to other valid addresses are misguided.

### 7.2 "Blind" Copies
- SMTP clients and servers SHOULD NOT copy full set of RCPT command arguments into header section.
- Sending systems may send each blind copy as separate transaction with single RCPT.
- Receiving systems SHOULD NOT deduce relationships and alter header section. "Apparently-to" header field is a violation and SHOULD NOT be used.

### 7.3 VRFY, EXPN, and Security
- Sites MAY disable VRFY/EXPN for security. If disabled, server MUST return 252, not confusing codes.
- Returning 250 after only syntax check violates rule.
- EXPN can be used to harvest addresses; implementations SHOULD still support but sites SHOULD evaluate tradeoffs.

### 7.4 Mail Rerouting Based on the 251 and 551 Response Codes
- Before updating behavior based on 251/551, client should be certain of server authenticity to avoid man-in-the-middle.

### 7.5 Information Disclosure in Announcements
- Implementations SHOULD minimally provide for making type and version information available in some way.

### 7.6 Information Disclosure in Trace Fields
- Trace fields may disclose host names; sites with disclosure concerns should be aware. Optional FOR clause should be supplied with caution.

### 7.7 Information Disclosure in Message Forwarding
- Using 251/551 to identify replacement address may disclose sensitive information. Sites should configure servers appropriately.

### 7.8 Resistance to Attacks
- Servers may detect attacks (e.g., many invalid RCPT TO) and close connection after appropriate number of 5yz replies.

### 7.9 Scope of Operation of SMTP Servers
- SMTP server may refuse mail for operational/technical reasons. But excessive rejection threatens ubiquity.
- Implementations SHOULD provide capability to limit relay function to known sources. When rejecting for policy, use 550 with EHLO/MAIL/RCPT.

## 8. IANA Considerations
- IANA maintains three registries:
  1. SMTP Service Extensions – only non-"X" keywords from Standards-Track or IESG-approved Experimental.
  2. Address Literal Tags – tags for domain literals other than IPv4.
  3. Mail Transmission Types – link and protocol identifiers for Received header (via/with). Additional registered clauses added.
- All new trace header fields must be added to IANA registry per BCP 90 (RFC 3864).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | SMTP servers MUST accept responsibility for delivery or proper failure reporting after success response at end of mail data. | MUST | Section 2.1 |
| R2 | Contemporary SMTP implementations MUST support the basic extension mechanisms (EHLO). | MUST | Section 2.2.1 |
| R3 | SMTP servers MUST support the EHLO command even if they do not implement any specific extensions. | MUST | Section 2.2.1 |
| R4 | SMTP clients and servers MUST support the original HELO mechanisms as a fallback. | MUST | Section 2.2.1 |
| R5 | A conforming server MUST NOT offer non-"X"-prefixed EHLO keyword values that are not described in a registered extension. | MUST NOT | Section 2.2.2 |
| R6 | Local aliases MUST NOT appear in any SMTP transaction. | MUST NOT | Section 2.3.5 |
| R7 | Conforming implementations MUST NOT recognize or generate any line terminator other than <CRLF>. | MUST NOT | Section 2.3.8 |
| R8 | SMTP client implementations MUST NOT transmit bare CR or LF characters except as part of <CRLF>. | MUST NOT | Section 2.3.8 |
| R9 | The local-part of a mailbox MUST BE treated as case sensitive by SMTP implementations. | MUST | Section 2.4 |
| R10 | An originating SMTP client that has not successfully negotiated an extension MUST NOT transmit messages with information in the high-order bit of octets. | MUST NOT | Section 2.4 |
| R11 | SMTP servers MUST NOT return the extended EHLO-style response to a HELO command. | MUST NOT | Section 3.2 |
| R12 | The MAIL command clears the reverse-path buffer, the forward-path buffer, and the mail data buffer. | MUST | Section 4.1.1.2 |
| R13 | Servers MUST be prepared to encounter source routes in forward-path but SHOULD ignore them. | MUST/SHOULD | Section 3.3 |
| R14 | If a RCPT command appears without a previous MAIL command, the server MUST return a 503 response. | MUST | Section 3.3 |
| R15 | After end-of-data indication, server MUST send an OK reply if successful. | MUST | Section 4.1.1.4 |
| R16 | SMTP servers MUST NOT close the connection as the result of receiving a RSET. | MUST NOT | Section 4.1.1.5 |
| R17 | The QUIT command MUST cause the receiver to send a "221 OK" reply and close the transmission channel. | MUST | Section 4.1.1.10 |
| R18 | SMTP servers MUST NOT intentionally close the transmission channel until it receives and replies to a QUIT command. | MUST NOT | Section 4.1.1.10 |
| R19 | An SMTP server MUST NOT intentionally close the connection under normal operational circumstances except as specified. | MUST NOT | Section 3.8 |
| R20 | Any system that includes an SMTP server supporting mail relaying or delivery MUST support the reserved mailbox "postmaster". | MUST | Section 4.5.1 |
| R21 | The maximum total length of a reverse-path or forward-path is 256 octets. | MUST | Section 4.5.3.1.3 |
| R22 | The maximum total length of a command line including <CRLF> is 512 octets. | MUST | Section 4.5.3.1.4 |
| R23 | The maximum total length of a text line including <CRLF> is 1000 octets (excluding transparency dot). | MUST | Section 4.5.3.1.6 |
| R24 | The minimum total number of recipients that MUST be buffered is 100 recipients. | MUST | Section 4.5.3.1.8 |
| R25 | An SMTP client MUST provide a timeout mechanism with per-command timeouts. | MUST | Section 4.5.3.2 |
| R26 | Any queuing strategy MUST include timeouts on all activities on a per-command basis. | MUST | Section 4.5.4 |
| R27 | Any queuing strategy MUST NOT send error messages in response to error messages. | MUST NOT | Section 4.5.4 |
| R28 | The sender MUST delay retrying a particular destination after one attempt has failed (retry interval SHOULD be at least 30 minutes). | MUST | Section 4.5.4.1 |
| R29 | Retries continue until message transmitted or sender gives up; give-up time at least 4-5 days. | MUST | Section 4.5.4.1 |
| R30 | The parameters to the retry algorithm MUST be configurable. | MUST | Section 4.5.4.1 |
| R31 | The SMTP server MUST insert trace (Received) information at the beginning of the message content. | MUST | Section 4.4 |
| R32 | An Internet mail program MUST NOT change or delete a Received line that was previously added. | MUST NOT | Section 4.4 |
| R33 | SMTP servers MUST prepend Received lines; they MUST NOT change the order of existing lines. | MUST | Section 4.4 |
| R34 | A server MUST NOT return a 250 code in response to VRFY or EXPN unless it has actually verified the address. | MUST NOT | Section 3.5.3 |
| R35 | Systems MUST NOT define mailboxes in such a way as to require the use in SMTP of non-ASCII characters or control characters. | MUST NOT | Section 4.1.2 |
| R36 | Characters outside ALPHA, DIGIT, hyphen MUST NOT appear in domain name labels for SMTP clients or servers. | MUST NOT | Section 4.1.2 |
| R37 | SMTP servers that receive a command with invalid character codes MUST reject with 501 (unless overridden by extension). | MUST | Section 4.1.2 |
| R38 | EHLO response MUST contain keywords for all commands not listed as "required" in Section 4.5.1 except private-use commands. | MUST | Section 4.1.1.1 |
| R39 | MAIL command clears buffers and inserts reverse-path. | MUST | Section 4.1.1.2 |
| R40 | RCPT command appends forward-path to buffer; does not change other buffers. | MUST | Section 4.1.1.3 |
| R41 | DATA command causes mail data to be appended to mail data buffer. | MUST | Section 4.1.1.4 |
| R42 | RSET discards all stored sender, recipients, and mail data; clears buffers and state tables. | MUST | Section 4.1.1.5 |
| R43 | QUIT aborts any current uncompleted mail transaction. | MUST | Section 4.1.1.10 |

## Informative Annexes (Condensed)
- **Appendix A. TCP Transport Service**: SMTP over TCP uses 8-bit bytes with 7-bit ASCII characters (high-order bit cleared). Extensions may allow full 8-bit data.
- **Appendix B. Generating SMTP Commands from RFC 822 Header Fields**: Recommendations for generating SMTP commands from header fields when envelope not supplied. Avoid gatewaying using only header fields to prevent loops.
- **Appendix C. Source Routes**: Historical background; source routes (e.g., @ONE,@TWO:JOE@THREE) are deprecated. Servers MUST accept but SHOULD ignore; clients SHOULD NOT generate.
- **Appendix D. Scenarios**: Example SMTP sessions: typical transaction, aborted transaction, relayed mail (two steps), verifying and sending. Illustrates command-reply sequences.
- **Appendix E. Other Gateway Issues**: Gateways should preserve layering semantics between mail systems. Information loss is almost inevitable when environments differ.
- **Appendix F. Deprecated Features of RFC 821**: TURN (security issues), Source Routing (obsoleted by MX), HELO (use EHLO instead), #-literals (obsolete), Dates/Years (four-digit years required, two-digit deprecated), Sending vs Mailing (SEND/SOML/SAML rarely implemented; clients SHOULD NOT provide them).