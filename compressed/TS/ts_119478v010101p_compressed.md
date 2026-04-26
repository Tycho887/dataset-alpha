# ETSI TS 119 478 V1.1.1: Electronic Signatures and Trust Infrastructures (ESI); Specification of interfaces related to Authentic Sources

**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2026-01 | **Type**: Normative Technical Specification  
**Original**: DTS/ESI-0019478

## Scope (Summary)

This document specifies the technical framework (architecture, components, interfaces, protocols, data structures) for accessing authentic sources to enable qualified trust service providers (QTSPs) to verify attributes listed in Annex VI of the amended eIDAS-Regulation (EU) No 910/2014 at the user's request, as required by Article 45e. It also specifies an optional interface to retrieve additional attributes. Two interface variants are defined: an HTTP/OAuth‑based API and an ISO 15000‑based interface. A **Discover Interface** (I1) reuses the Once‑Only Technical System (OOTS) common services for attribute and data service discovery. Policy and security requirements for resource service endpoints are out of scope.

## Normative References

The following documents are necessary for the application of the present document:

- [1] IETF RFC 1738: "Uniform Resource Locators (URL)"
- [2] IETF RFC 3986: "Uniform Resource Identifier (URI): Generic Syntax"
- [3] IETF RFC 4648: "The Base16, Base32, and Base64 Data Encodings"
- [4] IETF RFC 5141: "A Uniform Resource Name (URN) Namespace for the International Organization for Standardization (ISO)"
- [5] IETF RFC 5280: "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile"
- [6] IETF RFC 6749: "The OAuth 2.0 Authorization Framework"
- [7] IETF RFC 6819: "OAuth 2.0 Threat Model and Security Considerations"
- [8] IETF RFC 6838: "Media Type Specifications and Registration Procedures"
- [9] IETF RFC 7519: "JSON Web Token (JWT)"
- [10] IETF RFC 7591: "OAuth 2.0 Dynamic Client Registration Protocol"
- [11] IETF RFC 7636: "Proof Key for Code Exchange by OAuth Public Clients"
- [12] IETF RFC 8259: "The JavaScript Object Notation (JSON) Data Interchange Format"
- [13] IETF RFC 8705: "OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens"
- [14] IETF RFC 9068: "JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens"
- [15] IETF RFC 9110: "HTTP Semantics"
- [16] IETF RFC 9449: "OAuth 2.0 Demonstrating Proof of Possession (DPoP)"
- [17] IETF RFC 9535: "JSONPath: Query Expressions for JSON"
- [18] IETF RFC 9562: "Universally Unique IDentifiers (UUIDs)"
- [19] IETF RFC 9700: "Best Current Practice for OAuth 2.0 Security"
- [20] ISO 639:2023: "Code for individual languages and language groups"
- [21] ISO 3166-1:2020: "Codes for the representation of names of countries and their subdivisions — Part 1: Country code"
- [22] ISO 8601-1:2019: "Date and time — Representations for information interchange — Part 1: Basic rules"
- [23] ISO 15000-2:2021: "Electronic business eXtensible Markup Language (ebXML) — Part 2: Applicability Statement (AS) profile of ebXML messaging service"
- [24] ISO 15000-3:2023: "Electronic business eXtensible Markup Language (ebXML) — Part 3: Registry and repository"
- [25] ISO/IEC 27001:2022: "Information security, cybersecurity and privacy protection — Information security management systems — Requirements"
- [26] OASIS: "ebXML Messaging Protocol Binding for RegRep Version 1.0", Committee Specification 01, 09 March 2021
- [27] OpenAPI Initiative: "OpenAPI Specification"
- [28] OpenID Foundation: "FAPI 2.0 Security Profile"
- [29] OpenID Foundation: "OpenID Connect Core 1.0 incorporating errata set 2"
- [30] W3C® Recommendation 21 March 2017: "W3C XML Path Language (XPath) 3.1"

## Definitions and Abbreviations

### Terms

- **attribute**: characteristic, quality, right or permission of a natural or legal person or of an object (see Article 3 (43) eIDAS)
- **authentic source**: repository or system, held under the responsibility of a public sector body or private entity, that contains and provides attributes and is considered primary or recognized as authentic (Article 3 (47) eIDAS)
- **authentic source interface**: interface allowing verification or retrieval of attributes stored in an authentic source (clause 6)
- **authentic source interface provider (ASIP)**: provider of the authentic source interface (can be the authentic source or an intermediary)
- **authorization server**: server issuing access tokens after authenticating the resource owner (IETF RFC 6749)
- **authorization server provider (AZSP)**: provider of an authorization server
- **catalogue of attributes**: digital repository maintained by the Commission (Article 2 (3) CIR 2025/1569)
- **client**: application making protected resource requests on behalf of the resource owner (IETF RFC 6749)
- **common services**: collection of services provided by the European Commission related to the catalogue of attributes and OOTS (CIR 2022/1463)
- **data service directory (DSD)**: registry of authentic sources and data services
- **discover interface (I1)**: interface for searching attribute unique identifiers and retrieving data service endpoints (clause 5)
- **discover interface provider (DIP)**: provider of the discover interface
- **electronic attestation of attributes**: attestation in electronic form that allows attributes to be authenticated (Article 3 (44) eIDAS)
- **European Digital Identity Wallet (EUDI Wallet)**: electronic identification means for storing, managing, validating PID and attributes (Article 3 (42) eIDAS)
- **Once-Only Technical System (OOTS)**: technical system for cross-border exchange of evidence (Regulation 2018/1724)
- **person identification data (PID)**: set of data enabling establishment of identity (Article 3 (3) eIDAS)
- **qualified trust service provider (QTSP)**: trust service provider granted qualified status by supervisory body (Article 3 (20) eIDAS)
- **resource owner**: entity capable of granting access to a protected resource (IETF RFC 6749)
- **resource server**: server hosting protected resources (IETF RFC 6749)
- **semantic repository (SR)**: catalogue of semantic assets (attributes, attestation schemes, code lists)
- **trust service provider (TSP)**: natural or legal person providing trust services (Article 3 (19) eIDAS)
- **user**: natural or legal person that is subject of the attribute and capable of authorizing access
- **wallet-relying party**: relying party intending to use wallet units (CIR 2025/848)
- **wallet-relying party access certificate (WRPAC)**: certificate for authenticating wallet-relying parties (ETSI TS 119 411-8)
- **wallet unit**: unique configuration of a wallet solution (CIR 2025/848)

### Abbreviations

API, ASIP, AZSP, CBOR, CDDL, CIR, DPoP, DSD, eID, eIDAS, EUDIW, GDPR, JSON, JSON-LD, JWT, MTLS, OOTS, OpenID4VCI, OpenID4VP, PID, PKCE, PubEAA, QTSP, RDF, RIM, SDG, SR, TSP, URI, URL, URN, UUID, WRPAC, XML

### Notation

- **REQ-ASIP-<clause number>-<id>**: requirement for Authentic Source Interface Provider
- **REQ-AZSP-<clause number>-<id>**: requirement for Authorization Server Provider
- **REQ-DIP-<clause number>-<id>**: requirement for Discover Interface Provider
- **REQ-TSP-<clause number>-<id>**: requirement for (Qualified) Trust Service Provider

## System Architecture

### Overview

The architecture comprises: Common Services (European Commission), Authentic Sources, Authorization Server, User, and Trust Service Providers. The Discover Interface (I1) enables searching for attribute identifiers and retrieving endpoint information. The Authentic Source Interface contains I2 (Verify) and optionally I3 (Retrieve).

### Common Services

Operated by the EC for OOTS; reused for the catalogue of attributes. I1 Discover interface is provided by a DIP.

### Authentic Source

**REQ-ASIP-4.3-01**: The ASIP shall provide the I2 (Verify) interface.  
**REQ-ASIP-4.3-02**: The ASIP may provide the I3 (Retrieve) interface.  
**REQ-ASIP-4.3-03**: The ASIP should impose access controls or other verification mechanisms that provide integrity, authenticity, and confidentiality to determine that the requester is a trust service provider and is acting at the request of a legitimate user.  
**REQ-ASIP-4.3-04**: The ASIP shall choose to support either:
- the interface based on HTTP/OAuth (clause 6.1) or
- the interface based on ISO 15000 (clause 6.2) or both.

### Authorization Server

**REQ-AZP-4.4-01 [CONDITIONAL]**: If the authentic source interface is based on HTTP (clause 6.1), there shall be an Authorization Server Provider (AZSP) operating an authorization server according to clause 6.1.3.  
**REQ-AZP-4.4-02 [CONDITIONAL]**: If the authentic source interface is based on ISO 15000 (clause 6.2), authorization shall be handled directly within the endpoints.

### User

The user interface (I5) provides PID to the TSP. Authentication, identification and authorization shall occur before the verification/retrieval request is sent.

### Trust Service Providers

- **QTSPs**: may access I2 (Verify) according to Article 45e and may access I3 (Retrieve) if supported.
- **Public Sector Electronic Attestation of Attributes Providers (PubEAA)**: may access I2 and/or I3 if granted.
- **Non-Qualified TSPs**: may access if granted by ASIP.

## Discover Interface (I1)

### General

**REQ-DIP-5.1-01**: The DIP shall provide the (I1) Discover interface, which allows to search for attributes and their unique identifier, as well as retrieve detailed information on specific data service endpoints.  
Provides two operations: **search** (find attributes in SR) and **retrieve** (lookup data services in DSD).

### Find Attributes (search)

**REQ-DIP-5.2.1-01**: The DIP shall provide the search query, allowing search for catalogued attribute-related metadata in the SR, optionally filtered.  
**REQ-DIP-5.2.1-02**: The search request shall be implemented as HTTP GET (IETF RFC 9110 clause 9.3.1).

#### Input parameters

**REQ-DIP-5.2.2-01**: The search query shall contain the parameter `assetType`, fixed to "attribute".  
**REQ-DIP-5.2.2-03**: May contain `creator` (string).  
**REQ-DIP-5.2.2-04**: May contain `country` (ISO 3166-1 alpha-2).  
**REQ-DIP-5.2.2-05**: May contain `text` (string for free-text search).  
**REQ-DIP-5.2.2-06**: May contain `semanticDataSpecification` (URI).  
**REQ-DIP-5.2.2-07**: May contain `schemaMediaType` (media type per IETF RFC 6838).

#### Output parameters

**REQ-DIP-5.2.3-01**: Output shall be an `attributes` object containing an array of `attribute` objects.  
**REQ-DIP-5.2.3-03**: Each `attribute` object shall contain `attributeIdentifier` (URI) with namespace, local identifier, version.  
**REQ-DIP-5.2.3-04**: May contain localized `title` elements (with `value` and `language`).  
**REQ-DIP-5.2.3-05**: May contain localized `description` elements.  
**REQ-DIP-5.2.3-06**: May contain `creator` (string).  
**REQ-DIP-5.2.3-07**: May contain `country` (ISO 3166-1 alpha-2).  
**REQ-DIP-5.2.3-08**: May contain `semanticDataSpecification` (URI).  
**REQ-DIP-5.2.3-09**: Shall contain one or more `schemaDistribution` elements with `accessURL` and `mediaType`.  
**REQ-DIP-5.2.3-11**: Output may contain additional elements.

### Find Data Services for Attributes (retrieve)

**REQ-DIP-5.3.1-01**: The DIP shall provide the retrieve query to lookup data services for verification/retrieval within a given Member State.  
**REQ-DIP-5.3.1-02**: Implemented as HTTP GET.

#### Input parameters

**REQ-DIP-5.3.2-01**: Shall have `queryType` (fixed "dataServices") and `attributeIdentifier` (URI).  
**REQ-DIP-5.3.2-02**: May contain `country` (ISO 3166-1 alpha-2); if omitted, all Member States returned.  
**REQ-DIP-5.3.2-03**: May contain `conformsTo` (URI) to filter by interface technology:  
- `urn:ietf:rfc:9110` for HTTP-based interface (clause 6.1)  
- `urn:iso:std:iso:15000` for ISO 15000-based interface (clause 6.2)

#### Output parameters

**REQ-DIP-5.3.3-01**: Output shall be a `dataServices` object containing an array of `dataService` elements.  
**REQ-DIP-5.3.3-03**: Each dataService element shall contain:  
1. `attributeIdentifier` (URI)  
2. `endpointDescription` (URI pointing to OpenAPI spec for HTTP, or URN `urn:iso:std:iso:15000` for ISO 15000)  
3. `endpointURI` (URL for HTTP, or party identifier for ISO 15000 per [i.18])  
4. `provider` (identification of ASIP with legalName, optional identifiers, establishedByLaw, currentAddress)  
**REQ-DIP-5.3.3-04**: May contain `country`.  
**REQ-DIP-5.3.3-05**: Output may contain additional elements.

### Use of HTTP and response format selection

**REQ-DIP-5.4-01**: The DIP shall support HTTP GET.  
**REQ-DIP-5.4-02**: The DIP shall support the Accept header.  
**REQ-DIP-5.4-03**: The DIP shall support at least one of:  
- `application/x-ebrs+xml` (ISO 15000-3 QueryManager response)  
- `application/json` (OpenAPI response per Annex A)  
**REQ-TSP-5.4-01**: (Q)TSPs should include the Accept header.  
**REQ-TSP-5.4-02**: (Q)TSPs shall examine the HTTP response body in addition to the status code.

## Authentic Source Interface

### Based on HTTP/OAuth (clause 6.1)

#### I2 (Verify) – Verify Request

**REQ-ASIP-6.1.1.1-01**: The I2 Verify interface shall use HTTP POST.  
**REQ-ASIP-6.1.1.1-02**: The POST /verify shall contain a `verifyRequest` object specifying attributes/fragments to verify.  
**REQ-ASIP-6.1.1.1-03**: May contain `attributes` property (array of `attribute` objects).  
**REQ-ASIP-6.1.1.1-04**: May contain `attributeFragments` property (array of `attributeFragment` objects with JSONPath).  
**REQ-ASIP-6.1.1.1-05**: Shall contain `attributes` or `attributeFragments` or both.  
**REQ-ASIP-6.1.1.1-06**: Each `attribute` object shall contain `attributeIdentifier` (URI) and `attributeValue` (JSON conforming to registered JSON schema).  
**REQ-ASIP-6.1.1.1-07**: Each `attributeFragment` object shall contain `attributeIdentifier`, `location` (JSONPath), and `value`.  
**REQ-ASIP-6.1.1.1-08**: The ASIP shall support verification of full attributes; may support fragments.  
**REQ-ASIP-6.1.1.1-09**: If fragments not supported, respond with 501 (Not Implemented).  
**REQ-ASIP-6.1.1.1-10**: The ASIP may support fuzzy matching (orthographic variations). If so, shall return the attribute value as stored in the authentic source in the response.  
**REQ-ASIP-6.1.1.1-11**: May contain a `mandate` property if verification is for another data subject.  
**REQ-ASIP-6.1.1.1-12**: The ASIP may support mandate handling.  
**REQ-ASIP-6.1.1.1-13**: If not supported, return 501.

#### I2 (Verify) – Verify Response

**REQ-ASIP-6.1.1.2-01**: The /verify response shall be a `verifyResponse` object.  
**REQ-ASIP-6.1.1.2-02**: May contain `attributeVerificationResults` array with one `attributeVerificationResult` per requested attribute.  
**REQ-ASIP-6.1.1.2-03**: Each result shall contain `attributeIdentifier`.  
**REQ-ASIP-6.1.1.2-04**: Shall contain `attributeVerificationResult` child with one of four URIs:  
- `http://uri.etsi.org/19478/VerificationResult/Match`  
- `http://uri.etsi.org/19478/VerificationResult/NoMatch`  
- `http://uri.etsi.org/19478/VerificationResult/MatchWithVariation`  
- `http://uri.etsi.org/19478/VerificationResult/Unknown`  

Conditionally includes `attributeValue`.  
**REQ-ASIP-6.1.1.2-05**: If fragment verification supported, shall include `fragmentVerificationResults`.  
**REQ-ASIP-6.1.1.2-06**: Each fragment result contains `attributeIdentifier`, `fragmentVerificationResult` (same URIs), and optionally `fragmentValue`.  
**REQ-ASIP-6.1.1.2-07**: The response shall contain `provider` (identification of ASIP).  
**REQ-ASIP-6.1.1.2-08**: If ASIP is different from authentic source, shall contain `authenticSource` element.  
**REQ-ASIP-6.1.1.2-09**: The `authenticSource` element shall have same structure as `provider`.  
**REQ-ASIP-6.1.1.2-10**: May contain `mandateResult`.  
**REQ-ASIP-6.1.1.2-12**: HTTP status codes: 200 (OK), 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), 501 (Not Implemented).

#### I3 (Retrieve)

**REQ-ASIP-6.1.2.1-01**: The I3 Retrieve interface shall use HTTP POST.  
**REQ-ASIP-6.1.2.1-02**: POST /retrieve shall contain a `retrieveRequest` object with `attributeIdentifiers` (one or more URIs).  
**REQ-ASIP-6.1.2.1-04**: May contain `mandate` property.  
**REQ-ASIP-6.1.2.2-01**: Response shall be a `retrieveResponse` object.  
**REQ-ASIP-6.1.2.2-02**: If successful, shall contain `attributes` array (attribute objects as per request).  
**REQ-ASIP-6.1.2.2-03**: Shall contain `provider` element.  
**REQ-ASIP-6.1.2.2-04**: If ASIP is different from authentic source, shall contain `authenticSource`.  
**REQ-ASIP-6.1.2.2-05**: May contain `mandateResult`.  
**REQ-ASIP-6.1.2.2-06**: HTTP status codes: 200, 400, 401, 404, 501.

#### I4 (Authorize)

**REQ-AZSP-6.1.3.1-01**: Authorization shall be realized with OAuth 2.0 authorization code flow (IETF RFC 6749).  
**REQ-AZSP-6.1.3.1-02**: The authorization server shall identify the user.  
**REQ-AZSP-6.1.3.1-03**: May use EUDI Wallet (OpenID4VP) or alternative (ETSI TS 119 461).  
**REQ-AZSP-6.1.3.1-04**: Shall support PKCE (IETF RFC 7636).  
**REQ-TSP-6.1.3.1-01**: The (Q)TSP shall use PKCE.  
**REQ-AZSP-6.1.3.1-05**: Shall mandate MTLS (IETF RFC 8705) or private_key_jwt (OpenID Connect) for client authentication.  
**REQ-TSP-6.1.3.1-02**: The (Q)TSP shall use the mandated mechanism.  
**REQ-AZSP-6.1.3.1-06**: Shall support sender-constrained access tokens (MTLS or DPoP).  
**REQ-TSP-6.1.3.1-03**: The (Q)TSP shall use the supported mechanism.  
**REQ-AZSP-6.1.3.1-07**: Shall support dynamic client registration (IETF RFC 7591).  
**REQ-AZSP-6.1.3.1-08**: Shall use JWT-based access tokens (IETF RFC 9068) containing required identification data.

##### Dynamic Client Registration (IETF RFC 7591)

**REQ-AZSP-6.1.3.2-01**: The authorization server shall support dynamic client registration with a sealed software statement.  
**REQ-TSP-6.1.3.2-01**: The (Q)TSP shall use an X.509 certificate (IETF RFC 5280) for creating signed/ sealed software statements.  
**REQ-TSP-6.1.3.2-02**: The certificate shall contain information to identify the (Q)TSP.  
**REQ-TSP-6.1.3.2-03**: Should contain information enabling automated check of trust service provider status.  
**REQ-AZSP-6.1.3.2-02**: Should accept Wallet-Relying Party Access Certificates (WRPAC) per ETSI TS 119 411-8.

##### Authorization Code Flow (IETF RFC 6749)

Figure 3 (informative) describes the overall process: user requests attestation → (Q)TSP discovers attribute and service → authorization request with PKCE → user authentication/identification (e.g. via EUDI Wallet) → authorization response → access token request → token issuance → resource request (verify/retrieve) → attestation issuance.

##### Security considerations

**REQ-AZSP-6.1.3.4-01**: The authorization server shall take into account security considerations from IETF RFC 6819, RFC 7636, RFC 9700, and FAPI 2.0 Security Profile.  
**REQ-AZSP-6.1.3.4-02**: Shall be operated in a trustworthy environment with an ISMS (e.g. ISO/IEC 27001).

### Based on ISO 15000 (clause 6.2)

#### Overview

**REQ-ASIP-6.2.1-01**: The I2 (Verify) interface based on ISO 15000 shall be as specified in clause 6.2.3.  
**REQ-ASIP-6.2.1-02 [CONDITIONAL]**: The I3 (Retrieve) interface based on ISO 15000 shall be as specified in clause 6.2.4, if supported.  
Uses request-response pattern between requester and provider. Requests contain data subject identification and attribute value pairs. Responses: successful, failure error, or deferred.

#### Protocol Binding

**REQ-ASIP-6.2.2-01**: All messages shall be exchanged using the OASIS ebXML Messaging Protocol Binding for RegRep Version 1.0 (ISO 15000-2 and -3).  
**REQ-ASIP-6.2.2-02**: A provider or community may mandate additional implementation guidelines.  
**REQ-ASIP-6.2.2-03 [CONDITIONAL]**: If additional guidelines are mandated, all requestors shall follow them.

#### I2 (Verify) – Verify Request

**REQ-ASIP-6.2.3.1-01**: The verification request shall be an XML document rooted in `query:QueryRequest` with attributes `id` (UUID) and six mandatory `rim:Slot` child elements:  
1. `SpecificationIdentifier` (fixed "https://uri.etsi.org/19478/v1.1.1")  
2. `IssueDateTime` (ISO 8601-1)  
3. `Requester` (NaturalPersonValueType or LegalPersonValueType)  
4. `Provider` (same)  
5. `IssuingPurposeQEAA` (Boolean)  
6. `ExplicitRequestGiven` (Boolean)  
**REQ-ASIP-6.2.3.1-02 [CONDITIONAL]**: For deferred response retrieval, shall contain `DeferredResponseIdentifier` slot.  
**REQ-ASIP-6.2.3.1-03**: The `query:Query` element shall be of fixed type "VerificationQuery" with slots `Person` and `VerificationQueryDetails`.  
**REQ-ASIP-6.2.3.1-04**: For each attribute, a separate `AttributeVerificationQuery` element within `VerificationsQueryDetails`.  
**REQ-ASIP-6.2.3.1-05**: Each `AttributeVerificationQuery` shall have `AttributeIdentifier` (xs:anyURI).  
**REQ-ASIP-6.2.3.1-06**: May contain `Schema` (URI).  
**REQ-ASIP-6.2.3.1-07**: May contain `SchemaMediaType`. If Schema present, SchemaMediaType shall also be present.  
**REQ-ASIP-6.2.3.1-08**: Shall include exactly one of: `TextValue`, `XMLValue`, or `AttributeProperties`.  
- `TextValue`: for JSON or atomic text; may have `encoding` (base64) and `xml:lang`.  
- `XMLValue`: for complex XML content.  
- `AttributeProperties`: for selected properties; contains `ExpressionLanguage` (URI) and `AttributeProperty` with `QueryExpression` and `TextValue`/`XMLValue`.  
**REQ-ASIP-6.2.3.1-09**: `ExpressionLanguage` URIs: `https://www.w3.org/TR/xpath-31/` for XML, `urn:ietf:rfc:9535` for JSON.  
**REQ-ASIP-6.2.3.1-12**: The QueryRequest shall include `ResponseOption` with returnType "RegistryObject".

#### I2 (Verify) – Verify Response

##### Successful

**REQ-ASIP-6.2.3.2.1-01**: Successful immediate response: `query:QueryResponse` with status `Success`.  
**REQ-ASIP-6.2.3.2.1-02**: Has attribute `requestId` matching request `id`.  
**REQ-ASIP-6.2.3.2.1-03**: Contains five slots: `SpecificationIdentifier`, `ResponseIdentifier` (UUID), `IssueDateTime`, `Requester`, `Provider`.  
**REQ-ASIP-6.2.3.2.1-04**: Contains `rim:RegistryObjectList` with one `RegistryObject` per request. No `Exception`. No `ResponseAvailableDateTime`.  
**REQ-ASIP-6.2.3.2.1-05**: Each `RegistryObject` contains slots `Person` and `VerificationResponseDetails`.  
**REQ-ASIP-6.2.3.2.1-06**: ASIP may support fuzzy matching; if so, shall return attribute value as stored in authentic source.  
**REQ-ASIP-6.2.3.2.1-07**: Contains `AttributeVerificationResponse` with `AttributeIdentifier`, optionally `Schema` and `SchemaMediaType` (copies from request), and exactly one of `TextValue`, `XMLValue`, `AttributeProperties` (with values from source).  
**REQ-ASIP-6.2.3.2.1-08-05**: If ASIP is different from authentic source, shall contain `AuthenticSource` (PersonType).  
**REQ-ASIP-6.2.3.2.1-08-06**: `VerificationResult` with one of the four URIs (Match, NoMatch, MatchWithVariation, Unknown).

##### Failure Error Response

**REQ-ASIP-6.2.3.2.2-01**: Failure response: `query:QueryResponse` with status `Failure`.  
**REQ-ASIP-6.2.3.2.2-03**: Contains mandatory slots as above.  
**REQ-ASIP-6.2.3.2.2-04**: May contain `ErrorProvider` if different from ASIP.  
**REQ-ASIP-6.2.3.2.2-06**: Contains `rim:Exception` (type `ObjectNotFoundExceptionType` for non-match, other types for other errors).  
**REQ-ASIP-6.2.3.2.2-07**: Exception contains `TimeStamp` slot.

##### Deferred Response

**REQ-ASIP-6.2.3.2.3-01 [CONDITIONAL]**: If outcome not immediately available, response with status `Unavailable`.  
**REQ-ASIP-6.2.3.2.3-02**: Contains empty `RegistryObjectList`.  
**REQ-ASIP-6.2.3.2.3-03**: No `Exception`.  
**REQ-ASIP-6.2.3.2.3-04**: Contains mandatory slots plus `ResponseAvailableDateTime` (ISO 8601-1).

#### I3 (Retrieve) – Overview

**REQ-ASIP-6.2.4.1-01**: The I3 Retrieve protocol is a variant of I2 Verify; clause 6.2.3 applies except as specified.

#### I3 (Retrieve) – Retrieve Request

**REQ-ASIP-6.2.4.2-01**: XML document rooted in `query:QueryRequest` with same six slots as Verify Request.  
**REQ-ASIP-6.2.4.2-02 [CONDITIONAL]**: For deferred response retrieval, include `DeferredResponseIdentifier`.  
**REQ-ASIP-6.2.4.2-03**: `query:Query` of fixed type "RetrieveQuery" with slots `Person` and `RetrieveQueryDetails`.  
**REQ-ASIP-6.2.4.2-05**: For each attribute, a separate `AttributeRetrieveQuery` element.  
**REQ-ASIP-6.2.4.2-06**: Each `AttributeRetrieveQuery` shall contain `AttributeIdentifier` (xs:anyURI). May contain `Schema` and `SchemaMediaType`. If Schema omitted, attribute returned in all available distributions.

#### I3 (Retrieve) – Retrieve Response

##### Successful

**REQ-ASIP-6.2.4.3.1-01**: Successful immediate response: status `Success`, attribute `requestId`.  
**REQ-ASIP-6.2.4.3.1-02**: Contains same five slots as Verify Response.  
**REQ-ASIP-6.2.4.3.1-03**: Contains `RegistryObjectList` (one per request, no Exception, no `ResponseAvailableDateTime`).  
**REQ-ASIP-6.2.4.3.1-04**: Each `RegistryObject` contains `Person` and `RetrieveResponseDetails`.  
**REQ-ASIP-6.2.4.3.1-04-03**: `AttributeRetrieveResponse` contains `AttributeIdentifier`, optionally `Schema`, `SchemaMediaType`, exactly one of `TextValue` or `XMLValue`, and `RetrieveResult` with one of:  
- `http://uri.etsi.org/19478/RetrieveResultTypes/Success`  
- `http://uri.etsi.org/19478/RetrieveResultTypes/Failure`

##### Failure Error Response

**REQ-ASIP-6.2.4.3.2-01**: Follows verify failure error response (clause 6.2.3.2.2).

##### Deferred Response

**REQ-ASIP-6.2.4.3.3-01**: Follows verify deferred response (clause 6.2.3.2.3).

## Normative Annexes (Condensed)

- **Annex A (normative): OpenAPI Specification for Discover Interface** – The DIP shall provide the Discover Interface based on the OpenAPI 3.0 specification file at the ETSI forge URL. Integrates JSON schemas for search and retrieve responses.
- **Annex B (normative): OpenAPI Specification for Authentic Source Interface** – The ASIP shall provide the HTTP/OAuth interface based on the OpenAPI 3.0 specification file at the ETSI forge URL. Integrates JSON schema for provider object.
- **Annex C (normative): XML-Schemata for PID and RIM binding** – Three XSD files (PID schema, Interface Details schema, Interface Details RIM Binding schema) define the XML types used in the ISO 15000-based interface.
- **Annex D (informative): XML-Examples** – Provides example XML files for verify request, successful response, and failure response.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| REQ-ASIP-4.3-01 | The ASIP shall provide the I2 (Verify) interface. | shall | clause 4.3 |
| REQ-ASIP-4.3-02 | The ASIP may provide the I3 (Retrieve) interface. | may | clause 4.3 |
| REQ-ASIP-4.3-03 | The ASIP should impose access controls... | should | clause 4.3 |
| REQ-ASIP-4.3-04 | The ASIP shall choose to support HTTP/OAuth or ISO 15000 or both. | shall | clause 4.3 |
| REQ-AZP-4.4-01 | If HTTP interface, there shall be an AZSP. | shall (conditional) | clause 4.4 |
| REQ-AZP-4.4-02 | If ISO 15000, authorization handled directly. | shall (conditional) | clause 4.4 |
| REQ-DIP-5.1-01 | The DIP shall provide the (I1) Discover interface. | shall | clause 5.1 |
| REQ-DIP-5.2.1-01 | Provide search query. | shall | clause 5.2.1 |
| REQ-DIP-5.2.1-02 | Search as HTTP GET. | shall | clause 5.2.1 |
| REQ-DIP-5.2.2-01 | Search query shall contain assetType="attribute". | shall | clause 5.2.2 |
| REQ-DIP-5.2.2-03 to -07 | Optional parameters (creator, country, text, etc.). | may | clause 5.2.2 |
| REQ-DIP-5.2.3-01 | Output attributes object. | shall | clause 5.2.3 |
| REQ-DIP-5.2.3-03 | attributeIdentifier URI. | shall | clause 5.2.3 |
| REQ-DIP-5.3.1-01 | Provide retrieve query. | shall | clause 5.3.1 |
| REQ-DIP-5.3.1-02 | Retrieve as HTTP GET. | shall | clause 5.3.1 |
| REQ-DIP-5.3.2-01 | Input: queryType, attributeIdentifier. | shall | clause 5.3.2 |
| REQ-DIP-5.3.3-01 | Output dataServices object. | shall | clause 5.3.3 |
| REQ-DIP-5.4-01 | Support HTTP GET. | shall | clause 5.4 |
| REQ-DIP-5.4-02 | Support Accept header. | shall | clause 5.4 |
| REQ-DIP-5.4-03 | Support at least one response media type. | shall | clause 5.4 |
| REQ-TSP-5.4-01 | Should include Accept header. | should | clause 5.4 |
| REQ-TSP-5.4-02 | Examine response body. | shall | clause 5.4 |
| REQ-ASIP-6.1.1.1-01 | I2 Verify uses HTTP POST. | shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-02 | verifyRequest object. | shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-03 to -05 | attributes/attributeFragments. | may/shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-06 | attribute object with identifier and value. | shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-07 | attributeFragment object. | shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-08 | Support full attributes; may support fragments. | shall/may | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-09 | If fragments not supported, return 501. | shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-10 | Fuzzy matching support. | may | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.1-11 to -13 | mandate handling. | may/shall | clause 6.1.1.1 |
| REQ-ASIP-6.1.1.2-01 | verifyResponse object. | shall | clause 6.1.1.2 |
| REQ-ASIP-6.1.1.2-02 to -04 | attributeVerificationResults with URIs. | shall | clause 6.1.1.2 |
| REQ-ASIP-6.1.1.2-05 to -06 | fragmentVerificationResults. | conditional | clause 6.1.1.2 |
| REQ-ASIP-6.1.1.2-07 | provider element. | shall | clause 6.1.1.2 |
| REQ-ASIP-6.1.1.2-08 to -09 | authenticSource if ASIP different. | conditional | clause 6.1.1.2 |
| REQ-ASIP-6.1.1.2-12 | HTTP status codes. | shall | clause 6.1.1.2 |
| REQ-ASIP-6.1.2.1-01 | I3 Retrieve uses HTTP POST. | shall | clause 6.1.2.1 |
| REQ-ASIP-6.1.2.1-02 | retrieveRequest with attributeIdentifiers. | shall | clause 6.1.2.1 |
| REQ-ASIP-6.1.2.1-04 | mandate optional. | may | clause 6.1.2.1 |
| REQ-ASIP-6.1.2.2-01 | retrieveResponse object. | shall | clause 6.1.2.2 |
| REQ-ASIP-6.1.2.2-02 | attributes array if successful. | conditional | clause 6.1.2.2 |
| REQ-ASIP-6.1.2.2-03 to -04 | provider/authenticSource. | shall/conditional | clause 6.1.2.2 |
| REQ-ASIP-6.1.2.2-06 | HTTP status codes. | shall | clause 6.1.2.2 |
| REQ-AZSP-6.1.3.1-01 | Authorization via OAuth 2.0 code flow. | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-02 | Identify user. | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-03 | May use EUDI Wallet or alternative. | may | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-04 | Support PKCE. | shall | clause 6.1.3.1 |
| REQ-TSP-6.1.3.1-01 | Use PKCE. | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-05 | Mandate MTLS or private_key_jwt. | shall | clause 6.1.3.1 |
| REQ-TSP-6.1.3.1-02 | Use mandated client authentication. | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-06 | Support sender-constrained tokens (MTLS/DPoP). | shall | clause 6.1.3.1 |
| REQ-TSP-6.1.3.1-03 | Use supported access token protection. | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-07 | Support dynamic client registration (RFC 7591). | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.1-08 | Use JWT access tokens (RFC 9068). | shall | clause 6.1.3.1 |
| REQ-AZSP-6.1.3.2-01 | Support dynamic registration with software statement. | shall | clause 6.1.3.2 |
| REQ-TSP-6.1.3.2-01 | Use X.509 certificate for software statement. | shall | clause 6.1.3.2 |
| REQ-TSP-6.1.3.2-02 | Certificate shall identify the (Q)TSP. | shall | clause 6.1.3.2 |
| REQ-TSP-6.1.3.2-03 | Should enable automated entitlement check. | should | clause 6.1.3.2 |
| REQ-AZSP-6.1.3.2-02 | Should accept WRPAC. | should | clause 6.1.3.2 |
| REQ-AZSP-6.1.3.4-01 | Consider security from RFCs and FAPI 2.0. | shall | clause 6.1.3.4 |
| REQ-AZSP-6.1.3.4-02 | Operate in trustworthy environment. | shall | clause 6.1.3.4 |
| REQ-ASIP-6.2.1-01 | I2 Verify based on ISO 15000. | shall | clause 6.2.1 |
| REQ-ASIP-6.2.1-02 | I3 Retrieve if supported. | conditional | clause 6.2.1 |
| REQ-ASIP-6.2.2-01 | Use ebXML RegRep protocol binding. | shall | clause 6.2.2 |
| REQ-ASIP-6.2.2-02 | May mandate additional guidelines. | may | clause 6.2.2 |
| REQ-ASIP-6.2.2-03 | Follow guidelines if mandated. | conditional | clause 6.2.2 |
| REQ-ASIP-6.2.3.1-01 | Verify request format and slots. | shall | clause 6.2.3.1 |
| REQ-ASIP-6.2.3.2.1-01 | Successful response status Success. | shall | clause 6.2.3.2.1 |
| REQ-ASIP-6.2.3.2.2-01 | Failure response status Failure. | shall | clause 6.2.3.2.2 |
| REQ-ASIP-6.2.3.2.3-01 | Deferred response status Unavailable. | conditional | clause 6.2.3.2.3 |
| REQ-ASIP-6.2.4.1-01 | Retrieve protocol variant of Verify. | shall | clause 6.2.4.1 |
| REQ-ASIP-6.2.4.3.1-01 | Successful retrieve status Success. | shall | clause 6.2.4.3.1 |
| REQ-ASIP-6.2.4.3.1-04 | Response details with AttributeRetrieveResponse. | shall | clause 6.2.4.3.1 |
| REQ-ASIP-6.2.4.3.2-01 | Failure error follows verify failure. | shall | clause 6.2.4.3.2 |
| REQ-ASIP-6.2.4.3.3-01 | Deferred follows verify deferred. | shall | clause 6.2.4.3.3 |

## Informative Annexes (Condensed)

- **Annex D (informative): XML-Examples** – Contains example XML files for verify request, successful verify response, and failure verify response, located at ETSI forge URLs, to illustrate the ISO 15000-based interface messages.