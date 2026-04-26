# RFC 4288: Media Type Specifications and Registration Procedures
**Source**: Internet Engineering Task Force (IETF) – Best Current Practice 13 | **Version**: December 2005 | **Date**: December 2005 | **Type**: Normative (BCP)
**Original**: https://www.rfc-editor.org/rfc/rfc4288

## Scope (Summary)
This document defines procedures for the specification and registration of media types for use in MIME and other Internet protocols, establishing a central registry at IANA and detailing requirements and processes for different registration trees (standards, vendor, personal, and special x.).

## Normative References
- [RFC2045] – MIME Part One: Format of Internet Message Bodies
- [RFC2046] – MIME Part Two: Media Types
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- [RFC2978] – IANA Charset Registration Procedures
- [RFC3023] – XML Media Types
- [RFC3555] – MIME Type Registration of RTP Payload Formats
- [RFC3986] – URI Generic Syntax (STD 66)
- [RFC4234] – Augmented BNF for Syntax Specifications (ABNF)

## Definitions and Abbreviations
- **Media Type**: A label used to identify the format of data in protocols (e.g., MIME).
- **Registration Tree**: A classification of media types based on origin and purpose: Standards Tree, Vendor Tree, Personal/Vanity Tree, Special x. Tree.
- **Subtype Name**: The second part of a media type (e.g., "text/plain") structured with optional facets (e.g., "vnd.com.example").
- **IANA**: Internet Assigned Numbers Authority.
- **IESG**: Internet Engineering Steering Group.
- **RTP**: Real-time Transport Protocol.
- **Keywords**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per RFC2119).

## 1. Introduction
- **Purpose**: Define procedures for media type specification and registration to ensure orderly, well-specified, and public development of content labels.
- **Historical Note**: Process originally limited to MIME email; generalized in RFC2048, now independent of MIME. Restrictions on use of media types in specific environments now allowed (Section 4.9).

## 2. Media Type Registration Preliminaries
- Registration involves constructing a proposal, circulating for review appropriate to the tree, and registering if acceptable.

## 3. Registration Trees and Subtype Names
- Faceted names (e.g., "vnd.mudpie") distinguish trees.

### 3.1. Standards Tree
- **Intended for**: Types of general interest to the Internet community.
- **Requirement**: MUST be approved by the IESG and correspond to a formal publication by a recognized standards body. For IETF, MUST be published as an RFC (standalone or within a general specification).
- **Naming**: Not explicitly faceted (no period).
- **Owner**: The standards body itself. Modification requires same level of processing (e.g., standards track).

### 3.2. Vendor Tree
- **Intended for**: Commercially available products. "Vendor" broadly construed.
- **Facet**: Leading "vnd.". May be followed by a well-known producer name (e.g., "vnd.mudpie") or IANA-approved producer name + product designation (e.g., "vnd.bigcompany.funnypictures").
- **Review**: Not required but strongly encouraged via ietf-types@iana.org. Registrations may be submitted directly to IANA.

### 3.3. Personal or Vanity Tree
- **Intended for**: Experimental or non-commercial product registrations.
- **Facet**: Leading "prs.".
- **Owner**: Person or entity making registration, or transferee.
- **Review**: Encouraged via ietf-types list. Registrations may be submitted directly to IANA.

### 3.4. Special x. Tree
- **Purpose**: For unregistered, experimental types (analogous to "x-" prefix). Use discouraged.
- **Rule**: "x." as first facet; MUST NOT be registered.

### 3.5. Additional Registration Trees
- IANA may create new top-level trees with IESG advice and consent, for external registration by well-known permanent bodies. Expected to have equivalent review quality to standards tree. Establishment announced via RFC approved by IESG.

## 4. Registration Requirements
- All proposals must conform to requirements below; specifics vary by tree.

### 4.1. Functionality Requirement
- Media types MUST function as actual media formats. Charsets, transfer encodings, or collections of separate entities MUST NOT be registered.

### 4.2. Naming Requirements
- **Type/subtype names**: Case-insensitive, MUST conform to ABNF:
  ```
  type-name = reg-name
  subtype-name = reg-name
  reg-name = 1*127reg-name-chars
  reg-name-chars = ALPHA / DIGIT / "!" / "#" / "$" / "&" / "." / "+" / "-" / "^" / "_"
  ```
- **Reserved**: Names beginning with "X-" MUST NOT be registered.
- **Suffixes**: Subtypes not representing XML entities MUST NOT end with "+xml". "+suffix" constructs used with care due to potential conflicts.
- **Multiple names**: Discouraged.
- **Top-level type selection**: MUST consider nature of media. New subtypes MUST conform to restrictions of top-level type.

#### 4.2.1. Text Media Types
- Intended for textual material. "charset" parameter MAY be used; if defined, MUST specify charset name per RFC2978.
- **Plain text**: No formatting commands; linear sequence, possibly with line breaks, stacking, bidirectional text.
- **Rich text**: Formatted textual data should use text subtypes.

#### 4.2.2. Image Media Types
- Content specifies one or more images; subtype names the format.

#### 4.2.3. Audio Media Types
- Content contains audio data.

#### 4.2.4. Video Media Types
- Time-varying picture, possibly with color and coordinated sound. May include synchronized audio/text.

#### 4.2.5. Application Media Types
- For discrete data not fitting other types, to be processed by application. Examples: file transfer, spreadsheets, presentations, active languages.

#### 4.2.6. Multipart and Message Media Types
- Composite types encapsulating one or more objects with own labels. MUST conform to RFC2046 syntax and requirements.

#### 4.2.7. Additional Top-level Types
- If needed, MUST be defined via standards-track RFC only.

### 4.3. Parameter Requirements
- **Names**: Follow same ABNF as media type names (reg-name).
- **Value syntax**: MUST be specified by registration.
- **Standards tree**: Names, values, meanings MUST be fully specified; new parameters SHOULD NOT define new functionality (except for conveying additional information like version level).
- **Vendor/personal trees**: Should specify as completely as possible.

### 4.4. Canonicalization and Format Requirements
- **All trees**: MUST employ a single, canonical data format.
- **Standards tree**: Openly available specification MUST exist; MUST be referenced or included in proposal.
- **Vendor tree**: Specifications may be proprietary; reference to software/version is permitted.
- **Personal tree**: Format specification required; may be RFC or deposited with IANA (need not be public).
- **Patented technology**: Permitted, but respecting RFC2026 rules for standards-track; other bodies follow own IPR rules.

### 4.5. Interchange Recommendations
- Media types SHOULD interoperate across many systems/applications. Known interoperability issues SHOULD be identified. Universal interoperability not required.

### 4.6. Security Requirements
- **Standards tree**: MUST have security analysis. Vendor/personal trees encouraged but not required.
- **All trees**: Security descriptions MUST be accurate; "no security issues" ≠ "not assessed". All known risks MUST be identified.
- **Issues to consider**: Active content, data disclosure, compression attacks, lack of security mechanisms. Registration MUST state if active content used and steps taken to protect users.

### 4.7. Requirements specific to XML media types
- Additional requirements in RFC3023.

### 4.8. Encoding Requirements
- **Field**: "Encoding considerations". Possible values: 7bit, 8bit, binary, framed.
- **7bit/8bit**: CRLF-delimited text, additional restrictions in RFC2046.
- **framed**: Series of frames/packets; unsuitable for many traditional protocols; RTP usage rules in RFC3555.

### 4.9. Usage and Implementation Non-requirements
- Universal support NOT required for registration. If limited use intended, MUST be noted in "Restrictions on Usage" field.

### 4.10. Publication Requirements
- **Standards tree (IETF)**: MUST be published as RFC. Vendor/personal encouraged but not required. IANA retains copies.
- **Other standards bodies**: Formal specification with registration template (Section 10) must allow IANA to copy it.
- **Disclaimer**: Registration does not imply endorsement by IANA/IETF. Standards tree requires substantive review; vendor/personal trees do not.

### 4.11. Additional Information
- Optional SHOULD include: magic numbers, file extensions, Mac OS file type codes, fragment/anchor identifier info.

## 5. Registration Procedure
- Not a formal standards process; administrative.

### 5.1. Preliminary Community Review
- Standards tree registrations MUST be sent to ietf-types@iana.org. Other trees MAY be sent.

### 5.2. IESG Approval
- Standards tree registrations MUST be approved by IESG before registration.

### 5.3. IANA Registration
- Submit to iana@iana.org or via web form. Sending to ietf-types does not constitute submission. If part of RFC or IESG approved, no additional submission needed.

### 5.4. Media Types Reviewer
- Appointed by IETF Applications Area Director(s). Reviews registration for compliance. Decisions appealable to IESG per RFC2026 section 6.5.4. Once approved, IANA registers and makes it available.

## 6. Comments on Media Type Registrations
- Community may submit comments to IANA. Reviewed by media types reviewer, passed to owner if possible. Comments may be attached to registration with IANA approval.

## 7. Location of Registered Media Type List
- http://www.iana.org/assignments/media-types/

## 8. IANA Procedures for Registering Media Types
- **Standards tree**: Only upon IESG communication.
- **Vendor/personal trees**: Automatic without formal approval if minimal conditions met:
  - Must function as actual media format (no charsets/transfer encodings).
  - Properly formed type/subtype names, unique, correct tree prefix. Type names defined by standards-track RFC.
  - Personal tree: format specification or pointer required.
  - Reasonable security considerations section (IANA may reject obviously incompetent material).
- Additional requirement for standards tree: origin from IETF or recognized standards body.

## 9. Change Procedures
- Owner may request change; same procedure as original. Change denied if invalidates previously valid entities.
- Ownership transfer: Inform IANA and ietf-types list without discussion.
- IESG may reassign responsibility if owner unreachable.
- Registrations cannot be deleted; obsolete types marked OBSOLETE in "intended use" field.

## 10. Registration Template
- **Head**: To: ietf-types@iana.org, Subject: Registration of media type XXX/YYY
- Fields: Type name, Subtype name, Required parameters, Optional parameters, Encoding considerations, Security considerations, Interoperability considerations, Published specification, Applications that use this media type, Additional information (Magic number(s), File extension(s), Macintosh file type code(s)), Person & email address, Intended usage (COMMON, LIMITED USE, OBSOLETE), Restrictions on usage, Author, Change controller.
- Note: "none" not to be used for file extension/type code.

## 11. Security Considerations
- Security requirements discussed in Section 4.6.

## 12. IANA Considerations
- Purpose is to define IANA registries.

## 13. Acknowledgements
- Acknowledgment to Dr. Jon Postel.

## 14. References
- Normative and informative references as listed above.

## Informative Annexes (Condensed)
- **Appendix A – Grandfathered Media Types**: Pre-1996 registered types that would now belong to vendor/personal trees; reregistration encouraged but not required; ownership/change control principles apply.
- **Appendix B – Changes Since RFC 2048**: Summary of key updates: separation from MIME, URLs changed to iana.org, clarification of procedures, security sections extended, new syntax and length limit (127), encoding considerations extended to "framed", mandatory ietf-types list review for standards tree, etc.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Media types MUST function as actual media format; charsets and transfer encodings MUST NOT be registered. | MUST | Section 4.1 |
| R2 | Standards tree registrations MUST be approved by IESG and correspond to formal publication by recognized standards body. | MUST | Section 3.1 |
| R3 | Vendor/personal tree registrations may be submitted directly to IANA; review on ietf-types list strongly encouraged. | SHOULD | Sections 3.2, 3.3 |
| R4 | Type/subtype names MUST conform to ABNF (max 127 characters, specified characters). | MUST | Section 4.2 |
| R5 | Names beginning with "X-" or "x." MUST NOT be registered. | MUST | Sections 3.4, 4.2 |
| R6 | If "charset" parameter used for text subtype, it MUST specify a charset name per RFC2978. | MUST | Section 4.2.1 |
| R7 | Application of new top-level types MUST be via standards-track RFC only. | MUST | Section 4.2.7 |
| R8 | All registered media types MUST employ a single canonical data format. | MUST | Section 4.4 |
| R9 | Standards tree registrations MUST have a precise openly available specification referenced or included. | MUST | Section 4.4 |
| R10 | Security analysis MUST be done for standards tree registrations; all known security risks MUST be identified regardless of tree. | MUST | Section 4.6 |
| R11 | Media types with limited use MUST note that in registration. | MUST | Section 4.9 |
| R12 | Standards tree registrations (IETF) MUST be published as RFC. | MUST | Section 4.10 |
| R13 | Standards tree registrations MUST be announced on ietf-types list. | MUST | Section 5.1 |
| R14 | IANA registers vendor/personal types automatically if minimal conditions met (functioning media, proper naming, security section). | MUST | Section 8 |
| R15 | Media type registrations cannot be deleted; may be marked OBSOLETE. | MUST | Section 9 |