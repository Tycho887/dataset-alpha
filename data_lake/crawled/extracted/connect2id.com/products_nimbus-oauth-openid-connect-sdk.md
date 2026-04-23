---
{
  "title": "\n    \n    \n    \n        \n            \n                Nimbus OAuth 2.0 SDK with OpenID Connect extensions · Docs · Connect2id\n            \n        \n    \n",
  "url": "https://connect2id.com/products/nimbus-oauth-openid-connect-sdk",
  "domain": "connect2id.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5187,
  "crawled_at": "2026-04-23T20:52:08"
}
---

Nimbus OAuth 2.0 SDK with OpenID Connect extensions
Comprehensive Java library for developing OAuth 2.0 and OpenID Connect
clients and servers
Standards compliant, robust and extensible
Open source (Apache 2.0 licence)
This library is your starting point for developing
OAuth 2.0
/
2.1
and
OpenID Connect
applications in Java. It provides ready and simple to use classes for dealing
with tokens and representing the protocol messages, ensuring standards
compliance and thus interoperability.
The OAuth 2.0 and OpenID Connect standards permit application-specific profiles
and extensions, and this library also caters for that, with suitable interfaces
and base classes where required.
OAuth 2.0
Supported endpoints:
Authorisation Server Metadata
Pushed Authorisation Request (PAR) endpoint
Authorisation Endpoint
Token Endpoint
Token Introspection Endpoint
Token Revocation Endpoint
Client Registration and Management Endpoint
Client-Initiated Back-channel Authentication (CIBA) Endpoint
Client Notification Endpoint (for CIBA)
Request Object Endpoint (obsoleted by PAR)
Resource protected with an OAuth 2.0 access token
OpenID Connect
Supported endpoints:
OpenID Provider Metadata
Authorisation Endpoint for OpenID Authentication requests
Token Endpoint
UserInfo Endpoint
End-Session (Logout) Endpoint
Back-Channel Logout Endpoint
Federation Entity Configuration Endpoint
Federation API Endpoint
Additional features
Process plain, signed and encrypted JSON Web Tokens (JWTs) with help of the
Nimbus JOSE + JWT
library.
Full OpenID Connect UserInfo i10n and l10n support with help of the
Nimbus Language Tags
library.
Specifications
Implemented standards and drafts:
The OAuth 2.0 Authorization Framework (RFC 6749)
The OAuth 2.1 Authorization Framework (draft-ietf-oauth-v2-1-09)
The OAuth 2.0 Authorization Framework: Bearer Token Usage (RFC 6750)
OAuth 2.0 Token Introspection (RFC 7662)
OAuth 2.0 Token Revocation (RFC 7009)
OAuth 2.0 Authorization Server Metadata (RFC 8414)
OAuth 2.0 Dynamic Client Registration Protocol (RFC 7591)
OAuth 2.0 Dynamic Client Registration Management Protocol (RFC 7592)
Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants (RFC 7521)
JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants (RFC 7523)
SAML 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants (RFC 7522)
Proof Key for Code Exchange by OAuth Public Clients (RFC 7636)
Authentication Method Reference Values (RFC 8176)
OAuth 2.0 Authorization Server Metadata (RFC 8414)
OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens (RFC 8705)
OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP) (RFC 9449)
Resource Indicators for OAuth 2.0 (RFC 8707)
OAuth 2.0 Device Authorization Grant (RFC 8628)
OAuth 2.0 Token Exchange (RFC 8693)
OAuth 2.0 Incremental Authorization (draft-ietf-oauth-incremental-authz-04)
The OAuth 2.0 Authorization Framework: JWT Secured Authorization Request (JAR) (RFC 9101)
OAuth 2.0 Pushed Authorization Requests (RFC 9126)
OAuth 2.0 Authorization Server Issuer Identification (RFC 9207)
OAuth 2.0 Rich Authorization Requests (RFC 9396)
OAuth 2.0 Step Up Authentication Challenge Protocol (RFC 9470)
OpenID Connect Core 1.0 (2014-02-25)
OpenID Connect Core Unmet Authentication Requirements 1.0 (2019-05-08)
OpenID Connect Discovery 1.0 (2014-02-25)
OpenID Connect Dynamic Registration 1.0 (2014-02-25)
OpenID Connect Session Management 1.0 (2022-09-12)
OpenID Connect RP-Initiated Logout 1.0 (2022-09-12)
OpenID Connect Front-Channel Logout 1.0 (2022-09-12)
OpenID Connect Back-Channel Logout 1.0 (2022-09-12)
OpenID Connect Extended Authentication Profile (EAP) ACR Values 1.0 - draft 01
OpenID Connect for Identity Assurance 1.0 - draft 12
OpenID Connect Native SSO for Mobile Apps - draft 06
OpenID Federation 1.0 - draft 25
Initiating User Registration via OpenID Connect 1.0
OAuth 2.0 Multiple Response Type Encoding Practices 1.0 (2014-02-25)
Financial Services – Financial API - Part 1: Read Only API Security Profile (2021-03-12)
Financial Services – Financial API - Part 2: Read and Write API Security Profile (2021-03-12)
Financial-grade API: JWT Secured Authorization Response Mode for OAuth 2.0 (JARM) (2018-10-17)
OpenID Connect Client Initiated Backchannel Authentication (CIBA) Flow - Core 1.0
JavaDocs
The SDK code comes with excellent JavaDocs. These are available from Maven
Central just as the code JARs are. You can also browse them
online
.
Licensing
This library is free and made available under the terms of the open source
Apache 2.0 license
.
Acknowledgements
Julian Krautwald, Vladislav Mladenov and
Christian Mainka
,
security researchers at
Horst Görtz Institute for IT-Security
/
Chair for Network and Data Security
.
Tim McClean
for his security audit of the Java
library for
AES SIV-mode encryption
,
created and maintained by
Crytomator
.
Emond Papegaaij and Topicus KeyHub for the Device Code grant implementation.
Wei Huang for the Token Exchange (RFC 8693) implementation.
The members of the OpenID Connect and OAuth working groups.
Other contributors of bug reports, fixes, patches and suggestions.