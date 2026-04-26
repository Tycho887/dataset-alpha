# RFC 6176: Prohibiting Secure Sockets Layer (SSL) Version 2.0
**Source**: IETF (Internet Engineering Task Force) | **Version**: Standards Track | **Date**: March 2011 | **Type**: Normative  
**Updates**: RFC 2246 (TLS 1.0), RFC 4346 (TLS 1.1), RFC 5246 (TLS 1.2)  
**Original**: https://www.rfc-editor.org/info/rfc6176

## Scope (Summary)
This document requires that TLS clients and servers never negotiate the use of SSL version 2.0 when establishing connections, and updates the backward compatibility sections in TLS specifications (RFC 2246, RFC 4346, RFC 5246) accordingly.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [TLS1.0] Dierks, T. and C. Allen, "The TLS Protocol Version 1.0", RFC 2246, January 1999.
- [TLS1.1] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.1", RFC 4346, April 2006.
- [TLS1.2] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.

## Definitions and Abbreviations
- **Keywords (MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL)**: As defined in RFC 2119.
- **SSL 2.0**: Secure Sockets Layer version 2.0 [SSL2].
- **TLS**: Transport Layer Security (RFC 2246, 4346, 5246).
- **CLIENT-HELLO / SERVER-HELLO**: Handshake messages as defined in TLS/SSL.

## 1. Introduction
Many IETF protocols rely on TLS for security. Some TLS implementations also support SSL 2.0, which has known deficiencies (Section 2). This document describes those deficiencies and **requires** that TLS clients and servers never negotiate the use of SSL version 2.0, updating the backward compatibility sections in TLS [TLS1.0][TLS1.1][TLS1.2] as previously warned in RFC 4346 and RFC 5246.

## 2. SSL 2.0 Deficiencies
SSL version 2.0 [SSL2] has the following deficiencies:

- **Message authentication** uses MD5 [MD5], which is no longer considered secure [RFC6151].
- **Handshake messages are not protected**, allowing a man-in-the-middle to trick the client into choosing a weaker cipher suite.
- **Message integrity and encryption use the same key**, problematic with weak encryption algorithms.
- **Sessions can be easily terminated** via insertion of a TCP FIN, preventing the peer from determining a legitimate end of session.

## 3. Changes to TLS
Because of the deficiencies noted:

- **TLS clients MUST NOT** send the SSL version 2.0 compatible CLIENT-HELLO message format.
- **Clients MUST NOT** send any ClientHello message that specifies a protocol version less than `{0x03, 0x00}`.
- The client **SHOULD** specify the highest protocol version it supports (as per previous TLS definitions).
- **TLS servers MAY** continue to accept ClientHello messages in the version 2 CLIENT-HELLO format as specified in RFC 5246 [TLS1.2], Appendix E.2. Note: This does not contradict the prohibition against actually negotiating SSL 2.0.
- **TLS servers MUST NOT** reply with an SSL 2.0 SERVER-HELLO with a protocol version less than `{0x03, 0x00}`.
- Instead, servers **MUST** abort the connection (i.e., when the highest protocol version offered by the client is `{0x02, 0x00}`, the TLS connection will be refused).

Note: The number of servers supporting the "MAY accept" option is declining, and the SSL 2.0 CLIENT-HELLO precludes TLS protocol enhancements requiring TLS extensions (which can only be sent as part of an Extended ClientHello).

## 4. Security Considerations
This entire document addresses security considerations; the prohibition of SSL 2.0 directly mitigates the deficiencies listed in Section 2.

## 5. Acknowledgements
Inspired by discussions on the XMPP mailing list. Thanks to Michael D'Errico, Paul Hoffman, Nikos Mavrogiannopoulos, Tom Petch, Yngve Pettersen, Marsh Ray, Martin Rex, Yaron Sheffer, and Glen Zorn for reviews and comments.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | TLS clients MUST NOT send the SSL version 2.0 compatible CLIENT-HELLO message format. | MUST | Section 3 |
| R2 | Clients MUST NOT send any ClientHello specifying a protocol version less than {0x03, 0x00}. | MUST | Section 3 |
| R3 | The client SHOULD specify the highest protocol version it supports. | SHOULD | Section 3 (also RFC 2246, 4346, 5246) |
| R4 | TLS servers MAY continue to accept ClientHello in version 2 format as per RFC 5246 Appendix E.2. | MAY | Section 3 |
| R5 | TLS servers MUST NOT reply with an SSL 2.0 SERVER-HELLO with a version less than {0x03, 0x00}. | MUST | Section 3 |
| R6 | Servers MUST abort the connection when the highest protocol version offered by the client is {0x02, 0x00}. | MUST | Section 3 |

## Informative Annexes (Condensed)
- **Annex A – SSL 2.0 Deficiencies (Section 2)**: Summarized above in Section 2.
- **Annex B – References**: Normative and informative references as listed.
  - [SSL2] Hickman, K., "The SSL Protocol", Netscape, Feb 1995.
  - [MD5] Rivest, R., "The MD5 Message-Digest Algorithm", RFC 1321, April 1992.
  - [RFC6151] Turner, S. and L. Chen, "Updated Security Considerations for the MD5 Message-Digest and the HMAC-MD5 Algorithms", RFC 6151, March 2011.