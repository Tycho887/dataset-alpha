# RFC 7049: Concise Binary Object Representation (CBOR)
**Source**: IETF | **Version**: Standards Track | **Date**: October 2013 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7049

## Scope (Summary)
Defines the Concise Binary Object Representation (CBOR), a binary data serialization format optimized for very small code size, fairly small message size, and extensibility without version negotiation. CBOR is designed for constrained nodes and high-volume applications, supports all JSON data types, and provides a self-describing encoding.

## Normative References
- [ECMA262] ECMAScript Language Specification 5.1 Edition
- [RFC2045] MIME Part One
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC3339] Date and Time on the Internet: Timestamps
- [RFC3629] UTF‑8, a transformation format of ISO 10646
- [RFC3986] URI Generic Syntax
- [RFC4287] The Atom Syndication Format
- [RFC4648] Base16, Base32, and Base64 Data Encodings
- [RFC5226] Guidelines for Writing an IANA Considerations Section
- [TIME_T] POSIX “Seconds Since the Epoch”

## Definitions and Abbreviations
- **Data item**: A single piece of CBOR data; may contain nested data items.
- **Decoder**: A process that decodes a CBOR data item and makes it available to an application.
- **Encoder**: A process that generates the representation format of a CBOR data item.
- **Data Stream**: A sequence of zero or more data items, not assembled into a larger item.
- **Well-formed**: A data item that follows the syntactic structure of CBOR, using initial bytes and implied byte strings/data items as defined, without extraneous data.
- **Valid**: A data item that is well-formed and also follows the semantic restrictions.
- **Stream decoder**: A process that decodes a data stream and makes each data item available as received.
- **byte**: synonym for “octet”. All multi‑byte values are in network byte order (big‑endian).

## 1. Introduction
CBOR is a binary serialization format whose underlying data model is an extended version of the JSON data model [RFC4627]. It is designed to be compact, code‑efficient, and extensible.

### 1.1. Objectives (in decreasing order of importance)
1. Unambiguously encode most common data formats used in Internet standards.
   - Must represent a reasonable set of basic types and structures using binary encoding; supported structures are arrays and trees only (no loops or lattices).
   - Multiple encodings for the same value (e.g., number 7) are acceptable.
2. The code for encoder or decoder MUST be implementable in a very small amount of code (e.g., class 1 constrained nodes [CNN-TERMS]). Format MUST use contemporary machine representations of data.
3. Data MUST be decodable without a schema description.
4. Serialization MUST be reasonably compact (bounded by JSON as upper bound) but code compactness takes precedence.
5. Format MUST be applicable to both constrained nodes and high-volume applications.
6. Format MUST support all JSON data types for conversion to/from JSON and MUST define a unidirectional mapping towards JSON for all data types.
7. Format MUST be extensible; extended data MUST be decodable by earlier decoders. Must support fallback so that a decoder that does not understand an extension can still decode the message. Must be able to be extended by future IETF standards.

### 1.2. Terminology
- The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” are to be interpreted as described in RFC 2119, BCP 14.
- **Data item**, **Decoder**, **Encoder**, **Data Stream**, **Well-formed**, **Valid**, **Stream decoder** – see Definitions above.
- Notation: C‑style arithmetic, “**” for exponentiation, “0x” for hex, “0b” for binary; underscores allowed for readability.

## 2. Specification of the CBOR Encoding
The initial byte of each data item contains a major type (high-order 3 bits) and additional information (low-order 5 bits). If additional information <24, it is the small unsigned integer; 24–27 indicate 1‑, 2‑, 4‑, or 8‑byte unsigned integer; 31 indicates indefinite length; 28–30 are reserved for future expansion.

### 2.1. Major Types
- **Major type 0**: Unsigned integer. Value is 5‑bit additional info or variable‑length integer following same rules.
- **Major type 1**: Negative integer. Value is -1 minus the encoded unsigned integer.
- **Major type 2**: Byte string. Length follows rules for positive integers (major type 0), then that many bytes.
- **Major type 3**: Text string (UTF‑8). Encoding identical to byte string (length is number of bytes). Unicode characters are never escaped (e.g., U+000A is always 0x0a).
- **Major type 4**: Array of data items. Length denotes number of items. Items can be of different types.
- **Major type 5**: Map of key‑value pairs. Length denotes number of pairs. Duplicate keys are well‑formed but not valid (see Section 3.7).
- **Major type 6**: Semantic tagging of other items (see Section 2.4).
- **Major type 7**: Floating‑point numbers and simple values (including “break” stop code). See Section 2.3.

### 2.2. Indefinite Lengths for Some Major Types
Four CBOR items (arrays, maps, byte strings, text strings) can be encoded with indefinite length using additional information 31, useful for streaming.

#### 2.2.1. Indefinite‑Length Arrays and Maps
- Opened with additional information 31; followed by elements; terminated by “break” (major type 7, additional info 31). “break” is not a data item.
- Nesting allowed; each indefinite item requires its own “break”.

#### 2.2.2. Indefinite‑Length Byte Strings and Text Strings
- Concatenation of definite‑length chunks of the same major type.
- **[Requirement]**: For indefinite‑length byte strings, every data item (chunk) between the indefinite‑length indicator and the “break” MUST be a definite‑length byte string item; any other type before “break” is an error.
- **[Requirement]**: For indefinite‑length text strings, every chunk MUST be a definite‑length text string; bytes of a single UTF‑8 character MUST NOT be spread across chunks.

### 2.3. Floating‑Point Numbers and Values with No Content (Major Type 7)
- 5‑bit values 0..23 are simple values.
- 5‑bit value 24: variable simple value (value 32..255 in next byte).
- 25: IEEE 754 half‑precision float (16 bits follow).
- 26: single‑precision float (32 bits).
- 27: double‑precision float (64 bits).
- 28–30: unassigned.
- 31: “break”.
- Simple values assigned: false(20), true(21), null(22), undefined(23); others unassigned/reserved.

### 2.4. Optional Tagging of Items (Major Type 6)
- A tag (major type 6) precedes a single data item. Tags give additional semantics.
- **[Requirement]**: Decoders need not understand tags; they can skip the tag and interpret the tagged data item itself.
- A tag always applies to the directly following item; tag nesting applies recursively.
- Tags define common types: dates, bignums, decimal fractions, bigfloats, content hints, etc.
- IANA maintains a tag registry (Section 7.2). Table 3 lists initial tags.

#### 2.4.1. Date and Time
- Tag value 0: date/time string per RFC 3339, refined by Section 3.3 of RFC 4287.
- Tag value 1: numeric seconds relative to 1970-01-01T00:00Z UTC (POSIX “seconds since the epoch”). The tagged item can be a positive/negative integer or floating‑point number (including fractional seconds).

#### 2.4.2. Bignums
- Tag value 2 (positive bignum) and tag value 3 (negative bignum) encode integers that do not fit in major types 0/1. The tag is on a byte string interpreted as unsigned integer n in network byte order. For tag 3, value is -1 - n.
- **[Requirement]**: Decoders that understand bignums MUST be able to decode bignums that have leading zeroes.

#### 2.4.3. Decimal Fractions and Bigfloats
- Tag value 4: decimal fraction, value = m * 10^e, represented as an array of two integers [e, m].
- Tag value 5: bigfloat, value = m * 2^e.
- e MUST be in major type 0 or 1; m can be a bignum.
- No representation of Infinity/‑Infinity/NaN; if needed, use IEEE 754 half‑precision.
- **[Quality‑of‑implementation expectation]**: When alternative representations are possible (e.g., integer vs. decimal fraction with non‑negative exponent), the integer representation should be used directly.

#### 2.4.4. Content Hints
- Tag 24: Encoded CBOR data item – tags a byte string encoded in CBOR format.
- Tags 21–23: Expected later encoding for CBOR‑to‑JSON converters (base64url, base64, base16). Tag applies to byte string or any data item containing byte strings.
- Tags 32–36: Encoded text – URI, base64url text, base64 text, regex (PCRE/JS), MIME message.

#### 2.4.5. Self‑Describe CBOR
- Tag 55799 (serialization 0xd9d9f7) marks a CBOR data item for disambiguation (e.g., from JSON). The tag imparts no extra semantics.

## 3. Creating CBOR‑Based Protocols
This section is advisory (only “MAY” language); no normative requirements beyond Section 2.

### 3.1. CBOR in Streaming Applications
- Data stream may be a sequence of CBOR data items. Decoder should immediately decode a new item if data follows.
- Some decoders may buffer until complete; others may present partial information (e.g., nested items, partial byte strings).
- Indefinite‑length encoding may cause memory allocation issues; applications should consider tradeoffs.

### 3.2. Generic Encoders and Decoders
- Generic decoders decode all well‑formed CBOR data.
- Not all well‑formed CBOR is valid (e.g., simple values <32 with extension byte, invalid UTF‑8, tag mismatch).
- Generic decoders and encoders are expected to forward unknown simple values and tags.

### 3.3. Syntax Errors
- A decoder encountering a non‑well‑formed item may fail, substitute, or take other action.

#### 3.3.1. Incomplete CBOR Data Items
- Examples: unexpected end of data before array/map count, after a tag, before indefinite‑length “break”.

#### 3.3.2. Malformed Indefinite‑Length Items
- Examples: wrong major type in chunk, missing value after key in indefinite map, “break” outside an indefinite item.

#### 3.3.3. Unknown Additional Information Values
- Unassigned additional info values (28–30) cause failure because syntax is undefined.

### 3.4. Other Decoding Errors
- Duplicate keys in map: generic decoders shall decode to map with one instance or stop; streaming decoders may not notice.
- Inadmissible type following a tag: decoders that decode into native types must check.
- Invalid UTF‑8 string: decoder may or may not verify.

### 3.5. Handling Unknown Simple Values and Tags
- **[Requirement]**: Generic decoders expected to present unknown simple values and unknown tags (with contained data item) to the application.
- Other decoders may issue warning, stop, or ignore tag.

### 3.6. Numbers
- All number representations for the same numeric value are equivalent.
- CBOR‑based protocols may restrict number representations (e.g., no floats, no 64‑bit ints).
- Encoders should use most compact integer representation; decoders should accept longer encodings.

### 3.7. Specifying Keys for Maps
- Applications should agree on key types; JSON interop likely requires UTF‑8 string keys only.
- If multiple key types used, mapping must be specified.
- Streaming decoders may not enforce uniqueness; protocol should define behavior for duplicate keys (e.g., error).
- Duplicate keys are prohibited by strict mode (Section 3.10).
- Map order has no semantic meaning; changing order should not change semantics.
- For constrained devices, use small integers (≤24) for compact keys.

### 3.8. Undefined Values
- The simple value Undefined can be used as substitute for a data item with encoding problem.

### 3.9. Canonical CBOR
- Rules for canonical encoding (protocol may define):
  - Integers must be as small as possible.
  - Lengths in major types 2–5 must be as short as possible.
  - Map keys sorted by length then byte‑wise lexical order.
  - Indefinite‑length items must be made definite.
  - For floats: test conversion from 64‑bit to 32‑bit, then 16‑bit, using shortest same‑value; NaN represented as 0xf97e00.
  - Tags: optional tags not allowed; required tags must appear.

### 3.10. Strict Mode
- **[Recommendation]**: Decoders in security‑sensitive contexts should support a strict mode that rejects ambiguously decodable data.
- Strict decoder must report error for:
  - Map with duplicate keys.
  - Tag used on incorrect data item type.
  - Data incorrectly formatted for its type (e.g., invalid UTF‑8, tag semantic violation).
- For unknown tags/simple values, strict decoder may either error or emit unknown item with indication.
- Support of strict mode is not required for all decoders, but firewalls and security systems should use it.
- Generic encoders may also provide strict mode.

## 4. Converting Data between CBOR and JSON (Non‑normative)
- Provides advice; not binding.
- CBOR‑to‑JSON: integers → number, byte strings → base64url without padding, UTF‑8 strings → JSON string with escaping, arrays → array, maps → object (only if keys are UTF‑8 strings), false/true/null → JSON equivalents, finite floats → number, non‑finite → substitute, other simple → substitute, bignums → base64url string (negative bignums prefixed with “~”), encoding hints → encoded string, other tags → ignored. Indefinite items made definite beforehand.
- JSON‑to‑CBOR: integers (no fraction) → smallest integer, longer ints → float, fractional numbers → float (shortest exact), decimals only if protocol specifies.

## 5. Future Evolution of CBOR
- CBOR has three extension points: simple values, tags, additional information.
- Unknown simple values can be processed; unknown tags can be forwarded or ignored.
- Unknown additional information values cannot be parsed; only a few remain.

### 5.1. Extension Points
- Simple space (major type 7): 24 efficient values + 224 less efficient; many unassigned.
- Tag space (major type 6): abundant; early numbers more efficient.
- Additional information space: very few codepoints left (28–30); allocations only by updating this specification.

### 5.2. Curating the Additional Information Space
- Additional information values 28 and 29 should be viewed as candidates for 128‑bit and 256‑bit quantities.
- Value 30 is the only remaining general allocation, requiring very good reason for assignment.

## 6. Diagnostic Notation (Informative)
- Human‑readable representation for debugging; not for interchange.
- Based on JSON, extended with: hex/base64 encoded byte strings (prefix h', b64', etc.), tags as <tag>(<item>), undefined as `undefined`, non‑finite as `Infinity`/`-Infinity`/`NaN`.
- Encoding indicators: `_` after `[` or `{` for indefinite length; `_` followed by digit n for additional information size (e.g., `1.5_1` for half‑precision).

## 7. IANA Considerations
- Two registries created: Simple Values and Tags.
- Simple Values: 0–19 by Standards Action (small numbers reserved), 32–255 by Specification Required.
- Tags: 0–23 Standards Action, 24–255 Specification Required, 256–18446744073709551615 First Come First Served.
- Media Type: `application/cbor`, binary encoding, file extension `.cbor`.
- CoAP Content‑Format ID: 60.
- Structured syntax suffix `+cbor` registered.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | For indefinite-length byte strings, every data item (chunk) between the indefinite-length indicator and the “break” MUST be a definite-length byte string item. | MUST | Section 2.2.2 |
| R2 | For indefinite-length text strings, every chunk MUST be a definite-length text string; bytes of a single UTF-8 character MUST NOT be spread across chunks. | MUST | Section 2.2.2 |
| R3 | Decoders that understand bignum tags (2,3) MUST be able to decode bignums that have leading zeroes. | MUST | Section 2.4.2 |
| R4 | In a decimal fraction or bigfloat array, the exponent e MUST be represented in an integer of major type 0 or 1. | MUST | Section 2.4.3 |
| R5 | For maps, duplicate keys are not valid; generic decoders that process strict mode (Section 3.10) MUST reject maps with duplicate keys. | MUST | Section 3.10, 3.7 |
| R6 | A strict decoder MUST report an error for a CBOR data item that contains a map with duplicate keys, a tag on incorrect data type, or data incorrectly formatted for its type (e.g., invalid UTF-8). | MUST | Section 3.10 |
| R7 | Generic decoders are expected to forward unknown simple values and unknown tags (with contained data item) to the application. | SHOULD | Section 3.5 |
| R8 | Encoders should use the most compact integer representation that can represent a given value. | SHOULD | Section 3.6 |
| R9 | Decoders should accept longer-than-needed integer encodings. | SHOULD | Section 3.6 |

## Informative Annexes (Condensed)
- **Appendix A (Examples)**: Provides a table of CBOR encoded values in hex and corresponding diagnostic notation for integers, floats, strings, arrays, maps, tags, indefinite-length items, and special values.
- **Appendix B (Jump Table)**: Tabular mapping of initial bytes (0x00–0xff) to structure/semantics, omitting reserved bytes and showing a selection of optional features.
- **Appendix C (Pseudocode)**: Pseudocode for checking well-formedness of CBOR items (the `well_formed` and `well_formed_indefinite` functions) and for encoding a signed integer.
- **Appendix D (Half-Precision)**: Provides C and Python code examples for decoding IEEE 754 half-precision floating-point numbers.
- **Appendix E (Comparison of Other Binary Formats)**: Compares CBOR’s design objectives with ASN.1 DER/BER/PER, MessagePack, BSON, UBJSON, and MSDTP (RFC 713), including a wire-size comparison table for a sample nested array.