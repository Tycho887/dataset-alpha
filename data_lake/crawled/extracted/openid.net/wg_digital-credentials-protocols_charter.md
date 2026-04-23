---
{
  "title": "Digital Credentials Protocols (DCP) Working Group – Charter - OpenID Foundation",
  "url": "https://openid.net/wg/digital-credentials-protocols/charter",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5073,
  "crawled_at": "2026-04-23T20:55:07"
}
---

Digital Credentials Protocols (DCP) Working Group - Charter
The goal of the Digital Credentials Protocols (DCP) working group is to develop OpenID specifications for the Issuer-Holder-Verifier-Model use-cases to enable issuance and presentations of the Digital Credentials of any format (W3C VCs, IETF SD-JWT VCs, ISO/IEC 18013-5, etc.) and pseudonymous authentication from the End-User to the Verifier.
Digital Credentials Protocols (DCP) Working Group
OVERVIEW
Digital Credentials Protocols (DCP) Working Group
CHARTER
Digital Credentials Protocols (DCP) Working Group
SPECIFICATIONS
Digital Credentials Protocols (DCP) Working Group
REPOSITORIES
Digital Credentials Protocols (DCP) Working Group
Charter
1) Working Group name
Digital Credentials Protocols Working Group
2) Purpose
In the Issuer-Holder-Verifier Model, Issuers issue Digital Credentials to the Holder’s Wallet, which the End-User can then use to present the Digital Credentials to the Verifiers. Digital Credentials are cryptographically signed statements about a Subject, typically the Wallet Holder. Verifiers can check the authenticity of the data in the Digital Credentials and optionally enforce Key Binding, Biometrics Binding and/or Claim-based Binding i.e., ask the Wallet to prove that it is the intended Holder of the Digital Credential.
The goal of this WG is to develop OpenID specifications for the Issuer-Holder-Verifier-Model use-cases to enable issuance and presentations of the Digital Credentials of any format (IETF SD-JWTl, ISO/IEC 18013-5, etc.) and pseudonymous authentication from the End-User to the Verifier.
These specifications are aimed at enabling End-Users to gain more control, privacy, and portability over their identity information; cheaper, faster, and more secure identity verification, when transforming physical credentials into digital ones using digital credentials; and a universal approach to handle identification, authentication, and authorization in digital and physical space.
The work is planned to be done in liaison with the European Commission, Decentralized Identity Foundation (DIF), the European Telecommunications Standards Institute (ETSI), and ISO/IEC SC17 WG4 and WG10, which have expressed interest in profiling specifications proposed to be worked on in this WG. There is also a liaison with the OpenWallet Foundation (OWF), to foster implementation of the standards developed by this WG.
3) Scope
Creation of specifications describing:
Issuance of Digital Credentials from the Issuer to the Wallet (acting as RP). This includes the mechanisms to specify which Digital Credentials the Issuer is capable of issuing.
Presentation of Digital Credentials between the Wallet (acting as IdP) and the Verifier via online (over the Internet) and proximity (near field communication) communication channels. This includes the mechanisms to specify which Digital Credentials are being requested.
Pseudonymous authentication from the End-User to the Verifier.
Interoperability profiles of the above specifications
Out of Scope:
Legal or regulatory advice, Identity Proofing, Identity information verification, new Credential formats
4) Proposed specifications
OpenID for Verifiable Presentations
OpenID for Verifiable Credential Issuance
Self-Issued OpenID Provider v2.0
OpenID for Verifiable Presentations over BLE
OpenID Connect UserInfo Verifiable Credentials
Security and Trust in OpenID for Verifiable Credentials
OpenID4VC High Assurance Interoperability Profile with SD-JWT VC
5) Anticipated audience or users
Issuers of Digital Credentials
Verifiers Digital Credentials
Wallet Providers
Trust Framework operators
Regulators
Security Researchers
Developer tools & infrastructure/service provider
6) Language
English.
7) Method of work
Mailing list and telephone/internet conference calls combined with face-to-face (where needed) and information sharing/collaborative working via online tools.
8) Basis for determining when the work is completed
Approved “final” specifications consistent with the purpose and scope that have been through the OpenID Foundation process including vote by the membership and running code in one or more proof-of-concept, interoperability event or commercial project.
Related work
The work is planned to be done in liaison with the European Commission, Decentralized Identity Foundation (DIF), ETSI, and ISO/IEC SC17 WG4 and WG10, which have expressed interest in profiling specifications proposed to be worked on in this WG.
Proposers
Kristina Yasuda, Microsoft
Torsten Lodderstedt, yes.com AG
Joseph Heenan, Authlete
Mark Haine, Considrd.Consulting Limited
Oliver Terbu, Spruce Systems Inc.
Takahiko Kawasaki, Authlete
Vittorio Bertocci, Okta
Giuseppe De Marco, Dipartimento per la trasformazione digitale
Brian Campbell, Ping Identity
Michael B. Jones, independent
Jacob Ideskog, Curity AB
Morteza Ansari, independent
David Luna, ForgeRock
Timo Glastra, Animo Solutions
Judith Kahrer, Curity AB
Anticipated contributions
https://openid.net/sg/openid4vc/specifications/
https://github.com/vcstuff/oid4vc-haip-sd-jwt-vc