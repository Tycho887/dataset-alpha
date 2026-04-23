---
{
  "title": "Naming and Contents of Specifications - OpenID Foundation",
  "url": "https://openid.net/wg/resources/naming-and-contents-of-specifications",
  "domain": "openid.net",
  "depth": 2,
  "relevance_score": 0.2,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3905,
  "crawled_at": "2026-04-23T20:56:29"
}
---

OpenID Working Group specifications use the following naming conventions:
The title line of a draft contains the draft title, a specification version number (typically 1.0), and a draft number, for example “OpenID Federation 1.0 – draft 32”.
The filenames for a draft specification in source code repositories incorporate the title and version but not the draft number, for example
openid-federation-1_0.html
and
openid-federation-1_0.html
. When published to
openid.net/specs/
filenames including the draft number are also published, such as
openid-federation-1_0-32.html
and
openid-federation-1_0-32.html
.
Drafts published to
openid.net/specs/
use sequential draft numbers. The initial working group draft for a specification uses draft number -00.
The filenames for spec sources and spec outputs are the same, except for the extensions, for example,
fapi-2_0-message-signing.md
and
fapi-2_0-message-signing.html
.
Specifications that are Implementer’s Drafts are also published at
openid.net/specs/
with filenames indicating the Implementer’s Draft number, such as openid-client-initiated-backchannel-authentication-core-1_0-ID2.html.
Final Specifications indicate that their status is “Final” in their header material and do not include a draft number, for example, see
https://openid.net/specs/openid-connect-prompt-create-1_0.html
.
Final Specifications are also published at
openid.net/specs/
with filenames including -final, such as openid-connect-prompt-create-1_0-final.html.
Specifications including Errata corrections indicate that in their titles, for example, “OpenID Connect Core 1.0 incorporating errata set 2”.
Non-final drafts of specifications including Errata corrections also include a draft number in their titles, for example, “OpenID Connect Core 1.0 – draft 36 incorporating errata set 3”.
When published to
openid.net/specs/
, filenames of non-final drafts of specifications including Errata corrections including the draft number are published, such as
openid-connect-core-1_0-36.html
but not the name without a version number, such as
openid-connect-core-1_0.html
, so as to not overwrite the published Final specification or approved Errata specification.  Specifications named without version numbers are only published for Approved specifications including Errata corrections.
Approved specifications including Errata corrections are also published at
openid.net/specs/
with filenames indicating the errata number, such as openid-connect-core-1_0-errata2.html.
OpenID Working Group specifications contain:
A title.
A draft number, unless the specification is a Final Specification or a Final Specification incorporating Errata corrections.
A specification date that is current.
A list of authors and their affiliations. The affiliation may be “independent”.
A “Notices” appendix, as specified in the
OpenID Intellectual Property Rights Policy document
. The appendix starts with “Copyright (c) 2024 The OpenID Foundation.”, where “2024” is updated to be the current year.
At least these sections:
Abstract
Introduction
Security Considerations
References, with Normative References and Informative References subsections
Notices (appendix)
Acknowledgements (appendix)
History (appendix) – List of major changes made in each numbered draft (deleted from Final Specifications).
These sections are also often included:
Requirements and Notation Conventions – RFC 2119/RFC 8174 references and boilerplate.
Terminology
Implementation Considerations
Privacy Considerations
IANA Considerations (may indicate that no actions are required from IANA)
References should be to the most recent stable version of a specification. When referencing OpenID Specifications, references should always be to the versions published at
openid.net/specs/
.
Specifications must not contain:
IPR Notices for other organizations. (Use
ipr="none"
in the XML source to prevent this when using
xml2rfc
.)