# RFC 7638: JSON Web Key (JWK) Thumbprint
**Source**: IETF | **Version**: Standards Track | **Date**: September 2015 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc7638

## Scope (Summary)
This specification defines a method for computing a cryptographic hash (thumbprint) over a JSON Web Key (JWK) by selecting only required members, creating a canonical JSON object with lexicographically sorted member names, and hashing its UTF-8 encoding. The resulting thumbprint can be used for key identification or selection, e.g., as a "kid" value.

## Normative References
- [IANA.JOSE] IANA, "JSON Object Signing and Encryption (JOSE)", <http://www.iana.org/assignments/jose>
- [JWA] Jones, M., "JSON Web Algorithms (JWA)", RFC 7518, DOI 10.17487/RFC7518, May 2015
- [JWK] Jones, M., "JSON Web Key (JWK)", RFC 7517, DOI 10.17487/RFC7517, May 2015
- [JWS] Jones, M., Bradley, J., and N. Sakimura, "JSON Web Signature (JWS)", RFC 7515, DOI 10.17487/RFC7515, May 2015
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC7159] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", RFC 7159, March 2014
- [SHS] National Institute of Standards and Technology, "Secure Hash Standard (SHS)", FIPS PUB 180-4, March 2012
- [UNICODE] The Unicode Consortium, "The Unicode Standard", <http://www.unicode.org/versions/latest/>

## Definitions and Abbreviations
- **JWK Thumbprint**: The digest value for a JWK computed as defined in Section 3.

## 1. Introduction
This specification defines a method for computing a hash value over a JSON Web Key (JWK). It defines which fields in a JWK are used in the hash computation, the method of creating a canonical form for those fields, and how to convert the resulting Unicode string into a byte sequence to be hashed. The resulting hash value can be used for identifying or selecting the key represented by the JWK that is the subject of the thumbprint, for instance, by using the base64url-encoded JWK Thumbprint value as a "kid" (key ID) value.

### 1.1. Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119. The interpretation should only be applied when the terms appear in all capital letters.

## 2. Terminology
This specification uses the same terminology as the "JSON Web Key (JWK)" [JWK], "JSON Web Signature (JWS)" [JWS], and "JSON Web Algorithms (JWA)" [JWA] specifications.
- **JWK Thumbprint**: The digest value for a JWK.

## 3. JSON Web Key (JWK) Thumbprint
The thumbprint of a JSON Web Key (JWK) is computed as follows:
1. Construct a JSON object [RFC7159] containing only the required members of a JWK representing the key and with no whitespace or line breaks before or after any syntactic elements and with the required members ordered lexicographically by the Unicode code points of the member names. (This JSON object is itself a legal JWK representation of the key.)
2. Hash the octets of the UTF-8 representation of this JSON object with a cryptographic hash function H. For example, SHA-256 [SHS] might be used as H. See Section 3.4 for a discussion on the choice of hash function.

The resulting value is the JWK Thumbprint with H of the JWK.

### 3.1. Example JWK Thumbprint Computation
*(Informative example)* For an RSA public key with members "kty", "n", "e", the lexicographic order is "e", "kty", "n". The intermediate JSON object is {"e":"AQAB","kty":"RSA","n":"..."}. Using SHA-256, the base64url-encoded thumbprint is `NzbLsXh8uDCcd-6MNwXF4W_7noWXFZAfHkxZsRGC9Xs`.

### 3.2. JWK Members Used in the Thumbprint Computation
Only the required members of a key's representation are used when computing its JWK Thumbprint value. As defined in JWK and JWA:
- For elliptic curve public key: "crv", "kty", "x", "y" (lexicographic order)
- For RSA public key: "e", "kty", "n"
- For symmetric key: "k", "kty"
As other "kty" values are defined, the specifications defining them should be similarly consulted to determine which members, in addition to "kty", are required.

#### 3.2.1. JWK Thumbprint of a Private Key
The JWK Thumbprint of a JWK representing a private key is computed as the JWK Thumbprint of a JWK representing the corresponding public key. This enables the same thumbprint to be used by both public and private key holders.

#### 3.2.2. Why Not Include Optional Members?
Optional members are intentionally excluded to ensure the thumbprint refers to the key itself, not key attributes. This ensures any JWK representing the same key yields the same thumbprint irrespective of additional attributes. Other specifications may define different kinds of thumbprints that include optional members.

### 3.3. Order and Representation of Members in Hash Input
- **Requirement (MUST)**: Characters in member names and member values MUST be represented without being escaped. Thumbprints of JWKs that require such characters are not defined by this specification.
- **Requirement (MUST)**: If the JWK key type uses members whose values are themselves JSON objects, then the members of those objects MUST likewise be lexicographically ordered.
- **Requirement (MUST)**: If the JWK key type uses members whose values are JSON numbers, and if those numbers are integers, then they MUST be represented as a JSON number as defined in RFC 7159 Section 6 without including a fraction part or exponent part. Thumbprints of JWKs using non-integer numbers are not defined.

### 3.4. Selection of Hash Function
A specific hash function must be chosen by an application to compute the hash value. SHA-256 is a good default at this writing but may change over time. In many cases, only the key producer needs to know the hash function; the consumer treats the thumbprint as opaque. When multiple parties compute thumbprints, they must use the same hash function.

### 3.5. JWK Thumbprints of Keys Not in JWK Format
A key need not be in JWK format to create a JWK Thumbprint. The only prerequisites are that the JWK representation of the key is defined and the party has the necessary key material.

## 4. Practical JSON and Unicode Considerations (Condensed)
Implementations should use platform JSON support but must avoid issues with non-ASCII characters, escaped characters, and non-integer numbers. All defined JWK member names and values currently use only printable ASCII. Future specifications should restrict to printable ASCII or specify exact Unicode code point sequences. Escaped characters in hash input are prohibited. Number representations with fraction or exponent parts should be avoided. These follow Jon Postel's principle.

## 5. Relationship to Digests of X.509 Values (Condensed)
JWK Thumbprints are analogous to digests of X.509 Subject Public Key Info (SPKI) values, not complete certificates. They are computed over JSON rather than ASN.1.

## 6. IANA Considerations
This specification adds instructions for Designated Experts of the JOSE registries (JWK Types, Elliptic Curves, Parameters). IANA added a link to this specification in the Reference sections.
- **Requirement (MUST)**: For these registries, Designated Experts must either:
  (a) require that JWK member names and values use only printable ASCII characters excluding double quote and backslash (Unicode code points U+0021, U+0023–U+005B, U+005D–U+007E); or
  (b) if other code points are used, require that definitions specify exact Unicode code point sequences. Proposed registrations that use code points representable only as escaped characters must not be accepted.

## 7. Security Considerations (Condensed)
- The JSON Security and Unicode Comparison Security Considerations from JWS apply.
- Incorrect results may occur with esoteric or escaped characters; security impact is limited for public keys.
- JWK Thumbprint of a symmetric key may leak information; it should be concealed from unauthorized parties unless the hash function provides sufficient protection.
- Uniqueness of thumbprints relies on unambiguous JWK representations; implementations must validate correct key representations.
- Thumbprint comparison is not a reliable means of blacklisting keys (e.g., transformed keys).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Characters in member names and values MUST be represented without being escaped. | MUST | Section 3.3 |
| R2 | If members are JSON objects, their members MUST be lexicographically ordered. | MUST | Section 3.3 |
| R3 | Integer values in members MUST be represented as JSON numbers without fraction/exponent parts. | MUST | Section 3.3 |
| R4 | A cryptographic hash function must be chosen by the application. | must (application choice) | Section 3.4 |
| R5 | For IANA JOSE registries, Designated Experts must follow either (a) printable ASCII restriction or (b) exact Unicode sequence requirement and prohibit escaped characters. | MUST | Section 6 |
| R6 | Use of escaped characters in hash input JWKs is prohibited. | prohibition | Section 4 |
| R7 | Use of number representations with fraction or exponent parts in JWKs should be avoided. | SHOULD | Section 4 |

## Informative Annexes (Condensed)
- **Section 3.1 Example**: Demonstrates computation steps for an RSA key using SHA-256, resulting in base64url thumbprint `NzbLsXh8uDCcd-6MNwXF4W_7noWXFZAfHkxZsRGC9Xs`.
- **Section 4 Practical Considerations**: Discusses platform differences, avoiding non-ASCII and escaped characters, and integer-only numbers.
- **Section 5 Relationship to X.509**: JWK Thumbprints are analogous to SPKI digests, not full certificate digests.
- **Section 7 Security Considerations**: Warns about key transformation attacks, symmetric key leakage, and reliance on correct key representation for uniqueness.