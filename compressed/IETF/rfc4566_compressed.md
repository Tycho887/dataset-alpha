# RFC 4566: SDP: Session Description Protocol
**Source**: IETF Network Working Group, Standards Track | **Version**: July 2006 | **Date**: July 2006 | **Type**: Normative
**Original**: RFC 4566 (obsoletes RFC 2327, RFC 3266)

## Scope (Summary)
The Session Description Protocol (SDP) defines a textual format for describing multimedia sessions, including media types, transport addresses, timing, and other session metadata. SDP is transport-independent and intended for use with protocols such as SAP, SIP, RTSP, email, and HTTP. It does not support negotiation of session content or media encodings.

## Normative References
- RFC 1034: Domain Names – Concepts and Facilities
- RFC 1035: Domain Names – Implementation and Specification
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- RFC 4234: Augmented BNF for Syntax Specifications: ABNF
- RFC 3629: UTF-8, a transformation format of ISO 10646
- RFC 2327: SDP: Session Description Protocol (obsoleted by this document)
- RFC 3986: Uniform Resource Identifier (URI): Generic Syntax
- RFC 2434: Guidelines for Writing an IANA Considerations Section in RFCs
- RFC 3066: Tags for the Identification of Languages
- RFC 3266: Support for IPv6 in SDP (obsoleted by this document)
- RFC 3490: Internationalizing Domain Names in Applications (IDNA)
- RFC 3548: The Base16, Base32, and Base64 Data Encodings

## Definitions and Abbreviations
- **Conference**: A set of two or more communicating users along with their software for communication.
- **Session**: A set of multimedia senders and receivers and the data streams flowing from senders to receivers. A multimedia conference is an example of a session.
- **Session Description**: A well-defined format for conveying sufficient information to discover and participate in a multimedia session.
- **SDP**: Session Description Protocol.
- **Key Words**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL – as defined in RFC 2119.

## 1. Introduction (Summarized)
SDP provides a standard representation for conveying media details, transport addresses, and session description metadata. It is purely a format for session description and does not incorporate a transport protocol. It is intended for use in a wide range of network environments but not for negotiation of session content or media encodings. This document obsoletes RFC 2327 and RFC 3266.

## 2. Glossary of Terms (Structured above)

## 3. Examples of SDP Usage (Condensed Informative)
- **Session Initiation (SIP)**: SDP is commonly used with SIP [RFC 3261] and the offer/answer model [RFC 3264] for media negotiation.
- **Streaming Media (RTSP)**: RTSP [RFC 2326] uses SDP syntax to describe parameters for on-demand delivery of real-time data.
- **Email and WWW**: The media type "application/sdp" enables automatic launching of session participation tools from email or web clients.
- **Multicast Session Announcement (SAP)**: SDP is the recommended format for session announcements via SAP [RFC 2974].

## 4. Requirements and Recommendations
### 4.1 Media and Transport Information
- SDP session description MUST convey media type, transport protocol, media format, address and port details.
- For unicast, the remote address and port SHOULD be the destination for data unless redefined by media type; redefinition is NOT RECOMMENDED.
### 4.2 Timing Information
- SDP can convey start/stop times and repeat times. Timing information is globally consistent independent of local time zones.
### 4.3 Private Sessions
- SDP itself does not distinguish between public and private sessions; encryption of the session description is dependent on the transport mechanism.
### 4.4 Obtaining Further Information
- SDP may include URIs for additional information about the session.
### 4.5 Categorisation
- SDP supports automated filtering via the "a=cat:" attribute.
### 4.6 Internationalisation
- ISO 10646/UTF-8 is recommended; other character sets (e.g., ISO 8859-1) may be used via "a=charset". Internationalisation applies only to free-text fields.

## 5. SDP Specification
### 5.1 Protocol Version ("v=")
- `v=0` (Required). Version 0; no minor version.

### 5.2 Origin ("o=")
- `o=<username> <sess-id> <sess-version> <nettype> <addrtype> <unicast-address>` (Required)
- `<username>` MUST NOT contain spaces; `<sess-id>` numeric string; tuple forms globally unique identifier.
- `<sess-version>` RECOMMENDED to use NTP timestamp when updated.
- `<nettype>` initially "IN"; `<addrtype>` initially "IP4" and "IP6"; others MAY be registered.
- `<unicast-address>` SHOULD be fully qualified domain name; local IP address MUST NOT be used outside scope.

### 5.3 Session Name ("s=")
- `s=<session name>` (Required, one only). MUST NOT be empty; SHOULD contain ISO 10646 characters; if no meaningful name, "s= " (single space) SHOULD be used.

### 5.4 Session Information ("i=")
- `i=<session description>` (Optional, at most one per session and per media). UTF-8 unless "a=charset" present.

### 5.5 URI ("u=")
- `u=<uri>` (Optional, at most one, MUST appear before first media field).

### 5.6 Email Address and Phone Number ("e=" and "p=")
- `e=<email-address>`, `p=<phone-number>` (Optional, multiple allowed, MUST appear before first media field if present).
- Phone numbers SHOULD be in ITU-T E.164 preceded by "+".

### 5.7 Connection Data ("c=")
- `c=<nettype> <addrtype> <connection-address>` (Required: at least one per media or one at session level).
- For IP4 multicast, TTL MUST be specified (range 0-255); for IPv6 multicast, TTL MUST NOT be present.
- Slash notation for multiple multicast addresses allowed only for hierarchical/layered encoding; MUST NOT be used for unicast.

### 5.8 Bandwidth ("b=")
- `b=<bwtype>:<bandwidth>` (Optional). Defined bwtypes: CT (conference total), AS (application specific). Prefix "X-" for experimental use is NOT RECOMMENDED; new modifiers SHOULD be registered with IANA. Unknown modifiers MUST be ignored.

### 5.9 Timing ("t=")
- `t=<start-time> <stop-time>` (Required, multiple allowed). NTP timestamps in seconds since 1900. Stop time=0 means unbounded; both zero means permanent. Permanent sessions SHOULD have associated repeat times.

### 5.10 Repeat Times ("r=")
- `r=<repeat interval> <active duration> <offsets from start-time>` (Optional, after t line). Units: d, h, m, s.

### 5.11 Time Zones ("z=")
- `z=<adjustment time> <offset> ...` (Optional). Adjustments apply to all t and r lines.

### 5.12 Encryption Keys ("k=")
- `k=<method>` or `k=<method>:<encryption key>` (Optional, use NOT RECOMMENDED). Methods: clear, base64, uri, prompt.
- MUST NOT be used unless SDP is conveyed over a secure and trusted channel. The "prompt" method is NOT RECOMMENDED.

### 5.13 Attributes ("a=")
- `a=<attribute>` or `a=<attribute>:<value>` (Primary extension mechanism). Attribute names MUST use US-ASCII. Unknown attributes MUST be ignored. Attributes MUST be registered with IANA.

### 5.14 Media Descriptions ("m=")
- `m=<media> <port> <proto> <fmt> ...` (Required for each media).
- Defined media types: audio, video, text, application, message; others MAY be registered.
- Transport protocols defined: udp, RTP/AVP, RTP/SAVP; others MAY be registered.
- For RTP/AVP or RTP/SAVP, fmt is RTP payload type number; dynamic types REQUIRE "a=rtpmap". First fmt SHOULD be default.
- Ports: for layered encoding, use `<port>/<number of ports>`. Semantics of multiple m lines with same transport address are undefined.

## 6. SDP Attributes (Summary of Defined Attributes)
- **cat**: Session-level, dot-separated hierarchical category.
- **keywds**: Session-level, keywords for filtering.
- **tool**: Session-level, name and version of creating tool.
- **ptime**: Media-level, packet time in ms.
- **maxptime**: Media-level, maximum packet time in ms.
- **rtpmap**: Media-level, mapping payload type to encoding name/clock rate/parameters.
- **recvonly**, **sendrecv**, **sendonly**, **inactive**: Either session or media-level, define direction.
- **orient**: Media-level, orientation (portrait/landscape/seascape).
- **type**: Session-level, conference type (broadcast/meeting/moderated/test/H332).
- **charset**: Session-level, character set for text fields.
- **sdplang**, **lang**: Either level, language tags.
- **framerate**: Media-level, maximum video frame rate.
- **quality**: Media-level, integer 0-10 for video quality tradeoff.
- **fmtp**: Media-level, format-specific parameters.

## 7. Security Considerations (Condensed)
- SDP session descriptions SHOULD only be trusted if obtained via authenticated transport from a known source.
- Endpoints SHOULD exercise care when session description is not obtained in a trusted manner.
- Software parsing SDP MUST NOT start other software without user consent.
- Use of "k=" line is NOT RECOMMENDED due to security risks; SDP MUST NOT be used to convey key material unless channel is private and authenticated.
- Intermediary systems modifying session descriptions are NOT RECOMMENDED unless authenticity and authority are checked.

## 8. IANA Considerations
- Media type "application/sdp" registered as detailed in Section 8.1.
- Parameters requiring registration: media types, transport protocols, media formats, attribute names, bandwidth specifiers, network types, address types. Registration procedures specified.
- Encryption key access methods table is obsolete; new registrations MUST NOT be accepted.

## 9. SDP Grammar (Condensed)
- Provided in augmented BNF (RFC 4234) in the original document. Refer to the original RFC for complete grammar.

## 10. Summary of Changes from RFC 2327 (Condensed)
- Extensive clarifications; ABNF revised; media type registration added; registration requirements tightened; RFC 2119 terms used; "RTP/SAVP" registered; "a=inactive" and "a=maxptime" added; "e=" and "p=" made optional; "k=" line deprecated; "x-" prefix deprecated; "control" and "data" media types deprecated.

## 11. Acknowledgements (Not compressed – reference to original)

## 12. References
- Normative references as listed above.
- Informative references: [13]–[31] as per original.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | v= field MUST give version; this memo defines version 0. | must | Section 5.1 |
| R2 | o= field MUST be present. | must | Section 5.2 |
| R3 | s= field MUST be present and MUST NOT be empty. | must | Section 5.3 |
| R4 | s= field SHOULD contain ISO 10646 characters; if no name, "s= " SHOULD be used. | should | Section 5.3 |
| R5 | At most one i= per session and per media. | must | Section 5.4 |
| R6 | URI field if present MUST appear before first media field; at most one. | must | Section 5.5 |
| R7 | e= or p= if present MUST appear before first media field. | must | Section 5.6 |
| R8 | Phone numbers SHOULD be given in E.164 with leading "+". | should | Section 5.6 |
| R9 | Session description MUST contain either at least one c= per media or a single session-level c=. | must | Section 5.7 |
| R10 | For IPv4 multicast c=, TTL MUST be included (0-255). | must | Section 5.7 |
| R11 | For IPv6 multicast c=, TTL MUST NOT be present. | must | Section 5.7 |
| R12 | Slash notation for multiple addresses MUST NOT be used for unicast. | must | Section 5.7 |
| R13 | Unknown bandwidth modifiers MUST be ignored. | must | Section 5.8 |
| R14 | Use of "X-" prefix for bwtype is NOT RECOMMENDED; new modifiers SHOULD be registered. | should/not recommended | Section 5.8 |
| R15 | t= lines are required (one or more). | must | Section 5.9 |
| R16 | k= field MUST NOT be used unless SDP is conveyed over secure and trusted channel. | must (negative) | Section 5.12 |
| R17 | Attribute names MUST use US-ASCII subset. | must | Section 5.13 |
| R18 | Unknown attributes MUST be ignored. | must | Section 5.13 |
| R19 | Attributes MUST be registered with IANA. | must | Section 5.13 |
| R20 | For RTP/AVP or RTP/SAVP, dynamic payload types require "a=rtpmap". | must | Section 5.14 |
| R21 | First fmt in m= SHOULD be used as default format. | should | Section 5.14 |
| R22 | Semantics of multiple m= lines with same transport address are undefined. | must (informative) | Section 5.14 |
| R23 | SDP parser MUST completely ignore any session description with unknown type letter. | must | Section 5 (General) |
| R24 | Software parsing SDP MUST NOT start other software without user consent. | must | Section 7 |
| R25 | Endpoints SHOULD exercise care when session description not obtained in trusted manner. | should | Section 7 |
| R26 | Use of "k=" line is NOT RECOMMENDED. | not recommended | Section 5.12, 7 |
| R27 | New encryption key access method registrations MUST NOT be accepted. | must (negative) | Section 8.3 |
| R28 | The "prompt" key method is NOT RECOMMENDED. | not recommended | Section 5.12 |
| R29 | For RTP, if odd port used and "a=rtcp:" present, MUST NOT subtract 1 from RTP port. | must | Section 5.14 |
| R30 | Application-level referral MUST NOT include local IP address outside scope. | must | Section 5.2 |

## Informative Annexes (Condensed)
- **Annex A (Section 10)**: Summary of Changes – details modifications from RFC 2327 including ABNF corrections, attribute additions, deprecation of "k=" line and "x-" prefix, and clarification of requirements.
- **Annex B (Authors' Addresses)**: Contact information for Mark Handley, Van Jacobson, and Colin Perkins.
- **Annex C (Full Copyright Statement)**: Copyright notice and disclaimer.