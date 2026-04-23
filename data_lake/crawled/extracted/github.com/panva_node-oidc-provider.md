---
{
  "title": "GitHub - panva/node-oidc-provider: OpenID Certified™ OAuth 2.0 Authorization Server implementation for Node.js · GitHub",
  "url": "https://github.com/panva/node-oidc-provider",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6510,
  "crawled_at": "2026-04-23T20:56:09"
}
---

panva
/
node-oidc-provider
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
782
Star
3.7k
main
Branches
Tags
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
2,794 Commits
2,794 Commits
.github
.github
certification
certification
docs
docs
example
example
lib
lib
sponsor
sponsor
test
test
.editorconfig
.editorconfig
.eslintrc
.eslintrc
.gitignore
.gitignore
.release-notes.cjs
.release-notes.cjs
.versionrc.json
.versionrc.json
CHANGELOG.md
CHANGELOG.md
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTING.md
LICENSE.md
LICENSE.md
OpenID_Certified.png
OpenID_Certified.png
Procfile
Procfile
README.md
README.md
SECURITY.md
SECURITY.md
package-lock.json
package-lock.json
package.json
package.json
View all files
Repository files navigation
oidc-provider
This module provides an OAuth 2.0 (
RFC 6749
) Authorization Server with support for OpenID Connect (
OIDC
) and many
other additional features and standards.
Table of Contents
Implemented specs & features
Certification
Documentation & Configuration
Community Guides
Events
Implemented specs & features
The following specifications are implemented by oidc-provider (not exhaustive):
Note that not all features are enabled by default, check the configuration section on how to enable them.
RFC6749
- OAuth 2.0
&
OIDC
Core 1.0
OIDC
Discovery 1.0
&
RFC8414
Authorization Server Metadata
Dynamic Client Registration
OIDC
Dynamic Client Registration 1.0
RFC7591
- OAuth 2.0 Dynamic Client Registration Protocol
RFC7592
- OAuth 2.0 Dynamic Client Registration Management Protocol
OIDC
RP-Initiated Logout 1.0
OIDC
Back-Channel Logout 1.0
RFC7009
- OAuth 2.0 Token Revocation
RFC7636
- Proof Key for Code Exchange (
PKCE
)
RFC7662
- OAuth 2.0 Token Introspection
RFC8252
- OAuth 2.0 for Native Apps BCP (
AppAuth
)
RFC8628
- OAuth 2.0 Device Authorization Grant (
Device Flow
)
RFC8705
- OAuth 2.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens (
MTLS
)
RFC8707
- OAuth 2.0 Resource Indicators
RFC9101
- OAuth 2.0 JWT-Secured Authorization Request (
JAR
)
RFC9126
- OAuth 2.0 Pushed Authorization Requests (
PAR
)
RFC9207
- OAuth 2.0 Authorization Server Issuer Identifier in Authorization Response
RFC9449
- OAuth 2.0 Demonstration of Proof-of-Possession at the Application Layer (
DPoP
)
RFC9701
- JWT Response for OAuth Token Introspection
FAPI 1.0 Security Profile - Part 2: Advanced (
FAPI 1.0
)
FAPI 2.0 Security Profile (
FAPI 2.0
)
FAPI 2.0 Message Signing (
FAPI 2.0
)
JWT Secured Authorization Response Mode for OAuth 2.0 (
JARM
)
OIDC Client Initiated Backchannel Authentication Flow (
CIBA
)
OIDC Relying Party Metadata Choices 1.0
Supported Access Token formats:
Opaque
JSON Web Token (JWT) Profile for OAuth 2.0 Access Tokens
The following specifications and drafts are implemented as experimental features:
Financial-grade API: Client Initiated Backchannel Authentication Profile (
FAPI-CIBA
) - Implementers Draft 01
OAuth 2.0 Attestation-Based Client Authentication - Draft 06
OAuth Client ID Metadata Document (
CIMD
) - Draft 01
Updates to experimental feature specification versions are released as MINOR library versions,
if you utilize these features consider using the tilde
~
operator in your
package.json since breaking changes may be introduced as part of these version updates. Alternatively
acknowledge
the version and be notified of breaking changes as part of
your CI.
Certification
Filip Skokan has
certified
that
oidc-provider
conforms to the following profiles of the OpenID Connect™ protocol.
Basic, Implicit, Hybrid, Config, Form Post, and 3rd Party-Init
Back-Channel Logout and RP-Initiated Logout
FAPI 1.0
FAPI CIBA
FAPI 2.0
Sponsor
If you want to quickly add OpenID Connect authentication to Node.js apps, feel free to check out Auth0's Node.js SDK and free plan.
Create an Auth0 account; it's free!
Support
If you or your company use this module, or you need help using/upgrading the module, please consider becoming a
sponsor
so I can continue maintaining it and adding new features carefree. The only way to guarantee you get feedback from the author & sole maintainer of this module is to support the package through GitHub Sponsors.
Documentation
& Configuration
oidc-provider can be mounted to existing connect, express, fastify, hapi, or koa applications, see
how
. The authorization server allows to be extended and configured in
various ways to fit a variety of uses. See the
documentation
and
example folder
.
import
*
as
oidc
from
"oidc-provider"
;
const
provider
=
new
oidc
.
Provider
(
"http://localhost:3000"
,
{
// refer to the documentation for other available configuration
clients
:
[
{
client_id
:
"foo"
,
client_secret
:
"bar"
,
redirect_uris
:
[
"http://localhost:8080/cb"
]
,
// ... other client properties
}
,
]
,
}
)
;
const
server
=
provider
.
listen
(
3000
,
(
)
=>
{
console
.
log
(
"oidc-provider listening on port 3000, check http://localhost:3000/.well-known/openid-configuration"
,
)
;
}
)
;
External type definitions are available via
DefinitelyTyped
.
Community Guides
Collection of Community-maintained configuration use cases are in the
Community Guides Discussions section
Events
oidc-provider instances are event emitters, using event handlers you can hook into the various
actions and i.e. emit metrics that react to specific triggers. See the list of available emitted
event names
and their description.
Supported Versions
Version
Security Fixes 🔑
Other Bug Fixes 🐞
New Features ⭐
v9.x
Security Policy
✅
✅
v8.x
Security Policy
❌
❌
About
OpenID Certified™ OAuth 2.0 Authorization Server implementation for Node.js
Topics
oauth2
server
provider
authorization
connect
openid
openid-connect
openid-provider
oidc
authorization-server
Resources
Readme
License
MIT license
Code of conduct
Code of conduct
Contributing
Contributing
Security policy
Security policy
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
3.7k
stars
Watchers
66
watching
Forks
782
forks
Report repository
Releases
264
v9.8.2
Latest
Apr 17, 2026
+ 263 releases
Sponsor this project
Sponsor
Uh oh!
There was an error while loading.
Please reload this page
.
Learn more about GitHub Sponsors
Uh oh!
There was an error while loading.
Please reload this page
.
Contributors
Uh oh!
There was an error while loading.
Please reload this page
.
Languages
JavaScript
99.5%
Other
0.5%