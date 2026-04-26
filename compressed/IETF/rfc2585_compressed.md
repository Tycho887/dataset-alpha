# RFC 2585: Internet X.509 Public Key Infrastructure Operational Protocols: FTP and HTTP
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: May 1999 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc2585

## Scope (Summary)
Specifies conventions for using FTP and HTTP to retrieve X.509 certificates and certificate revocation lists (CRLs) from PKI repositories. Also registers two MIME media types for certificate and CRL transfer.

## Normative References
- [RFC 959] Postel, J. and J. Reynolds, "File Transfer Protocol (FTP)", STD 5, RFC 959, October 1985.
- [RFC 1738] Berners-Lee, T., Masinter, L. and M. McCahill, "Uniform Resource Locators (URL)", RFC 1738, December 1994.
- [RFC 2068] Fielding, R., Gettys, J., Mogul, J., Frystyk, H. and T. Berners-Lee; "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2068, January 1997.

## Definitions and Abbreviations
- **End Entity**: user of PKI certificates and/or end user system that is the subject of a certificate.
- **CA**: certification authority.
- **RA**: registration authority, i.e., an optional system to which a CA delegates certain management functions.
- **Repository**: a system or collection of distributed systems that store certificates and CRLs and serves as a means of distributing these certificates and CRLs to end entities.
- **CRL**: certificate revocation list.

## FTP Conventions
### 2. FTP Conventions
- **URI GeneralName**: The URI form of GeneralName shall be used to specify the location where issuer certificates and CRLs may be obtained. Example: `ftp://ftp.your.org/pki/id48.cer`
- **Certificate file naming**: For convenience, the names of files that contain certificates should have a suffix of `.cer`. Each `.cer` file contains exactly one certificate, encoded in DER format.
- **CRL file naming**: Likewise, the names of files that contain CRLs should have a suffix of `.crl`. Each `.crl` file contains exactly one CRL, encoded in DER format.
- **Use scope**: This service satisfies retrieval of information related to a certificate already identified by a URI; it is not intended for general certificate discovery.

## HTTP Conventions
### 3. HTTP Conventions
- **URI GeneralName**: The URI form of GeneralName shall be used to specify the location where issuer certificates and CRLs may be obtained. Example: `http://www.your.org/pki/id48.cer`
- **Certificate file naming**: For convenience, the names of files that contain certificates should have a suffix of `.cer`. Each `.cer` file contains exactly one certificate, encoded in DER format.
- **CRL file naming**: Likewise, the names of files that contain CRLs should have a suffix of `.crl`. Each `.crl` file contains exactly one CRL, encoded in DER format.
- **Use scope**: Same as FTP scope.

## MIME Registrations
### 4.1. application/pkix-cert
- **MIME media type name**: application
- **MIME subtype name**: pkix-cert
- **Required parameters**: None
- **Optional parameters**: version (default value is "1")
- **Encoding considerations**: none for 8‑bit transports; most likely Base64 for 7‑bit transports (e.g., SMTP)
- **Security considerations**: Carries a cryptographic certificate
- **File extension(s)**: .CER

### 4.2. application/pkix-crl
- **MIME media type name**: application
- **MIME subtype name**: pkix-crl
- **Required parameters**: None
- **Optional parameters**: version (default value is "1")
- **Encoding considerations**: same as above
- **Security considerations**: Carries a cryptographic certificate revocation list
- **File extension(s)**: .CRL

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The URI form of GeneralName shall be used to specify the location where issuer certificates and CRLs may be obtained. | shall | §2, §3 |
| R2 | Certificate files should have suffix `.cer`. | should | §2, §3 |
| R3 | Each `.cer` file shall contain exactly one certificate, encoded in DER format. | shall | §2, §3 |
| R4 | CRL files should have suffix `.crl`. | should | §2, §3 |
| R5 | Each `.crl` file shall contain exactly one CRL, encoded in DER format. | shall | §2, §3 |
| R6 | MIME media type `application/pkix-cert` shall be used with optional version parameter (default "1"). | shall | §4.1 |
| R7 | MIME media type `application/pkix-crl` shall be used with optional version parameter (default "1"). | shall | §4.2 |

## Informative Annexes (Condensed)
- **Model (Section 1.1)**: Defines components: End Entity, CA, RA, Repository. Describes two types of transactions (operational and management) and the flow of certificate/CRL publishing and retrieval.
- **Security Considerations**: Since certificates and CRLs are digitally signed, no additional integrity or privacy service is necessary. HTTP caching proxies may return out‑of‑date responses if misconfigured. Operators of FTP/HTTP servers should authenticate publishers, but authentication is not required for retrieval.