# RFC 4262: X.509 Certificate Extension for S/MIME Capabilities
**Source**: IETF | **Version**: RFC 4262 | **Date**: December 2005 | **Type**: Normative (Standards Track)
**Original**: https://www.rfc-editor.org/rfc/rfc4262

## Scope (Summary)
Defines an optional X.509 certificate extension (per RFC 3280) to indicate the S/MIME cryptographic capabilities (content encryption algorithms, etc.) of the certificate subject, complementing the SMIMECapabilities signed attribute (RFC 3851). Enables senders of encrypted messages to select appropriate algorithms when no prior S/MIME exchange has occurred. Limited to static capabilities; dynamic updates are out of scope.

## Normative References
- RFC 2119: "Key words for use in RFCs to Indicate Requirement Levels" (BCP 14)
- RFC 3280: "Internet X.509 Public Key Infrastructure Certificate and CRL Profile"
- RFC 3851: "S/MIME Version 3.1 Message Specification"

## Definitions and Abbreviations
- **S/MIME**: Secure/Multipurpose Internet Mail Extensions
- **CA**: Certification Authority
- **SMIMECapabilities**: ASN.1 SEQUENCE OF SMIMECapability (OID 1.2.840.113549.1.9.15)
- **SMIMECapability**: ASN.1 SEQUENCE { capabilityID OBJECT IDENTIFIER, parameters ANY DEFINED BY capabilityID OPTIONAL }
- **Key words**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (as per RFC 2119)

## S/MIME Capabilities Extension
### Extension Definition
- **E1**: The S/MIME Capabilities extension data structure SHALL be identical to the SMIMECapabilities attribute structure defined in RFC 3851. (The ASN.1 is included for illustration.)
- **E2**: All content requirements defined for the SMIMECapabilities attribute in RFC 3851 apply also to this extension (normative).
- **E3**: CAs SHOULD limit the type of included S/MIME Capabilities to those relevant to the intended use of the certificate.
- **E4**: Client applications processing this extension MAY ignore any present S/MIME Capabilities and SHOULD gracefully ignore any present S/MIME Capabilities not considered relevant to the particular use.
- **E5**: This extension MUST NOT be marked critical.

### Use in Applications
- **A1**: Applications using this extension SHOULD NOT use information from it if more reliable and relevant authenticated capabilities information is available. (What constitutes "more reliable" is outside the scope of this specification.)

## Security Considerations Summary
The extension states the subject’s capabilities at certificate issuance; change during the certificate lifetime may require revocation if an algorithm is broken or too weak for the governing security policy. The sender remains responsible for choosing sufficiently strong encryption.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| E1 | Extension data structure identical to SMIMECapabilities attribute (RFC 3851) | SHALL (implied) | Section 2 |
| E2 | All content requirements from RFC 3851 apply to this extension | SHALL (implied) | Section 2 |
| E3 | Limit included capabilities to types relevant to certificate use | SHOULD | Section 2 |
| E4 | Clients may ignore capabilities; must gracefully ignore irrelevant ones | MAY / SHOULD | Section 2 |
| E5 | Extension MUST NOT be marked critical | MUST NOT | Section 2 |
| A1 | Do not use extension when more reliable authenticated capabilities available | SHOULD NOT | Section 3 |

*Note: Informative annexes are not present in the original document.*