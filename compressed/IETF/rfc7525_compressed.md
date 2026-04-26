# RFC 7525: Recommendations for Secure Use of Transport Layer Security (TLS) and Datagram Transport Layer Security (DTLS)
**Source**: Internet Engineering Task Force (IETF) | **Version**: BCP 195 | **Date**: May 2015 | **Type**: Best Current Practice (Normative)
**Original**: http://www.rfc-editor.org/info/rfc7525

## Scope (Summary)
This document provides minimum recommendations for the secure deployment of TLS 1.2 and DTLS 1.2, applicable to the majority of use cases (e.g., HTTP, SMTP, IMAP, POP, SIP, XMPP). It addresses protocol versions, cipher suites, compression, resumption, renegotiation, SNI, public key lengths, and related security considerations. It does not cover opportunistic security scenarios.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC2818] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
- [RFC3766] Orman, H. and P. Hoffman, "Determining Strengths For Public Keys Used For Exchanging Symmetric Keys", BCP 86, RFC 3766, April 2004.
- [RFC4492] Blake-Wilson, S., et al., "Elliptic Curve Cryptography (ECC) Cipher Suites for Transport Layer Security (TLS)", RFC 4492, May 2006.
- [RFC4949] Shirey, R., "Internet Security Glossary, Version 2", FYI 36, RFC 4949, August 2007.
- [RFC5246] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [RFC5288] Salowey, J., et al., "AES Galois Counter Mode (GCM) Cipher Suites for TLS", RFC 5288, August 2008.
- [RFC5289] Rescorla, E., "TLS Elliptic Curve Cipher Suites with SHA-256/384 and AES Galois Counter Mode (GCM)", RFC 5289, August 2008.
- [RFC5746] Rescorla, E., et al., "Transport Layer Security (TLS) Renegotiation Indication Extension", RFC 5746, February 2010.
- [RFC6066] Eastlake 3rd, D., "Transport Layer Security (TLS) Extensions: Extension Definitions", RFC 6066, January 2011.
- [RFC6125] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.
- [RFC6176] Turner, S. and T. Polk, "Prohibiting Secure Sockets Layer (SSL) Version 2.0", RFC 6176, March 2011.
- [RFC6347] Rescorla, E. and N. Modadugu, "Datagram Transport Layer Security Version 1.2", RFC 6347, January 2012.
- [RFC7465] Popov, A., "Prohibiting RC4 Cipher Suites", RFC 7465, February 2015.

## Definitions and Abbreviations
- **TLS**: Transport Layer Security [RFC5246].
- **DTLS**: Datagram Transport Layer Security [RFC6347].
- **PFS/Forward Secrecy**: Property that prevents decryption of past sessions if long-term keys are later compromised.
- **AEAD**: Authenticated Encryption with Associated Data [RFC5116].
- **SNI**: Server Name Indication [RFC6066].
- **OCSP**: Online Certificate Status Protocol [RFC6960].
- **HSTS**: HTTP Strict Transport Security [RFC6797].
- **MITM**: Man-in-the-middle.
- **MUST, SHOULD, etc.**: As defined in [RFC2119].

## 3. General Recommendations

### 3.1. Protocol Versions

#### 3.1.1. SSL/TLS Protocol Versions
- **R1 (3.1.1)**: Implementations MUST NOT negotiate SSL version 2. (Rationale: SSLv2 insecure [RFC6176])
- **R2 (3.1.1)**: Implementations MUST NOT negotiate SSL version 3. (Rationale: SSLv3 insecure, POODLE attack [DEP-SSLv3])
- **R3 (3.1.1)**: Implementations SHOULD NOT negotiate TLS version 1.0; exception only when no higher version available. (Rationale: lacks strong cipher suites, per-record IV issues)
- **R4 (3.1.1)**: Implementations SHOULD NOT negotiate TLS version 1.1; exception only when no higher version available. (Rationale: does not support certain stronger cipher suites)
- **R5 (3.1.1)**: Implementations MUST support TLS 1.2 and MUST prefer to negotiate TLS 1.2 over earlier versions. (Rationale: stronger cipher suites available only with TLS 1.2)

#### 3.1.2. DTLS Protocol Versions
- **R6 (3.1.2)**: Implementations SHOULD NOT negotiate DTLS version 1.0. (Rationale: correlates to TLS 1.1)
- **R7 (3.1.2)**: Implementations MUST support and MUST prefer to negotiate DTLS version 1.2. (Rationale: correlates to TLS 1.2)

#### 3.1.3. Fallback to Lower Versions
- **R8 (3.1.3)**: Clients that fall back to lower protocol versions after server rejection MUST NOT fall back to SSLv3 or earlier. (Rationale: prevents forced downgrade by MITM)

### 3.2. Strict TLS
- **R9 (3.2)**: Clients and servers SHOULD prefer strict TLS configuration over dynamic upgrade (e.g., STARTTLS) when possible.
- **R10 (3.2)**: A client SHOULD attempt to negotiate TLS even if server does not advertise TLS support.
- **R11 (3.2)**: HTTP client and server implementations MUST support the HTTP Strict Transport Security (HSTS) header [RFC6797].
- **R12 (3.2)**: Web servers SHOULD use HSTS to indicate willingness to accept TLS-only clients, unless using HSTS would weaken security (e.g., self-signed certificates, see RFC 6797 Section 11.3). (Rationale: prevents SSL Stripping)

### 3.3. Compression
- **R13 (3.3)**: Implementations and deployments SHOULD disable TLS-level compression, unless the application protocol is shown not to be vulnerable to compression attacks (e.g., CRIME). (Rationale: compression attacks)

### 3.4. TLS Session Resumption
- **R14 (3.4)**: If using session tickets [RFC5077], resumption information MUST be authenticated and encrypted.
- **R15 (3.4)**: A strong cipher suite MUST be used when encrypting the ticket (at least as strong as main TLS cipher suite).
- **R16 (3.4)**: Ticket keys MUST be changed regularly (e.g., once a week) to preserve forward secrecy.
- **R17 (3.4)**: Session ticket validity SHOULD be limited to a reasonable duration (e.g., half as long as ticket key validity). (Rationale: preserve forward secrecy)

### 3.5. TLS Renegotiation
- **R18 (3.5)**: Where renegotiation is implemented, both clients and servers MUST implement the renegotiation_info extension [RFC5746].
- **R19 (3.5)**: The most secure option to counter the Triple Handshake attack is to refuse any change of certificates during renegotiation. Clients SHOULD apply the same validation policy for all certificates received over a connection. (See [triple-handshake] for other countermeasures.)

### 3.6. Server Name Indication
- **R20 (3.6)**: TLS implementations MUST support the Server Name Indication (SNI) extension [RFC6066] for protocols that benefit (e.g., HTTPS). Actual use is a matter of local policy. (Rationale: enables fine-grained security for virtual servers)

## 4. Recommendations: Cipher Suites

### 4.1. General Guidelines
- **R21 (4.1)**: Implementations MUST NOT negotiate cipher suites with NULL encryption.
- **R22 (4.1)**: Implementations MUST NOT negotiate RC4 cipher suites. (Rationale: RC4 weaknesses, [RFC7465])
- **R23 (4.1)**: Implementations MUST NOT negotiate cipher suites offering less than 112 bits of security (including export-level 40/56-bit). (Rationale: [RFC3766])
- **R24 (4.1)**: Implementations SHOULD NOT negotiate cipher suites using algorithms offering less than 128 bits of security. (Rationale: weaker suites are expected to have short lifespan)
- **R25 (4.1)**: Implementations SHOULD NOT negotiate cipher suites based on RSA key transport (static RSA). (Rationale: lack of forward secrecy)
- **R26 (4.1)**: Implementations MUST support and prefer to negotiate cipher suites offering forward secrecy (e.g., DHE, ECDHE families). (Rationale: forward secrecy prevents decryption of past sessions)

### 4.2. Recommended Cipher Suites
- **R27 (4.2)**: Implementation and deployment of the following cipher suites is RECOMMENDED:
  - TLS_DHE_RSA_WITH_AES_128_GCM_SHA256
  - TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
  - TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
  - TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
  (These are AEAD algorithms, supported only in TLS 1.2.)

#### 4.2.1. Implementation Details
- **R28 (4.2.1)**: Clients SHOULD include TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 as the first proposal, unless prior knowledge that server cannot respond to TLS 1.2 client_hello.
- **R29 (4.2.1)**: Servers MUST prefer that cipher suite over weaker ones whenever it is proposed, even if not first.
- **R30 (4.2.1)**: When clients offer stronger suites (e.g., AES-256), server SHOULD prefer the stronger suite unless compelling reasons (e.g., degraded performance) to choose otherwise.
- **R31 (4.2.1)**: Both clients and servers SHOULD include the "Supported Elliptic Curves" extension [RFC4492]; SHOULD support NIST P-256 (secp256r1) curve; clients SHOULD send ec_point_formats extension with "uncompressed".

### 4.3. Public Key Length
- **R32 (4.3)**: For DHE cipher suites, DH key lengths of at least 2048 bits are RECOMMENDED. (Rationale: 2048 bits sufficient for ~10 years, per NIST SP 800-56A)
- **R33 (4.3)**: ECDH curves of less than 192 bits SHOULD NOT be used. (Rationale: 160-bit equivalent to ~80-bit symmetric)
- **R34 (4.3)**: When using RSA, servers SHOULD authenticate using certificates with at least 2048-bit modulus. Use of SHA-256 hash algorithm is RECOMMENDED. Clients SHOULD indicate request for SHA-256 via "Signature Algorithms" extension.

### 4.4. Modular Exponential vs. Elliptic Curve DH
- **R35 (4.4)**: When accommodating implementations that do not support both MODP and EC DH, the following priority order is RECOMMENDED:
  1. ECDHE with strong MAC (e.g., AES-GCM-SHA256)
  2. TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 with 2048-bit DH
  3. TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 with 1024-bit DH
  (Rationale: EC widely deployed but some communities limited; MODP DH has negotiation and parameter length issues)

### 4.5. Truncated HMAC
- **R36 (4.5)**: Implementations MUST NOT use the Truncated HMAC extension [RFC6066 Section 7]. (Rationale: insecure for non-AEAD ciphers, per Paterson et al. 2011)

## 5. Applicability Statement
- The recommendations apply to the most common Internet applications using TLS/DTLS (HTTP, email, XMPP, IRC, SRTP with DTLS). They do not modify existing mandatory-to-implement cipher suites of underlying protocols; updates require explicit changes (e.g., [TLS-XMPP]).
- Designers of new application protocols are expected to conform to these best practices unless compelling reasons exist.

### 5.1. Security Services
- This document applies to deployments where confidentiality, data integrity, and authentication are required. It does not address scenarios where one service is not desired.

### 5.2. Opportunistic Security
- Opportunistic security (dynamic fallback to cleartext) is out of scope; separate future document expected.

## 6. Security Considerations (Condensed)
- **6.1 Host Name Validation**: Application authors should ensure host name validation is performed by TLS implementation; refer to [RFC6125] and [RFC2818] for HTTPS. Host names discovered via insecure means (e.g., insecure DNS) SHOULD NOT be used as reference identifiers [RFC6125].
- **6.2 AES-GCM**: Refer to RFC 5246 Section 11 and RFC 5288 Section 6 for security considerations.
- **6.3 Forward Secrecy**: Explanation of importance, risks of long-term key compromise. Document advocates strict use of forward-secrecy-only ciphers.
- **6.4 Diffie-Hellman Exponent Reuse**: Reuse can negate forward secrecy and lead to attacks if group membership not tested. See [RFC6989] for IKEv2 tests.
- **6.5 Certificate Revocation**: Current state-of-the-art considerations. Servers SHOULD support OCSP [RFC6960], status_request and status_request_v2 extensions [RFC6066, RFC6961], and OCSP stapling [RFC6961]. DANE-TLSA [RFC6698] is an alternative approach.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST NOT negotiate SSLv2. | MUST | 3.1.1 |
| R2 | Implementations MUST NOT negotiate SSLv3. | MUST | 3.1.1 |
| R3 | Implementations SHOULD NOT negotiate TLS 1.0; exception when no higher version available. | SHOULD NOT | 3.1.1 |
| R4 | Implementations SHOULD NOT negotiate TLS 1.1; exception when no higher version available. | SHOULD NOT | 3.1.1 |
| R5 | Implementations MUST support TLS 1.2 and MUST prefer it over earlier versions. | MUST | 3.1.1 |
| R6 | Implementations SHOULD NOT negotiate DTLS 1.0. | SHOULD NOT | 3.1.2 |
| R7 | Implementations MUST support and MUST prefer DTLS 1.2. | MUST | 3.1.2 |
| R8 | Clients falling back MUST NOT fall to SSLv3 or earlier. | MUST NOT | 3.1.3 |
| R9 | Clients and servers SHOULD prefer strict TLS over dynamic upgrade. | SHOULD | 3.2 |
| R10 | Client SHOULD attempt TLS even if server doesn't advertise. | SHOULD | 3.2 |
| R11 | HTTP implementations MUST support HSTS. | MUST | 3.2 |
| R12 | Web servers SHOULD use HSTS unless it weakens security. | SHOULD | 3.2 |
| R13 | Implementations SHOULD disable TLS compression unless safe. | SHOULD | 3.3 |
| R14 | Session ticket info MUST be authenticated and encrypted. | MUST | 3.4 |
| R15 | Strong cipher suite MUST be used for ticket encryption. | MUST | 3.4 |
| R16 | Ticket keys MUST be changed regularly (e.g., weekly). | MUST | 3.4 |
| R17 | Ticket validity SHOULD be limited (e.g., half key validity). | SHOULD | 3.4 |
| R18 | Renegotiation must implement renegotiation_info extension. | MUST | 3.5 |
| R19 | Refuse change of certificates during renegotiation; same validation policy. | SHOULD | 3.5 |
| R20 | TLS implementations MUST support SNI where beneficial. | MUST | 3.6 |
| R21 | MUST NOT negotiate NULL cipher suites. | MUST NOT | 4.1 |
| R22 | MUST NOT negotiate RC4 cipher suites. | MUST NOT | 4.1 |
| R23 | MUST NOT negotiate ciphers with <112-bit security. | MUST NOT | 4.1 |
| R24 | SHOULD NOT negotiate ciphers with <128-bit security. | SHOULD NOT | 4.1 |
| R25 | SHOULD NOT negotiate static RSA cipher suites. | SHOULD NOT | 4.1 |
| R26 | MUST support and prefer forward-secrecy cipher suites. | MUST | 4.1 |
| R27 | RECOMMENDED cipher suites: TLS_DHE_RSA_WITH_AES_(128/256)_GCM_SHA(256/384) and ECDHE variants. | RECOMMENDED | 4.2 |
| R28 | Clients SHOULD offer TLS_ECDHE_RSA_WITH_... first. | SHOULD | 4.2.1 |
| R29 | Servers MUST prefer that suite when offered. | MUST | 4.2.1 |
| R30 | Server SHOULD prefer stronger suite if offered and feasible. | SHOULD | 4.2.1 |
| R31 | Clients and servers SHOULD include Supported Elliptic Curves extension; SHOULD support P-256; clients SHOULD send ec_point_formats with "uncompressed". | SHOULD | 4.2.1 |
| R32 | DHE key lengths of at least 2048 bits are RECOMMENDED. | RECOMMENDED | 4.3 |
| R33 | ECDH curves <192 bits SHOULD NOT be used. | SHOULD NOT | 4.3 |
| R34 | RSA certs with at least 2048-bit modulus; SHA-256 recommended; clients request SHA-256 via Signature Algorithms. | SHOULD | 4.3 |
| R35 | Priority order: ECDHE with strong MAC > DHE 2048 > DHE 1024. | RECOMMENDED | 4.4 |
| R36 | MUST NOT use Truncated HMAC extension. | MUST NOT | 4.5 |
| R37 | Designers of new protocols shall conform unless compelling reasons. | expectation | 5 |
| R38 | Servers SHOULD support OCSP, status_request/status_request_v2, and OCSP stapling. | SHOULD | 6.5 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 6)**: The entire section provides informative background and rationale for the normative recommendations. Key points: forward secrecy rationale (6.3), DH exponent reuse risks (6.4), host name validation importance (6.1), and certificate revocation limitations (6.5) with current best practices.
- **Acknowledgments**: List of contributors and reviewers; not normative.