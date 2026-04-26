# RFC 3490: Internationalizing Domain Names in Applications (IDNA)
**Source**: IETF - Network Working Group | **Version**: Standards Track | **Date**: March 2003 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc3490

## Scope (Summary)
This document defines internationalized domain names (IDNs) and a mechanism called Internationalizing Domain Names in Applications (IDNA) for handling them in a standard fashion. IDNA allows non-ASCII characters (from Unicode) to be represented using only ASCII characters in existing protocols like DNS, without changes to the existing infrastructure.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [STRINGPREP] Hoffman, P. and M. Blanchet, "Preparation of Internationalized Strings ("stringprep")", RFC 3454, December 2002.
- [NAMEPREP] Hoffman, P. and M. Blanchet, "Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)", RFC 3491, March 2003.
- [PUNYCODE] Costello, A., "Punycode: A Bootstring encoding of Unicode for use with Internationalized Domain Names in Applications (IDNA)", RFC 3492, March 2003.
- [STD3] Braden, R., "Requirements for Internet Hosts -- Communication Layers", STD 3, RFC 1122, and "Requirements for Internet Hosts -- Application and Support", STD 3, RFC 1123, October 1989.
- [STD13] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034 and "Domain names - implementation and specification", STD 13, RFC 1035, November 1987.

## Definitions and Abbreviations
- **ASCII**: US-ASCII, coded character set of 128 characters (0..7F). Unicode includes these same code points.
- **LDH code points**: ASCII letters (A-Z, a-z), digits (0-9), and hyphen-minus (U+002D). "LDH" = letters, digits, hyphen.
- **Label**: Individual part of a domain name, separated by dots. The zero-length root label is not considered a label in this specification. In this document, "label" means "text label".
- **Internationalized label**: A label to which the ToASCII operation (with UseSTD3ASCIIRules unset) can be applied without failing. Every ASCII label satisfying STD13 length restriction is an internationalized label.
- **Internationalized domain name (IDN)**: A domain name where every label is an internationalized label. Every ASCII domain name is an IDN.
- **ACE label**: ASCII Compatible Encoding label – an internationalized label rendered in ASCII, equivalent to a non-ASCII internationalized label. Every ACE label begins with the ACE prefix.
- **ACE prefix**: String "xn--" (case-insensitive) appearing at the beginning of every ACE label. All ACE labels begin with this prefix.
- **Domain name slot**: A protocol element or function argument explicitly designated for carrying a domain name (e.g., QNAME in DNS query, gethostbyname() argument, email local part after @).
- **IDN-aware domain name slot**: A domain name slot explicitly designated for carrying an IDN.
- **IDN-unaware domain name slot**: Any domain name slot that is not IDN-aware.
- **ToASCII**: Operation transforming a label (Unicode code points) into an ASCII sequence (or failing). Used before putting an IDN into an IDN-unaware slot.
- **ToUnicode**: Operation transforming a label (Unicode code points) into a non-ACE form if possible; never fails.

## Requirements and Applicability

### Requirements (Section 3.1)
IDNA conformance requires adherence to four requirements:

**R1 – Label Separator Recognition**: Whenever dots are used as label separators, the following characters MUST be recognized as dots: U+002E (full stop), U+3002 (ideographic full stop), U+FF0E (fullwidth full stop), U+FF61 (halfwidth ideographic full stop).

**R2 – ASCII-Only in IDN-Unaware Slots**: Whenever a domain name is put into an IDN-unaware domain name slot, it MUST contain only ASCII characters. Given an IDN, an equivalent domain name satisfying this can be obtained by applying ToASCII to each label and, if dots are used as separators, changing all label separators to U+002E.

**R3 – Hide ACE Labels from Users**: ACE labels obtained from domain name slots SHOULD be hidden from users when the environment can handle the non-ACE form, except when the ACE form is explicitly requested. If unknown, the application MAY use the non-ACE form (which might fail) or the ACE form (unintelligible). Given an IDN, an equivalent domain name with no ACE labels can be obtained by applying ToUnicode to each label. When R2 and R3 both apply, R2 takes precedence.

**R4 – Case-Insensitive Matching**: Whenever two labels are compared, they MUST be considered to match if and only if they are equivalent – their ASCII forms (from ToASCII) match using case-insensitive ASCII comparison. Whenever two names are compared, they MUST be considered to match if and only if their corresponding labels match, regardless of label separator forms.

### Applicability (Section 3.2)
- IDNA applies to all domain names in all domain name slots except where explicitly excluded.
- IDNs occupying domain name slots in protocols that predate IDNA MUST be in ASCII form (per R2).
- IDNA does not apply to domain names in NAME and RDATA fields of DNS resource records whose CLASS is not IN, unless future standards invite IDNA.
- No other exclusions currently; depends on CLASS, not TYPE.
- IDNA does not enable non-ASCII characters in other data types stored in domain names (e.g., email local parts in SOA RDATA). Unless email standards are revised, a domain label holding an email local part SHOULD NOT begin with the ACE prefix.

## Conversion Operations (Section 4)

### General Steps for a Whole Domain Name
1. Decide if domain name is "stored string" or "query string" per [STRINGPREP]; set AllowUnassigned flag if "queries".
2. Split domain name into individual labels (separators excluded).
3. For each label, decide whether to enforce STD3 restrictions; set UseSTD3ASCIIRules flag if yes.
4. Process each label with ToASCII (for IDN-unaware slot) or ToUnicode (for display); see R2, R3.
5. If ToASCII applied and dots used as separators, change all label separators to U+002E.

### ToASCII Operation (Section 4.1)
- Input: sequence of code points, AllowUnassigned flag, UseSTD3ASCIIRules flag.
- Output: sequence of ASCII code points or failure.
- Steps:
  1. If any code point outside ASCII (0..7F), go to step 2; else skip to step 3.
  2. Perform [NAMEPREP]; fail on error. (AllowUnassigned used.)
  3. If UseSTD3ASCIIRules is set:
     a. Verify absence of non-LDH ASCII code points (0..2C, 2E..2F, 3A..40, 5B..60, 7B..7F).
     b. Verify absence of leading/trailing hyphen-minus (U+002D).
  4. If any code point outside ASCII, go to step 5; else skip to step 8.
  5. Verify sequence does NOT begin with ACE prefix.
  6. Encode using [PUNYCODE]; fail on error.
  7. Prepend ACE prefix.
  8. Verify number of code points is 1 to 63 inclusive.
- ToASCII never alters a sequence already all-ASCII (but may fail).
- Applying multiple times same as once.

### ToUnicode Operation (Section 4.2)
- Input: sequence of code points, AllowUnassigned flag, UseSTD3ASCIIRules flag.
- Output: sequence of Unicode code points (never fails; on failure returns original input).
- Steps:
  1. If all code points in ASCII range (0..7F), skip to step 3.
  2. Perform [NAMEPREP]; fail if error (but overall operation returns original). (AllowUnassigned used.)
  3. Verify sequence begins with ACE prefix; save a copy of sequence.
  4. Remove ACE prefix.
  5. Decode using [PUNYCODE]; fail if error (return original). Save result.
  6. Apply ToASCII to the decoded result.
  7. Verify result of step 6 matches saved copy from step 3 (case-insensitive ASCII comparison); if fail, return original.
  8. Return saved copy from step 5 (decoded Unicode).

### ACE Prefix (Section 5)
- The ACE prefix is "xn--" (case-insensitive). Implementations MUST recognize it case-insensitively.
- Not all labels beginning with "xn--" are necessarily ACE labels; non-ACE labels beginning with the prefix will confuse users and SHOULD NOT be allowed in DNS zones.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Dots recognized as U+002E, U+3002, U+FF0E, U+FF61 when used as label separators. | MUST | Section 3.1 |
| R2 | Domain name in IDN-unaware slot MUST contain only ASCII characters; use ToASCII on each label and separators to U+002E. | MUST | Section 3.1 |
| R3 | ACE labels SHOULD be hidden from users when environment can handle non-ACE form; if unknown, MAY use non-ACE or ACE. ToUnicode can produce non-ACE form. When both R2 and R3 apply, R2 takes precedence. | SHOULD/MAY | Section 3.1 |
| R4 | Labels compared equivalent iff their ASCII forms (ToASCII) match case-insensitively; names match iff corresponding labels match, regardless of separator form. | MUST | Section 3.1 |
| R5 | ToASCII shall be applied before passing labels to resolver library (or any IDN-unaware slot). | MUST | Section 6.2 |
| R6 | DNS servers MUST use ACE form for internationalized labels that cannot be represented directly in ASCII; all IDNs served MUST contain only ASCII. | MUST | Section 6.3 |
| R7 | Domain names stored in zones follow "stored strings" rules from [STRINGPREP]; queries follow "queries" rule. | MUST | Section 6.2, 6.3 |
| R8 | Implementations MUST fully implement Nameprep and Punycode; neither is optional. | MUST | Section 1.3 |
| R9 | Implementations MUST NOT use more recent normalization tables than referenced in this document. | MUST | Section 10 |

## Implications for Typical Applications Using DNS (Section 6)

### Entry and Display (Section 6.1)
- Applications can accept domain names in any charset; IDNA does not affect user interface.
- ACE labels displayed or input MUST always include the ACE prefix.
- Applications MAY allow input/display of ACE labels, but not encouraged except for debugging or display limitations.
- ACE is opaque and ugly; if an option exists for user to select display method, rendering ACE SHOULD NOT be default.
- Internationalized labels SHOULD be transmitted in the character encoding and escape mechanism of the protocol/document format at that place.

### Applications and Resolver Libraries (Section 6.2)
- Applications MUST prepare labels passed to resolver library using ToASCII.
- IDNA-aware applications MUST work with both non-internationalized labels (per STD13/STD3) and internationalized labels.
- Domain names passed to resolvers or into DNS question section follow "queries" rules from [STRINGPREP].

### DNS Servers (Section 6.3)
- Domain names stored in zones follow "stored strings" rules.
- DNS servers MUST use ACE form for labels that cannot be represented directly in ASCII.
- All IDNs served by DNS servers MUST contain only ASCII characters.

### Avoiding Exposing Users to Raw ACE (Section 6.4)
- If an application decodes an ACE name but cannot show all characters (e.g., due to display limitations), it SHOULD show the name in ACE format instead of replacement character U+FFFD.
- Programs that default to ACE when characters cannot be displayed SHOULD also have a mechanism to show the ToUnicode output with replacement characters.

### DNSSEC Authentication (Section 6.5)
- DNSSEC authenticates the ASCII domain name, not the Unicode form or mapping.
- The ASCII name (ACE form) MUST be signed in the zone and MUST be validated against.
- Any proxies or forwarders that transform user input into IDNs must be earlier in the resolution flow than DNSSEC authenticating nameservers.

## Name Server Considerations (Section 7)
- Existing DNS servers do not know IDNA rules for non-ASCII forms; all channels (master files, DNS updates) are IDN-unaware. Requirement R2 provides shielding.
- Only one ASCII encoding per domain name exists due to ToASCII/ToUnicode design; no multiple ASCII encodings.
- Labels may contain octets beyond ASCII (0..7F) per [RFC2181], but no defined interpretation; only ASCII form from ToASCII is standard.

## Root Server Considerations (Section 8)
- IDNs likely longer than current domain names; root server bandwidth may increase slightly.
- Queries/responses may be longer, possibly forcing more TCP usage.

## Security Considerations (Section 10)
- Encoding does not introduce security issues beyond ACE itself.
- Different interpretations of IDNs could lead to different servers; transcoding between local charsets and Unicode is application-specific and could cause security issues.
- Normative references to [NAMEPREP], [PUNYCODE], [STRINGPREP] include their security considerations.
- If specification updates to newer Unicode normalization table, backwards incompatible changes must be handled to avoid security/operational implications.
- Implementations MUST NOT use more recent normalization tables than referenced; if unsure, application must include the table itself.
- To prevent confusion from visually similar characters, implementations are suggested to provide visual indications where domain name contains multiple scripts, or to distinguish zero/one from O/l.
- When comparing domain names for privileged/anti-privileged lists, comparisons MUST be done per R4 (case-insensitive ASCII comparison of ToASCII results).
- Existing labels that start with ACE prefix and would be altered by ToUnicode become ACE labels automatically.

## Informative Annexes (Condensed)
- **Section 1.2 (Limitations of IDNA)**: IDNA does not solve all linguistic issues; e.g., mixed traditional/simplified Chinese, Scandinavian O with diaeresis vs. O with stroke. It also does not provide high probability mapping for visual/aural input.
- **Section 3.2.2 (Non-domain-name data types)**: Example: email local parts stored in domain labels (SOA RDATA) are not covered by IDNA; unless email standards are revised, such labels SHOULD NOT begin with ACE prefix.
- **Section 9.2 (Informative References)**: Lists [RFC2535], [RFC2181], [UAX9], [UNICODE] (3.2.0), [USASCII].
- **Section 11 (IANA Considerations)**: IANA assigned the ACE prefix in consultation with IESG.