# RFC 1058: Routing Information Protocol
**Source**: Network Working Group | **Version**: 1 (June 1988) | **Date**: June 1988 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc1058

## Scope (Summary)
This RFC documents the Routing Information Protocol (RIP), a distance-vector interior gateway protocol for exchanging routing information among hosts and gateways in IP-based networks. It defines message formats, algorithms, timers, and procedures to maintain consistent routing tables. The protocol is limited to networks with a maximum path length of 15 hops and is intended for moderate-sized, homogeneous networks.

## Normative References
- [3] Braden, R., and Postel, J., "Requirements for Internet Gateways", RFC-1009, June 1987.
- [5] Clark, D. D., "Fault Isolation and Recovery", RFC-816, July 1982.
- Bellman, R. E., "Dynamic Programming", Princeton University Press, 1957.
- Bertsekas, D. P., and Gallaher, R. G., "Data Networks", Prentice-Hall, 1987.
- Ford, L. R. Jr., and Fulkerson, D. R., "Flows in Networks", Princeton University Press, 1962.
- Xerox Corp., "Internet Transport Protocols", XSIS 028112, December 1981.
- Boggs, D. R., et al., "Pup: An Internetwork Architecture", IEEE Trans. Comm., April 1980.

## Definitions and Abbreviations
- **RIP**: Routing Information Protocol, a distance-vector protocol using UDP port 520.
- **Distance vector algorithm**: An algorithm where each node computes routes based on distances (metrics) reported by neighbors.
- **Metric**: A integer cost (1–15) representing total distance to a destination; 16 indicates infinity (unreachable).
- **Split horizon**: A technique to avoid routing loops by not advertising a route back to the neighbor from which it was learned (simple), or by advertising it with metric 16 (poisoned reverse).
- **Triggered update**: An update sent immediately after a metric change, with optional delay of 1–5 seconds.
- **Timeout**: 180 seconds after last update; route is marked invalid.
- **Garbage-collection timer**: 120 seconds after invalidation; route is deleted.
- **Infinity**: Metric value 16, larger than any valid metric.
- **IGP**: Interior Gateway Protocol.
- **UDP**: User Datagram Protocol.

## 1. Introduction
RIP is based on the Bellman-Ford (distance vector) algorithm. It is widely used as an interior gateway protocol (IGP) for small to moderate networks. The protocol is derived from the “routed” program in 4BSD and the Xerox Network Systems (XNS) Routing Information Protocol. It is intended for IP-based internetworks.

### 1.1. Limitations of the Protocol
- **Maximum path length**: 15 hops; metric 16 means unreachable.
- **Counting to infinity**: May require significant time or bandwidth in large routing loops.
- **Fixed metrics**: Not suitable for real-time parameters such as delay, reliability, or load.

### 1.2. Organization of this Document
The document has two main parts: Section 2 provides conceptual background on distance vector algorithms; Section 3 contains the actual protocol specification.

## 2. Distance Vector Algorithms
### 2.1. Dealing with Changes in Topology
- Routes are timed out after 180 seconds of inactivity.
- When a gateway fails, its neighbors mark the route as invalid by setting metric to infinity (16).

### 2.2. Preventing Instability
#### 2.2.1. Split Horizon
- **Simple split horizon**: Omit routes learned from a neighbor in updates sent to that neighbor.
- **Split horizon with poisoned reverse**: Include those routes with metric set to infinity (16).
- Implementors **may** at their option implement simple split horizon or split horizon with poisoned reverse, or provide a configuration option. Hybrid schemes are also permitted.

#### 2.2.2. Triggered Updates
- When a metric changes, a gateway **must** send update messages almost immediately.
- A **small random delay (1–5 seconds)** **should** be imposed to avoid excessive network traffic.

## 3. Specifications for the Protocol
### 3.1. Message Formats
- RIP uses UDP port 520.
- Packet format (see Figure 1): command (1 octet), version (1), must be zero (2), then up to 25 entries each with address family identifier (2), must be zero (2), IP address (4), must be zero (4), must be zero (4), metric (4).
- Metrics: 1–15 valid; 16 = infinity (unreachable).
- Maximum datagram size: 512 octets (excluding IP/UDP headers).
- Commands: 1 (request), 2 (response), 3 (traceon – ignore), 4 (traceoff – ignore), 5 (reserved for Sun).
- Address family identifier for IP is 2.
- Implementations **must** skip entries with unsupported address families.

### 3.2. Addressing Considerations
- Destinations can be host addresses, subnet numbers, network numbers, or 0.0.0.0 (default route).
- Hosts **must** use the most specific route when forwarding.
- Subnet routes **must not** be sent outside the subnetted network unless special provisions are made.
- Border gateways **must** send only a single entry for the whole network to neighbors on other networks.
- Default route (0.0.0.0) is optional but strongly recommended; implementations that do not support it **must** ignore entries with that address.

### 3.3. Timers
- **Regular update**: Every 30 seconds. Implementation **must** take precautions to prevent synchronization (e.g., random offset).
- **Timeout**: 180 seconds after last update; route is invalidated.
- **Garbage collection**: 120 seconds after invalidation; route is deleted.
- During garbage collection, the route is included in updates with metric 16.

### 3.4. Input Processing
- Datagrams with version 0 **must be ignored**. Version 1: check "must be zero" fields; if non-zero, ignore entire message. Version >1: ignore "must be zero" fields.
- Requests from port 520 are broadcast; silent processes do not respond unless request comes from a non-520 port.
- **Special request**: One entry with address family 0 and metric 16 causes the entire routing table to be sent (with split horizon and subnet filtering).
- For responses, validate: source port must be 520; source IP must be on a directly-connected network; ignore own broadcasts.
- Processing entries:
  - Ignore if metric > 16.
  - Ignore if address family not IP (2).
  - Ignore class D/E, net 0 (except default), net 127, broadcast addresses.
  - Optionally ignore host routes (with non-zero host part) if host routes not supported.
  - Update metric: `metric = MIN(metric + cost, 16)`.
  - If new route: add if metric < 16 and not subsumed by network route.
  - If existing route from same gateway: adopt new metric, reinitialize timeout, trigger update if metric changed.
  - If new metric is 16, start deletion (set metric to 16, garbage timer 120s, trigger update).
  - If same metric and different gateway: optionally switch if existing route timeout ≥ 90s (180s/2) – optional heuristic.

### 3.5. Output Processing
- Responses generated for requests, regular updates (every 30s), and triggered updates.
- For regular and triggered updates: send to each neighbor (point-to-point) or broadcast on each network.
- Triggered updates:
  - **Must** be delayed by a random time between 1 and 5 seconds.
  - If a regular update is due, triggered update may be suppressed.
  - **Must** include at least routes with route change flag set; may include all routes.
  - Split horizon applies.
- For each network, IP source address **must** be the host’s address on that network.
- Subnet routes **must** be omitted outside the subnetted network; replace with network route.
- Host routes subsumed by network route **must** be omitted.
- Routes with metric infinity are included unless split horizon omits them.
- If split horizon with poisoned reverse is used, metric set to 16 for routes learned from that network.

### 3.6. Compatibility
- The document adopts a different viewpoint on metric increment (cost added on receipt, not on sending) but results in identical update messages. Implementations that only support cost 1 need not change but **must** follow all other specifications.

## 4. Control Functions (Optional)
The following administrative controls are strongly recommended but not required:
- **Neighbor list**: Accept responses only from listed neighbors.
- **Allow/Disallow destinations**: Specify lists of destination addresses per interface for incoming or outgoing updates.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | RIP must use UDP port 520 for all communications to the RIP process. | shall | 3.1 |
| R2 | Update messages must be sent every 30 seconds. | shall | 3.3 |
| R3 | A route is timed out after 180 seconds without update. | shall | 3.3 |
| R4 | The garbage-collection timer must be 120 seconds after invalidation. | shall | 3.3 |
| R5 | The maximum metric value is 15; value 16 denotes infinity (unreachable). | shall | 2.2, 3.1 |
| R6 | Triggered updates must include a random delay of 1–5 seconds. | shall | 3.5 |
| R7 | Subnet routes must not be sent outside the subnetted network unless special provisions are made. | shall | 3.2 |
| R8 | Border gateways must send only a single network route to neighbors on other networks. | shall | 3.2 |
| R9 | Datagrams with version 0 must be ignored. | shall | 3.4 |
| R10 | Responses from port other than 520 must be ignored. | shall | 3.4.2 |
| R11 | The IP source address of a RIP response must be the sender’s address on the network. | shall | 3.5 |
| R12 | Implementations may implement simple split horizon or split horizon with poisoned reverse. | may | 2.2.1 |
| R13 | Default route (0.0.0.0) is optional but strongly recommended. | should | 3.2 |
| R14 | Triggered updates must include at least the routes whose change flag is set. | shall | 3.5 |

## Informative Annexes (Condensed)
- **Bibliography**: Provides references to foundational works on dynamic programming (Bellman), data networks (Bertsekas & Gallaher), Internet gateway requirements (RFC-1009), fault isolation (RFC-816), the PUP internetwork architecture, and the Xerox XNS protocol. These are informative background sources for understanding the distance vector algorithm and the context of RIP.