# RFC 2718: Guidelines for New URL Schemes
**Source**: Internet Engineering Task Force (IETF) | **Version**: Informational | **Date**: November 1999 | **Type**: Informative
**Original**: https://datatracker.ietf.org/doc/rfc2718/

## Scope (Summary)
This document provides guidelines for the definition of new URL schemes, emphasizing syntactic compatibility, well-defined semantics, demonstrated utility, and security considerations.

## Normative References
- **RFC 2396**: Uniform Resource Identifiers (URI): Generic Syntax
- **RFC 2717**: Registration Procedures for URL Scheme Names
- **RFC 2279**: UTF-8, A Transformation Format of Unicode and ISO 10646

## Definitions and Abbreviations
- **URL**: Uniform Resource Locator – a compact string representation of the location for a resource available via the Internet.
- **URI**: Uniform Resource Identifier – general syntax defined in RFC 2396.
- **Scheme**: The first component of a URI/URL (e.g., “http”, “ftp”).

## 1. Introduction (Summary)
RFC 2396 defines URI syntax; URLs are designated by “<scheme>:<scheme-specific-part>”. Many URL schemes already exist. This document provides guidelines for defining new URL schemes, complementing the registration process defined in RFC 2717.

## 2. Guidelines for New URL Schemes
New schemes **must** have demonstrable utility, operability, and compatibility with existing URL schemes.

### 2.1 Syntactic Compatibility
- **Motivations** – Sharing fragment, relative, “..”, “/”, and naming authority syntax allows content to be moved between schemes without rewriting. See Section 2.1.1 for detailed examples.
- **Improper use of “//”** – Double slashes after “<scheme>:” **must** be used ONLY when the scheme-specific-part contains a hierarchical structure as described in RFC 2396 (Section 3). Schemes without such structure **should not** use “//”.
- **Compatibility with relative URLs** – Schemes intended for relative URLs **should** follow RFC 2396 parsing. The scheme definition **should** describe allowed relative forms. Specifically:
  - Tokens “//”, “/”, “;”, “?” **should** have their RFC 2396 meanings if used.
  - The scheme **should** be usable in relative URLs as per RFC 2396.
  - If the syntax is broken into pieces, documentation **must** specify what the pieces are, why they are broken that way, and why they differ from RFC 2396.
  - Hierarchy, if present, **should** go left-to-right with slash separators.

### 2.2 Is the Scheme Well Defined?
- Semantics of the resource **must** be well defined.
- **Clear mapping from other name spaces** – The mapping **must** be complete, describe character encoding, and cover all legal values of the base standard.
- **URL schemes associated with network protocols** – The specification **must** describe how URLs translate to protocol actions unambiguously; configuration elements **must** be identified.
- **Definition of non-protocol URL schemes** – Must describe notation and a complete mapping of the locator.
- **Definition of URL schemes not associated with data resources** – The properties of names must be clearly defined.
- **Character encoding** – Recommended to translate character sequences into UTF-8 (RFC 2279) then %HH encoding for unsafe octets, unless a compelling reason for a different encoding exists.
- **Definition of operations** – The scheme definition **should** describe all well-defined operations on the URL identifier (e.g., GET). If only one operation is defined, that **must** be stated. Operations that are not GET-like (e.g., telnet) **should** be documented.

### 2.3 Demonstrated Utility
- New schemes are expensive to support; they **must** provide utility not achievable via existing schemes or proxy gateways.
- **Proxy into HTTP/HTML** – Consider whether a global resolution mechanism exists, whether users can “run their own proxy”, if operations map to HTTP, if returned objects have defined MIME types, and if running code exists.

### 2.4 Security Considerations
- **Must** address:
  - Whether user notification is needed for implicit GETs (e.g., IMG src).
  - Possibility of fake URLs pointing to dangerous resources.
  - Requester identification mechanisms (e.g., From: field, Kerberos).
  - Clear-text passwords or other security information passed in the URL.

### 2.5 Does It Start with “UR”?
- Schemes starting with “U” and “R” (e.g., “uniform”, “universal”) **should** have large consensus to avoid debate, or pick another name.

### 2.6 Non-Considerations
- Questions about whether all valid objects can be accessed by any user agent are not relevant to scheme definition; accessibility depends on factors like firewalls or client configuration.

## 3. Security Considerations
- New URL schemes are **required** to address all security considerations in their definitions.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| G1 | New URL schemes must have demonstrable utility and operability. | must | Section 2 |
| G2 | Schemes should follow generic URI syntax conventions where appropriate. | should | Section 2.1 |
| G3 | Double slashes after “<scheme>:” must only be used for hierarchical structure. | must | Section 2.1.2 |
| G4 | Schemes intended for relative URLs should be compatible with RFC 2396. | should | Section 2.1.3 |
| G5 | The semantics of the resource must be well defined. | must | Section 2.2 |
| G6 | Character encoding should use UTF-8 and %HH encoding unless compelling reason. | should | Section 2.2.5 |
| G7 | Scheme definition should describe all well-defined operations. | should | Section 2.2.6 |
| G8 | New URL schemes must address security considerations. | must | Section 2.4, Section 3 |

## Informative Annexes (Condensed)
- **Authors’ Addresses** – Boilerplate contact information for the document authors (omitted per compression rules).
- **Full Copyright Statement** – Standard IETF copyright notice; preserved in original but not reproduced here.