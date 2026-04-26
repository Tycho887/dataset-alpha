# ETSI TS 119 422: Electronic Signatures and Infrastructures (ESI); Time-stamping protocol and time-stamp profiles
**Source**: ETSI | **Version**: V1.0.1 | **Date**: July 2015 | **Type**: Normative Technical Specification  
**Original**: http://www.etsi.org/standards-search (ETSI TS 119 422 V1.0.1)

## Scope (Summary)
Defines a profile for the time-stamping protocol and time-stamp token defined in IETF RFC 3161 [1], including optional ESSCertIDv2 update in IETF RFC 5816 [2]. Specifies requirements for both time-stamping clients and servers. Time-stamp validation is out of scope (covered by ETSI TS 119 102-1 [i.6]).

## Normative References
- [1] IETF RFC 3161: "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)"
- [2] IETF RFC 5816: "ESSCertIDV2 update to RFC 3161"
- [3] ETSI TS 119 312: "Electronic Signatures and Infrastructures (ESI); Cryptographic Suites"
- [4] ETSI TS 119 412-2: "Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 2: Certificate profile for certificates issued to natural persons"
- [5] ETSI TS 119 412-3: "Electronic Signatures and Infrastructures (ESI); Certificate Profiles; Part 3: Certificate profile for certificates issued to legal persons"

## Definitions and Abbreviations
### Definitions
- **time-stamp**: data in electronic form which binds other electronic data to a particular time establishing evidence that these data existed at that time
- **time-stamp token**: data object defined in IETF RFC 3161 [1], representing a time-stamp
- **time-stamping authority**: Trust Service Provider which issues time-stamp using one or more time-stamping units
- **time-stamping unit**: set of hardware and software which is managed as a unit and has a single time-stamp signing key active at a time

### Abbreviations
- ASN: Abstract Syntax Notation
- EU: Europe
- HTTP: HyperText Transfer Protocol
- HTTPS: Hypertext Transfer Protocol over TLS
- OID: Object Identifier
- RFC: Request for Comments
- TLS: Transport Layer Security
- TSA: Time-Stamping Authority
- TSU: Time-Stamping Unit

## 4 Requirements for a time‑stamping client
### 4.1 Profile for the format of the request
#### 4.1.1 Core requirement
- A time‑stamping client **shall** support the time‑stamping request as defined in IETF RFC 3161 [1], clause 2.4.1, with amendments defined below.

#### 4.1.2 Parameters to be supported
- The following parameters **should** be supported: `reqPolicy`, `nonce`, `certReq`.

#### 4.1.3 Hash algorithms to be used
- Hash algorithms **should** be as specified in clause A.8 of ETSI TS 119 312 [3], taking into account expected duration of the time‑stamp and recommended hash functions versus time given in clause 9.2 of [3].

### 4.2 Profile for the format of the response
#### 4.2.1 Core requirement
- A time‑stamping client **shall** support the time‑stamping response as defined in IETF RFC 3161 [1], clause 2.4.2, with amendments defined below.

#### 4.2.2 Parameters to be supported
- The `accuracy` field **shall** be supported and understood.
- The `nonce` parameter **should** be supported.
- A TSU **need not** support ordering; clients **should not** depend on the ordering of time‑stamps.

#### 4.2.3 Algorithms to be supported
- Time‑stamp token signature algorithms **shall** be as specified in clause A.8 of ETSI TS 119 312 [3].

#### 4.2.4 Key lengths to be supported
- Key lengths **should** be supported as recommended in clause 9.3 of ETSI TS 119 312 [3].

## 5 Requirements for a time‑stamping server
### 5.1 Profile for the format of the request
#### 5.1.1 Core requirement
- A time‑stamping server **shall** support the request as defined in IETF RFC 3161 [1], clause 2.4.1, with amendments below.

#### 5.1.2 Parameters to be supported
- `reqPolicy` **shall** be supported.
- `nonce` **shall** be supported.
- `certReq` **shall** be supported.

#### 5.1.3 Algorithms to be supported
- Hash algorithms **shall** be as specified in clause A.8 of ETSI TS 119 312 [3], taking into account expected duration and recommendations in clause 9.2 of [3].

### 5.2 Profile for the format of the response
#### 5.2.1 Core requirement
- A time‑stamping server **shall** support the response as defined in IETF RFC 3161 [1] clause 2.4.2, with amendments below.

#### 5.2.2 Parameters to be supported
- Requirements from IETF RFC 3161 [1] clause 2.4.2 apply, plus:
  - `policy` **shall** be present as identifier for time‑stamp policy and **shall** conform to annex A.
  - `genTime` representing time with precision necessary to support declared accuracy **shall** be supported.
  - `accuracy` **shall** be present; minimum accuracy of one second **shall** be supported.
  - `ordering` **shall** not be present or **shall** be set to false.
  - No extension **shall** be critical.
  - In the SignedData structure: the certificate identifier of the TSU certificate (ESSCertID as in [1] or ESSCertIDv2 as in [2]) **shall** be included as a signerInfo attribute inside a SigningCertificate attribute.

#### 5.2.3 Algorithms to be used
- Hash algorithms and time‑stamp token signature algorithms **shall** be as specified in clause A.8 of ETSI TS 119 312 [3].

## 6 TSU certificate profile
### 6.1 General requirements
- The TSU certificate **shall** be as defined in ETSI TS 119 412‑2 [4] (natural person) or ETSI TS 119 412‑3 [5] (legal person) with amendments below.

### 6.2 Subject name requirements
- `countryName` **shall** specify the country where the TSA is established (not necessarily location of TSU).
- `organizationName`, when applicable, **shall** contain the full registered name of the TSA responsible for managing the TSU; name **should** be officially registered.
- For legal person, `organizationIdentifier` **should** be used as defined in Recommendation ITU‑T X.520 [i.4].
- `commonName` **shall** be present; it specifies an identifier for the TSU; within the TSA, it uniquely identifies the TSU.
- For natural person, `serialNumber` **should** be used.
- Additional attributes **may** be present.

### 6.3 Key lengths requirements
- Key length for the selected signature algorithm **should** be as recommended in clause 9.3 of ETSI TS 119 312 [3].

### 6.4 Key usage requirements
- The TSU certificate key usage **shall** be as defined in IETF RFC 3161 [1], clause 2.3.

### 6.5 Algorithm requirements
- The TSU public key and certificate signature **should** use algorithms as specified in clause A.9 of ETSI TS 119 312 [3].

## 7 Profiles for the transport protocols to be supported
- The time‑stamp client and server **shall** support the time‑stamp protocol via HTTP or HTTPS as defined in clause 3.4 of IETF RFC 3161 [1].

## 8 Object identifiers of the cryptographic algorithms
- OIDs for recommended hashing and signature algorithms are specified in annex F of ETSI TS 119 312 [3].

## 9 Additional requirements for Regulation (EU) No 910/2014
### 9.1 Regulation statement
- When a time‑stamp token is a qualified electronic time‑stamp per Regulation (EU) No 910/2014 [i.3], it **should** contain one instance of the `qcStatements` extension with syntax as defined in IETF RFC 3739 [i.5], clause 3.2.6.
- If the `qcStatements` extension is present, it **shall** contain one instance of the statement `esi4-qtstStatement-1` defined in annex B.

## Annex A (normative): Structure for the policy field
When the time‑stamp token is issued by a TSA that conforms to ETSI TS 119 421 [i.1], the policy field in TSTInfo **shall** include:
- `itu-t(0) identified-organization(4) etsi(0) time-stamp-policy (2023) policy-identifiers(1) baseline-ts-policy (1)`  
  **or**
- TSA’s own identifier when the TSA incorporates or further constrains the above policy.

## Annex B (normative): ASN.1 declarations
```asn1
-- object identifiers
id-etsi-tsts OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0) id-tst-profile(19422) 1 }
id-etsi-tsts-EuQCompliance OBJECT IDENTIFIER ::= { id-etsi-tsts 1 }

-- statements
esi4-qtstStatement-1 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-tsts-EuQCompliance }

-- By inclusion of this statement the issuer asserts that this
-- time-stamp token is issued as a qualified electronic time-stamp according to
-- the REGULATION (EU) No 910/2014.
```

## Requirements Summary
| ID | Requirement (Condensed) | Type | Reference |
|----|------------------------|------|-----------|
| R1 | Client shall support TSP request per RFC 3161 §2.4.1 | shall | 4.1.1 |
| R2 | Client should support reqPolicy, nonce, certReq | should | 4.1.2 |
| R3 | Client hash algorithms per TS 119 312 §A.8 | should | 4.1.3 |
| R4 | Client shall support TSP response per RFC 3161 §2.4.2 | shall | 4.2.1 |
| R5 | Client shall support accuracy field | shall | 4.2.2 |
| R6 | Client should support nonce parameter | should | 4.2.2 |
| R7 | Client should not depend on ordering | should not | 4.2.2 |
| R8 | Client signature algorithms per TS 119 312 §A.8 | shall | 4.2.3 |
| R9 | Client key lengths per TS 119 312 §9.3 | should | 4.2.4 |
| R10 | Server shall support TSP request per RFC 3161 §2.4.1 | shall | 5.1.1 |
| R11 | Server shall support reqPolicy, nonce, certReq | shall | 5.1.2 |
| R12 | Server hash algorithms per TS 119 312 §A.8 | shall | 5.1.3 |
| R13 | Server shall support TSP response per RFC 3161 §2.4.2 | shall | 5.2.1 |
| R14 | Policy parameter shall be present and conform to Annex A | shall | 5.2.2 |
| R15 | genTime shall be supported | shall | 5.2.2 |
| R16 | accuracy shall be present (min 1 second) | shall | 5.2.2 |
| R17 | ordering shall not be present or false | shall | 5.2.2 |
| R18 | No critical extensions | shall | 5.2.2 |
| R19 | TSU certificate identifier in SigningCertificate attribute | shall | 5.2.2 |
| R20 | Server signature algorithms per TS 119 312 §A.8 | shall | 5.2.3 |
| R21 | TSU certificate per TS 119 412-2 or -3 | shall | 6.1 |
| R22 | countryName = country of TSA establishment | shall | 6.2 |
| R23 | organizationName (if applicable) shall be full registered name | shall | 6.2 |
| R24 | organizationIdentifier should be used for legal persons | should | 6.2 |
| R25 | commonName shall be present and identify TSU uniquely within TSA | shall | 6.2 |
| R26 | serialNumber should be used for natural persons | should | 6.2 |
| R27 | Key lengths per TS 119 312 §9.3 | should | 6.3 |
| R28 | Key usage per RFC 3161 §2.3 | shall | 6.4 |
| R29 | Algorithms per TS 119 312 §A.9 | should | 6.5 |
| R30 | Transport via HTTP/HTTPS per RFC 3161 §3.4 | shall | 7 |
| R31 | Qualified e‑time‑stamp: qcStatements extension with esi4-qtstStatement-1 | should / shall | 9.1 |
| R32 | Policy OID for TSA conforming to TS 119 421 | shall | Annex A |

## Informative Annexes (Condensed)
- **Foreword & Introduction**: This TS replaces ETSI TS 101 861 [i.2] and aims to meet requirements of Regulation (EU) No 910/2014 [i.3]. Time‑stamping is critical for digital signatures; this profile limits options in IETF RFC 3161 [1].
- **Intellectual Property Rights**: IPRs may have been declared; see SR 000 314. No investigation for other IPRs.
- **History**: Previously published as TS 101 861 (versions V1.1.1 to V1.4.1), then as TS 119 422 V1.0.1 (June 2015).