---
{
  "title": "Health Relationship Trust Profile for OAuth 2.0",
  "url": "https://openid.net/specs/openid-heart-oauth2-1_0-ID1.html",
  "domain": "openid.net",
  "depth": 2,
  "relevance_score": 0.51,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 45515,
  "crawled_at": "2026-04-23T20:50:25"
}
---

Health Relationship Trust Profile for OAuth 2.0
J. Richer, Ed.
February 15, 2016
Health Relationship Trust Profile for OAuth 2.0
openid-heart-oauth2-1_0
Abstract
The OAuth 2.0 protocol framework defines a mechanism to allow a resource owner to delegate access to a protected resource for a client application.
This specification profiles the OAuth 2.0 protocol framework to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) the healthcare domain.
Table of Contents
1.
Introduction
1.1.
Requirements Notation and Conventions
1.2.
Terminology
2.
OAuth 2.0 Client Profiles
2.1.
Client Types
2.1.1.
Full Client with User Delegation
2.1.2.
Browser-embedded Client with User Delegation
2.1.3.
Direct Access Client
2.2.
Requests to the Token Endpoint
2.3.
Requests to the Authorization Endpoint
3.
Client Registration
3.1.
Redirect URI
3.2.
Dynamic Registration
4.
OAuth 2.0 Server Profile
4.1.
Discovery
4.2.
JWT Bearer Tokens
4.3.
Token Lifetimes
4.4.
Token Revocation and Introspection
5.
Requests to the Protected Resource
6.
Scopes
7.
Advanced OAuth Security Options
7.1.
Client TLS Authentication
7.2.
Proof of Possession Tokens
8.
Security Considerations
9.
Normative References
Appendix A.
Acknowledgements
Appendix B.
Notices
Appendix C.
Document History
Author's Address
1.
Introduction
This document profiles the OAuth 2.0 web authorization framework for use in the context of securing web-facing application programming interfaces (APIs), particularly Representational State Transfer (RESTful) APIs. The OAuth 2.0 specifications accommodate a wide range of implementations with varying security and usability considerations, across different types of software clients. To achieve this flexibility, the standard makes many security controls optional. OAuth implementations using only the minimum mandatory security measures require minimal effort on the part of developers and users, but they also fail to prevent known attacks and are unsuitable for protecting sensitive data. The OAuth 2.0 client and server profiles defined in this document serve two purposes: 1. Define a mandatory baseline set of security controls suitable for a wide range of use cases, while maintaining reasonable ease of implementation and functionality 2.  Identify optional advanced security controls for sensitive use cases where heightened risks justify more stringent controls that increase the required implementation effort and may reduce or restrict functionality
This OAuth profile is intended to be shared broadly, and ideally to influence OAuth implementations in other domains besides health care.
1.1.
Requirements Notation and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in
RFC 2119
[RFC2119]
.
All uses of
JSON Web Signature (JWS)
[RFC7515]
and
JSON Web Encryption (JWE)
[RFC7516]
data structures in this specification utilize the JWS Compact Serialization or the JWE Compact Serialization; the JWS JSON Serialization and the JWE JSON Serialization are not used.
1.2.
Terminology
This specification uses the terms "Access Token", "Authorization Code", "Authorization Endpoint", "Authorization Grant", "Authorization Server", "Client", "Client Authentication", "Client Identifier", "Client Secret", "Grant Type", "Protected Resource", "Redirection URI", "Refresh Token", "Resource Owner", "Resource Server", "Response Type", and "Token Endpoint" defined by
OAuth 2.0
[RFC6749]
, the terms "Claim Name", "Claim Value", and "JSON Web Token (JWT)" defined by
JSON Web Token (JWT)
[RFC7519]
, and the terms defined by
OpenID Connect Core 1.0
[OpenID.Core]
.
2.
OAuth 2.0 Client Profiles
2.1.
Client Types
The following profile descriptions give patterns of deployment for use in different types of client applications based on the OAuth grant type. The resource owner password credentials grant type defined in
[RFC6749]
is intentionally omitted from this discussion, and MUST NOT be used under these profiles. Additional grant types, such as assertions, chained tokens, or other mechanisms, are out of scope of this profile and must be covered separately by appropriate profile documents.
2.1.1.
Full Client with User Delegation
This client type applies to clients that act on behalf of a particular resource owner and require delegation of that user’s authority to access the protected resource.  Furthermore, these clients are capable of interacting with a separate web browser application to facilitate the resource owner’s interaction with the authentication endpoint of the authorization server.
These clients MUST use the authorization code flow of OAuth 2 by sending the resource owner to the authorization endpoint to obtain authorization. The user MUST authenticate to the authorization endpoint. The user’s web browser is then redirected back to a URI hosted by the client, from which the client can obtain an authorization code passed as a query parameter. The client then presents that authorization code along with its own credentials to the authorization server's token endpoint to obtain an access token.
The authorization code flow is supported only for confidential clients. Examples of this client type include web applications and native applications that can store installation-instance-specific client credentials securely. For applications that can have multiple identical instances operating in different environments and running simultaneously, such as with a native application on a mobile device, it is RECOMMENDED to generate a unique key on the device and use
dynamic client registration
[RFC7591]
to register that key with the authorization server. Client credentials MUST NOT be shared among instances of client software.
This client type MAY request and be issued a refresh token if the security parameters of the access request allow for it.
2.1.2.
Browser-embedded Client with User Delegation
This client type applies to clients that act on behalf of a particular resource owner and require delegation of that user’s authority to access the protected resource.  Furthermore, these clients are embedded within a web browser and effectively share an active session between systems.
These clients use the implicit flow of OAuth 2 by sending a resource owner to the authorization endpoint to obtain authorization. The user MUST authenticate to the authorization endpoint. The user’s web browser is then redirected back to a URI hosted by the client, from which the client can directly obtain an access token. Since the client itself never authenticates to the server and the token is made available directly to the browser, this flow is appropriate only for clients embedded within a web browser, such as a JavaScript client with no back-end server component.  Wherever possible, it is preferable to use the authorization code flow due to its superior security properties.
This client type MUST NOT request or be issued a refresh token.  Access tokens issued to this type of client MUST be short lived and SHOULD expire when the user's authenticated session with the client expires.
2.1.3.
Direct Access Client
This profile applies to clients that connect directly to protected resources and do not act on behalf of a particular resource owner, such as those clients that facilitate bulk transfers.
These clients use the client credentials flow of OAuth 2 by sending a request to the token endpoint with the client's credentials and obtaining an access token in the response. Since this profile does not involve an authenticated user, this flow is appropriate only for trusted applications, such as those that would traditionally use a developer key. For example, a partner system that performs bulk data transfers between two systems would be considered a direct access client.
This client type MUST NOT request or be issued a refresh token.
2.2.
Requests to the Token Endpoint
Full clients and direct access clients as defined above MUST authenticate to the authorization server's token endpoint using a JWT assertion as defined by the
JWT Profile for OAuth 2.0 Client Authentication and Authorization Grants
[RFC7523]
and the
private_key_jwt
method defined in
OpenID Connect Core
[OpenID.Core]
. The assertion MUST use the claims as follows:
iss
the client ID of the client creating the token
sub
the client ID of the client creating the token
aud
the URL of the authorization server's token endpoint
iat
the time that the token was created by the client
exp
the expiration time, after which the token MUST be considered invalid
jti
a unique identifier generated by the client for this authentication. This identifier MUST contain at least 128 bits of entropy and MUST NOT be re-used by any subsequent authentication token.
The following sample claim set illustrates the use of the required claims for a client authentication JWT as defined in this profile; additional claims MAY be included in the claim set.
{
   "iss": "55f9f559-2496-49d4-b6c3-351a586b7484",
   "sub": "55f9f559-2496-49d4-b6c3-351a586b7484",
   "aud": "https://idp-p.example.com/token",
   "iat": 1418698788,
   "exp": 1418698848,
   "jti": "1418698788/107c4da5194df463e52b56865c5af34e5595"
}
The JWT assertion MUST be signed by the client using the client's private key. See
Section 3
for mechanisms by which the client can make its public key known to the server. The authorization server MUST support the RS256 signature method (the Rivest, Shamir, and Adleman (RSA) signature algorithm with a 256-bit hash) and MAY use other asymmetric signature methods listed in the JSON Web Algorithms (
JWA
[RFC7518]
) specification.
The following sample JWT contains the above claims and has been signed using the RS256 JWS algorithm and the client's own private key (with line breaks for display purposes only):
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.ew0KICAgImlzcyI6ICI1NWY5ZjU1OS0yNDk2LTQ5Z
DQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgInN1YiI6ICI1NWY5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0
zNTFhNTg2Yjc0ODQiLA0KICAgImF1ZCI6ICJodHRwczovL2lkcC1wLmV4YW1wbGUuY29tL3Rva2VuI
iwNCiAgICJpYXQiOiAxNDE4Njk4Nzg4LA0KICAgImV4cCI6IDE0MTg2OTg4NDgsDQogICAianRpIjo
gIjE0MTg2OTg3ODgvMTA3YzRkYTUxOTRkZjQ2M2U1MmI1Njg2NWM1YWYzNGU1NTk1Ig0KfQ.t-_gX8
JQGq3G2OEc2kUCQ8zVj7pqff87Sua5nktLIHj28l5onO5VpsL4sRHIGOvrpo7XO6jgtPWy3iLXv3-N
Lyo1TWHbtErQEGpmf7nKiNxVCXlGYJXSDJB6shP3OfvdUc24urPJNUGBEDptIgT7-Lhf6BbwQNlMQu
bNeOPRFDqQoLWqe7UxuI06dKX3SEQRMqcxYSIAfP7CQZ4WLuKXb6oEbaqz6gL4l6p83G7wKGDeLETO
THszt-ZjKR38v4F_MnSrx8e0iIqgZwurW0RtetEWvynOCJXk-p166T7qZR45xuCxgOotXY6O3et4n7
7GtgspMgOEKj3b_WpCiuNEwQ
This is sent in the request to the token endpoint as in the following example:
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Rack::OAuth2 (1.0.8.7) (2.5.3.2, ruby 2.1.3 (2014-09-19))
Accept: */*
Date: Tue, 16 Dec 2014 02:59:48 GMT
Content-Length: 884
Host: idp-p.example.com

grant_type=authorization_code&code=sedaFh&scope=openid+email
&client_id=55f9f559-2496-49d4-b6c3-351a586b7484
&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer
&client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.ew0KICAgImlzcyI6ICI1NWY
5ZjU1OS0yNDk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgInN1YiI6ICI1NWY5ZjU1OS0yN
Dk2LTQ5ZDQtYjZjMy0zNTFhNTg2Yjc0ODQiLA0KICAgImF1ZCI6ICJodHRwczovL2lkcC1wLmV4YW1
wbGUuY29tL3Rva2VuIiwNCiAgICJpYXQiOiAxNDE4Njk4Nzg4LA0KICAgImV4cCI6IDE0MTg2OTg4N
DgsDQogICAianRpIjogIjE0MTg2OTg3ODgvMTA3YzRkYTUxOTRkZjQ2M2U1MmI1Njg2NWM1YWYzNGU
1NTk1Ig0KfQ.t-_gX8JQGq3G2OEc2kUCQ8zVj7pqff87Sua5nktLIHj28l5onO5VpsL4sRHIGOvrpo
7XO6jgtPWy3iLXv3-NLyo1TWHbtErQEGpmf7nKiNxVCXlGYJXSDJB6shP3OfvdUc24urPJNUGBEDpt
IgT7-Lhf6BbwQNlMQubNeOPRFDqQoLWqe7UxuI06dKX3SEQRMqcxYSIAfP7CQZ4WLuKXb6oEbaqz6g
L4l6p83G7wKGDeLETOTHszt-ZjKR38v4F_MnSrx8e0iIqgZwurW0RtetEWvynOCJXk-p166T7qZR45
xuCxgOotXY6O3et4n77GtgspMgOEKj3b_WpCiuNEwQ
Authorization servers MAY require some clients to additionally authenticate using mutual Transport Layer Security (TLS) authentication, with the client's TLS certificate having been registered at the authorization server alongside its key. Due to problems inherent in configuring a large mutual TLS network at scale, it is RECOMMENDED by this profile that such authentication be limited to instances where the security benefits sufficiently outweigh the complications.
2.3.
Requests to the Authorization Endpoint
Full clients and browser-embedded clients making a request to the authorization endpoint MUST use an unpredictable value for the state parameter with at least 128 bits of entropy. Clients MUST validate the value of the
state
parameter upon return to the redirect URI and MUST ensure that the state value is securely tied to the user’s current session (e.g., by relating the state value to a session identifier issued by the client software to the browser).
Clients MUST include their full redirect URIs in the authorization request. To prevent open redirection and other injection attacks, the authorization server MUST match the entire redirect URI using a direct string comparison against registered values and MUST reject requests with invalid or missing redirect URIs.
The following is a sample response from a web-based client to the end user’s browser for the purpose of redirecting the end user to the authorization server's authorization endpoint:
HTTP/1.2 302 Found
Cache-Control: no-cache
Connection: close
Content-Type: text/plain; charset=UTF-8
Date: Wed, 07 Jan 2015 20:24:15 GMT
Location: https://idp-p.example.com/authorize?client_id=55f9f559-2496-49d4-b6c3-351a586b7484&nonce=cd567ed4d958042f721a7cdca557c30d&response_type=code&scope=openid+email 
Status: 302 Found
This causes the browser to send the following request to the authorization endpoint:
GET /authorize?client_id=55f9f559-2496-49d4-b6c3-351a586b7484&nonce=cd567ed4d958042f721a7cdca557c30d&response_type=code&scope=openid+email HTTP/1.1 
Host: idp-p.example.com 
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.2.0 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 
Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate 
Referer: https://ehr-va.example.com/portal/signin 
Cookie: JSESSIONID=706D5B3A7B3AB3FCE8C6AA7201B8B9CF 
Connection: keep-alive
3.
Client Registration
All clients MUST register with the authorization server. For client software that may be installed on multiple client instances, such as native applications or web application software, each client instance MUST receive a unique client identifier from the authorization server.
Clients using the authorization code or client credentials grant type MUST have a public and private key pair for use in authentication to the token endpoint. These clients MUST register their public keys in their client registration metadata by either sending the public key directly in the
jwks
field or by registering a
jwks_uri
that MUST be reachable by the authorization server. It is RECOMMENDED that clients use a
jwks_uri
if possible as this allows for key rotation more easily.
The
jwks
field or the content available from the
jwks_uri
of a client MUST contain a public key in
JSON Web Key Set (JWK Set)
[RFC7517]
format. The authorization server MUST validate the content of the client's registered jwks_uri document and verify that it contains a JWK Set. The following example is of a 2048-bit RSA key:
{
   "keys": [
     {
       "alg": "RS256",
       "e": "AQAB",
       "n": "kAMYD62n_f2rUcR4awJX4uccDt0zcXRssq_mDch5-ifcShx9aTtTVza23P
Tn3KaKrsBXwWcfioXR6zQn5eYdZQVGNBfOR4rxF5i7t3hfb4WkS50EK1gBYk2lO9NSrQ-xG
9QsUsAnN6RHksXqsdOqv-nxjLexDfIJlgbcCN9h6TB-C66ZXv7PVhl19gIYVifSU7liHkLe
0l0fw7jUI6rHLHf4d96_neR1HrNIK_xssr99Xpv1EM_ubxpktX0T925-qej9fMEpzzQ5HLm
cNt1H2_VQ_Ww1JOLn9vRn-H48FDj7TxlIT74XdTZgTv31w_GRPAOfyxEw_ZUmxhz5Z-gTlQ",
       "kty": "RSA",
       "kid": "oauth-client"
     }
   ]
}
For reference, the corresponding public/private key pair for this public key is the following (in JWK format):
{
   "alg": "RS256",
   "d": "PjIX4i2NsBQuOVIw74ZDjqthYsoFvaoah9GP-cPrai5s5VUIlLoadEAdGbBrss
_6dR58x_pRlPHWh04vLQsFBuwQNc9SN3O6TAaai9Jg5TlCi6V0d4O6lUoTYpMR0cxFIU-xF
MwII--_OZRgmAxiYiAXQj7TKMKvgSvVO7-9-YdhMwHoD-UrJkfnZckMKSs0BoAbjReTski3
IV9f1wVJ53_pmr9NBpiZeHYmmG_1QDSbBuY35Zummut4QShF-fey2gSALdp9h9hRk1p1fsT
ZtH2lwpvmOcjwDkSDv-zO-4Pt8NuOyqNVPFahROBPlsMVxc_zjPck8ltblalBHPo6AQ",
   "e": "AQAB",
   "n": "kAMYD62n_f2rUcR4awJX4uccDt0zcXRssq_mDch5-ifcShx9aTtTVza23PTn3K
aKrsBXwWcfioXR6zQn5eYdZQVGNBfOR4rxF5i7t3hfb4WkS50EK1gBYk2lO9NSrQ-xG9QsU
sAnN6RHksXqsdOqv-nxjLexDfIJlgbcCN9h6TB-C66ZXv7PVhl19gIYVifSU7liHkLe0l0f
w7jUI6rHLHf4d96_neR1HrNIK_xssr99Xpv1EM_ubxpktX0T925-qej9fMEpzzQ5HLmcNt1
H2_VQ_Ww1JOLn9vRn-H48FDj7TxlIT74XdTZgTv31w_GRPAOfyxEw_ZUmxhz5Z-gTlQ",
   "kty": "RSA",
   "kid": "oauth-client" 
}
Note that the second example contains both the public and private keys, while the first example contains the public key only.
3.1.
Redirect URI
Clients using the authorization code or implicit grant types MUST register their full redirect URIs. The Authorization Server MUST validate the redirect URI given by the client at the authorization endpoint using strict string comparison.
A client MUST protect the values passed back to its redirect URI by ensuring that the redirect URI is one of the following:
Hosted on a website with Transport Layer Security (TLS) protection (a Hypertext Transfer Protocol – Secure (HTTPS) URI)
Hosted on the local domain of the client (e.g., http://localhost/)
Hosted on a client-specific non-remote-protocol URI scheme (e.g., myapp://)
Clients MUST NOT have URIs in more than one category and SHOULD NOT have multiple redirect URIs on different domains.
Clients MUST NOT forward values passed back to their redirect URIs to other arbitrary or user-provided URIs (a practice known as an "open redirector”).
3.2.
Dynamic Registration
Authorization servers MUST support dynamic client registration, and clients MAY register using the
Dynamic Client Registration Protocol
[RFC7591]
for authorization code or implicit grant types. Clients MUST NOT dynamically register for the client credentials grant type. Authorization servers MAY limit the scopes available to dynamically registered clients.
Authorization servers MUST signal to end users that a client was dynamically registered on the authorization screen. Authorization servers MAY accept signed software statements as described in
[RFC7591]
issued to client software developers from a trusted registration entity, and MUST indicate to the end user that such a statement was used in the client's registration. The software statement can be used to tie together many instances of the same client software that will be run, dynamically registered, and authorized separately at runtime. The software statement MUST include the following client metadata parameters:
redirect_uris
array of redirect URIs used by the client; subject to the requirements listed in
Section 3.1
grant_types
grant type used by the client; must be "authorization_code” or "implicit”
jwks_uri or jwks
client's public key in JWK Set format; if jwks_uri is used it MUST be reachable by the Authorization Server and point to the client's public key set
client_name
human-readable name of the client
client_uri
URL of a web page containing further information about the client
4.
OAuth 2.0 Server Profile
All servers MUST conform to applicable recommendations found in the Security Considerations sections of
[RFC6749]
and those found in the
OAuth Threat Model Document
[RFC6819]
.
The authorization server MUST support the
authorization_code
,
implicit
, and
client_credentials
grant types as described above. The authorization server MUST limit each registered client (identified by a client ID) to a single grant type only. The authorization server MUST enforce client authentication as described above for the authorization code and client credentials grant types. The authorization server MUST validate all redirect URIs for authorization code and implicit grant types.
The authorization server MUST protect all communications to and from its OAuth endpoints using TLS.
4.1.
Discovery
The authorization server MUST provide an
OpenID Connect service discovery
[OpenID.Discovery]
endpoint listing the components relevant to the OAuth protocol:
issuer
The fully qualified issuer URL of the server
authorization_endpoint
The fully qualified URL of the server's authorization endpoint defined by
OAuth 2.0
[RFC6749]
token_endpoint
The fully qualified URL of the server's token endpoint defined by
OAuth 2.0
[RFC6749]
introspection_endpoint
The fully qualified URL of the server's introspection endpoint defined by
OAuth Token Introspection
[RFC7662]
revocation_endpoint
The fully qualified URL of the server's revocation endpoint defined by
OAuth 2.0 Token Revocation
[RFC7009]
jwks_uri
The fully qualified URI of the server's public key in
JWK Set
[RFC7517]
format
If the authorization server is also an OpenID Connect Provider, it MUST provide a discovery endpoint meeting the requirements listed in Section 6 of the HEART OpenID Connect profile.
The following example shows the JSON document found at a discovery endpoint for an authorization server:
{
  "request_parameter_supported": true,
  "registration_endpoint": "https://idp-p.example.com/register",
  "userinfo_signing_alg_values_supported": [
    "HS256", "HS384", "HS512", "RS256", "RS384", "RS512"
  ],
  "token_endpoint": "https://idp-p.example.com/token",
  "request_uri_parameter_supported": false,
  "request_object_encryption_enc_values_supported": [
    "A192CBC-HS384", "A192GCM", "A256CBC+HS512",
    "A128CBC+HS256", "A256CBC-HS512",
    "A128CBC-HS256", "A128GCM", "A256GCM"
  ],
  "token_endpoint_auth_methods_supported": [
    "client_secret_post",
    "client_secret_basic",
    "client_secret_jwt",
    "private_key_jwt",
    "none"
  ],
  "jwks_uri": "https://idp-p.example.com/jwk",
  "authorization_endpoint": "https://idp-p.example.com/authorize",
  "require_request_uri_registration": false,
  "introspection_endpoint": "https://idp-p.example.com/introspect",
  "request_object_encryption_alg_values_supported": [
    "RSA-OAEP", ?RSA1_5", "RSA-OAEP-256"
  ],
  "service_documentation": "https://idp-p.example.com/about",
  "response_types_supported": [
    "code", "token"
  ],
  "token_endpoint_auth_signing_alg_values_supported": [
    "HS256", "HS384", "HS512", "RS256", "RS384", "RS512"
  ],
  "revocation_endpoint": "https://idp-p.example.com/revoke",
  "request_object_signing_alg_values_supported": [
    "HS256", "HS384", "HS512", "RS256", "RS384", "RS512"
  ],
  "grant_types_supported": [
    "authorization_code",
    "implicit",
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "client_credentials",
    "urn:ietf:params:oauth:grant_type:redelegate"
  ],
  "scopes_supported": [
    "profile", "openid", "email", "address", "phone", "offline_access"
  ],
  "op_tos_uri": "https://idp-p.example.com/about",
  "issuer": "https://idp-p.example.com/",
  "op_policy_uri": "https://idp-p.example.com/about"
}
Clients and protected resources SHOULD cache this discovery information. It is RECOMMENDED that servers provide cache information through HTTP headers and make the cache valid for at least one week.
The server MUST provide its public key in JWK Set format, such as the following 2048-bit RSA public key:
{
  "keys": [
    {
      "alg": "RS256",
      "e": "AQAB",
      "n": "o80vbR0ZfMhjZWfqwPUGNkcIeUcweFyzB2S2T-hje83IOVct8gVg9FxvHPK1R
eEW3-p7-A8GNcLAuFP_8jPhiL6LyJC3F10aV9KPQFF-w6Eq6VtpEgYSfzvFegNiPtpMWd7C43
EDwjQ-GrXMVCLrBYxZC-P1ShyxVBOzeR_5MTC0JGiDTecr_2YT6o_3aE2SIJu4iNPgGh9Mnyx
dBo0Uf0TmrqEIabquXA1-V8iUihwfI8qjf3EujkYi7gXXelIo4_gipQYNjr4DBNlE0__RI0kD
U-27mb6esswnP2WgHZQPsk779fTcNDBIcYgyLujlcUATEqfCaPDNp00J6AbY6w",
      "kty": "RSA",
      "kid": "rsa1"
    }
  ]
}
Clients and protected resources SHOULD cache this key. It is RECOMMENDED that servers provide cache information through HTTP headers and make the cache valid for at least one week.
4.2.
JWT Bearer Tokens
The server MUST issue tokens as JWTs with, at minimum, the following claims:
iss
the issuer URL of the server that issued the token
azp
The client id of the client to whom this token was issued
sub
The identifier of the end-user that authorized this client, or the client id of a client acting on its own behalf (such as a bulk transfer)
kid
the key ID of the keypair used to sign this token
exp
the expiration time (integer number of seconds since from 1970-01-01T00:00:00Z UTC), after which the token MUST be considered invalid
jti
A unique JWT Token ID value with at least 128 bits of entropy. This value MUST NOT be re-used in another token.  Clients MUST check for reuse of jti values and reject all tokens issued with duplicate jti values.
The server MAY issue tokens with an aud (audience) claim whose value is an array containing the identifier(s) of protected resource(s) for which the token is valid, if this information is known. The aud claim may contain multiple values if the token is valid for multiple protected resources.
The following sample claim set illustrates the use of the required claims for an access token as defined in this profile; additional claims MAY be included in the claim set:
{
   "exp": 1418702388,
   "azp": "55f9f559-2496-49d4-b6c3-351a586b7484",
   "iss": "https://idp-p.example.com/",
   "jti": "2402f87c-b6ce-45c4-95b0-7a3f2904997f",
   "iat": 1418698788,
   "kid": "rsa1"
}
The access tokens MUST be signed with
JWS
[RFC7515]
. The authorization server MUST support the RS256 signature method for tokens and MAY use other asymmetric signing methods. This example access token has been signed with the server's private key using RS256:
eyJhbGciOiJSUzI1NiJ9.ew0KICAgImV4cCI6IDE0MTg3MDIzODgsDQogICAiYXpwIjo
gIjU1ZjlmNTU5LTI0OTYtNDlkNC1iNmMzLTM1MWE1ODZiNzQ4NCIsDQogICAiaXNzIjo
gImh0dHBzOi8vaWRwLXAuZXhhbXBsZS5jb20vIiwNCiAgICJqdGkiOiAiMjQwMmY4N2M
tYjZjZS00NWM0LTk1YjAtN2EzZjI5MDQ5OTdmIiwNCiAgICJpYXQiOiAxNDE4Njk4Nzg
4LA0KICAgImtpZCI6ICJyc2ExIg0KfQ.iB6Ix8Xeg-L-nMStgE1X75w7zgXabzw7znWU
ECOsXpHfnYYqb-CET9Ah5IQyXIDZ20qEyN98UydgsTpiO1YJDDcZV4f4DgY0ZdG3yBW3
XqwUQwbgF7Gwza9Z4AdhjHjzQx-lChXAyfL1xz0SBDkVbJdDjtXbvaSIyfF7ueWF3M1C
M70-GXuRY4iucKbuytz9e7eW4Egkk4Aagl3iTk9-l5V-tvL6dYu8IlR93GKsaKE8bng0
EZ04xcnq8s4V5Yykuc_NARBJENiKTJM8w3wh7xWP2gvMp39Y0XnuCOLyIx-J1ttX83xm
pXDaLyyY-4HT9XHT9V73fKF8rLWJu9grrA
Refresh tokens SHOULD be signed with
JWS
[RFC7515]
using the same public key and contain the same set of claims as the access tokens.
The authorization server MAY encrypt access tokens and refresh tokens using
JWE
[RFC7516]
. Access tokens MUST be encrypted using the public key of either the protected resource or the authorization server itself. Refresh tokens MUST be encrypted using the authorization server's public key.
4.3.
Token Lifetimes
This profile provides RECOMMENDED lifetimes for different types of tokens issued to different types of clients. Specific applications MAY issue tokens with different lifetimes. Any active token MAY be revoked at any time.
For clients using the authorization code grant type, access tokens SHOULD have a valid lifetime no greater than one hour, and refresh tokens (if issued) SHOULD have a valid lifetime no greater than twenty-four hours.
For clients using the implicit grant type, access tokens SHOULD have a valid lifetime no greater than fifteen minutes.
For clients using the client credentials grant type, access tokens SHOULD have a valid lifetime no greater than six hours.
4.4.
Token Revocation and Introspection
The authorization server MUST supply
token revocation
[RFC7009]
and
token introspection
[RFC7662]
endpoints to allow clients and protected resources to manage the lifecycle of issued tokens.
Token revocation allows a client to signal to an authorization server that a given token will no longer be used. A client MUST immediately discard the token and not use it again after revoking it.
Token introspection allows a protected resource to query the authorization server for metadata about a token. The protected resource makes a request like the following to the token introspection endpoint:
POST /introspect HTTP/1.1
User-Agent: Faraday v0.9.0
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3
Accept: */*
Connection: close
Host: as-va.example.com
Content-Length: 1412

client_assertion=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3M
iOiJhMmMzNjkxOS0wMWZmLTQ4MTAtYTgyOS00MDBmYWQzNTczNTEiLCJzdWIi
OiJhMmMzNjkxOS0wMWZmLTQ4MTAtYTgyOS00MDBmYWQzNTczNTEiLCJhdWQiO
iJodHRwczovL2FzLXZhLmV4YW1wbGUuY29tL3Rva2VuIiwiaWF0IjoxNDE4Nj
k4ODE0LCJleHAiOjE0MTg2OTg4NzQsImp0aSI6IjE0MTg2OTg4MTQvZmNmNDQ
2OGY2MDVjNjE1NjliOWYyNGY5ODJlMTZhZWY2OTU4In0.md7mFdNBaGhiJfE_
pFkAAWA5S-JBvDw9Dk7pOOJEWcL08JGgDFoi9UDbg3sHeA5DrrCYGC_zw7fCG
c9ovpfMB7W6YN53hGU19LtzzFN3tv9FNRq4KIzhK15pns9jckKtui3HZ25L_B
-BnxHe7xNo3kA1M-p51uYYIM0hw1SRi2pfwBKG5O8WntybLjuJ0R3X97zvqHn
2Q7xdVyKlInyNPA8gIZK0HVssXxHOI6yRrAqvdMn_sneDTWPrqVpaR_c7rt8D
dd7drf_nTD1QxESVhYqKTax5Qfd-aq8gZz8gJCzS0yyfQh6DmdhmwgrSCCRC6
BUQkeFNvjMVEYHQ9fr0NA
&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Ajwt-bearer
&client_id=a2c36919-01ff-4810-a829-400fad357351
&token=eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTQsImF1ZCI6W
yJlNzFmYjcyYS05NzRmLTQwMDEtYmNiNy1lNjdjMmJjMDAzN2YiXSwiaXNzIj
oiaHR0cHM6XC9cL2FzLXZhLmV4YW1wbGUuY29tXC8iLCJqdGkiOiIyMWIxNTk
2ZC04NWQzLTQzN2MtYWQ4My1iM2YyY2UyNDcyNDQiLCJpYXQiOjE0MTg2OTg4
MTR9.FXDtEzDLbTHzFNroW7w27RLk5m0wprFfFH7h4bdFw5fR3pwiqejKmdfA
bJvN3_yfAokBv06we5RARJUbdjmFFfRRW23cMbpGQCIk7Nq4L012X_1J4IewO
QXXMLTyWQQ_BcBMjcW3MtPrY1AoOcfBOJPx1k2jwRkYtyVTLWlff6S5gK-ciY
f3b0bAdjoQEHd_IvssIPH3xuBJkmtkrTlfWR0Q0pdpeyVePkMSI28XZvDaGnx
A4j7QI5loZYeyzGR9h70xQLVzqwwl1P0-F_0JaDFMJFO1yl4IexfpoZZsB3Hh
F2vFdL6D_lLeHRy-H2g2OzF59eMIsM_Ccs4G47862w
The client assertion parameter is structured as described in
Section 2.2
.
The server responds to an introspection request with a JSON object representing the token containing the following fields as defined in the token introspection specification:
active
Boolean value indicating whether or not this token is currently active at this authorization server. Tokens that have been revoked, have expired, or were not issued by this authorization server are considered non-active.
scope
Space-separated list of OAuth 2.0 scope values represented as a single string.
exp
Timestamp of when this token expires (integer number of seconds since from 1970-01-01T00:00:00Z UTC)
sub
An opaque string that uniquely identifies the user who authorized this token at this authorization server (if applicable)
client_id
An opaque string that uniquely identifies the OAuth 2.0 client that requested this token
The following example is a response from the introspection endpoint:
HTTP/1.1 200 OK
Date: Tue, 16 Dec 2014 03:00:14 GMT
Access-Control-Allow-Origin: *
Content-Type: application/json;charset=ISO-8859-1
Content-Language: en-US
Content-Length: 266
Connection: close

{
   "active": true,
   "scope": "conditions encounters patients medications allergies observations",
   "exp": 1418702414,
   "user_id": "{sub\u003d6WZQPpnQxV, iss\u003dhttps://idp-p.example.com/}",
   "client_id": "e71fb72a-974f-4001-bcb7-e67c2bc0037f",
   "token_type": "Bearer"
}
The authorization server MUST require authentication for both the revocation and introspection endpoints as described in
Section 2.2
. Protected resources calling the introspection endpoint MUST use credentials distinct from any other OAuth client registered at the server.
A protected resource MAY cache the response from the introspection endpoint for a period of time no greater than half the lifetime of the token. A protected resource MUST NOT accept a token that is not active according to the response from the introspection endpoint.
5.
Requests to the Protected Resource
The protected resource MUST support bearer tokens passed in the Authentication header as defined by
[RFC6750]
. Protected resources MAY support the form-parameter or query-parameter methods in
[RFC6750]
. Authorized requests MUST be made over TLS, and clients MUST validate the protected resource server's certificate. An example of an OAuth-protected call to the OpenID Connect UserInfo endpoint, sending the token in the Authorization header, follows:
GET /userinfo HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE0MTg3MDI0MTIsImF1ZCI6WyJjMWJjOD
RlNC00N2VlLTRiNjQtYmI1Mi01Y2RhNmM4MWY3ODgiXSwiaXNzIjoiaHR0cHM6XC9cL2lkcC1wLmV4YW1wbGU
uY29tXC8iLCJqdGkiOiJkM2Y3YjQ4Zi1iYzgxLTQwZWMtYTE0MC05NzRhZjc0YzRkZTMiLCJpYXQiOjE0MTg2
OTg4MTJ9.iHMz_tzZ90_b0QZS-AXtQtvclZ7M4uDAs1WxCFxpgBfBanolW37X8h1ECrUJexbXMD6rrj_uuWEq
PD738oWRo0rOnoKJAgbF1GhXPAYnN5pZRygWSD1a6RcmN85SxUig0H0e7drmdmRkPQgbl2wMhu-6h2Oqw-ize
4dKmykN9UX_2drXrooSxpRZqFVYX8PkCvCCBuFy2O-HPRov_SwtJMk5qjUWMyn2I4Nu2s-R20aCA-7T5dunr0
iWCkLQnVnaXMfA22RlRiU87nl21zappYb1_EHF9ePyq3Q353cDUY7vje8m2kKXYTgc_bUAYuW-W3SMSw5UlKa
HtSZ6PQICoA
Accept: text/plain, application/json, application/*+json, */*
Host: idp-p.example.com
Connection: Keep-Alive
User-Agent: Apache-HttpClient/4.2.3 (java 1.5)
The protected resource MUST check the audience claim, if it exists in the token, to ensure that it includes the protected resource's identifier. The protected resource MUST ensure that the rights associated with the token are sufficient to grant access to the resource. For example, this can be accomplished by querying the scopes associated with the token from the authorization server's token introspection endpoint.
6.
Scopes
Scopes define individual pieces of authority that can be requested by clients, granted by resource owners, and enforced by protected resources. Specific scope values will be highly dependent on the specific types of resources being protected in a given interface. OpenID Connect, for example, defines scope values to enable access to different attributes of user profiles.
Protected resources MUST define and document which scopes are required for access to the resource.
Authorization servers SHOULD define and document default scope values that will be used if an authorization request does not specify a requested set of scopes.
To facilitate general use across a wide variety of protected resources, authorization servers SHOULD allow for the use of arbitrary scope values at runtime, such as allowing clients or protected resources to use arbitrary scope strings upon registration. Authorization servers MAY restrict certain scopes from use by dynamically registered systems.
7.
Advanced OAuth Security Options
The preceding portions of this OAuth profile provide a level of security adequate for a wide range of use cases, while still maintaining relative ease of implementation and usability for developers, system administrators, and end users. The following are some additional security measures that can be employed for use cases where elevated risks justify the use of additional controls at the expense of implementation effort and usability. This section also addresses future security capabilities, currently in the early draft stages, being added to the OAuth standard suite.
7.1.
Client TLS Authentication
The OAuth 2.0 specification requires the use of TLS to protect several different connections among the parties involved in an OAuth transaction, but in each case only server authentication is required.  Clients could additionally be required to negotiate a mutually-authenticated TLS connection:
When connecting to the Authorization server's Token Endpoint to retrieve access and refresh tokens
When connecting to protected resources
Stronger client authentication to the Token Endpoint reduces the risk of a captured Authorization Code being used to obtain tokens.  Stronger client authentication to the protected resource, combined with validation that the authenticated client is identified in the
azp
token claim, reduces the risk of captured tokens being used by unauthorized clients. In both cases, mutual TLS authentication provides much stronger protection against man-in-the-middle attacks than server authentication alone.
Apart from the difficulty of implementing Public Key Infrastructure (PKI) solutions in distributed, cross-organization settings, one concern with this approach is the clients’ highly variable capabilities to protect private keys. Web application clients may be able to provide strong protection, but with native clients such as mobile apps, the key may be stored in a hardware security module or in plaintext in flash storage.
7.2.
Proof of Possession Tokens
OAuth proof of possession tokens are currently defined in a set of drafts under active development in the Internet Engineering Task Force (IETF) OAuth Working Group. While a bearer token can be used by anyone in possession of the token, a proof of possession token is bound to a particular symmetric or asymmetric key issued to, or already possessed by, the client. The association of the key to the token is also communicated to the protected resource; a variety of mechanisms for doing this are outlined in the draft
OAuth 2.0 Proof-of-Possession (PoP) Security Architecture
[I-D.ietf-oauth-pop-architecture]
. When the client presents the token to the protected resource, it is also required to demonstrate possession of the corresponding key (e.g., by creating a cryptographic hash or signature of the request).
Proof of Possession tokens are somewhat analogous to the Security Assertion Markup Language's (SAML's) Holder-of-Key mechanism for binding assertions to user identities. Proof of possession could prevent a number of attacks on OAuth that entail the interception of access tokens by unauthorized parties. The attacker would need to obtain the legitimate client's cryptographic key along with the access token to gain access to protected resources. Additionally, portions of the HTTP request could be protected by the same signature used in presentation of the token. Proof of possession tokens may not provide all of the same protections as PKI authentication, but they are far less challenging to implement on a distributed scale.
8.
Security Considerations
All transactions MUST be protected in transit by TLS as described in
BCP195
[BCP195]
.
All clients MUST conform to applicable recommendations found in the Security Considerations sections of
[RFC6749]
and those found in the
OAuth 2.0 Threat Model and Security Considerations document
[RFC6819]
.
9.
Normative References
[BCP195]
Sheffer, Y.
,
Holz, R.
and
P. Saint-Andre
, "
Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)
", BCP 195, RFC 7525, DOI 10.17487/RFC7525, May 2015.
[I-D.ietf-oauth-pop-architecture]
Hunt, P.
,
Richer, J.
,
Mills, W.
,
Mishra, P.
and
H. Tschofenig
, "
OAuth 2.0 Proof-of-Possession (PoP) Security Architecture
", Internet-Draft draft-ietf-oauth-pop-architecture-07, December 2015.
[OpenID.Core]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
,
de Medeiros, B.
and
C. Mortimore
, "
OpenID Connect Core 1.0
", August 2015.
[OpenID.Discovery]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
and
E. Jay
, "
OpenID Connect Discovery 1.0
", August 2015.
[RFC2119]
Bradner, S.
, "
Key words for use in RFCs to Indicate Requirement Levels
", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.
[RFC2246]
Dierks, T.
and
C. Allen
, "
The TLS Protocol Version 1.0
", RFC 2246, DOI 10.17487/RFC2246, January 1999.
[RFC3986]
Berners-Lee, T.
,
Fielding, R.
and
L. Masinter
, "
Uniform Resource Identifier (URI): Generic Syntax
", STD 66, RFC 3986, DOI 10.17487/RFC3986, January 2005.
[RFC5246]
Dierks, T.
and
E. Rescorla
, "
The Transport Layer Security (TLS) Protocol Version 1.2
", RFC 5246, DOI 10.17487/RFC5246, August 2008.
[RFC5322]
Resnick, P.
, "
Internet Message Format
", RFC 5322, DOI 10.17487/RFC5322, October 2008.
[RFC5646]
Phillips, A.
and
M. Davis
, "
Tags for Identifying Languages
", BCP 47, RFC 5646, DOI 10.17487/RFC5646, September 2009.
[RFC5785]
Nottingham, M.
and
E. Hammer-Lahav
, "
Defining Well-Known Uniform Resource Identifiers (URIs)
", RFC 5785, DOI 10.17487/RFC5785, April 2010.
[RFC6125]
Saint-Andre, P.
and
J. Hodges
, "
Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)
", RFC 6125, DOI 10.17487/RFC6125, March 2011.
[RFC6749]
Hardt, D.
, "
The OAuth 2.0 Authorization Framework
", RFC 6749, DOI 10.17487/RFC6749, October 2012.
[RFC6750]
Jones, M.
and
D. Hardt
, "
The OAuth 2.0 Authorization Framework: Bearer Token Usage
", RFC 6750, DOI 10.17487/RFC6750, October 2012.
[RFC6819]
Lodderstedt, T.
,
McGloin, M.
and
P. Hunt
, "
OAuth 2.0 Threat Model and Security Considerations
", RFC 6819, DOI 10.17487/RFC6819, January 2013.
[RFC7009]
Lodderstedt, T.
,
Dronia, S.
and
M. Scurtescu
, "
OAuth 2.0 Token Revocation
", RFC 7009, DOI 10.17487/RFC7009, August 2013.
[RFC7033]
Jones, P.
,
Salgueiro, G.
,
Jones, M.
and
J. Smarr
, "
WebFinger
", RFC 7033, DOI 10.17487/RFC7033, September 2013.
[RFC7159]
Bray, T.
, "
The JavaScript Object Notation (JSON) Data Interchange Format
", RFC 7159, DOI 10.17487/RFC7159, March 2014.
[RFC7515]
Jones, M.
,
Bradley, J.
and
N. Sakimura
, "
JSON Web Signature (JWS)
", RFC 7515, DOI 10.17487/RFC7515, May 2015.
[RFC7516]
Jones, M.
and
J. Hildebrand
, "
JSON Web Encryption (JWE)
", RFC 7516, DOI 10.17487/RFC7516, May 2015.
[RFC7517]
Jones, M.
, "
JSON Web Key (JWK)
", RFC 7517, DOI 10.17487/RFC7517, May 2015.
[RFC7518]
Jones, M.
, "
JSON Web Algorithms (JWA)
", RFC 7518, DOI 10.17487/RFC7518, May 2015.
[RFC7519]
Jones, M.
,
Bradley, J.
and
N. Sakimura
, "
JSON Web Token (JWT)
", RFC 7519, DOI 10.17487/RFC7519, May 2015.
[RFC7523]
Jones, M.
,
Campbell, B.
and
C. Mortimore
, "
JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants
", RFC 7523, DOI 10.17487/RFC7523, May 2015.
[RFC7591]
Richer, J.
,
Jones, M.
,
Bradley, J.
,
Machulak, M.
and
P. Hunt
, "
OAuth 2.0 Dynamic Client Registration Protocol
", RFC 7591, DOI 10.17487/RFC7591, July 2015.
[RFC7662]
Richer, J.
, "
OAuth 2.0 Token Introspection
", RFC 7662, DOI 10.17487/RFC7662, October 2015.
Appendix A.
Acknowledgements
The OpenID Community would like to thank the following people for their contributions to this specification: Mark Russel, Mary Pulvermacher, David Hill, Dale Moberg, Adrian Gropper, Eve Maler, Danny van Leeuwen, John Moehrke, Aaron Seib, John Bradley, Debbie Bucci, Josh Mandel, and Sarah Squire.
The original version of this specification was part of the Secure RESTful Interfaces project from The MITRE Corporation, available online at http://secure-restful-interface-profile.github.io/pages/
Appendix B.
Notices
Copyright (c) 2015 The OpenID Foundation.
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
Appendix C.
Document History
-2016-02-15
Implementer's Draft 1
-2015-11-30
Clarified client instances.
Replaced "mitre.org" with "example.com" (JWTs need to be regenerated).
Fixed specification references to new RFCs.
Clarified scope flexibility.
Clarified dynamic registration requirement.
Added some UX requirements and guidance.
Added security considerations section and TLS BCP reference.
-2015-04-24
Fixed references to make it compile
-2015-04-01
Imported content from Secure RESTful OAuth profile.
Author's Address
Justin Richer
(editor)
Richer
EMail:
openid@justin.richer.org
URI:
http://justin.richer.org/