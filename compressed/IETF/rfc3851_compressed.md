# RFC 3851: Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.1 Message Specification
**Source**: IETF | **Version**: 3.1 | **Date**: July 2004 | **Type**: Standards Track
**Original**: https://datatracker.ietf.org/doc/rfc3851/

## Scope (Summary)
Defines S/MIME v3.1 for consistent secure MIME messaging, providing digital signatures (authentication, integrity, non-repudiation), encryption (confidentiality), and compression. This document obsoletes RFC 2633.

## Normative References
- [CERT31] RFC 3850 - S/MIME v3.1 Certificate Handling
- [CHARSETS] IANA Character Sets
- [CMS] RFC 3852 - Cryptographic Message Syntax (CMS)
- [CMSAES] RFC 3565 - Use of AES in CMS
- [CMSALG] RFC 3370 - CMS Algorithms
- [CMSCOMPR] RFC 3274 - Compressed Data Content Type for CMS
- [CONTDISP] RFC 2183 - Content-Disposition Header
- [ESS] RFC 2634 - Enhanced Security Services for S/MIME
- [FIPS180-2] NIST FIPS 180-2 (SHA)
- [MIME-SPEC] RFC 2045-2049 - MIME Parts 1-5
- [MIME-SECURE] RFC 1847 - Security Multiparts for MIME
- [MUSTSHOULD] RFC 2119 - Key words for requirements
- [X.208-88] CCITT X.208 (ASN.1)
- [X.209-88] CCITT X.209 (BER)
- [X.509-88] CCITT X.509 (DER)

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One (CCITT X.208)
- **BER**: Basic Encoding Rules (CCITT X.209)
- **Certificate**: Binds entity name to public key with digital signature
- **DER**: Distinguished Encoding Rules (CCITT X.509)
- **7-bit data**: Text lines <998 chars, only 7-bit ASCII, <CR><LF> endings, no NULL
- **8-bit data**: Text lines <998 chars, 8-bit, no NULL, <CR><LF> endings
- **Binary data**: Arbitrary data
- **Transfer Encoding**: Reversible transform for 7-bit transport
- **Receiving agent**: Software interpreting S/MIME/CMS objects
- **Sending agent**: Software creating S/MIME/CMS objects
- **S/MIME agent**: User software as receiving, sending, or both

## Compatibility with Prior Practice
- S/MIME v3.1 agents SHOULD interoperate with v2 (RFC 2311-2315) and v3 (RFC 2630-2634)

## Changes Since S/MIME v3
- RSA key wrap: MUST implement; Diffie-Hellman: SHOULD implement
- AES symmetric encryption: SHOULD implement
- RSA signature: MUST implement
- Cleared language on empty SignedData for certificates/CRLs
- Explicit binary encoding for MIME entities
- Header protection via message/rfc822
- CompressedData type with new MIME type (.p7z) and file extension

## 2. CMS Options
### 2.1 DigestAlgorithmIdentifier
- **Sending/Receiving agents**: MUST support SHA-1 [CMSALG]
- **Receiving agents**: SHOULD support MD5 [CMSALG] for backward compatibility with S/MIME v2

### 2.2 SignatureAlgorithmIdentifier
- **Receiving agents**: MUST support id-dsa-with-sha1 (parameters absent, not NULL) [CMSALG] and rsaEncryption
- **Sending agents**: MUST support either id-dsa-with-sha1 or rsaEncryption
- If using rsaEncryption, MUST support digest algorithms per section 2.1
- Note: v3 may use id-dsa; receiving SHOULD treat id-dsa as id-dsa-with-sha1; sending MUST use id-dsa-with-sha1

### 2.3 KeyEncryptionAlgorithmIdentifier
- **Sending/Receiving**: MUST support rsaEncryption [CMSALG]
- **Sending/Receiving**: SHOULD support Diffie-Hellman (ephemeral-static) [CMSALG]
- Note: v3 may only use Diffie-Hellman; v2 only rsaEncryption

### 2.4 General Syntax
- Only Data, SignedData, EnvelopedData, CompressedData used for S/MIME
#### 2.4.1 Data Content Type
- **Sending agents**: MUST use id-data OID for inner MIME content
- For SignedData: eContentType = id-data; eContent = MIME content (except multipart/signed where absent)
- For EnvelopedData: encryptedContentInfo contentType = id-data; encryptedContent = encrypted MIME

#### 2.4.2 SignedData Content Type
- **Sending agents**: MUST use to apply digital signature or convey certificates (degenerate case with no signature)

#### 2.4.3 EnvelopedData Content Type
- Used for data confidentiality; sender needs public key of each recipient

#### 2.4.4 CompressedData Content Type
- Used for data compression only; NO authentication/integrity/confidentiality

### 2.5 Attributes and the SignerInfo Type
- **Receiving agents**: MUST handle zero or one instance of each signed attribute listed
- **Sending agents**: SHOULD generate one instance of each:
  - signingTime (2.5.1)
  - sMIMECapabilities (2.5.2)
  - sMIMEEncryptionKeyPreference (2.5.3)
  - id-messageDigest [CMS §11.2]
  - id-contentType [CMS §11.1]
- **Receiving agents**: SHOULD handle zero or one instance of signingCertificate [ESS §5]
- **Sending agents**: SHOULD generate one instance of signingCertificate
- **Receiving agents**: SHOULD gracefully handle unknown attributes/values
- **Interactive sending agents**: SHOULD display unsigned attributes not listed

#### 2.5.1 Signing-Time Attribute
- **Sending agents**: MUST encode through 2049 as UTCTime; 2050+ as GeneralizedTime
- For UTCTime: YY >=50 => 19YY; YY <50 => 20YY

#### 2.5.2 SMIMECapabilities Attribute
- **If present**: MUST be SignedAttribute (NOT Unsigned)
- **SignerInfo**: MUST NOT contain multiple instances; AttributeValue: MUST contain exactly one instance
- Semantics: partial list of supported capabilities; OIDs listed by preference, grouped by type
- DER encoding must be identical for same algorithms; parameters MUST specify all differentiating parameters
- Ambiguous OIDs: new OID assigned under smimeCapabilities OID
- For OIDs with no differentiating parameters: parameters MUST be omitted (not NULL)
- **Receiving agents**: MUST gracefully handle unrecognized values

##### 2.5.2.1 SMIMECapability For RC2
- capabilityID = rc2-cbc [CMSALG]
- parameters = SMIMECapabilitiesParametersForRC2CBC (INTEGER effective key length, e.g., 128 for 128-bit key; NOT version value)

#### 2.5.3 Encryption Key Preference Attribute
- **If present**: MUST be SignedAttribute (NOT Unsigned)
- **Sending agents**: SHOULD include referenced certificate in message; MAY omit if previously available
- **Sending agents**: SHOULD use if encryption cert differs from signing cert
- **Receiving agents**: SHOULD store preference if signature valid and signing time > stored value (check clock skew)
- **Receiving agents**: SHOULD respect sender's preference if possible

##### 2.5.3.1 Selection of Recipient Key Management Certificate
- **Order to determine certificate**:
  1. Use SMIMEEncryptionKeyPreference from recipient's SignedData
  2. If not found, search for cert with same subject name as signing cert suitable for key management
  3. Otherwise use other method; if none found, encryption impossible; if multiple, arbitrary choice

### 2.6 SignerIdentifier SignerInfo Type
- **S/MIME v3.1 implementations**: MUST support both issuerAndSerialNumber and subjectKeyIdentifier
- Note: v2 cannot read subjectKeyIdentifier
- **Implementations**: MUST prepare for multiple certificates with same subjectKeyIdentifier; MUST try each during verification before error

### 2.7 ContentEncryptionAlgorithmIdentifier
- **Sending/Receiving**: MUST support tripleDES (DES EDE3 CBC) [CMSALG]
- **Receiving**: SHOULD support RC2/40 [CMSALG]
- **Sending/Receiving**: SHOULD support AES-128, AES-192, AES-256 [CMSAES]

#### 2.7.1 Deciding Which Encryption Method To Use
- Use capabilities from incoming signed messages; process as follows:
  - If no list for sender's public key: create list with signing time and symmetric capabilities
  - If list exists: update if incoming signing time > stored and signature valid; reject future timestamps or unverifiable signatures
- **Sending agent**: MUST decide if weak encryption acceptable; if not, MUST NOT use RC2/40
- Rules (ordered):
  1. **Known capabilities**: use first capability in recipient's list that sending agent can encrypt
  2. **Unknown capabilities/version**: use tripleDES; if not, use RC2/40

#### 2.7.2 Choosing Weak Encryption
- RC2/40 considered weak; human-controlled sender SHOULD allow human to assess risks and possibly use stronger algorithm

#### 2.7.3 Multiple Recipients
- If capabilities don't overlap, sending agent MUST send multiple messages; if sending both strong and weak encrypted copies, attacker may decrypt weak to get strong content

## 3. Creating S/MIME Messages
- Combines MIME bodies and CMS content types; data is canonical MIME entity
- Three types: enveloped-only, signed-only (several formats), signed-and-enveloped

### 3.1 Preparing the MIME Entity
- **MIME entity** = sub-part or whole message (excluding RFC-822 headers)
- Header protection: sending client MAY wrap MIME message in message/rfc822
- Steps:
  1. Prepare MIME entity per local conventions
  2. Canonicalize leaf parts
  3. Apply transfer encoding
- **Receiving**: if top-level protected entity is message/rfc822, assume header protection; SHOULD present inner headers considering merging

#### 3.1.1 Canonicalization
- **MUST** canonicalize for signing, enveloping, compressing
- Text: line endings MUST be <CR><LF>; charset SHOULD be registered; charset parameter MUST be present
- For charsets with multiple representations (e.g., ISO-2022), MUST use canonical representation

#### 3.1.2 Transfer Encoding
- **No transfer encoding required** except multipart/signed; must handle binary MIME
- If no Content-Transfer-Encoding, assumed 7BIT
- **S/MIME implementations**: SHOULD use transfer encoding per 3.1.3 for all secured MIME entities
- If all recipients known capable of inner binary: SHOULD use binary encoding (no expansion)
- Otherwise SHOULD use transfer encoding

#### 3.1.3 Transfer Encoding for multipart/signed
- MUST be 7-bit; 8-bit/binary encoded with quoted-printable or base64
- Reason: SMTP cannot guarantee 8-bit transport; agents cannot modify first part of multipart/signed

#### 3.1.4 Sample Canonical MIME Entity
- (See original example; condensed here as informative) Example of multipart/mixed with text and image, showing canonical form.

### 3.2 The application/pkcs7-mime Type
- Carries CMS EnvelopedData, SignedData, CompressedData
- When eContentType = id-data, carried MIME entity prepared per §3.1
- Base-64 transfer encoding common for SMTP
- **Sending agents**: SHOULD include smime-type parameter
- **Sending agents**: SHOULD include "name" parameter and Content-Disposition with "filename" parameter
- File extensions: .p7m (SignedData/EnvelopedData), .p7c (degenerate SignedData certs), .p7z (CompressedData), .p7s (application/pkcs7-signature)
- Filename base SHOULD be "smime" (8.3 format)
- **Implementations**: MUST use MIME types, not file extensions

#### 3.2.2 The smime-type Parameter
- Values: enveloped-data, signed-data, certs-only, compressed-data
- Guidelines for new smime-type: if signing and encryption possible, assign "signed-*" and "encrypted-*"; use common string for content OID; if none, use "OID.<oid>"

### 3.3 Creating an Enveloped-only Message
1. Prepare MIME entity per §3.1
2. Process into CMS EnvelopedData; SHOULD encrypt content-encryption key for originator
3. Wrap in ContentInfo
4. Insert into application/pkcs7-mime with smime-type=enveloped-data, extension .p7m
- Sample provided (see original)

### 3.4 Creating a Signed-only Message
- Two formats: application/pkcs7-mime with SignedData, and multipart/signed
- **Receiving agents**: MUST handle both

#### 3.4.1 Choosing Format
- multipart/signed: viewable without S/MIME; susceptible to modification by benign agents
- application/pkcs7-mime: not viewable without S/MIME; protects content from modification

#### 3.4.2 Signing Using application/pkcs7-mime with SignedData
1. Prepare MIME entity per §3.1
2. Process into CMS SignedData
3. Wrap in ContentInfo
4. Insert into application/pkcs7-mime with smime-type=signed-data, extension .p7m
- Sample provided

#### 3.4.3 Signing Using multipart/signed
- Two parts: first = MIME entity to sign; second = detached signature (application/pkcs7-signature)

##### 3.4.3.1 The application/pkcs7-signature MIME Type
- Contains CMS SignedData with encapContentInfo eContent absent; signerInfos contains signatures
- Extension: .p7s

##### 3.4.3.2 Creating a multipart/signed Message
1. Prepare MIME entity per §3.1
2. Process to obtain SignedData with eContent absent
3. Insert MIME entity into first part (no further processing)
4. Transfer encode detached signature and insert into application/pkcs7-signature entity
5. Insert as second part of multipart/signed
- Parameters: protocol="application/pkcs7-signature"; micalg = algorithm values (md5, sha1, sha256, sha384, sha512, or "unknown")
- Historical values "rsa-md5" and "rsa-sha1"; receiving agents SHOULD gracefully handle unrecognized micalg

### 3.5 Creating a Compressed-only Message
1. Prepare MIME entity per §3.1
2. Process into CMS CompressedData
3. Wrap in ContentInfo
4. Insert into application/pkcs7-mime with smime-type=compressed-data, extension .p7z
- Sample provided

### 3.6 Multiple Operations
- Formats can be nested; **S/MIME implementation**: MUST be able to receive and process arbitrarily nested S/MIME within reasonable resource limits
- Signing and encrypting order: sign-first obscures signatory; encrypt-first allows signature verification without decryption
- Security: encrypt-then-sign allows validation only of encrypted block; sign-then-encrypt protects signed message but attacker could change unauthenticated parts
- Compression guidelines: avoid compressing binary encrypted data; if lossy compression used with signing, compress first then sign

### 3.7 Creating a Certificate Management Message
- For transporting certificates/CRLs
1. Create SignedData with signerInfos empty and eContent absent
2. Wrap in ContentInfo
3. Enclose in application/pkcs7-mime with smime-type=certs-only, extension .p7c

### 3.8 Registration Requests
- Not specified; S/MIME v3.1 does not require particular certificate request mechanism

### 3.9 Identifying S/MIME Messages
- Criteria:
  - MIME type application/pkcs7-mime (any param/extension)
  - MIME type multipart/signed with protocol="application/pkcs7-signature"
  - MIME type application/octet-stream with extensions p7m, p7s, p7c, p7z

## 4. Certificate Processing
- **Receiving agent**: MUST provide certificate retrieval mechanism
- At minimum: user agent could request certificate in signed return message
- **Receiving/Sending agents**: SHOULD provide mechanism to store and protect certificates

### 4.1 Key Pair Generation
- **All key pairs**: MUST be generated from good non-deterministic random input [RANDOM]; private keys MUST be protected securely
- RSA key pair guidelines:
  - SHOULD generate at minimum 768 bits
  - MUST NOT generate less than 512 bits
  - Longer than 1024 bits may cause compatibility issues but offers better security
  - **Receiving agent**: SHOULD verify signatures with keys >512 bits
  - Note: 512-bit keys considered cryptographically insecure
  - Multiple active key pairs may be associated with an individual

## 5. Security Considerations
- 40-bit encryption is weak; using weak cryptography offers little security
- Sending agents SHOULD inform senders/recipients of cryptographic strength
- Choosing key sizes is difficult; this specification provides framework
- **Sending agent**: SHOULD NOT send same message with weaker cryptography (attacker could decrypt weak version)
- Modification of ciphertext undetected without authentication (EnvelopedData without SignedData)
- See RFC 3218 [MMA] for thwarting adaptive chosen ciphertext attacks on PKCS#1 v1.5
- Diffie-Hellman in prime order subgroup vulnerable to small-subgroup attacks; prevent using methods in RFC 2785 [DHSUB]

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Sending and receiving agents MUST support SHA-1 digest | shall | §2.1 |
| R2 | Receiving agents MUST support id-dsa-with-sha1 signature | shall | §2.2 |
| R3 | Receiving agents MUST support rsaEncryption signature | shall | §2.2 |
| R4 | Sending agents MUST support id-dsa-with-sha1 or rsaEncryption | shall | §2.2 |
| R5 | Sending and receiving agents MUST support rsaEncryption key wrap | shall | §2.3 |
| R6 | Sending agents MUST use id-data for inner MIME content | shall | §2.4.1 |
| R7 | Sending agents MUST use SignedData for digital signatures (or certificates) | shall | §2.4.2 |
| R8 | Sending agents MUST encode signing time: UTCTime through 2049, GeneralizedTime 2050+ | shall | §2.5.1 |
| R9 | SMIMECapabilities if present MUST be SignedAttribute, single instance | shall | §2.5.2 |
| R10 | SMIMEEncryptionKeyPreference if present MUST be SignedAttribute, single instance | shall | §2.5.3 |
| R11 | S/MIME v3.1 implementations MUST support both issuerAndSerialNumber and subjectKeyIdentifier | shall | §2.6 |
| R12 | Sending and receiving agents MUST support tripleDES encryption | shall | §2.7 |
| R13 | Sending agent MUST not use weak encryption if unacceptable for data | shall | §2.7.1 |
| R14 | MIME entity MUST be canonicalized for signing, enveloping, compressing | shall | §3.1.1 |
| R15 | Text MIME entities MUST have <CR><LF> line endings | shall | §3.1.1 |
| R16 | S/MIME implementations MUST be able to deal with binary MIME objects | shall | §3.1.2 |
| R17 | If multipart/signed to be transmitted over 7-bit transport, MUST apply 7-bit transfer encoding | shall | §3.1.3 |
| R18 | Sending agent SHOULD include smime-type parameter for application/pkcs7-mime | should | §3.2 |
| R19 | Sending agent SHOULD emit "name" and Content-Disposition "filename" parameters | should | §3.2.1 |
| R20 | Receiving agents MUST handle both SignedData formats | shall | §3.4 |
| R21 | S/MIME implementation MUST be able to receive and process arbitrarily nested S/MIME | shall | §3.6 |
| R22 | All key pairs MUST be generated from good non-deterministic random input | shall | §4.1 |
| R23 | Private keys MUST be protected securely | shall | §4.1 |
| R24 | RSA keys MUST NOT be less than 512 bits | shall | §4.1 |
| R25 | Sending agents SHOULD support Diffie-Hellman key encryption | should | §2.3 |
| R26 | Receiving agents SHOULD support MD5 digest for v2 compatibility | should | §2.1 |
| R27 | Sending and receiving agents SHOULD support AES encryption | should | §2.7 |
| R28 | Receiving agents SHOULD handle zero or one instance of signingCertificate attribute | should | §2.5 |
| R29 | Sending agents SHOULD generate one instance of signingCertificate | should | §2.5 |
| R30 | Sending agents SHOULD generate signingTime, sMIMECapabilities, encryptionKeyPref attributes | should | §2.5 |
| R31 | Receiving agents SHOULD respect sender's encryption key preference | should | §2.5.3 |
| R32 | Sending agents SHOULD use 7-bit transfer encoding for all secured MIME entities | should | §3.1.2 |
| R33 | Sending agents SHOULD use file extensions (p7m, p7c, p7z, p7s) | should | §3.2.1 |
| R34 | Implementations SHOULD generate RSA keys at minimum 768 bits | should | §4.1 |
| R35 | S/MIME v3.1 agents SHOULD attempt interoperability with prior versions | should | §1.4 |
| R36 | Sending agents MAY wrap MIME message in message/rfc822 for header protection | may | §3.1 |
| R37 | Implementations MAY "know" recipient capability via attribute, agreement, or other means | may | §3.1.2 |
| R38 | S/MIME agents MAY use different key pairs for confidentiality and authentication | may | §4.1 |

## Informative Annexes (Condensed)
- **Annex A - ASN.1 Module**: Defines S/MIME v3.1 ASN.1 module with imports from CMS; includes SMIMECapabilities, SMIMEEncryptionKeyPreference, id-cap-preferBinaryInside, and RC2 parameters.
- **Annex C - Acknowledgements**: Thanks to contributors including Tony Capel, Piers Chivers, Dave Crocker, Bill Flanigan, Peter Gutmann, Paul Hoffman, Russ Housley, William Ottaway, John Pawling, Jim Schaad.
- **Copyright and Intellectual Property**: Standard IETF copyright notice and IPR disclaimer (condensed).