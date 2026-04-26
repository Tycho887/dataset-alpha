# RFC 8949: Concise Binary Object Representation (CBOR)
**Source**: IETF | **Version**: STD 94 | **Date**: December 2020 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/info/rfc8949

## Scope (Summary)
Defines the Concise Binary Object Representation (CBOR), a binary data format designed for extremely small code size, fairly small message size, and extensibility without version negotiation. Obsoletes RFC 7049, keeping full compatibility.

## Normative References
- [C] ISO/IEC 9899:2018
- [Cplusplus20] ISO/IEC DIS 14882 (N4860)
- [IEEE754] IEEE Std 754-2019
- [RFC2045] MIME Part One
- [RFC2119] Key words (BCP 14)
- [RFC3339] Date and Time on the Internet: Timestamps
- [RFC3629] UTF-8
- [RFC3986] URI Generic Syntax
- [RFC4287] Atom Syndication Format
- [RFC4648] Base16, Base32, Base64 Data Encodings
- [RFC8126] IANA Considerations (BCP 26)
- [RFC8174] Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [TIME_T] POSIX Seconds Since the Epoch

## Definitions and Abbreviations
- **Data item**: Single piece of CBOR data, may contain nested items.
- **Decoder**: Process that decodes a well-formed encoded CBOR data item for an application.
- **Encoder**: Process that generates well-formed CBOR representation.
- **Data Stream**: Sequence of zero or more data items not assembled into a larger item.
- **Well-formed**: Data item following CBOR syntactic structure; no extraneous data.
- **Valid**: Well-formed and following semantic restrictions (Section 5.3).
- **Expected**: Requirements beyond validity that an application imposes.
- **Stream decoder**: Decodes a data stream, making items available as received.
- **Byte**: Synonym for octet; multi-byte values in network byte order (big-endian).
- **Argument**: Unsigned integer derived from additional information bytes.
- **Head**: Initial byte and any additional bytes for the argument.
- **Tag**: Major type 6 data item with tag number and enclosed tag content.
- **Simple values**: Values in major type 7 (Table 4).
- **Infinity, NaN, negative zero, subnormal**: As per IEEE 754.
- **Note**: Terms and concepts from IEEE 754 are used.

## Section 1: Introduction
CBOR's data model is an extended version of the JSON data model. This document obsoletes RFC 7049.

### 1.1 Objectives (Hierarchical list preserved)
1. **Unambiguous encoding** of common data formats used in Internet standards.
   - Represent basic data types (influenced by JSON, plus byte strings).
   - Structures limited to arrays and trees.
   - Multiple encodings for same value allowed.
2. **Compact encoder/decoder code** for constrained environments.
   - Must be implementable in very small code (e.g., class 1 constrained nodes [RFC7228]).
   - Use contemporary machine representations (no binary-to-decimal conversion).
3. **Self-describing** – no schema needed for decoding.
4. **Reasonably compact serialization** – bounded by JSON; code compactness higher priority than wire compactness.
5. **Applicable to both constrained nodes and high-volume applications** – frugal in CPU usage.
6. **Support all JSON data types** for conversion to/from JSON.
   - Must allow unidirectional mapping to JSON.
7. **Extensible** – extended data decodable by earlier decoders.
   - Allow fallback for unknown extensions.
   - Must be extensible by future IETF standards.

### 1.2 Terminology (Normative key words)
Key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL) interpreted as per BCP 14 [RFC2119][RFC8174] when in all capitals.

## Section 2: CBOR Data Models

### Basic Generic Data Model
A data item is one of:
- Integer: -2^64 .. 2^64-1
- Simple value (0..255, distinct from the number)
- Floating-point value (IEEE 754 binary64, including non-finites)
- Byte string
- Text string (Unicode code points)
- Array (sequence of data items)
- Map (mapping from keys to values)
- Tag (tag number 0..2^64-1 and tag content)

Integers and floats are distinct. Serialization variants are not visible at the data model level.

### Extended Generic Data Models
Extension via registered simple values and tags (e.g., false, true, null, undefined, bignums, date/time).

### Specific Data Models
Subset of extended generic model with application semantics. Can define value equivalency for map keys.

## Section 3: Specification of the CBOR Encoding
- An encoder MUST produce only well-formed encoded data items.
- A decoder MUST NOT return decoded data when input is not a well-formed encoded CBOR data item.
- Initial byte: high-order 3 bits = major type, low-order 5 bits = additional information.
- Argument derivation:
  - <24: argument = additional information value.
  - 24,25,26,27: argument in following 1,2,4,8 bytes (network byte order). For major type 7 with 25-27, bytes are floating-point value.
  - 28,29,30: reserved; not well-formed.
  - 31: no argument; indefinite length (for types 2-5) or break stop code (type 7).
- The head consists of initial byte and any additional bytes for the argument.
- If input ends before end of a data item, not well-formed.
- If bytes remain after outermost item, not a single well-formed CBOR item (depending on application may treat as error or identify remaining bytes).

### Major Types (Table 1 summarized)
- Type 0: unsigned integer N (argument is value)
- Type 1: negative integer -1-N
- Type 2: byte string of N bytes
- Type 3: text string (UTF-8) of N bytes
- Type 4: array of N data items
- Type 5: map of N pairs (2N data items)
- Type 6: tag of number N, followed by 1 data item
- Type 7: simple/float/break

### 3.2 Indefinite Lengths
- Additional information 31 for types 2-5.
- Break stop code (0b111_11111) closes indefinite-length items. It is not a data item.
- If break appears where a data item is expected (except directly inside indefinite-length items), not well-formed.

#### 3.2.2 Indefinite-Length Arrays and Maps
- Represented by major type + 31, followed by items/key-value pairs, then break.
- If break appears after a key (in place of its value), map not well-formed.

#### 3.2.3 Indefinite-Length Byte/Text Strings
- Major type + 31, then zero or more definite-length strings of same type (chunks), then break.
- Represented as concatenation of chunks.
- If any chunk is not definite-length string of same major type, not well-formed.
- Nesting indefinite-length strings as chunks not allowed.
- If any definite-length text string inside indefinite-length text string is invalid, the whole is invalid. UTF-8 code point cannot be spread across chunks.

### 3.3 Floating-Point Numbers and Simple Values
- Major type 7 additional information values (Table 3):
  - 0-23: simple value 0-23
  - 24: simple value 32-255 in following byte
  - 25: IEEE 754 half-precision (16 bits)
  - 26: IEEE 754 single-precision (32 bits)
  - 27: IEEE 754 double-precision (64 bits)
  - 28-30: reserved, not well-formed
  - 31: break stop code

- Simple values assigned: false(20), true(21), null(22), undefined(23). (Table 4)
- An encoder MUST NOT issue two-byte sequences starting with 0xf8 followed by a byte <0x20. Such sequences are not well-formed. (Each simple value has only one representation variant.)

### 3.4 Tagging of Items
- Tag: major type 6, tag number from argument, followed by tag content (single data item).
- Tag definitions may specify preferred serialization.
- Decoders do not need to understand all tag numbers.
- Tags may nest.
- IANA registry for tag numbers.
- Protocols can extend data model with tags 0-5.
- Tag numbers 65535, 4294967295, 18446744073709551615 are reserved for implementation convenience; implementations MAY flag as error.

#### 3.4.1 Standard Date/Time String (tag 0)
- Content MUST be text string matching "date-time" production in [RFC3339] as refined by [RFC4287] Section 3.3. Other types or non-matching strings are invalid.

#### 3.4.2 Epoch-Based Date/Time (tag 1)
- Content MUST be unsigned/negative integer (major types 0,1) or floating-point (major type 7 with add. info 25,26,27). Other types are invalid.
- Nonnegative values: time on/after 1970-01-01T00:00Z UTC, interpreted per POSIX.
- Negative values: interpreted as determined by application.
- Fractional seconds via floating-point.
- Application may restrict content to integer or float only.

#### 3.4.3 Bignums (tags 2 and 3)
- Content MUST be byte string interpreted as unsigned integer n in network byte order. Other types are invalid.
- Tag 2: value = n. Tag 3: value = -1-n.
- Preferred serialization: no leading zeros. For n=0, empty byte string (but preferred integer encoding).
- Decoders MUST be able to decode bignums with leading zeros.
- Preferred serialization for integers representable via major types 0 or 1 is to use those types instead of bignum.

#### 3.4.4 Decimal Fractions and Bigfloats (tags 4 and 5)
- Content MUST be array of exactly two integers: exponent e and mantissa m.
- Tag 4: decimal fraction = m * 10^e. e MUST be integer (major type 0 or 1); m can be bignum.
- Tag 5: bigfloat = m * 2^e. Same constraints.
- Other structures are invalid.

#### 3.4.5 Content Hints

##### 3.4.5.1 Encoded CBOR Data Item (tag 24)
- Content MUST be byte string that encodes a well-formed CBOR data item. Other types are invalid. Validity checking of decoded CBOR not required for tag validity.

##### 3.4.5.2 Expected Later Encoding for CBOR-to-JSON Converters (tags 21-23)
- Tag 21: suggest base64url encoding without padding.
- Tag 22: suggest base64 encoding with padding.
- Tag 23: suggest base16 (hex) with uppercase.
- Padding bits must be zero.
- Tag may be applied to any data item; applies to all byte strings contained, except those nested with another expected conversion tag.

##### 3.4.5.3 Encoded Text (tags 32-34, 36)
- Tag 32 (URI): content MUST be text string matching URI-reference production [RFC3986]; else invalid.
- Tag 33 (base64url): content MUST be text string following base64url encoding [RFC4648] with no padding; invalid if (non-alphabet chars, only 1 alphabet char in last block, padding bits not 0, or padding characters present).
- Tag 34 (base64): similarly with padding; invalid if wrong number of padding or conditions.
- Tag 36 (MIME message): content MUST be valid MIME message [RFC2045]; invalid otherwise.

#### 3.4.6 Self-Described CBOR (tag 55799)
- Does not change semantics of tag content. Serialization: 0xd9d9f7.

## Section 4: Serialization Considerations

### 4.1 Preferred Serialization
- Use shortest form for argument. Use shortest floating-point encoding preserving value.
- Definite-length encoding preferred when length known at start of serialization.
- Preferred encoder is more universally interoperable.

### 4.2 Deterministically Encoded CBOR

#### 4.2.1 Core Deterministic Encoding Requirements
- Preferred serialization MUST be used: arguments as short as possible:
  - 0-23: in same byte; -1-24: same byte.
  - 24-255: only with additional uint8_t.
  - 256-65535: only with additional uint16_t.
  - 65536-4294967295: only with additional uint32_t.
- Floating-point values MUST use shortest form preserving value.
- Indefinite-length items MUST NOT appear.
- Keys in every map MUST be sorted in bytewise lexicographic order of their deterministic encodings.

#### 4.2.3 Length-First Map Key Ordering
- Alternative: keys sorted first by length (shorter first), then bytewise lexicographic.

## Section 5: Creating CBOR-Based Protocols
- Protocols MUST specify decoder handling of invalid/unexpected data.
- Protocols MAY specify that arbitrary valid data is unexpected.
- Encoders MUST produce only valid items.

### 5.1 CBOR in Streaming Applications
- Indefinite-length encoding may be used; decoder may present partial information.
- Application MUST have matching streaming security mechanism.

### 5.2 Generic Encoders and Decoders
- Generic decoder can decode all well-formed CBOR items.

### 5.3 Validity of Items
- Layers: well-formed (processable), valid (checked by generic decoder), expected (checked by application).
- First layer processing semantics of invalid item MUST either replace with error marker and continue, or stop processing.
- Protocol MUST specify which option.

#### 5.3.1 Basic Validity
- Duplicate keys in map: generic decoder decodes to map with only one instance.
- Invalid UTF-8 string: decoder may or may not verify.

#### 5.3.2 Tag Validity
- Inadmissible type/value for tag content: decoder expected to check.

### 5.6 Specifying Keys for Maps
- Protocol MUST define handling of multiple identical keys in a map.
- Protocol MUST NOT specify that changing key/value pair order changes semantics (except to disallow orders not meeting deterministic encoding requirements).

### 5.6.1 Equivalence of Keys
- At generic data model: integers and floats distinct; text vs byte strings distinct; tagged vs untagged distinct.
- Numeric values equal if numerically equal; -0.0 == 0.0.
- NaN equivalent if same significand after zero-extending to 64 bits.
- Byte and text strings compared bytewise; arrays elementwise; maps by set of pairs; tagged values by tag number and content.
- Simple values equal if same value.
- Nothing else equal.

### 5.7 Undefined Values
- May be used as substitute for encoding problem to allow rest of encoding.

## Section 6: Converting Data between CBOR and JSON (Non-normative)
- (Summarized: conversion guidance; implementers MAY follow.)

## Section 7: Future Evolution of CBOR
- Three extension points: simple values space, tag space, additional information space.
- Allocations for additional information values 28-30 only by updating this specification.

## Section 8: Diagnostic Notation (Non-normative summary)
A human-readable notation loosely based on JSON; described informally.

## Section 9: IANA Considerations
- CBOR Simple Values registry: ranges 0-19 by Standards Action, 32-255 by Specification Required.
- CBOR Tags registry: ranges 0-23 (Standards Action), 24-32767 (Specification Required), 32768-18446744073709551615 (First Come First Served).
- Media type: application/cbor. CoAP Content-Format: 60. Structured syntax suffix: +cbor.

## Section 10: Security Considerations (Key points)
- CBOR decoders must handle all hostile input as if untrusted.
- Interoperability issues between constrained and full decoders can be exploited.
- Resource exhaustion attacks: decoder must have appropriate resource management.
- Input validation may be linear but superlinear effort (e.g., hash-table collisions) must be avoided.
- Encoders should check inputs for overflows.
- Protocols must specify data model to avoid multiple interpretations.
- Conversion to JSON may cause security issues.

## Key Normative Requirements (Summary)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | An encoder MUST produce only well-formed encoded CBOR data items. | MUST | Section 3 |
| R2 | A decoder MUST NOT return a decoded data item when input is not well-formed. | MUST | Section 3 |
| R3 | An encoder MUST NOT issue two-byte sequences 0xf8 followed by byte <0x20 (not well-formed). | MUST | Section 3.3 |
| R4 | Simple value "false" must be encoded as 0xf4 only (not 0xf8 0x14). | MUST | Section 3.3 |
| R5 | Tag 0 content MUST be text string matching RFC 3339 "date-time" production. | MUST | Section 3.4.1 |
| R6 | Tag 1 content MUST be integer (types 0,1) or float (type 7 with add. info 25-27). | MUST | Section 3.4.2 |
| R7 | Tag 2/3 content MUST be byte string (bignum). | MUST | Section 3.4.3 |
| R8 | Tag 4/5 content MUST be array of exactly two integers. | MUST | Section 3.4.4 |
| R9 | Tag 24 content MUST be byte string encoding a well-formed CBOR item. | MUST | Section 3.4.5.1 |
| R10 | Tag 32 content MUST be text string matching URI-reference. | MUST | Section 3.4.5.3 |
| R11 | In core deterministic encoding, preferred serialization MUST be used. | MUST | Section 4.2.1 |
| R12 | In core deterministic encoding, indefinite-length items MUST NOT appear. | MUST | Section 4.2.1 |
| R13 | In core deterministic encoding, map keys MUST be sorted by bytewise lexicographic order of deterministic encodings. | MUST | Section 4.2.1 |
| R14 | CBOR-based protocols MUST specify how decoders handle invalid/unexpected data. | MUST | Section 5 |
| R15 | Encoders for CBOR-based protocols MUST produce only valid items. | MUST | Section 5 |
| R16 | In a streaming application, application MUST have matching streaming security mechanism. | MUST | Section 5.1 |
| R17 | CBOR-based protocol MUST define handling of duplicate keys in a map. | MUST | Section 5.6 |
| R18 | Protocol MUST NOT specify that changing key/value pair order changes semantics (except to disallow non-deterministic orders). | MUST | Section 5.6 |

## Informative Annexes (Condensed)
- **Appendix A**: Table of encoded CBOR examples (hex and diagnostic notation).
- **Appendix B**: Jump table for initial byte (summarized mapping).
- **Appendix C**: Pseudocode for well-formedness check; encoding signed integer.
- **Appendix D**: C and Python code for half-precision decoder.
- **Appendix E**: Comparison with ASN.1, MessagePack, BSON, RFC 713; conciseness examples.
- **Appendix F**: Well-formedness errors (three kinds) and examples.
- **Appendix G**: Changes from RFC 7049 (errata, new sections, deterministic encoding instead of canonical).