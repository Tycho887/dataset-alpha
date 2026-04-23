---
{
  "title": "\n    \n    \n    \n        JOSE + JWT library for Java\n    \n",
  "url": "https://connect2id.com/products/nimbus-jose-jwt",
  "domain": "connect2id.com",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 9874,
  "crawled_at": "2026-04-23T21:01:03"
}
---

Nimbus JOSE + JWT
The most popular and robust Java and Android library for JSON Web Tokens (JWT)
Covers all standard signature (JWS) and encryption (JWE) algorithms,
including recent
secp256k1
,
ECDH-1PU
and
XC20P
additions
Open source
Apache 2.0 license
Secure tokens and APIs
This library implements the Javascript Object Signing and Encryption (JOSE) and
JSON Web Token (JWT)
standards
, with a comprehensive yet easy to use
API for:
Signing and encrypting tokens, such as self-contained
OAuth
2.0
access tokens and
OpenID Connect
identity tokens
Self-contained API keys, with optional revocation
Stateless sessions
Security event tokens
Applying signatures or authenticated encryption to content and messages
Authenticating clients and web API requests
Hello, world!
// Create an HMAC-protected JWS object with a string payload
JWSObject jwsObject = new JWSObject(new JWSHeader(JWSAlgorithm.HS256),
                                    new Payload("Hello, world!"));

// We need a 256-bit key for HS256 which must be pre-shared
byte[] sharedKey = new byte[32];
new SecureRandom().nextBytes(sharedKey);

// Apply the HMAC to the JWS object
jwsObject.sign(new MACSigner(sharedKey));

// Output in URL-safe format
System.out.println(jwsObject.serialize());
Looking for
more examples
?
Maven
Check out the
latest release
:
<dependency>
    <groupId>com.nimbusds</groupId>
    <artifactId>nimbus-jose-jwt</artifactId>
    <version>10.x</version>
</dependency>
Go to the
downloads
page for more
instructions.
Full compact JOSE and JWT support
Create, serialise and process:
JSON Web Signature (JWS) secured objects
JSON Web Encryption (JWE) secured objects
Signed and / or encrypted JSON Web Tokens (JWTs)
Unsecured (
alg=none
) objects and JWTs are also supported.
Supported JOSE serialisations:
Compact – the most commonly used (by JWTs)
JSON:
General syntax – supports multiple JWS signatures or JWE recipients
Flattened syntax – optimised JSON syntax
All standard JWS and JWE algorithms are covered
Check out our
algorithm selection
guide
if you’re unsure
which JWS or JWE might be appropriate for your application.
JWS
MAC / signature
JWS alg identifiers
HMAC integrity
HS256, HS384 and HS512
RSASSA-PKCS1-V1_5 signatures
RS256, RS384 and RS512
RSASSA-PSS signatures
PS256, PS384 and PS512
EC signatures
ES256, ES256K
✝
, ES384 and ES512
EdDSA signatures
EdDSA, Ed25519
✝
Based on the
secp256k1
curve.
JWE
Key management
JWE alg identifiers
RSAES-PKCS1-V1_5 encryption
RSA1_5
RSAES OAEP encryption
RSA-OAEP, RSA-OAEP-256, RSA-OAEP-384, RSA-OAEP-512
AES key wrap encryption
A128KW, A192KW and A256KW
Direct shared symmetric key encryption
dir
Elliptic Curve Diffie-Hellman key agreement
ECDH-ES, ECDH-ES+A128KW, ECDH-ES+A192KW and ECDH-ES+A256KW
Elliptic Curve Diffie-Hellman public key authenticated encryption
ECDH-1PU, ECDH-1PU+A128KW, ECDH-1PU+A128KW and ECDH-1PU+A256KW
AES GCM key wrap encryption
A128GCMKW, A192GCMKW and A256GCMKW
PBES2 key encryption
PBES2-HS256+A128KW, PBES2-HS384+A192KW and PBES2-HS512+A256KW
Encryption methods
JWE enc identifiers
AES/CBC/HMAC/SHA authenticated encryption
A128CBC-HS256, A192CBC-HS384, A256CBC-HS512, A128CBC+HS256 (deprecated) and A256CBC+HS512 (deprecated)
AES in Galois/Counter Mode (GCM)
A128GCM, A192GCM and A256GCM
Extended nonce ChaCha20-Poly1305
XC20P
Compression
JWE zip identifier
RFC 1951
DEFLATE
JWK
Key type
JWK kty identifier
RSA (RFC 3447)
RSA
Elliptic Curve (DSS)
EC
Octet sequence (symmetric key)
oct
Octet key pair (RFC 8037)
OKP
Neat decoupling between the JOSE / JWT layer and the underlying cryptography implementations
The JOSE / JWT layer and the underlying cryptography implementations are neatly
decoupled by means of stable public interfaces. This enables application
developers to easily switch algorithm implementations and plug JCA providers,
including hardware-based (PKCS#11 smart cards and
HSM
s). Cloud-based providers, such as Google
Cloud’s
KMS
, are also
supported.
JSON entity mapping
JSON and Java entities are naturally mapped. Check the usage
examples
.
JSON
Java
string
java.lang.String
number
java.lang.Number
true / false
java.lang.Boolean
JSON array
java.util.List<Object>
JSON object
java.util.Map<String, Object>
null
null
JavaDocs
The comprehensive
JavaDocs
can serve as
API reference and to discover the library’s many features and capabilities. You
can browse the JavaDocs
online
or
download them from
Maven Central
.
Implemented specifications
From the
JOSE
,
OAuth
,
COSE
working groups and other sources:
JWS
(
RFC 7515
)
JWE
(
RFC 7516
)
JWK
(
RFC 7517
)
JWA
(
RFC 7518
)
JWK Thumbprint
(
RFC 7638
)
JWK Thumbprint URI
(
RFC 9278
)
JWS Unencoded Payload Option
(
RFC 7797
)
JWT
(
RFC 7519
)
COSE and JOSE Registrations for WebAuthn Algorithms
(
draft-ietf-cose-webauthn-algorithms-03
)
EdDSA and ECDH with X25519
(
RFC 8037
)
Public key authenticated encryption with ECDH-1PU
(
draft-madden-jose-ecdh-1pu-04
)
Chacha derived AEAD algorithms in JOSE
(
draft-amringer-jose-chacha-02
)
OpenID Federation 1.0
for JWK
exp
,
nbf
,
iat
and
revoked
(
openid-federation-1_0
)
Fully-Specified Algorithms for JOSE and COSE
(
draft-ietf-jose-fully-specified-algorithms-02
)
JSON Web Token Best Current Practices
(
RFC 8725
)
Related specifications
Web Cryptography API
– W3C effort to
specify a standard JavaScript API for performing cryptographic operations in
the browser.
System requirements and dependencies
The Nimbus JOSE + JWT library works with Java 7+ and has minimal dependencies.
(shaded)
Gson
for efficient JSON parsing
and serialisation.
(shaded)
JCIP
for concurrency
annotations.
(optional)
BouncyCastle
can be used as an alternative cryptographic backend via the standard Java
Cryptography Architecture (JCA) interface. Developers typically resort to
BouncyCastle if their application requires a cryptographic algorithm that
isn’t supported by their Java or Android runtime. Check the
JCA algorithm
support
.
(optional)
BouncyCastle
FIPS
as a
FIPS 140-2, Level 1 compliant JCA provider. Must not be imported as
dependency together with the plain BouncyCastle provider!
(optional)
Tink
for handling
Ed25519 signatures (RFC 8037), ECDH with X25519 (RFC 8037) and content
encryption with Extended nonce ChaCha20-Poly1305
(XC20P, draft-amringer-jose-chacha-02).
JWK generator
A tool for generating RSA, EC and symmetric JSON Web Keys (JWKs) is also
available
, thanks to Justin Richer. He
also hosts an
online version
.
License
The library source code is made available under the
Apache 2.0
license
.
To post bug reports and suggestions
Your feedback is important. Read how to
submit bug reports and
suggestions
. Here is a
list of new
features and algorithms
that the we would
like to see implemented and supported by the library.
History
Development of this library was started by
Connect2id
in January 2012. The initial code was based on JWS/JWE/JWT crypto classes
factored out of the OpenInfoCard project. A rewrite to fully decouple the
JOSE + JWT object representation from the crypto implementation led to the next
major 2.0 release in October 2012. Today the library is used by our
OpenID Connect server
and numerous other products and
services in identity, messaging, mobile and finance.
Acknowledgements
Axel Nennker
from Deutsche
Telekom and the developers behind OpenInfoCard for providing much of the
initial code.
Stepan Yakimovich at
MONET+
for contributing a
draft-ietf-jose-pqc-kem
implementation for post-quantum cryptography support.
Thomas Rørvik Skjølberg at
Entur
for contributing
a powerful mini framework for retrieving JWK sets with caching, outage,
retrial and fail-over capabilities.
Egor Puzanov for contributing the JSON Web Encryption (JWE) to multiple
recipients and reworking the JWE JSON class.
Stian Valentin Svedenborg for adding ESxxx support to the existing JWS
creation on Android and other devices with biometric prompt.
SICPA and DSR Corporation,
Alexander Martynov
,
Alexander Sherbakov, Yolan Romailler and Patrick McClurg for contributing
EDCH-1PU and XC20P support.
Justin Richer
for handling initial
releases to Maven Central, JPSK support, numerous improvements, fixes and
suggestions.
Melisa Halsband from CertiVox for implementing AES key wrap and AES GCM key
wrap encryption.
Tim McLean
for implementing RFC 8037.
Josh Cummings from the Spring Security team for contributing the JWS minter
framework and many other patches.
Cedric Staub for adding explicit JCA provider interfaces.
Toma Velev
for implementing the JSON Smart
shading in v9.0.
Ville Kurkinen for adding initial Maven support.
David Ortiz for initiating RSA encryption development.
Quan Nguyen
, Google
Information Security Engineer,
Project
Wycheproof
, for reporting
Padding Oracle and integer overflow vulnerabilities in AES/CBC/HMAC
decryption.
Devin Cook of
Oracle Cloud Infrastructure
(OCI) - Security Research Team.
Juraj Somorovsky for security related reviews, improvements and suggestions.
Antonio Sanso
for his work in investigating
invalid curve vulnerabilities in JOSE implementations.
Jürg Wullschleger and Markus Löwe for discovering StackOverflowError issues
when parsing specially crafted JSON input and proposing suitable mitigations.
Jingcheng Yang and Jianjun Chen from Sichuan University and Zhongguancun Lab,
for reporting a DoS vulnerability in the PBKDF2 decrypter.
Lai Xin Chu for initial work on JWE.
Wisgary Torres from the Microsoft Xbox team for important feedback and bug
reports.
Brian Campbell for JWT thumbprint debugging.
CertiVox UK for supporting the library development.
Casey Lee for adding a Java 6 build profile.
Dimitar A. Stoikov on adding support for AES ciphers with internally
generated IV.
Aleksei Doroganov for adding ES256P support based on secp256k1 ECDSA.
Peter Laurina for contributing RSA-OAEP-512 support.
Everyone on the
JOSE WG
at the IETF.
Numerous other contributors of bug reports, fixes and suggestions.