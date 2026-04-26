# RFC 4645: Initial Language Subtag Registry
**Source**: Internet Engineering Task Force (IETF) | **Version**: Informational | **Date**: September 2006 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc4645

## Scope (Summary)
This document defines the initial contents of the IANA Language Subtag Registry as specified by RFC 4646, using criteria based on ISO 639-1/2, ISO 15924, ISO 3166-1, and UN M.49. It describes the process for converting existing RFC 3066 tags and selecting subtags from source standards. The actual registry contents have been removed from this memo to avoid confusion; the live registry is maintained by IANA.

## Normative References
- **RFC 4646**: Phillips, A., Ed. and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 4646, September 2006.

## Definitions and Abbreviations
- **Language Subtag Registry**: A database maintained by IANA containing language subtags (language, script, region, variant) used in BCP 47 language tags.
- **ILSR**: Initial Language Subtag Registry, the initial version created by this document.
- **Grandfathered**: A registry record type for tags registered under RFC 3066 that cannot be expressed as a valid sequence of defined subtags under RFC 4646.
- **Redundant**: A registry record type for tags that are entirely composed of defined subtags and thus are superseded by the subtag-based mechanism.
- **Deprecated**: A field indicating that a subtag or tag is obsolete; a preferred value may be provided.
- **Code element**: A value assigned by a source standard (e.g., ISO 639-1 alpha-2 code, ISO 15924 script code).

## 1. Introduction
- RFC 4646 (BCP 47) defines the Language Subtag Registry format and update process. This memo defines the initial registry contents based on the criteria in Section 2.
- The registry is expected to change over time; this memo does **not** define permanent contents.
- Subtags are derived from ISO 639-1, ISO 639-2, ISO 15924, ISO 3166-1, and UN M.49. **The registry is not a mirror of those standards and must not be used as one.**

## 2. Initialization of the Registry
The process described in this section was used to create the initial records.

### 2.1 Selection from Source Standards (Criteria 1–6)
1. **Date basis**: For each standard, the date referenced in RFC 1766 was selected as the starting date. Code elements valid on that date were added. Code elements withdrawn before that date were not added.
2. **Subsequent assignments**: Additional assignments up to the adoption date of RFC 4646 were added. Withdrawn values are marked as deprecated but not removed. Changes in assignment (e.g., 'CS' from Czechoslovakia to Serbia and Montenegro) were permitted.

**Additional rules for UN M.49 (criteria 3–6):**
3. UN numeric code elements for macro-geographical (continental) regions as of adoption of RFC 4646 were added and made valid for use in language tags.
4. Code elements for economic groupings or other groupings, and alphanumeric codes in Appendix X, were **not** added.
5. UN numeric code elements for countries/areas not associated with an ISO 3166-1 alpha-2 code were **not** added (see Section 4). These may be requested for registration under RFC 4646. Listing in Section 4 is not a guarantee of future registration.
6. Withdrawn, vacated, or deprecated UN M.49 code elements as of adoption date were **not** added.

### 2.2 Conversion of RFC 3066 Tags (Criteria 7–11)
The initial set of subtags was used to evaluate tags in the RFC 3066 registry:
7. Tags that were not deprecated, entirely composed of defined subtags, and correctly formatted were converted to type **"redundant"** (e.g., "zh-Hant").
8. Tags containing subtags that did not match valid registration patterns or were not defined by RFC 4646 were converted to type **"grandfathered"**. They cannot become "redundant" except by revision of RFC 4646, but may acquire "Deprecated" and "Preferred-Value" fields.
9. Tags that were deprecated in RFC 3066 were converted to type **"grandfathered"** with a "Deprecated" date and "Preferred-Value". For example, "art-lojban" → preferred value "jbo".
10. Tags that were not deprecated, had correct format, but contained subtags not yet in the ILSR—where those subtags were eligible as variants—were converted to type **"redundant"** after creating appropriate variant records. The subtags added as variants were:
    - `1901` (Prefix: de)
    - `1996` (Prefix: de)
    - `nedis` (Prefix: sl)
    - `rozaj` (Prefix: sl)
11. All remaining RFC 3066 tags were converted to type **"grandfathered"**. Interested parties may register variant subtags under RFC 4646; if all subtags become fully defined, the grandfathered tag record is changed to "redundant". Prior approval under RFC 3066 does not guarantee approval of a variant subtag under RFC 4646.

## 3. Initial Registry Contents
The material specifying the initial set of records was deleted on publication to avoid confusion with the live registry. The IANA language subtag registry is available at <http://www.iana.org/numbers.html> under "Language Tags".

## 4. Omitted Code Elements
The following UN M.49 code elements were not associated with an ISO 3166-1 alpha-2 code and were not assigned as subtags in the ILSR. They were valid candidates for registration as region subtags under RFC 4646:
- 830 Channel Islands
- 831 Guernsey
- 832 Jersey
- 833 Isle of Man

The last three became ineligible for registration in April 2006 when ISO 3166-1 codes GG, JE, and IM were assigned as region subtags.

## 5. Security Considerations
Security considerations relevant to the Language Subtag Registry and the use of language tags are described in RFC 4646.

## 6. IANA Considerations
This document points to the initial content for the Language Subtag Registry maintained by IANA at <http://www.iana.org/numbers.html> under "Language Tags". For procedures on format and ongoing maintenance, see RFC 4646.

## 7. References
### 7.1 Normative References
- **RFC 4646**: Phillips, A., Ed. and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 4646, September 2006.

### 7.2 Informative References
- **ISO 15924**: "Information and documentation — Codes for the representation of names of scripts", January 2004.
- **ISO 3166-1**: "Codes for the representation of names of countries", 3rd edition, August 1988.
- **ISO 639-1**: "Codes for the representation of names of languages — Part 1: Alpha-2 code", 2002.
- **ISO 639-2**: "Codes for the representation of names of languages — Part 2: Alpha-3 code", 1998.
- **RFC 1766**: Alvestrand, H., "Tags for the Identification of Languages", March 1995.
- **RFC 3066**: Alvestrand, H., "Tags for the Identification of Languages", BCP 47, January 2001.
- **UN M.49**: Statistics Division, United Nations, "Standard Country or Area Codes for Statistical Use", Revision 4, June 1999.
- **record-jar**: Raymond, E., "The Art of Unix Programming", 2003.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Code elements valid on the RFC 1766 reference date shall be added; withdrawn before that date shall not be added. | procedural rule | §2, criterion 1 |
| R2 | Subsequent assignments up to adoption of RFC 4646 shall be added; withdrawn values marked deprecated but not removed. | procedural rule | §2, criterion 2 |
| R3 | UN M.49 numeric macro-geographical region codes as of adoption shall be added. | procedural rule | §2, criterion 3 |
| R4 | UN M.49 economic/other groupings and alphanumeric codes in Appendix X shall not be added. | procedural rule | §2, criterion 4 |
| R5 | UN M.49 codes for countries/areas without ISO 3166-1 alpha-2 shall not be added; they may be registered individually. | procedural rule | §2, criterion 5 |
| R6 | Withdrawn/vacated/deprecated UN M.49 codes as of adoption shall not be added. | procedural rule | §2, criterion 6 |
| R7 | Non-deprecated RFC 3066 tags composed of defined subtags with correct format shall be converted to type "redundant". | procedural rule | §2, criterion 7 |
| R8 | RFC 3066 tags containing undefined or invalid subtags shall be converted to type "grandfathered". | procedural rule | §2, criterion 8 |
| R9 | Deprecated RFC 3066 tags shall be converted to "grandfathered" with deprecation date and preferred value. | procedural rule | §2, criterion 9 |
| R10 | Eligible variant subtags (1901, 1996, nedis, rozaj) shall be registered; tags using them shall become "redundant". | procedural rule | §2, criterion 10 |
| R11 | Remaining RFC 3066 tags shall be "grandfathered"; variant subtags may be registered later, superseding the tag. | procedural rule | §2, criterion 11 |

## Informative Annexes (Condensed)
None present in this document.