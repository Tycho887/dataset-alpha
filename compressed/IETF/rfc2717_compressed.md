# RFC 2717: Registration Procedures for URL Scheme Names
**Source**: IETF | **Version**: BCP 35 | **Date**: November 1999 | **Type**: Best Current Practice  
**Original**: https://tools.ietf.org/html/rfc2717

## Scope (Summary)
This document defines the process for registering new Uniform Resource Locator (URL) scheme names to prevent collisions and ensure orderly, well-specified, public development of schemes intended for widespread use. It establishes multiple registration trees, with primary focus on the IETF tree.

## Normative References
- [1] Berners-Lee, T., Fielding, R. and L. Masinter, "Uniform Resource Identifiers (URI): Generic Syntax", RFC 2396, August 1998.
- [2] Masinter, L., Alvestrand, H., Zigmond, D. and R. Petke, "Guidelines for new URL Schemes", RFC 2718, November 1999.
- [3] Postel, J. and J. Reynolds, "Instructions to RFC Authors", RFC 2223, October 1997.

## Definitions and Abbreviations
- **URL scheme name**: The `<scheme>` portion of a URL as defined in RFC 2396.
- **IETF Tree**: A registration tree for URL schemes of general interest to the Internet community, under IETF ownership and control.
- **Alternative Trees**: Additional top-level registration trees created by IESG that may have different registration and change control requirements.

## Notation
The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119.

## 1 Introduction
A registration process is needed to ensure that names of all new URL schemes are guaranteed not to collide and that schemes intended for widespread public use are developed in an orderly, well-specified, and public manner. This document defines registration procedures; RFC 2718 provides guidelines for creating new URL schemes.

## 2 URL Scheme Name Registration Trees
### 2.1 General
Multiple registration trees exist to accommodate different requirements. The first step is determining which tree is appropriate based on intended use and desired syntax.

### 2.2 The IETF Tree
Intended for URL schemes of general interest to the Internet community. Requires substantive review and approval. Expect applicability statements recommending implementation of proven schemes.

### 2.3 Additional Registration Trees
IESG may create new top-level trees as needed. These may require little or no registration and allow change control to rest with individuals or groups other than IETF. A new tree shall only be created if no existing tree addresses the set of needs.

## 3 Requirements for Scheme Name Registration
### 3.1 General Requirements
- **R1**: All new URL schemes, regardless of registration tree, **MUST** conform to the generic syntax for URLs as specified in RFC 2396.

### 3.2 The IETF Tree
- **R2**: Registration in the IETF tree requires publication of syntax and semantics in either an Informational or Standards Track RFC. In general, creation requires a Standards Track RFC. An Informational RFC may be used only for schemes already in wide usage meeting other standards (e.g., demonstrated utility); IESG has broad discretion and may recommend changes or reject publication.
- **R3**: An Informational RFC purporting to describe a URL scheme **shall not** be published without IESG approval (departure from RFC 2026).
- **R4**: The names of schemes registered in the IETF tree **MUST NOT** contain the dash character ('-', USASCII 2Dh) to avoid confusion with alternative trees.
- **R5**: An analysis of security issues inherent in the new URL scheme is **REQUIRED**.
- **R6**: URL schemes registered in the IETF tree **should not** introduce additional security risks into the Internet Architecture.
- **R7**: The "owner" of a URL scheme name in the IETF tree is assumed to be the IETF itself. Modification or alteration requires the same level of processing (Informational or Standards Track RFC) as initial registration. Schemes defined via Informational RFC may be replaced with Standards Track documents.

### 3.3 Alternative Trees
- **R8**: While public exposure and review are not required, using the IETF Internet-Draft mechanism for peer review is **strongly encouraged**.
- **R9**: RFC publication of alternative tree URL schemes is **encouraged but not required**. Material may be published as an Informational RFC by sending it to the RFC Editor per RFC 2223.
- **R10**: The defining document for an alternative tree **may** require public exposure and/or review via a mechanism other than the IETF Internet-Draft mechanism.
- **R11**: URL schemes created in an alternative tree **must** conform to the generic URL syntax (RFC 2396). The tree's defining document **may** set forth additional syntax and semantics requirements beyond RFC 2396.
- **R12**: All new URL schemes **SHOULD** follow the Guidelines for URL Schemes (RFC 2718).
- **R13**: An analysis of security issues is **encouraged**. All descriptions of security issues **must** be as accurate as possible. A statement like "no security issues" **must not** be confused with unassessed or unpredictable issues.
- **R14**: There is **absolutely no requirement** that alternative tree URL schemes be secure or free from risks. Nevertheless, the tree's defining document **must** set forth the standard for security considerations, and all known security risks **SHOULD** be identified.
- **R15**: Change control **must** be defined for a new tree. Change control **may** be vested in IETF, an individual, group, or other entity. The change control standard for the tree **must** be approved by the IESG.
- **R16**: The syntax for alternative trees **shall** be as follows: each tree will be identified by a unique prefix established in the same fashion as an IETF tree scheme name, except that the prefix **must** be defined by a Standards Track document. Scheme names are constructed by prepending the prefix to a tree-specific identifier: `<prefix>'-'<tree-specific identifier>`.

## 4 Registration Procedures
### 4.1 The IETF Tree
- **R17**: The first step is to publish an IETF Internet-Draft detailing syntax and semantics. The draft **must**, minimally, address all items covered by the registration template (Section 6).
- **R18**: After all issues raised during a review period of **no less than 4 weeks** have been addressed, submit the draft to the IESG for review.
- **R19**: The IESG will review and either refer the scheme to a working group (existing or new) or directly present to the IESG for last call. In the former case, the working group is responsible for submitting a final version to the IESG for approval after adequate review.

### 4.2 Alternative Trees
- **R20**: Registration **may** be formal (IETF documents, IANA registration, or other acknowledged organization), informal (mailing list or other publication mechanism), or nonexistent. The registration mechanism **must** be documented for each alternative tree and **must** be consistent for all scheme names created in that tree.
- **R21**: It is the responsibility of the tree's creator to establish that the registration mechanism is workable; IESG **may** reject the tree's defining document if the mechanism is impractical or creates an undue burden on a party who will not accept it.

## 5 Change Control
### 5.1 Schemes in the IETF Tree
- **R22**: URL schemes in the IETF tree are owned by the IETF and **may** be changed by updating the RFC that describes them. Standards Track RFCs **may** be replaced with new Standards Track RFCs. Informational RFCs **may** be replaced with new Informational or Standards Track RFCs.

### 5.2 Schemes in Alternative Trees
- **R23**: Undocumented alternative tree schemes (as allowed by the tree's rules) **may** be changed by their owner at any time without notifying the IETF.
- **R24**: Alternative tree schemes documented by an Informational RFC **may** be changed at any time by the owner, but an updated Informational RFC detailing changes **must** be submitted to the IESG.
- **R25**: The owner of an alternative tree scheme documented by an Informational RFC **may** pass responsibility to another person or agency by informing the IESG.
- **R26**: The IESG **may** reassign responsibility for an alternative tree scheme documented by an Informational RFC (e.g., when owner is unreachable).
- **R27**: The IESG **may** reclassify an alternative tree scheme documented via an Informational RFC as "historic" if it determines the scheme is no longer in use.

## 6 Registration Template
The following items **must** be addressed when documenting a new URL scheme (for IETF tree; guideline for alternative trees):
- URL scheme name
- URL scheme syntax (use ABNF recommended; refer to RFC 2718)
- Character encoding considerations (e.g., support for character sets beyond USASCII)
- Intended usage (resource type or action; if not resource, explain action; identify associated MIME type)
- Applications and/or protocols that use the scheme (include references to documentation)
- Interoperability considerations (e.g., proprietary encoding, inability to support multibyte characters, incompatibility with underlying protocol)
- Security considerations
- Relevant publications
- Person and email address for further information
- Author/Change controller

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All new URL schemes MUST conform to generic syntax (RFC 2396). | shall | Section 3.1 |
| R2 | IETF tree registration requires publication in Informational or Standards Track RFC; generally Standards Track required; Informational only for wide usage with IESG discretion. | shall | Section 3.2 |
| R3 | Informational RFC describing a URL scheme shall not be published without IESG approval. | shall | Section 3.2 |
| R4 | Scheme names in IETF tree MUST NOT contain dash ('-'). | shall | Section 3.2 |
| R5 | Security analysis is REQUIRED for IETF tree schemes. | required | Section 3.2 |
| R6 | IETF tree schemes should not introduce additional security risks. | should | Section 3.2 |
| R7 | Owner of IETF tree scheme is IETF; changes require same processing level as initial registration. | shall | Section 3.2 |
| R8 | Using IETF Internet-Draft for peer review of alternative trees is strongly encouraged. | should | Section 3.3 |
| R9 | RFC publication of alternative tree schemes is encouraged but not required. | may | Section 3.3 |
| R10 | Alternative tree defining document may require public exposure/review via other mechanisms. | may | Section 3.3 |
| R11 | Alternative tree schemes must conform to RFC 2396; tree's document may add requirements. | must | Section 3.3 |
| R12 | All new schemes SHOULD follow RFC 2718 guidelines. | should | Section 3.3 |
| R13 | Security analysis is encouraged; descriptions must be accurate; avoid confusing "no issues" with unassessed. | must | Section 3.3 |
| R14 | No requirement for security in alternative trees, but document must set standard and identify risks. | must/should | Section 3.3 |
| R15 | Change control must be defined and approved by IESG. | must | Section 3.3 |
| R16 | Alternative tree syntax: prefix defined by Standards Track, then dash and tree-specific identifier. | shall | Section 3.3 |
| R17 | IETF tree draft must address all items in template (Section 6). | must | Section 4.1 |
| R18 | Review period of no less than 4 weeks before IESG submission. | shall | Section 4.1 |
| R19 | IESG may refer to working group or directly process. | may | Section 4.1 |
| R20 | Alternative tree registration mechanism must be documented and consistent. | must | Section 4.2 |
| R21 | IESG may reject tree if registration mechanism is impractical or burdensome. | may | Section 4.2 |
| R22 | IETF tree schemes may be changed via updated RFC. | may | Section 5.1 |
| R23 | Undocumented alternative tree schemes may be changed without notice. | may | Section 5.2 |
| R24 | Documented alternative tree schemes changed by owner require updated Informational RFC to IESG. | must | Section 5.2 |
| R25 | Owner may transfer responsibility by informing IESG. | may | Section 5.2 |
| R26 | IESG may reassign responsibility for alternative tree schemes. | may | Section 5.2 |
| R27 | IESG may reclassify alternative tree schemes as historic. | may | Section 5.2 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 7)**: Information creating or updating registration must be authenticated. Security vulnerabilities may change over time; claims should be updated. If IESG delegates registration to an external entity, that entity must have sufficient security procedures to authenticate changes.
- **Registration Template (Section 6)**: A detailed checklist for documenting new URL schemes, covering syntax, character encoding, intended usage, applications, interoperability, security, publications, contact, and change controller. Use ABNF; refer to RFC 2718.