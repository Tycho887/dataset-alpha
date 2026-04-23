---
{
  "title": "FAPI Working Group - OpenID Foundation",
  "url": "https://openid.net/wg/fapi",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 18152,
  "crawled_at": "2026-04-23T20:55:11"
}
---

FAPI Working Group - Overview
FAPI is a general-purpose high-security API protection profile over OAuth. It has been adopted as a nationwide standard in many countries. FAPI WG is currently working on FAPI 2.0 suite of specifications.
FAPI Working Group
OVERVIEW
FAPI
Working Group
CHARTER
FAPI
Working Group
SPECIFICATIONS
FAPI
Working Group
REPOSITORY
WG News
FAPI 2.0 is now approved as FINAL specification (2025-02-19)
FAPI 2.0 Security Profile
–
A secured OAuth profile that aims to provide specific implementation guidelines for security and interoperability. Formally verified under FAPI 2.0 Attacker Model.
FAPI 2.0 Attacker Model
– An
attacker model that informs the decisions on security mechanisms employed by the FAPI security profiles.
Papers and Presentations
“Open Banking, Open Data, and the Financial Grade API,” March 2022
A primer for markets looking at enabling Open Banking and Open Data, covering the origins of “user-consent” based data sharing, global adoption, key standards, implementation considerations, and application across industry verticals.
“Open Banking and Open Data: Ready to Cross Borders?”, July 2022, working draft
The whitepaper offers an overview of the global open data landscape and makes a hypothesis that the next stage of open data development will be focused on global interoperability.
“Financial-grade API (FAPI) Profiles”, July 2022
This paper provides a comparison of available FAPI profiles and recommendations for new markets looking to implement FAPI as their security profile.
Overview of the FAPI Profiles
April 20, 2021
Meeting Notes
FAPI Meeting Notes 2025
FAPI Meeting Notes 2024
FAPI Meeting Notes 2023
FAPI Meeting Notes 2022
FAPI Meeting Notes 2021
FAPI Meeting Notes 2020
FAPI Meeting Notes 2019
FAPI Meeting Notes 2018
FAPI Meeting Notes 2017
FAPI Meeting Notes 2016
Working Group Chairs
Nat Sakimura (NAT Consulting)
Anoop Saxena (Intuit)
Anthony Nadalin
Dave Tonge (Moneyhub)
Dima Postnikov
The chairs can be reached at
openid-specs-fapi-owner@lists.openid.net
Participation
To monitor progress and connect with working group members, join the
mailing list
.
To participate in or contribute to a specification within the working group requires the submission of an Intellectual Property Rights (IPR) contribution agreement.  You can complete this electronically or by paper at
openid.net/intellectual-property
.
Be sure to specify, in the working groups box, the exact name:
Meeting Schedule
Regular Meetings
Pacific zone call: Bi-weekly Thursday Call @ 11pm UTC
Atlantic zone call: Weekly Wednesday Call @ 2pm UTC
Zoom software is available on Mac, PC, iPhone, and Android Phone.
Join Meeting
Meeting Minutes
View Calendar
Frequently asked Questions
What is the FAPI Working Group?
The FAPI Working Group is a working group at the OpenID Foundation. FAPI was previously known as the Financial-grade API but there was consensus within the working group to update the name to just FAPI to reflect that the specification is appropriate for many high-value use-cases requiring a more secure model beyond just financial services.
The group has expert members from the Identity and Access Management sector. The working group was initially formed to help develop security profiles and API standards for financial APIs. Over time the group has focussed its efforts on security profiles that while applicable for financial APIs, can be used in other industries and ecosystems.
The security profiles developed by the working group are based on the OAuth 2.0 and OpenID Connect suite of standards. OAuth 2.0 is an authorization framework which can be used for both low and high value operations. The standards produced by the FAPI WG contain much less optionality than the general OAuth 2.0 framework and require implementers to use modern security best practices.
The major benefits of the FAPI specifications are:
Clear point-by-point specifications that implementers can use as a “check list”
Exhaustive conformance tests to allow implementers to ensure their software is secure and interoperable
Standards based approach to securing complex interactions (e.g. decoupled authZ flows via CIBA, grant management, pushed request objects).
The FAPI WG does not work on data models or standards for financial or other APIs. These are ecosystem specific.
What are the differences between the FAPI RW Implementers Draft 2 and FAPI 1.0 Advanced Final?
Please reference the normative changes documentation:
https://bitbucket.org/openid/fapi/src/master/FAPI_1.0/changes-between-id2-and-final.md
What are the differences between FAPI 1.0 and FAPI 2.0?
FAPI 2.0 has a broader scope than FAPI 1.0. It aims for complete interoperability at the interface between client and authorization server as well as interoperable security mechanisms at the interface between client and resource server.
As a consequence, FAPI 2.0 provides mechanisms for obtaining fine-grained and transactional authorization for API access and security mechanisms for replay detection and non-repudiation on both interfaces in addition to the mechanisms already defined in FAPI 1.0 focusing on the security of the authorization flow.
The working group also evolved the profile to be easier to use for developers based on the results of an analysis of various open banking implementations, the recommendations of the latest OAuth Security BCP, and a comprehensive security threat model.
Both FAPI 1.0 as well as FAPI 2.0 define two compliance levels, but the FAPI 2.0 levels are aligned with different protection levels (baseline vs advanced) rather than API access modes (read vs read-write) in FAPI 1.0. The baseline level aims to be secure against all threats captured in the security threat model, the advanced level adds non-repudiation.
What are the advantages of FAPI 2.0?
FAPI 2.0 provides a higher degree of interoperability and is easier to use while maintaining a comparable security level. FAPI 2.0 aims at on-the-wire compatibility between compliant implementations and to this end removes optional and alternative features.
What is the current status of the FAPI 2.0 specifications?
The specifications are under development and are currently in ‘draft’ status.
The OpenID Foundation process for specification development is involves publishing one (or more) Implementers Drafts that have public review periods and are approved by the membership, then another review period / vote for ‘Final’ status.
For FAPI 1.0, the dates were:
First Implementers Draft: July 2017
Second Implementers Draft: October 2018
Conformance testing launched: April 2019
Final: March 2021
The working group intends to move FAPI 2.0 forward at a faster pace.
How can I suggest improvements to the FAPI 2.0 specifications?
You are very welcome to join the working group and propose changes.
Anyone can join the WG and contribute to the specifications after the submission of an IPR Agreement.
Are there conformance/certification tests for FAPI 2.0?
FAPI 2.0 conformance tests were launched in March 2023. The first set of FAPI 2.0 self-certifications have been published and can now be viewed on the
Certification Listings
.
We congratulate Authlete, Cloudentity, ConnectID, Ping Identity, and Raidiam for achieving compliance with the current FAPI 2.0 certifications and for being thought leaders on the leading edge of this important work. We are grateful to ConnectID in Australia who adopted FAPI 2.0 for their ecosystem and funded the FAPI 2.0 conformance test suite development.
Which versions of FAPI are implemented (live) and where?
Here are some examples of ecosystems that have implemented FAPI 1.0:
Open Banking, UK
Consumer Data Rights, Australia
yes® QES Scheme
Specifications available at
https://standards.openbanking.org.uk/
https://consumerdatastandardsaustralia.github.io/standards/
https://yes.com/docs/qes/2.5/index.html
Date
2018-01-13
2020-07-01
2020-09-24
Version
FAPI 1.0
FAPI 1.0
FAPI 2.0
The
Financial Data Exchange
is also working closely with the FAPI WG to implement the specs in North America.
Here is a list of FAPI 1.0 certified implementations:
https://openid.net/certification
Are there FAPI 2.0 implementations?
FAPI 2.0 as an OAuth profile utilizes OAuth features and extensions that are available in existing implementations or can be implemented on top of existing implementations.
In detail:
PKCE –
https://tools.ietf.org/html/rfc7636
This security mechanism is already widely supported by vendors.
mTLS –
https://datatracker.ietf.org/doc/rfc8705/
A standard for client authentication and sender-constraining of access tokens that is also recommended by the OAuth Security BCP.
DPoP –
https://tools.ietf.org/html/draft-ietf-oauth-dpop-02
A standard for sender-constraining access tokens at the application layer
Pushed Authorization Requests –
https://tools.ietf.org/html/draft-ietf-oauth-par
IETF specification awaiting publication
Wide adoption by open source projects and commercial vendors
Rich Authorization Requests (RAR) –
https://tools.ietf.org/html/draft-ietf-oauth-rar
RAR can be implemented on top of OAuth 2.0 implementations as an extension parameter. Existing implementations demonstrate the feasibility.
Authorization Server Issuer Identifier in Authorization Response
https://tools.ietf.org/html/draft-ietf-oauth-iss-auth-resp
Can be implemented on top of existing OAuth 2.0 implementations.
The working group has been informed that the following organisations have implemented FAPI 2:
yes QES Scheme Signing API (implemented by three different authorization servers), uses PKCE, mTLS, PAR, RAR, iss authorization response parameter
Authlete: Supports PKCE, mTLS, PAR, RAR and the iss response parameter.
The working group is not endorsing these organisations or their products, we are simply reporting information that we have received.
Is FAPI 2.0 backwards compatible with FAPI 1.0?
There are similarities between FAPI 1.0 and FAPI 2.0 (e.g., response type code + PKCE in FAPI 1.0/read and FAPI 2.0/baseline) but the scope is different so there is no full backwards compatibility.
Is FAPI 2.0 more secure than FAPI 1.0?
The reason for work on the 2.0 draft is not a more secure specification than 1.0, but rather FAPI 2.0 aims to be:
simpler to implement (less requirement on message signing without reducing security),
more interoperable (through reduced optionality),
closer aligned to the OAuth Security BCP,
wider in scope – covering fine grained and transactional authorization, which was out of scope of FAPI 1.0.
Regarding security, FAPI 1.0 has been analyzed using an in-depth formal analysis. FAPI 2.0 provides a more clearly defined attacker model with the aim to make the standard easier amenable to this kind of analysis and to make the security-related decisions in the specification more transparent.
It is worth noting that FAPI 2.0 Baseline aims to protect against a similar attacker model as FAPI 1.0 Advanced. FAPI 2.0 Advanced further extends the scope of FAPI 1.0 by bringing “non-repudiation” to all exchanges. This table gives a rough comparison:
Security Level
Non-Repudiation
FAPI 1.0 Baseline
Medium
None
FAPI 1.0 Advanced
FAPI 2.0 Baseline
High
Limited
FAPI 2.0 Advanced
High
Comprehensive
What is the current status of the FAPI 1.0 specifications?
The final version of the 1.0 specifications were published in March 2021.
A final spec is one that has gone through multiple rounds of review by many industry experts and has multiple live implementations.
I’m creating a new ecosystem, should I adopt FAPI 1.0 or 2.0?
There are valid reasons for adopting 1.0 or 2.0.
If vendors in an ecosystem already support FAPI 1.0, this could be a valid reason to use it.
If an ecosystem is already using OpenID Connect for identity claims, it may be harder to use FAPI 1.0.
FAPI 1.0 is a mature and widely supported security profile.
FAPI 2.0 requires less use of message signing which may make it easier to implement (especially for clients).
FAPI 1.0 does not cover complex authorization requests and grant lifecycle management, so you might need to implement a custom solution. FAPI 2.0 covers these aspects. Although the specifications are still in development they already represent the experience gathered by the WG and others who have implemented such solutions.
Should all FAPI 1.0 ecosystems migrate to FAPI 2.0?
For the same reason as the above answer, this is an ecosystem specific decision.
Will FAPI 1.0 be maintained
Yes, if there are any security issues, or major interoperability issues found with FAPI 1.0 the working group is likely to update the FAPI 1.0 specs. However the specs have been used in production in multiple ecosystems for some time, so the working group does not expect many (if any) changes to FAPI 1.0.
No new features are planned to be added to FAPI 1.0.
Can my authorization server support FAPI 1.0 and 2.0 at the same time to make migration easier?
This may be possible. FAPI 1.0 Advanced allows the use of PAR and PKCE. These are both required by FAPI 2.0.
Does a FAPI 1.0 Certified AS need to be OpenID Connect Certified
The FAPI and OpenID Connect certifications are orthogonal. In order to pass OpenID Connect certifications servers would have to support various lower security methods (like client_secret_basic for client authentication) that would generally not be enabled in FAPI compliant servers.
Has there been a security review of FAPI?
Yes. the analysis of FAPI 1.0 was led by Daniel Fett is found at
https://arxiv.org/pdf/1901.11520.pdf
FAPI Global Adoption References
FAPI 1.0
FAPI 2.0
UK Open Banking
Open Banking UK FAPI Adoption Announcement
Most of the CMA9 have certified and OIDF anticipates OBIE requiring CMA9 to recertify annually
Currently
15 UK banks have 31 FAPI certifications of 16 deployments
:
Barclays (Barclays OB TIAA)
Cater Allen (CA Open Banking v1.3.0)
Coutts & company (F23)
First Direct (Open Banking Read-Write API version 3.1.3)
Hargreaves Lansdown Savings Limited (Open Banking 3.1 FAPI)
HSBC RBWM (Open Banking Read-Write API version 3.1.3)
HSBC Business (Open Banking Read-Write API version 3.1.3)
ICICI Bank UK Plc (Open Banking v 3.1.2)
Marks and Spencer (Open Banking Read-Write API version 3.1.3)
National Westminster Bank Plc (Open Banking 3.1 FAPI)
Sainsbury’s Bank PLC (Sainsbury’s Bank Digital IAM Platform (version 19.8.8))
The Royal Bank Of Scotland Plc (Open Banking 3.1 FAPI)
TSB Bank PLC (CA API Gateway 9.4)
Ulster Bank Limited   (Open Banking 3.1 FAPI)
Vanquis Bank Ltd (Open Banking 3.1 FAPI)
WSO2 (UK) Limited (Openbanking v1.4.0)
AU CDR (Data 61)
https://consumerdatastandardsaustralia.github.io/standards/#future-dated-obligations
https://consumerdatastandardsaustralia.github.io/standards/#security-profile
Initial AU FAPI outreach workshops confirmed with AU DSB team for April 20th and May 4th
Berlin Group
STET
Mexico
Bahrain
Brazil
https://openbanking-brasil.github.io/areadesenvolvedor-fase2/#padroes
yes Scheme
yes QES service is based on FAPI 2.0 Baseline
FAPI Liaison Relationships
Financial Data Exchange (FDX) - USA
How does the FDX and OIDF collaboration work?
All FAPI work is done in the OIDF FAPI Working Group. The OpenID Foundation actively encourages participation in and contributions to all its working groups. FDX work groups operate under their own IP and membership rules. FDX makes independent assessments of normative references and certification requirements.
The group has expert members from the Identity and Access Management sector. The working group was initially formed to help develop security profiles and API standards for financial APIs. Over time the group has focussed its efforts on security profiles that while applicable for financial APIs, can be used in other industries and ecosystems.
The security profiles developed by the working group are based on the OAuth 2.0 and OpenID Connect suite of standards. OAuth 2.0 is an authorization framework which can be used for both low and high value operations. The standards produced by the FAPI WG contain much less optionality than the general OAuth 2.0 framework and require implementers to use modern security best practices.
The major benefits of the FAPI specifications are:
Clear point-by-point specifications that implementers can use as a “check list”
Exhaustive conformance tests to allow implementers to ensure their software is secure and interoperable
Standards based approach to securing complex interactions (e.g. decoupled authZ flows via CIBA, grant management, pushed request objects).
The FAPI WG does not work on data models or standards for financial or other APIs. These are ecosystem specific.
How does the FDX and OIDF liaison agreement work?
The FDX/OIDF agreement clarifies FDX’s usage of OIDF trademarks. The Liaison Agreement describes the common interests of the two organizations and how they might work together.
Can individuals and organizations be members of and contribute to both organizations?
Yes. OpenID Foundation recognizes the importance of diverse views and encourages robust community engagement. OIDF thanks organizations like Ping Identity, Intuit, Authlete and others for membership of both organizations and their contributions to FDX Work Groups as well as the OpenID Foundation’s Financial-Grade API Working Group.
As a consequence, FAPI 2.0 provides mechanisms for obtaining fine-grained and transactional authorization for API access and security mechanisms for replay detection and non-repudiation on both interfaces in addition to the mechanisms already defined in FAPI 1.0 focusing on the security of the authorization flow.
The working group also evolved the profile to be easier to use for developers based on the results of an analysis of various open banking implementations, the recommendations of the latest OAuth Security BCP, and a comprehensive security threat model.
Both FAPI 1.0 as well as FAPI 2.0 define two compliance levels, but the FAPI 2.0 levels are aligned with different protection levels (baseline vs advanced) rather than API access modes (read vs read-write) in FAPI 1.0. The baseline level aims to be secure against all threats captured in the security threat model, the advanced level adds non-repudiation.