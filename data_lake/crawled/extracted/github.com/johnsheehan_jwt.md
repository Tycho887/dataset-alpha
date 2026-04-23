---
{
  "title": "GitHub - jwt-dotnet/jwt: Jwt.Net, a JWT (JSON Web Token) implementation for .NET · GitHub",
  "url": "https://github.com/johnsheehan/jwt",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 10826,
  "crawled_at": "2026-04-23T20:48:44"
}
---

jwt-dotnet
/
jwt
Public
Notifications
You must be signed in to change notification settings
Fork
467
Star
2.2k
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
321 Commits
321 Commits
.github
.github
.pipelines
.pipelines
src
src
tests
tests
.editorconfig
.editorconfig
.gitignore
.gitignore
CHANGELOG.md
CHANGELOG.md
Directory.Build.props
Directory.Build.props
JWT.sln
JWT.sln
JWT.sln.DotSettings
JWT.sln.DotSettings
JwtStrongNameKey.snk
JwtStrongNameKey.snk
LICENSE.md
LICENSE.md
NuGet.config
NuGet.config
README.md
README.md
View all files
Repository files navigation
Jwt.Net, a JWT (JSON Web Token) implementation for .NET
Sponsor
Avaliable NuGet packages
Supported .NET versions:
Jwt.NET
Creating (encoding) token
Or using the fluent builder API
Parsing (decoding) and verifying token
Or using the fluent builder API
Or using the fluent builder API
Validate token expiration
Parsing (decoding) token header
Or using the fluent builder API
Turning off parts of token validation
Or using the fluent builder API
Custom JSON serializer
Custom JSON serialization settings with the default JsonNetSerializer
Jwt.Net ASP.NET Core
Register authentication handler to validate JWT
Custom factories to produce Identity or AuthenticationTicket
License
Jwt.Net, a JWT (JSON Web Token) implementation for .NET
This library supports generating and decoding
JSON Web Tokens
.
Sponsor
If you want to quickly implement a secure authentication to your JWT project,
create an Auth0 account
; it's Free!
Avaliable NuGet packages
Jwt.Net
Jwt.Net for Microsoft Dependency Injection container
Jwt.Net for ASP.NET Core
Supported .NET versions:
.NET Framework 3.5
.NET Framework 4.0 - 4.8
.NET Standard 1.3, 2.0
.NET 6.0
Jwt.NET
Creating (encoding) token
var
payload
=
new
Dictionary
<
string
,
object
>
{
{
"claim1"
,
0
}
,
{
"claim2"
,
"claim2-value"
}
}
;
IJwtAlgorithm
algorithm
=
new
RS256Algorithm
(
certificate
)
;
IJsonSerializer
serializer
=
new
JsonNetSerializer
(
)
;
IBase64UrlEncoder
urlEncoder
=
new
JwtBase64UrlEncoder
(
)
;
IJwtEncoder
encoder
=
new
JwtEncoder
(
algorithm
,
serializer
,
urlEncoder
)
;
const
string
key
=
null
;
// not needed if algorithm is asymmetric
var
token
=
encoder
.
Encode
(
payload
,
key
)
;
Console
.
WriteLine
(
token
)
;
Or using the fluent builder API
var
token
=
JwtBuilder
.
Create
(
)
.
WithAlgorithm
(
new
RS256Algorithm
(
certificate
)
)
.
AddClaim
(
"exp"
,
DateTimeOffset
.
UtcNow
.
AddHours
(
1
)
.
ToUnixTimeSeconds
(
)
)
.
AddClaim
(
"claim1"
,
0
)
.
AddClaim
(
"claim2"
,
"claim2-value"
)
.
Encode
(
)
;
Console
.
WriteLine
(
token
)
;
Parsing (decoding) and verifying token
try
{
IJsonSerializer
serializer
=
new
JsonNetSerializer
(
)
;
IDateTimeProvider
provider
=
new
UtcDateTimeProvider
(
)
;
IJwtValidator
validator
=
new
JwtValidator
(
serializer
,
provider
)
;
IBase64UrlEncoder
urlEncoder
=
new
JwtBase64UrlEncoder
(
)
;
IJwtAlgorithm
algorithm
=
new
RS256Algorithm
(
certificate
)
;
IJwtDecoder
decoder
=
new
JwtDecoder
(
serializer
,
validator
,
urlEncoder
,
algorithm
)
;
var
json
=
decoder
.
Decode
(
token
)
;
Console
.
WriteLine
(
json
)
;
}
catch
(
TokenNotYetValidException
)
{
Console
.
WriteLine
(
"Token is not valid yet"
)
;
}
catch
(
TokenExpiredException
)
{
Console
.
WriteLine
(
"Token has expired"
)
;
}
catch
(
SignatureVerificationException
)
{
Console
.
WriteLine
(
"Token has invalid signature"
)
;
}
Or using the fluent builder API
var
json
=
JwtBuilder
.
Create
(
)
.
WithAlgorithm
(
new
RS256Algorithm
(
certificate
)
)
.
MustVerifySignature
(
)
.
Decode
(
token
)
;
Console
.
WriteLine
(
json
)
;
The output would be:
{ "claim1": 0, "claim2": "claim2-value" }
You can also deserialize the JSON payload directly to a .NET type:
var
payload
=
decoder
.
DecodeToObject
<
IDictionary
<
string
,
object
>
>
(
token
,
secret
)
;
Or using the fluent builder API
var
payload
=
JwtBuilder
.
Create
(
)
.
WithAlgorithm
(
new
RS256Algorithm
(
certificate
)
)
.
WithSecret
(
secret
)
.
MustVerifySignature
(
)
.
Decode
<
IDictionary
<
string
,
object
>
>
(
token
)
;
Validate token expiration
As described in the
RFC 7519 section 4.1.4
:
The
exp
claim identifies the expiration time on or after which the JWT MUST NOT be accepted for processing.
If it is present in the payload and is past the current time, the token will fail verification. The value must be specified as the number of seconds since the
Unix epoch
, 1/1/1970 00:00:00 UTC.
IDateTimeProvider
provider
=
new
UtcDateTimeProvider
(
)
;
var
now
=
provider
.
GetNow
(
)
.
AddMinutes
(
-
5
)
;
// token has expired 5 minutes ago
double
secondsSinceEpoch
=
UnixEpoch
.
GetSecondsSince
(
now
)
;
var
payload
=
new
Dictionary
<
string
,
object
>
{
{
"exp"
,
secondsSinceEpoch
}
}
;
var
token
=
encoder
.
Encode
(
payload
)
;
decoder
.
Decode
(
token
)
;
// throws TokenExpiredException
Then, as described in the
RFC 7519 section 4.1.5
:
The "nbf" (not before) claim identifies the time before which the JWT MUST NOT be accepted for processing
If it is present in the payload and is prior to the current time, the token will fail verification.
Parsing (decoding) token header
IJsonSerializer
serializer
=
new
JsonNetSerializer
(
)
;
IBase64UrlEncoder
urlEncoder
=
new
JwtBase64UrlEncoder
(
)
;
IJwtDecoder
decoder
=
new
JwtDecoder
(
serializer
,
urlEncoder
)
;
JwtHeader
header
=
decoder
.
DecodeHeader
<
JwtHeader
>
(
token
)
;
var
typ
=
header
.
Type
;
// JWT
var
alg
=
header
.
Algorithm
;
// RS256
var
kid
=
header
.
KeyId
;
// CFAEAE2D650A6CA9862575DE54371EA980643849
Or using the fluent builder API
JwtHeader
header
=
JwtBuilder
.
Create
(
)
.
DecodeHeader
<
JwtHeader
>
(
token
)
;
var
typ
=
header
.
Type
;
// JWT
var
alg
=
header
.
Algorithm
;
// RS256
var
kid
=
header
.
KeyId
;
// CFAEAE2D650A6CA9862575DE54371EA980643849
Turning off parts of token validation
If you'd like to validate a token but ignore certain parts of the validation (such as whether to the token has expired or not valid yet), you can pass a
ValidateParameters
object to the constructor of the
JwtValidator
class.
var
validationParameters
=
new
ValidationParameters
{
ValidateSignature
=
true
,
ValidateExpirationTime
=
false
,
ValidateIssuedTime
=
false
,
TimeMargin
=
100
}
;
IJwtValidator
validator
=
new
JwtValidator
(
serializer
,
provider
,
validationParameters
)
;
IJwtDecoder
decoder
=
new
JwtDecoder
(
serializer
,
validator
,
urlEncoder
,
algorithm
)
;
var
json
=
decoder
.
Decode
(
expiredToken
)
;
// will not throw because of expired token
Or using the fluent builder API
var
json
=
JwtBuilder
.
Create
(
)
.
WithAlgorithm
(
new
RS256Algorirhm
(
certificate
)
)
.
WithSecret
(
secret
)
.
WithValidationParameters
(
new
ValidationParameters
{
ValidateSignature
=
true
,
ValidateExpirationTime
=
false
,
ValidateIssuedTime
=
false
,
TimeMargin
=
100
}
)
.
Decode
(
expiredToken
)
;
Custom JSON serializer
By default JSON serialization is performed by JsonNetSerializer implemented using
Json.Net
. To use a different one, implement the
IJsonSerializer
interface:
public
sealed
class
CustomJsonSerializer
:
IJsonSerializer
{
public
string
Serialize
(
object
obj
)
{
// Implement using favorite JSON serializer
}
public
T
Deserialize
<
T
>
(
string
json
)
{
// Implement using favorite JSON serializer
}
}
And then pass this serializer to JwtEncoder constructor:
IJwtAlgorithm
algorithm
=
new
RS256Algorirhm
(
certificate
)
;
IJsonSerializer
serializer
=
new
CustomJsonSerializer
(
)
;
IBase64UrlEncoder
urlEncoder
=
new
JwtBase64UrlEncoder
(
)
;
IJwtEncoder
encoder
=
new
JwtEncoder
(
algorithm
,
serializer
,
urlEncoder
)
;
Custom JSON serialization settings with the default JsonNetSerializer
As mentioned above, the default JSON serialization is done by
JsonNetSerializer
. You can define your own custom serialization settings as follows:
JsonSerializer
customJsonSerializer
=
new
JsonSerializer
{
// All keys start with lowercase characters instead of the exact casing of the model/property, e.g. fullName
ContractResolver
=
new
CamelCasePropertyNamesContractResolver
(
)
,
// Nice and easy to read, but you can also use Formatting.None to reduce the payload size
Formatting
=
Formatting
.
Indented
,
// The most appropriate datetime format.
DateFormatHandling
=
DateFormatHandling
.
IsoDateFormat
,
// Don't add keys/values when the value is null.
NullValueHandling
=
NullValueHandling
.
Ignore
,
// Use the enum string value, not the implicit int value, e.g. "red" for enum Color { Red }
Converters
.
Add
(
new
StringEnumConverter
(
)
)
}
;
IJsonSerializer
serializer
=
new
JsonNetSerializer
(
customJsonSerializer
)
;
Jwt.Net ASP.NET Core
Register authentication handler to validate JWT
public
void
ConfigureServices
(
IServiceCollection
services
)
{
services
.
AddAuthentication
(
options
=>
{
options
.
DefaultAuthenticateScheme
=
JwtAuthenticationDefaults
.
AuthenticationScheme
;
options
.
DefaultChallengeScheme
=
JwtAuthenticationDefaults
.
AuthenticationScheme
;
}
)
.
AddJwt
(
options
=>
{
// secrets, required only for symmetric algorithms, such as HMACSHA256Algorithm
// options.Keys = new[] { "mySecret" };
// optionally; disable throwing an exception if JWT signature is invalid
// options.VerifySignature = false;
}
)
;
// the non-generic version AddJwt() requires registering an instance of IAlgorithmFactory manually
services
.
AddSingleton
<
IAlgorithmFactory
>
(
new
RSAlgorithmFactory
(
certificate
)
)
;
// or
services
.
AddSingleton
<
IAlgorithmFactory
>
(
new
DelegateAlgorithmFactory
(
algorithm
)
)
;
// or use the generic version AddJwt<TFactory() to use a custom implementation of IAlgorithmFactory
.
AddJwt
<
MyCustomAlgorithmFactory
>
(
options
=>
..
.
)
;
}
public
void
Configure
(
IApplicationBuilder
app
)
{
app
.
UseAuthentication
(
)
;
}
Custom factories to produce Identity or AuthenticationTicket
services
.
AddSingleton
<
IIdentityFactory
,
CustomIdentityFctory
>
(
)
;
services
.
AddSingleton
<
ITicketFactory
,
CustomTicketFactory
>
(
)
;
License
The following projects and their resulting packages are licensed under Public Domain, see the
LICENSE#Public-Domain
file.
JWT
The following projects and their resulting packages are licensed under the MIT License, see the
LICENSE#MIT
file.
JWT.Extensions.AspNetCore
JWT.Extensions.DependencyInjection
About
Jwt.Net, a JWT (JSON Web Token) implementation for .NET
Topics
c-sharp
json
jwt
authorization
Resources
Readme
License
View license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
2.2k
stars
Watchers
81
watching
Forks
467
forks
Report repository
Releases
87
Jwt 20241203.4
Latest
Dec 4, 2024
+ 86 releases
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
C#
100.0%