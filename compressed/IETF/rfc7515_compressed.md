# RFC 7515: JSON Web Signature (JWS)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/info/rfc7515

## Scope (Summary)
Defines the JSON Web Signature (JWS) data structure for representing content secured with digital signatures or Message Authentication Codes (MACs) using JSON-based structures. Specifies two serializations (Compact and JSON) and a set of registered header parameters for describing cryptographic operations. Defines how to produce and consume JWSs, including signing, validation, key identification, and security considerations.

## Normative References
- [ECMAScript] Ecma International, "ECMAScript Language Specification, 5.1 Edition", ECMA 262, June 2011.
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015.
- [JWK] Jones, M., "JSON Web Key (JWK)", RFC 7517, May 2015.
- [RFC20] Cerf, V., "ASCII format for Network Interchange", STD 80, RFC 20, 1969.
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One", RFC 2045, 1996.
- [RFC2046] Freed, N. and N. Borenstein, "MIME Part Two: Media Types", RFC 2046, 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, 1997.
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, 2000.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, 2003.
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, 2005.
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, 2005.
- [RFC4945] Korver, B., "The Internet IP Security PKI Profile of IKEv1/ISAKMP, IKEv2, and PKIX", RFC 4945, 2007.
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", FYI 36, RFC 4949, 2007.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, 2008.
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", RFC 5280, 2008.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within PKIX", RFC 6125, 2011.
- [RFC6176] Turner, S. and T. Polk, "Prohibiting Secure Sockets Layer (SSL) Version 2.0", RFC 6176, 2011.
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, 2014.
- [UNICODE] The Unicode Consortium, "The Unicode Standard".
- [ITU.X690.2008] ITU-T Recommendation X.690, 2008.

## Definitions and Abbreviations
- **JSON Web Signature (JWS)**: A data structure representing a digitally signed or MACed message.
- **JOSE Header**: JSON object containing parameters describing cryptographic operations. Comprises a set of Header Parameters.
- **JWS Payload**: The sequence of octets to be secured (the message).
- **JWS Signature**: Digital signature or MAC over the JWS Protected Header and the JWS Payload.
- **Header Parameter**: A name/value pair that is a member of the JOSE Header.
- **JWS Protected Header**: JSON object containing Header Parameters that are integrity protected by the JWS Signature operation. For JWS Compact Serialization, this is the entire JOSE Header. For JWS JSON Serialization, it is one component.
- **JWS Unprotected Header**: JSON object containing Header Parameters that are not integrity protected. Only present in JWS JSON Serialization.
- **Base64url Encoding**: Base64 encoding using URL-safe characters (RFC 4648 Section 5) with all trailing '=' omitted; base64url of empty octets is empty string.
- **JWS Signing Input**: ASCII(BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload)).
- **JWS Compact Serialization**: A compact, URL-safe string representation of a JWS.
- **JWS JSON Serialization**: A JSON object representation, enabling multiple signatures/MACs. Not optimized for compactness or URL-safety.
- **Unsecured JWS**: A JWS using "alg":"none", providing no integrity protection.
- **Collision-Resistant Name**: A name in a namespace designed to avoid collisions (e.g., Domain Names, OIDs, UUIDs).
- **StringOrURI**: A JSON string value; any value containing ":" MUST be a URI [RFC3986]. Compared as case-sensitive strings.
- **Digital Signature** and **Message Authentication Code (MAC)**: As defined in RFC 4949.

## 1. Introduction
JWS represents content secured with digital signatures or MACs using JSON-based data structures (RFC 7159). Provides integrity protection for arbitrary octet sequences. Two serializations: JWS Compact Serialization (URL-safe, for space-constrained environments) and JWS JSON Serialization (supports multiple signatures/MACs). Cryptographic algorithms defined in JWA [JWA] and associated IANA registry. Related encryption described in JWE [JWE]. Names are short for compactness.

### 1.1. Notational Conventions
- **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, **OPTIONAL** as per RFC 2119.
- BASE64URL(OCTETS): base64url encoding per Section 2.
- UTF8(STRING): UTF-8 octets of STRING.
- ASCII(STRING): ASCII octets of STRING.
- A || B: concatenation of A and B.

## 2. Terminology
(Definitions provided in Definitions and Abbreviations section above.)

## 3. JSON Web Signature (JWS) Overview
JWS represents logical values: JOSE Header, JWS Payload, JWS Signature. JOSE Header members are union of JWS Protected Header and JWS Unprotected Header members. Two serializations defined.

### 3.1. JWS Compact Serialization Overview
No JWS Unprotected Header used. JWS represented as:  
`BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload) || '.' || BASE64URL(JWS Signature)`.

### 3.2. JWS JSON Serialization Overview
One or both of JWS Protected Header and JWS Unprotected Header MUST be present. JWS represented as JSON object with members "protected", "header", "payload", "signature". Can represent multiple signatures/MACs.

### 3.3. Example JWS
Example using HMAC SHA-256 with JWS Compact Serialization. Header: `{"typ":"JWT","alg":"HS256"}`. Payload: `{"iss":"joe","exp":1300819380,"http://example.com/is_root":true}`. Signature and complete JWS shown. (Full example in Appendix A.1.)

## 4. JOSE Header
Members of JSON object(s) representing JOSE Header describe the digital signature or MAC and optional properties. Header Parameter names MUST be unique; parsers MUST either reject duplicates or use a JSON parser that returns only the lexically last duplicate member name (per ECMAScript 5.1 Section 15.12). Implementations MUST understand and process Header Parameters designated as "MUST be understood". Other defined parameters MUST be ignored when not understood. Undefined parameters MUST be ignored unless listed as critical.

Three classes: Registered, Public, Private.

### 4.1. Registered Header Parameter Names
Registered in IANA "JSON Web Signature and Encryption Header Parameters" registry.

#### 4.1.1. "alg" (Algorithm) Header Parameter
Identifies cryptographic algorithm used. JWS Signature is not valid if "alg" does not represent a supported algorithm or if no key for that algorithm is associated with the signer. "alg" values should be registered in IANA "JSON Web Signature and Encryption Algorithms" registry or be a Collision-Resistant Name. Value is case-sensitive ASCII StringOrURI. MUST be present and MUST be understood and processed.

#### 4.1.2. "jku" (JWK Set URL) Header Parameter
URI referring to a resource for a set of JSON-encoded public keys, one of which corresponds to the signing key. Keys MUST be encoded as a JWK Set [JWK]. Protocol MUST provide integrity protection; HTTP GET MUST use TLS; server identity MUST be validated per RFC 6125 Section 6. Use is OPTIONAL.

#### 4.1.3. "jwk" (JSON Web Key) Header Parameter
Public key corresponding to the signing key, represented as a JWK [JWK]. Use is OPTIONAL.

#### 4.1.4. "kid" (Key ID) Header Parameter
Hint indicating which key was used. Structure unspecified. Value MUST be case-sensitive string. Use is OPTIONAL. When used with JWK, matches JWK "kid" parameter.

#### 4.1.5. "x5u" (X.509 URL) Header Parameter
URI referring to resource for the X.509 public key certificate or certificate chain (RFC 5280). Resource MUST provide PEM-encoded certificate chain per RFC 5280. First certificate MUST be the signing key certificate. Protocol MUST provide integrity protection; HTTP GET MUST use TLS; server identity MUST be validated per RFC 6125 Section 6. Use is OPTIONAL.

#### 4.1.6. "x5c" (X.509 Certificate Chain) Header Parameter
X.509 public key certificate or certificate chain as JSON array of base64-encoded (RFC 4648 Section 4) DER PKIX certificate strings. First certificate MUST be signing key certificate. Recipient MUST validate certificate chain per RFC 5280; invalid if any validation failure occurs. Use is OPTIONAL.

#### 4.1.7. "x5t" (X.509 Certificate SHA-1 Thumbprint) Header Parameter
Base64url-encoded SHA-1 thumbprint (digest) of the DER encoding of the X.509 certificate. Use is OPTIONAL.

#### 4.1.8. "x5t#S256" (X.509 Certificate SHA-256 Thumbprint) Header Parameter
Base64url-encoded SHA-256 thumbprint of the DER encoding of the X.509 certificate. Use is OPTIONAL.

#### 4.1.9. "typ" (Type) Header Parameter
Declares media type of the complete JWS. Intended for disambiguation by applications. Ignored by JWS implementations. Use is OPTIONAL. RECOMMENDED to omit "application/" prefix if no other '/' appears in the value. Recipient MUST treat value without '/' as if "application/" were prepended. "JOSE" indicates JWS/JWE using Compact Serialization; "JOSE+JSON" indicates JSON Serialization.

#### 4.1.10. "cty" (Content Type) Header Parameter
Declares media type of the secured content (payload). Ignored by JWS implementations. Use is OPTIONAL. RECOMMENDED to omit "application/" prefix if no other '/' appears. Recipient MUST treat value without '/' as if "application/" were prepended.

#### 4.1.11. "crit" (Critical) Header Parameter
Array listing extension Header Parameter names that MUST be understood and processed. If any listed extension is not understood/supported, the JWS is invalid. Producers MUST NOT include names defined by this specification or JWA for use with JWS, duplicate names, or names not present in JOSE Header. Producers MUST NOT use empty list. Recipients MAY consider JWS invalid if critical list contains names from this spec or JWA for JWS. MUST be integrity protected, so MUST occur only in JWS Protected Header. Use is OPTIONAL. MUST be understood and processed.

### 4.2. Public Header Parameter Names
May be defined by users. To prevent collisions, should be registered in IANA registry or be a Public Name (Collision-Resistant Name). Should be introduced sparingly to avoid non-interoperability.

### 4.3. Private Header Parameter Names
Agreed between producer and consumer. Subject to collision; use with caution.

## 5. Producing and Consuming JWSs

### 5.1. Message Signature or MAC Computation
Steps (order not significant unless dependencies exist):
1. Create JWS Payload.
2. Compute BASE64URL(JWS Payload).
3. Create JOSE Header (JWS Protected Header and/or JWS Unprotected Header) as JSON objects.
4. Compute BASE64URL(UTF8(JWS Protected Header)). If not present, use empty string.
5. Compute JWS Signature over JWS Signing Input using algorithm specified by "alg" Header Parameter, which MUST be present and accurate.
6. Compute BASE64URL(JWS Signature).
7. If JWS JSON Serialization, repeat steps 3-6 for each signature/MAC.
8. Create serialized output (Compact or JSON Serialization).

### 5.2. Message Signature or MAC Validation
Steps (order not significant unless dependencies exist; failure of any step means validation failure):
1. Parse JWS representation to extract components. For Compact Serialization: three base64url-encoded parts separated by '.'; for JSON Serialization: JSON object with "protected", "header", "payload", "signature".
2. Base64url-decode JWS Protected Header (no extra characters).
3. Verify decoded octets are UTF-8-encoded valid JSON object (RFC 7159); let this be JWS Protected Header.
4. For Compact Serialization, JOSE Header = JWS Protected Header. For JSON Serialization, JOSE Header = union of corresponding JWS Protected Header and JWS Unprotected Header (both must be valid JSON), ensuring no duplicate Header Parameter names across the union.
5. Verify implementation understands and can process all required fields (by this spec, algorithm, or "crit").
6. Base64url-decode JWS Payload.
7. Base64url-decode JWS Signature.
8. Validate JWS Signature against JWS Signing Input using algorithm represented by "alg" (MUST be present). Record success/failure.
9. For JSON Serialization, repeat steps 4-8 for each signature/MAC.
10. If none succeeded, JWS MUST be considered invalid. Otherwise, return results. In Compact Serialization, result indicates validity. Application decision which algorithms are acceptable; even if validated, JWS SHOULD be considered invalid if algorithm is not acceptable.

### 5.3. String Comparison Rules
JSON string comparisons for member names and values (except "typ" and "cty") MUST use equality/inequality rules from RFC 7159 Section 8.3. For case-insensitive components (e.g., DNS in "kid"), application may need canonical case convention.

## 6. Key Identification
Recipient must determine key used. Header Parameters "jku", "jwk", "kid", "x5u", "x5c", "x5t", "x5t#S256" can be used for identification. These parameters MUST be integrity protected if used in trust decisions; if only key matters, they need not be. Producer SHOULD include sufficient information to identify key. Validation fails if algorithm requires key (except "none") and key cannot be determined. Means of exchanging symmetric keys outside scope.

## 7. Serializations

### 7.1. JWS Compact Serialization
Single string: `BASE64URL(UTF8(JWS Protected Header)) || '.' || BASE64URL(JWS Payload) || '.' || BASE64URL(JWS Signature)`. Only one signature/MAC; no JWS Unprotected Header.

### 7.2. JWS JSON Serialization
JSON object; not optimized for compactness or URL-safety. Two syntaxes: General and Flattened.

#### 7.2.1. General JWS JSON Serialization Syntax
Top-level members:
- "payload": MUST be present, value = BASE64URL(JWS Payload).
- "signatures": MUST be an array of JSON objects, each representing a signature/MAC.

Each element in "signatures":
- "protected": MUST be present if JWS Protected Header non-empty (value = BASE64URL(UTF8(protected))); otherwise absent.
- "header": MUST be present if JWS Unprotected Header non-empty (value = unencoded JSON object); otherwise absent.
- "signature": MUST be present (value = BASE64URL(JWS Signature)).

At least one of "protected" and "header" MUST be present for each signature/MAC to convey "alg". Header Parameter names in "protected" and "header" MUST be disjoint. Additional members allowed; if not understood, MUST be ignored. Union of protected and header comprises JOSE Header. Each JWS Signature computed same way as for Compact Serialization. Syntax summary in Section 7.2.1.

#### 7.2.2. Flattened JWS JSON Serialization Syntax
Optimized for single signature/MAC. "signatures" member MUST NOT be present. Instead, "protected", "header", and "signature" members appear at top level alongside "payload". Processed identically to general syntax.

## 8. TLS Requirements
Implementations supporting "jku" and/or "x5u" MUST support TLS. TLS version should be current secure version (at writing, TLS 1.2 [RFC5246]). Confidentiality protection MUST be applied using TLS with ciphersuite providing confidentiality and integrity. Follow guidance from IETF TLS WG and RFC 7525. When TLS used, service provider identity in TLS server certificate MUST be verified per RFC 6125 Section 6.

## 9. IANA Considerations
Registration for all registries on Specification Required basis (RFC 5226) after three-week review on jose-reg-review@ietf.org, on advice of Designated Experts. Review process described. IANA only accepts updates from Designated Experts. Multiple Experts suggested.

### 9.1. JSON Web Signature and Encryption Header Parameters Registry
Established for Header Parameter names. Records name and reference to defining spec. Same name can be registered multiple times if usage compatible.

#### 9.1.1. Registration Template
- Header Parameter Name: short (≤8 characters recommended), case-sensitive.
- Header Parameter Description: brief description.
- Header Parameter Usage Location(s): one or more of "JWS" or "JWE".
- Change Controller: "IESG" for Standards Track RFCs.
- Specification Document(s): reference.

#### 9.1.2. Initial Registry Contents
List of 11 header parameters (alg, jku, jwk, kid, x5u, x5c, x5t, x5t#S256, typ, cty, crit) with descriptions, usage location JWS, Change Controller IESG, specification reference to respective sections of RFC 7515.

### 9.2. Media Type Registration

#### 9.2.1. Registry Contents
- "application/jose": indicates JWS or JWE using Compact Serialization. Encoding: 8bit, base64url values separated by '.'. Security considerations see RFC 7515.
- "application/jose+json": indicates JWS or JWE using JSON Serialization. Encoding: 8bit; UTF-8 SHOULD be employed for the JSON object.

Both media types have required parameters n/a, optional n/a, etc. Intended usage COMMON.

## 10. Security Considerations
All security issues pertinent to cryptographic applications must be addressed. Reference XML Signature security considerations (W3C.NOTE-xmldsig-core2-20130411) applying to JWS except XML-specific ones.

### 10.1. Key Entropy and Random Values
Keys require sufficient entropy; minimum 128 bits recommended. Implementations must randomly generate key pairs, MAC keys, and padding. Use of inadequate PRNGs compromises security. Guidance in RFC 4086.

### 10.2. Key Protection
Implementations must protect signer's private key and MAC key. Compromise leads to masquerade or undetectable modification.

### 10.3. Key Origin Authentication
Public key management must authenticate key origin; otherwise, signer unknown. MAC key distribution must provide data origin authentication.

### 10.4. Cryptographic Agility
Refer to JWA [JWA] Section 8.1.

### 10.5. Differences between Digital Signatures and MACs
Signatures assume private key only with one entity; MAC key is shared. MAC validation only shows one of the key-holders generated the message; cannot prove origination to third party.

### 10.6. Algorithm Validation
Implementations MUST ensure that algorithm information encoded in the signature (e.g., hash in RSASSA-PKCS1-v1_5) matches the "alg" Header Parameter. Otherwise attacker could claim strong hash while using weak one.

### 10.7. Algorithm Protection
Risk of algorithm substitution attacks when verifiers support multiple algorithms. Mitigations: use algorithms not vulnerable to substitution (e.g., SHA-2), require "alg" in Protected Header (always in Compact Serialization), include algorithm field in payload and verify match.

### 10.8. Chosen Plaintext Attacks
Creators should not allow third parties to insert arbitrary content without entropy not controlled by third party.

### 10.9. Timing Attacks
Implementations must avoid timing differences between successful and unsuccessful operations to prevent key information leakage.

### 10.10. Replay Protection
Applications can thwart replay by including unique message identifier as integrity-protected content and verifying it hasn't been previously received.

### 10.11. SHA-1 Certificate Thumbprints
SHA-1 used for "x5t" for compatibility. If effective SHA-1 collision discovered, attacker could substitute certificate if they have write access to victim's certificate store. Alternative: use "x5t#S256". At writing, no platform supports SHA-256 thumbprints.

### 10.12. JSON Security Considerations
Strict JSON validation required. Malformed JSON MUST be rejected (RFC 7159). Header Parameter names MUST be unique; parsers MUST reject duplicates or return lexically last duplicate member name. Input with extra characters after valid JSON MUST be considered invalid.

### 10.13. Unicode Comparison Security Considerations
Header Parameter names and algorithm names must be compared verbatim after escape processing. Characters outside Basic Multilingual Plane SHOULD be preserved and compared correctly; otherwise, input containing them MUST be rejected.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Header Parameter names within the JOSE Header MUST be unique; JWS parsers MUST either reject JWSs with duplicate Header Parameter names or use a JSON parser that returns only the lexically last duplicate member name. | must | Section 4 |
| R2 | Implementations are required to understand the specific Header Parameters designated as "MUST be understood" and process them accordingly. | must | Section 4 |
| R3 | All other Header Parameters defined by this specification that are not designated as "MUST be understood" MUST be ignored when not understood. | must | Section 4 |
| R4 | Unless listed as a critical Header Parameter, all Header Parameters not defined by this specification MUST be ignored when not understood. | must | Section 4 |
| R5 | The "alg" Header Parameter MUST be present and MUST be understood and processed by implementations. | must | 4.1.1 |
| R6 | The keys in "jku" (JWK Set URL) MUST be encoded as a JWK Set. The protocol used to acquire the resource MUST provide integrity protection; an HTTP GET request MUST use TLS; the identity of the server MUST be validated per RFC 6125 Section 6. | must | 4.1.2 |
| R7 | The "kid" value MUST be a case-sensitive string. | must | 4.1.4 |
| R8 | The resource identified by "x5u" MUST provide a representation of the certificate or certificate chain conforming to RFC 5280 in PEM-encoded form. The protocol used MUST provide integrity protection; HTTP GET MUST use TLS; server identity MUST be validated per RFC 6125. | must | 4.1.5 |
| R9 | For "x5c", the recipient MUST validate the certificate chain according to RFC 5280 and consider it invalid if any validation failure occurs. | must | 4.1.6 |
| R10 | The "typ" value without '/' MUST be treated as if "application/" were prepended. | must | 4.1.9 |
| R11 | The "cty" value without '/' MUST be treated as if "application/" were prepended. | must | 4.1.10 |
| R12 | Producers MUST NOT include Header Parameter names defined by this specification or JWA for use with JWS, duplicate names, or names that do not occur as Header Parameter names within the JOSE Header in the "crit" list. Producers MUST NOT use the empty list "[]" as the "crit" value. | must | 4.1.11 |
| R13 | When used, the "crit" Header Parameter MUST be integrity protected; therefore it MUST occur only within the JWS Protected Header. | must | 4.1.11 |
| R14 | The "crit" Header Parameter MUST be understood and processed by implementations. | must | 4.1.11 |
| R15 | For creating a JWS, the "alg" (algorithm) Header Parameter MUST be present in the JOSE Header, with the algorithm value accurately representing the algorithm used to construct the JWS Signature. | must | 5.1 |
| R16 | For validation, the algorithm MUST be accurately represented by the value of the "alg" Header Parameter, which MUST be present. | must | 5.2 |
| R17 | If none of the validations succeeded, then the JWS MUST be considered invalid. | must | 5.2 |
| R18 | Even if a JWS can be successfully validated, unless the algorithm(s) used are acceptable to the application, it SHOULD consider the JWS to be invalid. | should | 5.2 |
| R19 | String comparison rules from RFC 7159 Section 8.3 MUST be used for all JSON string comparisons except for "typ" and "cty". | must | 5.3 |
| R20 | Header Parameters used to identify the key ("jku", "jwk", "kid", "x5u", "x5c", "x5t", "x5t#S256") MUST be integrity protected if the information they convey is to be utilized in a trust decision. | must | 6 |
| R21 | At least one of "protected" and "header" MUST be present for each signature/MAC computation in JWS JSON Serialization so that an "alg" Header Parameter value is conveyed. | must | 7.2.1 |
| R22 | The Header Parameter names in "protected" and "header" locations MUST be disjoint. | must | 7.2.1 |
| R23 | The "signatures" member MUST NOT be present when using flattened JWS JSON Serialization. | must | 7.2.2 |
| R24 | Implementations supporting "jku" and/or "x5u" MUST support TLS. | must | 8 |
| R25 | Confidentiality protection MUST be applied using TLS with a ciphersuite that provides confidentiality and integrity protection. | must | 8 |
| R26 | Whenever TLS is used, the identity of the service provider encoded in the TLS server certificate MUST be verified using the procedures described in Section 6 of RFC 6125. | must | 8 |
| R27 | For algorithm validation, implementations MUST ensure that the algorithm information encoded in the signature corresponds to that specified with the "alg" Header Parameter. | must | 10.6 |
| R28 | Any JSON inputs not conforming to the JSON-text syntax defined in RFC 7159 MUST be rejected in their entirety. | must | 10.12 |
| R29 | Input containing extra significant characters after valid JSON MUST be considered invalid. | must | 10.12 |
| R30 | Header Parameter names and algorithm names must be compared verbatim after escape processing. | must | 10.13 |
| R31 | If characters outside Basic Multilingual Plane cannot be preserved and compared correctly, input containing them MUST be rejected. | must | 10.13 |
| R32 | The "payload" member in general JWS JSON Serialization MUST be present. | must | 7.2.1 |
| R33 | The "signatures" member in general JWS JSON Serialization MUST be present and contain an array of JSON objects. | must | 7.2.1 |
| R34 | For each element in "signatures": "signature" member MUST be present. "protected" MUST be present if JWS Protected Header non-empty; otherwise absent. "header" MUST be present if JWS Unprotected Header non-empty; otherwise absent. | must | 7.2.1 |

## Informative Annexes (Condensed)
- **Appendix A. JWS Examples**: Provides detailed examples of JWS using HMAC SHA-256, RSASSA-PKCS1-v1_5 SHA-256, ECDSA P-256 SHA-256, ECDSA P-521 SHA-512, Unsecured JWS (alg "none"), and examples using the General and Flattened JWS JSON Serializations. Each sub-appendix includes encoding steps and validation procedures.
- **Appendix B. "x5c" (X.509 Certificate Chain) Example**: Shows a JSON array example of an X.509 certificate chain for use with the "x5c" Header Parameter.
- **Appendix C. Notes on Implementing base64url Encoding without Padding**: Provides C# code for base64url encoding/decoding without padding, based on standard base64 functions, with explanation of padding determination.
- **Appendix D. Notes on Key Selection**: Describes a family of possible algorithms for selecting keys for validation/decryption, including collecting, filtering, ordering, making trust decisions, and attempting validation/decryption. Steps are illustrative; specific applications may have simpler methods.
- **Appendix E. Negative Test Case for "crit" Header Parameter**: Provides a JWS that MUST be rejected because it uses an unknown critical extension `http://example.invalid/UNDEFINED`. Conforming implementations must reject such input.
- **Appendix F. Detached Content**: Explains how to integrity-protect content not contained in the JWS by creating a normal JWS, then deleting the payload representation (replacing with empty string for Compact Serialization or removing "payload" member for JSON Serialization), and having the recipient reconstruct the JWS.