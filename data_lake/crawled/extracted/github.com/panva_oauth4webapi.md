---
{
  "title": "GitHub - panva/oauth4webapi: Low-Level OAuth 2 / OpenID Connect Client API for JavaScript Runtimes · GitHub",
  "url": "https://github.com/panva/oauth4webapi",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5511,
  "crawled_at": "2026-04-23T20:48:59"
}
---

panva
/
oauth4webapi
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
69
Star
747
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
1,207 Commits
1,207 Commits
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
mod.ts
mod.ts
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
typedoc.json
typedoc.json
View all files
Repository files navigation
oauth4webapi
Low-Level OAuth 2 / OpenID Connect Client API for JavaScript Runtimes
This software provides a collection of routines that can be used to build client modules for OAuth 2.1, OAuth 2.0 with the latest Security Best Current Practices (BCP), and FAPI 2.0, as well as OpenID Connect where applicable. The primary goal of this software is to promote secure and up-to-date best practices while using only the capabilities common to both browser and non-browser JavaScript runtimes.
Features
The following features are currently in scope and implemented in this software:
Authorization Server Metadata discovery
Resource Server Metadata discovery
Authorization Code Flow (profiled under OpenID Connect 1.0, OAuth 2.0, OAuth 2.1, and FAPI 2.0), with PKCE
Refresh Token, Device Authorization, Client-Initiated Backchannel Authentication (CIBA), and Client Credentials Grants
Demonstrating Proof-of-Possession at the Application Layer (DPoP)
Token Introspection and Revocation
Pushed Authorization Requests (PAR)
UserInfo and Protected Resource Requests
Authorization Server Issuer Identification
JWT Secured Introspection, Response Mode (JARM), Authorization Request (JAR), and UserInfo
Dynamic Client Registration (DCR)
Validating incoming JWT Access Tokens
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
Dependencies: 0
oauth4webapi
has no dependencies and it exports tree-shakeable ESM.
API Reference
oauth4webapi
is distributed via
npmjs.com
,
jsr.io
,
jsdelivr.com
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
oauth
from
'oauth4webapi'
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
Client Authentication
Client Secret in HTTP Authorization Header -
source
Client Secret in HTTP Body -
source
|
diff
Private Key JWT Client Authentication -
source
|
diff
Public Client -
source
|
diff
Other Grants
Client Credentials Grant -
source
Client-Initiated Backchannel Authentication Grant (CIBA) -
source
Device Authorization Grant -
source
Refresh Token Grant -
source
|
diff
FAPI
FAPI 1.0 Advanced -
source
|
diff
FAPI 2.0 Security Profile -
source
|
diff
FAPI 2.0 Message Signing -
source
|
diff
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
v3.x
Security Policy
✅
✅
Footnotes
CJS style
let oauth = require('oauth4webapi')
is possible in Node.js versions where the
require(esm)
feature is enabled by default (^20.19.0 || ^22.12.0 || >= 23.0.0).
↩
Node.js v20.x as baseline is required
↩
About
Low-Level OAuth 2 / OpenID Connect Client API for JavaScript Runtimes
Topics
electron
nodejs
javascript
oauth2
node
browser
authentication
nextjs
authorization
openid
openid-connect
oidc
bun
deno
cloudflare-workers
vercel-edge
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
747
stars
Watchers
7
watching
Forks
69
forks
Report repository
Releases
86
v3.8.5
Latest
Feb 16, 2026
+ 85 releases
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
96.7%
JavaScript
2.2%
Shell
1.1%