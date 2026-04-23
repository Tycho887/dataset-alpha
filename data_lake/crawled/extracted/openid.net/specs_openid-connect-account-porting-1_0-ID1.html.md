---
{
  "title": "OpenID Connect Account Porting",
  "url": "https://openid.net/specs/openid-connect-account-porting-1_0-ID1.html",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 36530,
  "crawled_at": "2026-04-23T20:52:40"
}
---

OpenID Connect Account Porting
J. Manger
Telstra
T. Lodderstedt
YES Europe AG
A. Gleditsch
Telenor
March 6, 2017
OpenID Connect Account Porting
openid-connect-account-porting-1_0
Abstract
This specification defines mechanisms to support a user porting from one OpenID Connect Provider to another, such that relying parties can automatically recognize and verify the change.
Note
Discussions on this draft occur in the
OpenID Foundation MODRNA working group
.
Table of Contents
1.
Introduction
1.1.
Requirements Notation, Conventions, and Terminology
1.2.
Porting flow
2.
Discovery
3.
Porting data API
4.
Encrypting "port_token"
5.
Indicating a previous identity: "aka" member
6.
Porting check API
7.
"user_ported" error code
8.
Security Considerations
8.1.
Impersonation of legitimate user's old OP account
8.2.
Trick user into login with attacker's account
8.3.
Impersonate old OP/replay migration data
8.4.
Bad OP
8.5.
Inject migration data during RP account migration
8.6.
Further Considerations
9.
Privacy Considerations
10.
IANA Considerations
11.
References
11.1.
Normative References
11.2.
Informative References
Appendix A.
Example flow
Appendix B.
Acknowledgements
Appendix C.
Notices
Appendix D.
Document history
Authors' Addresses
1.
Introduction
OpenID Connect is a federated identity protocol that allows a user to leverage his or her authentication to an OpenID Connect Provider (OP) to login to Relying Parties (RPs). An RP can (and often will) accept logins via many OPs. The primary identifier for a user at an RP is the combination of a Subject Id ("sub" value) and OP identifier ("iss" value). The "sub" value is only defined to be unambiguous within the context of an "iss" value
[OpenID.Core]
§5.7. "Claim Stability and Uniqueness".  This design deliberately isolates each OP's user population so one OP cannot adversely affect the security of another OP. One consequence, however, is that a user porting from one OP to another appears to an RP as two unrelated users.
This specification extends OpenID Connect to enable an RP to recognize when a user logging in via a New OP is the same user who has previously logged in via an Old OP. That is, it enables porting between OPs to be handled automatically by RPs. The central idea is that the user logs into both Old and New OPs in a single session to establish the link between the user's accounts at each. Subsequently, RPs can interact with both OPs to confirm that link, without needing the user to repeat the dual logins.
OpenID Connect account porting is motivated by (but not limited to) the GSMA Mobile Connect scheme, in which mobile network operators collectively offer federated identity services
[MobileConnect]
. Most jurisdictions allow users to port their mobile phone number between network operators, and a reasonable expectation of those users will be that their Mobile Connect account (provided by those same operators) can also be ported at the same time. There is a significant difference between phone number and account porting, however. Other parties are generally unaware when number porting occurs; they simply keep using the same phone number to communicate with the user. In contrast, RPs are aware when an OpenID Connect account is ported as they interact with a New OP.
Section 1.2
gives an overview of the message flows during porting.
Section 2
defines metadata that indicates an OP supports porting, which can be obtained via
[OpenID.Discovery]
.
Section 3
specifies an API offered by an Old OP that a New OP calls when a user ports to collect a token representing the port.  This API is protected by an OAuth 2.0 exchange to ensure the user consents to the porting process.
Section 5
specifies how a New OP can identify the Old OP in an id_token presented to an RP.
Section 6
describes how an RP can confirm the porting information with the Old OP.
Appendix A
provides a example of a complete porting flow.
1.1.
Requirements Notation, Conventions, and Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in
[RFC2119]
.
Throughout this document, values are quoted to indicate that they are to be taken literally in protocol messages.
Terms such as "OpenID Provider" (OP), "Relying Party" (RP), "Subject Id" (sub), and "Sector Id" are defined in
[OpenID.Core]
. This document uses the terms "Old OP" and "New OP" to indicate OpenID Providers that support users porting out and porting in respectively. An OP can support both roles (and hopefully most will).
1.2.
Porting flow
Porting involves a user, their Old OP and New OP, plus any number of RPs.  A sample porting flow is described below.
The first stage for a specific porting event is for the New OP to get confirmation from the Old OP that the user wants to port.  The New OP does so by calling the Old OP's Porting data API on the user's behalf, which first requires orchestrating an approval interaction between the user and the Old OP using OAuth 2.0
[RFC6749]
.
The user browses to the New OP, logs in, and indicates that they want to port from a particular Old OP.
New OP initiates an OAuth 2.0 flow by redirecting the user's browser to the Old OP's authorization endpoint.
The user authenticates to the Old OP, and confirms they want to port to the New OP.
Old OP redirects the user's browser back to the New OP.
New OP completes the OAuth 2.0 flow by getting an access token from the Old OP's token endpoint.
New OP calls the Old OP's Porting data API with the access token; receiving a "port_token".
The second stage of the porting process occurs multiple times: once for each RP. It occurs the first time the user visits a given RP after porting.  That is, the first time the user logs in to a given RP via the New OP.  A normal OpenID Connect flow occurs, but the New OP includes extra details in the resulting "id_token" to indicate that the user previously used a particular Old OP.
When an RP does not recognize the New OP's Subject Id for the user, the RP can see whether it knows this user under an id from a previous OP.  The RP does not blindly trust the New OP to identify the account that was ported. Instead, the RP gets confirmation from the Old OP that the user really did port to the New OP. It is only in that confirmation that the Old OP identifies the ported account, enabling the RP to link the user's ids from both OPs.
The user browses to the RP, and choses to login via the New OP.
RP initiates an OpenID Connect login by redirecting the user's browser to the New OP's authorization endpoint.
The user authenticates to the New OP, and consents to being identified to the RP.
New OP redirects the user's browser back to the RP.
RP completes the OpenID Connect flow by getting an id_token from the New OP's token endpoint.
New OP included an "aka" member in the id_token listing the user's Old OP, along with an encrypted version of the user's "port_token" obtained in the first stage. Note: the audience for the encryption applied to the "port_token" is the Old OP, not the RP.
RP prepares to make API calls to the Old OP, by calling the Old OP's token endpoint (with an OAuth 2.0 client credential grant) to get an access token.
RP calls the Old OP's Porting check API with the access token, passing along the encrypted "port_token"; receiving the Old OP's Subject Id for the user in response.
RP automatically accepts the two Subject Ids from Old and New OPs as identifiers for the same account at the RP.
A user could have ported to the Old OP from an even Older OP.  That can be indicated by the Old OP including an "aka" member in it's Porting check API response (step 5 above). An RP can automatically process that port in the same way that an "aka" value from the New OP is handled.
The porting flow maintains the privacy benefit offered by the use of pairwise Subject Ids, but still works if an OP uses public Subject Ids.
It is possible for an OP to implement the porting flow without maintaining details of the RPs each user has visited.
2.
Discovery
OpenID Discovery offers details about the features supported by an OP
[OpenID.Discovery]
. The following members MUST be included in the metadata for an Old OP that supports users porting out:
"port_data_endpoint"
Base URL for the Porting data API described in
Section 3
that a New OP can use to obtain details about an account that is being ported.  The URL MUST use the "https" scheme.
"port_check_endpoint"
Base URL for the Porting check API described in
Section 6
that an RP can use to confirm that an account has been ported to a specific New OP. The URL MUST use the "https" scheme.
"port_enc_values_supported"
Array of string algorithm names
[IANA.JOSE]
identifying content encryption algorithms supported by the OP that can be used by a New OP to encrypt a "port_token".
The metadata MUST also include a "jwks_uri" member pointing to the OP's JSON Web Key Set. And that set MUST include at least one encryption public key, indicated with a "use":"enc" member
[RFC7517]
, that can be used to encrypt a port_token.
Below are sample metadata requests and responses.
GET /.well-known/openid-configuration HTTP/1.1
Host: oldop.example.net
HTTP/1.1 200 OK
Content-Type: application/json

{
                     "issuer": "https://oldop.example.net/",
     "authorization_endpoint": "https://oldop.example.net/connect/authorize",
             "token_endpoint": "https://oldop.example.net/connect/token",
         "port_data_endpoint": "https://oldop.example.net/connect/port_data",
        "port_check_endpoint": "https://oldop.example.net/connect/port_check",
                   "jwks_uri": "https://oldop.example.net/keys.jwks",
  "port_enc_values_supported": [ "A256GCM", "A256CBC-HS512" ],
  …
}
GET /keys.jwks HTTP/1.1
Host: oldop.example.net
HTTP/1.1 200 OK
Content-Type: application/jwk-set+json

{"keys":
  [
    {"kty":"RSA",
       "n": "0vx7agoebGcQSuuPiLJXZptN9nndrQmbXEps2a … DKgw",
       "e":"AQAB",
     "use":"enc",
     "alg":"RSA-OAEP-256",
     "kid":"2011-04-29"},
    …
  ]
}
3.
Porting data API
The Porting data API (offered by an Old OP and consumed by a New OP) provides a token to represent a porting event. The New OP passes the token (after encrypting it [
Section 4
]) to each RP when the user subsequently logs into that RP [
Section 5
]. The RP, in turn, passes the token to the Porting check API [
Section 6
] to confirm the port with the Old OP.
Access to porting data requires the consent of the user to whom it relates.  The Old OP MUST support the OAuth 2.0 authorization code flow for accessing the API
[RFC6749]
. The Old OP MUST support Bearer access tokens
[RFC6750]
. The New OP MUST include the scope "port_data" when requesting access.
The API provides a single read-only resource per user. It can be read with a "GET" request. The path "/me" appended to the base URL (from the "port_data_endpoint" member in the Old OP discovery metadata) indicates the resource for the user associated with the access token used to make the request.
The response is a JSON object with a "port_token" member that has a string value. The Old OP needs to be able to identify the user and New OP involved in the porting from the port token. The Old OP MUST choose port token values to have sufficient entropy that they cannot be guessed by other parties, including by New OPs and RPs that have seen other port tokens. All "port_token" values from the Old OP for a given New OP MUST be the same length so the length itself (which is typically preserved by encryption) does not allow correlation across RPs. Consequently, a port token cannot simply be the concatenation of ids for the user and New OP. It could be a combination of the user and New OP ids signed by the Old OP. It could also be a random number used as a reference to porting details recorded by the Old OP.
Any unrecognized members in the response MUST be ignored (such as "extra_stuff" in the example below).
Below is a sample porting data request and response:
GET /connect/port_data/me HTTP/1.1
Host: oldop.example.net
Authorization: Bearer E3yyDiR5_i8CFCVDo3h8T5qgKpAdu8XkGZBv81vn428
HTTP/1.1 200 OK
Content-Type: application/json

{
  "port_token": "3O9YHawMDXLpKb-FVjQ1_qSS9R9wbwb0TWbUxLvqAAI",
  "extra_stuff": 34
}
Only OPs explicitly trusted by the Old OP SHOULD be allowed to use the API (eg to use the "port_data" scope) as it is security and privacy sensitive.  In some situations an Old OP will know via other processes when and to whom a user is  porting (eg when it is combined with porting a phone number).  In such circumstances, the Old OP SHOULD reject requests about a user not known to be in the process of porting, and SHOULD reject requests from any OP other than the known porting destination.
4.
Encrypting "port_token"
A "port_token" value received by a New OP is encrypted to create an "enc_port_token" value, which is passed to an RP, then back to the Old OP.
When pairwise Subject Ids are used for enhanced privacy (that is, a user is assigned a separate "sub" value for each collection of related RPs identified by a "sector_id"), any porting information revealed to RPs also needs to be at least pairwise so as not to undermine that privacy. This is achieved by using encrypted versions of the "port_token". Encryption is performed by the New OP, and decryption by the Old OP.
A separate encryption MUST be used whenever a different "sub" value is involved. The encryptions MUST involve nonces so each ciphertext is different.  The nonces themselves MUST NOT allow extra correlations, which effectively means multiple encryptions of a given "port_token" for multiple RPs MUST NOT be pre-calculated during the porting process if the nonces include a counter or time-based component. Instead, it is safe to perform the encryption for an RP when the user subsequently logs in to that RP.
It is RECOMMENDED that a fresh "enc_port_token" value be calculated each time one is sent so they can have short lifetimes, hence avoiding requirements for revocation.
Encryption offers less privacy benefit when the New OP uses public Subject Ids. However, encryption is still used in such cases to avoid introducing additional options to the porting mechanism.
A "port_token" value is encrypted with the Old OP's public encryption key to create an "enc_port_token" value. The New OP obtains the public key by following the "jwks_uri" member in the Old OP's metadata, then selecting a key with a "use":"enc" member and a supported key type ("kty") and encryption algorithm ("alg"). The Old OP can change keys, which the New OP MUST cope with by periodically re-checking the metadata.  Cache-control details delivered with the metadata indicate how often the New OP ought to re-check (with an expectation that keys will not change more often than daily)
[RFC7234]
.
The encryption follows the JSON Web Encryption (JWE) process, creating a JWE compact serialization
[RFC7516]
.  The selected public key provides the key id ("kid") and algorithm ("alg").  The content encryption algorithm ("enc") is chosen from the "port_enc_values_supported" list published in the Old OP's discovery metadata.  The plaintext is the "port_token" value.
The JWE header MUST include a type parameter ("typ") with the value "openid-connect-porting" to explicitly indicate the semantics of the message.  The JWE header MUST include a "sector_id" parameter, holding the host component (that is, a fully-qualified domain name) of the RP's "sector_identifier_uri" or "redirect_uri"
[OpenID.Core]
§ 8.1. "Pairwise Identifier Algorithm".
The New OP MUST support "RSA-OAEP-256" for key encryption and MUST support "A256GCM" for content encryption
[RFC7518]
.
Below is a sample JWE, using keys and tokens from previous sections (with line-breaks just for display purposes only):
JWE protected header:
{
        "typ": "openid-connect-porting",
        "alg": "RSA-OAEP-256",
        "enc": "A256GCM",
        "kid": "oldop43",
  "sector_id": "rp.example.org"
}
Randomly choose a 256-bit AES content encryption key (CEK) and 96-bit GCM nonce (iv); shown in base64url:
cek: t7gDQpQvlLTYc_1KDgRw-iuUr-AvlBYsNM79zR1LP1g
           iv: 48V1_ALb6US04U3b
Encrypt the CEK with the Old OP's RSA public encryption key:
encrypted_key:
  GqwEk3osLFgnGmh6UJsuNUI134QVYKmhtXqfdszQBl70o8-pQLK5eZbun0vFmWhd
  h7VDEUzX3Lxce6CzV80wEH57T-6LlJOjsCTOWmc_I8HUbPfGW4JjxBYv9Woab3Sv
  apSDRne7qJ-ykN_MRYAUVASF5kRGBKLBU6ip3XIagHy0k6M0QnpMhwHdp82AKZl9
  mSc2qwaB7Bhm3zjsPXCklyUUI5ojfEv9jFxYz6IzlMC3a5zObEGHRCIo2Xt21-GQ
  KMBG3fiTd-59GXUupg_aZXECqWcyhSxxMzYMDl8cgrrJXdNMxcuPIywlnR4-JqKz
  9dWVMQNmTdnJ8IqLMjqAwg
The payload is the "port_token" value from the previous section. The additional authenticated data (AAD) is the base64url-encoding of the JWE protected header.
plaintext: 3O9YHawMDXLpKb-FVjQ1_qSS9R9wbwb0TWbUxLvqAAI
          aad: 
  eyJ0eXAiOiJvcGVuaWQtY29ubmVjdC1wb3J0aW5nIiwiYWxnIjoiUlNBLU9BRVAt
  MjU2IiwiZW5jIjoiQTI1NkdDTSIsImtpZCI6Im9sZG9wNDMiLCJzZWN0b3JfaWQi
  OiJycC5leGFtcGxlLm9yZyJ9
Applying AES-GCM encryption gives ciphertext and an authentication tag:
ciphertext:
  IPvR7VRL9tjxZrWMul3v94G4xiyEadCi-nubi0Xg74WIiN4BNbhO58JuuA
           tag: 5JijJVt4bRz7q2C950WH7w
Putting it all together (with eliding and line breaks only for display):
"enc_port_token": "eyJ0eX … 9yZyJ9
                   .GqwEk3 … MjqAwg
                   .48V1_ALb6US04U3b
                   .IPvR7V … 58JuuA
                   .5JijJVt4bRz7q2C950WH7w"
5.
Indicating a previous identity: "aka" member
This document defines the "aka" (also known as) member that indicates that the given user has (or had) another identifier from an Old OP.  An "aka" member can be included in an id_token (issued as part of an OpenID Connect login), or in a Porting check API response [
Section 6
].
An "aka" value is a JSON object with "enc_port_token" and "iss" members, both with string values. "iss" identifies the Old OP.  "enc_port_token" can be used at the Old OP's Porting check API [
Section 6
] to confirm the port and obtain the Old OP's "sub" value for the user.
An "enc_port_token" value is opaque to an RP who receives it: they simply copy it from the "aka" member to an API parameter.  The OP sending an "enc_port_token" MUST construct its value by encrypting a port token as per
Section 4
.
On receiving an id_token, an RP uses "iss" & "sub" to lookup the user's account in the RP's systems. If no such account is found, but the id_token contains an "aka" member, then the RP MUST process the "aka" value to determine if the RP knows the user via federation from an Old OP. Processing involves: calling the Porting check API for the Old OP with the given "enc_port_token"; looking for an existing account at the RP that matches the Old OP's "sub" value; and linking that account to the New OP's "sub" value.
Below is a sample payload of an id_token.
{
  "iss": "https://newop.example.net/",
  "sub": "JRrr09BzhZ6BJ9t0yD8DzyZjg7ziB3a40jeoUvZkUgw",
  "aud": "s6BhdRkqt3"
  "iat": 1471238000
  "exp": 1471238300,
  "at_hash": "mrxuWF8TvnILKqFpZgEYCQ",
  "aka": {
    "iss": "https://oldop.example.net/",
    "enc_port_token": "eyJ0eX … 50WH7w"
  }
}
6.
Porting check API
The Porting check API is offered by an Old OP to RPs so they can confirm that a user did port to a specific New OP. The API converts an "enc_port_token" to a Subject Id ("sub" value), which the RP needs to identify the ported user's existing account at the RP.
Access to the Porting check API requires authentication of the RP.  This enables the Old OP to match the caller of the API to uses of the OpenID Connect authentication process so it can apply any RP-specific policy.  The Old OP and RP MUST support the OAuth 2.0 client credentials flow
[RFC6749]
and Bearer access tokens
[RFC6750]
.  The RP MUST include the scope "port_check" when requesting access.
An RP makes a "GET" request to the API endpoint (from the "port_check_endpoint" member in the Old OP discovery metadata), adding query parameters identifying the New OP ("iss") and a porting event ("enc_port_token"). A successful response (eg with a status code of 200) conveys a JSON object that can have "sub", "aka", and "remove" members.  A successful response means the user associated with "enc_port_token" has ported from the Old OP to the given New OP. Otherwise an unsuccessful HTTP response status code MUST be returned (eg 400 Bad request).
The Old OP makes the following checks:
MUST decrypt the "enc_port_token", which MUST include verifying that it uses acceptable algorithms (for instance, "alg" and "enc" values are not "none").
MUST verify that the JWE "typ" member is present with the value "openid-connect-porting", to avoid misinterpretting the meaning of the JWE.
MUST verify that the "port_token" (the plaintext from the JWE) was issued by the Old OP.
MUST verify that the "iss" query parameter matches the New OP to whom the port_token was given. This confirms that the RP and Old OP have the same understanding of who the New OP is.
SHOULD verify that the "sector_id" from the JWE header matches the sector_id for the RP or matches the domain name portion of the RP's redirect_uri.
A successful response is a JSON object that can include the following members (any unrecognized members MUST be ignored):
"sub"
Old OP's Subject Id for the ported user for the RP, as a string.  This member MAY be absent if the Old OP knows the user never logged in to this RP.
"aka"
Another identifier for the same user, with the same syntax and semantics as when it appears in an id_token [
Section 5
].  It indicates that the user ported to the Old OP from an even older OP.
"remove"
A boolean value (false or true) indicating whether or not the RP can expect future logins from the user via the Old OP.
When the RP does not recognize the "sub" value (in combination with the Old OP's "iss" value), the RP SHOULD process the "aka" value if present as per
Section 5
to determine if the RP knows the user via a login from the even older OP. An RP MUST NOT recursively follow "aka" values indefinitely; a limit of a few recursions is likely to be sufficient for valid use cases.
"remove": true — means the RP MUST no longer accept a login from the Old OP with the given "sub" as valid for this user's account at the RP.  Future logins will be via the New OP.
"remove": false — means the RP can expect and SHOULD continue to accept logins to this account via the Old OP, in addition to logins via the New OP. It indicates that logins from the Old OP and New OP are linked to the same user, but not that one is being replaced by the other.
The Old OP MUST include the "remove" member when "sub" is present.
Below is a sample request with a successful response. [The long request line is wrapped over 4 lines just for display purposes.] The RP would lookup "sub=kY6N6…" & "iss=https://oldop…" in its user database to find the existing account that has ported to the New OP.
GET /connect/port_check
  ?iss=https://newop.example.net/
  &enc_port_token=eyJ0eX … 50WH7w
   HTTP/1.1
Host: oldop.example.net
Authorization: Bearer JOpIXW60qfjKQOlQ8trLBTSzwDl8zGgujLxBVTvWMG8
HTTP/1.1 200 OK
Content-Type: application/json

{
     "sub": "kY6N64H86MBTho9I-JlRnpvaLOwAb5m3yYta6pq1VFM",
  "remove": true
}
Below is a sample response that identifies a previous port. If the RP did not recognize "sub=kY6N6…" & "iss=https://oldop…" it can process the "aka" value to see if that leads back to an account known to the RP.
HTTP/1.1 200 OK
Content-Type: application/json

{
     "sub": "kY6N64H86MBTho9I-JlRnpvaLOwAb5m3yYta6pq1VFM",
  "remove": false,
     "aka": {
               "iss": "https://anotherop.example.net/",
    "enc_port_token": "QSfmp2V30cNqKShhyOjQEwDaQzLNhji5w5nD-EZq3ok"
  }
}
Below is a sample unsuccessful response (which happens to use the Problem Details format specified in
[RFC7807]
).
HTTP/1.1 400 Bad request
Content-Type: application/problem+json

{
   "type": "https://oldop.example.net/probs/porting_rp",
  "title": "Port_token presented by the wrong RP"
}
7.
"user_ported" error code
An Old OP MAY return the "user_ported" error code from the authorization endpoint during an OpenID Connect login flow when the user has ported to a New OP. An RP receiving this error code SHOULD remove any cached hints linking the user to the Old OP (eg a cookie), and SHOULD perform its OP discovery process (for instance, by prompting the user to select an OP, invoking a discovery service, or triggering an account chooser).
The New OP to whom the user ported is not identified in the error response for privacy reasons. It avoids revealing this information before the Old OP has authenticated the RP, and confirmed the user has logged into the RP via the New OP.
8.
Security Considerations
Attacker's goal: get access to the victim's RP accounts either by taking over the respective OP or RP account.  This section analyses the protocol flow along the lines of the migration process for threat vectors. Note: this list is a starting point and not meant to be comprehensive (yet).
8.1.
Impersonation of legitimate user's old OP account
If the attacker can get hold of the authorization grant issued by the old OP for access to the account migration API, the attacker can impersonate the legitimate user in the migration process at the new OP.
Prevent leakage of authorization grant at old OP (mix up, referrer header, log files, ...)
Prevent injection at new OP (TBD - state, id_token, nonce, pkce, token binding, ...)
Audience/purpose restrict access tokens on old OP side, in order to strictly limit access tokens, which can be used for account migration. Combined with a strict limitation (whitelisting) of all clients, which are allowed to request access tokens for account migration shall reduce attack surface.
idea: use migration specific credential, which is directly entered during migration process at new OP (in turn potentially imposes the risk of men in the middle/phishing)
old OP should notify user of account migration process via different communication channel.
8.2.
Trick user into login with attacker's account
The attacker could try to cause the legitimate user to login with her new OP with the attacker's account with this new OP. That would cause the new OP to associate the migration data with the attackers account, which in turn allows the attacker to migrate all RP accounts of the legitimate user to his account with the new OP.
Prevent XSRF, session fixation
Explicitly show user identity data of both user accounts, which she is about to tie together and ask for consent.
Send information back to old OP about new OP identity? It could inform user of the migration, which just happened (too).
8.3.
Impersonate old OP/replay migration data
If the attacker gets hold of valid migration data of an account at OP1 and "migrates" the account data to his account with OP1. Scenario: The attacker logs into the new OP with her OP account and sends the new OP to the OP under her control. This OP returns migration data obtained from a legitimate OP in a previous step.
audience restriction: verify subject of migration data (migrated_to must be iss of new OP)
detection: use discovery to match account migration endpoint to endpoint of legitimate OP
8.4.
Bad OP
Attacker could try to trick victim into (unintentionally) migration her OP account to a OP under the attacker's control
white listing or blacklisting of OPs for which account migration is supported
clear wording and consent during release of the account migration authorization grant.
no SSO and no auto consent: require re-authentication and explicit consent + specific migration credential (just to make the process less convenient and make the victim think about what she is up to.).
old OP should notify user of account migration process via different communication channel.
8.5.
Inject migration data during RP account migration
Attacker gets hold of valid migration data and injects it into the login response. This would only work for implicit grant, not for grant type code.
use grant type code
migration data is included in ID Token, so it is signed by the new OP and cannot be modfied by the attacker.
8.6.
Further Considerations
Note: the new OP could also accidentally assign the account migration data to the wrong user account in its database. Care must be taken that the respective functions are thoroughly tested with every change.
9.
Privacy Considerations
A user's OP can see which RPs the user logs in to, and when.  That is the nature of the OpenID Connect federated login protocol.  By porting, a user moves that visibility from the Old OP to the New OP.
After porting, the Old OP can still see when the user next logs in to each RP, as each RP will contact the Old OP at that time to confirm the port.  This is true even for an RP that the user never accessed via the Old OP, as the RP does not know that this is the case before trying to confirm the port with the Old OP. Subsequent logins to an RP will not be visible to the Old OP.
The New OP learn nothing about a user's activity before the port.  For instance, an RP accessed via the Old OP but not accessed after porting will not be revealed to the New OP.
RPs see which Old OP a user has used, which is necessary for continuity of access after porting. Even an RP that a user never accessed before the port learns about the user's Old OP.  An RP that is not accessed after porting does not learn of the port.
10.
IANA Considerations
This document registers the "aka" claim in the IANA "JSON Web Token Claims" registry
[IANA.JWT_Claims]
.
Claim Name: "aka"
Claim Description: Also Known As
Change Controller: OpenID Foundation MODRNA working group <https://openid.net/wg/mobile/>
Specification Document(s):
Section 5
of [[ this specification ]]
This document registers the "sector_id" claim in the IANA "JSON Web Signature and Encryption Header Parameters" registry
[IANA.JOSE]
.
Header Parameter Name: "sector_id"
Header Parameter Description: Sector identifier for a group of websites under common administrative control
Header Parameter Usage Location: JWE
Change Controller: OpenID Foundation MODRNA working group <https://openid.net/wg/mobile/>
Specification Document(s):
Section 4
of [[ this specification ]]
This document registers the "user_ported" error code in the IANA "OAuth Extensions Error Registry"
[IANA.OAUTH]
.
Error name: "user_ported"
Error usage location: authorization endpoint
Related protocol extension:
Change controller: OpenID Foundation
Specification document:
Section 7
of [[ this specification ]]
This document registers the "application/openid-connect-porting" media type in the IANA "Media Types" registry
[IANA.MEDIA]
.  It identifies a JSON Web Encryption (JWE) compact serialization that is the encryption of a port token.
Type name: application
Subtype name: openid-connect-porting
Required parameters: N/A
Optional parameters: N/A
Encoding considerations: 7bit
Security considerations: see
[RFC7516]
Interoperability considerations: N/A
Published specification:
Section 4
of [[ this specification ]]
Applications that use this media type: OpenID Connect
Fragment identifier considerations: N/A
Additional information: N/A
Intended usage: COMMON
Restrictions on usage: N/A
Change controller: OpenID Foundation
11.
References
11.1.
Normative References
[OpenID.Core]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
,
de Medeiros, B.
and
C. Mortimore
, "
OpenID Connect Core 1.0
", November 2014.
[OpenID.Discovery]
Sakimura, N.
,
Bradley, J.
,
Jones, M.
and
E. Jay
, "
OpenID Connect Discovery 1.0
", November 2014.
[IANA.JWT_Claims]
IANA
, "
JSON Web Token Claims
", January 2015.
[IANA.JOSE]
IANA
, "
JSON Object Signing and Encryption (JOSE)
", January 2015.
[IANA.OAUTH]
IANA
, "
OAuth Parameters
", July 2012.
[IANA.MEDIA]
IANA
, "
Media Types
", November 2016.
[RFC7234]
Fielding, R.
,
Nottingham, M.
and
J. Reschke
, "
Hypertext Transfer Protocol (HTTP/1.1): Caching
", RFC 7234, DOI 10.17487/RFC7234, June 2014.
[RFC7516]
Jones, M.
and
J. Hildebrand
, "
JSON Web Encryption (JWE)
", RFC 7516, DOI 10.17487/RFC7516, May 2015.
[RFC7517]
Jones, M.
, "
JSON Web Key (JWK)
", RFC 7517, DOI 10.17487/RFC7517, May 2015.
[RFC7518]
Jones, M.
, "
JSON Web Algorithms (JWA)
", RFC 7518, DOI 10.17487/RFC7518, May 2015.
[RFC6749]
Hardt, D.
, "
The OAuth 2.0 Authorization Framework
", RFC 6749, DOI 10.17487/RFC6749, October 2012.
[RFC6750]
Jones, M.
and
D. Hardt
, "
The OAuth 2.0 Authorization Framework: Bearer Token Usage
", RFC 6750, DOI 10.17487/RFC6750, October 2012.
[RFC2119]
Bradner, S.
, "
Key words for use in RFCs to Indicate Requirement Levels
", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.
11.2.
Informative References
[MobileConnect]
GSMA
, "
Mobile Connect
", January 2015.
[RFC7807]
Nottingham, M.
and
E. Wilde
, "
Problem Details for HTTP APIs
", RFC 7807, DOI 10.17487/RFC7807, March 2016.
Appendix A.
Example flow
This example involves a user (Alice), an RP, and 3 OPs (OP1, OP2, and OP3).  Alice originally federated to the RP via OP1; ported to OP2; then (shortly afterwards) ported to OP3. When Alice logs in to RP via OP3 for the first time she is not recognized directly from OP3's id_token. But by following the "aka" trail, the RP automatically establishes the link to an id from OP1 that the RP recognizes as Alice.
Many details are elided. Dotted arrows represent HTTP redirects.
Appendix B.
Acknowledgements
The following people in particular have contributed to the development of this specification: Jörg Connotte; John Bradley; Axel Nennker.
Appendix C.
Notices
Copyright (c) 2017 The OpenID Foundation.
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others. Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights. The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer. The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers. The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
Appendix D.
Document history
[[ To be removed from the final specification ]]
-07
Change co-author affilliation
-06
Privacy considerations
Example values
-05
Public key encryption of the port_token
Mandate RSA-OAEP-256 and AES256GCM
-04
Clarify and reorganize
-03
Overview of porting flow
"remove":true/false signal from Old OP to RP
user_ported error code
"oidc_porting" renamed to "openid-connect-porting"
-02
Remove unencrypted port tokens
Authenticate RPs to Old OP
-01
Single port_token from Old OP to New OP
Encrypted port_token from New OP to RP
Torsten and Arne as additional authors
-00
Initial draft
Proposed as an alternative approach to draft-account-migration-02
Authors' Addresses
James Manger
Manger
Telstra
EMail:
james.h.manger@team.telstra.com
Torsten Lodderstedt
Lodderstedt
YES Europe AG
EMail:
torsten@yes.de
Arne Georg Gleditsch
Gleditsch
Telenor
EMail:
argggh@telenordigital.com