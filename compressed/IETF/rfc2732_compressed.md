# RFC 2732: Format for Literal IPv6 Addresses in URL's
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: December 1999 | **Type**: Normative
**Original**: [RFC 2732 text](https://datatracker.ietf.org/doc/html/rfc2732)

## Scope (Summary)
Defines a format for literal IPv6 addresses in URLs, primarily for World Wide Web browsers, and updates the generic URI syntax defined in RFC 2396 to allow use of "[" and "]" specifically for enclosing IPv6 addresses.

## Normative References
- [ARCH] Hinden, R. and S. Deering, "IP Version 6 Addressing Architecture", RFC 2373, July 1998.
- [URL] Fielding, R., Masinter, L. and T. Berners-Lee, "Uniform Resource Identifiers: Generic Syntax", RFC 2396, August 1998.
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", RFC 2119, March 1997.
- [STD-PROC] Bradner, S., "The Internet Standards Process -- Revision 3", BCP 9, RFC 2026, October 1996.

## Definitions and Abbreviations
- **IPv6address**: An IPv6 address as defined in RFC 2373 [ARCH].
- **IPv6reference**: The literal IPv6 address enclosed in "[" and "]".
- **MUST / REQUIRED / SHALL**: Absolute requirement of the specification.
- **SHOULD / RECOMMENDED**: Strongly recommended but not absolute.
- **MAY / OPTIONAL**: Optional, at implementor's discretion.

## Introduction
The textual representation of IPv6 addresses (as in [ARCH]) uses ":" and "." characters, conflicting with URL syntax. This document defines a method to embed literal IPv6 addresses in URLs by enclosing them in brackets. This format is implemented in IPv6 versions of major browsers (Microsoft Internet Explorer, Mozilla, Lynx) and is intended for use in the IPv6 service location protocol.

### Requirements Language
- Keywords (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) are as defined in [KEYWORDS].
- **SHOULD**: World Wide Web browsers SHOULD implement the format defined herein.
- **MAY**: Other applications and protocols using URLs MAY use this format.

## Literal IPv6 Address Format in URL's Syntax
- To use a literal IPv6 address in a URL, the address **SHALL** be enclosed in "[" and "]" characters.
- Examples (informative):
  - `http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html`
  - `http://[1080:0:0:0:8:800:200C:417A]/index.html`
  - `http://[3ffe:2a00:100:7031::1]`
  - `http://[1080::8:800:200C:417A]/foo`
  - `http://[::192.9.5.5]/ipng`
  - `http://[::FFFF:129.144.52.38]:80/index.html`
  - `http://[2010:836B:4179::836B:4179]`

## Changes to RFC 2396
This document updates the generic URI syntax from RFC 2396. The following changes **SHALL** be applied:

1. **Modify the `host` non-terminal** to add an `IPv6reference` option:
   ```
   host = hostname | IPv4address | IPv6reference
   ipv6reference = "[" IPv6address "]"
   ```
   (where `IPv6address` is defined in [ARCH])

2. **Replace the definition of `IPv4address`** with that from RFC 2373 (at most three decimal digits per segment).

3. **Add "[" and "]" to the set of `reserved` characters**:
   ```
   reserved = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
              "$" | "," | "[" | "]"
   ```
   **Remove "[" and "]" from the `unwise` set**:
   ```
   unwise = "{" | "}" | "|" | "\" | "^" | "`"
   ```

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | World Wide Web browsers SHOULD implement the format of IPv6 literals in URLs defined in this document. | SHOULD | Section 1.1 |
| R2 | Other types of applications and protocols that use URLs MAY use this format. | MAY | Section 1.1 |
| R3 | The literal address in a URL SHALL be enclosed in "[" and "]" characters. | SHALL | Section 2 |
| R4 | Syntax changes to RFC 2396: (1) add IPv6reference to `host`, (2) replace IPv4address definition, (3) add "[" and "]" to reserved, remove from unwise. | SHALL (normative update) | Section 3 |

## Security Considerations
No new security concerns are introduced by this specification.

## IANA Considerations
None.

## Informative Annexes (Condensed)
- **Authors' Addresses**: Robert M. Hinden (Nokia), Brian E. Carpenter (IBM), Larry Masinter (AT&T Labs) – email and postal addresses provided.
- **Full Copyright Statement**: Standard IETF copyright, allowing unlimited distribution and derivative works with notice, subject to Internet Standards process.
- **Acknowledgement**: Funding for RFC Editor provided by Internet Society.