# ETSI TS 119 612: Electronic Signatures and Trust Infrastructures (ESI); Trusted Lists

**Source**: ETSI | **Version**: V2.4.1 | **Date**: 2025-08 | **Type**: Normative Technical Specification
**Original**: [ETSI TS 119 612 V2.4.1](https://www.etsi.org/deliver/etsi_ts/119600_119699/119612/02.04.01_60/ts_119612v020401p.pdf) (PDF)

## 1 Scope (Summary)

This Technical Specification specifies a format and mechanisms for establishing, locating, accessing and authenticating Trusted Lists (TLs) that provide trust service status information. It defines the format and semantics of a TL as well as mechanisms for accessing TLs, and applies to EU Member State trusted lists for expressing compliance with Regulation (EU) No 910/2014 [i.10] and applicable secondary legislation. Non-EU countries or international organizations may also issue TLs in accordance with this document to facilitate mutual recognition of digital signatures. The document also defines requirements for relying parties to use TLs and the status information contained therein.

## 2 Normative References

- [1] Recommendation ITU-T X.509
- [2] ETSI TS 119 312
- [3] ETSI EN 319 132-1 (V1.3.1)
- [4] W3C® Recommendation 11 April 2013: "XML Signature Syntax and Processing. Version 1.1"
- [5] ISO/IEC 10646:2020
- [6] IETF RFC 2368
- [7] IETF RFC 2616
- [8] IETF RFC 3986
- [9] IETF RFC 5322
- [10] FIPS Publication 180-4 (2015)
- [11] IETF RFC 5646
- [12] IETF RFC 5280
- [13] ISO/IEC 6429:1992
- [14] ISO/IEC 2022:1994
- [15] ISO 3166-1:2020
- [16] ISO 8601:2019 (parts 1 and 2)
- [17] IETF RFC 3966

## 3 Definitions and Abbreviations (Condensed)

**Key Terms** (exact definitions preserved per clause 3.1):

- **approval**: Assertion that a trust service has been positively endorsed or assessed for compliance (active approval) or has received no explicit restriction (passive approval).
- **approval scheme**: Any organized process of supervision, monitoring, or assessment to ensure adherence to specific criteria.
- **certification authority**: Authority trusted to create and assign certificates (see ISO/IEC 9594-8 [i.12] and ITU‑T X.509 [1]).
- **conformity assessment**: Process demonstrating whether specified requirements are fulfilled (from Regulation (EC) No 765/2008 [i.4] and ISO/IEC 17000 [i.8]).
- **digital signature**: Data appended to or cryptographic transformation of a data unit allowing proof of source and integrity.
- **qualified certificate (EU)**: Qualified certificate as specified in Regulation (EU) No 910/2014 [i.10].
- **qualified electronic signature/seal/...**: As defined in Regulation (EU) No 910/2014 [i.10].
- **scheme operator**: Body responsible for operation/management of an assessment scheme.
- **trust service**: Electronic service which enhances trust and confidence in electronic transactions.
- **trust service provider (TSP)**: Entity providing one or more electronic trust services.
- **trusted list (TL)**: List that provides information about the status and status history of trust services from TSPs regarding compliance with applicable requirements.
- **XML Advanced Electronic Signature (XAdES)**: As defined in ETSI EN 319 132-1 [3].

**Abbreviations** (common ones used in normative sections):
- CA: Certification Authority
- CRL: Certificate Revocation List
- DN: Distinguished Name
- EU: European Union
- LOTL: List Of Trusted Lists
- OCSP: Online Certificate Status Protocol
- QC: Qualified Certificate
- QSCD: Qualified Signature/Seal Creation Device
- SSCD: Secure Signature Creation Device
- TLS: Trusted List (used interchangably with TL)
- TLSO: Trusted List Scheme Operator
- TSP: Trust Service Provider
- URI: Uniform Resource Identifier
- XAdES: XML Advanced Electronic Signature

## 4 Overall Structure of Trusted Lists

**TLSOs shall comply with:**
- Format and semantics of a TL (clause 5);
- Mechanisms for locating, accessing, and authenticating TLs (clause 6).

**Logical components** (mandatory occurrence: 1., 2., 6.; others may be replicated):
1. **TSL Tag** (clause 5.2.1)
2. **Scheme Information** (clause 5.3) – includes version, sequence number, type, operator name/address, scheme name/territory, status determination approach, etc.
3. **TSP Information** (clause 5.4) – unambiguous identification of each TSP recognized under the scheme.
4. **Service Information** (clause 5.5) – details of each listed trust service (type, name, digital identity, current status, history).
5. **Service History** (clause 5.5.10) – status history for each service.
6. **Digital Signature** (clause 5.7) – for authentication.

The number of TSPs, services per TSP, and history sections per service is unbounded.

## 5 Trusted List Format and Content

### 5.1 General Principles

#### 5.1.1 Trusted List Format
- A TL **shall** be issued in XML format as specified in annexes B and C.
- If other formats are provided, they **shall** contain exactly the same information as the XML format.

#### 5.1.2 Use of Uniform Resource Identifiers
- Many fields use URIs; common names are linked to annex D.
- Implementers **shall** use general URI syntax per IETF RFC 3986 [8].

#### 5.1.3 Date-time Indication
- All date-time fields **shall** comply with:
  1) Formatted per ISO 8601 [16];
  2) Expressed as UTC: year (4 digits), month, day, hour, minute, second (no decimal fraction), and "Z" designator.

#### 5.1.4 Language Support
- TLs **shall** be issued supporting at least UK English (language code 'en' per IETF RFC 5646 [11] and annex E).
- Multilingual character strings and pointers defined with language tag (lowercase) and text/URI.
- If native terms cannot be represented in Latin alphabet, one issue in native language plus one transliteration to Latin alphabet **shall** be used.

#### 5.1.5 Country Code Fields
- **Shall** be in capital letters per either:
  a) ISO 3166-1 [15] Alpha 2 with exceptions: United Kingdom = "UK", Greece = "EL", EU = "EU";
  b) Common extensions (e.g., AP, ASIA);
  c) Recognized multi-state grouping identifiers not conflicting with a) or b) (e.g., GCC, ASEAN).

### 5.2 Trusted List Tag

#### 5.2.1 TSL Tag
- **Presence**: **shall** be present.
- **Description**: Attribute of `<tsl:TrustServiceStatusList>` root element.
- **Format**: Character string representing the TSLTag URI.
- **Value**: Unique value enabling WWW search; only characters required to fully represent the URI **shall** be present.

### 5.3 Scheme Information

#### 5.3.1 TSL Version Identifier
- **Presence**: **shall** be present.
- **Format**: Integer.
- **Value**: **Shall** be "6".

#### 5.3.2 TSL Sequence Number
- **Presence**: **shall** be present.
- **Format**: Integer.
- **Value**: First release = 1; **shall** be incremented at each subsequent release and **shall not** be recycled to "1" or lower.

#### 5.3.3 TSL Type
- **Presence**: **shall** be present.
- **Format**: URI.
- **Value (EU MS)**: `http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric` (clause D.5).
- **Value (non-EU)**: `http://uri.etsi.org/TrstSvc/TrustedList/TSLType/CClist` where "CC" identifies the community (clause D.6) or a registered URI.
- For lists of pointers (LOTL): `EUlistofthelists` or `CClistofthelists`.

#### 5.3.4 Scheme Operator Name
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual character strings (clause 5.1.4).
- **Value**: The formal name of the legal entity or mandated entity in charge; used in formal legal registration.

#### 5.3.5 Scheme Operator Address
##### 5.3.5.0 General
- **Presence**: **shall** be present.
- **Format**: Multi-part: postal address (5.3.5.1) and electronic address (5.3.5.2).

##### 5.3.5.1 Scheme Operator Postal Address
- **Presence**: **shall** be present.
- **Format**: Sequence(s) of multilingual character strings giving: street address (sub-components delimited by ";"), locality, optionally state/province, postal code, and country name as two-character code (clause 5.1.5(a)).
- **Value**: Address where scheme operator provides help line via conventional mail.

##### 5.3.5.2 Scheme Operator Electronic Address
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual character strings giving:
  - Mandatorily: e-mail URI per IETF RFC 2368 [6];
  - Mandatorily: web-site URI per IETF RFC 3986 [8];
  - Optionally: telephone URI per IETF RFC 3966 [17].
- **Value**: Addresses for help line service addressing TL-related matters.

#### 5.3.6 Scheme Name
- **Presence**: **shall** be present.
- **Format**: Multilingual character strings; English version structured as `CC:EN_name_value`; national language versions as `CC:name_value`.
- **Value**: The name used in formal references, unique to the scheme.

#### 5.3.7 Scheme Information URI
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual pointers (clause 5.1.4).
- **Value**: URI(s) providing information about the scheme (scope, approval process, criteria, responsibilities, liabilities, etc.).

#### 5.3.8 Status Determination Approach
- **Presence**: **shall** be present.
- **Format**: URI.
- **Value (EU MS)**: `http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate` (clause D.5).
- **Value (non-EU)**: `http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/CCdetermination` (clause D.6) or registered URI.

#### 5.3.9 Scheme Type/Community/Rules
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual pointers.
- **Value**: URI(s) identifying policy/rules against which services are approved; if participating in a wider scheme, common URI used (EU: `http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon`). Also a country-specific URI `http://uri.etsi.org/TrstSvc/TrustedList/schemerules/CC`.

#### 5.3.10 Scheme Territory
- **Presence**: **shall** be present.
- **Format**: Character string per clause 5.1.5.
- **Value**: Country or territory where the scheme is established.

#### 5.3.11 TSL Policy/Legal Notice
- **Presence**: **shall** be present.
- **Format**: Either sequence of multilingual pointers or sequence of multilingual character strings.
- **Value**: Describes policy or legal notices for the TL.

#### 5.3.12 Historical Information Period
- **Presence**: **shall** be present.
- **Format**: Integer.
- **Value**: **Shall** be '65535', signifying historical information **shall never** be removed.

#### 5.3.13 Pointers to Other TSLs
- **Presence**: **shall** be present for EU MS; optional for non-EU.
- **Format**: Sequence of tuples, each giving:
  a) URI of machine-processable format of another TL;
  b) one or more digital identities of the issuer (clause 5.5.3);
  c) additional TL Qualifiers (TSLType, Scheme operator name, Scheme type/rules, Scheme territory, Mime type).
- **Value (EU MS)**: Includes pointer to European LOTL. More than one digital identity may be used.

#### 5.3.14 List Issue Date and Time
- **Presence**: **shall** be present.
- **Format**: Date-time value (clause 5.1.3).
- **Value**: UTC at which the TL was issued.

#### 5.3.15 Next Update
- **Presence**: **shall** be present or null for a closed TL.
- **Format**: Date-time value or null.
- **Value**: UTC by which an update **shall** be issued. The difference between 'Next update' and 'List issue date and time' **shall not** exceed six (6) months. In the event of scheme cessation, final version with all services' status "expired" and this field null.

#### 5.3.16 Distribution Points
- **Presence**: Optional.
- **Format**: Non-empty sequence of URIs.
- **Value**: Dereferencing the URI delivers the latest update. If multiple points, they **shall** provide identical copies.

#### 5.3.17 Scheme Extensions
- **Presence**: **shall not** be present for EU MS; optional for non-EU.
- **Format**: Sequence of extensions with criticality indication.
- **Value**: Each extension defined by its source specification. Criticality semantics as in X.509 certificates [1]; TL **shall** reject if unrecognized critical extension.

#### 5.3.18 Trust Service Provider List
- **Presence**: If no TSP is/was approved, **shall not** be present; otherwise **shall** be present.
- **Format**: Sequence of Trust Service Provider elements, each with TSP Information (clause 5.4) and TSP Services (list of Service Information elements, each with optional Service History).
- **Value**: Contains identifying information for each TSP and details on status and status history of their services.

### 5.4 TSP Information

#### 5.4.1 TSP Name
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual character strings.
- **Value**: The name used in formal legal registrations and official records.

#### 5.4.2 TSP Trade Name
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual character strings.
- **Value**: **Shall** include an official registration identifier (for legal person: 3-character type (VAT/NTR), 2-character ISO country code, hyphen, identifier; for natural person: PAS/IDC/PNO/TIN, country code, hyphen, identifier). May additionally include alternative name under which TSP operates.

#### 5.4.3 TSP Address
##### 5.4.3.0 General
- **Presence**: **shall** be present.
- **Format**: Multi-part: postal address (5.4.3.1) and electronic address (5.4.3.2).
- **Value**: In case of termination, replaced by scheme operator's address for enquiries.

##### 5.4.3.1 TSP Postal Address
- **Presence**: **shall** be present.
- **Format**: As clause 5.3.5.1.
- **Value**: Address at which TSP provides customer care/help line.

##### 5.4.3.2 TSP Electronic Address
- **Presence**: **shall** be present.
- **Format**: As clause 5.3.5.2.
- **Value**: E-mail, web-site URI, optional telephone number, all for customer care.

#### 5.4.4 TSP Information URI
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual pointers.
- **Value**: URI(s) providing TSP-specific information (e.g., CPS, CP, GTC, etc.). In case of termination, replaced by scheme operator's URI for terminated services.

#### 5.4.5 TSP Information Extensions
- **Presence**: Optional.
- **Format**: Sequence of extensions (format left open).
- **Value**: For EU MS, when used, **shall not** be made critical.

#### 5.4.6 TSP Services (List of Services)
- **Presence**: **shall** be present.
- **Format**: Sequence of TSP Service elements (Service Information + optional Service History).
- **Value**: At least one service listed; historical information retained even if service is withdrawn.

### 5.5 Service Information

#### 5.5.1 Service Type Identifier
- **Presence**: **shall** be present.
- **Format**: URI.
- **Value**: One of:
  - URIs from clause 5.5.1.1 (EU qualified trust services): e.g., `http://uri.etsi.org/TrstSvc/Svctype/CA/QC`
  - URIs from clause 5.5.1.2 (EU non-qualified): e.g., `http://uri.etsi.org/TrstSvc/Svctype/CA/PKC`
  - URIs from clause 5.5.1.3 (nationally defined): e.g., `http://uri.etsi.org/TrstSvc/Svctype/RA`
  - Other registered URIs.

#### 5.5.2 Service Name
- **Presence**: **shall** be present.
- **Format**: Sequence of multilingual character strings.
- **Value**: Name under which TSP provides the service.

#### 5.5.3 Service Digital Identity
- **Presence**: **shall** be present.
- **Format**: When not using PKI (e.g., type ending in `/nothavingPKIid`): a URI. When using PKI: tuple with one or more X509Certificate (Base64), optionally X509SubjectName, KeyValue, X509SKI.
- **Value**: Unique identifier of the service (public key used to verify authenticity). At least one X509Certificate **shall** be used. When multiple certificates represent the same public key, all shall have identical subject names. The same public key shall not appear more than once for the same service type.

#### 5.5.4 Service Current Status
- **Presence**: **shall** be present.
- **Format**: URI.
- **Value (EU MS for qualified services)**: `granted` or `withdrawn` (clause D.5). For non-qualified: `recognisedatnationallevel` or `deprecatedatnationallevel`. Status flow as per Figure 2. Initial status for new services: `granted` or `recognisedatnationallevel`. For non-EU: as specified by TLSO.

#### 5.5.5 Current Status Starting Date and Time
- **Presence**: **shall** be present.
- **Format**: Date-time value.
- **Value**: UTC when current status became effective. TLSO **shall** ensure consistency between list issue date, signing time, and status change time; status change date/time shall not be prior to list issuance.

#### 5.5.6 Scheme Service Definition URI
- **Presence**: Optional.
- **Format**: Sequence of multilingual pointers.
- **Value**: URI(s) to service-specific information from TL scheme operator (e.g., fallback TSP ID, additional qualification info).

#### 5.5.7 Service Supply Points
- **Presence**: Optional.
- **Format**: Non-empty sequence of URIs, each optionally further specified with a URI.
- **Value**: Where/how the service can be accessed (e.g., CRL distribution point, OCSP responder).

#### 5.5.8 TSP Service Definition URI
- **Presence**: For type `NationalRootCA-QC` this field **shall** be present; otherwise optional.
- **Format**: Sequence of multilingual pointers.
- **Value**: URI(s) to service-specific info from the TSP (including details on establishment, management rules, national legislation for NationalRootCA-QC).

#### 5.5.9 Service Information Extensions
##### 5.5.9.0 General
- **Presence**: Optional.
- **Format**: Sequence of service information extensions (pre-defined in clauses 5.5.9.1–5.5.9.4).
- **Value**: ExpiredCertsRevocationInfo, Qualifications (with CriteriaList and Qualifiers), TakenOverBy, additionalServiceInformation.

##### 5.5.9.1 expiredCertsRevocationInfo Extension
- **Presence**: Optional; only for specific service types (CA/QC, CA/PKC, etc.). Not critical.
- **Format**: Date-time value.
- **Value**: Indicates that CRLs/OCSP responses issued by the service include revocation info for certificates expired after that date/time. Overridden by extensions in CRLs/OCSP responses if present.

##### 5.5.9.2 Qualifications Extension
- **Presence**: **Shall** be present when qualified certificates do not allow machine-processable identification of qualifiers (qualified status, SSCD/QSCD, legal person, signature/seal/web auth). If critical, validation shall discard certificate if not understood.
- **Format**: Sequence of Qualification Elements, each with CriteriaList (assertions) and Qualifiers (URIs).
- **Qualifiers** include: QCWithSSCD, QCNoSSCD, QCSSCDStatusAsInCert, QCWithQSCD, QCNoQSCD, QCQSCDStatusAsInCert, QCQSCDManagedOnBehalf, QCForLegalPerson, QCForESig, QCForESeal, QCForWSA, NotQualified, QCStatement.

##### 5.5.9.3 TakenOverBy Extension
- **Presence**: **Shall** be present when a service is taken over by another TSP.
- **Format**: Contains URI and attributes: TSP name, Scheme operator name, Scheme territory, optional additional info.
- **Value**: Identifies the taking-over TSP; not meant to enforce action on signature validation. If critical, validation shall discard if not understood.

##### 5.5.9.4 additionalServiceInformation Extension
- **Presence**: Optional.
- **Format**: Sequence of tuples with URI (identifying additional info) and optional serviceInformation classification and additional info.
- **URI examples**: ForSignatures (`http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/ForeSignatures`), ForSeals, ForWebSiteAuthentication, RootCA-QC, or nationally defined.

#### 5.5.10 Service History
- **Presence**: **Shall** be present only when historical information is applicable (i.e., service has prior statuses).
- **Format**: Sequence of Service History Instance elements (clause 5.6).
- **Value**: Previous status entries in descending order of status change date/time.

### 5.6 Service History Instance

#### 5.6.1 Service Type Identifier
- Same format/value as clause 5.5.1.

#### 5.6.2 Service Name
- Same format/value as clause 5.5.2.

#### 5.6.3 Service Digital Identity
- Same format/value as clause 5.5.3, but **shall** include at least the X509SKI element and exclude any certificate.

#### 5.6.4 Service Previous Status
- Same format/value as clause 5.5.4.

#### 5.6.5 Previous Status Starting Date and Time
- Same format/value as clause 5.5.5.

#### 5.6.6 Service Information Extensions
- Optional; same format/value as clause 5.5.9.

### 5.7 Digital Signature

#### 5.7.1 Digitally Signed Trusted List
- The TL **shall** be digitally signed by the Scheme Operator (clause 5.3.4).
- **Signature format**: XAdES-B-B per ETSI EN 319 132-1 [3] with requirements in annex B.
- **Algorithm**: Shall conform to security requirements for minimum 3 years usable key per ETSI TS 119 312 [2] (tables 4, 6, 7).
- **Certificate inclusion**: TLSO certificate **shall** be protected within `<ds:KeyInfo>`; no other certificates forming a chain.
- **Certificate restrictions** (normative):
  - Issuer: self-signed or a TSP trust service listed in the TL or same community.
  - Subject DN: Country code and Organization shall match Scheme Territory and Scheme operator name (UK English preferred or local transliterated).
  - KeyUsage: `digitalSignature` and/or `nonRepudiation` only.
  - ExtendedKeyUsage: should contain `id-tsl-kp-tslSigning`.
  - SubjectKeyIdentifier: present, using first 2 methods of IETF RFC 5280 [12] clause 4.2.1.2.
  - BasicConstraints: `CA=false`.

#### 5.7.2 Digital Signature Algorithm Identifier
- **Presence**: **shall** be present.
- **Description**: Specifies the cryptographic algorithm used.
- **Format**: Character or bit string.
- **Value**: **Shall** be included in the signature calculation.

#### 5.7.3 Digital Signature Value
- **Presence**: **shall** be present.
- **Value**: All fields of the TL except the signature value itself **shall** be included in the calculation.

## 6 Operations

### 6.1 TL Publication
- TLSOs **shall** make TLs available via HTTP (IETF RFC 2616 [7]); optionally LDAP or FTP.
- HTTP URI **shall** be stable, permanent, without special characters, redirects, cookies, or extra headers; absolute path shall end with `.xml` or `.xtsl`.
- Cache control should be set to a maximum of 4 hours.
- TLSOs **shall** publish a SHA-256 digest of the TL at a URI derived by replacing `.xml`/`.xtsl` with `.sha2`. This digest may be used to detect updates but **shall not** be used for authentication.
- Applications should check regularly for updates.

### 6.2 Transport Protocols
#### 6.2.1 HTTP-Transport
##### 6.2.1.1 HTTP-Media Type
- TL payloads **shall** be sent with media type `application/vnd.etsi.tsl+xml`.
- Client should include `Accept: application/vnd.etsi.tsl+xml`.

#### 6.2.2 MIME Registrations
- MIME type: `application/vnd.etsi.tsl+xml`
- File extensions: xml or xtsl.

### 6.3 TL Distribution Points in Trust Service Tokens
- TSPs may include TL location extensions in tokens (certificates, CRLs, etc.). If criticality allowed, extension should not be marked critical. Distribution point should remain accessible until all referencing tokens have expired. TSP **shall** guarantee the distribution point resolves to the latest applicable TL or to a scheme including a pointer to it.

### 6.4 TL Availability
- TLSOs **shall** make TLs available 24/7 with minimum 99.9% availability over one year.

### 6.5 TLSO Practices
- TLSO **shall** define, maintain, and implement appropriate measures, practices, and policies (including change management and security procedures) to ensure information is timely, accurate, complete, and authentic.

## Normative Annexes (Key Requirements)

### Annex B (normative): Implementation in XML
- TL **shall** comply with XML schemas in annex C (namespaces: `http://uri.etsi.org/02231/v2#`, `http://uri.etsi.org/TrstSvc/SvcInfoExt/eSigDir-1999-93-EC-TrustedList/#`, `http://uri.etsi.org/02231/v2/additionaltypes#`).
- Applications **shall** use UTF-8 encoding.
- Processing of critical attribute as per IETF RFC 5280 [12]; TL **shall** be rejected if unrecognized critical extension.
- Signature element: enveloped, with specific ds:Transforms (enveloped signature then exclusive canonicalization), ds:CanonicalizationMethod `http://www.w3.org/2001/10/xml-exc-c14n#`.
- `xades:SigningCertificateV2` **shall** be used as signed property.
- Algorithms: those supported by XML-Signature [4], plus ECDSA per [1] and SHA-2 per [10].

### Annex C (normative): XML Schema
- Provided in ZIP file `ts_119612v020401p0.zip`; also at https://forge.etsi.org/rep/esi/x19_612_trusted_lists.
- In case of conflict, the text of the present document prevails.

### Annex D (normative): Registered Uniform Resource Identifiers (Condensed)
- Lists all URIs used in the document, organized by purpose: TSLTag, namespaces, scheme URIs, common trusted lists URIs (schemerules/CC, RootCA-QC), EU-specific (TSLType, StatusDetn, schemerules, qualifications qualifiers, additionalServiceInformation, service statuses), non-EU-specific (CClist, CClistofthelists, CCdetermination).
- **Key URIs**:
  - `http://uri.etsi.org/TrstSvc/TrustedList/TSLType/EUgeneric` – EU generic TL
  - `http://uri.etsi.org/TrstSvc/TrustedList/StatusDetn/EUappropriate` – EU status determination
  - `http://uri.etsi.org/TrstSvc/TrustedList/schemerules/EUcommon` – common EU rules
  - `http://uri.etsi.org/TrstSvc/TrustedList/SvcInfoExt/QCWithSSCD` etc. – qualifications
  - `http://uri.etsi.org/TrstSvc/TrustedList/Svcstatus/granted` etc. – service statuses

### Annex E (normative): Multilingual Support
- Language codes in lower case, country codes upper case.
- Table E.1 specifies language and country codes for EU MS and transliterations.
- Multilingual character strings **shall** comply with ISO/IEC 10646 [5] UTF-8, no control characters, no private-use or tag characters.
- Multilingual pointers (URI) may contain mark-up; must follow W3C Technical Report #20 [i.7] recommendations.

### Annex G (normative): Management and Policy Considerations
- **G.1**: Changes to scheme administrative information – TL **shall** be re-issued.
- **G.2**: Trust-service identification – digital identity field is the only option for secure identification.
- **G.3**: Change of trust service status – TL **shall** be re-issued with previous status moved to history.
- **G.4**: Change in service digital identity – new public key → new service entry; new certificate for same key → may be added to existing set.
- **G.5**: Amendment response times – changes **shall** be provided in ≤24 hours; ideally status changes implemented in <4 working hours.
- **G.6**: On-going verification of authenticity – scheme operator should make frequent verification; regular re-issuing even without changes.
- **G.7**: User reference to TL – operators should offer notifications for new TLs.
- **G.8**: TL size – implementers should limit embedded text and use URIs to control size.

### Annex J (normative): Migration of EU MS Trusted Lists for Regulation (EU) No 910/2014
- **Migration date**: 01 July 2016.
- For each service type, status values are migrated as per mapping tables (e.g., `undersupervision` → `granted` for qualified services; `supervisionceased` → `withdrawn`). Old statuses moved to history.
- Specific migration of qualifications qualifiers (SSCD → QSCD, etc.) and addition of `QCForESig` etc.
- For services of type TSA/QTST, EDS/Q, etc., initial migration sets status to `withdrawn` unless already listed.
- By 1 July 2017, if no conformity assessment report is submitted, qualified status may change to `withdrawn`.

## Informative Annexes (Condensed)

### Annex A (informative): Authenticating and Trusting Trusted Lists
- **Purpose**: Describes how to authenticate TLs using compiled lists of pointers (e.g., LOTL). Relying parties can validate TL signature via certificates published in LOTL, which is signed and trusted via OJEU digests. Procedures for key compromise and continuity outlined.

### Annex F (informative): TL Manual/Auto Field Usage
- **Purpose**: Table F.1 indicates which fields should be human-readable and which are essential for machine processing. All fields are accessible via automated processes.

### Annex H (informative): Locating a TL
- **Purpose**: The European Commission publishes a central LOTL with links to all Member States' TLs. For PKI-based services, the country code in the trust service token provides a hint for TL location.

### Annex I (informative): Usage of Trusted Lists
- **Purpose**: Describes an example model for using TLs in signature validation: TLs provide trust anchors for certificate path validation. Policy elements can specify acceptable service types and statuses.

### Annex J (normative): Migration (already covered in normative section) – note: Annex J is normative, not informative. Corrected.

## Requirements Summary (Representative)

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | TL **shall** be issued in XML format as per annex B and C. | shall | 5.1.1 |
| R2 | Date-time fields **shall** be ISO 8601 UTC with "Z". | shall | 5.1.3 |
| R3 | TL **shall** support at least UK English. | shall | 5.1.4 |
| R4 | TSL version identifier **shall** be "6". | shall | 5.3.1 |
| R5 | TSL sequence number **shall** start at 1 and increment at each release. | shall | 5.3.2 |
| R6 | Type URI for EU MS **shall** be `EUgeneric`. | shall | 5.3.3 |
| R7 | Historical information period **shall** be 65535. | shall | 5.3.12 |
| R8 | Next update – List issue date difference **shall not** exceed 6 months. | shall | 5.3.15 |
| R9 | TL **shall** be digitally signed using XAdES-B-B. | shall | 5.7.1 |
| R10 | TL availability **shall** be min 99.9% over one year. | shall | 6.4 |
| R11 | Changes to TL information **shall** be provided ≤24 hours. | shall | G.5 |