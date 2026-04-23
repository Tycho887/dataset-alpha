---
{
  "title": "CBOR Object Signing and Encryption (COSE)",
  "url": "https://www.iana.org/assignments/cose",
  "domain": "www.iana.org",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 25730,
  "crawled_at": "2026-04-23T20:56:24"
}
---

CBOR Object Signing and Encryption (COSE)
Created
2017-01-11
Last Updated
2026-03-04
Available Formats
XML
HTML
Plain text
Registries Included Below
COSE Header Parameters
COSE Header Algorithm Parameters
COSE Algorithms
COSE Key Common Parameters
COSE Key Type Parameters
COSE Key Types
COSE Elliptic Curves
COSE Verifiable Data Structure Algorithms
COSE Verifiable Data Structure Proofs
COSE Header Parameters
Expert(s)
Francesca Palombini, Carsten Bormann
Reference
[
RFC9052
]
Available Formats
CSV
Range
Registration Procedures
Integers less than -65536
Private Use
Integer values in the range -1 to -65536
delegated to the COSE Header Algorithm Parameters registry
Integer values between 1 and 255
Standards Action With Expert Review
Integer values from 256 to 65535
Specification Required
Integer values greater than 65535
Expert Review
Strings of length 1
Standards Action With Expert Review
Strings of length 2
Specification Required
Strings of length greater than 2
Expert Review
Name
Label
Value Type
Value Registry
Description
Reference
Reserved for Private Use
less than -65536
[
RFC9052
]
delegated to the COSE Header Algorithm Parameters registry
-65536 to -1
Reserved
0
[
RFC9052
]
alg
1
int / tstr
[
COSE Algorithms
]
Cryptographic algorithm to use
[
RFC9052
]
crit
2
[+ label]
[
COSE Header Parameters
]
Critical headers to be understood
[
RFC9052
]
content type
3
tstr / uint
[
COAP Content-Formats
] 
        or [
Media Types
]
Content type of the payload
[
RFC9052
]
kid
4
bstr
Key identifier
[
RFC9052
]
IV
5
bstr
Full Initialization Vector
[
RFC9052
]
Partial IV
6
bstr
Partial Initialization Vector
[
RFC9052
]
counter signature
7
COSE_Signature / [+ COSE_Signature ]
CBOR-encoded signature structure (Deprecated by [
RFC9338
])
[
RFC8152
]
Unassigned
8
CounterSignature0
9
bstr
Counter signature with implied signer and headers (Deprecated by [
RFC9338
])
[
RFC8152
]
kid context
10
bstr
Identifies the context for the key identifier
[
RFC8613, Section 5.1
]
Countersignature version 2
11
COSE_Countersignature / [+ COSE_Countersignature]
V2 countersignature attribute
[
RFC9338
]
Countersignature0 version 2
12
COSE_Countersignature0
V2 Abbreviated Countersignature
[
RFC9338
]
kcwt
13
COSE_Messages
A CBOR Web Token (CWT) containing a COSE_Key in a 'cnf' 
        claim and possibly other claims. CWT is defined in [
RFC8392
]. 
        COSE_Messages is defined in [
RFC9052
].
[
RFC9528
]
kccs
14
map
A CWT Claims Set (CCS) containing a COSE_Key in a 'cnf' 
        claim and possibly other claims. CCS is defined in [
RFC8392
].
[
RFC9528
]
CWT Claims
15
map
map keys in [
CWT Claims
]
Location for CWT Claims in COSE Header Parameters.
[
RFC9597, Section 2
]
typ (type)
16
uint / tstr
[
COAP Content-Formats
] 
        or [
Media Types
]
Content type of the complete COSE object
[
RFC9596, Section 2
]
sd_claims (TEMPORARY - registered 2026-01-16, expires 2027-01-16)
17
[ +bstr ]
A list of selectively disclosed claims, which were originally redacted, then later disclosed at the discretion of the sender.
[
RFC-ietf-spice-sd-cwt-06, Section 4
]
Unassigned
18-21
c5t (TEMPORARY - registered 2024-03-11, publication requested 2025-09-23)
22
COSE_CertHash
Hash of a C509Certificate
[
draft-ietf-cose-cbor-encoded-cert-12
]
c5u (TEMPORARY - registered 2024-03-11, publication requested 2025-09-23)
23
uri
URI pointing to a COSE_C509 containing an ordered chain of certificates
[
draft-ietf-cose-cbor-encoded-cert-12
]
c5b (TEMPORARY - registered 2024-03-11, publication requested 2025-09-23)
24
COSE_C509
An unordered bag of C509 certificates
[
draft-ietf-cose-cbor-encoded-cert-12
]
c5c (TEMPORARY - registered 2024-03-11, publication requested 2025-09-23)
25
COSE_C509
An ordered chain of C509 certificates
[
draft-ietf-cose-cbor-encoded-cert-12
]
Unassigned
26-31
x5bag
32
COSE_X509
An unordered bag of X.509 certificates
[
RFC9360
]
x5chain
33
COSE_X509
An ordered chain of X.509 certificates
[
RFC9360
]
x5t
34
COSE_CertHash
Hash of an X.509 certificate
[
RFC9360
]
x5u
35
uri
URI pointing to an X.509 certificate
[
RFC9360
]
Unassigned
36-169
sd_alg (TEMPORARY - registered 2026-01-16, expires 2027-01-16)
170
int
[
COSE Algorithms
]
The hash algorithm used for redacting disclosures.
[
RFC-ietf-spice-sd-cwt-06, Section 7
]
sd_aead_encrypted_claims (TEMPORARY - registered 2026-01-16, expires 2027-01-16)
171
[ +[bstr,bstr,bstr] ]
A list of AEAD encrypted selectively disclosed claims, which were originally redacted, then later disclosed at the discretion of the sender.
[
RFC-ietf-spice-sd-cwt-06, Section 12.1
]
sd_aead (TEMPORARY - registered 2026-01-16, expires 2027-01-16)
172
uint .size 2
[
AEAD Algorithms
]
The AEAD algorithm used for encrypting disclosures.
[
RFC-ietf-spice-sd-cwt-06, Section 12.1
]
Unassigned
173-255
CUPHNonce
256
bstr
Challenge Nonce
[
FIDO Device Onboard Specification
]
CUPHOwnerPubKey
257
array
Public Key
[
FIDO Device Onboard Specification
]
payload-hash-alg
258
int
[
COSE Algorithms
]
The hash algorithm used to produce the payload of a COSE_Sign1
[
RFC-ietf-cose-hash-envelope-09, Section 3
]
preimage-content-type
259
uint / tstr
[
CoAP Content-Formats
]
The content-format number or content-type (media-type name) of data that has been hashed to produce the payload of the COSE_Sign1
[
RFC-ietf-cose-hash-envelope-09, Section 3
]
payload-location
260
tstr
The string or URI hint for the location of the data hashed to produce the payload of a COSE_Sign1
[
RFC-ietf-cose-hash-envelope-09, Section 3
]
x5ts
261
array of COSE_CertHash
CBOR array of instances of COSE_CertHash
[
TS 119 152-1 V0.0.9, Clause 5.2.2
]
srCms
262
array of SrCm
set of commitments and optional commitments qualifiers
[
TS 119 152-1 V0.0.9, Clause 5.2.3
]
sigPl
263
map
CBOR map for indicating the location where the signature was generated. 
It may contain an indication of the country, the locality, the region, a box number in a 
post office, the postal code, and the street address
[
TS 119 152-1 V0.0.9, Clause 5.2.4
]
srAts
264
map
CBOR map that may contain: an array of attributes that the signer claims 
to be in possession of, an array of attribute certificates (X.509 attribute certificates or 
other) issued to the signer, an array of signed assertions issued by a third party to the signer,
or any combination of the three aforementioned CBOR arrays
[
TS 119 152-1 V0.0.9, Clause 5.2.5
]
adoTst
265
map
CBOR map that encapsulates one or more electronic time-stamps, generated 
before the signature production, and whose message imprint computation input is the COSE 
Payload of the CB-AdES signature
[
TS 119 152-1 V0.0.9, Clause 5.2.6
]
sigPId
266
map
CBOR map that identifies a certain signature policy and may contain the 
digest of the document defining this signature policy.
[
TS 119 152-1 V0.0.9, Clause 5.2.7
]
sigD
267
map
CBOR map that references data objects that are detached from the CB-AdES 
signature and that are collectively signed.
[
TS 119 152-1 V0.0.9, Clause 5.2.8
]
uHeaders
268
[+bstr]
CBOR array that contains a number of CBOR elements that are placed within 
the array in the order they are incorporated into the CB-AdES signature
[
TS 119 152-1 V0.0.9, Clause 5.3.1
]
3161-ttc
269
bstr
Timestamp Token per [
RFC3161
]: Timestamp, Then COSE
[
RFC9921, Section 3.2
]
3161-ctt
270
bstr
Timestamp Token per [
RFC3161
]: COSE, Then Timestamp
[
RFC9921, Section 3.1
]
Unassigned
271-393
receipts
394
array
Priority ordered sequence of CBOR encoded Receipts
[
RFC-ietf-cose-merkle-tree-proofs-18, Section 2
]
vds
395
int
[
COSE Verifiable Data Structure Algorithms
]
Algorithm identifier for verifiable data structures, used to produce verifiable data structure proofs
[
RFC-ietf-cose-merkle-tree-proofs-18, Section 2
]
vdp
396
map
map key in [
COSE Verifiable Data Structure Proofs
]
Location for verifiable data structure proofs in COSE Header Parameters
[
RFC-ietf-cose-merkle-tree-proofs-18, Section 2
]
COSE Header Algorithm Parameters
Registration Procedure(s)
Expert Review
Expert(s)
Göran Selander, Derek Atkins, Sean Turner
Reference
[
RFC9053
]
Available Formats
CSV
Name
Algorithm
Label
Type
Description
Reference
Unassigned
-65536 to -30
x5chain-sender
ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-SS+A128KW, 
        ECDH-SS+A192KW, ECDH-SS+A256KW
-29
COSE_X509
static key X.509 certificate chain
[
RFC9360
]
x5u-sender
ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-SS+A128KW,
        ECDH-SS+A192KW, ECDH-SS+A256KW
-28
uri
URI for the sender's X.509 certificate
[
RFC9360
]
x5t-sender
ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-SS+A128KW,
        ECDH-SS+A192KW, ECDH-SS+A256KW
-27
COSE_CertHash
Thumbprint for the sender's X.509 certificate
[
RFC9360
]
PartyV other
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-26
bstr
Party V other provided information
[
RFC9053
]
PartyV nonce
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-25
bstr / int
Party V provided nonce
[
RFC9053
]
PartyV identity
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-24
bstr
Party V identity information
[
RFC9053
]
PartyU other
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-23
bstr
Party U other provided information
[
RFC9053
]
PartyU nonce
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-22
bstr / int
Party U provided nonce
[
RFC9053
]
PartyU identity
direct+HKDF-SHA-256, direct+HKDF-SHA-512, direct+HKDF-AES-128, 
        direct+HKDF-AES-256, ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, 
        ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-ES+A128KW, ECDH-ES+A192KW, 
        ECDH-ES+A256KW, ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-21
bstr
Party U identity information
[
RFC9053
]
salt
direct+HKDF-SHA-256, direct+HKDF-SHA-512, 
        direct+HKDF-AES-128, direct+HKDF-AES-256, ECDH-ES+HKDF-256, 
        ECDH-ES+HKDF-512, ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, 
        ECDH-ES+A128KW, ECDH-ES+A192KW, ECDH-ES+A256KW, 
        ECDH-SS+A128KW, ECDH-SS+A192KW, ECDH-SS+A256KW
-20
bstr
Random salt
[
RFC9053
]
Unassigned
-19 to -4
static key id
ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-SS+A128KW, 
        ECDH-SS+A192KW, ECDH-SS+A256KW
-3
bstr
Static public key identifier for the sender
[
RFC9053
]
static key
ECDH-SS+HKDF-256, ECDH-SS+HKDF-512, ECDH-SS+A128KW, 
        ECDH-SS+A192KW, ECDH-SS+A256KW
-2
COSE_Key
Static public key for the sender
[
RFC9053
]
ephemeral key
ECDH-ES+HKDF-256, ECDH-ES+HKDF-512, ECDH-ES+A128KW, 
        ECDH-ES+A192KW, ECDH-ES+A256KW
-1
COSE_Key
Ephemeral public key for the sender
[
RFC9053
]
COSE Algorithms
Expert(s)
Göran Selander, Derek Atkins, Sean Turner
Reference
[
RFC9053
][
RFC9054
][
RFC9864, Section 4.2
]
Available Formats
CSV
Range
Registration Procedures
Integers less than -65536
Private Use
Integer values from -65536 to -257
Specification Required
Integer values between -256 and 255
Standards Action With Expert Review
Integer values from 256 to 65535
Specification Required
Integer values greater than 65535
Expert Review
Strings of length 1
Standards Action With Expert Review
Strings of length 2
Specification Required
Strings of length greater than 2
Expert Review
Name
Value
Description
Capabilities
Change Controller
Reference
Recommended
Reserved for Private Use
less than -65536
[
RFC9053
]
No
Unassigned
-65536
RS1
-65535
RSASSA-PKCS1-v1_5 using SHA-1
[kty]
IESG
[
RFC8812
][
RFC9053
]
Deprecated
A128CTR
-65534
AES-CTR w/ 128-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
A192CTR
-65533
AES-CTR w/ 192-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
A256CTR
-65532
AES-CTR w/ 256-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
A128CBC
-65531
AES-CBC w/ 128-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
A192CBC
-65530
AES-CBC w/ 192-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
A256CBC
-65529
AES-CBC w/ 256-bit key
[kty]
IETF
[
RFC9459
]
Deprecated
Unassigned
-65528 to -269
ESB512
-268
ECDSA using BrainpoolP512r1 curve and SHA-512
[kty]
IETF
[
RFC9864, Section 2.1
]
No
ESB384
-267
ECDSA using BrainpoolP384r1 curve and SHA-384
[kty]
IETF
[
RFC9864, Section 2.1
]
No
ESB320
-266
ECDSA using BrainpoolP320r1 curve and SHA-384
[kty]
IETF
[
RFC9864, Section 2.1
]
No
ESB256
-265
ECDSA using BrainpoolP256r1 curve and SHA-256
[kty]
IETF
[
RFC9864, Section 2.1
]
No
KT256
-264
KT256 XOF
[kty]
IETF
[
RFC9861
]
No
KT128
-263
KT128 XOF
[kty]
IETF
[
RFC9861
]
No
TurboSHAKE256
-262
TurboSHAKE256 XOF
[kty]
IETF
[
RFC9861
]
No
TurboSHAKE128
-261
TurboSHAKE128 XOF
[kty]
IETF
[
RFC9861
]
No
WalnutDSA
-260
WalnutDSA signature
[kty]
[
RFC9021
][
RFC9053
]
No
RS512
-259
RSASSA-PKCS1-v1_5 using SHA-512
[kty]
IESG
[
RFC8812
][
RFC9053
]
No
RS384
-258
RSASSA-PKCS1-v1_5 using SHA-384
[kty]
IESG
[
RFC8812
][
RFC9053
]
No
RS256
-257
RSASSA-PKCS1-v1_5 using SHA-256
[kty]
IESG
[
RFC8812
][
RFC9053
]
No
Unassigned
-256 to -54
Ed448
-53
EdDSA using the Ed448 parameter set in Section 5.2 of [
RFC8032
]
[kty]
IETF
[
RFC9864, Section 2.2
]
Yes
ESP512
-52
ECDSA using P-521 curve and SHA-512
[kty]
IETF
[
RFC9864, Section 2.1
]
Yes
ESP384
-51
ECDSA using P-384 curve and SHA-384
[kty]
IETF
[
RFC9864, Section 2.1
]
Yes
ML-DSA-87
-50
CBOR Object Signing Algorithm for ML-DSA-87
[kty]
IETF
[
RFC-ietf-cose-dilithium-10
]
Yes
ML-DSA-65
-49
CBOR Object Signing Algorithm for ML-DSA-65
[kty]
IETF
[
RFC-ietf-cose-dilithium-10
]
Yes
ML-DSA-44
-48
CBOR Object Signing Algorithm for ML-DSA-44
[kty]
IETF
[
RFC-ietf-cose-dilithium-10
]
Yes
ES256K
-47
ECDSA using secp256k1 curve and SHA-256
[kty]
IESG
[
RFC8812
][
RFC9053
]
No
HSS-LMS
-46
HSS/LMS hash-based digital signature
[kty]
[
RFC8778
][
RFC9053
]
Yes
SHAKE256
-45
SHAKE-256 512-bit Hash Value
[kty]
[
RFC9054
][
RFC9053
]
Yes
SHA-512
-44
SHA-2 512-bit Hash
[kty]
[
RFC9054
][
RFC9053
]
Yes
SHA-384
-43
SHA-2 384-bit Hash
[kty]
[
RFC9054
][
RFC9053
]
Yes
RSAES-OAEP w/ SHA-512
-42
RSAES-OAEP w/ SHA-512
[kty]
[
RFC8230
][
RFC9053
]
Yes
RSAES-OAEP w/ SHA-256
-41
RSAES-OAEP w/ SHA-256
[kty]
[
RFC8230
][
RFC9053
]
Yes
RSAES-OAEP w/ RFC 8017 default parameters
-40
RSAES-OAEP w/ SHA-1
[kty]
[
RFC8230
][
RFC9053
]
Yes
PS512
-39
RSASSA-PSS w/ SHA-512
[kty]
[
RFC8230
][
RFC9053
]
Yes
PS384
-38
RSASSA-PSS w/ SHA-384
[kty]
[
RFC8230
][
RFC9053
]
Yes
PS256
-37
RSASSA-PSS w/ SHA-256
[kty]
[
RFC8230
][
RFC9053
]
Yes
ES512
-36
ECDSA w/ SHA-512
[kty]
IETF
[
RFC9053
][
RFC9864
]
Deprecated
ES384
-35
ECDSA w/ SHA-384
[kty]
IETF
[
RFC9053
][
RFC9864
]
Deprecated
ECDH-SS + A256KW
-34
ECDH SS w/ Concat KDF and AES Key Wrap w/ 256-bit key
[kty]
[
RFC9053
]
Yes
ECDH-SS + A192KW
-33
ECDH SS w/ Concat KDF and AES Key Wrap w/ 192-bit key
[kty]
[
RFC9053
]
Yes
ECDH-SS + A128KW
-32
ECDH SS w/ Concat KDF and AES Key Wrap w/ 128-bit key
[kty]
[
RFC9053
]
Yes
ECDH-ES + A256KW
-31
ECDH ES w/ Concat KDF and AES Key Wrap w/ 256-bit key
[kty]
[
RFC9053
]
Yes
ECDH-ES + A192KW
-30
ECDH ES w/ Concat KDF and AES Key Wrap w/ 192-bit key
[kty]
[
RFC9053
]
Yes
ECDH-ES + A128KW
-29
ECDH ES w/ Concat KDF and AES Key Wrap w/ 128-bit key
[kty]
[
RFC9053
]
Yes
ECDH-SS + HKDF-512
-28
ECDH SS w/ HKDF - generate key directly
[kty]
[
RFC9053
]
Yes
ECDH-SS + HKDF-256
-27
ECDH SS w/ HKDF - generate key directly
[kty]
[
RFC9053
]
Yes
ECDH-ES + HKDF-512
-26
ECDH ES w/ HKDF - generate key directly
[kty]
[
RFC9053
]
Yes
ECDH-ES + HKDF-256
-25
ECDH ES w/ HKDF - generate key directly
[kty]
[
RFC9053
]
Yes
Unassigned
-24 to -20
Ed25519
-19
EdDSA using the Ed25519 parameter set in Section 5.1 of [
RFC8032
]
[kty]
IETF
[
RFC9864, Section 2.2
]
Yes
SHAKE128
-18
SHAKE-128 256-bit Hash Value
[kty]
[
RFC9054
][
RFC9053
]
Yes
SHA-512/256
-17
SHA-2 512-bit Hash truncated to 256-bits
[kty]
[
RFC9054
][
RFC9053
]
Yes
SHA-256
-16
SHA-2 256-bit Hash
[kty]
[
RFC9054
][
RFC9053
]
Yes
SHA-256/64
-15
SHA-2 256-bit Hash truncated to 64-bits
[kty]
[
RFC9054
][
RFC9053
]
Filter Only
SHA-1
-14
SHA-1 Hash
[kty]
[
RFC9054
][
RFC9053
]
Filter Only
direct+HKDF-AES-256
-13
Shared secret w/ AES-MAC 256-bit key
[kty]
[
RFC9053
]
Yes
direct+HKDF-AES-128
-12
Shared secret w/ AES-MAC 128-bit key
[kty]
[
RFC9053
]
Yes
direct+HKDF-SHA-512
-11
Shared secret w/ HKDF and SHA-512
[kty]
[
RFC9053
]
Yes
direct+HKDF-SHA-256
-10
Shared secret w/ HKDF and SHA-256
[kty]
[
RFC9053
]
Yes
ESP256
-9
ECDSA using P-256 curve and SHA-256
[kty]
IETF
[
RFC9864, Section 2.1
]
Yes
EdDSA
-8
EdDSA
[kty]
IETF
[
RFC9053
][
RFC9864
]
Deprecated
ES256
-7
ECDSA w/ SHA-256
[kty]
IETF
[
RFC9053
][
RFC9864
]
Deprecated
direct
-6
Direct use of CEK
[kty]
[
RFC9053
]
Yes
A256KW
-5
AES Key Wrap w/ 256-bit key
[kty]
[
RFC9053
]
Yes
A192KW
-4
AES Key Wrap w/ 192-bit key
[kty]
[
RFC9053
]
Yes
A128KW
-3
AES Key Wrap w/ 128-bit key
[kty]
[
RFC9053
]
Yes
Unassigned
-2 to -1
Reserved
0
[
RFC9053
]
No
A128GCM
1
AES-GCM mode w/ 128-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
A192GCM
2
AES-GCM mode w/ 192-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
A256GCM
3
AES-GCM mode w/ 256-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
HMAC 256/64
4
HMAC w/ SHA-256 truncated to 64 bits
[kty]
[
RFC9053
]
Yes
HMAC 256/256
5
HMAC w/ SHA-256
[kty]
[
RFC9053
]
Yes
HMAC 384/384
6
HMAC w/ SHA-384
[kty]
[
RFC9053
]
Yes
HMAC 512/512
7
HMAC w/ SHA-512
[kty]
[
RFC9053
]
Yes
Unassigned
8-9
AES-CCM-16-64-128
10
AES-CCM mode 128-bit key, 64-bit tag, 13-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-16-64-256
11
AES-CCM mode 256-bit key, 64-bit tag, 13-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-64-64-128
12
AES-CCM mode 128-bit key, 64-bit tag, 7-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-64-64-256
13
AES-CCM mode 256-bit key, 64-bit tag, 7-byte nonce
[kty]
[
RFC9053
]
Yes
AES-MAC 128/64
14
AES-MAC 128-bit key, 64-bit tag
[kty]
[
RFC9053
]
Yes
AES-MAC 256/64
15
AES-MAC 256-bit key, 64-bit tag
[kty]
[
RFC9053
]
Yes
Unassigned
16-23
ChaCha20/Poly1305
24
ChaCha20/Poly1305 w/ 256-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
AES-MAC 128/128
25
AES-MAC 128-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
AES-MAC 256/128
26
AES-MAC 256-bit key, 128-bit tag
[kty]
[
RFC9053
]
Yes
Unassigned
27-29
AES-CCM-16-128-128
30
AES-CCM mode 128-bit key, 128-bit tag, 13-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-16-128-256
31
AES-CCM mode 256-bit key, 128-bit tag, 13-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-64-128-128
32
AES-CCM mode 128-bit key, 128-bit tag, 7-byte nonce
[kty]
[
RFC9053
]
Yes
AES-CCM-64-128-256
33
AES-CCM mode 256-bit key, 128-bit tag, 7-byte nonce
[kty]
[
RFC9053
]
Yes
IV-GENERATION
34
For doing IV generation for symmetric algorithms.
[
RFC9053
]
No
COSE Key Common Parameters
Expert(s)
Francesca Palombini, Carsten Bormann
Reference
[
RFC9052
]
Available Formats
CSV
Range
Registration Procedures
Integers less than -65536
Private Use
Integer values in the range -65536 to -1
used for key parameters specific to a single algorithm
delegated to the COSE Key Type Parameters registry
Integer values between 0 and 255
Standards Action With Expert Review
Integer values from 256 to 65535
Specification Required
Integer values greater than 65535
Expert Review
Strings of length 1
Standards Action With Expert Review
Strings of length 2
Specification Required
Strings of length greater than 2
Expert Review
Name
Label
CBOR Type
Value Registry
Description
Reference
Reserved for Private Use
less than -65536
[
RFC9052
]
used for key parameters specific to a single algorithm
        delegated to the COSE Key Type Parameters registry
-65536 to -1
[
RFC9052
]
Reserved
0
[
RFC9052
]
kty
1
tstr / int
[
COSE Key Types
]
Identification of the key type
[
RFC9052
]
kid
2
bstr
Key identification value - match to kid in message
[
RFC9052
]
alg
3
tstr / int
[
COSE Algorithms
]
Key usage restriction to this algorithm
[
RFC9052
]
key_ops
4
[+ (tstr/int)]
Restrict set of permissible operations
[
RFC9052
]
Base IV
5
bstr
Base IV to be XORed with Partial IVs
[
RFC9052
]
COSE Key Type Parameters
Registration Procedure(s)
Expert Review
Expert(s)
Göran Selander, Derek Atkins, Sean Turner
Reference
[
RFC9053
]
Available Formats
CSV
Key Type
Name
Label
CBOR Type
Description
Reference
1
crv
-1
int / tstr
EC identifier -- Taken from the "COSE Elliptic Curves" registry
[
RFC9053
]
1
x
-2
bstr
Public Key
[
RFC9053
]
1
d
-4
bstr
Private key
[
RFC9053
]
2
crv
-1
int / tstr
EC identifier -- Taken from the "COSE Elliptic Curves" registry
[
RFC9053
]
2
x
-2
bstr
x-coordinate
[
RFC9053
]
2
y
-3
bstr / bool
y-coordinate
[
RFC9053
]
2
d
-4
bstr
Private key
[
RFC9053
]
3
n
-1
bstr
the RSA modulus n
[
RFC8230
]
3
e
-2
bstr
the RSA public exponent e
[
RFC8230
]
3
d
-3
bstr
the RSA private exponent d
[
RFC8230
]
3
p
-4
bstr
the prime factor p of n
[
RFC8230
]
3
q
-5
bstr
the prime factor q of n
[
RFC8230
]
3
dP
-6
bstr
dP is d mod (p - 1)
[
RFC8230
]
3
dQ
-7
bstr
dQ is d mod (q - 1)
[
RFC8230
]
3
qInv
-8
bstr
qInv is the CRT coefficient q^(-1) mod p
[
RFC8230
]
3
other
-9
array
other prime infos, an array
[
RFC8230
]
3
r_i
-10
bstr
a prime factor r_i of n, where i >= 3
[
RFC8230
]
3
d_i
-11
bstr
d_i = d mod (r_i - 1)
[
RFC8230
]
3
t_i
-12
bstr
the CRT coefficient t_i = (r_1 * r_2 * ... *
        r_(i-1))^(-1) mod r_i
[
RFC8230
]
4
k
-1
bstr
Key Value
[
RFC9053
]
5
pub
-1
bstr
Public key for HSS/LMS hash-based digital signature
[
RFC8778
]
6
N
-1
uint
Group and Matrix (NxN) size
[
RFC9021
]
6
q
-2
uint
Finite field F_q
[
RFC9021
]
6
t-values
-3
array (of uint)
List of T-values, entries in F_q
[
RFC9021
]
6
matrix 1
-4
array (of array of uint)
NxN Matrix of entries in F_q in column-major form
[
RFC9021
]
6
permutation 1
-5
array (of uint)
Permutation associated with matrix 1
[
RFC9021
]
6
matrix 2
-6
array (of array of uint)
NxN Matrix of entries in F_q in column-major form
[
RFC9021
]
7
pub
-1
bstr
Public key
[
RFC-ietf-cose-dilithium-10
]
7
priv
-2
bstr
Private key
[
RFC-ietf-cose-dilithium-10
]
COSE Key Types
Registration Procedure(s)
Expert Review
Expert(s)
Göran Selander, Derek Atkins, Sean Turner
Reference
[
RFC9053
]
Available Formats
CSV
Name
Value
Description
Capabilities
Reference
Reserved
0
This value is reserved
[
RFC9053
]
OKP
1
Octet Key Pair
[kty(1), crv]
[
RFC9053
]
EC2
2
Elliptic Curve Keys w/ x- and y-coordinate pair
[kty(2), crv]
[
RFC9053
]
RSA
3
RSA Key
[kty(3)]
[
RFC8230
][
RFC9053
]
Symmetric
4
Symmetric Keys
[kty(4)]
[
RFC9053
]
HSS-LMS
5
Public key for HSS/LMS hash-based digital signature
[kty(5), hash algorithm]
[
RFC8778
][
RFC9053
]
WalnutDSA
6
WalnutDSA public key
[kty(6)]
[
RFC9021
][
RFC9053
]
AKP
7
COSE Key Type for Algorithm Key Pairs
[kty(7)]
[
RFC-ietf-cose-dilithium-10
]
COSE Elliptic Curves
Expert(s)
Göran Selander, Derek Atkins, Sean Turner
Reference
[
RFC9053
]
Available Formats
CSV
Range
Registration Procedures
Integers less than -65536
Private Use
Integer values -65536 to -257
Specification Required
Integer values -256 to 255
Standards Action With Expert Review
Integer values 256 to 65535
Specification Required
Integer values greater than 65535
Expert Review
Name
Value
Key Type
Description
Change Controller
Reference
Recommended
Reserved for Private Use
Integer values less than -65536
[
RFC9053
]
No
Unassigned
-65536 to -1
Reserved
0
[
RFC9053
]
No
P-256
1
EC2
NIST P-256 also known as secp256r1
[
RFC9053
]
Yes
P-384
2
EC2
NIST P-384 also known as secp384r1
[
RFC9053
]
Yes
P-521
3
EC2
NIST P-521 also known as secp521r1
[
RFC9053
]
Yes
X25519
4
OKP
X25519 for use w/ ECDH only
[
RFC9053
]
Yes
X448
5
OKP
X448 for use w/ ECDH only
[
RFC9053
]
Yes
Ed25519
6
OKP
Ed25519 for use w/ EdDSA only
[
RFC9053
]
Yes
Ed448
7
OKP
Ed448 for use w/ EdDSA only
[
RFC9053
]
Yes
secp256k1
8
EC2
SECG secp256k1 curve
IESG
[
RFC8812
]
No
Unassigned
9-255
brainpoolP256r1
256
EC2
BrainpoolP256r1
[
ISO/IEC JTC 1/SC 17/WG 10
]
[
ISO/IEC 18013-5:2021, 9.1.5.2
]
No
brainpoolP320r1
257
EC2
BrainpoolP320r1
[
ISO/IEC JTC 1/SC 17/WG 10
]
[
ISO/IEC 18013-5:2021, 9.1.5.2
]
No
brainpoolP384r1
258
EC2
BrainpoolP384r1
[
ISO/IEC JTC 1/SC 17/WG 10
]
[
ISO/IEC 18013-5:2021, 9.1.5.2
]
No
brainpoolP512r1
259
EC2
BrainpoolP512r1
[
ISO/IEC JTC 1/SC 17/WG 10
]
[
ISO/IEC 18013-5:2021, 9.1.5.2
]
No
COSE Verifiable Data Structure Algorithms
Registration Procedure(s)
Specification Required
Expert(s)
Mike Jones, Orie Steele
Reference
[
RFC-ietf-cose-merkle-tree-proofs-18
]
Available Formats
CSV
Name
Value
Description
Change Controller
Reference
Reserved
0
Reserved
[
RFC-ietf-cose-merkle-tree-proofs-18
]
RFC9162_SHA256
1
SHA256 Binary Merkle Tree
IETF
[
RFC9162, Section 2.1
]
COSE Verifiable Data Structure Proofs
Registration Procedure(s)
Specification Required
Expert(s)
Mike Jones, Orie Steele
Reference
[
RFC-ietf-cose-merkle-tree-proofs-18
]
Available Formats
CSV
Verifiable Data Structure
Name
Label
CBOR Type
Description
Change Controller
Reference
1
inclusion proofs
-1
array (of bstr)
Proof of inclusion
IETF
[
RFC-ietf-cose-merkle-tree-proofs-18, Section 5.2
]
1
consistency proofs
-2
array (of bstr)
Proof of append only property
IETF
[
RFC-ietf-cose-merkle-tree-proofs-18, Section 5.3
]