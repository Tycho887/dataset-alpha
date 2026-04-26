# RFC 2048 (BCP 13): Multipurpose Internet Mail Extensions (MIME) Part Four: Registration Procedures
**Source**: Network Working Group (N. Freed, J. Klensin, J. Postel) | **Version**: November 1996 | **Date**: November 1996 | **Type**: Best Current Practice
**Obsoletes**: RFC 1521, 1522, 1590 | **Original**: https://datatracker.ietf.org/doc/html/rfc2048

## Scope (Summary)
This document defines IANA registration procedures for MIME facilities: media types, external body access types, and content-transfer-encodings. It establishes registration trees (IETF, vendor, personal, and special “x.”), requirements for each tree, and the procedures for review, approval, and change control. Registration of character sets for MIME is covered elsewhere and is not addressed here.

## Normative References
- RFC 822 (STD 11) – Message Representation Protocol
- RFC 934 – earlier work on message bodies
- RFC 1049 – earlier work on message content types
- RFC 1341, 1342 (obsoleted by 1521, 1522)
- RFC 1521, 1522 (obsoleted by this document)
- RFC 1543 – Instructions to RFC Authors
- RFC 1602 – IETF Standards Process (patented technology restrictions)
- RFC 1700 (STD 2) – Assigned Numbers
- RFC 2045 – Multipurpose Internet Mail Extensions (MIME) Part One
- RFC 2046 – Multipurpose Internet Mail Extensions (MIME) Part Two
- RFC 2049 – MIME Conformance (Appendix describes changes from previous versions)

## Definitions and Abbreviations
- **IANA**: Internet Assigned Numbers Authority – central registry for values.
- **IESG**: Internet Engineering Steering Group – approves IETF tree registrations.
- **MIME**: Multipurpose Internet Mail Extensions.
- **Media Type**: A MIME content type (type/subtype) that identifies a data format.
- **Access Type**: Mechanism used to retrieve actual body data for message/external-body references.
- **Transfer Encoding**: Transformation applied to MIME media types after canonical form, e.g., base64, quoted-printable.
- **Registration Tree**: A naming structure; IETF tree (no facet), vendor tree (“vnd.”), personal tree (“prs.”), special “x.” tree.
- **Facet**: A component of a subtype name separated by periods (e.g., “vnd.”).
- **Canonical Form**: The single, standard data format required for all registered media types.

---

## 1. Introduction
Recent Internet protocols (especially MIME [RFC 2045]) are extensible. This document defines registration procedures using IANA as a central registry to ensure orderly, well-specified, public development. The historical note explains that the original procedure was too restrictive for new environments.

## 2. Media Type Registration
Registration of a new media type requires a proposal that conforms to requirements specific to the registration tree used.

### 2.1 Registration Trees and Subtype Names
Subtype names use faceted names (e.g., “tree.subtree...type”). The trees are:

#### 2.1.1 IETF Tree
- Intended for types of general interest to the Internet Community.
- **Approval required**: IESG approval and **must** be published as an RFC.
- Names are **not** explicitly faceted (no period).
- Owner: IETF itself. Changes require the same level of processing as initial registration.

#### 2.1.2 Vendor Tree
- For commercially available products.
- Distinguished by leading facet “vnd.”.
- Optionally: “vnd.producer” or “vnd.producer.product”.
- Registration may be submitted directly to IANA; public review is strongly encouraged but not required.

#### 2.1.3 Personal or Vanity Tree
- For experimental or non-commercial products.
- Distinguished by leading facet “prs.”.
- Owner: the person or entity making the registration.
- Registration may be submitted directly to IANA; public review is strongly encouraged but not required.

#### 2.1.4 Special “x.” Tree
- For unregistered, experimental types (equivalent to “x-” names).
- **Should** only be used with active agreement of exchanging parties.
- Use of “x-” and “x.” forms is discouraged.

#### 2.1.5 Additional Registration Trees
- IANA **may**, with IESG advice and consent, create new top-level trees (e.g., for scientific societies).
- Quality of review expected equivalent to IETF tree. Announcement via RFC approved by IESG.

### 2.2 Registration Requirements
#### 2.2.1 Functionality Requirement
- Media types **must** function as an actual media format. Transfer encodings, character sets, or collections of separate entities **shall not** be registered as media types.

#### 2.2.2 Naming Requirements
- Each registered media type **must** be assigned MIME type and subtype names that uniquely identify it.
- The subtype name identifies the registration tree.
- The top-level type **must** reflect the nature of the media (e.g., image, audio).
- New subtypes **must** conform to restrictions of the top-level type (e.g., multipart subtypes **must** use encapsulation syntax).
- New top-level types **must** be defined via standards-track RFC only.

#### 2.2.3 Parameter Requirements
- Names, values, and meanings of any parameters **must** be fully specified for IETF tree registrations; **should** be specified as completely as possible for vendor/personal trees.
- New parameters **must not** be defined as a way to introduce new functionality in IETF tree types, though additional information (e.g., “revision”) is allowed.

#### 2.2.4 Canonicalization and Format Requirements
- All registered media types **must** employ a single, canonical data format.
- For IETF tree: a precise and openly available specification **must** be referenced or included.
- Vendor tree: format specification may be proprietary; registration **must** include specification of software/version that produces or processes the type.
- Personal tree: format specification required, may be deposited with IANA (may not be public).
- Patented technology permitted, but restrictions in RFC 1602 for standards-track **must** be respected.

#### 2.2.5 Interchange Recommendations
- Media types **should** interoperate across as many systems as possible. Known interoperability issues **should** be identified. Universal interoperability not required.

#### 2.2.6 Security Requirements
- Security analysis **required** for IETF tree registrations; encouraged for vendor/personal trees.
- All security issues **must** be identified accurately; a statement of no security issues **must** not be confused with lack of assessment.
- Known risks **must** be identified regardless of tree.
- Security considerations subject to continuing evaluation.

#### 2.2.7 Usage and Implementation Non-requirements
- Universal support/implementation is **not** a requirement for registration. If limited use intended, it **should** be noted in registration.

#### 2.2.8 Publication Requirements
- IETF tree proposals **must** be published as RFCs. Vendor/personal proposals are encouraged but not required.
- IANA retains copies of all proposals and publishes them as part of the registration tree.
- Registration in non-IETF trees does **not** imply endorsement by IANA or IETF.

#### 2.2.9 Additional Information
- Optional information: magic numbers, file extensions, Macintosh file type codes – if available, **should** be provided.

### 2.3 Registration Procedure
#### 2.3.1 Present the Media Type to the Community for Review
- **Must** send proposal to ietf-types@iana.org for a two-week review period.
- Proposed types **must not** be used; use “x-” prefix until registration complete.

#### 2.3.2 IESG Approval
- IETF tree registrations **must** be submitted to IESG for approval.

#### 2.3.3 IANA Registration
- After meeting requirements and necessary approval, submit to IANA for registration.

### 2.4 Comments on Media Type Registrations
- Comments may be submitted to IANA, which passes them to the owner. If IANA approves, comment is attached to the registration.

### 2.5 Location of Registered Media Type List
- Posted in anonymous FTP: ftp://ftp.isi.edu/in-notes/iana/assignments/media-types/
- Also listed in periodically issued “Assigned Numbers” RFC.

### 2.6 IANA Procedures for Registering Media Types
- IETF tree: only in response to IESG communication.
- Vendor/Personal trees: automatic and without formal review if minimal conditions are met:
  1. **Must** function as actual media format.
  2. **Must** have properly formed type and subtype names, unique, conform to MIME grammar, and contain proper tree prefix.
  3. Personal tree: **must** provide a format specification or pointer.
  4. Security considerations **must not** be obviously bogus; IANA has authority to exclude incompetent material.

### 2.7 Change Control
- Author may request change; follows same procedure as registration (publish revised template, two-week comment, IANA after review if required).
- Changes **should** only be for serious omissions/errors. May be denied if it invalidates previously valid entities.
- Owner may transfer responsibility to another person/agency by informing IANA and ietf-types list.
- IESG may reassign responsibility (e.g., if author unreachable).
- Media type registrations **may not** be deleted; obsolete types **shall** be marked by change to “intended use” field.

### 2.8 Registration Template
Template includes: MIME media type name, subtype name, required/optional parameters, encoding considerations, security considerations, interoperability considerations, published specification, applications, additional info (magic number, file extension, Mac code), contact, intended usage (COMMON, LIMITED USE, OBSOLETE), author/change controller.

## 3. External Body Access Types
RFC 2046 defines message/external-body; this section covers registration of additional access types.

### 3.1 Registration Requirements
#### 3.1.1 Naming Requirements
- Each access type **must** have a unique name conforming to MIME parameter syntax.

#### 3.1.2 Mechanism Specification Requirements
- All protocols, transports, procedures **must** be described in sufficient detail for implementation. Secret/proprietary methods **expressly prohibited**. Restrictions of RFC 1602 **must** be respected.

#### 3.1.3 Publication Requirements
- All access types **must** be described by an RFC (may be informational).

#### 3.1.4 Security Requirements
- Known security issues **must** be fully described. Not required to be secure, but risks must be identified. Subject to continuing evaluation.

### 3.2 Registration Procedure
#### 3.2.1 Present the Access Type to the Community
- **Must** send proposal to ietf-types@iana.org for two-week review. Proposed types **must not** be used.

#### 3.2.2 Access Type Reviewer
- Reviewer appointed by IETF Applications Area Director. After two weeks, either forwards to IANA or rejects due to objections. Decision **must** be posted within 14 days. May be appealed to IESG.

#### 3.2.3 IANA Registration
- IANA registers after approval or successful appeal. Specification **must** also be published as an RFC.

### 3.3 Location of Registered Access Type List
- Posted in ftp://ftp.isi.edu/in-notes/iana/assignments/access-types/ and listed in “Assigned Numbers” RFC.

### 3.4 IANA Procedures for Registering Access Types
- IANA acts only on approval from access type reviewer or IESG communication overturning reviewer’s ruling.

## 4. Transfer Encodings
Transfer encodings transform MIME entities after canonical form. Standardization of many transfer encodings is **expressely discouraged**.

### 4.1 Transfer Encoding Requirements
#### 4.1.1 Naming Requirements
- Unique name conforming to Content-Transfer-Encoding header syntax.

#### 4.1.2 Algorithm Specification Requirements
- Algorithms **must** be described in full. Secret/proprietary algorithms **expressly prohibited**. Restrictions of RFC 1602 **must** be respected.

#### 4.1.3 Input Domain Requirements
- **Must** be applicable to arbitrary sequence of octets of any length. Dependence on particular input forms **not allowed**. (The 7bit and 8bit encodings do not conform; no additional such encodings permitted.)

#### 4.1.4 Output Range Requirements
- Output format **must** be fully documented, specifying whether output is 7bit, 8bit, or pure binary.

#### 4.1.5 Data Integrity and Generality Requirements
- **Must** be fully invertible on any platform. Lossy compression and encryption are **excluded**.

#### 4.1.6 New Functionality Requirements
- **Must** provide new functionality; some overlap acceptable but must offer something no other encoding provides.

### 4.2 Transfer Encoding Definition Procedure
- Begin with draft of standards-track RFC defining encoding precisely and providing substantial justification. Submit to IESG, which may: (1) reject, (2) approve formation of working group, (3) accept as-is and put on standards track. Transfer encoding considered defined once on standards track.

### 4.3 IANA Procedures for Transfer Encoding Registration
- No special procedure; all legitimate registrations appear as standards-track RFC. IESG notifies IANA when approved.

### 4.4 Location of Registered Transfer Encodings List
- Posted in ftp://ftp.isi.edu/in-notes/iana/assignments/transfer-encodings/ and listed in “Assigned Numbers” RFC.

## 5. Authors’ Addresses
(Informative – contact information for Ned Freed, John Klensin, Jon Postel provided; omitted from compression as non-normative.)

## Informative Annexes (Condensed)
- **Annex A — Grandfathered Media Types**: Media types registered prior to 1996 that would now belong in vendor or personal trees. Reregistration is encouraged but not required; ownership and change control principles from this document apply.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Media types must function as an actual media format. | shall | §2.2.1 |
| R2 | Subtype names must be unique, conform to MIME grammar, and contain proper tree prefix. | shall | §2.6 (2) |
| R3 | IETF tree registrations must be published as RFCs and approved by IESG. | shall | §2.1.1, §2.2.8, §2.3.2 |
| R4 | Vendor/personal tree registrations must meet minimal conditions (format, naming, etc.) for automatic registration. | shall | §2.6 |
| R5 | New top-level types must be defined via standards-track RFC only. | shall | §2.2.2 |
| R6 | All registered media types must employ a single, canonical data format. | shall | §2.2.4 |
| R7 | Security analysis required for IETF tree registrations; all known security risks must be identified regardless of tree. | shall | §2.2.6 |
| R8 | Access type mechanisms must be fully described; secret/proprietary methods prohibited. | shall | §3.1.2 |
| R9 | Transfer encodings must be fully invertible; lossy compression and encryption excluded. | shall | §4.1.5 |
| R10 | Transfer encodings must be applicable to arbitrary octet sequences of any length. | shall | §4.1.3 |
| R11 | Transfer encoding definitions must be on standards track; new functionalities must be justified. | shall | §4.1.6, §4.2 |
| R12 | Media type registrations may not be deleted; obsolete types must be marked. | shall | §2.7 |