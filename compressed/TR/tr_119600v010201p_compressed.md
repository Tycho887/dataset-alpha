# ETSI TR 119 600: Electronic Signatures and Infrastructures (ESI); Guidance on the use of standards for trust service status lists providers
**Source**: ETSI | **Version**: V1.2.1 | **Date**: 2016-03 | **Type**: Informative (Technical Report)
**Original**: RTR/ESI-0019600v121

## Scope (Summary)
Provides guidance on selecting standards and their options for organizations wishing to establish a trust service status list (TSL) or trusted list (TL), tailored to business implementation context and associated requirements. Describes business scoping parameters and identifies relevant standards.

## Normative References
Not applicable.

## Informative References
- [i.1] Directive 1999/93/EC (repealed 1 July 2016 by [i.2])
- [i.2] Regulation (EU) No 910/2014 (eIDAS)
- [i.3] ETSI TS 119 612: "Trusted Lists"
- [i.4] Commission Decision 2009/767/EC (measures for electronic procedures)
- [i.5] ETSI EN 319 411 (all parts): "Policy and security requirements for TSPs issuing certificates"
- [i.6] Regulation 765/2008 (accreditation and market surveillance)
- [i.7] Commission Decision 2010/425/EU (amending [i.4])
- [i.8] Commission Decision 2013/662/EU (amending [i.4])
- [i.9] ETSI TS 102 231: "Provision of harmonized Trust-service status information"
- [i.10] ETSI TS 119 611: "Policy & security requirements for trusted lists providers"
- [i.11] ETSI TS 119 602: "Trust service status lists"
- [i.12] ETSI TS 119 172 (all parts): "Signature Policies"
- [i.13] ETSI TS 119 603: "Conformity assessment of trust service status lists providers"
- [i.14] ETSI TS 119 613: "Requirements for conformity assessment bodies assessing trusted lists providers"
- [i.15] ETSI TS 119 614: "Testing conformance & interoperability of trusted lists"
- [i.16] Commission Implementing Decision (EU) 2015/1505 (technical specifications for trusted lists under [i.2])

## Definitions and Abbreviations

### Definitions
- **advanced electronic seal**: as defined in Regulation (EU) No 910/2014 [i.2]
- **advanced electronic signature**: as defined in Regulation (EU) 910/2014 [i.2]
- **advanced electronic signature under e-signature Directive**: as defined in Directive 1999/93/EC [i.1]
- **digital signature**: data appended to, or a cryptographic transformation of a data unit that allows recipient to prove source and integrity, and protect against forgery
- **electronic signature**: as defined in Regulation (EU) 910/2014 [i.2]
- **non-EU countries**: countries outside the European Union and the European Economic Area
- **trusted list (TL)**: list providing information about status and status history of trust services from TSPs regarding compliance with applicable requirements and legislation; in EUMS context refers to supervision/accreditation status list (as per CD 2009/767/EC amendments or eIDAS); for non-EU or international, a list meeting ETSI TS 119 612 [i.3] requirements
- **trusted list provider**: entity that establishes, maintains, and publishes trusted lists (also called TL issuer or TLSO)
- **trust service**: electronic service enhancing trust and confidence in electronic transactions
- **trust service provider (TSP)**: entity providing one or more trust services
- **trust service status list (TSL)**: form of a signed list as basis for presentation of trust service status information
- **trust service status list provider**: entity that establishes, maintains, and publishes TSLs (also called TSL issuer or TSLSO)
- **trust service token**: physical or binary object generated as a result of using a trust service (e.g., certificates, CRLs, time stamps, OCSP responses)

### Abbreviations
- CA – Certification Authority
- CD – Commission Decision
- CID – Commission Implementing Decision
- CSP – Certification Service Provider
- EC – European Commission
- EEA – European Economic Area
- EU – European Union
- EUMS – European Union Member States
- IPR – Intellectual Property Rights
- LOTL – List Of Trusted Lists
- MS – Member State
- TL – Trusted List
- TLSO – Trusted List Scheme Operator
- TR – Technical Report
- TS – Technical Specification
- TSL – Trust service Status List
- TSLSO – Trust service Status List Scheme Operator
- TSP – Trust Service Provider
- XML – eXtensible Markup Language

## 4 Introduction to Trusted Lists, Trust Service Status Lists, and Their Providers

### 4.1 Trust service and trust service provider
Trust service is an electronic service enhancing trust/confidence, provided by a TSP (third party). TSP issues trust service tokens (e.g., certificates, time stamps, signature services). Trustworthiness depends on level of assurance and security policies. Approval scheme operators publish status information about TSPs under their scheme, possibly relying on conformity assessment bodies.

### 4.2 Trust service status lists and trusted lists

#### 4.2.1 Trust service status lists
TSL is a signed list used to present trust service status information. Approval schemes use TSLs to publish current and historical status about TSPs they oversee. TSLs may also refer to other schemes. Purpose: enhance confidence of relying parties.

#### 4.2.2 Trusted lists
TLs are TSLs providing status and status history of TSPs' compliance with applicable legislation. EU MS TLs established by CD 2009/767/EC (amended) and later by eIDAS Regulation (applicable from 1 July 2016). TLs include qualified and non-qualified services, and enable verification of signature validity. European Commission publishes a List of Trusted Lists (LOTL) with pointers to MS TLs. Technical specifications: up to 30 June 2016 – CD 2009/767/EC (based on TS 119 612 V1.1.1); from 1 July 2016 – CID 2015/1505 (based on TS 119 612 V2.1.1). Non-EU countries/international organizations can adopt same specifications. TLs have four components: provider/scheme info, TSPs, services and current status, status history.

### 4.3 TSL/TL trust model
TSLs/TLs are signed documents; signature verification requires public key. Since scheme is "above" TSPs, public key cannot be certified by any TSP inside/outside scheme. A compiled list of pointers (LOTL) can authenticate each TL by including the public key.

### 4.4 Providers of trust service status list or trusted lists
TSL/TL providers are a specific type of TSP. Their trustworthiness depends on applicable legislation and policy/security requirements.

### 4.5 Aspects of TSL/TL provisioning services subject to standardization
Standardization covers:
- **Policy & security requirements** (e.g., TS 119 611 [i.10])
- **Technical specifications** (common template for status information, e.g., TS 119 612 [i.3], TS 119 602 [i.11])
- **Conformity assessment** (auditing TSL/TL provider practices, e.g., TS 119 603 [i.13], TS 119 613 [i.14])
- **Testing technical conformity & interoperability** (e.g., TS 119 614 [i.15])

## 5 Guidance on the Implementation of TSLs/TLs and Selection of Standards

### 5.1 Business requirements analysis
Analysis should consider:
- Impact of providing status information on relying parties
- Specific business, legislative, geographical context
- Potential mutual recognition with other domains

### 5.2 Policy and security requirements analysis
Addressed in relevant policy requirements document (see clause 5.4).

### 5.3 Business scoping parameters
Selection depends on:
1. **Business domain**:
   - TL for EU MS or EEA country (applicable EU/national legislation)
   - TL for non-EU country or international organization (seeking mutual recognition/interoperability)
   - Other type of TSL
2. Whether formal recognition (independent audit) is required.

### 5.4 Technical implementation and further selection of standards
Standards selection per table 1:

| Topic | TL – EU MS | TL – non-EU & International Organizations | TSLs (Other) |
|---|---|---|---|
| **Practices** | No standard yet (possible future: TS 119 611 [i.10]) | No standard yet (possible future: TS 119 611 [i.10]) | No standard available |
| **List content provisions** | Before 1 July 2016: CD 2009/767/EC as amended (based on TS 119 612 V1.1.1). From 1 July 2016: CID (EU) 2015/1505 (based on TS 119 612 V2.1.1) | Ad hoc rules (can be based on TS 119 612 [i.3]) | Ad hoc (can be based on standards below) |
| **List format** | As above (CD/CID based on TS 119 612) | TS 119 612 [i.3] | TS 102 231 [i.9]; possible future: TS 119 602 [i.11] |
| **List usage** | As above (CD/CID based on TS 119 612). Also TS 119 172 [i.12] | Ad hoc; no standard | Ad hoc |
| **Conformity Assessment for List issuers** | No standard yet (possible future: TS 119 603 [i.13], TS 119 613 [i.14]) | No standard yet (possible future: same) | No standard (possible future: same) |
| **Testing conformance & interoperability** | No standard yet (possible future: TS 119 614 [i.15]) | No standard yet (possible future: same) | No standard |

**Legend**: Items marked with () indicate standards not yet available at time of publication (TS 119 611, TS 119 602, TS 119 603, TS 119 613, TS 119 614).

**NOTE 1**: TS 119 603 and TS 119 613 may be necessary only if formal recognition via conformity assessment is required.

**NOTE 2**: Specific guidance for validating e-signatures against EU MS TLs expected in future part of TS 119 172 [i.12].

**NOTE 3**: TSL/TL providers should consider standards for TSPs supporting digital signatures.

## Informative Annexes (Condensed)
- No formal annexes in this document; clause 4.5 identifies four aspects subject to standardization (policy, technical, conformity assessment, testing).
- Table 1 provides a summary of applicable and future standards per business domain.

## Document History
- V1.1.1: May 2015 (Publication)
- V1.2.1: March 2016 (Publication)