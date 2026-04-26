# RFC 7230: Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing
**Source**: IETF | **Version**: 1.1 | **Date**: June 2014 | **Type**: Standards Track
**Original**: https://www.rfc-editor.org/rfc/rfc7230

## Scope (Summary)
Defines HTTP/1.1 message syntax, parsing, and routing; defines the "http" and "https" URI schemes; describes connection management, transfer codings, and security considerations for message handling.

## Normative References
- [RFC0793] – Transmission Control Protocol, STD 7
- [RFC1950] – ZLIB Compressed Data Format Specification
- [RFC1951] – DEFLATE Compressed Data Format Specification
- [RFC1952] – GZIP file format specification
- [RFC2119] – Key words for use in RFCs to Indicate Requirement Levels
- [RFC3986] – Uniform Resource Identifier (URI): Generic Syntax
- [RFC5234] – Augmented BNF for Syntax Specifications: ABNF
- [RFC7231] – HTTP/1.1: Semantics and Content
- [RFC7232] – HTTP/1.1: Conditional Requests
- [RFC7233] – HTTP/1.1: Range Requests
- [RFC7234] – HTTP/1.1: Caching
- [RFC7235] – HTTP/1.1: Authentication
- [USASCII] – ANSI X3.4, 1986
- [Welch] – A Technique for High-Performance Data Compression

## Definitions and Abbreviations
- **HTTP**: Hypertext Transfer Protocol
- **URI**: Uniform Resource Identifier
- **ABNF**: Augmented Backus-Naur Form
- **OWS**: optional whitespace
- **RWS**: required whitespace
- **BWS**: "bad" whitespace
- **CRLF**: carriage return line feed
- **client**: program that establishes a connection to send HTTP requests
- **server**: program that accepts connections to service HTTP requests
- **user agent**: client program that initiates a request (browsers, spiders, etc.)
- **origin server**: program that can originate authoritative responses for a target resource
- **proxy**: message-forwarding agent selected by client
- **gateway**: intermediary that acts as origin server for outbound connection
- **tunnel**: blind relay between two connections
- **cache**: local store of previous response messages
- **effective request URI**: reconstructed target URI by server

## Section/Article Title

### 1. Introduction
- Part of a series: [RFC7230] (this document), [RFC7231], [RFC7232], [RFC7233], [RFC7234], [RFC7235]
- Obsoletes RFC 2616 and RFC 2145; updates RFC 2817 and RFC 2818

#### 1.1. Requirements Notation
- Key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" interpreted as per [RFC2119]

#### 1.2. Syntax Notation
- Uses ABNF of [RFC5234] with list extension (#rule) defined in Section 7
- Core rules from [RFC5234] Appendix B.1: ALPHA, CR, CRLF, CTL, DIGIT, DQUOTE, HEXDIG, HTAB, LF, OCTET, SP, VCHAR
- ABNF rule names prefixed with "obs-" denote obsolete grammar

### 2. Architecture

#### 2.1. Client/Server Messaging
- HTTP is a stateless request/response protocol exchanging messages across a connection
- **request-line**: method, request-target, protocol version
- **status-line**: protocol version, status code, reason phrase
- Example GET request and response provided

#### 2.2. Implementation Diversity
- User agents include diverse devices; not all can provide interactive feedback
- Requirements for error reporting may be satisfied by logs

#### 2.3. Intermediaries
- Three forms: proxy, gateway, tunnel
- Terms: upstream/downstream (message flow), inbound/outbound (request route)
- **proxy**: selected by client; may transform messages
- **gateway** (reverse proxy): acts as origin server for outbound connection
- **tunnel**: blind relay; ceases when both ends closed
- **interception proxy**: not selected by client; filters/redirects traffic
- **Server MUST NOT assume two requests on same connection are from same user agent** unless connection is secured and specific to that agent

#### 2.4. Caches
- Cache stores cacheable responses; any client or server MAY employ a cache (except tunnel)
- Cacheable response: allowed to be stored for answering subsequent requests
- Cache behavior defined in [RFC7234]

#### 2.5. Conformance and Error Handling
- Implementation conformant if complies with all requirements for roles it partakes
- **Sender MUST NOT generate protocol elements that convey false meaning or do not match grammar**
- **Recipient MUST be able to parse any reasonable length value for its role**
- **Recipient MUST interpret received element according to defined semantics**, unless sender known to be incorrect
- **Recipient MAY attempt to recover from invalid constructs**, but no specific error handling required unless security impact

#### 2.6. Protocol Versioning
- HTTP-version = HTTP-name "/" DIGIT "." DIGIT (case-sensitive)
- Major version indicates messaging syntax; minor indicates highest conformant minor version
- Intermediaries (except tunnels) **MUST send their own HTTP-version** in forwarded messages
- **Client SHOULD send request version equal to highest conformant version ≤ server's highest known version**
- **Client MUST NOT send version not conformant to**
- **Server SHOULD send response version ≤ its highest conformant with major ≤ request major; MUST NOT send non-conformant version**
- **Server MAY send HTTP/1.0 response if client known to misbehave; such downgrades SHOULD NOT be performed unless triggered by specific client attributes**
- **Recipient SHOULD process message with higher minor version as if highest supported minor version within that major**

#### 2.7. Uniform Resource Identifiers
- URIs used for identifying resources
- Adopts definitions from [RFC3986]: URI-reference, absolute-URI, relative-part, scheme, authority, port, host, path-abempty, segment, query, fragment
- Defines absolute-path and partial-URI for HTTP

##### 2.7.1. http URI Scheme
- http-URI = "http://" authority path-abempty [ "?" query ] [ "#" fragment ]
- **Sender MUST NOT generate "http" URI with empty host identifier; recipient MUST reject as invalid**
- Default port 80 if not given
- **Sender MUST NOT generate userinfo subcomponent in "http" URI reference within a message as request-target or header field value**
- **Recipient SHOULD parse for userinfo and treat its presence as error** (phishing risk)

##### 2.7.2. https URI Scheme
- https-URI = "https://" authority path-abempty [ "?" query ] [ "#" fragment ]
- Default port 443
- **User agent MUST ensure connection to origin server is secured with strong encryption prior to sending first HTTP request**
- Distinct namespace from http even if same authority

##### 2.7.3. http and https URI Normalization and Comparison
- Normalize according to [RFC3986] Section 6; omit default port; empty path equivalent to "/"; scheme and host case-insensitive; non-reserved characters not encoded

### 3. Message Format
- HTTP-message = start-line *( header-field CRLF ) CRLF [ message-body ]
- **Recipient MUST parse as sequence of octets in a superset of US-ASCII**; string-based parsers unsafe for raw message
- **Sender MUST NOT send whitespace between start-line and first header field; recipient MUST either reject or consume such lines without processing**
- Presence of whitespace may be security attack

#### 3.1. Start Line
- start-line = request-line / status-line

##### 3.1.1. Request Line
- request-line = method SP request-target SP HTTP-version CRLF
- method = token (case-sensitive)
- **Recipients of invalid request-line SHOULD respond with 400 (Bad Request) or 301 (Moved Permanently) with properly encoded target; SHOULD NOT autocorrect without redirect** (security)
- **Server receiving too long method SHOULD respond 501; too long request-target MUST respond 414**
- **RECOMMENDED support for request-line lengths of 8000 octets minimum**

##### 3.1.2. Status Line
- status-line = HTTP-version SP status-code SP reason-phrase CRLF
- status-code = 3DIGIT (classes defined in [RFC7231])
- reason-phrase = *( HTAB / SP / VCHAR / obs-text )
- **Client SHOULD ignore reason-phrase content**

#### 3.2. Header Fields
- header-field = field-name ":" OWS field-value OWS
- field-name = token (case-insensitive)
- field-value = *( field-content / obs-fold )
- obs-fold = CRLF 1*( SP / HTAB ) – deprecated (see Section 3.2.4)

##### 3.2.1. Field Extensibility
- No limit on new field names or number of header fields
- **Proxy MUST forward unrecognized header fields unless field-name in Connection header field or configured to block; other recipients SHOULD ignore unrecognized fields**

##### 3.2.2. Field Order
- Order of fields with different names not significant; good practice to put control data first
- **Server MUST NOT apply request to target resource until entire request header section received**
- **Sender MUST NOT generate multiple header fields with same field name unless field value defined as comma-separated list or known exception (e.g., Set-Cookie)**
- **Recipient MAY combine multiple header fields with same name into one by appending values separated by comma; proxy MUST NOT change order of such field values**

##### 3.2.3. Whitespace
- OWS = *( SP / HTAB ) – optional; sender SHOULD use single SP when optional whitespace preferred, otherwise SHOULD NOT generate except for filtering
- RWS = 1*( SP / HTAB ) – required; sender SHOULD generate as single SP
- BWS = OWS – "bad" whitespace; **sender MUST NOT generate BWS; recipient MUST parse and remove it before interpreting**

##### 3.2.4. Field Parsing
- No whitespace allowed between field-name and colon
- **Server MUST reject request message containing whitespace between header field-name and colon with 400 (Bad Request)**
- **Proxy MUST remove any such whitespace from response before forwarding**
- Field value does not include leading/trailing OWS; parsers should exclude them
- obs-fold deprecated except within message/http media type
- **Sender MUST NOT generate message with obs-fold unless intended for message/http packaging**
- **Server receiving obs-fold in request (not in message/http) MUST either reject with 400 or replace obs-fold with SP octets**
- **Proxy/gateway receiving obs-fold in response (not in message/http) MUST either discard and replace with 502 or replace with SP**
- **User agent receiving obs-fold in response MUST replace with SP**
- **Newly defined header fields SHOULD limit to US-ASCII; recipient SHOULD treat other octets (obs-text) as opaque**

##### 3.2.5. Field Limits
- No predefined limit on header field length (see Section 2.5)
- **Server receiving request header fields larger than it wishes to process MUST respond with appropriate 4xx status code**
- **Client MAY discard or truncate received header fields if semantics allow safe ignoring**

##### 3.2.6. Field Value Components
- token = 1*tchar (tchar defined as VCHAR except delimiters)
- quoted-string = DQUOTE *( qdtext / quoted-pair ) DQUOTE
- comment = "(" *( ctext / quoted-pair / comment ) ")"
- quoted-pair = "\" ( HTAB / SP / VCHAR / obs-text )
- **Recipient that processes quoted-string MUST handle quoted-pair as replacement octet**
- **Sender SHOULD NOT generate quoted-pair in quoted-string except to quote DQUOTE and backslash; similarly for comment**

#### 3.3. Message Body
- message-body = *OCTET
- Presence of message body determined by Content-Length or Transfer-Encoding header fields
- Responses to HEAD, 1xx, 204, 304 never include body; CONNECT 2xx responses switch to tunnel

##### 3.3.1. Transfer-Encoding
- Transfer-Encoding = 1#transfer-coding
- **Recipient MUST be able to parse chunked transfer coding**
- **Sender MUST NOT apply chunked more than once to a message body**
- If any transfer coding other than chunked applied to request payload, **sender MUST apply chunked as final encoding**
- If any non-chunked coding applied to response payload, **sender MUST either apply chunked as final encoding or close connection**
- **Server MUST NOT send Transfer-Encoding in 1xx or 204 responses; also not in 2xx to CONNECT**
- **Client MUST NOT send Transfer-Encoding unless knows server handles HTTP/1.1 (or later)**
- **Server MUST NOT send Transfer-Encoding unless request indicates HTTP/1.1 (or later)**
- **Server receiving unknown transfer coding SHOULD respond 501**

##### 3.3.2. Content-Length
- Content-Length = 1*DIGIT
- **Sender MUST NOT send Content-Length if Transfer-Encoding present**
- **User agent SHOULD send Content-Length in request when no Transfer-Encoding and method defines meaning for payload body; SHOULD NOT send when no payload body and method does not anticipate**
- **Server MAY send Content-Length in response to HEAD; MUST NOT unless value equals what would have been for GET**
- **Server MAY send Content-Length in 304; MUST NOT unless value equals what would have been for 200**
- **Server MUST NOT send Content-Length in 1xx, 204, or 2xx to CONNECT**
- **Origin server SHOULD send Content-Length when payload size known prior to sending complete header section** (except as above)
- **Recipient MUST anticipate large numerals and prevent integer overflow errors**
- **If multiple Content-Length fields with same value or single field with list of same values, recipient MUST either reject or replace with single valid Content-Length prior to determining body length or forwarding**
- **If multiple Content-Length fields with differing values or invalid value, recipient MUST treat as unrecoverable error; see Section 3.3.3**

##### 3.3.3. Message Body Length
- Determined by order of precedence:
  1. HEAD response or 1xx/204/304: terminated by empty line after header fields
  2. 2xx to CONNECT: tunnel after header fields; client MUST ignore Content-Length/Transfer-Encoding
  3. Transfer-Encoding with chunked as final: decode chunked data; if not final encoding, length determined by connection close (response) or server MUST respond 400 (request). If both Transfer-Encoding and Content-Length present, Transfer-Encoding overrides; **sender MUST remove Content-Length before forwarding**. Such message may indicate smuggling/splitting.
  4. Without Transfer-Encoding: multiple Content-Length with differing values or invalid value => unrecoverable error. For request: server MUST respond 400 and close. For response via proxy: proxy MUST close, discard, and send 502. For user agent: user agent MUST close and discard.
  5. Valid Content-Length: its value defines length; if fewer octets received, recipient MUST consider message incomplete and close.
  6. Request without above: no body.
  7. Otherwise: response without declared length: length determined by server closing connection.
- **Server SHOULD generate encoding or length-delimited messages whenever possible**
- **Server MAY reject request with body but no Content-Length with 411 (Length Required)**
- **Client sending request with body SHOULD use Content-Length if length known in advance, rather than chunked** (some services reject chunked)
- **User agent sending request with body MUST send valid Content-Length if does not know server handles HTTP/1.1 (or later)**
- If extra data after final response, **client MUST NOT process, cache, or forward as separate response** (cache poisoning risk)

#### 3.4. Handling Incomplete Messages
- **Server receiving incomplete request MAY send error response prior to closing**
- **Client receiving incomplete response MUST record message as incomplete** (cache requirements in [RFC7234])
- If response terminates before empty line, client cannot assume full meaning; may need to retry
- Chunked message incomplete if zero-sized chunk not received; Content-Length incomplete if fewer octets received; connection-close response complete if header section intact

#### 3.5. Message Parsing Robustness
- **HTTP/1.1 user agent MUST NOT preface or follow request with extra CRLF**; if terminating body with CRLF, count as part of message body length
- **Server expecting request-line SHOULD ignore at least one empty line (CRLF) received prior**
- **Recipient MAY recognize single LF as line terminator** and ignore preceding CR
- **Recipients MAY parse on whitespace-delimited word boundaries** and treat any whitespace as SP, but lenient parsing can lead to security vulnerabilities (see Section 9.5)
- **Server receiving sequence not matching HTTP-message grammar (aside from robustness exceptions) SHOULD respond with 400**

### 4. Transfer Codings
- transfer-coding = "chunked" / "compress" / "deflate" / "gzip" / transfer-extension
- transfer-extension = token *( OWS ";" OWS transfer-parameter )
- All transfer-coding names case-insensitive; should be registered in HTTP Transfer Coding registry (Section 8.4)

#### 4.1. Chunked Transfer Coding
- chunked-body = *chunk last-chunk trailer-part CRLF
- chunk = chunk-size [ chunk-ext ] CRLF chunk-data CRLF
- chunk-size = 1*HEXDIG; last-chunk = 1*"0" [ chunk-ext ] CRLF
- **Recipient MUST be able to parse and decode chunked transfer coding**

##### 4.1.1. Chunk Extensions
- chunk-ext = *( ";" chunk-ext-name [ "=" chunk-ext-val ] )
- **Recipient MUST ignore unrecognized chunk extensions**
- Server ought to limit total length of chunk extensions received and generate appropriate 4xx if exceeded

##### 4.1.2. Chunked Trailer Part
- trailer-part = *( header-field CRLF )
- **Sender MUST NOT generate trailer containing fields necessary for message framing, routing, request modifiers, authentication, response control data, or payload processing** (e.g., Transfer-Encoding, Content-Length, Host, etc.)
- **Recipient MAY process allowed trailer fields as if appended to header section; MUST ignore forbidden trailer fields**
- Unless request includes TE indicating "trailers" acceptable, **server SHOULD NOT generate trailer fields necessary for user agent**

##### 4.1.3. Decoding Chunked
- Pseudo-code provided for decoding: concatenate chunk-data, discover Content-Length, remove "chunked" from Transfer-Encoding, remove Trailer header

#### 4.2. Compression Codings

##### 4.2.1. Compress Coding
- Adaptive LZW coding; **recipient SHOULD consider "x-compress" equivalent to "compress"**

##### 4.2.2. Deflate Coding
- "zlib" data format [RFC1950] containing "deflate" compressed data [RFC1951]; note: some implementations send deflate without zlib wrapper

##### 4.2.3. Gzip Coding
- LZ77 with CRC-32; **recipient SHOULD consider "x-gzip" equivalent to "gzip"**

#### 4.3. TE
- TE = #t-codings; t-codings = "trailers" / ( transfer-coding [ t-ranking ] )
- **Client MUST NOT send chunked in TE** (always acceptable)
- Presence of "trailers" indicates client willing to accept trailer fields
- **If TE field-value empty or absent, only acceptable transfer coding is chunked**
- **Sender of TE MUST also send "TE" connection option in Connection header field** to prevent forwarding by intermediaries that don't support it

#### 4.4. Trailer
- Trailer = 1#field-name
- **Sender SHOULD generate Trailer header field before message body to indicate which fields will be present in trailers** (allows recipient to prepare)

### 5. Message Routing

#### 5.1. Identifying a Target Resource
- Target resource identified by URI reference; target URI excludes fragment

#### 5.2. Connecting Inbound
- Client checks cache first, then proxy configuration, then direct connection to authority based on URI scheme

#### 5.3. Request Target
- request-target = origin-form / absolute-form / authority-form / asterisk-form

##### 5.3.1. origin-form
- origin-form = absolute-path [ "?" query ]
- **When making request directly to origin server (except CONNECT or server-wide OPTIONS), client MUST send only absolute path and query components as request-target.** If path empty, **client MUST send "/"**. Host header field also sent (Section 5.4)

##### 5.3.2. absolute-form
- absolute-form = absolute-URI
- **When making request to proxy (except CONNECT or server-wide OPTIONS), client MUST send target URI in absolute-form**
- **Server MUST accept absolute-form in requests** (for future transition)

##### 5.3.3. authority-form
- authority-form = authority
- **Only used for CONNECT requests; client MUST send only target URI's authority component (excluding userinfo and "@")**

##### 5.3.4. asterisk-form
- asterisk-form = "*"
- **Only used for server-wide OPTIONS request; client MUST send "*"**
- If proxy receives OPTIONS with absolute-form and empty path/no query, **last proxy on request chain MUST send "*" when forwarding to origin server**

#### 5.4. Host
- Host = uri-host [ ":" port ]
- **Client MUST send Host header field in all HTTP/1.1 request messages. If target URI includes authority, client MUST send Host identical to that authority component (excluding userinfo). If authority missing/undefined, client MUST send Host with empty field-value**
- **User agent SHOULD generate Host as first header field following request-line**
- **Client MUST send Host even if request-target in absolute-form** (for forwarding through HTTP/1.0 proxies)
- **Proxy receiving request with absolute-form MUST ignore received Host and replace it with host information of request-target; proxy MUST generate new Host based on request-target**
- **Server MUST respond with 400 to HTTP/1.1 request lacking Host, or containing more than one Host, or invalid field-value**

#### 5.5. Effective Request URI
- Server reconstructs effective request URI from request-target, Host, connection context
- Algorithm provided: scheme determined by TLS or configuration; authority from configuration, authority-form, or Host; path/query from request-target
- Example: insecure TCP with GET /path Host: example.org:8080 → http://example.org:8080/path
- **Origin server decides whether to provide service for that URI; inconsistency may indicate misdirection or attack**

#### 5.6. Associating a Response to a Request
- No request identifier; relies on order of response arrival
- **Client with multiple outstanding requests on a connection MUST maintain list of outstanding requests in sent order and associate each response to highest ordered request not yet received final response**

#### 5.7. Message Forwarding

##### 5.7.1. Via
- Via = 1#( received-protocol RWS received-by [ RWS comment ] )
- **Proxy MUST send appropriate Via header field in each forwarded message**
- **HTTP-to-HTTP gateway MUST send Via in each inbound request; MAY send in forwarded responses**
- Intermediary SHOULD NOT forward names/ports of hosts inside firewall unless explicitly enabled; SHOULD replace with pseudonym
- Intermediary MAY combine ordered subsequence of Via entries if identical received-protocol values and under same organizational control; **MUST NOT combine entries with different protocol values**

##### 5.7.2. Transformations
- **Proxy MAY add its own domain to host name if request-target contains non-fully qualified domain name; MUST NOT change host name if fully qualified**
- **Proxy MUST NOT modify absolute-path and query parts of received request-target when forwarding** except to replace empty path with "/" or "*"
- **Proxy MAY modify message body through application/removal of transfer coding**
- **Proxy MUST NOT transform payload of message containing no-transform cache-control directive**
- **Proxy MAY transform payload of message without no-transform; MUST add Warning header with warn-code 214 if transformation applied; MAY change status code to 203**
- **Proxy SHOULD NOT modify header fields providing endpoint, resource state, or representation information** unless specifically allowed or needed for privacy/security

### 6. Connection Management

#### 6.1. Connection
- Connection = 1#connection-option; connection-option = token (case-insensitive)
- **Proxy or gateway MUST remove or replace any received connection options before forwarding**
- **When a header field aside from Connection is used for control information about the current connection, sender MUST list corresponding field-name within Connection header field**
- **Proxy/gateway MUST parse Connection before forwarding, remove any header fields with same names as connection-options, and remove Connection header itself**
- **Sender MUST NOT send connection option corresponding to header field intended for all recipients** (e.g., Cache-Control)
- "close" connection option signals connection will close after current response
- **Client that does not support persistent connections MUST send "close" in every request**
- **Server that does not support persistent connections MUST send "close" in every response (except 1xx)**
- New connection options should not share name with existing header fields

#### 6.2. Establishment
- Beyond scope; each connection applies to one transport link

#### 6.3. Persistence
- HTTP/1.1 defaults to persistent connections; "close" signals non-persistence
- **HTTP implementations SHOULD support persistent connections**
- Recipient determines persistence from protocol version and Connection header:
  - "close" present => not persistent
  - HTTP/1.1 (or later) => persistent
  - HTTP/1.0 with "keep-alive" and recipient not proxy and wishes to honor => persistent
  - Otherwise => close after current response
- **Client MAY send additional requests on persistent connection until "close" sent/received or HTTP/1.0 response without "keep-alive"**
- **Server MUST read entire request body or close after response; client MUST read entire response body if intending to reuse connection**
- **Proxy MUST NOT maintain persistent connection with HTTP/1.0 client**

##### 6.3.1. Retrying Requests
- **Client MAY open new connection and automatically retransmit aborted sequence if all requests have idempotent methods**
- **Proxy MUST NOT automatically retry non-idempotent requests**
- **User agent MUST NOT automatically retry non-idempotent request unless knows request semantics are idempotent or can detect original request was never applied**
- **Client SHOULD NOT automatically retry a failed automatic retry**

##### 6.3.2. Pipelining
- **Client that supports persistent connections MAY pipeline requests**
- **Server MAY process pipelined requests in parallel if all safe methods, but MUST send responses in same order as requests received**
- **Client that pipelines SHOULD retry unanswered requests if connection closes; MUST NOT pipeline immediately after connection establishment** (TCP reset problem)
- **User agent SHOULD NOT pipeline after non-idempotent method until final response received**
- **Intermediary receiving pipelined requests MAY pipeline them when forwarding; may retry idempotent sequence if inbound fails; otherwise SHOULD forward received responses and close outbound connections**

#### 6.4. Concurrency
- Client ought to limit number of simultaneous open connections to a given server; no specific maximum mandated
- Using multiple connections can avoid head-of-line blocking but consumes resources and may cause congestion

#### 6.5. Failures and Timeouts
- **Client or server that wishes to time out SHOULD issue graceful close**
- **Implementations SHOULD constantly monitor open connections for closure signal and respond appropriately**
- **Client, server, or proxy MAY close transport connection at any time**
- **Server SHOULD sustain persistent connections when possible and let flow-control resolve temporary overloads**
- **Client sending message body SHOULD monitor for error response; if sees response indicating server closing, SHOULD immediately cease transmitting body and close**

#### 6.6. Tear-down
- **Sender SHOULD send "close" when it wishes to close after current request/response**
- **Client sending "close" MUST NOT send further requests on that connection; MUST close after reading final response**
- **Server receiving "close" MUST initiate close after sending final response; SHOULD send "close" in final response; MUST NOT process further requests**
- **Server sending "close" MUST initiate close after sending response; MUST NOT process further requests**
- **Client receiving "close" MUST cease sending requests and close after reading response; SHOULD NOT assume pipelined requests processed**
- Servers should use half-close to avoid TCP reset problem

#### 6.7. Upgrade
- Upgrade = 1#protocol; protocol = protocol-name ["/" protocol-version]
- **Client MAY send Upgrade to invite server to switch protocols; server MAY ignore**
- **Server sending 101 MUST send Upgrade indicating new protocol(s); MUST list in layer-ascending order; MUST NOT switch to protocol not indicated by client**
- **Server sending 426 MUST send Upgrade to indicate acceptable protocols**
- **Server MAY send Upgrade in any other response to advertise future upgrade capability**
- **Server MUST NOT switch protocols unless received message semantics can be honored by new protocol**
- **When Upgrade sent, sender MUST also send Connection header field with "upgrade" connection option**
- **Server MUST ignore Upgrade received in HTTP/1.0 request**
- **If server receives both Upgrade and Expect: 100-continue, server MUST send 100 before 101**
- Upgrade only applies to switching application protocols on top of existing connection; not for underlying transport

### 7. ABNF List Extension: #rule
- #rule: comma-delimited list of elements with optional whitespace
- **Sender MUST NOT generate empty list elements**
- **Recipient MUST parse and ignore a reasonable number of empty list elements** (for compatibility)
- Full grammar for #element and 1#element provided with expansion to standard ABNF (see Appendix B)

### 8. IANA Considerations
- **Header fields registered**: Connection, Content-Length, Host, TE, Trailer, Transfer-Encoding, Upgrade, Via
- **Close field name registered as "reserved"**
- **URI schemes registered**: http (Section 2.7.1), https (Section 2.7.2)
- **Media types registered**: message/http, application/http
- **Transfer Coding registry updated**: chunked, compress, deflate, gzip, x-compress (deprecated), x-gzip (deprecated)
- **Content Coding registry updated**: compress, deflate, gzip, x-compress, x-gzip
- **Upgrade Token registry**: HTTP token registered; procedure defined (First Come First Served, IESG reassignment possible)

### 9. Security Considerations

#### 9.1. Establishing Authority
- HTTP relies on authoritative response; phishing attacks on user perception; user agents should allow easy inspection of target URI, reject userinfo, avoid sending stored credentials from untrusted sources
- DNS and routing attacks can undermine "http" authority; "https" scheme intended to prevent/reveal attacks via TLS and proper verification

#### 9.2. Risks of Intermediaries
- Intermediaries are men-in-the-middle; compromise can lead to serious security/privacy problems; shared caches vulnerable to cache poisoning

#### 9.3. Attacks via Protocol Element Length
- Large streams can cause vulnerabilities; minimum recommended limits: request-line 8000 octets (Section 3.1.1), header fields (Section 3.2)
- **Recipients ought to carefully limit processing of other protocol elements** to avoid overflow vulnerabilities

#### 9.4. Response Splitting
- Exploits line-based nature and ordered association; CRLF injection; defense: filter requests for encoded CR/LF; more effective: restrict output of header fields to APIs that filter bad octets

#### 9.5. Request Smuggling
- Exploits differences in protocol parsing; Section 3.3.3 introduces requirements to reduce effectiveness

#### 9.6. Message Integrity
- HTTP relies on lower layers; additional integrity mechanisms can be added via extensible header fields; user agents encouraged to implement configurable means for detecting/reporting failures

#### 9.7. Message Confidentiality
- HTTP relies on underlying transport; "https" scheme for confidential connections

#### 9.8. Privacy of Server Log Information
- Log information can identify user patterns; should be securely stored; purged of personally identifiable information when no longer needed

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Server MUST NOT assume two requests on same connection are from same user agent unless connection secured and agent-specific | MUST | Section 2.3 |
| R2 | Sender MUST NOT generate protocol elements that convey false meaning | MUST | Section 2.5 |
| R3 | Sender MUST NOT generate protocol elements not matching ABNF grammar | MUST | Section 2.5 |
| R4 | Recipient MUST be able to parse any reasonable length value for its role | MUST | Section 2.5 |
| R5 | Recipient MUST interpret received element according to defined semantics | MUST | Section 2.5 |
| R6 | Intermediaries (except tunnels) MUST send their own HTTP-version in forwarded messages | MUST | Section 2.6 |
| R7 | Client MUST NOT send version not conformant to | MUST | Section 2.6 |
| R8 | Server MUST NOT send version not conformant to | MUST | Section 2.6 |
| R9 | Sender MUST NOT generate "http" URI with empty host identifier; recipient MUST reject | MUST | Section 2.7.1 |
| R10 | Sender MUST NOT generate userinfo subcomponent in "http" URI reference within message | MUST | Section 2.7.1 |
| R11 | Recipient SHOULD parse for userinfo and treat as error | SHOULD | Section 2.7.1 |
| R12 | User agent MUST ensure connection to origin server is secured with strong encryption prior to sending first HTTPS request | MUST | Section 2.7.2 |
| R13 | Recipient MUST parse HTTP message as sequence of octets in superset of US-ASCII | MUST | Section 3 |
| R14 | Sender MUST NOT send whitespace between start-line and first header field | MUST | Section 3 |
| R15 | Recipient of whitespace between start-line and first header field MUST either reject or ignore each whitespace-preceded line | MUST | Section 3 |
| R16 | Recipients of invalid request-line SHOULD respond with 400 or 301; SHOULD NOT autocorrect without redirect | SHOULD | Section 3.1.1 |
| R17 | Server receiving too long request-target MUST respond with 414 | MUST | Section 3.1.1 |
| R18 | RECOMMENDED support for request-line lengths of 8000 octets | RECOMMENDED | Section 3.1.1 |
| R19 | Client SHOULD ignore reason-phrase | SHOULD | Section 3.1.2 |
| R20 | Proxy MUST forward unrecognized header fields unless field-name in Connection or configured to block | MUST | Section 3.2.1 |
| R21 | Other recipients SHOULD ignore unrecognized header fields | SHOULD | Section 3.2.1 |
| R22 | Server MUST NOT apply request to target resource until entire request header section received | MUST | Section 3.2.2 |
| R23 | Sender MUST NOT generate multiple header fields with same field name unless comma-separated list or known exception | MUST | Section 3.2.2 |
| R24 | Proxy MUST NOT change order of field values when combining multiple header fields with same name | MUST | Section 3.2.2 |
| R25 | Sender SHOULD generate optional whitespace as single SP when preferred; otherwise SHOULD NOT generate | SHOULD | Section 3.2.3 |
| R26 | Sender MUST NOT generate BWS messages | MUST | Section 3.2.3 |
| R27 | Recipient MUST parse for BWS and remove before interpreting | MUST | Section 3.2.3 |
| R28 | Server MUST reject request with whitespace between field-name and colon with 400 | MUST | Section 3.2.4 |
| R29 | Proxy MUST remove such whitespace from response before forwarding | MUST | Section 3.2.4 |
| R30 | Sender MUST NOT generate message with obs-fold unless intended for message/http media type | MUST | Section 3.2.4 |
| R31 | Server receiving obs-fold in request not in message/http MUST either reject with 400 or replace with SP | MUST | Section 3.2.4 |
| R32 | Proxy/gateway receiving obs-fold in response not in message/http MUST either discard and send 502 or replace with SP | MUST | Section 3.2.4 |
| R33 | User agent receiving obs-fold in response MUST replace with SP | MUST | Section 3.2.4 |
| R34 | Newly defined header fields SHOULD limit to US-ASCII | SHOULD | Section 3.2.4 |
| R35 | Recipient SHOULD treat obs-text as opaque | SHOULD | Section 3.2.4 |
| R36 | Server receiving request header fields larger than it wishes to process MUST respond with appropriate 4xx | MUST | Section 3.2.5 |
| R37 | Client MAY discard or truncate received header fields if safe ignoring | MAY | Section 3.2.5 |
| R38 | Recipient processing quoted-string MUST handle quoted-pair as replacement octet | MUST | Section 3.2.6 |
| R39 | Sender SHOULD NOT generate unnecessary quoted-pairs | SHOULD | Section 3.2.6 |
| R40 | Recipient MUST be able to parse chunked transfer coding | MUST | Section 3.3.1 |
| R41 | Sender MUST NOT apply chunked more than once to message body | MUST | Section 3.3.1 |
| R42 | If any non-chunked transfer coding applied to request payload, sender MUST apply chunked as final encoding | MUST | Section 3.3.1 |
| R43 | If any non-chunked transfer coding applied to response payload, sender MUST either apply chunked as final encoding or close connection | MUST | Section 3.3.1 |
| R44 | Server MUST NOT send Transfer-Encoding in 1xx, 204, or 2xx to CONNECT responses | MUST | Section 3.3.1 |
| R45 | Client MUST NOT send Transfer-Encoding unless knows server handles HTTP/1.1 or later | MUST | Section 3.3.1 |
| R46 | Server MUST NOT send Transfer-Encoding unless request indicates HTTP/1.1 or later | MUST | Section 3.3.1 |
| R47 | Server receiving unknown transfer coding SHOULD respond 501 | SHOULD | Section 3.3.1 |
| R48 | Sender MUST NOT send Content-Length if Transfer-Encoding present | MUST | Section 3.3.2 |
| R49 | User agent SHOULD send Content-Length in request when no Transfer-Encoding and method defines meaning for payload body | SHOULD | Section 3.3.2 |
| R50 | User agent SHOULD NOT send Content-Length when no payload body and method not anticipate | SHOULD | Section 3.3.2 |
| R51 | Server MAY send Content-Length in response to HEAD; MUST NOT unless value equals what would be for GET | MUST | Section 3.3.2 |
| R52 | Server MAY send Content-Length in 304; MUST NOT unless value equals what would be for 200 | MUST | Section 3.3.2 |
| R53 | Server MUST NOT send Content-Length in 1xx, 204, or 2xx to CONNECT | MUST | Section 3.3.2 |
| R54 | Origin server SHOULD send Content-Length when payload size known prior to sending complete header section | SHOULD | Section 3.3.2 |
| R55 | Recipient MUST anticipate large Content-Length values and prevent integer overflow | MUST | Section 3.3.2 |
| R56 | If multiple Content-Length with same value or single list of same values, recipient MUST either reject or replace with single valid Content-Length | MUST | Section 3.3.2 |
| R57 | If multiple Content-Length with differing values or invalid single value, recipient MUST treat as unrecoverable error | MUST | Section 3.3.3 |
| R58 | For 2xx to CONNECT, client MUST ignore Content-Length/Transfer-Encoding | MUST | Section 3.3.3 |
| R59 | If Transfer-Encoding present with chunked not final encoding in request, server MUST respond 400 | MUST | Section 3.3.3 |
| R60 | If message has both Transfer-Encoding and Content-Length, sender MUST remove Content-Length before forwarding | MUST | Section 3.3.3 |
| R61 | For invalid Content-Length (differing values) in request, server MUST respond 400 and close; in response via proxy, proxy MUST close, discard, send 502; in user agent, user agent MUST close and discard | MUST | Section 3.3.3 |
| R62 | If fewer octets received than Content-Length, recipient MUST consider message incomplete and close | MUST | Section 3.3.3 |
| R63 | Server SHOULD generate encoding or length-delimited messages whenever possible | SHOULD | Section 3.3.3 |
| R64 | Client sending request with body SHOULD use Content-Length if length known in advance, rather than chunked | SHOULD | Section 3.3.3 |
| R65 | User agent sending request with body MUST send valid Content-Length if does not know server handles HTTP/1.1 or later | MUST | Section 3.3.3 |
| R66 | Client MUST NOT process, cache, or forward extra data after final response as separate response | MUST | Section 3.3.3 |
| R67 | Server receiving incomplete request MAY send error response | MAY | Section 3.4 |
| R68 | Client receiving incomplete response MUST record as incomplete | MUST | Section 3.4 |
| R69 | HTTP/1.1 user agent MUST NOT preface or follow request with extra CRLF | MUST | Section 3.5 |
| R70 | Server expecting request-line SHOULD ignore at least one CRLF received prior | SHOULD | Section 3.5 |
| R71 | Recipient MAY recognize single LF as line terminator | MAY | Section 3.5 |
| R72 | Recipients MAY parse on whitespace-delimited word boundaries (lenient) | MAY | Section 3.5 |
| R73 | Server receiving non-HTTP-message sequence SHOULD respond 400 | SHOULD | Section 3.5 |
| R74 | Recipient MUST be able to parse and decode chunked transfer coding | MUST | Section 4.1 |
| R75 | Recipient MUST ignore unrecognized chunk extensions | MUST | Section 4.1.1 |
| R76 | Sender MUST NOT generate trailer containing forbidden fields (framing, routing, etc.) | MUST | Section 4.1.2 |
| R77 | Recipient MAY process allowed trailer fields as if appended to header section; MUST ignore forbidden trailer fields | MAY/MUST | Section 4.1.2 |
| R78 | Unless TE indicates "trailers" acceptable, server SHOULD NOT generate trailer fields necessary for user agent | SHOULD | Section 4.1.2 |
| R79 | Client MUST NOT send chunked in TE header field | MUST | Section 4.3 |
| R80 | Sender of TE MUST also send "TE" connection option in Connection header field | MUST | Section 4.3 |
| R81 | Sender SHOULD generate Trailer header field before message body to indicate future trailer fields | SHOULD | Section 4.4 |
| R82 | When making request directly to origin server (except CONNECT/OPTIONS*), client MUST send origin-form (path and query only) | MUST | Section 5.3.1 |
| R83 | If path empty, client MUST send "/" | MUST | Section 5.3.1 |
| R84 | When making request to proxy (except CONNECT/OPTIONS*), client MUST send absolute-form (absolute URI) | MUST | Section 5.3.2 |
| R85 | Server MUST accept absolute-form in requests | MUST | Section 5.3.2 |
| R86 | For CONNECT request, client MUST send authority-form (authority only, no userinfo) | MUST | Section 5.3.3 |
| R87 | For server-wide OPTIONS, client MUST send asterisk-form ("*") | MUST | Section 5.3.4 |
| R88 | If proxy receives OPTIONS with absolute-form and empty path, last proxy MUST send "*" when forwarding | MUST | Section 5.3.4 |
| R89 | Client MUST send Host header field in all HTTP/1.1 requests; if authority component exists, Host identical; if missing, Host empty | MUST | Section 5.4 |
| R90 | User agent SHOULD generate Host as first header field | SHOULD | Section 5.4 |
| R91 | Client MUST send Host even if request-target in absolute-form | MUST | Section 5.4 |
| R92 | Proxy receiving absolute-form request MUST ignore received Host and replace with host from request-target; MUST generate new Host | MUST | Section 5.4 |
| R93 | Server MUST respond with 400 to request lacking Host, more than one Host, or invalid Host | MUST | Section 5.4 |
| R94 | Client with multiple outstanding requests MUST maintain list and associate response to highest ordered request not yet final | MUST | Section 5.6 |
| R95 | Proxy MUST send appropriate Via header field in each forwarded message | MUST | Section 5.7.1 |
| R96 | HTTP-to-HTTP gateway MUST send Via in each inbound request | MUST | Section 5.7.1 |
| R97 | Intermediary SHOULD NOT forward names/ports of hosts behind firewall unless explicitly enabled | SHOULD | Section 5.7.1 |
| R98 | Intermediary MUST NOT combine Via entries with different received-protocol values | MUST | Section 5.7.1 |
| R99 | Proxy MUST NOT change host name if fully qualified domain name | MUST | Section 5.7.2 |
| R100 | Proxy MUST NOT modify absolute-path and query parts of request-target when forwarding (except empty path to "/" or "*") | MUST | Section 5.7.2 |
| R101 | Proxy MUST NOT transform payload of message with no-transform directive | MUST | Section 5.7.2 |
| R102 | Proxy MAY transform payload without no-transform; MUST add Warning 214 if transformed; MAY change status to 203 | MUST/MAY | Section 5.7.2 |
| R103 | Proxy SHOULD NOT modify endpoint, resource state, or representation header fields | SHOULD | Section 5.7.2 |
| R104 | Proxy or gateway MUST remove or replace any received connection options before forwarding | MUST | Section 6.1 |
| R105 | When header field aside from Connection used for connection control, sender MUST list field-name in Connection | MUST | Section 6.1 |
| R106 | Proxy/gateway MUST parse Connection before forwarding, remove header fields with same names as connection-options, and remove Connection header itself | MUST | Section 6.1 |
| R107 | Sender MUST NOT send connection option corresponding to header field intended for all recipients | MUST | Section 6.1 |
| R108 | Client not supporting persistent connections MUST send "close" in every request | MUST | Section 6.1 |
| R109 | Server not supporting persistent connections MUST send "close" in every response (except 1xx) | MUST | Section 6.1 |
| R110 | Implementations SHOULD support persistent connections | SHOULD | Section 6.3 |
| R111 | Server MUST read entire request body or close after response; client MUST read entire response body if intending to reuse connection | MUST | Section 6.3 |
| R112 | Proxy MUST NOT maintain persistent connection with HTTP/1.0 client | MUST | Section 6.3 |
| R113 | Proxy MUST NOT automatically retry non-idempotent requests | MUST | Section 6.3.1 |
| R114 | User agent MUST NOT automatically retry non-idempotent request unless knows idempotent or can detect original never applied | MUST | Section 6.3.1 |
| R115 | Client SHOULD NOT automatically retry a failed automatic retry | SHOULD | Section 6.3.1 |
| R116 | Server MAY process pipelined requests in parallel if safe methods, but MUST send responses in same order | MUST | Section 6.3.2 |
| R117 | Client that pipelines SHOULD retry unanswered requests if connection closes | SHOULD | Section 6.3.2 |
| R118 | When retrying pipelined after failed connection, client MUST NOT pipeline immediately after connection establishment | MUST | Section 6.3.2 |
| R119 | User agent SHOULD NOT pipeline after non-idempotent method until final response received | SHOULD | Section 6.3.2 |
| R120 | Intermediary receiving pipelined MAY pipeline when forwarding | MAY | Section 6.3.2 |
| R121 | Client or server wishing to time out SHOULD issue graceful close | SHOULD | Section 6.5 |
| R122 | Implementations SHOULD constantly monitor connection for closure signal | SHOULD | Section 6.5 |
| R123 | Server SHOULD sustain persistent connections when possible | SHOULD | Section 6.5 |
| R124 | Client sending message body SHOULD monitor for error response | SHOULD | Section 6.5 |
| R125 | Sender SHOULD send "close" when wishing to close after current request/response | SHOULD | Section 6.6 |
| R126 | Client sending "close" MUST NOT send further requests and MUST close after reading final response | MUST | Section 6.6 |
| R127 | Server receiving "close" MUST initiate close after sending final response; SHOULD send "close" in final response; MUST NOT process further requests | MUST/SHOULD | Section 6.6 |
| R128 | Server sending "close" MUST initiate close after sending response; MUST NOT process further requests | MUST | Section 6.6 |
| R129 | Client receiving "close" MUST cease sending requests and close after reading response; SHOULD NOT assume pipelined requests processed | MUST/SHOULD | Section 6.6 |
| R130 | Client MAY send Upgrade to invite server to switch protocols | MAY | Section 6.7 |
| R131 | Server MAY ignore Upgrade | MAY | Section 6.7 |
| R132 | Server sending 101 MUST send Upgrade with new protocol(s); MUST list in layer-ascending order; MUST NOT switch to protocol not indicated by client | MUST | Section 6.7 |
| R133 | Server sending 426 MUST send Upgrade indicating acceptable protocols | MUST | Section 6.7 |
| R134 | Server MUST NOT switch protocols unless received message semantics can be honored by new protocol | MUST | Section 6.7 |
| R135 | When Upgrade sent, sender MUST also send Connection header with "upgrade" connection option | MUST | Section 6.7 |
| R136 | Server MUST ignore Upgrade received in HTTP/1.0 request | MUST | Section 6.7 |
| R137 | If server receives Upgrade and Expect: 100-continue, server MUST send 100 before 101 | MUST | Section 6.7 |
| R138 | Sender MUST NOT generate empty list elements in ABNF list constructs | MUST | Section 7 |
| R139 | Recipient MUST accept lists with reasonable number of empty elements (for legacy) | MUST | Section 7 |
| R140 | Registration of transfer codings requires IETF Review (Section 4.1 of [RFC5226]) and MUST conform to purpose of transfer coding | MUST | Section 8.4.1 |
| R141 | Upgrade token registration is First Come First Served with specified rules | - | Section 8.6.1 |
| R142 | Server MUST NOT accept message with Transfer-Encoding and Content-Length as valid; see Section 3.3.3 for handling (part of R60) | MUST | Section 9.5 (implicit from 3.3.3) |

## Informative Annexes (Condensed)

- **Appendix A (HTTP Version History)**: Summarizes evolution from HTTP/0.9 to HTTP/1.1, changes from HTTP/1.0 (multihomed servers, keep-alive, Transfer-Encoding), and changes from RFC 2616 (detailed list of clarifications and removals such as removal of HTTP/0.9 support, deprecation of line folding, etc.).
- **Appendix B (Collected ABNF)**: Presents the complete ABNF grammar with all list operators expanded to standard ABNF notation.
- **Index**: Provides cross-references to terms and concepts used in the document.