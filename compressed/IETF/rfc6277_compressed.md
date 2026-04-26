# RFC 6277: Online Certificate Status Protocol Algorithm Agility
**Source**: IETF | **Version**: Standards Track | **Date**: June 2011 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc6277

## Scope (Summary)
This document specifies rules for OCSP responder signature algorithm selection and defines an extension that allows a client to indicate preferred signature algorithms to a server, thereby improving interoperability in multi-algorithm environments.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2560] Myers, M., et al., "X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP", RFC 2560, June 1999.
- [RFC3279] Bassham, L., et al., "Algorithms and Identifiers for the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3279, April 2002.
- [RFC4055] Schaad, J., et al., "Additional Algorithms and Identifiers for RSA Cryptography for use in the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 4055, June 2005.
- [RFC5280] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [RFC5751] Ramsdell, B. and S. Turner, "Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.2 Message Specification", RFC 5751, January 2010.
- [RFC5912] Hoffman, P. and J. Schaad, "New ASN.1 Modules for the Public Key Infrastructure Using X.509 (PKIX)", RFC 5912, June 2010.

## Definitions and Abbreviations
- **OCSP**: Online Certificate Status Protocol
- **CA**: Certification Authority
- **CRL**: Certificate Revocation List
- **PreferredSignatureAlgorithms**: ASN.1 type defined in Section 4; a SEQUENCE OF PreferredSignatureAlgorithm.
- **PreferredSignatureAlgorithm**: ASN.1 SEQUENCE containing `sigIdentifier` (AlgorithmIdentifier) and optional `pubKeyAlgIdentifier` (SMIMECapability).
- **Key Words**: "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in RFC 2119.

## 1. Introduction (Condensed)
OCSP [RFC2560] requires signed responses but does not specify how signature algorithms are selected. This lack of mechanism causes interoperability failures when multiple algorithms are in use. This document defines a client extension to indicate preferred algorithms and provides rules for responder algorithm selection.

## 2. OCSP Algorithm Agility Requirements (Condensed)
Without a client indication mechanism, a responder cannot reliably choose an algorithm the client supports, especially for unknown certificates. Different algorithms may be needed for efficiency, compromise avoidance, or mismatch with responder keys. This document addresses these issues.

## 3. Updates to Mandatory and Optional Cryptographic Algorithms
This section updates Section 4.3 of RFC 2560 as follows:

- **OLD** (removed): Clients SHALL be capable of DSA; SHOULD be capable of RSA; responders SHALL support SHA1.
- **NEW**:  
  - Clients that request OCSP services **SHALL** be capable of processing responses signed using RSA with SHA-1 (identified by sha1WithRSAEncryption OID [RFC3279]) and RSA with SHA-256 (identified by sha256WithRSAEncryption OID [RFC4055]).  
  - Clients **SHOULD** also be capable of processing responses signed using DSA keys (identified by id-dsa-with-sha1 OID [RFC3279]).  
  - Clients **MAY** support other algorithms.

## 4. Client Indication of Preferred Signature Algorithms
- A client **MAY** declare a preferred set of algorithms by including the `id-pkix-ocsp-pref-sig-algs` extension in `requestExtensions` of the OCSPRequest [RFC2560].
- The extension uses the ASN.1 type `PreferredSignatureAlgorithms` (a SEQUENCE OF `PreferredSignatureAlgorithm`).
- Each `PreferredSignatureAlgorithm` contains:
  - `sigIdentifier` (AlgorithmIdentifier) – the signature algorithm the client prefers.
  - `pubKeyAlgIdentifier` (SMIMECapability, OPTIONAL) – the subject public key algorithm and parameters (e.g., curve) the client prefers in the responder's certificate.
- **The client MUST support** each specified preferred signature algorithm.
- **The client MUST specify** the algorithms in order of preference, from most preferred to least preferred.

## 5. Responder Signature Algorithm Selection
### 5.1 Dynamic Response
A responder **MAY** maximize interoperability by selecting a supported signature algorithm using the following order of precedence (highest first):
1. An algorithm specified as a preferred signing algorithm in the client request.
2. The signing algorithm used to sign a CRL issued by the certificate issuer for the certificate specified by CertID.
3. The signing algorithm used to sign the OCSPRequest.
4. A default signature algorithm advertised out-of-band.
5. A mandatory or recommended signing algorithm for the version of OCSP in use.

A responder **SHOULD** always apply the lowest-numbered selection mechanism that results in the selection of a known and supported algorithm meeting the responder's cryptographic strength criteria.

### 5.2 Static Response
- When using pre-generated responses, the responder **SHOULD** still use the client request data during selection of the pre-generated response to return.
- Responders **MAY** use historical client requests as input to decisions about which algorithms to use for pre-generated responses.

## 6. [Acknowledgements] (Informative – omitted)

## 7. Security Considerations (Condensed with preserved normative statements)
- **The mechanism used to choose the response signing algorithm MUST be considered sufficiently secure** against cryptanalytic attack for the intended application.
- The signing algorithm should generally be at least as strong as the algorithm used to sign the original certificate, though this may not hold for long‑term archival queries.
- **The responder MUST NOT generate a signature using a signing mechanism that is not considered acceptably secure**.
- **A client MUST accept any signing algorithm in a response that it specified as a preferred signing algorithm in the request.**
- **A client MUST NOT specify a preferred signing algorithm that is either not supported or not considered acceptably secure.**
- Man‑in‑the‑middle downgrade attacks on the client indication are not a significant concern because the responder will not sign with weak algorithms and the client can reject unacceptable responses.
- Denial‑of‑service attack surface is slightly increased; considerations from RFC 4732 apply.

## 8. References (Normative and Informative – listed in Normative References above; informative omitted per condensation rules)

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Clients SHALL be capable of processing responses signed using RSA with SHA-1 and RSA with SHA-256. | SHALL | Section 3 |
| R2 | Clients SHOULD be capable of processing DSA signatures (id-dsa-with-sha1). | SHOULD | Section 3 |
| R3 | Clients MAY support other algorithms. | MAY | Section 3 |
| R4 | A client MAY declare a preferred set of algorithms via the `id-pkix-ocsp-pref-sig-algs` extension. | MAY | Section 4 |
| R5 | The client MUST support each specified preferred signature algorithm. | MUST | Section 4 |
| R6 | The client MUST list algorithms in order of preference. | MUST | Section 4 |
| R7 | A responder MAY use the precedence order for dynamic response algorithm selection. | MAY | Section 5.1 |
| R8 | A responder SHOULD apply the lowest‑numbered selection mechanism that yields a known, supported, and sufficiently strong algorithm. | SHOULD | Section 5.1 |
| R9 | For static responses, the responder SHOULD use client request data to select a pre‑generated response. | SHOULD | Section 5.2 |
| R10 | Responders MAY use historical client requests for pre‑generation decisions. | MAY | Section 5.2 |
| R11 | The response signing algorithm selection mechanism MUST be considered sufficiently secure. | MUST | Section 7 |
| R12 | Responder MUST NOT generate a signature using an algorithm not considered acceptably secure. | MUST NOT | Section 7.1 |
| R13 | Client MUST accept any signing algorithm it specified as a preferred algorithm in the request. | MUST | Section 7.1 |
| R14 | Client MUST NOT specify a preferred algorithm that is not supported or not acceptably secure. | MUST NOT | Section 7.1 |

## Informative Annexes (Condensed)

### Appendix A. ASN.1 Modules
Two ASN.1 modules are provided for the extension definitions. They are identical in content but use different syntax versions (2009 and 1988). The key normative definitions are:

```asn1
-- OID and types for Preferred Signature Algorithms extension
id-pkix-ocsp-pref-sig-algs OBJECT IDENTIFIER ::= { id-pkix-ocsp 8 }

PreferredSignatureAlgorithms ::= SEQUENCE OF PreferredSignatureAlgorithm

PreferredSignatureAlgorithm ::= SEQUENCE {
    sigIdentifier        AlgorithmIdentifier{SIGNATURE-ALGORITHM, {...}},
    pubKeyAlgIdentifier  SMIMECapability{PUBLIC-KEY, {...}} OPTIONAL
}
```

The modules import from RFC 5912, RFC 2560, RFC 5280, and RFC 5751. The 1988 module uses older import syntax but maintains the same structure and semantics.