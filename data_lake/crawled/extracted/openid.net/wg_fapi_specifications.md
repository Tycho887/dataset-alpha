---
{
  "title": "FAPI Working Group – Specifications - OpenID Foundation",
  "url": "https://openid.net/wg/fapi/specifications",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3882,
  "crawled_at": "2026-04-23T20:55:46"
}
---

FAPI Working Group - Specifications
FAPI is a general-purpose high-security API protection profile over OAuth. It has been adopted as nation-wide standard in many countries. FAPI WG is currently working on FAPI 2.0 suite of specifications.
FAPI Working Group
OVERVIEW
FAPI Working Group
CHARTER
FAPI Working Group
SPECIFICATIONS
FAPI Working Group
REPOSITORY
The working group has been developing the following specifications:
Final Specifications
FAPI 2 Specifications
FAPI 2.0 has a broader scope than FAPI 1.0 as it aims for complete interoperability at the interface between client and authorization server as well as interoperable security mechanisms at the interface between client and resource server.
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
FAPI 1 Specifications
FAPI 1 is a widely deployed highly secured OpenID Connect and OAuth profile that aims to provide specific implementation guidelines for security and interoperability. It is formally analized.
Financial-grade API Security Profile (FAPI) 1.0 – Part 1: Baseline
– A secured OpenID Connect and OAuth profile that aims to provide specific implementation guidelines for security and interoperability.
Financial-grade API Security Profile (FAPI) 1.0 – Part 2: Advanced
– A highly secured OpenID Connect and OAuth profile that aims to provide specific implementation guidelines for security and interoperability.
JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
– This specification was created to bring some of the security features defined as part of OpenID Connect to OAuth 2.0
Implementer's Drafts
FAPI: Client Initiated Backchannel Authentication (CIBA) Profile
– FAPI CIBA is a profile of the OpenID Connect’s CIBA specification that supports the decoupled flow
– Most recent
Implementer’s Draft
– Most recent
working copy
Grant Management for OAuth 2.0
– This profile specifies a standards based approach to managing “grants” that represent the consent a data subject has given. It was born out of experience with the roll out of PSD2 and requirements in Australia
– Most recent
Implementer’s Draft
– Most recent
working copy
Errata Correcions
Errata Corrections to JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)
– defines a new JWT-based mode to encode OAuth authorization responses. Clients are enabled to request the transmission of the authorization response parameters along with additional data in JWT format. This mechanism enhances the security of the standard authorization response with support for signing and optional encryption of the response. A signed response provides message integrity, sender authentication, audience restriction, and protection from mix-up attacks. Encrypting the response provides confidentiality of the response parameter values. The JWT authorization response mode can be used in conjunction with any response type.
Drafts
FAPI 2.0: Message Signing
– an extension of the baseline profile that provides non-repudiation for all exchanges including responses from resource servers
FAPI 2.0 Http Signatures
– This document specifies the methods for clients, authorization servers and resource servers to sign and verify messages.
FAPI 1.0 — Lodging Intent ===> Now
OAuth PAR
+
OAuth RAR
Resources
Australia Consumer Data Rights
Brazil Security Work Group
EU General Data Protection Regulation (GDPR)
European Payment Services Directive (PSD2)
UK Open Banking Initiative (OBIE)
USA and Canada (FDX)