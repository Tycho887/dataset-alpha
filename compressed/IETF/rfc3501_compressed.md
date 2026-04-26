# RFC 3501: Internet Message Access Protocol – Version 4rev1
**Source**: IETF | **Version**: Standards Track | **Date**: March 2003 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3501

## Scope (Summary)
This document specifies the Internet Message Access Protocol, Version 4rev1 (IMAP4rev1), which allows a client to access and manipulate electronic mail messages on a server, including mailbox manipulation, message flagging, searching, and selective retrieval of message texts and attributes. It supports a single server and is designed for resynchronization by offline clients.

## Normative References
- [ABNF] RFC 2234 (Crocker, Overell)
- [ANONYMOUS] RFC 2245
- [CHARSET] RFC 2978
- [DIGEST-MD5] RFC 2831
- [DISPOSITION] RFC 2183
- [IMAP-TLS] RFC 2595
- [KEYWORDS] RFC 2119
- [LANGUAGE-TAGS] RFC 3066
- [LOCATION] RFC 2557
- [MD5] RFC 1864
- [MIME-HDRS] RFC 2047
- [MIME-IMB] RFC 2045
- [MIME-IMT] RFC 2046
- [RFC-2822] RFC 2822
- [SASL] RFC 2222
- [TLS] RFC 2246
- [UTF-7] RFC 2152
- Informative references: [IMAP-IMPLEMENTATION] RFC 2683, [IMAP-MULTIACCESS] RFC 2180, [IMAP-DISC] (work in progress), [IMAP-MODEL] RFC 1733, [ACAP] RFC 2244, [SMTP] RFC 2821, [IMAP-COMPAT] RFC 2061, [IMAP-HISTORICAL] RFC 1732, [IMAP-OBSOLETE] RFC 2062, [IMAP2] RFC 1176, [RFC-822] STD 11, [RFC-821] STD 10.

## Definitions and Abbreviations
- **Connection**: Entire sequence from establishment to termination of TCP (port 143).
- **Session**: Sequence from mailbox selection (SELECT/EXAMINE) until deselection (SELECT/EXAMINE of another mailbox, CLOSE, or logout).
- **Tag**: Identifier (e.g., A0001) prefixed to each client command.
- **Untagged response**: Prefix "*" – server data not indicating command completion.
- **Tagged response**: Prefix matching command tag – completion result (OK/NO/BAD).
- **Command continuation request**: Prefix "+" – server ready for more data.
- **MUST/MUST NOT/REQUIRED/SHALL/SHALL NOT/SHOULD/SHOULD NOT/MAY/OPTIONAL**: As per [KEYWORDS].
- **Atom**: Non-special characters (excluding atom-specials: "(", ")", "{", SP, CTL, "%", "*", DQUOTE, "\", "]").
- **Number**: 1*DIGIT (32-bit unsigned).
- **String**: Literal `{n} CRLF <n octets>` or quoted string `"<...>"`.
- **Parenthesized list**: `( ... )`.
- **NIL**: Represents non-existence of a string or list.
- **Message attributes**: Unique Identifier (UID), Message Sequence Number, Flags, Internal Date, [RFC-2822] Size, Envelope, Body Structure.
- **UID**: 32-bit, strictly ascending, MUST NOT change during session, SHOULD NOT change between sessions; combined with UIDVALIDITY forms 64-bit immutable identifier.
- **Message Sequence Number**: Relative position 1..N, ordered by ascending UID; can change on expunge.
- **Flags**: System flags (predefined, begin with "\"): \Seen, \Answered, \Flagged, \Deleted, \Draft, \Recent (session-only, cannot be altered by client). Keywords (server-defined, do not begin with "\"). Permanent vs. session-only.
- **Internal Date**: Date/time of message receipt (typically final delivery time for SMTP).
- **Envelope Structure**: Parsed representation of [RFC-2822] header (not same as SMTP envelope).
- **Body Structure**: Parsed [MIME-IMB] body structure.
- **Modified UTF-7**: International mailbox naming, using "&" to shift to modified BASE64, "-" to shift back; printable US-ASCII except "&" represent themselves.

## Protocol Overview
### Link Level
- Assumes reliable data stream (TCP). IMAP4rev1 server listens on port 143.

### Commands and Responses
- Client command → tag + command + arguments CRLF.
- Server → untagged data ("*") and tagged completion (OK/NO/BAD).
- Server data MAY be sent unilaterally; client MUST be prepared to accept any response at all times.
- Servers SHOULD enforce syntax strictly; BAD for protocol errors.

### State and Flow
Four states: Not Authenticated, Authenticated, Selected, Logout.
- Initial greeting: OK (not authenticated), PREAUTH (pre-authenticated), or BYE (rejected).
- Successful LOGIN/AUTHENTICATE → Authenticated.
- Successful SELECT/EXAMINE → Selected.
- CLOSE, failed SELECT/EXAMINE → back to Authenticated.
- LOGOUT or connection close → Logout state.

### Message Attributes (Section 2.3)
- **UID**: MUST NOT change during session; SHOULD NOT change between sessions; UIDVALIDITY MUST increase if UIDs do not persist.
- **Message Sequence Number**: Reassigned on expunge; new messages get next number.
- **Flags**: \Recent is session-only; system flags and keywords.
- **Internal Date**, [RFC-2822] Size, Envelope, Body Structure as defined.

### Data Formats (Section 4)
- Atom, Number, String (literal or quoted), Parenthesized List, NIL.
- 8-bit and binary strings: MUST encode binary (NUL) into textual form (e.g., BASE64); 8-bit characters allowed in literals when CHARSET identified.

### Operational Considerations (Section 5)
- Mailbox names are 7-bit; INBOX case-insensitive reserved.
- Hierarchy delimiter single character; "#" namespace convention.
- Modified UTF-7 for international names; server MUST preserve case of modified BASE64 parts.
- Server MUST send mailbox size updates automatically; MUST NOT send EXISTS that reduces count (only EXPUNGE).
- Autologout timer MUST be at least 30 minutes.
- Client MAY pipeline commands except when ambiguity arises; commands that can cause untagged EXPUNGE (other than FETCH, STORE, SEARCH) require waiting for completion before next sequence number command.

## Client Commands (Section 6)

### Commands Valid in Any State
- **CAPABILITY**: Returns server capabilities (REQUIRED: IMAP4rev1, STARTTLS, LOGINDISABLED, AUTH=PLAIN).
- **NOOP**: Poll for updates; no effect.
- **LOGOUT**: Server MUST send BYE untagged, then OK tagged, then close.

### Commands in Not Authenticated State
- **STARTTLS**: Begin TLS negotiation; server remains not authenticated; client MUST re-issue CAPABILITY after TLS.
- **AUTHENTICATE**: SASL mechanism; service name "imap". Server MUST implement configuration denying plaintext unless STARTTLS or equivalent protection. Client MAY send "*" to cancel.
- **LOGIN**: Plaintext user/password. Server MUST implement configuration where LOGINDISABLED is advertised if no protection; client MUST NOT send LOGIN if LOGINDISABLED advertised.

### Commands in Authenticated State
- **SELECT**: Select mailbox for read-write (or read-only). REQUIRED untagged responses: FLAGS, EXISTS, RECENT; OK untagged: UNSEEN, PERMANENTFLAGS, UIDNEXT, UIDVALIDITY.
- **EXAMINE**: Read-only SELECT; MUST NOT cause loss of \Recent; response MUST begin with [READ-ONLY].
- **CREATE**: Create mailbox; MUST NOT create INBOX; if hierarchy delimiter present, server SHOULD create superior hierarchies.
- **DELETE**: Remove mailbox; MUST NOT remove inferior hierarchies; MUST preserve highest UID of deleted mailbox.
- **RENAME**: Rename mailbox; renames inferiors; special behavior for INBOX (moves messages to new name).
- **SUBSCRIBE / UNSUBSCRIBE**: Manage subscription list; server MUST NOT unilaterally remove names.
- **LIST**: Return mailbox names matching pattern. Empty reference returns hierarchy delimiter/root. Wildcards "*" (any) and "%" (not matching hierarchy delimiter).
- **LSUB**: Return subscribed names; with "%" wildcard, returns \Noselect for unsubscribed parent.
- **STATUS**: Request mailbox status (MESSAGES, RECENT, UIDNEXT, UIDVALIDITY, UNSEEN). MUST NOT be used on selected mailbox; MAY be slow.
- **APPEND**: Append message to end of mailbox; MUST NOT create mailbox if missing (use [TRYCREATE]); if mailbox selected, SHOULD send untagged EXISTS.

### Commands in Selected State
- **CHECK**: Checkpoint mailbox; equivalent to NOOP if no housekeeping.
- **CLOSE**: Permanently remove \Deleted messages; return to authenticated state; no EXPUNGE responses.
- **EXPUNGE**: Remove \Deleted messages; send EXPUNGE untagged per message.
- **SEARCH**: Search mailbox; OPTIONAL CHARSET; returns matching sequence numbers (or UIDs if UID SEARCH). Supports numerous keys (ALL, ANSWERED, BCC, BEFORE, BODY, CC, DELETED, DRAFT, FLAGGED, FROM, HEADER, KEYWORD, LARGER, NEW, NOT, OLD, ON, OR, RECENT, SEEN, SENTBEFORE, SENTON, SENTSINCE, SINCE, SMALLER, SUBJECT, TEXT, TO, UID, UNANSWERED, UNDELETED, UNDRAFT, UNFLAGGED, UNKEYWORD, UNSEEN). Case-insensitive substring matching.
- **FETCH**: Retrieve message data; macros ALL (FLAGS INTERNALDATE RFC822.SIZE ENVELOPE), FAST (FLAGS INTERNALDATE RFC822.SIZE), FULL (FLAGS INTERNALDATE RFC822.SIZE ENVELOPE BODY). BODY with section specifiers (HEADER, HEADER.FIELDS, HEADER.FIELDS.NOT, MIME, TEXT) and partial fetch. BODY.PEEK to avoid setting \Seen.
- **STORE**: Alter flags; FLAGS, FLAGS.SILENT, +FLAGS, +FLAGS.SILENT, -FLAGS, -FLAGS.SILENT. Server SHOULD send FETCH if flags change externally.
- **COPY**: Copy messages to destination mailbox; SHOULD preserve flags and internal date; set \Recent in copy.
- **UID**: Commands using UIDs instead of sequence numbers; for FETCH, STORE, COPY, SEARCH. Non-existent UIDs ignored. FETCH response always includes UID.

### Experimental Commands (X<atom>)
- Must use "X" prefix; untagged responses must also be prefixed with "X".

## Server Responses (Section 7)
### Status Responses
- **OK**: Success (tagged) or informational (untagged). Response codes: ALERT, BADCHARSET, CAPABILITY, PARSE, PERMANENTFLAGS, READ-ONLY, READ-WRITE, TRYCREATE, UIDNEXT, UIDVALIDITY, UNSEEN.
- **NO**: Operation error.
- **BAD**: Protocol error.
- **PREAUTH**: Pre-authenticated greeting.
- **BYE**: Closing connection (normal logout, panic, autologout, or rejected connection).

### Server and Mailbox Status (untagged)
- **CAPABILITY**: Lists server capabilities; MUST include "IMAP4rev1".
- **LIST**: Attributes: \Noinferiors, \Noselect, \Marked, \Unmarked; hierarchy delimiter; name.
- **LSUB**: Same format as LIST.
- **STATUS**: Returns requested status items.
- **SEARCH**: Sequence numbers (or UIDs) matching search.
- **FLAGS**: Flag list applicable to mailbox.

### Mailbox Size Responses
- **EXISTS**: Number of messages; client MUST record.
- **RECENT**: Number of messages with \Recent; client MUST record.

### Message Status Responses
- **EXPUNGE**: Message sequence number removed; client MUST record; MUST NOT be sent during FETCH/STORE/SEARCH or when no command in progress.
- **FETCH**: Message data pairs (BODY, BODYSTRUCTURE, ENVELOPE, FLAGS, INTERNALDATE, RFC822, RFC822.HEADER, RFC822.SIZE, RFC822.TEXT, UID). Static items (ENVELOPE, INTERNALDATE, RFC822*, BODY*, UID) MUST NOT change; dynamic items (FLAGS) MAY change.

### Command Continuation Request
- "+" followed by optional text; used for AUTHENTICATE challenges and literal continuations.

## Security Considerations (Section 11)
- Transactions are sent in clear unless STARTTLS or privacy from AUTHENTICATE is negotiated.
- **STARTTLS**: Client MUST check hostname against server certificate; both MUST verify acceptable auth/privacy.
- Required cipher suite: TLS_RSA_WITH_RC4_128_MD5; SHOULD implement TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA.
- Server MUST implement configuration requiring either STARTTLS or equivalent protection before plaintext passwords, or advertise LOGINDISABLED and reject all plaintext mechanisms.
- AUTHENTICATE error messages SHOULD NOT detail invalid credentials.
- LOGIN error messages SHOULD NOT specify whether user name is invalid.
- Server SHOULD implement rate limiting for failed AUTHENTICATE/LOGIN attempts.

## IANA Considerations
- IMAP4 capabilities registry: http://www.iana.org/assignments/imap4-capabilities
- New capabilities MUST be registered via standards track or IESG-approved experimental RFC.

## Requirements Summary (Commands)
| Command | State | Key Requirement (Excerpt) | Reference |
|---|---|---|---|
| CAPABILITY | Any | Server MUST return "IMAP4rev1" in CAPABILITY response. | 6.1.1 |
| LOGOUT | Any | Server MUST send BYE before OK; client MUST read OK before closing. | 6.1.3 |
| STARTTLS | Not Auth | Server remains in not authenticated state; client MUST discard cached capabilities. | 6.2.1 |
| AUTHENTICATE | Not Auth | Service name "imap"; client MAY cancel with "*". | 6.2.2 |
| LOGIN | Not Auth | Client MUST NOT send if LOGINDISABLED advertised. | 6.2.3 |
| SELECT | Auth | Server MUST send FLAGS, EXISTS, RECENT; required OK codes: UNSEEN, PERMANENTFLAGS, UIDNEXT, UIDVALIDITY. | 6.3.1 |
| EXAMINE | Auth | MUST NOT cause \Recent loss; response begins [READ-ONLY]. | 6.3.2 |
| CREATE | Auth | MUST NOT create INBOX; server SHOULD create superior hierarchies. | 6.3.3 |
| DELETE | Auth | MUST NOT remove inferiors; MUST preserve highest UID. | 6.3.4 |
| RENAME | Auth | Renames inferiors; special INBOX behavior. | 6.3.5 |
| LIST | Auth | Empty reference returns hierarchy delimiter/root. | 6.3.8 |
| LSUB | Auth | With "%" wildcard, returns \Noselect for unsubscribed parent. | 6.3.9 |
| STATUS | Auth | MUST NOT be used on selected mailbox. | 6.3.10 |
| APPEND | Auth | MUST NOT auto-create mailbox; if selected, SHOULD send EXISTS. | 6.3.11 |
| CHECK | Selected | Equivalent to NOOP if no housekeeping. | 6.4.1 |
| CLOSE | Selected | Permanently removes \Deleted; returns to authenticated state; no EXPUNGE responses. | 6.4.2 |
| EXPUNGE | Selected | Sends untagged EXPUNGE per removed message. | 6.4.3 |
| SEARCH | Selected | Server MAY exclude non-text MIME parts; CHARSET support optional. | 6.4.4 |
| FETCH | Selected | BODY.PEEK does not set \Seen; partial fetch syntax. | 6.4.5 |
| STORE | Selected | Server SHOULD send FETCH if flags change externally. | 6.4.6 |
| COPY | Selected | SHOULD preserve flags and internal date; set \Recent in copy. | 6.4.7 |
| UID | Selected | Non-existent UIDs ignored; FETCH response always includes UID. | 6.4.8 |

## Informative Annexes (Condensed)
- **Sample IMAP4rev1 Connection (Section 8)**: Transcript showing login, SELECT, FETCH, STORE, LOGOUT. Illustrates typical command/response flow.
- **Changes from RFC 2060 (Annex B)**: 114 changes including clarification of UID semantics, mandatory SELECT responses, addition of BADCHARSET, STARTTLS and LOGINDISABLED moved from [IMAP-TLS], security updates, and syntax corrections.
- **Key Word Index (Annex C)**: Alphabetical listing of protocol terms with section references (not reproduced here).