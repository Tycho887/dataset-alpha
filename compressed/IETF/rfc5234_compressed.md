# RFC 5234: Augmented BNF for Syntax Specifications: ABNF
**Source**: IETF | **Version**: STD 68 | **Date**: January 2008 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc5234

## Scope (Summary)
Defines the Augmented Backus-Naur Form (ABNF) meta-language for formal syntax specifications in Internet technical documents. Balances compactness and simplicity with reasonable representational power. Supersedes RFC 4234.

## Normative References
- [US-ASCII] ANSI X3.4, 1986 (7-bit ASCII).

## Definitions and Abbreviations
- **Rule**: A named sequence of elements defined by `name = elements crlf`.
- **Element**: A rule name, terminal value, group, option, or prose value.
- **Terminal value**: A non-negative integer representing a character, specified in binary (`b`), decimal (`d`), or hexadecimal (`x`).
- **CRLF**: Carriage return (`%d13`) followed by line feed (`%d10`).
- **ABNF strings**: Case-insensitive US-ASCII printable characters enclosed in DQUOTE.
- **Linear white space (LWSP)**: Not implicitly provided; must be explicit.

## Rule Definition
### 2.1 Rule Naming
- **Name**: Sequence of characters beginning with an alphabetic, followed by ALPHA, DIGIT, or hyphen (`-`).
- **Case Insensitivity**: `<rulename>`, `<Rulename>`, etc. refer to the same rule.
- **Angle brackets**: Not required in rules; may be used in prose to clarify.

### 2.2 Rule Form
- **Format**: `name = elements crlf`
- **Continuation lines**: Indented; left alignment of rule definitions relative to first rule line.

### 2.3 Terminal Values
- **Bases**: `b` (binary), `d` (decimal), `x` (hexadecimal).
- **Concatenated values**: Dot notation, e.g., `%d13.10`.
- **Literal text strings**: Enclosed in DQUOTE; case-insensitive. For case-sensitive match, specify decimal values individually (e.g., `%d97.98.99` for "abc").

### 2.4 External Encodings
- ABNF grammar may have multiple external encodings (e.g., 7-bit ASCII, binary octet, Unicode). Encoding details are outside ABNF scope; Appendix B provides common 7-bit ASCII encoding.

## Operators
### 3.1 Concatenation: Rule1 Rule2
- Ordered sequence of rule names; e.g., `mumble = foo bar foo` matches "aba".
- **Linear white space**: Not implicit; must be specified explicitly.

### 3.2 Alternatives: Rule1 / Rule2
- Forward slash separates alternatives.
- Quoted string with alphabetic characters is a special form representing case-insensitive combinatorial strings.

### 3.3 Incremental Alternatives: Rule1 =/ Rule2
- Adds alternatives to an existing rule; `oldrule =/ additional-alternatives` merges alternatives.

### 3.4 Value Range Alternatives: %c##-##
- Dash indicates range of numeric values, e.g., `DIGIT = %x30-39` equivalent to `"0"/"1"/.../"9"`.
- Dotted concatenation and dash range cannot be mixed in same string.

### 3.5 Sequence Group: (Rule1 Rule2)
- Parentheses group elements into a single ordered element; e.g., `elem (foo / bar) blat`.
- **Recommendation**: Use grouping to avoid ambiguity with bare alternatives.

### 3.6 Variable Repetition: *Rule
- Form: `<a>*<b>element` where `<a>` (minimum) default 0, `<b>` (maximum) default infinity.
- Examples: `*element` (any), `1*element` (at least 1), `3*3element` (exactly 3).

### 3.7 Specific Repetition: nRule
- Equivalent to `<n>*<n>element`; e.g., `2DIGIT` matches exactly 2 digits.

### 3.8 Optional Sequence: [RULE]
- Square brackets enclose optional element; equivalent to `*1(foo bar)`.

### 3.9 Comment: ; Comment
- Semicolon starts a comment to end of line.

### 3.10 Operator Precedence (highest to lowest)
1. Rule name, prose-val, Terminal value
2. Comment
3. Value range
4. Repetition
5. Grouping, Optional
6. Concatenation
7. Alternative
- **Recommendation**: Use grouping to make concatenation groups explicit.

## ABNF Definition of ABNF (Section 4)
*Normative grammar as defined in RFC 5234:*

```abnf
rulelist       =  1*( rule / (*c-wsp c-nl) )
rule           =  rulename defined-as elements c-nl
                      ; continues if next line starts with white space
rulename       =  ALPHA *(ALPHA / DIGIT / "-")
defined-as     =  *c-wsp ("=" / "=/") *c-wsp
elements       =  alternation *c-wsp
c-wsp          =  WSP / (c-nl WSP)
c-nl           =  comment / CRLF
comment        =  ";" *(WSP / VCHAR) CRLF
alternation    =  concatenation *(*c-wsp "/" *c-wsp concatenation)
concatenation  =  repetition *(1*c-wsp repetition)
repetition     =  [repeat] element
repeat         =  1*DIGIT / (*DIGIT "*" *DIGIT)
element        =  rulename / group / option / char-val / num-val / prose-val
group          =  "(" *c-wsp alternation *c-wsp ")"
option         =  "[" *c-wsp alternation *c-wsp "]"
char-val       =  DQUOTE *(%x20-21 / %x23-7E) DQUOTE
num-val        =  "%" (bin-val / dec-val / hex-val)
bin-val        =  "b" 1*BIT [ 1*("." 1*BIT) / ("-" 1*BIT) ]
dec-val        =  "d" 1*DIGIT [ 1*("." 1*DIGIT) / ("-" 1*DIGIT) ]
hex-val        =  "x" 1*HEXDIG [ 1*("." 1*HEXDIG) / ("-" 1*HEXDIG) ]
prose-val      =  "<" *(%x20-3D / %x3F-7E) ">"
```

## Security Considerations
Security is not relevant to this document.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Rule names are case insensitive. | normative | Section 2.1 |
| R2 | ABNF strings are case insensitive using US-ASCII | normative | Section 2.3 |
| R3 | Literal text strings must be enclosed in DQUOTE | normative | Section 2.3 |
| R4 | Linear white space must be explicitly specified | normative | Section 3.1 |
| R5 | Alternatives use `/` | normative | Section 3.2 |
| R6 | Incremental alternatives use `=/` | normative | Section 3.3 |
| R7 | Value ranges use dash `-` | normative | Section 3.4 |
| R8 | Grouping uses parentheses `()` | normative | Section 3.5 |
| R9 | Variable repetition uses `*` with optional bounds | normative | Section 3.6 |
| R10 | Specific repetition uses `<n>element` | normative | Section 3.7 |
| R11 | Optional sequence uses square brackets `[]` | normative | Section 3.8 |
| R12 | Comments start with `;` | normative | Section 3.9 |
| R13 | Operator precedence as specified in Section 3.10 | normative | Section 3.10 |
| R14 | Rule definitions follow the ABNF grammar in Section 4 | normative | Section 4 |
| R15 | External encoding details are outside ABNF scope | normative | Section 2.4 |

## Informative Annexes (Condensed)
- **Appendix A: Acknowledgements**: Originally from RFC 733; DRUMS working group contributions; Julian Reschke converted to XML source.
- **Appendix B: Core ABNF Rules** (commonly used basic rules for 7-bit ASCII encoding):

  *Core Rules (case-sensitive definitions):*
  - `ALPHA = %x41-5A / %x61-7A`   ; A-Z / a-z
  - `BIT = "0" / "1"`
  - `CHAR = %x01-7F`              ; any 7-bit US-ASCII excluding NUL
  - `CR = %x0D`
  - `CRLF = CR LF`
  - `CTL = %x00-1F / %x7F`
  - `DIGIT = %x30-39`
  - `DQUOTE = %x22`
  - `HEXDIG = DIGIT / "A" / "B" / "C" / "D" / "E" / "F"`
  - `HTAB = %x09`
  - `LF = %x0A`
  - `LWSP = *(WSP / CRLF WSP)`    ; caution: permits blank lines
  - `OCTET = %x00-FF`
  - `SP = %x20`
  - `VCHAR = %x21-7E`
  - `WSP = SP / HTAB`

  *Common Encoding*: 7-bit US-ASCII in 8-bit field, high bit zero, network byte order.