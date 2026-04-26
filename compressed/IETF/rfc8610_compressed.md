# RFC 8610: Concise Data Definition Language (CDDL): A Notational Convention to Express Concise Binary Object Representation (CBOR) and JSON Data Structures
**Source**: IETF | **Version**: Standards Track | **Date**: June 2019 | **Type**: Normative  
**Original**: [https://www.rfc-editor.org/info/rfc8610](https://www.rfc-editor.org/info/rfc8610)

## Scope (Summary)
Defines a notational convention (CDDL) for expressing CBOR and JSON data structures, providing unambiguous descriptions, flexibility, and machine-processability for protocol messages and data formats.

## Normative References
- ISO 6093:1985
- RFC 2119 (BCP 14)
- RFC 3552 (BCP 72)
- RFC 3629 (STD 63)
- RFC 4648
- RFC 5234 (STD 68)
- RFC 7049
- RFC 7493
- RFC 8126 (BCP 26)
- RFC 8174 (BCP 14)
- RFC 8259 (STD 90)
- W3C.REC-xmlschema-2-20041028

## Definitions and Abbreviations
- **CDDL**: Concise Data Definition Language
- **CBOR**: Concise Binary Object Representation (RFC 7049)
- **JSON**: JavaScript Object Notation (RFC 8259)
- **PEG**: Parsing Expression Grammar
- **ABNF**: Augmented Backus-Naur Form (RFC 5234)
- **Group**: A sequence of name/value pairs used for composition in CDDL.
- **Type**: A set of CBOR data items; the entire specification defines a type.
- **Occurrence**: Indicator (?, *, +, n*m) controlling repetition of a group entry.
- **Control**: Operator (e.g., .size, .bits) relating target type to controller type.
- **Socket/Plug**: Extension points marked with $ (type) or $$ (group), starting as empty choices.
- **Cut**: Symbol "^" used in maps to lock in a key match, preventing later matches.
- **Unwrap**: Operator "~" to strip one layer of a type (map/array/tag) to expose underlying group/type.

## 1. Introduction
- Main goal: Provide unified notation for protocols using CBOR.
- Goals: (G1) Unambiguous structure, (G2) Flexible representation, (G3) Express common CBOR types/structures, (G4) Human-readable and machine-processable, (G5) Enable automated compliance checking, (G6) Enable extraction of specific elements.
- Also applicable to JSON due to subset relationship of data models.
- Document structure: Section 3 defines syntax; Appendix H has examples; Section 4 discusses usage; Appendix B provides ABNF; Appendix D lists standard prelude.

### 1.1 Requirements Notation
- **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, **OPTIONAL** as per BCP 14 (RFC 2119, RFC 8174) when in all capitals.

### 1.2 Terminology
- New terms in *cursive*; CDDL text in "typewriter".
- "byte" = synonym for "octet".

## 2. The Style of Data Structure Specification
- Focuses on data model used in JSON/CBOR community.
- Composition styles: **vector** (array of same-semantics elements), **record** (array with positionally defined semantics), **table** (map with open key domain), **struct** (map with specification-defined keys).
- Two foundational concepts:
  1. **Group**: Only kind of composition; can be used in arrays or maps.
  2. **Type**: Defined by first rule; set of acceptable CBOR data items.

### 2.1 Groups and Composition in CDDL
- Groups are lists of entries (name/value pairs) or group expressions.
- Array context: only values; order matters.
- Map context: names become keys; order irrelevant.
- Matching: Array matches if group matches elements in order; Map matches if all name/value pairs present and no extra pairs.
- Example: `person = { age: int, name: tstr, employer: tstr }`
- Groups can be named and reused: `identity = ( age: int, name: tstr )`

#### 2.1.1 Usage
- Style choice: define groups inline or as separate named rules for reuse.

#### 2.1.2 Syntax
- Group delimited by parentheses "(" and ")".
- Entry: *keytype => valuetype*; comma optional.
- Double arrow "=>" for general key types; colon ":" shortcut for text string or integer literal keys (also implies cut semantics).

### 2.2 Types

#### 2.2.1 Values
- Values (numbers, strings) can be used as types.
- Number notation: integer (no fraction/exponent) vs. floating-point (fraction/exponent present).

#### 2.2.2 Choices
- Type choice: `type1 / type2` (PEG prioritized choice).
- Group choice: `group1 // group2` (weaker binding).
- Augmentation operators: `/=` for type, `//=` for group.
- Ranges: inclusive `..`, exclusive `...` (only between integers or floats).
- Enumeration from group: `&groupname` or `&(group)`.

#### 2.2.3 Representation Types
- Use `#` followed by major type (0-7) and optional additional info.
- E.g., `#6.55799(breakfast)` for a tag.
- Notation defines value sets at data model level, not serialization constraints.

#### 2.2.4 Root Type
- First rule in file is the root type (must be a type, not a group).

## 3. Syntax

### 3.1 General Conventions
- Rule: `name = definition` (type or group).
- Name characters: A-Z, a-z, 0-9, _, -, @, ., $; case-sensitive; start with alphabetic or @, _, $.
- Comments: `;` to end of line.
- Whitespace separates tokens; optional except within strings.
- Hex numbers: `0x`; binary: `0b`.
- Text strings: double quotes, JSON string conventions.
- Byte strings: single quotes; optional prefix `h` (hex) or `b64` (base64/url).
- CDDL uses UTF-8; no Unicode normalization.

### 3.2 Occurrence
- Indicators: `?` (0 or 1), `*` (0 or more), `+` (1 or more), `n*m` (n to m).
- Default: exactly once (1*1).
- Occurrence modifies group entry, creating sequence of matches.

### 3.3 Predefined Names for Types
- `bool`, `uint`, `nint`, `int`, `float16`, `float32`, `float64`, `float`, `bstr`/`bytes`, `tstr`/`text`.
- Also tagged types: `tdate`, `time`, `bigint`, `regexp`, etc. (see Appendix D).

### 3.4 Arrays
- `[ group ]`
- Example: `unlimited-people = [* person]`

### 3.5 Maps
- `{ group }`
- Structs: keys are identifiers (barewords) or quoted strings, using colon (with cut).
- Tables: `type => type` for open key/value domains.
- Non-deterministic order: Avoid ambiguous specifications where general rule matches subset of keys.
- Cuts: `^` after key type in entry to lock in match; colon shortcut includes cut.

### 3.6 Tags
- `#6.nnn(type)` for tagged data items.
- Example: `biguint = #6.2(bstr)`

### 3.7 Unwrapping
- `~typename` exposes the group inside a map/array or the type inside a tag.
- Example: `advanced-header = [ ~basic-header, field3: bytes ]`

### 3.8 Controls
- Syntax: `target .control-operator controller`
- Defined operators: `.size`, `.bits`, `.regexp`, `.cbor`, `.cborseq`, `.within`, `.and`, `.lt`, `.le`, `.gt`, `.ge`, `.eq`, `.ne`, `.default`.

#### 3.8.1 .size
- Controls byte length for bstr/tstr; for uint, limits range to 0..256^N.

#### 3.8.2 .bits
- On bstr/uint: only bits numbered in controller type may be set.

#### 3.8.3 .regexp
- tstr must match XSD regular expression (W3C REC).

#### 3.8.4 .cbor and .cborseq
- bstr contains CBOR-encoded data item(s) matching given type.

#### 3.8.5 .within and .and
- Type intersection; `.within` expresses subset intent.

#### 3.8.6 .lt, .le, .gt, .ge, .eq, .ne, .default
- Numeric comparisons; .eq/.ne also for other types (text, bytes, arrays, maps, tagged, simple). .default adds intent for default value (used with optional).

### 3.9 Socket/Plug
- Extension points: `$name` (type socket), `$$name` (group socket).
- Empty by default; extended with `/=` and `//=`.
- Not an error if undefined (empty choice).

### 3.10 Generics
- `name<param1, param2> = ...`; use `name<arg1, arg2>`.
- Formal parameters bound to actual arguments.

### 3.11 Operator Precedence
- Table 1 (see Appendix B for full precedence; lowest to highest):
  - =, /=, //= (assignment)
  - // (group choice)
  - , (sequence)
  - *, n*m, +, ? (occurrence)
  - =>, : (key/value)
  - / (type choice)
  - .., ... (range)
  - .ctrl (control)
  - &, ~ (enumeration, unwrap)

## 4. Making Use of CDDL
- Guide for human implementers, automated checking of CBOR/JSON data, data analysis tools.
- No requirement to enforce all details; left to application.
- Not intended for code generation.

## 5. Security Considerations
- Language itself brings no security issues; protocol specifications must follow RFC 3552.
- Potential confusion in language might create security issues.
- Security should not depend on correctness of CDDL specification or implementation without further defenses.
- Extensions require careful security analysis.
- Clarity and simplicity valued over elegance.
- Complexity does not become lesser just because CDDL handles it.

## 6. IANA Considerations
- Registry created: CDDL Control Operators (within "Concise Data Definition Language (CDDL)").
- Initial entries: .size, .bits, .regexp, .cbor, .cborseq, .within, .and, .lt, .le, .gt, .ge, .eq, .ne, .default.
- Policy: Specification Required (Expert Review) for names without internal dot; IETF Review for names with internal dot.
- Expert reviewer instructed to facilitate SDO-specific control operators.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The key words "MUST", "MUST NOT", etc. in this document are to be interpreted as described in BCP 14 when in all capitals. | shall | Section 1.1 |
| R2 | The first rule in a CDDL file defines the root type. | shall | Section 2.2.4 |
| R3 | Occurrence indicator defaults to exactly once (1*1). | shall | Section 3.2 |
| R4 | CDDL uses UTF-8 for encoding; no Unicode normalization. | shall | Section 3.1 |
| R5 | Comments start with ";" and finish at end of line. | shall | Section 3.1 |
| R6 | The colon ":" shortcut in map keys implies cut semantics (^). | shall | Section 3.5.4 |
| R7 | Control operators are extension points; new operators may be registered. | shall | Section 3.8, 6.1 |
| R8 | Sockets ($name, $$name) start as empty choices; must be extended via /= and //= respectively. | shall | Section 3.9 |
| R9 | CDDL does not provide syntactic predicate operators ! or & from PEG. | shall | Appendix A |
| R10 | The standard prelude (Appendix D) is automatically prepended to every CDDL file. | shall | Appendix D |
| R11 | JSON compatibility requires limiting to JSON data model (no byte strings, tags, simple values other than false/true/null). | shall | Appendix E |
| R12 | Extended Diagnostic Notation (EDN) allows whitespace in prefixed byte strings, text in byte strings, embedded CBOR, concatenated strings, hex/octal/binary numbers, and comments. | shall | Appendix G |

## Normative Appendices (Condensed)
- **Appendix A (PEGs)**: CDDL's group matching is based on PEG semantics (prioritized choice, greedy repetition). The ABNF grammar in Appendix B can be interpreted as PEG.
- **Appendix B (ABNF Grammar)**: Formal ABNF for CDDL syntax; defines rules for types, groups, values, and syntactic elements.
- **Appendix C (Matching Rules)**: Semantics of each syntactic construction: types match data items; groups match sequences of name/value pairs. First rule defines root. Choice operators use PEG order. Occurrence indicators repeat group matching. Key/value matching with cuts in maps.
- **Appendix D (Standard Prelude)**: Fixed prelude defining `any`, `uint`, `nint`, `int`, `bstr`, `tstr`, `float*`, tagged types (`tdate`, `time`, etc.), and simple values (`false`, `true`, `nil`, `undefined`). Note: `string` not defined – use `tstr` or `bstr`.
- **Appendix E (Use with JSON)**: JSON data model subset of CBOR; use limited prelude (no byte strings, tags, extra simple values). JSON numbers are all floating-point; distinguish integer vs. float by value. I-JSON range restrictions given as optional types.
- **Appendix G (Extended Diagnostic Notation)**: Normative extensions: whitespace in hex byte strings, UTF-8 text in single-quoted byte strings, embedded CBOR with << >>, concatenated strings, hex/octal/binary numbers, comments delimited by slashes.

## Informative Annexes (Condensed)
- **Appendix F (CDDL Tool)**: Reference Ruby gem `cddl` for syntax checking, instance generation, validation. Install via `gem install cddl`.
- **Appendix H (Examples)**: Example from RFC 7071 (reputon) in CDDL; demonstrates compact vs. verbose styles; instance output shown.