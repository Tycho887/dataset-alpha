# RFC 3369: Cryptographic Message Syntax (CMS)
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: August 2002 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3369

## Scope (Summary)
This document specifies the Cryptographic Message Syntax (CMS) for digitally signing, digesting, authenticating, or encrypting arbitrary message content. It obsoletes RFC 2630 and RFC 3211, adding password-based key management and an extension mechanism for new key management schemes.

## Normative References
- [CMSALG] Housley, R., "Cryptographic Message Syntax (CMS) Algorithms", RFC 3269, August 2002
- [ESS] Hoffman, P., "Enhanced Security Services for S/MIME", RFC 2634, June 1999
- [MSG] Ramsdell, B., "S/MIME Version 3 Message Specification", RFC 2633, June 1999
- [OLDCMS] Housley, R., "Cryptographic Message Syntax", RFC 2630, June 1999
- [PKCS#6] RSA Laboratories. PKCS #6: Extended-Certificate Syntax Standard, Version 1.5. November 1993
- [PKCS#7] Kaliski, B., "PKCS #7: Cryptographic Message Syntax, Version 1.5.", RFC 2315, March 1998
- [PKCS#9] RSA Laboratories. PKCS #9: Selected Attribute Types, Version 1.1. November 1993
- [PROFILE] Housley, R., Polk, W., Ford, W. and D. Solo, "Internet X.509 Public Key Infrastructure: Certificate and CRL Profile", RFC 3280, April 2002
- [ACPROFILE] Farrell, S. and R. Housley, "An Internet Attribute Certificate Profile for Authorization", RFC 3281, April 2002
- [STDWORDS] Bradner, S., "Key Words for Use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [X.208-88], [X.209-88], [X.501-88], [X.509-88], [X.509-97], [X.509-00] as referenced in Section 13
- [RANDOM] Eastlake, D., Crocker, S. and J. Schiller, "Randomness Recommendations for Security", RFC 1750, December 1994
- [DSS] National Institute of Standards and Technology. FIPS Pub 186: Digital Signature Standard. 19 May 1994

## Definitions and Abbreviations
- **CMS**: Cryptographic Message Syntax
- **ASN.1**: Abstract Syntax Notation One (X.208-88)
- **BER**: Basic Encoding Rules (X.209-88)
- **DER**: Distinguished Encoding Rules
- **MAC**: Message Authentication Code
- **CRL**: Certificate Revocation List
- **UKM**: User Keying Material
- **KEK**: Key-Encryption Key
- **OID**: Object Identifier
- **PKCS**: Public-Key Cryptography Standards
- **S/MIME**: Secure/Multipurpose Internet Mail Extensions
- **Must/Shall/Required**: defined in [STDWORDS]; MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, RECOMMENDED, MAY, and OPTIONAL are to be interpreted as described in [STDWORDS].

## 1. Introduction
The CMS describes an encapsulation syntax for data protection supporting digital signatures and encryption. It allows multiple encapsulations and nesting. Arbitrary attributes (e.g., signing time) can be signed. Values are generated using ASN.1 and BER-encoding. CMS is derived from PKCS #7 version 1.5 (RFC 2315). Backward compatibility is preserved where possible. Section 1.1 details changes since RFC 2630: password-based key management (RFC 3211) is included; version 2 attribute certificate transfer added; version 1 attribute certificates deprecated; cryptographic algorithms moved to separate document [CMSALG].

## 2. General Overview
- CMS defines one protection content type: **ContentInfo**.
- Six content types defined: **data**, **signed-data**, **enveloped-data**, **digested-data**, **encrypted-data**, **authenticated-data**.
- **Conformance**: An implementation MUST implement ContentInfo, data, signed-data, and enveloped-data content types. Other content types MAY be implemented.
- Single-pass processing using indefinite-length BER is permitted. Signed attributes and authenticated attributes MUST be DER encoded.

## 3. General Syntax
- Object identifier: `id-ct-contentInfo ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) smime(16) ct(1) 6 }`
- ASN.1 type `ContentInfo`:
  - `contentType ContentType` (OID)
  - `content [0] EXPLICIT ANY DEFINED BY contentType`
- **contentType**: indicates type of associated content.
- **content**: associated content; type determined by contentType. Additional content types defined elsewhere SHOULD NOT be a CHOICE type.

## 4. Data Content Type
- Object identifier: `id-data ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 1 }`
- Intended to refer to arbitrary octet strings (e.g., ASCII text). Interpretation left to application. Generally encapsulated in other content types.

## 5. Signed-data Content Type

### 5.1 SignedData Type
- Object identifier: `id-signedData ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 2 }`
- ASN.1 type `SignedData`:
  - `version CMSVersion`
  - `digestAlgorithms DigestAlgorithmIdentifiers`
  - `encapContentInfo EncapsulatedContentInfo`
  - `certificates [0] IMPLICIT CertificateSet OPTIONAL`
  - `crls [1] IMPLICIT CertificateRevocationLists OPTIONAL`
  - `signerInfos SignerInfos`
- **version** assignment rules:
  - IF (certificates is present) AND (any version 2 attribute certificates are present) THEN version MUST be 4
  - ELSE IF ((certificates is present) AND (any version 1 attribute certificates are present)) OR (encapContentInfo eContentType is other than id-data) OR (any SignerInfo structures are version 3) THEN version MUST be 3
  - ELSE version MUST be 1
- **digestAlgorithms**: collection of message digest algorithm identifiers; MAY have zero elements. Lists algorithms used by signers; implementations MAY fail to validate signatures using a digest algorithm not in this set.
- **encapContentInfo**: signed content (see Section 5.2).
- **certificates**: collection of certificates; may contain chains from root CA to signers. Use of version 1 attribute certificates is strongly discouraged.
- **crls**: collection of CRLs; may be more or fewer than necessary.
- **signerInfos**: collection of per-signer information; MAY be zero. All implementations MUST gracefully handle unimplemented versions of SignerInfo and unimplemented signature algorithms.

### 5.2 EncapsulatedContentInfo Type
- ASN.1 type `EncapsulatedContentInfo`:
  - `eContentType ContentType` (OID)
  - `eContent [0] EXPLICIT OCTET STRING OPTIONAL`
- **eContentType**: uniquely specifies content type.
- **eContent**: content itself as octet string; need not be DER encoded.
- Optional omission of eContent permits "external signatures". In degenerate case with no signers, eContentType MUST be id-data and eContent omitted.

### Section 5.2.1 Compatibility with PKCS #7
- Informative: Describes differences between CMS and PKCS #7 SignedData. CMS defines eContent as OCTET STRING; PKCS #7 uses ANY. Backward compatibility strategies are provided.

### 5.3 SignerInfo Type
- ASN.1 type `SignerInfo`:
  - `version CMSVersion`
  - `sid SignerIdentifier`
  - `digestAlgorithm DigestAlgorithmIdentifier`
  - `signedAttrs [0] IMPLICIT SignedAttributes OPTIONAL`
  - `signatureAlgorithm SignatureAlgorithmIdentifier`
  - `signature SignatureValue`
  - `unsignedAttrs [1] IMPLICIT UnsignedAttributes OPTIONAL`
- **SignerIdentifier** CHOICE: `issuerAndSerialNumber` or `subjectKeyIdentifier [0]`.
- **version**: MUST be 1 if IssuerAndSerialNumber; MUST be 3 if SubjectKeyIdentifier.
- **digestAlgorithm**: identifies message digest algorithm; SHOULD be among those in digestAlgorithms set.
- **signedAttrs**: optional but MUST be present if eContentType is not id-data. Must be DER encoded. If present, MUST contain content-type and message-digest attributes. Content-type attribute MUST NOT be used in countersignature.
- **signatureAlgorithm**: identifies signature algorithm.
- **signature**: result of digital signature generation.
- **unsignedAttrs**: optional collection of attributes not signed.
- **Attribute**: SEQUENCE of attrType OID and attrValues SET OF AttributeValue.

### 5.4 Message Digest Calculation Process
- Input is the value of the eContent OCTET STRING (not tag or length).
- If signedAttrs absent: result is message digest of content.
- If signedAttrs present: result is message digest of DER encoding of SignedAttrs, using EXPLICIT SET OF tag (not IMPLICIT [0] tag). Must include content-type and message-digest attributes.
- When signedAttrs absent, only content octets are input; length need not be known in advance.

### 5.5 Signature Generation Process
- Input: message digest result and signer’s private key. Signature value MUST be encoded as OCTET STRING in signature field.

### 5.6 Signature Verification Process
- Input: message digest result and signer’s public key (preferably from certificates field). Recipient MUST NOT rely on message digest values computed by originator. If signedAttrs present, computed message digest MUST equal messageDigest attribute value. Content-type attribute value MUST match eContentType.

## 6. Enveloped-data Content Type

### 6.1 EnvelopedData Type
- Object identifier: `id-envelopedData ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 3 }`
- ASN.1 type `EnvelopedData`:
  - `version CMSVersion`
  - `originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL`
  - `recipientInfos RecipientInfos`
  - `encryptedContentInfo EncryptedContentInfo`
  - `unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL`
- **version** assignment:
  - IF ((originatorInfo present) AND (any version 2 attribute certificates present)) OR (any RecipientInfo includes pwri) OR (any RecipientInfo includes ori) THEN version is 3
  - ELSE IF (originatorInfo present) OR (unprotectedAttrs present) OR (any RecipientInfo version other than 0) THEN version is 2
  - ELSE version is 0
- **originatorInfo**: optional; contains certificates and CRLs.
- **recipientInfos**: collection of per-recipient info; MUST have at least one element.
- **encryptedContentInfo**: includes contentType, contentEncryptionAlgorithm, encryptedContent (optional).
- **unprotectedAttrs**: optional.

### 6.2 RecipientInfo Type
- CHOICE: `ktri KeyTransRecipientInfo`, `kari [1] KeyAgreeRecipientInfo`, `kekri [2] KEKRecipientInfo`, `pwri [3] PasswordRecipientInfo`, `ori [4] OtherRecipientInfo`.
- Implementations MUST gracefully handle unimplemented alternatives and versions.
- **Implementations MUST support** ktri, kari, kekri. MAY support pwri and ori.

#### 6.2.1 KeyTransRecipientInfo Type
- ASN.1 type: `KeyTransRecipientInfo` with version, rid (RecipientIdentifier CHOICE), keyEncryptionAlgorithm, encryptedKey.
- **version**: MUST be 0 if IssuerAndSerialNumber, 2 if SubjectKeyIdentifier.
- **rid**: specifies recipient's certificate; must contain key transport public key. For sender, MUST support at least one alternative; for recipient, MUST support both.

#### 6.2.2 KeyAgreeRecipientInfo Type
- ASN.1 type: `KeyAgreeRecipientInfo` with version (MUST be 3), originator, optional ukm, keyEncryptionAlgorithm, recipientEncryptedKeys.
- **originator**: CHOICE of IssuerAndSerialNumber, SubjectKeyIdentifier, or OriginatorPublicKey. Implementations MUST support all three.
- **ukm**: optional; implementations MUST support recipient processing if present.
- **recipientEncryptedKeys**: SEQUENCE OF RecipientEncryptedKey; implementations MUST support both alternatives for recipient identifier.
- Recipient certificate must contain key agreement public key (keyAgreement bit asserted).

#### 6.2.3 KEKRecipientInfo Type
- ASN.1 type: `KEKRecipientInfo` with version (MUST be 4), kekid (KEKIdentifier), keyEncryptionAlgorithm, encryptedKey.
- **KEKIdentifier**: keyIdentifier (OCTET STRING), optional date, optional other.

#### 6.2.4 PasswordRecipientInfo Type
- ASN.1 type: `PasswordRecipientInfo` with version (MUST be 0), optional keyDerivationAlgorithm, keyEncryptionAlgorithm, encryptedKey.

#### 6.2.5 OtherRecipientInfo Type
- ASN.1 type: `OtherRecipientInfo` with oriType (OID) and oriValue (ANY DEFINED BY oriType).

### 6.3 Content-encryption Process
- Randomly generate content-encryption key. Pad data as needed: if input length lth is not multiple of block size k, pad with k-(lth mod k) octets each of that value. Padding is always added, even if already multiple. Removable uniquely if k < 256.

### 6.4 Key-encryption Process
- Input is the value of the content-encryption key. Any key management technique may be used per recipient.

## 7. Digested-data Content Type
- Object identifier: `id-digestedData ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 5 }`
- ASN.1 type `DigestedData`:
  - `version CMSVersion`: if eContentType is id-data then MUST be 0, else MUST be 2.
  - `digestAlgorithm DigestAlgorithmIdentifier`
  - `encapContentInfo EncapsulatedContentInfo`
  - `digest Digest` (OCTET STRING)
- Message digesting process same as Section 5.4 when no signed attributes.

## 8. Encrypted-data Content Type
- Object identifier: `id-encryptedData ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 6 }`
- ASN.1 type `EncryptedData`:
  - `version CMSVersion`: if unprotectedAttrs present MUST be 2, else MUST be 0.
  - `encryptedContentInfo EncryptedContentInfo`
  - `unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL`

## 9. Authenticated-data Content Type

### 9.1 AuthenticatedData Type
- Object identifier: `id-ct-authData ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) ct(1) 2 }`
- ASN.1 type `AuthenticatedData`:
  - `version CMSVersion`: IF (originatorInfo present AND any version 2 attribute certificates present) THEN version is 1, ELSE version is 0.
  - `originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL`
  - `recipientInfos RecipientInfos` (MUST have at least one)
  - `macAlgorithm MessageAuthenticationCodeAlgorithm`
  - `digestAlgorithm [1] DigestAlgorithmIdentifier OPTIONAL`
  - `encapContentInfo EncapsulatedContentInfo`
  - `authAttrs [2] IMPLICIT AuthAttributes OPTIONAL`
  - `mac MessageAuthenticationCode`
  - `unauthAttrs [3] IMPLICIT UnauthAttributes OPTIONAL`
- **digestAlgorithm**: if present, authAttrs MUST also be present.
- **authAttrs**: optional but MUST be present if eContentType is not id-data. If present, digestAlgorithm MUST also be present. Must be DER encoded. Must contain content-type and message-digest attributes.
- **mac**: message authentication code.

### 9.2 MAC Generation
- If authAttrs absent: MAC input is value of eContent OCTET STRING.
- If authAttrs present: input to MAC is DER encoding of authAttrs (using EXPLICIT SET OF tag). Message digest of content computed similarly (only value octets).
- Originator uses authentication key from recipientInfo.

### 9.3 MAC Verification
- Recipient MUST NOT rely on MAC or digest values computed by originator. MAC value calculated by recipient MUST equal mac field. If authAttrs present, content message digest must match message-digest attribute. Content-type attribute value must match eContentType.

## 10. Useful Types

### 10.1 Algorithm Identifier Types
- All use `AlgorithmIdentifier` from X.509.
- **DigestAlgorithmIdentifier**: e.g., SHA-1, MD2, MD5.
- **SignatureAlgorithmIdentifier**: e.g., RSA, DSA, ECDSA.
- **KeyEncryptionAlgorithmIdentifier**: for encrypting content-encryption keys.
- **ContentEncryptionAlgorithmIdentifier**: e.g., Triple-DES, RC2.
- **MessageAuthenticationCodeAlgorithm**: e.g., DES-MAC, HMAC-SHA-1.
- **KeyDerivationAlgorithmIdentifier**: for password-based key derivation.

### 10.2 Other Useful Types
- **CertificateRevocationLists**: SET OF CertificateList.
- **CertificateChoices**: CHOICE of Certificate, ExtendedCertificate (obsolete), AttributeCertificateV1 (obsolete), AttributeCertificateV2.
- **CertificateSet**: SET OF CertificateChoices.
- **IssuerAndSerialNumber**: SEQUENCE of issuer (Name) and serialNumber (INTEGER).
- **CMSVersion**: INTEGER {v0(0), v1(1), v2(2), v3(3), v4(4)}.
- **UserKeyingMaterial**: OCTET STRING.
- **OtherKeyAttribute**: SEQUENCE of keyAttrId (OID) and optional keyAttr.

## 11. Useful Attributes

### 11.1 Content Type (id-contentType)
- Object identifier: `id-contentType ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) 3 }`
- **MUST be present** whenever signed/authenticated attributes are present. Attribute value MUST match eContentType. MUST be signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected. SINGLE attribute value. No multiple instances permitted.

### 11.2 Message Digest (id-messageDigest)
- Object identifier: `id-messageDigest ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) 4 }`
- **MUST be present** when any signed/authenticated attributes present. MUST be signed or authenticated attribute. SINGLE attribute value. Only one instance in SignedAttributes or AuthAttributes.

### 11.3 Signing Time (id-signingTime)
- Object identifier: `id-signingTime ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) 5 }`
- **MUST be signed or authenticated attribute**. SINGLE attribute value. No multiple instances.
- Encoding: UTCTime for dates 1950-2049 (inclusive) in GMT "YYMMDDHHMMSSZ". GeneralizedTime for other years in GMT "YYYYMMDDHHMMSSZ". No fractional seconds.
- No requirement on correctness; acceptance at recipient's discretion.

### 11.4 Countersignature (id-countersignature)
- Object identifier: `id-countersignature ::= { iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs9(9) 6 }`
- **MUST be unsigned attribute**. MUST NOT be signed/authenticated/unauthenticated/unprotected.
- ASN.1 type `Countersignature ::= SignerInfo` with exceptions:
  1. signedAttributes MUST NOT contain content-type attribute.
  2. signedAttributes MUST contain message-digest attribute if any other attributes present.
  3. Input to message digest is contents octets of DER encoding of signatureValue field of associated SignerInfo.
- Multiple attribute values allowed; unsigedAttributes may include multiple instances.

## 12. ASN.1 Modules (Summarized)
- **Section 12.1**: Full ASN.1 module for CMS (CryptographicMessageSyntax) with all type definitions and OIDs.
- **Section 12.2**: Version 1 Attribute Certificate ASN.1 module (AttributeCertificateVersion1), deprecated.

## 13. References
List of normative references as in original (see Normative References above).

## 14. Security Considerations
- Protect signer's private key, key management private key, key-encryption keys, content-encryption keys, and message-authentication keys.
- Key management for MAC keys must provide data origin authentication; RSA and Ephemeral-Static Diffie-Hellman do not; Static-Static Diffie-Hellman does when public keys bound to identities.
- When more than two parties share a MAC key, data origin authentication is not provided.
- Content-encryption keys, MAC keys, IVs, and padding must be generated randomly; use of inadequate PRNGs reduces security; [RANDOM] and FIPS 186 provide guidance.
- Ensure key-encryption algorithms are as strong or stronger than content-encryption algorithms.
- Cryptographic algorithms weaken over time; implementations should be modular.
- Countersignature can sign inappropriate signature values; implementations should verify original signature before countersigning or ensure appropriate context.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST implement ContentInfo, data, signed-data, and enveloped-data content types. | shall | Section 2 |
| R2 | Implementations MAY implement digested-data, encrypted-data, and authenticated-data content types. | may | Section 2 |
| R3 | Signed attributes and authenticated attributes MUST be DER encoded. | shall | Section 2, 5.3, 9.1 |
| R4 | ContentInfo content type MUST be an OID; content field is EXPLICIT ANY defined by contentType. | shall | Section 3 |
| R5 | Additional content types defined elsewhere SHOULD NOT be a CHOICE type. | should | Section 3 |
| R6 | SignedData version MUST be assigned per rules in Section 5.1. | shall | 5.1 |
| R7 | When signedAttrs are present in SignedData, they MUST contain at minimum content-type and message-digest attributes. | shall | 5.3 |
| R8 | content-type attribute MUST NOT be used in countersignature unsigned attribute. | shall | 5.4, 11.4 |
| R9 | Implementations MUST support reception of both issuerAndSerialNumber and subjectKeyIdentifier forms of SignerIdentifier. | shall | 5.3 |
| R10 | Implementing signature verification: recipient MUST NOT rely on originator's message digest values; computed digest must equal messageDigest attribute. | shall | 5.6 |
| R11 | EnvelopedData version MUST be assigned per rules in Section 6.1. | shall | 6.1 |
| R12 | RecipientInfo: implementations MUST support ktri, kari, kekri; MAY support pwri and ori. | shall/may | 6.2 |
| R13 | KeyTransRecipientInfo version MUST be 0 (IssuerAndSerialNumber) or 2 (subjectKeyIdentifier). | shall | 6.2.1 |
| R14 | KeyAgreeRecipientInfo version MUST be 3. | shall | 6.2.2 |
| R15 | KeyAgreeRecipientInfo: originator subjectKeyIdentifier, IssuerAndSerialNumber, and originatorKey MUST all be supported for originator. | shall | 6.2.2 |
| R16 | Implementations MUST support both alternatives for specifying recipient in KeyAgreeRecipientInfo. | shall | 6.2.2 |
| R17 | KEKRecipientInfo version MUST be 4. | shall | 6.2.3 |
| R18 | PasswordRecipientInfo version MUST be 0. | shall | 6.2.4 |
| R19 | DigestedData version: if eContentType id-data then MUST be 0, else MUST be 2. | shall | 7 |
| R20 | EncryptedData version: if unprotectedAttrs present then MUST be 2, else MUST be 0. | shall | 8 |
| R21 | AuthenticatedData version: if originatorInfo present with v2 attr certs then version 1 else 0. | shall | 9.1 |
| R22 | authAttrs in AuthenticatedData: if present, digestAlgorithm MUST also be present; authAttrs MUST be DER encoded and contain content-type and message-digest attributes. | shall | 9.1 |
| R23 | MAC verification: recipient MUST NOT rely on originator's MAC or digest values; computed MAC must equal mac field. | shall | 9.3 |
| R24 | Content-type attribute MUST be a signed or authenticated attribute, not unsigned/unauthenticated/unprotected. | shall | 11.1 |
| R25 | Message-digest attribute MUST be a signed or authenticated attribute. | shall | 11.2 |
| R26 | SigningTime attribute MUST be signed or authenticated attribute; MUST encode per rules (UTCTime 1950-2049, GeneralizedTime otherwise; GMT; seconds required). | shall | 11.3 |
| R27 | Countersignature attribute MUST be an unsigned attribute. | shall | 11.4 |
| R28 | Countersignature signedAttributes MUST NOT contain content-type attribute; MUST contain message-digest if any other attributes. | shall | 11.4 |
| R29 | Content-encryption keys, MAC keys, IVs, and padding must be randomly generated. | shall | Sec 14 |
| R30 | Key-encryption algorithms must be at least as strong as content-encryption algorithms. | shall | Sec 14 |
| R31 | Implementations must protect private keys, key-encryption keys, content-encryption keys, and MAC keys. | shall | Sec 14 |

## Informative Annexes (Condensed)
- **Section 1.1 Changes Since RFC 2630**: Summaries of changes: password-based key management added; version 2 attribute certificate transfer added; version 1 deprecated; algorithms separated.
- **Section 5.2.1 Compatibility with PKCS #7**: Describes differences between CMS (encapsulated content as OCTET STRING) and PKCS #7 (ANY). Strategies for backward compatibility when processing or creating SignedData.
- **Section 12 ASN.1 Modules**: Full normative ASN.1 definitions of CMS types and Version 1 Attribute Certificate (deprecated). Provided for implementation.
- **Section 14 Security Considerations**: Detailed guidance on key protection, randomness, algorithm strength, modularity, and countersignature verification.