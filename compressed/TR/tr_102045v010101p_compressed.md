# ETSI TR 102 045: Electronic Signatures and Infrastructures (ESI); Signature policy for extended business model
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2003-03 | **Type**: Technical Report (Informative)
**Original**: https://www.etsi.org/deliver/etsi_tr/102000_102099/102045/01.01.01_60/tr_102045v010101p.pdf

## Scope (Summary)
This Technical Report analyses business needs and provides a framework for signature policies governing multiple electronic signatures in extended business models (e.g., contracts, countersignatures, witnessing, notarization). It supplements TS 101 733 and TR 102 038 by addressing requirements for managing multiple signatures and proposes extensions to existing formats.

## Normative References
- [1] ETSI TS 101 733: "Electronic Signature Formats"
- [2] ETSI TR 102 038: "XML format for signature policies"
- [3] CEN CWA 14171: "Procedures for Electronic Signature Verification"
- [4] ETSI TR 102 041: "Signature Policies Report"
- [5] Directive 1999/93/EC of the European Parliament and of the Council
- [6] Concise Oxford English Dictionary, Fifth Edition 1974
- [7] ITU-T Recommendation X.509
- [8] IETF RFC 2630: "Cryptographic Message Syntax"
- [9] ETSI TS 101 862: "Qualified certificate profile"
- [10] ETSI TR 102 044: "Requirements for role and attribute certificates"

## Definitions and Abbreviations
- **attribute**: information bounded to an entity that specifies a characteristic (e.g., group membership, role, authorization) associated with an Attribute Certificate holder.
- **Certification Authority (CA)**: authority trusted to create and assign certificates, optionally creating users’ keys (X.509).
- **contractual signature policy**: set of rules for the creation and validation of multiple signatures on a contract.
- **digital signature**: data appended to, or cryptographic transformation of, a data unit that allows proof of source and integrity and protects against forgery (ISO 7498-2).
- **public key certificate**: public key of a user rendered unforgeable by CA encipherment (X.509).
- **role**: part played in a transaction or protocol; one’s function or expected behaviour.
- **signature policy**: set of rules for the creation and validation of an electronic signature, under which the signature can be determined to be valid.
- **signature policy issuer**: entity that defines technical and procedural requirements for electronic signature creation and validation to meet a particular business need (IETF RFC 3126).
- **signature validation policy**: part of the signature policy specifying requirements on signer and verifier.
- **signer**: person or entity that creates an (electronic) signature.
- **signing role**: role specified in a signature policy, allocated to or adopted by a signer, defining the relationship between its signature and any other required signatures.
- **TimeStamping Authority (TSA)**: trusted third party that creates time stamp tokens.
- **transactional signature policy**: set of rules for creation and validation of multiple signatures giving effect to a transaction.
- **valid electronic signature**: electronic signature that passes validation according to a signature validation policy.
- **verifier**: entity that validates an electronic signature or signatures.
- **Abbreviations**: ASN.1, CA, OCSP, OID, TSA, XML.

## 4 Overview
### 4.1 Background research
Goal: define signature policy for multiple signatures in wide range of business models. Identified use cases: parallel, countersignatures (embedded), sequential signatures. Sources: legal research, business experience, experts, authoritative literature. Finding: a single generic signature policy cannot meet all business needs; signatures often used without clear definition of commitment type or validation process.

### 4.2 Implications of the Electronic Signatures Directive 1999/93/EC
Directive preserves party autonomy, does not restrict contractual conditions, leaves national rules of evidence and form intact. Three categories: electronic signature (art. 5.2), advanced electronic signature (art. 2.2), qualified electronic signature (art. 5.1). Article 5.1 requires Member States to give qualified e-signatures equivalent status to handwritten signatures, but recitals preserve national rules. The Directive does not define signer’s intention; intent is essential in legal proceedings. Signature policies can provide context and method to demonstrate intention and commitment type.

### 4.3 Extended business model
Extended business model: transaction involving several actors/actions requiring multiple signatures. Approach: analyse transaction context and essential elements of signature creation and validation. Scenarios considered: purchase of life insurance (Italy), supply chain with linked SLAs, land purchase (UK) – detailed in Annex A.

### 4.4 Signature scenarios
Focus on: two or more primary signatures (buyer/seller), countersignature as authorization or witnessing, signatures in document flow, combination with notarial signature.

### 4.5 Introduction to signature policies
#### 4.5.1 Signature policies in the "paper" world
Meaning inferred from context. Implicit policies common (e.g., personal cheque). Statutory policies (wills, land, consumer protection) and customary policies (countersignatures, witnessing) exist.

#### 4.5.2 "Real world" signature policy example – Banking
Cheque example: document (form), signer (account holder, specimen signature held by bank), commitment type (authorization to pay), timing (date, six-month limit), location (some jurisdictions), formalities (mandate for joint/corporate accounts), technical/security considerations (signature matching, mandate rules, completion requirements, banking regulations).

#### 4.5.3 Electronic signature policies
Article 5.1 of Directive is a statutory signature policy. National implementations (Germany, Italy) are examples. Main use of signature policies: communicate business requirements and signature context for interoperability between enterprise applications. Signature usage rules must consider human operator interface; only a person can decide to sign.

## 5 Analysis of signature issues
### 5.1 Transactional context/field of application
Signature role, meaning, and formalities are context-specific. For example, position of signature on a contract indicates binding intent; draft documents may use pencil, initials, or annotations like "Draft".

### 5.2 Formalities of signing/intention to sign
Act of signing is a ceremony; it draws attention to commitment. Degrees: simple signature, printed declaration, witnessing, notarization, formal ceremony. The Directive does not require evidence of intention to sign. Signature policies can specify formalities.

### 5.3 Identity of signer
Signature must be attributable to signer. In paper world, often achieved by printing name under signature. Role or attributes may be more important than identity.

### 5.4 Roles and attributes of signer
Apparent authority sufficient in most commercial contexts. Electronic environment may require verifiable evidence (public key certificate, attribute certificate). Standard business roles could be categorized and referenced (e.g., OID).

### 5.5 Signature commitment types
Meaning of signature inferred from context. Common types: draft (no legal commitment), contract (legal commitment), acknowledgement of receipt. Ambiguity can lead to unenforceability.

### 5.6 Timing and sequence
Sequence matters: witness must sign after primary signer; supervisor countersigns after subordinate. Timing can provide evidence of proper process (e.g., short interval increases likelihood of genuine witnessing).

### 5.7 Location
Location may affect jurisdiction. Some jurisdictions require location on cheques. Witnessing/notarization can attest to physical presence. Hard to verify without extraneous evidence.

### 5.8 Longevity
Paper signatures durable; e-signatures need longevity mechanisms: robust signature techniques or early verification and secure archiving of verification data.

### 5.9 Technical and security considerations
Paper world: handwritten signature, cheque card, specimen signatures, identification, personal attendance. Electronic world: certificates (qualified, non-repudiation), secure signature creation devices, signature policies.

### 5.10 Multiple signatures
#### 5.10.1 Countersignatures
Countersignature used to give effect to or activate a primary signature. Meaning varies: authorization (supervisor), approval, or mere witnessing. Technical countersignature (RFC 2630) signs only the primary signature; business countersignature may sign data content as well. Responsibility and commitment must be specified in the signature policy.

#### 5.10.2 Witnesses
Witness attests to seeing the signer make the signature, not necessarily to identity. In electronic world, witnessing could be after signature creation, but must be clearly defined.

#### 5.10.3 Notarial signatures
Notary provides incontrovertible evidence of legal validity, capacity, authority, free will. Notarization rarely challenged; therefore, once notarial signature is validated, no need to verify underlying signatures. Traditional notarial functions require personal attendance; full electronic notarization faces legal/ethical obstacles.

## 6 Formalities of signing
Electronic signatures may lose the “warning” mechanism of handwritten signing. Additional steps (e.g., typing "lu et approuvé", on-screen warnings, displaying a picture of the signature) can replicate context. Selection of PIN alone insufficient to prove intent.

## 7 Roles and attributes
### 7.1 Meaning of “role”, “attribute”, and “privilege”
- **Role**: part played in a process; stable, may be held by different persons.
- **Attribute**: characteristic bound to an entity; business role becomes attribute in transactional context.
- **Privilege**: right to take action (e.g., signing authority) that can be an attribute.

### 7.2 Claimed versus certified business roles or attributes
Paper world: trust built over time; claimed authority often accepted. Electronic environment may require certification for added certainty, but not always necessary.

### 7.3 Authority as an attribute
Business role implies authority. Additional information may be needed (e.g., value limits). Certification of authority may be required for e-commerce.

#### 7.3.1 Delegated authority
- **Agency**: acts of agent bind principal, even if exceeding authority.
- **Powers of Attorney**: must be actual authority; certificate containing attribute and pointer to source document recommended.
- **Per proxy (p.p., p.o.)**: claimed authority; rules should specify whether actual or claimed authorization is sufficient.

#### 7.3.2 Restricted authority
Negative attribute (limits). Reliable method needed for trading partners to know limits. Employer may use certificate to restrict authority; relying party protected by vicarious liability.

### 7.4 Categorization of roles
#### 7.4.1 Business roles
Insufficient consistency across jurisdictions for full categorization. Recommended: define roles by reference to established legal definitions (e.g., company laws). Categorization would enhance certainty and harmonization.

#### 7.4.2 Transactional roles in international trade
Refer to TR 102 044 Annex B for Italian Assocertificatori document on role certification.

#### 7.4.3 Signing roles
Signing roles manage multiple signatures: Primary Signature (PS) and Countersignature (CS). Role may be allocated or claimed; if certification needed, it becomes an attribute.

## 8 Commitment types in electronic signatures
### 8.1 Real world commitment types
List of 18 purposes (e.g., indicate intention to be bound, approve, authorize, witness, notarize, acknowledge receipt, test). Not recommended to categorize all for electronic use.

### 8.2 Electronic commitment types
Need to distinguish between signatures for authentication only, handwritten equivalent with legal commitment, and other intents. Commitment type may be express (signer selects) or implicit. For primary signatures: final commitment, approval, authentication, proof of receipt. For countersignatures: authorization, witnessing, notarial. Administrative types: administrative (simple), e-notary, e-signature validation.

#### 8.2.1 E-notary signatures
Trusted third party service that validates authenticity/integrity at a given point and archives evidence. Not equivalent to traditional notarial services.

#### 8.2.2 Electronic signatures as part of a validation process
E-notary/verifier validates signatures, captures and signs validation data for future reference.

#### 8.2.3 Simple administrative e-signature
Indicates data integrity without content review; used for archiving or joining documents (e.g., electronic “stapling”).

## 9 Multiple signatures
### 9.1 Parallel signatures
Mutually independent signatures, ordering not important. Each is applied to the hash of data, not to another signature. Example: buyer and seller on contract.

### 9.2 Sequential (parallel) signatures
Variation of parallel signatures where ordering is significant. May be applied to same data content or to other signatures as part of data content.

### 9.3 Embedded signatures
One signature applied to another (countersignature). Sequence important; validity of first depends on second. Example: witness or notary signature applied over primary signature.

### 9.4 Multiple signature management
Management requires specifying creation method for each signature, then defining relationships via signing roles and commitment types.

#### 9.4.1 Signing roles
- **Primary Signature (PS)**: applied in parallel; may require countersignature.
- **Countersignature (CS)**: applied to one or more PS and other CS. Examples: contract (PS/1 buyer, PS/2 seller); expenses claim (PS/1 employee, CS/1 manager, CS/2 accounts).

#### 9.4.2 Commitment types for electronic signatures
Help validate relationships. For primary: final commitment, approval, authentication, proof of receipt. For countersignatures: authorization, witnessing, notarial. Administrative: simple, e-notary, e-validation.

### 9.5 Multiple signature validation
Three stages: (1) creation and collection of validation data; (2) predicted validation results; (3) comparison. Validate each single signature under a single signature policy, then validate relationships: presence, roles, commitment types, signed data, timing/sequence. Example: purchase/sale with witnessing – acceptable sequences defined by timestamps and identity comparisons.

## 10 Signature policies
### 10.1 Legal effect of signature policies
Failure to read a signature policy may not be treated like standard contract terms. Signer must understand they are making a signature; signature policy may need to be brought to signer’s attention to be enforceable.

### 10.2 Implicit or express signature policies
Policy may be implied (by law, custom, or technical implementation) or express. Combining technical rules with human intervention raises risk; high-level policies (e.g., “will conform to article 5.1”) are more suitable for human use.

### 10.3 Drafting a signature policy
Two parts: business rules (high-level) and signature policy rules (management/operational and technical). Signature validation should inform creation requirements. Claimed facts may still be relevant (e.g., location). Validation must relate to time of creation.

### 10.4 Significant elements of a signature policy
Three-level approach: business rules, signature usage rules (management/operational and technical), technical specifications. “Umbrella” approach allows subordinate policies.

#### 10.4.1 Business rules
Include: title/identification, issuer, business application domain, transactional context, consent to accept electronic signatures, proposed signers (signing roles), proof of authority, signature commitment type, formalities of signing, timing constraints, security considerations (trust model, longevity, archiving), allocation of responsibility for verification, audience conditions (e.g., jurisdiction), access control, dispute resolution, boilerplate terms. Example in Annex C.

#### 10.4.2 Signature policy rules
- **Management practices and procedures**: allocation of attributes, management of certificates, use of tokens, creation procedures, verification/validation of countersignatures, archiving, disciplinary procedures.
- **Technical rules**: identification and allocation of signing roles, reliance on certificates (type, CA, algorithms, sscd), certification of attribute information, time stamping, signature attributes (commitment type, delegated/non-delegated, parallel/embedded/sequential).

### 10.5 Illustrations for signature policy rules
#### 10.5.1 Countersignatures for authorization
Detailed analysis of countersignature purpose: (a) part of process, (b) confirm prior signer’s actions/authority, (c) confirm validity of signature. Rules should specify verification steps (time stamp, primary signature validation, data checks, archiving) and creation requirements (identity, role, declaration, commitment type, time stamp, what is signed).

#### 10.5.2 Countersignatures in a document flow
Parallel signatures where signers add data/function; sequence and timing important. Technical rules cover time stamps and ordering.

#### 10.5.3 Delegated authority
Policy must state whether delegated authority accepted, and whether actual or claimed authorization required. Actual delegation can be certified via certificate. For claimed authority, specify conditions under which validation does not fail.

#### 10.5.4 Notarial signatures
Notary duties: ensure legal validity, authority, understanding, capacity, free will. Full electronic notarization not possible due to requirement for personal attendance and paper archiving. Hybrid process (electronic initial consideration, personal attendance for signing) may be feasible; requires security specifications.

## 11 Conclusions
1. Signature policies cover legal and technical aspects, including formalities and acceptance conditions.
2. The Directive does not address signer’s intention; signature policies can mitigate.
3. Policy may relate to single signature, document, or transaction.
4. No single generic policy for all models or multiple signatures.
5. Policy consists of business rules and subordinate policies.
6. Until business custom established, trading partners should agree signature policy terms.
7. Signature policies are not equivalent to normal contractual terms; they may be enforceable even if signer lacks actual knowledge.
8. Automated implementation is most effective.

### 11.1 Recommended changes to the signature policy formats
The TR supplements TS 101 733 and TR 102 038; reconciliation of differences may follow future work.

### 11.2 Recommendations for future work
Develop an XML-oriented protocol for managing multiple signatures and publishing acceptance conditions. Should be generic, complement OASIS initiatives. Suggested focus on a widely used business model (e.g., purchasing). Further work should include participation from other organizations and consider e-government or notarization as potential areas.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Signature policies shall include rules for creation and validation of electronic signatures. | shall | Clause 10 (TS 101 733) |
| R2 | Each single signature shall be validated according to a single signature policy (e.g., TS 101 733). | shall | Clause 9.5 |
| R3 | Relationships between multiple signatures shall be validated by checking presence, roles, commitment types, signed data, and timing/sequence. | shall | Clause 9.5 |
| R4 | Signing roles shall be allocated as Primary Signature (PS) or Countersignature (CS) in the signature policy. | shall | Clause 9.4.1 |
| R5 | Commitment type for primary signatures shall distinguish between final commitment, approval, authentication, and proof of receipt. | shall | Clause 8.2 |
| R6 | Commitment type for countersignatures shall distinguish between authorization, witnessing, and notarial. | shall | Clause 8.2 |
| R7 | When a signature policy requires a countersignature for authorization, the countersigner shall validate the primary signature (identity, certificate status, authority). | shall | Clause 10.5.1 |
| R8 | Signature policies shall specify whether delegated authority is accepted and whether actual or claimed authorization is required. | shall | Clause 10.5.3 |
| R9 | For notarial signatures, the signature policy shall specify the jurisdiction and security requirements; full electronic notarization requires further work. | shall | Clause 10.5.4 |
| R10 | Signature policies shall include business rules covering: identification, issuer, domain, transactional context, consent, proposed signers, proof of authority, commitment type, formalities, timing, security, allocation of verification, audience conditions, access control, dispute resolution. | shall | Clause 10.4.1 |

## Informative Annexes (Condensed)
- **Annex A (Business scenario descriptions)**: Describes three use cases: purchase of life insurance (Italy), supply chain with linked SLAs, land purchase (UK). Each includes actors, sequence diagrams, and signature requirements.
- **Annex B (Signature commitment categories)**: Lists 11 commitment types: legal commitment, authentication, acknowledgement of receipt, authorship/attribution, countersignature for authorization, witnessing, notarization, administrative signature, e-notary, e-validation, claimed delegated authority (per proxy). Notes restrictions on combination.
- **Annex C (Model/specimen policy document)**: Provides an example signature policy for a mortgage/loan offer/acceptance between ABC plc and a consumer. Includes business rules: title, domain, transactional context (offer/acceptance), consent, proposed signers (authorized persons + witness), proof of authority (certificate with identity and job title), signature commitment type (legal commitment), timing constraints (28-day offer expiry), security considerations (article 5.1 compliance, accredited CA, timestamping), allocation of responsibility (each party verifies), audience conditions (offer not binding unless signed and countersigned), access control (banking confidentiality), dispute resolution (expert determination).
- **Annex D (Bibliography)**: Lists references to ebXML, OASIS, legal texts, IETF RFCs, ISO standards, and other relevant publications.