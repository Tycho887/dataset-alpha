# RFC 2028: The Organizations Involved in the IETF Standards Process
**Source**: IETF | **Version**: BCP 11 | **Date**: October 1996 | **Type**: Best Current Practice (Normative)
**Original**: https://www.rfc-editor.org/rfc/rfc2028

## Scope (Summary)
This document describes the individuals and organizations involved in the IETF, including the RFC Editor, Working Group Chairs, Document Editors, IESG, IAB, IANA, and the relationship between the IETF and the Internet Society (ISOC). It references the governing procedures in RFC 2026 and related documents.

## Normative References
- [B] Bradner, S., "The Internet Standards Process -- Revision 3", RFC 2026, October 1996.
- [A] Huizer, E. and D. Crocker, "IETF Working Group Guidelines and Procedures", RFC 1603, March 1994.
- [C] ISOC By Laws (gopher://info.isoc.org/00/isoc/basic_docs/bylaws.txt).
- [D] Huitema, C. and the IAB, "Charter of the Internet Architecture Board (IAB)", RFC 1601, March 1994.
- [E] Galvin, J. (Ed.), "IAB and IESG Selection, Confirmation, and Recall Process", RFC 2027, October 1996.
- [F] IANA Charter (Work in Progress).
- [G] RFC Editor Charter (Work in Progress).
- [H] IRTF Charter, RFC 2014, October 1996.

## Definitions and Abbreviations
- **RFC Editor**: Individual(s) or organization(s) responsible for the RFC publication series, upholding technical and editorial standards.
- **Working Group Chair**: Head of an IETF Working Group, responsible for directing activities, presiding over meetings, and serving as formal point of contact with the IESG.
- **Document Editor**: Person(s) designated by a Working Group to ensure that a document accurately reflects group decisions.
- **IETF**: Internet Engineering Task Force – open international community of network designers, operators, vendors, and researchers; principal body for developing Internet Standards.
- **IESG**: Internet Engineering Steering Group – manages IETF technical activities, administers the standards process, approves new Working Groups and final specifications.
- **IAB**: Internet Architecture Board – provides architectural oversight, appoints IETF chair, approves IESG candidates, reviews Working Group charters, acts as appeal board.
- **IANA**: Internet Assigned Numbers Authority – assigns protocol parameters (version numbers, port numbers, etc.), publishes "Assigned Numbers" RFCs, and establishes assignment policies.
- **IRTF**: Internet Research Task Force – investigates topics too uncertain or advanced for standardization; not directly involved in standards process.
- **ISOC**: Internet Society – international organization; Board of Trustees ratifies procedures and rules of the Internet standards process.

## 1. Documents Controlling the Process

### 1.1 The IETF Standards Process
- The standardization process is defined in RFC 2026 [B], which specifies stages, requirements for progression, document types, and intellectual property rights and copyright issues.

## 2. Key Individuals in the Process

### 2.1 The Request for Comments Editor
- **RFC-EDITOR-ROLE**: The RFC Editor manages the RFC publication series, upholds high technical and editorial standards, and is selected per the RFC Editor charter [G].

### 2.2 The Working Group Chair
- **WG-CHAIR-RESP**: The Working Group Chair is the formal point of contact between the WG and the IESG (via the Area Director). The chair shall direct group activities, preside over meetings, and ensure commitments to the standards process are met.
- **Selection and responsibilities** are detailed in [A].

### 2.3 The Document Editor
- **DOC-EDITOR-ROLE**: The Document Editor ensures that document contents accurately reflect WG decisions. By general practice, the WG Chair and Document Editor shall be different individuals to ensure consensus and process compliance.

## 3. Key Organizations in the Process

### 3.1 Internet Engineering Task Force (IETF)
- **IETF-NATURE**: The IETF is an open international community concerned with evolution of the Internet architecture and smooth operation; it is the principal body developing new Internet Standard specifications.

### 3.2 IETF Working Groups
- **WG-MEMBERSHIP**: Membership in IETF and Working Groups is established solely by individual participation, not by formal organizational representation.
- **WG-PARTICIPATION**: Anyone with time and interest is entitled and urged to participate actively; active participation is possible via email or video conferencing.
- **IPR-DISCLOSURE**: Participants must disclose to the WG Chair any relevant current or pending intellectual property rights that are reasonably and personally known to them when discussing a specific technology.
- **WG-FORMATION**: New Working Groups are established by explicit charter; formation and operation guidelines are in [A].
- **WG-MANAGEMENT**: A WG is managed by one or more chairs (see 2.2) and may include document editors (see 2.3).
- **WG-COOPERATION**: Working Groups display a spirit of cooperation and technical maturity; participants recognize that cooperative development benefits the Internet community.

### 3.3 IETF Secretariat
- **SEC-ROLE**: The IETF Executive Director and staff perform administrative functions. The Executive Director is the formal point of contact for all aspects of the Internet standards process and shall maintain the formal public record [B].

### 3.4 Internet Society (ISOC)
- **ISOC-ROLE**: ISOC is an international organization with individual and organizational members; Internet standardization is an organized activity of ISOC. The Board of Trustees ratifies the procedures and rules of the Internet standards process [B].
- **Governance** is described in the ISOC By Laws [C].

### 3.5 Internet Engineering Steering Group (IESG)
- **IESG-ROLE**: The IESG manages IETF technical activities, administers the standards process [B], approves new Working Groups, and final approval of specifications as Internet Standards.
- **IESG-COMPOSITION**: Composed of IETF Area Directors and the IETF Chair (who chairs the IESG). Members are nominated by the Nomcom and approved by the IAB [E].
- Other matters are described in the IESG charter (still under development at time of writing).

### 3.6 Internet Architecture Board (IAB)
- **IAB-ROLE**: Chartered by ISOC Trustees to provide architectural oversight; appoints the IETF Chair, approves IESG candidates from the Nomcom, reviews and approves charters of new Working Groups, serves as appeal board for standards process complaints [B], and advises IETF, ISOC, and ISOC Board on technical, architectural, procedural, and policy matters.
- **IAB-MEMBERSHIP**: Members are nominated by Nomcom and approved by ISOC board; includes Nomcom-selected members and the IETF Chair as ex-officio member. Procedures in [E] and charter in [D].

### 3.7 Internet Assigned Numbers Authority (IANA)
- **IANA-ROLE**: Responsible for assigning protocol parameters; publishes "Assigned Numbers" RFCs; establishes policies for DNS and Internet Address assignment. Functions performed per IANA charter [F].

### 3.8 Internet Research Task Force (IRTF)
- **IRTF-ROLE**: Not directly involved in standards process; investigates topics too uncertain for standardization. Specifications stable enough are processed through IETF. Overseen by IRSG; details in [H].

## 4. Security Considerations
- Security is not addressed in this memo.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| RFC-EDITOR-ROLE | The RFC Editor shall manage the RFC publication series and uphold high technical and editorial standards. | shall | Section 2.1, [B] |
| WG-CHAIR-RESP | The Working Group Chair shall be the formal point of contact between the WG and the IESG, direct group activities, preside over meetings, and ensure commitments are met. | shall | Section 2.2 |
| DOC-EDITOR-ROLE | The Document Editor shall ensure document contents accurately reflect WG decisions. | shall | Section 2.3 |
| IPR-DISCLOSURE | Participants in IETF and its Working Groups must disclose to the WG Chair any relevant current or pending intellectual property rights that are reasonably and personally known to them when discussing a specific technology. | must | Section 3.2 |
| SEC-ROLE | The IETF Executive Director shall maintain the formal public record of the Internet standards process. | shall | Section 3.3 |
| WG-MEMBERSHIP | Membership in IETF and Working Groups is established solely by individual participation, not by formal representatives of organizations. | must | Section 3.2 |
| IESG-ROLE | The IESG shall manage IETF technical activities, administer the standards process, approve new Working Groups, and final approval of specifications as Internet Standards. | shall | Section 3.5 |
| IAB-ROLE | The IAB shall provide architectural oversight, appoint IETF Chair, approve IESG candidates, review and approve new Working Group charters, and serve as appeal board. | shall | Section 3.6 |
| IANA-ROLE | The IANA shall assign protocol parameters and publish "Assigned Numbers" RFCs. | shall | Section 3.7 |
| WG-FORMATION | New Working Groups must be established by explicit charter per [A]. | must | Section 3.2 |

## Informative Annexes (Condensed)
- **Appendix A – Contact Information**: Lists contact email and URLs for IETF, IESG, IAB, RFC Editor, and IANA. (Provided for reference; not normative.)