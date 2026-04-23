---
{
  "title": "OpenID Connect for Identity Assurance 1.0",
  "url": "https://openid.net/specs/openid-connect-4-identity-assurance-1_0-ID4.html",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 133577,
  "crawled_at": "2026-04-23T20:52:39"
}
---

OpenID Connect for Identity Assurance 1.0
openid-connect-4-identity-assurance-1_0
August 2022
Lodderstedt, et al.
Standards Track
[Page]
Workgroup:
eKYC-IDA
Internet-Draft:
openid-connect-4-identity-assurance-1_0-13
Published:
19 August 2022
Intended Status:
Standards Track
Authors:
T. Lodderstedt
yes.com
D. Fett
yes.com
M. Haine
Considrd.Consulting Ltd
A. Pulido
Santander
K. Lehmann
1&1 Mail & Media Development & Technology GmbH
K. Koiwai
KDDI Corporation
OpenID Connect for Identity Assurance 1.0
Abstract
This specification defines an extension of OpenID Connect for providing Relying Parties with Verified Claims about End-Users. This extension facilitates the verification of the identity of a natural person.
¶
▲
Table of Contents
1.
Introduction
This specification defines an extension to OpenID Connect
[
OpenID
]
for providing Relying Parties with identity information, i.e., Verified Claims, along with an explicit statement about the verification status of these Claims (what, how, when, according to what rules, using what evidence). This specification is aimed at enabling use cases requiring strong assurance, for example, to comply with regulatory requirements such as Anti-Money Laundering laws or access to health data, risk mitigation, or fraud prevention.
¶
In such use cases, the Relying Party (RP) needs to understand the trustworthiness or assurance level of the Claims about the End-User that the OpenID Connect Provider (OP) is willing to communicate, along with process-related information and evidence used to verify the End-User Claims.
¶
The
acr
Claim, as defined in Section 2 of the OpenID Connect specification
[
OpenID
]
, is suited to assure information about the authentication performed in an OpenID Connect transaction. Identity assurance, however, requires a different representation: While authentication is an aspect of an OpenID Connect transaction, assurance is a property of a certain Claim or a group of Claims. Several of them will typically be conveyed to the RP as the result of an OpenID Connect transaction.
¶
For example, the assurance an OP typically will be able to give for an e-mail address will be "self-asserted" or "verified by opt-in or similar mechanism". The family name of an End-User, in contrast, might have been verified in accordance with the respective Anti Money Laundering Law by showing an ID Card to a trained employee of the OP operator.
¶
Identity assurance therefore requires a way to convey assurance data along with and coupled to the respective Claims about the End-User. This specification defines a suitable representation and mechanisms the RP will utilize to request Verified Claims about an End-User along with assurance data and for the OP to represent these Verified Claims and accompanying assurance data.
¶
Note: This specifications fulfills the criteria for portability and interoperability mechanisms of Digital ID systems as defined in
[
FATF-Digital-Identity
]
.
¶
1.1.
Terminology
This section defines some terms relevant to the topic covered in this document, inspired by NIST SP 800-63A
[
NIST-SP-800-63a
]
.
¶
Identity Proofing - process in which an End-User provides evidence to an OP or Claim provider reliably identifying themselves, thereby allowing the OP or Claim provider to assert that identification at a useful assurance level.
¶
Identity Verification - process conducted by the OP or a Claim provider to verify the End-User's identity.
¶
Identity Assurance - process in which the OP or a Claim provider asserts identity data of a certain End-User with a certain assurance towards an RP, typically expressed by way of an assurance level. Depending on legal requirements, the OP may also be required to provide evidence of the identity verification process to the RP.
¶
Verified Claims - Claims about an End-User, typically a natural person, whose binding to a particular End-User account was verified in the course of an identity verification process.
¶
2.
Scope
This specification defines the technical mechanisms to allow Relying Parties to request Verified Claims and to enable OpenID Providers to provide Relying Parties with Verified Claims ("the tools").
¶
Additional facets needed to deploy a complete solution for identity assurance, such as legal aspects (including liability), concrete trust frameworks, or commercial agreements are out of scope. It is up to the particular deployment to complement the technical solution based on this specification with the respective definitions ("the rules").
¶
Note: Although such aspects are out of scope, the aim of the specification is to enable implementations of the technical mechanism to be flexible enough to fulfill different legal and commercial requirements in jurisdictions around the world. Consequently, such requirements will be discussed in this specification as examples.
¶
3.
Requirements
The RP will be able to request the minimal data set it needs (data minimization) and to express requirements regarding this data, the evidence and the identity verification processes employed by the OP.
¶
This extension will be usable by OPs operating under a certain regulation related to identity assurance, such as eIDAS, as well as other OPs operating without such a regulation.
¶
It is assumed that OPs operating under a suitable regulation can assure identity data without the need to provide further evidence since they are approved to operate according to well-defined rules with clearly defined liability. For example in the case of eIDAS, the peer review ensures eIDAS compliance and the respective member state assumes the liability for the identities asserted by its notified eID systems.
¶
Every other OP not operating under such well-defined conditions may be required to provide the RP data about the identity verification process along with identity evidence to allow the RP to conduct their own risk assessment and to map the data obtained from the OP to other laws. For example, if an OP verifies and maintains identity data in accordance with an Anti Money Laundering Law, it shall be possible for an RP to use the respective identity in a different regulatory context, such as eHealth or the previously mentioned eIDAS.
¶
The basic idea of this specification is that the OP provides all identity data along with metadata about the identity verification process at the OP. It is the responsibility of the RP to assess this data and map it into its own legal context.
¶
From a technical perspective, this means this specification allows the OP to provide Verified Claims along with information about the respective trust framework, but also supports the externalization of information about the identity verification process.
¶
The representation defined in this specification can be used to provide RPs with Verified Claims about the End-User via any appropriate channel. In the context of OpenID Connnect, Verified Claims can be provided in ID Tokens or as part of the UserInfo response. It is also possible to utilize the format described here in OAuth Access Tokens or Token Introspection responses to provide resource servers with Verified Claims.
¶
This extension is intended to be truly international and support identity assurance across different jurisdictions. The extension is therefore extensible to support various trust frameworks, identity evidence and assurance processes.
¶
In order to give implementors as much flexibility as possible, this extension can be used in conjunction with existing OpenID Connect Claims and other extensions within the same OpenID Connect assertion (e.g., ID Token or UserInfo response) utilized to convey Claims about End-Users.
¶
For example, OpenID Connect
[
OpenID
]
defines Claims for representing family name and given name of an End-User without a verification status. These Claims can be used in the same OpenID Connect assertion beside Verified Claims represented according to this extension.
¶
In the same way, existing Claims to inform the RP of the verification status of the
phone_number
and
email
Claims can be used together with this extension.
¶
Even for representing Verified Claims, this extension utilizes existing OpenID Connect Claims if possible and reasonable. The extension will, however, ensure RPs cannot (accidentally) interpret unverified Claims as Verified Claims.
¶
4.
Claims
4.1.
Additional Claims about End-Users
In order to fulfill the requirements of some jurisdictions on identity assurance, this specification defines the following Claims for conveying End-User data in addition to the Claims defined in the OpenID Connect specification
[
OpenID
]
:
¶
Table 1
Claim
Type
Description
place_of_birth
JSON object
End-User's place of birth. The value of this member is a JSON structure containing some or all of the following members:
country
: String representing country in
[
ISO3166-1
]
Alpha-2 (e.g., DE) or
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
End-User's nationalities using ICAO 3-letter codes
[
ICAO-Doc9303
]
, e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
birth_family_name
string
End-User's family name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the family name later in life for any reason. Note that in some cultures, people can have multiple family names or no family name; all can be present, with the names being separated by space characters.
birth_given_name
string
End-User's given name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the given name later in life for any reason. Note that in some cultures, people can have multiple given names; all can be present, with the names being separated by space characters.
birth_middle_name
string
End-User's middle name(s) when they were born, or at least from the time they were a child. This term can be used by a person who changes the middle name later in life for any reason. Note that in some cultures, people can have multiple middle names; all can be present, with the names being separated by space characters. Also note that in some cultures, middle names are not used.
salutation
string
End-User's salutation, e.g., "Mr."
title
string
End-User's title, e.g., "Dr."
msisdn
string
End-User's mobile phone number formatted according to ITU-T recommendation
[
E.164
]
, e.g., "1999550123"
also_known_as
string
Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides its legal name. This must be part of the applicable legislation and thus the trust framework (e.g., be an attribute on the identity card).
4.2.
txn Claim
Strong identity verification typically requires the participants to keep an audit trail of the whole process.
¶
The
txn
Claim as defined in
[
RFC8417
]
is used in the context of this extension to build audit trails across the parties involved in an OpenID Connect transaction.
¶
If the OP issues a
txn
, it MUST maintain a corresponding audit trail, which at least consists of the following details:
¶
the transaction ID,
¶
the authentication method employed, and
¶
the transaction type (e.g., the set of Claims returned).
¶
This transaction data MUST be stored as long as it is required to store transaction data for auditing purposes by the respective regulation.
¶
The RP requests this Claim like any other Claim via the
claims
parameter or as part of a default Claim set identified by a scope value.
¶
The
txn
value MUST allow an RP to obtain these transaction details if needed.
¶
Note: The mechanism to obtain the transaction details from the OP and their format is out of scope of this specification.
¶
4.3.
Extended address Claim
This specification extends the
address
Claim as defined in
[
OpenID
]
by another sub field containing the country as ISO code.
¶
country_code
: OPTIONAL. country part of an address represented using an ISO 3-letter code
[
ISO3166-3
]
, e.g., "USA" or "JPN". 2-letter ISO codes
[
ISO3166-1
]
MAY be used for compatibility reasons.
country_code
MAY be used as alternative to the existing
country
field.
¶
5.
Representing Verified Claims
This specification defines a generic mechanism to add Verified Claims to JSON-based assertions. The basic idea is to use a container element, called
verified_claims
, to provide the RP with a set of Claims along with the respective metadata and verification evidence related to the verification of these Claims. This way, RPs cannot mix up Verified Claims and unverified Claims and accidentally process unverified Claims as Verified Claims.
¶
The following example would assert to the RP that the OP has verified the Claims provided (
given_name
and
family_name
) according to an example trust framework
trust_framework_example
:
¶
{
  "verified_claims": {
    "verification": {
      "trust_framework": "trust_framework_example"
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier"
    }
  }
}
¶
The normative definition is given in the following.
¶
verified_claims
: A single object or an array of objects, each object comprising the following sub-elements:
¶
verification
: REQUIRED. Object that contains data about the verification process.
¶
claims
: REQUIRED. Object that is the container for the Verified Claims about the End-User.
¶
Note: Implementations MUST ignore any sub-element not defined in this specification or extensions of this specification. Extensions to this specification that specify additional sub-elements under the
verified_claims
element MAY be created by the OpenID Foundation, ecosystem or scheme operators or indeed singular OpenID Connect for IDA implementers.
¶
A machine-readable syntax definition of
verified_claims
is given as JSON schema in
[
verified_claims.json
]
, it can be used to automatically validate JSON documents containing a
verified_claims
element. The provided JSON schema files are a non-normative implementation of this specification and any discrepancies that exist are either implementation bugs or interpretations.
¶
Extensions of this specification, including trust framework definitions, can define further constraints on the data structure.
¶
5.1.
verification Element
This element contains the information about the process conducted to verify a person's identity and bind the respective person data to a user account.
¶
The
verification
element consists of the following elements:
¶
trust_framework
: REQUIRED. String determining the trust framework governing the identity verification process of the OP.
¶
An example value is
eidas
, which denotes a notified eID system under eIDAS
[
eIDAS
]
.
¶
RPs SHOULD ignore
verified_claims
Claims containing a trust framework identifier they do not understand.
¶
The
trust_framework
value determines what further data is provided to the RP in the
verification
element. A notified eID system under eIDAS, for example, would not need to provide any further data whereas an OP not governed by eIDAS would need to provide verification evidence in order to allow the RP to fulfill its legal obligations. An example of the latter is an OP acting under the German Anti-Money Laundering Law (
de_aml
).
¶
assurance_level
: OPTIONAL. String determining the assurance level associated with the End-User Claims in the respective
verified_claims
. The value range depends on the respective
trust_framework
value.
¶
For example, the trust framework
eidas
can have the identity assurance levels
low
,
substantial
and
high
.
¶
For information on predefined trust framework and assurance level values see
Section 14
.
¶
assurance_process
: OPTIONAL. JSON object representing the assurance process that was followed. This reflects how the evidence meets the requirements of the
trust_framework
and
assurance_level
. The factual record of the evidence and the procedures followed are recorded in the
evidence
element, this element is used to cross reference the
evidence
to the
assurance_process
followed. This has one or more of the following sub-elements:
¶
policy
: OPTIONAL. String representing the standard or policy that was followed.
¶
procedure
: OPTIONAL. String representing a specific procedure from the
policy
that was followed.
¶
assurance_details
: OPTIONAL. JSON array denoting the details about how the evidence complies with the
policy
. When present this array MUST have at least one member. Each member can have the following sub-elements:
¶
assurance_type
: OPTIONAL. String denoting which part of the
assurance_process
the evidence fulfils.
¶
assurance_classification
: OPTIONAL. String reflecting how the
evidence
has been classified or measured as required by the
trust_framework
.
¶
evidence_ref
: OPTIONAL. JSON array of the evidence being referred to. When present this array MUST have at least one member.
¶
txn
: REQUIRED. Identifier referring to the
txn
used in the
check_details
. The OP MUST ensure that
txn
is present in the
check_details
when
evidence_ref
element is used.
¶
evidence_metadata
: OPTIONAL. Object indicating any meta data about the
evidence
that is required by the
assurance_process
in order to demonstrate compliance with the
trust_framework
. It has the following sub-elements:
¶
evidence_classification
: OPTIONAL. String indicating how the process demonstrated by the
check_details
for the
evidence
is classified by the
assurance_process
in order to demonstrate compliance with the
trust_framework
.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date and time when the identity verification process took place. This time might deviate from (a potentially also present)
document/time
element since the latter represents the time when a certain evidence was checked whereas this element represents the time when the process was completed. Moreover, the overall verification process and evidence verification can be conducted by different parties (see
document/verifier
). Presence of this element might be required for certain trust frameworks.
¶
verification_process
: OPTIONAL. Unique reference to the identity verification process as performed by the OP. Used for identifying and retrieving details in case of disputes or audits. Presence of this element might be required for certain trust frameworks.
¶
Note: While
verification_process
refers to the identity verification process at the OP, the
txn
Claim refers to a particular OpenID Connect transaction in which the OP provided the End-User's verified identity data towards an RP.
¶
evidence
: OPTIONAL. JSON array containing information about the evidence the OP used to verify the End-User's identity as separate JSON objects. Every object contains the property
type
which determines the type of the evidence. The RP uses this information to process the
evidence
property appropriately.
¶
Important: Implementations MUST ignore any sub-element not defined in this specification or extensions of this specification.
¶
5.1.1.
evidence Element
The
evidence
element is structured with the following elements:
¶
attachments
: OPTIONAL. Array of JSON objects representing attachments like photocopies of documents or certificates. See
Section 5.1.2
on how an attachment is structured.
¶
type
: REQUIRED. The value defines the type of the evidence.
¶
The following types of evidence are defined:
¶
document
: Verification based on any kind of physical or electronic document provided by the End-User.
¶
electronic_record
: Verification based on data or information obtained electronically from an approved or recognized source.
¶
vouch
: Verification based on an attestation or reference given by an approved or recognized person declaring they believe to the best of their knowledge that the Claim(s) are genuine and true.
¶
utility_bill
: Verification based on a utility bill (this is to be deprecated in future releases and implementers are recommended to use the
document
type instead).
¶
electronic_signature
: Verification based on an electronic signature.
¶
Note:
id_document
is an alias for
document
for backward compatibility purposes but will be deprecated in future releases, implementers are recommended to use
document
.
¶
Depending on the evidence type additional elements are defined, as described in the following.
¶
5.1.1.1.
Evidence Type document
The following elements are contained in an evidence sub-element where type is
document
.
¶
type
: REQUIRED. Value MUST be set to
document
.
¶
check_details
: OPTIONAL. JSON array representing the checks done in relation to the
evidence
. When present this array MUST have at least one member.
¶
check_method
: REQUIRED. String representing the check done, this includes processes such as checking the authenticity of the document, or verifying the user's biometric against an identity document. For information on predefined
check_details
values see
Section 14
.
¶
organization
: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
¶
txn
: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when
evidence_ref
element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when the check was completed.
¶
method
: OPTIONAL. The method used to validate the document and verify the person is the owner of it. In practice this is a combination of a several instances
check_details
, implementers are recommended to use the
check_details
type and deprecate the use of this option unless methods are defined by the trust framework. For information on predefined method values see
Section 14
.
¶
verifier
: OPTIONAL. JSON object denoting the legal entity that performed the identity verification. This object SHOULD be included if the OP did not perform the identity verification itself. This object is retained for backward compatibility, implementers are recommended to use
check_details
&
organization
instead. This object consists of the following properties:
¶
organization
: REQUIRED. String denoting the organization which performed the verification on behalf of the OP.
¶
txn
: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when this document was verified.
¶
document_details
: OPTIONAL. JSON object representing the document used to perform the identity verification. Note:
document
can be used as an alias for
document_details
for backward compatibility purposes but will be deprecated in future releases, implementers are recommended to use
document_details
. It consists of the following properties:
¶
type
: REQUIRED. String denoting the type of the document. For information on predefined document values see
Section 14
. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
¶
document_number
: OPTIONAL. String representing an identifier/number that uniquely identifies a document that was issued to the End-User. This is used on one document and will change if it is reissued, e.g., a passport number, certificate number, etc. Note:
number
can be used as an alias for 'document_number' for backward compatibility purposes but will be deprecated in future releases, implementers are recommended to use
document_number
.
¶
personal_number
: OPTIONAL. String representing an identifier that is assigned to the End-User and is not limited to being used in one document, for example a national identification number, personal identity number, citizen number, social security number, driver number, account number, customer number, licensee number, etc.
¶
serial_number
: OPTIONAL. String representing an identifier/number that identifies the document irrespective of any personalization information (this usually only applies to physical artifacts and is present before personalization).
¶
date_of_issuance
: OPTIONAL. The date the document was issued as ISO 8601
[
ISO8601
]
YYYY-MM-DD
format.
¶
date_of_expiry
: OPTIONAL. The date the document will expire as ISO 8601
[
ISO8601
]
YYYY-MM-DD
format.
¶
issuer
: OPTIONAL. JSON object containing information about the issuer of this document. This object consists of the following properties:
¶
name
: OPTIONAL. Designation of the issuer of the document.
¶
All elements of the OpenID Connect
address
Claim (see
[
OpenID
]
)
¶
country_code
: OPTIONAL. String denoting the country or supranational organization that issued the document as ISO 3166/ICAO 3-letter codes
[
ICAO-Doc9303
]
, e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
¶
jurisdiction
: OPTIONAL. String containing the name of the region(s)/state(s)/province(s)/municipality(ies) that issuer has jurisdiction over (if this information is not common knowledge or derivable from the address).
¶
5.1.1.2.
Evidence Type electronic_record
The following elements are contained in an evidence sub-element where type is
electronic_record
.
¶
type
: REQUIRED. Value MUST be set to
electronic_record
.
¶
check_details
: OPTIONAL. JSON array representing the checks done in relation to the
evidence
.
¶
check_method
: REQUIRED. String representing the check done. For information on predefined
check_method
values see
Section 14
.
¶
organization
: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
¶
txn
: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when
evidence_ref
element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when the check was completed.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when this record was verified.
¶
record
: OPTIONAL. JSON object representing the record used to perform the identity verification. It consists of the following properties:
¶
type
: REQUIRED. String denoting the type of electronic record. For information on predefined identity evidence values see
Section 14
. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
¶
personal_number
: OPTIONAL. String representing an identifier that is assigned to the End-User and is not limited to being used in one record, for example a national identification number, personal identity number, citizen number, social security number, driver number, account number, customer number, licensee number, etc.
¶
created_at
: OPTIONAL. The time the record was created as ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format.
¶
date_of_expiry
: OPTIONAL. The date the evidence will expire as ISO 8601
[
ISO8601
]
YYYY-MM-DD
format.
¶
source
: OPTIONAL. JSON object containing information about the source of this record. This object consists of the following properties:
¶
name
: OPTIONAL. Designation of the source of the electronic_record.
¶
All elements of the OpenID Connect
address
Claim (see
[
OpenID
]
): OPTIONAL.
¶
country_code
: OPTIONAL. String denoting the country or supranational organization that issued the evidence as ISO 3166/ICAO 3-letter codes
[
ICAO-Doc9303
]
, e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
¶
jurisdiction
: OPTIONAL. String containing the name of the region(s) / state(s) / province(s) / municipality(ies) that source has jurisdiction over (if it's not common knowledge or derivable from the address).
¶
5.1.1.3.
Evidence Type vouch
The following elements are contained in an evidence sub-element where type is
vouch
.
¶
type
: REQUIRED. Value MUST be set to
vouch
.
¶
check_details
: OPTIONAL. JSON array representing the checks done in relation to the
vouch
.
¶
check_method
: REQUIRED. String representing the check done, this includes processes such as checking the authenticity of the vouch, or verifing the user as the person referenced in the vouch. For information on predefined
check_method
values see
Section 14
.
¶
organization
: OPTIONAL. String denoting the legal entity that performed the check. This  SHOULD be included if the OP did not perform the check itself.
¶
txn
: OPTIONAL. Identifier referring to the identity verification transaction. The OP MUST ensure that this is present when
evidence_ref
element is used. The OP MUST ensure that the transaction identifier can be resolved into transaction details during an audit.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when the check was completed.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when this vouch was verified.
¶
attestation
: OPTIONAL. JSON object representing the attestation that is the basis of the vouch. It consists of the following properties:
¶
type
: REQUIRED. String denoting the type of vouch. For information on predefined vouch values see
Section 14
. The OP MAY use other than the predefined values in which case the RPs will either be unable to process the assertion, just store this value for audit purposes, or apply bespoken business logic to it.
¶
reference_number
: OPTIONAL. String representing an identifier/number that uniquely identifies a vouch given about the End-User.
¶
personal_number
: OPTIONAL. String representing an identifier that is assigned to the End-User and is not limited to being used in one document, for example a national identification number, personal identity number, citizen number, social security number, driver number, account number, customer number, licensee number, etc.
¶
date_of_issuance
: OPTIONAL. The date the vouch was made as ISO 8601
[
ISO8601
]
YYYY-MM-DD
format.
¶
date_of_expiry
: OPTIONAL. The date the evidence will expire as ISO 8601
[
ISO8601
]
YYYY-MM-DD
format.
¶
voucher
: OPTIONAL. JSON object containing information about the entity giving the vouch. This object consists of the following properties:
¶
name
: OPTIONAL. String containing the name of the person giving the vouch/reference in the same format as defined in Section 5.1 (Standard Claims) of the OpenID Connect Core specification.
¶
birthdate
: OPTIONAL. String containing the birthdate of the person giving the vouch/reference in the same format as defined in Section 5.1 (Standard Claims) of the OpenID Connect Core specification.
¶
All elements of the OpenID Connect
address
Claim (see
[
OpenID
]
): OPTIONAL.
¶
country_code
: OPTIONAL. String denoting the country or supranational organization that issued the evidence as ISO 3166/ICAO 3-letter codes
[
ICAO-Doc9303
]
, e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
¶
occupation
: OPTIONAL. String containing the occupation or other authority of the person giving the vouch/reference.
¶
organization
: OPTIONAL. String containing the name of the organization the voucher is representing.
¶
5.1.1.4.
Evidence Type utility_bill
Note: This type is to be deprecated in future releases. Implementers are recommended to use
document
instead.
¶
The following elements are contained in an evidence sub-element where type is
utility_bill
.
¶
type
: REQUIRED. Value MUST be set to "utility_bill".
¶
provider
: OPTIONAL. JSON object identifying the respective provider that issued the bill. The object consists of the following properties:
¶
name
: REQUIRED. String designating the provider.
¶
All elements of the OpenID Connect
address
Claim (see
[
OpenID
]
)
¶
country_code
: OPTIONAL. String denoting the country or supranational organization that issued the evidence as ISO 3166/ICAO 3-letter codes
[
ICAO-Doc9303
]
, e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
¶
date
: OPTIONAL. String in ISO 8601
[
ISO8601
]
YYYY-MM-DD
format containing the date when this bill was issued.
¶
method
: OPTIONAL. The method used to verify the utility bill. For information on predefined method values see
Section 14
.
¶
time
: OPTIONAL. Time stamp in ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format representing the date when the utility bill was verified.
¶
5.1.1.5.
Evidence Type electronic_signature
The following elements are contained in a
electronic_signature
evidence sub-element.
¶
type
: REQUIRED. Value MUST be set to
electronic_signature
.
¶
signature_type
: REQUIRED. String denoting the type of signature used as evidence. The value range might be restricted by the respective trust framework.
¶
issuer
: REQUIRED. String denoting the certification authority that issued the signer's certificate.
¶
serial_number
: REQUIRED. String containing the serial number of the certificate used to sign.
¶
created_at
: OPTIONAL. The time the signature was created as ISO 8601
[
ISO8601
]
YYYY-MM-DDThh:mm[:ss]TZD
format.
¶
5.1.2.
Attachments
During the identity verification process, specific document artifacts will be created and depending on the trust framework, will be required to be stored for a specific duration. These artifacts can later be reviewed during audits or quality control for example. These artifacts include, but are not limited to:
¶
scans of filled and signed forms documenting/certifying the verification process itself,
¶
scans or photocopies of the documents used to verify the identity of End-Users,
¶
video recordings of the verification process,
¶
certificates of electronic signatures.
¶
When requested by the RP, these artifacts can be attached to the Verified Claims response allowing the RP to store these artifacts along with the Verified Claims information.
¶
An attachment is represented by a JSON object. This specification allows two types of representations:
¶
5.1.2.1.
Embedded Attachments
All the information of the document (including the content itself) is provided within a JSON object having the following elements:
¶
desc
: OPTIONAL. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework of the OP.
¶
content_type
: REQUIRED. Content (MIME) type of the document. See
[
RFC6838
]
. Multipart or message media types are not allowed. Example: "image/png"
¶
content
: REQUIRED. Base64 encoded representation of the document content.
¶
txn
: OPTIONAL. Identifier referring to the transaction. The OP SHOULD ensure this matches a
txn
contained within
check_method
when
check_method
needs to reference the embedded attachment.
¶
The following example shows embedded attachments. The actual contents of the documents are truncated:
¶
{
  "verified_claims": {
    "verification": {
      "trust_framework":"eidas",
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
Note: Due to their size, embedded attachments are not appropriate when embedding Verified Claims in Access Tokens or ID Tokens.
¶
5.1.2.2.
External Attachments
External attachments are similar to distributed Claims. The reference to the external document is provided in a JSON object with the following elements:
¶
desc
: OPTIONAL. Description of the document. This can be the filename or just an explanation of the content. The used language is not specified, but is usually bound to the jurisdiction of the underlying trust framework or the OP.
¶
url
: REQUIRED. OAuth 2.0 resource endpoint from which the document can be retrieved. Providers MUST protect this endpoint. The endpoint URL MUST return the document whose cryptographic hash matches the value given in the
digest
element. The content MIME type of the document must be indicated in a content-type HTTP response header, as per
RFC6838
. Multipart or message media types SHALL NOT be used.
¶
access_token
: OPTIONAL. Access Token as type
string
enabling retrieval of the document from the given
url
. The attachment MUST be requested using the OAuth 2.0 Bearer Token Usage
[
RFC6750
]
protocol and the OP MUST support this method, unless another Token Type or method has been negotiated with the Client. Use of other Token Types is outside the scope of this specification. If the
access_token
element is not available, RPs MUST use the Access Token issued by the OP in the Token response and when requesting the attachment the RP MUST use the same method as when accessing the UserInfo endpoint. If the value of this element is
null
, no Access Token is used to request the attachment and the RP MUST NOT use the Access Token issued by the Token response. In this case the OP MUST incorporate other effective methods to protect the attachment and inform/instruct the RP accordingly.
¶
expires_in
: OPTIONAL. Positive integer representing the number of seconds until the attachment becomes unavailable and/or the provided
access_token
becomes invalid.
¶
digest
: REQUIRED. JSON object representing a cryptographic hash of the document content. The JSON object has the following elements:
¶
alg
: REQUIRED. Specifies the algorithm used for the calculation of the cryptographic hash. The algorithm has been negotiated previously between RP and OP during Client Registration or Management.
¶
value
: REQUIRED. Base64 encoded representation of the cryptographic hash.
¶
txn
: OPTIONAL. Identifier referring to the transaction. The OP SHOULD ensure this matches a
txn
contained within
check_method
when
check_method
needs to reference the embedded attachment.
¶
External attachments are suitable when embedding Verified Claims in Tokens. However, the
verified_claims
element is not self-contained. The documents need to be retrieved separately, and the digest values MUST be calculated and validated to ensure integrity.
¶
It is RECOMMENDED that access tokens for external attachments have a binding to the specific resource being requested so that the access token may not be used to retrieve additional external attachments or resources. For example, the value of
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
      "trust_framework":"eidas",
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
              "expires_in": 30
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
              "url": "https://example.com/attachments/4Ag8IpOf95",
              "access_token": null,
              "expires_in": 30
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
5.1.2.3.
Privacy Considerations
As attachments will most likely contain more personal information than was requested by the RP with specific Claim names, an OP MUST ensure that the End-User is well aware of when and what kind of attachments are about to be transferred to the RP. If possible or applicable, the OP SHOULD allow the End-User to review the content of these attachments before giving consent to the transaction.
¶
5.2.
claims Element
The
claims
element contains the Claims about the End-User which were verified by the process and according to the policies determined by the corresponding
verification
element.
¶
The
claims
element MAY contain one or more of the following Claims as defined in Section 5.1 of the OpenID Connect specification
[
OpenID
]
¶
name
¶
given_name
¶
middle_name
¶
family_name
¶
birthdate
¶
address
¶
and the Claims defined in
Section 4.1
.
¶
The
claims
element MAY also contain other Claims provided the value of the respective Claim was verified in the verification process represented by the sibling
verification
element.
¶
Claim names MAY be annotated with language tags as specified in Section 5.2 of the OpenID Connect specification
[
OpenID
]
.
¶
5.3.
verified_claims Delivery
OPs can deliver
verified_claims
in various ways.
¶
A
verified_claims
element can be added to an OpenID Connect UserInfo response or an ID Token.
¶
OAuth Authorization Servers can add
verified_claims
to Access Tokens in JWT format or Token Introspection responses, either in plain JSON or JWT-protected format.
¶
Here is an example of the payload of an Access Token in JWT format including Verified Claims:
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761",
  "aud": "https://rs.example.com/",
  "exp": 1544645174,
  "client_id": "s6BhdRkqt3_",
  "verified_claims": {
    "verification": {
      "trust_framework": "example"
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Mustermann"
    }
  }
}
¶
An OP or AS MAY also include
verified_claims
in the above assertions, whether they are Access Tokens or in Token Introspection responses, as aggregated or distributed claims (see Section 5.6.2 of the OpenID Connect specification
[
OpenID
]
).
¶
For aggregated or distributed claims, every assertion provided by the external Claims source MUST contain:
¶
an
iss
Claim identifying the claims source,
¶
a
sub
Claim identifying the End-User in the context of the claim source,
¶
a
verified_claims
element containing one or more
verified_claims
objects.
¶
The
verified_claims
element in an aggregated or distributed claims object MUST have one of the following forms:
¶
a JSON string referring to a certain claim source (as defined in
[
OpenID
]
)
¶
a JSON array of strings referring to the different claim sources
¶
a JSON object composed of sub-elements formatted with the syntax as defined for requesting
verified_claims
where the name of each object is a name for the respective claim source. Every such named object contains sub-objects called
claims
and
verification
expressing data provided by the respective claims source. This allows the RP to look ahead before it actually requests distributed Claims in order to prevent extra time, cost, data collisions, etc. caused by these requests.
¶
Note: The two later forms extend the syntax as defined in Section 5.6.2 of the OpenID Connect specification
[
OpenID
]
) in order to accommodate the specific use cases for
verified_claims
.
¶
The following are examples of assertions including Verified Claims as aggregated Claims
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "_claim_names": {
    "verified_claims": "src1"
  },
  "_claim_sources": {
    "src1": {
      "JWT": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlcnZlci5vdGhlcm9wLmNvbSIsInN1YiI6ImU4MTQ4NjAzLTg5MzQtNDI0NS04MjViLWMxMDhiOGI2Yjk0NSIsInZlcmlmaWVkX2NsYWltcyI6eyJ2ZXJpZmljYXRpb24iOnsidHJ1c3RfZnJhbWV3b3JrIjoiaWFsX2V4YW1wbGVfZ29sZCJ9LCJjbGFpbXMiOnsiZ2l2ZW5fbmFtZSI6Ik1heCIsImZhbWlseV9uYW1lIjoiTWVpZXIiLCJiaXJ0aGRhdGUiOiIxOTU2LTAxLTI4In19fQ.FArlPUtUVn95HCExePlWJQ6ctVfVpQyeSbe3xkH9MH1QJjnk5GVbBW0qe1b7R3lE-8iVv__0mhRTUI5lcFhLjoGjDS8zgWSarVsEEjwBK7WD3r9cEw6ZAhfEkhHL9eqAaED2rhhDbHD5dZWXkJCuXIcn65g6rryiBanxlXK0ZmcK4fD9HV9MFduk0LRG_p4yocMaFvVkqawat5NV9QQ3ij7UBr3G7A4FojcKEkoJKScdGoozir8m5XD83Sn45_79nCcgWSnCX2QTukL8NywIItu_K48cjHiAGXXSzydDm_ccGCe0sY-Ai2-iFFuQo2PtfuK2SqPPmAZJxEFrFoLY4g"
    }
  }
}
¶
and distributed Claims.
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "_claim_names": {
    "verified_claims": "src1"
  },
  "_claim_sources": {
    "src1": {
      "endpoint": "https://server.yetanotherop.com/claim_source",
      "access_token": "ksj3n283dkeafb76cdef"
    }
  }
}
¶
The following example shows an ID Token containing
verified_claims
from two different external claim sources, one as aggregated and the other as distributed Claims.
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "_claim_names": {
    "verified_claims": [
      "src1",
      "src2"
    ]
  },
  "_claim_sources": {
    "src1": {
      "JWT": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlcnZlci5vdGhlcm9wLmNvbSIsInN1YiI6ImU4MTQ4NjAzLTg5MzQtNDI0NS04MjViLWMxMDhiOGI2Yjk0NSIsInZlcmlmaWVkX2NsYWltcyI6eyJ2ZXJpZmljYXRpb24iOnsidHJ1c3RfZnJhbWV3b3JrIjoiaWFsX2V4YW1wbGVfZ29sZCJ9LCJjbGFpbXMiOnsiZ2l2ZW5fbmFtZSI6Ik1heCIsImZhbWlseV9uYW1lIjoiTWVpZXIiLCJiaXJ0aGRhdGUiOiIxOTU2LTAxLTI4In19fQ.FArlPUtUVn95HCExePlWJQ6ctVfVpQyeSbe3xkH9MH1QJjnk5GVbBW0qe1b7R3lE-8iVv__0mhRTUI5lcFhLjoGjDS8zgWSarVsEEjwBK7WD3r9cEw6ZAhfEkhHL9eqAaED2rhhDbHD5dZWXkJCuXIcn65g6rryiBanxlXK0ZmcK4fD9HV9MFduk0LRG_p4yocMaFvVkqawat5NV9QQ3ij7UBr3G7A4FojcKEkoJKScdGoozir8m5XD83Sn45_79nCcgWSnCX2QTukL8NywIItu_K48cjHiAGXXSzydDm_ccGCe0sY-Ai2-iFFuQo2PtfuK2SqPPmAZJxEFrFoLY4g"
    },
    "src2": {
      "endpoint": "https://server.yetanotherop.com/claim_source",
      "access_token": "ksj3n283dkeafb76cdef"
    }
  }
}
¶
The next example shows an ID Token containing
verified_claims
from two different external claim sources along with additional data about the content of the Verified Claims (look ahead).
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "_claim_names": {
    "verified_claims": {
      "src1": {
        "verification": {
          "trust_framework": {
            "value": "grids_kyb"
          },
          "evidence": [
            {
              "type": {
                "value": "document"
              },
              "registry": {
                "country": {
                  "essential": true,
                  "purpose": "string",
                  "value": "ES"
                }
              },
              "document": {
                "SKU": {
                  "value": "REX"
                }
              }
            }
          ]
        },
        "claims": {
          "legal_name": null,
          "legal_person_identifier": null,
          "lei": null,
          "vat_registration": null,
          "address": null,
          "tax_reference": null,
          "sic": null,
          "business_role": null,
          "sub_jurisdiction": null,
          "trading_status": null
        }
      },
      "src2": {
        "verification": {
          "trust_framework": {
            "value": "grids_kyb"
          },
          "evidence": [
            {
              "type": {
                "value": "document"
              },
              "registry": {
                "country": {
                  "essential": true,
                  "purpose": "string",
                  "value": "ES"
                }
              },
              "document": {
                "SKU": {
                  "value": "REX"
                }
              }
            }
          ]
        },
        "claims": {
          "legal_name": null,
          "legal_person_identifier": null,
          "sic": null,
          "business_role": null,
          "sub_jurisdiction": null,
          "trading_status": null
        }
      }
    }
  },
  "_claim_sources": {
    "src1": {
      "JWT": "eyJhbGciOiJIUzI1NiJ9.eyJhdF9yZWdpc3RyYXRpb24iOiIxMjM0NTQzMjEiLCJsZWkiOiIwOTg3NjU0MzIxIiwiYWRkcmVzcyI6IjEgdGhlIHN0cmVldCwgQmFyY2Vsb25hLCBTcGFpbiIsImJ1c2luZXNzX3JvbGUiOiJuL2EiLCJ0YXhfcmVmZXJlbmNlIjoiMDk4NzY1Njc4OTAiLCJsZWdhbF9uYW1lIjoiYWNtZSBsdGQiLCJzdWJfanVyaXNkaWN0aW9uIjoibi9hIiwidHJhZGluZ19zdGF0dXMiOiJhY3RpdmUiLCJzaWMiOiIwMDAwIiwibGVnYWxfcGVyc29uX2lkZW50aWZpZXIiOiIxMjM0NTY3ODkwIn0.9KMvagQjIlOLVxI9n4S0jIga9cQcWNx106b8kzHhTYU"
    },
    "src2": {
      "endpoint": "https://server.yetanotherop.com/claim_source",
      "access_token": "ksj3n283dkeafb76cdef"
    }
  }
}
¶
Claim sources SHOULD sign the assertions containing
verified_claims
in order to demonstrate authenticity and provide for non-repudiation.
The recommended way for an RP to determine the key material used for validation of the signed assertions is via the claim source's public keys. These keys SHOULD be available in the JSON Web Key Set available in the
jwks_uri
metadata value in the
openid-configuration
metadata document. This document can be discovered using the
iss
Claim of the particular JWT.
¶
The OP MAY combine aggregated and distributed Claims with
verified_claims
provided by itself (see
Section 8.16
).
¶
If
verified_claims
elements are contained in multiple places of a response, e.g., in the ID Token and an embedded aggregated Claim, the RP MUST preserve the claims source as context of the particular
verified_claims
element.
¶
Note: Any assertion provided by an OP or AS including aggregated or distributed Claims MAY contain multiple instances of the same End-User Claim. It is up to the RP to decide how to process these different instances.
¶
6.
Requesting Verified Claims
Making a request for Verified Claims and related verification data can be explicitly requested on the level of individual data elements by utilizing the
claims
parameter as defined in Section 5.5 of the OpenID Connect specification
[
OpenID
]
.
¶
It is also possible to use the
scope
parameter to request one or more specific pre-defined Claim sets as defined in Section 5.4 of the OpenID Connect specification
[
OpenID
]
.
¶
Note: The OP MUST NOT provide the RP with any data it did not request. However, the OP MAY at its discretion omit Claims from the response.
¶
6.1.
Requesting End-User Claims
Verified Claims can be requested on the level of individual Claims about the End-User by utilizing the
claims
parameter as defined in Section 5.5 of the OpenID Connect specification
[
OpenID
]
.
¶
Note: A machine-readable definition of the syntax to be used to request
verified_claims
is given as JSON schema in
[
verified_claims_request.json
]
, it can be used to automatically validate
claims
request parameters. The provided JSON schema files are a non-normative implementation of this specification and any discrepancies that exist are either implementation bugs or interpretations.
¶
To request Verified Claims, the
verified_claims
element is added to the
userinfo
or the
id_token
element of the
claims
parameter.
¶
Since
verified_claims
contains the effective Claims about the End-User in a nested
claims
element, the syntax is extended to include expressions on nested elements as follows. The
verified_claims
element includes a
claims
element, which in turn includes the desired Claims as keys. For each claim, the value is either
null
(default), or an object. The object may contain restrictions using
value
or
values
as defined in
[
OpenID
]
and/or the
essential
or
purpose
keys as described below. An example is shown in the following:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null
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
Use of the
claims
parameter allows the RP to exactly select the Claims about the End-User needed for its use case. This extension therefore allows RPs to fulfill the requirement for data minimization.
¶
RPs MAY use the
essential
field as defined in Section 5.5.1 of the OpenID Connect specification
[
OpenID
]
. The following example shows this for the family and given names.
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null
      },
      "claims": {
        "given_name": {
          "essential": true
        },
        "family_name": {
          "essential": true
        },
        "birthdate": null
      }
    }
  }
}
¶
This specification introduces the additional field
purpose
to allow an RP
to state the purpose for the transfer of a certain End-User Claim it is asking for.
The field
purpose
can be a member value of each individually requested
Claim, but a Claim cannot have more than one associated purpose.
¶
purpose
: OPTIONAL. String describing the purpose for obtaining a certain End-User Claim from the OP. The purpose MUST NOT be shorter than 3 characters or
longer than 300 characters. If this rule is violated, the authentication
request MUST fail and the OP return an error
invalid_request
to the RP.
The OP MUST display this purpose in the respective End-User consent screen(s)
in order to inform the End-User about the designated use of the data to be
transferred or the authorization to be approved. If the parameter
purpose
is not present in the request, the OP MAY display a
value that was pre-configured for the respective RP. For details on UI
localization, see
Section 11
.
¶
Example:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null
      },
      "claims": {
        "given_name": {
          "essential": true,
          "purpose": "To make communication look more personal"
        },
        "family_name": {
          "essential": true
        },
        "birthdate": {
          "purpose": "To send you best wishes on your birthday"
        }
      }
    }
  }
}
¶
6.2.
Requesting Verification Data
RPs request verification data in the same way they request Claims about the End-User. The syntax is based on the rules given in
Section 6.1
and extends them for navigation into the structure of the
verification
element.
¶
Elements within
verification
are requested by adding the respective element as shown in the following example:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null
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
It requests the trust framework the OP complies with and the date of the verification of the End-User Claims.
¶
The RP MUST explicitly request any data it wants the OP to add to the
verification
element.
¶
Therefore, the RP MUST set fields one step deeper into the structure if it wants to obtain evidence. One or more entries in the
evidence
array are used as filter criteria and templates for all entries in the result array. The following examples shows a request asking for evidence of type
document
.
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null,
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "method": null,
            "document_details": {
              "type": null
            }
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
The example also requests the OP to add the respective
method
and the
document
elements (including data about the document type) for every evidence to the resulting
verified_claims
Claim.
¶
A single entry in the
evidence
array represents a filter over elements of a certain evidence type. The RP therefore MUST specify this type by including the
type
field including a suitable
value
sub-element value. The
values
sub-element MUST NOT be used for the
evidence/type
field.
¶
If multiple entries are present in
evidence
, these filters are linked by a logical OR.
¶
check_details
is an array of the processes that have been applied to the
evidence
. An RP MAY filter
check_details
by requesting a particular value for one or more of its sub-elements. If multiple entries for the same sub-element are present this acts as a logical OR between them.
¶
assurance_details
is an array representing how the
evidence
and
check_details
meets the requirements of the
trust_framework
. RP SHOULD only request this where they need to know this information. Where
assurance_details
have been requested by an RP the OP MUST return the
assurance_details
element along with all sub-elements that it has. If an RP wants to filter what types of
evidence
and
check_methods
they MUST use those methods to do so, e.g. requesting an
assurance_type
should have no filtering effect.
¶
The RP MAY also request certain data within the
document
element to be present. This again follows the syntax rules used above:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null,
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "method": null,
            "document_details": {
              "type": null,
              "issuer": {
                "country": null,
                "name": null
              },
              "document_number": null,
              "date_of_issuance": null
            }
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
6.3.
Defining further constraints on Verification Data
6.3.1.
value/values
The RP MAY limit the possible values of the elements
trust_framework
,
evidence/method
,
evidence/check_details
, and
evidence/document/type
by utilizing the
value
or
values
fields and the element
evidence/type
by utilizing the
value
field.
¶
Note: Examples on the usage of a restriction on
evidence/type
were given in the previous section.
¶
The following example shows how an RP may request Claims either complying with trust framework
gold
or
silver
.
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": {
          "values": [
            "gold",
            "silver"
          ]
        }
      },
      "claims": {
        "given_name": null,
        "family_name": null
      }
    }
  }
}
¶
The following example shows that the RP wants to obtain an attestation based on the German Anti Money Laundering Law (trust framework
de_aml
) and limited to End-Users who were identified in a bank branch in person (physical in person proofing - method
pipp
) using either an
idcard
or a
passport
.
¶
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
            "document": {
              "type": {
                "values": [
                  "idcard",
                  "passport"
                ]
              }
            }
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
The OP MUST NOT ignore some or all of the query restrictions on possible values and MUST NOT deliver available verified/verification data that does not match these constraints.
¶
6.3.2.
max_age
The RP MAY also express a requirement regarding the age of certain data, like the time elapsed since the issuance/expiry of certain evidence types or since the verification process asserted in the
verification
element took place. Section 5.5.1 of the OpenID Connect specification
[
OpenID
]
defines a query syntax that allows for new special query members to be defined. This specification introduces a new such member
max_age
, which is applicable to the possible values of any elements containing dates or timestamps (e.g.,
time
,
date_of_issuance
and
date_of_expiry
elements of evidence of type
document
).
¶
max_age
: OPTIONAL. JSON number value only applicable to Claims that contain dates or timestamps. It defines the maximum time (in seconds) to be allowed to elapse since the value of the date/timestamp up to the point in time of the request. The OP should make the calculation of elapsed time starting from the last valid second of the date value.
¶
The following is an example of a request for Claims where the verification process of the data is not allowed to be older than 63113852 seconds:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": {
          "value": "jp_aml"
        },
        "time": {
          "max_age": 63113852
        }
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
The OP SHOULD try to fulfill this requirement. If the verification data of the End-User is older than the requested
max_age
, the OP MAY attempt to refresh the End-User's verification by sending them through an online identity verification process, e.g., by utilizing an electronic ID card or a video identification approach.
¶
6.4.
Requesting Claims sets with different verification requirements
It is also possible to request different trust frameworks, assurance levels, and methods for different Claim sets. This requires the RP to send an array of
verified_claims
objects instead of passing a single object.
¶
The following example illustrates this functionality.
¶
{
  "userinfo": {
    "verified_claims": [
      {
        "verification": {
          "trust_framework": {
            "value": "eidas"
          },
          "assurance_level": {
            "value": "high"
          }
        },
        "claims": {
          "given_name": null,
          "family_name": null
        }
      },
      {
        "verification": {
          "trust_framework": {
            "value": "eidas"
          },
          "assurance_level":{
            "values":[
              "high",
              "substantial"
            ]
          }
        },
        "claims": {
          "birthdate": null
        }
      }
    ]
  }
}
¶
When the RP requests multiple verifications as described above, the OP is supposed to process any element in the array independently. The OP will provide
verified_claims
response elements for every
verified_claims
request element whose requirements it is able to fulfill. This also means if multiple
verified_claims
elements contain the same End-User Claim(s), the OP delivers the Claim in as many Verified Claims response objects it can fulfil. For example, if the trust framework the OP uses is compatible with multiple of the requested trust frameworks, it provides a
verified_claims
element for each of them.
¶
The RP MAY combine multiple
verified_claims
Claims in the request with multiple
trust_framework
and/or
assurance_level
values using the
values
element. In that case, the rules given above for processing
values
are applied for the particular
verified_claims
request object.
¶
{
  "userinfo": {
    "verified_claims": [
      {
        "verification": {
          "trust_framework": {
            "value": "gold"
          },
          "evidence": [
            {
              "type": {
                "value": "document"
              }
            }
          ]
        },
        "claims": {
          "given_name": null,
          "family_name": null
        }
      },
      {
        "verification": {
          "trust_framework": {
            "values": [
              "silver",
              "bronze"
            ]
          },
          "evidence": [
            {
              "type": {
                "value": "electronic_record"
              }
            }
          ]
        },
        "claims": {
          "given_name": null,
          "family_name": null
        }
      }
    ]
  }
}
¶
In the above example, the RP asks for family and given name either under trust framework
gold
with an evidence of type
document
or under trust framework
silver
or
bronze
but with an evidence
electronic_record
.
¶
6.5.
Handling Unfulfillable Requests and Unavailable Data
In some cases, OPs cannot deliver the requested data to an RP, for example, because the data is not available or does not match the RP's requirements. The rules for handling these cases are described in the following.
¶
Extensions of this specification MAY define additional rules or override these rules, for example
¶
to allow or disallow the use of Claims depending on scheme-specific checks,
¶
to enable a finer-grained control of the RP over the behavior of the OP when data is unavailable or does not match the criteria, or
¶
to abort transactions (return error codes) in cases where requests cannot be fulfilled.
¶
Important: The behavior described below is independent from the use of
essential
(as defined in Section 5.5 of
[
OpenID
]
).
¶
6.5.1.
Unavailable Data
If the RP does not have data about a certain Claim, does not understand/support the respective Claim, or the End-User does not consent to the release of the data, the respective Claim MUST be omitted from the response. The OP MUST NOT return an error to the RP. If the End-User does not consent to the whole transaction, standard OpenID Connect logic applies, as defined in Section 3.1.2.6 of
[
OpenID
]
.
¶
6.5.2.
Data not Matching Requirements
When the available data does not fulfill the requirements of the RP expressed through
value
,
values
, or
max_age
, the following logic applies:
¶
If the respective requirement was expressed for a Claim within
verified_claims/verification
, the whole
verified_claims
element MUST be omitted.
¶
Otherwise, the respective Claim MUST be omitted from the response.
¶
In both cases, the OP MUST NOT return an error to the RP.
¶
6.5.3.
Omitting Elements
If an element is to be omitted according to the rules above, but is required for a valid response, its parent element MUST be omitted as well. This process MUST be repeated until the response is valid.
¶
6.5.4.
Error Handling
If the
claims
sub-element is empty, the OP MUST abort the transaction with an
invalid_request
error.
¶
Claims unknown to the OP or not available as Verified Claims MUST be ignored and omitted from the response. If the resulting
claims
sub-element is empty, the OP MUST omit the
verified_claims
element.
¶
6.6.
Requesting sets of Claims by scope
Verified Claims about the End-User can be requested as part of a pre-defined set by utilizing the
scope
parameter as defined in Section 5.4 of the OpenID Connect specification
[
OpenID
]
.
¶
When using this approach the Claims associated with a
scope
are administratively defined at the OP.  The OP configuration and RP request parameters will determine whether the Claims are returned via the ID Token or UserInfo endpoint as defined in Section 5.3.2 of the OpenID Connect specification
[
OpenID
]
.
¶
7.
Example Requests
This section shows examples of requests for
verified_claims
.
¶
7.1.
Verification of Claims by a document
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null,
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "method": null,
            "document_details": {
              "type": null
            }
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
Note that, as shown in the above example, this specification requires that implementations receiving requests are able to distinguish between JSON objects where a key is not present versus where a key is present with a null value.
¶
Support for these null value requests is mandatory for identity providers, so implementors are encouraged to test this behaviour early in their development process. In some programming languages many JSON libraries or HTTP frameworks will, at least by default, ignore null values and omit the relevant key when parsing the JSON.
¶
7.2.
Verification of Claims by trust framework and evidence types
{
  "userinfo": {
    "verified_claims": [
      {
        "verification": {
          "trust_framework": {
            "value": "gold"
          },
          "evidence": [
            {
              "type": {
                "value": "document"
              }
            }
          ]
        },
        "claims": {
          "given_name": null,
          "family_name": null
        }
      },
      {
        "verification": {
          "trust_framework": {
            "values": [
              "silver",
              "bronze"
            ]
          },
          "evidence": [
            {
              "type": {
                "value": "vouch"
              }
            }
          ]
        },
        "claims": {
          "given_name": null,
          "family_name": null
        }
      }
    ]
  }
}
¶
7.3.
Verification of Claims by trust framework and verification method
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": {
          "value": "it_spid"
        },
        "time": null,
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "verification_method": {
              "type": {
                "value": "bvr"
              }
            },
            "document_details": {
              "type": null,
              "issuer": {
                "country": null,
                "name": null
              },
              "document_number": null,
              "date_of_issuance": null
            }
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
7.4.
Verification of Claims by trust framework with a document and attachments
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
7.5.
Verification of Claims by electronic signature
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null,
        "evidence": [
          {
            "type": {
              "value": "electronic_signature"
            },
            "issuer": null,
            "serial_number": null,
            "created_at": null
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
7.5.1.
Attachments
RPs can explicitly request to receive attachments along with the Verified Claims:
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
As with other Claims, the attachment Claim can be marked as
essential
in the request as well.
¶
7.5.2.
Error Handling
The OP has the discretion to decide whether the requested verification data is to be provided to the RP.
¶
8.
Example Responses
This section shows examples of responses containing
verified_claims
.
¶
The first and second subsections show JSON snippets of the general identity assurance case, where the RP is provided with verification evidence for different methods along with the actual Claims about the End-User.
¶
The third subsection illustrates how the contents of this object could look like in case of a notified eID system under eIDAS, where the OP does not need to provide evidence of the identity verification process to the RP.
¶
Subsequent subsections contain examples for using the
verified_claims
Claim on different channels and in combination with other (unverified) Claims.
¶
8.1.
ID document [deprecated format]
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
          "document": {
            "type": "idcard",
            "issuer": {
              "name": "Stadt Augsburg",
              "country": "DE"
            },
            "number": "53554554",
            "date_of_issuance": "2010-03-23",
            "date_of_expiry": "2020-03-22"
          }
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
8.2.
Document
{
  "verified_claims": {
    "verification": {
      "trust_framework": "nist_800_63A",
      "assurance_level": "ial2",
      "assurance_process": {
        "assurance_details": [
          {
            "assurance_type": "evidence_validation",
            "assurance_classification": "strong",
            "evidence_ref": [
              {
                "txn": "DL1-93h506th2f45hf"
              }
            ]
          },
          {
            "assurance_type": "verification",
            "assurance_classification": "strong",
            "evidence_ref": [
              {
                "txn": "v-93jfk284ugjfj2093"
              }
            ]
          }
        ]
      },
      "time": "2021-06-06T05:32Z",
      "verification_process": "7675D80F-57E0-AB14-9543-26B41FC22",
      "evidence": [
        {
          "type": "document",
          "check_details": [
            {
              "check_method": "vpiruv",
              "organization": "doc_checker",
              "txn": "DL1-93h506th2f45hf"
            },
            {
              "check_method": "pvp",
              "organization": "face_checker",
              "txn": "v-93jfk284ugjfj2093"
            }
          ],
          "time": "2021-06-06T05:33Z",
          "document_details": {
            "type": "driving_permit",
            "document_number": "I1234568",
            "date_of_issuance": "2019-09-05",
            "date_of_expiry": "2024-08-01",
            "issuer": {
                "name": "CA DMV",
                "country": "US",
                "country_code": "USA",
                "jurisdiction": "CA"
            }
          }
        }
      ]
    },
    "claims": {
      "given_name": "Inga",
      "family_name": "Silverstone",
      "birthdate": "1991-11-06",
      "place_of_birth": {
        "country": "USA"
      },
      "address": {
        "locality": "Shoshone",
        "postal_code": "CA 92384",
        "country": "USA",
        "street_address": "114 Old State Hwy 127"
      }
    }
  }
}
¶
Same document under a different
trust_framework
¶
{
  "verified_claims": {
    "verification": {
      "trust_framework": "uk_diatf",
      "assurance_level": "medium",
      "assurance_process": {
        "policy": "gpg45",
        "procedure": "m1c",
        "assurance_details": [
          {
            "assurance_type": "evidence_validation",
            "assurance_classification": "score_3",
            "evidence_ref": [
              {
                "txn": "DL1-93h506th2f45hf",
                "evidence_metadata": {
                  "evidence_classification": "score_3_strength"
                }
              }
            ]
          },
          {
            "assurance_type": "verification",
            "assurance_classification": "score_3",
            "evidence_ref": [
              {
                "txn": "v-93jfk284ugjfj2093"
              }
            ]
          }
        ]
      },
      "time": "2021-06-06T05:32Z",
      "verification_process": "7675D80F-57E0-AB14-9543-26B41FC22",
      "evidence": [
        {
          "type": "document",
          "check_details": [
            {
              "check_method": "vpiruv",
              "organization": "doc_checker",
              "txn": "DL1-93h506th2f45hf",
              "time": "2021-06-08T11:41Z"
            },
            {
              "check_method": "pvp",
              "organization": "face_checker",
              "txn": "v-93jfk284ugjfj2093",
              "time": "2021-06-08T11:42Z"
            }
          ],
          "time": "2021-06-06T05:33Z",
          "document_details": {
            "type": "driving_permit",
            "document_number": "I1234568",
            "date_of_issuance": "2019-09-05",
            "date_of_expiry": "2024-08-01",
            "issuer": {
                "name": "CA DMV",
                "country": "US",
                "country_code": "USA",
                "jurisdiction": "CA"
            }
          },
          "attachments": [
            {
              "desc": "scan of driving_permit",
              "content_type": "image/jpeg",
              "txn": "DL1-93h506th2f45hf",
              "content": "d16d2552e35582810e5a40e523716504525b6016ae96844ddc533163059b3067=="
            },
            {
              "desc": "captured face",
              "content_type": "image/jpeg",
              "txn": "v-93jfk284ugjfj2093",
              "content": "6954697405687029456098270457602984756098274509687204576=="
            }
          ]
        }
      ]
    },
    "claims": {
      "given_name": "Inga",
      "family_name": "Silverstone",
      "birthdate": "1991-11-06",
      "place_of_birth": {
        "country": "USA"
      },
      "address": {
        "locality": "Shoshone",
        "postal_code": "CA 92384",
        "country": "USA",
        "street_address": "114 Old State Hwy 127"
      }
    }
  }
}
¶
8.3.
Document and verifier details
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
          "verifier": {
            "organization": "Deutsche Post",
            "txn": "1aa05779-0775-470f-a5c4-9f1f5e56cf06"
          },
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
          }
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
8.4.
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
8.5.
Evidence with all assurance details
{
  "verified_claims": {
    "verification": {
      "trust_framework": "uk_diatf",
      "assurance_level": "medium",
      "assurance_process": {
        "policy": "gpg45",
        "procedure": "m1b",
        "assurance_details": [
          {
            "assurance_type": "evidence_validation",
            "assurance_classification": "score_2",
            "evidence_ref": [
              {
                "txn": "DL1-85762937582385820",
                "evidence_metadata": {
                  "evidence_classification": "score_3_strength"
                }
              }
            ]
          },
          {
            "assurance_type": "verification",
            "assurance_classification": "score_2",
            "evidence_ref": [
              {
                "txn": "kbv1-hf934hn09234ng03jj3",
                "evidence_metadata": {
                  "evidence_classification": "high_kbv"
                }
              },
              {
                "txn": "kbv2-nm0f23u9459fj38u5j6",
                "evidence_metadata": {
                  "evidence_classification": "medium_kbv"
                }
              },
              {
                "txn": "kbv3-jf9028h023hj0f9jh23",
                "evidence_metadata": {
                  "evidence_classification": "medium_kbv"
                }
              }
            ]
          },
          {
            "assurance_type": "counter_fraud",
            "assurance_classification": "score_2",
            "evidence_ref": [
              {
                "txn": "GRO-9824hngvp9278hf5tmp924y5h",
                "evidence_metadata": {
                  "evidence_classification": "mortality_check"
                }
              },
              {
                "txn": "fi-2nbf02hfn384ufn",
                "evidence_metadata": {
                  "evidence_classification": "id_fraud"
                }
              }
            ]
          }
        ]
      },
      "time": "2021-05-11T14:29Z",
      "verification_process": "7675D80F-57E0-AB14-9543-26B41FC22",
      "evidence": [
        {
          "type": "document",
          "check_details": [
            {
              "check_method": "data",
              "organization": "DVLA",
              "time": "2021-04-09T14:15Z",
              "txn": "DL1-85762937582385820"
            }
          ],
          "time": "2021-04-09T14:12Z",
          "document_details": {
            "type": "driving_permit",
            "personal_number": "MORGA753116SM9IJ",
            "document_number": "MORGA753116SM9IJ35",
            "serial_number": "ZG21000001",
            "date_of_issuance": "2021-01-01",
            "date_of_expiry": "2030-12-31",
            "issuer": {
              "name": "DVLA",
              "country": "UK",
              "country_code": "GBR",
              "jurisdiction": "GB-GBN"
            }
          }
        },
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "kbv",
              "organization": "TheCreditBureau",
              "txn": "kbv1-hf934hn09234ng03jj3"
            }
          ],
          "time": "2021-04-09T14:12Z",
          "record": {
            "type": "mortgage_account",
            "source": {
              "name": "TheCreditBureau"
            }
          }
        },
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "kbv",
              "organization": "OpenBankingTPP",
              "txn": "kbv2-nm0f23u9459fj38u5j6"
            }
          ],
          "time": "2021-04-09T14:12Z",
          "record": {
            "type": "bank_account",
            "source": {
              "name": "TheBank"
            }
          }
        },
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "kbv",
              "organization": "GSMA",
              "txn": "kbv3-jf9028h023hj0f9jh23"
            }
          ],
          "time": "2021-04-09T15:42Z",
          "record": {
            "type": "mno",
            "source": {
              "name": "Vodafone"
            }
          }
        },
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "data",
              "organization": "GRO",
              "txn": "GRO-9824hngvp9278hf5tmp924y5h"
            }
          ],
          "time": "2021-04-09T16:12Z",
          "record": {
            "type": "death_register",
            "source": {
              "name": "General Register Office",
              "street_address": "PO BOX 2",
              "locality": "Southport",
              "postal_code": "PR8 2JD",
              "country": "UK",
              "country_code": "GBR",
              "jurisdiction": "GB-EAW"
            }
          }
        },
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "data",
              "organization": "NextLex",
              "txn": "fi-2nbf02hfn384ufn"
            }
          ],
          "time": "2021-04-09T16:51Z",
          "record": {
            "type": "fraud_register",
            "source": {
              "name": "National Fraud Database",
              "jurisdiction": "UK"
            }
          }
        }
      ]
    },
    "claims": {
      "given_name": "Sarah",
      "family_name": "Meredyth",
      "birthdate": "1976-03-11",
      "place_of_birth": {
        "country": "UK"
      },
      "address": {
        "locality": "Edinburgh",
        "postal_code": "EH1 9GP",
        "country": "UK",
        "street_address": "122 Burns Crescent"
      }
    }
  }
}
¶
8.6.
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
8.7.
Document + utility statement
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
              "check_method": "pvp"
            },
            {
              "check_method": "vpip"
            }
          ],
          "time": "2012-04-22T11:30Z",
          "document_details": {
            "type": "de_erp_replacement_idcard",
            "issuer": {
              "name": "Stadt Augsburg",
              "country": "DE"
            },
            "document_number": "53554554",
            "date_of_issuance": "2010-04-23",
            "date_of_expiry": "2020-04-22"
          }
        },
        {
          "type": "document",
          "validation_method": {
            "type": "vpip"
          },
          "time": "2012-04-22T11:30Z",
          "document_details": {
            "type": "utility_statement",
            "issuer": {
                "name": "Stadtwerke Musterstadt",
                "country": "DE",
                "region": "Niedersachsen",
                "street_address": "Energiestrasse 33"
            },
            "date_of_issuance": "2013-01-31"
          }
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
8.8.
ID document + utility bill [deprecated format]
{
  "verified_claims": {
    "verification": {
      "trust_framework": "de_aml",
      "time": "2012-04-23T18:25Z",
      "verification_process": "513645-e44b-4951-942c-7091cf7d891d",
      "evidence": [
        {
          "type": "document",
          "method": "pipp",
          "time": "2012-04-22T11:30Z",
          "document": {
            "type": "de_erp_replacement_idcard",
            "issuer": {
              "name": "Stadt Augsburg",
              "country": "DE"
            },
            "number": "53554554",
            "date_of_issuance": "2010-04-23",
            "date_of_expiry": "2020-04-22"
          }
        },
        {
          "type": "utility_bill",
          "provider": {
            "name": "Stadtwerke Musterstadt",
            "country": "DE",
            "region": "Niedersachsen",
            "street_address": "Energiestrasse 33"
          },
          "date": "2013-01-31"
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
8.9.
Notified eID system (eIDAS)
{
  "verified_claims": {
    "verification": {
      "trust_framework": "eidas",
      "assurance_level": "substantial"
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
      ]
    }
  }
}
¶
8.10.
Electronic_record
{
  "verified_claims": {
    "verification": {
      "trust_framework": "se_bankid",
      "assurance_level": "al_2",
      "time": "2021-03-03T09:42Z",
      "verification_process": "4346D80F-57E0-4E26-9543-26B41FC22",
      "evidence": [
        {
          "type": "electronic_record",
          "check_details": [
            {
              "check_method": "data"
            },
            {
              "check_method": "token"
            }
          ],
          "time": "2021-02-15T16:51Z",
          "record": {
            "type": "population_register",
            "source": {
                "name": "Skatteverket",
                "country": "Sverige",
                "country_code": "SWE"
            },
            "personal_number": "4901224131",
            "created_at": "1979-01-22"
          }
        }
      ]
    },
    "claims": {
      "given_name": "Fredrik",
      "family_name": "Str&#246;mberg",
      "birthdate": "1979-01-22",
      "place_of_birth": {
        "country": "SWE",
        "locality": "&#214;rnsk&#246;ldsvik"
      },
      "nationalities": [
        "SE"
      ],
      "address": {
        "locality": "Karlstad",
        "postal_code": "65344",
        "country": "SWE",
        "street_address": "Gatunamn 221b"
      }
    }
  }
}
¶
8.11.
Vouch
{
  "verified_claims": {
    "verification": {
      "trust_framework": "uk_diatf",
      "assurance_level": "very_high",
      "time": "2020-03-19T13:05Z",
      "verification_process": "76755DA2-81E1-5N14-9543-26B415B77",
      "evidence": [
        {
          "type": "vouch",
          "check_details": [
            {
              "check_method": "vcrypt"
            },
            {
              "check_method": "bvr"
            }
          ],
          "time": "2020-03-19T12:42Z",
          "attestation": {
            "type": "digital_attestation",
            "reference_number": "6485-1619-3976-6671",
            "date_of_issuance": "2021-06-04",
            "voucher": {
                "organization": "HMP Dartmoor"
            }
          }
        }
      ]
    },
    "claims": {
      "given_name": "Sam",
      "family_name": "Lawler",
      "birthdate": "1981-04-13",
      "place_of_birth": {
        "country": "GBR"
      },
      "address": {
        "postal_code": "98015",
        "country": "Monaco"
      }
    }
  }
}
¶
8.12.
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
8.13.
Multiple Verified Claims
{
  "verified_claims": [
    {
      "verification": {
        "trust_framework": "eidas",
        "assurance_level": "substantial"
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
        ]
      }
    },
    {
      "verification": {
        "trust_framework": "de_aml",
        "time": "2012-04-23T18:25Z",
        "verification_process": "f24c6f-6d3f-4ec5-973e-b0d8506f3bc7",
        "evidence": [
          {
            "type": "document",
            "method": "pipp",
            "time": "2012-04-22T11:30Z",
            "document": {
              "type": "idcard"
            }
          }
        ]
      },
      "claims": {
        "address": {
          "locality": "Maxstadt",
          "postal_code": "12344",
          "country": "DE",
          "street_address": "An der Weide 22"
        }
      }
    }
  ]
}
¶
8.14.
Verified Claims in UserInfo Response
8.14.1.
Request
In this example we assume the RP uses the
scope
parameter to request the email address and, additionally, the
claims
parameter, to request Verified Claims.
¶
The scope value is:
scope=openid email
¶
The value of the
claims
parameter is:
¶
{
  "userinfo": {
    "verified_claims": {
      "verification": {
        "trust_framework": null
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
8.14.2.
UserInfo Response
The respective UserInfo response would be
¶
{
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "verified_claims": {
    "verification": {
      "trust_framework": "de_aml"
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier",
      "birthdate": "1956-01-28"
    }
  }
}
¶
8.15.
Verified Claims in ID Tokens
8.15.1.
Request
In this case, the RP requests Verified Claims along with other Claims about the End-User in the
claims
parameter and allocates the response to the ID Token (delivered from the token endpoint in case of grant type
authorization_code
).
¶
The
claims
parameter value is
¶
{
  "id_token": {
    "email": null,
    "preferred_username": null,
    "picture": null,
    "verified_claims": {
      "verification": {
        "trust_framework": null,
        "time": null,
        "verification_process": null,
        "evidence": [
          {
            "type": {
              "value": "document"
            },
            "method": null,
            "time": null,
            "document_details": {
              "type": null,
              "issuer": {
                "name": null,
                "country": null
              },
              "document_number": null,
              "date_of_issuance": null,
              "date_of_expiry": null
            }
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
8.15.2.
ID Token
The respective ID Token could be
¶
{
  "iss": "https://server.example.com",
  "sub": "24400320",
  "aud": "s6BhdRkqt3",
  "nonce": "n-0S6_WzA2Mj",
  "exp": 1311281970,
  "iat": 1311280970,
  "auth_time": 1311280969,
  "acr": "urn:mace:incommon:iap:silver",
  "email": "janedoe@example.com",
  "preferred_username": "j.doe",
  "picture": "http://example.com/janedoe/me.jpg",
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
          }
        }
      ]
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier",
      "birthdate": "1956-01-28"
    }
  }
}
¶
8.16.
Claims provided by the OP and external sources
This example shows how an OP can mix own Claims and Claims provided by
external sources in a single ID Token.
¶
{
  "iss": "https://server.example.com",
  "sub": "248289761001",
  "email": "janedoe@example.com",
  "email_verified": true,
  "verified_claims": {
    "verification": {
      "trust_framework": "trust_framework_example"
    },
    "claims": {
      "given_name": "Max",
      "family_name": "Meier"
    }
  },
  "_claim_names": {
    "verified_claims": [
      "src1",
      "src2"
    ]
  },
  "_claim_sources": {
    "src1": {
      "JWT": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlcnZlci5vdGhlcm9wLmNvbSIsInN1YiI6ImU4MTQ4NjAzLTg5MzQtNDI0NS04MjViLWMxMDhiOGI2Yjk0NSIsInZlcmlmaWVkX2NsYWltcyI6eyJ2ZXJpZmljYXRpb24iOnsidHJ1c3RfZnJhbWV3b3JrIjoiaWFsX2V4YW1wbGVfZ29sZCJ9LCJjbGFpbXMiOnsiZ2l2ZW5fbmFtZSI6Ik1heCIsImZhbWlseV9uYW1lIjoiTWVpZXIiLCJiaXJ0aGRhdGUiOiIxOTU2LTAxLTI4In19fQ.FArlPUtUVn95HCExePlWJQ6ctVfVpQyeSbe3xkH9MH1QJjnk5GVbBW0qe1b7R3lE-8iVv__0mhRTUI5lcFhLjoGjDS8zgWSarVsEEjwBK7WD3r9cEw6ZAhfEkhHL9eqAaED2rhhDbHD5dZWXkJCuXIcn65g6rryiBanxlXK0ZmcK4fD9HV9MFduk0LRG_p4yocMaFvVkqawat5NV9QQ3ij7UBr3G7A4FojcKEkoJKScdGoozir8m5XD83Sn45_79nCcgWSnCX2QTukL8NywIItu_K48cjHiAGXXSzydDm_ccGCe0sY-Ai2-iFFuQo2PtfuK2SqPPmAZJxEFrFoLY4g"
    },
    "src2": {
      "endpoint": "https://server.yetanotherop.com/claim_source",
      "access_token": "ksj3n283dkeafb76cdef"
    }
  }
}
¶
8.17.
Self-Issued OpenID Connect Provider and External Claims
This example shows how a Self-Issued OpenID Connect Provider (SIOP)
may include Verified Claims obtained from different external Claim
sources into a ID Token.
¶
{
  "iss": "https://self-issued.me",
  "sub": "248289761001",
  "preferred_username": "superman445",
  "_claim_names": {
    "verified_claims": [
      "src1",
      "src2"
    ]
  },
  "_claim_sources": {
    "src1": {
      "JWT": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL3NlcnZlci5vdGhlcm9wLmNvbSIsInN1YiI6ImU4MTQ4NjAzLTg5MzQtNDI0NS04MjViLWMxMDhiOGI2Yjk0NSIsInZlcmlmaWVkX2NsYWltcyI6eyJ2ZXJpZmljYXRpb24iOnsidHJ1c3RfZnJhbWV3b3JrIjoiaWFsX2V4YW1wbGVfZ29sZCJ9LCJjbGFpbXMiOnsiZ2l2ZW5fbmFtZSI6Ik1heCIsImZhbWlseV9uYW1lIjoiTWVpZXIiLCJiaXJ0aGRhdGUiOiIxOTU2LTAxLTI4In19fQ.FArlPUtUVn95HCExePlWJQ6ctVfVpQyeSbe3xkH9MH1QJjnk5GVbBW0qe1b7R3lE-8iVv__0mhRTUI5lcFhLjoGjDS8zgWSarVsEEjwBK7WD3r9cEw6ZAhfEkhHL9eqAaED2rhhDbHD5dZWXkJCuXIcn65g6rryiBanxlXK0ZmcK4fD9HV9MFduk0LRG_p4yocMaFvVkqawat5NV9QQ3ij7UBr3G7A4FojcKEkoJKScdGoozir8m5XD83Sn45_79nCcgWSnCX2QTukL8NywIItu_K48cjHiAGXXSzydDm_ccGCe0sY-Ai2-iFFuQo2PtfuK2SqPPmAZJxEFrFoLY4g"
    },
    "src2": {
      "endpoint": "https://op.mymno.com/claim_source",
      "access_token": "ksj3n283dkeafb76cdef"
    }
  }
}
¶
9.
OP Metadata
The OP advertises its capabilities with respect to Verified Claims in its openid-configuration (see
[
OpenID-Discovery
]
) using the following new elements:
¶
verified_claims_supported
: REQUIRED. Boolean value indicating support for
verified_claims
, i.e., the OpenID Connect for Identity Assurance extension.
¶
trust_frameworks_supported
: REQUIRED. JSON array containing all supported trust frameworks. This array MUST have at least one member.
¶
evidence_supported
: REQUIRED. JSON array containing all types of identity evidence the OP uses. This array MUST have at least one member.
¶
documents_supported
: REQUIRED when
evidence_supported
contains "document". JSON array containing all identity document types utilized by the OP for identity verification. This array MUST have at least one member.
¶
documents_methods_supported
: OPTIONAL. JSON array containing the methods the OP supports for evidences of type "document" (see @!predefined_values). When present this array MUST have at least one member.
¶
documents_check_methods_supported
: OPTIONAL. JSON array containing the check methods the OP supports for evidences of type "document" (see @!predefined_values). When present this array MUST have at least one member.
¶
electronic_records_supported
: REQUIRED when
evidence_supported
contains "electronic_record". JSON array containing all electronic record types the OP supports (see
Section 14
). When present this array MUST have at least one member.
¶
claims_in_verified_claims_supported
: REQUIRED. JSON array containing all Claims supported within
verified_claims
. Claims that are not present in this array MUST NOT be returned within the
verified_claims
object. This array MUST have at least one member.
¶
attachments_supported
: REQUIRED when OP supports attachments. JSON array containing all attachment types supported by the OP. Possible values are
external
and
embedded
. When present this array MUST have at least one member.
¶
digest_algorithms_supported
: REQUIRED when OP supports external attachments. JSON array containing all supported digest algorithms which can be used as
alg
property within the digest object of external attachments. If the OP supports external attachments, at least the algorithm
sha-256
MUST be supported by the OP as well. The list of possible digest/hash algorithm names is maintained by IANA in
[
hash_name_registry
]
(established by
[
RFC6920
]
).
¶
This is an example openid-configuration snippet:
¶
{
...
   "verified_claims_supported":true,
   "trust_frameworks_supported":[
     "nist_800_63A"
   ],
   "evidence_supported": [
      "document",
      "electronic_record",
      "vouch",
      "electronic_signature"
   ],
   "documents_supported": [
       "idcard",
       "passport",
       "driving_permit"
   ],
   "documents_methods_supported": [
       "pipp",
       "sripp",
       "eid"
   ],
   "electronic_records_supported": [
       "secure_mail"
   ],
   "claims_in_verified_claims_supported": [
      "given_name",
      "family_name",
      "birthdate",
      "place_of_birth",
      "nationalities",
      "address"
   ],
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
The OP MUST support the
claims
parameter and needs to publish this in its openid-configuration using the
claims_parameter_supported
element.
¶
If the OP supports distributed and/or aggregated Claim types in
verified_claims
, the OP MUST advertise this in its metadata using the
claim_types_supported
element.
¶
10.
Client Registration and Management
During Client Registration (see
[
OpenID-Registration
]
) as well as during Client Management
[
RFC7592
]
the following additional properties are available:
¶
digest_algorithm
: String value representing the chosen digest algorithm (for external attachments). The value MUST be one of the digest algorithms supported by the OP as advertised in the
OP metadata
. If this property is not set,
sha-256
will be used by default.
¶
11.
Transaction-specific Purpose
This specification introduces the request parameter
purpose
to allow an RP
to state the purpose for the transfer of End-User data it is asking for.
¶
purpose
: OPTIONAL. String describing the purpose for obtaining certain End-User data from the OP. The purpose MUST NOT be shorter than 3 characters and MUST NOT be longer than 300 characters. If these rules are violated, the authentication request MUST fail and the OP returns an error
invalid_request
to the RP.
¶
The OP SHOULD use the purpose provided by the RP to inform the respective End-User about the designated use of the data to be transferred or the authorization to be approved.
¶
In order to ensure a consistent UX, the RP MAY send the
purpose
in a certain language and request the OP to use the same language using the
ui_locales
parameter.
¶
If the parameter
purpose
is not present in the request, the OP MAY utilize a description that was pre-configured for the respective RP.
¶
Note: In order to prevent injection attacks, the OP MUST escape the text appropriately before it will be shown in a user interface. The OP MUST expect special characters in the URL decoded purpose text provided by the RP. The OP MUST ensure that any special characters in the purpose text cannot be used to inject code into the web interface of the OP (e.g., cross-site scripting, defacing). Proper escaping MUST be applied by the OP. The OP SHALL NOT remove characters from the purpose text to this end.
¶
12.
Privacy Consideration
Timestamps with a time zone component can potentially reveal the person's location. To preserve the person's privacy timestamps within the verification element and Verified Claims that represent times SHOULD be represented in Coordinated Universal Time (UTC), unless there is a specific reason to include the time zone, such as the time zone being an essential part of a consented time related Claim in verified data.
¶
The use of scopes is a potential shortcut to request a pre-defined set of Claims, however, the use of scopes might result in more data being returned to the RP than is strictly necessary and not achieving the goal of data minimization. The RP SHOULD only request End-User Claims and metadata it requires.
¶
13.
Security Considerations
This specification focuses on mechanisms to carry End-User Claims and accompanying metadata in JSON objects and JSON web tokens, typically as part of an OpenID Connect protocol exchange. Since such an exchange is supposed to take place in security sensitive use cases, implementers MUST:
¶
ensure End-Users are authenticated using appropriately strong authentication methods, and
¶
combine this specification with an appropriate security profile for OpenID Connect.
¶
13.1.
End-User Authentication
Secure identification of End-Users not only depends on the identity verification at the OP but also on the strength of the user authentication at the OP. Combining a strong identification with weak authentication creates a false impression of security while being open to attacks. For example if an OP uses a simple PIN login, an attacker could guess the PIN of another user and identify himself as the other user at an RP with a high identity assurance level. To prevent this kind of attack, RPs SHOULD request the OP to authenticate the user at a reasonable level, typically using multi-factor authentication, when requesting verified End-User Claims. OpenID Connect supports this by way of the
acr_values
request parameter.
¶
13.2.
Security Profile
This specification does not define or require a particular security profile since there are several security
profiles and new security profiles under development.  Implementers shall be given flexibility to select the security profile that best suits
their needs. Implementers might consider
[
FAPI-1-RW
]
or
[
FAPI-2-BL
]
.
¶
Implementers are recommended to select a security profile that has a certification program or other resources that allow both OpenID Providers and Relying Parties to ensure they have complied with the profile's security and interoperability requirements, such as the OpenID Foundation Certification Program,
https://openid.net/certification/
.
¶
The integrity and authenticity of the issued assertions MUST be ensured in order to prevent identity spoofing.
¶
The confidentiality of all End-User data exchanged between the protocol parties MUST be ensured using suitable methods at transport or application layer.
¶
14.
Predefined Values
This specification focuses on the technical mechanisms to convey Verified Claims and thus does not define any identifiers for trust frameworks, documents, methods, validation methods or verification methods. This is left to adopters of the technical specification, e.g., implementers, identity schemes, or jurisdictions.
¶
Each party defining such identifiers MUST ensure the collision resistance of these identifiers. This is achieved by including a domain name under the control of this party into the identifier name, e.g.,
https://mycompany.com/identifiers/cool_verification_method
.
¶
The eKYC and Identity Assurance Working Group maintains a wiki page
[
predefined_values_page
]
that can be utilized to share predefined values with other parties.
¶
15.
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
[RFC7519]
Jones, M.
, Bradley, J.
, and N. Sakimura
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
[OpenID]
Sakimura, N.
, Bradley, J.
, Jones, M.
, de Medeiros, B.
, and C. Mortimore
,
"OpenID Connect Core 1.0 incorporating errata set 1"
,
8 November 2014
,
<
http://openid.net/specs/openid-connect-core-1_0.html
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
[RFC6750]
Jones, M.
and D. Hardt
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
[ICAO-Doc9303]
INTERNATIONAL CIVIL AVIATION ORGANIZATION
,
"Machine Readable Travel Documents, Seventh Edition, 2015, Part 3: Specifications Common to all MRTDs"
,
2015
,
<
https://www.icao.int/publications/Documents/9303_p3_cons_en.pdf
>
.
[ISO8601]
ISO
,
"ISO 8601. Data elements and interchange formats - Information interchange - Representation of dates and times"
,
,
<
http://www.iso.org/iso/catalogue_detail?csnumber=40874
>
.
[RFC6838]
Freed, N.
, Klensin, J.
, and T. Hansen
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
[hash_name_registry]
IANA
,
"Named Information Hash Algorithm Registry"
,
September 2016
,
<
https://www.iana.org/assignments/named-information/
>
.
[OpenID-Registration]
Sakimura, N.
, Bradley, J.
, and M. Jones
,
"OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 1"
,
8 November 2014
,
<
https://openid.net/specs/openid-connect-registration-1_0.html
>
.
[RFC8417]
Hunt, P., Ed.
, Jones, M.
, Denniss, W.
, and M. Ansari
,
"Security Event Token (SET)"
,
RFC 8417
,
DOI 10.17487/RFC8417
,
July 2018
,
<
https://www.rfc-editor.org/info/rfc8417
>
.
[OpenID-Discovery]
Sakimura, N.
, Bradley, J.
, Jones, M.
, and E. Jay
,
"OpenID Connect Discovery 1.0 incorporating errata set 1"
,
8 November 2014
,
<
https://openid.net/specs/openid-connect-discovery-1_0.html
>
.
16.
Informative References
[FATF-Digital-Identity]
Financial Action Task Force (FATF)
,
"Guidance on Digital Identity"
,
March 2020
,
<
https://www.fatf-gafi.org/media/fatf/documents/recommendations/Guidance-on-Digital-Identity.pdf
>
.
[verified_claims.json]
OpenID Foundation
,
"JSON Schema for assertions using verified_claims"
,
2020
,
<
https://openid.net/wg/ekyc-ida/references/
>
.
[eIDAS]
European Parliament
,
"REGULATION (EU) No 910/2014 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL on electronic identification and trust services for electronic transactions in the internal market and repealing Directive 1999/93/EC"
,
23 July 2014
,
<
https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32014R0910
>
.
[RFC7592]
Richer, J., Ed.
, Jones, M.
, Bradley, J.
, and M. Machulak
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
[NIST-SP-800-63a]
Grassi, Paul. A.
, Fentony, James L.
, Lefkovitz, Naomi B.
, Danker, Jamie M.
, Choong, Yee-Yin.
, Greene, Kristen K.
, and Mary F. Theofanos
,
"NIST Special Publication 800-63A, Digital Identity Guidelines, Enrollment and Identity Proofing Requirements"
,
June 2017
,
<
https://doi.org/10.6028/NIST.SP.800-63a
>
.
[RFC8707]
Campbell, B.
, Bradley, J.
, and H. Tschofenig
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
[verified_claims_request.json]
OpenID Foundation
,
"JSON Schema for requesting verified_claims"
,
2020
,
<
https://openid.net/wg/ekyc-ida/references/
>
.
[RFC6920]
Farrell, S.
, Kutscher, D.
, Dannewitz, C.
, Ohlman, B.
, Keranen, A.
, and P. Hallam-Baker
,
"Naming Things with Hashes"
,
RFC 6920
,
DOI 10.17487/RFC6920
,
April 2013
,
<
https://www.rfc-editor.org/info/rfc6920
>
.
[FAPI-1-RW]
OpenID Foundation's Financial API (FAPI) Working Group
,
"Financial-grade API - Part 2: Read and Write API Security Profile"
,
9 September 2020
,
<
https://bitbucket.org/openid/fapi/src/master/Financial_API_WD_002.md
>
.
[FAPI-2-BL]
OpenID Foundation's Financial API (FAPI) Working Group
,
"FAPI 2.0 Baseline Profile"
,
9 September 2020
,
<
https://bitbucket.org/openid/fapi/src/master/FAPI_2_0_Baseline_Profile.md
>
.
Appendix A.
IANA Considerations
A.1.
JSON Web Token Claims Registration
This specification requests registration of the following value in the IANA "JSON Web Token Claims Registry" established by
[
RFC7519
]
.
¶
A.1.1.
Registry Contents
Claim Name:
verified_claims
¶
Claim Description:
This container Claim is composed of the verification evidence related to a certain verification process and the corresponding Claims about the End-User which were verified in this process.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Verified Claims
of this document
¶
Claim Name:
place_of_birth
¶
Claim Description:
A structured Claim representing the End-User's place of birth.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
Claim Name:
nationalities
¶
Claim Description:
String array representing the End-User's nationalities.
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
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
Claim Name:
salutation
¶
Claim Description:
End-User's salutation, e.g., "Mr."
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
Claim Name:
title
¶
Claim Description:
End-User's title, e.g., "Dr."
¶
Change Controller:
eKYC and Identity Assurance Working Group - openid-specs-ekyc-ida@lists.openid.net
¶
Specification Document(s):
Section
Claims
of this document
¶
Claim Name:
msisdn
¶
Claim Description:
End-User's mobile phone number formatted according to ITU-T recommendation
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
Claim Name:
also_known_as
¶
Claim Description:
Stage name, religious name or any other type of alias/pseudonym with which a person is known in a specific context besides its legal name. This must be part of the applicable legislation and thus the trust framework (e.g., be an attribute on the identity card).
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
We would like to thank Julian White, Bjorn Hjelm, Stephane Mouy, Alberto Pulido, Joseph Heenan, Vladimir Dzhuvinov, Azusa Kikuchi, Naohiro Fujie, Takahiko Kawasaki, Sebastian Ebling, Marcos Sanz, Tom Jones, Mike Pegman, Michael B. Jones, Jeff Lombardo, Taylor Ongaro, Peter Bainbridge-Clayton, Adrian Field, George Fletcher, Tim Cappalli, Michael Palage, Sascha Preibisch, Giuseppe De Marco, and Nat Sakimura for their valuable feedback and contributions that helped to evolve this specification.
¶
Appendix C.
Notices
Copyright (c) 2022 The OpenID Foundation.
¶
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.
¶
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
¶
Appendix D.
Document History
[[ To be removed from the final specification ]]
¶
-13
   * Preparation for Implementers Draft 4
   * Checked and fixed referencing
   * Added note about issues with JSON null
   * Defined clearly that JSON schema is not normative
   * Various editorial clarifications
   * Added checking of defined end-user claims to JSON schema
   * Clarified OP Metadata wording
¶
-12
¶
introduced
document
evidence type, which is more universal than
id_document
¶
deprecated
id_document
¶
introduced
electronic_record
and
vouch
evidence types
¶
introduced
check_details
&
assurance_details
to provide more detail than
method
¶
added lookahead capabilities for distributed Claims
¶
added support to attach document artifacts
¶
added txn for attachments
¶
changed evidence type
qes
to
electronic_signature
¶
added Claim
also_known_as
¶
added text regarding security profiles
¶
editorial improvements
¶
added further co-authors
¶
added
assurance_level
field
¶
added
assurance_process
type
¶
added text about dependency between identity assurance and authentication assurance
¶
added new field
country_code
to
address
Claim
¶
relaxed requirements for showing purpose
¶
-11
¶
Added support for requesting different sets of Claims with different requirements regarding trust_framework and other verification elements (e.g., evidence)
¶
added
msisdn
Claim
¶
clarified scope of this specification
¶
-10
¶
Editorial improvements
¶
Improved JSON schema (alignment with spec and bug fix)
¶
-09
¶
verified_claims
element may contain one or more Verified Claims objects
¶
an individual assertion may contain
verified_claims
elements in the assertion itself and any aggregated or distributed Claims sets it includes or refers to, respectively
¶
moved all definitions of pre-defined values for trust frameworks, id documents and verification methods to a wiki page as non-normative overview
¶
clarified and simplified request syntax
¶
reduced mandatory requirement
verified_claims
to bare minimum
¶
removed JSON schema from draft and added reference to JSON schema file instead
¶
added request JSON schema
¶
added IANA section with JSON Web Token Claims Registration
¶
integrated source into single md file
¶
added privacy considerations regarding time zone data, enhanced syntax definition of time and date-time fields in spec and response schema
¶
fixed typos
¶
-08
¶
added
uripp
verification method
¶
small fixes to examples
¶
-07
¶
fixed typos
¶
changed
nationality
String Claim to
nationalities
String array Claim
¶
replaced
agent
in id_document verifier element by
txn
element
¶
qes method: fixed error in description of
issuer
¶
qes method: changed
issued_at
to
created_at
since this field applies to the signature (that is created and not issued)
¶
Changed format of
nationalities
and issuing
country
to ICAO codes
¶
Changed
date
in verification element to
time
¶
Added Japanese trust frameworks to pre-defined values
¶
Added Japanese id documents to pre-defined values
¶
adapted JSON schema and examples
¶
-06
¶
Incorporated review feedback by Marcos Sanz and Adam Cooper
¶
Added text on integrity, authenticity, and confidentiality for data passed between OP and RP to Security Considerations section
¶
added
purpose
field to
claims
parameter
¶
added feature to let the RP explicitly requested certain
verification
data
¶
-05
¶
incorporated review feedback by Mike Jones
¶
Added OIDF Copyright Notices
¶
Moved Acknowledgements to Appendix A
¶
Removed RFC 2119 keywords from scope & requirements section and rephrased section
¶
rephrased introduction
¶
replaced
birth_name
with
birth_family_name
,
birth_given_name
, and
birth_middle_name
¶
replaced
transaction_id
with
txn
from RFC 8417
¶
added references to eIDAS, ISO 3166-1, ISO 3166-3, and ISO 8601-2004
¶
added note on
purpose
and locales
¶
changed file name and document title to include 1.0 version id
¶
corrected evidence plural
¶
lots of editorial fixes
¶
Alignment with OpenID Connect Core wording
¶
Renamed
id
to
verification_process
¶
Renamed
verified_person_data
to
verified_claims
¶
-04
¶
incorporated review feedback by Marcos Sanz
¶
-03
¶
enhanced draft to support multiple evidence
¶
added a JSON Schema for assertions containing the
verified_person_data
Claim
¶
added more identity document definitions
¶
added
region
field to
place_of_birth
Claim
¶
changed
eidas_loa_substantial/high
to
eidas_ial_substantial/high
¶
fixed typos in examples
¶
uppercased all editorial occurences of the term
claims
to align with OpenID Connect Core
¶
-02
¶
added new request parameter
purpose
¶
simplified/reduced number of verification methods
¶
simplfied identifiers
¶
added
identity_documents_supported
to metadata section
¶
improved examples
¶
-01
¶
fixed some typos
¶
remove organization element (redundant) (issue 1080)
¶
allow other Claims about the End-User in the
claims
sub element (issue 1079)
¶
changed
legal_context
to
trust_framework
¶
added explanation how the content of the verification element is determined by the trust framework
¶
added URI-based identifiers for
trust_framework
,
identity_document
and (verification)
method
¶
added example attestation for notified/regulated eID system
¶
adopted OP metadata section accordingly
¶
changed error behavior for
max_age
member to alig with OpenID Core
¶
Added feature to let the RP express requirements for verification data (trust framework, identity documents, verification method)
¶
Added privacy consideration section and added text on legal basis for data exchange
¶
Added explanation about regulated and un-regulated eID systems
¶
-00 (WG document)
¶
turned the proposal into a WG document
¶
changed name
¶
added terminology section and reworked introduction
¶
added several examples (ID Token vs UserInfo, unverified & Verified Claims, aggregated & distributed Claims)
¶
incorporated text proposal of Marcos Sanz regarding max_age
¶
added IANA registration for new error code
unable_to_meet_requirement
¶
Authors' Addresses
Torsten Lodderstedt
yes.com
Email:
torsten@lodderstedt.net
Daniel Fett
yes.com
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