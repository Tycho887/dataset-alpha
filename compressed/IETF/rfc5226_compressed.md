# RFC 5226 (BCP 26): Guidelines for Writing an IANA Considerations Section in RFCs
**Source**: Internet Engineering Task Force (IETF) | **Version**: BCP 26 (Obsoletes RFC 2434) | **Date**: May 2008 | **Type**: Best Current Practice (Normative)
**Original**: https://www.rfc-editor.org/rfc/rfc5226.txt

## Scope (Summary)
This document provides guidelines for authors on how to write an IANA Considerations section in RFCs that requires assignment of constants, protocol parameters, or other well-known values. It defines assignment policies (e.g., First Come First Served, Expert Review, Standards Action) and the roles of IANA and Designated Experts, ensuring clear instructions to IANA for managing namespaces.

## Normative References
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **Namespace**: The set of possible values for a field (numbers, strings, etc.).
- **Assigned number / code point / protocol constant**: A specific value bound to a particular purpose within a namespace.
- **Registration**: The act of assigning a value in a namespace.
- **Registry**: A repository of assigned values maintained by IANA.
- **Designated Expert**: An individual appointed by the IESG to evaluate assignment requests and recommend decisions to IANA.
- **IANA**: Internet Assigned Numbers Authority.
- **IESG**: Internet Engineering Steering Group.
- **RFC**: Request for Comments (publication series).
- **WG**: Working Group (of the IETF).
- **BCP**: Best Current Practice.
- **OID**: Object Identifier.

## Section 1: Introduction
- This document obsoletes RFC 2434.
- For IANA to manage a namespace, guidelines MUST describe conditions for assigning new values or modifying existing ones.
- Key words (MUST, SHOULD, etc.) are as defined in RFC 2119; "the specification" refers to IETF standards process documents.

## Section 2: Why Management of a Namespace May Be Necessary
- **Size**: Small spaces require careful assignment to prevent exhaustion; unlimited spaces may still need minimal review to prevent hoarding, sanity checks, and interoperability issues.
- **Delegation**: Delegate when possible to reduce IANA burden (e.g., DNS, OIDs).
- **Interoperability**: Unreviewed extensions can cause problems; community review is often essential.

## Section 3: Designated Experts
### 3.1 Motivation
- IANA does not define policy; it executes policies from RFCs. IANA needs clear guidelines to make decisions with minimal subjectivity.
- For review, a designated expert is used because WGs disband. IANA cannot participate in all mailing lists; the expert shepherds the request.
- Key motivation: IETF provides IANA with a subject matter expert to whom evaluation can be delegated.

### 3.2 Role of the Designated Expert
- The designated expert initiates and coordinates appropriate review (wide or narrow, as judged). They follow documented review criteria.
- Experts MUST be able to defend decisions to the IETF community. They are appointed by IESG (normally on Area Director recommendation).
- For some registries, multiple experts may be used; a single chair MUST define how requests are assigned. IANA MUST receive a single clear recommendation.
- The IESG may remove an expert.

### 3.3 Designated Expert Reviews
- Experts MUST respond in a timely fashion (normally within a week for simple requests, a few weeks for complex ones). Unreasonable delays MUST be raised with IESG.
- Expert acts as shepherd, enlisting help as appropriate. If a request is denied and controversial, expert should have support of other subject matter experts.
- In absence of specific criteria, the presumption is that a code point SHOULD be granted unless there is a compelling reason to deny. Possible denial reasons include: scarcity, insufficient documentation, harmful protocol extension, conflict with existing deployments, or conflict with IETF active development.

## Section 4: Creating a Registry
- Status labels for assignments: Private Use, Experimental, Unassigned, Reserved.

### 4.1 Well-Known IANA Policy Definitions
- **Private Use**: For local/private use; no IANA review.
- **Experimental Use**: For experimentation; similar to Private Use. See [EXPERIMENTATION].
- **Hierarchical Allocation**: Delegated managers assign values under IANA control (e.g., DNS names, IP addresses).
- **First Come First Served**: No substantive review; minimal clerical info required. IANA assigns values upon request.
- **Expert Review (Designated Expert)**: Approval by Designated Expert required; documentation and review criteria should be provided.
- **Specification Required**: Value must be documented in a permanent, publicly available specification. Implies use of Designated Expert to review clarity for interoperability.
- **RFC Required**: Publication of any RFC (IETF or independent submission) suffices.
- **IETF Review** (formerly "IETF Consensus"): Values assigned only through RFCs shepherded through IESG (AD-sponsored or WG documents) with IETF Last Call.
- **Standards Action**: Values assigned only for Standards Track RFCs approved by IESG.
- **IESG Approval**: IESG may approve assignments in special cases (e.g., expediency with strong consensus). Should not circumvent public review; community should be consulted via "call for comments". Use is not common.

### 4.2 What to Put in Documents That Create a Registry
Documents MUST include:
1. Name of registry (and sub-registry if applicable). Provide full name and abbreviation. Include URL that will be removed before publication.
2. What information must be provided in a request (e.g., security considerations).
3. Review process. When Designated Expert is used, document MUST NOT name the expert; name is conveyed to Area Director. If a public mailing list is to be used, must also specify Designated Expert.
4. Size, format, syntax of registry entries (e.g., decimal/hex, encoding like ASCII/UTF8).
5. Initial assignments and reservations.

Example text provided in the document.

### 4.3 Updating IANA Guidelines for Existing Registries
- Process similar to creating new namespace; document references existing namespace and provides detailed guidelines. Normally processed as BCP.

## Section 5: Registering New Values in an Existing Registry
### 5.1 What to Put in Documents When Registering Values
- Clearly identify namespace (use exact name and cite defining RFC). URL may be included but is normally removed.
- Each requested value should have a unique reference (e.g., TBD1, TBD2). For text strings, a specific name can be suggested; IANA will assign unless conflict.
- IANA Considerations section MUST summarize all IANA actions, with pointers to relevant sections. Include summary table in the format desired for IANA web site.

### 5.2 Updating Registrations
- Document defining namespace MUST state who is responsible for maintaining/updating a registration. Options: author (subject to same constraints), mechanism for attaching comments, designation of IESG/Designated Expert to change registrant.

### 5.3 Overriding Registration Procedures
- IESG may approve assignments in cases where documented procedures are too stringent, unclear, or incomplete, provided there is strong IETF consensus. This is not to overrule proper procedures but to permit assignments when updating procedures is too heavy a burden. If used, it indicates IANA registration procedures should be updated.

## Section 6: Miscellaneous Issues
### 6.1 When There Are No IANA Actions
- Document MUST include an IANA Considerations section stating "This document has no IANA actions." Only after careful verification. Can optionally note that values are managed by another registry, and may request that the section be removed or kept.

### 6.2 Namespaces Lacking Documented Guidance
- All future RFCs that rely on IANA to manage a namespace MUST provide guidelines for managing the namespace.

### 6.3 After-the-Fact Registrations
- IANA will not condone misuse of unassigned or reassigned values. Procedures MUST be applied. Values may only be reassigned with consent of original assignee and due consideration. In controversial cases, consultation with IESG is advised.

### 6.4 Reclaiming Assigned Values
- Reclaiming is tricky; consider contacting original party to determine usage-level. Reassignment should not normally be made without concurrence of original requester. IESG Approval is needed if reclaiming without consent. May be appropriate to solicit comments from user communities and possibly write an RFC.

## Section 7: Appeals
- Appeals of registration decisions follow normal IETF appeals process (Section 6.5 of [IETF-PROCESS]): directed to IESG, then IAB, etc.

## Section 8: Mailing Lists
- All IETF mailing lists associated with evaluating assignment requests are subject to BCP rules and IESG decisions.

## Section 9: Security Considerations
- Information updating registries must be authenticated and authorized. IANA updates registries per RFCs and IESG, and may accept clarifications from authors, WG chairs, Designated Experts.
- Security vulnerabilities may change over time; information may need to be attached to existing registrations.
- Analysis of security issues is required for protocols using IANA parameters; responsibility lies with IANA Considerations section of the registry.

## Section 10: Changes Relative to RFC 2434 (Informative – Condensed)
Major changes: reordering for clarity, term "IETF Consensus" changed to "IETF Review", added "RFC Required" policy, more explicit directions, "Specification Required" now implies Designated Expert, revised Section 3 for accountability, removed special appeals path, added sections on reclaiming values and after-the-fact registrations, added section on mailing list rules.

## Informative Annexes (Condensed)
- **Section 11 (Acknowledgments)**: Thanks to various reviewers.
- **Section 12 (References)**: Normative references: RFC 2119. Informative references: [ASSIGNED], [DHCP-OPTIONS], [DHCP-IANA], [EXPERIMENTATION], [IANA-CONSIDERATIONS], [IANA-MOU], [IETF-PROCESS], [IP], [IPSEC], [MIME-REG], [PROTOCOL-EXT], and many others as cited.
- **Authors' Addresses**: Thomas Narten (IBM), Harald Alvestrand (Google).
- **Full Copyright Statement**: Standard IETF Trust copyright; BCP 78 applies.
- **Intellectual Property**: Standard IPR disclosure.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Documents that create a new namespace and expect IANA to maintain it MUST provide clear instructions on registry name, required information, review process, format, and initial assignments. | MUST | Section 4.2 |
| R2 | When Designated Expert is used, the document MUST NOT name the expert. | MUST | Section 4.2 item 3 |
| R3 | Documents requesting assignment from existing namespace MUST clearly identify the namespace and cite the defining RFC. | MUST (implied) | Section 5.1 |
| R4 | IANA Considerations section MUST summarize all IANA actions. | MUST | Section 5.1 |
| R5 | Future RFCs that implicitly or explicitly rely on IANA to manage namespace MUST provide guidelines for managing the namespace. | MUST | Section 6.2 |
| R6 | IANA MUST NOT make assignments contrary to documented procedures without IESG approval (overriding procedures). | MUST (normative) | Section 5.3 |
| R7 | Designated Experts MUST respond in a timely fashion (normally within a week for simple requests). | MUST | Section 3.3 |
| R8 | IANA MUST raise recurring non-response from expert to IESG. | MUST | Section 3.3 |
| R9 | Reclaiming unused values without original requester's concurrence requires IESG Approval. | MUST (normative "needed") | Section 6.4 |
| R10 | In the absence of specific review criteria, a code point SHOULD be granted unless compelling reason to deny. | SHOULD | Section 3.3 |
| R11 | Use of the well-known policy terms (e.g., "First Come First Served") is RECOMMENDED. | RECOMMENDED | Section 4.1 |
| R12 | Documents with no IANA actions SHOULD include an IANA Considerations section stating "This document has no IANA actions." | SHOULD | Section 6.1 |
| R13 | IESG Approval for an assignment SHOULD be based on community consultation (call for comments). | SHOULD | Section 4.1 (IESG Approval guidelines) |