# RFC 6657: Update to MIME regarding "charset" Parameter Handling in Textual Media Types
**Source**: IETF | **Version**: Standards Track | **Date**: July 2012 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc6657

## Scope
This document changes RFC 2046 rules regarding default "charset" parameter values for "text/*" media types to better align with common usage by existing clients and servers. It does not change defaults for any currently registered media type.

## Normative References
- [RFC2046] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.

## Definitions and Abbreviations
- **Key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL)**: As defined in [RFC2119].

## 1. Introduction and Overview (Condensed)
RFC 2046 specified default charset "US-ASCII" for "text/*" media types. RFC 2616 changed the HTTP default to "ISO-8859-1", causing confusion. Many complex subtypes (e.g., text/html, text/xml) carry charset information internally. This document updates RFC 2046 to address these issues.

## 2. Conventions Used in This Document
The key words are to be interpreted as described in [RFC2119].

## 3. New Rules for Default "charset" Parameter Values for "text/*" Media Types
Section 4.1.2 of [RFC2046] is replaced by the following rules:

- Each subtype of the "text" media type that uses the "charset" parameter can define its own default value for the "charset" parameter, including the absence of any default.
- To improve interoperability, "text/*" media type registrations SHOULD either:
  - **(a)** specify that the "charset" parameter is not used for the defined subtype, because the charset information is transported inside the payload (e.g., "text/xml"), or
  - **(b)** require explicit unconditional inclusion of the "charset" parameter, eliminating the need for a default value.
- Registrations for "text/*" media types that can transport charset information inside the payload (e.g., "text/html", "text/xml") SHOULD NOT specify the use of a "charset" parameter, nor any default value, to avoid conflicting interpretations should the "charset" parameter value and the value specified in the payload disagree.
- New subtypes of the "text" media type SHOULD NOT define a default "charset" value. If there is a strong reason to do so despite this advice, they SHOULD use "UTF-8" [RFC3629] as the default.
- **Regardless of the approach chosen, all new "text/*" registrations MUST clearly specify how the charset is determined; relying on the default defined in Section 4.1.2 of [RFC2046] is no longer permitted.**
- Existing "text/*" registrations that fail to specify how the charset is determined still default to US-ASCII.
- Specifications covering the "charset" parameter, and what default value, if any, are subtype-specific, NOT protocol-specific. **Protocols that use MIME, therefore, MUST NOT override default charset values for "text/*" media types to be different for their specific protocol. Protocol definitions MUST leave that to the subtype definitions.**

## 4. Default "charset" Parameter Value for "text/plain" Media Type
The default "charset" parameter value for "text/plain" remains "US-ASCII" (unchanged from [RFC2046]).

## 5. Security Considerations
Guessing the charset can lead to security issues (buffer overflows, denial of service, filtering bypass). This document encourages using charset information specified by the sender. Conflicting in-band vs. out-of-band information should be resolved by preferring in-band charset information when it is more likely to be correct.

## 6. IANA Considerations
IANA has updated the "text" subregistry of the Media Types registry to add the preamble: "See [RFC6657] for information about 'charset' parameter handling for text media types." Also, this RFC was added to the list of references at the beginning of the Application for Media Type.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Each subtype of "text" that uses "charset" can define its own default, including no default. | MAY | Section 3 |
| R2 | "text/*" registrations SHOULD either (a) specify "charset" not used or (b) require explicit inclusion of "charset". | SHOULD | Section 3 |
| R3 | Registrations for "text/*" that transport charset internally SHOULD NOT specify a "charset" parameter or default. | SHOULD | Section 3 |
| R4 | New "text/*" subtypes SHOULD NOT define a default "charset" value. | SHOULD | Section 3 |
| R5 | If a new "text/*" subtype defines a default despite R4, it SHOULD use "UTF-8". | SHOULD | Section 3 |
| R6 | All new "text/*" registrations MUST clearly specify how charset is determined; relying on RFC 2046 default is no longer permitted. | MUST | Section 3 |
| R7 | Existing "text/*" registrations without charset determination default to US-ASCII. | (default) | Section 3 |
| R8 | Protocols MUST NOT override default charset values for "text/*"; protocol definitions MUST leave that to subtype definitions. | MUST NOT / MUST | Section 3 |
| R9 | Default "charset" for "text/plain" remains US-ASCII. | (unchanged) | Section 4 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgements**: Thanks to Ned Freed, John Klensin, Carsten Bormann, Murray S. Kucherawy, Barry Leiba, and Henri Sivonen for comments and text suggestions.