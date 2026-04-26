# RFC 5480: Elliptic Curve Cryptography Subject Public Key Information
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: March 2009 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc5480.txt (or URL as provided)

## Scope (Summary)
This document specifies the syntax and semantics for the Subject Public Key Information field in X.509 certificates supporting Elliptic Curve Cryptography (ECC). It updates RFC 3279 by defining encoding formats for public keys used with ECDSA, ECDH, and ECMQV algorithms, and provides two methods (unrestricted and restricted) for specifying algorithms associated with the public key.

## Normative References
- [FIPS180-3] NIST FIPS 180-3: Secure Hash Standard, October 2008.
- [FIPS186-3] NIST FIPS 186-3 (draft): Digital Signature Standard, November 2008.
- [MUSTSHOULD] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [PKI] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [PKI-ALG] Bassham, L., et al., "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3279, April 2002.
- [RSAOAEP] Schaad, J., et al., "Additional Algorithms and Identifiers for RSA Cryptography for use in the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 4055, June 2005.
- [SEC1] Standards for Efficient Cryptography Group (SECG), "SEC 1: Elliptic Curve Cryptography", Version 1.0, September 2000.
- [X9.62] ANSI X9.62-2005: The Elliptic Curve Digital Signature Algorithm (ECDSA), 2005.
- [X.680] ITU-T X.680 (2002) | ISO/IEC 8824-1:2002, Abstract Syntax Notation One.

## Definitions and Abbreviations
- **ECDSA**: Elliptic Curve Digital Signature Algorithm.
- **ECDH**: Elliptic Curve Diffie-Hellman (key agreement family).
- **ECMQV**: Elliptic Curve Menezes-Qu-Vanstone (key agreement family).
- **ECPoint**: OCTET STRING representing an ECC public key.
- **ECParameters**: CHOICE type for elliptic curve domain parameters (namedCurve, implicitCurve, specifiedCurve).
- **SubjectPublicKeyInfo**: ASN.1 SEQUENCE containing algorithm identifier and public key BIT STRING.
- **Key words**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (as per RFC 2119).

## Subject Public Key Information Fields
### 2.1 Elliptic Curve Cryptography Public Key Algorithm Identifiers
- **id-ecPublicKey**: unrestricted algorithm identifier; **MUST be supported**. Used with ECDSA and when key usage is unrestricted.
- **id-ecDH**: restricted to ECDH; **MAY be supported**.
- **id-ecMQV**: restricted to ECMQV; **MAY be supported**.

### 2.1.1 Unrestricted Algorithm Identifier and Parameters
- **id-ecPublicKey** OID: `{iso(1) member-body(2) us(840) ansi-X9-62(10045) keyType(2) 1}`
- **ECParameters** MUST always be present.
  - **namedCurve** (OBJECT IDENTIFIER) **MUST be supported**.
  - **implicitCurve** (NULL) **MUST NOT be used**.
  - **specifiedCurve** (SpecifiedECDomain) **MUST NOT be used**.
- If elliptic curve domain parameters are not present, clients **MUST reject** the certificate.
- Any future additions to ECParameters must be coordinated with ANSI X9.

#### 2.1.1.1 Named Curves (NIST-recommended)
- Fifteen OIDs published for NIST curves (secp192r1, sect163k1, sect163r2, secp224r1, sect233k1, sect233r1, secp256r1, sect283k1, sect283r1, secp384r1, sect409k1, sect409r1, secp521r1, sect571k1, sect571r1). Cross-references to [X9.62], [PKI-ALG], and [FIPS186-3] naming conventions noted.

### 2.1.2 Restricted Algorithm Identifiers and Parameters
- **id-ecDH**: `{iso(1) identified-organization(3) certicom(132) schemes(1) ecdh(12)}`
- **id-ecMQV**: `{iso(1) identified-organization(3) certicom(132) schemes(1) ecmqv(13)}`
- Parameters are always ECParameters and **MUST always be present**.

### 2.2 Subject Public Key
- **ECPoint** ::= OCTET STRING.
- Implementations **MUST support** uncompressed form (first octet 0x04) and **MAY support** compressed form (first octet 0x02 or 0x03).
- Hybrid form **MUST NOT be used**.
- Public key **MUST be rejected** if first octet is any value other than 0x04, 0x02, or 0x03.
- Mapping from OCTET STRING to BIT STRING as per [SEC1] Sections 2.3.1 and 2.3.2.

## Key Usage Bits
### CA Certificates (id-ecPublicKey)
- Any combination of `digitalSignature`, `nonRepudiation`, `keyAgreement`, `keyCertSign`, `cRLSign` **MAY be present**.
- If `keyAgreement` asserted, then `encipherOnly` or `decipherOnly` **MAY be present**.
- **RECOMMENDED**: If `keyCertSign` or `cRLSign` present, then `keyAgreement`, `encipherOnly`, and `decipherOnly` **SHOULD NOT be present**.

### EE Certificates (id-ecPublicKey)
- Any combination of `digitalSignature`, `nonRepudiation`, `keyAgreement` **MAY be present**.
- If `keyAgreement` asserted, then `encipherOnly` or `decipherOnly` **MAY be present**.

### Certificates with id-ecDH or id-ecMQV
- `keyAgreement` **MUST be present**.
- `encipherOnly` or `decipherOnly` **MAY be present** (one of them).
- `digitalSignature`, `nonRepudiation`, `keyTransport`, `keyCertSign`, `cRLSign` **MUST NOT be present**.

## Security Considerations
- CAs must consider public key size, hash algorithm, and curve to provide equivalent security bits. Recommended combinations provided in a table (see requirements summary for the recommended minimum security bits, key sizes, hash algorithms, and curves).
- Risks of using non-well-known curves: may not satisfy MOV condition or may be vulnerable to Anomalous attack. Public key arithmetic validation required per [SP800-56A].
- Use of MD2 and MD5 discouraged for new applications; still permissible for verifying existing signatures.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | id-ecPublicKey MUST be supported. | MUST | Section 2.1 |
| R2 | id-ecDH MAY be supported. | MAY | Section 2.1 |
| R3 | id-ecMQV MAY be supported. | MAY | Section 2.1 |
| R4 | ECParameters MUST always be present for id-ecPublicKey. | MUST | Section 2.1.1 |
| R5 | namedCurve in ECParameters MUST be supported. | MUST | Section 2.1.1 |
| R6 | implicitCurve MUST NOT be used. | MUST NOT | Section 2.1.1 |
| R7 | specifiedCurve MUST NOT be used. | MUST NOT | Section 2.1.1 |
| R8 | Clients MUST reject certificate if elliptic curve domain parameters are absent. | MUST | Section 2.1.1 |
| R9 | Uncompressed ECC public key form MUST be supported. | MUST | Section 2.2 |
| R10 | Compressed ECC public key form MAY be supported. | MAY | Section 2.2 |
| R11 | Hybrid ECC public key form MUST NOT be used. | MUST NOT | Section 2.2 |
| R12 | Public key MUST be rejected if first octet is not 0x04, 0x02, or 0x03. | MUST | Section 2.2 |
| R13 | ECParameters MUST always be present for id-ecDH and id-ecMQV. | MUST | Section 2.1.2 |
| R14 | For id-ecDH/id-ecMQV certificates, keyAgreement MUST be present. | MUST | Section 3 |
| R15 | For id-ecDH/id-ecMQV certificates, encipherOnly or decipherOnly MAY be present. | MAY | Section 3 |
| R16 | For id-ecDH/id-ecMQV certificates, digitalSignature, nonRepudiation, keyTransport, keyCertSign, cRLSign MUST NOT be present. | MUST NOT | Section 3 |
| R17 | For CA certificates with id-ecPublicKey, any combination of digitalSignature/nonRepudiation/keyAgreement/keyCertSign/cRLSign MAY be present. | MAY | Section 3 |
| R18 | For CA certificates with id-ecPublicKey and keyAgreement, encipherOnly/decipherOnly MAY be present. | MAY | Section 3 |
| R19 | RECOMMENDED: If keyCertSign or cRLSign present, then keyAgreement/encipherOnly/decipherOnly SHOULD NOT be present. | SHOULD NOT | Section 3 |
| R20 | For EE certificates with id-ecPublicKey, any combination of digitalSignature/nonRepudiation/keyAgreement MAY be present. | MAY | Section 3 |
| R21 | For EE certificates with id-ecPublicKey and keyAgreement, encipherOnly/decipherOnly MAY be present. | MAY | Section 3 |

## Informative Annexes (Condensed)
- **Appendix A: ASN.1 Module**: Defines the complete ASN.1 module (PKIX1Algorithms2008) including OIDs for message digest algorithms (MD2, MD5, SHA-1/224/256/384/512), public key algorithms (RSA, DSA, DH, KEA, and ECC), signature algorithms (RSA with MD/HASH, DSA with SHA, ECDSA with SHA), signature values (DSA-Sig-Value, ECDSA-Sig-Value), and the fifteen NIST elliptic curve OIDs. This module supersedes the ASN.1 from RFC 3279; implementers should use this module. Note that PER encoding differences may arise compared to the X9.62 module.
- **Security Considerations Table (interoperability recommendations)**:
  - For 80-bit security: secp192r1 with SHA-256.
  - For 112-bit security: secp224r1 with SHA-256.
  - For 128-bit security: secp256r1 with SHA-256.
  - For 192-bit security: secp384r1 with SHA-384.
  - For 256-bit security: secp521r1 with SHA-512.
  - Larger hash values than necessary are discouraged on constrained devices.