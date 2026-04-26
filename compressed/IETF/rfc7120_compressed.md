# RFC 7120: Early IANA Allocation of Standards Track Code Points
**Source**: IETF (Best Current Practice) | **Version**: BCP 100 | **Date**: January 2014 | **Type**: Normative (Best Current Practice)  
**Original**: http://www.rfc-editor.org/info/rfc7120

## Scope (Summary)
This memo defines the process for early allocation of code points by IANA from registries with policies "Specification Required" (where the specification will be published as an RFC), "RFC Required", "IETF Review", or "Standards Action". It obsoletes RFC 4020 and applies only to IETF Stream documents.

## Normative References
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.

## Definitions and Abbreviations
- **Early Allocation**: Allocation of code points by IANA before RFC publication, marked as "Temporary" with a one-year validity.
- **Deprecated Code Point**: A code point not allocated for use and not available for future allocation until explicitly de-allocated.
- **WG chairs**: For non‑Working Group documents, "WG chairs" is replaced by "Shepherding Area Director".

## 1. Introduction (Informative Summary)
Early allocation solves the problem of code point contention when pre‑RFC implementations are deployed. The procedures apply only to registries that require an RFC (RFC Required, IETF Review, Standards Action) or where a "Specification Required" registry will use an RFC as the stable reference. This document obsoletes RFC 4020.

## 2. Conditions for Early Allocation
The following conditions **must** hold before IANA considers a request:
- **(a)**: The code points must be from a space designated as "RFC Required", "IETF Review", or "Standards Action". Additionally, requests from a "Specification Required" registry are allowed if the specification will be published as an RFC.
- **(b)**: The specifications must be adequately described in an Internet‑Draft.
- **(c)**: The specifications must be stable – changes must be seamlessly interoperable.
- **(d)**: WG chairs and Area Directors (ADs) judge that there is sufficient interest in early implementation/deployment or that failure to make an early allocation might lead to code‑point contention.

## 3. Process for Early Allocation
### 3.1. Request
1. Authors submit a request to the WG chairs specifying the code points and the document.
2. WG chairs determine whether conditions (c) and (d) are met.
3. WG chairs gauge consensus within the WG.
4. If satisfied, WG chairs request approval from the AD(s). ADs may apply judgment, especially if registry depletion risk exists.
5. If AD approves, WG chairs request IANA to make the early allocation.
6. IANA allocates from the registry, marking it as **"Temporary"**, valid for **one year** from the allocation date. The allocation date and expiry date are recorded and publicly visible.
- **Note**: Internet‑Drafts should not include a specific code point value until IANA has completed the early allocation.

### 3.2. Follow‑Up
- Authors and WG chairs must review changes to ensure backward compatibility.
- If non‑backward‑compatible changes are required, a decision must be made on whether to deprecate the previously allocated code points.
- When the document reaches the point where IANA normally makes allocations, authors and WG chairs must remind IANA of the early allocations and their values. IANA then removes the "Temporary" tag.

### 3.3. Expiry
- **Renewal**: One renewal request is permitted per original request. Under rare circumstances, more renewals may be granted only after IESG review; the renewal request must include reasons and the WG’s plans.
- **Failure to progress**: If no follow‑up request is made or the document fails to become an RFC, the assignment remains visible but is marked expired. WG chairs must inform IANA that the expired assignments are not required and that the code points are to be marked **"deprecated"**.
- A deprecated code point is not available for new allocation. WG chairs may later request that IANA **de‑allocate** it (make it available for new allocations), considering existing implementations and registry space.
- **Implementer notice**: Deprecation and de‑allocation can occur any time after expiry; an expired early allocation should be considered deprecated.
- **IANA responsibility**: IANA is not responsible for tracking status, expirations, or re‑allocation.
- **IESG grace**: If a document is submitted to the IESG with valid early allocations, those allocations must not expire while the document is under IESG consideration or in the RFC Editor’s queue.

## 4. IANA Considerations
This document defines procedures for early allocation; IANA has updated impacted registries by removing any markings that specifically allowed early allocation, as this document supersedes the need for such markings.

## 5. Security Considerations
Denial‑of‑service attacks (code space depletion, process overloading) are possible. IANA may at any time request the IESG to suspend these procedures. ADs must guard against the process being used as an end‑run around the IETF consensus. If concerned, ADs **should** escalate the issue for IESG‑wide discussion.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Code points must be from a space designated as "RFC Required", "IETF Review", or "Standards Action" (or "Specification Required" if the spec will be published as an RFC). | must | Section 2(a) |
| R2 | Specifications must be adequately described in an Internet‑Draft. | must | Section 2(b) |
| R3 | Specifications must be stable (changes must be seamlessly interoperable). | must | Section 2(c) |
| R4 | WG chairs and ADs must judge sufficient interest or risk of contention. | must | Section 2(d) |
| R5 | Authors submit request to WG chairs. | must | Section 3.1(1) |
| R6 | WG chairs must determine conditions and gauge WG consensus. | must | Section 3.1(2,3) |
| R7 | WG chairs must request AD approval. | must | Section 3.1(4) |
| R8 | ADs may apply judgment, especially if registry depletion risk. | may | Section 3.1(4) |
| R9 | If AD approves, WG chairs must request IANA to make early allocation. | must | Section 3.1(5) |
| R10 | IANA must allocate and mark as "Temporary", valid for one year, and record dates. | must | Section 3.1(6) |
| R11 | Internet‑Drafts should not include specific code point value until IANA early allocation. | should | Section 3.1 Note |
| R12 | Authors and WG chairs must review changes for backward compatibility. | must | Section 3.2 |
| R13 | If non‑backward‑compatible changes, decide on deprecation. | must | Section 3.2 |
| R14 | When document progresses, authors and WG chairs must remind IANA of early allocations. | must | Section 3.2 |
| R15 | One renewal request allowed per original request; more only with IESG review. | must (limitation) | Section 3.3 |
| R16 | If no follow‑up or document fails, WG chairs must inform IANA to mark deprecated. | must | Section 3.3 |
| R17 | WG chairs may inform IANA to de‑allocate deprecated code points at any time. | may | Section 3.3 |
| R18 | IANA not responsible for tracking status. | (responsibility) | Section 3.3 |
| R19 | Early allocations valid at IESG submission must not expire during review/queue. | must | Section 3.3 |
| R20 | IANA may request IESG to suspend procedures at any time. | may | Section 5 |
| R21 | ADs with concern should escalate to IESG. | should | Section 5 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgments**: Thanks to contributors and reviewers of RFC 4020 and this document.