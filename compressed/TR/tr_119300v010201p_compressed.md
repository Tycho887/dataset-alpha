# ETSI TR 119 300: Electronic Signatures and Infrastructures (ESI); Guidance on the use of standards for cryptographic suites
**Source**: ETSI | **Version**: V1.2.1 | **Date**: March 2016 | **Type**: Informative (Technical Report)
**Original**: ETSI TR 119 300 V1.2.1 (2016-03)

## Scope (Summary)
Provides business-driven guidance on selecting cryptographic suites for digital signature creation. Explains security parameters, how to analyze business needs, and how to select a system satisfying those needs. Audience: application designers, implementers, trust service providers, and security device manufacturers.

## Normative References
- Not applicable.

## Informative References
- [i.1] ETSI EN 319 102-1: Procedures for creation and validation of AdES digital signatures; Part 1: Creation and validation
- [i.2] ETSI TS 103 174: ASiC Baseline Profile
- [i.3] ISO/IEC 10118-3 (2004): Hash functions – Part 3: Dedicated hash functions
- [i.4] FIPS Publication 180-4 (2012): Secure Hash Standard (SHS)
- [i.5] Regulation (EU) No 910/2014 on electronic identification and trust services
- [i.6] ETSI TS 119 312: Cryptographic Suites
- [i.7] ETSI TS 101 733: CMS Advanced Electronic Signatures (CAdES)
- [i.8] ETSI TS 101 903: XML Advanced Electronic Signatures (XAdES)
- [i.9] ETSI TS 102 778: PDF Advanced Electronic Signature Profiles (PAdES)
- [i.10] ETSI TS 102 918: Associated Signature Containers (ASiC)
- [i.11] ETSI TS 103 171: XAdES Baseline Profile
- [i.12] ETSI TS 103 172: PAdES Baseline Profile
- [i.13] ETSI TS 103 173: CAdES Baseline Profile
- [i.14] ETSI EN 319 122-1: CAdES digital signatures; Part 1: Building blocks and CAdES baseline signatures
- [i.15] ETSI EN 319 122-2: CAdES digital signatures; Part 2: Extended CAdES signatures
- [i.16] ETSI EN 319 132-1: XAdES digital signatures; Part 1: Building blocks and XAdES baseline signatures
- [i.17] ETSI EN 319 132-2: XAdES digital signatures; Part 2: Extended XAdES signatures
- [i.18] ETSI EN 319 142-1: PAdES digital signatures; Part 1: Building blocks and PAdES baseline signatures
- [i.19] ETSI EN 319 142-2: PAdES digital signatures; Part 2: Additional PAdES signatures profiles
- [i.20] ETSI EN 319 162-1: Associated Signature Containers (ASiC); Part 1: Building blocks and ASiC baseline containers
- [i.21] ETSI TR 119 001: Framework for standardization of signatures; Definitions and abbreviations

## Definitions and Abbreviations
- **advanced electronic signature**: As defined in Regulation (EU) No 910/2014 [i.5].
- **cryptographic suite**: Combination of a signature scheme with a padding method and a cryptographic hash function.
- **(digital) signature**: Data appended to, or a cryptographic transformation of a data unit that allows the recipient to prove source and integrity and protect against forgery.
- **electronic signature**: As defined in Regulation (EU) No 910/2014 [i.5].
- **hash function**: As defined in ISO/IEC 10118-3 [i.3].
- **signature augmentation policy**: Set of rules defining technical and procedural requirements for augmentation of digital signatures to meet a business need.
- **signature creation policy**: Set of rules defining technical and procedural requirements for creation of digital signatures.
- **signature policy**: Signature creation, augmentation, validation policy, or any combination thereof.
- **signature scheme**: Triplet of signature creation, verification, and key generation algorithms.
- **signature validation policy**: Set of rules defining technical and procedural requirements for validation of digital signatures.
- **trust service**: Electronic service enhancing trust and confidence in electronic transactions.
- **trust service provider**: Natural or legal person providing one or more trust services.

## Abbreviations
- CMS – Cryptographic Message Syntax
- ENISA – European Union Agency for Network and Information Security
- EU – European Union
- ISO – International Organization for Standardization
- PDF – Portable Document Format
- PIN – Personal Identification Number
- TR – Technical Report
- TS – Technical Specification
- XML – eXtensible Markup Language

## 4 Introduction to cryptographic suites

### 4.1 General
A cryptographic suite is a set of standardized algorithms used to create a digital signature. Selection of the cryptographic suite is not a task for a single signature creation but appears in different business processes and system design.

### 4.2 Digital signatures
ETSI EN 319 102-1 [i.1] specifies format-agnostic procedures for creating and augmenting digital signatures. It defines general principles, objects, and functions for signature creation and augmentation, and general forms to increase longevity.

### 4.3 Signature creation and verification
Creation consists of data input encoding (including formatting) and application of signature algorithm using the signer's private key. Verification uses the same encoding and the signer's public key; output is "valid" or "invalid".

### 4.4 Cryptographic algorithms

#### 4.4.1 Hash functions
Before signing, data is binary encoded and hashed. The hash function must be cryptographically strong: computationally hard to invert, collision-resistant, and pre-image resistant. Bit length is a parameter defining an upper bound for security level.

#### 4.4.2 Message encoding and random numbers
Pre-formatting creates signature input. Randomization ensures different signatures per application; quality of random values is an important security parameter.

#### 4.4.3 Asymmetric signature algorithms
Uses private key for creation, public key for verification. The key length determines cryptographic strength. Security depends on state-of-the-art cryptography; algorithms can weaken over time.

#### 4.4.4 Security bits
Cryptographic strength is measured in bits: if an attack requires 2ⁿ operations, strength is n.

### 4.5 Standardization

#### 4.5.1 Standardization bodies
Cryptographic algorithms should be public and approved by independent expert groups. All algorithms in ETSI TS 119 312 [i.6] are standardized by ISO.

#### 4.5.2 Technical specifications
ETSI TS 119 312 [i.6] recommends algorithms suitable for digital signatures and conditions for their use. It defines requirements based on various security recommendations. Algorithms not listed may still be secure.

## 5 Selecting an appropriate signature suite

### 5.1 Introduction
Use of digital signatures should be defined integral to process specification. Different signature formats can use the same cryptographic functions. There is no absolute scale of security; needs should be analyzed carefully. Interoperability is important; selection of widely deployed suites is recommended.

### 5.2 Evaluating pre-conditions

#### 5.2.1 Trust level
Security parameters should be selected stronger for higher-level keys (e.g., trust anchors) than for end user keys. A table of security parameters vs. trust level is given in ETSI TS 119 312 [i.6].

#### 5.2.2 Trust period
Security parameter of a key should remain secure during its intended usage period. Verification keys of certification authorities, time stamping units, or archival services should be selected stronger and for longer time frames than primary signature keys.

#### 5.2.3 Hardware security
Recommended algorithms are all available in specialized hardware. Hardware may provide an upper bound for security parameters; usage time can be determined accordingly.

#### 5.2.4 Attack potential
Security parameters should be chosen based on value of target. Weak end user keys have limited impact; weak trust anchor keys may require infrastructure replacement.

### 5.3 Guidance to selection

#### 5.3.1 National supervisory bodies
National supervisory bodies provide information on security breaches to the European Commission and ENISA under Regulation (EU) No 910/2014 [i.5].

#### 5.3.2 Trust service providers
Trust service providers shall select the public key algorithm and key length for certificate holders, taking into account device capabilities, software support, efficiency, security requirements, and applicable legislation. They shall guarantee infrastructure homogeneity. They should select appropriate cryptographic suites at a security level that fits their needs, considering conditions in clause 5.2.

#### 5.3.3 Manufacturers of security devices
Manufacturers should implement secret key algorithms at specified key sizes. There should be trust service providers able to certify the keys and software support for interoperability.

#### 5.3.4 Information to end users
End users should be informed about relevant requirements by the trust service provider. Based on usage time of signature creation key and required verification time frame, a suitable set of cryptographic algorithms and parameters can be selected from ETSI TS 119 312 [i.6].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Trust service providers shall select the public key algorithm and key length for certificate holders, taking into account device capabilities, software support, efficiency, security requirements, and applicable legislation. | shall | 5.3.2 |
| R2 | Trust service providers shall guarantee the homogeneity of the infrastructure by selecting the cryptographic suites to be used by their customers. | shall | 5.3.2 |
| R3 | Trust service providers should select the appropriate cryptographic suite at the security level that fits their needs. | should | 5.3.2 |
| R4 | The selection of the cryptographic suite should take the conditions listed in clause 5.2 into account. | should | 5.3.2 |
| R5 | Manufacturers of security devices should implement the secret key algorithms at the specified key sizes. | should | 5.3.3 |
| R6 | There should be trust service providers able to certify the keys, and there should be software support for the selected algorithms (interoperability). | should | 5.3.3 |

## Informative Annexes (Condensed)
- **Annex A (Bibliography)**: Lists Directive 1999/93/EC (repealed by Regulation (EU) No 910/2014 as of 1 July 2016) and ETSI EN 319 162-2 (Additional ASiC containers).