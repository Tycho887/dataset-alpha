# RFC 2277: IETF Policy on Character Sets and Languages
**Source**: IETF | **Version**: BCP 18 | **Date**: January 1998 | **Type**: Best Current Practice  
**Original**: [RFC 2277 on ietf.org](https://tools.ietf.org/html/rfc2277)

## Scope (Summary)
This document establishes IETF policies for internationalization of Internet protocols, focusing on character sets and language tagging. It requires protocols to identify character sets, mandate UTF-8 support, provide language metadata, and support multilingual negotiation where applicable.

## Normative References
- **[RFC 2119]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- **[BCP9]**: Bradner, S., "The Internet Standards Process -- Revision 3", BCP 9, RFC 2026, October 1996.
- **[10646]**: ISO/IEC, Information Technology - Universal Multiple-Octet Coded Character Set (UCS) - Part 1: Architecture and Basic Multilingual Plane, May 1993, with amendments.
- **[UTF-8]**: Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 2279, January 1998.
- **[REG]**: Freed, N., and J. Postel, "IANA Charset Registration Procedures", BCP 19, RFC 2278, January 1998.
- **[WR]**: Weider, C., et al., "The Report of the IAB Character Set Workshop", RFC 2130, April 1997.
- **[RFC 1958]**: Carpenter, B., "Architectural Principles of the Internet", RFC 1958, June 1996.
- **[POSIX]**: ISO/IEC 9945-2:1993, Information technology -- Portable Operating System Interface (POSIX) -- Part 2: Shell and Utilities.

## Definitions and Abbreviations
- **charset**: A set of rules for mapping from a sequence of octets to a sequence of characters (e.g., combination of coded character set and character encoding scheme). Used as identifier in MIME `charset=` parameters and IANA charset registry.
- **name**: An identifier such as a person’s name, hostname, domain name, filename, or email address; often treated as an identifier rather than as a piece of text.
- **Default Language (tag “i-default”)**: Identifies the condition where the language preferences of the user cannot be established; a fallback for emergency situations.

## 1. Introduction
The Internet is international, requiring interchange of data in multiple languages. Based on the IAB Character Set Workshop (RFC 2130), this policy defines requirements for IETF standardization. The terms **MUST**, **SHOULD**, and **MAY** are used as defined in RFC 2119.

## 2. Where to do internationalization
Internationalization applies to text strings, not protocols. Where protocol elements resemble text tokens, **protocols MUST specify which parts are protocol and which are text** [WR 2.2.1.1].  
This document does **not** mandate a policy on name internationalization but **requires that all protocols describe whether names are internationalized or US-ASCII**.  
Responsibility for internationalization must be assigned explicitly; leaving it to “another layer” is allowed only if that layer is aware of the responsibility.

## 3. Definition of Terms

### 3.1. What charset to use
- **All protocols MUST identify, for all character data, which charset is in use.**
- **Protocols MUST be able to use the UTF-8 charset** (ISO 10646 + UTF-8) for all text.
- **Protocols MAY specify other charsets** (e.g., UTF-16), but lack of UTF-8 is a policy violation requiring variance per BCP 9 section 9.
- For existing protocols or data from existing datastores, support for other charsets or a default other than UTF-8 is acceptable, **but UTF-8 support MUST be possible**.
- **When using other charsets than UTF-8, these MUST be registered in the IANA charset registry** (register if necessary at publication).

### 3.2. How to decide a charset
When a protocol allows multiple charsets, the decision may involve negotiation (e.g., HTTP) or explicit identification with stored data (e.g., email). A charset is absolute; text cannot be rendered comprehensibly without supporting the chosen charset.  
Negotiation may be regarded as interim, but the timeframe may be permanent (≥50 years).

## 4. Languages

### 4.1. The need for language information
All human-readable text has a language. Language information benefits formatting, speech synthesis, searching, hyphenation, spellchecking [WC 3.1.1.4]. Protocols **must** specify how to transfer language information; machines cannot deduce it automatically.

### 4.2. Requirement for language tagging
- **Protocols that transfer text MUST provide for carrying information about the language of that text.**
- **Protocols SHOULD also provide for carrying information about the language of names**, where appropriate.
- The requirement does not force presence of the information; it mandates a well-defined mechanism if the sender wishes to include it.

### 4.3. How to identify a language
- **Protocols SHOULD use RFC 1766 language tags**, or provide clear and solid justification for doing otherwise.
- A language tag is distinct from a POSIX locale; a locale implies cultural conventions, not necessarily language.

### 4.4. Considerations for language negotiation
- **Protocols where users have text presented to them in response to user actions MUST provide for support of multiple languages.**
- Methods include client-server negotiation or sending multiple variants.
- Negotiation is a permanent requirement.

### 4.5. Default Language
- When the sender has no knowledge of the recipient’s language preferences (e.g., login failures, email warnings, prior to negotiation), **text SHOULD be presented in Default Language** (tag “i-default”).
- **Messages in Default Language MUST be understandable by an English-speaking person** because English is the most widely accessible language.
- Note: negotiating English is **not** the same as Default Language; Default Language is an emergency measure.

## 5. Locale
This document does **not require** communication of locale information on all text but **encourages** its inclusion when appropriate.  
Care must be taken to distinguish language and charset parts if included in a locale tag. The default locale is the “POSIX” locale.

## 6. Documenting internationalization decisions
In documents dealing with internationalization, a synopsis of the approaches chosen **SHOULD** be collected into a section called “Internationalization considerations”, placed next to the Security Considerations section.

## 7. Security Considerations
No significant security considerations identified beyond the risk that security warnings in a foreign language may cause inappropriate user behavior, and multilingual systems may have consistency issues between language variants.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Protocols MUST specify which parts are protocol and which are text. | MUST | Section 2 |
| R2 | Protocols MUST describe whether names are internationalized or US-ASCII. | MUST | Section 2 |
| R3 | All protocols MUST identify, for all character data, which charset is in use. | MUST | Section 3 |
| R4 | Protocols MUST be able to use UTF-8 for all text. | MUST | Section 3.1 |
| R5 | Protocols MAY specify other charsets, but lack of UTF-8 is a policy violation requiring variance. | MAY / MUST (violation) | Section 3.1 |
| R6 | When using other charsets than UTF-8, they MUST be registered in the IANA charset registry. | MUST | Section 3.1 |
| R7 | Protocols that transfer text MUST provide for carrying language information. | MUST | Section 4.2 |
| R8 | Protocols SHOULD provide for carrying language information of names. | SHOULD | Section 4.2 |
| R9 | Protocols SHOULD use RFC 1766 language tags. | SHOULD | Section 4.3 |
| R10 | Protocols that present text in response to user actions MUST support multiple languages. | MUST | Section 4.4 |
| R11 | When sender has no knowledge of recipient’s language preferences, text SHOULD be presented in Default Language (i-default). | SHOULD | Section 4.5 |
| R12 | Messages in Default Language MUST be understandable by an English-speaking person. | MUST | Section 4.5 |
| R13 | In documents dealing with internationalization, a synopsis SHOULD be placed in “Internationalization considerations” section. | SHOULD | Section 6 |

## Informative Annexes (Condensed)
- **Annex A (Author Contact)**: Harald Tveit Alvestrand, UNINETT, Norway.  
- **Annex B (Copyright)**: Full copyright notice and disclaimer as per Internet Society (1998); reproduction permitted with restrictions.