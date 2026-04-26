# RFC 6066: Transport Layer Security (TLS) Extensions: Extension Definitions
**Source**: IETF | **Version**: Standards Track | **Date**: January 2011 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc6066

## Scope (Summary)
This document specifies six TLS extensions: server_name, max_fragment_length, client_certificate_url, trusted_ca_keys, truncated_hmac, and status_request. It is a companion to RFC 5246 (TLS 1.2) and obsoletes RFC 4366.

## Normative References
- [RFC2104] HMAC: Keyed-Hashing for Message Authentication
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC2560] X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP
- [RFC2585] Internet X.509 Public Key Infrastructure Operational Protocols: FTP and HTTP
- [RFC2616] Hypertext Transfer Protocol -- HTTP/1.1
- [RFC3986] Uniform Resource Identifier (URI): Generic Syntax
- [RFC5246] The Transport Layer Security (TLS) Protocol Version 1.2
- [RFC5280] Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- [RFC5890] Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework

## Definitions and Abbreviations
- **TLS**: Transport Layer Security
- **MAC**: Message Authentication Code
- **HMAC**: Keyed-Hashing for Message Authentication
- **OCSP**: Online Certificate Status Protocol
- **CRL**: Certificate Revocation List
- **DTLS**: Datagram Transport Layer Security
- **URI**: Uniform Resource Identifier
- **DER**: Distinguished Encoding Rules
- **PRF**: Pseudo-Random Function
- **HandshakeType**: Enumeration of handshake message types (including new types certificate_url(21), certificate_status(22))
- **ExtensionType**: Enumeration of extension types (server_name(0), max_fragment_length(1), client_certificate_url(2), trusted_ca_keys(3), truncated_hmac(4), status_request(5))
- **AlertDescription**: Enumeration of alert descriptions (including new alerts: certificate_unobtainable(111), unrecognized_name(112), bad_certificate_status_response(113), bad_certificate_hash_value(114))
- **ServerNameList**: Structure containing a list of server names, each with a NameType and name value
- **MaxFragmentLength**: Enumeration of allowed maximum fragment lengths: 2^9(1), 2^10(2), 2^11(3), 2^12(4)
- **CertificateURL**: Handshake message sent in place of Certificate when client_certificate_url negotiated
- **TrustedAuthorities**: List of TrustedAuthority structures identifying CA root keys
- **Truncated HMAC**: HMAC output truncated to 80 bits (10 bytes)
- **CertificateStatusRequest**: Structure containing status_type and request for OCSP
- **CertificateStatus**: Handshake message containing status response (e.g., OCSPResponse)
- **PkiPath**: ASN.1 type representing a certification path (SEQUENCE OF Certificate)

## 1. Introduction
The TLS Protocol Version 1.2 [RFC5246] includes framework for extensions but only specifies Signature Algorithms. This document provides specifications for existing TLS extensions.

### 1.1 Specific Extensions Covered
Extensions defined: server_name, max_fragment_length, client_certificate_url, trusted_ca_keys, truncated_hmac, status_request.
- Allow TLS clients to provide server name for virtual hosting.
- Allow negotiation of smaller maximum fragment length for memory/bandwidth constraints.
- Allow use of client certificate URLs to conserve memory.
- Allow clients to indicate which CA root keys they possess to avoid handshake failures.
- Allow use of truncated MACs to save bandwidth.
- Allow server to send certificate status (e.g., OCSP response) during handshake.
- Backward compatible: supporting clients can talk to non-supporting servers and vice versa.
- Messages associated with these extensions sent during handshake MUST be included in Finished message hash calculations.
- All extensions are relevant only when session is initiated. On session resumption:
  - server_name MAY be used by server to decide whether to resume.
  - If resumption denied, extensions negotiated normally.
  - If older session resumed, server MUST ignore extensions and send server hello with none of these extensions; functionality from original session applies.

### 1.2 Conventions Used in This Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC2119].

## 2. Extensions to the Handshake Protocol
Two new handshake messages: "CertificateURL" and "CertificateStatus". Handshake type enums: certificate_url(21), certificate_status(22). Structure defined for Handshake message including new cases.

## 3. Server Name Indication
- **server_name extension**: Clients MAY include extension of type "server_name" in (extended) client hello.
- **Extension_data** SHALL contain ServerNameList:
  - Struct ServerName { NameType name_type; select (name_type) { case host_name: HostName; } name; }
  - NameType: host_name(0)
  - HostName: opaque <1..2^16-1> (fully qualified DNS hostname, ASCII encoding without trailing dot, case-insensitive; literal IPv4/IPv6 not permitted)
  - ServerNameList: struct { ServerName server_name_list<1..2^16-1>; }
- ServerNameList MUST NOT contain more than one name of the same name_type.
- If server understands ClientHello extension but does not recognize server name, server SHOULD either abort handshake with fatal unrecognized_name(112) alert or continue handshake. Sending warning-level unrecognized_name is NOT RECOMMENDED.
- TLS implementations encouraged to make warning-level alerts available to application callers.
- Note: Previous versions permitted multiple names of same name_type; now prohibited.
- Currently only DNS hostnames supported; other name types may be added by RFC updating this document. For backward compatibility, future data structures MUST begin with 16-bit length.
- TLS MAY treat server names as opaque data.
- RECOMMENDED that clients include "server_name" extension whenever they locate server by supported name type.
- Server MAY use information to guide certificate selection; if it does, server SHALL include "server_name" extension in server hello with empty extension_data.
- Session resumption: Server MAY use server_name in session cache lookup; client SHOULD include same server_name in resumption request. Server MUST NOT accept resumption if server_name contains different name; instead proceed with full handshake. When resuming, server MUST NOT include server_name extension in server hello.
- If application protocol negotiates server name and then upgrades to TLS, the server_name extension SHOULD contain same name. Client SHOULD NOT attempt different server name at application layer.

## 4. Maximum Fragment Length Negotiation
- Without extension, max plaintext fragment length is 2^14 bytes.
- Clients MAY include "max_fragment_length" extension in client hello.
- Extension_data SHALL contain MaxFragmentLength enum: 2^9(1), 2^10(2), 2^11(3), 2^12(4).
- Servers MAY accept by including same extension with same value in server hello.
- If server receives request for value other than allowed, MUST abort handshake with "illegal_parameter" alert. Similarly, if client receives response differing from requested, MUST abort with "illegal_parameter".
- After successful negotiation, client and server MUST immediately begin fragmenting messages to ensure no fragment larger than negotiated length. (TLS already requires support for handshake fragmentation.)
- Negotiated length applies for duration of session including session resumptions.
- Negotiated length limits TLSPlaintext.length. Output may be larger (e.g., with headers, padding, MAC). If output exceeds negotiated max, peer MUST discard and send "record_overflow" alert (without decrypting). When used with DTLS, SHOULD NOT generate record_overflow alerts unless packet passes message authentication.

## 5. Client Certificate URLs
- Without extension, client certificates sent in handshake. This extension allows constrained clients to send certificate URLs.
- Clients MAY include "client_certificate_url" extension in client hello with empty extension_data.
- Servers MAY indicate acceptance by including same extension with empty extension_data in server hello.
- After negotiation, clients MAY send "CertificateURL" message instead of "Certificate".
- Structures:
  - CertChainType: individual_certs(0), pkipath(1)
  - CertificateURL: { CertChainType type; URLAndHash url_and_hash_list<1..2^16-1>; }
  - URLAndHash: { opaque url<1..2^16-1>; uint8 padding; opaque SHA1Hash[20]; }
- Each url MUST be absolute URI reference [RFC3986].
- For X.509 certificates:
  - If type "individual_certs", each URL refers to single DER-encoded X.509v3 certificate, client's certificate first.
  - If type "pkipath", single URL refers to DER-encoded PkiPath (Section 10.1).
- padding byte MUST be 0x01 (backward compatibility).
- Hash is SHA-1 of DER-encoded certificate or PkiPath.
- Ordering of URLs same as TLS Certificate message, opposite of PkiPath encoding. Self-signed root MAY be omitted.
- Servers receiving CertificateURL SHALL attempt to retrieve certificate chain from URLs. Cached copy MAY be used if SHA-1 hash matches.
- Servers supporting this extension MUST support 'http' URI scheme; MAY support others. Use of other schemes may cause problems.
- If HTTP used, server can use Cache-Control/Expires directives.
- TLS server MUST NOT follow HTTP redirects when retrieving certificates. URLs MUST NOT depend on redirects.
- MIME Content-Types: "application/pkix-cert" for single certificate, "application/pkix-pkipath" for chain.
- Server MUST check SHA-1 hash of retrieved object matches given hash. If not, MUST abort handshake with bad_certificate_hash_value(114) alert (fatal).
- Clients may choose to send Certificate or CertificateURL after negotiation.
- If server unable to obtain certificates and requires them, MUST send fatal certificate_unobtainable(111) alert. If not required, may continue with warning-level alert.

## 6. Trusted CA Indication
- Clients MAY include "trusted_ca_keys" extension in client hello to indicate which CA root keys they possess.
- Extension_data SHALL contain TrustedAuthorities:
  - struct { TrustedAuthority trusted_authorities_list<0..2^16-1>; }
  - TrustedAuthority: { IdentifierType identifier_type; select (identifier_type) { case pre_agreed: struct {}; case key_sha1_hash: SHA1Hash; case x509_name: DistinguishedName; case cert_sha1_hash: SHA1Hash; } identifier; }
  - IdentifierType: pre_agreed(0), key_sha1_hash(1), x509_name(2), cert_sha1_hash(3)
- For key_sha1_hash: SHA-1 hash of subjectPublicKey (DSA/ECDSA) or modulus (RSA, big-endian without leading zeros).
- For x509_name: DER-encoded X.509 DistinguishedName.
- For cert_sha1_hash: SHA-1 hash of DER-encoded Certificate.
- Clients may include none, some, or all CA root keys.
- Servers MAY use information to guide certificate chain selection; if they do, server SHALL include "trusted_ca_keys" extension in server hello with empty extension_data.

## 7. Truncated HMAC
- TLS cipher suites use HMAC with full output. This extension negotiates truncation to 80 bits.
- Clients MAY include "truncated_hmac" extension in client hello with empty extension_data.
- Servers MAY agree by including same extension with empty extension_data in server hello.
- If session negotiates cipher suite not using HMAC, extension has no effect.
- If successfully negotiated and cipher suite uses HMAC, both client and server MUST use truncated HMAC: SecurityParameters.mac_length = 10 bytes, only first 10 bytes of HMAC output transmitted and checked. Does not affect PRF or key derivation.
- Negotiated truncation applies for duration of session including session resumptions.

## 8. Certificate Status Request
- Clients MAY include "status_request" extension in client hello to request certificate status (e.g., OCSP).
- Extension_data SHALL contain CertificateStatusRequest:
  - struct { CertificateStatusType status_type; select (status_type) { case ocsp: OCSPStatusRequest; } request; }
  - CertificateStatusType: ocsp(1)
  - OCSPStatusRequest: { ResponderID responder_id_list<0..2^16-1>; Extensions request_extensions; }
  - ResponderID: opaque <1..2^16-1>
  - Extensions: opaque <0..2^16-1> (DER-encoded as per [RFC2560] and [RFC5280])
- Zero-length responder_id_list means responders implicitly known. Zero-length request_extensions means no extensions.
- For OCSP nonce extension: nonce MUST be DER-encoded OCTET STRING encapsulated as another OCTET STRING.
- Servers MAY return suitable certificate status response along with their certificate. If OCSP requested, they SHOULD use information in extension to select responder and SHOULD include request_extensions in OCSP request.
- Server sends "CertificateStatus" message immediately after "Certificate" message (before ServerKeyExchange or CertificateRequest). If server returns CertificateStatus, it MUST have included "status_request" extension with empty extension_data in server hello.
- CertificateStatus: { CertificateStatusType status_type; select (status_type) { case ocsp: OCSPResponse; } response; }
- OCSPResponse: opaque <1..2^24-1> (complete DER-encoded OCSP response).
- Only one OCSP response may be sent.
- Server MAY choose not to send CertificateStatus even if it received status_request in client hello and sent status_request in server hello.
- Server MUST NOT send CertificateStatus unless it received status_request in client hello and sent status_request in server hello.
- Clients requesting OCSP response and receiving it MUST check the response and abort handshake with bad_certificate_status_response(113) alert (fatal) if response not satisfactory.

## 9. Error Alerts
Four new error alerts defined: certificate_unobtainable(111), unrecognized_name(112), bad_certificate_status_response(113), bad_certificate_hash_value(114). These alerts MUST NOT be sent unless the sending party has received an extended hello from the communicating party.

## 10. IANA Considerations
- Updated TLS Extensions registry references from RFC 4366 to this document.
- Updated TLS Alert registry entries: 111-114.
- Updated TLS HandshakeType registry entries: 21, 22.
- Updated ExtensionType registry entries: 0-5.
- Registered MIME type application/pkix-pkipath as specified in Section 10.1.

### 10.1 pkipath MIME Type Registration
- MIME type: application/pkix-pkipath
- Encoding: DER of ASN.1 type PkiPath (SEQUENCE OF Certificate). Order: subject of first is issuer of second, etc.
- Use only with PKIX-conformant certificates [RFC5280].
- Security: see [X509-4th], [RFC5280], and protocol using this type.
- File extension: .pkipath

## 11. Security Considerations
### 11.1 server_name
- Server hosting multiple domains must satisfy security needs of each owner.
- If application protocol presents different server name, server MUST check consistency.
- Implementations MUST ensure buffer overflow does not occur regardless of length fields.

### 11.2 max_fragment_length
- Takes effect immediately, including for handshake messages, but TLS already requires fragmentation support.
- Buffer sizing must account for cipher suite and compression effects on output size.

### 11.3 client_certificate_url
- Server acts as client in URI scheme, subject to security concerns of that scheme. Attackers could prompt server to connect to malicious URLs.
- Denial-of-service possible.
- RECOMMENDED that extension be specifically enabled by administrator, not by default. URI schemes enabled individually; minimal set; unusual schemes SHOULD be avoided.
- URLs with non-default ports or very long URLs may cause problems.
- Use of SHA-1 for hashes relies on second pre-image resistance; collision resistance not required for this context.
- HTTP caching proxies may return out-of-date responses.

### 11.4 trusted_ca_keys
- CA root keys may be confidential; extension should be used with care.
- SHA-1 used for certificate hash; cryptographic hash not strictly required here.

### 11.5 truncated_hmac
- Truncated MACs may be weaker but no significant weaknesses known for HMAC-MD5 or SHA-1 truncated to 80 bits.
- MAC output length need not equal cipher key length because forging cannot be done off-line in TLS.
- Active attacker cannot force truncated HMAC because MAC algorithm only takes effect after handshake authentication.

### 11.6 status_request
- Attacker's server using compromised key may pretend not to support extension. Client requiring OCSP SHOULD contact OCSP server directly or abort.
- Use of OCSP nonce may improve replay protection.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | ServerNameList MUST NOT contain more than one name of the same name_type. | MUST | Section 3 |
| R2 | Server that understands server_name but does not recognize name SHOULD either abort with fatal unrecognized_name or continue. Warning-level NOT RECOMMENDED. | SHOULD / NOT RECOMMENDED | Section 3 |
| R3 | If server uses server_name to select certificate, it SHALL include server_name extension in server hello with empty extension_data. | SHALL | Section 3 |
| R4 | Server MUST NOT accept session resumption if server_name extension contains different name; proceed with full handshake. | MUST | Section 3 |
| R5 | When resuming session, server MUST NOT include server_name extension in server hello. | MUST | Section 3 |
| R6 | If application protocol negotiates server name then upgrades to TLS, extension SHOULD contain same name. Client SHOULD NOT request different name. | SHOULD | Section 3 |
| R7 | Client may include max_fragment_length extension with allowed values: 2^9, 2^10, 2^11, 2^12. | MAY | Section 4 |
| R8 | If server receives request for invalid max_fragment_length, MUST abort with illegal_parameter. Client receiving different response MUST abort with illegal_parameter. | MUST | Section 4 |
| R9 | After negotiating max_fragment_length, client and server MUST immediately fragment messages to not exceed negotiated length. | MUST | Section 4 |
| R10 | Client may include client_certificate_url extension in client hello with empty extension_data. | MAY | Section 5 |
| R11 | Server may indicate acceptance by including same extension with empty extension_data in server hello. | MAY | Section 5 |
| R12 | Each URL in CertificateURL MUST be absolute URI reference. | MUST | Section 5 |
| R13 | Padding byte in URLAndHash MUST be 0x01. | MUST | Section 5 |
| R14 | Servers receiving CertificateURL SHALL attempt to retrieve certificates. Cached copy MAY be used if SHA-1 hash matches. | SHALL/MAY | Section 5 |
| R15 | Servers supporting this extension MUST support 'http' URI scheme. | MUST | Section 5 |
| R16 | TLS server MUST NOT follow HTTP redirects when retrieving certificates. URLs MUST NOT depend on redirects. | MUST | Section 5 |
| R17 | Server MUST check SHA-1 hash of retrieved object; if mismatch, abort with bad_certificate_hash_value (fatal). | MUST | Section 5 |
| R18 | If server unable to obtain certificates and requires them, MUST send fatal certificate_unobtainable. | MUST | Section 5 |
| R19 | Clients may include trusted_ca_keys extension in client hello. | MAY | Section 6 |
| R20 | If server uses trusted_ca_keys to select certificate chain, it SHALL include trusted_ca_keys extension in server hello with empty extension_data. | SHALL | Section 6 |
| R21 | Clients may include truncated_hmac extension in client hello. | MAY | Section 7 |
| R22 | Servers may agree by including same extension in server hello. | MAY | Section 7 |
| R23 | If truncated HMAC negotiated and cipher suite uses HMAC, both MUST use truncated HMAC: mac_length=10, only first 10 bytes transmitted and checked. | MUST | Section 7 |
| R24 | Clients may include status_request extension in client hello with CertificateStatusRequest. | MAY | Section 8 |
| R25 | If server sends CertificateStatus, it MUST have included status_request extension in server hello with empty extension_data. | MUST | Section 8 |
| R26 | Server MUST NOT send CertificateStatus unless it received status_request in client hello and sent status_request in server hello. | MUST | Section 8 |
| R27 | Clients receiving OCSP response MUST check it and abort with bad_certificate_status_response (fatal) if not satisfactory. | MUST | Section 8 |
| R28 | New error alerts MUST NOT be sent unless sending party has received extended hello from communicating party. | MUST | Section 9 |

## Informative Annexes (Condensed)
- **Appendix A: Changes from RFC 4366**: Summarizes major changes: moved general extension mechanisms to RFC 5246; server_name now ASCII only, prohibits multiple names of same type, specifies behavior on unrecognized name and session resumption; client_certificate_url hash now mandatory; max_fragment_length DTLS behavior change; servers prohibited from following HTTP redirects.
- **Appendix B: Acknowledgements**: Credits authors of RFC 4366 and additional contributors.