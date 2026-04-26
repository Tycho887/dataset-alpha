# RFC 2439: BGP Route Flap Damping
**Source**: IETF (Network Working Group) | **Version**: Standards Track | **Date**: November 1998 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/rfc2439/

## Scope (Summary)
This document specifies a method for reducing BGP routing update traffic caused by unstable routes ("route flap") without adversely affecting convergence for stable routes. The technique uses a figure of merit based on route withdrawal history to suppress the use and announcement of unstable routes, and is also applicable to IDRP.

## Normative References
- BGP-3: RFC 1267 (October 1991)
- BGP-4: RFC 1771 (March 1995)
- Application of BGP in the Internet: RFC 1772 (March 1995)
- BGP-4 Protocol Analysis: RFC 1774 (March 1995)
- Experience with BGP-4: RFC 1773 (March 1995)
- Exchanging Routing Information Across Provider Boundaries: RFC 1520 (September 1993)

## Definitions and Abbreviations
- **Route Flap**: Repeated reachability changes (withdrawal and re‑advertisement) of a BGP prefix.
- **Figure of Merit**: A cumulative, time‑decayed measure of instability, incremented on each withdrawal.
- **Cutoff Threshold (cut)**: Value above which a route advertisement is suppressed.
- **Reuse Threshold (reuse)**: Value below which a suppressed route may be used again.
- **Decay Half‑Life**: Time in which the figure of merit reduces by half when the route is reachable (`decay-ok`) or unreachable (`decay-ng`).
- **Maximum Hold‑Down Time (T‑hold)**: Maximum time a route can be suppressed regardless of past instability.
- **Suppression**: Withholding the use and advertisement of a route due to high figure of merit.
- **Reuse List**: A circular list of queues that group suppressed routes scheduled for future re‑evaluation.
- **BGP**: Border Gateway Protocol
- **IDRP**: Inter‑Domain Routing Protocol (ISO/IEC 10747)
- **NLRI**: Network Layer Reachability Information
- **AS**: Autonomous System
- **IBGP / EBGP**: Internal / External BGP
- **RIB**: Routing Information Base
- **MED**: MULTI_EXIT_DISCRIMINATOR

## 1 Overview
A BGP implementation **must** be prepared for a large volume of routing traffic. The mechanisms described limit propagation of unnecessary change without requiring the sender to shield the receiver from instabilities. The goals are:
- reduce router processing load caused by instability,
- prevent sustained routing oscillations,
- preserve convergence time for stable routes,
- pack changes into few updates,
- maintain routing consistency,
- minimise space and computational overhead.

## 2 Methods of Limiting Route Advertisement
Two methods are described: fixed timers and stability‑sensitive suppression. The former has no per‑route state but slows convergence; the latter uses per‑route state to avoid unnecessary delays for stable routes. Combining both is possible and desirable.

### 2.1 Existing Fixed Timer Recommendations
BGP‑4 [5] defines `MinRouteAdvertisementInterval` (recommended 30 s) and `MinASOriginationInterval` (recommended 15 s) for limiting advertisement frequency.

### 2.2 Desirable Properties of Damping Algorithms
- Suppression should be based on a prediction of future stability.
- Delay for well‑behaved routes must be minimal.
- Unstable routes should be suppressed until confidence in stability is restored.
- Route changes that can be packed should be combined.
- Suppression should apply to use and announcement, not just withdrawal.
- If an alternate route exists, the unstable route should be suppressed more aggressively.
- IBGP delay must be minimal; routing consistency is critical.
- Figure of merit should use exponential decay to remember past instability gradually.

### 2.3 Design Choices
Exponential decay is chosen because it allows efficient computation: decay can be applied in fixed time increments using precomputed arrays. The figure of merit is incremented on each withdrawal, clipped to a ceiling, and decayed at different rates when reachable vs. unreachable.

## 3 Limiting Route Advertisements Using Fixed Timers
Fixed timers are used to improve packing of routes into BGP update messages. An implementation **must** provide:
- a minimum advertisement delay,
- an upper bound on that delay,
- computationally efficient handling of many candidates (e.g., grouping routes with common attributes).

## 4 Stability Sensitive Suppression of Route Advertisement
This method is applied only when receiving updates from EBGP peers. Applying it to IBGP learned routes or to advertisements after route selection **may** cause routing loops. A figure of merit per route is maintained; routes with high values are suppressed.

### 4.1 Single vs. Multiple Configuration Parameter Sets
Multiple parameter sets **may** be used to handle severe flap vs. chronic instability. Parameter selection **may** be based on LOCAL_PREF, existence of alternate paths, or prefix length. Different aggressiveness for routes with or without alternates is recommended.

### 4.2 Configuration Parameters
The following **may** be configured (per set):
- `cut` (cutoff threshold)
- `reuse` (reuse threshold)
- `T-hold` (maximum hold‑down time)
- `decay-ok` (half‑life when reachable)
- `decay-ng` (half‑life when unreachable; 0 means no decay)
- `Tmax-ok`, `Tmax-ng` (memory retention times)
- `delta-t` (time granularity)
- `delta-reuse` (reuse list evaluation interval)
- `reuse-list-max`, `reuse-list-size`
- `reuse-index-array-size`

### 4.3 Guidelines for Setting Parameters
- Decay half‑life should be considerably longer than the period of the flap it is meant to address.
- The figure of merit converges under constant flap rate; a ceiling prevents indefinite suppression.
- Recommended decay rates and thresholds produce a sawtooth pattern; routes flapping at half‑life or faster are suppressed after 2–3 withdrawals and reused after ~1.5–2.5 half‑lives of stability.

### 4.4 Run‑Time Data Structures
- Fixed per‑system storage: decay arrays, reuse index arrays, reuse list heads.
- Per‑route state: figure‑of‑merit, last‑update time, configuration pointer, reuse list pointers.
- The route tuple includes NLRI, AS path (by default), optionally next‑hop and MED.

### 4.4.3 Per‑Route State
The tuple for damping **must** contain:
- NLRI (prefix + length)
- AS path (default; may be excluded optionally)
- Last AS set in path (excluded by default)
- Next hop (excluded by default)
- MED (excluded by default)

### 4.5 Processing Configuration Parameters
Precomputed values from configuration: decay per tick, decay and reuse index arrays. Scaling **should** use integer arithmetic with sufficient headroom to avoid overflow.

### 4.6 Building Reuse Index Arrays
The reuse array maps a scaled ratio (current figure of merit / reuse threshold) to a reuse list index. This avoids computing a logarithm on each insertion.

### 4.7 A Sample Configuration
Example parameters: cut=1.25, reuse=0.5, T‑hold=15 min, decay‑ok=5 min, decay‑ng=15 min, Tmax‑ok=15 min, Tmax‑ng=30 min, delta‑t=1 s, delta‑reuse=15 s, reuse‑list‑size=256, reuse‑index‑array‑size=1024. Space estimates are provided.

### 4.8 Processing Routing Protocol Activity
#### 4.8.1 Processing a New Peer or New Routes
If no previous history, damping structure pointer is zeroed; route is used.

#### 4.8.2 Processing Unreachable Messages
- If no existing damping structure: allocate one, set figure‑of‑merit = 1, withdraw route.
- If existing: decay figure of merit using `decay-array-ok[t-diff]`, increment by 1, clip to ceiling, remove from reuse list, withdraw route, insert into reuse list.

#### 4.8.3 Processing Route Advertisements
- If no damping structure: use route, no structure created.
- If exists: decay figure of merit using `decay-array-ng[t-diff]`.
  - If figure < cut and not suppressed: use route.
  - If suppressed and figure < reuse: clear suppressed, remove from reuse list, use route.
  - Else: suppress, insert into reuse list.
  - If figure becomes zero: free damping structure.

#### 4.8.4 Processing Route Changes
Treat a change as an unreachable (Section 4.8.2) followed by a new advertisement (Section 4.8.3). This penalises both paths when a peer oscillates between two AS paths.

#### 4.8.5 Processing a Peer Router Loss
**May** mark the peer session itself as unstable to reduce per‑route memory. Downstream routers will eventually discard damping state.

#### 4.8.6 Inserting into the Reuse Timer List
Use the reuse index array to determine the queue. Insert into `reuse-list[(index + offset) modulo reuse-list-size]`. The offset rotates periodically.

#### 4.8.7 Handling Reuse Timer Events
Every `delta-reuse` seconds:
- Save pointer to current zeroth queue head, zero it.
- Increment offset (circular).
- For each route in saved queue: decay using `decay-array-ok`, if figure < reuse then use route (treat as new advertisement), else re‑insert via Section 4.8.6.

## 5 Implementation Experience
- Route flap damping **must not** be applied on IBGP learned routes – doing so can cause persistent routing loops.
- Penalties **should** be applied only when a route is removed or replaced, not on addition.
- Damping **should** be applied near the source of instability (e.g., by the provider owning the unstable prefix).
- Providers **should** publish their damping parameters and be willing to manually clear damping state on request when the problem is corrected.
- Aggregation and static routes are alternative means to damp flapping.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | A BGP implementation **must** be prepared for a large volume of routing traffic. | must | §1 |
| R2 | Damping on IBGP learned routes **must not** be applied. | must | §5 |
| R3 | Penalties for instability **should** be applied only on route removal/replacement, not on addition. | should | §5 |
| R4 | Damping **should** be applied near the source of route flap. | should | §5 |
| R5 | Parameters **may** be configured per route prefix, peer, AS path, or global sets. | may | §4.1 |
| R6 | Different decay rates for reachable vs. unreachable state **may** be used; slower decay while unreachable is recommended. | recommended | §4 |
| R7 | Fixed timers **must** provide a minimum advertisement delay and an upper bound on that delay. | must | §3 |
| R8 | Implementation **shall** use an exponential decay algorithm for the figure of merit. | shall | §2.3 |
| R9 | The route tuple for damping **must** include NLRI and AS path (by default). | must | §4.4.3 |
| R10 | When a route is suppressed, it **should** be inserted into a reuse list for future evaluation. | should | §4.8.6 |
| R11 | Providers **should** publish damping parameters and be willing to clear damping state manually on credible request. | should | §5 |

## Informative Annexes (Condensed)
- **Figure 1**: Illustrates the sawtooth figure of merit for constant‑rate route flap at frequencies related to the decay half‑life. The plot shows that routes flapping at or above the decay rate are suppressed after a few cycles and kept suppressed until the route becomes stable for ~1.5–2.5 half‑lives.
- **Figure 2**: Shows the effect of separate decay constants when the route is unreachable (5× slower decay). Routes that are reachable for a higher percentage of the flap cycle are reused sooner after stabilization.
- **Figure 3**: Demonstrates the algorithm with a sample configuration; routes flapping over a 12‑minute period with 2‑minute and 4‑minute periods are suppressed for 9–15 minutes after stability.
- **Figure 4**: Depicts the circular reuse list data structure, with list heads rotated every `delta-reuse` seconds.
- **Security Considerations**: The method does not weaken routing security but may prolong denial‑of‑service attacks; no new attack vectors are introduced.