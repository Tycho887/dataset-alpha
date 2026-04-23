---
{
  "title": "OpenID Attachments 1.0",
  "url": "https://openid.net/specs/openid-connect-4-ida-attachments-1_0.html",
  "domain": "openid.net",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 32406,
  "crawled_at": "2026-04-23T20:48:36"
}
---

OpenID Attachments 1.0
openid-connect-4-ida-attachments-1_0
June 2025
Lodderstedt, et al.
Standards Track
[Page]
Workgroup:
eKYC-IDA
Published:
23 June 2025
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
OpenID Attachments 1.0
Abstract
This document defines a way of representing binary data in the context of a JSON payload. It can be used as an extension of OpenID Connect that defines new attachments relating to the identity of a natural person or in other JSON contexts that have binary data elements. The work and the preceding drafts are the work of the eKYC and Identity Assurance working group of the OpenID Foundation.
¶
Introduction
This document defines an attachment element as a JWT claim for use in various contexts.
¶
Attachment element was inspired by the work done on
[
OpenID4IDA
]
and in particular how to include images of various pieces of evidence used as part of an identity assurance process. However, it is anticipated that there are other cases where the ability to embed or refer to non-JSON structured data is useful.
¶
Foreword
The OpenID Foundation (OIDF) promotes, protects and nurtures the OpenID community and technologies. As a non-profit international standardizing body, it is comprised of over 160 participating entities. The work of preparing implementer drafts and final international standards is carried out through OIDF workgroups in accordance with the OpenID Process. Participants interested in a subject for which a workgroup has been established have the right to be represented in that workgroup. International organizations, governmental and non-governmental, in liaison with OIDF, also take part in the work. OIDF collaborates closely with other standardizing bodies in the related fields.
¶
Final drafts adopted by the Workgroup through consensus are circulated publicly for the public review for 60 days and for the OIDF members for voting. Publication as an OIDF Standard requires approval by at least 50% of the members casting a vote. There is a possibility that some of the elements of this document may be subject to patent rights. OIDF shall not be held responsible for identifying any or all such patent rights.
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
This document defines how embedded and external attachments are used.
¶
2.
Normative references
See section 9 for normative references.
¶
3.
Terms and definitions
No terms and definitions are listed in this document.
¶
4.
Attachments
There are potentially a wide range of use cases where representing binary data in the context of a JSON payload might be useful. One example is when evidence is used in identity verification process, specific document artifacts (such as images of that evidence) might need to be presented and, depending on the trust framework, might need to be stored by the recipient for a period. These artifacts can then, for example, be reviewed during audit or quality control. These artifacts include, but are not limited to:
¶
scans of filled and signed forms documenting/certifying the verification process itself
¶
scans or photographs of the documents used to verify the identity of end-users
¶
video recordings of the verification process
¶
certificates of electronic signatures
¶
The intent is that this document can be referenced by any implementer or specification author where the ability to convey binary artifacts that relate to a JSON structure is useful.
¶
When using OpenID Connect and requested by the RP, these artifacts can be included as part of an ID token or UserInfo response, and in particular part of an
[
OpenID4IDA
]
verified_claims
element allowing the RP to store these artifacts along with the other
verified_claims
information.
¶
An attachment is part of JSON object. This document allows for two types, "Embedded" or "External".
¶
4.1.
Embedded attachments
All the information of the attached artifact (including the content itself) is provided within a JSON object having the following elements:
¶
desc
: Optional. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework of the OP.
¶
type
: Optional. A type identifier that indicates the type of attachment contained in the
content
element.  Values for this element should be handled as described in the section below about Predefined Values.
¶
content_type
: Required. Content (MIME) type of the document. See
[
RFC6838
]
. Multipart or message media types are not allowed. Example: "image/png"
¶
content
: Required. Base64 encoded representation of the document content. See
[
RFC4648
]
.
¶
The following example shows embedded attachments within an OpenID Connect UserInfo endpoint response. The actual contents of the attached documents are truncated:
¶
{
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "attachments": [
    {
      "desc": "Front of id document",
      "content_type": "image/png",
      "content": "Wkd0bWFtVnlhWFI2Wlc0Mk16VER2RFUyY0RRMWFUbDBNelJ1TlRjd31dzdaM1pTQXJaWGRsTXpNZ2RETmxDZwo="
    },
    {
      "desc": "Back of id document",
      "content_type": "image/png",
      "content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAADSFsjdkhjwhAABJRU5ErkJggg=="
    }
  ]
}
¶
Note: Due to their size, embedded attachments are not always appropriate when embedding in objects such as access tokens or ID Tokens.
¶
4.2.
External attachments
External attachments are similar to distributed claims as defined in
[
OpenID
]
in that the binary content is accessible as a referenced resource that is separate from the JSON object. The difference is that there are additional elements that provide more certainty that the binary object returned is the one intended when the assertion containing the attachment was created. The reference to the external attachment is provided in a JSON object with the following elements:
¶
desc
: Optional. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework or the OP.
¶
type
: Optional. A type identifier that indicates the type of attachment linked via
url
element.  Values for this element should be handled as described in the section below about Predefined Values.
¶
url
: Required. OAuth 2.0
[
RFC6749
]
protected resource endpoint from which the attachment can be retrieved. Providers shall protect this endpoint, ensuring that the attachment cannot be retrieved by unauthorized parties (typically by requiring an access token as described below). The endpoint URL shall return the attachment whose cryptographic hash matches the value given in the
digest
element. The content MIME type of the attachment shall be indicated in a content-type HTTP response header, as per
[
RFC6838
]
. Multipart or message media types shall not be used.
¶
access_token
: Optional. Access token as type
string
enabling retrieval of the attachment from a Resource server at the given
url
. The attachment shall be requested using the OAuth 2.0 Bearer Token Usage
[
RFC6750
]
protocol and the OP shall support this method, unless another token type or method has been negotiated between the OP and the client. Use of other token types is outside the scope of this document. If the
access_token
element is not available or the value of the
access_token
element is
null
then the RP shall use the access token issued by the OP in the token response, unless an alternative effective method to protect the
url
endpoint from unauthorized access has been negotiated between the OP and the client.
¶
exp
: Optional. The "exp" (expiration time) claim identifies the expiration time on or after which the external attachment will not be available from the resource endpoint defined in the
url
element (e.g. the
access_token
will expire or the document will be removed at that time). Implementers may provide for some small leeway, usually no more than a few minutes, to account for clock skew.  Its value shall be a number containing a NumericDate value as per
[
RFC7519
]
.
¶
digest
: Required. JSON object containing details of a cryptographic hash of the document content taken over the bytes of the payload (and not, e.g., the representation in the HTTP response). The JSON object has the following elements:
¶
alg
: Required. Specifies the algorithm used for the calculation of the cryptographic hash. The algorithm has been negotiated previously between RP and OP during client registration or management.
¶
value
: Required. Base64-encoded
[
RFC4648
]
bytes of the cryptographic hash.
¶
Access tokens for external attachments should be bound to the specific resource being requested so that the access token may not be used to retrieve additional external attachments or resources. For example, the value of
url
could be tied to the access token as audience. This enhances security by enabling the resource server to check whether the audience of a presented access token matches the accessed URL and reject the access when they do not match. The same idea is described in Resource Indicators for OAuth 2.0
[
RFC8707
]
, which defines the
resource
request parameter whereby to specify one or more resources which should be tied to an access token being issued.
¶
The following example shows external attachments:
¶
{
  "verified_claims": {
    "verification": {
      "trust_framework": "eidas",
      "assurance_level": "substantial",
      "evidence": [
        {
          "type": "document",
          "method": "pipp",
          "time": "2012-04-22T11:30Z",
          "document_details": {
            "type": "idcard",
            "issuer": {
              "name": "Stadt Augsburg",
              "country": "DE"
            },
            "document_number": "53554554",
            "date_of_issuance": "2010-03-23",
            "date_of_expiry": "2020-03-22"
          },
          "attachments": [
            {
              "desc": "Front of id document",
              "digest": {
                "alg": "sha-256",
                "value": "qC1zE5AfxylOFLrCnOIURXJUvnZwSFe5uUj8t6hdQVM="
              },
              "url": "https://example.com/attachments/pGL9yz4hZQ",
              "access_token": "ksj3n283dke",
              "exp": 1676552089
            },
            {
              "desc": "Back of id document",
              "digest": {
                "alg": "sha-256",
                "value": "2QcDeLJ/qeXJn4nP+v3nijMgxOBCT9WJaV0LjRS4aT8="
              },
              "url": "https://example.com/attachments/4Ag8IpOf95"
            },
            {
              "desc": "Signed document",
              "digest": {
                "alg": "sha-256",
                "value": "i3O7U79LiyKmmesIgULKT2Q8LAxNO0CpwJVcbepaYf8="
              },
              "url": "https://example.com/attachments/E67563323915",
              "access_token": null,
              "exp": 1676552189
            }
          ]
        }
      ]
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Mustermann",
      "birthdate": "1956-01-28"
    }
  }
}
¶
4.3.
External attachment validation
Clients shall validate each external attachment they wish to rely on in the following manner:
¶
Ensure that the object includes the required elements:
url
,
digest
.
¶
Ensure that, when an
exp
element is present, the request to the value in
url
is made before the time represented by the
exp
element.
¶
Ensure that the URL defined in the
url
element uses the
https
scheme.
¶
Ensure that the
digest
element contains both
alg
and
value
keys.
¶
Retrieve the attachment from the
url
element in the object.
¶
Ensure that the content MIME type of the attachment is indicated in a content-type HTTP response header
¶
Ensure that the MIME type is not multipart (see Section 5.1 of
[
RFC2046
]
)
¶
Ensure that the MIME type is not a "message" media type (see
[
RFC5322
]
)
¶
Ensure the returned attachment has a cryptographic hash digest that matches the value given in the
digest
object's
value
and algorithm defined in the value of the
alg
element.
¶
If any of these requirements are not met, do not use the content of the attachment, discard it and do not rely upon it.
¶
5.
Privacy considerations
As attachments will most likely contain more personal information than was requested by the RP with specific claim names, an OP shall ensure that the end-user is well aware of when and what kind of attachments are about to be transferred to the RP. If possible or applicable, the OP should allow the end-user to review the content of these attachments before giving consent to the transaction.
¶
6.
Security considerations
When using attachments containing personal information, implementers should choose a well tested and well-supported hashing function. Cryptographic hash functions take as input a message of arbitrary length and produce a fixed length message digest and are employed as a data integrity mechanism for non-repudiation. The OP should ensure that hash functions and algorithms used follow the recommendedations of an appropriate standards body. Lists of approved digest/hash function names and status are maintained by NIST CSRC in
[
nist_approved_hash_algorithms
]
(established in
[
FIPSSP180-4
]
and
[
FIPSSP202
]
), by ISO as established in
[
ISO10118-3
]
, and by EPC as esablished in
[
EPCCryptoAlgoUsage
]
.
¶
7.
Client registration and management
If external attachments are used in the context of an OpenID Provider that uses mechanisms such as
[
OpenID-Registration
]
or
[
RFC7592
]
to gather client details the following additional properties should be available as part of any client registration or client management interactions:
¶
digest_algorithm
: String value representing the chosen digest algorithm (for external attachments). The value shall be one of the digest algorithms supported by the OP as advertised in the
OP metadata
. If this property is not set,
sha-256
will be used by default.
¶
8.
OP metadata
If attachments are used in
[
OpenID
]
implementations, an additional element of OP Metadata is required to advertise its capabilities with respect to supported attachments in its openid-configuration (see
[
OpenID-Discovery
]
):
¶
attachments_supported
: Required when OP supports attachments. JSON array containing all attachment types supported by the OP. Possible values are
external
and
embedded
. When present, this array shall have at least one member. If omitted, the OP does not support attachments.
¶
digest_algorithms_supported
: Required when OP supports external attachments. JSON array containing all supported digest algorithms which can be used as
alg
property within the digest object of external attachments.
¶
This is an example openid-configuration snippet:
¶
{
...
  "attachments_supported": [
    "external",
    "embedded"
  ],
  "digest_algorithms_supported": [
    "sha-256"
  ],
...
}
¶
9.
Predefined values
This document focuses on the technical mechanisms to convey attachments and thus does not define any identifiers for the many attachment types. This is left to adopters of the technical specification, e.g., implementers, identity schemes, or jurisdictions.
¶
Each party defining such identifiers shall ensure the collision resistance of these identifiers. This can be achieved by including a domain name under the control of this party into the identifier name, e.g.,
https://mycompany.com/identifiers/cool_check_method
.
¶
The eKYC and Identity Assurance Working Group maintains a wiki page
[
predefined_values_page
]
that can be utilized to share predefined values with other parties and may reference any registry that emerges in the future.
¶
10.
Examples
This section contains JSON snippets showing examples of evidences and attachments described in this document.
¶
10.1.
Example requests
This section shows examples of requests for
verified_claims
.
¶
10.1.1.
Verification of claims by trust framework with a document and attachments
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": {
          "value": "de_aml"
        },
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "method": {
              "value": "pipp"
            },
            "document_details": {
              "type": {
                "values": [
                  "idcard",
                  "passport"
                ]
              }
            },
            "attachments": null
          }
        ]
      },
      "claims": {
        "given_name": null,
        "family_name": null,
        "birthdate": null
      }
    }
  }
}
¶
10.1.1.1.
Attachments
RPs can explicitly request to receive attachments along with the verified claims:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "attachments": null
      },
      "claims": {
        "given_name": null,
        "family_name": null,
        "birthdate": null
      }
    }
  }
}
¶
As with other claims, the attachment claim can be marked as
essential
in the request as well.
¶
10.2.
Example responses
This section shows examples of responses containing
verified_claims
.
¶
Note: examples of embedded attachments contain truncated values.
¶
10.2.1.
Document with external attachments
{
  "verified_claims": {
    "verification": {
      "trust_framework": "de_aml",
      "time": "2012-04-23T18:25Z",
      "verification_process": "f24c6f-6d3f-4ec5-973e-b0d8506f3bc7",
      "evidence": [
        {
          "type": "document",
          "method": "pipp",
          "time": "2012-04-22T11:30Z",
          "document_details": {
            "type": "idcard",
            "issuer": {
              "name": "Stadt Augsburg",
              "country": "DE"
            },
            "document_number": "53554554",
            "date_of_issuance": "2010-03-23",
            "date_of_expiry": "2020-03-22"
          },
          "attachments": [
            {
              "desc": "Front of id document",
              "digest" : {
                "alg": "sha-256",
                "value": "n4bQgYhMfWWaL+qgxVrQFaO/TxsrC4Is0V1sFbDwCgg="
              },
              "url": "https://example.com/attachments/pGL9yz4hZQ"
            },
            {
              "desc": "Back of id document",
              "digest" : {
                "alg": "sha-256",
                "value": "/WGgOvT3fYcPwh4F5+gGeAlcktgIz7O1wnnuBMdKyhM="
              },
              "url": "https://example.com/attachments/4Ag8IpOf95"
            }
          ]
        }
      ]
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier",
      "birthdate": "1956-01-28",
      "place_of_birth": {
        "country": "DE",
        "locality": "Musterstadt"
      },
      "nationalities": [
        "DE"
      ],
      "address": {
        "locality": "Maxstadt",
        "postal_code": "12344",
        "country": "DE",
        "street_address": "An der Weide 22"
      }
    }
  }
}
¶
10.2.2.
Utility statement with attachments
{
  "verified_claims": {
    "verification": {
      "trust_framework": "de_aml",
      "time": "2012-04-23T18:25Z",
      "verification_process": "513645-e44b-4951-942c-7091cf7d891d",
      "evidence": [
        {
          "type": "document",
          "check_details": [
            {
              "check_method": "vpip"
            }
          ],
          "time": "2021-04-09T14:12Z",
          "document_details": {
            "type": "utility_statement",
            "date_of_issuance": "2013-01-31",
            "issuer": {
              "name": "Stadtwerke Musterstadt",
              "country": "DE",
              "region": "Niedersachsen",
              "street_address": "Energiestrasse 33"
            }
          },
          "attachments": [
            {
              "desc": "scan of bill",
              "content_type": "application/pdf",
              "content": "iVBORw0KGgoAAAANSUhEUgAAAAIAAAACCAYAAABytg0kAADSFsjdkhjwhAABJRU5ErkJggg=="
            }
          ]
        }
      ]
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier",
      "birthdate": "1956-01-28",
      "place_of_birth": {
        "country": "DE",
        "locality": "Musterstadt"
      },
      "nationalities": [
        "DE"
      ],
      "address": {
        "locality": "Maxstadt",
        "postal_code": "12344",
        "country": "DE",
        "street_address": "An der Weide 22"
      }
    }
  }
}
¶
10.2.3.
Vouch with embedded attachments
{
  "verified_claims": {
    "verification": {
      "trust_framework": "uk_diatf",
      "assurance_level": "high",
      "assurance_process": {
        "policy": "gpg45",
        "procedure": "h1b"
      },
      "time": "2020-09-23T14:12Z",
      "verification_process": "99476DA2-ACDC-5N13-10WC-26B415B52",
      "evidence": [
        {
          "type": "vouch",
          "check_details": [
            {
              "check_method": "vpip"
            },
            {
              "check_method": "pvr"
            }
          ],
          "time": "2020-02-23T07:52Z",
          "attestation": {
            "type": "written_attestation",
            "reference_number": "6485-1619-3976-6671",
            "date_of_issuance": "2020-02-13",
            "voucher": {
              "given_name": "Peter",
              "family_name": "Crowe",
              "occupation": "Executive Principal",
              "organization": "Kristin School"
            }
          },
          "attachments": [
            {
              "desc": "scan of vouch",
              "content_type": "application/pdf",
              "content": "d16d2552e35582810e5a40e523716504525b6016ae96844ddc533163059b3067=="
            }
          ]
        }
      ]
    },
    "claims": {
      "given_name": "Megan",
      "family_name": "Howard",
      "birthdate": "2000-01-31",
      "place_of_birth": {
        "country": "NZL"
      },
      "address": {
        "locality": "Croydon",
        "country": "UK",
        "street_address": "69 Kidderminster Road"
      }
    }
  }
}
¶
11.
Normative References
[ISODIR2]
ISO/IEC
,
"ISO/IEC Directives, Part 2 - Principles and rules for the structure and drafting of ISO and IEC documents"
,
<
https://www.iso.org/sites/directives/current/part2/index.xhtml
>
.
[OpenID-Discovery]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
, and
E. Jay
,
"OpenID Connect Discovery 1.0 incorporating errata set 1"
,
8 November 2014
,
<
https://openid.net/specs/openid-connect-discovery-1_0.html
>
.
[OpenID-Registration]
Sakimura, N.
,
Bradley, J.
, and
M. Jones
,
"OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1"
,
8 November 2014
,
<
https://openid.net/specs/openid-connect-registration-1_0.html
>
.
[RFC6750]
Jones, M.
and
D. Hardt
,
"The OAuth 2.0 Authorization Framework: Bearer Token Usage"
,
RFC 6750
,
DOI 10.17487/RFC6750
,
October 2012
,
<
https://www.rfc-editor.org/info/rfc6750
>
.
[RFC6838]
Freed, N.
,
Klensin, J.
, and
T. Hansen
,
"Media Type Specifications and Registration Procedures"
,
BCP 13
,
RFC 6838
,
DOI 10.17487/RFC6838
,
January 2013
,
<
https://www.rfc-editor.org/info/rfc6838
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
[RFC7591]
Richer, J., Ed.
,
Jones, M.
,
Bradley, J.
,
Machulak, M.
, and
P. Hunt
,
"OAuth 2.0 Dynamic Client Registration Protocol"
,
RFC 7591
,
DOI 10.17487/RFC7591
,
July 2015
,
<
https://www.rfc-editor.org/info/rfc7591
>
.
[RFC8414]
Jones, M.
,
Sakimura, N.
, and
J. Bradley
,
"OAuth 2.0 Authorization Server Metadata"
,
RFC 8414
,
DOI 10.17487/RFC8414
,
June 2018
,
<
https://www.rfc-editor.org/info/rfc8414
>
.
[predefined_values_page]
OpenID Foundation
,
"Overview page for predefined values"
,
2021
,
<
https://openid.net/wg/ekyc-ida/identifiers/
>
.
12.
Informative References
[EPCCryptoAlgoUsage]
European Payments Council
,
"Guidelines on cryptographic algorithms usage and key management"
,
8 March 2022
,
<
https://www.europeanpaymentscouncil.eu/sites/default/files/kb/file/2022-03/EPC342-08%20v11.0%20Guidelines%20on%20Cryptographic%20Algorithms%20Usage%20and%20Key%20Management.pdf
>
.
[FIPSSP180-4]
National Institute of Standards and Technology
,
"FIPS PUB 180-4, Secure Hash Standard"
,
4 August 2015
,
<
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf
>
.
[FIPSSP202]
National Institute of Standards and Technology
,
"FIPS PUB 202, SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions"
,
4 August 2015
,
<
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.202.pdf
>
.
[IANA.OAuth.Parameters]
IANA
,
"OAuth Parameters"
,
<
https://www.iana.org/assignments/oauth-parameters
>
.
[ISO10118-3]
International Organization for Standardization
,
"ISO/IEC 10118-3:2018 IT Security techniques - Hash-functions - Part 3: Dedicated hash-functions"
,
October 2018
,
<
https://www.iso.org/obp/ui/en/#iso:std:iso-iec:10118:-3:ed-4:v1:en
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
http://openid.net/specs/openid-connect-core-1_0.html
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
http://openid.net/specs/openid-connect-4-identity-assurance-1_0.html
>
.
[RFC2046]
Freed, N.
and
N. Borenstein
,
"Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types"
,
RFC 2046
,
DOI 10.17487/RFC2046
,
November 1996
,
<
https://www.rfc-editor.org/info/rfc2046
>
.
[RFC4648]
Josefsson, S.
,
"The Base16, Base32, and Base64 Data Encodings"
,
October 2006
,
<
https://www.rfc-editor.org/info/rfc4648
>
.
[RFC5322]
Resnick, P., Ed.
,
"Internet Message Format"
,
RFC 5322
,
DOI 10.17487/RFC5322
,
October 2008
,
<
https://www.rfc-editor.org/info/rfc5322
>
.
[RFC6749]
Hardt, D.
,
"The OAuth 2.0 Authorization Framework"
,
October 2012
,
<
https://www.rfc-editor.org/info/rfc6749
>
.
[RFC7592]
Richer, J., Ed.
,
Jones, M.
,
Bradley, J.
, and
M. Machulak
,
"OAuth 2.0 Dynamic Client Registration Management Protocol"
,
RFC 7592
,
DOI 10.17487/RFC7592
,
July 2015
,
<
https://www.rfc-editor.org/info/rfc7592
>
.
[RFC8707]
Campbell, B.
,
Bradley, J.
, and
H. Tschofenig
,
"Resource Indicators for OAuth 2.0"
,
RFC 8707
,
DOI 10.17487/RFC8707
,
February 2020
,
<
https://www.rfc-editor.org/info/rfc8707
>
.
[nist_approved_hash_algorithms]
NIST
,
"NIST CSRC Approved Hash Functions"
,
September 2024
,
<
https://csrc.nist.gov/projects/hash-functions#approved-algorithms
>
.
Appendix A.
IANA Considerations
A.1.
OAuth Authorization Server Metadata Registry
This specification registers the following authorization server metadata parameters
in the IANA "OAuth Authorization Server Metadata" registry
[
IANA.OAuth.Parameters
]
established by
[
RFC8414
]
.
¶
A.1.1.
attachments_supported
Metadata Name:
attachments_supported
¶
Metadata Description: An array containing a list attachment types supported by the OP
¶
Change Controller: OpenID Foundation eKYC & IDA Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Reference:
Section 8
of this specification
¶
A.1.2.
digest_algorithms_supported
Metadata Name:
digest_algorithms_supported
¶
Metadata Description: An array containing a list of values, where each value is a string identifying a digest algorithm supported by the OP in the context of an external attachment.
¶
Change Controller: OpenID Foundation eKYC & IDA Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Reference:
Section 8
of this specification
¶
A.2.
OAuth Dynamic Client Registration Metadata Registry
This specification registers the following client metadata parameters
in the IANA "OAuth Dynamic Client Registration Metadata" registry
[
IANA.OAuth.Parameters
]
established by
[
RFC7591
]
.
¶
A.2.1.
digest_algorithm
Client Metadata Name:
digest_algorithm
¶
Client Metadata Description: An element containing a single value, where the value of the string identifies the digest algorithm chosen the client to used by the OP when presenting any external attachments
¶
Change Controller: OpenID Foundation eKYC & IDA Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Reference:
Section 7
of this specification
¶
Appendix B.
Acknowledgements
The following people at yes.com and partner companies contributed to the concept described in the initial contribution to this document: Karsten Buch, Lukas Stiebig, Sven Manz, Waldemar Zimpfer, Willi Wiedergold, Fabian Hoffmann, Daniel Keijsers, Ralf Wagner, Sebastian Ebling, Peter Eisenhofer.
¶
We would like to thank Julian White, Bjorn Hjelm, Stephane Mouy, Alberto Pulido, Joseph Heenan, Vladimir Dzhuvinov, Azusa Kikuchi, Naohiro Fujie, Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman, Michael B. Jones, Jeff Lombardo, Taylor Ongaro, Peter Bainbridge-Clayton, Adrian Field, George Fletcher, Tim Cappalli, Michael Palage, Sascha Preibisch, Giuseppe De Marco, Nick Mothershaw, Hodari McClain, Nat Sakimura and Dima Postnikov for their valuable feedback and contributions that helped to evolve this document.
¶
Appendix C.
Notices
Copyright (c) 2025 The OpenID Foundation.
¶
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer,
or other interested party a non-exclusive, royalty free, worldwide copyright license to
reproduce, prepare derivative works from, distribute, perform and display, this
Implementers Draft, Final Specification, or Final Specification Incorporating Errata
Corrections solely for the purposes of (i) developing specifications, and (ii)
implementing Implementers Drafts, Final Specifications, and Final Specification
Incorporating Errata Corrections based on such documents, provided that attribution
be made to the OIDF as the source of the material, but that such attribution does not
indicate an endorsement by the OIDF.
¶
The technology described in this specification was made available from contributions
from various sources, including members of the OpenID Foundation and others.
Although the OpenID Foundation has taken steps to help ensure that the technology
is available for distribution, it takes no position regarding the validity or scope of any
intellectual property or other rights that might be claimed to pertain to the
implementation or use of the technology described in this specification or the extent
to which any license under such rights might or might not be available; neither does it
represent that it has made any independent effort to identify any such rights. The
OpenID Foundation and the contributors to this specification make no (and hereby
expressly disclaim any) warranties (express, implied, or otherwise), including implied
warranties of merchantability, non-infringement, fitness for a particular purpose, or
title, related to this specification, and the entire risk as to implementing this
specification is assumed by the implementer. The OpenID Intellectual Property
Rights policy (found at openid.net) requires contributors to offer a patent promise not
to assert certain patent claims against other contributors and against implementers.
OpenID invites any interested party to bring to its attention any copyrights, patents,
patent applications, or other proprietary rights that may cover technology that may be
required to practice this specification.
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