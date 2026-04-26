# RFC 6838: Media Type Specifications and Registration Procedures
**Source**: IETF | **Version**: BCP 13 | **Date**: January 2013 | **Type**: Best Current Practice (Normative)
**Original**: http://www.rfc-editor.org/info/rfc6838

## Scope (Summary)
Defines procedures for specification and registration of media types for use in HTTP, MIME, and other Internet protocols. Establishes registration trees, requirements, and IANA procedures for media types and structured syntax suffixes.

## Normative References
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies", RFC 2045, November 1996.
- [RFC2046] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2978] Freed, N. and J. Postel, "IANA Charset Registration Procedures", BCP 19, RFC 2978, October 2000.
- [RFC3023] Murata, M., St. Laurent, S., and D. Kohn, "XML Media Types", RFC 3023, January 2001.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3979] Bradner, S., "Intellectual Property Rights in IETF Technology", BCP 79, RFC 3979, March 2005.
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC4855] Casner, S., "Media Type Registration of RTP Payload Formats", RFC 4855, February 2007.
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5378] Bradner, S. and J. Contreras, "Rights Contributors Provide to the IETF Trust", BCP 78, RFC 5378, November 2008.
- [RFC6532] Yang, A., Steele, S., and N. Freed, "Internationalized Email Headers", RFC 6532, February 2012.
- [RFC6657] Melnikov, A. and J. Reschke, "Update to MIME regarding "charset" Parameter Handling in Textual Media Types", RFC 6657, July 2012.
- [RFC6839] Hansen, T. and A. Melnikov, "Additional Media Type Structured Syntax Suffixes", RFC 6839, January 2013.

## Definitions and Abbreviations
- **Media Type**: Label consisting of a top-level type and a subtype, optionally with parameters, used to label content in protocols like HTTP and MIME.
- **Top-Level Type**: Broad classification (e.g., text, image, audio, video, application, multipart, message).
- **Subtype**: Specific format within a top-level type.
- **Registration Tree**: Classification of subtype names by prefix: Standards Tree (no prefix), Vendor Tree (`vnd.`), Personal/Vanity Tree (`prs.`), Unregistered `x.` Tree.
- **Structured Syntax Suffix**: A suffix (e.g., `+xml`, `+json`) appended to subtype name to indicate underlying structure.
- **Provisional Registration**: Early assignment of media type names in standards tree for prototyping/testing.
- **Media Types Reviewer**: Designated Expert appointed by IETF Applications Area Director(s) for review.
- **ABNF**: Augmented Backus-Naur Form as defined in [RFC5234].

## 1. Introduction
(Informative) Protocols like HTTP and MIME use media types for labeled content. A registration process ensures an orderly, well-specified, public set. This document specifies criteria and procedures for registering media types (Section 5) and structured suffixes (Section 6) in the IANA central registry. The registry location is `http://www.iana.org/assignments/media-types/`.

### 1.1 Historical Note
(Summarized) The process originated for mail environments with limited types; was generalized in [RFC2048]. Now a separate document independent of MIME.

### 1.2 Conventions Used in This Document
- **Key Words**: `MUST`, `MUST NOT`, `REQUIRED`, `SHALL`, `SHALL NOT`, `SHOULD`, `SHOULD NOT`, `RECOMMENDED`, `MAY`, `OPTIONAL` — as defined in [RFC2119] when in ALL CAPS; lower or mixed case without normative meaning.
- **ABNF**: Notation per [RFC5234], including core rules from Appendix B.

## 2. Media Type Registration Preliminaries
Registration begins with a proposal. Different trees have different requirements. The proposal is circulated and reviewed; registered if acceptable.

## 3. Registration Trees and Subtype Names
To increase efficiency, different subtype name structures are used. Faceted names (with a tree prefix) distinguish trees. Some pre-existing types do not conform — see Appendix A.

### 3.1 Standards Tree
- **Purpose**: Types of general interest to the Internet community.
- **Requirements**: Registrations **MUST** be either:
  1. Approved directly by the IESG (IETF Consensus — Standards Track, BCP, Informational, or Experimental; also non-IETF stream with IESG approval). Registration RFC required.
  2. Registered by a recognized standards-related organization using "Specification Required" (Expert Review). IESG makes one-time recognition decision.
- **Names**: **MUST NOT** have faceted names unless grandfathered (Appendix A).
- **Owner**: The standards-related organization.
- **Modification**: Same level of processing as initial registration.
- **Submission**: For recognized organizations, submit to IANA; undergoes Expert Review.

### 3.2 Vendor Tree
- **Purpose**: Types associated with publicly available products. "Vendor" and "producer" broadly construed. Industry consortia and non-commercial entities not qualifying as standards-related organizations may register here.
- **Who may register**: Anyone needing to interchange files with a product. Ownership belongs to the vendor/organization; they may assert ownership over a third-party registration at any time.
- **Third-party registration**: Both entities **SHOULD** be noted in the Change Controller field (e.g., "Foo, on behalf of Bar").
- **Naming**: Leading facet `vnd.`. May be followed by a well-known producer's subtype name or IANA-approved producer designation + product designation.
- **Review**: Public exposure encouraged but not required.
- **Submission**: Direct to IANA for Expert Review.

### 3.3 Personal or Vanity Tree
- **Purpose**: Experimental or non-commercial products.
- **Naming**: Leading facet `prs.`.
- **Owner**: The person/entity making the registration, or transferee.
- **Review**: Public exposure encouraged but not required.
- **Submission**: Direct to IANA for Expert Review.

### 3.4 Unregistered x. Tree
- **Purpose**: Types for exclusive use in private, local environments. Cannot be registered.
- **Note**: Types beginning with `x-` are no longer considered part of this tree (see [RFC6648]). Use of `x.` tree strongly discouraged.
- **Reregistration**: If widely deployed with `x-` prefix, **MAY** be registered in an alternative tree via Appendix A.

### 3.5 Additional Registration Trees
- New top-level trees **MAY** be created by IETF Standards Action. Expected review quality equivalent to standards tree; IETF should consider the requesting organization's expertise.

## 4. Registration Requirements
All registrations must conform to the following; specifics vary by tree.

### 4.1 Functionality Requirement
- **MUST** function as actual media formats. Not allowed: transfer encodings, charsets, collections of separate entities. Example: base64 cannot be registered. Applies to all trees.

### 4.2 Naming Requirements
- **MUST** assign top-level type and subtype names. Combination uniquely identifies type; facet identifies tree. Names case-insensitive.
- **ABNF**:
  ```abnf
  type-name = restricted-name
  subtype-name = restricted-name
  restricted-name = restricted-name-first *126restricted-name-chars
  restricted-name-first = ALPHA / DIGIT
  restricted-name-chars = ALPHA / DIGIT / "!" / "#" / "$" / "&" / "-" / "^" / "_"
  restricted-name-chars =/ "."   ; first dot specifies facet
  restricted-name-chars =/ "+"   ; last plus specifies structured syntax suffix
  ```
  Maximum 127 characters; **SHOULD** be limited to 64.
- Facet-less standards-tree registrations cannot use periods.
- Different names for same type discouraged.
- **Top-level type choice**: Must consider nature; new subtypes **MUST** conform to top-level type restrictions. Protocols may impose additional restrictions (see [RFC2046]).

#### 4.2.1 Text Media Types
- Intended for principally textual material.
- If a `charset` parameter is defined, it **MUST** be used to specify a charset name per [RFC2978].
- A `charset` parameter **SHOULD NOT** be specified when charset info is transported inside the payload (e.g., `text/xml`). If specified, it **SHOULD** be required; if optional, subtype **MAY** specify default or no default. UTF-8 **SHOULD** be the default (see [RFC6657]).
- All new `text/*` registrations **MUST** clearly specify how the charset is determined; relying on US-ASCII default no longer permitted. Explanatory text **SHOULD** be in the additional information section.
- Plain text: no formatting commands, font attributes, etc.; may allow stacking and bidirectional text.

#### 4.2.2 Image Media Types
- Top-level `image`: content specifies one or more images. Subtype names the format.

#### 4.2.3 Audio Media Types
- Top-level `audio`: content contains audio data.

#### 4.2.4 Video Media Types
- Top-level `video`: time-varying picture, possibly with color and coordinated sound. May include synchronized audio and/or text.

#### 4.2.5 Application Media Types
- For discrete data not fitting elsewhere, especially data processed by an application. Examples: file transfer, spreadsheets, active languages. Security issues must be understood.

#### 4.2.6 Multipart and Message Media Types
- Composite types encapsulating zero or more objects. All subtypes **MUST** conform to syntax rules in [RFC2046] as amended by [RFC6532] Section 3.5.

#### 4.2.7 Additional Top-Level Types
- If a new type does not fit existing, a new top-level type **MUST** be defined via Standards Track RFC.

#### 4.2.8 Structured Syntax Name Suffixes
- Suffixes like `+xml` indicate underlying structure. This specification formalizes a registry for such suffixes.
- Guideline: described by a readily available description, preferably from an established standards-related organization, with a reference usable in Normative References.
- Media types using a named structured syntax **SHOULD** use the appropriate registered `+suffix`. **MUST NOT** use a suffix for a syntax not actually employed. `+suffix` for unregistered syntaxes **SHOULD NOT** be used.

#### 4.2.9 Deprecated Aliases
- If widely deployed under multiple names, a preferred name **MUST** be chosen; applications **MUST** use the preferred name for compliance. Deprecated aliases **MAY** be supplied as additional information.

### 4.3 Parameter Requirements
- Media types **MAY** use parameters; some may be automatically available from the top-level type.
- Names, values, meanings **MUST** be fully specified for standards tree; **SHOULD** be for vendor/personal.
- Parameter name ABNF: `parameter-name = restricted-name`.
- Case-insensitive; no meaning to order; error if specified more than once.
- Registrations **MUST** specify parameter value syntax. Care needed with binary or problematic syntaxes.
- Protocols may impose further restrictions (MIME [RFC2045][RFC2231], HTTP [RFC2045][RFC5987]).
- New parameters **SHOULD NOT** introduce new functionality in standards tree; **MAY** add additional information without changing functionality. Same encouraged but not required for vendor/personal.
- Changes to parameters managed same as other changes (Section 5.5).

### 4.4 Canonicalization and Format Requirements
- **MUST** employ a single, canonical data format, regardless of tree.
- Standards tree: permanent and readily available public specification **MUST** exist, sufficient for interoperability. **MUST** be referenced in registration.
- Vendor/personal: format specification may be not publicly available; registration may limit information to software/version info. Encouraged but not required.
- Patented technology allowed but must respect [BCP 79][RFC3979] and [BCP 78][RFC5378] for Standards Track. Other organizations may have own IPR rules.
- IPR disclosures for vendor/personal encouraged but not required.

### 4.5 Interchange Recommendations
- Universal interoperability not required, but known issues **SHOULD** be identified. Publication does not require exhaustive review. Applies to all trees.

### 4.6 Security Requirements
- **MUST** do security analysis for standards tree; encouraged but not required for vendor/personal. Descriptions **MUST** be as accurate as possible; **MUST NOT** state "no security issues". Vendor/personal **MAY** say "not assessed".
- No requirement that types be secure; all known risks **MUST** be identified.
- Security considerations subject to continuing evaluation and modification; may be extended via comments (Section 5.4).
- Issues to examine: active content directives, disclosure of information, compression attacks, need for external security services.

### 4.7 Requirements Specific to XML Media Types
- Additional requirements in [RFC3023].

### 4.8 Encoding Requirements
- Field "encoding considerations" with possible values: `7bit`, `8bit`, `binary`, `framed` (e.g., RTP). Additional rules for framed in [RFC4855].
- Restrictions on 7bit/8bit in [RFC2046] Section 4.1.1.

### 4.9 Usage and Implementation Non-Requirements
- Universal support not required. If intended for limited use, **MUST** be noted in "Restrictions on Usage" field.

### 4.10 Publication Requirements
- IETF standards tree: **MUST** be published as RFCs. Vendor/personal RFC publication allowed but not required. IANA retains copies.
- Other standards-related organizations: **MUST** be described by formal standards specification. Copyright must allow IANA to copy.
- Registration does not imply endorsement. Standards tree requires substantive review; vendor/personal do not. Applicability statements may recommend types.

### 4.11 Fragment Identifier Requirements
- Registrations can specify interpretation of fragment identifiers ([RFC3986] Section 3.5).
- Encouraged to adopt schemes used with semantically similar types. Types using registered `+suffix` **MUST** follow fragment identifier rules in the suffix registration.

### 4.12 Additional Information
- Optional information **SHOULD** be included if available: magic numbers, file extensions, Mac OS file type codes.
- Standards tree: may be provided in formal specification; suggested to incorporate IANA registration form.

## 5. Media Type Registration Procedures
Administrative procedure for community comment without excessive delay. IETF standards tree follows normal IETF processes.

### 5.1 Preliminary Community Review
- Potential standards tree registration **SHOULD** be sent to `media-types@iana.org` for review. Other trees **MAY** be sent (OPTIONAL but encouraged).
- Purpose: solicit comments on name, references, interoperability, security. Submitter may revise or abandon.

### 5.2 Submit Request to IANA
- IETF standards tree: reviewed by IESG. Standards-related organizations and vendor/personal submitted directly to IANA. Prior posting encouraged.
- Send to `iana@iana.org` or web form at `http://www.iana.org/form/media-types`.

#### 5.2.1 Provisional Registrations
- For early assignment in standards tree during standardization.
- **MUST** include media type name and contact (including organization name). IANA checks and publishes in distinct provisional list.
- **MAY** be updated or abandoned at any time. If abandoned, name becomes unassigned.

### 5.3 Review and Approval
- Except provisional, submissions go to media types reviewer (appointed by IETF Apps Area ADs). Reviewer checks requirements; rejects if not met.
- Decisions appealable to IESG per [RFC2026] Section 6.5.4.
- After approval, IANA registers and publishes.
- For standards tree from other organizations, IANA checks recognized status; IESG confirmation needed if not currently recognized.

### 5.4 Comments on Media Type Registrations
- Comments may be submitted to IANA; reviewed by media types reviewer and passed to owner. Submitter may request comment attached to registration; IANA and reviewer approve.

### 5.5 Change Procedures
- Owner may request change using same procedure as original.
- Registrations cannot be deleted; OBSOLETE marked via change to "intended use".
- Significant changes only for serious omissions/errors; may be denied if renders prior valid entities invalid.
- Owner may transfer responsibility by informing IANA.
- IESG may reassign responsibility if owner unreachable.

### 5.6 Registration Template
Fields:
- Type name, Subtype name, Required parameters, Optional parameters, Encoding considerations, Security considerations, Interoperability considerations, Published specification, Applications that use this media type, Fragment identifier considerations, Additional information (Deprecated alias names, Magic number(s), File extension(s), Macintosh file type code(s)), Person & email to contact, Intended usage (COMMON, LIMITED USE, or OBSOLETE), Restrictions on usage, Author, Change controller, Provisional registration? (standards tree only). Use "N/A" if not applicable. Limited-use types should note if application list is exhaustive.

## 6. Structured Syntax Suffix Registration Procedures
To register a `+suffix`:
1. Check IANA registry for existing entry.
2. If none, fill template (Section 6.2) and include with media type registration or separate document (treated as IETF Contribution).
3. Send to `media-types@iana.org` for review.
4. Respond to comments, revise.
5. Submit to IANA.

IANA processing:
1. Check completeness; reject if incomplete.
2. Check for duplicate; reject if exists.
3. Request Expert Review.
4. Designated Expert may request additional review.
5. If approved, add to registry.

Initial registry content in [RFC6839].

### 6.1 Change Procedures
Same as initial registration. If original in IESG-approved document, update requires IESG approval.

### 6.2 Structured Syntax Suffix Registration Template
Fields:
- Name (full name of syntax)
- `+suffix` (the suffix)
- References (full citations)
- Encoding considerations (same as Section 4.8)
- Interoperability considerations
- Fragment identifier considerations
- Security considerations (same as Section 4.6, but option of not assessing not available)
- Contact
- Author/Change controller

## 7. Security Considerations
Referenced Section 4.6 for both media type and suffix registrations.

## 8. IANA Considerations
(Document defines IANA registries and procedures. IANA maintains media type registry with provisional section; structured syntax suffix registry created; annotations with dates and change history; new mailing list `media-types@iana.org`; `ietf-types@iana.org` retained as alias.)

## Informative Annexes (Condensed)
- **Appendix A (Grandfathered Media Types)**: Pre-1996 unfaceted types should be reregistered in appropriate tree but not required. Widely deployed unregistered types (including `x-` prefix) **SHOULD** be reregistered with faceted name; if not possible, may be registered with unfaceted name subject to media types reviewer and IESG approval.
- **Appendix B (Changes since RFC 4288)**: Lists 16 key changes including suffix registration, allowance for widely deployed unfaceted types, revised standards tree process, addition of fragment identifier field, loosened change requirements, provisional registration, deprecated aliases, third-party change controller possibility, etc.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Media types **MUST** function as actual media formats. | shall | Section 4.1 |
| R2 | All registered media types **MUST** be assigned top-level type and subtype names. | shall | Section 4.2 |
| R3 | Type and subtype names **MUST** conform to `restricted-name` ABNF. | shall | Section 4.2 |
| R4 | Standards-tree registrations **MUST** be either approved by IESG or by recognized standards-related organization with Specification Required. | shall | Section 3.1 |
| R5 | Vendor-tree registrations **MUST** have leading facet `vnd.`. | shall | Section 3.2 |
| R6 | Personal-tree registrations **MUST** have leading facet `prs.`. | shall | Section 3.3 |
| R7 | Unregistered `x.` tree types cannot be registered. | shall | Section 3.4 |
| R8 | New top-level type names **MUST** be defined via Standards Track RFC. | shall | Section 4.2.7 |
| R9 | Media types using a structured syntax **SHOULD** use appropriate registered `+suffix`; **MUST NOT** use suffix for syntax not employed. | should/shall | Section 4.2.8 |
| R10 | If a `charset` parameter is defined for text subtype, it **MUST** be used. | shall | Section 4.2.1 |
| R11 | All new `text/*` registrations **MUST** clearly specify how charset is determined. | shall | Section 4.2.1 |
| R12 | Security analysis **MUST** be done for standards tree; all known risks **MUST** be identified for all trees. | shall | Section 4.6 |
| R13 | Standards-tree registrations **MUST** have permanent public specification. | shall | Section 4.4 |
| R14 | Media types **MUST** employ single canonical data format. | shall | Section 4.4 |
| R15 | Fragment identifier rules for types with `+suffix` **MUST** follow suffix registration. | shall | Section 4.11 |
| R16 | Provisional registrations **MUST** include media type name and contact. | shall | Section 5.2.1 |
| R17 | Registration changes follow same procedure as original. | shall | Section 5.5 |
| R18 | Structured syntax suffix registrations must provide all template fields. | shall | Section 6.2 |