# ETSI TR 103 684: Electronic Signatures and Infrastructures (ESI); Global Acceptance of EU Trust Services
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2020-01 | **Type**: Informative Technical Report  
**Original**: https://www.etsi.org/deliver/etsi_tr/103600_103699/103684/01.01.01_60/tr_103684v010101p.pdf

## Scope (Summary)
This Technical Report presents a study of existing PKI-based trust services schemes worldwide, assessing their possible mutual recognition with EU trust services based on eIDAS Regulation (EU) No 910/2014 and ETSI standards. It identifies a four-pillar methodology (legal context, supervision/audit, best practice, trust representation), analyses 37 national/sectoral PKI schemes, and concludes with 18 recommendations to facilitate cross-border acceptance.

## Normative References
None applicable. (The present document is informative; normative references are not applicable per clause 2.1.)

## Definitions and Abbreviations
Key abbreviations used in this document:
- **CA**: Certification Authority
- **CAB**: Conformity Assessment Body
- **CPS**: Certification Practice Statement
- **eIDAS**: Regulation (EU) 910/2014 on electronic identification and trust services
- **ETSI**: European Telecommunications Standards Institute
- **FPKI**: US Federal PKI
- **IMRT-WG**: International Mutual Recognition Technical Working Group
- **PKI**: Public Key Infrastructure
- **QTS**: Qualified Trust Service
- **QTSP**: Qualified Trust Service Provider
- **TSP**: Trust Service Provider
- **TSL**: Trusted Service List (equivalent to Trusted List)
- **UNCITRAL**: United Nations Commission on International Trade Law

For full terms, see ETSI TR 119 001 [i.55].

## 1 Scope (Full Text)
The present document presents the results of a study examining existing trust services and trust service providers that operate in different regions of the world, and their possible mutual recognition/global acceptance. In particular, the study aims to identify further steps which could be taken to facilitate cross recognition between EU trust services, based on ETSI standards supporting the eIDAS Regulation (EU) No 910/2014 [i.4], and trust services from other schemes. The study concentrates on existing PKI-based trust services as these are the most prevalent across the world. The present document first identifies the methodology used in the comparison of other PKI-based trust services with those defined in the existing ETSI standards based around the four main elements of a trust service: legal context, supervision and audit, best practice and trust representation. Then the information collected concerning major PKI-based trust service schemes around the world and how they relate to the European trust service scheme based on eIDAS and ETSI standards is presented. The approaches to PKI across the globe are analysed to identify enablers and barriers to mutual recognition. Finally, conclusions are presented on steps that could be taken to facilitate mutual recognition.

## 2 References
### 2.1 Normative references
Not applicable in the present document.
### 2.2 Informative references
The following documents are referenced in the study (see original document for full list of 66 items):
- [i.4] Regulation (EU) 910/2014 (eIDAS)
- [i.5] Commission Implementing Decision (EU) 2015/1506
- [i.6] Commission Implementing Decision (EU) 2016/650
- [i.31] CA/Browser Forum Baseline Requirements
- [i.38] ETSI TS 101 456
- [i.39] ETSI TS 101 861
- [i.40] ETSI TS 102 042
- [i.41] ETSI TS 102 023
- [i.44] ETSI TS 102 231
- [i.53] ETSI TS 119 612 (Trusted Lists)
- [i.54] ETSI EN 319 403 (Conformity Assessment)
- [i.58] ETSI EN 319 411-1
- [i.59] ETSI EN 319 411-2
- [i.60] ETSI EN 319 412 (Certificate Profiles)
- [i.61] ETSI EN 319 421
- [i.62] ETSI EN 319 422
- [i.64] Directive 1999/93/EC
- [i.65] Recommendation ITU-T X.509

## 3 Study Methodology (Clause 4)
### 4.1 Introduction
Trust service reliability depends on legal/regulatory provisions, practices, technology, and control mechanisms. Comparability of levels of reliability enables cross-model recognition and cross-border transactions.
### 4.2 Four Areas of Comparison
| Pillar | Key Aspects |
|--------|-------------|
| **Legal context** | Regulatory vs. agreement-based; target community; trust service type; legal effects; requirements on TSP |
| **Supervision and auditing** | Oversight entity; audit requirements on TSP; auditor accreditation; lifecycle coverage (initiation, normal, termination) |
| **Best practice** | Technical standards; certificate policies; interoperable protocols; equivalent security levels |
| **Trust representation** | Trusted lists (e.g., ETSI TS 119 612), trust stores, cross-certification, bridge mechanisms |

### 4.3 Comparison Process
i) Identify differences and issues; ii) Analyse causes; iii) Solve issues; iv) Implement changes. Process may be iterative.
### 4.4 Equivalence vs. Strict Compliance
Comparison should assess *equivalence* of reliability levels, not identical compliance.
### 4.5 Study Methodology
Collected information via questionnaires, workshops (Dubai, Tokyo, Mexico City, New York), and desktop research; presented per four pillars; identified enablers/barriers; proposed solutions.

## 4 Information Collected on Existing PKI-Based Trust Services Schemes (Clause 5)
### 5.1 Introduction
Survey includes international frameworks, sector-specific PKIs, and national schemes from South America, Middle East & Africa, Asia/Pacific, North America, and other regions (Russia, Switzerland).

### 5.2 International Legal Framework & Standards
#### 5.2.1 UNCITRAL
- **Legal context**: MLEC, MLES – functional equivalence for electronic signatures, model laws fostering cross-border recognition. Working Group IV developing Draft Provisions on cross-border IdM and Trust Services, heavily based on eIDAS.
- **Supervision/audit**: Proposed white list (ex ante) vs. ex post recognition via predetermined criteria (technologically neutral). Accreditation scheme needed.
- **Best practice**: Technology neutrality; legal toolbox concept defining reliability levels.
- **Trust representation**: No current consensus.
- **Enablers**: Clear liability frameworks; harmonised legal recognition.

#### 5.2.2 ISO 21188
- Financial services PKI practices and policy framework. Equivalence to ETSI EN 319 411-1.

#### 5.2.3 ISO/IEC CD 27099
- Under development; based on ISO 21188; comparable to ETSI EN 319 411-1.

#### 5.2.4 WebTrust for CAs
- **Legal context**: Contractual, adopted by major browsers. Licensed practitioners by CPA Canada.
- **Supervision/audit**: Self-contained qualification scheme; audits past performance; no formal accreditation by national accreditation body.
- **Best practice**: Based on ISO 21188 and CA/Browser Forum.
- **Trust representation**: WebTrust seal on CA website; trust store consumption by browsers.

#### 5.2.5 CA/Browser Forum
- **Legal context**: Agreement between CAs and application providers (browsers). Standards for website authentication, secure email, code signing.
- **Supervision/audit**: Requires WebTrust or ETSI-based audits; application providers act as equivalent supervisory authorities via root stores.
- **Best practice**: Baseline Requirements [i.31] and EV Guidelines [i.32]; aligned with ETSI standards.
- **Trust representation**: Root stores managed by Google, Apple, Microsoft, Mozilla.
- **Enablers**: Close alignment with ETSI.
- **Barriers**: Qualified certificates not automatically recognized per se – must also meet CA/B Forum requirements.

#### 5.2.6 IMRT-WG
- Informal group (Japan, North America, EU) aiming to identify methodology for mutual recognition; plans case studies (e.g., bridge certificates and trusted list mapping).

#### 5.2.7 Kantara Initiative
- **Legal context**: Commercial consortium.
- **Supervision/audit**: Accreditation of credential service providers and assessors; based on NIST SP 800-63-3 [i.30].
- **Trust representation**: Kantara Trust Registry.

### 5.3 Global Sector/Platform-Specific PKI
#### 5.3.1 Adobe Approved Trust List (AATL)
- **Legal context**: Proprietary list of trusted roots for PDF signatures.
- **Supervision/audit**: Recognises ETSI EN 319 411-1/2, WebTrust, ISO 21188 audits; auditors must be accredited (ISO/IEC 17065 + ETSI EN 319 403 for ETSI; WebTrust licensed for WebTrust).
- **Best practice**: Compatible with ETSI EN 319 411-1/2.
- **Trust representation**: AATL list; also imports EU Trusted Lists.
- **Enablers**: Supports mapping between trusted list and store.

#### 5.3.2 CertiPath
- **Legal context**: Bridge CA for cross-organisational trust (US defence, federal agencies, commercial).
- **Supervision/audit**: Policy Management Authority (PMA) reviews CPS; third-party auditor attestation required.
- **Best practice**: CertiPath X.509 Certificate Policy (consistent with IETF RFC 3647).
- **Trust representation**: Bridge certificate.

#### 5.3.3 SAFE-BioPharma
- **Legal context**: Agreement-based for pharmaceutical/life sciences sector; aligned with US Federal standards.
- **Supervision/audit**: Cross-certification with SAFE-BioPharma Bridge CA; auditor must demonstrate competence (ETSI EN 319 403 accepted).
- **Best practice**: Aligned with ETSI EN 319 401, 319 411-1/2.
- **Trust representation**: Trust list derived from bridge.
- **Enablers**: Mapping possible to EU trusted list.
- **Barriers**: Operates through agreement, not regulation.

#### 5.3.4 Google Chrome
- **Legal context**: Uses underlying OS root store; maintains its own EV-qualified list.
- **Supervision/audit**: Relies on operating system root program policies.
- **Best practice**: Active in CA/B Forum.
- **Barriers**: Organizational identifiers (as in ETSI) not used; EV trust declining.

#### 5.3.5 Apple
- **Supervision/audit**: requires WebTrust or equivalent; final decision by Apple.
- **Best practice**: CA/B Forum Baseline/EV.
- **Trust representation**: Apple root store.

#### 5.3.6 Microsoft
- **Supervision/audit**: Accepts WebTrust, ETSI EN 319 403, or government approval.
- **Trust representation**: Microsoft root store.

#### 5.3.7 Mozilla
- Similar to Apple: root store, requires audits per CA/B Forum.

### 5.4 South America
#### 5.4.1 Argentina
- **Legal**: Law 25.506, Decree 182/2019. Distinguishes electronic vs. digital signature (digital equivalent to qualified). Application Authority is Modernization Government Secretariat. Mutual recognition agreements possible.
- **Supervision**: Accreditation valid 5 years; regular audits.
- **Best practice**: Uses ETSI TS 102 023 (TSA) and ETSI TS 101 861 (time-stamp profile).
- **Trust representation**: Public list of licenced certifiers.

#### 5.4.2 Bolivia
- **Legal**: Law 164, Supreme Decree 1793. Recognises foreign certificates if endorsed by national CA. Services include digital certificates, signature validation, time-stamping, registration.
- **Supervision**: Five-year accreditation by Telecommunications Authority; audits per ISO 21188.
- **Best practice**: ETSI TS 102 023 and TS 101 861 for time-stamping.
- **Trust representation**: No formal trust list.

#### 5.4.3 Brazil
- **Legal**: Provisional Measure 2.200-2 establishes ICP-Brazil (public key infrastructure). Root CA operated by National Institute of Information Technology. Management Committee can negotiate cross-certification.
- **Supervision**: Accreditation by root CA; pre-operational and annual audits.
- **Best practice**: References eIDAS, ETSI TS 101 861, ETSI TS 102 231 (trusted list format). TSP list in XML per ETSI TS 102 231.
- **Trust representation**: Trusted Service Provider List published by root CA.

#### 5.4.4 Chile
- **Legal**: Law 19799, Decree 181, Decree 24. Accreditation by Undersecretary of Economy. Recognised foreign certificates.
- **Supervision**: Annual inspection; detailed guidelines for different services.
- **Best practice**: ETSI TS 102 042, TS 102 023, TS 102 231, TR 102 206 (mobile). Adoption of ETSI TS 119 431-1/2 for remote signature.
- **Trust representation**: Public registry of accredited providers.

#### 5.4.5 Colombia
- **Legal**: Law 527, Decree 1747, Decree 333/2014. National Accreditation Body certifies certification entities. Recognised foreign certificates.
- **Supervision**: Audit per national accreditation criteria; ETSI TS 102 042 and TS 102 023 referenced.
- **Best practice**: ETSI standards used for certificate lifecycle and time-stamping.

#### 5.4.6 Paraguay
- **Legal**: Law 4017, Decree 7369. Application Authority (Ministry of Industry and Commerce) may sign mutual recognition agreements.
- **Supervision**: Accreditation process includes audit by Authority or third party; periodic audits.
- **Best practice**: ETSI TS 102 042 as assessment standard.
- **Trust representation**: Public Register of Certification Service Providers.

#### 5.4.7 Peru
- **Legal**: Law 27269, Supreme Decree 52/2008. INDECOPI is administrative authority; digital certificates recognised via IOFE framework. Foreign certificates can be recognised.
- **Supervision**: Accreditation valid 5 years; annual audits; specific audit scheme owned by INDECOPI.
- **Best practice**: Uses ETSI and CEN standards for eIDAS-aligned requirements; TSA service uses ETSI EN 319 421, EN 319 422.
- **Trust representation**: Official registry implemented as Trusted List (ETSI TS 102 231).
- **Enablers**: Time-stamping aligned with EU standards.

#### 5.4.8 Uruguay
- **Legal**: Law 18.600, Decrees 436/2011, 70/2018. Recognised foreign certificates via international agreements.
- **Supervision**: Accreditation by Electronic Certification Unit (ECU); biennial assessment audits per WebTrust.
- **Best practice**: Uses ETSI qcStatements (QcCompliance, QcSSCD).
- **Trust representation**: Accredited Certification Services Providers Registry.

### 5.5 Middle East & Africa
#### 5.5.1 Arab-African e-Certification Authorities Network (AAECA-Net)
- Interregional network aiming to harmonise legal frameworks; WG2 (technical) and WG3 (legal) active; no audit or trust representation yet.

#### 5.5.2 Israel
- Electronic Signature Law 5761-2001 similar to EU Directive 1999/93/EC. Only two CAs registered; audited against CWA 14167-1. Trust representation: list on Ministry of Justice website.

#### 5.5.3 Sultanate of Oman
- **Legal**: Royal Decree 69/2008; Electronic Transactions Law. National PKI operated by Information Technology Authority (ITA). Foreign certificates recognised by ministerial decision.
- **Supervision**: ITA licences authentication service providers for 5 years; periodic auditing.
- **Best practice**: Aligned with ETSI TS 101 456, TS 102 042, EN 319 142-1, TS 103 172 (PAdES), TS 102 023 (TSA), TS 119 441 (validation).
- **Trust representation**: Root-signing model.

#### 5.5.4 United Arab Emirates
- **Legal**: Federal Law No. 1/2006, Ministerial Resolution No. 1/2008. New law under revision fully aligned with eIDAS, covering 9 types of qualified trust services (including remote QSCD as a service).
- **Supervision**: TRA (Telecommunications Regulatory Authority) licenses CSPs for 5 years; new framework expected to adopt ISO/IEC 17065 + ETSI EN 319 403.
- **Best practice**: Future profiled ETSI standards as normative.
- **Trust representation**: Current simple list; future trusted list per ETSI TS 119 612, aiming for GCC-wide federation.

#### 5.5.5 Botswana
- **Legal**: Electronic Communications and Transactions Act 2014; BOCRA accredits CAs. Foreign certificates have same legal effect if substantially equivalent.
- **Supervision**: Auditors appointed by BOCRA; conformity audit at accreditation and renewal.
- **Best practice**: Accreditation requires compliance with ISO 21188; also recognises WebTrust, CA/B Forum, ETSI TS 101 456.
- **Trust representation**: Register of accredited CSPs published by BOCRA.

### 5.6 Asia/Pacific
#### 5.6.1 China
- **Legal**: Electronic Signature Law 2004; electronic verification service providers. Banking industry required to use PKI. Limited information on supervision and trust representation.

#### 5.6.2 Hong Kong
- **Legal**: Electronic Transactions Ordinance (Cap. 553). Recognised CA is Hongkong Post (operations outsourced). Digital signatures required for government transactions.
- **Supervision**: GCIO (Government Chief Information Officer) grants recognition; recognised CAs must comply with Code of Practice; assessments by approved persons.
- **Best practice**: CPS follows IETF RFC 3647; certificates based on X.509 + IETF RFC 5280; uses Certificate Transparency.
- **Trust representation**: Disclosure record on GCIO website; mutual recognition with Guangdong (trust list published). Root certificate included in major browsers and AATL.

#### 5.6.3 India
- **Legal**: Information Technology Act 2000. Controller of Certifying Authorities (CCA) operates Root CA. Licences CAs; identity vetting strict (physical documents required, video mandatory). Cloud signatures (eSign) widely used with FIPS 140-2+ HSMs.
- **Supervision**: Auditors empanelled by CCA; audit criteria similar to ETSI and WebTrust; detailed report not public.
- **Best practice**: CCA defines India PKI Certificate Policy; CAs must use standard CPS template. Equivalent to ETSI EN 319 411-1.
- **Trust representation**: Root CA trust chain; list of licensed CAs on CCA website.
- **Enablers**: Interoperability project suggested.

#### 5.6.4 Japan
- **Legal**: Act on Electronic Signatures and Certification Business (e-Signature Act); e-Document Law.
- **Supervision**: Competent ministries (MIC, MOJ, METI) accredit Specified Certification Businesses (SCB) based on investigation by Designated Investigative Organization (JIPDEC). JIPDEC also runs JCAN Trusted Service Registration. JADAC accredits Time Authorities.
- **Best practice**: References ETSI TS 102 023, TS 102 042, EN 319 411-1/2, CA/B Forum, WebTrust.
- **Trust representation**: JCAN Trusted Service Registration List; JADAC issues logo.
- **Enablers**: Study underway to map standards to EU; possible adoption of ETSI TS 119 612.

#### 5.6.5 Asia PKI Consortium
- Established 2001; members from 10+ Asian countries. Mostly regulation-driven based on UNCITRAL Model Law. Working groups on business, legal/policy, technology/standards. No unified trust representation.

### 5.7 North America
#### 5.7.1 Canada
- **Legal**: Secure Electronic Signatures Regulation (SOR/2005-30); Government of Canada PKI governed by Treasury Board. Pan-Canadian trust framework (identity management). Little adoption of electronic signatures.
- **Supervision**: Recognition process for CAs, but unclear if applied.
- **Trust representation**: Treasury Board website list (may not exist).

#### 5.7.2 Mexico
- **Legal**: Advanced Electronic Signature Law 2012; General Rules for Certification Service Providers. Foreign certificates accepted if equivalent reliability.
- **Supervision**: Economy Department accredits providers; audit process per Federal Administrative Procedure Law.
- **Best practice**: ETSI TS 102 042 (physical security, business continuity, key management).
- **Trust representation**: Economy Department maintains list of accredited/suspended providers.

#### 5.7.3 US Federal PKI (FPKI)
- **Legal**: Bridge CA framework; Federal Bridge CA (FBCA) acts as trust hub; Policy Management Authority (FPKIPA) oversees.
- **Supervision**: All TSPs must demonstrate compliance via regular independent audits; audit requirements defined in FPKI Audit Requirements.
- **Best practice**: FBCA Certificate Policy defines seven levels of assurance.
- **Trust representation**: Bridge certificate issued by FBCA.
- **Enablers**: Comparable policy requirements to ETSI (historical comparison TR 102 458).
- **Barriers**: Agreement-based, not regulatory; direct comparability with current qualified certificate requirements unclear.

### 5.8 Other Countries
#### 5.8.1 Russia
- **Legal**: Government PKI with state root CA; mandatory use of Russian cryptographic algorithms (restrictions on export).
- **Supervision**: No regular audit; accreditation documentary check; on-site inspection only in case of complaints.
- **Best practice**: CPS recommended to follow IETF RFC 3647. Signature verification infrastructure being developed within Eurasian Economic Union.
- **Trust representation**: Hierarchical PKI; Trust Status List (TSL) used; suspension of CA reflected only in TSL, not CRL.
- **Enablers**: Cross-recognition possible via common principles (e.g., UN/CEFACT).

#### 5.8.2 Switzerland
- **Legal**: Law on the Electronic Signature; based on eIDAS concepts.
- **Supervision**: Recognition body (CAB) accredited by Swiss Accreditation Service; similar role to EU CABs. No national supervisory body. Full re-assessment every 3 years with annual surveillances.
- **Best practice**: References ETSI EN 319 411-2, EN 319 411-1, EN 319 412, EN 319 421, EN 319 422, CEN EN 419 211. Plans to implement machine-readable Trusted List per ETSI TS 119 612.
- **Trust representation**: PDF list of recognised CSPs on Swiss Accreditation website.
- **Enablers**: Conclusion of bilateral agreement with EU would enable cross-recognition.

## 5 Analysis of Enablers and Barriers to Mutual Recognition (Clause 6)
### 6.1 General
Summarises key findings per pillar.

### 6.2 Legal Context
- **Enablers**: Existence of non-qualified concepts (advanced signature) as common basis; qualification concept allows comparison; eIDAS article 14 agreements potential.
- **Barriers**: Lack of article 14 agreements with non-EU nations; different sets of regulated trust services (e.g., legal person seals not recognised everywhere).

### 6.3 Supervision and Auditing
- **Approaches**: National schemes, ISO/IEC 17065 + ETSI EN 319 403, or ad hoc (WebTrust). Policy Management Authorities (PMA) in agreement-based schemes.
- **Enablers**: IAF MLA recognition of ISO/IEC 17065; ETSI EN 319 403 as framework; PMAs as equivalent to supervisory bodies.
- **Barriers**: No globally adopted accreditation scheme; lack of consistency in EU audit practices (ETSI standards recommended but not mandatory); WebTrust not formally recognised as equivalent to accredited CAB; no publicly available eIDAS certification schemes.

### 6.4 Best Practice
- **Approaches**: All based on X.509, IETF RFC 3647 for CPS. Historical ETSI TS 101 456/102 042; current ETSI EN 319 411-1/2 for eIDAS. International standards: ISO 21188, ISO/IEC 27099.
- **Enablers**: Use of common standards (ITU-T X.509, IETF RFC 3647); alignment with ETSI standards by non-EU countries; acceptance by CA/B Forum.
- **Barriers**: ETSI EN 319 411-2 targeted at EU; non-EU countries cannot easily claim equivalence without oversight by equivalent authority and use of QSCD.

### 6.5 Trust Representation
- **Models**: Root-signing, trust stores, trusted lists (ETSI TS 119 612), cross-certification via bridge.
- **Enablers**: Mappings between bridge and trusted list demonstrated (SAFE-BioPharma, Adobe); trusted lists facilitate independence from vendors.
- **Barriers**: Extended specifications needed for cross-domain mapping; ETSI EN 319 412-5 QcCompliance statement is EU-specific.

## 6 Conclusions and Recommendations (Clause 7)
### 7.1 General
a) Mutual recognition requires consideration of all four pillars.
b) Maintain liaison with Asia PKI Consortium, AAECA-Net, IMRT-WG.

### 7.2 Legal Context
c) Further harmonisation at international level (e.g., UNCITRAL) will assist.
d) EU should use 2020 eIDAS revision to facilitate international recognition.
e) EU should recognise both regulatory and agreement-based schemes.
f) Non-qualified advanced signatures can act as basis for recognition.
g) Promote advantages of qualified trust services (single legal framework).
h) Lack of article 14 agreements is a barrier.

### 7.3 Supervision and Auditing
i) Promote ETSI EN 319 403 globally through IAF.
j) Recognise WebTrust as comparable where formal accreditation unavailable.
k) Address inconsistency of best practices in EU audits.
l) Encourage PMAs to apply oversight functions comparable to EU supervisory bodies.
m) Formal recognition of ETSI EN 319 403 under eIDAS article 20.4 or Cybersecurity Act would clarify preferred basis.

### 7.4 Best Practice
n) Adoption of common standards (e.g., ETSI) assists recognition.
o) Non-EU countries should adopt latest ETSI eIDAS standards.
p) Extend ETSI standards to provide interoperable equivalent of qualified certificate policies for non-EU adoption (including oversight and QSCD).
q) Influence ISO/IEC CD 27099 to align with ETSI.
r) Consider ISO/IEC 27701 for privacy alignment.

### 7.5 Trust Representation
s) Encourage non-EU PKI schemes to map trust representation to EU trusted list format.
t) Update ETSI EN 319 412-5 QcCompliance to cover non-EU countries.

## Conclusions/Recommendations Summary
| ID | Recommendation | Source Clause | Type |
|----|----------------|---------------|------|
| R01 | Maintain liaison with Asia PKI, AAECA-Net, IMRT-WG | 7.2(b) | should |
| R02 | Further harmonisation at international level (UNCITRAL) | 7.3(c) | should |
| R03 | Use 2020 eIDAS revision to facilitate mutual recognition | 7.3(d) | should |
| R04 | Recognise both regulatory and agreement-based schemes | 7.3(e) | should |
| R05 | Use non-qualified advanced signatures as basis for recognition | 7.3(f) | could |
| R06 | Promote advantages of qualified trust services | 7.3(g) | should |
| R07 | Address lack of article 14 agreements | 7.3(h) | should |
| R08 | Promote ETSI EN 319 403 globally through IAF | 7.4(i) | should |
| R09 | Recognise WebTrust as comparable where formal accreditation unavailable | 7.4(j) | may |
| R10 | Improve consistency of best practices in EU audit schemes | 7.4(k) | should |
| R11 | Encourage PMAs to apply oversight comparable to EU supervisory bodies | 7.4(l) | should |
| R12 | Formally recognise ETSI EN 319 403 under eIDAS article 20.4 or Cybersecurity Act | 7.4(m) | should |
| R13 | Adopt common standards (ETSI) for recognition | 7.5(n) | should |
| R14 | Non-EU countries should adopt latest ETSI eIDAS standards | 7.5(o) | should |
| R15 | Extend ETSI standards for interoperable qualified certificate policies | 7.5(p) | should |
| R16 | Influence ISO/IEC CD 27099 to align with ETSI | 7.5(q) | should |
| R17 | Consider ISO/IEC 27701 for privacy alignment | 7.5(r) | should |
| R18 | Encourage mapping of trust representation to EU trusted list format | 7.6(s) | should |
| R19 | Update ETSI EN 319 412-5 QcCompliance for non-EU | 7.6(t) | should |

## Informative Annexes (Condensed)
- **Annex A – Study Questionnaire**: Provides the questionnaire used to collect information from PKI schemes, covering trust management, audit, certificate policy, and views on cross-recognition.
- **Annex B – Example of Mutual Recognition Process Flow**: Outlines a high-level 7-step process for comparing trust models and executing mutual recognition agreements (MRA), including scope definition, comparison, preparation, signing, execution, maintenance, and termination.
- **Annex C – The Model of eIDAS Used as Reference for Comparison**: Detailed description of the eIDAS regulatory framework: nine types of qualified trust services (e.g., qualified certificates for signatures, seals, website authentication, preservation, validation, time-stamps, registered delivery); supervisory scheme with pre-authorisation, 24-month audit cycle by accredited CABs; technical standards (ETSI EN 319 series); trust representation via EU Trust Mark and national trusted lists (ETSI TS 119 612), with LOTL linking Member States’ lists.
- **Annex D – Reports of Workshops**: Summaries of four regional workshops (Dubai, Tokyo, Mexico City, New York) highlighting local perspectives, common themes (strong interest in mutual recognition, need for technical dialogue, awareness of eIDAS, desire for interoperable trust frameworks).