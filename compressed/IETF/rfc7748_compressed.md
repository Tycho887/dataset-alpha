# RFC 7748: Elliptic Curves for Security
**Source**: Internet Research Task Force (IRTF) – Crypto Forum Research Group | **Version**: RFC 7748 | **Date**: January 2016 | **Type**: Informational
**Original**: https://www.rfc-editor.org/info/rfc7748

## Scope (Summary)
This memo specifies two elliptic curves (Curve25519 and Curve448) over prime fields offering ~128-bit and ~224-bit security levels, respectively. The curves are Montgomery curves with birational Edwards equivalents, designed for constant-time, side-channel-resistant implementations. The document defines the X25519 and X448 functions for Diffie-Hellman key agreement and provides deterministic generation procedures.

## Normative References
- **[RFC2119]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.

## Definitions and Abbreviations
- **p**: Prime number defining the underlying field (2^255 – 19 or 2^448 – 2^224 – 1).
- **GF(p)**: Finite field with p elements.
- **A**: Element in GF(p), not equal to –2 or 2 (Montgomery curve parameter).
- **d**: Non-zero element in GF(p) (Edwards curve parameter; ≠1 for Edwards, ≠ –1 for twisted Edwards).
- **order**: Order of the prime-order subgroup.
- **P**: Generator point of prime order over GF(p).
- **U(P)**, **V(P)**: Coordinates of point P on Montgomery curve.
- **X(P)**, **Y(P)**: Coordinates of point P on (twisted) Edwards curve.
- **u, v**: Coordinates on Montgomery curve.
- **x, y**: Coordinates on (twisted) Edwards curve.
- **a24**: Constant (A – 2)/4: 121665 for Curve25519, 39081 for Curve448.
- **cswap**: Constant-time conditional swap function.

## 1. Introduction (Summary)
Progress in ECC efficiency and security has motivated new curves resistant to side-channel attacks. This memo specifies Curve25519 and Curve448, which support exception-free scalar multiplication and constant-time implementation. The curves are Montgomery curves (v² = u³ + A·u² + u) with birationally equivalent twisted Edwards or Edwards versions, and maps between them are provided.

## 2. Requirements Language
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 3. Notation
(See Definitions above)

## 4. Recommended Curves
### 4.1. Curve25519
- **p**: 2^255 – 19
- **A**: 486662
- **order**: 2^252 + 0x14def9dea2f79cd65812631a5cf5d3ed
- **cofactor**: 8
- **Base point (u, v)**: (9, 14781619447589544791020593568409986887264606134616475288964881837755586237401)
- **Birational Edwards equivalent (edwards25519)**: -x² + y² = 1 + d·x²·y², with d = 37095705934669439343138083508754565189542113879843219016388785533085940283555
- **Maps**: (u, v) = ((1+y)/(1-y), sqrt(-486664)·u/x); (x, y) = (sqrt(-486664)·u/v, (u-1)/(u+1))

### 4.2. Curve448
- **p**: 2^448 – 2^224 – 1
- **A**: 156326
- **order**: 2^446 – 0x8335dc163bb124b65129c96fde933d8d723a70aadc873d6d54a7bb0d
- **cofactor**: 4
- **Base point (u, v)**: (5, 355293926785568175264127502063783334808976399387714271831880898435169088786967410002932673765864550910142774147268105838985595290606362)
- **Birational Edwards equivalent**: x² + y² = 1 + d·x²·y², with d = 611975850744529176160423220965553317543219696871016626328968936415087860042636474891785599283666020414768678979989378147065462815545017
- **4-isogenous Edwards curve (edwards448)**: x² + y² = 1 – 39081·x²·y², with base point (224580040295924300187604334099896036246789641632564134246125461686950415467406032909029192869357953282578032075146446173674602635247710, 298819210078481492676017930443930673437544040154080242095928241372331506189835876003536878655418784733982303233503462500531545062832660)
- **4-isogeny maps** from Montgomery to edwards448: (u, v) = (y²/x², (2 – x² – y²)·y/x³); inverse: (x, y) = (4·v·(u² – 1)/(u⁴ – 2·u² + 4·v² + 1), -(u⁵ – 2·u³ – 4·u·v² + u)/(u⁵ – 2·u²·v² – 2·u³ – 2·v² + u))

## 5. The X25519 and X448 Functions
The X25519 and X448 functions perform scalar multiplication on the Montgomery form of the above curves. Inputs and outputs are u-coordinates encoded as 32-byte (X25519) or 56-byte (X448) little‑endian arrays.

### 5.1. Encoding and Decoding
- **DecodeUCoordinate**: For X25519, implementations MUST mask the most significant bit in the final byte (to preserve compatibility and resist fingerprinting).  
- **MUST accept non-canonical values** and process them as if reduced modulo p (2^255 – 19 to 2^255 – 1 for X25519; 2^448 – 2^224 – 1 to 2^448 – 1 for X448).  
- **Scalar decoding**:  
  - X25519: set the three least significant bits of the first byte and the most significant bit of the last byte to zero; set the second most significant bit of the last byte to 1; decode little‑endian.  
  - X448: set the two least significant bits of the first byte to 0; set the most significant bit of the last byte to 1; decode little‑endian.  
- **Output encoding**: For X25519, the unused most significant bit MUST be zero.

### 5.2. Scalar Multiplication Algorithm
The algorithm uses the Montgomery ladder with constant-time cswap. a24 = (A – 2)/4. The cswap function SHOULD be implemented in constant time.

### 5.3. Side-Channel Considerations
- The procedure ensures the same sequence of field operations for all secret key values.  
- Memory access and jump patterns MUST NOT depend on k.  
- Arithmetic MUST NOT leak information about GF(p) values (e.g., timing differences for various multiplications).  
- Implementors should follow ongoing side-channel research.

### 5.4. Test Vectors (Summary)
Two types provided: (1) Input/output pairs for X25519 and X448; (2) Iterated function results (1, 1000, 1,000,000 iterations) with initial k and u set to specific values. Full vectors are given in the original document.

## 6. Diffie-Hellman
### 6.1. Curve25519 (ECDH)
- Alice generates 32 random bytes a[0..31]; transmits K_A = X25519(a, 9).  
- Bob similarly generates b[0..31] and transmits K_B = X25519(b, 9).  
- Shared secret: K = X25519(a, K_B) = X25519(b, K_A).  
- **MAY** check whether K is the all-zero value and abort if so; ORing all bytes together eliminates standard side‑channels.  
- Test vector provided (Alice private, Bob private, shared secret).

### 6.2. Curve448 (ECDH)
- Same as §6.1 but with 56 random bytes and base u-coordinate 5.  
- **MAY** check for all-zero K.  
- Test vector provided.

## 7. Security Considerations
- Curve25519 security is slightly below 128 bits; this is acceptable because asymmetric primitives need not follow power-of-two security levels.  
- Curve448 (~224 bits) is provided as a trade-off between performance and paranoia; both curves are broken by large quantum computers.  
- Protocol designers MUST NOT assume contributory behaviour: small-order inputs can eliminate the other party’s contribution. May be detected via all-zero output check.  
- For each public key, several equivalent public keys produce the same shared secrets; using a public key as an identifier may lead to vulnerabilities unless public keys are included in key derivation.  
- Implementations using generic elliptic-curve libraries (e.g., rejecting points on the twist or non-canonical values) will interoperate with the Montgomery ladder but may be distinguishable.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | For X25519, implementations MUST mask the most significant bit in the final byte of the u-coordinate. | MUST | Section 5 |
| R2 | Implementations MUST accept non-canonical u-coordinate values and process them as if reduced modulo p. | MUST | Section 5 |
| R3 | The cswap function SHOULD be implemented in constant time (independent of swap argument). | SHOULD | Section 5 |
| R4 | For X25519, the most significant bit of the output u-coordinate MUST be zero. | MUST | Section 5 |
| R5 | Implementations MAY check for the all-zero shared secret K and abort if so (both X25519 and X448). | MAY | Section 6 |
| R6 | Protocol designers MUST NOT assume contributory behaviour. | MUST (normative for designers) | Section 7 |

## Informative Annexes (Condensed)
- **Appendix A – Deterministic Generation**: Defines an objective procedure to generate Montgomery curve parameter A from prime p. Cofactor sets: for p ≡ 1 mod 4 choose cofactors {8,4}; for p ≡ 3 mod 4 choose {4,4}. The base point is the minimal positive u in the prime-order subgroup. The algorithms ensure resistance to attacks (trace of Frobenius, MOV degree, CM discriminant). Full Sage scripts are provided.
- **Test Vectors (§5.2)**: Two types: (1) specific scalar/u-coordinate pairs with expected outputs; (2) iterative function application (1, 1000, 1,000,000 iterations). These validate implementation correctness.