# ETSI TR 119 476 V1.2.1 (2024-07): Electronic Signatures and Trust Infrastructures (ESI); Analysis of selective disclosure and zero-knowledge proofs applied to Electronic Attestation of Attributes

**Source**: ETSI Technical Committee ESI | **Version**: V1.2.1 | **Date**: 2024-07 | **Type**: Technical Report (Informative)

**Original**: https://www.etsi.org/standards-search

## Scope (Summary)

This Technical Report analyses cryptographic schemes for selective disclosure, unlinkability, and predicates (including range proofs) applied to (Qualified) Electronic Attestations of Attributes ((Q)EAAs) and Person Identification Data (PID) in the context of eIDAS2 and the EUDI Wallet Architecture and Reference Framework (ARF). It provides a comprehensive overview of schemes, formats, and protocols, with detailed analysis of ISO mDL MSO and IETF SD-JWT as mandated PID formats, and assesses feasibility of BBS+ and programmable ZKPs for future use.

## Normative References

Not applicable in the present document.

## Informative References

- [i.1] Adida: "Helios: Web-based Open-Audit Voting"
- [i.2] Paquin-Zaverucha: "U-Prove Cryptographic Specification V1.1"
- … (Full list of 217 references as per original, abbreviated for brevity; key references are cited in the text.)

## Definitions and Abbreviations

### Terms

- **Atomic (Q)EAA**: (Qualified) Electronic Attestation of Attribute with a single attribute claim.
- **Attribute**: feature, characteristic or quality of a natural or legal person or of an entity, in electronic form (ARF).
- **Authentic source**: repository or system, held under the responsibility of a public sector body or private entity, that contains attributes about a natural or legal person and is considered to be the primary source (ARF).
- **Blind signature**: type of digital signature in which the content of a message is disguised before it is signed.
- **Electronic Attestation of Attributes (EAAs)**: attestation in electronic form that allows the authentication of attributes (ARF).
- **EUDI Wallet Instance**: instance of an EUDI Wallet Solution belonging to and controlled by a user (ARF).
- **EUDI Wallet Provider**: organization responsible for the operation of an eIDAS-compliant EUDI Wallet Solution (ARF).
- **ISO mDL**: ISO mobile driving license according to ISO/IEC 18013-5 and ISO/IEC CD 18013-7.
- **Issuing Authority Certification Authority (IACA)**: certification authority that issues certificates for creating ISO mDL MSOs and auxiliary certificates.
- **Issuer**: issuing authority accredited or supervised for issuing certificates, attested attributes, ISO mDL or credentials.
- **MSO**: ISO mobile driving license Mobile Security Object, with salted attribute hashes of the user's elements in the ISO mDL mdoc.
- **Person Identification Data (PID)**: set of data enabling the identity of a natural or legal person to be established (ARF).
- **Person Identification Data Provider (PIDP)**: Member State or legal entity providing PID to users (ARF).
- **Predicate proof**: verifiable Boolean assertion about the value of another attribute claim without disclosing the claim value itself.
- **Qualified Electronic Attestations of Attributes (QEAAs)**: EAAs issued by a Qualified Trust Service Provider meeting eIDAS2 requirements.
- **Quantum-Safe Cryptography (QSC)**: cryptographic algorithms secure against cryptanalytic attack by a quantum computer.
- **Range proof**: method by which the user can prove that a number is in a given range without disclosing the actual number.
- **SD-JWT**: W3C Verifiable Credential used with SD-JWT containing a list of salted hash values of the user's claims.
- **Selective disclosure**: capability of the EUDI Wallet that enables the user to present a subset of attributes from PID and/or (Q)EAAs (ARF).
- **Unlinkability**: lack of information required to connect the user's selectively disclosed attributes beyond what is disclosed.
- **User**: natural or legal person using an EUDI Wallet (ARF).
- **Verified issuer certificate authority list (VICAL) provider**: ISO mDL provider that compiles and provides trust anchors.
- **W3C VCDM**: W3C Verifiable Credential Data Model.
- **W3C VCDI**: W3C Verifiable Credential Data Integrity.
- **Zero-Knowledge Proof (ZKP)**: method by which the user can prove to the relying party that a given statement is true without providing any additional information.

### Abbreviations

- **BBS**: Boneh-Boyen-Shacham
- **BBS+**: Extension of BBS for multi-message signatures
- **CL**: Camenisch-Lysyanskaya
- **DAA**: Direct Anonymous Attestation
- **HDK**: Hierarchical Deterministic Key
- **IACA**: Issuing Authority Certification Authority
- **JWT**: JSON Web Token
- **KVAC**: Keyed-Verification Anonymous Credentials
- **mDL**: mobile driving license
- **MSO**: Mobile Security Object
- **OID4VP**: OpenID for Verifiable Presentations
- **PID**: Person Identification Data
- **PIDP**: Person Identification Data Provider
- **PS-MS**: Pointcheval-Sanders Multi-Signatures
- **QSC**: Quantum-Safe Cryptography
- **QTSP**: Qualified Trust Service Provider
- **SD-JWT**: Selective Disclosure JSON Web Token
- **TPM**: Trusted Platform Module
- **VCDM**: Verifiable Credential Data Model
- **VCDI**: Verifiable Credential Data Integrity
- **VICAL**: Verified Issuer Certificate Authority List
- **ZKP**: Zero-Knowledge Proof
- **zk-SNARK**: Zero-Knowledge Succinct Non-Interactive Argument of Knowledge

## 4 Selective disclosure signature schemes

### 4.1 General

Analysis covers underlying cryptographic algorithms, maturity, and cryptographic aspects (SOG-IS approval, QSC). Four categories: atomic (Q)EAAs, multi-message signatures, salted attribute hashes, and proofs for arithmetic circuits.

### 4.2 Atomic (Q)EAAs schemes

- **Definition**: (Q)EAA with a single attribute claim, issued on request or batchwise.
- **Privacy**: Verifier unlinkability achievable by batch issuance; not fully unlinkable.
- **Pairing**: Cannot guarantee proper pairing of multiple atomic credentials in a presentation without additional mechanisms.

### 4.3 Multi-message signature schemes

#### 4.3.1 The BBS+ signature scheme

- **Background**: Evolved from BBS04 group signatures (Boneh-Boyen-Shacham, 2004). BBS+ allows signing multiple messages with constant-size signature; supports selective disclosure and ZKP.
- **IETF CFRG BBS draft** ([i.116]): Specifies BBS+ using BLS12-381 curve.
- **Cryptographic analysis**: Not quantum-safe (reliance on bilinear pairings). Not SOG-IS approved. Fully unlinkable.

#### 4.3.2 Camenisch-Lysyanskaya (CL) signatures

- **Properties**: Preserve algebraic structure of messages; support oblivious signing and ZKP of signature possession.
- **Unlinkability**: Fully unlinkable.
- **Cryptographic analysis**: Based on strong RSA or bilinear pairings; not quantum-safe; not SOG-IS approved.

#### 4.3.3 Mercurial signatures

- **Properties**: Allow transformation of signatures between equivalent keys/pseudonyms. Based on DDH; not quantum-safe.

#### 4.3.4 Pointcheval-Sanders Multi-Signatures (PS-MS)

- **Use**: Distributed privacy-preserving Attribute Based Credentials (dp-ABC). Based on bilinear pairings; not quantum-safe.

#### 4.3.5 ISO standardisation of multi-message signature schemes

- **ISO/IEC 20008**: Standardises anonymous digital signatures (mechanism 3 = BBS04 single-message).
- **ISO/IEC PWI 24843**: Preliminary work on privacy-preserving attribute-based credentials (potential standardisation of BBS+ and PS-MS with blinded signatures).
- **ISO/IEC CD 27565**: Guidelines on privacy preservation based on ZKP; includes BBS+ example (refers to IETF CFRG BBS).

#### 4.3.6 Extensions of multi-messages signature schemes

- **Research**: MoniPoly, efficient redactable signatures (Sanders) reduce proof size impact of undisclosed attributes.

### 4.4 Salted attribute hashes

#### 4.4.1 Overview

- **Concept**: Each attribute combined with a random salt and hashed; signed list of salted hashes.
- **Examples**: ISO mDL MSO, IETF SD-JWT.
- **Unlinkability**: Not inherently; verifier unlinkability via batch issuance with unique salts and unique holder keys.

#### 4.4.2 Issuance phase

- **Steps**: For each attribute, concatenate salt||attribute, hash, order in signed list (indexed, array, DAG). Store (Q)EAA and list in wallet.

#### 4.4.3 Presentation and verification phase

- **Steps**: Wallet presents disclosed attribute and salted hash list; verifier checks signature, recomputes hash of salt||attribute, compares.

#### 4.4.4 Salted attribute hashes and unlinkability

- **Criteria for verifier unlinkability**: Unique random salts per attestation; each attestation used once; unique user public keys per attestation (e.g., via Hierarchical Deterministic Keys – HDK).

#### 4.4.5 Cryptographic analysis

- **Advantage**: Use of SOG-IS approved algorithms (RSA, ECC) and QSC possible. Format flexibility.

#### 4.4.6 Predicates based on computational inputs

- **Static predicates**: Boolean claims (e.g., "age_over_18": true) can be included.
- **Dynamic predicates**: Possible via issuer-signed commitments to hash chain roots (e.g., HashWires).

#### 4.4.7 HashWires

- **Purpose**: Credential-based range proofs using hash chains; efficient inequality tests.
- **Integration**: Can be combined with SD-JWT or MSO by including hash chain commitments as selectively disclosable values.
- **Cryptography**: Based on hash functions; quantum-safe.

#### 4.4.8 Authentic Chained Data Containers (ACDC)

- **Structure**: Directed Acyclic Graph (DAG). Supports compact, partial, and selective disclosures.
- **Unlinkability**: Verifier unlinkable (batch issuance); not fully unlinkable.
- **Quantum-safe**: Based on hashes.

#### 4.4.9 Gordian Envelopes

- **Structure**: Verifiable hierarchical data using DAG. Supports selective disclosure.
- **Unlinkability**: Verifier unlinkable with salting and batch issuance.
- **Quantum-safe**: Based on hashes.

### 4.5 Proofs for arithmetic circuits (programmable ZKPs)

#### 4.5.1 General

Arithmetic circuits can represent any computation; programmable ZKPs allow proving any statement.

#### 4.5.2 zk-SNARKs

- **Characteristics**: Zero-Knowledge, Succinct, Non-interactive, Argument of Knowledge.
- **Trusted setup vs. transparent setup**.
- **Cryptographic building blocks**: Fiat-Shamir, PCP, QAP, PIOP, PCS.
- **Post-quantum**: Some (e.g., zk-STARKs) are quantum-safe; others (e.g., Groth16) are not.
- **Implementations**: ZeroCash, Ethereum zk-Rollups. Projects like Cinderella and zk-creds use zk-SNARKs with existing identities.

## 5 (Q)EAA formats with selective disclosure

### 5.1 General

Formats categorised by underlying signature scheme: atomic, multi-message, salted hashes, and JSON container formats.

### 5.2 Atomic (Q)EAA formats

#### 5.2.1 Introduction

Atomic (Q)EAAs contain a single claim. Formats include X.509 attribute certificates and W3C Verifiable Credentials.

#### 5.2.2 PKIX X.509 attribute certificate with atomic attribute

- **Standard**: IETF RFC 5755.
- **Use**: Linked to a public key certificate; short-lived; suitable for selective disclosure.
- **Cryptography**: SOG-IS approved algorithms; QSC possible.

#### 5.2.3 W3C Verifiable Credential with atomic attribute

- **Encoding**: JWT or JSON-LD.
- **Cryptography**: SOG-IS approved; QSC possible.

### 5.3 Multi-message signature (Q)EAA formats

#### 5.3.1 W3C VC Data Model with ZKP

- **Clause 5.8** in VCDM 1.1 describes ZKP support; examples using CL-signatures, BBS, etc.

#### 5.3.2 W3C VC Data Integrity with BBS Cryptosuite

- **W3C BBS Cryptosuite v2023**: Experimental; uses IETF CFRG BBS (BBS+).
- **ISO standardisation**: Potential compatibility if ISO/IEC PWI 24843 standardises BBS+.

#### 5.3.3 W3C Data Integrity ECDSA Cryptosuites v1.0

- **Selective disclosure**: ECDSA-SD-2023 functions (createDisclosureData) for derived proofs.

#### 5.3.4 Hyperledger AnonCreds (format)

- **Format**: JSON; uses CLRSA signatures; supports selective disclosure and full unlinkability.

#### 5.3.5 Cryptographic analysis

- **Maturity**: W3C VC high; BBS+, CL, ECDSA-SD not SOG-IS approved nor quantum-safe.

### 5.4 (Q)EAAs with salted attribute hashes

#### 5.4.1 General

Formats use salted attribute hashes: IETF SD-JWT, ISO mDL MSO.

#### 5.4.2 IETF SD-JWT

- **Structure**: Header, payload, signature. Payload includes `_sd` array of digests of disclosures.
- **Selective disclosure**: User shares disclosures (salt, key, value) out-of-band.
- **Cryptography**: JOSE allows SOG-IS approved and QSC algorithms.
- **Holder binding**: Optional JWT for holder binding.
- **Unlinkability**: Verifier unlinkable via batch issuance with unique salts and holder binding keys.

#### 5.4.3 ISO/IEC 18013-5 Mobile Security Object (MSO)

- **Structure**: Contains `valueDigests` (salted hashes), `deviceKey`, `docType`, `validityInfo`.
- **Signing**: COSE signature by IACA; SOG-IS approved curves; QSC possible.
- **Unlinkability**: Verifier unlinkable via batch MSOs with unique salts and device keys.

### 5.5 JSON container formats

#### 5.5.1 IETF JSON WebProof (JWP)

- **Purpose**: Container for selective disclosure and ZKP schemes (BBS+, CL, etc.). Supports multiple payloads and presentation forms.

#### 5.5.2 W3C JSON Web Proofs For Binary Merkle Trees

- **Specification**: Generic encoding of Merkle audit paths for selective disclosure; quantum-safe.

## 6 Selective disclosure systems and protocols

### 6.1 General

Systems and protocols categorised by underlying scheme: atomic, multi-message, salted hashes, proofs for arithmetic circuits, anonymous credentials, ISO mDL.

### 6.2 Atomic attribute (Q)EAA presentation protocols

#### 6.2.1 PKIX X.509 attribute certificates with single attributes

- **Flow**: User authenticates via public key certificate; attribute certificates (atomic) are pushed/pulled to verifier.
- **Privacy**: Pseudonymous public key certificates; short-lived attribute certificates.
- **Cryptography**: SOG-IS approved; QSC possible.

#### 6.2.2 VC-FIDO for atomic (Q)EAAs

- **Integration**: WebAuthn (FIDO2) extended for W3C VC enrolment; user can enrol for atomic VCs on demand.
- **Status**: Prototype (NHS UK pilot).

### 6.3 Multi-message signature protocols and solutions

#### 6.3.1 Hyperledger AnonCreds (protocols)

- **Implementation**: Based on CLRSA signatures; widely deployed (British Columbia, IDunion, IATA).

#### 6.3.2 Direct Anonymous Attestation (DAA) used with TPMs

- **Use**: TPM 2.0 and EPID 2.0; zero-knowledge attestation of platform integrity.
- **Cryptography**: ECC based; not quantum-safe.

### 6.4 Salted attribute hashes protocols

#### 6.4.1 OpenAttestation (Singapore's Smart Nation)

- **Method**: Target hash of sorted salted attribute hashes (Keccak256). Can use digital signatures or Ethereum.

### 6.5 Proofs for arithmetic circuits solutions

#### 6.5.1 Anonymous (Q)EAAs from programmable ZKPs and existing digital identities

- **Overview**: Combine existing credentials (X.509, ICAO) with zk-SNARKs to generate anonymous presentations.
- **Process**: Setup (circuit compiler), issuance (credential request), proof (local verification with ZKP).

#### 6.5.2 Cinderella: zk-SNARKs to verify the validity of X.509 certificates

- **Implementation**: Uses Pinocchio/Geppetto to create pseudo-certificates with selected attributes and OCSP stapling. Works with national eID cards (Belgium, Estonia, Spain).
- **Performance**: Offline generation up to 9 min; online verification <10 ms.

#### 6.5.3 zk-creds: zk-SNARKs used with ICAO passports

- **Implementation**: ZKP of ICAO eMRTD (e.g., DG1 data) for anonymous credentials. Uses zk-SNARKs.

#### 6.5.4 Analysis of systems based on programmable ZKPs

- **Advantages**: Reuse existing infrastructure; local validation; selective disclosure and predicates; quantum-safe options.
- **Challenges**: Complexity, proving time (especially for lattice-based), still research phase.

### 6.6 Anonymous attribute based credentials systems

#### 6.6.1 Idemix (Identity Mixer)

- **Technology**: IBM Research; uses CL-signatures; supports selective disclosure and full unlinkability.
- **Deployment**: Hyperledger Fabric, IRMA, PrimeLife.

#### 6.6.2 U-Prove

- **Technology**: Based on Brands work; blind signatures; selective disclosure; **not** multi-show unlinkable.
- **Security**: Broken under concurrent issuance (ROS attack); sequential only.
- **Standardisation**: ISO/IEC 18370-2:2016 mechanism 4.

#### 6.6.3 ISO/IEC 18370 (blind digital signatures)

- **Status**: Standard; mechanism 4 = U-Prove. Not recommended due to linkability and ROS vulnerability.

#### 6.6.4 Keyed-Verification Anonymous Credentials (KVAC)

- **Approach**: Algebraic MACs; MAC_BBS+ variant (pairing-free BBS). Suitable for resource-constrained environments (SIM cards). Public-key variant uses BBS+.

### 6.7 ISO mobile driving license (ISO mDL)

#### 6.7.1 Introduction to ISO/IEC 18013-5 (ISO mDL)

- **Components**: mDL mdoc (attributes), MSO (salted hashes), authentication key.

#### 6.7.2 ISO/IEC 18013-5 (device retrieval flow)

- **Protocol**: BLE/NFC/WiFi; user selects attributes; MSO and DeviceSignedItems sent to reader.
- **Cryptography**: COSE signatures; SOG-IS approved; QSC possible.
- **ARF**: Mandatory for EUDI Wallet PID.

#### 6.7.3 ISO/IEC 18013-5 (server retrieval flows)

- **WebAPI flow**: Issuer provides mDL response to reader upon user consent.
- **OIDC flow**: Issuer as OIDC Authorization Server; token includes selected JWT claims.
- **Privacy concern**: Issuer might track usage; eIDAS2 Art 5a.16 may restrict.

#### 6.7.4 ISO/IEC 18013-7 (unattended flow)

- **Device retrieval flow**: Direct HTTPS POST from wallet to reader.
- **OID4VP/SIOP2 flow**: Web-based presentation.
- **Backward compatible** with ISO/IEC 18013-5.

#### 6.7.5 ISO/IEC 23220-4 (operational protocols)

- **Scope**: Presentation protocols for digital wallets; supports ISO mDL and W3C VC with SD-JWT.
- **Security**: HTTPS with QWACs.

## 7 Implications of selective disclosure on standards for (Q)EAA/PID

### 7.1 General implications

ARF mandates ISO mDL MSO and SD-JWT as PID selective disclosure formats due to SOG-IS approval and QSC compatibility. Clause 7 analyses these formats and BBS+/ZKP alternatives.

### 7.2 Implications for ISO mDL with selective disclosure

#### 7.2.1 QTSP/PIDP issuing ISO mDL

- **Certificate profiles**: IACA trust anchor and subordinated certificates must comply with SOG-IS approved algorithms.
- **Trusted Lists**: EU TL may be mapped to ISO mDL VICAL; bridging needed (XML vs CDDL/CMS).
- **Issuance**: Batch issuance of MSOs with unique salts and device keys for verifier unlinkability. Static predicates (e.g., age_over_18) can be included.

#### 7.2.2 EUDI Wallet mDL authentication key

- **Storage**: Secure Element / TEE; PIN/biometric access. HDK can derive unique keys per MSO.

#### 7.2.3 EUDI Wallet used with ISO mDL device retrieval flow

- **Process**: User selects attributes; MSO and DeviceSignedItems presented; reader validates MSO signature and hashes.
- **Recommendations**: Use EU TL for trust anchor; MSOs must be unique per batch.

#### 7.2.4 EUDI Wallet used with ISO mDL server retrieval flow

- **Process**: User consent; issuer provides selected data via WebAPI or OIDC. Privacy concerns due to issuer involvement (eIDAS2 Art 5a.14, 5a.16).

#### 7.2.5 EUDI Wallets used with ISO/IEC 18013-7 for unattended flow

- **Process**: Direct wallet-to-reader; no issuer involvement. Supported by ARF.

### 7.3 Implications for SD-JWT selective disclosure

#### 7.3.1 Background to W3C VCDM and SD-JWT

ARF mandates joint use of W3C VCDM v1.1 and SD-JWT. However, there are unresolved issues (JSON-LD vs JSON, data integrity proofs). Recommendation: use SD-JWT VC and mapping to VCDM compliance.

#### 7.3.2 A primer on W3C VCDM

- **JSON-LD**: Semantic interoperability; data integrity proofs sign the graph.
- **JWT based VC**: Secured using SD-JWT; selective disclosure via `_sd` array.
- **Difficulties**: Double encoding, unclear mapping, lack of syntax for selective disclosure in VCDM.

#### 7.3.3 Analysis of using SD-JWT as (Q)EAA format applied to eIDAS2

- **Recommendation**: Use SD-JWT VC as standalone attestation; batch issuance with unique salts and holder binding keys for verifier unlinkability.
- **Predicates**: Static or via HashWires.
- **Signature**: JOSE with SOG-IS approved or QSC algorithms.

### 7.4 Feasibility of BBS+ applied to eIDAS2

#### 7.4.1 General

BBS+ offers full unlinkability but is not yet standardised.

#### 7.4.2 Standardization of BBS+

- **ISO/IEC PWI 24843**: Potential standardisation of BBS+; could be referenced by eIDAS2.

#### 7.4.3 Feasibility of using BBS+ with W3C VCDM

- **Requirement**: Update ARF to allow VCDM 2.0 with JSON-LD; standardise W3C BBS Cryptosuite referencing ISO BBS+.

#### 7.4.4 Post-quantum considerations for BBS+

- **Confidentiality**: Undisclosed attributes remain safe; integrity and authenticity vulnerable to quantum computer attacks (signature forgery). One-time use can provide post-quantum safety.

#### 7.4.5 Conclusions of using BBS+ applied to eIDAS2

- **Recommendation**: Await ISO standardisation; ETSI to profile BBS+ usage; use in pre-quantum world.

### 7.5 Feasibility of programmable ZKPs applied to eIDAS2 (Q)EAAs

#### 7.5.1 Background and existing solutions

- **Cinderella**: zk-SNARKs with X.509 certificates; existing eIDAS PKI re-used.
- **zk-creds**: zk-SNARKs with ICAO passports.

#### 7.5.2 Extensions to EUDI Wallets, relying parties and protocols

- **Requirements**: Wallet must support circuit compiler and zk-SNARK client; verifier must have server-side circuits; OID4VP extension needed.

#### 7.5.3 Conclusions of programmable ZKPs applied to eIDAS2 (Q)EAAs

- **Advantages**: Full unlinkability; quantum-safe options; reuses existing infrastructure.
- **Status**: Research phase; consider for future ARF versions and large-scale pilots.

### 7.6 Secure storage of PID/(Q)EAA keys in EUDI Wallet

- **ISO mDL authentication key and SD-JWT holder binding key**: Store in SE/TEE; PIN/biometric access.
- **BBS+**: Could be stored in remote HSM or SIM card (BBS_MAC).
- **Certification**: Under ENISA EUCC; reference to Protection Profiles (e.g., GlobalPlatform TEE, Eurosmart 3S).

## 8 Privacy aspects of revocation and validity checks

### 8.1 Introduction

eIDAS2 Art 5a.16(a) requires that revocation services do not allow tracking. Validity status checks must minimise correlation identifiers.

### 8.2 Online certificate status protocol (OCSP)

- **Privacy risk**: Submits unique identifier. Mitigations: single-show attestations, OCSP Must-Staple (wallet caches signed response).

### 8.3 Revocation lists

- **Privacy risk**: Identifiers in RL. Mitigations: single-show, large RLs, range requests, Private Set Intersection (PSI) or Private Information Retrieval (PIR).

### 8.4 Validity status lists

- **Method**: Bit vector; does not reveal identifier directly. Small size, can be fetched entirely.
- **Privacy risks**: Batch revocation reveals correlation. Mitigations: randomized index assignment, hiding still-valid entries.

### 8.5 Cryptographic accumulators

- **Types**: Bloom filters (probabilistic), dynamic accumulators (Camenisch-Lysyanskaya), universal accumulators.
- **Advantages**: Efficient batch updates; privacy-friendly witness updates.

### 8.6 Using programmable ZKP schemes for revocation checks

- **Approach**: Wallet performs revocation check locally (e.g., OCSP) and includes ZKP of validity; verifier learns only revocation status, not identifiers.

### 8.7 Conclusions on validity status checks

- **Recommendations**: Use OCSP Must-Staple, RL/SL with PSI/PIR, cryptographic accumulators, or programmable ZKPs for high privacy.

## 9 Post-quantum considerations - general remarks

- **Threat**: Quantum computers can break DLP-based cryptography (RSA, ECDSA, BBS+, etc.).
- **Impact**: Data confidentiality of undisclosed attributes in ZKP schemes remains; integrity and authenticity of signatures are compromised.
- **Mitigation**: Use quantum-safe signature schemes (FIPS 204, FIPS 205) for salted hash formats; one-time use of BBS+; select post-quantum safe zk-SNARKs (e.g., zk-STARKs).

## 10 Conclusions

- **ISO mDL MSO and SD-JWT**: Meet eIDAS2 selective disclosure requirements; verifier unlinkability via batch issuance; support SOG-IS and QSC algorithms.
- **BBS+**: Full unlinkability; not yet standardised; post-quantum limitations; recommended for future once standardised.
- **Programmable ZKPs**: Full unlinkability and predicates; still research; promising for future ARF.
- **Revocation**: Privacy-preserving methods exist (OCSP Must-Staple, accumulators, ZKPs); should be integrated.
- **Recommendations**: Consider for ETSI TS 119 471, 119 472-1, 119 462.

## Annex A: Comparison of selective disclosure mechanisms (Condensed)

| Category | Schemes | Unlinkability | Predicates | SOG-IS/QSC |
|---|---|---|---|---|
| Atomic | Single-attribute (X.509, W3C VC) | Verifier (batch) | No | Yes/Yes |
| Multi-message | BBS+, CL, Mercurial, PS-MS | Full (blinded) | Yes | No/No |
| Salted hashes | MSO, SD-JWT, ACDC, Gordian Envelope | Verifier (batch) | Limited (static) | Yes/Yes |
| Programmable ZKP | zk-SNARKs (various) | Full | Yes | Varies |

## Annex B: Code examples (Condensed)

- **Hash chain code example** (Python-like): Demonstrates iterative hashing for inequality test.
- **HashWires for SD-JWT and MSO**: Example of including hash chain commitments as selectively disclosable values in `_sd` array.

## Annex C: Post-quantum safe zero-knowledge proofs and anonymous credentials (Condensed)

### C.1 General

Research on quantum physics-based ZKP (e.g., graph 3-colouring) and lattice-based anonymous credentials.

### C.2 Quantum physics applied on ZKP schemes

- **QKD**: Unconditional security based on quantum mechanics.
- **Graph 3-colouring ZKP**: Quantum version allows zero-knowledge with quantum states.
- **Quantum Internet ZKP**: Based on Schnorr algorithm; requires quantum communication.

### C.3 Lattice-based anonymous credentials schemes

- **Background**: Post-quantum safe; smaller signatures near classical size.
- **Research**: Bootle et al. (2020), Jeudy et al. (2023); efficient lattice-based anonymous credentials.

## Annex D: Bibliography (175 entries, abbreviated)

(Full list as per original; key references cited above.)

## Annex E: Change history

(Not reproduced; contains version history.)

---
*End of compressed document.*