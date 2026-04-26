# RFC 2985: PKCS #9: Selected Object Classes and Attribute Types Version 2.0
**Source**: IETF (RSA Security) | **Version**: 2.0 | **Date**: November 2000 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc2985

## Scope (Summary)
This document defines two auxiliary object classes (pkcsEntity, naturalPerson) and selected attribute types for use with public-key cryptography and LDAP directories. It also includes ASN.1 syntax, matching rules, and BNF schema for LDAP integration.

## Normative References
- [1] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [3] Housley, R., "Cryptographic Message Syntax CMS", RFC 2630, June 1999.
- [8] ISO/IEC 9594-6:1997: Information technology – The Directory: Selected attribute types.
- [10] ISO/IEC 9594-8:1997: Information technology – The Directory: Authentication framework.
- [16] RSA Laboratories. PKCS #10: Certification Request Syntax Standard. Version 1.0, November 1993.
- [21] Wahl, M., et al., "Lightweight Directory Access Protocol (v3): Attribute Syntax Definitions", RFC 2252, December 1997.

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One, per [5].
- **Attributes**: ASN.1 type specifying a set of attributes, each with type (OID) and one or more values.
- **CertificationRequestInfo**: ASN.1 type specifying subject name, public key, and attributes.
- **ContentInfo**: ASN.1 type for content exchanged between entities, with contentType (OID) and content.
- **PrivateKeyInfo**: Type specifying private key and extended attributes.
- **SignerInfo**: Type specifying per-signer info in signed-data, including authenticated and unauthenticated attributes.
- **DER**: Distinguished Encoding Rules for ASN.1 (ISO 8825-1).
- **UCS**: Universal Multiple-Octet Coded Character Set (ISO 10646).
- **UTF8String**: UCS Transformation Format (UTF-8) encoded string.
- **MUST / SHALL / SHOULD / MAY**: interpreted as per RFC 2119.

## Auxiliary Object Classes
### 4.1 The pkcsEntity Object Class
- **pkcsEntity** is an auxiliary object class intended for PKCS-related entities.
- ASN.1 definition:
```asn1
pkcsEntity OBJECT-CLASS ::= {
    SUBCLASS OF { top }
    KIND auxiliary
    MAY CONTAIN { PKCSEntityAttributeSet }
    ID pkcs-9-oc-pkcsEntity
}
```
- PKCSEntityAttributeSet includes: pKCS7PDU, userPKCS12, pKCS15Token, encryptedPrivateKeyInfo.

### 4.2 The naturalPerson Object Class
- **naturalPerson** is an auxiliary object class intended for attributes of human beings.
- ASN.1 definition:
```asn1
naturalPerson OBJECT-CLASS ::= {
    SUBCLASS OF { top }
    KIND auxiliary
    MAY CONTAIN { NaturalPersonAttributeSet }
    ID pkcs-9-oc-naturalPerson
}
```
- NaturalPersonAttributeSet includes: emailAddress, unstructuredName, unstructuredAddress, dateOfBirth, placeOfBirth, gender, countryOfCitizenship, countryOfResidence, pseudonym, serialNumber.

## Selected Attribute Types
### 5.1 For pkcsEntity Object Class
#### 5.1.1 pKCS7PDU
- **Syntax**: ContentInfo. **OID**: pkcs-9-at-pkcs7PDU.
- **Usage**: Stores PKCS #7 PDUs in directory.

#### 5.1.2 userPKCS12
- **Syntax**: PFX. **OID**: pkcs-9-at-userPKCS12 (2.16.840.1.113730.3.1.216).
- **Usage**: Stores PKCS #12 PFX PDUs.

#### 5.1.3 pKCS15Token
- **Syntax**: PKCS15Token. **OID**: pkcs-9-at-pkcs15Token.
- **Usage**: Stores PKCS #15 tokens.

#### 5.1.4 encryptedPrivateKeyInfo
- **Syntax**: EncryptedPrivateKeyInfo. **OID**: pkcs-9-at-encryptedPrivateKeyInfo.
- **Usage**: Stores PKCS #8 encrypted private keys.

### 5.2 For naturalPerson Object Class
#### 5.2.1 emailAddress
- **Syntax**: IA5String (SIZE(1..pkcs-9-ub-emailAddress)). **Equality**: pkcs9CaseIgnoreMatch. **OID**: pkcs-9-at-emailAddress.
- **Multiple values allowed**. Case insensitive.

#### 5.2.2 unstructuredName
- **Syntax**: PKCS9String {pkcs-9-ub-unstructuredName} (choice of IA5String or DirectoryString). **Equality**: pkcs9CaseIgnoreMatch. **OID**: pkcs-9-at-unstructuredName.
- **Multiple values allowed**. Applications SHOULD use IA5String unless internationalization issues require UTF8String. Systems MUST handle all string types.

#### 5.2.3 unstructuredAddress
- **Syntax**: DirectoryString {pkcs-9-ub-unstructuredAddress}. **Equality**: caseIgnoreMatch (per [8]). **OID**: pkcs-9-at-unstructuredAddress.
- **Multiple values allowed**. Applications SHOULD use PrintableString unless issues, then UTF8String. Systems MUST handle all DirectoryString types.

#### 5.2.4 dateOfBirth
- **Syntax**: GeneralizedTime. **Equality**: generalizedTimeMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-dateOfBirth (1.3.6.1.5.5.7.9.1).
- Must be single-valued.

#### 5.2.5 placeOfBirth
- **Syntax**: DirectoryString {pkcs-9-ub-placeOfBirth}. **Equality**: caseExactMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-placeOfBirth (1.3.6.1.5.5.7.9.2).
- Must be single-valued.

#### 5.2.6 gender
- **Syntax**: PrintableString (SIZE(1) FROM ("M" | "F" | "m" | "f")). **Equality**: caseIgnoreMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-gender (1.3.6.1.5.5.7.9.3).
- Must be single-valued. "M"/"m" = male, "F"/"f" = female.

#### 5.2.7 countryOfCitizenship
- **Syntax**: PrintableString (SIZE(2)) constrained to two-letter ISO 3166 code. **Equality**: caseIgnoreMatch. **OID**: pkcs-9-at-countryOfCitizenship (1.3.6.1.5.5.7.9.4).
- Multiple values allowed.

#### 5.2.8 countryOfResidence
- **Syntax**: PrintableString (SIZE(2)) constrained to two-letter ISO 3166 code. **Equality**: caseIgnoreMatch. **OID**: pkcs-9-at-countryOfResidence (1.3.6.1.5.5.7.9.5).
- Multiple values allowed.

#### 5.2.9 pseudonym
- **Syntax**: DirectoryString {pkcs-9-ub-pseudonym}. **Equality**: caseExactMatch. **OID**: id-at-pseudonym (2.5.4.65).
- Multiple values allowed.

#### 5.2.10 serialNumber
- Defined in [8]; no new definition.

### 5.3 For PKCS #7 Data
#### 5.3.1 contentType
- **Syntax**: ContentType (OBJECT IDENTIFIER). **Equality**: objectIdentifierMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-contentType.
- Required if authenticated attributes present. Must be single-valued.

#### 5.3.2 messageDigest
- **Syntax**: MessageDigest (OCTET STRING). **Equality**: octetStringMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-messageDigest.
- Required if authenticated attributes present. Must be single-valued.

#### 5.3.3 signingTime
- **Syntax**: SigningTime (Time from [10]). **Equality**: signingTimeMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-signingTime.
- Must be single-valued. Encoding rules: dates 1950-2049 MUST be UTCTime; others GeneralizedTime. UTCTime MUST be YYMMDDHHMMSSZ, GeneralizedTime YYYYMMDDHHMMSSZ.

#### 5.3.4 randomNonce
- **Syntax**: RandomNonce (OCTET STRING SIZE(4..MAX)). **Equality**: octetStringMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-randomNonce.
- Must be single-valued.

#### 5.3.5 sequenceNumber
- **Syntax**: SequenceNumber (INTEGER (1..MAX)). **Equality**: integerMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-sequenceNumber.
- Must be single-valued.

#### 5.3.6 counterSignature
- **Syntax**: SignerInfo. **OID**: pkcs-9-at-counterSignature.
- Must be unauthenticated attribute. Multiple values allowed. Countersignature computed on the encryptedDigest field of the associated SignerInfo.

### 5.4 For PKCS #10 Certificate Requests
#### 5.4.1 challengePassword
- **Syntax**: DirectoryString {pkcs-9-ub-challengePassword}. **Equality**: caseExactMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-challengePassword.
- Applications SHOULD use PrintableString if possible, else UTF8String. Systems MUST handle all DirectoryString types.

#### 5.4.2 extensionRequest
- **Syntax**: ExtensionRequest (Extensions from [10]). **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-extensionRequest.
- Must be single-valued.

#### 5.4.3 extendedCertificateAttributes (deprecated)
- **Syntax**: SET OF Attribute. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-extendedCertificateAttributes.
- Deprecated; PKCS #6 is historic.

### 5.5 For PKCS #12 or PKCS #15
#### 5.5.1 friendlyName
- **Syntax**: BMPString (SIZE(1..pkcs-9-ub-friendlyName)). **Equality**: caseIgnoreMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-friendlyName.
- Must be single-valued.

#### 5.5.2 localKeyId
- **Syntax**: OCTET STRING. **Equality**: octetStringMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-localKeyId.
- Must be single-valued.

### 5.6 Attributes defined in S/MIME (for completeness)
#### 5.6.1 signingDescription
- **Syntax**: DirectoryString {pkcs-9-ub-signingDescription}. **Equality**: caseIgnoreMatch. **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-signingDescription.
- Provides short synopsis of message.

#### 5.6.2 smimeCapabilities
- **Syntax**: SMIMECapabilities (SEQUENCE OF SMIMECapability). **SINGLE VALUE TRUE**. **OID**: pkcs-9-at-smimeCapabilities.
- Syntax defined in RFC 2633.

## Matching Rules
### 6.1 pkcs9CaseIgnoreMatch
- **Syntax**: PKCS9String {pkcs-9-ub-match}. **OID**: pkcs-9-mr-caseIgnoreMatch (1.2.840.113549.1.9.27.1).
- Compares strings ignoring case. Returns TRUE if same length and characters identical ignoring case; if different ASN.1 syntax, compares if characters in both sets, else fails.

### 6.2 signingTimeMatch
- **Syntax**: SigningTime. **OID**: pkcs-9-mr-signingTimeMatch (1.2.840.113549.1.9.27.2).
- Returns TRUE if attribute value represents same time as presented value; missing seconds assumed zero. If different syntax, convert both to GeneralizedTime UTC and compare octet strings.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | pkcsEntity class MAY contain attributes from PKCSEntityAttributeSet. | may | 4.1 |
| R2 | naturalPerson class MAY contain attributes from NaturalPersonAttributeSet. | may | 4.2 |
| R3 | contentType attribute MUST be single-valued and is required if authenticated attributes present. | must | 5.3.1 |
| R4 | messageDigest attribute MUST be single-valued and is required if authenticated attributes present. | must | 5.3.2 |
| R5 | signingTime attribute MUST be single-valued. Encoding of time MUST follow UTCTime/GeneralizedTime rules per [3]. | must | 5.3.3 |
| R6 | randomNonce attribute MUST be single-valued and at least 4 octets. | must | 5.3.4 |
| R7 | sequenceNumber attribute MUST be single-valued (INTEGER >=1). | must | 5.3.5 |
| R8 | counterSignature attribute MUST be unauthenticated; multiple values allowed. | must | 5.3.6 |
| R9 | challengePassword attribute MUST be single-valued. | must | 5.4.1 |
| R10 | extensionRequest attribute MUST be single-valued. | must | 5.4.2 |
| R11 | extendedCertificateAttributes attribute is deprecated. | deprecated | 5.4.3 |
| R12 | friendlyName attribute MUST be single-valued. | must | 5.5.1 |
| R13 | localKeyId attribute MUST be single-valued. | must | 5.5.2 |
| R14 | signingDescription attribute MUST be single-valued. | must | 5.6.1 |
| R15 | smimeCapabilities attribute MUST be single-valued. | must | 5.6.2 |
| R16 | unstructuredName: Applications SHOULD use IA5String unless internationalization issues require UTF8String. Systems MUST process all string types. | should/must | 5.2.2 |
| R17 | unstructuredAddress: Applications SHOULD use PrintableString unless issues, then UTF8String. Systems MUST handle all DirectoryString types. | should/must | 5.2.3 |
| R18 | challengePassword: Applications SHOULD use PrintableString if possible, else UTF8String. Systems MUST process all DirectoryString types. | should/must | 5.4.1 |
| R19 | pkcs9CaseIgnoreMatch: returns TRUE if strings same length and characters identical ignoring case. | defined | 6.1 |
| R20 | signingTimeMatch: returns TRUE if times equal; if different syntax, convert to GeneralizedTime UTC and compare. | defined | 6.2 |

## Security Considerations
- Attributes in directories may contain personal information; privacy laws apply.
- challengePassword SHOULD NOT be stored unencrypted.
- Attributes of pkcsEntity (PKCS #8, #12, #15) may contain password-protected values; directory SHOULD authenticate requester before delivering to prevent offline password-search attacks. This raises non-repudiation issues.

## Informative Annexes (Condensed)
- **Annex A (ASN.1 module)**: Provides complete ASN.1 module "PKCS-9" with all object class, attribute, matching rule definitions and upper bounds. Source code included in original document.
- **Annex B (BNF schema summary)**: Augmented BNF definitions for all syntaxes, object classes, and attribute types per RFC 2252 for LDAP integration.
- **Annex C (Intellectual property considerations)**: RSA Security makes no patent claims on general constructions; license to copy granted with attribution.
- **Annex D (Revision history)**: Version 1.0 (June 1991), Version 1.1 (added challengePassword, unstructuredAddress, extendedCertificateAttributes), Version 2.0 (added object classes, new attributes, updated ASN.1, added BNF).
- **Annex E (References)**: Lists 22 references including RFCs, ISO standards, and PKCS documents.
- **Annex F (Contact information & About PKCS)**: Contact RSA Laboratories PKCS Editor for further information.