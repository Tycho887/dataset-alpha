# RFC 1075: Distance Vector Multicast Routing Protocol
**Source**: Network Working Group | **Version**: 1 | **Date**: November 1988 | **Type**: Experimental
**Original**: https://datatracker.ietf.org/doc/html/rfc1075

## Scope (Summary)
This RFC specifies an experimental distance-vector-style routing protocol (DVMRP) for routing multicast datagrams through an internet, derived from RIP and implementing multicasting per RFC 1054. It is an interior gateway protocol suitable for use within an autonomous system and is not recommended for implementation at this time.

## Normative References
- [1] Hedrick, C., "Routing Information Protocol", RFC 1058, June 1988.
- [2] Deering, S., "Host Extensions for IP Multicasting", RFC 1054, May 1988.
- [3] Deering, S., "Multicast Routing in Internetworks and Extended LANs", SIGCOMM Summer 1988 Proceedings, August 1988.
- [4] Callon, R., "A Comparison of 'Link State' and 'Distance Vector' Routing Algorithms", DEC, November 1987.
- [5] Postel, J., "Internet Protocol", RFC 791, September 1981.
- [6] Mills, D., "Toward an Internet Standard Scheme for Subnetting", RFC 940, April 1985.

## Definitions and Abbreviations
- **DVMRP**: Distance Vector Multicast Routing Protocol.
- **IGMP**: Internet Group Management Protocol.
- **TRPB**: Truncated Reverse Path Broadcasting.
- **RPB**: Reverse Path Broadcasting.
- **RPM**: Reverse Path Multicasting.
- **Virtual interface**: a physical interface or a tunnel local end-point.
- **Virtual network**: a physical network or a tunnel (routes only reference physical networks).
- **Parent router**: the router responsible for forwarding datagrams onto a virtual network through its connecting virtual interface.
- **Child virtual network**: a virtual network for which the router is the parent.
- **Leaf network**: a virtual network that is not used as an uptree path to any source by any other router.
- **Poisoned split horizon**: sending a route with metric equal to infinity and appropriate flag set in FLAGS0 command when the route is being sent on the network that is the next hop.
- **Tunnel**: a method for sending datagrams between routers separated by non-multicast gateways, using a weak encapsulation with a two-element IP loose source route.

## Protocol Description
DVMRP uses IGMP to exchange routing datagrams. DVMRP messages consist of a fixed-length IGMP header and a stream of tagged data commands.

### IGMP Header of DVMRP Messages
- **Version**: 1.
- **Type**: 3.
- **Subtype**: one of:
  - 1 = Response (provides routes).
  - 2 = Request (requests routes).
  - 3 = Non-membership report (provides NMRs).
  - 4 = Non-membership cancellation (cancels previous NMRs).
- **Checksum**: 16-bit one's complement of one's complement sum of entire message (excluding IP header); checksum field zeroed for computation.
- Message length limited to 512 bytes (excluding IP header).
- Commands are multiples of 16 bits; stream organized as 8-bit command code with at least 8-bit data portion.
- **Error handling**: A message with an error is discarded at the point of detection; state changed before the error is not restored.
- **Defaults**: Cautious implementation shall not send messages that depend on defaults, as defaults may change.

### Command Specifications

### 3.1 NULL Command (Code 0)
- **Format**: 8-bit code 0, 8-bit ignored.
- **Purpose**: Additional alignment or padding to 32 bits.

### 3.2 Address Family Indicator (AFI) Command (Code 2)
- **Format**: Code 2, family value (default = 2 for IP, 32-bit addresses).
- **Purpose**: Provides address family for subsequent addresses until a different AFI command is given.
- **Error**: If the receiver does not support the address family.

### 3.3 Subnetmask Command (Code 3)
- **Format**: Code 3, count (0 or 1), and if count=1, additional 32-bit subnet mask.
- **Default**: count=0 means following routes are to networks; use network mask of each route's destination.
- **Requirements**: Bits 0-7 of subnet mask shall be 1; all bits must not be 1.
- **Error**: count not 0 or 1.
- **Note**: Subnetmasks should not be sent outside the appropriate network.

### 3.4 Metric Command (Code 4)
- **Format**: Code 4, value (unsigned 1-255).
- **Default**: None.
- **Description**: Provides metric for subsequent destinations, relative to the sending router.
- **Error**: metric equal to 0.

### 3.5 Flags0 Command (Code 5)
- **Format**: Code 5, value (bits: 7 = destination unreachable, 6 = split horizon concealed route).
- **Default**: All bits zero.
- **Description**: Provides flags for routes. Unsupported flags shall be ignored. Experimental and may change.

### 3.6 Infinity Command (Code 6)
- **Format**: Code 6, value (unsigned 1-255).
- **Default**: 16.
- **Description**: Defines infinity for subsequent metrics.
- **Error**: infinity zero or less than current metric.

### 3.7 Destination Address (DA) Command (Code 7)
- **Format**: Code 7, count (1-255), array of count destination addresses (length depends on AFI).
- **Default**: None.
- **Description**: Provides list of destinations. Combined with current metric, infinity, flags0, subnetmask to define a route. Routing algorithm only supports network/subnetwork routing.
- **Error**: count = 0.

### 3.8 Requested Destination Address (RDA) Command (Code 8)
- **Format**: Code 8, count (0-255), array of count requested destination addresses.
- **Default**: None.
- **Description**: Lists destinations for which routes are requested. count=0 requests all routes.

### 3.9 Non Membership Report (NMR) Command (Code 9)
- **Format**: Code 9, count (1-255), array of count pairs (multicast address, 32-bit hold down time in seconds).
- **Default**: None.
- **Description**: Experimental. Tells receiving router that sending router has no descendent group members for the given multicast group. Receiving router can stop forwarding datagrams for that group. Hold down time indicates validity of NMR.
- **Error**: count = 0.
- **Allowed commands in same message**: AFI, flags0, NULL only.

### 3.10 Non Membership Report Cancel (NMR Cancel) Command (Code 10)
- **Format**: Code 10, count (1-255), array of count multicast addresses.
- **Default**: None.
- **Description**: Experimental. Cancels previous NMRs for each listed multicast address. If no corresponding NMR exists, the Cancel command shall be ignored for that address.
- **Error**: count = 0.
- **Allowed commands in same message**: AFI, flags0, NULL only.

### Summary of Commands (per 3.13)
| Code | Name        | Other commands allowed in same message                                                                 |
|------|-------------|-------------------------------------------------------------------------------------------------------|
| 0    | Null        | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA, RDA, NMR, NMR-cancel                           |
| 2    | AFI         | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA, RDA, NMR, NMR-cancel                           |
| 3    | Subnetmask  | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA, RDA                                            |
| 4    | Metric      | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA                                                 |
| 5    | Flags0      | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA                                                 |
| 6    | Infinity    | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA                                                 |
| 7    | DA          | Null, AFI, Subnetmask, Metric, Flags0, Infinity, DA                                                 |
| 8    | RDA         | Null, AFI, Subnetmask, Flags0, RDA                                                                  |
| 9    | NMR         | Null, AFI, Flags0, NMR                                                                              |
| 10   | NMR-cancel  | Null, AFI, Flags0, NMR-cancel                                                                       |

## Tunnels
Tunnels allow sending datagrams between routers separated by non-multicast gateways using a weak encapsulation with a two-element IP loose source route (LSRR).  
- A tunnel has local end-point, remote end-point, metric, and threshold.  
- To send: insert null IP option for alignment, then two-element LSRR option; set source route pointer to second element; first LSRR address = original IP source; second LSRR address = original IP multicast destination; IP source = local tunnel end-point; IP destination = remote tunnel end-point; transmit as unicast.  
- On reception: replace IP source with first LSRR address, IP destination with second LSRR address; remove null and LSRR options; adjust IP header length.  
- ICMP errors go to originating multicast router, not original host.  
- Routers at each end need only agree on local and remote end-points.  
- Routing messages shall be exchanged through tunnels as unicast datagrams directly to remote end-point (no LSRR).  
- No route is created for a tunnel.  

## Routing Algorithm
DVMRP uses a distance-vector algorithm with TRPB for forwarding. Only network/subnetwork routing is supported.

### Route Entry Fields
- Destination address (source of multicast datagrams)*
- Subnet mask of destination address*
- Next-hop router
- Virtual interface to next-hop router*
- List of child virtual interfaces*
- List of leaf virtual interfaces*
- Dominant router address per virtual interface
- Subordinate router address per virtual interface
- Timer
- Flags
- Metric
- Infinity  
(* used directly by forwarding algorithm)

### Sending Routing Messages
- **FULL_UPDATE_RATE** (60s): A router **shall** send all routing information to all virtual interfaces. Use real-time timer to avoid synchronization.
- **Triggered updates**: When a route changes, a routing update **should** be sent, with at least **TRIGGERED_UPDATE_RATE** (5s) between triggered updates.
- **Restart**: Request for all routes **shall** be sent on all virtual interfaces when router is restarted.
- **Termination**: If possible, router **should** send routes with metrics = infinity on all virtual interfaces.
- To physical interfaces: IP TTL=1; multicast to **224.0.0.4**; if multicasting not supported, use broadcast.
- To tunnels: unicast to remote end-point.
- **Poisoned split horizon**: **must** be done when sending routing messages (except in response to specific RDA with non-zero count). Route using network X sent on network X must have metric = infinity and appropriate FLAGS0 flag.
- **Threshold**: Configuration option for physical interfaces and tunnels; threshold restricts which multicast datagrams exit a network.
- **Startup**: Router must send request for all routes (RDA count=0) on each virtual interface.

### Receiving Routing Messages
- Router **must** know the virtual interface on which a routing message arrived.
- For each route in message:
  - If metric given, add metric of incoming virtual interface.
  - Look up destination address in routing tables.
  - If route does not exist: try to find route to same network. If found and from same router as the new route, skip. If route metric not infinity, add route.
  - If route exists and from same router: clear timer; if metric different, update metric and infinity; if metric = infinity, set timer to **EXPIRATION_TIMEOUT**; if infinity different, update and adjust metric.
  - If route exists and from different router: if received metric is less than existing metric, or (route timer half expired and metrics equal and metric less than received infinity), then update route, clear timer.

### Neighbors
- List of neighboring multicast routers **should** be kept per attached network.
- Neighbor not heard from in **NEIGHBOR_TIMEOUT** (240s) **should** be considered down.

### Local Group Memberships
- Router **must** track group memberships on multicast-capable networks per [2].
- Every **QUERY_RATE** (120s): designated router on each network **shall** send IGMP membership request to All Hosts (224.0.0.1) with IP TTL=1.
- Designated router: router with lowest IP address on that network. Upon startup, router considers itself designated until it learns of a lower address.
- At startup: router **should** multicast three membership requests separated by 4 seconds.
- Router **must** receive all datagrams to all multicast addresses. Upon receiving IGMP membership report, **shall** record group and interface with timestamp, or update timestamp if already recorded.
- Recorded groups **must** be timed out after **MEMBERSHIP_TIMEOUT** (260s).

## Forwarding Algorithm
The algorithm determines how multicast datagrams arriving on a virtual interface are handled, using child and leaf lists to prune the tree.

### Manipulation of Children and Leaf Lists
- **Upon router startup**: Create route entry per virtual interface with all other interfaces in child list; empty leaf list; no dominant or subordinate routers. Start hold down timer for each interface with **LEAF_TIMEOUT** (125s).
- **Upon receiving a new route**: Create entry with all interfaces (except incoming) in child list; empty leaf; no dominant/subordinate. Start hold down timer for all other interfaces with LEAF_TIMEOUT.
- **Upon receiving a route on V from N with lower metric (or same metric if N's address < my address for V)**: If V in child list, delete V from child list. If no dominant router for V and V not next-hop, record N as dominant router.
- **Upon receiving a route on V from N with larger metric (or same metric if N's address > my address for V)**: If N is dominant router for V, delete N as dominant and add V to child list.
- **Upon receiving a route from N on V with metric = infinity and split horizon flag set**: If V in leaf list, delete V from leaf list. If no subordinate router for V, record N as subordinate router.
- **Upon receiving a route from N on V with metric != infinity (no split horizon flag)**: If N is subordinate router for V, delete N as subordinate and start hold down timer for V.
- **Upon timer expiration for V (per route)**: If no subordinate router for V, add V to leaf list.
- **Upon failure of neighbor N on V (per route)**: If N is dominant, delete and add V to child list. If N is subordinate, delete and start hold down timer for V.

### Forwarding Algorithm Steps
1. If IP TTL < 2, skip datagram.
2. Find route to source of IP datagram. If no route exists, skip.
3. If datagram not received on next-hop virtual interface for route, skip.
4. If datagram is tunneled: replace source with first LSRR address, destination with second; delete LSRR and null option; adjust IP header length.
5. If destination is group 224.0.0.0 or 224.0.0.1, skip.
6. For each virtual interface V:
   - If V in child list for source:
     - If V not in leaf list for source OR there are members of destination group on V:
       - If IP TTL > V's threshold: subtract 1 from TTL, forward datagram out V.

## Time Values (all in seconds)
| Parameter                  | Value | Description                                                                 |
|----------------------------|-------|-----------------------------------------------------------------------------|
| FULL_UPDATE_RATE          | 60    | Interval for complete routing updates.                                      |
| TRIGGERED_UPDATE_RATE     | 5     | Minimum interval between triggered updates.                                 |
| QUERY_RATE                | 120   | Interval for IGMP membership queries.                                       |
| MEMBERSHIP_TIMEOUT        | 260   | Local group membership validity without confirmation (2×QUERY_RATE+20).     |
| LEAF_TIMEOUT              | 125   | Hold down timer for virtual interface (2×FULL_UPDATE_RATE+5).               |
| NEIGHBOR_TIMEOUT          | 240   | Neighbor considered up without confirmation (4×FULL_UPDATE_RATE).           |
| EXPIRATION_TIMEOUT        | 120   | Route valid without confirmation (2×FULL_UPDATE_RATE). After expiry, packets not forwarded, route metric set to infinity. |
| GARBAGE_TIMEOUT           | 240   | Route exists without confirmation (4×FULL_UPDATE_RATE). After expiry, route deleted. |

## Configuration Options
- **Tunnel**: local end-point, remote end-point, metric, and threshold (default = metric).
- **Physical interface**: metric, infinity, threshold, and subnetwork mask (default threshold = metric).

## Requirements Summary
| ID  | Requirement                                                                                          | Type   | Reference        |
|-----|------------------------------------------------------------------------------------------------------|--------|------------------|
| R1  | Message length shall be ≤512 bytes (excluding IP header).                                            | shall  | §3               |
| R2  | Checksum shall be 16-bit one's complement of one's complement sum; checksum field zeroed for computation. | shall | §3               |
| R3  | Cautious implementation shall not send messages that depend on defaults.                             | shall  | §3               |
| R4  | Router must send request for all routes on each virtual interface upon startup.                      | shall  | §5.1             |
| R5  | Poisoned split horizon must be done when sending routing messages (except response to specific RDA). | shall  | §5.1             |
| R6  | Router must know the virtual interface on which a routing message arrived.                           | shall  | §5.2             |
| R7  | Router must track local group memberships per [2].                                                   | shall  | §5.4             |
| R8  | Designated router shall send IGMP membership request to All Hosts every QUERY_RATE seconds with TTL=1. | shall | §5.4             |
| R9  | Upon receiving IGMP membership report, router shall record group and interface with timestamp.       | shall  | §5.4             |
| R10 | Recorded groups must be timed out after MEMBERSHIP_TIMEOUT.                                          | must   | §5.4             |
| R11 | In tunneling, routing messages shall be sent as unicast to remote end-point (no LSRR).               | shall  | §4               |
| R12 | Subnet mask bits 0-7 shall be 1; all bits must not be 1.                                            | shall  | §3.3             |
| R13 | It is an error for Metric command value to equal 0.                                                  | shall  | §3.4             |
| R14 | It is an error for Infinity command value to be zero or less than current metric.                    | shall  | §3.6             |
| R15 | It is an error for DA command count to equal 0.                                                      | shall  | §3.7             |
| R16 | It is an error for NMR command count to equal 0.                                                     | shall  | §3.9             |
| R17 | It is an error for NMR Cancel command count to equal 0.                                              | shall  | §3.10            |
| R18 | Unsupported flags in Flags0 command shall be ignored.                                                | shall  | §3.5             |
| R19 | Receiver not supporting AFI shall result in error.                                                   | shall  | §3.2             |
| R20 | When NMR Cancel has no corresponding NMR, cancel shall be ignored for that address.                  | shall  | §3.10            |

## Informative Annexes (Condensed)
- **Examples (§3.12)**: Provide byte-sequence examples for route supply, request, and NMR messages. These illustrate command usage but are non-normative.
- **Tunnel Justification (§4)**: Explains why LSRR option is used for tunneling: to avoid new IP option that would be blocked by intermediate gateways, and to enable detection by destination gateway via multicast address in LSRR.
- **Conclusion (§9)**: States DVMRP is implemented and being tested; notes that a link-state multicast routing protocol should be developed; TRPB can cause inefficiencies; RPM may be better.