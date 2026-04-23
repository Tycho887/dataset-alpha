---
{
  "title": "GitHub - panva/openid-client: OAuth 2 / OpenID Connect Client API for JavaScript Runtimes · GitHub",
  "url": "https://github.com/panva/openid-client",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 10029,
  "crawled_at": "2026-04-23T20:51:07"
}
---

panva
/
openid-client
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
410
Star
2.3k
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
1,188 Commits
1,188 Commits
.github
.github
conformance
conformance
docs
docs
examples
examples
patches
patches
sponsor
sponsor
src
src
tap
tap
test
test
.electron_flags.sh
.electron_flags.sh
.gitignore
.gitignore
.node_flags.sh
.node_flags.sh
.postbump.cjs
.postbump.cjs
.prettierrc.json
.prettierrc.json
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
README.md
README.md
SECURITY.md
SECURITY.md
ava.config.mjs
ava.config.mjs
check-examples.sh
check-examples.sh
jsr.json
jsr.json
package-lock.json
package-lock.json
package.json
package.json
playwright.config.ts
playwright.config.ts
tsconfig.docs.json
tsconfig.docs.json
tsconfig.json
tsconfig.json
tsconfig.passport.json
tsconfig.passport.json
typedoc.json
typedoc.json
View all files
Repository files navigation
openid-client
OAuth 2 / OpenID Connect Client API for JavaScript Runtimes
openid-client simplifies integration with authorization servers by providing easy-to-use APIs for the most common authentication and authorization flows, including OAuth 2 and OpenID Connect. It is designed for JavaScript runtimes like Node.js, Browsers, Deno, Cloudflare Workers, and more.
Features
The following features are currently in scope and implemented in this software:
Authorization Server Metadata discovery
Authorization Code Flow (profiled under OpenID Connect 1.0, OAuth 2.0, OAuth 2.1, FAPI 1.0 Advanced, and FAPI 2.0)
Refresh Token, Device Authorization, Client-Initiated Backchannel Authentication (CIBA), and Client Credentials Grants
Demonstrating Proof-of-Possession at the Application Layer (DPoP)
Token Introspection and Revocation
Pushed Authorization Requests (PAR)
UserInfo and Protected Resource Requests
Authorization Server Issuer Identification
JWT Secured Introspection, Response Mode (JARM), Authorization Request (JAR), and UserInfo
Dynamic Client Registration (DCR)
Passport
Strategy
Sponsor
If you want to quickly add authentication to JavaScript apps, feel free to check out Auth0's JavaScript SDK and free plan.
Create an Auth0 account; it's free!
Certification
Filip Skokan
has
certified
that
this software
conforms to the Basic, FAPI 1.0, and FAPI 2.0 Relying Party Conformance Profiles of the OpenID Connect™ protocol.
💗 Help the project
Support from the community to continue maintaining and improving this module is welcome. If you find the module useful, please consider supporting the project by
becoming a sponsor
.
API Reference Documentation
openid-client
is distributed via
npmjs.com
,
jsr.io
, and
github.com
.
Examples
example
ESM import
1
import
*
as
client
from
'openid-client'
Authorization Code Flow (OAuth 2.0) -
source
Authorization Code Flow (OpenID Connect) -
source
|
diff
Extensions
DPoP -
source
|
diff
JWT Secured Authorization Request (JAR) -
source
|
diff
JWT Secured Authorization Response Mode (JARM) -
source
|
diff
Pushed Authorization Request (PAR) -
source
|
diff
Passport Strategy -
source
Quick start
let
server
!
:
URL
// Authorization Server's Issuer Identifier
let
clientId
!
:
string
// Client identifier at the Authorization Server
let
clientSecret
!
:
string
// Client Secret
let
config
:
client
.
Configuration
=
await
client
.
discovery
(
server
,
clientId
,
clientSecret
,
)
Authorization Code Flow
Authorization Code flow is for obtaining Access Tokens (and optionally Refresh Tokens) to use with
third party APIs.
When you want to have your end-users authorize or authenticate you need to send them to the authorization server's
authorization_endpoint
. Consult the web framework of your choice on how to redirect but here's how
to get the authorization endpoint's URL with parameters already encoded in the query to redirect
to.
/**
* Value used in the authorization request as the redirect_uri parameter, this
* is typically pre-registered at the Authorization Server.
*/
let
redirect_uri
!
:
string
let
scope
!
:
string
// Scope of the access request
/**
* PKCE: The following MUST be generated for every redirect to the
* authorization_endpoint. You must store the code_verifier and state in the
* end-user session such that it can be recovered as the user gets redirected
* from the authorization server back to your application.
*/
let
code_verifier
:
string
=
client
.
randomPKCECodeVerifier
(
)
let
code_challenge
:
string
=
await
client
.
calculatePKCECodeChallenge
(
code_verifier
)
let
state
!
:
string
let
parameters
:
Record
<
string
,
string
>
=
{
redirect_uri
,
scope
,
code_challenge
,
code_challenge_method
:
'S256'
,
}
if
(
!
config
.
serverMetadata
(
)
.
supportsPKCE
(
)
)
{
/**
* We cannot be sure the server supports PKCE so we're going to use state too.
* Use of PKCE is backwards compatible even if the AS doesn't support it which
* is why we're using it regardless. Like PKCE, random state must be generated
* for every redirect to the authorization_endpoint.
*/
state
=
client
.
randomState
(
)
parameters
.
state
=
state
}
let
redirectTo
:
URL
=
client
.
buildAuthorizationUrl
(
config
,
parameters
)
// now redirect the user to redirectTo.href
console
.
log
(
'redirecting to'
,
redirectTo
.
href
)
When end-users are redirected back to the
redirect_uri
your application consumes the callback and
passes in PKCE
code_verifier
to include it in the authorization code grant token exchange.
let
getCurrentUrl
!
:
(
...
args
:
any
)
=>
URL
let
tokens
:
client
.
TokenEndpointResponse
=
await
client
.
authorizationCodeGrant
(
config
,
getCurrentUrl
(
)
,
{
pkceCodeVerifier
:
code_verifier
,
expectedState
:
state
,
}
,
)
console
.
log
(
'Token Endpoint Response'
,
tokens
)
You can then fetch a protected resource response
let
protectedResourceResponse
:
Response
=
await
client
.
fetchProtectedResource
(
config
,
tokens
.
access_token
,
new
URL
(
'https://rs.example.com/api'
)
,
'GET'
,
)
console
.
log
(
'Protected Resource Response'
,
await
protectedResourceResponse
.
json
(
)
,
)
Device Authorization Grant (Device Flow)
let
scope
!
:
string
// Scope of the access request
let
response
=
await
client
.
initiateDeviceAuthorization
(
config
,
{
scope
}
)
console
.
log
(
'User Code:'
,
response
.
user_code
)
console
.
log
(
'Verification URI:'
,
response
.
verification_uri
)
console
.
log
(
'Verification URI (complete):'
,
response
.
verification_uri_complete
)
You will display the instructions to the end-user and have them directed at
verification_uri
or
verification_uri_complete
, afterwards you can start polling for the Device Access Token Response.
let
tokens
:
client
.
TokenEndpointResponse
=
await
client
.
pollDeviceAuthorizationGrant
(
config
,
response
)
console
.
log
(
'Token Endpoint Response'
,
tokens
)
This will poll in a regular interval and only resolve with tokens once the end-user authenticates.
Client-Initiated Backchannel Authentication (CIBA)
let
scope
!
:
string
// Scope of the access request
/**
* One of login_hint, id_token_hint, or login_hint_token parameters must be
* provided in CIBA
*/
let
login_hint
!
:
string
let
response
=
await
client
.
initiateBackchannelAuthentication
(
config
,
{
scope
,
login_hint
,
}
)
/**
* OPTIONAL: If your client is configured with Ping Mode you'd invoke the
* following after getting the CIBA Ping Callback (its implementation is
* framework specific and therefore out of scope for openid-client)
*/
let
tokens
:
client
.
TokenEndpointResponse
=
await
client
.
pollBackchannelAuthenticationGrant
(
config
,
response
)
console
.
log
(
'Token Endpoint Response'
,
tokens
)
This will poll in a regular interval and only resolve with tokens once the end-user authenticates.
Client Credentials Grant
Client Credentials flow is for obtaining Access Tokens to use with third party APIs on behalf of your application, rather than an end-user which was the case in previous examples.
let
scope
!
:
string
// Scope of the access request
let
resource
!
:
string
// Resource Indicator of the Resource Server the access token is for
let
tokens
:
client
.
TokenEndpointResponse
=
await
lib
.
clientCredentialsGrant
(
config
,
{
scope
,
resource
}
,
)
console
.
log
(
'Token Endpoint Response'
,
tokens
)
Supported Runtimes
The supported JavaScript runtimes include those that support the utilized Web API globals and standard built-in objects. These are
(but are not limited to)
:
Browsers
Bun
Cloudflare Workers
Deno
Electron
Node.js
2
Supported Versions
Version
Security Fixes 🔑
Other Bug Fixes 🐞
New Features ⭐
Runtime and Module type
v6.x
Security Policy
✅
✅
Universal
3
ESM
1
v5.x
Security Policy
❌
❌
Node.js CJS + ESM
Footnotes
CJS style
let client = require('openid-client')
is possible in Node.js versions where the
require(esm)
feature is enabled by default (^20.19.0 || ^22.12.0 || >= 23.0.0).
↩
↩
2
Node.js v20.x as baseline is required
↩
Assumes runtime support of
WebCryptoAPI
and
Fetch API
↩
About
OAuth 2 / OpenID Connect Client API for JavaScript Runtimes
Topics
client
passport
connect
openid
openid-connect
oidc
openid-client
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
2.3k
stars
Watchers
32
watching
Forks
410
forks
Report repository
Releases
162
v6.8.3
Latest
Apr 13, 2026
+ 161 releases
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
TypeScript
94.1%
JavaScript
4.0%
Shell
1.9%