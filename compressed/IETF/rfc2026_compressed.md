# RFC 2026: The Internet Standards Process -- Revision 3
**Source**: IETF (Network Working Group) | **Version**: Revision 3 | **Date**: October 1996 | **Type**: Best Current Practice (Normative)  
**Original**: https://tools.ietf.org/html/rfc2026

## Scope (Summary)
This document specifies the process used by the Internet community for the standardization of protocols and procedures. It defines the stages in the standardization process, the requirements for moving between stages, and the types of documents used. It also addresses intellectual property rights and copyright issues associated with the standards process.

## Normative References
- [1] Postel, J., "Internet Official Protocol Standards", STD 1, March 1996.
- [2] ANSI, "Coded Character Set -- 7-Bit American Standard Code for Information Interchange", ANSI X3.4-1986.
- [3] Reynolds, J., and J. Postel, "Assigned Numbers", STD 2, October 1994.
- [4] Postel, J., "Introduction to the STD Notes", RFC 1311, March 1992.
- [5] Postel, J., "Instructions to RFC Authors", RFC 1543, October 1993.
- [6] Huitema, C., J. Postel, and S. Crocker, "Not All RFCs are Standards", RFC 1796, April 1995.
- BCP-11 (referenced in Section 10.4 for IPR procedures)

## Definitions and Abbreviations
- **Internet Engineering Steering Group (IESG)** – Group comprising IETF Area Directors and IETF Chair; responsible for management of IETF and standards approval.
- **Internet Architecture Board (IAB)** – Appointed group assisting management of IETF standards process.
- **Working Group** – Group chartered by IESG and IAB to work on specific specifications.
- **Last-Call** – Public comment period to gauge consensus on a proposed standards action.
- **Interoperable** – For this document, able to interoperate over a data communications path.
- **Technical Specification (TS)** – Description of a protocol, service, procedure, convention, or format.
- **Applicability Statement (AS)** – Specification of how and under what circumstances one or more TSs are applied to support a particular Internet capability.
- **Proposed Standard** – Entry-level maturity for standards track; specification is stable, has community review.
- **Draft Standard** – Specification with at least two independent, interoperable implementations and successful operational experience.
- **Internet Standard** – Specification with significant implementation and operational experience; assigned STD number.
- **Experimental** – Designation for research/development specifications.
- **Informational** – Designation for general information, not representing community consensus.
- **Historic** – Specification that is obsolete or superseded.
- **Best Current Practice (BCP)** – Subseries of RFCs that standardize community practices, principles, or IETF process functions.
- **Internet-Draft** – Preliminary draft version of a specification for informal review; no formal status.

## 1. Introduction
### 1.1 Internet Standards
- Internet Standards are specifications that are stable, well-understood, technically competent, have multiple independent interoperable implementations, significant operational experience, public support, and are useful in the Internet.
- The process applies to all protocols, procedures, and conventions used in the Internet, including those developed by non-Internet organizations (for application in the Internet context).

### 1.2 The Internet Standards Process
- Goals: technical excellence, prior implementation and testing, clear documentation, openness and fairness, timeliness.
- Procedures are fair, open, objective, reflect proven practice, and are flexible.
- A candidate specification **must** be implemented and tested by multiple independent parties before adoption as a Standard.
- The process balances timeliness with technical excellence and thorough testing.

### 1.3 Organization of This Document
- Sections 2–15 and Appendix A are described; see original for detailed table of contents.

## 2. Internet Standards-Related Publications
### 2.1 Requests for Comments (RFCs)
- Each distinct version of a standards-related specification is published as an RFC.
- RFC series is the official publication channel for Internet standards and other IESG, IAB, and community publications.
- The RFC Editor is responsible for publication under IAB direction.
- Every RFC is available in ASCII text; some in other formats.
- For standards-track specifications: **the ASCII text version is the definitive reference** and **must** be a complete and accurate specification including all necessary diagrams.
- RFCs that become Internet Standards are assigned an STD number (e.g., STD 1) but retain their RFC number.
- RFCs that become BCPs are assigned a BCP number.
- Non-standards track specifications (Experimental, Informational) may be published by the RFC Editor in consultation with the IESG.

### 2.2 Internet-Drafts
- Draft versions of specifications are made available in the Internet-Drafts directory for informal review.
- An Internet-Draft that remains unchanged for more than six months without IESG recommendation for RFC publication is removed.
- An Internet-Draft has no formal status, is subject to change or removal at any time.
- **Under no circumstances shall an Internet-Draft be referenced by any paper, report, or Request-for-Proposal, nor shall a vendor claim compliance with an Internet-Draft.**
- It is acceptable to reference a standards-track specification expected to be published as an RFC using the phrase "Work in Progress" without referencing an Internet-Draft.

## 3. Internet Standard Specifications
### 3.1 Technical Specification (TS)
- A TS **shall** include a statement of its scope and general intent for use (domain of applicability).
- A TS does not specify requirements for its use; that is defined by an Applicability Statement.

### 3.2 Applicability Statement (AS)
- An AS specifies how and under what circumstances one or more TSs are applied to support a particular Internet capability.
- An AS identifies relevant TSs and the specific way they are combined; it may specify particular values, ranges, or subfunctions.
- An AS specifies whether use is **required**, **recommended**, or **elective** (see 3.3).
- An AS may not have a higher maturity level than any standards-track TS it references.
  - Example: A TS at Draft Standard level may be referenced by an AS at Proposed Standard or Draft Standard, but not at Standard level.

### 3.3 Requirement Levels
An AS shall apply one of the following requirement levels to each referenced TS:
- **(a) Required**: Implementation is required for minimal conformance.
- **(b) Recommended**: Implementation is not required for minimal conformance, but experience/general wisdom suggest desirability; vendors **should** include it unless justified by special circumstances.
- **(c) Elective**: Implementation is optional within the domain of applicability.
- Additionally for non-standards-track or retired TSs:
  - **(d) Limited Use**: Appropriate only in limited or unique circumstances (e.g., Experimental).
  - **(e) Not Recommended**: Inappropriate for general use (e.g., Historic).

## 4. The Internet Standards Track
### 4.1 Standards Track Maturity Levels
#### 4.1.1 Proposed Standard
- Entry-level maturity; requires IESG action to move specification onto standards track.
- A Proposed Standard specification is generally stable, well-understood, has community review, and is considered valuable.
- Usually, neither implementation nor operational experience is required, but is highly desirable.
- The IESG **may require** implementation and/or operational experience prior to granting Proposed Standard status for specifications that materially affect core Internet protocols or that have significant operational impact.
- A Proposed Standard should have no known technical omissions with respect to requirements; IESG may waive this if useful and timely.
- Implementors **should** treat Proposed Standards as immature; deploying in disruption-sensitive environments is **not recommended**.

#### 4.1.2 Draft Standard
- At least two independent and interoperable implementations from different code bases required, plus sufficient successful operational experience.
- "Interoperable" means functionally equivalent or interchangeable components. If patented technology is required, implementations must result from separate exercise of licensing process.
- All options and features must be demonstrated in at least two interoperable implementations; otherwise those options must be removed.
- The Working Group chair **must** document specific implementations and testing, including support of each option and feature; submitted to Area Director.
- Draft Standard must be well-understood and stable; may still require more field experience.
- A Draft Standard is normally considered final; changes likely only to solve specific problems. It is reasonable for vendors to deploy implementations in disruption-sensitive environments.

#### 4.1.3 Internet Standard
- Significant implementation and successful operational experience obtained.
- Characterized by high technical maturity and belief of significant benefit to Internet community.
- Assigned STD number.

### 4.2 Non-Standards Track Maturity Levels
#### 4.2.1 Experimental
- Typically denotes research/development effort; published for general information and archival record.
- May be output of IRTF Research Group, IETF WG, or individual contribution.

#### 4.2.2 Informational
- Published for general information; does not represent community consensus or recommendation.
- Specifications prepared outside the Internet community may be published as Informational RFCs with permission of owner and concurrence of RFC Editor.

#### 4.2.3 Procedures for Experimental and Informational RFCs
- Unless result of IETF WG action, documents for Experimental/Informational publication should be submitted directly to RFC Editor.
- RFC Editor will publish as Internet-Drafts (if not already), labeled/grouped to be easily recognizable; waits two weeks for comments.
- RFC Editor may refuse publication if unrelated to Internet activity or below technical/editorial standard.
- RFC Editor shall refer to IESG any document that may be related to IETF work; IESG shall review and recommend.
- If IESG recommends bringing document into IETF but author declines, or if document conflicts with established IETF effort, it may still be published with appropriate disclaimer inserted by IESG.
- Experimental/Informational RFCs proposed by IETF WGs go through IESG review per section 6.1.1.

#### 4.2.4 Historic
- Specification that is superseded or considered obsolete is assigned Historic level.
- Norm: Standards track specifications normally **must not** depend on other standards track specifications at lower maturity level or on non-standards track specifications other than referenced specifications from other standards bodies.

## 5. Best Current Practice (BCP) RFCs
- BCP subseries standardizes practices, principles, and IETF process functions.
- Same basic procedures as standards track documents, but without the three-stage maturity model.
- BCP approval process is similar to Proposed Standard: submitted to IESG for review, including a Last-Call on IETF Announce mailing list. After IESG approval, document is published.
- BCPs require particular care because they are arrived at more quickly than standards.
- A specification approved as a BCP is assigned a BCP number while retaining its RFC number.

### 5.1 BCP Review Process
- BCPs are not suited to phased roll-in; they are instantiated fully upon approval.
- Process: submit per section 6.1.1, IESG review, Last-Call, IESG approval.
- Appeals per section 6.5.

## 6. The Internet Standards Process
### 6.1 Standards Actions
- A standards action (entering, advancing, or removing from standards track) **must** be approved by the IESG.

#### 6.1.1 Initiation of Action
- A specification intended to enter or advance **shall** first be posted as an Internet-Draft (unless unchanged since RFC publication) for at least two weeks.
- Action is initiated by recommendation from responsible IETF Working Group to Area Director (copied to Secretariat) or by individual to IESG.

#### 6.1.2 IESG Review and Approval
- IESG **shall** determine if specification satisfies applicable criteria (sections 4.1, 4.2) and that technical quality and clarity are appropriate for the maturity level.
- IESG may commission independent technical review.
- IESG will send a Last-Call notification to IETF Announce mailing list for final community review.
- Last-Call period shall be no shorter than two weeks (four weeks if not initiated by an IETF WG). IESG may extend.
- IESG is not bound by the recommended action; it may decide a different category.
- If IESG changes category to a higher level than the Last-Call, a new Last-Call **shall** be issued.
- In case of significant controversy on a Last-Call for a specification not from an IETF WG, IESG may recommend formation of a new WG.
- IESG shall make final determination in a timely fashion after Last-Call expiration and notify IETF.

#### 6.1.3 Publication
- If approved, notification sent to RFC Editor and copied to IETF with instructions to publish. Specification is removed from Internet-Drafts directory.
- An official summary of standards actions shall appear in each issue of the Internet Society's newsletter (publication of record).
- RFC Editor shall periodically publish "Internet Official Protocol Standards" RFC summarizing status of all Internet protocol and service specifications.

### 6.2 Advancing in the Standards Track
- Procedure from section 6.1 is followed for each advancement.
- Specification shall remain at Proposed Standard for at least six (6) months.
- Specification shall remain at Draft Standard for at least four (4) months, or until at least one IETF meeting has occurred, whichever comes later.
- Minimum periods measured from date of RFC publication or, if no publication, date of announcement of IESG approval.
- If specification is significantly revised, IESG may require more experience or treat as new document.
- Change of status results in republication as an RFC, except if no changes at all.
- If a standards-track specification has not reached Internet Standard and remains at same level for 24 months (and every 12 months thereafter), IESG shall review viability and usefulness. IESG shall approve termination or continuation and decide to maintain or move to Historic. Decision communicated to IETF via IETF Announce.

### 6.3 Revising a Standard
- A new version of an established Internet Standard must progress through the full standardization process as if a completely new specification.
- Once new version reaches Standard, it will usually replace the previous (moved to Historic). In some cases both may remain; relationship must be explicitly stated.

### 6.4 Retiring a Standard
- IESG shall approve change of status to Historic for an existing standard that should be retired.
- Recommendation requires Last-Call and notification per normal standards action.
- Request can originate from Working Group, Area Director, or other interested party.

### 6.5 Conflict Resolution and Appeals
#### 6.5.1 Working Group Disputes
- An individual may disagree with WG recommendation based on (a) views not adequately considered, or (b) incorrect technical choice.
- Disagreeing party shall first discuss with WG chair(s).
- If unresolved, any party may bring to Area Director(s) for resolution.
- If still unresolved, any party may appeal to IESG.
- If still unresolved, any party may appeal to IAB.
- IAB decision is final on both procedural and technical merit.

#### 6.5.2 Process Failures
- Individual disagreeing with IESG action shall first discuss with IESG Chair. If not satisfied, IESG as a whole re-examines. IESG shall issue report to IETF.
- If not satisfied, appeal to IAB. IAB reviews and reports outcome.
- IAB may annul IESG decision; situation returns to before IESG decision. IAB may recommend action but cannot pre-empt IESG role.
- IAB decision is final on whether standards procedures were followed.

#### 6.5.3 Questions of Applicable Procedure
- Further recourse only if procedures themselves are claimed inadequate or insufficient. Claim may be made to Internet Society Board of Trustees.
- President of Internet Society shall acknowledge appeal within two weeks and advise expected duration.
- Trustees review and report to IETF; decision is final.

#### 6.5.4 Appeals Procedure
- All appeals must include detailed and specific description of facts.
- Must be initiated within two months of public knowledge of action/decision.
- Decision-making individuals/bodies have discretion to define specific procedures.
- Decision must be accomplished within a reasonable time (not fixed maximum; process prioritizes consensus).

## 7. External Standards and Specifications
### 7.1 Use of External Specifications
- The Internet community will not standardize a specification that is simply an "Internet version" of an existing external specification unless explicit cooperative arrangement exists.

#### 7.1.1 Incorporation of an Open Standard
- An Internet Standard TS or AS may incorporate an open external standard by reference. The referenced specification should be available online when possible.

#### 7.1.2 Incorporation of Other Specifications
- Proprietary specifications may be incorporated by reference if proprietor meets section 10 requirements. If not widely available, IESG may request publication as Informational RFC.
- IESG generally should not favor a particular proprietary specification over technically equivalent competing specifications by making it "required" or "recommended".

#### 7.1.3 Assumption
- IETF Working Group may start from an external specification and develop it into an Internet specification if (1) provided in compliance with section 10, and (2) change control has been conveyed to IETF by original developer for the specification or derived works.

## 8. Notices and Record Keeping
- Each organization involved (IETF, IESG, IAB, WGs, ISOC Board) shall publicly announce and maintain a publicly accessible record of every activity that represents prosecution of the Internet Standards Process.
- For meetings, announcements **shall** be by email to IETF Announce mailing list, sufficiently far in advance.
- Announcement shall contain (or point to) all information necessary to support participation.
- Formal record shall include at least: charter, complete and accurate minutes, archives of WG email lists, and all written contributions.
- Formal record maintained by IETF Secretariat; each WG must maintain its own email list archive and ensure all traffic captured; WG chair responsible for providing minutes to Secretariat.
- Internet-Drafts removed from directories shall be archived by Secretariat only for historical record and are not retrievable except in special circumstances.

## 9. Varying the Process
- The variance procedure allows one-time exceptions to some requirements.

### 9.1 The Variance Procedure
- Upon recommendation of responsible IETF WG (or ad hoc committee), IESG may enter or advance a specification even if some requirements are not met.
- IESG **may** approve variance only if it first determines that likely benefits outweigh costs. IESG shall at least consider: (a) technical merit, (b) possibility of achieving goals without variance, (c) alternatives, (d) collateral and precedential effects, (e) ability to craft narrow variance.
- Proposed variance must detail the problem, precise provision causing need, and results of IESG considerations.
- Proposed variance shall be issued as an Internet Draft.
- IESG shall issue an extended Last-Call of no less than 4 weeks.
- After Last-Call, IESG makes final determination and notifies IETF.
- If approved, forwarded to RFC Editor for publication as a BCP.
- Permanent changes to this document shall be accomplished through normal BCP process.
- Appeals process (section 6.5) applies.

### 9.2 Exclusions
- No use of this procedure may lower any specified delays, nor exempt from requirements of openness, fairness, consensus, or proper record keeping.
- The following sections **must not** be subject of a variance: 5.1, 6.1, 6.1.1 (first paragraph), 6.1.2, 6.3 (first sentence), 6.5, and 9.

## 10. Intellectual Property Rights
### 10.1 General Policy
- Intention is to benefit the Internet community and public while respecting legitimate rights of others.

### 10.2 Confidentiality Obligations
- No contribution subject to any requirement of confidentiality or restriction on dissemination may be considered in any part of the Internet Standards Process.
- There must be no assumption of confidentiality obligation with respect to any contribution.

### 10.3 Rights and Permissions
#### 10.3.1 All Contributions
- By submission, each person submitting the contribution agrees (on own behalf, on behalf of organization represented, and on behalf of owners of proprietary rights) to:
  1. Grant unlimited perpetual, non-exclusive, royalty-free, worldwide license to ISOC and IETF under any copyrights, including right to copy, publish, distribute, and prepare derivative works.
  2. Acknowledge that ISOC and IETF have no duty to publish or use the contribution.
  3. Grant permission to reference contributor names/addresses.
  4. Represent that contribution properly acknowledges major contributors.
  5. Agree that no information is confidential and that ISOC and affiliates may freely disclose.
  6. Represent that contributor has disclosed existence of any proprietary or intellectual property rights reasonably and personally known.
  7. Represent that there are no limits to contributor's ability to make the grants, acknowledgments, and agreements above that are reasonably and personally known.

- By ratifying this description, the Internet Society warrants that it will not inhibit traditional open and free access to IETF documents for which license and right have been assigned per this section. This warrant is perpetual.

#### 10.3.2 Standards Track Documents
- (A) Where any patents, patent applications, or other proprietary rights are known or claimed with respect to any specification on the standards track and brought to IESG attention, the IESG **shall not** advance the specification without including a note indicating the existence of such rights.
  - Where implementations are required before advancement, only implementations that have, by statement of implementors, taken adequate steps to comply with such rights shall be considered for showing adequacy.
- (B) IESG disclaims responsibility for identifying or evaluating applicability of any claimed rights; takes no position on validity or scope.
- (C) Where IESG knows of rights under (A), the IETF Executive Director shall attempt to obtain written assurance from claimant that upon approval, any party will be able to obtain right to implement, use, and distribute under openly specified, reasonable, non-discriminatory terms. The Working Group may assist. Results shall not affect advancement except that IESG may defer approval to facilitate obtaining assurances. Results recorded by Executive Director and made available. IESG may direct inclusion of summary in RFC.

#### 10.3.3 Determination of Reasonable and Non-discriminatory Terms
- IESG will not make explicit determination that assurance of reasonable and non-discriminatory terms has been fulfilled in practice. Instead, normal requirements for advancement (two unrelated implementations for Draft Standard, significant implementation/operational experience for Standard) assume terms are reasonable. This assumption may be challenged during Last-Call.

### 10.4 Notices
- (A) Standards track documents shall include the standard IPR notice as specified in the original (see full text in RFC 2026 Section 10.4(A)).
- (B) Standards documents shall include invitation to bring intellectual property rights to attention of IETF Executive Director.
- (C) All ISOC standards-related documentation shall include the copyright notice and disclaimer as specified in the original (see full text in RFC 2026 Section 10.4(C)).
- (D) Where IESG is aware of proprietary rights at time of publication, the document shall contain a notice indicating that IETF has been notified of claimed rights and directing readers to online list of claimed rights.

## 11. Acknowledgments
- The process was first described in RFC 1310, revised in RFC 1602, then this revision. Specific acknowledgments to Lyman Chapin, Phill Gross, Christian Huitema, Jon Postel, Dave Crocker, Andy Ireland, Geoff Stewart, Jim Lampert, Dick Holleman, John Stewart, Robert Elz, Steve Coya, and members of the POISED Working Group.

## 12. Security Considerations
- Security issues are not discussed in this memo.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The ASCII text version of a standards-track specification is the definitive reference and must be a complete and accurate specification. | must | Section 2.1 |
| R2 | An Internet-Draft shall not be referenced by any paper, report, or Request-for-Proposal, nor shall a vendor claim compliance with an Internet-Draft. | shall (prohibition) | Section 2.2 |
| R3 | A Technical Specification shall include a statement of its scope and general intent for use (domain of applicability). | shall | Section 3.1 |
| R4 | An Applicability Statement shall apply one of the requirement levels defined in 3.3 to each referenced TS. | shall | Section 3.3 |
| R5 | An AS may not have a higher maturity level than any standards-track TS on which it relies. | may not (prohibition) | Section 3.2 |
| R6 | The IESG may require implementation/operational experience prior to granting Proposed Standard status for specifications affecting core protocols or significant operational impact. | may | Section 4.1.1 |
| R7 | At least two independent and interoperable implementations from different code bases are required for Draft Standard. | must | Section 4.1.2 |
| R8 | All options and features must be demonstrated in at least two interoperable implementations; otherwise options must be removed. | must | Section 4.1.2 |
| R9 | The Working Group chair must document specific implementations and testing for Draft/Standard advancement. | must | Section 4.1.2 |
| R10 | Standards track specifications normally must not depend on other standards track specifications at lower maturity or on non-standards track specifications (except external standards). | must not | Section 4.2.4 |
| R11 | A standards action must be approved by the IESG. | must | Section 6.1 |
| R12 | A specification intended to enter or advance shall first be posted as an Internet-Draft for at least two weeks. | shall | Section 6.1.1 |
| R13 | The IESG shall determine if specification satisfies applicable criteria and technical quality. | shall | Section 6.1.2 |
| R14 | Last-Call period shall be no shorter than two weeks (four weeks if not initiated by WG). | shall | Section 6.1.2 |
| R15 | Specification shall remain at Proposed Standard at least six months. | shall | Section 6.2 |
| R16 | Specification shall remain at Draft Standard at least four months or until next IETF meeting, whichever later. | shall | Section 6.2 |
| R17 | IESG shall review viability of standards-track specification that has not reached Standard after 24 months and every 12 months thereafter. | shall | Section 6.2 |
| R18 | New version of established Internet Standard must progress through full process as new specification. | must | Section 6.3 |
| R19 | IESG shall approve change to Historic for retiring a standard, with Last-Call and notification. | shall | Section 6.4 |
| R20 | Appeals must be initiated within two months of public knowledge of action/decision. | must | Section 6.5.4 |
| R21 | The following sections must not be subject of a variance: 5.1, 6.1, 6.1.1 (first paragraph), 6.1.2, 6.3 (first sentence), 6.5, and 9. | must not | Section 9.2 |
| R22 | No contribution subject to confidentiality may be considered in standards process. | may not | Section 10.2 |
| R23 | IESG shall not advance a standards-track specification with known IPR claims without including a note. | shall not | Section 10.3.2(A) |
| R24 | Standards track documents shall include the prescribed IPR notices and disclaimer. | shall | Section 10.4 |

## Informative Annexes (Condensed)
- **Appendix A: Glossary of Acronyms**: Provides expansions for abbreviations used in the document, such as ANSI, IAB, IESG, IETF, ISOC, RFC, TCP, etc. Useful for readers unfamiliar with the terms.
- **Section 11 (Acknowledgments)**: Credits contributions of individuals and groups who developed and refined the standards process over time.
- **Section 12 (Security Considerations)**: States that security issues are not discussed in this memo; no further detail.