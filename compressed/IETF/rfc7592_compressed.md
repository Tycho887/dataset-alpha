# RFC 7592: OAuth 2.0 Dynamic Client Registration Management Protocol
**Source**: IETF | **Version**: Experimental | **Date**: July 2015 | **Type**: Experimental
**Original**: http://www.rfc-editor.org/info/rfc7592

## Scope (Summary)
Defines methods for management of OAuth 2.0 dynamic client registrations (read, update, delete) via a Client Configuration Endpoint, extending [RFC7591]. Not all authorization servers supporting dynamic registration will support these management methods.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750
- [RFC6819] Lodderstedt, T., Ed., et al., "OAuth 2.0 Threat Model and Security Considerations", RFC 6819
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159
- [RFC7231] Fielding, R. and J. Reschke, Ed., "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content", RFC 7231
- [RFC7591] Richer, J., Ed., et al., "OAuth 2.0 Dynamic Client Registration Protocol", RFC 7591
- [BCP195] Sheffer, Y., et al., "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525

## Definitions and Abbreviations
- **Client Configuration Endpoint**: OAuth 2.0 endpoint through which registration information for a registered client can be managed. URL is returned in the client information response.
- **Registration Access Token**: OAuth 2.0 Bearer Token issued by the authorization server via the client registration endpoint, used to authenticate the caller when accessing the client's registration information at the Client Configuration Endpoint. Associated with a particular registered client.
- **Initial Access Token** (informative): Optionally used at the registration endpoint; out of scope for this specification.
- **Client Credentials** (e.g., client_secret): Used at the token endpoint; can be rotated via read/update operations.
- For other OAuth 2.0 terms, see [RFC6749].

## 1. Introduction
Extends [RFC7591] with methods to query, update, and delete client registration state. Not all authorization servers will support these methods. (Experimental RFC intended to gather feedback.)

### 1.1. Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119]. Unless otherwise noted, all protocol parameter names and values are case sensitive.

### 1.2. Terminology
(See Definitions section above.)

### 1.3. Protocol Flow
Extends the flow in [RFC7591] with additional steps (E)-(H) for management:
- (A) Optional initial access token.
- (B) Optional software statement.
- (C) Registration request.
- (D) Registration response includes: client metadata, client_id, client_secret (if applicable), `registration_client_uri`, and `registration_access_token`.
- (E) Client optionally calls Client Configuration Endpoint (read/update) using registration access token.
- (F) Server responds with current configuration, potentially including new registration access token and/or client secret.
- (G) Client optionally calls delete.
- (H) Server confirms deletion.

## 2. Client Configuration Endpoint
Protected resource for viewing, updating, and deleting client registration. Location conveyed via `registration_client_uri`.  
- **Client MUST** use its registration access token as Bearer Token [RFC6750] in all calls.  
- **Endpoint MUST** be protected by transport-layer security (see Section 5).  
- Operations are switched via HTTP methods.  
- If server does not support a method, **MUST** respond with appropriate error.

### 2.1. Client Read Request
- **Method**: HTTP GET to Client Configuration Endpoint.
- **Authentication**: Bearer token (registration access token).
- **Successful response**: HTTP 200 OK, `application/json`, payload per Section 3.  
- The response MAY include a new `client_secret` and/or `registration_access_token`.  
  - If new credentials issued, **client MUST immediately discard** previous ones.  
  - `client_id` **MUST NOT** change.
- **Error conditions**:  
  - Invalid registration token → respond per [RFC6750].  
  - Client does not exist → HTTP 401 Unauthorized; registration token SHOULD be revoked.  
  - Client not allowed to read → HTTP 403 Forbidden.

### 2.2. Client Update Request
- **Method**: HTTP PUT to Client Configuration Endpoint, `Content-Type: application/json`.
- **Body**: JSON object with all client metadata fields (as returned from previous registration/read/update).  
  - **MUST NOT** include `registration_access_token`, `registration_client_uri`, `client_secret_expires_at`, `client_id_issued_at`.  
  - **MUST include** `client_id` (same as current).  
  - If `client_secret` included, it **MUST** match current secret; server **MUST NOT** allow overwriting with chosen value.  
  - Omitted fields treated as null/empty → client requests deletion; server MAY ignore null/empty values.
- **Response**: HTTP 200 OK with payload per Section 3, possibly with new credentials (client discards previous).  
  - `client_id` **MUST NOT** change.
- **Server actions**: MAY replace invalid values with defaults; **MUST** return such fields in response.
- **Error conditions**:  
  - Invalid registration token → respond per [RFC6750].  
  - Client does not exist → HTTP 401 Unauthorized; token SHOULD be revoked.  
  - Not allowed to update → HTTP 403 Forbidden.  
  - Invalid metadata field (no default) → error per [RFC7591].

### 2.3. Client Delete Request
- **Method**: HTTP DELETE to Client Configuration Endpoint.
- **Authentication**: Bearer token (registration access token).
- **Successful response**: HTTP 204 No Content.  
  - Invalidation: `client_id`, `client_secret`, `registration_access_token` become invalid.  
  - Server SHOULD immediately invalidate all associated grants, access tokens, refresh tokens.
- **Error conditions**:  
  - Server does not support delete → HTTP 405 Not Supported.  
  - Invalid registration token → respond per [RFC6750].  
  - Client does not exist → HTTP 401 Unauthorized; token SHOULD be revoked.  
  - Not allowed to delete → HTTP 403 Forbidden.

## 3. Client Information Response
Extends [RFC7591] response with two additional REQUIRED members:
- **registration_client_uri**: Fully qualified URL of the client configuration endpoint for this client.
- **registration_access_token**: Access token for subsequent operations at the client configuration endpoint.
The response **MUST** include all registered metadata (including server-provisioned fields). Server MAY reject or replace submitted values. Response is `application/json`.

## 4. IANA Considerations
Registers two metadata names in the "OAuth Dynamic Client Registration Metadata" registry (per [RFC7591]):

| Name | Description | Change Controller | Specification |
|------|-------------|------------------|---------------|
| `registration_access_token` | OAuth 2.0 Bearer Token used to access the client configuration endpoint | IESG | RFC 7592 |
| `registration_client_uri` | Fully qualified URI of the client registration endpoint | IESG | RFC 7592 |

## 5. Security Considerations
- **Registration access token**: SHOULD NOT expire while client is active; MAY be rotated on read/update.  
  - **MUST** be protected as Bearer Token [RFC6750].  
  - **MUST** contain sufficient entropy to prevent guessing [RFC6750, RFC6819].
- **Transport security**: Authorization server **MUST** require TLS for client configuration endpoint; **MUST** support TLS 1.2 [RFC5246]; client **MUST** perform server certificate check per [RFC6125].
- **Deprovisioning**: If client is deprovisioned, any outstanding registration access token **MUST** be invalidated; all subsequent requests **MUST** be treated as invalid token (HTTP 401).

## 6. Privacy Considerations
No additional considerations beyond those in [RFC7591].

## 7. Normative References
(See references listed above in Normative References section.)

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Client MUST use registration access token as Bearer Token in all calls to Client Configuration Endpoint. | shall | Section 2 |
| R2 | Client Configuration Endpoint MUST be protected by transport-layer security. | shall | Section 2, 5 |
| R3 | If a method is not supported, server MUST respond with appropriate error code. | shall | Section 2 |
| R4 | On read or update, if new client_secret or registration_access_token is issued, client MUST immediately discard previous ones. | shall | Sections 2.1, 2.2 |
| R5 | Value of client_id MUST NOT change from initial registration. | shall | Sections 2.1, 2.2 |
| R6 | On read, if client does not exist, server MUST respond HTTP 401 and SHOULD revoke registration access token. | shall/should | Section 2.1 |
| R7 | On read, if client not allowed, server MUST return HTTP 403. | shall | Section 2.1 |
| R8 | On update, request MUST include all client metadata fields (as returned previously). | shall | Section 2.2 |
| R9 | On update, request MUST NOT include registration_access_token, registration_client_uri, client_secret_expires_at, client_id_issued_at. | shall | Section 2.2 |
| R10 | On update, client MUST include client_id and it MUST be the same as issued. | shall | Section 2.2 |
| R11 | On update, if client_secret included, it MUST match currently issued client secret. | shall | Section 2.2 |
| R12 | On update, server MUST NOT allow client to overwrite its client secret with chosen value. | shall | Section 2.2 |
| R13 | On update, omitted fields treated as null/empty; server MAY ignore null/empty values. | may | Section 2.2 |
| R14 | On update, server MAY replace invalid values with defaults and MUST return them in response. | shall | Section 2.2 |
| R15 | On delete, successful response is HTTP 204 No Content. | shall | Section 2.3 |
| R16 | On delete, server SHOULD immediately invalidate associated grants and tokens. | should | Section 2.3 |
| R17 | On delete, if server does not support method, respond HTTP 405. | shall | Section 2.3 |
| R18 | On delete, if client does not exist, respond HTTP 401 and SHOULD revoke token. | shall/should | Section 2.3 |
| R19 | On delete, if not allowed, respond HTTP 403. | shall | Section 2.3 |
| R20 | Client information response MUST include registration_client_uri and registration_access_token. | shall | Section 3 |
| R21 | Authorization server MUST return all registered metadata in client information response. | shall | Section 3 |
| R22 | Registration access token SHOULD NOT expire while client is active. | should | Section 5 |
| R23 | Registration access token MUST contain sufficient entropy. | shall | Section 5 |
| R24 | If client deprovisioned, any outstanding registration access token MUST be invalidated. | shall | Section 5 |
| R25 | All subsequent requests after deprovisioning MUST be treated as invalid token (HTTP 401). | shall | Section 5 |
| R26 | Authorization server MUST require TLS for client configuration endpoint; MUST support TLS 1.2. | shall | Section 5 |
| R27 | Client MUST perform TLS server certificate check per RFC 6125. | shall | Section 5 |

## Informative Annexes (Condensed)
- **Appendix A: Registration Tokens and Client Credentials**: Describes three credential classes: initial access token (registration endpoint), registration access token (client configuration endpoint), and client credentials (token endpoint). Each has distinct properties and targets. Registration access tokens should not be shared between client instances. Credential rotation (new tokens/secrets) may be issued by the server on read/update; the old ones are discarded. The server decides rotation frequency.
- **Appendix B: Forming the Client Configuration Endpoint URL**: The server MUST provide the fully qualified URL in `registration_client_uri`; the client MUST NOT construct it. Common patterns include path or query parameters incorporating the client_id. The server must match the token to the client.