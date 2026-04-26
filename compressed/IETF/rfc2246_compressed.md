# RFC 2246: The TLS Protocol Version 1.0
**Source**: IETF | **Version**: 1.0 | **Date**: January 1999 | **Type**: Normative (Standards Track)
**Original**: https://tools.ietf.org/html/rfc2246

## Scope (Summary)
This document specifies Version 1.0 of the Transport Layer Security (TLS) protocol, which provides communications privacy and data integrity over the Internet. The protocol consists of two layers: the TLS Record Protocol (providing connection security with symmetric encryption and keyed MACs) and the TLS Handshake Protocol (allowing server and client to authenticate each other and negotiate encryption algorithms and keys before any application data is transmitted).

## Normative References
- [DES] ANSI X3.106, "Data Link Encryption"
- [HMAC] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104
- [MD5] Rivest, R., "The MD5 Message Digest Algorithm", RFC 1321
- [PKCS1] RSA Laboratories, "PKCS #1: RSA Encryption Standard", version 1.5
- [PKIX] Housley, R., Ford, W., Polk, W. and D. Solo, "Internet Public Key Infrastructure: Part I: X.509 Certificate and CRL Profile", RFC 2459
- [RC2] Rivest, R., "A Description of the RC2(r) Encryption Algorithm", RFC 2268
- [RSA] R. Rivest, A. Shamir, and L. M. Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"
- [SHA] NIST FIPS PUB 180-1, "Secure Hash Standard"
- [SSL3] A. Frier, P. Karlton, and P. Kocher, "The SSL 3.0 Protocol"
- [TCP] Postel, J., "Transmission Control Protocol", STD 7, RFC 793
- [X509] CCITT Recommendation X.509: "The Directory - Authentication Framework"
- [XDR] Srinivansan, R., "XDR: External Data Representation Standard", RFC 1832

## Definitions and Abbreviations
- **TLS**: Transport Layer Security protocol, as specified herein.
- **Record Protocol**: Layered protocol that fragments, optionally compresses, applies a MAC, encrypts, and transmits data.
- **Handshake Protocol**: Suite of three sub-protocols (Change Cipher Spec, Alert, Handshake) for negotiating security parameters.
- **MAC**: Message Authentication Code; keyed secure digest.
- **PRF**: Pseudorandom Function used for key expansion and verification.
- **CipherSuite**: A 2-byte identifier defining a key exchange algorithm, a bulk encryption algorithm, and a MAC algorithm.
- **Session**: Association between client and server defined by a session identifier, peer certificate, compression method, cipher spec, master secret, and resumability flag.
- **Connection**: A transient peer-to-peer relationship associated with one session; each connection has read and write states.
- **Master Secret**: 48-byte secret shared between peers, derived from the pre-master secret via PRF.
- **Pre-master Secret**: Secret value (48 bytes for RSA, variable for DH) used to compute the master secret.

## Presentation Language (Section 4)
- All multi-byte values use network byte order (big endian).
- Vectors: fixed-length `T T'[n]` (n bytes); variable-length `T T'<floor..ceiling>` with length field preceding.
- Numbers: `uint8`, `uint16` (2 bytes), `uint24` (3 bytes), `uint32`, `uint64`.
- Enumerations: `enum { e1(v1), ... } Te`; occupy bytes based on maximal ordinal value.
- Constructed types: struct { ... } T; fields may be qualified with type name.
- Variants: `select (E) { case e1: Te1; ... }` based on an enumerated selector.
- Cryptographic attributes: `digitally-signed`, `stream-ciphered`, `block-ciphered`, `public-key-encrypted`.
- Constants: typed constants can be defined; under-specified types (opaque, variable-length vectors) cannot be assigned values.

## HMAC and the Pseudorandom Function (Section 5)
- **P_hash(secret, seed) = HMAC_hash(secret, A(1)+seed) + HMAC_hash(secret, A(2)+seed) + ...**, where A(0)=seed, A(i)=HMAC_hash(secret, A(i-1)).
- **PRF(secret, label, seed) = P_MD5(S1, label+seed) XOR P_SHA-1(S2, label+seed)**, where S1 and S2 are the two halves of the secret (rounded up).
- Label is an ASCII string without length byte or trailing null.

## The TLS Record Protocol (Section 6)
### Connection States (6.1)
- Four states: current read/write and pending read/write.
- Security parameters include: `ConnectionEnd`, `BulkCipherAlgorithm`, `CipherType`, `key_size`, `key_material_length`, `IsExportable`, `MACAlgorithm`, `hash_size`, `CompressionMethod`, master_secret, client_random, server_random.
- Record layer generates: client write MAC secret, server write MAC secret, client write key, server write key, client write IV (block ciphers only), server write IV.
- Each state includes: compression state, cipher state (with IV for CBC), MAC secret, sequence number (uint64, starts at 0).
- **The sequence number must be set to zero whenever a connection state is made active.**
- **It is illegal to make a state which has not been initialized with security parameters a current state.**

### Record Layer (6.2)
- Fragmentation: Records carry data in chunks of **2^14 bytes or less** (TLSPlaintext.length <= 2^14).
- Record structure: `ContentType` (change_cipher_spec(20), alert(21), handshake(22), application_data(23)), `ProtocolVersion` (major=3, minor=1), `length`, `fragment`.
- **Data of different TLS Record layer content types may be interleaved.**
- Compression: **Compression must be lossless and may not increase content length by more than 1024 bytes.** If decompressed length exceeds 2^14 bytes, report fatal `decompression_failure`.
- Encryption/MAC: TLSCompressed converted to TLSCiphertext; MAC includes sequence number.
- Stream ciphers: `GenericStreamCipher` includes content + MAC. For null cipher, MAC size is zero.
- Block ciphers: `GenericBlockCipher` includes content + MAC + padding. Padding must be filled with padding length value. The total structure must be a multiple of the cipher block length.
- **The IV for the first record is generated with keys; for subsequent records, IV is the last ciphertext block.**

### Key Calculation (6.3)
- `key_block = PRF(master_secret, "key expansion", server_random + client_random)`, partitioned into MAC secrets, keys, IVs.
- Exportable ciphers: `final_client_write_key = PRF(client_write_key, "client write key", client_random + server_random)`, similarly for server.
- Export IVs: `iv_block = PRF("", "IV block", client_random + server_random)`.

## The TLS Handshake Protocol (Section 7)
### Overview (7.3)
- Steps: exchange hello messages, exchange cryptographic parameters, exchange certificates, generate master secret, provide parameters to record layer, verify handshake.
- **Higher layers must be cognizant of their security requirements and never transmit information over a channel less secure than required.**
- Message flow diagrams (Figures 1 and 2) show full and abbreviated handshakes.

### Change Cipher Spec Protocol (7.1)
- Single message `{ type = change_cipher_spec(1) }`. Sent after security parameters agreed, before Finished.
- Upon reception, receiver immediately copies read pending state to current. Sender instructs record layer to make write pending state active.

### Alert Protocol (7.2)
- Alerts: `warning(1)` or `fatal(2)`. Fatal alerts cause immediate connection termination and session invalidation.
- Defined alerts: `close_notify`, `unexpected_message`, `bad_record_mac`, `decryption_failed`, `record_overflow`, `decompression_failure`, `handshake_failure`, `bad_certificate`, `unsupported_certificate`, `certificate_revoked`, `certificate_expired`, `certificate_unknown`, `illegal_parameter`, `unknown_ca`, `access_denied`, `decode_error`, `decrypt_error`, `export_restriction`, `protocol_version`, `insufficient_security`, `internal_error`, `user_canceled`, `no_renegotiation`.
- **The client and the server must share knowledge that the connection is ending to avoid truncation attack.** Both parties must send `close_notify` before closing write side.
- For errors without explicit level, sending party may determine level; fatal must be treated as fatal.

### Handshake Protocol (7.4)
- Handshake message types: `hello_request`, `client_hello`, `server_hello`, `certificate`, `server_key_exchange`, `certificate_request`, `server_hello_done`, `certificate_verify`, `client_key_exchange`, `finished`.
- **Sending handshake messages in an unexpected order results in a fatal error.**
- Hello messages: `ClientHello` includes version, random (32 bytes: 4-byte unix time + 28 random), session ID, cipher suites (ordered by preference), compression methods (must include null). `ServerHello` selects version (lower of client and server), session ID, cipher suite, compression method.
- Certificate message: The sender's certificate must come first in the list; each following certificate must directly certify the one preceding it.
- Server key exchange: sent only when certificate does not contain enough data (e.g., RSA_EXPORT with key >512 bits, DHE, DH_anon). Contains parameters signed with hello.random.
- Certificate request: optional, includes certificate types and distinguished names of acceptable CAs. **It is a fatal handshake_failure alert for an anonymous server to request client identification.**
- Client key exchange: For RSA, client generates 48-byte `PreMasterSecret` (version + 46 random), encrypts with server's public key. **Server should treat incorrectly formatted RSA blocks indistinguishably from correct ones (generate random 48-byte value).**
- Certificate verify: Used for client certificates with signing capability; signs all handshake messages.
- Finished: `verify_data = PRF(master_secret, finished_label, MD5(handshake_messages)+SHA-1(handshake_messages))[0..11]`. **It is a fatal error if a Finished message is not preceded by a Change Cipher Spec message.**

## Cryptographic Computations (Section 8)
- Master secret: `master_secret = PRF(pre_master_secret, "master secret", ClientHello.random + ServerHello.random)[0..47]`.
- RSA: pre_master_secret is 48 bytes; signing uses PKCS#1 block type 1, encryption uses block type 2.
- Diffie-Hellman: negotiated key (Z) is pre_master_secret; parameters may be ephemeral or in certificate.

## Mandatory Cipher Suites (Section 9)
- **A TLS compliant application MUST implement the cipher suite `TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA`.**

## Application Data Protocol (Section 10)
- Application data messages are fragmented, compressed, and encrypted based on current connection state; treated as transparent data.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Fragment records into chunks of 2^14 bytes or less. | must | Section 6.2.1 |
| R2 | Compression must be lossless and must not increase content length by more than 1024 bytes. | must | Section 6.2.2 |
| R3 | Decompression failure if fragment decompresses to >2^14 bytes. | must | Section 6.2.2 |
| R4 | Sequence number must be set to zero when connection state becomes active. | must | Section 6.1 |
| R5 | It is illegal to make an uninitialized state current. | must | Section 6.1 |
| R6 | Padding in GenericBlockCipher must be filled with padding length value. | must | Section 6.2.3.2 |
| R7 | Client and server must share knowledge of connection end (close_notify). | must | Section 7.2.1 |
| R8 | Fatal alert causes immediate connection termination and session invalidation. | must | Section 7.2 |
| R9 | Sending handshake messages in unexpected order results in fatal error. | must | Section 7.4 |
| R10 | Server should treat incorrectly formatted RSA blocks as correctly formatted (generate random 48-byte value). | should | Section 7.4.7.1 |
| R11 | Finished message must be preceded by Change Cipher Spec. | must | Section 7.4.9 |
| R12 | TLS compliant application MUST implement `TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA`. | must | Section 9 |

## Informative Annexes (Condensed)
- **Annex A (Protocol Constant Values)**: Defines exact structures and enumerations for record layer, change cipher spec, alerts, handshake messages, CipherSuite list, and SecurityParameters struct.
- **Annex B (Glossary)**: Defines terms such as application protocol, authentication, block cipher, CBC, certificate, client, connection, DES, DSS, digital signature, handshake, IV, MAC, master secret, MD5, one-way hash, public key, RC2, RC4, RSA, salt, session, SHA, SSL, stream cipher, TLS.
- **Annex C (CipherSuite Definitions)**: Table listing each CipherSuite with its exportability, key exchange algorithm, cipher, and hash. Also tables for key exchange descriptions, cipher properties (key material, effective key bits, IV size, block size), and hash sizes.
- **Annex D (Implementation Notes)**: Recommends temporary RSA keys be changed often (daily or every 500 transactions); suggests using a low-priority process for key generation. Notes secure seeding of PRNG and warns about order-independent seeding in RSAREF/BSAFE. Emphasizes certificate verification and careful selection of trusted CAs. Recommends limiting cipher suites to strong ones; discourages 40-bit keys and anonymous DH.
- **Annex E (Backward Compatibility With SSL)**: Describes how TLS 1.0 and SSL 3.0 interoperate using version field {3,1}. Specifies format for SSL 2.0 client hello and mechanism to avoid version rollback attacks by setting specific padding bytes in PKCS#1 encryption.
- **Annex F (Security Analysis)**: Discusses handshake protocol security against eavesdropping, man-in-the-middle, version rollback, and replay attacks. Notes that anonymous key exchange is vulnerable to active attacks. Recommends session ID lifetime of 24 hours. Emphasizes conservative use of both MD5 and SHA.
- **Annex G (Patent Statement)**: Notes patents held by RSA Data Security (U.S. Patent 4,405,829) and Netscape Communications (U.S. Patent 5,657,390). Netscape grants royalty-free license under certain conditions for implementing TLS.
- **Security Considerations**: Referenced throughout the memo.