---
{
  "title": "Formal Security Analysis of OpenID for Verifiable Credentials - OpenID Foundation",
  "url": "https://openid.net/formal-security-analysis-openid-verifiable-credentials",
  "domain": "openid.net",
  "depth": 2,
  "relevance_score": 0.47,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3991,
  "crawled_at": "2026-04-23T20:52:00"
}
---

Formal Security Analysis of OpenID for Verifiable Credentials
Published January 18, 2024
The first in-depth security analysis of OpenID for Verifiable Credentials has been completed, with the goal of increasing confidence in the security of these specifications. The formal security analysis includes the protocols OpenID for Verifiable Credential Issuance (OID4VCI) and OpenID for Verifiable Presentations (OID4VP), both part of the
OpenID for Verifiable Credentials family
.
The
formal security analysis
uses the Web Infrastructure Model (WIM), a detailed formal model of the web, which has been developed by the University of Stuttgart and used to complete formal analysis of other protocols including the OpenID Foundation standards OpenID Connect, FAPI 1.0 and FAPI 2.0, and the foundational IETF standard OAuth 2.0 (RFC6749). In this instance, the WIM is used to model the interaction of OID4VCI and OID4VP in an ecosystem.
This work has been carried out as part of a master’s thesis at University of Stuttgart co-supervised by Verimi GmbH. The goal of the thesis was to prove that both protocols are secure with respect to the definition of security under certain assumptions and modeling decisions. The security definition used in the analysis covers several important properties around credential issuance and presentation; in particular, that an attacker must not be able to impersonate an honest user, initiate a login flow on a user's device, or force a user to be logged in under an attacker-chosen identity.
For cases where certain preconditions are not met, the analysis revealed some potential attacks. In particular, the pre-authorized code flow in OID4VCI and the cross-device flow in OID4VP may be vulnerable to phishing attacks and require user attention to be secure. These attacks are not surprising, as cross-device flow vulnerabilities are a well-known class of attacks, affecting
most cross-device protocols
. However, the analysis also confirmed the security of the same-device flows of OpenID for Verifiable Credentials. The OpenID Foundation’s Decentralized Credentials Protocols WG has taken the feedback from this master’s thesis into account in the current versions of the specifications.
Please refer to the analysis, a
master’s thesis
, for details on the assumptions, modeling decisions, security properties, and the formal mathematical proof.
Our thanks to Fabian Hauck for his master’s thesis, conducted under the supervision of Dr. Daniel Fett and Pedram Hosseyni M.Sc with Prof. Ralf Küsters as the Examiner at the Institute of Information Security, University of Stuttgart. The thesis was generously supported by Verimi GmbH through the IDunion project. Please note that this analysis is preliminary and has not yet been peer-reviewed. Additionally, it may not reflect recent changes in the current specifications as the analysis is based on the May 2023 versions of OpenID for Verifiable Presentations and OpenID for Verifiable Credential Issuance.
OpenID Foundation
The OpenID Foundation (OIDF) is a global open standards body committed to helping people assert their identity wherever they choose. Founded in 2007, we are a community of technical experts leading the creation of open identity standards that are secure, interoperable, and privacy preserving. The Foundation’s OpenID Connect standard is now used by billions of people across millions of applications. In the last five years, the Financial Grade API has become the standard of choice for Open Banking and Open Data implementations, allowing people to access and share data across entities. Today, the OpenID Foundation’s standards are the connective tissue to enable people to assert their identity and access their data at scale, the scale of the internet, enabling “networks of networks” to interoperate globally. Individuals, companies, governments and non-profits are encouraged to join or participate.
Find out more at
openid.net
.
Tagged
Security Analysis
Verifiable Credentials