# RFC 4513: Lightweight Directory Access Protocol (LDAP): Authentication Methods and Security Mechanisms
**Source**: IETF (Standards Track) | **Version**: Obsoletes RFC 2251, 2829, 2830 | **Date**: June 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc4513

## Scope (Summary)
This document specifies authentication methods and security mechanisms for LDAP, including TLS via StartTLS, simple Bind (anonymous, unauthenticated, name/password), and SASL Bind (including EXTERNAL). It defines implementation requirements, server identity checks, authorization state transitions, and security considerations.

## Normative References
- RFC 791 (IP)
- RFC 2119 (Key words)
- RFC 2460 (IPv6)
- RFC 3454 (Stringprep)
- RFC 3490 (IDNA)
- RFC 3629 (UTF-8)
- RFC 4013 (SASLprep)
- RFC 4234 (ABNF)
- RFC 4346 (TLS 1.1)
- RFC 4422 (SASL)
- RFC 4510 (LDAP Road Map)
- RFC 4511 (LDAP Protocol)
- RFC 4512 (LDAP DIT)
- RFC 4514 (LDAP DN String)
- RFC 4517 (Syntaxes and Matching)
- RFC 4519 (User Schema)
- RFC 4520 (IANA Considerations for LDAP)
- Unicode Standard 3.2.0
- ITU-T Rec. X.501 (Directory Models)

## Definitions and Abbreviations
- **user**: Any human or application entity accessing the directory using a client.
- **transport connection**: Underlying transport services and associations used to carry protocol exchange.
- **TLS layer**: TLS services and associations used for security.
- **SASL layer**: SASL services and associations used for security.
- **LDAP message layer**: LDAP Message (PDU) services and associations used for directory services.
- **LDAP session**: Combined services of transport connection, TLS layer, SASL layer, LDAP message layer and their associations.
- **reference identity**: Client's understanding of the server's identity (e.g., from transport connection).
- **authorization identity**: Name of entity requesting operations; may differ from authentication identity.
- **authentication identity**: Name presented in a credential.

## 2. Implementation Requirements
- **R1**: LDAP server implementations **MUST** support the anonymous authentication mechanism of the simple Bind method (Section 5.1.1).
- **R2**: LDAP implementations that support any authentication mechanism other than anonymous **MUST** support the name/password authentication mechanism of simple Bind (Section 5.1.3) **and** **MUST** be capable of protecting it using TLS as established by StartTLS (Section 3).
- **R3**: Implementations **SHOULD** disallow name/password authentication by default when suitable data security services are not in place; they **MAY** provide other suitable data security services.
- **R4**: LDAP server implementations **SHOULD** support client assertion of authorization identity via SASL EXTERNAL (Section 5.2.3).
- **R5**: LDAP server implementations that support no authentication mechanism other than anonymous **SHOULD** support TLS via StartTLS.
- **R6**: Implementations supporting TLS **MUST** support `TLS_RSA_WITH_3DES_EDE_CBC_SHA` ciphersuite and **SHOULD** support `TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA`.

## 3. StartTLS Operation
### 3.1. TLS Establishment Procedures
#### 3.1.1. StartTLS Request Sequencing
- Client **MAY** send StartTLS extended request at any time after establishing an LDAP session, except:
  - when TLS is currently established,
  - when a multi-stage SASL negotiation is in progress,
  - when there are outstanding responses for operations.
- Violation results in `operationsError` resultCode (per [RFC4511] Section 4.14.1).
- If a client intends to perform both Bind and StartTLS, it **SHOULD** perform StartTLS first to protect Bind messages.

#### 3.1.2. Client Certificate
- If server requests/demands a client certificate and client does not present a suitable one, server may use local security policy to determine whether to complete TLS.
- If client provides a suitable certificate and later performs SASL EXTERNAL Bind, certificate info may be used for identification and authentication.

#### 3.1.3. Server Identity Check
- Client **MUST** verify server's identity using certificate to prevent man-in-the-middle attacks.
- Client determines type (e.g., DNS name, IP address) of reference identity and compares against `subjectAltName` values of same type until a match.
- Server identity may also be verified by comparing reference identity to Common Name (CN) in leaf RDN of subjectName, using DNS comparison rules but without wildcards. **Deprecated**.
- If identity check fails, user-oriented clients **SHOULD** notify user or close connection; automated clients **SHOULD** close and log error.

##### 3.1.3.1. Comparison of DNS Names
- Internationalized domain names **MUST** be converted to ACE format per RFC 3490 Section 4 before comparison.
- '*' wildcard allowed only as left-most DNS label, matches any single left-most label.

##### 3.1.3.2. Comparison of IP Addresses
- Reference IP address **MUST** be converted to network byte order octet string (4 octets for IPv4, 16 for IPv6) and compared to `iPAddress` subjectAltName values.

##### 3.1.3.3. Comparison of Other subjectName Types
- Client implementations **MAY** support matching against other subjectAltName types as defined in other documents.

#### 3.1.4. Discovery of Resultant Security Level
- After TLS establishment, both parties independently decide whether to continue based on local policy and security level.
- If inadequate, party **SHOULD** remove TLS layer immediately after negotiation completes.

#### 3.1.5. Refresh of Server Capabilities Information
- After TLS layer established, client **SHOULD** discard or refresh all server information obtained prior to TLS initiation that was not obtained through secure mechanisms.
- Server may advertise different capabilities after TLS (e.g., `supportedSASLMechanisms` may include EXTERNAL and PLAIN).

### 3.2. Effect of TLS on Authorization State
- Establishment, change, or closure of TLS may cause authorization state to move to a new state (see Section 4).

### 3.3. TLS Ciphersuites
- Considerations: confidentiality protection, man-in-the-middle vulnerability, verification of adequacy.
- Ciphersuites vulnerable to man-in-the-middle attacks **SHOULD NOT** be used to protect passwords or sensitive data unless negligible danger.

## 4. Authorization State
- Every LDAP session has an associated authorization state, affected by events like Bind, StartTLS, TLS closure, and external events.
- At session start, session has anonymous authorization identity.
- Client may send any operation before performing Bind; server **MUST** treat as if after anonymous Bind.
- Upon receipt of Bind request, server moves session to anonymous authorization state. If successful, moves to requested authentication state; otherwise remains anonymous.
- Other events (e.g., establishment/closure of security services, credential expiration) may move state to anonymous.

## 5. Bind Operation
### 5.1. Simple Authentication Method
#### 5.1.1. Anonymous Authentication Mechanism
- Client sends Bind request with zero-length name and zero-length password to explicitly establish anonymous authorization state.

#### 5.1.2. Unauthenticated Authentication Mechanism
- Client sends Bind request with non-zero-length name and zero-length password.
- DN used for trace (logging) only; not authenticated or validated; not used for authorization.
- **Security**: Clients **SHOULD** require user selection of unauthenticated mechanism by other means than empty password. Servers **SHOULD** by default fail with `unwillingToPerform`.

#### 5.1.3. Name/Password Authentication Mechanism
- Client sends Bind request with non-zero-length name (DN) and non-zero-length password.
- Servers map DN to entry with associated passwords; password valid if matches any member of set.
- Result codes: `invalidDNSyntax` (syntactically invalid DN), `invalidCredentials` (DN or password invalid), `success` (valid and willing to serve).
- Behavior undefined for zero-length name and non-zero-length password.
- Not suitable for environments without confidentiality protection.

### 5.2. SASL Authentication Method
#### 5.2.1. SASL Protocol Profile
##### 5.2.1.1. SASL Service Name
- Service name for LDAP is `"ldap"` (registered with IANA).

##### 5.2.1.2. SASL Authentication Initiation and Protocol Exchange
- Initiated via BindRequest with version 3, `sasl` AuthenticationChoice, mechanism name, optional initial credentials.
- Exchange: series of challenges (server sends `saslBindInProgress`) and responses (client sends new BindRequest with same mechanism).
- Challengeresponse tokens are opaque binary; LDAP does not Base64-transform.
- Client sending SASL Bind **SHOULD** send zero-length name. Server **SHALL** ignore any name value.
- Client may abort by sending different mechanism or non-SASL AuthenticationChoice.
- Empty string in mechanism field results in `authMethodNotSupported`.
- Server indicates completion by resultCode other than `saslBindInProgress`.

##### 5.2.1.3. Optional Fields
- Distinguish zero-length initial response from absent: present empty OCTET STRING vs omit.
- For serverSaslCreds: present zero-length OCTET STRING if sending additional data; otherwise **SHALL** omit.

##### 5.2.1.4. Octet Where Negotiated Security Layers Take Effect
- SASL layers take effect after transmission/reception of final BindResponse with success.
- Layer remains until new layer installed; not affected by failed or non-SASL Bind.

##### 5.2.1.5. Determination of Supported SASL Mechanisms
- Clients read `supportedSASLMechanisms` attribute from root DSE. Servers **SHOULD** allow all clients to retrieve it before and after SASL exchange.
- Clients and servers should be configurable to specify acceptable mechanisms.

##### 5.2.1.6. Rules for Using SASL Layers
- Client **SHOULD** discard or refresh server information obtained prior to SASL negotiation that was not secure.
- If lower-level security layer (e.g., TLS) exists, SASL layer **SHALL** be layered on top regardless of negotiation order.
- Layers act independently (e.g., removing TLS does not affect SASL layer).

##### 5.2.1.7. Support for Multiple Authentications
- LDAP supports multiple SASL authentications as defined in [RFC4422] Section 4.

##### 5.2.1.8. SASL Authorization Identities
- Authorization identity string grammar (ABNF):
  ```
  authzId = dnAuthzId / uAuthzId
  dnAuthzId = "dn:" distinguishedName
  uAuthzId = "u:" userid
  userid = *UTF8
  ```
- `dnAuthzId` uses DN matching rule; no requirement that DN exists as entry.
- `uAuthzId` format is local; **SHOULD NOT** be assumed globally unique. For comparison, each value **MUST** be prepared as "query" string using SASLprep and compared octet-wise.
- Grammar extensible; new forms registered with unique prefix.

#### 5.2.2. SASL Semantics within LDAP
- Implementers must maintain SASL semantics; e.g., DIGEST-MD5 uses simple strings, not LDAP DNs.

#### 5.2.3. SASL EXTERNAL Authentication Mechanism
- Used to request authentication using credentials from lower security layer (e.g., TLS certificate).
- If credentials not established, Bind **MUST** fail with `inappropriateAuthentication`.
- Two assertions:
  - **Implicit**: No credentials field; server derives authorization identity from lower layer credentials.
  - **Explicit**: Credentials field contains authorization identity as per Section 5.2.1.8.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | LDAP server must support anonymous simple Bind. | MUST | Section 2 |
| R2 | Implementations supporting non‑anonymous auth must support name/password simple Bind and protect it with TLS. | MUST | Section 2 |
| R3 | Implementations should disallow name/password without data security by default. | SHOULD | Section 2 |
| R4 | LDAP servers should support SASL EXTERNAL for authorization identity assertion. | SHOULD | Section 2 |
| R5 | Servers supporting only anonymous should support TLS. | SHOULD | Section 2 |
| R6 | TLS implementations must support TLS_RSA_WITH_3DES_EDE_CBC_SHA and should support TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA. | MUST/SHOULD | Section 2 |
| R7 | Client must verify server identity using certificate. | MUST | Section 3.1.3 |
| R8 | Internationalized domain names must be converted to ACE for comparison. | MUST | Section 3.1.3.1 |
| R9 | IP addresses must be converted to network byte order octet string for comparison. | MUST | Section 3.1.3.2 |
| R10 | Upon TLS establishment, client should discard or refresh unsecured server info. | SHOULD | Section 3.1.5 |
| R11 | Session starts anonymous; server must treat operations sent before Bind as after anonymous Bind. | MUST | Section 4 |
| R12 | Upon receipt of Bind request, server moves session to anonymous state immediately. | MUST | Section 4 |
| R13 | If authorization identity is specified in Bind, server must verify that authentication identity is permitted to assume it. Must reject with invalidCredentials if not authorized. | MUST | Section 5 |
| R14 | Server shall ignore any value in name field of SASL Bind request. | SHALL | Section 5.2.1.2 |
| R15 | If client sends mechanism empty string, server must return authMethodNotSupported. | MUST | Section 5.2.1.2 |
| R16 | Distinguish absent vs zero-length initial response: omit SaslCredentials.credentials or include zero-length. | MUST | Section 5.2.1.3 |
| R17 | Server shall omit serverSaslCreds if no additional data. | SHALL | Section 5.2.1.3 |
| R18 | SASL layers take effect after final BindResponse with success. | - | Section 5.2.1.4 |
| R19 | SASL layer must be layered on top of lower security layers. | SHALL | Section 5.2.1.6 |
| R20 | SASL EXTERNAL Bind must fail with inappropriateAuthentication if lower layer credentials not established. | MUST | Section 5.2.3 |
| R21 | Servers supporting password-based auth that transmits passwords in the clear must support policy requiring TLS, other confidentiality mechanism, or return confidentialityRequired. | MUST | Section 6.3.3 |
| R22 | Clients must warn user or refuse to proceed if TLS security level inadequate. | MUST | Section 6.2 |
| R23 | Servers should by default fail unauthenticated Bind requests with unwillingToPerform. | SHOULD | Section 5.1.2 |
| R24 | Clients should disallow empty password input to name/password auth UI. | SHOULD | Section 5.1.2 |
| R25 | uAuthzId values must be prepared with SASLprep before comparison. | MUST | Section 5.2.1.8 |

## Informative Annexes (Condensed)
- **Appendix A: Authentication and Authorization Concepts**: Defines access control policy, factors, authentication credentials, and authorization identity. Provides foundational concepts for understanding security mechanisms in LDAP.
- **Appendix B: Summary of Changes**: Documents substantive changes from RFC 2251, RFC 2829, and RFC 2830. Key changes: name/password auth with TLS replaces mandatory DIGEST‑MD5; SASL ANONYMOUS and PLAIN are no longer precluded; server identity check algorithm updated; authorization identity matching rules refined; TLS ciphersuite recommendations updated.