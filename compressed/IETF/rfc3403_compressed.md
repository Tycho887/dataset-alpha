# RFC 3403: Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: October 2002 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc3403

## Scope (Summary)
This document specifies the use of the Domain Name System (DNS) as a distributed database for the Dynamic Delegation Discovery System (DDDS). It defines the Naming Authority Pointer (NAPTR) DNS Resource Record (type 35) and how NAPTR records encode DDDS rules with keys as domain names. This RFC obsoletes RFC 2915 and is part of the DDDS series (RFC 3401, 3402, 3403, 3404, 3405).

## Normative References
- [6] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [7] Mockapetris, P., "Domain names - implementation and specification", STD 13, RFC 1035, November 1987.
- [8] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- [17] Yergeau, F., "UTF-8, a transformation format of ISO 10646", RFC 2279, January 1998.
- [3] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database", RFC 3403, October 2002. (self-reference for terminology)
- [1] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS", RFC 3401, October 2002.
- [2] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part Two: The Algorithm", RFC 3402, October 2002.

## Definitions and Abbreviations
- **DDDS**: Dynamic Delegation Discovery System.
- **DNS**: Domain Name System.
- **NAPTR**: Naming Authority Pointer Resource Record (type 35).
- **ORDER**: 16-bit unsigned integer specifying processing order; MUST be processed lowest to highest.
- **PREFERENCE**: 16-bit unsigned integer specifying priority among records with equal Order; SHOULD be processed low to high.
- **FLAGS**: <character-string> containing control flags; single characters A–Z and 0–9; case-insensitive.
- **SERVICES**: <character-string> specifying service parameters per application.
- **REGEXP**: <character-string> containing a substitution expression applied to the original client string.
- **REPLACEMENT**: <domain-name> that is the next domain to query; MUST be fully qualified.

## 3. DDDS Database Specification
- **General**: Uses DNS as specified in [8] and [7]. Character set is UTF-8 [17]. Substitution expressions MUST NOT depend on a specific POSIX locale.
- **Key Format**: Validly constructed DNS domain-name.
- **Lookup Request**: Client issues a DNS query for NAPTR records for the given Key (domain-name).
- **Lookup Response**: Series of NAPTR records as defined in Section 4.
- **Rule Insertion**: Rules added by adding new records to the appropriate DNS zone. Only the administrative controller of a zone can specify rules for Keys in that zone.
- **Collision Avoidance** (three methods):
  1. Create a new zone within the common domain for each application (e.g., urires.example.com, enum.example.com).
  2. Write regular expressions to anchor on the Application Unique String (e.g., scheme name or "+" character).
  3. Use distinct Flags or Services values so records from other applications are ignored.
- **TTL and Expiration**: Application MUST ensure no records have expired when relying on a set of rules. If any record has expired, the application MUST restart the DDDS algorithm from the beginning.

## 4. NAPTR RR Format

### 4.1 Packet Format
- DNS type code: 35.
- **ORDER**: 16-bit unsigned integer; records MUST be processed in order from lowest to highest. Equal order values are considered the same rule.
- **PREFERENCE**: 16-bit unsigned integer; records with equal Order SHOULD be processed low to high. Client MAY process higher preferences if it has good reason (e.g., protocol support). Once a match is found, client MUST NOT consider records with different Order, but MAY process records with same Order and different Preferences.
- **FLAGS**: <character-string>; single characters A–Z and 0–9; case-insensitive; can be empty. Application defines flags, including terminal vs. non-terminal.
- **SERVICES**: <character-string>; values defined by application specification.
- **REGEXP**: <character-string>; substitution expression applied to the original client string. Regular expressions MUST NOT be used in a cumulative fashion.
- **REPLACEMENT**: <domain-name>; used as next domain to query. MUST be fully qualified. Mutually exclusive with REGEXP – if both are present, record is in error and SHOULD be ignored or error returned.

### 4.2 Additional Information Processing
- **DNS Servers**: MAY add relevant RRsets (e.g., A, SRV) to the additional section.
- **Resolver/Applications**: MAY inspect additional section, but MUST NOT require records in the additional section for functionality.

### 4.3 Master File Format
- Follows RFC 1035; ORDER and PREFERENCE integers between 0–65535; Flags, Services, Regexp are quoted strings.

## 5. Application Specifications
An application using this database must define:
- The domain category for Keys produced by the First Well Known Rule (e.g., "foo.net" for the hypothetical 'foo' application).
- Allowed values for Services and Protocols fields.
- Expected output of terminal rewrite rules and encoding/use of Flags.

## 6. Examples (Informative, condensed)

### 6.1 URN Example
- Shows URN "urn:cid:199606121851.1@bar.example.com" resolved via NAPTR. First rule extracts "cid", appends "urn.arpa" → "cid.urn.arpa". Query returns a regexp that extracts "example.com". Subsequent query returns terminal records with flags 'a' and 's' leading to A records for cidserver.example.com and www.example.com.

### 6.2 E164 Example
- Telephone number +1-770-555-1212 becomes Key "17705551212"; inverted with dots and appended to "e164.arpa" → "2.1.2.1.5.5.5.0.7.7.1.e164.arpa.". Query returns terminal NAPTR records with flag 'u' and services "sip+E2U" and "smtp+E2U", producing URIs.

## 7. Advice for DNS Administrators (Informative)
- Double all backslashes in zone files to appear once in query response.
- Use the 'default delimiter' feature of the regular expression (first character after regex delimiter) to reduce backslashes.

## 8. Notes (Normative)
- Client **MUST** process multiple NAPTR records in the order specified by the "order" field – not simply use the first known service.
- When multiple RRs have the same "order", client **should** use preference to select next NAPTR, but may sort by additional criteria.
- If a rewrite lookup fails, clients are **strongly encouraged** to report failure rather than backing up to pursue other rewrite paths.

## 9. IANA Considerations (Informative)
- Values for Services and Flags fields are determined by applications; this specification itself does not require IANA registration.

## 10. Security Considerations (Informative)
- NAPTR records can be signed and validated via DNSSEC.
- This database makes identifiers subject to DNS attacks.
- Regular expressions **should** be checked for sanity and not blindly passed to execution environments like Perl.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Substitution expressions MUST NOT depend on a specific POSIX locale. | MUST | Section 3 |
| R2 | Application MUST ensure no records have expired when using a set of rules; if any expire, restart algorithm. | MUST | Section 3 |
| R3 | NAPTR ORDER field: 16-bit unsigned integer; records processed in ascending order. | MUST | Section 4.1 |
| R4 | NAPTR PREFERENCE field: records with equal Order SHOULD be processed in ascending order. | SHOULD | Section 4.1 |
| R5 | Once a match is found, client MUST NOT consider records with different Order, but MAY process same Order different Preference. | MUST/MAY | Section 4.1 |
| R6 | Regular expressions MUST NOT be used in a cumulative fashion. | MUST | Section 4.1 |
| R7 | REPLACEMENT field MUST be a fully qualified domain-name. | MUST | Section 4.1 |
| R8 | If REPLACEMENT and REGEXP both present, record SHOULD be ignored or error returned. | SHOULD | Section 4.1 |
| R9 | Applications MUST NOT require records in the Additional Information section for functionality. | MUST | Section 4.2.2 |
| R10 | Client MUST process NAPTR records in order specified by ORDER field. | MUST | Section 8 |
| R11 | If a rewrite lookup fails, clients are strongly encouraged to report a failure. | STRONGLY ENCOURAGED (SHOULD) | Section 8 |