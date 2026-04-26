# RFC 7159: The JavaScript Object Notation (JSON) Data Interchange Format
**Source**: IETF | **Version**: Standards Track | **Date**: March 2014 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc7159

## Scope (Summary)
JSON is a lightweight, text-based, language-independent data interchange format derived from ECMAScript. This document removes inconsistencies with other JSON specifications, repairs errata, and offers interoperability guidance.

## Normative References
- [IEEE754] IEEE, "IEEE Standard for Floating-Point Arithmetic", IEEE Standard 754, August 2008.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [UNICODE] The Unicode Consortium, "The Unicode Standard", http://www.unicode.org/versions/latest/.

## Definitions and Abbreviations
- **JSON**: JavaScript Object Notation, a text format for serialization of structured data.
- **Object**: unordered collection of zero or more name/value pairs.
- **Array**: ordered sequence of zero or more values.
- **String**: sequence of zero or more Unicode characters.
- **Number**: representation in base 10 using decimal digits.
- **name/value pair**: member of an object, where name is a string and value is a JSON value.
- **ws**: whitespace (Space, Horizontal tab, Line feed, Carriage return).

## 1. Introduction
JSON represents four primitive types (strings, numbers, booleans, and null) and two structured types (objects and arrays). It is derived from JavaScript object literals (ECMA-262, 3rd Edition). Design goals: minimal, portable, textual, subset of JavaScript.

### 1.1. Conventions Used in This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC2119]. Grammatical rules per [RFC5234].

### 1.2. Specifications of JSON
This document updates [RFC4627]. JSON also described in ECMAScript 5.1 Section 15.12 [ECMA-262] and [ECMA-404]. All specifications agree on syntactic elements.

### 1.3. Introduction to This Revision
Applies errata (IDs 607, 3607), removes inconsistencies, highlights interoperability problems observed since RFC 4627.

## 2. JSON Grammar
A JSON text is a sequence of tokens: six structural characters, strings, numbers, three literal names. A JSON text is a serialized value (not constrained to object or array). Grammar:
```
JSON-text = ws value ws
begin-array     = ws %x5B ws  ; [
begin-object    = ws %x7B ws  ; {
end-array       = ws %x5D ws  ; ]
end-object      = ws %x7D ws  ; }
name-separator  = ws %x3A ws  ; :
value-separator = ws %x2C ws  ; ,
ws = *( %x20 / %x09 / %x0A / %x0D )
```

## 3. Values
A JSON value MUST be an object, array, number, string, or one of: `false`, `null`, `true`. Literal names MUST be lowercase. No other literal names allowed.
```
value = false / null / true / object / array / number / string
false = %x66.61.6c.73.65
null  = %x6e.75.6c.6c
true  = %x74.72.75.65
```

## 4. Objects
Object structure: curly brackets surrounding zero or more name/value pairs (members). A name is a string. A single colon after each name separates name from value. A single comma separates value from following name. Names within an object SHOULD be unique. (Normative: names SHOULD be unique.)
```
object = begin-object [ member *( value-separator member ) ] end-object
member = string name-separator value
```
Non-unique names cause unpredictable behavior. Implementations may differ on member ordering visibility; interoperability achieved when software does not depend on member ordering.

## 5. Arrays
Array structure: square brackets surrounding zero or more values (elements). Elements separated by commas. No requirement that values be same type.
```
array = begin-array [ value *( value-separator value ) ] end-array
```

## 6. Numbers
Number represented in base 10 using decimal digits. May have integer component (prefixed with optional minus), fraction part, exponent part. Leading zeros not allowed. Numeric values like Infinity and NaN not permitted.
```
number = [ minus ] int [ frac ] [ exp ]
decimal-point = %x2E       ; .
digit1-9 = %x31-39         ; 1-9
e = %x65 / %x45            ; e E
exp = e [ minus / plus ] 1*DIGIT
frac = decimal-point 1*DIGIT
int = zero / ( digit1-9 *DIGIT )
minus = %x2D               ; -
plus = %x2B                ; +
zero = %x30                ; 0
```
Implementations MAY set limits on range and precision. Good interoperability with IEEE 754-2008 binary64 (double precision). Numbers like 1E400 may indicate interoperability problems. Integers in range [-(2**53)+1, (2**53)-1] are interoperable.

## 7. Strings
String begins and ends with quotation marks. All Unicode characters allowed except those that must be escaped: quotation mark, reverse solidus, control characters (U+0000–U+001F). Escaping allowed for any character. For BMP: `\uXXXX`. For non-BMP: UTF-16 surrogate pair (12-character sequence). Two-character escape sequences for popular characters.
```
string = quotation-mark *char quotation-mark
char = unescaped /
    escape (
        %x22 /   ; "
        %x5C /   ; \
        %x2F /   ; /
        %x62 /   ; b
        %x66 /   ; f
        %x6E /   ; n
        %x72 /   ; r
        %x74 /   ; t
        %x75 4HEXDIG )  ; uXXXX
escape = %x5C
quotation-mark = %x22
unescaped = %x20-21 / %x23-5B / %x5D-10FFFF
```

## 8. String and Character Issues

### 8.1. Character Encoding
JSON text SHALL be encoded in UTF-8, UTF-16, or UTF-32. Default encoding is UTF-8. Implementations MUST NOT add a byte order mark (BOM). Interoperability: implementations MAY ignore BOM rather than treating as error.

### 8.2. Unicode Characters
Texts composed entirely of Unicode characters (however escaped) are interoperable. However, ABNF allows bit sequences that cannot encode Unicode characters (e.g., unpaired UTF-16 surrogate `\uDEAD`). Such values are unpredictable, may cause runtime exceptions.

### 8.3. String Comparison
Implementations that compare strings numerically (code unit by code unit) after transforming to Unicode code units are interoperable. Example: `"a\\b"` and `"a\u005Cb"` are equal if compared correctly (after unescaping).

## 9. Parsers
A JSON parser MUST accept all texts that conform to the JSON grammar. A JSON parser MAY accept non-JSON forms or extensions. Implementation MAY set limits on: size of texts, maximum nesting depth, range and precision of numbers, length and character contents of strings.

## 10. Generators
A JSON generator produces JSON text. Resulting text MUST strictly conform to the JSON grammar.

## 11. IANA Considerations
MIME media type: `application/json`. No required or optional parameters. Encoding considerations: binary. File extension: `.json`. No "charset" parameter defined.

## 12. Security Considerations
JSON is a subset of JavaScript excluding assignment and invocation. Use of `eval()` to parse JSON texts constitutes unacceptable security risk; applies to any language where JSON conforms to that language's syntax.

## 13. Examples (Informative - Condensed)
- Example of JSON object with nested objects and array.
- Example of JSON array containing two objects.
- Three simple JSON values: `"Hello world!"`, `42`, `true`.

## 14. Contributors
RFC 4627 written by Douglas Crockford. Majority of text is his.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A JSON value MUST be an object, array, number, string, false, null, or true. | MUST | Section 3 |
| R2 | Literal names (false, null, true) MUST be lowercase. | MUST | Section 3 |
| R3 | Names within an object SHOULD be unique. | SHOULD | Section 4 |
| R4 | JSON text SHALL be encoded in UTF-8, UTF-16, or UTF-32. | SHALL | Section 8.1 |
| R5 | Implementations MUST NOT add a byte order mark to beginning of JSON text. | MUST | Section 8.1 |
| R6 | Implementations MAY ignore byte order mark rather than treating as error. | MAY | Section 8.1 |
| R7 | A JSON parser MUST accept all texts conforming to JSON grammar. | MUST | Section 9 |
| R8 | A JSON parser MAY accept non-JSON forms or extensions. | MAY | Section 9 |
| R9 | A JSON generator MUST produce text strictly conforming to JSON grammar. | MUST | Section 10 |

## Informative Annexes (Condensed)
- **Appendix A. Changes from RFC 4627**: Summary of changes: expanded allowed JSON text to any value, clarified duplicate names, number interoperability, character encoding, security considerations, errata application, updated references.