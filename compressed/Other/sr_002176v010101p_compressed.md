# ETSI SR 002 176: Electronic Signatures and Infrastructures (ESI); Algorithms and Parameters for Secure Electronic Signatures
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2003-03 | **Type**: Normative
**Original**: http://www.etsi.org (reference PDF)

## Scope (Summary)
This document defines an initial set of approved cryptographic algorithms, parameters, and signature suites for secure electronic signatures, aligned with Directive 1999/93/EC. It covers management practices, hash functions, padding methods, signature algorithms (RSA, DSA, ECDSA, ECGDSA), key generation, and random number generation. These approved items shall be referenced in Protection Profiles for SSCDs and CSPs.

## Normative References
- [1] Directive 1999/93/EC
- [2] ISO/IEC 9979 (1999)
- [3] IETF RFC 2459 (1999)
- [4] ISO/IEC 10118-3 (1998)
- [5] FIPS Publication 180-1 (1995)
- [6] PKCS #1 v2.0 (1998)
- [7] ISO/IEC 14888-3 (1999)
- [8] FIPS Publication 140-1 (1994)
- [9] FIPS Publication 186-2 (2000)
- [10] IEEE P1363 (2000)
- [11] ANSI X9.62-1998 (1998)
- [12] ISO/IEC 9796-3 (2000)
- [13] ISO/IEC FCD 15946-2 (1999)
- [14] ISO/IEC CD 15946-4 (2001)
- [15] IETF RFC 1750 (1994)
- [16] ANSI X9.17-1985 (1985)
- [17] PKCS #1 v2.1 draft 2 (2001)
- [18] Change Recommendation for ANSI X9.30-1995, Part 1, Draft April 2001
- [19] IETF RFC 3161 (2001)

## Definitions and Abbreviations
- **bit length**: The bit length of integer p is r if 2^(r-1) ≤ p < 2^r.
- **Management Activity (MA)**: action that shall be taken by the electronic signature committee under circumstances specified in clause 4.
- **signature suite**: combination of a signature algorithm with its parameters, a key generation algorithm, a padding method, and a cryptographic hash function.
- **Abbreviations**: A9C, CRL, CRT, CSP, CWA, DSA, ECDSA, ECGDSA, MA, OID, PRNG, RSA, SCD, SSCD, SVD, TRNG.

## 4 Algorithms and Parameters for Secure Electronic Signatures

### 4.1 Management Activities
- **MA**: Shall enable dynamic updating of the approved lists to respond to:
  1. Need to introduce new algorithms (rapid, within 6 months).
  2. Phasing out due to crypto advances (within 6 months).
  3. Immediate removal due to new attacks (within 1 month).
- Mechanisms shall be put in place through A9C.

### 4.2 Signature Suites for Secure Electronic Signatures
- Algorithms and parameters **shall** be used only in predefined **signature suites**.
- A suite consists of: signature algorithm (with parameters), key generation algorithm, padding method, and cryptographic hash function.
- If a component is cancelled, the suite **must** be cancelled. If updated, the suite **must** be updated.
- Each suite entry has a "valid until (signing)" date; dates shall be reviewed regularly (e.g., annually).

**Table 1: Approved Signature Suites**

| Suite Index | Signature Algorithm | Parameters | Key Gen Algorithm | Padding | Hash | Valid Until |
|-------------|-------------------|-------------|------------------|---------|------|-------------|
| 001 | rsa | MinModLen=1020 | rsagen1 | emsa-pkcs1-v1_5 | sha1 | 31.12.2005 |
| 002 | rsa | MinModLen=1020 | rsagen1 | emsa-pss | sha1 | 31.12.2005 |
| 003 | rsa | MinModLen=1020 | rsagen1 | emsa-pkcs1-v1_5 | ripemd160 | 31.12.2005 |
| 004 | rsa | MinModLen=1020 | rsagen1 | emsa-pss | ripemd160 | 31.12.2005 |
| 005 | dsa | pMinLen=1024, qMinLen=160 | dsagen1 | - | sha1 | 31.12.2005 |
| 006 | ecdsa-Fp | qMinLen=160, r0Min=104, MinClass=200 | ecgen1 | - | sha1 | 31.12.2005 |
| 007 | ecdsa-F2m | qMinLen=160, r0Min=104, MinClass=200 | ecgen2 | - | sha1 | 31.12.2005 |
| 008 | ecgdsa-Fp | qMinLen=160, r0Min=104, MinClass=200 | ecgen1 | - | sha1 | 31.12.2005 |
| 009 | ecgdsa-Fp | qMinLen=160, r0Min=104, MinClass=200 | ecgen1 | - | ripemd160 | 31.12.2005 |
| 010 | ecgdsa-F2m | qMinLen=160, r0Min=104, MinClass=200 | ecgen2 | - | sha1 | 31.12.2005 |
| 011 | ecgdsa-F2m | qMinLen=160, r0Min=104, MinClass=200 | ecgen2 | - | ripemd160 | 31.12.2005 |

### 4.3 Cryptographic Hash Functions
- A hash function **must** be collision-resistant. If not, it **must** be removed (see 4.1).

**Table 2: Approved Hash Functions**

| Entry Index | Short Name | Adoption Date | Normative References |
|-------------|------------|---------------|----------------------|
| 2.01 | sha1 | 01.01.2001 | [4] and [5] |
| 2.02 | ripemd160 | 01.01.2001 | [4] |

### 4.4 Padding Methods
- If required by an algorithm, padding **shall** meet requirements in normative references.

**Table 3: Approved Padding Methods**

| Entry Index | Short Name | Random Generator | Parameters | Adoption Date | Normative Reference |
|-------------|------------|------------------|------------|---------------|---------------------|
| 3.01 | emsa-pkcs1-v1_5 | - | - | 01.01.2001 | [6] clause 9.2.1 |
| 3.02 | emsa-pss | TBD | TBD | TBD | [17] clause 9.2.2 |

### 4.5 Signature Algorithms
- **General**: Applied to hashcode; parameters must be defined; SCD must be practically impossible to compute from SVD. Minimum modulus for RSA is 1020 bits to allow for implementations that cannot use topmost bits.

**Table 4: Approved Signature Algorithms**

| Entry Index | Short Name | Parameters | Key Gen Algorithm | Adoption Date | Normative References |
|-------------|------------|------------|------------------|---------------|---------------------|
| 1.01 | rsa | MinModLen=1020 | rsagen1 | 01.01.2001 | [7] |
| 1.02 | dsa | pMinLen=1024, qMinLen=160 | dsagen1 | 01.01.2001 | [9] |
| 1.03 | ecdsa-Fp | qMinLen=160, r0Min=104, MinClass=200 | ecgen1 | 01.01.2001 | [9], [11] |
| 1.04 | ecdsa-F2m | qMinLen=160, r0Min=104, MinClass=200 | ecgen2 | 01.01.2001 | [9], [11] |
| 1.05 | ecgdsa-Fp | qMinLen=160, r0Min=104, MinClass=200 | ecgen1 | 25.06.2001 | [13] |
| 1.06 | ecgdsa-F2m | qMinLen=160, r0Min=104, MinClass=200 | ecgen2 | 25.06.2001 | [13] |

**Table 5: Approved Key Generation Algorithms**

| Entry Index | Short Name | Signature Algorithm | Random Number Generation Method | Parameters | Adoption Date | Normative References |
|-------------|------------|-------------------|--------------------------------|------------|---------------|---------------------|
| 4.01 | rsagen1 | rsa | trueran or pseuran | EntropyBits ≥ 128 or SeedLen ≥ 128 | 01.01.2001 | - |
| 4.02 | dsagen1 | dsa | trueran or pseuran | EntropyBits ≥ 128 or SeedLen ≥ 128 | 01.01.2001 | [18] |
| 4.03 | ecgen1 | ecdsa-Fp, ecgdsa-Fp | trueran or pseuran | EntropyBits ≥ 128 or SeedLen ≥ 128 | 01.01.2001 | - |
| 4.04 | ecgen2 | ecdsa-F2m, ecgdsa-F2m | trueran or pseuran | EntropyBits ≥ 128 or SeedLen ≥ 128 | 01.01.2001 | - |

#### 4.5.2 RSA
- **Parameters**: p and q prime, length of n ≥ MinModLen (1020), p and q roughly equal length, sufficiently many primes.
- **SCD**: private exponent d and modulus n.
- **SVD**: public exponent e and modulus n. CRT allowed.
- **rsagen1**: Generate p, q using trueran or pseuran with appropriate seed; each prime influenced by EntropyBits bits of true randomness or SeedLen seed; primality test with error probability ≤ 2⁻⁶⁰. Select e coprime to lcm(p-1,q-1); compute d as modular inverse.

#### 4.5.3 DSA
- **Parameters**: p at least pMinLen (1024), q at least qMinLen (160), g as per [9]. SCD: x and k (0<k<q, regenerated each signature). SVD: p,q,g and y = g^x mod p. No padding of hashcode needed.
- **dsagen1**: Generate p,q per [9] appendix 2.2. Generate x with trueran or pseuran (EntropyBits ≥128 or SeedLen≥128). Generate k similarly; [18] recommended for pseudo-random to mitigate Bleichenbacher attack.

#### 4.5.4 ECDSA-Fp
- **Parameters**: Large prime p, prime q≥qMinLen, elliptic curve E over F_p with order divisible by q, point P of order q. Class number ≥ MinClass; r0 > r0Min. SCD: x,k (0<x,k<q). SVD: Q=xP.
- **ecgen1**: p generated per [11] or use generalized Mersenne primes from [9]. Curve selected per [11]. Generate x,k with trueran or pseuran (EntropyBits≥128 or SeedLen≥128); k need not use same method.

#### 4.5.5 ECDSA-F2m
- **Parameters**: m prime, q≥qMinLen, elliptic curve E over F_{2^m} with order divisible by q, not definable over F_2, P of order q. Class number and r0 as above. Field representation common to signer and verifier; recommended irreducible trinomial or pentanomial per [9][10]. SCD: x,k; SVD: Q=xP.
- **ecgen2**: m fixed per [11]; curve selected per [11]; generate x,k with trueran or pseuran.

#### 4.5.6 EC-GDSA based on E(F_p)
- **Parameters**: as ecdsa-Fp per [13]; variant with modified signing equation.
- **Key generation**: same as ecgen1.

#### 4.5.7 EC-GDSA based on E(F_{2^m})
- **Parameters**: as ecdsa-F2m per [13]; variant with modified signing equation.
- **Key generation**: same as ecgen2.

### 4.6 Random Number Generation
**Table 6: Approved Random Number Generation Methods**

| Entry Index | Short Name | Parameters | Adoption Date | Normative References |
|-------------|------------|------------|---------------|---------------------|
| 5.01 | trueran | EntropyBits | 01.01.2001 | - |
| 5.02 | pseuran | SeedLen | 01.01.2001 | - |
| 5.03 | cr_to_X9.30_x | SeedLen | 01.01.2001 | [18] |
| 5.04 | cr_to_X9.30_k | SeedLen | 01.01.2001 | [18] |

- **trueran**: Physical noise source + post-treatment; primary noise must be statistically tested regularly; guessing effort at least equivalent to EntropyBits random bits.
- **pseuran**: Initialized by genuine random seed (SeedLen); output must satisfy: no prior knowledge of bits, no inference from partial output, no recovery of seed/state from output. Re-seeding allowed except in smartcards; no backups of seed/state permitted. Expected effort to recover internal state ~ guessing SeedLen bits.
- **cr_to_X9.30_x and cr_to_X9.30_k**: As specified in [18] B.2.1 and B.2.2.

## 5 Normative Annexes

### Annex A (Normative): Updating Algorithms and Parameters
- **Process**: Dynamic updates to the approved lists shall be performed based on crypto/technology developments.
- Cases: adopting new algorithm (requires complete parameter set), cancelling an algorithm (with reasoning), updating parameter values (with reasoning and transition period).
- If any component of a signature suite is cancelled/updated, the suite **must** be cancelled/updated.
- Monitoring: continuous activity by notified bodies; set cancellation/update date allowing transition period.
- If security implications are severe, products should be withdrawn before planned expiry; CSPs should ensure certificate validity does not exceed presumed validity of algorithms/parameters.

## 6 Informative Annexes (Condensed)

- **Annex B (Informative) – Algorithm Object Identifiers**: Provides OIDs for algorithms (e.g., rsa, sha1, id-dsa, id-ecdsa-with-sha1, id-rsassa-pss). Users should consult owner organizations for updates.

- **Annex C (Informative) – Generation of RSA Keys for Signatures**: Describes probabilistic primality testing (Miller-Rabin) and generation of prime numbers, modulus, and keys. Recommends using random primes without special form; strong primes not necessary. Suggests methods for generating modulus of exactly k bits.

- **Annex D (Informative) – On the Generation of Random Data**: Explains need for random numbers in cryptography (distinct values, secret keys, public parameters, temporary secrets). Describes true random number generation (TRNG) from physical sources with hashing to extract entropy, and pseudorandom generation (PRNG) from an initial seed. Discusses statistical tests (e.g., FIPS 140-1), and presents examples (ANSI X9.17, FIPS 186, RSA/Blum-Blum-Shub PRNGs). Concludes with recommendations for secure generation.

- **Annex E (Informative) – Verification**: Recommends that verification of signatures be performed at most one year after the signature suite’s expiration date for signing, unless additional measures (time-stamping, re-signing) are taken. (No legal impact.)

- **Annex F (Informative) – Bibliography**: Lists references for further reading on cryptographic algorithms, random number generation, and related topics.

## Requirements Summary

| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Algorithms and parameters shall be used only in predefined signature suites. | shall | Clause 4.2 |
| R2 | If any component of a suite is cancelled/updated, the suite must be cancelled/updated. | must | Clause 4.2 |
| R3 | Each suite entry shall contain a date representing the last day for signing. | shall | Clause 4.2 |
| R4 | Hash function must be collision-resistant; otherwise must be removed. | must | Clause 4.3 |
| R5 | Hash function removal shall follow management activities (clause 4.1). | shall | Clause 4.3 |
| R6 | Padding method, if required, shall meet requirements in normative references. | shall | Clause 4.4 |
| R7 | Key generation using pseuran requires seed of length SeedLen and at least EntropyBits of true randomness per pivotal value. | shall | Clauses 4.5.2.2, 4.5.3.2, 4.5.4.2, 4.5.5.2 |
| R8 | Random number generation for key generation shall use trueran or pseuran with EntropyBits ≥ 128 or SeedLen ≥ 128. | shall | Table 5 |
| R9 | For DSA, k must be regenerated for each signature; its distribution must be uniform to avoid Bleichenbacher attack. | must | Clause 4.5.3.1 |
| R10 | For DSA, pseudo-random method of [18] shall be used for k generation (FIPS 186 methods not recommended). | shall (implied) | Clause 4.5.3.2 |
| R11 | For RSA, prime generation shall use probabilistic test with error ≤ 2⁻⁶⁰. | shall | Clause 4.5.2.2 |
| R12 | For RSA, p and q should be roughly equal length. | should | Clause 4.5.2.1 |
| R13 | For ECDSA/ECGDSA curves, class number ≥ MinClass and r0 > r0Min. | shall | Clauses 4.5.4.1, 4.5.5.1 |
| R14 | For ECDSA-F2m, curve must not be definable over F_2. | must | Clause 4.5.5.1 |
| R15 | Physical random generator (trueran) shall be statistically tested regularly. | shall | Clause 4.6.2 |
| R16 | Pseudo-random generator (pseuran) output must satisfy: no a priori knowledge, no inference from partial output, no recovery of seed/state. | must | Clause 4.6.3 |
| R17 | No backups of seed or internal state of pseuran generator are permitted. | shall | Clause 4.6.3 |
| R18 | Re-seeding of pseuran in smartcards is not permitted. | shall | Clause 4.6.3 |
| R19 | Management actions (adopt/cancel/update) shall be completed within 6 months for cases 1 and 2, 1 month for case 3. | shall | Clause 4.1 |
| R20 | If a suite component is cancelled/updated, the suite must be cancelled/updated. | must | Annex A |