# RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)
**Source**: IETF | **Version**: Standards Track | **Date**: September 2023 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/info/rfc9449

## Scope (Summary)
This document specifies a mechanism for sender-constraining OAuth 2.0 access and refresh tokens using an application-level proof-of-possession mechanism. DPoP enables the detection of replay attacks by binding tokens to a client-held public key and requiring proof of possession of the corresponding private key.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2005.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity ...", RFC 6125, March 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750, October 2012.
- [RFC7515] Jones, M., et al., "JSON Web Signature (JWS)", RFC 7515, May 2015.
- [RFC7517] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015.
- [RFC7519] Jones, M., et al., "JSON Web Token (JWT)", RFC 7519, May 2015.
- [RFC7638] Jones, M. and N. Sakimura, "JSON Web Key (JWK) Thumbprint", RFC 7638, September 2015.
- [RFC7800] Jones, M., et al., "Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)", RFC 7800, April 2016.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.
- [SHS] National Institute of Standards and Technology, "Secure Hash Standard (SHS)", FIPS PUB 180-4, August 2015.

## Definitions and Abbreviations
- **DPoP**: Demonstrating Proof of Possession.
- **JWT**: JSON Web Token [RFC7519].
- **JWS**: JSON Web Signature [RFC7515].
- **JWK**: JSON Web Key [RFC7517].
- **Access Token, Refresh Token, Authorization Server, Resource Server, Authorization Endpoint, Token Endpoint, Grant Type, Client, Public Client, Confidential Client**: As defined in [RFC6749].
- **Request, Response, Header Field, Target URI**: As defined in [RFC9110].
- **JOSE, JOSE Header**: As defined in [RFC7515].
- **DPoP Proof**: A JWT sent in the `DPoP` HTTP header, proving possession of a private key.
- **jti**: Unique identifier for a DPoP proof (JWT ID).
- **htm**: HTTP method of the request.
- **htu**: HTTP target URI (without query and fragment).
- **iat**: Issued-at timestamp.
- **ath**: Base64url-encoded SHA-256 hash of the associated access token.
- **nonce**: Value provided by server via `DPoP-Nonce` header.
- **jkt**: JWK SHA-256 Thumbprint confirmation method.

## 1. Introduction
DPoP is an application-level mechanism for sender-constraining OAuth tokens. It enables a client to prove possession of a public/private key pair by including a `DPoP` header containing a JWT. The authorization server binds issued tokens to the client's public key. Recipients verify the binding, constraining the token to the holder of the private key. DPoP is usable where TLS-level mechanisms like mTLS or token binding are not available (e.g., single-page applications). DPoP does not replace client authentication.

### 1.1. Conventions and Terminology
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL**: Interpreted as per BCP 14 [RFC2119] [RFC8174].
- ABNF notation per [RFC5234].
- Terms from [RFC6749], [RFC9110], [RFC7515] apply.

## 2. Objectives
Primary aim: Prevent unauthorized use of leaked/stolen tokens by binding a token to a public key upon issuance and requiring proof of private key possession when using the token. DPoP provides defense-in-depth against token leakage; it is not a substitute for secure transport and **MUST** always be used with HTTPS. DPoP also prevents token replay at different endpoints. For browser-based clients, DPoP with non-extractable keys renders exfiltrated tokens unusable. Server-provided nonces can prevent pre-generated DPoP proofs.

## 3. Concept
A DPoP proof JWT is sent as a header in HTTP requests. It is a signature over: request method and URI, timestamp, unique identifier, optional server nonce, and hash of the access token if present. The basic flow:
- (A) Client sends token request with DPoP proof to authorization server.
- (B) Authorization server binds access token (and refresh token for public clients) to the public key.
- (C) Client uses access token with new DPoP proof to protected resource.
- (D) Resource server verifies DPoP proof and key binding; refuses if checks fail.

## 4. DPoP Proof JWTs
Each HTTP request requires a unique DPoP proof.

### 4.1. The DPoP HTTP Header
- **Header field**: `DPoP`
- **Value**: A JWT per Section 4.2, using token68 syntax.
- ABNF: `DPoP = token68`

### 4.2. DPoP Proof JWT Syntax
**JOSE Header (MUST contain):**
- `typ`: Value `dpop+jwt`
- `alg`: Asymmetric digital signature algorithm from [IANA.JOSE.ALGS]; **MUST NOT** be `none` or symmetric.
- `jwk`: Public key in JWK format; **MUST NOT** contain private key.

**Payload (MUST contain):**
- `jti`: Unique identifier (≥96 bits random or UUID v4)
- `htm`: HTTP method of the request
- `htu`: HTTP target URI without query/fragment
- `iat`: Creation timestamp

**When presenting access token (MUST also contain):**
- `ath`: Base64url-encoded SHA-256 hash of the access token value (ASCII encoding).

**When server provides nonce (MUST also contain):**
- `nonce`: Value from `DPoP-Nonce` header.

May contain other extension parameters.

### 4.3. Checking DPoP Proofs
Receiving server **MUST** ensure:
1. Only one `DPoP` header.
2. Value is a well-formed JWT.
3. All required claims present.
4. `typ` is `dpop+jwt`.
5. `alg` is registered asymmetric, not `none`, supported and acceptable per local policy.
6. Signature verifies with public key from `jwk`.
7. `jwk` contains no private key.
8. `htm` matches request method.
9. `htu` matches request URI (ignoring query/fragment).
10. If nonce provided, `nonce` matches server value.
11. Creation time (via `iat` or nonce) is within acceptable window.
12. If access token present: `ath` equals hash of that token, and public key matches token binding.
Servers **SHOULD** use syntax and scheme normalization per [RFC3986] for `htu` comparison.

## 5. DPoP Access Token Request
- Client **MUST** provide a valid DPoP proof in `DPoP` header for all token requests (any grant type).
- If DPoP proof is invalid, authorization server **MUST** respond with error `invalid_dpop_proof` per [RFC6749] Section 5.2.
- Authorization server associates issued access token with public key from DPoP proof.
- `token_type` **MUST** be `DPoP` in response.
- For public clients: refresh tokens **MUST** be bound to the public key used to obtain them. Validation **MUST** be performed on refresh token usage.
- For confidential clients: refresh tokens are not DPoP-bound (already sender-constrained by client authentication).
- Authorization server **MAY** issue non-DPoP tokens (token_type=Bearer); for public clients, refresh tokens alone may be DPoP-bound.
- If token_type is not `DPoP`, client **MUST** discard response if DPoP protection deemed important.

### 5.1. Authorization Server Metadata
- New parameter: `dpop_signing_alg_values_supported`: JSON array of JWS algorithms supported for DPoP proofs.

### 5.2. Client Registration Metadata
- New parameter: `dpop_bound_access_tokens`: Boolean, default `false`. If `true`, server **MUST** reject token requests without `DPoP` header.

## 6. Public Key Confirmation
Resource servers **MUST** be able to determine if token is DPoP-bound and verify binding. Binding can be via embedding hash in JWT (Section 6.1) or token introspection (Section 6.2). Other methods are beyond scope. Resource servers **MUST** ensure public key from DPoP proof matches token binding.

### 6.1. JWK Thumbprint Confirmation Method
- Under `cnf` claim, new member `jkt`: base64url encoding of JWK SHA-256 Thumbprint [RFC7638] of the DPoP public key.
- Used in JWT-structured access tokens.

### 6.2. JWK Thumbprint Confirmation Method in Token Introspection
- Introspection response includes `cnf` with `jkt` as top-level member.
- If `token_type` included, **MUST** be `DPoP`.

## 7. Protected Resource Access
- Requests **MUST** include both `DPoP` proof (with `ath` claim) and access token.
- `ath` binds token to proof, preventing swap.
- Resource server calculates hash of token value and verifies match with `ath`.

### 7.1. The DPoP Authentication Scheme
- Use `Authorization: DPoP <token>` header with token68 syntax.
- Resource server **MUST** check DPoP proof according to Section 4.3 and that public key matches token binding.
- **MUST NOT** grant access unless all checks succeed.
- WWW-Authenticate scheme is `DPoP`. Parameters: `realm`, `scope`, `error`, `error_description`, `algs`. Error values: `invalid_dpop_proof`, `use_dpop_nonce`.
- For CORS, `WWW-Authenticate` must be exposed via `Access-Control-Expose-Headers`.
- **MUST NOT** be used with Proxy-Authenticate/Proxy-Authorization.

### 7.2. Compatibility with Bearer Authentication Scheme
- Protected resource supporting both schemes **MUST** reject a DPoP-bound token used as Bearer.
- Recommendations for multiple challenges: omit error if no auth; use corresponding scheme; otherwise both.

### 7.3. Client Considerations
- Requests with DPoP proof may not be idempotent. **RECOMMENDED** to generate unique proof even when retrying idempotent requests.

## 8. Authorization Server-Provided Nonce
- Server **MAY** provide nonce to limit DPoP proof lifetime.
- Server responds to requests without nonce with HTTP 400, error `use_dpop_nonce`, and `DPoP-Nonce` header.
- Nonce values **MUST** be unpredictable.
- Client **MUST** include `nonce` claim in subsequent DPoP proofs.
- If `nonce` does not match, server **MUST** reject request.
- Server **MAY** provide new nonce in HTTP 200 responses; client **MUST** use new nonce.
- Responses with `DPoP-Nonce` should be uncacheable.
- For CORS, `DPoP-Nonce` must be exposed via `Access-Control-Expose-Headers`.

### 8.1. Nonce Syntax
- `nonce = 1*NQCHAR`

### 8.2. Providing a New Nonce Value
- Server controls when to issue new nonce.
- New nonce can be supplied in same manner (HTTP error) or in HTTP 200 response.

## 9. Resource Server-Provided Nonce
- Resource server can provide nonce via `DPoP-Nonce` header in HTTP 401 response with `WWW-Authenticate: DPoP error="use_dpop_nonce"`.
- Nonces are server-specific; must not be confused between servers.

## 10. Authorization Code Binding to a DPoP Key
- Optional authorization request parameter `dpop_jkt`: JWK Thumbprint of the proof-of-possession public key (SHA-256).
- On token request, authorization server computes thumbprint from DPoP proof and verifies match with `dpop_jkt`; if not, **MUST** reject.
- Can be used with PKCE.

### 10.1. DPoP with Pushed Authorization Requests
- Two ways to communicate DPoP key: (1) `dpop_jkt` in POST body; (2) `DPoP` header in PAR request. Server **MUST** support both.
- If both used, server **MUST** reject if thumbprints don't match.
- Using DPoP header provides stronger binding (proof of possession).

## 11. Security Considerations
### 11.1. DPoP Proof Replay
- Servers **MUST** limit acceptance of DPoP proofs to a short time window (seconds/minutes) after creation.
- Servers **MUST** store `jti` during that window to prevent replay; accept only if `jti` not seen before.
- To prevent memory exhaustion, reject overly large `jti` or store hash.
- Server **MAY** accept `iat` in near future to accommodate clock skew; using server-provided nonce with embedded time is recommended.

### 11.2. DPoP Proof Pre-generation
- Server-provided nonce that is unpredictable can prevent pre-generation attack.
- The `ath` claim limits pre-generation to lifetime of access token.
- Deployments without nonce **SHOULD** use short-lived access tokens and refresh tokens.

### 11.3. DPoP Nonce Downgrade
- Server **MUST NOT** accept DPoP proofs without `nonce` claim if nonce has been provided.

### 11.4. Untrusted Code in the Client Context
- If adversary executes code in client context, DPoP security is compromised. Use of non-extractable private keys limits exfiltration but does not prevent use during online sessions.
- Protecting against XSS is critical; Content Security Policy recommended.

### 11.5. Signed JWT Swapping
- Servers **MUST** verify `typ` is `dpop+jwt` to prevent misuse of other JWTs.

### 11.6. Signature Algorithms
- Only asymmetric algorithms deemed secure; `none` **MUST NOT** be allowed.

### 11.7. Request Integrity
- DPoP does not ensure integrity of payload or headers beyond method and URI. TLS provides protection in many setups.

### 11.8. Access Token and Public Key Binding
- Uses SHA-256 hash of JWK for binding; relies on second-preimage resistance.

### 11.9. Authorization Code and Public Key Binding
- Binding via `dpop_jkt` prevents capture/replay of authorization code; works with PKCE.

### 11.10. Hash Algorithm Agility
- Specification uses SHA-256; if needed, new claims/parameters would be defined.

### 11.11. Binding to Client Identity
- DPoP is not cryptographically bound to client authentication; improvement beyond scope.

## 12. IANA Considerations
(Summarized registrations – see original for full details)
- OAuth Access Token Type: `DPoP`
- OAuth Extensions Error: `invalid_dpop_proof`, `use_dpop_nonce`
- OAuth Parameters: `dpop_jkt`
- HTTP Authentication Scheme: `DPoP`
- Media Type: `application/dpop+jwt`
- JWT Confirmation Method: `jkt`
- JWT Claims: `htm`, `htu`, `ath`; updated `nonce`
- HTTP Field Names: `DPoP`, `DPoP-Nonce`
- OAuth Authorization Server Metadata: `dpop_signing_alg_values_supported`
- OAuth Dynamic Client Registration Metadata: `dpop_bound_access_tokens`

## 13. References
(Normative and Informative as listed in original – preserved for completeness)

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | DPoP proof JWT header MUST contain `typ`, `alg`, `jwk` | MUST | Section 4.2 |
| R2 | DPoP proof payload MUST contain `jti`, `htm`, `htu`, `iat` | MUST | Section 4.2 |
| R3 | When access token present, DPoP proof MUST contain `ath` | MUST | Section 4.2 |
| R4 | When server provides nonce, DPoP proof MUST contain `nonce` | MUST | Section 4.2 |
| R5 | Receiver MUST validate DPoP proof per 12-step checklist | MUST | Section 4.3 |
| R6 | Token requests MUST include valid DPoP proof | MUST | Section 5 |
| R7 | Authorization server MUST respond with `invalid_dpop_proof` on invalid proof | MUST | Section 5 |
| R8 | Access token response MUST include `token_type: DPoP` | MUST | Section 5 |
| R9 | Refresh tokens for public clients MUST be bound to DPoP key | MUST | Section 5 |
| R10 | Resource server MUST check DPoP proof and key binding on each request | MUST | Section 7.1 |
| R11 | Resource server MUST reject DPoP-bound token used as Bearer | MUST | Section 7.2 |
| R12 | Server-provided nonces MUST be unpredictable | MUST | Section 8 |
| R13 | Authorization server MUST reject request if `dpop_jkt` thumbprint doesn't match | MUST | Section 10 |
| R14 | Server MUST NOT accept DPoP proof without nonce if nonce was provided | MUST | Section 11.3 |
| R15 | Servers MUST accept only DPoP proofs within limited time window | MUST | Section 11.1 |
| R16 | `alg` MUST NOT be `none` or symmetric | MUST | Section 11.6 |
| R17 | Use of HTTPS is REQUIRED | MUST | Section 2 |