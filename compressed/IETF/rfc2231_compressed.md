# RFC 2231: MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: November 1997 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc2231/

## Scope (Summary)
This memo defines extensions to RFC 2045 media type and RFC 2183 disposition parameter values to allow: (1) parameter values in character sets other than US-ASCII, (2) language specification for display, and (3) a continuation mechanism for long parameter values. It also extends RFC 2047 encoded words to include language information.

## Normative References
- RFC 822 – Standard for ARPA Internet Text Messages
- RFC 1766 – Tags for the Identification of Languages
- RFC 2045 – MIME Part One: Format of Internet Message Bodies
- RFC 2046 – MIME Part Two: Media Types
- RFC 2047 – MIME Part Three: Representation of Non-ASCII Text in Headers
- RFC 2048 – MIME Part Four: MIME Registration Procedures
- RFC 2049 – MIME Part Five: Conformance Criteria
- RFC 2060 – Internet Message Access Protocol – Version 4rev1
- RFC 2119 – Key words for use in RFCs to Indicate Requirement Levels
- RFC 2130 – Report from the IAB Character Set Workshop
- RFC 2183 – Communicating Presentation Information: The Content-Disposition Header

## Definitions and Abbreviations
- **MIME**: Multipurpose Internet Mail Extensions
- **IMAP4**: Internet Message Access Protocol version 4
- **LWSP**: Linear White Space
- **ABNF**: Augmented Backus-Naur Form (as used in RFC 2045)
- **tspecials**: Special characters used in MIME tokens (defined in RFC 2045)
- **attribute-char**: Any US-ASCII CHAR except SPACE, CTLs, "*", "'", "%", or tspecials
- **ext-octet**: Percent-encoded octet: `%` followed by 2 hex digits (0-9, A-F)
- **charset**: Registered character set name
- **language**: Registered language tag per RFC 1766

## 1. Abstract (Informative)
The abstract is summarized in Scope. This memo addresses three limitations: header line wrapping with long values, non-ASCII parameter values, and language display information.

## 2. Introduction (Informative)
MIME’s success created needs for additional mechanisms. Existing MIME mechanisms provide named parameters for content-type and content-disposition. Three inherent limitations:
1. Long parameter values are problematic due to header folding rules.
2. Parameter values cannot use RFC 2047 encoded words; limited to US-ASCII.
3. Language information is needed for proper display (e.g., text-to-speech for handicapped users). The last also applies to encoded words.

This document defines extensions that are syntactically compatible with existing MIME and designed for minimal impact.

**IMPORTANT NOTE**: These mechanisms should not be used lightly; reserved for situations where a real need exists.

### 2.1. Requirements Notation
When capitalized, the key words **MUST**, **SHOULD**, **MUST NOT**, **SHOULD NOT**, and **MAY** are used to indicate requirement levels as per RFC 2119.

## 3. Parameter Value Continuations
- A mechanism is needed to break up long parameter values for header line wrapping.
- **Requirements**:
  - **MUST NOT** change the syntax of MIME media type and disposition lines.
  - **MUST NOT** depend on parameter ordering (MIME states parameters are not order sensitive; user agent processing may reorder).
- **Solution**: Use the asterisk (`*`) followed by a decimal count to indicate multiple parameters encapsulating a single value. Count starts at 0 and increments by 1. Decimal values only; leading zeroes or gaps in sequence are **not allowed**.
- The original value is recovered by concatenating sections in order.
- Quotes around parameter values are part of value syntax, **not** the value itself.
- A mixture of quoted and unquoted continuation fields is explicitly permitted.

## 4. Parameter Value Character Set and Language Information
- Asterisks (`*`) at the end of a parameter name indicate that character set and language information may appear at the beginning of the parameter value.
- Encoding: Percent signs (`%`) flag octets encoded in hexadecimal (similar to RFC 2047).
- Single quote (`'`) delimits character set, language, and actual value. Example:
  `title*=us-ascii'en-us'This%20is%20%2A%2A%2Afun%2A%2A%2A`
- It is permissible to leave either character set or language field blank, but delimiters **MUST** be present.
- Parameter field definitions **MUST NOT** assign a default character set or language.

### 4.1. Combining Character Set, Language, and Parameter Continuations
- Language and character set information only appear at the beginning of a given parameter value.
- Continuations do not allow using more than one character set or language in the same value.
- A value may contain a mixture of encoded and unencoded segments.
- The first segment of a continuation **MUST** be encoded if language and character set are given.
- If the first segment is encoded, the language and character set field delimiters **MUST** be present even when fields are blank.

## 5. Language Specification in Encoded Words
- RFC 2047 encoded word construct is extended: suffix the charset with `*language`. Example:
  `From: =?US-ASCII*EN?Q?Keith_Moore?= <moore@cs.utk.edu>`

## 6. IMAP4 Handling of Parameter Values
- IMAP4 servers **SHOULD** decode parameter value continuations when generating BODY and BODYSTRUCTURE fetch attributes.

## 7. Modifications to MIME ABNF
The ABNF for parameter values in RFC 2045 is replaced by the following (exact syntax):

```
parameter := regular-parameter / extended-parameter
regular-parameter := regular-parameter-name "=" value
regular-parameter-name := attribute [section]
attribute := 1*attribute-char
attribute-char := <any (US-ASCII) CHAR except SPACE, CTLs, "*", "'", "%", or tspecials>
section := initial-section / other-sections
initial-section := "*0"
other-sections := "*" ("1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9") *DIGIT)
extended-parameter := (extended-initial-name "=" extended-value) /
                       (extended-other-names "=" extended-other-values)
extended-initial-name := attribute [initial-section] "*"
extended-other-names := attribute other-sections "*"
extended-initial-value := [charset] "'" [language] "'" extended-other-values
extended-other-values := *(ext-octet / attribute-char)
ext-octet := "%" 2(DIGIT / "A" / "B" / "C" / "D" / "E" / "F")
charset := <registered character set name>
language := <registered language tag [RFC-1766]>
```

ABNF for encoded words in RFC 2047 is changed from:
`encoded-word := "=?" charset "?" encoding "?" encoded-text "?="`
to:
`encoded-word := "=?" charset ["*" language] "?" encoded-text "?="`

## 8. Character Sets Allowing Language Specification (Informative)
If future character sets provide inline language labeling facilities, they **SHOULD** be used in preference to the mechanisms defined here. The mechanisms in this spec allow omission of language labels to accommodate such future usage.

## 9. Security Considerations
This RFC does not discuss security issues and is not believed to raise any security issues not already endemic in electronic mail and present in fully conforming MIME implementations.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Parameter value continuation mechanism **MUST NOT** change MIME media type/disposition line syntax. | MUST | Section 3 |
| R2 | Continuation mechanism **MUST NOT** depend on parameter ordering. | MUST | Section 3 |
| R3 | Continuation count starts at 0, increments by 1; leading zeroes and gaps **not allowed**. | MUST | Section 3 |
| R4 | Parameter field definitions **MUST NOT** assign a default character set or language. | MUST | Section 4 |
| R5 | When character set or language field is blank, single quote delimiters **MUST** be present. | MUST | Section 4 |
| R6 | First segment of a continued parameter **MUST** be encoded if language and character set are given. | MUST | Section 4.1 |
| R7 | If first segment is encoded, language and charset delimiters **MUST** be present even when blank. | MUST | Section 4.1 |
| R8 | IMAP4 servers **SHOULD** decode parameter value continuations when generating BODY/BODYSTRUCTURE. | SHOULD | Section 6 |
| R9 | Future inline language labeling facilities **SHOULD** be used in preference to this specification’s mechanisms. | SHOULD | Section 8 |

## Informative Annexes (Condensed)
- **Annex A (Section 2)**: Motivation – MIME’s limitations for long, non-ASCII, and language-tagged parameter values.
- **Annex B (Section 2.1)**: Requirements notation per RFC 2119.
- **Annex C (Section 8)**: Future character sets with inline language labels should be preferred.
- **Annex D (Section 9)**: No new security issues beyond standard MIME.