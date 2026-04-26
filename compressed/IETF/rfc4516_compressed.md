# RFC 4516: Lightweight Directory Access Protocol (LDAP): Uniform Resource Locator
**Source**: IETF | **Version**: RFC 4516 (Standards Track) | **Date**: June 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc4516

## Scope (Summary)
This document specifies the LDAP URL format for LDAPv3, defining the syntax and semantics of an LDAP URL that describes an LDAP search operation or, in the context of referrals/references, a service where an LDAP operation may be progressed. It also defines an extension mechanism for LDAP URLs.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC4234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [RFC4510] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map", RFC 4510, June 2006.
- [RFC4511] Sermersheim, J., Ed., "Lightweight Directory Access Protocol (LDAP): The Protocol", RFC 4511, June 2006.
- [RFC4512] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Directory Information Models", RFC 4512, June 2006.
- [RFC4513] Harrison, R., Ed., "Lightweight Directory Access Protocol (LDAP): Authentication Methods and Security Mechanisms", RFC 4513, June 2006.
- [RFC4514] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names", RFC 4514, June 2006.
- [RFC4515] Smith, M. Ed. and T. Howes, "Lightweight Directory Access Protocol (LDAP): String Representation of Search Filters", RFC 4515, June 2006.

## Definitions and Abbreviations
- **LDAP**: Lightweight Directory Access Protocol.
- **LDAP URL**: A URL with scheme "ldap" that encodes an LDAP search operation or reference.
- **ABNF**: Augmented Backus-Naur Form.
- **Percent-Encoding**: Encoding of octets as "%" followed by two hexadecimal digits as per [RFC3986].

Key ABNF productions:
- `ldapurl = scheme COLON SLASH SLASH [host [COLON port]] [SLASH dn [QUESTION [attributes] [QUESTION [scope] [QUESTION [filter] [QUESTION extensions]]]]]`
- `scheme = "ldap"`
- `dn = distinguishedName` (from [RFC4514], subject to percent-encoding)
- `attributes = attrdesc *(COMMA attrdesc)`
- `scope = "base" / "one" / "sub"`
- `extensions = extension *(COMMA extension)`
- `extension = [EXCLAMATION] extype [EQUALS exvalue]`
- `extype = oid` (from [RFC4512])
- `exvalue = LDAPString` (from [RFC4511], subject to percent-encoding)
- Critical extension: prefixed with '!' (EXCLAMATION, %x21)
- Non-critical extension: no prefix.

## URL Definition
### 2. URL Definition
- **ABNF**: As above. `<host>` and `<port>` defined in [RFC3986]; `<filter>` from [RFC4515]; `<dn>` from [RFC4514]; `<attrdesc>` uses `<attributeSelector>` from [RFC4511].
- **Extension Handling**:
  - If an extension is implemented, the implementation **MUST** make use of it.
  - If an extension is not implemented and is marked critical, the implementation **MUST NOT** process the URL.
  - If an extension is not implemented and is not marked critical, the implementation **MUST** ignore the extension.
  - Use of descriptor form for `<extype>` **SHOULD** be restricted to registered OID descriptive names (see [RFC4520]).
- **Percent-Encoding** (Section 2.1):
  - A generated LDAP URL **MUST** consist only of characters from `<reserved>`, `<unreserved>`, or `<pct-encoded>` as defined in [RFC3986].
  - Implementations **SHOULD** accept other valid UTF-8 strings [RFC3629] as input.
  - An octet **MUST** be percent-encoded if:
    - It is not in the reserved or unreserved sets.
    - It is the single reserved character '?' and occurs inside `<dn>`, `<filter>`, or other element.
    - It is a comma ',' that occurs inside an `<exvalue>`.
  - The extensions component may contain null (zero) bytes; no other component may.

### 3. Defaults for Fields of the LDAP URL
- **<host>**: If absent, client must have a priori knowledge.
- **<port>**: Default TCP port 389.
- **<dn>**: If absent, default is zero-length DN "".
- **<attributes>**: If omitted, all user attributes requested (e.g., by setting AttributeDescriptionList to NULL list or using "*").
- **<scope>**: If omitted, default is "base".
- **<filter>**: If omitted, default is "(objectClass=*)".
- **<extensions>**: If omitted, no extensions assumed.
- These defaults apply unless other documents specify different rules (e.g., [RFC4511] Section 4.1.10 for referrals).

### 5. Security Considerations
- General URL security from [RFC3986] applies.
- **Client policy**: A client **SHOULD** have a user‑configurable policy controlling which servers and security mechanisms are allowed, and **SHOULD NOT** establish sessions inconsistent with policy.
- **Session reuse**: If reusing an existing LDAP session for URL resolution, the client **MUST** ensure the session is compatible with the URL and no security policies are violated.
- **Authentication**: In absence of specific policy, client should use anonymous session. Strong authentication methods **SHOULD** be used for referrals to update operations.
- **Privacy**: Opening a transport connection to another server may violate privacy; clients should provide user control over URL processing.
- **Unexpected results**: Following an LDAP URL may cause retrieval of large data or long‑lived searches; implications same as for any LDAP search query.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST make use of an implemented extension. | MUST | Section 2 |
| R2 | If an extension is not implemented and is critical, the implementation MUST NOT process the URL. | MUST | Section 2 |
| R3 | If an extension is not implemented and is not critical, the implementation MUST ignore the extension. | MUST | Section 2 |
| R4 | Use of descriptor form for extype SHOULD be restricted to registered OID descriptive names. | SHOULD | Section 2 |
| R5 | A generated LDAP URL MUST consist only of reserved, unreserved, or percent-encoded characters from [RFC3986]. | MUST | Section 2.1 |
| R6 | Implementations SHOULD accept other valid UTF-8 strings as input. | SHOULD | Section 2.1 |
| R7 | An octet MUST be percent-encoded if not in reserved or unreserved sets, or if it is '?' inside dn/filter/element, or ',' inside exvalue. | MUST | Section 2.1 |
| R8 | Client SHOULD have user-configurable policy for server/security sessions. | SHOULD | Section 5 |
| R9 | Client SHOULD NOT establish sessions inconsistent with policy. | SHOULD | Section 5 |
| R10 | When reusing an existing session for URL resolution, client MUST ensure session compatibility and policy adherence. | MUST | Section 5 |
| R11 | If an extension is not implemented and is marked critical, the implementation MUST NOT process the URL. | MUST | Section 2 |

## Informative Annexes (Condensed)
- **Appendix A: Changes Since RFC 2255**: Summary of technical and editorial changes. Key technical changes include revised ABNF, use of [RFC3986] (allowing literal IPv6 addresses), updated attribute definition to use `<attributeSelector>` from [RFC4511], and removal of the "Bindname Extension" due to lack of implementations. Editorial changes include title addition, boilerplate updates, and restructuring of sections.
- **Examples (Section 4)**: Provided to illustrate various URL constructions, including percent-encoding of reserved characters and interaction between LDAP escaping and URL encoding. No normative requirements.
- **Acknowledgements (Section 8)**: Recognizes University of Michigan, NSF, and contributions from LDAPbis WG members.