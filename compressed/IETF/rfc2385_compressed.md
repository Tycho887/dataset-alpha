# RFC 2385: Protection of BGP Sessions via the TCP MD5 Signature Option
**Source**: IETF – Standards Track | **Version**: August 1998 | **Date**: August 1998 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc2385  

## IESG Note (Summary)
This document describes current practice for securing BGP against simple attacks but is understood to have security weaknesses against concerted attacks.

## Abstract (Condensed)
Defines a TCP option (Kind=19) carrying an MD5 digest to protect BGP sessions against spoofed TCP segments, especially resets. The digest uses a secret key known only to endpoints; there is no negotiation for the option. This significantly reduces certain security risks but is not a complete solution.

## Scope (Summary)
Specifies a TCP extension for enhancing BGP security by adding an MD5 signature option to every segment of a protected connection. Covers digest computation, validation, and implications for TCP operations.

## Normative References
- [RFC1321] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
- [RFC1323] Jacobson, V., Braden, R., and D. Borman, "TCP Extensions for High Performance", RFC 1323, May 1992.
- [Dobb] H. Dobbertin, "The Status of MD5 After a Recent Attack", RSA Labs' CryptoBytes, Vol. 2 No. 2, Summer 1996.  

## Definitions and Abbreviations
- **MD5 digest**: 16-byte cryptographic hash computed as specified in Section 2.0.
- **Key**: Independently specified secret known to both TCPs, presumably connection-specific; nature deliberately unspecified.
- **Signed segment**: TCP segment containing the option with valid MD5 digest.
- **TCP pseudo-header**: For digest calculation: source IP, destination IP, zero-padded protocol number, segment length (network byte order).

## Sections

### 1.0 Introduction
Primary motivation is to protect BGP against spoofed TCP segments (particularly resets). An attacker must guess both TCP sequence numbers and the secret key (never transmitted). Use of the option is a matter of site policy; no negotiation occurs.

### 2.0 Proposal
- **Requirement 2.1 (shall)**: Every segment sent on a TCP connection protected against spoofing shall contain the 16-byte MD5 digest produced by applying MD5 to the following items in order:
  1. TCP pseudo-header (source IP, destination IP, zero-padded protocol number, segment length)
  2. TCP header excluding options, with checksum assumed zero
  3. TCP segment data (if any)
  4. An independently-specified key known to both TCPs.
- **Requirement 2.2 (must)**: Upon receiving a signed segment, the receiver must validate it by computing its own digest (using its own key) and comparing. A failing comparison must result in the segment being dropped and must not produce any response back to the sender. Logging the failure is advisable.
- **Requirement 2.3 (must)**: Unlike other TCP extensions, the absence of the option in the SYN/ACK segment must not cause the sender to disable sending signatures. Sending signatures must be under the complete control of the application.

### 3.0 Syntax
The option format:
```
+---------+---------+-------------------+
| Kind=19 |Length=18|   MD5 digest...   |
+---------+---------+-------------------+
```
- MD5 digest is always 16 bytes; the option appears in every segment of a connection.

### 4.0 Some Implications
- **4.1 (informative)**: Connectionless resets will be ignored because the sender lacks the key. This causes timeouts instead of immediate resets, potentially delaying BGP recovery from peer crashes.
- **4.2 (informative)**: Performance measurements: on a 100 MHz R4600, signature generation took ~0.0268 ms for ACK segments, ~0.8776 ms for 4096-byte data segments (input path also compares 16 bytes).
- **4.3 (informative)**: Option increases TCP header size by 18 bytes; MSS reduction must account for this. Total header size (incl. options) must remain ≤60 bytes. Example with 4.4BSD defaults shows SYN packet uses exactly 40 bytes.
- **4.4 (informative)**: MD5 is considered weak against collision attacks, but the option remains specified because it is already deployed. No algorithm type field was defined. Deployment of a similar option with another hash (e.g., SHA-1) is not prevented; a new option would need definition in another document.
- **4.5 (strongly recommended)**: An implementation must be able to support at minimum a key composed of a string of printable ASCII of 80 bytes or less (current practice).

### 5.0 Security Considerations
This document defines a weak but currently practiced security mechanism for BGP. It is anticipated that future work will provide stronger mechanisms.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Every segment sent on a TCP connection protected against spoofing shall contain the 16-byte MD5 digest computed per Section 2.0. | shall | Sec. 2.0 |
| R2 | Upon receiving a signed segment, the receiver must validate it by computing its own digest and comparing. Failing comparison must result in segment being dropped and must not produce any response. | must | Sec. 2.0 |
| R3 | Absence of the option in SYN/ACK must not disable sending signatures; sending signatures must be under complete control of the application. | must | Sec. 2.0 |
| R4 | Implementation must support at minimum a key of printable ASCII of 80 bytes or less. | must (strongly recommended) | Sec. 4.5 |

## Informative Annexes (Condensed)
- **Performance Measurements (Section 4.2)**: Provides sample implementation timings to illustrate computational cost.
- **TCP Header Size Example (Section 4.3)**: Illustrates that with typical options (MSS, window scale, timestamps), a SYN packet with MD5 option exactly fills 40 bytes (maximum option space).
- **MD5 Weakness Discussion (Section 4.4)**: Notes MD5 vulnerability to collision attacks; option was defined without an algorithm type field due to option space constraints. Deployment of an alternative using a different hash is possible but would require a new option number.