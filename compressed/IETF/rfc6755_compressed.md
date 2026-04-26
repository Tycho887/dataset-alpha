# RFC 6755: An IETF URN Sub-Namespace for OAuth
**Source**: IETF | **Version**: RFC 6755 | **Date**: October 2012 | **Type**: Informational
**Original**: http://www.rfc-editor.org/info/rfc6755

## Scope (Summary)
Creates and registers an IETF URN Sub-namespace `urn:ietf:params:oauth` for use by OAuth-related specifications to identify extensions or other context, following the process in RFC 3553.

## Normative References
- [RFC2141]: Moats, R., "URN Syntax", May 1997.
- [RFC3553]: Mealling, M., et al., "An IETF URN Sub-namespace for Registered Protocol Parameters", BCP 73, June 2003.
- [RFC5226]: Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, May 2008.

## Definitions and Abbreviations
- **OAuth URI**: A URI of the form `urn:ietf:params:oauth:<value>` registered in the OAuth URI registry.
- **Specification Required**: Per RFC 5226, the registration policy for new entries.
- **Change Controller**: For Standards Track RFCs, "IETF"; otherwise, name of responsible party.

## Section 1: Introduction
- Various OAuth 2.0 extensions and companion specifications use URIs to identify extensions. This document creates the `urn:ietf:params:oauth` sub-namespace.

## Section 2: Registration Template
- **2. Registration Procedure**: A registrant requesting an OAuth URI must use the form `urn:ietf:params:oauth:<value>` where `<value>` represents the functionality. The procedure is "Specification Required" per RFC 5226.
- **Template fields**:
  - **URN**: The URI identifying the registered functionality.
  - **Common Name**: The generally known name.
  - **Change Controller**: For Standards Track RFCs, state "IETF". For others, give name of responsible party. Other details (postal, email, URI) may be included.
  - **Specification Document(s)**: Reference to the document specifying the URI, preferably including a retrieval URI. An indication of relevant sections may be included but is not required.
- **2.1 Example Registration Request** (informative): Illustrates registration of `urn:ietf:params:oauth:grant-type:example` with Common Name "An Example Grant Type for OAuth 2.0", Change Controller "IETF", and a specification document URI.

## Section 3: Security Considerations
- No additional security considerations beyond those inherent to URNs (see RFC 2141). Familiarity with OAuth 2.0 security considerations (OAUTH-V2) is recommended.

## Section 4: IANA Considerations
- IANA has created:
  - A new URN Sub-namespace `urn:ietf:params:oauth:` per RFC 3553 (registration in Section 4.1).
  - A new registry called "OAuth URI" for URNs subordinate to `urn:ietf:params:oauth`, added to the "OAuth Parameters" top-level registry (as defined by OAUTH-V2). Instructions for requesting registration are in Section 2.

### 4.1 IETF URN Sub-Namespace Registration `urn:ietf:params:oauth`
- **Registry name**: oauth
- **Specification**: [this document]
- **Repository**: The registry created in Section 2.
- **Index value**: Values subordinate to `urn:ietf:params:oauth` are of the form `urn:ietf:params:oauth:<value>` with `<value>` as index. It is suggested that `<value>` include a "class" and an "identifier-within-class" separated by a colon (":"); other compositions may also be used.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A registrant requesting an OAuth URI shall use the form `urn:ietf:params:oauth:<value>` where `<value>` represents the functionality. | shall (implied by procedure) | Section 2 |
| R2 | Registration procedure is "Specification Required" per RFC 5226. | mandatory (per policy) | Section 2 |
| R3 | Change Controller field: For Standards Track RFCs, shall be "IETF". | shall | Section 2 |
| R4 | The URN Sub-namespace `urn:ietf:params:oauth` is registered per RFC 3553. | shall | Section 4.1 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgements**: Lists contributors: Stephen Farrell, Barry Leiba, Peter Saint-Andre, Eran Hammer, John Bradley, Ben Campbell, Michael B. Jones.
- **Example (Section 2.1)**: Demonstrates a sample registration request for `urn:ietf:params:oauth:grant-type:example` with required fields.