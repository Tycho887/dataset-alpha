---
{
  "title": "JSON Object Signing and Encryption (JOSE)",
  "url": "https://www.iana.org/assignments/jose/jose.xhtml",
  "domain": "www.iana.org",
  "depth": 2,
  "relevance_score": 0.15,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 19001,
  "crawled_at": "2026-04-23T20:56:27"
}
---

JSON Object Signing and Encryption (JOSE)
Created
2015-01-23
Last Updated
2026-02-05
Available Formats
XML
HTML
Plain text
Registries Included Below
JSON Web Signature and Encryption Header Parameters
JSON Web Signature and Encryption Algorithms
JSON Web Encryption Compression Algorithms
JSON Web Key Types
JSON Web Key Elliptic Curve
JSON Web Key Parameters
JSON Web Key Use
JSON Web Key Operations
JSON Web Key Set Parameters
JSON Web Signature and Encryption Header Parameters
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7515
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7515
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Header Parameter Name
Header Parameter Description
Header Parameter Usage Location(s)
Change Controller
Reference
alg
Algorithm
JWS
[
IESG
]
[
RFC7515, Section 4.1.1
]
jku
JWK Set URL
JWS
[
IESG
]
[
RFC7515, Section 4.1.2
]
jwk
JSON Web Key
JWS
[
IESG
]
[
RFC7515, Section 4.1.3
]
kid
Key ID
JWS
[
IESG
]
[
RFC7515, Section 4.1.4
]
x5u
X.509 URL
JWS
[
IESG
]
[
RFC7515, Section 4.1.5
]
x5c
X.509 Certificate Chain
JWS
[
IESG
]
[
RFC7515, Section 4.1.6
]
x5t
X.509 Certificate SHA-1 Thumbprint
JWS
[
IESG
]
[
RFC7515, Section 4.1.7
]
x5t#S256
X.509 Certificate SHA-256 Thumbprint
JWS
[
IESG
]
[
RFC7515, Section 4.1.8
]
typ
Type
JWS
[
IESG
]
[
RFC7515, Section 4.1.9
]
cty
Content Type
JWS
[
IESG
]
[
RFC7515, Section 4.1.10
]
crit
Critical
JWS
[
IESG
]
[
RFC7515, Section 4.1.11
]
alg
Algorithm
JWE
[
IESG
]
[
RFC7516, Section 4.1.1
]
enc
Encryption Algorithm
JWE
[
IESG
]
[
RFC7516, Section 4.1.2
]
zip
Compression Algorithm
JWE
[
IESG
]
[
RFC7516, Section 4.1.3
]
jku
JWK Set URL
JWE
[
IESG
]
[
RFC7516, Section 4.1.4
]
jwk
JSON Web Key
JWE
[
IESG
]
[
RFC7516, Section 4.1.5
]
kid
Key ID
JWE
[
IESG
]
[
RFC7516, Section 4.1.6
]
x5u
X.509 URL
JWE
[
IESG
]
[
RFC7516, Section 4.1.7
]
x5c
X.509 Certificate Chain
JWE
[
IESG
]
[
RFC7516, Section 4.1.8
]
x5t
X.509 Certificate SHA-1 Thumbprint
JWE
[
IESG
]
[
RFC7516, Section 4.1.9
]
x5t#S256
X.509 Certificate SHA-256 Thumbprint
JWE
[
IESG
]
[
RFC7516, Section 4.1.10
]
typ
Type
JWE
[
IESG
]
[
RFC7516, Section 4.1.11
]
cty
Content Type
JWE
[
IESG
]
[
RFC7516, Section 4.1.12
]
crit
Critical
JWE
[
IESG
]
[
RFC7516, Section 4.1.13
]
epk
Ephemeral Public Key
JWE
[
IESG
]
[
RFC7518, Section 4.6.1.1
]
apu
Agreement PartyUInfo
JWE
[
IESG
]
[
RFC7518, Section 4.6.1.2
]
apv
Agreement PartyVInfo
JWE
[
IESG
]
[
RFC7518, Section 4.6.1.3
]
iv
Initialization Vector
JWE
[
IESG
]
[
RFC7518, Section 4.7.1.1
]
tag
Authentication Tag
JWE
[
IESG
]
[
RFC7518, Section 4.7.1.2
]
p2s
PBES2 Salt Input
JWE
[
IESG
]
[
RFC7518, Section 4.8.1.1
]
p2c
PBES2 Count
JWE
[
IESG
]
[
RFC7518, Section 4.8.1.2
]
iss
Issuer
JWE
[
IESG
]
[
RFC7519, Section 4.1.1
]
sub
Subject
JWE
[
IESG
]
[
RFC7519, Section 4.1.2
]
aud
Audience
JWE
[
IESG
]
[
RFC7519, Section 4.1.3
]
b64
Base64url-Encode Payload
JWS
[
IESG
]
[
RFC7797, Section 3
]
ppt
PASSporT extension identifier
JWS
[
IESG
]
[
RFC8225, Section 8.1
]
url
URL
JWE, JWS
[
IESG
]
[
RFC8555, Section 6.4.1
]
nonce
Nonce
JWE, JWS
[
IESG
]
[
RFC8555, Section 6.5.2
]
svt
Signature Validation Token
JWS
[
IETF
]
[
RFC9321
]
iheSSId
The iheSSId header parameter's value shall specify the SubmissionSet.uniqueId as per [
https://profiles.ihe.net/ITI/TF/Volume3/ch-4.2.html#4.2.3.3.12
].
JWS
[
IHE_ITI
]
[
https://profiles.ihe.net/ITI/DSGj/Volume3/ch-5.10.html#5.10
]
jwt
This header contains a JWT. Processing rules MAY depend on the typ header value of the respective JWT.
JWS
[
OpenID_Foundation_Digital_Credentials_Protocols_Working_Group
]
[
OpenID for Verifiable Presentations 1.0, Section 12
]
client_id
This header contains a Client Identifier. A Client Identifier is used in OAuth to identify a certain client. It is defined in [
RFC6749
], section 2.2.
JWS
[
IETF
]
[
RFC6749
]
trust_chain
OpenID Federation Trust Chain
JWS
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 4.3
]
peer_trust_chain
OpenID Federation Peer Trust Chain
JWS
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 4.4
]
JSON Web Signature and Encryption Algorithms
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7518
][
RFC9864, Section 4.3.1
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7518
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Algorithm Name
Algorithm Description
Algorithm Usage Location(s)
JOSE Implementation Requirements
Change Controller
Reference
Algorithm Analysis Document(s)
HS256
HMAC using SHA-256
alg
Required
[
IESG
]
[
RFC7518, Section 3.2
]
n/a
HS384
HMAC using SHA-384
alg
Optional
[
IESG
]
[
RFC7518, Section 3.2
]
n/a
HS512
HMAC using SHA-512
alg
Optional
[
IESG
]
[
RFC7518, Section 3.2
]
n/a
RS256
RSASSA-PKCS1-v1_5 using SHA-256
alg
Recommended
[
IESG
]
[
RFC7518, Section 3.3
]
n/a
RS384
RSASSA-PKCS1-v1_5 using SHA-384
alg
Optional
[
IESG
]
[
RFC7518, Section 3.3
]
n/a
RS512
RSASSA-PKCS1-v1_5 using SHA-512
alg
Optional
[
IESG
]
[
RFC7518, Section 3.3
]
n/a
ES256
ECDSA using P-256 and SHA-256
alg
Recommended+
[
IESG
]
[
RFC7518, Section 3.4
]
n/a
ES384
ECDSA using P-384 and SHA-384
alg
Optional
[
IESG
]
[
RFC7518, Section 3.4
]
n/a
ES512
ECDSA using P-521 and SHA-512
alg
Optional
[
IESG
]
[
RFC7518, Section 3.4
]
n/a
PS256
RSASSA-PSS using SHA-256 and MGF1 with SHA-256
alg
Optional
[
IESG
]
[
RFC7518, Section 3.5
]
n/a
PS384
RSASSA-PSS using SHA-384 and MGF1 with SHA-384
alg
Optional
[
IESG
]
[
RFC7518, Section 3.5
]
n/a
PS512
RSASSA-PSS using SHA-512 and MGF1 with SHA-512
alg
Optional
[
IESG
]
[
RFC7518, Section 3.5
]
n/a
none
No digital signature or MAC performed
alg
Optional
[
IESG
]
[
RFC7518, Section 3.6
]
n/a
RSA1_5
RSAES-PKCS1-v1_5
alg
Recommended-
[
IESG
]
[
RFC7518, Section 4.2
]
n/a
RSA-OAEP
RSAES OAEP using default parameters
alg
Recommended+
[
IESG
]
[
RFC7518, Section 4.3
]
n/a
RSA-OAEP-256
RSAES OAEP using SHA-256 and MGF1 with SHA-256
alg
Optional
[
IESG
]
[
RFC7518, Section 4.3
]
n/a
A128KW
AES Key Wrap using 128-bit key
alg
Recommended
[
IESG
]
[
RFC7518, Section 4.4
]
n/a
A192KW
AES Key Wrap using 192-bit key
alg
Optional
[
IESG
]
[
RFC7518, Section 4.4
]
n/a
A256KW
AES Key Wrap using 256-bit key
alg
Recommended
[
IESG
]
[
RFC7518, Section 4.4
]
n/a
dir
Direct use of a shared symmetric key
alg
Recommended
[
IESG
]
[
RFC7518, Section 4.5
]
n/a
ECDH-ES
ECDH-ES using Concat KDF
alg
Recommended+
[
IESG
]
[
RFC7518, Section 4.6
]
n/a
ECDH-ES+A128KW
ECDH-ES using Concat KDF and "A128KW" wrapping
alg
Recommended
[
IESG
]
[
RFC7518, Section 4.6
]
n/a
ECDH-ES+A192KW
ECDH-ES using Concat KDF and "A192KW" wrapping
alg
Optional
[
IESG
]
[
RFC7518, Section 4.6
]
n/a
ECDH-ES+A256KW
ECDH-ES using Concat KDF and "A256KW" wrapping
alg
Recommended
[
IESG
]
[
RFC7518, Section 4.6
]
n/a
A128GCMKW
Key wrapping with AES GCM using 128-bit key
alg
Optional
[
IESG
]
[
RFC7518, Section 4.7
]
n/a
A192GCMKW
Key wrapping with AES GCM using 192-bit key
alg
Optional
[
IESG
]
[
RFC7518, Section 4.7
]
n/a
A256GCMKW
Key wrapping with AES GCM using 256-bit key
alg
Optional
[
IESG
]
[
RFC7518, Section 4.7
]
n/a
PBES2-HS256+A128KW
PBES2 with HMAC SHA-256 and "A128KW" wrapping
alg
Optional
[
IESG
]
[
RFC7518, Section 4.8
]
n/a
PBES2-HS384+A192KW
PBES2 with HMAC SHA-384 and "A192KW" wrapping
alg
Optional
[
IESG
]
[
RFC7518, Section 4.8
]
n/a
PBES2-HS512+A256KW
PBES2 with HMAC SHA-512 and "A256KW" wrapping
alg
Optional
[
IESG
]
[
RFC7518, Section 4.8
]
n/a
A128CBC-HS256
AES_128_CBC_HMAC_SHA_256 authenticated encryption algorithm
enc
Required
[
IESG
]
[
RFC7518, Section 5.2.3
]
n/a
A192CBC-HS384
AES_192_CBC_HMAC_SHA_384 authenticated encryption algorithm
enc
Optional
[
IESG
]
[
RFC7518, Section 5.2.4
]
n/a
A256CBC-HS512
AES_256_CBC_HMAC_SHA_512 authenticated encryption algorithm
enc
Required
[
IESG
]
[
RFC7518, Section 5.2.5
]
n/a
A128GCM
AES GCM using 128-bit key
enc
Recommended
[
IESG
]
[
RFC7518, Section 5.3
]
n/a
A192GCM
AES GCM using 192-bit key
enc
Optional
[
IESG
]
[
RFC7518, Section 5.3
]
n/a
A256GCM
AES GCM using 256-bit key
enc
Recommended
[
IESG
]
[
RFC7518, Section 5.3
]
n/a
EdDSA
EdDSA signature algorithms
alg
Deprecated
[
IETF
]
[
RFC9864, Section 2.2
]
[
RFC8032
]
RS1
RSASSA-PKCS1-v1_5 with SHA-1
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
RSA-OAEP-384
RSA-OAEP using SHA-384 and MGF1 with SHA-384
alg
Optional
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
n/a
RSA-OAEP-512
RSA-OAEP using SHA-512 and MGF1 with SHA-512
alg
Optional
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
n/a
A128CBC
AES CBC using 128 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
A192CBC
AES CBC using 192 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
A256CBC
AES CBC using 256 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
A128CTR
AES CTR using 128 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
A192CTR
AES CTR using 192 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
A256CTR
AES CTR using 256 bit key
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
HS1
HMAC using SHA-1
JWK
Prohibited
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
[
draft-irtf-cfrg-webcrypto-algorithms-00
]
ES256K
ECDSA using secp256k1 curve and SHA-256
alg
Optional
[
IESG
]
[
RFC8812, Section 3.2
]
[
SEC2
]
ML-DSA-44
ML-DSA-44 as described in US NIST FIPS 204
alg
Optional
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
[
FIPS-204
]
ML-DSA-65
ML-DSA-65 as described in US NIST FIPS 204
alg
Optional
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
[
FIPS-204
]
ML-DSA-87
ML-DSA-87 as described in US NIST FIPS 204
alg
Optional
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
[
FIPS-204
]
Ed25519
EdDSA using the Ed25519 parameter set in Section 5.1 of [
RFC8032
]
alg
Optional
[
IETF
]
[
RFC9864, Section 2.2
]
[
RFC8032
]
Ed448
EdDSA using the Ed448 parameter set in Section 5.2 of [
RFC8032
]
alg
Optional
[
IETF
]
[
RFC9864, Section 2.2
]
[
RFC8032
]
JSON Web Encryption Compression Algorithms
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7518
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7518
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Compression Algorithm Value
Compression Algorithm Description
Change Controller
Reference
DEF
DEFLATE
[
IESG
]
[
RFC7516
]
JSON Web Key Types
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7518
][
RFC7638
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7518
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
"kty" Parameter Value
Key Type Description
JOSE Implementation Requirements
Change Controller
Reference
EC
Elliptic Curve
Recommended+
[
IESG
]
[
RFC7518, Section 6.2
]
RSA
RSA
Required
[
IESG
]
[
RFC7518, Section 6.3
]
oct
Octet sequence
Required
[
IESG
]
[
RFC7518, Section 6.4
]
OKP
Octet string key pairs
Optional
[
IESG
]
[
RFC8037, Section 2
]
AKP
Algorithm Key Pair
Optional
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
JSON Web Key Elliptic Curve
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7518
][
RFC7638
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7518
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Curve Name
Curve Description
JOSE Implementation Requirements
Change Controller
Reference
P-256
P-256 Curve
Recommended+
[
IESG
]
[
RFC7518, Section 6.2.1.1
]
P-384
P-384 Curve
Optional
[
IESG
]
[
RFC7518, Section 6.2.1.1
]
P-521
P-521 Curve
Optional
[
IESG
]
[
RFC7518, Section 6.2.1.1
]
Ed25519
Ed25519 signature algorithm key pairs
Optional
[
IESG
]
[
RFC8037, Section 3.1
]
Ed448
Ed448 signature algorithm key pairs
Optional
[
IESG
]
[
RFC8037, Section 3.1
]
X25519
X25519 function key pairs
Optional
[
IESG
]
[
RFC8037, Section 3.2
]
X448
X448 function key pairs
Optional
[
IESG
]
[
RFC8037, Section 3.2
]
secp256k1
SECG secp256k1 curve
Optional
[
IESG
]
[
RFC8812, Section 3.1
]
JSON Web Key Parameters
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7517
][
RFC7638
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7517
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Parameter Name
Parameter Description
Used with "kty" Value(s)
Parameter Information Class
Change Controller
Reference
kty
Key Type
*
Public
[
IESG
]
[
RFC7517, Section 4.1
]
use
Public Key Use
*
Public
[
IESG
]
[
RFC7517, Section 4.2
]
key_ops
Key Operations
*
Public
[
IESG
]
[
RFC7517, Section 4.3
]
alg
Algorithm
*
Public
[
IESG
]
[
RFC7517, Section 4.4
]
kid
Key ID
*
Public
[
IESG
]
[
RFC7517, Section 4.5
]
x5u
X.509 URL
*
Public
[
IESG
]
[
RFC7517, Section 4.6
]
x5c
X.509 Certificate Chain
*
Public
[
IESG
]
[
RFC7517, Section 4.7
]
x5t
X.509 Certificate SHA-1 Thumbprint
*
Public
[
IESG
]
[
RFC7517, Section 4.8
]
x5t#S256
X.509 Certificate SHA-256 Thumbprint
*
Public
[
IESG
]
[
RFC7517, Section 4.9
]
crv
Curve
EC
Public
[
IESG
]
[
RFC7518, Section 6.2.1.1
]
x
X Coordinate
EC
Public
[
IESG
]
[
RFC7518, Section 6.2.1.2
]
y
Y Coordinate
EC
Public
[
IESG
]
[
RFC7518, Section 6.2.1.3
]
d
ECC Private Key
EC
Private
[
IESG
]
[
RFC7518, Section 6.2.2.1
]
n
Modulus
RSA
Public
[
IESG
]
[
RFC7518, Section 6.3.1.1
]
e
Exponent
RSA
Public
[
IESG
]
[
RFC7518, Section 6.3.1.2
]
d
Private Exponent
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.1
]
p
First Prime Factor
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.2
]
q
Second Prime Factor
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.3
]
dp
First Factor CRT Exponent
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.4
]
dq
Second Factor CRT Exponent
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.5
]
qi
First CRT Coefficient
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.6
]
oth
Other Primes Info
RSA
Private
[
IESG
]
[
RFC7518, Section 6.3.2.7
]
k
Key Value
oct
Private
[
IESG
]
[
RFC7518, Section 6.4.1
]
crv
The subtype of key pair
OKP
Public
[
IESG
]
[
RFC8037, Section 2
]
d
The private key
OKP
Private
[
IESG
]
[
RFC8037, Section 2
]
x
The public key
OKP
Public
[
IESG
]
[
RFC8037, Section 2
]
ext
Extractable
*
Public
[
W3C_Web_Application_Security_WG
]
[
https://www.w3.org/TR/WebCryptoAPI
]
iat
Issued At, as defined in [
RFC7519
]
*
Public
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 8.7.2
]
nbf
Not Before, as defined in [
RFC7519
]
*
Public
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 8.7.2
]
exp
Expiration Time, as defined in [
RFC7519
]
*
Public
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 8.7.2
]
revoked
Revoked Key Properties
*
Public
[
OpenID_Foundation_Artifact_Binding_Working_Group
]
[
OpenID Federation 1.0, Section 8.7.2
]
pub
Public key
AKP
Public
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
priv
Private key
AKP
Private
[
IETF
]
[
RFC-ietf-cose-dilithium-10
]
JSON Web Key Use
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7517
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7517
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Use Member Value
Use Description
Change Controller
Reference
sig
Digital Signature or MAC
[
IESG
]
[
RFC7517, Section 4.2
]
enc
Encryption
[
IESG
]
[
RFC7517, Section 4.2
]
JSON Web Key Operations
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7517
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7517
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Key Operation Value
Key Operation Description
Change Controller
Reference
sign
Compute digital signature or MAC
[
IESG
]
[
RFC7517, Section 4.3
]
verify
Verify digital signature or MAC
[
IESG
]
[
RFC7517, Section 4.3
]
encrypt
Encrypt content
[
IESG
]
[
RFC7517, Section 4.3
]
decrypt
Decrypt content and validate decryption, if applicable
[
IESG
]
[
RFC7517, Section 4.3
]
wrapKey
Encrypt key
[
IESG
]
[
RFC7517, Section 4.3
]
unwrapKey
Decrypt key and validate decryption, if applicable
[
IESG
]
[
RFC7517, Section 4.3
]
deriveKey
Derive key
[
IESG
]
[
RFC7517, Section 4.3
]
deriveBits
Derive bits not to be used as a key
[
IESG
]
[
RFC7517, Section 4.3
]
JSON Web Key Set Parameters
Registration Procedure(s)
Specification Required
Expert(s)
Sean Turner, Mike Jones, Filip Skokan
Reference
[
RFC7517
]
Note
Registration requests should be sent to the mailing list described in 
[
RFC7517
]. If approved, designated experts should notify IANA within 
three weeks. For assistance, please contact iana@iana.org.
Available Formats
CSV
Parameter Name
Parameter Description
Change Controller
Reference
keys
Array of JWK Values
[
IESG
]
[
RFC7517, Section 5.1
]
Contact Information
ID
Name
Contact URI
Last Updated
[IESG]
IESG
mailto:iesg&ietf.org
[IETF]
IETF
mailto:iesg&ietf.org
[IHE_ITI]
IHE ITI
https://www.ihe.net
2025-02-27
[OpenID_Foundation_Artifact_Binding_Working_Group]
OpenID Foundation Artifact Binding Working Group
mailto:openid-specs-ab&lists.openid.net
2024-08-20
[OpenID_Foundation_Digital_Credentials_Protocols_Working_Group]
OpenID Foundation Digital Credentials Protocols Working Group
mailto:openid-specs-digital-credentials-protocols&lists.openid.net
2025-08-13
[W3C_Web_Application_Security_WG]
W3C Web Application Security Working Group
mailto:public-webappsec&w3.org
2024-10-16