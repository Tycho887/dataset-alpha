# RFC 6819: OAuth 2.0 Threat Model and Security Considerations
**Source**: IETF (Informational) | **Version**: January 2013 | **Date**: January 2013 | **Type**: Informative
**Original**: http://www.rfc-editor.org/info/rfc6819

## Scope (Summary)
This document provides additional security considerations for OAuth 2.0 [RFC6749] based on a comprehensive threat model. It covers clients bound to a specific deployment with static resource server URLs and well-known token scope values. Out of scope: communication between authorization server and resource server, token formats, user authentication mechanisms (except for password grant), and clients not bound to a specific deployment.

## Normative References
- [RFC6749] Hardt, D., "The OAuth 2.0 Authorization Framework", RFC 6749, October 2012.
- [RFC6750] Jones, M. and D. Hardt, "The OAuth 2.0 Authorization Framework: Bearer Token Usage", RFC 6750, October 2012.

## Definitions and Abbreviations
- **Handle (artifact)**: Token that is a reference to internal data structure; requires communication between issuer and consumer for validation.
- **Assertion (self-contained token)**: Parseable token with duration, audience, and digital signature; can be validated independently.
- **Bearer token**: Token usable by any party in possession; must be protected in transit.
- **Proof token**: Token that requires client to prove ownership (e.g., via MAC signature).
- **Scope**: Access authorization associated with a token, controlling resource servers, resources, and methods.
- **Access token**: Short-lived token used to access resources; may be refreshed.
- **Refresh token**: Long-lasting token used to obtain new access tokens; always exchanged at authorization server.
- **Authorization "code"**: Intermediate result of end-user authorization; exchanged for tokens over secure channel.
- **Redirect URI**: URI used to detect malicious clients; must be validated during code exchange.
- **"state" parameter**: Links request to callback to prevent CSRF; should be bound to user agent session.
- **Client identifier**: Used to collate requests, display client info, limit requests, and differentiate access.
- **Confidential client**: Capable of maintaining client credentials (e.g., secret); can authenticate.
- **Public client**: Cannot maintain credentials securely; no secret or easily reversible.

## Overview (Section 2)
### Scope (2.1)
- Covers clients bound to specific deployment with static RS URLs; token scope well-known; client registration out of scope.
- Out of scope: communication between AS and RS, token formats, user authentication (except password grant), assertion mechanisms, and clients not bound to specific deployment.

### Attack Assumptions (2.2)
- Attacker has full network access between client and AS/RS; unlimited resources; two parties may collude against third.

### Architectural Assumptions (2.3)
- **Authorization Server**: stores usernames/passwords, client ids/secrets, refresh/access tokens, HTTPS key, per-authorization data.
- **Resource Server**: stores user data, HTTPS key, either AS credentials (handle design) or shared secret/public key (assertion), access tokens. No refresh tokens, user passwords, or client secrets.
- **Client**: stores client id (and secret), refresh/access tokens, trusted CA certs, per-authorization redirect URI and code.

## Security Features (Section 3) - Preserved Key Points
### Tokens (3.1)
- **Handle**: Reference to internal data; simple revocation; need communication for validation.
- **Assertion**: Self-contained, signed; better performance; revocation harder.
- **Bearer token**: Usable by any bearer; must secure transport.
- **Proof token**: Requires client proof (e.g., MAC).

### Scope (3.1.1)
- Represents access authorization; controlled by AS/end user; can be limited.

### Limited Access Token Lifetime (3.1.2)
- `expires_in` parameter allows short-lived tokens.

### Access Token (3.2)
- Short lifespan; can be refreshed.

### Refresh Token (3.3)
- Long-lasting authorization; always exchanged at AS; bound to client id and instance.

### Authorization "code" (3.4)
- Intermediate result; passed instead of tokens to avoid exposure in browser; short-lived; client authentication over direct connection.

### Redirect URI (3.5)
- Helps detect malicious clients; must be verified during code exchange; AS should pre-register for public/confidential implicit clients.

### "state" Parameter (3.6)
- Prevents CSRF; must be bound to user agent session; kept in same-origin protected location.

### Client Identifier (3.7)
- Identifies software component; used for collating requests, displaying info, limiting requests.
- Types: deployment-independent with/without secret, deployment-specific with/without validated properties.

## Threat Model (Section 4)

### 4.1 Clients
#### 4.1.1 Threat: Obtaining Client Secrets
- **Attack**: Extract from source code/binary; obtain deployment-specific secret.
- **Impact**: Bypass client authentication; replay refresh tokens/codes.
- **Countermeasures**: 
  - Don't issue secrets to public clients (5.2.3.1)
  - Require user consent for public clients (5.2.3.2)
  - Use deployment-specific secrets (5.2.3.4)
  - Revoke client secrets (5.2.3.6)
  - Web server protection (5.3.2); native: secure storage (5.3.3)

#### 4.1.2 Threat: Obtaining Refresh Tokens
- **Attacks**: Web server breach; read from native filesystem; device theft; device cloning.
- **Impact**: Exposure of all refresh tokens (web app) or single user (native).
- **Countermeasures**:
  - General: validate client id with refresh (5.2.2.2); limit scope (5.1.5.1); revoke tokens (5.2.2.4); revoke client secrets (5.2.3.6); rotate refresh tokens (5.2.2.3)
  - Web: server protection (5.3.2); strong client authentication (5.2.3.7)
  - Native: secure storage (5.3.3); device lock (5.3.4)
  - Device theft/clone: lock (5.3.4); device identification (5.2.2.5); rotation (5.2.2.3); revocation (5.2.2.4)

#### 4.1.3 Threat: Obtaining Access Tokens
- **Attack**: Stolen from device storage.
- **Impact**: Attacker can access all resources within token scope.
- **Countermeasures**: Keep in transient memory (5.1.6); limit scope (5.1.5.1); protect as refresh tokens (5.2.2); short lifetime (5.1.5.3)

#### 4.1.4 Threat: End-User Credentials Phishing via Compromised/Embedded Browser
- **Attack**: Malicious app uses embedded browser to capture UID/password.
- **Impact**: Credential theft.
- **Countermeasures**: Client apps must never ask for user passwords; delegate to system browser; validate apps in app market.

#### 4.1.5 Threat: Open Redirectors on Client
- **Attack**: Client's open redirector used to redirect code/token to attacker.
- **Impact**: Code/token theft.
- **Countermeasures**: Require full redirect URI registration (5.2.3.5)

### 4.2 Authorization Endpoint
#### 4.2.1 Threat: Password Phishing by Counterfeit AS
- **Attack**: DNS/ARP spoofing to intercept requests.
- **Impact**: Password theft.
- **Countermeasures**: Use TLS (5.1.2); educate users.

#### 4.2.2 Threat: User Unintentionally Grants Too Much Scope
- **Attack**: User misunderstands scope.
- **Countermeasures**: Explain scope clearly (5.2.4.2); narrow scope based on client (5.1.5.1)

#### 4.2.3 Threat: Malicious Client Obtains Existing Authorization by Fraud
- **Attack**: Exploit automatic repeat authorization.
- **Countermeasures**: Don't auto-process for public clients unless registered redirect URI (5.2.4.1); limit scope (5.1.5.1)

#### 4.2.4 Threat: Open Redirector (AS)
- **Attack**: AS used as open redirector via redirect_uri parameter.
- **Impact**: Phishing.
- **Countermeasures**: Require full redirect URI registration (5.2.3.5); don't redirect if cannot verify (5.2.3.5)

### 4.3 Token Endpoint
#### 4.3.1 Threat: Eavesdropping Access Tokens (AS to client)
- **Countermeasures**: TLS (5.1.1); reduce scope/expiry (5.1.5.1, 5.1.5.3)

#### 4.3.2 Threat: Obtaining Access Tokens from AS Database
- **Countermeasures**: System security (5.1.4.1.1); store hashes (5.1.4.1.3); SQL injection countermeasures (5.1.4.1.2)

#### 4.3.3 Threat: Disclosure of Client Credentials during Transmission
- **Countermeasures**: TLS (5.1.1); use alternative authentication (e.g., HMAC)

#### 4.3.4 Threat: Obtaining Client Secret from AS Database
- **Countermeasures**: System security (5.1.4.1.1); SQL injection countermeasures (5.1.4.1.2); credential storage best practices (5.1.4.1)

#### 4.3.5 Threat: Obtaining Client Secret by Online Guessing
- **Countermeasures**: High entropy (5.1.4.2.2); lock accounts (5.1.4.2.3); strong client authentication (5.2.3.7)

### 4.4 Obtaining Authorization - Grant Type Specific
#### 4.4.1 Authorization Code
##### 4.4.1.1 Threat: Eavesdropping/Leaking Codes
- **Attack**: Referrer headers, request logs, open redirectors, browser history.
- **Countermeasures**: TLS (5.1.1); authenticate client (5.2.4.4); short expiry (5.1.5.3); one-time usage (5.1.5.4); revoke derived tokens on abuse (5.2.1.1); reduce scope/expiry (5.1.5.1,5.1.5.3); reload page to clear cache.

##### 4.4.1.2 Threat: Obtaining Codes from AS Database
- **Countermeasures**: Credential storage protection (5.1.4.1); system security (5.1.4.1.1); store hashes (5.1.4.1.3); SQL injection countermeasures (5.1.4.1.2)

##### 4.4.1.3 Threat: Online Guessing of Codes
- **Countermeasures**: High entropy for handle (5.1.4.2.2); sign assertion (5.1.5.9); authenticate client (5.2.3.4); bind code to redirect URI (5.2.4.5); short expiry (5.1.5.3)

##### 4.4.1.4 Threat: Malicious Client Obtains Authorization
- **Attack**: Client pretends to be valid; screen-scraping to simulate consent.
- **Countermeasures**: Authenticate client (5.2.3.4); validate redirect URI (5.2.3.5); user consent with client info (5.2.4.3); no automatic re-authorization for unauthenticated clients (5.2.4.1); require user input (CAPTCHA, multi-factor); limit scope (5.1.5.1)

##### 4.4.1.5 Threat: Authorization Code Phishing
- **Attack**: Impersonate client site via DNS/ARP spoofing.
- **Countermeasures**: Use HTTPS for redirect URI (5.1.2); authenticate client (5.2.4.4)

##### 4.4.1.6 Threat: User Session Impersonation
- **Attack**: Intercept code in transit to client; use it to access resources.
- **Countermeasures**: HTTPS for redirect URI (5.1.2)

##### 4.4.1.7 Threat: Code Leakage through Counterfeit Client
- **Attack**: Attacker modifies redirect URI to his site; victim authorizes; attacker injects code into original client.
- **Countermeasures**: Bind code to redirect URI (5.2.4.5); enforce pre-registered redirect URIs (5.2.3.5); use deployment-specific client ids/secrets (5.2.3.4) and bind code to client_id (5.2.4.4); consider implicit grant or password credentials.

##### 4.4.1.8 Threat: CSRF Attack against redirect-uri
- **Attack**: Attacker obtains code to his own resources; tricks victim to follow redirect; client associates token with victim's session.
- **Countermeasures**: Use "state" parameter linked to user agent session (5.3.5); educate users.

##### 4.4.1.9 Threat: Clickjacking Attack against Authorization
- **Attack**: Malicious site overlays iFrame over authorization page.
- **Countermeasures**: X-FRAME-OPTIONS header (5.2.2.6); JavaScript frame-busting.

##### 4.4.1.10 Threat: Resource Owner Impersonation
- **Attack**: Client programmatically simulates user approval (e.g., hidden browser, session abuse).
- **Countermeasures**: Force user interaction (CAPTCHA, one-time secrets out-of-band); notify resource owner.

##### 4.4.1.11 Threat: DoS Attacks Exhausting Resources
- **Attack**: Repeated authorization requests exhaust pool of codes/tokens.
- **Countermeasures**: Limit tokens per user; include high entropy in codes.

##### 4.4.1.12 Threat: DoS Using Manufactured Authorization Codes
- **Attack**: Botnet uses client redirect URIs with random codes to concentrate HTTPS connections on AS.
- **Countermeasures**: CSRF defense and "state" parameter; client should authenticate user and suspend account on excessive invalid codes; AS should rate-limit clients.

##### 4.4.1.13 Threat: Code Substitution (OAuth Login)
- **Attack**: Attacker obtains victim's code via malicious app; substitutes it in target app login.
- **Countermeasures**: Client must include client_id in token exchange; AS must validate code issued to that client; use OpenID/SAML with audience restrictions.

#### 4.4.2 Implicit Grant
##### 4.4.2.1 Threat: Access Token Leak in Transport/Endpoints
- **Countermeasures**: TLS (5.1.1)

##### 4.4.2.2 Threat: Access Token Leak in Browser History
- **Countermeasures**: Short expiry (5.1.5.3); reduce scope (5.1.5.1); non-cacheable responses.

##### 4.4.2.3 Threat: Malicious Client Obtains Authorization
- Same countermeasures as 4.4.1.4, except client authentication.

##### 4.4.2.4 Threat: Manipulation of Scripts
- **Attack**: DNS/ARP spoofing to replace client script.
- **Countermeasures**: Server authentication (5.1.2); ensure script integrity (5.1.1); use one-time per-use secrets.

##### 4.4.2.5 Threat: CSRF Attack against redirect-uri
- Same as 4.4.1.8 but for implicit grant. Countermeasure: use "state" parameter (5.3.5).

##### 4.4.2.6 Threat: Token Substitution (OAuth Login)
- Same as 4.4.1.13 but with access tokens. Countermeasure: use OpenID/SAML.

#### 4.4.3 Resource Owner Password Credentials
- **General risk**: UID/password anti-pattern; no scope control; token revocation bypassed.
- **Countermeasures**: Minimize use; validate client id with refresh (5.2.2.2); TLS (5.1.1); encourage unique passwords; limit to same organization.

##### 4.4.3.1 Threat: Accidental Exposure of Passwords at Client Site
- **Countermeasures**: Use other flows; digest authentication; obfuscate passwords in logs.

##### 4.4.3.2 Threat: Client Obtains Scopes without End-User Authorization
- **Countermeasures**: Use other flows; restrict scope (5.1.5.1); notify resource owner (5.1.3).

##### 4.4.3.3 Threat: Client Obtains Refresh Token through Automatic Authorization
- **Countermeasures**: Use other flows; restrict issuance of refresh tokens (5.2.2.1); notify resource owner (5.1.3).

##### 4.4.3.4 Threat: Obtaining User Passwords on Transport
- **Countermeasures**: TLS (5.1.1); use alternative authentication (HMAC).

##### 4.4.3.5 Threat: Obtaining User Passwords from AS Database
- **Countermeasures**: Credential storage best practices (5.1.4.1).

##### 4.4.3.6 Threat: Online Guessing
- **Countermeasures**: Strong password policy (5.1.4.2.1); lock accounts (5.1.4.2.3); tar pit (5.1.4.2.4); CAPTCHAs (5.1.4.2.5); avoid password grant; client authentication.

#### 4.4.4 Client Credentials
- Threats similar to Section 4.4.3.

### 4.5 Refreshing an Access Token
#### 4.5.1 Threat: Eavesdropping Refresh Tokens
- **Countermeasures**: TLS (5.1.1); reduce scope/expiry (5.1.5.1,5.1.5.3)

#### 4.5.2 Threat: Obtaining Refresh Token from AS Database
- **Countermeasures**: Credential storage best practices (5.1.4.1); bind token to client id (5.1.5.8)

#### 4.5.3 Threat: Obtaining Refresh Token by Online Guessing
- **Countermeasures**: High entropy for handle (5.1.4.2.2); sign assertion (5.1.5.9); bind to client id (5.1.5.8); authenticate client (5.2.3.4)

#### 4.5.4 Threat: Refresh Token Phishing by Counterfeit AS
- **Countermeasures**: Server authentication (5.1.2)

### 4.6 Accessing Protected Resources
#### 4.6.1 Threat: Eavesdropping Access Tokens on Transport
- **Countermeasures**: TLS (5.1.1); short lifetime (5.1.5.3); bind token to client (5.4.2)

#### 4.6.2 Threat: Replay of Authorized Resource Server Requests
- **Countermeasures**: TLS (5.1.1); signed requests with nonces/timestamps (5.4.3)

#### 4.6.3 Threat: Guessing Access Tokens
- **Countermeasures**: High entropy for handle (5.1.4.2.2); sign assertion (5.1.5.9); short duration (5.1.5.2,5.1.5.3)

#### 4.6.4 Threat: Access Token Phishing by Counterfeit Resource Server
- **Attack**: Fake RS accepts token and uses it elsewhere.
- **Countermeasures**: Authenticate RS (5.1.2); bind token to endpoint URL (audience) (5.1.5.5,5.1.5.6); authenticate client with resource server (5.4.2); restrict scope (5.1.5.1) and audience (5.1.5.5)

#### 4.6.5 Threat: Abuse of Token by Legitimate Resource Server or Client
- **Countermeasures**: Restrict token to particular RS (5.1.5.5)

#### 4.6.6 Threat: Leak of Confidential Data in HTTP Proxies
- **Countermeasures**: Use Authorization headers (5.4.1); set Cache-Control: no-store (client), private (RS); reduce scope/expiry.

#### 4.6.7 Threat: Token Leakage via Log Files and HTTP Referrers
- **Countermeasures**: Use Authorization headers (5.4.1); configure logging; restrict log access; enforce authenticated requests (5.4.2); limit scope/duration/one-time usage.

## Security Considerations (Section 5) - Condensed Countermeasures

### 5.1 General
- **5.1.1 Ensure Confidentiality**: All requests must be protected with TLS (or VPN) between client, AS, RS.
- **5.1.2 Utilize Server Authentication**: Use HTTPS server authentication to verify server identity; client must validate certificate binding.
- **5.1.3 Always Keep Resource Owner Informed**: Use consent forms, notifications, activity logs, self-care portals.
- **5.1.4 Credentials Protection**:
  - 5.1.4.1.1 System security measures.
  - 5.1.4.1.2 SQL injection countermeasures (minimum privileges, static SQL, bind arguments, input validation).
  - 5.1.4.1.3 No cleartext storage; store hashes (with salt for low-entropy secrets) or encrypt.
  - 5.1.4.1.4 Encrypt client credentials.
  - 5.1.4.1.5 Use asymmetric cryptography for authentication.
- **5.1.4.2 Online Attacks**:
  - 5.1.4.2.1 Strong password policy.
  - 5.1.4.2.2 High entropy for secrets (>=128 bits, cryptographically random).
  - 5.1.4.2.3 Lock accounts after failed attempts.
  - 5.1.4.2.4 Tar pit (delay response).
  - 5.1.4.2.5 CAPTCHAs.
- **5.1.5 Tokens (Access, Refresh, Code)**:
  - 5.1.5.1 Limit scope (client-specific, service-specific, resource-owner-specific policy).
  - 5.1.5.2 Determine expiration time based on risk.
  - 5.1.5.3 Use short expiration time (reduces impact of replay, leak, guessing).
  - 5.1.5.4 Limit number of usages or one-time usage; revoke derived tokens on multiple redeem attempts.
  - 5.1.5.5 Bind tokens to a particular resource server (audience).
  - 5.1.5.6 Use endpoint address as token audience.
  - 5.1.5.7 Use explicitly defined scopes for audience and tokens.
  - 5.1.5.8 Bind token to client id (validate on each request).
  - 5.1.5.9 Sign self-contained tokens (HMAC or digital signature).
  - 5.1.5.10 Encrypt token content.
  - 5.1.5.11 Adopt standard assertion format (SAML, JWT).
- **5.1.6 Access Tokens**: Keep in transient memory; pass over secure transport; do not share with 3rd parties.

### 5.2 Authorization Server
- **5.2.1 Authorization codes**: 5.2.1.1 Automatic revocation of derived tokens if abuse detected (multiple redeem attempts).
- **5.2.2 Refresh Tokens**:
  - 5.2.2.1 Restricted issuance (refuse if client cannot store securely).
  - 5.2.2.2 Binding to client_id (validate client_id on refresh; authenticate client if possible).
  - 5.2.2.3 Rotation (change refresh token on each refresh; revoke if old token used).
  - 5.2.2.4 Revocation (allow clients/users to invalidate tokens).
  - 5.2.2.5 Device identification (bind to device identifier).
  - 5.2.2.6 X-FRAME-OPTIONS header (DENY or SAMEORIGIN to prevent clickjacking).
- **5.2.3 Client Authentication and Authorization**:
  - 5.2.3.1 Don't issue secrets to public clients.
  - 5.2.3.2 Require user consent for public clients without secret.
  - 5.2.3.3 Issue client_id only in combination with redirect_uri (bind and validate).
  - 5.2.3.4 Issue installation-specific client secrets.
  - 5.2.3.5 Validate pre-registered redirect_uri (full URI; reject if mismatch; do not redirect on error).
  - 5.2.3.6 Revoke client secrets.
  - 5.2.3.7 Use strong client authentication (e.g., client assertion).
- **5.2.4 End-User Authorization**:
  - 5.2.4.1 Do not automatically process repeat authorizations for unauthenticated clients.
  - 5.2.4.2 Informed decisions based on transparency (explain scope, duration, client properties).
  - 5.2.4.3 Validation of client properties by end user (review client name, website).
  - 5.2.4.4 Bind authorization code to client_id.
  - 5.2.4.5 Bind authorization code to redirect_uri.

### 5.3 Client App Security
- 5.3.1 Don't store credentials in code or resources bundled with software.
- 5.3.2 Use standard web server protection measures.
- 5.3.3 Store secrets in secure storage (OS-level segregation, application-specific storage, user-supplied secret).
- 5.3.4 Utilize device lock (PIN, password, biometric).
- 5.3.5 Link "state" parameter to user agent session.

### 5.4 Resource Servers
- 5.4.1 Use Authorization headers (reduces leakage via proxies/caches).
- 5.4.2 Authenticated requests: bind token to client identifier and validate via client certificate, signed request, or Holder-of-Key.
- 5.4.3 Signed requests (with unique identifiers, non-replay).

### 5.5 A Word on User Interaction and User-Installed Apps
- End users may not understand ramification; devices prone to compromise; malicious apps can steal credentials; no complete solution; restrict user-installed software in limited environments; authorization servers must clearly indicate client properties and risks.

## Requirements Summary (Key Normative Statements)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Authorization servers must ensure transmissions are protected using transport-layer mechanisms (TLS). | must | 4.3.1, 4.4.1.1, 4.4.3, 4.5.1, 4.6.1, 5.1.1 |
| R2 | Clients must keep access tokens in transient memory and pass them securely. | must | 5.1.6 |
| R3 | Authorization servers should validate pre-registered redirect URI and reject mismatches. | should | 5.2.3.5 |
| R4 | Authorization servers should not allow automatic authorization for public clients. | should | 5.2.4.1 |
| R5 | Authorization servers should bind authorization code to client_id and redirect_uri. | should | 5.2.4.4, 5.2.4.5 |
| R6 | Clients should utilize "state" parameter to prevent CSRF. | should | 5.3.5 |
| R7 | Authorization servers should limit token scope and lifetime. | should | 5.1.5.1, 5.1.5.3 |
| R8 | Credentials and secrets must not be stored in cleartext (hash or encrypt). | must | 5.1.4.1.3 |
| R9 | Token secrets must have high entropy (>=128 bits). | must | 5.1.4.2.2 |
| R10 | Self-contained tokens must be signed. | must | 5.1.5.9 |
| R11 | Authorization servers should revoke derived tokens if abuse detected. | should | 5.2.1.1 |
| R12 | Refresh tokens should be rotated on each use. | should | 5.2.2.3 |
| R13 | Clients must authenticate to AS when exchanging authorization code (if confidential). | must (implied) | 5.2.3 |
| R14 | Resource servers must use TLS for access token transmission. | must | 5.1.1 |

## Informative Annexes (Condensed)
- **Token Formats (Section 3.1)**: Handles vs assertions; bearer vs proof tokens. Provides basis for threat analysis.
- **Client Types (Section 3.7)**: Categorization by deployment and secret availability; impacts trust level.
- **Attack Assumptions (Section 2.2)**: Attacker has network access, unlimited resources; two parties may collude.
- **Architectural Assumptions (Section 2.3)**: Data stored per entity; used for threat model.
- **User Interaction (Section 5.5)**: Highlights challenges with end-user involvement; recommends clear communication and restriction of untrusted apps.