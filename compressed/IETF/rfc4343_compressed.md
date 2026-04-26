# RFC 4343: Domain Name System (DNS) Case Insensitivity Clarification
**Source**: IETF Standards Track | **Version**: RFC 4343 | **Date**: January 2006 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc4343

## Scope (Summary)
This document clarifies the meaning of “case insensitive” for DNS names, specifying that ASCII letters in DNS labels must be treated as equivalent during comparison while preserving case on output when feasible. It updates RFCs 1034, 1035, and 2181.

## Normative References
- [ASCII] ANSI X3.4, 1968
- [RFC1995] Ohta, M., “Incremental Zone Transfer in DNS”, RFC 1995, August 1996
- [RFC2119] Bradner, S., “Key words for use in RFCs to Indicate Requirement Levels”, BCP 14, RFC 2119, March 1997
- [RFC2136] Vixie, P. et al., “Dynamic Updates in the Domain Name System (DNS UPDATE)”, RFC 2136, April 1997
- [RFC2181] Elz, R. and R. Bush, “Clarifications to the DNS Specification”, RFC 2181, July 1997
- [RFC3007] Wellington, B., “Secure Domain Name System (DNS) Dynamic Update”, RFC 3007, November 2000
- [RFC3597] Gustafsson, A., “Handling of Unknown DNS Resource Record (RR) Types”, RFC 3597, September 2003
- [RFC4034] Arends, R. et al., “Resource Records for the DNS Security Extensions”, RFC 4034, March 2005
- [STD13] Mockapetris, P., “Domain names – concepts and facilities”, STD 13, RFC 1034, November 1987; “Domain names – implementation and specification”, STD 13, RFC 1035, November 1987

## Definitions and Abbreviations
- **DNS**: Domain Name System
- **DNS label**: A component of a DNS name; maximum 63 octets per label
- **ASCII label**: DNS label type 0x0; may contain arbitrary byte values but conventionally interpreted as ASCII
- **Indirect label**: Label type that is a compression pointer to another name location in a DNS message
- **Case insensitive (DNS)**: Uppercase ASCII letters (0x41–0x5A) and lowercase ASCII letters (0x61–0x7A) are considered equivalent for comparison
- **Case folding**: Converting all letters to the same case prior to comparison (not required but a possible implementation)
- **Master File**: ASCII representation of DNS zone data as defined in STD13

## 1. Introduction (Condensed)
DNS names are treated case insensitively. This document defines the exact rule and updates RFCs 1034, 1035, and 2181. The key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) are used per [RFC2119].

## 2. Case Insensitivity of DNS Labels
DNS labels are 8‑bit byte sequences; ASCII is typical but all values allowed. Case-varied alternatives (e.g., “Foo.ExamplE.net.”) are equivalent for comparison.

### 2.1. Escaping Unusual DNS Label Octets
- **Requirement**: In Master Files and human-readable ASCII contexts, the octet value for period (0x2E) and all octets outside the inclusive range 0x21 (“!”) to 0x7E (“~”) **MUST** be escaped.
- **Escape syntax**: Backslash followed by exactly three decimal digits representing the octet value (e.g., `\032` for space).
- Backslash itself can be expressed as `\092` or `\\`; period as `\046` or `\.`.
- A backslash followed by one or two decimal digits is **undefined**.
- A backslash followed by four decimal digits produces two octets: first three digits as a decimal number produce the first octet, the fourth digit becomes the second octet.

### 2.2. Example Labels with Escapes
Examples show embedded spaces, null bytes, and backslashes within labels (e.g., `Donald\032E\.\032Eastlake\0323rd.example.`).

## 3. Name Lookup, Label Types, and CLASS
### 3.1. Original DNS Label Types
- **ASCII labels** (type 0x0): length 0–63 octets; arbitrary bytes allowed; **ASCII case insensitivity** applies.
- **Indirect labels**: replaced by the target name, which is then treated with the case insensitivity rules.
- Zero-length label reserved for the root node.

### 3.2. Extended Label Type Case Insensitivity Considerations
- **ASCII case insensitivity applies only to label type 0x0** (ASCII labels), including those reached via indirect labels. Other label types (e.g., BINARY per [RFC2673]) are not subject to these rules.

### 3.3. CLASS Case Insensitivity Considerations
- **DNS label case handling is not CLASS dependent.** Uniform handling across CLASSes is required for forward compatibility. A future CLASS needing case‑sensitive labels would require a new label type.

## 4. Case on Input and Output
### 4.1. DNS Output Case Preservation
- **Requirement**: Case **MUST** be preserved on output **except** when name compression (use of indirect labels) is employed. Compression compares names case‑insensitively, so the case of the pointed‑to name may differ from the original.

### 4.2. DNS Input Case Preservation
- **Requirement**: On input (Master File, zone transfer, dynamic update), case **MUST** be preserved for newly created nodes. For existing nodes, implementations **MAY** retain the case first loaded, override it, or keep multiple capitalizations.
- Example: Loading `foo.bar.example` then `xyz.BAR.example` may result in the node name being stored as `bar` or `BAR`, or both. Retrieval with either capitalization returns all RRs. The order of insertion in a Master File is not defined, leading to unpredictable output capitalization.

## 5. Internationalized Domain Names (Informative)
Internationalized Domain Names (IDNA) per [RFC3490], [RFC3454], [RFC3491], [RFC3492] handle case insensitivity at the application level via stringprep; this is not part of the DNS as standardized in STD13.

## 6. Security Considerations (Condensed)
- Case equivalence can be exploited for user confusion (e.g., believing `Example.com` and `example.com` are different).
- Use of DNS names as case‑sensitive indices or binary data may cause issues. A canonical form (e.g., lowercasing all ASCII letters as in [RFC4034]) **SHOULD** be used to reduce risks.
- Storing case‑sensitive data (e.g., email local parts in RP records) may result in unexpected case changes and security implications.

## Normative References
[Listed in full in the Normative References section above]

## Informative References (Condensed)
- [ISO-8859-1], [ISO-8859-2] – Character encodings.
- [RFC1183] – New DNS RR Definitions.
- [RFC1591] – DNS Structure and Delegation.
- [RFC2606] – Reserved Top Level DNS Names.
- [RFC2671] – EDNS0.
- [RFC2673] – Binary Labels in DNS.
- [RFC2929] – DNS IANA Considerations.
- [RFC3092] – Etymology of “Foo”.
- [RFC3363] – Representing IPv6 in DNS.
- [RFC3454] – Stringprep.
- [RFC3490] – IDNA.
- [RFC3491] – Nameprep.
- [RFC3492] – Punycode.
- [UNICODE] – The Unicode Standard.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Uppercase ASCII letters (0x41–0x5A) MUST match the identical value and also the corresponding lowercase letter (0x61–0x7A). | MUST | Section 3 |
| R2 | Lowercase ASCII letters (0x61–0x7A) MUST match the identical value and also the corresponding uppercase letter (0x41–0x5A). | MUST | Section 3 |
| R3 | Case MUST be preserved on output, except when name compression (indirect labels) is used; compression may alter case because comparison is case‑insensitive. | MUST (with exception) | Section 4.1 |
| R4 | On input, case MUST be preserved for new nodes; for existing nodes, implementations MAY retain, override, or keep multiple capitalizations. | MUST / MAY | Section 4.2 |
| R5 | In Master Files, octet value 0x2E and all octets outside 0x21–0x7E MUST be escaped using backslash + three decimal digits. | MUST | Section 2.1 |
| R6 | ASCII case insensitivity applies only to label type 0x0 (ASCII labels). | MUST | Section 3.2 |
| R7 | DNS label case handling is not CLASS dependent. | MUST | Section 3.3 |