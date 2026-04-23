---
{
  "title": "OpenID Connect | Okta",
  "url": "https://www.okta.com/openid-connect",
  "domain": "www.okta.com",
  "depth": 2,
  "relevance_score": 0.35,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5828,
  "crawled_at": "2026-04-23T20:58:09"
}
---

What is OpenID Connect?
Whether you are boarding a flight, checking into a hotel or requesting a passport, in order to complete any of these tasks you must first verify your identity (authentication). Followed by flight and seat assignment, reservation and credit card confirmation and citizenship verification (authorization). In today's ever changing technology landscape, identity is becoming the only true identifier. When we think about
authentication and authorization
, both have their place in the identity and access management space but authentication is key to the identity component and key to federation. This is where OpenID Connect comes into play.
What is OpenID Connect?
OpenID Connect is a protocol that sits on top of the OAuth 2.0 framework. Where OAuth 2.0 provides authorization via an access token containing scopes, OpenID Connect provides authentication by introducing a new token, the ID token which contains a new set of scopes and claims specifically for identity. With the ID token, OpenID Connect adds structure and predictability to allow otherwise different systems to interoperate and share authentication state and user profile information.
Why is OpenID Connect important?
Identity is the key to any cloud strategy. At the core of modern authorization is OAuth 2.0, but OAuth 2.0 lacks an authentication component. Implementing OpenID Connect on top of OAuth 2.0 completes an IAM strategy. As more and more companies need to interoperate and more identities are being populated on the internet the demand to be able to re-use these identities will also increase thus, to serve the demand of digital customers it is crucial that identity and authentication be a part of your strategy not only authorization.
What Does OpenID Connect add to OAuth 2.0?
Scopes
Of the changes OpenID Connect brings and arguably one of the most important is a standard set of scopes. In the OAuth 2.0 specification, scopes are whatever the OAuth provider wants them to be. While this is flexible, it makes interoperability effectively impossible. OIDC standardizes these scopes to openid, profile, email, and address.
Claims
In addition to standardizing the scopes used, OpenID Connect also standardizes the sets of claims for the OpenID Connect scopes. It is these standard sets of claims that contain the user specific information for authentication. For example, by having claims specifically named given_name and family_name, other systems from other organizations can create and receive user information in repeatable, predictable patterns.
ID token
For OpenID Connect, scopes can be used to request specific sets of information. This information is made available as claim values. The identity information in the ID token is specifically intended to be read by 3rd party applications to authenticate the same identity across multiple web applications, a crucial component of federation.
User info endpoint
In addition to the ID token, with the implementation of OpenID Connect comes standardized endpoints. In particular, the /userinfo endpoint allows for the verification of identity information metadata and is key to interoperability with other OpenID Connect systems suitable for enterprise grade solutions.
JWT (JSON Web Token)
JWT (pronounced j-o-t) is a cryptographically signed JSON payload that stores the user information. Using JWT’s allows information to be verified and trusted with a digital signature. With this trusted digital signature in place the information can later be verified using a signing key. OpenID Connect utilizes the JWT standard for the ID token.
OAuth 2.0 and OpenID Connect
What is the OpenID Foundation?
The OpenID Foundation is an open standards working group crafting specifications around OpenID and promoting its adoption. OpenID Connect is their primary standard, which defines establishing authentication through the OAuth2.0 framework. The OpenID Foundation provides certifications through a full test suite based on the requirements laid out in the specifications they publish.
Why is an OpenID Connect certification important?
The OpenID Connect certification and accompanying conformance profiles (areas of certification) work to promote interoperability among different entities. Okta is proud to hold the OpenID Connect certification in Basic OpenID Provider, Implicit OpenID Provider, Hybrid OpenID Provider,Config OpenID Provider and Form Post OpenID Provider. Supporting this standard reassures our customers that Okta can serve as the foundation for, or consume information from any other OpenID Connect certified system using standard patterns, tools, and libraries. This is also a testament of our dedication to our customers’ continued success.
Why use OpenID Connect with Okta?
Okta is the only 5 time Gartner Magic Quadrant leader in the access management space. Our support of OpenID Connect solidifies this position and demonstrates our continued commitment to modern authentication standards. Also of importance is Okta’s commitment to the OpenID Connect foundation of which it is a member. This membership demonstrates our commitment to promoting and enabling our customers to utilize OpenID technologies. Many companies are already leveraging the next generation of authentication for their modern applications and the investment Okta is making to help make them be successful is evident via the OpenID Connect certification and OpenID Connect foundation membership.
Start using your free developer Okta tenant and OpenID Connect.
Get started
OpenID Connect Resources
OpenID Connect Certification
OpenID Connect Conformance Profiles
OpenID Connect Spec
OpenID Connect at Okta
Get Started with OpenID Connect in Okta
Okta’s Authentication Guide
Troubleshooting OpenID Connect
Okta's Related Products
API Access Management
Customer Identity Products