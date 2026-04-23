---
{
  "title": "ipsie/CHARTER.md at main · openid/ipsie · GitHub",
  "url": "https://github.com/openid/ipsie/blob/main/CHARTER.md",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 4751,
  "crawled_at": "2026-04-23T20:53:04"
}
---

openid
/
ipsie
Public
Notifications
You must be signed in to change notification settings
Fork
13
Star
40
Files
Expand file tree
main
/
CHARTER.md
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
65 lines (46 loc) · 4.31 KB
main
/
CHARTER.md
Top
File metadata and controls
Preview
Code
Blame
65 lines (46 loc) · 4.31 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions
Working Group name
Interoperability Profiling for Secure Identity in the Enterprise (IPSIE) Work Group.
Purpose
The purpose of this working group is to develop interoperability and security profiles of existing specifications that enable secure identity management within the enterprise.
The current state of identity within an enterprise extends well beyond single-sign-on. Many aspects of enterprise identity are covered by specifications both within and outside the OpenID Foundation, such as OpenID Connect, Shared Signals Framework, OAuth, and SCIM. These specifications often enable a wide range of capabilities – in many cases these capabilities that go beyond the minimum requirements for enterprise identity management, and sometimes also include features that are not relevant in an enterprise context. Additionally, many of these specifications are frameworks and contain optionality to the point of two independent implementations not being guaranteed to be interoperable without further coordination.
This working group will develop profiles of existing specifications with the primary goal of achieving independent implementations being interoperable, while also prioritizing secure defaults within the specifications.
The initial problem space of the working group is focused around:
Single Sign-On
User Lifecycle Management
Entitlements
Risk Signal Sharing
Logout
Token Revocation
The working group may also address problems such as:
Discoverability of specific features within the above-mentioned capabilities
New user onboarding and account recovery
Discovering the applications used within an enterprise
Monitoring and provisioning application usage
Managing restrictions on application usage
Scope & Objectives
The scope of the working group includes:
Develop profiles of existing specifications with the goal of interoperability within the enterprise ecosystem.
Define an interoperability profile of OpenID Connect that meets the needs and security requirements of the enterprise.
Define an interoperability profile of Shared Signals Framework that enables sharing signals about threat detection and device posture.
Define an interoperability profile of SCIM that enables user account lifecycle and entitlements management.
Define an interoperability profile of logout specifications to enable an identity provider to revoke sessions and tokens of downstream applications.
Out of scope:
Developing new general-purpose specifications, technologies, or features is out of scope of this working group. Profiles are created by including or excluding parts of existing specifications.
If a pertinent problem space without an existing specification is identified, an effort will first be made to find an existing working group or standards body where development of the specification may be more appropriate. If none is found, consideration will be given to creating a new specification within this working group.
The working group will actively coordinate with the following working groups doing related work:
OpenID Connect
FAPI
iGov
Shared Signals
OAuth
SCIM
Proposed specifications
The initial proposed deliverable by the group is: Interoperability Profile for Secure Identity in the Enterprise (IPSIE) This specification will be divided into sections for each use case, with subsections for each specification that this profiles. The group may provide additional interoperability profile specifications that address the concerns of specific use cases or certain specifications that require interoperability profiles.
Anticipated audience or users
Identity Providers that serve an enterprise customer market SaaS apps that sell to enterprise customers, also known as Independent Software Vendors (ISVs) Developers of tools, libraries, and other resources in support of either of the previous two audiences
Language
English.
Method of work
Mailing list and telephone/internet conference calls combined with face-to-face (where needed) and information sharing/collaborative working via online tools.
Basis for determining when the work is completed
Approved “final” specifications consistent with the purpose and scope that have been through the OpenID Foundation process including vote by the membership and running code in one or more proof-of-concept, interoperability event, or commercial projects.