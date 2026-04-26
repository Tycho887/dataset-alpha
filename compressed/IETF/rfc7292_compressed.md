# RFC 7292: PKCS #12: Personal Information Exchange Syntax v1.1
**Source**: IETF (IESG) | **Version**: v1.1 (RFC 7292) | **Date**: July 2014 | **Type**: Informational  
**Original**: http://www.rfc-editor.org/info/rfc7292

## Scope (Summary)
PKCS #12 v1.1 defines a transfer syntax for personal identity information — private keys, certificates, secrets, and extensions — enabling import/export between platforms. It supports multiple privacy/integrity modes (public-key and password-based) and is an IETF republication of the RSA Laboratories PKCS #12 v1.1.

## Normative References
- [2] ISO/IEC 8824-1:2008 (ASN.1 basic notation)
- [3] ISO/IEC 8824-2:2008 (ASN.1 information object specification)
- [4] ISO/IEC 8824-3:2008 (ASN.1 constraint specification)
- [5] ISO/IEC 8824-4:2008 (ASN.1 parameterization)
- [6] ISO/IEC 8825-1:2008 (BER/CER/DER)
- [7] ISO/IEC 9594-2:1997 (Directory models)
- [8] ISO/IEC 9594-8:1997 (Authentication framework)
- [10] NIST FIPS 180-4 (Secure Hash Standard)
- [11] NIST FIPS 198-1 (HMAC)
- [12] NIST SP 800-132 (Password-based key derivation)
- [13] RSA PKCS #5 v2.1 (Password-Based Encryption)
- [14] RSA PKCS #7 v1.5 (Cryptographic Message Syntax)
- [15] RSA PKCS #8 v1.2 (Private-Key Information Syntax)
- [16] RSA PKCS #12 v1.1 (original)
- [17] Rivest & Lampson (SDSI)
- [20] RFC 2104 (HMAC)
- [21] RFC 2315 (PKCS #7 v1.5)
- [22] RFC 2898 (PKCS #5 v2.0)
- [23] RFC 2985 (PKCS #9)
- [24] RFC 5958 (Asymmetric Key Packages)
- Additional references [1], [9], [18], [19], [25] for MD2, MD5, and HMAC-MD5 security.

## Definitions and Abbreviations
- **AlgorithmIdentifier**: ASN.1 type identifying an algorithm by OID and parameters (per [8]).
- **ASN.1**: Abstract Syntax Notation One (per [2]-[5]).
- **Attribute**: ASN.1 type with OID and value (per [7]).
- **Certificate**: Digitally signed binding of public key to identity (per [8] or [17]).
- **CRL**: Certificate Revocation List (per [8]).
- **ContentInfo**: ASN.1 type holding data, possibly cryptographically protected (per [21][14]).
- **DER**: Distinguished Encoding Rules (per [6]).
- **Destination platform**: Final target for personal information.
- **DigestInfo**: ASN.1 type for message digest (per [21][14]).
- **Encryption Key Pair (DestEncK)**: For public-key privacy mode; public half PDestEncK/TPDestEncK, private half VDestEncK.
- **Export/Import time**: Times of reading/writing personal information to/from PDU.
- **MAC**: Message Authentication Code (collision-resistant, keyed).
- **Object Identifier**: Unique integer sequence (ASN.1 primitive).
- **PFX**: Top-level exchange PDU; sometimes expanded as Personal Information Exchange.
- **Platform**: Machine/OS/application combination.
- **PDU**: Protocol Data Unit in machine-independent format.
- **Shrouding**: Encryption of private keys, possibly policy-bound.
- **Signature Key Pair (SrcSigK)**: For public-key integrity mode; public half PSrcSigK/TPSrcSigK, private half VSrcSigK.
- **Source platform**: Origin of personal information.

## 1. Introduction
- Republication of PKCS #12 v1.1 from RSA Laboratories; change control transferred to IETF.
- Describes transfer syntax for private keys, certificates, secrets, extensions.
- Supports direct transfer under privacy and integrity modes: public-key and password-based.
- Builds on PKCS #8 by including ancillary identity information and public-key privacy/integrity.

### 1.1 Changes from PKCS #12 Version 1
- Addition of hash algorithms.
- Incorporation of Technical Corrigendum #1 (minor ASN.1 corrections).
- Removed example iteration count 1024 from ASN.1.
- Recommendation to use PKCS#5 v2.1 instead of Appendix B method for password privacy mode.
- Comments and minor corrections to ASN.1 module.
- Removal of export regulations discussion (former Appendix D).
- Replacement of RSA with EMC in IP considerations.
- Added NIST SP 800-132 reference for iteration count.
- PFX acronym expansion note.
- Clarification: "no longer recommended" changed to "not recommended" for password privacy method in Appendix B.

## 2. Overview
### 2.1 Exchange Modes
Four combinations of privacy and integrity modes:
- **Public-key privacy**: Personal information enveloped using trusted encryption public key of destination; opened with corresponding private key.
- **Password privacy**: Encrypted with symmetric key derived from username, password, salt (per [22][13]).
- **Public-key integrity**: Digital signature using source platform’s private signature key; verified with public key.
- **Password integrity**: MAC derived from secret integrity password.

### 2.2 Mode Choice Policies
All combinations permitted. Security policy: public-key modes preferable; password modes may be used when public-key not possible (e.g., unknown destination).

### 2.3 Trusted Public Keys
- Asymmetric keys used for encryption (public-key privacy) and signature (public-key integrity).
- Keys dedicated solely for transport; distinct from user’s personal keys.
- Private encryption key kept on destination; private signature key kept on source.
- Public keys must be transported and trusted; trust verification left to user (not specified further).

### 2.4 The AuthenticatedSafe
- **Shall**: Each compliant platform shall be able to import and export AuthenticatedSafe PDUs wrapped in PFX PDUs.
- For integrity: AuthenticatedSafe is signed (public-key) or MACed (password). Signature uses VSrcSigK; TPSrcSigK must accompany PFX.
- MAC uses secret integrity password, salt, iteration count, and contents of AuthenticatedSafe.
- AuthenticatedSafe is sequence of ContentInfo values: plaintext (Data), enveloped (public-key privacy), or encrypted (password privacy).
- Enveloped: symmetric cipher key encrypted with RSA public key (TPDestEncK). Encrypted: symmetric cipher key derived from password, salt, iteration count.
- Each ContentInfo contains SafeContents (private keys, shrouded keys, certificates, CRLs, opaque data).
- Unencrypted option allowed for exportability; multi-part design permits flexibility.
- Integrity wrapper protects whole AuthenticatedSafe (including unencrypted parts) – reverse of typical order.

## 3. PFX PDU Syntax
- All modes use same PDU format; ASN.1 and BER-encoding ensure platform independence.
- One ASN.1 export: **PFX** – outer integrity wrapper.

### PFX Structure
- **version**: shall be v3 for this version.
- **authSafe**: ContentInfo; contentType = signedData (public-key integrity) or data (password integrity).
- **macData**: optional (only in password integrity); contains DigestInfo (MAC value), macSalt, iterationCount. MAC key derived from password, salt, iteration count via HMAC (per Appendix B). salt and iteration count thwart dictionary attacks.

```
PFX ::= SEQUENCE {
    version     INTEGER {v3(3)}(v3,...),
    authSafe    ContentInfo,
    macData     MacData OPTIONAL
}
MacData ::= SEQUENCE {
    mac         DigestInfo,
    macSalt     OCTET STRING,
    iterations  INTEGER DEFAULT 1 -- deprecated use
}
```

### 3.1 The AuthenticatedSafe Type
- authSafe contentType shall be data or signedData.
- content field shall contain BER-encoded AuthenticatedSafe.
```
AuthenticatedSafe ::= SEQUENCE OF ContentInfo
    -- Data if unencrypted
    -- EncryptedData if password-encrypted
    -- EnvelopedData if public key-encrypted
```

### 3.2 The SafeBag Type
- SafeContents is SEQUENCE OF SafeBag.
- Each SafeBag holds one item (key, certificate, etc.) identified by OID.

```
SafeContents ::= SEQUENCE OF SafeBag
SafeBag ::= SEQUENCE {
    bagId          BAG-TYPE.&id ({PKCS12BagSet}),
    bagValue       [0] EXPLICIT BAG-TYPE.&Type({PKCS12BagSet}{@bagId}),
    bagAttributes  SET OF PKCS12Attribute OPTIONAL
}
PKCS12Attribute ::= SEQUENCE {
    attrId      ATTRIBUTE.&id ({PKCS12AttrSet}),
    attrValues  SET OF ATTRIBUTE.&Type ({PKCS12AttrSet}{@attrId})
}
```

- Six bag types defined:
  - **keyBag**: PrivateKeyInfo (PKCS #8).
  - **pkcs8ShroudedKeyBag**: EncryptedPrivateKeyInfo.
  - **certBag**: CertBag – certificate, distinguished by OID. Two types: x509Certificate (DER-encoded OCTET STRING) and sdsiCertificate (Base64 IA5String).
  - **crlBag**: CRLBag – CRL, distinguished by OID. One type: x509CRL (DER-encoded OCTET STRING).
  - **secretBag**: SecretBag – miscellaneous secret, OID-dependent value.
  - **safeContentsBag**: SafeContents – recursive nesting.

- BAG-TYPE definitions with OIDs (bagtypes 1-6).
- PKCS12BagSet extensible for future bag types.

### 3.3 Creating PFX PDUs (Section 5.1)
1. Create SafeContents instances (SC_1...SC_n).
2. For each SC_i, depending on encryption:
   - A. No encryption: ContentInfo with Data, BER-encoding of SC_i.
   - B. Password encryption: ContentInfo EncryptedData, encryptedContent set to encryption of BER-encoding.
   - C. Public-key encryption: ContentInfo EnvelopedData similar.
3. Form AuthenticatedSafe as SEQUENCE of these ContentInfo.
4. Wrap in ContentInfo T (Data) containing BER-encoding of AuthenticatedSafe.
5. Integrity:
   - A. SignedData: ContentInfo of type SignedData with contentInfo = T.
   - B. HMAC: HMAC (SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, or SHA-512/256) computed on contents of Data (excluding tag/length bytes).

### 3.4 Importing from a PFX PDU
- Reverse creation procedure.
- Importing application should ignore unknown OIDs; may alert user.
- Special care when overwriting local items; behavior may depend on item type (e.g., private key vs. CRL). Appropriate to ask user.

## 4. Security Considerations
- Password-based cryptography limited; off-line password search possible.
- Salt and iteration count increase attack complexity.
- Passwords must be well-selected (see NIST SP 800-61-1) and protected if stored.
- Salt: ideally as long as hash output, randomly generated (per PKCS #5 2.1 Section 4).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Each compliant platform **shall** be able to import and export AuthenticatedSafe PDUs wrapped in PFX PDUs. | shall | Section 3.4 (Overview paragraph) |
| R2 | The version of PFX **shall** be v3 for this version of this document. | shall | Section 4 (PFX syntax) |
| R3 | The contentType of authSafe **shall** be of type data or signedData. | shall | Section 4.1 (AuthenticatedSafe) |
| R4 | The content field of authSafe **shall**, either directly (data case) or indirectly (signedData case), contain a BER-encoded value of type AuthenticatedSafe. | shall | Section 4.1 |
| R5 | Public keys from encryption/signature key pairs **must** be transported to the other platform such that they are trusted to have originated at the correct platform. | must | Section 3.3 |
| R6 | TPSrcSigK **must** accompany the PFX to the destination platform for signature verification. | must | Section 3.4 |
| R7 | When password integrity mode is used, HMAC with SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, or SHA-512/256 is computed on the BER-encoding of the contents of the content field of authSafe. | should (normative) | Section 5.1 Step 5B, Appendix A |

*Note: Additional "should" recommendations exist (e.g., salt length, iteration count) but are not listed as requirements.*

## Informative Annexes (Condensed)

- **Appendix A – MACs**: Describes use of HMAC [11][20] for password integrity mode. HMAC may use SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, or SHA-512/256. The same hash algorithm is used for MAC key derivation. MAC key lengths match hash output (160–512 bits).

- **Appendix B – Deriving Keys and IVs from Passwords and Salt**: **Not recommended** for password privacy mode (use PKCS #5 v2.1 PBES2/PBKDF2). Method still used for password integrity mode. Procedure: password formatted as BMPString with NULL terminator (big-endian). General method uses hash function H (MD2, MD5, SHA-1/224/256/384/512/512-224/512-256) with iteration count. ID byte distinguishes key material (1), IV (2), or integrity key (3). For password integrity mode, MAC key length equals hash output; same hash as used for MACing.

- **Appendix C – Keys and IVs for Password Privacy Mode**: Deprecated; retained for backwards compatibility only. Uses SHA-1-based PBE algorithms (RC4 128/40, Triple-DES CBC, RC2-CBC 128/40) with pkcs-12PbeParams. Iteration count recommended ≥1024. Notes that future definitions should replace MacData with PBMAC1 from PKCS #5.

- **Appendix D – ASN.1 Module**: Full ASN.1 module "PKCS-12" defining PFX, MacData, AuthenticatedSafe, SafeContents, SafeBag, bag types, attributes, and OIDs. Not reproduced in full here; see original.

- **Appendix E – Intellectual Property Considerations**: EMC makes no patent claims on general constructions; RC2/RC4 are trademarks. No representations regarding third-party claims.

- **Appendix F – Acknowledgments**: Thanks to Dan Simon (Microsoft), Jim Spring (Netscape), Brian Beckman (Microsoft) for early drafts.

- **Appendix G – About PKCS**: History and role of Public-Key Cryptography Standards; further development through IETF.