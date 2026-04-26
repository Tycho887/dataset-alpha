# RFC 2918: Route Refresh Capability for BGP-4
**Source**: IETF | **Version**: RFC 2918 (Standards Track) | **Date**: September 2000 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/rfc2918/

## Scope (Summary)
Defines a new BGP capability (Route Refresh Capability) that allows dynamic exchange of route refresh requests between BGP speakers and subsequent re-advertisement of the respective Adj‑RIB‑Out, enabling non‑disruptive routing policy changes without requiring continuous storage of unmodified route copies.

## Normative References
- [BGP-4] Rekhter, Y. and T. Li, "A Border Gateway Protocol 4 (BGP-4)", RFC 1771, March 1995
- [BGP-MP] Bates, T., Chandra, R., Katz, D. and Y. Rekhter, "Multiprotocol Extensions for BGP-4", RFC 2858, June 2000
- [BGP-CAP] Chandra, R. and J. Scudder, "Capabilities Advertisement with BGP-4", RFC 2842, May 2000

## Definitions and Abbreviations
- **Route Refresh Capability**: A BGP capability (code 2, length 0) that indicates a speaker can receive and properly handle the ROUTE‑REFRESH message.
- **ROUTE‑REFRESH message**: BGP message type 5, carrying one <AFI, SAFI> pair to request re‑advertisement of the Adj‑RIB‑Out for that address family.
- **Adj‑RIB‑Out**: Per‑peer routing information base for outbound routes.
- **AFI**: Address Family Identifier (16‑bit).
- **SAFI**: Subsequent Address Family Identifier (8‑bit).

## Section 2: Route Refresh Capability
- **Capability Advertisement**: A BGP speaker **shall** use BGP Capabilities Advertisement [BGP-CAP] to advertise the Route Refresh Capability to a peer. The capability is advertised with Capability code 2 and Capability length 0.
- **Meaning**: By advertising this capability, the speaker conveys that it is capable of receiving and properly handling the ROUTE‑REFRESH message (as defined in Section 3) from the peer.

## Section 3: Route-REFRESH Message
- **Message Type**: 5 – ROUTE‑REFRESH
- **Message Format**: One <AFI, SAFI> encoded as:
  ```
  0       7      15      23      31
  +-------+-------+-------+-------+
  |      AFI      | Res.  | SAFI  |
  +-------+-------+-------+-------+
  ```
  - **AFI**: Address Family Identifier (16 bit)
  - **Res.**: Reserved (8 bit). **Should** be set to 0 by the sender and ignored by the receiver.
  - **SAFI**: Subsequent Address Family Identifier (8 bit)
- **Encoding Reference**: Meaning, use, and encoding of <AFI, SAFI> are the same as defined in [BGP-MP, section 7].

## Section 4: Operation
- **Willingness to Receive**: A BGP speaker that is willing to receive the ROUTE‑REFRESH message from its peer **should** advertise the Route Refresh Capability to the peer using BGP Capabilities advertisement [BGP-CAP].
- **Conditions for Sending**:
  - A BGP speaker **may** send a ROUTE‑REFRESH message to its peer **only if** it has received the Route Refresh Capability from that peer.
  - The <AFI, SAFI> carried in such a message **should** be one of the <AFI, SAFI> that the peer advertised to the speaker at session establishment time via capability advertisement.
- **Reception Handling**:
  - If a BGP speaker receives from its peer a ROUTE‑REFRESH message with an <AFI, SAFI> that the speaker **did not** advertise to the peer at session establishment time via capability advertisement, the speaker **shall** ignore such a message.
  - Otherwise, the BGP speaker **shall** re‑advertise to that peer the Adj‑RIB‑Out of the <AFI, SAFI> carried in the message, based on its outbound route filtering policy.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | A BGP speaker shall use BGP Capabilities Advertisement [BGP-CAP] to advertise Route Refresh Capability (code 2, length 0). | shall | Section 2 |
| R2 | By advertising the Route Refresh Capability, the speaker conveys capability to receive and handle ROUTE‑REFRESH messages. | (normative implication) | Section 2 |
| R3 | Reserved field in ROUTE‑REFRESH message shall be set to 0 by sender and ignored by receiver. | should (normative) | Section 3 |
| R4 | A BGP speaker willing to receive ROUTE‑REFRESH should advertise the Route Refresh Capability. | should | Section 4 |
| R5 | A BGP speaker may send ROUTE‑REFRESH only if it has received the Route Refresh Capability from the peer. | may | Section 4 |
| R6 | The <AFI, SAFI> in a sent ROUTE‑REFRESH should be one advertised by the peer at session establishment. | should | Section 4 |
| R7 | If a speaker receives a ROUTE‑REFRESH with an <AFI, SAFI> it did not advertise, it shall ignore the message. | shall | Section 4 |
| R8 | Otherwise, the speaker shall re‑advertise the Adj‑RIB‑Out for the given <AFI, SAFI> based on outbound route filtering policy. | shall | Section 4 |

## Informative Annexes (Condensed)
- **Section 1 (Introduction)**: Describes the problem of dynamic route refresh in BGP-4; the proposed Route Refresh Capability avoids the memory/CPU overhead of soft-reconfiguration.
- **Section 5 (Security Considerations)**: This extension does not change the underlying security issues.
- **Section 6 (Acknowledgments)**: The concept is derived from IDRP; thanks to reviewers.
- **Section 9 (Copyright)**: Standard IETF copyright notice and disclaimer.