# RFC 4519: Lightweight Directory Access Protocol (LDAP): Schema for User Applications
**Source**: IETF | **Version**: Standards Track, June 2006 | **Date**: June 2006 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc4519

## Scope (Summary)
This document defines attribute types and object classes intended for LDAP directory clients (e.g., White Pages). It obsoletes RFC 2256 and updates RFCs 2247, 2798, and 2377. The descriptions herein SHALL be considered definitive for LDAP use. Attribute definitions use ABNF from [RFC4512]; key words are per RFC 2119.

## Normative References
- [E.123] ITU-T Rec. E.123 (1988)
- [E.164] ITU-T Rec. E.164 (1997)
- [F.1] CCITT Rec. F.1 (1992)
- [F.31] CCITT Rec. F.31 (1988)
- [ISO3166] Codes for the representation of names of countries
- [RFC1034] STD 13, RFC 1034
- [RFC1123] STD 3, RFC 1123
- [RFC2119] BCP 14, RFC 2119
- [RFC2181] RFC 2181
- [RFC3490] RFC 3490
- [RFC4013] RFC 4013
- [RFC4234] RFC 4234
- [RFC4510] RFC 4510
- [RFC4512] RFC 4512
- [RFC4517] RFC 4517
- [X.121] ITU-T Rec. X.121 (1996)
- [X.509] ITU-T Rec. X.509 (1993)
- [X.520] ITU-T Rec. X.520 (1993)
- [X.521] ITU-T Rec. X.521 (1993)

## Definitions and Abbreviations
*(No separate glossary; terms like LDAP, DN, ABNF, OID used throughout)*

## 1. Introduction
This document provides attribute types and object classes for LDAP user applications, originally from X.500. It obsoletes RFC 2256; updates RFCs 2247 (supersedes 'dc', 'dcObject'), 2798 (supersedes 'uid'), 2377 (supersedes 'uidObject'). Server implementations SHOULD recognize all attribute types except 'searchGuide' and 'teletexTerminalIdentifier', whose use is greatly discouraged. Server SHOULD recognize all object classes.

## 2. Attribute Types
Each attribute type includes OID, description, syntax (with OID), and examples. Normative statements preserved.

### 2.1 'businessCategory' (2.5.4.15)
**Description**: Kinds of business performed by an organization. Multi-valued. Syntax: Directory String.

### 2.2 'c' / 'countryName' (2.5.4.6)
**Description**: Two-letter ISO 3166 country code. Single-valued. Syntax: Country String.

### 2.3 'cn' / 'commonName' (2.5.4.3)
**Description**: Names of an object. Multi-valued. Typically full name for a person.

### 2.4 'dc' / 'domainComponent' (0.9.2342.19200300.100.1.25)
**Description**: Single label of a DNS domain name. Syntax: IA5 String. Must conform to ABNF `label = (ALPHA / DIGIT) [*61(ALPHA / DIGIT / HYPHEN) (ALPHA / DIGIT)]`. Equality case-insensitive. Single-valued. Directory service does not enforce label restrictions; client responsibility. For IDN, SHALL use ToASCII method [RFC3490] with considerations per Section 4 of RFC 3490 for stored vs query purposes.

### 2.5 'description' (2.5.4.13)
**Description**: Human-readable descriptive phrases. Multi-valued. Syntax: Directory String.

### 2.6 'destinationIndicator' (2.5.4.27)
**Description**: Country and city strings for Public Telegram Service per CCITT F.1/F.31. Multi-valued. Syntax: Printable String. Directory will not ensure conformance.

### 2.7 'distinguishedName' (2.5.4.49)
**Description**: Base type for DN syntax attributes; not used directly. Servers not supporting subtyping need not recognize. Clients MUST NOT assume subtyping capability.

### 2.8 'dnQualifier' (2.5.4.46)
**Description**: Disambiguating strings to prevent name conflicts when merging data. Recommended to be same for all entries from a source. Multi-valued.

### 2.9 'enhancedSearchGuide' (2.5.4.47)
**Description**: Sets of information for search filter construction. Multi-valued. Syntax: Enhanced Guide.

### 2.10 'facsimileTelephoneNumber' (2.5.4.23)
**Description**: Telephone numbers for facsimile terminals, optionally with parameters. Multi-valued. Syntax: Facsimile Telephone Number.

### 2.11 'generationQualifier' (2.5.4.44)
**Description**: Suffix part of a person's name. Multi-valued.

### 2.12 'givenName' (2.5.4.42)
**Description**: Part of a person's name that is not the surname. Multi-valued.

### 2.13 'houseIdentifier' (2.5.4.51)
**Description**: Building identifiers within a location. Multi-valued. Syntax: Directory String.

### 2.14 'initials' (2.5.4.43)
**Description**: Initials of some or all names except surname(s). Multi-valued.

### 2.15 'internationalISDNNumber' (2.5.4.25)
**Description**: ISDN addresses per ITU E.164. Multi-valued. Syntax: Numeric String.

### 2.16 'l' / 'localityName' (2.5.4.7)
**Description**: Names of a locality or place. Multi-valued.

### 2.17 'member' (2.5.4.31)
**Description**: Distinguished names of objects on a list or in a group. Multi-valued.

### 2.18 'name' (2.5.4.41)
**Description**: Supertype for user attribute types with name syntax. Multi-valued. Unlikely used directly. Servers not supporting subtyping need not recognize. Clients MUST NOT assume subtyping. Syntax: Directory String.

### 2.19 'o' / 'organizationName' (2.5.4.10)
**Description**: Names of an organization. Multi-valued.

### 2.20 'ou' / 'organizationalUnitName' (2.5.4.11)
**Description**: Names of an organizational unit. Multi-valued.

### 2.21 'owner' (2.5.4.32)
**Description**: Distinguished names of objects with ownership responsibility. Multi-valued.

### 2.22 'physicalDeliveryOfficeName' (2.5.4.19)
**Description**: Names used by Postal Service to identify a post office. Syntax: Directory String.

### 2.23 'postalAddress' (2.5.4.16)
**Description**: Addresses used by Postal Service. Multi-valued. Syntax: Postal Address.

### 2.24 'postalCode' (2.5.4.17)
**Description**: Codes for postal service zones. Multi-valued. Syntax: Directory String.

### 2.25 'postOfficeBox' (2.5.4.18)
**Description**: Postal box identifiers. Multi-valued. Syntax: Directory String.

### 2.26 'preferredDeliveryMethod' (2.5.4.28)
**Description**: Indication of preferred delivery method. Single-valued. Syntax: Delivery Method.

### 2.27 'registeredAddress' (2.5.4.26)
**Description**: Postal addresses for telegrams or expedited documents. Multi-valued. Syntax: Postal Address (subtype of postalAddress).

### 2.28 'roleOccupant' (2.5.4.33)
**Description**: Distinguished names of objects fulfilling role responsibilities. Multi-valued.

### 2.29 'searchGuide' (2.5.4.14)
**Description**: Sets of information for search filters; superseded by enhancedSearchGuide. (Use discouraged.)

### 2.30 'seeAlso' (2.5.4.34)
**Description**: Distinguished names of related objects. Multi-valued.

### 2.31 'serialNumber' (2.5.4.5)
**Description**: Serial numbers of devices. Multi-valued. Syntax: Printable String.

### 2.32 'sn' / 'surname' (2.5.4.4)
**Description**: Family names of a person. Multi-valued.

### 2.33 'st' / 'stateOrProvinceName' (2.5.4.8)
**Description**: Full names of states or provinces. Multi-valued.

### 2.34 'street' / 'streetAddress' (2.5.4.9)
**Description**: Site information from postal address (street name, number). Multi-valued. Syntax: Directory String.

### 2.35 'telephoneNumber' (2.5.4.20)
**Description**: Telephone numbers per ITU E.123. Multi-valued. Syntax: Telephone Number.

### 2.36 'teletexTerminalIdentifier' (2.5.4.22)
**Description**: Withdrawn due to withdrawal of F.200. (Use discouraged.)

### 2.37 'telexNumber' (2.5.4.21)
**Description**: Telex number, country code, answerback code. Multi-valued. Syntax: Telex Number.

### 2.38 'title' (2.5.4.12)
**Description**: Title of a person in organizational context. Multi-valued.

### 2.39 'uid' / 'userid' (0.9.2342.19200300.100.1.1)
**Description**: Computer system login names. Multi-valued. Syntax: Directory String.

### 2.40 'uniqueMember' (2.5.4.50)
**Description**: Distinguished names of group members with optional unique identifier to handle DN reuse. Multi-valued. Syntax: Name and Optional UID.

### 2.41 'userPassword' (2.5.4.35)
**Description**: Octet strings known only to user and system. Multi-valued. Application SHOULD prepare textual passwords by transcoding to Unicode, applying SASLprep [RFC4013], and encoding as UTF-8. Passwords stored as Octet String – not encrypted. Transfer over unencrypted transport strongly discouraged. For authentication, user need only prove knowledge of one value.

### 2.42 'x121Address' (2.5.4.24)
**Description**: Data network addresses per ITU X.121. Multi-valued. Syntax: Numeric String.

### 2.43 'x500UniqueIdentifier' (2.5.4.45)
**Description**: Binary strings to distinguish objects when DN reused. Multi-valued. Syntax: Bit String. Note: called 'uniqueIdentifier' in X.520; different from 'uid' and LDAP 'uniqueIdentifier' [RFC4524].

## 3. Object Classes
Server implementations SHOULD recognize all object classes listed. Each includes OID, type (STRUCTURAL or AUXILIARY), mandatory (MUST) and optional (MAY) attributes.

| Class | OID | Type | MUST | MAY |
|-------|-----|------|------|-----|
| applicationProcess | 2.5.6.11 | STRUCTURAL | cn | seeAlso, ou, l, description |
| country | 2.5.6.2 | STRUCTURAL | c | searchGuide, description |
| dcObject | 1.3.6.1.4.1.1466.344 | AUXILIARY | dc |  |
| device | 2.5.6.14 | STRUCTURAL | cn | serialNumber, seeAlso, owner, ou, o, l, description |
| groupOfNames | 2.5.6.9 | STRUCTURAL | member, cn | businessCategory, seeAlso, owner, ou, o, description |
| groupOfUniqueNames | 2.5.6.17 | STRUCTURAL | uniqueMember, cn | businessCategory, seeAlso, owner, ou, o, description |
| locality | 2.5.6.3 | STRUCTURAL |  | street, seeAlso, searchGuide, st, l, description |
| organization | 2.5.6.4 | STRUCTURAL | o | userPassword, searchGuide, seeAlso, businessCategory, x121Address, registeredAddress, destinationIndicator, preferredDeliveryMethod, telexNumber, teletexTerminalIdentifier, telephoneNumber, internationalISDNNumber, facsimileTelephoneNumber, street, postOfficeBox, postalCode, postalAddress, physicalDeliveryOfficeName, st, l, description |
| organizationalPerson | 2.5.6.7 | STRUCTURAL | (inherits sn, cn from person) | title, x121Address, registeredAddress, destinationIndicator, preferredDeliveryMethod, telexNumber, teletexTerminalIdentifier, telephoneNumber, internationalISDNNumber, facsimileTelephoneNumber, street, postOfficeBox, postalCode, postalAddress, physicalDeliveryOfficeName, ou, st, l |
| organizationalRole | 2.5.6.8 | STRUCTURAL | cn | x121Address, registeredAddress, destinationIndicator, preferredDeliveryMethod, telexNumber, teletexTerminalIdentifier, telephoneNumber, internationalISDNNumber, facsimileTelephoneNumber, seeAlso, roleOccupant, street, postOfficeBox, postalCode, postalAddress, physicalDeliveryOfficeName, ou, st, l, description |
| organizationalUnit | 2.5.6.5 | STRUCTURAL | ou | businessCategory, description, destinationIndicator, facsimileTelephoneNumber, internationalISDNNumber, l, physicalDeliveryOfficeName, postalAddress, postalCode, postOfficeBox, preferredDeliveryMethod, registeredAddress, searchGuide, seeAlso, st, street, telephoneNumber, teletexTerminalIdentifier, telexNumber, userPassword, x121Address |
| person | 2.5.6.6 | STRUCTURAL | sn, cn | userPassword, telephoneNumber, seeAlso, description |
| residentialPerson | 2.5.6.10 | STRUCTURAL | l (plus inherited sn, cn from person) | businessCategory, x121Address, registeredAddress, destinationIndicator, preferredDeliveryMethod, telexNumber, teletexTerminalIdentifier, telephoneNumber, internationalISDNNumber, facsimileTelephoneNumber, street, postOfficeBox, postalCode, postalAddress, physicalDeliveryOfficeName, st, l |
| uidObject | 1.3.6.1.1.3.1 | AUXILIARY | uid |  |

## 4. IANA Considerations
The IANA updated the LDAP descriptors registry per the template and table in RFC 4519, assigning or reserving OIDs for all attribute and object class descriptors listed (e.g., 'c', 'cn', 'dc', 'ou', etc.). Full table omitted for brevity.

## 5. Security Considerations
Attributes may contain personal information; privacy laws apply. Transfer of cleartext 'userPassword' is strongly discouraged without confidentiality. Multiple values for 'userPassword' require careful administration; servers encouraged to restrict to one value if appropriate. For authentication, only one value need be proven.

## 6. Acknowledgements
*(Informative – omitted)*

## 7. References
### 7.1 Normative References
*(Listed in Normative References section above)*

### 7.2 Informative References
- [RFC1274] Barker, P. and S. Kille, "The COSINE and Internet X.500 Schema", RFC 1274, November 1991.
- [RFC2247] Kille, S., et al., "Using Domains in LDAP/X.500 Distinguished Names", RFC 2247, January 1998.
- [RFC2377] Grimstad, A., et al., "Naming Plan for Internet Directory-Enabled Applications", RFC 2377, September 1998.
- [RFC2798] Smith, M., "Definition of the inetOrgPerson LDAP Object Class", RFC 2798, April 2000.
- [RFC4513] Harrison, R., Ed., "LDAP: Authentication Methods and Security Mechanisms", RFC 4513, June 2006.
- [RFC4523] Zeilenga, K., "LDAP Schema Definitions for X.509 Certificates", RFC 4523, June 2006.
- [RFC4524] Zeilenga, K., Ed., "COSINE LDAP/X.500 Schema", RFC 4524, June 2006.
- [X.500] ITU-T Rec. X.500 (1993) | ISO/IEC 9594-1:1994.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Descriptions in this document SHALL be considered definitive for use in LDAP. | shall | Section 1 |
| R2 | An LDAP server implementation SHOULD recognize all attribute types described in Section 2 except 'searchGuide' and 'teletexTerminalIdentifier'. | should | Section 2 |
| R3 | Client implementations MUST NOT assume that LDAP servers are capable of performing attribute subtyping. | must | Sections 2.7, 2.18 |
| R4 | LDAP server implementations that do not support attribute subtyping need not recognize 'distinguishedName' or 'name' in requests. | may | Sections 2.7, 2.18 |
| R5 | Directory applications supporting International Domain Names SHALL use the ToASCII method [RFC3490] to produce the domain component label. | shall | Section 2.4 |
| R6 | The application SHOULD prepare textual strings used as passwords by transcoding them to Unicode, applying SASLprep [RFC4013], and encoding as UTF-8. | should | Section 2.41 |
| R7 | Transfer of cleartext passwords is strongly discouraged where the underlying transport service cannot guarantee confidentiality and integrity. | should | Sections 2.41, 5 |
| R8 | LDAP servers SHOULD recognize all Object Classes listed in Section 3 as values of the 'objectClass' attribute | should | Section 3 |

## Informative Annexes (Condensed)
- **Appendix A – Changes Made Since RFC 2256**: Lists editorial and substantive changes, including removal of certificate-related attributes and classes (moved to [RFC4523]), removal of sections superseded by [RFC4517] and [RFC4512], addition of 'dc' attribute type and 'uid'/'uidObject' definitions, addition of IANA and Security sections, and consistent formatting. (Non-normative)