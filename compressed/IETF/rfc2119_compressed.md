# RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
**Source**: Network Working Group, IETF | **Version**: BCP 14 | **Date**: March 1997 | **Type**: Normative (Best Current Practice)
**Original**: https://www.rfc-editor.org/rfc/rfc2119

## Scope (Summary)
Defines the meaning of capitalized key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) used in IETF documents to specify requirement levels. Authors should incorporate a specific phrase near the beginning of their document to reference this definition. Note that the force of these words is modified by the requirement level of the document in which they are used.

## Normative References
- None (self-contained)

## Definitions and Abbreviations
- **MUST / REQUIRED / SHALL**: Absolute requirement of the specification.
- **MUST NOT / SHALL NOT**: Absolute prohibition of the specification.
- **SHOULD / RECOMMENDED**: Valid reasons may exist to ignore, but full implications must be understood and carefully weighed.
- **SHOULD NOT / NOT RECOMMENDED**: Valid reasons may exist when the behavior is acceptable, but full implications should be understood and carefully weighed.
- **MAY / OPTIONAL**: Truly optional; one vendor may include, another may omit. Implementations without the option MUST be prepared to interoperate with those that include it (possibly with reduced functionality), and implementations with the option MUST be prepared to interoperate with those without it (except for the feature the option provides).

Authors should incorporate the following phrase near the beginning of their document:
> The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 1. MUST
This word, or the terms "REQUIRED" or "SHALL", mean that the definition is an absolute requirement of the specification.

## 2. MUST NOT
This phrase, or the phrase "SHALL NOT", mean that the definition is an absolute prohibition of the specification.

## 3. SHOULD
This word, or the adjective "RECOMMENDED", mean that there may exist valid reasons in particular circumstances to ignore a particular item, but the full implications must be understood and carefully weighed before choosing a different course.

## 4. SHOULD NOT
This phrase, or the phrase "NOT RECOMMENDED", mean that there may exist valid reasons in particular circumstances when the particular behavior is acceptable or even useful, but the full implications should be understood and the case carefully weighed before implementing any behavior described with this label.

## 5. MAY
This word, or the adjective "OPTIONAL", mean that an item is truly optional. One vendor may choose to include the item because a particular marketplace requires it or because the vendor feels that it enhances the product while another vendor may omit the same item. An implementation which does not include a particular option MUST be prepared to interoperate with another implementation which does include the option, though perhaps with reduced functionality. In the same vein an implementation which does include a particular option MUST be prepared to interoperate with another implementation which does not include the option (except, of course, for the feature the option provides.)

## 6. Guidance in the use of these Imperatives
Imperatives of the type defined in this memo must be used with care and sparingly. In particular, they MUST only be used where it is actually required for interoperation or to limit behavior which has potential for causing harm (e.g., limiting retransmissions). For example, they must not be used to try to impose a particular method on implementors where the method is not required for interoperability.

## 7. Security Considerations
These terms are frequently used to specify behavior with security implications. The effects on security of not implementing a MUST or SHOULD, or doing something the specification says MUST NOT or SHOULD NOT be done may be very subtle. Document authors should take the time to elaborate the security implications of not following recommendations or requirements as most implementors will not have had the benefit of the experience and discussion that produced the specification.

## 8. Acknowledgments (Condensed)
The definitions are an amalgam from a number of RFCs. Suggestions from Robert Ullmann, Thomas Narten, Neal McBurnett, and Robert Elz are acknowledged.

## 9. Author's Address (Condensed)
Scott Bradner, Harvard University. Phone: +1 617 495 3864, Email: sob@harvard.edu.

## Requirements Summary
| ID | Requirement (Exact Text) | Type | Reference |
|---|---|---|---|
| R1 | MUST / REQUIRED / SHALL: absolute requirement of the specification | shall | Section 1 |
| R2 | MUST NOT / SHALL NOT: absolute prohibition of the specification | shall not | Section 2 |
| R3 | SHOULD / RECOMMENDED: may exist valid reasons to ignore, but full implications must be understood and carefully weighed | should | Section 3 |
| R4 | SHOULD NOT / NOT RECOMMENDED: may exist valid reasons for acceptable behavior, but full implications should be understood and carefully weighed | should not | Section 4 |
| R5 | MAY / OPTIONAL: truly optional; interoperability constraints apply (see text) | may | Section 5 |
| R6 | Imperatives MUST only be used where required for interoperation or to limit harmful behavior | shall | Section 6 |
| R7 | Authors should elaborate security implications of not following recommendations/requirements | should | Section 7 |

## Informative Annexes (Condensed)
None.