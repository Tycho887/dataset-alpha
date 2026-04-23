---
{
  "title": "AB/Connect Working Group – Specifications - OpenID Foundation",
  "url": "https://openid.net/wg/connect/specifications",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6637,
  "crawled_at": "2026-04-23T21:01:01"
}
---

AB/Connect Working Group - Specifications
The AB/Connect working group is a combined working group of the Artifact Binding (AB) Working Group and the Connect Working Group aimed at producing the OAuth 2.0 based “OpenID Connect” specifications. It also includes a project named OpenID for Verifiable Credentials which consists of three specifications.
AB/Connect Working Group
OVERVIEW
AB/Connect Working Group
CHARTER
AB/Connect Working Group
SPECIFICATIONS
AB/Connect Working Group
REPOSITORIES
The working group has been developing the following specifications:
Final Specifications
OpenID Connect Relying Party Metadata Choices 1.0
– this specification extends the OpenID Connect Dynamic Client Registration 1.0 specification to enable RPs to express a set of supported values for some RP metadata parameters, rather than just single values.
OpenID Federation 1.0
– defines basic components to build multilateral federations. It also defines how to apply them in the contexts of OpenID Connect and OAuth 2.0. These components can be used by other application protocols for the purpose of establishing trust.
OpenID Connect Core
– Defines the core OpenID Connect functionality: authentication built on top of OAuth 2.0 and the use of claims to communicate information about the End-User
OpenID Connect Discovery
– Defines how clients dynamically discover information about OpenID Providers
OpenID Connect Dynamic Registration
– Defines how clients dynamically register with OpenID Providers
OAuth 2.0 Multiple Response Types
– Defines several specific new OAuth 2.0 response types
OAuth 2.0 Form Post Response Mode
– Defines how to return OAuth 2.0 Authorization Response parameters (including OpenID Connect Authentication Response parameters) using HTML form values that are auto-submitted by the User Agent using HTTP POST
OpenID 2.0 to OpenID Connect Migration 1.0
– Defines how to migrate from OpenID 2.0 to OpenID Connect
OpenID Connect RP-Initiated Logout
– Defines how a Relying Party requests that an OpenID Provider log out the End-User
Session Management
– Defines how to manage OpenID Connect sessions, including postMessage-based logout and RP-initiated logout functionality
Front-Channel Logout
– Defines a front-channel logout mechanism that does not use an OP iframe on RP pages
Back-Channel Logout
– Defines a logout mechanism that uses direct back-channel communication between the OP and RPs being logged out
OpenID Connect Core Error Code unmet_authentication_requirements
– Defines the unmet_authentication_requirements authentication response error code
Initiating User Registration via OpenID Connect
– Defines the prompt=create authentication request parameter
OpenID Federation 1.0
– Defines how parties within a federation can establish trust with one another
Implementer's Drafts
OpenID Connect Native SSO for Mobile Apps Second Implementer’s Draft
– describes a mechanism that allows a mobile app to share the identity/authentication obtained by a different mobile app where both apps are written by the same vendor and installed on the same physical device
Self-Issued OpenID Provider V2
– Enables End-users to use OpenID Providers (OPs) that they control
– Most recent
Implementer’s Draft
OpenID Connect Native SSO for Mobile Apps
– Enables native applications by the same vendor to share login information
– Most recent
Implementer’s Draft
Errata Corrections
OpenID Connect Core 1.0 Second Errata
– defines the core OpenID Connect functionality: authentication built on top of OAuth 2.0 and the use of Claims to communicate information about the End-User. It also describes the security and privacy considerations for using OpenID Connect.
OpenID Connect Discovery 1.0 Second Errata
– specification defines a mechanism for an OpenID Connect Relying Party to discover the End-User’s OpenID Provider and obtain information needed to interact with it, including its OAuth 2.0 endpoint locations
OpenID Connect Dynamic Client Registration 1.0 Second Errata
– defines how an OpenID Connect Relying Party can dynamically register with the End-User’s OpenID Provider, providing information about itself to the OpenID Provider, and obtaining information needed to use it, including the OAuth 2.0 Client ID for this Relying Party
OpenID Connect Back-Channel Logout 1.0 Second Errata
– defines a logout mechanism that uses direct back-channel communication between the OP and RPs being logged out; this differs from front-channel logout mechanisms, which communicate logout requests from the OP to RPs via the User Agent
Drafts
OpenID Connect Claims Aggregation
– Enables RPs to request and Claims Providers to return aggregated claims through OPs
OpenID Federation Extended Subordinate Listing
–
Extends OpenID Federation to facilitate listings of large numbers of subordinates
OpenID Federation for Wallet Architectures
–
Defines how to perform trust establishment for Wallet ecosystems with OpenID Federation
OpenID Connect Relying Party Metadata Choices
– E
nables RPs to express a set of supported values for RP metadata parameters
OpenID Provider Commands
– Complements OpenID Connect by introducing a set of Commands for an OP to directly manage an end-user Account at an RP
OpenID Connect Enterprise Extensions
– Specifies a number of common or desirable extensions to OpenID Connect
OpenID Connect Ephemeral Subject Identifier
– Specifies an ephemeral subject identifier type that prevents correlation of the subject identifier across multiple visits
OpenID Connect Key Binding
– Specifies how to bind a public key to an ID Token using mechanisms defined in OAuth 2.0 Demonstrating Proof of Possession (DPoP) [
RFC9449
].
OpenID Federation Subordinate Events Endpoint
– Specifies a mechanism for Trust Anchors and Intermediates to publish historical events related to their Immediate Subordinates
OpenID Federation 1.1
– Protocol-independent functionality enabling parties within a federation to establish trust with one another
OpenID Federation for OpenID Connect 1.1
– Protocol-specific functionality enabling parties using OpenID Connect or OAuth 2.0 within a federation to establish trust with one another
Resources
Implementer's Guides
Two implementer’s guides are also available to serve as self-contained references for implementers of basic Web-based Relying Parties:
Basic Client Implementer’s Guide
– Simple subset of the Core functionality for a web-based Relying Party using the OAuth code flow
Implicit Client Implementer’s Guide
– Simple subset of the Core functionality for a web-based Relying Party using the OAuth implicit flow
Repositories
Repositories and Rendered HTML Editor’s Drafts