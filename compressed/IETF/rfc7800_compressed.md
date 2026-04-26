# RFC 7800: Proof-of-Possession Key Semantics for JSON Web Tokens (JWTs)
**Source**: IETF | **Version**: Standards Track | **Date**: April 2016 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc7800

## Scope (Summary)
This specification defines how a JSON Web Token (JWT) can declare that the presenter possesses a particular proof-of-possession (PoP) key and how the recipient cryptographically confirms possession. It introduces the `cnf` (confirmation) claim and member values for representing asymmetric keys (jwk), encrypted symmetric keys (jwe), key identifiers (kid), and key set URLs (jku). The means of proving possession (e.g., nonce/challenge) are intentionally protocol specific.

## Normative References
- [IANA.JWT.Claims] IANA, "JSON Web Token Claims"
- [JWE] RFC 7516, "JSON Web Encryption (JWE)"
- [JWK] RFC 7517, "JSON Web Key (JWK)"
- [JWT] RFC 7519, "JSON Web Token (JWT)"
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels"
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646"
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax"
- [RFC5226] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs"
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2"
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)"

## Definitions and Abbreviations
- **Issuer**: Party that creates the JWT and binds the proof-of-possession key to it.
- **Presenter**: Party that proves possession of a private key (asymmetric) or secret key (symmetric) to a recipient.
- **Recipient**: Party that receives the JWT containing the proof-of-possession key information from the presenter.
- **cnf (confirmation) claim**: A claim in a JWT whose value is a JSON object whose members identify the proof-of-possession key.

## Notational Conventions
- The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **NOT RECOMMENDED**, **MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119.
- All protocol parameter names and values are case sensitive unless otherwise noted.

## 1. Introduction (Condensed)
Two use cases are illustrated: symmetric and asymmetric PoP keys.  

*Symmetric case*: A symmetric key is established between presenter and issuer; issuer creates a JWT with an encrypted copy of the key (encrypted to the recipient) in the `cnf` claim. The presenter proves possession by using the key in a challenge/response with the recipient.  

*Asymmetric case*: The presenter generates a public/private key pair and sends the public key to the issuer; the issuer issues a JWT containing the public key (or identifier) in the `cnf` claim. The presenter proves possession by using the private key in TLS or by signing a nonce.  

In both cases, the JWT may contain additional claims as needed by the application.

## 3. Representations for Proof-of-Possession Keys

### 3.1 Confirmation Claim
- The `cnf` claim declares that the presenter possesses a particular key and that the recipient can cryptographically confirm possession.
- At least one of the `sub` (subject) and `iss` (issuer) claims **MUST** be present in the JWT.
- The `cnf` claim value **MUST** represent only a single proof-of-possession key; at most one of the `jwk`, `jwe`, and `jku` confirmation values may be present.
- In the absence of application-specific requirements, all confirmation members not understood by implementations **MUST** be ignored.
- The set of confirmation members required for validity is context dependent and outside the scope of this specification.
- This specification establishes the IANA "JWT Confirmation Methods" registry (Section 6.2) and registers the members defined herein.

### 3.2 Representation of an Asymmetric Proof-of-Possession Key
- **`jwk` member**: A JSON Web Key (JWK) representing the corresponding public key.
- The JWK **MUST** contain the required key members for a JWK of that key type and **MAY** contain other JWK members, including `kid`.

### 3.3 Representation of an Encrypted Symmetric Proof-of-Possession Key
- **`jwe` member**: An encrypted JSON Web Key (JWK) encrypted to a key known to the recipient using the JWE Compact Serialization.
- The rules for encrypting a JWK are found in Section 7 of [JWK].
- The UTF-8 encoding of the JWK is used as the JWE Plaintext when encrypting.
- If the JWT is not encrypted, the symmetric key **MUST** be encrypted as described (i.e., using the `jwe` member).

### 3.4 Representation of a Key ID for a Proof-of-Possession Key
- **`kid` member**: A key identifier identifying the proof-of-possession key.
- The content of the `kid` value is application specific (e.g., a JWK Thumbprint).

### 3.5 Representation of a URL for a Proof-of-Possession Key
- **`jku` member**: A URI that refers to a resource for a set of JSON-encoded public keys represented as a JWK Set, one of which is the proof-of-possession key.
- If there are multiple keys in the referenced JWK Set document, a `kid` member **MUST** also be included with the referenced key's JWK also containing the same `kid` value.
- The protocol used to acquire the resource **MUST** provide integrity protection. An HTTP GET request to retrieve the JWK Set **MUST** use TLS and the identity of the server **MUST** be validated, as per Section 6 of RFC 6125.

### 3.6 Specifics Intentionally Not Specified
- The means of communicating the nonce/challenge and the signed nonce are not specified; they are protocol specific.
- The means of obtaining a key for the recipient is also protocol specific.

## 4. Security Considerations (Condensed with preserved normative statements)
- All security considerations from [JWT] apply.
- Appropriate means **must** be used to ensure that unintended parties do not learn private key or symmetric key values.
- Applications using proof-of-possession **should** also use audience restriction as described in Section 4.1.3 of [JWT].
- Applications that require the proof-of-possession keys to be understood **must** ensure that the relevant parts of this specification are implemented.
- Proof of possession via encrypted symmetric secrets is subject to replay attacks. This can be avoided by using a signed nonce or challenge, or by deriving a sub-key specific to the instance.
- Data origin authentication and integrity protection (via a keyed message digest or a digital signature) **must** be applied to the JWT.
- Symmetric keys carried in the JWT require both integrity protection and confidentiality protection.

## 5. Privacy Considerations (Condensed)
- For privacy reasons, it is **recommended** that different proof-of-possession keys be used when interacting with different parties to avoid correlation.

## 6. IANA Considerations

### 6.1 JSON Web Token Claims Registration
- Register the `cnf` claim in the IANA "JSON Web Token Claims" registry.
- Claim Name: `cnf` | Claim Description: Confirmation | Change Controller: IESG | Specification Document: Section 3.1 of RFC 7800.

### 6.2 JWT Confirmation Methods Registry
- Established for JWT `cnf` member values.
- Registration procedure: Specification Required [RFC5226] after a three-week review period on the jwt-reg-review@ietf.org mailing list, on advice of one or more Designated Experts.
- Criteria: no duplication, general applicability, sensible security properties.
- Recommended name length ≤ 8 characters.
- **Initial Registry Contents**:

| Confirmation Method Value | Description | Specification Document(s) |
|---------------------------|-------------|--------------------------|
| `jwk`                     | JSON Web Key Representing Public Key | Section 3.2 of RFC 7800 |
| `jwe`                     | Encrypted JSON Web Key | Section 3.3 of RFC 7800 |
| `kid`                     | Key Identifier | Section 3.4 of RFC 7800 |
| `jku`                     | JWK Set URL | Section 3.5 of RFC 7800 |

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | At least one of `sub` and `iss` claims **MUST** be present in the JWT. | MUST | Section 3 |
| R2 | The `cnf` claim value **MUST** represent only a single proof-of-possession key (at most one of `jwk`, `jwe`, `jku`). | MUST | Section 3.1 |
| R3 | All confirmation members not understood by implementations **MUST** be ignored (unless application requires otherwise). | MUST | Section 3.1 |
| R4 | The `jwk` member, when used, **MUST** contain the required key members for a JWK of that key type. | MUST | Section 3.2 |
| R5 | If the JWT is not encrypted, the symmetric key **MUST** be encrypted using the `jwe` member. | MUST | Section 3.3 |
| R6 | If multiple keys exist in a JWK Set referenced by `jku`, a `kid` member **MUST** be included and the referenced JWK **MUST** contain the same `kid`. | MUST | Section 3.5 |
| R7 | The protocol used to acquire the JWK Set resource **MUST** provide integrity protection; HTTP GET **MUST** use TLS and server identity validated per RFC 6125 Section 6. | MUST | Section 3.5 |
| R8 | Data origin authentication and integrity protection (via keyed message digest or digital signature) must be applied to the JWT. | normative requirement | Section 4 |
| R9 | Symmetric keys carried in the JWT require both integrity protection and confidentiality protection. | normative requirement | Section 4 |