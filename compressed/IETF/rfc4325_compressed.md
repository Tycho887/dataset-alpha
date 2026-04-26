# RFC 4325: Internet X.509 Public Key Infrastructure Authority Information Access Certificate Revocation List (CRL) Extension
**Source**: IETF | **Version**: Standards Track | **Date**: December 2005 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc4325

## Scope (Summary)
This document updates RFC 3280 by defining the Authority Information Access Certificate Revocation List (CRL) extension to provide a means of discovering and retrieving CRL issuer certificates.

## Normative References
- RFC 2119: "Key words for use in RFCs to Indicate Requirement Levels"
- RFC 2587: "Internet X.509 Public Key Infrastructure: LDAPv2 Schema"
- RFC 3280: "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile"
- RFC 2616: "Hypertext Transfer Protocol -- HTTP/1.1"
- RFC 3986: "Uniform Resource Identifier (URI): Generic Syntax"
- RFC 2251: "Lightweight Directory Access Protocol (v3)"
- RFC 2585: "Internet X.509 Public Key Infrastructure Operational Protocols: FTP and HTTP"
- RFC 2797: "Certificate Management Messages over CMS"

## Definitions and Abbreviations
- **MUST/MUST NOT/REQUIRED/SHALL/SHALL NOT/SHOULD/SHOULD NOT/RECOMMENDED/MAY/OPTIONAL**: interpreted as described in RFC 2119.
- **Authority Information Access (AIA) extension**: An extension defined in RFC 3280, here reused in CRLs with restricted semantics.

## Section 2: Authority Information Access CRL Extension
- **Criticality**: This CRL extension MUST NOT be marked critical.
- **OID**: This extension MUST be identified by the object identifier 1.3.6.1.5.5.7.1.1 (id-pe-authorityInfoAccess).
- **Syntax**: The AuthorityInfoAccessSyntax MUST be used to form the extension value. The ASN.1 definition from RFC 3280 is repeated below:
  ```
  id-pe-authorityInfoAccess OBJECT IDENTIFIER ::= { id-pe 1 }
  AuthorityInfoAccessSyntax ::= SEQUENCE SIZE (1..MAX) OF AccessDescription
  AccessDescription ::= SEQUENCE {
      accessMethod  OBJECT IDENTIFIER,
      accessLocation GeneralName }
  id-ad OBJECT IDENTIFIER ::= { id-pkix 48 }
  id-ad-caIssuers OBJECT IDENTIFIER ::= { id-ad 2 }
  ```
- **Access Method**: When present in a CRL, this extension MUST include at least one AccessDescription specifying `id-ad-caIssuers` as the accessMethod. Access method types other than `id-ad-caIssuers` MUST NOT be included.
- **Access Location**:
  - At least one instance of AccessDescription SHOULD specify an accessLocation that is an HTTP [HTTP/1.1] or Lightweight Directory Access Protocol [LDAP] Uniform Resource Identifier [URI].
  - **HTTP or FTP**: accessLocation MUST be a uniformResourceIdentifier. The URI MUST point to a certificate containing file. The certificate file MUST contain either a single Distinguished Encoding Rules (DER) [X.690] encoded certificate (indicated by the `.cer` file extension) or a collection of certificates (indicated by the `.p7c` file extension). Conforming applications that support HTTP or FTP for accessing certificates MUST be able to accept `.cer` files and SHOULD be able to accept `.p7c` files. HTTP server implementations accessed via the URI SHOULD use the appropriate MIME content-type for the certificate containing file ( `application/pkix-cert` for `.cer`, `application/pkcs7-mime` for `.p7c`). Consuming clients may use the MIME type and file extension as a hint but should not depend solely on the presence of the correct MIME type or file extension.
  - **directoryName**: Information obtained from whatever directory server is locally configured. When one CA public key is used to validate signatures on certificates and CRLs, the desired CA certificate is stored in the `crossCertificatePair` and/or `cACertificate` attributes as specified in RFC 2587. When different public keys are used, the desired certificate is stored in the `userCertificate` attribute. Implementations that support the directoryName form of accessLocation MUST be prepared to find the needed certificate in any of these three attributes.
  - **LDAP**: The accessLocation SHOULD be a uniformResourceIdentifier. The URI MUST specify a distinguishedName and attribute(s) and MAY specify a host name. Omitting the host name has the effect of specifying the use of whatever LDAP server is locally configured. The URI MUST list appropriate attribute descriptions for one or more attributes holding certificates or cross‑certificate pairs.

## Security Considerations
- Implementers should take into account the possible existence of multiple unrelated CAs and CRL issuers with the same name.
- Implementers should be aware of risks involved if the Authority Information Access extensions of corrupted CRLs contain links to malicious code. Implementers should always take the steps of validating the retrieved data to ensure that the data is properly formed.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | This CRL extension MUST NOT be marked critical. | MUST | Section 2 |
| R2 | This extension MUST be identified by the OID 1.3.6.1.5.5.7.1.1. | MUST | Section 2 |
| R3 | The extension MUST include at least one AccessDescription specifying `id-ad-caIssuers` as the accessMethod. | MUST | Section 2 |
| R4 | Access method types other than `id-ad-caIssuers` MUST NOT be included. | MUST | Section 2 |
| R5 | At least one AccessDescription SHOULD specify an accessLocation that is an HTTP or LDAP URI. | SHOULD | Section 2 |
| R6 | For HTTP or FTP, accessLocation MUST be a uniformResourceIdentifier and the URI MUST point to a certificate containing file. | MUST | Section 2 |
| R7 | The certificate file MUST contain either a single DER encoded certificate (`.cer`) or a collection of certificates (`.p7c`). | MUST | Section 2 |
| R8 | Conforming applications that support HTTP or FTP MUST be able to accept `.cer` files and SHOULD be able to accept `.p7c` files. | MUST / SHOULD | Section 2 |
| R9 | HTTP server SHOULD use the appropriate MIME content-type for the certificate containing file. | SHOULD | Section 2 |
| R10 | Implementations that support the directoryName form of accessLocation MUST be prepared to find the needed certificate in any of the `crossCertificatePair`, `cACertificate`, or `userCertificate` attributes. | MUST | Section 2 |
| R11 | For LDAP URI, accessLocation SHOULD be a uniformResourceIdentifier. The URI MUST specify a distinguishedName and attribute(s). The URI MUST list appropriate attribute descriptions for one or more attributes holding certificates or cross‑certificate pairs. | SHOULD / MUST | Section 2 |

## Informative References (Condensed)
- ITU‑T X.680 (2002): Abstract Syntax Notation One (ASN.1).
- ITU‑T X.690: ASN.1 encoding rules (BER, CER, DER), used for certificate encoding.