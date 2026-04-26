# RFC 8615: Well-Known Uniform Resource Identifiers (URIs)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2019 | **Type**: Normative
**Original**: [https://www.rfc-editor.org/info/rfc8615](https://www.rfc-editor.org/info/rfc8615)

## Scope (Summary)
Defines the path prefix `/.well-known/` for “well-known locations” in HTTP, HTTPS, WS, and WSS URI schemes, and provides a registration mechanism to avoid collisions. Obsoletes RFC 5785; updates RFC 7230 and RFC 7595.

## Normative References
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels
- [RFC3986] – Uniform Resource Identifier (URI): Generic Syntax
- [RFC6454] – The Web Origin Concept
- [RFC7230] – Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
- [RFC8126] – Guidelines for Writing an IANA Considerations Section in RFCs
- [RFC8174] – Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words

## Definitions and Abbreviations
- **Well-Known URI**: A URI whose path component begins with `/.well-known/`, provided the scheme explicitly supports well-known URIs (Section 3).
- **`/.well-known/`**: The reserved path prefix for well-known locations.
- **Well-Known URI Registry**: IANA registry at <https://www.iana.org/assignments/well-known-uris/>.
- **URI Scheme Registry**: IANA registry; updated to include a “Well-Known URI Support” field.

## Section 2: Notational Conventions
The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, and OPTIONAL in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals.

## Section 3: Well-Known URIs
- **Definition**: A well-known URI is a URI whose path component begins with `/.well-known/`, provided that the scheme is explicitly defined to support well-known URIs. (Normative)
- **Scheme support**: This specification updates “http” and “https” [RFC7230] to support well-known URIs. Other schemes (e.g., “ws”, “wss” per [RFC8307]) may be updated separately.
- **Registration requirement**: Applications that wish to mint new well-known URIs **MUST** register them following Section 5.1 procedures, subject to the following requirements.
- **Name conformance**: Registered names **MUST** conform to the “segment-nz” production in [RFC3986] (cannot contain `/`).
- **Precision**: Registered names **SHOULD** be correspondingly precise; squatting on generic terms is not encouraged.
- **Registration content**: At a minimum, a registration must reference a specification that defines the format and associated media type(s) for the well-known URI, along with the URI scheme(s) it can be used with. If no schemes are specified, “http” and “https” are assumed.
- **Port**: Applications **MUST** explicitly specify any alternative port.
- **Additional information**: Registrations MAY include additional path components, query strings, fragment identifiers, or protocol-specific details (e.g., HTTP method handling).
- **Hostname and scope**: Not defined by this specification; applications should define both.
- **Root requirement**: Well-known URIs are rooted at the top of the path hierarchy (e.g., `/.well-known/example` is well-known; `/foo/.well-known/example` is not).

### Section 3.1: Registering Well-Known URIs
- **Registry location**: <https://www.iana.org/assignments/well-known-uris/>
- **Registration requests**: Must include at least: URI suffix, Change controller, Specification document(s), Status, Related information (optional).
- **Status values**: 
  - Permanent: for values defined by Standards Track RFCs or other open standards [RFC2026]; others may become permanent if experts find them in use.
  - Provisional: for other values (SHOULD be registered as provisional).
- **Removal/upgrade**: Provisional entries can be removed by experts if not in use; experts may change status to permanent after consulting the community.
- **Third-party registration**: Allowed if an unregistered well-known URI is widely deployed and unlikely to be registered in a timely manner.

## Section 4: Security Considerations (Summarized)
### 4.1 Protecting Well-Known Resources
Server operators should carefully control write access to well-known locations, especially when multiple entities are co-located on the same origin.

### 4.2 Interaction with Web Browsing
Well-known resources under http/https are accessible to browsers; applications must consider attack vectors (e.g., XSS, cookies, Web Storage). Mitigations include encrypting sensitive data, using `HttpOnly` and `Path` on cookies, `X-Content-Type-Options: nosniff`, application-specific media types, Content-Security-Policy, Referrer-Policy, and avoiding compression on sensitive information.

### 4.3 Scoping Applications
Applications must define the scope of well-known URIs and how to discover them; mis-scoping (e.g., applying policy to different hosts) can cause security and administrative issues.

### 4.4 Hidden Capabilities
Server operators may be unaware of the `.well-known` directory if hidden; attackers with write access could control its contents.

## Section 5: IANA Considerations
### 5.1 The Well-Known URI Registry
- **Updated procedure**: Specification Required [RFC8126]; Status column added; existing registrations marked as “permanent”.
- **Expert review**: Conformance to Section 3, availability/stability of specifying document, and Section 4 considerations.

### 5.2 The Uniform Resource Identifier (URI) Schemes Registry
- **New field**: “Well-Known URI Support” added to registration template, default “-”.
- **Initial values**: http, https → [RFC8615]; ws, wss → [RFC8307]; coap variants → [RFC7252], [RFC8323].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Applications that wish to mint new well-known URIs MUST register them, following the procedures in Section 5.1, subject to the following requirements. | MUST | Section 3, para 4 |
| R2 | Registered names MUST conform to the “segment-nz” production in [RFC3986] (no `/`). | MUST | Section 3, para 5 |
| R3 | Registered names for a specific application SHOULD be correspondingly precise; squatting on generic terms is not encouraged. | SHOULD | Section 3, para 6 |
| R4 | At a minimum, a registration will reference a specification that defines the format and associated media type(s) to be obtained by dereferencing the well-known URI, along with the URI scheme(s) that the well-known URI can be used with. If no URI schemes are explicitly specified, “http” and “https” are assumed. | MUST (implied by “will”) | Section 3, para 7 |
| R5 | If an alternative port is used, it MUST be explicitly specified by the application in question. | MUST | Section 3, para 8 |
| R6 | Registration requests consist of at least: URI suffix, Change controller, Specification document(s), Status, Related information. | MUST (procedural) | Section 3.1, para 2 |
| R7 | Values defined by Standards Track RFCs and other open standards [RFC2026] have a status of “permanent”. Other values should be registered as “provisional”. | SHOULD | Section 3.1, para 6 |
| R8 | Provisional entries can be removed by experts if not in use; experts may change status to permanent after consulting the community. | MAY | Section 3.1, para 7 |
| R9 | Well-known URIs can be registered by third parties if widely deployed and likely not to be registered otherwise. | MAY | Section 3.1, para 9 |
| R10 | The registry procedure is updated to Specification Required [RFC8126]; a Status column is added. | MUST (IANA action) | Section 5.1, para 1 |
| R11 | A “Well-Known URI Support” field is added to the URI Schemes registry; default “-”. | MUST (IANA action) | Section 5.2, para 1 |

## Informative Annexes (Condensed)
- **Appendix A: Frequently Asked Questions**: Addresses concerns: well-known locations are a necessary “sandbox”; `/.well-known/` chosen for brevity and low collision risk; no impact on existing mechanisms like P3P or robots.txt until they adopt it; per-directory well-known locations not defined due to collision and scalability issues.
- **Appendix B: Changes from RFC 5785**: Notable changes: allowed non-Web well-known locations; adjusted IANA instructions; updated references; made various clarifications; tracked supporting schemes in the URI Schemes registry.