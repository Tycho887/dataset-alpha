# RFC 3281: An Internet Attribute Certificate Profile for Authorization
**Source**: IETF Network Working Group | **Version**: Standards Track | **Date**: April 2002 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc3281/

## Scope (Summary)
This specification defines a profile for X.509 Attribute Certificates (ACs) for use in Internet protocols, covering a common baseline for broad interoperability with emphasis on email, IPSec, and WWW security. It distinguishes ACs from public key certificates (PKCs) and supports both "push" and "pull" distribution models. ACs provide authorization information such as group membership, role, clearance, or other attributes.

## Normative References
- BCP 14, RFC 2119 (Key words for requirement levels)
- RFC 3280 [PKIXPROF] (X.509 PKI Certificate and CRL Profile)
- RFC 3279 [PKIXALGS] (Algorithms and Identifiers for X.509 PKI)
- ITU-T X.509 (2000) [X.509-2000]
- ITU-T X.501 (1993) [X.501-1993]
- RFC 2560 [OCSP] (Online Certificate Status Protocol)
- RFC 1738 [URL] (Uniform Resource Locators)

## Definitions and Abbreviations
- **AA**: Attribute Authority (synonymous with AC issuer)
- **AC**: Attribute Certificate
- **AC user**: any entity that parses or processes an AC
- **AC verifier**: any entity that checks validity of an AC and uses the result
- **AC issuer**: entity that signs the AC (synonymous with AA)
- **AC holder**: entity indicated (maybe indirectly) in the holder field
- **Client**: entity requesting action for which authorization is checked
- **Proxying**: application server acting as client on behalf of a user (not delegation)
- **PKC**: Public Key Certificate (X.509 Certificate as profiled in PKIXPROF)
- **Server**: entity requiring authorization checks

## Requirements
### Time/Validity
1. Support for short-lived (hours) and long-lived ACs. Short-lived ACs may not need revocation.

### Attribute Types
2. Issuers MAY define their own attribute types for closed domains.
3. Standard attribute types MUST be defined: access identity, group, role, clearance, audit identity, charging identity.
4. Standard attribute types MUST permit distinction between domains (e.g., same group name from different authorities).

### Targeting of ACs
5. ACs SHOULD be targetable to one or a few servers; trustworthy non-target server MUST reject the AC.

### Push vs. Pull
6. ACs MUST be usable in both push (client to server) and pull (server retrieves) models.

## Attribute Certificate Profile
### 4.1 X.509 Attribute Certificate Definition
- **AttributeCertificate** ::= SEQUENCE { acinfo, signatureAlgorithm, signatureValue }
- **AttributeCertificateInfo** ::= SEQUENCE { version (v2), holder, issuer, signature, serialNumber, attrCertValidityPeriod, attributes, issuerUniqueID OPTIONAL, extensions OPTIONAL }
- **Holder** ::= SEQUENCE { baseCertificateID [0] OPTIONAL, entityName [1] OPTIONAL, objectDigestInfo [2] OPTIONAL }
- **AttCertIssuer** ::= CHOICE { v1Form (MUST NOT be used), v2Form [0] V2Form }
- **V2Form** ::= SEQUENCE { issuerName OPTIONAL (MUST be present in this profile), baseCertificateID [0] OPTIONAL (MUST NOT), objectDigestInfo [1] OPTIONAL (MUST NOT) }
- **AttCertValidityPeriod** ::= SEQUENCE { notBeforeTime GeneralizedTime, notAfterTime GeneralizedTime }

### 4.2 Profile of Standard Fields
- **GeneralName**: MUST support dNSName, directoryName, uniformResourceIdentifier, iPAddress. MUST NOT use x400Address, ediPartyName, registeredID. MAY use otherName for Internet Standards (e.g., Kerberos principal).
- **Version**: MUST be v2.
- **Holder**: RECOMMEND that only one option (baseCertificateID, entityName, or objectDigestInfo) be used. Where PKC authentication is used, holder SHOULD use baseCertificateID. With baseCertificateID, holder.baseCertificateID.issuer MUST be same as PKC issuer (non-empty DN). entityName MUST match PKC subject or subjectAltName. objectDigestInfo optional (see section 7.3). Protocol SHOULD specify holder option.
- **Issuer**: MUST use v2Form with exactly one GeneralName in issuerName containing non-empty directoryName. baseCertificateID and objectDigestInfo MUST be omitted.
- **Signature**: MUST use one of the signing algorithms from [PKIXALGS]. Conformant implementations MUST honor all MUST/SHOULD/MAY statements in [PKIXALGS].
- **Serial Number**: issuer/serialNumber pair MUST be unique. serialNumber MUST be positive integer (sign bit zero, leading '00'H if needed). AC users MUST handle serialNumber longer than 4 octets. Conformant ACs MUST NOT have serialNumber longer than 20 octets.
- **Validity Period**: GeneralizedTime values MUST be in UTC (YYYYMMDDHHMMSSZ), MUST include seconds, MUST NOT include fractional seconds.
- **Attributes**: Each AttributeType in the SEQUENCE MUST be unique. AC MUST contain at least one attribute. AC users MUST handle multiple values for all attribute types.
- **Issuer Unique Identifier**: MUST NOT be used unless also used in AC issuer's PKC; then MUST be used.
- **Extensions**: AC with no extensions conforms. If any critical extension other than those defined in section 4.3 is used, AC does not conform. Non-critical private extensions allowed.

### 4.3 Extensions
#### 4.3.1 Audit Identity
- OID: { id-pe 4 }
- Syntax: OCTET STRING (1 to 20 octets)
- Criticality: MUST be TRUE
- Used to obscure holder identity in audit trails. Server + AC issuer MUST be able to identify holder from audit identity.

#### 4.3.2 AC Targeting
- OID: { id-ce 55 }
- Syntax: SEQUENCE OF Targets (but conforming issuers MUST produce only one Targets element; users MUST accept SEQUENCE OF)
- Criticality: MUST be TRUE
- If present, AC SHOULD only be usable at specified servers. Non-target server MUST reject AC. The targetCert CHOICE MUST NOT be used.

#### 4.3.3 Authority Key Identifier
- OID: { id-ce 35 }
- Syntax: AuthorityKeyIdentifier (as per [PKIXPROF])
- Criticality: MUST be FALSE
- SHOULD be included to assist signature verification.

#### 4.3.4 Authority Information Access
- OID: { id-pe 1 }
- Syntax: AuthorityInfoAccessSyntax
- Criticality: MUST be FALSE
- MAY be used for revocation status (OCSP). accessLocation MUST be HTTP URL.

#### 4.3.5 CRL Distribution Points
- OID: { id-ce 31 }
- Syntax: CRLDistPointsSyntax
- Criticality: MUST be FALSE
- If present, exactly one distribution point, using DistributionPointName with fullName containing either DN or URI (HTTP or LDAP URL).

#### 4.3.6 No Revocation Available
- OID: { id-ce 56 }
- Syntax: NULL (DER '0500'H)
- Criticality: MUST be FALSE
- Indicates no revocation info will be provided. AC verifier may find CRL but AC will never appear.

### 4.4 Attribute Types
- **IetfAttrSyntax**: SEQUENCE { policyAuthority [0] GeneralNames OPTIONAL, values SEQUENCE OF CHOICE { octets, oid, string } } – Each value MUST use same choice.
- **Service Authentication Information** (id-aca 1): SvceAuthInfo – Multiple allowed.
- **Access Identity** (id-aca 2): SvceAuthInfo – authInfo MUST NOT be present.
- **Charging Identity** (id-aca 3): IetfAttrSyntax – One attribute value only; multiple values within syntax.
- **Group** (id-aca 4): IetfAttrSyntax – One attribute value only; multiple values within syntax.
- **Role** (id-at 72): RoleSyntax – roleAuthority OPTIONAL, roleName MUST present (uniformResourceIdentifier). Multiple allowed.
- **Clearance** (joint-iso-ccitt(2) ds(5) module(1) selected-attribute-types(5) clearance(55)): Clearance syntax – Multiple allowed.

### 4.5 Profile of AC issuer's PKC
- MUST conform to [PKIXPROF].
- keyUsage MUST NOT explicitly forbid digitalSignature.
- AC issuer MUST NOT also be a PKC issuer (CA). basicConstraints cA MUST NOT be TRUE.

## Attribute Certificate Validation
To be valid, AC MUST satisfy all:
1. Holder's PKC (if used) found and verified per [PKIXPROF].
2. AC signature correct, AC issuer's PKC chain verified per [PKIXPROF].
3. AC issuer's PKC conforms to section 4.5.
4. AC issuer directly trusted as AA (by configuration).
5. Evaluation time within validity (including boundaries).
6. Targeting check passes (section 4.3.2).
7. No unsupported critical extensions.

Additional checks: May reject based on configuration; May filter attributes based on configuration.

## Revocation
- **Never revoke scheme**: noRevAvail extension MUST be present. AC user MUST support this. AC issuer MUST support this.
- **Pointer in AC scheme**: Use authorityInfoAccess or crlDistributionPoints. AC user SHOULD support; if only never revoke supported, ACs without noRevAvail MUST be rejected. AC issuer MUST support if any AC is issued without noRevAvail.
- An AC MUST NOT contain both noRevAvail and a pointer.
- AC verifier MAY use any source for revocation status.

## Optional Features
### 7.1 Attribute Encryption
- Use CMS EnvelopedData. Encrypted attributes stored in encAttrs attribute (id-aca 6, ContentInfo, multiple allowed).
- Cleartext: ACClearAttrs { acIssuer, acSerial, attrs }.
- Decryption failure MUST cause AC rejection.

### 7.2 Proxying
- ProxyInfo extension (id-pe 10, critical MUST be TRUE).
- Proxy check: sender matches holder or is in a proxy set that also includes current server. For multiple hops, all targets on path MUST be in same proxy set.

### 7.3 Use of ObjectDigestInfo
- Holder MAY be identified by digest. Only publicKey and publicKeyCert allowed (not otherObjectTypes).
- If publicKey, digest over SubjectPublicKeyInfo including AlgorithmIdentifier. If PKC, digest over entire DER-encoded PKC.
- Implementations MUST handle algorithms from [PKIXPROF] section 7.3.

### 7.4 AA Controls
- AAControls extension (id-pe 6) in CA/AA PKCs.
- Fields: pathLenConstraint, permittedAttrs, excludedAttrs, permitUnSpecified.
- Additional validation checks: AA CA must be trusted; all PKCs from AA CA to AC issuer must contain AAControls; only allowed attributes may be used; others ignored.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | AC version MUST be v2 | shall | 4.2.1 |
| R2 | AC issuer MUST use v2Form with non-empty directoryName in issuerName | shall | 4.2.3 |
| R3 | AC serial number MUST be positive, unique per issuer | shall | 4.2.5 |
| R4 | AC MUST contain at least one attribute | shall | 4.2.7 |
| R5 | AC targeting extension, if present, MUST be critical | shall | 4.3.2 |
| R6 | AC with unsupported critical extension MUST be rejected | shall | 5 |
| R7 | AC issuer MUST NOT be a CA | shall | 4.5 |
| R8 | AC verifier MUST support “never revoke” scheme | shall | 6 |
| R9 | AC issuer MUST support “never revoke” scheme | shall | 6 |
| R10 | AC MUST NOT contain both noRevAvail and revocation pointer | shall | 6 |
| R11 | Attribute encryption: If AC contains encrypted attributes for verifier, decryption MUST not fail | shall | 7.1 |
| R12 | Proxy extension MUST be critical | shall | 7.2 |

## Normative Annexes (Condensed)
- **Appendix A: Object Identifiers**: Lists all OIDs defined or imported (id-pkix, id-pe, id-ad, id-at, id-ce, etc.). Conformant implementations MUST support OIDs with arc elements < 2^32, SHOULD be < 2^31. OID string length up to 100 bytes, up to 20 elements. AAs SHOULD NOT issue ACs with OIDs exceeding these limits.
- **Appendix B: ASN.1 Module**: Defines complete ASN.1 module for AttributeCertificate, Holder, Issuer, Validity, Extensions, IetfAttrSyntax, RoleSyntax, Clearance, AAControls, ProxyInfo, etc. The module is normative and must be used for encoding.