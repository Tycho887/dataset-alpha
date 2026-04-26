# RFC 3768: Virtual Router Redundancy Protocol (VRRP)
**Source**: IETF | **Version**: Standards Track | **Date**: April 2004 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc3768/

## Scope (Summary)
This document defines the Virtual Router Redundancy Protocol (VRRP), which provides dynamic failover for default routers on a LAN by electing a Master router to forward packets for a virtual router IP address(es). VRRP eliminates the single point of failure in static default routing without requiring dynamic routing on end-hosts.

## Normative References
- [802.1D] ISO/IEC 10038:1993, ANSI/IEEE Std 802.1D-1993
- [CKSM] Braden, R., Borman, D. and C. Partridge, "Computing the Internet checksum", RFC 1071, September 1988
- [HSRP] Li, T., Cole, B., Morton, P. and D. Li, "Cisco Hot Standby Router Protocol (HSRP)", RFC 2281, March 1998
- [IPSTB] Higginson, P. and M. Shand, "Development of Router Clusters to Provide Fast Failover in IP Networks", Digital Technical Journal, Volume 9 Number 3, Winter 1997
- [IPX] Novell Inc., "IPX Router Specification", Version 1.10, October 1992
- [RFC1469] Pusateri, T., "IP Multicast over Token Ring Local Area Networks", RFC 1469, June 1993
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997
- [RFC2338] Knight, S., et al., "Virtual Router Redundancy Protocol", RFC 2338, April 1998
- [TKARCH] IBM Token-Ring Network, Architecture Reference, Publication SC30-3374-02, Third Edition, September 1989

## Definitions and Abbreviations
- **VRRP Router**: A router running VRRP; may participate in one or more virtual routers.
- **Virtual Router**: An abstract object managed by VRRP that acts as a default router for hosts on a shared LAN. Consists of a VRID and set of associated IP address(es) across a common LAN.
- **IP Address Owner**: The VRRP router that has the virtual router's IP address(es) as real interface address(es). When up, it will respond to packets addressed to those IP addresses (e.g., ICMP pings, TCP connections).
- **Primary IP Address**: An IP address selected from the set of real interface addresses. VRRP advertisements are always sent using the primary IP address as the source of the IP packet.
- **Virtual Router Master**: The VRRP router assuming responsibility for forwarding packets to the virtual router's IP address(es) and answering ARP requests for those addresses. If the IP address owner is available, it will always become Master.
- **Virtual Router Backup**: The set of VRRP routers available to assume forwarding responsibility if the current Master fails.
- **VRID**: Virtual Router Identifier, configurable in range 1–255 (no default).
- **Priority**: Priority value for Master election; 255 for IP address owner, 1–254 for backup routers (default 100), 0 signals Master is leaving.
- **Skew_Time**: (256 - Priority) / 256 seconds.
- **Master_Down_Interval**: (3 * Advertisement_Interval) + Skew_time seconds.
- **Preempt_Mode**: Controls whether a higher-priority Backup preempts a lower-priority Master (default True), except IP address owner always preempts.
- **Advertisement_Interval**: Time between VRRP Advertisement messages (seconds, default 1).
- **Authentication_Type**: 0 = No Authentication; 1,2 = Reserved.

## 1. Introduction
VRRP eliminates the single point of failure in static default routing by providing dynamic failover. It uses an election protocol to assign one VRRP router as Master for a virtual router IP address(es). VRRP functions similarly to HSRP and IPSTB.

Key words (MUST, SHOULD, etc.) are as defined in [RFC2119].

### 1.1 Contributors
Authors of RFC 2338 (P. Higginson, R. Hinden, P. Hunt, S. Knight, A. Lindem, D. Mitzel, M. Shand, D. Weaver, D. Whipple) contributed to this document.

### 1.2 Scope
VRRP is intended for IPv4 routers only. The specification covers protocol features, design goals, message format, state machine, and operational issues (MAC mapping, ARP, ICMP redirects, security).

## 2. Required Features
### 2.1 IP Address Backup
Primary function of VRRP. Protocol should minimize black hole duration, steady-state overhead, function over multiaccess LANs, support multiple virtual routers for load balancing, and multiple logical IP subnets.

### 2.2 Preferred Path Indication
VRRP must allow expression of path preference and guarantee convergence to the highest-preference router available.

### 2.3 Minimization of Unnecessary Service Disruptions
After Master election, no transition triggered by a Backup of equal or lower preference while Master functions properly. It may be useful to support override of immediate convergence to preferred path.

### 2.4 Efficient Operation over Extended LANs
VRRP should use virtual router MAC as source in Master packets to trigger bridge learning, send a message immediately after transitioning to Master, and send periodic messages to maintain learning caches.

## 3. VRRP Overview
- Protocol uses IP multicast (224.0.0.18) with well-known MAC address (00-00-5E-00-01-{VRID}).
- Each VRRP router has a VRID and set of IP addresses. Only Master sends periodic Advertisements.
- Backup routers do not preempt unless they have higher priority (or IP address owner always preempts). Preemption can be disabled.
- Optimizations assume typical scenarios (two routers, distinct preferences) to reduce complexity; duplicates may occur briefly in equal-preference scenarios.

## 4. Sample Configurations
### 4.1 Sample 1: Two routers, one virtual router.
Rtr1 owns IP A (VRID=1, priority=255) becomes Master; Rtr2 is Backup (priority=100). If Rtr1 fails, Rtr2 becomes Master.

### 4.2 Sample 2: Two virtual routers for load balancing.
Rtr1 is Master for VRID=1 and Backup for VRID=2; Rtr2 is Master for VRID=2 and Backup for VRID=1. Hosts use either IP A or IP B as default.

## 5. Protocol
### 5.1 VRRP Packet Format
- Version: 2
- Type: 1 (Advertisement only)
- Fields: Version, Type, VRID, Priority, Count IP Addrs, Auth Type, Adver Int, Checksum, IP Address(es), Authentication Data (reserved).

### 5.2 IP Field Descriptions
- **Source Address**: Primary IP address of the sending interface.
- **Destination Address**: 224.0.0.18 (link-local multicast). Routers MUST NOT forward.
- **TTL**: MUST be set to 255; MUST discard if TTL ≠ 255.
- **Protocol**: 112 (decimal).

### 5.3 VRRP Field Descriptions
- **Version**: 2.
- **Type**: 1 (Advertisement); unknown types MUST be discarded.
- **VRID**: 1-255.
- **Priority**: 255 for owner, 1-254 for backups (default 100), 0 to signal Master leaving.
- **Count IP Addrs**: Number of IP addresses in the advertisement.
- **Auth Type**: 0 (No Authentication); 1,2 reserved.
- **Adver Int**: Time interval between advertisements (seconds, default 1).
- **Checksum**: 16-bit one's complement sum of entire VRRP message (with checksum field zeroed).
- **IP Address(es)**: List of addresses associated with virtual router.
- **Authentication Data**: SHOULD be set to zero; ignored on reception.

## 6. Protocol State Machine
### 6.1 Parameters per Virtual Router
- VRID (1-255), Priority (0-255), IP_Addresses, Advertisement_Interval, Skew_Time, Master_Down_Interval, Preempt_Mode (True/False, default True), Authentication_Type, Authentication_Data.

### 6.2 Timers
- **Master_Down_Timer**: Fires when no advertisement heard for Master_Down_Interval.
- **Adver_Timer**: Fires every Advertisement_Interval to trigger advertisement.

### 6.3 State Transition Diagram
States: Initialize → (if Priority=255) Master, else Backup. Master ↔ Backup.

### 6.4 State Descriptions
**Initialize**: On Startup: if Priority=255, send Advertisement, send gratuitous ARP, set Adver_Timer, transition to Master; else set Master_Down_Timer, transition to Backup.

**Backup**: 
- MUST NOT respond to ARP for virtual router IP addresses.
- MUST discard packets with virtual router MAC.
- MUST NOT accept packets addressed to virtual router IP addresses.
- On Shutdown: cancel Master_Down_Timer, go to Initialize.
- On Master_Down_Timer fire: send Advertisement, gratuitous ARP, set Adver_Timer, go to Master.
- On Advertisement received:
  - If Priority=0: set Master_Down_Timer to Skew_Time.
  - Else: if Preempt_Mode=False or received Priority >= local Priority: reset Master_Down_Timer to Master_Down_Interval; else discard advertisement.

**Master**:
- MUST respond to ARP for virtual router IP addresses.
- MUST forward packets with virtual router MAC.
- MUST NOT accept packets addressed to virtual router IP addresses unless IP address owner.
- On Shutdown: cancel Adver_Timer, send Advertisement with Priority=0, go to Initialize.
- On Adver_Timer fire: send Advertisement, reset timer.
- On Advertisement received:
  - If Priority=0: send Advertisement, reset Adver_Timer.
  - Else: if received Priority > local Priority, or equal and sender primary IP > local primary IP: cancel Adver_Timer, set Master_Down_Timer, go to Backup; else discard advertisement.

## 7. Sending and Receiving VRRP Packets
### 7.1 Receiving VRRP Packets
MUST verify:
- IP TTL = 255
- VRRP version = 2
- Complete packet (including fixed fields, IP addresses, Authentication Data)
- VRRP checksum
- VRID is configured on receiving interface and local router is not IP address owner (Priority ≠ 255)
- Auth Type matches local configuration
- Adver Interval matches local configuration

If any check fails, discard, SHOULD log, MAY indicate via network management.
MAY verify Count IP Addrs and IP addresses match configuration; if mismatch and sender is not address owner, MUST drop; otherwise continue.

### 7.2 Transmitting VRRP Packets
MUST:
- Fill packet fields with appropriate virtual router state.
- Compute VRRP checksum.
- Set source MAC to Virtual Router MAC Address.
- Set source IP to interface primary IP address.
- Set IP protocol to VRRP (112).
- Send to VRRP IP multicast group (224.0.0.18).

### 7.3 Virtual Router MAC Address
IEEE 802 MAC: `00-00-5E-00-01-{VRID}` (hex). First three octets from IANA OUI; next two (00-01) indicate VRRP address block. Supports up to 255 virtual routers.

## 8. Operational Issues
### 8.1 ICMP Redirects
Should use source address of the virtual router the packet was sent to. When Master does not own the address, deduce virtual router from destination MAC. Redirects may be disabled in symmetric load-sharing topologies.

### 8.2 Host ARP Requests
Master MUST respond to ARP requests for virtual router IP addresses with the virtual router MAC address (not its physical MAC). On restart or boot, VRRP router SHOULD send gratuitous ARP with virtual MAC and delay until both IP and virtual MAC are configured.

### 8.3 Proxy ARP
If used, VRRP router MUST advertise the Virtual Router MAC address in Proxy ARP messages.

### 8.4 Potential Forwarding Loop
A VRRP router that is not the IP address owner SHOULD NOT forward packets addressed to the virtual router's IP addresses (e.g., by adding/removing reject host route on state transitions).

## 9. Operation over FDDI, Token Ring, and ATM LANE
### 9.1 FDDI
SHOULD configure virtual router MAC as a unicast filter (not change hardware address) to avoid removal of foreign advertisements.

### 9.2 Token Ring
Functional address mode (see mapping table) MUST be implemented. Unicast mode MAY be supported (same MAC as Ethernet, but ARP uses virtual MAC as source). Source-route bridge issues noted.

### 9.3 ATM LANE
Operation beyond scope of this document.

## 10. Security Considerations
VRRP does not include authentication (earlier types removed due to ineffectiveness). Attackers on the LAN can already disrupt ARP and forwarding independently. TTL=255 check limits remote injection to local attacks. No confidentiality needed.

## 11. Acknowledgements
Various contributors listed.

## 12. References
Normative and informative references (see above).

## 13. Changes from RFC 2338
- Removed authentication methods; fields retained for backward compatibility.
- Clarified IP address owner mapping, address list validation, Preempt_Mode.
- Added subsection on ATM LANE scope, forwarding loop prevention, security clarification.
- Editorial updates.

## 14. Editor's Address
Robert Hinden, Nokia, Mountain View, CA; phone +1 650 625-2004; email bob.hinden@nokia.com.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | IP TTL for VRRP packets MUST be 255 | shall | Section 5.2.3, 7.1 |
| R2 | Destination IP address MUST be 224.0.0.18 | shall | Section 5.2.2 |
| R3 | Router MUST NOT forward packets with destination 224.0.0.18 | shall | Section 5.2.2 |
| R4 | VRRP packet with unknown type MUST be discarded | shall | Section 5.3.2 |
| R5 | Priority for IP address owner MUST be 255 | shall | Section 5.3.4 |
| R6 | Backup routers MUST use priority 1-254 | shall | Section 5.3.4 |
| R7 | Advertisement with Priority=0 indicates Master is leaving | normative | Section 5.3.4 |
| R8 | TTL ≠ 255 MUST discard packet | shall | Section 7.1 |
| R9 | Must verify VRID is configured and local router is not IP address owner | shall | Section 7.1 |
| R10 | Must verify Auth Type matches local configuration | shall | Section 7.1 |
| R11 | Must verify Adver Interval matches local configuration | shall | Section 7.1 |
| R12 | On Master_Down_Timer fire, Backup MUST send ADVERTISEMENT, gratuitous ARP, transition to Master | shall | Section 6.4.2 |
| R13 | Master MUST respond to ARP requests with virtual MAC | shall | Section 6.4.3, 8.2 |
| R14 | Master MUST forward packets to virtual MAC | shall | Section 6.4.3 |
| R15 | Non-owner Master MUST NOT accept packets for virtual IP addresses | shall | Section 6.4.3 |
| R16 | Owner Master MUST accept packets for virtual IP addresses | shall | Section 6.4.3 |
| R17 | On Shutdown, Master MUST send Advertisement with Priority=0 | shall | Section 6.4.3 |
| R18 | Preempt_Mode default is True | should | Section 6.1 |
| R19 | IP address owner always preempts regardless of Preempt_Mode | must (normative exception) | Section 6.1 |
| R20 | Token ring functional address mode MUST be implemented | shall | Section 9.2 |

## Informative Annexes (Condensed)
- **Annex A (Sample Configurations)**: Illustrates two typical setups: single virtual router with one Master and one Backup, and dual virtual routers for load balancing. Provides context for protocol behavior.
- **Annex B (Changes from RFC 2338)**: Summarizes removal of authentication, clarifications on IP address owner, address validation, preemption, and security. Ensures backward compatibility while updating security stance.