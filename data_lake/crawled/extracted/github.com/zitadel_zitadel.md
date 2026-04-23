---
{
  "title": "GitHub - zitadel/zitadel: ZITADEL - Identity infrastructure, simplified for you. · GitHub",
  "url": "https://github.com/zitadel/zitadel",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 7318,
  "crawled_at": "2026-04-23T21:01:20"
}
---

zitadel
/
zitadel
Public
Notifications
You must be signed in to change notification settings
Fork
1k
Star
13.6k
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
4,453 Commits
4,453 Commits
.codecov
.codecov
.devcontainer
.devcontainer
.github
.github
apps
apps
backend
backend
benchmark
benchmark
cmd
cmd
console
console
deploy/
compose
deploy/
compose
internal
internal
openapi
openapi
packages
packages
pkg
pkg
proto
proto
statik
statik
tests/
functional-ui
tests/
functional-ui
.cursorrules
.cursorrules
.gitattributes
.gitattributes
.gitignore
.gitignore
.golangci.yaml
.golangci.yaml
.npmrc
.npmrc
.nvmrc
.nvmrc
.nxignore
.nxignore
.releaserc.js
.releaserc.js
ADOPTERS.md
ADOPTERS.md
AGENTS.md
AGENTS.md
API_DESIGN.md
API_DESIGN.md
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
CONTRIBUTING.md
CONTRIBUTING.md
LICENSE
LICENSE
LICENSING.md
LICENSING.md
MEETING_SCHEDULE.md
MEETING_SCHEDULE.md
README.md
README.md
SECURITY.md
SECURITY.md
TERMINOLOGY.md
TERMINOLOGY.md
buf.gen.yaml
buf.gen.yaml
buf.work.yaml
buf.work.yaml
changelog.config.js
changelog.config.js
go.mod
go.mod
go.sum
go.sum
main.go
main.go
nx.json
nx.json
package.json
package.json
pnpm-lock.yaml
pnpm-lock.yaml
pnpm-workspace.yaml
pnpm-workspace.yaml
project.json
project.json
View all files
Repository files navigation
The Identity Infrastructure for Developers
ZITADEL
is an open-source identity and access management platform built for teams that need more than basic auth. Whether you're securing a SaaS product, building a B2B platform, or self-hosting a production IAM stack — ZITADEL gives you everything out of the box: SSO, MFA, Passkeys, OIDC, SAML, SCIM, and a battle-tested multi-tenancy model.
No vendor lock-in. No compromise on control. Just a robust, API-first identity platform you can own.
🏡 Website
|
💬 Chat
|
📋 Docs
|
🧑‍💻 Blog
|
📞 Contact
Why ZITADEL
We built ZITADEL to handle the hardest IAM challenges at scale — starting with multi-tenancy.
ZITADEL
FusionAuth
Keycloak
Auth0/Okta
Open-source
✅
❌
✅
❌
Self-hostable
✅
✅
✅
❌
Infrastructure-level tenants
✅ Instances (High scale)
✅ Tenants
🟡 Realms (Scaling limits)
❌ (Multi-tenant = multi-account)
B2B Organizations
✅ Native & Unlimited
🟡 via Entity Management
✅ (Recent addition)
🟡 (Plan/Account dependent)
Full audit trail
✅ Comprehensive Event Stream*
🟡 Audit logs
🟡 Audit logs
🟡 Audit logs
Passkeys (FIDO2)
✅
✅
✅
✅
Actions / webhooks
✅
✅
🟡 via SPI
✅
API-first (gRPC + REST)
✅
🟡 REST only
🟡 REST only
🟡 REST only
SaaS + self-host parity
✅
✅
➖ N/A
➖ N/A
ZITADEL Cloud and self-hosted ZITADEL run the same codebase.
Key differentiators for architects:
Relational core, event-driven soul
— every mutation is written as an immutable event for a complete, API-accessible
audit trail
. Unlike systems that log only select activities, ZITADEL provides a comprehensive event stream that can be audited or streamed to external systems via Webhooks.
Strict multi-tenant hierarchy
— Identity System → Organizations → Projects, with isolated data and policy scoping at multiple levels
API-first design
— every resource and action is available via
connectRPC, gRPC, and HTTP/JSON APIs
Zero-downtime updates
and
horizontal scalability
without external session stores
Get Started in 3 Minutes
👉
Quick Start Guide
ZITADEL Self-Hosted
#
Docker Compose — up and running in under 3 minutes
curl -LO https://raw.githubusercontent.com/zitadel/zitadel/main/deploy/compose/docker-compose.yml \
&&
curl -LO https://raw.githubusercontent.com/zitadel/zitadel/main/deploy/compose/.env.example \
&&
cp .env.example .env \
&&
docker compose up -d --wait
Full deployment guides:
Docker Compose
Kubernetes
Need professional support for your self-hosted deployment?
Contact us
.
ZITADEL Cloud (SaaS)
Start for free at
zitadel.com
— no credit card required. Available in US · EU · AU · CH.
Pay-as-you-go pricing
.
Integrate with the V2 API
ZITADEL exposes every capability over a typed API. Here's how to create a user with the V2 REST API:
curl -X POST https://
$ZITADEL_DOMAIN
/v2/users/human \
  -H
"
Authorization: Bearer
$ACCESS_TOKEN
"
\
  -H
"
Content-Type: application/json
"
\
  -d
'
{
"username": "alice@example.com",
"profile": { "givenName": "Alice", "familyName": "Smith" },
"email": { "email": "alice@example.com", "sendCode": {} }
}
'
Explore the full
API reference
— including connectRPC and gRPC transports — or jump straight to
quickstart examples
.
Features
Authentication
Single Sign On (SSO) · Username/Password ·
Passkeys (FIDO2 / WebAuthn)
MFA: OTP, U2F, OTP Email, OTP SMS
LDAP
·
Enterprise IdPs and social logins
OpenID Connect certified
·
SAML 2.0
·
Device authorization
Machine-to-machine
: JWT Profile, PAT, Client Credentials
Token exchange and impersonation
Custom sessions
for flows beyond OIDC/SAML
Hosted Login V2
Multi-Tenancy
Identity brokering
with pre-built IdP templates
Customizable B2B onboarding
with self-service for customers
Delegated role management
to third parties
Domain discovery
Integration
gRPC, connectRPC, and REST APIs
for every resource
Actions
: webhooks, custom code, token enrichment
RBAC
·
SCIM 2.0 Server
Audit log and SOC/SIEM integration
SDKs and example apps
Self-Service & Admin
Self-registration
with email/phone verification
Administration Console
for orgs and projects
Custom branding
per organization
Deployment
PostgreSQL
(≥ 14) ·
Zero-downtime updates
·
High scalability
Track upcoming features on our
roadmap
and follow our
changelog
for recent updates.
Showcase
Login V2
Our new, fully customizable login experience —
documentation
Adopters & Ecosystem
Used in production by organizations worldwide. See the full
Adopters list
— and add yours by submitting a pull request.
SDKs
:
All supported languages and frameworks
Examples
:
Clone and use our examples
How To Contribute
ZITADEL is built in the open and welcoming to contributions of all kinds.
📖 Read the
Contribution Guide
to get started
💬 Join the conversation on
Discord
🐛 Report bugs or request features via
GitHub Issues
Contributors
Made with
contrib.rocks
.
Security
Security policy:
SECURITY.md
Vulnerability Disclosure Policy
— how to responsibly report security issues.
Technical Advisories
are published for major issues that could impact security or stability in production.
License
AGPL-3.0
— see
LICENSING.md
for the full licensing policy, including Apache 2.0 and MIT exceptions for specific directories.
About
ZITADEL - Identity infrastructure, simplified for you.
zitadel.com
Topics
identity
saml
oauth2
authentication
login
authorization
sso
user
openid-connect
oidc
mfa
scim
multitenancy
2fa
fido2
passkeys
Resources
Readme
License
AGPL-3.0 license
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
13.6k
stars
Watchers
59
watching
Forks
1k
forks
Report repository
Releases
2,034
v4.13.1
Latest
Apr 1, 2026
+ 2,033 releases
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
75.8%
TypeScript
11.7%
MDX
7.0%
HTML
2.7%
SCSS
1.2%
CSS
0.8%
Other
0.8%