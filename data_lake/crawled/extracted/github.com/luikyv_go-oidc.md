---
{
  "title": "GitHub - luikyv/go-oidc: A configurable OpenID Provider built in Go. · GitHub",
  "url": "https://github.com/luikyv/go-oidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 16993,
  "crawled_at": "2026-04-23T20:56:09"
}
---

luikyv
/
go-oidc
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
12
Star
96
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
531 Commits
531 Commits
.claude/
skills/
test
.claude/
skills/
test
.github
.github
examples
examples
internal
internal
pkg
pkg
.gitignore
.gitignore
.golangci.yml
.golangci.yml
.pre-commit-config.yaml
.pre-commit-config.yaml
CONTRIBUTING.md
CONTRIBUTING.md
LICENSE
LICENSE
Makefile
Makefile
README.md
README.md
docker-compose.yml
docker-compose.yml
go.mod
go.mod
go.sum
go.sum
View all files
Repository files navigation
go-oidc
A configurable OpenID Connect Provider for Go.
Supported Specifications
OpenID Connect Core 1.0
OpenID Connect Discovery 1.0
RFC 6749
- The OAuth 2.0 Authorization Framework
OpenID Connect Dynamic Client Registration 1.0
RFC 7591
- OAuth 2.0 Dynamic Client Registration Protocol (DCR)
RFC 7592
- OAuth 2.0 Dynamic Client Registration Management Protocol (DCM)
RFC 9126
- OAuth 2.0 Pushed Authorization Requests (PAR)
RFC 9101
- The OAuth 2.0 Authorization Framework: JWT-Secured Authorization Request (JAR)
JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
RFC 7636
- Proof Key for Code Exchange by OAuth Public Clients (PKCE)
RFC 9207
- OAuth 2.0 Authorization Server Issuer Identification
RFC 8705
- OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens
RFC 9449
- OAuth 2.0 Demonstrating Proof of Possession (DPoP)
RFC 9396
- OAuth 2.0 Rich Authorization Requests (RAR)
RFC 8707
- Resource Indicators for OAuth 2.0
RFC 7662
- OAuth 2.0 Token Introspection
RFC 7009
- OAuth 2.0 Token Revocation
RFC 8252
- OAuth 2.0 for Native Apps
FAPI 1.0 Security Profile 1.0 - Part 1: Baseline
FAPI 1.0 Security Profile 1.0 - Part 2: Advanced
FAPI 2.0 Security Profile
OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0 (CIBA)
OpenID Federation 1.0
OpenID Connect RP-Initiated Logout 1.0
OpenID Shared Signals Framework Specification 1.0
Certification
Luiky Vasconcelos has certified that
go-oidc
conforms to the following profiles of the OpenID Connect™ protocol.
Basic OP, Implicit OP, Hybrid OP, Config OP and Dynamic OP
FAPI 1.0
FAPI 2.0
Get Started
Install the module:
go get github.com/luikyv/go-oidc@latest
Create and run a provider:
key
,
_
:=
rsa
.
GenerateKey
(
rand
.
Reader
,
2048
)
jwks
:=
goidc.
JSONWebKeySet
{
Keys
: []goidc.
JSONWebKey
{{
KeyID
:
"key_id"
,
Key
:
key
,
Algorithm
:
"RS256"
,
  }},
}
op
,
_
:=
provider
.
New
(
goidc
.
ProfileOpenID
,
"http://localhost"
,
func
(
_
context.
Context
) (goidc.
JSONWebKeySet
,
error
) {
return
jwks
,
nil
},
)
op
.
Run
(
":80"
)
Verify the setup at
http://localhost/.well-known/openid-configuration
.
Table of Contents
Running the Provider
Entities
Authentication Policies
Signing and Encryption
Tokens
Scopes
Dynamic Client Registration
Mutual TLS
JAR
JARM
OpenID Federation
Shared Signals Framework
Running the Provider
The simplest way to run the provider:
op
.
Run
(
":80"
)
For more flexibility, use
op.Handler()
to get an
http.Handler
with all endpoints configured:
mux
:=
http
.
NewServeMux
()
mux
.
Handle
(
"/"
,
op
.
Handler
())
server
:=
&
http.
Server
{
Addr
:
":443"
,
Handler
:
mux
,
}
server
.
ListenAndServeTLS
(
certFilePath
,
certKeyFilePath
)
Entities
go-oidc revolves around four entities:
goidc.Client
,
goidc.AuthnSession
,
goidc.Grant
and
goidc.Token
.
These entities are managed by implementations of
goidc.ClientManager
,
goidc.AuthnSessionManager
,
goidc.GrantManager
and
goidc.TokenManager
respectively.
By default, all entities are stored in memory and lost when the server shuts down. For production, replace the default managers with persistent implementations using
provider.WithClientManager
,
provider.WithAuthnSessionManager
,
provider.WithGrantManager
and
provider.WithTokenManager
.
Client
goidc.Client
represents an OAuth 2.0 client that interacts with the authorization server to request tokens and access protected resources. It is always identified and queried by its ID.
Authentication Session
goidc.AuthnSession
is a short-lived session that tracks the state of an authorization request as it progresses through authentication.
At any given time,
goidc.AuthnSession
has an ID and exactly one of the following lookup identifiers:
Pushed Authorization Request ID
– Created during
POST /par
. See
RFC 9126
.
Callback ID
– Present while the authentication policy is in progress.
Authorization Code
– Set when authentication completes successfully with the
authorization_code
grant type.
Authentication Request ID
– Used for CIBA. See
CIBA
.
Grant
goidc.Grant
represents what a user (or the client itself) has authorized: the subject, scopes, authorization details, resources, and proof-of-possession bindings (DPoP or mTLS).
It may contain the following lookup identifiers:
Refresh Token
– Present when the grant allows refresh tokens.
Authorization Code
– Present for the
authorization_code
grant type.
Token
goidc.Token
is the credential issued under a grant. It captures a snapshot of the active scopes, resources, and authorization details at the moment of issuance, which may be a subset of what the grant holds.
Each token has its own lifetime and is linked to its grant via
GrantID
. During a refresh token request, a new token is issued under the same grant. The refresh token on the grant is updated only if rotation is enabled.
Authentication Policies
Authorization requests (starting at
/authorize
by default) are handled by
goidc.AuthnPolicy
. A policy has two parts:
Setup function
– Determines whether the policy applies to a given request. If it returns
false
, the policy is skipped.
Authentication function
– Handles user interaction and authentication.
The authentication function returns one of:
goidc.StatusSuccess
– Authentication succeeded. The
Subject
field on the session must be set.
goidc.StatusInProgress
– Awaiting user interaction. Authentication resumes when a request is made to
/authorize/{callback_id}
(the callback ID is available via
goidc.AuthnSession.CallbackID
).
goidc.StatusFailure
(or an error) – Authentication failed, and the grant is denied.
policy
:=
goidc
.
NewPolicy
(
"main_policy"
,
func
(
_
*
http.
Request
,
_
*
goidc.
Client
,
_
*
goidc.
AuthnSession
)
bool
{
return
true
},
func
(
w
http.
ResponseWriter
,
r
*
http.
Request
,
as
*
goidc.
AuthnSession
) (goidc.
Status
,
error
) {
username
:=
r
.
PostFormValue
(
"username"
)
if
username
==
""
{
renderHTMLPage
(
w
)
return
goidc
.
StatusInProgress
,
nil
}
if
username
==
"banned_user"
{
return
goidc
.
StatusFailure
,
errors
.
New
(
"the user is banned"
)
    }
as
.
Subject
=
username
return
goidc
.
StatusSuccess
,
nil
},
)
op
,
_
:=
provider.
New
(
...
,
provider
.
WithAuthorizationCodeGrant
(),
provider
.
WithPolicies
(
policy
),
...
,
)
For more examples, see the
examples
folder.
Signing and Encryption
When creating a
provider.Provider
, a JWKS function must be provided. This function returns the keys used for signing and encryption. It should typically return both private and public key material.
Every algorithm configured for the provider must have a corresponding JWK in the JWKS.
key
,
_
:=
rsa
.
GenerateKey
(
rand
.
Reader
,
2048
)
jwks
:=
goidc.
JSONWebKeySet
{
Keys
: []goidc.
JSONWebKey
{{
KeyID
:
"key_id"
,
Key
:
key
,
Algorithm
:
"RS256"
,
  }},
}
op
,
_
:=
provider
.
New
(
goidc
.
ProfileOpenID
,
"http://localhost"
,
func
(
_
context.
Context
) (goidc.
JSONWebKeySet
,
error
) {
return
jwks
,
nil
},
)
If direct access to private keys is unavailable or granular control over signing is needed, the JWKS function can return only public key material. In that case,
provider.WithSignerFunc
must be added:
key
,
_
:=
rsa
.
GenerateKey
(
rand
.
Reader
,
2048
)
jwks
:=
goidc.
JSONWebKeySet
{
Keys
: []goidc.
JSONWebKey
{{
KeyID
:
"key_id"
,
Key
:
key
.
Public
(),
Algorithm
:
"RS256"
,
  }},
}
op
,
_
:=
provider
.
New
(
goidc
.
ProfileOpenID
,
"http://localhost"
,
func
(
_
context.
Context
) (goidc.
JSONWebKeySet
,
error
) {
return
jwks
,
nil
},
provider
.
WithSignerFunc
(
func
(
_
context.
Context
,
_
goidc.
SignatureAlgorithm
) (
kid
string
,
signer
crypto.
Signer
,
err
error
) {
return
"key_id"
,
key
,
nil
}),
)
Similarly, if server-side decryption is needed (e.g., for encrypted JARs), configure
provider.WithDecrypterFunc
.
Tokens
ID tokens are signed using
RS256
by default. Use
provider.WithIDTokenSignatureAlgs
to change the default or add additional algorithms.
Access tokens are
opaque
by default. To customize this, provide a
goidc.TokenOptionsFunc
:
op
,
_
:=
provider.
New
(
...
,
provider
.
WithTokenOptions
(
func
(
_
context.
Context
,
_
*
goidc.
Grant
,
_
*
goidc.
Client
) goidc.
TokenOptions
{
return
goidc
.
NewJWTTokenOptions
(
goidc
.
RS256
,
600
)
  }),
...
,
)
Use
goidc.NewJWTTokenOptions
for JWT access tokens or
goidc.NewOpaqueTokenOptions
for opaque ones.
Refresh tokens are always opaque.
Scopes
goidc.NewScope
creates a scope matched by exact string comparison:
scope
:=
goidc
.
NewScope
(
"openid"
)
goidc.NewDynamicScope
creates a scope with custom matching logic:
paymentScope
:=
goidc
.
NewDynamicScope
(
"payment"
,
func
(
requestedScope
string
)
bool
{
return
strings
.
HasPrefix
(
requestedScope
,
"payment:"
)
})
paymentScope
.
Matches
(
"payment:30"
)
// true
Dynamic scopes appear by their base name (e.g., "payment") in
scopes_supported
.
op
,
_
:=
provider.
New
(
...
,
provider
.
WithScopes
(
goidc
.
ScopeOpenID
,
goidc
.
ScopeOfflineAccess
),
...
,
)
Dynamic Client Registration (DCR)
DCR allows clients to register and update themselves dynamically:
op
,
_
:=
provider.
New
(
...
,
provider
.
WithDCR
(),
...
,
)
Use
provider.WithDCRHandleClientFunc
to run custom logic during registration and update requests, such as validation or setting default metadata values.
Use
provider.WithDCRValidateInitialTokenFunc
(
goidc.DCRValidateInitialTokenFunc
) to validate the initial access token during registration. Omit this option to skip validation.
By default, the DCR endpoint is
/register
and the management endpoint is
/register/{client_id}
.
To rotate the registration access token on each update request, add
provider.WithDCRTokenRotation()
.
Mutual TLS (mTLS)
mTLS enables client authentication and certificate-bound access tokens via TLS certificates:
op
,
_
:=
provider.
New
(
...
,
provider
.
WithMTLS
(
"https://matls-go-oidc.com"
,
func
(context.
Context
) (
*
x509.
Certificate
,
error
) {
...
},
  ),
...
,
)
All enabled endpoints are listed under
mtls_endpoint_aliases
in the discovery response:
{
"mtls_endpoint_aliases"
: {
"token_endpoint"
:
"
https://matls-go-oidc.com/token
"
}
}
The certificate function (
goidc.ClientCertFunc
) may be called multiple times per request. Consider caching the result if extraction is expensive.
JWT-Secured Authorization Request (JAR)
JAR
allows clients to send authorization requests as signed (and optionally encrypted) JWTs:
op
,
_
:=
provider.
New
(
...
,
provider
.
WithJAR
(
goidc
.
RS256
,
goidc
.
PS256
),
...
,
)
This adds the following to the discovery response:
{
"request_parameter_supported"
:
true
,
"request_object_signing_alg_values_supported"
: [
"
RS256
"
,
"
PS256
"
]
}
To enable encryption:
provider
.
WithJAREncryption
(
goidc
.
RSA_OAEP_256
)
To customize content encryption algorithms, use
provider.WithJARContentEncryptionAlgs
.
JWT-Secured Authorization Response Mode (JARM)
JARM
returns authorization responses as signed (and optionally encrypted) JWTs, adding the response modes
jwt
,
query.jwt
,
fragment.jwt
and
form_post.jwt
:
op
,
_
:=
provider.
New
(
...
,
provider
.
WithJARM
(
goidc
.
RS256
,
goidc
.
PS256
),
...
,
)
To enable encryption:
provider
.
WithJARMEncryption
(
goidc
.
RSA_OAEP_256
)
To customize content encryption algorithms, use
provider.WithJARMContentEncryptionAlgs
.
Rich Authorization Requests
RAR
allows clients to request fine-grained access using structured
authorization_details
objects. Each detail has a
type
field that maps to a registered handler.
op
,
_
:=
provider.
New
(
...
,
provider
.
WithRAR
(
"payment_initiation"
),
...
,
)
When using the
authorization_code
or
refresh_token
grant types, the client may request a subset of the originally granted authorization details. Provide
provider.WithRARCompareDetailsFunc
to enforce consistency between the granted and requested sets:
provider
.
WithRARCompareDetailsFunc
(
func
(
ctx
context.
Context
,
granted
,
requested
[]goidc.
AuthorizationDetail
)
error
{
// Verify that every requested detail is consistent with the granted ones.
return
nil
})
OpenID Federation
OpenID Federation
establishes trust dynamically through signed entity statements, allowing federated clients to authenticate without prior manual registration.
op
,
_
:=
provider.
New
(
...
,
provider
.
WithOpenIDFederation
(
func
(
_
context.
Context
) (goidc.
JSONWebKeySet
,
error
) {
return
fedJWKS
,
nil
},
"https://trust-anchor.example.com"
,
  ),
provider
.
WithOpenIDFedAuthorityHints
(
"https://intermediate.example.com"
),
...
,
)
The entity configuration is exposed at
GET /.well-known/openid-federation
.
Client Registration Types
Federated clients can use automatic or explicit registration:
provider
.
WithOpenIDFedClientRegistrationTypes
(
goidc
.
ClientRegistrationTypeAutomatic
,
goidc
.
ClientRegistrationTypeExplicit
,
)
With
automatic
registration, the provider resolves the trust chain by fetching entity configurations and subordinate statements. With
explicit
registration, the client provides the trust chain directly.
Trust Marks
Require specific trust marks from clients:
provider
.
WithOpenIDFedRequiredTrustMarksFunc
(
func
(
_
context.
Context
,
_
*
goidc.
Client
) []goidc.
TrustMark
{
return
[]goidc.
TrustMark
{
"https://trust-anchor.example.com/marks/certified"
}
  },
)
Include trust marks in the provider's entity configuration:
provider
.
WithOpenIDFedTrustMark
(
"https://trust-anchor.example.com/marks/certified"
,
"https://trust-mark-issuer.example.com"
,
)
Additional Options
provider
.
WithOpenIDFedSignatureAlgs
(
goidc
.
RS256
,
goidc
.
PS256
)
provider
.
WithOpenIDFedTrustChainMaxDepth
(
5
)
provider
.
WithOpenIDFedOrganizationName
(
"Example Organization"
)
provider
.
WithOpenIDFedHTTPClientFunc
(
func
(
_
context.
Context
)
*
http.
Client
{
return
customHTTPClient
})
Shared Signals Framework (SSF)
The
Shared Signals Framework
allows the provider to act as an SSF transmitter, publishing Security Event Tokens (SETs) to receivers. go-oidc supports
CAEP
and
RISC
event types.
op
,
_
:=
provider.
New
(
...
,
provider
.
WithSSF
(
func
(
_
context.
Context
) (goidc.
JSONWebKeySet
,
error
) {
return
ssfJWKS
,
nil
},
func
(
ctx
context.
Context
) (goidc.
SSFReceiver
,
error
) {
return
goidc.
SSFReceiver
{
ID
:
"receiver"
},
nil
},
  ),
provider
.
WithSSFEventTypes
(
goidc
.
SSFEventTypeCAEPSessionRevoked
,
goidc
.
SSFEventTypeCAEPCredentialChange
),
provider
.
WithSSFDeliveryMethods
(
goidc
.
SSFDeliveryMethodPoll
,
goidc
.
SSFDeliveryMethodPush
),
...
,
)
The transmitter configuration is exposed at
GET /.well-known/ssf-configuration
.
Push delivery (
RFC 8935
) sends SETs to a receiver-provided endpoint. Poll delivery (
RFC 8936
) lets receivers fetch pending events from
/ssf/poll
.
To publish events:
op
.
PublishSSFEvent
(
ctx
,
streamID
, goidc.
SSFEvent
{
Type
:
goidc
.
SSFEventTypeCAEPSessionRevoked
,
Subject
: goidc.
SSFSubject
{
Format
:
goidc
.
SSFSubjectFormatEmail
,
Email
:
"user@example.com"
,
  },
})
Additional options:
// Allow receivers to update stream status (enabled/paused/disabled).
provider
.
WithSSFEventStreamStatusManagement
()
// Allow receivers to add/remove subjects from a stream.
provider
.
WithSSFEventStreamSubjectManagement
()
// Allow receivers to request verification events.
provider
.
WithSSFEventStreamVerification
(
func
(
ctx
context.
Context
,
streamID
string
,
opts
goidc.
SSFStreamVerificationOptions
)
error
{
// Schedule the verification event for async delivery.
return
nil
})
For production, replace the in-memory SSF storage with persistent implementations using
provider.WithSSFEventStreamManager
and
provider.WithSSFEventPollManager
.
For a complete example, see
examples/ssf
.
About
A configurable OpenID Provider built in Go.
Resources
Readme
License
MIT license
Contributing
Contributing
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
96
stars
Watchers
6
watching
Forks
12
forks
Report repository
Releases
22
v0.18.0
Latest
Apr 18, 2026
+ 21 releases
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
Go
99.1%
Makefile
0.9%