# RFC 8259: The JavaScript Object Notation (JSON) Data Interchange Format
**Source**: IETF | **Version**: Standards Track | **Date**: December 2017 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc8259

## Scope (Summary)
Defines the JSON data interchange format, a lightweight, text-based, language-independent serialization format. This revision removes inconsistencies with other JSON specifications, repairs specification errors, and provides interoperability guidance.

## Normative References
- [ECMA-404]: Ecma International, "The JSON Data Interchange Format", Standard ECMA-404
- [IEEE754]: IEEE, "IEEE Standard for Floating-Point Arithmetic", IEEE 754
- [RFC2119]: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC3629]: Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629
- [RFC5234]: Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234
- [RFC8174]: Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174
- [UNICODE]: The Unicode Consortium, "The Unicode Standard"

## Definitions and Abbreviations
- **JSON**: JavaScript Object Notation; a text format for serialization of structured data.
- **object**: An unordered collection of zero or more name/value pairs, where a name is a string and a value is any JSON value.
- **array**: An ordered sequence of zero or more JSON values.
- **string**: A sequence of zero or more Unicode characters.
- **number**: A numeric value represented in base 10 using decimal digits, optionally with a fraction and/or exponent.
- **value**: One of: object, array, number, string, or the literal names false, null, true.
- **ws**: Whitespace characters (space, horizontal tab, line feed, carriage return).
- **UTF-8**: A character encoding defined in RFC 3629.

## 1. Introduction
JSON is derived from ECMAScript object literals [ECMA-262]. It can represent four primitive types (strings, numbers, booleans, null) and two structured types (objects and arrays).

### 1.1. Conventions Used in This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when they appear in all capitals. Grammatical rules are interpreted per [RFC5234].

### 1.2. Specifications of JSON
This document replaces [RFC7159], which obsoleted [RFC4627]. JSON is also described in [ECMA-404]. ECMA-404 is a normative reference to ensure consistency; there are no inconsistencies in the definition of "JSON text". However, ECMA-404 allows practices that this specification recommends avoiding for interoperability. If a difference is found, ECMA and IETF will work to update both documents.

### 1.3. Introduction to This Revision
This revision applies errata from RFC 4627 and RFC 7159, removes inconsistencies, and highlights practices causing interoperability problems.

## 2. JSON Grammar
A JSON text is a sequence of tokens: six structural characters, strings, numbers, and three literal names.

```
JSON-text = ws value ws
```

Structural characters:
- `[` (begin-array)
- `{` (begin-object)
- `]` (end-array)
- `}` (end-object)
- `:` (name-separator)
- `,` (value-separator)

Whitespace (ws) is allowed before or after structural characters:
```
ws = *(
      %x20 /              ; Space
      %x09 /              ; Horizontal tab
      %x0A /              ; Line feed or New line
      %x0D )              ; Carriage return
```

## 3. Values
- **value = false / null / true / object / array / number / string**
- A JSON value MUST be an object, array, number, string, or one of the literal names `false`, `null`, `true`. The literal names MUST be lowercase. No other literal names are allowed.

## 4. Objects
- **object = begin-object [ member *( value-separator member ) ] end-object**
- **member = string name-separator value**
- The names within an object SHOULD be unique. Duplicate names cause unpredictable behavior; many implementations report only the last name/value pair.

## 5. Arrays
- **array = begin-array [ value *( value-separator value ) ] end-array**
- Elements are separated by commas; values need not be of the same type.

## 6. Numbers
- **number = [ minus ] int [ frac ] [ exp ]**
- A number is represented in base 10. It may have an optional minus sign, integer part, fraction part, and/or exponent part. Leading zeros are not allowed (except for zero itself). Numeric values like Infinity and NaN are not permitted.
- Implementations MAY set limits on range and precision. Good interoperability is achieved by using IEEE 754 binary64 (double precision). Integers in the range [-(2^53)+1, (2^53)-1] are interoperable.

## 7. Strings
- **string = quotation-mark *char quotation-mark**
- A string begins and ends with quotation marks. All Unicode characters may appear except those that MUST be escaped: quotation mark (`"`), reverse solidus (`\`), and control characters (U+0000-U+001F). Escaping can be done via two-character sequences or `\uXXXX` for BMP characters; characters outside BMP require UTF-16 surrogate pairs.

## 8. String and Character Issues

### 8.1. Character Encoding
- JSON text exchanged between systems not part of a closed ecosystem MUST be encoded using UTF-8 [RFC3629].
- Implementations MUST NOT add a byte order mark (U+FEFF) to the beginning of a networked-transmitted JSON text. Implementations MAY ignore a BOM when parsing.

### 8.2. Unicode Characters
- When all strings in a JSON text are composed entirely of Unicode characters, the text is interoperable. However, the ABNF allows bit sequences that cannot encode Unicode characters (e.g., unpaired surrogates), leading to unpredictable behavior. Implementations should avoid generating such sequences.

### 8.3. String Comparison
- Implementations that compare strings after converting escaped characters to Unicode code units will be interoperable. For example, `"a\\b"` and `"a\u005Cb"` should be considered equal.

## 9. Parsers
- A JSON parser MUST accept all texts that conform to the JSON grammar. A JSON parser MAY accept non-JSON forms or extensions.
- Implementations MAY set limits on text size, nesting depth, numeric range/precision, and string length/character contents.

## 10. Generators
- A JSON generator produces JSON text. The resulting text MUST strictly conform to the JSON grammar.

## 11. IANA Considerations
- Media type: `application/json`
- No optional parameters; no "charset" parameter defined.
- File extension: `.json`
- Macintosh file type: `TEXT`

## 12. Security Considerations
- JSON is a subset of JavaScript but excludes assignment and invocation. Using `eval()` to parse JSON is a security risk because the text could contain executable code. This applies to any programming language where JSON texts conform to that language's syntax.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | A JSON value MUST be an object, array, number, string, or one of false/null/true. | shall | 3 |
| R2 | The literal names MUST be lowercase. No other literal names are allowed. | shall | 3 |
| R3 | The names within an object SHOULD be unique. | should | 4 |
| R4 | JSON text exchanged between systems not part of a closed ecosystem MUST be encoded using UTF-8. | shall | 8.1 |
| R5 | Implementations MUST NOT add a byte order mark (U+FEFF) to the beginning of a networked-transmitted JSON text. | shall | 8.1 |
| R6 | Implementations MAY ignore a byte order mark rather than treating it as an error. | may | 8.1 |
| R7 | A JSON parser MUST accept all texts that conform to the JSON grammar. | shall | 9 |
| R8 | A JSON parser MAY accept non-JSON forms or extensions. | may | 9 |
| R9 | A JSON generator MUST produce text that strictly conforms to the JSON grammar. | shall | 10 |

## Informative Annexes (Condensed)
- **Appendix A – Changes from RFC 7159**: Lists specific changes: updates to section 1.2 (normative reference to ECMA-404), section 1.3 (errata references), section 8.1 (UTF-8 required for network transmission), section 12 (clarified eval risk), and adjustments to references.
- **Examples (Section 13)**: Provides two representative JSON examples: a nested object with array of numbers and an array of objects. Also shows minimal valid JSON values.
- **Security Considerations (Section 12)**: Highlights the risk of using eval() and similar functions; JSON should be parsed with a dedicated parser.