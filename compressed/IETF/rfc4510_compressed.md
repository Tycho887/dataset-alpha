# RFC 4510: Lightweight Directory Access Protocol (LDAP): Technical Specification Road Map
**Source**: IETF (Standards Track) | **Version**: June 2006 | **Date**: June 2006 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4510

## Scope (Summary)
This document provides a road map of the LDAP Technical Specification, which defines LDAPv3 as an Internet protocol for accessing distributed directory services in accordance with X.500 data and service models. It lists the component documents and defines the relationship to X.500 and previous specifications.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC4511] Sermersheim, J., Ed., "Lightweight Directory Access Protocol (LDAP): The Protocol", RFC 4511, June 2006.
- [RFC4512] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Directory Information Models", RFC 4512, June 2006.
- [RFC4513] Harrison, R., Ed., "Lightweight Directory Access Protocol (LDAP): Authentication Methods and Security Mechanisms", RFC 4513, June 2006.
- [RFC4514] Zeilenga, K., Ed., "Lightweight Directory Access Protocol (LDAP): String Representation of Distinguished Names", RFC 4514, June 2006.
- [RFC4515] Smith, M., Ed. and T. Howes, "Lightweight Directory Access Protocol (LDAP): String Representation of Search Filters", RFC 4515, June 2006.
- [RFC4516] Smith, M., Ed. and T. Howes, "Lightweight Directory Access Protocol (LDAP): Uniform Resource Locator", RFC 4516, June 2006.
- [RFC4517] Legg, S., Ed., "Lightweight Directory Access Protocol (LDAP): Syntaxes and Matching Rules", RFC 4517, June 2006.
- [RFC4518] Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Internationalized String Preparation", RFC 4518, June 2006.
- [RFC4519] Sciberras, A., Ed., "Lightweight Directory Access Protocol (LDAP): Schema for User Applications", RFC 4519, June 2006.
- [RFC4520] Zeilenga, K., "Internet Assigned Numbers Authority (IANA) Considerations for the Lightweight Directory Access Protocol (LDAP)", BCP 64, RFC 4520, June 2006.
- [RFC4521] Zeilenga, K., "Considerations for LDAP Extensions", BCP 118, RFC 4521, June 2006.
- [X.500] ITU-T, "The Directory -- Overview of concepts, models and services", X.500(1993) (also ISO/IEC 9594-1:1994).
- [X.501] ITU-T, "The Directory -- Models", X.501(1993) (also ISO/IEC 9594-2:1994).
- [X.511] ITU-T, "The Directory: Abstract Service Definition", X.511(1993) (also ISO/IEC 9594-3:1993).

## Definitions and Abbreviations
- **LDAP / LDAPv3**: The Lightweight Directory Access Protocol version 3 as defined by this technical specification (see Section 1).
- **MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / MAY / OPTIONAL**: Keywords as defined in BCP 14 [RFC2119] (see Section 1.1).

## 1. The LDAP Technical Specification
- The LDAP technical specification consists of this document and the following documents (list preserved):
  - LDAP: The Protocol [RFC4511]
  - LDAP: Directory Information Models [RFC4512]
  - LDAP: Authentication Methods and Security Mechanisms [RFC4513]
  - LDAP: String Representation of Distinguished Names [RFC4514]
  - LDAP: String Representation of Search Filters [RFC4515]
  - LDAP: Uniform Resource Locator [RFC4516]
  - LDAP: Syntaxes and Matching Rules [RFC4517]
  - LDAP: Internationalized String Preparation [RFC4518]
  - LDAP: Schema for User Applications [RFC4519]
- The terms "LDAP" and "LDAPv3" refer informally to the protocol specified by this technical specification.
- **Normative Identification**: The LDAP suite, as defined here, **should** be formally identified in other documents by a normative reference to this document.
- Extensions to LDAP may be specified in other documents; nomenclature for LDAP-plus-extensions is not defined here. Extensions are expected to be truly optional.
- Considerations for LDAP extensions described in BCP 118, RFC 4521 fully apply to this revision.
- IANA considerations described in BCP 64, RFC 4520 fully apply to this revision.

### 1.1. Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119].

## 2. Relationship to X.500
- This technical specification defines LDAP in terms of [X.500] as an X.500 access mechanism.
- **R1**: An LDAP server **MUST** act in accordance with the X.500 (1993) series of ITU-T Recommendations when providing the service.
- It is **not required** that an LDAP server make use of any X.500 protocols in providing this service (e.g., LDAP can be mapped onto any other directory system so long as the X.500 data and service models [X.501][X.511] are not violated in the LDAP interface).
- This technical specification explicitly incorporates portions of X.500(93). Later revisions of X.500 do **not automatically apply**.

## 3. Relationship to Obsolete Specifications
- This technical specification obsoletes the previously defined LDAP technical specification defined in RFC 3377 (and consisting of RFCs 2251-2256, 2829, 2830, 3771, and 3377 itself).
- Specific replacement relationships:
  - This document replaces RFC 3377 and Section 3.3 of RFC 2251.
  - [RFC4512] replaces portions of RFC 2251, RFC 2252, and RFC 2256.
  - [RFC4511] replaces the majority of RFC 2251, portions of RFC 2252, and all of RFC 3771.
  - [RFC4513] replaces RFC 2829, RFC 2830, and portions of RFC 2251.
  - [RFC4517] replaces the majority of RFC 2252 and portions of RFC 2256.
  - [RFC4519] replaces the majority of RFC 2256.
  - [RFC4514] replaces RFC 2253.
  - [RFC4515] replaces RFC 2254.
  - [RFC4516] replaces RFC 2255.
- [RFC4518] is new to this revision.
- Each document contains appendices summarizing changes. Appendix A.1 details changes to RFC 3377; Appendix A.2 details changes to Section 3.3 of RFC 2251.
- Portions of this technical specification also update and/or replace other documents not listed above; these are discussed in the respective documents.

## 4. Security Considerations
- LDAP security considerations are discussed in each document comprising the technical specification.

## 5. Acknowledgements
- This document is based largely on RFC 3377 by J. Hodges and R. Morgan, and also borrows from RFC 2251 by M. Wahl, T. Howes, and S. Kille. It is a product of the IETF LDAPBIS Working Group.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | An LDAP server **MUST** act in accordance with the X.500 (1993) series of ITU-T Recommendations when providing the service. | **MUST** (normative) | Section 2 |
| R2 | The LDAP suite **should** be formally identified in other documents by a normative reference to this document. | **should** (normative but weaker) | Section 1 |
| R3 | Extensions are expected to be truly optional. | **expectation** (informative normative?) | Section 1 |
| R4 | Considerations for LDAP extensions [RFC4521] fully apply. | **fully apply** (normative) | Section 1 |
| R5 | IANA considerations [RFC4520] fully apply. | **fully apply** (normative) | Section 1 |
| R6 | The key words (MUST, etc.) are to be interpreted as described in BCP 14. | **interpretation rule** | Section 1.1 |

## Informative Annexes (Condensed)
- **Appendix A.1 – Changes to RFC 3377**: This document is nearly a complete rewrite of RFC 3377. The primary change is redefining "LDAP" and "LDAPv3" to refer to this revision.
- **Appendix A.2 – Changes to Section 3.3 of RFC 2251**: The word "document" was replaced with "technical specification" to clarify that the section applies to the entire LDAP technical specification.