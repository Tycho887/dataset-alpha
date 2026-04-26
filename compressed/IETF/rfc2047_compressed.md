# RFC 2047: MIME (Multipurpose Internet Mail Extensions) Part Three: Message Header Extensions for Non-ASCII Text
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: November 1996 | **Type**: Normative
**Obsoletes**: RFC 1521, 1522, 1590

## Scope (Summary)
This document defines extensions to RFC 822 to allow non-ASCII text data in Internet mail header fields by using "encoded-words" – sequences of printable ASCII characters that encode the original text in a specified character set and encoding. It specifies syntax, character sets, encodings (B and Q), and rules for placement and display in headers, while maintaining backward compatibility with existing mail handling software.

## Normative References
- [RFC 822] Crocker, D., "Standard for the Format of ARPA Internet Text Messages", STD 11, August 1982.
- [RFC 2045] Borenstein, N., and N. Freed, "MIME Part One: Format of Internet Message Bodies", November 1996.
- [RFC 2046] Borenstein, N., and N. Freed, "MIME Part Two: Media Types", November 1996.
- [RFC 2048] Freed, N., Klensin, J., and J. Postel, "MIME Part Four: Registration Procedures", November 1996.
- [RFC 2049] Borenstein, N., and N. Freed, "MIME Part Five: Conformance Criteria and Examples", November 1996.

## Definitions and Abbreviations
- **ASCII**: ANSI X3.4-1986; MIME charset name is "US-ASCII".
- **encoded-word**: A sequence of printable ASCII characters beginning with "=?", ending with "?=", with two "?"s in between, containing charset, encoding, and encoded-text.
- **charset**: Character set name allowed in MIME text/plain charset parameter (case-insensitive token).
- **encoding**: Encoding method; initially "Q" or "B" (case-insensitive token).
- **token**: 1*<Any CHAR except SPACE, CTLs, and especials>.
- **especials**: "(" / ")" / "<" / ">" / "@" / "," / ";" / ":" / "\"" / "/" / "[" / "]" / "?" / "." / "=".
- **encoded-text**: 1*<Any printable ASCII character other than "?" or SPACE> (subject to further restrictions in section 5).
- **linear-white-space**: As defined in RFC 822.
- **atom, comment, ctext, phrase, word, addr-spec, quoted-string, quoted-pair, SPACE, CHAR, CTLs**: As defined in RFC 822.

## 1. Introduction
Describes techniques to encode non-ASCII text in RFC 822 message headers using encoded-words. Avoids reliance on little-used RFC 822 features to prevent breakage of existing mail software.

## 2. Syntax of encoded-words
- **encoded-word** = "=?" charset "?" encoding "?" encoded-text "?="
- No white space allowed between components.
- Maximum length: 75 characters (including all delimiters). For longer text, multiple encoded-words separated by CRLF SPACE may be used.
- Each line containing encoded-word(s) is limited to 76 characters.
- **Important**: Encoded-words are designed to be recognized as atoms by RFC 822 parsers; SPACE and HTAB are FORBIDDEN within an encoded-word.

## 3. Character sets
- charset parameter can be any MIME charset registered with IANA for text/plain.
- For character sets using code-switching, unencoded text MUST switch back to ASCII mode at the end of each encoded-word.
- Recommendation: Use ISO-8859-* series when multiple charsets are possible.

## 4. Encodings
- Initially "Q" and "B". Mail readers MUST accept either encoding for any supported charset.
- Mail readers claiming to recognize encoded-words MUST support both encodings.

### 4.1. The "B" encoding
- Identical to BASE64 encoding defined in RFC 2045.

### 4.2. The "Q" encoding
- Similar to Quoted-Printable from RFC 2045.
- Any 8-bit value may be represented by "=" followed by two hex digits (upper case for A-F).
- SPACE (hex 20) may be represented as "_" (underscore, ASCII 95.).
- Printable ASCII characters other than "=", "?", and "_" MAY be represented as themselves, subject to section 5 restrictions. SPACE and TAB MUST NOT be represented as themselves within encoded-words.

## 5. Use of encoded-words in message headers
1. **In '*text' fields** (Subject, Comments, extension headers, user-defined X- headers): An encoded-word may replace a 'text' token. MUST be separated from adjacent encoded-word or text by linear-white-space.
2. **Within a 'comment'**: Encoded-word may appear wherever 'ctext' is allowed. "Q"-encoded encoded-word MUST NOT contain "(", ")" or "\"". MUST be separated from adjacent encoded-word or ctext by linear-white-space. Comments are only recognized in structured field bodies.
3. **Within a 'phrase'** (e.g., before an address in From/To/Cc): As replacement for a 'word'. "Q"-encoded encoded-word restricted to: <upper/lower case letters, digits, "!", "*", "+", "-", "/", "=", "_">. MUST be separated from adjacent word/text/special by linear-white-space.

**Prohibited locations**:
- MUST NOT appear in any portion of an 'addr-spec'.
- MUST NOT appear within a 'quoted-string'.
- MUST NOT be used in a Received header field.
- MUST NOT be used in a parameter of MIME Content-Type or Content-Disposition field, or in any structured field body except within a 'comment' or 'phrase'.

**Additional rules**:
- Encoded-text must be self-contained; must not be continued from one encoded-word to another. Each encoded-word MUST encode an integral number of octets and MUST represent an integral number of characters. Multi-octet characters must not be split across adjacent encoded-words.
- Only printable and white space character data should be encoded. Use to encode non-textual data is not defined by this memo.

## 6. Support of encoded-words by mail readers
### 6.1. Recognition of encoded-words in message headers
- **In '*text' fields**: Beginning at field-body start and after each linear-white-space, each sequence of up to 75 printable characters (no linear-white-space) should be examined to see if it is an encoded-word; others treated as ordinary ASCII text.
- **In structured fields**: Parse according to syntax rules; any 'word' within a 'phrase' that meets encoded-word syntax should be treated as such.
- **Within 'comment'**: Any sequence of up to 75 printable characters (no linear-white-space) that meets encoded-word syntax should be treated as encoded-word.
- **MIME-Version header**: NOT required for interpretation of encoded-words.

### 6.2. Display of encoded-words
- Recognized encoded-words are decoded; if possible the unencoded text is displayed in the original character set.
- Decoding and display occurs *after* parsing of structured field bodies.
- **Linear-white-space between adjacent encoded-words is ignored** for display (allows long strings without interspersed spaces).
- If encoding is unsupported: may display as ordinary text or substitute appropriate message.
- If charset is unsupported: may display as ordinary text, make best effort, or substitute message.
- For code-switching charsets: display implicitly begins in ASCII mode; output device MUST be returned to ASCII mode after display.

### 6.3. Mail reader handling of incorrectly formed encoded-words
- Examples of incorrect formation: characters illegal for encoding, non-integral number of characters/octets.
- Mail reader need not attempt to display such text, but MUST NOT prevent display or handling of the message.

## 7. Conformance
- **Mail composing program**: MUST ensure that any string of non-white-space printable ASCII within '*text' or '*ctext' that begins with "=?" and ends with "?=" is a valid encoded-word. Any 'word' within a 'phrase' that begins with "=?" and ends with "?=" must be a valid encoded-word.
- **Mail reading program**: MUST distinguish encoded-words from text/ctext/words according to section 6 rules. MUST support both "B" and "Q" encodings for any supported charset. Must display unencoded text if charset is US-ASCII. For ISO-8859-* charsets, must at least display characters also in ASCII set.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Encoded-word syntax: "=?" charset "?" encoding "?" encoded-text "?=" | shall | Section 2 |
| R2 | No white space within encoded-word | shall (FORBIDDEN) | Section 2 |
| R3 | Max encoded-word length 75 characters | shall | Section 2 |
| R4 | Each line containing encoded-word(s) limited to 76 characters | shall | Section 2 |
| R5 | For code-switching charsets, ASCII mode must be re-selected at end of each encoded-word | shall (MUST) | Section 3 |
| R6 | Mail reader must accept both "B" and "Q" encodings for any supported charset | shall (MUST) | Section 4 |
| R7 | Encoded-words in '*text' fields: separated by linear-white-space | shall (MUST) | Section 5(1) |
| R8 | Encoded-words in phrase: restricted characters for "Q" encoding | shall (MUST NOT contain other chars) | Section 5(3) |
| R9 | Encoded-word not allowed in addr-spec, quoted-string, Received header, or MIME Content-Type/Disposition parameters | shall (MUST NOT) | Section 5 |
| R10 | Encoded-text must be self-contained (not continued between encoded-words) | shall (MUST) | Section 5 |
| R11 | Each encoded-word must encode integral number of octets and represent integral number of characters | shall (MUST) | Section 5 |
| R12 | Mail reader must ignore linear-white-space between adjacent encoded-words for display | shall (ignored) | Section 6.2 |
| R13 | Mail reader must not prevent display/handling of message due to incorrectly formed encoded-word | shall (MUST NOT) | Section 6.3 |
| R14 | Composer: ensure any string beginning "=?" and ending "?=" in specified places is valid encoded-word | shall (MUST) | Section 7 |
| R15 | Reader: distinguish encoded-words per section 6, support both encodings, display US-ASCII text | shall (MUST) | Section 7 |

## Informative Annexes (Condensed)
- **Section 8 (Examples)**: Provides sample headers with encoded-words in From, To, Cc, Subject fields, and illustrates display behavior with adjacent linear-white-space. Demonstrates handling in structured vs. '*text' fields.
- **Section 10 (Security Considerations)**: Security issues are not discussed in this memo.
- **Section 11 (Acknowledgements)**: Thanks to contributors.
- **Appendix (Changes since RFC 1522)**: Summary of editorial and clarificatory changes, including explicit statement that MIME-Version is not required, prohibition of SPACE/TAB within encoded-words, clarification of allowed locations, and other refinements.