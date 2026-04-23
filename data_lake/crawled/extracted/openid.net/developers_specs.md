---
{
  "title": "Explore All Specifications - OpenID Foundation",
  "url": "https://openid.net/developers/specs",
  "domain": "openid.net",
  "depth": 0,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 19987,
  "crawled_at": "2026-04-23T20:47:24"
}
---

What are OpenID Specifications
OpenID specifications are developed by working groups in three phases: Drafts, Implementer’s Drafts, and Final Specifications. Implementer’s Drafts and Final Specifications provide intellectual property protections to implementers. Final Specifications are OpenID Foundation standards.
Final Specifications
AB/Connect Working Group Specifications
OpenID Connect Relying Party Metadata Choices 1.0
– this specification extends the OpenID Connect Dynamic Client Registration 1.0 specification to enable RPs to express a set of supported values for some RP metadata parameters, rather than just single values.
OpenID Federation 1.0
– defines basic components to build multilateral federations. It also defines how to apply them in the contexts of OpenID Connect and OAuth 2.0. These components can be used by other application protocols for the purpose of establishing trust.
OpenID Connect Core
– Defines the core OpenID Connect functionality: authentication built on top of OAuth 2.0 and the use of claims to communicate information about the End-User
OpenID Connect Discovery
– Defines how clients dynamically discover information about OpenID Providers
OpenID Connect Dynamic Client Registration
– Defines how clients dynamically register with OpenID Providers
OAuth 2.0 Multiple Response Types
– Defines several specific new OAuth 2.0 response types
OAuth 2.0 Form Post Response Mode
– Defines how to return OAuth 2.0 Authorization Response parameters (including OpenID Connect Authentication Response parameters) using HTML form values that are auto-submitted by the User-Agent using HTTP POST
OpenID 2.0 to OpenID Connect Migration 1.0
– Defines how to migrate from OpenID 2.0 to OpenID Connect
OpenID Connect RP-Initiated Logout
– Defines how a Relying Party requests that an OpenID Provider log out the End-User
OpenID Connect Session Management
– Defines how to manage OpenID Connect sessions, including postMessage-based logout functionality
OpenID Connect Front-Channel Logout
– Defines a front-channel logout mechanism that does not use an OP iframe on RP pages
OpenID Connect Back-Channel Logout
– Defines a logout mechanism that uses direct back-channel communication between the OP and RPs being logged out
OpenID Connect Core Error Code unmet_authentication_requirements
– Defines the unmet_authentication_requirements authentication response error code
Initiating User Registration via OpenID Connect
– Defines the prompt=create authentication request parameter
OpenID Federation
– Defines how parties within a federation can establish trust with one another
AuthZEN Working Group Specifications
Authorization API 1.0 Final Specification
– the Authorization API enables Policy Decision Points (PDPs) and Policy Enforcement Points (PEPs) to communicate authorization requests and decisions to each other without requiring knowledge of each other’s inner workings
Digital Credentials Protocols (DCP) Working Group Specifications
OpenID for Verifiable Credential Issuance
– defines an OAuth-protected API for the issuance of Verifiable Credentials. Credentials can be of any format, including, but not limited to, IETF SD-JWT VC [
I-D.ietf-oauth-sd-jwt-vc
], ISO mdoc [
ISO.18013-5
], and W3C VCDM [
VC_DATA
].
OpenID for Verifiable Presentations 1.0
– defines a mechanism on top of OAuth 2.0 [
RFC6749
] for requesting and delivering Presentations of Credentials. Credentials and Presentations can be of any format, including, but not limited to W3C Verifiable Credentials Data Model [
VC_DATA
], ISO mdoc [
ISO.18013-5
], and IETF SD-JWT VC [
I-D.ietf-oauth-sd-jwt-vc
].
OpenID4VC High Assurance Interoperability Profile (HAIP)
– defines a profile of OpenID for Verifiable Credentials in combination with the credential formats IETF SD-JWT VC [
I-D.ietf-oauth-sd-jwt-vc
] and ISO mdoc [
ISO.18013-5
]. The aim is to select features and to define a set of requirements for the existing specifications to enable interoperability among Issuers, Wallets, and Verifiers of Credentials where a high level of security and privacy is required. The profiled specifications include OpenID for Verifiable Credential Issuance [
OIDF.OID4VCI
], OpenID for Verifiable Presentations [
OIDF.OID4VP
], IETF SD-JWT VC [
I-D.ietf-oauth-sd-jwt-vc
], and ISO mdoc [
ISO.18013-5
].
EAP Working Group Specifications
EAP ACR Values
– Enables OpenID Connect RPs to request that specific authentication context classes be applied to authentications performed and for OPs to inform RPs whether these requests were satisfied
eKYC and Identity Assurance Working Group Specifications
OpenID Identity Assurance Schema Definition 1.0
– defines a payload schema that can be used to describe a wide variety of identity assurance metadata about a number of claims that have been assessed as meeting a given assurance level
OpenID Connect for Identity Assurance Claims Registration 1.0
– specification defines an extension of OpenID Connect that registers new JWT claims about end-users. This extension defines new claims relating to the identity of a natural person that were originally defined within earlier drafts of OpenID Connect for Identity Assurance.
OpenID Connect for Identity Assurance 1.0
– defines an extension of OpenID Connect protocol for providing relying parties with claims about end-users that have a certain level of verification and/or additional metadata about the claim or the process of verification for access control, entitlement decisions or input to further verification processes
FAPI Working Group Specifications
FAPI 2.0 Message Signing
–
An API security profile for signing and verifying certain FAPI 2.0 Security Profile [
FAPI2_Security_Profile
] based requests and responses.
FAPI 2.0 Security Profile
–
A secured OAuth profile that aims to provide specific implementation guidelines for security and interoperability. Formally verified under FAPI 2.0 Attacker Model.
FAPI 2.0 Attacker Model
– An
attacker model that informs the decisions on security mechanisms employed by the FAPI security profiles.
Financial-grade API Security Profile (FAPI) 1.0 – Part 1: Baseline
– A secured OAuth profile that aims to provide specific implementation guidelines for security and interoperability.
Financial-grade API Security Profile (FAPI) 1.0 – Part 2: Advanced
– A highly secured OAuth profile that aims to provide specific implementation guidelines for security and interoperability.
JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
– This specification was created to bring some of the security features defined as part of OpenID Connect to OAuth 2.0
MODRNA Working Group Specifications
OpenID Connect Client Initiated Backchannel Authentication Flow – Core
(replacing
OpenID Connect Backchannel Authentication
) –
OpenID Connect Client Initiated Backchannel Authentication Flow is an authentication flow like OpenID Connect. However, unlike OpenID Connect, there is direct Relying Party to OpenID Provider communication without redirects through the user’s browser. This specification has the concept of a Consumption Device (on which the user interacts with the Relying Party) and an Authentication Device (on which the user authenticates with the OpenID Provider and grants consent). This specification allows a Relying Party that has an identifier for a user to obtain tokens from the OpenID Provider. The user starts the flow with the Relying Party at the Consumption Device, but authenticates and grants consent on the Authentication Device.
Shared Signals Working Group Specifications
OpenID Shared Signals and Events Framework Specification 1.0
– This Shared Signals and Events (SSE) Framework enables sharing of signals and events between cooperating peers. It enables multiple applications such as Risk Incident Sharing and Coordination (RISC) and the Continuous Access Evaluation Profile (CAEP)
OpenID Continuous Access Evaluation Profile 1.0
– Defines the Continuous Access Evaluation Profile (CAEP) of the
Shared Signals Framework
.  It specifies a set of event types conforming to the Shared Signals Framework. These event types are intended to be used between cooperating Transmitters and Receivers such that Transmitters may send continuous updates using which Receivers can attenuate access to shared human or robotic users, devices, sessions and applications.
OpenID RISC Profile Specification 1.0
– Defines the Risk Incident Sharing and Coordination (RISC) Event Types based on the
Shared Signals Framework
. Event Types are introduced and defined in
Security Event Token (SET)
.
Active Drafts
AB/Connect Working Group Specifications
See the
OpenID Connect Working Group Specifications
page
AuthZEN Working Group Specifications
See the
AuthZEN Working Group Specifications
page
Digital Credentials Protocols (DCP) Working Group Specifications
See the
DCP Working Group Specifications
page
eKYC & IDA Working Group Specifications
See the
eKYC & IDA Working Group Specifications
page
FAPI Working Group Specifications
See the
FAPI Working Group Specifications
page
iGov Working Group Specifications
See the
iGov Working Group Specifications
page
MODRNA Working Group Specifications
See the
MODRNA Working Group Specifications
page
Shared Signals Working Group Specifications
See the
Shared Signals Working Group Specifications
page
Implementer's Drafts
AB/Connect Working Group Specifications
OpenID Connect Native SSO for Mobile Apps Second Implementer’s Draft
– describes a mechanism that allows a mobile app to share the identity/authentication obtained by a different mobile app where both apps are written by the same vendor and installed on the same physical device
Self-Issued OpenID Provider V2
– enables End-users to use OpenID Providers (OPs) that they control
– most recent
Implementer’s Draft
OpenID Connect Native SSO for Mobile Apps
– Enables native applications by the same vendor to share login information
– Most recent
Implementer’s Draft
AuthZEN Working Group Specifications
AuthZEN 1.0
– Defines the API for a Policy Enforcement Point requesting an authorization decision from a Policy Decision Point
Digital Credentials Protocols (DCP) Working Group Specifications
OpenID for Verifiable Credential Issuance (OpenID4VCI)
– Defines an API and corresponding OAuth-based authorization mechanisms for issuance of Verifiable Credentials
– Most recent
Implementer’s Draft
EAP Working Group Specifications
Token Bound Authentication
– defines how to apply Token Binding to OpenID Connect ID Tokens
– Most recent
Implementer’s Draft
eKYC-IDA Working Group Specifications
OpenID Connect for Identity Assurance 1.0.
– Defines an extension to
OpenID Connect
for providing Relying Parties with identity information, i.e., Verified Claims, along with an explicit statement about the verification status of these Claims (what, how, when, according to what rules, using what evidence).
– Most recent
Implementer’s Draft
FAPI Working Group Specifications
Financial-grade API: Client Initiated Backchannel Authentication Profile
– FAPI CIBA is a profile of the OpenID Connect’s CIBA specification that supports the decoupled flow
– Most recent
Implementer’s Draft
Grant Management for OAuth 2.0
– This profile specifies a standards based approach to managing “grants” that represent the consent a data subject has given. It was born out of experience with the roll out of PSD2 and requirements in Australia.
– Most recent
Implementer’s Draft
FastFed Working Group Specifications
FastFed Core 1.0
– FastFed simplifies the administrative effort to configure identity federation between an identity provider and a hosted application. The specification defines metadata documents, APIs, and flows to enable an administrator to quickly connect two providers that support common standards such as OpenID Connect, SAML, and SCIM, and allows configuration changes to be communicated directly between the identity provider and hosted application on a recurring basis.
– Most recent
Implementer’s Draft
FastFed 1.0 SAML Profile
– This specification defines the requirements to implement the FastFed Enterprise SAML Profile.
– Most recent
Implementer’s Draft
FastFed 1.0 SCIM Profile
– This specification defines the requirements to implement the FastFed Profile for SCIM 2.0 Enterprise provisioning. This profile supports continual provisioning, update, and deprovisioning of end-users between the Identity Provider and Application Provider.
– Most recent
Implementer’s Draft
HEART Working Group Specifications
Health Relationship Trust Profile for OAuth 2.0
– This specification profiles the OAuth 2.0 protocol framework to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) the healthcare domain.
– Most recent
Implementer’s Draft
Health Relationship Trust Profile for Fast Healthcare Interoperability Resources (FHIR) OAuth 2.0 Scopes
– This specification profiles the OAuth 2.0 protocol scopes to be used with the FHIR protocol to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) the healthcare domain.
– Most recent
Implementer’s Draft
Health Relationship Trust Profile for User-Managed Access 2.0
– This specification profiles the UMA protocol to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) the healthcare domain.
– Most recent
Implementer’s Draft
Health Relationship Trust Profile for Fast Healthcare Interoperability Resources (FHIR) UMA 2 Resources
– This specification profiles the resource types and claim types to be used with the FHIR protocol to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) the healthcare domain.
– Most recent
Implementer’s Draft
iGov Working Group Specifications
International Government Assurance Profile (iGov) for OAuth 2.0
– Profiles the OAuth 2.0 protocol framework to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable, but not limited to consumer-to-government deployments
– Most recent
Implementer’s Draft
International Government Assurance Profile (iGov) for OpenID Connect 1.0
– Profiles the OpenID Connect protocol to increase baseline security, provide greater interoperability, and structure deployments in a manner specifically applicable to (but not limited to) government and public service domains
– Most recent
Implementer’s Draft
MODRNA Working Group Specifications
OpenID Connect MODRNA Authentication Profile
– RPs are keen to use high quality authentication methods, which can be provided by Mobile Network Operators (MNO). However a RP must be able to describe its demands for an authentication request and it must be able to do this in an interoperable way. The MODRNA Authentication Profile will specify how RP’s request a certain level of assurance for the authentication. In addition, the profile will specify an encrypted login hint token to allow for the transport of user identifiers to the OP in a privacy preserving fashion. Lastly, the profile will specify an additional message parameter intended to serve as an interlock between the user’s consumption device and authentication device.
– Most recent
Implementer’s Draft
OpenID Connect Account Porting
– This specification defines mechanisms to support a user porting from one OpenID Connect Provider to another, such that relying parties can automatically recognize and verify the change.
– Most recent
Implementer’s Draft
OpenID Connect User Questioning API
– This specification defines an API offered by an OpenID Provider (OP) that can be used by an application to send a question to a user of the OP. The user does not need to be interacting with the application when the question is asked. The user’s answer is returned asynchronously, digitally-signed by the OP.
– Most recent
Implementer’s Draft
Shared Signals Working Group Specifications
OpenID Shared Signals Framework Specification 1.0
– This Shared Signals Framework enables sharing of signals and events between cooperating peers. It enables multiple applications such as Risk Incident Sharing and Coordination (RISC) and the Continuous Access Evaluation Profile (
[CAEP]
)
– Most recent
Implementer’s Draft
OpenID Continuous Access Evaluation Profile 1.0
– Defines the Continuous Access Evaluation Profile (CAEP) of the Shared Signals Framework
[SSE-FRAMEWORK]
. It specifies a set of event types conforming to the Shared Signals Framework. These event types are intended to be used between cooperating Transmitters and Receivers such that Transmitters may send continuous updates using which Receivers can attenuate access to shared human or robotic users, devices, sessions and applications.
– Most recent
Implementer’s Draft
OpenID RISC Profile Specification 1.0
– Defines the Risk Incident Sharing and Coordination (RISC) Event Types based on the
Shared Signals Framework
. Event Types are introduced and defined in
Security Event Token (SET)
.
– Most recent
Implementer’s Draft
CAEP Interoperability Profile
Inactive Drafts
Account Chooser & Open YOLO working group specifications
Account Chooser 1.0
Native Applications working group specifications
Native Applications Agent Core 1.0
Native Applications Agent API Bindings 1.0
Errata Corrections
AB/Connect Working Group Specifications
OpenID Connect Core 1.0 Second Errata
– defines the core OpenID Connect functionality: authentication built on top of OAuth 2.0 and the use of Claims to communicate information about the End-User. It also describes the security and privacy considerations for using OpenID Connect.
OpenID Connect Discovery 1.0 Second Errata
– specification defines a mechanism for an OpenID Connect Relying Party to discover the End-User’s OpenID Provider and obtain information needed to interact with it, including its OAuth 2.0 endpoint locations
OpenID Connect Dynamic Client Registration 1.0 Second Errata
– defines how an OpenID Connect Relying Party can dynamically register with the End-User’s OpenID Provider, providing information about itself to the OpenID Provider, and obtaining information needed to use it, including the OAuth 2.0 Client ID for this Relying Party
OpenID Connect Back-Channel Logout 1.0 Second Errata
– defines a logout mechanism that uses direct back-channel communication between the OP and RPs being logged out; this differs from front-channel logout mechanisms, which communicate logout requests from the OP to RPs via the User Agent
FAPI Working Group Specifications
Errata Corrections to JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
– defines a new JWT-based mode to encode OAuth authorization responses. Clients are enabled to request the transmission of the authorization response parameters along with additional data in JWT format. This mechanism enhances the security of the standard authorization response with support for signing and optional encryption of the response. A signed response provides message integrity, sender authentication, audience restriction, and protection from mix-up attacks. Encrypting the response provides confidentiality of the response parameter values. The JWT authorization response mode can be used in conjunction with any response type.
Obsolete Drafts
Early OpenID specifications
OpenID Authentication 1.1
(
txt
)
OpenID Authentication 1.1 (original format)
OpenID Authentication 1.0 (original format)
Final OpenID 2.0 specifications
OpenID Authentication 2.0
(
txt
)
OpenID Attribute Exchange 1.0
(
txt
)
OpenID Provider Authentication Policy Extension 1.0
(
txt
)
OpenID Simple Registration Extension 1.0
(
txt
)
Yadis Discovery Protocol
(Developed separately from OpenID, though used in OpenID 2.0)
OpenID 2.0 Drafts
OpenID Simple Registration Extension 1.1 – Draft 1
(
txt
)
Contract Exchange 1.0