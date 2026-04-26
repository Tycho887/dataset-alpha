# RFC 7516: JSON Web Encryption (JWE)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7516

## Scope (Summary)
Defines a compact, URL-safe JSON-based data structure (JWE) for representing encrypted and integrity-protected content. Two serializations are specified: a compact serialization for constrained environments and a JSON serialization supporting encryption to multiple recipients. Cryptographic algorithms and identifiers are defined in the companion JSON Web Algorithms (JWA) specification; digital signature and MAC capabilities are in JSON Web Signature (JWS).

## Normative References
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, DOI 10.17487/RFC7518, May 2015.
- [JWS] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, DOI 10.17487/RFC7515, May 2015.
- [JWK] Jones, M., "JSON Web Key (JWK)", RFC 7517, DOI 10.17487/RFC7517, May 2015.
- [RFC1951] Deutsch, P., "DEFLATE Compressed Data Format Specification version 1.3", RFC 1951, DOI 10.17487/RFC1951, May 1996.
- [RFC20] Cerf, V., "ASCII format for Network Interchange", STD 80, RFC 20, DOI 10.17487/RFC0020, October 1969.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, DOI 10.17487/RFC3629, November 2003.
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", FYI 36, RFC 4949, DOI 10.17487/RFC4949, August 2007.
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, DOI 10.17487/RFC5280, May 2008.
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, DOI 10.17487/RFC7159, March 2014.
- [UNICODE] The Unicode Consortium, "The Unicode Standard", <http://www.unicode.org/versions/latest/>.

## Definitions and Abbreviations
- **JSON Web Encryption (JWE)**: A data structure representing an encrypted and integrity-protected message.
- **Authenticated Encryption with Associated Data (AEAD)**: An algorithm that encrypts plaintext, allows Additional Authenticated Data, and provides integrated integrity check over ciphertext and AAD.
- **Additional Authenticated Data (AAD)**: Input to AEAD that is integrity protected but not encrypted.
- **Authentication Tag**: Output of AEAD ensuring integrity of ciphertext and AAD; empty octet sequence for algorithms not using a tag.
- **Content Encryption Key (CEK)**: Symmetric key for AEAD used to encrypt plaintext.
- **JWE Encrypted Key**: Encrypted CEK value; empty octet sequence for some algorithms.
- **JWE Initialization Vector**: IV used when encrypting plaintext; empty octet sequence for algorithms not using an IV.
- **JWE AAD**: Additional value integrity protected by authenticated encryption; only present in JWE JSON Serialization.
- **JWE Ciphertext**: Ciphertext resulting from authenticated encryption.
- **JWE Authentication Tag**: Authentication tag resulting from authenticated encryption.
- **JWE Protected Header**: JSON object containing Header Parameters integrity protected by the authenticated encryption operation; applies to all recipients.
- **JWE Shared Unprotected Header**: JSON object containing Header Parameters applying to all recipients that are not integrity protected; only for JWE JSON Serialization.
- **JWE Per-Recipient Unprotected Header**: JSON object containing Header Parameters applying to a single recipient, not integrity protected; only for JWE JSON Serialization.
- **JWE Compact Serialization**: Compact, URL-safe string representation.
- **JWE JSON Serialization**: JSON object representation enabling encryption to multiple parties; not optimized for compactness or URL safety.
- **Key Management Mode**: Method for determining CEK value. Modes: Key Encryption, Key Wrapping, Direct Key Agreement, Key Agreement with Key Wrapping, Direct Encryption.
- Additional terms from JWS: "JSON Web Signature (JWS)", "Base64url Encoding", "Collision-Resistant Name", "Header Parameter", "JOSE Header", "StringOrURI".
- Additional terms from RFC 4949: "Ciphertext", "Digital Signature", "Initialization Vector (IV)", "Message Authentication Code (MAC)", "Plaintext".

### Notational Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119 when in all capital letters.
- BASE64URL(OCTETS): base64url encoding per Section 2 of JWS.
- UTF8(STRING): octets of UTF-8 representation (RFC 3629).
- ASCII(STRING): octets of ASCII representation (RFC 20).
- Concatenation of A and B: A || B.

## JWE Overview (Section 3)
JWE uses JSON data structures and base64url encoding. It represents: JOSE Header, JWE Encrypted Key, JWE Initialization Vector, JWE AAD, JWE Ciphertext, JWE Authentication Tag. JOSE Header members are union of JWE Protected Header, JWE Shared Unprotected Header, JWE Per-Recipient Unprotected Header. JWE uses authenticated encryption for confidentiality/integrity of plaintext and integrity of JWE Protected Header and JWE AAD.

### JWE Compact Serialization Overview (3.1)
No JWE Shared Unprotected Header or JWE Per-Recipient Unprotected Header are used. Representation: `BASE64URL(UTF8(JWE Protected Header)) || '.' || BASE64URL(JWE Encrypted Key) || '.' || BASE64URL(JWE Initialization Vector) || '.' || BASE64URL(JWE Ciphertext) || '.' || BASE64URL(JWE Authentication Tag)`.

### JWE JSON Serialization Overview (3.2)
At least one of JWE Protected Header, JWE Shared Unprotected Header, JWE Per-Recipient Unprotected Header MUST be present. JOSE Header is union of all present. JSON object members: "protected", "unprotected", "header", "encrypted_key", "iv", "ciphertext", "tag", "aad". Some members OPTIONAL.

## JOSE Header (Section 4)
Members of JSON object(s) describing encryption and optional properties. Header Parameter names in JOSE Header MUST be unique. Rules for handling unknown parameters same as JWS. Classes of Header Parameter names same as JWS.

### Registered Header Parameter Names (4.1)
Parameters registered in IANA "JSON Web Signature and Encryption Header Parameters" registry.

#### 4.1.1 "alg" (Algorithm) Header Parameter
Same meaning, syntax, processing rules as "alg" in JWS Section 4.1.1, except identifies algorithm used to encrypt/determine CEK. Encrypted content not usable if "alg" value is not supported or recipient lacks matching key. Defined "alg" values in IANA "JSON Web Signature and Encryption Algorithms" registry (JWA Section 4.1).

#### 4.1.2 "enc" (Encryption Algorithm) Header Parameter
Identifies content encryption algorithm used for authenticated encryption. Algorithm MUST be AEAD with specified key length. Encrypted content not usable if unsupported. "enc" values should be registered or be a Collision-Resistant Name. Case-sensitive ASCII StringOrURI. This Header Parameter MUST be present and MUST be understood and processed by implementations.

#### 4.1.3 "zip" (Compression Algorithm) Header Parameter
Compression algorithm applied to plaintext before encryption. Defined value: "DEF" (DEFLATE, RFC 1951). Other values MAY be used. "zip" is case-sensitive string. If absent, no compression. When used, MUST be integrity protected; therefore MUST occur only within JWE Protected Header. OPTIONAL. MUST be understood and processed by implementations.

#### 4.1.4 "jku" (JWK Set URL) Header Parameter
Same meaning, syntax, processing rules as "jku" in JWS Section 4.1.2, except JWK Set resource contains public key to which JWE was encrypted.

#### 4.1.5 "jwk" (JSON Web Key) Header Parameter
Same meaning, syntax, processing rules as "jwk" in JWS Section 4.1.3, except key is public key to which JWE was encrypted.

#### 4.1.6 "kid" (Key ID) Header Parameter
Same meaning, syntax, processing rules as "kid" in JWS Section 4.1.4, except key hint references public key to which JWE was encrypted.

#### 4.1.7 "x5u" (X.509 URL) Header Parameter
Same meaning, syntax, processing rules as "x5u" in JWS Section 4.1.5, except X.509 certificate chain contains public key to which JWE was encrypted.

#### 4.1.8 "x5c" (X.509 Certificate Chain) Header Parameter
Same meaning, syntax, processing rules as "x5c" in JWS Section 4.1.6, except X.509 certificate chain contains public key to which JWE was encrypted. See JWS Appendix B for example.

#### 4.1.9 "x5t" (X.509 Certificate SHA-1 Thumbprint) Header Parameter
Same meaning, syntax, processing rules as "x5t" in JWS Section 4.1.7, except certificate referenced by thumbprint contains public key to which JWE was encrypted.

#### 4.1.10 "x5t#S256" (X.509 Certificate SHA-256 Thumbprint) Header Parameter
Same meaning, syntax, processing rules as "x5t#S256" in JWS Section 4.1.8, except certificate referenced by thumbprint contains public key to which JWE was encrypted.

#### 4.1.11 "typ" (Type) Header Parameter
Same meaning, syntax, processing rules as "typ" in JWS Section 4.1.9, except type is that of complete JWE.

#### 4.1.12 "cty" (Content Type) Header Parameter
Same meaning, syntax, processing rules as "cty" in JWS Section 4.1.10, except type is that of secured content (plaintext).

#### 4.1.13 "crit" (Critical) Header Parameter
Same meaning, syntax, processing rules as "crit" in JWS Section 4.1.11, except refers to JWE Header Parameters.

### Public Header Parameter Names (4.2)
New Header Parameters should be registered in IANA registry or be a Public Name (Collision-Resistant Name). Should be introduced sparingly to avoid non-interoperability.

### Private Header Parameter Names (4.3)
May use Private Names agreed by producer and consumer; subject to collision and should be used with caution.

## Producing and Consuming JWEs (Section 5)

### Message Encryption (5.1)
Process:
1. Determine Key Management Mode from "alg".
2. When Key Wrapping, Key Encryption, or Key Agreement with Key Wrapping: generate random CEK (RFC 4086). CEK MUST have length required for content encryption algorithm.
3. When Direct Key Agreement or Key Agreement with Key Wrapping: compute agreed upon key. For Direct Key Agreement: CEK = agreed key. For Key Agreement with Key Wrapping: agreed key used to wrap CEK.
4. When Key Wrapping, Key Encryption, or Key Agreement with Key Wrapping: encrypt CEK to recipient; result = JWE Encrypted Key.
5. When Direct Key Agreement or Direct Encryption: JWE Encrypted Key = empty octet sequence.
6. When Direct Encryption: CEK = shared symmetric key.
7. Compute encoded key value BASE64URL(JWE Encrypted Key).
8. If JWE JSON Serialization: repeat steps 1-7 for each recipient.
9. Generate random JWE Initialization Vector of correct size (or empty octet sequence if algorithm doesn't require).
10. Compute encoded IV.
11. If "zip" present: compress plaintext; otherwise M = plaintext.
12. Create JOSE Header JSON objects (JWE Protected Header, JWE Shared Unprotected Header, JWE Per-Recipient Unprotected Header).
13. Compute Encoded Protected Header: BASE64URL(UTF8(JWE Protected Header)); if absent (JWE JSON only) empty string.
14. Additional Authenticated Data = ASCII(Encoded Protected Header). If JWE AAD present: ASCII(Encoded Protected Header || '.' || BASE64URL(JWE AAD)).
15. Encrypt M using CEK, IV, AAD to produce JWE Ciphertext and JWE Authentication Tag.
16. Compute encoded ciphertext.
17. Compute encoded Authentication Tag.
18. If JWE AAD present, compute encoded AAD.
19. Create serialized output.

### Message Decryption (5.2)
Process:
1. Parse JWE representation.
2. Base64url decode components.
3. Verify decoded JWE Protected Header is valid UTF-8 JSON object (RFC 7159).
4. For JWE Compact: JOSE Header = JWE Protected Header. For JWE JSON: JOSE Header = union of members from JWE Protected Header, JWE Shared Unprotected Header, JWE Per-Recipient Unprotected Header; verify no duplicate Header Parameter names.
5. Verify implementation understands all required fields (including "crit").
6. Determine Key Management Mode from "alg".
7. Verify key is known to recipient.
8. For Direct Key Agreement or Key Agreement with Key Wrapping: compute agreed upon key; for Direct Key Agreement: CEK = agreed key; for Key Agreement with Key Wrapping: agreed key used to decrypt JWE Encrypted Key.
9. For Key Wrapping, Key Encryption, or Key Agreement with Key Wrapping: decrypt JWE Encrypted Key to produce CEK. CEK MUST have required length.
10. For Direct Key Agreement or Direct Encryption: verify JWE Encrypted Key is empty octet sequence.
11. For Direct Encryption: CEK = shared symmetric key.
12. Record whether CEK could be successfully determined.
13. If JWE JSON Serialization: repeat steps 4-12 for each recipient.
14. Compute Encoded Protected Header.
15. Compute Additional Authenticated Data as in encryption.
16. Decrypt JWE Ciphertext using CEK, IV, AAD, JWE Authentication Tag; reject if Authentication Tag is incorrect.
17. If "zip" present, uncompress plaintext.
18. If no recipient succeeded, JWE MUST be considered invalid; otherwise output plaintext.

### String Comparison Rules (5.3)
Same as JWS Section 5.3.

## Key Identification (Section 6)
Same as JWS Section 6, except key identified is public key to which JWE was encrypted.

## Serializations (Section 7)
Two serializations: JWE Compact Serialization and JWE JSON Serialization. Applications specify which serialization and features are used.

### JWE Compact Serialization (7.1)
Only one recipient. Syntax: `BASE64URL(UTF8(JWE Protected Header)) || '.' || BASE64URL(JWE Encrypted Key) || '.' || BASE64URL(JWE Initialization Vector) || '.' || BASE64URL(JWE Ciphertext) || '.' || BASE64URL(JWE Authentication Tag)`.

### JWE JSON Serialization (7.2)

#### General JWE JSON Serialization Syntax (7.2.1)
JSON object members:
- "protected": MUST be present with non-empty value, otherwise absent.
- "unprotected": MUST be present with non-empty value, otherwise absent.
- "iv": MUST be present with non-empty value, otherwise absent.
- "aad": MUST be present with non-empty value, otherwise absent.
- "ciphertext": MUST be present.
- "tag": MUST be present with non-empty value, otherwise absent.
- "recipients": MUST be present, array of JSON objects (one per recipient). Each recipient object may have "header" and "encrypted_key" members (MUST be present if non-empty). At least one of "header", "protected", "unprotected" MUST be present. Header Parameter names across these three locations MUST be disjoint. All recipients share same JWE Protected Header, IV, ciphertext, and Authentication Tag. The "enc" value MUST be same for all recipients.

#### Flattened JWE JSON Serialization Syntax (7.2.2)
Optimized for single recipient. No "recipients" member; "header" and "encrypted_key" members at top level. Otherwise identical.

## TLS Requirements (Section 8)
Same as JWS Section 8.

## Distinguishing between JWS and JWE Objects (Section 9)
- Compact: JWS has 3 segments (2 periods), JWE has 5 segments (4 periods).
- JSON: JWS has "payload" member, JWE has "ciphertext" member.
- JOSE Header: check "alg" (JWS: signature/MAC/none; JWE: Key Encryption/Key Wrapping etc.) or presence of "enc" (JWE has "enc").

## IANA Considerations (Section 10)
### JSON Web Signature and Encryption Header Parameters Registration (10.1)
Registers "alg", "enc", "zip", "jku", "jwk", "kid", "x5u", "x5c", "x5t", "x5t#S256", "typ", "cty", "crit" as JWE Header Parameters with details per Section 4.1.

## Security Considerations (Section 11)
- All security issues from JWS and XML Encryption 1.1 (except XML-specific) apply.
- Key Entropy and Random Values: see JWS Section 10.1; random values used for CEKs and IVs.
- Key Protection: see JWS Section 10.2; protect key encryption key and CEK.
- Using Matching Algorithm Strengths: algorithms of matching strengths should be used together; effective security determined by weaker algorithm.
- Adaptive Chosen-Ciphertext Attacks: do not allow recipient to be used as oracle; report all formatting errors as single error; restrict key to limited set of algorithms.
- Timing Attacks: MUST NOT distinguish between format, padding, length errors of encrypted keys; strongly recommended to substitute randomly generated CEK on improper key formatting.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The "enc" Header Parameter MUST be present and MUST be understood and processed by implementations. | shall | Section 4.1.2 |
| R2 | When used, the "zip" Header Parameter MUST be integrity protected; therefore it MUST occur only within the JWE Protected Header. | shall | Section 4.1.3 |
| R3 | The "zip" Header Parameter MUST be understood and processed by implementations. | shall | Section 4.1.3 |
| R4 | The CEK MUST have a length equal to that required for the content encryption algorithm. | shall | Section 5.1 step 2, Section 5.2 step 9 |
| R5 | For recipients using Direct Key Agreement or Direct Encryption, the JWE Encrypted Key MUST be the empty octet sequence. | shall | Sections 5.1 step 5, 5.2 step 10 |
| R6 | When decrypting, if the JWE Authentication Tag is incorrect, the input MUST be rejected without emitting any decrypted output. | shall | Section 5.2 step 16 |
| R7 | If no recipient succeeded in all decryption steps, the JWE MUST be considered invalid. | shall | Section 5.2 step 18 |
| R8 | The "protected" member MUST be present (with non-empty value) when the JWE Protected Header value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R9 | The "unprotected" member MUST be present (with non-empty value) when the JWE Shared Unprotected Header value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R10 | The "iv" member MUST be present (with non-empty value) when the JWE Initialization Vector value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R11 | The "aad" member MUST be present (with non-empty value) when the JWE AAD value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R12 | The "ciphertext" member MUST be present. | shall | Section 7.2.1 |
| R13 | The "tag" member MUST be present (with non-empty value) when the JWE Authentication Tag value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R14 | The "recipients" member MUST be present with exactly one array element per recipient. | shall | Section 7.2.1 |
| R15 | The "header" member MUST be present (with non-empty value) when the JWE Per-Recipient Unprotected Header value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R16 | The "encrypted_key" member MUST be present (with non-empty value) when the JWE Encrypted Key value is non-empty; otherwise it MUST be absent. | shall | Section 7.2.1 |
| R17 | At least one of "header", "protected", and "unprotected" MUST be present. | shall | Section 7.2.1 |
| R18 | Header Parameter names in the three locations (protected, unprotected, header) MUST be disjoint. | shall | Section 7.2.1 |
| R19 | The "recipients" member MUST NOT be present when using the flattened JWE JSON Serialization. | shall | Section 7.2.2 |
| R20 | When decrypting, the recipient MUST NOT distinguish between format, padding, and length errors of encrypted keys. | shall | Section 11.5 |
| R21 | It is strongly recommended that on receiving an improperly formatted key, the recipient substitute a randomly generated CEK and proceed to next step to mitigate timing attacks. | RECOMMENDED | Section 11.5 |
| R22 | Even if a JWE can be successfully decrypted, unless the algorithms used are acceptable to the application, it SHOULD consider the JWE to be invalid. | SHOULD | Section 5.2 (final note) |
| R23 | Additional members in JSON objects not understood by implementations MUST be ignored. | shall | Section 7.2.1 |

## Informative Annexes (Condensed)

- **Appendix A: JWE Examples** – Provides full worked examples for different key management modes and content encryption algorithms, including RSAES-OAEP + AES GCM, RSAES-PKCS1-v1_5 + AES_128_CBC_HMAC_SHA_256, AES Key Wrap + AES_128_CBC_HMAC_SHA_256, and the general and flattened JWE JSON Serialization. Each example details the JOSE Header, CEK generation, key encryption, IV, AAD, content encryption, and final representation, with validation notes.
- **Appendix B: Example AES_128_CBC_HMAC_SHA_256 Computation** – Walks through the steps of extracting MAC_KEY and ENC_KEY from the CEK, encrypting plaintext with AES-128-CBC, forming the AAD length in 64-bit big-endian, creating HMAC input, computing HMAC SHA-256, and truncating to produce the Authentication Tag.