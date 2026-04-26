# RFC 2978: IANA Charset Registration Procedures
**Source**: IETF (BCP: 19) | **Version**: Obsoletes RFC 2278 | **Date**: October 2000 | **Type**: Best Current Practice (Normative)
**Original**: https://datatracker.ietf.org/doc/html/rfc2978

## Scope (Summary)
This document specifies the procedures for registering character sets (charsets) with the Internet Assigned Numbers Authority (IANA) for use with MIME and other Internet protocols. Registration associates names with charsets and indicates suitability for MIME text; it does not address general applicability.

## Normative References
- [RFC-2045] Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies
- [RFC-2046] MIME Part Two: Media Types
- [RFC-2047] MIME Part Three: Representation of Non-Ascii Text in Internet Message Headers
- [RFC-2184] MIME Parameter Value and Encoded Word Extensions: Character Sets, Languages, and Continuations
- [RFC-2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC-1759] Printer MIB
- [RFC-1700] Assigned Numbers
- [RFC-1543] Instructions to RFC Authors
- [RFC-2130] Report from the IAB Character Set Workshop
- [RFC-2468] I Remember IANA
- [ISO-10646] Information technology – Universal Multiple-Octet Coded Character Set (UCS) – Part 1: Architecture and Basic Multilingual Plane
- [ISO-8859] 8-bit Single-Byte Coded Graphic Character Sets (various parts)
- [US-ASCII] Coded Character Set – 7-Bit American Standard Code for Information Interchange, ANSI X3.4-1986

## Definitions and Abbreviations
- **Character**: A member of a set of elements used for the organization, control, or representation of data.
- **Charset**: A method of converting a sequence of octets into a sequence of characters; may also produce control information (e.g., directionality). Unconditional reverse conversion is not required. External profiling to determine mapping is **not permitted**.
- **Coded Character Set (CCS)**: A one-to-one mapping from a set of abstract characters to a set of integers (e.g., ISO 10646, US-ASCII).
- **Character Encoding Scheme (CES)**: A mapping from one or more CCSs to a set of octet sequences (e.g., UTF-8 applies only to ISO 10646).
- **MIBenum**: A unique integer identifier for a charset, assigned by IANA, used in the Printer MIB.

## 1. Charset Registration Requirements

### 1.1 Required Characteristics
- **R1**: Registered charsets **MUST** conform to the definition of "charset" (Section 1.3).
- **R2**: Charsets intended for use in MIME content types under the "text" top-level type **MUST** conform to RFC 2045 restrictions.
- **R3**: All registered charsets **MUST** note whether they are suitable for use in MIME text.
- **R4**: Charsets composed of one or more CCSs and a CES **MUST** either include or cite a definition of those CCSs/CES.
- **R5**: All registered charsets **MUST** be specified in a stable, openly available specification. Registration of charsets with unstable/unavailable specifications is **forbidden**.

### 1.2 New Charsets
- **R6**: Only charsets defined by other processes/standards bodies, or specific profiles/combinations thereof, are eligible for registration. The registration mechanism is **not** intended for design of entirely new charsets.

### 1.3 Naming Requirements
- **R7**: One or more names **MUST** be assigned to all registered charsets. Multiple names are permitted, but one primary name **MUST** be identified; others are aliases.
- **R8**: Each assigned name **MUST** uniquely identify a single charset.
- **R9**: All charset names **MUST** conform to MIME parameter value syntax (even if not suitable for "text" media type).
- **R10**: All charsets **MUST** be assigned a name beginning with "cs" (for MIBenum display) with no more than 40 characters from printable US-ASCII. Only one "cs" name per charset. If none explicitly defined, IANA will assign "cs"+primary name.
- **R11**: Charsets registered for use with "text" media type **MUST** have a primary name conforming to the restricted syntax of charset field in MIME encoded-words (RFC 2047, 2184). ABNF definition provided:
  ```
  mime-charset = 1*mime-charset-chars
  mime-charset-chars = ALPHA / DIGIT / "!" / "#" / "$" / "%" / "&" / "'" / "+" / "-" / "^" / "_" / "`" / "{" / "}" / "~"
  ALPHA = "A".."Z"  ; Case insensitive
  DIGIT = "0".."9"
  ```

### 1.4 Functionality Requirement
- **R12**: Charsets **MUST** function as actual charsets. Registration of transfer encodings, media types, or collections of separate entities is **not allowed**.

### 1.5 Usage and Implementation Requirements
- **R13**: A charset should be registered **ONLY** if it adds significant functionality valuable to a large community, **OR** if it documents existing practice in a large community. Charsets registered for the latter reason **should** be explicitly marked as of limited or specialized use and used only with prior bilateral agreement.

### 1.6 Publication Requirements
- **R14**: Charset registrations **MAY** be published in RFCs; RFC publication is **not required**.
- **R15**: Charset registrations **SHOULD** include a specification of mapping from the charset to ISO 10646 if feasible.

### 1.7 MIBenum Requirements
- **R16**: Each registered charset **MUST** be assigned a unique MIBenum integer by IANA at registration. MIBenum values are **not assigned** by the registrant.

## 2. Charset Registration Procedure

### 2.1 Present the Charset to the Community
- Send proposed registration to `ietf-charsets@iana.org`.
- Initiate a **two-week public review** process.
- Proposed charsets are **not formally registered** and **must not** be used; the "x-" prefix (RFC 2045) can be used until registration is complete.

### 2.2 Charset Reviewer
- After two weeks and when consensus is achieved, submit application to IANA and charset reviewer (appointed by IETF Applications Area Directors).
- Reviewer **either approves or rejects** within two weeks (posted to mailing list).
- Reviewer may issue last call to full IETF or recommend standards track processing.
- Decisions may be appealed to IESG.

### 2.3 IANA Registration
- Upon approval or successful appeal, IANA registers the charset, assigns a MIBenum, and makes it available to the community.

## 3. Location of Registered Charset List
- Registered charsets are posted in anonymous FTP file: `ftp://ftp.isi.edu/in-notes/iana/assignments/character-sets`
- Listed in periodically issued "Assigned Numbers" RFC (currently RFC-1700).
- Description may also be published as an Informational RFC via `rfc-editor@isi.edu`.

## 4. Charset Registration Template
- **To**: `ietf-charsets@iana.org`
- **Subject**: Registration of new charset [names]
- **Fields** (all names must be suitable for MIME content-type parameter):
  - Charset name
  - Charset aliases
  - Suitability for use in MIME text
  - Published specification(s) (openly available; compositions must include/reference CCS/CES)
  - ISO 10646 equivalency table (URI recommended)
  - Additional information
  - Person & email address for further information
  - Intended usage (COMMON, LIMITED USE, or OBSOLETE)

## 5. Security Considerations
This registration procedure does not raise security considerations appreciably different from those in protocols using registered charsets.

## 6. Changes made since RFC 2278
- Inclusion of mapping to ISO 10646 is now recommended for all registered charsets.
- Registration template updated to include ISO 10646 mapping and suitability for MIME text.

## 7. Informative Annexes (Condensed)
- **Section 8 – References**: Contains full list of normative and informative references as enumerated above.
- **Section 10 – Authors' Addresses**: Contact information for Ned Freed; note that Jon Postel passed away in 1998.
- **Section 11 – Full Copyright Statement**: Standard IETF copyright notice. Retained as per IETF policy.

## Requirements Summary
| ID | Requirement Summary | Normative Language | Reference |
|---|---|---|---|
| R1 | Conform to charset definition | MUST | Section 1.1, §1.3 |
| R2 | MIME text charsets must conform to RFC 2045 | MUST | Section 1.1 |
| R3 | Note suitability for MIME text | MUST | Section 1.1 |
| R4 | CCS/CES composition must be defined or referenced | MUST | Section 1.1 |
| R5 | Stable, openly available specification | MUST / forbidden | Section 1.1 |
| R6 | Only from existing standards or profiles | eligible only | Section 1.2 |
| R7 | One or more names, primary name identified | MUST | Section 1.3 |
| R8 | Names uniquely identify a charset | MUST | Section 1.3 |
| R9 | Names conform to MIME parameter value syntax | MUST | Section 1.3 |
| R10 | "cs" prefix name for MIBenum, ≤40 chars | MUST | Section 1.3 |
| R11 | Primary name for MIME text conform to restricted ABNF | MUST | Section 1.3 |
| R12 | Function as actual charset; no transfer encoding, etc. | MUST / not allowed | Section 1.4 |
| R13 | Register only if adds value or documents practice | should | Section 1.5 |
| R14 | RFC publication not required | MAY | Section 1.6 |
| R15 | Include ISO 10646 mapping if feasible | SHOULD | Section 1.6 |
| R16 | Unique MIBenum assigned by IANA | MUST | Section 1.7 |