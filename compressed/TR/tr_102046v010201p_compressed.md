# ETSI TR 102 046 V1.2.1: Electronic Signatures and Infrastructures (ESI); Maintenance report
**Source**: ETSI TC ESI | **Version**: V1.2.1 | **Date**: 2004-06 | **Type**: Informative (Technical Report)  
**Original**: http://www.etsi.org

## Scope (Summary)
This Technical Report records comments and issues raised with ETSI TC ESI on Technical Specifications and Technical Reports for Electronic Signatures and Infrastructures, and in some cases proposes resolutions. Comments may lead to future revisions of the specifications.

## Normative References
- [1] ETSI TR 102 317: Process and tool for maintenance of ETSI deliverables.
- [2] ETSI TS 101 456: Policy requirements for CAs issuing qualified certificates.
- [3] ETSI TS 102 042: Policy requirements for CAs issuing public key certificates.
- [4] ETSI TS 101 733: Electronic signature formats.
- [5] ETSI TS 101 903: XML Advanced Electronic Signatures (XAdES).
- [6] ETSI TS 101 861: Time stamping profile.
- [7] ETSI TS 101 862: Qualified certificate profile.
- [8] ETSI TS 102 023: Policy requirements for time-stamping authorities.
- [9] ETSI TR 102 038: XML format for signature policies.
- [10] ETSI TR 102 041: Signature Policies Report.
- [11] Directive 1999/93/EC (Electronic Signatures Directive).
- [12] CWA 14167-1: System security requirements for trustworthy systems managing certificates.
- [13] CWA 14170: Security requirements for signature creation applications.
- [14] CWA 14167-2: Cryptographic module for CSP signing operations.
- [15] CWA 14168: Secure signature-creation devices EAL 4.
- [16] CWA 14169: Secure Signature-Creation devices EAL 4+.
- [17] ISO/IEC 15408 (all parts): Evaluation criteria for IT security.
- [18] ISO/TS 17090-1: Health informatics PKI – Framework and overview.
- [19] ISO/TS 17090-2: Health informatics PKI – Certificate profile.
- [20] ISO/TS 17090-3: Health informatics PKI – Policy management of CA.
- [21] ISO/IEC 17799: Code of practice for information security management.
- [22] ETSI TS 102 158: Policy requirements for CSPs issuing attribute certificates.
- [23] Council Directive 93/13/EEC: Unfair terms in consumer contracts.
- [24] ITU-T X.520: Selected attribute types.
- [25] IETF RFC 2247: Using Domains in LDAP/X.500 Distinguished Names.
- [26] IETF RFC 2459: Internet X.509 PKI Certificate and CRL Profile (Obsoleted by RFC 3280).
- [27] IETF RFC 2526: Reserved IPv6 Subnet Anycast Addresses.
- [28] IETF RFC 2527: Certificate Policy and Certification Practices Framework (Obsoleted by RFC 3647).
- [29] IETF RFC 3039: Internet X.509 PKI Qualified Certificates Profile.
- [30] IETF RFC 3161: Internet X.509 PKI Time-Stamp Protocol (TSP).
- [31] IETF RFC 3280: Internet X.509 PKI Certificate and CRL Profile.
- [32] FIPS PUB 140-2: Security Requirements for Cryptographic Modules (Supersedes FIPS PUB 140-1).

## Definitions and Abbreviations
Definitions and abbreviations as given in TS 101 456 [2], TS 102 042 [3], TS 101 733 [4], TS 101 903 [5], TS 101 861 [6], TS 101 862 [7], TS 102 023 [8], TR 102 038 [9] and TR 102 041 [10] apply.

## Role and Structure (Clause 4)
The document tracks contributions, organizes them under relevant headings, and processes comments to identify resolutions. Clause 5 contains the structured comments (elementary comments with metadata). Annex A contains original contributions in their original format.

## Comments (Clause 5)

### 5.1 TS 101 456 - Qualified certificate policy
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS101456-001 | 7.4.8 | technical | Add subsection "System backup and recovery" – restore must be under dual control. | not yet processed |
| TS101456-002 | 7.4.3 g) | technical | Auditors should only view, not maintain, audit logs. | not yet processed |
| TS101456-003 | 2 | editorial | Update FIPS PUB 140-1 reference to FIPS PUB 140-2. | not yet processed |
| TS101456-004 | 4.1 (1st para) | editorial | Rephrase: "Certification Authority has overall responsibility ... its private key is used to sign qualified certificates." | not yet processed |
| TS101456-005 | 4.1 (2nd para) | editorial | Change "key used to generate" to "private key used to sign". | not yet processed |
| TS101456-006 | 4.2 | technical | Dissemination service: change "disseminates" to "makes available" for relying parties. | not yet processed |
| TS101456-007 | 6.2 | technical | Restructure subscriber obligations: add awareness for subject, direct notification possibilities. | not yet processed |
| TS101456-008 | 7.2.1 | technical | Reference FIPS PUB 140-1 or 140-2 level 3. | not yet processed |
| TS101456-009 | 7.2.2 | technical | Reference FIPS PUB 140-1 or 140-2. | not yet processed |
| TS101456-010 | 7.2.9 | technical | Specify separation of activation data and delivery of SSCD. | not yet processed |
| TS101456-011 | 7.3.1 | technical | Move subscriber contact info to obligations; retention period per national law. | not yet processed |
| TS101456-012 | 7.3.3 | technical | Private key securely passed to subject, not SSCD. | not yet processed |
| TS101456-013 | 7.3.6 | technical | Add requirement: CRL shall be signed by CA or designated authority. | not yet processed |
| TS101456-014 | 7.4.4 | technical | Physical protection applies to subject device preparation, not provision. | not yet processed |
| TS101456-015 | 7.4.5 | technical | Add media lifecycle management to prevent obsolescence. | not yet processed |
| TS101456-016 | 7.4.8 | technical | In case of compromise, inform subscribers (who inform subjects). | not yet processed |
| TS101456-017 | 7.4.9 | technical | In CA termination, inform subscribers who inform subjects. | not yet processed |
| TS101456-018 | 7.4.11 | technical | Record registration information; retention per national law. | not yet processed |
| TS101456-019 | 4.3 | technical | Add cross-certification relations? | resolution: no change (cross certs not addressed) |
| TS101456-020 | 7.2.4 | technical | Legal monitor for wireless? | resolution: no change (signing keys only) |
| TS101456-021 | 7.2 | technical | Add CA key update operation? | resolution: no change (covered by 7.2.1/7.2.2) |
| TS101456-022 | – | technical | Discuss conflicts from multiple certificates per key pair. | not yet processed |
| TS101456-023 | – | technical | General: TS 101 456 is too technical, redundant. | not yet processed |
| TS101456-024 | – | technical | Mandate formal assessment before issuing first qualified certificate. | not yet processed |
| TS101456-025 | 7.2.9 | technical | Add note recommending CA advise subscribers on SSCD environment (CWA 14170). | not yet processed |
| TS101456-026 | 7.2.5 | technical | Change "shall not use same key" to "shall not use if violates security". Alternative: delete clause. | not yet processed |
| TS101456-027 | 7.4.7 | technical | Explicitly reference CWA 14167-1 in note. | not yet processed |
| TS101456-028 | 8 | technical | Clarify when new certification policy is needed. | not yet processed |
| TS101456-029 | Introduction | technical | Add paragraph about attributes in PKCs. | not yet processed |
| TS101456-030 | Introduction | technical | Update paragraph to mention attribute inclusion per Directive Annex I d). | not yet processed |
| TS101456-031 | 2 | technical | Add reference to Council Directive 93/13/EEC. | not yet processed |
| TS101456-032 | 3.1 | technical | Add definitions for attribute, Attribute Granting Authority, role. | not yet processed |
| TS101456-033 | 4.1 | technical | Fix reference to clause 4.2; add paragraphs on qualifications/attributes. | not yet processed |
| TS101456-034 | 4.3.4 | technical | Modify terms and conditions to comply with Directive 93/13/EEC. | not yet processed |
| TS101456-035 | 4.5 (new) | technical | New clause: Certified attributes – verification required. | not yet processed |
| TS101456-036 | 4.6 (new) | technical | New clause: Attribute semantics – standard or local definition. | not yet processed |
| TS101456-037 | 6.3 (new) | technical | New clause: Subject obligations – use PKC as specified, notify inaccuracies. | not yet processed |
| TS101456-038 | 7.3.1 | technical | Replace c) to include time of registration. | not yet processed |
| TS101456-039 | 7.3.1 | technical | Add l) to o) on attribute verification, recording, consent. | not yet processed |
| TS101456-040 | 7.3.2 | technical | Add Attribute Registration clause (a-d) with verification and recording. | not yet processed |
| TS101456-041 | 7.3.4 | technical | Add requirements for attribute description, verification procedures, representation. | not yet processed |
| TS101456-042 | Annex E | technical | Add references to ISO/TS 17090-1, -2, -3. | not yet processed |
| TS101456-043 | – | technical | Comparison with Federal PKI: some areas "missing" in QCP. | not yet processed |
| TS101456-044 | – | technical | FPKI: revoked cert info remains until certificate expires. | not yet processed |
| TS101456-045 | – | technical | FPKI: all CAs should issue CRLs regardless of other validation. | not yet processed |
| TS101456-046 | – | technical | FPKI: CRL issuance at least daily; within 18h for compromise. | not yet processed |
| TS101456-047 | – | technical | FPKI: audit logs reviewed at least every 2 months. | not yet processed |
| TS101456-048 | – | technical | FPKI: audit processes at startup and shutdown. | not yet processed |
| TS101456-049 | – | technical | FPKI: routine self-assessments. | not yet processed |
| TS101456-050 | – | technical | FPKI: full backups periodically, off-site at least weekly. | not yet processed |
| TS101456-051 | – | technical | FPKI: administrative/disciplinary actions for unauthorized actions. | not yet processed |
| TS101456-052 | – | technical | FPKI: documentation of personnel training. | not yet processed |
| TS101456-053 | 7.2.2 b) | technical | CA key export protection can use threshold secret sharing. | not yet processed |
| TS101456-054 | Annex D | technical | Correct cross-reference inconsistencies between RFC 2527 and TS 101 456. | not yet processed |

### 5.2 TS 101 733 - ES electronic signature formats
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS101733-001 | 2 | editorial | Update RFC references (2459 to 3280). | already applied |
| TS101733-002 | – | technical | Signing Time optional? | already applied |
| TS101733-003 | – | technical | Time-mark concept for TSA compromise issues. | no change |
| TS101733-004 | – | technical | Invalidity Date extension may invalidate long-term formats. | no change |
| TS101733-005 | – | technical | Need better specification of verification processes. | no change |
| TS101733-006 | – | technical | Need good practices document for formats. | no change |
| TS101733-007 | – | technical | Relationship between Certificate Policy rules and Signature Policy rules. | no change |
| TS101733-008 | – | technical | Make SignaturePolicyID optional without NULL. | already applied |
| TS101733-009 | – | technical | Make SigningTime optional. | already applied |
| TS101733-010 | – | technical | Generalize time-mark concept. | no change |
| TS101733-011 | – | technical | ES as minimum mandatory format. | already applied |
| TS101733-012 | – | technical | Signature policy: mandating minimum format for specific application. | no change |
| TS101733-013 | – | editorial | Better separation of mandatory and optional formats. | already applied |
| TS101733-014 | – | editorial | Move signature policy definitions out of TS 101 733 into separate doc. | already applied |
| TS101733-015 | – | technical | Add roadmap document for EESSI deliverables. | no change |
| TS101733-016 | – | technical | Add non-normative document describing whole model. | no change |
| TS101733-017 | – | technical | Add document on hand-written and electronic signatures interoperability. | no change |
| TS101733-018 | – | technical | Rationale on signature policy integration; comments on policy reference, content, protection, data structure, interoperability with XACML. | no change |
| TS101733-019 | 5.4.2 | editorial | "OPTIONAL" keyword missing for OtherRevVals. | already applied |
| TS101733-020 | 4.4 | technical | Timestamps in ES-X Types 1 and 2 unnecessary; ES-X-L sufficient. | no change |
| TS101733-021 | 8.9.1 | technical | Make SignaturePolicyIdentifier optional; allow dynamic policy referencing. | already applied |
| TS101733-022 | 11.1 | technical | Need signature of signature policy itself, not just hash. | no change |
| TS101733-023 | 11.11 | technical | Concrete specification of extension instances needed. | no change |
| TS101733-024 | 5.4.2 | editorial | "CRI Information" should be "CRL Information". | already applied |
| TS101733-025 | 5.4.5/5.4.7 | editorial | Identical clause titles "Timestamping for long life of signature". | in process |
| TS101733-026 | 10.4 | technical | Archive timestamp definition revised. | already applied |

### 5.3 TS 101 861 - Time stamping profile
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS101861-001 | 5.1.2 | editorial | Add "One of" to sentence with "must". | in process |
| TS101861-002 | 5.2.3 | editorial | Add "One of" to sentence with "must". | in process |
| TS101861-003 | – | technical | Profile appropriate for common use. | no change |
| TS101861-004 | 5.2.1 | technical | genTime precision: "one second or better" rather than limited to one second. | not yet processed |
| TS101861-005 | 5.2.1 | technical | Allow ordering parameter; requirement is not to mandate ordering. | not yet processed |
| TS101861-006 | 6 | technical | Store-and-forward support not appropriate; change to only one online protocol. | not yet processed |
| TS101861-007 | 7.1.1 | technical | Allow algorithm parameters to be absent; accept SHA-1 with absent parameters. | not yet processed |

### 5.4 TS 101 862 - Qualified certificate profile
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS101862-001 | 2 | editorial | Update RFC 2459 to RFC 3280. | applied |
| TS101862-002 | 3.1.1/4.1 | technical | Add organizationName attribute and serialNumber for CA identification. | no change (covered by TS 102 280) |
| TS101862-003 | 4.2.1 | technical | Recommend dateOfBirth, placeOfBirth, gender, countryOfCitizenship. | no change (covered by TS 102 280) |
| TS101862-004 | 4.3.1 | technical | Pseudonym MUST be in pseudonym attribute, not commonName. | no change (covered by TS 102 280) |
| TS101862-005 | 4.3.2 | technical | serialNumber attribute mandatory; include government/civil authority identifier. | no change (covered by TS 102 280) |
| TS101862-006 | 4.4 | technical | nonRepudiation bit set exclusively; keyUsage extension marked critical. | no change (covered by TS 102 280) |
| TS101862-007 | – | technical | Need a CRL profile. | no change (to be addressed) |
| TS101862-008 | – | technical | Allow domainComponent attribute for country of supervision. | no change (covered by TS 102 280) |
| TS101862-009 | – | technical | Add QCstatement equivalent to "QCP public + SSCD". | applied |

### 5.5 TS 101 903 - XML advanced electronic signatures (XAdES)
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS101903-001 | – | technical | Detailed rationale on signature policy; comments on policy reference, content, protection, data structure, interoperability. | no change |
| TS101903-002 | – | technical | XAdES-X unnecessary when XAdES-X-L exists. | no change |
| TS101903-003 | – | technical | Investigate interoperability with SAML, XACML, WS-Security. | no change |
| TS101903-004 | – | technical | Promote XAdES interoperability testing; fix schema errors. | no change |
| TS101903-005 | 7.6.2 | technical | Clarify content of EncapsulatedOCSPValue: should be full OCSPResponse. | not yet processed |
| TS101903-006 | TimeStampType | technical | Redefine TimeStampType to use ID-list and canonicalization; problems with HashDataInfo. | not yet processed |
| TS101903-007 | 7.7.1 | technical | ArchiveTimeStamp includes SignedProperties twice; add xsd:ID attributes. | not yet processed |
| TS101903-008 | various | technical | Replace "must" with RFC 2119 capitalization (MUST, SHOULD, etc.). | not yet processed |
| TS101903-009 | 6.2 | technical | Mandatory Target attribute MUST refer to ds:Signature Id. | not yet processed |
| TS101903-010 | 7.1, 7.2.8 | technical | Mandate DER encoding for ASN.1 elements. | not yet processed |
| TS101903-011 | – | technical | Include Trust Status Lists (TSL) in future versions. | not yet processed |
| TS101903-012 | 7.2.2 | technical | Move sentence about attribute certificates to clause 7.2.8. | not yet processed |
| TS101903-013 | – | technical | Allow archival versions 'references only', 'values only', 'mixed'. | not yet processed |
| TS101903-014 | – | technical | Allow XAdES-A without mandatory SignedProperties. | not yet processed |
| TS101903-015 | – | technical | Fix AnyType definition to allow content without schema (add processContents="lax"). | not yet processed |
| TS101903-016 | – | technical | Add URI attribute to CertID to point to archived certificate. | not yet processed |
| TS101903-017 | – | technical | Fix schema to be compatible with .NET validating parser. | not yet processed |
| TS101903-018 | – | technical | Add missing import statement for XMLDSig schema. | not yet processed |
| TS101903-019 | – | technical | Use ref to ds:Transforms instead of local element. | not yet processed |
| TS101903-020 | – | technical | Fix examples in non-normative annex D. | not yet processed |
| TS101903-021 | 7.2.5 | technical | Clarify DataObjectFormat: applies to one object, not objects; use RFC 2119. | not yet processed |
| TS101903-022 | 7.6.1 | technical | Certificates in ds:KeyInfo may not be archived; suggest inclusion in CertificateValues or time-stamp ds:KeyInfo. | not yet processed |
| TS101903-023 | 7.4.1 | technical | Remove "optionally" because schema mandates issuer and serial number. | not yet processed |

### 5.6 TS 102 023 - Time stamping policy
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS102023-001 | Introduction | editorial | Grammar corrections. | not yet processed |
| TS102023-002 | 4.3 | editorial | Grammar correction. | not yet processed |
| TS102023-003 | 4.4.3 | editorial | "time-stamp" consistency. | not yet processed |
| TS102023-004 | 7 | editorial | "those objectives" typo. | not yet processed |
| TS102023-005 | 1 | technical | Reword scope to clarify TSA is synchronized with UTC. | not yet processed |
| TS102023-006 | 2 | technical | Update FIPS PUB 140-1 to 140-2. | not yet processed |
| TS102023-007 | 6.1.1 | technical | "time-stamp token" instead of "time-stamp". | not yet processed |
| TS102023-008 | 6.2 | technical | Rephrase subscriber verification to check digital signature validity. | not yet processed |
| TS102023-009 | 6.3 | technical | Rephrase relying party verification: check digital signature validity. | not yet processed |
| TS102023-010 | 7.1.2 d), j) | technical | Correct references and wording. | not yet processed |
| TS102023-011 | 7.2.1 | technical | Reference FIPS PUB 140-1 or 140-2. | not yet processed |
| TS102023-012 | 7.2.2 | technical | Reference FIPS PUB 140-1 or 140-2. | not yet processed |
| TS102023-013 | 7.2.4 | technical | Reword note: records retention period based on signature verification key. | not yet processed |
| TS102023-014 | 7.2.5 | technical | Add substitution other than expiry; reject if key not valid. | not yet processed |
| TS102023-015 | 7.2.6 | technical | Title: "used to sign time-stamp tokens". | not yet processed |
| TS102023-016 | 7.3.1 | technical | "requests/responses of time-stamp tokens"; "time-stamping unit". | not yet processed |
| TS102023-017 | 7.3.2 | technical | "Subscribers and relying parties" instead of just relying parties. | not yet processed |
| TS102023-018 | 7.4.5 | technical | Add media lifecycle management. | not yet processed |
| TS102023-019 | 7.4.6 | technical | Correct reference to clause 7.4.11. | not yet processed |
| TS102023-020 | 7.4.8 | technical | "TSA private signing key compromise". | not yet processed |
| TS102023-021 | 7.4.9 | technical | Correct reference to clause 7.4.11. | not yet processed |
| TS102023-022 | 7.4.11 | technical | "signature verification (public) key". | not yet processed |
| TS102023-023 | 4.2 | technical | Clarify TSA key vs TSU key. | no change |
| TS102023-024 | 4.2 | technical | Restriction on key backup? | no change |
| TS102023-025 | 7.1.2 d) | technical | Reader understanding of expiration date. | no change |
| TS102023-026 | 7.1.2 j) | technical | Correct clause reference to 7.4.11. | in process |
| TS102023-027 | 7.2.1 b) | technical | Add FIPS PUB 140-2. | in process |
| TS102023-028 | 7.2.2 a) | technical | Add FIPS PUB 140-2. | in process |
| TS102023-029 | 7.2.2 b) | technical | Note: avoid reusing serial numbers when backup key recovered. | in process |
| TS102023-030 | 7.2.4 | editorial | Correct clause reference to 7.4.11. | in process |
| TS102023-031 | 7.3.1 e) | technical | If clock out of accuracy, TSA shall revoke TSTs. | no change |
| TS102023-032 | 7.3.2 a) | technical | TSA needs to show clock correctness; guideline required. | in process |
| TS102023-033 | 7.3.2 d) | technical | TSA should not issue time-stamps during leap second processing. | in process |
| TS102023-034 | 7.4.8 | technical | Deal with issued TSTs in case of compromise. | no change |
| TS102023-035 | 7.4.8 c) | technical | TSA need to inform relying parties/subscribers if TSTs issued after compromise. | no change |
| TS102023-036 | – | technical | Time Authentication mechanism needed to prove time source accuracy. | no change |
| TS102023-037 | – | technical | Consistency: use "time-stamp token" and "TimeStampToken". | not yet processed |
| TS102023-038 | 7.2.3 | technical | Two levels of clock protection: procedural vs HSM-based. | not yet processed |
| TS102023-039 | 7.2.2 b) | technical | Specify how long exported key protection should last. | not yet processed |

### 5.7 TR 102 038 - XML format for signature policies
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TR102038-001 | – | technical | Add OCSPTrustCondition element to schema. | no change |

### 5.8 TR 102 041 - Signature policies report
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TR102041-001 | 8.3.1 | technical | Clarify difference between Common Rules and Commitment Rules; add OCSP trust conditions. | no change |
| TR102041-002 | 8.3.2 | technical | Add CRL Distribution Points. | no change |

### 5.9 TS 102 042 - PKC certificate policy
| Comment ID | Clause | Type | Comment Summary | Resolution Status |
|---|---|---|---|---|
| TS102042-001 | 2 | editorial | Update FIPS PUB 140-1 to 140-2. | not yet processed |
| TS102042-002 | 4.1 | editorial | Same as TS101456-004. | not yet processed |
| TS102042-003 | 4.1 | editorial | Same as TS101456-005. | not yet processed |
| TS102042-004 | 4.2 | technical | Same as TS101456-006. | not yet processed |
| TS102042-005 | 6.2 | technical | Same as TS101456-007 (adapted for TS 102 042). | not yet processed |
| TS102042-006 | 7.2.1 | technical | Reference FIPS PUB 140-1 or 140-2. | not yet processed |
| TS102042-007 | 7.2.2 | technical | Reference FIPS PUB 140-1 or 140-2. | not yet processed |
| TS102042-008 | 7.2.9 | technical | Same as TS101456-010. | not yet processed |
| TS102042-009 | 7.3.1 | technical | Same as TS101456-011 (adapted). | not yet processed |
| TS102042-010 | 7.2.8 | technical | Correction: "private key" not "public key". | not yet processed |
| TS102042-011 | 3.1 | technical | Add definition for Extended Normalized Certificate Policy. | not yet processed |
| TS102042-012 | 7.4.4 | technical | Same as TS101456-014. | not yet processed |
| TS102042-013 | 7.4.5 | technical | Same as TS101456-015. | not yet processed |
| TS102042-014 | 7.4.8 | technical | Same as TS101456-016. | not yet processed |
| TS102042-015 | 7.4.9 | technical | Same as TS101456-017. | not yet processed |
| TS102042-016 | 7.4.11 | technical | Same as TS101456-018. | not yet processed |
| TS102042-017 | 3.2 | technical | Update abbreviation NCP+ to "Extended Normalized Certificate Policy". | not yet processed |
| TS102042-018 | – | technical | Same as TS101456-022 (keys certified under multiple policies). | not yet processed |
| TS102042-019 | 7.2.9 | technical | Same as TS101456-025 (advise on SSCD environment). | not yet processed |
| TS102042-020 | 7.2.5 | technical | Same as TS101456-026 (use of CA key for multiple policies). | not yet processed |
| TS102042-021 | 7.4.7 | technical | Same as TS101456-027 (reference CWA 14167-1). | not yet processed |
| TS102042-022 | 8 | technical | Same as TS101456-028 (when new policy OID needed). | not yet processed |
| TS102042-023 | 7.2.2 b) NCP | technical | Same as TS101456-053 (key export protection by threshold secret sharing). | not yet processed |
| TS102042-024 | Annex D | technical | Same as TS101456-054 (correct cross-references). | not yet processed |

## Informative Annexes (Condensed)
- **Annex A (Comments in original format)**: Contains full original contributions organized by source (TC-ESI members, UNINFO-STT, Japan/China PKI forums, EESSI evaluation, CEN/ISSS, others, STF-220 tasks, XAdES-PLUGTESTS). Each contribution preserves original text and proposed resolutions. These are the raw inputs from which clause 5 elementary comments were derived.