# ETSI SR 019 050: Rationalized Framework of Standards for Electronic Registered Delivery Services Applying Electronic Signatures
**Source**: ETSI TC ESI | **Version**: V1.1.1 | **Date**: June 2015 | **Type**: Special Report (Informative)
**Original**: [ETSI SR 019 050](https://www.etsi.org/deliver/etsi_sr/019000_019099/019050/01.01.01_60/sr_019050v010101p.pdf)

## Scope (Summary)
This document provides a proposal for a rationalized framework of standards for electronic registered delivery services as defined by the eIDAS Regulation [i.4], aligned with the principles of ETSI TR 119 000 [i.15]. It analyzes features, service models, and existing specifications to identify gaps and recommends a structure of future standardization documents along with a work plan.

## Normative References
- Not applicable. (No normative references are cited in this document.)

## Informative References (Selected)
- [i.4] Regulation (EU) No 910/2014 (eIDAS)
- [i.5] CEN/TS 16326:2013 (Postal Registered Electronic Mail)
- [i.6] ETSI TS 119 612 (Trusted Lists)
- [i.7]–[i.14] ETSI TS 102 640 series (REM)
- [i.15] ETSI TR 119 000 (Rationalized structure for eSignature standardization)
- [i.30] European Interoperability Framework (EIF)
- [i.31] Regulation (EU) No 283/2014 (eTelNet)
- [i.36] ISO/IEC 13888-3 (Non-repudiation)
- [i.38] ETSI EN 319 401 (General Policy Requirements for TSPs)
- [i.39] ETSI TR 103 071 (REM test suite)
- [i.40] ETSI TS 102 231 (Trust-service status information)
- [i.41] ISO 15459 (Unique identifiers)
- [i.42] IETF RFC 5424 (Syslog Protocol)
- [Plus 40+ other informative references listed in clause 2.2]

## Definitions and Abbreviations

### Definitions (selected, precedence over other sources)
- **electronic registered delivery**: transmission of data by electronic means providing evidence relating to handling, including proof of sending or receiving, and protecting against loss, theft, damage, or unauthorised alterations.
- **electronic registered delivery service (eRDS)**: service providing electronic registered delivery.
- **end entity**: message sender and recipient (user or system).
- **(qualified) electronic registered delivery management domain ((Q)eRDMD)**: set of technical and physical components, personnel, policies, and processes that provide (qualified) electronic registered delivery services within a network.
- **(qualified) electronic registered delivery network**: network of interconnected (qualified) eRDMDs federated in a trust circle.
- **qualified electronic registered delivery service (QeRDS)**: eRDS meeting the requirements laid down in Article 42 of eIDAS Regulation [i.4].
- **qualified trust service**, **qualified trust service provider**, **trust service**, **trust service provider** – as defined in eIDAS Regulation.
- **trust application service provider**: TSP operating a value added trust service based on electronic signatures (covers REM, eRDS, preservation services).
- **registered electronic mail service**: eRDS based on electronic mail technology.

### Abbreviations (selected)
| Abbreviation | Full Term |
|--------------|-----------|
| eRDS | Electronic Registered Delivery Service |
| eRDMD | Electronic Registered Delivery Management Domain |
| (Q)eRDMD | Qualified eRDMD |
| REM | Registered Electronic Mail |
| LSP | Large Scale Pilot |
| PEPPOL | Pan-European Public eProcurement On-Line |
| SPOCS | Simple Procedures Online for Cross-border Services |
| e-CODEX | e-Justice Communication via Online Data Exchange |
| ebMS | ebXML Messaging Services |
| TSL | Trust-service Status List |
| SML/SMP | Service Metadata Locator/Publisher |
| EIF | European Interoperability Framework |

## 5 Features
Table 1 (condensed) identifies features of electronic (registered or not) delivery solutions. Features are categorized by name, alternative terms, entities involved, scope, and description. Key features include: end-entity authentication, node authentication, non‑repudiation, confidentiality, integrity, reliable delivery, antivirus, antispam, time reference, electronic signature provision, service trust, service discovery, user discovery, address management, translation, semantic check, structured/non‑structured contents, service level negotiation, evidence validation, electronic signature validation, deadlines, and governance (policy).

## 6 Electronic Registered Delivery Service Model

### 6.1 Introduction
A high-level model is presented for further elaboration; not intended to impose specific requirements.

### 6.2 Basic Service Model
- **Sender authenticates** → submits message with options → service tracks submission (submission evidence) → message made available to recipient → service tracks consignment (consignment evidence) → evidence stored/sent to sender → recipient authenticates → gets message.

### 6.3 Distributed Service Model
- Multiple eRDMDs interact: sender submits to own eRDMD → discovery/negotiation (routing, capabilities, trust) → message dispatched to recipient’s eRDMD → relay evidence → delivery → consignment evidence returned → recipient retrieves.

### 6.4 Extended Service Model (4‑corner model)
- Adds interoperability layer: sender side (non‑interoperable solution + translation gateway), interoperable network of gateways, recipient side. Used in LSPs like SPOCS, e‑SENS, e‑CODEX.

### 6.5 Roles in eRDMD
Core roles: Message transfer and routing, Message store, Evidence provider, End‑entity registration.
Ancillary roles: Identity provider, Signature creation/validation, Malware/spam protection, Certification authority, Time certification, Service discovery/negotiation.
Optional roles: Message repository, Evidence validation, Message gateway, Message interpretation/transformation, End‑entity directory.

Table 2 maps features to roles (see original clause 6.5).

### 6.6 Implications to Standards
Three key interactions between eRDMDs: service discovery/negotiation, payload delivery, evidence & identification exchange. Specification needed in content semantics, syntax, and protocol. Table 3 classifies each interaction as “out of scope,” “in scope,” or “partially in scope.”

- **Routing**: out of scope.
- **Capabilities/requirements**: content semantics in scope; syntax partially in scope; protocol (binding) in scope.
- **Trust establishment**: content semantics in scope; syntax partially in scope; protocol partially in scope.
- **Payload delivery**: out of scope (existing protocols).
- **Meta‑information exchange**: semantics/syntax in scope; protocol (binding) in scope.
- **User identity exchange**: profiling of existing tokens (e.g., SAML, X.509) and binding required.
- **Evidence exchange**: semantics/syntax for evidence (PDF/XML) in scope; push/pull bindings required.

## 7 Inventory of Existing Specifications
Annex B provides the detailed inventory (not reproduced). It covers international, European, and sector standards for core e‑delivery services. National/commercial solutions excluded.

## 8 Rationalized Structure for e‑Delivery Standards

### 8.1 Classification Scheme
The structure follows the model of ETSI TR 119 000 (five document types: guidance, policy & security requirements, technical specifications, conformity assessment, testing). Sub‑areas within Trust Application Service Providers (area 5) are: Data preservation, Electronic registered delivery services, and Registered electronic mail (REM).

### 8.2 Proposed Standards Aligned with Rationalized Framework

#### Guidance
| ID | Title | Type |
|----|-------|------|
| ETSI TR 119 500 | Business Driven Guidance for Trust Application Service Providers (to include e‑delivery guidance) | TR |

#### Policy & Security Requirements
| ID | Title | Parts |
|----|-------|-------|
| ETSI EN 319 521 | Policy & Security Requirements for Electronic Registered Delivery Service Providers | Part 1: non‑qualified; Part 2: qualified |
| ETSI EN 319 531 | Policy & Security Requirements for Registered Electronic Mail (REM) Service Providers | Part 1: non‑qualified; Part 2: qualified (conditioned on REM‑specific requirements) |

#### Technical Specifications
| ID | Title | Parts |
|----|-------|-------|
| ETSI EN 319 522 | Electronic Registered Delivery Services | 1: Framework/Architecture; 2: Semantic Contents; 3: Formats; 4: Bindings (multi‑part, open); 5: Technical Specs for Qualified e‑Delivery |
| ETSI EN 319 532 | Registered Electronic Mail (REM) Services | 1: Framework/Architecture; 2: Semantic Contents; 3: Formats (S/MIME on SMTP); 4: Interoperability Profiles (SMTP, UPU PReM) |

#### Testing Conformance & Interoperability
| ID | Title | Parts |
|----|-------|-------|
| ETSI TS 119 504 | General Requirements for Testing Trust Application Services | General for TASPs |
| ETSI TS 119 524 | Testing Conformance & Interoperability of Electronic Registered Delivery Services | 1: Interoperability test suites; 2: Conformance tests |
| ETSI TS 119 534 | Testing Conformance & Interoperability of Registered Electronic Mail Services | 1: Interop (same format/transport); 2: Interop (different formats); 3: Conformance |

## 9 Analysis and Work Plan

### 9.2 Analysis for Trust Application Service Providers Area
Tables 5–8 provide a detailed gap analysis and work plan for each proposed deliverable. The overall plan indicates that many existing specifications (e.g., REM suite) serve as starting points; new documents are needed for generic e‑delivery (EN 319 521, EN 319 522, etc.). Timescales are given as T0 (start) + months (e.g., T0+12+12 for EN 319 522).

## Informative Annexes (Condensed)

- **Annex A (Pan‑European solutions)**: Summarizes seven LSPs and platforms: SPOCS, e‑SENS, epSOS, PEPPOL, e‑CODEX, e‑TrustEx. Each uses a four‑corner model and provides details on transport, security, discovery, evidence.
- **Annex B (Inventory)**: Contains the full list of known standards and specifications (provided in separate archive sr_019050v010101p0.zip).
- **Annex C (Bibliography)**: Lists over 60 additional references including EU directives, IETF RFCs, ISO standards, and academic papers.

## Requirements Summary
*(No explicit normative requirements in this SR; the rationalized framework proposes future standards. The following table summarises key proposed documents and their status.)*

| ID | Proposed Document | Type | Based On / Starting Point | Status |
|----|-------------------|------|--------------------------|--------|
| R1 | EN 319 521-1 | Policy | REM TS 102 640-3 | Input exists |
| R2 | EN 319 522-1 | Technical | REM TS 102 640-1 | Little basis |
| R3 | EN 319 522-2 | Technical | (new) | Little basis |
| R4 | EN 319 522-3 | Technical | (new) | Little basis |
| R5 | EN 319 522-4 | Technical | REM TS 102 640-6 | Input exists for some bindings |
| R6 | EN 319 532 | Technical | REM TS 102 640 series | Scope almost fully met |
| R7 | TS 119 524 | Testing | REM TR 103 071 | Some inputs exist |

*(Full analysis and work plan in clause 9 tables.)*