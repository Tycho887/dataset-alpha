# RFC 6149: MD2 to Historic Status
**Source**: IETF | **Version**: N/A | **Date**: March 2011 | **Type**: Informational
**Original**: http://www.rfc-editor.org/info/rfc6149

## Scope (Summary)
This document retires the MD2 message digest algorithm and moves RFC 1319 (MD2) to Historic status, citing cryptographic weaknesses. It discusses the rationale, impact on referencing RFCs, and recommends deprecation.

## Normative References
None.

## Definitions and Abbreviations
- **MD2**: A message digest algorithm producing a 128-bit fingerprint, defined in RFC 1319.
- **Pre-image attack**: An attack that finds a message hashing to a given digest.
- **Second pre-image attack**: An attack that finds a second message with the same digest as a given message.
- **Collision attack**: An attack that finds two distinct messages with the same digest.

## Section 1: Introduction
- MD2 [RFC1319] takes input of arbitrary length and outputs a 128-bit digest.
- This document moves RFC 1319 to Historic status; attacks on MD2 are discussed, with assumed familiarity with [HASH-Attack] (RFC 4270).

## Section 2: Rationale
- MD2 (1992) is not collision-free [ROCH1995] [KNMA2005] [ROCH1997]; collision attacks are not significantly better than birthday bound.
- Successful pre-image and second pre-image attacks exist [KNMA2005] [MULL2004] [KMM2010].

## Section 3: Documents that Reference RFC 1319
List of RFCs referencing MD2, grouped by maturity (Proposed Standard, Informational, Experimental). Detailed list preserved in original; condensed here to avoid redundancy.
- PS: [RFC3279] (PKIX), [RFC4572] (TLS/SDP)
- Informational: [RFC1983] (Glossary), [RFC2315] (PKCS#7), [RFC2898] (PKCS#5), [RFC3447] (PKCS#1)
- Experimental: [RFC2660] (S-HTTP)
- Also [RFC2313] (PKCS#1 v1.5), [RFC2437] (PKCS#1 v2.0) – obsoleted or historic.

## Section 4: Impact on Moving MD2 to Historic
- Minimal impact on referencing RFCs:
  - TLS dropped MD2 support in TLS 1.1.
  - [RFC4572] makes MD2 optional; SHA-1 preferred.
  - [RFC3279] includes MD2 for backward compatibility but discourages use.
  - Informational RFCs: [RFC1983] only listed it as example; [RFC2313] updated stance; [RFC2898] recommends against PBES using MD2; [RFC2315] replaced by CMS (RFCs 2630, 3369, 5652) – MD2 dropped in [RFC3370].
  - [RFC2660] largely supplanted by RFC 2818; only RFC using HMAC-MD2.

## Section 5: Other Considerations
- MD2 is slower than MD4, MD5, and SHA-1/2 (SHS) because it was optimized for 8-bit machines.

## Section 6: Security Considerations
- MD2 design: nonlinear checksum as t+1 block; collision resistance depends on checksum.
- Without checksum: collision in 2^12 operations; with checksum: best collision attack 2^63.3 with 2^50 memory [MULL2004], not significantly better than birthday.
- **Pre-image attack**: Can be found with 2^104 MD2 operations [KMM2010]; improved to 2^73 operations. This invertibility may leak HMAC keys when used in HMAC.
- **Second pre-image**: Pre-image attack implies second pre-image; more severe than collision for digital signatures.
- **MD2 must not be used for digital signatures.** [Normative]
- Guidance on algorithm strengths: [SP800-57] and [SP800-131].

## Section 7: Recommendation
- **MD2 is not a reasonable candidate for further standardization and should be deprecated in favor of one or more existing hash algorithms (e.g., SHA-256 [SHS]).**
- RSA Security agrees with moving to Historic status.
- **Implementations should strongly consider removing support and migrating to another hash algorithm.** [Normative]

## Section 8: Acknowledgements
(Summary) Thanks to RSA and cryptographers; contributors: Ran Atkinson, Alfred Hoenes, John Linn, Martin Rex.

## Section 9: Informative References
- [HASH-Attack] – RFC 4270 (2005)
- [KMM2010] – Cryptanalysis of MD2, Journal of Cryptology 23(1):72-90, 2010
- [KNMA2005] – Preimage and Collision Attacks on MD2, FSE 2005
- [MD2] – RFC 1319 (1992)
- [MD4] – RFC 1320
- [MD5] – RFC 1321
- [MULL2004] – The MD2 Hash Function Is Not One-Way, ASIACRYPT 2004
- [RFC1983], [RFC2104], [RFC2313], [RFC2315], [RFC2437], [RFC2630], [RFC2660], [RFC2898], [RFC3279], [RFC3369], [RFC3370], [RFC3447], [RFC4572], [RFC5652] – as cited.
- [ROCH1995] – The compression function of MD2 is not collision free, SAC ’95
- [ROCH1997] – MD2 is not secure without the checksum byte, Des. Codes Cryptogr. 12(3), 245-251
- [SHS] – FIPS 180-3 (2008)
- [SP800-57] – NIST SP 800-57 Part 1 (Revised)
- [SP800-131] – NIST SP 800-131 (Draft, 2010)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | MD2 must not be used for digital signatures. | shall | Section 6 |
| R2 | MD2 should be deprecated in favor of one or more existing hash algorithms (e.g., SHA-256). | should | Section 7 |
| R3 | Implementations should strongly consider removing support for MD2 and migrating to another hash algorithm. | should | Section 7 |