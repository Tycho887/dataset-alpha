# RFC 9396: OAuth 2.0 Rich Authorization Requests
**Source**: IETF | **Version**: Standards Track | **Date**: May 2023 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9396

## Scope
Defines the `authorization_details` parameter to carry fine-grained authorization data (JSON objects) in OAuth 2.0 messages, enabling clients to specify structured, type-specific permissions (e.g., payment amount, resource paths) beyond the `scope` parameter.

## Normative References
- [RFC2119] – Key words for requirement levels
- [RFC7519] – JSON Web Token (JWT)
- [RFC7662] – OAuth 2.0 Token Introspection
- [RFC8174] – Ambiguity of uppercase vs lowercase in RFC 2119 key words
- [RFC8414] – OAuth 2.0 Authorization Server Metadata
- [RFC8628] – OAuth 2.0 Device Authorization Grant
- [RFC8707] – Resource Indicators for OAuth 2.0

## Definitions and Abbreviations
- **authorization_details**: JSON array of objects; each object contains data specifying authorization requirements for a resource type.
- **type**: REQUIRED string identifier for the authorization details type.
- **locations, actions, datatypes, identifier, privileges**: Common data fields (defined in Section 2.2).
- **AS**: Authorization Server
- **RS**: Resource Server
- **authorization_endpoint, token_endpoint, etc.**: As defined in [RFC6749].

## Section 2: Request Parameter "authorization_details"
### 2.1 Authorization Details Types
- **type**: REQUIRED string. Determines allowable object fields. The AS controls interpretation.
- RECOMMENDED to use collision-resistant namespaces (e.g., URIs) for cross-deployment APIs.
- RECOMMENDED to choose type values easily copied (ASCII, machine-readable listing).

### 2.2 Common Data Fields
- **locations**: array of strings (typically URIs) for RS location.
- **actions**: array of strings for actions to be taken.
- **datatypes**: array of strings for kinds of data.
- **identifier**: string identifying a specific resource.
- **privileges**: array of strings for levels of privilege.
- Permissions are the product of all listed values (e.g., all actions × all locations × all datatypes).
- Multiple objects allow finer control (granular combinations).
- API MAY define its own extension fields per type.

## Section 3: Authorization Request
- `authorization_details` can be used in: authorization requests [RFC6749], device authorization [RFC8628], backchannel authentication [OID-CIBA].
- Implementers MAY use pushed authorization requests (PAR) [RFC9126] for security and reliability.
- Parameter encoding: `application/x-www-form-urlencoded` serialized JSON.
- AS asks for user consent; user may grant a subset.

### 3.1 Relationship to "scope"
- `authorization_details` and `scope` MAY appear together for independent requirements.
- RECOMMENDED that a given API uses only one form.
- AS MUST process both sets together (details are API-specific).
- AS MUST present merged set to user for consent.
- Tokens are associated with respective `authorization_details` (and `scope` if applicable).

### 3.2 Relationship to "resource"
- `resource` parameter (RFC 8707) does not affect processing of `authorization_details`.

## Section 4: Authorization Response
- No extensions defined.

## Section 5: Authorization Error Response
- AS MUST refuse processing of any object in `authorization_details` that:
  - contains unknown type value,
  - is of known type but unknown fields,
  - fields of wrong type,
  - fields with invalid values,
  - missing required fields.
- Error code: `invalid_authorization_details`.

## Section 6: Token Request
- Client can use `authorization_details` to specify details for an access token.
- AS checks grant (authorization_code, refresh_token, etc.) or client policy (client_credentials) for allowed issuance.
- AS refuses with `invalid_authorization_details` if not allowed.

### 6.1 Comparing Authorization Details
- No standardized comparison mechanism; AS should not rely on simple object comparison.
- AS determines if new request is "within" previous authorization (e.g., reduced privileges, subset of locations).
- Comparison is type-specific (e.g., additive rights, subsuming actions, privileges).

## Section 7: Token Response
- AS MUST include `authorization_details` as granted and assigned to the access token.
- Determined by token request parameter; if absent, AS decides.
- AS MAY omit values.

### 7.1 Enriched Authorization Details
- Authorization details MAY differ from client request (e.g., user adds accounts, AS adds identifiers).
- Enrichment is defined per authorization details type.

## Section 8: Token Error Response
- MUST conform to error rules in Section 5.

## Section 9: Resource Servers
- AS MUST make authorization data available to RS: via JWT access token or introspection response.

### 9.1 JWT-Based Access Tokens
- RECOMMENDED that AS adds `authorization_details` as a top-level JWT claim, filtered to audience.

### 9.2 Token Introspection
- If included, `authorization_details` MUST be a top-level member of introspection response.
- MUST contain same structure as Section 2, potentially filtered/extended for RS.

## Section 10: Metadata
- AS advertises supported types via metadata parameter `authorization_details_types_supported` (JSON array) [RFC8414].
- Client may indicate intended types via registration metadata `authorization_details_types`.

## Section 11: Implementation Considerations
- Steps: define types, publish metadata, UI consent, enrichment, token content, RS processing, client entitlement.
- Minimal support: metadata, accept parameter, store consent, default inclusion in tokens.
- Customization: presentation, modification, merging – e.g., via extension modules.
- Machine‑readable schemas (e.g., JSON Schema) may be used for validation (type value as identifier, no dereferencing assumed).
- Large requests: use `request_uri` [RFC9101] + PAR [RFC9126].

## Section 12: Security Considerations
- Clients MUST protect integrity of `authorization_details` against tampering and swapping (using signed request objects [RFC9101] or request_uri + PAR [RFC9126]).
- All string comparisons done as per [RFC8259]; no normalization.
- `locations` field enables audience restriction, preventing unintended cross‑RS authorizations.
- AS MUST sanitize input to prevent injection.
- Also apply security considerations of [RFC6749], [RFC7662], [RFC8414].

## Section 13: Privacy Considerations
- Sensitive personal data in `authorization_details` must be prevented from leaking (referrer headers, etc.).
- Use encrypted request objects or end‑to‑end encryption via PAR.
- Attack: attacker may use AS to display decrypted data – implement countermeasures (e.g., showing portions, validating user context).
- Share on need‑to‑know basis with parties.

## Section 14: IANA Considerations
- Registered: OAuth parameter `authorization_details` (authorization request, token request, token response).
- Registered: JWT claim `authorization_details`.
- Registered: Token Introspection Response member `authorization_details`.
- Registered: AS metadata `authorization_details_types_supported`.
- Registered: Client metadata `authorization_details_types`.
- Registered: Error `invalid_authorization_details`.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | The `type` field in `authorization_details` is REQUIRED. | shall | Section 2 |
| R2 | AS MUST refuse processing of invalid `authorization_details` (unknown type, malformed). | shall | Section 5 |
| R3 | When combining `scope` and `authorization_details`, AS MUST present merged set to user. | shall | Section 3.1 |
| R4 | Token response MUST include `authorization_details` as granted. | shall | Section 7 |
| R5 | AS MUST make authorization data available to RS (JWT or introspection). | shall | Section 9 |
| R6 | If introspection includes `authorization_details`, it MUST be a top-level member. | shall | Section 9.2 |
| R7 | Clients MUST protect integrity of `authorization_details` against tampering. | must | Section 12 |
| R8 | AS MUST sanitize input to prevent injection. | shall | Section 12 |

## Informative Annexes (Condensed)
- **A.1 OpenID Connect**: Shows how authorization details could encapsulate OIDC claims, claim sets, max_age, acr_values alongside existing OIDC flows (not normative).
- **A.2 Remote Electronic Signing**: Example based on ETSI TS 119 432 / CSC API – includes credentialID, documentDigests, hashAlgorithmOID; AS asks consent for signing specific documents.
- **A.3 Access to Tax Data**: Example with fields `periods`, `duration_of_access`, `tax_payer_id` for accessing tax declarations.
- **A.4 eHealth**: Two examples: first with requesting_entity (practitioner, organization); second adds patient_identifier, reason_for_request, profession; AS authenticates requester and enforces policy.