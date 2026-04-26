# RFC 4346: The Transport Layer Security (TLS) Protocol Version 1.1
**Source**: IETF | **Version**: 1.1 | **Date**: April 2006 | **Type**: Normative (Standards Track)
**Original**: https://tools.ietf.org/html/rfc4346

## Scope (Summary)
Specifies Version 1.1 of the TLS protocol, which provides communications security over the Internet. The protocol prevents eavesdropping, tampering, or message forgery between client/server applications.

## Normative References
- [AES] NIST FIPS 197 (Advanced Encryption Standard)
- [3DES] Tuchman, IEEE Spectrum, 1979
- [DES] ANSI X3.106, 1983
- [DSS] NIST FIPS PUB 186-2, 2000
- [HMAC] RFC 2104
- [IDEA] Lai, 1992
- [MD5] RFC 1321
- [PKCS1A] RFC 2313
- [PKCS1B] RFC 3447
- [PKIX] RFC 3280
- [RC2] RFC 2268
- [REQ] RFC 2119
- [RFC2434] BCP 26, RFC 2434
- [SHA] NIST FIPS PUB 180-2
- [TLSAES] RFC 3268
- [TLSEXT] RFC 3546
- [TLSKRB] RFC 2712
- [SCH] Schneier, Applied Cryptography, 1996
- [SSL3] Netscape SSL 3.0

## Definitions and Abbreviations
- **AES**: Advanced Encryption Standard, block cipher with 128/192/256-bit keys, 16-byte block.
- **Block cipher**: Encrypts plaintext in fixed-size blocks (e.g., 64 bits).
- **Bulk cipher**: Symmetric encryption algorithm for large data.
- **CBC**: Cipher Block Chaining mode.
- **Certificate**: X.509v3 binding identity to public key.
- **Client write key / MAC secret**: Keys used to encrypt/authenticate data written by client.
- **Connection**: Peer-to-peer transport relationship; transient, associated with a session.
- **DES**: Data Encryption Standard, block cipher with 56-bit key, 8-byte block.
- **Digital signature**: Public-key cryptography with one-way hash for authentication.
- **DSS**: Digital Signature Standard (NIST FIPS PUB 186-2).
- **Finished message**: Verifies handshake success.
- **Handshake**: Initial negotiation establishing parameters.
- **HMAC**: Keyed-hash message authentication code (RFC 2104).
- **IV**: Initialization Vector for CBC mode.
- **MAC**: Message Authentication Code.
- **Master secret**: 48-byte shared secret used to derive keys.
- **MD5**: Secure hash function (16-byte digest).
- **Premaster secret**: Secret used to generate master secret.
- **PRF**: Pseudorandom Function based on HMAC.
- **RC2/RC4**: Symmetric ciphers.
- **RSA**: Public-key algorithm for encryption/signing.
- **Server write key / MAC secret**: Keys used to encrypt/authenticate data written by server.
- **Session**: Association between client and server sharing cryptographic parameters.
- **SHA**: Secure Hash Algorithm (20-byte output).
- **SSL**: Netscape Secure Socket Layer (predecessor).
- **Stream cipher**: Encrypts by XOR with keystream.
- **TLS**: Transport Layer Security.

## 1. Introduction
- TLS provides privacy and data integrity using TLS Record Protocol and TLS Handshake Protocol.
- **Properties**: Connection private (symmetric encryption, unique keys per connection), reliable (keyed MAC).
- Handshake provides authentication (optional but required for at least one peer), secure negotiation of shared secret, reliable negotiation.
- TLS is application-protocol independent.

### 1.1. Differences from TLS 1.0
- Explicit IV replaces implicit IV (defends against CBC attacks).
- Padding errors use `bad_record_mac` alert instead of `decryption_failed`.
- IANA registries defined.
- Premature closes no longer cause session nonresumable.
- Added informational notes on new attacks.

## 1.2. Requirements Terminology
- **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **MAY** as per RFC 2119.

## 2. Goals (Informative)
1. Cryptographic security.
2. Interoperability.
3. Extensibility.
4. Relative efficiency (session caching).

## 4. Presentation Language
- Data representation uses network byte order (big-endian).
- Basic block size: 1 byte (8 bits).
- Comments: `/* ... */`, optional components: `[[ ]]`.
- **Vectors**: Fixed-length `T T'[n]`; variable-length `T T'<floor..ceiling>` with length prefix.
- **Numbers**: `uint8`, `uint16`, `uint24`, `uint32`, `uint64`.
- **Enumerateds**: `enum { name(value) } Te;` occupy space of maximal ordinal value.
- **Constructed types**: `struct { ... } T;` with variant support `select (E) { case e1: Te1; ... }`.
- **Cryptographic attributes**: `digitally-signed`, `stream-ciphered`, `block-ciphered`, `public-key-encrypted`.
- **Constants**: Typed constants for specification.

## 5. HMAC and the Pseudorandom Function
- HMAC (RFC 2104) used with MD5 and SHA-1 as `HMAC_MD5(secret, data)` and `HMAC_SHA(secret, data)`.
- **PRF**: `PRF(secret, label, seed) = P_MD5(S1, label+seed) XOR P_SHA-1(S2, label+seed)`
- `P_hash(secret, seed) = HMAC_hash(secret, A(1)+seed) | HMAC_hash(secret, A(2)+seed) | ...`
- Secret split into two halves (S1, S2) for mixing.

## 6. The TLS Record Protocol
- Protocol layers: fragmentation, optional compression, MAC, encryption, transmission.
- Four record protocol clients: handshake, alert, change cipher spec, application data.
- New record types **SHOULD** allocate ContentType values immediately beyond existing (see Appendix A.1); all values **MUST** be defined by RFC 2434 Standards Action.
- If implementation receives unknown record type, it **SHOULD** ignore it.
- Type and length not encrypted; care **SHOULD** be taken to minimize traffic analysis.

### 6.1. Connection States
- Four states: current/pending read/write.
- Initial state: no encryption, compression, or MAC.
- Security parameters: connection end, bulk encryption algorithm, MAC algorithm, compression algorithm, master secret, client random, server random.
- Record layer generates: client write MAC secret, server write MAC secret, client write key, server write key.
- Current states **MUST** be updated per record.
- **Sequence number**: 64-bit, set to zero when state active, **MUST NOT** wrap (renegotiate if needed), incremented after each record.

### 6.2. Record Layer
#### 6.2.1. Fragmentation
- Fragment into `TLSPlaintext` records of **2^14 bytes or less**.
- Multiple client messages of same ContentType **MAY** be coalesced; single message **MAY** be fragmented.
- `TLSPlaintext` structure: `ContentType type`, `ProtocolVersion version` (TLS 1.1 = {3,2}), `uint16 length` (≤ 2^14), `opaque fragment[]`.
- Interleaving of content types allowed; application data lower precedence; records delivered in same order as protected.

#### 6.2.2. Record Compression and Decompression
- Compression algorithm from current session state (initially `null`).
- Compression must be lossless; content length **MUST NOT** increase by more than 1024 bytes.
- If decompression would exceed 2^14 bytes, **shall** report fatal decompression failure.

#### 6.2.3. Record Payload Protection
- `TLSCiphertext` structure: type, version, length (≤ 2^14+2048), fragment (stream or block cipher).
##### 6.2.3.1. Null or Standard Stream Cipher
- `GenericStreamCipher`: `opaque content[]`, `opaque MAC[]` (HMAC over seq_num, type, version, length, fragment).
- MAC computed before encryption; stream cipher encrypts entire block.
- For `TLS_NULL_WITH_NULL_NULL`: identity encryption, no MAC.
##### 6.2.3.2. CBC Block Cipher
- `GenericBlockCipher`: `IV[]`, `content[]`, `MAC[]`, `padding[]`, `padding_length`.
- **Explicit IV** per record to prevent [CBCATT]. Two recommended methods (generate random IV; or prepend random block). One alternative method **MAY** be used but not demonstrated as strong.
- Padding **MAY** be any length up to 255 bytes; each padding byte **MUST** be filled with padding length value. Receiver **MUST** check padding and **SHOULD** use `bad_record_mac` for padding errors.
- **Implementation Note**: Timing attack defense – **MUST** ensure processing time same whether padding correct or not; compute MAC even if padding incorrect.

### 6.3. Key Calculation
- `key_block = PRF(master_secret, "key expansion", server_random + client_random)`.
- Partitioned: `client_write_MAC_secret`, `server_write_MAC_secret`, `client_write_key`, `server_write_key`.

## 7. The TLS Handshaking Protocols
- Three subprotocols: Handshake, Change Cipher Spec, Alert.
- Handshake negotiates session: session identifier, peer certificate, compression method, cipher spec, master secret, is resumable.

### 7.1. Change Cipher Spec Protocol
- Single message: `enum { change_cipher_spec(1) } type;`.
- Sent by both client and server; causes receiver to copy pending read state to current.
- Sender **MUST** make write pending state active immediately after sending.
- Note: during rehandshake, old CipherSpec may continue until ChangeCipherSpec sent; then new **MUST** be used. Small window for buffering may exist.

### 7.2. Alert Protocol
- Alert messages convey severity (warning/fatal) and description.
- Fatal alerts cause immediate connection termination; session identifier **MUST** be invalidated.
#### 7.2.1. Closure Alerts
- `close_notify` sent to avoid truncation attack.
- Unless other fatal alert, each party **required** to send `close_notify` before closing write side.
- Receiving party **MUST** respond with `close_notify` and close down immediately.
- If application protocol transfers data after TLS close, implementation **must** receive `close_notify` before indicating end.
#### 7.2.2. Error Alerts
- Fatal alerts cause immediate close; servers and clients **MUST** forget session-identifiers, keys, secrets.
- Key alerts: `bad_record_mac` (fatal, returned for incorrect MAC or invalid decryption), `decryption_failed` (fatal, **MAY** return but uniform use of `bad_record_mac` preferred), `record_overflow` (fatal), `decompression_failure` (fatal), `handshake_failure` (fatal), `illegal_parameter` (fatal), etc.
- New alert values **MUST** be defined by RFC 2434 Standards Action.

### 7.3. Handshake Protocol Overview
- Steps: exchange hellos, exchange cryptographic parameters, exchange certificates, generate master secret, provide parameters to record layer, verify.
- Man-in-the-middle can attempt to downgrade; higher layers **MUST NOT** transmit over less secure channel. Cipher suite offers promised security; **SHOULD NOT** send data over 40-bit encryption if unacceptable.
- Full handshake flow (Fig. 1): ClientHello, ServerHello, Certificate*, ServerKeyExchange*, CertificateRequest*, ServerHelloDone, Certificate*, ClientKeyExchange, CertificateVerify*, [ChangeCipherSpec], Finished.
- Abbreviated handshake (Fig. 2): ClientHello with SessionID, ServerHello with same ID, both send ChangeCipherSpec and Finished.
- Application data **MUST NOT** be sent before first handshake completes (except `TLS_NULL_WITH_NULL_NULL` established).

### 7.4. Handshake Protocol
- Handshake messages encapsulated in TLSPlaintext.
- Order **MUST** be as specified; unexpected order results in fatal error.
- New HandshakeType values **MUST** be defined via RFC 2434 Standards Action.

#### 7.4.1. Hello Messages
##### 7.4.1.1. Hello Request
- Server **MAY** send at any time; client may ignore if negotiating or may respond with `no_renegotiation`. Server **SHOULD NOT** repeat request until subsequent handshake complete.
- This message **MUST NOT** be included in handshake hashes.
##### 7.4.1.2. Client Hello
- Client **required** to send as first message; can also be sent in response to Hello Request.
- Contains `Random` (gmt_unix_time + 28 random bytes), `SessionID` (variable, 0..32 bytes), `CipherSuite` list (ordered by preference), `CompressionMethod` list.
- If session_id non-empty (resumption request), vector **MUST** include at least cipher_suite from that session.
- **MUST** include `CompressionMethod.null`.
- After client hello, client waits for server hello; any other handshake message (except hello request) is fatal error.
- Extra data after compression methods **MAY** be included for forward compatibility; **MUST** be included in handshake hashes.
##### 7.4.1.3. Server Hello
- Server sends in response if acceptable algorithms found; otherwise `handshake_failure` alert.
- `server_version` = lower of client suggested and server highest.
- `random` **MUST** be independently generated from ClientHello.random.
- If session_id matches cache and server willing, respond with same session_id = resumed session; then proceed directly to Finished. Otherwise different session_id (or empty to indicate no caching). Resumed session **must** use same cipher suite.

#### 7.4.2. Server Certificate
- Server **MUST** send certificate unless key exchange is anonymous.
- Certificate type **MUST** be appropriate for cipher suite key exchange algorithm (RSA, DHE_DSS, DHE_RSA, DH_DSS, DH_RSA). Public key usage extensions **MUST** be set appropriately.
- Structure: `Certificate` sequence (chain) of X.509v3 certificates; sender's certificate first.

#### 7.4.3. Server Key Exchange Message
- Sent when server certificate does not contain enough data (e.g., DHE_DSS, DHE_RSA, DH_anon). Not legal for RSA, DH_DSS, DH_RSA.
- Conveys RSA public key or Diffie-Hellman public key.
- For non-anonymous, includes signature over `ClientHello.random + ServerHello.random + ServerParams`.

#### 7.4.4. Certificate Request
- Non-anonymous server **can optionally** request client certificate.
- Contains `certificate_types` list and `certificate_authorities` distinguished names.
- Fatal error for anonymous server to request client authentication.

#### 7.4.5. Server Hello Done
- Server indicates end of hello messages; after sending, waits for client response.
- Client **SHOULD** verify server certificate and parameters.

#### 7.4.6. Client Certificate
- First client message after ServerHelloDone (if server requested). If no suitable certificate, client **SHOULD** send empty certificate list.
- When using static DH, client's DH parameters **MUST** match server's.

#### 7.4.7. Client Key Exchange Message
- Always sent; sets premaster secret.
- For RSA: client generates 48-byte `PreMasterSecret` (client_version + 46 random), encrypts with server's public key.
- For Diffie-Hellman: sends public value (explicit or implicit).
- **Implementation Note**: RSA with PKCS#1 v1.5: server **SHOULD** treat incorrectly formatted blocks as random to avoid Bleichenbacher attack. Server **SHOULD** use RSA blinding to prevent timing attacks.
- **PreMasterSecret version**: client must use version from ClientHello (not negotiated). Client implementations **MUST** check, server implementations **MAY** check (but randomize on error to avoid attack).

#### 7.4.8. Certificate Verify
- Sent after client certificate with signing capability; provides explicit verification.
- Contains signature over all handshake messages (including type and length fields) from client hello up to but not including this message.

#### 7.4.9. Finished
- Always sent immediately after ChangeCipherSpec.
- First record protected with new algorithms. Recipients **MUST** verify contents.
- `verify_data` = first 12 bytes of `PRF(master_secret, finished_label, MD5(handshake_messages) + SHA-1(handshake_messages))`.
- `finished_label` = "client finished" or "server finished".
- Fatal error if Finished not preceded by ChangeCipherSpec.

## 8. Cryptographic Computations
### 8.1. Computing the Master Secret
- `master_secret = PRF(pre_master_secret, "master secret", ClientHello.random + ServerHello.random)[0..47]`
- Premaster secret length varies by key exchange.
#### 8.1.1. RSA
- Client generates 48-byte premaster secret, encrypts with server public key (PKCS#1 block type 2). Server decrypts.
- RSA signatures use PKCS#1 block type 1.
#### 8.1.2. Diffie-Hellman
- Conventional DH computation; negotiated key (Z) used as premaster secret. Leading zero bytes stripped.

## 9. Mandatory Cipher Suites
- In absence of application profile, TLS compliant application **MUST** implement `TLS_RSA_WITH_3DES_EDE_CBC_SHA`.

## 10. Application Data Protocol
- Application data messages are transparent to record layer; fragmented, compressed, encrypted based on current state.

## 12. IANA Considerations
- Create registries: ClientCertificateType, Cipher Suite, ContentType, Alert, HandshakeType.
- Allocation policies as per RFC 2434 (Standards Action, Specification Required, Private Use).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations **MUST** implement TLS_RSA_WITH_3DES_EDE_CBC_SHA | must | Sec 9 |
| R2 | Record sequence numbers **MUST NOT** wrap; renegotiate if needed | must | Sec 6.1 |
| R3 | Per-record IV **SHOULD** be generated using one of two recommended methods | should | Sec 6.2.3.2 |
| R4 | Padding errors **MUST** use bad_record_mac alert | must | Sec 6.2.3.2 |
| R5 | Implementations **MUST** ensure record processing time same regardless of padding correctness | must | Sec 6.2.3.2 |
| R6 | Client **MUST** send ClientHello as first message | must | Sec 7.4.1.2 |
| R7 | Server **MUST** send certificate unless anonymous key exchange | must | Sec 7.4.2 |
| R8 | New ContentType, Alert, HandshakeType values **MUST** be defined by Standards Action | must | Sec 12 |
| R9 | Export cipher suites **MUST NOT** be negotiated in TLS 1.1 mode | must | Appendix A.5 |
| R10 | Client version in PreMasterSecret **MUST** be from ClientHello, not negotiated version | must | Sec 7.4.7.1 |

## Informative Annexes (Condensed)
- **Appendix A – Protocol Constant Values**: Complete structures for record layer, change cipher spec, alerts, handshake, cipher suites, security parameters. (Normative definitions preserved in structured form above.)
- **Appendix B – Glossary**: Definitions of key terms (AES, authentication, block cipher, CBC, certificate, etc.). (Summarized in main Definitions section.)
- **Appendix C – CipherSuite Definitions**: Table mapping cipher suite names to key exchange, cipher, hash, and key sizes. Key exchange algorithms: DHE_DSS, DHE_RSA, DH_anon, DH_DSS, DH_RSA, RSA, NULL. Cipher properties (key material, IV size, block size) listed.
- **Appendix D – Implementation Notes**: 
  - D.1: PRNG must be cryptographically secure; use secure hash operations; estimate seed bits.
  - D.2: Certificates must be integrity-verified; support revocation; users should view certificate info.
  - D.3: Many cipher suites provide minimal security; implementations should enforce minimum key sizes; anonymous DH strongly discouraged.
- **Appendix E – Backward Compatibility with SSL**: 
  - Describes interop with SSLv3/TLS 1.0; clients **SHOULD** send SSLv3 record format with version {3,2} for TLS 1.1.
  - TLS 1.1 clients supporting SSLv2 **MUST** send SSLv2 client hello; servers **SHOULD** accept both.
  - Version rollback protection using special PKCS#1 padding in SSLv2 compatibility mode.
- **Appendix F – Security Analysis**: 
  - Handshake authentication and key exchange modes (anonymous, RSA, DH) with security properties.
  - Version rollback attacks; detection via finished messages.
  - Session resumption security; master secret compromise countermeasures.
  - Use of both MD5 and SHA for conservative hashing.
  - Application data protection: MAC computed with sequence number, message type; independent write/read keys.
  - Explicit IVs defend against [CBCATT]; composite cipher modes (authenticate-then-encrypt) proven secure for stream ciphers and CBC with random IV.
  - Denial of service considerations; IPsec AH/ESP for termination attacks.
  - General caution: system only as strong as weakest algorithm; trustworthy functions required; choose acceptable certificates/authorities carefully.