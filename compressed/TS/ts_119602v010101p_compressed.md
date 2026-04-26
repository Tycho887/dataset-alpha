# ETSI TS 119 602 V1.1.1: Electronic Signatures and Trust Infrastructures (ESI); Lists of trusted entities; Data model
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2025-11 | **Type**: Normative Technical Specification
**Original**: DTS/ESI-0019602 (available from ETSI Search & Browse Standards)

## Scope (Summary)
Defines a data model for lists of trusted entities (LoTEs), including syntax bindings (XML, JSON) and profiles for EU-specific lists (e.g., PID providers, wallet providers, etc.). The model generalizes existing trusted lists from ETSI TS 119 612 and aims to support representation of approval statuses for any community.

## Normative References
- [1] ETSI TS 119 612 (V2.4.1): "Trusted Lists"
- [2] ISO 3166-1:2020: Country codes
- [3] ETSI TS 119 182-1 (V1.2.1): JAdES signatures
- [4] ETSI EN 319 132-1 (V1.3.1): XAdES signatures
- [5] ISO/IEC 10646:2020: Universal coded character set (UCS)
- [6] ISO/IEC 6429:1992: Control functions
- [7] ISO/IEC 2022:1994: Character code structure
- [8] ISO 8601:2019 (parts 1 and 2): Date and time
- [9] IETF RFC 3986: URI generic syntax
- [10] IETF RFC 4514: LDAP Distinguished Names
- [11] IETF RFC 5646: Language tags
- [12] Recommendation ITU-T X.509: Public-key infrastructure
- [13] IETF RFC 2368: mailto URL scheme
- [14] IETF RFC 3966: tel URI scheme
- [15] ETSI EN 319 412-1 (V1.6.1): Certificate profiles

## Definitions and Abbreviations
- **List of Trusted Entities (LoTE)**: A list conveying trust in entities providing services under an approval scheme.
- **Approval scheme**: Organized process of supervision/approval to ensure adherence to criteria.
- **Trusted entity (TE)**: Entity recognized as trustworthy for a specific scope/purpose.
- **LoTE scheme operator (LoTESO)**: Body responsible for operating/managing the approval scheme and publishing the LoTE.
- **Provider of person identity data**: As defined in Regulation (EU) 910/2014.
- **Provider of relying party access certificate**: As defined in Regulation (EU) 910/2014.
- **Provider of relying party registration certificate**: As defined in Regulation (EU) 910/2014.
- **Wallet provider**: As defined in Regulation (EU) 910/2014.
- Abbreviations: CC, EU, HTTP, LoTE, LoTESO, MS, PID, Pub-EAA, TE, URI, WRPAC, WRPRC, XML

## 4 General Concepts
### 4.1 List of Trusted Entities (LoTE)
LoTE conveys trust in entities providing services within a given approval scheme. It lists entities granted a particular status. Assessment process is out of scope.

### 4.2 Approval scheme
Organized process of supervision/approval.

### 4.3 Trusted entities
Entity recognized as trustworthy; can be legal/natural persons or objects.

### 4.4 Trusted entity services
Service entries with type identifier giving scope of recognition.

### 4.5 List of Trusted Entities Scheme Operator
LoTESO: body responsible for establishing, maintaining, publishing the LoTE.

### 4.6 Syntax bindings
Instantiation of LoTE data model into specific syntax (XML, JSON). Annex A provides bindings.

### 4.7 LoTE profiles
Scheme-defined constraints on LoTE elements (optional elements may be made mandatory/forbidden). Mandatory elements cannot be made optional.

## 5 Overall Structure of Lists of Trusted Entities
LoTE logical model comprises:
1. **Tag**: facilitates identification (clause 6.2)
2. **Scheme information**: version, sequence number, type, operator info, scheme details (clause 6.3)
3. **TE information**: for each TE, identification details (clause 6.5)
4. **Service information**: details of each TE service (clause 6.6)
5. **Service approval history**: optional, status history (clause 6.7)
6. **Digital signature**: AdES signature (clause 6.8)

Structure shall have exactly one occurrence of 1,2,6; others may repeat.

## 6 List of Trusted Entities Components
### 6.1 General Principles
#### 6.1.1 Formats
Bindings in XML and JSON per Annex A. Additional bindings may be defined in future versions.

#### 6.1.2 Use of URIs
Fields using URIs shall conform to IETF RFC 3986. Common names linked to Annex C.

#### 6.1.3 Date-time Indication
All date-time values **shall** be formatted per ISO 8601, expressed as UTC with "Z" designator, year/month/day/hour/minute/second (no fractions).

#### 6.1.4 Language Support
LoTE **shall** be issued supporting at least UK English (code 'en'). May support multiple languages. Multilingual character strings consist of language tag (RFC 5646, lowercase) and UTF-8 encoded text. Multilingual pointers consist of language tag and URI. When native terms cannot be represented in Latin alphabet, provide native + transliteration.

#### 6.1.5 Value of Country Code Fields
CC fields **shall** be capital letters per ISO 3166-1 Alpha-2 with exceptions:
- UK for United Kingdom
- EL for Greece
- EU for European Union/Commission
Or commonly used extensions (AP, ASIA) or other non-conflicting identifiers.

### 6.2 List of Trusted Entities Tag
- **LoTE Tag**: character string indicating LoTE. **Shall** be a URI. Enables web search to identify resource as a LoTE.

### 6.3 List and Scheme Information
#### 6.3.0 General
- Scheme info may be implicit or explicit.
- If implicit: LoTE **shall** contain at least LoTEVersionIdentifier, LoTESequenceNumber, SchemeOperatorName, ListIssueDateTime, NextUpdate.
- If explicit: additionally LoTEType, SchemeInformationURI, StatusDeterminationApproach, SchemeTypeCommunityRules, SchemeTerritory, PolicyOrLegalNotice.
- Table 1 defines mandatory (M), optional (O), disallowed (/) for each element.

#### 6.3.1 LoTE version identifier
- **LoTEVersionIdentifier**: integer. Incremented only when parsing rules change.

#### 6.3.2 LoTE sequence number
- **LoTESequenceNumber**: integer. First release = 1. Incremented at each release; never recycled.

#### 6.3.3 LoTE type
- **LoTEType**: URI. Unique per profile. Registered URIs in Annex C.

#### 6.3.4 Scheme operator name
- **SchemeOperatorName**: sequence of multilingual character strings. Formal name of entity establishing/maintaining LoTE.

#### 6.3.5 Scheme operator address
**General**: contains PostalAddresses and ElectronicAddress.

**6.3.5.1 Postal address**: sequence of multilingual PostalAddress components. Each mandatory: StreetAddress (string), Country (two-char code per 6.1.5(a)); optional: Locality, StateOrProvince, PostalCode.

**6.3.5.2 Electronic address**: sequence of multilingual strings. Mandatory: email URI (RFC 2368), website URI; optional: telephone URI (RFC 3966).

#### 6.3.6 Scheme name
- **SchemeName**: multilingual character strings. English version format: "CC:EN_name_value". National versions: "CC:name_value". Name shall be unique.

#### 6.3.7 Scheme information URI
- **SchemeInformationURI**: sequence of multilingual pointers. Provides info on scope, approval process, criteria, etc. May include archived lists.

#### 6.3.8 Status determination approach
- **StatusDeterminationApproach**: URI.

#### 6.3.9 Scheme type/community/rules
- **SchemeTypeCommunityRules**: sequence of multilingual pointers. Identifies policy/rules for assessment and usage of list.

#### 6.3.10 Scheme territory
- **SchemeTerritory**: character string per 6.1.5.

#### 6.3.11 LoTE policy/legal notice
- **PolicyOrLegalNotice**: either sequence of multilingual pointers (LoTEPolicy) or multilingual character strings (LoTELegalNotice). Describes policy/legal status.

#### 6.3.12 Historical information period
- **HistoricalInformationPeriod**: integer. Value 65535 = never remove historical info. Absent = no historical info kept.

#### 6.3.13 Pointers to other LoTEs
- **PointersToOtherLoTE**: sequence of OtherLoTEPointer elements, each with a) URI of another LoTE, b) ServiceDigitalIdentity of issuer, c) qualifiers (LoTE type, scheme operator name, etc.).

#### 6.3.14 List issue date and time
- **ListIssueDateTime**: date-time per 6.1.3. UTC.

#### 6.3.15 Next update
- **NextUpdate**: date-time per 6.1.3. UTC. If scheme ceases, final version with all services "expired" and NextUpdate null.

#### 6.3.16 Distribution points
- **DistributionPoints**: non-empty sequence of URIs. Dereferencing delivers latest update. All copies identical.

#### 6.3.17 Scheme extensions
- **SchemeExtensions**: sequence of extensions with criticality indication (like X.509). Critical extensions must be recognized, else reject LoTE.

### 6.4 Trusted Entities List
#### 6.4.0 General
If no TE approved, component **shall not** be present. If at least one service approved, component **shall** be present. Contains sequence of TrustedEntity components.

#### 6.4.1 Trusted entity
Contains TrustedEntityInformation and TrustedEntityServices (sequence of TrustedEntityService components). Each service may have ServiceHistory.

#### 6.4.2 Trusted entity services
Sequence of TrustedEntityService components. When historical info required, at least one service shall be listed (even if historical).

#### 6.4.3 Trusted entity service
Contains ServiceInformation (mandatory) and optionally ServiceHistory (sequence of ServiceHistoryInstance). ServiceHistory present only when applicable.

#### 6.4.4 Service history
Sequence of ServiceHistoryInstance elements in descending order of status change.

### 6.5 Trusted Entity Information
#### 6.5.0 General
Mandatory: TEName, TEAddress, TEInformationURI. Optional: TETradeName, TEInformationExtensions.

#### 6.5.1 TE name
Sequence of multilingual character strings. Formal name used in legal registrations.

#### 6.5.2 TE trade name
Sequence of multilingual character strings. Shall include official registration identifier if exists. May include alternative name.

#### 6.5.3 TE address
Contains TEPostalAddress and TEElectronicAddress (same format as scheme operator, clauses 6.3.5.1 and 6.3.5.2).

#### 6.5.4 TE information URI
Sequence of multilingual pointers. Profiles should specify requirements on info at URI.

#### 6.5.5 TE information extensions
Sequence of TE extensions (format open). Includes **OtherAssociatedBodies** extension (clauses 6.5.5.1.0–6.5.5.1.7) that can list associated bodies with name, trade name, address, URI, type identifier, extensions.

### 6.6 Service Information
#### 6.6.0 General
Mandatory: ServiceName, ServiceDigitalIdentity. Optional: ServiceTypeIdentifier, ServiceStatus, StatusStartingTime, SchemeServiceDefinitionURI, ServiceSupplyPoint, TEServiceDefinitionURI, ServiceInformationExtensions.
- If HistoricalInformationPeriod present with non-zero, ServiceStatus **shall** be present.
- If ServiceTypeIdentifier absent, all services same type.
- If StatusStartingTime absent, verification only at current time.
- For PKI-based services, ServiceDigitalIdentity **shall** contain at least one X509Certificate.

#### 6.6.1 Service type identifier
URI. LoTE profiles should define/register URIs.

#### 6.6.2 Service name
Multilingual character strings.

#### 6.6.3 Service digital identity
May contain one or more: X509Certificate (Base64), X509SubjectName, PublicKeyValue, X509SKI, OtherId.
When using PKI, shall contain at least X509Certificate or X509SKI. organizationName in certificate should match TEName.

#### 6.6.4 Service current status
URI. Profiles should define status values.

#### 6.6.5 Current status starting date and time
Date-time per 6.1.3. Shall not be set before list issue date/time (no retroactive changes).

#### 6.6.6 Scheme service definition URI
Sequence of multilingual pointers.

#### 6.6.7 Service supply points
Non-empty sequence of URIs, optionally with type URI.

#### 6.6.8 TE service definition URI
Sequence of multilingual pointers.

#### 6.6.9 Service information extensions
Sequence of extensions. Includes **ServiceUniqueIdentifier** (URI) for unique service identification.

### 6.7 Service History Instance
Mandatory: ServiceName, ServiceDigitalIdentity, ServiceStatus, StatusStartingTime. Optional: ServiceTypeIdentifier, ServiceInformationExtensions.
ServiceDigitalIdentity shall contain applicable identifiers from that time (at least X509SKI if PKI).

### 6.8 Digital Signature
LoTE **shall** be signed with AdES digital signature at conformance level Baseline B. Signature may be within LoTE (via Signature component) or encapsulate LoTE. Subject distinguished name must match Scheme Territory and Scheme operator name.

#### 6.8.1 Signature component
Encapsulates the AdES signature.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | LoTE tag shall be a URI identifying the list. | shall | 6.2 |
| R2 | Date-time values shall be ISO 8601 UTC with "Z". | shall | 6.1.3 |
| R3 | LoTE shall support at least UK English (en). | shall | 6.1.4 |
| R4 | Country codes shall be ISO 3166-1 Alpha-2 except UK, EL, EU. | shall | 6.1.5 |
| R5 | In implicit scheme info, LoTEType shall not be present. | / | Table 1 |
| R6 | In explicit scheme info, LoTEType shall be present. | shall | 6.3.3 |
| R7 | SchemeOperatorName shall be formal name. | shall | 6.3.4 |
| R8 | LoTEVersionIdentifier integer increments only on parsing changes. | shall | 6.3.1 |
| R9 | LoTESequenceNumber starts at 1, never recycled. | shall | 6.3.2 |
| R10 | NextUpdate shall not be in the past; scheme may set null. | shall | 6.3.15 |
| R11 | If HistoricalInformationPeriod is non-zero, ServiceStatus shall be present. | shall | 6.6.0 |
| R12 | For PKI services, ServiceDigitalIdentity shall contain X509Certificate. | shall | 6.6.0 |
| R13 | Digital signature shall be AdES Baseline B. | shall | 6.8.0 |
| R14 | Signature Subject DN shall match Scheme Territory and Scheme operator name. | shall | 6.8.0 |
| R15 | Multilingual character strings shall be UTF-8 encoded, no control chars. | shall | B.1, B.2 |
| R16 | LoTE shall be signed with JAdES (JSON) or XAdES (XML) as per profile. | shall | Annexes D-I |

## Normative Annexes (Condensed)
- **Annex A (Bindings)**: Provides JSON and XML bindings for scheme-explicit LoTEs. Repositories: https://forge.etsi.org/rep/esi/x19_60201_lists_of_trusted_entities. In case of conflict, text of this TS prevails. A.2.2 maps components to ETSI TS 119 612 fields.
- **Annex B (Multilingual support)**: Specifies rules for language tags, character encoding (UTF-8), prohibited control characters, and handling of Latin transliteration for EU member states. Table B.1 lists language codes per Member State.
- **Annex C (Registered URIs)**: Lists URIs for LoTE types, status determination approaches, and scheme rules for EU-specific lists (PID, Wallet, WRPAC, WRPRC, Pub-EAA, Registrars). All under radix http://uri.etsi.org/19602/.
- **Annex D (Profile: PID providers list)**: JSON schema, explicit scheme, LoTEType = "http://uri.etsi.org/19602/LoTEType/EUPIDProvidersList". No historical info; ServiceStatus absent implies all notified. Signed with JAdES Baseline B.
- **Annex E (Profile: wallet providers list)**: Similar to D but for wallet providers. ServiceStatus absent implies all certified. ServiceUniqueIdentifier extension used for reference number.
- **Annex F (Profile: WRPAC providers list)**: For providers of wallet relying party access certificates. ServiceStatus absent implies all mandated.
- **Annex G (Profile: WRPRC providers list)**: For providers of wallet relying party registration certificates. Same pattern as F.
- **Annex H (Profile: Pub-EAA providers list)**: Historical information period = 65535 (never removed). ServiceStatus present (notified/withdrawn). May use JSON or XML binding. Signature: JAdES (JSON) or XAdES (XML) with enveloped signature.
- **Annex I (Profile: registrars and registers list)**: No historical info; ServiceStatus absent implies all mandated. ServiceSupplyPoint provides machine-readable register URI.