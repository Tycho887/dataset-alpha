# ETSI TR 102 044: Electronic Signatures and Infrastructures (ESI); Requirements for role and attribute certificates
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2002-12 | **Type**: Informative (Technical Report)
**Original**: http://www.etsi.org/deliver/etsi_tr/102000_102099/102044/01.01.01_60/tr_102044v010101p.pdf

## Scope (Summary)
This Technical Report identifies a set of requirements to serve as a basis for a subsequent standard on policy requirements for attributes certified by Attribute Authorities or Certification Authorities – either in Public Key Certificates (PKCs) or Attribute Certificates (ACs). It focuses on attributes used in electronic signatures but may also apply to authorization contexts.

## Normative References
- [1] ETSI TS 101 733: Electronic Signature Formats
- [2] ETSI TR 102 041: Signature Policies Report
- [3] Directive 1999/93/EC of the European Parliament and of the Council on a Community framework for electronic signatures
- [4] ISO/IEC 9594-8 (2001): Public-key and attribute certificate frameworks
- [5] IETF RFC 3280: Internet X.509 PKI Certificate and CRL Profile
- [6] IETF RFC 3039: Internet X.509 PKI Qualified Certificates Profile
- [7] ITU-T X.520: Selected attribute types
- [8] IETF RFC 3281: An Internet Attribute Certificate Profile for Authorization
- [9] EN 45013: General criteria for certification bodies operating certification of personnel
- [10] ISO/IEC FDIS 17024 (2002): Conformity assessment – General requirements for bodies operating certification of persons
- [11] EAC/G4: Guidelines on the Application of EN 45013
- [12] ETSI TS 101 862: Qualified certificate profile
- [13] ISO/IEC 9594-6: Selected attribute types

## Definitions and Abbreviations
- **attribute**: information bound to an entity specifying a characteristic (e.g., group membership, role).
- **Attribute Authority (AA)**: authority trusted to create and sign attribute certificates.
- **Attribute Certificate (AC)**: data structure containing attributes for an end-entity, signed by the issuing AA.
- **Attribute Certificate Policy (ACP)**: named set of rules indicating applicability of an AC.
- **Attribute Certification Authority (ACA)**: authority trusted to include attributes in PKCs or ACs.
- **Attribute Issuing Authority (AIA)**: authoritative source of an attribute.
- **Attribute Certificate validity period**: time during which attributes in an AC are deemed valid.
- **Attribute certification period**: time during which ACs for a given attribute will be provided.
- **Attribute Certification Practice Statement (ACPS)**: statement of practices employed by an ACA.
- **Role**: function, position, or status in an organization, society, or relationship.
- **Group membership**: state of being a member of a group.
- **Privilege Management Infrastructure (PMI)**: infrastructure supporting management of privileges in relation to a PKI.
- **Public Key Certificate (PKC)**: data structure containing a public key, signed by the issuing CA.
- **Qualified Certificate (QC)**: PKC conforming to Annex I of Directive 1999/93/EC.

*Abbreviations*: AA, AC, ACA, ACP, ACPS, AIA, ASN.1, CA, EESSI, OID, PKC, PKI, PMI, QC.

## 4 Implications from the Requirements of the Directive
- Directive [3] Art. 2(3) introduces the need to define under which role a signatory acts.
- Annex I(d) allows inclusion of a specific attribute of the signatory in a Qualified Certificate.
- Such attributes may be placed in the `subjectDirectoryAttributes` extension as per RFC 3039 [6].
- Limitations on value or use (Art. 6(3),(4) and Annex I(i),(j)) are placed in `QcEuLimitValue` or `keyUsage`/`extendedKeyUsage`.
- An AC cannot be a QC because it does not contain a public key.
- The QC issuer (CSP) is liable for accuracy of all information at issuance (Art. 6(1)).
- QC public availability requires subject’s consent (Annex II(l), 3rd bullet).
- CSP must verify any specific attributes (Annex II(d)).
- **Shall**: If the CA that issues PKCs also certifies attributes (e.g., via subjectDirectoryAttribute), the Certificate Policy **shall** be enriched with additional attribute certification requirements.
- **Shall**: If an AA issues ACs, it **shall** specify the applicable ACP in every AC.

## 5 European Surveys
### 5.1 Personnel Certification
- Personnel certification bodies under EN 45013 assess subject’s competency; an ACA does **not** assess competency but only verifies entitlement to the attribute.
- **Shall**: The ACA **shall** specify in its ACPS the official information and practices upon which attributes have been issued (no requirement to directly assess competency).

### 5.2 Currently Implemented Attribute Certificate Usage
- Survey of PERMIS project (Bologna, Barcelona/Camerfirma, Salford). Only Camerfirma uses practices to certify attributes.
- Example: for legal entity representatives, public/private documents are required; the ACA verifies documents, not direct capability.

## 6 Various Kinds of Attributes
### 6.1 Group Memberships
- Hierarchical or functional groups.

### 6.2 Roles
- Roles express organizational/functional responsibility (e.g., CEO, Minister).
- Role is stable; management by User Administrator.
- Roles may be assigned independently of individuals.
- Revoking authority may differ from certifying authority.

### 6.3 Other Authorization Information
#### 6.3.1 Proxies
- Subject may sign on behalf of another; delegation may be via an AC issued by AA or directly by delegating person.
- Delegating person may restrict delegated powers (attribute subset, context restrictions).

#### 6.3.2 Capabilities
- In electronic signature context, a capability is the right to use a commitment type under a policy.

## 7 Claimed and Certified Attributes
### 7.1 Claimed Attributes
- Claimant is responsible for assertion; legal consequences if false. Some applications accept claimed attributes.

### 7.2 Certified Attributes
- Certified by ACA based on information from an AIA.
- **Directly certified**: ACA is also AIA.
- **Verified**: ACA is not AIA; attributes must be verified so that ACA has **no reasonable doubt**.
- **Shall**: The ACA **shall** specify in its ACPS the details of official information and practices upon which attributes are verified.
- **Shall**: The ACA **shall** keep a copy of the official information upon which the attribute was verified.

### 7.2.1 The Attribute Issuing Authority
- AIA assesses competence; ACA only verifies entitlement.
- If one organization acts as both ACA and AIA, clear separation of personnel **shall** be maintained.

## 8 Attribute Meaning and Representation
### 8.1 Attribute Meaning
- **Shall**: A clear description of the attribute **shall** be given in readily-understandable terms, and if appropriate the law that defines the attribute **shall** be indicated. There **must** be a way to find the description.

### 8.2 Attribute Representation
- Attribute can be user understandable, machine processable, or both.
- For cross-European equivalence, use OIDs rather than language-dependent strings.

#### 8.2.1 Group Membership
- Carries information about group memberships.

#### 8.2.2 Role
- Role attribute (ISO/IEC 9594-8) has two components: roleAuthority (optional, identifies AIA) and roleName.

## 9 Other Attribute Characteristics
### 9.1 Attribute Life Span
- Three classes: life-lasting, long-lasting, short-lasting.

### 9.2 Attribute Certification Period
- Time period the AA will certify the attribute.

### 9.3 Attribute Certificate Validity Period
- The period during which attributes in an AC are deemed valid; always ≤ attribute certification period.

### 9.4 Attribute Revocation and AC Revocation
- Revocation may be managed (on-line/off-line) or not (ephemeral attributes).
- If revocation is supported, users **shall** test revocation status according to signature policy, unless AC states no revocation information is available.
- Two management approaches: assign validity period equal to life span with revocation; or assign much shorter validity without revocation.
- **Shall**: The AA **shall** indicate in its Policies the conditions to revoke the attributes.

### 9.5 Attribute Privacy
- Attributes that the subject does not want to always disclose **shall** be included only in ACs, not in PKCs.

### 9.6 Ways to Acquire Attributes
- By default (in PKC), upon request (in AC), or from a repository.

### 9.7 Delegable Attributes
- Some attributes may be delegable; right to delegate may be restricted.
- **Shall**: It **shall** always be possible to know who performed the delegation.
- **Shall**: For accountability, the name of the delegating person **shall** be directly or indirectly traceable.

## 10 Placement of Attributes in Certificates
- Attributes can be placed in PKCs or ACs.
- **Recommendation**: Attributes **shall** be included in a PKC only if their life span is **no shorter** than the PKC validity period.
- PKCs natively support attributes via `commonName` (deprecated for role) or `subjectDirectoryAttributes` extension (recommended).
- Use of `Title` in subject field is deprecated.
- ACs are appropriate when attribute lifetime does not match PKC validity or for privacy.

## 11 Attribute Certificates Management
### 11.1 Attribute Verification by the ACA
- For PKCs, verification at registration only; CA must revoke if informed. For ACs, policies may define continuous verification.
- **Shall**: The ACA **shall** specify whether attributes are verified only at initial registration or subsequently checked.

### 11.2 Link with a PKC
- AC links to a PKC via `baseCertificateID` (issuer name + serial number) or `entityName`.
- **Shall**: The AA **shall** ensure that the presented PKC was actually issued to the subscriber.
- If `entityName` is used, the structure does not include CA name; thus cannot be used in open multi-CA environments without extension to include issuer DN.
- **Recommendation**: Only long-term stable information **shall** be placed in the subject DN; temporary info in `subjectAltName`.

### 11.3 AC Revocation Management
- For short validity, revocation may be unnecessary.
- **Shall**: The AA **shall** keep track of all currently valid ACs to know which to revoke.
- **Shall**: If an attribute revocation affects an AC subset, the subscriber **shall** be informed.

### 11.4 AC Acquisition
- Subscriber can obtain a default AC, an attribute set name defined by AA, by subscriber, or by delegating individual.
- **Shall**: The AA **shall** indicate in an ACPS how ACs can be acquired.
- Note: No standard protocol yet; LDAP schema missing.

### 11.5 Attribute Delegation Management
- **Shall**: The subscriber **shall** indicate delegation period and delegate (unambiguous link to certificate).
- **Shall**: The AA **shall** indicate in an ACPS how AC can be delegated and acquired.

## 12 Recommendations
### 12.1 Requirements for ACP
- Every AC can be issued under a different ACP; same AA may support multiple policies but **shall** ensure each grouping is under a coherent set of ACPs.

#### 12.1.1 Requirements for ACAs
- **Shall**: The ACA **shall** keep a copy of the official information collected for attribute verification.
- **Shall**: The ACA **shall** specify in the ACPS the details of official information and practices.
- **Shall**: If the same authority acts as ACA and AIA, ICT skills are required, and the two functions **should** be separated to ensure separation of duties.
- **Shall**: For any attribute, the ACA **shall** specify: (a) description in understandable terms, (b) representation, (c) whether certified by authoritative source or only verified, (d) whether publicly available or restricted, (e) where placed (PKC or AC).

#### 12.1.2 Requirements for AAs
- **Shall**: The AA **shall** indicate whether revocation is supported. If not, that fact **shall** be indicated.
- **Shall**: The AA **shall** indicate for every AC which alternative applies: (a) initial check only, no revocation; (b) initial check only, with revocation; (c) subsequent checking with revocation.
- **Shall**: For any attribute, the AA **shall** specify in the ACPS: (1) attribute certification period; (2) possible validity periods; (3) revocation support, conditions, rules; (4) whether obtainable in subset; (5) whether delegable, and if so how to trace the delegating person and any restrictions.
- **Shall**: The AA **should** inform subscribers and relying parties about the need to check both AC and associated PKC validity.

### 12.2 Definition of Cross-European Roles
- Recommendation to study equivalence of roles across EU.

### 12.3 AC Profile for Electronic Signatures
- Identified enhancements to RFC 3281:
  1. Need for an “Attribute Certificate Policies Extension”.
  2. Unambiguous link between AC and PKC: use `baseCertificateID` (issuer + serial) or possibly an extended `entityName` with issuer DN or Permanent Identifier.
  3. RoleSyntax as defined in X.509 is preferred; restriction to URI is too limiting.
  4. Need a “restrictions extension” for delegation.
  5. Need a “delegating person extension” for audit.
- Conclusion: a new document “Attribute Certificate Profile for Electronic Signatures” is needed.

### 12.4 AC Acquisition Protocol
- Two kinds: on-demand (returned to requestor) or pre-produced in repository (fetched via LDAP with appropriate schema, noting privacy issues).

### 12.5 Criteria for Using PKCs or ACs
- Non-public attributes **shall** be in ACs only.
- Life/long-lasting attributes (≥ PKC validity) may be in PKCs; short-lasting ( < PKC validity) **shall** be in ACs.
- Attributes inserted in PKCs are verified only at issuance; if continued accuracy is needed, use ACs under appropriate policy.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | If a CA certifies attributes via PKC, the Certificate Policy shall be enriched with additional attribute certification requirements. | shall | §4 |
| R2 | If an AA issues ACs, it shall specify the applicable ACP in every AC. | shall | §4 |
| R3 | The ACA shall specify in its ACPS the official information and practices upon which attributes have been issued. | shall | §5.1, §7.2.1, §7.2.3, §12.1.1 |
| R4 | The ACA shall keep a copy of the official information upon which the attribute was verified. | shall | §7.2.3, §12.1.1 |
| R5 | If one organization acts as both ACA and AIA, a clear separation of personnel shall be maintained. | shall | §7.2.1 |
| R6 | A clear description of the attribute shall be given in readily-understandable terms; where appropriate the law shall be indicated. | shall | §8.1 |
| R7 | There must be a way to find the description of the attribute. | must | §8.1 |
| R8 | Users shall test revocation status of ACs unless the AC states no revocation info is available. | shall | §9.4 |
| R9 | The AA shall indicate in its Policies the conditions to revoke the attributes. | shall | §9.4 |
| R10 | Attributes that the subject does not want always to disclose shall be included only in ACs. | shall | §9.5 |
| R11 | It shall always be possible to know who performed a delegation. | shall | §9.7 |
| R12 | For accountability, the delegating person’s name shall be directly or indirectly traceable. | shall | §9.7 |
| R13 | Attributes shall be included in a PKC only if their life span is no shorter than the PKC validity period. | shall (recommendation) | §10 |
| R14 | The AA shall ensure that the presented PKC was actually issued to the subscriber. | shall | §11.2 |
| R15 | The AA shall keep track of all currently valid ACs to know which to revoke. | shall | §11.3 |
| R16 | If an attribute revocation affects an AC subset, the subscriber shall be informed. | shall | §11.3 |
| R17 | The AA shall indicate in an ACPS how ACs can be acquired. | shall | §11.4 |
| R18 | The subscriber shall indicate delegation period and delegate (unambiguous link to certificate). | shall | §11.5 |
| R19 | The AA shall indicate in an ACPS how AC can be delegated and acquired. | shall | §11.5 |
| R20 | The ACA shall specify for any attribute: (a) description, (b) representation, (c) certified or verified, (d) public/private, (e) placement (PKC or AC). | shall | §12.1.1 |
| R21 | The AA shall indicate whether revocation is supported and, per AC, which alternative (initial/no revoc, initial/revoc, subsequent/revoc). | shall | §12.1.2 |
| R22 | The AA shall specify in the ACPS: attribute certification period, validity periods, revocation conditions, subset availability, delegation information. | shall | §12.1.2 |
| R23 | The AA should inform subscribers and relying parties about the need to check AC and associated PKC validity. | should | §12.1.2 |
| R24 | Non-public attributes shall be included only in ACs. | shall | §12.5 |
| R25 | If an attribute expires before the related PKC, it shall not be placed in the PKC but in an AC. | shall | §12.5 |

## Informative Annexes (Condensed)
- **Annex A: Attribute syntax in ASN.1** – Repeats definitions from IETF RFC 3280, RFC 3281, and X.520 for Attribute, Group attribute (IetfAttrSyntax), Member attribute, Role attribute (RoleSyntax), and Role Occupant attribute. Provides OIDs and constraints (e.g., multi-valued IetfAttrSyntax must use same choice of value syntax).
- **Annex B: Guidelines for the certification of roles in subscription certificates** – Excerpt from the Italian Assocertificatori document. Describes a solution for encoding roles in the `Description` field of the Subject DN using a natural language string and a numeric code from a Unique Role Table. Specifies use of Organization, Organization Unit, and Locality fields to identify the represented entity. Outlines organizational processes for verification, liability, and practice statements. Includes examples and the initial role table (e.g., Director:2.10.3.1). The solution is compatible with IETF RFC 3039 qualified certificates by placing the role data in the `subjectDirectoryAttributes` extension.
- **Annex C: Bibliography** – Lists the study “Requirements for CSPs issuing Attribute Certificates” (Thomas Hueske, Christian Tobias, 2000-09-18).