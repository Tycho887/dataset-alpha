# ETSI TS 119 192: Electronic Signatures and Infrastructures (ESI); AdES related Uniform Resource Identifier
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2023-02 | **Type**: Technical Specification (Normative)
**Original**: http://www.etsi.org/standards-search

## Scope (Summary)
This document defines the root URI `http://uri.etsi.org/ades` and sub-branches for URIs applicable to multiple AdES signature formats (CAdES, XAdES, PAdES, JAdES) and the ASiC container. It specifies how to construct URIs for signature levels, versions, and attributes/properties. URIs are unique identifiers, not locators.

## Normative References
- [1] ETSI TS 103 171: "XAdES Baseline Profile"
- [2] ETSI TS 103 172: "PAdES Baseline Profile"
- [3] ETSI TS 103 173: "CAdES Baseline Profile"
- [4] ETSI TS 103 174: "ASiC Baseline Profile"
- [5] ETSI EN 319 122-1: "CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures"
- [6] ETSI EN 319 122-2: "CAdES digital signatures; Part 2: Extended CAdES signatures"
- [7] ETSI TS 119 122-3: "CAdES digital signatures; Part 3: Incorporation of ERS mechanisms in CAdES"
- [8] ETSI EN 319 132-1: "XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures"
- [9] ETSI EN 319 132-2: "XAdES digital signatures; Part 2: Extended XAdES signatures"
- [10] ETSI TS 119 132-3: "XAdES digital signatures; Part 3: Incorporation of ERS mechanisms in XAdES"
- [11] ETSI EN 319 142-1: "PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures"
- [12] ETSI EN 319 142-2: "PAdES digital signatures; Part 2: Additional PAdES signatures profiles"
- [13] ETSI EN 319 162-1: "ASiC; Part 1: Building blocks and ASiC baseline containers"
- [14] Void.
- [15] ETSI TS 119 182-1: "JAdES digital signatures; Part 1: Building blocks and JAdES baseline signatures"

## Informative References
- [i.1] ETSI TR 119 000: "The framework for standardization of signatures: overview"
- [i.2] Commission Implementing Decision (EU) 2015/1506
- [i.3] ETSI TR 119 001: "The framework for standardization of signatures; Definitions and abbreviations"

## Definitions and Abbreviations
- **AdES (digital) signature**: digital signature that is either a CAdES, PAdES, XAdES, or JAdES signature
- **JAdES signature**: JSON Web Signature (as defined in ETSI TS 119 182-1 [15])
- **signature class**: set of signatures achieving a given functionality
- **signature level**: format specific definition of a set of data incorporated into a digital signature, which allows to implement a signature class
- **CID**: Commission Implementation Decision
- **URI**: Uniform Resource Identifier

## 4 URI namespaces
### 4.1 The main branch
- **R1**: Any URI under the root `http://uri.etsi.org/ades` **shall** be used to describe URIs applicable for all types of AdES signatures.

### 4.2 URIs used to describe signature levels
#### 4.2.1 Baseline signature and container levels as defined in the standardization framework for signatures ETSI TR 119 000
- **R2**: A URI describing a baseline signature level (defined in [5][8][11]) or a baseline container level (defined in [13]) **shall** be built in the following way:  
  `http://uri.etsi.org/ades/191x2/level/baseline/<name-of-the-baselinelevel>#`  
  where `191x2` indicates the level is defined in all signature format documents with number x19 1x2; `level` states this URI defines a signature level; `baseline` states it defines a baseline signature level.
- **R3**: The following URIs are defined:
  - `http://uri.etsi.org/ades/191x2/level/baseline/B-B#` **shall** denote a B-B level (as defined in [5][8][11][13][15])
  - `http://uri.etsi.org/ades/191x2/level/baseline/B-T#` **shall** denote a B-T level (as defined in [5][8][11][13][15])
  - `http://uri.etsi.org/ades/191x2/level/baseline/B-LT#` **shall** denote a B-LT level (as defined in [5][8][11][13][15])
  - `http://uri.etsi.org/ades/191x2/level/baseline/B-LTA#` **shall** denote a B-LTA level (as defined in [5][8][11][13][15])
- **NOTE**: For ASiC levels see [13] clause 5.1.

#### 4.2.2 Baseline signature and container levels as defined in the CID 2015/1506
- **R4**: A URI describing a baseline signature level (defined in [1][2][3]) or a baseline container level (defined in [4]) as referenced in [i.2] **shall** be built in the following way:  
  `http://uri.etsi.org/ades/etsits/level/baseline/<name-of-the-baselinelevel>#`  
  where `etsits` indicates the level is defined in all signature format documents with number x19 1x2; `level` and `baseline` as above.
- **R5**: The following URIs are defined:
  - `http://uri.etsi.org/ades/etsits/level/baseline/B-B#` **shall** denote a B level ([1][2][3][4])
  - `http://uri.etsi.org/ades/etsits/level/baseline/B-T#` **shall** denote a T level ([1][2][3][4])
  - `http://uri.etsi.org/ades/etsits/level/baseline/B-LT#` **shall** denote an LT level ([1][2][3][4])
  - `http://uri.etsi.org/ades/etsits/level/baseline/B-LTA#` **shall** denote an LTA level ([1][2][3])
- **NOTE 1**: For ASiC levels see [4] clause 4.
- **NOTE 2**: No LTA level for ASiC is defined in [4].

#### 4.2.3 Extended signature levels as defined in the standardization framework for signatures ETSI TR 119 000
- **R6**: A URI describing an extended signature level defined in more than one of [6][9][12] **shall** be built as:  
  `http://uri.etsi.org/ades/191x2/level/extended/<name-of-the-extendedlevel>#`  
  where `191x2` indicates the level is defined in more than one document; `level` and `extended` as indicated.
- **R7**: The following URIs are defined:
  - `http://uri.etsi.org/ades/191x2/level/extended/E-BES#` **shall** denote E-BES level ([6][9][12])
  - `http://uri.etsi.org/ades/191x2etsits/level/extended/E-EPES#` **shall** denote E-EPES level ([6][9][12])
  - `http://uri.etsi.org/ades/191x2/level/extended/E-T#` **shall** denote E-T level ([6][9])
  - `http://uri.etsi.org/ades/191x2/level/extended/E-A#` **shall** denote E-A level ([6][9])
  - `http://uri.etsi.org/ades/191x2/level/extended/E-ERS#` **shall** denote E-ERS level ([7][10])

### 4.3 How to reference specific signature format version
- **R8**: To reference a specific version of a signature format or an ASiC container, the URI **shall** have the structure:  
  `http://uri.etsi.org/<number_of_the_document>/<specific_version>`  
  where `number_of_the_document` **shall** be the five-digit number obtained by removing the first digit of the ETSI document number, and any part or sub-part numbers.  
  `specific_version` **shall** be of format `vx.y.z` where x.y.z are the three digits used to identify an ETSI document version.
- **Example**: Version V1.1.1 of [5] is referenced as `http://www.etsi.org/19122/v1.1.1`.

### 4.4 How to reference specific attribute/properties in an AdES signature
- **R9**: To reference a specific attribute/property of a signature format or ASiC container, the URI **shall** have the structure:  
  `http://uri.etsi.org/<number_of_the_document>/<specific_version>/<name_of_the_attribute_or_property>`  
  where `number_of_the_document` and `specific_version` as defined in clause 4.3, and `name_of_the_attribute_or_property` **shall** be the name as used within the specific ETSI document.
- **Example**: The signature-time-stamp as defined in [5] is referenced as `http://uri.etsi.org/19122/v1.1.1/signature-time-stamp`.
- **NOTE 1**: A signature attribute or property is always specified together with the version of the ETSI document in which it is defined.
- **NOTE 2**: In case of an ASiC container, a specific attribute/property of a signature format can be referenced as specified in this clause.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Any URI under `http://uri.etsi.org/ades` shall be used to describe URIs applicable for all types of AdES signatures. | shall | 4.1 |
| R2 | URI for baseline signature/container level (TR 119 000) shall be built as `http://uri.etsi.org/ades/191x2/level/baseline/<name>#` | shall | 4.2.1 |
| R3 | Specific URIs for B-B, B-T, B-LT, B-LTA are defined. | shall | 4.2.1 |
| R4 | URI for baseline signature/container level (CID 2015/1506) shall be built as `http://uri.etsi.org/ades/etsits/level/baseline/<name>#` | shall | 4.2.2 |
| R5 | Specific URIs for B-B, B-T, B-LT, B-LTA are defined. | shall | 4.2.2 |
| R6 | URI for extended signature level shall be built as `http://uri.etsi.org/ades/191x2/level/extended/<name>#` | shall | 4.2.3 |
| R7 | Specific URIs for E-BES, E-EPES, E-T, E-A, E-ERS are defined. | shall | 4.2.3 |
| R8 | Version referencing URI shall be `http://uri.etsi.org/<number_of_the_document>/vx.y.z` | shall | 4.3 |
| R9 | Attribute/property referencing URI shall be `http://uri.etsi.org/<number>/<version>/<name>` | shall | 4.4 |

## Informative Annexes (Condensed)
- **Annex A (Change History)**: Lists changes between versions: in January 2023, JAdES was included in corresponding URIs, references to ETSI TS 119 182 were updated with "-1", and an unnecessary semicolon was removed.