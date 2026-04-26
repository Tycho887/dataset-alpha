# RFC 4514: Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names
**Source**: IETF | **Version**: Standards Track, June 2006 | **Date**: June 2006 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/html/rfc4514

## Scope (Summary)
This document defines the string representation of Distinguished Names (DNs) used in LDAP. Section 2 specifies the RECOMMENDED algorithm for converting a DN from its ASN.1 structured representation to a UTF-8 string. Section 3 defines the ABNF grammar and parsing algorithm for converting a string back to a DN. All strings produced by LDAP implementations MUST conform to the grammar in Section 3.

## Normative References
- [REGISTRY] IANA, Object Identifier Descriptors Registry, <http://www.iana.org/assignments/ldap-parameters>.
- [Unicode] The Unicode Standard, Version 3.2.0 (as defined by Unicode 3.0 plus Annexes #27 and #28).
- [X.501] ITU-T, "The Directory – Models", X.501 (1993) (also ISO/IEC 9594-2:1994).
- [X.680] ITU-T, "Abstract Syntax Notation One (ASN.1) – Specification of Basic Notation", X.680 (1997) (also ISO/IEC 8824-1:1998).
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC4234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [RFC4510] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map", RFC 4510, June 2006.
- [RFC4511] Sermersheim, J., Ed., "Lightweight Directory Access Protocol (LDAP): The Protocol", RFC 4511, June 2006.
- [RFC4512] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Directory Information Models", RFC 4512, June 2006.
- [RFC4513] Harrison, R., Ed., "Lightweight Directory Access Protocol (LDAP): Authentication Methods and Security Mechanisms", RFC 4513, June 2006.
- [RFC4517] Legg, S., Ed., "Lightweight Directory Access Protocol (LDAP): Syntaxes and Matching Rules", RFC 4517, June 2006.
- [RFC4519] Sciberras, A., Ed., "Lightweight Directory Access Protocol (LDAP): Schema for User Applications", RFC 4519, June 2006.
- [RFC4520] Zeilenga, K., "Internet Assigned Numbers Authority (IANA) Considerations for the Lightweight Directory Access Protocol (LDAP)", BCP 64, RFC 4520, June 2006.

## Definitions and Abbreviations
- **DN**: Distinguished Name – the primary key to a directory entry.
- **RDN**: Relative Distinguished Name – a set of attribute value assertions.
- **AVA**: Attribute Value Assertion – a type-value pair.
- **BER**: Basic Encoding Rules (see X.690).
- **DESCR**: A short name for an AttributeType (e.g., `CN`).
- **NUMERICOID**: Dotted-decimal representation of an OBJECT IDENTIFIER.
- **UTF-8**: Unicode Transformation Format 8-bit encoding (RFC 3629).
- **Must-recognize attribute type short names** (from Section 3 grammar):

| String | X.500 AttributeType | OID |
|--------|---------------------|-----|
| CN     | commonName          | 2.5.4.3 |
| L      | localityName        | 2.5.4.7 |
| ST     | stateOrProvinceName | 2.5.4.8 |
| O      | organizationName    | 2.5.4.10 |
| OU     | organizationalUnitName | 2.5.4.11 |
| C      | countryName         | 2.5.4.6 |
| STREET | streetAddress       | 2.5.4.9 |
| DC     | domainComponent     | 0.9.2342.19200300.100.1.25 |
| UID    | userId              | 0.9.2342.19200300.100.1.1 |

These attribute types are described in [RFC4519].

## Section 1: Background and Intended Usage (Condensed)
- DNs are used in X.500 and LDAP to unambiguously refer to directory entries.
- This document specifies the LDAP string representation; its primary goal is ease of encoding/decoding, with human readability a secondary goal.
- This document does **not** define a canonical string representation; equality comparison uses distinguishedNameMatch [RFC4517].
- The key words (MUST, SHOULD, etc.) are as defined in BCP 14 [RFC2119].

## Section 2: Converting DistinguishedName from ASN.1 to a String
### 2.1 Converting the RDNSequence
- **[R1]**: If the RDNSequence is empty, the result is the empty or zero-length string.
- **[R2]**: Otherwise, the output consists of string encodings of each RelativeDistinguishedName, starting with the last element and moving backward, separated by a comma (‘,’ U+002C) character.

### 2.2 Converting RelativeDistinguishedName
- **[R3]**: Output consists of the string encodings of each AttributeTypeAndValue (in any order). Adjoining AttributeTypeAndValues are separated by a plus sign (‘+’ U+002B) character.

### 2.3 Converting AttributeTypeAndValue
- **[R4]**: Encoded as the string representation of the AttributeType, followed by an equals sign (‘=’ U+003D) character, followed by the string representation of the AttributeValue.
- **[R5]**: If the AttributeType has a registered short name (descriptor) known to be registered [RFC4520], that short name (**descr**) SHALL be used. Otherwise, the dotted-decimal encoding (**numericoid**) of its OBJECT IDENTIFIER SHALL be used.
- **[R6]**: Implementations SHOULD provide a mechanism to update their knowledge of registered short names.

### 2.4 Converting an AttributeValue from ASN.1 to a String
- **[R7]**: If the AttributeType is of dotted-decimal form, the AttributeValue is represented by a number sign (‘#’ U+0023) followed by the hexadecimal encoding of each octet of the BER encoding of the X.500 AttributeValue (hexstring form). This form is also used when the syntax does not have an LDAP-specific string encoding or that encoding is not restricted to UTF-8. This form MAY also be used in other cases (e.g., when a reversible string representation is desired – see Section 5.2).
- **[R8]**: Otherwise, if the syntax has an LDAP-specific string encoding, convert the value to a UTF-8-encoded Unicode string according to its syntax specification. If that string does not contain any of the following characters that need escaping, it MAY be used directly:
  - a space or number sign at the beginning;
  - a space at the end;
  - any of: `"`, `+`, `,`, `;`, `<`, `>`, or `\` (U+0022, U+002B, U+002C, U+003B, U+003C, U+003E, U+005C);
  - the null character (U+0000).
- **[R9]**: Each octet of a character to be escaped is replaced by a backslash and two hex digits. Alternatively, if the character is one of: ` `, `"`, `#`, `+`, `,`, `;`, `<`, `=`, `>`, or `\`, it MAY be escaped by prefixing it with a backslash.

## Section 3: Parsing a String Back to a Distinguished Name
- **[R10]**: The string representation of DNs is restricted to UTF-8 encoded Unicode characters.
- **[R11]**: The structure is specified by the following ABNF grammar (from RFC 4234):
```
distinguishedName = [ relativeDistinguishedName *( COMMA relativeDistinguishedName ) ]
relativeDistinguishedName = attributeTypeAndValue *( PLUS attributeTypeAndValue )
attributeTypeAndValue = attributeType EQUALS attributeValue
attributeType = descr / numericoid
attributeValue = string / hexstring
string = [ ( leadchar / pair ) [ *( stringchar / pair ) ( trailchar / pair ) ] ]
leadchar = LUTF1 / UTFMB
trailchar = TUTF1 / UTFMB
stringchar = SUTF1 / UTFMB
pair = ESC ( ESC / special / hexpair )
special = escaped / SPACE / SHARP / EQUALS
escaped = DQUOTE / PLUS / COMMA / SEMI / LANGLE / RANGLE
hexstring = SHARP 1*hexpair
hexpair = HEX HEX
```
- **Note**: The productions `<descr>`, `<numericoid>`, `<COMMA>`, `<DQUOTE>`, `<EQUALS>`, `<ESC>`, `<HEX>`, `<LANGLE>`, `<NULL>`, `<PLUS>`, `<RANGLE>`, `<SEMI>`, `<SPACE>`, `<SHARP>`, and `<UTFMB>` are defined in [RFC4512].
- **[R12]**: If in `<string>` form, the asserted value is obtained by replacing (left to right, non‑recursively) each `<pair>`: `<ESC><ESC>` → `<ESC>`, `<ESC><special>` → `<special>`, `<ESC><hexpair>` → the octet indicated by the `<hexpair>`.
- **[R13]**: If in `<hexstring>` form, the BER representation is obtained by converting each `<hexpair>` to the octet indicated.
- **[R14]**: Implementers MUST recognize the attribute type short names listed in the table above (CN, L, ST, O, OU, C, STREET, DC, UID). They MAY recognize other name strings.
- **[R15]**: Implementations SHOULD only generate DN strings in accordance with Section 2 of this document.

## Section 5: Security Considerations (Condensed)
- Distinguished Names often contain descriptive information that may be sensitive (e.g., full names, addresses). Server implementers should support DIT structural rules to allow administrators to select appropriate naming attributes.
- Administrators should use access controls and other mechanisms to restrict use of sensitive attributes in naming.
- Use of authentication and data security services (RFC 4513, RFC 4511) should be considered.
- **[R16]**: Applications that require reconstruction of the DER form of the value (e.g., X.509 certificate verification) SHOULD NOT use the string representation of attribute syntaxes; they SHOULD use the hexadecimal form (hexstring) prefixed by ‘#’ (U+0023) described in Section 2.4.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | If the RDNSequence is empty, the result is the empty or zero-length string. | SHALL | Section 2.1 |
| R2 | Non-empty RDNSequence: output string encodings of each RDN in reverse order, separated by comma. | SHALL | Section 2.1 |
| R3 | Multi-valued RDN: AVAs separated by plus sign. | SHALL | Section 2.2 |
| R4 | AttributeTypeAndValue: type = value. | SHALL | Section 2.3 |
| R5 | Use registered short name if available; otherwise numericoid. | SHALL | Section 2.3 |
| R6 | Implementations SHOULD provide mechanism to update knowledge of registered short names. | SHOULD | Section 2.3 |
| R7 | Dotted-decimal type or undefined string syntax: use hexstring (# followed by hex encoded BER). | SHALL | Section 2.4 |
| R8 | Syntax with LDAP-specific string encoding: convert to UTF-8; escape certain characters. | MAY (direct), SHALL (escape if needed) | Section 2.4 |
| R9 | Escaping: each octet replaced by backslash + two hex digits; alternatively, single backslash prefix for listed special characters. | SHALL (if escaping) | Section 2.4 |
| R10 | DN string representation restricted to UTF-8. | SHALL | Section 3 |
| R11 | DN strings must conform to the provided ABNF grammar. | SHALL | Section 3 |
| R12 | Parsing <string> form: replace <pair> as described. | SHALL | Section 3 |
| R13 | Parsing <hexstring> form: convert hex pairs to octets. | SHALL | Section 3 |
| R14 | Must recognize the nine attribute type short names (CN, L, ST, O, OU, C, STREET, DC, UID). | MUST | Section 3 |
| R15 | Should only generate DN strings per Section 2. | SHOULD | Section 3 |
| R16 | Applications requiring DER reconstruction: use hexstring instead of string form. | SHOULD | Section 5.2 |

## Informative Annexes (Condensed)
- **Appendix A: Presentation Issues** – The string representation is not intended for direct human presentation without translation. Guidance is provided for displaying DN strings: use hex pair escaping for non-printable characters, use `<` and `>` to delimit in free-form text (note they must be escaped within the DN), and wrap long DNs by inserting whitespace after RDN/AVA separators (with clear indication to users that added whitespace is not part of the DN). LDIF [RFC2849] is recommended for multi-line representation.
- **Appendix B: Changes Made since RFC 2253** – Summary of substantive changes: removed IESG Note, updated references, clarified canonical representation and alternative algorithms, allowed all registered short names, updated ABNF to RFC 4234, added escaping for equals sign and null character, added presentation appendix, and numerous editorial changes.