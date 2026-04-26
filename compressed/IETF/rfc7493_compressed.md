# RFC 7493: The I-JSON Message Format
**Source**: IETF (Standards Track) | **Version**: March 2015 | **Date**: March 2015 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7493

## Scope (Summary)
I-JSON (“Internet JSON”) is a restricted profile of JSON defined to maximize interoperability and increase confidence that software can process it with predictable results. It imposes extra constraints on JSON texts as defined in RFC 7159.

## Normative References
- [RFC2119] Bradner, S., “Key words for use in RFCs to Indicate Requirement Levels”, BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., “UTF-8, a transformation format of ISO 10646”, STD 63, RFC 3629, November 2003.
- [RFC3339] Klyne, G. and C. Newman, “Date and Time on the Internet: Timestamps”, RFC 3339, July 2002.
- [RFC4648] Josefsson, S., “The Base16, Base32, and Base64 Data Encodings”, RFC 4648, October 2006.
- [RFC7159] Bray, T., Ed., “The JavaScript Object Notation (JSON) Data Interchange Format”, RFC 7159, March 2014.
- [IEEE754] IEEE, “IEEE Standard for Floating-Point Arithmetic”, IEEE 754-2008, 2008.
- [UNICODE] The Unicode Consortium, “The Unicode Standard”, latest version.

## Definitions and Abbreviations
- **Object, Member, Array, Number, Name, String**: As defined in RFC 7159.
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL**: As defined in RFC 2119.

## 1. Introduction (Informative)
RFC 7159 describes JSON but allows idioms that cause interoperability problems. I-JSON specifies a restricted profile that enforces good practices to avoid these problems.

## 2. I-JSON Messages
### 2.1. Encoding and Characters
- **I-JSON messages MUST be encoded using UTF-8** [RFC3629].
- **Object member names and string values in arrays and object members MUST NOT include code points that identify Surrogates or Noncharacters** as defined by [UNICODE]. This applies to both directly encoded and escaped characters (e.g., `"\uDEAD"` is invalid, `"\uD800\uDEAD"` is legal).

### 2.2. Numbers
- **I-JSON messages SHOULD NOT include numbers that express greater magnitude or precision than an IEEE 754 double precision number provides** (e.g., `1E400` or `3.141592653589793238462643383279`).
- **An I-JSON sender cannot expect a receiver to treat an integer whose absolute value is greater than 9007199254740991 (i.e., outside the range [-(2⁵³)+1, (2⁵³)-1]) as an exact value.**
- **For applications that require exact interchange of numbers with greater magnitude or precision, it is RECOMMENDED to encode them in JSON string values.** (The receiving program must understand the semantic.)

### 2.3. Object Constraints
- **Objects in I-JSON messages MUST NOT have members with duplicate names.** “Duplicate” means the names are identical sequences of Unicode characters after processing any escaped characters.
- **The order of object members does not change the meaning. A receiving implementation MAY treat two I-JSON messages as equivalent if they differ only in the order of object members.**

## 3. Software Behavior
- **Designers of protocols that use I-JSON messages SHOULD provide a way for the receiver of erroneous data to signal the problem to the sender.**
- (Informative) Receivers can reject messages that do not conform to I-JSON constraints, and protocols may require such rejection.

## 4. Recommendations for Protocol Design
### 4.1. Top-Level Constructs
- **For maximum interoperability with older implementations [RFC4627], protocol designers SHOULD NOT use top‑level JSON texts that are neither objects nor arrays.**

### 4.2. Must-Ignore Policy
- **When an implementation encounters an unrecognized protocol element, it SHOULD treat the rest of the transaction as if the element did not appear and MUST NOT treat this as an error condition.**
- **A good way to support Must‑Ignore is to require that top‑level protocol elements MUST be JSON objects, and to specify that members with unrecognized names MUST be ignored.**

### 4.3. Time and Date Handling
- **It is RECOMMENDED that all timestamp or time‑duration data items be expressed as string values in ISO 8601 format as specified in [RFC3339], with the additional restrictions: uppercase letters, timezone included (not defaulted), and optional trailing seconds included even when “00”.**
- **It is also RECOMMENDED that all time‑duration data items conform to the “duration” production in Appendix A of RFC 3339, with the same additional restrictions.**

### 4.4. Binary Data
- **When an I‑JSON protocol element must contain arbitrary binary data, it is RECOMMENDED that the data be encoded in a string value in base64url** (see Section 5 of [RFC4648]).

## 5. Security Considerations (Informative)
All security considerations of JSON (RFC 7159) apply. I-JSON forbids idioms that lead to unpredictable behavior, making it a more secure basis for Internet protocols.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | I-JSON messages MUST be encoded using UTF-8. | shall | Section 2.1 |
| R2 | Object member names and string values MUST NOT include Surrogate or Noncharacter code points (directly or escaped). | shall | Section 2.1 |
| R3 | I-JSON messages SHOULD NOT include numbers with greater magnitude or precision than IEEE 754 double precision. | should | Section 2.2 |
| R4 | Integers outside [-(2⁵³)+1, (2⁵³)-1] cannot be expected to be treated as exact values. | (informational constraint) | Section 2.2 |
| R5 | For exact interchange of numbers with greater magnitude/precision, encode them in JSON string values (RECOMMENDED). | recommended | Section 2.2 |
| R6 | Objects MUST NOT have duplicate member names (after processing escapes). | shall | Section 2.3 |
| R7 | A receiving implementation MAY treat I-JSON messages differing only in object member order as equivalent. | may | Section 2.3 |
| R8 | Protocol designers SHOULD provide a way for receivers to signal erroneous data to senders. | should | Section 3 |
| R9 | Protocol designers SHOULD NOT use top-level JSON texts that are neither objects nor arrays. | should | Section 4.1 |
| R10 | When an unrecognized protocol element is encountered, it MUST NOT be treated as an error (Must‑Ignore). | shall | Section 4.2 |
| R11 | Top‑level protocol elements MUST be JSON objects, and unrecognized member names MUST be ignored (for Must‑Ignore support). | shall | Section 4.2 |
| R12 | Time/duration data items SHOULD be expressed as ISO 8601 strings per RFC 3339 with uppercase, timezone included, and optional seconds. | should | Section 4.3 |
| R13 | Time‑duration data items SHOULD conform to the RFC 3339 “duration” production with same restrictions. | should | Section 4.3 |
| R14 | Binary data SHOULD be encoded in base64url string values. | should | Section 4.4 |

## Informative Annexes (None)
(I‑JSON has no annexes; all sections are either normative or informative as indicated.)