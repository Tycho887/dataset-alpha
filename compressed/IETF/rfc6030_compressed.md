# RFC 6030: Portable Symmetric Key Container (PSKC)
**Source**: IETF | **Version**: 1.0 | **Date**: October 2010 | **Type**: Standards Track
**Original**: https://www.rfc-editor.org/rfc/rfc6030

## Scope (Summary)
This document defines an XML-based container for transporting symmetric keys and associated metadata (e.g., OTP shared secrets, cryptographic keys) between crypto modules. It supports encryption, integrity, authentication, and bulk provisioning, and establishes IANA registries for algorithm profiles, versions, and key usage.

## Normative References
- [FIPS197] NIST, "FIPS Pub 197: Advanced Encryption Standard (AES)", November 2001.
- [HOTP] RFC 4226: HOTP: An HMAC-Based One-Time Password Algorithm.
- [IANAPENREG] IANA, "Private Enterprise Numbers".
- [ISOIEC7812] ISO/IEC 7812-1:2006.
- [OATHMAN] OATH, "List of OATH Manufacturer Prefixes".
- [PKCS5] RSA Labs, "PKCS #5: Password-Based Cryptography Standard", Version 2.0.
- [RFC2119] Key words for requirement levels.
- [RFC3023] XML Media Types.
- [RFC3688] The IETF XML Registry.
- [RFC4288] Media Type Specifications.
- [RFC4514] LDAP: String Representation of Distinguished Names.
- [RFC4648] Base16, Base32, Base64 Data Encodings.
- [RFC5646] Tags for Identifying Languages.
- [RFC5649] AES Key Wrap with Padding.
- [SP800-67] NIST SP 800-67 Ver 1.1: Triple Data Encryption Algorithm.
- [W3C.REC-xmlschema-2] XML Schema Part 2: Datatypes.
- [XMLDSIG] XML-Signature Syntax and Processing.
- [XMLENC] XML Encryption Syntax and Processing.
- [XMLENC11] XML Encryption Syntax and Processing Version 1.1.

## Definitions and Abbreviations
- **PSKC**: Portable Symmetric Key Container.
- **OTP**: One-Time Password.
- **CR**: Challenge/Response.
- **HOTP**: HMAC-Based One-Time Password.
- **TDEA (Triple DES)**: Triple Data Encryption Algorithm.
- **MAC**: Message Authentication Code.
- **PBKDF2**: Password-Based Key Derivation Function 2.
- **IV**: Initialization Vector.
- **CBC**: Cipher Block Chaining.
- **HMAC**: Hashed-based Message Authentication Code.
- **PBE**: Password-Based Encryption.
- **Key words**: "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL" as per [RFC2119].

## 1. Introduction
PSKC provides a standardized XML-based container for provisioning symmetric keys, supporting OTP, CR, and other symmetric-key-based systems. It defines an IANA registry for algorithm profiles.

### 1.1 Key Words
Interpretation per [RFC2119].

### 1.2 Version Support
- The `Version` attribute shall be used. Only version "1.0" is currently specified.
- Version numbering: `<major>.<minor>`. Major/minor are separate integers; leading zeros MUST be ignored and MUST NOT be sent.
- The major version increments only if message format changes prevent interoperability; minor version indicates new capabilities and MUST be ignored by entities with smaller minor version.

### 1.3 Namespace Identifiers
- **PSKC**: `urn:ietf:params:xml:ns:keyprov:pskc` (prefix `pskc`)
- **XML Signature**: `http://www.w3.org/2000/09/xmldsig#` (prefix `ds`)
- **XML Encryption**: `http://www.w3.org/2001/04/xmlenc#` (prefix `xenc`)
- **XML Encryption 1.1**: `http://www.w3.org/2009/xmlenc11#` (prefix `xenc11`)
- **PKCS#5**: `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5v2-0#` (prefix `pkcs5`)

## 2. Terminology
- **Mandatory** elements/attributes are highlighted; optional unless stated otherwise.

## 3. Portable Key Container Entities Overview
Key conceptual entities:
1. **KeyContainer**: Contains at least one KeyPackage.
2. **KeyPackage**: Package of at most one key and its DeviceInfo/CryptoModuleInfo.
3. **DeviceInfo**: Uniquely identifies the device.
4. **CryptoModuleInfo**: Identifies the crypto module.
5. **Key**: The symmetric key and metadata.
6. **Data**: List of metadata (Secret, Counter, Time, etc.) either encrypted or plaintext.

See Figure 1 in original.

## 4. `<KeyContainer>` Element: Basics
- **`Version`** attribute: REQUIRED, identifies PSKC schema version. Initial "1.0".
- **`Id`** attribute: optional unique identifier for the container.

### 4.1 `<Key>`: Embedding Keying Material
Required attributes:
- **`Id`**: Unique identifier for the key in context of provisioning exchanges. MUST be the same value across containers referencing the same key (e.g., for updating metadata). String of alphanumeric characters.
- **`Algorithm`**: Contains a unique identifier for the PSKC algorithm profile (e.g., `urn:ietf:params:xml:ns:keyprov:pskc:hotp`).

Optional child elements:
- `<Issuer>`: Name of issuing party.
- `<FriendlyName>`: Human-readable name; SHOULD have `xml:lang` attribute; if absent, assume 'en'.
- `<AlgorithmParameters>`: Parameters for OTP/CR algorithms (see 4.3.4).
- `<Data>`: Contains key-related data. Child elements:
  - `<Secret>`: Key value in binary (see 4.2).
  - `<Counter>`: Event counter for OTP.
  - `<Time>`: Time value for time-based OTP.
  - `<TimeInterval>`: Time interval in seconds.
  - `<TimeDrift>`: Device clock drift (integer).
- All data elements MUST support either `<PlainValue>` (plaintext) or `<EncryptedValue>` (encrypted). `<ValueMAC>` may be present for integrity.

### 4.2 Key Value Encoding
- Two parties must decode `xs:base64Binary` identically to interoperate.
- **AES Key Value Encoding**: First octet becomes index 0 in AES key expansion; subsequent octets in increasing order. Example given.
- **Triple-DES Key Value Encoding**: Key bundle (Key1, Key2, Key3). First octet is bits 1-8 of Key1 (MSB), etc. Example given.
- Unless otherwise specified, AES encoding MUST be used.

### 4.3 Transmission of Supplementary Information

#### 4.3.1 `<DeviceInfo>` Element
Uniquely identifies the device. Child elements (optional except as needed for uniqueness):
- `<Manufacturer>`: value MUST be taken from [OATHMAN] (prepend "oath.") or [IANAPENREG] (prepend "iana.").
- `<SerialNo>`: serial number.
- `<Model>`: model identifier.
- `<IssueNo>`: issue number.
- `<DeviceBinding>`: ensures key provisioned to approved device (e.g., IMEI).
- `<StartDate>` and `<ExpiryDate>`: dateTime in canonical representation; devices SHOULD enforce usage between dates (but server enforcement may be only option).
- Combinations of child elements MUST uniquely identify the device; e.g., SerialNo alone insufficient.

#### 4.3.2 `<CryptoModuleInfo>` Element
- `<Id>`: MUST be included, unique identifier for crypto module.

#### 4.3.3 `<UserId>` Element
- Distinguished name per [RFC4514]. Informational only. May appear as child of `<Key>` or `<DeviceInfo>`.

#### 4.3.4 `<AlgorithmParameters>` Element
Child elements:
- `<Suite>`: Additional algorithm-specific characteristics (e.g., hash strength).
- `<ChallengeFormat>`: Attributes:
  - `Encoding`: REQUIRED, one of DECIMAL, HEXADECIMAL, ALPHANUMERIC, BASE64, BINARY.
  - `CheckDigit`: For DECIMAL, whether to check Luhn digit.
  - `Min` and `Max`: REQUIRED, minimum/maximum size (digits/bytes depending on encoding).
- `<ResponseFormat>`: Attributes:
  - `Encoding`: REQUIRED, as above.
  - `CheckDigit`: Append Luhn digit (DECIMAL only).
  - `Length`: REQUIRED, length in digits/bytes depending on encoding.

### 4.4 Transmission of Key Derivation Values
- `<KeyProfileId>`: Reference to out-of-band agreed profile.
- `<KeyReference>`: Reference to external key (e.g., master key label). The `<Secret>` element may be absent; the key is derived using serial number, profile, and external key.
- Example in Figure 4.

## 5. Key Policy
The `<Policy>` element (child of `<Key>`) restricts key usage. If any child element/value is not understood, the recipient MUST assume key usage is not permitted.

- `<StartDate>` and `<ExpiryDate>`: Validity period; key MUST only be used between inclusive dates. Canonical dateTime.
- `<NumberOfTransactions>`: Maximum uses of the key.
- `<KeyUsage>`: Enforced constraints. Registered values:
  - `OTP`, `CR`, `Encrypt`, `Integrity`, `Verify`, `Unlock`, `Decrypt`, `KeyWrap`, `Unwrap`, `Derive`, `Generate`.
  - May be repeated for multiple usages. Absent = unrestricted.
- `<PINPolicy>`: Attributes:
  - `PINKeyId`: Reference to `<Key>` element containing PIN value.
  - `PINUsageMode`: REQUIRED, one of `Local` (PIN checked locally), `Prepend`, `Append`, `Algorithmic`.
  - `MaxFailedAttempts`: Maximum PIN failures before key unusable.
  - `MinLength`, `MaxLength`: PIN length constraints.
  - `PINEncoding`: REQUIRED, one of DECIMAL, HEXADECIMAL, ALPHANUMERIC, BASE64, BINARY.
  - If `PINUsageMode` is `Local`, device MUST enforce restrictions; otherwise server enforces.

### 5.1 PIN Algorithm Definition
`boolean = comparePIN(K,P)` – straight octet comparison. Returns TRUE if lengths equal and all octets match.

## 6. Key Protection Methods
The `<EncryptionKey>` element enables encryption. Encryption algorithm MUST be same for all encrypted elements. When using CBC mode, a random IV MUST be generated and prepended per [XMLENC].

### 6.1 Encryption Based on Pre-Shared Keys
- Implementation MUST set the key name in `<ds:KeyName>` inside `<EncryptionKey>`.
- If CBC mode requires explicit IV, it MUST be prepended to encrypted value.
- RECOMMENDED: support AES-128-CBC and KW-AES128. If key length not multiple of 8, use key-wrap with padding [RFC5649].
- Table of optional algorithms provided.

#### 6.1.1 MAC Method
- If encryption algorithm lacks integrity (e.g., AES-128-CBC), a keyed-MAC MUST be placed in `<ValueMAC>`.
- MAC algorithm set in `<MACMethod>` of `<KeyContainer>`. MAC key SHOULD be randomly generated by sender, encrypted with same encryption key, and placed in `<MACKey>` (with `<EncryptionMethod>` and `<CipherData>`). Alternatively, `<MACKeyReference>` MAY indicate pre-shared or derived key.
- RECOMMENDED: HMAC-SHA1. Optional algorithms listed.

### 6.2 Encryption Based on Passphrase-Based Keys
- Use `<DerivedKey>` element from XML Encryption 1.1 inside `<EncryptionKey>`.
- When PBKDF2 used, `Algorithm` attribute of `<KeyDerivationMethod>` MUST be `http://www.rsasecurity.com/rsalabs/pkcs/schemas/pkcs-5#pbkdf2`.
- Must include `<PBKDF2-params>` with salt, iteration count, etc.
- Encryption algorithm in `Algorithm` attribute of `<EncryptionMethod>` within encrypted data.
- Example in Figure 7.

### 6.3 Encryption Based on Asymmetric Keys
- Use `<X509Data>` inside `<EncryptionKey>` to provide certificate.
- Encryption algorithm in `Algorithm` attribute of `<EncryptionMethod>` (e.g., `http://www.w3.org/2001/04/xmlenc#rsa_1_5`).
- RECOMMENDED: RSA-1.5. Optional: RSA-OAEP-MGF1P.
- Example in Figure 8.

### 6.4 Padding of Encrypted Values
- For algorithms without embedded padding (e.g., AES-CBC), if value length not multiple of block length, RECOMMENDED to pad using PKCS#5 padding [PKCS5] before encryption.

## 7. Digital Signature
- Digital Signature as child element of `<KeyContainer>`, per [XMLDSIG].
- Example in Figure 9.

## 8. Bulk Provisioning
- Repeat `<KeyPackage>` within `<KeyContainer>`. `<EncryptionKey>` applies to all.
- To provision multiple keys to same device, repeat `<KeyPackage>` with identical `<DeviceInfo>`.
- Example in Figure 10.

## 9. Extensibility
- New PSKC Versions: allocate new version number; scheme per Section 1.2.
- New XML Elements: use `<Extensions>` or `<xs:any>` extension points.
- New XML Attributes: use `<xs:anyAttribute>`.
- New PSKC Algorithm Profiles: register per Section 12.4.
- Algorithm URIs: new URIs can be used for key protection.
- Policy: new `<KeyUsage>` values can be registered per Section 12.6.

## 10. PSKC Algorithm Profile

### 10.1 HOTP
- URI: `urn:ietf:params:xml:ns:keyprov:pskc:hotp`
- Definition: [HOTP]
- Profiling:
  - `<KeyPackage>` MUST be present.
  - `<ResponseFormat>` MUST be used to indicate OTP length and format.
  - `<Counter>` MUST be provided.
  - `<Secret>` if present MUST have at least 16 octets (128 bits).
  - `<ResponseFormat>`: `Format` attribute MUST be "DECIMAL", `Length` between 6 and 9 inclusive.
  - `<PINPolicy>` MAY be present but `PINUsageMode` cannot be "Algorithmic".

### 10.2 PIN
- URI: `urn:ietf:params:xml:ns:keyprov:pskc:pin`
- Definition: Section 5.1 of this RFC.
- Profiling:
  - `<Usage>` MAY be present, no required attributes.
  - `<Secret>` MUST be provided.
  - `<ResponseFormat>` MAY be used to indicate PIN value format.

## 11. XML Schema
- Full schema provided in RFC; reference only.

## 12. IANA Considerations
- Media type registration: `application/pskc+xml`.
- XML Schema registration: `urn:ietf:params:xml:schema:keyprov:pskc`.
- URN sub-namespace: `urn:ietf:params:xml:ns:keyprov:pskc`.
- PSKC Algorithm Profile Registry: Specification Required.
- PSKC Version Registry: Standards Action; initial "1.0".
- Key Usage Registry: Specification Required; Expert Review for new values. Initial values: OTP, CR, Encrypt, Integrity, Verify, Unlock, Decrypt, KeyWrap, Unwrap, Derive, Generate.

## 13. Security Considerations
- Confidentiality: Encrypt key payload or use lower-layer security (TLS/IPsec). When using PBE, use strong passphrase and PBESalt/iteration count.
- Integrity: RECOMMENDED to sign entire PSKC.
- Authenticity: Use digital signature; recipient SHOULD verify origin via public key/certificate.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Format MUST support transport of multiple symmetric key types (HOTP, OTP, CR, etc.) | MUST | App. B |
| R2 | Format MUST handle key itself and attributes (Id, Issuer, Algorithm, etc.) | MUST | App. B |
| R3 | Format SHOULD support both offline and online scenarios | SHOULD | App. B |
| R4 | Format SHOULD allow bulk representation of symmetric keys | SHOULD | App. B |
| R5 | Format SHOULD allow bulk representation of PINs related to keys | SHOULD | App. B |
| R6 | Format SHOULD be portable and computationally efficient | SHOULD | App. B |
| R7 | Format MUST provide data encryption and integrity | MUST | App. B |
| R8 | Format SHOULD NOT rely solely on transport layer security for core security | SHOULD | App. B |
| R9 | Format SHOULD be extensible | SHOULD | App. B |
| R10 | Format SHOULD allow distribution of key derivation data without key | SHOULD | App. B |
| R11 | Format SHOULD allow lifecycle management operations | SHOULD | App. B |
| R12 | Format MUST support pre-shared symmetric keys for confidentiality | MUST | App. B |
| R13 | Format MUST support PBE [PKCS5] for security | MUST | App. B |
| R14 | Format SHOULD support asymmetric encryption (e.g., RSA) | SHOULD | App. B |
| R15 | Recipient MUST assume key usage not permitted if policy elements not understood | MUST | §5 |
| R16 | If encryption algorithm lacks integrity, ValueMAC MUST be present | MUST | §6.1.1 |
| R17 | `Version` attribute MUST be included | MUST | §4 |
| R18 | `Id` attribute of `<Key>` MUST be the same when referencing same key across containers | MUST | §4.1 |
| R19 | Key usage constraints in `<KeyUsage>` MUST be enforced | MUST | §5 |
| R20 | If `PINUsageMode` is `Local`, device MUST enforce restrictions | MUST | §5 |

## Informative Annexes (Condensed)
- **Appendix A (Use Cases)**: Describes online (server-to-module, module-to-module, module-to-server, server-to-server bulk) and offline (bulk import/export) provisioning scenarios. These motivated the requirements.
- **Appendix B (Requirements)**: Lists 14 requirements (R1-R14) that drove the design. Key ones: support multiple key types, handle attributes, offline/online, bulk, PINs, portability, security, extensibility, key derivation, lifecycle, pre-shared keys, PBE, asymmetric encryption.