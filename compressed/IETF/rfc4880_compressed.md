# RFC 4880: OpenPGP Message Format
**Source**: IETF | **Version**: Standards Track | **Date**: November 2007 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4880

## Scope (Summary)
This document specifies the message formats for OpenPGP, which uses public-key and symmetric cryptography to provide confidentiality, key management, authentication, and digital signatures for electronic communications and data storage. It defines packet formats, signature types, key structures, and encoding methods necessary for interoperable applications.

## Normative References
- [RFC1991] – PGP Message Exchange Formats (Informative)
- [RFC2440] – OpenPGP Message Format (Informative)
- [RFC1950] – ZLIB Compressed Data Format
- [RFC1951] – DEFLATE Compressed Data Format
- [RFC2045] – MIME Base64
- [RFC2119] – Key words for requirement levels
- [RFC2434] – IANA Considerations
- [RFC2822] – Internet Message Format
- [RFC3447] – PKCS#1 v2.1
- [RFC3629] – UTF-8
- [RFC4086] – Randomness Requirements
- [FIPS180] – Secure Hash Standard
- [FIPS186] – Digital Signature Standard
- [HAC] – Handbook of Applied Cryptography
- [ISO10646] – Unicode
- [AES], [BLOWFISH], [BZ2], [ELGAMAL], [IDEA], [JFIF], [TWOFISH] – Algorithm specifications

## Definitions and Abbreviations
- **OpenPGP**: Security software based on PGP 5.x, formalized in RFC 2440 and this document.
- **PGP**: Pretty Good Privacy; family of software by Philip Zimmermann.
- **PGP 2.6.x**: Earlier version using RSA, MD5, IDEA.
- **PGP 5.x**: Version formerly known as PGP 3, introduced new formats.
- **GnuPG (GPG)**: OpenPGP implementation avoiding encumbered algorithms.
- **Session key**: Symmetric key used for one message.
- **Packet**: Chunk of data with a tag; basic unit of OpenPGP messages.
- **Key ID**: 8-octet identifier for a key.
- **S2K**: String-to-key specifier for converting passphrases to symmetric keys.
- **Radix-64**: ASCII armor encoding; base64 plus CRC-24.
- **MPI**: Multi-precision integer.
- **CFB**: Cipher Feedback mode.

## 1. Introduction
- This document is a revision of RFC 2440, replacing it. It describes packet formats for encryption, decryption, signing, and key management.
- Key terms: OpenPGP, PGP, PGP 2.6.x, PGP 5.x, GnuPG.
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are as per RFC 2119.
- Namespace allocation terms as per RFC 2434.

## 2. General Functions
- OpenPGP provides: digital signatures, encryption, compression, Radix-64 conversion. Also key management but beyond scope.

### 2.1 Confidentiality via Encryption
- Session key is generated randomly for each message, encrypted with recipient's public key. Message encrypted with session key.
- Symmetric encryption from passphrase or shared secret also possible.
- Both signature and encryption can be applied to same message (sign first, then encrypt).

### 2.2 Authentication via Digital Signature
- Hash of message signed with sender's private key. Receiver verifies.

### 2.3 Compression
- **SHOULD** compress after signing but before encryption.
- Decompression **should** be implemented even if compression not; compression thwarts some attacks.
- Non-normative: Attacks can be prevented by MDC.

### 2.4 Conversion to Radix-64
- **SHOULD** provide Radix-64 conversions.

### 2.5 Signature-Only Applications
- Subset implementations that omit encryption are reasonable but non-conformant.

## 3. Data Element Formats
### 3.1 Scalar Numbers
- Unsigned, big-endian. Two-octet and four-octet definitions given.

### 3.2 Multiprecision Integers (MPIs)
- Two-octet length (bits) followed by big-endian octets.
- Unused bits **MUST** be zero. Length from most significant non-zero bit.

### 3.3 Key IDs
- Eight-octet scalar. **SHOULD NOT** assume uniqueness.

### 3.4 Text
- Unless specified, character set is UTF-8.

### 3.5 Time Fields
- Unsigned four-octet number: seconds since 1970-01-01 UTC.

### 3.6 Keyrings
- Collection of keys; sequential list or database. Beyond scope.

### 3.7 String-to-Key (S2K) Specifiers
- Used to convert passphrases to keys for private key encryption and symmetric message encryption.

#### 3.7.1 S2K Specifier Types
- 0: Simple S2K
- 1: Salted S2K
- 2: Reserved
- 3: Iterated and Salted S2K
- 100-110: Private/Experimental

#### 3.7.1.1 Simple S2K
- Direct hash of passphrase. If hash size > key size, use high-order octets; if smaller, concatenate multiple hashes with preloading of zeros.

#### 3.7.1.2 Salted S2K
- 8-octet salt hashed with passphrase.

#### 3.7.1.3 Iterated and Salted S2K
- Salt and passphrase hashed repeatedly according to coded count. Count formula provided.

#### 3.7.2 Usage
- **SHOULD** use salted or iterated-salted; simple is vulnerable.
- **3.7.2.1 Secret-Key Encryption**: Special values 254/255 indicate S2K specifier. Backward compatibility with old format (cipher alg + MD5) deprecated, **SHOULD NOT** be generated.
- **3.7.2.2 Symmetric-Key Message Encryption**: Allows passphrase or public-key decryption. PGP 2.x used IDEA with Simple S2K; deprecated but **MAY** be used.

## 4. Packet Syntax
### 4.1 Overview
- Message consists of packets. Each packet has header and body.

### 4.2 Packet Headers
- First octet: Packet Tag: bit 7 always 1, bit 6 indicates new format.
- Old format: bits 5-2 = tag, bits 1-0 = length type (0,1,2,3).
- New format: bits 5-0 = tag.
- **RECOMMENDED** to use new format if interoperability not an issue. Tags >= 16 must use new format.

#### 4.2.1 Old Format Packet Lengths
- 0: one-octet length; 1: two-octet; 2: four-octet; 3: indeterminate (not recommended).

#### 4.2.2 New Format Packet Lengths
- 1-octet: 0-191 octets.
- 2-octet: 192-8383 octets.
- 5-octet: up to 4,294,967,295 octets.
- Partial Body Lengths: for streaming; last length must not be partial. Minimum first partial length 512 octets. **MUST NOT** be used for non-data packets.

### 4.3 Packet Tags
- Defined tags (decimal): 0 Reserved, 1 PKESK, 2 Signature, 3 SKESK, 4 One-Pass Signature, 5 Secret-Key, 6 Public-Key, 7 Secret-Subkey, 8 Compressed Data, 9 Sym. Encrypted Data, 10 Marker, 11 Literal Data, 12 Trust, 13 User ID, 14 Public-Subkey, 17 User Attribute, 18 Sym. Encrypted Integrity Protected Data, 19 Modification Detection Code, 60-63 Private/Experimental.

## 5. Packet Types
### 5.1 Public-Key Encrypted Session Key Packet (Tag 1)
- Contains session key encrypted to recipient's public key.
- Version 3 defined. Body: version, Key ID, public-key algorithm, encrypted session key (PKCS#1 encoding for RSA; Elgamal specific fields).
- **MUST** make new PKCS#1 encoding for each key if multiple recipients. Key ID of zero allowed as wildcard.

### 5.2 Signature Packet (Tag 2)
- Binds key to data. Two versions: V3 (basic), V4 (expandable with subpackets).
- **SHOULD** accept V3, **SHOULD** generate V4.

#### 5.2.1 Signature Types
- 0x00: binary document; 0x01: canonical text; 0x02: standalone; 0x10-0x13: certifications (generic, persona, casual, positive); 0x18: subkey binding; 0x19: primary key binding; 0x1F: direct on key; 0x20: key revocation; 0x28: subkey revocation; 0x30: certification revocation; 0x40: timestamp; 0x50: third-party confirmation.

#### 5.2.2 Version 3 Signature Packet Format
- Fields: version (3), length (5), signature type, creation time, key ID, public-key algorithm, hash algorithm, left 16 bits of hash, MPIs (RSA or DSA).
- Hash includes data + signature type + creation time.
- RSA uses PKCS#1 EMSA-PKCS1-v1_5 with defined OIDs. DSA uses hash size equal to q; if larger, truncate.

#### 5.2.3 Version 4 Signature Packet Format
- Fields: version (4), signature type, public-key algorithm, hash algorithm, hashed subpacket count, hashed subpackets, unhashed subpacket count, unhashed subpackets, left 16 bits of hash, MPIs.
- Hash includes data from version through hashed subpackets.

##### 5.2.3.1 Signature Subpacket Specification
- Subpacket header: length (1,2,5 octets) + type (1 octet). Length format similar to new packet lengths.
- Types: 2=Creation Time, 3=Expiration Time, 4=Exportable Certification, 5=Trust, 6=Regular Expression, 7=Revocable, 9=Key Expiration, 10=Placeholder, 11=Preferred Sym. Alg., 12=Revocation Key, 16=Issuer, 20=Notation Data, 21=Preferred Hash, 22=Preferred Compression, 23=Key Server Preferences, 24=Preferred Key Server, 25=Primary User ID, 26=Policy URI, 27=Key Flags, 28=Signer's User ID, 29=Reason for Revocation, 30=Features, 31=Signature Target, 32=Embedded Signature.
- **SHOULD** ignore unknown types. Bit 7 is critical; if set on unknown subpacket, signature considered error.
- **SHOULD** implement preferred algorithm subpackets (11,21,22) and Reason for Revocation.

##### 5.2.3.3 Notes on Self-Signatures
- Self-signatures (certification, direct-key, subkey binding) contain preferences; implementers should interpret narrowly per User ID.
- Revoking self-signature retires that user ID or subkey.
- **SHOULD** allow rewriting self-signature; **RECOMMENDED** priority to most recent self-signature.

##### 5.2.3.4 Signature Creation Time
- **MUST** be present in hashed area.

##### 5.2.3.5 Issuer
- 8-octet Key ID of signing key.

##### 5.2.3.6 Key Expiration Time
- Seconds after creation; zero = never expires. Only on self-signature.

##### 5.2.3.7 Preferred Symmetric Algorithms
- Ordered list of algorithm numbers; only on self-signature.

##### 5.2.3.8 Preferred Hash Algorithms
- Ordered list; only on self-signature.

##### 5.2.3.9 Preferred Compression Algorithms
- Ordered list; if absent, ZIP preferred; 0 = uncompressed. Only on self-signature.

##### 5.2.3.10 Signature Expiration Time
- Seconds after creation; zero = never expires.

##### 5.2.3.11 Exportable Certification
- 1 octet: 0=non-exportable, 1=exportable. If absent, exportable. Local certifications trimmed on export/import.

##### 5.2.3.12 Revocable
- 1 octet: 0=not revocable, 1=revocable. If absent, revocable.

##### 5.2.3.13 Trust Signature
- Level (depth) and trust amount. Level >0 asserts key as trusted introducer. **SHOULD** emit 60 for partial, 120 for complete trust.

##### 5.2.3.14 Regular Expression
- Null-terminated regex limiting scope of trust. Syntax from Henry Spencer's regex.

##### 5.2.3.15 Revocation Key
- Class (bit 0x80 set; bit 0x40 sensitive), algorithm, 20-octet fingerprint. If sensitive, **SHOULD NOT** export except when needed.

##### 5.2.3.16 Notation Data
- Flags (0x80 = human-readable), name length, value length, name, value. Namespaces: IETF (no '@') and user (tag@domain). Undefined flags **MUST** be zero. Criticality applies to specific notation.

##### 5.2.3.17 Key Server Preferences
- N octets of flags. Defined: 0x80 = No-modify. Only on self-signature.

##### 5.2.3.18 Preferred Key Server
- URI of preferred key server.

##### 5.2.3.19 Primary User ID
- Boolean flag: 1 if primary. If multiple primaries, **RECOMMENDED** most recent self-signature. Separate for User ID and User Attribute.

##### 5.2.3.20 Policy URI
- URI of policy document.

##### 5.2.3.21 Key Flags
- N octets of flags: 0x01=certify, 0x02=sign, 0x04=encrypt communications, 0x08=encrypt storage, 0x10=split key, 0x20=authentication, 0x80=group key. **MUST NOT** assume fixed size. Split/group flags only on self-signature (direct-key or subkey).

##### 5.2.3.22 Signer's User ID
- String indicating which User ID responsible for signing.

##### 5.2.3.23 Reason for Revocation
- Revocation code (0=unspecified, 1=superseded, 2=compromised, 3=retired, 32=User ID info invalid, 100-110=Private Use) and human-readable string (UTF-8). **SHOULD** implement and include in revocation signatures.

##### 5.2.3.24 Features
- N octets of flags: 0x01 = Modification Detection. Only in self-signature. **SHOULD NOT** use feature if recipient doesn't state support. **SHOULD** implement if any defined feature used.

##### 5.2.3.25 Signature Target
- Public-key algorithm, hash algorithm, hash of target signature.

##### 5.2.3.26 Embedded Signature
- Complete Signature packet body.

#### 5.2.4 Computing Signatures
- Hash data includes appropriate prefix octets (0x99 for keys, 0xB4 for User ID, 0xD1 for User Attribute, 0x88 for Signature packets) and lengths. Then trailer: V3 hashes signature type + time; V4 hashes from version through hashed subpackets plus six-octet trailer (0x04, 0xFF, 4-octet length).

##### 5.2.4.1 Subpacket Hints
- **SHOULD** use last subpacket in case of conflict; **MAY** use any sensible resolution.

### 5.3 Symmetric-Key Encrypted Session Key Packet (Tag 3)
- Version 4 only. Contains symmetric algorithm, S2K specifier, optionally encrypted session key. If session key absent, S2K output is key. S2K **MUST** use salt.

### 5.4 One-Pass Signature Packet (Tag 4)
- Version 3. Contains signature type, hash algorithm, public-key algorithm, signing key ID, nested flag. Used for one-pass signing.

### 5.5 Key Material Packet
#### 5.5.1 Variants
- Tag 6: Public-Key; Tag 14: Public-Subkey; Tag 5: Secret-Key; Tag 7: Secret-Subkey.

#### 5.5.2 Public-Key Packet Formats
- V3 keys: deprecated, **MUST NOT** generate, **MAY** accept. Contain version, creation time, validity (days), algorithm, MPIs (RSA n,e). Weaknesses: Key ID = low 64 bits of modulus; fingerprint collision; MD5 weaknesses.
- V4 keys: **MUST** create. Contain version, creation time, algorithm, algorithm-specific MPIs (RSA: n,e; DSA: p,q,g,y; Elgamal: p,g,y).

#### 5.5.3 Secret-Key Packet Formats
- Includes Public-Key packet plus: S2K usage (0=unencrypted, 255/254=S2K specifier, other = cipher alg), optional IV, encrypted or plain MPIs (RSA: d,p,q,u; DSA: x; Elgamal: x). Checksum (2-octet sum) or SHA-1 hash (if usage 254). **SHOULD** use SHA-1 hash; checksum deprecated. V3: MPI bit count not encrypted; V4: all MPI data encrypted.

### 5.6 Compressed Data Packet (Tag 8)
- Algorithm octet (0=uncompressed, 1=ZIP, 2=ZLIB, 3=BZip2) followed by compressed data.

### 5.7 Symmetrically Encrypted Data Packet (Tag 9)
- Encrypted data in OpenPGP CFB mode with IV of zeros and random prefix (BS+2 octets, last two repeat). Quick check: duplicates two octets.

### 5.8 Marker Packet (Tag 10)
- Body: 0x50, 0x47, 0x50 ("PGP"). **MUST** be ignored. Used to indicate newer features.

### 5.9 Literal Data Packet (Tag 11)
- Format field: 'b' binary, 't' text, 'u' UTF-8 text. Deprecated 'l' local. Then filename (length + string; "_CONSOLE" for eyes-only), date (4 octets), literal data. Text stored with <CR><LF>; receiver converts.

### 5.10 Trust Packet (Tag 12)
- Implementation-defined, used only in keyrings. **SHOULD NOT** be exported; **SHOULD** be ignored on non-local input.

### 5.11 User ID Packet (Tag 13)
- UTF-8 text representing name and email. Typically RFC 2822 mail name-addr.

### 5.12 User Attribute Packet (Tag 17)
- Contains subpackets: length, type, data. Only defined type is 1 = Image Attribute. **SHOULD** handle certifications on these packets (treat as opaque User ID).

#### 5.12.1 Image Attribute Subpacket
- Header: little-endian length, version (1), encoding (1=JPEG), 12 reserved octets (must be 0). Image data in JFIF format.

### 5.13 Sym. Encrypted Integrity Protected Data Packet (Tag 18)
- Version 1. Uses CFB with random prefix (BS+2) but no resync after prefix. Plaintext includes SHA-1 hash of prefix + plaintext + tag+length of MDC packet (0xD3,0x14). MDC packet MUST be last. On decryption, compare hash; failure **MUST** be treated as security problem.
- **MUST** support decrypting; **SHOULD** prefer generating over Tag 9. **SHOULD** denote support (e.g., via Features subpacket).
- Non-normative explanation: MDC provides integrity without signature, preserves deniability. Hard-defines SHA-1 to avoid downgrade attacks.

### 5.14 Modification Detection Code Packet (Tag 19)
- 20-octet SHA-1 hash. **MUST** be last packet in encrypted plaintext and appear nowhere else. **MUST** use new format encoding with one-octet length.

## 6. Radix-64 Conversions
- Base64 encoding of binary data plus 24-bit CRC (generator 0x864CFB, init 0xB704CE). Checksum prefixed with '=' may appear after base64 data.

### 6.1 CRC-24 Implementation in C
- Provided as code snippet.

### 6.2 Forming ASCII Armor
- Header line surrounded by five dashes, blank line, base64 data, checksum, tail.
- Header types: "BEGIN PGP MESSAGE", "PUBLIC KEY BLOCK", "PRIVATE KEY BLOCK", "MESSAGE, PART X/Y", "MESSAGE, PART X", "SIGNATURE".
- Armor Headers: key-value pairs separated by ": ". Defined keys: Version, Comment, MessageID (32-character, deterministic), Hash (comma-separated), Charset.
- Tail line replaces "BEGIN" with "END".

### 6.3 Encoding Binary in Radix-64
- 24-bit groups -> 4 characters per table. Lines <=76 characters. Padding with '=' for incomplete groups.

### 6.4 Decoding Radix-64
- Ignore whitespace. Invalid characters **may** indicate error.

### 6.5 Examples provided.

### 6.6 Example of ASCII Armored Message (with extra indenting noted).

## 7. Cleartext Signature Framework
- Allows signing text without armor. Format:
   -----BEGIN PGP SIGNED MESSAGE-----
   Hash: algorithm(s)
   (blank line)
   dash-escaped cleartext
   -----BEGIN PGP SIGNATURE-----
   ...
   -----END PGP SIGNATURE-----

### 7.1 Dash-Escaped Text
- Lines starting with '-' are prefixed with "- ". **SHOULD** escape lines starting with "From ". **MUST** escape lines starting with '-'. Hash computed on original cleartext, not escaped. Trailing whitespace removed. Line ending before signature header not included.

## 8. Regular Expressions
- Syntax: branches separated by '|', pieces with '*','+','?', atoms (parentheses, range, '.', '^', '$', '\' + char, literal). Range: characters in '[]', with '-' for range, '^' for negation.

## 9. Constants
### 9.1 Public-Key Algorithms
- 1 RSA (Encrypt or Sign), 2 RSA Encrypt-Only (deprecated), 3 RSA Sign-Only (deprecated), 16 Elgamal (Encrypt-Only), 17 DSA, 18 Reserved EC, 19 Reserved ECDSA, 20 Reserved (former Elgamal Encrypt or Sign), 21 Reserved Diffie-Hellman (X9.42), 100-110 Private/Experimental.
- **MUST** implement DSA for signatures and Elgamal for encryption. **SHOULD** implement RSA keys.

### 9.2 Symmetric-Key Algorithms
- 0 Plaintext, 1 IDEA, 2 TripleDES, 3 CAST5, 4 Blowfish, 5-6 Reserved, 7 AES-128, 8 AES-192, 9 AES-256, 10 Twofish-256, 100-110 Private/Experimental.
- **MUST** implement TripleDES. **SHOULD** implement AES-128 and CAST5.

### 9.3 Compression Algorithms
- 0 Uncompressed, 1 ZIP, 2 ZLIB, 3 BZip2, 100-110 Private/Experimental.
- **MUST** implement uncompressed. **SHOULD** implement ZIP.

### 9.4 Hash Algorithms
- 1 MD5 (deprecated), 2 SHA-1, 3 RIPE-MD/160, 4-7 Reserved, 8 SHA256, 9 SHA384, 10 SHA512, 11 SHA224, 100-110 Private/Experimental.
- **MUST** implement SHA-1.

## 10. IANA Considerations
- S2K specifier types: IETF CONSENSUS.
- New packets: IETF CONSENSUS.
- User Attribute types: IETF CONSENSUS.
- Image Attribute subpacket types: IETF CONSENSUS.
- Signature subpacket types: IETF CONSENSUS.
- Signature Notation Data types: EXPERT REVIEW.
- Key Server Preference extensions: IETF CONSENSUS.
- Key Flags extensions: IETF CONSENSUS.
- Reason for Revocation extensions: IETF CONSENSUS.
- Implementation Features: IETF CONSENSUS.
- New packet versions: IETF CONSENSUS.
- New algorithms: IETF CONSENSUS for each category.

## 11. Packet Composition
### 11.1 Transferable Public Keys
- Sequence: Public-Key packet, zero or more revocation signatures, one or more User ID packets (each followed by zero or more certifications), zero or more User Attribute packets (each followed by certifications), zero or more Subkey packets (each followed by binding signature, + optional revocation). V3 keys **MUST NOT** have subkeys.

### 11.2 Transferable Secret Keys
- Same as public key but with secret-key and secret-subkey packets. **SHOULD** include self-signatures.

### 11.3 OpenPGP Messages
- Grammar: Encrypted Message | Signed Message | Compressed Message | Literal Message.
- Encrypted: ESK Sequence (PKESK and/or SKESK) + Encrypted Data. Signed: Signature Packet + OpenPGP Message, or One-Pass Signature Packet + OpenPGP Message + Corresponding Signature.

### 11.4 Detached Signatures
- Signature packet stored separately from signed data.

## 12. Enhanced Key Formats
### 12.1 Key Structures
- V3: RSA Public Key, [Revocation], User IDs with signatures. Deprecated, **MUST NOT** generate new V3.
- V4: Primary-Key, [Revocation], [Direct Key Signatures], User IDs/Attributes with signatures, Subkeys with binding signatures (if signing subkey, must have embedded 0x19 signature). Primary key **MUST** be capable of certification.

### 12.2 Key IDs and Fingerprints
- V3 Key ID: low 64 bits of RSA modulus. Fingerprint: MD5 of MPIs (deprecated).
- V4 fingerprint: SHA-1 of 0x99 + 2-octet length + Public-Key packet (version through algorithm-specific fields). Key ID: low 64 bits of fingerprint.
- Subkey fingerprint computed similarly (including 0x99).

## 13. Notes on Algorithms
### 13.1 PKCS#1 Encoding in OpenPGP
- EME-PKCS1-v1_5-ENCODE: message padded with 0x00, 0x02, random non-zero octets (at least 8), 0x00, message.
- EME-PKCS1-v1_5-DECODE: check structure, output message.
- EMSA-PKCS1-v1_5: hash prefix (OID) padded with 0x00, 0x01, 0xFF octets, 0x00, prefix.

### 13.2 Symmetric Algorithm Preferences
- Ordered list; TripleDES implicitly at end if not listed. **MUST NOT** use algorithm not in recipient's list. Intersection taken for multiple recipients. **SHOULD** decrypt even if algorithm not preferred, but warn.

### 13.3 Other Algorithm Preferences
- Compression: if not present, assume [ZIP, Uncompressed]. **MUST NOT** use algorithm not in list. Minimal implementation can never compress.
- Hash: SHA-1 implicitly at end. Preference enables negotiation.

### 13.4 Plaintext
- Algorithm 0 only for unencrypted secret keys. **MUST NOT** use in Sym. Encrypted Data packets.

### 13.5 RSA
- RSA Sign-Only and Encrypt-Only deprecated. **SHOULD NOT** create such keys. **SHOULD NOT** implement keys < 1024 bits.

### 13.6 DSA
- **SHOULD NOT** implement < 1024 bits. **MUST NOT** implement q < 160 bits. Key and q sizes must be multiples of 64 and 8 bits respectively. Recommended pairs per DSS.

### 13.7 Elgamal
- **SHOULD NOT** implement keys < 1024 bits.

### 13.8 Reserved Algorithm Numbers
- Elliptic Curve (18), ECDSA (19), X9.42 (21) reserved; parameters not defined. Elgamal signatures (ID 20) **MUST NOT** be generated.

### 13.9 OpenPGP CFB Mode
- Detailed step-by-step: IV all zeros, prefix of BS+2 random octets (last two repeat), then plaintext; CFB shift size = block size.

### 13.10 Private/Experimental Parameters
- Ranges 100-110 for S2K, signature subpackets, user attributes, image formats, algorithms; packet tags 60-63. PRIVATE USE.

### 13.11 Extension of MDC System
- Must avoid downgrade attacks. Options: new packets, new packet 18 version reflecting hash. **MUST** be done through IETF CONSENSUS.

### 13.12 Meta-Considerations for Expansion
- Non-backwards-compatible extensions should be declared in Features subpacket. If not, proposal **SHOULD** be rejected.

## 14. Security Considerations
- Check current literature for algorithm vulnerabilities.
- Private keys must be secured.
- Use appropriate entropy (RFC 4086).
- MD5 deprecated for new signatures; **MUST NOT** generate new MD5 signatures; **MAY** accept old.
- SHA-224/384 rarely needed outside DSS.
- Dual-use keys for privacy and integrity controversial.
- DSA sensitive to hash quality; only accept strong hashes.
- Careful about weakest link; NIST SP 800-57 equivalence table provided.
- Potential hash algorithm collision attacks; if hash weakness found, revise allowed algorithms.
- Signer should not use weak algorithm just because recipient requests.
- Encryption algorithms vary in analysis depth.
- Jallad-Katz-Schneier attack: treat decompression errors and MDC failures as security problems. **MUST** treat MDC failure as security problem. **SHOULD** treat decompression error similarly.
- PKCS#1 padding oracle attacks: report single error for decryption/padding failures.
- Some technologies may be subject to government control.
- Mister-Zuccherato quick check attack: use with care; not needed with PKESK; if used, avoid timing oracle.

## 15. Implementation Nits
- IDEA patented, required for PGP 2.x interoperability.
- Older versions use "BEGIN PGP SECRET KEY BLOCK" instead of "PRIVATE".
- V2 keys identical to V3; **MUST NOT** generate, may accept.
- PGP 2.6.x rejects key packets with version > 3.
- Same key material can have different fingerprints if creation time differs.
- zlib windowBits = -13 for PGP 2.x.
- Back signatures (0x19) not always present; handle as appropriate.
- No strict limit on public key sizes; practical upper bound ~4096 bits currently.
- ASCII armor optional but recommended for compatibility, especially with OpenPGP/MIME.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations **SHOULD** accept V3 signatures. | SHOULD | Section 5.2 |
| R2 | Implementations **SHOULD** generate V4 signatures. | SHOULD | Section 5.2 |
| R3 | Implementation **MUST** create keys with version 4 format. | MUST | Section 5.5.2 |
| R4 | Implementation **MUST NOT** generate V3 keys. | MUST NOT | Section 5.5.2 |
| R5 | Implementation **MUST** implement DSA for signatures and Elgamal for encryption. | MUST | Section 9.1 |
| R6 | Implementation **MUST** implement TripleDES. | MUST | Section 9.2 |
| R7 | Implementation **MUST** implement SHA-1. | MUST | Section 9.4 |
| R8 | Implementation **MUST** implement uncompressed data. | MUST | Section 9.3 |
| R9 | Implementation **SHOULD** implement ZIP compression. | SHOULD | Section 9.3 |
| R10 | Implementation **MUST** treat MDC failure as a security problem. | MUST | Section 5.13 |
| R11 | Implementation **MUST NOT** generate new MD5 signatures. | MUST NOT | Section 14 |
| R12 | Implementation **MUST** use salt in Symmetric-Key ESK S2K specifier. | MUST | Section 5.3 |
| R13 | Implementation **MUST NOT** generate Elgamal signatures. | MUST NOT | Section 13.8 |
| R14 | Implementation **SHOULD** prefer generating Sym. Encrypted Integrity Protected Data packets over Sym. Encrypted Data packets. | SHOULD | Section 5.13 |

## Informative Annexes (Condensed)
- **Non-normative explanation of MDC (Section 5.13)**: MDC provides integrity without digital signature, preserving deniability. It is not a MAC but a checksum; relies on one-way hash, not collision resistance. Hard-defines SHA-1 to prevent downgrade attacks. Should be upgraded via IETF CONSENSUS.
- **Notes on Self-Signatures (Section 5.2.3.3)**: Self-signatures bind key to User ID or subkey; revoking them retires the associated identity. Implementations should interpret preferences per User ID, and allow rewriting.
- **Algorithm Preferences (Sections 13.2–13.3)**: Preferences are ordered lists; TripleDES and SHA-1 are implicitly at end. Intersection used for multiple recipients. Implementations should decrypt even if algorithm not preferred but warn.
- **PKCS#1 Encoding (Section 13.1)**: Describes EME and EMSA functions adapted from PKCS#1 v2.1; used for RSA encryption and signing.
- **OpenPGP CFB Mode (Section 13.9)**: Detailed procedure with random prefix and resynchronization; used for symmetric encryption.
- **Security Considerations (Section 14)**: Summarizes known attacks and mitigations, including Jallad-Katz-Schneier attack, PKCS#1 padding oracle, Mister-Zuccherato quick check attack. Emphasizes treating decompression errors and MDC failures as security issues.
- **Implementation Nits (Section 15)**: Collection of backward-compatibility tips, including IDEA requirement, V2 keys, zlib windowBits, back signature history, key size limits, and ASCII armor optionality.