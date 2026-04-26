# RFC 3211: Password-based Encryption for CMS
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: December 2001 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3211

## Scope (Summary)
This document specifies a password-based content encryption mechanism for the Cryptographic Message Syntax (CMS), implemented as a new RecipientInfo type (PasswordRecipientInfo). It enables encryption using user-supplied passwords or any variable-length keying material.

## Normative References
- [ASN1] CCITT Recommendation X.208: Specification of Abstract Syntax Notation One (ASN.1), 1988.
- [RFC2119] Bradner, S., "Key Words for Use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2630] Housley, R., "Cryptographic Message Syntax", RFC 2630, June 1999.
- [RFC2898] Kaliski, B., "PKCS #5: Password-Based Cryptography Specification, Version 2.0", RFC 2898, September 2000.
- [PACKAGE] Rivest, R., "All-or-Nothing Encryption and the Package Transform", Proceedings of Fast Software Encryption '97, 1997.

## Definitions and Abbreviations
- **CEK**: Content-Encryption Key.
- **KEK**: Key-Encryption Key.
- **PBKDF2**: Password-Based Key Derivation Function 2 (as defined in [RFC2898]).
- **CMS**: Cryptographic Message Syntax.
- **PasswordRecipientInfo**: New RecipientInfo type for password-based key wrapping.

## Section 1: Introduction
### 1.1 Password-based Content Encryption
- CMS defines three existing RecipientInfo types; this RFC adds a fourth: **PasswordRecipientInfo** for password-based key wrapping.

### 1.2 RecipientInfo Types
- **RecipientInfo ::= CHOICE { ktri KeyTransRecipientInfo, kari [1] KeyAgreeRecipientInfo, kekri [2] KEKRecipientInfo, pwri [3] PasswordRecipientinfo }**.
- The process is described as password-based but is general-purpose; it can derive keys from any keying material.

#### 1.2.1 PasswordRecipientInfo Type
- **PasswordRecipientInfo ::= SEQUENCE { version CMSVersion, keyDerivationAlgorithm [0] KeyDerivationAlgorithmIdentifier OPTIONAL, keyEncryptionAlgorithm KeyEncryptionAlgorithmIdentifier, encryptedKey EncryptedKey }**.
  - **version**: MUST be 0.
  - **keyDerivationAlgorithm**: Identifies the algorithm to derive KEK from password; if absent, KEK is supplied externally.
  - **keyEncryptionAlgorithm**: Identifies the algorithm to encrypt CEK with KEK.
  - **encryptedKey**: The encrypted CEK.

#### 1.2.2 Rationale
- Two-stage process (password→KEK→CEK) is specified with separate algorithm identifiers to allow flexibility beyond PKCS#5v2.
- Multiple passwords for same data are not supported in this version due to lack of existing practice; may be addressed in future.

## Section 2: Supported Algorithms
### 2.1 Key Derivation Algorithms
- **Conforming implementations MUST include PBKDF2** [RFC2898].
- More precise definition in Appendix B.

### 2.2 Key Encryption Algorithms
- **id-alg-PWRI-KEK** OID: `{ iso(1) member-body(2) us(840) rsadsi(113549) pkcs(1) pkcs-9(9) smime(16) alg(3) 9 }`.
- The AlgorithmIdentifier parameters field for this algorithm contains the KEK encryption algorithm used with the key wrap algorithm (section 2.3).
- Conforming implementations **MUST implement id-alg-PWRI-KEK** key wrap.
- For KEK encryption algorithms: **MUST include Triple-DES in CBC mode**; **MAY include** AES, CAST-128, RC5, IDEA, Skipjack, Blowfish, etc. **SHOULD NOT include** any KSG ciphers (RC4, OFB) or ECB mode.

#### 2.2.1 Rationale
- Indirection in KeyEncryptionAlgorithmIdentifier allows future alternative wrapping algorithms without changing the PasswordRecipientInfo structure.
- The parameter field is explicit (no default) to avoid confusion over NULL vs absent parameters.

### 2.3.1 Key Wrap (Encryption)
- **Two phases**: formatting and wrapping.
- **Key formatting**: `CEK byte count (1 byte) || check value (bitwise complement of first 3 bytes of CEK) || CEK || padding (to multiple of KEK block length, at least two blocks)`.
- **Key wrapping**:
  1. Encrypt padded key using KEK.
  2. Without resetting IV, encrypt the encrypted padded key a second time.
- The result is the EncryptedKey.

### 2.3.2 Key Unwrap
- **Step 1**: Using n-1'th ciphertext block as IV, decrypt n'th block.
- **Step 2**: Using decrypted n'th block as IV, decrypt 1st...n-1'th blocks (strips outer encryption).
- **Step 3**: Decrypt inner layer with KEK.
- **Key format verification**:
  - If CEK byte count < min allowed (usually 5) or > wrapped length or invalid for algorithm → KEK invalid.
  - If bitwise complement of check value ≠ first three bytes of key → KEK invalid.

### 2.3.3 Example
- Given Skipjack CEK (10 bytes), Triple-DES KEK. Wrap and unwrap steps demonstrated.

### 2.3.4 Rationale for Double Wrapping
- Prevents collision attacks after ~2^32 encryptions with same KEK and 64-bit block size.
- Makes every ciphertext bit dependent on every CEK bit.
- No extra algorithms (hash) required; implementable in devices with only one cipher.

## Section 3: Test Vectors
(Summarized)
- Two test sets: basic (DES, 5 iterations PBKDF2) and stress-test (long passphrase, 500 iterations). Full known-answer and wrapping results provided in hex and ASN.1 encoded form. Refer to original text for exact values.

## Section 4: Security Considerations
- Security depends on underlying mechanisms (RFC 2630, PKCS5v2) and critically on password entropy.
- Pass phrases **STRONGLY RECOMMENDED**; even with pass phrases, deriving a KEK with sufficient entropy to protect a 128-bit CEK is difficult.

## Section 5: IANA Considerations
- OIDs assigned from RSA Security arc; additional algorithms to assign OIDs from own arcs. No IANA action required.

## Acknowledgments
- Jim Schaad, Phil Griffin, S/MIME Working Group.

## References
- As listed in Normative References section.

## Appendix A: ASN.1:1988 Module
- Provides 1988 ASN.1 definitions for PasswordRecipientInfo and PBKDF2-params. Note: PBKDF2-params copied from PKCS#5 due to ASN.1 version differences.

## Appendix B: ASN.1:1997 Module
- More precise 1997 ASN.1 definitions; Appendix A takes precedence in conflicts.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|-------------|------|-----------|
| R1 | PasswordRecipientInfo version MUST be 0. | shall | 1.2.1 |
| R2 | Conforming implementations MUST include PBKDF2 for key derivation. | must | 2.1 |
| R3 | Conforming implementations MUST implement id-alg-PWRI-KEK key wrap. | must | 2.2 |
| R4 | For KEK encryption, conforming implementations MUST include Triple-DES in CBC mode. | must | 2.2 |
| R5 | Implementations MAY include other algorithms (AES, CAST-128, etc.) | may | 2.2 |
| R6 | Implementations SHOULD NOT include any KSG ciphers (RC4, OFB) or ECB mode. | should not | 2.2 |
| R7 | Check value verification MUST be performed on unwrapping. | shall | 2.3.2 |
| R8 | Pass phrases are STRONGLY RECOMMENDED. | should | 4 |

## Informative Annexes (Condensed)
- **Appendix A, B (ASN.1 modules)**: Provide normative ASN.1 definitions for the PasswordRecipientInfo structure and supporting types. Appendix A uses 1988 ASN.1 (less precise); Appendix B uses 1997 ASN.1. In case of conflict, Appendix A takes precedence.
- **Test vectors (Section 3)**: Provide self-validation examples for key derivation and wrap/unwrap with DES and Triple-DES under various parameters. Included for implementation verification.