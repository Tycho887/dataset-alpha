---
{
  "title": "GitHub - oidc-sweden/openid-federation-base: Implementing an extended profile of the OpenID federation standard · GitHub",
  "url": "https://github.com/idsec-solutions/sc-openid-federation",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 9308,
  "crawled_at": "2026-04-23T20:55:57"
}
---

oidc-sweden
/
openid-federation-base
Public
Notifications
You must be signed in to change notification settings
Fork
1
Star
1
main
Branches
Tags
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
55 Commits
55 Commits
src
src
.gitignore
.gitignore
LICENSE
LICENSE
README.md
README.md
pom.xml
pom.xml
View all files
Repository files navigation
OpenID Federation Base Library
<dependency>
    <groupId>se.oidc.oidfed</groupId>
    <artifactId>openid-federation-base</artifactId>
    <version>${openid-federation-base.version}</version>
</dependency>
About
This library is a core library implementing the OpenID federation standard under development.
This library faithfully implements the latest version of the OpenID federation specification draft,
but adds some features that are specified in the draft national Swedish OpenID federation profile.
Core features:
Serializers and builders for OpenID federation data types
Metadata policy support
Chain validation
This library is based on JWT processing from Nimbus combined with JSON processing from Jackson
Since version 3.0.0 this library has removed the metadata support and moved this into a separate lib located at
https://github.com/oidc-sweden/openid-federation-metadata
.
Extended features
This library addresses the challenges documented in
OIDC Sweden - OpenID Federation Challenges
.
This means that the chain validation has implemented support for an additional Entity Statement claim
subject_entity_configuration_location
. This claim is optional to specify the location of the subordinate Entity Configuration, which may be a custom location or embedded using the data URI scheme. The rationale for this additional claim is to support early adoption of leaf entities that does not have the capability of publishing Entity Configuration at the required location.
This implementation also supports some extended policy operators:
regex - one or more regular expressions that must match all metadata values.
intersects - At least one of the policy values must match at least one of the metadata values.
All extended features are specified in
OIDC Sweden - OpenID Federation Profile
Language support and extended serializers
This library implements extended serializers to support:
Multi language support for metadata parameters
Possible updates to metadata policy expression
Language support
Multi-language support is provided in all Metadata classes by assigning the metadata parameter to the LanguageObject value class.
When serialized to JSON, this object type produces language tagged json parameter names.
When JSON string is deserialized to a Java object, then a LanguageObject value is created, allowing structured access to language tagged data.
This functionality is implemented by the
OidcLangJsonSerializer
class.
Metadata policy serialization
The
MetadataPolicySerializer
provides an interface for serialization of metadata policy between JSON and Java objects. This allows independent customization of metadata policy expression formats, under discussion. If the expression format changes, then this can be handled by a separate implementation of this serializer.
Builder support
All essential federation data objects are supported by builders.
This is illustrated by the following example used to build and sign an Entity Statement object
final
EntityStatement
entityStatement
=
EntityStatement
.
builder
()
  .
issuer
(
"issuer"
)
  .
subject
(
"subject"
)
  .
expriationTime
(
Date
.
from
(
Instant
.
now
().
plusSeconds
(
180
)))
  .
issueTime
(
new
Date
())
  .
definedParams
(
EntityStatementDefinedParams
.
builder
()
    .
authorityHints
(
List
.
of
(
"hint1"
,
"hint2"
))
    .
constraints
(
ConstraintsClaim
.
builder
()
      .
allowedLeafEntityTypes
(
List
.
of
(
"openid_relying_party"
,
"openid_provider"
))
      .
maxPathLength
(
2
)
      .
namingConstraints
(
NamingConstraints
.
builder
()
        .
excluded
(
List
.
of
(
"https://example.com/excluded"
))
        .
permitted
(
List
.
of
(
"https://example.com/permitted"
))
        .
build
())
      .
build
())
    .
subjectEntityConfigurationLocation
(
"https://example.com/entity-configuration"
,
true
)
    .
addCriticalClaim
(
"other_critical_claim"
)
    .
jwkSet
(
this
.
getJwkSet
(
TestCredentials
.
p256Credential
.
getCertificate
()))
    .
metadata
(
EntityMetadataInfoClaim
.
builder
()
      .
opMetadataObject
(
TestMetadata
.
opMetadata
)
      .
oidcRelyingPartyMetadataObject
(
TestMetadata
.
rpMetadata
)
      .
build
())
    .
addPolicyLanguageCriticalClaim
(
RegexpPolicyOperator
.
OPERATOR_NAME
)
    .
addPolicyLanguageCriticalClaim
(
ValuePolicyOperator
.
OPERATOR_NAME
)
    .
addPolicyLanguageCriticalClaim
(
SkipSubordinatesPolicyOperator
.
OPERATOR_NAME
)
    .
metadataPolicy
(
EntityMetadataInfoClaim
.
builder
()
      .
opMetadataObject
(
serializer
.
toJsonObject
(
EntityTypeMetadataPolicy
.
builder
()
        .
addMetadataParameterPolicy
(
MetadataParameterPolicy
.
builder
(
PolicyParameterFormats
.
issuer
.
toMetadataParameter
())
            .
add
(
RegexpPolicyOperator
.
OPERATOR_NAME
,
OidcUtils
.
URI_REGEXP
)
            .
build
())
        .
addMetadataParameterPolicy
(
MetadataParameterPolicy
.
builder
(
PolicyParameterFormats
.
acr_values_supported
.
toMetadataParameter
())
          .
add
(
SubsetOfPolicyOperator
.
OPERATOR_NAME
,
List
.
of
(
"http://id.elegnamnden.se/loa/1.0/loa3"
,
"http://id.elegnamnden.se/loa/1.0/loa4"
,
"http://id.elegnamnden.se/loa/1.0/eidas-sub"
,
"http://id.elegnamnden.se/loa/1.0/eidas-nf-sub"
,
"http://id.elegnamnden.se/loa/1.0/eidas-high"
,
"http://id.elegnamnden.se/loa/1.0/eidas-nf-high"
))
          .
add
(
RegexpPolicyOperator
.
OPERATOR_NAME
,
List
.
of
(
OidcUtils
.
URI_REGEXP
,
"^.{3,}$"
))
          .
build
())
        .
build
()))
      .
build
())
    .
sourceEndpoint
(
"http://example.com/source"
)
    .
trustMarkIssuers
(
TrustMarkIssuersBuilder
.
getInstance
()
      .
trustMark
(
"https://example.com/tm1"
,
List
.
of
(
"https://example.com/issuer1"
))
      .
trustMark
(
"https://example.com/tm2"
,
List
.
of
(
"https://example.com/issuer1"
,
"https://example.com/issuer2"
))
      .
build
())
    .
trustMarks
(
List
.
of
(
TrustMarkClaim
.
builder
()
        .
trustMarkId
(
"https://example.com/tm1"
)
        .
trustMark
(
TrustMark
.
builder
()
          .
trustMarkId
(
"https://example.com/tm1"
)
          .
subject
(
"https://example.com/subject"
)
          .
issueTime
(
new
Date
())
          .
issuer
(
"https://example.com/trust_mark_issuer"
)
          .
build
(
TestCredentials
.
p256JwtCredential
,
null
).
getSignedJWT
().
serialize
())
        .
build
(),
TrustMarkClaim
.
builder
()
        .
trustMarkId
(
"https://example.com/tm2"
)
        .
trustMark
(
"Signed trust mark JWT"
)
        .
build
()))
    .
trustMarkOwners
(
TrustMarkOwnersBuilder
.
getInstance
()
      .
trustMark
(
"https://example.com/tm1"
,
"https://example.com/owner1"
,
this
.
getJwkSet
(
TestCredentials
.
p256Credential
.
getCertificate
()))
      .
trustMark
(
"https://example.com/tm2"
,
"https://example.com/owner2"
,
this
.
getJwkSet
(
TestCredentials
.
p256Credential
.
getCertificate
()))
      .
build
())
    .
build
())
  .
build
(
TestCredentials
.
p256JwtCredential
,
null
);
The example and its necessary dependencies are illustrated in the EntityStatementTest class.
Parsing from Signed JWT back to java objects is illustrated by the following example:
EntityStatement
parsedEntityStatement
=
new
EntityStatement
(
signedEntityStatementJwt
);
Map
<
String
,
Object
>
opMetadataObject
=
parsedEntityStatement
.
getMetadata
().
getOpMetadataObject
();
OpMetadata
parsedOpMetadata
=
OpMetadata
.
getJsonSerializer
().
parse
(
opMetadataObject
);
Chain validation
This implementation separates chain validation from Trust Mark validation.
The primary reason for this is that chain validation is used as a subcomponent of Trust Mark validation.
Chain validation implementation
Chain validation is supported by implementing the
FederationChainValidator
interface.
A default implementation is provided by
DefaultFederationChainValidator
.
Trust Mark validation implementation
Trust Mark validation is supported by implementing the
TrustMarkValidator
interface.
A default implementation is provided by
DefaultTrustMarkValidator
The default implementation of the Trust Mark validator also requires implementations of:
TrustMarkStatusResolver
- Providing the status of TrustMarks.
FederationPathBuilder
- Providing the chain path from Trust Anchor to target entity.
These interfaces are not implemented in this library.
Copyright © 2024,
OIDC Sweden
. Licensed under version 2.0 of the
Apache License
.
About
Implementing an extended profile of the OpenID federation standard
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
1
star
Watchers
4
watching
Forks
1
fork
Report repository
Releases
7
4.0.0 version
Latest
May 5, 2025
+ 6 releases
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
Uh oh!
There was an error while loading.
Please reload this page
.
Contributors
Uh oh!
There was an error while loading.
Please reload this page
.
Languages
Java
100.0%