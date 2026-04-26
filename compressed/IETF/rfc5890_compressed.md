# RFC 5890: Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework
**Source**: IETF | **Version**: Standards Track (obsoletes RFC 3490) | **Date**: August 2010 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc5890

## Scope (Summary)
This document is part of the IDNA2008 specification set. It provides definitions, terminology, and document framework common to the IDNA2008 protocol suite, superseding the earlier IDNA2003 (RFC 3490, RFC 3491). It is intended for protocol implementers and policy makers.

## Normative References
- **[ASCII]**: ANSI X3.4-1968 (USA Code for Information Interchange)
- **[RFC1034]**: STD 13, Domain names - concepts and facilities
- **[RFC1035]**: STD 13, Domain names - implementation and specification
- **[RFC1123]**: STD 3, Requirements for Internet Hosts - Application and Support
- **[RFC2119]**: BCP 14, Key words for use in RFCs to Indicate Requirement Levels
- **[Unicode-UAX15]**: Unicode Standard Annex #15, Unicode Normalization Forms, Revision 31
- **[Unicode52]**: The Unicode Standard, Version 5.2.0

## Definitions and Abbreviations
### Characters and Character Sets
- **Code point**: An integer value in the codespace of a coded character set (Unicode: 0 to 0x10FFFF).
- **Unicode**: A coded character set (v5.2) with >100,000 characters. Notation: U+XXXX.
- **ASCII**: US-ASCII, 128 characters (code points 0000..007F). Unicode is a superset.
- **Letters**: Characters with Unicode General Category starting with "L".

### DNS-Related Terminology
- **Label**: An individual component of a domain name (e.g., "www", "example" in "www.example.com"). IDNA extends usable characters for text labels.
- **Lookup**: Combination of IDNA2008 protocol operations and DNS resolver operations.
- **Registration**: Process of placing an entry into the DNS.
- **Registry/Zone administrator**: Used interchangeably regardless of DNS tree level.
- **LDH code point**: ASCII letters (U+0041-005A, U+0061-007A), digits (U+0030-0039), and hyphen-minus (U+002D).

### Terminology Specific to IDNA
#### LDH Label (Section 2.3.1)
Classical label form for hostnames (RFC 952, RFC 1034 as modified by RFC 1123): ASCII letters, digits, hyphen; hyphen not at beginning or end; total length ≤ 63 octets.
- **Reserved LDH (R-LDH) labels**: Contain "--" in third and fourth characters.
- **Non-Reserved LDH (NR-LDH) labels**: Valid LDH labels without "--" in third and fourth positions.
- **XN-labels**: R-LDH labels beginning with "xn--" (case-independent).
- **A-labels**: XN-labels whose remainder is valid Punycode output and meets IDNA-validity criteria. Must be produced only in lowercase.
- **Fake A-labels**: XN-labels that are not valid Punycode output or fail other IDNA tests.
- **Other R-LDH labels (not "xn--")**: MUST NOT be processed as ordinary LDH labels by IDNA-conforming programs. SHOULD NOT be mixed with IDNA labels in the same zone.

#### Terms for IDN Label Codings (Section 2.3.2)
- **IDNA-valid string**: Meets all requirements of these specifications for an IDNA label. Must conform to basic DNS label requirements.
- **A-label**: The ACE (ASCII-Compatible Encoding) form. Begins with "xn--" followed by valid Punycode output (max 59 ASCII chars). Must be a complete label.
- **U-label**: An IDNA-valid string of Unicode characters in NFC, including at least one non-ASCII character. Subject to constraints in Protocol (RFC 5891), Tables (RFC 5892), Bidi (RFC 5893), and symmetry constraint.
- **Symmetry constraint**: A-label A1 must be convertible to U-label U1 and vice versa. Both must be in Unicode NFC.
- **Allowed categories for IDNA-aware applications**: A-label, U-label, NR-LDH label. Only A-labels are valid among R-LDH labels.
- **Unvalidated/putative/apparent labels**: Strings in form of A-label or U-label but not yet verified.

#### NR-LDH Label (Section 2.3.2.2)
All-ASCII label obeying LDH syntax, neither IDN nor R-LDH. All A-labels obey hostname rules except length.

#### Internationalized Domain Name and Internationalized Label (Section 2.3.2.3)
- **Internationalized Domain Name (IDN)**: Domain name containing at least one A-label or U-label.
- **Internationalized Label**: Single label of an IDN (NR-LDH, A-label, or U-label). Excludes underscore labels (e.g., SRV).

#### Label Equivalence (Section 2.3.2.4)
Equivalence defined by A-labels using case-independent comparison. Only equivalents:
- Exact matches between U-labels.
- Case-insensitive matches between A-labels.
- Equivalence between U-label and A-label via translation and case-insensitive match.

#### ACE Prefix (Section 2.3.2.5)
The string "xn--" appearing at the beginning of every A-label.

#### Domain Name Slot (Section 2.3.2.6)
- **Domain name slot**: Protocol element or function argument explicitly designated for a domain name. Examples: QNAME, gethostbyname() argument, email address after "@", host portion of URI.
- **IDNA-aware domain name slot**: Explicitly designated for an IDN (static or dynamic).

#### Order of Characters in Labels (Section 2.3.3)
Characters are numbered strictly in wire order: leftmost first in LTR, rightmost first in RTL.

#### Punycode (Section 2.3.4)
The term "Punycode" should be used only to describe the encoding method in RFC 3492, not as an adjective.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | R-LDH labels not prefixed with "xn--" MUST NOT be processed as ordinary LDH labels by IDNA-conforming programs. | MUST NOT | Section 2.3.1 |
| R2 | R-LDH labels not prefixed with "xn--" SHOULD NOT be mixed with IDNA labels in the same zone. | SHOULD NOT | Section 2.3.1 |
| R3 | U-labels and A-labels MUST contain only characters specified in the document series and only in contexts indicated as appropriate. | MUST | Section 2.3.2.1 |
| R4 | U-labels and A-labels MUST be strings in Unicode NFC normalized form. | MUST | Section 2.3.2.1 |
| R5 | The three allowed categories for IDNA-aware applications are A-label, U-label, and NR-LDH label. | MUST interpret | Section 2.3.2.1 |
| R6 | Equivalence of labels is defined in terms of A-labels; case-independent comparison. | MUST use | Section 2.3.2.4 |

## Security Considerations (Condensed)
- **General**: Changes to DNS characteristics affect Internet security. Different interpretations of IDNs can lead to connecting to different servers. Zone administrators must be aware of character interpretation changes from IDNA2003.
- **U-label Lengths**: U-labels may be up to 252 characters; application authors must exert due caution against buffer overflow and truncation.
- **Local Character Set Issues**: Conversion between local character sets and Unicode is implementation-specific; different conversions may lead to inconsistency.
- **Visually Similar Characters**: Implementations should provide visual warnings for mixed scripts. Zone administrators may impose restrictions to minimize confusable characters.
- **IDNA Lookup and Registration**: Procedures depend on Punycode encoding. Security issues from encoding itself are not introduced beyond ACE encoding. Existing labels starting with ACE prefix may be misconstrued as A-labels.
- **Legacy IDN Strings**: URIs and other protocols permit only A-labels. Differences between IDNA2003 and IDNA2008 may be exploited in attacks; care in registry handling is required.
- **Security Differences from IDNA2003**: IDNA2008 rejects labels with unassigned code points, strengthening validation. However, pre-lookup validation by applications is reduced; risk is largely illusory per RFC 4690.
- **Summary**: No naming mechanism alone protects against spoofing, DNS attacks, etc.

## Informative Annexes (Condensed)
- **Road Map of IDNA2008 Documents (Section 1.2)**: Lists constituent documents: Defs (RFC 5890), Rationale (RFC 5894, non-normative), Protocol (RFC 5891), Bidi (RFC 5893), Tables (RFC 5892), Mapping (RFC 5891? actually referenced as [IDNA2008-Mapping], a Work in Progress). Explains that Mapping is not required.
- **Acknowledgments**: Contributions from various individuals.
- **References (Normative and Informative)**: Full bibliography.