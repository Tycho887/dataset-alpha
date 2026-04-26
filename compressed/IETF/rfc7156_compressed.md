# RFC 7156: Diameter Support for Proxy Mobile IPv6 Localized Routing
**Source**: IETF | **Version**: Standards Track | **Date**: April 2014 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7156

## Scope (Summary)
This document defines AAA support using Diameter for authorizing localized routing sessions between Mobile Access Gateways (MAGs) in a Proxy Mobile IPv6 domain, covering scenarios A11, A12, and A21 from RFC 6279.

## Normative References
- RFC 2119 (Key words for requirement levels)
- RFC 5213 (Proxy Mobile IPv6)
- RFC 5447 (Diameter Mobile IPv6: NAS-Diameter interaction)
- RFC 5779 (Diameter Proxy Mobile IPv6: MAG/LMA interaction with Diameter server)
- RFC 5844 (IPv4 Support for PMIPv6)
- RFC 6705 (Localized Routing for PMIPv6)
- RFC 6733 (Diameter Base Protocol)
- RFC 7155 (Diameter Network Access Server Application)

## Definitions and Abbreviations
- **MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / MAY / OPTIONAL**: As defined in RFC 2119.
- **MAG**: Mobile Access Gateway
- **LMA**: Local Mobility Anchor
- **MN**: Mobile Node
- **CN**: Correspondent Node
- **PMIPv6**: Proxy Mobile IPv6
- **LR**: Localized Routing
- **AAA**: Authentication, Authorization, and Accounting
- **HAAA**: Home AAA server

## 3. Solution Overview
This document addresses how to provide authorization information to the MN's MAG or LMA enabling localized routing and resolution of the destination MN's MAG via interaction between LMA and AAA server. The reference architecture assumes:
- If MN and CN belong to different LMAs, they must share the same MAG (scenario A12).
- If MN and CN are attached to different MAGs, they should belong to the same LMA (scenario A21).
- If MN and CN belong to same LMA and same MAG (scenario A11).
- MAG and LMA support Diameter client functionality.

The interaction according to this specification authorizes the localized routing service.

## 4. Attribute Value Pairs Used in This Document

### 4.1. User-Name AVP
- **AVP Code**: 1 (RFC 6733, Section 8.14)
- **Usage**: Carries the Mobile Node identifier (MN-Identifier) [RFC5213] in the Diameter AA-Request message [RFC7155] sent to the AAA server.

### 4.2. PMIP6-IPv4-Home-Address AVP
- **AVP Code**: 505 (RFC 5779, Section 5.2)
- **Usage**: Carries the Mobile Node's IPv4 home address (IPv4-MN-HoA) [RFC5844] in the AA-Request message [RFC7155].

### 4.3. MIP6-Home-Link-Prefix AVP
- **AVP Code**: 125 (RFC 5779, Section 5.3)
- **Usage**: Carries the Mobile Node's home network prefix (MN-HNP) in the AA-Request [RFC7155].

### 4.4. MIP6-Feature-Vector AVP
- **Definition**: RFC 5447; 64-bit flags field.
- **New flag**: `INTER_MAG_ROUTING_SUPPORTED (0x0002000000000000)`
- **Normative**: When set, indicates support or authorization of direct routing of IP packets between MNs anchored to different MAGs without LMA.
- **Procedure**: During network access authentication [RFC5779], MAG or LMA sets this flag in AA-Request to indicate inter-MAG direct routing may be provided to the MN. HAAA sets the flag in AA-Answer to authorize. MAG and LMA also set this flag in AA-R to request authorization for inter-MAG direct routing between two MNs. If cleared, procedure not supported or not authorized.
- **Requirement**: MAG and LMA compliant to this specification MUST support this policy feature on a per-MN and per-subscription basis.

## 5. Example Signaling Flows for Localized Routing Service Authorization
Localized Routing Service Authorization can occur during network access authentication [RFC5779] before LR is initialized. Preauthorized pairs of LMA/prefix sets can be downloaded during that procedure. LR can be initiated when destination of a received packet matches one or more prefixes from the procedure.

### Figure 2: MAG-Initiated LR Authorization in A12 (same MAG, different LMAs)
- MAG1 receives data from MN1 to MN2. MAG1 knows MN2 belongs to LMA2 (different from LMA1). MAG1 sends AA-Request to AAA server containing:
  - MIP6-Feature-Vector with `LOCAL_MAG_ROUTING_SUPPORTED` bit set (RFC 5779, Section 5.5)
  - Two instances of User-Name AVP (MN1, MN2)
  - Optionally: MIP6-Home-Link-Prefix (MN1's home prefix) or PMIP6-IPv4-Home-Address (MN1's IPv4 address)
- AAA server checks authorization; if allowed, responds with AA-Answer containing MIP6-Feature-Vector with `LOCAL_MAG_ROUTING_SUPPORTED` bit set.
- MAG1 then sends Localized Routing Initialization (LRI) to LMA1 and LMA2; they respond with Localized Routing Acknowledge (LRA) per RFC 6705.
- **Retry**: On LRA_WAIT_TIME expiration, MAG1 should re-request authorization before retransmitting LRI up to LRI_RETRIES.

### Figure 3: LMA-Initiated LR Authorization in A21 (different MAGs, same LMA)
- LMA1 receives data from MN2 to MN1. LMA1 knows both MNs belong to it. LMA1 (Diameter client) sends AA-Request with:
  - MIP6-Feature-Vector with `INTER_MAG_ROUTING_SUPPORTED` (Section 4.5) set
  - Two instances of User-Name AVP (MN1, MN2)
- AAA server authorizes; responds with AA-Answer containing MIP6-Feature-Vector with `INTER_MAG_ROUTING_SUPPORTED` set.
- LMA1 then initiates LR per RFC 6705.
- **Retry**: Same as Figure 2.

### Figure 4: LMA-Initiated LR Authorization in A11 (same MAG, same LMA)
- LMA1 receives data from MN2 to MN1. LMA1 (Diameter client) sends AA-Request with:
  - MIP6-Feature-Vector with `LOCAL_MAG_ROUTING_SUPPORTED` set (RFC 5779, Section 5.5)
  - Two instances of User-Name AVP (MN1, MN2)
- AAA server authorizes; responds with AA-Answer containing MIP6-Feature-Vector with `LOCAL_MAG_ROUTING_SUPPORTED` set.
- LMA1 responds to MAG1 for LR per RFC 6705.
- **Retry**: Same as above.

## 6. Security Considerations
- Security considerations from RFC 7155 (NASREQ) and RFC 5779 (Diameter PMIPv6) apply.
- Service authorization relies on existing trust relationship between MAG/LMA and AAA server.
- An authorized MAG could track mobile node movement at MAG level; if compromised, this could be a privacy breach. Monitoring for excessive queries from MAGs is recommended.

## 7. IANA Considerations
- A new value in the "Mobility Capability Registry" [RFC5447] for MIP6-Feature-Vector AVP: `INTER_MAG_ROUTING_SUPPORTED` (0x0002000000000000).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | MAG and LMA compliant to this specification MUST support the INTER_MAG_ROUTING_SUPPORTED policy feature on a per-MN and per-subscription basis. | MUST | Section 4.4 |
| R2 | On LRA_WAIT_TIME expiration, MAG or LMA should ask for authorization again before retransmitting LRI up to LRI_RETRIES. | SHOULD | Section 5 (Figures 2–4) |

## Informative Annexes (Condensed)
- **Contributors**: Paulo Loureiro, Jinwei Xia, Yungui Wang contributed to early versions.
- **Acknowledgements**: Thanks to Lionel Morand, Marco Liebsch, Carlos Jesus Bernardos Cano, Dan Romascanu, Elwyn Davies, Basavaraj Patil, Ralph Droms, Stephen Farrel, Robert Sparks, Benoit Claise, Abhay Roy for comments.