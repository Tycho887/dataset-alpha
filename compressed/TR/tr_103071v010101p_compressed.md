# ETSI TR 103 071: Registered Electronic Mail (REM); Test suite for future REM interoperability test events
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2011-09 | **Type**: Informative Technical Report  
**Original**: DTR/ESI-000070, keywords: email, interoperability, testing, trust services

## Scope (Summary)
Defines test suites for interoperability testing of Registered Electronic Mail as per TS 102 640 parts 1–6. Tests are layered: evidence formats, REM-MD envelope formats (S/MIME on SMTP and SOAP on HTTP), REM-MD signatures, and complete REM object flows. Both positive and negative tests are included for intra-REM-MD, cross-REM-MD, and REM-MD/UPU interoperability scenarios.

## Normative References
- Not applicable (this TR cites no normative references).

## Informative References
- [i.1] ETSI TS 102 640-1: REM Architecture.
- [i.2] ETSI TS 102 640-2: REM Data requirements, Formats and Signatures.
- [i.3] ETSI TS 102 640-3: REM Information Security Policy Requirements.
- [i.4] ETSI TS 102 640-4: REM-MD Conformance Profiles.
- [i.5] ETSI TS 102 640-5: REM-MD Interoperability Profiles.
- [i.6] ETSI TS 102 640-6: REM Interoperability Profiles.

## Abbreviations
- DO: Designated Operator
- QES: Qualified Electronic Signature
- REM-MD: Registered Electronic Mail Management Domain
- SAML: Security Assertion Markup Language
- SMTP: Simple Mail Transfer Protocol

## 4 Testing Evidence Formats
Defines test cases for each evidence type using a tabular form. Each row specifies one test case with columns for optional/conditional components (eventReasons, evidenceIssuerPolicyID, senderAuthenticationDetails, recipientAuthenticationDetails, recipientsDelegateDetails, TransactionLogInformation, Extensions, Signature, Notification tag). Tables indicate presence/absence and remarks. Test identifier pattern: EVF-[EvidenceTypeAcronym]-[number].

### 4.1 senderAuthenticationDetails component
| Test ID | Trigger Event | senAuthDet | Purpose |
|---|---|---|---|
| EVF-AUT-001 | Acceptance of Message by REM-MD | Basic, Enhanced, Strong, or SAML token | Check senderAuthenticationDetails when no signature used for authenticating sender. |
| EVF-AUT-002 | Acceptance of Message by REM-MD | AdES, AdES-Plus, or QES (no sig in evidence) | Check senderAuthenticationDetails when signature used but not present in evidence. |
| EVF-AUT-003 | Acceptance of Message by REM-MD | AdES, AdES-Plus, or QES (sig included in AdditionalDetails) | Check senderAuthenticationDetails when signature used and present in evidence. |

### 4.2 recipientAuthenticationDetails component
| Test ID | Trigger Event | recAuthDet | Purpose |
|---|---|---|---|
| EVF-AUT-004 | Retrieval by recipient | Basic, Enhanced, Strong, or SAML token | Check recipientAuthenticationDetails when no signature for authenticating sender. |
| EVF-AUT-005 | Retrieval by recipient | AdES, AdES-Plus, or QES (no sig) | Check recipientAuthenticationDetails when signature used but not present. |
| EVF-AUT-006 | Retrieval by recipient | AdES, AdES-Plus, or QES (sig included) | Check recipientAuthenticationDetails when signature used and present. |

### 4.3 SubmissionAcceptanceRejection evidence
| Test ID | Trigger Event | evR | evIsPolID | senAuthDet | repTo | Purpose |
|---|---|---|---|---|---|---|
| EVF-SUBACC-001 | Acceptance | – | – | – | – | Check acceptance evidence (same as EVF-AUT-001). |
| EVF-SUBACC-002 | Rejection (invalid format) | 1 | – | – | – | Check rejection due to invalid format. |
| EVF-SUBACC-003 | Rejection (malware) | 1 | – | – | – | Check rejection due to malware. |
| EVF-SUBACC-004 | Rejection (unaccepted attachment) | 1 | – | – | – | Check rejection due to attachment format not accepted. |
| EVF-SUBACC-005 | Rejection (invalid sender signature) | 1 | – | – | – | Check rejection due to invalid sender's signature. |
| EVF-SUBACC-006 | Rejection (certificate revoked/expired) | 1 | – | – | – | Check rejection due to sender's certificate revoked or expired. |

(Note: 1 indicates presence with standard authentication as per TS 102 640-2.)

### 4.4 RelayREMMDAcceptanceRejection evidence
Analogous structure with trigger events: acceptance, rejection due to invalid format, malware, invalid signature, expired/revoked certificate, policy violation. Test IDs EVF-RELACC-001 to EVF-RELACC-006.

### 4.5 RelayREMMDFailure evidence
Test IDs EVF-RELFAL-001 to EVF-RELFAL-004 covering failure reasons: no identification of recipient REM-MD, unreachable, malfunction, unknown recipient.

### 4.6 DeliveryNonDeliveryToRecipient evidence
Test IDs EVF-DELREC-001 to EVF-DELREC-009 covering successful delivery, failures (timeout, invalid format, mailbox full, technical malfunction, unaccepted attachment, retention expired, notification delivery), and delegate delivery.

### 4.7 DownloadNonDownloadByRecipient evidence
Test IDs EVF-DOWNREC-001 to EVF-DOWNREC-008 covering successful download, failures (timeout, invalid format, malfunction, unaccepted attachment, retention expired, rejection), and delegate download.

### 4.8 RetrievalNonRetrievalByRecipient evidence
Test IDs EVF-RETRREC-001 to EVF-RETRREC-008 covering successful retrieval, failures (invalid format, malware, malfunction, unaccepted attachment, retention expired), delegate retrieval, and notification retrieval.

### 4.9 AcceptanceRejectionByRecipient evidence
Test IDs EVF-ACRECREC-001 to EVF-ACRECREC-004 covering acceptance/rejection by recipient, acceptance/rejection by delegate, and acceptance of notification.

### 4.10 RelayToNonREMSystem evidence
Test IDs EVF-RELNREM-001 to EVF-RELNREM-007 for successful relay, failures (unreachable, non operational, relay rejected) and printing failures (unreachable, non operational, buffer full).

### 4.11 ReceivedFromNonREMSystem evidence
Test ID EVF-RECNREM-001 for successful reception from regular e-mail.

## 5 Testing REM-MD Envelope Formats
Two sets: S/MIME on SMTP (clause 5.1) and SOAP on HTTP (clause 5.2). Test IDs: MSGF-... for SMTP, XMSGF-... for SOAP.

### 5.1 S/MIME on SMTP
Test cases for envelope headers and sections (Introduction, Evidence, Original Message, combinations). Tables indicate presence of optional headers (X-REM-Msg-Type, X-REM-Section-Type) and sections. Test IDs:
- MSGF-INTR-001 to MSGF-INTR-004: Introduction section tests.
- MSGF-EVD-001 to MSGF-EVD-009: Evidence section(s) in XML, ASN.1, or PDF.
- MSGF-ORM-001 to MSGF-ORM-004: Original Message section.
- MSGF-ORM&EVD-001 to MSGF-ORM&EVD-012: Original Message + Evidence combination.
- MSGF-INTR&EVD-001 to MSGF-INTR&EVD-009: Introduction + Evidence (for Store & Notify).

### 5.2 SOAP on HTTP
Test cases for `<REMDispatch>` and `<REMMDMessage>`:
- XMSGF-ORM-001 to XMSGF-ORM-010: `<REMDispatch>` without evidence, testing optional elements like DeliveryConstraints, multiple recipients, In-Reply-To, References, attachments.
- XMSGF-ORM&EVD-001 to XMSGF-ORM&EVD-005: `<REMDispatch>` with evidence.
- XMSGF-EVD-001 to XMSGF-EVD-011: `<REMMDMessage>` with one or two evidence sections.

## 6 Testing REM-MD Signatures
Tests for XAdES signatures on evidence, S/MIME (CAdES) on envelopes, and XAdES on SOAP envelopes.

### 6.1 Individual Evidence Signatures (XAdES)
Test IDs SIG-EVXADES-1 to SIG-EVXADES-4, testing presence of SignaturePolicyIdentifier and SignatureTimeStamp properties. All include SigningCertificate and SigningTime.

### 6.2 S/MIME Signatures (CAdES)
Test IDs SIG-SMIME-1 to SIG-SMIME-6, testing signature-policy-identifier and signature-time-stamp attributes. S/MIME envelopes may contain original message and/or evidence (not individually XAdES-signed).

### 6.3 XAdES on SOAP REM-MD Envelope
Test IDs SIG-XADESSOAP-1 to SIG-XADESSOAP-7, testing signature on `<REMDispatch>` with/without attachment and evidence (signed or unsigned). Properties include SigningCertificate, SigningTime, SignaturePolicyIdentifier, SignatureTimeStamp.

## 7 Testing REM Objects Flows
Test cases for complete flows within same REM-MD (intra), between REM-MD and non-REM systems, and across different REM-MDs. Test ID pattern: OF-[systems][mode][evidence set][recipient]-number.

### 7.1 Intra REM-MD Objects Flows
#### 7.1.1 Store and Forward Mode
- **Mandatory evidence set** `{SubAccRej, DelivNonDeliv}`: Tables 27–29 for one recipient, several recipients, delegate delivery. Test IDs OF-ISF-ME-ONER-1 to ONER-12, SEVR-1 to SEVR-12, RDEL-1 to RDEL-12.
- **Mandatory + optional evidence set** `{SubAccRej, DelivNonDeliv, RetrNonRetr}`: Table 30 (one recipient), Test IDs OF-ISF-MOE-ONER-1 to ONER-5.
- **Mandatory + optional `{SubAccRej, DelivNonDeliv, AccRejRec}`**: Tables 31–32 (one and several recipients), Test IDs OF-ISF-MOE-ONER-1 to ONER-3, SEVR-1 to SEVR-3.

#### 7.1.2 Store and Notify Mode
- **Mandatory evidence set** `{SubAccRej, DownNonDown}`: Tables 33–35 for one recipient, several recipients, delegate. Test IDs OF-ISN-ME-ONER-1 to ONER-12, SEVR-1 to SEVR-8, RDEL-1 to RDEL-6.
- **Mandatory + optional `{SubAccRej, AccRejRec}`**: Tables 36–37 (one and several recipients), Test IDs OF-ISN-MOE-ONER-1 to ONER-2, SEVR-1 to SEVR-1.

### 7.2 Object Flows between REM-MD and Non REM System
Table 38: Flows from REM-MD to regular e-mail (Store and Forward) – test IDs OF-SFTNR-MOE-ONER-1 to -2_x, SEVR-1; from regular e-mail to REM-MD – OF-SFNR-MOE-ONER-1, SEVR-1. Table 39: Relaying to printing systems – OF-SFTPR-MOE-ONER-1, -2_x.

### 7.3 Cross REM-MD Objects Flows
Tables 40–52. Test ID pattern: COF-... for cross. Subsections:
- 7.3.1: Both REM-MDs Store and Forward – Tables 41–44 for delivery, delegate, several recipients, acceptance/rejection.
- 7.3.2: Recipient's REM-MD Store and Notify – Tables 45–48 for download, delegate, several recipients, acceptance/rejection.
- 7.3.3: Sender's REM-MD Store and Notify – Tables 49–52 for download, delegate, several recipients, acceptance/rejection.

All test cases include purpose and cross-references to evidence test cases (e.g., EVF-...).

## 8 Test Suite for REM-MD UPU PReM Interoperability Profile
Defined in clause 6 (placeholder for clause 8). Two sets:
- 8.1: Sender subscribed to REM-MD, recipient to UPU DO (Table 54). Test IDs UPUG-REM2DO-ONER-DEL-1 to -DEL-6_x, SEVR variants.
- 8.2: Sender subscribed to UPU DO, recipient to REM-MD (Table 55). Test IDs UPUG-DO2REM-ONER-DEL-1 to -DEL-5_x, SEVR variants.

Each table describes incoming/outgoing objects on both sides of the gateway, with evidence types (e.g., E-DSP-ACC/REJ-DOD, RelREMMD, RetrNonRetr).

## Requirements Summary
Since the document defines a test suite, the "requirements" are the test cases themselves. A full enumeration would exceed space. The above tables list all test identifiers. Implementers shall select appropriate subsets per their scope. No additional normative requirements beyond those implied by the referenced standards.