# RFC 4732: Internet Denial-of-Service Considerations
**Source**: IETF | **Version**: November 2006 | **Date**: November 2006 | **Type**: Informational
**Status**: This memo provides information for the Internet community. It does not specify an Internet standard of any kind.

## Scope (Summary)
This document provides an overview of possible avenues for denial-of-service (DoS) attack on Internet systems, aiming to encourage protocol designers and network engineers towards more robust designs. It discusses partial solutions that reduce attack effectiveness and highlights how some solutions may inadvertently open alternative vulnerabilities.

## Normative References
- [1] J. Abley, "Hierarchical Anycast for Global Service Distribution" (ISC)
- [2] D.J. Bernstein, "SYN Cookies"
- [3] Chen, E., "Route Refresh Capability for BGP-4", RFC 2918, September 2000
- [4] Deering, S., "Host extensions for IP multicasting", STD 5, RFC 1112, August 1989
- [5] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.1", RFC 4346, April 2006
- [6] Fenner, B. et al., "Protocol Independent Multicast - Sparse Mode (PIM-SM): Protocol Specification (Revised)", RFC 4601, August 2006
- [7] Ferguson, P. and D. Senie, "Network Ingress Filtering: Defeating Denial of Service Attacks which employ IP Source Address Spoofing", BCP 38, RFC 2827, May 2000
- [8] Gill, V., Heasley, J., and D. Meyer, "The Generalized TTL Security Mechanism (GTSM)", RFC 3682, February 2004
- [9] Heffernan, A., "Protection of BGP Sessions via the TCP MD5 Signature Option", RFC 2385, August 1998
- [10] Rekhter, Y., Li, T., and S. Hares, "A Border Gateway Protocol 4 (BGP-4)", RFC 4271, January 2006
- [11] Villamizar, C., Chandra, R., and R. Govindan, "BGP Route Flap Damping", RFC 2439, November 1998
- [12] Waitzman, D., Partridge, C., and S. Deering, "Distance Vector Multicast Routing Protocol", RFC 1075, November 1988
- [13] L. von Ahn et al., "CAPTCHA: Using hard AI problems for security" (Eurocrypt, 2003)

## Definitions and Abbreviations
- **Denial-of-Service (DoS) attack**: An attack in which one or more machines target a victim and attempt to prevent the victim from doing useful work. Victim may be a network server, client, router, link, entire network, user, ISP, country, etc.
- **Distributed Denial-of-Service (DDoS) attack**: A DoS attack perpetrated from multiple compromised hosts.
- **Flash crowd**: Unexpected heavy but non-malicious traffic having the same effect as a DoS attack.
- **Livelock**: State where after saturation, increasing load causes a decrease in useful work done.
- **SYN flood**: A memory-exhaustion attack exploiting TCP connection setup.
- **Smurf attack**: Sending ICMP echo request with spoofed victim source address to subnet-broadcast address, causing many responses to victim.

## 1. Introduction
- **Purpose**: Highlight attack avenues, encourage robust design, discuss partial solutions, and show how solutions may be exploited for alternative attacks.
- **Key observation**: In principle, it is not possible to distinguish between a sufficiently subtle DoS attack and a flash crowd. Defending against DoS raises the bar for malicious traffic, not prevent all attacks.
- **Not all DoS problems are malicious**: Failed links, flash crowds, misconfigured bots also cause resource exhaustion; overall goal is robustness to all forms of overload.

## 2. Overview of Denial-of-Service Threats
### 2.1 DoS Attacks on End-Systems
#### 2.1.1 Exploiting Poor Software Quality
- Simplest DoS: cause software to crash via buffer-overflow, etc. Example: "ping of death" (fragmented ICMP echo request exceeding 65535 bytes) caused OS crashes. Patching resolves such issues.

#### 2.1.2 Application Resource Exhaustion
- Finite resources: memory, CPU, disk space, processes/threads, max simultaneous connections.
- Some resources self-renew (CPU), others require explicit action (disk space).
- Configuration limits: must be chosen appropriately – too low makes attacker's job easier; too high may cause crash or livelock.

#### 2.1.3 Operating System Resource Exhaustion
- SYN flood: attacker floods TCP SYN packets without completing handshake, exhausting memory for half-open connections.
- Ack flood: CPU exhaustion via packets pretending to be from non-existent connections.
- **Strong authentication mechanisms do not necessarily mitigate CPU exhaustion**; poorly designed crypto authentication can exacerbate by requiring expensive verification before discarding.
- OS should be designed to avoid livelock: as incoming traffic increases, useful work increases to saturation, then should be constant. Not decreasing.

#### 2.1.4 Triggered Lockouts and Quota Exhaustion
- Authentication lockout: attacker can trigger lockout after few failed attempts, blocking legitimate user.
- Quota exhaustion: e.g., small web server hosted with daily traffic limit; attacker can exhaust quota causing service suspension. Financial denial-of-service also possible if victim charged per traffic.

### 2.2 DoS Attacks on Routers
- Many end-system attacks apply to router control processor (e.g., flooding control ports). Consequences: routing failure, routing protocol churn, BGP route flap damping may cause routes to be suppressed.
- DoS on router control processor may also prevent management and diagnosis.

#### 2.2.1 Attacks on Routers through Routing Protocols
- Overload routing table with many routes (memory exhaustion) or routing churn (CPU exhaustion). Route flap damping can worsen: spoofed routes may cause legitimate routes to be damped.
- Announce spoofed desirable route to draw traffic to attacking router where it is discarded.
- Inconsistent routing information can cause traffic loops.
- BGP specification errors (different interpretations) can cause peerings to drop, but can be patched.

#### 2.2.2 IP Multicast-based DoS Attacks
- **Any-Source Multicast (ASM)**: Protocols like PIM-SM, MSDP instantiate routing state when packet sent; attacker can cause multicast routing table explosion (memory exhaustion) and forwarding table thrashing.
- **Source-Specific Multicast (SSM)**: Only receivers can request traffic, so sender-based attacks on routing state not possible. However, receiver can join many groups causing memory exhaustion.
- IPv6: mandatory ICMP responses to multicast destination can be exploited (e.g., unknown Destination Option generates many responses). IPv4 same issue with multicast ICMP Echo Request, but easier to filter.
- General problem: multicast/broadcast request soliciting reply from many nodes.

#### 2.2.3 Attacks on Router Forwarding Engines
- Routers with forwarding cache (only active subset of forwarding table) can be attacked by overloading communication link between control processor and forwarding engine.
- Methods: send to router's IP address (filterable), cause packets to use "slow path" (special handling), thrash forwarding cache, data-triggered events (e.g., PIM-SM).
- Effects: forwarding table desynchronization, traffic drop or looping.
- Attackers can also exhaust ACL resources by triggering IDS responses that auto-install ACL entries.

### 2.3 Attacks on Ongoing Communications
- Disrupt TCP connection by spoofing packets to reset or desynchronize. If attacker can observe connection, easy. If not, may require guessing ports and sequence numbers; some OSes have predictable algorithms.
- Spoofed ICMP source quench can reduce throughput; modern OSes should ignore.
- **Future transport/signaling protocols must avoid similar exploitable mechanisms.**

### 2.4 Attacks Using the Victim's Own Resources
- Example: spoofing source address of victim to a UDP echo server, causing victim to bounce packets with another service (e.g., chargen), overloading victim or network.

### 2.5 DoS Attacks on Local Hosts or Infrastructure
- DHCP: exhaust address pool by spoofing MAC addresses, or respond faster than legitimate server with bad addresses.
- ARP spoofing: respond to ARP requests before victim, preventing traffic from reaching victim.
- Broadcast storms: send unicast IP packets to broadcast MAC address, causing amplification.
- 802.11 wireless: association unprotected; rogue APs can solicit notifications. SSID field provides no defense. Deauthentication/disassociation attacks even with WEP. 802.11w will protect Deauthenticate frames, but Association frame forging remains.
- Beacons cannot be encrypted; discussions focus on authentication, not encryption.

### 2.6 DoS Attacks on Sites through DNS
- Denying access to DNS servers makes site effectively unreachable.
- DNS servers can be attacked like end-systems; authoritative servers must have relaying disabled to avoid state exhaustion.
- Routing attacks can target DNS server routes; co-location with site makes both unavailable. All DNS servers being unavailable may cause email bounce.
- Congestion on links to DNS server denies access.
- External DNS failure can cause email from site to be dropped (e.g., sendmail checks domain existence as anti-spam measure; anti-spam defense opens DoS vulnerability).
- Data corruption attack: attacker spoofs responses to DNS queries with different IDs, competing with legitimate response; probability increased if multiple requests with different IDs.
- Anycast DNS makes spoofing easier; attacker can convince ISP to accept anycast route to fake DNS server.
- Anycast DNS also allows disabling one server while maintaining BGP route, causing failures for clients routed there.

### 2.7 DoS Attacks on Links
- Simplest: send enough non-congestion-controlled traffic to congest link, causing packet loss.
- Effects: routing adjacency drops if routing packets lost; router implementations should prioritize routing packets, but shared medium may still lose them.
- Remote access to router (ssh/SNMP) may be prevented, hindering diagnosis.
- Prioritization of routing packets can itself cause DoS if attacker causes high routing flux.
- Monitoring/report traffic (e.g., SNMP traps) not congestion-controlled; attacker can fill link.
- Physical access to multiple access links can easily bring down link, especially wireless.

### 2.8 DoS Attacks on Firewalls
- Stateless firewalls only vulnerable to processing resource exhaustion.
- Stateful firewalls: excessive state (memory exhaustion) or pathological state structure (e.g., hash table collision causing O(n) lookup) can cause denial-of-service.

### 2.9 DoS Attacks on IDS Systems
- Similar resource exhaustion issues as firewalls. IDS normally fails open but may miss subsequent attacks.
- Reactive IDS: attacker can spoof packets from legitimate system, causing IDS to block that system (denial-of-service).

### 2.10 DoS Attacks on or via NTP
- DoS the NTP servers themselves, causing clock drift; problematic for distributed systems relying on accurate clocks.
- Subvert NTP servers to control system clock, causing premature expiry of encryption/authentication keys.

### 2.11 Physical DoS
- Power failure, cut cables, switching off system. Physical security as important as network security.

### 2.12 Social Engineering DoS
- Convincing employee to make configuration changes that prevent normal operation.

### 2.13 Legal DoS
- "Cease and desist" letters, government censorship, etc., touch on denial-of-service issues.

### 2.14 Spam and Black-Hole Lists
- Spam causes denial-of-service to email systems (waste time, legitimate email lost). Spam filtering yields false positives.
- Black-hole lists: possible for attacker to cause victim to be listed even if not relaying spam. Policy on additions varies; consumers should investigate policies before subscribing.

## 3. Attack Amplifiers
### 3.1 Methods of Attack Amplification
- **Smurf attack**: ICMP echo request to subnet-broadcast with spoofed victim source address (now mitigated by router dropping and end-systems not responding).
- **DNS reflection attack**: DNS request with spoofed victim source address; response larger than request. Largest responses often from DNSSEC. Only possible if attacker can spoof source address. If victim's DNS server relays external requests, it may congest its own link.
- **TCP amplification (bang.c)**: Spoofed TCP SYN to arbitrary server; server sends SYN|ACK to victim; retransmissions if no RST or firewall drops RST.
- **Protocols with payload IP address/name for subsequent messages** (e.g., SIP with SDP): attacker sets payload IP to victim; recipient generates traffic to victim. This does not require source spoofing. Example: "voice hammer" – single SIP INVITE causes continuous media stream.
- **Prevention**: Protocols should avoid including IP addresses/hostnames in payload for subsequent messaging; if unavoidable, include handshake to verify destination wishes to receive, with lightweight anti-spoofing.
- **Protocols where one message leads to another not sent as reply to source** (e.g., mobility protocols) can permit attacker to avoid ingress filtering.

### 3.2 Strategies to Mitigate Attack Amplification
1. Perform ingress filtering [7][39] to prevent source address spoofing.
2. Avoid protocols/mechanisms returning significantly larger responses than request size unless handshake validates client source address (with unpredictable nonce).
3. All retransmission during initial connection setup should be performed by the client.
4. Proxies should not arbitrarily relay requests to destinations chosen by a client.
5. Avoid signaling third-party connections; any unavoidable third-party connections should incorporate lightweight validation before sending significant data.

## 4. DoS Mitigation Strategies
### 4.1 Protocol Design
#### 4.1.1 Don't Hold State for Unverified Hosts
- Avoid instantiating state without handshake to validate client address. Push work/state to client. Techniques like SYN cookies [2] should be designed into protocols; enabling at server's discretion.

#### 4.1.2 Make It Hard to Simulate a Legitimate User
- Use puzzles, reverse Turing tests (CAPTCHA), reachability testing to discriminate attackers.
- **Limitations**: Puzzles discriminate against slow computers; bots provide ample computing power. Reverse Turing tests are vulnerable to automated attacks. Reachability testing weakened by bots that do not need to hide source address.

#### 4.1.3 Graceful Routing Degradation
- Routing protocols should degrade gracefully under overload and recover automatically. Example: RIP can drop routes and send infinite metric; BGP is stateful and lacks refresh mechanism (route refresh option hard to use under overload). BGP router that cannot store received route must restart or shut down peerings, amplifying attacks.
- **Future routing protocol designs should explicitly consider behavior under overload.**

#### 4.1.4 Autoconfiguration and Authentication
- Unauthenticated autoconfiguration opens attack avenues. Tension between ease of configuration and security. Future autoconfiguration protocols should allow different end-systems to operate at different points in the spectrum within same framework. Network elements should avoid acting for unauthenticated hosts.

### 4.2 Network Design and Configuration
- Provision private, out-of-band access to console/control ports for management under DoS. Out-of-band is crucial as redundancy/prioritization may fail.
- Disable default configurations that can be exploited: IP redirect, directed broadcast, proxy ARP. Avoid publicly readable SNMP communities (e.g., "public"). Avoid unauthenticated TFTP; protect TFTP archives. Router password encryption often reversible; avoid storing encrypted passwords in archives.

#### 4.2.1 Redundancy and Distributed Service
- Use redundant servers and distribute service delivery points across network to make attacks on single link/server more difficult.

#### 4.2.2 Authenticate Routing Adjacencies
- Use cryptographic authentication (TCP MD5 [9] or IPsec) combined with GTSM [8] for BGP. Future: better authentication of routing information itself.

#### 4.2.3 Isolate Router-to-Router Traffic
- Isolate routing traffic from data traffic as feasible. Goal: failure of data link should also fail routing traffic, but attacker cannot directly send packets to control processor. Downside: diagnostic techniques like pinging may be lost; alternative mechanisms should be designed.

### 4.3 Router Implementation Issues
#### 4.3.1 Checking Protocol Syntax and Semantics
- Verify sender (source IP, MAC, TTL check [8]), content conformance to protocol, correct timing. Use cryptographic authentication where available (TCP MD5 or IPsec). Perform rigorous syntax checking to prevent crashes from ill-formed messages.

#### 4.3.2 Consistency Checks
- e.g., When router A withdraws prefix P, B should ensure alternative path does not go through A (improves BGP convergence).
- "Allowed origin list" test: attach list of valid origin ASes to route announcement; remote ASes can detect false updates by comparing origin AS lists from multiple paths.
- Policies do not change often; verify new updates against recent past routes. Combination of techniques reduces probability of undetected faults.

#### 4.3.3 Enhance Router Robustness through Operational Adjustments
- Coordinate limit on number of prefixes a BGP speaker will send to peer [43] (careful with hard limits to avoid black-holing).
- Adjust BGP KeepAlive/Hold Timer values to minimize peering session resets under heavy load (e.g., worm traffic).

#### 4.3.4 Proper Handling of Router Resource Exhaustion
- ARP cache exhaustion: under virus attack, many packets to non-existing IP addresses cause no ARP replies; routers may fail to forward. Implement protection.
- Queue management: high-end routers with specialized processors may be vulnerable to low-effort DoS saturating queues between ASIC and supporting CPU. Countermeasure: multiple queues designed to prevent attacker from filling multiple queues [45].

### 4.4 End-System Implementation Issues
#### 4.4.1 State Lookup Complexity
- Use hash tables with keyed hash mechanisms so attacker cannot control hash bucket distribution.

##### 4.4.1.1 Avoid Livelock
- Under heavy load, use network polling instead of interrupt-driven receive. Architecture: traffic processed to completion or cheaply discarded.

##### 4.4.1.2 Use Unpredictable Values for Session IDs
- Dynamically allocated session identifiers (TCP initial sequence numbers, ports, DNS IDs) should be unpredictable to increase attack search space. DNS ID field only 16 bits, limited protection.

#### 4.4.2 Operational Issues
##### 4.4.2.1 Eliminate Bad Traffic Early
- Filter attacks near attacker before they traverse scarce link to victim. Perform ingress filtering [7].

##### 4.4.2.2 Establish a Monitoring Framework
- Set baseline of "normal" traffic, detect aberrant flows, determine type and source. Essential for responding to DDoS or flash crowd; should be in place prior to event.

## 5. Conclusions
- This document highlights DoS attack avenues to encourage robust design, discusses partial solutions, and shows how solutions may be exploited.
- Focus on protocol and network architecture; network/service operators can also lessen threat (advice in [24][39][25]).
- Hope to spur discussion leading to architectural solutions reducing susceptibility of all Internet systems to DoS.

## 6. Security Considerations
- This entire document is about security.

## 7. Acknowledgements
- Thanks to Vern Paxson, Paul Vixie, Rob Thomas, Dug Song, George Jones, Jari Arkko, Geoff Huston, and Barry Greene.

## Normative References (Listed above in Normative References section)

## Informative References (Condensed)
- [14] Aura et al., "DOS-resistant authentication with client puzzles" (Security Protocols Workshop, 2000)
- [15] Bellardo & Savage, "802.11 Denial-of-Service Attacks: Real Vulnerabilities and Practical Solutions" (USENIX Security, 2003)
- [16] Bellovin, "Security Problems in the TCP/IP Protocol Suite" (CCR, 1989)
- [17] CCAIS/RNP, "Vulnerability in the sending requests control of Bind versions 4 and 8 allows DNS spoofing"
- [18] CERT Advisory CA-1996-01, "UDP Port Denial-of-Service Attack"
- [19] CERT Advisory CA-1996-21, "TCP SYN Flooding and IP Spoofing Attacks"
- [20] CERT Advisory CA-2001-09, "Statistical Weaknesses in TCP/IP Initial Sequence Numbers"
- [21] CERT Advisory CA-1996-26, "Denial-of-Service Attack via ping"
- [22] CERT Advisory CA-1998-01, "Smurf IP Denial-of-Service Attacks"
- [23] CERT Incident Note IN-2000-05, "'mstream' Distributed Denial of Service Tool"
- [24] CERT/CC, "Managing the Threat of Denial of Service Attacks"
- [25] CERT/CC, "Trends in Denial of Service Attack Technology"
- [26] Chang et al., "An Empirical Study of Router Response to Large Routing Table Load" (IMW 2002)
- [27] Cisco Systems, "Configuring the BGP Maximum-Prefix Feature"
- [28] Crosby & Wallach, "Denial of Service via Algorithmic Complexity Attacks" (USENIX Security, 2003)
- [29] Joncheray, "Simple Active Attack Against TCP" (USENIX Security, 1995)
- [30] Lough, "A Taxonomy of Computer Attacks with Applications to Wireless" (PhD thesis, 2001)
- [31] Mao et al., "Route Flap Dampening Exacerbates Internet Routing Convergence" (SIGCOMM, 2002)
- [32] Fenner & Meyer, "Multicast Source Discovery Protocol (MSDP)", RFC 3618, October 2003
- [33] Mogul & Ramakrishnan, "Eliminating Receive Livelock in an Interrupt-driven Kernel" (ACM TOCS, 1997)
- [34] Watson, "Slipping in the Window: TCP Reset attacks" (CanSecWest, 2004)
- [35] Paxson, "An Analysis of Using Reflectors for Distributed Denial-of-Service Attacks" (CCR, 2001)
- [36] Stewart, "DNS Cache Poisoning - The Next Generation"
- [37] Stewart & Dalal, "Improving TCP's Robustness to Blind In-Window Attacks" (Work in Progress, June 2006)
- [38] Vixie et al., "Events of 21-Oct-2002"
- [39] Vixie, "Securing the Edge"
- [40] Wessels, "Running An Authoritative-Only BIND Nameserver"
- [41] Zalewski, "Strange Attractors and TCP/IP Sequence Number Analysis"
- [42] Pei et al., "Improving BGP Convergence Through Assertions Approach" (INFOCOM, 2002)
- [43] Chavali et al., "Peer Prefix Limits Exchange in BGP" (Work in Progress, April 2004)
- [44] Zhao et al., "BGP Multiple Origin AS (MOAS) Conflicts" (NANOG, 2001)
- [45] Cisco Systems, "Building Security Into the Hardware" (2004)
- [46] Ylonen & Lonvick, "The Secure Shell (SSH) Protocol Architecture", RFC 4251, January 2006
- [47] Hinden, "Virtual Router Redundancy Protocol (VRRP)", RFC 3768, April 2004
- [48] Harrington et al., "An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks", STD 62, RFC 3411, December 2002
- [49] Malkin & Harkin, "TFTP Timeout Interval and Transfer Size Options", RFC 2349, May 1998
- [50] Rosenberg et al., "SIP: Session Initiation Protocol", RFC 3261, June 2002
- [51] Handley et al., "SDP: Session Description Protocol", RFC 4566, July 2006
- [52] Schulzrinne et al., "RTP: A Transport Protocol for Real-Time Applications", STD 64, RFC 3550, July 2003
- [53] Hedrick, "Routing Information Protocol", RFC 1058, June 1988

## Appendix A. IAB Members at the Time of This Writing
- Bernard Aboba, Loa Andersson, Brian Carpenter, Leslie Daigle, Elwyn Davies, Kevin Fall, Olaf Kolkman, Kurtis Lindvist, David Meyer, David Oran, Eric Rescorla, Dave Thaler, Lixia Zhang

## Requirements Summary (Key Normative "should" Statements from the Document)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Ingress filtering should be performed to prevent source address spoofing. | should | Section 3.2, [7] |
| R2 | Protocols should avoid including IP addresses/hostnames in payloads for subsequent messaging; if unavoidable, include handshake with unpredictable nonce and lightweight validation. | should | Section 3.2 |
| R3 | All retransmission during initial connection setup should be performed by the client. | should | Section 3.2 |
| R4 | Proxies should not arbitrarily relay requests to destinations chosen by a client. | should | Section 3.2 |
| R5 | Avoid signaling third-party connections; if unavoidable, incorporate lightweight validation before sending significant data. | should | Section 3.2 |
| R6 | Don't hold state for unverified hosts; use handshake to validate client address and push work/state to client. | should | Section 4.1.1 |
| R7 | Use puzzles, reverse Turing tests, or reachability testing to discriminate attackers (with awareness of limitations). | should | Section 4.1.2 |
| R8 | Routing protocols should be designed for graceful degradation under overload and automatic recovery. | should | Section 4.1.3 |
| R9 | Future autoconfiguration protocols should allow different end-systems to operate at different points in the ease-configuration/security spectrum. | should | Section 4.1.4 |
| R10 | Provision private, out-of-band access to console/control ports. | should | Section 4.2 |
| R11 | Disable default configurations that can be exploited (IP redirect, directed broadcast, proxy ARP). Avoid publicly readable SNMP communities. | should | Section 4.2 |
| R12 | Use cryptographic authentication (TCP MD5 or IPsec) combined with GTSM for BGP routing adjacencies. | should | Section 4.2.2 |
| R13 | Isolate router-to-router traffic from data traffic as feasible. | should | Section 4.2.3 |
| R14 | Routers should check protocol syntax and semantics rigorously, including sender verification (source IP, MAC, TTL). | should | Section 4.3.1 |
| R15 | Perform consistency checks on routing updates (e.g., origin AS list test). | should | Section 4.3.2 |
| R16 | Coordinate prefix limits between BGP peers (with care to avoid black-holing). | should | Section 4.3.3 |
| R17 | Adjust BGP KeepAlive/Hold Timer values to minimize session resets under heavy load. | should | Section 4.3.3 |
| R18 | Handle router resource exhaustion (ARP cache, queues) properly; implement multiple queues. | should | Section 4.3.4 |
| R19 | Use keyed hash mechanisms for state lookup to prevent algorithmic complexity attacks. | should | Section 4.4.1 |
| R20 | Use network polling under heavy load instead of interrupt-driven receive to avoid livelock. | should | Section 4.4.1.1 |
| R21 | Use unpredictable values for session IDs (TCP ISN, ports, DNS IDs). | should | Section 4.4.1.2 |
| R22 | Filter bad traffic early (ingress filtering). | should | Section 4.4.2.1 |
| R23 | Establish monitoring framework to detect and log abnormal network activity. | should | Section 4.4.2.2 |

## Informative Annexes (Condensed)
- **Appendix A. IAB Members**: Lists the IAB members at the time of writing (see above).
```
**Note**: The document text includes a full copyright statement and author addresses, which are not essential for technical compression; they are omitted.