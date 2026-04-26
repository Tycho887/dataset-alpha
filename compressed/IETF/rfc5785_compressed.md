# RFC 5785: Defining Well-Known Uniform Resource Identifiers (URIs)
**Source**: IETF | **Version**: Standards Track | **Date**: April 2010 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc5785

## Scope (Summary)
This document defines the path prefix "/.well-known/" for use in selected URI schemes (HTTP, HTTPS, and others explicitly specified) to provide a standardized location for site-wide metadata, reducing collisions and minimizing impact on existing URI space.

## Normative References
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC 3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC 5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.

## Definitions and Abbreviations
- **Well-Known URI**: A URI whose path component begins with "/.well-known/" and whose scheme is HTTP, HTTPS, or another scheme explicitly specified to use well-known URIs.
- **/.well-known/**: The path prefix designated for well-known locations within a URI.

## Section 1: Introduction
It is increasingly common for Web-based protocols to require discovery of site-wide metadata (e.g., robots.txt, P3P). To avoid collisions with other such locations and pre-existing resources, this memo defines a standardized path prefix "/.well-known/". Future specifications that need such metadata can register their use.

### 1.1 Appropriate Use of Well-Known URIs
Well-known URIs are not intended for general information retrieval or large URI namespaces; they are designed to facilitate discovery of policy or metadata when other mechanisms are impractical. They should be used to make site-wide policy information directly available or provide references to it.

## Section 2: Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## Section 3: Well-Known URIs
- A well-known URI is a URI whose path component begins with "/.well-known/" and whose scheme is HTTP, HTTPS, or another scheme explicitly specified to use well-known URIs.
- **R1**: Applications that wish to mint new well-known URIs **MUST** register them, following the procedures in Section 5.1.
- **R2**: Registered names **MUST** conform to the segment-nz production in RFC 3986.
- This specification does not define how to determine the authority for a particular context, nor the scope of the metadata; both should be defined by the application.
- A registration typically references a specification that defines the format and media type obtained by dereferencing the well-known URI.
- A registration **MAY** contain additional information (e.g., syntax of path components, query strings, fragment identifiers, HTTP method handling).
- This specification does not define a format or media-type for the resource at "/.well-known/"; clients should not expect a resource to exist at that location.

## Section 4: Security Considerations
Individual applications must define the scope of applicability and discovery of well-known URIs. Applications minting new well-known URIs and administrators deploying them must consider: exposure of sensitive data, denial-of-service attacks, server and client authentication, DNS rebinding attacks, and limited access granting ability to affect serving of well-known URIs.

## Section 5: IANA Considerations
### 5.1 The Well-Known URI Registry
This document establishes the well-known URI registry.
- Registration is on the advice of one or more Designated Experts (appointed by IESG), with a Specification Required (RFC 5226).
- Designated Experts may approve registration before publication if satisfied that a specification will be published.
- Registration requests should be sent to wellknown-uri-review@ietf.org.
- Within 14 days, the Designated Expert(s) will approve or deny, communicating to the review list and IANA. Denials should include explanation and suggestions.
- Undetermined requests after 21 days may be brought to IESG attention.

#### 5.1.1 Registration Template
- **URI suffix**: The name relative to "/.well-known/", e.g., "example".
- **Change controller**: For Standards-Track RFCs, "IETF"; otherwise, responsible party.
- **Specification document(s)**: Reference to the document that specifies the field, preferably with a retrieval URI.
- **Related information**: Optionally, citations to additional relevant documents.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Applications that wish to mint new well-known URIs **MUST** register them, following the procedures in Section 5.1. | shall | Section 3 |
| R2 | Registered names **MUST** conform to the segment-nz production in RFC 3986. | shall | Section 3 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgements**: Thanks to contributors (list omitted) for feedback and use cases.
- **Appendix B. Frequently Asked Questions**: Clarifies that while well-known locations are generally bad for the Web, this memo creates a "sandbox" to reduce risks; explains choice of "/.well-known/" (short, descriptive, not widely used); notes no immediate impact on existing mechanisms like P3P and robots.txt; and explains why per-directory locations are not defined (increased collision risk and poor scalability).