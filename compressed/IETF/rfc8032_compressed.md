# RFC 8032: Edwards-Curve Digital Signature Algorithm (EdDSA)
**Source**: IRTF (Crypto Forum Research Group) | **Version**: January 2017 | **Date**: January 2017 | **Type**: Informational
**Original**: https://www.rfc-editor.org/info/rfc8032

## Scope (Summary)
This document specifies the Edwards-curve Digital Signature Algorithm (EdDSA) with recommended parameters for the edwards25519 and edwards448 curves. It provides an implementation-oriented description, sample code in Python, and test vectors. The document is published for informational purposes and represents the consensus of the IRTF Crypto Forum Research Group.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC6234] Eastlake 3rd, D. and T. Hansen, "US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF)", RFC 6234, May 2011.
- [RFC7748] Langley, A., Hamburg, M., and S. Turner, "Elliptic Curves for Security", RFC 7748, January 2016.
- [FIPS202] National Institute of Standards and Technology, "SHA-3 Standard: Permutation-Based Hash and Extendable-Output Functions", FIPS PUB 202, August 2015.

## Definitions and Abbreviations
- **EdDSA**: Edwards-curve Digital Signature Algorithm.
- **PureEdDSA**: EdDSA where the prehash function PH is the identity function (PH(M) = M).
- **HashEdDSA**: EdDSA where PH is a collision-resistant hash function (e.g., SHA-512).
- **Ed25519**: PureEdDSA instantiated with edwards25519 curve parameters.
- **Ed25519ctx**: EdDSA with edwards25519, phflag=0, and a non-empty context.
- **Ed25519ph**: EdDSA with edwards25519, phflag=1, and PH = SHA-512.
- **Ed448**: PureEdDSA instantiated with edwards448 curve parameters.
- **Ed448ph**: EdDSA with edwards448, phflag=1, and PH = SHAKE256(x,64).
- **dom2(x, y)**: The blank octet string for Ed25519; otherwise the prefix string "SigEd25519 no Ed25519 collisions" || octet(x) || octet(OLEN(y)) || y.
- **dom4(x, y)**: The prefix string "SigEd448" || octet(x) || octet(OLEN(y)) || y.
- **b**: Number of bits in public keys and signatures (256 for Ed25519, 456 for Ed448).
- **c**: Base-2 logarithm of the cofactor (3 for Ed25519, 2 for Ed448).
- **n**: Top bit position for secret scalars (254 for Ed25519, 447 for Ed448).
- **L**: Order of the base point B.
- **PH**: Prehash function.
- **ENC(S)**: Little-endian b-bit encoding of integer S.
- **ENC(x,y)**: b-bit encoding of a curve point: (b-1)-bit encoding of y concatenated with sign bit of x.

## Notation and Conventions
- Bit strings are converted to octets left-to-right, LSB first.
- Integers are encoded in little-endian.
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are used as per RFC 2119.

## EdDSA Algorithm (Generic Description)
The EdDSA signature system has 11 parameters (p, b, GF(p) encoding, hash H, c, n, d, a, B, L, PH). Points on the curve form a group with complete addition formulas. Encoding, key generation, signing, and verification follow the description in sections 3.1–3.4.

- **Encoding**: Points encoded as ENC(y) with sign bit of x.
- **Keys**: Private key k (b-bit). Compute H(k) = (h0..h2b-1). Derive secret scalar s from h0..hb-1 after clamping (set bits c..n, clear bits 0..c-1 and n+1..b-1). Public key A = [s]B encoded.
- **Sign** (PureEdDSA): r = H(hb..h2b-1 || M) mod 2^(2b); R = [r]B; S = (r + H(ENC(R) || ENC(A) || M) * s) mod L. Signature = ENC(R) || ENC(S).
- **Verify** (PureEdDSA): Decode R and A; compute h = H(ENC(R) || ENC(A) || M); check [2^c * S]B = [2^c]R + [2^c * h]A. Reject if parsing fails or group equation fails.
- EdDSA signature of M is PureEdDSA signature of PH(M).

## Instances and Variants
### Ed25519, Ed25519ctx, Ed25519ph
- **Parameters**: p = 2^255-19, b=256, H(x)=SHA-512(dom2(phflag,context)||x), c=3, n=254, d=-121665/121666, a=-1, B=(15112221349535807..., 46316835694926478...), L=2^252+27742317777372353535851937790883648493, PH(x)=x (identity) for Ed25519; PH=SHA-512 for Ed25519ph.
- **dom2**: Empty for Ed25519; for Ed25519ctx phflag=0, context must be non-empty; for Ed25519ph phflag=1.
- **Key Generation**: Private key 32 octets; hash with SHA-512; prune lower 3 bits of first octet, clear high bit, set second-highest bit of last octet.
- **Sign**: Compute SHA-512(dom2(F,C) || prefix || PH(M)), interpret as r mod L; R = [r]B; compute k = SHA-512(dom2(F,C) || R || A || PH(M)) mod L; S = (r + k*s) mod L; signature = R (32 octets) || S (32 octets).
- **Verify**: Split signature; decode R and S (0 <= S < L); compute k; check [8][S]B == [8]R + [8][k]A'.

### Ed448 and Ed448ph
- **Parameters**: p = 2^448-2^224-1, b=456, H(x)=SHAKE256(dom4(phflag,context)||x, 114), c=2, n=447, d=-39081, a=1, B=(224580040295924..., 298819210078481...), L=2^446-1381806680989511535200738674851542688033692474882178609894547503885, PH(x)=x for Ed448; PH=SHAKE256(x,64) for Ed448ph.
- **dom4**: Prefix "SigEd448" || octet(phflag) || octet(len(context)) || context.
- **Key Generation**: Private key 57 octets; hash with SHAKE256(x,114); clear low 2 bits of first octet, clear all bits of last octet, set high bit of second-to-last octet.
- **Sign**: Similar to Ed25519 but with SHAKE256 and output 114 octets.
- **Verify**: Check [4][S]B == [4]R + [4][k]A'.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Private key MUST be generated from cryptographically secure random data | SHALL | Section 5.1.5, 5.2.5 |
| R2 | For Ed25519, context MUST be empty | MUST | Section 5.1 |
| R3 | Context maximum length is 255 octets | MUST | Section 5.1, 5.2 |
| R4 | Signature verification fails if S >= L | MUST | Section 3.4 |
| R5 | The context SHOULD be a constant string; SHOULD NOT incorporate variable elements from the message | SHOULD | Section 8.3 |
| R6 | Contexts SHOULD NOT be used opportunistically | SHOULD | Section 8.3 |
| R7 | If contexts are used, all signature schemes in the protocol SHOULD support contexts | SHOULD | Section 8.3 |
| R8 | Ed25519ph and Ed448ph variants SHOULD NOT be used (prefer non-prehashed) | SHOULD NOT | Section 8.5 |
| R9 | For 128-bit security, Ed25519 is RECOMMENDED; otherwise Ed448 | RECOMMENDED | Section 8.5 |
| R10 | Verification formula may check [S]B = R + [k]A' instead of cofactor version (not required) | MAY | Section 5.1.7, 5.2.7 |
| R11 | Secret scalar clamping: lowest c bits cleared, highest bit set, others cleared | MUST | Section 5.1.5, 5.2.5 |

## Security Considerations (Condensed)
- **Side-Channel Leaks**: Implementations SHOULD be side-channel silent (no data-dependent branches). EdDSA is easier than other schemes due to complete addition formulas.
- **Randomness**: Signatures are deterministic; private key generation requires randomness but few missing bits not disastrous.
- **Use of Contexts**: Context SHOULD be a constant string; SHOULD NOT be opportunistic; SHOULD be supported by all signature schemes in a protocol.
- **Signature Malleability**: Ed25519 and Ed448 signatures are not malleable because S < L is checked.
- **Choice of Primitive**: Ed25519 (128-bit strength) is RECOMMENDED; Ed448 for higher security. Prehashed variants SHOULD NOT be used.
- **Mixing Prehashes**: Schemes are resistant to mixing; same key pair can be used for Ed25519, Ed25519ctx, Ed25519ph (and similarly for Ed448).
- **Large Data**: Avoid signing large amounts at once; receiver MUST buffer entire message for verification.
- **Cofactor Multiplication**: Verification includes cofactor multiplication to avoid disagreements; not strictly necessary but recommended.
- **SHAKE256 Usage**: Acceptable for Ed448 despite not being a hash function; output lengths fixed.

## Test Vectors
Test vectors are provided for Ed25519 (7 tests), Ed25519ctx (4 tests), Ed25519ph (1 test), Ed448 (8 tests), and Ed448ph (2 tests), including zero-length messages and various contexts. Vectors are hex-encoded.

## Informative Annexes (Condensed)
- **Appendix A – Ed25519/Ed448 Python Library**: Provides a complete Python 3.2+ implementation of Ed25519 and Ed448 including SHA-3, field arithmetic, point operations, and signature schemes. Not intended for production; for illustration only.
- **Appendix B – Library Driver**: A command-line tool to run test vectors from the file format used by ed25519.cr.yp.to.