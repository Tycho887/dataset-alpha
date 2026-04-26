# RFC 2141: URN Syntax
**Source**: IETF | **Version**: Standards Track | **Date**: May 1997 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc2141/

## Scope (Summary)
Uniform Resource Names (URNs) are intended as persistent, location-independent resource identifiers. This document sets forward the canonical syntax for URNs, requirements for URN presentation and transmission, and discusses lexical and functional equivalence.

## Normative References
- [1] Sollins, K.R., "Requirements and a Framework for URN Resolution Systems," Work in Progress.
- [2] Berners-Lee, T., "Universal Resource Identifiers in WWW," RFC 1630, June 1994.
- [3] Sollins, K. and L. Masinter, "Functional Requirements for Uniform Resource Names," RFC 1737, December 1994.
- [4] Berners-Lee, T., R. Fielding, L. Masinter, "Uniform Resource Locators (URL)," Work in Progress.
- [5] Appendix A.2 of The Unicode Consortium, "The Unicode Standard, Version 2.0", Addison-Wesley, 1996. ISBN 0-201-48345-9.

## Definitions and Abbreviations
- **URN**: Uniform Resource Name.
- **NID**: Namespace Identifier.
- **NSS**: Namespace Specific String.
- **URN Syntax**: `<URN> ::= "urn:" <NID> ":" <NSS>`
- **<let-num-hyp>**: `<upper> | <lower> | <number> | "-"`
- **<let-num>**: `<upper> | <lower> | <number>`
- **<trans>**: `<upper> | <lower> | <number> | <other> | <reserved>`
- **<other>**: `"(" | ")" | "+" | "," | "-" | "." | ":" | "=" | "@" | ";" | "$" | "_" | "!" | "*" | "'"`
- **<reserved>**: `"%" | "/" | "?" | "#"`
- **<excluded>**: octets 1-32, `"\" | """ | "&" | "<" | ">" | "[" | "]" | "^" | "`" | "{" | "|" | "}" | "~"`, octets 127-255
- **Lexical Equivalence**: Two URNs are lexically equivalent if octet-by-octet equal after normalizing case of "urn:", NID, and %-escaping.

## 2. Syntax
### 2.1 Namespace Identifier Syntax
- `<NID> ::= <let-num> [ 1,31 <let-num-hyp> ]`; case-insensitive.
- NID "urn" is reserved and MUST NOT be used.

### 2.2 Namespace Specific String Syntax
- `<NSS> ::= 1*<URN chars>`
- `<URN chars> ::= <trans> | "%" <hex> <hex>`
- Characters outside the URN character set MUST be translated into canonical NSS format: encode each as UTF-8 octets, then %-encode each octet (hexadecimal).

### 2.3 Reserved Characters
- "%": reserved for escape sequences; `%` in a URN MUST be followed by two <hex> characters. Literal "%" MUST be encoded as "%25". Namespaces MAY designate characters with special meaning; if same character used literally, it MUST be %-encoded. A character MUST NOT be %-encoded if not reserved.
- "/", "?", "#": RESERVED for future developments; namespace developers SHOULD NOT use them unencoded.

### 2.4 Excluded Characters
- Characters in `<excluded>` MUST be %-encoded if used in a URN.
- Octet 0 (0 hex) MUST NEVER be used.
- A URN ends when an excluded character is encountered; that character is not part of the URN.

## 3. Support of Existing and New Naming Systems
Any namespace proposed as a URN namespace that fulfills the criteria of URN namespaces MUST be expressed in this syntax. Names containing characters outside the URN character set MUST be translated into canonical form (section 2.2).

## 4. URN Presentation and Transport
- All URN transport and interchanges MUST use canonical format.
- All URN-aware applications MUST offer the option of displaying URNs in canonical form (e.g., cut-and-paste).
- Applications MAY support more human-friendly display using extended character sets.

## 5. Lexical Equivalence
- Two URNs are lexically equivalent if octet-by-octet equal after:
  1. Normalizing case of leading "urn:" token
  2. Normalizing case of NID
  3. Normalizing case of any %-escaping
- %-escaping MUST NOT be removed.
- Namespaces MAY define additional lexical equivalences; these MUST be documented during namespace registration, MUST only eliminate false negatives, and MUST NEVER say two URNs are not equivalent if the base procedure says they are equivalent.

## 6. Examples of Lexical Equivalence (condensed)
- `URN:foo:a123,456`, `urn:foo:a123,456`, `urn:FOO:a123,456` are equivalent.
- `urn:foo:A123,456` is not equivalent to any of the above.
- `urn:foo:a123%2C456` and `urn:FOO:a123%2c456` are equivalent only to each other.

## 7. Functional Equivalence
Determined by practice within a namespace; beyond the scope of this document. Namespace registration must include guidance on functional equivalence.

## 8. Security Considerations
This document specifies syntax; security considerations from special character meanings in resolvers are outside scope. It is strongly recommended that namespace registration include security considerations.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Leading "urn:" sequence is case-insensitive. | MUST | §2 |
| R2 | NID "urn" is reserved and MUST NOT be used. | MUST | §2.1 |
| R3 | Characters outside URN character set MUST be translated (UTF-8 + %-encoding). | MUST | §2.2 |
| R4 | "%" in URN MUST be followed by two <hex> characters. | MUST | §2.3.1 |
| R5 | If a namespace character has special meaning, literal use MUST be %-encoded. | MUST | §2.3.1 |
| R6 | Reserved characters "/", "?", "#" SHOULD NOT be used unencoded. | SHOULD | §2.3.2 |
| R7 | Characters in excluded set MUST be %-encoded if used in URN. | MUST | §2.4 |
| R8 | Octet 0 MUST NEVER be used. | MUST | §2.4 |
| R9 | All URN transport/interchanges MUST use canonical format. | MUST | §4 |
| R10 | URN-aware applications MUST offer option of displaying URNs in canonical form. | MUST | §4 |
| R11 | %-escaping MUST NOT be removed during lexical equivalence testing. | MUST | §5 |
| R12 | Additional lexical equivalences MUST be documented during namespace registration. | MUST | §5 |
| R13 | Additional lexical equivalences MUST NOT contradict base equivalence procedure (cannot make equivalent URNs non-equivalent). | MUST | §5 |
| R14 | URN MUST be considered an opaque URL by URL resolvers. | MUST | Appendix A |
| R15 | URL browser SHOULD display complete URN including "urn:" tag. | SHOULD | Appendix A |

## Informative Annexes (Condensed)
- **Appendix A. Handling of URNs by URL resolvers/browsers**: URNs can be used where URLs are expected. URL resolvers must treat URNs as opaque and pass to a URN resolver. To avoid confusion, browsers should display the full URN (including "urn:" tag).