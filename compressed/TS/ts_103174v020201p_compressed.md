# ETSI TS 103 174: Electronic Signatures and Infrastructures (ESI); ASiC Baseline Profile
**Source**: ETSI | **Version**: V2.2.1 | **Date**: 2013-06 | **Type**: Normative (Technical Specification)
**Original**: ETSI TS 103 174 V2.2.1 (2013-06)

## Scope (Summary)
Defines a baseline profile for ASiC containers (based on TS 102 918) to maximise interoperability for electronic signatures and time‑stamp tokens across borders. Specifies three conformance levels (B‑Level, T‑Level, LT‑Level) aligned with CAdES [3] and XAdES [4] profiles, addressing incremental requirements for long‑term validity. Particularly addresses the EU Services Directive [i.3].

## Normative References
- [1] ETSI TS 101 733: "CMS Advanced Electronic Signatures (CAdES)"
- [2] ETSI TS 101 903: "XML Advanced Electronic Signatures (XAdES)"
- [3] ETSI TS 103 173: "CAdES Baseline Profile"
- [4] ETSI TS 103 171: "XAdES Baseline Profile"
- [5] ETSI TS 102 176-1: "Algorithms and Parameters for Secure Electronic Signatures; Part 1: Hash functions and asymmetric algorithms"
- [6] ETSI TS 102 918: "Associated Signature Containers (ASiC)"
- [7] ETSI TS 101 861: "Time stamping profile"

## Informative References (Condensed)
- [i.1] RFC 3161 (TSP)
- [i.2] .ZIP Application Note (PKWARE)
- [i.3] Directive 2006/123/EC (EU Services Directive)
- [i.4] ECRYPT II Yearly Report on Algorithms and Keysizes
- [i.5] TS 101 533-1 (Data Preservation Systems Security)
- [i.6] TS 102 640-1 (Registered Electronic Mail)
- [i.7] Commission Decision 2011/130/EU (cross‑border processing of electronic signatures)

## Definitions and Abbreviations
### Definitions
- **generator**: any party which creates, or adds attributes to, a signature (may be signatory or verifier/maintainer)
- **protocol element**: element of the protocol which may include data elements and/or elements of procedure
- **service element**: element of service that may be provided using one or more protocol elements (all alternatives provide equivalent service)
- **verifier**: entity that validates or verifies an electronic signature

### Abbreviations
As given in CAdES [1], XAdES [2], and ASiC [6] apply.

## Conformance Levels
- **B‑Level**: Signatures conforming to clause 6 of [3] or [4] (as applicable). Sufficient for Commission Decision 2011/130/EU [i.7].
- **T‑Level**: B‑Level plus signatures conforming to clause 7 of [3] or [4] (trusted time for signature existence).
- **LT‑Level**: T‑Level plus signatures conforming to clause 8 of [3] or [4] (long‑term validation material).
- No LTA‑Level is defined because ASiC [6] (V1.2.1) does not yet support it; a future revision is anticipated.

When signed data is exchanged, the sender **should** use at least a level that allows the relying parties to trust the signature at the time of exchange. LT‑Level is sufficient when combined with appropriate preservation/transmission techniques.

## General Requirements
### 5.1 Algorithm Requirements
- Generators shall follow applicable national laws for algorithms and key lengths.
- Generators are **recommended** to consult the latest TS 102 176‑1 [5] and ECRYPT II [i.4] reports.
- **MD5 algorithm shall not be used** as digest algorithm.
- For CAdES and XAdES signatures, the respective profiles ([3] and [4]) **shall** apply.

### 5.2 Compliance Requirements
- **Verifier shall accept** ASiC containers with any elements/properties conformant to XAdES [2] or CAdES [1], but no processing requirements are specified in this profile.
- Requirement categories:
  - **M**: Generator **shall** include the element.
  - **O**: Generator **may** include the element.
- Optional elements from ASiC [6] not specified here are treated as "O".
- Elements from CAdES/XAdES not specified here are treated as per the baseline profiles.
- For mandatory/optional services with multiple protocol choices, see Tables 2 and 3 (definitions in original).

## Requirements for ASiC Formats
### 6.1 ASiC Conformance
A conformant implementation may support a single ASiC type. Table 5 requirements (service M, protocol choices O):

| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| **Service:** ASiC | – | M | |
| ASiC‑S CAdES | Clause 7.1.1 | O | |
| ASiC‑S XAdES | Clause 7.1.2 | O | |
| ASiC‑S Time‑stamp token | Clause 7.1.3 | O | |
| ASiC‑E XAdES | Clause 7.2.1 | O | |
| ASiC‑E CAdES | Clause 7.2.2 | O | |
| ASiC‑E Time‑stamp | Clause 7.2.3 | O | |
*Note: Generator and verifier may implement one or more options; documentation shall reference applicable TS 102 918 clause(s).*

## Requirements for ASiC‑S
### 7.1 ASiC‑S Media Type Identification
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| **Service:** ASiC‑S Media type identification | – | M | |
| ASiC file extension is ".asics" | Clause 5.2.1 | O | |
| ASiC file extension is ".scs" | Clause 5.2.1 | O | |
| mimetype | Clauses 5.2.1 and A.1 | O | |

### 7.2 ASiC‑S Signed Data Object
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| Signed data object | Clause 5.2.2 point 2 | M | a) This protocol element **shall** be the only element, with an arbitrary name, in the root container folder. |

### 7.3 Requirements for ASiC‑S Format
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| **Service:** ASiC‑S format | – | M | |
| META‑INF/timestamp.tst | Clause 5.2.2 point 3a | O | Clause 6.3.1 shall apply |
| META‑INF/signature.p7s | Clause 5.2.2 point 3b | O | Clause 6.3.2 shall apply |
| META‑INF/signatures.xml | Clause 5.2.2 point 3c | O | Clause 6.3.3 shall apply |

#### 7.3.1 ASiC‑S CAdES Signature Format
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/signature.p7m | Clause 5.2.2 point 3b | M | a) The CAdES [1] signature **shall** conform to CAdES baseline profile [3], clause 5 and all subclauses, except subclause 5.1.1 where only the detached signature service shall be supported. |

#### 7.3.2 ASiC‑S XAdES Signature Format
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/signatures.xml | Clause 5.2.2 point 3c | M | a) **shall** contain a `<asic:XAdESSignatures>` element as per TS 102 918 [6], point 3a. b) Each XAdES [2] element **shall** reference the signed data object using `<ds:Reference>`. |

#### 7.3.3 ASiC‑S Time Stamp Token Format
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/timestamp.tst | Clause 5.2.2 point 3a | M | a) **shall** conform to TS 101 861 [7]. |

## Requirements for ASiC‑E
### 8.1 ASiC‑E Media Type Identification
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| **Service:** ASiC‑E Media type identification | – | M | |
| ASiC file extension is ".asice" | Clause 6.2.1 | O | |
| ASiC file extension is ".sce" | Clause 6.2.1 | O | |
| mimetype | Clause 6.2.1 | O | |

### 8.2 ASiC‑E Signed Data Object
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| Signed data object | Clause 6.2.2 | M | At least one signed data object **shall** be in the container outside the META‑INF folder. |

### 8.3 Requirements for ASiC‑E XAdES
#### 8.3.1 ASiC‑E XAdES Signature
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| ASiC‑E XAdES signature | Clause 6.2.2 point 2 | M | a) At least one signature **shall** be present in META‑INF conforming to TS 102 918 [6], point 2. b) Root element shall contain `<asic:XAdESSignatures>` as per clause 6.2.2 point 3a. c) Each XAdES element **shall** directly reference all signed data objects with `<ds:Reference>` elements. |

#### 8.3.2 Requirements for the contents of Container
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/manifest.xml | Clause 6.2.2 point 4b | M | a) No additional data objects shall be present in META‑INF beyond those specified in this clause and in clause 7.3.1. |

### 8.4 Requirements for ASiC‑E CAdES
#### 8.4.1 ASiC‑E CAdES Signature
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| ASiC‑E CAdES signature | Clause 6.3.2 point 4a | M | a) At least one signature **shall** be present in META‑INF as per TS 102 918 [6], clause 6.3.2 point 4a. b) Each CAdES [1] signature **shall** conform to CAdES baseline profile [3], clause 5 and all subclauses, except clause 5.1.1 where only detached signature service shall be supported. |

#### 8.4.2 Requirements for the contents of Container
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/AsiCManifest | Clause 6.3.2 point 3 | M | a) At least one AsiCManifest **shall** be present. b) No additional data objects in META‑INF beyond those specified in this clause and in clause 7.4.1. |

### 8.5 Requirements for ASiC‑E Time Stamp Token
#### 8.5.1 Requirements on Time Stamp Tokens
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| ASiC‑E Time stamp token | Clause 6.3.2 point 4b | M | a) At least one time stamp token **shall** be present in META‑INF as per TS 102 918 [6], clause 6.3.2 point 4b. b) Each time stamp token **shall** conform to TS 101 861 [7]. |

#### 8.5.2 Requirements for the contents of Container
| Service/Protocol element | ASiC [6] reference | Generator requirement | Additional requirements/notes |
|---|---|---|---|
| META‑INF/AsiCManifest | Clause 6.3.2 point 3 | M | a) At least one AsiCManifest **shall** be present. b) No additional objects in META‑INF beyond those specified in this clause and in clause 7.5.1. |

## Informative Annexes (Condensed)
- **Annex A (referenced in clauses)**: Defines mimetype and file extension details. The profile uses the standard ASiC structure from TS 102 918; the specific extensions (.asics, .scs, .asice, .sce) and mimetype are recommended.
- **Intellectual Property Rights (IPR)**: ETSI SR 000 314 provides information on essential IPRs; no investigation performed.
- **Foreword**: TS produced by ETSI TC ESI.
- **Introduction**: Explains motivation for profiling ASiC to maximise interoperability, especially under EU Services Directive.
- **History**: V1.1.1 (2011-09), V1.2.1 (2012-01), V2.1.1 (2012-03), V2.2.1 (2013-06).