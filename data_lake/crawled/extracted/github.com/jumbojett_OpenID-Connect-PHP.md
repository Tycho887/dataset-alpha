---
{
  "title": "GitHub - jumbojett/OpenID-Connect-PHP: Minimalist OpenID Connect client · GitHub",
  "url": "https://github.com/jumbojett/OpenID-Connect-PHP",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 8361,
  "crawled_at": "2026-04-23T20:51:03"
}
---

jumbojett
/
OpenID-Connect-PHP
Public
Notifications
You must be signed in to change notification settings
Fork
402
Star
719
master
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
543 Commits
543 Commits
.github
.github
src
src
tests
tests
.gitattributes
.gitattributes
.gitignore
.gitignore
CHANGELOG.md
CHANGELOG.md
LICENSE
LICENSE
README.md
README.md
client_example.php
client_example.php
composer.json
composer.json
phpunit.xml.dist
phpunit.xml.dist
View all files
Repository files navigation
PHP OpenID Connect Basic Client
A simple library that allows an application to authenticate a user through the basic OpenID Connect flow.
This library hopes to encourage OpenID Connect use by making it simple enough for a developer with little knowledge of
the OpenID Connect protocol to set up authentication.
A special thanks goes to Justin Richer and Amanda Anganes for their help and support of the protocol.
Requirements
PHP 7.2 or greater
CURL extension
JSON extension
Install
Install library using composer
composer require jumbojett/openid-connect-php
Include composer autoloader
require
__DIR__
.
'
/vendor/autoload.php
'
;
Example 1: Basic Client
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
'
ClientSecretHere
'
);
$
oidc
->
setCertPath
(
'
/path/to/my.cert
'
);
$
oidc
->
authenticate
();
$
name
=
$
oidc
->
requestUserInfo
(
'
given_name
'
);
See openid spec for available user attributes
Example 2: Dynamic Registration
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
"
https://id.provider.com
"
);
$
oidc
->
register
();
$
client_id
=
$
oidc
->
getClientID
();
$
client_secret
=
$
oidc
->
getClientSecret
();
// Be sure to add logic to store the client id and client secret
Example 3: Network and Security
// Configure a proxy
$
oidc
->
setHttpProxy
(
"
http://my.proxy.com:80/
"
);
// Configure a cert
$
oidc
->
setCertPath
(
"
/path/to/my.cert
"
);
Example 4: Request Client Credentials Token
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
'
ClientSecretHere
'
);
$
oidc
->
providerConfigParam
([
'
token_endpoint
'
=>
'
https://id.provider.com/connect/token
'
]);
$
oidc
->
addScope
([
'
my_scope
'
]);
// this assumes success (to validate check if the access_token property is there and a valid JWT) :
$
clientCredentialsToken
=
$
oidc
->
requestClientCredentialsToken
()->
access_token
;
Example 5: Request Resource Owners Token (with client auth)
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
'
ClientSecretHere
'
);
$
oidc
->
providerConfigParam
([
'
token_endpoint
'
=>
'
https://id.provider.com/connect/token
'
]);
$
oidc
->
addScope
([
'
my_scope
'
]);
//Add username and password
$
oidc
->
addAuthParam
([
'
username
'
=>
'
<Username>
'
]);
$
oidc
->
addAuthParam
([
'
password
'
=>
'
<Password>
'
]);
//Perform the auth and return the token (to validate check if the access_token property is there and a valid JWT) :
$
token
=
$
oidc
->
requestResourceOwnerToken
(
TRUE
)->
access_token
;
Example 6: Basic client for implicit flow e.g. with Azure AD B2C (see
http://openid.net/specs/openid-connect-core-1_0.html#ImplicitFlowAuth
)
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
'
ClientSecretHere
'
);
$
oidc
->
setResponseTypes
([
'
id_token
'
]);
$
oidc
->
setAllowImplicitFlow
(
true
);
$
oidc
->
addAuthParam
([
'
response_mode
'
=>
'
form_post
'
]);
$
oidc
->
setCertPath
(
'
/path/to/my.cert
'
);
$
oidc
->
authenticate
();
$
sub
=
$
oidc
->
getVerifiedClaims
(
'
sub
'
);
Example 7: Introspection of an access token (see
https://tools.ietf.org/html/rfc7662
)
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
'
ClientSecretHere
'
);
$
data
=
$
oidc
->
introspectToken
(
'
an.access-token.as.given
'
);
if
(!
$
data
->
active
) {
// the token is no longer usable
}
Example 8: PKCE Client
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
null
);
$
oidc
->
setCodeChallengeMethod
(
'
S256
'
);
$
oidc
->
authenticate
();
$
name
=
$
oidc
->
requestUserInfo
(
'
given_name
'
);
Example 9: Back-channel logout
Back-channel authentication assumes you can end a session on the server side on behalf of the user (without relying
on their browser). The request is a POST from the OP direct to your RP. In this way, the use of this library can
ensure your RP performs 'single sign out' for the user even if they didn't have your RP open in a browser or other
device, but still had an active session there.
Either the sid or the sub may be accessible from the logout token sent from the OP. You can use either
getSidFromBackChannel()
or
getSubjectFromBackChannel()
to retrieve them if it is helpful to match them to a session
in order to destroy it.
The below ensures the use of this library to ensure validation of the back-channel logout token, but is afterward
just a hypothetical way of finding such a session and destroying it. Adjust it to the needs of your RP.
function
handleLogout
() {
// NOTE: assumes that $this->oidc is an instance of OpenIDConnectClient()
if
(
$
this
->
oidc
->
verifyLogoutToken
()) {
$
sid
=
$
this
->
oidc
->
getSidFromBackChannel
();
if
(
isset
(
$
sid
)) {
// Somehow find the session based on the $sid and
// destroy it. This depends on your RP's design,
// there is nothing in the OIDC spec to mandate how.
//
// In this example, we find a Redis key, which was
// previously stored using the sid we obtained from
// the access token after login.
//
// The value of the Redis key is that of the user's
// session ID specific to this hypothetical RP app.
//
// We then switch to that session and destroy it.
$
this
->
redis
->
connect
(
'
127.0.0.1
'
,
6379
);
$
session_id_to_destroy
=
$
this
->
redis
->
get
(
$
sid
);
if
(
$
session_id_to_destroy
) {
session_commit
();
session_id
(
$
session_id_to_destroy
);
// switches to that session
session_start
();
$
_SESSION
= [];
// effectively ends the session
}
        }
    }
}
Example 10: Enable Token Endpoint Auth Methods
By default, only
client_secret_basic
is enabled on client side which was the only supported for a long time.
Recently
client_secret_jwt
and
private_key_jwt
have been added, but they remain disabled until explicitly enabled.
use
Jumbojett
\
OpenIDConnectClient
;
$
oidc
=
new
OpenIDConnectClient
(
'
https://id.provider.com
'
,
'
ClientIDHere
'
,
null
);
# enable 'client_secret_basic' and 'client_secret_jwt'
$
oidc
->
setTokenEndpointAuthMethodsSupported
([
'
client_secret_basic
'
,
'
client_secret_jwt
'
]);
# for 'private_key_jwt' in addition also the generator function has to be set.
$
oidc
->
setTokenEndpointAuthMethodsSupported
([
'
private_key_jwt
'
]);
$
oidc
->
setPrivateKeyJwtGenerator
(
function
(
string
$
token_endpoint
) {
# TODO: what ever is necessary
})
Development Environments
In some cases you may need to disable SSL security on your development systems.
Note: This is not recommended on production systems.
$
oidc
->
setVerifyHost
(
false
);
$
oidc
->
setVerifyPeer
(
false
);
Also, your local system might not support HTTPS, so you might disable upgrading to it:
$
oidc
->
setHttpUpgradeInsecureRequests
(
false
);
Todo
Dynamic registration does not support registration auth tokens and endpoints
Contributing
All pull requests, once merged, should be added to the CHANGELOG.md file.
About
Minimalist OpenID Connect client
github.com/jumbojett/OpenID-Connect-PHP
Topics
authentication
protocol
authorization
identity-verification
openid
openid-connect
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
719
stars
Watchers
32
watching
Forks
402
forks
Report repository
Releases
20
v1.0.2
Latest
Sep 13, 2024
+ 19 releases
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
PHP
100.0%