# RFC 8152: CBOR Object Signing and Encryption (COSE)
**Source**: IETF | **Version**: Standards Track | **Date**: July 2017 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc8152

## Scope (Summary)
This document defines the CBOR Object Signing and Encryption (COSE) protocol for creating and processing signatures, message authentication codes (MACs), and encryption using CBOR serialization. It also specifies how to represent cryptographic keys using CBOR, targeting constrained IoT devices with small code and message sizes.

## Normative References
- [AES-GCM] NIST SP 800-38D
- [COAP.Formats] IANA CoRE Parameters
- [DSS] FIPS PUB 186-4
- [MAC] FIPS PUB 113
- [RFC2104] HMAC: Keyed-Hashing for Message Authentication
- [RFC2119] Key words for use in RFCs
- [RFC3394] AES Key Wrap Algorithm
- [RFC3610] Counter with CBC-MAC (CCM)
- [RFC5869] HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
- [RFC6090] Fundamental Elliptic Curve Cryptography Algorithms
- [RFC6979] Deterministic Usage of DSA and ECDSA
- [RFC7049] Concise Binary Object Representation (CBOR)
- [RFC7539] ChaCha20 and Poly1305
- [RFC7748] Elliptic Curves for Security
- [RFC8032] Edwards-Curve Digital Signature Algorithm (EdDSA)
- [RFC8174] Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [SEC1] Standards for Efficient Cryptography, Version 2.0

## Definitions and Abbreviations
- **Byte**: synonym for octet.
- **CoAP**: Constrained Application Protocol [RFC7252].
- **AE**: Authenticated Encryption algorithms that provide authentication check with encryption.
- **AEAD**: Authenticated Encryption with Authenticated Data, provides authentication of non-encrypted data.
- **label**: map key in COSE (int or tstr).
- **values**: any CBOR value.

## 1. Introduction (Condensed)
COSE provides security services (signing, MAC, encryption) for CBOR-encoded messages. It re-examines decisions from JOSE [RFC7515][RFC7516][RFC7517][RFC7518] and adapts to CBOR's binary capabilities. Design changes include: single top message structure, binary encodings, combined authentication tag with ciphertext, and expanded/trimmed algorithm set.

### 1.2 Requirements Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in BCP 14 [RFC2119][RFC8174] only when they appear in all capitals.

## 2. Basic COSE Structure
- All COSE messages are CBOR arrays. First three elements: protected header (bstr), unprotected header (map), content (bstr or nil). Additional elements depend on message type.
- Messages identified by CBOR tag, context, media type parameter `cose-type`, or CoAP Content-Format.
- Two layers: content layer and recipient/signature layer.
- **Tagged messages** use CBOR tags from Table 1.
- **Untagged messages** omit the tag.
- The CDDL non-terminal `COSE_Messages = COSE_Untagged_Message / COSE_Tagged_Message`.

## 3. Header Parameters
- Two buckets: **protected** (cryptographically protected, encoded as bstr) and **unprotected** (not protected).
- Protected bucket MUST be empty if not included in cryptographic computation. Senders SHOULD encode zero-length map as zero-length bstr. Recipients MUST accept both zero-length bstr and zero-length map.
- Labels in each map MUST be unique. Duplicate labels -> message MUST be rejected as malformed. Applications SHOULD verify no duplicate across both buckets; attributes obtained from protected before unprotected.

### 3.1 Common COSE Header Parameters
- **alg (1)**: int/tstr, algorithm identifier from COSE Algorithms registry. MUST be authenticated if possible.
- **crit (2)**: array of labels that must be understood. MUST be in protected bucket. MUST have at least one value.
- **content type (3)**: tstr or uint from CoAP Content-Formats or Media Types.
- **kid (4)**: bstr, key identifier.
- **IV (5)**: bstr, Initialization Vector.
- **Partial IV (6)**: bstr, part of IV for per-message change. MUST NOT coexist with full IV in same layer.
- **counter signature (7)**: COSE_Signature or array of COSE_Signatures.
- **Required processing**: If `crit` includes a label not in protected bucket, fatal error.

## 4. Signing Objects
- **COSE_Sign**: multiple signers. Structure: [Headers, payload (bstr/nil), signatures: [+COSE_Signature]].
- **COSE_Sign1**: single signer. Structure: [Headers, payload (bstr/nil), signature (bstr)].
- Tagged: COSE_Sign (tag 98), COSE_Sign1 (tag 16? Actually tag 18 for Sign1? Table 1 shows tag 18 for Sign1, tag 98 for Sign).
- Payload can be detached (nil). If all bytes consumed by recovery, payload is zero-length bstr.

### 4.3 Externally Supplied Data
Applications may supply additional authenticated data not in COSE object. Construction must ensure deterministic byte string: use fixed-width or TLV encoding, defined ordering, and guarantee same byte stream at both ends.

### 4.4 Signing and Verification Process
- **Sig_structure**: CBOR array [context ("Signature"/"Signature1"/"CounterSignature"), body_protected (bstr), ?sign_protected (bstr), external_aad (bstr), payload (bstr)].
- Signature creation: encode Sig_structure to bytes using Canonical CBOR (Section 14), call signing algorithm.
- Verification: same steps, compare signature.

### 4.5 Computing Counter Signatures
- Counter signatures can be placed in unprotected attributes of COSE_Sign1, COSE_Signature, COSE_Encrypt, COSE_recipient, COSE_Encrypt0, COSE_Mac, COSE_Mac0.
- Sig_structure context = "CounterSignature". Only signature with appendix allowed (no message recovery).

## 5. Encryption Objects
- **COSE_Encrypt**: multiple recipients. Structure: [Headers, ciphertext (bstr/nil), recipients: [+COSE_recipient]].
- **COSE_Encrypt0**: single recipient (implicit key). Structure: [Headers, ciphertext (bstr/nil)].
- Tagged: COSE_Encrypt (tag 96), COSE_Encrypt0 (tag 16). (But Table 1 says tag 96 for Encrypt, tag 16 for Encrypt0.)

### 5.1 Enveloped COSE Structure
- **COSE_recipient**: [Headers, ciphertext (bstr/nil), ?recipients: [+COSE_recipient]].
- Encrypted key is symmetric key binary value.
- For AE algorithms (no AD): protected field MUST be empty, external AAD MUST be absent.
- For AEAD algorithms: use Enc_structure for AAD.

### 5.2 Single Recipient Encrypted (COSE_Encrypt0)
- Assumes key is known implicitly. If key needs identification, use enveloped structure.

### 5.3 How to Encrypt/Decrypt for AEAD Algorithms
- **Enc_structure**: CBOR array [context ("Encrypt"/"Encrypt0"/"Enc_Recipient"/"Mac_Recipient"/"Rec_Recipient"), protected (bstr), external_aad (bstr)].
- Encrypt: create Enc_structure, encode to bytes (AAD), determine key (from direct, KDF, or random), call AEAD, output ciphertext.
- Decrypt: same AAD, determine key, call decryption.

### 5.4 How to Encrypt/Decrypt for AE Algorithms (without AD)
- Protected field MUST be empty. No external AAD. Same key determination.

## 6. MAC Objects
- **COSE_Mac**: multiple recipients. Structure: [Headers, payload (bstr/nil), tag (bstr), recipients: [+COSE_recipient]].
- **COSE_Mac0**: single implicit recipient. Structure: [Headers, payload (bstr/nil), tag (bstr)].
- Tagged: COSE_Mac (tag 97), COSE_Mac0 (tag 17).
- MAC provides data authentication/integrity; weak origination possible with pre-shared secrets or static-static key agreement.

### 6.3 How to Compute and Verify a MAC
- **MAC_structure**: [context ("MAC"/"MAC0"), protected (bstr), external_aad (bstr), payload (bstr)].
- Compute: encode MAC_structure, call MAC algorithm, place tag. Encrypt and encode MAC key for each recipient.
- Verify: same steps, compare tag.

## 7. Key Objects
- **COSE_Key**: CBOR map. Required element: `kty` (1). Other common: `kid` (2), `alg` (3), `key_ops` (4), `Base IV` (5).
- **COSE_KeySet**: CBOR array of COSE_Key. MUST have at least one element. Each element processed independently; malformed keys ignored.
- `alg` in key restricts usage; if present, MUST match algorithm used, else key MUST NOT be used.
- `key_ops`: array of values from Table 4 (sign, verify, encrypt, decrypt, wrap key, unwrap key, derive key, derive bits, MAC create, MAC verify).

## 8. Signature Algorithms
- Two schemes: signature with appendix (e.g., ECDSA, EdDSA) and signature with message recovery (not defined in this document).
- Specified algorithms: ECDSA (ES256, ES384, ES512) and EdDSA (Ed25519, Ed448).

### 8.1 ECDSA
- Algorithms: ES256 (-7, SHA-256), ES384 (-35, SHA-384), ES512 (-36, SHA-512).
- Only works with curves P-256, P-384, P-521 using EC2 key type.
- Signature encoded as concatenation of R and S integers: `Signature = I2OSP(R, n) | I2OSP(S, n)`, n = ceil(key_length/8).
- Key checks: `kty` MUST be 'EC2'; if `alg` present, must match; if `key_ops` present, must include 'sign' for creation, 'verify' for verification.

### 8.2 Edwards-Curve Digital Signature Algorithms (EdDSA)
- Algorithm: EdDSA (-8). Only pure EdDSA used (no pre-hash).
- Key type MUST be 'OKP' (Octet Key Pair). Curve MUST be Ed25519 or Ed448.
- Key checks similar to ECDSA.

## 9. Message Authentication Code (MAC) Algorithms
- HMAC (SHA-256/384/512, truncated variants) and AES-CBC-MAC (128/256-bit keys, 64/128-bit tags).
- For HMAC, key size SHOULD equal hash function size for carried keys; for derived keys, MUST equal hash size.
- For AES-CBC-MAC, IV fixed to all zeros. Single key MUST only be used for messages of fixed and known length.

## 10. Content Encryption Algorithms
- Only AEAD algorithms allowed. Specified: AES-GCM (nonce 96 bits, tag 128 bits), AES-CCM (various L/M/k), ChaCha20/Poly1305.
- AES-GCM: key/nonce pair MUST be unique. Total encrypted data MUST NOT exceed 2^39 - 256 bits.
- AES-CCM: key/nonce pair MUST be unique; total block cipher uses MUST NOT exceed 2^61.

## 11. Key Derivation Functions (KDFs)
- HKDF (HMAC-based) with SHA-256, SHA-512, or AES-CBC-MAC as PRF. Context structure COSE_KDF_Context defined.
- Context includes AlgorithmID, PartyUInfo, PartyVInfo, SuppPubInfo (with keyDataLength and protected), optional SuppPrivInfo.
- For direct key agreement, salt or nonce MUST be present and unique.

## 12. Content Key Distribution Methods
- Direct encryption (direct key value or direct + KDF), key wrap (AES Key Wrap), key transport (not defined), direct key agreement (ECDH ephemeral-static or static-static), key agreement with key wrap.
- For direct (Section 12.1.1): key type MUST be 'Symmetric'; protected field MUST be zero-length.
- For direct + KDF: salt or PartyU nonce MUST be present.
- ECDH algorithms: ECDH-ES+HKDF-256, etc. Ephemeral key MUST be generated new each time.

## 13. Key Object Parameters
- Key types: OKP (1), EC2 (2), Symmetric (4).
- EC2 parameters: crv (-1), x (-2), y (-3), d (-4). For public: crv, x, y REQUIRED. For private: crv, d REQUIRED; x, y RECOMMENDED.
- OKP parameters: crv (-1), x (-2), d (-4). For public: crv, x REQUIRED. For private: crv, d REQUIRED; x RECOMMENDED.
- Symmetric key parameter: k (-1).

## 14. CBOR Encoder Restrictions
- For Sig_structure, Enc_structure, MAC_structure: Canonical CBOR MUST be used (definite lengths, minimum length encoding).
- Duplicate labels in a map MUST NOT be generated; applications MUST NOT parse/process duplicate labels.

## 15. Application Profiling Considerations
- Applications must determine message types, define new header parameters, specify external AAD encoding, select algorithms (consider diversity), and provide negotiation/discovery if multiple options.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Protected bucket MUST be empty if not included in cryptographic computation. | MUST | Section 3 |
| R2 | Labels in each map MUST be unique. Duplicate => malformed. | MUST | Section 3 |
| R3 | `crit` parameter MUST be in protected bucket. | MUST | Section 3.1 |
| R4 | For AE algorithms, protected field MUST be empty; external AAD MUST be absent. | MUST | Sections 5.3, 5.4 |
| R5 | Key/nonce pair MUST be unique for AES-GCM and AES-CCM. | MUST | Sections 10.1.1, 10.2.1 |
| R6 | For ECDSA, `kty` MUST be 'EC2'; key checks. | MUST | Section 8.1 |
| R7 | For EdDSA, `kty` MUST be 'OKP'; curve Ed25519/Ed448. | MUST | Section 8.2 |
| R8 | For direct key wrap, protected field MUST be zero-length. | MUST | Section 12.1.1 |
| R9 | `kty` element REQUIRED in COSE_Key. | MUST | Section 7 |
| R10 | Canonical CBOR MUST be used for Sig_structure, Enc_structure, MAC_structure. | MUST | Section 14 |

## Informative Annexes (Condensed)
- **Appendix A: Guidelines for External Data Authentication of Algorithms**: Discusses omitting algorithm identifier for smaller messages; requires application to define implicit algorithms, key association, and protection of via external AAD.
- **Appendix B: Two Layers of Recipient Information**: Illustrates three-layer encryption (content, key wrap, key agreement) with a decomposed ECDH-ES+A128KW example.
- **Appendix C: Examples**: Provides extensive CBOR diagnostic notation examples of signed, encrypted, MACed messages, counter signatures, key sets (public/private). All examples are available on GitHub for testing.