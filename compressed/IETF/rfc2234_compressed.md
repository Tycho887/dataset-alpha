# RFC 2234: Augmented BNF for Syntax Specifications: ABNF
**Source**: IETF (Standards Track) | **Version**: November 1997 | **Date**: November 1997 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc2234

## Scope (Summary)
This document defines Augmented BNF (ABNF), a modified version of Backus-Naur Form (BNF) used in many Internet technical specifications to define format syntax. It balances compactness and simplicity with reasonable representational power, and provides a formal meta-language separate from specific encodings. The core rule definitions in Appendix A are provided as a convenience for common lexical analysis.

## Normative References
- [US-ASCII] Coded Character Set--7-Bit American Standard Code for Information Interchange, ANSI X3.4-1986.
- [RFC733] Crocker, D., Vittal, J., Pogran, K., and D. Henderson, "Standard for the Format of ARPA Network Text Message", RFC 733, November 1977.
- [RFC822] Crocker, D., "Standard for the Format of ARPA Internet Text Messages", STD 11, RFC 822, August 1982.

## Definitions and Abbreviations
- **ABNF**: Augmented BNF, the notation defined in this document.
- **Concatenation**: Ordered string of values (Rule1 Rule2).
- **Alternative**: Elements separated by "/" (Rule1 / Rule2).
- **Incremental Alternative**: Adding alternatives to an existing rule using "=/" (Rule1 =/ Rule2).
- **Value Range Alternative**: Compact range of numeric values using "%c##-##".
- **Sequence Group**: Elements in parentheses "( )", treated as a single strictly ordered element.
- **Variable Repetition**: "*" operator: `<a>*<b>element`, defaults 0 and infinity.
- **Specific Repetition**: `<n>element` means exactly `<n>` occurrences.
- **Optional Sequence**: Square brackets "[ ]", equivalent to *1().
- **Comment**: ";" starts a comment to end of line.
- **Terminal Value**: Numeric characters with base indicator (b=bin, d=dec, x=hex). Literal text strings in DQUOTE.
- **Rule Name**: Sequence of characters starting with ALPHA, followed by ALPHA/DIGIT/"-". Case-insensitive.
- **CRLF**: Carriage return (%x0D) followed by linefeed (%x0A).
- **c-wsp**: White space (WSP) or comment plus newline.
- **prose-val**: Bracket-delimited prose description (%x3C ... %x3E).

## 1. Introduction (Condensed)
ABNF has evolved from earlier specifications (RFC733, RFC822) and is widely used in Internet standards. This document formalizes the notation, separating it from email-specific uses. It includes modifications and enhancements such as explicit handling of repetition, alternatives, and value ranges. The core lexical definitions in Appendix A are non-normative convenience.

## 2. Rule Definition
### 2.1 Rule Naming
- **Name**: sequence of ALPHA *(ALPHA / DIGIT / "-"). Case-insensitive.
- Angle brackets ("<", ">") are not required but may be used for clarity in prose.

### 2.2 Rule Form
- Rule: `name = elements crlf`
- **elements**: one or more rule names or terminal specifications combined with operators.
- **Continuation lines**: indented relative to the first line.

### 2.3 Terminal Values
- Terminals are non-negative integers, with base indicator: `b` (binary), `d` (decimal), `x` (hexadecimal).
- Examples: `CR = %d13`, `CRLF = %d13.10`.
- Literal text strings in DQUOTE are case-insensitive us-ascii. To match case-sensitive strings, use numeric values individually.
- **Concatenation within terminal**: period "." separates characters in a value string.

### 2.4 External Encodings
- ABNF grammars may have multiple external encodings (e.g., 7-bit ASCII, binary octet, 16-bit Unicode). Encoding details are outside the scope of ABNF.

## 3. Operators
### 3.1 Concatenation (Rule1 Rule2)
- Simple ordered string of values. No implicit linear white space; LWSP must be defined explicitly if allowed.

### 3.2 Alternatives (Rule1 / Rule2)
- Matches either alternative. Quoted strings are special: they represent case-insensitive combinatorial strings.

### 3.3 Incremental Alternatives (Rule1 =/ Rule2)
- Adds alternatives to an existing rule definition. Equivalent to defining all alternatives at once.

### 3.4 Value Range Alternatives (%c##-##)
- Compact representation of a range of numeric values. Example: `DIGIT = %x30-39`.
- Cannot combine concatenated numeric values and value ranges in the same string.

### 3.5 Sequence Group ((Rule1 Rule2))
- Parentheses group elements into a strictly ordered single element. Recommended to avoid ambiguity in alternatives.

### 3.6 Variable Repetition (*Rule)
- Full form: `<a>*<b>element`. Defaults: a=0, b=infinity. Examples: `*element` (any number), `1*element` (at least one), `3*3element` (exactly three).

### 3.7 Specific Repetition (nRule)
- `<n>element` is equivalent to `<n>*<n>element`. Example: `2DIGIT` matches exactly two digits.

### 3.8 Optional Sequence ([RULE])
- Square brackets are equivalent to `*1(foo bar)`.

### 3.9 ; Comment
- Semi-colon starts a comment to end of line.

### 3.10 Operator Precedence (highest to lowest)
1. Strings, Names formation
2. Comment
3. Value range
4. Repetition
5. Grouping, Optional
6. Concatenation
7. Alternative

Use of grouping is recommended to make concatenation groups explicit.

## 4. ABNF Definition of ABNF (Normative Grammar)

The following syntax uses the rules from Appendix A (Core).

```abnf
rulelist       =  1*( rule / (*c-wsp c-nl) )
rule           =  rulename defined-as elements c-nl
                     ; continues if next line starts
                     ;  with white space
rulename       =  ALPHA *(ALPHA / DIGIT / "-")
defined-as     =  *c-wsp ("=" / "=/") *c-wsp
                     ; basic rules definition and
                     ;  incremental alternatives
elements       =  alternation *c-wsp
c-wsp          =  WSP / (c-nl WSP)
c-nl           =  comment / CRLF
                     ; comment or newline
comment        =  ";" *(WSP / VCHAR) CRLF
alternation    =  concatenation
                  *(*c-wsp "/" *c-wsp concatenation)
concatenation  =  repetition *(1*c-wsp repetition)
repetition     =  [repeat] element
repeat         =  1*DIGIT / (*DIGIT "*" *DIGIT)
element        =  rulename / group / option /
                  char-val / num-val / prose-val
group          =  "(" *c-wsp alternation *c-wsp ")"
option         =  "[" *c-wsp alternation *c-wsp "]"
char-val       =  DQUOTE *(%x20-21 / %x23-7E) DQUOTE
                     ; quoted string of SP and VCHAR
                        without DQUOTE
num-val        =  "%" (bin-val / dec-val / hex-val)
bin-val        =  "b" 1*BIT
                  [ 1*("." 1*BIT) / ("-" 1*BIT) ]
                     ; series of concatenated bit values
                     ; or single ONEOF range
dec-val        =  "d" 1*DIGIT
                  [ 1*("." 1*DIGIT) / ("-" 1*DIGIT) ]
hex-val        =  "x" 1*HEXDIG
                  [ 1*("." 1*HEXDIG) / ("-" 1*HEXDIG) ]
prose-val      =  "<" *(%x20-3D / %x3F-7E) ">"
                     ; bracketed string of SP and VCHAR
                        without angles
                     ; prose description, to be used as
                        last resort
```

## 5. Security Considerations
Security is irrelevant to this document.

## 6. Appendix A - Core (Non-normative Convenience)
This appendix provides a convenient set of core rule definitions for use in specific grammars. The encoding is network virtual ASCII (7-bit US-ASCII in 8-bit field, high bit zero).

### 6.1 Core Rules
| Rule    | Definition                | Description                                      |
|---------|---------------------------|--------------------------------------------------|
| ALPHA   | %x41-5A / %x61-7A        | A-Z / a-z                                        |
| BIT     | "0" / "1"                | Binary digit                                     |
| CHAR    | %x01-7F                  | Any 7-bit US-ASCII character except NUL           |
| CR      | %x0D                     | Carriage return                                  |
| CRLF    | CR LF                    | Internet standard newline                         |
| CTL     | %x00-1F / %x7F          | Control characters                                |
| DIGIT   | %x30-39                  | 0-9                                              |
| DQUOTE  | %x22                     | Double quote                                     |
| HEXDIG  | DIGIT / "A" / "B" / "C" / "D" / "E" / "F" | Hexadecimal digit |
| HTAB    | %x09                     | Horizontal tab                                   |
| LF      | %x0A                     | Linefeed                                         |
| LWSP    | *(WSP / CRLF WSP)        | Linear white space (past newline)                 |
| OCTET   | %x00-FF                  | 8 bits of data                                   |
| SP      | %x20                     | Space                                            |
| VCHAR   | %x21-7E                  | Visible (printing) characters                     |
| WSP     | SP / HTAB                | White space                                      |

### 6.2 Common Encoding
Externally, data are represented as 7-bit US-ASCII in an 8-bit field with high bit zero. Values are in network byte order (higher-valued bytes on left, sent first).

## Informative Annexes (Condensed)
- **Acknowledgments**: Syntax originally from RFC 733; enhancements by DRUMS working group members including J. Abela, H. Alvestrand, R. Elz, R. Fajman, A. Garrett, T. Harsch, D. Kohn, B. McQuillan, K. Moore, C. Newman, P. Resnick, H. Schulzrinne.
- **Full Copyright Statement**: Copyright (C) The Internet Society (1997). Document may be copied and distributed, derivative works allowed with copyright notice; provided "AS IS" without warranty.