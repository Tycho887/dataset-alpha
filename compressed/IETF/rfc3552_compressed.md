# RFC 3552 (BCP 72): Guidelines for Writing RFC Text on Security Considerations
**Source**: IETF | **Version**: July 2003 | **Date**: July 2003 | **Type**: Best Current Practice (Normative)
**Original**: https://datatracker.ietf.org/doc/rfc3552/

## Scope (Summary)
This document provides guidelines for RFC authors on writing a good Security Considerations section, including definitions of security goals, a threat model for the Internet, common security issues, and explicit requirements for documenting attacks and residual risks.

## Normative References
- [AH] – Kent, S., Atkinson, R., "IP Authentication Header", RFC 2402, November 1998.
- [DNSSEC] – Eastlake, D., "Domain Name System Security Extensions", RFC 2535, March 1999.
- [ENCOPT] – Tso, T., "Telnet Data Encryption Option", RFC 2946, September 2000.
- [ESP] – Kent, S., Atkinson, R., "IP Encapsulating Security Payload (ESP)", RFC 2406, November 1998.
- [GSS] – Linn, J., "Generic Security Services Application Program Interface Version 2, Update 1", RFC 2743, January 2000.
- [HTTP] – Fielding, R. et al., "HyperText Transfer Protocol", RFC 2616, June 1999.
- [HTTPTLS] – Rescorla, E., "HTTP over TLS", RFC 2818, May 2000.
- [HMAC] – Madson, C., Glenn, R., "The Use of HMAC-MD5-96 within ESP and AH", RFC 2403, November 1998.
- [KERBEROS] – Kohl, J., Neuman, C., "The Kerberos Network Authentication Service (V5)", RFC 1510, September 1993.
- [KEYWORDS] – Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [OTP] – Haller, N. et al., "A One-Time Password System", STD 61, RFC 2289, February 1998.
- [PHOTURIS] – Karn, P., Simpson, W., "Photuris: Session-Key Management Protocol", RFC 2522, March 1999.
- [PKIX] – Housley, R. et al., "Internet X.509 Public Key Infrastructure Certificate and CRL Profile", RFC 3280, April 2002.
- [RFC-2223] – Postel, J., Reynolds, J., "Instructions to RFC Authors", RFC 2223, October 1997.
- [RFC-2505] – Lindberg, G., "Anti-Spam Recommendations for SMTP MTAs", BCP 30, RFC 2505, February 1999.
- [RFC-2821] – Klensin, J., "Simple Mail Transfer Protocol", RFC 2821, April 2001.
- [SASL] – Myers, J., "Simple Authentication and Security Layer (SASL)", RFC 2222, October 1997.
- [SPKI] – Ellison, C. et al., "SPKI Certificate Theory", RFC 2693, September 1999.
- [SSH] – Ylonen, T., "SSH – Secure Login Connections Over the Internet", 6th USENIX Security Symposium, July 1996.
- [SASLSMTP] – Myers, J., "SMTP Service Extension for Authentication", RFC 2554, March 1999.
- [STARTTLS] – Hoffman, P., "SMTP Service Extension for Secure SMTP over Transport Layer Security", RFC 3207, February 2002.
- [S-HTTP] – Rescorla, E., Schiffman, A., "The Secure HyperText Transfer Protocol", RFC 2660, August 1999.
- [S/MIME] – Ramsdell, B. (Ed.), "S/MIME Version 3 Message Specification", RFC 2633, June 1999.
- [TELNET] – Postel, J., Reynolds, J., "Telnet Protocol Specification", STD 8, RFC 854, May 1983.
- [TLS] – Dierks, T., Allen, C., "The TLS Protocol Version 1.0", RFC 2246, January 1999.
- [TLSEXT] – Blake-Wilson, S. et al., "Transport Layer Security (TLS) Extensions", RFC 3546, May 2003.
- [TCPSYN] – "TCP SYN Flooding and IP Spoofing Attacks", CERT Advisory CA-1996-21.
- [UPGRADE] – Khare, R., Lawrence, S., "Upgrading to TLS Within HTTP/1.1", RFC 2817, May 2000.
- [URL] – Berners-Lee, T. et al., "Uniform Resource Locators (URL)", RFC 1738, December 1994.
- [VRRP] – Knight, S. et al., "Virtual Router Redundancy Protocol", RFC 2338, April 1998.

## Definitions and Abbreviations
- **Communication Security (COMSEC)**: Protecting communications via confidentiality, data integrity, and peer entity authentication.
- **Confidentiality**: Keeping data secret from unintended listeners.
- **Data Integrity**: Ensuring received data is exactly as sent; protecting against undetected modification.
- **Peer Entity Authentication**: Confirming that one endpoint is the intended party; includes data origin authentication.
- **Non-Repudiation**: Ability to prove to a third party that a communication occurred or that a party agreed to content; difficult in practice.
- **System Security**: Protecting machines and data from unauthorized usage, inappropriate usage, and denial of service.
- **Denial of Service (DoS)**: Attacks that consume resources or crash machines, preventing legitimate access.
- **Threat Model**: Description of attacker capabilities; typically assumes end-systems uncompromised but attacker has nearly complete control of the communications channel.
- **Passive Attack**: Attack where attacker reads packets but does not write; includes sniffing, password sniffing, offline cryptographic attacks.
- **Active Attack**: Attack where attacker writes data to the network; includes spoofing, replay, insertion, deletion, modification, man-in-the-middle.
- **Spoofing Attack**: Forging packet source address (possible without IPsec).
- **Blind Attack**: Active attack where attacker sends forged packets but cannot receive responses.
- **Man-in-the-Middle (MITM)**: Attacker poses as both endpoints; prevented by peer entity authentication.
- **Authorization**: Process of determining whether an authenticated party has permission to access a resource.
- **Key Distribution Center (KDC)**: Online trusted third party that mediates authentication (e.g., Kerberos).
- **Certificate**: Signed credential binding identity to public key; issued by a Certificate Authority (CA).
- **Object Security**: Security applied to entire data objects (e.g., S/MIME); persists beyond transmission.
- **Channel Security**: Security of a communication channel (e.g., IPsec, TLS); protects data in transit only.

## 1. Introduction
- All RFCs MUST contain a Security Considerations section per RFC 2223.
- This document provides guidance for authors to consider security in designs and inform readers of relevant issues.
- Structured as: (1) security tutorial and definitions, (2) guidelines for writing Security Considerations, (3) examples.

### 1.1. Requirements
- The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and **OPTIONAL** in this document are to be interpreted as described in BCP 14, RFC 2119 [KEYWORDS].

## 2. The Goals of Security
- Security is not monolithic; includes communication security and system security.

### 2.1. Communication Security
Divided into:
- **Confidentiality** (2.1.1): Data kept secret from eavesdroppers.
- **Data Integrity** (2.1.2): Ensures data not tampered in transit.
- **Peer Entity Authentication** (2.1.3): Knowing one endpoint is the intended party; asymmetric possible; includes data origin authentication.

### 2.2. Non-Repudiation
- Ability to demonstrate communication or agreement to a third party. Difficult due to key compromise claims, signing context, etc.

### 2.3. Systems Security
- **Unauthorized Usage** (2.3.1): Use of resources by unauthorized users.
- **Inappropriate Usage** (2.3.2): Authorized users performing forbidden activities.
- **Denial of Service** (2.3.3): Attacks that consume resources or crash machines.

## 3. The Internet Threat Model
- Assumes end-systems uncompromised; attacker has nearly complete control of the communications channel (read, remove, change, inject PDUs).
- PDU meaning differs per layer (IP packet, TCP segment, application PDU).

### 3.1. Limited Threat Models
- Passive attack: read only (e.g., packet sniffing).
- Active attack: write only or both.

### 3.2. Passive Attacks
- Attacker reads packets; possible on same LAN, compromised path, or via wireless.
- **Confidentiality Violations** (3.2.1): Sniffing private data (e.g., credit cards).
- **Password Sniffing** (3.2.2): Capture passwords for replay.
- **Offline Cryptographic Attacks** (3.2.3): Capture data using victim's key; dictionary attacks on low-entropy passwords.

### 3.3. Active Attacks
- **Replay Attacks** (3.3.1): Record and retransmit messages (e.g., duplicate transaction).
- **Message Insertion** (3.3.2): Forge and inject packets (e.g., SYN flood).
- **Message Deletion** (3.3.3): Remove messages (e.g., to prevent RST in sequence number attack).
- **Message Modification** (3.3.4): Alter messages (e.g., cut-and-paste on credit card order).
- **Man-In-The-Middle** (3.3.5): Attacker positions between endpoints; prevented by peer entity authentication of at least one side.

### 3.4. Topological Issues
- Not all attackers are equally capable.

### 3.5. On-path versus off-path
- On-path attackers can read/modify all datagrams along path.
- Off-path attackers can send arbitrary packets but may not receive responses.
- **Application protocol designers MUST NOT assume that all attackers will be off-path. Where possible, protocols SHOULD be designed to resist attacks from attackers who have complete control of the network.** Designers should give more weight to attacks mountable by off-path attackers.

### 3.6. Link-local
- On-path special case: same link; can verify with IP TTL=255 (must be set and checked). Use with caution in tunneling.

## 4. Common Issues

### 4.1. User Authentication
#### 4.1.1. Username/Password
- Vulnerable to passive sniffing. Must be protected (e.g., TLS, IPsec). Unprotected plaintext username/password NOT acceptable in IETF standards.

#### 4.1.2. Challenge Response and One Time Passwords
- Protect against replay; often vulnerable to offline keysearch/dictionary attack. Still vulnerable to connection hijacking unless entire session secured.

#### 4.1.3. Shared Keys
- Random large keys resist dictionary attacks; management problem.

#### 4.1.4. Key Distribution Centers
- KDC (e.g., Kerberos) shares symmetric key with each party; provides tickets.

#### 4.1.5. Certificates
- Public key certificates [PKIX] used in TLS, S/MIME; requires trusted roots; deployment challenge for clients.

#### 4.1.6. Some Uncommon Systems
- Protocols like EKE, SPEKE, SRP securely bootstrap passwords; IP status unclear.

#### 4.1.7. Host Authentication
- Need secure binding between certificate and expected hostname (not IP address unless secure name resolution).

### 4.2. Generic Security Frameworks
- GSS-API, SASL allow pluggable mechanisms.
- Problems: downgrade attacks (integrity check limited to weakest algorithm), unclear interaction with application.
- **Designers SHOULD carefully examine framework options and specify only mechanisms appropriate for threat model. If framework necessary, SHOULD choose established ones instead of designing own.**

### 4.3. Non-repudiation
- Naive use of digital signatures insufficient due to key compromise claims. Requires timestamp servers, CRL archival, etc. Difficult in practice.

### 4.4. Authorization vs. Authentication
- Authentication identifies; authorization defines permissions. Authentication does not imply authorization.

#### 4.4.1. Access Control Lists
- List users per resource; hierarchical inheritance.

#### 4.4.2. Certificate Based Systems
- Valid signature does not imply authorization; need trusted root in context. Policies via ACLs or certificate extensions.

### 4.5. Providing Traffic Security
#### 4.5.1. IPsec
- Provides host-to-host security; supports various identity granularities. Deployment limited; API not standardized.
- **Designers MUST NOT assume IPsec will be available. Security policy SHOULD NOT simply state IPsec must be used. For IPv6, AH/ESP mandatory to implement, but IKE not. [USEIPSEC] provides guidance.**

#### 4.5.2. SSL/TLS
- Channel security over TCP; separate port or upward negotiation (e.g., STARTTLS). Vulnerable to IP layer attacks (forged RSTs).
- **Virtual Hosts** (4.5.2.1): TLS hostname extension solves certificate selection.
- **Remote Authentication and TLS** (4.5.2.2): Using TLS without server authentication (anonymous DH) and SASL leaves man-in-the-middle possible. Server authentication required; challenge-response then less desirable.

#### 4.5.3. Remote Login
- Telnet encryption option (no integrity) reduces overhead. SSH provides secure port forwarding; improper use can bypass firewalls.

### 4.6. Denial of Service Attacks and Countermeasures
- **Authors of Internet standards MUST describe which denial of service attacks their protocol is susceptible to. This description MUST include the reasons it was unreasonable or out of scope to attempt to avoid these DoS attacks.**

#### 4.6.1. Blind Denial of Service
- Attacker uses forged IP addresses; harder to filter. **Designers should make every attempt possible to prevent blind denial of service attacks.**

#### 4.6.2. Distributed Denial of Service (DDoS)
- Multiple zombies coordinated; hard to counter.

#### 4.6.3. Avoiding Denial of Service
1. **Make attacker do more work than you** (e.g., require cryptographic operation).
2. **Make attacker prove they can receive data from you** (e.g., require reply with information from earlier exchange).

#### 4.6.4. Example: TCP SYN Floods
- Single packet forces resource consumption; blind attack.

#### 4.6.5. Example: Photuris
- Anti-clogging cookie mechanism prevents stateless attack.

### 4.7. Object vs. Channel Security
- Object security (e.g., S/MIME) protects the object itself; channel security (e.g., IPsec, TLS) protects transmission only. Distinction is perspective: IPsec looks like object security at IP layer, channel security at application layer.

### 4.8. Firewalls and Network Topology
- **Protocol designers cannot safely assume their protocols will be deployed behind firewalls.** Networks may be reconfigured; firewalls pass generic protocols. Insider threats are serious.

## 5. Writing Security Considerations Sections
- **Authors MUST describe:**
  1. Which attacks are out of scope (and why!)
  2. Which attacks are in-scope:
     2.1 Attacks the protocol is susceptible to
     2.2 Attacks the protocol protects against
- **At least the following attacks MUST be considered:** eavesdropping, replay, message insertion, deletion, modification, man-in-the-middle. Potential denial of service attacks MUST be identified.
- If cryptographic protection used, indicate which portions of data are protected and what protections (integrity, confidentiality, authentication). Indicate susceptibility to attacks. Label secret data (keying material, seeds).
- **User authentication method security MUST be clearly specified.** Document assumptions (e.g., password strength, vulnerability to sniffing, dictionary attack).
- **It is insufficient to simply state that one's protocol should be run over some lower layer security protocol. If a system relies upon lower layer security, the protections expected MUST be clearly specified. Resultant properties of combined system must be specified.**
- **In general, the IESG will not approve standards track protocols which do not provide for strong authentication, either internal or through tight binding to a lower layer security protocol.**
- **The threat environment MUST at a minimum include deployment across the global Internet across multiple administrative boundaries without assuming firewalls, even if only to justify why out of scope.**
- **There should be a clear description of residual risk after threat mitigation.**
- **Discuss potential security risks from misapplication of the protocol or technology, possibly with an Applicability Statement.**

## 6. Examples (Condensed)
### 6.1. SMTP
- Original RFC 821 lacked Security Considerations; RFC 2821 added it.
- **Security Considerations from RFC 2821 reproduced with commentary.** Key points:
  - SMTP inherently insecure; spoofing trivial.
  - Blind copies: servers SHOULD NOT copy RCPT args into headers.
  - VRFY/EXPN: implementations that disable MUST NOT appear to verify; return 252.
  - Information disclosure in announcements, trace fields, forwarding.
  - **Scope of operation:** relay function may be limited; 550 code for rejection.
- **Additional sections added by this document:**
  - **Inappropriate Usage (spam):** SMTP provides no protection; blacklists, open relays, closed relaying.
  - **Communications Security:** SMTP over IPsec, SMTP/TLS, S/MIME and PGP/MIME.
    - SMTP over IPsec: confidentiality between gateways; endpoint identification problem; lack of standard API. **Implementors MUST NOT assume IPsec available.**
    - SMTP/TLS: similar protection; susceptible to DNS spoofing; low-security export mode.
    - S/MIME and PGP/MIME: object security; end-to-end sender/recipient authentication; no replay protection; traffic analysis possible.
  - **Denial of Service:** None of these measures protect; connection attacks, forged RSTs.

### 6.2. VRRP
- Security Considerations from RFC 2338 with commentary.
- **No Authentication:** SHOULD only be used with minimal risk.
- **Simple Text Password:** RECOMMENDED for minimal risk; password sent frequently.
- **IP Authentication Header (AH):** RECOMMENDED for limited control over LAN nodes; protects against replay, modification. **Note:** AH should be MUST implement and MUST for untrusted nodes.
- Additional analysis: VRRP authentication may be brittle and offer marginal benefit over ARP attacks.

## 7–10. (Condensed)
- **7. Acknowledgments:** Based on note by Ran Atkinson (1997) and IAB Security Workshop; thanks to various contributors.
- **8. Normative References:** Listed above in Normative References section.
- **9. Informative References:** [DDOS], [EKE], [IDENT], [INTAUTH], [IPSPPROB], [KLEIN], [NNTP], [POP], [SEQNUM], [SOAP], [SPEKE], [SRP], [USEIPSEC], [WEP].
- **10. Security Considerations:** This entire document is about security considerations.

## Appendix A
- IAB Members at time of writing: Harald Alvestrand, Ran Atkinson, Rob Austein, Fred Baker, Leslie Daigle, Steve Deering, Sally Floyd, Ted Hardie, Geoff Huston, Charlie Kaufman, James Kempf, Eric Rescorla, Mike St. Johns.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Key words MUST, SHOULD, etc. interpreted per RFC 2119. | MUST | §1.1 |
| R2 | Application protocol designers MUST NOT assume all attackers are off-path. | MUST | §3.5 |
| R3 | Protocols SHOULD be designed to resist attacks from attackers with complete network control. | SHOULD | §3.5 |
| R4 | Unprotected (plaintext) username/password systems are not acceptable in IETF standards. | MUST NOT | §4.1.1 |
| R5 | If a generic security framework is used, designers SHOULD carefully examine options and specify only appropriate mechanisms. | SHOULD | §4.2 |
| R6 | If a framework is necessary, designers SHOULD choose established ones. | SHOULD | §4.2 |
| R7 | Designers MUST NOT assume IPsec will be available. | MUST NOT | §4.5.1 |
| R8 | Security policy for generic application layer protocol SHOULD NOT simply state "IPsec must be used" unless IPsec availability is assured. | SHOULD NOT | §4.5.1 |
| R9 | For IPv6-only protocols, it is reasonable to assume AH/ESP available, but IKE not; designers SHOULD NOT assume IKE present. | SHOULD NOT | §4.5.1 |
| R10 | Authors of Internet standards MUST describe which denial of service attacks their protocol is susceptible to, including reasons why avoidance was unreasonable or out of scope. | MUST | §4.6 |
| R11 | Designers should make every attempt possible to prevent blind denial of service attacks. | SHOULD | §4.6.1 |
| R12 | In Security Considerations sections, authors MUST describe out-of-scope attacks (with reasons), in-scope attacks, and which attacks protocol protects against. | MUST | §5 |
| R13 | At least eavesdropping, replay, message insertion, deletion, modification, man-in-the-middle, and denial of service MUST be considered. | MUST | §5 |
| R14 | If cryptographic protection used, indicate protected portions and types of protection. Label secret data. | MUST | §5 |
| R15 | User authentication method security MUST be clearly specified; document assumptions. | MUST | §5 |
| R16 | It is insufficient to only state protocol should be run over lower-layer security; protections expected MUST be specified. | MUST | §5 |
| R17 | IESG will not approve standards track protocols without strong authentication (internal or via tight binding to lower-layer security). | MUST | §5 |
| R18 | Threat environment MUST include deployment across global Internet without assuming firewalls. | MUST | §5 |
| R19 | Must describe residual risk after threat mitigation. | MUST | §5 |
| R20 | Should discuss risks from misapplication. | SHOULD | §5 |
| R21 | SMTP implementations that disable VRFY/EXPN MUST NOT appear to have verified addresses; return 252. | MUST | §6.1.1.3 |
| R22 | SMTP clients and servers SHOULD NOT copy full RCPT set into headers. | SHOULD | §6.1.1.2 |
| R23 | Receiving systems SHOULD NOT deduce relationships between envelope and header addresses. | SHOULD | §6.1.1.2 |
| R24 | SMTP servers MUST return 252 if VRFY disabled for security reasons. | MUST | §6.1.1.3 |
| R25 | SMTP implementations SHOULD provide capability to limit relay function. | SHOULD | §6.1.1.7 |
| R26 | SMTP over IPsec: implementors MUST NOT assume IPsec available. | MUST | §6.1.2.1 |
| R27 | VRRP No Authentication SHOULD only be used in minimal risk environments. | SHOULD | §6.2.1.1 |
| R28 | VRRP Simple Text Password is RECOMMENDED when minimal risk of active disruption; password should not be security significant. | RECOMMENDED | §6.2.1.2 |
| R29 | VRRP IP Authentication Header is RECOMMENDED when limited control over LAN administration. | RECOMMENDED | §6.2.1.3 |