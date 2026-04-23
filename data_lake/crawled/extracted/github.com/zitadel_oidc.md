---
{
  "title": "GitHub - zitadel/oidc: Easy to use OpenID Connect client and server library written for Go and certified by the OpenID Foundation · GitHub",
  "url": "https://github.com/zitadel/oidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 7679,
  "crawled_at": "2026-04-23T20:56:21"
}
---

zitadel
/
oidc
Public
Notifications
You must be signed in to change notification settings
Fork
208
Star
1.8k
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
779 Commits
779 Commits
.codecov
.codecov
.github
.github
example
example
internal
internal
pkg
pkg
.gitignore
.gitignore
.releaserc.js
.releaserc.js
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTING.md
LICENSE
LICENSE
NOTICE
NOTICE
README.md
README.md
SECURITY.md
SECURITY.md
UPGRADING.md
UPGRADING.md
doc.go
doc.go
go.mod
go.mod
go.sum
go.sum
View all files
Repository files navigation
OpenID Connect SDK (client and server) for Go
What Is It
This project is an easy-to-use client (RP) and server (OP) implementation for the
OIDC
(OpenID Connect) standard written for
Go
.
The RP is certified for the
basic
and
config
profile.
Whenever possible we tried to reuse / extend existing packages like
OAuth2 for Go
.
Note
We currently have limited availability for feature reviews:
#785
Basic Overview
The most important packages of the library:
/pkg
    /client            clients using the OP for retrieving, exchanging and verifying tokens
        /rp            definition and implementation of an OIDC Relying Party (client)
        /rs            definition and implementation of an OAuth Resource Server (API)
    /op                definition and implementation of an OIDC OpenID Provider (server)
    /oidc              definitions shared by clients and server

/example
    /client/api        example of an api / resource server implementation using token introspection
    /client/app        web app / RP demonstrating authorization code flow using various authentication methods (code, PKCE, JWT profile)
    /client/github     example of the extended OAuth2 library, providing an HTTP client with a reuse token source
    /client/service    demonstration of JWT Profile Authorization Grant
    /server            examples of an OpenID Provider implementations (including dynamic) with some very basic login UI
Semver
This package uses
semver
for
releases
. Major releases ship breaking changes. Starting with the
v2
to
v3
increment we provide an
upgrade guide
to ease migration to a newer version.
How To Use It
Check the
/example
folder where example code for different scenarios is located.
#
start oidc op server
#
oidc discovery http://localhost:9998/.well-known/openid-configuration
go run github.com/zitadel/oidc/v3/example/server
#
start oidc web client (in a new terminal)
CLIENT_ID=web CLIENT_SECRET=secret ISSUER=http://localhost:9998/ SCOPES=
"
openid profile
"
PORT=9999 go run github.com/zitadel/oidc/v3/example/client/app
open
http://localhost:9999/login
in your browser
you will be redirected to op server and the login UI
login with user
test-user@localhost
and password
verysecure
the OP will redirect you to the client app, which displays the user info
for the dynamic issuer, just start it with:
go run github.com/zitadel/oidc/v3/example/server/dynamic
the oidc web client above will still work, but if you add
oidc.local
(pointing to 127.0.0.1) in your hosts file you can also start it with:
CLIENT_ID=web CLIENT_SECRET=secret ISSUER=http://oidc.local:9998/ SCOPES=
"
openid profile
"
PORT=9999 go run github.com/zitadel/oidc/v3/example/client/app
Note: Usernames are suffixed with the hostname (
test-user@localhost
or
test-user@oidc.local
)
Build Tags
The library uses build tags to enable or disable features. The following build tags are available:
Build Tag
Description
no_otel
Disables the OTel instrumentation, which is enabled by default. This is useful if you do not want to use OTel or if you want to use a different instrumentation library.
Server configuration
Example server allows extra configuration using environment variables and could be used for end-to-end testing of your services.
Name
Format
Description
PORT
Number between 1 and 65535
OIDC listen port
REDIRECT_URI
Comma-separated URIs
List of allowed redirect URIs
USERS_FILE
Path to json in local filesystem
Users with their data and credentials
Here is json equivalent for one of the default users
{
"id2"
: {
"ID"
:
"
id2
"
,
"Username"
:
"
test-user2
"
,
"Password"
:
"
verysecure
"
,
"FirstName"
:
"
Test
"
,
"LastName"
:
"
User2
"
,
"Email"
:
"
test-user2@zitadel.ch
"
,
"EmailVerified"
:
true
,
"Phone"
:
"
"
,
"PhoneVerified"
:
false
,
"PreferredLanguage"
:
"
DE
"
,
"IsAdmin"
:
false
}
}
Features
Relying party
OpenID Provider
Specification
Code Flow
yes
yes
OpenID Connect Core 1.0,
Section 3.1
Implicit Flow
no
1
yes
OpenID Connect Core 1.0,
Section 3.2
Hybrid Flow
no
not yet
OpenID Connect Core 1.0,
Section 3.3
Client Credentials
yes
yes
OpenID Connect Core 1.0,
Section 9
Refresh Token
yes
yes
OpenID Connect Core 1.0,
Section 12
Discovery
yes
yes
OpenID Connect
Discovery
1.0
JWT Profile
yes
yes
RFC 7523
PKCE
yes
yes
RFC 7636
Token Exchange
yes
yes
RFC 8693
Device Authorization
yes
yes
RFC 8628
mTLS
not yet
not yet
RFC 8705
Back-Channel Logout
not yet
yes
OpenID Connect
Back-Channel Logout
1.0
Contributors
Made with
contrib.rocks
.
Resources
For your convenience you can find the relevant guides linked below.
OpenID Connect Core 1.0 incorporating errata set 1
OIDC/OAuth Flow in Zitadel (using this library)
Supported Go Versions
For security reasons, we only support and recommend the use of one of the latest two Go versions (:white_check_mark:).
Versions that also build are marked with :warning:.
Version
Supported
<1.25
❌
1.25
✅
1.26
✅
Why another library
As of 2020 there are not a lot of
OIDC
library's in
Go
which can handle server and client implementations. ZITADEL is strongly committed to the general field of IAM (Identity and Access Management) and as such, we need solid frameworks to implement services.
Goals
Certify this library as OP
Other Go OpenID Connect libraries
https://github.com/coreos/go-oidc
The
go-oidc
does only support
RP
and is not feasible to use as
OP
that's why we could not rely on
go-oidc
https://github.com/ory/fosite
We did not choose
fosite
because it implements
OAuth 2.0
on its own and does not rely on the golang provided package. Nonetheless, this is a great project.
License
The full functionality of this library is and stays open source and free to use for everyone. Visit
our
website
and get in touch.
See the exact licensing terms
here
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "
AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific
language governing permissions and limitations under the License.
Footnotes
https://github.com/zitadel/oidc/issues/135#issuecomment-950563892
↩
About
Easy to use OpenID Connect client and server library written for Go and certified by the OpenID Foundation
zitadel.com
Topics
go
golang
client
oauth
jwt
library
oauth2
server
openidconnect
discovery
standard
openid-connect
oidc
pkce
certified
refresh-token
relying-party
code-flow-pkce
code-flow
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
1.8k
stars
Watchers
15
watching
Forks
208
forks
Report repository
Releases
242
v3.47.5
Latest
Apr 20, 2026
+ 241 releases
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
99.5%
Other
0.5%