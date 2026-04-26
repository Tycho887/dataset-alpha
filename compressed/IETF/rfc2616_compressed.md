# RFC 2616: Hypertext Transfer Protocol -- HTTP/1.1
**Source**: IETF Network Working Group | **Version**: HTTP/1.1 | **Date**: June 1999 | **Type**: Standards Track
**Obsoletes**: RFC 2068 | **Original**: https://www.rfc-editor.org/rfc/rfc2616

## Scope (Summary)
Defines the HTTP/1.1 protocol – an application-level, stateless, request/response protocol for distributed hypermedia systems. Provides more stringent requirements than HTTP/1.0 to ensure reliable implementation of features like persistent connections, caching, virtual hosts, and content negotiation.

## Normative References
- [34] RFC 2119 (Key words for requirement levels)
- [42] RFC 2396 (URI Generic Syntax)
- [36] RFC 2145 (HTTP Version Numbers)
- [43] RFC 2617 (HTTP Authentication: Basic and Digest)
- [6] RFC 1945 (HTTP/1.0)
- [7] RFC 2045 (MIME Part 1)
- [9] RFC 822 (Standard for ARPA Internet Text Messages)
- [8] RFC 1123 (Requirements for Internet Hosts – Communication Layers)
- [14] RFC 2047 (MIME Message Header Extensions for Non-ASCII Text)
- [17] RFC 1590 (Media Type Registration Procedure)
- [1] RFC 1766 (Tags for the Identification of Languages)
- [25] RFC 1952 (GZIP file format)
- [31] RFC 1950 (ZLIB Compressed Data Format)
- [29] RFC 1951 (DEFLATE Compressed Data Format)
- [23] RFC 1864 (The Content-MD5 Header Field)
- [21] ANSI X3.4-1986 (US-ASCII)
- [22] ISO-8859 (8-bit character sets)
- [28] RFC 1305 (NTP v3)
- [38] RFC 2279 (UTF-8)
- [41] RFC 2277 (IETF Policy on Character Sets and Languages)
- [45] RFC 2110 (MHTML)
- [49] RFC 2183 (Content-Disposition)
- [35] RFC 1806 (Content-Disposition – obsolete)
- [32] RFC 2069 (Digest Access Authentication – obsolete)
- [33] RFC 2068 (HTTP/1.1 – obsolete)
- [44] Luotonen, A., "Tunneling TCP based protocols through Web proxy servers" (Work in Progress)
- [46] RFC 2026 (Internet Standards Process)
- [47] RFC 2324 (HTCPCP/1.0)
- [48] RFC 2049 (MIME Part 5)

## Definitions and Abbreviations
- **connection**: Transport layer virtual circuit between two programs for communication.
- **message**: Basic unit of HTTP communication – a structured sequence of octets (Section 4 syntax).
- **request**: HTTP request message (Section 5).
- **response**: HTTP response message (Section 6).
- **resource**: Network data object/service identified by a URI (Section 3.2).
- **entity**: Payload of a request/response; consists of entity-header fields and entity-body (Section 7).
- **representation**: Entity included with a response subject to content negotiation (Section 12).
- **content negotiation**: Mechanism for selecting the appropriate representation (Section 12).
- **variant**: One of possibly multiple representations associated with a resource at a given instant.
- **client**: Program that establishes connections for sending requests.
- **user agent**: Client that initiates a request (e.g., browsers, spiders).
- **server**: Application program that accepts connections and services requests.
- **origin server**: Server on which a given resource resides or is to be created.
- **proxy**: Intermediary that acts as both client and server for making requests on behalf of others. A proxy MUST implement both client and server requirements of this specification.
- **gateway**: Server that acts as an intermediary for some other server; receives requests as if it were the origin server.
- **tunnel**: Blind relay between two connections; ceases to exist when both ends are closed.
- **cache**: Local store of response messages and control subsystem. A cache stores cacheable responses. Any client or server may include a cache, but a tunnel cannot.
- **cacheable**: A response is cacheable if a cache is allowed to store a copy for use in answering subsequent requests (rules in Section 13).
- **first-hand**: Response coming directly from origin server without unnecessary delay.
- **explicit expiration time**: Time at which origin server intends an entity to no longer be returned by a cache without further validation.
- **heuristic expiration time**: Expiration time assigned by a cache when no explicit expiration time is available.
- **age**: Time since response was sent by or validated with the origin server.
- **freshness lifetime**: Length of time between generation and expiration.
- **fresh**: Response whose age has not exceeded its freshness lifetime.
- **stale**: Response whose age has passed its freshness lifetime.
- **semantically transparent**: A cache behaves transparently if its use does not alter the response seen by client or origin server (except hop-by-hop headers).
- **validator**: Protocol element (e.g., entity tag or Last-Modified time) used to determine if a cache entry is equivalent to an entity.
- **upstream/downstream**: Flow direction of messages.
- **inbound/outbound**: Request path (toward origin server) and response path (toward user agent).

## 1. Introduction
### 1.1 Purpose
HTTP has been in use since 1990. HTTP/1.1 includes more stringent requirements than HTTP/1.0 to ensure reliable implementation of features such as persistent connections, caching, and virtual hosts. HTTP allows an open-ended set of methods and headers (see [47]).

### 1.2 Requirements
Key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are interpreted as described in RFC 2119 [34]. An implementation is **not compliant** if it fails to satisfy any MUST/REQUIRED level requirement. Unconditionally compliant = satisfies all MUST and SHOULD; conditionally compliant = satisfies all MUST but not all SHOULD.

### 1.3 Terminology
(See Definitions section above.)

### 1.4 Overall Operation
- HTTP is a request/response protocol. A client sends a request (method, URI, protocol version, MIME-like message with headers and body). Server responds with status line, headers, and optional body.
- Intermediaries: proxy, gateway, tunnel. A proxy forwards requests (may rewrite parts); a gateway translates to underlying server protocols; a tunnel relays blindly.
- Caches can shorten the request/response chain.
- HTTP/1.1 allows persistent connections for multiple request/response exchanges (Section 8.1).
- Default port is TCP 80; HTTP presumes a reliable transport.

## 2. Notational Conventions and Generic Grammar
### 2.1 Augmented BNF
Uses augmented BNF similar to RFC 822. Key constructs: name = definition, literal, alternatives (|), grouping, repetition (*), optional ([]), specific repetition (n), list (#rule), comments (;), implied linear white space (LWS).

### 2.2 Basic Rules
- CRLF is the end-of-line marker for all protocol elements except entity-body (see Appendix 19.3 for tolerant applications). Entity-body line breaks are defined by its media type (Section 3.7).
- LWS (linear white space) can be folded onto multiple lines; any LWS can be replaced by a single SP.
- TEXT rule: any OCTET except CTLs, including LWS. CRLF allowed only for header continuation.
- Token = 1*<any CHAR except CTLs or separators>. Separators: "(" ")" "<" ">" "@" "," ";" ":" "\" <"> "/" "[" "]" "?" "=" "{" "}" SP HT.
- quoted-string: double-quote marks; backslash quoting allowed only within quoted-string and comment constructs.

## 3. Protocol Parameters
### 3.1 HTTP Version
- Format: "HTTP/" major "." minor. Major/minor numbers treated as separate integers; leading zeros ignored/not sent.
- Version indicates message format and sender's capabilities, not features obtained.
- An application sending "HTTP/1.1" MUST be at least conditionally compliant. Compliant applications SHOULD use "HTTP/1.1" and MUST do so for messages incompatible with HTTP/1.0.
- Proxy/gateway MUST NOT forward a version indicator greater than its own version. If a higher version request is received, MUST either downgrade, respond with error, or tunnel.
- Caching proxies MUST, gateways MAY, tunnels MUST NOT upgrade request version. Response MUST be in the same major version as the request.

### 3.2 Uniform Resource Identifiers (URIs)
- URIs can be absolute or relative. HTTP does not place a priori limit on URI length; servers MUST be able to handle any URI they serve, and SHOULD handle unbounded lengths if providing GET-based forms that generate them. Server SHOULD return 414 (Request-URI Too Long) if URI longer than server can handle.

#### 3.2.1 General Syntax
- Definitions from RFC 2396: URI-reference, absoluteURI, relativeURI, port, host, abs_path, rel_path, authority.

#### 3.2.2 http URL
- Syntax: `http_URL = "http:" "//" host [ ":" port ] [ abs_path [ "?" query ]]`
- Default port 80. If abs_path absent in URL, MUST be "/" when used as Request-URI.
- Proxy receiving host name that is not fully qualified MAY add its domain; if fully qualified, MUST NOT change host name.

#### 3.2.3 URI Comparison
- SHOULD use case-sensitive octet-by-octet comparison with exceptions:
  - Empty/omitted port equals default port.
  - Host names and scheme names compared case-insensitively.
  - Empty abs_path equivalent to "/".
  - Characters other than reserved/unsafe are equivalent to their percent-encoding.

### 3.3 Date/Time Formats
#### 3.3.1 Full Date
- HTTP applications historically accept three formats: RFC 1123 (preferred), RFC 850 (obsolete), and ANSI C asctime(). HTTP/1.1 clients and servers MUST accept all three for parsing, but MUST only generate RFC 1123 format.
- All HTTP date/time stamps MUST be in GMT. HTTP-date is case-sensitive and MUST NOT include additional LWS beyond grammar.
- Grammar for HTTP-date, rfc1123-date, rfc850-date, asctime-date, wkday, weekday, month.

#### 3.3.2 Delta Seconds
- Integer number of seconds (delta-seconds = 1*DIGIT).

### 3.4 Character Sets
- HTTP uses the MIME definition of character set (conversion from octets to characters). Charset tokens are case-insensitive; IANA registry governs tokens.
- Senders SHOULD limit to IANA registered character sets.

#### 3.4.1 Missing Charset
- HTTP/1.0 misinterpretations: senders MAY include charset parameter even when ISO-8859-1, and SHOULD do so if it won't confuse recipient.
- HTTP/1.1 recipients MUST respect the charset label. User agents MUST use the charset from Content-Type if supported, rather than guessing.

### 3.5 Content Codings
- Content-coding values (token) indicate an encoding transformation applied to an entity. Case-insensitive.
- IANA registry initially includes: gzip (RFC 1952), compress (adaptive LZW), deflate (zlib + deflate), identity (no transformation). "x-gzip" and "x-compress" considered equivalent to gzip and compress for compatibility.
- New content-coding tokens SHOULD be registered with publicly available specifications.

### 3.6 Transfer Codings
- Transfer-coding values indicate an encoding transformation for safe transport, a property of the message, not entity.
- All transfer-coding values are case-insensitive. Used in TE and Transfer-Encoding headers.
- When transfer-coding applied, set MUST include "chunked" unless message terminated by connection close. Chunked MUST be the last coding applied and MUST NOT be applied more than once.
- IANA registry initially includes: chunked, identity, gzip, compress, deflate.
- New transfer-coding tokens SHOULD be registered like content-codings.
- Server receiving entity-body with unknown transfer-coding SHOULD return 501 (Unimplemented) and close connection. Server MUST NOT send transfer-codings to HTTP/1.0 client.

#### 3.6.1 Chunked Transfer Coding
- Chunked-Body = *chunk last-chunk trailer CRLF
- chunk-size in hex; last-chunk is zero chunk.
- Trailer allowed to include additional header fields. Server using chunked MUST NOT use trailer unless:
  a) request included TE header indicating "trailers" acceptable, or
  b) origin server and trailer fields are optional metadata, and recipient could use message without it.
- All HTTP/1.1 applications MUST be able to receive and decode chunked, and MUST ignore chunk-extension extensions they do not understand.

### 3.7 Media Types
- Used in Content-Type and Accept headers. Media-type = type "/" subtype *(";" parameter). Type and subtype case-insensitive; parameters may or may not be case-sensitive.
- HTTP servers MUST respect canonical form for entity-body prior to transmission except for "text" types.
- For text media, HTTP allows CRLF, bare CR, or bare LF as line breaks, as long as consistent for entire entity-body. HTTP applications MUST accept all three.
- If entity-body encoded with content-coding, underlying data must be in canonical form before encoding.
- Default charset for text types when no explicit charset is "ISO-8859-1". Data in other charsets MUST be labeled.
- Multipart types: MUST include boundary parameter; MUST use only CRLF for line breaks between body-parts; epilogue MUST be empty. Unrecognized multipart subtype MUST be treated as "multipart/mixed".

### 3.8 Product Tokens
- Used for identifying software (e.g., User-Agent, Server). Product = token ["/" product-version].
- SHOULD be short; MUST NOT be used for advertising or non-essential information.

### 3.9 Quality Values
- Floating point numbers in range 0-1 for content negotiation. qvalue: "0" optionally followed by up to 3 digits, or "1" optionally followed by up to 3 zeros. MUST NOT generate more than three digits after decimal.

### 3.10 Language Tags
- Syntax per RFC 1766: primary-tag *("-" subtag). Case-insensitive. White space not allowed. IANA administered.

### 3.11 Entity Tags
- Entity-tag = [ weak ] opaque-tag, weak = "W/", opaque-tag = quoted-string.
- Strong entity tag: shared only if entities are octet-equivalent.
- Weak entity tag: shared only if entities are semantically substitutable with no significant change.
- Entity tag MUST be unique across all versions of all entities for a particular resource. Same tag value MAY be used for entities obtained by requests on different URIs, but does not imply equivalence.

### 3.12 Range Units
- Range-unit = bytes-unit | other-range-unit. Only "bytes" defined. HTTP/1.1 implementations MAY ignore ranges specified using other units.

## 4. HTTP Message
### 4.1 Message Types
- Request and Response use generic message format: start-line, headers, empty line, optional message-body.
- Servers SHOULD ignore empty lines received where Request-Line is expected.
- HTTP/1.1 client MUST NOT preface or follow request with extra CRLF.

### 4.2 Message Headers
- Header fields: field-name ":" field-value. Field names case-insensitive. Field value MAY be preceded by LWS.
- Multiple header fields with same field-name MAY be present only if entire field-value is defined as comma-separated list. They MUST be combinable by appending with commas. Order significant; proxy MUST NOT change order.
- Good practice: general-header first, then request/response-header, then entity-header.

### 4.3 Message Body
- message-body = entity-body (if no Transfer-Encoding) or entity-body encoded as per Transfer-Encoding.
- Transfer-Encoding MUST be used to indicate any transfer-codings applied.
- Rules for when message-body allowed: presence signaled by Content-Length or Transfer-Encoding. Request message-body MUST NOT be included if method does not allow it. Server SHOULD read and forward; if method has no defined semantics for body, SHOULD ignore.
- For responses: HEAD, 1xx, 204, 304 MUST NOT include message-body. All others do (may be zero length).

### 4.4 Message Length
- Transfer-length determined by (in order):
  1. Responses that MUST NOT have body (1xx, 204, 304, HEAD): terminated by first empty line after headers.
  2. If Transfer-Encoding present and not "identity", then chunked transfer-coding defines length (unless connection close).
  3. If Content-Length present, it represents both entity-length and transfer-length. Content-Length MUST NOT be sent if they differ (i.e., if Transfer-Encoding present). If both received, Content-Length MUST be ignored.
  4. If media type "multipart/byteranges" and transfer-length not otherwise specified, self-delimiting media type defines length. MUST NOT be used unless sender knows recipient can parse it.
  5. Server closing connection.
- HTTP/1.1 requests containing body MUST include valid Content-Length unless server known to be HTTP/1.1 compliant. If not given, server SHOULD respond 400 or 411.
- All HTTP/1.1 applications MUST accept chunked transfer-coding.
- Messages MUST NOT include both Content-Length and non-identity transfer-coding.
- When Content-Length given, it MUST exactly match number of OCTETs in message-body. HTTP/1.1 user agents MUST notify user of invalid length.

### 4.5 General Header Fields
- Cache-Control, Connection, Date, Pragma, Trailer, Transfer-Encoding, Upgrade, Via, Warning.
- General-header field names can be extended reliably only with protocol version change. Unrecognized header fields treated as entity-header fields.

## 5. Request
### 5.1 Request-Line
- Request-Line = Method SP Request-URI SP HTTP-Version CRLF.
- No CR or LF except final CRLF.

#### 5.1.1 Method
- Method token: OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT, or extension-method.
- GET and HEAD MUST be supported by all general-purpose servers. Other methods OPTIONAL; if implemented, MUST have same semantics as Section 9.
- Origin server SHOULD return 405 if method known but not allowed, 501 if unrecognized or not implemented.

#### 5.1.2 Request-URI
- Four forms: "*", absoluteURI, abs_path, authority.
- AbsoluteURI REQUIRED when request made to a proxy.
- All HTTP/1.1 servers MUST accept absoluteURI form.
- Authority form used only by CONNECT method.
- For most common form (abs_path), Host header field MUST carry the authority.
- Transparent proxy MUST NOT rewrite abs_path part of Request-URI (except replace null abs_path with "/").

### 5.2 The Resource Identified by a Request
- Determined by Request-URI and Host header.
- Origin server that differentiates resources based on host (virtual hosts) MUST:
  1. If absoluteURI, host is part of Request-URI; Host header ignored.
  2. If not absoluteURI and Host header present, host is Host field value.
  3. If host invalid, return 400.
- Recipients of HTTP/1.0 request without Host MAY use heuristics.

### 5.3 Request Header Fields
- List: Accept, Accept-Charset, Accept-Encoding, Accept-Language, Authorization, Expect, From, Host, If-Match, If-Modified-Since, If-None-Match, If-Range, If-Unmodified-Since, Max-Forwards, Proxy-Authorization, Range, Referer, TE, User-Agent.
- Unrecognized header fields treated as entity-header.

## 6. Response
### 6.1 Status-Line
- Status-Line = HTTP-Version SP Status-Code SP Reason-Phrase CRLF.

#### 6.1.1 Status Code and Reason Phrase
- Status-Code is 3-digit integer. First digit defines class: 1xx Informational, 2xx Success, 3xx Redirection, 4xx Client Error, 5xx Server Error.
- Applications MUST understand the class of any status code; treat unrecognized code as x00 of that class, except that unrecognized responses MUST NOT be cached.
- Reason-Phrase is for human user; client not required to examine/display.
- Defined codes: 100, 101, 200-206, 300-305, 307, 400-417, 500-505.
- HTTP status codes extensible.

### 6.2 Response Header Fields
- Accept-Ranges, Age, ETag, Location, Proxy-Authenticate, Retry-After, Server, Vary, WWW-Authenticate.
- Unrecognized header fields treated as entity-header.

## 7. Entity
### 7.1 Entity Header Fields
- Allow, Content-Encoding, Content-Language, Content-Length, Content-Location, Content-MD5, Content-Range, Content-Type, Expires, Last-Modified, extension-header.
- Unrecognized entity-header fields SHOULD be ignored by recipient and MUST be forwarded by transparent proxies.

### 7.2 Entity Body
- Entity-body = *OCTET. Present only when a message-body is present (Section 4.3). Obtained by decoding any Transfer-Encoding.

#### 7.2.1 Type
- Determined by Content-Type and Content-Encoding (two-layer model). Content-Encoding indicates additional content codings applied; no default encoding.
- Any HTTP/1.1 message containing body SHOULD include Content-Type. If not given, recipient MAY guess; if unknown, SHOULD treat as "application/octet-stream".

#### 7.2.2 Entity Length
- Length of message-body before any transfer-codings applied. Determined per Section 4.4.

## 8. Connections
### 8.1 Persistent Connections
#### 8.1.1 Purpose
- Advantages: reduce CPU/memory, allow pipelining, reduce network congestion, reduce latency, graceful evolution.
- HTTP implementations SHOULD implement persistent connections.

#### 8.1.2 Overall Operation
- Persistent connections are default in HTTP/1.1. Client SHOULD assume server will maintain persistent connection even after error responses.
- Signaling close via Connection header with "close" token.
- Once close signaled, client MUST NOT send more requests.

##### 8.1.2.1 Negotiation
- Server MAY assume HTTP/1.1 client intends persistent unless Connection: close in request. If server chooses to close immediately after response, it SHOULD send Connection: close.
- Client MAY expect connection to remain open; if not wanting persistence, SHOULD send Connection: close.
- If either side sends close token, that request is last.
- Clients and servers SHOULD NOT assume persistence for HTTP versions <1.1 unless explicitly signaled.
- To remain persistent, all messages MUST have self-defined message length (not by connection closure), per Section 4.4.

##### 8.1.2.2 Pipelining
- Client supporting persistent connections MAY pipeline requests. Server MUST send responses in same order as requests received.
- Clients assuming persistence and pipelining SHOULD be prepared to retry on failure. On retry, MUST NOT pipeline until connection known persistent. Clients MUST be prepared to resend if server closes connection before all responses.
- Clients SHOULD NOT pipeline non-idempotent methods/sequences. Non-idempotent request SHOULD wait for response to previous request.

#### 8.1.3 Proxy Servers
- Proxy MUST signal persistent connections separately with clients and origin servers. Each persistent connection applies to only one transport link.
- Proxy MUST NOT establish HTTP/1.1 persistent connection with HTTP/1.0 client.

#### 8.1.4 Practical Considerations
- Servers will have timeout for inactive connections. No requirements on length of timeout.
- When timing out, SHOULD issue graceful close. Both sides SHOULD watch for close and respond.
- Client, server, or proxy MAY close transport connection at any time.
- Clients, servers, proxies MUST be able to recover from asynchronous close events. Client software SHOULD reopen connection and retransmit aborted sequence if idempotent. Non-idempotent MUST NOT be automatically retried (may offer user choice).
- Servers SHOULD always respond to at least one request per connection. Servers SHOULD NOT close connection in middle of transmitting response unless network/client failure suspected.
- Clients using persistent connections SHOULD limit simultaneous connections to a given server: single-user client SHOULD NOT maintain more than 2 connections. Proxy SHOULD use up to 2*N connections to another server/proxy, where N is number of simultaneously active users.

### 8.2 Message Transmission Requirements
#### 8.2.1 Persistent Connections and Flow Control
- HTTP/1.1 servers SHOULD maintain persistent connections and use TCP flow control to resolve temporary overloads, rather than terminating connections.

#### 8.2.2 Monitoring Connections for Error Status Messages
- HTTP/1.1 (or later) client sending message-body SHOULD monitor network connection for error status while transmitting. If error seen, SHOULD immediately cease transmitting body. If using chunked, zero length chunk and empty trailer MAY be used to prematurely mark end. If Content-Length preceded body, client MUST close connection.

#### 8.2.3 Use of the 100 (Continue) Status
Purpose: allow client to determine if origin server is willing to accept request before sending body.

Client requirements:
- If client will wait for 100 (Continue) before sending body, MUST send Expect: 100-continue.
- MUST NOT send Expect: 100-continue if not intending to send body.
- If sent Expect: 100-continue and never seen 100 from origin server (possibly via proxy), client SHOULD NOT wait indefinitely before sending body.

Origin server requirements:
- Upon receiving request with Expect: 100-continue, MUST either respond with 100 and continue reading, or respond with final status code. MUST NOT wait for body before sending 100. If final status, MAY close or continue to read/discard. MUST NOT perform requested method if final status.
- SHOULD NOT send 100 if request does not include Expect: 100-continue, and MUST NOT send 100 if request from HTTP/1.0 (or earlier) client. Exception: for compatibility with RFC 2068, server MAY send 100 in response to HTTP/1.1 PUT or POST without Expect: 100-continue (only for HTTP/1.1, not other versions).
- MAY omit 100 if already received some/all of request body.
- If sends 100, MUST ultimately send final status code after processing body.
- If receives request without Expect: 100-continue but with body, and sends final status before reading entire body, SHOULD NOT close connection until entire request read or client closes connection.

Proxy requirements:
- If proxy receives request with Expect: 100-continue and knows next-hop is HTTP/1.1 or higher, or does not know version, MUST forward request including Expect header.
- If knows next-hop is HTTP/1.0 or lower, MUST NOT forward request and MUST respond 417.
- Proxies SHOULD maintain cache of HTTP version numbers received from next-hop servers.
- MUST NOT forward 100 response if request was from HTTP/1.0 (or earlier) client and did not include Expect: 100-continue.

#### 8.2.4 Client Behavior if Server Prematurely Closes Connection
- If HTTP/1.1 client sends request with body, no Expect: 100-continue, not directly connected to HTTP/1.1 origin server, and sees connection close before status, SHOULD retry request.
- If retrying, MAY use binary exponential backoff algorithm described in steps. If error status received, SHOULD NOT continue and SHOULD close connection if not completed sending request.

## 9. Method Definitions
- The Host request-header field MUST accompany all HTTP/1.1 requests.

### 9.1 Safe and Idempotent Methods
#### 9.1.1 Safe Methods
- GET and HEAD SHOULD NOT have significance of taking an action other than retrieval; considered "safe". This allows user agents to represent other methods (POST, PUT, DELETE) as possibly unsafe.

#### 9.1.2 Idempotent Methods
- Methods GET, HEAD, PUT, DELETE are idempotent. OPTIONS and TRACE SHOULD NOT have side effects, so are inherently idempotent.
- A sequence of requests may be non-idempotent even if each method is idempotent.

### 9.2 OPTIONS
- Represents request for communication options available on request/response chain.
- Responses not cacheable.
- If entity-body included, media type MUST be indicated by Content-Type.
- If Request-URI is "*", applies to server in general.
- A 200 response SHOULD include header fields indicating optional features (e.g., Allow). Response body format not defined; Content Negotiation MAY be used. If no body, MUST include Content-Length: 0.
- Max-Forwards header MAY target specific proxy. If Max-Forwards is 0, proxy MUST NOT forward; SHOULD respond with own options. If greater than 0, proxy MUST decrement when forwarding. If no Max-Forwards in request, forwarded request MUST NOT include Max-Forwards.

### 9.3 GET
- Retrieve information identified by Request-URI.
- Conditional GET: If-Modified-Since, If-Unmodified-Since, If-Match, If-None-Match, or If-Range header.
- Partial GET: Range header. Intended to reduce network usage.
- Response to GET is cacheable if it meets caching requirements (Section 13).

### 9.4 HEAD
- Identical to GET except server MUST NOT return message-body.
- Metainformation SHOULD be identical to GET response.
- Response MAY be cacheable; if headers indicate change, cache MUST treat as stale.

### 9.5 POST
- Requests origin server accept enclosed entity as new subordinate of Request-URI.
- Functions: annotation, posting to groups, form submission, database extension.
- Actual function determined by server.
- Responses: 200 or 204 if no new resource; 201 if created (with Location header). Not cacheable unless appropriate Cache-Control or Expires. 303 can be used to direct to cacheable resource.
- POST requests MUST obey message transmission requirements (Section 8.2).

### 9.6 PUT
- Requests enclosed entity stored under supplied Request-URI. If resource exists, consider modified version; if not, origin server can create.
- 201 if created; 200 or 204 if modified; error response otherwise.
- Recipient MUST NOT ignore Content-* headers it doesn't understand; MUST return 501.
- If request passes through cache, cached entries SHOULD be treated as stale. Responses not cacheable.
- Fundamental difference from POST: URI in PUT identifies enclosed entity; server MUST NOT apply to different resource.
- PUT requests MUST obey Section 8.2.
- Entity-headers in PUT SHOULD be applied to resource.

### 9.7 DELETE
- Requests origin server delete resource identified by Request-URI. May be overridden by human intervention.
- Successful response: 200 (with entity), 202 (not yet enacted), or 204 (enacted no entity).
- If passes through cache, cached entries SHOULD be treated as stale. Responses not cacheable.

### 9.8 TRACE
- Used for application-layer loop-back of request message. Final recipient reflects message back as entity-body of 200 response.
- Final recipient is origin server or first proxy with Max-Forwards=0.
- TRACE request MUST NOT include entity.
- Responses MUST NOT be cached.

### 9.9 CONNECT
- Reserved for use with proxy that can dynamically switch to being a tunnel (e.g., SSL tunneling [44]).

## 10. Status Code Definitions
### 10.1 Informational 1xx
- Provisional response, only Status-Line and optional headers. No required headers.
- Servers MUST NOT send 1xx to HTTP/1.0 client except under experimental conditions.
- Client MUST be prepared to accept one or more 1xx before regular response. Unexpected 1xx MAY be ignored.
- Proxies MUST forward 1xx unless connection closed or proxy itself requested 1xx.

#### 10.1.1 100 Continue
- Client SHOULD continue with request. Server MUST send final response after completion. (See Section 8.2.3.)

#### 10.1.2 101 Switching Protocols
- Server willing to comply with client's Upgrade header. Protocol SHOULD be switched only when advantageous.

### 10.2 Successful 2xx
#### 10.2.1 200 OK
- Request succeeded. Information dependent on method used.

#### 10.2.2 201 Created
- New resource created. Response SHOULD include URI(s) in Location header. Origin server MUST create resource before returning 201. MAY contain ETag.

#### 10.2.3 202 Accepted
- Request accepted but processing not completed. Intentional non-committal.

#### 10.2.4 203 Non-Authoritative Information
- Metainformation not definitive from origin server, gathered from local/third-party copy.

#### 10.2.5 204 No Content
- Server fulfilled request but no entity-body. Response MAY include updated metainformation. User agent SHOULD NOT change document view. MUST NOT include message-body.

#### 10.2.6 205 Reset Content
- User agent SHOULD reset document view that caused request. MUST NOT include entity.

#### 10.2.7 206 Partial Content
- Server has fulfilled partial GET request. Request MUST have included Range header. Response MUST include:
  - Content-Range or multipart/byteranges (if Content-Length present, MUST match actual bytes).
  - Date
  - ETag and/or Content-Location if would have been in 200.
  - Expires, Cache-Control, and/or Vary if might differ.
- If result of If-Range with strong validator, SHOULD NOT include other entity-headers; if weak validator, MUST NOT.
- Cache MUST NOT combine 206 with other cached content if ETag or Last-Modified don't match exactly.
- Cache not supporting Range and Content-Range MUST NOT cache 206.

### 10.3 Redirection 3xx
- Further action needed. Action MAY be carried out without user interaction only if second request method is GET or HEAD. Client SHOULD detect infinite redirection loops.

#### 10.3.1 300 Multiple Choices
- Requested resource has multiple representations. Response SHOULD include entity with list. Location field MAY indicate server's preferred URI. Cacheable unless indicated otherwise.

#### 10.3.2 301 Moved Permanently
- New permanent URI given in Location. Future references SHOULD use new URI. Cacheable unless indicated otherwise. User agent MUST NOT automatically redirect for methods other than GET/HEAD unless confirmed by user.

#### 10.3.3 302 Found
- Resource temporarily under different URI. Client SHOULD continue to use Request-URI. Cacheable only if indicated.

#### 10.3.4 303 See Other
- Response found under different URI and SHOULD be retrieved using GET. MUST NOT be cached. Note: many pre-HTTP/1.1 user agents treat 302 as 303.

#### 10.3.5 304 Not Modified
- Conditional GET: document not modified. MUST NOT contain message-body. Response MUST include Date (unless omitted per 14.18.1), and ETag/Content-Location, Expires/Cache-Control/Vary if would have been in 200. If strong validator, SHOULD NOT include other entity-headers; if weak, MUST NOT.
- If 304 indicates entity not cached, cache MUST disregard and repeat request without conditional.
- If updating cache entry with 304, MUST update to reflect new field values.

#### 10.3.6 305 Use Proxy
- Resource MUST be accessed through proxy given in Location. Must only be generated by origin servers.

#### 10.3.7 306 (Unused)
- Reserved.

#### 10.3.8 307 Temporary Redirect
- Resource temporarily under different URI. Client SHOULD continue to use Request-URI. Cacheable only if indicated. User agent MUST NOT automatically redirect for methods other than GET/HEAD unless confirmed by user.

### 10.4 Client Error 4xx
- Client seems to have erred. Server SHOULD include entity explaining error. User agents SHOULD display entity.
- Server using TCP SHOULD ensure client acknowledges receipt before closing input connection.

#### 10.4.1 400 Bad Request
- Malformed syntax. Client SHOULD NOT repeat without modifications.

#### 10.4.2 401 Unauthorized
- Requires authentication. Response MUST include WWW-Authenticate header.

#### 10.4.3 402 Payment Required
- Reserved.

#### 10.4.4 403 Forbidden
- Server understood but refuses. Authorization will not help; request SHOULD NOT be repeated.

#### 10.4.5 404 Not Found
- Nothing matching Request-URI.

#### 10.4.6 405 Method Not Allowed
- Method not allowed for resource. Response MUST include Allow header.

#### 10.4.7 406 Not Acceptable
- Resource only capable of generating responses not acceptable per accept headers. Response SHOULD include entity with available characteristics.

#### 10.4.8 407 Proxy Authentication Required
- Similar to 401, but proxy. Proxy MUST return Proxy-Authenticate.

#### 10.4.9 408 Request Timeout
- Client did not produce request within server's wait time.

#### 10.4.10 409 Conflict
- Request could not be completed due to conflict with current resource state. Response body SHOULD include enough information for user to resolve.

#### 10.4.11 410 Gone
- Resource permanently unavailable. Cacheable unless indicated otherwise.

#### 10.4.12 411 Length Required
- Server refuses request without defined Content-Length.

#### 10.4.13 412 Precondition Failed
- Precondition in request-header fields evaluated false.

#### 10.4.14 413 Request Entity Too Large
- Request entity larger than server willing/able to process. MAY close connection. If temporary, SHOULD include Retry-After.

#### 10.4.15 414 Request-URI Too Long
- Server refuses because URI too long.

#### 10.4.16 415 Unsupported Media Type
- Entity format not supported for requested method.

#### 10.4.17 416 Requested Range Not Satisfiable
- If request included Range and no range-specifier values overlap current resource extent (unless If-Range present). Response SHOULD include Content-Range specifying current length. MUST NOT use multipart/byteranges.

#### 10.4.18 417 Expectation Failed
- Expectation in Expect header could not be met.

### 10.5 Server Error 5xx
- Server aware it has erred or incapable.
#### 10.5.1 500 Internal Server Error
- Unexpected condition prevented fulfillment.
#### 10.5.2 501 Not Implemented
- Server does not support required functionality.
#### 10.5.3 502 Bad Gateway
- Gateway/proxy received invalid response from upstream server.
#### 10.5.4 503 Service Unavailable
- Temporary overloading or maintenance. MAY indicate delay in Retry-After.
#### 10.5.5 504 Gateway Timeout
- Gateway/proxy did not receive timely response from upstream server.
#### 10.5.6 505 HTTP Version Not Supported
- Server does not support HTTP version used. Response SHOULD describe supported protocols.

## 11. Access Authentication
- HTTP provides several OPTIONAL challenge-response authentication mechanisms. General framework defined in [43].

## 12. Content Negotiation
- Two kinds: server-driven and agent-driven (orthogonal; can be combined as transparent negotiation).

### 12.1 Server-driven Negotiation
- Selection by server algorithm based on request headers (Accept, Accept-Language, Accept-Encoding) or other info.
- Vary header expresses parameters used.

### 12.2 Agent-driven Negotiation
- Selection by user agent after receiving initial response (e.g., list of alternatives). Defined status codes: 300, 406.

### 12.3 Transparent Negotiation
- Combination: cache performs server-driven negotiation on behalf of origin server using agent-driven info. Not defined in this spec.

## 13. Caching in HTTP
- Goal: eliminate need to send requests (expiration) and full responses (validation). Protocol allows origin servers, caches, and clients to explicitly reduce transparency when necessary.
- Basic principle: it must be possible for clients to detect any relaxation of semantic transparency.

### 13.1.1 Cache Correctness
- A correct cache MUST respond with the most up-to-date appropriate response held that meets one of:
  1. Revalidated with origin server (Section 13.3).
  2. "Fresh enough" (Section 13.2) – default is least restrictive freshness requirement of client, origin server, and cache; if origin server so specifies, it's that alone. If not fresh enough, cache MAY still return with Warning in carefully considered circumstances unless prohibited.
  3. Appropriate 304, 305, or error response.
- If cache cannot communicate with origin server, correct cache SHOULD respond as above if possible; if not, MUST return error/warning.
- If cache receives response that is no longer fresh after forwarding (e.g., in transit), SHOULD forward without new Warning.

### 13.1.2 Warnings
- Whenever cache returns response that is neither first-hand nor fresh enough, MUST attach Warning header.
- Warning codes: 1xx (freshness/revalidation status, MUST be deleted after successful revalidation; generated only by caches when validating, not by clients); 2xx (entity aspect not rectified by revalidation, MUST NOT be deleted).
- Multiple warnings allowed. HTTP/1.0 caches will cache all Warnings, so extra warning-date field provided.

### 13.1.3 Cache-control Mechanisms
- Cache-Control header allows explicit directives overriding default algorithms. Most restrictive interpretation applies if conflict.

### 13.1.4 Explicit User Agent Warnings
- User agent SHOULD NOT default to non-transparent or abnormally ineffective caching; MAY be explicitly configured by user.
- If user overrides, SHOULD explicitly indicate stale information.

### 13.1.5 Exceptions to the Rules and Warnings
- Operator of cache MAY choose to return stale responses. MUST mark with Warning. SHOULD NOT return stale if client explicitly requests first-hand/fresh, unless impossible.

### 13.1.6 Client-controlled Behavior
- Client MAY specify max age, min time before expiration, or accept stale responses up to a maximum staleness (via Cache-Control directives).

### 13.2 Expiration Model
#### 13.2.1 Server-Specified Expiration
- Origin server can provide explicit expiration time in future; cache MAY use fresh response without contacting server.
- If origin server wishes to force validation every request, it MAY assign an explicit expiration time in the past. To force all caches to validate, SHOULD use "must-revalidate".
- Expiration specified via Expires header or max-age directive of Cache-Control.

#### 13.2.2 Heuristic Expiration
- Caches may assign heuristic expiration times using other header values (e.g., Last-Modified). HTTP/1.1 imposes worst-case constraints; heuristic expiration ought to be used cautiously.

#### 13.2.3 Age Calculations
- Age calculation: `current_age = corrected_initial_age + resident_time`
- corrected_initial_age = max(apparent_age, age_value) + response_delay
- apparent_age = max(0, response_time - date_value)
- response_delay = response_time - request_time
- When response generated from cache entry, MUST include single Age header field with value equal to current_age.
- Presence of Age implies response not first-hand.

#### 13.2.4 Expiration Calculations
- freshness_lifetime = max_age_value (if present) or expires_value - date_value (if Expires present) or heuristic.
- Cache MUST attach Warning 113 to any response whose age > 24 hours if not already added.
- If response has Last-Modified, heuristic expiration SHOULD be no more than some fraction of interval since that time (e.g., 10%).
- Response is fresh if freshness_lifetime > current_age.

#### 13.2.5 Disambiguating Expiration Values
- If client performing retrieval receives non-first-hand response for request already fresh in its own cache, and existing Date is newer, client MAY ignore response and retry with "Cache-Control: max-age=0".
- If cache has two fresh responses for same representation with different validators, MUST use the one with more recent Date.

#### 13.2.6 Disambiguating Multiple Responses
- If client receives response with Date older than existing entry, SHOULD repeat request unconditionally with "Cache-Control: max-age=0" or "no-cache".
- If Date values equal, client MAY use either.
- Servers MUST NOT depend on clients choosing deterministically between responses during same second if expiration times overlap.

### 13.3 Validation Model
- Cache has stale entry; validates with origin server using conditional methods.
- Key protocol features: cache validators (entity tags, Last-Modified). Conditional request carries validator; server responds with 304 if matches, else full response.

#### 13.3.1 Last-Modified Dates
- Used as cache validator; cache entry valid if entity not modified since that value.

#### 13.3.2 Entity Tag Cache Validators
- ETag provides opaque validator; allows more reliable validation.

#### 13.3.3 Weak and Strong Validators
- Strong validator changes whenever entity bits change; weak changes on semantic changes.
- Weak validators only usable in contexts not depending on exact equality (e.g., sub-range retrieval requires strong).
- Two comparison functions: strong (both identical and not weak) and weak (identical, may be weak).
- Last-Modified is weak unless it can be proved strong (see rules).
- Cache or origin server receiving conditional request other than full-body GET MUST use strong comparison.

#### 13.3.4 Rules for When to Use Entity Tags and Last-Modified Dates
- Origin servers:
  - SHOULD send entity tag unless unfeasible.
  - MAY send weak entity tag if performance considerations support.
  - SHOULD send Last-Modified if feasible unless risk of transparency breakdown.
- Preferred: both strong entity tag and Last-Modified.
- Clients:
  - If entity tag provided, MUST use it in cache-conditional requests (If-Match/If-None-Match).
  - If only Last-Modified, SHOULD use in non-subrange requests (If-Modified-Since).
  - If both, SHOULD use both.
- When both Last-Modified and entity tags present, server MUST NOT return 304 unless consistent with all conditional headers.

#### 13.3.5 Non-validating Conditionals
- Comparisons of headers other than Last-Modified never used for cache validation.

### 13.4 Response Cacheability
- Unless constrained by cache-control, caching system MAY always store a successful response.
- Status codes 200, 203, 206, 300, 301, 410 MAY be stored by cache subject to expiration. Cache not supporting Range/Content-Range MUST NOT cache 206.
- Other status codes MUST NOT be returned from cache unless explicitly allowed by cache-control directives or other headers (Expires, max-age, etc.).

### 13.5 Constructing Responses From Caches
#### 13.5.1 End-to-end and Hop-by-hop Headers
- End-to-end headers MUST be stored and transmitted in any response from cache entry.
- Hop-by-hop headers: Connection, Keep-Alive, Proxy-Authenticate, Proxy-Authorization, TE, Trailers, Transfer-Encoding, Upgrade.
- Other hop-by-hop headers MUST be listed in Connection header.

#### 13.5.2 Non-modifiable Headers
- Transparent proxy MUST NOT modify: Content-Location, Content-MD5, ETag, Last-Modified in request/response; Expires in response. MAY add Expires if not present (MUST be same as Date).
- Proxy MUST NOT modify or add Content-Encoding, Content-Range, Content-Type in messages containing no-transform directive or in any request.
- Non-transparent proxy MAY modify/add these if no-transform absent, but MUST add Warning 214.
- Transparent proxy MUST preserve entity-length, MAY change transfer-length.

#### 13.5.3 Combining Headers
- On receiving 304 or 206, cache constructs response using stored entity-body and combines headers.
- End-to-end headers from 304/206 MUST replace corresponding headers from cache entry, except: 1xx Warning deleted; 2xx Warning retained.
- Cache MUST also replace end-to-end headers stored with entry with incoming response headers (except Warning).

#### 13.5.4 Combining Byte Ranges
- If cache has partial ranges and receives another subrange, MAY combine if both have cache validators that match using strong comparison.
- If not, MUST use only most recent partial response (based on Date).

### 13.6 Caching Negotiated Responses
- Server SHOULD use Vary header to inform cache of selecting request-header fields.
- Cache MUST NOT use cache entry for subsequent request unless all selecting request-headers match (by removing LWS and combining headers). "*" always fails to match.
- If no match, cache MUST relay request to origin server conditionally.
- If entity tag assigned, forwarded request SHOULD include entity tags in If-None-Match.
- If cache receives successful response whose Content-Location matches existing entry, entity-tag differs, and Date more recent, existing entry SHOULD NOT be returned and SHOULD be deleted.

### 13.7 Shared and Non-Shared Caches
- Non-shared cache accessible only to single user; should be enforced by security mechanisms. All others are shared.

### 13.8 Errors or Incomplete Response Cache Behavior
- Cache receiving incomplete response MAY store as partial; MUST NOT return partial without 206 status. MUST NOT use 200 for partial.
- If receives 5xx while revalidating, MAY forward 5xx or act as if server failed; may return previously received response unless "must-revalidate".

### 13.9 Side Effects of GET and HEAD
- Unless origin server prohibits caching, GET and HEAD SHOULD NOT have side effects that would cause erroneous behavior if cached.
- Caches MUST NOT treat responses to query URIs (containing "?") as fresh unless server provides explicit expiration time.

### 13.10 Invalidation After Updates or Deletions
- Methods PUT, DELETE, POST MUST cause cache to invalidate the entity (referenced by Request-URI, Location, or Content-Location). Invalidation based on URI in Location/Content-Location only if host part same as Request-URI.
- Cache that passes through methods it does not understand SHOULD invalidate entities referred to by Request-URI.

### 13.11 Write-Through Mandatory
- All methods that might modify origin server's resources MUST be written through. Cache MUST NOT reply to such request before transmitting to inbound server and receiving response. (Does not prevent 100 Continue.)

### 13.12 Cache Replacement
- If new cacheable response received while existing responses for same resource are cached, cache SHOULD use new response to reply to current request. May insert into cache. If new response has older Date header than existing cached responses, it is not cacheable.

### 13.13 History Lists
- History mechanisms SHOULD NOT try to be semantically transparent; they show exactly what user saw. Expiration time does not apply by default. SHOULD display even if expired unless user configured to refresh.

## 14. Header Field Definitions
### 14.1 Accept
- Specifies media types acceptable for response.
- Grammar: `Accept = "Accept" ":" #( media-range [ accept-params ] )`
- Each media-range may have quality factor q (0 to 1). Default q=1.
- If no Accept header, client accepts all media types. If present and server cannot send acceptable response, SHOULD send 406.
- More specific media ranges override less specific.

### 14.2 Accept-Charset
- Indicates acceptable character sets. Grammar: `Accept-Charset = "Accept-Charset" ":" 1#( ( charset | "*" )[ ";" "q" "=" qvalue ] )`
- Default q=1. "*" matches every charset not mentioned. ISO-8859-1 gets q=1 if not mentioned.
- If no header, any charset acceptable. If present and server cannot send acceptable charset, SHOULD send 406.

### 14.3 Accept-Encoding
- Restricts content-codings acceptable in response. Grammar: `Accept-Encoding = "Accept-Encoding" ":" 1#( codings [ ";" "q" "=" qvalue ] )`
- Codings include content-coding or "*". Rules for testing acceptability:
  1. If content-coding listed and q not 0, acceptable.
  2. "*" matches any not listed.
  3. Highest non-zero qvalue preferred.
  4. "identity" always acceptable unless explicitly refused (identity;q=0 or *;q=0 without identity).
- If header absent, server MAY assume client will accept any content coding; but if identity available, SHOULD use identity.

### 14.4 Accept-Language
- Restricts preferred natural languages. Grammar: `Accept-Language = "Accept-Language" ":" 1#( language-range [ ";" "q" "=" qvalue ] )`
- Language-range matches language-tag if exact or prefix followed by "-". Default q=1.
- If header absent, server SHOULD assume all languages equally acceptable.
- Client applications SHOULD make choice of linguistic preference available to user. If not available, MUST NOT send Accept-Language.

### 14.5 Accept-Ranges
- Server indicates acceptance of range requests. Grammar: `Accept-Ranges = "Accept-Ranges" ":" acceptable-ranges`
- Values: range-unit or "none".

### 14.6 Age
- Sender's estimate of time since response generated/revalidated. Grammar: `Age = "Age" ":" age-value`
- Non-negative decimal integer (seconds). If cache receives value larger than can represent, MUST transmit 2147483648 (2^31). An HTTP/1.1 server that includes a cache MUST include Age in every response generated from its own cache.

### 14.7 Allow
- Lists methods supported by resource. MUST be present in 405 response. Proxy MUST NOT modify Allow header.

### 14.8 Authorization
- User agent authenticates with server using credentials. Grammar: `Authorization = "Authorization" ":" credentials`
- Shared cache receiving request containing Authorization MUST NOT return corresponding response to other requests unless:
  1. Response includes "s-maxage" directive (proxy MUST revalidate if expired).
  2. Response includes "must-revalidate".
  3. Response includes "public".

### 14.9 Cache-Control
- General-header field with directives for caches. Directives are unidirectional. MUST be passed through by proxy/gateway.
- Cache request directives: no-cache, no-store, max-age, max-stale, min-fresh, no-transform, only-if-cached.
- Cache response directives: public, private, no-cache, no-store, no-transform, must-revalidate, proxy-revalidate, max-age, s-maxage.
- Wildcard field-name parameter applies only to named fields.

#### 14.9.1 What is Cacheable
- Default: response cacheable if method, headers, status indicate. Override with:
  - public: MAY be cached by any cache.
  - private: MUST NOT be cached by shared cache.
  - no-cache: without field-name, cache MUST NOT use response without revalidation. With field-name, specified headers MUST NOT be sent without revalidation.

#### 14.9.2 What May be Stored by Caches
- no-store: cache MUST NOT store any part of request/response (non-volatile) and make best-effort to remove from volatile storage. Applies to both shared and non-shared caches. History buffers MAY store.

#### 14.9.3 Modifications of the Basic Expiration Mechanism
- max-age overrides Expires. Response is stale if current age > max-age.
- s-maxage: for shared cache only, overrides max-age and Expires; implies proxy-revalidate.
- Request directives: max-age (client willing to accept response with age ≤ specified), min-fresh (response fresh for at least specified seconds), max-stale (willing to accept stale response up to specified seconds). Cache returning stale response due to max-stale MUST attach Warning 110.

#### 14.9.4 Cache Revalidation and Reload Controls
- End-to-end reload: request includes "no-cache".
- Specific end-to-end revalidation: "max-age=0" with cache-validating conditional.
- Unspecified end-to-end revalidation: "max-age=0" without conditional.
- only-if-cached: cache SHOULD respond with cached entry or 504.
- must-revalidate: cache MUST NOT use stale entry without revalidation; if cannot reach origin server, MUST generate 504.
- proxy-revalidate: same as must-revalidate but does not apply to user agent caches.

#### 14.9.5 No-Transform Directive
- Intermediate cache/proxy MUST NOT change headers listed in 13.5.2 (Content-Encoding, Content-Range, Content-Type) and entity-body.

#### 14.9.6 Cache Control Extensions
- Extensible via cache-extension tokens. Unrecognized directives MUST be ignored.

### 14.10 Connection
- Allows sender to specify options for particular connection; MUST NOT be communicated by proxies over further connections.
- Proxies MUST parse Connection header and remove header fields with same name as connection-tokens.
- "close" connection option signals connection will close after response.
- HTTP/1.1 applications not supporting persistent connections MUST include "close" in every message.

### 14.11 Content-Encoding
- Modifier on media type; value indicates additional content codings applied to entity-body.
- Example: `Content-Encoding: gzip`
- If content-coding not identity, response MUST include Content-Encoding listing non-identity encodings.
- If content-coding not acceptable to origin server, SHOULD respond 415.
- Multiple encodings MUST be listed in order applied.

### 14.12 Content-Language
- Describes natural language(s) of intended audience for enclosed entity.
- Example: `Content-Language: da`
- If no Content-Language specified, default is all language audiences.
- Multiple languages MAY be listed.

### 14.13 Content-Length
- Indicates size of entity-body in decimal number of OCTETs.
- Example: `Content-Length: 3495`
- SHOULD use this field to indicate transfer-length unless prohibited by Section 4.4.
- Any value ≥ 0 valid.

### 14.14 Content-Location
- Supplies resource location for entity when accessible from separate location.
- Value can be absolute or relative URI. Relative interpreted relative to Request-URI.
- Not a replacement for original URI; future requests MAY specify it.
- Cache cannot assume entity with different Content-Location can be used for later requests on that URI.

### 14.15 Content-MD5
- MD5 digest of entity-body for end-to-end integrity check.
- Only origin servers or clients MAY generate; proxies and gateways MUST NOT.
- Digest computed based on entity-body including any content-coding, before transfer-encoding.
- Line break conversion MUST NOT be done before computing digest.

### 14.16 Content-Range
- Sent with partial entity-body to specify where partial body should be applied.
- Grammar: `Content-Range = "Content-Range" ":" content-range-spec`
- SHOULD indicate total length of full entity-body unless unknown; "*" means unknown.
- Invalid byte-range-resp-spec MUST be ignored.
- Response with 416 SHOULD include Content-Range with byte-range-resp-spec "*".
- Response with 206 MUST NOT include Content-Range with "*".
- Single range response MUST NOT use multipart/byteranges. Multiple ranges use multipart/byteranges.
- Server SHOULD return ranges in order they appeared in request.
- Invalid range-spec: treat as if Range header absent (return 200).
- Unsatisfiable Range (first-byte-pos > current length): SHOULD return 416.

### 14.17 Content-Type
- Indicates media type of entity-body.
- Example: `Content-Type: text/html; charset=ISO-8859-4`

### 14.18 Date
- Date and time message was originated. Must be in RFC 1123 format.
- Origin servers MUST include Date in all responses except:
  1. 100 or 101 (MAY include).
  2. Server error (500, 503) if inconvenient.
  3. Server without clock – MUST NOT include Date; must follow Section 14.18.1.
- Received message without Date MUST be assigned one by recipient if cached or gatewayed.
- HTTP implementation without clock MUST NOT cache responses without revalidating on every use.
- Clients SHOULD only send Date in messages with entity-body (e.g., PUT, POST); optional.

#### 14.18.1 Clockless Origin Server Operation
- Origin server without clock MUST NOT assign Expires or Last-Modified unless values from reliable source. MAY assign Expires known to be in past.

### 14.19 ETag
- Provides current entity tag for requested variant.
- Grammar: `ETag = "ETag" ":" entity-tag`
- Examples: `ETag: "xyzzy"`, `ETag: W/"xyzzy"`, `ETag: ""`

### 14.20 Expect
- Indicates particular server behaviors required.
- Grammar: `Expect = "Expect" ":" 1#expectation`
- Expectation: "100-continue" or expectation-extension.
- Server that does not understand expectation MUST respond 417.
- If server receives expectation-extension it does not support, MUST respond 417.
- Comparison case-insensitive for unquoted tokens.
- Expect mechanism is hop-by-hop; proxy MUST return 417 if cannot meet expectation. However, Expect header is end-to-end and MUST be forwarded.

### 14.21 Expires
- Gives date/time after which response is stale.
- Format: `Expires = "Expires" ":" HTTP-date` (must be RFC 1123).
- If response includes max-age, max-age overrides Expires.
- Invalid date formats (including "0") MUST be treated as "already expired".
- To mark as "already expired", send Expires equal to Date.
- To mark as "never expires", send date approximately one year from now. Servers SHOULD NOT send more than one year.
- Presence of future Expires on otherwise non-cacheable response indicates cacheable unless Cache-Control prohibits.

### 14.22 From
- Contains Internet e-mail address of human user controlling user agent.
- Example: `From: webmaster@w3.org`
- SHOULD be machine-usable. MAY be used for logging; SHOULD NOT be used as insecure access protection.
- Robot agents SHOULD include.
- Client SHOULD NOT send without user's approval; user should be able to disable/enable/modify.

### 14.23 Host
- Specifies Internet host and port of resource being requested.
- Grammar: `Host = "Host" ":" host [ ":" port ]`
- A client MUST include Host header in all HTTP/1.1 request messages. If requested URI does not include host name, Host header MUST be given with empty value.
- HTTP/1.1 proxy MUST ensure forwarded request contains appropriate Host header.
- All Internet-based HTTP/1.1 servers MUST respond with 400 to any HTTP/1.1 request lacking Host header.

### 14.24 If-Match
- Used to make method conditional; client verifies entity tags match.
- Grammar: `If-Match = "If-Match" ":" ( "*" | 1#entity-tag )`
- If any entity tag matches (strong comparison) or "*" and entity exists, server MAY perform method.
- If no match or "*" and no entity, server MUST NOT perform method and MUST return 412.
- If request would result in something other than 2xx or 412 without header, If-Match MUST be ignored.
- "If-Match: *": method SHOULD be performed if representation exists, MUST NOT if not.

### 14.25 If-Modified-Since
- Makes GET conditional on modification since given date.
- Grammar: `If-Modified-Since = "If-Modified-Since" ":" HTTP-date`
- If not modified, server SHOULD return 304.
- If date invalid, treat as normal GET.

### 14.26 If-None-Match
- Makes method conditional on entity tags not matching.
- Grammar: `If-None-Match = "If-None-Match" ":" ( "*" | 1#entity-tag )`
- If any entity tag matches (strong or weak only for GET/HEAD) or "*" and entity exists, server MUST NOT perform method; for GET/HEAD, SHOULD return 304; otherwise 412.
- If no tags match, server MAY perform method and MUST ignore any If-Modified-Since.
- If request would result in something other than 2xx or 304 without header, If-None-Match MUST be ignored.
- "If-None-Match: *": method MUST NOT be performed if representation exists, SHOULD if not.

### 14.27 If-Range
- Used with Range: if entity unchanged, send missing part(s); else send entire entity.
- Grammar: `If-Range = "If-Range" ":" ( entity-tag | HTTP-date )`
- SHOULD only be used together with Range; MUST be ignored if no Range.
- If entity tag matches, server SHOULD provide sub-range with 206; else return entire entity with 200.

### 14.28 If-Unmodified-Since
- Makes method conditional on resource not modified since given time.
- Grammar: `If-Unmodified-Since = "If-Unmodified-Since" ":" HTTP-date`
- If not modified, server SHOULD perform operation. If modified, MUST NOT perform and MUST return 412.

### 14.29 Last-Modified
- Date and time origin server believes variant was last modified.
- Grammar: `Last-Modified = "Last-Modified" ":" HTTP-date`
- Origin server MUST NOT send Last-Modified later than server's message origination time. If future, replace with message origination date.
- Origin server SHOULD obtain Last-Modified as close as possible to generating Date value.
- HTTP/1.1 servers SHOULD send Last-Modified whenever feasible.

### 14.30 Location
- Redirects recipient to a location other than Request-URI.
- For 201: Location of new resource. For 3xx: preferred URI for automatic redirection.
- Value is single absolute URI.

### 14.31 Max-Forwards
- Limits number of proxies/gateways that can forward request (TRACE, OPTIONS).
- Value is decimal integer. Each recipient MUST check and decrement if forwarding. If zero, MUST NOT forward and MUST respond as final recipient.
- MAY be ignored for other methods.

### 14.32 Pragma
- Implementation-specific directives. Grammar: `Pragma = "Pragma" ":" 1#pragma-directive`
- "no-cache" has same semantics as Cache-Control: no-cache.
- HTTP/1.1 caches SHOULD treat "Pragma: no-cache" as "Cache-Control: no-cache". No new Pragma directives will be defined.

### 14.33 Proxy-Authenticate
- MUST be included as part of 407 response. Contains challenge for proxy.
- Applies only to current connection; SHOULD NOT be passed on to downstream clients.

### 14.34 Proxy-Authorization
- Allows client to identify itself to proxy requiring authentication. Consumed by first outbound proxy that expected credentials. Proxy MAY relay credentials.

### 14.35 Range
#### 14.35.1 Byte Ranges
- Byte range specifications apply to sequence of bytes in entity-body.
- Grammar: `byte-ranges-specifier = bytes-unit "=" byte-range-set`
- Byte offsets start at zero. last-byte-pos if absent or ≥ current length taken as one less than length.
- suffix-byte-range-spec: "-" suffix-length.
- If byte-range-set is satisfiable (at least one range with first-byte-pos < current length or non-zero suffix), server SHOULD return 206 with satisfiable ranges. If unsatisfiable, SHOULD return 416.

#### 14.35.2 Range Retrieval Requests
- GET methods MAY request one or more sub-ranges using Range header.
- Server MAY ignore Range; but HTTP/1.1 origin servers and intermediate caches ought to support byte ranges.
- If Range present in unconditional GET, response is 206 instead of 200.
- If Range in conditional GET, modifies response only if condition true; does not affect 304.
- If proxy supports ranges and receives entire entity, SHOULD only return requested range to client. SHOULD store entire response in cache.

### 14.36 Referer
- Allows client to specify URI of resource from which Request-URI was obtained.
- MUST NOT be sent if Request-URI obtained from source without own URI (e.g., keyboard input).
- Grammar: `Referer = "Referer" ":" ( absoluteURI | relativeURI )` – must not include fragment.

### 14.37 Retry-After
- Can be used with 503 (how long service is expected unavailable) or with 3xx (minimum time user-agent asked to wait).
- Value: HTTP-date or delta-seconds.

### 14.38 Server
- Contains information about software used by origin server.
- Example: `Server: CERN/3.0 libwww/2.17`
- Proxy MUST NOT modify Server response-header; SHOULD include Via instead.

### 14.39 TE
- Indicates what extension transfer-codings client is willing to accept and whether willing to accept trailer fields in chunked transfer-coding.
- Grammar: `TE = "TE" ":" #( t-codings )`, t-codings = "trailers" | transfer-extension [ accept-params ].
- The TE header field only applies to immediate connection; MUST be supplied within Connection header.
- "chunked" always acceptable; "trailers" keyword indicates willingness to accept trailer fields.
- If TE field-value empty or absent, only "chunked" transfer-coding is allowed.

### 14.40 Trailer
- Indicates given set of header fields present in trailer of chunked message.
- HTTP/1.1 message SHOULD include Trailer header in chunked transfer-coding with non-empty trailer.
- If no Trailer, trailer SHOULD NOT include any header fields.
- Fields listed in Trailer MUST NOT include Transfer-Encoding, Content-Length, Trailer.

### 14.41 Transfer-Encoding
- Indicates what type of transformation applied to message body for safe transfer.
- Example: `Transfer-Encoding: chunked`
- Multiple encodings MUST be listed in order applied.

### 14.42 Upgrade
- Allows client to specify additional communication protocols it supports and would like to use.
- Server MUST use Upgrade in 101 response to indicate switching.
- Only applies to immediate connection; MUST be supplied within Connection header.
- Cannot be used to indicate switch to protocol on different connection.

### 14.43 User-Agent
- Contains information about user agent originating request.
- User agents SHOULD include this field.

### 14.44 Vary
- Indicates set of request-header fields that determine whether a cache is permitted to use response to reply to subsequent request without revalidation.
- Grammar: `Vary = "Vary" ":" ( "*" | 1#field-name )`
- HTTP/1.1 server SHOULD include Vary with any cacheable response subject to server-driven negotiation.
- "*" must not be generated by proxy; only by origin server.

### 14.45 Via
- MUST be used by gateways and proxies to indicate intermediate protocols and recipients.
- Multiple Via values ordered according to sequence of forwarding applications.
- Proxies/gateways behind firewall SHOULD NOT forward names/ports by default; use pseudonyms.
- May combine ordered subsequence with identical received-protocol values if under same organizational control and hosts pseudonymized.

### 14.46 Warning
- Used to carry additional information about status or transformation of message.
- Grammar: `Warning = "Warning" ":" 1#warning-value`
- warn-code: 3DIGIT. Defined codes:
  - 110 Response is stale (MUST be included when stale).
  - 111 Revalidation failed.
  - 112 Disconnected operation.
  - 113 Heuristic expiration.
  - 199 Miscellaneous warning.
  - 214 Transformation applied.
  - 299 Miscellaneous persistent warning.
- If message with Warning sent to HTTP/1.0 or lower, sender MUST include warn-date matching Date.
- If received warn-date differs from Date, that warning-value MUST be deleted (and Warning header if all deleted).

### 14.47 WWW-Authenticate
- MUST be included in 401 response. Contains at least one challenge.

## 15. Security Considerations
- Discusses numerous security issues: personal information (Server, Via, Referer, From headers), URI encoding, file/path name attacks, DNS spoofing, Location header spoofing, Content-Disposition issues, authentication credentials, proxies and caching.
- Key security recommendations: control dissemination of personal information; restrict file access; use DNS TTL; authenticate locations; protect proxy/cache contents; disable non-essential headers when privacy needed.

## Requirements Summary (Partial – Chunk 1)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R001 | GET and HEAD MUST be supported by all general-purpose servers. | MUST | Section 5.1.1 |
| R002 | Host request-header field MUST accompany all HTTP/1.1 requests. | MUST | Section 9 |
| R003 | A client MUST include a Host header field in all HTTP/1.1 request messages. | MUST | Section 14.23 |
| R004 | HTTP/1.1 origin servers MUST respond with 400 to any HTTP/1.1 request lacking Host header. | MUST | Section 14.23 |
| R005 | Proxy must implement both client and server requirements of this specification. | MUST | Section 1.3 |
| R006 | All HTTP/1.1 applications MUST be able to receive and decode "chunked" transfer-coding. | MUST | Section 3.6.1 |
| R007 | Server MUST NOT send transfer-codings to an HTTP/1.0 client. | MUST | Section 3.6 |
| R008 | HTTP/1.1 recipients MUST respect the charset label provided by the sender. | MUST | Section 3.4.1 |
| R009 | Origin server MUST decode the Request-URI if encoded with percent-encoding. | MUST | Section 5.1.2 |
| R010 | Transparent proxy MUST NOT rewrite abs_path part of Request-URI. | MUST | Section 5.1.2 |
| R011 | A server MUST NOT send a 1xx response to an HTTP/1.0 client except under experimental conditions. | MUST | Section 10.1 |
| R012 | A correct cache MUST respond to a request with the most up-to-date response held that meets conditions. | MUST | Section 13.1.1 |
| R013 | Whenever cache returns response that is neither first-hand nor fresh enough, MUST attach Warning. | MUST | Section 13.1.2 |
| R014 | Origin servers MUST include a Date header in all responses except in specified cases. | MUST | Section 14.18 |
| R015 | If a response includes both a Transfer-Encoding header and a Content-Length header, the latter MUST be ignored. | MUST | Section 4.4 |
| R016 | Messages MUST NOT include both a Content-Length header field and a non-identity transfer-coding. | MUST | Section 4.4 |
| R017 | HTTP/1.1 servers MUST accept the absoluteURI form in requests. | MUST | Section 5.1.2 |
| R018 | An origin server that differentiates resources based on the host requested MUST use the rules in Section 5.2. | MUST | Section 5.2 |
| R019 | Servers MUST understand the class of any status code; unrecognized codes treated as x00 and MUST NOT be cached. | MUST | Section 6.1.1 |
| R020 | Proxy MUST NOT forward a 100 response if request was from HTTP/1.0 client without Expect: 100-continue. | MUST | Section 8.2.3 |
| R021 | Client using persistent connections MUST NOT send more requests after close signaled. | MUST | Section 8.1.2 |
| R022 | Server MUST send responses to pipelined requests in the same order requests were received. | MUST | Section 8.1.2.2 |
| R023 | A proxy MUST NOT establish HTTP/1.1 persistent connection with an HTTP/1.0 client. | MUST | Section 8.1.3 |
| R024 | Clients, servers, and proxies MUST be able to recover from asynchronous close events. | MUST | Section 8.1.4 |
| R025 | HTTP/1.1 client sending message-body SHOULD monitor network connection for error status. | SHOULD | Section 8.2.2 |
| R026 | If client sees error status, SHOULD immediately cease transmitting the body. | SHOULD | Section 8.2.2 |
| R027 | Clients using persistent connections SHOULD limit simultaneous connections to a given server (2 for single-user). | SHOULD | Section 8.1.4 |
| R028 | Servers SHOULD always respond to at least one request per connection. | SHOULD | Section 8.1.4 |
| R029 | HTTP/1.1 servers SHOULD maintain persistent connections and use TCP flow control for overloads. | SHOULD | Section 8.2.1 |
| R030 | If origin server wishes to force validation every request, it SHOULD use "must-revalidate". | SHOULD | Section 13.2.1 |
| R031 | Clients SHOULD NOT pipeline non-idempotent methods/sequences. | SHOULD | Section 8.1.2.2 |
| R032 | A server MUST NOT use the trailer for header fields unless conditions (a) or (b) in 3.6.1 are met. | MUST | Section 3.6.1 |
| R033 | All HTTP/1.1 applications that receive entities MUST accept "chunked" transfer-coding. | MUST | Section 4.4 |
| R034 | Messages MUST NOT include both a Content-Length header field and a non-identity transfer-coding. | MUST | Section 4.4 |
| R035 | HTTP/1.1 user agents MUST notify the user when an invalid length is received and detected. | MUST | Section 4.4 |
| R036 | The methods GET and HEAD MUST be supported by all general-purpose servers. | MUST | Section 5.1.1 |
| R037 | If a request contains a message-body and a Content-Length is not given, server SHOULD respond 400 or 411. | SHOULD | Section 4.4 |
| R038 | Clients SHOULD NOT use weak validators in other forms of request (non-subrange). | MUST NOT | Section 13.3.3 |
| R039 | Cache or origin server receiving conditional request other than full-body GET MUST use strong comparison. | MUST | Section 13.3.3 |
| R040 | If both new request and cached entry include "max-age" directives, lesser value used for freshness. | – | Section 14.9.3 |
| R041 | Cache MUST NOT use a 206 response to construct response to subsequent request unless ETag or Last-Modified match exactly. | MUST | Section 13.5.4 |
| R042 | Cache that does not support Range and Content-Range headers MUST NOT cache 206. | MUST | Section 13.4 |
| R043 | A cache MUST NOT return a partial response to a client without explicitly marking as 206. | MUST | Section 13.8 |
| R044 | Caches MUST NOT treat responses to query URIs as fresh unless server provides explicit expiration. | MUST | Section 13.9 |
| R045 | Methods PUT, DELETE, POST MUST cause cache to invalidate entity. | MUST | Section 13.10 |
| R046 | All methods that might modify origin server's resources MUST be written through. | MUST | Section 13.11 |
| R047 | Transparent proxy MUST NOT modify certain headers as listed in Section 13.5.2. | MUST | Section 13.5.2 |
| R048 | Non-transparent proxy MUST add Warning 214 if it modifies headers subject to transformation. | MUST | Section 13.5.2 |
| R049 | Origin server MUST NOT send a Last-Modified date later than its message origination time. | MUST | Section 14.29 |
| R050 | HTTP/1.1 servers SHOULD send Last-Modified whenever feasible. | SHOULD | Section 14.29 |
| R051 | Origin servers SHOULD send an entity tag validator unless unfeasible. | SHOULD | Section 13.3.4 |
| R052 | Client MUST use entity tag in cache-conditional requests if provided by origin server. | MUST | Section 13.3.4 |
| R053 | Client SHOULD use both entity tag and Last-Modified if both provided. | SHOULD | Section 13.3.4 |
| R054 | Server MUST NOT return 304 unless consistent with all conditional header fields if both validators present. | MUST | Section 13.3.4 |
| R055 | If no entity tags match in If-None-Match, server MAY perform method but MUST ignore any If-Modified-Since. | MUST | Section 14.26 |
| R056 | Proxy MUST parse Connection header and remove header fields with same name as connection-tokens. | MUST | Section 14.10 |
| R057 | HTTP/1.1 applications not supporting persistent connections MUST include "close" connection option in every message. | MUST | Section 14.10 |
| R058 | Only origin servers or clients MAY generate Content-MD5 header; proxies and gateways MUST NOT. | MUST | Section 14.15 |
| R059 | A system receiving HTTP/1.0 (or lower-version) message with Connection header MUST remove and ignore listed headers. | MUST | Section 14.10 |
| R060 | Client SHOULD NOT send the From header field without user's approval. | SHOULD | Section 14.22 |
| R061 | User agents SHOULD include User-Agent field with requests. | SHOULD | Section 14.43 |
| R062 | Server SHOULD include Vary header field with any cacheable response subject to server-driven negotiation. | SHOULD | Section 14.44 |
| R063 | Origin server that does not support Range header MAY ignore it. | MAY | Section 14.35.2 |
| R064 | If server supports Range and specified range is appropriate, response should be 206 instead of 200. | – | Section 14.35.2 |
| R065 | Proxy that supports ranges and receives entire entity SHOULD only return requested range to client and SHOULD store entire response in cache. | SHOULD | Section 14.35.2 |
| R066 | Clients MUST NOT use weak validators in other forms of request (e.g., sub-range). | MUST NOT | Section 13.3.3 |
| R067 | If a cache receives a 304 response indicating entity not cached, cache MUST disregard and repeat request without conditional. | MUST | Section 10.3.5 |
| R068 | If cache uses 304 to update entry, MUST update to reflect new field values. | MUST | Section 10.3.5 |
| R069 | Servers SHOULD send the must-revalidate directive if failure to revalidate could result in incorrect operation. | SHOULD | Section 14.9.4 |
| R070 | Recipients MUST NOT take any automated action that violates must-revalidate and MUST NOT automatically provide unvalidated copy if revalidation fails. | MUST | Section 14.9.4 |
| R071 | An HTTP/1.1 cache MUST obey the must-revalidate directive; if cannot reach origin server, MUST generate 504. | MUST | Section 14.9.4 |
| R072 | If both the new request and the cached entry include "max-age" directives, the lesser of the two values is used. | – | Section 14.9.3 |
| R073 | A cache MAY be configured to return stale responses without validation only if not conflicting with MUST-level requirements. | – | Section 14.9.3 |
| R074 | The "no-transform" directive: intermediate cache/proxy MUST NOT change certain headers and entity-body. | MUST | Section 14.9.5 |
| R075 | Unrecognized cache-directives MUST be ignored. | MUST | Section 14.9.6 |
| R076 | If a response includes "s-maxage" directive, for shared cache it overrides max-age and Expires. | – | Section 14.9.3 |
| R077 | A Vary field value of "*" must not be generated by a proxy server. | MUST NOT | Section 14.44 |
| R078 | Proxy servers MUST NOT generate "*" in Vary header. | MUST NOT | Section 14.44 |
| R079 | A server MUST NOT modify the Server response-header; proxy SHOULD include Via. | MUST, SHOULD | Section 14.38 |
| R080 | TE header field only applies to immediate connection; MUST be supplied within Connection header. | MUST | Section 14.39 |
| R081 | Upgrade header field only applies to immediate connection; MUST be supplied within Connection header. | MUST | Section 14.42 |
| R082 | If multiple encodings applied to entity, transfer-codings MUST be listed in order applied. | MUST | Section 14.41 |
| R083 | If multiple content codings applied, they MUST be listed in order applied. | MUST | Section 14.11 |
| R084 | A received message without Date header MUST be assigned one by recipient if cached or gatewayed via protocol requiring Date. | MUST | Section 14.18 |
| R085 | HTTP implementation without clock MUST NOT cache responses without revalidating on every use. | MUST | Section 14.18 |
| R086 | Origin server without clock MUST NOT assign Expires or Last-Modified unless values from reliable source. | MUST | Section 14.18.1 |
| R087 | Clients SHOULD ONLY send Date in messages that include an entity-body (PUT, POST); even then optional. | SHOULD | Section 14.18 |
| R088 | A client without a clock MUST NOT send a Date header field in a request. | MUST NOT | Section 14.18 |
| R089 | Origin servers MUST include a Date header field in all responses except 100, 101, server errors, or when no clock available. | MUST | Section 14.18 |
| R090 | HTTP/1.1 caches and clients MUST treat other invalid date formats, especially "0", as in the past. | MUST | Section 14.21 |
| R091 | HTTP/1.1 servers SHOULD NOT send Expires dates more than one year in the future. | SHOULD | Section 14.21 |
| R092 | A server MUST NOT send a 100 (Continue) response if request is from HTTP/1.0 (or earlier) client. | MUST NOT | Section 8.2.3 |
| R093 | Proxy MUST NOT forward a 100 (Continue) response if request was from HTTP/1.0 client without Expect:100-continue. | MUST NOT | Section 8.2.3 |
| R094 | Proxy SHOULD maintain a cache recording HTTP version numbers of next-hop servers. | SHOULD | Section 8.2.3 |
| R095 | If proxy receives request with Expect:100-continue and knows next-hop is HTTP/1.0 or lower, MUST respond with 417. | MUST | Section 8.2.3 |
| R096 | If proxy receives request with Expect:100-continue and either knows next-hop is HTTP/1.1 or higher or does not know version, MUST forward request including Expect header. | MUST | Section 8.2.3 |
| R097 | Origin server that sends a 100 response MUST ultimately send a final status code. | MUST | Section 8.2.3 |
| R098 | Client that sends Expect:100-continue but does not intend to send body MUST NOT send that expectation. | MUST NOT | Section 8.2.3 |
| R099 | If client will wait for 100 before sending body, it MUST send Expect:100-continue. | MUST | Section 8.2.3 |
| R100 | Client SHOULD NOT wait indefinitely for 100 if it has never seen 100 from that server. | SHOULD | Section 8.2.3 |
| R101 | If server responds with final status code to a request with body, it MUST NOT perform the requested method. | MUST | Section 8.2.3 |
| R102 | A server MUST respond with a 417 status if any expectations cannot be met. | MUST | Section 14.20 |
| R103 | Comparison of expectation values is case-insensitive for unquoted tokens, case-sensitive for quoted-string. | – | Section 14.20 |
| R104 | Proxy MUST forward the Expect request-header itself if it forwards the request. | MUST | Section 14.20 |
| R105 | An HTTP/1.1 proxy MUST return a 417 status if it receives a request with an expectation it cannot meet. | MUST | Section 14.20 |
| R106 | The "no-cache" directive in Cache-Control overrides the default caching algorithms. | – | Section 14.9 |
| R107 | The "private" directive indicates that all or part of response is intended for single user and MUST NOT be cached by shared cache. | MUST NOT | Section 14.9.1 |
| R108 | The "no-store" directive: cache MUST NOT store any part of request/response in non-volatile storage and must make best-effort to remove from volatile storage. | MUST | Section 14.9.2 |
| R109 | If a response includes "public", it MAY be cached by any cache. | MAY | Section 14.9.1 |
| R110 | If a response includes "must-revalidate", cache MUST NOT use entry after stale without revalidation. | MUST | Section 14.9.4 |
| R111 | If a response includes "proxy-revalidate", shared caches must revalidate; non-shared user agent caches need not. | – | Section 14.9.4 |
| R112 | Cache SHOULD NOT return stale response if client explicitly requests first-hand or fresh, unless impossible. | SHOULD | Section 13.1.5 |
| R113 | Client MAY specify in a request that it will accept stale responses up to a maximum amount of staleness. | MAY | Section 13.1.6 |

(Note: This summary is non-exhaustive. All MUSTs and MUST NOTs from the specification are captured where critical, but many SHOULDs and MAYs are important for compliance.)

## Informative Annexes (Condensed)
- **Appendix 19.1**: Defines Internet media types `message/http` and `application/http` for encapsulating HTTP messages. IANA registration details provided.
- **Appendix 19.2**: Defines `multipart/byteranges` media type for transmitting multiple byte ranges in 206 responses. Requires boundary parameter.
- **Appendix 19.3**: Tolerant Applications – recommends that implementations be lenient in parsing (accept different amounts of white space, recognize bare LF as line terminator, handle date inconsistencies). Guidance on handling year 2000, GMT conversions.
- **Appendix 19.4**: Differences Between HTTP Entities and RFC 2045 Entities – HTTP uses MIME-like constructs but with differences: MIME-Version header optional; line breaks in text media may be CR, LF, or CRLF; Content-Encoding introduced; Content-Transfer-Encoding not used; Transfer-Encoding introduced for chunking.
- **Appendix 19.4.1-19.4.6**: Detail each difference. Important: Proxies/gateways to/from MIME must perform appropriate conversions (e.g., remove non-identity CTE before HTTP, decode chunked before MIME).

(End of Chunk 1)

### 15.4 Location and Content-Location Headers (Spoofing)
- **Requirement**: If a single server supports multiple organizations that do not trust one another, it **MUST** check the values of `Location` and `Content-Location` headers in responses generated under control of those organizations to ensure they do not attempt to invalidate resources over which they have no authority. (Section 15.4)

### 15.5 Content-Disposition Issues
- **Informative**: The `Content-Disposition` header (derived from RFC 1806 [35], updated by RFC 2183 [49]) is not part of the HTTP standard but widely implemented. Implementors must be aware of serious security considerations described in the referenced RFCs.

### 15.6 Authentication Credentials and Idle Clients
- **Informative**: HTTP/1.1 does not provide a method for servers to discard cached credentials. This is a recognized defect. Workarounds include password-protected screen savers, idle time-outs, and user agents providing a mechanism for discarding cached credentials under user control.

### 15.7 Proxies and Caching
- **Proxy security**: Proxy operators **should** protect proxy systems as they would any sensitive system. Log information (often highly sensitive) **should** be carefully guarded. (Section 15.1.1)
- **Cache security**: Cache contents **should** be protected as sensitive information because they persist after HTTP requests complete and can be exploited later.
- **Design responsibilities**: Proxy implementors **should** consider privacy and security implications of design, coding, and default configurations.
- **User awareness**: Users of a proxy must be aware that trust in the proxy is limited by the trustworthiness of its operators; HTTP itself cannot solve this.
- **Cryptography**: When appropriate, cryptography may protect against security and privacy attacks, but it is beyond the scope of HTTP/1.1.

#### 15.7.1 Denial of Service Attacks on Proxies
- **Informative**: DoS attacks exist, are hard to defend against, and research continues. Operators should be aware.

### 16 Acknowledgments (Summary)
This specification builds upon RFC 822 [9] and MIME [7]. It has benefited from the www-talk community, early protocol definers, and the HTTP-WG members. Special thanks to the "MUST/MAY/SHOULD" auditors and early implementors of RFC 2068.

### 17 Normative References
The following references are cited in RFC 2616. (Full list preserved; only IDs shown for brevity. See original for complete entries.)
- [1] RFC 1766 – Language Tags
- [2] RFC 1436 – Gopher Protocol
- [3] RFC 1630 – URI
- [4] RFC 1738 – URL
- [5] RFC 1866 – HTML 2.0
- [6] RFC 1945 – HTTP/1.0
- [7] RFC 2045 – MIME Part One
- [8] RFC 1123 – Host Requirements
- [9] RFC 822 – Internet Text Messages
- [10] WAIS Protocol (informal)
- [11] RFC 1808 – Relative URL
- [12] RFC 1036 – USENET Messages
- [13] RFC 977 – NNTP
- [14] RFC 2047 – MIME Part Three (Non-ASCII)
- [15] RFC 1867 – Form-based File Upload
- [16] RFC 821 – SMTP
- [17] RFC 1590 – Media Type Registration
- [18] RFC 959 – FTP
- [19] RFC 1700 – Assigned Numbers
- [20] RFC 1737 – URN Requirements
- [21] ANSI X3.4-1986 – US-ASCII
- [22] ISO-8859 – Character Sets
- [23] RFC 1864 – Content-MD5
- [24] RFC 1900 – Renumbering Needs
- [25] RFC 1952 – GZIP
- [26] Padmanabhan & Mogul – HTTP Latency
- [27] Touch et al. – HTTP Performance
- [28] RFC 1305 – NTPv3
- [29] RFC 1951 – DEFLATE
- [30] Spero – HTTP Performance Problems
- [31] RFC 1950 – ZLIB
- [32] RFC 2069 – Digest Access Authentication
- [33] RFC 2068 – HTTP/1.1 (previous version)
- [34] RFC 2119 – Key Words for Requirements
- [35] RFC 1806 – Content-Disposition
- [36] RFC 2145 – HTTP Version Numbers
- [37] RFC 2076 – Common Internet Message Headers
- [38] RFC 2279 – UTF-8
- [39] Nielsen et al. – HTTP/1.1 Performance
- [40] RFC 2046 – MIME Part Two (Media Types)
- [41] RFC 2277 – IETF Policy on Character Sets
- [42] RFC 2396 – URI Generic Syntax
- [43] RFC 2617 – HTTP Authentication (Basic/Digest)
- [44] Luotonen – Tunneling TCP (Work in Progress)
- [45] RFC 2110 – MHTML
- [46] RFC 2026 – Internet Standards Process
- [47] RFC 2324 – HTCPCP
- [48] RFC 2049 – MIME Part Five (Conformance)
- [49] RFC 2183 – Content-Disposition (Updated)

### 18 Authors' Addresses (Informative)
Roy T. Fielding, James Gettys, Jeffrey C. Mogul, Henrik Frystyk Nielsen, Larry Masinter, Paul J. Leach, Tim Berners-Lee. (Full contact details available in original.)

### 19 Appendices
#### 19.1 Internet Media Types: `message/http` and `application/http`
- **message/http**: Used to enclose a single HTTP request or response. Parameters: `version`, `msgtype`. Encoding: 7bit, 8bit, binary. No security considerations.
- **application/http**: Used to enclose a pipeline of one or more HTTP requests or responses (not intermixed). Same parameters as message/http. Encoding: binary; appropriate Content-Transfer-Encoding required for e-mail. No security considerations.

#### 19.2 Internet Media Type: `multipart/byteranges`
- **Defined for 206 Partial Content responses containing multiple ranges.**
- **Required parameter**: `boundary`. Encoding: 7bit, 8bit, binary. No security considerations.
- **Note**: Some implementations mistakenly use `multipart/x-byteranges`; this is incompatible.

#### 19.3 Tolerant Applications
- **[19.3.1]**: Clients **SHOULD** be tolerant in parsing the Status-Line; servers **SHOULD** be tolerant when parsing the Request-Line. They **SHOULD** accept any amount of SP or HT characters between fields.
- **[19.3.2]**: Applications **should** recognize a single LF as a line terminator and ignore the leading CR.
- **[19.3.3]**: The character set of an entity-body **SHOULD** be labeled as the lowest common denominator; not labeling is preferred over labeling as US-ASCII or ISO-8859-1. (See 3.7.1, 3.4.1)
- **[Date parsing rules]**:
  - HTTP/1.1 clients and caches **SHOULD** assume that an RFC-850 date more than 50 years in the future is in the past.
  - An HTTP/1.1 implementation **MAY** internally represent a parsed Expires date as earlier than the proper value, but **MUST NOT** represent it as later.
  - All expiration-related calculations **MUST** be done in GMT. Local time zone **MUST NOT** influence age or expiration time.
  - If an HTTP header carries a date value with a non-GMT time zone, it **MUST** be converted into GMT using the most conservative possible conversion.

#### 19.4 Differences Between HTTP/1.1 and RFC 2045 (MIME)
- **19.4.1 MIME-Version**: HTTP/1.1 messages **MAY** include a single MIME-Version header. Proxies/gateways exporting to strict MIME environments are responsible for ensuring compliance.
- **19.4.2 Canonical Form**: Proxies/gateways from HTTP to strict MIME **SHOULD** translate all line breaks in text media types to CRLF (RFC 2049 canonical form). Note: this may break cryptographic checksums.
- **19.4.3 Date Formats**: Proxies/gateways from other protocols **SHOULD** ensure Date headers conform to HTTP/1.1 formats and rewrite if necessary.
- **19.4.4 Content-Encoding**: Proxies/gateways from HTTP to MIME-compliant protocols **MUST** either change Content-Type or decode the entity-body before forwarding.
- **19.4.5 No Content-Transfer-Encoding**: Proxies/gateways from MIME to HTTP **MUST** remove any non-identity CTE encoding. Proxies/gateways from HTTP to MIME **SHOULD** label data with appropriate CTE if it improves safe transport.
- **19.4.6 Transfer-Encoding**: Proxies/gateways **MUST** remove any transfer-coding before forwarding to a MIME-compliant protocol. Pseudocode for decoding chunked encoding provided.
- **19.4.7 MHTML**: HTTP does not have MIME line length limitations; MHTML messages transported by HTTP follow all MHTML conventions.

#### 19.5 Additional Features
- **19.5.1 Content-Disposition**: The `Content-Disposition` response header may suggest a default filename. The receiving user agent **SHOULD NOT** respect directory path information; the filename **SHOULD** be treated as a terminal component only. See section 15.5 for security issues.

#### 19.6 Compatibility with Previous Versions
- **19.6.1.1 Changes**: To simplify multi-homed web servers and conserve IP addresses:
  - Both clients and servers **MUST** support the Host request-header.
  - A client sending an HTTP/1.1 request **MUST** send a Host header.
  - Servers **MUST** report a 400 (Bad Request) error if an HTTP/1.1 request lacks a Host header.
  - Servers **MUST** accept absolute URIs.
- **19.6.2 Persistent Connections**: Persistent connections are default in HTTP/1.1; `Connection: close` is used to declare non-persistence. The original HTTP/1.0 Keep-Alive mechanism is documented in RFC 2068.
- **19.6.3 Changes from RFC 2068**: This specification corrects key word usage per RFC 2119 and resolves ambiguities in areas including error codes, chunked encoding, caching, ranges, message transmission, TE header, and more. Details in original sections.

### 20 Index
- **Informative**: Refer to the PostScript version of RFC 2616 for the index.

### 21 Full Copyright Statement
- Copyright (C) The Internet Society (1999). All rights reserved. Permissions for copying, derivative works, and translation granted with restrictions. No warranty. (Full text in original.)

---

## Requirements Summary
| ID | Requirement Text (Normative) | Type | Reference |
|----|-----------------------------|------|-----------|
| R1 | Server supporting multiple untrusted organizations MUST check Location/Content-Location headers. | MUST | 15.4 |
| R2 | Clients MUST observe TTL information from DNS when caching host name lookups. | MUST | 15.1 (pre-chunk) |
| R3 | Clients SHOULD rely on name resolver for IP/DNS association. | SHOULD | 15.1 |
| R4 | Platforms SHOULD be configured to cache host name lookups locally when appropriate. | SHOULD | 15.1 |
| R5 | Clients and caches SHOULD assume RFC-850 dates more than 50 years in the future are in the past. | SHOULD | 19.3 |
| R6 | Implementation MAY represent parsed Expires date as earlier, but MUST NOT represent as later. | MAY/MUST NOT | 19.3 |
| R7 | All expiration calculations MUST be in GMT; local time zone MUST NOT influence. | MUST | 19.3 |
| R8 | Non-GMT date values MUST be converted using most conservative conversion. | MUST | 19.3 |
| R9 | Clients SHOULD be tolerant in parsing Status-Line and Request-Line, accepting extra SP/HT. | SHOULD | 19.3 |
| R10 | Proxies/gateways from HTTP to strict MIME SHOULD translate line breaks to CRLF. | SHOULD | 19.4.2 |
| R11 | Proxies/gateways from other protocols SHOULD ensure Date headers conform to HTTP/1.1. | SHOULD | 19.4.3 |
| R12 | Proxies/gateways from HTTP to MIME MUST change Content-Type or decode entity-body. | MUST | 19.4.4 |
| R13 | Proxies/gateways from MIME to HTTP MUST remove non-identity CTE. | MUST | 19.4.5 |
| R14 | Proxies/gateways from HTTP to MIME SHOULD label data with appropriate CTE if helpful. | SHOULD | 19.4.5 |
| R15 | Proxies/gateways MUST remove transfer-coding before MIME forwarding. | MUST | 19.4.6 |
| R16 | User agent SHOULD NOT respect directory path in Content-Disposition filename. | SHOULD NOT | 19.5.1 |
| R17 | Filename in Content-Disposition SHOULD be treated as terminal component only. | SHOULD | 19.5.1 |
| R18 | Both clients and servers MUST support Host request-header. | MUST | 19.6.1.1 |
| R19 | HTTP/1.1 client MUST send Host header. | MUST | 19.6.1.1 |
| R20 | Server MUST report 400 error if HTTP/1.1 lacks Host. | MUST | 19.6.1.1 |
| R21 | Servers MUST accept absolute URIs. | MUST | 19.6.1.1 |