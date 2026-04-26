# RFC 2046: Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types
**Source**: IETF | **Version**: Standards Track | **Date**: November 1996 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc2046/

## Scope (Summary)
Defines the general structure of the MIME media typing system and an initial set of media types (text, image, audio, video, application, multipart, message). Specifies parameters, syntax, and semantics for each media type and subtype, including composite types and mechanisms for fragmentation, external-body referencing, and character set handling.

## Normative References
- RFC 822 (STD 11)
- RFC 2045 (MIME Part One)
- RFC 2047 (MIME Part Three)
- RFC 2048 (MIME Part Four)
- RFC 2049 (MIME Part Five)
- RFC 934, RFC 1049
- ANSI X3.4-1986 (US-ASCII)
- ISO-8859 series
- RFC 821 (SMTP)
- RFC 959 (FTP)
- RFC 783 (TFTP)
- RFC 1896 (text/enriched)
- [JPEG], [PCM], [MPEG], [POSTSCRIPT], [POSTSCRIPT2]

## Definitions and Abbreviations
- **MIME**: Multipurpose Internet Mail Extensions
- **Content-Type**: Header field specifying media type and subtype.
- **Media Type**: Consists of a top-level type and a subtype (e.g., text/plain).
- **Subtype**: Specific format for a given top-level type.
- **Parameters**: Modifiers of media subtype (e.g., charset, boundary).
- **Boundary**: Unique delimiter used in multipart entities.
- **IANA**: Internet Assigned Numbers Authority – central registry for MIME extensions.
- **CRLF**: Carriage Return Line Feed (US-ASCII 13,10) – required line break representation in MIME text.
- **DSC**: Document Structuring Conventions (PostScript).
- **Access-type**: Parameter for message/external-body specifying retrieval mechanism.

## 1. Introduction
- **Content-Type** header field (defined in RFC 2045) specifies nature of body data using media type, subtype, and parameters.
- Top-level type declares general data type; subtype specifies format. Unknown subtypes can be handled accordingly (e.g., show unrecognized text, but not unrecognized image).
- Parameters are modifiers; implementations **must** ignore unrecognized parameters.
- MIME is extensible; new types/subtypes/parameters are registered via IANA as per RFC 2048.
- Seven initial top-level media types are defined: five discrete (text, image, audio, video, application) and two composite (multipart, message).

## 2. Definition of a Top-Level Media Type
A top-level media type definition consists of:
1. Name and description, including qualification criteria.
2. Parameters defined for all subtypes (required/optional).
3. How user agents/gateways handle unknown subtypes.
4. Gatewaying considerations.
5. Restrictions on content-transfer-encodings.

## 3. Overview of Initial Top-Level Media Types
- **text**: textual information. Subtype "plain" – no formatting. Subtype "enriched" (RFC 1896) for rich text.
- **image**: image data (e.g., jpeg, gif).
- **audio**: audio data (e.g., basic: 8-bit ISDN mu-law, 8000 Hz).
- **video**: time-varying picture (e.g., mpeg). May include synchronized audio.
- **application**: other data (e.g., octet-stream for binary, PostScript for active messaging).
- **multipart**: multiple independent entities (mixed, alternative, parallel, digest).
- **message**: encapsulated message (rfc822, partial, external-body).

## 4. Discrete Media Type Values
### 4.1 Text Media Type
- For textual material. Parameter "charset" indicates character set.
- **Plain text**: linear sequence of characters, no formatting.
- **Rich text**: formats readable without special software; use subtypes of "text".

#### 4.1.1 Representation of Line Breaks
- **Shall**: Canonical form of any MIME "text" subtype **MUST** represent line break as CRLF. Any occurrence of CRLF **MUST** represent a line break. Use of CR and LF outside line breaks is forbidden.
- Note: Line break interpretation depends on subtype (e.g., text/plain vs text/enriched).
- Note: SMTP limits line length to 998 octets before CRLF; longer lines must be encoded.

#### 4.1.2 Charset Parameter
- Specified as `charset=value`. Values case-insensitive.
- Default charset is US-ASCII if absent.
- Future "text" subtypes must specify if they use charset parameter.
- All chars in body must be from specified charset.
- Initial charset values: US-ASCII, ISO-8859-1 through ISO-8859-10.
- Characters 128-159 have no defined meaning in ISO-8859-X.
- Characters below 128 same as US-ASCII.
- "ISO-8859-6" and "ISO-8859-8" use visual method for bidirectional text.
- No shift/escape sequences defined.
- Charset **must** be explicitly specified if other than US-ASCII.
- Private charset names start with "X-".
- Implementors discouraged from defining new charsets.
- Composition software **should** use lowest common denominator charset (e.g., mark as US-ASCII if only ASCII chars).

#### 4.1.3 Plain Subtype
- No formatting commands. Default media type for Internet mail is `text/plain; charset=us-ascii`.

#### 4.1.4 Unrecognized Subtypes
- **Should** treat as subtype "plain" if charset is known; otherwise treat as `application/octet-stream`.

### 4.2 Image Media Type
- "image" indicates body contains an image. Subtype names case-insensitive.
- Initial subtype: "jpeg" (JFIF encoding).
- Unrecognized subtypes **should** be treated as `application/octet-stream`; optionally pass to general-purpose image viewer (with security warning).

### 4.3 Audio Media Type
- "audio" indicates audio data. Initial subtype "basic": 8-bit ISDN mu-law, 8000 Hz, single channel.
- Unrecognized subtypes **should** be treated as `application/octet-stream`; optionally pass to audio player.

### 4.4 Video Media Type
- "video" indicates time-varying picture, possibly with sound. Subtype "mpeg".
- Synchronized audio explicitly permitted.
- Unrecognized subtypes **should** be treated as `application/octet-stream`; optionally pass to video player.

### 4.5 Application Media Type
- For discrete data not fitting other categories, typically processed by application programs.
- Subtypes: "octet-stream" and "PostScript".

#### 4.5.1 Octet-Stream Subtype
- Indicates arbitrary binary data.
- Optional parameters: TYPE (general category), PADDING (bits appended).
- NAME parameter deprecated (use Content-Disposition).
- Recommended action: offer to put data in file or use as input to user-specified process.
- **Strongly recommended** not to implement path-search for executing arbitrary programs named in parameters.

#### 4.5.2 PostScript Subtype
- "application/postscript" – PostScript program (Level 1 or 2).
- Use of DSC strongly recommended.
- **Security risks** – implementors discouraged from sending to off-the-shelf interpreters. Detailed list of dangerous operators (deletefile, renamefile, file, filenameforall, exitserver, startjob, setsystemparams, setdevparams, etc.).
- Recommendations:
  - Senders should avoid dangerous operators.
  - Receivers should disable or restrict dangerous operators.
  - Disable ability to make retained changes to environment.
  - Disable system/device parameter changes.
  - Avoid nonstandard extensions.
  - Provide abort mechanisms for resource consumption.
  - Avoid raw binary inside PostScript.
  - Be aware of interpreter bugs.

#### 4.5.3 Other Application Subtypes
- Unrecognized subtypes **must** be treated as `application/octet-stream`.

## 5. Composite Media Type Values
### 5.1 Multipart Media Type
- Combines one or more body parts, each preceded by a boundary delimiter line.
- Body parts have header area, blank line, body area – syntactically similar to RFC 822 message but different semantics.
- Only header fields beginning with "Content-" have defined meaning; others may be ignored.
- Default Content-Type for body parts: `text/plain; charset=US-ASCII`, except in multipart/digest where default is `message/rfc822`.
- Boundary delimiter **MUST NOT** appear inside encapsulated parts.
- All present and future "multipart" subtypes must use identical syntax.
- Content-Transfer-Encoding restricted to "7bit", "8bit", or "binary".

#### 5.1.1 Common Syntax
- Content-Type requires "boundary" parameter.
- Boundary delimiter line: two hyphens ("--") + boundary parameter value + optional linear whitespace + CRLF.
- Boundary delimiter line **MUST** occur at beginning of a line (after CRLF).
- Boundary must be 1-70 characters from specific set, not ending with whitespace.
- Last body part followed by closing delimiter: `--boundary--`.
- Preamble and epilogue areas are ignored by MIME-compliant software but may contain explanatory notes for non-MIME readers.
- Nested multipart allowed with different boundaries.
- Single body part allowed in multipart.
- Grammar for boundary and multipart-body provided (see Appendix A).

#### 5.1.2 Handling Nested Messages and Multiparts
- **Required**: MIME implementations must recognize outer level boundary markers at any level of inner nesting.

#### 5.1.3 Mixed Subtype
- Independent body parts bundled in order. Unrecognized multipart subtypes **must** be treated as "mixed".

#### 5.1.4 Alternative Subtype
- Body parts are alternative versions of same information. Order increases faithfulness – last part is best choice.
- Senders should place plainest format first, richest last. Receivers should display last recognized format.
- Each part may have different Content-ID if information content differs; same Content-ID if identical.
- Content-ID values for parts must differ from that of the overall multipart/alternative.

#### 5.1.5 Digest Subtype
- Default Content-Type for parts is `message/rfc822`. Intended for collections of messages.
- Should not include text/plain parts; use multipart/mixed if needed.

#### 5.1.6 Parallel Subtype
- Order of body parts not significant. Presentation may display simultaneously if supported.

#### 5.1.7 Other Multipart Subtypes
- Unrecognized subtypes **must** be treated as `multipart/mixed`.

### 5.2 Message Media Type
- Encapsulates another mail message. Subtypes: rfc822, partial, external-body.
- Mail gateways must not alter encapsulated headers.

#### 5.2.1 RFC822 Subtype
- Body contains encapsulated RFC 822 message. At least one of "From", "Subject", or "Date" must be present.
- No encoding other than "7bit", "8bit", or "binary" permitted for body.
- Headers always US-ASCII; non-US-ASCII text in headers per RFC 2047.

#### 5.2.2 Partial Subtype
- Large entities split into fragments for transport. Body is a fragment of a larger entity.
- **Must** have Content-Transfer-Encoding of 7bit (default). "8bit" or "binary" prohibited.
- Three parameters: **id** (unique identifier), **number** (fragment number, starting at 1), **total** (total fragments – required on final fragment, optional but encouraged on earlier).
- Reassembly merges headers per rules: copy non-Content- headers from first enclosing message, then append Content- headers and Subject/Message-ID/Encrypted/MIME-Version from inner message.
- Fragmented messages must be split only at line boundaries.

#### 5.2.3 External-Body Subtype
- Actual body data is not included; only referenced. Parameters describe access mechanism.
- Encapsulated headers MUST include Content-ID header field.
- **Must** have Content-Transfer-Encoding of 7bit (default).
- Parameters: **access-type** (mandatory): FTP, ANON-FTP, TFTP, LOCAL-FILE, MAIL-SERVER; also optional EXPIRATION, SIZE, PERMISSION.
- For FTP/TFTP: mandatory NAME, SITE; optional DIRECTORY, MODE. Default MODE: NETASCII for TFTP, ASCII for FTP.
- ANON-FTP: same as FTP but with anonymous login and user's mail address as password.
- LOCAL-FILE: mandatory NAME; optional SITE (wildcards allowed).
- MAIL-SERVER: mandatory SERVER; optional SUBJECT. Phantom body contains commands to mail server.
- Security issues: user agents must ask for explicit permission before retrieving external data; mail-server requests should include indication of automatic generation.
- Phantom body (after encapsulated headers) is ignored for most access-types except mail-server.
- Headers merge using same rules as message/partial.

#### 5.2.4 Other Message Subtypes
- Unrecognized subtypes **must** be treated as `application/octet-stream`.
- Future message subtypes for email should be restricted to "7bit" encoding.

## 6. Experimental Media Type Values
- Values beginning with "X-" are private; must be used by consenting systems.
- Public values shall never begin with "X-".
- Use of "X-" top-level types strongly discouraged; use subtypes of existing types.

## 7. Summary
The five discrete media types (text, image, audio, video, application) provide standardized tagging. Composite types (multipart, message) allow mixing and hierarchical structuring. A distinguished parameter syntax supports specification of details like character sets. Useful subtypes include message/partial and message/external-body.

## 8. Security Considerations
- Discussed for application/postscript, message/external-body, and in RFC 2048.
- Implementors should pay special attention to media types causing remote execution; model after application/postscript analysis.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Canonical form of MIME "text" subtype MUST represent line break as CRLF. | shall | Section 4.1.1 |
| R2 | Any occurrence of CRLF in MIME "text" MUST represent a line break. | shall | Section 4.1.1 |
| R3 | Use of CR and LF outside line break sequences is forbidden. | shall | Section 4.1.1 |
| R4 | Default charset for "text/plain" is US-ASCII if charset parameter absent. | must | Section 4.1.2 |
| R5 | Charset parameter values for "text" are NOT case sensitive. | shall | Section 4.1.2 |
| R6 | Unrecognized subtypes of "text" with known charset should be treated as "plain". | should | Section 4.1.4 |
| R7 | Unrecognized "text" subtypes with unrecognized charset should be treated as "application/octet-stream". | should | Section 4.1.4 |
| R8 | Unrecognized "image", "audio", "video" subtypes should at minimum be treated as "application/octet-stream". | should | Sections 4.2, 4.3, 4.4 |
| R9 | Implementations NOT recommended to implement path-search for executing programs from Content-Type parameters. | strongly recommended | Section 4.5.1 |
| R10 | For application/postscript, senders should avoid dangerous operators; receivers should disable/restrict them. | should | Section 4.5.2 |
| R11 | Any present/future "multipart" subtype must use identical syntax. | must | Section 5.1 |
| R12 | Multipart boundary delimiter MUST NOT appear inside encapsulated parts. | must | Section 5.1 |
| R13 | Boundary delimiter line must occur at beginning of a line (after CRLF). | must | Section 5.1.1 |
| R14 | Boundary must be 1-70 characters from allowed set. | shall | Section 5.1.1 |
| R15 | Multipart Content-Transfer-Encoding restricted to "7bit", "8bit", or "binary". | shall | Section 5.1 |
| R16 | Unrecognized multipart subtypes must be treated as "multipart/mixed". | must | Section 5.1.7 |
| R17 | MIME implementations must recognize outer level boundary markers at any level of inner nesting. | required | Section 5.1.2 |
| R18 | Message/partial must have Content-Transfer-Encoding of 7bit. | must | Section 5.2.2 |
| R19 | Message/partial fragments must be split at line boundaries only. | shall | Section 5.2.2.1 |
| R20 | Message/external-body must have Content-Transfer-Encoding of 7bit. | must | Section 5.2.3 |
| R21 | Message/external-body encapsulated headers MUST include Content-ID. | must | Section 5.2.3 |
| R22 | Unrecognized message subtypes must be treated as "application/octet-stream". | must | Section 5.2.4 |
| R23 | Future message subtypes for email should be restricted to "7bit" encoding. | should | Section 5.2.4 |
| R24 | Experimental media type values beginning with "X-" are private. | shall | Section 6 |

## Informative Annexes (Condensed)
- **Appendix A – Collected Grammar**: Provides complete BNF for syntax defined in this document, referencing RFC 822 for undefined terms. Includes productions for boundary, body-part, multipart-body, transport-padding, etc. (Grammar is reproduced in the original document.)