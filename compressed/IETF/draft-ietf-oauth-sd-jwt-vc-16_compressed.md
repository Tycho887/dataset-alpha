# draft-ietf-oauth-sd-jwt-vc-16: SD-JWT-based Verifiable Digital Credentials (SD-JWT VC)
**Source**: IETF | **Version**: draft-16 | **Date**: 24 April 2026 | **Type**: Normative (Standards Track)
**Expires**: 26 October 2026 | **Intended Status**: Standards Track
**Authors**: O. Terbu (MATTR), D. Fett (Authlete Inc.), B. Campbell (Ping Identity)
**Original**: [https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/](https://datatracker.ietf.org/doc/draft-ietf-oauth-sd-jwt-vc/)

## Scope (Summary)
This specification defines data formats, validation, and processing rules for expressing Verifiable Digital Credentials with JSON payloads, with or without selective disclosure, based on the SD-JWT format [RFC9901]. It covers encoding, verification, metadata, and integrity protection.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC5646] Phillips, A. and M. Davis, "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- [RFC5785] Nottingham, M. and E. Hammer-Lahav, "Defining Well-Known URIs", RFC 5785, April 2010.
- [RFC7515] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015.
- [RFC7517] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015.
- [RFC7519] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, May 2015.
- [RFC7800] Jones, M., Bradley, J., and H. Tschofenig, "Proof-of-Possession Key Semantics for JWTs", RFC 7800, April 2016.
- [RFC9901] Fett, D., Yasuda, K., and B. Campbell, "Selective Disclosure for JSON Web Tokens", RFC 9901, November 2025.
- [W3C.CSS-COLOR] Çelik, T., Lilley, C., and L. D. Baron, "CSS Color Module Level 3", 18 January 2022.
- [W3C.SRI] Akhawe, D., Braun, F., Marier, F., and J. Weinberger, "Subresource Integrity", 23 June 2016.

## Definitions and Abbreviations
- **Holder, Issuer, Verifier, Disclosure, Selectively Disclosable JWT (SD-JWT), Key Binding, Key Binding JWT (KB-JWT), SD-JWT+KB**: as defined in [RFC9901].
- **Consumer**: An application using Type Metadata (Section 4). Typically includes Issuers, Verifiers, and Holders.
- **Publisher**: An entity that publishes Type Metadata or auxiliary documents referenced by an SD-JWT VC (e.g., via a vct URI), not necessarily the Issuer.
- **Verifiable Digital Credential**: An assertion with claims about a Subject that is cryptographically secured by an Issuer (usually by a digital signature).
- **SD-JWT-based Verifiable Digital Credential (SD-JWT VC)**: A Verifiable Digital Credential encoded using [RFC9901]. It may or may not contain selectively disclosable claims.
- **Unsecured Payload of an SD-JWT VC**: A JSON object containing all selectively disclosable and non-selectively disclosable claims of the SD-JWT VC; the input JSON to issue an SD-JWT VC.

## 1. Introduction (Summary)
### 1.1. Issuer-Holder-Verifier Model
- Issuers issue Verifiable Digital Credentials to a Holder, who can present them to Verifiers. Verifiers can check authenticity and optionally enforce Key Binding (proof of possession of a cryptographic key referenced in the credential, per [RFC9901]).

### 1.2. SD-JWT as a Credential Format
- JWTs [RFC7519] can express Verifiable Digital Credentials. SD-JWT [RFC9901] adds selective disclosure. This specification defines SD-JWT VCs: Verifiable Digital Credentials with JSON payloads. Selective disclosure is optional. SD-JWT VCs can use registered, public, or private claims.

### 1.3. Requirements Notation and Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in RFC 2119.

## 2. Verifiable Digital Credentials based on SD-JWT
### 2.1. Media Type
- SD-JWT VCs compliant with this specification MUST use the media type `application/dc+sd-jwt`. The base subtype `dc` stands for "digital credential".

### 2.2. Data Format
- Issuers MUST encode an SD-JWT VC using the SD-JWT format defined in Section 4 or Section 8 of [RFC9901]. By default, Section 4 format is used; support for JWS JSON Serialization (Section 8) is OPTIONAL.
- An SD-JWT VC MAY have no selectively disclosable claims; then no Disclosures are present.
- A presentation of an SD-JWT VC MUST be encoded as an SD-JWT or SD-JWT+KB as defined in Section 4 or Section 8 of [RFC9901]. By default, Section 4 format; JWS JSON Serialization is OPTIONAL.

#### 2.2.1. JOSE Header
- The Issuer MUST include the `typ` header parameter in the SD-JWT. The `typ` value MUST be `dc+sd-jwt`.
- During a transitional period, both `vc+sd-jwt` and `dc+sd-jwt` should be accepted.

#### 2.2.2. JWT Claims Set
##### 2.2.2.1. Verifiable Digital Credential Type – `vct` Claim
- Defines new JWT claim `vct`. Its value MUST be a case-sensitive string serving as an identifier for the type of the SD-JWT VC. The `vct` value MUST be a Collision-Resistant Name as defined in Section 2 of [RFC7515].
- A type is associated with rules defining permitted/required claims and selective disclosure constraints. This specification does not define any `vct` values; ecosystems define them.
- The `vct` value identifies the version of the credential type definition. Changes that introduce incompatibilities should use a new `vct` value.

##### 2.2.2.2. Registered JWT Claims
Claims that MUST NOT be selectively disclosed (cannot be in Disclosures):
- `iss`: OPTIONAL (Issuer identifier)
- `nbf`: OPTIONAL (not before time)
- `exp`: OPTIONAL (expiry time)
- `cnf`: OPTIONAL unless Key Binding is supported, in which case it is REQUIRED. Contains confirmation method per [RFC7800]; RECOMMENDED to contain a JWK. For Key Binding, the KB-JWT MUST be secured by the key identified in this claim.
- `vct`: REQUIRED (type identifier)
- `vct#integrity`: OPTIONAL (hash of Type Metadata for integrity, per Section 5)
- `status`: OPTIONAL (status information; if using `status_list`, the Status List Token MUST be in JWT format)

Claims that MAY be selectively disclosed:
- `sub`: OPTIONAL (Subject identifier; no binding requirement between `sub` and `cnf`)
- `iat`: OPTIONAL (issuance time)

##### 2.2.2.3. Public and Private JWT Claims
- Any public and private claims per Sections 4.2 and 4.3 of [RFC7519] MAY be used.
- Binary data in claims SHOULD be encoded as data URIs [RFC2397]. Exceptions for established text encodings.

##### 2.2.2.4. SD-JWT VC without Selectively Disclosable Claims
- An SD-JWT VC MAY have no selectively disclosable claims. In that case, the SD-JWT VC MUST NOT contain the `_sd` claim in the JWT body and MUST NOT have any Disclosures.

### 2.3. Example (Informative – condensed)
- Section provides examples of issuance and presentation of SD-JWT VCs, including SD-JWT+KB. Examples illustrate unsecured payloads, Disclosures, and processed payloads after verification. (Refer to original for full examples.)

### 2.4. Verification and Processing
- The recipient (Holder or Verifier) of an SD-JWT VC MUST process and verify as described in Section 7 of [RFC9901].
- The check in point 2.c of Section 7.1 of [RFC9901] (validate Issuer and signing key) MUST be satisfied by determining and validating the public verification key using a permitted key discovery and validation mechanism (Section 2.5).
- If Key Binding is required (per security considerations in Section 9.5 of [RFC9901]), the Verifier MUST verify the KB-JWT according to Section 7.3 of [RFC9901] using the `cnf` claim of the SD-JWT.
- If no selectively disclosable claims, no need to process `_sd` or Disclosures.
- If `status` is present, the status SHOULD be checked; Verifier policy decides acceptance.
- Additional validation rules MAY apply but are out of scope.

### 2.5. Issuer Verification Key Discovery and Validation
- A key discovery and validation mechanism defines how a Verifier determines the appropriate key and procedure for verifying the Issuer-signed JWT.
- A recipient MUST determine and validate the public verification key using a supported mechanism permitted for the Issuer according to policy. This specification defines two mechanisms:
  - **JWT VC Issuer Metadata**: When the `iss` claim is an HTTPS URI, the recipient obtains the public key from the JWT VC Issuer Metadata as defined in Section 3.
  - **Inline X.509 Certificates**: When the protected header contains the `x5c` parameter, the recipient uses the public key from the end-entity certificate and validates the X.509 chain. The Issuer is the subject of the end-entity certificate.
- Separate specifications or ecosystem regulations may define additional mechanisms (see Section 6.2).
- If a recipient cannot validate that the public verification key corresponds to the Issuer using a permitted mechanism, the SD-JWT VC MUST be rejected.

## 3. JWT VC Issuer Metadata
- Defines metadata to retrieve the configuration of the SD-JWT VC Issuer (identified by `iss`). Use is OPTIONAL.
- Issuers publishing metadata MUST make it available at `/.well-known/jwt-vc-issuer` inserted between host and path of the `iss` value. The `iss` MUST be a case-sensitive HTTPS URL with scheme, host, optionally port and path, no query or fragment.

### 3.1. JWT VC Issuer Metadata Request
- MUST be queried using HTTP GET at the path defined in Section 3. If `iss` contains a path component, any terminating `/` MUST be removed before inserting `/.well-known/`.

### 3.2. JWT VC Issuer Metadata Response
- Successful response MUST use HTTP 200 and return JSON with `application/json`.
- Error response MUST use applicable HTTP status code.
- Defined parameters:
  - `issuer`: REQUIRED. MUST be identical to `iss` in the JWT.
  - `jwks_uri`: OPTIONAL. URL referencing the Issuer's JWK Set [RFC7517].
  - `jwks`: OPTIONAL. JWK Set document (JSON object).
- Metadata MUST include either `jwks_uri` or `jwks`, not both.
- RECOMMENDED that the Issuer-signed JWT contains a `kid` header for key lookup.
- Additional parameters MAY be used.

### 3.3. JWT VC Issuer Metadata Validation
- The `issuer` value returned MUST be identical to the `iss` value of the Issuer-signed JWT. If not identical, the data MUST NOT be used.

## 4. SD-JWT VC Type Metadata
- Defines metadata associated with a `vct` value, including display and claim information. Intended for developers, Verifiers (to check rules), and Holders (for display).
- Type Metadata can be retrieved as described in Section 4.3.

### 4.1. Type Metadata Example (Informative – condensed)
- Example shows an SD-JWT VC payload with `vct` and `vct#integrity`, and a Type Metadata document with `extends` and integrity.

### 4.2. Type Metadata Format
- MUST be a JSON object. Defined properties:
  - `vct`: REQUIRED. The type described.
  - `name`: OPTIONAL (human-readable for developers).
  - `description`: OPTIONAL (human-readable for developers).
  - `extends`: OPTIONAL. URI of another type that this type extends (Section 4.4).
  - `display`: OPTIONAL. Array of display objects per locale (Section 4.5).
  - `claims`: OPTIONAL. Array of claim metadata objects (Section 4.6).
- `extends#integrity` MAY be present (Section 5).
- May contain additional properties; Consumers MUST ignore unknown properties.

### 4.3. Retrieving Type Metadata
- Consumer MUST ensure that the `vct` value in the SD-JWT VC payload is identical to the `vct` value in the reference to the Type Metadata.
- Methods:
  - **From a URL in the `vct` claim**: If the type is an HTTPS URL, metadata MAY be retrieved via HTTP GET. Successful response: HTTP 200, JSON as Section 4.2, `application/json`. Error: applicable HTTP status code. If `vct#integrity` is present, it MUST be an integrity metadata string per Section 5.
  - **From a Registry**: Consumer MAY use a trusted registry to provide Type Metadata in the same format.
  - **Using a Defined Retrieval Method**: Ecosystems MAY define additional methods.
  - **From a Local Cache**: Consumer MAY cache metadata. If hash for integrity is present, may cache indefinitely; otherwise MUST use Cache-Control header.

### 4.4. Extending Type Metadata
- A type can extend another type via the `extends` URI. Consumers MUST retrieve and process metadata for the extended type before the extending type.
- Extended type may itself extend another type (chain). Circular dependencies MUST be avoided (see Section 6.3).
- Processing rules for display and claim metadata inheritance are defined in Sections 4.5.2 and 4.6.5.

### 4.5. Display Metadata
- `display` property: array with one object per supported locale. Required properties per object:
  - `locale`: REQUIRED (language tag per [RFC5646]).
  - `name`: REQUIRED (human-readable name for end users).
  - `description`: OPTIONAL.
  - `rendering`: OPTIONAL (object containing rendering method objects).

#### 4.5.1. Rendering Metadata
- Object with property for each rendering method. Methods defined:
  - **`simple`** (for non-SVG applications): properties:
    - `logo`: OPTIONAL (object with `uri` REQUIRED, `uri#integrity` OPTIONAL, `alt_text` OPTIONAL).
    - `background_image`: OPTIONAL (object with `uri` REQUIRED, `uri#integrity` OPTIONAL).
    - `background_color`: OPTIONAL (RGB color value).
    - `text_color`: OPTIONAL (RGB color value).
  - **`svg_templates`** (for SVG rendering): array of objects with:
    - `uri`: REQUIRED.
    - `uri#integrity`: OPTIONAL.
    - `properties`: OPTIONAL (object with `orientation`, `color_scheme`, `contrast` – at least one required if more than one template).

##### 4.5.1.2.2. SVG Rendering
- Consuming application MUST preprocess the SVG template by replacing placeholders `{{svg_id}}` with properly escaped claim values.
- Placeholders MUST only be used in text content. Characters to escape: `&` → `&amp;`, `<` → `&lt;`, `>` → `&gt;`, `"` → `&quot;`, `'` → `&apos;`.
- If `svg_id` is not in claim metadata, SHOULD reject the template. If present but claim absent, replace with empty string or appropriate text.
- Application MUST NOT execute any code in the SVG; sandbox if needed. External resources in SVG must not enable tracking.

#### 4.5.2. Extending Display Metadata
- When a type extends another, the display metadata of the extended type remains valid for the inheriting type unless the inheriting type defines its own `display` property, in which case the original is ignored. This does not affect claim display metadata (see 4.6.5).

### 4.6. Claim Metadata
- `claims` array: each object describes one or more claims. Properties:
  - `path`: REQUIRED (non-empty array of strings, null values, or non-negative integers). Describes how to select the claim(s) in the credential. (Processing rules in 4.6.1.2.)
  - `display`: OPTIONAL (array per locale, see 4.6.2).
  - `mandatory`: OPTIONAL (boolean; default `false`). If `true`, the claim MUST be included by the Issuer.
  - `sd`: OPTIONAL (string: `always`, `allowed`, `never`; default `allowed`). Indicates selective disclosure rules.
  - `svg_id`: OPTIONAL (string for SVG template placeholder; must be unique within type metadata, alphanumeric and underscores, not start with digit).

#### 4.6.1. Claim Path
- Path elements: string selects key; null selects all array elements; non-negative integer selects array index.
- Processing from left to right: if at any point key/index not found, remove that element from selection. If selection becomes empty, abort with error.
- Path MUST point to claim as if all selectively disclosable claims were disclosed (so consumer without all disclosures may not identify the claim).
- Not using JSON Pointer or JSON Path for reasons explained.

#### 4.6.2. Claim Display Metadata
- Array of objects per locale:
  - `locale`: REQUIRED.
  - `label`: REQUIRED (human-readable).
  - `description`: OPTIONAL.

#### 4.6.3. Claim Mandatory Metadata
- Boolean `mandatory`: if `true`, claim MUST be included by Issuer. If `false` or omitted, optional. A mandatory claim can still be selectively disclosable.

#### 4.6.4. Claim Selective Disclosure Metadata
- `sd` values:
  - `always`: Issuer MUST make the claim selectively disclosable.
  - `allowed`: Issuer MAY make the claim selectively disclosable (default).
  - `never`: Issuer MUST NOT make the claim selectively disclosable.
- RECOMMENDED to use `always` or `never` to avoid ambiguity.

#### 4.6.5. Extending Claim Metadata
- When a type extends another, all claim metadata from the extended type MUST be respected and inherited unless overridden.
- If child type defines metadata with the same path, child's properties take precedence on a per-property basis (no deep merge). Limitations:
  - `sd`: child can change `allowed` to `always` or `never`, but MUST NOT change `always` or `never` to a different value.
  - `mandatory`: child can set `true` on optional claim, but MUST NOT change `true` to `false`.
- (Example in 4.6.5.2 shows inheritance and override.)

## 5. Integrity of Referenced Documents
- For references (`vct`, `extends`, `uri`), a corresponding `#integrity` value can be used to identify expected content.
- Value MUST be an "integrity metadata" string as defined in Section 3 of [W3C.SRI].
- If integrity property is present, the Consumer MUST verify the integrity of the retrieved document as defined in Section 3.3.5 of [W3C.SRI].

## 6. Security Considerations (Condensed)
- Security considerations from [RFC9901] apply.
- **6.1. SSRF**: Before requesting JWT VC Issuer Metadata, Holder/Verifier MUST validate the URL (HTTPS, not internal resources). Request must be time-bound and size-bound. Response must be validated.
- **6.2. Ecosystem-specific Key Verification**: Rules must maintain integrity of `iss`-to-public-key relationship. Verifier MUST ensure attacker cannot influence the verification process type.
- **6.3. Circular "extends" Dependencies**: MUST NOT have circular type extension. Consumers MUST detect and reject.
- **6.4. Robust Retrieval**: SHOULD implement local cache to avoid network failures.
- **6.5. Risks with Textual Information**: Consuming application MUST properly escape text to prevent XSS and handle overly long text.
- **6.6. Credential Type Extension and Issuer Authorization**: Extending a type does not confer authorization to issue. Verifiers MUST independently verify issuer authority. Rogue issuers MUST NOT be accepted based on type hierarchy.
- **6.7. Trust in Type Metadata**: Consumer MUST NOT assume metadata is accurate unless Publisher is authoritative. Ecosystems SHOULD define governance. Consumers SHOULD treat untrusted metadata with reduced trust.
- **6.8. Data URIs for Claim Types**: SHOULD treat data URIs as untrusted input, restrict media types, enforce size limits, avoid dereferencing active content.

## 7. Privacy Considerations (Condensed)
- Privacy considerations from [RFC9901] apply.
- **7.1. Unlinkability**: Per [RFC9901] Section 10.1, especially related to `cnf`.
- **7.2. Verifiable Digital Credential Type Identifier**: `vct` is not selectively disclosable, may leak context. Issuers should choose `vct` values following data minimization. Holders should be informed that `vct` is shared.
- **7.3. Issuer Phone-Home**: Malicious Issuer can use Holder-specific Issuer identifier to track usage via metadata retrieval. Verifiers should pin specific Issuer identifiers and reject suspicious ones. For `cnf`, SHOULD not support remote retrieval of key material (x5u, jku, etc.).
- **7.4. Privacy-Preserving Retrieval**: Consumers SHOULD prefer methods that do not leak usage. Recommendations in 6.4 apply.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | SD-JWT VCs MUST use media type `application/dc+sd-jwt`. | MUST | 2.1 |
| R2 | Issuers MUST encode SD-JWT VC using SD-JWT format per Section 4 or 8 of [RFC9901]. | MUST | 2.2 |
| R3 | Presentations MUST be encoded as SD-JWT or SD-JWT+KB per [RFC9901]. | MUST | 2.2 |
| R4 | The `typ` header MUST be `dc+sd-jwt`. | MUST | 2.2.1 |
| R5 | The `vct` claim value MUST be a case-sensitive Collision-Resistant Name. | MUST | 2.2.2.1 |
| R6 | `iss`, `nbf`, `exp`, `cnf`, `vct`, `vct#integrity`, `status` MUST NOT be selectively disclosed. | MUST | 2.2.2.2 |
| R7 | `cnf` is REQUIRED if Key Binding is supported. | MUST | 2.2.2.2 |
| R8 | `vct` is REQUIRED. | MUST | 2.2.2.2 |
| R9 | SD-JWT VC without selectively disclosable claims MUST NOT contain `_sd` or Disclosures. | MUST | 2.2.2.4 |
| R10 | Verification must follow Section 7 of [RFC9901] and key discovery per Section 2.5. | MUST | 2.4 |
| R11 | If Key Binding required, Verifier MUST verify KB-JWT using `cnf`. | MUST | 2.4 |
| R12 | Recipient MUST determine and validate public verification key using a permitted mechanism; if not, reject. | MUST | 2.5 |
| R13 | JWT VC Issuer Metadata `issuer` value MUST be identical to `iss` in JWT; otherwise data MUST NOT be used. | MUST | 3.3 |
| R14 | JWT VC Issuer Metadata MUST include either `jwks_uri` or `jwks`, not both. | MUST | 3.2 |
| R15 | Type Metadata `vct` value in the SD-JWT VC payload must be identical to the reference value. | MUST | 4.3 |
| R16 | Consumers MUST retrieve and process extended type metadata before extending type. | MUST | 4.4 |
| R17 | `mandatory: true` means claim MUST be included by Issuer. | MUST | 4.6.3 |
| R18 | `sd: always` means Issuer MUST make claim selectively disclosable; `never` means MUST NOT. | MUST | 4.6.4 |
| R19 | Extending type MUST NOT change `sd` from `always`/`never` to another value; MUST NOT change `mandatory` from `true` to `false`. | MUST | 4.6.5.1 |
| R20 | If integrity property present, Consumer MUST verify integrity of retrieved document per [W3C.SRI]. | MUST | 5 |
| R21 | SSRF: Before requesting metadata, validate URL is HTTPS and not internal; time-bound/size-bound request. | MUST | 6.1 |
| R22 | Circular type extension MUST be detected and rejected. | MUST | 6.3 |
| R23 | SVG rendering: MUST escape special characters; MUST NOT execute code; MUST sandbox if code execution possible. | MUST | 4.5.1.2.2 |
| R24 | For `cnf` claims, SHOULD not support remote key retrieval mechanisms (x5u, jku, etc.). | SHOULD | 7.3 |

## Informative Annexes (Condensed)
- **Appendix A. IANA Considerations**: Requests registration of `vct` and `vct#integrity` JWT claims, media type `application/dc+sd-jwt`, and well-known URI `jwt-vc-issuer`.
- **Appendix B. Examples**: Non-normative examples of Person Identification Data (PID) credential and Type Metadata, including issuance, presentation, and claim path usage.
- **Appendix C. Acknowledgements**: Lists contributors.
- **Appendix D. Document History**: Summarizes changes from version -16 back to -00.