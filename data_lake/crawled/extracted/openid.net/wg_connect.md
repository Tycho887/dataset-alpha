---
{
  "title": "AB/Connect Working Group - OpenID Foundation",
  "url": "https://openid.net/wg/connect",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 7989,
  "crawled_at": "2026-04-23T21:00:56"
}
---

AB/Connect Working Group - Overview
The AB/Connect working group is a combined working group of the Artifact Binding (AB) Working Group and the Connect Working Group aimed at producing the OAuth 2.0 based “OpenID Connect” specifications. It also includes a project named OpenID for Verifiable Credentials which consists of three specifications.
AB/Connect Working Group
OVERVIEW
AB/Connect
Working Group
CHARTER
AB/Connect
Working Group
SPECIFICATIONS
AB/Connect
Working Group
REPOSITORIES
What is AB/Connect Working Group?
OpenID Connect is a suite of lightweight specifications that provide a framework for identity interactions via REST like APIs. The simplest deployment of OpenID Connect allows for clients of all types including browser-based, mobile, and JavaScript clients, to request and receive information about identities and currently authenticated sessions. The specification suite is extensible, allowing participants to optionally also support encryption of identity data, discovery of the OpenID Provider, and advanced session management, including logout.
Papers, Presentations, and Announcements
OpenID Connect specifications published as ISO standards
on October 1, 2024
Fourth Implementer’s Draft of OpenID Federation Approved
on July 24, 2024
Second Errata Set for OpenID Connect Specifications Approved
on December 16, 2023
The OpenID Connect Logout specifications are now Final Specifications
on September 12, 2022
OpenID Foundation Publishes “OpenID for Verifiable Credentials” Whitepaper
on May 12, 2022
OpenID Certification
for RPs was made available to all in August 2017
Final OAuth 2.0 Form Post Response Mode Specification was approved
on April 27, 2015
The certification program for OpenID Connect was launched
on April 22, 2015
Final OpenID Connect specifications were launched
on February 26, 2014
Working Group Chairs
Michael B. Jones, Self-Issued Consulting
Nat Sakimura,  NAT Consulting
Frederik Krogsdal Jacobsen, Idura
Participation
To monitor progress and connect with working group members, join the
mailing list
.
To participate in or contribute to a specification within the working group requires the submission of an Intellectual Property Rights (IPR) contribution agreement.  You can complete this electronically or by paper at
openid.net/intellectual-property
.
Be sure to specify, in the working groups box, the exact name:
Meeting Schedule
Monday Meetings
When: Tuesday 8am Japan Time every other week
Join Meeting
Thursday Meetings
When: Thursday 7am PDT every week
Join Meeting
View Calendar
Frequently asked Questions
What is OAuth 2.0 and how is it related to OpenID Connect?
OAuth 2.0, is a framework, specified by the IETF in RFCs 6749 and 6750 (published in 2012) designed to support the development of authentication and authorization protocols. It provides a variety of standardized message flows based on JSON and HTTP; OpenID Connect uses these to provide Identity services.
How is OpenID Connect different from OpenID 2.0?
OpenID Connect has many architectural similarities to OpenID 2.0, and in fact the protocols solve a very similar set of problems. However, OpenID 2.0 used XML and a custom message signature scheme that in practice sometimes proved difficult for developers to get right, with the effect that OpenID 2.0 implementations would sometimes mysteriously refuse to interoperate. OAuth 2.0, the substrate for OpenID Connect, outsources the necessary encryption to the Web’s built-in TLS (also called HTTPS or SSL) infrastructure, which is universally implemented on both client and server platforms. OpenID Connect uses standard JSON Web Token (JWT) data structures when signatures are required. This makes OpenID Connect dramatically easier for developers to implement, and in practice has resulted in much better interoperability.
The OpenID Connect interoperability story has been proven in practice during an extended series of interoperability trials conducted by members of the OpenID Connect Working Group and the developers behind numerous OpenID Connect implementations.
Does OpenID Connect work for native and mobile apps?
Yes. There are already system-level APIs built into the Android operating system to provide OpenID Connect services. OpenID Connect can also accessed by interacting with the built-in system browser on mobile and desktop platforms; a variety of libraries are under construction to simplify this process.
Why should network operators care about OpenID Connect?
Simply stated, there is a significant increase of online services being accessed via mobile devices and there is an increase in online identity thefts. The GSMA has articulated the business case for Mobile Network Operators (MNOs)
http://www.gsma.com/mobileidentity
. In summary, it states that MNOs, with their differentiated identity and authentication assets, have the ability to provide sufficient authentication to enable consumers, businesses, and governments to interact in private, trusted and secure environment and enable access to services.
MNOs increasingly are interested in identity services currently being used online (i.e. login, marketing, post sales engagement, payments, etc.), to mitigate some of the pain points encountered in existing services, in order to meet the rapidly increasing market demand for mobile identity services.
How does OpenID Connect improve security?
Public-key-encryption-based authentication frameworks like OpenID Connect (and its predecessors) globally increase the security of the whole Internet by putting the responsibility for user identity verification in the hands of the most expert service providers. Compared to its predecessors, OpenID Connect is dramatically easier to implement and integrate and can expect to receive much wider adoption.
Is OpenID Connect privacy preserving?
OpenID Connect identifies a set of personal attributes that can be exchanged between Identity Providers and the apps that use them, and includes an approval step so that users can consent (or deny) the sharing of this information.
What about new authentication technologies like biometrics and devices?
This is an exciting time; innovators are working on several new kinds of authentication technologies to replace or supplement passwords – in particular, the use of hardware authentication devices and embedded cryptography.
These new methods can be adopted by OpenID Connect Identity Providers as they mature to provide more secure authentication to them. For example, two-factor identification is already in production at some OpenID Connect IDPs.
The fact that professionally run OpenID Connect IDPs can take advantage of these new technologies as they mature only increases the value proposition of OpenID Connect. Without doing anything extra, it means that OpenID Connect Relying Parties can benefit from the adoption of stronger authentication technologies by IDPs, simply because they already use OpenID Connect.
How does OpenID Connect relate to the FIDO Alliance?
The FIDO Alliance is one organization in which non-password authentication technologies are being explored. Some OpenID Foundation members are also members of the FIDO Alliance, working on authentication technologies there that can be used by OpenID Providers.
How does OpenID Connect relate to SAML?
The Security Assertion Markup Language (SAML) is an XML-based federation technology used in some enterprise and academic use cases. OpenID Connect can satisfy these same use cases but with a simpler, JSON/REST based protocol. OpenID Connect was designed to also support native apps and mobile applications, whereas SAML was designed only for Web-based applications. SAML and OpenID Connect will likely coexist for quite some time, with each being deployed in situations where they make sense.
How does OpenID Connect enable creating an Internet identity ecosystem?
Interoperability
Security
Ease of deployment
Flexibility
Wide support of devices
Enabling Claims Providers to be distinct from Identity Providers