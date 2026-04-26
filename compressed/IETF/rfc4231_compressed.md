# RFC 4231: Identifiers and Test Vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: December 2005 | **Type**: Normative
**Original**: RFC 4231

## Scope
This document provides test vectors for HMAC-SHA-224, HMAC-SHA-256, HMAC-SHA-384, and HMAC-SHA-512 message authentication schemes. It also provides ASN.1 object identifiers and URIs for use in protocols such as those based on S/MIME [4] or XML Digital Signatures [5].

## Normative References
- [1] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [2] National Institute of Standards and Technology, "Secure Hash Standard", FIPS 180-2, August 2002, with Change Notice 1 dated February 2004.
- [3] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **HMAC-SHA-224/256/384/512**: Realization of the HMAC message authentication code [1] using the respective SHA-2 hash function (SHA-224, SHA-256, SHA-384, SHA-512) as described in [2].
- **Key words**: The key word "SHOULD" in this document is to be interpreted as described in RFC 2119 [3].

## 2. Conventions Used in This Document
- The key word "SHOULD" in this document is to be interpreted as described in RFC 2119 [3].

## 3. Scheme Identifiers

### 3.1. ASN.1 Object Identifiers
- The following ASN.1 object identifiers have been allocated for these schemes:
  - `rsadsi OBJECT IDENTIFIER ::= {iso(1) member-body(2) us(840) rsadsi(113549)}`
  - `digestAlgorithm OBJECT IDENTIFIER ::= {rsadsi 2}`
  - `id-hmacWithSHA224 OBJECT IDENTIFIER ::= {digestAlgorithm 8}`
  - `id-hmacWithSHA256 OBJECT IDENTIFIER ::= {digestAlgorithm 9}`
  - `id-hmacWithSHA384 OBJECT IDENTIFIER ::= {digestAlgorithm 10}`
  - `id-hmacWithSHA512 OBJECT IDENTIFIER ::= {digestAlgorithm 11}`
- **Normative requirement**: When the "algorithm" component in a value of ASN.1 type AlgorithmIdentifier identifies one of these schemes, the "parameter" component SHOULD be present but have type NULL.

### 3.2. Algorithm URIs
- The following URIs have been allocated:
  - `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5#hmac-sha-224`
  - `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5#hmac-sha-256`
  - `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5#hmac-sha-384`
  - `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5#hmac-sha-512`
- Informative note: When used in the context of [5], the `<ds:HMACOutputLength>` element may specify the truncated length of the scheme output.

## 4. Test Vectors

### 4.1. Introduction
The test vectors have been cross-verified by three independent implementations. Keys, data, and digests are provided in hex.

### 4.2. Test Case 1
- **Key** (20 bytes): `0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b0b`
- **Data** ("Hi There"): `4869205468657265`
- **HMAC-SHA-224**: `896fb1128abbdf196832107cd49df33f47b4b1169912ba4f53684b22`
- **HMAC-SHA-256**: `b0344c61d8db38535ca8afceaf0bf12b881dc200c9833da726e9376c2e32cff7`
- **HMAC-SHA-384**: `afd03944d84895626b0825f4ab46907f15f9dadbe4101ec682aa034c7cebc59cfaea9ea9076ede7f4af152e8b2fa9cb6`
- **HMAC-SHA-512**: `87aa7cdea5ef619d4ff0b4241a1d6cb02379f4e2ce4ec2787ad0b30545e17cdedaa833b7d6b8a702038b274eaea3f4e4be9d914eeb61f1702e696c203a126854`

### 4.3. Test Case 2
- **Key** ("Jefe"): `4a656665`
- **Data** ("what do ya want for nothing?"): `7768617420646f2079612077616e7420666f72206e6f7468696e673f`
- **HMAC-SHA-224**: `a30e01098bc6dbbf45690f3a7e9e6d0f8bbea2a39e6148008fd05e44`
- **HMAC-SHA-256**: `5bdcc146bf60754e6a042426089575c75a003f089d2739839dec58b964ec3843`
- **HMAC-SHA-384**: `af45d2e376484031617f78d2b58a6b1b9c7ef464f5a01b47e42ec3736322445e8e2240ca5e69e2c78b3239ecfab21649`
- **HMAC-SHA-512**: `164b7a7bfcf819e2e395fbe73b56e0a387bd64222e831fd610270cd7ea2505549758bf75c05a994a6d034f65f8f0e6fdcaeab1a34d4a6b4b636e070a38bce737`

### 4.4. Test Case 3
- **Key** (20 bytes): `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- **Data** (50 bytes): `dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd`
- **HMAC-SHA-224**: `7fb3cb3588c6c1f6ffa9694d7d6ad2649365b0c1f65d69d1ec8333ea`
- **HMAC-SHA-256**: `773ea91e36800e46854db8ebd09181a72959098b3ef8c122d9635514ced565fe`
- **HMAC-SHA-384**: `88062608d3e6ad8a0aa2ace014c8a86f0aa635d947ac9febe83ef4e55966144b2a5ab39dc13814b94e3ab6e101a34f27`
- **HMAC-SHA-512**: `fa73b0089d56a284efb0f0756c890be9b1b5dbdd8ee81a3655f83e33b2279d39bf3e848279a722c806b485a47e67c807b946a337bee8942674278859e13292fb`

### 4.5. Test Case 4
- **Key** (25 bytes): `0102030405060708090a0b0c0d0e0f10111213141516171819`
- **Data** (50 bytes): `cdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcdcd`
- **HMAC-SHA-224**: `6c11506874013cac6a2abc1bb382627cec6a90d86efc012de7afec5a`
- **HMAC-SHA-256**: `82558a389a443c0ea4cc819899f2083a85f0faa3e578f8077a2e3ff46729665b`
- **HMAC-SHA-384**: `3e8a69b7783c25851933ab6290af6ca77a9981480850009cc5577c6e1f573b4e6801dd23c4a7d679ccf8a386c674cffb`
- **HMAC-SHA-512**: `b0ba465637458c6990e5a8c5f61d4af7e576d97ff94b872de76f8050361ee3dba91ca5c11aa25eb4d679275cc5788063a5f19741120c4f2de2adebeb10a298dd`

### 4.6. Test Case 5 (Truncation to 128 bits)
- **Key** (20 bytes): `0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c`
- **Data** ("Test With Truncation"): `546573742057697468205472756e636174696f6e`
- **HMAC-SHA-224**: `0e2aea68a90c8d37c988bcdb9fca6fa8`
- **HMAC-SHA-256**: `a3b6167473100ee06e0c796c2955552b`
- **HMAC-SHA-384**: `3abf34c3503b2a23a46efc619baef897`
- **HMAC-SHA-512**: `415fad6271580a531d4179bc891d87a6`

### 4.7. Test Case 6 (Key larger than 128 bytes)
- **Key** (131 bytes): `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`
- **Data** ("Test Using Larger Than Block-Size Key - Hash Key First"): `54657374205573696e67204c6172676572205468616e20426c6f636b2d53697a65204b6579202d2048617368204b6579204669727374`
- **HMAC-SHA-224**: `95e9a0db962095adaebe9b2d6f0dbce2d499f112f2d2b7273fa6870e`
- **HMAC-SHA-256**: `60e431591ee0b67f0d8a26aacbf5b77f8e0bc6213728c5140546040f0ee37f54`
- **HMAC-SHA-384**: `4ece084485813e9088d2c63a041bc5b44f9ef1012a2b588f3cd11f05033ac4c60c2ef6ab4030fe8296248df163f44952`
- **HMAC-SHA-512**: `80b24263c7c1a3ebb71493c1dd7be8b49b46d1f41b4aeec1121b013783f8f3526b56d037e05f2598bd0fd2215d6a1e5295e64f73f63f0aec8b915a985d786598`

### 4.8. Test Case 7 (Both key and data larger than 128 bytes)
- **Key** (131 bytes): (same as Test Case 6)
- **Data** (152 bytes): `5468697320697320612074657374207573696e672061206c6172676572207468616e20626c6f636b2d73697a65206b657920616e642061206c6172676572207468616e20626c6f636b2d73697a6520646174612e20546865206b6579206e6565647320746f20626520686173686564206265666f7265206265696e6720757365642062792074686520484d414320616c676f726974686d2e`
- **HMAC-SHA-224**: `3a854166ac5d9f023f54d517d0b39dbd946770db9c2b95c9f6f565d1`
- **HMAC-SHA-256**: `9b09ffa71b942fcb27635fbcd5b0e944bfdc63644f0713938a7f51535c3a35e2`
- **HMAC-SHA-384**: `6617178e941f020d351e2f254e8fd32c602420feb0b8fb9adccebb82461e99c5a678cc31e799176d3860e6110c46523e`
- **HMAC-SHA-512**: `e37b6a775dc87dbaa4dfa9f96e5e3ffddebd71f8867289865df5a32d20cdc944b6022cac3c4982b10d5eeb55c3e4de15134676fb6de0446065c97440fa8c6a58`

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The key word "SHOULD" is to be interpreted as described in RFC 2119. | SHOULD | Section 2, RFC 2119 |
| R2 | When the "algorithm" component in a value of ASN.1 type AlgorithmIdentifier identifies one of these schemes, the "parameter" component SHOULD be present but have type NULL. | SHOULD | Section 3.1 |

## Security Considerations (Condensed)
This document provides identifications and test vectors; no assertion of security for any particular use is intended. The reader is referred to [1] for a discussion of the general security of the HMAC construction.

## Informative References
- [4] Housley, R., "Cryptographic Message Syntax (CMS)", RFC 3852, July 2004.
- [5] Eastlake 3rd, D., Reagle, J., and D. Solo, "(Extensible Markup Language) XML-Signature Syntax and Processing", RFC 3275, March 2002.
- [6] Cheng, P. and R. Glenn, "Test Cases for HMAC-MD5 and HMAC-SHA-1", RFC 2202, September 1997.

## Acknowledgements (Condensed)
Test cases derived from [6]; thanks to Jim Schaad and Brad Hards for assistance in verifying results.