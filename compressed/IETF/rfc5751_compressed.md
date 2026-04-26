# RFC 5751: Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.2 Message Specification
**Source**: IETF | **Version**: 3.2 | **Date**: January 2010 | **Type**: Standards Track (Normative)
**Original**: http://www.rfc-editor.org/info/rfc5751

## Scope (Summary)
This document defines S/MIME version 3.2, providing a consistent way to send and receive secure MIME data. Digital signatures provide authentication, message integrity, and non-repudiation; encryption provides confidentiality; compression reduces data size. It obsoletes RFC 3851.

## Normative References
- [CERT32] Ramsdell, B. and S. Turner, "Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.2 Certificate Handling", RFC 5750, January 2010.
- [CHARSETS] Character sets assigned by IANA. See http://www.iana.org/assignments/character-sets.
- [CMSAES] Schaad, J., "Use of the Advanced Encryption Standard (AES) Encryption Algorithm in Cryptographic Message Syntax (CMS)", RFC 3565, July 2003.
- [CMSALG] Housley, R., "Cryptographic Message Syntax (CMS) Algorithms", RFC 3370, August 2002.
- [CMSCOMPR] Gutmann, P., "Compressed Data Content Type for Cryptographic Message Syntax (CMS)", RFC 3274, June 2002.
- [CMS-SHA2] Turner, S., "Using SHA2 Algorithms with Cryptographic Message Syntax", RFC 5754, January 2010.
- [CONTDISP] Troost, R., Dorner, S., and K. Moore, Ed., "Communicating Presentation Information in Internet Messages: The Content-Disposition Header Field", RFC 2183, August 1997.
- [FIPS186-2] National Institute of Standards and Technology (NIST), "Digital Signature Standard (DSS)", FIPS Publication 186-2, January 2000. [With Change Notice 1].
- [FIPS186-3] National Institute of Standards and Technology (NIST), FIPS Publication 186-3: Digital Signature Standard, June 2009.
- [MIME-SECURE] Galvin, J., Murphy, S., Crocker, S., and N. Freed, "Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted", RFC 1847, October 1995.
- [MUSTSHOULD] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RANDOM] Eastlake, D., 3rd, Schiller, J., and S. Crocker, "Randomness Requirements for Security", BCP 106, RFC 4086, June 2005.
- [RFC2045] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies", RFC 2045, November 1996.
- [RFC2046] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996.
- [RFC2047] Moore, K., "MIME (Multipurpose Internet Mail Extensions) Part Three: Message Header Extensions for Non-ASCII Text", RFC 2047, November 1996.
- [RFC2049] Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Five: Conformance Criteria and Examples", RFC 2049, November 1996.
- [RFC2634] Hoffman, P. Ed., "Enhanced Security Services for S/MIME", RFC 2634, June 1999.
- [RFC4288] Freed, N. and J. Klensin, "Media Type Specifications and Registration Procedures", BCP 13, RFC 4288, December 2005.
- [RFC4289] Freed, N. and J. Klensin, "Multipurpose Internet Mail Extensions (MIME) Part Four: Registration Procedures", BCP 13, RFC 4289, December 2005.
- [RFC5035] Schaad, J., "Enhanced Security Services (ESS) Update: Adding CertID Algorithm Agility", RFC 5035, August 2007.
- [RFC5652] Housley, R., "Cryptographic Message Syntax (CMS)", RFC 5652, September 2009.
- [RSAOAEP] Housley, R. "Use of the RSAES-OAEP Key Transport Algorithm in the Cryptographic Message Syntax (CMS)", RFC 3560, July 2003.
- [RSAPSS] Schaad, J., "Use of the RSASSA-PSS Signature Algorithm in Cryptographic Message Syntax (CMS)", RFC 4056, June 2005.
- [SP800-56A] National Institute of Standards and Technology (NIST), Special Publication 800-56A: Recommendation Pair-Wise Key Establishment Schemes Using Discrete Logarithm Cryptography (Revised), March 2007.
- [X.680] ITU-T Recommendation X.680 (2002) | ISO/IEC 8824-1:2002. Information Technology - Abstract Syntax Notation One (ASN.1): Specification of basic notation.
- [X.690] ITU-T Recommendation X.690 (2002) | ISO/IEC 8825-1:2002. Information Technology - ASN.1 encoding rules: Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER).

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One, as defined in ITU-T Recommendation X.680 [X.680].
- **BER**: Basic Encoding Rules for ASN.1, as defined in ITU-T Recommendation X.690 [X.690].
- **Certificate**: A type that binds an entity's name to a public key with a digital signature.
- **DER**: Distinguished Encoding Rules for ASN.1, as defined in ITU-T Recommendation X.690 [X.690].
- **7-bit data**: Text data with lines less than 998 characters long, none of the characters have the 8th bit set, and no NULL characters. <CR> and <LF> occur only as part of a <CR><LF> end-of-line delimiter.
- **8-bit data**: Text data with lines less than 998 characters, none of the characters are NULL. <CR> and <LF> occur only as part of a <CR><LF> end-of-line delimiter.
- **Binary data**: Arbitrary data.
- **Transfer encoding**: A reversible transformation made on data so 8-bit or binary data can be sent via a channel that only transmits 7-bit data.
- **Receiving agent**: Software that interprets and processes S/MIME CMS objects, MIME body parts that contain CMS content types, or both.
- **Sending agent**: Software that creates S/MIME CMS content types, MIME body parts that contain CMS content types, or both.
- **S/MIME agent**: User software that is a receiving agent, a sending agent, or both.
- **SHOULD+**: Same as SHOULD; expected to be promoted to MUST in future.
- **SHOULD-**: Same as SHOULD; expected to be demoted to MAY in future.
- **MUST-**: Same as MUST; expected to not remain a MUST in future document, but at least SHOULD or SHOULD-.

## 1. Introduction
S/MIME provides authentication, message integrity, non-repudiation (digital signatures), data confidentiality (encryption), and compression for electronic messaging. It can be used with any transport that transports MIME data (e.g., HTTP, SIP).

### 1.1. Specification Overview
Defines how to create a MIME body part cryptographically enhanced according to CMS, and defines application/pkcs7-mime media type. Also discusses multipart/signed with application/pkcs7-signature. S/MIME agents MUST follow this specification and references [CMS], [CMSALG], [RSAPSS], [RSAOAEP], and [CMS-SHA2]. "Be liberal in what you receive and conservative in what you send."

### 1.4. Compatibility with Prior Practice
S/MIME v3.2 agents ought to attempt greatest interoperability with prior versions (v2 [SMIMEv2], v3 [SMIMEv3], v3.1 [SMIMEv3.1]).

### 1.5. Changes from S/MIME v3 to v3.1
- RSA key wrapping MUST, DH SHOULD.
- AES symmetric encryption SHOULD.
- RSA signature MUST.
- Clarified use of empty SignedData for certificates and CRLs.
- Binary encoding discussed.
- Header protection via message/rfc822.
- CompressedData CMS type allowed.

### 1.6. Changes since S/MIME v3.1
- Editorial updates.
- Added definitions for SHOULD+, SHOULD-, MUST-.
- References to RSASSA-PSS, RSAES-OAEP, SHA2.
- SHA-256 added as MUST for digest; SHA-1 and MD5 made SHOULD-.
- Signature algorithms: RSA with SHA-256 MUST, DSA with SHA-256 SHOULD+, RSASSA-PSS with SHA-256 SHOULD+, RSA with SHA-1, DSA with SHA-1, RSA with MD5 SHOULD-.
- Key encryption: DH SHOULD-, RSAES-OAEP SHOULD+.
- Content encryption: AES-128 CBC MUST, AES-192/256 CBC SHOULD+, tripleDES SHOULD-.
- Key size updates for RSA and DSA.

## 2. CMS Options
CMS options to achieve base interoperability. See [CMSALG] and [CMS-SHA2] for details, [ESS] for additional attributes.

### 2.1. DigestAlgorithmIdentifier
- **R-Dig-1**: Sending and receiving agents MUST support SHA-256 [CMS-SHA2].
- **R-Dig-2**: Sending and receiving agents SHOULD- support SHA-1 [CMSALG].
- **R-Dig-3**: Receiving agents SHOULD- support MD5 [CMSALG] for backward compatibility with S/MIME v2 SignedData.

### 2.2. SignatureAlgorithmIdentifier
Receiving agents:
- MUST support RSA with SHA-256.
- SHOULD+ support DSA with SHA-256.
- SHOULD+ support RSASSA-PSS with SHA-256.
- SHOULD- support RSA with SHA-1.
- SHOULD- support DSA with SHA-1.
- SHOULD- support RSA with MD5.

Sending agents:
- MUST support RSA with SHA-256.
- SHOULD+ support DSA with SHA-256.
- SHOULD+ support RSASSA-PSS with SHA-256.
- SHOULD- support RSA with SHA-1 or DSA with SHA-1.
- SHOULD- support RSA with MD5.

Note: v3.1 clients support id-dsa-with-sha1 and rsaEncryption; v3 clients might only use id-dsa-with-sha1; v2 clients only rsaEncryption with SHA-1 or MD5.

### 2.3. KeyEncryptionAlgorithmIdentifier
Receiving and sending agents:
- MUST support RSA Encryption [CMSALG].
- SHOULD+ support RSAES-OAEP [RSAOAEP].
- SHOULD- support DH ephemeral-static mode [CMSALG][SP800-57].

When DH ephemeral-static is used, key wrap algorithm MUST be same key size as content encryption algorithm; AES-128 key wrap MUST be supported when DH used (since AES-128 CBC is mandatory content encryption).

### 2.4. General Syntax
Only Data, SignedData, EnvelopedData, and CompressedData used for S/MIME.

#### 2.4.1. Data Content Type
- **R-Data-1**: Sending agents MUST use id-data content type identifier to identify the "inner" MIME message content.

#### 2.4.2. SignedData Content Type
- **R-Signed-1**: Sending agents MUST use SignedData content type to apply digital signature or, in degenerate case (no signatures), to convey certificates.

#### 2.4.3. EnvelopedData Content Type
Used to apply data confidentiality. Sender needs public key of each recipient.

#### 2.4.4. CompressedData Content Type
Used to apply data compression only; no authentication or confidentiality.

### 2.5. Attributes and the SignerInfo Type
Receiving agents MUST handle zero or one instance of each signed attribute. Sending agents SHOULD generate one instance of:
- Signing Time (2.5.1)
- SMIME Capabilities (2.5.2)
- Encryption Key Preference (2.5.3)
- Message Digest [CMS]
- Content Type [CMS]

Receiving agents SHOULD handle zero or one instance of signingCertificate or signingCertificatev2 [ESS]. Sending agents SHOULD generate one instance of signingCertificate or signingCertificatev2.

#### 2.5.1. Signing Time Attribute
- **R-SigTime-1**: Sending agents MUST encode signing time through year 2049 as UTCTime; times in 2050 or later MUST be encoded as GeneralizedTime.
- **R-SigTime-2**: When UTCTime is used, interpret YY: if YY >= 50, year = 19YY; if YY < 50, year = 20YY.
- **R-SigTime-3**: Receiving agents MUST be able to process signing-time attributes encoded in UTCTime or GeneralizedTime.

#### 2.5.2. SMIME Capabilities Attribute
- **R-SMIMECap-1**: If present, SMIMECapabilities MUST be a SignedAttribute; MUST NOT be UnsignedAttribute.
- **R-SMIMECap-2**: SignedAttributes in a signerInfo MUST NOT include multiple instances of SMIMECapabilities attribute.
- **R-SMIMECap-3**: SMIMECapabilities attribute MUST only include a single instance of AttributeValue; MUST NOT be zero or multiple.
- **R-SMIMECap-4**: For any capability, associated parameters MUST specify all parameters necessary to differentiate between two instances of the same algorithm.
- **R-SMIMECap-5**: If no differentiating parameters, parameters MUST be omitted, MUST NOT be encoded as NULL.
- **R-SMIMECap-6**: Receiving agents MUST handle SMIMECapabilities with unrecognized values gracefully.

#### 2.5.3. Encryption Key Preference Attribute
- **R-EncKeyPref-1**: If present, SMIMEEncryptionKeyPreference MUST be a SignedAttribute; MUST NOT be UnsignedAttribute.
- **R-EncKeyPref-2**: SignedAttributes in signerInfo MUST NOT include multiple instances.
- **R-EncKeyPref-3**: MUST only include a single instance of AttributeValue.
- **R-EncKeyPref-4**: Sending agent SHOULD include referenced certificate in set of certificates; MAY be omitted if previously made available.
- **R-EncKeyPref-5**: Sending agents SHOULD use this attribute if preferred encryption certificate differs from signing certificate.
- **R-EncKeyPref-6**: Receiving agents SHOULD store preference data if signature is valid and signing time > stored value; SHOULD respect sender's preference if possible.

##### 2.5.3.1. Selection of Recipient Key Management Certificate
Steps to determine key management certificate for future CMS EnvelopedData:
1. If SMIMEEncryptionKeyPreference found in SignedData from recipient, use that certificate.
2. Else search for X.509 certificate with same subject name as signer that can be used for key management.
3. Or use other method; if none found, cannot encrypt.

### 2.6. SignerIdentifier SignerInfo Type
- **R-SignerId-1**: S/MIME v3.2 implementations MUST support both issuerAndSerialNumber and subjectKeyIdentifier.
- **R-SignerId-2**: Implementations MUST be prepared for multiple certificates with same subjectKeyIdentifier value; MUST try each matching certificate during signature verification before error.

### 2.7. ContentEncryptionAlgorithmIdentifier
Sending and receiving agents:
- MUST support encryption and decryption with AES-128 CBC [CMSAES].
- SHOULD+ support AES-192 CBC and AES-256 CBC [CMSAES].
- SHOULD- support tripleDES (DES EDE3 CBC) [CMSALG].

#### 2.7.1. Deciding Which Encryption Method to Use
When creating encrypted message, use capabilities from received messages. Process:
- If no list for sender's public key, after verifying signature and timestamp, create list with signing time and symmetric capabilities.
- If list exists, verify signing time > stored and signature valid; if so, update.
- Values far in future or capabilities from unverifiable signatures MUST NOT be accepted.
- Before sending, MUST decide if weak encryption acceptable; if not, MUST NOT use weak algorithm.

##### 2.7.1.1. Rule 1: Known Capabilities
If sending agent has received capabilities from recipient, SHOULD use first capability in list (most preferred) that sending agent knows how to encrypt.

##### 2.7.1.2. Rule 2: Unknown Capabilities, Unknown Version
If no knowledge of recipient's encryption capabilities or S/MIME version, then SHOULD use AES-128; if not, SHOULD use tripleDES.

#### 2.7.2. Choosing Weak Encryption
Algorithms with 40-bit keys considered weak. Sending agent controlled by human SHOULD allow human to decide risks before sending, possibly use stronger encryption.

#### 2.7.3. Multiple Recipients
If capabilities do not overlap, sending agent forced to send more than one message. If sending same message with strong and weak encryption, attacker could learn contents from weakly encrypted copy.

## 3. Creating S/MIME Messages
S/MIME messages are combination of MIME bodies and CMS content types. Data to be secured is always a canonical MIME entity.

### 3.1. Preparing the MIME Entity for Signing, Enveloping, or Compressing
Steps:
1. MIME entity prepared per local conventions.
2. Leaf parts converted to canonical form.
3. Appropriate transfer encoding applied.

To protect outer headers, sending client MAY wrap full MIME message in message/rfc822; receiving client decides how to present inner header.

#### 3.1.1. Canonicalization
- **R-Canon-1**: Each MIME entity MUST be converted to canonical form uniquely and unambiguously representable in both signature creation and verification environments.
- **R-Canon-2**: MIME entities of major type "text" MUST have line endings as <CR><LF> and charset SHOULD be registered.
- **R-Canon-3**: When preparing text for signing, canonical representation for the charset MUST be used.

#### 3.1.2. Transfer Encoding
- **R-TE-1**: S/MIME implementations MUST be able to deal with binary MIME objects.
- **R-TE-2**: If no Content-Transfer-Encoding header, presumed 7BIT.
- **R-TE-3**: S/MIME implementations SHOULD use transfer encoding from 3.1.3 for all MIME entities they secure (to allow handling in any environment).
- **R-TE-4**: If all intended recipients capable of handling inner binary objects, SHOULD use binary encoding; else SHOULD use transfer encoding from 3.1.3.

#### 3.1.3. Transfer Encoding for Signing Using multipart/signed
If multipart/signed will be transmitted over 7-bit constrained transport, MUST have transfer encoding to 7-bit. Primary reason: Internet mail transport cannot guarantee 8-bit/binary transport; changing transfer encoding would invalidate signature.

### 3.2. The application/pkcs7-mime Media Type
Carries CMS EnvelopedData, SignedData, CompressedData. The carried CMS object always contains a MIME entity prepared per 3.1 if eContentType is id-data. Those using base-64 transfer encoding for SMTP.

- **R-app/pkcs7-mime-1**: Sending agent SHOULD include optional "smime-type" parameter in Content-Type to help receiving agent know contents.

#### 3.2.1. The name and filename Parameters
- **R-name-1**: Sending agents SHOULD emit optional "name" parameter to Content-Type for compatibility.
- **R-name-2**: Sending agents SHOULD emit optional Content-Disposition with "filename" parameter.
- **R-name-3**: Values SHOULD be filename with appropriate extension: .p7m (SignedData, EnvelopedData), .p7c (degenerate SignedData certificate management), .p7z (CompressedData), .p7s (application/pkcs7-signature).
- **R-name-4**: Filename SHOULD be limited to eight chars plus three-letter extension; use "smime" base to indicate S/MIME.
- **R-name-5**: Proper S/MIME implementation MUST use media types, not rely on file extensions.

#### 3.2.2. The smime-type Parameter
Defined smime-types: enveloped-data, signed-data, certs-only, compressed-data. Guideline for new smime-type: if both signing and encryption can be applied, assign "signed-*" and "enveloped-*". Common string for content OID; use "data" for id-data. If no common string, use "OID.<oid>".

### 3.3. Creating an Enveloped-Only Message
- **R-Enveloped-1**: The MIME entity prepared per 3.1.
- **R-Enveloped-2**: Process into CMS EnvelopedData; SHOULD include encrypted content-encryption key for originator [CMS].
- **R-Enveloped-3**: Wrap in ContentInfo, then in application/pkcs7-mime with smime-type=enveloped-data, extension .p7m.

### 3.4. Creating a Signed-Only Message
Two formats: application/pkcs7-mime with SignedData and multipart/signed. Multipart/signed preferred for sending; receiving agents MUST handle both.

#### 3.4.1. Choosing a Format
Multipart/signed can be viewed without S/MIME; SignedData protects content from benign modification.

#### 3.4.2. Signing Using application/pkcs7-mime with SignedData
Steps: prepare MIME entity, process into SignedData, wrap in ContentInfo, insert into application/pkcs7-mime with smime-type=signed-data, extension .p7m.

#### 3.4.3. Signing Using multipart/signed
Clear-signing format. Two parts: first part MIME entity to be signed; second part "detached signature" CMS SignedData with absent encapContentInfo eContent.

##### 3.4.3.1. The application/pkcs7-signature Media Type
- **R-app/pkcs7-sig-1**: Contains CMS ContentInfo with a single SignedData; encapContentInfo eContent MUST be absent.
- Extension .p7s.

##### 3.4.3.2. Creating a multipart/signed Message
Steps: prepare MIME entity per 3.1, obtain SignedData with absent eContent, insert MIME entity as first part, transfer-encode detached signature and insert as second part of type application/pkcs7-signature. Required parameters: protocol="application/pkcs7-signature", micalg parameter with digest algorithm values (md5, sha-1, sha-224, sha-256, sha-384, sha-512, or "unknown"). Receiving agents SHOULD recover gracefully from unrecognized micalg parameter.

### 3.5. Creating a Compressed-Only Message
Steps: prepare MIME entity per 3.1, process into CMS CompressedData, wrap in ContentInfo, insert into application/pkcs7-mime with smime-type=compressed-data, extension .p7z.

### 3.6. Multiple Operations
- **R-Nest-1**: S/MIME implementation MUST be able to receive and process arbitrarily nested S/MIME within reasonable resource limits.
- Operations may be applied in any order; security ramifications described.

### 3.7. Creating a Certificate Management Message
Transport certificates/CRLs. Steps: create SignedData with absent encapContentInfo eContent and empty signerInfos, wrap in ContentInfo, enclose in application/pkcs7-mime with smime-type=certs-only, extension .p7c.

### 3.8. Registration Requests
No specific certificate request mechanism required; S/MIME v2 used application/pkcs10 but not mandated.

### 3.9. Identifying an S/MIME Message
A message is S/MIME if it matches:
- Media type application/pkcs7-mime (any parameters, any file suffix)
- Media type multipart/signed with protocol="application/pkcs7-signature"
- Media type application/octet-stream with file suffix p7m, p7s, p7c, p7z

## 4. Certificate Processing
Receiving agent MUST provide certificate retrieval mechanism. Detailed in [CERT32].

### 4.1. Key Pair Generation
- **R-KeyGen-1**: All generated key pairs MUST be generated from a good source of non-deterministic random input [RANDOM].
- **R-KeyGen-2**: Private key MUST be protected in a secure fashion.
- **R-KeyGen-3**: MUST NOT generate asymmetric keys less than 512 bits for RSA or DSA signature algorithms.
- References for specific key sizes and algorithms provided.

### 4.2. Signature Generation (RSA, RSASSA-PSS, DSA)
- key size <= 1023: SHOULD NOT
- 1024 <= key size <= 2048: SHOULD
- 2048 < key size: MAY

### 4.3. Signature Verification (RSA, RSASSA-PSS, DSA)
- key size <= 1023: MAY
- 1024 <= key size <= 2048: MUST
- 2048 < key size: MAY

### 4.4. Encryption (for key establishment using RSA, RSA-OAEP, DH)
- key size <= 1023: SHOULD NOT
- 1024 <= key size <= 2048: SHOULD
- 2048 < key size: MAY

### 4.5. Decryption (RSA, RSAES-OAEP, DH)
- key size <= 1023: MAY
- 1024 <= key size <= 2048: MUST
- 2048 < key size: MAY

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R-Dig-1 | Sending and receiving agents MUST support SHA-256 for digest. | MUST | 2.1 |
| R-Dig-2 | Sending and receiving agents SHOULD- support SHA-1. | SHOULD- | 2.1 |
| R-Dig-3 | Receiving agents SHOULD- support MD5 for backward compatibility. | SHOULD- | 2.1 |
| R-Data-1 | Sending agents MUST use id-data content type for inner MIME content. | MUST | 2.4.1 |
| R-Signed-1 | Sending agents MUST use SignedData for signing or conveying certificates. | MUST | 2.4.2 |
| R-SigTime-1 | Signing time through 2049 MUST be UTCTime; 2050+ MUST be GeneralizedTime. | MUST | 2.5.1 |
| R-SigTime-2 | UTCTime interpretation: YY>=50 => 19YY; YY<50 => 20YY. | MUST | 2.5.1 |
| R-SigTime-3 | Receiving agents MUST process both UTCTime and GeneralizedTime. | MUST | 2.5.1 |
| R-SMIMECap-1 | SMIMECapabilities MUST be SignedAttribute, not UnsignedAttribute. | MUST | 2.5.2 |
| R-SMIMECap-2 | SignedAttributes MUST NOT include multiple instances. | MUST | 2.5.2 |
| R-SMIMECap-3 | AttributeValue MUST be single instance. | MUST | 2.5.2 |
| R-SMIMECap-4 | Parameters MUST differentiate algorithm instances. | MUST | 2.5.2 |
| R-SMIMECap-5 | No parameters => omit, not NULL. | MUST | 2.5.2 |
| R-SMIMECap-6 | Receiving agents MUST handle unrecognized values gracefully. | MUST | 2.5.2 |
| R-EncKeyPref-1 | SMIMEEncryptionKeyPreference MUST be SignedAttribute. | MUST | 2.5.3 |
| R-EncKeyPref-2 | No multiple instances. | MUST | 2.5.3 |
| R-EncKeyPref-3 | Single AttributeValue. | MUST | 2.5.3 |
| R-SignerId-1 | MUST support both issuerAndSerialNumber and subjectKeyIdentifier. | MUST | 2.6 |
| R-SignerId-2 | MUST be prepared for multiple certificates with same subjectKeyIdentifier. | MUST | 2.6 |
| R-Canon-1 | Each MIME entity MUST be canonicalized. | MUST | 3.1.1 |
| R-Canon-2 | Text type MUST have <CR><LF> line endings; charset SHOULD be registered. | MUST/SHOULD | 3.1.1 |
| R-Canon-3 | When signing, canonical charset representation MUST be used. | MUST | 3.1.1 |
| R-TE-1 | S/MIME implementations MUST handle binary MIME objects. | MUST | 3.1.2 |
| R-TE-2 | No Content-Transfer-Encoding => 7BIT. | MUST | 3.1.2 |
| R-TE-3 | SHOULD use 7-bit transfer encoding for all secured entities to ensure transportability. | SHOULD | 3.1.2 |
| R-TE-4 | If recipients known capable of binary, SHOULD use binary; else SHOULD use 7-bit. | SHOULD | 3.1.2 |
| R-app/pkcs7-mime-1 | SHOULD include smime-type parameter. | SHOULD | 3.2 |
| R-name-1 | SHOULD emit name parameter to Content-Type. | SHOULD | 3.2.1 |
| R-name-2 | SHOULD emit Content-Disposition filename. | SHOULD | 3.2.1 |
| R-name-3 | Filename SHOULD have appropriate extension. | SHOULD | 3.2.1 |
| R-name-4 | Filename SHOULD be 8.3; use "smime" base. | SHOULD | 3.2.1 |
| R-name-5 | MUST use media types, not rely on extensions. | MUST | 3.2.1 |
| R-Enveloped-1 | MUST prepare MIME entity per 3.1. | MUST | 3.3 Step 1 |
| R-Enveloped-2 | Process into EnvelopedData; SHOULD include originator key. | SHOULD | 3.3 Step 2 |
| R-Enveloped-3 | Wrap in ContentInfo, then application/pkcs7-mime. | MUST | 3.3 Steps 3-4 |
| R-app/pkcs7-sig-1 | Detached signature: encapContentInfo eContent MUST be absent. | MUST | 3.4.3.1 |
| R-Nest-1 | MUST receive and process arbitrarily nested S/MIME within resource limits. | MUST | 3.6 |
| R-KeyGen-1 | Key pair MUST be generated from good randomness. | MUST | 4.1 |
| R-KeyGen-2 | Private key MUST be protected securely. | MUST | 4.1 |
| R-KeyGen-3 | MUST NOT generate asymmetric keys <512 bits for RSA/DSA signatures. | MUST | 4.1 |

## Informative Annexes (Condensed)
- **Appendix A. ASN.1 Module**: Provides ASN.1 definitions for SecureMimeMessageV3dot1 module, including OIDs for smimeCapabilities, SMIMEEncryptionKeyPreference, id-cap-preferBinaryInside, etc. Unchanged from RFC 3851 except comment.
- **Appendix B. Moving S/MIME v2 Message Specification to Historic Status**: Recommends RFC 2311 be moved to Historic as v3, v3.1, and v3.2 are backwards compatible except dropped RC2/40 requirement.
- **Appendix C. Acknowledgments**: Thanks to contributors.