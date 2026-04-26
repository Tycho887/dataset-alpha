# RFC 3920: Extensible Messaging and Presence Protocol (XMPP): Core
**Source**: IETF | **Version**: Standards Track | **Date**: October 2004 | **Type**: Normative

## Scope (Summary)
This memo defines the core features of XMPP, a protocol for streaming XML elements to exchange structured information near real-time between network endpoints. It provides a generalized framework for exchanging XML data, primarily used for instant messaging and presence applications meeting RFC 2779 [IMP-REQS].

## Normative References
- [ABNF] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 2234, November 1997.
- [BASE64] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 3548, July 2003.
- [CHARSET] Alvestrand, H., "IETF Policy on Character Sets and Languages", BCP 18, RFC 2277, January 1998.
- [DIGEST-MD5] Leach, P. and C. Newman, "Using Digest Authentication as a SASL Mechanism", RFC 2831, May 2000.
- [DNS] Mockapetris, P., "Domain names - implementation and specification", STD 13, RFC 1035, November 1987.
- [GSS-API] Linn, J., "Generic Security Service Application Program Interface Version 2, Update 1", RFC 2743, January 2000.
- [HTTP-TLS] Rescorla, E., "HTTP Over TLS", RFC 2818, May 2000.
- [IDNA] Faltstrom, P., Hoffman, P., and A. Costello, "Internationalizing Domain Names in Applications (IDNA)", RFC 3490, March 2003.
- [IPv6] Hinden, R. and S. Deering, "Internet Protocol Version 6 (IPv6) Addressing Architecture", RFC 3513, April 2003.
- [LANGTAGS] Alvestrand, H., "Tags for the Identification of Languages", BCP 47, RFC 3066, January 2001.
- [NAMEPREP] Hoffman, P. and M. Blanchet, "Nameprep: A Stringprep Profile for Internationalized Domain Names (IDN)", RFC 3491, March 2003.
- [RANDOM] Eastlake 3rd, D., Crocker, S., and J. Schiller, "Randomness Recommendations for Security", RFC 1750, December 1994.
- [SASL] Myers, J., "Simple Authentication and Security Layer (SASL)", RFC 2222, October 1997.
- [SRV] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [STRINGPREP] Hoffman, P. and M. Blanchet, "Preparation of Internationalized Strings ('stringprep')", RFC 3454, December 2002.
- [TCP] Postel, J., "Transmission Control Protocol", STD 7, RFC 793, September 1981.
- [TERMS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [TLS] Dierks, T. and C. Allen, "The TLS Protocol Version 1.0", RFC 2246, January 1999.
- [UCS2] ISO/IEC 10646-1, "Information Technology - Universal Multiple-octet coded Character Set (UCS) - Amendment 2: UCS Transformation Format 8 (UTF-8)", October 1996.
- [UTF-8] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [X509] Housley, R., Polk, W., Ford, W., and D. Solo, "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, April 2002.
- [XML] Bray, T., Paoli, J., Sperberg-McQueen, C., and E. Maler, "Extensible Markup Language (XML) 1.0 (2nd ed)", W3C REC-xml, October 2000, <http://www.w3.org/TR/REC-xml>.
- [XML-NAMES] Bray, T., Hollander, D., and A. Layman, "Namespaces in XML", W3C REC-xml-names, January 1999, <http://www.w3.org/TR/REC-xml-names>.

## Definitions and Abbreviations
- **JID (Jabber Identifier)**: An XMPP entity address, consisting of node identifier (optional), domain identifier, and resource identifier (optional), formatted as `[node "@"] domain [ "/" resource ]`.
- **XML Stream**: A container for exchanging XML elements between two entities over a network, delimited by `<stream>` tags. The initial stream is from initiating entity to receiving entity; the response stream is the opposite direction.
- **XML Stanza**: A discrete semantic unit of structured information sent over an XML stream, one of `<message/>`, `<presence/>`, or `<iq/>` qualified by the default namespace. Elements used for TLS, SASL, or dialback negotiation are not stanzas.
- **Bare JID**: `<node@domain>`.
- **Full JID**: `<node@domain/resource>`.
- **Originating Server / Receiving Server / Authoritative Server**: Terms used in server dialback (Section 8).
- **Required, SHOULD, MAY, etc.**: Interpreted per BCP 14, RFC 2119.

## 1. Introduction
### 1.1 Overview
XMPP is an open XML protocol for near-real-time messaging, presence, and request-response services. Developed originally in the Jabber community, adapted by the IETF XMPP WG. Core features defined here; instant messaging and presence extensions are in [XMPP-IM].

### 1.2 Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119.

## 2. Generalized Architecture
### 2.1 Overview
XMPP typically uses a client-server architecture over TCP. Servers communicate with each other over TCP. Diagram shows clients, servers, gateways, foreign networks.

### 2.2 Server
A server manages XML streams to/from clients, servers, and other entities, and routes appropriately-addressed XML stanzas. Servers may store client data (e.g., contact lists).

### 2.3 Client
Clients connect to a server over TCP. Multiple resources (e.g., devices) MAY connect simultaneously, differentiated by resource identifier. RECOMMENDED port for client-server: 5222.

### 2.4 Gateway
A server-side service translating XMPP to foreign messaging protocols (e.g., SMTP, IRC, SIMPLE, SMS). Communications beyond XMPP are not defined.

### 2.5 Network
Servers inter-communicate, creating a network. Server-to-server communications are OPTIONAL; if enabled, SHOULD occur over TCP. RECOMMENDED port: 5269. Both ports registered with IANA.

## 3. Addressing Scheme
### 3.1 Overview
All entities are addressable by a JID, which conforms to RFC 2396 [URI]. Syntax (ABNF):
```
jid       = [ node "@" ] domain [ "/" resource ]
domain    = fqdn / address-literal
fqdn      = (sub-domain 1*("." sub-domain))
sub-domain = (internationalized domain label)
address-literal = IPv4address / IPv6address
```
JID example: `user@host/resource`. Must follow specific stringprep profiles for node and resource. Each portion MUST NOT exceed 1023 bytes; total max 3071 bytes.

### 3.2 Domain Identifier
The primary identifier, REQUIRED. May be IP address but SHOULD be FQDN. MUST be an IDN [IDNA], to which Nameprep [NAMEPREP] can be applied without failing. Before comparing, server MUST apply Nameprep; client SHOULD.

### 3.3 Node Identifier
Optional secondary identifier before '@'. Must be formatted per Nodeprep profile (Appendix A). Before comparing, server MUST apply Nodeprep; client SHOULD.

### 3.4 Resource Identifier
Optional tertiary identifier after '/'. Must be formatted per Resourceprep profile (Appendix B). Before comparing, server MUST apply Resourceprep; client SHOULD. Resource is typically defined during Resource Binding (Section 7).

### 3.5 Determination of Addresses
After SASL and resource binding, the receiving entity MUST determine the initiating entity's JID. For server-to-server, the authorization identity derived from authentication identity SHOULD be used. For client-to-server, the bare JID SHOULD be the authorization identity; full JID includes resource from binding. Receiving entity MUST ensure JID conforms to syntax rules.

## 4. XML Streams
### 4.1 Overview
XML Stream is a container; start is `<stream>` tag, end is `</stream>`. The initiating entity sends initial stream; the receiving entity MUST open a response stream for bidirectional communication. XML stanzas are child elements at depth=1 of the root `<stream/>`: `<message/>`, `<presence/>`, `<iq/>`. They must be well-balanced per XML.

### 4.2 Binding to TCP
XMPP is bound to TCP. Client-to-server: MUST allow sharing a single TCP connection for both directions. Server-to-server: MUST use one TCP connection per direction (initiated by each server), total two.

### 4.3 Stream Security
TLS SHOULD be used (Section 5); SASL MUST be used (Section 6). Initial and response streams MUST be secured separately. Entities SHOULD NOT send stanzas before authentication; if they do, other entity MUST NOT accept stanzas and SHOULD return a `<not-authorized/>` stream error and terminate stream and TCP.

### 4.4 Stream Attributes
- `to`: SHOULD be used only in initial stream header, set to hostname of receiving entity. No `to` in response header; if present, SHOULD be silently ignored.
- `from`: SHOULD be used only in response stream header, set to hostname of receiving entity. No `from` in initial header; if present, SHOULD be silently ignored.
- `id`: SHOULD be used only in response header, unique session key, MUST be unpredictable and non-repeating.
- `xml:lang`: SHOULD be included in initial header for default language. Receiving entity SHOULD remember that value; if absent, use configurable default. If included in stanza, MUST NOT modify or delete. Value MUST be NMTOKEN per RFC 3066.
- `version`: Presence with value at least "1.0" signals support for stream-related protocols (TLS, SASL, stream errors) and basic stanza semantics.

### 4.4.1 Version Support
XMPP version "1.0". Versioning scheme `<major>.<minor>`. Major increments only if backward compatibility broken; minor indicates new capabilities. Rules:
1. Initiating entity MUST set version to highest supported (e.g., "1.0").
2. Receiving entity MUST set response version to lower of initiating or its own.
3. If response is at least one major lower and incompatible, initiating entity SHOULD send `<unsupported-version/>` stream error and terminate.
4. If no version attribute, consider "0.0"; SHOULD omit version in reply.

### 4.5 Namespace Declarations
Stream element MUST have a streams namespace declaration (e.g., `xmlns:stream='http://etherx.jabber.org/streams'`) and a default namespace declaration (e.g., `xmlns='jabber:client'` or `jabber:server`).

### 4.6 Stream Features
If version >= 1.0, receiving entity MUST send a `<features/>` child element to announce negotiable features (TLS, SASL, Resource Binding, etc.). If a non-security feature requires prior security, it SHOULD NOT be advertised before security negotiated.

### 4.7 Stream Errors
Root stream element may contain an `<error/>` child (prefixed streams namespace). All stream errors are unrecoverable; entity MUST send error, closing `</stream>`, and terminate TCP. If error during stream setup, server MUST still send opening `<stream>` tag with error child.

### 4.7.2 Syntax
```
<stream:error>
  <defined-condition xmlns='urn:ietf:params:xml:ns:xmpp-streams'/>
  <text xmlns='urn:ietf:params:xml:ns:xmpp-streams' xml:lang='langcode'>OPTIONAL</text>
  [OPTIONAL application-specific condition element]
</stream:error>
```
- Error element MUST contain a child from defined conditions.
- May contain `<text/>` (OPTIONAL), SHOULD have `xml:lang`.
- May contain application-specific condition.

### 4.7.3 Defined Conditions
- `<bad-format/>`
- `<bad-namespace-prefix/>`
- `<conflict/>`
- `<connection-timeout/>`
- `<host-gone/>`
- `<host-unknown/>`
- `<improper-addressing/>`
- `<internal-server-error/>`
- `<invalid-from/>`
- `<invalid-id/>`
- `<invalid-namespace/>`
- `<invalid-xml/>`
- `<not-authorized/>`
- `<policy-violation/>`
- `<remote-connection-failed/>`
- `<resource-constraint/>`
- `<restricted-xml/>`
- `<see-other-host/>`
- `<system-shutdown/>`
- `<undefined-condition/>`
- `<unsupported-encoding/>`
- `<unsupported-stanza-type/>`
- `<unsupported-version/>`
- `<xml-not-well-formed/>`

### 4.7.4 Application-Specific Conditions
May be included; SHOULD supplement a defined condition.

### 4.8 Simplified Stream Examples
Two examples: a normal session and a session with error. (Informative, preserved as reference.)

## 5. Use of TLS
### 5.1 Overview
XMPP uses TLS for channel encryption, via STARTTLS extension (namespace `urn:ietf:params:xml:ns:xmpp-tls`). Rules:
1. Initiating entity MUST include version >= 1.0.
2. If server-to-server, communications MUST NOT proceed until DNS hostnames resolved.
3. Receiving entity MUST include `<starttls/>` in stream features if version >= 1.0.
4. TLS MUST be completed before SASL.
5. No white space between elements during TLS negotiation.
6. TLS negotiation begins after closing '>' of `<proceed/>` element.
7. Initiating entity MUST validate certificate.
8. Certificates MUST be checked against hostname as provided by initiating entity (not resolved DNS name). JID in certificate as UTF8String subjectAltName with OID id-on-xmppAddr (1.3.6.1.5.5.7.8.5).
9. After successful TLS, receiving entity MUST discard insecure knowledge.
10. After successful TLS, initiating entity MUST discard insecure knowledge.
11. After successful TLS, receiving entity MUST NOT offer STARTTLS again.
12. After successful TLS, initiating entity MUST continue with SASL.
13. If TLS fails, receiving entity MUST terminate stream and TCP.
14. Mandatory-to-implement technologies (Section 14.7).

### 5.1.1 ASN.1 Object Identifier for XMPP Address
Defined as id-on-xmppAddr ::= { id-on 5 }, represented as UTF8String.

### 5.2 Narrative
Steps: initiate stream -> server replies with features including starttls -> client sends `<starttls/>` -> server replies with `<proceed/>` or `<failure/>` -> TLS negotiation -> if successful, initiate new stream (no closing tag needed, original stream considered closed) -> server responds with new stream and features (without starttls).

### 5.3 Client-to-Server Example
(Informative example showing steps 1-9.)

### 5.4 Server-to-Server Example
(Informative example.)

## 6. Use of SASL
### 6.1 Overview
XMPP uses SASL for authentication (namespace `urn:ietf:params:xml:ns:xmpp-sasl`). Rules:
1. If server-to-server, communications MUST NOT proceed until DNS hostnames resolved.
2. Initiating entity MUST include version >= 1.0.
3. Receiving entity MUST advertise mechanisms in `<mechanisms/>` element.
4. No white space between elements during SASL negotiation.
5. All base64 data MUST adhere to RFC 3548 Section 3.
6. Simple username SHOULD be sending domain (server-to-server) or account name (client-to-server).
7. If acting on behalf of another entity, authorization identity MUST be provided (form `<domain>` for servers, `<node@domain>` for clients). If not, MUST NOT provide.
8. After successful SASL with security layer, receiving entity MUST discard insecure knowledge.
9. After successful SASL with security layer, initiating entity MUST discard insecure knowledge.
10. Mandatory-to-implement technologies (Section 14.7).

### 6.2 Narrative
Steps: initiate stream with version -> server advertises mechanisms -> client sends `<auth>` with mechanism -> server challenges with `<challenge>` -> client responds with `<response>` -> loop until success, failure, or abort. On success, both sides consider original stream closed; initiate new stream. On failure, allow configurable retries (at least 2), then terminate TCP.

### 6.3 SASL Definition
- service name: "xmpp"
- initiation: after stream headers, server lists mechanisms, client chooses.
- exchange: challenges and responses; success/failure/abort.
- security layer: takes effect after closing '>' of `<success/>`.
- authorization identity: used to denote non-default `<node@domain>` or `<domain>`.

### 6.4 SASL Errors
- `<aborted/>`
- `<incorrect-encoding/>`
- `<invalid-authzid/>`
- `<invalid-mechanism/>`
- `<mechanism-too-weak/>`
- `<not-authorized/>`
- `<temporary-auth-failure/>`

### 6.5 Client-to-Server Example
(Informative example.)

### 6.6 Server-to-Server Example
(Informative example.)

## 7. Resource Binding
After SASL, client MAY bind a resource. Server MUST include empty `<bind/>` element in stream features if required. Client MUST send IQ type='set' with `<bind/>` child. Client may allow server to generate resource (empty `<bind/>`) or specify `<resource>`. Server MUST generate unique resource identifier if none provided. Server MUST return IQ result with `<jid/>` child containing full JID. Server SHOULD accept client-provided resource but MAY override. Errors: `<bad-request/>` (modify), `<not-allowed/>` (cancel), `<conflict/>` (cancel). Before binding, server MUST NOT process other stanzas; SHOULD return `<not-authorized/>` stanza error.

## 8. Server Dialback
### 8.1 Overview
Server dialback is a weak verification method to prevent domain spoofing, not a security mechanism. Domains requiring robust security SHOULD use TLS and SASL. If SASL used, dialback SHOULD NOT be used. Dialback is unidirectional; MUST be done in both directions for bidirectional communications. Key generation must use hostnames, stream ID, and a secret. Stream ID MUST be unpredictable and non-repeating. Errors during dialback are stream errors.

### 8.2 Order of Events
1. Originating Server connects to Receiving Server.
2. Originating sends key.
3. Receiving connects to Authoritative Server.
4. Receiving sends key to Authoritative.
5. Authoritative replies valid/invalid.
6. Receiving informs Originating.

### 8.3 Protocol
Detailed steps with namespace `jabber:server:dialback`. Key points:
- If namespace incorrect, generate `<invalid-namespace/>` stream error.
- If `to` address not recognized, `<host-unknown/>` error.
- If `from` matches existing connection, maintain existing until validation.
- Receiving Server MUST verify `to` and `from` in subsequent stanzas; if missing, `<improper-addressing/>`; if `from` not validated, `<invalid-from/>`.
- After validation, `db:result` with type='valid' allows data.

## 9. XML Stanzas
### 9.1 Common Attributes
Five attributes: `to`, `from`, `id`, `type`, `xml:lang`.

#### 9.1.1 to
Specifies recipient JID. In `jabber:client`, SHOULD possess (except for server-handled stanzas). In `jabber:server`, MUST possess; if missing, `<improper-addressing/>` stream error.

#### 9.1.2 from
Specifies sender JID. For client-to-server, server MUST either validate sender's from or add a from (bare JID or full JID). If client sends with incorrect from, server SHOULD return `<invalid-from/>` stream error. Server-generated stanzas MUST either omit from or use account's bare/full JID. In `jabber:server`, MUST possess; domain identifier MUST match sending server's validated domain; otherwise `<invalid-from/>` stream error.

#### 9.1.3 id
Optional, used for tracking. REQUIRED for IQ stanzas (Section 9.2.3).

#### 9.1.4 type
Varies per stanza kind. For IQ: get, set, result, error. For message/presence: defined in [XMPP-IM]. Only common type is "error".

#### 9.1.5 xml:lang
SHOULD be present if human-readable content. Default language from stream if not present. Value NMTOKEN per RFC 3066.

### 9.2 Basic Semantics
#### 9.2.1 Message Semantics
Push mechanism. All message stanzas SHOULD have a `to` attribute; server SHOULD route/deliver (Section 10).

#### 9.2.2 Presence Semantics
Broadcast/publish-subscribe. Generally, entity sends presence with no `to` for broadcast; with `to` for directed delivery. Server SHOULD route/deliver accordingly.

#### 9.2.3 IQ Semantics
Request-response (like HTTP). Rules:
1. `id` REQUIRED.
2. `type` REQUIRED: get, set, result, error.
3. Receiver of get/set MUST reply with result or error, preserving `id`.
4. Receiver of result/error MUST NOT respond with further result/error.
5. get/set MUST contain exactly one child element.
6. result MUST contain zero or one child.
7. error SHOULD include original child and MUST include `<error/>`.

### 9.3 Stanza Errors
Recoverable errors. Entity detecting error MUST return a stanza of same kind with type='error', including original XML (RECOMMENDED). Error stanza MUST contain `<error/>` child. Error types: cancel, continue, modify, auth, wait.

#### 9.3.2 Syntax
```
<stanza-kind type='error'>
  [RECOMMENDED original XML]
  <error type='error-type'>
    <defined-condition xmlns='urn:ietf:params:xml:ns:xmpp-stanzas'/>
    <text xmlns='urn:ietf:params:xml:ns:xmpp-stanzas' xml:lang='langcode'>OPTIONAL</text>
    [OPTIONAL application-specific condition]
  </error>
</stanza-kind>
```

#### 9.3.3 Defined Conditions
- `<bad-request/>` (modify)
- `<conflict/>` (cancel)
- `<feature-not-implemented/>` (cancel)
- `<forbidden/>` (auth)
- `<gone/>` (modify, may contain new address)
- `<internal-server-error/>` (wait)
- `<item-not-found/>` (cancel)
- `<jid-malformed/>` (modify)
- `<not-acceptable/>` (modify)
- `<not-allowed/>` (cancel)
- `<not-authorized/>` (auth)
- `<payment-required/>` (auth)
- `<recipient-unavailable/>` (wait, but must not reveal presence to unauthorized)
- `<redirect/>` (modify, should contain alternate JID)
- `<registration-required/>` (auth)
- `<remote-server-not-found/>` (cancel)
- `<remote-server-timeout/>` (wait)
- `<resource-constraint/>` (wait)
- `<service-unavailable/>` (cancel)
- `<subscription-required/>` (auth)
- `<undefined-condition/>` (any type, only with app-specific)
- `<unexpected-request/>` (wait)

#### 9.3.4 Application-Specific Conditions
May supplement defined conditions.

## 10. Server Rules for Handling XML Stanzas
Servers MUST ensure in-order processing of stanzas between any two entities.

### 10.1 No 'to' Address
If stanza has no `to`, server SHOULD process on behalf of sender (e.g., broadcast presence). Applies only to stanzas from registered entity (not other servers). For IQ get/set with no `to`, server MUST either process or return error.

### 10.2 Foreign Domain
If domain part of `to` not hosted by server, SHOULD route to foreign domain. If stream exists, use it; otherwise, resolve hostname, negotiate server-to-server stream (TLS+SASL), then route. If routing fails, sender's server MUST return error.

### 10.3 Subdomain
If `to` domain matches a configured subdomain, server MUST either process, route to specialized service, or return error if subdomain not configured.

### 10.4 Mere Domain or Specific Resource
If `to` domain equals server's hostname and JID is `<domain>` or `<domain/resource>`, server MUST process stanza as appropriate or return error.

### 10.5 Node in Same Domain
If `to` is `<node@domain>` or `<node@domain/resource>`, server SHOULD deliver to intended recipient. Rules:
1. If resource specified and matches connected resource, deliver to that stream.
2. If resource specified but not found, return `<service-unavailable/>` error.
3. If no resource (bare JID) and at least one connected resource, deliver to at least one (application-specific rules, e.g., [XMPP-IM]).

## 11. XML Usage within XMPP
### 11.1 Restrictions
XMPP MUST NOT inject: comments, processing instructions, DTD subsets, entity references (except predefined), unescaped characters that map to predefined entities. If received, MUST ignore.

### 11.2 XML Namespace Names and Prefixes
#### 11.2.1 Streams Namespace
REQUIRED in all XML stream headers. Name MUST be `http://etherx.jabber.org/streams`. SHOULD generate `stream:` prefix; MAY accept only `stream:`.

#### 11.2.2 Default Namespace
REQUIRED. SHALL be same for both streams. Common values: `jabber:client`, `jabber:server`. Server MUST support both; client MUST support `jabber:client`. MUST NOT generate prefixes for elements in these default namespaces. SHOULD NOT generate prefixes for content namespaces other than these.

#### 11.2.3 Dialback Namespace
REQUIRED for server dialback (Section 8). Name MUST be `jabber:server:dialback`. SHOULD generate `db:` prefix; MAY accept only `db:`.

### 11.3 Validation
Server not responsible for XML validation (except as noted for `to`/`from` in `jabber:server`). Clients SHOULD NOT rely on ability to send non-conformant data; SHOULD ignore non-conformant elements/attributes. Validation is OPTIONAL; schemas are descriptive only.

### 11.4 Inclusion of Text Declaration
Implementations SHOULD send text declaration before stream header. Applications MUST follow XML rules.

### 11.5 Character Encoding
MUST support UTF-8 (RFC 3629). MUST NOT attempt other encodings.

## 12. Core Compliance Requirements
### 12.1 Servers
MUST support:
- Nameprep, Nodeprep, Resourceprep application to addresses.
- XML streams, TLS, SASL, Resource Binding.
- Basic semantics of message, presence, IQ.
- Generation and handling of error syntax/semantics for streams, TLS, SASL, stanzas.
MAY support server dialback.

### 12.2 Clients
MUST support:
- XML streams, TLS, SASL, Resource Binding.
- Basic semantics of message, presence, IQ.
- Handling and (where appropriate) generation of error syntax/semantics for streams, TLS, SASL, stanzas.
SHOULD support generation of addresses conforming to Nameprep, Nodeprep, Resourceprep.

## 13. Internationalization Considerations
XML streams MUST be UTF-8. Stream SHOULD include `xml:lang`. Stanzas SHOULD include `xml:lang` if human-readable content. Server SHOULD apply default `xml:lang` to stanzas it routes; MUST NOT modify or delete `xml:lang` attributes.

## 14. Security Considerations
### 14.1 High Security
Mutual authentication and integrity-checking. Implementations MUST support high security. Service provisioning SHOULD use high security.

### 14.2 Certificate Validation
Peer MUST validate certificate. Three cases:
1. End entity certificate with trust anchor chain: Validate per X509 [X509] and check expected identity per [HTTP-TLS]; subjectAltName of type "xmpp" must be used as identity if present. User-oriented clients MUST notify user or terminate; automated clients SHOULD terminate and log. MAY provide config to disable but MUST provide enable.
2. Untrusted CA: SHOULD show certificate to user for approval, cache, verify future connections.
3. Self-signed: SHOULD act as in case 2.

### 14.3 Client-to-Server Communications
Client MUST support TLS and SASL. Communications MUST NOT proceed until DNS hostname resolved; SHOULD first try SRV `_xmpp-client._tcp` then fallback to A/AAAA on port 5222. Client IP MUST NOT be made public.

### 14.4 Server-to-Server Communications
Server MUST support TLS and SASL; SHOULD support dialback. Inter-domain communications OPTIONAL; if enabled, SHOULD high security. MUST NOT proceed until DNS hostnames resolved; MUST first try SRV `_xmpp-server._tcp` then fallback to port 5269. Dialback is weak; does not provide authentication or confidentiality. Dialback susceptible to DNS poisoning; domains needing robust security SHOULD use TLS and SASL. If SASL used, dialback SHOULD NOT be used.

### 14.5 Order of Layers
1. TCP
2. TLS
3. SASL
4. XMPP

### 14.6 Lack of SASL Channel Binding to TLS
SASL does not provide channel binding; if endpoints not identical, lower layer security cannot be trusted.

### 14.7 Mandatory-to-Implement Technologies
- Authentication: SASL DIGEST-MD5.
- Confidentiality: TLS using TLS_RSA_WITH_3DES_EDE_CBC_SHA.
- Both: TLS + SASL EXTERNAL with client-side certificates.

### 14.8 Firewalls
XMPP uses ports 5222 (client-to-server) and 5269 (server-to-server).

### 14.9 Use of base64 in SASL
Both parties MUST verify base64 data; MUST reject disallowed characters and malformed padding (only '=' as last character). Base64 not confidential.

### 14.10 Stringprep Profiles
Nameprep used for domain identifiers. Nodeprep and Resourceprep defined in Appendices A and B; similar-looking characters not mapped; security implications for user identification and access control.

## 15. IANA Considerations
### 15.1 XML Namespace Name for TLS Data
URI: `urn:ietf:params:xml:ns:xmpp-tls` | RFC 3920 | Contact: XMPP WG

### 15.2 XML Namespace Name for SASL Data
URI: `urn:ietf:params:xml:ns:xmpp-sasl` | RFC 3920 | Contact: XMPP WG

### 15.3 XML Namespace Name for Stream Errors
URI: `urn:ietf:params:xml:ns:xmpp-streams` | RFC 3920 | Contact: XMPP WG

### 15.4 XML Namespace Name for Resource Binding
URI: `urn:ietf:params:xml:ns:xmpp-bind` | RFC 3920 | Contact: XMPP WG

### 15.5 XML Namespace Name for Stanza Errors
URI: `urn:ietf:params:xml:ns:xmpp-stanzas` | RFC 3920 | Contact: XMPP WG

### 15.6 Nodeprep Profile of Stringprep
Registered: Nodeprep, RFC 3920, first version.

### 15.7 Resourceprep Profile of Stringprep
Registered: Resourceprep, RFC 3920, first version.

### 15.8 GSSAPI Service Name
Registered: "xmpp".

### 15.9 Port Numbers
Registered: "xmpp-client" (TCP 5222), "xmpp-server" (TCP 5269). Use OPTIONAL.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Node identifier MUST be formatted per Nodeprep; server MUST apply Nodeprep before comparison. | MUST | Section 3.3 |
| R2 | Resource identifier MUST be formatted per Resourceprep; server MUST apply Resourceprep before comparison. | MUST | Section 3.4 |
| R3 | Receiving entity MUST determine the initiating entity's JID after SASL and resource binding. | MUST | Section 3.5 |
| R4 | For server-to-server communications, initiating entity's JID SHOULD be authorization identity from SASL. | SHOULD | Section 3.5 |
| R5 | In client-to-server, the 'bare JID' SHOULD be authorization identity from SASL; full JID includes resource from binding. | SHOULD | Section 3.5 |
| R6 | Receiving entity MUST ensure JID conforms to syntax rules. | MUST | Section 3.5 |
| R7 | In server-to-server, each direction MUST use a separate TCP connection. | MUST | Section 4.2 |
| R8 | When negotiating XML streams, TLS SHOULD be used and SASL MUST be used. | MUST (SASL), SHOULD (TLS) | Section 4.3 |
| R9 | Initial and response streams MUST be secured separately. | MUST | Section 4.3 |
| R10 | Entity SHOULD NOT send stanzas before authentication; if it does, other MUST NOT accept and SHOULD return `<not-authorized/>` stream error. | SHOULD/MUST (non-accept) | Section 4.3 |
| R11 | Stream 'id' attribute MUST be unpredictable and nonrepeating. | MUST | Section 4.4 |
| R12 | On successful TLS, receiving entity MUST discard insecure knowledge. | MUST | Section 5.1 rule 9 |
| R13 | Initiating entity MUST validate TLS certificate. | MUST | Section 5.1 rule 7 |
| R14 | SASL authentication MUST be completed before sending stanzas. | MUST | Section 6.2 |
| R15 | For server-to-server, SASL negotiation MUST NOT proceed until DNS hostnames resolved. | MUST | Section 6.1 rule 1 |
| R16 | Initiating entity MUST include authorization identity if acting on behalf of another; otherwise MUST NOT. | MUST | Section 6.1 rule 7 |
| R17 | After successful SASL with security layer, both entities MUST discard insecure knowledge. | MUST | Section 6.1 rules 8-9 |
| R18 | Client MUST bind a resource after SASL if server requires. | MUST | Section 7 |
| R19 | Server MUST generate a unique resource identifier if client does not provide one. | MUST | Section 7 |
| R20 | Server MUST ensure in-order processing of stanzas. | MUST | Section 10 |
| R21 | Server MUST process or return error for IQ get/set with no 'to' if understood. | MUST | Section 10.1 |
| R22 | For server-to-server stanzas, 'to' and 'from' attributes MUST be present. | MUST | Section 9.1.1, 9.1.2 |
| R23 | For server-to-server, 'from' domain identifier MUST match validated domain of sending server. | MUST | Section 9.1.2 |
| R24 | XMPP implementations MUST NOT inject comments, PIs, DTDs, entity references, unescaped characters. | MUST | Section 11.1 |
| R25 | All implementations MUST support SASL DIGEST-MD5 and TLS with specified cipher. | MUST | Section 14.7 |
| R26 | Implementations MUST support UTF-8 encoding; MUST NOT use other encodings. | MUST | Section 11.5 |

## Informative Annexes (Condensed)
- **A. Nodeprep**: Defines a stringprep profile for XMPP node identifiers. Uses Unicode 3.2, mappings from Tables B.1 and B.2, normalization KC, prohibition of specific Unicode categories and eight extra characters (`" & ' / : < > @`), and bidirectional checking.
- **B. Resourceprep**: Defines a stringprep profile for XMPP resource identifiers. Uses Unicode 3.2, mapping from Table B.1, normalization KC, prohibition of specific Unicode categories (but not the extra characters), and bidirectional checking.
- **C. XML Schemas**: Non-normative schemas for streams, stream error, TLS, SASL, resource binding, dialback, and stanza error namespaces. Included for descriptive purposes only.
- **D. Differences between Core Jabber Protocols and XMPP**: Non-normative summary of key changes: SSL replaced by TLS; SASL replaces IQ-based authentication; dedicated resource binding namespace; formal JID processing with stringprep; standardized error handling; introduction of `xml:lang` and version attribute.