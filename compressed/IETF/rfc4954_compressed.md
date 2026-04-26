# RFC 4954: SMTP Service Extension for Authentication
**Source**: IETF | **Version**: Standards Track | **Date**: July 2007 | **Type**: Normative
**Original**: http://www.ietf.org/rfc/rfc4954.txt

## Scope (Summary)
Defines an SMTP extension that allows a client to authenticate to a server using SASL, optionally negotiate a security layer, and include an authorization identity in the MAIL FROM command. Obsoletes RFC 2554.

## Normative References
- [ABNF] RFC 4234
- [BASE64] RFC 4648
- [ESMTP-CODES] RFC 2034
- [ENHANCED] RFC 3463
- [ESMTP-DSN] RFC 3461
- [KEYWORDS] RFC 2119 (BCP 14)
- [SASL] RFC 4422
- [SASLprep] RFC 4013
- [SMTP] RFC 2821
- [SMTP-TLS] RFC 3207
- [StringPrep] RFC 3454
- [SUBMIT] RFC 4409
- [SMTP-TT] RFC 3848
- [PLAIN] RFC 4616
- [X509] RFC 3280

## Definitions and Abbreviations
- **SASL**: Simple Authentication and Security Layer (RFC 4422)
- **AUTH**: EHLO keyword and SMTP command for authentication
- **BASE64**: encoding per RFC 4648
- **xtext**: encoding per RFC 3461 Section 4
- **initial-response**: optional first client response in AUTH command
- **cancel-response**: single "*" to abort authentication
- **continue-req**: server challenge in 334 reply
- **auth-param**: AUTH= parameter on MAIL FROM
- **authorization identity**: identity derived from successful AUTH command
- **authenticated identity**: identity from AUTH (authorization identity)
- **authorized identity**: mailbox associated with a message (MAIL FROM AUTH parameter)

## 1. Introduction
This document defines an SMTP extension for authentication using SASL. It deprecates response code 538, adds enhanced status codes, requires SASLprep for authorization identities, recommends RFC 3848 transmission types, and clarifies interaction with PIPELINING.

## 2. How to Read This Document
Keywords (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL) are interpreted as described in RFC 2119. In examples, "C:" and "S:" denote client and server lines.

## 3. The Authentication Service Extension
1. **Name**: Authentication
2. **EHLO keyword**: AUTH
3. **AUTH parameter**: space-separated list of SASL mechanisms (may change after STARTTLS)
4. **New verb**: AUTH
5. **MAIL FROM parameter**: AUTH= , extends MAIL FROM max line length by 500 characters
6. **Appropriate for**: SUBMIT protocol

## 4. The AUTH Command
### 4.1 AUTH Command Specification
- **Arguments**: mechanism (SASL mechanism name), initial-response (optional, encoded per BASE64 or "=")
- **Restrictions**:
  - Only one successful AUTH per session; further AUTH commands MUST be rejected with 503.
  - AUTH not permitted during a mail transaction; if attempted, MUST be rejected with 503.
- **Discussion**:
  - Server challenge: 334 reply with BASE64 text (no extra text).
  - Client response: BASE64 line, or "*" to cancel (server MUST reject with 501).
  - Initial response saves round-trip; if omitted and mechanism requires initial response, server proceeds per SASL Section 5.1 (empty challenge = "334 ").
  - If initial-response would exceed line length, client MUST NOT use it.
  - Zero-length initial response transmitted as "=".
  - If mechanism doesn't begin with client, server MUST reject AUTH with 501 (enhanced 5.7.0 SHOULD).
  - BASE64 errors: client cancels with "*", server rejects with 501 (enhanced 5.5.2 SHOULD).
  - Invalid BASE64 pad character: MUST reject.
  - Clients/servers MUST handle maximum encoded sizes (12288 octets considered sufficient). Buffer overflow -> 500 (enhanced 5.5.6 SHOULD).
  - Authorization identity MUST be prepared using SASLprep; if preparation fails or results in empty string (unless intentionally empty), server MUST fail authentication. (SHOULD; future revision may be MUST.)
  - Authentication failure: server SHOULD reject with 535 (unless more specific code).
  - Success: server issues 235.
  - Security layer takes effect after CRLF of last client response (client end) and after CRLF of success reply (server end).
  - After security layer established: SMTP state reset (client discards server capabilities, server discards client info). Client SHOULD send EHLO after security layer.
  - If both TLS and SASL security layers, TLS encoding applied after SASL encoding.
  - Service name: "smtp" (also for SUBMIT).
  - On failure, client may proceed without authentication or try another mechanism.
  - Server MUST implement a configuration that prohibits plaintext password mechanisms unless STARTTLS or equivalent protection is in place. Sites SHOULD NOT use such configurations without protection.
  - Mandatory-to-implement: SASL PLAIN over TLS (client and server).
  - CRAM-MD5 MAY be implemented for interoperability; note no server authentication.
  - When used with PIPELINING: AUTH MUST be last command in a pipelined group, unless (a) contains initial response, (b) mechanism allows client data first, (c) completes in one round-trip, (d) no security layer negotiated. Examples: PLAIN, EXTERNAL.
- **Examples**: Provided for PLAIN, CRAM-MD5, EXTERNAL (see Annex).

## 5. The AUTH Parameter to the MAIL FROM command
- **Syntax**: AUTH= (xtext encoding of mailbox or "<>")
- **Purpose**: Communicate authorization identity of message submitter.
- **Server requirements**:
  - MUST support AUTH parameter even if client not authenticated.
  - If server trusts authenticated identity, it SHOULD propagate the same mailbox via AUTH parameter when relaying.
  - AUTH=<> indicates submitter unknown.
  - If AUTH parameter omitted, server MAY generate mailbox from authenticated identity; if cannot generate valid mailbox, MUST transmit AUTH=<>.
  - If client not authenticated or not trusted, server MUST behave as if AUTH=<> supplied (may log actual value).
  - If AUTH=<> supplied (explicit or implicit), server MUST supply AUTH=<> when relaying to authenticated servers.
  - Mailing list expansion may be treated as new submission, setting AUTH to list address.
  - Hard-coded untrusted clients are compliant.
- **Examples**: Provided in Section 5.1.

## 6. Status Codes
| Reply | Enhanced | Meaning | Action |
|-------|----------|---------|--------|
| 235 | 2.7.0 | Authentication succeeded | - |
| 432 | 4.7.12 | Password transition needed | Use PLAIN once then new mechanism |
| 454 | 4.7.0 | Temporary authentication failure | Do not prompt user |
| 534 | 5.7.9 | Mechanism too weak | Retry with stronger mechanism |
| 535 | 5.7.8 | Invalid credentials | Ask user for new credentials |
| 500 | 5.5.6 | Authentication line too long | - |
| 530 | 5.7.0 | Authentication required | Returned for commands other than AUTH/EHLO/HELO/NOOP/RSET/QUIT when auth needed |
| 538 | 5.7.11 | Encryption required (historical) | Should not advertise mechanisms without encryption |

New enhanced status codes: 5.7.8, 5.7.9, 5.7.11, and X.5.6 (for line length errors).

## 7. Additional Requirements on Servers
Upon successful authentication, server SHOULD use "ESMTPA" or "ESMTPSA" (if TLS) in the "with" clause of the Received header field (per RFC 3848).

## 8. Formal Syntax
Using ABNF (RFC 4234). Key ABNF productions: auth-command, auth-param, base64, continue-req, initial-response, cancel-response, xtext, hexchar, xchar. All alphabetic characters are case-insensitive. Implementations MUST accept in case-insensitive fashion.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Only one AUTH per session; subsequent AUTH MUST be rejected with 503 | MUST | Section 4 |
| R2 | AUTH not permitted during mail transaction; if attempted MUST be rejected with 503 | MUST | Section 4 |
| R3 | Server MUST reject AUTH with 501 if client sends "*" to cancel | MUST | Section 4 |
| R4 | Server MUST reject AUTH with 501 if initial-response used with mechanism that doesn't start with client | MUST | Section 4 |
| R5 | Server MUST reject AUTH with 501 if BASE64 decoding fails | MUST | Section 4 |
| R6 | Server MUST reject AUTH with 500 if line exceeds authentication buffer | MUST | Section 4 |
| R7 | Server MUST fail authentication if SASLprep preparation fails or results in empty string (unless empty sent) | MUST | Section 4 |
| R8 | Server MUST implement configuration that does not permit plaintext password mechanisms without STARTTLS or equivalent | MUST | Section 4 |
| R9 | Client and server MUST implement SASL PLAIN over TLS | MUST | Section 4 |
| R10 | AUTH MUST be last command in pipelined group except when initial-response, one round-trip, no security layer, client sends first | MUST | Section 4 |
| R11 | Server MUST support AUTH parameter on MAIL FROM even if client not authenticated | MUST | Section 5 |
| R12 | If server trusts authenticated identity, it SHOULD supply same mailbox in AUTH parameter when relaying | SHOULD | Section 5 |
| R13 | If client not authenticated/trusted, server MUST behave as if AUTH=<> supplied | MUST | Section 5 |
| R14 | If AUTH=<> supplied (explicit or implicit), server MUST supply AUTH=<> when relaying to authenticated servers | MUST | Section 5 |
| R15 | Client MUST NOT use SASL PLAIN over TLS if server certificate verification fails | MUST | Section 14 |
| R16 | Client MUST check server hostname against certificate after TLS; if mismatch, MUST NOT use SASL PLAIN | MUST | Section 14 |
| R17 | Server SHOULD use "ESMTPA"/"ESMTPSA" in Received header after authentication | SHOULD | Section 7 |
| R18 | Server SHOULD reject with 535 on authentication failure unless more specific code | SHOULD | Section 4 |
| R19 | Client SHOULD send EHLO after security layer established | SHOULD | Section 4 |
| R20 | Authorization identity SHOULD be prepared with SASLprep | SHOULD | Section 4 |
| R21 | Server SHOULD NOT drop connection until at least 3 failed auth attempts if implementing such policy | SHOULD | Section 9 |

## Security Considerations (Condensed)
- Clients must be configured to use authentication only over mutually authenticated encrypted connections to avoid hijacking.
- Before SASL negotiation, protocol is in clear; upon establishing security layer, all prior knowledge MUST be discarded.
- Active attacker may redirect MTA connection to submission port; AUTH=<> prevents relay hijacking.
- Submission servers may choose not to advertise SASL mechanisms that grant no benefit.
- Servers MAY drop connection after failed attempts, but not before at least 3 attempts.
- If SASL mechanisms vulnerable to eavesdropping are supported, must have configuration to not advertise without external security layer (e.g., TLS).
- Does not replace end-to-end signature/encryption (S/MIME, PGP); protects envelope, authenticates submission, not authorship; mutual authentication + security layer gives assurance of next-hop delivery.

## Informative Annexes (Condensed)
- **14. Additional Requirements When Using SASL PLAIN over TLS** (Normative for PLAIN+TLS implementations): Client MUST verify server certificate per X.509; if verification fails, MUST NOT attempt PLAIN. Hostname matching: use server hostname from connection (not from insecure DNS), compare against dNSName (case-insensitive, wildcard leftmost component only). Multiple names: match any one. CNAME canonicalization not done.
- **15. Changes since RFC 2554**: Listed 13 changes: clarified AUTH= support for unauthenticated clients, initial-client-send, updated references, mandatory PLAIN over TLS, mechanism list changeability, deprecated 538, SASLprep, cleanup of response codes, ABNF update, PIPELINING clarification, RFC 3848 reference, new enhanced status code for line length, editorial clarifications.
- **Examples** (from Section 4.1): Provided in original; not reproduced here but represent typical usage.