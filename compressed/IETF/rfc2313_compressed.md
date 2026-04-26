# RFC 2313: PKCS #1: RSA Encryption Version 1.5
**Source**: Internet Society (IETF) | **Version**: 1.5 | **Date**: March 1998 | **Type**: Informational
**Original**: https://datatracker.ietf.org/doc/html/rfc2313

## Scope (Summary)
This document specifies a method for encrypting data using the RSA public-key cryptosystem, intended for digital signatures and digital envelopes as described in PKCS #7. It also defines syntax for RSA public and private keys, and three signature algorithms (MD2/RSA, MD4/RSA, MD5/RSA) for use in X.509/PEM certificates and other objects.

## Normative References
- FIPS PUB 46-1: Data Encryption Standard (January 1988)
- PKCS #6: Extended-Certificate Syntax (v1.5, November 1993)
- PKCS #7: Cryptographic Message Syntax (v1.5, November 1993)
- PKCS #8: Private-Key Information Syntax (v1.2, November 1993)
- RFC 1319: MD2 Message-Digest Algorithm (April 1992)
- RFC 1320: MD4 Message-Digest Algorithm (April 1992)
- RFC 1321: MD5 Message-Digest Algorithm (April 1992)
- RFC 1423: PEM Part III: Algorithms, Modes, and Identifiers (February 1993)
- X.208: ASN.1 (1988)
- X.209: BER (1988)
- X.411: Message Handling Systems (1988)
- X.509: Directory Authentication Framework (1988)
- [dBB92]: Den Boer & Bosselaers, CRYPTO '91
- [dBB93]: Den Boer & Bosselaers, EUROCRYPT '93
- [DO86]: Desmedt & Odlyzko, CRYPTO '85
- [Has88]: Hastad, SIAM J. Computing 17(2)
- [IM90]: I'Anson & Mitchell, CCR April 1990
- [Mer90]: Merkle, unpublished
- [Mil76]: Miller, J. CSS 13(3)
- [QC82]: Quisquater & Couvreur, Electronics Letters 18(21)
- [RSA78]: Rivest, Shamir, Adleman, CACM 21(2)

## Definitions and Abbreviations
- **AlgorithmIdentifier**: Type identifying an algorithm by OID and parameters (X.509).
- **ASN.1**: Abstract Syntax Notation One (X.208).
- **BER**: Basic Encoding Rules (X.209).
- **DES**: Data Encryption Standard (FIPS PUB 46-1).
- **MD2/MD4/MD5**: Message-digest algorithms (RFC 1319/1320/1321).
- **Modulus**: Integer product of two primes.
- **PEM**: Privacy-Enhanced Mail (RFC 1423).
- **RSA**: RSA public-key cryptosystem [RSA78].
- **Private key**: Modulus and private exponent.
- **Public key**: Modulus and public exponent.
- **Symbols (Section 4)**: Upper-case: octet/bit strings; lower-case: integers. Specific symbols: BT (block type), D (data), EB (encryption block), ED (encrypted data), M (message), MD (message digest), PS (padding string), S (signature), c (exponent), d (private exponent), e (public exponent), k (modulus length in octets), n (modulus), p, q (prime factors), x (integer encryption block), y (integer encrypted data), `||` (concatenation), `||X||` (length in octets of X).

## 5. General Overview
- Each entity **shall** generate a pair of keys: public and private.
- Encryption process **shall** be performed with one key; decryption with the other.
- Both processes transform octet string to octet string.
- Processes are inverses if one uses an entity’s public key and the other uses the same entity’s private key.
- Encryption/decryption can implement classic RSA transformations or variations with padding.

## 6. Key Generation
- Each entity **shall** select a positive integer **e** as its public exponent.
- Each entity **shall** privately and randomly select two distinct odd primes **p** and **q** such that gcd(p-1, e) = 1 and gcd(q-1, e) = 1.
- Public modulus **n** **shall** be product p*q.
- Private exponent **d** **shall** be a positive integer such that (d*e -1) is divisible by both p-1 and q-1.
- Modulus length in octets k **must** be at least 12 octets (to accommodate block formats).
- Notes:
  - Public exponent may be standardized (e.g., 3 or 65537 per X.509 Annex C).
  - Additional prime selection conditions for security are outside scope.

## 7. Key Syntax
### 7.1 Public-key syntax
- An RSA public key **shall** have ASN.1 type `RSAPublicKey`:
  ```
  RSAPublicKey ::= SEQUENCE {
    modulus INTEGER, -- n
    publicExponent INTEGER -- e
  }
  ```
- Fields: modulus = n; publicExponent = e. (Type per X.509.)

### 7.2 Private-key syntax
- An RSA private key **shall** have ASN.1 type `RSAPrivateKey`:
  ```
  RSAPrivateKey ::= SEQUENCE {
    version Version,
    modulus INTEGER, -- n
    publicExponent INTEGER, -- e
    privateExponent INTEGER, -- d
    prime1 INTEGER, -- p
    prime2 INTEGER, -- q
    exponent1 INTEGER, -- d mod (p-1)
    exponent2 INTEGER, -- d mod (q-1)
    coefficient INTEGER -- (inverse of q) mod p
  }
  Version ::= INTEGER
  ```
- Fields: version = 0 (for this document); modulus = n; publicExponent = e; privateExponent = d; prime1 = p; prime2 = q; exponent1 = d mod (p-1); exponent2 = d mod (q-1); coefficient = q⁻¹ mod p.
- Notes:
  - Extra values are for efficiency (Quisquater & Couvreur).
  - Public exponent included to derive public key from private key.

## 8. Encryption Process
- Input: octet string D (data), integer n (modulus), integer c (exponent). For public-key: c = e; for private-key: c = d.
- Output: octet string ED (encrypted data).
- Length of D **shall not** be more than k-11 octets (k ≥ 12).
- Steps: encryption-block formatting, octet-string-to-integer conversion, RSA computation, integer-to-octet-string conversion.

### 8.1 Encryption-block formatting
- EB = `00 || BT || PS || 00 || D`
- Block type BT **shall** be a single octet: 00, 01, or 02. For private-key: 00 or 01; for public-key: 02.
- Padding string PS **shall** consist of k-3-||D|| octets. For BT=00: all 00; BT=01: all FF; BT=02: pseudorandomly generated and nonzero.
- Leading 00 ensures integer < modulus.
- Notes: BT=01 recommended for private-key; BT=02 requires independent pseudorandom generation; PS ≥ 8 octets security condition.

### 8.2 Octet-string-to-integer conversion
- EB converted to integer x: `x = Σ 2^(8(k-i)) EB_i` (i=1..k). First octet most significant. Condition: 0 ≤ x < n.

### 8.3 RSA computation
- `y = x^c mod n`, 0 ≤ y < n.

### 8.4 Integer-to-octet-string conversion
- y converted to octet string ED of length k: `y = Σ 2^(8(k-i)) ED_i` (i=1..k). First octet most significant.

## 9. Decryption Process
- Input: ED (encrypted data), n, c. Public-key: c=e; private-key: c=d.
- Output: D (data). Error if length of ED ≠ k.
- Steps: octet-string-to-integer, RSA computation, integer-to-octet-string, encryption-block parsing.
- Errors: integer y not in [0, n); EB cannot be parsed unambiguously; PS < 8 octets or inconsistent with BT; decryption public-key and BT not 00/01, or private-key and BT not 02.

## 10. Signature Algorithms
- Three algorithms: MD2 with RSA, MD4 with RSA, MD5 with RSA.
- Signature process performed with private key; verification with public key.
- Input: message M (octet string), signer’s private key. Output: signature S (bit string).
- Verification: input message M, signer’s public key, signature S. Output success/failure.
- Note: Signatures represented as bit strings per X.509 SIGNED macro.

### 10.1 Signature Process (shall)
1. **Message digesting**: Digest M with selected algorithm → MD.
2. **Data encoding**: Combine MD and digest algorithm identifier into `DigestInfo` (ASN.1 SEQUENCE), BER-encode → D.
   ```
   DigestInfo ::= SEQUENCE {
     digestAlgorithm DigestAlgorithmIdentifier,
     digest Digest
   }
   DigestAlgorithmIdentifier ::= AlgorithmIdentifier
   Digest ::= OCTET STRING
   ```
   - digestAlgorithm identifies the message-digest algorithm (OIDs: md2, md4, md5; parameters NULL).
3. **RSA encryption**: Encrypt D with private key (block type 01) → ED.
4. **Octet-string-to-bit-string conversion**: ED → S (most significant bit of first octet becomes first bit of S).

### 10.2 Verification Process (shall)
1. **Bit-string-to-octet-string conversion**: S → ED (error if length not multiple of 8).
2. **RSA decryption**: Decrypt ED with public key → D (error if block type ≠ 01).
3. **Data decoding**: BER-decode D → DigestInfo, separate MD and algorithm identifier (error if algorithm not MD2/MD4/MD5).
4. **Message digesting and comparison**: Digest M with selected algorithm → MD'. Success if MD' == MD; else failure.

## 11. Object Identifiers
- `pkcs-1` OID: `{ iso(1) member-body(2) US(840) rsadsi(113549) pkcs(1) 1 }`
- `rsaEncryption` OID: `{ pkcs-1 1 }` — identifies RSA public/private keys (Section 7) and encryption/decryption (Sections 8-9). Used in AlgorithmIdentifier with parameters NULL.
- `md2WithRSAEncryption` OID: `{ pkcs-1 2 }`
- `md4WithRSAEncryption` OID: `{ pkcs-1 3 }`
- `md5WithRSAEncryption` OID: `{ pkcs-1 4 }`
- These three identify signature/verification processes (Section 10). Used in AlgorithmIdentifier with parameters NULL.
- Note: X.509’s `rsa` OID also identifies public keys but not private keys or processes; public keys are compatible.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Each entity shall generate a pair of keys: public and private. | shall | Section 5 |
| R2 | Encryption/decryption shall be performed with one key for encryption and the other for decryption. | shall | Section 5 |
| R3 | Each entity shall select a positive integer e as public exponent. | shall | Section 6 |
| R4 | Each entity shall privately and randomly select two distinct odd primes p, q such that gcd(p-1,e)=1 and gcd(q-1,e)=1. | shall | Section 6 |
| R5 | Public modulus n shall be product p*q. | shall | Section 6 |
| R6 | Private exponent d shall be positive integer such that (d*e-1) divisible by p-1 and q-1. | shall | Section 6 |
| R7 | Modulus length k must be at least 12 octets. | must | Section 6 |
| R8 | RSA public key shall have ASN.1 type RSAPublicKey as defined. | shall | Section 7.1 |
| R9 | RSA private key shall have ASN.1 type RSAPrivateKey as defined. | shall | Section 7.2 |
| R10 | Length of data D shall not be more than k-11 octets. | shall | Section 8 |
| R11 | Encryption block EB shall be formatted as 00 \|\| BT \|\| PS \|\| 00 \|\| D. | shall | Section 8.1 |
| R12 | Block type BT shall be single octet: 00, 01, or 02. For private-key: 00 or 01; for public-key: 02. | shall | Section 8.1 |
| R13 | Padding string PS shall consist of k-3-\|\|D\|\| octets: for BT=00 all 00, BT=01 all FF, BT=02 pseudorandom nonzero. | shall | Section 8.1 |
| R14 | Encryption block EB shall be converted to integer x by Formula (2) (most significant first octet). | shall | Section 8.2 |
| R15 | RSA computation: y = x^c mod n. | shall | Section 8.3 |
| R16 | Integer y shall be converted to octet string ED of length k by Formula (3). | shall | Section 8.4 |
| R17 | Decryption input shall be ED, n, c; error if length of ED ≠ k. | shall | Section 9 |
| R18 | ED shall be converted to integer y by Formula (3); error if y not in [0, n). | shall | Section 9.1 |
| R19 | RSA computation: x = y^c mod n. | shall | Section 9.2 |
| R20 | Integer x shall be converted to EB of length k by Formula (2). | shall | Section 9.3 |
| R21 | EB shall be parsed into BT, PS, D per Equation (1); errors for ambiguous parsing, PS < 8 or inconsistent, wrong BT for operation. | shall | Section 9.4 |
| R22 | Signature process input: message M and signer’s private key; output: signature S (bit string). | shall | Section 10.1 |
| R23 | Message M shall be digested with selected algorithm → MD. | shall | Section 10.1.1 |
| R24 | MD and digest algorithm identifier shall be combined into DigestInfo ASN.1 value, BER-encoded → D. | shall | Section 10.1.2 |
| R25 | Data D shall be encrypted with private key (block type 01) → ED. | shall | Section 10.1.3 |
| R26 | ED shall be converted to bit string S (most significant bit of first octet becomes first bit of S). | shall | Section 10.1.4 |
| R27 | Verification input: M, public key, S; output success/failure. | shall | Section 10.2 |
| R28 | S shall be converted to ED (error if bit length not multiple of 8). | shall | Section 10.2.1 |
| R29 | ED shall be decrypted with public key → D (error if block type ≠ 01). | shall | Section 10.2.2 |
| R30 | D shall be BER-decoded to DigestInfo; separate MD and algorithm identifier (error if algorithm not MD2/MD4/MD5). | shall | Section 10.2.3 |
| R31 | Message M shall be digested with selected algorithm → MD'; verification succeeds if MD' == MD, fails otherwise. | shall | Section 10.2.4 |

## Informative Annexes (Condensed)
- **Security Considerations**: Discussed throughout the memo.
- **Revision History**: Versions 1.0-1.3 distributed to RSA PKCS meetings; Version 1.4 (June 3, 1991) initial public release; Version 1.5 (this document) includes editorial changes, adds MD4/RSA signature, and md4WithRSAEncryption OID.
- **Acknowledgements**: Based on contribution of RSA Laboratories; attribution required.