# RFC 3977: Network News Transfer Protocol (NNTP)
**Source**: IETF (Standards Track) | **Version**: RFC 3977 (Obsoletes RFC 977, Updates RFC 2980) | **Date**: October 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc3977/

## Scope (Summary)
This document specifies the Network News Transfer Protocol (NNTP) for the distribution, inquiry, retrieval, and posting of Netnews articles over a reliable stream-based mechanism. It replaces RFC 977, clarifies ambiguities, adds new base functionality (e.g., CAPABILITIES command, mandatory commands), and provides a mechanism for standardized extensions.

## Normative References
- [ANSI1986] ANSI X3.4, "Coded Character Set – 7-bit American Standard Code for Information Interchange", 1986.
- [RFC977] Kantor, B. and P. Lapsley, "Network News Transfer Protocol", RFC 977, February 1986.
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One", RFC 2045, November 1996.
- [RFC2047] Moore, K., "MIME Part Three: Message Header Extensions for Non-ASCII Text", RFC 2047, November 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC4234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, October 2006.
- [TF.686-1] ITU-R Recommendation TF.686-1, "Glossary", October 1997.
- [NNTP-AUTH] Vinocur, J. et al., "NNTP Extension for Authentication", RFC 4643, October 2006.
- [NNTP-STREAM] Vinocur, J. and K. Murchison, "NNTP Extension for Streaming Feeds", RFC 4644, October 2006.
- [NNTP-TLS] Murchison, K. et al., "Using TLS with NNTP", RFC 4642, October 2006.

## Definitions and Abbreviations
- **MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / MAY / OPTIONAL**: As defined in RFC 2119.
- **client / server**: Host using NNTP service / host offering NNTP service.
- **message-id**: Unique identifier for an article, enclosed in angle brackets, 3–250 octets, printable US-ASCII.
- **wildmat**: Pattern matching format as defined in Section 4.
- **CRLF**: Sequence %x0D.0A.
- **keyword**: US-ASCII letters, digits, dot, dash; at least 3 characters, beginning with a letter.
- **capability**: A set of related facilities (e.g., READER, IHAVE).
- **extension**: Package of associated facilities defining at least one new capability label.
- **metadata**: Data about an article not in the article itself; names begin with colon.
- **pipelining**: Sending commands before receiving responses to previous ones.
- **dot-stuffing**: In multi-line blocks, each line beginning with "." is prepended with an extra ".".

## 1. Introduction
- NNTP used for distribution, inquiry, retrieval, posting of Netnews articles via reliable stream.
- Key changes from RFC 977: default charset changed to UTF-8; some optional commands now mandatory; added CAPABILITIES command.
- Normative language per RFC 2119.
- Compliance: "unconditionally compliant" satisfies all MUST and SHOULD; "conditionally compliant" satisfies all MUST but not all SHOULD.

## 2. Notation
- UPPERCASE = literal; lowercase = token; brackets optional; ellipsis repeatable; vertical bar choice.
- "message-id" includes angle brackets.
- "wildmat" as per Section 4; if not conforming, server MAY place own interpretation or treat as syntax error.
- NUL=%x00, TAB=%x09, LF=%x0A, CR=%x0D, space=%x20.
- "keyword" MUST consist of US-ASCII letters, digits, ".", "-", MUST begin with letter, MUST be ≥3 characters.
- Examples are non-normative.

## 3. Basic Concepts

### 3.1 Commands and Responses
- Server MUST send greeting upon connection. Client and server exchange commands/responses.
- For TCP: server listens; client establishes connection on same port.
- Charset for all commands: UTF-8.
- Commands MUST consist of keyword, MAY have arguments; terminated by CRLF. Multiple commands MUST NOT be on same line.
- Arguments SHOULD be printable US-ASCII. Keywords and arguments separated by one or more space/TAB.
- Command lines MUST NOT exceed 512 octets (including CRLF). Arguments MUST NOT exceed 497 octets.
- Server MAY relax limits for extension commands.
- For UTF-8 outside U+0000-U+007F: MUST NOT use BOM (U+FEFF), MUST use Word Joiner (U+2060) for ZWNBSP. Implementations SHOULD apply same throughout.
- "character" = single Unicode code point; normalization not required.
- Commands with variants use second keyword (e.g., LIST ACTIVE). Keywords case insensitive.
- Each response MUST start with three-digit code. Multi-line responses: initial line followed by multi-line data block.
- Server MAY have inactivity autologout timer: SHOULD be ≥3 minutes; MAY be shorter waiting for first command. Receipt of any command or significant data SHOULD reset timer. Expiry: server SHOULD close connection without response.

### 3.1.1 Multi-line Data Blocks
- Block consists of sequence of lines ending with CRLF. Stream MUST NOT include NUL, LF, CR (except as CRLF).
- If line begins with "." (termination octet), it MUST be dot-stuffed by prepending an extra ".".
- Block MUST be terminated by line consisting of single "." CRLF.
- When interpreting, dot-stuffing MUST be undone; terminating line MUST NOT be considered part of block.
- Texts using encodings that may contain NUL, LF, CR other than CRLF cannot be reliably conveyed.

### 3.2 Response Codes
- First digit: 1xx=informative, 2xx=completed OK, 3xx=command OK so far send rest, 4xx=syntactically correct but failed, 5xx=unknown/syntax error.
- Second digit: x0x=connection/setup, x1x=newsgroup selection, x2x=article selection, x3x=distribution, x4x=posting, x8x=authentication/privacy, x9x=private use.
- Arguments fixed per response code. 211 is exception (may be single or multi-line).
- Arguments separated from status indicator and each other by single space. Numeric arguments decimal, MAY have leading zeros. String arguments MUST contain at least one character, no TAB/LF/CR/space. Server MAY add text after response code or last argument; client MUST NOT make decisions based on that text.
- Server MUST respond with appropriate generic response (Section 3.2.1) if applicable. Recognized commands MUST return codes listed in description or extension.
- Server MUST NOT produce other responses to client that does not invoke additional features.
- Client receiving unexpected response SHOULD use first digit to determine result.
- Response codes not specified MAY be used for installation-specific commands; SHOULD be x9x.
- Neither this document nor registered extensions will specify x9x.

### 3.2.1 Generic Response Codes
- **500**: command not recognized or optional command not implemented.
- **501**: syntax error in arguments (including too many arguments or variant not supported when base command is implemented; use 501 for variant, 500 only for base command).
- **504**: argument required to be base64-encoded and not validly encoded.
- **403**: internal fault/unable to carry out.
- **503**: command recognized but optional feature not provided or only handles subset.
- **502**: need to terminate connection and start new with appropriate authority. MUST NOT be used after MODE READER. Server MUST NOT close connection immediately after 502 except at initial connection or MODE READER.
- **480**: client must authenticate.
- **483**: client must negotiate privacy.
- **401**: client must change state; first argument MUST be capability label.
- **400**: server must terminate connection; give 400 to next command then close. Clients SHOULD use exponential backoff or present text to user.
- Client MUST be prepared to receive any of these for any command (server MUST NOT generate 500 for mandatory commands).

### 3.3 Capabilities and Extensions
- Client uses CAPABILITIES command to determine capabilities.
- Capability list: lines with one or more tokens; each line begins with capability label (keyword), then zero or more tokens.
- Server MUST ensure list accurately reflects currently available capabilities. If capability only available in certain state, MUST only include label when in that state.
- Lines beginning with other than letter reserved; clients MUST ignore any they don't understand.

### 3.3.2 Standard Capabilities
- **VERSION**: MUST be advertised by all servers, first line; at least one argument (decimal number, no leading zero). Version number of this spec: 2.
- **READER**: indicates implementation of commands useful for reading clients.
- **IHAVE**: indicates IHAVE command.
- **POST**: indicates POST command.
- **NEWNEWS**: indicates NEWNEWS command.
- **HDR**: indicates HDR and LIST HEADERS.
- **OVER**: indicates OVER and LIST OVERVIEW.FMT; if message-id form supported, MUST have argument MSGID.
- **LIST**: indicates at least one LIST variant; MUST have one argument per variant.
- **IMPLEMENTATION**: MAY be provided; SHOULD contain server software info; client MUST NOT use to determine capabilities.
- **MODE-READER**: indicates mode-switching server and MODE READER command.

### 3.3.3 Extensions
- Extension package of associated facilities, must define at least one new capability label.
- Extension either private (label begins with "X") or registered (in IANA registry, defined in standards-track or IESG-approved experimental RFC).
- Registered extension label MUST NOT begin with "X".
- Definition must include: descriptive name; capability labels; syntax, values, meanings of arguments; new commands (names for registered MUST NOT begin with "X"); response codes; new arguments for existing commands; any increase in max command/response length; effect on pipelining; circumstances when capabilities list changes; circumstances when existing commands produce 401,480,483; interaction with MODE READER; other behavior; formal syntax per Section 9.9.
- Private extension MAY be in capabilities list with label beginning with "X". Server MAY provide additional keywords beginning with "X".
- If server advertises registered extension, MUST implement fully. If not, MAY provide private extension but SHOULD NOT.
- Server MUST NOT send different response codes to basic NNTP commands or registered extension commands due to private extension availability.

### 3.3.4 Initial IANA Register
- IANA registry of NNTP capability labels; initial entries: AUTHINFO, HDR, IHAVE, IMPLEMENTATION, LIST, MODE-READER, NEWNEWS, OVER, POST, READER, SASL, STARTTLS, STREAMING, VERSION.

### 3.4 Mandatory and Optional Commands
- Some commands mandatory; remainder bundled by capability label.
- If label in capabilities list, server MUST support all commands in that bundle.
- If label not included, server MAY support some or none but SHOULD NOT support all.
- Command description indicates if mandatory or gives capability label.
- If server does not implement command, MUST always generate 500 (or 501 for variant). Otherwise MUST fully implement; no partial implementation.
- Note: some servers may return 502 for unimplemented commands.

### 3.4.1 Reading and Transit Servers
- Reading: client fetches/posts articles for user.
- Transit: bulk transfer between peer servers.
- Server may be optimized for reading or transit. IHAVE for transit; commands indicated by READER capability for reading.
- Except via MODE READER on mode-switching server, once server advertises IHAVE or READER, MUST continue for entire session.
- Server MAY provide different modes to different connections.
- Official TCP port: 119 (reading), port 433 (transit, if separate).

### 3.4.2 Mode Switching
- Implementation MAY (but SHOULD NOT) provide both transit and reader on same server requiring client to select. Called mode-switching server.
- Transit mode after initial connection: MUST advertise MODE-READER, MUST NOT advertise READER. May cease advertising MODE-READER after any command except CAPABILITIES.
- Reading mode after successful MODE READER: MUST NOT advertise MODE-READER, MUST advertise READER, MAY NOT advertise IHAVE.
- Client SHOULD only issue MODE READER if server advertises MODE-READER. Without CAPABILITIES, client MAY use heuristic.

### 3.5 Pipelining
- Client MAY use pipelining except where stated otherwise. Server MUST allow pipelining and MUST NOT throw away any text received after a command. Server MUST process commands in order.
- If command says "MUST NOT be pipelined", it MUST end any pipeline. Client MUST NOT send following command until response CRLF received. Server MAY ignore data after command until response CRLF.
- Initial connection MUST NOT be part of pipeline; client MUST NOT send until greeting CRLF.
- Client using blocking send must ensure deadlock avoidance.

### 3.6 Articles
- Article consists of headers and body separated by single empty line (two CRLF pairs). Article MUST NOT contain NUL; MUST NOT contain LF or CR except as part of CRLF pair; MUST end with CRLF.
- Headers: one or more header lines; each header line: name, colon, space, content, CRLF. Name printable US-ASCII except colon; case insensitive. Multiple same name allowed. Content MUST NOT contain CRLF; MAY be empty. Folding allowed (CRLF before TAB or space). There MUST be some other octet between any two CRLF pairs in a header line. Folding does not affect meaning. Header lines SHOULD NOT be folded before space after colon and SHOULD include at least one non-%x09/%x20 between CRLF pairs. If article fails this, servers MAY transfer without re-folding.
- Header content SHOULD be UTF-8. Implementations MUST be prepared to receive non-UTF-8 octets 128-255.
- Each article MUST have unique message-id; two articles MUST NOT have same message-id. Message-id MUST begin with "<", end with ">", MUST NOT contain ">" except at end. Length 3-250 octets. MUST NOT contain octets other than printable US-ASCII. Two message-ids same iff same sequence of octets.
- Server MUST synthesize message-id if cannot determine; this spec does not require article change.

## 4. The WILDMAT Format
- Based on Rich Salz wildmat; uniform pattern matching.

### 4.1 Wildmat Syntax
- wildmat = wildmat-pattern *("," ["!"] wildmat-pattern)
- wildmat-pattern = 1*wildmat-item
- wildmat-item = wildmat-exact / wildmat-wild
- wildmat-exact = printable US-ASCII characters excluding ! * , ? [ \ ] and UTF-8 non-ASCII.
- wildmat-wild = "*" / "?"
- Characters "," "\" "[" "]" not allowed in wildmats; * and ? always wildcards.

### 4.2 Wildmat Semantics
- Tested against string; rightmost matching pattern determines match. If pattern preceded by "!", whole wildmat doesn't match. If no pattern matches, no match.
- wildmat-pattern matches if string can be broken into components matching items in order; whole string used; anchored.

### 4.3 Extensions
- Server or extension MAY extend syntax/semantics provided all wildmats meeting Section 4.1 have meaning per Section 4.2.

## 5. Session Administration Commands

### 5.1 Initial Connection
- MUST NOT be pipelined.
- Server MUST present greeting: 200 (posting allowed), 201 (posting prohibited), 400 (temporarily unavailable, close), 502 (permanently unavailable, close).
- If service available with POST: 200. If available but no posting: 201. Otherwise 400 or 502 and close.
- 400 for temporary; 502 for permanent or insufficient info.
- Clients SHOULD use CAPABILITIES rather than rely on greeting for posting info.

### 5.2 CAPABILITIES (Mandatory)
- Syntax: CAPABILITIES [keyword]
- Response: 101 multi-line capability list.
- MAY be issued at any time; server MUST NOT require it for any capability.
- Capability list: one line per capability; VERSION MUST be first; no duplicates. Order not significant.
- Client MAY cache but MUST NOT rely on correctness; MUST cope gracefully; SHOULD provide refresh; MUST NOT cache security/privacy/authentication extensions.
- If keyword argument not recognized, respond with 101 as if omitted. If recognized, MAY use 101 or other defined code. If argument not keyword, 501.
- Server MUST NOT generate any other response.

### 5.3 MODE READER (Indicating capability: MODE-READER)
- MUST NOT be pipelined.
- Syntax: MODE READER
- Responses: 200 (posting allowed), 201 (posting prohibited), 502 (reading permanently unavailable, close).
- If mode-switching: switch to reader mode; return 200/201. Client MUST NOT issue more than once or after security/privacy commands. Server MAY reset state.
- If not mode-switching: if READER advertised, return 200/201 and MUST NOT affect state; otherwise 502 and close.

### 5.4 QUIT (Mandatory)
- Syntax: QUIT
- Response: 205 (connection closing). Server MUST acknowledge and close.
- If client disconnects or fault, server MUST gracefully cease attempts.
- Server MUST NOT generate any response other than 205 or 501 for arguments.

## 6. Article Posting and Retrieval
- Three key types: message-id, newsgroup+article number, arrival timestamp.
- Article numbers must be assigned in order of arrival; MUST be between 1 and 2,147,483,647.
- Server MUST ensure article numbers issued in order of arrival timestamp.
- Leading zeros allowed up to 16 digits.

### 6.1 Group and Article Selection
- "currently selected newsgroup" and "current article number" initially invalid.

#### 6.1.1 GROUP (Indicating capability: READER)
- Syntax: GROUP group
- Responses: 211 number low high group (success), 411 (no such group).
- Selects newsgroup; returns summary. If group not empty, estimate MUST be at least actual count, no more than (high-low+1). Empty group: high < low (preferred), or all zero, or high>=low with zero count.
- When group selected, current article number set to first article. If empty, current article number invalid. If invalid group, no change.
- GROUP or LISTGROUP must be used before any command depending on current selection.
- Low water mark: subsequent GROUP for same newsgroup MUST have low ≥ previous in session; SHOULD be ≥ any previous ever.

#### 6.1.2 LISTGROUP (Indicating capability: READER)
- Syntax: LISTGROUP [group [range]]
- Responses: 211 multi-line (article numbers follow), 411, 412.
- Like GROUP but also returns list of article numbers. Optional range: number, number-, number-number.
- On success, list one per line in numerical order. Sets current article number to first article in group.

#### 6.1.3 LAST (Indicating capability: READER)
- Syntax: LAST
- Responses: 223 n message-id, 412, 420, 422.
- Sets current article number to previous article. If already first, 422. If invalid, 420. If no newsgroup, 412.

#### 6.1.4 NEXT (Indicating capability: READER)
- Syntax: NEXT
- Responses: 223 n message-id, 412, 420, 421.
- Sets current article number to next article. If already last, 421.

### 6.2 Retrieval of Articles and Article Sections

#### 6.2.1 ARTICLE (Indicating capability: READER)
- Syntax: ARTICLE message-id, ARTICLE number, ARTICLE
- Responses: 220 multi-line (article follows), 430, 412, 423, 420.
- Three forms. First (message-id): server MUST NOT alter current newsgroup or article number. In response, article number replaced with zero unless article in current group (server MAY use number). Second (number): if exists, set current article number to that number. Third (current article). Server MUST NOT change currently selected newsgroup. Article returned as multi-line block.

#### 6.2.2 HEAD (Mandatory)
- Syntax: HEAD message-id, HEAD number, HEAD
- Responses: 221 multi-line (headers follow), 430, 412, 423, 420.
- Identical to ARTICLE except response code 221, only headers presented (empty line not included).

#### 6.2.3 BODY (Indicating capability: READER)
- Syntax: BODY message-id, BODY number, BODY
- Responses: 222 multi-line (body follows), 430, 412, 423, 420.
- Identical to ARTICLE except response code 222, only body presented.

#### 6.2.4 STAT (Mandatory)
- Syntax: STAT message-id, STAT number, STAT
- Responses: 223 n message-id, 430, 412, 423, 420.
- Identical to ARTICLE except if article exists, it is NOT presented, response code 223 (not multi-line).

### 6.3 Article Posting

#### 6.3.1 POST (Indicating capability: POST)
- MUST NOT be pipelined.
- Syntax: POST
- Initial responses: 340 (send article), 440 (posting not permitted).
- Subsequent responses: 240 (received OK), 441 (posting failed).
- If posting permitted, article sent as multi-line data block. Server SHOULD reject unwanted articles with 441 rather than accept and discard. 240 indicates barring unforeseen errors, article will be made available.
- If session interrupted, client SHOULD check or ensure same message-id.

#### 6.3.2 IHAVE (Indicating capability: IHAVE)
- MUST NOT be pipelined.
- Syntax: IHAVE message-id
- Initial responses: 335 (send article), 435 (not wanted), 436 (try later).
- Subsequent responses: 235 (transferred OK), 436 (transfer failed, try later), 437 (rejected, do not retry).
- For transferring already-posted articles; SHOULD NOT be used by personal news-reader. Server MAY later discard.
- Client SHOULD treat lack of response as 436.

## 7. Information Commands

### 7.1 DATE (Indicating capability: READER)
- Syntax: DATE
- Response: 111 yyyymmddhhmmss (server date and time in UTC).
- MUST return timestamp from same clock as used for article arrival. Clock SHOULD be monotonic. Server SHOULD keep clock accurate.

### 7.2 HELP (Mandatory)
- Syntax: HELP
- Response: 100 multi-line help text.
- Help text not guaranteed format; MUST NOT be used as replacement for CAPABILITIES.

### 7.3 NEWGROUPS (Indicating capability: READER)
- Syntax: NEWGROUPS date time [GMT]
- Response: 231 multi-line list of new newsgroups (same format as LIST ACTIVE).
- Date: 6 or 8 digits (yymmdd or yyyymmdd); time: hhmmss. "GMT" indicates UTC.
- Empty list valid. Clients SHOULD use GMT when possible.

### 7.4 NEWNEWS (Indicating capability: NEWNEWS)
- Syntax: NEWNEWS wildmat date time [GMT]
- Response: 230 multi-line list of message-ids.
- List of message-ids of articles posted/received since specified date-time in newsgroups matching wildmat. Order not significant; duplicates allowed.

### 7.5 Time
- Informative section on using DATE and NEWNEWS to avoid gaps. Summarized: clients can timestamp successive sessions to ensure coverage.

### 7.6 The LIST Commands
- LIST family returns multi-line information. Set of keywords given in LIST capability. Command MUST NOT change visible server state.

#### 7.6.1 LIST (Indicating capability: LIST)
- Syntax: LIST [keyword [wildmat|argument]]
- Response: 215 multi-line information.
- If keyword not recognized or argument unexpected: 501. If keyword recognized but server doesn't maintain info: 503.
- Information may be newsgroup-based; optional wildmat restricts groups.

#### 7.6.2 Standard LIST Keywords
- ACTIVE, ACTIVE.TIMES, DISTRIB.PATS, HEADERS, NEWSGROUPS, OVERVIEW.FMT. Status table lists mandatory/optional per capability.

#### 7.6.3 LIST ACTIVE
- Mandatory if READER advertised. Returns valid newsgroups and info: name, high water mark, low water mark, status (y, n, m). Server MUST include every group client can select.

#### 7.6.4 LIST ACTIVE.TIMES
- Optional. Returns creation time and creator of newsgroups (if available). May omit groups.

#### 7.6.5 LIST DISTRIB.PATS
- Optional. Returns distribution patterns for posting.

#### 7.6.6 LIST NEWSGROUPS
- Mandatory if READER advertised. Returns newsgroup name and description. Description SHOULD be UTF-8; clients MUST be prepared for other encodings.

## 8. Article Field Access Commands

### 8.1 Article Metadata
- Metadata item names begin with colon; case insensitive. Server MUST compute for itself; MUST NOT trust article's values.

#### 8.1.1 :bytes Metadata Item
- SHOULD equal number of octets in entire article (headers, body, empty line; excluding dot-stuffing and terminating CRLF). Note: clients MUST NOT rely on accuracy.

#### 8.1.2 :lines Metadata Item
- MUST equal number of lines in article body (excluding empty line). Equivalently, two less than number of CRLF pairs in BODY response.

### 8.2 Database Consistency
- Database consistent for a field if it records content/absence for all articles. LIST OVERVIEW.FMT SHOULD list consistent fields; MUST NOT include inconsistent or not stored. When set of stored fields changes, output must be altered carefully.

### 8.3 OVER (Indicating capability: OVER)
- Syntax: OVER message-id, OVER range, OVER
- Responses: 224 multi-line, 430, 412, 423, 420.
- Returns overview information for article(s). First 8 fields: article number (0 if message-id form and not in current group), Subject, From, Date, Message-ID, References, :bytes, :lines. Subsequent fields: other headers/metadata with header name included for headers.
- Field values: remove all CRLF pairs, replace TAB with space. If header absent, field empty.
- Server SHOULD NOT produce output for articles that no longer exist.
- Support for message-id form optional; if supported, OVER capability line MUST include MSGID.

### 8.4 LIST OVERVIEW.FMT (Indicating capability: OVER)
- Returns description of database fields consistent, one per line. First 7 lines MUST be: Subject:, From:, Date:, Message-ID:, References:, :bytes, :lines (or Bytes: and Lines: for compatibility). Subsequent lines: header:full or metadata name.

### 8.5 HDR (Indicating capability: HDR)
- Syntax: HDR field message-id, HDR field range, HDR field
- Responses: 225 multi-line, 430, 412, 423, 420.
- Returns contents of specified header or metadata for article(s). For headers, header name, colon, and first space omitted.
- Header contents modified: remove CRLF pairs, replace TAB with space.
- If header absent, line included with empty content (space after article number MAY be retained or omitted). If multiple occurrences, only first returned.
- Server MAY restrict fields; if so, respond with 503. May differ between message-id and range forms.

### 8.6 LIST HEADERS (Indicating capability: HDR)
- Returns list of fields available via HDR. If all headers allowed, include special entry ":" (single colon). Metadata items listed explicitly.
- If server treats message-id form differently, HEADERS MSGID and HEADERS RANGE give respective lists; with no argument, only items common to both.

## 9. Augmented BNF Syntax (Condensed)
- Formal ABNF defined for commands, responses, capabilities, articles, and general non-terminals. Extensions must provide syntax for additional forms.

## 10. Internationalisation Considerations
- Historical: RFC 977 assumed ASCII; now UTF-8 is default. Article headers names MUST be US-ASCII. Header values SHOULD use US-ASCII or RFC 2047 encoding. MIME recommended. Implementations MUST not convert/re-encode; MAY pass non-UTF-8 unchanged. Newsgroup names SHOULD be US-ASCII until successor standard.

## 11. IANA Considerations
- IANA registry of NNTP capability labels. Labels beginning with X reserved for private use. Different entries MUST use different labels and different command names.

## 12. Security Considerations
- Personal/proprietary information in articles; implementers should provide warnings and management mechanisms.
- Server log information confidential; handle per law.
- Weak authentication; extension recommended.
- DNS spoofing: clients and servers SHOULD rely on resolver, observe TTL.
- UTF-8 issues: MUST NOT generate malformed sequences; SHOULD detect and act (e.g., 501, replacement char, close). Replacement MUST not bypass checks.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Server MUST send greeting upon connection. | shall | 3.1, 5.1 |
| R2 | Commands MUST consist of keyword terminated by CRLF; MUST NOT exceed 512 octets. | shall | 3.1 |
| R3 | Server MUST allow pipelining and MUST NOT throw away text after command. | shall | 3.5 |
| R4 | Article MUST NOT contain NUL; MUST NOT contain LF/CR except as CRLF; MUST end with CRLF. | shall | 3.6 |
| R5 | Each article MUST have unique message-id. | shall | 3.6 |
| R6 | Server MUST respond to any command with appropriate generic response if applicable. | shall | 3.2.1 |
| R7 | CAPABILITIES command MUST be implemented. | shall | 5.2 |
| R8 | QUIT command MUST be implemented. | shall | 5.4 |
| R9 | HEAD command MUST be implemented. | shall | 6.2.2 |
| R10 | STAT command MUST be implemented. | shall | 6.2.4 |
| R11 | HELP command MUST be implemented. | shall | 7.2 |
| R12 | If server advertises READER capability, GROUP, LISTGROUP, LAST, NEXT, ARTICLE, BODY, DATE, NEWGROUPS, LIST ACTIVE, LIST NEWSGROUPS MUST be supported. | shall | 3.4, 6.1, 6.2, 7.1, 7.3, 7.6.3, 7.6.6 |
| R13 | Server MUST present correct capability list reflecting current state. | shall | 3.3.1 |
| R14 | Server MUST NOT change currently selected newsgroup or current article number except as specified. | shall | 6.1, 6.2 |
| R15 | Multi-line data blocks MUST adhere to dot-stuffing rules. | shall | 3.1.1 |
| R16 | Server MUST ensure article numbers are issued in order of arrival timestamp. | shall | 6 |
| R17 | If server implements IHAVE, it MUST implement IHAVE command fully. | shall | 3.4, 6.3.2 |
| R18 | If server implements POST, it MUST implement POST command fully. | shall | 3.4, 6.3.1 |
| R19 | Server MUST NOT generate malformed UTF-8 sequences; SHOULD detect and act. | shall / should | 12.5 |
| R20 | Clients MUST NOT cache security/privacy extension capabilities. | must | 12.6 |

## Informative Annexes (Condensed)

- **Appendix A: Interaction with Other Specifications** – Discusses header folding, message-id handling, and article posting considerations for Netnews (RFC 1036) and email (RFC 2822). Key points: header folding SHOULD conform to stricter syntax; message-ids should be globally unique; for email articles, server should canonicalize equivalent message-ids; for IHAVE, server MAY use provided message-id; for POST, article SHOULD contain Message-ID header for duplicate detection.
- **Appendix B: Summary of Commands** – Tables listing commands ordered by name and by indicating capability.
- **Appendix C: Summary of Response Codes** – Lists all response codes with generating commands, arguments, and meanings.
- **Appendix D: Changes from RFC 977** – Lists changes: added ABNF, UTF-8 instead of US-ASCII, mandatory message-id, clarified response codes, removed SLAVE, extended LIST and CAPABILITIES, added formal metadata, among others.