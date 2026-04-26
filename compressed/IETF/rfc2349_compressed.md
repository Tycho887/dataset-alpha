# RFC 2349: TFTP Timeout Interval and Transfer Size Options
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: May 1998 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc2349

## Scope (Summary)
This document defines two TFTP options: the Timeout Interval option allows negotiation of the retransmission timeout, and the Transfer Size option allows the receiving side to determine the file size before transfer. Both options extend the TFTP protocol via the Option Extension mechanism defined in RFC 2347.

## Normative References
- [1] Sollins, K., "The TFTP Protocol (Revision 2)", STD 33, RFC 1350, October 1992.
- [2] Malkin, G., and A. Harkin, "TFTP Option Extension", RFC 2347, May 1998.

## Definitions and Abbreviations
- **opc**: Opcode (1 for Read Request, 2 for Write Request), as defined in [1].
- **filename**: Name of the file to be read or written, NULL-terminated, as defined in [1].
- **mode**: File transfer mode ("netascii", "octet", or "mail"), NULL-terminated, as defined in [1].
- **timeout**: The Timeout Interval option string "timeout" (case-insensitive), NULL-terminated field.
- **#secs**: Number of seconds to wait before retransmitting (ASCII). Valid values range between "1" and "255" inclusive. NULL-terminated field.
- **tsize**: The Transfer Size option string "tsize" (case-insensitive), NULL-terminated field.
- **size**: Size of the file to be transferred (in octets), NULL-terminated field.

## Timeout Interval Option Specification
- **Packet Format**: The TFTP Read Request or Write Request packet is modified to include the timeout option as follows:
  ```
  +-------+---~~---+---+---~~---+---+---~~---+---+---~~---+---+
  |  opc  |filename| 0 |  mode  | 0 | timeout| 0 |  #secs | 0 |
  +-------+---~~---+---+---~~---+---+---~~---+---+---~~---+---+
  ```
- **T1**: If the server is willing to accept the timeout option, it shall send an Option Acknowledgment (OACK) to the client. The specified timeout value must match the value specified by the client.
- **Example**: A Read Request for file "foobar" in octet mode with timeout interval of 1 second is encoded as:
  ```
  +-------+--------+---+--------+---+--------+---+-------+---+
  |   1   | foobar | 0 | octet  | 0 | timeout| 0 |   1   | 0 |
  +-------+--------+---+--------+---+--------+---+-------+---+
  ```

## Transfer Size Option Specification
- **Packet Format**: The TFTP Read Request or Write Request packet is modified to include the tsize option as follows:
  ```
  +-------+---~~---+---+---~~---+---+---~~---+---+---~~---+---+
  |  opc  |filename| 0 |  mode  | 0 | tsize  | 0 |  size  | 0 |
  +-------+---~~---+---+---~~---+---+---~~---+---+---~~---+---+
  ```
- **Read Request (RRQ)**:
  - **T2**: In Read Request packets, a size of "0" shall be specified in the request. The server shall return the actual file size (in octets) in the OACK.
  - If the file is too large for the client to handle, the client may abort the transfer with an Error packet (error code 3).
- **Write Request (WRQ)**:
  - **T3**: In Write Request packets, the size of the file (in octets) shall be specified in the request. The server shall echo back that size in the OACK.
  - If the file is too large for the server to handle, the server may abort the transfer with an Error packet (error code 3).
- **Example**: A Write Request for file "foobar" in octet mode with file size 673312 octets is encoded as:
  ```
  +-------+--------+---+--------+---+--------+---+--------+---+
  |   2   | foobar | 0 | octet  | 0 | tsize  | 0 | 673312 | 0 |
  +-------+--------+---+--------+---+--------+---+--------+---+
  ```

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | If the server accepts the timeout option, it must send an OACK with the matching timeout value. | shall | Timeout Interval Option Specification |
| R2 | For a Read Request, the client shall specify size="0"; the server shall return the file size in the OACK. The client may abort with error code 3 if too large. | shall / may | Transfer Size Option Specification (RRQ) |
| R3 | For a Write Request, the client shall specify the file size; the server shall echo it in the OACK. The server may abort with error code 3 if too large. | shall / may | Transfer Size Option Specification (WRQ) |

## Informative Annexes (Condensed)
- **Security Considerations**: The basic TFTP protocol has no security mechanism (no rename, delete, overwrite). This document does not add any security risks beyond the existing protocol.
- **Full Copyright Statement**: Copyright (C) The Internet Society (1998). All rights reserved. Permission to copy, distribute, and create derivative works is granted provided the copyright notice is retained and any modifications comply with Internet Standards process. The document is provided "AS IS" without warranty.