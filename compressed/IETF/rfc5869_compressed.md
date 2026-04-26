# RFC 5869: HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
**Source**: IETF | **Version**: Informational | **Date**: May 2010 | **Type**: Informational
**Original**: https://www.rfc-editor.org/rfc/rfc5869

## Scope (Summary)
This document specifies a simple HMAC-based key derivation function (HKDF) that follows the extract-then-expand paradigm. It is intended as a building block for protocols and applications, and is conservative in its use of cryptographic hash functions.

## Normative References
- [HMAC] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [SHS] National Institute of Standards and Technology, "Secure Hash Standard", FIPS PUB 180-3, October 2008.

## Definitions and Abbreviations
- **HKDF**: HMAC-based Extract-and-Expand Key Derivation Function.
- **HMAC-Hash**: HMAC function instantiated with hash function 'Hash'.
- **IKM**: Input Keying Material.
- **PRK**: Pseudorandom Key (output of extract step).
- **OKM**: Output Keying Material.
- **HashLen**: Length of the hash function output in octets.
- **L**: Length of output keying material in octets.
- **salt**: Optional non-secret random value.
- **info**: Optional context and application-specific information.

## 1. Introduction (Condensed)
Key derivation functions (KDFs) transform initial keying material into cryptographically strong secret keys. HKDF uses a two-stage approach: first, it extracts a fixed-length pseudorandom key (PRK) from the input keying material (IKM); second, it expands PRK into the desired number of output keys. The extract stage can be omitted if IKM is already a strong pseudorandom key. This specification documents HKDF to promote uniform use and to discourage proliferation of multiple KDF mechanisms; it does not change existing protocols.

## 2. HMAC-based Key Derivation Function (HKDF)
### 2.1 Notation
- **HMAC-Hash**: HMAC function [HMAC] with hash function 'Hash'. HMAC always has two arguments: key and input/message. Concatenation of elements is denoted by "|".
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [KEYWORDS].

### 2.2 Step 1: Extract
**HKDF-Extract(salt, IKM) -> PRK**
- **Options**: Hash (hash function); HashLen = length of hash output in octets.
- **Inputs**: salt (optional; if not provided, set to string of HashLen zeros), IKM.
- **Output**: PRK (pseudorandom key of HashLen octets).
- **Calculation**: PRK = HMAC-Hash(salt, IKM)

### 2.3 Step 2: Expand
**HKDF-Expand(PRK, info, L) -> OKM**
- **Options**: Hash; HashLen.
- **Inputs**: PRK (pseudorandom key of at least HashLen octets), info (optional; can be zero-length string), L (length of output keying material in octets, <= 255*HashLen).
- **Output**: OKM (of L octets).
- **Calculation**:
  ```
  N = ceil(L/HashLen)
  T = T(1) | T(2) | T(3) | ... | T(N)
  OKM = first L octets of T
  where:
  T(0) = empty string (zero length)
  T(1) = HMAC-Hash(PRK, T(0) | info | 0x01)
  T(2) = HMAC-Hash(PRK, T(1) | info | 0x02)
  T(3) = HMAC-Hash(PRK, T(2) | info | 0x03)
  ...
  (the constant concatenated to the end of each T(n) is a single octet)
  ```

## 3. Notes to HKDF Users (Condensed)
### 3.1 To Salt or not to Salt
- The use of salt significantly strengthens HKDF, ensuring independence, supporting source-independent extraction, and strengthening analytical results. Salt is non-secret and can be reused. Ideally, it is a random (or pseudorandom) string of length HashLen, but lower quality still contributes to security. Applications are encouraged to provide salt if obtainable. Secret salt provides even stronger guarantees (e.g., IKEv1 modes).

### 3.2 The 'info' Input to HKDF
- 'info' is optional but often important to bind derived keying material to context (e.g., protocol numbers, algorithm identifiers). It prevents derivation of the same keying material for different contexts when IKM is the same. 'info' should be independent of IKM.

### 3.3 To Skip or not to Skip
- If IKM is already a cryptographically strong pseudorandom key (e.g., TLS RSA premaster secret), the extract part can be skipped and IKM used directly as PRK in the expand step. However, if IKM is a Diffie-Hellman value (e.g., g^xy), the extract part SHOULD NOT be omitted. Skipping the expand step when L <= HashLen is NOT RECOMMENDED because it omits the use of 'info'.

### 3.4 The Role of Independence
- Analysis assumes IKM comes from a probability distribution. The goal is to ensure that applying HKDF to two different IKM values yields essentially independent OKM outputs. Salt values must be independent of IKM and must not be chosen or manipulated by an attacker. For example, when salt is derived from authenticated nonces, those nonces must be verified as coming from legitimate parties.

## 4. Applications of HKDF (Condensed)
- Suitable for building pseudorandom generators from imperfect randomness, deriving keys from Diffie-Hellman values, hybrid encryption, key wrapping, and similar tasks. Not recommended for low-entropy sources like passwords; for password-based KDFs, consider [PKCS5].

## 5. Security Considerations
- Refer to [HKDF-paper] for detailed security analysis, design rationale, and guidelines. The security of HKDF depends on the strength of the underlying hash function.

## 6. Acknowledgments
- Thanks to CFRG list members and Dan Harkins for test vectors.

## 7. References
- Normative: [HMAC], [KEYWORDS], [SHS]
- Informative: [1363a], [800-108], [800-56A], [EAP-AKA], [HKDF-paper], [IKEv2], [PANA], [PKCS5]

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | PRK = HMAC-Hash(salt, IKM) | shall | Section 2.2 |
| R2 | If salt not provided, set to string of HashLen zeros | shall | Section 2.2 |
| R3 | OKM = first L octets of T, computed as per Section 2.3 expansion | shall | Section 2.3 |
| R4 | L <= 255 * HashLen | shall | Section 2.3 |
| R5 | PRK must be at least HashLen octets | shall (precondition) | Section 2.3 |
| R6 | Extract SHOULD NOT be skipped for Diffie-Hellman IKM | should NOT | Section 3.3 |
| R7 | Skipping expand when L <= HashLen is NOT RECOMMENDED | NOT RECOMMENDED | Section 3.3 |
| R8 | Applications SHOULD provide salt if obtainable | should | Section 3.1 |

## Informative Annexes (Condensed)
- **Appendix A: Test Vectors**: Provides test vectors for SHA‑256 and SHA‑1, including basic cases, longer inputs/outputs, zero-length salt/info, and the case where salt is not provided (defaults to zeros). Seven test cases with expected PRK and OKM hex values are given for verification of implementation correctness.