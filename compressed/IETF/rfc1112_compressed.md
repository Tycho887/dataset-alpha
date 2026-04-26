# RFC 1112: Host Extensions for IP Multicasting
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standard | **Date**: August 1989 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/html/rfc1112

## Scope (Summary)
This memo specifies the extensions required of a host implementation of IP to support multicasting, defining three conformance levels (0–2). It covers host group addressing, sending and receiving multicast IP datagrams, and the Internet Group Management Protocol (IGMP) for level 2 hosts.

## Normative References
- RFC‑988, RFC‑1054 (obsoleted by this memo)
- Assigned Numbers (for permanent group addresses)
- IEEE 802.2 (for local network multicast handling)

## Definitions and Abbreviations
- **Host group**: a set of zero or more hosts identified by a single IP destination address (class D).
- **Multicast router**: forwards multicast datagrams between networks; transparent to hosts.
- **Class D address**: IP address with high‑order bits `1110`; range 224.0.0.0–239.255.255.255.
- **All‑hosts group**: permanent group 224.0.0.1 for all IP hosts on a directly connected network.
- **IGMP**: Internet Group Management Protocol, used by hosts to report group memberships to multicast routers.

## 3. Levels of Conformance
- **Level 0**: No support. Class D datagrams shall be quietly discarded.
- **Level 1**: Support for sending only. Only Sections 4, 5, 6 apply.
- **Level 2**: Full support, including IGMP. All sections apply.

## 4. Host Group Addresses
- Host groups are identified by class D IP addresses. 224.0.0.0 is unassigned; 224.0.0.1 is the all‑hosts group.
- Permanent groups have well‑known addresses; transient groups are dynamically assigned.
- Class E addresses (high‑order `1111`) are reserved.

## 5. Model of a Host IP Implementation
- IGMP and ICMP reside within the IP module; IP‑to‑local address mapping is in local network modules.
- Level 1 requires sending support; Level 2 requires both sending and receiving.

## 6. Sending Multicast IP Datagrams

### 6.1 Extensions to the IP Service Interface
- **R1**: Upper‑layer protocol shall be able to specify the IP time‑to‑live of an outgoing multicast datagram; default shall be 1.
- **R2**: Upper‑layer protocol shall be able to identify the outgoing network interface; default under system management.
- **R3** (Level 2 only): Upper‑layer protocol shall be able to inhibit local delivery (loopback) of a datagram if the host is a member of the destination group; default is to loop back a copy.

### 6.2 Extensions to the IP Module
- **R4**: Routing logic shall treat a host group address as local:
  ```
  if IP-destination is on the same local network
  or IP-destination is a host group,
      send datagram locally to IP-destination
  else
      send datagram locally to GatewayTo( IP-destination )
  ```
- **R5** (Level 2): If the sending host is a member of the destination group on the outgoing interface, a copy of the datagram shall be looped back for local delivery unless inhibited by the sender.
- **R6**: The IP source address shall be one of the individual addresses of the outgoing interface.
- **R7**: A host group address must never be placed in the source address field or anywhere in a source route or record route option.

### 6.3 Extensions to the Local Network Service Interface
- No change required.

### 6.4 Extensions to an Ethernet Local Network Module
- **R8**: Map IP host group address to Ethernet multicast address by placing the low‑order 23 bits of the IP address into the low‑order 23 bits of Ethernet address `01‑00‑5E‑00‑00‑00` (hex).

### 6.5 Extensions to Local Network Modules other than Ethernet
- For broadcast networks: map all IP host group addresses to a single local broadcast address.
- For point‑to‑point links: transmit as unicast.
- For store‑and‑forward networks: map to the well‑known address of an IP multicast router.

## 7. Receiving Multicast IP Datagrams

### 7.1 Extensions to the IP Service Interface
- **R9**: The IP service interface shall provide the following non‑blocking operations:
  ```c
  JoinHostGroup ( group-address, interface )
  LeaveHostGroup ( group-address, interface )
  ```
- **R10**: `JoinHostGroup` may fail due to invalid address or lack of resources; `LeaveHostGroup` may fail if the host is not a member. Membership persists if multiple upper‑layer protocols have joined the same group.
  - The interface argument may be omitted on single‑interface hosts; if omitted, the default sending interface is used.

### 7.2 Extensions to the IP Module
- **R11**: The IP module shall maintain a list of host group memberships per network interface. Incoming datagrams destined to a joined group are processed like unicast.
- **R12**: Incoming datagrams destined to groups the host does not belong to shall be discarded without generating any error report or log entry.
- **R13**: If a datagram arrives on one interface but the host belongs to the group only on a different interface, the datagram shall be quietly discarded.
- **R14**: An incoming datagram shall not be rejected for having an IP time‑to‑live of 1.
- **R15**: An incoming datagram with a host group address in its source address field shall be quietly discarded.
- **R16**: An ICMP error message (Destination Unreachable, Time Exceeded, Parameter Problem, Source Quench, Redirect) must never be generated in response to a datagram destined to a host group.
- **R17**: Each membership shall have a reference count. On the first join and the last leave for a group on a given interface, the local network module shall be notified.
- **R18**: The IP module shall implement the Internet Group Management Protocol (IGMP) as specified in Appendix I (required for Level 2).
- **R19**: Every Level 2 host shall join the all‑hosts group (224.0.0.1) on each network interface at initialization time and shall remain a member for as long as the host is active.

### 7.3 Extensions to the Local Network Service Interface
- **R20**: Extend the interface with:
  ```c
  JoinLocalGroup ( group-address )
  LeaveLocalGroup ( group-address )
  ```
  where `group-address` is an IP host group address. The local network module shall map IP addresses to local network addresses to update its multicast reception filter.
- **R21**: The local network module may ignore `LeaveLocalGroup` requests and may deliver up packets destined to more addresses than those specified in `JoinLocalGroup` requests if filtering is inadequate.
- **R22**: The local network module must not deliver up any multicast packets that were transmitted from that module; loopback is handled at the IP layer or higher.

### 7.4 Extensions to an Ethernet Local Network Module
- **R23**: An Ethernet module shall be able to receive packets addressed to the Ethernet multicast addresses that correspond to the host’s IP host group addresses. It should use hardware address filtering where possible, but must be capable of listening on an arbitrary number of Ethernet multicast addresses. If the hardware filter limit is exceeded, the module may open the filter to accept all multicast packets.

### 7.5 Extensions to Local Network Modules other than Ethernet
- Other multicast networks (e.g., IEEE 802.2): same as Ethernet.
- Pure broadcast networks: accept all broadcast packets and filter at IP.
- Point‑to‑point or store‑and‑forward networks: no change; multicast datagrams arrive as unicasts.

## Appendix I: Internet Group Management Protocol (IGMP) (Normative)

IGMP is required for Level 2 hosts. Messages are encapsulated in IP with protocol number 2. Format (8 octets):

```
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Type  |    Unused     |           Checksum            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                         Group Address                         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- **Version**: 1 (this memo).  
- **Type**: 1 = Host Membership Query, 2 = Host Membership Report.  
- **Unused**: zeroed when sent, ignored when received.  
- **Checksum**: 16‑bit one’s complement of the one’s complement sum of the 8‑octet message (checksum field zeroed for computation).  
- **Group Address**: In Query, zeroed; in Report, the IP host group address being reported.

### Informal Protocol Description
- Multicast routers send Queries (to all‑hosts, TTL=1) to discover group members.
- Hosts respond with Reports after a random delay \(t \in [0, D]\) seconds.  
- Reports are sent to the group address being reported; other hosts hearing a Report cancel their timers for that group.  
- Exceptions: (1) a running timer is not reset on a new Query; (2) membership in the all‑hosts group is never reported.  
- When joining a new group, the host shall immediately transmit a Report for that group, and it is recommended to repeat once or twice after short delays.  
- On a network without multicast routers, the only IGMP traffic is the Report(s) sent when a host joins a group.

### State Transition Diagram
States per group per interface: **Non‑Member**, **Delaying Member**, **Idle Member**.

```
                  ┌────────────────┐
                  │  Non‑Member    │
                  │                │
                  └────┬───────────┘
                       │
       join group (send report, start timer)
                       │
                       ▼
                  ┌────────────────┐
                  │ Delaying Member│◄──────── query received (start timer)
                  │                │────────► report received (stop timer)
                  └────────┬───────┘
                           │
               timer expired (send report)
                           │
                           ▼
                  ┌────────────────┐
                  │  Idle Member   │
                  │                │
                  └────────────────┘
```

Transitions:
- **Non‑Member**: on `join group` → Delaying Member (action: send report, start timer).  
- **Delaying Member**: on `query received` → Delaying Member (action: start timer, unless timer already running); on `report received` → Idle Member (action: stop timer); on `timer expired` → Idle Member (action: send report); on `leave group` → Non‑Member (action: stop timer).  
- **Idle Member**: on `join group` → (not applicable); on `leave group` → Non‑Member; on `query received` → Delaying Member (action: start timer); on `report received` → Idle Member (no action).  

All‑hosts group: starts in Idle Member state, never transitions.

### Protocol Parameters
- **Maximum report delay \(D\)**: 10 seconds.

## Appendix II: Host Group Address Issues (Informative)
Provides background on binding (dynamic binding of group addresses to a set of interfaces), allocation of transient addresses (possible servers, algorithmic mapping from higher‑level addresses), and cautions that misdelivery must be detected at layers above IP (encryption or administrative controls may be used for privacy).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Upper‑layer shall be able to specify TTL; default 1. | shall | 6.1 |
| R2 | Upper‑layer shall be able to specify outgoing interface; default under system management. | shall | 6.1 |
| R3 | Upper‑layer shall be able to inhibit local loopback; default loopback. | shall | 6.1 |
| R4 | Routing logic: treat host group as local. | shall | 6.2 |
| R5 | Loopback copy if host is member of destination group on outgoing interface, unless inhibited. | shall | 6.2 |
| R6 | Source address shall be individual address of outgoing interface. | shall | 6.2 |
| R7 | Host group address never in source field or route options. | must not | 6.2 |
| R8 | Ethernet mapping: low‑order 23 bits of IP to low‑order 23 bits of 01‑00‑5E‑00‑00‑00. | shall | 6.4 |
| R9 | Provide JoinHostGroup and LeaveHostGroup operations. | shall | 7.1 |
| R10 | Join/Leave non‑blocking, report success/failure. | shall | 7.1 |
| R11 | Maintain per‑interface membership list. | shall | 7.2 |
| R12 | Discard datagrams for groups not joined, no error report. | shall | 7.2 |
| R13 | Discard datagrams arriving on interface where group not joined. | shall | 7.2 |
| R14 | Do not reject datagram because TTL=1. | shall | 7.2 |
| R15 | Discard datagram with host group source address. | shall | 7.2 |
| R16 | No ICMP error for datagrams to host groups. | shall | 7.2 |
| R17 | Reference count memberships, notify local network on first join/last leave. | shall | 7.2 |
| R18 | Implement IGMP per Appendix I (Level 2). | shall | 7.2 |
| R19 | Join all‑hosts group on each interface at init, remain member while active. | shall | 7.2 |
| R20 | Provide JoinLocalGroup and LeaveLocalGroup at local network interface. | shall | 7.3 |
| R21 | May ignore LeaveLocalGroup, may oversupply packets. | may | 7.3 |
| R22 | Must not loop back locally transmitted multicast packets. | must not | 7.3 |
| R23 | Ethernet module shall receive packets for mapped multicast addresses; must handle arbitrary number of addresses. | shall | 7.4 |