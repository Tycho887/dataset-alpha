# RFC 9901: Selective Disclosure for JSON Web Tokens
**Source**: IETF (Internet Engineering Task Force) | **Version**: Standards Track | **Date**: November 2025 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9901

## Scope (Summary)
Defines a mechanism for selective disclosure of individual elements of a JSON data structure used as the payload of a JSON Web Signature (JWS). The primary use case is selective disclosure of JSON Web Token (JWT) claims. The mechanism uses salted hashes: for each selectively disclosable element, a digest replaces the cleartext in the signed payload; the Holder presents cleartext and salt only for those claims to be disclosed.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997, <https://www.rfc-editor.org/info/rfc2119>.
- [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, DOI 10.17487/RFC5234, January 2008, <https://www.rfc-editor.org/info/rfc5234>.
- [RFC6838] Freed, N., Klensin, J., and T. Hansen, "Media Type Specifications and Registration Procedures", BCP 13, RFC 6838, DOI 10.17487/RFC6838, January 2013, <https://www.rfc-editor.org/info/rfc6838>.
- [RFC7515] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, DOI 10.17487/RFC7515, May 2015, <https://www.rfc-editor.org/info/rfc7515>.
- [RFC7516] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, DOI 10.17487/RFC7516, May 2015, <https://www.rfc-editor.org/info/rfc7516>.
- [RFC7519] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015, <https://www.rfc-editor.org/info/rfc7519>.
- [RFC7800] Jones, M., Bradley, J., and H. Tschofenig, "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)", RFC 7800, DOI 10.17487/RFC7800, April 2016, <https://www.rfc-editor.org/info/rfc7800>.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017, <https://www.rfc-editor.org/info/rfc8174>.
- [RFC8725] Sheffer, Y., Hardt, D., and M. Jones, "JSON Web Token Best Current Practices", BCP 225, RFC 8725, DOI 10.17487/RFC8725, February 2020, <https://www.rfc-editor.org/info/rfc8725>.

## Definitions and Abbreviations
- **Base64url**: URL-safe base64 encoding without padding as defined in Section 2 of [RFC7515].
- **Claim**: Refers to object properties (name/value pairs) and array elements.
- **Selective Disclosure**: Process of a Holder disclosing a subset of claims contained in a JWT issued by an Issuer.
- **Selectively Disclosable JWT (SD-JWT)**: Composite structure of an Issuer-signed JWT (JWS) and zero or more Disclosures. Supports selective disclosure.
- **Disclosure**: Base64url-encoded JSON array containing salt, claim name (for name/value pairs) or omitted (for array elements), and claim value. Used to compute digest.
- **Key Binding**: Ability of Holder to prove possession of an SD-JWT by proving control over a private key during presentation. SD-JWT contains the public key or a reference.
- **Key Binding JWT (KB-JWT)**: JWT tied to a particular SD-JWT; contains sd_hash, nonce, aud, iat.
- **Selectively Disclosable JWT with Key Binding (SD-JWT+KB)**: Composite of SD-JWT and a KB-JWT.
- **Processed SD-JWT Payload**: JSON object after verification and processing, with digest placeholders replaced by disclosed values.
- **Issuer**: Entity that creates SD-JWTs.
- **Holder**: Entity that receives and controls SD-JWTs.
- **Verifier**: Entity that requests, checks, and extracts claims from an SD-JWT.

## Introduction and Feature Summary
### Feature Summary
Defines two primary data formats:
1. **SD-JWT**: JWS plus optional Disclosures.
   - Format for selective disclosure in nested JSON (object properties and array elements).
   - Encoding of selectively disclosable data items.
   - Extension of JWS Compact Serialization for combined transport.
   - Alternate format using JWS JSON Serialization.
2. **SD-JWT+KB**: SD-JWT plus cryptographic Key Binding.
   - Mechanism to associate SD-JWT with a key pair.
   - Format for KB-JWT proving possession of private key.
   - Extension of SD-JWT format for combined transport.

### Conventions and Terminology
Normative language (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL) is interpreted per BCP 14 [RFC2119][RFC8174].

## Flow Diagram
- Issuer issues SD-JWT (including all Disclosures) to Holder.
- Holder presents SD-JWT or SD-JWT+KB (including selected Disclosures) to Verifiers.

## Concepts
### SD-JWT and Disclosures
- SD-JWT contains digests over selectively disclosable claims; Disclosures are outside the signed part.
- Digests computed over base64url-encoded Disclosure (salt + claim name (for object properties) + claim value).
- SD-JWT MAY contain cleartext claims.

### Disclosing to a Verifier
Holder sends only the selected Disclosures.

### Optional Key Binding
- When required, SD-JWT MUST contain Holder public key (via `cnf` claim). Refer to Section 4.1.2.
- Holder presents SD-JWT+KB: SD-JWT plus KB-JWT.
- KB-JWT encodes signature over: sd_hash (hash of SD-JWT), nonce, aud.

### Verification
Verifier: verifies Issuer signature on SD-JWT, optionally verifies KB-JWT signature using Holder public key, computes digests over received Disclosures and checks they exist in SD-JWT.

## SD-JWT and SD-JWT+KB Data Formats
### Issuer-Signed JWT
- MUST be signed (MUST NOT use "none").
- Payload rules:
  1. MAY contain `_sd_alg` (hash algorithm claim) at top level. If absent, default is `sha-256`.
  2. MAY contain digests of Disclosures.
  3. MAY contain decoy digests.
  4. MAY contain permanently disclosed claims.
  5. MAY contain Holder public key(s) via `cnf` (see [RFC7800]).
  6. MAY contain other claims like `iss`, `iat`, etc.
  7. MUST NOT contain `_sd` or `...` except as described in Sections 4.2.4.1 and 4.2.4.2.
- Same digest MUST NOT appear more than once. Applications SHOULD use explicit typing. See Section 9.11.

### Disclosures
#### For Object Properties (name/value pairs)
- MUST create JSON array of three elements: [salt (string), claim name (string), claim value (any JSON type)].
- Salt MUST be unique, cryptographically random, minimum recommended 128 bits. MUST NOT be revealed except to Holder.
- Claim name MUST NOT be `_sd`, `...`, or a permanently disclosed claim at that level.
- Base64url-encode UTF-8 byte sequence of the JSON array → Disclosure string.

#### For Array Elements
- MUST create JSON array of two elements: [salt (string), element value (any JSON type)].
- Base64url-encode as above.

#### Hashing Disclosures
- Digest computed over US-ASCII bytes of the base64url-encoded Disclosure string.
- Hash algorithm from `_sd_alg` or default SHA-256.
- Output bytes base64url encoded.

#### Embedding Disclosure Digests in SD-JWTs
- **Object Properties**: Digests are added to an array under the key `_sd` in the object. `_sd` MUST be an array of strings (digests or decoys). RECOMMENDED to shuffle (e.g., sort alphabetically) to hide original order. May be empty; RECOMMENDED to omit when not used.
- **Array Elements**: For each digest, an object of form `{"...": "<digest>"}` replaces the element. Key MUST be `...`, value MUST be digest.

#### Decoy Digests
- Additional digests not associated with any claim. Created by hashing a random number. No Disclosure sent. RECOMMENDED to obscure actual number of claims.

#### Recursive Disclosures
- Disclosures may contain further `_sd` arrays or array placeholders. If a Disclosure is included, all other Disclosures necessary to "connect" it to the signed JWT MUST also be included.

### Key Binding JWT (KB-JWT)
- MUST be a JWT with:
  - Header: `typ` REQUIRED, value `kb+jwt`; `alg` REQUIRED (digital signature, not "none").
  - Payload: `iat` REQUIRED, `aud` REQUIRED (single string), `nonce` REQUIRED (string), `sd_hash` REQUIRED (hash of SD-JWT as defined).
- Additional claims SHOULD be avoided.
- `sd_hash` computed over: `<Issuer-signed JWT>~<Disclosure 1>~...~<Disclosure N>~` using same hash algorithm as `_sd_alg`.

### Serialization Format
- SD-JWT (compact): `<Issuer-signed JWT>~<D.1>~<D.2>~...~<D.N>~` (trailing tilde required; last component empty).
- SD-JWT+KB: same but last component is KB-JWT; trailing tilde absent.
- ABNF provided.

## Verification and Processing
### Verification of SD-JWT
1. Separate Issuer-signed JWT and Disclosures.
2. Validate Issuer-signed JWT:
   a. Ensure signing algorithm is secure; MUST NOT accept "none".
   b. Validate signature per [RFC7515] Section 5.2.
   c. Validate Issuer and signing key.
   d. Check `_sd_alg` value is understood and secure.
3. Process Disclosures and digests:
   a. For each Disclosure, compute digest.
   b. Identify all embedded digests in payload:
      - Objects with `_sd` key (array of strings).
      - Array elements that are objects with one key `...` (string).
   c. For each digest:
      - If found in `_sd`: Verify Disclosure is JSON array of three elements; claim name must not be `_sd` or `...`; claim name must not already exist at that level; insert claim into object; recursively process value.
      - If found in array: Verify Disclosure is JSON array of two elements; replace element with value; recursively process.
   d. Remove array elements for which no matching Disclosure found.
   e. Remove all `_sd` keys.
   f. Remove `_sd_alg` claim.
4. Reject if any digest appears more than once.
5. Reject if any Disclosure is not referenced by a digest (directly or recursively).
6. Reject if required validity claims (nbf, exp, aud) are missing.
- Failure aborts. Otherwise produce Processed SD-JWT Payload.

### Processing by Holder
- Receive SD-JWT (not SD-JWT+KB). MUST reject SD-JWT+KB as input.
- Validate SD-JWT per above.
- For presentation:
  1. Decide which Disclosures to release.
  2. Verify each selected Disclosure has its digest in signed JWT or in another selected Disclosure.
  3. Assemble SD-JWT.
  4. If Key Binding required: create KB-JWT, assemble SD-JWT+KB.

### Verification by Verifier
- Determine if Key Binding required per policy (MUST NOT decide based on presence of KB-JWT).
- If Key Binding required and Holder provided SD-JWT without KB, reject.
- If SD-JWT+KB, parse into SD-JWT and KB-JWT.
- Process SD-JWT per Section 7.1.
- If Key Binding required:
  a. Determine Holder public key from SD-JWT.
  b. Ensure KB-JWT signing algorithm secure; reject "none".
  c. Validate KB-JWT signature.
  d. Check `typ` is `kb+jwt`.
  e. Check `iat` within acceptable window.
  f. Validate `nonce` and `aud` (replay detection).
  g. Compute `sd_hash` over SD-JWT (compact form) and verify equality.
  h. Validate KB-JWT per [RFC7519] and [RFC8725].
- If any step fails, reject.

## JWS JSON Serialization (OPTIONAL)
- New unprotected header parameters: `disclosures` (array of strings), `kb_jwt` (KB-JWT string).
- For SD-JWT+KB in JSON serialization, `kb_jwt` MUST be present and `sd_hash` computed over compact SD-JWT.
- Flattened and General JSON serialization examples.
- Verification uses same logic but Disclosures are read from header.

## Security Considerations
**Summary of key normative requirements**:
- **Mandatory Signing**: JWT MUST be signed; signature MUST be verified. Reject unsigned.
- **Manipulation of Disclosures**: Verifier MUST check digests; naive extraction is insecure.
- **Salt Entropy**: Each salt MUST be cryptographically random, minimum 128 bits, unique per claim.
- **Hash Algorithm**: Must be preimage resistant and second-preimage resistant. SHOULD be collision resistant. Must be from "Named Information Hash Algorithm Registry", but truncated digests (sha-256-32 etc.) are unfit.
- **Key Binding**: Verifier MUST decide beforehand; MUST NOT be influenced by presence of KB-JWT. Without Key Binding, credential can be replayed.
- **Concealing Claim Names**: Permanently disclosed claim names are not hidden.
- **Selectively Disclosable Validity Claims**: Issuer MUST NOT allow critical claims (iss, aud, exp, nbf, cnf) to be selectively disclosable. Verifier MUST ensure all required validity claims are present.
- **Distribution of Issuer Keys**: RECOMMENDED to use JWKS; Verifiers must check key expiry/revocation.
- **Forwarding Credentials**: Any entity in possession can forward (without Key Binding); if undesirable, enforce Key Binding.
- **Integrity**: SD-JWT alone does not protect set of Disclosures; SD-JWT+KB does.
- **Explicit Typing**: RECOMMENDED to use `typ` header with media type `application/example+sd-jwt`.
- **Key Management**: Follow secure generation, storage, lifecycle (NIST SP 800-57).

## Privacy Considerations
- **Unlinkability**: SD-JWT does not provide full unlinkability. Batch issuance with different keys and salts can help. Colluding Verifiers/Issuers can link credential.
- **Storage**: Minimize storage. Issuers SHOULD NOT store SD-JWTs. Holders SHOULD store encrypted, use hardware-backed keys. Verifiers SHOULD NOT store SD-JWT/Disclosures after verification.
- **Confidentiality During Transport**: MUST ensure transport confidentiality (e.g., TLS). MAY encrypt using JWE.
- **Decoy Digests**: RECOMMENDED to obscure number of claims.
- **Issuer Identifier**: May reveal info about user; consider group identifier.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Issuer-signed JWT MUST be signed using Issuer's private key; MUST NOT use "none". | shall | Section 4.1 |
| R2 | The payload MUST NOT contain claims `_sd` or `...` except as specified. | shall | Section 4.1 |
| R3 | Same digest value MUST NOT appear more than once. | shall | Section 4.1 |
| R4 | `_sd_alg` claim, if present, MUST appear at top level. | shall | Section 4.1.1 |
| R5 | If `_sd_alg` absent, default `sha-256` MUST be used. | shall | Section 4.1.1 |
| R6 | Implementations MUST support sha-256. | shall | Section 4.1.1 |
| R7 | For object property claim, Disclosure MUST be JSON array of three elements: [salt, name, value]; salt MUST be string unique; claim name MUST NOT be `_sd`, `...`, or existing permanent claim. | shall | Section 4.2.1 |
| R8 | For array element claim, Disclosure MUST be JSON array of two elements: [salt, value]. | shall | Section 4.2.2 |
| R9 | Digest MUST be computed over US-ASCII bytes of base64url-encoded Disclosure. | shall | Section 4.2.3 |
| R10 | `_sd` key MUST refer to array of strings (digests or decoys). | shall | Section 4.2.4.1 |
| R11 | For array elements, placeholder object MUST have single key `...` with digest value. | shall | Section 4.2.4.2 |
| R12 | Decoy digests MUST use same hash function as Disclosures. | shall | Section 4.2.5 |
| R13 | KB-JWT MUST have `typ` "kb+jwt", `alg` digital signature (not "none"). | shall | Section 4.3 |
| R14 | KB-JWT payload MUST include `iat`, `aud` (single string), `nonce` (string), `sd_hash`. | shall | Section 4.3 |
| R15 | `sd_hash` computed over `<Issuer-signed JWT>~<D.1>~...~<D.N>~` using same hash as `_sd_alg`. | shall | Section 4.3.1 |
| R16 | In SD-JWT compact format, order MUST be: Issuer-signed JWT, tilde, zero or more Disclosures each followed by tilde, then optionally KB-JWT. If no KB-JWT, last element empty string, trailing tilde MUST NOT be omitted. | shall | Section 4 |
| R17 | Verifier of SD-JWT MUST verify final tilde-separated component is empty. | shall | Section 4 |
| R18 | Verifier of SD-JWT+KB MUST verify final component is valid KB-JWT. | shall | Section 4 |
| R19 | Holder presenting SD-JWT MUST NOT send Disclosures not issued or send any Disclosure more than once. | shall | Section 4 |
| R20 | If Key Binding required, SD-JWT MUST contain Holder public key (via `cnf`). | shall | Section 4.1.2 |
| R21 | Verification algorithm (Section 7.1) MUST be followed step-by-step; abort on failure. | shall | Section 7.1 |
| R22 | Verifier MUST reject SD-JWT if any digest appears more than once or any Disclosure is unreferenced. | shall | Section 7.1 |
| R23 | Verifier MUST reject SD-JWT if required validity claims missing. | shall | Section 7.1 |
| R24 | Holder processing (Section 7.2): MUST reject SD-JWT+KB as input. | shall | Section 7.2 |
| R25 | Before presentation, Holder MUST verify each selected Disclosure's hash is in signed JWT or another selected Disclosure. | shall | Section 7.2 |
| R26 | Verifier MUST decide whether Key Binding is required before verification; MUST NOT base decision on presence of KB-JWT. | shall | Section 7.3 |
| R27 | If Key Binding required and no KB-JWT provided, reject. | shall | Section 7.3 |
| R28 | Verifier MUST validate KB-JWT signature, typ, iat, nonce, aud, sd_hash. | shall | Section 7.3 |
| R29 | Salt MUST be cryptographically random, minimum 128 bits recommended. | shall | Section 9.3 |
| R30 | Issuer MUST NOT allow critical claims (iss, aud, exp, nbf, cnf) to be selectively disclosable. | shall | Section 9.7 |
| R31 | Verifier MUST ensure all required validity claims are present/disclosed. | shall | Section 9.7 |
| R32 | Transport confidentiality MUST be ensured (e.g., TLS); if URL transmitted, use JWE. | shall | Section 10.3 |

## Informative Annexes (Condensed)
- **Appendix A.1 – Simple Structured SD-JWT**: Example with Japanese user data, nested address with sub-claims selectively disclosable, decoy digests added. Shows flat vs structured approach.
- **Appendix A.2 – Complex Structured SD-JWT**: Example based on OpenID Connect for Identity Assurance, nested verification and claims objects, recursive disclosures.
- **Appendix A.3 – SD-JWT-Based Verifiable Credentials (SD-JWT VC)**: Example of PID credential with many selectively disclosable claims, Key Binding via `cnf`. Shows SD-JWT+KB presentation for subset of claims.
- **Appendix A.4 – W3C Verifiable Credentials Data Model v2.0**: Example with vaccination certificate, selective disclosure of vaccine and recipient fields.
- **Appendix A.5 – Elliptic Curve Key**: Public JWK used in examples.
- **Appendix B – Disclosure Format Considerations**: Explains design choice of base64url-encoded JSON array (source string hardening) to avoid canonicalization issues. Verifier computes digest on the encoded string before decoding.