---
{
  "title": "GitHub - italia/eudi-wallet-it-python: Python toolchain for building an OpenID4VP RP with a SATOSA backend compliant with the Italian Wallet implementation profile · GitHub",
  "url": "https://github.com/italia/eudi-wallet-it-python",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 8508,
  "crawled_at": "2026-04-23T20:56:02"
}
---

italia
/
eudi-wallet-it-python
Public
Notifications
You must be signed in to change notification settings
Fork
17
Star
26
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
1,721 Commits
1,721 Commits
.github/
workflows
.github/
workflows
docs
docs
example
example
integration_test
integration_test
pyeudiw
pyeudiw
.coveragerc
.coveragerc
.flake8
.flake8
.gitguardian.yaml
.gitguardian.yaml
.gitignore
.gitignore
LICENSE
LICENSE
README.md
README.md
build_docs.sh
build_docs.sh
build_pypi.sh
build_pypi.sh
html_linting.sh
html_linting.sh
linting.sh
linting.sh
pytest.ini
pytest.ini
requirements-dev.txt
requirements-dev.txt
run_tests.sh
run_tests.sh
setup.cfg
setup.cfg
setup.py
setup.py
View all files
Repository files navigation
eudi-wallet-it-python
The eID Wallet Python toolchain is a suite of Python libraries designed to
make it easy the implementation of an EUDI Wallet Relying Party according
to the
Italian Wallet implementation profile
.
The toolchain contains the following components:
Name
Description
jwk
JSON Web Key (JWK) according to
RFC7517
.
jwt
Signed and encrypted JSON Web Token (JWT) according to
RFC7519
,
RFC7515
and
RFC7516
tools.qrcode
QRCodes creation
oauth2.dpop
Tools for issuing and parsing DPoP artifacts, according to
OAuth 2.0 Demonstrating Proof-of-Possession at the Application Layer (DPoP)
federation
Trust evaluation mechanisms, according to
OpenID Federation 1.0
x509
Trust evaluation mechanism using X.509 PKI, according to
RFC5280
trust
trust handlers bringing multiple evaluation mechanisms
satosa.backend
SATOSA Relying Party backend, according to
OpenID for Verifiable Presentations
satosa.frontend
SATOSA Issuer frontend, according to
OpenID for Verifiable Credential Issuance
openid4vp
Classes and schemas related to
OpenID for Verifiable Presentations
openid4vci
Classes and schemas related to
OpenID for Verifiable Credential Issuance
sd_jwt
Issuance and verification of SD-JWT(-VC) according to
Selective Disclosure for JWTs (SD-JWT)
status_list
Credential revocation check mechanisms according to
Token Status List
Setup
Install enviroment and dependencies
sudo apt install python3-dev python3-pip git
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install virtualenv
Activate the environment. It's optional and up to you if you want to install
in a separate env or system wide
virtualenv -p python3 env
source env/bin/activate
Install using pip:
pip install pyeudiw
or
pip install pyeudiw[satosa]
for the satosa backend.
Install using github:
pip install git+https://github.com/italia/eudi-wallet-it-python
Optionally for generate the documentation you need to install the following packages:
pip install sphinx sphinx_rtd_theme
Documentation
The API documentation is available in the githubpages,
here
.
In the
docs/
folder there are some common example for some specific tasks.
Build the Documentation
For generate the documentation enter in the terminal the following commands.
The last argument is the exclude path, unit tests are then excluded from the API documentation.
cd docs
sphinx-apidoc -o ./source ../pyeudiw ../pyeudiw/tests
make html
Example project
The example project is a docker-compose that runs a demo composed by the following component:
Wordpress with SAML2 support and Bootstrap Italia template preregistered to the IAM Proxy.
Satosa-Saml2Spid
IAM Proxy with a preconfigured OpenID4VP backend.
Please read
this README
to get a fully working Wordpress setup with SAML2 support.
SatoSa configuration
SaToSa
is a general purpose IAM
proxy solution that allows interoperability between different entities that implements different
authentication protocols such as SAML2, OpenID Connect and OAuth2. This project offers:
a SaToSa backend to enable the OpenID4VP protocol;
a SaToSa frontend to enable the OpenID4VCI protocol.
There is a SaToSa distribution, created by the Developers Italia community, pre-configured to facilitate integration with the Italian National Digital Identity Systems,
it is
Satosa-Saml2Spid
.
Please refer to the dedicate README files for details on how to configure SaToSa with the respective components:
OpenID4VP Relying Party backend
;
OpenID4VCI Issuer fronted
.
Protocol Support Recap
Compliance checklist against the
Italian Wallet implementation profile
and related OpenID4VCI/OpenID4VP specifications.
OpenID4VCI (Credential Issuer Frontend)
🟢 Supported · 🟠 Partial · 🔴 Not supported
Feature
Status
Pushed Authorization Requests (PAR)
🟢
PAR: reject
request_uri
in request body (RFC 9126)
🟢
OAuth 2.0 Attestation-Based Client Authentication
🟢
PKCE
🟢
Authorization Code Flow
🟢
DPoP at Token endpoint
🟢
Immediate Issuance
🟢
JWT Proof of Possession (
openid4vci-proof+jwt
)
🟢
Nonce endpoint (
c_nonce
)
🟢
Credential Offer (by value and QR code)
🟢
Notification endpoint
🟢
SD-JWT VC credential format
🟢
mso_mdoc credential format
🟢
Refresh Token (DPoP-bound)
🟢
Batch Credential Issuance
🔴
Deferred Issuance Flow
🔴
OpenID4VP (Relying Party Backend)
🟢 Supported · 🟠 Partial · 🔴 Not supported
Feature
Status
DCQL (Duckle) query language
🟢
Same Device flow
🟢
Cross Device flow (QR code)
🟢
Request Object by reference (
request_uri
)
🟢
Request URI method GET
🟢
Request URI method POST (wallet metadata)
🟢
wallet_metadata
and
wallet_nonce
🟢
Response mode
direct_post.jwt
(encrypted)
🟢
Response mode
direct_post
🟢
vp_token
keyed by credential id
🟢
dc+sd-jwt
format
🟢
mso_mdoc
format
🟢
Status endpoint (session polling)
🟢
Trust evaluation (X.509 PKI, OpenID Federation)
🟢
Credential revocation (status list)
🟢
Custom URL schemes (
haip
, configurable)
🟢
transaction_data
/
transaction_data_hashes
🔴
Executing Tests Using Preexisting MongoDb Instances
Use the env variable
PYEUDIW_MONGO_TEST_AUTH_INLINE
so tests connect with credentials.
CI uses
PYEUDIW_MONGO_TEST_AUTH_INLINE=""
(MongoDB without auth). For local MongoDB with auth,
set it in
.env
(loaded by
./run_tests.sh
) or export it:
PYEUDIW_MONGO_TEST_AUTH_INLINE=satosa:thatpassword@ pytest pyeudiw -x
# or: echo 'PYEUDIW_MONGO_TEST_AUTH_INLINE=satosa:thatpassword@' >> .env && ./run_tests.sh
Contribute
Your contribution is welcome, no question is useless and no answer is obvious, we need you.
Contribute as end user
Please open an issue if you've found a bug or if you want to ask some features.
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
Executing Unit Tests
Once you have activate the virtualenv, further dependencies must be installed as show below.
pip install -r requirements-dev.txt
Therefore the unit tests can be executed as show below.
pytest pyeudiw -x
If you test pyeudiw on a development machine where also iam-proxy-italia is running with its mongodb and the same collection names,
you can run the test by passing the mon user and password in this way
PYEUDIW_MONGO_TEST_AUTH_INLINE="satosa:thatpassword@" pytest pyeudiw -x
Executing integration tests
iam-proxy-italia project must be configured and in execution.
Integrations tests checks bot hthe cross device flow and the same device flow.
The cross device flow requires
playwrite
to be installed.
cd examples/satosa/integration_tests

playwrite install

PYEUDIW_MONGO_TEST_AUTH_INLINE="satosa:thatpassword@" pytest pyeudiw -x
External Resources and Tools
EUDIW Ref Implementation VCI
EUDIW Ref Implementation RP
Authors
Giuseppe De Marco
Acknowledgments
Manuel Pacella
Manuel Ciofo
Thomas Chiozzi
Pasquale De Rose
Elisa Nicolussi Paolaz
Salvatore Laiso
Alessio Murru
Nicola Saitto
Sara Longobardi
About
Python toolchain for building an OpenID4VP RP with a SATOSA backend compliant with the Italian Wallet implementation profile
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
26
stars
Watchers
3
watching
Forks
17
forks
Report repository
Releases
19
2.2.0
Latest
Mar 11, 2026
+ 18 releases
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
58.0%
JavaScript
35.3%
PHP
3.6%
HTML
2.0%
Other
1.1%