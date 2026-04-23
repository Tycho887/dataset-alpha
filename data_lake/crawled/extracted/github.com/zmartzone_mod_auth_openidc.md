---
{
  "title": "GitHub - OpenIDC/mod_auth_openidc: OpenID Certified™ OpenID Connect and FAPI 2 Relying Party module for Apache HTTPd · GitHub",
  "url": "https://github.com/zmartzone/mod_auth_openidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6721,
  "crawled_at": "2026-04-23T20:56:23"
}
---

OpenIDC
/
mod_auth_openidc
Public
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
331
Star
1.1k
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
2,064 Commits
2,064 Commits
.github
.github
m4
m4
src
src
test
test
.clang-format
.clang-format
.gitignore
.gitignore
AUTHORS
AUTHORS
ChangeLog
ChangeLog
INSTALL
INSTALL
LICENSE.txt
LICENSE.txt
Makefile.am
Makefile.am
README.md
README.md
SECURITY.md
SECURITY.md
auth_openidc.conf
auth_openidc.conf
autogen.sh
autogen.sh
configure.ac
configure.ac
sonar-project.properties
sonar-project.properties
View all files
Repository files navigation
mod_auth_openidc
mod_auth_openidc
is an OpenID Certified™ authentication and authorization module for the Apache 2.x
HTTP server that implements the OpenID Connect 1.x and FAPI 2.x Relying Party functionality.
Overview
This module enables an Apache 2.x web server to operate as an
OpenID Connect
Relying Party
(RP) towards an OpenID Connect
Provider
(OP). It relays end user authentication to a Provider and
receives user identity information from that Provider. It then passes on that identity information (a.k.a. claims)
to applications protected by the Apache web server and establishes an authentication session for the identified user.
The protected content, applications and services can be hosted by the Apache server itself or served from
origin server(s) residing behind it by configuring Apache as a Reverse Proxy in front of those servers. The
latter allows for adding OpenID Connect based authentication to existing applications/services/SPAs without
modifying those applications, possibly migrating them away from legacy authentication mechanisms to standards-based
OpenID Connect Single Sign On (SSO).
By default the module sets the
REMOTE_USER
variable to the
id_token
[sub]
claim, concatenated with the OP's Issuer
identifier (
[sub]@[iss]
). Other
id_token
claims are passed in HTTP headers and/or environment variables together with those
(optionally) obtained from the UserInfo endpoint. The provided HTTP headers and environment variables can be consumed by
applications protected by the Apache server.
Custom fine-grained authorization rules - based on Apache's
Require
primitives - can be specified to match against the
set of claims provided in the
id_token
/
userinfo
claims, see
here
.
Clustering for resilience and performance can be configured using one of the supported cache backends options as
listed
here
.
For a complete overview of all configuration options, see the file
auth_openidc.conf
.
This file can also serve as an include file for
httpd.conf
.
How to Use It
install and load
mod_auth_openidc.so
in your Apache server
set
OIDCRedirectURI
to a "vanity" URL within a location that is protected by mod_auth_openidc
configure
OIDCProviderMetadataURL
so it points to the Discovery metadata of your OpenID Connect Provider served on the
.well-known/openid-configuration
endpoint
register/generate a Client identifier and a secret with the OpenID Connect Provider and configure those in
OIDCClientID
and
OIDCClientSecret
respectively
register the
OIDCRedirectURI
configured above as the Redirect or Callback URI for your client at the Provider
configure your protected content/locations with
AuthType openid-connect
A minimal working configuration would look like:
LoadModule
auth_openidc_module modules/mod_auth_openidc.so
# OIDCRedirectURI is a vanity URL that must point to a path protected by this module but must NOT point to any content
OIDCRedirectURI https://<hostname>/secure/redirect_uri

OIDCProviderMetadataURL <issuer>/.well-known/openid-configuration
OIDCClientID <client_id>
OIDCClientSecret <client_secret>

<
Location
/secure
>
AuthType
openid-connect
Require
valid-user
</
Location
>
For claims-based authorization with
Require claim:
directives see the
Wiki page on Authorization
. For details on configuring multiple providers see the
Wiki
.
Quickstart for specific Providers
Keycloak
Microsoft Entra ID (Azure AD)
Google Accounts
Sign in with Apple
GLUU Server
Curity Identity Server
and
more
See the
Wiki
for configuration docs for other OpenID Connect Providers.
Interoperability and Supported Specifications
mod_auth_openidc
is
OpenID Certified™
and supports the following specifications:
OpenID Connect Core 1.0
(Basic, Implicit, Hybrid and Refresh flows)
RFC 7636 - Proof Key for Code Exchange by OAuth Public Clients
FAPI 2.0 Security Profile
FAPI 2.0 Message Signing
RFC 9126 - OAuth 2.0 Pushed Authorization Requests
RFC 9449 - OAuth 2.0 Demonstrating Proof of Possession (DPoP)
OpenID Connect Discovery 1.0
OpenID Connect Dynamic Client Registration 1.0
OAuth 2.0 Form Post Response Mode 1.0
OAuth 2.0 Multiple Response Type Encoding Practices 1.0
OpenID Connect Session Management 1.0
see the
Wiki
for information on how to configure it)
OpenID Connect Front-Channel Logout 1.0
OpenID Connect Back-Channel Logout 1.0
Support
Community
Documentation can be found at the Wiki (including Frequently Asked Questions) at:
https://github.com/OpenIDC/mod_auth_openidc/wiki
For questions, issues and suggestions use the Github Discussions forum at:
https://github.com/OpenIDC/mod_auth_openidc/discussions
Commercial
Licensed builds with support for Redis/Valkey over TLS, Redis Sentinel/Cluster as well as binary packages for Microsoft Windows, EOL Red Hat, Ubuntu and Debian releases, Oracle HTTP Server and IBM HTTP Server are available under a commercial agreement.
For inquiries about commercial - subscription based - support and licensing please contact:
sales@openidc.com
Disclaimer
This software is open sourced by OpenIDC, a subsidiary of ZmartZone Holding B.V. For commercial services
you can contact
OpenIDC
as described above in the
Support
section.
About
OpenID Certified™ OpenID Connect and FAPI 2 Relying Party module for Apache HTTPd
www.openidc.com
Topics
c
authentication
sso
apache-httpd
openidc
openid-connect
oidc
access-control
openidconnect-client
Resources
Readme
License
Apache-2.0 license
Security policy
Security policy
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
1.1k
stars
Watchers
63
watching
Forks
331
forks
Report repository
Releases
110
release 2.4.19.2
Latest
Feb 23, 2026
+ 109 releases
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
C
98.3%
M4
1.3%
Other
0.4%