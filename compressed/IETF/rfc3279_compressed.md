# RFC 3279: Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: April 2002 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/html/rfc3279

## Scope (Summary)
This document specifies algorithm identifiers and ASN.1 encoding formats for digital signatures and subject public keys used in the Internet X.509 PKI. It supplements RFC 3280 and defines the contents of the `signatureAlgorithm`, `signatureValue`, `signature`, and `subjectPublicKeyInfo` fields within X.509 certificates and CRLs.

## Normative References
- [FIPS 180-1] Secure Hash Standard, April 1995
- [FIPS 186-2] Digital Signature Standard, January 2000
- [P1363] IEEE P1363, 2001
- [RFC 1034] Domain Names - Concepts and Facilities, STD 13
- [RFC 1319] The MD2 Message-Digest Algorithm
- [RFC 1321] The MD5 Message-Digest Algorithm
- [RFC 1422] Privacy Enhancement for Internet Electronic Mail: Part II
- [RFC 1423] Privacy Enhancement for Internet Electronic Mail: Part III
- [RFC 2119] Key Words for Use in RFCs to Indicate Requirement Levels
- [RFC 2313] PKCS #1: RSA Encryption Version 1.5
- [RFC 3174] US Secure Hash Algorithm 1 (SHA1)
- [RFC 3280] Internet X.509 Public Key Infrastructure Certificate and CRL Profile
- [SDN.701r] Message Security Protocol 4.0
- [X9.42] Public Key Cryptography for The Financial Services Industry: Agreement of Symmetric Keys Using Discrete Logarithm Cryptography
- [X9.62] Public Key Cryptography For The Financial Services Industry: The Elliptic Curve Digital Signature Algorithm (ECDSA)
- [X9.63] Key Agreement and Key Transport Using Elliptic Curve Cryptography

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One, as defined in [X.208] and [X.660]
- **CA**: Certification Authority
- **CRL**: Certificate Revocation List
- **DH**: Diffie-Hellman key agreement algorithm
- **DSA**: Digital Signature Algorithm (FIPS 186)
- **ECDH**: Elliptic Curve Diffie-Hellman
- **ECDSA**: Elliptic Curve Digital Signature Algorithm
- **KEA**: Key Exchange Algorithm
- **OID**: Object Identifier
- **PKI**: Public Key Infrastructure
- **RSA**: Rivest-Shamir-Adelman asymmetric encryption algorithm

## 1. Introduction
- **Normative Keywords**: The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC 2119].
- **Compliance**: Implementations of this specification MUST also conform to RFC 3280.
- **Scope**: Defines the contents of `signatureAlgorithm`, `signatureValue`, `signature`, and `subjectPublicKeyInfo` fields within Internet X.509 certificates and CRLs.
- **Identifies one-way hash functions** for use with digital signatures: MD2, MD5, SHA-1.
- **Specifies encoding of signatures** generated with RSA, DSA, and ECDSA.
- **Specifies encoding of public keys** for RSA, DSA, DH, KEA, ECDSA, and ECDH.

## 2. Algorithm Support
- **Conforming CAs and applications MUST**, at a minimum, support digital signatures and public keys for one of the specified algorithms.
- **When using any of the algorithms identified in this specification, conforming CAs and applications MUST support them as described.**

### 2.1 One-Way Hash Functions
- **SHA-1** is the preferred one-way hash function.
- MD2 and MD5 are included for legacy compatibility (PEM, etc.).
- Hash function OIDs:
  - `md2 OBJECT IDENTIFIER ::= { iso(1) member-body(2) US(840) rsadsi(113549) digestAlgorithm(2) 2 }`
  - `md5 OBJECT IDENTIFIER ::= { iso(1) member-body(2) US(840) rsadsi(113549) digestAlgorithm(2) 5 }`
  - `id-sha1 OBJECT IDENTIFIER ::= { iso(1) identified-organization(3) oiw(14) secsig(3) algorithms(2) 26 }` (used in PKCS#1 encoding)

#### 2.1.1 MD2 One-Way Hash Function
- **Informative**: MD2 produces a 128-bit hash. An attack by Rogier and Chauvaud can nearly find collisions. Use of MD2 for new applications is discouraged; it remains reasonable for verifying existing signatures.

#### 2.1.2 MD5 One-Way Hash Function
- **Informative**: MD5 produces a 128-bit hash. Pseudo-collisions have been found. Use of MD5 for new applications is discouraged; it remains reasonable for verifying existing signatures.

#### 2.1.3 SHA-1 One-Way Hash Function
- **Informative**: SHA-1 produces a 160-bit hash. Defined in [FIPS 180-1] and [RFC 3174].

### 2.2 Signature Algorithms
- **The algorithm identifier** appears in the `signatureAlgorithm` field of Certificate or CertificateList.
- **Signature algorithms are always used in conjunction with a one-way hash function.**
- **OIDs** are provided for RSA, DSA, and ECDSA.
- **The signature value** is ASN.1 encoded as a BIT STRING.

#### 2.2.1 RSA Signature Algorithm
- Three signature algorithms: RSA with MD2, MD5, or SHA-1.
- Encoding per PKCS #1 [RFC 2313]; uses padding and data encoding step.
- When encoding, the OIDs for the hash functions (`md2`, `md5`, `id-sha1`) MUST be used.
- OIDs:
  - `md2WithRSAEncryption OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 2 }`
  - `md5WithRSAEncryption OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 4 }`
  - `sha-1WithRSAEncryption OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-1(1) 5 }`
- **When any of these three OIDs appears in AlgorithmIdentifier, the parameters component SHALL be the ASN.1 type NULL.**

#### 2.2.2 DSA Signature Algorithm
- DSA used with SHA-1 per [FIPS 186].
- OID: `id-dsa-with-sha1 OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) x9-57 (10040) x9cm(4) 3 }`
- **When id-dsa-with-sha1 appears, the encoding SHALL omit the parameters field.**
- **The DSA parameters in the subjectPublicKeyInfo of the issuer SHALL apply to signature verification.**
- Signature encoded as `Dss-Sig-Value ::= SEQUENCE { r INTEGER, s INTEGER }`.

#### 2.2.3 ECDSA Signature Algorithm
- ECDSA per [X9.62] with SHA-1.
- OIDs:
  - `ansi-X9-62 OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) 10045 }`
  - `id-ecSigType OBJECT IDENTIFIER ::= { ansi-X9-62 signatures(4) }`
  - `ecdsa-with-SHA1 OBJECT IDENTIFIER ::= { id-ecSigType 1 }`
- **When ecdsa-with-SHA1 appears, the encoding MUST omit the parameters field. (The AlgorithmIdentifier SHALL be a SEQUENCE of one component: the OID.)**
- **Elliptic curve parameters in the subjectPublicKeyInfo of the issuer SHALL apply to signature verification.**
- Signature encoded as `Ecdsa-Sig-Value ::= SEQUENCE { r INTEGER, s INTEGER }`.

### 2.3 Subject Public Key Algorithms
- **Certificates conforming to [RFC 3280] may convey a public key for any public key algorithm.**
- **Conforming CAs MUST use the identified OIDs when issuing certificates containing public keys for these algorithms.**
- **Conforming applications supporting any of these algorithms MUST, at a minimum, recognize the OID identified in this section.**

#### 2.3.1 RSA Keys
- OID: `rsaEncryption OBJECT IDENTIFIER ::= { pkcs-1 1 }` (where `pkcs-1` = `{ iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) 1 }`)
- **parameters field MUST have ASN.1 type NULL.**
- Public key encoded as:
  ```
  RSAPublicKey ::= SEQUENCE {
      modulus            INTEGER,    -- n
      publicExponent     INTEGER  }  -- e
  ```
- The DER-encoded `RSAPublicKey` becomes the value of the BIT STRING `subjectPublicKey`.
- **keyUsage extension**: For end-entity certificates, any combination of `digitalSignature`, `nonRepudiation`, `keyEncipherment`, `dataEncipherment` MAY be present. For CA/CRL issuer certificates, additionally `keyCertSign` and `cRLSign` MAY be present.
  - **RECOMMENDED**: if `keyCertSign` or `cRLSign` is present, both `keyEncipherment` and `dataEncipherment` SHOULD NOT be present.

#### 2.3.2 DSA Signature Keys
- OID: `id-dsa OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) x9-57(10040) x9cm(4) 1 }`
- **Domain parameters (p, q, g) are optional.** When omitted, the parameters component MUST be omitted entirely (AlgorithmIdentifier SEQUENCE of one component: OID).
- If parameters are present, use `Dss-Parms ::= SEQUENCE { p INTEGER, q INTEGER, g INTEGER }`.
- **The AlgorithmIdentifier within subjectPublicKeyInfo is the only place within a certificate where the parameters may be used.**
- If parameters are omitted from subjectPublicKeyInfo, then:
  - If CA signed with DSA, the CA's DSA parameters apply.
  - If CA signed with a non-DSA algorithm and parameters not available elsewhere, clients MUST reject the certificate.
- Public key encoded as: `DSAPublicKey ::= INTEGER` (the public key Y).
- **keyUsage extension**: For end-entity, only `digitalSignature` and `nonRepudiation` MAY be present. For CA/CRL issuer, additionally `keyCertSign` and `cRLSign` MAY be present.

#### 2.3.3 Diffie-Hellman Key Exchange Keys
- OID: `dhpublicnumber OBJECT IDENTIFIER ::= { iso(1) member-body(2) us(840) ansi-x942(10046) number-type(2) 1 }`
- Parameters are of type `DomainParameters`:
  ```
  DomainParameters ::= SEQUENCE {
      p       INTEGER,           -- odd prime, p=jq+1
      g       INTEGER,           -- generator
      q       INTEGER,           -- factor of p-1
      j       INTEGER OPTIONAL,
      validationParms ValidationParms OPTIONAL }
  ValidationParms ::= SEQUENCE {
      seed             BIT STRING,
      pgenCounter      INTEGER }
  ```
- If either `pgenCounter` or `seed` is provided, the other MUST be present.
- Public key encoded as: `DHPublicKey ::= INTEGER` (y = g^x mod p).
- **keyUsage extension**: If present, MUST assert `keyAgreement`, MAY assert `encipherOnly` or `decipherOnly`, and MUST NOT assert both `encipherOnly` and `decipherOnly`.

#### 2.3.4 KEA Public Keys
- OID: `id-keyExchangeAlgorithm OBJECT IDENTIFIER ::= { 2 16 840 1 101 2 1 1 22 }`
- **Parameters field** in AlgorithmIdentifier SHALL contain an 80-bit parameter identifier (domain identifier) as an OCTET STRING. The domain identifier is computed by:
  1. DER-encoding KEA domain parameters (p,q,g) using `Dss-Parms`.
  2. SHA-1 hash the result.
  3. XOR high 80 bits with low 80 bits to get 80-bit value.
- Public key y is conveyed as a BIT STRING with zero unused bits, encoded such that MSB of y is MSB of BIT STRING value field.
- **keyUsage extension**: If present, MUST assert `keyAgreement`, MAY assert `encipherOnly` or `decipherOnly`, and MUST NOT assert both.

#### 2.3.5 ECDSA and ECDH Keys
- Use the same OIDs and parameter encodings.
- **Algorithm identifier**: `id-ecPublicKey OBJECT IDENTIFIER ::= { id-publicKeyType 1 }`, where `id-publicKeyType` = `{ ansi-X9-62 keyType(2) }`.
- **Parameters** may be inherited (implicitlyCA = NULL), named curve (object identifier), or explicit (ECParameters).
  ```
  EcpkParameters ::= CHOICE {
      ecParameters  ECParameters,
      namedCurve    OBJECT IDENTIFIER,
      implicitlyCA  NULL }
  ECParameters ::= SEQUENCE {
      version   ECPVer,          -- version is always 1
      fieldID   FieldID,
      curve     Curve,
      base      ECPoint,
      order     INTEGER,
      cofactor  INTEGER OPTIONAL }
  Curve ::= SEQUENCE {
      a         FieldElement,
      b         FieldElement,
      seed      BIT STRING OPTIONAL }
  FieldElement ::= OCTET STRING
  ECPoint ::= OCTET STRING
  FieldID ::= SEQUENCE {
      fieldType   OBJECT IDENTIFIER,
      parameters   ANY DEFINED BY fieldType }
  ```
- **Implementations MUST support the uncompressed form of ECPoint; MAY support compressed form.**
- **If parameters are inherited (implicitlyCA) and CA signed with ECDSA, then the CA's ECDSA parameters apply. If CA signed with a non-ECDSA algorithm, clients MUST not make use of the elliptic curve public key.**
- For prime fields: `prime-field OBJECT IDENTIFIER ::= { id-fieldType 1 }` with `Prime-p ::= INTEGER`.
- For characteristic-2 fields: `characteristic-two-field OBJECT IDENTIFIER ::= { id-fieldType 2 }` with `Characteristic-two ::= SEQUENCE { m INTEGER, basis OBJECT IDENTIFIER, parameters ANY DEFINED BY basis }`. Basis types: `gnBasis`, `tpBasis` (with `Trinomial ::= INTEGER`), `ppBasis` (with `Pentanomial ::= SEQUENCE { k1 INTEGER, k2 INTEGER, k3 INTEGER }`).
- **keyUsage extension** for end-entity certificates: any combination of `digitalSignature`, `nonRepudiation`, `keyAgreement` MAY be present. If `keyAgreement` is present, MAY also have `encipherOnly` or `decipherOnly` (but not both).
- For CA/CRL issuer certificates: additionally `keyCertSign` and `cRLSign` MAY be present.
  - **RECOMMENDED**: if `keyCertSign` or `cRLSign` are present, `keyAgreement`, `encipherOnly`, and `decipherOnly` SHOULD NOT be present.
- Named curves from ANSI X9.62 are listed in the ASN.1 module (see Section 3).

## 3. ASN.1 Module (Condensed)
- Module name: `PKIX1Algorithms88 { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-mod-pkix1-algorithms(17) }`
- All OIDs and type definitions from sections 2.1 through 2.3 are encoded here.
- Key additional definitions:
  - Elliptic curve OIDs for prime and c-Two curves (see full list in original document).
  - The module is provided in the original text for implementers.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST also conform to RFC 3280. | MUST | Section 1 |
| R2 | Conforming CAs/applications MUST at minimum support one algorithm. | MUST | Section 2 |
| R3 | When using algorithms from this spec, conforming CAs/applications MUST support them as described. | MUST | Section 2 |
| R4 | For RSA signature OIDs (md2WithRSAEncryption, md5WithRSAEncryption, sha-1WithRSAEncryption), the parameters field SHALL be NULL. | SHALL | 2.2.1 |
| R5 | For id-dsa-with-sha1, the parameters field SHALL be omitted. | SHALL | 2.2.2 |
| R6 | DSA signature verification uses the issuer's DSA parameters from subjectPublicKeyInfo. | SHALL | 2.2.2 |
| R7 | DSA signature encoded as Dss-Sig-Value SEQUENCE. | SHALL | 2.2.2 |
| R8 | For ecdsa-with-SHA1, the parameters field MUST be omitted. | MUST | 2.2.3 |
| R9 | ECDSA signature verification uses issuer's EC parameters from subjectPublicKeyInfo. | SHALL | 2.2.3 |
| R10 | ECDSA signature encoded as Ecdsa-Sig-Value SEQUENCE. | MUST | 2.2.3 |
| R11 | When rsaEncryption OID used, parameters field MUST be NULL. | MUST | 2.3.1 |
| R12 | RSA public key encoded as RSAPublicKey SEQUENCE. | MUST | 2.3.1 |
| R13 | DSA public key parameters: if omitted from subjectPublicKeyInfo, issuer's DSA params apply if CA signed with DSA; if CA signed with non-DSA and params not available, clients MUST reject. | MUST/SHALL | 2.3.2 |
| R14 | DSA public key encoded as DSAPublicKey INTEGER. | MUST | 2.3.2 |
| R15 | For DH public key, if either seed or pgenCounter supplied, both MUST be present. | MUST | 2.3.3 |
| R16 | DH public key encoded as DHPublicKey INTEGER. | MUST | 2.3.3 |
| R17 | DH keyUsage: MUST assert keyAgreement; MAY assert encipherOnly or decipherOnly; MUST NOT assert both. | MUST/MAY/SHALL | 2.3.3 |
| R18 | KEA public key parameters SHALL contain 80-bit domain identifier (OCTET STRING). | SHALL | 2.3.4 |
| R19 | ECDSA/ECDH public key MUST use id-ecPublicKey OID. | MUST | 2.3.5 |
| R20 | Implementations MUST support uncompressed ECPoint; MAY support compressed. | MUST/MAY | 2.3.5 |
| R21 | If EC parameters inherited (implicitlyCA) and CA signed with non-ECDSA, clients MUST NOT use the public key. | MUST NOT | 2.3.5 |
| R22 | ECDSA/ECDH keyUsage: end-entity MAY have digitalSignature, nonRepudiation, keyAgreement; if keyAgreement, MAY have encipherOnly or decipherOnly (not both). | MAY/SHALL NOT | 2.3.5 |
| R23 | CA certificates with EC key: additionally keyCertSign, cRLSign; RECOMMENDED not to combine keyAgreement with keyCertSign/cRLSign. | MAY/RECOMMENDED | 2.3.5 |

## Security Considerations (Condensed)
- Key size selection is critical; this specification does not constrain key sizes.
- Selection of elliptic curves impacts strength; use of well-known named curves (e.g., from ANSI X9.62) is sound.
- Refer to RFC 3280 security considerations.