# RFC 7636: Proof Key for Code Exchange by OAuth Public Clients
**Source**: Internet Engineering Task Force (IETF) | **Version**: RFC 7636 (Standards Track) | **Date**: September 2015 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7636

## Scope (Summary)
This specification describes the authorization code interception attack against OAuth 2.0 public clients using the Authorization Code Grant and defines Proof Key for Code Exchange (PKCE, pronounced "pixy") to mitigate the threat. PKCE uses a dynamically created cryptographically random key called "code verifier" to bind the authorization code to the client.

## Normative References
- [BCP195] Sheffer, Y., Holz, R., and P. Saint-Andre, "Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)", BCP 195, RFC 7525, May 2015.
- [RFC20] Cerf, V., "ASCII format for network interchange", STD 80, RFC 20, October 1969.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, October 2006.
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.
- [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC6234] Eastlake 3rd, D. and T. Hansen, "US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)", RFC 6234, May 2011.
- [RFC6749] Hardt, D., Ed., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.

## Definitions and Abbreviations
- **code verifier**: A cryptographically random string that is used to correlate the authorization request to the token request.
- **code challenge**: A challenge derived from the code verifier that is sent in the authorization request, to be verified against later.
- **code challenge method**: A method that was used to derive code challenge.
- **Base64url Encoding**: Base64 encoding using the URL- and filename-safe character set defined in Section 5 of [RFC4648], with all trailing '=' characters omitted (as permitted by Section 3.2 of [RFC4648]) and without inclusion of line breaks, whitespace, or other additional characters.
- **Abbreviations**: ABNF (Augmented Backus-Naur Form), Authz (Authorization), PKCE (Proof Key for Code Exchange), MITM (Man-in-the-middle), MTI (Mandatory To Implement).

## 1. Introduction
OAuth 2.0 public clients are susceptible to the authorization code interception attack. The attacker intercepts the authorization code in a communication path not protected by TLS (e.g., inter-application communication within the client's OS). Once the attacker has the code, it can obtain the access token.

**Pre-conditions for the attack**:
1. The attacker manages to register a malicious application on the client device and registers a custom URI scheme also used by another application. The OS must allow a custom URI scheme to be registered by multiple applications.
2. The OAuth 2.0 authorization code grant is used.
3. The attacker has access to the `client_id` and `client_secret` (if provisioned). All native app client-instances use the same `client_id`; secrets are not confidential.
4. Either:
   - 4a. The attacker can observe only the responses from the authorization endpoint. ("plain" method mitigates this.)
   - 4b. The attacker can observe requests (in addition to responses) to the authorization endpoint but is not a man-in-the-middle. To mitigate this, `code_challenge_method` MUST be set to "S256" or a cryptographically secure extension.

This extension mitigates the attack by using a dynamically created cryptographically random key called "code verifier". A unique code verifier is created for every authorization request; its transformed value ("code challenge") is sent to the authorization server to obtain the authorization code. The code and verifier are later sent to the token endpoint; the server transforms and compares.

### 1.1 Protocol Flow
- **A**: Client creates and records `code_verifier`, derives `code_challenge = t(code_verifier)`, sends in Authorization Request with transformation method `t_m`.
- **B**: Authorization Endpoint responds as usual but records `t(code_verifier)` and transformation method.
- **C**: Client sends authorization code in Access Token Request along with `code_verifier`.
- **D**: Authorization server transforms `code_verifier` and compares to recorded `t(code_verifier)`. Access is denied if not equal.

## 2. Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in [RFC2119].
- STRING: sequence of zero or more ASCII characters.
- OCTETS: sequence of zero or more octets.
- ASCII(STRING): octets of ASCII representation.
- BASE64URL-ENCODE(OCTETS): base64url encoding per Appendix A, producing a STRING.
- BASE64URL-DECODE(STRING): base64url decoding per Appendix A.
- SHA256(OCTETS): SHA2 256-bit hash [RFC6234].

## 4. Protocol
### 4.1 Client Creates a Code Verifier
- **R1 (shall)**: `code_verifier` MUST be a high-entropy cryptographic random STRING using the unreserved characters `[A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~"` from Section 2.3 of [RFC3986], with a minimum length of 43 characters and a maximum length of 128 characters.
  - ABNF: `code-verifier = 43*128unreserved`
- **R2 (should/recommended)**: The code verifier SHOULD have enough entropy to be impractical to guess. It is RECOMMENDED to use a 32-octet random sequence base64url-encoded to produce a 43-octet URL-safe string.

### 4.2 Client Creates the Code Challenge
- **R3 (shall)**: If the client is capable of using "S256", it MUST use "S256".
- **R4 (shall)**: "S256" is Mandatory To Implement (MTI) on the server.
- **R5 (may)**: Clients MAY use "plain" only if they cannot support "S256" for some technical reason and know via out-of-band configuration that the server supports "plain".
- Transformations:
  - `plain`: `code_challenge = code_verifier`
  - `S256`: `code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))`
- ABNF: `code-challenge = 43*128unreserved`

### 4.3 Client Sends Code Challenge with Authorization Request
- **R6 (required)**: `code_challenge` parameter is REQUIRED.
- **R7 (optional)**: `code_challenge_method` parameter is OPTIONAL, defaults to "plain" if not present. Values: "S256" or "plain".

### 4.4 Server Returns the Code
- **R8 (shall)**: When issuing the authorization code, the server MUST associate the `code_challenge` and `code_challenge_method` values with the authorization code so it can be verified later.
- **R9 (shall)**: The server MUST NOT include the `code_challenge` value in client requests in a form that other entities can extract.
- The method of association is out of scope.

#### 4.4.1 Error Response
- **R10 (shall)**: If the server requires PKCE and the client does not send `code_challenge` in the request, the authorization endpoint MUST return an error with `error` value set to `"invalid_request"`. The `error_description` or `error_uri` SHOULD explain the nature of error (e.g., "code challenge required").
- **R11 (shall)**: If the server does not support the requested transformation, the authorization endpoint MUST return an error with `error` value set to `"invalid_request"`. The `error_description` or `error_uri` SHOULD explain (e.g., "transform algorithm not supported").

### 4.5 Client Sends Authorization Code and Code Verifier to Token Endpoint
- **R12 (required)**: `code_verifier` parameter is REQUIRED in the Access Token Request.
- **R13 (shall)**: The `code_challenge_method` is bound to the Authorization Code when issued; that is the method the token endpoint MUST use to verify the `code_verifier`.

### 4.6 Server Verifies code_verifier before Returning Tokens
- **R14 (shall)**: The server MUST verify by calculating the code challenge from the received `code_verifier` and comparing it with the previously associated `code_challenge`, after transforming according to the `code_challenge_method`.
  - If method was "S256": `BASE64URL-ENCODE(SHA256(ASCII(code_verifier))) == code_challenge`.
  - If method was "plain": `code_verifier == code_challenge`.
- **R15 (shall)**: If the values are equal, the token endpoint MUST continue processing as normal per OAuth 2.0 [RFC6749].
- **R16 (shall)**: If the values are not equal, an error response with `"invalid_grant"` as described in Section 5.2 of [RFC6749] MUST be returned.

## 5. Compatibility
- **R17 (may)**: Server implementations MAY accept OAuth 2.0 clients that do not implement this extension. If `code_verifier` is not received, servers supporting backwards compatibility revert to OAuth 2.0 without this extension.
- **R18 (should)**: Client implementations SHOULD send the additional parameters as defined in Section 4 to all servers, as server responses are unchanged by this specification.

## 6. IANA Considerations
- **OAuth Parameters Registry**: Registered parameters:
  - `code_verifier` (token request, change controller: IESG)
  - `code_challenge` (authorization request, change controller: IESG)
  - `code_challenge_method` (authorization request, change controller: IESG)
- **PKCE Code Challenge Method Registry**: New sub-registry of "OAuth Parameters". Registration uses Specification Required policy [RFC5226] with review by Designated Experts. Names should be short (≤8 characters). Initial contents:
  - **plain**: Change Controller IESG, Specification: Section 4.2 of RFC 7636.
  - **S256**: Change Controller IESG, Specification: Section 4.2 of RFC 7636.

## 7. Security Considerations
- **R19 (shall)**: Clients MUST NOT downgrade to "plain" after trying the "S256" method.
- **R20 (should)**: "plain" SHOULD NOT be used in new implementations unless they cannot support "S256" for some technical reason.
- **R21 (should)**: The "S256" code challenge method or other cryptographically secure extension SHOULD be used. The "plain" method relies on the OS and transport security not to disclose the request.
- **R22 (shall)**: If the code challenge method is "plain" and the code challenge is returned inside the authorization code (for stateless server), it MUST be encrypted such that only the server can decrypt.
- **Entropy**: code_verifier SHOULD have minimum 256 bits of entropy. A 32-octet random sequence base64url-encoded provides this.
- **OAuth Security Considerations**: All security analysis from [RFC6819] applies; readers SHOULD follow it carefully.
- **TLS Security**: Current recommendations are in [BCP195], superseding the TLS version recommendations in [RFC6749].

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | code_verifier MUST be high-entropy cryptographic random STRING using unreserved characters, min 43, max 128 characters. | shall | Section 4.1 |
| R2 | code_verifier SHOULD have enough entropy; RECOMMENDED 32-octet sequence base64url-encoded. | should/recommended | Section 4.1 |
| R3 | If client is capable of using "S256", it MUST use "S256". | shall | Section 4.2 |
| R4 | "S256" is Mandatory To Implement (MTI) on the server. | shall | Section 4.2 |
| R5 | Clients MAY use "plain" only if they cannot support "S256" and know server supports "plain". | may | Section 4.2 |
| R6 | code_challenge is REQUIRED in authorization request. | required | Section 4.3 |
| R7 | code_challenge_method is OPTIONAL, defaults to "plain". | optional | Section 4.3 |
| R8 | Server MUST associate code_challenge and code_challenge_method with authorization code. | shall | Section 4.4 |
| R9 | Server MUST NOT include code_challenge in client requests in extractable form. | shall | Section 4.4 |
| R10 | If server requires PKCE and client does not send code_challenge, authorization endpoint MUST return error "invalid_request". | shall | Section 4.4.1 |
| R11 | If server does not support requested transformation, authorization endpoint MUST return error "invalid_request". | shall | Section 4.4.1 |
| R12 | code_verifier is REQUIRED in Access Token Request. | required | Section 4.5 |
| R13 | Token endpoint MUST use the code_challenge_method bound to authorization code for verification. | shall | Section 4.5 |
| R14 | Server MUST verify by calculating code challenge from received code_verifier and comparing to associated code_challenge per the method. | shall | Section 4.6 |
| R15 | If values equal, token endpoint MUST continue processing as normal. | shall | Section 4.6 |
| R16 | If values not equal, MUST return error "invalid_grant". | shall | Section 4.6 |
| R17 | Server implementations MAY accept clients not implementing this extension (backwards compatibility). | may | Section 5 |
| R18 | Client implementations SHOULD send additional parameters to all servers. | should | Section 5 |
| R19 | Clients MUST NOT downgrade to "plain" after trying "S256". | shall | Section 7.2 |
| R20 | "plain" SHOULD NOT be used in new implementations unless unable to support "S256". | should | Section 7.2 |
| R21 | "S256" or other cryptographically secure method SHOULD be used. | should | Section 7.2 |
| R22 | If "plain" and code challenge inside authorization code, it MUST be encrypted server-side only. | shall | Section 7.2 |

## Informative Annexes (Condensed)
- **Appendix A – Base64url Encoding without Padding**: Describes how to implement base64url encoding by removing trailing '=' and replacing '+' with '-' and '/' with '_'. Includes example C# code and an encoded/decoded example.
- **Appendix B – Example for S256**: Demonstrates the full flow: generates a 32-octet random sequence, base64url-encodes to create `code_verifier` (`dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk`), SHA256 hashes and base64url-encodes to create `code_challenge` (`E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM`). Shows the authorization request including `code_challenge` and `code_challenge_method=S256`, and the token request including `code_verifier`. On server, the verification step hashes and compares successfully.