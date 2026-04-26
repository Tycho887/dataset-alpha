# RFC 6120: Extensible Messaging and Presence Protocol (XMPP): Core
**Source**: IETF | **Version**: Standards Track | **Date**: March 2011 | **Type**: Normative  
**Original**: http://www.rfc-editor.org/info/rfc6120

## Scope (Summary)
XMPP is an application profile of XML enabling near-real-time exchange of structured data between network entities. This document defines core protocol methods: XML stream setup/teardown, channel encryption, authentication, error handling, and communication primitives for messaging, presence, and request-response. It obsoletes RFC 3920.

## Normative References
- [BASE64] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, October 2006.
- [CHANNEL] Williams, N., "On the Use of Channel Bindings to Secure Channels", RFC 5056, November 2007.
- [CHANNEL-TLS] Altman, J., Williams, N., and L. Zhu, "Channel Bindings for TLS", RFC 5929, July 2010.
- [CHARSETS] Alvestrand, H., "IETF Policy on Character Sets and Languages", BCP 18, RFC 2277, January 1998.
- [DNS-CONCEPTS] Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- [DNS-SRV] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [IPv6-ADDR] Kawamura, S. and M. Kawashima, "A Recommendation for IPv6 Address Text Representation", RFC 5952, August 2010.
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [LANGMATCH] Phillips, A. and M. Davis, "Matching of Language Tags", BCP 47, RFC 4647, September 2006.
- [LANGTAGS] Phillips, A. and M. Davis, "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- [OCSP] Myers, M., Ankney, R., Malpani, A., Galperin, S., and C. Adams, "X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP", RFC 2560, June 1999.
- [PKIX] Cooper, D., Santesson, S., Farrell, S., Boeyen, S., Housley, R., and W. Polk, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.
- [PKIX-ALGO] Jonsson, J. and B. Kaliski, "Public-Key Cryptography Standards (PKCS) #1: RSA Cryptography Specifications Version 2.1", RFC 3447, February 2003.
- [PKIX-SRV] Santesson, S., "Internet X.509 Public Key Infrastructure Subject Alternative Name for Expression of Service Name", RFC 4985, August 2007.
- [PLAIN] Zeilenga, K., "The PLAIN Simple Authentication and Security Layer (SASL) Mechanism", RFC 4616, August 2006.
- [RANDOM] Eastlake, D., Schiller, J., and S. Crocker, "Randomness Requirements for Security", BCP 106, RFC 4086, June 2005.
- [SASL] Melnikov, A. and K. Zeilenga, "Simple Authentication and Security Layer (SASL)", RFC 4422, June 2006.
- [SCRAM] Newman, C., Menon-Sen, A., Melnikov, A., and N. Williams, "Salted Challenge Response Authentication Mechanism (SCRAM) SASL and GSS-API Mechanisms", RFC 5802, July 2010.
- [STRONGSEC] Schiller, J., "Strong Security Requirements for Internet Engineering Task Force Standard Protocols", BCP 61, RFC 3365, August 2002.
- [TCP] Postel, J., "Transmission Control Protocol", STD 7, RFC 793, September 1981.
- [TLS] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [TLS-CERTS] Saint-Andre, P. and J. Hodges, "Representation and Verification of Domain-Based Application Service Identity within Internet Public Key Infrastructure Using X.509 (PKIX) Certificates in the Context of Transport Layer Security (TLS)", RFC 6125, March 2011.
- [TLS-NEG] Rescorla, E., Ray, M., Dispensa, S., and N. Oskov, "Transport Layer Security (TLS) Renegotiation Indication Extension", RFC 5746, February 2010.
- [TLS-SSL2] Turner, S. and T. Polk, "Prohibiting Secure Sockets Layer (SSL) Version 2.0", RFC 6176, March 2011.
- [UCS2] ISO, "Information Technology - Universal Multiple-octet coded Character Set (UCS) - Amendment 2: UCS Transformation Format 8 (UTF-8)", ISO Standard 10646-1 Addendum 2, October 1996.
- [UNICODE] The Unicode Consortium, "The Unicode Standard, Version 6.0", 2010.
- [UTF-8] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [URI] Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- [X509] ITU-T Recommendation X.509, ISO Standard 9594-8, March 2000.
- [XML] Maler, E., Yergeau, F., Sperberg-McQueen, C., Paoli, J., and T. Bray, "Extensible Markup Language (XML) 1.0 (Fifth Edition)", W3C REC-xml-20081126, November 2008.
- [XML-GUIDE] Hollenbeck, S., Rose, M., and L. Masinter, "Guidelines for the Use of Extensible Markup Language (XML) within IETF Protocols", BCP 70, RFC 3470, January 2003.
- [XML-MEDIA] Murata, M., St. Laurent, S., and D. Kohn, "XML Media Types", RFC 3023, January 2001.
- [XML-NAMES] Thompson, H., Hollander, D., Layman, A., Bray, T., and R. Tobin, "Namespaces in XML 1.0 (Third Edition)", W3C REC-xml-names-20091208, December 2009.
- [XMPP-ADDR] Saint-Andre, P., "Extensible Messaging and Presence Protocol (XMPP): Address Format", RFC 6122, March 2011.
- [XMPP-IM] Saint-Andre, P., "Extensible Messaging and Presence Protocol (XMPP): Instant Messaging and Presence", RFC 6121, March 2011.

## Definitions and Abbreviations
- **whitespace**: One or more SP, HTAB, CR, or LF characters per ABNF.
- **localpart, domainpart, resourcepart**: As defined in [XMPP-ADDR].
- **bare JID**: XMPP address of form `<localpart@domainpart>` or `<domainpart>`.
- **full JID**: XMPP address of form `<localpart@domainpart/resourcepart>` or `<domainpart/resourcepart>`.
- **XML stream**: Container for exchange of XML elements between two entities over a network, denoted by opening `<stream>` and closing `</stream>` tags.
- **XML stanza**: First-level element under stream with name "message", "presence", or "iq" qualified by namespace 'jabber:client' or 'jabber:server'.
- **originating entity**: Entity that first generates a stanza.
- **input stream**: Stream over which a server receives data.
- **output stream**: Stream over which a server sends data.
- **route, deliver, ignore**: Actions a server may take on received stanzas.

## Section 1: Introduction
### 1.1 Overview (Condensed)
XMPP enables near-real-time exchange of structured data. Defines core methods: stream setup/teardown, encryption, authentication, error handling, messaging, presence, and request-response.

### 1.2 History (Condensed)
XMPP developed from Jabber community. RFC 3920 published 2004. This document obsoletes RFC 3920 based on implementation experience.

### 1.3 Functional Summary (Condensed)
Client connects to server via TCP, opens XML stream, negotiates TLS, authenticates via SASL, binds resource, exchanges stanzas, closes stream. Server-to-server follows similar process; strong authentication via SASL EXTERNAL recommended.

### 1.4 Terminology (Condensed)
Key words: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, NOT RECOMMENDED, MAY, OPTIONAL per RFC 2119. Security terms per [SEC-TERMS]. Certificate terms per [TLS-CERTS].

## Section 2: Architecture (Condensed)
XMPP uses distributed client-server architecture. Features: global addresses (JIDs), presence, persistent XML streams over TCP, structured data stanzas, network of clients and servers. Clients authenticate and bind resources; servers manage streams and route stanzas.

## Section 3: TCP Binding
### 3.1 Scope
Initiating entity MUST open TCP connection before negotiating XML streams.

### 3.2 Resolution of Fully Qualified Domain Names
#### 3.2.1 Preferred Process: SRV Lookup
- Construct SRV query for "_xmpp-client._tcp.<domain>" or "_xmpp-server._tcp.<domain>".
- If response with Target "." -> abort.
- Choose resolved FQDN; perform A/AAAA lookups.
- Use returned IP:port.
- If connection fails, try next IP, then next SRV target.
- If SRV fails, SHOULD attempt fallback.

#### 3.2.2 Fallback Processes
SHOULD use A/AAAA records with default ports (5222 for client, 5269 for server).

#### 3.2.3 When Not to Use SRV
If explicitly configured, use configured FQDN instead of SRV.

#### 3.2.4 Use of SRV Records with Add-On Services
Administrators MUST advertise "_xmpp-server" SRV records for add-on services if remote access is desired.

### 3.3 Reconnection
- SHOULD set reconnect delay to unpredictable number between 0 and 60 seconds.
- SHOULD back off exponentially.
- RECOMMENDED to use TLS session resumption.

### 3.4 Reliability
Core XMPP does not guarantee reliability; extensions exist (e.g., XEP-0198).

## Section 4: XML Streams
### 4.1 Stream Fundamentals
- **XML stream**: Started by `<stream>` header, ended by `</stream>` tag. Initial stream from initiator to receiver; response stream from receiver to initiator (MUST negotiate opposite direction).
- **XML stanza**: First-level element `<message/>`, `<presence/>`, or `<iq/>` in 'jabber:client' or 'jabber:server' namespace. Child elements may be in any namespace.

### 4.2 Opening a Stream
After TCP connection, initiator sends stream header with attributes (from, to, version, xml:lang, stream namespace). Receiver replies with own stream header including id.

### 4.3 Stream Negotiation
#### 4.3.1 Basic Concepts
Receiver imposes conditions (e.g., TLS, SASL). It communicates stream features via `<features/>` element.

#### 4.3.2 Stream Features Format
If initiator includes version >= "1.0", receiver MUST send `<features/>`. Features are child elements in different namespaces. Features may be mandatory-to-negotiate (e.g., with `<required/>` child) or voluntary.

#### 4.3.3 Restarts
After successful negotiation of features requiring restart (TLS, SASL), parties MUST consider stream replaced but NOT close TCP; initiator sends new stream header.

#### 4.3.4 Resending Features
Receiver MUST send updated features after restart.

#### 4.3.5 Completion of Stream Negotiation
Completed when receiver sends empty `<features/>` or only voluntary features. Initiator MUST NOT send stanzas until completion; if it does, receiver MUST close stream with `<not-authorized/>` error.

#### 4.3.6 Determination of Addresses
- Client-to-server: bare JID from SASL authorization identity; resource from binding.
- Server-to-server: bare JID from SASL authorization identity (or Server Dialback).
- Server MUST canonicalize JID per [XMPP-ADDR].

#### 4.3.7 Flow Chart (Non-normative, summarized)
Flow from TCP open to completion: initiator sends header, receives features, negotiates mandatory features, restarts if needed, until no mandatory features remain.

### 4.4 Closing a Stream
Send closing `</stream>` tag. If two streams over single TCP, sender must wait for peer's reciprocal close before terminating. Must send TLS close_notify and receive response.

### 4.5 Directionality
- Stream is unidirectional.
- Client-to-server uses two streams over single TCP (server MUST allow).
- Server-to-server uses two streams over two TCP connections.
- Multiple streams over multiple TCP connections allowed; server MAY close with `<conflict/>` if remote attempts more than one stream.

### 4.6 Handling of Silent Peers
#### 4.6.1 Dead Connection
Terminate TCP; no stream error needed.

#### 4.6.2 Broken Stream
Close with `<connection-timeout/>` stream error.

#### 4.6.3 Idle Peer
May close stream or use `<resource-constraint/>` or `<policy-violation/>`.

#### 4.6.4 Use of Checking Methods
RECOMMENDED not more than once every 5 minutes; ideally initiated by clients.

### 4.7 Stream Attributes
- **from**: Initiator's JID (SHOULD include after TLS); receiver MUST include.
- **to**: Initiator MUST include; receiver MUST include if initiator included 'from'.
- **id**: Receiver MUST include; initiator MUST NOT include.
- **xml:lang**: SHOULD be included; receiver MUST include.
- **version**: Initiator sets to highest supported; receiver sets to lower of initiator's and its own.

### 4.8 XML Namespaces
#### 4.8.1 Stream Namespace
Must be 'http://etherx.jabber.org/streams'. Violation results in `<invalid-namespace/>`.

#### 4.8.2 Content Namespace
Default namespace for data (other than stream namespace). Must be same for both streams.

#### 4.8.3 XMPP Content Namespaces
'jabber:client' for client-to-server; 'jabber:server' for server-to-server. Client MUST support 'jabber:client'. Server MUST support both. Stanzas sent over server-to-server MUST have 'to' and 'from' attributes.

#### 4.8.4 Other Namespaces
Data qualified by other namespaces may be sent but server MUST NOT route them to other entities unless explicitly negotiated.

#### 4.8.5 Namespace Declarations and Prefixes
Stream namespace prefix historically 'stream' (backward compat). Content namespace prefixes prohibited for 'jabber:client' or 'jabber:server'. Extended namespace declarations must be in stanza, not stream header.

### 4.9 Stream Errors
#### 4.9.1 Rules
- Unrecoverable; send `<error/>` then close stream.
- Error may occur during setup; receiver must still send opening `<stream>` header.
- If 'to' attribute missing or unknown, 'from' in response must be authoritative FQDN or empty.
- If two TCP connections, errors on initial stream returned via same connection; stanza errors returned via other connection.

#### 4.9.2 Syntax
```xml
<stream:error>
  <defined-condition xmlns='urn:ietf:params:xml:ns:xmpp-streams'/>
  [<text xml:lang='langcode'>optional text</text>]
  [optional app-specific condition]
</stream:error>
```
- MUST contain a defined condition.
- MAY contain `<text/>` (SHOULD have xml:lang). MUST NOT be interpreted programmatically.

#### 4.9.3 Defined Stream Error Conditions
| Condition | Description | Notes |
|---|---|---|
| bad-format | XML cannot be processed | See also specific XML errors |
| bad-namespace-prefix | Unsupported namespace prefix | |
| conflict | New stream conflicts with existing | Client must choose different resourcepart on reconnect |
| connection-timeout | Peer lost ability to communicate | SHOULD only if peer not responding |
| host-gone | 'to' FQDN no longer serviced | |
| host-unknown | 'to' FQDN not serviced | |
| improper-addressing | Stanza missing 'to' or 'from' on server-to-server | |
| internal-server-error | Server misconfiguration | |
| invalid-from | 'from' does not match authorized JID | |
| invalid-namespace | Stream namespace incorrect | |
| invalid-xml | XML invalid per schema | |
| not-authorized | Sent before authentication | |
| not-well-formed | Violates XML or XML-NAMES well-formedness | |
| policy-violation | Local service policy violation | E.g., stanza too large |
| remote-connection-failed | Cannot connect to remote for auth | |
| reset | Server closing stream for new features or key/expiration | Encryption and auth must re-negotiate |
| resource-constraint | Server lacks resources | |
| restricted-xml | Prohibited XML features (comment, PI, DTD, entity) | |
| see-other-host | Redirect to another host | SHOULD only after TLS; MUST resolve new host |
| system-shutdown | Server shutting down | |
| undefined-condition | Unknown condition; use with app-specific | |
| unsupported-encoding | Encoding not UTF-8 | |
| unsupported-feature | Mandatory feature not supported | |
| unsupported-stanza-type | First-level child not supported | |
| unsupported-version | Version attribute unsupported | |

#### 4.9.4 Application-Specific Conditions
May add namespaced child elements for extra info.

### 4.10 Simplified Stream Examples
Illustrates basic connection and error case.

## Section 5: STARTTLS Negotiation
### 5.1 Fundamentals
Uses TLS via STARTTLS extension. Namespace 'urn:ietf:params:xml:ns:xmpp-tls'.

### 5.2 Support
REQUIRED for clients and servers. TLS may be mandatory-to-negotiate.

### 5.3 Stream Negotiation Rules
#### 5.3.1 Mandatory-to-Negotiate
If only STARTTLS advertised or includes `<required/>`, TLS is mandatory. Other features not advertised until after TLS.

#### 5.3.2 Restart
After TLS, parties MUST restart stream.

#### 5.3.3 Data Formatting
No whitespace allowed between STARTTLS elements.

#### 5.3.4 Order: TLS before SASL (MUST).

#### 5.3.5 TLS Renegotiation
OPTIONAL. If supported, MUST implement TLS Renegotiation Extension [TLS-NEG]. If unsupported and detected, close TCP connection without stream error.

#### 5.3.6 TLS Extensions
Any extensions may be used at TLS layer.

### 5.4 Process
1. Initiator sends stream header; receiver responds with features including STARTTLS.
2. Initiator sends `<starttls xmlns='urn:ietf:params:xml:ns:xmpp-tls'/>`.
3. Receiver replies with `<proceed/>` or `<failure/>`.
4. On proceed, TLS negotiation begins; receiver MUST present certificate per MTI ciphersuites.
5. After TLS success: both parties discard insecure info, initiate new stream headers, receiver generates new stream ID and sends features (without STARTTLS, with SASL).

## Section 6: SASL Negotiation
### 6.1 Fundamentals
XMPP uses SASL for authentication. Namespace 'urn:ietf:params:xml:ns:xmpp-sasl'.

### 6.2 Support
REQUIRED.

### 6.3 Stream Negotiation Rules
#### 6.3.1 Mandatory-to-Negotiate: YES.
#### 6.3.2 Restart: After SASL, restart stream.
#### 6.3.3 Mechanism Preferences: Initiator maintains own ordered list; tries mechanisms in its order.
#### 6.3.4 Mechanism Offers: Receiver MUST NOT offer mechanisms that require TLS before TLS completed. SHOULD offer EXTERNAL if client presented acceptable certificate. SHOULD list EXTERNAL first.
#### 6.3.5 Data Formatting: No whitespace between SASL elements. Base64 encoding per [BASE64].
#### 6.3.6 Security Layers: On success, discard application-layer state.
#### 6.3.7 Simple User Name: SHOULD assume authentication identity is localpart.
#### 6.3.8 Authorization Identity: Optional; if provided, MUST be bare JID (client) or domainpart (server). Receiver MUST verify authorization.
#### 6.3.9 Realms: If not communicated, initiator MUST NOT assume realm exists.
#### 6.3.10 Round Trips: Support for initial response and additional data with success REQUIRED.

### 6.4 Process
1. Initiator sends stream header; receiver responds with features including `<mechanisms/>`.
2. Initiator selects mechanism via `<auth/>` with optional initial response.
3. Challenge-response exchange: `<challenge/>`, `<response/>`.
4. Abort: `<abort/>` -> `<failure><aborted/></failure>`.
5. Failure: `<failure/>` with defined condition.
6. Success: `<success/>` with optional additional data. Then restart stream.

### 6.5 SASL Errors
- **aborted**: Initiator aborted.
- **account-disabled**: Temporary disabled.
- **credentials-expired**: Credentials expired.
- **encryption-required**: Mechanism cannot be used without TLS.
- **incorrect-encoding**: Base64 incorrect.
- **invalid-authzid**: Authzid invalid or not allowed.
- **invalid-mechanism**: Mechanism not supported.
- **malformed-request**: Request violates mechanism syntax.
- **mechanism-too-weak**: Weaker than policy.
- **not-authorized**: Incorrect credentials; no differentiation for directory harvest prevention.
- **temporary-auth-failure**: Temporary server error.

### 6.6 SASL Definition
Service name: "xmpp". Security layer order: TCP, TLS, SASL, XMPP.

## Section 7: Resource Binding
### 7.1 Fundamentals
After SASL, client MUST bind a resource. Namespace 'urn:ietf:params:xml:ns:xmpp-bind'.

### 7.2 Support
REQUIRED.

### 7.3 Stream Negotiation Rules
- Mandatory-to-negotiate.
- No restart after binding.

### 7.4 Advertising Support
Server includes `<bind/>` in features after SASL success.

### 7.5 Generation of Resource Identifiers
Server MUST ensure uniqueness among connected resources for the same bare JID. Resourcepart may be security-critical; random or server-generated recommended.

### 7.6 Server-Generated Resource Identifier
Client sends IQ set with empty `<bind/>`. Server returns IQ result with `<jid/>`. Error cases: `<resource-constraint/>` (limit reached), `<not-allowed/>`.

### 7.7 Client-Submitted Resource Identifier
Client sends IQ set with `<resource/>` child. Server SHOULD accept; may override. Error cases: `<bad-request/>` (invalid), `<conflict/>` (already in use). Server behavior on conflict: (1) override, (2) disallow new, (3) terminate old (discouraged). Retries allowed (5-10); after limit close stream with `<policy-violation/>`.

## Section 8: XML Stanzas
### 8.1 Common Attributes
#### 8.1.1 to
Client-to-server: stanza to specific recipient MUST have 'to'; stanza for server processing MUST NOT. Server MUST NOT modify 'to' when delivering from other entity.

Server-to-server: stanza MUST have 'to'; domainpart must match receiving server's FQDN; otherwise stream error.

#### 8.1.2 from
Client-to-server: server MUST add/override 'from' with full JID. Server-generated stanzas for client must have 'from' (bare JID of server). Stanza from server on behalf of account may omit 'from'.

Server-to-server: stanza MUST have 'from'; domainpart must match sending server's FQDN; otherwise stream error.

#### 8.1.3 id
RECOMMENDED for message/presence; REQUIRED for IQ. Response/error must preserve id.

#### 8.1.4 type
Defined per stanza kind; "error" common.

#### 8.1.5 xml:lang
SHOULD be present if human-readable data. Server SHOULD add default xml:lang from stream header to stanzas lacking it. MUST NOT modify/delete.

### 8.2 Basic Semantics
#### 8.2.1 Message: Push mechanism.
#### 8.2.2 Presence: Broadcast/publish-subscribe for network availability.
#### 8.2.3 IQ: Request-response. Rules: id REQUIRED; type REQUIRED (get/set/result/error). Receiver must reply with result/error. Get/set MUST have exactly one child; result zero or one; error may have child plus `<error/>`.

### 8.3 Stanza Errors
Recoverable. Error stanza has type="error", swaps from/to, mirrors id, contains `<error/>` child.

#### 8.3.1 Rules
- SHOULD return error (MUST for IQ).
- Error stanza should swap from/to unless security risk.
- MUST preserve id.
- `<error/>` required.
- May include 'by' attribute.
- MAY include original XML (if safe).
- MUST NOT respond to error with error.

#### 8.3.2 Syntax
```xml
<stanza-kind to='sender' from='recipient' type='error'>
  [optional original payload]
  <error type='error-type'>
    <defined-condition xmlns='urn:ietf:params:xml:ns:xmpp-stanzas'/>
    [<text xml:lang='langcode'>...</text>]
    [app-specific condition]
  </error>
</stanza-kind>
```
Error types: auth, cancel, continue, modify, wait.

#### 8.3.3 Defined Stanza Error Conditions
| Condition | Description | Recommended Error Type |
|---|---|---|
| bad-request | XML does not conform to schema | modify |
| conflict | Resource name in use | cancel |
| feature-not-implemented | Feature not implemented | cancel/modify |
| forbidden | No permission | auth |
| gone | Address permanently unavailable | cancel (include new address) |
| internal-server-error | Server misconfiguration | cancel |
| item-not-found | Address/item not found | cancel (MUST NOT if would leak presence) |
| jid-malformed | JID violates rules | modify |
| not-acceptable | Request does not meet criteria | modify |
| not-allowed | Action not allowed | cancel |
| not-authorized | Credentials required | auth |
| policy-violation | Local policy violated | modify/wait |
| recipient-unavailable | Recipient temporarily unavailable | wait (MUST NOT if would leak presence) |
| redirect | Temporary redirect | modify (include alternate URI) |
| registration-required | Prior registration needed | auth |
| remote-server-not-found | Remote server does not exist | cancel |
| remote-server-timeout | Remote server unreachable | wait |
| resource-constraint | Server busy | wait |
| service-unavailable | Service not provided | cancel |
| subscription-required | Prior subscription required | auth |
| undefined-condition | Unknown condition; use with app-specific | any |
| unexpected-request | Request out of order | wait/modify |

#### 8.3.4 Application-Specific Conditions
May add namespaced child; unknown conditions ignored.

### 8.4 Extended Content
Stanzas may contain extension elements (child elements with non-content namespace) to extend semantics. Extension attributes also allowed. Recipient MUST handle unknown namespaces: for message/presence, ignore that portion; for IQ get/set, return service-unavailable error. Server MUST route/deliver unmodified.

## Section 9: Detailed Examples (Condensed)
Examples omitted for brevity; refer to original for full client-to-server and server-to-server flows.

## Section 10: Server Rules for Processing XML Stanzas
### 10.1 In-Order Processing
Server MUST ensure in-order processing over a given input stream. Applies to stream negotiation elements, stanzas addressed to same recipient (bare/full JID equivalent). Server MUST route over single output stream to remote domain to preserve order. Not responsible across multiple input streams.

### 10.2 General Considerations
Balance delivery vs. error reporting vs. preventing directory harvesting and presence leaks.

### 10.3 No 'to' Address
- Message: treat as to bare JID of sender.
- Presence: broadcast to subscribers.
- IQ: process on behalf of account; if namespace unknown, return service-unavailable.

### 10.4 Remote Domain
If 'to' domain not local, server SHOULD route to remote server over existing or new stream. If unsuccessful, return remote-server-not-found or remote-server-timeout.

### 10.5 Local Domain
If 'to' domain matches configured FQDN, server must handle. Subcases: domainpart (handle or error), domainpart/resourcepart (handle or error), localpart@domainpart (user exists or not), localpart@domainpart/resourcepart (deliver if exact match, else treat as bare JID).

## Section 11: XML Usage
### 11.1 XML Restrictions
Prohibited: comments, processing instructions, DTD subsets, entity references (except predefined). Implementation MUST NOT inject; if received, close stream with `<restricted-xml/>`.

### 11.2 XML Namespace Names and Prefixes
See Section 4.8.

### 11.3 Well-Formedness
Must generate XML-well-formed and namespace-well-formed. Must not accept non-well-formed data; close stream with `<not-well-formed/>`.

### 11.4 Validation
Optional for server; clients should ignore non-conformant data.

### 11.5 Inclusion of XML Declaration
SHOULD send XML declaration before stream header. Standalone document declaration MUST NOT be included; if received, ignore or close stream.

### 11.6 Character Encoding
MUST support UTF-8 only. MUST NOT send BOM. If other encoding detected, close stream with `<unsupported-encoding/>`.

### 11.7 Whitespace
Allowed between stanzas (except during TLS/SASL negotiation). Used for keepalives.

### 11.8 XML Versions
XMPP defined for XML 1.0 only.

## Section 12: Internationalization Considerations
UTF-8 encoding; xml:lang attributes for human-readable data; server SHOULD apply default lang.

## Section 13: Security Considerations
### 13.1 Fundamentals
Covers direct streams between two entities; multi-hop security out of scope.

### 13.2 Threat Model
Standard Internet threat model: eavesdropping, password sniffing, directory harvesting, replay, spoofing, denial of service, man-in-the-middle, etc.

### 13.3 Order of Layers
TCP → TLS → SASL → XMPP (MUST).

### 13.4 Confidentiality and Integrity
TLS provides protection per stream. No end-to-end encryption defined.

### 13.5 Peer Entity Authentication
SASL provides authentication.

### 13.6 Strong Security
Must support mutual authentication and integrity. Implementations SHOULD allow provisioning of specific trust anchors.

### 13.7 Certificates
#### 13.7.1 Certificate Generation
- End entity certificates: conform to PKIX, no basicConstraints cA=true, subject non-null, SHOULD use SHA-256, SHOULD include AIA for OCSP.
- CA certificates: MUST have keyUsage digitalSignature, subject non-null, basicConstraints cA=true.

#### 13.7.1.2 Server Certificates
- MUST support DNS-ID; REQUIRED.
- MUST support SRV-ID (_xmpp-client, _xmpp-server).
- XmppAddr identifier encouraged for backward compat.
- Wildcards allowed as leftmost label.

#### 13.7.1.3 Client Certificates
RECOMMENDED to include JIDs as XmppAddr.

#### 13.7.1.4 XmppAddr Identifier Type
OID: 1.3.6.1.5.5.7.8.5 (id-on-xmppAddr). Represented as UTF8String in subjectAltName.

#### 13.7.2 Certificate Validation
Must verify integrity, signature, path, rules, revocation. If any fail, terminate session. Should correlate validated identity with 'from' address.

#### 13.7.2.3 Long-Lived Streams
SHOULD cache expiration and check OCSP periodically; close with `<reset/>` if cert expired or revoked.

### 13.8 Mandatory-to-Implement TLS and SASL
- For auth only: SCRAM-SHA-1 and SCRAM-SHA-1-PLUS (MUST).
- For confidentiality only: TLS_RSA_WITH_AES_128_CBC_SHA (server SHOULD).
- For confidentiality+auth with passwords: TLS plus SCRAM (MUST); PLAIN over TLS only as last resort (server MUST NOT offer PLAIN without TLS).
- For confidentiality+auth without passwords: TLS plus SASL EXTERNAL (server MUST, client SHOULD).

### 13.9 Technology Reuse
- Base64: must reject non-allowed characters.
- DNS: should use secure DNS if available; certificate validation helps prevent spoofing.
- Hash functions: monitor attacks.
- SASL: protect channel via TLS before auth; prefer channel binding variant; limit retries.
- TLS: must not use SSL 2.0; verify server certificate.
- UTF-8: beware spoofing.
- XML: mitigate risks via restrictions.

### 13.10 Information Leaks
#### 13.10.1 IP Addresses: Must not be made public.
#### 13.10.2 Presence Information: Must not leak. Server must not return different errors for bare vs. full JID.

### 13.11 Directory Harvesting
Return service-unavailable to mitigate.

### 13.12 Denial of Service
Implementations SHOULD allow limits on: TCP connections per IP, connection attempts per IP, resources per account, stanza size (>=10000 bytes), stanzas per time, bandwidth. May refuse abusive stanzas.

### 13.13 Firewalls
Default ports 5222 (xmpp-client) and 5269 (xmpp-server) facilitate firewall configuration.

### 13.14 Interdomain Federation
Federation is OPTIONAL. When enabled, SHOULD use strong security. Use of Server Dialback for weak identity verification; protect channel with TLS even if certificates are self-signed.

### 13.15 Non-Repudiation
XMPP provides authentication and integrity but not non-repudiation.

## Section 14: IANA Considerations
Registers XML namespaces:
- urn:ietf:params:xml:ns:xmpp-tls (TLS data)
- urn:ietf:params:xml:ns:xmpp-sasl (SASL data)
- urn:ietf:params:xml:ns:xmpp-streams (stream errors)
- urn:ietf:params:xml:ns:xmpp-bind (resource binding)
- urn:ietf:params:xml:ns:xmpp-stanzas (stanza errors)
- GSSAPI service name: "xmpp"
- Port numbers: 5222 (xmpp-client), 5269 (xmpp-server) with updated registrations.

## Section 15: Conformance Requirements
Detailed feature set (omitted for brevity; see original for full list of MUST/SHOULD features per role).

## Section 16: References
Normative and informative as listed.

## Informative Annexes (Condensed)
- **Appendix A**: XML Schemas for stream namespaces, stream errors, STARTTLS, SASL, client/server, resource binding, stanza errors. (Full schemas can be referenced; not reproduced here.)
- **Appendix B**: Contact addresses (informative).
- **Appendix C**: Account provisioning (informative).
- **Appendix D**: Differences from RFC 3920 (informative; summarizes changes).
- **Appendix E**: Acknowledgements (informative).

## 14.3. URN Sub-namespace for Stream Error Data

- **URI**: `urn:ietf:params:xml:ns:xmpp-streams`
- **Specification**: RFC 6120
- **Description**: XML namespace name for stream error data in XMPP as defined by RFC 6120.
- **Registrant Contact**: IESG <iesg@ietf.org>

## 14.4. URN Sub-namespace for Resource Binding

- **URI**: `urn:ietf:params:xml:ns:xmpp-bind`
- **Specification**: RFC 6120
- **Description**: XML namespace name for resource binding in XMPP as defined by RFC 6120.
- **Registrant Contact**: IESG <iesg@ietf.org>

## 14.5. URN Sub-namespace for Stanza Errors

- **URI**: `urn:ietf:params:xml:ns:xmpp-stanzas`
- **Specification**: RFC 6120
- **Description**: XML namespace name for stanza error data in XMPP as defined by RFC 6120.
- **Registrant Contact**: IESG <iesg@ietf.org>

## 14.6. GSSAPI Service Name

IANA has registered "xmpp" as a [GSS-API] service name, as defined under Section 6.6.

## 14.7. Port Numbers and Service Names

IANA has registered "xmpp-client" and "xmpp-server" as keywords for [TCP] ports 5222 and 5269 respectively. Updates existing registration per [IANA-PORTS].

- **Service Name**: xmpp-client
  - **Transport Protocol**: TCP
  - **Description**: A service offering support for connections by XMPP client applications
  - **Registrant**: IETF XMPP Working Group
  - **Contact**: IESG <iesg@ietf.org>
  - **Reference**: RFC 6120
  - **Port Number**: 5222

- **Service Name**: xmpp-server
  - **Transport Protocol**: TCP
  - **Description**: A service offering support for connections by XMPP server applications
  - **Registrant**: IETF XMPP Working Group
  - **Contact**: IESG <iesg@ietf.org>
  - **Reference**: RFC 6120
  - **Port Number**: 5269

## 15. Conformance Requirements

This section describes a protocol feature set summarizing conformance requirements of this specification. For each feature: human-readable name, description, reference to normatively defining section, applicability to Client/Server roles, and required implementation level (MUST/SHOULD/MAY).

| Feature | Description | Section | Client | Server |
|---|---|---|---|---|
| bind-gen | Generate a random resource on demand. | Section 7.6 | N/A | MUST |
| bind-mtn | Consider resource binding as mandatory-to-negotiate. | Section 7.3.1 | MUST | MUST |
| bind-restart | Do not restart the stream after negotiation of resource binding. | Section 7.3.2 | MUST | MUST |
| bind-support | Support binding of client resources to an authenticated stream. | Section 7 | MUST | MUST |
| sasl-correlate | When authenticating a stream peer using SASL, correlate the authentication identifier resulting from SASL negotiation with the 'from' address (if any) of the stream header it received from the peer. | Section 6.4.6 | SHOULD | SHOULD |
| sasl-errors | Support SASL errors during the negotiation process. | Section 6.5 | MUST | MUST |
| sasl-mtn | Consider SASL as mandatory-to-negotiate. | Section 6.3.1 | MUST | MUST |
| sasl-restart | Initiate or handle a stream restart after SASL negotiation. | Section 6.3.2 | MUST | MUST |
| sasl-support | Support the Simple Authentication and Security Layer for stream authentication. | Section 6 | MUST | MUST |
| security-mti-auth-scram | Support the SASL SCRAM mechanism for authentication only (implies support for both SCRAM-SHA-1 and SCRAM-SHA-1-PLUS variants). | Section 13.8 | MUST | MUST |
| security-mti-both-external | Support TLS with SASL EXTERNAL for confidentiality and authentication. | Section 13.8 | SHOULD | MUST |
| security-mti-both-plain | Support TLS using TLS_RSA_WITH_AES_128_CBC_SHA ciphersuite plus SASL PLAIN for confidentiality and authentication. | Section 13.8 | SHOULD | MAY |
| security-mti-both-scram | Support TLS using TLS_RSA_WITH_AES_128_CBC_SHA ciphersuite plus SCRAM-SHA-1/SCRAM-SHA-1-PLUS for confidentiality and authentication. | Section 13.8 | MUST | MUST |
| security-mti-confidentiality | Support TLS using TLS_RSA_WITH_AES_128_CBC_SHA for confidentiality only. | Section 13.8 | N/A | SHOULD |
| stanza-attribute-from | Support the common 'from' attribute for all stanza kinds. | Section 8.1.2 | MUST | MUST |
| stanza-attribute-from-stamp | Stamp or rewrite the 'from' address of all stanzas received from connected clients. | Section 8.1.2.1 | N/A | MUST |
| stanza-attribute-from-validate | Validate the 'from' address of all stanzas received from peer servers. | Section 8.1.2.2 | N/A | MUST |
| stanza-attribute-id | Support the common 'id' attribute for all stanza kinds. | Section 8.1.3 | MUST | MUST |
| stanza-attribute-to | Support the common 'to' attribute for all stanza kinds. | Section 8.1.1 | MUST | MUST |
| stanza-attribute-to-validate | Ensure that all stanzas received from peer servers include a 'to' address. | Section 8.1.1 | N/A | MUST |
| stanza-attribute-type | Support the common 'type' attribute for all stanza kinds. | Section 8.1.4 | MUST | MUST |
| stanza-attribute-xmllang | Support the common 'xml:lang' attribute for all stanza kinds. | Section 8.1.5 | MUST | MUST |
| stanza-error | Generate and handle stanzas of type "error" for all stanza kinds. | Section 8.3 | MUST | MUST |
| stanza-error-child | Ensure that stanzas of type "error" include an <error/> child element. | Section 8.3 | MUST | MUST |
| stanza-error-id | Ensure that stanzas of type "error" preserve the 'id' provided in the triggering stanza. | Section 8.3 | MUST | MUST |
| stanza-error-reply | Do not reply to a stanza of type "error" with another stanza of type "error". | Section 8.3 | MUST | MUST |
| stanza-extension | Correctly process XML data qualified by an unsupported XML namespace: for message/presence stanzas, ignore that portion; for IQ stanzas, return error; for routing entities, route or deliver. | Section 8.4 | MUST | MUST |
| stanza-iq-child | Include exactly one child element in an <iq/> stanza of type "get" or "set", zero or one in type "result", and one or two in type "error". | Section 8.2.3 | MUST | MUST |
| stanza-iq-id | Ensure that all <iq/> stanzas include an 'id' attribute. | Section 8.2.3 | MUST | MUST |
| stanza-iq-reply | Reply to an <iq/> stanza of type "get" or "set" with an <iq/> stanza of type "result" or "error". | Section 8.2.3 | MUST | MUST |
| stanza-iq-type | Ensure that all <iq/> stanzas include a 'type' attribute whose value is "get", "set", "result", or "error". | Section 8.2.3 | MUST | MUST |
| stanza-kind-iq | Support the <iq/> stanza. | Section 8.2.3 | MUST | MUST |
| stanza-kind-message | Support the <message/> stanza. | Section 8.2.1 | MUST | MUST |
| stanza-kind-presence | Support the <presence/> stanza. | Section 8.2.2 | MUST | MUST |
| stream-attribute-initial-from | Include a 'from' attribute in the initial stream header. | Section 4.7.1 | SHOULD | MUST |
| stream-attribute-initial-lang | Include an 'xml:lang' attribute in the initial stream header. | Section 4.7.4 | SHOULD | SHOULD |
| stream-attribute-initial-to | Include a 'to' attribute in the initial stream header. | Section 4.7.2 | MUST | MUST |
| stream-attribute-response-from | Include a 'from' attribute in the response stream header. | Section 4.7.1 | N/A | MUST |
| stream-attribute-response-id | Include an 'id' attribute in the response stream header. | Section 4.7.3 | N/A | MUST |
| stream-attribute-response-id-unique | Ensure that the 'id' attribute in the response stream header is unique within the context of the receiving entity. | Section 4.7.3 | N/A | MUST |
| stream-attribute-response-to | Include a 'to' attribute in the response stream header. | Section 4.7.2 | N/A | SHOULD |
| stream-error-generate | Generate a stream error (followed by closing stream tag and TCP connection termination) upon detecting a stream-related error condition. | Section 4.9 | MUST | MUST |
| stream-fqdn-resolution | Resolve FQDNs before opening a TCP connection to the receiving entity. | Section 3.2 | MUST | MUST |
| stream-negotiation-complete | Do not consider stream negotiation complete until the receiving entity sends a stream features advertisement that is empty or contains only voluntary-to-negotiate features. | Section 4.3.5 | MUST | MUST |
| stream-negotiation-features | Send stream features after sending a response stream header. | Section 4.3.2 | N/A | MUST |
| stream-negotiation-restart | Consider the previous stream replaced upon negotiation of a feature that necessitates a stream restart; send/receive a new initial stream header. | Section 4.3.3 | MUST | MUST |
| stream-reconnect | Reconnect with exponential backoff if a TCP connection is terminated unexpectedly. | Section 3.3 | MUST | MUST |
| stream-tcp-binding | Bind an XML stream to a TCP connection. | Section 3 | MUST | MUST |
| tls-certs | Check the identity specified in a certificate presented during TLS negotiation. | Section 13.7.2 | MUST | MUST |
| tls-mtn | Consider TLS as mandatory-to-negotiate if STARTTLS is the only feature advertised or the STARTTLS feature includes an empty <required/> element. | Section 5.3.1 | MUST | MUST |
| tls-restart | Initiate or handle a stream restart after TLS negotiation. | Section 5.3.2 | MUST | MUST |
| tls-support | Support Transport Layer Security for stream encryption. | Section 5 | MUST | MUST |
| tls-correlate | When validating a certificate presented during TLS negotiation, correlate the validated identity with the 'from' address (if any) of the stream header received from the peer. | Section 13.7.2 | SHOULD | SHOULD |
| xml-namespace-content-client | Support 'jabber:client' as a content namespace. | Section 4.8.2 | MUST | MUST |
| xml-namespace-content-server | Support 'jabber:server' as a content namespace. | Section 4.8.2 | N/A | MUST |
| xml-namespace-streams-declaration | Ensure a namespace declaration for the 'http://etherx.jabber.org/streams' namespace. | Section 4.8.1 | MUST | MUST |
| xml-namespace-streams-prefix | Ensure that all elements qualified by the 'http://etherx.jabber.org/streams' namespace are prefixed by the prefix defined in the namespace declaration. | Section 4.8.1 | MUST | MUST |
| xml-restriction-comment | Do not generate or accept XML comments. | Section 11.1 | MUST | MUST |
| xml-restriction-dtd | Do not generate or accept internal or external DTD subsets. | Section 11.1 | MUST | MUST |
| xml-restriction-pi | Do not generate or accept XML processing instructions. | Section 11.1 | MUST | MUST |
| xml-restriction-ref | Do not generate or accept internal or external entity references except predefined entities. | Section 11.1 | MUST | MUST |
| xml-wellformed-xml | Do not generate or accept data that is not XML-well-formed. | Section 11.3 | MUST | MUST |
| xml-wellformed-ns | Do not generate or accept data that is not namespace-well-formed. | Section 11.3 | MUST | MUST |

## 16. References

### 16.1. Normative References

- [BASE64] RFC 4648
- [CHANNEL] RFC 5056
- [CHANNEL-TLS] RFC 5929
- [CHARSETS] BCP 18, RFC 2277
- [DNS-CONCEPTS] STD 13, RFC 1034
- [DNS-SRV] RFC 2782
- [IPv6-ADDR] RFC 5952
- [KEYWORDS] BCP 14, RFC 2119
- [LANGMATCH] BCP 47, RFC 4647
- [LANGTAGS] BCP 47, RFC 5646
- [OCSP] RFC 2560
- [PKIX] RFC 5280
- [PKIX-ALGO] RFC 3447
- [PKIX-SRV] RFC 4985
- [PLAIN] RFC 4616
- [RANDOM] BCP 106, RFC 4086
- [SASL] RFC 4422
- [SCRAM] RFC 5802
- [STRONGSEC] BCP 61, RFC 3365
- [TCP] STD 7, RFC 793
- [TLS] RFC 5246
- [TLS-CERTS] RFC 6125
- [TLS-NEG] RFC 5746
- [TLS-SSL2] RFC 6176
- [UCS2] ISO 10646-1 Addendum 2
- [UNICODE] Unicode Standard Version 6.0
- [UTF-8] STD 63, RFC 3629
- [URI] STD 66, RFC 3986
- [X509] ITU-T X.509 / ISO 9594-8
- [XML] W3C REC-xml-20081126
- [XML-GUIDE] BCP 70, RFC 3470
- [XML-MEDIA] RFC 3023
- [XML-NAMES] W3C REC-xml-names-20091208
- [XMPP-ADDR] RFC 6122
- [XMPP-IM] RFC 6121

### 16.2. Informative References

- [AAA] BCP 132, RFC 4962
- [ABNF] STD 68, RFC 5234
- [ACAP] RFC 2244
- [ANONYMOUS] RFC 4505
- [ASN.1] CCITT X.208
- [DIGEST-MD5] RFC 2831
- [DNSSEC] RFC 4033
- [DNS-TXT] RFC 1464
- [DOS] RFC 4732
- [E2E-REQS] Work in Progress
- [EMAIL-ARCH] RFC 5598
- [ETHERNET] IEEE 802.3
- [GSS-API] RFC 2743
- [HASHES] RFC 4270
- [HTTP] RFC 2616
- [IANA-GUIDE] BCP 26, RFC 5226
- [IANA-PORTS] Work in Progress
- [IMAP] RFC 3501
- [IMP-REQS] RFC 2779
- [INTEROP] Work in Progress
- [IRC] RFC 2810
- [IRI] RFC 3987
- [LDAP] RFC 4510
- [LINKLOCAL] RFC 3927
- [MAILBOXES] RFC 2142
- [POP3] STD 53, RFC 1939
- [PROCESS] BCP 9, RFC 2026
- [REPORTS] BCP 9, RFC 5657
- [REST] Fielding, 2000
- [RFC3920] RFC 3920
- [RFC3921] RFC 3921
- [SASLPREP] RFC 4013
- [SEC-TERMS] RFC 4949
- [SMTP] RFC 5321
- [SEC-GUIDE] BCP 72, RFC 3552
- [TLS-EXT] RFC 6066
- [TLS-RESUME] RFC 5077
- [URN-OID] RFC 3061
- [USINGTLS] RFC 2595
- [UUID] RFC 4122
- [XEP-0001] XSF XEP 0001
- [XEP-0016] XSF XEP 0016
- [XEP-0045] XSF XEP 0045
- [XEP-0060] XSF XEP 0060
- [XEP-0071] XSF XEP 0071
- [XEP-0077] XSF XEP 0077
- [XEP-0086] XSF XEP 0086
- [XEP-0100] XSF XEP 0100
- [XEP-0114] XSF XEP 0114
- [XEP-0124] XSF XEP 0124
- [XEP-0138] XSF XEP 0138
- [XEP-0156] XSF XEP 0156
- [XEP-0160] XSF XEP 0160
- [XEP-0174] XSF XEP 0174
- [XEP-0175] XSF XEP 0175
- [XEP-0178] XSF XEP 0178
- [XEP-0191] XSF XEP 0191
- [XEP-0198] XSF XEP 0198
- [XEP-0199] XSF XEP 0199
- [XEP-0205] XSF XEP 0205
- [XEP-0206] XSF XEP 0206
- [XEP-0220] XSF XEP 0220
- [XEP-0225] XSF XEP 0225
- [XEP-0233] XSF XEP 0233
- [XEP-0288] XSF XEP 0288
- [XML-FRAG] W3C CR-xml-fragment-20010212
- [XML-REG] BCP 81, RFC 3688
- [XML-SCHEMA] W3C REC-xmlschema-1-20041028
- [XMPP-URI] RFC 5122

## Appendix A. XML Schemas (Informative)

The following schemas formally define various namespaces used in this document, in conformance with [XML-SCHEMA]. Because validation of XML streams and stanzas is optional, these schemas are not normative and are provided for descriptive purposes only.

- **A.1. Stream Namespace**: Defines elements `<stream>`, `<features>`, `<error>` in namespace `http://etherx.jabber.org/streams`.
- **A.2. Stream Error Namespace**: Defines stream error condition elements (e.g., `<bad-format>`, `<not-well-formed>`) and `<text>` element in `urn:ietf:params:xml:ns:xmpp-streams`.
- **A.3. STARTTLS Namespace**: Defines `<starttls>`, `<proceed>`, `<failure>` elements in `urn:ietf:params:xml:ns:xmpp-tls`.
- **A.4. SASL Namespace**: Defines `<mechanisms>`, `<auth>`, `<challenge>`, `<response>`, `<success>`, `<failure>` elements in `urn:ietf:params:xml:ns:xmpp-sasl`.
- **A.5. Client Namespace**: Defines stanzas and their children (`<message>`, `<presence>`, `<iq>`, `<error>`) for `jabber:client` namespace.
- **A.6. Server Namespace**: Defines stanzas with required `from` and `to` attributes for `jabber:server` namespace.
- **A.7. Resource Binding Namespace**: Defines `<bind>` element with `<resource>` and `<jid>` in `urn:ietf:params:xml:ns:xmpp-bind`.
- **A.8. Stanza Error Namespace**: Defines stanza error condition elements (e.g., `<bad-request>`, `<forbidden>`) and `<text>` in `urn:ietf:params:xml:ns:xmpp-stanzas`.

## Appendix B. Contact Addresses (Informative)

Organizations offering XMPP services are encouraged to provide an Internet mailbox of "XMPP" for inquiries, using the organization's domain as the host (e.g., xmpp@example.com), consistent with [MAILBOXES].

## Appendix C. Account Provisioning (Informative)

Account provisioning is out of scope. Possible methods include server administrator creation or in-band registration via `jabber:iq:register` [XEP-0077]. Any assigned JID MUST conform to the canonical format defined in [XMPP-ADDR].

## Appendix D. Differences from RFC 3920 (Informative)

Substantive modifications from RFC 3920 include:
- Moved XMPP address format to separate document.
- Recommended/mandated use of 'from' and 'to' attributes on stream headers.
- More fully specified stream closing handshake.
- Specified recommended stream reconnection algorithm.
- Renamed `<xml-not-well-formed/>` to `<not-well-formed/>` for XML compliance.
- Removed unused `<invalid-id/>` stream error.
- Specified return of `<restricted-xml/>` stream error for prohibited XML.
- More completely specified `<see-other-host/>` error including IPv6 address format.
- Mandated SASL SCRAM for client-to-server streams.
- Mandated TLS + SASL PLAIN for client-to-server streams.
- Required SASL EXTERNAL for servers, recommended for clients.
- Removed hard two-connection rule for server-to-server streams.
- Clarified certificate profile.
- Added `<reset/>` stream error for expired/revoked certificates or security-critical additions.
- Added SASL error conditions: `<account-disabled/>`, `<credentials-expired/>`, `<encryption-required/>`, `<malformed-request/>`.
- Removed unused `<payment-required/>` stanza error.
- Removed requirement for escaping predefined entities.
- Clarified DNS SRV lookups, SASL security layers, stream negotiation process.
- Added 'by' attribute to `<error/>` element for stanza errors.
- Clarified handling of data violating XML well-formedness definitions.
- More detailed security considerations, especially presence leaks and DoS.
- Moved Server Dialback protocol to a separate specification.

## Appendix E. Acknowledgements (Informative)

This document updates RFC 3920. The editor thanks the many contributors and commenters, with special thanks to Kevin Smith, Matthew Wild, Dave Cridland, Philipp Hancke, Waqas Hussain, Florian Zeitz, Ben Campbell, Jehan Pages, Paul Aurich, Justin Karneges, Kurt Zeilenga, Simon Josefsson, Ralph Meijer, Curtis King, Yaron Sheffer, Elwyn Davies, and Working Group chairs Ben Campbell and Joe Hildebrand. Responsible Area Director: Gonzalo Camarillo. Author: Peter Saint-Andre (Cisco).