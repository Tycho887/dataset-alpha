# ETSI TR 119 500 V1.1.1 (2019-02): Business Driven Guidance for Trust Application Service Providers
**Source**: ETSI | **Version**: V1.1.1 | **Date**: February 2019 | **Type**: Informative (Technical Report)
**Original**: http://www.etsi.org/standards-search (DTR/ESI-0019500)

## Scope (Summary)
This Technical Report provides guidance on selecting standards for Trust Application Service Providers (TASP) (Area 5 of the framework defined in ETSI TR 119 000). It describes Business Scoping Parameters relevant to TASP and how to identify appropriate standards and options based on these parameters. Target audience includes business managers, application architects, and developers.

## Normative References
None applicable.

## Informative References
- [i.1] ETSI TR 119 000: "Electronic Signatures and Infrastructures (ESI); The framework for standardization of signatures: overview"
- [i.2] ETSI EN 319 521: "Policy and security requirements for Electronic Registered Delivery Service Providers"
- [i.3] ETSI EN 319 522-1: "Electronic Registered Delivery Services; Part 1: Framework and Architecture"
- [i.4] ETSI EN 319 522-2: "Electronic Registered Delivery Services; Part 2: Semantic contents"
- [i.5] ETSI EN 319 522-3: "Electronic Registered Delivery Services; Part 3: Formats"
- [i.6] ETSI EN 319 522-4-1: "Electronic Registered Delivery Services; Part 4: Bindings; Sub-part 1: Message delivery bindings"
- [i.7] ETSI EN 319 531: "Policy and security requirements for Registered Electronic Mail Service Providers"
- [i.8] ETSI EN 319 532-1: "Registered Electronic Mail (REM) Services; Part 1: Framework and architecture"
- [i.9] ETSI EN 319 532-2: "Registered Electronic Mail (REM) Services; Part 2: Semantic Contents"
- [i.10] ETSI EN 319 532-3: "Registered Electronic Mail (REM) Services; Part 3: Formats"
- [i.11] ETSI EN 319 532-4: "Registered Electronic Mail (REM) Services; Part 4: Interoperability profiles"
- [i.12] Regulation (EU) N 910/2014 (eIDAS)
- [i.13] ETSI TR 119 100: "Guidance on the use of standards for signature creation and validation"
- [i.14] ETSI TR 119 001: "The framework for standardization of signatures; Definitions and abbreviations"
- [i.15] ETSI EN 319 401: "General Policy Requirements for Trust Service Providers"
- [i.16] Directive 1999/93/EC (repealed by [i.12])
- [i.17] ETSI EN 319 522-4-2: "Bindings; Sub-part 2: Evidence and identification bindings"
- [i.18] ETSI EN 319 522-4-3: "Bindings; Sub-part 3: Capability/requirements bindings"
- [i.19] ETSI TS 119 524-1: "Testing Conformance and Interoperability of ERD Services; Part 1: Testing conformance"
- [i.20] ETSI TS 119 524-2: "Testing Conformance and Interoperability of ERD Services; Part 2: Test suites for interoperability testing"
- [i.21] ETSI TS 119 534-1: "Testing Conformance and Interoperability of REM Services; Part 1: Testing conformance"
- [i.22] ETSI TS 119 534-2: "Testing Conformance and Interoperability of REM Services; Part 2: Test suites for interoperability testing"
- [i.23] ETSI SR 001 604: "Rationalised Framework for Electronic Signature Standardisation"

## Definitions and Abbreviations
- **Electronic Registered Delivery Service (ERDS)**: electronic service that transmits data between sender and recipients by electronic means, providing evidence of handling, and protecting against loss, theft, damage, or unauthorized alterations.
- **ERDS evidence**: data generated within an ERDS aiming to prove occurrence of a certain event at a certain time.
- **ERDS practice statement**: statement of practices employed by an ERDSP in providing its service.
- **Electronic Registered Delivery Service Provider (ERDSP)**: trust service provider providing ERDS (may be a TSP under eIDAS).
- **Qualified Electronic Registered Delivery Service (QERDS)**: as specified in eIDAS.
- **Qualified Electronic Registered Delivery Service Provider (QERDSP)**: provider of QERDS.
- **Registered Electronic Mail (REM)**: specific type of ERDS building on ordinary e-mail formats, protocols, and mechanisms.
- **REMSP**: Registered Electronic Mail Service Provider.
- **Data Preservation Service (DPS)**: service maintaining data integrity, authenticity, and legibility over a storage period.
- **TASP**: Trust Application Service Provider (value-added trust service applying digital signatures).
- **TSP**: Trust Service Provider.
- **CAB**: Conformity Assessment Body.

## 4 Overview of TASP Standardization

### 4.1 What is a TASP?
A TASP operates a value-added trust service applying digital signatures that rely on generation/validation of digital signatures in normal operation. Includes registered e-mail, e-delivery services, and long-term storage services. TASPs are Trust Service Providers.

### 4.2 Types of Trust Application Service

#### 4.2.1 ERDS
- ERDS provides secure, reliable delivery of electronic messages with evidence for legal accountability.
- Evidence may be delivered immediately or stored in a repository.
- Framework aims to cover common requirements independent of legislative framework and to support eIDAS compliance.
- Standards: ETSI EN 319 521, 319 522 (parts 1-4), TS 119 524 (parts 1-2).

#### 4.2.2 REM
- REM builds on ordinary e-mail protocols and adds evidence of shipment, delivery, non-delivery, retrieval, etc.
- Standards: ETSI EN 319 531, 319 532 (parts 1-4), TS 119 534 (parts 1-2). All REM standards reference ERDS standards where applicable.

#### 4.2.3 Data Preservation Service (DPS)
- DPS ensures integrity, authenticity, and legibility throughout storage. To be detailed in future version.

#### 4.2.4 Other potential Trust Application Services
- None identified so far.

### 4.3 Aspects Requiring Standardization

#### 4.3.1 Policy & Security Requirements
- Trustworthiness requires TASP practices meeting recognized best practices; qualified TASPs must meet regulatory requirements.
- Standardization provides a recognized level of trust; standards are related to TASP Policies and Practices.

#### 4.3.2 Technical Specifications
- Data must be protected against loss, theft, damage, unauthorized alterations. ETSI EN 319 401 applies.

#### 4.3.3 Conformity Assessment
- Independent CAB assesses TASP policies and practices against standards; required for formal recognition (supervisory body, commercial organization, or association).

## 5 Introduction to the Selection Process
- Guidance based on analyzing business requirements into Business Scoping Parameters.
- Stakeholders identify TASP scoping parameters, then map to applicable standards and technical rules.
- Risk analysis and policy requirements addressed in policy/security documents (e.g., ETSI EN 319 401).
- Even providers of specific services (e.g., REM) must consider overall requirements.

## 6 Business Scoping Parameters

### 6.1 Overview
- Process based on ETSI TR 119 000 and TR 119 100.
- Analysis of business requirements and risks leads to policy/security requirements and selection of standards.
- Inter-area dependencies stated via scoping parameters.

### 6.2 Scoping the Trust Application Processes and/or Services
- **Organizational parameters**: business context (domain, process, risks), budgetary constraints, security policies, legal requirements, risk mitigation, target community (global, EU, national, sector).
- **Trust application services parameters**: scope includes business processes, assets, interfaces, roles.
- **Organization's security parameters**: assess assets, treat risks, select controls.
- **Digital signature specific parameters**: as described in ETSI TR 119 100.

## 7 Selecting the Most Appropriate Standards and Options

### 7.1 Introduction
- Selection depends on applying scoping factors to the service or process.
- TASP selects standards and determines all necessary controls.

### 7.2 Illustration of Application of Standards

#### 7.2.1 ERDS – Standards applicable as indicated by "x":

| Standard | Conformity Assessment | Policy & practices (including security) | Provisions on ERDSP | Provisions on EU qualified ERDSP | Evidence: semantics and format | Interoperability profiles, formats and bindings |
|---|---|---|---|---|---|---|
| ETSI EN 319 401 | X | X | | | | |
| ETSI EN 319 521 | X | X | X | X | | |
| ETSI EN 319 522-1 | X | X | X | X | | |
| ETSI EN 319 522-2 | | | | | X | |
| ETSI EN 319 522-3 | | | | | X | X |
| ETSI EN 319 522-4-1 | | | | | | X |

#### 7.2.2 REM – Standards applicable as indicated by "x":

| Standard | Conformity Assessment | Policy & practices (including security) | Provisions on REMSP | Provisions on EU qualified REMSP | Evidence: semantics and format | Interoperability profiles, formats and bindings |
|---|---|---|---|---|---|---|
| ETSI EN 319 401 | X | X | | | | |
| ETSI EN 319 531 | X | X | X | X | | |
| ETSI EN 319 532-1 | X | X | X | X | | |
| ETSI EN 319 532-2 | | | | | X | |
| ETSI EN 319 532-3 | | | | | X | X |
| ETSI EN 319 532-4 | | | | | | X |

#### 7.2.3 Data Preservation Service
- To be described in a future version.

## Requirements Summary
This document is informative (Technical Report); it contains no normative requirements. All "should" and "may" are interpreted per ETSI Drafting Rules. The guidance is non-binding.

## Informative Annexes (Condensed)
None present. The document contains no annexes; the "History" section records publication in February 2019.