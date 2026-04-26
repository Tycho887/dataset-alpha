# RFC 7517: JSON Web Key (JWK)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc7517

## Scope (Summary)
Defines the JSON Web Key (JWK) data structure for representing cryptographic keys in JSON, and the JWK Set data structure for sets of JWKs. Cryptographic algorithm identifiers are specified separately in JSON Web Algorithms (JWA) [RFC 7518] and associated IANA registries.

## Normative References
- [ECMAScript] Ecma International, "ECMAScript Language Specification, 5.1 Edition", ECMA Standard 262, June 2011
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015
- [JWE] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, May 2015
- [JWS] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015
- [RFC20] Cerf, V., "ASCII format for Network Interchange", STD 80, RFC 20, October 1969
- [RFC2046] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003
- [RFC3986] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, October 2006
- [RFC4945] Korver, B., "The Internet IP Security PKI Profile of IKEv1/ISAKMP, IKEv2, and PKIX", RFC 4945, August 2007
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", FYI 36, RFC 4949, August 2007
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, March 2014
- [UNICODE] The Unicode Consortium, "The Unicode Standard"
- [ITU.X690.1994] ITU-T Recommendation X.690, "Information Technology - ASN.1 encoding rules", 1994

## Definitions and Abbreviations
- **JSON Web Key (JWK)**: A JSON object that represents a cryptographic key. Members represent key properties, including its value.
- **JWK Set**: A JSON object that MUST have a "keys" member, which is an array of JWKs.
- **Base64url Encoding**: As defined in Section 2 of [JWS].
- **UTF8(STRING)**: Octets of the UTF-8 representation of STRING.
- **ASCII(STRING)**: Octets of the ASCII representation of STRING.
- **Collision-Resistant Name**: Defined in [JWS].
- **Header Parameter**, **JOSE Header**: Defined in [JWS].
- **JWE**, **Additional Authenticated Data (AAD)**, **JWE Authentication Tag**, **JWE Ciphertext**, **JWE Compact Serialization**, **JWE Encrypted Key**, **JWE Initialization Vector**, **JWE Protected Header**: Defined in [JWE].

## 1. Introduction
A JWK is a JSON data structure representing a cryptographic key. This specification also defines a JWK Set for a set of JWKs. Algorithm identifiers are described in [JWA]. Goals do not include representing new certificate chains or replacing X.509 certificates. JWKs and JWK Sets are used in JWS and JWE.

### 1.1. Notational Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC2119] when in all capitals.
- BASE64URL(OCTETS) denotes base64url encoding per Section 2 of [JWS].
- UTF8(STRING) denotes octets of UTF-8 representation.
- ASCII(STRING) denotes octets of ASCII representation.
- Concatenation of A and B is denoted as A || B.

## 2. Terminology
(Definitions as listed above in "Definitions and Abbreviations".)

## 3. Example JWK
(Provides an example Elliptic Curve key. Informative.)

## 4. JSON Web Key (JWK) Format
A JWK is a JSON object representing a cryptographic key. The JSON object MAY contain whitespace/line breaks per [RFC7159]. This section defines common parameters; key-type specific parameters are in [JWA].

- **Member name uniqueness**: Member names within a JWK MUST be unique. JWK parsers MUST reject duplicates or use a JSON parser that returns only the lexically last duplicate member name (as per [ECMAScript] Section 15.12).
- **Unknown members**: Additional members not understood by implementations MUST be ignored.
- **New member names**: Should either be registered in the IANA "JSON Web Key Parameters" registry (Section 8.1) or be a Collision-Resistant Name.

### 4.1. "kty" (Key Type) Parameter
- **Requirement**: The "kty" member MUST be present in a JWK.
- **Value**: Identifies the cryptographic algorithm family (e.g., "RSA", "EC"). Case-sensitive string.
- **Registration**: Values should be registered in the IANA "JSON Web Key Types" registry [JWA] or be a Collision-Resistant Name.
- **Key type definitions** include specification of members for those key types.

### 4.2. "use" (Public Key Use) Parameter
- **Purpose**: Identifies intended use of the public key: "sig" (signature) or "enc" (encryption). "enc" also used for key wrapping and key agreement.
- **Requirement**: Use of "use" is OPTIONAL, unless the application requires its presence.
- **Additional values**: May be registered in the "JSON Web Key Use" registry (Section 8.2). Unregistered extensions can be used in closed environments.

### 4.3. "key_ops" (Key Operations) Parameter
- **Value**: Array of key operation values (case-sensitive strings). Defined values: "sign", "verify", "encrypt", "decrypt", "wrapKey", "unwrapKey", "deriveKey", "deriveBits".
- **Duplicate values**: MUST NOT be present.
- **Requirement**: Use of "key_ops" is OPTIONAL, unless the application requires its presence.
- **Restrictions**: Multiple unrelated key operations SHOULD NOT be specified. Permitted combinations: "sign" with "verify", "encrypt" with "decrypt", "wrapKey" with "unwrapKey". Other combinations SHOULD NOT be used.
- **"use" and "key_ops"**: SHOULD NOT be used together; if both present, they MUST be consistent.

### 4.4. "alg" (Algorithm) Parameter
- **Value**: Case-sensitive ASCII string identifying the algorithm intended for use with the key.
- **Registration**: Should be registered in the "JSON Web Signature and Encryption Algorithms" registry [JWA] or be a Collision-Resistant Name.
- **Requirement**: Use is OPTIONAL.

### 4.5. "kid" (Key ID) Parameter
- **Purpose**: Used to match a specific key, e.g., for key rollover.
- **Uniqueness**: Within a JWK Set, different keys SHOULD use distinct "kid" values (except when equivalent alternatives).
- **Value**: Case-sensitive string.
- **Requirement**: Use is OPTIONAL. When used with JWS/JWE, matches the "kid" Header Parameter.

### 4.6. "x5u" (X.509 URL) Parameter
- **Value**: URI referring to an X.509 public key certificate or certificate chain [RFC5280] in PEM form.
- **Requirement**: The identified resource MUST provide the certificate in PEM form. The key in the first certificate MUST match the public key represented by other members. The protocol MUST provide integrity protection; HTTP GET MUST use TLS; server identity MUST be validated per [RFC6125].
- **Consistency**: If other members (e.g., "use", "alg") are present, they MUST be semantically consistent with the first certificate.
- **Requirement**: Use is OPTIONAL.

### 4.7. "x5c" (X.509 Certificate Chain) Parameter
- **Value**: JSON array of base64-encoded (not base64url) DER PKIX certificates. The first certificate contains the key; subsequent certificates certify the previous one.
- **Requirement**: The key in the first certificate MUST match the public key represented by other members.
- **Consistency**: If other members are present, they MUST be semantically consistent with the first certificate.
- **Requirement**: Use is OPTIONAL.

### 4.8. "x5t" (X.509 Certificate SHA-1 Thumbprint) Parameter
- **Value**: base64url-encoded SHA-1 thumbprint of the DER encoding of an X.509 certificate.
- **Requirement**: The key in the certificate MUST match the public key represented by other members.
- **Consistency**: If other members are present, they MUST be semantically consistent with the referenced certificate.
- **Requirement**: Use is OPTIONAL.

### 4.9. "x5t#S256" (X.509 Certificate SHA-256 Thumbprint) Parameter
- **Value**: base64url-encoded SHA-256 thumbprint of the DER encoding of an X.509 certificate.
- **Requirement**: The key in the certificate MUST match the public key represented by other members.
- **Consistency**: Same as x5t; other members MUST be semantically consistent.
- **Requirement**: Use is OPTIONAL.

## 5. JWK Set Format
A JWK Set is a JSON object that MUST have a "keys" member, whose value is an array of JWKs. The JSON object MAY contain whitespace/line breaks.

- **Member name uniqueness**: Same as JWK (MUST be unique; parsers MUST reject or take last duplicate).
- **Unknown members**: MUST be ignored.
- **New JWK Set parameters**: Should be registered in the "JSON Web Key Set Parameters" registry (Section 8.4) or be a Collision-Resistant Name.
- **Ignoring unrecognized JWKs**: Implementations SHOULD ignore JWKs with unknown "kty" values, missing required members, or out-of-range values.

### 5.1. "keys" Parameter
- **Value**: Array of JWK values. The order of JWKs does not imply preference by default; applications may assign meaning.

## 6. String Comparison Rules
Same as Section 5.3 of [JWS].

## 7. Encrypted JWK and Encrypted JWK Set Formats
- **Requirement**: Access to non-public key material MUST be prevented. Encryption recommended.
- **Encrypted JWK**: JWE with the UTF-8 encoding of a JWK as plaintext. The "cty" (content type) Header Parameter value MUST be "jwk+json" unless the application knows the content is a JWK by other means.
- **Encrypted JWK Set**: JWE with the UTF-8 encoding of a JWK Set as plaintext. The "cty" value MUST be "jwk-set+json" unless otherwise known.

## 8. IANA Considerations (Summarized)
Registries established with Specification Required [RFC5226] after three-week review on jose-reg-review@ietf.org.

### 8.1. JSON Web Key Parameters Registry
Records parameter name, key type(s), and information class (Public/Private). Initial entries include: "kty", "use", "key_ops", "alg", "kid", "x5u", "x5c", "x5t", "x5t#S256". All are Public, used with "*" key types. Change Controller: IESG.

### 8.2. JSON Web Key Use Registry
Records use member values. Initial: "sig" (Digital Signature or MAC), "enc" (Encryption).

### 8.3. JSON Web Key Operations Registry
Records key operation values. Initial: "sign", "verify", "encrypt", "decrypt", "wrapKey", "unwrapKey", "deriveKey", "deriveBits".

### 8.4. JSON Web Key Set Parameters Registry
Records JWK Set parameter names. Initial: "keys" (Array of JWK Values).

### 8.5. Media Type Registration
Registers "application/jwk+json" and "application/jwk-set+json". Encoding considerations: 8bit, JSON object, UTF-8 SHOULD be employed.

## 9. Security Considerations (Summary)
- **Key Provenance and Trust**: Trust in key should be based on trusted attributes (e.g., via PKIX certificates or JWT). See Section 10.3 of [JWS].
- **Preventing Disclosure**: Private and symmetric keys MUST be protected. Encryption of JWKs/JWK Sets using JWE is recommended.
- **RSA Private Key Representations**: To enable blinding, should include "e". Representations lacking "e" should be avoided.
- **Key Entropy and Random Values**: See Section 10.1 of [JWS].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Member names within a JWK MUST be unique; parsers MUST reject duplicates or use JSON parser returning last duplicate. | MUST | Section 4 |
| R2 | Unknown JWK/JWK Set members MUST be ignored. | MUST | Sections 4, 5 |
| R3 | The "kty" member MUST be present in a JWK. | MUST | Section 4.1 |
| R4 | The "use" member is OPTIONAL unless required by application. | OPTIONAL | Section 4.2 |
| R5 | The "key_ops" member value MUST be an array of strings; duplicate values MUST NOT be present. | MUST | Section 4.3 |
| R6 | The "use" and "key_ops" members SHOULD NOT be used together; if both present, they MUST be consistent. | SHOULD/MUST | Section 4.3 |
| R7 | The "x5u" resource MUST provide PEM-encoded certificate; retrieval MUST use TLS with server identity validation. | MUST | Section 4.6 |
| R8 | The first certificate in "x5c" MUST match the public key in other JWK members. | MUST | Section 4.7 |
| R9 | The key in the certificate referenced by "x5t" or "x5t#S256" MUST match the public key in other JWK members. | MUST | Sections 4.8, 4.9 |
| R10 | A JWK Set MUST have a "keys" member whose value is an array of JWKs. | MUST | Section 5 |
| R11 | Implementations SHOULD ignore JWKs with unknown "kty" values, missing required members, or out-of-range values. | SHOULD | Section 5 |
| R12 | Encrypted JWK: "cty" value MUST be "jwk+json" unless otherwise known. | MUST | Section 7 |
| R13 | Encrypted JWK Set: "cty" value MUST be "jwk-set+json" unless otherwise known. | MUST | Section 7 |

## Informative Annexes (Condensed)
- **Appendix A: Example JSON Web Key Sets**: Provides examples of public keys (EC, RSA), private keys (EC, RSA), and symmetric keys (AES Key Wrap, HMAC) in JWK Set format.
- **Appendix B: Example Use of "x5c" Parameter**: Shows a JWK with an RSA signing key represented both as an RSA public key and an X.509 certificate chain using "x5c".
- **Appendix C: Example Encrypted RSA Private Key**: Walks through the encryption of an RSA private key using PBES2-HS256+A128KW key encryption and A128CBC-HS256 content encryption, producing a JWE Compact Serialization output.