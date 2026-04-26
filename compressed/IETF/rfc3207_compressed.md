# RFC 3207: SMTP Service Extension for Secure SMTP over Transport Layer Security
**Source**: IETF (Standards Track) | **Version**: Obsoletes RFC 2487 | **Date**: February 2002 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3207

## Scope (Summary)
Defines the STARTTLS extension to SMTP (RFC 2821) that enables SMTP servers and clients to use TLS (RFC 2246) for private, authenticated communication over the Internet, protecting against eavesdropping and attacks.

## Normative References
- RFC 2119 – Key words for requirement levels
- RFC 2821 – Simple Mail Transfer Protocol
- RFC 2034 – SMTP Service Extension for Returning Enhanced Error Codes
- RFC 2476 – Message Submission
- RFC 2222 – Simple Authentication and Security Layer (SASL)
- RFC 2554 – SMTP Service Extension for Authentication
- RFC 2246 – The TLS Protocol Version 1.0

## Definitions and Abbreviations
- **SMTP**: Simple Mail Transfer Protocol
- **TLS**: Transport Layer Security (also known as SSL)
- **STARTTLS**: The ESMTP keyword and command defined by this extension
- **Publicly-referenced SMTP server**: An SMTP server running on port 25 of a host listed in the MX or A record for the domain on the right-hand side of an Internet mail address
- **MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL**: As defined in RFC 2119

## 1. Introduction
SMTP (RFC 2821) normally sends data in clear text; TLS enhances TCP with privacy and authentication. This document obsoletes RFC 2487 and adds security to SMTP via the STARTTLS extension.

## 1.1 Terminology
Normative keywords defined in RFC 2119 apply.

## 2. STARTTLS Extension
- **Service name**: STARTTLS
- **EHLO keyword**: STARTTLS (no parameters)
- **New SMTP verb**: STARTTLS
- **No additional parameters** to any SMTP command.

## 3. The STARTTLS Keyword
The STARTTLS keyword indicates the server is able to negotiate TLS; it takes no parameters.

## 4. The STARTTLS Command
- **Format**: `STARTTLS` (no parameters)
- **Reply codes**:
  - `220 Ready to start TLS`
  - `501 Syntax error (no parameters allowed)`
  - `454 TLS not available due to temporary reason`
- **Client handling of 454**: Based on local policy – may continue, wait, or abort.
- **Publicly-referenced SMTP servers MUST NOT require STARTTLS** for local delivery (to preserve interoperability).
- Any SMTP server may refuse relay based on TLS authentication.
- Non‑publicly‑referenced servers may require TLS; they **SHOULD** return `530 Must issue a STARTTLS command first` to commands other than NOOP, EHLO, STARTTLS, or QUIT (or `5.7.0` if ENHANCEDSTATUSCODES is used).
- After `220`, the client **MUST** start TLS negotiation before any other SMTP command.
- If using pipelining (RFC 2920), STARTTLS must be the last command in a group.

### 4.1 Processing After the STARTTLS Command
- Both parties **MUST** decide to continue based on authentication/privacy achieved.
- Client **SHOULD** send QUIT if level is inadequate.
- Server **SHOULD** reply `554` to commands (except QUIT) if level inadequate.
- General rules:
  - Client may authenticate server via certificate domain name.
  - Publicly-referenced server may accept any verifiable certificate and optionally include certificate info in Received headers.

### 4.2 Result of the STARTTLS Command
- After TLS handshake, SMTP resets to initial state (after 220 greeting).
- Server **MUST discard** prior knowledge (e.g., EHLO argument); client **MUST discard** prior knowledge (e.g., service extensions).
- Client **SHOULD** send EHLO as first command after TLS.
- EHLO response after TLS **MAY** differ (e.g., advertise different SASL mechanisms).
- A **MUST NOT** start TLS if already active; server **MUST NOT** advertise STARTTLS after a completed handshake.

### 4.3 STARTTLS on the Submission Port
- Valid on Submission port (RFC 2476). Particularly useful for providing security and authentication, as Submission servers are not publicly referenced.

## 5. Usage Example (Condensed)
Illustrates typical client‑server TLS handshake: greeting, EHLO (server includes STARTTLS), STARTTLS, `220`, TLS negotiation, then new EHLO. (See RFC for full dialog.)

## 6. Security Considerations (Condensed)
- SMTP is not end‑to‑end; TLS secures only one hop.
- Both parties **must** check TLS result; ignoring invalidates security.
- Man‑in‑the‑middle attacks (deleting `250 STARTTLS` or altering handshake) are countered by requiring **MUST** be configurable to require successful TLS for selected hosts; **SHOULD** also support opportunistic TLS.
- Clients and servers **MUST** discard knowledge obtained before TLS handshake upon completion.
- STARTTLS does not authenticate message authors; hop‑by‑hop authentication and MIME security (RFC 3156) are needed. SASL EXTERNAL with STARTTLS can provide authorization identity.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Publicly-referenced SMTP server MUST NOT require STARTTLS to deliver mail locally. | MUST | Section 4 |
| R2 | Client MUST start TLS negotiation after receiving 220 response to STARTTLS. | MUST | Section 4 |
| R3 | Client MUST abort connection if unable to start TLS handshake after STARTTLS. | SHOULD | Section 4 |
| R4 | STARTTLS command must be last in a group when pipelining. | MUST (implied) | Section 4 |
| R5 | After TLS handshake, both parties MUST decide to continue based on authentication/privacy. | MUST | Section 4.1 |
| R6 | Client SHOULD issue QUIT if authentication/privacy level insufficient. | SHOULD | Section 4.1 |
| R7 | Server SHOULD reply 554 to commands (except QUIT) if level insufficient. | SHOULD | Section 4.1 |
| R8 | Server MUST discard prior knowledge (e.g., EHLO argument) after TLS. | MUST | Section 4.2 |
| R9 | Client MUST discard prior knowledge (e.g., service extensions) after TLS. | MUST | Section 4.2 |
| R10 | Client SHOULD send EHLO as first command after successful TLS. | SHOULD | Section 4.2 |
| R11 | Client MUST NOT attempt STARTTLS if TLS already active. | MUST | Section 4.2 |
| R12 | Server MUST NOT advertise STARTTLS after TLS handshake completed. | MUST | Section 4.2 |
| R13 | Clients and servers MUST be configurable to require successful TLS for selected hosts. | MUST | Section 6 |
| R14 | Implementation SHOULD also provide option to use TLS when possible. | SHOULD | Section 6 |
| R15 | Implementation MAY record TLS usage and warn if not used later. | MAY | Section 6 |
| R16 | Clients and servers MUST discard knowledge obtained prior to TLS handshake upon completion. | MUST | Section 6 |
| R17 | SASL EXTERNAL MAY be used with STARTTLS to provide authorization identity. | MAY | Section 6 |

## Informative Annexes (Condensed)
- **Appendix (Changes from RFC 2487)**: Summarizes modifications including additional man-in-the-middle attack discussion, clarifications on advertising STARTTLS, handling of 220 response, certificate verification, new Submission port section, example fix, and reference update from RFC 821 to RFC 2821.
- **Full Copyright Statement**: Standard IETF copyright; document may be copied and distributed with restrictions.