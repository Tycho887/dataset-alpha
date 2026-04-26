# RFC 8725 BCP 225: JSON Web Token Best Current Practices
**Source**: IETF | **Version**: N/A | **Date**: February 2020 | **Type**: Best Current Practice (Normative)
**Updates**: RFC 7519  
**Original**: [https://www.rfc-editor.org/info/rfc8725](https://www.rfc-editor.org/info/rfc8725)

## Scope (Summary)
This document updates RFC 7519 to provide actionable guidance leading to secure implementation and deployment of JSON Web Tokens (JWTs). It covers threats and vulnerabilities, algorithm verification, key management, validation of cryptographic operations and JWT claims, and prevention of substitution and confusion attacks. The recommendations are minimum standards for most use cases; stronger options are always permitted.

## Normative References
- [nist-sp-800-56a-r3] Barker, E., et al., "Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography", NIST SP 800-56A Rev 3, DOI 10.6028/NIST.SP.800-56Ar3, April 2018.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.
- [RFC6979] Pornin, T., "Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA)", RFC 6979, DOI 10.17487/RFC6979, August 2013.
- [RFC7515] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, DOI 10.17487/RFC7515, May 2015.
- [RFC7516] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, DOI 10.17487/RFC7516, May 2015.
- [RFC7518] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, DOI 10.17487/RFC7518, May 2015.
- [RFC7519] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Token (JWT)", RFC 7519, DOI 10.17487/RFC7519, May 2015.
- [RFC8017] Moriarty, K., Ed., et al., "PKCS #1: RSA Cryptography Specifications Version 2.2", RFC 8017, DOI 10.17487/RFC8017, November 2016.
- [RFC8037] Liusvaara, I., "CFRG Elliptic Curve Diffie-Hellman (ECDH) and Signatures in JOSE", RFC 8037, DOI 10.17487/RFC8037, January 2017.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017.
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, DOI 10.17487/RFC8259, December 2017.

## Definitions and Abbreviations
- **JWT**: JSON Web Token as defined in [RFC7519].
- **JWS**: JSON Web Signature as defined in [RFC7515].
- **JWE**: JSON Web Encryption as defined in [RFC7516].
- **JWA**: JSON Web Algorithms as defined in [RFC7518].
- **"alg" Header Parameter**: Indicates the cryptographic algorithm used.
- **"enc" Header Parameter**: Indicates the content encryption algorithm.
- **"typ" Header Parameter**: Used for explicit typing of JWTs.
- **"iss" (issuer) claim**: Identifies the principal that issued the JWT.
- **"sub" (subject) claim**: Identifies the principal that is the subject of the JWT.
- **"aud" (audience) claim**: Identifies the recipients that the JWT is intended for.
- **"kid" (key ID) header**: Used for key lookup.
- **"jku" (JWK Set URL) header**: URL from which to retrieve a key set.
- **"x5u" (X.509 URL) header**: URL from which to retrieve an X.509 certificate.
- **ECDH-ES**: Elliptic Curve Diffie-Hellman Ephemeral Static key agreement.
- **HS256**: HMAC using SHA-256.
- **RS256**: RSA using SHA-256 signature.
- **none**: No cryptographic algorithm.
- **Nested JWT**: A JWT that is itself a JWS or JWE payload.

## Threats and Vulnerabilities (Summary)
Each vulnerability is followed by cross-references to mitigating best practices.

- **2.1 Weak Signatures / Insufficient Validation**: Attackers change "alg" to "none" or from "RS256" to "HS256" using public key as HMAC secret. Mitigated by Sections 3.1, 3.2.
- **2.2 Weak Symmetric Keys**: Low-entropy keys used with HMAC are vulnerable to brute-force. Mitigated by Section 3.5.
- **2.3 Incorrect Composition of Encryption and Signature**: JWE containing JWS may not validate inner signature. Mitigated by Section 3.3.
- **2.4 Plaintext Leakage via Ciphertext Length**: Compression before encryption leaks info. Mitigated by Section 3.6.
- **2.5 Insecure Elliptic Curve Encryption**: Invalid curve points in ECDH-ES may leak private key. Mitigated by Section 3.4.
- **2.6 Multiplicity of JSON Encodings**: Non-UTF-8 encodings cause misinterpretation. Mitigated by Section 3.7.
- **2.7 Substitution Attacks**: JWT used at unintended recipient. Mitigated by Sections 3.8, 3.9.
- **2.8 Cross-JWT Confusion**: JWT used for a different purpose. Mitigated by Sections 3.8, 3.9, 3.11, 3.12.
- **2.9 Indirect Attacks on Server**: Claims used for lookups may cause injection/SSRF. Mitigated by Section 3.10.

## Best Practices (Requirements)

### 3.1 Perform Algorithm Verification
- **R1**: Libraries MUST enable the caller to specify a supported set of algorithms and MUST NOT use any other algorithms.
- **R2**: The library MUST ensure that the "alg" or "enc" header specifies the same algorithm that is used for the cryptographic operation.
- **R3**: Each key MUST be used with exactly one algorithm, and this MUST be checked when the cryptographic operation is performed.

### 3.2 Use Appropriate Algorithms
- **R4**: Applications MUST only allow the use of cryptographically current algorithms that meet the security requirements of the application. (Ref: [RFC7515] Section 5.2)
- **R5**: Applications MUST be designed to enable cryptographic agility.
- **R6**: The "none" algorithm SHOULD only be used when the JWT is cryptographically protected by other means (e.g., TLS).
- **R7**: JWT libraries SHOULD NOT generate or consume JWTs using "none" unless explicitly requested by the caller.
- **R8**: Avoid all RSA-PKCS1 v1.5 encryption algorithms ([RFC8017] Section 7.2); prefer RSAES-OAEP ([RFC8017] Section 7.1).
- **R9**: JWT libraries SHOULD implement ECDSA using deterministic approach per [RFC6979].

### 3.3 Validate All Cryptographic Operations
- **R10**: All cryptographic operations used in the JWT MUST be validated, and the entire JWT MUST be rejected if any fail. For Nested JWTs, both outer and inner operations MUST be validated.

### 3.4 Validate Cryptographic Inputs
- **R11**: The JWS/JWE library MUST validate cryptographic inputs (e.g., elliptic curve points) before use, or use underlying libraries that do.
- **R12**: For NIST prime-order curves P-256, P-384, P-521, validation MUST be performed according to [nist-sp-800-56a-r3] Section 5.6.2.3.4 (ECC Partial Public-Key Validation Routine).
- **R13**: For X25519/X448, the security considerations in [RFC8037] apply.

### 3.5 Ensure Cryptographic Keys Have Sufficient Entropy
- **R14**: The Key Entropy and Random Values advice in [RFC7515] Section 10.1 and Password Considerations in [RFC7518] Section 8.8 MUST be followed.
- **R15**: Human-memorizable passwords MUST NOT be directly used as the key to a keyed-MAC algorithm such as "HS256".

### 3.6 Avoid Compression of Encryption Inputs
- **R16**: Compression of data SHOULD NOT be done before encryption.

### 3.7 Use UTF-8
- **R17**: Implementations and applications MUST use UTF-8 for encoding/decoding JSON used in Header Parameters and JWT Claims Sets and MUST NOT admit other Unicode encodings.

### 3.8 Validate Issuer and Subject
- **R18**: When a JWT contains an "iss" claim, the application MUST validate that the cryptographic keys used belong to the issuer. If not, the application MUST reject the JWT.
- **R19**: When the JWT contains a "sub" claim, the application MUST validate that the subject value corresponds to a valid subject and/or issuer-subject pair at the application. If invalid, the application MUST reject the JWT.

### 3.9 Use and Validate Audience
- **R20**: If the same issuer issues JWTs intended for more than one relying party, the JWT MUST contain an "aud" claim.
- **R21**: The relying party or application MUST validate the audience value; if absent or not associated with the recipient, it MUST reject the JWT.

### 3.10 Do Not Trust Received Claims
- **R22**: Applications should ensure that the "kid" header does not create injection vulnerabilities by validating and/or sanitizing the received value.
- **R23**: Applications SHOULD protect against SSRF when processing "jku" or "x5u" headers (e.g., URL whitelist, no cookies in GET).

### 3.11 Use Explicit Typing
- **R24**: It is RECOMMENDED that the "application/" prefix be omitted from the "typ" value (e.g., "secevent+jwt" for SETs).
- **R25**: When explicit typing is employed, it is RECOMMENDED to use a media type of the format "application/example+jwt".
- **R26**: For Nested JWTs, the "typ" with the explicit type MUST be present in the inner JWT.
- **R27**: Explicit typing is RECOMMENDED for new uses of JWTs.

### 3.12 Use Mutually Exclusive Validation Rules for Different Kinds of JWTs
- **R28**: If more than one kind of JWT can be issued by the same issuer, the validation rules MUST be mutually exclusive, rejecting JWTs of the wrong kind.
- **R29**: Strategies include: different "typ" values, different required claims/values, different Header Parameters, different keys, different "aud" values, or different issuers. Explicit typing is RECOMMENDED for new applications.

## Requirements Summary
| ID | Requirement Text | Type | Reference |
|---|---|---|---|
| R1 | Libraries MUST enable caller to specify supported algorithms and MUST NOT use others. | MUST | Section 3.1 |
| R2 | Library MUST ensure "alg"/"enc" header matches algorithm used. | MUST | Section 3.1 |
| R3 | Each key MUST be used with exactly one algorithm. | MUST | Section 3.1 |
| R4 | Applications MUST only allow cryptographically current algorithms meeting security requirements. | MUST | Section 3.2 |
| R5 | Applications MUST be designed to enable cryptographic agility. | MUST | Section 3.2 |
| R6 | "none" SHOULD only be used when JWT is cryptographically protected by other means. | SHOULD | Section 3.2 |
| R7 | Libraries SHOULD NOT generate/consume "none" unless explicitly requested. | SHOULD | Section 3.2 |
| R8 | Avoid RSA-PKCS1 v1.5; prefer RSAES-OAEP. | SHOULD | Section 3.2 |
| R9 | Implement ECDSA using deterministic approach per RFC 6979. | SHOULD | Section 3.2 |
| R10 | All cryptographic operations MUST be validated; entire JWT rejected on failure. | MUST | Section 3.3 |
| R11 | Library MUST validate cryptographic inputs (e.g., EC points) or use validating libraries. | MUST | Section 3.4 |
| R12 | For P-256/384/521, validate per NIST SP 800-56A r3 Section 5.6.2.3.4. | MUST | Section 3.4 |
| R13 | For X25519/X448, follow RFC 8037 security considerations. | MUST | Section 3.4 |
| R14 | Follow [RFC7515] §10.1 and [RFC7518] §8.8 for key entropy. | MUST | Section 3.5 |
| R15 | Passwords MUST NOT be used directly as HMAC key. | MUST | Section 3.5 |
| R16 | Compression SHOULD NOT be done before encryption. | SHOULD | Section 3.6 |
| R17 | MUST use UTF-8 for JSON in headers and claims; no other encodings. | MUST | Section 3.7 |
| R18 | Validate that keys belong to issuer; reject if not. | MUST | Section 3.8 |
| R19 | Validate subject value; reject if invalid. | MUST | Section 3.8 |
| R20 | If multiple relying parties, JWT MUST contain "aud". | MUST | Section 3.9 |
| R21 | Recipient MUST validate audience; reject if absent/mismatch. | MUST | Section 3.9 |
| R22 | Sanitize/validate "kid" to prevent injection. | should | Section 3.10 |
| R23 | Protect against SSRF for "jku"/"x5u" (whitelist, no cookies). | SHOULD | Section 3.10 |
| R24 | Omit "application/" prefix in "typ" value. | RECOMMENDED | Section 3.11 |
| R25 | Use "application/example+jwt" format for explicit typing. | RECOMMENDED | Section 3.11 |
| R26 | For Nested JWTs, "typ" MUST be in inner JWT. | MUST | Section 3.11 |
| R27 | Explicit typing RECOMMENDED for new JWT uses. | RECOMMENDED | Section 3.11 |
| R28 | Validation rules for different JWT kinds MUST be mutually exclusive. | MUST | Section 3.12 |
| R29 | Use combination of types, claims, keys, etc., for differentiation; explicit typing RECOMMENDED. | RECOMMENDED | Section 3.12 |

## Informative Annexes (Condensed)
- **Section 2 Threats and Vulnerabilities**: Provides background on known attacks on JWT implementations and deployments, each linked to mitigating best practices in Section 3. (Informative)
- **Section 4 Security Considerations**: This entire document is about security considerations for JWT implementation and deployment. (Informative)
- **Section 5 IANA Considerations**: No IANA actions.
- **Section 6 References**: Contains both normative and informative references.