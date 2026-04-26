# RFC 3553: An IETF URN Sub-namespace for Registered Protocol Parameters
**Source**: IETF | **Version**: BCP 73 | **Date**: June 2003 | **Type**: Normative (Best Current Practice)
**Original**: https://www.rfc-editor.org/rfc/rfc3553

## Scope (Summary)
This document defines the "params" sub-namespace under the "ietf" URN namespace (RFC 2648), providing a standardized mechanism for naming protocol parameters registered with IANA. It specifies the structure, assignment process, and persistence rules for such URNs.

## Normative References
- [1] Moats, R., "URN Syntax", RFC 2141, May 1997.
- [2] Moats, R., "A URN Namespace for IETF Documents", RFC 2648, August 1999.
- [3] Daigle, L., et al., "Uniform Resource Names (URN) Namespace Definition Mechanisms", BCP 66, RFC 3406, October 2002.
- [4] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 2434, October 1998.
- [7] Hoffman, P. and M. Blanchet, "Preparation of Internationalized Strings ("stringprep")", RFC 3454, December 2002.

## Definitions and Abbreviations
- **URN**: Uniform Resource Name.
- **IETF**: Internet Engineering Task Force.
- **IESG**: Internet Engineering Steering Group.
- **IANA**: Internet Assigned Numbers Authority.
- **"params"**: The sub-namespace under "ietf" for registered protocol parameters.
- **Sub-namespace**: A named component within a URN namespace, e.g., `urn:ietf:params:*`.

## 1. Introduction (Informative)
IETF standards require registration of protocol elements (e.g., port numbers, MIME types) in a central IANA repository. A need exists to reference these as URIs. This document creates the "params" sub-delegation to standardize naming. Assignments are made via RFCs following IETF consensus and must include the template in Section 4.

## 2. Terminology
The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119.

## 3. IETF Sub-namespace Specifics
### Sub-namespace name
`params`

### Declared registrant
The Internet Engineering Task Force

### Declaration of structure
The namespace is primarily opaque. IANA may suggest names but reserves the right to assign names within IESG guidelines. The colon character (`:`) denotes a limited hierarchy: items on both sides are valid names. The left side represents a class containing other items (e.g., `urn:ietf:params:dns:rr-type-codes` for the list, `urn:ietf:params:dns:rr-type-codes:soa` for an individual code).

### Relevant ancillary documentation
[3], [2], [1]

### Identifier uniqueness considerations
The IESG uses IETF consensus to ensure unique sub-namespace names. IANA ensures uniqueness by comparing new names against previously assigned names; if a conflict arises, IANA requests a new string from the registrant.

### Identifier persistence considerations
- Once allocated, a name **MUST NOT** be re-allocated for a different purpose.
- Rules for value assignments **MUST** be constructed so the meaning of values cannot change.
- This mechanism is not appropriate for naming values whose meaning may change over time.
- If a value changes, the assignment **MUST** name the container or concept, not the value itself. Example: `urn:ietf:params:foo-params:foo` identifies a slot; it is not valid to embed a changing value unless it is persistent (e.g., version number).

### Process of identifier assignment
Identifiers are assigned only after a protocol element or number has been registered with IANA using standard policies and procedures, or documented in a standards-track RFC. The gating function is "IETF Consensus" as per RFC 2434 [4].

### Process of identifier resolution
At this time, no resolution mechanism is defined.

### Rules for Lexical Equivalence
Lexical equivalence is achieved by exact string match per URN syntax (RFC 2141 [1]). The `stringprep` standard (RFC 3454) does not apply.

### Conformance with URN Syntax
No additional characters are reserved.

### Validation mechanism
None.

### Scope
Global

## 4. Assigning Names
The creation of a new registry name requires:
- Registry name (typically same as IANA registry name)
- Specification (relevant IETF documents)
- Repository (pointer to current location of registry; may change over time)
- Index value (description of how to embed a registered value in the URI; **MUST** include details of transformations to conform to URN syntax and canonicalization for case-sensitive comparison)

For complex registries, repeat information for sub-namespaces. Clarify whether a name is assigned to the sub-namespace itself.

**Template:**
- **Registry name**: The name of the sub-namespace.
- **Specification**: Relevant IETF published documents.
- **Repository**: Pointer to current location of registry in protocol parameters repository or relevant RFCs.
- **Index value**: Description of how to embed a registered value in the URI; **MUST** include transformations and canonicalization details.

The process for requesting a URN assignment is to include the above template in the IANA Considerations section of the specifying document.

## 5. Security Considerations
None beyond those inherent to URNs (see RFC 2141 [1]). Additional considerations for URN resolution are in RFC 3404 [5] (part of DDDS series starting with RFC 3401 [6]).

## 6. IANA Considerations
This document imposes an additional assignment process on IANA. To minimize burden, sub-namespace registrations **MUST** be clear about inclusion criteria. Defining a registry that fits URN constraints imposes extra discipline.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Once a name has been allocated it **MUST NOT** be re-allocated for a different purpose. | SHALL | Section 3 (Identifier persistence) |
| R2 | Rules for assignments of values within a sub-namespace **MUST** be constructed so that the meaning of values cannot change. | SHALL | Section 3 (Identifier persistence) |
| R3 | If a value changes over time, the assignment **MUST** name the container or concept that contains the value, not the value itself. | SHALL | Section 3 (Identifier persistence) |
| R4 | Identifiers are assigned only after a particular protocol element or number has been registered with IANA using standard policies and procedures, or documented in an RFC describing a standards track protocol. | SHALL | Section 3 (Process of identifier assignment) |
| R5 | The Index value description **MUST** include details of any transformations needed for the resulting string to conform to URN syntax rules and any canonicalization needed for case-sensitive string comparison. | SHALL | Section 4 (Template) |

## Informative Annexes (Condensed)
- **7. Intellectual Property Statement**: Standard IETF IPR disclaimer (BCP-11). Not modified.
- **8. Normative References**: See list above.
- **9. Authors' Addresses**: Contact information for M. Mealling, L. Masinter, T. Hardie, G. Klyne.
- **10. Full Copyright Statement**: Standard IETF copyright (2003), allowing reproduction and derivative works with copyright notice retained. Document provided "AS IS" with disclaimer.