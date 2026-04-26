# RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace
**Source**: IETF | **Version**: Standards Track | **Date**: July 2005 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc4122

## Scope (Summary)
This specification defines a Uniform Resource Name (URN) namespace for UUIDs (Universally Unique IDentifiers), also known as GUIDs. A UUID is 128 bits long and can guarantee uniqueness across space and time without requiring a central registration process. This document derives from the OSF DCE specification and aligns with ITU-T Rec. X.667 / ISO/IEC 9834-8.

## Normative References
- [1] Zahn, L., Dineen, T., and P. Leach, "Network Computing Architecture", ISBN 0-13-611674-4, January 1990.
- [2] "DCE: Remote Procedure Call", Open Group CAE Specification C309, ISBN 1-85912-041-5, August 1994.
- [3] ISO/IEC 9834-8:2004 (ITU-T Rec. X.667), "Procedures for the operation of OSI Registration Authorities: Generation and registration of Universally Unique Identifiers (UUIDs) and their use as ASN.1 Object Identifier components".
- [4] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [5] Eastlake, D., et al., "Randomness Requirements for Security", BCP 106, RFC 4086, June 2005.
- [6] Moats, R., "URN Syntax", RFC 2141, May 1997.
- [7] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 2234, November 1997.
- [8] National Institute of Standards and Technology, "Secure Hash Standard", FIPS PUB 180-1, April 1995.

## Definitions and Abbreviations
- **UUID**: Universally Unique IDentifier, a 128-bit identifier.
- **GUID**: Globally Unique IDentifier (synonym for UUID).
- **Variant**: Field determining the interpretation of other UUID bits (Section 4.1.1).
- **Version**: Sub-type encoded in 4 bits of time_hi_and_version (Section 4.1.3).
- **Timestamp**: 60-bit value; for version 1, a count of 100-nanosecond intervals since 00:00:00.00, 15 October 1582 (UTC).
- **Clock Sequence**: 14-bit value used to avoid duplicates when clock is set backward or node ID changes.
- **Node**: 48-bit identifier; for version 1, typically an IEEE 802 MAC address.
- **Nil UUID**: Special UUID with all 128 bits set to zero.
- **ABNF**: Augmented Backus-Naur Form (RFC 2234).

## 3. Namespace Registration Template
- **Namespace ID**: UUID
- **Registration date**: 2003-10-01
- **Declared registrant**: JTC 1/SC6 (ASN.1 Rapporteur Group)
- **Syntactic structure**: See ABNF below.
- **Example URN**: `urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6`
- **Uniqueness**: Three algorithms (time-based, random, name-based) ensure global uniqueness.
- **Persistence**: UUIDs are temporally unique within spatial context; inherently difficult to resolve globally.
- **Assignment**: No registration authority needed; IEEE MAC address or alternatives per Section 4.5.
- **Lexical equivalence**: Compare fields as unsigned integers; equality when all fields equal.
- **Conformance with URN syntax**: String representation fully compatible per ABNF.
- **Validation**: No mechanism to determine 'validity' beyond checking timestamp not in future.
- **Scope**: Global.

### UUID String Representation (ABNF)
```
UUID                   = time-low "-" time-mid "-"
                         time-high-and-version "-"
                         clock-seq-and-reserved
                         clock-seq-low "-" node
time-low               = 4hexOctet
time-mid               = 2hexOctet
time-high-and-version  = 2hexOctet
clock-seq-and-reserved = hexOctet
clock-seq-low          = hexOctet
node                   = 6hexOctet
hexOctet               = hexDigit hexDigit
hexDigit = "0" / "1" / "2" / "3" / "4" / "5" / "6" / "7" / "8" / "9" /
           "a" / "b" / "c" / "d" / "e" / "f" /
           "A" / "B" / "C" / "D" / "E" / "F"
```

## 4. Specification

### 4.1 Format
UUID is 16 octets; variant field determines finer structure.

#### 4.1.1 Variant
The variant field (most significant bits of octet 8) determines interpretation. Table (msb0 msb1 msb2):
- `0 x x` – Reserved, NCS backward compatibility.
- `1 0 x` – Variant specified in this document.
- `1 1 0` – Reserved, Microsoft backward compatibility.
- `1 1 1` – Reserved for future definition.

Interoperability with other variants not guaranteed.

#### 4.1.2 Layout and Byte Order
Fields (most significant first):
| Field | Data Type | Octet # | Note |
|---|---|---|---|
| time_low | unsigned 32-bit | 0-3 | Low field of timestamp |
| time_mid | unsigned 16-bit | 4-5 | Middle field of timestamp |
| time_hi_and_version | unsigned 16-bit | 6-7 | High field of timestamp multiplexed with version number |
| clock_seq_hi_and_reserved | unsigned 8-bit | 8 | High field of clock sequence multiplexed with variant |
| clock_seq_low | unsigned 8-bit | 9 | Low field of clock sequence |
| node | unsigned 48-bit | 10-15 | Spatially unique node identifier |

Encoding: 16 octets, network byte order (MSB first). Bit diagram provided.

#### 4.1.3 Version
Version number in most significant 4 bits of time_hi_and_version (bits 4-7).
Table:
- `0001` (1) – Time-based version (this document).
- `0010` (2) – DCE Security version, with embedded POSIX UIDs.
- `0011` (3) – Name-based version using MD5 hashing.
- `0100` (4) – Randomly or pseudo-randomly generated version.
- `0101` (5) – Name-based version using SHA-1 hashing.

#### 4.1.4 Timestamp
- Version 1: 60-bit value representing UTC as 100-ns intervals since 1582-10-15 00:00:00.
- Systems without UTC may use local time consistently (not recommended).
- Version 3/5: Constructed from name per Section 4.3.
- Version 4: Randomly or pseudo-randomly generated (Section 4.4).

#### 4.1.5 Clock Sequence
- Version 1: Helps avoid duplicates when clock set backward or node ID changes.
  - If clock set backward: increment known clock sequence; otherwise set to random value.
  - If node ID changes: set to random number.
  - **MUST** be initially (once per system lifetime) initialized to a random number.
  - Initial value **MUST NOT** be correlated to node identifier.
- Version 3/5: 14-bit value from name (Section 4.3).
- Version 4: Randomly or pseudo-randomly generated (Section 4.4).

#### 4.1.6 Node
- Version 1: Typically IEEE 802 MAC address. For multiple addresses, any available. Multicast bit **must** be set if random address used.
- Version 3/5: 48-bit value from name (Section 4.3).
- Version 4: Randomly or pseudo-randomly generated (Section 4.4).

#### 4.1.7 Nil UUID
All 128 bits set to zero.

### 4.2 Algorithms for Creating a Time-Based UUID (Version 1)

#### 4.2.1 Basic Algorithm
1. Obtain system-wide global lock.
2. Read state (timestamp, clock sequence, node ID) from stable store.
3. Get current time as 60-bit 100-ns ticks since UUID epoch.
4. Get current node ID.
5. If state unavailable or node ID changed: generate random clock sequence.
6. If saved timestamp > current timestamp: increment clock sequence.
7. Save state back to stable store.
8. Release lock.
9. Format UUID per Section 4.2.2.

Performance improvements addressed in subsections: caching state, simulating high-resolution timestamp, periodic writes, block allocation.

#### 4.2.1.1 Reading Stable Storage
State may be read once at boot into shared volatile store. If no stable store available, treat as unavailable (least desirable). If node ID never changes, may be returned without stable store.

#### 4.2.1.2 System Clock Resolution
If system clock resolution less than 100 ns, the UUID service **MUST** either return an error or stall until clock catches up. A count of UUIDs per tick can simulate higher resolution.

#### 4.2.1.3 Writing Stable Storage
State may be written periodically (e.g., setting future timestamp) to reduce writes.

#### 4.2.1.4 Sharing State Across Processes
If shared state access is expensive, allocate blocks of timestamps per process.

#### 4.2.2 Generation Details (Version 1)
- Use UTC-based timestamp and clock sequence determined per Section 4.2.1.
- Set time_low = least significant 32 bits of timestamp.
- Set time_mid = bits 32-47 of timestamp.
- Set 12 least significant bits of time_hi_and_version = bits 48-59 of timestamp.
- Set 4 most significant bits of time_hi_and_version = version number (0001).
- Set clock_seq_low = least significant 8 bits of clock sequence.
- Set 6 least significant bits of clock_seq_hi_and_reserved = most significant 6 bits of clock sequence.
- Set 2 most significant bits of clock_seq_hi_and_reserved to 0 and 1 respectively.
- Set node field = 48-bit IEEE address in same significance order.

### 4.3 Algorithm for Creating a Name-Based UUID (Version 3 or 5)
- Requirements:
  - Same name in same namespace **MUST** produce equal UUIDs.
  - Different names in same namespace should produce different UUIDs (very high probability).
  - Same name in different namespaces should produce different UUIDs.
  - If two UUIDs equal, they were generated from same name in same namespace (very high probability).
- Algorithm:
  1. Allocate namespace ID UUID (see Appendix C for predefined).
  2. Choose MD5 (version 3) or SHA-1 (version 5); SHA-1 preferred if backward compatibility not an issue.
  3. Convert name to canonical sequence of octets; namespace ID in network byte order.
  4. Compute hash of namespace ID concatenated with name.
  5. Set UUID fields from hash octets:
     - time_low = octets 0-3
     - time_mid = octets 4-5
     - time_hi_and_version = octets 6-7 (zero out top 4 bits, then set version)
     - clock_seq_hi_and_reserved = octet 8 (set top 2 bits to 0 and 1)
     - clock_seq_low = octet 9
     - node = octets 10-15
  6. Convert to local byte order.

### 4.4 Algorithm for Creating a UUID from Truly Random or Pseudo-Random Numbers (Version 4)
- Set 2 most significant bits of clock_seq_hi_and_reserved to 0 and 1.
- Set 4 most significant bits of time_hi_and_version to version number (0100).
- Set all other bits to randomly (or pseudo-randomly) chosen values.

### 4.5 Node IDs that Do Not Identify the Host
- If IEEE 802 address unavailable or undesired:
  - Obtain separate block from IEEE (cost ~US$550 at time of writing).
  - Better: generate 47-bit cryptographic-quality random number, set least significant bit of first octet of node ID to 1 (multicast bit). This ensures no conflict with network card addresses.
- Use unicast/multicast bit (not local/global) for compatibility.
- Additional sources: computer name, OS name, etc.; accumulate into buffer, hash with MD5 or SHA-1, take 6 bytes, set multicast bit.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Clock sequence **MUST** be originally initialized to a random number. | MUST | Section 4.1.5 |
| R2 | Initial clock sequence value **MUST NOT** be correlated to the node identifier. | MUST | Section 4.1.5 |
| R3 | UUID service **MUST** return an error or stall if system clock resolution insufficient and overrun occurs. | MUST | Section 4.2.1.2 |
| R4 | Same name in same namespace MUST produce equal UUIDs (version 3/5). | MUST | Section 4.3 |
| R5 | For non-IEEE address, multicast bit must be set in node ID. | MUST | Section 4.1.6 |
| R6 | Version 4: Set variant bits as specified (clock_seq_hi_and_reserved top 2 bits to 0,1). | MUST | Section 4.4 |
| R7 | Version 4: Set version bits as specified (time_hi_and_version top 4 bits to 0100). | MUST | Section 4.4 |
| R8 | Nil UUID: all 128 bits set to zero. | MUST | Section 4.1.7 |
| R9 | UUID string representation lower-case hexadecimal recommended (case insensitive on input). | SHOULD | Section 3 (ABNF) |
| R10 | For name-based UUIDs, SHA-1 is preferred if backward compatibility not an issue. | SHOULD | Section 4.3 |
| R11 | Systems without UTC may use local time consistently (not recommended). | MAY | Section 4.1.4 |

## Informative Annexes (Condensed)
- **Appendix A – Sample Implementation**: Provides C source code (uuid.h, uuid.c, sysdep.h, sysdep.c, utest.c) demonstrating the UUID generation algorithms with optimizations (excluding efficient state sharing across processes). Assumes 64-bit integer support.
- **Appendix B – Sample Output of utest**: Shows example output from the test program, verifying basic UUID creation and comparison.
- **Appendix C – Some Name Space IDs**: Provides pre-defined namespace UUIDs for DNS, URL, OID, and X.500 name spaces as C structures and string representations.