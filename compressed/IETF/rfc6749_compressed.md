# RFC 6749: The OAuth 2.0 Authorization Framework
**Source**: IETF | **Version**: Standards Track | **Date**: October 2012 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6749

## Scope (Summary)
The OAuth 2.0 authorization framework enables a third-party application to obtain limited access to an HTTP service, either on behalf of a resource owner by orchestrating an approval interaction or by allowing the third-party application to obtain access on its own behalf. This specification replaces RFC 5849 and is designed for use with HTTP.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2246] Dierks, T. and C. Allen, "The TLS Protocol Version 1.0", RFC 2246, January 1999.
- [RFC2616] Fielding, R., et al., "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [RFC2617] Franks, J., et al., "HTTP Authentication: Basic and Digest Access Authentication", RFC 2617, June 1999.
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [RFC4627] Crockford, D., "The application/json Media Type for JavaScript Object Notation (JSON)", RFC 4627, July 2006.
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", RFC 4949, August 2007.
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.
- [USASCII] American National Standards Institute, "Coded Character Set -- 7-bit American Standard Code for Information Interchange", ANSI X3.4, 1986.
- [W3C.REC-html401-19991224] Raggett, D., et al., "HTML 4.01 Specification", W3C Recommendation, December 1999.
- [W3C.REC-xml-20081126] Bray, T., et al., "Extensible Markup Language (XML) 1.0 (Fifth Edition)", W3C Recommendation, November 2008.

## Definitions and Abbreviations
- **resource owner**: An entity capable of granting access to a protected resource. When the resource owner is a person, it is referred to as an end-user.
- **resource server**: The server hosting the protected resources, capable of accepting and responding to protected resource requests using access tokens.
- **client**: An application making protected resource requests on behalf of the resource owner and with its authorization. The term "client" does not imply any particular implementation characteristics.
- **authorization server**: The server issuing access tokens to the client after successfully authenticating the resource owner and obtaining authorization.
- **authorization grant**: A credential representing the resource owner's authorization (to access its protected resources) used by the client to obtain an access token. This specification defines four grant types: authorization code, implicit, resource owner password credentials, and client credentials.
- **access token**: Credentials used to access protected resources. A string representing an authorization issued to the client, usually opaque to the client. Tokens represent specific scopes and durations of access.
- **refresh token**: Credentials used to obtain access tokens. Refresh tokens are issued to the client by the authorization server and are used to obtain a new access token when the current access token becomes invalid or expires, or to obtain additional access tokens with identical or narrower scope. Issuing a refresh token is optional.
- **confidential client**: Clients capable of maintaining the confidentiality of their credentials (e.g., client implemented on a secure server).
- **public client**: Clients incapable of maintaining the confidentiality of their credentials (e.g., native application or browser-based application).

## 1. Introduction
The traditional client-server authentication model has several problems: third-party applications store resource owner's credentials, servers must support password authentication, third parties gain overly broad access, revocation is difficult, compromise of any third party compromises the end-user's password. OAuth addresses these by introducing an authorization layer and separating the role of the client from that of the resource owner. The client obtains an access token instead of using the resource owner's credentials.

### 1.1 Roles
OAuth defines four roles: resource owner, resource server, client, authorization server. The interaction between authorization server and resource server is beyond the scope of this specification.

### 1.2 Protocol Flow
Abstract flow: (A) client requests authorization from resource owner; (B) client receives authorization grant; (C) client requests access token presenting authorization grant; (D) authorization server issues access token; (E) client requests protected resource presenting access token; (F) resource server validates access token and serves request.

### 1.3 Authorization Grant
Authorization grant is a credential used by the client to obtain an access token. Four grant types defined.

#### 1.3.1 Authorization Code
Obtained using authorization server as intermediary. Authorization code provides security benefits: client authentication, transmission of access token directly to client.

#### 1.3.2 Implicit
Simplified authorization code flow for browser-based clients. Access token issued directly. Does not authenticate client. Access token may be exposed to resource owner.

#### 1.3.3 Resource Owner Password Credentials
Username and password used directly as authorization grant. Should only be used when high trust between resource owner and client.

#### 1.3.4 Client Credentials
Client credentials used as authorization grant when scope limited to client's own protected resources or previously arranged.

### 1.4 Access Token
Access tokens are credentials used to access protected resources. Usually opaque to client. Represent specific scopes and durations. May be self-contained or identifier. Access token provides abstraction layer.

### 1.5 Refresh Token
Refresh tokens are credentials used to obtain access tokens. Issuing is optional. Used to get new access tokens when current expires or to obtain additional access tokens with narrower scope. Only intended for authorization servers, not sent to resource servers.

### 1.6 TLS Version
Implementations MAY support additional transport-layer security mechanisms. At time of writing, TLS 1.2 is most recent but limited deployment; TLS 1.0 most widely deployed.

### 1.7 HTTP Redirections
Use of HTTP 302 status code shown, but any method available via user-agent allowed.

### 1.8 Interoperability
OAuth 2.0 is a rich framework but likely to produce non-interoperable implementations. Future work expected to define profiles and extensions.

### 1.9 Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC2119]. All protocol parameter names and values are case sensitive unless noted.

## 2. Client Registration
Before initiating protocol, client registers with authorization server. Client developer SHALL specify client type (Section 2.1), provide redirection URIs (Section 3.1.2), and include any other information required.

### 2.1 Client Types
- **confidential**: Clients capable of maintaining credential confidentiality.
- **public**: Clients incapable of maintaining credential confidentiality.
Client profiles: web application (confidential), user-agent-based application (public), native application (public).

### 2.2 Client Identifier
The authorization server issues a unique client identifier. It is not a secret and MUST NOT be used alone for client authentication. Size left undefined.

### 2.3 Client Authentication
Confidential clients establish authentication method. Authorization server MAY accept any form. MUST NOT rely on public client authentication for identification. The client MUST NOT use more than one authentication method in each request.

#### 2.3.1 Client Password
Clients in possession of a client password MAY use HTTP Basic authentication scheme. Authorization server MUST support HTTP Basic for clients issued client password. Alternatively, authorization server MAY support including client credentials in request-body using "client_id" and "client_secret" parameters. Including credentials in request-body is NOT RECOMMENDED and SHOULD be limited to clients unable to use HTTP Basic. Parameters MUST NOT be included in request URI. Authorization server MUST require use of TLS when sending requests using password authentication. Authorization server MUST protect endpoint against brute force attacks.

#### 2.3.2 Other Authentication Methods
Authorization server MAY support any suitable HTTP authentication scheme. When using other methods, authorization server MUST define a mapping between client identifier and authentication scheme.

### 2.4 Unregistered Clients
Use of unregistered clients is beyond scope of this specification and requires additional security analysis.

## 3. Protocol Endpoints
- **Authorization endpoint**: Used by client to obtain authorization from resource owner via user-agent redirection.
- **Token endpoint**: Used by client to exchange authorization grant for access token, typically with client authentication.
- **Redirection endpoint**: Used by authorization server to return responses containing authorization credentials to client via resource owner user-agent.

### 3.1 Authorization Endpoint
Authorization server MUST first verify identity of resource owner. Must require use of TLS. Must support HTTP GET method, MAY support POST. Parameters sent without a value MUST be treated as omitted. Authorization server MUST ignore unrecognized request parameters. Request and response parameters MUST NOT be included more than once.

#### 3.1.1 Response Type
- **response_type**: REQUIRED. Value MUST be "code" for authorization code, "token" for implicit grant, or registered extension value. Extension response types MAY contain space-delimited list of values. If missing or not understood, authorization server MUST return error response as described in Section 4.1.2.1.

#### 3.1.2 Redirection Endpoint
Redirection endpoint URI MUST be an absolute URI. MUST NOT include fragment component.

##### 3.1.2.1 Endpoint Request Confidentiality
Redirection endpoint SHOULD require TLS when response type is "code" or "token". This specification does not mandate TLS because requiring clients to deploy TLS is a significant hurdle.

##### 3.1.2.2 Registration Requirements
Authorization server MUST require public clients and confidential clients using implicit grant to register their redirection endpoint. SHOULD require all clients to register. SHOULD require complete redirection URI.

##### 3.1.2.3 Dynamic Configuration
If multiple URIs registered, client MUST include "redirect_uri" request parameter. Authorization server MUST compare and match against registered URIs.

##### 3.1.2.4 Invalid Endpoint
If validation fails due to missing, invalid, or mismatching redirection URI, authorization server SHOULD inform resource owner and MUST NOT automatically redirect.

##### 3.1.2.5 Endpoint Content
Client SHOULD NOT include third-party scripts in redirection endpoint response. If included, client MUST ensure its own scripts execute first.

### 3.2 Token Endpoint
Used with every grant except implicit. Must require TLS. Client MUST use HTTP POST method. Parameters sent without a value MUST be treated as omitted. Authorization server MUST ignore unrecognized parameters. Request and response parameters MUST NOT be included more than once.

#### 3.2.1 Client Authentication
Confidential clients or others issued credentials MUST authenticate when making requests to token endpoint. Authorization code requests: unauthenticated client MUST send "client_id" to prevent code substitution.

### 3.3 Access Token Scope
Scope parameter is a list of space-delimited, case-sensitive strings. Authorization server MAY fully or partially ignore scope. If different, MUST include "scope" response parameter. If omitted, authorization server MUST either use default value or fail request.

## 4. Obtaining Authorization
OAuth defines four grant types: authorization code, implicit, resource owner password credentials, client credentials. Extension mechanism provided.

### 4.1 Authorization Code Grant
Optimized for confidential clients. Steps: (A) client directs user-agent to authorization endpoint; (B) authorization server authenticates resource owner and obtains authorization; (C) authorization server redirects with authorization code; (D) client requests access token at token endpoint; (E) authorization server responds with access token and optionally refresh token.

#### 4.1.1 Authorization Request
Parameters: response_type=code (REQUIRED), client_id (REQUIRED), redirect_uri (OPTIONAL), scope (OPTIONAL), state (RECOMMENDED for CSRF protection).

#### 4.1.2 Authorization Response
Parameters: code (REQUIRED, MUST expire shortly, max 10 minutes RECOMMENDED, MUST NOT be used more than once), state (REQUIRED if present in request).

##### 4.1.2.1 Error Response
Error codes: invalid_request, unauthorized_client, access_denied, unsupported_response_type, invalid_scope, server_error, temporarily_unavailable. Error code values MUST NOT include characters outside set %x20-21 / %x23-5B / %x5D-7E. Optional error_description, error_uri.

#### 4.1.3 Access Token Request
Parameters: grant_type=authorization_code (REQUIRED), code (REQUIRED), redirect_uri (REQUIRED if included in authorization request), client_id (REQUIRED if client is not authenticating). Client MUST authenticate if confidential or issued credentials.

#### 4.1.4 Access Token Response
If valid and authorized, authorization server issues access token and optional refresh token as described in Section 5.1. If client authentication failed or invalid, error response as per Section 5.2.

### 4.2 Implicit Grant
Optimized for public clients. Access token issued directly in redirection URI fragment. Steps: (A) client directs to authorization endpoint; (B) authorization server authenticates; (C) redirects with access token in fragment; (D) user-agent requests web-hosted resource; (E) script extracts token; (F) token passed to client.

#### 4.2.1 Authorization Request
Parameters: response_type=token (REQUIRED), client_id (REQUIRED), redirect_uri (OPTIONAL), scope (OPTIONAL), state (RECOMMENDED). Authorization server MUST verify redirect URI matches registered.

#### 4.2.2 Access Token Response
Parameters: access_token (REQUIRED), token_type (REQUIRED), expires_in (RECOMMENDED), scope (OPTIONAL, REQUIRED if different from request), state (REQUIRED if present). Authorization server MUST NOT issue refresh token. Access token sent in URI fragment.

##### 4.2.2.1 Error Response
Same error codes as authorization code grant, returned in fragment.

### 4.3 Resource Owner Password Credentials Grant
Steps: (A) resource owner provides credentials to client; (B) client requests access token at token endpoint; (C) authorization server issues access token.

#### 4.3.1 Authorization Request and Response
Method of obtaining credentials beyond scope. Client MUST discard credentials once access token obtained.

#### 4.3.2 Access Token Request
Parameters: grant_type=password (REQUIRED), username (REQUIRED), password (REQUIRED), scope (OPTIONAL). Authorization server MUST require client authentication for confidential clients, authenticate client if included, validate credentials, protect endpoint against brute force attacks.

#### 4.3.3 Access Token Response
Same as Section 5.1.

### 4.4 Client Credentials Grant
MUST only be used by confidential clients. Steps: (A) client authenticates and requests token; (B) authorization server issues access token.

#### 4.4.1 Authorization Request and Response
No additional request needed; client authentication is authorization grant.

#### 4.4.2 Access Token Request
Parameters: grant_type=client_credentials (REQUIRED), scope (OPTIONAL). Client MUST authenticate.

#### 4.4.3 Access Token Response
Refresh token SHOULD NOT be included.

### 4.5 Extension Grants
Use absolute URI as "grant_type" value. If additional parameters needed, MUST register in OAuth Parameters registry.

## 5. Issuing an Access Token

### 5.1 Successful Response
Parameters: access_token (REQUIRED), token_type (REQUIRED, case insensitive), expires_in (RECOMMENDED), refresh_token (OPTIONAL), scope (OPTIONAL, REQUIRED if different). Response uses "application/json". Authorization server MUST include Cache-Control: no-store and Pragma: no-cache.

### 5.2 Error Response
HTTP 400 (Bad Request) unless otherwise specified. Error codes: invalid_request, invalid_client, invalid_grant, unauthorized_client, unsupported_grant_type, invalid_scope. Values MUST NOT include characters outside set %x20-21 / %x23-5B / %x5D-7E. Optional error_description, error_uri. Response uses "application/json".

## 6. Refreshing an Access Token
Parameters: grant_type=refresh_token (REQUIRED), refresh_token (REQUIRED), scope (OPTIONAL). Authorization server MUST require client authentication for confidential clients, authenticate client and ensure refresh token bound to that client, validate refresh token. May issue new refresh token, client MUST discard old.

## 7. Accessing Protected Resources
Resources server MUST validate access token. Method of using access token depends on token type.

### 7.1 Access Token Types
Client MUST NOT use access token if it does not understand the token type. Examples: bearer token (RFC 6750), MAC token.

### 7.2 Error Response
Resource server SHOULD inform client of error. New authentication schemes SHOULD register error codes in OAuth Extensions Error registry.

## 8. Extensibility

### 8.1 Defining Access Token Types
Can be registered (Section 11.1) or use absolute URI. Types using URI SHOULD be limited to vendor-specific. All other MUST be registered. Type names MUST conform to type-name ABNF.

### 8.2 Defining New Endpoint Parameters
Must be registered in OAuth Parameters registry (Section 11.2). Parameter names MUST conform to param-name ABNF.

### 8.3 Defining New Authorization Grant Types
Can be defined by assigning unique absolute URI for "grant_type" parameter. Additional token endpoint parameters MUST be registered in OAuth Parameters registry.

### 8.4 Defining New Authorization Endpoint Response Types
Must be registered in Authorization Endpoint Response Types registry (Section 11.3). Response type names MUST conform to response-type ABNF.

### 8.5 Defining Additional Error Codes
Extension error codes MUST be registered (Section 11.4) if used with registered extension. Error codes MUST conform to error ABNF and SHOULD be prefixed by identifying name.

## 9. Native Applications
Native applications can invoke external or embedded user-agent. Considerations: external browser may improve completion rate, provide familiar experience; embedded browser may offer usability but poses security challenges (phishing). When choosing between implicit and authorization code, native apps using authorization code SHOULD do so without client credentials. Implicit flow does not return refresh token.

## 10. Security Considerations

### 10.1 Client Authentication
Authorization server encouraged to consider stronger authentication than password. Web application clients MUST ensure confidentiality. Authorization server MUST NOT issue client passwords or credentials to native or user-agent-based applications for client authentication. MAY issue for specific installation. When client authentication not possible, SHOULD employ other means.

### 10.2 Client Impersonation
Authorization server MUST authenticate client whenever possible. SHOULD enforce explicit resource owner authentication.

### 10.3 Access Tokens
Must be kept confidential in transit and storage. MUST only be transmitted using TLS. Implicit grant exposes token in URI fragment. Authorization server MUST ensure tokens cannot be generated, modified, or guessed. Client SHOULD request minimal scope.

### 10.4 Refresh Tokens
Must be kept confidential. Authorization server MUST maintain binding to client. SHOULD deploy means to detect abuse, e.g., rotation.

### 10.5 Authorization Codes
SHOULD be transmitted over secure channel. Client redirection endpoint MUST require TLS if client relies on authorization code for authentication. Must be short lived and single-use.

### 10.6 Authorization Code Redirection URI Manipulation
Authorization server MUST ensure redirection URI used to obtain code is identical to that used when exchanging for token. Must require public clients and SHOULD require confidential clients to register URIs.

### 10.7 Resource Owner Password Credentials
Carries higher risk. Authorization server and client SHOULD minimize use.

### 10.8 Request Confidentiality
Access tokens, refresh tokens, resource owner passwords, client credentials MUST NOT be transmitted in clear. "state" and "scope" SHOULD NOT include sensitive information.

### 10.9 Ensuring Endpoint Authenticity
Authorization server MUST require TLS with server authentication for authorization and token endpoints. Client MUST validate certificate per RFC 6125.

### 10.10 Credentials-Guessing Attacks
Authorization server MUST prevent guessing. Probability of guessing tokens MUST be ≤ 2^(-128), SHOULD be ≤ 2^(-160). Must protect credentials for end-user usage.

### 10.11 Phishing Attacks
Service providers should educate end-users. Authorization servers MUST require TLS on endpoints used for end-user interaction.

### 10.12 Cross-Site Request Forgery
Client MUST implement CSRF protection for redirection URI. SHOULD use "state" parameter. Authorization server MUST implement CSRF protection for its authorization endpoint.

### 10.13 Clickjacking
Native applications SHOULD use external browsers. Authorization server can use "x-frame-options" header.

### 10.14 Code Injection and Input Validation
Authorization server and client MUST sanitize (and validate when possible) any value received, especially "state" and "redirect_uri".

### 10.15 Open Redirectors
Improperly configured endpoints can operate as open redirectors.

### 10.16 Misuse of Access Token to Impersonate Resource Owner in Implicit Flow
Any public client that assumes only resource owner can present a valid access token is vulnerable. Any specification that uses authorization process as delegated end-user authentication MUST NOT use implicit flow without additional security mechanisms.

## 11. IANA Considerations

### 11.1 OAuth Access Token Types Registry
Registration with Specification Required after two-week review on oauth-ext-review@ietf.org.

#### 11.1.1 Registration Template
Includes type name, additional token endpoint response parameters, HTTP authentication schemes, change controller, specification document(s).

### 11.2 OAuth Parameters Registry
Registration with Specification Required. Initial registry contents are listed in Section 11.2.2.

#### 11.2.1 Registration Template
Includes parameter name, parameter usage location, change controller, specification document(s).

#### 11.2.2 Initial Registry Contents
Lists all parameters defined in RFC 6749 with their usage locations.

### 11.3 OAuth Authorization Endpoint Response Types Registry
Registration with Specification Required.

#### 11.3.1 Registration Template
Includes response type name, change controller, specification document(s).

#### 11.3.2 Initial Registry Contents
- code
- token

### 11.4 OAuth Extensions Error Registry
Registration with Specification Required.

#### 11.4.1 Registration Template
Includes error name, error usage location, related protocol extension, change controller, specification document(s).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The authorization server MUST verify the identity of the resource owner for the authorization endpoint. | MUST | Section 3.1 |
| R2 | The authorization endpoint URI MUST NOT include a fragment component. | MUST | Section 3.1 |
| R3 | The authorization server MUST require use of TLS on authorization and token endpoints. | MUST | Sections 3.1, 3.2 |
| R4 | The authorization server MUST support HTTP GET method for the authorization endpoint. | MUST | Section 3.1 |
| R5 | Parameters sent without a value MUST be treated as omitted. | MUST | Sections 3.1, 3.2 |
| R6 | The authorization server MUST ignore unrecognized request parameters. | MUST | Sections 3.1, 3.2 |
| R7 | Request and response parameters MUST NOT be included more than once. | MUST | Sections 3.1, 3.2 |
| R8 | The redirection endpoint URI MUST be an absolute URI. | MUST | Section 3.1.2 |
| R9 | The redirection endpoint URI MUST NOT include a fragment component. | MUST | Section 3.1.2 |
| R10 | The authorization server MUST require public clients and confidential clients using implicit grant to register their redirection endpoint. | MUST | Section 3.1.2.2 |
| R11 | The client MUST use HTTP POST method for access token requests. | MUST | Section 3.2 |
| R12 | Confidential clients MUST authenticate with token endpoint. | MUST | Section 3.2.1 |
| R13 | For authorization code grant, the response type value MUST be "code". | MUST | Section 4.1.1 |
| R14 | The client identifier "client_id" is REQUIRED in authorization request. | MUST | Section 4.1.1 |
| R15 | The authorization code MUST expire shortly after issuance (max 10 min RECOMMENDED). | MUST | Section 4.1.2 |
| R16 | The authorization code MUST NOT be used more than once. | MUST | Section 4.1.2 |
| R17 | If authorization code used more than once, authorization server MUST deny request and SHOULD revoke tokens. | MUST | Section 4.1.2 |
| R18 | The "state" parameter is REQUIRED in authorization response if present in request. | MUST | Section 4.1.2 |
| R19 | For implicit grant, response type value MUST be "token". | MUST | Section 4.2.1 |
| R20 | The authorization server MUST verify redirect URI for implicit grant against registered URIs. | MUST | Section 4.2.2.1 |
| R21 | Authorization server MUST NOT issue refresh token in implicit grant. | MUST | Section 4.2.2 |
| R22 | For password grant, the "grant_type" MUST be "password". | MUST | Section 4.3.2 |
| R23 | For client credentials grant, the "grant_type" MUST be "client_credentials". | MUST | Section 4.4.2 |
| R24 | Client credentials grant MUST only be used by confidential clients. | MUST | Section 4.4 |
| R25 | Successful token response MUST include "access_token" and "token_type". | MUST | Section 5.1 |
| R26 | Authorization server MUST include Cache-Control: no-store and Pragma: no-cache in token response. | MUST | Section 5.1 |
| R27 | Access token credentials MUST be kept confidential in transit and storage. | MUST | Section 10.3 |
| R28 | Authorization server MUST ensure access tokens cannot be generated, modified, or guessed. | MUST | Section 10.3 |
| R29 | Refresh tokens MUST be kept confidential in transit and storage. | MUST | Section 10.4 |
| R30 | Authorization server MUST maintain binding between refresh token and client. | MUST | Section 10.4 |
| R31 | Authorization server MUST require TLS on all endpoints used for end-user interaction. | MUST | Section 10.11 |
| R32 | Client MUST implement CSRF protection for redirection URI. | MUST | Section 10.12 |
| R33 | Authorization server MUST implement CSRF protection for authorization endpoint. | MUST | Section 10.12 |
| R34 | Authorization server MUST sanitize (and validate when possible) any value received, especially "state" and "redirect_uri". | MUST | Section 10.14 |

## Informative Annexes (Condensed)
- **Appendix A. Augmented Backus-Naur Form (ABNF) Syntax**: Provides formal ABNF syntax for all parameter elements defined in the specification, including client_id, client_secret, response_type, scope, state, redirect_uri, error, error_description, error_uri, grant_type, code, access_token, token_type, expires_in, username, password, refresh_token, and endpoint parameters.
- **Appendix B. Use of application/x-www-form-urlencoded Media Type**: Addresses incompleteness of the media type definition in HTML 4.01. Specifies that names and values MUST be encoded using UTF-8 first, then URL-encoded. When parsing, reverse the process.
- **Appendix C. Acknowledgements**: Lists editors and contributors to the specification, including prior work on OAuth 1.0 and OAuth WRAP.