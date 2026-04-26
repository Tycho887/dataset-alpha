# RFC 4210: Internet X.509 Public Key Infrastructure Certificate Management Protocol (CMP)
**Source**: IETF | **Version**: Standards Track | **Date**: September 2005 | **Type**: Normative
**Obsoletes**: RFC 2510

## Scope (Summary)
Defines the Internet X.509 Public Key Infrastructure (PKI) Certificate Management Protocol (CMP) for X.509v3 certificate creation and management. Provides on-line interactions between PKI components (e.g., CA and client system). Obsoletes RFC 2510 with enhanced confirmation mechanisms, polling, implicit confirmation, and revised profiles.

## Normative References
- [X509] ISO 9594-8:2001 / ITU-T X.509
- [MvOV97] Menezes et al., Handbook of Applied Cryptography, CRC Press, 1996
- [RFC2104] Krawczyk et al., HMAC: Keyed-Hashing for Message Authentication, RFC 2104, 1997
- [RFC2119] Bradner, S., Key words for use in RFCs to Indicate Requirement Levels, BCP 14, RFC 2119, 1997
- [RFC2202] Cheng & Glenn, Test Cases for HMAC-MD5 and HMAC-SHA-1, RFC 2202, 1997
- [RFC3629] Yergeau, F., UTF-8, a transformation format of ISO 10646, STD 63, RFC 3629, 2003
- [RFC2482] Whistler & Adams, Language Tagging in Unicode Plain Text, RFC 2482, 1999
- [CRMF] Schaad, J., Internet X.509 Public Key Infrastructure Certificate Request Message Format (CRMF), RFC 4211, 2005
- [RFC3066] Alvestrand, H., Tags for the Identification of Languages, BCP 47, RFC 3066, 2001
- [PKCS10] Nystrom & Kaliski, Certification Request Syntax Standard, Version 1.7, RFC 2986, 2000
- [PKCS11] RSA, Cryptographic Token Interface Standard, Version 2.10, 1999
- [ANSI-X9.42] Public Key Cryptography: Agreement of Symmetric Keys Using Discrete Logarithm Cryptography, 2000

## Definitions and Abbreviations
- **End Entity (EE)**: Entity to whom a certificate is issued; may be human user or application.
- **Certification Authority (CA)**: Entity that issues certificates; root CA is directly trusted by EE.
- **Registration Authority (RA)**: Optional entity that performs tasks such as authentication, token distribution, etc.; RA is itself a certified end entity.
- **Personal Security Environment (PSE)**: Secure local storage of EE’s own name, private key, CA name, and CA public key.
- **Certificate Revocation List (CRL)**: Published list of revoked certificates.
- **Proof-of-Possession (POP)**: Demonstration by EE that it possesses the private key corresponding to a requested public key.
- **Initial Authentication Key (IAK)**: Secret value distributed out-of-band to authenticate EE messages.
- **Cross-Certificate**: Certificate where subject CA and issuer CA are distinct.
- **OOBCert / OOBCertHash**: Structures for out-of-band distribution of root CA public key.
- **ProtectedPart**: DER-encoded PKIHeader and PKIBody used for message protection.
- **PKIMessage**: Overall structure: header + body + optional protection + optional extra certificates.
- **CertTemplate**: Requested certificate contents (all fields optional).
- **EncryptedValue**: Used to transport encrypted private keys or certificates.
- **PKIStatus**: Integer status (accepted, grantedWithMods, rejection, waiting, revocationWarning, revocationNotification, keyUpdateWarning).
- **PKIFailureInfo**: BIT STRING with specific failure reasons (badAlg, badPOP, etc.).
- **CertId**: Identifies a particular certificate.
- **PKIPublicationInfo**: Indicates desired publication of a certificate.
- **PKIArchiveOptions**: Request to archive private key.
- **POPOSigningKey**: Structure for proof-of-possession of signing key.
- **POPOPrivKey**: CHOICE for encryption/key agreement key POP (thisMessage, subsequentMessage, dhMAC).
- **Challenge / POPODecKeyChallContent / POPODecKeyRespContent**: Direct POP protocol for decryption keys.
- **CertRepMessage**: Response containing certificates (optionally encrypted).
- **CertConfirmContent**: SEQUENCE OF CertStatus used to accept/reject certificates.
- **GenMsgContent / GenRepContent**: General message/response for info requests.
- **ErrorMsgContent**: Error information with optional error code.
- **PollReqContent / PollRepContent**: Polling mechanism for pending requests.

## Introduction (Summary)
CMP defines on-line PKI management messages for certificate creation and management. This specification obsoletes RFC 2510 with changes including: required/optional profile split, revised confirmation mechanism, polling, transport separation, implicit confirmation, and improved explanatory text.

## Requirements (Section 2)
The key words "MUST", "MUST NOT", "REQUIRED", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

## PKI Management Overview (Section 3)
- **Entities**: End Entity (EE), Certification Authority (CA), Registration Authority (RA – optional).
- **Management Operations** (High-level): CA establishment, end entity initialization, certification (initial, key update, certificate update, CA key update, cross-certification), certificate/CRL discovery, recovery operations, revocation operations, PSE operations.
- **Requirements**: Must conform to X.509; allow regular key updates; minimize confidentiality use; support multiple algorithms; allow key generation by EE, RA, or CA; support publication; support CRL production; usable over multiple transports; final authority rests with CA; support CA key update; RA functions may be performed by CA; EE must prove POP of private key.

## Assumptions and Restrictions (Section 4)
### 4.1 End Entity Initialization
- EE must securely acquire root CA public key and supported PKI functions.

### 4.2 Initial Registration/Certification
- Several schemes classified by initiation, authentication, key generation location, and confirmation. Two mandatory schemes:
  - **Centralized Scheme** (Section 4.2.2.1): CA initiates, no on-line authentication, CA generates keys, no confirmation; single message CA→EE.
  - **Basic Authenticated Scheme** (Section 4.2.2.2): EE initiates, message authentication REQUIRED, EE generates keys, confirmation REQUIRED. Uses IAK out-of-band. Message flow: ir → ip → certConf → pkiConf.

### 4.3 Proof-of-Possession (POP) of Private Key
- **CAs/RAs MUST enforce POP** by some means to verify binding between EE and key pair.
- **Signature Keys**: Sign a value.
- **Encryption Keys**: Provide private key to CA/RA or decrypt a value (direct challenge or indirect encrypted certificate).
- **Key Agreement Keys**: Establish shared secret via DH.
- POP can be verified by RA and attested to CA.

### 4.4 Root CA Key Update
- CA protects new public key with old private key and vice versa. Produces four certificates: OldWithOld, OldWithNew, NewWithOld, NewWithNew.
- Verification scenarios for certificate chains during key update (cases 1-8). Failure occurs if repository not updated properly.

## Data Structures (Section 5)
### 5.1 Overall PKI Message
```
PKIMessage ::= SEQUENCE {
  header           PKIHeader,
  body             PKIBody,
  protection   [0] PKIProtection OPTIONAL,
  extraCerts   [1] SEQUENCE SIZE (1..MAX) OF CMPCertificate OPTIONAL
}
PKIMessages ::= SEQUENCE SIZE (1..MAX) OF PKIMessage
```
- **PKIHeader**: pvno (2 for this spec), sender, recipient, messageTime, protectionAlg, senderKID, recipKID, transactionID, senderNonce, recipNonce, freeText, generalInfo.
  - **transactionID**: Used for correlation; MUST be set in multi-message transactions; clients SHOULD generate 128 bits of random data. Server MUST set response transactionID to same value if present in request; if missing, server MAY generate.
  - **senderNonce/recipNonce**: Protect against replay; senderNonce typically 128 bits; recipNonce copied from previous senderNonce.
  - **ImplicitConfirm** (id-it 13): If EE includes in header, it informs CA it does not wish to send certConf. If CA grants, MUST include same extension in response; otherwise EE MUST send certConf.
  - **ConfirmWaitTime** (id-it 14): CA informs EE how long it will wait for certConf before revoking.

### 5.1.2 PKIBody
- CHOICE of message types (ir, ip, cr, cp, p10cr, popdecc, popdecr, kur, kup, krr, krp, rr, rp, ccr, ccp, ckuann, cann, rann, crlann, pkiconf, nested, genm, genp, error, certConf, pollReq, pollRep).

### 5.1.3 PKI Message Protection
- **PKIProtection** BIT STRING – input is DER of ProtectedPart.
- Three methods:
  - **Shared Secret (PasswordBasedMAC)**: id-PasswordBasedMac with PBMParameter (salt, OWF, iterationCount, mac). Key derivation from BASEKEY.
  - **DH Key Pairs**: id-DHBasedMac with DHBMParameter (owf, mac). Key derived from DH shared secret.
  - **Signature**: AlgorithmIdentifier for digital signature (e.g., md5WithRSA, dsaWithSha1).
- **Multiple Protection**: RA can nest EE messages using NestedMessageContent; must be same type; original message may be included in generalInfo (id-it 15).

### 5.2 Common Data Structures
- **CertTemplate**: All fields optional (from CRMF).
- **EncryptedValue**: For encrypted private keys or certificates.
- **PKIStatusInfo**: status, statusString (optional), failInfo (optional).
- **CertId**: Identifies certificate (from CRMF).
- **OOBCert**: Self-signed certificate for out-of-band root CA key.
- **OOBCertHash**: Hash of self-signed certificate for integrity verification.
- **PKIArchiveOptions** (from CRMF).
- **PKIPublicationInfo** (from CRMF).
- **Proof-of-Possession Structures**:
  - **POPOSigningKey**: For signing keys; poposkInput must be omitted if certTemplate contains both subject and publicKey; otherwise MUST be present.
  - **POPOPrivKey**: For encryption/key agreement keys. Options: thisMessage (encrypted private key), subsequentMessage, dhMAC.
  - **Challenge/Response** (POPODecKeyChallContent / POPODecKeyRespContent) for direct POP.
- Summary of POP options: RAVerified, SKPOP, EKPOPThisMessage, KAKPOPThisMessage, KAKPOPThisMessageDHMAC, EKPOPEncryptedCert, KAKPOPEncryptedCert, EKPOPChallengeResp, KAKPOPChallengeResp.

### 5.3 Operation-Specific Data Structures
- **Initialization Request (ir)**: CertReqMessages.
- **Initialization Response (ip)**: CertRepMessage (caPubs optional, response SEQUENCE OF CertResponse).
- **Certification Request (cr)**: CertReqMessages or PKCS#10 CertificationRequest.
- **Certification Response (cp)**: CertRepMessage.
- **Key Update Request (kur)**: CertReqMessages.
- **Key Update Response (kup)**: CertRepMessage.
- **Key Recovery Request (krr)**: CertReqMessages.
- **Key Recovery Response (krp)**: KeyRecRepContent (status, optional newSigCert, caCerts, keyPairHist).
- **Revocation Request (rr)**: RevReqContent (SEQUENCE OF RevDetails).
- **Revocation Response (rp)**: RevRepContent (status, revCerts, crls).
- **Cross Certification Request (ccr)**: CertReqMessages; key pair MUST be generated by requesting CA; private key MUST NOT be sent to responding CA.
- **Cross Certification Response (ccp)**: CertRepMessage; no encrypted private key.
- **CA Key Update Announcement (ckuann)**: CAKeyUpdAnnContent (oldWithNew, newWithOld, newWithNew).
- **Certificate Announcement (cann)**: CertAnnContent (Certificate).
- **Revocation Announcement (rann)**: RevAnnContent (status, certId, willBeRevokedAt, badSinceDate, crlDetails).
- **CRL Announcement (crlann)**: CRLAnnContent (SEQUENCE OF CertificateList).
- **PKI Confirmation (pkiconf)**: PKIConfirmContent (NULL).
- **Certificate Confirmation (certConf)**: CertConfirmContent (SEQUENCE OF CertStatus). Omission of statusInfo indicates acceptance. Empty sequence indicates rejection of all.
- **General Message (genm)**: GenMsgContent (SEQUENCE OF InfoTypeAndValue). Defined infoTypes include: caProtEncCert (1), signKeyPairTypes (2), encKeyPairTypes (3), preferredSymmAlg (4), caKeyUpdateInfo (5), currentCRL (6), unsupportedOIDs (7), keyPairParamReq/Rep (10/11), revPassphrase (12), implicitConfirm (13), confirmWaitTime (14), origPKIMessage (15), suppLangTags (16).
- **General Response (genp)**: GenRepContent.
- **Error Message (error)**: ErrorMsgContent (pKIStatusInfo, errorCode, errorDetails). If client sends, server MUST respond with PKIConfirm or ErrorMsg. Both sides treat as end of transaction.
- **Polling Request (pollReq)**: PollReqContent (SEQUENCE OF certReqId).
- **Polling Response (pollRep)**: PollRepContent (SEQUENCE OF certReqId, checkAfter, reason). Used when waiting status received; EE waits at least checkAfter seconds before sending next pollReq.

## Mandatory PKI Management Functions (Section 6)
- **Root CA Initialization (6.1)**: Must produce self-certificate (NewWithNew) and OOBCertHash for out-of-band fingerprint.
- **Root CA Key Update (6.2)**: CA issues NewWithNew, NewWithOld, OldWithNew to aid transition.
- **Subordinate CA Initialization (6.3)**: Same as EE initialization; must also produce initial CRL.
- **CRL Production (6.4)**: Before issuing certificates, CA must produce empty CRLs.
- **PKI Information Request (6.5)**: EE MAY send GenMsg to CA to request information; CA MUST respond with GenRep; error if information cannot be provided. Protection using PasswordBasedMAC or other authenticated means.
- **Cross Certification (6.6)**: One-way scheme using authorization code out-of-band. Requesting CA sends ccr with MAC; responder validates and sends ccp; requester sends certConf; responder sends PKIConfirm.
- **End Entity Initialization (6.7)**: Must acquire root CA public key and certification path (if any) and verify root CA public key out-of-band.
- **Certificate Request (6.8)**: EE MAY request additional certificate using cr message; protected by signature if EE has signing key.
- **Key Update (6.9)**: EE requests key update via kur; receives kup (syntactically same as CertRepMessage).

## Version Negotiation (Section 7)
- Client sends highest supported version; server responds with same version if supported. ErrorMsg with unsupportedVersion bit if version not supported. Supports negotiation with RFC 2510 (version cmp1999).

## Security Considerations (Summary)
- **POP with Decryption Key**: Risk of oracle attacks; implementers should be careful about decrypting arbitrary ciphertext.
- **POP by Exposing Private Key**: Caution advised; user should explicitly trust CA/RA before revealing private key.
- **Attack Against Diffie-Hellman Key Exchange**: Small subgroup attack possible; RECOMMENDED that CA generate fresh DH key pair per EE.

## IANA Considerations
- OIDs for general message types were assigned from IANA-delegated arc to PKIX WG. No further IANA action required.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | PKI management MUST conform to ISO/IEC 9594-8/ITU-T X.509 standards. | MUST | 3.1.2 (1) |
| R2 | PKI management protocols MUST allow use of different industry-standard cryptographic algorithms (RSA, DSA, MD5, SHA-1). | MUST | 3.1.2 (4) |
| R3 | PKI management protocols MUST support publication of certificates by EE, RA, or CA. | MUST | 3.1.2 (6) |
| R4 | PKI management protocols MUST support CRL production. | MUST | 3.1.2 (7) |
| R5 | Final authority for certification creation rests with the CA. | MUST | 3.1.2 (9) |
| R6 | CA key pair update shall be supported. | SHALL | 3.1.2 (10) |
| R7 | End entity MUST be ready to demonstrate possession of private key when requesting certificate. | MUST | 3.1.2 (12) |
| R8 | CAs/RAs MUST enforce Proof-of-Possession by some means. | MUST | 4.3 |
| R9 | In Basic Authenticated Scheme, message authentication is REQUIRED and a confirmation message is REQUIRED. | REQUIRED | 4.2.2.2 |
| R10 | The pvno field in PKIHeader is fixed at 2 for this version. | FIXED | 5.1.1 |
| R11 | If no protection bits are supplied, protectionAlg MUST be omitted; if protection bits are supplied, protectionAlg MUST be supplied. | MUST | 5.1.1 |
| R12 | senderKID and recipKID MUST be used if required to uniquely identify a key; SHOULD be omitted otherwise. | MUST/SHOULD | 5.1.1 |
| R13 | For multi-message transactions, clients SHOULD generate transactionID; server MUST set response transactionID to same value if present. | SHOULD/MUST | 5.1.1 |
| R14 | A client MUST NOT have more than one transaction with the same transactionID in progress at any time (to a given server). | MUST | 5.1.1 |
| R15 | For transactions with more than one request/response pair, subsequent messages MUST set transactionID to the established value. | MUST | 5.1.1 |
| R16 | Server receiving first message with duplicate transactionID MUST send ErrorMsgContent with PKIFailureInfo transactionIdInUse. | MUST | 5.1.1 |
| R17 | ImplicitConfirm: if CA grants request, CA MUST put same extension in response header; if EE does not find extension, EE MUST send certConf. | MUST | 5.1.1.1 |
| R18 | All response messages MUST include PKIStatusInfo. | MUST | 5.2.3 |
| R19 | OOBCert MUST be self-signed; subject and issuer fields MUST be identical. | MUST | 5.2.5 |
| R20 | Use of PKIConfirm for certificate confirmation is NOT RECOMMENDED; certConf SHOULD be used instead. | NOT RECOMMENDED / SHOULD | 5.3.17 |
| R21 | Error message: if client sends, server MUST respond with PKIConfirm or another ErrorMsg. Both sides MUST treat as end of transaction. | MUST | 5.3.21 |
| R22 | CA MUST produce "empty" CRLs before issuing any certificates. | MUST | 6.4 |
| R23 | CA MUST respond to PKI information request with at least all requested information; if not possible, error MUST be conveyed. | MUST | 6.5 |
| R24 | In cross certification, key pair MUST have been generated by requesting CA and private key MUST NOT be sent to responding CA. | MUST | 5.3.11, 6.6.1 |
| R25 | All end entities MUST be prepared to provide POP. | MUST | Appendix D.3 |
| R26 | PasswordBasedMAC on revocation request is MANDATORY to support if revocation requests are supported and shared secret information can be established. | MANDATORY | Appendix B |
| R27 | For POPOSigningKey: if certTemplate contains both subject and publicKey, poposkInput MUST be omitted and signature computed on CertReqMsg certReq. | MUST | Appendix C |
| R28 | In initial registration (Basic Authenticated), EE MUST include all CertReqMsg in a single PKIMessage; PKI MUST produce a single response. | MUST | Appendix D.4 |

## Informative Annexes (Condensed)
- **Appendix A (Reasons for RAs)**: Lists technical and organizational reasons for using an RA (e.g., token initialization, revocation request signing, cost efficiency).
- **Appendix B (Use of Revocation Passphrase)**: Describes optional mechanism to establish shared secret (revocation passphrase) for authenticating revocation requests when private key is unavailable. Encrypted passphrase may be sent in GenMsg or PKIHeader generalInfo.
- **Appendix C (Request Message Behavioral Clarifications)**: Provides clarifications to CRMF for use in CMP, including conditions for POPOSigningKey input and encoding of POPOPrivKey.thisMessage.
- **Appendix D (PKI Management Message Profiles – REQUIRED)**: Defines mandatory profiles for initial registration/certification (Basic Authenticated), certificate request, and key update. Specifies algorithm use (MSG_SIG_ALG, MSG_MAC_ALG, SYM_PENC_ALG, PROT_ENC_ALG, PROT_SYM_ALG) with mandatory DSA/SHA-1 for signature, PasswordBasedMac for MAC, 3-DES for symmetric encryption, D-H for asymmetric encryption. Includes detailed message field tables.
- **Appendix E (PKI Management Message Profiles – OPTIONAL)**: Profiles for root CA key update, information request/response, cross-certification (1-way), and in-band initialization using external identity certificate.
- **Appendix F (Compilable ASN.1 Definitions)**: Full ASN.1 module for CMP including all types defined in the specification.
- **Appendix G (Acknowledgements)**: Thanks to IETF PKIX WG and ICSA CA-talk list contributors.