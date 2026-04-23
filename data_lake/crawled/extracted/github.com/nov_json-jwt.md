---
{
  "title": "GitHub - nov/json-jwt: JSON Web Token and its family (JSON Web Signature, JSON Web Encryption and JSON Web Key) in Ruby · GitHub",
  "url": "https://github.com/nov/json-jwt",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3378,
  "crawled_at": "2026-04-23T20:48:19"
}
---

nov
/
json-jwt
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
82
Star
299
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
477 Commits
477 Commits
.github
.github
lib/
json
lib/
json
spec
spec
.gitignore
.gitignore
.gitmodules
.gitmodules
.rspec
.rspec
CHANGELOG.md
CHANGELOG.md
Gemfile
Gemfile
LICENSE
LICENSE
README.md
README.md
Rakefile
Rakefile
VERSION
VERSION
json-jwt.gemspec
json-jwt.gemspec
View all files
Repository files navigation
JSON::JWT
JSON Web Token and its family (JSON Web Signature, JSON Web Encryption and JSON Web Key) in Ruby
Installation
gem install json-jwt
Resources
View Source on GitHub (
https://github.com/nov/json-jwt
)
Report Issues on GitHub (
https://github.com/nov/json-jwt/issues
)
Documentation on GitHub (
https://github.com/nov/json-jwt/wiki
)
Examples
require
'json/jwt'
private_key
=
OpenSSL
::
PKey
::
RSA
.
new
<<-PEM
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAyBKIFSH8dP6bDkGBziB6RXTTfZVTaaNSWNtIzDmgRFi6FbLo
:
-----END RSA PRIVATE KEY-----
PEM
public_key
=
OpenSSL
::
PKey
::
RSA
.
new
<<-PEM
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyBKIFSH8dP6bDkGBziB6
:
-----END PUBLIC KEY-----
PEM
# Sign & Encode
claim
=
{
iss
:
'nov'
,
exp
:
1
.
week
.
from_now
,
nbf
:
Time
.
now
}
jws
=
JSON
::
JWT
.
new
(
claim
)
.
sign
(
private_key
,
:RS256
)
jws
.
to_s
# Decode & Verify
input
=
"jwt_header.jwt_claims.jwt_signature"
JSON
::
JWT
.
decode
(
input
,
public_key
)
If you need to get a JWK from
jwks_uri
of OpenID Connect IdP, you can use
JSON::JWK::Set::Fetcher
to fetch (& optionally cache) it.
# JWK Set Fetching & Caching
# NOTE: Optionally by setting cache instance, JWKs are cached by kid.
JSON
::
JWK
::
Set
::
Fetcher
.
cache
=
Rails
.
cache
JSON
::
JWK
::
Set
::
Fetcher
.
fetch
(
jwks_uri
,
kid
:
kid
)
# => returns JSON::JWK instance or raise JSON::JWK::Set::KidNotFound
For more details, read
Documentation Wiki
.
Note on Patches/Pull Requests
Fork the project.
Make your feature addition or bug fix.
Add tests for it. This is important so I don't break it in a
future version unintentionally.
Commit, do not mess with rakefile, version, or history.
(if you want to have your own version, that is fine but bump version in a commit by itself I can ignore when I pull)
Send me a pull request. Bonus points for topic branches.
Copyright
Copyright (c) 2011 nov matake. See LICENSE for details.
About
JSON Web Token and its family (JSON Web Signature, JSON Web Encryption and JSON Web Key) in Ruby
Topics
jwt
jose
jwk
jwe
jws
json-web-key
json-web-encryption
json-web-signature
json-web-token
Resources
Readme
License
MIT license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
299
stars
Watchers
10
watching
Forks
82
forks
Report repository
Releases
9
v1.17.0
Latest
Aug 9, 2025
+ 8 releases
Sponsor this project
Sponsor
Uh oh!
There was an error while loading.
Please reload this page
.
Learn more about GitHub Sponsors
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
Ruby
100.0%