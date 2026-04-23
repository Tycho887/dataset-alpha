---
{
  "title": "GitHub - IdentityPython/oidc-op: An implementation of an OIDC Provider (OP) · GitHub",
  "url": "https://github.com/IdentityPython/oidc-op",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2601,
  "crawled_at": "2026-04-23T20:50:50"
}
---

This repository was archived by the owner on Jun 23, 2023. It is now read-only.
IdentityPython
/
oidc-op
Public archive
Notifications
You must be signed in to change notification settings
Fork
25
Star
67
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
603 Commits
603 Commits
.github
.github
docs
docs
example
example
src/
oidcop
src/
oidcop
tests
tests
.gitignore
.gitignore
.isort.cfg
.isort.cfg
.readthedocs.yml
.readthedocs.yml
LICENSE
LICENSE
README.md
README.md
pyproject.toml
pyproject.toml
requirements-dev.txt
requirements-dev.txt
requirements-docs.txt
requirements-docs.txt
requirements.txt
requirements.txt
setup.py
setup.py
View all files
Repository files navigation
oidc-op
This project is a Python implementation of an
OIDC Provider
on top of
jwtconnect.io
that shows to you how to 'build' an OP using the classes and functions provided by oidc-op.
If you want to add or replace functionality the official documentation should be able to tell you how.
If you are just going to build a standard OP you only have to understand how to write your configuration file.
In
example/
folder you'll find some complete examples based on flask and django.
Idpy OIDC-op implements the following standards:
OpenID Connect Core 1.0 incorporating errata set 1
Web Finger
OpenID Connect Discovery 1.0 incorporating errata set 1
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1
OpenID Connect Session Management 1.0
OpenID Connect Back-Channel Logout 1.0
OpenID Connect Front-Channel Logout 1.0
OAuth2 Token introspection
It also comes with the following
add_on
modules.
Custom scopes, that extends
OIDC standard ScopeClaims
Proof Key for Code Exchange by OAuth Public Clients (PKCE)
OAuth2 PAR
OAuth2 RAR
OAuth2 DPoP
OAuth 2.0 Authorization Server Issuer Identification
The entire project code is open sourced and therefore licensed under the
Apache 2.0
For any futher information please read the
Official Documentation
.
Certifications
Contribute
Join in
.
Authors
Roland Hedberg
About
An implementation of an OIDC Provider (OP)
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
67
stars
Watchers
4
watching
Forks
25
forks
Report repository
Releases
16
v2.4.3
Latest
May 13, 2022
+ 15 releases
Packages
0
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
Python
98.8%
Other
1.2%