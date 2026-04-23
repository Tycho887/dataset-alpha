---
{
  "title": "Re-thinking federated identity with the Continuous Access Evaluation Protocol | Google Cloud Blog",
  "url": "https://cloud.google.com/blog/products/identity-security/re-thinking-federated-identity-with-the-continuous-access-evaluation-protocol",
  "domain": "cloud.google.com",
  "depth": 2,
  "relevance_score": 0.35,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 9599,
  "crawled_at": "2026-04-23T20:52:15"
}
---

Security & Identity
Re-thinking federated identity with the Continuous Access Evaluation Protocol
February 22, 2019
Atul Tulshibagwale
Software Engineer
In today’s mobile and cloud-centric world, your typical enterprise user is logged in simultaneously to multiple cloud- and enterprise-hosted apps using federation protocols or certificates. These login sessions can last hours or even days—especially on mobile devices.
Increasingly however, whether or not to authorize a user session needs to be based on dynamic data such as the device’s location, IP location, device and app health, and user privileges. Imagine, for example, a user in the U.S. who is logged in on their phone to a cloud-based CRM service, and they get on a plane to China. When they land, the CRM provider needs to detect that new location and change the user’s access accordingly.
Here are some other scenarios that could benefit from dynamic authorization decisions:
A device connected into a corporate VPN needs to be disconnected after a malicious app is observed to be present on the device.
A file sharing app discovers the user’s IP address has changed, and needs to re-evaluate the user’s access privilege given its new IP location.
A user is added to a task group that requires access to a specific customer account. The CRM app must be notified of this change in order for the user to be able to access the required resources.
Unfortunately, providing this kind of dynamic access authorization can be difficult. Today’s technology determines access authorization only at the time of authentication, typically with the help of a  federated identity provider—or in the case of TLS client-auth, by the server-side app itself. Even with enterprise infrastructure such as WiFi routers or VPN servers, it’s hard for cloud-based identity providers to signal a change in session authorization.
Introducing the Continuous Access Evaluation Protocol
Continuous access evaluation is a new approach to access authorization that enables independent parties to control live user session properties. Sometimes referred to as “continuous authentication” by our industry peers, Google’s vision for a Continuous Access Evaluation Protocol (or CAEP) addresses the same concerns, but uses a standards-based approach.
Our vision for continuous access evaluation is based on a publish-and-subscribe (“pub-sub”) approach. Pub-sub is a good model to convey updated information about a session between apps, infrastructure, identity providers, device management services and device security services—regardless of whether they’re in the cloud or on-premises. Specifically, a publish-and-subscribe model has the following advantages:
It’s complementary to federated or cert-based authentication
It’s not as chatty as
WAM
It doesn’t impact latency for user access
Using pub-sub, a server-side endpoint—either a cloud app or an identity provider—can convey updated information about a session to interested parties. If a user is logged into multiple apps or infrastructure endpoints, they’re all notified about the updated status.
In contrast, federated identity, which is the most commonly used authentication system, is a “fire and forget” model—authorization decisions are only evaluated at login time. (Before the federated model was popular, enterprises used a chatty WAM model and evaluated every access to an app using a central access management server. This model, of course, isn’t viable with today’s traffic volumes and distributed environments.)
CAEP publishers and subscribers
In a typical cloud environment, a service can function either as a publisher or subscriber for various events. For example, an identity provider service is the publisher for authorization decisions or user attributes, but a VPN server or a SaaS app may also be a publisher for client IP address within a session.
On the flip side, a VPN server or SaaS app will typically subscribe to the identity provider’s authorization decisions or user attributes, and the identity provider may subscribe to information about a client IP from a VPN server or a SaaS app.
In other words, with CAEP, a typical cloud session may have multiple publishers such as identity providers, device management services, and security services, etc. It may also have multiple subscribers, e.g., multiple cloud apps, enterprise apps, and VPN and WiFi routers, etc.
Interacting with CAEP
CAEP allows publishers and subscribers to communicate a wide range of information about their active user sessions. You can see the CAEP’s operational flows by the interactions below.
In the diagram above, the interactions are:
Service request:
The device or app requests service from a relying party. This can happen multiple times during the life of an authenticated user session (e.g., each HTTP request is a service request.) The response can either be the successful completion of the request or a remediation response.
Context update:
If anything about a session is different from the previous access (e.g., first time access after authentication or a changed IP), the relying party publishes the updated context. This update message can also contain an interest or disinterest in receiving updates about the session. Subscribers to these messages may include policy servers such as identity providers.
User, device or policy update:
If a policy service learns about changes that impact a session (either from its own observations or after getting notified by a relying party), it processes and publishes updated information to all of that session’s subscribers.
Remediation response:
An update may result in the user, device, or app needing to be remediated. In this case, the relying party provides a response to a service request that specifies what went wrong and what remediation actions the user must take in order to resume services.
Note that in the above flow diagram, only interactions #1 and #4 have a request / response semantic. Interactions #2 and #3 are asynchronous updates that may be triggered at any time.
Establishing trust with CAEP
Each party in this pub-sub model establishes point-to-point trust with other parties. Each party announces what information they are capable of publishing about a  user session, and the trusting party determines which information that a publisher announces may be trusted. These communication channels use peer-authenticated TLS to ensure authenticity, privacy and integrity.
CAEP use cases
Here are some ways in which CAEP can solve real-world issues:
Geolocation
A user of a file sharing service travels to a foreign country with weak IP protections.
CAEP solution
The file sharing service provider publishes an event that the user’s IP location has changed.
The identity provider, which had expressed interest in the session by previously authorizing the service provider to allow access, is notified that the user’s IP location has changed.
It then re-evaluates the user’s access privileges and publishes new user attributes (including authorization decisions specific to the service provider) for all sessions that the user had logged into.
All service providers interested in that user’s sessions (including the file sharing service) obtain the new user attributes that include decisions on whether the user should continue to be allowed access to certain resources.
The service provider disables access to the user for certain resources.
App vulnerability
A vulnerability is discovered in a popular mobile app.
CAEP solution
The policy server re-evaluates access decisions for all users based on updated information from its internal vulnerability assessment. It publishes a termination message for all sessions that it knows to be using the mobile app. Service providers subscribing to those sessions receive the new message and terminate the client-session.
Suspicious user activity
A mobile phone belonging to an authenticated user has just downloaded suspicious apps and visited untrusted websites.
CAEP solution
An endpoint security service monitoring the device obtains information about the suspicious activity. It publishes a message that invalidates all sessions from that device. All service providers subscribed to those sessions then invalidate their internal sessions from that device, and the user needs to re-authenticate from that device in order to proceed.
Standardizing access authorization
With the rise of mobile devices and cloud-based apps, the time has come to reevaluate  federated approaches to identity and authorization. Here at the Google Cloud Identity team, we intend to submit CAEP as an open standard that leverages existing standards such as
SET
. A
related effort
in Google aims to standardize consumer account related security events through the
RISC working group
in the
OpenID foundation
. CAEP could be implemented as an extension of the same RISC proposal.
Can you think of more use cases where CAEP would be useful? Want to participate and keep up-to-date on CAEP? Provide your feedback
here
.
Posted in
Security & Identity
Google Cloud
Google Workspace
Related articles
Security & Identity
Introducing Google Cloud Fraud Defense, the next evolution of reCAPTCHA
By Jian Zhen • 4-minute read
Security & Identity
Next ‘26: Redefining security for the AI era with Google Cloud and Wiz
By Francis deSouza • 11-minute read
Security & Identity
Announcing new partner-supported workflows for Google Security Operations
By Raimundo Alcazar • 6-minute read
Security & Identity
Cloud CISO Perspectives: How CISOs can pursue technical and cultural resilience (Q&A)
By Thiébaut Meyer • 8-minute read