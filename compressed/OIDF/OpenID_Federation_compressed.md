# OpenID Federation 1.0
**Source**: OpenID Foundation | **Version**: Final | **Date**: 17 February 2026 | **Type**: Standards Track
**Original**: [OpenID Federation 1.0 specification](https://openid.net/specs/openid-federation-1_0.html)

## Scope (Summary)
This specification defines basic components to build multilateral federations using a trusted third party (Trust Anchor) and establishes how entities in a federation can trust each other's identity and metadata. It provides mechanisms for entity statements, trust chains, metadata policies, trust marks, and federation endpoints, applicable to OpenID Connect and OAuth 2.0, and extensible to other protocols.

## Normative References
- [OpenID.Core] Sakimura, N., et al., "OpenID Connect Core 1.0", 15 December 2023
- [OpenID.Discovery] Sakimura, N., et al., "OpenID Connect Discovery 1.0", 15 December 2023
- [OpenID.Registration] Sakimura, N., et al., "OpenID Connect Dynamic Client Registration 1.0", 15 December 2023
- [OpenID.RP.Choices] Jones, M.B., et al., "OpenID Connect Relying Party Metadata Choices 1.0", 8 January 2026
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119
- [RFC4732] Handley, M., et al., "Internet Denial-of-Service Considerations", RFC 4732
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", RFC 5280
- [RFC5646] Phillips, A., et al., "Tags for Identifying Languages", BCP 47, RFC 5646
- [RFC6749] Hardt, D., "The OAuth 2.0 Authorization Framework", RFC 6749
- [RFC7515] Jones, M., et al., "JSON Web Signature (JWS)", RFC 7515
- [RFC7516] Jones, M., et al., "JSON Web Encryption (JWE)", RFC 7516
- [RFC7517] Jones, M., "JSON Web Key (JWK)", RFC 7517
- [RFC7519] Jones, M., et al., "JSON Web Token (JWT)", RFC 7519
- [RFC7591] Richer, J., et al., "OAuth 2.0 Dynamic Client Registration Protocol", RFC 7591
- [RFC7638] Jones, M., et al., "JSON Web Key (JWK) Thumbprint", RFC 7638
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174
- [RFC8259] Bray, T., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259
- [RFC8414] Jones, M., et al., "OAuth 2.0 Authorization Server Metadata", RFC 8414
- [RFC8705] Campbell, B., et al., "OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens", RFC 8705
- [RFC9101] Sakimura, N., et al., "The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)", RFC 9101
- [RFC9126] Lodderstedt, T., et al., "OAuth 2.0 Pushed Authorization Requests", RFC 9126
- [RFC9728] Jones, M.B., et al., "OAuth 2.0 Protected Resource Metadata", RFC 9728
- [UNICODE] The Unicode Consortium, "The Unicode Standard"
- [USA15] Whistler, K., "Unicode Normalization Forms", Unicode Standard Annex 15

## Definitions and Abbreviations
- **Entity**: Something that has a separate and distinct existence and can be identified in a context.
- **Entity Identifier**: A globally unique string identifier bound to one Entity, specified as an `https` URL with host component, optionally port and path; MUST NOT contain query or fragment. Profiles may define other types.
- **Trust Anchor**: An Entity that represents a trusted third party.
- **Federation Entity**: An Entity for which it is possible to construct a Trust Chain from the Entity to a Trust Anchor.
- **Entity Statement**: A signed JWT containing information for an Entity to participate in federation(s), including metadata and policies.
- **Entity Configuration**: An Entity Statement issued by an Entity about itself, containing signing keys and authority hints.
- **Subordinate Statement**: An Entity Statement issued by a Superior Entity about an Immediate Subordinate.
- **Entity Type**: A role and function that an Entity plays within a federation. An Entity MUST be at least one type.
- **Entity Type Identifier**: String identifier for an Entity Type.
- **Federation Operator**: An organization authoritative for a federation, administering Trust Anchors.
- **Intermediate Entity**: An Entity that issues Entity Statements in a Trust Chain between Trust Anchor and subject.
- **Leaf Entity**: An Entity with no Subordinate Entities, typically playing a protocol role.
- **Subordinate Entity**: An Entity below a Superior in the trust hierarchy, possibly with Intermediates between.
- **Superior Entity**: An Entity above one or more Entities in the trust hierarchy.
- **Immediate Subordinate Entity**: An Entity directly below a Superior with no Intermediates.
- **Immediate Superior Entity**: An Entity directly above one or more Subordinates.
- **Federation Entity Discovery**: Process starting from Entity Identifier, collecting Entity Statements until Trust Anchor reached, then constructing and verifying Trust Chain.
- **Trust Chain**: Sequence of Entity Statements from an Entity Configuration to a Trust Anchor.
- **Trust Mark**: Statement of conformance to a set of trust/interoperability requirements determined by an accreditation authority.
- **Trust Mark Issuer**: Federation Entity that issues Trust Marks.
- **Trust Mark Owner**: Entity that owns a Trust Mark type identifier.
- **Federation Entity Keys**: Keys used for cryptographic signatures required by trust mechanisms; published in Entity Configuration.
- **Resolved Metadata**: Metadata resulting from applying metadata policy in the Trust Chain to the subject's Entity Configuration metadata.

## 1. Introduction
This specification describes how two Entities can establish trust via a trusted third party (Trust Anchor). It provides basic technical trust infrastructure for dynamic distributed trust networks (federations). The specification only concerns itself with how Entities get to know about each other; an organization MAY be represented by more than one Entity, and an Entity MAY belong to more than one federation. Determining common Trust Anchor is basis for trust.

### 1.1. Requirements Notation and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as per BCP 14 [RFC2119] [RFC8174] when in all capitals. All uses of JWS and JWE data structures utilize Compact Serialization only.

### 1.2. Terminology
Referenced terms from JWT, OpenID Connect Core, OAuth 2.0. Additional terms defined in Definitions section above.

## 2. Overall Architecture
Basic component is Entity Statement (signed JWT). A set of Entity Statements forms a path from an Entity to a Trust Anchor. Entity Configuration contains `authority_hints` to Immediate Superiors. Trust Chain is verified via signatures. Metadata policy is applied to derive Resolved Metadata. This specification deals with trust operations, not protocol operations beyond metadata derivation.

### 2.1. Cryptographic Trust Mechanism
Objects are secured as signed JWTs using public key cryptography. Public keys are distributed through the objects themselves. Does not rely on Web PKI/TLS certificates; uses self-managed JWKs.

## 3. Entity Statement
Entity Statement is a signed JWT. Entity Configuration (self-signed) or Subordinate Statement (issued by superior). MUST use `typ: entity-statement+jwt`. Signed with Federation Entity Keys. MUST include `kid` header parameter.

### 3.1. Entity Statement Claims
#### 3.1.1. Claims in both Entity Configurations and Subordinate Statements
- `iss` (REQUIRED): Entity Identifier of issuer.
- `sub` (REQUIRED): Entity Identifier of subject.
- `iat` (REQUIRED): Number, time issued.
- `exp` (REQUIRED): Number, expiration time.
- `jwks` (REQUIRED): JWK Set of subject's Federation Entity signing keys. OPTIONAL in Explicit Registration Response.
- `metadata` (OPTIONAL): JSON object with Entity Type Identifiers and metadata parameters.
- `crit` (OPTIONAL): Array of critical Claims that MUST be understood.

#### 3.1.2. Claims in Entity Configurations only
- `authority_hints` (OPTIONAL): Array of Entity Identifiers of Immediate Superiors. REQUIRED for Entities with Superiors; MUST NOT be empty array; MUST NOT be present for Trust Anchors with no Superiors.
- `trust_anchor_hints` (OPTIONAL): Array of Trust Anchor Entity Identifiers.
- `trust_marks` (OPTIONAL): Array of Trust Mark objects.
- `trust_mark_issuers` (OPTIONAL): For Trust Anchors; maps Trust Mark type identifiers to arrays of trusted issuers.
- `trust_mark_owners` (OPTIONAL): For Trust Anchors; specifies owners for Trust Mark types.

#### 3.1.3. Claims in Subordinate Statements only
- `constraints` (OPTIONAL): Trust Chain constraints.
- `metadata_policy` (OPTIONAL): Metadata policy for subject and its Subordinates.
- `metadata_policy_crit` (OPTIONAL): Array of critical policy operators.
- `source_endpoint` (OPTIONAL): Fetch endpoint URL for optimized refresh.

#### 3.1.4-3.1.5. Claims for Explicit Registration Requests/Responses
- `aud` (OPTIONAL): In request: Entity Identifier of OP. In response: Entity Identifier of RP.
- `trust_anchor` (OPTIONAL, response): Entity Identifier of Trust Anchor selected.

### 3.2. Entity Statement Validation
Detailed validation steps (20+ checks) MUST be performed. Key rules: signed JWT, `typ` value, `alg` not `none`, `iss` and `sub` valid, `iat` and `exp` times, `jwks` present, signature verification, `crit` processing, syntactic checks for each claim.

### 3.3. Entity Statement Example
Non-normative example given.

## 4. Trust Chain
A Trust Chain begins with Entity Configuration of the subject (typically Leaf), includes Subordinate Statements up to Trust Anchor's Entity Configuration. Chain is verified by checking `iss`/`sub` matches and signature binding.

### 4.1. Beginning and Ending Trust Chains
Starts with Entity Configuration of subject; ends with Trust Anchor's Entity Configuration. Trust Anchor may have Superiors in hierarchical federations.

### 4.2. Trust Chain Example
Diagram and explanation of relationships.

### 4.3. Trust Chain Header Parameter
JWS header parameter `trust_chain` containing the array of Entity Statements. OPTIONAL; Entity Configurations and Subordinate Statements MUST NOT include it.

### 4.4. Peer Trust Chain Header Parameter
JWS header parameter `peer_trust_chain` containing Trust Chain from peer to Trust Anchor. OPTIONAL.

## 5. Metadata
Entity metadata in `metadata` Claim of Entity Statement. Each member name is Entity Type Identifier. JSON values other than `null` allowed.

### 5.1. Entity Type Identifiers
#### 5.1.1. Federation Entity
- `federation_entity` Entity Type.
- Properties: `federation_fetch_endpoint`, `federation_list_endpoint`, `federation_resolve_endpoint`, `federation_trust_mark_status_endpoint`, `federation_trust_mark_list_endpoint`, `federation_trust_mark_endpoint`, `federation_historical_keys_endpoint`, `endpoint_auth_signing_alg_values_supported`. Must use `https` scheme.

#### 5.1.2. OpenID Connect Relying Party
- `openid_relying_party`. Uses parameters from OpenID Connect Dynamic Client Registration, plus `client_registration_types`.

#### 5.1.3. OpenID Connect OpenID Provider
- `openid_provider`. Uses parameters from OpenID Connect Discovery, plus `client_registration_types_supported`, `federation_registration_endpoint`. `issuer` MUST match Entity Identifier.

#### 5.1.4. OAuth Authorization Server
- `oauth_authorization_server`. Parameters from RFC 8414.

#### 5.1.5. OAuth Client
- `oauth_client`. Parameters from RFC 7591.

#### 5.1.6. OAuth Protected Resource
- `oauth_resource`. Parameters from Section 5.2 and optionally RFC 9728.

### 5.2. Common Metadata Parameters
#### 5.2.1. Parameters for JWK Sets in Entity Metadata
- `signed_jwks_uri`: URL referencing signed JWT with JWK Set. Signed with Federation Entity Key. MUST have `typ: jwk-set+jwt`. Claims: `keys`, `iss`, `sub`, `iat`, `exp`.
- `jwks_uri`: URL referencing JWK Set document.
- `jwks`: JWK Set by value.
- Usage: RECOMMENDED to use only one representation.

#### 5.2.2. Informational Metadata Parameters
- `organization_name`, `display_name`, `description`, `keywords`, `contacts`, `logo_uri`, `policy_uri`, `information_uri`, `organization_uri`. OPTIONAL.

## 6. Federation Policy
### 6.1. Metadata Policy
Trust Anchors and Intermediates MAY define policies for Subordinate metadata. Policies are hierarchical, equal opportunity, specific to Entity Types and metadata parameters. Operators: value check/modification.

#### 6.1.1. Principles
Hierarchy, equal opportunity, specificity, integral enforcement, determinism.

#### 6.1.2. Structure
`metadata_policy` Claim: three levels: Entity Type → metadata parameter → operators. No duplicate names.

#### 6.1.3. Operators
Standard operators: `value`, `add`, `default`, `one_of`, `subset_of`, `superset_of`, `essential`. Each has defined action, required value types, combination rules, order of application, and merge behavior.

#### 6.1.4. Enforcement
Resolution process: iterate Subordinate Statements from most Superior to Immediate Superior, merge policies. Application: first apply `metadata` from Immediate Superior, then apply resolved policy. Policy errors invalidate Trust Chain.

#### 6.1.5. Metadata Policy Example
Non-normative example provided.

### 6.2. Constraints
- `max_path_length`: Integer, maximum number of Intermediates.
- `naming_constraints`: JSON object with `permitted` and `excluded` arrays (domain name syntax per RFC 5280).
- `allowed_entity_types`: Array of Entity Type Identifiers; `federation_entity` always allowed.
- Constraints applied independently; failure invalidates Trust Chain.

## 7. Trust Marks
Trust Marks are signed JWTs attesting conformance to accreditation criteria. Issued by Trust Mark Issuers. Trust Anchor publishes `trust_mark_issuers` Claim. Trust Marks MUST have `typ: trust-mark+jwt`, signed with Federation Entity Key.

### 7.1. Trust Mark Claims
- `iss`, `sub`, `trust_mark_type`, `iat` (REQUIRED); `logo_uri`, `exp`, `ref`, `delegation` (OPTIONAL).

### 7.2. Trust Mark Delegation
When Trust Mark Issuer is not owner, delegation JWT (`typ: trust-mark-delegation+jwt`) is included in `delegation` Claim. Trust Anchor publishes `trust_mark_owners`.

### 7.3. Validating a Trust Mark
Validation steps: signed JWT, `typ`, algorithm, `sub` matches entity, time checks, signature, delegation validation if present. May use status endpoint.

### 7.4-7.5. Examples
Non-normative examples provided.

## 8. Federation Endpoints
Endpoints are published in `federation_entity` metadata.

### 8.1. Fetching a Subordinate Statement (Fetch Endpoint)
- GET with `sub` parameter, or POST with client authentication.
- Response: `application/entity-statement+jwt`, status 200.

### 8.2. Subordinate Listing (List Endpoint)
- GET with optional `entity_type`, `trust_marked`, `trust_mark_type`, `intermediate` parameters.
- Response: JSON array of Entity Identifiers.

### 8.3. Resolve Entity (Resolve Endpoint)
- GET with `sub`, `trust_anchor`, optional `entity_type`.
- Response: `application/resolve-response+jwt`, signed JWT with `metadata`, `trust_chain`, optional `trust_marks`.

### 8.4. Trust Mark Status
- POST with `trust_mark` parameter.
- Response: `application/trust-mark-status-response+jwt`, with `status` (active, expired, revoked, invalid).

### 8.5. Trust Marked Entities Listing
- GET with `trust_mark_type`, optional `sub`.
- Response: JSON array of Entity Identifiers.

### 8.6. Trust Mark Endpoint
- GET with `trust_mark_type`, `sub`.
- Response: `application/trust-mark+jwt` (the Trust Mark).

### 8.7. Federation Historical Keys Endpoint
- GET returns `application/jwk-set+jwt` signed JWT with historical keys. Each key includes `iat`, `exp`, optional `revoked` object with `revoked_at` and `reason`.

### 8.8. Client Authentication at Federation Endpoints
Default no authentication. Optionally use `private_key_jwt` signed with Federation Entity Key. Metadata parameters for supported methods per endpoint.

### 8.9. Error Responses
JSON with `error`, `error_description`. Standard and custom error codes defined.

## 9. Obtaining Federation Entity Configuration Information
Entity Configuration published at `/.well-known/openid-federation` relative to Entity Identifier (https scheme). Mandatory for Trust Anchors and Intermediates; SHOULD for Leaf Entities. Response type `application/entity-statement+jwt`.

## 10. Resolving the Trust Chain and Metadata
Entity must fetch Entity Statements to build a Trust Chain to a Trust Anchor. Validation steps per Section 4. Must apply metadata policy and constraints. Multiple Trust Chains possible; choose one (e.g., shortest). Expiration time is min of all `exp`. Trust Chain refresh on expiry. May delegate to Resolve endpoint.

## 11. Updating Metadata, Key Rollover, and Revocation
Federation participants MUST support refreshing Trust Chains. Key rollover for Trust Anchor: add new keys, sign with old until propagated, then switch. Redundant retrieval of Trust Anchor keys recommended. Revocation not defined in this spec; federations may define own.

## 12. OpenID Connect Client Registration
Two methods: Automatic (no prior registration) and Explicit (prior registration). Both use Trust Chains. Applicable to OAuth 2.0 as well.

### 12.1. Automatic Registration
RP uses Entity Identifier as Client ID. OP fetches Entity Configuration. Authentication Request MUST use signed Request Object or Pushed Authorization with proof of key possession. OP resolves Trust Chain and metadata for RP.

### 12.2. Explicit Registration
RP sends Entity Configuration or Trust Chain to OP's `federation_registration_endpoint`. OP validates, creates registration, returns signed registration Entity Statement with `trust_anchor`, `client_id`, etc.

### 12.3-12.5. Additional details on validity, differences, rationale.

## 13. General-Purpose JWT Claims
- `jwks`: JWK Set.
- `metadata`: JSON object.
- `constraints`: JSON object.
- `crit`: Array of critical Claims.
- `ref`: URI reference.
- `delegation`: StringOrURI for delegation.
- `logo_uri`: URI for logo.

## 14. Claims Languages and Scripts
Human-readable values MAY be represented in multiple languages/scripts using BCP47 language tags delimited by `#`.

## 15. Media Types
Defined: `application/entity-statement+jwt`, `application/trust-mark+jwt`, `application/resolve-response+jwt`, `application/trust-chain+json`, `application/trust-mark-delegation+jwt`, `application/jwk-set+jwt`, `application/trust-mark-status-response+jwt`, `application/explicit-registration-response+jwt`.

## 16. String Operations
Comparisons must be performed as Unicode code point equality after JSON escaping removal; no normalization.

## 17. Implementation Considerations
- Topologies: multiple trust paths possible; trees recommended to avoid ambiguity. Loops forbidden in Trust Chains.
- Discovery vs Trust Chain Resolution patterns: Bottom-up, Top-down, Single Point of Trust Resolution.
- Trust Anchors should also be Resolvers for simplicity.
- One Entity, One Service recommended for sharing between federations.
- Trust Mark validation: syntax, specific mark, policy decisions.

## 18. Security Considerations
DoS prevention: limit `authority_hints` count, require Trust Chains in requests, use Trust Marks as filter, restrict resolve endpoint to authenticated or cached responses. Unsigned error messages allow DoS.

## 19. Privacy Considerations
Entity Statements should contain only essential info. Trust Mark Status and Fetch endpoints may enable tracking; mitigation with short-lived Trust Marks, static Trust Chains.

## 20. IANA Considerations
Multiple registrations for metadata, parameters, errors, JWS header parameters, JWK parameters, JWT claims, well-known URI, and media types. Full details in original.

## 21. References
Normative and Informative references as listed.

## Informative Annexes (Condensed)
- **Appendix A (Examples)**: Detailed example of setting up a federation, discovery process for an OP, and both Automatic and Explicit client registration flows. Shows step-by-step Entity Statement retrieval and metadata policy application.
- **Appendix B (Notices)**: Copyright and license information from OpenID Foundation. Disclaimer of warranties.

## Requirements Summary (Selected Key Requirements)
| ID | Requirement | Type | Reference |
|----|------------|------|-----------|
| R1 | Entity Statements MUST be explicitly typed with `typ: entity-statement+jwt` | MUST | Section 3 |
| R2 | Entity Statements without `typ` header or with different value MUST be rejected | MUST | Section 3 |
| R3 | `iss`, `sub`, `iat`, `exp`, `jwks` Claims MUST be present in Entity Statements (except `jwks` OPTIONAL in Explicit Registration Response) | MUST | Section 3.1.1 |
| R4 | `authority_hints` Claim is REQUIRED in Entity Configurations of Entities with Superiors; MUST NOT be empty array | MUST | Section 3.1.2 |
| R5 | `authority_hints` MUST NOT be present in Entity Configurations of Trust Anchors with no Superiors | MUST | Section 3.1.2 |
| R6 | Entity Statements MUST be validated according to Section 3.2 | MUST | Section 3.2 |
| R7 | Trust Chain validation must verify `iss`/`sub` matches and signature bindings | MUST | Section 4 |
| R8 | Trust Anchor public keys distributed out-of-band | SHOULD | Section 4 |
| R9 | Metadata policy resolution must begin from most Superior and end with Immediate Superior | MUST | Section 6.1.4.1 |
| R10 | If policy error occurs, Trust Chain invalid | MUST | Section 6.1.4 |
| R11 | `federation_fetch_endpoint` MUST be published by Intermediates and Trust Anchors; Leaf Entities MUST NOT | MUST/MUST NOT | Section 5.1.1 |
| R12 | `federation_list_endpoint` MUST be published by Intermediates and Trust Anchors; Leaf Entities MUST NOT | MUST/MUST NOT | Section 5.1.1 |
| R13 | Resolve response JWTs MUST have `typ: resolve-response+jwt` | MUST | Section 8.3.2 |
| R14 | Client authentication at federation endpoints default none; `private_key_jwt` when supported | OPTIONAL | Section 8.8 |
| R15 | Entity Configuration MUST be published at `/.well-known/openid-federation` for Trust Anchors and Intermediates; SHOULD for Leaf Entities | MUST/SHOULD | Section 9 |
| R16 | Federation participants MUST NOT attempt to fetch Entity Statements already obtained to prevent loops | MUST NOT | Section 10.1 |
| R17 | Support refreshing Trust Chain when it expires | MUST | Section 11 |
| R18 | Trust Mark JWTs MUST have `typ: trust-mark+jwt` | MUST | Section 7 |
| R19 | Trust Mark delegation JWTs MUST have `typ: trust-mark-delegation+jwt` | MUST | Section 7.2.1 |
| R20 | String comparisons MUST be Unicode code point equality after JSON escaping removal | MUST | Section 16 |