# RFC 4855: Media Type Registration of RTP Payload Formats
**Source**: IETF | **Version**: Standards Track | **Date**: February 2007 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc4855

## Scope
Defines the specific procedures and requirements for registering RTP payload formats as audio, video, or other media subtype names in the IANA registry, enabling identification of RTP transmissions in text-based formats like SDP.

## Normative References
- [1] Freed, N. and J. Klensin, "Media Type Specifications and Registration Procedures", BCP 13, RFC 4288, December 2005.
- [2] Schulzrinne, H., et al., "RTP: A Transport Protocol for Real-Time Applications", RFC 3550, July 2003.
- [3] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [4] Schulzrinne, H. and S. Casner, "RTP Profile for Audio and Video Conferences with Minimal Control", RFC 3551, July 2003.
- [5] Handley, M., et al., "SDP: Session Description Protocol", RFC 4566, July 2006.
- [6] Freed, N. and N. Borenstein, "MIME Part One: Format of Internet Message Bodies", RFC 2045, November 1996.

## Definitions and Abbreviations
- **RTP**: Real-time Transport Protocol (RFC 3550)
- **SDP**: Session Description Protocol (RFC 4566)
- **IANA**: Internet Assigned Numbers Authority
- **MUST / MUST NOT / REQUIRED / SHALL / SHALL NOT / SHOULD / SHOULD NOT / RECOMMENDED / MAY / OPTIONAL**: Requirement levels per RFC 2119.

## Procedure for Registering Media Types for RTP Payload Types
- **General**: Follows RFC 4288 procedures and template (Section 10). Additional requirements for RTP-specific sections:
  - **Required parameters**: "rate" required if RTP timestamp clock rate is not fixed; may have other required parameters per payload format.
  - **Optional parameters**: "channels" (default order per RFC 3551), "ptime", "maxptime" (defined in RFC 4566). New optional parameters MAY be added to previously defined RTP media types, but MUST NOT change existing functionality and MUST be ignorable by existing implementations.
  - **Encoding considerations**: Must note binary or framed data as per RFC 4288 Section 4.8.
  - **Published specification**: Must include description of media encoding and payload format specification (usually an RFC). Must include RTP timestamp clock rate.
  - **Restrictions on usage**: Must note if transfer depends on RTP framing and is only defined for RTP.
- **Cases for existing/non-RTP types**:
  - **a) Not yet registered**: New registration; may specify transfer via other means. Optional parameters must clearly state to which mode(s) they apply.
  - **b) Media type exists for non-RTP**: Modify restrictions to indicate also transferable via RTP. Add RTP-specific parameters with clear scope.
  - **c) Existing RTP type extended to non-RTP**: Modify restrictions to indicate also transferable via non-RTP protocol. Add non-RTP-specific parameters with clear scope.

### Example Media Type Registration (audio/example)
- **Type name**: audio
- **Subtype name**: example
- **Required parameters**: rate (RTP timestamp clock rate, typically 8000)
- **Optional parameters**: channels (1 default), ptime, maxptime
- **Encoding considerations**: framed binary data (RFC 4288 Section 4.8)
- **Security considerations**: See Section n of RFC nnnn
- **Intended usage**: COMMON
- **Restrictions on usage**: Depends on RTP framing, only defined for transfer via RTP.

### Restrictions on Sharing a Subtype Name
- **Same subtype name MUST NOT be shared** for RTP and non-RTP unless data format is same (file format = concatenated RTP payloads without headers; magic number/header allowed).
- **Required parameters sets MUST be same** for both methods.
- If data format or required parameters differ, **MUST register separate types**; **RECOMMENDED** to use related names (e.g., common root + suffix; "+rtp" suggested for RTP).

## Mapping to SDP Parameters
- Media type syntax: `type "/" subtype *(";" parameter)` per RFC 2045.
- **Mapping**:
  - Media type (e.g., audio) → SDP `m=` media name.
  - Media subtype (payload format) → SDP `a=rtpmap` encoding name.
  - Parameters "rate" and "channels" → `a=rtpmap` clock rate and encoding parameters.
  - "ptime" and "maxptime" → `a=ptime` and `a=maxptime`.
  - Payload-format-specific parameters → `a=fmtp`; allowed set defined by payload format RFC and MUST NOT be extended without corresponding revision; suggested format: semicolon-separated list of parameter=value pairs.
- Names are case-insensitive.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Registration of RTP payload type as media type shall follow RFC 4288 procedures and template. | shall | Section 2 |
| R2 | If payload format does not have fixed RTP timestamp clock rate, a "rate" parameter is required. | required | Section 2 (Required parameters) |
| R3 | New optional parameters MAY be added to previously defined RTP media types, but MUST NOT change existing functionality and MUST be ignorable. | MAY / MUST | Section 2 (Optional parameters) |
| R4 | Encoding considerations must note binary or framed data. | must | Section 2 (Encoding considerations) |
| R5 | Published specification must include RTP timestamp clock rate. | must | Section 2 (Published specification) |
| R6 | Restrictions on usage must note if transfer depends on RTP framing. | must | Section 2 (Restrictions on usage) |
| R7 | Same subtype name MUST NOT be shared for RTP and non-RTP unless data format is same. | must not | Section 2.2 |
| R8 | Required parameters sets must be same for both methods if sharing subtype name. | must | Section 2.2 |
| R9 | If data formats differ, MUST register separate types. | must | Section 2.2 |
| R10 | Payload-format-specific parameters in SDP `a=fmtp` MUST NOT be extended without corresponding revision of payload format specification. | must not | Section 3 |
| R11 | Security analysis MUST be done for all types in standards tree. | must | Section 5 |

## Informative Annexes (Condensed)
- **Section 4 (Changes from RFC 3555)**: Updates RFC 3555 to conform to revised procedures in RFC 4288. Encoding considerations now under restrictions on usage. Adds conditions for adding new optional parameters to existing RTP media types and new Section 2.2. Removed media type registrations (moved to RFC 4856).
- **Section 5 (Security Considerations)**: No security risks imposed by procedure itself, but use of registered types may involve risks: active content, steganography, encryption needs. Each registration must state specific security considerations. Analysis of security issues MUST be done for standards tree types; all known risks MUST be identified. Active content and compression-related risks must be addressed.
- **Section 6 (IANA Considerations)**: This document specifies requirements and procedures; no registrations are defined here.