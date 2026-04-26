# RFC 2045: Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies
**Source**: IETF (Network Working Group) | **Version**: MIME-Version 1.0 | **Date**: November 1996 | **Type**: Standards Track
**Original**: https://tools.ietf.org/html/rfc2045

## Scope (Summary)
This document defines the format of Internet message bodies for MIME, specifying headers (MIME-Version, Content-Type, Content-Transfer-Encoding, Content-ID, Content-Description) that enable the inclusion of textual and non-textual content (e.g., audio, video, multi-part) in RFC 822 messages without breaking existing infrastructure.

## Normative References
- RFC 821 (SMTP) – line length ≤ 1000 characters, 7bit US-ASCII restriction
- RFC 822 (Standard for ARPA Internet Text Messages) – header format, message structure
- RFC 1123 (Requirements for Internet Hosts) – modifies `return`, `date`, `mailbox` syntax
- RFC 1652 (SMTP Service Extension for 8bit-MIMEtransport)
- RFC 2046, RFC 2047, RFC 2048, RFC 2049 (companion MIME documents)
- STD 1 (Internet Official Protocol Standards)
- RFC 934, RFC 1049 (earlier work, superseded)

## Definitions and Abbreviations
- **CRLF**: The two-octet sequence CR (13) followed by LF (10) denoting a line break in RFC 822 mail.
- **Character Set**: A method of converting a sequence of octets into a sequence of characters; must be fully specified by the MIME charset name.
- **Message**: A complete RFC 822 message or an encapsulated message in "message/rfc822" or "message/partial".
- **Entity**: The MIME-defined header fields and contents of a message or one part of a multipart entity.
- **Body Part**: An entity inside a multipart entity.
- **Body**: The body of an entity (message or body part).
- **7bit Data**: Data with lines ≤ 998 octets between CRLF, using only octets 0–127, no NULs, CR and LF only in CRLF line separators.
- **8bit Data**: As 7bit but octets 128–255 allowed, lines ≤ 998 octets, no NULs.
- **Binary Data**: Any sequence of octets; no restrictions.
- **Lines**: Octet sequences separated by CRLF; may differ from display lines.

## MIME Header Fields
- **Entity-headers**: optional `content`, `encoding`, `id`, `description`, and any `MIME-extension-field` (beginning with "Content-").
- **MIME-message-headers**: entity-headers + RFC 822 fields + version.
- **MIME-part-headers**: entity-headers + optional fields; fields not beginning with "content-" may be ignored.

## MIME-Version Header Field
- **Requirement (MUST)**: Messages conforming to this document MUST include the header `MIME-Version: 1.0` (exact text).
- **Syntax**: `version := "MIME-Version" ":" 1*DIGIT "." 1*DIGIT`
- **Scope**: Required at top level of a message; not required for each body part of multipart; required for embedded headers of type "message/rfc822" or "message/partial" only if the embedded message claims MIME conformance.
- **Interpretation**: If *MIME-Version* ≠ "1.0", message may not conform. Any RFC 822 comments in the value must be ignored when checking.
- **Absence**: In absence of *MIME-Version*, a receiving UA may interpret body according to local conventions.

## Content-Type Header Field
- **Purpose**: Describes data in the body so the receiving UA can select an appropriate agent.
- **Syntax**:
  - `content := "Content-Type" ":" type "/" subtype *(";" parameter)`
  - `type := discrete-type / composite-type`
  - `discrete-type := "text" / "image" / "audio" / "video" / "application" / extension-token`
  - `composite-type := "message" / "multipart" / extension-token`
  - `subtype := extension-token / iana-token` (subtype is MANDATORY)
  - `parameter := attribute "=" value` (value case-sensitive unless specified)
- **Case insensitivity**: Type, subtype, parameter names are case-insensitive. Parameter values are case-sensitive except when specified otherwise (e.g., multipart boundaries case-sensitive, `access-type` not).
- **Parameter semantics**: Parameters are modifiers of media subtype; unknown parameters MUST be ignored. No globally meaningful parameters; global mechanisms should use additional Content-* header fields.
- **Default**: RFC 822 messages without Content-Type default to `text/plain; charset=us-ascii`.
- **Registration**: Private subtypes must use "X-" prefix; standard subtypes must be registered with IANA per RFC 2048.

## Content-Transfer-Encoding Header Field
- **Purpose**: Encodes 8bit or binary data into 7bit short-line format for transport through restricted protocols (e.g., SMTP).
- **Syntax**: `encoding := "Content-Transfer-Encoding" ":" mechanism`
  - `mechanism := "7bit" / "8bit" / "binary" / "quoted-printable" / "base64" / ietf-token / x-token`
  - **Default**: "7BIT" if absent.
- **Semantics**: Each mechanism specifies both a decoding transformation and the domain of the result.
  - **Identity encodings**: "7bit", "8bit", "binary" (no transformation; indicate data domain).
  - **Transformations**: "quoted-printable" and "base64" produce 7bit US-ASCII output.
- **Restrictions**:
  - Composite media types ("multipart", "message") MUST NOT use any encoding other than "7bit", "8bit", or "binary".
  - Unencoded 8bit data labelled as "7bit" is NOT allowed; unencoded non-line-oriented data labelled other than "binary" is NOT allowed.
- **New encodings**: Private values must use "X-" prefix; standardized values must be defined by a standards-track RFC (creation STRONGLY discouraged).
- **Interpretation**: If Content-Transfer-Encoding appears in message header, it applies to entire message; in entity header, to that entity body only.
- **Unrecognized encoding**: Must treat entity as `Content-Type: application/octet-stream`.
- **Note on nested encodings**: Prohibited; encoding must be done at innermost level.

### Quoted-Printable Encoding (Section 6.7)
- **Designed for**: Mostly US-ASCII text; produces human-readable output; lines ≤ 76 characters.
- **Rules**:
  1. Any octet except CR/LF in a CRLF line break MAY be represented as `=XX` (hexadecimal, uppercase letters).
  2. Octets 33–60 and 62–126 MAY be represented literally.
  3. TAB (9) and SPACE (32) MAY be literal but MUST NOT appear at end of encoded line.
  4. Line breaks in text: CRLF in canonical form becomes CRLF in encoded form.
  5. Soft line breaks: `=` at end of line indicates continuation (line ≤ 76 chars).
- **Illegal substrings** (for robustness): lowercase hex, `=` followed by non-hex non-CR, `=` as last or penultimate char, control characters other than TAB/CR/LF, octets > 126, lines > 76 chars.

### Base64 Encoding (Section 6.8)
- **Designed for**: Arbitrary binary data; 33% size increase; universally representable in ISO 646 and EBCDIC.
- **Alphabet**: 65-character subset (64 characters + "=" padding) as per Table 1.
- **Encoding**: 24-bit groups (3 octets) → 4 encoded characters. Padding with "=" for incomplete groups.
- **Line length**: Encoded lines ≤ 76 characters; all characters not in alphabet (except line breaks) should be ignored.
- **Special**: No hyphens appear in base64, so no need to worry about boundary delimiters in multipart.

## Content-ID Header Field
- **Syntax**: `id := "Content-ID" ":" msg-id` (syntactically identical to Message-ID).
- **Use**: Uniquely identify MIME entities; MANDATORY for `message/external-body` to enable caching.
- **Special semantics**: In multipart/alternative, Content-ID refers to body parts (see RFC 2046).

## Content-Description Header Field
- **Syntax**: `description := "Content-Description" ":" *text`
- **Purpose**: Associative descriptive text (always optional). Default character set US-ASCII; RFC 2047 allows non-US-ASCII values.

## Additional MIME Header Fields
- **Rule**: New fields that describe content must begin with "Content-".
- **Formal**: `MIME-extension-field := <Any RFC 822 header field beginning with "Content-">`

## Summary
MIME-Version + Content-Type + Content-Transfer-Encoding enable standardized inclusion of arbitrary data in RFC 822 messages without violating RFC 821/822 constraints. RFC 2046 defines initial media types.

## Security Considerations
Refer to RFC 2046 for security issues.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Messages conforming to this document MUST include `MIME-Version: 1.0` | MUST | Section 4 |
| R2 | Unknown Content-Type parameters MUST be ignored | MUST | Section 5 |
| R3 | Composite media types (multipart, message) MUST NOT use encodings other than "7bit", "8bit", or "binary" | MUST (FORBIDDEN otherwise) | Section 6.4 |
| R4 | Unencoded 8bit data labelled as "7bit" is NOT allowed | MUST NOT | Section 6.2 |
| R5 | Unencoded non-line-oriented data labelled other than "binary" is NOT allowed | MUST NOT | Section 6.2 |
| R6 | Implementations generating `message/external-body` MUST include a Content-ID header | MUST | Section 7 |
| R7 | Quoted-printable encoded lines MUST NOT exceed 76 characters | MUST | Section 6.7 (Rule 5) |
| R8 | Soft line breaks in quoted-printable are indicated by `=` at line end | REQUIRED | Section 6.7 (Rule 5) |
| R9 | In quoted-printable, TAB/SPACE MUST NOT appear at end of line (must encode as `=09`/`=20`) | MUST | Section 6.7 (Rule 3) |
| R10 | Base64 encoded output lines MUST NOT exceed 76 characters | MUST | Section 6.8 |
| R11 | All characters not in base64 alphabet (except line breaks) in base64 data MUST be ignored | MUST | Section 6.8 |
| R12 | When converting quoted-printable to base64, hard line breaks (CRLF) must be preserved | MUST | Section 6.5 |
| R13 | New standardized Content-Transfer-Encoding values MUST be defined by a standards-track RFC | MUST | Section 6.3 |

## Collected Grammar (Appendix A, Normative)
The complete BNF grammar for all syntax specified in this document is provided below. It references RFC 822 definitions for terms not defined here.

- `attribute := token` (case-insensitive)
- `composite-type := "message" / "multipart" / extension-token`
- `content := "Content-Type" ":" type "/" subtype *(";" parameter)` (type/subtype matching case-insensitive)
- `description := "Content-Description" ":" *text`
- `discrete-type := "text" / "image" / "audio" / "video" / "application" / extension-token`
- `encoding := "Content-Transfer-Encoding" ":" mechanism`
- `entity-headers := [ content CRLF ] [ encoding CRLF ] [ id CRLF ] [ description CRLF ] *( MIME-extension-field CRLF )`
- `extension-token := ietf-token / x-token`
- `hex-octet := "=" 2(DIGIT / "A"/"B"/"C"/"D"/"E"/"F")` (only uppercase)
- `iana-token := <publicly-defined token, registered with IANA per RFC 2048>`
- `ietf-token := <standards-track RFC token, registered with IANA>`
- `id := "Content-ID" ":" msg-id`
- `mechanism := "7bit" / "8bit" / "binary" / "quoted-printable" / "base64" / ietf-token / x-token`
- `MIME-extension-field := <RFC 822 header field beginning with "Content-">`
- `MIME-message-headers := entity-headers fields version CRLF` (ordering ignored)
- `MIME-part-headers := entity-headers [fields]` (non-"Content-" fields may be ignored)
- `parameter := attribute "=" value`
- `ptext := hex-octet / safe-char`
- `qp-line := *(qp-segment transport-padding CRLF) qp-part transport-padding`
- `qp-part := qp-section` (max 76 chars)
- `qp-section := [*(ptext / SPACE / TAB) ptext]`
- `qp-segment := qp-section *(SPACE / TAB) "="` (max 76 chars)
- `quoted-printable := qp-line *(CRLF qp-line)`
- `safe-char := <octet decimal 33–60, 62–126>`
- `subtype := extension-token / iana-token`
- `token := 1*<any US-ASCII CHAR except SPACE, CTLs, or tspecials>`
- `transport-padding := *LWSP-char` (composers MUST NOT generate non-zero; receivers MUST handle)
- `tspecials := "(" / ")" / "<" / ">" / "@" / "," / ";" / ":" / "\" / <"> / "/" / "[" / "]" / "?" / "="`
- `type := discrete-type / composite-type`
- `value := token / quoted-string`
- `version := "MIME-Version" ":" 1*DIGIT "." 1*DIGIT`
- `x-token := "X-" or "x-" followed by any token` (no white space)