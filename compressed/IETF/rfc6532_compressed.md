# RFC 6532: Internationalized Email Headers
**Source**: IETF | **Version**: Standards Track | **Date**: February 2012 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc6532

## Scope (Summary)
This document extends the Internet Message Format (RFC 5322) and MIME to allow direct use of Unicode (UTF-8) in mail addresses and most header field values, eliminating the need for complex encoded‑word constructs. It also defines the `message/global` media type and updates RFC 2045 to permit non‑identity content‑transfer‑encodings on message subtypes.

## Normative References
- [ASCII] ANSI X3.4, 1986
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC3629] Yergeau, F., "UTF‑8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003
- [RFC5198] Klensin, J. and M. Padlipsky, "Unicode Format for Network Interchange", RFC 5198, March 2008
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008
- [RFC5321] Klensin, J., "Simple Mail Transfer Protocol", RFC 5321, October 2008
- [RFC5322] Resnick, P., Ed., "Internet Message Format", RFC 5322, October 2008
- [RFC6530] Klensin, J. and Y. Ko, "Overview and Framework for Internationalized Email", RFC 6530, February 2012
- [RFC6531] Yao, J. and W. Mao, "SMTP Extension for Internationalized Email", RFC 6531, February 2012
- [UNF] Davis, M. and K. Whistler, "Unicode Standard Annex #15: Unicode Normalization Forms", September 2010, <http://www.unicode.org/reports/tr15/>

## Definitions and Abbreviations
- **8‑bit**: Octets with values above 0x7F.
- **MUST / MUST NOT / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / MAY / OPTIONAL**: Interpreted as described in RFC 2119.
- **Non‑ASCII strings**: UTF-8 strings that contain at least one `<UTF8-non-ascii>` (Section 3.1).
- **Plain ASCII string**: Fully compatible with RFC 5321 and RFC 5322.

## Section 3: Changes to Message Header Fields
- **General**: RFC 5322 header definition is extended to permit non‑ASCII Unicode characters in field values. Header field names remain ASCII only.
- **Transport**: Messages in this format MUST use the SMTPUTF8 extension [RFC6531] for SMTP transfer.

### 3.1 UTF-8 Syntax and Normalization
- **Syntax**: `UTF8-non-ascii = UTF8-2 / UTF8-3 / UTF8-4` (as defined in RFC 3629, Section 4).
- **Normalization**: Unicode normalization form NFC [UNF] SHOULD be used. NFKC SHOULD NOT be used (may lose information needed for correct spelling of names).

### 3.2 Syntax Extensions to RFC 5322
The following ABNF rules are extended to allow `UTF8-non-ascii`:
- VCHAR =/ UTF8-non-ascii
- ctext =/ UTF8-non-ascii
- atext =/ UTF8-non-ascii
- qtext =/ UTF8-non-ascii
- text =/ UTF8-non-ascii (note: upgrades the body to UTF‑8)
- dtext =/ UTF8-non-ascii

These changes permit UTF‑8 in:
1. Unstructured text (e.g., "Subject:", "Content-description:")
2. Atoms (including local parts of addresses and Message-IDs; addresses in "for" clauses of "Received:" headers)
3. Quoted strings
4. Domains
- Header field names remain ASCII only.

### 3.3 Use of 8-bit UTF-8 in Message-IDs
- Implementers MAY prefer to generate ASCII Message-IDs (advantages for "In-reply-to:" and "References:" in mixed environments).

### 3.4 Effects on Line Length Limits
- Changed from 998 characters to **998 octets** (RFC 5322 Section 2.1.1 limit).
- The 78‑character limit remains in characters (display‑width purpose).

### 3.5 Changes to MIME Message Type Encoding Restrictions
- **Updates RFC 2045 Section 6.4**: Relaxes prohibition on content‑transfer‑encodings for message subtypes.
- Allows content‑transfer‑encoding for `message/global` (see Section 3.7).
- **Background**: Under 8‑bit‑clean channels, identity encoding is used. When downgrading from 8‑bit to 7‑bit (RFC 6152), encoding may be applied. Multiple transitions between environments may cause nested encodings; this is expected to be rare.

### 3.6 Use of MIME Encoded‑Words
- Encoded‑words [RFC2047] SHOULD NOT be used when generating header fields for messages employing this extension.
- Agents MAY convert encoded‑word use to direct UTF‑8 (when incorporating material from another message).
- Processors that decode encoded‑words MUST NOT generate syntactically invalid fields (ensuring the replacement does not break syntax).

### 3.7 The message/global Media Type
- **Definition**: A message is a `message/global` message if it contains 8‑bit UTF‑8 header values as specified (or 8‑bit UTF‑8 in body part header fields). Content is otherwise identical to `message/rfc822`.
- **Transmission**: MUST only be transmitted as authorized by [RFC6531] or within a non‑SMTP environment that supports these messages.
- **Downgrade**: If sent to a 7‑bit‑only system, it MUST have an appropriate content‑transfer‑encoding applied. Systems unaware of `message/global` treat it as `application/octet-stream` (RFC 2046 Section 5.2.4).
- **Registration**:
  - Type: message
  - Subtype: global
  - Required parameters: none
  - Optional parameters: none
  - Encoding considerations: Any content‑transfer‑encoding is permitted. 8‑bit or binary recommended where permitted.
  - Security considerations: See Section 4.
  - Interoperability considerations: Similar to `message/rfc822` but with internationalized headers. Systems unaware see it as unknown attachment; systems that understand provide superior functionality.
  - Published specification: RFC 6532
  - Applications: SMTP servers, email clients supporting multipart/report, forwarding.
  - File extension: `.u8msg`
  - UTI: `public.utf8-email-message` (conforms to `public.message` and `public.composite-content` but not necessarily `public.utf8-plain-text`).
  - Intended usage: COMMON
  - Restrictions: 8‑bit or binary content‑transfer‑encoding SHOULD be used unless sent over 7‑bit‑only transport.
  - Change controller: IETF Standards Process

## Section 4: Security Considerations
- UTF‑8 may increase header field and address lengths; lines MUST be ≤ 998 octets (excluding CRLF). MDA processes must handle buffer overflows, truncation, and storage allotments; when comparing addresses, use entire length.
- Multiple UTF‑8 representations can display similar characters; normalization (Section 3.1) is recommended to minimize issues.
- Impacts on email signature systems (DKIM, S/MIME, OpenPGP) are discussed in RFC 6530 Section 14.
- If a user has both non‑ASCII and ASCII mailbox addresses, a digital certificate may include both identities, as supported by PKIX (RFC 5280) and OpenPGP (RFC 3156); user‑interface issues may arise.

## Section 5: IANA Considerations
- IANA updated the registration of the `message/global` MIME type using the form in Section 3.7.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Messages in this format MUST use the SMTPUTF8 extension [RFC6531] for SMTP transfer | MUST | §3 |
| R2 | Normalization form NFC SHOULD be used; NFKC SHOULD NOT be used | SHOULD / SHOULD NOT | §3.1 |
| R3 | The line length limit is changed to 998 octets (from 998 characters). The 78‑character limit remains in characters. | MUST (octet limit) / SHOULD (78‑character) | §3.4 |
| R4 | Content‑transfer‑encoding is allowed for `message/global` and newly defined MIME types that permit it; updates RFC 2045 Section 6.4 | Permitted | §3.5 |
| R5 | Encoded‑words SHOULD NOT be used when generating header fields for messages employing this extension | SHOULD NOT | §3.6 |
| R6 | Processors that decode encoded‑words MUST NOT generate syntactically invalid fields | MUST NOT | §3.6 |
| R7 | Messages with 8‑bit UTF‑8 header values MUST be transmitted only as authorized by [RFC6531] or within a non‑SMTP environment supporting these messages | MUST | §3.7 |
| R8 | If `message/global` is sent to a 7‑bit‑only system, it MUST have an appropriate content‑transfer‑encoding applied | MUST | §3.7 |
| R9 | Each line of characters MUST be no more than 998 octets, excluding CRLF | MUST | §4 (Security) |
| R10 | MDA processes must use entire address length when comparing addresses | MUST | §4 (Security) |

## Informative Annexes (Condensed)
- **Section 1 (Introduction)**: Explains motivation for internationalized email headers, limitations of ASCII and MIME encoded‑words, and the move to native UTF‑8 support. Based on end‑to‑end 8‑bit‑clean transport. Replaces RFC 5335.
- **Section 6 (Acknowledgements)**: Thanks to Paul Hoffman, Jeff Yeh, John C Klensin, Dave Crocker, and many other contributors.
- **Section 7.2 (Informative References)**: Lists RFCs 2045, 2046, 2047, 3156, 5280, 5335, 6152 for background.