---
{
  "title": "Jose.Jwe",
  "url": "https://hackage.haskell.org/package/jose-jwt-0.1/docs/Jose-Jwe.html",
  "domain": "hackage.haskell.org",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 1258,
  "crawled_at": "2026-04-23T20:48:43"
}
---

Jose.Jwe
Source
Contents
Index
jose-jwt-0.1: JSON Object Signing and Encryption Library
Safe Haskell
None
Jose.Jwe
Description
JWE RSA encrypted token support.
Example usage:
>>>
import Jose.Jwe
>>>
import Jose.Jwa
>>>
import Crypto.Random.AESCtr
>>>
g <- makeSystem
>>>
import Crypto.PubKey.RSA
>>>
let ((kPub, kPr), g') = generate g 512 65537
>>>
let (jwt, g'') = rsaEncode g' RSA_OAEP A128GCM kPub "secret claims"
>>>
rsaDecode kPr jwt
Right (JweHeader {jweAlg = RSA_OAEP, jweEnc = A128GCM, jweTyp = Nothing, jweCty = Nothing, jweZip = Nothing, jweKid = Nothing},"secret claims")
Synopsis
rsaEncode
::
CPRG
g => g ->
JweAlg
->
Enc
->
PublicKey
->
ByteString
-> (
ByteString
, g)
rsaDecode
::
PrivateKey
->
ByteString
->
Either
JwtError
Jwe
Documentation
rsaEncode
Source
Arguments
::
CPRG
g
=> g
Random number generator
->
JweAlg
RSA algorithm to use (
RSA_OAEP
or
RSA1_5
)
->
Enc
Content encryption algorithm
->
PublicKey
RSA key to encrypt with
->
ByteString
The JWT claims (content)
-> (
ByteString
, g)
The encoded JWE and new generator
Creates a JWE.
rsaDecode
Source
Arguments
::
PrivateKey
Decryption key
->
ByteString
The encoded JWE
->
Either
JwtError
Jwe
The decoded JWT, unless an error occurs
Decrypts a JWE.
Produced by
Haddock
version 2.13.2