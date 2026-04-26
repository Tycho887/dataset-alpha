# RFC 5987: Character Set and Language Encoding for Hypertext Transfer Protocol (HTTP) Header Field Parameters
**Source**: IETF | **Version**: Standards Track | **Date**: August 2010 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc5987

## Scope (Summary)
Defines an encoding for HTTP header field parameters to carry characters outside the ISO-8859-1 character set, compatible with a profile of RFC 2231. Does not apply to HTTP payloads (e.g., multipart/form-data).

## Normative References
- [ISO-8859-1] International Organization for Standardization, "Information technology -- 8-bit single-byte coded graphic character sets -- Part 1: Latin alphabet No. 1", ISO/IEC 8859-1:1998, 1998.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC2978] Freed, N. and J. Postel, "IANA Charset Registration Procedures", BCP 19, RFC 2978, October 2000.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 3629, STD 63, November 2003.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", RFC 3986, STD 66, January 2005.
- [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5646] Phillips, A., Ed. and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- [USASCII] American National Standards Institute, "Coded Character Set -- 7-bit American Standard Code for Information Interchange", ANSI X3.4, 1986.

## Definitions and Abbreviations
- **parameter**: `attribute LWSP "=" LWSP value` (as defined in [RFC2616] Section 3.6, modified by this specification)
- **reg-parameter**: `parmname LWSP "=" LWSP value` (regular parameter, must not end with "*")
- **ext-parameter**: `parmname "*" LWSP "=" LWSP ext-value` (extended parameter, identifier ends with asterisk)
- **parmname**: `1*attr-char`
- **ext-value**: `charset "'" [ language ] "'" value-chars` — value part consisting of REQUIRED charset, OPTIONAL language, and percent-encoded value
- **charset**: `"UTF-8" / "ISO-8859-1" / mime-charset` (producers MUST use UTF-8 or ISO-8859-1)
- **mime-charset**: as defined in [RFC2978] Section 2.3, but excluding the single quote character; SHOULD be registered in IANA registry
- **language**: `<Language-Tag>` as defined in [RFC5646] Section 2.1
- **value-chars**: `*( pct-encoded / attr-char )`
- **pct-encoded**: `"%" HEXDIG HEXDIG`
- **attr-char**: `ALPHA / DIGIT / "!" / "#" / "$" / "&" / "+" / "-" / "." / "^" / "_" / "`" / "|" / "~"` (token except "*", "'", "%")
- **parameter continuations**: not part of this specification (Section 3.1)
- **encoded words (RFC 2047)**: not extended by this specification (Section 3.3)

## Introduction
By default, HTTP header parameters cannot carry characters outside ISO-8859-1. This encoding is based on RFC 2231 but omits parameter continuations and encoded word language extensions. It is purely informative with respect to RFC 2231 (see Section 1 notes).

## Notational Conventions
- **Key words** (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) are interpreted as described in [RFC2119].
- ABNF notation per [RFC5234]; core rules ALPHA, DIGIT, HEXDIG, LWSP included by reference.
- Term "character set" used for consistency with IETF specs (e.g., [RFC2277]); a more accurate term would be "character encoding".

## 3. Comparison to RFC 2231 and Definition of the Encoding
### 3.1. Parameter Continuations
RFC 2231 continuations address MIME length limitations; HTTP does not have such limitations ([RFC2616] Section 19.4.7). **Thus, parameter continuations are not part of this encoding.**

### 3.2. Parameter Value Character Set and Language Information
#### 3.2.1. Definition
- **Grammar modification**:
  - `parameter = reg-parameter / ext-parameter`
  - `ext-parameter = parmname "*" LWSP "=" LWSP ext-value`
  - `ext-value = charset "'" [ language ] "'" value-chars`
- **Mandatory character sets**: Recipients implementing this specification **MUST** support "ISO-8859-1" and "UTF-8".
- **Producers** **MUST** use either "UTF-8" or "ISO-8859-1". Extension character sets (mime-charset) are reserved for future use.
- **Encoding of value-chars**: Characters not in `attr-char` are encoded into an octet sequence using the specified charset, then percent-encoded per [RFC3986] Section 2.1.
- **Language** is optional; charset is REQUIRED.
- **Error handling**: Recipients should handle malformed percent-escapes or non-decodable octets robustly (e.g., ignore parameter, strip, or substitute with replacement character U+FFFD). No mandated behavior.
- **Note**: The ABNF for `mime-charset` differs from [RFC2978] by excluding single quote (per Errata ID 1912). No registered charset names use that character.

#### 3.2.2. Examples
- Non-extended token: `foo: bar; title=Economy`
- Non-extended quoted-string: `foo: bar; title="US-$ rates"`
- Extended ISO-8859-1: `foo: bar; title*=iso-8859-1'en'%A3%20rates` (POUND SIGN U+00A3)
- Extended UTF-8: `foo: bar; title*=UTF-8''%c2%a3%20and%20%e2%82%ac%20rates` (POUND SIGN and EURO SIGN, language omitted)
- Note: HEXDIG allows both cases; language information optional, charset not.

### 3.3. Language Specification in Encoded Words
RFC 2231 Section 5 extends RFC 2047 for language in encoded words. HTTP/1.1 does reference RFC 2047 but it is unclear which headers apply and whether implemented. **Thus, this feature is not included.**

## 4. Guidelines for Usage in HTTP Header Field Definitions
Specifications using the extensions ought to clearly state that by normatively referencing this RFC and including the `ext-value` production in ABNF. Example:
```
foo-header  = "foo" LWSP ":" LWSP token ";" LWSP title-param
title-param = "title" LWSP "=" LWSP value
            / "title*" LWSP "=" LWSP ext-value
ext-value   = <see RFC 5987, Section 3.2>
```
- **Note**: Parameter Value Continuation (RFC 2231 Section 3) prohibits multiple extended parameters with same `parmname`; thus specifications should disallow this for compatibility.

### 4.1. When to Use the Extension
- Per [RFC2277] Section 4.2, protocol elements with human-readable text must carry language information. Therefore, `ext-value` **ought to be always used** when the parameter value is textual and its language is known.
- Also use when parameter value needs characters outside US-ASCII; it would be unacceptable to restrict to a Unicode subset.

### 4.2. Error Handling
- Header specs should define whether multiple instances of same `parmname` are allowed. This specification suggests that an extended parameter takes precedence over a regular one. Example:
  ```
  foo: bar; title="EURO exchange rates";
            title*=utf-8''%e2%82%ac%20exchange%20rates
  ```
  - Producers can provide both ASCII and internationalized versions. Recipients understanding this specification **ought to prefer the extended syntax**.
- **Note**: Many implementations at time of writing failed to ignore unknown forms or prioritize ASCII form.

## 5. Security Considerations
- Non-ASCII transport enables character spoofing (displayed value may appear different).
- UTF-8 decoding attack scenarios exist (see [RFC3629] Section 10).
- Multiple language variants for a single parameter may enable spoofing if they are not equivalent; impact depends on the parameter.

## 6. Acknowledgements
Thanks to Martin Duerst, Frank Ellermann, Graham Klyne, Alexey Melnikov, Chris Newman, Benjamin Carlyle, and Roar Lauritzsen.

## 7. References
- Normative: [ISO-8859-1], [RFC2119], [RFC2616], [RFC2978], [RFC3629], [RFC3986], [RFC5234], [RFC5646], [USASCII]
- Informative: [Err1912], [RFC2045], [RFC2047], [RFC2231], [RFC2277], [RFC2388]

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Recipients implementing this specification MUST support the character sets "ISO-8859-1" and "UTF-8". | shall | Section 3.2 |
| R2 | Producers MUST use either the "UTF-8" or the "ISO-8859-1" character set. | shall | Section 3.2.1 |
| R3 | The charset is REQUIRED; language is OPTIONAL in ext-value. | shall | Section 3.2.1 |
| R4 | Characters not in attr-char must be percent-encoded after encoding to octets using the specified charset. | mandatory | Section 3.2.1 |
| R5 | The key words (MUST, SHOULD, etc.) are interpreted as described in [RFC2119]. | normative | Section 2 |
| R6 | Parameter continuations are NOT part of this encoding. | prohibition | Section 3.1 |
| R7 | Language specification in encoded words is NOT included. | omission | Section 3.3 |
| R8 | Specifications using the extension ought to normatively reference this RFC and include ext-value ABNF. | SHOULD | Section 4 |
| R9 | When parameter value is textual and language known, ext-value ought to be used. | SHOULD | Section 4.1 |
| R10 | Extended parameter should take precedence over regular parameter with same name. | SHOULD | Section 4.2 |

## Informative Annexes (Condensed)
- **Section 3.2.2 Examples**: Demonstrates encoding of POUND SIGN (ISO-8859-1 and UTF-8) and EURO SIGN (UTF-8) in extended parameters. Illustrates percent-encoding of space and optional language.
- **Section 4 Error Handling Example**: Shows dual supply of ASCII and internationalized title; recipients should prefer the extended syntax. Notes implementation failures at time of writing.
- **Security Considerations**: Warns of spoofing via non-ASCII, UTF-8 attacks, and potential multi-language parameter spoofing.