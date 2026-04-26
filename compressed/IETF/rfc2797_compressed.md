# RFC 2797: Certificate Management Messages over CMS
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: April 2000 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc2797

## Scope (Summary)
This document defines the Certificate Management over CMS (CMC) protocol, an Internet standards track protocol for public key certificate enrollment and management. It addresses an interface to certification services based on CMS/PKCS7 and PKCS#10/CRMF, and supports S/MIME v3 requirements. The protocol defines request/response message formats, control attributes for transaction management, identity proof, proof-of-possession (POP), and local registration authority (LRA) interactions.

## Normative References
- [CMS] Housley, R., "Cryptographic Message Syntax", RFC 2630, June 1999.
- [CRMF] Myers, M., et al., "Internet X.509 Certificate Request Message Format", RFC 2511, March 1999.
- [DH-POP] Prafullchandra, H. and J. Schaad, "Diffie-Hellman Proof-of-Possession Algorithms", Work in Progress.
- [HMAC] Krawczyk, H., et al., "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [PKCS10] Kaliski, B., "PKCS #10: Certification Request Syntax v1.5", RFC 2314, October 1997.
- [PKIXCERT] Housley, R., et al., "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", RFC 2459, January 1999.
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [SMIMEV3] Ramsdell, B., "S/MIME Version 3 Message Specification", RFC 2633, June 1999.
- [X942] Rescorla, E., "Diffie-Hellman Key Agreement Method", RFC 2631, June 1999.

## Definitions and Abbreviations
- **End-Entity (EE)**: The entity that owns a key pair and for whom a certificate is issued.
- **LRA / RA**: (Local) Registration Authority, an intermediary between an End-Entity and a Certification Authority.
- **CA**: Certification Authority, the entity that performs actual certificate issuance.
- **Client**: An entity that creates a PKI request (RAs and End-Entities).
- **Server**: Entities that process PKI requests and create responses (CAs and RAs).
- **PKCS#10**: Public Key Cryptography Standard #10 – Certificate Request Message syntax.
- **CRMF**: Certificate Request Message Format RFC [CRMF].
- **CMS**: Cryptographic Message Syntax RFC [CMS] (superset of PKCS7).
- **POP**: Proof of Possession – a value used to prove that the private key corresponding to a public key is possessed by the end-entity.
- **Transport wrapper**: The outermost CMS wrapping layer.

## Protocol Requirements (Section 1)
- The protocol shall be based as much as possible on existing CMS, PKCS#10, and CRMF specifications.
- The protocol must support current industry practice of a PKCS#10 request followed by a PKCS#7 response as a subset.
- The protocol needs to easily support multi-key enrollment protocols required by S/MIME and other groups.
- The protocol must supply a way of doing all operations in a single-round trip; when not possible, the number of round trips is to be minimized.
- The protocol will be designed such that all key generation can occur on the client.
- The mandatory algorithms must superset the required algorithms for S/MIME.
- The protocol will contain POP methods; optional provisions for multiple-round trip POP will be made if necessary.
- The protocol will support deferred and pending responses for cases where external procedures are required to issue a certificate.
- The protocol needs to support arbitrary chains of local registration authorities as intermediaries between certificate requesters and issuers.

## Protocol Overview (Section 2)
- Enrollment transactions generally consist of a single round trip.
- Two request messages: (a) bare PKCS#10 (Simple Enrollment Request), (b) PKCS#10 or CRMF wrapped in CMS as PKIData (Full PKI Request).
- Two response messages: (a) degenerate CMS signedData (Simple Enrollment Response), (b) ResponseBody wrapped in CMS signedData (Full PKI Response).
- Renewal and re-key messages look like any enrollment; identity proof supplied by existing certificates from the CA.
- LRAs can wrap client enrollment messages with additional requirements.
- Underlying transport is independent; optional services include transaction management, replay detection, deferred issuance, revocation, and certificate/CRL retrieval.

## Protocol Elements (Section 3)

### PKIData Object (3.1)
- **ID**: `id-cct-PKIData OBJECT IDENTIFIER ::= { id-cct 2 }`
- **ASN.1 Structure**:
  ```asn1
  PKIData ::= SEQUENCE {
      controlSequence    SEQUENCE SIZE(0..MAX) OF TaggedAttribute,
      reqSequence        SEQUENCE SIZE(0..MAX) OF TaggedRequest,
      cmsSequence        SEQUENCE SIZE(0..MAX) OF TaggedContentInfo,
      otherMsgSequence   SEQUENCE SIZE(0..MAX) OF OtherMsg
  }
  ```
- **controlSequence**: Sequence of control attributes (OID-defined). Unrecognized OIDs MUST result in no part of the request being successfully processed.
- **reqSequence**: Sequence of certificate requests (PKCS#10 or CRMF per CertificationRequest or CertReqMsg).
- **cmsSequence**: Sequence of CMS objects (EnvelopedData, SignedData, EncryptedData only).
- **otherMsgSequence**: Allows arbitrary data items (OID + any).

### ResponseBody Object (3.2)
- **ID**: `id-cct-PKIResponse OBJECT IDENTIFIER ::= { id-cct 3 }`
- **ASN.1 Structure**:
  ```asn1
  ResponseBody ::= SEQUENCE {
      controlSequence   SEQUENCE SIZE(0..MAX) OF TaggedAttribute,
      cmsSequence       SEQUENCE SIZE(0..MAX) OF TaggedContentInfo,
      otherMsgSequence  SEQUENCE SIZE(0..MAX) OF OtherMsg
  }
  ```
- Same fields as PKIData without reqSequence.

### Certification Requests (3.3)
#### PKCS#10 Request Body (3.3.1)
- **Servers MUST** be able to understand and process PKCS#10 request bodies.
- **Clients MUST** produce PKCS#10 request body when using Simple Enrollment Request; **MAY** produce when using Full Enrollment Request.
- Client: subject name and public key MUST be present; subject name MAY be NULL but MUST be present. CAs that receive a NULL subject name MAY reject (if rejected and response returned, MUST respond with failInfo **badRequest**).
- Client MAY incorporate X.509 v3 extensions as `ExtensionReq` attribute (OID `pkcs-9 14`).
- **Servers MUST** be able to process all extensions defined in [PKIXCERT]. Servers not required to process other V3 extensions or private extensions.
- Servers may modify client-requested extensions but **MUST NOT** alter extension so as to invalidate original intent. If denied due to extension, server **MUST** respond with failInfo **unsupportedExt**.

#### CRMF Request Body (3.3.2)
- **Servers MUST** be able to understand and process CRMF request body; **Clients MAY** produce CRMF message body when using Full Enrollment Request.
- Additional constraints:
  - Each CRMF message MUST include both subject and publicKey fields; subject MAY be NULL but MUST be present.
  - When both CRMF and CMC controls exist with equivalent functionality, CMC control SHOULD be used; **CMC control MUST override** any CRMF control.
  - `regInfo` field **MUST NOT** be used on a CRMF message; use `regInfo` control attribute (section 5.12) instead.
  - Indirect POP method not supported; direct or other methods **MUST** be used. `encrCert` SubsequentMessage **MUST NOT** be used.
  - `POPOSigningKeyInput` **MUST NOT** be used (since subject and publicKey always present).
- Server extension handling: same as PKCS#10 (must process [PKIXCERT], may modify, MUST NOT invalidate intent, denied -> failInfo unsupportedExt).

#### Diffie-Hellman Public Key Certification Requests (3.3.3)
- **No-Signature Signature Mechanism** (3.3.3.1): OID `id-alg-noSignature`; parameters MUST be present and encoded as NULL; value is hash of certification request. No security – if POP required, POP mechanism in section 5.7 **MUST** be used.
- **Diffie-Hellman POP Signature** (3.3.3.2): CMC compliant implementations MUST support section 5 of [DH-POP].
- **Diffie-Hellman MAC signature** (3.3.3.3): CMC compliant implementations MAY support section 4 of [DH-POP].

### Body Part Identifiers (3.4)
- Each element in PKIData or PKIResponse has a unique 4-octet integer (bodyPartID). Zero reserved for current PKIData object.
- Duplicate IDs in different layers allowed; within a single object, duplicates **MUST** cause error (badRequest, bodyPartID 0).

### Control Attributes (3.5)
- **Servers MUST** fail processing of entire PKIData if any control attribute is unrecognized; response MUST be error badRequest and bodyList contains bodyPartID of invalid/unrecognized attribute.
- Syntax:
  ```asn1
  TaggedAttribute ::= SEQUENCE {
      bodyPartID         BodyPartId,
      attrType           OBJECT IDENTIFIER,
      attrValues         SET OF AttributeValue
  }
  ```

### Content Info Objects (3.6)
- TaggedContentInfo wraps a ContentInfo; uses SignedData, EnvelopedData, Data.

#### Signed Data (3.6.1)
- Used as wrapper for PKIData in request and as outer part of response. For response without data, no signerInfo.

#### Enveloped Data (3.6.2)
- Provides confidentiality. Used to encrypt entire request (section 4.5) or wrap private key material for archival. **Servers MUST** implement envelopedData per [CMS].

### Other Message Bodies (3.7)
- Allows arbitrary data objects (OtherMsg) with OID-defined type and value.

## PKI Messages (Section 4)

### Simple Enrollment Request (4.1)
- Plain PKCS#10 message. If private key capable of signing, **PKCS#10 MUST be signed** with that key. For D-H key, **D-H POP mechanism [DH-POP] MUST be used**.
- **Servers MUST support** Simple Enrollment Request. If granted, server **MUST return** Simple Enrollment Response (Section 4.3). If fails, Full Enrollment Response MAY be returned or no response.
- Advanced services not supported.

### Full PKI Request (4.2)
- **Clients SHOULD use** Full Enrollment Request when enrolling. **Servers MUST support**.
- An enrollment response **MUST be returned** to all Full Enrollment Requests.
- Structure: PKIData wrapped in signedData CMS. Order within PKIData: 1. All Control Attributes, 2. All certification requests, 3. All CMS objects, 4. All other messages.
- Duplicate bodyPartIDs -> server MUST return error badRequest with bodyPartID 0.
- SignedData may be signed by private key of signature certification request or by previously certified signature key. If using signature certification request key:
  a) the certification request **MUST include** Subject Key Identifier extension request,
  b) subjectKeyIdentifier form of SignerIdentifier **MUST be used**,
  c) value of subjectKeyIdentifier **MUST be** the SKI specified in the corresponding certification request.
- If request key used for signing, there **MUST be only one** signerInfo.
- Renewal/re-key: identification and identityProof not required (use existing certificate). CAs/LRAs may impose restrictions; if key reuse prohibited, CA MUST return NOKEYREUSE failure code.

### Simple Enrollment Response (4.3)
- **Servers SHOULD use** simple enrollment response whenever possible. **Clients MUST** be able to process it.
- Consists of signedData with no signerInfo; certificates in certificate bag.
- **Clients MUST NOT assume** certificates are in any order. **Servers SHOULD include** all intermediate certificates needed for complete chains. Server MAY include CRLs and self-signed certificates. **Clients MUST NOT implicitly trust** self-signed certificates due to presence; **clients SHOULD** provide a mechanism to enable explicit trust.

### Full PKI Response (4.4)
- **Servers MUST return** full PKI response if (a) full request failed or (b) additional services required. Servers **MAY** return full PKI responses with failure for simple requests.
- Structure: signedData encapsulating ResponseBody. In ResponseBody, all Control Attributes **MUST precede** all CMS objects.
- Certificate order and chain inclusion same as Simple.
- **Clients MUST** be able to process full PKI response.

### Application of Encryption (4.5)
- PKI message may be encrypted by wrapping signedData in EnvelopedData (nested content type `id-signedData`). Recommended: if enveloped layer applied, place second signing layer outside.
- Three options: Normal (SignedData only), Option 1 (EnvelopedData(SignedData(PKIData))), Option 2 (SignedData(EnvelopedData(SignedData(PKIData)))).
- **Servers MUST** support all three versions. Clients and servers MAY use authenticated secure channel instead.

## Control Attributes (Section 5)

### CMC Status Info (5.1)
- OID: `id-cmc 1`, Syntax: `CMCStatusInfo`.
- Used in Full PKI Response to return status. Servers MAY emit multiple; **Clients MUST** handle multiple.
- `CMCStatus` values: success(0), failed(2), pending(3), noSupport(4), confirmRequired(5).
- `CMCFailInfo` values: badAlg(0), badMessageCheck(1), badRequest(2), badTime(3), badCertId(4), unsuportedExt(5), mustArchiveKeys(6), badIdentity(7), popRequired(8), popFailed(9), noKeyReuse(10), internalCAError(11), tryLater(12).
- If cMCStatus is success, control MAY be omitted unless it is only item.

### Identification and IdentityProof (5.2)
- OIDs: `id-cmc 2`, `id-cmc 3`. Syntax: UTF8String, OCTET STRING.
- **If clients support Full Request, they MUST implement** this identity proof method. **Servers MUST provide** this method; MAY also have bilateral method.
- Method: out-of-band token, hash with SHA-1, HMAC-SHA1 over reqSequence (exact encoding). Server verifies by recomputing. If fail, failInfo **badIdentity**.
- Optional `identification` attribute assists server in locating shared secret; if present, HMAC uses hash of concatenation of token and identification value.
- Hardware token generation (5.2.1): identification MUST include hardware token, shared secret = token, subject name MUST contain required fields.

### Linking Identity and POP (5.3)
#### Witness values derived from shared-secret (5.3.1)
- **Clients and servers MUST support** this technique.
- Client computes random R (≥512 bits), SHA-1 hash of token, HMAC-SHA1 over R using hash of token as secret. R encoded as `idPOPLinkRandom` control attribute; HMAC result as `idPOPLinkWitness` extension in each certificate request (CRMF controls or PKCS#10 attributes).
- **Servers MUST verify** each certificate request contains `idPOPLinkWitness` and value derived correctly.

#### Shared-secret/subject DN matching (5.3.2)
- **Clients and servers MAY support**.
- Subject DN associated with shared secret; client MUST include that exact subject DN in every certificate request (not null). Client MUST include identityProof control attribute.
- Server MUST (a) validate identityProof, (b) check subject DN matches. If either fails, request rejected.

#### Renewal and Re-Key Messages (5.3.3)
- Subject DN in certificate referenced by CMS signerInfo and in all certificate requests **MUST match** per [PKIXCERT] name matching.

### Data Return (5.4)
- OID: `id-cmc 4`, Syntax: OCTET STRING. If appears in request, server MUST return same data in response.

### Add Extensions (5.5)
- OID: `id-cmc 8`, Syntax: `AddExtensions` (with pkiDataReference, certReferences, extensions).
- Used by LRAs. Servers MUST process [PKIXCERT] extensions; may modify LRA-requested extensions but MUST NOT reverse meaning. If denied due to extension, failInfo unsupportedExt.
- Conflict rules: if within single PKIData, reject with badRequest; if between layers, outermost version used.

### Transaction Management (5.6)
- OIDs: `id-cmc 5` (transactionId), `id-cmc 6` (senderNonce), `id-cmc 7` (recipientNonce).
- Clients MAY include transactionId. If present, all subsequent messages in same transaction MUST include same transactionId. **Server MUST use only transactionIds in outermost PKIdata object.**
- Replay protection via nonces: first message contains senderNonce; response reflects as recipientNonce and includes new senderNonce. **Server MUST use only nonces in outermost PKIdata.**

### Proof-of-possession for encryption-only keys (5.7)
- OIDs: `id-cmc 9` (encryptedPOP), `id-cmc 10` (decryptedPOP). Optional to implement for both servers and clients.
- **Servers MAY require** this POP method only if another unavailable. **Servers SHOULD reject** all requests if any required POP missing.
- Algorithm: server generates random y, returns EncryptedPOP with request, envelopedData containing y, algorithm identifiers, witness (hash of y). Client decrypts, verifies witness, if fails MUST abort with failInfo popFailed. Client returns DecryptedPOP with possession proof (HMAC-SHA1 using y as secret). Server recomputes and compares.
- Clients MUST implement SHA-1 for witnessAlgID, HMAC-SHA1 for thePOPAlgID.
- Stateless server: use seed x, compute y = F(x,R).

### LRA POP Witness (5.8)
- OID: `id-cmc 11`, Syntax: `LraPopWitness` (pkiDataBodyid, bodyIds).
- If CA does not allow LRA POP verification, returns error POPFAILURE. **CA MUST NOT** start challenge-response to re-verify.

### Get Certificate (5.9)
- OID: `id-cmc 15`, Syntax: `GetCert` (issuerName, serialNumber). Optional.
- Response: certificates in signedData.

### Get CRL (5.10)
- OID: `id-cmc 16`, Syntax: `GetCRL` (issuerName, cRLName, time, reasons). Optional.
- Response: CRL in signedData.

### Revocation Request (5.11)
- OID: `id-cmc 17`, Syntax: `RevRequest` (issuerName, serialNumber, reason, invalidityDate, sharedSecret, comment).
- For loss of private key, shared secret may be used as alternative authenticator. (Acceptability is local policy.)
- **Clients MUST** provide capability to produce digitally signed revocation request; **SHOULD** be capable of unsigned request containing shared secret. If client provides self-revocation, **MUST** be capable of producing request containing shared secret.
- **Servers MUST** accept both forms. Full response message MUST be returned.

### Registration and Response Information (5.12)
- OIDs: `id-cmc 18` (regInfo), `id-cmc 19` (responseInfo). Syntax: OCTET STRING. Content based on bilateral agreement.

### Query Pending (5.13)
- OID: `id-cmc 21`, Syntax: `QueryPending` (OCTET STRING). Contains token from server's PendInfo.
- If server returns pending state, the token MUST NOT change during the request.

### Confirm Certificate Acceptance (5.14)
- OID: `id-cmc 24`, Syntax: `CMCCertId` (IssuerSerial).
- If CMCStatusInfo has confirmRequired, client **MUST return** Confirm Certificate Acceptance prior to any usage of certificate. **Clients SHOULD** wait for response. **Servers MUST return** full enrollment response for confirm.

## Local Registration Authorities (Section 6)
- LRAs may batching, POP proofs, add extensions, archive keys, route requests.
- LRA may forward unchanged, add new wrapping layer, or remove layers.
- LRA places client messages appropriately: Simple in reqSequence, Full in cmsSequence.
- **LRA MUST NOT alter** any certificate request body (would invalidate signature and POP).
- When removing or modifying encryption (6.1), LRA **MUST** remove signing layers containing encryption, merge control statements as per local policy, and place in new LRA signing layer.
- Signature layer removal (6.2): only if encryption needs modification or CA will not accept multiple LRA signatures. **LRAs SHOULD NOT** remove signing layer otherwise. When removing, merge controls and place in new LRA signing layer.

## Transport Wrapping (Section 7)
- Three methods: MIME, file-based, socket.
- MIME wrapping (7.1): specific Content-Type and smime-type parameters as per table.
  - Simple PKI request: application/pkcs10, extension .p10.
  - Full PKI request: application/pkcs7-mime, smime-type "CMC-request", .p7m.
  - Simple PKI response: application/pkcs7-mime, smime-type "certs-only", .p7c.
  - Full PKI response: application/pkcs7-mime, smime-type "CMC-response", .p7m.
- File-based (7.2): Full PKI request .crq, Full PKI response .crp.
- Socket-based (7.3): raw BER encoded, no wrapping.

## Interoperability (Section 8)

### Mandatory and Optional Algorithms (8.1)
- **CMC clients and servers MUST** be capable of producing and processing message signatures using DSA (AlgorithmIdentifier per [PKIXCERT] section 7.2.2). **SHOULD** also be capable of RSA signatures.
- **CMC clients and servers MUST** be capable of protecting/accessing message encryption keys using Diffie-Hellman (D-H) key exchange; D-H/3DES protection MUST be indicated per [CMS]. **SHOULD** also be capable of RSA key transport.

### Minimum Conformance Requirements (8.2)
- **Minimally compliant server:**
  - a) MUST accept Full PKI Request (MUST accept CRMF and PKCS#10 bodies)
  - b) MUST accept Simple Enrollment Request
  - c) MUST be able to return Full PKI Response; SHOULD use Simple Enrollment Response when possible.
- **Minimally compliant client:**
  - a) MAY use Simple or Full; MUST use PKCS#10 for Simple, MAY use PKCS#10 or CRMF for Full
  - b) MUST understand Simple Enrollment Response
  - c) MUST understand Full PKI Response.

## Security Considerations (Section 9 – condensed)
- Out-of-band trust initiation required (e.g., IPSEC, TLS). Replay detection may be needed; implementers should consider nonce attributes (5.6). Signing keys **must not be archived**. Key archival requires careful verification. Clients and servers should check cryptographic parameters to avoid small subgroup attacks.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Servers MUST be able to understand and process PKCS#10 request bodies. | shall | 3.3.1 |
| R2 | Clients MUST produce PKCS#10 request body when using Simple Enrollment. | shall | 3.3.1 |
| R3 | Clients MAY produce PKCS#10 request body when using Full Enrollment. | may | 3.3.1 |
| R4 | Subject name in CertificationRequest MUST be present (may be NULL). | shall | 3.3.1 |
| R5 | CA that rejects NULL subject MUST respond with failInfo badRequest. | shall | 3.3.1 |
| R6 | Servers MUST be able to process all extensions defined in [PKIXCERT]. | shall | 3.3.1 |
| R7 | Servers MUST NOT alter extension to invalidate original intent. | shall | 3.3.1 |
| R8 | If certification request denied due to extension, server MUST respond with unsupportedExt. | shall | 3.3.1 |
| R9 | Servers MUST be able to understand and process CRMF request body. | shall | 3.3.2 |
| R10 | Each CRMF message in Full Enrollment MUST include subject and publicKey. | shall | 3.3.2 |
| R11 | When both CRMF and CMC controls exist, CMC control MUST override. | shall | 3.3.2 |
| R12 | regInfo field MUST NOT be used on a CRMF message. | shall | 3.3.2 |
| R13 | Indirect POP method not supported; other methods MUST be used if POP desired. | shall | 3.3.2 |
| R14 | POPOSigningKeyInput MUST NOT be used. | shall | 3.3.2 |
| R15 | CMC compliant implementations MUST support section 5 of [DH-POP]. | shall | 3.3.3.2 |
| R16 | CMC compliant implementations MAY support section 4 of [DH-POP]. | may | 3.3.3.3 |
| R17 | Unrecognized control attributes MUST cause entire PKIData to fail with badRequest. | shall | 3.5 |
| R18 | Servers MUST implement envelopedData according to [CMS]. | shall | 3.6.2 |
| R19 | Servers MUST support Simple Enrollment Request. | shall | 4.1 |
| R20 | If Simple Enrollment granted, server MUST return Simple Enrollment Response. | shall | 4.1 |
| R21 | Clients SHOULD use Full Enrollment Request when enrolling. | should | 4.2 |
| R22 | Servers MUST support Full Enrollment Request. | shall | 4.2 |
| R23 | An enrollment response MUST be returned to all Full Enrollment Requests. | shall | 4.2 |
| R24 | Duplicate bodyPartIDs in Full Request -> server MUST return error badRequest. | shall | 4.2 |
| R25 | Servers MUST return full PKI response if full request failed or additional services required. | shall | 4.4 |
| R26 | Clients MUST be able to process full PKI response. | shall | 4.4 |
| R27 | Servers MUST support all three encryption options (normal, Option1, Option2). | shall | 4.5 |
| R28 | Clients MUST implement identity proof method (shared secret). | shall | 5.2 |
| R29 | Servers MUST provide shared secret identity proof method. | shall | 5.2 |
| R30 | Clients and servers MUST support witness technique for identity-POP linking (5.3.1). | shall | 5.3 |
| R31 | Servers MUST verify idPOPLinkWitness per section 5.3.1. | shall | 5.3.1 |
| R32 | Clients MUST be able to deal with multiple CMC status info controls. | shall | 5.1 |
| R33 | If dataReturn appears, server MUST return it in response. | shall | 5.4 |
| R34 | Servers MUST process [PKIXCERT] extensions in AddExtensions. | shall | 5.5 |
| R35 | Servers MUST NOT reverse meaning of LRA-requested extension. | shall | 5.5 |
| R36 | If transactionId present, all subsequent messages MUST include same. | shall | 5.6 |
| R37 | Server MUST use only transactionIds in outermost PKIdata. | shall | 5.6 |
| R38 | Clients MUST implement SHA-1 for witnessAlgID and HMAC-SHA1 for thePOPAlgID in encrypted POP. | shall | 5.7 |
| R39 | If CA does not allow LRA POP, return POPFAILURE; CA MUST NOT re-verify. | shall | 5.8 |
| R40 | Clients MUST provide capability to produce digitally signed revocation request. | shall | 5.11 |
| R41 | Clients SHOULD be capable of producing unsigned revocation with shared secret. | should | 5.11 |
| R42 | If client provides self-revocation, MUST produce revocation containing shared secret. | shall | 5.11 |
| R43 | Servers MUST accept both signed and unsigned revocation requests. | shall | 5.11 |
| R44 | Full response message MUST be returned for revocation request. | shall | 5.11 |
| R45 | If confirmRequired, client MUST return Confirm Certificate Acceptance before using certificate. | shall | 5.14 |
| R46 | Servers MUST return full enrollment response for confirm certificate acceptance. | shall | 5.14 |
| R47 | LRA MUST NOT alter any certificate request body. | shall | 6 |
| R48 | CMC clients and servers MUST be capable of DSA signatures and D-H key exchange. | shall | 8.1 |
| R49 | Minimally compliant server MUST accept Full PKI Request (CRMF and PKCS#10), Simple Enrollment, and return Full PKI Response. | shall | 8.2 |
| R50 | Minimally compliant client MUST understand both Simple and Full PKI Responses. | shall | 8.2 |

## Informative Annexes (Condensed)
- **Appendix A: ASN.1 Module**: Provides complete ASN.1 definitions for all structures, OIDs, and types used in the protocol. This is normative for implementation; refer to the original for exact syntax.