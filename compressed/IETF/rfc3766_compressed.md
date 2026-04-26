# RFC 3766: Determining Strengths For Public Keys Used For Exchanging Symmetric Keys
**Source**: IETF, BCP 86 | **Version**: Best Current Practice | **Date**: April 2004 | **Type**: Best Current Practice (Informative / Prescriptive)
**Original**: https://datatracker.ietf.org/doc/rfc3766/

## Scope (Summary)
This document provides guidance for implementors on matching the cryptographic strength of public key algorithms (RSA, Diffie-Hellman, elliptic curve) to symmetric cipher key strengths, based on estimated attack resistance measured in MIPS years. It includes a procedure for determining appropriate key sizes and an equivalence table for common security levels.

## Normative References
None. All references are informative.

## Definitions and Abbreviations
- **NFS**: Number Field Sieve, the best known method for factoring integers and solving discrete logarithms.
- **MIPS year (MY)**: One million instructions per second for one year (~3.1536e13 instructions).
- **TWIRL**: A special-purpose sieving machine that substantially reduces factoring cost.
- **Pollard’s rho method**: A collision-based attack on discrete logarithms requiring an exponent twice the symmetric key size.

## [Section 1] Model of Protecting Symmetric Keys with Public Keys

### 1.1 The key exchange algorithms
- **Diffie-Hellman**: Uses group, generator, exponents; defined with prime p = 2q+1, generator g. Alice: g^a mod p, Bob: g^b mod p; shared key = g^(ab) mod p.
- **Elliptic curve Diffie-Hellman**: More efficient, uses smaller group. Exponent size must be 2*K bits.
- **RSA key exchange**: Bob has modulus m = p*q, encryption exponent e, decryption exponent d. Alice sends k^e mod m; Bob recovers k.

### Selection procedure (normative)
1. **Determine attack resistance**: Estimate minimum number of computer operations for compromise; take log base 2 = "n".  
   *Note*: 1996 recommended 90 bits, increasing by 2/3 bit/year (~96 bits in 2005).
2. **Choose symmetric cipher** with key ≥ n bits and at least that cryptanalytic strength.
3. **Choose key exchange algorithm** with resistance ≥ n bits.
4. **Choose authentication algorithm** with resistance ≥ n bits (unless authentication keys are changed frequently).

Cross-references: [RFC2409] for Diffie-Hellman groups and elliptic curve references.

## [Section 2] Determining the Effort to Factor

### 2.1 Choosing parameters for the equation
- **NFS complexity**: L(n) = k * e^((1.92+o(1)) * cubrt(ln(n) * (ln(ln(n)))^2)).  
- Document uses empirical k≈0.02, o(1)=0 for numbers 100–200 decimal digits.  
  *Formula for MIPS years*: MYs = 6e-16 * e^(1.92 * cubrt(ln(n) * (ln(ln(n)))^2)).

### 2.2 Choosing k from empirical reports
- Factoring RSA130 (430 bits) ~500 MYs, RSA140 ~2000 MYs, RSA155 (512 bits) ~8000 MYs, RSA160 ~3000 MYs.  
- Empirical k ≈ 0.02 gives ~5–6 bits less effective strength than naive L(n).

### 2.3 Pollard’s rho method
- For Diffie-Hellman, exponent must be **at least 2*K bits** to resist Pollard’s rho.  
- For elliptic curve, multiplier size also 2*K bits, modulus can be 2*K bits.  
- Normalizing factor between symmetric key search and discrete log operations is only a few bits.

### 2.4 Limits of large memory and many machines
- Silverman (references [SILIEEE99], [SIL00]) predicts 1024-bit RSA factoring not feasible until ~2037 due to memory and machine constraints.  
- **Document notes**: This is speculative; embedded systems may change availability. Recommends periodic reconsideration.

### 2.5 Special purpose machines
- TWIRL design (2003) can sieve 512-bit numbers in 10 minutes for $10K; 1024-bit in one year for $10M.  
- Implies speed-up factor of ~2 million over commodity processors.

## [Section 3] Compute Time for the Algorithms

### 3.1 Diffie-Hellman Key Exchange
- **Effort**: ~2*K n-by-n-word multiplies, where n = modulus words.  
- Doubling modulus quadruples operations.  
- Cross-reference: [RFC2409] for group sizes.

### 3.1.1 Diffie-Hellman with elliptic curve groups
- Equivalent security: 200-bit EC group vs 2048-bit modular group.  
- Relative time: ((2048/200)^2)/20 ≈ 5 times faster for EC.

### 3.2 RSA encryption and decryption
- **Encryption**: ~28 n-by-n-word multiplies (small exponent e).  
- **Decryption**: Using CRT, effort ≈ j/4 n-by-n-word multiplies.  
- Doubling modulus: encryption cost ×4, decryption cost ×8.

### 3.3 Real-world examples
- Summarized tables from Celeron 400 MHz and Alpha 500 MHz for DH (modular and elliptic curve) and RSA signing (512–2048 bits).  
- 1024-bit RSA decryption ~0.9 ms on 500 MHz Itanium.

## [Section 4] Equivalences of Key Sizes

- Assumes system security requirement of 112 bits for illustration.  
- TripleDES has effective 112-bit key; AES 128-bit is ~16 bits stronger.  
- Two attack models:

### 4.1 Key equivalence against special purpose brute force hardware
- Attacker with $1T can perform 5e12 MYs/year.  
- Solving for n: n ≈ 10^(625) = 2^2077 → modulus ~2100 bits for RSA/DH.

### 4.2 Key equivalence against conventional CPU brute force attack
- 300 instructions per TripleDES encryption; break 2^112 keys: 1.6e36 instructions.  
- Solving: n ≈ 10^(734) = 2^2439 → modulus ~2400 bits.  
- Conservative authors recommend >4000 bits for 50-year protection.

### 4.3 A One Year Attack: 80 bits of strength
- Attacker with $1T can crack 80-bit symmetric key in one year.  
- Equivalent modulus: n ≈ 2^1195 → ~1200 bits.

### 4.4 Key equivalence for other ciphers
- AES 128-bit ≈ 2^16 more work than TripleDES → modulus ~700 bits longer.  
- AES 256-bit safe for centuries if Moore’s Law continues; otherwise 128-bit keys safe “forever”.

### 4.5 Hash functions for deriving symmetric keys from public key algorithms
- **Requirement**: Use a cryptographic hash function over the entire shared secret.  
- If desired key length > hash output, iterate with counter as in:  
  `K1 = SHA(DHkey | 0x00)`, `K2 = select_32_bits(SHA(K1 | 0x01))` etc.  
- **Better**: Use hash with output ≥ desired symmetric key length (e.g., SHA-256, SHA-384, SHA-512) to preserve entropy.

### 4.6 Importance of randomness
- **Requirement**: Secret exponents must be chosen from truly random bits; insufficient randomness weakens security.  
- Cross-reference: [ECS] (RFC 1750) for randomness recommendations.

## [Section 5] Conclusion

### Table: Equivalent Key Sizes (general purpose computers, year 2000 hardware)

| System Attack Resistance (bits) | Symmetric Key Size (bits) | RSA/DH Modulus Size (bits) | DSA Subgroup Size (bits) |
|--------------------------------|---------------------------|----------------------------|--------------------------|
| 70                             | 70                        | 947                        | 129                      |
| 80                             | 80                        | 1228                       | 148                      |
| 90                             | 90                        | 1553                       | 167                      |
| 100                            | 100                       | 1926                       | 186                      |
| 150                            | 150                       | 4575                       | 284                      |
| 200                            | 200                       | 8719                       | 383                      |
| 250                            | 250                       | 14596                      | 482                      |

### 5.1 TWIRL Correction
- If TWIRL is realized, subtract ~11 bits from system security column (e.g., 89 bits → RSA modulus ~1900 bits).

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | The three quantities (system strength, symmetric key strength, public key strength) must be consistently matched for any network protocol usage. | must | Abstract / §1 |
| R2 | Determine attack resistance n as minimum number of computer operations (log₂). | should | §1 step 1 |
| R3 | Choose symmetric cipher with key ≥ n bits and at least that cryptanalytic strength. | should | §1 step 2 |
| R4 | Choose key exchange algorithm with resistance ≥ n bits. | should | §1 step 3 |
| R5 | Choose authentication algorithm with resistance ≥ n bits (unless keys changed frequently). | should | §1 step 4 |
| R6 | DH exponent must be at least 2*K bits to resist Pollard’s rho. | must | §2.3 |
| R7 | For elliptic curve DH, multiplier must be 2*K bits. | must | §2.3 |
| R8 | Use a cryptographic hash function over the entire DH shared secret to derive symmetric key. | should | §4.5 |
| R9 | If desired symmetric key length exceeds hash output, iterate with distinct counters to avoid entropy loss. | should | §4.5 |
| R10 | Secret exponents must be chosen based on truly random bits. | must | §4.6 |

## Informative Annexes (Condensed)

- **Annex A: Historical Factoring Efforts (§2.2)**: Empirical data from factoring RSA130–160 shows effective k≈0.02, giving ~5–6 bits lower effective strength than naive formula.
- **Annex B: Practical Limits of Factoring (§2.4)**: Silverman’s analysis suggests 1024-bit RSA safe until ~2037 due to memory/processor limits; document notes uncertainty from embedded systems.
- **Annex C: TWIRL Special-Purpose Machine (§2.5)**: Reduces factoring cost by factor ~2 million; could break 1024-bit RSA in one year at $10M.
- **Annex D: Real-World Performance Data (§3.3)**: Tables of modular exponentiation times on Celeron 400 MHz, Alpha 500 MHz, and Pentium II–350 for various modulus sizes; 2048-bit RSA signing ~387 ms.
- **Annex E: Hash Function Iteration (§4.5)**: Detailed examples for using SHA-1 to produce keys longer than 160 bits while preserving entropy.
- **Annex F: Randomness Importance (§4.6)**: Reference to RFC 1750; insufficient randomness is a common vulnerability.

## Security Considerations
The equations and values are approximate; predictions cannot be completely accurate. Empirical results used for calibration may contain inaccuracies. The authors aim for minimal variance from real-world experience.

## Informational References
- [DL]: Dodson & Lenstra, NFS with four large primes, Crypto 95.
- [ECS]: Eastlake et al., "Randomness Recommendations for Security", RFC 1750, 1994.
- [GIL98]: "Cracking DES", EFF, 1998.
- [GOR93]: Gordon, "Discrete logarithms in GF(p) using NFS", SIAM 1993.
- [LEN93]: Lenstra & Lenstra (eds), "Development of the NFS", Springer 1993.
- [MH81]: Merkle & Hellman, "Security of Multiple Encryption", CACM 1981.
- [ODL95]: Odlyzko, "Future of Integer Factorization", RSA Labs CryptoBytes 1995.
- [ODL99]: Odlyzko, "Discrete logarithms: past and future", 1999.
- [POL78]: Pollard, "Monte Carlo methods for index computation mod p", Math. Comp. 1978.
- [RFC2409]: Harkins & Carrel, "The Internet Key Exchange (IKE)", RFC 2409, 1998.
- [SCH95]: Schroeppel et al., "Fast Key Exchange With Elliptic Curve Systems", Crypto 1995.
- [SHAMIR03]: Shamir & Tromer, "Factoring Large Numbers with the TWIRL Device", Crypto 2003.
- [SIL00]: Silverman, RSA Laboratories Bulletin #13, April 2000.
- [SILIEEE99]: Silverman, "The Mythical MIPS Year", IEEE Computer, August 1999.