---
{
  "title": "OpenID Connect for Identity Assurance Claims Registration 1.0",
  "url": "https://openid.net/specs/openid-connect-4-ida-claims-1_0-final.html",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 17111,
  "crawled_at": "2026-04-23T20:49:26"
}
---

OpenID Connect for Identity Assurance Claims Registration 1.0
openid-connect-4-ida-claims-1_0
October 2024
Lodderstedt, et al.
Standards Track
[Page]
Workgroup:
eKYC-IDA
Published:
1 October 2024
Status:
Final
Authors:
T. Lodderstedt
sprind.org
D. Fett
Authlete
M. Haine
Considrd.Consulting Ltd
A. Pulido
Santander
K. Lehmann
1&1 Mail & Media Development & Technology GmbH
K. Koiwai
KDDI Corporation
OpenID Connect for Identity Assurance Claims Registration 1.0
Abstract
This specification defines an extension of OpenID Connect that registers new JWT claims about end-users. This extension defines new claims relating to the identity of a natural person that were originally defined within earlier drafts of OpenID Connect for Identity Assurance. The work and the preceding drafts are the work of the eKYC and Identity Assurance working group of the OpenID Foundation.
¶
Foreword
The OpenID Foundation (OIDF) promotes, protects and nurtures the OpenID community and technologies. As a non-profit international standardizing body, it is comprised by over 160 participating entities (workgroup participant). The work of preparing implementer drafts and final international standards is carried out through OIDF workgroups in accordance with the OpenID Process. Participants interested in a subject for which a workgroup has been established have the right to be represented in that workgroup. International organizations, governmental and non-governmental, in liaison with OIDF, also take part in the work. OIDF collaborates closely with other standardizing bodies in the related fields.
¶
Final drafts adopted by the Workgroup through consensus are circulated publicly for the public review for 60 days and for the OIDF members for voting. Publication as an OIDF Standard requires approval by at least 50% of the members casting a vote. There is a possibility that some of the elements of this document may be subject to patent rights. OIDF shall not be held responsible for identifying any or all such patent rights.
¶
Introduction
This specification defines additional JWT claims about the natural person.  The claims defined can be used in various contexts including an ID Token.
¶
Warning
This document is not an OIDF International Standard. It is distributed for
review and comment. It is subject to change without notice and may not be
referred to as an International Standard.
Recipients of this draft are invited to submit, with their comments,
notification of any relevant patent rights of which they are aware and to
provide supporting documentation.
¶
Notational conventions
The keywords "shall", "shall not", "should", "should not", "may", and "can" in
this document are to be interpreted as described in ISO Directive Part 2
[
ISODIR2
]
. These keywords are not used as dictionary terms such that any
occurrence of them shall be interpreted as keywords and are not to be
interpreted with their natural language meanings.
¶
▲
Table of Contents
1.
Scope
This specification only defines claims to be maintained in the IANA "JSON Web Token Claims Registry" established by
[
RFC7519
]
.  These claims should be used in any context that needs to describe these characteristics of the end-user in a JWT as per
[
RFC7519
]
.
¶
2.
Normative references
See section 5 for normative references.
¶
3.
Terms and definitions
For the purposes of this document, the following terms and definitions apply.
¶
3.1.
claim
piece of information asserted about an entity
¶
[SOURCE:
[
OpenID
]
, 1.2]
¶
3.2.
identity proofing
process in which an end-user provides evidence to an OP or claim provider reliably identifying themselves, thereby allowing the OP or claim provider to assert that identification at a useful assurance level
¶
3.3.
identity verification
process conducted by the OP or a claim provider to verify the end-user's identity
¶
3.4.
identity assurance
process in which the OP or a claim provider asserts identity data of a certain end-user with a certain assurance towards an RP, typically expressed by way of an assurance level. Depending on legal requirements, the OP can be required to provide evidence of the identity verification process to the RP
¶
3.5.
verified claims
claims about an end-user, typically a natural person, whose binding to a particular end-user account was verified in the course of an identity verification process
¶
4.
Claims
4.1.
Additional claims about end-users
This specification defines the following claims for conveying end-user data in addition to the claims defined in the OpenID Connect specification
[
OpenID
]
and the OpenID Connect for Identity Assurance specification
[
OpenID4IDA
]
and in any other context that a JWT (as per
[
RFC7519
]
) may be used:
¶
Table 1
Claim
Type
Description
place_of_birth
JSON object
End-user's place of birth. The value of this member is a JSON structure containing some or all of the following members:
country
: String representing country in
[
ISO3166-1
]
Alpha-2  or
[
ISO3166-3
]
syntax.
region
: String representing state, province, prefecture, or region component. This field might be required in some jurisdictions.
locality
: String representing city or locality component.
nationalities
array
End-user's nationalities using ICAO 3-letter codes
[
ICAO-Doc9303
]
, 2-letter ICAO codes may be used in some circumstances for compatibility reasons.
birth_family_name
string
End-user's family name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the family name later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.
birth_given_name
string
End-user's given name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.
birth_middle_name
string
End-user's middle name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the middle name later in life for any reason. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.
salutation
string
End-user's salutation
title
string
End-user's title
msisdn
string
End-user's mobile phone number formatted according to ITU-T recommendation
[
E.164
]
also_known_as
string
Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides their legal name.
4.2.
Extended address claim
This specification extends the
address
claim as defined in
[
OpenID
]
by another sub field containing the country as ISO code.
¶
country_code
: Optional. country part of an address represented using an ISO 3-letter code
[
ISO3166-3
]
, e.g., "USA" or "JPN". 2-letter ISO codes
[
ISO3166-1
]
may be used for compatibility reasons.
country_code
may be used as alternative to the existing
country
field.
¶
4.3.
Examples
This section contains JSON snippets showing examples of end-user claims described in this document.
¶
{
"place_of_birth": {
  "country": "GB",
  "locality": "London"
  }
}
¶
{
"nationalities": ["GB", "SL"]
}
¶
{
"birth_family_name": "Elba"
}
¶
{
"birth_given_name": "Idrissa"
}
¶
{
"birth_middle_name": "Akuna"
}
¶
{
"salutation": "Mr"
}
¶
{
"title": "Dr"
}
¶
{
"msisdn": "1999550123"
}
¶
{
"also_known_as": "DJ Big Driis"
}
¶
"address": {
  "locality": "Leavesden",
  "postal_code": "WD25 7LR",
  "country": "United Kingdom",
  "street_address": "4 Privet Drive",
  "country_code": "GBR"
}
¶
5.
Security considerations
The working group has identified no security considerations that pertain directly to this specification.
¶
The data structures described in this specification will contain personal information. Standards referencing this specification and implementers using this specification should consider the secure transport of these structures and security and privacy implications that may arise from their use.
¶
6.
Normative References
[E.164]
ITU-T
,
"Recommendation ITU-T E.164"
,
November 2010
,
<
https://www.itu.int/rec/T-REC-E.164/en
>
.
[ICAO-Doc9303]
International Civil Aviation Organization
,
"Machine Readable Travel Documents, Seventh Edition, 2015, Part 3: Specifications Common to all MRTDs"
,
2015
,
<
https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf
>
.
[ISO3166-1]
ISO
,
"ISO 3166-1:2020. Codes for the representation of names of countries and their subdivisions -- Part 1: Country codes"
,
2020
,
<
https://www.iso.org/standard/72482.html
>
.
[ISO3166-3]
ISO
,
"ISO 3166-3:2020. Codes for the representation of names of countries and their subdivisions -- Part 3: Code for formerly used names of countries"
,
2020
,
<
https://www.iso.org/standard/72482.html
>
.
[ISODIR2]
ISO/IEC
,
"ISO/IEC Directives, Part 2 - Principles and rules for the structure and drafting of ISO and IEC documents"
,
<
https://www.iso.org/sites/directives/current/part2/index.xhtml
>
.
[OpenID]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
,
de Medeiros, B.
, and
C. Mortimore
,
"OpenID Connect Core 1.0 incorporating errata set 1"
,
8 November 2014
,
<
https://openid.net/specs/openid-connect-core-1_0.html
>
.
[OpenID4IDA]
Lodderstedt, T.
,
Fett, D.
,
Haine, M.
,
Pulido, A.
,
Lehmann, K.
, and
K. Koiwai
,
"OpenID Connect for Identity Assurance 1.0"
,
16 June 2023
,
<
https://openid.net/specs/openid-connect-4-identity-assurance-1_0.html
>
.
[RFC7519]
Jones, M.
,
Bradley, J.
, and
N. Sakimura
,
"JSON Web Token (JWT)"
,
RFC 7519
,
DOI 10.17487/RFC7519
,
May 2015
,
<
https://www.rfc-editor.org/info/rfc7519
>
.
Appendix A.
IANA considerations
A.1.
JSON Web Token claims registration
This specification requests registration of the following value in the IANA "JSON Web Token Claims Registry" established by
[
RFC7519
]
.
¶
A.1.1.
Registry contents
A.1.1.1.
Claim
place_of_birth
Claim Name:
place_of_birth
¶
Claim Description:
A structured claim representing the end-user's place of birth.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.2.
Claim
nationalities
Claim Name:
nationalities
¶
Claim Description:
String array representing the end-user's nationalities.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.3.
Claim
birth_family_name
Claim Name:
birth_family_name
¶
Claim Description:
Family name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the family name(s) later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.4.
Claim
birth_given_name
Claim Name:
birth_given_name
¶
Claim Description:
Given name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.5.
Claim
birth_middle_name
Claim Name:
birth_middle_name
¶
Claim Description:
Middle name(s) someone has when they were born, or at least from the time they were a child. This term can be used by a person who changes the middle name later in life for any reason. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.6.
Claim
salutation
Claim Name:
salutation
¶
Claim Description:
End-user's salutation, e.g., "Mr"
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.7.
Claim
title
Claim Name:
title
¶
Claim Description:
End-user's title, e.g., "Dr"
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.8.
Claim
msisdn
Claim Name:
msisdn
¶
Claim Description:
End-user's mobile phone number formatted according to ITU-T recommendation
[
E.164
]
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
A.1.1.9.
Claim
also_known_as
Claim Name:
also_known_as
¶
Claim Description:
Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides its legal name.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
Appendix B.
Acknowledgements
The following people at yes.com and partner companies contributed to the concept described in the initial contribution to this specification: Karsten Buch, Lukas Stiebig, Sven Manz, Waldemar Zimpfer, Willi Wiedergold, Fabian Hoffmann, Daniel Keijsers, Ralf Wagner, Sebastian Ebling, Peter Eisenhofer.
¶
We would like to thank Julian White, Bjorn Hjelm, Stephane Mouy, Alberto Pulido, Joseph Heenan, Vladimir Dzhuvinov, Azusa Kikuchi, Naohiro Fujie, Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman, Michael B. Jones, Jeff Lombardo, Taylor Ongaro, Peter Bainbridge-Clayton, Adrian Field, George Fletcher, Tim Cappalli, Michael Palage, Sascha Preibisch, Giuseppe De Marco, Nick Mothershaw, Hodari McClain, and Nat Sakimura for their valuable feedback and contributions that helped to evolve this specification.
¶
Appendix C.
Notices
Copyright (c) 2024 The OpenID Foundation.
¶
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.
¶
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
¶
Authors' Addresses
Torsten Lodderstedt
sprind.org
Email:
torsten@lodderstedt.net
Daniel Fett
Authlete
Email:
mail@danielfett.de
Mark Haine
Considrd.Consulting Ltd
Email:
mark@considrd.consulting
Alberto Pulido
Santander
Email:
alberto.pulido@santander.co.uk
Kai Lehmann
1&1 Mail & Media Development & Technology GmbH
Email:
kai.lehmann@1und1.de
Kosuke Koiwai
KDDI Corporation
Email:
ko-koiwai@kddi.com