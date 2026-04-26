# RFC 4601: Protocol Independent Multicast - Sparse Mode (PIM-SM): Protocol Specification (Revised)
**Source**: Internet Engineering Task Force (IETF) – Standards Track | **Version**: 1.0 | **Date**: August 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc4601

## Scope (Summary)
This document specifies Protocol Independent Multicast - Sparse Mode (PIM-SM), a multicast routing protocol that builds unidirectional shared trees rooted at a Rendezvous Point (RP) per group, optionally creating shortest-path trees per source. It uses the underlying unicast routing information base (MRIB) and defines state machines for Join/Prune, Register, Assert, and DR election. This revision obsoletes RFC 2362.

## Normative References
- RFC 2119 (Key words for requirements levels)
- RFC 3376 (IGMPv3)
- RFC 1112 (IP multicast host extensions)
- RFC 2710 (MLD for IPv6)
- RFC 2460 (IPv6 Specification)
- RFC 4301 (IPsec Architecture)
- RFC 2434 (IANA Considerations Guidelines)
- [RFC 4507] (SSM for IP, referenced as [6])
- [RFC 2715] (Interoperability Rules for Multicast Routing)
- [RFC 2983] (Differentiated Services and Tunnels)
- [RFC 3956] (Embedding RP in IPv6 Multicast Address)
- [RFC 4609] (PIM-SM Security Issues and Enhancements)

## Definitions and Abbreviations
- **RP**: Rendezvous Point – root of the shared tree.
- **DR**: Designated Router – elected per interface for local host membership.
- **MRIB**: Multicast Routing Information Base – used for reverse-path forwarding decisions.
- **RPF Neighbor**: Reverse Path Forwarding neighbor, the next hop toward a source or RP.
- **TIB**: Tree Information Base – all multicast distribution tree state.
- **MFIB**: Multicast Forwarding Information Base – forwarding table derived from TIB.
- **GenID**: Generation Identifier – random 32-bit value to detect reboots.
- **PMBR**: PIM Multicast Border Router – joins PIM domain with another multicast domain.
- **SPTbit(S,G)**: Boolean indicating whether (S,G) traffic is forwarded on the Shortest Path Tree.
- **KAT**: Keepalive Timer – holds (S,G) state in absence of explicit joins.
- **Assert**: Message to elect a single forwarder on a multi-access LAN.
- **SSM**: Source-Specific Multicast – uses (S,G) state only.

## 1. Introduction (Informative)
PIM-SM is a protocol for efficiently routing multicast groups across wide-area internets. It is protocol-independent and uses an MRIB. This specification corrects deficiencies in RFC 2362 and brings PIM-SM to Standards Track. Routers implementing this spec will interoperate with RFC 2362 implementations.

## 2. Terminology
Key words “MUST”, “MUST NOT”, “SHALL”, etc. are as per RFC 2119.

## 3. Protocol Overview (Informative, condensed)
PIM-SM operates in three phases:
1. **RP Tree**: DR sends (*,G) Join towards RP; data flows encapsulated to RP.
2. **Register-Stop**: RP joins (S,G) source tree; when native packets arrive, RP sends Register-Stop to DR.
3. **Shortest-Path Tree**: Last-hop DR may switch to SPT, sending (S,G,rpt) Prune towards RP.

Multi-access LANs may cause duplicate packets; resolved via Assert messages.

## 4. Protocol Specification (Normative)

### 4.1 PIM Protocol State
The TIB holds state for (*,*,RP), (*,G), (S,G), and (S,G,rpt). Each has per-interface downstream state (NoInfo, Join, Prune-Pending) and upstream state (NotJoined/Joined). Assert winner state (NoInfo, Winner, Loser) is stored per interface.

#### State Summarization Macros (Section 4.1.6)
- `immediate_olist(*,G) = joins(*,G) (+) pim_include(*,G) (-) lost_assert(*,G)`
- `inherited_olist(S,G) = inherited_olist(S,G,rpt) (+) joins(S,G) (+) pim_include(S,G) (-) lost_assert(S,G)`
- `RPF'(*,G)` and `RPF'(S,G)` define upstream neighbor, modified by Asserts.

### 4.2 Data Packet Forwarding Rules
- On receipt of data from S to G on interface iif:
  - If DirectlyConnected(S) and iif == RPF_interface(S), set KeepaliveTimer(S,G) to Keepalive_Period.
  - If iif == RPF_interface(S) and UpstreamJPState(S,G)==Joined and inherited_olist(S,G) != NULL, set KeepaliveTimer(S,G) to Keepalive_Period.
  - Update_SPTbit(S,G,iif).
  - If SPTbit(S,G)==TRUE and iif==RPF_interface(S), oiflist = inherited_olist(S,G).
  - Else if SPTbit(S,G)==FALSE and iif==RPF_interface(RP(G)), oiflist = inherited_olist(S,G,rpt) and CheckSwitchToSpt(S,G).
  - If RPF check fails, send appropriate Assert.
  - Forward packet on oiflist minus iif.

#### CheckSwitchToSpt(S,G) (Section 4.2.1)
- If pim_include(*,G) (-) pim_exclude(S,G) (+) pim_include(S,G) != NULL and SwitchToSptDesired(S,G) is TRUE, set KeepaliveTimer(S,G) to Keepalive_Period.

#### Update_SPTbit(S,G,iif) (Section 4.2.2)
- Set SPTbit to TRUE if iif==RPF_interface(S) and JoinDesired(S,G)==TRUE and one of: DirectlyConnected(S), RPF_interface(S)!=RPF_interface(RP(G)), inherited_olist(S,G,rpt)==NULL, RPF'(S,G)==RPF'(*,G) (both non-NULL), or I_Am_Assert_Loser(S,G,iif).

### 4.3 Designated Routers and Hello Messages (Section 4.3)
- **Hello messages** MUST be sent on all PIM-enabled interfaces (including point-to-point) with TTL 1 to ALL-PIM-ROUTERS (224.0.0.13 for IPv4, ff02::d for IPv6). They include Holdtime, DR Priority (SHOULD), GenID (SHOULD), LAN Prune Delay (SHOULD on multi-access), Address List (MUST if secondary addresses exist).
- **DR Election** (Section 4.3.2): Compare DR_Priority (numerically larger preferred), tie-break by highest primary IP address. Election occurs when Hello received, neighbor times out, or own priority changes.
- **LAN Prune Delay** (Section 4.3.3): Effective_Propagation_Delay and Effective_Override_Interval are negotiated; Suppression_Enabled depends on all neighbors supporting T bit.
- **Secondary Address List** (Section 4.3.4): Updated on Hello; conflicts MUST be resolved with most recent mapping.

### 4.4 PIM Register Messages (Section 4.4)
- **DR Register State Machine** (Figure 1): States Join, Prune, Join-Pending, NoInfo. On Register-Stop, transition to Prune; set Register-Stop Timer to random value in (0.5*Register_Suppression_Time, 1.5*Register_Suppression_Time) minus Register_Probe_Time. On expiry in Prune state, send Null-Register and set timer to Register_Probe_Time. `CouldRegister(S,G)` is true when I_am_DR(RPF_interface(S)), KeepaliveTimer running, and DirectlyConnected(S).
- **Register Message Content**: Encapsulated multicast packet; B bit for PMBR; N bit for Null-Register. Checksum over first 8 bytes only.
- **RP Receiving Register** (Section 4.4.2): If I_am_RP(G) and outer.dst equals RP(G): if SPTbit(S,G) or SwitchToSptDesired with NULL inherited_olist, send Register-Stop; maintain KeepaliveTimer(S,G) at RP_Keepalive_Period (3*Register_Suppression_Time + Register_Probe_Time). Otherwise, decapsulate and forward on inherited_olist(S,G,rpt). If not RP, send Register-Stop.

### 4.5 PIM Join/Prune Messages (Section 4.5)
- **General**: Join/Prune messages contain group sets with joined/pruned source lists. Upstream Neighbor Address must match router's primary IP (or all zeros for backwards compatibility). Messages from unknown neighbors SHOULD be discarded.

#### 4.5.1 Downstream (*,*,RP) State Machine (Figure 2)
- States: NoInfo, Join, Prune-Pending. Transitions: Receive Join -> Join (start ET); Receive Prune -> Prune-Pending (start PPT); Prune-Pending Timer expiry -> NoInfo (send PruneEcho); Expiry Timer expiry -> NoInfo.

#### 4.5.2 Downstream (*,G) State Machine (Figure 3)
- Same structure as (*,*,RP). Join(*,G) checked against RP(G); if mismatch, Join silently dropped (Prune still processed if no RP info, may accept).

#### 4.5.3 Downstream (S,G) State Machine (Figure 4)
- Identical to (*,G) but for source-specific.

#### 4.5.4 Downstream (S,G,rpt) State Machine (Figure 5)
- States: NoInfo, Prune, Prune-Pending, PruneTmp, Prune-Pending-Tmp. Transitions depend on receiving Join(*,G), Join(S,G,rpt), Prune(S,G,rpt). End of message event in transient states may revert to NoInfo.

#### 4.5.5 Upstream (*,*,RP) State Machine (Figure 6)
- States: NotJoined, Joined. `JoinDesired(*,*,RP)` true if immediate_olist(*,*,RP) != NULL. On JoinDesired->True: send Join, set JT to t_periodic. On False: send Prune, cancel JT. In Joined state, timer expiry, seeing Join/Prune to MRIB.next_hop(RP), neighbor change, or GenID change trigger actions (increase/decrease JT, send Join/Prune to new/old neighbor).

#### 4.5.6 Upstream (*,G) State Machine (Figure 7)
- Similar to (*,*,RP). `JoinDesired(*,G)` true if immediate_olist(*,G) != NULL OR (JoinDesired(*,*,RP(G)) AND AssertWinner(*,G,RPF_interface(RP(G))) != NULL). Extra transitions for RPF'(*,G) changes due to Assert.

#### 4.5.7 Upstream (S,G) State Machine (Figure 8)
- `JoinDesired(S,G)` true if immediate_olist(S,G) != NULL OR (KeepaliveTimer(S,G) running AND inherited_olist(S,G) != NULL). Transitions: on JoinDesired->True: send Join, set JT. On False: send Prune, set SPTbit(S,G) FALSE. In Joined state, seeing Prune(S,G,rpt) or Prune(*,G) to RPF'(S,G) will decrease JT to t_override for backwards compatibility.

#### 4.5.8 (S,G,rpt) Periodic Messages
- When sending Join(*,G), include Prune(S,G,rpt) if: SPTbit(S,G)==TRUE and RPF'(*,G) != RPF'(S,G); or inherited_olist(S,G,rpt)==NULL; or RPF'(*,G) != RPF'(S,G,rpt).

#### 4.5.9 Upstream (S,G,rpt) Triggered Messages State Machine (Figure 9)
- States: RPTNotJoined(G), Pruned(S,G,rpt), NotPruned(S,G,rpt). `PruneDesired(S,G,rpt)` true if RPTJoinDesired(G) AND (inherited_olist(S,G,rpt)==NULL OR (SPTbit(S,G)==TRUE AND RPF'(*,G) != RPF'(S,G))). Override Timer OT(S,G,rpt) used to delay Join(S,G,rpt) in response to Prune(S,G,rpt) etc. Transition rules handle override of prunes from upstream LAN peers.

#### 4.5.10 Background: (*,*,RP) and (S,G,rpt) Interaction
- Prune(S,G,rpt) required to prevent forwarding on (*,*,RP). To prune off (*,*,RP), a Join(*,G) must also be sent. No Assert(*,*,RP) exists. Triggered (S,G,rpt) messages may be sent when only (*,*,RP) state is present.

### 4.6 PIM Assert Messages (Section 4.6)
- **Asserts** are used to elect a single forwarder on a multi-access LAN. Assert messages SHOULD be discarded if sender is not a known PIM neighbor (Hello not received). If Hello was authenticated with IPsec AH, all Asserts MUST also be authenticated.

#### 4.6.1 (S,G) Assert State Machine (Figure 10)
- States: NoInfo (NI), I am Assert Winner (W), I am Assert Loser (L).
- `CouldAssert(S,G,I)` true if SPTbit(S,G)==TRUE, RPF_interface(S) != I, and I in appropriate olist components.
- `AssertTrackingDesired(S,G,I)` true if interface in join/prune/local membership sets, or if RPF_interface(S)==I and JoinDesired(S,G)==TRUE, or RPF_interface(RP(G))==I and JoinDesired(*,G)==TRUE and SPTbit==FALSE.
- Transitions: On receiving inferior assert with RPTbit=0 and CouldAssert, or data trigger, go to W (actions A1: send Assert, set AT to Assert_Time - Assert_Override_Interval). On receiving acceptable assert with RPTbit=0 and AssertTrackingDesired, go to L (actions A6). In W: timer expiry -> resend Assert; inferior assert -> resend; preferred assert -> go to L; CouldAssert->FALSE -> go to NI (send AssertCancel). In L: preferred assert -> stay L; acceptable from winner -> stay L; inferior/AssertCancel from winner -> go to NI; timer expiry, winner GenID change, AssertTrackingDesired->FALSE, my metric better, RPF_interface(S) changes, or Receive Join(S,G) -> go to NI.

#### 4.6.2 (*,G) Assert State Machine (Figure 11)
- Similar to (S,G) but for (*,G). NO TRANSITION occurs if (S,G) state machine changed state due to same message. `CouldAssert(*,G,I)` true if I in joins(*,*,RP(G)) (+) joins(*,G) (+) pim_include(*,G) and RPF_interface(RP(G)) != I.
- Actions similar to (S,G) but use `rpt_assert_metric`.

#### 4.6.3 Assert Metrics
- `assert_metric { rpt_bit_flag, metric_preference, route_metric, ip_address }`. Comparison: lower value wins order of first three fields, tie break by higher IP address.
- `my_assert_metric(S,G,I)`: if CouldAssert(S,G,I) -> spt_assert_metric; else if CouldAssert(*,G,I) -> rpt_assert_metric; else infinite.
- `spt_assert_metric(S,I) = {0, MRIB.pref(S), MRIB.metric(S), my_ip_address(I)}`
- `rpt_assert_metric(G,I) = {1, MRIB.pref(RP(G)), MRIB.metric(RP(G)), my_ip_address(I)}`

#### 4.6.4 AssertCancel Messages
- AssertCancel(S,G) is an infinite metric assert with RPT bit set naming S. AssertCancel(*,G) is infinite metric with source zero. Sent by winner when forwarding state deleted.

#### 4.6.5 Assert State Macros
- `lost_assert(S,G,rpt,I)`: true if (RPF_interface(RP(G)) != I AND (RPF_interface(S) != I OR SPTbit==FALSE)) AND AssertWinner(S,G,I) != NULL and not me.
- `lost_assert(S,G,I)`: true if RPF_interface(S) != I AND AssertWinner(S,G,I) != NULL and not me AND AssertWinnerMetric better than spt_assert_metric.
- `lost_assert(*,G,I)`: true if RPF_interface(RP(G)) != I AND AssertWinner(*,G,I) != NULL and not me.

### 4.7 Bootstrap and RP Discovery (Section 4.7)
- Group-to-RP mapping uses longest match on group-range, then highest priority, then hash function. Four mechanisms: Static Configuration (MUST support), Embedded-RP, Auto-RP, BSR. BSR hash function: Value = (1103515245 * ((1103515245*(G&M)+12345) XOR C(i)) + 12345) mod 2^31. Higher hash value wins; tie by highest IP address.

### 4.8 Source-Specific Multicast (Section 4.8)
- For SSM addresses (232.0.0.0/8 IPv4, FF3x::/32 IPv6): MUST NOT send (*,G) or (S,G,rpt) Joins/Prunes; MUST NOT forward based on (*,G) or (S,G,rpt); MUST NOT send Register for SSM; RP MUST NOT forward Register-encapsulated SSM packets.
- PIM-SSM-only routers implement only (S,G) upstream/downstream state machines, (S,G) Assert, Hello/DR election, packet forwarding. Keepalive always running, SPTbit always set.

### 4.9 PIM Packet Formats (Section 4.9)
#### Common Header:
- PIM Ver=2, Type (0-8), Reserved, Checksum (standard IP checksum; for IPv6 includes pseudo-header).
- Checksum for Register only over first 8 bytes.

#### Hello Message Format (Section 4.9.2):
- Options: Holdtime (Type=1), LAN Prune Delay (Type=2, 4 bytes), DR Priority (Type=19, 4 bytes), GenID (Type=20, 4 bytes), Address List (Type=24, variable). Options 3-16 reserved, 17-65000 assigned IANA.

#### Register Message Format (Section 4.9.3):
- Fields: B bit, N bit, Reserved2, Multicast data packet. Null-Register includes dummy IP/PIM header.

#### Register-Stop Message Format (Section 4.9.4):
- Contains Group Address and Source Address (Encoded-Unicast). Source may be all zeros for wildcard.

#### Join/Prune Message Format (Section 4.9.5):
- Fields: Upstream Neighbor Address, Holdtime, Number of Groups, then group sets. Each group set: Multicast Group Address, Number of Joined Sources, Joined Source Addresses, Number of Pruned Sources, Pruned Source Addresses.
- Source list entries use Encoded-Source Address with WC and RPT bits.
- Rules for valid combinations in Group Set (Section 4.9.5.1): Wildcard Group Set (*,*,RP) or Group-Specific Set (*,G), (S,G,rpt), (S,G). Invalid combinations MUST NOT be generated; MAY be accepted but undefined.
- **Group Set Fragmentation** (Section 4.9.5.2): If (*,G) Join included, all (S,G,rpt) Prunes MUST be in same message; if too many, include first N numerically smallest in network byte order.

#### Assert Message Format (Section 4.9.6):
- Fields: Group Address, Source Address (zero for (*,G)), RPT bit, Metric Preference, Metric.

### 4.10 PIM Timers (Section 4.10)
List of global per-interface, per-neighbor, per-RP, per-group, per-source timers including Hello, Neighbor Liveness, Expiry, Prune-Pending, Assert, Upstream Join, Keepalive, Register-Stop, Override.

### 4.11 Timer Values (Section 4.11)
- Hello_Period: 30s, Triggered_Hello_Delay: 5s.
- Default_Hello_Holdtime: 105s (3.5 * Hello_Period).
- J/P_Holdtime: from message (typically 3.5 * t_periodic).
- J/P_Override_Interval(I): Effective_Propagation_Delay(I) + Effective_Override_Interval(I).
- Assert_Override_Interval: 3s, Assert_Time: 180s.
- t_periodic: 60s; t_suppressed: rand(1.1*t_periodic, 1.4*t_periodic) if suppression enabled, else 0; t_override: rand(0, Effective_Override_Interval).
- Keepalive_Period: 210s; RP_Keepalive_Period: (3*Register_Suppression_Time) + Register_Probe_Time.
- Register_Suppression_Time: 60s; Register_Probe_Time: 5s.

## 5. IANA Considerations
- PIM Address Family: values 0-127 same as IANA Address Family Numbers; 128-250 assigned by IANA via IESG Approval; 251-255 Private Use.
- PIM Hello Options: values 17-65000 assigned by IANA (First Come First Served, temporary 1 year, permanent requires specification).

## 6. Security Considerations (Condensed)
- **Forged Link-Local Messages**: Join/Prune/Hello/Asserts only affect LAN; can waste bandwidth or disrupt forwarding. Hello forgery can change DR. Assert forgery can stop forwarding.
- **Forged Unicast Messages**: Register forgery injects forged traffic; Register-Stop forgery prevents encapsulation.
- **Non-Cryptographic Authentication**: SHOULD restrict neighbor set; MUST NOT accept messages before Hello; address validation for Register/Register-Stop; SHOULD provide source restriction on RP.
- **IPsec Authentication**: RECOMMENDED for integrity and authentication. Use AH transport mode. For link-local messages, same SA per link. For unicast (Register/Register-Stop), may use shared key for simplicity.
- **Denial-of-Service**: Sending many packets to different groups can overload DR/RP; forged joins can build trees. (*,*,RP) joins can cause domain-wide traffic to PMBR – consider security.

## 7. Acknowledgements (Informative)
- Condensed: PIM-SM designed by many contributors including D. Estrin, D. Farinacci, A. Helmy, D. Thaler, S. Deering, V. Jacobson, and others.

## 8. Normative References (List as above)

## 9. Informative References
- [10] Bates et al., RFC 2858.
- [11] Bhaskar et al., BSR Mechanism (work in progress).
- [12] Black, RFC 2983.
- [13] Handley et al., Bidirectional PIM (work in progress).
- [14] Kaufman, RFC 4306.
- [15] Savola et al., RFC 4609.
- [16] Savola and Lingard, Last-hop threats (work in progress).
- [17] Savola and Haberman, RFC 3956.
- [18] Thaler, RFC 2715.

## Appendix A: PIM Multicast Border Router Behavior (Condensed)
- PMBR interconnects PIM and non-PIM domains. For external sources, acts as DR with Border bit set. For internal sources, may send (*,*,RP) Joins or explicit (S,G) joins based on RFC 2715. State changes through discard interface. Pruning off (*,*,RP) requires joining (*,G) and pruning each source.

## Appendix B: Index (Informative)
- Index of terms and their section references (not reproduced in full).

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Hello messages MUST be sent on all active interfaces (including point-to-point). | shall | Section 4.3.1 |
| R2 | DR election MUST be performed on ALL active PIM-SM interfaces. | shall | Section 4.3.2 |
| R3 | A router MUST send Hello immediately if it needs to send Join/Prune/Assert on an interface where it has not yet sent Hello. | shall | Section 4.3.1 |
| R4 | If Hello from neighbor was authenticated via IPsec AH, all Join/Prune/Assert from that neighbor MUST also be authenticated. | shall | Section 4.5, 4.6 |
| R5 | Register-Stop(*,G) messages SHOULD NOT be sent by RP; DR SHOULD accept for compatibility. | should | Section 4.4.1 |
| R6 | RP MUST NOT forward Register-encapsulated packets for SSM addresses. | shall | Section 4.8.1 |
| R7 | For SSM, router MUST NOT send (*,G) Join/Prune, (S,G,rpt) Join/Prune, or Register for SSM. | shall | Section 4.8.1 |
| R8 | Assert messages from unknown neighbors SHOULD be discarded. | should | Section 4.6 |
| R9 | PIM-SSM-only routers MUST implement (S,G) upstream/downstream, (S,G) Assert, Hello/DR, forwarding; MAY omit Register, (*,G), (S,G,rpt), (*,*,RP) state machines. | shall | Section 4.8.2 |
| R10 | In Join/Prune group set fragmentation, if (*,G) Join present, all (S,G,rpt) Prunes MUST be in same message. | shall | Section 4.9.5.2 |
| R11 | Invalid combinations of source list entries (e.g., Join(*,G) and Prune(*,G) in same group set) MUST NOT be generated. | shall | Section 4.9.5.1 |

## Informative Annexes (Condensed)
- **Annex A (PMBR Behavior)**: Describes how border routers connect PIM-SM domains to non-PIM domains, including external source injection and handling of wildcard receivers via (*,*,RP) joins.
- **Annex B (Index)**: Provides an alphabetical index of terms and section numbers for reference.