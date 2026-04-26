# RFC 4301: Security Architecture for the Internet Protocol
**Source**: IETF | **Version**: Standards Track | **Date**: December 2005 | **Type**: Normative  
**Original**: [RFC 4301 text](https://datatracker.ietf.org/doc/rfc4301/)

## Scope (Summary)
This document specifies the base architecture for IPsec-compliant systems, providing security services (access control, integrity, authentication, anti-replay, confidentiality, limited traffic flow confidentiality) at the IP layer for IPv4 and IPv6. It obsoletes RFC 2401.

## Normative References (Key)
- **RFC 2119**: Key words for requirement levels (MUST, SHOULD, etc.)
- **RFC 791**: Internet Protocol (IPv4)
- **RFC 2460**: Internet Protocol, Version 6 (IPv6)
- **RFC 4302**: IP Authentication Header (AH)
- **RFC 4303**: IP Encapsulating Security Payload (ESP)
- **RFC 4305**: Cryptographic Algorithm Implementation Requirements for ESP and AH
- **RFC 4306**: Internet Key Exchange (IKEv2)
- **RFC 4307**: Cryptographic Algorithms for IKEv2
- **RFC 2474**: Definition of the Differentiated Services Field (DS Field)
- **RFC 3168**: Explicit Congestion Notification (ECN)
- **RFC 1191**: Path MTU Discovery
- **RFC 2003**: IP Encapsulation within IP
- **RFC 3740**: Multicast Group Security Architecture

## Definitions and Abbreviations (Key)
- **Access Control**: Prevents unauthorized use of a resource.
- **Anti-replay**: Partial sequence integrity; detects duplicate datagrams within a window.
- **Authentication**: Data origin authentication and connectionless integrity.
- **Confidentiality**: Protects data from unauthorized disclosure; ESP provides this.
- **Data Origin Authentication**: Verifies the identity of the claimed source.
- **Encryption**: Transforms plaintext to ciphertext for confidentiality.
- **Integrity**: Detection of modifications; connectionless and anti-replay forms.
- **Protected/Unprotected**: Inside/outside the IPsec protection boundary.
- **Security Association (SA)**: Simplex logical connection providing security services; identified by SPI.
- **Security Gateway (SG)**: Intermediate system implementing IPsec (e.g., IPsec-enabled firewall/router).
- **Security Parameters Index (SPI)**: 32-bit value identifying an SA; carried in AH/ESP headers.
- **SPD, SAD, PAD**: Security Policy Database, Security Association Database, Peer Authorization Database.
- **BITS/BITW**: Bump-in-the-stack / Bump-in-the-wire implementations.

## 1. Introduction
### 1.1 Summary
This document specifies architecture for IPsec-compliant systems, covering AH, ESP, SAs, key management, and cryptographic algorithms. Security services are provided at the IP layer.

### 1.2 Audience
Implementers and technically adept users; assumes familiarity with IP and security concepts.

### 1.3 Related Documents
- Security protocols: AH [Ken05b], ESP [Ken05a]
- Cryptographic algorithms: [Eas05], [Sch05]
- Key management: IKEv2 [Kau05]

## 2. Design Objectives
### 2.1 Goals/Requirements
- Provide interoperable, high-quality cryptographic security for IPv4/IPv6.
- Services: access control, connectionless integrity, data origin authentication, anti-replay, confidentiality, limited traffic flow confidentiality.
- Includes minimal firewall functionality at IP layer.
- Protocol and algorithm independent.
- Default algorithms specified in separate documents.

### 2.2 Caveats and Assumptions
- Security depends on implementation quality, system environment, and operational practices – outside scope of this standard.

## 3. System Overview
### 3.1 What IPsec Does
- Creates a boundary between unprotected and protected interfaces.
- Traffic can be PROTECTED (AH/ESP), DISCARDed, or BYPASSed.
- Supports protection between host pairs, SG pairs, or host-SG.

### 3.2 How IPsec Works
- **AH**: Integrity and data origin authentication, optional anti-replay.
- **ESP**: Same plus confidentiality. **NOT RECOMMENDED** to use ESP with confidentiality without integrity.
- Both support transport and tunnel modes.
- Mode usage: transport for next layer protocols; tunnel for IP tunnels.
- SPD determines granularity and processing.

### 3.3 Where IPsec Can Be Implemented
- **Native IP stack**, **BITS** (between IP and network drivers), **BITW** (dedicated inline processor).
- Hosts: MUST support both modes. SGs: MUST support tunnel mode, MAY support transport mode.

## 4. Security Associations
### 4.1 Definition and Scope
- SA is simplex; bi-directional communication requires a pair.
- **MUST** support SA concept.
- For unicast: SPI suffices; for multicast: MUST use SPI plus dest (and source) address for demuxing.
- Inbound SAD search order: (1) SPI+dest+src, (2) SPI+dest, (3) SPI (+protocol). Externally visible behavior MUST be functionally equivalent.
- **SHOULD** put different DSCP traffic on different SAs to support QoS.
- **MUST** permit multiple SAs with same selectors between sender and receiver.
- Transport mode: typically between hosts; may be used between SGs or SG-host for in-IP tunneling, but access control is limited.
- Tunnel mode: required when either end is an SG (except management traffic).
- **MUST NOT** use transport mode for fragments (IPv4/IPv6).

### 4.2 SA Functionality
- Services depend on protocol, mode, endpoints, and optional services.
- **MUST NOT** instantiate ESP SA using both NULL encryption and no integrity algorithm (auditable event).

### 4.3 Combining SAs (Nested SAs)
- Support for nested SAs is optional; can be achieved via SPD and forwarding configuration.
- Implementations that support nested SAs **SHOULD** provide a management interface for nesting.

### 4.4 Major IPsec Databases
#### 4.4.1 Security Policy Database (SPD)
- **MUST** have at least one SPD; may support multiple SPDs with explicit SPD selection function.
- Ordered database; entries can overlap.
- Processing choices: **DISCARD, BYPASS, PROTECT**.
- Logically divided into SPD-S (secure), SPD-O (outbound bypass/discard), SPD-I (inbound bypass/discard).
- Each entry keyed by selectors: Remote/Local IP addresses (ranges), Next Layer Protocol, Local/Remote Ports (or ICMP type/code, MH type), and optionally Name.
- Special selector values: **ANY** (wildcard), **OPAQUE** (field not available).
- PFP flag (Populate From Packet): determines if SA selector values come from packet or SPD entry.
- **MUST** provide management interface for ordering and specifying all selectors.
- **MUST** support Name selector for responder (e.g., DNS, email, DN) and optionally for initiator.
- For ICMP: selector is 16-bit (type*256+code). For MH: 8-bit type placed in upper 8 bits of port selector.
- Decorrelation can be used for caching (not required).

#### 4.4.2 Security Association Database (SAD)
- Each SA has an SAD entry; for inbound, SPI (or SPI+addresses) is key.
- **MUST** contain: SPI, Sequence Number Counter (64-bit default, 32-bit allowed), Sequence Counter Overflow flag, Anti-Replay Window (64-bit counter+bitmap), AH Auth algorithm/key, ESP Encryption algorithm/key, ESP Integrity algorithm/key, ESP Combined mode algorithm/key, SA Lifetime (time/byte count, both MUST be supported), IPsec protocol mode, Bypass DF bit (for tunnel), DSCP values, Bypass DSCP mapping, Path MTU, Tunnel header addresses.

#### 4.4.3 Peer Authorization Database (PAD)
- Provides link between SA management (IKE) and SPD.
- **MUST** support six ID types: DNS name (exact or subtree), Distinguished Name (complete or subtree), RFC 822 email (complete or subtree), IPv4/IPv6 address (range), Key ID (exact match).
- **MUST** support authentication methods: X.509 certificate and pre-shared secret.
- For certificate-based auth, contains trust anchor and revocation data.
- Must provide means to require match between IKE ID and certificate subject/alt name.
- Used during IKE initial exchange to locate entry, verify identity, and then constrain child SA creation.

### 4.5 SA and Key Management
- **MUST** support both manual and automated key management.
- Default automated protocol: IKEv2 [Kau05].
- If multiple keys derived from a single string, encryption keys **MUST** be taken from first (high-order) bits; integrity keys from remaining bits.

### 4.6 SAs and Multicast
- For multicast: SPI assigned by group controller; **MUST** de-multiplex correctly even with SPI collisions.
- Multiple senders to multicast group **SHOULD** use a single SA (symmetric key).

## 5. IP Traffic Processing
### 5.1 Outbound Traffic
- **MUST** invoke SPD selection function, match against cache (SPD-O and SPD-S), then process.
- If cache miss, search SPD; create SA if needed via IKEv2.
- If DISCARD, **SHOULD** send ICMP type 3/code 13 (IPv4) or type 1/code 1 (IPv6) with administrator control to prevent DoS.
- For nested SAs: packet may be looped back; must have SPD-I bypass entry.

### 5.2 Inbound Traffic
- Reassemble fragments before IPsec processing.
- Demux: if protected and addressed to device, look up SAD; else SPD-I.
- If IPsec packet has no matching SAD entry, **MUST** discard (auditable event).
- After AH/ESP processing, match packet against inbound selectors in SAD; if mismatch, **MUST** discard and **SHOULD** send IKE notification INVALID_SELECTORS (rate-limited).

## 6. ICMP Processing
- Applies to error messages only; non-error ICMP must be handled by SPD entries.
- **MUST** allow administrator to accept/reject unauthenticated ICMP at type granularity.
- For transit ICMP errors: **MUST** be configurable to check payload header consistency with SA selectors.
- If no matching SA/SPD for outbound ICMP error, **MUST** map to SA carrying the triggering packet's return traffic.

## 7. Handling Fragments (Protected Side)
- Three approaches (MUST/MAY):
  1. **MUST** support tunnel mode SAs configured with port/ICMP/MH selectors as ANY (carries all fragments).
  2. **MAY** support separate tunnel mode SAs for non-initial fragments using OPAQUE selectors; receivers **MUST** perform minimum offset check for IPv4.
  3. **MAY** support stateful fragment checking; senders **MUST** notify peer via NON_FIRST_FRAGMENTS_ALSO NOTIFY.
- For BYPASS/DISCARD traffic: **MUST** support stateful fragment checking when non-trivial port ranges are specified.

## 8. Path MTU/DF Processing
### 8.1 DF Bit
- **MUST** support option to copy DF bit from inner to outer tunnel header (set, clear, copy).

### 8.2 Path MTU Discovery
- When processing ICMP PMTU: update SAD PMTU field.
- For outbound traffic exceeding PMTU:
  - IPv4 with DF set: **SHOULD** discard and send PMTU ICMP.
  - IPv4 with DF clear: **SHOULD** fragment (before or after encryption) and forward.
  - IPv6: **SHOULD** discard and send PMTU ICMP.
- **MUST** age PMTU; **SHOULD** use approach from RFC 1191 Section 6.3 (periodically reset to first-hop MTU); period **SHOULD** be configurable.

## 9. Auditing
- Auditing not required, but specified events must have defined minimum info.
- Events: SA setup failure, invalid selectors, packet discards, etc.

## 10. Conformance Requirements
- All IPv4 and IPv6 implementations **MUST** comply with all requirements of this document.

## 11. Security Considerations (Summary)
- Covert channel concerns: DSCP/ECN propagation, ICMP error checking, fragment handling.
- ICMP error messages on SAs without payload checking can enable DoS attacks.

## 12. IANA Considerations
- IANA assigned OID 1.3.6.1.5.8.3.1 for SPD ASN.1 module.

## 13. Differences from RFC 2401
- Revised processing model: separation of forwarding and security, addition of SPD cache, PAD.
- No mandatory support for nested SAs/SA bundles.
- SPD entries redefined: list of ranges for selectors, multiple selector sets.
- DSCP/ECN replaces TOS/Traffic Class.
- Transport mode now allowed between SGs and SG-host.
- All traffic (including IKE) MUST consult SPD.
- AH support downgraded to MAY.
- Fragment handling: three approaches defined.
- Names selector clarified.
- ICMP message type/code and Mobility Header type added as selectors.
- “Local” and “Remote” used for policy rules.

## 14. Acknowledgements
- Contributions from Ran Atkinson, Charlie Lynn (memory), IPsec and MSEC working groups.

## Informative Annexes (Condensed)
- **Appendix A (Glossary)**: Key terms (SA, SPI, Security Gateway, etc.) – definitions preserved in main document.
- **Appendix B (Decorrelation)**: Algorithm to convert correlated SPD entries into a set of decorelated entries for caching; includes mathematical description and optimization suggestions. Not required but useful for performance.
- **Appendix C (ASN.1 for SPD Entry)**: Informative ASN.1 definition of SPD entry structure, consistent with normative text in Section 4.4.1.
- **Appendix D (Fragment Handling Rationale)**: Explains problems with non-initial fragments and justifies the three approaches: (1) ANY selectors, (2) OPAQUE selectors with offset check, (3) stateful fragment checking. Concludes no one-size-fits-all solution.
- **Appendix E (Example of Nested SAs)**: Shows how to configure SPD and forwarding tables to support transport mode SA over tunnel mode SA (A to C over A to B).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All IPsec implementations MUST support the concept of an SA. | MUST | §4.1 |
| R2 | Unicast SA: SPI suffices; multicast: MUST use SPI plus dest/src address for demux. | MUST | §4.1 |
| R3 | Implementations MUST permit multiple SAs with same selectors between sender and receiver. | MUST | §4.1 |
| R4 | Transport mode MUST NOT be used for fragments. | MUST | §4.1 |
| R5 | Security gateway MUST support tunnel mode; MAY support transport mode when acting as host. | MUST/MAY | §4.1 |
| R6 | MUST NOT instantiate ESP SA with NULL encryption and no integrity (auditable event). | MUST NOT | §4.2 |
| R7 | MUST have at least one SPD; MUST consult SPD for all traffic crossing IPsec boundary. | MUST | §4.4.1 |
| R8 | SPD MUST support DISCARD, BYPASS, PROTECT actions. | MUST | §4.4.1 |
| R9 | SPD MUST support selectors: Remote/Local IP (ranges), Next Layer Protocol, ports (or ICMP type/code, MH type), Name. | MUST | §4.4.1.1 |
| R10 | MUST support OPAQUE and ANY selector values. | MUST | §4.4.1.1 |
| R11 | MUST support PFP flag for each traffic selector. | MUST | §4.4.1.2 |
| R12 | SAD MUST contain SPI, Sequence Number Counter, overflow flag, anti-replay window, algorithms, lifetime, mode, etc. | MUST | §4.4.2.1 |
| R13 | SAD lifetime MUST support time and byte count, both simultaneously. | MUST | §4.4.2.1 |
| R14 | PAD MUST support 6 ID types (DNS, DN, email, IPv4/IPv6 range, Key ID). | MUST | §4.4.3.1 |
| R15 | PAD MUST support authentication using X.509 certificates and pre-shared secrets. | MUST | §4.4.3.2 |
| R16 | Implementations MUST support both manual and automated SA/key management. | MUST | §4.5 |
| R17 | If multiple keys from one string, encryption keys MUST be taken from first bits; integrity keys from remaining. | MUST | §4.5.2 |
| R18 | Outbound packet matched to no SPD entry MUST be discarded. | MUST | §5 |
| R19 | Inbound IPsec packet with no SAD match MUST be discarded (auditable). | MUST | §5.2 |
| R20 | Received packet inconsistent with SA selectors MUST be discarded; SHOULD send INVALID_SELECTORS notification. | MUST/SHOULD | §5.2 |
| R21 | ICMP error messages: MUST allow admin to configure acceptance; MUST check payload consistency for transit ICMP errors when configured. | MUST | §6.2 |
| R22 | Outbound ICMP error without matching SA: MUST map to SA of triggering packet's return traffic. | MUST | §6.2 |
| R23 | MUST support tunnel mode SAs with ANY port/ICMP/MH selectors to carry all fragments. | MUST | §7.1 |
| R24 | MAY support separate tunnel mode SAs for non-initial fragments using OPAQUE; receivers MUST check minimum offset for IPv4. | MAY/MUST | §7.2 |
| R25 | MAY support stateful fragment checking; if used, MUST notify peer via IKE NOTIFY. | MAY/MUST | §7.3 |
| R26 | BYPASS/DISCARD traffic MUST support stateful fragment checking when non-trivial port ranges specified. | MUST | §7.4 |
| R27 | MUST support option to copy DF bit to tunnel header (set, clear, copy). | MUST | §8.1 |
| R28 | MUST age PMTU of SA; SHOULD use approach from RFC 1191 Section 6.3. | MUST/SHOULD | §8.2.2 |
| R29 | All IPv4 and IPv6 implementations MUST comply with all requirements of this document. | MUST | §10 |