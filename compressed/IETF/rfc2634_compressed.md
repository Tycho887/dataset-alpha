# RFC 2634: Enhanced Security Services for S/MIME
**Source**: IETF – Network Working Group | **Version**: Standards Track | **Date**: June 1999 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc2634

## Scope (Summary)
This document specifies four optional security service extensions for S/MIME v3: signed receipts, security labels, secure mailing lists, and signing certificates. It defines procedures and attributes necessary to implement these services, using ASN.1:1988 syntax.

## Normative References
- [ASN1-1988] ITU-T X.208
- [CERT] RFC 2632, S/MIME Version 3 Certificate Handling
- [CMS] RFC 2630, Cryptographic Message Syntax
- [MSG] RFC 2633, S/MIME Version 3 Message Specification
- [MUSTSHOULD] BCP 14, RFC 2119
- [MSP4] SDNS Message Security Protocol 4.0
- [MTSABS] ITU-T X.411 (Message Transfer System: Abstract Service Definition)
- [SMIME2] RFC 2311, RFC 2312
- [UTF8] RFC 2279

## Definitions and Abbreviations
- **Triple wrapping**: Sign, then encrypt, then sign again.
- **MLA**: Mail List Agent
- **Receipt**: Signed message proving delivery and signature verification.
- **Security Label**: Set of security information regarding content sensitivity.
- **Signing Certificate Attribute**: Cryptographically binds the signer’s certificate to the signature.
- **ESSVersion**: INTEGER { v1(1) }
- **ub-receiptsTo**: INTEGER ::= 16
- **ub-ml-expansion-history**: INTEGER ::= 64
- **ub-integer-options**: INTEGER ::= 256
- **ub-privacy-mark-length**: INTEGER ::= 128
- **ub-security-categories**: INTEGER ::= 64

## 1. Introduction
- Extensions apply to S/MIME v3 ([MSG], [CERT]) and can partially apply to v2.
- Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per [MUSTSHOULD]).
- ASN.1:1988 used.

### 1.1 Triple Wrapping
- **Triple wrapped message**: signed, then encrypted, then signed again.
- **Purpose**: Inner signature for integrity/non-repudiation; encryption for confidentiality; outer signature for hop-by-hop attributes.

#### Steps for Triple Wrapping (Normative)
1. Start with original content.
2. Encapsulate with MIME Content-type headers (exception: signed receipt not put in MIME headers).
3. Sign the result: SignedData encapContentInfo eContentType MUST be id-data. If multipart/signed, eContent MUST be absent. If application/pkcs7-mime, eContent MUST contain step 2.
4. Add MIME construct as defined in [MSG]. (Inside signature)
5. Encrypt as application/pkcs7-mime. EnvelopedData encryptedContentInfo contentType MUST be id-data.
6. Add MIME headers: Content-type application/pkcs7-mime with parameters.
7. Sign result of step 6 as in step 3.
8. Add MIME construct from step 4. (Outside signature)

### 1.2 Format of a Triple Wrapped Message
- Receiving agents MUST be able to interpret both multipart/signed and application/pkcs7-mime signature structures.
- Detailed ASN.1 and MIME layering described (preserved in original).

### 1.3 Security Services and Triple Wrapping
- **Signed Receipts**: Receipt request MUST be in inside signature; MLA may change receipt policy in outside signature.
- **Security Labels**: May be in either signature. Inner label for plaintext access control; outer label for encrypted message routing. eSSSecurityLabel attribute MUST NOT be used in EnvelopedData or unsigned attributes.
- **Secure Mailing Lists**: MLA never changes inner signature data; adds/updates mlExpansionHistory attribute; adds/replaces outer signature.
- **Placement of Attributes**: Table provided (see below). Certain attributes MUST be in SignedAttributes or AuthAttributes; some MUST NOT be in UnsignedAttributes, etc.

#### Attribute Placement Table
| Attribute | OID | Inner/Outer | Signed |
|-----------|-----|-------------|--------|
| contentHints | id-aa-contentHint [ESS] | either | MAY |
| contentIdentifier | id-aa-contentIdentifier [ESS] | either | MAY |
| contentReference | id-aa-contentReference [ESS] | either | MUST |
| contentType | id-contentType [CMS] | either | MUST |
| counterSignature | id-countersignature [CMS] | either | MUST NOT |
| equivalentLabel | id-aa-equivalentLabels [ESS] | either | MUST |
| eSSSecurityLabel | id-aa-securityLabel [ESS] | either | MUST |
| messageDigest | id-messageDigest [CMS] | either | MUST |
| msgSigDigest | id-aa-msgSigDigest [ESS] | inner only | MUST |
| mlExpansionHistory | id-aa-mlExpandHistory [ESS] | outer only | MUST |
| receiptRequest | id-aa-receiptRequest [ESS] | inner only | MUST |
| signingCertificate | id-aa-signingCertificate [ESS] | either | MUST |
| signingTime | id-signingTime [CMS] | either | MUST |
| smimeCapabilities | sMIMECapabilities [MSG] | either | MUST |
| sMIMEEncryptionKeyPreference | id-aa-encrypKeyPref [MSG] | either | MUST |

- A SignerInfo MUST NOT include multiple instances of any ESS attribute types.
- For all ESS attribute types, if present, MUST include exactly one instance of AttributeValue.
- counterSignature MUST be in unsigned attributes; allowed only counterSignature, messageDigest, signingTime, signingCertificate.

### 1.4 Required and Optional Attributes
- Gateway adding a signerInfo to existing signedData MUST copy mlExpansionHistory and eSSSecurityLabel attributes from other signerInfos.
- It is safer to wrap messages with new signatures than to insert signerInfos.

### 1.5 Object Identifiers
- OIDs defined in [CMS], [MSG], [CERT]; registry at <http://www.imc.org/ietf-smime/oids.html>; IANA to maintain.

## 2. Signed Receipts

### 2.1 Signed Receipt Concepts
- Receipt provides proof of delivery and signature verification.
- Receiving user agent software SHOULD automatically create a signed receipt when requested.
- Sending agent SHOULD remember to avoid re-sending receipt.
- Receipt request can indicate receipts sent to multiple places; sender SHOULD NOT request receipts be sent to anyone without exact copy of message.

### 2.2 Receipt Request Creation (Normative)
- Receipts may be requested only for the innermost SignedData layer in a multi-layer S/MIME message.
- Only one receiptRequest attribute per SignerInfo.
- ReceiptRequest attribute MUST NOT be included in a SignedData object that encapsulates a Receipt content.
- Steps:
  1. Create receiptRequest data structure.
  2. Assign signedContentIdentifier.
  3. Set receiptsFrom.
  4. Populate receiptsTo with GeneralNames for each entity; MUST include originator if desired.
  5. Place in signedAttributes.

#### 2.2.1 Multiple Receipt Requests
- Multiple SignerInfos may have receiptRequests; each recipient SHOULD return only one signed receipt.
- All receiptRequest attributes in a SignedData MUST be identical.

#### 2.2.2 Information Needed to Validate Signed Receipts
- Sender must retain original signedData or message signature digest and Receipt content digest values.

### 2.3 Receipt Request Processing (Normative)
- Receiving agent MUST verify signature covering receiptRequest before processing.
- If multiple receiptRequest attributes in verified SignerInfos are not identical, MUST NOT return any signed receipt.
- If mlExpansionHistory present in outermost signedData, apply rules:
  - mlReceiptPolicy absent: SHOULD examine receiptRequest.
  - mlReceiptPolicy none: MUST NOT create receipt.
  - mlReceiptPolicy insteadOf/inAdditionTo: SHOULD examine receiptsFrom; send to designated entities.
- If receiptsFrom allOrFirstTier:
  - allReceipts: SHOULD create receipt.
  - firstTierRecipients: if mlExpansionHistory present, MUST NOT create; else SHOULD create.
- If receiptsFrom receiptList: if recipient in list, SHOULD create receipt; else MUST NOT.
- Flow chart provided (see original).

### 2.4 Signed Receipt Creation
- Must verify original signature first.
- Steps:
  1. Verify original signedData signerInfo signature.
  2. Create Receipt structure: version=1, contentType from original, signedContentIdentifier, originatorSignatureValue.
  3. DER encode Receipt.
  4. Digest D1 for messageDigest attribute.
  5. Include msgSigDigest attribute (digest of original signedAttributes).
  6. Include contentType attribute with id-ct-receipt.
  7. Include signingTime attribute (SHOULD).
  8. Digest signedAttributes for signature.
  9. DER encoded Receipt MUST be directly inside signedData encapContentInfo eContent; id-ct-receipt MUST be eContentType; Data content type MUST NOT be used; Receipt MUST NOT be encapsulated in MIME header.
  10. Wrap in application/pkcs7-mime with smime-type="signed-receipt".
  11. If encrypted, create outer signedData with contentHints attribute containing id-ct-receipt.
- All sending agents MUST provide ability to send encrypted signed receipts.

#### 2.4.1 MLExpansionHistory Attributes and Receipts
- MUST NOT be included in a SignedData object encapsulating a Receipt.

### 2.5 Determining Recipients of Signed Receipt
- ReceiptsTo from receiptRequest is initial sequence.
- If mlExpansionHistory present and last MLData has insteadOf, replace with insteadOf.
- If inAdditionTo, add inAdditionTo to sequence.

### 2.6 Signed Receipt Validation
- Identified by id-ct-receipt in encapContentInfo eContentType.
- Steps:
  - Decode signedData.
  - Extract contentType, signedContentIdentifier, originatorSignatureValue.
  - Obtain message signature digest value (from sender or recalc).
  - Compare with msgSigDigest attribute; if different, fail.
  - Obtain Receipt content digest value (sender or recalc).
  - Compare with messageDigest attribute; if different, fail.
  - Digest signedAttributes of receipt signerInfo.
  - Verify signature; if fail, process fails.

### 2.7 Receipt Request Syntax (ASN.1)
```
ReceiptRequest ::= SEQUENCE {
  signedContentIdentifier ContentIdentifier,
  receiptsFrom ReceiptsFrom,
  receiptsTo SEQUENCE SIZE (1..ub-receiptsTo)) OF GeneralNames }
ub-receiptsTo INTEGER ::= 16
id-aa-receiptRequest OBJECT IDENTIFIER ::= { ... }
ContentIdentifier ::= OCTET STRING
id-aa-contentIdentifier OBJECT IDENTIFIER ::= { ... }
ReceiptsFrom ::= CHOICE {
  allOrFirstTier [0] AllOrFirstTier,
  receiptList [1] SEQUENCE OF GeneralNames }
AllOrFirstTier ::= INTEGER { allReceipts (0), firstTierRecipients (1) }
```

### 2.8 Receipt Syntax (ASN.1)
```
Receipt ::= SEQUENCE {
  version ESSVersion,
  contentType ContentType,
  signedContentIdentifier ContentIdentifier,
  originatorSignatureValue OCTET STRING }
id-ct-receipt OBJECT IDENTIFIER ::= { ... }
ESSVersion ::= INTEGER { v1(1) }
```

### 2.9 Content Hints
- ContentHints ::= SEQUENCE { contentDescription UTF8String OPTIONAL, contentType ContentType }
- id-aa-contentHint OID given.
- Messages with signedData wrapped around envelopedData SHOULD include a contentHints attribute except for data content type.
- For encrypted signedData/Receipt, outer signedData MUST include contentHints with id-ct-receipt.

### 2.10 Message Signature Digest Attribute
- msgSigDigest ::= OCTET STRING; id-aa-msgSigDigest OID.
- Used only in signed attributes of a signed receipt.

### 2.11 Signed Content Reference Attribute
- ContentReference ::= SEQUENCE { contentType, signedContentIdentifier, originatorSignatureValue }
- Links one SignedData to another.

## 3. Security Labels

### 3.1 Security Label Processing Rules
- eSSSecurityLabel attribute MUST be in signedAttributes; MUST NOT be in unsigned attributes.
- If more than one SignerInfo in a SignedData, all MUST have identical eSSSecurityLabel if any has it.
- Receiving agent MUST verify signature covering eSSSecurityLabel before processing.
- Must process first verified eSSSecurityLabel; if not identical across verified SignerInfos, MUST warn user.
- If security-policy-identifier not recognized, SHOULD stop processing and indicate error.

### 3.2 Syntax of eSSSecurityLabel (ASN.1)
```
ESSSecurityLabel ::= SET {
  security-policy-identifier SecurityPolicyIdentifier,
  security-classification SecurityClassification OPTIONAL,
  privacy-mark ESSPrivacyMark OPTIONAL,
  security-categories SecurityCategories OPTIONAL }
id-aa-securityLabel OID ::= { ... }
SecurityPolicyIdentifier ::= OBJECT IDENTIFIER
SecurityClassification ::= INTEGER { unmarked(0) ... top-secret(5) } (0..256)
ESSPrivacyMark ::= CHOICE { pString, utf8String }
SecurityCategories ::= SET SIZE (1..64) OF SecurityCategory
SecurityCategory ::= SEQUENCE { type [0] OID, value [1] ANY DEFINED BY type }
```

### 3.3 Security Label Components
- Security Policy Identifier: identifies policy in force.
- Security Classification: hierarchical values defined by policy; integers 0-5 reserved for X.411 basic hierarchy (unmarked, unclassified, restricted, confidential, secret, top-secret); SHOULD NOT use 0-5 for other meanings.
- Privacy Mark: not for access control; defined by policy or originator.
- Security Categories: further granularity; syntax defined by policy.

### 3.4 Equivalent Security Labels
- EquivalentLabels ::= SEQUENCE OF ESSSecurityLabel; id-aa-equivalentLabels OID.
- MAY be included in addition to eSSSecurityLabel; all signerInfos MUST have same eSSSecurityLabel.
- EquivalentLabels MUST be signed attribute; MUST NOT be unsigned.
- MUST include only one instance of AttributeValue.
- Receiving agent MUST validate signature on EquivalentLabels; MUST NOT act unless signed by trusted entity.
- If eSSSecurityLabel policy understood, MUST process that and ignore EquivalentLabels.

## 4. Mail List Management

### 4.1 Mail List Expansion
- MLA MUST add an MLData record with its ID, expansion time, optional receipt policy to end of mlExpansionHistory sequence.
- If mlExpansionHistory absent, MLA adds it.
- Only one mlExpansionHistory per SignerInfo.
- If MLA creates multiple SignerInfos, all MUST have identical mlExpansionHistory.
- Recipient MUST verify signature covering mlExpansionHistory before processing; MUST NOT process unless all verified mlExpansionHistory attributes identical; otherwise stop and notify.

#### 4.1.1 Detecting Mail List Expansion Loops
- Examines mailListIdentifier field; if own ID found, discontinue expansion and notify administrator.

### 4.2 Mail List Agent Processing
- MLA MUST parse all layers to find eSSSecurityLabel attributes; MUST verify signatures before using.
- MLA MUST sign message to ML members in new outer signedData layer; MUST include all signed attributes from original outer signedData (unless replaced), including mlExpansionHistory.
- Detailed processing rules for EnvelopedData, SignedData, data (see subsections 4.2.3.1-4.2.3.3).
- Flow chart provided.

### 4.3 Mail List Agent Signed Receipt Policy Processing
- Table for union of policies A and B (see original).

### 4.4 Mail List Expansion History Syntax (ASN.1)
```
MLExpansionHistory ::= SEQUENCE SIZE (1..64) OF MLData
id-aa-mlExpandHistory OID ::= { ... }
MLData ::= SEQUENCE {
  mailListIdentifier EntityIdentifier,
  expansionTime GeneralizedTime,
  mlReceiptPolicy MLReceiptPolicy OPTIONAL }
EntityIdentifier ::= CHOICE { issuerAndSerialNumber, subjectKeyIdentifier }
MLReceiptPolicy ::= CHOICE { none [0] NULL, insteadOf [1] SEQUENCE OF GeneralNames, inAdditionTo [2] SEQUENCE OF GeneralNames }
```

## 5. Signing Certificate Attribute
- Prevents certificate substitution and re-issue attacks; binds certificate identifier to signature.

### 5.1 Attack Descriptions
- Substitution, Reissue of Certificate, Rogue Duplicate CA.

### 5.2 Attack Responses
- Denial of service not preventable; using hash of certificate prevents substitution of valid certificate; re-issue of CA certificates not fully addressed; rogue CA avoided by not trusting it.

### 5.3 Related Signature Verification Context
- Authorization certificates and policy information can be bound via signingCertificate attribute.

### 5.4 Signing Certificate Attribute Definition (ASN.1)
```
SigningCertificate ::= SEQUENCE {
  certs SEQUENCE OF ESSCertID,
  policies SEQUENCE OF PolicyInformation OPTIONAL }
id-aa-signingCertificate OID ::= { ... }
ESSCertID ::= SEQUENCE { certHash Hash, issuerSerial IssuerSerial OPTIONAL }
Hash ::= OCTET STRING (SHA1 hash of entire certificate)
IssuerSerial ::= SEQUENCE { issuer GeneralNames, serialNumber CertificateSerialNumber }
```
- First ESSCertID MUST be the signing certificate; hash must match; if not, signature invalid.
- Subsequent ESSCertIDs limit authorization certificates.
- If present, MUST be signed attribute; MUST NOT be unsigned; MUST include exactly one instance of AttributeValue.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R01 | SignedData encapContentInfo eContentType MUST be id-data when triple wrapping | shall | 1.1.2 Step 3 |
| R02 | EnvelopedData encryptedContentInfo contentType MUST be id-data | shall | 1.1.2 Step 5 |
| R03 | Receipt request MUST be in inside signature of triple wrapped message | shall | 1.3.1 |
| R04 | eSSSecurityLabel MUST NOT be used in EnvelopedData or unsigned attributes | shall | 1.3.2 |
| R05 | mlExpansionHistory MUST be in outer signature only | shall | 1.3.4 |
| R06 | receiptRequest MUST be in inner signature only | shall | 1.3.4 |
| R07 | All ESS attribute types MUST have exactly one AttributeValue if present | shall | 1.3.4 |
| R08 | counterSignature MUST be in unsigned attributes | shall | 1.3.4 |
| R09 | Gateway adding signerInfo MUST copy mlExpansionHistory and eSSSecurityLabel | shall | 1.4 |
| R10 | ReceiptRequest MUST NOT be in SignedData encapsulating Receipt | shall | 2.2 |
| R11 | All receiptRequests in a SignedData MUST be identical | shall | 2.2.1 |
| R12 | Recipient MUST NOT process unverified receiptRequest | shall | 2.3 |
| R13 | If mlReceiptPolicy is none, MUST NOT create receipt | shall | 2.3 |
| R14 | If verified receiptRequests not identical, MUST NOT return receipt | shall | 2.3 |
| R15 | Signed receipt MUST be created only after verifying original signature | shall | 2.4 |
| R16 | Receipt content MUST be directly encoded in signedData encapContentInfo eContent | shall | 2.4 Step 9 |
| R17 | Receipt content MUST NOT be encapsulated in MIME header | shall | 2.4 Step 9 |
| R18 | Sending agents MUST provide ability to send encrypted signed receipts | shall | 2.4 |
| R19 | MLExpansionHistory MUST NOT be in SignedData encapsulating Receipt | shall | 2.4.1 |
| R20 | eSSSecurityLabel MUST be in signedAttributes | shall | 3.1.1 |
| R21 | All SignerInfos in a SignedData MUST have identical eSSSecurityLabel if any has it | shall | 3.1.1 |
| R22 | Recipient MUST NOT process unverified eSSSecurityLabel | shall | 3.1.2 |
| R23 | If eSSSecurityLabels not identical, MUST warn user | shall | 3.1.2 |
| R24 | If security-policy-identifier not recognized, SHOULD stop processing | should | 3.1.2 |
| R25 | SecurityClassification values 0-5 reserved for X.411 hierarchy | shall | 3.3.2 |
| R26 | EquivalentLabels MUST be signed attribute | shall | 3.4.1 |
| R27 | EquivalentLabels MUST NOT have multiple AttributeValues | shall | 3.4.1 |
| R28 | Receiving agent MUST validate signature on EquivalentLabels | shall | 3.4.2 |
| R29 | MUST NOT act on EquivalentLabels unless signed by trusted entity | shall | 3.4.2 |
| R30 | MLA MUST add MLData to end of mlExpansionHistory | shall | 4.1 |
| R31 | If MLA creates multiple SignerInfos, all MUST have identical mlExpansionHistory | shall | 4.1 |
| R32 | Recipient MUST verify signature on mlExpansionHistory | shall | 4.1 |
| R33 | If verified mlExpansionHistory attributes not identical, MUST stop | shall | 4.1 |
| R34 | MLA MUST sign new outer signedData layer for ML members | shall | 4.2 |
| R35 | MLA MUST include all signed attributes from original outer signedData (unless replaced) | shall | 4.2 |
| R36 | SigningCertificate attribute MUST be signed | shall | 5.4 |
| R37 | First ESSCertID MUST be the signing certificate; hash must match; else signature invalid | shall | 5.4 |

## Informative Annexes (Condensed)
- **A. ASN.1 Module**: Complete ASN.1 definitions for ExtendedSecurityServices module (ess-2000). Includes all types and object identifiers referenced in main sections.
- **B. References**: List of normative references including RFCs, ITU-T standards, and industry specifications.
- **C. Acknowledgments**: Contributors listed.
- **Full Copyright Statement**: Copyright (C) The Internet Society (1999). All Rights Reserved.