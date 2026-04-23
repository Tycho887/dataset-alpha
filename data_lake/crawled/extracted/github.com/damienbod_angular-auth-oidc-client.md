---
{
  "title": "GitHub - damienbod/angular-auth-oidc-client: npm package for OpenID Connect, OAuth Code Flow with PKCE, Refresh tokens, Implicit Flow · GitHub",
  "url": "https://github.com/damienbod/angular-auth-oidc-client",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6035,
  "crawled_at": "2026-04-23T20:55:53"
}
---

damienbod
/
angular-auth-oidc-client
Public
Notifications
You must be signed in to change notification settings
Fork
451
Star
1.2k
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
4,327 Commits
4,327 Commits
.github
.github
.vscode
.vscode
certs
certs
docs/
site/
angular-auth-oidc-client
docs/
site/
angular-auth-oidc-client
projects
projects
tools
tools
.editorconfig
.editorconfig
.eslintrc.json
.eslintrc.json
.gitignore
.gitignore
.prettierignore
.prettierignore
.prettierrc
.prettierrc
CHANGELOG.md
CHANGELOG.md
LICENSE
LICENSE
README.md
README.md
SECURITY.md
SECURITY.md
angular.json
angular.json
lefthook.yml
lefthook.yml
license-banner.txt
license-banner.txt
package-lock.json
package-lock.json
package.json
package.json
tsconfig.json
tsconfig.json
View all files
Repository files navigation
Angular Lib for OpenID Connect & OAuth2
Secure your Angular app using the latest standards for OpenID Connect & OAuth2. Provides support for token refresh, all modern OIDC Identity Providers and more.
Acknowledgements
This library is
certified
by OpenID Foundation. (RP Implicit and Config RP)
Features
Code samples
for most of the common use cases
Supports schematics via
ng add
support
Supports all modern OIDC identity providers
Supports OpenID Connect Code Flow with PKCE
Supports Code Flow PKCE with Refresh tokens
Supports OpenID Connect Implicit Flow
Supports OpenID Connect Session Management 1.0
Supports RFC7009 - OAuth 2.0 Token Revocation
Supports RFC7636 - Proof Key for Code Exchange (PKCE)
Supports OAuth 2.0 Pushed authorisation requests (PAR) draft
Semantic releases
Github actions
Modern coding guidelines with prettier, husky
Up to date documentation
Implements OIDC validation as specified, complete client side validation for REQUIRED features
Supports authentication using redirect or popup
Installation
Ng Add
You can use the schematics and
ng add
the library.
ng add angular-auth-oidc-client
And answer the questions. A module will be created which encapsulates your configuration.
Npm / Yarn
Navigate to the level of your
package.json
and type
npm install angular-auth-oidc-client
or with yarn
yarn add angular-auth-oidc-client
Documentation
Read the docs here
Samples
Explore the Samples here
Quickstart
For the example of the Code Flow. For further examples please check the
Samples
Section.
If you have done the installation with the schematics, these modules and files should be available already!
Configuration
Import the
AuthModule
in your module.
import
{
NgModule
}
from
'@angular/core'
;
import
{
AuthModule
,
LogLevel
}
from
'angular-auth-oidc-client'
;
// ...
@
NgModule
(
{
// ...
imports
:
[
// ...
AuthModule
.
forRoot
(
{
config
:
{
authority
:
'<your authority address here>'
,
redirectUrl
:
window
.
location
.
origin
,
postLogoutRedirectUri
:
window
.
location
.
origin
,
clientId
:
'<your clientId>'
,
scope
:
'openid profile email offline_access'
,
responseType
:
'code'
,
silentRenew
:
true
,
useRefreshToken
:
true
,
logLevel
:
LogLevel
.
Debug
,
}
,
}
)
,
]
,
// ...
}
)
export
class
AppModule
{
}
And call the method
checkAuth()
from your
app.component.ts
. The method
checkAuth()
is needed to process the redirect from your Security Token Service and set the correct states. This method must be used to ensure the correct functioning of the library.
import
{
Component
,
OnInit
,
inject
}
from
'@angular/core'
;
import
{
OidcSecurityService
}
from
'angular-auth-oidc-client'
;
@
Component
(
{
/*...*/
}
)
export
class
AppComponent
implements
OnInit
{
private
readonly
oidcSecurityService
=
inject
(
OidcSecurityService
)
;
ngOnInit
(
)
{
this
.
oidcSecurityService
.
checkAuth
(
)
.
subscribe
(
(
loginResponse
:
LoginResponse
)
=>
{
const
{
isAuthenticated
,
userData
,
accessToken
,
idToken
,
configId
}
=
loginResponse
;
/*...*/
}
)
;
}
login
(
)
{
this
.
oidcSecurityService
.
authorize
(
)
;
}
logout
(
)
{
this
.
oidcSecurityService
.
logoff
(
)
.
subscribe
(
(
result
)
=>
console
.
log
(
result
)
)
;
}
}
Using the access token
You can get the access token by calling the method
getAccessToken()
on the
OidcSecurityService
const
token
=
this
.
oidcSecurityService
.
getAccessToken
(
)
.
subscribe
(
...
)
;
And then you can use it in the HttpHeaders
import
{
HttpHeaders
}
from
'@angular/common/http'
;
const
token
=
this
.
oidcSecurityServices
.
getAccessToken
(
)
.
subscribe
(
(
token
)
=>
{
const
httpOptions
=
{
headers
:
new
HttpHeaders
(
{
Authorization
:
'Bearer '
+
token
,
}
)
,
}
;
}
)
;
You can use the built in interceptor to add the accesstokens to your request
AuthModule
.
forRoot
(
{
config
:
{
// ...
secureRoutes
:
[
'https://my-secure-url.com/'
,
'https://my-second-secure-url.com/'
]
,
}
,
}
)
,
providers
:
[
{
provide
:
HTTP_INTERCEPTORS
,
useClass
:
AuthInterceptor
,
multi
:
true
}
,
]
,
Versions
Current Version is Version 21.x
Info about Version 20
Info about Version 19
Info about Version 18
Info about Version 17
Info about Version 16
Info about Version 15
Info about Version 14
Info about Version 13
Info about Version 12
Info about Version 11
Info about Version 10
License
MIT
Authors
@DamienBod
@FabianGosebrink
About
npm package for OpenID Connect, OAuth Code Flow with PKCE, Refresh tokens, Implicit Flow
www.npmjs.com/package/angular-auth-oidc-client
Topics
npm
security
identity
oauth2
angular
authentication
openidconnect
auth
openid
oidc
authn
implicit-flow
Resources
Readme
License
MIT, Unknown licenses found
Licenses found
MIT
LICENSE
Unknown
license-banner.txt
Security policy
Security policy
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
1.2k
stars
Watchers
35
watching
Forks
451
forks
Report repository
Releases
140
21.0.1
Latest
Dec 11, 2025
+ 139 releases
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
Used by
2.3k
+ 2,278
Contributors
Uh oh!
There was an error while loading.
Please reload this page
.
Languages
TypeScript
87.1%
JavaScript
9.8%
HTML
2.6%
Other
0.5%