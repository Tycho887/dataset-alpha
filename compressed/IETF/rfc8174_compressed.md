# RFC 8174: Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
**Source**: Internet Engineering Task Force (IETF) | **Version**: BCP 14 | **Date**: May 2017 | **Type**: Normative (Best Current Practice)
**Original**: http://www.rfc-editor.org/info/rfc8174

## Scope (Summary)
This document clarifies that the key words defined in RFC 2119 (MUST, SHOULD, MAY, etc.) have their defined special meanings only when they appear in UPPERCASE. Lowercase usage retains normal English meanings.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **Key words (RFC 2119)**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL – only when in all capitals.
- **BCP**: Best Current Practice

## 1. Introduction
RFC 2119 specifies key words that "are often capitalized," causing confusion about non-capitalized words. This document updates RFC 2119 by clarifying that only UPPERCASE usage has the defined special meanings. This document is part of BCP 14.

## 2. Clarifying Capitalization of Key Words
The following change is made to [RFC2119]:

=== OLD ===
In many standards track documents several words are used to signify the requirements in the specification. These words are often capitalized. This document defines these words as they should be interpreted in IETF documents. Authors who follow these guidelines should incorporate this phrase near the beginning of their document:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

=== NEW ===
In many IETF documents, several words, when they are in all capitals as shown below, are used to signify the requirements in the specification. These capitalized words can bring significant clarity and consistency to documents because their meanings are well defined. This document defines how those words are interpreted in IETF documents when the words are in all capitals.

- These words can be used as defined here, but using them is not required. Specifically, normative text does not require the use of these key words. They are used for clarity and consistency when that is what's wanted, but a lot of normative text does not use them and is still normative.
- The words have the meanings specified herein only when they are in all capitals.
- When these words are not capitalized, they have their normal English meanings and are not affected by this document.

Authors who follow these guidelines should incorporate this phrase near the beginning of their document:

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

=== END ===

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Key words in RFC 2119 have defined meanings only when in all capitals; otherwise they have normal English meanings. | shall | Section 2 (NEW) |
| R2 | Authors should incorporate the specified phrase (including "when, and only when, they appear in all capitals") near the beginning of their document. | should | Section 2 (NEW) |
| R3 | Using these key words is not required; normative text may exist without them. | may (permissive) | Section 2 (bullet 1) |

## IANA Considerations
No IANA actions required.

## Security Considerations
This document is purely procedural; no related security considerations.

## Informative Annexes (Condensed)
- None.