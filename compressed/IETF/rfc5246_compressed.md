# RFC 5246: The Transport Layer Security (TLS) Protocol Version 1.2
**Source**: IETF | **Version**: 1.2 | **Date**: August 2008 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc5246

## Scope (Summary)
This document specifies Version 1.2 of the TLS protocol, which provides communications security over the Internet. The protocol allows client/server applications to communicate in a way designed to prevent eavesdropping, tampering, and message forgery.

## Normative References
- [AES] NIST FIPS 197 (AES)
- [3DES] NIST SP 800-67 (Triple DES)
- [DSS] NIST FIPS PUB 186-2 (Digital Signature Standard)
- [HMAC] RFC 2104 (HMAC)
- [MD5] RFC 1321 (MD5)
- [PKCS1] RFC 3447 (RSA Cryptography v2.1)
- [PKIX] RFC 3280 (X.509 PKI)
- [SCH] Schneier, Applied Cryptography, 2nd ed.
- [SHS] NIST FIPS PUB 180-2 (Secure Hash Standard)
- [REQ] RFC 2119 (Key words for requirements)
- [RFC2434] RFC 2434 (IANA Considerations)
- [X680] ITU-T X.680 (ASN.1)
- [X690] ITU-T X.690 (ASN.1 encoding)

## Definitions and Abbreviations
- **AEAD**: Authenticated Encryption with Additional Data
- **CBC**: Cipher Block Chaining
- **Cipher Suite**: A set of cryptographic algorithms (key exchange, bulk encryption, MAC, PRF)
- **Connection State**: Operating environment of the TLS Record Protocol (compression, encryption, MAC algorithms and keys)
- **Finished message**: First message protected with newly negotiated algorithms, used to verify handshake integrity
- **Handshake Protocol**: Protocol for negotiating security parameters and authenticating peers
- **HMAC**: Keyed-Hash Message Authentication Code
- **MAC**: Message Authentication Code
- **Master Secret**: 48-byte secret shared between peers, derived from premaster secret
- **PreMaster Secret**: Secret exchanged during handshake used to derive the master secret
- **PRF**: Pseudorandom Function for key expansion
- **Record Protocol**: Layer that fragments, compresses, encrypts, and transmits data
- **Session**: Association between client and server defining cryptographic parameters shared across multiple connections
- **TLS**: Transport Layer Security
- **Algorithm types**: ConnectionEnd (server/client), PRFAlgorithm, BulkCipherAlgorithm, CipherType (stream/block/aead), MACAlgorithm, CompressionMethod

## 1. Introduction
- **Primary goal**: Privacy and data integrity between two communicating applications.
- **Two layers**: TLS Record Protocol (fragmentation, compression, encryption, MAC) and TLS Handshake Protocol (authentication and key negotiation).
- The Record Protocol provides private (symmetric encryption) and reliable (keyed MAC) connections.
- The Handshake Protocol provides authenticated identity, secure shared secret negotiation, and reliable negotiation (no undetected modification).

### 1.1. Requirements Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

### 1.2. Major Differences from TLS 1.1
- MD5/SHA-1 PRF replaced with cipher-suite-specified PRF (all suites in this doc use P_SHA256).
- Digitally-signed elements now include explicit hash algorithm field.
- Cleaned up client/server negotiation of hash and signature algorithms.
- Support for AEAD modes added.
- TLS Extensions and AES Cipher Suites merged in.
- Tighter checking of EncryptedPreMasterSecret version numbers.
- Verify_data length depends on cipher suite (default 12).
- Many alerts now MUST be sent.
- Clients without certificates after a certificate_request MUST send an empty certificate list.
- Mandatory cipher suite: TLS_RSA_WITH_AES_128_CBC_SHA.
- Added HMAC-SHA256 cipher suites.
- Removed IDEA and DES cipher suites.
- SSLv2 backward-compatible hello: MAY (send), SHOULD NOT (initiate).
- Added limited "fall-through" in presentation language.
- Added Implementation Pitfalls section.

## 2. Goals (Summary)
1. Cryptographic security
2. Interoperability
3. Extensibility (framework for new algorithms)
4. Relative efficiency (session caching, reduced network activity)

## 3. Goals of This Document
- Define TLS 1.2 based on SSL 3.0; differences prevent interoperation but allow version fallback.
- Intended for implementors and cryptographers; algorithm-dependent data structures included in body.

## 4. Presentation Language
- **Basic block size**: 1 byte (8 bits), big-endian (network byte order).
- **Comments**: /* ... */.
- **Optional components**: [[ ]].
- **Vectors**: Fixed-length `T T'[n]`; variable-length `T'<floor..ceiling>` with length field.
- **Numbers**: uint8, uint16, uint24, uint32, uint64; unsigned, big-endian.
- **Enumerateds**: `enum { name(value), ... } Type;` width based on max ordinal.
- **Constructed types**: `struct { ... } [T];` with optional variant `select (E) { case ... }`.
- **Cryptographic attributes**: `digitally-signed`, `stream-ciphered`, `block-ciphered`, `aead-ciphered`, `public-key-encrypted`.

### 4.7. Cryptographic Attributes (Normative)
- **DigitallySigned**: Contains `SignatureAndHashAlgorithm algorithm` and `opaque signature<0..2^16-1>`.
  - RSA signing: RSASSA-PKCS1-v1_5; DigestInfo MUST be DER-encoded; for SHA-1, parameters field MUST be NULL, but implementations MUST accept both without and with NULL parameters.
  - DSA: 20 bytes SHA-1 hash run through DSA; produces r,s; signature is DER encoding of `Dss-Sig-Value`.
- **Stream cipher**: plaintext XORed with keystream.
- **Block cipher encryption**: all in CBC mode; plaintext must be multiple of block length.
- **AEAD encryption**: plaintext simultaneously encrypted and integrity protected; output generally larger.
- **Public key encryption**: encoded as opaque vector `0..2^16-1`; RSA uses RSAES-PKCS1-v1_5.

## 5. HMAC and the Pseudorandom Function
- **MAC**: HMAC based on a hash function. Other cipher suites MAY define own MAC.
- **PRF**: takes secret, seed, label; produces arbitrary length output. Defined as `P_hash(secret, label + seed)`.
  - All cipher suites in this document use P_SHA256.
  - New cipher suites MUST explicitly specify a PRF and SHOULD use TLS PRF with SHA-256 or stronger.
- **P_hash**: `HMAC_hash(secret, A(i) + seed)` where `A(0)=seed`, `A(i)=HMAC_hash(secret, A(i-1))`.
- **Label**: ASCII string without length byte or trailing null.

## 6. The TLS Record Protocol
- **Layered**: fragments, optionally compresses, applies MAC, encrypts, transmits. Received: decrypt, verify, decompress, reassemble, deliver.
- **Four protocols**: handshake, alert, change cipher spec, application data. Additional record content types can be registered via IANA.
- **Implementation restrictions**:
  - **MUST NOT** send record types not defined unless negotiated by extension.
  - **MUST** send `unexpected_message` alert if unexpected record type received.
  - Type and length of record not protected by encryption; application designers may pad or use cover traffic.

### 6.1. Connection States
- **Four states**: current read/write, pending read/write.
- **Security parameters** include: connection end, PRF algorithm, bulk encryption algorithm (key size, type, block size, IV lengths), MAC algorithm, compression algorithm, master secret (48 bytes), client random (32 bytes), server random (32 bytes).
- **Keys generated**: client write MAC key, server write MAC key, client write encryption key, server write encryption key, client write IV, server write IV.
- **Sequence numbers**: uint64, set to zero when state becomes active, increment after each record, MUST NOT wrap; if would wrap, must renegotiate.
- **MUST**: update connection state for each record.

### 6.2. Record Layer
- **Fragmentation**: Data fragmented into TLSPlaintext records of `2^14` bytes or less. Multiple messages of same ContentType may be coalesced or fragmented.
- **TLSPlaintext**: type (higher-level protocol), version (TLS 1.2 uses {3,3}), length (MUST NOT exceed `2^14`), fragment.
- **Zero-length fragments**: MUST NOT be sent for Handshake, Alert, or ChangeCipherSpec. Application data zero-length MAY be sent.
- **Interleaving**: Records must be delivered in same order as protected. Recipients MUST accept interleaved application data during subsequent handshakes.

### 6.2.2. Record Compression and Decompression
- All records compressed using current session compression algorithm; initially null.
- Compression must be lossless and may not increase content length by more than 1024 bytes.
- **MUST**: report fatal decompression failure if decompressed length > `2^14`.

### 6.2.3. Record Payload Protection
- **TLSCiphertext**: contains type, version, length (MUST NOT exceed `2^14+2048`), and fragment (select based on cipher_type).
- **GenericStreamCipher**: `content` + `MAC`. MAC computed over `seq_num + TLSCompressed.type + TLSCompressed.version + TLSCompressed.length + TLSCompressed.fragment`.
- **GenericBlockCipher**: IV (SHOULD be random, MUST be unpredictable) + block-ciphered content + MAC + padding + padding_length.
  - Padding: each byte set to padding length. Receiver MUST check padding and MUST use `bad_record_mac` alert for padding errors.
  - **MUST**: ensure record processing time essentially the same regardless of padding correctness (timing attack defense). Compute MAC even if padding incorrect.
- **GenericAEADCipher**: explicit nonce + AEAD-ciphered content. Nonce construction specified by cipher suite; implicit part derived from key_block. Additional authenticated data: `seq_num + type + version + length`. If decryption fails, **MUST** generate fatal `bad_record_mac` alert. Expansion MUST NOT exceed 1024 bytes.

### 6.3. Key Calculation
- **key_block** = `PRF(master_secret, "key expansion", server_random + client_random)`
- Partition: client_write_MAC_key, server_write_MAC_key, client_write_key, server_write_key, client_write_IV, server_write_IV.
- Currently, client_write_IV/server_write_IV only generated for implicit nonce techniques.

## 7. The TLS Handshaking Protocols
- **Three subprotocols**: Handshake Protocol, Change Cipher Spec Protocol, Alert Protocol.
- **Session items**: session identifier, peer certificate (may be null), compression method, cipher spec (PRF, bulk cipher, MAC), master secret, is resumable flag.

### 7.1. Change Cipher Spec Protocol
- Single message: one byte value 1.
- Sent by both client and server to notify that subsequent records will be protected under new CipherSpec.
- Reception causes receiver to copy read pending state to read current state.
- Sender MUST immediately make write pending state the write active state.
- Sent after security parameters agreed but before Finished message.
- Note: May need to buffer data briefly if other side is computing keys.

### 7.2. Alert Protocol
- **AlertLevel**: warning(1), fatal(2).
- **Fatal alerts**: immediate termination, session identifier MUST be invalidated.
- **Closing**: `close_notify` sent before closing write side; other party MUST respond with `close_notify` and close immediately. Data received after closure alert is ignored.
- **Error alerts**: Upon fatal alert, both parties forget session-identifiers, keys, secrets. Fatal alert MUST be sent before closing for defined conditions.
- **Warning alerts**: generally allow connection to continue; receiver SHOULD send fatal alert if unwilling to proceed.

#### 7.2.2. Error Alerts (Normative definitions)
- `unexpected_message`: fatal.
- `bad_record_mac`: fatal; also for invalid decryption or padding errors.
- `decryption_failed_RESERVED`: MUST NOT be sent.
- `record_overflow`: fatal; length > 2^14+2048 or decrypted > 2^14+1024.
- `decompression_failure`: fatal.
- `handshake_failure`: fatal.
- `no_certificate_RESERVED`: MUST NOT be sent.
- `bad_certificate`, `unsupported_certificate`, `certificate_revoked`, `certificate_expired`, `certificate_unknown`: various.
- `illegal_parameter`: fatal.
- `unknown_ca`: fatal.
- `access_denied`: fatal.
- `decode_error`: fatal.
- `decrypt_error`: fatal.
- `export_restriction_RESERVED`: MUST NOT be sent.
- `protocol_version`: fatal.
- `insufficient_security`: fatal.
- `internal_error`: fatal.
- `user_canceled`: warning; should be followed by `close_notify`.
- `no_renegotiation`: warning.
- `unsupported_extension`: fatal.

### 7.3. Handshake Protocol Overview
- Steps: exchange hello messages, exchange cryptographic parameters, optionally exchange certificates/authentication, generate master secret, provide parameters to record layer, verify handshake integrity via Finished messages.
- Application data **MUST NOT** be sent before first handshake completes (before non-null cipher suite established).
- Full handshake flow (Figure 1): ClientHello → ServerHello + Certificate + ServerKeyExchange* + CertificateRequest* + ServerHelloDone → Client Certificate* + ClientKeyExchange + CertificateVerify* + [ChangeCipherSpec] + Finished → [ChangeCipherSpec] + Finished → Application Data.
- Abbreviated handshake (session resumption, Figure 2): ClientHello (with session ID) → ServerHello (same session ID) → [ChangeCipherSpec] + Finished → [ChangeCipherSpec] + Finished → Application Data.

### 7.4. Handshake Protocol
- **HandshakeType**: hello_request(0), client_hello(1), server_hello(2), certificate(11), server_key_exchange(12), certificate_request(13), server_hello_done(14), certificate_verify(15), client_key_exchange(16), finished(20). New types assigned by IANA.
- Handshake messages must be sent in order; unexpected order causes fatal error. HelloRequest may be sent at any time but SHOULD be ignored if during handshake.

#### 7.4.1. Hello Messages
- Used to exchange security enhancement capabilities.

##### 7.4.1.1. Hello Request
- Server MAY send at any time; client SHOULD respond with ClientHello when convenient. Servers SHOULD NOT send immediately upon initial connection.
- Client may ignore if currently negotiating a session, or respond with `no_renegotiation` alert.
- After sending, servers SHOULD NOT repeat until subsequent handshake complete.
- **MUST NOT** be included in handshake message hashes.

##### 7.4.1.2. Client Hello
- **When sent**: First message from client, or in response to HelloRequest/renegotiation.
- **Structure**: `ProtocolVersion client_version` (SHOULD be latest supported), `Random` (32 bytes: gmt_unix_time + 28 random bytes), `SessionID session_id` (empty if no session), `CipherSuite cipher_suites<2..2^16-2>` (in preference order; if resuming MUST include cipher_suite from that session), `CompressionMethod compression_methods<1..2^8-1>` (MUST include null; if resuming MUST include compression_method from that session), optional `Extension extensions`.
- If session_id non-empty (resumption request), cipher_suites MUST include at least that session's cipher_suite; compression_methods MUST include that session's compression_method.
- Server MUST accept ClientHello with or without extensions; if extensions present, data must match format; else fatal `decode_error`.
- After sending, client waits for ServerHello; any other handshake message (except HelloRequest) is fatal error.

##### 7.4.1.3. Server Hello
- **When sent**: In response to ClientHello when acceptable algorithms found; else `handshake_failure` alert.
- **Structure**: `server_version` (lower of client suggested and server highest; for TLS 1.2 version = 3.3), `random` (independently generated), `session_id` (same as client if resuming; else new; may be empty to indicate no caching), `cipher_suite` (selected from client list; for resumed sessions, value from session state), `compression_method` (selected from client list; for resumed sessions, value from session state), optional extensions.
- **Resumption requirements**: If session resumed, it must be with same cipher suite originally negotiated.
- Clients **MUST** be prepared to do full negotiation during any handshake.

##### 7.4.1.4. Hello Extensions
- **Format**: `ExtensionType extension_type`, `opaque extension_data<0..2^16-1>`.
- **ExtensionType**: currently only `signature_algorithms(13)` defined in this document; others in [TLSEXT]. IANA registry.
- **Rules**: Extension type MUST NOT appear in ServerHello unless it appeared in corresponding ClientHello. If client receives unexpected extension, **MUST** abort with `unsupported_extension` fatal alert.
- Multiple extensions may appear in any order; no duplicates.
- Client requesting resumption SHOULD send same extensions as for full handshake.
- **Security considerations**: Active attackers can modify extensions until handshake authenticated. Use of extensions to change major design aspects is not recommended; better to define new TLS version.

###### 7.4.1.4.1. Signature Algorithms
- Client uses `signature_algorithms` extension to indicate acceptable signature/hash algorithm pairs.
- **HashAlgorithm**: none(0), md5(1), sha1(2), sha224(3), sha256(4), sha384(5), sha512(6), (255).
- **SignatureAlgorithm**: anonymous(0), rsa(1), dsa(2), ecdsa(3), (255).
- **supported_signature_algorithms**: list of `SignatureAndHashAlgorithm`, descending preference.
- If client does not send extension, server MUST behave as if client sent default: `{sha1,rsa}` for RSA-based key exchanges, `{sha1,dsa}` for DSA-based, `{sha1,ecdsa}` for ECDSA-based (see list for each key exchange algorithm).
- Clients **MUST NOT** offer this extension if offering TLS versions prior to 1.2. Servers **MUST NOT** send this extension. Servers **MUST** support receiving it.
- During session resumption, not included in ServerHello; server ignores in ClientHello.

#### 7.4.2. Server Certificate
- **When sent**: Must send whenever agreed key exchange method uses certificates (all except DH_anon). Immediately follows ServerHello.
- **Structure**: `ASN.1Cert certificate_list<0..2^24-1>` (chain; sender's certificate first; root CA may be omitted).
- **Rules**:
  - Certificate type MUST be X.509v3 unless negotiated otherwise.
  - End entity certificate's public key MUST be compatible with selected key exchange algorithm (detailed table in Section 7.4.2: e.g., RSA for RSA key exchange; DHE_RSA requires RSA signing key with digitalSignature bit; DHE_DSS requires DSA key; fixed DH requires DH key; ECDHE_ECDSA requires ECDSA key, etc.).
  - If client provided `signature_algorithms` extension, all server certificates MUST be signed by a hash/signature pair appearing in that extension.
  - Fixed DH certificates (DH_DSS, DH_RSA, ECDH_ECDSA, ECDH_RSA) MAY be signed with any hash/signature pair from the extension.
  - Server chooses certificate based on criteria; if single certificate, SHOULD validate it meets criteria.
  - Certain algorithm combinations (e.g., RSASSA-PSS) cannot currently be used with TLS.

#### 7.4.3. Server Key Exchange Message
- **When sent**: Only when server Certificate does not contain enough data for client to exchange premaster secret. For: DHE_DSS, DHE_RSA, DH_anon. Not legal for RSA, DH_DSS, DH_RSA. Other key exchange methods MUST specify.
- **Structure**: `ServerDHParams params` (dh_p, dh_g, dh_Ys) for anonymous; for signed variants, additionally `digitally-signed struct { client_random, server_random, params } signed_params`.
- **Signature**: If client offered `signature_algorithms` extension, the signature algorithm and hash algorithm MUST be a pair listed in that extension.
- Server MUST check candidate cipher suites against extension before selecting.
- Hash and signature algorithms MUST be compatible with server's end-entity certificate key.
- DSA signatures currently only used with SHA-1.

#### 7.4.4. Certificate Request
- **When sent**: Non-anonymous server may optionally request client certificate. Immediately after ServerKeyExchange (or after Certificate if no ServerKeyExchange).
- **Structure**: `ClientCertificateType certificate_types<1..2^8-1>`, `SignatureAndHashAlgorithm supported_signature_algorithms<2^16-1>`, `DistinguishedName certificate_authorities<0..2^16-1>`.
- **Rules**:
  - Any client certificates **MUST** be signed using a hash/signature pair found in `supported_signature_algorithms`.
  - End-entity certificate key **MUST** be compatible with `certificate_types`. If key is signature key, it MUST be usable with some pair in supported_signature_algorithms.
  - For historical types (e.g., rsa_fixed_dh), the certificate type no longer restricts signing algorithm; only key type matters.
- It is a fatal `handshake_failure` for anonymous server to request client authentication.

#### 7.4.5. Server Hello Done
- Server sends to indicate end of hello messages. After receiving, client SHOULD verify server certificate and hello parameters are acceptable.

#### 7.4.6. Client Certificate
- **When sent**: Only if server requests certificate. First message after ServerHelloDone. If no suitable certificate, **MUST** send empty certificate_list.
- Server may continue without client authentication or send fatal `handshake_failure`.
- Certificate type MUST be X.509v3 unless negotiated otherwise. End-entity key must be compatible with certificate types in CertificateRequest (table in Section 7.4.6).
- If certificate_authorities list non-empty, one certificate in chain SHOULD be issued by listed CA.
- Certificates **MUST** be signed using acceptable hash/signature pair (as per Section 7.4.4).

#### 7.4.7. Client Key Exchange Message
- **Always sent**: immediately after client certificate (if sent) or first after ServerHelloDone.
- **Select**: For RSA: `EncryptedPreMasterSecret`; for DH (dhe_dss, dhe_rsa, dh_dss, dh_rsa, dh_anon): `ClientDiffieHellmanPublic`.
- If client uses static DH (fixed_dh client auth), message **MUST** be sent but **MUST** be empty.

##### 7.4.7.1. RSA-Encrypted Premaster Secret
- Client generates 48-byte `PreMasterSecret` (version + 46 random bytes), encrypts with server's RSA public key.
- **Version**: Must be the version offered in ClientHello.client_version (not negotiated version). This prevents rollback attacks.
- **Implementation requirements**:
  - Client implementations **MUST** always send correct version number.
  - Servers with TLS 1.1+ **MUST** check version; for TLS ≤1.0, SHOULD check but MAY have config to disable.
  - If check fails, **MUST** randomize premaster secret as described (to avoid Bleichenbacher/Klima attacks). **MUST NOT** generate alert.
  - Use RSA blinding to prevent timing attacks.
- **Encoding**: Must include length bytes; differs from some SSLv3 implementations.

##### 7.4.7.2. Client Diffie-Hellman Public Value
- **PublicValueEncoding**: `implicit` (if client certificate contains DH key) → send empty; `explicit` → send `dh_Yc<1..2^16-1>`.

#### 7.4.8. Certificate Verify
- **When sent**: Only if client certificate has signing capability (not fixed DH). Immediately after ClientKeyExchange.
- **Structure**: `digitally-signed struct { opaque handshake_messages[] }`.
- `handshake_messages`: all handshake messages from ClientHello up to (not including) this message, including type and length fields.
- Hash and signature algorithms **MUST** be one of those in CertificateRequest's `supported_signature_algorithms` and compatible with client's end-entity certificate.
- DSA currently only used with SHA-1.

#### 7.4.9. Finished
- **When sent**: Immediately after ChangeCipherSpec. Verifies key exchange and authentication.
- **Structure**: `verify_data[verify_data_length]`. Computed as `PRF(master_secret, finished_label, Hash(handshake_messages))[0..verify_data_length-1]`.
- `finished_label`: "client finished" for client, "server finished" for server.
- Hash used must be the same as the basis for the PRF.
- `verify_data_length`: default 12; cipher suites may specify other length but MUST be at least 12 bytes.
- It is a fatal error if Finished not preceded by ChangeCipherSpec.
- Recipients **MUST** verify Finished contents; after both sides verified, application data may be sent.

## 8. Cryptographic Computations

### 8.1. Computing the Master Secret
- `master_secret = PRF(pre_master_secret, "master secret", ClientHello.random + ServerHello.random)[0..47]`; always exactly 48 bytes.
- Pre_master_secret length varies by key exchange method.

#### 8.1.1. RSA
- Client generates 48-byte pre_master_secret, encrypts under server's public key.

#### 8.1.2. Diffie-Hellman
- Conventional DH computation; negotiated key (Z) used as pre_master_secret. Leading zero bytes stripped before use.

## 9. Mandatory Cipher Suites
- In absence of application profile specifying otherwise, a TLS-compliant application **MUST** implement `TLS_RSA_WITH_AES_128_CBC_SHA`.

## 10. Application Data Protocol
- Application data messages carried by record layer; fragmented, compressed, encrypted based on current connection state.

## 11. Security Considerations
- Discussed throughout; especially Appendices D, E, and F.

## 12. IANA Considerations
- Registries: TLS ClientCertificateType Identifiers, TLS Cipher Suite, TLS ContentType, TLS Alert, TLS HandshakeType, TLS ExtensionType (including signature_algorithms), TLS SignatureAlgorithm, TLS HashAlgorithm. All with specified allocation policies.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST NOT send record types not defined in this document unless negotiated by extension. | MUST | 6 |
| R2 | If a TLS implementation receives an unexpected record type, it MUST send an unexpected_message alert. | MUST | 6 |
| R3 | Sequence numbers MUST be set to zero when a connection state is made active; MUST NOT wrap; if wrap would occur, must renegotiate. | MUST | 6.1 |
| R4 | A sequence number is incremented after each record. | MUST | 6.1 |
| R5 | Fragment length in TLSPlaintext MUST NOT exceed 2^14 bytes. | MUST | 6.2.1 |
| R6 | Implementations MUST NOT send zero-length fragments of Handshake, Alert, or ChangeCipherSpec content types. | MUST | 6.2.1 |
| R7 | Records MUST be delivered to the network in the same order as they are protected by the record layer. | MUST | 6.2.1 |
| R8 | Recipients MUST receive and process interleaved application layer traffic during handshakes subsequent to the first. | MUST | 6.2.1 |
| R9 | Compression must be lossless and may not increase content length by more than 1024 bytes. | MUST | 6.2.2 |
| R10 | If decompression function encounters a fragment that would decompress to length > 2^14, it MUST report a fatal decompression failure. | MUST | 6.2.2 |
| R11 | The IV in GenericBlockCipher SHOULD be chosen at random, and MUST be unpredictable. | MUST/SHOULD | 6.2.3.2 |
| R12 | Each uint8 in the padding data vector MUST be filled with the padding length value. | MUST | 6.2.3.2 |
| R13 | The receiver MUST check padding and MUST use bad_record_mac alert to indicate padding errors. | MUST | 6.2.3.2 |
| R14 | With block ciphers in CBC mode, it is critical that the entire plaintext of the record be known before any ciphertext is transmitted. | (critical note) | 6.2.3.2 |
| R15 | Implementations MUST ensure that record processing time is essentially the same whether or not the padding is correct. | MUST | 6.2.3.2 |
| R16 | If AEAD decryption fails, a fatal bad_record_mac alert MUST be generated. | MUST | 6.2.3.3 |
| R17 | Each AEAD cipher MUST NOT produce an expansion greater than 1024 bytes. | MUST | 6.2.3.3 |
| R18 | ChangeCipherSpec message: Reception causes receiver to instruct record layer to immediately copy the read pending state into the read current state. | MUST | 7.1 |
| R19 | Immediately after sending ChangeCipherSpec, the sender MUST instruct the record layer to make the write pending state the write active state. | MUST | 7.1 |
| R20 | Alert messages with level fatal result in immediate termination; session identifier MUST be invalidated. | MUST | 7.2 |
| R21 | Unless some other fatal alert has been transmitted, each party is required to send a close_notify alert before closing the write side. | REQUIRED | 7.2.1 |
| R22 | The other party MUST respond with a close_notify alert of its own and close down immediately. | MUST | 7.2.1 |
| R23 | Upon transmission or receipt of a fatal alert, both parties MUST forget any session-identifiers, keys, and secrets associated with a failed connection. | MUST | 7.2.2 |
| R24 | Whenever an implementation encounters a condition defined as a fatal alert, it MUST send the appropriate alert prior to closing. | MUST | 7.2.2 |
| R25 | The decryption_failed_RESERVED alert value MUST NOT be sent by compliant implementations. | MUST NOT | 7.2.2 |
| R26 | The no_certificate_RESERVED alert value MUST NOT be sent by compliant implementations. | MUST NOT | 7.2.2 |
| R27 | The export_restriction_RESERVED alert value MUST NOT be sent by compliant implementations. | MUST NOT | 7.2.2 |
| R28 | Application data MUST NOT be sent prior to completion of the first handshake (before cipher suite other than TLS_NULL_WITH_NULL_NULL established). | MUST NOT | 7.3 |
| R29 | Handshake messages MUST be sent in the order defined; unexpected order results in a fatal error. | MUST | 7.4 |
| R30 | HelloRequest message SHOULD be ignored by the client if it arrives in the middle of a handshake. | SHOULD | 7.4 |
| R31 | Servers SHOULD NOT send HelloRequest immediately upon initial connection. | SHOULD NOT | 7.4.1.1 |
| R32 | After sending HelloRequest, servers SHOULD NOT repeat the request until subsequent handshake is complete. | SHOULD NOT | 7.4.1.1 |
| R33 | HelloRequest MUST NOT be included in handshake message hashes. | MUST NOT | 7.4.1.1 |
| R34 | Client SHOULD send the latest (highest) version supported in client_version. | SHOULD | 7.4.1.2 |
| R35 | If session_id in ClientHello is non-empty (resumption), cipher_suites MUST include at least the cipher_suite from that session. | MUST | 7.4.1.2 |
| R36 | If session_id non-empty, compression_methods MUST include the compression_method from that session. | MUST | 7.4.1.2 |
| R37 | compression_methods MUST contain, and all implementations MUST support, CompressionMethod.null. | MUST | 7.4.1.2 |
| R38 | Server MUST accept ClientHello both with and without extensions; if data does not precisely match format, MUST send fatal "decode_error" alert. | MUST | 7.4.1.2 |
| R39 | After ClientHello, any handshake message from server except HelloRequest is treated as fatal error. | MUST | 7.4.1.2 |
| R40 | If server cannot find acceptable algorithms, respond with handshake_failure alert. | MUST | 7.4.1.3 |
| R41 | ServerHello.random MUST be independently generated from ClientHello.random. | MUST | 7.4.1.3 |
| R42 | If a session is resumed, it must be resumed using the same cipher suite it was originally negotiated with. | MUST | 7.4.1.3 |
| R43 | Clients MUST be prepared to do a full negotiation during any handshake. | MUST | 7.4.1.3 |
| R44 | An extension type MUST NOT appear in ServerHello unless it appeared in corresponding ClientHello. | MUST NOT | 7.4.1.4 |
| R45 | If client receives unexpected extension in ServerHello, MUST abort with unsupported_extension fatal alert. | MUST | 7.4.1.4 |
| R46 | There MUST NOT be more than one extension of the same type. | MUST NOT | 7.4.1.4 |
| R47 | If client does not send signature_algorithms extension, server MUST behave as if default sent as per key exchange algorithm. | MUST | 7.4.1.4.1 |
| R48 | Clients MUST NOT offer signature_algorithms extension if offering prior TLS versions. | MUST NOT | 7.4.1.4.1 |
| R49 | Servers MUST NOT send signature_algorithms extension. | MUST NOT | 7.4.1.4.1 |
| R50 | TLS servers MUST support receiving signature_algorithms extension. | MUST | 7.4.1.4.1 |
| R51 | Server MUST send Certificate message whenever agreed key exchange uses certificates (except DH_anon). | MUST | 7.4.2 |
| R52 | Certificate MUST be appropriate for negotiated cipher suite's key exchange algorithm and extensions. | MUST | 7.4.2 |
| R53 | If client provided signature_algorithms extension, all server certificates MUST be signed by hash/signature pair appearing in that extension. | MUST | 7.4.2 |
| R54 | ServerKeyExchange is not legal for RSA, DH_DSS, DH_RSA key exchanges. | MUST NOT | 7.4.3 |
| R55 | If client offered signature_algorithms extension, the signature algorithm and hash algorithm in ServerKeyExchange MUST be a pair listed in that extension. | MUST | 7.4.3 |
| R56 | Server MUST check candidate cipher suites against signature_algorithms extension before selecting. | MUST | 7.4.3 |
| R57 | It is a fatal handshake_failure alert for an anonymous server to request client authentication. | (fatal error) | 7.4.4 |
| R58 | If no suitable certificate available after server request, client MUST send Certificate message with empty certificate_list. | MUST | 7.4.6 |
| R59 | In RSA EncryptedPreMasterSecret, client implementations MUST always send correct version number (from ClientHello.client_version). | MUST | 7.4.7.1 |
| R60 | Server implementations with TLS 1.1 or higher MUST check version number; SHOULD check for ≤1.0 but MAY have config to disable. | MUST/SHOULD | 7.4.7.1 |
| R61 | If version check fails, server MUST NOT generate alert; MUST continue with randomized premaster secret. | MUST NOT/MUST | 7.4.7.1 |
| R62 | Implementations that use static RSA keys MUST use RSA blinding or other anti-timing technique. | MUST | 7.4.7.1 |
| R63 | If client certificate has signing capability, CertificateVerify message MUST be sent. | MUST | 7.4.8 |
| R64 | In CertificateVerify, hash/signature algorithms MUST be one of those in CertificateRequest's supported_signature_algorithms and compatible with client certificate key. | MUST | 7.4.8 |
| R65 | A Finished message is always sent immediately after a ChangeCipherSpec. | MUST | 7.4.9 |
| R66 | Recipients of Finished messages MUST verify that the contents are correct. | MUST | 7.4.9 |
| R67 | It is a fatal error if Finished is not preceded by ChangeCipherSpec at appropriate point. | (fatal) | 7.4.9 |
| R68 | In absence of application profile specifying otherwise, a TLS-compliant application MUST implement TLS_RSA_WITH_AES_128_CBC_SHA. | MUST | 9 |
| R69 | Application data messages are treated as transparent data to the record layer. | (definition) | 10 |

## Informative Annexes (Condensed)
- **Appendix A. Protocol Data Structures and Constant Values**: Provides formal definitions of all protocol structures: Record Layer (TLSPlaintext, TLSCompressed, TLSCiphertext, GenericStreamCipher, GenericBlockCipher, GenericAEADCipher), Change Cipher Specs, Alert Messages, Handshake Protocol (all message types), Cipher Suite definitions (list of assigned values), Security Parameters struct, and changes to RFC 4492 (elliptic curve cipher suites) to align with TLS 1.2.
- **Appendix B. Glossary**: Defines key terms: AES, application protocol, asymmetric cipher, AEAD, authentication, block cipher, bulk cipher, CBC, certificate, client, client write key/MAC key, connection, DES, 3DES, DSS, digital signatures, handshake, IV, MAC, master secret, MD5, public key cryptography, one-way hash function, RC4, RSA, server, session, session identifier, server write key/MAC key, SHA, SHA-256, SSL, stream cipher, symmetric cipher, TLS.
- **Appendix C. Cipher Suite Definitions**: Tabular listing of all cipher suites with key exchange algorithm, cipher type, MAC, Key Material, IV Size, Block Size, MAC algorithm lengths. Includes NULL, RC4, 3DES, AES variants with SHA-1 and SHA-256.
- **Appendix D. Implementation Notes**: Recommends cryptographically secure PRNG (e.g., based on SHA-1), careful seeding; certificate verification and support for revocation; caution about anonymous Diffie-Hellman; minimum key size recommendations. **D.4 (Implementation Pitfalls)** lists common mistakes: handling fragmented handshake messages, ignoring record layer version before ServerHello, handling extensions, supporting renegotiation, sending empty Certificate when no client certificate available, proper RSA premaster secret version handling, timing attack countermeasures, RSA signature verification (accept both NULL and missing parameters), DH leading zero stripping, DH parameter validation by client, unpredictable IV generation, long CBC padding acceptance, CBC timing attack mitigation, strong random number generation.
- **Appendix E. Backward Compatibility**: Describes version negotiation mechanism. **E.1**: TLS 1.2 clients use {3,3} in ClientHello; if server supports lower version, it responds with that version; if client doesn't support, MUST send `protocol_version` alert and close. Servers receiving higher version than supported MUST reply with highest supported. Servers MUST accept any {03,XX} record layer version for ClientHello. **E.2 (SSL 2.0 Compatibility)**: TLS 1.2 clients supporting SSL 2.0 MAY send Version 2.0 CLIENT-HELLO; TLS 1.2 clients SHOULD NOT support SSL 2.0. The message format is specified; TLS servers may accept it even if not supporting SSL 2.0. **E.3 (Version Rollback Prevention)**: TLS clients falling back to SSL 2.0 must set rightmost 8 random bytes of PKCS padding to 0x03; TLS-capable servers SHOULD check these bytes; if not 0x03, server SHOULD randomize key data and continue handshake.
- **Appendix F. Security Analysis**: **F.1 (Handshake Protocol)**: Describes authentication modes (both, server-only, anonymous). Anonymous connections vulnerable to man-in-the-middle. RSA key exchange provides server authentication but not perfect forward secrecy; DHE provides forward secrecy. DH with fixed certificates must be careful of small subgroup attacks; implementations SHOULD generate fresh DH private key for each handshake. Client SHOULD verify DH group and public exponent size. **F.1.2 (Version Rollback)**: SSL 2.0 fallback attack mitigated by PKCS padding check. **F.1.3 (Detecting Attacks)**: Handshake message hashes ensure detection of modification; cannot be repaired without master_secret. **F.1.4 (Resuming Sessions)**: Security relies on master_secret not compromised; upper limit of 24 hours suggested for session ID lifetimes. **F.2 (Protecting Application Data)**: MAC computed with sequence number, message type, etc.; prevents replay, reorder, deletion. Independent MAC keys for each direction. **F.3 (Explicit IVs)**: Explicit IVs prevent chosen plaintext attack possible in earlier versions. **F.4 (Composite Cipher Modes)**: TLS uses authenticate-then-encrypt; proven secure for stream ciphers and CBC with secure block cipher and unpredictable IV. **F.5 (Denial of Service)**: Vulnerable to DoS via RSA decryption CPU load; TCP SYN randomization helps; IPsec AH/ESP can defend against connection attacks. **F.6 (Final Notes)**: System security depends on weakest algorithm; dishonest CA can cause damage.