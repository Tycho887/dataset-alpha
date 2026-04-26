# RFC 8705: OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens
**Source**: IETF | **Version**: RFC 8705 | **Date**: February 2020 | **Type**: Standards Track
**Original**: https://www.rfc-editor.org/info/rfc8705

## Scope (Summary)
This document defines two OAuth 2.0 extensions: mutual-TLS client authentication using X.509 certificates (PKI or self-signed) and certificate-bound access/refresh tokens. It provides methods for binding tokens to client certificates and verifying that binding at resource servers.

## Normative References
- [BCP195] – Recommendations for Secure Use of TLS and DTLS (RFC 7525)
- [RFC2119] – Key words for requirement levels
- [RFC4514] – LDAP: String Representation of Distinguished Names
- [RFC4648] – Base16, Base32, Base64 Data Encodings
- [RFC5246] – TLS 1.2
- [RFC5280] – X.509 PKI Certificate and CRL Profile
- [RFC6749] – OAuth 2.0 Authorization Framework
- [RFC6750] – OAuth 2.0 Bearer Token Usage
- [RFC7517] – JSON Web Key (JWK)
- [RFC7519] – JSON Web Token (JWT)
- [RFC7591] – OAuth 2.0 Dynamic Client Registration Protocol
- [RFC7662] – OAuth 2.0 Token Introspection
- [RFC7800] – Proof-of-Possession Key Semantics for JWTs
- [RFC8174] – Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [RFC8414] – OAuth 2.0 Authorization Server Metadata
- [RFC8446] – TLS 1.3
- [SHS] – Secure Hash Standard (FIPS PUB 180-4)
- [X690] – ASN.1 encoding rules

## Definitions and Abbreviations
- **mutual TLS**: TLS handshake where client presents X.509 certificate and proves possession of corresponding private key.
- **PKI Method**: Mutual-TLS client authentication using a trusted CA-issued certificate, validated by chain and subject DN/SAN.
- **Self-Signed Method**: Mutual-TLS client authentication using self-signed certificate, validated by matching registered public key (via JWK).
- **Certificate-Bound Access Token**: Access token whose usage is restricted to the TLS client certificate used during its issuance.
- **x5t#S256**: JWT Confirmation Method member; base64url-encoded SHA-256 hash of DER-encoded X.509 certificate.
- **Client_id**: Required parameter for mutual-TLS authentication to identify client.

## Section 1: Introduction (Summarized)
OAuth 2.0 allows delegated access. This RFC enhances security using mutual TLS: Section 2 provides client authentication options; Section 3 provides certificate-bound access tokens with local (JWT) and remote (introspection) verification. Mutual-TLS certificate-bound tokens prevent stolen token usage.

## Section 2: Mutual TLS for OAuth Client Authentication
- TLS connection between client and AS MUST be established with mutual-TLS X.509 certificate authentication.
- Client MUST include "client_id" parameter for all mutual-TLS requests.
- AS MUST enforce binding between client and certificate per methods below.
- On mismatch, AS returns error response with "invalid_client" per Section 5.2 of [RFC6749].

### 2.1 PKI Mutual-TLS Method
- Relies on validated certificate chain [RFC5280] and single subject DN or SAN.
- Only one subject name value used per client.
- AS validates private key possession and certificate chain.
- Revocation checking is deployment decision.
- Clients can rotate certificates by obtaining new cert with same subject from trusted CA.

#### 2.1.1 PKI Method Metadata Value
- **tls_client_auth**: Indicates mutual-TLS with PKI method.

#### 2.1.2 Client Registration Metadata
- Exactly one of the following MUST be used:
  - `tls_client_auth_subject_dn` (string, [RFC4514] representation)
  - `tls_client_auth_san_dns` (string, dNSName)
  - `tls_client_auth_san_uri` (string, uniformResourceIdentifier)
  - `tls_client_auth_san_ip` (string, IP address in dotted decimal or colon-delimited hex per [RFC5952]; comparison in binary)
  - `tls_client_auth_san_email` (string, rfc822Name)

### 2.2 Self-Signed Certificate Mutual-TLS Method
- Client registers X.509 certificates using `jwks` or `jwks_uri` from [RFC7591].
- Certificate chain not validated; AS checks that presented certificate matches registered certificate.
- Allows rotation via `jwks_uri` without direct metadata update.

#### 2.2.1 Self-Signed Method Metadata Value
- **self_signed_tls_client_auth**: Indicates mutual-TLS with self-signed certificate.

#### 2.2.2 Client Registration Metadata
- Uses `jwks_uri` or `jwks` parameters; certificate represented via `x5c` member in JWK. JWK key members (e.g., n, e) required per [RFC7518].

## Section 3: Mutual-TLS Client Certificate-Bound Access Tokens
- AS can bind access token to client certificate used at token endpoint.
- Binding accomplished by embedding certificate hash in token (Section 3.1) or via introspection (Section 3.2).
- For resource server to use certificate-bound tokens, it must know mutual TLS is required (AS policy out of scope).
- Client MUST use same certificate for mutual TLS on token endpoint and resource access.
- Resource server MUST obtain client certificate from TLS layer and verify it matches token binding; mismatch results in HTTP 401 "invalid_token".

### 3.1 JWT Certificate Thumbprint Confirmation Method
- When access tokens are JWTs, certificate hash SHOULD be represented using `x5t#S256` member.
- `x5t#S256`: base64url-encoded SHA-256 hash of DER encoding of X.509 certificate; omit pad '='; no line breaks.
- Example payload shown.

### 3.2 Confirmation Method for Token Introspection
- For certificate-bound tokens, introspection response includes `cnf` with `x5t#S256` member.
- Resource server compares hash to client certificate hash; reject if mismatch.

### 3.3 Authorization Server Metadata
- `tls_client_certificate_bound_access_tokens`: OPTIONAL boolean; default false. Indicates AS support for certificate-bound tokens.

### 3.4 Client Registration Metadata
- `tls_client_certificate_bound_access_tokens`: OPTIONAL boolean; default false. Indicates client intention to use certificate-bound tokens.
- If client requests token over non-mutual-TLS connection, AS discretion to issue unbound token or error.

## Section 4: Public Clients and Certificate-Bound Tokens
- Certificate-bound tokens can be used without mutual-TLS client authentication.
- Public client creates self-signed certificate; AS does not authenticate client via certificate but binds token to it.
- Refresh token SHOULD also be bound to certificate (implementation details at AS discretion).

## Section 5: Metadata for Mutual-TLS Endpoint Aliases
- `mtls_endpoint_aliases`: OPTIONAL JSON object containing alternative endpoints (e.g., token_endpoint, revocation_endpoint, introspection_endpoint).
- Client intending mutual TLS MUST use alias URLs when present; otherwise use conventional endpoints.
- Non-endpoint parameters in aliases SHOULD be ignored.
- Example provided.

## Section 6: Implementation Considerations (Summarized)
- **6.1 AS**: Configure TLS for mutual TLS; for self-signed method, do not verify CA; consider separate host/port for endpoints to avoid impact on other clients.
- **6.2 Resource Server**: Does not need to validate client certificate chain; mutual TLS serves as proof-of-possession.
- **6.3 Certificate Expiration**: Token invalid when certificate updated; client should request new token (e.g., via refresh token).
- **6.4 Implicit Grant Unsupported**: Binding tokens from implicit grant is out of scope.
- **6.5 TLS Termination**: May terminate at intermediary; secure propagation of client certificate metadata is out of scope.

## Section 7: Security Considerations (Summarized)
- **7.1**: Refresh tokens are indirectly certificate-bound for confidential clients via authentication; Section 4 covers public clients.
- **7.2**: SHA-256 used for thumbprint; second-preimage resistance required; future hash functions should define new JWT confirmation members.
- **7.3**: Applicable with TLS versions supporting certificate-based client auth; TLS 1.2 and 1.3 referenced; validation requires trusted CA database (out of scope).
- **7.4**: PKI method: AS SHOULD limit trust anchors to prevent certificate spoofing.
- **7.5**: X.509 parsing and validation complexity; implementors SHOULD use established libraries, not write own validation.

## Section 8: Privacy Considerations (Summarized)
- In TLS <1.3, client certificate sent unencrypted; may enable tracking for single-user clients; use TLS 1.3 when possible.

## Section 9: IANA Considerations
- **9.1**: JWT Confirmation Method "x5t#S256" registered.
- **9.2**: Authorization Server Metadata "tls_client_certificate_bound_access_tokens", "mtls_endpoint_aliases" registered.
- **9.3**: Token Endpoint Authentication Methods "tls_client_auth", "self_signed_tls_client_auth" registered.
- **9.4**: Token Introspection Response "cnf" registered.
- **9.5**: Dynamic Client Registration Metadata: "tls_client_certificate_bound_access_tokens", "tls_client_auth_subject_dn", "tls_client_auth_san_dns", "tls_client_auth_san_uri", "tls_client_auth_san_ip", "tls_client_auth_san_email" registered.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|------------|------|-----------|
| R1 | TLS connection for mutual-TLS client auth MUST be established/re-established with mutual-TLS X.509 cert auth | MUST | Section 2 |
| R2 | Client MUST include "client_id" parameter in all requests using mutual-TLS client auth | MUST | Section 2 |
| R3 | AS MUST enforce binding between client and certificate | MUST | Section 2 |
| R4 | For PKI method, exactly one of the five subject metadata parameters MUST be used | MUST | Section 2.1.2 |
| R5 | Client using "self_signed_tls_client_auth" MUST register certificate via "jwks" or "jwks_uri" | MUST | Section 2.2.2 |
| R6 | For certificate-bound tokens, client MUST use same certificate for mutual TLS at token endpoint and resource access | MUST | Section 3 |
| R7 | Resource server MUST verify certificate matches token binding; if not, reject with 401 "invalid_token" | MUST | Section 3 |
| R8 | When access tokens are JWTs, certificate hash SHOULD be represented with "x5t#S256" | SHOULD | Section 3.1 |
| R9 | For introspection, AS includes "cnf" with "x5t#S256" in response | (implied by spec) | Section 3.2 |
| R10 | Client intending mutual TLS MUST use alias endpoints from "mtls_endpoint_aliases" when present | MUST | Section 5 |
| R11 | AS SHOULD limit trust anchors for PKI method to prevent spoofing | SHOULD | Section 7.4 |
| R12 | Implementors SHOULD use established X.509 libraries | SHOULD | Section 7.5 |

## Informative Annexes (Condensed)
- **Appendix A**: Provides example "x5t#S256" claim, PEM-encoded self-signed certificate, and JWK representation.
- **Appendix B**: Compares to Token Binding [TOKEN]; mutual TLS is currently more deployable; both may coexist.
- **Acknowledgements**: Lists contributors.