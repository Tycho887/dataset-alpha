# RFC 7591: OAuth 2.0 Dynamic Client Registration Protocol
**Source**: IETF | **Version**: Standards Track | **Date**: July 2015 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc7591

## Scope (Summary)
Defines mechanisms for dynamically registering OAuth 2.0 clients with authorization servers. Registration requests send desired client metadata; responses return a client identifier and registered metadata. Also defines common client metadata fields and values.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5646] Phillips, A. and M. Davis, "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.
- [RFC6749] Hardt, D., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750, October 2012.
- [RFC7120] Cotton, M., "Early IANA Allocation of Standards Track Code Points", BCP 100, RFC 7120, January 2014.
- [RFC7159] Bray, T., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, March 2014.
- [RFC7515] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015.
- [RFC7517] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015.
- [RFC7519] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, May 2015.
- [RFC7522] Campbell, B., Mortimore, C., and M. Jones, "Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants", RFC 7522, May 2015.
- [RFC7523] Jones, M., Campbell, B., and C. Mortimore, "JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants", RFC 7523, May 2015.
- [BCP195] Sheffer, Y., Holz, R., and P. Saint-Andre, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525, May 2015.
- [IANA.Language] IANA, "Language Subtag Registry", <http://www.iana.org/assignments/language-subtag-registry>.

## Definitions and Abbreviations
- **access token**: As defined in OAuth 2.0 [RFC6749].
- **authorization code**: As defined in OAuth 2.0 [RFC6749].
- **authorization endpoint**: As defined in OAuth 2.0 [RFC6749].
- **authorization grant**: As defined in OAuth 2.0 [RFC6749].
- **authorization server**: As defined in OAuth 2.0 [RFC6749].
- **client**: As defined in OAuth 2.0 [RFC6749].
- **client identifier**: As defined in OAuth 2.0 [RFC6749].
- **client secret**: As defined in OAuth 2.0 [RFC6749].
- **grant type**: As defined in OAuth 2.0 [RFC6749].
- **protected resource**: As defined in OAuth 2.0 [RFC6749].
- **redirection URI**: As defined in OAuth 2.0 [RFC6749].
- **refresh token**: As defined in OAuth 2.0 [RFC6749].
- **resource owner**: As defined in OAuth 2.0 [RFC6749].
- **resource server**: As defined in OAuth 2.0 [RFC6749].
- **response type**: As defined in OAuth 2.0 [RFC6749].
- **token endpoint**: As defined in OAuth 2.0 [RFC6749].
- **Claim**: As defined in JSON Web Token (JWT) [RFC7519].
- **Client Software**: Software implementing an OAuth 2.0 client.
- **Client Instance**: A deployed instance of a piece of client software.
- **Client Developer**: The person or organization that builds a client software package and prepares it for distribution.
- **Client Registration Endpoint**: OAuth 2.0 endpoint through which a client can be registered at an authorization server.
- **Initial Access Token**: OAuth 2.0 access token optionally issued by an authorization server to a developer or client and used to authorize calls to the client registration endpoint.
- **Deployment Organization**: An administrative security domain under which a software API (service) is deployed and protected by an OAuth 2.0 framework.
- **Software API Deployment**: A deployed instance of a software API that is protected by OAuth 2.0 in a particular deployment organization domain.
- **Software API Publisher**: The organization that defines a particular web-accessible API that may be deployed in one or more deployment environments.
- **Software Statement**: A digitally signed or MACed JSON Web Token (JWT) [RFC7519] that asserts metadata values about the client software.

## 1. Introduction
Describes OAuth 2.0 dynamic client registration. Used to obtain a client identifier and metadata. A software statement (digitally signed/MACed JWT) can be used to present metadata. Generalizes mechanisms from OpenID Connect Dynamic Client Registration 1.0 and UMA Profile.

### 1.1. Notational Conventions
- The key words 'MUST', 'MUST NOT', 'REQUIRED', 'SHALL', 'SHALL NOT', 'SHOULD', 'SHOULD NOT', 'RECOMMENDED', 'MAY', and 'OPTIONAL' in this document are to be interpreted as described in [RFC2119].
- Unless otherwise noted, all protocol parameter names and values are case sensitive.

### 1.2. Terminology
See Definitions above.

### 1.3. Protocol Flow
- **(A)** Optionally, client/developer is issued initial access token.
- **(B)** Optionally, client/developer is issued software statement.
- **(C)** Client/developer calls client registration endpoint with desired registration metadata, optionally including initial access token.
- **(D)** Authorization server registers client and returns registered metadata, client identifier, and client credentials (if applicable).

## 2. Client Metadata
Registered clients have associated metadata. Metadata used as input to registration requests and output in responses.

- **redirect_uris**: Array of redirection URI strings for redirect-based flows. Clients using flows with redirection MUST register their redirection URI values. Authorization servers that support dynamic registration for redirect-based flows MUST implement support for this metadata value.
- **token_endpoint_auth_method**: String indicator of requested authentication method for token endpoint. Defined values: "none", "client_secret_post", "client_secret_basic". Additional values can be registered via IANA registry. If unspecified, default is "client_secret_basic".
- **grant_types**: Array of OAuth 2.0 grant type strings. Defined values: "authorization_code", "implicit", "password", "client_credentials", "refresh_token", "urn:ietf:params:oauth:grant-type:jwt-bearer", "urn:ietf:params:oauth:grant-type:saml2-bearer". If omitted, default is "authorization_code".
- **response_types**: Array of OAuth 2.0 response type strings. Defined values: "code", "token". If omitted, default is "code".
- **client_name**: Human-readable string name of the client. RECOMMENDED to always send. May be internationalized per Section 2.2.
- **client_uri**: URL string of a web page providing information about the client. RECOMMENDED to always send. MUST point to valid web page. May be internationalized.
- **logo_uri**: URL string referencing a logo. MUST point to valid image file. May be internationalized.
- **scope**: Space-separated list of scope values.
- **contacts**: Array of strings representing ways to contact people responsible for client (e.g., email addresses).
- **tos_uri**: URL string pointing to terms of service document. MUST point to valid web page. May be internationalized.
- **policy_uri**: URL string pointing to privacy policy. MUST point to valid web page. May be internationalized.
- **jwks_uri**: URL string referencing client's JSON Web Key Set [RFC7517] document. MUST point to valid JWK Set. Use preferred over jwks for key rotation. jwks_uri and jwks MUST NOT both be present.
- **jwks**: Client's JSON Web Key Set [RFC7517] document value (JSON object). jwks_uri and jwks MUST NOT both be present.
- **software_id**: Unique identifier string (e.g., UUID) assigned by client developer/publisher. SHOULD remain same for all instances and across updates.
- **software_version**: Version identifier string. SHOULD change on any update. Comparison using string equality.
- **Extensions**: Metadata names can be registered per IANA Section 4. Authorization server MUST ignore unknown metadata. Server MAY reject or replace requested values.

### 2.1. Relationship between Grant Types and Response Types
- Server SHOULD ensure consistency (e.g., return invalid_client_metadata error if inconsistent).
- Mapping: authorization_code ↔ code; implicit ↔ token; others have no response type.

### 2.2. Human-Readable Client Metadata
- May be represented in multiple languages/scripts using BCP 47 language tags appended with "#" (e.g., "client_name#en").
- RECOMMENDED to use language tags as registered in IANA Language Subtag Registry, case-insensitively.
- If no language tag, no assumptions about language; RECOMMENDED to have a language-neutral value.

### 2.3. Software Statement
- A JWT [RFC7519] that asserts metadata values about client software.
- MUST be digitally signed or MACed using JWS [RFC7515] and MUST contain "iss" claim.
- RECOMMENDED to use "RS256" signature and include "software_id" claim.
- Authorization server MAY accept software statement as client identifier directly without prior registration (conditions out of scope).

## 3. Client Registration Endpoint
- MUST accept HTTP POST with "application/json" entity body.
- MUST be protected by transport-layer security (see Section 5).
- MAY be an OAuth 2.0 protected resource and accept initial access token.
- SHOULD allow registration with no authorization (open registration), possibly rate-limited.

### 3.1. Client Registration Request
- HTTP POST to endpoint, content type "application/json". JSON object containing requested client metadata.
- Authorization server assigns client identifier, optionally client secret, and associates metadata. May provision defaults.

#### 3.1.1. Client Registration Request Using a Software Statement
- OPTIONAL member "software_statement": string containing entire signed JWT.
- If server supports software statements, client metadata values in software statement MUST take precedence over plain JSON elements.

### 3.2. Responses
- Successful: HTTP 201 Created, "application/json" body with client information.
- Unsuccessful: error response as per Section 3.2.2.

#### 3.2.1. Client Information Response
- **client_id**: REQUIRED. OAuth 2.0 client identifier string. SHOULD NOT be currently valid for any other registered client.
- **client_secret**: OPTIONAL. MUST be unique per client_id. SHOULD be unique for multiple instances.
- **client_id_issued_at**: OPTIONAL. Time as seconds from Unix epoch.
- **client_secret_expires_at**: REQUIRED if client_secret issued. Time or 0 if no expiration.
- Server MUST return all registered metadata, possibly replaced or rejected values.
- If software statement used, it MUST be returned unmodified as "software_statement".

#### 3.2.2. Client Registration Error Response
- For OAuth errors, appropriate response for token type.
- For registration errors: HTTP 400 (unless specified), JSON object with members:
  - **error**: REQUIRED. Single ASCII error code.
  - **error_description**: OPTIONAL. Human-readable description.
- Defined error codes:
  - **invalid_redirect_uri**
  - **invalid_client_metadata**
  - **invalid_software_statement**
  - **unapproved_software_statement**
- Other members must be ignored if not understood.

## 4. IANA Considerations
### 4.1. OAuth Dynamic Client Registration Metadata Registry
- Specification Required [RFC5226] after review on oauth-ext-review@ietf.org.
- Designated Experts approve/deny.
- Registration template: Client Metadata Name (case-sensitive), Description, Change Controller, Specification Document(s).
- Initial registry contents include all metadata fields defined in Section 2 (redirect_uris, token_endpoint_auth_method, grant_types, response_types, client_name, client_uri, logo_uri, scope, contacts, tos_uri, policy_uri, jwks_uri, jwks, software_id, software_version, client_id, client_secret, client_id_issued_at, client_secret_expires_at).

### 4.2. OAuth Token Endpoint Authentication Methods Registry
- Specification Required [RFC5226] after review on oauth-ext-review@ietf.org.
- Registration template: Token Endpoint Authentication Method Name (case-sensitive), Change Controller, Specification Document(s).
- Initial contents: "none", "client_secret_post", "client_secret_basic".

## 5. Security Considerations (Condensed)
- Authorization server MUST require TLS (MUST support TLS 1.2 [RFC5246], MAY support others). Client MUST perform TLS/SSL certificate check per RFC 6125.
- For redirect-based grant types, authorization servers MUST require registration of redirection URI values. Registered URIs MUST be one of: remote web site protected by TLS, local machine HTTP URI, or non-HTTP app-specific URL.
- Public clients (token_endpoint_auth_method="none") may register; server may expire registrations.
- Server MAY require separate registrations for different grant types; may return invalid_client_metadata.
- Unless in software statement, metadata is self-asserted; server must take steps to mitigate impersonation.
- For open registration, server must be careful with user-displayed URLs; SHOULD check host/scheme match redirect_uris, and protect against malicious content.
- If both direct JSON and software statement present, software statement values MUST take precedence if valid.
- Full registration request (software statement, initial access token, JSON metadata) must be considered.
- If duplication detected (same software_id/version), SHOULD treat new registration as suspect.
- Server SHOULD NOT issue same client secret to multiple instances; SHOULD NOT issue same client_id to different instances unless careful.

## 6. Privacy Considerations (Condensed)
- Main privacy concern is the "contacts" field; developers should use dedicated contact emails.
- Client identifiers can be used for tracking, but resource owner authorization still needed.
- Clients are forbidden from creating their own client identifier; uniqueness per registration helps privacy.

## 7. References
### 7.1. Normative References (listed above)
### 7.2. Informative References
- [OpenID.Discovery] Sakimura et al., "OpenID Connect Discovery 1.0", November 2014.
- [OpenID.Registration] Sakimura et al., "OpenID Connect Dynamic Client Registration 1.0", November 2014.
- [RFC7592] Richer et al., "OAuth 2.0 Dynamic Client Registration Management Protocol", RFC 7592, July 2015.
- [UMA-Core] Hardjono et al., "User-Managed Access (UMA) Profile of OAuth 2.0", Work in Progress, April 2015.

## Appendix A. Use Cases (Condensed)
- **A.1 Open vs. Protected**: Open registration no initial token; protected requires initial access token.
- **A.2 Without/With Software Statement**: Without: self-asserted; With: attested by authority.
- **A.3 Registration by Client or Developer**: Client registers itself; developer preregisters and packages client ID.
- **A.4 Client ID per Instance or per Software**: Per instance: distinct IDs; per software: shared ID.
- **A.5 Stateful or Stateless**: Stateful: server maintains state; stateless: encode state in client ID.

## Requirements Summary

| ID  | Requirement | Type | Reference |
|-----|-------------|------|-----------|
| R1  | Clients using redirect-based flows MUST register their redirection URI values. | MUST | Section 2, redirect_uris |
| R2  | Authorization servers that support dynamic registration for redirect-based flows MUST implement support for redirect_uris metadata. | MUST | Section 2 |
| R3  | The client registration endpoint MUST accept HTTP POST with application/json. | MUST | Section 3 |
| R4  | The client registration endpoint MUST be protected by transport-layer security. | MUST | Section 3, Section 5 |
| R5  | Authorization server MUST require use of TLS; MUST support TLS 1.2. | MUST | Section 5 |
| R6  | When using TLS, client MUST perform TLS/SSL server certificate check per RFC 6125. | MUST | Section 5 |
| R7  | For redirect-based grant types, authorization servers MUST require clients to register redirection URI values. | MUST | Section 5 |
| R8  | Registered redirection URI values MUST be one of: remote TLS site, local machine HTTP, non-HTTP app-specific URL. | MUST | Section 5 |
| R9  | If software statement is valid and signed by acceptable authority, values within it MUST take precedence over plain JSON. | MUST | Section 2, Section 5 |
| R10 | jwks_uri and jwks MUST NOT both be present in the same request or response. | MUST | Section 2 |
| R11 | The authorization server MUST ignore any client metadata it does not understand. | MUST | Section 2 |
| R12 | The authorization server MUST return all registered metadata in response. | MUST | Section 3.2.1 |
| R13 | client_id is REQUIRED in successful response. | REQUIRED | Section 3.2.1 |
| R14 | client_secret_expires_at is REQUIRED if client_secret is issued. | REQUIRED | Section 3.2.1 |
| R15 | If software statement used, it MUST be returned unmodified in response. | MUST | Section 3.2.1 |
| R16 | Software statement MUST be digitally signed or MACed using JWS and MUST contain "iss" claim. | MUST | Section 2.3 |
| R17 | Authorization server MUST treat all client metadata as self-asserted unless in software statement. | MUST | Section 5 |
| R18 | Authorization server MUST consider full registration request when deciding to honor it. | MUST | Section 5 |
| R19 | Clients are forbidden from creating their own client identifier. | MUST NOT | Section 6 |
| R20 | (Implicit) The token_endpoint_auth_method default is "client_secret_basic". | Default | Section 2 |
| R21 | (Implicit) grant_types default is "authorization_code". | Default | Section 2 |
| R22 | (Implicit) response_types default is "code". | Default | Section 2 |
| R23 | Server SHOULD ensure consistency between grant_types and response_types. | SHOULD | Section 2.1 |
| R24 | Client registration endpoint SHOULD allow registration with no authorization (open). | SHOULD | Section 3 |
| R25 | Client name and client_uri: RECOMMENDED to always send. | RECOMMENDED | Section 2 |
| R26 | Software signatures: RECOMMENDED to use RS256. | RECOMMENDED | Section 2.3 |
| R27 | Software statements: RECOMMENDED to contain software_id. | RECOMMENDED | Section 2.3 |
| R28 | Human-readable fields without language tags: RECOMMENDED to have language-neutral values. | RECOMMENDED | Section 2.2 |
| R29 | Language tag values: SHOULD be interpreted case-insensitively. | SHOULD | Section 2.2 |
| R30 | client_id SHOULD NOT be currently valid for any other registered client. | SHOULD | Section 3.2.1 |
| R31 | client_secret SHOULD be unique for multiple instances using same client_id. | SHOULD | Section 3.2.1 |
| R32 | software_id SHOULD remain same for all instances and across updates. | SHOULD | Section 2 |
| R33 | software_version SHOULD change on any update. | SHOULD | Section 2 |
| R34 | If duplication suspected, authorization server SHOULD treat new registration as suspect. | SHOULD | Section 5 |
| R35 | Server SHOULD NOT issue same client secret to multiple instances. | SHOULD | Section 5 |
| R36 | Authorization server MAY reject or replace requested metadata values. | MAY | Section 2, Section 3.2.1 |
| R37 | Authorization server MAY expire registrations for public clients. | MAY | Section 5 |
| R38 | Authorization server MAY require separate registrations for different grant types. | MAY | Section 5 |
| R39 | Server MAY disallow registration for both authorization_code and implicit simultaneously. | MAY | Section 5 |
| R40 | Authorization server MAY accept software statement as client identifier without prior registration. | MAY | Section 2.3 |
| R41 | Server MAY ignore software statement if it does not support feature. | MAY | Section 3.1.1 |

**Note**: Informative annexes (Appendix A) are condensed. Full examples and non-normative text are omitted per compression rules.