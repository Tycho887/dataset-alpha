# ETSI TS 101 861 V1.4.1: Time stamping profile
**Source**: ETSI Technical Committee Electronic Signatures and Infrastructures (ESI) | **Version**: V1.4.1 | **Date**: July 2011 | **Type**: Normative Technical Specification
**Original**: [ETSI TS 101 861](http://www.etsi.org)

## Scope (Summary)
Based on IETF RFC 3161 [1] including ESSCertIDv2 update RFC 5816 [9]. Defines mandatory support requirements for Time Stamping Protocol (TSP) clients and servers.

## Normative References
- [1] IETF RFC 3161: "Internet X.509 Public Key Infrastructure Time-Stamp Protocol (TSP)"
- [7] ISO 9594-6: "Information technology - Open Systems Interconnection - The Directory: Selected attribute types"
- [8] ITU-T Recommendation X.520: "Information technology - Open Systems Interconnection - The Directory: Selected attribute types"
- [9] IETF RFC 5816: "ESSCertIDv2 update to RFC 3161"
- [10] ETSI TS 102 176-1: "Electronic Signatures and Infrastructures (ESI); Algorithms and Parameters for Secure Electronic Signatures; Part 1: Hash functions and asymmetric algorithms"

## Definitions and Abbreviations
- **time-stamping unit**: set of hardware and software which is managed as a unit and has a single time-stamping signing key active at a time
- **HTTP**: HyperText Transfer Protocol
- **TSA**: Time Stamping Authority
- **TSP**: Time Stamp Protocol

## 4 Requirements for a TSP client
### 4.1 Void
- Clause 4.1 is void.

### 4.2 Profile for the format of the request
#### 4.2.1 Parameters to be supported
- **R1**: No extension field **shall** be present.

#### 4.2.2 Hash Algorithms to be used
- **R2**: Hash algorithms supported for the time-stamp data **shall** be as specified in clause A.8 of TS 102 176-1 [10].
- **R3**: This **should** take into account the expected duration of the time-stamp and recommended hash functions versus time given in clause 9.2 of TS 102 176-1 [10].
- NOTE: In the case of old time-stamps that were applied at a time when use of other algorithms were accepted then implementations **may** raise a warning to users and **may** indicate that the time-stamp remains valid even if the algorithms is no longer considered acceptable.

### 4.3 Profile for the format of the response
#### 4.3.1 Parameters to be supported
- **R4**: The `accuracy` field **must** be supported and understood.
- **R5**: The `nonce` parameter **must** be supported.
- **R6**: No extension is required to be supported.
- NOTE: A TSA **may** not support ordering hence clients **should** not depend on the ordering of time-stamps.

#### 4.3.2 Algorithms to be supported
- **R7**: Time-stamp token signature algorithms to be supported **shall** be as specified in clause A.8 of TS 102 176-1 [10].
- NOTE: (same as above for old time-stamps)

#### 4.3.3 Key lengths to be supported
- **R8**: Signature algorithm key lengths for the selected signature algorithm **should** be supported as recommended in clause 9.3 of TS 102 176-1 [10].

## 5 Requirements for a TSP server
### 5.1 Profile for the format of the request
#### 5.1.1 Parameters to be supported
- **R9**: The `nonce` **must** be supported.
- **R10**: `certReq` **must** be supported.
- **R11**: No extension is required to be supported.

#### 5.1.2 Algorithms to be supported
- **R12**: Hash algorithms for the time-stamp data to be supported **shall** be as specified in clause A.8 of TS 102 176-1 [10].
- **R13**: This **should** take into account the expected duration of the time-stamp and recommended hash functions versus time given in clause 9.2 of TS 102 176-1 [10].
- NOTE: (same as above for old time-stamps)

### 5.2 Profile for the format of the response
#### 5.2.1 Parameters to be supported
- **R14**: A `genTime` parameter limited to represent time with one second is required.
- **R15**: A minimum `accuracy` of one second is required.
- **R16**: An `ordering` parameter missing or set to `false` is required.
- **R17**: No extension is required to be generated.
- **R18**: No extension **shall** be critical.

#### 5.2.2 Structure for the name of the issuing TSP server
- **R19**: The name of the issuing TSP server **shall** contain an appropriate subset of the following attributes (defined in ISO 9594-6 [7] and ITU-T Recommendation X.520 [8]): `countryName`, `stateOrProvinceName`, `organizationName`, `commonName`.
- **R20**: The `countryName`, when applicable, identifies the name of the country where the TSA is established (not necessarily where the time-stamping unit is located).
- **R21**: The `stateOrProvinceName` is an optional component that identifies a geographical subdivision in which the TSA is established.
- **R22**: The `organizationName` **shall** be present. It identifies the TSA responsible for managing the time-stamping unit. That name **should** be an officially registered name of the TSA.
- **R23**: The `commonName` **shall** be present. It specifies an identifier for the time-stamping unit. Within the TSA, the attribute `commonName` uniquely identifies the time-stamping unit used.

#### 5.2.3 Algorithms to be supported
- **R24**: Time-stamp token signature algorithms **shall** be supported as specified in clause A.8 of TS 102 176-1 [10].
- NOTE: (same as above for old time-stamps)

#### 5.2.4 Key lengths to be supported
- **R25**: It is recommended that key length for the selected signature algorithm is as recommended in clause 9.3 of TS 102 176-1 [10].

#### 5.2.5 TSA Certificates
- **R26**: It is recommended that certificates issued for TSA are as specified in clauses A.9 and A.10 of TS 102 176-1 [10].

#### 5.2.6 TSA Certificate Identifier
- **R27**: The TSA certificate identifier **must** be present in the TSA signature as specified in RFC 3161 [1] (ESSCertID) or RFC 5816 [9] (ESSCertID or ESSCerIDv2).

## 6 Profiles for the transport protocols to be supported
- **R28**: One on-line protocol and one store and forward protocol **must** be supported for every TSA.
- **R29**: Among the four protocols defined in RFC 3161 [1], the following protocol **should** be supported: the Time Stamp Protocol via HTTP (section 3.4 from RFC 3161 [1]).

## 7 Object identifiers of the cryptographic algorithms
- **R30**: Object identifiers for the recommended hashing and signature algorithms are specified in annex F of TS 102 176-1 [10].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | No extension field shall be present. | shall | 4.2.1 |
| R2 | Hash algorithms for time-stamp data shall be as specified in clause A.8 of TS 102 176-1 [10]. | shall | 4.2.2 |
| R3 | Consider expected duration and recommended hash functions versus time per clause 9.2 of TS 102 176-1 [10]. | should | 4.2.2 |
| R4 | accuracy field must be supported and understood. | must | 4.3.1 |
| R5 | nonce parameter must be supported. | must | 4.3.1 |
| R6 | No extension required to be supported. | (no type) | 4.3.1 |
| R7 | Time-stamp token signature algorithms shall be as specified in clause A.8 of TS 102 176-1 [10]. | shall | 4.3.2 |
| R8 | Signature algorithm key lengths should be as recommended in clause 9.3 of TS 102 176-1 [10]. | should | 4.3.3 |
| R9 | nonce must be supported. | must | 5.1.1 |
| R10 | certReq must be supported. | must | 5.1.1 |
| R11 | No extension required to be supported. | (no type) | 5.1.1 |
| R12 | Hash algorithms for time-stamp data shall be as specified in clause A.8 of TS 102 176-1 [10]. | shall | 5.1.2 |
| R13 | Consider expected duration and recommended hash functions versus time per clause 9.2 of TS 102 176-1 [10]. | should | 5.1.2 |
| R14 | genTime limited to 1 second is required. | required | 5.2.1 |
| R15 | Minimum accuracy of 1 second is required. | required | 5.2.1 |
| R16 | ordering parameter missing or set to false is required. | required | 5.2.1 |
| R17 | No extension required to be generated. | (no type) | 5.2.1 |
| R18 | No extension shall be critical. | shall | 5.2.1 |
| R19 | Issuing TSP server name shall contain appropriate subset of attributes from ISO 9594-6/X.520. | shall | 5.2.2 |
| R20 | countryName identifies country where TSA established. | (informative) | 5.2.2 |
| R21 | stateOrProvinceName is optional geographic subdivision. | (informative) | 5.2.2 |
| R22 | organizationName shall be present; should be officially registered name. | shall/should | 5.2.2 |
| R23 | commonName shall be present; uniquely identifies time-stamping unit. | shall | 5.2.2 |
| R24 | Time-stamp token signature algorithms shall be supported per clause A.8 of TS 102 176-1 [10]. | shall | 5.2.3 |
| R25 | Recommend key length per clause 9.3 of TS 102 176-1 [10]. | recommended | 5.2.4 |
| R26 | Recommend certificates per clauses A.9 and A.10 of TS 102 176-1 [10]. | recommended | 5.2.5 |
| R27 | TSA certificate identifier must be present per RFC 3161 or RFC 5816. | must | 5.2.6 |
| R28 | One on-line and one store-and-forward protocol must be supported per TSA. | must | 6 |
| R29 | Should support TSP via HTTP (RFC 3161 section 3.4). | should | 6 |
| R30 | OIDs for recommended hashing and signature algorithms are in annex F of TS 102 176-1 [10]. | (reference) | 7 |

## Informative Annexes (Condensed)
- **Annex A (Structure for the policy field)**: When TSA conforms to TS 102 023 [i.1], the TSTInfo policy field should contain the identifier `itu-t(0) identified-organization(4) etsi(0) time-stamp-policy(02023) policy-identifiers(1) baseline-ts-policy (1)`. If not included, TSA may define its own enhanced policy.
- **Annex B (Bibliography)**: Lists references including Directive 1999/93/EC, RFC 2459, RFC 2630, FIPS PUB 186, and cryptography literature (e.g., RIPEMD-160, Handbook of Applied Cryptography).