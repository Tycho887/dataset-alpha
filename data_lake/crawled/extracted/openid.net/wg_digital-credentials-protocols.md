---
{
  "title": "Digital Credentials Protocols (DCP) Working Group - OpenID Foundation",
  "url": "https://openid.net/wg/digital-credentials-protocols",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5017,
  "crawled_at": "2026-04-23T20:48:47"
}
---

Digital Credentials Protocols (DCP) Working Group - Overview
The goal of the Digital Credentials Protocols (DCP) working group is to develop OpenID specifications for the Issuer-Holder-Verifier-Model use-cases to enable issuance and presentations of the Digital Credentials of any format (W3C VCs, IETF SD-JWT VCs, ISO/IEC 18013-5, etc.) and pseudonymous authentication from the End-User to the Verifier.
Digital Credentials Protocols (DCP) Working Group
OVERVIEW
Digital Credentials Protocols (DCP) Working Group
CHARTER
Digital Credentials Protocols (DCP) Working Group
SPECIFICATIONS
Digital Credentials Protocols (DCP) Working Group
REPOSITORIES
What is the Digital Credentials Protocols (DCP) Working Group?
In the Issuer-Holder-Verifier Model, Issuers issue Digital Credentials to the Holder’s Wallet, which the End-User can then use to present the Digital Credentials to the Verifiers. Digital Credentials are cryptographically signed statements about a Subject, typically the Wallet Holder. Verifiers can check the authenticity of the data in the Digital Credentials and optionally enforce Key Binding, Biometrics Binding and/or Claim-based Binding i.e., ask the Wallet to prove that it is the intended Holder of the Digital Credential.
The goal of this WG is to develop OpenID specifications for the Issuer-Holder-Verifier-Model use-cases to enable issuance and presentations of the Digital Credentials of any format (IETF SD-JWT, ISO/IEC 18013-5, etc.) and pseudonymous authentication from the End-User to the Verifier.
These specifications are aimed at allowing End-Users to gain more control, privacy, and portability over their identity information; cheaper, faster, and more secure identity verification, when transforming physical credentials into digital ones using digital credentials; and a universal approach to handle identification, authentication, and authorization in digital and physical space.
The work is planned to be done in liaison with the European Commission, Decentralized Identity Foundation (DIF), the European Telecommunications Standards Institute (ETSI), and ISO/IEC SC17 WG4 and WG10, which have expressed interest in profiling specifications proposed to be worked on in this WG. There is also a liaison with the OpenWallet Foundation (OWF), to foster implementation of the standards developed by this WG.
Adoption
European Digital Identity Architecture and Reference Framework
lists OID4VCI, OID4VP and SIOPv2 as required for certain use-cases
18 wallets in European Commission EBSI project support OID4VCI and OID4VP specifications (as of 2023/04/05).
–
Conformant wallets – EBSI – (europa.eu)
DIF JWT VC Presentation Profile
uses OID4VP as the base protocol for the request and verification of W3C JWT VCs, and uses SIOPv2 for user authentication.
NIST National Cybersecurity Center of Excellence plans to implement reference implementation for OID4VP to present mdocs/mDL
–
Landing page
–
Project description (draft)
The following draft ISO standards reference
–
draft ISO/IEC DTS 23220-4
profiles OID4VP to present mdocs
–
draft ISO/IEC TS 18013-7
profiles OID4VP to present mDLs (mobile driving licence)
–
draft ISO/IEC TS 23220-3
profiles OID4VCI to issue mdocs
Note that the three Technical Specifications mentioned above are not final, are subject to change, and are not public yet.
Publications and Media
The original white paper “
OpenID for Verifiable Credentials
”
Torsten Lodderstedt and Kristina Yasuda on
Identerati Office Hours
Security Analysis
Formal Security Analysis of the OpenID for Verifiable Presentations Specification
– A July 2025 analysis conducted by the University of Stuttgart.
Formal security analysis of OpenID for Verifiable Credentials
— The first in-depth security analysis of OpenID for Verifiable Credentials has been completed, with the goal of increasing confidence in the security of these specifications. The formal security analysis includes the protocols OpenID for Verifiable Credential Issuance (OID4VCI) and OpenID for Verifiable Presentations (OID4VP), both part of the
OpenID for Verifiable Credentials family
. Learn more
here
.
Working Group Chairs
Kristina Yasuda (SPRIND)
Joseph Heenan (Authlete)
Dima Postnikov
Brent Zundel (Yubico)
The chairs can be reached at
openid-specs-digital-credentials-protocols-owner@lists.openid.net
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
EU Call: Thursday’s @ 8AM PT
America Call: Tuesday’s @ Midday PT
APAC Call: Thursday’s @ 4PM JST
Zoom software is available on Mac, PC, iPhone, and Android Phone.
Join Meeting
Meeting Minutes are available in the
mailing list archives
View Calendar