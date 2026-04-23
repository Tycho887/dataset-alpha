---
{
  "title": "GitHub - italia/spid-cie-oidc-django: The SPID/CIE OIDC Federation SDK, written in Python · GitHub",
  "url": "https://github.com/italia/spid-cie-oidc-django",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 8802,
  "crawled_at": "2026-04-23T20:48:47"
}
---

italia
/
spid-cie-oidc-django
Public
Notifications
You must be signed in to change notification settings
Fork
36
Star
41
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
1,404 Commits
1,404 Commits
.github/
workflows
.github/
workflows
docs
docs
examples
examples
spid_cie_oidc
spid_cie_oidc
uwsgi_setup
uwsgi_setup
.coveragerc
.coveragerc
.flake8
.flake8
.gitignore
.gitignore
AUTHORS
AUTHORS
Dockerfile
Dockerfile
LICENSE
LICENSE
README.md
README.md
SECURITY.md
SECURITY.md
build_pypi.sh
build_pypi.sh
docker-compose.yml
docker-compose.yml
docker-prepare.sh
docker-prepare.sh
linting.sh
linting.sh
requirements-dev.txt
requirements-dev.txt
setup.py
setup.py
View all files
Repository files navigation
SPID/CIE OIDC Federation SDK
SPID/CIE OIDC Federation is a suite of Django applications designed to
make it easy to build an
Openid Connect Federation
,
each of these can be installed separately within a django project. These are the following:
Application
Description
spid_cie_oidc.accounts
Customizable application that extends the django User model.
spid_cie_oidc.entity
OpenID Connect Federation django app that implements OIDC Federation 1.0 Entity Statements, metadata discovery, Trust Chain, Trust Marks and Metadata policy. Technical specifications:
OIDC Federation Entity
spid_cie_oidc.authority
OpenID Connect Federation API and models for
OIDC Federation Trust Chain/Intermediate
,
Technical specifications
and
tutorial
.
spid_cie_oidc.onboarding
OpenID Connect Federation onboarding demo service
and tools
spid_cie_oidc.relying_party
OpenID Connect Relying Party
and test suite for OIDC Providers
spid_cie_oidc.provider
OpenID Connect Provider
and test suite for OIDC Relying Parties
Summary
Features
Setup
Docker
Usage
OpenAPI Schema 3
Tools
Contribute
Contribute as end user
Contribute as developer
Implementations notes
License and Authors
An onboarded Relying Party with a succesful authentication.
Setup
All the Django apps are available in the folder
spid_cie_oidc/
.
The examples projects are available in the folder
examples/
.
There is a substantial difference between an app and a project.
The app is installed using a common python package manager, such as
poetry
or
pip
,
and can be used, inherited, and integrated into other projects.
A project is a service configuration that integrates one or more applications.
In this repository we have three example projects:
federation_authority
relying_party
provider
Federation Authority loads all the applications for development needs, acting as both authority, SPID RP and SPID OP.
This allows us to make a demo by starting a single service. See admin page
http://127.0.0.1:8000/admin/
and user login page
http://127.0.0.1:8000/oidc/rp/landing/
.
Then we have also another Relying Party, as indipendent project, and another Provider configured with the CIE profile.
Relying party and Provider are examples that only integrate
spid_cie_oidc.entity
and
spid_cie_oidc.provider
or
.relying_party
as applications.
Read the
setup documentation
to get started.
Docker
Docker image
docker pull ghcr.io/italia/spid-cie-oidc-django:latest
Docker compose
Please do your customizations in each
settingslocal.py
files and/or in the example dumps json file.
Change hostnames from 127.0.0.1 to which one configured in the compose file, in the settingslocal.py files and in the dumps/example.json files.
In our example we rename:
http://127.0.0.1:8000
to
http://trust-anchor.org:8000/
http://127.0.0.1:8001
to
http://relying-party.org:8001/
http://127.0.0.1:8002
to
http://cie-provider.org:8002/
We can do that with the following steps:
Execute
bash docker-prepare.sh
Customize the example data and settings contained in
examples-docker/
if needed (not necessary for a quick demo)
Run the stack
sudo docker-compose up
Configure a proper DNS resolution for trust-anchor.org. In GNU/Linux we can configure it in
/etc/hosts
:
127.0.0.1   localhost  trust-anchor.org relying-party.org cie-provider.org wallet.trust-anchor.org
Point your web browser to
http://relying-party.org:8001/oidc/rp/landing
and do your first oidc authentication.
Usage
The demo proposes a small federation composed by the following entities:
Federation Authority, acts as trust anchor and onboarding system. It's available at
http://127.0.0.1:8000/
. It has also an embedded Spid provider and a embedded Relying Party available at
/oidc/rp/landing
.
OpenID Relying Party, available at
http://127.0.0.1:8001/
CIE OpenID Provider, available at
http://127.0.0.1:8002/
In the docker example we have only the Federation Authority with an embedded SPID OP and a RP.
Examples Users and Passwords:
admin
oidcadmin
user
oidcuser
OpenAPI Schema 3
Each application has an exportable OAS3 available at
/rest/schema.json
with a browsable reDoc UI at
/rest/api/docs
.
The reDoc OAS3 browsable page.
Tools
The OnBoarding app comes with the following collection of tools:
JWK
Create a jwk
Convert a private JWK to PEM
Convert a public JWK to PEM
Convert a private PEM to JWK
Convert a public PEM to JWK
JWT decode and verification
Federation
Resolve entity statement
Apply policy
Validators
Validate OP metadata spid
Validate OP metadata cie
Validate RP metadata spid
Validate RP metadata cie
Validate Authn Request spid
Validate Authn Request cie
Validate Entity Configuration
Trust mark validation
Schemas
Authorization Endpoint
Introspection Endpoint
Metadata
Token Endpoint
Revocation Endpoint
Jwt client Assertion
OIDC tools facilitates the lives of developers and service operators, here a simple interface to decode and verify a JWT.
To explore a federation on the commandline, use the
ofcli
tool. It can be used to export federation metadata to json files for further analysis.
Contribute
Your contribution is welcome, no question is useless and no answer is obvious, we need you.
Contribute as end user
Please open an issue if you've discoveerd a bug or if you want to ask some features.
Contribute as developer
Please open your Pull Requests on the
dev
branch.
Please consider the following branches:
main
: where we merge the code before tag a new stable release.
dev
: where we push our code during development.
other-custom-name
: where a new feature/contribution/bugfix will be handled, revisioned and then merged to dev branch.
Backup and share your demo data
# backup your data (upgrade example data), -e excludes.
./manage.py dumpdata -e admin -e spid_cie_oidc_relying_party -e spid_cie_oidc_provider -e spid_cie_oidc_relying_party_test -e auth -e contenttypes -e sessions --indent 2 > dumps/example.json
In this project we adopt
Semver
and
Conventional commits
specifications.
Implementation notes
All the operation related to JWT signature and encryption are built on top of
IdentityPython
cryptojwt
This project proposes an implementation of the italian OIDC Federation profile with
automatic_client_registration
and the adoption of the trust marks as mandatory.
If you're looking for a fully compliant implementation of OIDC Federation 1.0,
with a full support of explicit client registration, please look at idpy's
fedservice
.
General Features
SPID and CIE OpenID Connect Provider
SPID and CIE OpenID Connect Relying Party
OIDC Federation onboarding demo service
OIDC Federation 1.0
Trust Anchor and Intermediary
Automatic client registration
Entity profiles and Trust marks
Trust chain storage and discovery
Entity statement resolve endpoint
Fetch statement endpoing
List entities endpoint
Advanced List endpoint
Federation CLI
RP: build trust chains for all the available OPs
OP: build trust chains for all the available RPs
Multitenancy, a single service can configure many entities like RPs, OP, Trust Anchors and intermediaries
gettext compliant (i18n)
Bootstrap Italia Design templates
License and Authors
This software is released under the Apache 2 License by:
Giuseppe De Marco
gi.demarco@innovazione.gov.it
.
In this project we use the
metadata policy code
written by Roland Hedberg and licensed under the same Apache 2 license.
About
The SPID/CIE OIDC Federation SDK, written in Python
Topics
federation
cie
oidc-provider
oidc-client
spid
oidc-token-management
oidc-federation
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
41
stars
Watchers
3
watching
Forks
36
forks
Report repository
Releases
77
1.6.3
Latest
Mar 23, 2026
+ 76 releases
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
Python
85.9%
HTML
10.6%
CSS
1.8%
JavaScript
1.1%
Other
0.6%