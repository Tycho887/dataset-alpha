# RFC 2633: S/MIME Version 3 Message Specification
**Source**: IETF – Standards Track | **Version**: 3 | **Date**: June 1999 | **Type**: Normative
**Original**: [RFC 2633](https://tools.ietf.org/html/rfc2633)

## Scope (Summary)
This document defines the S/MIME Version 3 protocol for adding cryptographic signature and encryption services to MIME data, using the Cryptographic Message Syntax (CMS). It specifies how to create and interpret secured MIME body parts (application/pkcs7-mime and multipart/signed) and provides requirements for sending and receiving agents to achieve interoperability.

## Normative References
- [MIME-SPEC] RFC 2045–2049 (MIME)
- [MIME-SECURE] RFC 1847 (Security Multiparts)
- [CMS] RFC 2630 (Cryptographic Message Syntax)
- [PKCS-7] RFC 2315
- [MUSTSHOULD] RFC 2119
- [DSS] FIPS PUB 186
- [SHA1] FIPS PUB 180-1
- [MD5] RFC 1321
- [DH] RFC 2631
- [PKCS-1] RFC 2437
- [3DES] ANSI X9.52
- [DES] ANSI X3.106
- [RC2] RFC 2268
- [ESS] RFC 2634
- [RANDOM] RFC 1750
- [CERT3] RFC 2632
- [CONTDISP] RFC 2183

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One (CCITT X.208)
- **BER**: Basic Encoding Rules for ASN.1 (X.209)
- **DER**: Distinguished Encoding Rules (X.509)
- **Certificate**: Binds an entity's distinguished name to a public key with a digital signature.
- **7-bit data**: Text lines <998 chars, no 8th bit, no NULL; CRLF only as line delimiter.
- **8-bit data**: Text lines <998 chars, no NULL; CRLF only.
- **Binary data**: Arbitrary data.
- **Transfer Encoding**: Reversible transformation for 7-bit transport.
- **Receiving agent**: Software that interprets and processes S/MIME CMS objects.
- **Sending agent**: Software that creates S/MIME CMS objects.
- **S/MIME agent**: User software that is a receiving agent, sending agent, or both.
- **MUST / SHOULD / MAY**: As per RFC 2119.

## 1. Introduction
- S/MIME provides authentication, integrity, non-repudiation (digital signatures) and privacy (encryption) for MIME data.
- Not restricted to mail; can be used with any MIME transport (e.g., HTTP).
- S/MIME v3 agents should maintain backward compatibility with v2 (RFC 2311–2315).

## 2. CMS Options
### 2.1 DigestAlgorithmIdentifier
- **R1**: Sending and receiving agents MUST support SHA-1.
- **R2**: Receiving agents SHOULD support MD5 for backward compatibility with S/MIME v2.

### 2.2 SignatureAlgorithmIdentifier
- **R3**: Sending and receiving agents MUST support id-dsa (DSS). Parameters MUST be absent (not NULL).
- **R4**: Receiving agents SHOULD support rsaEncryption.
- **R5**: Sending agents SHOULD support rsaEncryption.

### 2.3 KeyEncryptionAlgorithmIdentifier
- **R6**: Sending and receiving agents MUST support Diffie-Hellman (RFC 2631).
- **R7**: Receiving agents SHOULD support rsaEncryption.
- **R8**: Sending agents SHOULD support rsaEncryption.

### 2.4 General Syntax – Content Types
- Only Data, SignedData, and EnvelopedData are used for S/MIME.

#### 2.4.1 Data Content Type
- **R9**: Sending agents MUST use id-data for the encapContentInfo eContentType when applying signature or encryption. For signedData multipart/signed, eContent is absent. For envelopedData, encrypted content MUST be in encryptedContent OCTET STRING.

#### 2.4.2 SignedData Content Type
- **R10**: Sending agents MUST use signedData to apply a digital signature or to convey certificates (degenerate case).

#### 2.4.3 EnvelopedData Content Type
- Used for privacy; sender needs recipient’s public key. Does not provide authentication.

### 2.5 Attribute SignerInfo Type
- **R11**: Receiving agents MUST handle zero or one instance of each signed attribute listed (signingTime, sMIMECapabilities, sMIMEEncryptionKeyPreference).
- **R12**: Sending agents SHOULD generate one instance of each of the above signed attributes.
- **R13**: Receiving agents SHOULD handle zero or one instance of signingCertificate (from [ESS]).
- **R14**: Sending agents SHOULD generate one instance of signingCertificate.
- **R15**: Receiving agents SHOULD gracefully handle unrecognized attributes/values.
- **R16**: Sending agents SHOULD display non-listed signed attributes to the user.

#### 2.5.1 Signing-Time Attribute
- **R17**: Sending agents MUST encode signing time through 2049 as UTCTime; 2050+ as GeneralizedTime.
- **R18**: S/MIME agents MUST interpret UTCTime YY: if YY >= 50 then 19YY, else 20YY.

#### 2.5.2 SMIMECapabilities Attribute
- **R19**: SMIMECapabilities MUST be a SignedAttribute, NOT UnsignedAttribute.
- **R20**: signerInfo MUST NOT include multiple instances of SMIMECapabilities.
- **R21**: SMIMECapabilities MUST include only a single AttributeValue instance.
- **R22**: OIDs in the attribute SHOULD be ordered by preference within categories (signature, symmetric, key encipherment).
- **R23**: DER-encoding for each SMIMECapability MUST be identical across implementations.
- **R24**: For symmetric algorithms, parameters MUST specify all differentiating details (e.g., rounds, block size for RC5).
- **R25**: OIDs for algorithms SHOULD use the same OID as the algorithm, unless ambiguous; then a new OID under smimeCapabilities MUST be allocated.
- **R26**: Parameters for OIDs MUST be omitted if no differentiating parameters; MUST NOT be encoded as NULL.
- **R27**: Receiving agents MUST gracefully handle unrecognized SMIMECapabilities values.

#### 2.5.3 Encryption Key Preference Attribute
- **R28**: SMIMEEncryptionKeyPreference MUST be a SignedAttribute, NOT UnsignedAttribute.
- **R29**: signerInfo MUST NOT include multiple instances of SMIMEEncryptionKeyPreference.
- **R30**: Attribute MUST include only a single AttributeValue instance.
- **R31**: Sending agent SHOULD include the referenced certificate in the signed message’s certificate set.
- **R32**: Sending agents SHOULD use this attribute if preferred encryption certificate differs from signing certificate.
- **R33**: Receiving agents SHOULD store preference data if signature is valid and signing time is greater than currently stored value (account for clock skew).
- **R34**: Receiving agents SHOULD respect sender’s encryption key preference if possible.

##### 2.5.3.1 Selection of Recipient Key Management Certificate
- **R35**: Steps to determine the key management certificate:
  1. If SMIMEEncryptionKeyPreference found in signedData from recipient, use that certificate.
  2. Else, search certificates for one with same subject name as signing cert that can be used for key management.
  3. Otherwise, use other method; if none found, encryption not possible. If multiple, arbitrary choice.

### 2.6 SignerIdentifier SignerInfo Type
- **R36**: S/MIME v3 requires SignerInfo version 1; issuerAndSerialNumber MUST be used.

### 2.7 ContentEncryptionAlgorithmIdentifier
- **R37**: Sending and receiving agents MUST support tripleDES (DES EDE3 CBC).
- **R38**: Receiving agents SHOULD support RC2/40 (RC2 with 40-bit key).

#### 2.7.1 Deciding Which Encryption Method To Use
- **R39**: When deciding encryption, use recipient’s capabilities list from signed messages.
- **R40**: On receiving a signed message with capabilities, if no list exists, create one with signing time and symmetric capabilities. If list exists, update if signing time > stored time and signature valid.
- **R41**: Signing time far in future (beyond reasonable clock skew) or capabilities from messages with invalid signature MUST NOT be accepted.
- **R42**: Sending agent MUST decide whether weak encryption is acceptable for data. If unacceptable, MUST NOT use weak algorithm (e.g., RC2/40).

##### 2.7.1.1 Rule 1: Known Capabilities
- **R43**: If capabilities received from recipient, sending agent SHOULD use the first capability in the list that the agent knows how to encrypt (if recipient can decrypt).

##### 2.7.1.2 Rule 2: Unknown Capabilities, Known Use of Encryption
- **R44**: If no knowledge of capabilities, but at least one encrypted message received from recipient with trusted signature, then SHOULD use same algorithm as that last signed-and-encrypted message.

##### 2.7.1.3 Rule 3: Unknown Capabilities, Unknown Version of S/MIME
- **R45**: If no knowledge of capabilities or version, sending agent SHOULD use tripleDES. If not, SHOULD use RC2/40.

#### 2.7.2 Choosing Weak Encryption
- **R46**: Sending agent controlled by human SHOULD allow human to assess risks of RC2/40 and possibly choose stronger encryption.

#### 2.7.3 Multiple Recipients
- **R47**: If encryption capabilities of recipients do not overlap, sending agent must send multiple messages. Risk: sending same message with strong and weak encryption may allow attacker to decrypt strongly-encrypted version.

## 3. Creating S/MIME Messages
### 3.1 Preparing the MIME Entity for Signing or Enveloping
- **R48**: MIME entity must be prepared according to [MIME-SPEC] with additional restrictions for signing.
- **R49**: Steps: 1) prepare entity per local conventions; 2) convert leaf parts to canonical form; 3) apply appropriate transfer encoding.

#### 3.1.1 Canonicalization
- **R50**: Each MIME entity MUST be converted to a canonical form uniquely representable for signature creation and verification. MIME entities MUST be canonicalized for enveloping as well as signing.
- **R51**: For text types, line endings must be <CR><LF>; charset should be registered. The chosen charset SHOULD be named in the charset parameter.
- **R52**: For charsets with multiple representations (e.g., ISO-2022), the canonical representation MUST be used.

#### 3.1.2 Transfer Encoding
- **R53**: For secured MIME entities except multipart/signed, no transfer encoding is required. S/MIME implementations MUST deal with binary MIME objects.
- **R54**: S/MIME implementations SHOULD use transfer encoding (section 3.1.3) for all secured MIME entities to ensure handling in any environment.

#### 3.1.3 Transfer Encoding for Signing Using multipart/signed
- **R55**: If a multipart/signed entity will be transmitted over 7-bit constrained transport, it MUST have transfer encoding applied (quoted-printable or base64) to be 7-bit data.
- **R56**: Reason: Internet mail infrastructure may not guarantee 8-bit transport; 8-bit data in first part of multipart/signed could cause undeliverability.

#### 3.1.4 Sample Canonical MIME Entity
- Example of multipart/mixed with quoted-printable text and base64 image, showing CRLF line endings and encoding of whitespace and "From ".

### 3.2 The application/pkcs7-mime Type
- Carries CMS objects (envelopedData, signedData).
- **R57**: Transfer encoding of the CMS object depends on transport; base64 is typical for SMTP.
- **R58**: Sending agent SHOULD include optional "smime-type" parameter to help receiving agent identify content without decoding ASN.1.

#### 3.2.1 The name and filename Parameters
- **R59**: Sending agents SHOULD emit optional "name" parameter in Content-Type and optional Content-Disposition "filename" parameter.
- **R60**: File extensions: .p7m for signedData/envelopedData, .p7c for degenerate signedData (certs-only), .p7s for application/pkcs7-signature.
- **R61**: Filename SHOULD be limited to 8 characters plus 3-letter extension; base "smime" SHOULD be used to indicate S/MIME.
- **R62**: Proper S/MIME implementation MUST use MIME types, not rely on file extensions.

#### 3.2.2 The smime-type parameter
- Defined smime-types: enveloped-data, signed-data, certs-only.
- **R63**: Guidelines for new smime-type: if both signing and encryption can be applied, assign "signed-*" and "encrypted-*". Use common string for content OID; if none, use "OID.<oid>".

### 3.3 Creating an Enveloped-only Message
- Steps: prepare MIME entity per 3.1; process into CMS envelopedData; insert into application/pkcs7-mime with smime-type=enveloped-data.
- **R64**: Sending agent SHOULD encrypt a copy of the content-encryption key for the originator and include in envelopedData.

### 3.4 Creating a Signed-only Message
- Two formats: application/pkcs7-mime with SignedData, and multipart/signed.
- **R65**: Receiving agents SHOULD be able to handle both.

#### 3.4.1 Choosing a Format for Signed-only Messages
- multipart/signed: viewable by recipients without S/MIME; signedData: requires S/MIME facilities but verifiable if unchanged.

#### 3.4.2 Signing Using application/pkcs7-mime with SignedData
- Steps: prepare MIME entity; process into CMS signedData; insert into application/pkcs7-mime with smime-type=signed-data.

#### 3.4.3 Signing Using the multipart/signed Format
- Uses multipart/signed with two parts: first = MIME entity to sign, second = detached signature (CMS signedData with absent eContent).
- **R66**: protocol parameter MUST be "application/pkcs7-signature" (quoted).
- **R67**: micalg parameter value depends on digest algorithm: md5 → "md5", sha-1 → "sha1", else "unknown". Receiving agents SHOULD recover gracefully from unrecognized micalg.
- **R68**: If multiple digest algorithms used, they MUST be separated by commas per [MIME-SECURE].

### 3.5 Signing and Encrypting
- **R69**: S/MIME implementation MUST be able to receive and process arbitrarily nested S/MIME within reasonable resource limits.
- Choice of order: sign then encrypt (signers obscured) or encrypt then sign (signatures verifiable without decryption). Security ramifications noted.

### 3.6 Creating a Certificates-only Message
- Steps: create CMS signedData with absent eContent and empty signerInfos; enclose in application/pkcs7-mime (smime-type=certs-only, extension .p7c).

### 3.7 Registration Requests
- S/MIME v3 does not specify certificate request method; mandates that sending agents already have a certificate. Standardization pursued in IETF PKIX.

### 3.8 Identifying an S/MIME Message
- Criteria:
  - MIME type: application/pkcs7-mime (any parameters/suffix)
  - MIME type: multipart/signed with protocol="application/pkcs7-signature"
  - MIME type: application/octet-stream with file suffix p7m, p7s, p7c

## 4. Certificate Processing
- **R70**: Receiving agent MUST provide certificate retrieval mechanism.
- Handling after validation/rejection covered in [CERT3].
- **R71**: Receiving and sending agents SHOULD provide mechanism to store and protect certificates for correspondents.

### 4.1 Key Pair Generation
- **R72**: If agent needs to generate key pair, it MUST be capable of generating separate DH and DSS key pairs. Each key pair MUST be generated from good non-deterministic random input and private key MUST be protected securely.
- **R73**: If agent needs to generate RSA key pair, it SHOULD do so.
- **R74**: User agent SHOULD generate RSA key pairs at minimum key size 768 bits.
- **R75**: User agent MUST NOT generate RSA key pairs less than 512 bits.
- **R76**: Receiving agent SHOULD be able to verify signatures with keys of any size over 512 bits.

## 5. Security
- 40-bit encryption is weak; using weak cryptography offers little security. S/MIME provides tripleDES and capability announcement.
- Sending same message with different encryption strengths can expose weak version.
- Modification of ciphertext can go undetected if authentication not used (EnvelopedData without SignedData).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Support SHA-1 | MUST | 2.1 |
| R2 | Support MD5 for backward compatibility | SHOULD | 2.1 |
| R3 | Support id-dsa (DSS) with absent parameters | MUST | 2.2 |
| R4 | Support rsaEncryption for signatures | SHOULD | 2.2 |
| R5 | Support rsaEncryption for signatures (sending) | SHOULD | 2.2 |
| R6 | Support Diffie-Hellman | MUST | 2.3 |
| R7 | Support rsaEncryption for key decryption | SHOULD | 2.3 |
| R8 | Support rsaEncryption for key encryption (sending) | SHOULD | 2.3 |
| R9 | Use id-data for content type in CMS | MUST | 2.4.1 |
| R10 | Use signedData for digital signatures | MUST | 2.4.2 |
| R11 | Handle zero or one instance of listed signed attributes | MUST | 2.5 |
| R12 | Generate one instance of signingTime, sMIMECapabilities, sMIMEEncryptionKeyPreference | SHOULD | 2.5 |
| R13 | Handle zero or one instance of signingCertificate | SHOULD | 2.5 |
| R14 | Generate one instance of signingCertificate | SHOULD | 2.5 |
| R15 | Handle unrecognized attributes gracefully | SHOULD | 2.5 |
| R16 | Display non-listed signed attributes to user | SHOULD | 2.5 |
| R17 | Encode signing time: UTCTime for ≤2049, GeneralizedTime for ≥2050 | MUST | 2.5.1 |
| R18 | Interpret UTCTime YY per rule | MUST | 2.5.1 |
| R19 | SMIMECapabilities MUST be SignedAttribute | MUST | 2.5.2 |
| R20 | No multiple SMIMECapabilities in signerInfo | MUST | 2.5.2 |
| R21 | Only one AttributeValue in SMIMECapabilities | MUST | 2.5.2 |
| R22 | Order OIDs by preference within categories | SHOULD | 2.5.2 |
| R23 | DER-encoding identical across implementations | MUST | 2.5.2 |
| R24 | Specify all differentiating parameters for symmetric algorithms | MUST | 2.5.2 |
| R25 | Use same OID as algorithm unless ambiguous; allocate new OID if needed | SHOULD/MUST | 2.5.2 |
| R26 | Omit parameters if not needed; do not encode as NULL | MUST | 2.5.2 |
| R27 | Handle unrecognized SMIMECapabilities gracefully | MUST | 2.5.2 |
| R28 | SMIMEEncryptionKeyPreference MUST be SignedAttribute | MUST | 2.5.3 |
| R29 | No multiple instances in signerInfo | MUST | 2.5.3 |
| R30 | Only one AttributeValue | MUST | 2.5.3 |
| R31 | Include referenced certificate in message | SHOULD | 2.5.3 |
| R32 | Use attribute if preferred encryption cert differs from signing cert | SHOULD | 2.5.3 |
| R33 | Store preference data if valid signature and newer signing time | SHOULD | 2.5.3 |
| R34 | Respect sender's encryption key preference if possible | SHOULD | 2.5.3 |
| R35 | Follow steps to select key management certificate | SHOULD | 2.5.3.1 |
| R36 | Use issuerAndSerialNumber for SignerIdentifier | MUST | 2.6 |
| R37 | Support tripleDES | MUST | 2.7 |
| R38 | Support RC2/40 | SHOULD | 2.7 |
| R39 | Use recipient capabilities list to decide encryption | SHOULD | 2.7.1 |
| R40 | Create/update capabilities list based on signed messages | SHOULD | 2.7.1 |
| R41 | Reject capabilities from messages with invalid signature or far future time | MUST | 2.7.1 |
| R42 | Do not use weak encryption if unacceptable for data | MUST | 2.7.1 |
| R43 | Use first matching capability from recipient's list | SHOULD | 2.7.1.1 |
| R44 | Use same algorithm as last signed/encrypted message from recipient | SHOULD | 2.7.1.2 |
| R45 | Use tripleDES when capabilities and version unknown; else RC2/40 | SHOULD | 2.7.1.3 |
| R46 | Allow human to assess weak encryption risks | SHOULD | 2.7.2 |
| R47 | Handle non-overlapping capabilities among multiple recipients | must send multiple messages | 2.7.3 |
| R48 | Prepare MIME entity per [MIME-SPEC] with signing restrictions | MUST | 3.1 |
| R49 | Apply canonicalization and transfer encoding steps | --- | 3.1 |
| R50 | Canonicalize MIME entity for signing and enveloping | MUST | 3.1.1 |
| R51 | Text types: CRLF line endings, registered charset in parameter | MUST/SHOULD | 3.1.1 |
| R52 | Use canonical representation for multi-representation charsets | MUST | 3.1.1 |
| R53 | Handle binary MIME objects | MUST | 3.1.2 |
| R54 | Use transfer encoding for all secured MIME entities | SHOULD | 3.1.2 |
| R55 | Apply 7-bit transfer encoding for multipart/signed if needed | MUST | 3.1.3 |
| R56 | Reason: avoid transport corruption | --- | 3.1.3 |
| R57 | Transfer encoding of CMS object depends on transport | --- | 3.2 |
| R58 | Include smime-type parameter | SHOULD | 3.2 |
| R59 | Emit name and filename parameters | SHOULD | 3.2.1 |
| R60 | Use specified file extensions | SHOULD | 3.2.1 |
| R61 | Limit filename to 8.3 and use "smime" base | SHOULD | 3.2.1 |
| R62 | Must use MIME types, not file extensions | MUST | 3.2.1 |
| R63 | Guidelines for new smime-type parameters | --- | 3.2.2 |
| R64 | Encrypt content-encryption key for originator | SHOULD | 3.3 |
| R65 | Handle both signed-only formats | SHOULD | 3.4 |
| R66 | protocol parameter MUST be "application/pkcs7-signature" | MUST | 3.4.3.2 |
| R67 | micalg parameter values as specified; recover gracefully from unknown | SHOULD | 3.4.3.2 |
| R68 | Separate multiple digest algorithms with commas | MUST | 3.4.3.2 |
| R69 | Process arbitrarily nested S/MIME within resource limits | MUST | 3.5 |
| R70 | Provide certificate retrieval mechanism | MUST | 4 |
| R71 | Provide mechanism to store and protect certificates | SHOULD | 4 |
| R72 | Generate DH and DSS key pairs from good random; protect private key | MUST | 4.1 |
| R73 | Generate RSA key pairs if needed | SHOULD | 4.1 |
| R74 | Generate RSA keys at least 768 bits | SHOULD | 4.1 |
| R75 | Do not generate RSA keys < 512 bits | MUST | 4.1 |
| R76 | Verify signatures with keys >512 bits | SHOULD | 4.1 |

## Informative Annexes (Condensed)
- **Annex A: ASN.1 Module**: Defines the `SecureMimeMessageV3` module, including OIDs for smimeCapabilities, SMIMECapability, SMIMEEncryptionKeyPreference, and encryption algorithms (DES-EDE3-CBC, RC2-CBC). Lists standard OIDs for digest, signature, and asymmetric algorithms (commented out for reference).
- **Annex B: References**: Lists all normative and informative references (RFC 2630–2634, 1847, 2045–2049, 2119, 2311–2315, etc.).
- **Annex C: Acknowledgements**: Thanks to S/MIME Working Group members, especially Dave Crocker, Bill Flanigan, Paul Hoffman, Russ Housley, John Pawling, Jim Schaad. Editor contact: Blake Ramsdell, Worldtalk.

*(Note: Full copyright statement and RFC editor funding acknowledgement are retained for legal completeness but not condensed.)*