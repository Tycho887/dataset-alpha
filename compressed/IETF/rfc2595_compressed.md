# RFC 2595: Using TLS with IMAP, POP3 and ACAP
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: June 1999 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc2595

## Scope (Summary)
Defines STARTTLS extensions for IMAP, POP3, and ACAP to add TLS security, including mandatory cipher suites, server identity checking, privacy modes, and a PLAIN SASL mechanism for clear-text password authentication only over encrypted channels.

## Normative References
- [ABNF] RFC 2234
- [ACAP] RFC 2244
- [AUTH] RFC 1704
- [CRAM-MD5] RFC 2195
- [IMAP] RFC 2060
- [KEYWORDS] BCP 14, RFC 2119
- [MIME-SEC] RFC 1847
- [POP3] STD 53, RFC 1939
- [POP3EXT] RFC 2449
- [POP-AUTH] RFC 1734
- [SASL] RFC 2222
- [SMTPTLS] RFC 2487
- [TLS] RFC 2246
- [UTF-8] RFC 2279

## Definitions and Abbreviations
- **TLS**: Transport Layer Security (formerly SSL)
- **SASL**: Simple Authentication and Security Layer
- **STARTTLS/STLS**: Commands to initiate TLS negotiation
- **LOGINDISABLED**: IMAP capability indicating LOGIN command is disabled
- **PLAIN SASL mechanism**: Clear-text password authentication, MUST only be used over TLS
- **Cipher suite**: TLS cryptographic algorithm combination
- **Man-in-the-middle attack**: Active network attack altering communications

## 1. Motivation (Condensed)
TLS secures IMAP, POP3, ACAP against eavesdropping and hijacking. Complements SASL mechanisms. PLAIN SASL defined for clear-text passwords over TLS. STARTTLS preferred over separate secure ports (see §7).

## 1.1. Conventions Used in this Document
- Key words: REQUIRED, MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, OPTIONAL (RFC 2119)
- Authentication terms per [AUTH]
- Formal syntax per ABNF [ABNF]
- Examples: C: client, S: server

## 2. Basic Interoperability and Security Requirements
### 2.1. Cipher Suite Requirements
- **REQUIRED**: TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA [TLS]
- **OPTIONAL**: All other cipher suites

### 2.2. Privacy Operational Mode Security Requirements
- **SHOULD**: Both clients and servers have a privacy mode that refuses authentication unless an encryption layer (e.g., TLS) is active prior to or at authentication, and terminates connection if encryption layer deactivated.
- **SHOULD**: Servers have a mode where only base protocol authentication mechanisms are needed (backward compatibility).
- **MAY**: Clients have a mode using encryption only when advertised, but authentication continues regardless.

### 2.3. Clear-Text Password Requirements
- **MUST**: Clients and servers implementing STARTTLS be configurable to refuse all clear-text login commands/mechanisms unless an adequate encryption layer is active.
- **SHOULD**: Servers allowing unencrypted clear-text logins be configurable to refuse clear-text logins for entire server and per-user.

### 2.4. Server Identity Check
- **MUST**: Client check server hostname against server certificate during TLS negotiation to prevent man-in-the-middle.
- **MUST**: Client use the hostname used to open the connection (not from insecure remote source like insecure DNS). CNAME canonicalization not done.
- **SHOULD**: Use subjectAltName of type dNSName if present.
- Matching is case-insensitive.
- **MAY**: "*" wildcard as left-most name component (e.g., *.example.com matches a.example.com, but not example.com).
- Multiple names: match any one is acceptable.
- On failure, **SHOULD** either ask for explicit user confirmation or terminate.

### 2.5. TLS Security Policy Check
- **MUST**: Both client and server check result of STARTTLS command and TLS negotiation for acceptable authentication or privacy. Local decision, implementation-dependent.

## 3. IMAP STARTTLS Extension
### 3.1. STARTTLS Command
- **Command**: STARTTLS (no arguments)
- **Responses**: OK (begin negotiation), BAD (unknown/invalid)
- TLS negotiation begins immediately after CRLF of tagged OK response.
- **MUST NOT**: Client issue further commands until server response seen and TLS negotiation complete.
- Valid only in non-authenticated state. Server remains in non-authenticated state even if client credentials supplied.
- **MAY**: SASL EXTERNAL mechanism used after TLS, but not required.
- **MUST**: Client discard cached server capabilities after TLS; **SHOULD** re-issue CAPABILITY command. Server MAY advertise different capabilities after TLS.
- Formal syntax: `command_any =/ "STARTTLS"`
- Example provided.

### 3.2. IMAP LOGINDISABLED Capability
- **MAY**: Server advertise LOGINDISABLED to indicate LOGIN command disabled.
- **MUST**: IMAP server implementing STARTTLS implement LOGINDISABLED on unencrypted connections.
- **MUST NOT**: Compliant client issue LOGIN if LOGINDISABLED present.
- Protects against passive attacks only; does not protect against active attacks.

## 4. POP3 STARTTLS Extension
- Adds STLS command.
- **MUST**: Implement POP3 extension mechanism [POP3EXT] if STLS supported.
- Capability name: "STLS".
- **Command**: STLS (no arguments). Only permitted in AUTHORIZATION state.
- TLS negotiation begins after CRLF of +OK response.
- **MUST NOT**: Client issue further commands until server response and TLS complete.
- **MUST**: Client discard cached capabilities; **SHOULD** re-issue CAPA command.
- Server remains in AUTHORIZATION state; MAY use AUTH EXTERNAL after TLS.
- Examples provided.

## 5. ACAP STARTTLS Extension
- Capability "STARTTLS" in ACAP greeting.
- **Command**: STARTTLS (no arguments). Valid only in non-authenticated state.
- TLS negotiation after CRLF of tagged OK response.
- **MUST NOT**: Client issue further commands until server response and TLS complete.
- **MUST**: Server re-issue untagged ACAP greeting after TLS layer established. Client MUST discard cached capabilities and use new greeting.
- Server MAY advertise different capabilities after STARTTLS.
- Formal syntax: `command_any =/ "STARTTLS"`
- Example provided.

## 6. PLAIN SASL Mechanism
- For use with ACAP and protocols lacking clear-text login command.
- **MUST NOT**: Advertise or use PLAIN unless strong encryption layer (e.g., TLS) is active or backward compatibility dictates.
- Single message from client: `[authorize-id] NUL authenticate-id NUL password` (US-ASCII NUL characters).
- Authorization identity may be empty (same as authentication identity).
- Server verifies authentication identity and password; checks authorization.
- **MAY**: Server use password to initialize new authentication database (e.g., CRAM-MD5).
- Non-US-ASCII characters permitted in UTF-8.
- Formal ABNF grammar provided (up to 255 octets per field).
- Example given.

## 7. imaps and pop3s Ports (Condensed)
Separate "imaps" and "pop3s" ports are discouraged in favor of STARTTLS/STLS. Problems enumerated: separate URL schemes confuse users; "secure" vs "not secure" model is misleading; port numbers limited; client security policies become binary (SSL or not).

## 8. IANA Considerations
- Registration of IMAP capabilities "STARTTLS" and "LOGINDISABLED".
- Registration of POP3 "STLS" capability:
  - CAPA tag: STLS, Arguments: none, Added commands: STLS, Valid states: AUTHORIZATION, Specification: this memo
- Registration of ACAP "STARTTLS" capability.
- Registration of PLAIN SASL mechanism:
  - Name: PLAIN, Published specification: this memo, Intended usage: COMMON

## 9. Security Considerations
- TLS protects only data in transit; end-to-end security requires MIME security multiparts.
- Man-in-the-middle can remove STARTTLS from capability list or cause failure response; clients **SHOULD** warn user when session privacy not active and/or be configurable to refuse without acceptable security.
- Implementations **SHOULD** be configurable to refuse weak mechanisms or cipher suites.
- **MUST**: Clients discard cached capability info prior to TLS handshake.
- Clients encouraged to indicate when encryption strength is vulnerable (e.g., ≤56-bit keys).
- LOGINDISABLED only prevents passive attacks; active attacks can bypass.
- PLAIN MUST NOT be used without TLS (or backward compatibility).
- Server gains ability to impersonate user; clients encouraged to have mode disabling mechanisms that reveal passwords to server.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implement TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA | REQUIRED | §2.1 |
| R2 | Clients & servers SHOULD have privacy mode requiring encryption | SHOULD | §2.2 |
| R3 | Servers SHOULD have mode where TLS not required for authentication | SHOULD | §2.2 |
| R4 | Be configurable to refuse all clear-text login without encryption | MUST | §2.3 |
| R5 | Server SHOULD be configurable to refuse clear-text login per-server and per-user | SHOULD | §2.3 |
| R6 | Client MUST check server identity against certificate | MUST | §2.4 |
| R7 | Client MUST use hostname used to open the connection | MUST | §2.4 |
| R8 | Client MUST NOT use hostname from insecure remote source | MUST | §2.4 |
| R9 | Client SHOULD support subjectAltName dNSName | SHOULD | §2.4 |
| R10 | Client SHOULD ask confirmation or terminate on identity mismatch | SHOULD | §2.4 |
| R11 | Both client and server MUST check result of STARTTLS for acceptable privacy | MUST | §2.5 |
| R12 | Client MUST NOT issue further commands until server response and TLS negotiation complete | MUST | §3.1,4,5.1 |
| R13 | Client MUST discard cached capability information after TLS | MUST | §3.1,4,5.1,9 |
| R14 | Client SHOULD re-issue CAPABILITY/CAPA after TLS | SHOULD | §3.1,4 |
| R15 | IMAP server with STARTTLS MUST implement LOGINDISABLED | MUST | §3.2 |
| R16 | IMAP client MUST NOT issue LOGIN if LOGINDISABLED present | MUST | §3.2 |
| R17 | POP3 server MUST implement POP3 extension mechanism | MUST | §4 |
| R18 | ACAP server MUST re-issue ACAP greeting after TLS | MUST | §5.1 |
| R19 | Client SHOULD warn when session privacy not active and/or refuse to proceed | SHOULD | §9 |
| R20 | SHOULD be configurable to refuse weak mechanisms/cipher suites | SHOULD | §9 |
| R21 | PLAIN SASL MUST NOT be used unless strong encryption active or backward compatibility | MUST | §6,9 |
| R22 | PLAIN mechanism MUST use UTF-8 encoding for characters | MUST | §6 |

## Informative Annexes (Condensed)
- **Appendix A – Compliance Checklist**: Lists all MUST and SHOULD requirements by section. An implementation meeting all MUST and SHOULD is "unconditionally compliant"; meeting all MUST but not all SHOULD is "conditionally compliant". Requirements are tabulated for easy verification.