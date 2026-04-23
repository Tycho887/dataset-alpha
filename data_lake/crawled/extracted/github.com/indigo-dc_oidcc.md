---
{
  "title": "GitHub - erlef/oidcc: OpenId Connect client library in Erlang & Elixir · GitHub",
  "url": "https://github.com/indigo-dc/oidcc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6570,
  "crawled_at": "2026-04-23T20:56:00"
}
---

erlef
/
oidcc
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
63
Star
227
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
743 Commits
743 Commits
.github
.github
LICENSES
LICENSES
assets
assets
certification
certification
guides
guides
include
include
lib
lib
priv/
test/
fixtures
priv/
test/
fixtures
src
src
test
test
.credo.exs
.credo.exs
.env
.env
.formatter.exs
.formatter.exs
.gitignore
.gitignore
.tool-versions
.tool-versions
LICENSE
LICENSE
README.md
README.md
elvis.config
elvis.config
mix.exs
mix.exs
rebar.config
rebar.config
rebar.config.script
rebar.config.script
View all files
Repository files navigation
oidcc
OpenID Connect client library for Erlang.
OpenID Certified by
Jonatan Männchen
at the
Erlang Ecosystem Foundation
of multiple Relaying
Party conformance profiles of the OpenID Connect protocol:
For details, check the
Conformance Test Suite
.
The refactoring for
v3
and the certification is funded as an
Erlang Ecosystem Foundation
stipend entered by the
Security Working Group
.
A security audit was performed by
SAFE-Erlang-Elixir
more info
HERE
.
Supported Features
Discovery
(
[ISSUER]/.well-known/openid-configuration
)
Client Registration
Authorization (Code Flow)
Request Object
PKCE
Pushed Authorization Requests
Authorization Server Issuer Identification
Token
Authorization:
client_secret_basic
,
client_secret_post
,
client_secret_jwt
, and
private_key_jwt
Grant Types:
authorization_code
,
refresh_token
,
jwt_bearer
, and
client_credentials
Automatic JWK Refreshing when needed
Userinfo
JWT Response
Aggregated and Distributed Claims
Token Introspection
Logout
RP-Initiated
JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
Demonstrating Proof of Possession (DPoP)
OAuth 2 Purpose Request Parameter
Profiles
FAPI 2.0 Security Profile
FAPI 2.0 Message Signing
Setup
Please note that the minimum supported Erlang OTP version is OTP26.
Erlang
directly
{
ok
,
Pid
}
=
oidcc_provider_configuration_worker
:
start_link
(#{
issuer
=>
<<
"
https://accounts.google.com
"
>>,
name
=>
{
local
,
google_config_provider
}
    }).
via
supervisor
-
behaviour
(
supervisor
).
%
% ...
init
(
_Args
)
->
SupFlags
=
#{
strategy
=>
one_for_one
},
ChildSpecs
=
[
        #{
id
=>
oidcc_provider_configuration_worker
,
start
=>
{
oidcc_provider_configuration_worker
,
start_link
, [
                    #{
issuer
=>
"
https://accounts.google.com
"
,
name
=>
{
local
,
myapp_oidcc_config_provider
}
                    }
                ]},
shutdown
=>
brutal_kill
}
    ],
    {
ok
, {
SupFlags
,
ChildSpecs
}}.
Elixir
directly
{
:ok
,
_pid
}
=
Oidcc.ProviderConfiguration.Worker
.
start_link
(
%
{
issuer:
"https://accounts.google.com"
,
name:
Myapp.OidccConfigProvider
}
)
via
Supervisor
Supervisor
.
init
(
[
{
Oidcc.ProviderConfiguration.Worker
,
%
{
issuer:
"https://accounts.google.com"
,
name:
Myapp.OidccConfigProvider
}
}
]
,
strategy:
:one_for_one
)
using
igniter
mix oidcc.gen.provider_configuration_worker \
  --name MyApp.OidccConfigProvider \
  --issuer https://accounts.google.com
Usage
Companion libraries
oidcc
offers integrations for various libraries:
oidcc_cowboy
- Integrations for
cowboy
oidcc_plug
- Integrations for
plug
and
phoenix
ueberauth_oidcc
- Integration for
ueberauth
Erlang
%
% Create redirect URI for authorization
{
ok
,
RedirectUri
}
=
oidcc
:
create_redirect_url
(
myapp_oidcc_config_provider
,
    <<
"
client_id
"
>>,
    <<
"
client_secret
"
>>,
    #{
redirect_uri
=>
<<
"
https://example.com/callback
"
>>}
),
%
% Redirect user to `RedirectUri`
%
% Retrieve `code` query / form param from redirect back
%
% Exchange code for token
{
ok
,
Token
}
=
oidcc
:
retrieve_token
(
AuthCode
,
myapp_oidcc_config_provider
,
        <<
"
client_id
"
>>,
        <<
"
client_secret
"
>>,
        #{
redirect_uri
=>
<<
"
https://example.com/callback
"
>>}
    ),
%
% Load userinfo for token
{
ok
,
Claims
}
=
oidcc
:
retrieve_userinfo
(
Token
,
myapp_oidcc_config_provider
,
        <<
"
client_id
"
>>,
        <<
"
client_secret
"
>>,
        #{}
    ),
%
% Load introspection for access token
{
ok
,
Introspection
}
=
oidcc
:
introspect_token
(
Token
,
myapp_oidcc_config_provider
,
        <<
"
client_id
"
>>,
        <<
"
client_secret
"
>>,
        #{}
    ),
%
% Refresh token when it expires
{
ok
,
RefreshedToken
}
=
oidcc
:
refresh_token
(
Token
,
myapp_oidcc_config_provider
,
        <<
"
client_id
"
>>,
        <<
"
client_secret
"
>>,
        #{}
    ).
for more details, see
https://hexdocs.pm/oidcc/oidcc.html
Elixir
# Create redirect URI for authorization
{
:ok
,
redirect_uri
}
=
Oidcc
.
create_redirect_url
(
Myapp.OidccConfigProvider
,
"client_id"
,
"client_secret"
,
%
{
redirect_uri:
"https://example.com/callback"
}
)
# Redirect user to `redirect_uri`
# Retrieve `code` query / form param from redirect back
# Exchange code for token
{
:ok
,
token
}
=
Oidcc
.
retrieve_token
(
auth_code
,
Myapp.OidccConfigProvider
,
"client_id"
,
"client_secret"
,
%
{
redirect_uri:
"https://example.com/callback"
}
)
# Load userinfo for token
{
:ok
,
claims
}
=
Oidcc
.
retrieve_userinfo
(
token
,
Myapp.OidccConfigProvider
,
"client_id"
,
"client_secret"
,
%
{
expected_subject:
"sub"
}
)
# Load introspection for access token
{
:ok
,
introspection
}
=
Oidcc
.
introspect_token
(
token
,
Myapp.OidccConfigProvider
,
"client_id"
,
"client_secret"
)
# Refresh token when it expires
{
:ok
,
refreshed_token
}
=
Oidcc
.
refresh_token
(
token
,
Myapp.OidccConfigProvider
,
"client_id"
,
"client_secret"
)
for more details, see
https://hexdocs.pm/oidcc/Oidcc.html
About
OpenId Connect client library in Erlang & Elixir
hexdocs.pm/oidcc
Topics
client
erlang
elixir
openid
openid-connect
openid-client
security-wg
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
227
stars
Watchers
11
watching
Forks
63
forks
Report repository
Releases
51
v3.7.2
Latest
Apr 14, 2026
+ 50 releases
Sponsor this project
Uh oh!
There was an error while loading.
Please reload this page
.
https://members.erlef.org/join-us
https://erlef.org/sponsors#become-a-sponsor
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
Erlang
79.7%
Elixir
20.3%