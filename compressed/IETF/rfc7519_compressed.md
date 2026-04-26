# RFC 7519: JSON Web Token (JWT)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc7519

## Scope (Summary)
JSON Web Token (JWT) is a compact, URL-safe claims representation format for use in space-constrained environments (e.g., HTTP Authorization headers, URI query parameters). JWTs encode claims as a JSON object that serves as the payload of a JSON Web Signature (JWS) or plaintext of a JSON Web Encryption (JWE), enabling digital signing, integrity protection via MAC, and/or encryption. JWTs always use JWS or JWE Compact Serialization.

## Normative References
- [ECMAScript] Ecma International, "ECMAScript Language Specification, 5.1 Edition", ECMA Standard 262, June 2011
- [IANA.MediaTypes] IANA, "Media Types", <http://www.iana.org/assignments/media-types>
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, May 2015
- [JWE] Jones, M. and J. Hildebrand, "JSON Web Encryption (JWE)", RFC 7516, May 2015
- [JWS] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, May 2015
- [RFC20] Cerf, V., "ASCII format for Network Interchange", STD 80, RFC 20, October 1969
- [RFC2046] Freed, N. and N. Borenstein, "MIME Part Two: Media Types", RFC 2046, November 1996
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", FYI 36, RFC 4949, August 2007
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, March 2014
- [UNICODE] The Unicode Consortium, "The Unicode Standard"

## Definitions and Abbreviations
- **JSON Web Token (JWT)**: A string representing a set of claims as a JSON object encoded in a JWS or JWE, enabling digital signing/MACing and/or encryption.
- **JWT Claims Set**: The JSON object containing the claims conveyed by the JWT.
- **Claim**: A piece of information asserted about a subject, represented as a name/value pair (Claim Name / Claim Value).
- **Claim Name**: The name portion of a claim (always a string).
- **Claim Value**: The value portion of a claim (any JSON value).
- **Nested JWT**: A JWT used as payload or plaintext of an enclosing JWS or JWE, enabling nested signing/encryption.
- **Unsecured JWT**: A JWT whose claims are not integrity protected or encrypted (JWS with "alg":"none" and empty signature).
- **Collision-Resistant Name**: A name in a namespace that minimizes collision likelihood (e.g., Domain Names, OIDs, UUIDs). Definer must control the portion of namespace used.
- **StringOrURI**: A JSON string; any value containing ":" MUST be a URI [RFC3986]. Compared as case-sensitive string.
- **NumericDate**: A JSON numeric value representing seconds from 1970-01-01T00:00:00Z UTC (ignoring leap seconds), equivalent to IEEE Std 1003.1 "Seconds Since the Epoch", allowing non-integer values.

## 1. Introduction
JWT is a compact claims representation. Claims are encoded as JSON object used as JWS Payload or JWE plaintext. JWTs are always represented using JWS or JWE Compact Serialization.

### 1.1. Notational Conventions
Key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL) are interpreted as described in RFC 2119, only when in all capital letters.

## 2. Terminology
Terms from JWS: "JSON Web Signature", "Base64url Encoding", "Header Parameter", "JOSE Header", "JWS Compact Serialization", "JWS Payload", "JWS Signature", "Unsecured JWS".
Terms from JWE: "JSON Web Encryption", "Content Encryption Key (CEK)", "JWE Compact Serialization", "JWE Encrypted Key", "JWE Initialization Vector".
Terms from RFC 4949: "Ciphertext", "Digital Signature", "Message Authentication Code (MAC)", "Plaintext".
Defined in this spec: see Definitions above.

## 3. JSON Web Token (JWT) Overview
JWTs represent claims as JSON object (JWT Claims Set). JOSE Header describes cryptographic operations. If JWS, claims are signed/MACed; if JWE, encrypted. Nested JWTs allow nested signing/encryption. JWT is a sequence of URL-safe base64url-encoded parts separated by '.'.
### 3.1. Example JWT
See example in original (Section 3.1). JOSE Header: {"typ":"JWT","alg":"HS256"}. JWT Claims Set: {"iss":"joe","exp":1300819380,"http://example.com/is_root":true}. Complete JWT: three base64url-encoded parts separated by '.'.

## 4. JWT Claims
JWT Claims Set is a JSON object. Claim Names MUST be unique; parsers MUST either reject duplicates or return lexically last duplicate as per ECMAScript 5.1. Unrecognized claims MUST be ignored (unless application requirements specify otherwise). Three classes: Registered, Public, Private.

### 4.1. Registered Claim Names
Registered in IANA "JSON Web Token Claims" registry (Section 10.1). None mandatory; provide interoperable set.
#### 4.1.1. "iss" (Issuer) Claim
Identifies principal that issued JWT. Value: case-sensitive StringOrURI. OPTIONAL.
#### 4.1.2. "sub" (Subject) Claim
Identifies principal subject. MUST be locally unique in issuer context or globally unique. Value: case-sensitive StringOrURI. OPTIONAL.
#### 4.1.3. "aud" (Audience) Claim
Identifies recipients. Each intended principal MUST identify itself in "aud". If present and principal does not match, JWT MUST be rejected. Value: array of case-sensitive StringOrURI, or single string if one audience. OPTIONAL.
#### 4.1.4. "exp" (Expiration Time) Claim
Expiration time on/after which JWT MUST NOT be accepted. Current time MUST be before expiration. MAY provide small leeway for clock skew. Value: NumericDate. OPTIONAL.
#### 4.1.5. "nbf" (Not Before) Claim
Time before which JWT MUST NOT be accepted. Current time MUST be after or equal to nbf. MAY provide small leeway. Value: NumericDate. OPTIONAL.
#### 4.1.6. "iat" (Issued At) Claim
Time JWT was issued. Value: NumericDate. OPTIONAL.
#### 4.1.7. "jti" (JWT ID) Claim
Unique identifier for JWT. MUST be assigned with negligible collision probability; collisions prevented across issuers. Can prevent replay. Value: case-sensitive string. OPTIONAL.

### 4.2. Public Claim Names
Claim Names defined at will; to prevent collisions, should be registered in the IANA registry or be a Collision-Resistant Name. Definer must control namespace.

### 4.3. Private Claim Names
Producer/consumer MAY agree to use Private Names (not Registered or Public). Subject to collision; use with caution.

## 5. JOSE Header
Members describe cryptographic operations and optionally additional properties. Rules from JWS/JWE apply.
### 5.1. "typ" (Type) Header Parameter
Declares media type of complete JWT. Used by applications to disambiguate when non-JWT objects may be present. Ignored by JWT implementations. RECOMMENDED value "JWT" (uppercase). OPTIONAL.
### 5.2. "cty" (Content Type) Header Parameter
Conveys structural information. When no nesting, NOT RECOMMENDED. For Nested JWT, MUST be present with value "JWT". RECOMMENDED uppercase. See Appendix A.2.
### 5.3. Replicating Claims as Header Parameters
Applications may replicate claims as Header Parameters in JWE (unencrypted). Receiving application SHOULD verify identical values unless other rules defined. Application ensures only safe claims replicated. Section 10.4.1 registers "iss", "sub", "aud" as Header Parameter names for JWE. Other specs may register additional.

## 6. Unsecured JWTs
JWTs MAY be created without signature/encryption for use cases where security is external. Unsecured JWT: JWS with "alg":"none" and empty JWS Signature.
### 6.1. Example Unsecured JWT
JOSE Header: {"alg":"none"}. JWT Claims Set same as Section 3.1 example. Complete JWT: two base64url-encoded parts and trailing '.' (empty signature).

## 7. Creating and Validating JWTs
### 7.1. Creating a JWT
1. Create JWT Claims Set (whitespace allowed).
2. Let Message be UTF-8 octets of JWT Claims Set.
3. Create JOSE Header. JWT MUST conform to JWS or JWE.
4. If JWS, create JWS per [JWS]; if JWE, create JWE per [JWE].
5. If nested operation, set Message as JWS or JWE, use "cty":"JWT" in new Header, go to step 3.
6. Otherwise, result is the JWS or JWE.
### 7.2. Validating a JWT
Steps; if any fail, JWT MUST be rejected.
1. Verify JWT contains at least one '.'.
2. Encoded JOSE Header: part before first '.'.
3. Base64url decode with restrictions.
4. Verify UTF-8 valid JSON object (RFC 7159) → JOSE Header.
5. Verify Header contains only understood/supported parameters (or ignored as specified).
6. Determine if JWS or JWE (per JWE Section 9).
7. If JWS, validate per [JWS]; let Message = base64url-decoded JWS Payload. If JWE, validate per [JWE]; let Message = plaintext.
8. If JOSE Header "cty" = "JWT", Message is nested JWT; return to step 1 with Message.
9. Otherwise, base64url decode Message with restrictions.
10. Verify UTF-8 valid JSON object (RFC 7159) → JWT Claims Set.
Application decision: reject JWT if algorithms used are not acceptable in context (SHOULD).
### 7.3. String Comparison Rules
Equality/inequality comparisons use JSON rules (RFC 7159 Section 8.3) for all member names/values except where member definition explicitly states different rule. In this spec, only "typ" and "cty" have different rules. Applications may need conventions for case-insensitive portions (e.g., DNS names in "iss").

## 8. Implementation Requirements
Conforming JWT implementations MUST implement HMAC SHA-256 ("HS256") and "none". RECOMMENDED: RSASSA-PKCS1-v1_5 SHA-256 ("RS256") and ECDSA P-256 SHA-256 ("ES256"). Other algorithms OPTIONAL.
Support for encrypted JWTs OPTIONAL. If supported, MUST implement: RSAES-PKCS1-v1_5 2048-bit ("RSA1_5"), AES Key Wrap 128/256-bit ("A128KW","A256KW"), composite AES-CBC HMAC SHA-2 ("A128CBC-HS256","A256CBC-HS512"). RECOMMENDED: ECDH-ES with key wrapping ("ECDH-ES+A128KW","ECDH-ES+A256KW"), AES GCM 128/256-bit ("A128GCM","A256GCM"). Others OPTIONAL.
Support for Nested JWTs OPTIONAL.

## 9. URI for Declaring that Content is a JWT
Registers URN "urn:ietf:params:oauth:token-type:jwt" for applications using URIs to declare content type.

## 10. IANA Considerations
### 10.1. JSON Web Token Claims Registry
Established registry for JWT Claim Names. Registration on Specification Required [RFC5226] after three-week review on jwt-reg-review@ietf.org, with Designated Experts. Registration template includes Claim Name (≤8 chars recommended), Claim Description, Change Controller, Specification Document(s). Initial registry contents: "iss" (Issuer), "sub" (Subject), "aud" (Audience), "exp" (Expiration Time), "nbf" (Not Before), "iat" (Issued At), "jti" (JWT ID), all with Change Controller IESG and specification reference to respective sections of RFC 7519.
### 10.2. Sub-Namespace Registration of urn:ietf:params:oauth:token-type:jwt
Registered in "OAuth URI" registry per RFC 6755. Common Name: JSON Web Token (JWT) Token Type.
### 10.3. Media Type Registration
Registered "application/jwt" media type. Encoding: 8bit, base64url-encoded parts separated by '.'. Applications: OpenID Connect, Mozilla Persona, Salesforce, Google, Android, Windows Azure, Amazon Web Services, etc.
### 10.4. Header Parameter Names Registration
Registers "iss", "sub", "aud" as Header Parameters in JWE Header (for replication per Section 5.3). Usage location: JWE.

## 11. Security Considerations
All cryptographic security issues must be addressed. JWS and JWE security considerations apply. In particular, JWS Sections 10.12 and 10.13 apply to JWT Claims Set.
### 11.1. Trust Decisions
JWT contents cannot be relied upon unless cryptographically secured and bound to context. Keys must be verifiably under control of issuer.
### 11.2. Signing and Encryption Order
For Nested JWTs, normally sign then encrypt (encrypting signature) to prevent stripping and provide privacy. JWE uses authenticated encryption, so cryptographic concerns about sign-after-encrypt are addressed.

## 12. Privacy Considerations
If JWT contains privacy-sensitive information, measures MUST prevent disclosure to unintended parties (e.g., encrypted JWT with recipient authentication, or transmission over TLS). Omitting sensitive info is simplest.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Claim Names within JWT Claims Set MUST be unique | MUST | Section 4 |
| R2 | JWT parsers MUST either reject duplicate Claim Names or use ECMAScript 5.1 behavior | MUST | Section 4 |
| R3 | Unrecognized claims MUST be ignored (unless application requires otherwise) | MUST | Section 4 |
| R4 | The "sub" value MUST be scoped to locally unique in issuer context or globally unique | MUST | Section 4.1.2 |
| R5 | Each principal intended to process JWT MUST identify itself in "aud" claim | MUST | Section 4.1.3 |
| R6 | If principal does not match "aud", JWT MUST be rejected | MUST | Section 4.1.3 |
| R7 | Current time MUST be before "exp" | MUST | Section 4.1.4 |
| R8 | Current time MUST be after or equal to "nbf" | MUST | Section 4.1.5 |
| R9 | "jti" MUST be assigned with negligible collision probability | MUST | Section 4.1.7 |
| R10 | For Nested JWT, "cty" Header Parameter MUST be present with value "JWT" | MUST | Section 5.2 |
| R11 | If claims replicated as Header Parameters, receiving application SHOULD verify identical values | SHOULD | Section 5.3 |
| R12 | Conforming JWT implementations MUST implement HS256 and "none" | MUST | Section 8 |
| R13 | RECOMMENDED to implement RS256 and ES256 | RECOMMENDED | Section 8 |
| R14 | If supporting encryption, MUST implement RSA1_5, A128KW, A256KW, A128CBC-HS256, A256CBC-HS512 | MUST | Section 8 |
| R15 | RECOMMENDED to implement ECDH-ES+A128KW, ECDH-ES+A256KW, A128GCM, A256GCM | RECOMMENDED | Section 8 |
| R16 | JWT validation steps (Section 7.2) – if any fails, JWT MUST be rejected | MUST | Section 7.2 |
| R17 | Application SHOULD reject JWT if algorithms not acceptable | SHOULD | Section 7.2 |
| R18 | String comparisons MUST use JSON rules except where explicitly overridden | MUST | Section 7.3 |
| R19 | Privacy-sensitive information MUST be protected (encryption or secure transport) | MUST | Section 12 |

## Informative Annexes (Condensed)
- **Appendix A. JWT Examples**: Provides example encrypted JWT (RSA1_5/A128CBC-HS256) and nested JWT (signed then encrypted); details of computation are referenced to JWS/JWE appendices.
- **Appendix B. Relationship of JWTs to SAML Assertions**: JWTs offer a simpler, more compact token format than SAML 2.0, using JSON instead of XML; not a full replacement but suitable when ease of implementation or compactness is needed.
- **Appendix C. Relationship of JWTs to Simple Web Tokens (SWTs)**: Both convey claims; SWTs use string claim values, JWTs allow any JSON type. JWTs support multiple algorithms; SWTs use HMAC SHA-256 only.
- **Acknowledgements**: Design influenced by SWTs and earlier JSON signing efforts (Magic Signatures, JSS, Canvas Applications). Work of OAuth working group; contributors listed.