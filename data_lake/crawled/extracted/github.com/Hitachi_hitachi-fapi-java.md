---
{
  "title": "GitHub - Hitachi/hitachi-fapi-java · GitHub",
  "url": "https://github.com/Hitachi/hitachi-fapi-java",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3055,
  "crawled_at": "2026-04-23T20:51:54"
}
---

Hitachi
/
hitachi-fapi-java
Public
Notifications
You must be signed in to change notification settings
Fork
0
Star
12
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
3 Commits
3 Commits
certs
certs
client
client
server
server
.gitignore
.gitignore
LICENSE
LICENSE
OpenID-Certified-Mark.png
OpenID-Certified-Mark.png
README.md
README.md
keycloak-export.json
keycloak-export.json
keycloak.p12
keycloak.p12
pom.xml
pom.xml
truststore.p12
truststore.p12
View all files
Repository files navigation
Hitachi FAPI Implementation for Java
Reference Implementation of Financial-grade API 1.0(FAPI 1.0) Client Application and Resource Server following
Financial-grade API Security Profile 1.0 - Part 2: Advanced
Certification
Hitachi has
certified
that Reference Implementation of FAPI 1.0 Client Application conforms to the following profiles of the OpenID Connect™ protocol
FAPI Adv. RP w/ MTLS
FAPI Adv. RP w/ Private Key
Specs of Client Application
TLS
JSON Web Key (
RFC7517
)
Support Obtaining Authorization Server Metadata (
Chapter 3 of RFC8414
)
Hybrid Flow (
Section 3.3 of OpenID Connect Core 1.0 incorporating errata set 1
)
OAuth 2.0 Form Post Response Mode
Proof Key for Code Exchange by OAuth Public Clients (
RFC7636
)
Support Passing a Request Object by Value (
Section 6.1 of OpenID Connect Core 1.0 incorporating errata set 1
)
Support signature algorithm
PS256
ES256
Support key encryption algorithm
RSA-OAEP
RSA-OAEP-256
ID Token as Detached Signature
Client Authentication
private_key_jwt (
Chapter 9 of OpenID Connect Core 1.0 incorporating errata set 1
)
tls_client_auth (
Section 2.1 of RFC8705
)
OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens (
RFC8705
)
Refresh Request (
Chapter 12 of of OpenID Connect Core 1.0 incorporating errata set 1
)
OAuth 2.0 Token Revocation (
RFC7009
)
Specs of Resource Server
TLS
Client Authentication
tls_client_auth (
Section 2.1 of RFC8705
)
OAuth 2.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens (
RFC8705
)
Token Introspection (
RFC7662
)
Requirements
Java 11
Apache Maven 3.6
How to run client and resource server
client
$
cd
client
$ mvn spring-boot:run
resource server
$
cd
server
$ mvn spring-boot:run
Precautions
This code is provided "as is" without warranty of any kind.
We don't take responsibility for any damage by using this sample source code.
License
Apache License, Version 2.0
About
No description, website, or topics provided.
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
12
stars
Watchers
1
watching
Forks
0
forks
Report repository
Releases
No releases published
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
Java
88.1%
HTML
10.2%
Makefile
1.7%