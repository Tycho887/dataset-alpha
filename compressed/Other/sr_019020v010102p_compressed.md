# ETSI SR 019 020: The framework for standardization of signatures; Standards for AdES digital signatures in mobile and distributed environments
**Source**: ETSI | **Version**: V1.1.2 | **Date**: 2016-08 | **Type**: Informative (Special Report)
**Original**: ETSI SR 019 020 V1.1.2 (2016-08)

## Scope (Summary)
Provides a framework for further standardization of creation and validation of AdES digital signatures (CAdES, XAdES, PAdES, ASiC) in mobile and distributed environments assisted by remote servers. Analyzes common usage scenarios (local signing, server signing, split-key signing, validation) and identifies standardization requirements, building on existing OASIS DSS and M-COMM standards. Does not address fully local scenarios or mobile access to other trust services. Security requirements are referenced to CEN TS 419 241.

## Normative References
None.

## Definitions and Abbreviations
### Definitions
- **AdES digital signature**: digital signature format compliant with one of the CAdES, XAdES, PAdES format specifications
- **application provider**: provider of a system, other than the personal device, which prepares document or other information required to be signed
- **communications network**: mobile network or fixed network supporting communications from personal devices to networked services
- **Identity Provider (IdP)**: entity that makes available identity information (see ISO/IEC 24760-1)
- **mobile device**: personal device which can communicate over a mobile network, usually a device suitable for carrying in hand, purse or pocket such as a mobile or smart phone
- **mobile network**: communications network operated specifically for mobile devices, usually requiring a UICC
- **Mobile Network Operator (MNO)**: entity offering mobile network services
- **mobile signature service**: facility that coordinates and manages the process by which an end user can sign a document using a signing key on or connected to a personal device (local signing only)
- **Mobile Signature Service Provider (MSSP)**: provider of a mobile signature service
- **personal device**: a networked device assumed to be under sole control of a natural person at time of signing/validation (includes mobile devices, PCs, tablets, laptops)
- **Secure Element (SE)**: tamper resistant component used in a personal device to provide security, confidentiality, and multiple application environments
- **signer**: entity identified as the creator of a signature
- **signing service**: facility that coordinates and manages the process by which an end user can remotely sign a document using a signing key stored in the signing service remote from the user
- **Signing Service Provider (SSP)**: provider of a signing service
- **Trusted Execution Environment (TEE)**: specific execution environment on the mobile or personal device that defines a boundary between internal secure and external unsecure execution environment (see GlobalPlatform TEE System Architecture)
- **Trusted Service Manager (TSM)**: trusted logical component implementing service management roles for provisioning, life cycle management and deletion of a mobile service
- **validation service**: system accessible via a communication network, which validates a digital signature

### Abbreviations
- AE: Acquiring Entity
- ASiC: Associated Signature Container
- CMS: Cryptographic Message Syntax
- DSS: Digital Signature Service (OASIS)
- DSS-X: OASIS Digital Signature Services-eXtended
- GAA: 3GPP Generic Authentication Architecture
- HMSSP: Home MSSP
- IdP: Identity Provider
- M-COMM: Set of ETSI specifications for mobile commerce
- MNO: Mobile Network Operator
- MSSP: Mobile Signature Service Provider
- NA: Not Applicable
- NFC: Near Field Communications
- OASIS: Organization for the Advancement of Structured Information Standards
- PC: Personal Computer
- PIN: Personal Identification Number
- PKI: Public Key Infrastructure
- RE: Routing Entity
- SCVP: Server-Based Certificate Validation Protocol
- SE: Secure Element
- SIM: Subscriber Identity Module
- SMS: Short Message Service
- SSP: Signing Service Provider
- TEE: Trusted Execution Environment
- TSM: Trusted Service Manager
- TSP: Trust Service Provider
- UICC: Universal Integrated Circuit Card
- URI: Uniform Resource Identifier
- VE: Verifying Entity
- VS: Validation Service scenario
- XKISS: XML Key Information Service Specification
- XKMS: W3C XML Key Management Specification
- XML: eXtensible Markup Language

## Usage Scenarios for Signing
### Introduction
Clause 4 identifies features classifying scenarios and models common implementations for digital signature creation in distributed environments. Differentiates local signing (key in personal device) from server signing (key in remote server). Also includes split-key scenario. All scenarios show synchronous interactions; asynchronous can be derived.

### Actors
- User (signer)
- Personal device
- Mobile Signature Service Provider (MSSP)
- Signing service provider (SSP)
- Validation service
- Application provider
- Identity provider (IdP)
- Trusted Service Manager (TSM)

### Features
Used to distinguish scenarios:
- a) Document creation location
- b) Hashing location
- c) What is displayed to user (document/hash/summary)
- d) Sole control location
- e) Key holding and signature value computation location
- f) If local: within SE, TEE, external device, other trusted environment
- g) AdES completion steps location
- h) Signer authentication method
- i) Mobile network specific or not
- j) Applicability to any personal device or just mobile
- k) Multiple communication channels involved

### Local Signing Scenarios
#### L1: Digital signature value generation in personal device
- Document exists on personal device. Digest computed by MSSP. Digital signature value computed by personal device. AdES built by MSSP.
- Key held in personal device (SE, TEE, external device, etc.). MSSP may communicate over mobile network.
- Additional channel possible for signature request (e.g., SMS).

#### L2: Digital signature value generation in personal device with application provider / MSSP interaction
- Document exists at application provider. MSSP activity triggered by application provider. Digest computed by MSSP (or application provider). Digital signature value computed by personal device. AdES built by MSSP.
- Typical of M-COMM specifications. Interface between application provider and MSSP specified; MSSP-to-personal device interface not specified (out of scope).

#### L3: AdES completely generated in a personal device
- Document exists at application provider. MSSP activity triggered by application provider. AdES generated by personal device. Personal device may compute hash, create digital signature value, and build AdES. MSSP passes AdES to application provider.
- User consent on personal device.

### Server Signing Scenarios
#### S1: Generation of AdES in a server
- Personal device requests signature from signing service that holds user's signing key in cryptographic module. Document may be generated locally or by application provider. Hashing and AdES creation may be done by personal device or signing service.
- Signer authenticated to signing service.

#### S2: Generation of AdES in a server with multi-channel
- Extends S1: uses different channels for authentication and signature activation (e.g., Internet for request, mobile network for confirmation). Signature activation data sent to personal device. Sole control may be on computing device or personal device.

### LS: Split local and server signing scenario (threshold cryptography)
- Private key split between personal device and signing service. Pre-digital signature value created on personal device, completed by signing service. AdES can be generated by either.

## VS: Validation Service Scenario
User receives signed document on personal device, requests validation from remote validation service. Validation results presented to user. Variant: only certificate validation performed remotely. Validation can also be requested directly from application provider.

## Further Standardization Requirements
### Requirements on Protocols for Signing and Validation
The protocols used for the scenarios in clauses 4 and 5 **should** fulfil the following requirements:
1. Work with any identification/authentication scheme provided assurance level meets requirements of CEN TS 419 241.
2. Support signature activation protocol requirements as identified in CEN TS 419 241.
3. Allow requests for signature generation, augmentation, and validation.
4. Allow requests according to constraints specified in a signature policy.
5. Allow generation of CAdES, XAdES, PAdES, or ASiC containers fully compliant with standards.
6. Allow generation of AdES with incorporated time-stamp and certificate status information.
7. Allow request to compute digest to be signed by (secure) signature creation device on personal device.
8. Allow request to build AdES based on digital signature value computed at personal device.
9. Allow inclusion of visual representation of AdES at specified place (visible signatures).
10. Permit both synchronous and asynchronous communication where possible.
11. Prevent man-in-the-middle and other attacks resulting in fraudulent signatures.
12. Incorporate mechanisms verifying personal device is under signer's control at signing time.
13. When document displayed on separate device, ensure link between act of signing and displayed document.
14. Allow multiple communication channels.
15. When multiple channels used, consider security implications of attacks on one channel.
16. Support split-key solutions.
17. When requesting validation, allow detailed validation report aligned with ETSI EN 319 102-1 and ETSI EN 319 102-2.
18. When requesting validation, allow signed validation report.
19. Identify and authenticate any service involved towards user/personal device.

### Requirements Related to Service Life Cycle Management
#### Use Cases for Life Cycle of User Subscription to MSSP/SSP
- Subscription, activation, suspension, resumption, certificate revocation/renewal, termination/unsubscription. Each may require interaction with certification authority and MNO.

#### Use Cases for Events Related to Mobile Device and MNO
- Secure element change, phone number change, device change, mobile subscription termination, MNO swap. May affect certificates and service continuity.

### Standardization Requirements and Rationalized Framework (Table 9)
| Area | Local signing (L1, L2, L3) | Signing service (S1, S2) | Split-key (LS) | Validation service (VS) |
|------|----------------------------|--------------------------|----------------|-------------------------|
| 1. Signature creation/validation | Existing standards + **New: ETSI TS 119 152** | Existing + **New: ETSI TS 119 152** | Existing + **New: ETSI TS 119 152** | Existing + **New: ETSI TS 119 152** |
| 2. Signature creation devices | CEN EN 419 211, 419 212 | CEN EN 419 221, **CEN EN 419 241** | CEN EN 419 221, 419 212 | CEN EN 419 221 |
| 3. Cryptographic suites | ETSI TS 119 312 | ETSI TS 119 312 | To be determined | ETSI TS 119 312 |
| 4. Trust service providers | No policy req. (note 1) | **New: ETSI TS 119 431, TS 119 432**, ETSI EN 319 401, 319 403 | See note 4 | **New: ETSI TS 119 441, TS 119 442**, ETSI EN 319 401, 319 403 |
| 5. Trust application service providers | Not applicable | Not applicable | Not applicable | Not applicable |
| 6. Trust service status list | See note 1 | Extension to ETSI TS 119 612 may be needed | Note 4 | Extension to ETSI TS 119 612 may be needed |
*Note 1: Assuming signature validated after creation, MSSP does not need to be trusted.*
*Note 4: Architecture document needed for interaction between TSP and other elements; not necessary for validation service.*

### Scope of New Standards Identified
#### ETSI TS 119 152: Architecture for digital signatures in distributed environments
- Specifies architecture for creation of AdES in distributed environments using protocols from TS 119 432 and TS 119 442, and M-COMM. Identifies functional elements and interactions. Supports eIDAS electronic signatures and seals.

#### CEN EN 419 241: Trustworthy Systems Supporting Server Signing
- Security requirements for systems generating advanced electronic signatures (server signing), including protection profiles for compliance with eIDAS Annex II (Qualified Signature Creation Devices).

#### ETSI TS 119 431: Policy and security requirements for TSPs providing AdES digital signature generation services
- Policy requirements building on ETSI EN 319 401 for signature generation where private keys are stored in TSP hardware modules. Takes into account CEN TS/EN 419 241.

#### ETSI TS 119 441: Policy and security requirements for TSPs providing AdES digital signature validation services
- Policy requirements for TSPs providing validation services, referencing ETSI EN 319 401.

#### ETSI TS 119 432: Protocol profiles for TSPs providing AdES digital signature generation services
- Multi-part document profiling M-COMM and DSS protocols:
  - Part 1: Trusted Service Manager (life cycle management)
  - Part 2: Local signing on personal device (based on M-COMM)
  - Part 3: Local signing on general computing device (based on OASIS DSS)
  - Part 4: Remote signing (based on OASIS DSS, supporting level 1 and 2 sole control per CEN TS 419 241)

#### ETSI TS 119 442: Protocol profiles for TSPs providing AdES digital signature validation services
- Profile for formats and protocols used by validation services, based on OASIS DSS, possibly augmented by XKMS, RFC 3029, RFC 5055.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Work with any identification/authentication scheme provided assurance level meets CEN TS 419 241 | should | Clause 6.1 #1 |
| R2 | Support signature activation protocol per CEN TS 419 241 | should | Clause 6.1 #2 |
| R3 | Allow requests for signature generation, augmentation, validation | should | Clause 6.1 #3 |
| R4 | Allow requests according to signature policy constraints | should | Clause 6.1 #4 |
| R5 | Allow generation of CAdES, XAdES, PAdES, or ASiC fully compliant | should | Clause 6.1 #5 |
| R6 | Allow generation of AdES with time-stamp and certificate status | should | Clause 6.1 #6 |
| R7 | Allow request to compute digest for signing by secure device on personal device | should | Clause 6.1 #7 |
| R8 | Allow request to build AdES based on locally computed signature value | should | Clause 6.1 #8 |
| R9 | Allow inclusion of visible signature representation | should | Clause 6.1 #9 |
| R10 | Permit synchronous and asynchronous communication | should | Clause 6.1 #10 |
| R11 | Prevent man-in-the-middle and other attacks | should | Clause 6.1 #11 |
| R12 | Verify personal device under signer's control at signing time | should | Clause 6.1 #12 |
| R13 | Ensure link between act of signing and displayed document when separate | should | Clause 6.1 #13 |
| R14 | Allow multiple communication channels | should | Clause 6.1 #14 |
| R15 | Consider security implications of attacks on one channel | should | Clause 6.1 #15 |
| R16 | Support split-key solutions | should | Clause 6.1 #16 |
| R17 | Allow detailed validation report aligned with EN 319 102-1/2 | should | Clause 6.1 #17 |
| R18 | Allow signed validation report | should | Clause 6.1 #18 |
| R19 | Identify and authenticate any service involved | should | Clause 6.1 #19 |

## Informative Annexes (Condensed)
### Annex A: Most Relevant Standards
#### A.1 Introduction
Reviews OASIS DSS and M-COMM specifications as basis for remote signature generation and validation.

#### A.2 OASIS DSS and DSS-X specifications
- Defines SignRequest/SignResponse and VerifyRequest/VerifyResponse protocols (Core) plus profiles:
  - **AdES Profile**: generation, validation, upgrade of CAdES and XAdES (not yet PAdES/ASiC)
  - **Asynchronous Profile**: allows pending requests and later pull
  - **Visible Signature Profile**: allows embedding visual representation of signature
  - **Local Signature Computation Profile**: extends Core to allow signature value computation on user's device, server builds AdES
  - **Comprehensive Multi-Signature Verification Reports Profile**: detailed validation reports (not aligned with EN 319 102-1)
- Table A.1 maps DSS profiles to scenarios; for most scenarios, DSS Core + AdES profile + optional profiles needed. Some features (PAdES/ASiC, split-key) require new profiles.

#### A.3 ETSI M-COMM specifications
- Set of specs (2003) for mobile signatures: TR 102 203, TS 102 204, TR 102 206, TS 102 207.
- MSSP communicates with application provider via web service interface. Communication to personal device out of scope.
- Supports synchronous and asynchronous modes.
- Roaming service (TS 102 207) allows application provider to obtain signatures from any user through a mesh of acquiring entities, home MSSPs, routing entities, attribute providers, identity issuers, verifying entities.