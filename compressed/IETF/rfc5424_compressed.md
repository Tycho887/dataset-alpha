# RFC 5424: The Syslog Protocol

**Source**: IETF | **Version**: 1 | **Date**: March 2009 | **Type**: Standards Track  
**Original**: https://tools.ietf.org/html/rfc5424

## Scope (Summary)

Defines a layered syslog protocol for conveying event notification messages. Provides a transport‑independent message format with structured data for easy extensibility, obsoleting RFC 3164. The architecture separates message content from transport, enabling reusable code and secure, reliable transport via TLS.

## Normative References

- [ANSI.X3-4.1968] – USA Code for Information Interchange, ANSI X3.4, 1968.
- [RFC1034] – STD 13, Domain Concepts and Facilities, November 1987.
- [RFC1035] – STD 13, Domain Implementation and Specification, November 1987.
- [RFC2119] – BCP 14, Key Words for Requirement Levels, March 1997.
- [RFC2578] – STD 58, SMIv2, April 1999.
- [RFC2914] – BCP 41, Congestion Control Principles, September 2000.
- [RFC3339] – Date and Time on the Internet: Timestamps, July 2002.
- [RFC3418] – STD 62, MIB for SNMP, December 2002.
- [RFC3629] – STD 63, UTF‑8, November 2003.
- [RFC4291] – IPv6 Addressing Architecture, February 2006.
- [RFC4646] – BCP 47, Language Tags, September 2006.
- [RFC5226] – BCP 26, Guidelines for Writing IANA Considerations, May 2008.
- [RFC5234] – STD 68, Augmented BNF, January 2008.
- [RFC5425] – TLS Transport Mapping for Syslog, March 2009.
- [RFC5426] – Transmission of Syslog Messages over UDP, March 2009.
- [UNICODE-TR36] – Unicode Security Considerations, July 2005.

## Definitions and Abbreviations

- **Syslog layers**: *syslog content* (management info), *syslog application* (generation, interpretation, routing, storage), *syslog transport* (wire delivery).
- **Originator**: generates syslog content to be carried in a message.
- **Collector**: gathers syslog content for analysis.
- **Relay**: forwards messages from originators/relays to collectors/relays.
- **Transport sender/receiver**: passes syslog messages to/from a specific transport protocol.
- **SD-ID**: Structured Data ID (name of an SD-ELEMENT).
- **SD-PARAM**: a parameter name‑value pair inside an SD-ELEMENT.
- **PRIVAL**: Priority value combining Facility × 8 + Severity.
- **NILVALUE**: represented as “-”.
- **BOM**: Unicode Byte Order Mark for UTF‑8 (%xEF.BB.BF).

## Basic Principles

- No acknowledgment; simplex communication.
- Originators/relays may be configured to send the same message to multiple collectors/relays.
- Originator, relay, and collector functionality may reside on the same system.

## Transport Layer Protocol

- This document **does not specify** any transport protocol; transport mappings are defined in separate documents.
- **Any transport MUST NOT deliberately alter the syslog message.** Temporary transformations at the transport sender MUST be reversed at the transport receiver so that the relay/collector sees an exact copy.

### Minimum Required Transport Mapping

- **MUST** support TLS‑based transport per [RFC5425].
- **SHOULD** support UDP‑based transport per [RFC5426].
- **RECOMMENDED** to use TLS transport in deployments.

## Syslog Message Format

### ABNF

```
SYSLOG-MSG      = HEADER SP STRUCTURED-DATA [SP MSG]
HEADER          = PRI VERSION SP TIMESTAMP SP HOSTNAME SP APP-NAME SP PROCID SP MSGID
PRI             = "<" PRIVAL ">"
PRIVAL          = 1*3DIGIT ; 0..191
VERSION         = NONZERO-DIGIT 0*2DIGIT
HOSTNAME        = NILVALUE / 1*255PRINTUSASCII
APP-NAME        = NILVALUE / 1*48PRINTUSASCII
PROCID          = NILVALUE / 1*128PRINTUSASCII
MSGID           = NILVALUE / 1*32PRINTUSASCII
TIMESTAMP       = NILVALUE / FULL-DATE "T" FULL-TIME
FULL-DATE       = DATE-FULLYEAR "-" DATE-MONTH "-" DATE-MDAY
FULL-TIME       = PARTIAL-TIME TIME-OFFSET
PARTIAL-TIME    = TIME-HOUR ":" TIME-MINUTE ":" TIME-SECOND [TIME-SECFRAC]
TIME-SECFRAC    = "." 1*6DIGIT
TIME-OFFSET     = "Z" / ("+" / "-") TIME-HOUR ":" TIME-MINUTE
STRUCTURED-DATA = NILVALUE / 1*SD-ELEMENT
SD-ELEMENT      = "[" SD-ID *(SP SD-PARAM) "]"
SD-PARAM        = PARAM-NAME "=" %d34 PARAM-VALUE %d34
SD-ID           = SD-NAME
PARAM-NAME      = SD-NAME
PARAM-VALUE     = UTF-8-STRING ; escape '"', '\', ']' as '\"', '\\', '\]'
SD-NAME         = 1*32PRINTUSASCII ; except '=', SP, ']', %d34
MSG             = MSG-ANY / MSG-UTF8
MSG-ANY         = *OCTET ; not starting with BOM
MSG-UTF8        = BOM UTF-8-STRING
BOM             = %xEF.BB.BF
UTF-8-STRING    = *OCTET ; RFC 3629 UTF-8
```

### Message Length

- Transport receiver **MUST** accept messages up to 480 octets.
- **SHOULD** accept up to 2048 octets.
- **MAY** receive larger.
- If truncation needed, **MUST** occur at end of message; truncated message may contain invalid UTF‑8 or invalid STRUCTURED‑DATA. Transport receiver **MAY** discard or process as much as possible.

### HEADER

- Character set **MUST** be 7‑bit ASCII (ANSI X3.4‑1968).

#### PRI

- **MUST** have 3–5 characters, bound by “<” and “>”.
- PRIVAL range 0–191.
- Facility values **MUST** be 0–23; Severity values **MUST** be 0–7.
- Priority = Facility × 8 + Severity. Leading “0”s **MUST NOT** be used except for value 0.

#### VERSION

- Denotes protocol version; **MUST** be incremented for any HEADER change (addition/removal of fields or change of syntax/semantics).
- This document uses VERSION “1”.
- IANA‑assigned via Standards Action ([RFC5226]).

#### TIMESTAMP

- Formalized from [RFC3339] with restrictions:
  - “T” and “Z” **MUST** be uppercase.
  - “T” **REQUIRED**.
  - Leap seconds **MUST NOT** be used.
- **SHOULD** include TIME-SECFRAC if clock accuracy permits.
- **MUST** use NILVALUE if incapable of obtaining system time.

#### HOSTNAME

- **SHOULD** contain FQDN.
- Order of preference: FQDN → static IP → hostname → dynamic IP → NILVALUE.
- IPv4 **MUST** be dotted decimal; IPv6 **MUST** be per [RFC4291] Section 2.2.
- **SHOULD** consistently use same value.

#### APP-NAME

- **SHOULD** identify the device or application that originated the message.
- NILVALUE **MAY** be used.

#### PROCID

- No interoperable meaning; change in value indicates a discontinuity in syslog reporting.
- NILVALUE **MAY** be used.

#### MSGID

- **SHOULD** identify message type.
- NILVALUE **SHOULD** be used when no value available.

### STRUCTURED-DATA

- Contains zero or more SD‑ELEMENTS; NILVALUE if zero.
- Character set **MUST** be 7‑bit ASCII except PARAM‑VALUE (UTF‑8 **MUST** be used).
- Collector **MAY** ignore malformed STRUCTURED‑DATA; relay **MUST** forward unaltered.

#### SD-ELEMENT

- Format: `[` SD‑ID *(SP SD‑PARAM) `]`

#### SD-ID

- Case‑sensitive; same SD‑ID **MUST NOT** appear more than once in a message.
- Two formats:
  - IANA‑registered (no “@”) — **MUST** be registered via IETF Review.
  - Enterprise‑specific: `name@<private enterprise number>`
- Names **MUST NOT** contain `@`, `=`, `]`, `"`, whitespace, or control characters.

#### SD-PARAM

- PARAM‑NAME case‑sensitive; scope within SD‑ID.
- PARAM‑VALUE **MUST** be UTF‑8 encoded.
- Characters `"`, `\`, `]` **MUST** be escaped as `\"`, `\\`, `\]`.
- Invalid backslash sequences **MUST** be treated as literal (backslash + character).

#### Change Control

- Once defined, syntax and semantics **MUST NOT** be altered. New SD‑ID or PARAM‑NAME **MUST** be created for any change.

### MSG

- Free‑form message.
- **SHOULD** be UTF‑8 encoded (with BOM if UTF‑8). If not, any encoding **MAY** be used.
- **SHOULD** avoid octets < 32 (control characters). Syslog application **MAY** modify those characters upon reception.
- If BOM present, message **MUST** be shortest form per UNICODE TR36.

## Structured Data IDs (IANA‑Registered)

All are **OPTIONAL**.

### timeQuality

- `tzKnown`: “1” if time zone known, else “0”.
- `isSynced`: “1” if synchronized to reliable external source, else “0”.
- `syncAccuracy`: max microseconds off; **MUST NOT** be specified if `isSynced` is “0”.

### origin

- `ip`: IP address textual representation (per Section 6.2.4).
- `enterpriseId`: SMI Private Enterprise Code (e.g., 32473). Sub‑identifiers allowed separated by periods.
- `software`: name of generating software (max 48 chars).
- `swVersion`: version (max 32 chars).

### meta

- `sequenceId`: integer starting at 1, incremented each message, max 2147483647, then wrap to 1.
- `sysUpTime`: SNMP sysUpTime value (hundredths of a second) as decimal integer.
- `language`: BCP 47 language identifier.

## Security Considerations (Condensed)

- **UNICODE**: shortest form required to avoid spoofing per TR36.
- **Control characters**: NUL and other control chars may be exploited; syslog application may modify them.
- **Message truncation**: place important data early; originator should limit user‑supplied size.
- **Replay**: no mechanism; cryptographic signing can mitigate.
- **Reliable delivery**: not ensured; rate‑limiting may help. Reliable delivery (e.g., TLS) can intentionally discard to avoid blocking but notifies of loss.
- **Congestion control**: TLS transport required; UDP only in explicitly provisioned managed networks.
- **Message integrity**: use secure transport to prevent modification.
- **Message observation**: no confidentiality; use secure transport.
- **Inappropriate configuration**: administrator responsibility.
- **Forwarding loop**: avoid circular forwarding.
- **Load considerations**: capacity planning needed.
- **Denial of Service**: use filtering (e.g., accept only known IPs).

## IANA Considerations

- Registry “syslog Version Values”: VERSION “1” registered (Table 3).
- Registry “syslog Structured Data ID Values”: SD‑IDs `timeQuality`, `origin`, `meta` with their PARAM‑NAMEs registered (Table 4). New registrations via IETF Review.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All implementations **MUST** support TLS‑based transport (RFC 5425). | shall | Section 5.1 |
| R2 | All implementations **SHOULD** support UDP‑based transport (RFC 5426). | should | Section 5.1 |
| R3 | Transport **MUST NOT** deliberately alter the syslog message; temporary transformations **MUST** be reversed. | shall | Section 5 |
| R4 | Transport receiver **MUST** accept messages up to 480 octets. | shall | Section 6.1 |
| R5 | Transport receiver **SHOULD** accept messages up to 2048 octets. | should | Section 6.1 |
| R6 | Truncation **MUST** occur at end of message. | shall | Section 6.1 |
| R7 | HEADER character set **MUST** be 7‑bit ASCII. | shall | Section 6.2 |
| R8 | PRI **MUST** have 3–5 characters, bound by `<` and `>`. | shall | Section 6.2.1 |
| R9 | Facility values **MUST** be 0–23. | shall | Section 6.2.1 |
| R10 | Severity values **MUST** be 0–7. | shall | Section 6.2.1 |
| R11 | VERSION **MUST** be incremented for any HEADER change. | shall | Section 6.2.2 |
| R12 | TIMESTAMP **MUST** follow [RFC3339] with uppercase T/Z, T required, no leap seconds. | shall | Section 6.2.3 |
| R13 | Originator **SHOULD** include TIME‑SECFRAC if clock accuracy permits. | should | Section 6.2.3 |
| R14 | **MUST** use NILVALUE for TIMESTAMP if incapable of system time. | shall | Section 6.2.3 |
| R15 | HOSTNAME **SHOULD** be FQDN. | should | Section 6.2.4 |
| R16 | IPv6 address **MUST** per [RFC4291] Section 2.2. | shall | Section 6.2.4 |
| R17 | APP‑NAME **SHOULD** identify device/application. | should | Section 6.2.5 |
| R18 | PROCID change indicates discontinuity. | (normative statement) | Section 6.2.6 |
| R19 | MSGID **SHOULD** identify message type. | should | Section 6.2.7 |
| R20 | STRUCTURED‑DATA character set **MUST** be 7‑bit ASCII except PARAM‑VALUE (UTF‑8). | shall | Section 6.3 |
| R21 | Same SD‑ID **MUST NOT** appear more than once in a message. | shall | Section 6.3.2 |
| R22 | PARAM‑VALUE **MUST** be UTF‑8. | shall | Section 6.3.3 |
| R23 | Characters `"`, `\`, `]` in PARAM‑VALUE **MUST** be escaped. | shall | Section 6.3.3 |
| R24 | Syntax and semantics of SD‑IDs and PARAM‑NAMEs **MUST NOT** be altered. | shall | Section 6.3.4 |
| R25 | MSG **SHOULD** be UTF‑8 encoded with BOM. | should | Section 6.4 |
| R26 | If BOM present, **MUST** be shortest form. | shall | Section 6.4 |
| R27 | `tzKnown` values: “1” if time zone known, else “0”. `isSynced`: “1” if synchronized. `syncAccuracy` **MUST NOT** be specified if `isSynced` is “0”. | shall | Section 7.1 |
| R28 | `enterpriseId` **MUST** be a SMI Private Enterprise Code. | shall | Section 7.2.2 |
| R29 | `sequenceId` **MUST** start at 1, increase with every message, wrap after 2147483647 to 1. | shall | Section 7.3.1 |

## Informative Annexes (Condensed)

- **A.1 Relationship with BSD Syslog**: Compares RFC 3164 and RFC 5424; notes that PRI syntax is retained, TIMESTAMP gains year/time‑zone, HOSTNAME is more specific, TAG is split into APP‑NAME, PROCID, MSGID, and STRUCTURED‑DATA is new. Conversion guidelines are given.
- **A.2 Message Length**: Advises placing important data within the first 480 octets for robustness. Explains that larger messages may fragment and be unreliable; operators must ensure infrastructure supports required sizes.
- **A.3 Severity Values**: Recommends assigning Severity 7 for debugging, Severity 0 for critical events. Warns that severity is subjective across originators.
- **A.4 TIME-SECFRAC Precision**: Warns against removing leading zeros in fractional seconds (e.g., `.003` must not become `.3`).
- **A.5 Case Convention for Names**: Suggests lower camel case for SD‑IDs and PARAM‑NAMEs (e.g., `timeQuality`).
- **A.6 Syslog Without Knowledge of Time**: Encourages emitting a valid TIMESTAMP whenever possible; NILVALUE should be used only when truly impossible.
- **A.7 Notes on the timeQuality SD‑ID**: Recommends default `tzKnown=0` until configured; `isSynced=0` by default; accuracy should only be provided when known precisely.
- **A.8 UTF‑8 Encoding and the BOM**: Guidance on when to include the BOM: only if the syslog application is certain the MSG content is UTF‑8. Relays forwarding from non‑compliant devices may omit the BOM unless they have confirmed UTF‑8 encoding.