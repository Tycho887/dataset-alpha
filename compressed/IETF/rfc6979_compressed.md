# RFC 6979: Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA)
**Source**: Independent Submission (T. Pornin) | **Version**: RFC 6979 | **Date**: August 2013 | **Type**: Informational
**Original**: https://www.rfc-editor.org/info/rfc6979

## Scope (Summary)
Defines a deterministic digital signature generation procedure for DSA and ECDSA. Signatures remain fully compatible with standard verifiers. The process uses a deterministic method to generate the per-signature random value *k* from the private key and the message hash, eliminating the need for a high-quality random source during signing.

## Normative References
- [FIPS-186-4] NIST, "Digital Signature Standard (DSS)", FIPS PUB 186-4, July 2013.
- [RFC2104] Krawczyk, H., Bellare, M., and R. Canetti, "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, February 1997.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [SEC1] Certicom Research, "SEC 1: Elliptic Curve Cryptography (Version 2.0)", May 2009.
- [SP800-90A] NIST, "Recommendation for Random Number Generation Using Deterministic Random Bit Generators (Revised)", NIST SP 800-90A, January 2012.
- [X9.62] ANSI, "Public Key Cryptography for the Financial Services Industry: The Elliptic Curve Digital Signature Algorithm (ECDSA)", ANSI X9.62-2005, November 2005.

## Definitions and Abbreviations
- **qlen**: Binary length of the subgroup order *q*.
- **rlen**: *qlen* rounded up to the next multiple of 8.
- **blen**: Length (in bits) of an input bit sequence.
- **bits2int(b)**: Transform input bit sequence of length *blen* into an integer less than 2^qlen by truncating or left-padding to *qlen* bits and converting big-endian.
- **int2octets(x)**: Convert integer *x* (less than *q*) into a sequence of *rlen* bits (big-endian, resulting in an integral number of octets).
- **bits2octets(b)**: Convert input bit sequence to integer via bits2int, reduce modulo *q*, then apply int2octets.
- **HMAC_K(V)**: HMAC with key *K* over data *V*, returning *hlen* bits.

## 1. Introduction
DSA and ECDSA require a fresh random value *k* per signature. Deterministic (EC)DSA generates *k* deterministically from the private key and message hash, preserving security properties. Key pair generation still requires a source of randomness.

### 1.1. Requirements Language
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 2. DSA and ECDSA Notations
- **Key parameters**: DSA uses (*p*, *q*, *g*); ECDSA uses curve *E*, *q*, and base point *G*.
- **Key pairs**: Private key *x* in [1, *q*-1]; public key *y* = *g*^x mod *p* (DSA) or *U* = *xG* (ECDSA).
- **Integer conversions**: bits2int, int2octets, bits2octets as defined above.
- **Signature generation (standard)**: Compute *h* = bits2int(H(m)) mod *q*; generate random *k* in [1, *q*-1]; compute *r* (depends on scheme); compute *s* = (*h* + *x*·*r*)/*k* mod *q*; output (*r*, *s*). If *r* = 0, select new *k*.

## 3. Deterministic DSA and ECDSA
Deterministic (EC)DSA uses the standard process except that *k* is generated deterministically as described below.

### 3.1. Building Blocks
#### 3.1.1. HMAC
HMAC uses the same hash function *H* as used to process the input message.

### 3.2. Generation of k
The following process SHALL be applied:

a. **Hash message**: *h1* = *H(m)* (sequence of *hlen* bits).

b. **Initialize V**: Set *V* = 0x01 0x01 ... 0x01 (length = 8·ceil(*hlen*/8) bits, i.e., full octets of value 1).

c. **Initialize K**: Set *K* = 0x00 0x00 ... 0x00 (same length as *V*).

d. **Update K (first)**: *K* = HMAC_K(*V* || 0x00 || int2octets(*x*) || bits2octets(*h1*)).  
   The concatenation order is: current *V*, a zero byte, the encoding of private key *x*, and the hashed message processed by bits2octets.

e. **Update V (first)**: *V* = HMAC_K(*V*).

f. **Update K (second)**: *K* = HMAC_K(*V* || 0x01 || int2octets(*x*) || bits2octets(*h1*)).  
   Note the internal byte is 0x01.

g. **Update V (second)**: *V* = HMAC_K(*V*).

h. **Generate k**: Loop until a suitable *k* is found:
   1. Set *T* to empty. *tlen* = 0.
   2. While *tlen* < *qlen*:
      - *V* = HMAC_K(*V*)
      - *T* = *T* || *V*
   3. Compute *k* = bits2int(*T*).
   4. If *k* is in [1, *q*-1] **and** is suitable for (EC)DSA (i.e., *r* ≠ 0), then **k is final**.
   5. Else: *K* = HMAC_K(*V* || 0x00); *V* = HMAC_K(*V*); go to step h.1.

**Important**: *k* is compared to *q*, not reduced modulo *q*. This avoids biases.

### 3.3. Alternate Description
The process is equivalent to instantiating HMAC_DRBG (per SP800-90A) with:
- entropy_input = int2octets(*x*)
- nonce = bits2octets(H(*m*))
- personalization_string = empty
- prediction_resistance_flag = false
Then requesting *qlen* bits and converting to integer via bits2int, repeating until a valid *k* is obtained.

### 3.4. Usage Notes
- If *r* = 0, the value *k* is unsuitable and generation SHALL loop (though this is practically impossible).
- The code path for *r* = 0 need not be optimized.

### 3.5. Rationale
Using the private key *x* and hashed message as seed for HMAC_DRBG provides sufficient entropy (≥ *n*+64 bits) when *qlen* ≥ 160. bits2octets(H(m)) is used instead of H(m) to facilitate integration with systems that truncate the hash before signing.

### 3.6. Variants
Several optional modifications are possible but are **NOT** deterministic (EC)DSA as defined in this document. They include:
- Using H(m) directly instead of bits2octets(H(m)).
- Adding additional data *k'* (e.g., a counter) to the HMAC input to produce non-deterministic signatures.
- Using additional secret data instead of *x* as input to HMAC (SHALL have at least *n* bits of entropy).
- Deriving *x* and a separate value *x'* from a master secret.
- Using different hash functions for message hashing and HMAC.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | The generation of *k* SHALL follow the process in Section 3.2. | SHALL | 3.2 |
| R2 | The private key *x* SHALL be encoded as int2octets(*x*) for use in HMAC. | SHALL | 3.2 step d |
| R3 | The hashed message *h1* SHALL be processed by bits2octets before inclusion in HMAC. | SHALL | 3.2 step d |
| R4 | If the generated *k* is not in [1, *q*-1] or not suitable (r=0), the process SHALL loop as described. | SHALL | 3.2 step h, 3.4 |
| R5 | The same hash function *H* SHALL be used for both message hashing and HMAC in the defined deterministic process. | SHALL (implied by procedure) | 3.1.1, 3.6 |
| R6 | Implementations SHOULD use defensive measures to avoid leaking the private key through side channels. | SHOULD | 4 |
| R7 | Key pair generation MUST still use a cryptographically secure random source. | MUST | 1, 4 |
| R8 | The private key *x* SHALL NOT be 0; it SHALL be in [1, *q*-1]. | SHALL | 2.2 (standard) |
| R9 | The value *k* SHALL NOT be 0; it SHALL be in [1, *q*-1]. | SHALL | 2.4 step 2 (standard) |
| R10 | The value *r* SHALL NOT be 0; if 0, a new *k* SHALL be generated. | SHALL | 2.4 step 3, 3.4 |
| R11 | The additional secret data in the variant of Section 3.6 SHALL have at least *n* bits of entropy. | SHALL (for that variant) | 3.6 |

## Security Considerations (Condensed)
Deterministic (EC)DSA removes the need for randomness during signing but does not affect private key generation requirements. It enhances testability and avoids hard-to-detect failure modes. It is appropriate for protocols that tolerate deterministic signatures (e.g., TLS, SSH, CMS, X.509). The construction's security relies on HMAC_DRBG behaving as a pseudorandom function. The "double use" of the private key *x* is assumed reasonable given lack of common structure with discrete logarithms. Side-channel leakage remains a concern; implementations SHOULD use countermeasures.

## Informative Annexes (Condensed)
- **Annex A.1 (Detailed Example)**: Shows step-by-step generation of *k* for ECDSA on K-163 with SHA-256, message "sample". All intermediate values (V, K, T) and final signature (r, s) are provided.
- **Annex A.2 (Test Vectors)**: Contains 17 subsections with test vectors for various key sizes and hash functions: DSA (1024, 2048 bits) and ECDSA on NIST prime and binary curves (P-192, P-224, P-256, P-384, P-521, K-163, K-233, K-283, K-409, K-571, B-163, B-233, B-283, B-409, B-571). Each subsection lists the key pair and 10 signatures (two messages "sample" and "test" × five SHA functions: SHA-1, SHA-224, SHA-256, SHA-384, SHA-512). The *k* values are also given.
- **Annex A.3 (Sample Code)**: Provides a Java implementation of deterministic DSA (class `DeterministicDSA`) illustrating the `computek()` method. The code includes license (Simplified BSD) and is intended for illustration only, not optimized against side-channel attacks.