---
{
  "title": "Digital Credentials Protocols (DCP) Working Group – Specifications - OpenID Foundation",
  "url": "https://openid.net/wg/digital-credentials-protocols/specifications",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3222,
  "crawled_at": "2026-04-23T20:55:09"
}
---

Digital Credentials Protocols (DCP) Working Group - Specifications
The goal of the Digital Credentials Protocols (DCP) working group is to develop OpenID specifications for the Issuer-Holder-Verifier-Model use-cases to enable issuance and presentations of the Digital Credentials of any format (
W3C VCs, IETF SD-JWT VCs, ISO/IEC 18013-5, etc.
) and pseudonymous authentication from the End-User to the Verifier.
Digital Credentials Protocols (DCP) Working Group
OVERVIEW
Digital Credentials Protocols (DCP) Working Group
CHARTER
Digital Credentials Protocols (DCP) Working Group
SPECIFICATIONS
Digital Credentials Protocols (DCP) Working Group
REPOSITORIES
Some specifications are planned to be migrated from the
Connect WG
and some will be adopted in the new DCP WG. For the list of anticipated work items, please reference the
DCP WG Charter
.
Final Specifications
OpenID4VC High Assurance Interoperability Profile (HAIP) 1.0
– defines a profile of OpenID for Verifiable Credentials in combination with the credential formats IETF SD-JWT VC [
I-D.ietf-oauth-sd-jwt-vc
] and ISO mdoc [
ISO.18013-5
]. The aim is to select features and to define a set of requirements for the existing specifications to enable interoperability among Issuers, Wallets, and Verifiers of Credentials where a high level of security and privacy is required.
OpenID for Verifiable Credential Issuance 1.0
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
Open ID4VC High Assurance Interoperability Profile (HAIP) 1.0
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
Implementer's Drafts
None at present.
Drafts
Security and Trust in OpenID for Verifiable Credentials
Describes the trust architecture in OpenID for Verifiable Credentials, outlines security considerations and requirements for the components in an ecosystem, and provides an informal security analysis of the OpenID for VC protocols.
–
Working Group Draft
–
GitHub Repository
OpenID for Verifiable Presentations over BLE
Defines how Bluetooth Low Energy (BLE) can be used to request the presentation of verifiable credentials
–
GitHub Repository