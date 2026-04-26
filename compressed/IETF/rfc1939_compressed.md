# RFC 1939: Post Office Protocol - Version 3
**Source**: IETF Network Working Group | **Version**: STD 53 | **Date**: May 1996 | **Type**: Normative Standards Track
**Original**: RFC 1939 (https://www.rfc-editor.org/rfc/rfc1939)

## Scope (Summary)
POP3 enables a workstation to dynamically access a maildrop on a server host to retrieve mail, typically downloading and then deleting messages. It is not intended for extensive server-side mail manipulation; a more advanced protocol, IMAP4, is defined in RFC 1730.

## Normative References
- [RFC 821] Postel, J., "Simple Mail Transfer Protocol", STD 10, RFC 821, August 1982.
- [RFC 822] Crocker, D., "Standard for the Format of ARPA-Internet Text Messages", STD 11, RFC 822, August 1982.
- [RFC 1321] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [RFC 1730] Crispin, M., "Internet Message Access Protocol - Version 4", RFC 1730, December 1994.
- [RFC 1734] Myers, J., "POP3 AUTHentication command", RFC 1734, December 1994.

## Definitions and Abbreviations
- **client host**: a host making use of the POP3 service.
- **server host**: a host which offers the POP3 service.
- **maildrop**: the repository on the server holding mail for a user.
- **message-number**: a decimal number assigned to each message, starting at 1, in the order they appear in the maildrop.
- **scan listing**: a line containing the message-number and exact size in octets (e.g., "1 120").
- **drop listing**: a line containing the number of messages and total size of the maildrop (e.g., "+OK 2 320").
- **unique-id listing**: a line containing the message-number and a server-determined unique identifier.
- **byte-stuffing**: when a line in a multi-line response begins with the termination octet ('.'), an extra '.' is prepended.
- **CRLF**: Carriage Return Line Feed pair.

## 1. Introduction (Informative Summary)
POP3 addresses the inability of smaller nodes to maintain a full MTS; they can use a POP3 server to retrieve mail held in a maildrop. The protocol is not intended for extensive server manipulation; IMAP4 is a more advanced alternative.

## 2. A Short Digression (Informative Summary)
A consistent method: a client host enters mail into the transport system via an SMTP connection to its relay host (which may be the POP3 server or another host).

## 3. Basic Operation
- The POP3 server listens on TCP port 110. The client establishes a TCP connection; the server sends a greeting.
- **Commands**: case-insensitive keyword (3 or 4 characters) possibly followed by arguments, separated by SPACE, terminated by CRLF. Arguments up to 40 characters.
- **Responses**: status indicator ("+OK" or "-ERR") followed by keyword and text, terminated by CRLF. Up to 512 characters including CRLF.
- **[R1] Servers MUST send "+OK" and "-ERR" in upper case.**
- **Multi-line responses**: after the first CRLF, additional lines are sent, each terminated by CRLF. The response ends with a line containing only the termination octet ('.') and CRLF ("CRLF.CRLF"). If a line begins with '.', it is byte-stuffed by prepending another '.'.
- **Session states**: AUTHORIZATION (client identifies itself), TRANSACTION (client requests actions), UPDATE (server releases resources and says goodbye). QUIT command transitions from TRANSACTION to UPDATE.
- **[R2] Servers MUST respond to an unrecognized, unimplemented, or syntactically invalid command with a negative status indicator.**
- **[R3] Servers MUST respond to a command issued when the session is in an incorrect state with a negative status indicator.**
- **[R4] A POP3 server MAY have an inactivity autologout timer. Such a timer MUST be of at least 10 minutes' duration.**
- **[R5] When the timer expires, the session does NOT enter the UPDATE state—the server should close the TCP connection without removing any messages or sending any response to the client.** (Note: "should" as per RFC language.)

## 4. The AUTHORIZATION State
- Server issues a one-line greeting (positive response).
- Client must authenticate using at least one mechanism (USER/PASS or APOP as defined; also RFC 1734).
- Upon successful authentication, server acquires an exclusive-access lock on the maildrop and responds with "+OK". Session enters TRANSACTION state with no messages marked deleted.
- If maildrop cannot be opened (e.g., lock failure), server responds with "-ERR". **[R6] If a lock was acquired but the POP3 server intends to respond with a negative status indicator, the POP3 server must release the lock prior to rejecting the command.**
- After a negative response, the connection may be closed; client may issue a new authentication command or QUIT.
- **Message-number assignment**: first message is "1", second "2", etc. All message-numbers and sizes expressed in decimal.

### QUIT Command (in AUTHORIZATION state)
- Arguments: none
- Restrictions: none
- Possible Responses: +OK
- Example: `C: QUIT` `S: +OK dewey POP3 server signing off`

## 5. The TRANSACTION State
- Client may issue any of the following commands repeatedly. Eventually QUIT transitions to UPDATE.

### STAT Command
- Arguments: none
- Restrictions: only in TRANSACTION state
- Discussion: Server issues "+OK" followed by a single space, the number of messages, a single space, and the size of the maildrop in octets. This is a "drop listing". No additional information required, but memo STRONGLY discourages extra info.
- **[R7] Messages marked as deleted are not counted in either total.**
- Possible Responses: +OK nn mm
- Example: `C: STAT` `S: +OK 2 320`

### LIST [msg] Command
- Arguments: optional message-number (must not refer to a deleted message)
- Restrictions: only in TRANSACTION state
- Discussion: With argument, server returns a scan listing for that message. Without argument, multi-line response: each line is a scan listing (message-number and size). If no messages, response is "+OK" followed by termination line.
- **[R8] Scan listing format: message-number SPACE exact size in octets.** No additional info required; STRONGLY discouraged.
- Messages marked as deleted are not listed.
- Possible Responses: +OK scan listing follows; -ERR no such message
- Examples: `LIST` (multi-line), `LIST 2`

### RETR msg Command
- Arguments: message-number (required, must not refer to deleted message)
- Restrictions: only in TRANSACTION state
- Discussion: Multi-line response containing the message, byte-stuffed.
- Possible Responses: +OK message follows; -ERR no such message
- Example: `RETR 1`

### DELE msg Command
- Arguments: message-number (required, must not refer to deleted message)
- Restrictions: only in TRANSACTION state
- Discussion: Server marks message as deleted. Future reference to that message-number generates error. Message is not actually deleted until UPDATE state.
- Possible Responses: +OK message deleted; -ERR no such message
- Example: `DELE 1`

### NOOP Command
- Arguments: none
- Restrictions: only in TRANSACTION state
- Discussion: Server does nothing, replies with positive response.
- Possible Responses: +OK

### RSET Command
- Arguments: none
- Restrictions: only in TRANSACTION state
- Discussion: If any messages marked as deleted, they are unmarked. Server replies with positive response.
- Possible Responses: +OK

## 6. The UPDATE State
- Entered when client issues QUIT from TRANSACTION state. (QUIT from AUTHORIZATION terminates without entering UPDATE.)
- **[R14] If session terminates other than by client-issued QUIT, server MUST NOT enter UPDATE state and MUST NOT remove any messages.**

### QUIT Command (in UPDATE state)
- Arguments: none
- Restrictions: none
- Discussion: **[R15] Server removes all messages marked as deleted from maildrop and replies. If error (e.g., resource shortage), some or none of marked messages may be removed; server MUST NOT remove any messages not marked as deleted.** Server then releases the exclusive-access lock and closes TCP connection.
- Possible Responses: +OK; -ERR some deleted messages not removed
- Examples: `C: QUIT` `S: +OK dewey POP3 server signing off (maildrop empty)`

## 7. Optional POP3 Commands
- **[R16] The following commands must be supported by all minimal implementations: USER, PASS, QUIT, STAT, LIST, RETR, DELE, NOOP, RSET, QUIT.**
- The optional commands below provide greater freedom. (Memo STRONGLY encourages implementing these instead of augmented drop/scan listings.)

### TOP msg n Command
- Arguments: message-number (required, must not refer to deleted message) and non-negative number of lines (required)
- Restrictions: only in TRANSACTION state
- Discussion: Multi-line response: headers, blank line separating headers from body, then the first n lines of the body. If n exceeds number of lines in body, entire message is sent.
- Possible Responses: +OK top of message follows; -ERR no such message
- Example: `TOP 1 10`

### UIDL [msg] Command
- Arguments: optional message-number (must not refer to deleted message)
- Restrictions: only in TRANSACTION state
- Discussion: With argument, returns unique-id listing (message-number SPACE unique-id). Without argument, multi-line response listing each message's unique-id. **[R18] Unique-id is a server-determined string of 1 to 70 characters (range 0x21 to 0x7E) that uniquely identifies a message within the maildrop and persists across sessions.** **[R19] Server should never reuse a unique-id in a given maildrop.** Messages marked as deleted are not listed.
- Possible Responses: +OK unique-id listing follows; -ERR no such message
- Examples: `UIDL` (multi-line), `UIDL 2`

### USER name Command
- Arguments: string identifying a mailbox (required)
- Restrictions: only in AUTHORIZATION state after greeting or after unsuccessful USER/PASS
- Discussion: First part of USER/PASS authentication. If server responds "+OK", client may issue PASS or QUIT. If "-ERR", client may issue a new authentication command or QUIT. Server may return positive even if no such mailbox. Server may return negative if mailbox exists but does not permit plaintext password.
- Possible Responses: +OK name is a valid mailbox; -ERR never heard of mailbox name
- Example: `USER mrose`

### PASS string Command
- Arguments: server/mailbox-specific password (required)
- Restrictions: **[R20] may only be given in AUTHORIZATION state immediately after a successful USER command**
- Discussion: Server uses USER and PASS arguments to authenticate. Spaces in the argument may be treated as part of the password.
- Possible Responses: +OK maildrop locked and ready; -ERR invalid password; -ERR unable to lock maildrop
- Example: `PASS secret`

### APOP name digest Command
- Arguments: mailbox name (required) and MD5 digest string (required)
- Restrictions: may only be given in AUTHORIZATION state after greeting or after unsuccessful USER/PASS
- Discussion: Alternative authentication providing origin authentication and replay protection without sending password in clear. **[R21] Server includes a timestamp (unique and changing each time) in its greeting (syntax like msg-id in RFC 822). Client computes digest = MD5(timestamp + shared secret) and sends APOP command.** Server verifies digest. If correct, session enters TRANSACTION state. Shared secret should be long. The digest is 16 octets sent as lowercase hex.
- Possible Responses: +OK maildrop locked and ready; -ERR permission denied
- Example: `APOP mrose c4c9334bac560ecc979e58001b3e22fb`

## 8. Scaling and Operational Considerations (Informative Summary)
Large-scale commercial post offices have used UIDL and not issuing DELE to simulate weak IMAP functionality. This leads to accumulation of read messages, which is undesirable. Recommended server operator options:
- Impose per-user storage quota, informing users of quota status.
- Enforce site message retention policy (e.g., delete unread after 60 days, read after 7 days). Such deletions are outside POP3 protocol scope, but operators should inform users. Clients must not assume site policy automates deletions; they should use DELE explicitly. One special policy: download-and-delete (delete messages after RETR and QUIT). Servers should not delete on abnormal termination (no QUIT). They may disable TOP in such cases.

## 9. POP3 Command Summary
### Minimal POP3 Commands (must be implemented):
- **AUTHORIZATION state**: USER name, PASS string, QUIT
- **TRANSACTION state**: STAT, LIST [msg], RETR msg, DELE msg, NOOP, RSET, QUIT
### Optional POP3 Commands:
- **AUTHORIZATION state**: APOP name digest
- **TRANSACTION state**: TOP msg n, UIDL [msg]
### POP3 Replies: +OK, -ERR
Text after "+OK" or "-ERR" may be ignored by client (except for STAT, LIST, UIDL where structure matters).

## 10. Example POP3 Session (Informative)
(Example session using APOP, STAT, LIST, RETR, DELE, QUIT. Not reproduced; see original.)

## 11. Message Format
All messages transmitted during a POP3 session are assumed to conform to RFC 822. The octet count for a message may differ from local end-of-line conventions. The server calculates size by counting each internal end-of-line as two octets. Lines starting with termination octet need not (and must not) be counted twice due to byte-stuffing.

## 12. References (Informative)
Listed in Normative References section.

## 13. Security Considerations
- Use of APOP provides origin identification and replay protection.
- **[R22] A POP3 server which implements both PASS and APOP should not allow both methods for a given user.** (As per change from RFC 1725.)
- Longer shared secrets increase difficulty of deriving them.
- Servers that answer -ERR to USER command give attackers clues about valid names.
- PASS command sends passwords in clear over network.
- RETR and TOP commands send mail in clear over network.

## 14. Acknowledgements (Informative)
POP3 family history; contributions: Alfred Grimstad, Keith McCloghrie, Neil Ostroff.

## 15. Authors' Addresses (Informative)
John G. Myers, Carnegie-Mellon University. Marshall T. Rose, Dover Beach Consulting, Inc.

## Appendix A: Differences from RFC 1725 (Informative Summary)
Changes: clarified case-insensitivity, upper case responses, greeting format, behavior for unimplemented commands, made USER/PASS optional, clarified order and restrictions, UID persistence and length limit, status indicator length limit, LIST empty mailbox returns success, added references, clarified TOP's second argument, changed "must" to "should" for APOP/PASS coexistence, added scaling section.

## Appendix B: Command Index (Informative)
Index of command pages (omitted).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Servers MUST send "+OK" and "-ERR" in upper case. | shall | Section 3, Basic Operation |
| R2 | Servers MUST respond to an unrecognized, unimplemented, or syntactically invalid command with a negative status indicator. | shall | Section 3, Basic Operation |
| R3 | Servers MUST respond to a command issued in an incorrect state with a negative status indicator. | shall | Section 3, Basic Operation |
| R4 | A POP3 server MAY have an inactivity autologout timer. Such a timer MUST be of at least 10 minutes' duration. | shall/may | Section 3, Basic Operation |
| R5 | When the timer expires, the session does NOT enter the UPDATE state—the server should close the TCP connection without removing any messages or sending any response to the client. | should | Section 3, Basic Operation |
| R6 | If a lock was acquired but the POP3 server intends to respond with a negative status indicator, the POP3 server must release the lock prior to rejecting the command. | shall | Section 4, AUTHORIZATION State |
| R7 | Messages marked as deleted are not counted in either total in STAT response. | shall (implied) | Section 5, STAT |
| R8 | In LIST, scan listing format: message-number SPACE exact size in octets. | shall | Section 5, LIST |
| R9 | This memo STRONGLY discourages implementations from supplying additional information in the drop listing. | should (strong) | Section 5, STAT |
| R10 | This memo STRONGLY discourages implementations from supplying additional information in the scan listing. | should (strong) | Section 5, LIST |
| R11 | In RETR, response is multi-line, byte-stuffed. | shall (implied) | Section 5, RETR |
| R12 | DELE marks message as deleted; actual deletion occurs in UPDATE state. | shall | Section 5, DELE |
| R13 | RSET unmarks all deleted messages. | shall | Section 5, RSET |
| R14 | If session terminates other than by client-issued QUIT, server MUST NOT enter UPDATE state and MUST NOT remove any messages. | shall | Section 6, UPDATE State |
| R15 | In QUIT (UPDATE), server removes all messages marked as deleted; in no case may the server remove any messages not marked as deleted. | shall | Section 6, QUIT |
| R16 | The following commands must be supported by all minimal implementations: USER, PASS, QUIT, STAT, LIST, RETR, DELE, NOOP, RSET, QUIT. | shall | Section 7, Optional POP3 Commands |
| R17 | TOP command: arguments are message-number and non-negative number of lines. | shall | Section 7, TOP |
| R18 | UIDL unique-id is a server-determined string of one to 70 characters in the range 0x21 to 0x7E, uniquely identifies a message within a maildrop and persists across sessions. | shall | Section 7, UIDL |
| R19 | Server should never reuse a unique-id in a given maildrop. | should | Section 7, UIDL |
| R20 | PASS may only be given in AUTHORIZATION state immediately after a successful USER command. | shall | Section 7, PASS |
| R21 | APOP digest is calculated by applying MD5 to timestamp (including angle-brackets) followed by shared secret. The timestamp MUST be different each time the POP3 server issues a banner greeting. | shall/must | Section 7, APOP |
| R22 | A POP3 server which implements both PASS and APOP should not allow both methods for a given user. | should | Section 13, Security |
| R23 | All messages transmitted during a POP3 session are assumed to conform to RFC 822. | shall (by reference) | Section 11, Message Format |