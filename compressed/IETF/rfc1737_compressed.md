# RFC 1737: Functional Requirements for Uniform Resource Names
**Source**: IETF Network Working Group | **Version**: Informational | **Date**: December 1994 | **Type**: Informative
**Original**: RFC 1737 (full text provided)

## Scope (Summary)
Specifies a minimum set of requirements for Uniform Resource Names (URNs) as globally unique, persistent identifiers for resources. URNs are part of the Internet Information Infrastructure Architecture, alongside Uniform Resource Characteristics (URCs) and Uniform Resource Locators (URLs). This document provides a basis for evaluating URN standards.

## Normative References
- None explicit. Based on discussions on IETF URI Working Group and mailing list uri@bunyip.com.

## Definitions and Abbreviations
- **URN (Uniform Resource Name)**: A globally unique, persistent identifier used for recognition, access to characteristics of a resource, or access to the resource itself.
- **URC (Uniform Resource Characteristics)**: A set of meta-level information about a resource (e.g., owner, encoding, access restrictions).
- **URL (Uniform Resource Locator)**: Identifies the location or a container for an instance of a resource identified by a URN.
- **Resource**: Any information, object, or entity that can be identified (not further defined by URI architecture).
- **Naming Authority**: Entity responsible for assigning URNs, guaranteeing uniqueness within its scope.

## Requirements for Functional Capabilities
- **Global scope**: A URN is a name with global scope which does not imply a location. It has the same meaning everywhere.
- **Global uniqueness**: The same URN will never be assigned to two different resources.
- **Persistence**: It is intended that the lifetime of a URN be permanent. That is, the URN will be globally unique forever, and may well be used as a reference to a resource well beyond the lifetime of the resource it identifies or of any naming authority involved in the assignment of its name.
- **Scalability**: URNs can be assigned to any resource that might conceivably be available on the network, for hundreds of years.
- **Legacy support**: The scheme must permit the support of existing legacy naming systems, insofar as they satisfy the other requirements described here. (e.g., ISBN, ISO public identifiers, UPC product codes)
- **Extensibility**: Any scheme for URNs must permit future extensions to the scheme.
- **Independence**: It is solely the responsibility of a name issuing authority to determine the conditions under which it will issue a name.
- **Resolution**: A URN will not impede resolution (translation into a URL). For URNs that have corresponding URLs, there must be some feasible mechanism to translate a URN to a URL.

## Requirements for URN Encoding
- **Single encoding**: The encoding for presentation for people in clear text, electronic mail, and the like is the same as the encoding in other transmissions.
- **Simple comparison**: A comparison algorithm for URNs is simple, local, and deterministic. That is, a single algorithm that does not require contacting any external server.
- **Human transcribability**: URNs should be short, use a minimum of special characters, and be case insensitive. Comparison is insensitive to case, and probably white space and some punctuation marks.
- **Transport friendliness**: A URN can be transported unmodified in common Internet protocols (TCP, SMTP, FTP, Telnet, etc.) as well as printed paper.
- **Machine consumption**: A URN can be parsed by a computer.
- **Text recognition**: The encoding of a URN should enhance the ability to find and parse URNs in free text.

## Implications (Condensed)
A URN specification must meet the above requirements. Key implications:
- Name assignment delegated to naming authorities (which may sub-delegate) to guarantee uniqueness; top-level authorities centrally registered.
- Scalable naming schemes encouraged but not required.
- Strongly recommended that each naming authority provide a mapping from names to URLs, though not necessarily by the authority itself.
- Character set must be limited for transcribability and transport.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A URN is a name with global scope which does not imply a location. It has the same meaning everywhere. | shall | Section 2 |
| R2 | The same URN will never be assigned to two different resources. | shall | Section 2 |
| R3 | It is intended that the lifetime of a URN be permanent. That is, the URN will be globally unique forever, and may well be used as a reference to a resource well beyond the lifetime of the resource it identifies or of any naming authority involved in the assignment of its name. | shall | Section 2 |
| R4 | URNs can be assigned to any resource that might conceivably be available on the network, for hundreds of years. | shall | Section 2 |
| R5 | The scheme must permit the support of existing legacy naming systems, insofar as they satisfy the other requirements described here. | shall (must) | Section 2 |
| R6 | Any scheme for URNs must permit future extensions to the scheme. | shall (must) | Section 2 |
| R7 | It is solely the responsibility of a name issuing authority to determine the conditions under which it will issue a name. | shall | Section 2 |
| R8 | A URN will not impede resolution (translation into a URL). For URNs that have corresponding URLs, there must be some feasible mechanism to translate a URN to a URL. | shall (must) | Section 2 |
| R9 | The encoding for presentation for people in clear text, electronic mail and the like is the same as the encoding in other transmissions. | shall | Section 3 |
| R10 | A comparison algorithm for URNs is simple, local, and deterministic. | shall | Section 3 |
| R11 | For URNs to be easily transcribable by humans without error, they should be short, use a minimum of special characters, and be case insensitive. URN comparison is insensitive to case, and probably white space and some punctuation marks. | should | Section 3 |
| R12 | A URN can be transported unmodified in the common Internet protocols, such as TCP, SMTP, FTP, Telnet, etc., as well as printed paper. | shall | Section 3 |
| R13 | A URN can be parsed by a computer. | shall | Section 3 |
| R14 | The encoding of a URN should enhance the ability to find and parse URNs in free text. | should | Section 3 |

## Informative Annexes (Condensed)

### Annex A: Other Considerations (Section 5)
This document intentionally does not take a position on three issues: equality of resources (each naming authority defines its own algorithm for distinguishing resources), reflection of visible semantics in a URN (discouraged because semantics may change), and name resolution (beyond recommending mapping mechanisms). Third-party and distributed resolvers are encouraged.

### Annex B: Security Considerations
Applications requiring name-to-location translation may require authentication. Authentication information should be carried separately from the URN itself, not embedded in the identifier.