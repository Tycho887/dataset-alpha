# ETSI TS 101 862 V1.3.3: Qualified Certificate profile
**Source**: ETSI | **Version**: V1.3.3 | **Date**: 2006-01 | **Type**: Technical Specification (Normative)
**Original**: http://www.etsi.org (TS 101 862)

## Scope (Summary)
Defines a profile for Qualified Certificates based on RFC 3739, for issuers complying with Annex I and II of the European Electronic Signature Directive 1999/93/EC. This profile explicitly aligns with the Directive’s definition of "Qualified Certificate", whereas RFC 3739 uses the term in a universal context.

## Normative References
- [1] Directive 1999/93/EC of the European Parliament and of the Council of 13 December 1999 on a Community framework for electronic signatures.
- [2] ITU-T Recommendation X.509/ISO/IEC 9594-8: "Information technology - Open Systems Interconnection - The Directory: Public-key and attribute certificate frameworks".
- [3] IETF RFC 3280: "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile".
- [4] IETF RFC 3739: "Internet X.509 Public Key Infrastructure: Qualified Certificates Profile".
- [5] ISO/IEC 8824-1/ITU-T Recommendation X.680: "Information technology - Abstract Syntax Notation One (ASN.1): Specification of basic notation".
- [6] ISO/IEC 8824-2/ITU-T Recommendation X.681: "Information technology - Abstract Syntax Notation One (ASN.1): Information object specification".
- [7] ISO/IEC 8824-3/ITU-T Recommendation X.682: "Information technology - Abstract Syntax Notation One (ASN.1): Constraint specification".
- [8] ISO/IEC 8824-4/ITU-T Recommendation X.683: "Information technology - Abstract Syntax Notation One (ASN.1): Parameterization of ASN.1 specifications".
- [9] ISO 4217: "Codes for the representation of currencies and funds".

## Definitions and Abbreviations
- **CA** – Certification Authority
- **OID** – Object Identifier
- **SSCD** – Secure Signature Creation Device

## 4 Document Structure
- Clause 5 (core): Amendments to RFC 3739 [4].
- Annex A (informative): Relationship with the Directive.
- Annex B (normative): ASN.1 declarations.

## 5 Certificate Profile
Based on RFC 3739 [4], which in turn is based on RFC 3280 [3] and X.509 v3 [2]. Implementers **REQUIRED** to consult RFC 3739. In case of discrepancy, this document is normative.

### 5.1 Issuer Field
- The `issuer` field **MUST** contain a country name in the `countryName` attribute. The country **SHALL** be the country in which the issuer is established.

### 5.2 Qualified Certificate Statements
When the `qCStatements` extension is marked critical, all statements in it are regarded as critical.

#### 5.2.1 Statement claiming that the certificate is a Qualified Certificate
- **esi4-qcStatement-1**: Identifier OID `id-etsi-qcs-QcCompliance` (1.0.4.0.1862.1.1). Statement by the CA that the certificate is issued as a Qualified Certificate according to Annex I and II of the Directive, as implemented in the law of the country specified in the issuer field.
- ASN.1:
  ```
  esi4-qcStatement-1 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-qcs-QcCompliance }
  id-etsi-qcs-QcCompliance OBJECT IDENTIFIER ::= { id-etsi-qcs 1 }
  ```

#### 5.2.2 Statement regarding limits on the value of transactions (optional)
- **esi4-qcStatement-2**: Identifier OID `id-etsi-qcs-QcLimitValue` (1.0.4.0.1862.1.2). Syntax `MonetaryValue` (currency per ISO 4217, amount, exponent). Value = amount * 10^exponent. Recommended alphabetic currency code.
- ASN.1:
  ```
  esi4-qcStatement-2 QC-STATEMENT ::= { SYNTAX QcEuLimitValue IDENTIFIED BY id-etsi-qcs-QcLimitValue }
  QcEuLimitValue ::= MonetaryValue
  MonetaryValue ::= SEQUENCE { currency Iso4217CurrencyCode, amount INTEGER, exponent INTEGER }
  Iso4217CurrencyCode ::= CHOICE { alphabetic PrintableString (SIZE (3)), numeric INTEGER (1..999) }
  id-etsi-qcs-QcLimitValue OBJECT IDENTIFIER ::= { id-etsi-qcs 2 }
  ```

#### 5.2.3 Statement indicating the duration of the retention period of material information (optional)
- **esi4-qcStatement-3**: Identifier OID `id-etsi-qcs-QcRetentionPeriod` (1.0.4.0.1862.1.3). Syntax `INTEGER` (number of years after certificate expiry). The issuer guarantees archiving of material information for that period.
- ASN.1:
  ```
  esi4-qcStatement-3 QC-STATEMENT ::= { SYNTAX QcEuRetentionPeriod IDENTIFIED BY id-etsi-qcs-QcRetentionPeriod }
  QcEuRetentionPeriod ::= INTEGER
  id-etsi-qcs-QcRetentionPeriod OBJECT IDENTIFIER ::= { id-etsi-qcs 3 }
  ```

#### 5.2.4 Statement claiming that the private key related to the certified public key resides in a Secure Signature Creation Device (SSCD) (optional)
- **esi4-qcStatement-4**: Identifier OID `id-etsi-qcs-QcSSCD` (1.0.4.0.1862.1.4). Statement by the CA that the private key is protected according to Annex III of the Directive.
- ASN.1:
  ```
  esi4-qcStatement-4 QC-STATEMENT ::= { IDENTIFIED BY id-etsi-qcs-QcSSCD }
  id-etsi-qcs-QcSSCD OBJECT IDENTIFIER ::= { id-etsi-qcs 4 }
  ```

### 5.3 Qualified Certificate Indication
Two techniques to declare a certificate as a Qualified Certificate:
1) By identifying a certificate policy in the Certificate Policies extension (RFC 3280) expressing compliance with Annex I and II.
2) By including a Qualified Certificate Statements extension with `esi4-qcStatement-1` (clause 5.2.1).

- **SHOULD** include a policy according to 1).
- Certificates issued until June 30, 2005 **SHOULD** contain a statement according to 2).
- Certificates issued after June 30, 2005 **SHALL** contain a statement according to 2).
- **SHALL** in any case use at least one of the techniques.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Issuer field MUST contain countryName of establishment country. | shall | 5.1 |
| R2 | When qCStatements extension is critical, all statements are critical. | shall | 5.2 |
| R3 | Qualified Certificate statement esi4-qcStatement-1 OID id-etsi-qcs-QcCompliance. | shall (if used) | 5.2.1 |
| R4 | Limit value statement esi4-qcStatement-2 syntax MonetaryValue (ISO 4217). | shall (if used) | 5.2.2 |
| R5 | Retention period statement esi4-qcStatement-3 syntax INTEGER (years). | shall (if used) | 5.2.3 |
| R6 | SSCD statement esi4-qcStatement-4 OID id-etsi-qcs-QcSSCD. | shall (if used) | 5.2.4 |
| R7 | Certificates SHOULD include a policy per technique 1. | should | 5.3 |
| R8 | Certificates issued after June 30, 2005 SHALL include statement per technique 2. | shall | 5.3 |
| R9 | Certificates SHALL use at least one of the techniques. | shall | 5.3 |

## Informative Annexes (Condensed)
- **Annex A (Relationship with the Directive)**: Maps requirements of Annex I and II of the Directive 1999/93/EC to implementations defined in this profile and underlying standards (RFC 3739, RFC 3280, X.509). Annex I requirements (a)–(j) are met via certificate policies, issuer field, subject field, public key, validity, serial number, signature, extensions, and limit value statement (clause 5.2.2). Annex II requirements are supported by CRL distribution points, authority information access, retention period statement (clause 5.2.3), and certificate policy qualifier CPSuri.

- **Annex B (Normative: ASN.1 declarations)**: Contains the full ASN.1 module defining the QC-STATEMENT structures and OIDs for all four statements. The module imports `QC-STATEMENT` and `qcStatement-1` from `PKIXqualified97`. All OIDs are under the `id-etsi-qcs` arc (1.0.4.0.1862.1). The `SupportedStatements` set includes `qcStatement-1` and the four statements defined herein.

  ```asn1
  -- Full module (simplified for brevity)
  ETSIQCprofile { itu-t(0) identified-organization(4) etsi(0) id-qc-profile(1862) id-mod(0) id-mod-qc-profile-2(2) }
  DEFINITIONS EXPLICIT TAGS ::= BEGIN
  IMPORTS QC-STATEMENT, qcStatement-1 FROM PKIXqualified97 ...;
  -- Statements as per clauses 5.2.1–5.2.4
  -- OID tree:
  id-etsi-qcs OBJECT IDENTIFIER ::= { itu-t(0) identified-organization(4) etsi(0) id-qc-profile(1862) 1 }
  id-etsi-qcs-QcCompliance OBJECT IDENTIFIER ::= { id-etsi-qcs 1 }
  id-etsi-qcs-QcLimitValue OBJECT IDENTIFIER ::= { id-etsi-qcs 2 }
  id-etsi-qcs-QcRetentionPeriod OBJECT IDENTIFIER ::= { id-etsi-qcs 3 }
  id-etsi-qcs-QcSSCD OBJECT IDENTIFIER ::= { id-etsi-qcs 4 }
  SupportedStatements QC-STATEMENT ::= { qcStatement-1 | esi4-qcStatement-1 | esi4-qcStatement-2 | esi4-qcStatement-3 | esi4-qcStatement-4, ... }
  END
  ```