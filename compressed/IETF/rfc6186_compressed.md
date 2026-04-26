# RFC 6186: Use of SRV Records for Locating Email Submission/Access Services
**Source**: IETF | **Version**: Standards Track | **Date**: March 2011 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6186

## Scope (Summary)
This specification defines new DNS SRV service labels for message submission (SMTP), IMAP, and POP3 to enable automatic configuration of Mail User Agents (MUAs) using minimal user input (typically an email address). It also uses the SRV priority field to indicate domain preferences between IMAP and POP3.

## Normative References
- [RFC1939] Myers, J. and M. Rose, "Post Office Protocol - Version 3", STD 53, RFC 1939, May 1996.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2595] Newman, C., "Using TLS with IMAP, POP3 and ACAP", RFC 2595, June 1999.
- [RFC2782] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [RFC3207] Hoffman, P., "SMTP Service Extension for Secure SMTP over Transport Layer Security", RFC 3207, February 2002.
- [RFC3501] Crispin, M., "INTERNET MESSAGE ACCESS PROTOCOL - VERSION 4rev1", RFC 3501, March 2003.
- [RFC4409] Gellens, R. and J. Klensin, "Message Submission for Mail", RFC 4409, April 2006.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5321] Klensin, J., "Simple Mail Transfer Protocol", RFC 5321, October 2008.
- [RFC5322] Resnick, P., Ed., "Internet Message Format", RFC 5322, October 2008.
- [RFC6066] Eastlake, D., "Transport Layer Security (TLS) Extensions: Extension Definitions", RFC 6066, January 2011.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.

## Definitions and Abbreviations
- **SRV RR**: DNS resource record for service location, defined in [RFC2782].
- **MUA**: Mail User Agent.
- **MSA**: Mail Submission Agent.
- **submission**: Service label for message submission per [RFC4409] (covers both plain and STARTTLS).
- **_imap**: SRV label for IMAP server that MAY advertise LOGINDISABLED and MAY require STARTTLS prior to authentication.
- **_imaps**: SRV label for IMAP server where TLS is initiated directly upon connection.
- **_pop3**: SRV label for POP3 server that MAY require STLS extension command prior to authentication.
- **_pop3s**: SRV label for POP3 server where TLS is initiated directly upon connection.

## 1. Introduction (Condensed)
Email protocols (SMTP, IMAP, POP3) require MUAs to locate servers. Traditionally, users manually enter FQDN and port, leading to errors. [RFC2782] defines SRV records for service discovery. This specification defines SRV service labels for submission, IMAP, and POP3, enabling auto-configuration from the user's email address.

## 2. Conventions Used in This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in [RFC2119].

## 3. SRV Service Labels
### 3.1. Email Submission
- **Service label**: `_submission._tcp` identifies an MSA using [RFC4409].
- Example: `_submission._tcp SRV 0 1 587 mail.example.com.`

### 3.2. IMAP
- **_imap.**_tcp: IMAP server; MAY require STARTTLS prior to authentication.
- **_imaps._tcp**: IMAP server with direct TLS connection.
- Example: `_imap._tcp SRV 0 1 143 imap.example.com.`
- Example: `_imaps._tcp SRV 0 1 993 imap.example.com.`

### 3.3. POP3
- **_pop3._tcp**: POP3 server; MAY require STLS extension prior to authentication.
- **_pop3s._tcp**: POP3 server with direct TLS connection.
- Example: `_pop3._tcp SRV 0 1 110 pop3.example.com.`
- Example: `_pop3s._tcp SRV 0 1 995 pop3.example.com.`

### 3.4. Priority for Domain Preferences
- **Requirement**: Sites SHOULD offer both IMAP (_imap and/or _imaps) and POP3 (_pop3 and/or _pop3s) SRV records.
- **Requirement**: Sites SHOULD set priority such that preferred service has lower-numbered priority.
- **Requirement**: When MUA supports both IMAP and POP3, it SHOULD retrieve records for both and use service with lowest priority. If priority equal, MUA MAY choose either.
- **Requirement**: When multiple records for different protocols have same priority but different weights, client MUST first select protocol, then perform weight selection per [RFC2782] on records of that protocol.
- **Requirement**: If an SRV RR has target "." (indicating service not available), clients MUST assume that service is not available and use other SRV RRs for domain preference.

## 4. Guidance for MUAs
- **Requirement**: MUA MUST extract domain from user's email address and perform SRV lookups for desired services.
- **Requirement**: If SRV lookup fails, MUA SHOULD prompt user for FQDN/port or use other heuristic.
- **Requirement**: MUA MUST use priority and weight fields to select among multiple SRV records (per [RFC2782]).
- **Requirement**: MUAs supporting both POP3 and IMAP MUST follow Section 3.4 for service selection.
- **Requirement**: For TLS connections:
  - `_imaps`/`_pop3s`: TLS negotiation immediately upon connection.
  - `_imap`/`_pop3`/`_submission`: Use STARTTLS/STLS/STARTTLS respectively.
  - MUAs SHOULD use TLS Server Name Indication [RFC6066].
  - **Requirement**: Certificate verification MUST use procedure in Section 6 of [RFC6125] with SRV RR as starting point.
- **Requirement**: When user identifier required for authentication, MUA MUST first use full email address; if fails, SHOULD fall back to local-part. If both fail, MUA SHOULD prompt for valid identifier.
- **Requirement**: MUAs SHOULD cache successfully used service details (hostname, port, user identity).
- **Requirement**: If subsequent connection or authentication fails, MUAs SHOULD re-try SRV lookup for same protocol originally used; MUST NOT change from IMAP to POP3 (or vice versa) due to SRV priority changes without user interaction.

## 5. Guidance for Service Providers
- **Requirement (a)**: Servers SHOULD allow authentication with email address or email local-part. If using email addresses, they MUST NOT conflict with other login names. If using local-parts, they MUST be unique and MUST NOT conflict with other login names.
- **Requirement (b)**: If using TLS, service provider MUST install certificate verifiable per Section 6 of [RFC6125] with SRV RR. If hosting multiple domains on same IP, MUST enable TLS Server Name Indication [RFC6066].
- **Requirement (c)**: Install appropriate SRV records for offered services.

## 6. Security Considerations
- **Requirement**: If user explicitly requests transport layer security (e.g., "use SSL"), MUA MUST successfully negotiate TLS prior to sending authentication command.
- **Requirement**: MUAs SHOULD check that target FQDN in SRV record matches queried domain; if not in that domain, MUAs SHOULD verify with user.
- **Requirement**: If TLS is used for email service, MUAs MUST use Section 6 of [RFC6125] to verify service.
- **Requirement**: Email clients and servers MUST NOT request, offer, or use SSL 2.0 (see [RFC5246] Appendix E.2).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Sites SHOULD offer both IMAP and POP3 SRV records; SHOULD set priority to indicate preference. | SHOULD | Section 3.4 |
| R2 | MUA supporting both IMAP and POP3 SHOULD retrieve both and use service with lowest priority. | SHOULD | Section 3.4 |
| R3 | When multiple records for different protocols have same priority, client MUST first select protocol then apply weight selection. | MUST | Section 3.4 |
| R4 | If SRV target is ".", client MUST assume service not available. | MUST | Section 3.4 |
| R5 | MUA MUST use priority and weight per [RFC2782] for multiple SRV records. | MUST | Section 4 |
| R6 | MUA MUST extract domain from email address for SRV lookups. | MUST | Section 4 |
| R7 | Certificate verification MUST use Section 6 of [RFC6125] with SRV RR. | MUST | Section 4 |
| R8 | MUA MUST first use full email address for authentication; fall back to local-part if fails; prompt if both fail. | MUST/SHOULD | Section 4 |
| R9 | MUAs SHOULD cache successful service details; on failure re-try SRV lookup for same protocol. | SHOULD/MUST NOT | Section 4 |
| R10 | Service providers SHOULD allow authentication with email address or local-part; if using email addresses, MUST NOT conflict; local-parts MUST be unique. | MUST/SHOULD | Section 5 |
| R11 | If using TLS, provider MUST install verifiable certificate; if multi-domain, MUST enable SNI. | MUST | Section 5 |
| R12 | MUA MUST negotiate TLS before authentication if user requested secure connection. | MUST | Section 6 |
| R13 | MUAs SHOULD verify target FQDN if not in queried domain; if TLS used, MUST verify per [RFC6125]. | SHOULD/MUST | Section 6 |
| R14 | Email clients and servers MUST NOT request/offer/use SSL 2.0. | MUST | Section 6 |
| R15 | MUAs SHOULD use TLS Server Name Indication. | SHOULD | Section 4 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 6)**: Detailed guidance on DNS spoofing, certificate verification, and prohibition of SSL 2.0.
- **Acknowledgments**: Thanks to various individuals for feedback.