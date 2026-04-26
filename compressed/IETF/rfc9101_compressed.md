# RFC 9101: The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)
**Source**: IETF (Internet Engineering Task Force) | **Version**: Standards Track | **Date**: August 2021 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9101

## Scope (Summary)
Defines the use of JSON Web Tokens (JWTs) for OAuth 2.0 authorization requests, enabling signed and/or encrypted request objects to provide integrity, source authentication, and confidentiality. Requests can be passed by value (via the `request` parameter) or by reference (via the `request_uri` parameter).

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750, October 2012.
- [RFC7230] Fielding, R., Ed. and J. Reschke, Ed., "Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing", RFC 7230, June 2014.
- [RFC7515] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015.
- [RFC7516] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, May 2015.
- [RFC7518] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015.
- [RFC7519] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, May 2015.
- [RFC7525] Sheffer, Y., Holz, R., and P. Saint-Andre, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525, May 2015.
- [RFC8141] Saint-Andre, P. and J. Klensin, "Uniform Resource Names (URNs)", RFC 8141, April 2017.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017.
- [RFC8414] Jones, M., Sakimura, N., and J. Bradley, "OAuth 2.0 Authorization Server Metadata", RFC 8414, June 2018.

## Definitions and Abbreviations
- **Request Object**: A JWT whose JWT Claims Set holds the JSON-encoded OAuth 2.0 authorization request parameters (Section 2.1).
- **Request Object URI**: An absolute URI that references the set of parameters comprising an OAuth 2.0 authorization request. The content of the resource referenced by the URI is a Request Object, unless the URI was provided to the client by the same authorization server, in which case the content is an implementation detail (Section 2.2).
- **JSON**: JavaScript Object Notation
- **JWT**: JSON Web Token
- **JWS**: JSON Web Signature
- **JWE**: JSON Web Encryption
- **URI**: Uniform Resource Identifier
- **URL**: Uniform Resource Locator

## 4. Request Object
- A Request Object MUST contain all parameters (including extension parameters) used to process the OAuth 2.0 authorization request except the `request` and `request_uri` parameters defined in this document.
- Parameter names and string values MUST be included as JSON strings, encoded using UTF-8 [RFC3629]. Numerical values MUST be included as JSON numbers.
- The Request Object MAY include any extension parameters.
- To sign, JWS [RFC7515] is used. If signed, the Request Object SHOULD contain the Claims `iss` (issuer) and `aud` (audience) as defined in JWT [RFC7519]. The value of `aud` should be the value of the authorization server (AS) `issuer`, as defined in RFC 8414.
- To encrypt, JWE [RFC7516] is used. When both signature and encryption are applied, the JWT MUST be signed, then encrypted, as described in Section 11.2 of [RFC7519] (Nested JWT).
- The client determines the algorithms used. Algorithms must be supported by both client and authorization server. Client metadata `request_object_signing_alg`, `request_object_encryption_alg`, `request_object_encryption_enc`; server metadata `request_object_signing_alg_values_supported`, etc.
- `request` and `request_uri` parameters MUST NOT be included in Request Objects.
- Media type: `application/oauth-authz-req+jwt`. (Some deployments may use `application/jwt`.)

## 5. Authorization Request
- The client constructs the authorization request URI by adding parameters to the query component of the authorization endpoint URI (application/x-www-form-urlencoded).
- **`request`**: REQUIRED unless `request_uri` is specified. The Request Object containing authorization request parameters stated in Section 4 of [RFC6749]. If present, `request_uri` MUST NOT be present.
- **`request_uri`**: REQUIRED unless `request` is specified. The absolute URI (as defined by RFC 3986) that is the Request Object URI referencing authorization request parameters. If present, `request` MUST NOT be present.
- **`client_id`**: REQUIRED. MUST match the `client_id` claim in the Request Object.
- The Authorization Request Object MUST be either (a) JWS signed, or (b) JWS signed and JWE encrypted.
- The client MAY send parameters duplicated in query parameters for backward compatibility, but the authorization server supporting this specification MUST only use the parameters included in the Request Object.

### 5.1. Passing a Request Object by Value
- The client sends the authorization request as a Request Object as the `request` parameter value.

### 5.2. Passing a Request Object by Reference
- The entire Request URI SHOULD NOT exceed 512 ASCII characters.
- The contents of the resource referenced by the `request_uri` MUST be a Request Object and MUST be reachable by the authorization server unless the URI was provided to the client by the authorization server.
- In the first case (client-provided URI), the `request_uri` MUST be an `https` URI (Section 2.7.2 of [RFC7230]). In the second case (AS-provided URI), it MUST be a URN (RFC 8141).

#### 5.2.3. Authorization Server Fetches Request Object
- Upon receipt, the authorization server MUST send an HTTP GET request to the `request_uri` to retrieve the referenced Request Object unless it can retrieve it through other mechanisms securely.

## 6. Validating JWT-Based Requests
### 6.1. JWE Encrypted Request Object
- The authorization server MUST decrypt the JWT per JSON Web Encryption [RFC7516]. If decryption fails, return `invalid_request_object` error.

### 6.2. JWS-Signed Request Object
- The authorization server MUST validate the signature of the JWS-signed [RFC7515] Request Object.
- If a `kid` header is present, the key identified MUST be used and MUST be associated with the client.
- The signature MUST be validated using a key associated with the client and the algorithm specified in the `alg` header.
- Algorithm verification MUST be performed per Sections 3.1 and 3.2 of [RFC8725].
- If the key is not associated or signature validation fails, return `invalid_request_object` error.

### 6.3. Request Parameter Assembly and Validation
- The authorization server MUST extract the set of authorization request parameters from the Request Object value.
- The server MUST only use the parameters in the Request Object, even if the same parameter is provided in the query parameter.
- The `client_id` values in the request parameter and in the Request Object MUST be identical.
- If validation fails, the server MUST return an error per Section 5.2 of [RFC6749].

## 7. Authorization Server Response
- Authorization server response as in Section 4 of [RFC6749].
- Additional error values:
  - `invalid_request_uri`: The `request_uri` returns an error or contains invalid data.
  - `invalid_request_object`: The request parameter contains an invalid Request Object.
  - `request_not_supported`: The AS does not support the `request` parameter.
  - `request_uri_not_supported`: The AS does not support the `request_uri` parameter.

## 8. TLS Requirements
- Client implementations supporting Request Object URI method MUST support TLS, following [RFC7525].
- Confidentiality protection MUST be applied using TLS with a cipher suite that provides confidentiality and integrity protection.
- HTTP clients MUST verify the TLS server certificate, using DNS-ID [RFC6125].
  - Support for DNS-ID identifier type is REQUIRED.
  - DNS names may contain wildcard character "*".
  - Clients MUST NOT use CN-ID identifiers.
  - SRV-ID and URI-ID MUST NOT be used for comparison.

## 9. IANA Considerations
(Summarized: Registrations of OAuth parameters `iss`, `sub`, `aud`, `exp`, `nbf`, `iat`, `jti` as authorization request parameters; metadata `require_signed_request_object` for both AS and client metadata; media type `application/oauth-authz-req+jwt`.)

## 10. Security Considerations
- In addition to OAuth 2.0 security [RFC6819], consider [RFC7515], [RFC7516], [RFC7518], [RFC8725].

### 10.1. Choice of Algorithms
- When sending the Authorization Request Object through the `request` parameter, it MUST be either signed using JWS or signed and then encrypted using JWS and JWE, with appropriate algorithms.

### 10.2. Request Source Authentication
- The source of the authorization request MUST always be verified.
- Methods: (a) Verifying JWS Signature; (b) Verifying symmetric key for JWE if symmetric encryption; (c) Verifying TLS Server Identity of Request Object URI (but not reliable in general); (d) When AS returns a Request Object URI, it MUST perform client authentication, validate signature, and ensure short lifetime and sufficient entropy (recommended <1 minute, at least 128 bits random); (e) When trusted third party returns URI, it MUST validate signature and the AS must trust the third party.

### 10.3. Explicit Endpoints
- RECOMMENDED to explicitly state endpoints (protected_resources, authorization_endpoint, redirect_uri, token_endpoint) in tamper-evident manner.

### 10.4. Risks Associated with request_uri
- DDoS: Server should check URI not unexpected, check media type `application/oauth-authz-req+jwt`, implement timeout, not perform recursive GET.
- Request URI Rewrite: Server should check URI not unexpected, check media type, implement timeout.

### 10.5. Downgrade Attack
- Defines client and server metadata `require_signed_request_object` (boolean). When client metadata is `true`, server MUST reject non-conforming requests and reject `alg` value `none`. When server metadata is `true`, MUST reject non-conforming requests from any client and reject `alg` `none`. Default is `false`.

### 10.6. TLS Security Considerations
- Follow [RFC7525] superseding TLS version recommendations in [RFC6749].

### 10.7. Parameter Mismatches
- The two client ID values MUST match, only parameter values from Request Object are to be used, and neither `request` nor `request_uri` can appear in a Request Object.

### 10.8. Cross-JWT Confusion
- Apply mitigations from [RFC8725]. A simple prevention: never use the client ID as the `sub` value in a Request Object. Another method: use explicit typing with `typ` header `oauth-authz-req+jwt` (registered). Note that requiring explicit typing may break existing deployments. Also use key management where keys for Request Objects are distinct.

## 11. Privacy Considerations
- Should follow [RFC6973].

### 11.1. Collection Limitation
- Client SHOULD limit collection of personal data to that strictly necessary.
- A trusted third-party service can certify requests. When using such service, the AS MUST verify the authority portion of the Request Object URI, verify TLS server identity, and obtain the Request Object which includes `client_id`. The consent screen MUST indicate the client and SHOULD indicate that the request has been vetted.

### 11.2. Disclosure Limitation
#### 11.2.1. Request Disclosure
- If authorization request contains potentially sensitive parameters, the client SHOULD encrypt the Request Object using JWE.
- Where Request Object URI method is used, if sensitive information is included, the `request_uri` SHOULD be used only once and have short validity, and MUST have sufficient entropy (recommended <1 minute, at least 128 bits) unless the Request Object itself is encrypted.

#### 11.2.2. Tracking Using Request Object URI
- Per-user persistent Request Object URIs should be avoided; single-use URIs are an alternative.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Request Object MUST contain all authorization request parameters except `request` and `request_uri`. | MUST | Section 4 |
| R2 | Parameter names and string values MUST be JSON strings encoded in UTF-8; numbers as JSON numbers. | MUST | Section 4 |
| R3 | When both signed and encrypted, the JWT MUST be signed then encrypted (Nested JWT). | MUST | Section 4 |
| R4 | `request` and `request_uri` parameters MUST NOT be included in Request Objects. | MUST | Section 4 |
| R5 | The `request` parameter is REQUIRED unless `request_uri` is specified. | MUST | Section 5 |
| R6 | The `request_uri` parameter is REQUIRED unless `request` is specified. | MUST | Section 5 |
| R7 | `client_id` in the authorization request MUST match the `client_id` claim in the Request Object. | MUST | Section 5 |
| R8 | The Authorization Request Object MUST be either JWS signed or JWS signed and JWE encrypted. | MUST | Section 5 |
| R9 | The authorization server MUST only use parameters from the Request Object, even if duplicated in query. | MUST | Section 6.3 |
| R10 | Upon decryption failure of JWE, return `invalid_request_object` error. | MUST | Section 6.1 |
| R11 | Validate JWS signature using key associated with client; algorithm verification per RFC 8725. | MUST | Section 6.2 |
| R12 | If signature validation fails, return `invalid_request_object` error. | MUST | Section 6.2 |
| R13 | Client implementations supporting Request Object URI MUST support TLS (RFC 7525). | MUST | Section 8 |
| R14 | Confidentiality protection MUST be applied using TLS. | MUST | Section 8 |
| R15 | HTTP clients MUST verify TLS server certificate using DNS-ID. | MUST | Section 8 |
| R16 | The source of the authorization request MUST always be verified (see 10.2 methods). | MUST | Section 10.2 |
| R17 | When sending request via `request` parameter, it MUST be signed or signed+encrypted with appropriate algorithms. | MUST | Section 10.1 |
| R18 | If client metadata `require_signed_request_object` is true, server MUST reject non-conforming requests. | MUST | Section 10.5 |
| R19 | If server metadata `require_signed_request_object` is true, server MUST reject non-conforming requests from any client. | MUST | Section 10.5 |
| R20 | The two client ID values MUST match; only Request Object parameters used; `request`/`request_uri` not in Request Object. | MUST | Section 10.7 |
| R21 | For sensitive data in Request Object URI, the URI MUST have sufficient entropy and likely short validity unless encrypted. | MUST (entropy) / SHOULD (short validity) | Section 11.2.1 |