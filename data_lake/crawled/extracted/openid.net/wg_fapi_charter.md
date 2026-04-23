---
{
  "title": "FAPI Working Group – Charter - OpenID Foundation",
  "url": "https://openid.net/wg/fapi/charter",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5806,
  "crawled_at": "2026-04-23T21:01:02"
}
---

FAPI Working Group - Charter
The FAPI working group provides JSON data schemas, security and privacy recommendations and protocols to enable applications to utilize the data stored in a financial account, to enable applications to interact with a financial account, and enable users to control the security and privacy settings.
FAPI Working Group
OVERVIEW
FAPI Working Group
CHARTER
FAPI Working Group
SPECIFICATIONS
FAPI Working Group
REPOSITORY
1) Working Group name
FAPI was previously known as the Financial-grade API but there was consensus within the working group to update the name to just FAPI to reflect that the specification is appropriate for many high-value use-cases requiring a more secure model beyond just financial services.
2) Purpose
The goal of FAPI is to provide JSON data schemas, security and privacy recommendations and protocols to:
enable applications to utilize the data stored in the financial account,
enable applications to interact with the financial account, and
enable users to control the security and privacy settings.
Both commercial and investment banking account as well as insurance, and credit card accounts are to be considered.
3) Scope
The group will define
JSON format to represent account related data, e.g., Account Representation, Transactions, Current Status,
REST API for the accounts,
security profiles for OpenID Connect and OAuth,
Purchase history of commerce site, and
Receipt Data
Out of scope: Web Payment (will refer the W3C Web Payment WG product if needed.)
4) Proposed specifications
The group proposes the following Specification deliverables:
Read only APIs for
Commercial Bank Accounts,
Investment Bank (brokerage) Accounts,
Life Insurance Accounts,
Casualty Insurance Accounts,
Credit Card Accounts.
Write Access API including account creation but excluding web payment for
Commercial Bank Accounts,
Investment Bank (brokerage) Accounts,
Life Insurance Accounts,
Casualty Insurance Accounts,
Credit Card Accounts.
5) Anticipated audience or users
Financial institutions and service Providers who interacts with the financial accounts to provide the service to users.
6) Language
English
7) Method of work
E-mail discussions on the working group mailing list, working group conference calls, and face-to-face meetings from time to time.
8) Basis for determining when the work is completed
In many cases, Fintech services such as aggregation services uses screen scraping and stores user passwords. This model is both brittle and insecure. To cope with the brittleness, it should utilize an API model with structured data and to cope with insecurity, it should utilize a token model such as OAuth [RFC6749, RFC6750].
There are some examples of API models such as OFX, but it uses SOAP/XML model. However, SOAP/XML model has grown unpopular among the developers. Also, the OFX does not deploy the token model but uses user password, causing insecurity.
This working group aims to rectify the situation by developing a REST/JSON model protected by OAuth.
Related works
RFC 6749 OAuth Frameworks
RFC 6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage
RFC 7636 Proof Key for Code Exchange by OAuth Public Clients
OAuth 2.0 Proof-of-Possession (PoP) Security Architecture
OpenID Connect
Open Financial Exchange
ISO 20022 Payment Messages
OpenBank API
W3C Web Payments API
IFX
FIX
SWIFT
FS-ISAC Durable Data API
Proposers
Nat Sakimura, Nomura Research Institute
John Bradley, Ping Identity
Henrik Biering, Peercraft
Junichi Tabuchi, KDDI
Nov Matake, Yauth.jp
Anthony Nadalin, Microsoft
Anoop Saxena, Intuit
Toshio Taki, Money Forward
Anticipated contributions
Financial-grade API Pre-Working DraftInvestment Banking Read Only API pre-Working Draft
Investment Banking Transaction API pre-Working Draft
Commercial Banking Read Only API pre-Working Draft
Background information
The working group intends to expedite the process of gathering stakeholder representatives to collaborate in the development of profiles to support secure and privacy enhancing online authentication, authorization, and consent when accessing public sector and/or other high value private sector services.
France Connect, BA ID in Argentina and Clave Unica in Chile are some examples of Governments currently using OpenID Connect for broad citizen to Government interaction.
One impetus is the proliferated deployment of “identity hub” architectures within many international digital services delivery schemes, such as the US’s Connect.gov and the United Kingdom’s Verify UK. Currently, relying party applications integrate with these architectures using Security Assertions Markup Language (SAML) v2.0. While a well-known standard, SAML does not support the consent and authorization mechanisms of OpenID Connect, nor is it easy to integrate with for a broad range of application developers. This working group would determine the privacy and security characteristics, as well as the relevant use cases within the public sector necessary to establish a profile that can be widely deployed in government identity services.
It is expected that the profiles developed in this working group would be recommended within public services trust frameworks, such as the US Trust Framework Services (TFS) program.
Related work and liaison relationships
RFC 6749 OAuth Frameworks
RFC 6750 The OAuth 2.0 Authorization Framework: Bearer Token Usage
RFC 7636 Proof Key for Code Exchange by OAuth Public Clients
OAuth 2.0 Proof-of-Possession (PoP) Security Architecture
OpenID Connect
Open Financial Exchange
ISO 20022 Payment Messages
OpenBank API
W3C Web Payments API
IFX
FIX
SWIFT
FS-ISAC Durable Data API
WG considers establishing liaison agreement with the following organizations:
ISO/TC68 Financial Services
W3C Web Payments WG
Open Financial Exchange
IFX Forum
FS-ISAC