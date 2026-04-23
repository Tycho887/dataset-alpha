---
{
  "title": "GitHub - coreos/go-oidc: A Go OpenID Connect client. · GitHub",
  "url": "https://github.com/coreos/go-oidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3093,
  "crawled_at": "2026-04-23T21:01:13"
}
---

coreos
/
go-oidc
Public
Notifications
You must be signed in to change notification settings
Fork
427
Star
2.4k
v3
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
261 Commits
261 Commits
.github
.github
example
example
oidc
oidc
.gitignore
.gitignore
CONTRIBUTING.md
CONTRIBUTING.md
DCO
DCO
LICENSE
LICENSE
MAINTAINERS
MAINTAINERS
NOTICE
NOTICE
README.md
README.md
code-of-conduct.md
code-of-conduct.md
go.mod
go.mod
go.sum
go.sum
View all files
Repository files navigation
go-oidc
Updates from v2 to v3
There were two breaking changes made to the v3 branch. The import path has changed from:
github.com/coreos/go-oidc
to:
github.com/coreos/go-oidc/v3/oidc
And the return type of
NewRemoteKeySet()
is now
*RemoteKeySet
instead of an interface (
#262
).
OpenID Connect support for Go
This package enables OpenID Connect support for the
golang.org/x/oauth2
package.
provider
,
err
:=
oidc
.
NewProvider
(
ctx
,
"https://accounts.google.com"
)
if
err
!=
nil
{
// handle error
}
// Configure an OpenID Connect aware OAuth2 client.
oauth2Config
:=
oauth2.
Config
{
ClientID
:
clientID
,
ClientSecret
:
clientSecret
,
RedirectURL
:
redirectURL
,
// Discovery returns the OAuth2 endpoints.
Endpoint
:
provider
.
Endpoint
(),
// "openid" is a required scope for OpenID Connect flows.
Scopes
: []
string
{
oidc
.
ScopeOpenID
,
"profile"
,
"email"
},
}
OAuth2 redirects are unchanged.
func
handleRedirect
(
w
http.
ResponseWriter
,
r
*
http.
Request
) {
http
.
Redirect
(
w
,
r
,
oauth2Config
.
AuthCodeURL
(
state
),
http
.
StatusFound
)
}
The on responses, the provider can be used to verify ID Tokens.
var
verifier
=
provider
.
Verifier
(
&
oidc.
Config
{
ClientID
:
clientID
})
func
handleOAuth2Callback
(
w
http.
ResponseWriter
,
r
*
http.
Request
) {
// Verify state and errors.
oauth2Token
,
err
:=
oauth2Config
.
Exchange
(
ctx
,
r
.
URL
.
Query
().
Get
(
"code"
))
if
err
!=
nil
{
// handle error
}
// Extract the ID Token from OAuth2 token.
rawIDToken
,
ok
:=
oauth2Token
.
Extra
(
"id_token"
).(
string
)
if
!
ok
{
// handle missing token
}
// Parse and verify ID Token payload.
idToken
,
err
:=
verifier
.
Verify
(
ctx
,
rawIDToken
)
if
err
!=
nil
{
// handle error
}
// Extract custom claims
var
claims
struct
{
Email
string
`json:"email"`
Verified
bool
`json:"email_verified"`
}
if
err
:=
idToken
.
Claims
(
&
claims
);
err
!=
nil
{
// handle error
}
}
About
A Go OpenID Connect client.
Topics
golang
Resources
Readme
License
Apache-2.0 license
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
Custom properties
Stars
2.4k
stars
Watchers
34
watching
Forks
427
forks
Report repository
Releases
28
v3.18.0
Latest
Apr 8, 2026
+ 27 releases
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
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
Go
100.0%