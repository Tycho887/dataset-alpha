# RFC 4627: The application/json Media Type for JavaScript Object Notation (JSON)
**Source**: IETF Network Working Group | **Version**: July 2006 | **Date**: July 2006 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc4627

## Scope (Summary)
Defines the JSON data interchange format, its grammar, encoding, and the registration of the MIME media type `application/json`. Provides normative requirements for JSON parsers and generators.

## Normative References
- [ECMA] ECMAScript Language Specification 3rd Edition (Dec. 1999)
- [RFC0020] ASCII format for network interchange (Oct. 1969)
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels (BCP 14, Mar. 1997)
- [RFC4234] Augmented BNF for Syntax Specifications: ABNF (Oct. 2005)
- [UNICODE] The Unicode Standard Version 4.0 (2003)

## Definitions and Abbreviations
- **JSON**: JavaScript Object Notation – a lightweight, text-based, language-independent data interchange format.
- **JSON text**: A serialized object or array.
- **Object**: An unordered collection of zero or more name/value pairs, where each name is a string and each value is a string, number, boolean, null, object, or array.
- **Array**: An ordered sequence of zero or more values.
- **String**: A sequence of zero or more Unicode characters.
- **Number**: An integer component optionally prefixed with minus sign, optionally followed by a fraction part and/or exponent part.
- **Boolean**: The literal names `false` or `true`.
- **Null**: The literal name `null`.
- **Structural characters**: `[`, `{`, `]`, `}`, `:`, `,`.
- **Whitespace (ws)**: Space, Horizontal tab, Line feed, Carriage return.

## 1. Introduction
JSON is a text format for serialization of structured data, derived from JavaScript object literals. It represents four primitive types (strings, numbers, booleans, null) and two structured types (objects, arrays). Design goals: minimal, portable, textual, subset of JavaScript.

### 1.1. Conventions Used in This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119]. Grammatical rules are to be interpreted as described in [RFC4234].

## 2. JSON Grammar
- **JSON-text = object / array**
- Six structural characters: `[`, `{`, `]`, `}`, `:`, `,` (each with optional whitespace before/after).
- Whitespace allowed before or after any structural character.

### 2.1. Values
- **Requirement**: A JSON value MUST be an object, array, number, or string, or one of the three literal names: `false`, `null`, `true`.
- **Requirement**: The literal names MUST be lowercase. No other literal names are allowed.
- Grammar: `value = false / null / true / object / array / number / string`

### 2.2. Objects
- An object is represented as a pair of curly brackets surrounding zero or more members (name/value pairs).
- A name is a string; a colon separates name from value; a comma separates members.
- **Requirement**: The names within an object SHOULD be unique.
- Grammar: `object = begin-object [ member *( value-separator member ) ] end-object`; `member = string name-separator value`

### 2.3. Arrays
- An array is represented as square brackets surrounding zero or more values (elements), separated by commas.
- Grammar: `array = begin-array [ value *( value-separator value ) ] end-array`

### 2.4. Numbers
- A number contains an integer component optionally prefixed with minus sign, optionally followed by a fraction part and/or exponent part.
- **Prohibited**: Octal and hex forms are not allowed. Leading zeros are not allowed.
- **Prohibited**: Numeric values that cannot be represented as sequences of digits (such as Infinity and NaN) are not permitted.
- Grammar: `number = [ minus ] int [ frac ] [ exp ]`

### 2.5. Strings
- A string begins and ends with quotation marks. All Unicode characters may be placed within except those that must be escaped: quotation mark, reverse solidus, and control characters (U+0000-U+001F).
- Escape sequences: `\"`, `\\`, `\/`, `\b`, `\f`, `\n`, `\r`, `\t`, `\uXXXX` (hex digits). Surrogate pairs for characters outside BMP.
- Grammar: `string = quotation-mark *char quotation-mark`

## 3. Encoding
- **Requirement**: JSON text SHALL be encoded in Unicode. The default encoding is UTF-8.
- Since the first two characters are always ASCII, encoding (UTF-8, UTF-16 BE/LE, UTF-32 BE/LE) can be determined by null pattern in first four octets.

## 4. Parsers
- **Requirement**: A JSON parser MUST accept all texts that conform to the JSON grammar.
- **Permission**: A JSON parser MAY accept non-JSON forms or extensions.
- Implementation may set limits on text size, nesting depth, number range, string length and character contents.

## 5. Generators
- **Requirement**: A JSON generator produces JSON text. The resulting text MUST strictly conform to the JSON grammar.

## 6. IANA Considerations
- MIME media type: `application/json`
- Required parameters: n/a
- Optional parameters: n/a
- Encoding considerations: 8bit if UTF-8; binary if UTF-16 or UTF-32.
- Security considerations: JSON is a safe subset of JavaScript (excludes assignment and invocation). Can be safely passed to `eval()` if characters not in strings are JSON tokens.
- Interoperability considerations: n/a
- Published specification: RFC 4627
- File extension: .json
- Macintosh file type: TEXT
- Intended usage: COMMON

## 7. Security Considerations
See Security Considerations in Section 6. (Summarized above: JSON excludes assignment and invocation, safe for eval with proper token check.)

## 8. Examples (Condensed)
Provides two examples: a JSON object representing an image with nested Thumbnail object and IDs array; and a JSON array of two location objects. Illustrates structure.

## 9. References
### 9.1. Normative References
- [ECMA], [RFC0020], [RFC2119], [RFC4234], [UNICODE] (as listed above).

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A JSON value MUST be an object, array, number, or string, or one of the three literal names: false, null, true. | MUST | Section 2.1 |
| R2 | The literal names MUST be lowercase. No other literal names are allowed. | MUST | Section 2.1 |
| R3 | The names within an object SHOULD be unique. | SHOULD | Section 2.2 |
| R4 | Octal and hex forms are not allowed. Leading zeros are not allowed. | MUST NOT | Section 2.4 |
| R5 | Numeric values that cannot be represented as sequences of digits (such as Infinity and NaN) are not permitted. | MUST NOT | Section 2.4 |
| R6 | JSON text SHALL be encoded in Unicode. The default encoding is UTF-8. | SHALL | Section 3 |
| R7 | A JSON parser MUST accept all texts that conform to the JSON grammar. | MUST | Section 4 |
| R8 | A JSON parser MAY accept non-JSON forms or extensions. | MAY | Section 4 |
| R9 | The resulting text MUST strictly conform to the JSON grammar. | MUST | Section 5 |

## Informative Annexes (Condensed)
- **Section 8 Examples**: Demonstrates JSON object and array structures; no normative content.
- **Section 9.2 (non-normative references)**: None present.