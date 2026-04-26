# RFC 8392: CBOR Web Token (CWT)
**Source**: IETF | **Version**: Standards Track | **Date**: May 2018 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc8392

## Scope (Summary)
Defines CBOR Web Token (CWT), a compact means of representing claims encoded in CBOR and secured using COSE. CWT is derived from JSON Web Token (JWT) but uses CBOR for efficiency in constrained environments such as IoT.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC7049] Bormann, C. and P. Hoffman, "Concise Binary Object Representation (CBOR)", RFC 7049, October 2013.
- [RFC7519] Jones, M., et al., "JSON Web Token (JWT)", RFC 7519, May 2015.
- [RFC8152] Schaad, J., "CBOR Object Signing and Encryption (COSE)", RFC 8152, July 2017.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.
- [IANA.CBOR.Tags] IANA, "Concise Binary Object Representation (CBOR) Tags"
- [IANA.CoAP.Content-Formats] IANA, "CoAP Content-Formats"
- [IANA.CWT.Claims] IANA, "CBOR Web Token (CWT) Claims"
- [IANA.MediaTypes] IANA, "Media Types"

## Definitions and Abbreviations
- **StringOrURI**: Same meaning and processing as JWT StringOrURI (RFC 7519 Section 2) but represented as a CBOR text string.
- **NumericDate**: Same meaning as JWT NumericDate (RFC 7519 Section 2) but represented as a CBOR numeric date (RFC 7049 Section 2.4.1) with the leading tag 1 (epoch-based date/time) **MUST** be omitted.
- **Claim Name**: Human-readable name identifying a claim.
- **Claim Key**: CBOR map key identifying a claim.
- **Claim Value**: CBOR map value representing the value of the claim.
- **CWT Claims Set**: The CBOR map containing the claims conveyed by the CWT.

## Section 1: Introduction
JWT uses JSON; CWT uses CBOR for compactness. CWT references JWT claims and uses COSE for security.

### 1.1. CBOR-Related Terminology
CBOR uses integers as map keys for compactness; JSON only uses strings.

## Section 2: Terminology
Key words (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL) per BCP 14. Reuses terminology from JWT and COSE.

## Section 3: Claims
- Context determines mandatory claims. Unknown claims **MUST** be ignored.
- Claim Keys are integers or text strings for compactness.

### 3.1. Registered Claims
None are mandatory.

#### 3.1.1. iss (Issuer) Claim
- Same processing as JWT "iss" (RFC 7519 Section 4.1.1), value is StringOrURI. Claim Key: 1.

#### 3.1.2. sub (Subject) Claim
- Same as JWT "sub" (RFC 7519 Section 4.1.2), value is StringOrURI. Claim Key: 2.

#### 3.1.3. aud (Audience) Claim
- Same as JWT "aud" (RFC 7519 Section 4.1.3), value is StringOrURI or array of StringOrURI. Claim Key: 3.

#### 3.1.4. exp (Expiration Time) Claim
- Same as JWT "exp" (RFC 7519 Section 4.1.4), value is NumericDate. Claim Key: 4.

#### 3.1.5. nbf (Not Before) Claim
- Same as JWT "nbf" (RFC 7519 Section 4.1.5), value is NumericDate. Claim Key: 5.

#### 3.1.6. iat (Issued At) Claim
- Same as JWT "iat" (RFC 7519 Section 4.1.6), value is NumericDate. Claim Key: 6.

#### 3.1.7. cti (CWT ID) Claim
- Same as JWT "jti" (RFC 7519 Section 4.1.7), value is a byte string. Claim Key: 7.

## Section 4: Summary of Claim Names, Keys, and Value Types
| Name | Key | Value Type |
|------|-----|------------|
| iss  | 1   | text string |
| sub  | 2   | text string |
| aud  | 3   | text string |
| exp  | 4   | integer or floating-point number |
| nbf  | 5   | integer or floating-point number |
| iat  | 6   | integer or floating-point number |
| cti  | 7   | byte string |

## Section 5: CBOR Tags and Claim Values
Claim values defined in this specification **MUST NOT** be prefixed with any CBOR tag (e.g., tag 1 for dates is unnecessary). Future claim definitions may require tags.

## Section 6: CWT CBOR Tag
Optional; if present, the CWT tag (61) **MUST** prefix a tagged object using one of the COSE CBOR tags. Example: `61(17(COSE_Mac0 object))`.

## Section 7: Creating and Validating CWTs
### 7.1. Creating a CWT
1. Create CWT Claims Set.
2. Let Message = binary representation of CWT Claims Set.
3. Create COSE Header (valid per RFC 8152).
4. Three cases:
   - Signed: create COSE_Sign/COSE_Sign1, all steps per RFC 8152.
   - MACed: create COSE_Mac/COSE_Mac0, all steps per RFC 8152.
   - Encrypted: create COSE_Encrypt/COSE_Encrypt0, all steps per RFC 8152.
5. For nested operations, Message becomes the tagged COSE object; repeat from Step 3.
6. Prepend COSE CBOR tag and optionally CWT CBOR tag.

### 7.2. Validating a CWT
- If any step fails, the CWT **MUST** be rejected.
1. Verify it is valid CBOR.
2. If CWT tag present, remove it and verify a COSE tag follows.
3. Identify COSE type from tag or context.
4. COSE Header must contain only understood/supported parameters (or those specified as ignorable).
5. Validate according to the COSE type; let Message = payload/plaintext.
6. If Message begins with a COSE tag, go to Step 1 (nested).
7. Verify Message is a valid CBOR map (CWT Claims Set).

## Section 8: Security Considerations (Condensed)
- Security relies on COSE. Claims must be protected against modification. Recipient must authenticate the CWT creator. For nested operations, sign then encrypt to prevent signature stripping.

## Section 9: IANA Considerations (Condensed)
- Created "CBOR Web Token (CWT) Claims" registry (IANA).
- Registration reviewed on cwt-reg-review@ietf.org; Designated Experts appointed.
- Claim Key ranges: -256..255 and string length 1: Standards Action; -65536..-257 and 256..65535 and string length 2: Specification Required; others: Expert Review or Private Use.
- Initial registry includes keys 0 (RESERVED) and 1–7 as per Section 4.
- Registered media type "application/cwt" in IANA Media Types; CoAP Content-Format ID 61; CBOR Tag 61 for CWT.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Unknown claims **MUST** be ignored. | MUST | Section 3 |
| R2 | Claim values defined in this specification **MUST NOT** be prefixed with any CBOR tag. | MUST | Section 5 |
| R3 | NumericDate encoding: leading tag 1 (epoch-based date/time) **MUST** be omitted. | MUST | Section 2 (definition) |
| R4 | If CWT tag is present, it **MUST** prefix a tagged object using one of the COSE CBOR tags. | MUST | Section 6 |
| R5 | COSE Header in a CWT **MUST** be valid per RFC 8152. | MUST | Section 7.1 Step 3 |
| R6 | For signed/MACed/encrypted CWTs, all steps in RFC 8152 for the respective COSE object **MUST** be followed. | MUST | Section 7.1 Step 4 |
| R7 | If any validation step fails, the CWT **MUST** be rejected. | MUST | Section 7.2 |
| R8 | During validation, COSE Header must contain only understood/supported parameters (or those specified as ignorable). | MUST (implied by "verify") | Section 7.2 Step 4 |
| R9 | For nested operations, if Message begins with a COSE CBOR tag, validation continues from step 1. | MUST (implied) | Section 7.2 Step 6 |

## Informative Annexes (Condensed)
- **Appendix A (Examples)**: Provides detailed examples of CWT Claims Sets, keys (128-bit, 256-bit symmetric, ECDSA P-256), signed CWT, MACed CWT, encrypted CWT, nested CWT, and MACed CWT with floating-point value. All presented in hex and CBOR diagnostic notation for verification.

- **Acknowledgements**: Acknowledges contributions from JWT authors and many IETF participants. (Not normative.)