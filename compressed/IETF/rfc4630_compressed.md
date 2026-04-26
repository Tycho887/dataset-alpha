# RFC 4630: Update to DirectoryString Processing in the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
**Source**: IETF | **Version**: Standards Track | **Date**: August 2006 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc4630

## Scope (Summary)
This document updates RFC 3280 to change the handling of the `DirectoryString` type in X.509 certificates and CRLs. The use of `UTF8String` and `PrintableString` is now the preferred encoding; the previous mandate that all certificates issued after December 31, 2003 MUST use `UTF8String` is removed. Exceptions are allowed for backward compatibility with previously issued encodings.

## Normative References
- **[PKIX1]**: Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- **[STDWORDS]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **DirectoryString**: A choice of `PrintableString`, `TeletexString`, `BMPString`, `UTF8String`, and `UniversalString` as defined in X.501.
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL**: As defined in RFC 2119 [STDWORDS].

## Update to RFC 3280, Section 4.1.2.4: Issuer
The original RFC 3280 text is replaced with the following normative text:

> The `DirectoryString` type is defined as a choice of `PrintableString`, `TeletexString`, `BMPString`, `UTF8String`, and `UniversalString`. CAs conforming to this profile MUST use either the `PrintableString` or `UTF8String` encoding of `DirectoryString`, with one exception. When CAs have previously issued certificates with issuer fields with attributes encoded using the `TeletexString`, `BMPString`, or `UniversalString`, the CA MAY continue to use these encodings of the `DirectoryString` to preserve the backward compatibility.

**Effect**: Removes the 31 December 2003 UTF8String deadline. Eliminates prioritized options (a)-(c) and the three exceptions. Permits continued use of `TeletexString`, `BMPString`, or `UniversalString` only for backward compatibility.

## Update to RFC 3280, Section 4.1.2.6: Subject
The original RFC 3280 text is replaced with the following:

> The subject name field is defined as the X.501 type Name. Implementation requirements for this field are those defined for the issuer field (Section 4.1.2.4). CAs conforming to this profile MUST use either the `PrintableString` or `UTF8String` encoding of `DirectoryString`, with one exception. When CAs have previously issued certificates with subject fields with attributes encoded using the `TeletexString`, `BMPString`, or `UniversalString`, the CA MAY continue to use these encodings of the `DirectoryString` in new certificates for the same subject to preserve backward compatibility.
>
> Since name comparison assumes that attribute values encoded in different types (e.g., `PrintableString` and `UTF8String`) are assumed to represent different strings, any name components that appear in both the subject field and the issuer field SHOULD use the same encoding throughout the certification path.

**Effect**: Aligns subject field encoding rules with issuer field. Adds new guidance on consistent encoding for name comparison.

## Update to RFC 3280, Section 4.2.1.7: Subject Alternative Name
The original RFC 3280 text is replaced with the following:

> When the subjectAltName extension contains a DN in the directoryName, the encoding preference is defined in Section 4.1.2.4. The DN MUST be unique for each subject entity certified by the one CA as defined by the issuer name field. A CA MAY issue more than one certificate with the same DN to the same subject entity.

**Effect**: Adds cross-reference to encoding preference; otherwise unchanged.

## Security Considerations
- Consistent encoding for name components ensures that name constraints specified in [PKIX1] work as expected.
- Visual representation of strings may be ambiguous due to similar glyphs or composed characters (e.g., precomposed vs. decomposed Unicode). Certificate issuers and relying parties must be aware that visual comparison of different names may falsely indicate equality.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | CAs MUST use either `PrintableString` or `UTF8String` encoding of `DirectoryString` for issuer and subject fields. | MUST | Section 3, Section 4 |
| R2 | CAs MAY continue to use `TeletexString`, `BMPString`, or `UniversalString` for backward compatibility when previously issued certificates used those encodings. | MAY | Section 3, Section 4 |
| R3 | Name components appearing in both subject and issuer fields SHOULD use the same encoding throughout the certification path. | SHOULD | Section 4 |
| R4 | When `subjectAltName` contains a directoryName, the encoding preference follows Section 4.1.2.4. The DN MUST be unique per CA as defined by issuer name field. | MUST | Section 5 |

## Informative Annexes (Condensed)
- **Introduction (Section 1)**: Rationale – implementation and deployment experience resolved uncertainty about international character sets. UTF8String and PrintableString are the preferred encodings; the 2003 deadline is removed.
- **Terminology (Section 2)**: Standard RFC 2119 keyword definitions.