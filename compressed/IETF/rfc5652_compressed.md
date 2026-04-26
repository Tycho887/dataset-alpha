# RFC 5652: Cryptographic Message Syntax (CMS)
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: September 2009 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc5652

## Scope (Summary)
This document specifies the Cryptographic Message Syntax (CMS) used to digitally sign, digest, authenticate, or encrypt arbitrary message content. It defines an encapsulation syntax for data protection supporting digital signatures, encryption, and multiple encapsulations.

## Normative References
- [ACPROFILE] Farrell, S. and R. Housley, "An Internet Attribute Certificate Profile for Authorization", RFC 3281, April 2002.
- [PROFILE] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [STDWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [X.208-88] CCITT Recommendation X.208: Specification of Abstract Syntax Notation One (ASN.1), 1988.
- [X.209-88] CCITT Recommendation X.209: Specification of Basic Encoding Rules for Abstract Syntax Notation One (ASN.1), 1988.
- [X.501-88] CCITT Recommendation X.501: The Directory - Models, 1988.
- [X.509-88] CCITT Recommendation X.509: The Directory - Authentication Framework, 1988.
- [X.509-97] ITU-T Recommendation X.509: The Directory - Authentication Framework, 1997.
- [X.509-00] ITU-T Recommendation X.509: The Directory - Authentication Framework, 2000.

## Definitions and Abbreviations
- **CMS**: Cryptographic Message Syntax.
- **ASN.1**: Abstract Syntax Notation One.
- **BER**: Basic Encoding Rules.
- **DER**: Distinguished Encoding Rules.
- **MAC**: Message Authentication Code.
- **CRL**: Certificate Revocation List.
- **UKM**: User Keying Material.
- **ContentInfo**: Top-level protection content encapsulating a single content type.
- **id-data**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 1} – identifies data content type.
- **id-signedData**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 2}.
- **id-envelopedData**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 3}.
- **id-digestedData**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 5}.
- **id-encryptedData**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs7(7) 6}.
- **id-ct-authData**: OID {iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) ct(1) 2}.
- **SignerIdentifier**: CHOICE of issuerAndSerialNumber or subjectKeyIdentifier.
- **RecipientInfo**: CHOICE of key transport, key agreement, KEK, password, or other.
- **DigestAlgorithmIdentifier, SignatureAlgorithmIdentifier**, etc.: Defined as AlgorithmIdentifier.

## 1. Introduction
- **1.1 Evolution**: CMS derived from PKCS #7 v1.5; changes documented per version (2630, 3369, 3852, this RFC). 
- **1.2 Terminology**: Key words (MUST, MUST NOT, etc.) as per [STDWORDS].
- **1.3 Version Numbers**: Each major data structure includes a version number; lowest version supporting the syntax used.

## 2. General Overview
- **Required implementation**: ContentInfo, data, signed-data, enveloped-data content types MUST be implemented. Others MAY be implemented.
- **Encoding**: Single-pass processing with indefinite-length BER; signed/authenticated attributes MUST be DER encoded.

## 3. General Syntax
- **ContentInfo** ASN.1:
  ```
  ContentInfo ::= SEQUENCE {
    contentType ContentType,
    content [0] EXPLICIT ANY DEFINED BY contentType
  }
  ```
  - contentType: object identifier unique to content type.
  - content: associated content; if additional content types defined elsewhere, ASN.1 type SHOULD NOT be CHOICE.

## 4. Data Content Type
- **id-data**: OID as above.
- Intended for arbitrary octet strings; interpretation left to application.

## 5. Signed-data Content Type
### 5.1 SignedData Type
- **id-signedData** OID.
- ASN.1: 
  ```
  SignedData ::= SEQUENCE {
    version CMSVersion,
    digestAlgorithms DigestAlgorithmIdentifiers,
    encapContentInfo EncapsulatedContentInfo,
    certificates [0] IMPLICIT CertificateSet OPTIONAL,
    crls [1] IMPLICIT RevocationInfoChoices OPTIONAL,
    signerInfos SignerInfos
  }
  ```
- **Version assignment rules**:
  - If (certificates present with type other) OR (crls present with type other): version MUST be 5.
  - Else if (certificates present with version 2 attribute certificates): version MUST be 4.
  - Else if ((certificates present with version 1 attribute certificates) OR (any SignerInfo version 3) OR (encapContentInfo eContentType != id-data)): version MUST be 3.
  - Else: version MUST be 1.
- **digestAlgorithms**: SET of DigestAlgorithmIdentifier; MAY be zero elements. Implementations MAY fail to validate signatures using a digest algorithm not in this set.
- **encapContentInfo**: See Section 5.2.
- **certificates**: Optional; intended to contain sufficient certification paths. Version 1 attribute certificates are strongly discouraged.
- **crls**: Optional collection of revocation status information.
- **signerInfos**: SET of SignerInfo; MAY be zero elements. When multiple signatures, successful validation of one signature from a given signer ought to be treated as successful. All implementations MUST gracefully handle unimplemented versions of SignerInfo and unimplemented signature algorithms.

### 5.2 EncapsulatedContentInfo Type
- ASN.1:
  ```
  EncapsulatedContentInfo ::= SEQUENCE {
    eContentType ContentType,
    eContent [0] EXPLICIT OCTET STRING OPTIONAL
  }
  ```
- eContentType uniquely specifies content type. eContent is the content as octet string; need not be DER encoded.
- External signatures: eContent can be absent; signatureValue still calculated.
- Degenerate case (no signers): eContentType MUST be id-data, eContent MUST be omitted.

#### 5.2.1 Compatibility with PKCS #7
- CMS uses OCTET STRING for eContent; PKCS #7 uses ANY. Compatibility issues for non-Data types (e.g., signed receipts). Strategy: if CMS decode fails, try PKCS #7 decode. For creation, implementations MAY adjust encoding based on eContentType (e.g., Microsoft Authenticode).

### 5.3 SignerInfo Type
- ASN.1: 
  ```
  SignerInfo ::= SEQUENCE {
    version CMSVersion,
    sid SignerIdentifier,
    digestAlgorithm DigestAlgorithmIdentifier,
    signedAttrs [0] IMPLICIT SignedAttributes OPTIONAL,
    signatureAlgorithm SignatureAlgorithmIdentifier,
    signature SignatureValue,
    unsignedAttrs [1] IMPLICIT UnsignedAttributes OPTIONAL
  }
  ```
- SignerIdentifier CHOICE: issuerAndSerialNumber or subjectKeyIdentifier.
- **Version**: If issuerAndSerialNumber -> version MUST be 1. If subjectKeyIdentifier -> version MUST be 3.
- **sid**: Must support reception of both forms. When generating, subjectKeyIdentifier MUST be used for non-X.509 certificates.
- **digestAlgorithm**: SHOULD be among digestAlgorithms in SignedData. Implementations MAY fail to validate if not in set.
- **signedAttrs**: Optional; MUST be present if eContentType != id-data. SignedAttributes MUST be DER encoded. If present, MUST contain content-type and message-digest attributes. Content-type attribute MUST NOT be in countersignature unsigned attribute.
- **signatureAlgorithm**: Identifies signature algorithm.
- **signature**: SignatureValue OCTET STRING.
- **unsignedAttrs**: Optional.

### 5.4 Message Digest Calculation Process
- Input: value of eContent OCTET STRING (only octets, not tag/length).
- If signedAttrs absent: result is digest of content.
- If signedAttrs present: result is digest of complete DER encoding of SignedAttrs value (using EXPLICIT SET OF tag, not IMPLICIT [0]). This must include content-type and message-digest attributes.
- Content-type attribute MUST NOT be in countersignature unsigned attribute.

### 5.5 Signature Generation Process
- Input: message digest result and signer's private key. Signature value MUST be encoded as OCTET STRING in signature field.

### 5.6 Signature Verification Process
- Input: message digest result and signer's public key. Recipient MUST NOT rely on any message digest values computed by originator.
- If signedAttrs present: content message digest MUST be calculated per 5.4; must match messageDigest attribute.
- content-type attribute value MUST match encapContentInfo eContentType.

## 6. Enveloped-data Content Type
### 6.1 EnvelopedData Type
- **id-envelopedData** OID.
- ASN.1:
  ```
  EnvelopedData ::= SEQUENCE {
    version CMSVersion,
    originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
    recipientInfos RecipientInfos,
    encryptedContentInfo EncryptedContentInfo,
    unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL
  }
  ```
- **Version assignment rules**:
  - If originatorInfo present and (any certificates type other OR any crls type other): version 4.
  - Else if (originatorInfo present and any version 2 attr certs) OR (any RecipientInfo pwri) OR (any RecipientInfo ori): version 3.
  - Else if (originatorInfo absent AND unprotectedAttrs absent AND all RecipientInfo version 0): version 0.
  - Else: version 2.
- **originatorInfo**: Optional; may contain certificates and CRLs.
- **recipientInfos**: MUST have at least one element.
- **encryptedContentInfo**: Contains contentType, contentEncryptionAlgorithm, and optional encryptedContent.
- **contentEncryptionAlgorithm**: Same for all recipients.
- **unprotectedAttrs**: Optional collection of attributes.

### 6.2 RecipientInfo Type
- CHOICE: ktri (KeyTransRecipientInfo), kari (KeyAgreeRecipientInfo), kekri (KEKRecipientInfo), pwri (PasswordRecipientInfo), ori (OtherRecipientInfo).
- **Implementations MUST support** ktri, kari, kekri. MAY support pwri and ori.
- **Graceful handling**: All implementations MUST gracefully handle unimplemented algorithms, versions, and unknown ori alternatives.

#### 6.2.1 KeyTransRecipientInfo
- ASN.1:
  ```
  KeyTransRecipientInfo ::= SEQUENCE {
    version CMSVersion,  -- always 0 or 2
    rid RecipientIdentifier,
    keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier,
    encryptedKey EncryptedKey
  }
  ```
- **Version**: If RecipientIdentifier is issuerAndSerialNumber -> version MUST be 0. If subjectKeyIdentifier -> version MUST be 2.
- **rid**: Recipient's certificate/key. For X.509 v3 cert with key usage extension, MUST assert keyEncipherment bit.
- **keyEncryptionAlgorithm**: Identifies algorithm to encrypt content-encryption key.
- **encryptedKey**: Result of encrypting content-encryption key.

#### 6.2.2 KeyAgreeRecipientInfo
- ASN.1 with originator [0] EXPLICIT OriginatorIdentifierOrKey, optional ukm, etc.
- **Version**: MUST always be 3.
- **originator**: CHOICE of issuerAndSerialNumber, subjectKeyIdentifier, or originatorKey (public key). Implementations MUST support all three.
- **ukm**: Optional; implementations MUST accept a KeyAgreeRecipientInfo that includes ukm; implementations that do not support UKM MUST gracefully handle its presence.
- **recipientEncryptedKeys**: Contains one or more RecipientEncryptedKey.
- **RecipientKeyIdentifier** includes subjectKeyIdentifier, optional date, optional other.
- For recipient processing, implementations MUST support both alternatives for specifying recipient (issuerAndSerialNumber and RecipientKeyIdentifier).
- Recipient's certificate must contain key agreement public key; X.509 v3 certificate with key usage extension MUST assert keyAgreement bit.

#### 6.2.3 KEKRecipientInfo
- **Version**: MUST always be 4.
- ASN.1 with kekid (KEKIdentifier), keyEncryptionAlgorithm, encryptedKey.
- KEKIdentifier: keyIdentifier (OCTET STRING), optional date, optional other.

#### 6.2.4 PasswordRecipientInfo
- Defined in RFC 3211; repeated here.
- **Version**: MUST always be 0.
- Contains keyDerivationAlgorithm [0] optional, keyEncryptionAlgorithm, encryptedKey.
- keyDerivationAlgorithm: if absent, key-encryption key from external source (e.g., smart card).

#### 6.2.5 OtherRecipientInfo
- SEQUENCE: oriType (OID), oriValue (ANY defined by oriType).

### 6.3 Content-encryption Process
- Content-encryption key randomly generated. Data padded as needed: for block size k, pad with k-(lth mod k) octets of value k-(lth mod k). Padding well-defined if k < 256.

### 6.4 Key-encryption Process
- Input is value of content-encryption key.

## 7. Digested-data Content Type
- **id-digestedData** OID.
- ASN.1:
  ```
  DigestedData ::= SEQUENCE {
    version CMSVersion,
    digestAlgorithm DigestAlgorithmIdentifier,
    encapContentInfo EncapsulatedContentInfo,
    digest Digest
  }
  ```
- **Version**: If encapContentInfo eContentType is id-data -> version MUST be 0; else version MUST be 2.

## 8. Encrypted-data Content Type
- **id-encryptedData** OID.
- ASN.1:
  ```
  EncryptedData ::= SEQUENCE {
    version CMSVersion,
    encryptedContentInfo EncryptedContentInfo,
    unprotectedAttrs [1] IMPLICIT UnprotectedAttributes OPTIONAL
  }
  ```
- **Version**: If unprotectedAttrs present -> version MUST be 2; else version MUST be 0.

## 9. Authenticated-data Content Type
### 9.1 AuthenticatedData Type
- **id-ct-authData** OID.
- ASN.1:
  ```
  AuthenticatedData ::= SEQUENCE {
    version CMSVersion,
    originatorInfo [0] IMPLICIT OriginatorInfo OPTIONAL,
    recipientInfos RecipientInfos,
    macAlgorithm MessageAuthenticationCodeAlgorithm,
    digestAlgorithm [1] DigestAlgorithmIdentifier OPTIONAL,
    encapContentInfo EncapsulatedContentInfo,
    authAttrs [2] IMPLICIT AuthAttributes OPTIONAL,
    mac MessageAuthenticationCode,
    unauthAttrs [3] IMPLICIT UnauthAttributes OPTIONAL
  }
  ```
- **Version**:
  - If originatorInfo present and (any certs type other OR any crls type other): version 3.
  - Else if originatorInfo present and any version 2 attribute certificates: version 1.
  - Else: version 0.
- **recipientInfos**: MUST have at least one element.
- **digestAlgorithm**: If present, authAttrs MUST also be present.
- **authAttrs**: Optional; MUST be present if eContentType != id-data. AuthAttributes MUST be DER encoded. If present, digestAlgorithm MUST also be present, and authAttrs MUST contain content-type and message-digest attributes.
- **mac**: MessageAuthenticationCode OCTET STRING.
- **unauthAttrs**: Optional.

### 9.2 MAC Generation
- If authAttrs absent: input to MAC is value of eContent OCTET STRING (only octets).
- If authAttrs present: input is DER encoding of authAttrs (using EXPLICIT SET OF tag). MAC input includes the authentication key from recipientInfo.
- Message digest calculation on content (if authAttrs present) uses eContent OCTET STRING value.

### 9.3 MAC Verification
- Recipient MUST NOT rely on any MAC or message digest values computed by originator.
- For authentication to succeed, recipient's computed MAC MUST equal mac field. If authAttrs present, computed message digest must equal message-digest attribute.
- content-type attribute value MUST match encapContentInfo eContentType.

## 10. Useful Types
### 10.1 Algorithm Identifier Types
- **DigestAlgorithmIdentifier**: AlgorithmIdentifier.
- **SignatureAlgorithmIdentifier**: AlgorithmIdentifier.
- **KeyEncryptionAlgorithmIdentifier**: AlgorithmIdentifier.
- **ContentEncryptionAlgorithmIdentifier**: AlgorithmIdentifier.
- **MessageAuthenticationCodeAlgorithm**: AlgorithmIdentifier.
- **KeyDerivationAlgorithmIdentifier**: AlgorithmIdentifier (from RFC 3211).

### 10.2 Other Useful Types
- **RevocationInfoChoices**: SET OF RevocationInfoChoice (crl or other).
- **CertificateChoices**: CHOICE of Certificate, ExtendedCertificate (obsolete), v1AttrCert (obsolete), v2AttrCert, other.
- **CertificateSet**: SET OF CertificateChoices.
- **IssuerAndSerialNumber**: SEQUENCE { issuer Name, serialNumber CertificateSerialNumber }.
- **CMSVersion**: INTEGER {v0(0), v1(1),..., v5(5)}.
- **UserKeyingMaterial**: OCTET STRING.
- **OtherKeyAttribute**: SEQUENCE { keyAttrId OID, keyAttr ANY defined by keyAttrId OPTIONAL }.

## 11. Useful Attributes
### 11.1 Content Type
- OID: id-contentType {1 2 840 113549 1 9 3}.
- MUST be present whenever signed attributes (signed-data) or authenticated attributes (authenticated-data) are present.
- Attribute value type: ContentType (OID). MUST have single attribute value; zero or multiple not permitted.
- Mutiple instances not allowed in SignedAttributes or AuthAttributes.
- MUST be signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected.

### 11.2 Message Digest
- OID: id-messageDigest {1 2 840 113549 1 9 4}.
- MUST be present when signed/authenticated attributes are present.
- Value type: MessageDigest (OCTET STRING). MUST have single attribute value; zero or multiple not permitted.
- Only one instance allowed in SignedAttributes or AuthAttributes.
- MUST be signed or authenticated attribute; MUST NOT be unsigned, unauthenticated, or unprotected.

### 11.3 Signing Time
- OID: id-signingTime {1 2 840 113549 1 9 5}.
- Value type: Time (CHOICE of UTCTime or GeneralizedTime).
- **Encoding**: Dates 1950-2049 MUST be UTCTime; others MUST be GeneralizedTime. UTCTime MUST include seconds (YYMMDDHHMMSSZ). GeneralizedTime MUST include seconds and no fractional seconds.
- MUST be signed or authenticated attribute; MUST NOT be unsigned, etc. Single attribute value; multiple not allowed.

### 11.4 Countersignature
- OID: id-countersignature {1 2 840 113549 1 9 6}.
- Value type: Countersignature (SignerInfo). Countersigns the content octets of the signatureValue OCTET STRING (not tag/length).
- MUST be unsigned attribute; MUST NOT be signed, authenticated, unauthenticated, or unprotected.
- **Rules**: signedAttributes MUST NOT contain content-type attribute; MUST contain message-digest if any other attributes present.
- Input to message digest: content octets of DER encoding of the signatureValue field of the associated SignerInfo.
- Can have multiple attribute values.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementation MUST implement ContentInfo, data, signed-data, and enveloped-data content types. | shall | Section 2 |
| R2 | Additional content types (digested-data, encrypted-data, authenticated-data) MAY be implemented. | may | Section 2 |
| R3 | SignedAttributes and AuthAttributes MUST be DER encoded. | shall | Sections 5.3, 9.1 |
| R4 | SignedAttributes MUST contain content-type and message-digest attributes when present. | shall | Section 5.3 |
| R5 | AuthAttributes MUST contain content-type and message-digest attributes when present. | shall | Section 9.1 |
| R6 | content-type attribute MUST match encapContentInfo eContentType in signed-data and authenticated-data. | shall | Sections 5.6, 9.3 |
| R7 | Message digest calculation: if signedAttrs absent, input is value of eContent OCTET STRING; if present, input is DER of signedAttrs (EXPLICIT SET OF). | shall | Section 5.4 |
| R8 | SignerInfo version: if issuerAndSerialNumber -> v1; if subjectKeyIdentifier -> v3. | shall | Section 5.3 |
| R9 | Implementations MUST support both issuerAndSerialNumber and subjectKeyIdentifier forms of SignerIdentifier for reception. | shall | Section 5.3 |
| R10 | SubjectKeyIdentifier MUST be used to refer to public key in non-X.509 certificate. | shall | Section 5.3 |
| R11 | SignedData version assignment rules as per Section 5.1. | shall | Section 5.1 |
| R12 | EnvelopedData version assignment rules as per Section 6.1. | shall | Section 6.1 |
| R13 | RecipientInfos in EnvelopedData MUST have at least one element. | shall | Section 6.1 |
| R14 | Implementations MUST support key transport, key agreement, and KEK recipient info types. | shall | Section 6.2 |
| R15 | Implementations MUST gracefully handle unimplemented RecipientInfo types, versions, and unknown ori. | shall | Section 6.2 |
| R16 | KeyTransRecipientInfo: for X.509 v3 cert with key usage extension, MUST assert keyEncipherment bit for recipient. | shall | Section 6.2.1 |
| R17 | KeyAgreeRecipientInfo: version MUST be 3. Implementations MUST support all three originator alternatives. | shall | Section 6.2.2 |
| R18 | KeyAgreeRecipientInfo: for X.509 v3 cert with key usage, MUST assert keyAgreement bit for recipient. | shall | Section 6.2.2 |
| R19 | KEKRecipientInfo: version MUST be 4. | shall | Section 6.2.3 |
| R20 | PasswordRecipientInfo: version MUST be 0. | shall | Section 6.2.4 |
| R21 | DigestedData version: if id-data -> v0; else v2. | shall | Section 7 |
| R22 | EncryptedData version: if unprotectedAttrs present -> v2; else v0. | shall | Section 8 |
| R23 | AuthenticatedData version: as per rules in Section 9.1. | shall | Section 9.1 |
| R24 | AuthenticatedData: if digestAlgorithm present, authAttrs MUST be present. | shall | Section 9.1 |
| R25 | AuthenticatedData: MAC verification – recipient's computed MAC MUST equal mac field. | shall | Section 9.3 |
| R26 | content-type attribute MUST be signed or authenticated; MUST NOT be unsigned/unauthenticated/unprotected. | shall | Section 11.1 |
| R27 | message-digest attribute MUST be signed or authenticated; MUST NOT be unsigned/unauthenticated/unprotected. | shall | Section 11.2 |
| R28 | signing-time attribute MUST be signed or authenticated; MUST NOT be unsigned/unauthenticated/unprotected. | shall | Section 11.3 |
| R29 | countersignature attribute MUST be unsigned; MUST NOT be signed/authenticated/unauthenticated/unprotected. | shall | Section 11.4 |
| R30 | Countersignature signedAttributes MUST NOT contain content-type. | shall | Section 11.4 |
| R31 | Countersignature signedAttributes MUST contain message-digest if any other attributes present. | shall | Section 11.4 |

## Informative Annexes (Condensed)
- **Section 1.1 Evolution**: Summarizes changes from PKCS #7 v1.5 through RFC 2630, 3369, 3852, to this version. Key: algorithm independence, password-based key management added, extension mechanisms for certificates/revocation info.
- **Section 5.2.1 Compatibility with PKCS #7**: Describes differences in SignedData encoding for non-Data types. Strategies: fallback decode; adjust eContent encoding based on object identifier.
- **Section 14 Security Considerations**: 
  - Protect private keys, key management private keys, content-encryption keys, message-authentication keys.
  - Key management for MAC must provide data origin authentication; Static-Static Diffie-Hellman does if keys bound to identities.
  - Use adequate random number generation (RFC 4086).
  - Ensure key-encryption algorithms are as strong as content-encryption algorithms.
  - Countersignature implementations should verify original signature or ensure appropriate context before countersigning.
- **Section 15 Acknowledgments**: Contributors listed.
- **Author's Address**: Russell Housley, Vigil Security.