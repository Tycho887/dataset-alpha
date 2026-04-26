# RFC 4985: Internet X.509 Public Key Infrastructure Subject Alternative Name for Expression of Service Name
**Source**: IETF | **Version**: Standards Track | **Date**: August 2007 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4985

## Scope (Summary)
This document defines a new name form (SRVName) for inclusion in the `otherName` field of an X.509 Subject Alternative Name extension, enabling a certificate subject to be associated with the service name and domain name components of a DNS Service Resource Record (SRV RR) as defined in RFC 2782 [N3]. It specifies encoding, internationalization, and name constraint matching rules.

## Normative References
- [N1] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [N2] Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- [N3] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [N4] Mockapetris, P., "DOMAIN NAMES - CONCEPTS AND FACILITIES", STD 13, RFC 1034, November 1987.
- [N5] Reynolds, J., "Assigned Numbers: RFC 1700 is Replaced by an On-line Database", RFC 3232, January 2002.
- [N6] Faltstrom, P., Hoffman, P., and A. Costello, "Internationalizing Domain Names in Applications (IDNA)", RFC 3490, March 2003.

## Definitions and Abbreviations
- **id-on-dnsSRV**: OBJECT IDENTIFIER ::= { id-on 7 } = { iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) 8 7 }.
- **SRVName**: IA5String (SIZE (1..MAX)), containing `_Service.Name`.
- **Service**: Symbolic name of the desired service as defined in Assigned Numbers [N5] or locally, with underscore (`_`) prepended. Case insensitive.
- **Name**: DNS domain name of the domain where the service is located. For IDNs, encoded in ASCII Compatible Encoding (ACE).
- **ACE**: ASCII Compatible Encoding as per RFC 3490 [N6].

## Normative Content

### 2. Name Definitions
- **`id-on-dnsSRV`**: `{ id-on 7 }`
- **SRVName syntax**: `_Service.Name`
- **Requirement**: The SRVName, if present, MUST contain a service name and a domain name in the form `_Service.Name`. The content MUST be consistent with RFC 2782 [N3].
- **Service component**: If Assigned Numbers [N5] names the service indicated, that name is the only name allowed. Case insensitive.
- **Name component**: DNS domain name. If IDN, encoding in ASCII form SHALL be done as defined in §3.
- **Protocol component omitted**: The `_Proto` component from SRV RR is not included. Benefits: one certificate for multiple protocol alternatives; simpler name constraints.
- **Conditions for use**: A present SRVName MUST NOT be used to identify a host unless (a) the security protocol specifies this name form and the identified service has a defined service name per RFC 2782, or (b) use is configured by local policy.

### 3. Internationalized Domain Names
- **Encoding**: Conforming implementations MUST convert internationalized domain names to ACE as specified in §4 of RFC 3490 [N6], with clarifications:
  - Step 1: domain name SHALL be considered a "stored string" (AllowUnassigned flag SHALL NOT be set);
  - Step 3: set flag "UseSTD3ASCIIRules";
  - Step 4: process each label with the "ToASCII" operation;
  - Step 5: change all label separators to U+002E (full stop).
- **Comparison**: For equality, MUST perform case-insensitive exact match on the entire domain name. For name constraints, MUST perform case-insensitive exact match on a label-by-label basis.
- **Display**: Implementations SHOULD convert IDNs to Unicode before display, using §4 of RFC 3490 with clarifications:
  - Step 1: stored string (AllowUnassigned NOT set);
  - Step 3: set UseSTD3ASCIIRules;
  - Step 4: process each label with the "ToUnicode" operation;
  - Skip step 5.
- **Space allowance**: Implementations MUST allow for increased space for IDNs (e.g., "xn--" prefix).

### 4. Name Constraints Matching Rules
- **Applicability**: Name constraining, as per RFC 3280 [N2], MAY be applied to the SRVName by adding name restriction in the name constraints extension in the form of an SRVName.
- **Restriction forms**: Expressed as:
  - Complete SRVName (e.g., `_mail.example.com`)
  - Just a service name (`_mail`)
  - Just a DNS name (`example.com`)
- **Service name matching**: If a service name is included in the restriction, only SRVNames with that service name match. If the restriction has an absent service name, any SRVName that matches the domain part satisfies.
- **DNS name matching**: DNS name restrictions are expressed as `host.example.com`. Any DNS name constructed by adding subdomains to the left-hand side satisfies. For example, `www.host.example.com` satisfies `host.example.com`; `1host.example.com` does not.
- **Examples**:
  - Restriction `example.com`: matches `_mail.example.com`, `_ntp.example.com`; does not match `_mail.1example.com`.
  - Restriction `_mail`: matches `_mail.example.com`, `_mail.1example.com`; does not match `_ntp.example.com`.
  - Restriction `_mail.example.com`: matches `_mail.example.com`, `_mail.1.example.com`; does not match `_mail.1example.com` or `_ntp.example.com`.

### 5. Security Considerations
- **Revocation**: Implementers should be aware of the need to revoke old certificates that no longer reflect current service assignments and ensure all issued certificates are up to date.
- **When used with SRV RR**: All security considerations of RFC 2782 [N3] apply.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | SRVName MUST contain `_Service.Name` consistent with RFC 2782 | MUST | §2 |
| R2 | If Assigned Numbers names the service, that name is the only name allowed in the service component | MUST | §2 |
| R3 | IDN domain names SHALL be encoded in ACE per RFC 3490 §4 with specified clarifications | SHALL | §3 |
| R4 | Conforming implementations MUST convert IDNs to ACE before storage in Name part | MUST | §3 |
| R5 | When comparing DNS names for equality, perform case-insensitive exact match on entire domain name | MUST | §3 |
| R6 | When evaluating name constraints, perform case-insensitive exact match label-by-label | MUST | §3 |
| R7 | Implementations SHOULD convert IDNs to Unicode before display per RFC 3490 with specified clarifications | SHOULD | §3 |
| R8 | A present SRVName MUST NOT be used unless the security protocol specifies this name form (and service is defined) or local policy configures it | MUST | §2 |
| R9 | Name constraints MAY be applied to SRVName using restrictions expressed as complete SRVName, just service name, or just DNS name | MAY | §4 |
| R10 | If restriction includes service name, only SRVNames with that service name match (implicit) | (conditional) | §4 |
| R11 | DNS name restriction: any DNS name constructed by adding subdomains to left-hand side satisfies | (method) | §4 |

## Informative Annexes (Condensed)
- **Appendix A. ASN.1 Syntax**: Provides two ASN.1 modules (1988 and 1993 variants) defining the SRVName type and the `id-on-dnsSRV` OID. The 1988 module (`PKIXServiceNameSAN88`) is normative in case of discrepancies between the modules. Both modules define `SRVName ::= IA5String (SIZE (1..MAX))` and import `id-pkix` from RFC 3280.