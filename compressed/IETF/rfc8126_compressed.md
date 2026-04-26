# RFC 8126: Guidelines for Writing an IANA Considerations Section in RFCs
**Source**: IETF (Internet Engineering Task Force) | **Version**: BCP 26 (obsoletes RFC 5226) | **Date**: June 2017 | **Type**: Best Current Practice
**Original**: https://www.rfc-editor.org/info/rfc8126

## Scope (Summary)
Defines a framework for documenting guidelines in the IANA Considerations section of RFCs to ensure clear, prudent management of protocol parameter registries. Covers creation/revision of registries, registration policies, designated experts, and miscellaneous issues like reclaiming values and closing registries.

## Normative References
- [RFC2026] Bradner, S., "The Internet Standards Process -- Revision 3", BCP 9, RFC 2026, October 1996.

## Definitions and Abbreviations
- **Namespace**: The range of possible values for a protocol field.
- **Assignment/Registration**: Binding a specific value to a particular purpose within a namespace, recorded in a **registry**.
- **IANA**: The Internet Assigned Numbers Authority (IFO/IPPSO) coordinating protocol parameter allocations.
- **Designated Expert**: An individual responsible for evaluating assignment requests and making recommendations to IANA.
- **Registration Policy**: The policy controlling how new assignments in a registry are accepted (see Section 4).
- **Change Controller**: Entity authorized to modify a registry definition or a registered value.
- **IFO**: IANA Functions Operator.
- **IPPSO**: IANA PROTOCOL PARAMETER SERVICES Operator.

## 1. Introduction
- Many protocols use extensibility points with constants (e.g., Protocol field in IP header [RFC791], MIME types [RFC6838]).
- IETF selects an IANA Functions Operator (IFO), referred to as "IANA".
- This document provides guidance for authors to ensure clear IANA Considerations that address registry operation issues.
- The IANA Considerations section should be a single place for clear instructions to IANA, not primary technical documentation. Technical details go in other sections.

### 1.1 Keep IANA Considerations for IANA
- The IANA Considerations section must clearly enumerate each requested IANA action, include full registry names, and provide clear references.
- IANA actions are normally phrased as requests ("IANA is asked to assign..."); the RFC Editor will change to past tense upon publication.

### 1.2 For Updated Information
- Additional clarification is maintained at <https://iana.org/help/protocol-registration>.
- Significant updates require updating BCP 26 (this document).

### 1.3 A Quick Checklist Upfront
- Put IANA information in the IANA Considerations section.
- Keep technical information in technical sections.
- IESG has authority to resolve issues; consult document shepherd or WG chair.

## 2. Creating and Revising Registries
- Defining a registry involves describing namespaces, initial assignments, and guidelines for future assignments.
- Consider structuring namespaces hierarchically to distribute coordination.

### 2.1 Organization of Registries
- All registries are anchored from `https://www.iana.org/protocols` in protocol category groups.
- Document authors must identify group for new registries and communicate grouping to IANA.

### 2.2 Documentation Requirements for Registries
Documents that create or modify a namespace must provide clear instructions including:
- **Registry name**: Full name (and abbreviation) that appears on IANA page, not easily confused with others. Must identify the parent group.
- **Required information for registrations**: What registrants must provide (e.g., value, reference, template).
- **Applicable registration policy**: See Section 4.
- **Size, format, syntax**: Data types, lengths, valid ranges, display format (decimal, hex), case sensitivity for strings. Non-ASCII characters must use Unicode (U+XXXX) convention.
- **Initial assignments and reservations**: List initial values, and ranges for "Private Use", "Reserved", "Unassigned".

- Example template provided (Section 2.2).
- IANA may keep contact information private upon request.

### 2.3 Specifying Change Control for a Registry
- Change control for IETF-stream registries defaults to IETF via IESG.
- Registries should clearly specify a change control policy and change controller.
- For values registered outside IETF stream, include a change controller for each value.

### 2.4 Revising Existing Registries
- Updates to registration process or registry format follow a process similar to creation: produce a document with detailed instructions.
- Normally processed with same document status as the creating document.
- IESG may approve straightforward changes (e.g., adding a status column) without a new document.

## 3. Registering New Values in an Existing Registry
### 3.1 Documentation Requirements for Registrations
- Documents must clearly identify the existing registry by exact name and URL, and cite the defining RFC.
- If multiple assignment policies apply (different ranges), specify the requested range.
- Provide all required information (see registry's reference document) and follow any special processes.
- **Use placeholders (e.g., "TBD1") for numeric values; IANA assigns final values. Avoid specifying final values to prevent collisions.
- Text-string values can be specified, but may use draft-specific values for early implementations.
- Include a summary table of additions/changes in the same format as the registry.

### 3.2 Updating Existing Registrations
- Registrations may need updates (e.g., contact info, security issues). The defining document must state who is responsible for maintenance.
- Possible mechanisms: registrants/change controllers update with same review; attachment of comments; IESG/designated expert authority to change registrant.

### 3.3 Overriding Registration Procedures
- The IESG may override registration procedures and approve assignments on a case-by-case basis when documented procedures are insufficient or too stringent.
- This authority is not meant to circumvent proper documentation; it indicates the registry procedures should be updated.
- IANA may ask IESG for advice when policies are unclear or requests appear abusive.

### 3.4 Early Allocations
- Early allocation may be done before document approval using mechanisms in [RFC7120]. Not necessary to explicitly mark registry as allowing early allocations.

## 4. Choosing a Registration Policy and Well-Known Policies
- Registration policy controls how new assignments are accepted.
- Even with unlimited space, minimal review is often desirable to prevent hoarding, ensure sanity, and protect interoperability/security.
- Choose the least strict policy that suits needs; justify policies stricter than Expert Review or Specification Required.
- Well-known policies (from least to most strict):
  1. Private Use
  2. Experimental Use
  3. Hierarchical Allocation
  4. First Come First Served
  5. Expert Review
  6. Specification Required
  7. RFC Required
  8. IETF Review
  9. Standards Action
  10. IESG Approval
- Namespaces can be partitioned into ranges with different policies.

### 4.1 Private Use
- For private/local use; no IANA recording; no attempt to prevent conflicting uses.
- Examples: Site-specific DHCP options [RFC2939], Fibre Channel Port Type Registry [RFC4044], TLS ClientCertificateType Identifiers 224-255 [RFC5246].

### 4.2 Experimental Use
- For experimentation as per [RFC3692]; no IANA recording unless explicitly allowed.
- Must clarify restrictions on experimental scope (e.g., open Internet vs. closed environments).
- Example: Experimental Values in IPv4, IPv6, etc. [RFC4727].

### 4.3 Hierarchical Allocation
- Delegated administrators control part of the namespace; IANA allocates higher-level values using another policy.
- Examples: DNS names [RFC1591], Object Identifiers (ITU-T X.208), URN namespaces [RFC8141].

### 4.4 First Come First Served
- Assignments made without substantive review; only ensure well-formedness and no duplication.
- Must include point of contact and brief description.
- Registry should include a change controller field for each entry.
- Changes must retain compatibility; working groups must ensure wire compatibility.
- Examples: SASL mechanism names [RFC4422], LDAP Protocol Mechanisms [RFC4520].

### 4.5 Expert Review
- Requires review and approval by a designated expert (see Section 5).
- The registry definition must provide clear review guidance to the expert.
- Registry should include change controller field.
- Examples: EAP Method Types [RFC3748], URI schemes [RFC7595].

### 4.6 Specification Required
- Same as Expert Review, plus values must be documented in a permanent, readily available public specification sufficient for interoperability.
- The designated expert evaluates the specification's stability, clarity, and technical soundness.
- Use only the term "Specification Required"; not "Expert Review with Specification Required".
- Examples: Diffserv TE Bandwidth Constraints Model [RFC4124], TLS ClientCertificateType 64-223 [RFC5246].

### 4.7 RFC Required
- Registration must be published in an RFC (any stream: IETF, IRTF, IAB, Independent).
- Any type of RFC is sufficient unless otherwise specified.
- Examples: DNSSEC Algorithm Numbers [RFC6014], Media Control Channel Framework [RFC6230], DANE TLSA [RFC6698].

### 4.8 IETF Review
- Values assigned only through RFCs in the IETF Stream (AD-Sponsored or WG documents), with IETF Last Call and IESG approval.
- Any type of RFC (Standards Track, BCP, Informational, Experimental, Historic) unless otherwise specified.
- Examples: IPSECKEY Algorithm Types [RFC4025], TLS Extension Types [RFC5246].

### 4.9 Standards Action
- Values assigned only through Standards Track or BCP RFCs in the IETF Stream.
- Examples: BGP message types [RFC4271], Mobile Node Identifier option types [RFC4283], DCCP Packet Types [RFC4340].

### 4.10 IESG Approval
- New assignments approved by IESG; no requirement for RFC, but IESG may request supporting materials.
- Intended as fall-back, not common case; should not circumvent public review.
- Examples: IPv4 Multicast address assignments [RFC5771], IPv4 IGMP Type and Code [RFC3228].

### 4.11 Using the Well-Known Registration Policies
- Encouraged due to community experience; creation of new policies requires justification.
- It's acceptable to cite policies and add additional review guidelines.
- When policies stricter than Expert Review/Specification Required are proposed, the IESG should ask for justification.
- Document developers should document rationale for policy selection.

### 4.12 Using Multiple Policies in Combination
- Example: "RFC Required" or "IETF Review" for IETF documents, "Specification Required" for external SDO registrations.
- Common combinations: {Standards Action, IETF Review, RFC Required} with {Specification Required, Expert Review}.

### 4.13 Provisional Registrations
- Some registries allow provisional registrations (e.g., URI Schemes [RFC7595], Email Header Fields [RFC3864]) – easier to create, change, reassign, or remove.
- Criteria for promotion to permanent are stricter.
- Suitable for registries without practical limits on codepoints.

## 5. Designated Experts
### 5.1 The Motivation for Designated Experts
- IANA relies on designated experts to evaluate assignment requests when mailing list discussion does not yield clear consensus.
- Experts provide recommendations to IANA; registrants generally do not work directly with experts.

### 5.2 The Role of the Designated Expert
- Responsible for coordinating review, which may include consultation with experts, mailing list discussion, etc.
- Must follow documented review criteria; otherwise, follow generally accepted norms (Section 5.3). Experts are not gatekeepers unless specified.
- Multiple experts may serve; if deadlock, the designating body resolves.
- Conflicts of interest: recuse. If all experts are conflicted, request a temporary expert.
- Designated expert mechanism defined for IETF stream only.

### 5.2.1 Managing Designated Experts in the IETF
- Appointed by IESG, normally on recommendation of relevant Area Director.
- May be appointed at document approval or when first registration request arrives.
- IESG may remove any designated expert at its discretion.
- Appeals follow [RFC2026] Section 6.5.1.

### 5.3 Designated Expert Reviews
- Must respond in a timely fashion (normally within a week for simple requests, a few weeks for complex ones). Unreasonable delays must be reported to IESG.
- Expert acts as shepherd for the request; can enlist help.
- Must defend decisions to community; should have support of other experts for controversial rejections.
- Reasons for denial: scarcity of code points, insufficient documentation, inconsistency with protocol architecture, harm to deployed systems, conflict with IETF development.
- Documents must not name designated experts; suggested names go to Area Director via shepherd writeup.
- If review on a public mailing list is required, its address must be specified.

### 5.4 Expert Reviews and the Document Lifecycle
- Review should be done around IETF Last Call; rereview if documentation changes substantially.
- IESG and AD must be alert to post-review changes that would affect the registration.
- For Standards Track registrations requiring expert review, the expert review must be timely and submitted before IESG evaluation. The IESG should not hold the document for late review; expert review does not override IETF consensus.

## 6. Well-Known Registration Status Terminology
- **Private Use**: Private use only (not assigned).
- **Experimental**: For general experimental use [RFC3692]; specific assignments not recorded by IANA.
- **Unassigned**: Available for assignment via documented procedures.
- **Reserved**: Not assigned nor available; held for special uses; may be released by change controller.
- **Known Unregistered Use**: Known to be in use without proper definition; warning.

## 7. Documentation References in IANA Registries
- References should point to the document containing the definition and explanation, not merely the registration document.
- Include section numbers when useful.
- For new registries, reference should provide information about the registry itself (purpose, process, guidelines).

## 8. What to Do in "bis" Documents
- When an RFC obsoletes a previous edition, registration references should be updated to point to the current (not obsolete) documentation.
- If registered items are moved to other documents, update references accordingly. Leave references for obsolete items as they are if no longer in current use.
- Be clear in instructions about which references to update.

## 9. Miscellaneous Issues
### 9.1 When There Are No IANA Actions
- Include an IANA Considerations section stating: "This document has no IANA actions." IANA prefers to keep this section in the publication.

### 9.2 Namespaces Lacking Documented Guidance
- For existing RFCs without precise policies, IANA works with IESG to decide appropriate policy.
- All future RFCs relying on IANA to administer namespaces must provide guidelines.

### 9.3 After-the-Fact Registrations
- Unassigned values in use or assigned values used for different purposes must be handled via proper procedures; values may be reassigned only with consent of original assignee and due consideration of impact.

### 9.4 Reclaiming Assigned Values
- Attempt to contact original party to determine deployment extent.
- Reassignments should not normally be made without concurrence of original requester; IESG Approval needed if hostile reclamation.
- Consider differentiating revocation, release, transfer.

### 9.5 Contact Person vs Assignee or Owner
- Registries should include an "Assignee" or "Change Controller" field to clarify ownership, especially for non-RFC-based registries (First Come First Served, Expert Review, Specification Required). Alternatively, use organizational roles.

### 9.6 Closing or Obsoleting a Registry/Registrations
- Closing a registry: no further registrations accepted; existing info remains valid.
- A closed registry can be marked "obsolete". Specific entries can be "obsolete" or "deprecated".
- Changes subject to normal change controls.

## 10. Appeals
- Initial appeal to IESG, followed by appeal to IAB, per [RFC2026], Section 6.5.

## 11. Mailing Lists
- All IETF mailing lists used for evaluating assignment requests are subject to current best practices and IESG decisions.

## 12. Security Considerations
- IANA updates registries according to published RFCs and IESG instructions. Authentication and authorization of updates are required.
- Security vulnerabilities may change over time; information must be attached to registrations.
- Registration policies must consider security implications.
- Analysis of security issues is required for protocols using registered parameters [BCP72].

## 13. IANA Considerations
- Sitewide, IANA has replaced references to RFC 5226 with references to this document.

## 14. Changes Relative to Earlier Editions of BCP 26
### 14.1 2016: Changes relative to RFC 5226
- Removed RFC 2119 key words; added sections 1.1, 1.2, 2.1, 2.3, 3.4, 4.12, 5.4, 7, 8, 9.5, 9.6; reorganized; clarifications on registry identification, Unassigned vs Reserved, expert review guidance, Specification Required naming.

### 14.2 2008: Changes relative to RFC 2434
- Major reordering; term change "IETF Consensus" to "IETF Review"; added "RFC Required"; "Specification Required" now implies designated expert; section on provisional registrations; accountability of expert reviewers; normal appeals path; reclaiming values; after-the-fact registrations; mailing list rules.

## Requirements Summary
This BCP does not contain protocol-level requirements but provides normative instructions for document authors. Key "shall" and "must" statements are extracted:

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Documents that create or modify a namespace must provide clear instructions on details of the namespace in the IANA Considerations section or referenced from it. | must | Section 2.2 |
| R2 | When creating a registry, the instructions must include: registry name, required info for registrations, applicable registration policy, size/format/syntax, initial assignments/reservations. | must | Section 2.2 |
| R3 | Documents requesting assignment in an existing registry must clearly identify the registry by exact name (and optionally URL) and cite the defining RFC. | shall | Section 3.1 |
| R4 | Use placeholders like "TBD1" for numeric values; do not specify final values in drafts. | must | Section 3.1 |
| R5 | The IESG may override registration procedures and approve assignments on a case-by-case basis. | may (IESG) | Section 3.3 |
| R6 | Policy choices stricter than Expert Review or Specification Required must be justified. | must (for document reviewers) | Section 4 |
| R7 | For Expert Review policy, the registry definition must provide clear review criteria to the designated expert. | must | Section 4.5, 5.3 |
| R8 | For Specification Required policy, the same as Expert Review plus requirement for permanent, readily available public specification. | must | Section 4.6 |
| R9 | Documents must not name designated experts; suggested names relayed to Area Director. | must | Section 5.3 |
| R10 | All future RFCs relying on IANA to administer namespaces must provide guidelines for administration. | must | Section 9.2 |

## Informative Annexes (Condensed)
- **Annex (Appendix) - Changes and Acknowledgments**: Summarizes changes from previous editions and acknowledges contributors. Not normative.
- **Annex (References)**: Lists normative and informative references. Normative reference is [RFC2026]. Informative references include many RFCs cited throughout.
- **Annex (Authors' Addresses)**: Contact information for Michelle Cotton, Barry Leiba, Thomas Narten.