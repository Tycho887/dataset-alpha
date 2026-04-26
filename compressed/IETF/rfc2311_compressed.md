# RFC 2311: S/MIME Version 2 Message Specification
**Source**: IETF Network Working Group (Informational) | **Version**: RFC 2311 | **Date**: March 1998 | **Type**: Informational  
**Original**: https://www.rfc-editor.org/rfc/rfc2311

## Scope (Summary)
S/MIME provides a consistent way to send and receive secure MIME data, offering authentication, message integrity, non-repudiation, privacy, and data security for electronic messaging applications. It uses PKCS #7 cryptographic objects and defines MIME types (`application/pkcs7-mime`, `application/pkcs7-signature`, `application/pkcs10`) to transport secure content. This document is not an IETF standard; it describes a protocol for adopters of S/MIME version 2.

## Normative References
- [PKCS-1] Kaliski, B., "PKCS #1: RSA Encryption Version 1.5", RFC 2313, March 1998.
- [PKCS-7] Kaliski, B., "PKCS #7: Cryptographic Message Syntax Version 1.5", RFC 2315, March 1998.
- [PKCS-10] Kaliski, B., "PKCS #10: Certification Request Syntax Version 1.5", RFC 2314, March 1998.
- [MIME-SPEC] RFC 2045, 2046, 2047, 2048, 2049 (November 1996).
- [MIME-SECURE] Galvin, J., et al., "Security Multiparts for MIME: Multipart/Signed and Multipart/Encrypted", RFC 1847, October 1995.
- [MUSTSHOULD] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [SHA1] NIST FIPS PUB 180-1, "Secure Hash Standard", 31 May 1994.
- [MD5] Rivest, R., "The MD5 Message Digest Algorithm", RFC 1321, April 1992.
- [RC2] Rivest, R., "Description of the RC2(r) Encryption Algorithm", RFC 2268, January 1998.
- [DES] ANSI X3.106, 1983.
- [3DES] Tuchman, W., "Hellman Presents No Shortcut Solutions To DES", IEEE Spectrum, July 1979.
- [CONTDISP] Troost, R., et al., "Communicating Presentation Information in Internet Messages: The Content-Disposition Header Field", RFC 2183, August 1997.

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One (CCITT X.208)
- **BER**: Basic Encoding Rules for ASN.1 (CCITT X.209)
- **DER**: Distinguished Encoding Rules for ASN.1 (CCITT X.509)
- **7-bit data**: Text with lines <998 characters, no 8th bit set, no NULL characters; <CR><LF> only.
- **8-bit data**: Text with lines <998 characters, no NULL characters; <CR><LF> only.
- **Binary data**: Arbitrary data.
- **Transfer Encoding**: Reversible transformation for sending 8-bit/binary data over 7-bit channels.

## 1. Introduction
S/MIME provides cryptographic security services (authentication, integrity, non-repudiation via digital signatures; privacy via encryption) for MIME-based messaging. It can be used with any transport that carries MIME data (e.g., SMTP, HTTP). This document defines protocols using PKCS #7, PKCS #10, and MIME types. The best strategy is "be liberal in what you receive and conservative in what you send."

### 1.2 Terminology
The key words MUST, MUST NOT, SHOULD, and SHOULD NOT in this document are to be interpreted as described in [MUSTSHOULD].

## 2. PKCS #7 Options
### 2.1 DigestAlgorithmIdentifier
- Receiving agents MUST support SHA-1 and MD5.
- Sending agents SHOULD use SHA-1.

### 2.2 DigestEncryptionAlgorithmIdentifier
- Receiving agents MUST support `rsaEncryption` [PKCS-1] and MUST support verification of signatures using RSA public key sizes from 512 bits to 1024 bits.
- Sending agents MUST support `rsaEncryption`; outgoing messages are signed with the user’s private key.

### 2.3 KeyEncryptionAlgorithmIdentifier
- Receiving agents MUST support `rsaEncryption` for decrypting symmetric keys.
- Sending agents MUST support `rsaEncryption` and MUST support encryption of symmetric keys with RSA public keys of sizes 512 to 1024 bits.

### 2.4 General Syntax
- Receiving agents MUST support the `data`, `signedData`, and `envelopedData` content types (PKCS #7).
- **2.4.1 Data Content Type**: Sending agents MUST use the `data` content type as the inner content for secured messages.
- **2.4.2 SignedData Content Type**: Sending agents MUST use `signedData` to apply a digital signature or (degenerate case) to convey certificates.
- **2.4.3 EnvelopedData Content Type**: Used for privacy protection; requires recipient’s public key; does not provide authentication.

### 2.5 Attribute SignerInfo Type
- Receiving agents MUST be able to handle zero or one instance of each signed attribute described in this section.
- Sending agents SHOULD be able to generate one instance of each signed attribute and SHOULD include them in each signed message.
- Receiving agents SHOULD gracefully handle unrecognized attributes or values.

#### 2.5.1 Signing-Time Attribute
- Sending agents MUST encode signing time through 2049 as UTCTime; for 2050 or later, MUST encode as GeneralizedTime.
- Agents MUST interpret year field: if YY >= 50 ⇒ 19YY; if YY < 50 ⇒ 20YY.

#### 2.5.2 S/MIME Capabilities Attribute
- The attribute (SMIMECapabilities) includes signature, symmetric, and key encipherment algorithm OIDs, plus a preference for signedData.
- OIDs are listed in order of preference, logically separated by category.
- For symmetric algorithms, all differentiating parameters MUST be specified.
- When no differentiating parameters exist, parameters MUST be omitted (not encoded as NULL).
- Receiving agents MUST gracefully handle unrecognized SMIMECapability values.
- The registered SMIMECapability list is maintained by the Internet Mail Consortium.

### 2.6 ContentEncryptionAlgorithmIdentifier
- Receiving agents MUST support decryption using RC2/40 (40-bit key).
- Receiving agents SHOULD support decryption using tripleDES (DES EDE3 CBC) [3DES][DES].
- Sending agents SHOULD support encryption with RC2/40 and tripleDES.

#### 2.6.1 Deciding Which Encryption Method To Use
- If the sending agent decides weak encryption is unacceptable, it MUST NOT use weak algorithms (e.g., RC2/40).
- The following rules are ordered; sending agent SHOULD decide in the given order:

##### 2.6.2.1 Rule 1: Known Capabilities
If the sending agent has a capabilities list from the recipient, it SHOULD select the first capability it can use.

##### 2.6.2.2 Rule 2: Unknown Capabilities, Known Use of Encryption
If the sending agent has no capabilities list but has received a signed and encrypted message from the recipient with a trusted signature, it SHOULD use the same encryption algorithm as that last message.

##### 2.6.2.3 Rule 3: Unknown Capabilities, Risk of Failed Decryption
If the sending agent has no capabilities and is willing to risk failed decryption, it SHOULD use tripleDES.

##### 2.6.2.4 Rule 4: Unknown Capabilities, No Risk of Failed Decryption
If the sending agent has no capabilities and is not willing to risk failed decryption, it MUST use RC2/40.

#### 2.6.3 Choosing Weak Encryption
- A sending agent controlled by a human SHOULD allow the human to determine the risks of using RC2/40 and possibly choose a stronger method.

#### 2.6.4 Multiple Recipients
- If recipients have non-overlapping encryption capabilities, the sending agent may need to send multiple messages. Sending the same message with both strong and weak encryption compromises the strong encryption.

## 3. Creating S/MIME Messages
### 3.1 Preparing the MIME Entity for Signing or Enveloping
- The MIME entity to be secured is the "inside" object; it must be prepared according to [MIME-SPEC] with additional restrictions.
- Steps: (1) Prepare according to local conventions, (2) convert leaf parts to canonical form, (3) apply appropriate transfer encoding.

#### 3.1.1 Canonicalization
- Each MIME entity MUST be converted to a canonical form unambiguous in both signing and verifying environments.
- For text: line endings MUST be <CR><LF>; charset SHOULD be a registered charset; canonical representation for the charset MUST be used.

#### 3.1.2 Transfer Encoding
- S/MIME implementations MUST handle binary MIME objects. If no Content-Transfer-Encoding header, consider 7BIT.
- Implementations SHOULD use transfer encoding (section 3.1.3) even for enveloped data to allow handling in any environment.

#### 3.1.3 Transfer Encoding for Signing Using multipart/signed
- If a multipart/signed entity is to be transmitted over 7-bit transport, it MUST have transfer encoding applied so it is 7-bit text (e.g., quoted-printable or base64).

### 3.2 The application/pkcs7-mime Type
- Always carries a single PKCS #7 object, BER-encoded; `contentInfo` field must contain a MIME entity (never empty).
- Sending agents SHOULD include the optional `smime-type` parameter.

#### 3.2.1 The name and filename Parameters
- Sending agents SHOULD emit the optional `name` parameter and `Content-Disposition` with `filename` parameter.
- Recommended file extensions: `.p7m` (signedData, envelopedData), `.p7c` (certs-only), `.p7s` (signature), `.p10` (certification request). Filename base SHOULD be "smime".
- Proper S/MIME implementations MUST use MIME types, not rely on file extensions.

### 3.3 Creating an Enveloped-only Message
- Steps: prepare MIME entity per 3.1 → process into PKCS #7 envelopedData → wrap in application/pkcs7-mime with `smime-type=enveloped-data` and extension `.p7m`.

### 3.4 Creating a Signed-only Message
- Two formats: `application/pkcs7-mime` (signedData) and `multipart/signed`. Receiving agents SHOULD handle both.

#### 3.4.1 Choosing a Format for Signed-only Messages
- Multipart/signed allows viewing without S/MIME facilities; signedData format requires S/MIME for viewing.

#### 3.4.2 Signing Using application/pkcs7-mime and SignedData
- Steps: prepare MIME entity → process into PKCS #7 signedData → wrap in application/pkcs7-mime with `smime-type=signed-data`, extension `.p7m`.

#### 3.4.3 Signing Using the multipart/signed Format
- Clear-signing format; uses `multipart/signed` with two parts: first part = MIME entity to be signed; second part = detached signature (PKCS #7 signedData with empty `contentInfo`).

##### 3.4.3.1 The application/pkcs7-signature MIME Type
- Contains a single PKCS #7 signedData object; `contentInfo` must be empty. Extension `.p7s`.

##### 3.4.3.2 Creating a multipart/signed Message
- Steps: prepare MIME entity → obtain detached signature → insert entity as first part → encapsulate signature in application/pkcs7-signature as second part.
- Required parameters: `protocol="application/pkcs7-signature"` (quotes required), `micalg` (value based on digest algorithm: md5, sha1, or unknown).
- Receiving agents SHOULD gracefully recover from unrecognized `micalg` values.

### 3.5 Signing and Encrypting
- An S/MIME implementation MUST be able to receive and process arbitrarily nested S/MIME within reasonable resource limits.
- Signing first obscures signatories; enveloping first exposes signatories but allows verification without private key.

### 3.6 Creating a Certificates-only Message
- Steps: create PKCS #7 signedData with empty `contentInfo` and empty `signerInfos` → wrap in application/pkcs7-mime with `smime-type=certs-only`, extension `.p7c`.

### 3.7 Creating a Registration Request
#### 3.7.1 Format of the application/pkcs10 Body
- The body MUST be a PKCS #10 `CertificationRequest`, BER-encoded. Robust applications SHOULD output DER but accept BER or DER. Base64 encoding SHOULD be used.

#### 3.7.2 Sending and Receiving an application/pkcs10 Body Part
- The `application/pkcs10` MIME type MUST be used for certification requests. For conveying certificates/CRLs, use `application/pkcs7-mime` with degenerate signedData.

### 3.8 Identifying an S/MIME Message
- A message is S/MIME if it matches any of:
  - MIME type `application/pkcs7-mime` (any parameters, any file suffix)
  - `application/pkcs10` (any)
  - `multipart/signed` with `protocol="application/pkcs7-signature"`
  - `application/octet-stream` with file suffix p7m, p7s, aps, p7c, or p10.

## 4. Certificate Processing
- Receiving agent MUST provide certificate retrieval mechanism. This memo covers only post-validation handling.
- Agents SHOULD provide mechanism to store and protect certificates.

### 4.1 Key Pair Generation
- An S/MIME agent MUST be capable of generating RSA key pairs from good non-deterministic random input, protected securely.
- SHOULD generate RSA key pairs at minimum 768 bits, maximum 1024 bits. MUST NOT generate keys less than 512 bits.

## 5. Security Considerations
- 40-bit encryption (RC2/40) offers little actual security; using tripleDES is recommended when feasible.
- Senders should not send copies of a message with weaker cryptography than the original, as an observer can decrypt the weaker version.

---

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Receiving agents MUST support SHA-1 and MD5 for digest algorithms. | shall | §2.1 |
| R2 | Sending agents SHOULD use SHA-1. | should | §2.1 |
| R3 | Receiving agents MUST support rsaEncryption and signature verification with RSA key sizes 512–1024 bits. | shall | §2.2 |
| R4 | Sending agents MUST support rsaEncryption. | shall | §2.2 |
| R5 | Receiving agents MUST support rsaEncryption for key decryption. | shall | §2.3 |
| R6 | Sending agents MUST support rsaEncryption for key encryption with RSA key sizes 512–1024 bits. | shall | §2.3 |
| R7 | Receiving agents MUST support PKCS #7 content types: data, signedData, envelopedData. | shall | §2.4 |
| R8 | Sending agents MUST use data content type as inner content. | shall | §2.4.1 |
| R9 | Sending agents MUST use signedData for digital signatures. | shall | §2.4.2 |
| R10 | Receiving agents MUST handle zero or one instance of each signed attribute. | shall | §2.5 |
| R11 | Sending agents SHOULD generate one instance of each signed attribute and include them. | should | §2.5 |
| R12 | Sending agents MUST encode signing time: through 2049 as UTCTime; 2050+ as GeneralizedTime. | shall | §2.5.1 |
| R13 | Receiving agents MUST support decryption with RC2/40. | shall | §2.6 |
| R14 | Receiving agents SHOULD support decryption with tripleDES. | should | §2.6 |
| R15 | Sending agents SHOULD support encryption with RC2/40 and tripleDES. | should | §2.6 |
| R16 | If sending agent decides weak encryption is unacceptable, MUST NOT use weak algorithm. | shall | §2.6.1 |
| R17 | Sending agent SHOULD follow ordered rules (1–4) for encryption algorithm choice. | should | §2.6.2 |
| R18 | Sending agent MUST use RC2/40 if no capabilities and no risk of failed decryption (Rule 4). | shall | §2.6.2.4 |
| R19 | MIME entities MUST be canonicalized for signing and enveloping. | shall | §3.1.1 |
| R20 | For multipart/signed over 7-bit transport, MIME entity MUST be transfer-encoded to 7-bit. | shall | §3.1.3 |
| R21 | S/MIME implementations MUST handle binary MIME objects. | shall | §3.1.2 |
| R22 | Sending agents SHOULD include smime-type parameter on application/pkcs7-mime. | should | §3.2 |
| R23 | Sending agents SHOULD emit name/filename parameters with appropriate extensions. | should | §3.2.1 |
| R24 | Receiving agents SHOULD handle both signed message formats (application/pkcs7-mime and multipart/signed). | should | §3.4 |
| R25 | Protocol parameter for multipart/signed MUST be "application/pkcs7-signature". | shall | §3.4.3.2 |
| R26 | S/MIME implementation MUST be able to receive and process arbitrarily nested S/MIME within resource limits. | shall | §3.5 |
| R27 | For certs-only messages, use degenerate signedData with empty contentInfo and signerInfos. | must | §3.6 |
| R28 | Application/pkcs10 body MUST be a PKCS #10 CertificationRequest, BER-encoded. | shall | §3.7.1 |
| R29 | For certification requests, MUST use application/pkcs10. For certificates/CRLs, MUST use application/pkcs7-mime. | shall | §3.7.2 |
| R30 | S/MIME agent MUST be capable of generating RSA key pairs from good random input. | shall | §4.1 |
| R31 | MUST NOT generate RSA keys less than 512 bits. | shall | §4.1 |
| R32 | SHOULD generate keys of 768 to 1024 bits. | should | §4.1 |

---

## Informative Annexes (Condensed)

### Annex A: Object Identifiers and Syntax
Lists ASN.1 definitions for SMIMECapability, content encryption algorithms (RC2-CBC, DES-EDE3-CBC), digest algorithms (md5, sha-1), asymmetric encryption (rsaEncryption, rsa), signature algorithms (md2WithRSAEncryption, md5WithRSAEncryption, sha-1WithRSAEncryption), and signed attributes (signingTime, smimeCapabilities). Parameters must be encoded as specified.

### Annex B: References
Full bibliographic references for all normative and informative documents.

### Annex C: Compatibility with Prior Practice
- Receiving agents SHOULD attempt to interoperate with earlier S/MIME implementations that used `x-` prefixed MIME types (`application/x-pkcs7-mime`, etc.).
- Two historical encryption profiles: "restricted" (mandatory RC2/40) and "unrestricted" (mandatory RC2/40 plus tripleDES). Restricted profile was driven by US export regulations; agents may need to support both for interoperability.

### Annex D: Request for New MIME Subtypes
Registrations for `application/pkcs7-mime`, `application/pkcs7-signature`, and `application/pkcs10` with required/optional parameters, encoding considerations, and file extensions.

### Annex E: Encapsulating Signed Messages for Internet Transport
Explains why multiple signing formats exist: multipart/signed may be damaged by non-MIME gateways; application/pkcs7-mime can be treated as opaque attachment. A proposal for `application/mime` encapsulation exists but is not implemented. For non-MIME environments, multipart/signed entities should be given a `.aps` extension.

### Annex F: Acknowledgements
Contributions from Jim Schaad, Jeff Thompson, Jeff Weinstein.

### Annex G: Authors' Addresses
Contact information for Steve Dusse, Paul Hoffman, Blake Ramsdell, Laurence Lundblade, Lisa Repka.

### Annex H: Full Copyright Statement
Copyright © The Internet Society (1998). All Rights Reserved. Standard IETF copyright and disclaimer.