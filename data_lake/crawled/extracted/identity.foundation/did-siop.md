---
{
  "title": "Self-Issued OpenID Connect Provider DID Profile v0.1 (DEPRECATED)",
  "url": "https://identity.foundation/did-siop",
  "domain": "identity.foundation",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 26818,
  "crawled_at": "2026-04-23T20:51:58"
}
---

Self-Issued OpenID Connect Provider DID Profile v0.1 (DEPRECATED)
Abstract
This specification defines the "SIOP DID Profile" (
SIOP DID
) that is a
DID AuthN
flavor to use
        OpenID Connect (
OIDC
) together with the strong decentralization, privacy and security
        guarantees of Decentralized Identifiers (
DID
) for everyone who wants to have a generic
        way to integrate
Identity Wallets
into their web applications.
SIOP DID
is an unapproved DIF working group draft specification and now being DEPRECATED within the
Decentralized Identity Foundation
(DIF).
The work on DIF SIOP DID Profile specification has moved to OIDF AB WG to work on a number of new specifications in the course of the DIF/OIDF liaison:
OpenID Connect for Verifiable Presentations
SIOP V2
Terminology
Term
Description
DID
Decentralized Identifier as per [[DID]]
DID Document
DID Document as per [[DID]]
SIOP DID
Self-Issued OpenID Connect Provider DID profile. Refers to a specific flavor of DID AuthN used in the
                OIDC SIOP flow.
JWT
JSON Web Token as per [[RFC7797]]
JWE
JSON Web Encryption as per [[RFC7516]]
JWS
JSON Web Signature as per [[RFC7515]]
JWK
JSON Web Key as per [[RFC7517]]
JWKS
JWK Set as per [[RFC7517]]
OIDC
OpenID Connect as per [[?OIDC.Core]]
OIDC client
Used synonymously with Relying Party (see
RP
)
OP
OpenID Provider as per [[?OIDC.Core]]
SIOP
Self-Issued OpenID Provider as per [[?OIDC.Core]]
RP
Relying Party, as used in [[?OIDC.Core]]
Identity Wallet
An Identity Wallet refers to a application that is under the control and acts on behalf of the
                DID holder. This Also known as an identity agent. The Identity Wallet can have different form factors
                such as a mobile app, browser extension/ plugin etc.
DID AuthN
Refers to a method of proofing control over a DID for the purpose of authentication.
Introduction
An everyday use case that the Decentralized Identity community identified is the sign-up or login with web
        applications. Nowadays, this is often achieved through social login schemes such as Google Sign-In. While
        the Decentralized Identity community has serious concerns about social login, the underlying protocol,
OIDC
, does not have these flaws by design.
SIOP DID
provides
        great potential by leveraging an
Identity Wallet
,
        e.g., as a smartphone app, on the web. This will increase and preserve the user’s privacy by preventing
        third-parties from having the ability to track which web applications a user is interacting with.
While this specification focuses on the integration of
Identity Wallets
in the form of browser extensions/ plugins, or smartphone apps, it does not prevent implementers using
        the proposed flow in different scenarios as well, e.g., between two web services with pre-populated
DIDs
.
Purpose
The main purpose is to sign up with/ login to an
RP
, i.e., web application. It assumes
            the user operates a mobile or desktop browser or a browser-based app that can respond to
SIOP
requests according to this specification.
The
SIOP
flow is conducted peer-to-peer between the
RP
and the
SIOP
. This could be used to authenticate holders based on their
DID
,
            to setup/ bootstrap a DID Comm connection with any
DID
routing that you may need, or to
            provide the
login_hint
to an OpenID Connect service in the
DID Document
supporting the Client-Initiated Backend Channel (CIBA) as per [[?OIDC.CIBA]].
Goals
The main goals of this specification are:
Staying backward compatible with existing
OIDC clients
and
OPs
that implement the
SIOP
specification which is part of the
OIDC
core specification as per [[?OIDC.Core]] to reach a broader community.
Adding validation rules for
OIDC clients
that have
DID AuthN
support to make full use of
DIDs
.
Not relying on any intermediary such as a traditional centralized public or private
OP
while still being
OIDC
-compliant.
Protocol Flow
This specification assumes, the user is operating a mobile or desktop browser to visit a web application or uses
        a browser-based app.
First, the user clicks on the sign up or login UX element. The
RP
will then generate the
        redirect to
openid://<SIOP Request>
which will be handled by the
SIOP
.
On the mobile device, this would open the
Identity Wallet
app, e.g., uport,
        connect.me. On the desktop browser, this would either show a QR code which can be scanned by the
Identity Wallet
app or a redirect to
openid://<SIOP Request>
that for instance could be handled by a browser extension/ plugin implementing the
SIOP
.
The
SIOP
will generate the
<SIOP Response>
based on the specific
DID
method that is supported. The
<SIOP Response>
will be signed and
        optionally encrypted and will be provided according to the requested response mode.
This specification does not explicitly support any intermediate hubs or cloud agents. It is meant to be a
        protocol to exchange the
DID
. You could then interact with a hub/ cloud agent using the
        service endpoint in the
DID Document
.
Unlike the
OIDC
Authorization Code Flow as per [[!OIDC.Core]], the
SIOP
will not return an access token to the
RP
. If this is desired, this could be achieved by
        following the aforementioned CIBA flow as per [[?OIDC.CIBA]] in addition.
SIOP
also
        differs from Authorization Code Flow by not relying on a centralized and known
OP
. The
SIOP
can be unknown to the
RP
until the
        user starts to interact with the
RP
using its
Identity Wallet
.
OIDC
Authorization Code Flow is still a useful approach and should be used whenever the
OP
is known, and
OP
discovery is possible, e.g., exchanged or pre-populated
DID Document
containing an openid element in the service section.
        The
SIOP
flow allows to integrate
Identity Wallets
with
        plain
OIDC clients
if they implemented the
SIOP
specification.
        In contrast, using
DID AuthN
as the authentication means in the
OIDC
Authorization Code Flow would require integration with the
OP
vendor itself.
Example
SIOP
flow with a mobile browser as the User-Agent and an
Identity Wallet
app as the
SIOP
.
Generate SIOP Request
Redirect Request
The request contains
scope
,
response_type
and
client_id
as query
            string parameters for backward compatibility with the OAuth2 specification [[!RFC6749]].
response_type
MUST be
id_token
and
client_id
MUST specify the
            redirect URI of the
RP
(as per [[!OIDC.Core]]). All other
OIDC
request parameters MUST be provided in an Request Object as per [[!OIDC.Core]] which is encoded as a JWT.
            This enables the
RP
to authenticate against the
SIOP
using the
RP's
DID
. The Request Object can be passed by value in the
request
request parameter, or by reference using the
request_uri
parameter.
openid://?response_type=id_token
                &client_id=https%3A%2F%2Frp.example.com%2Fcb
                &scope=openid%20did_authn
                &request=<JWT>
In the example above the
DID AuthN
<SIOP Request>
is initiated
            by the
RP
using Request Object by value.
openid://?response_type=id_token
                &client_id=https%3A%2F%2Frp.example.com%2Fcb
                &scope=openid%20did_authn
                &request_uri=https%3A%2F%2Frp.example.com%2F90ce0b8a-a910-4dd0
In the example above the
DID AuthN
<SIOP Request>
is initiated
            by the
RP
using Request Object by reference.
RP Metadata
In contrast to other
OIDC
flows, e.g., Authorization Code Flow,
RPs
can provide client metadata in the
registration
request parameter. Clients MAY include
            any registration metadata parameters defined in
OpenID Connect Registration 1.0
, and servers MAY use these parameters as they see fit.
In addition to
RS256
, an
SIOP
according to this specification MUST support
EdDSA
and
ES256K
[[!draft-ietf-cose-webauthn-algorithms-03]] for
request_object_signing_alg
and
request_object_signing_alg
can be omitted.
RPs
implementing the
DID AuthN
profile MUST not use
none
for
request_object_signing_alg
.
The Request Object MUST be directly or indirectly verifiable by a verification method in the
RP's
DID Document
and directly by the
RP's
JWKS. The JWKS MUST be provided in the
jwks_uri
or
jwks
entry of the
registration
parameter. The JWKS MUST contain an entry with a
kid
that matches
            the
kid
in the Request Object.
jwks_uri
MUST use the HTTP(S) DID Resolution
            Binding as per [[DID.Resolution]] for backward compatibility reasons with plain
SIOP
OPs
. The
jwks
request parameter SHOULD be used only if the public key cannot
            be directly obtained from the
DID Document
.
RPs
can decide to receive the
SIOP Response
encrypted. To enable encryption,
            the registration parameter MUST use
id_token_encrypted_response_alg
and
id_token_encrypted_response_enc
according to
OIDC
Client Metadata
            [[!OIDC.Registration]]. This specification RECOMMENDS the use of `ECDH-ES` with the `X25519` curve for JWE
            as explained in section
Encryption
and described in
            [[!draft-amringer-jose-chacha-00]].
Request Object
The Request Object follows the
OIDC
specification, e.g., adding
nonce
,
state
,
response_type
, and
client_id
parameters.
The request contains
scope
,
response_type
and
client_id
as query
            string parameters for backward compatibility with the OAuth2 specification [[!RFC6749]].
response_type
MUST be
id_token
and
client_id
MUST specify the
            redirect URI of the
RP
(as per [[!OIDC.Core]]). All other
OIDC
request parameters MUST be provided in an Request Object as per [[!OIDC.Core]] which is encoded as a JWT.
            This enables the
RP
to authenticate against the
SIOP
using the
RP's
DID
. The Request Object can be passed by value in the
request
request parameter, or by reference using the
request_uri
parameter.
The Request Object follows the
OIDC
specification, e.g., adding
nonce
,
state
,
response_type
, and
client_id
parameters.
This specification introduces additional rules for request parameters and claims in the Request Object:
REQUIRED.
iss
MUST contain the
DID
of the
RP
that can
                be resolved to a
DID Document
. The
DID Document
MUST contain a verification method in the authentication section, e.g., public key, that allows the
SIOP
to verify the Request Object.
By default, the
iss
claim refers to the
client_id
but
SIOP
assumes that
client_id
is the redirect URI of the
RP
. That is the reason
                why the
DID
is not encoded in the
client_id
. It is compliant with the
OIDC
specification to use different values for
iss
and
client_id
.
REQUIRED.
kid
MUST be a DID URL referring to a verification method in the authentication
                section in the
RP's
DID Document
, e.g.,
did:example:0xab#key1
. The
SIOP
MUST be able to use that verification
                method to verify the Request Object directly or indirectly. Additionally, the referred JWKS in the
registration
parameter MUST contain an entry with the same
kid
.
REQUIRED.
scope
MUST include
did_authn
to indicate the
SIOP DID
profile is used.
REQUIRED.
registration
MUST be included in the Request Object
REQUIRED.
client_id
MUST be repeated in the Request Object
OPTIONAL.
response_mode
specifies how the response is returned to the redirect URI by the
SIOP
.
SIOP
implementing this specification MAY set the
response_mode
to
form_post
.
fragment
is the default
                Response Mode.
RPs
MUST take into consideration the platform of the
                User-Agent when specifying this request parameter.
See OAuth 2.0 Form Post Response Mode [[?OAuth2.FormPost]] and OAuth 2.0 Multiple Response Type Encoding
                Practices [[?OAuth2.ResponseTypes]] for more information about
response_mode
.
OPTIONAL.
response_context
specifies whether the response should be returned to the
                redirect URI in the context of an existing system browser session, or whether the response can be
                returned in a new/empty context (requested with a
response_context
of
wallet
).
                The default
response_context
is
rp
, indicating that the response should be submitted
                in the conext of the RP's existing system browser session.
A
response_context
of
wallet
indicates to the SIOP that the user flow should end in the SIOP,
                without any in-band redirection back to the RP. This behavior is useful in cross-device workflows where
                it's appropriate for the mobile portion of the flow to terminate in the wallet.
OPTIONAL.
claims
follows the
OIDC Core schema
,
                adding a top-level
vc
property as a sibling to (and following the schema of)
id_token
and
userinfo
. Requesting claims within the
vc
set indicates that the requesting party
                would like to receive (if
essential
is
false
), or requires (if
true
)
                a specific set of verifiable credential types within the
.vp.verifiableCredential
array of the
                SIOP Response. Specific [VC types](https://www.w3.org/TR/vc-data-model/#types) are identified using the VC type's full URI.
When providing claims in this manner, the SIOP Response acts as a W3C Verifiable Presentation; requested claims
                are provided in the Response by populating the array of Verifiable Credentials within the Presentation.
The following is a non-normative example of the JWT header of a Request Object:
{
                "alg": "ES256K",
                "typ": "JWT",
                "kid": "did:example:0xab#veri-key1"
            }
The following is a non-normative example of the JWT payload of a Request Object without requesting
<SIOP DID Response>
encryption:
{
                "iss": "did:example:0xab",
                "response_type": "id_token",
                "client_id": "https://my.rp.com/cb",
                "scope": "openid did_authn",
                "state": "af0ifjsldkj",
                "nonce": "n-0S6_WzA2Mj",
                "response_mode" : "form_post",
                "registration" : {
                    "jwks_uri" : "https://uniresolver.io/1.0/identifiers/did:example:0xab;transform-keys=jwks",
                    "id_token_signed_response_alg" : "ES256K"
                }
            }
The following is a non-normative example HTTP 302 redirect response by the
RP
, which
            triggers the User-Agent to make an
SIOP DID
Authentication Request using Request
            Object by value to the
SIOP
(with line wraps within values for display purposes
            only):
HTTP/1.1 302 Found
            Location: openid://?
                &client_id=https%3A%2F%2Frp.example.com%2Fcb
                &scope=openid%20did_authn
                &request=<JWT>
The following is a non-normative example HTTP 302 redirect response by the
RP
, which
            triggers the User-Agent to make an
SIOP DID
Authentication Request using Request
            Object by reference to the
SIOP
(with line wraps within values for display purposes
            only):
HTTP/1.1 302 Found
            Location: openid://?
                response_type=id_token
                &client_id=https%3A%2F%2Frp.example.com%2Fcb
                &scope=openid%20did_authn
                &request_uri=https%3A%2F%2Frp.example.com%2F90ce0b8a-a910-4dd0
Encryption
JWE encryption SHOULD use Diffie-Hellman key agreement, i.e., algorithm `ECDH-ES` using the `X25519` curve
            which uses direct key agreement with an ephemeral key. This means that a symmetric key is derived using
            Diffie-Hellman from the
RP's
public key and a randomly generated ephemeral private key.
            The corresponding ephemeral public key is included in the header of the JWE in the `epk` and the derived
            symmetric key is used to directly encrypt the JWT content. For symmetrically encrypting the content
            `XChaCha20Poly1305` is used which has algorithm code `XC20P`.
The following is an example of the protected header of the resulting JWE:
{
                "alg": "ECDH-ES",
                "epk":
                {
                    "kty": "OKP",
                    "crv":"X25519",
                    "x":"hSDwCYkwp1R0i33ctD73Wg2_Og0mOBr066SpjqqbTmo"
                }
                "enc": "XC20P",
                "kid": "did:example:0xab#key-1"
            }
Note that the `kid` above denotes the DID and key of the
RP
, i.e., this public key is the
            key used by the sender together with the ephemeral private key in order to derive the shared secret. For the
            encryption the 24 bytes nonce field in the `XChaCha20` algorithm is used as the initialization vector. The
            authentication tag is the MAC computed by the `Poly1305` function. It is 16 bytes long.
The message to be encrypted is the JWT of the `id_token`, including header and signature. The JWT is encoded
            via base64url before encryption.
For the final encoding of the JWE the JWE Compact Serialization outlined in
            [[!RFC7516]] is used. The structure of the message is as follows:
BASE64URL(JWE Protected Header) || '.' || '.' ||
            BASE64URL(JWE Initialization Vector) || '.' ||
            BASE64URL(JWE Ciphertext) || '.' ||
            BASE64URL(JWE Authentication Tag)
Note the two '.' characters above which indicates that the encrypted key is empty since we are
            using direct key agreement.
SIOP Request Validation
The
SIOP
MUST validate the
<SIOP Request>
by following the
            Self-Issued ID Token Validation rules as per [[!OIDC.Core]].
The step described above ensures that the Request Object is verified according to the
OIDC
specification. This includes basic JWS verification.
If scope contains the
did_authn
scope, the receiving
SIOP
MUST further validate the
<SIOP Request>
as follows in no particular order:
Resolve the
DID Document
from the
RP's
DID
specified in the
iss
request parameter.
If
jwks_uri
is present, ensure that the
DID
in the
jwks_uri
matches the
DID
in the
iss
claim.
Determine the verification method from the
RP's
DID Document
that matches the
kid
of the
SIOP Request
.
Verify the
SIOP Request
according to the verification method above. This step depends on
                the verification method in the authentication section in the
DID Document
and is out-of-scope of this specification.
If the key pair that signed the
SIOP Request
refers to the same key as indicated by the
            verification method, then no additional verification has to be done as the
SIOP
validation will verify the signature of the JWS.
Generate SIOP Response
The
SIOP
MUST generate and send the
<SIOP Response>
to the
RP
as described in the Self-Issued OpenID Provider Response section in [[!OIDC.Core]].
            The
id_token
represents the <SIOP Response> encoded as a JWS, or nested JWS/JWE.
This specification introduces additional rules for claims in the
id_token
:
REQUIRED.
sub_jwk
MUST contain a
kid
that is a DID URL referring to the
                verification method in the
SIOP's
DID Document
that can
                be used to verify the JWS of the
id_token
directly or indirectly.
REQUIRED.
did
MUST be the
SIOP's
DID
.
The
sub_jwk
claim has to be provided for backward compatibility reasons. The verification
            method in the
DID Document
can be different from a public key and can use a
publicKey
property value other than
publicKeyJwk
.
The following is a non-normative example of the JWT header of an
id_token
using no encryption:
{
                "alg": "ES256K",
                "typ": "JWT",
                "kid": "did:example:0xab#key-1"
            }
The following is a non-normative example of the unencrypted JWT payload of an
id_token
:
{
                "iss": "https://self-issued.me",
                "nonce": "n-0S6_WzA2Mj",
                "exp": 1311281970,
                "iat": 1311280970,
                "sub_jwk" : {
                    "crv":"secp256k1",
                    "kid":"did:example:0xcd#verikey-1",
                    "kty":"EC",
                    "x":"7KEKZa5xJPh7WVqHJyUpb2MgEe3nA8Rk7eUlXsmBl-M",
                    "y":"3zIgl_ml4RhapyEm5J7lvU-4f5jiBvZr4KgxUjEhl9o"
                },
                "sub": "9-aYUQ7mgL2SWQ_LNTeVN2rtw7xFP-3Y2EO9WV22cF0",
                "did": "did:example:0xcd"
            }
SIOP Response Validation
The
RP
MUST validate the
<SIOP Response>
as described in the
            Self-Issued ID Token Validation section in [[!OIDC.Core]]. This includes:
Optionally decrypting the JWE to obtain the JWS which contains the
id_token
.
Verifying that the
id_token
was signed by the key specified in the
sub_jwk
claim.
Additionally, the
RP
MUST validate the
id_token
against the
SIOP's
DID Document
as follows:
Resolve the
DID Document
from the
SIOP's
DID
specified in the
did
claim.
Determine the verification method from the
SIOP's
DID
                Document
that matches the
kid
of the
sub_jwk
claim in the
id_token
.
Verify the
id_token
according to the verification method above. This step depends on the
                verification method in the authentication section in the
DID Document
and
                is out-of-scope of this specification.
If the key pair that signed the
id_token
refers to the same key as indicated by the
            verification method, then no additional verification has to be done as the
SIOP
validation will verify the signature of the JWS.
SIOP Discovery
The
SIOP
specification assumes the following OP discovery metadata:
"id_token_signing_alg_values_supported": ["RS256"],
            "request_object_signing_alg_values_supported": ["none", "RS256"]
The
DID AuthN
profile assumes the following OP discovery metadata:
"id_token_signing_alg_values_supported": ["RS256", "ES256K", "EdDSA"],
            "request_object_signing_alg_values_supported":
                ["none", "RS256", "ES256K", "EdDSA"]
This change will allow
DID AuthN
enabled
RPs
to use additional
            signature algorithms commonly used amongst members of the SSI community.
"Self-Issued OpenID Provider Discovery" IS NOT normative and does not contain any MUST, SHOULD, or MAY
            statements. Therefore, using a different signing algorithmn than
RS256
shouldn't break the
SIOP
specification. A
DID AuthN
enabled
RP
would provide
id_token_signed_response_alg
to indicate its preferred signature algorithm
            among the three
id_token_signing_alg_values_supported
options listed above.
UX Considerations
SIOP
uses the custom URL scheme
openid://
. Mobile browsers would open the app
        that registered that scheme. Desktop browser extensions/ plugins have support for similar functionality. It is
        out of the scope of the spec under which circumstances a QR code will be rendered. One option will be to provide
        the QR code if the user is using the desktop browser, and no browser extension/ plugin is available.
On Android, the user can choose which app should open if multiple apps registered the same custom URL scheme. On
        iOS, the behavior is undefined. One approach would be to check if the user is on an iOS device and then, won't
        render the button if this is a concern. A fallback on iOS could be the use of custom mime types, but unusual UX
        has to be considered. Note, this issue is not specific to
SIOP
only but affects all apps
        using custom URL schemes. In case a QR Code is used where the user has to open the app first and has to scan the
        QR Code, this issue is mitigated.
Security Considerations
Threat: Interception of the Redirect URI
If an attacker can cause the
<SIOP Response>
to be sent a URI under his control, he will
        directly get access to the fragment carrying the
id_token
.
This attack can be mitigated by hardening the
RP
, e.g., no support for the open redirector
        pattern.
Threat: Identity Token Leak in Browser History
An attacker could obtain the
<SIOP Response>
from the browser's history.
This attack cannot be fully mitigated. It is RECOMMENDED to use short expiration times for
id_token
, and indicating that browsers should not cache the response.
Threat: Identity Token Leak to Third Party Scripts
It is relatively common to use third-party scripts on
RP
pages, such as analytics tools, crash
        reporting. The author of the application may not be able to be fully aware of the entirety of the code running
        in the application. When a
<SIOP Response>
is returned in the fragment, it is visible to any
        third-party scripts on the page.
This attack could be mitigated by using trusted/ audited third party scripts on the
RP's
page,
        or browser-based app.
Countermeasures
Use
response_mode=form_post
whenever possible to mitigate the risks described above. Under some
        circumstances, e.g., this will not be possible as such in the case of purely decentralized apps (dApp).
Threat: Session Fixation in Cross-Device Flow
When the protocol begins on one device and ends on another, there is a risk that the cross-device transfer can
        be hijacked. For example, consider a flow that begins with the display of a QR code by the
RP
transfers to a mobile wallet when the user scans the QR code. In this scenario, an attacker can trick the user
        into scanning a QR code associated with a legitimate RP's sign-in request, thereby causing the user to
        authenticate within the context of the attacker's session.
Countermeasures
Validate that the browser session in which the DID SIOP Response is submitted belongs to the same user as the
        browser session in which the DID SIOP Request was displayed. Even if these sessions are on different devices,
        the RP can take steps to ensure these belong to the same user (e.g., by checking whether an existing session
        exists or by asking the user to sign in through a non-SIOP means).
Additional Security Considerations
The OWASP Foundation maintains a set of security recommendations and best practices for web applications, and it
        is RECOMMENDED to follow these best practices when creating an
SIOP
or
RP
based on this specification.
IANA Considerations
This specification registers the
did
claim in the IANA JSON Web Token
        Claims registry defined in JWT.
OIDC Considerations
This specification aims to be backward compatible with existing
OIDC clients
and
OPs
that implement the
SIOP
specification. Although the
SIOP
specification is part of the OIDC core specification, it is not widely adopted yet.
        One of the reasons was that not many apps existed that provided functionality we can find in
Identity Wallets
. Nevertheless,
SIOP
uses the same or similar
        request and response messages and should be easy to allow
OIDC
vendors to upgrade existing
OIDC
clients to support
SIOP
.