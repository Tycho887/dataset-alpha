# RFC 9700: Best Current Practice for OAuth 2.0 Security
**Source**: IETF | **Version**: BCP 240 | **Date**: January 2025 | **Type**: Best Current Practice (Normative)
**Original**: https://www.rfc-editor.org/info/rfc9700

## Scope (Summary)
This document describes best current security practices for OAuth 2.0, updating and extending the threat model and security advice from RFCs 6749, 6750, and 6819. It addresses new threats from broader OAuth deployment, deprecates less secure modes, and provides detailed countermeasures for known attacks.

## Normative References
- [BCP195] – Deprecating TLS 1.0/1.1 (RFC 8996) and Recommendations for Secure Use of TLS/DTLS (RFC 9325)
- [RFC2119] – Key words for requirement levels
- [RFC3986] – URI Generic Syntax
- [RFC6749] – OAuth 2.0 Authorization Framework
- [RFC6750] – OAuth 2.0 Bearer Token Usage
- [RFC6819] – OAuth 2.0 Threat Model and Security Considerations
- [RFC7521] – Assertion Framework for OAuth 2.0
- [RFC7523] – JWT Profile for OAuth 2.0 Client Authentication
- [RFC7636] – Proof Key for Code Exchange (PKCE)
- [RFC8174] – Ambiguity of Key Words
- [RFC8252] – OAuth 2.0 for Native Apps
- [RFC8414] – OAuth 2.0 Authorization Server Metadata
- [RFC8705] – Mutual-TLS Client Authentication and Certificate-Bound Access Tokens
- [RFC9068] – JWT Profile for OAuth 2.0 Access Tokens

## Definitions and Abbreviations
- **Access Token**: as defined in [RFC6749]
- **Authorization Code Grant**: as defined in [RFC6749]
- **Authorization Server**: as defined in [RFC6749]
- **Client**: as defined in [RFC6749]
- **Open Redirector**: an endpoint on a web server that forwards a user's browser to an arbitrary URI obtained from a query parameter
- **PKCE**: Proof Key for Code Exchange [RFC7636]
- **Resource Owner**: as defined in [RFC6749]
- **Resource Server**: as defined in [RFC6749]

## Best Practices (Section 2)

### Protecting Redirect-Based Flows
- AS MUST use exact string matching for redirect URI comparison (except localhost port numbers for native apps) (Section 4.1.3)
- Clients and AS MUST NOT expose open redirectors (Section 4.11)
- Clients MUST prevent CSRF. PKCE or nonce (for OpenID Connect) may provide CSRF protection; otherwise, one-time use CSRF tokens in `state` MUST be used (Section 4.7.1)
- When client interacts with multiple AS, defense against mix-up attacks is REQUIRED. Clients SHOULD use `iss` parameter per [RFC9207] or alternative. Otherwise, distinct redirect URIs MAY be used (Section 4.4.2)
- AS MUST avoid forwarding user credentials via HTTP 307 redirect (Section 4.12)

#### Authorization Code Grant
- Clients MUST prevent authorization code injection. Public clients MUST use PKCE [RFC7636]. Confidential clients SHOULD use PKCE. OpenID Connect clients MAY use nonce with additional precautions (Section 4.5.3)
- PKCE challenge or nonce MUST be transaction-specific and securely bound to client and user agent
- Clients SHOULD use S256 code challenge method
- AS MUST support PKCE [RFC7636]
- AS MUST enforce `code_verifier` if `code_challenge` was sent
- AS MUST mitigate PKCE downgrade attacks (Section 4.8.2)
- AS MUST provide way to detect PKCE support (RECOMMENDED via AS Metadata `code_challenge_methods_supported`)

#### Implicit Grant (response_type token)
- Clients SHOULD NOT use implicit grant unless access token injection is prevented and leakage mitigated
- Clients SHOULD use response type code (authorization code) or other response types that issue tokens only in token response

### Token Replay Prevention
- AS and RS SHOULD use sender-constrained access tokens (mutual TLS [RFC8705] or DPoP [RFC9449]) (Section 4.10.1)
- Refresh tokens for public clients MUST be sender-constrained or use rotation (Section 4.14.2)

### Access Token Privilege Restriction
- Access tokens SHOULD be restricted to minimum privileges. SHOULD be audience-restricted to specific RS. RS MUST refuse if audience mismatch (Section 4.10.2)
- Access tokens SHOULD be restricted to specific resources/actions

### Resource Owner Password Credentials Grant
- The resource owner password credentials grant MUST NOT be used (Section 2.4)

### Client Authentication
- AS SHOULD enforce client authentication where feasible. RECOMMENDED to use asymmetric cryptography (mutual TLS or signed JWTs) (Section 2.5)

### Other Recommendations
- RECOMMENDED to use OAuth Authorization Server Metadata [RFC8414] (Section 2.6)
- AS SHOULD NOT allow clients to influence `client_id` to cause confusion with resource owner (Section 4.15.1)
- RECOMMENDED end-to-end TLS [BCP195] between client and RS
- Authorization responses MUST NOT be transmitted over unencrypted connections; AS MUST NOT allow `http` scheme redirect URIs except loopback for native apps (Section 2.6)
- If in-browser communication (e.g., postMessage) is used, both initiator and receiver MUST be strictly verified (Section 4.17)
- CORS MAY be supported at token endpoint, metadata endpoint, jwks_uri, DCR endpoint, but MUST NOT be supported at authorization endpoint (Section 2.6)

## The Updated OAuth 2.0 Attacker Model (Section 3)
- **(A1) Web attacker**: can set up/operate network endpoints (honest & attacker), own user agents, participate in protocol, lure users to arbitrary URIs. Cannot read/manipulate messages not targeted to them.
- **(A2) Network attacker**: full control over network (eavesdrop, manipulate, spoof) except messages protected by cryptography (e.g., TLS). Can block messages.
- **(A3) Attacker can read (but not modify) authorization response** (e.g., via open redirector, mix-up, insufficient redirect URI checking, browser history/proxy).
- **(A4) Attacker can read authorization request** (similar leakage).
- **(A5) Attacker can acquire issued access token** (e.g., compromised RS, misconfiguration, social engineering).

Implementers MUST consider all types of attackers in their environment.

## Attacks and Mitigations (Section 4)

### 4.1 Insufficient Redirection URI Validation
- **Attack**: Pattern matching errors allow authorization code/access token leakage to attacker-controlled URI or via open redirector + fragment reattachment.
- **Countermeasure**: Exact string matching (Section 4.1.3). Additional: no open redirectors, use fragment attachment prevention, use authorization code grant.

### 4.2 Credential Leakage via Referer Headers
- **Attack**: Authorization code/state/access token leaked via Referer header from AS or client page.
- **Countermeasures**: Page rendered after authorization response SHOULD NOT include third-party resources. Use Referrer-Policy header, use authorization code grant, bind code to PKCE, invalidate codes after use, invalidate state after first use, use form post response mode.

### 4.3 Credential Leakage via Browser History
- **Attack**: Code/access token stored in browser history.
- **Countermeasures**: Code replay prevention (PKCE), use form post; access tokens MUST NOT be passed in URI query parameters (Section 2.3 of [RFC6750]).

### 4.4 Mix-Up Attacks
- **Attack**: Client interacting with multiple AS; attacker intercepts authorization response to obtain code/token.
- **Countermeasure (4.4.2)**: Clients MUST prevent mix-up. Options: use `iss` parameter per [RFC9207] (preferred) or distinct redirect URIs per issuer. Client MUST store issuer for each request and compare upon response; abort if mismatch.

### 4.5 Authorization Code Injection
- **Attack**: Attacker injects stolen code into own session with client.
- **Countermeasures**: PKCE (Section 4.5.3.1) or nonce (Section 4.5.3.2) for confidential OpenID Connect clients. Also see limitations (Section 4.5.4).

### 4.6 Access Token Injection
- **Attack**: Attacker injects leaked access token into client via implicit grant.
- **Countermeasure**: No pure-OAuth detection; OpenID Connect mitigates via ID Token `at_hash`. Recommendations in Section 2.1.2 apply.

### 4.7 Cross-Site Request Forgery (CSRF)
- **Countermeasure**: CSRF token in `state` parameter. PKCE or nonce also provide CSRF protection. Clients MUST ensure AS supports PKCE if relying on it for CSRF.

### 4.8 PKCE Downgrade Attack
- **Attack**: Attacker removes `code_challenge` from request, then injects code without PKCE binding.
- **Countermeasure**: AS MUST reject token request with `code_verifier` if no `code_challenge` was present in authorization request.

### 4.9 Access Token Leakage at Resource Server
- **Attack**: Counterfeit RS or compromised RS.
- **Countermeasures**: Sender-constrained tokens (SHOULD), audience restriction (SHOULD), RS MUST treat tokens as sensitive.

### 4.10 Misuse of Stolen Access Tokens
- **Countermeasures**: Sender-constrained (Section 4.10.1) and audience-restricted (Section 4.10.2) access tokens. Authorization servers SHOULD implement these.

### 4.11 Open Redirection
- **Client**: MUST NOT expose open redirectors (Section 4.11.1)
- **Authorization Server**: MUST take precautions against phishing via open redirectors (Section 4.11.2); should not redirect automatically if URI untrusted.

### 4.12 307 Redirect
- AS MUST NOT use HTTP 307 for redirect after credential submission. SHOULD use 303.

### 4.13 TLS Terminating Reverse Proxies
- Reverse proxy MUST sanitize inbound headers, ensure authenticity/integrity of security-related headers. Communication between proxy and app server MUST be protected.

### 4.14 Refresh Token Protection
- AS MUST decide whether to issue refresh tokens based on risk assessment. If issued, MUST bind to scope and resource servers.
- For public clients, refresh tokens MUST be sender-constrained or use rotation.
- AS MAY revoke refresh tokens on password change or logout. Refresh tokens SHOULD expire after inactivity.

### 4.15 Client Impersonating Resource Owner
- AS SHOULD NOT allow clients to influence `client_id` that could confuse with resource owner. If unavoidable, AS MUST provide means for RS to distinguish.

### 4.16 Clickjacking
- AS MUST prevent clickjacking (X-Frame-Options, frame-busting, CSP level 2 or greater). CSP SHOULD be used on authentication endpoints.

### 4.17 Attacks on In-Browser Communication Flows
- AS MUST use exact origin matching for postMessage receivers. MUST NOT use wildcard origins.
- Clients MUST validate sender origin exactly.
- All protection measures from Section 2.1 apply.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | AS MUST use exact string matching for redirect URI validation (except localhost port) | MUST | 2.1, 4.1.3 |
| R2 | Clients and AS MUST NOT be open redirectors | MUST | 2.1, 4.11 |
| R3 | Clients MUST prevent CSRF. PKCE/nonce may be used; otherwise, one-time state tokens MUST be used | MUST | 2.1, 4.7.1 |
| R4 | When multiple AS, mix-up defense REQUIRED. Clients SHOULD use `iss` parameter per RFC 9207 | SHOULD/REQUIRED | 2.1, 4.4.2 |
| R5 | AS MUST NOT use HTTP 307 for redirect after credential submission | MUST NOT | 4.12 |
| R6 | Public clients MUST use PKCE for authorization code grant | MUST | 2.1.1 |
| R7 | Confidential clients SHOULD use PKCE | SHOULD | 2.1.1 |
| R8 | PKCE challenge/nonce MUST be transaction-specific and secure | MUST | 2.1.1 |
| R9 | AS MUST support PKCE | MUST | 2.1.1 |
| R10 | AS MUST enforce code_verifier if code_challenge sent | MUST | 2.1.1 |
| R11 | AS MUST mitigate PKCE downgrade attacks | MUST | 4.8.2 |
| R12 | AS MUST provide way to detect PKCE support (RECOMMENDED via metadata) | MUST/RECOMMENDED | 2.1.1 |
| R13 | Clients SHOULD NOT use implicit grant (response_type token) unless mitigated | SHOULD NOT | 2.1.2 |
| R14 | Authorization/resource servers SHOULD use sender-constrained access tokens | SHOULD | 2.2.1 |
| R15 | Refresh tokens for public clients MUST be sender-constrained or use rotation | MUST | 2.2.2 |
| R16 | Resource owner password credentials grant MUST NOT be used | MUST NOT | 2.4 |
| R17 | AS SHOULD enforce client authentication where feasible; RECOMMENDED asymmetric | SHOULD/RECOMMENDED | 2.5 |
| R18 | Authorization responses MUST NOT be transmitted unencrypted; AS MUST NOT allow http redirect URIs (except loopback native apps) | MUST/MUST NOT | 2.6 |
| R19 | If in-browser communication, both initiator and receiver MUST be strictly verified (exact origin matching) | MUST | 4.17.2 |
| R20 | AS MUST NOT support CORS at authorization endpoint | MUST NOT | 2.6 |
| R21 | AS MUST prevent clickjacking (X-Frame-Options, CSP, etc.) | MUST | 4.16 |
| R22 | AS MUST ensure token request with code_verifier is rejected if no code_challenge in auth request | MUST | 4.8.2 |
| R23 | Clients MUST NOT pass access tokens in URI query parameters | MUST NOT | 4.3.2 |
| R24 | Refresh tokens MUST be bound to scope and resource servers | MUST | 4.14.2 |
| R25 | AS SHOULD NOT allow clients to influence client_id to cause confusion with resource owner | SHOULD NOT | 4.15.1 |
| R26 | Reverse proxies MUST sanitize inbound headers and protect intra-network communication | MUST | 4.13 |
| R27 | RS MUST treat access tokens as sensitive secrets; not store/transfer in plaintext | MUST | 4.9.3 |
| R28 | RS MUST refuse request if access token audience does not match | MUST | 2.3 |
| R29 | AS MUST invalidate authorization codes after first use | MUST | 4.2.4 |

## Informative Annexes (Condensed)
- **Attacker Model (Section 3)**: Defines five attacker types: Web (A1), Network (A2), Authorization response reader (A3), Authorization request reader (A4), Token acquirer (A5). Implementers must consider all applicable.
- **Attack Details (Section 4)**: Each attack described with preconditions, attack steps, and countermeasures. Includes real-world examples (e.g., subdomain takeover, Chromium fragment leakage). Countermeasures are normative where indicated.
- **PKCE and Nonce Limitations (Section 4.5.4)**: Attacker may circumvent by modifying nonce/code_challenge in victim's request; thus protection of authorization response integrity remains essential.
- **Sender-Constrained vs Audience-Restricted (Section 4.10)**: Both methods mitigate token misuse; sender-constraining binds token to client, audience-restriction limits to specific RS. Discussion of metadata-based prevention and why it is not recommended.
- **Refresh Token Rotation (Section 4.14.2)**: If rotation used, AS must revoke all tokens of the grant upon detection of reuse.
- **Cross-Site Request Forgery via nonce (Section 4.7.1)**: PKCE provides stronger CSRF protection than state because attacker cannot replay state if learned; nonce also limited.
- **OpenID Connect mitigations**: For mix-up, code injection, and access token injection, OpenID Connect provides additional protections (ID Token, nonce, iss claim).