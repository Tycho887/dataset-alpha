# RFC 9110: HTTP Semantics
**Source**: IETF (Internet Engineering Task Force) | **Version**: STD 97 | **Date**: June 2022 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc9110

## Scope (Summary)
Defines the overall architecture of HTTP, common terminology, core protocol elements, extensibility mechanisms, and the "http" and "https" URI schemes. Obsoletes RFCs 2818, 7230-7233, 7235, 7538, 7615, 7694 and portions of 7230; updates RFC 3864.

## Normative References
- [RFC2119] Key words for use in RFCs to Indicate Requirement Levels
- [RFC5234] Augmented BNF for Syntax Specifications: ABNF
- [RFC7405] Case-Sensitive String Support in ABNF
- [RFC8174] Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [RFC6365] Terminology Used in Internationalization in the IETF
- [RFC5646] Tags for Identifying Languages
- [RFC4647] Matching of Language Tags
- [RFC6125] Representation and Verification of Domain-Based Application Service Identity
- [RFC5280] Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile
- [RFC3986] Uniform Resource Identifier (URI): Generic Syntax (adopted as [URI])
- [RFC2046] Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types
- [RFC5322] Internet Message Format
- [RFC1950] ZLIB Compressed Data Format Specification
- [RFC1951] DEFLATE Compressed Data Format Specification
- [RFC1952] GZIP file format specification
- [RFC5905] Network Time Protocol Version 4
- [RFC2557] MIME Encapsulation of Aggregate Documents
- [RFC7616] HTTP Digest Access Authentication
- [RFC7617] The 'Basic' HTTP Authentication Scheme
- [RFC5789] PATCH Method for HTTP
- [RFC8288] Web Linking
- [RFC8615] Well-Known Uniform Resource Identifiers (URIs)
- [RFC8941] Structured Field Values for HTTP
- [TLS13] The Transport Layer Security (TLS) Protocol Version 1.3
- [HTTP/1.1] RFC 9112 (separate document)
- [HTTP/2] RFC 9113
- [HTTP/3] RFC 9114
- [CACHING] RFC 9111 (HTTP Caching)

## Definitions and Abbreviations
- **resource**: The target of an HTTP request (Section 3.1)
- **representation**: Information reflecting a past, current, or desired state of a resource (Section 3.2)
- **connection**: A reliable transport- or session-layer connection (Section 3.3)
- **client**: A program that establishes a connection to send HTTP requests (Section 3.3)
- **server**: A program that accepts connections to service HTTP requests (Section 3.3)
- **user agent**: Any client program that initiates a request (Section 3.5)
- **origin server**: A program that can originate authoritative responses for a target resource (Section 3.6)
- **proxy**: A message-forwarding agent chosen by the client (Section 3.7)
- **gateway**: An intermediary that acts as an origin server for the outbound connection (Section 3.7)
- **tunnel**: A blind relay between two connections (Section 3.7)
- **cache**: A local store of previous response messages (Section 3.8)
- **field**: Name/value pairs sent in header or trailer sections (Section 5)
- **field name**: Case-insensitive token (Section 5.1)
- **field value**: Combined value of field lines (Section 5.2)
- **content**: Octet stream after message framing (Section 6.4)
- **target URI**: Absolute URI after resolving the URI reference (Section 7.1)
- **selected representation**: The representation chosen by content negotiation (Section 3.2)
- **validator**: Representation metadata used for conditional requests (Section 8.8)
- **strong validator**: Changes value whenever a change occurs to representation data observable in 200 response (Section 8.8.1)
- **weak validator**: Might not change for every change (Section 8.8.1)
- **safe method**: Read-only semantics (Section 9.2.1)
- **idempotent method**: Multiple identical requests have same intended effect (Section 9.2.2)
- **proactive negotiation**: Server selects representation based on client preferences (Section 12.1)
- **reactive negotiation**: Client selects after receiving list (Section 12.2)
- **conditional request**: Request with one or more preconditions (Section 13)
- **range request**: Request for only part(s) of the selected representation (Section 14)

## 1. Introduction
### 1.1 Purpose
HTTP is a stateless, application-level, request/response protocol for distributed hypertext information systems. It hides service implementation details via a uniform interface.

### 1.2 History and Evolution
HTTP evolved from HTTP/0.9 and HTTP/1.0 to HTTP/1.1 (RFCs 7230-7235), HTTP/2, and HTTP/3. This revision separates semantics (this document) and caching (RFC 9111) from messaging syntax.

### 1.3 Core Semantics
HTTP messages are requests or responses. Semantics include methods, status codes, header fields, and content negotiation.

### 1.4 Specifications Obsoleted by This Document
Refer to Table 1 (omitted here for brevity). Details in Appendix B.

## 2. Conformance
### 2.1 Syntax Notation
Uses ABNF per RFC 5234 extended with RFC 7405. List extension defined in Section 5.6.1.

### 2.2 Requirements Notation
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as per BCP 14 [RFC2119][RFC8174] when in all capitals.
- A sender MUST NOT generate protocol elements not matching ABNF grammar.
- Conformance requires adherence to both messaging syntax and semantics.
- A recipient MAY employ workarounds for non-conformant implementations.

### 2.3 Length Requirements
A recipient SHOULD parse defensively. At a minimum, a recipient MUST be able to parse lengths at least as long as it generates for the same elements.

### 2.4 Error Handling
A recipient MUST interpret elements according to defined semantics unless determined that sender incorrectly implements them. Unless noted, a recipient MAY attempt to recover from invalid constructs.

### 2.5 Protocol Version
Version numbers: major.minor. Major indicates messaging syntax; minor indicates highest conformant minor. Increment major for incompatible message syntax, minor for added capabilities. Minor version "0" implied when no minor defined.

## 3. Terminology and Core Concepts
### 3.1 Resources
Target of an HTTP request. Identified by URI. Request semantics separate from identification.

### 3.2 Representations
Information reflecting resource state, consisting of metadata and data. Used for conditional requests and response content.

### 3.3 Connections, Clients, and Servers
- Client establishes connection to send requests.
- Server accepts connections to send responses.
- A server MUST NOT assume two requests on same connection are from same user agent unless connection secured and specific.

### 3.4 Messages
Request/response messages: method, target, header fields, content, trailer fields. Responses include status code.

### 3.5 User Agents
Client programs (browsers, spiders, etc.). Reporting errors can be via logs. Confirmation may be advance configuration.

### 3.6 Origin Server
Program that can originate authoritative responses.

### 3.7 Intermediaries
- Proxy: chosen by client to forward requests.
- Gateway: acts as origin server outbound, translates inbound.
- Tunnel: blind relay.
- Interception proxy: not chosen by client.
An intermediary not acting as a tunnel MUST implement Connection header. MUST NOT forward to itself unless protected from infinite loops.

### 3.8 Caches
Local store of previous responses. Any client or server MAY employ a cache. A cache cannot be used while acting as a tunnel.

### 3.9 Example Message Exchange
(GET request example omitted in summary.)

## 4. Identifiers in HTTP
### 4.1 URI References
ABNF productions from RFC 3986. It is RECOMMENDED to support URIs of at least 8000 octets.

### 4.2 HTTP-Related URI Schemes
#### 4.2.1 http URI Scheme
`http-URI = "http" "://" authority path-abempty [ "?" query ]`
Default port 80. A sender MUST NOT generate an empty host identifier; recipient MUST reject such.

#### 4.2.2 https URI Scheme
`https-URI = "https" "://" authority path-abempty [ "?" query ]`
Default port 443. A sender MUST NOT generate an empty host identifier; recipient MUST reject such. A client MUST ensure HTTP requests for "https" resources are secured prior to communication and only accept secured responses.

#### 4.2.3 http(s) Normalization and Comparison
Normalization per URI scheme rules. Equivalent URIs can be assumed to identify same resource. Distinct resources SHOULD NOT be identified by equivalent URIs.

#### 4.2.4 Deprecation of userinfo in http(s) URIs
A sender MUST NOT generate userinfo subcomponent in http/https URI references within messages. Recipients SHOULD parse for userinfo and treat presence as error.

#### 4.2.5 http(s) References with Fragment Identifiers
Fragment identifiers are not part of scheme definition; use ABNF rules to distinguish.

### 4.3 Authoritative Access
#### 4.3.1 URI Origin
Triple: scheme, host, port (normalized). Two origins are distinct if they differ in scheme, host, or port.

#### 4.3.2 http Origins
Client MAY attempt access by resolving host, establishing TCP connection to indicated port, and sending HTTP request. Non-interim response is authoritative.

#### 4.3.3 https Origins
Authority based on server's private key and trust chain. Client attributes authority if connection secured and host matches certificate. Request target's host and port pass within each request.

#### 4.3.4 https Certificate Verification
Client MUST verify service identity per RFC 6125. Construct reference identity: IP-ID for IP addresses, DNS-ID for names. CN-ID MUST NOT be used by clients. If certificate invalid for target origin, user agent MUST obtain user confirmation or terminate with bad certificate error. Automated clients MUST log error and SHOULD terminate; MAY have configuration to disable check but MUST have setting to enable.

#### 4.3.5 IP-ID Reference Identity
IP-ID matches if address identical to iPAddress in certificate subjectAltName.

## 5. Fields
### 5.1 Field Names
Case-insensitive tokens. New fields can be introduced without changing protocol version if safely ignorable. A proxy MUST forward unrecognized header fields unless they are in Connection or specifically blocked. Other recipients SHOULD ignore unrecognized fields.

### 5.2 Field Lines and Combined Field Value
When field name repeated, combined value is comma-separated list of field line values in order.

### 5.3 Field Order
A proxy MUST NOT change order of field lines with same name. A sender MUST NOT generate multiple field lines with same name unless field definition allows comma-separated list. (Exception: Set-Cookie.) A server MUST NOT apply a request to target resource until entire request header section received.

### 5.4 Field Limits
No predefined limit. Server receiving larger than it wishes to process MUST respond with appropriate 4xx status. Client MAY discard or truncate if safely ignorable.

### 5.5 Field Values
Grammar: field-value = *field-content. No leading/trailing whitespace. Field values containing CR, LF, or NUL are invalid; recipient MUST reject or replace with SP. Fields that anticipate single member are singleton; multiple members are list-based.

### 5.6 Common Rules for Defining Field Values
#### 5.6.1 Lists (#rule ABNF Extension)
`<n>#<m>element` for comma-delimited lists. Sender MUST NOT generate empty elements. Recipient MUST parse and ignore a reasonable number of empty elements.

#### 5.6.2 Tokens
`token = 1*tchar` where tchar excludes delimiters.

#### 5.6.3 Whitespace
OWS, RWS, BWS defined. Sender SHOULD generate OWS as single SP. Sender MUST NOT generate BWS. Recipient MUST parse and remove BWS.

#### 5.6.4 Quoted Strings
`quoted-string = DQUOTE *(qdtext / quoted-pair) DQUOTE`. Sender SHOULD NOT generate quoted-pair except where necessary.

#### 5.6.5 Comments
Only allowed in fields containing "comment". `comment = "(" *(ctext / quoted-pair / comment) ")"`.

#### 5.6.6 Parameters
`semicolon-delimited name=value pairs`. Parameter names case-insensitive; values case-sensitivity depends on name.

#### 5.6.7 Date/Time Formats
Preferred: IMF-fixdate (`Sun, 06 Nov 1994 08:49:37 GMT`). Obsolete: rfc850-date and asctime-date. Recipient MUST accept all three. Sender MUST generate IMF-fixdate. Clock should use NTP.

## 6. Message Abstraction
### 6.1 Framing and Completeness
Each HTTP version defines its own framing. A message is complete when all octets indicated by framing are available.

### 6.2 Control Data
Request: method, target, version. Response: status code, optional reason, version. Client SHOULD send highest version conformant; MUST NOT send version not conformant. Server SHOULD send highest version conformant with major version ≤ request; MUST NOT send non-conformant version. Recipient receiving higher minor version SHOULD process as highest minor it conforms to.

### 6.3 Header Fields
Fields sent before content.

### 6.4 Content
Stream of octets after framing. Content semantics defined by method and status code.
- Responses to HEAD, 1xx, 204, 304 do not include content.
- 2xx CONNECT switches to tunnel.

### 6.4.1 Content Semantics
Defined in Section 6.4.1 (various cases).

### 6.4.2 Identifying Content
Rules for identifying which resource the content represents (e.g., for GET 200, content is representation of target resource; for Content-Location matching target URI, etc.).

### 6.5 Trailer Fields
Fields sent after content. A sender MUST NOT generate trailer field unless header field name's definition permits it. A recipient MUST NOT merge trailer fields into headers unless definition allows. Server SHOULD NOT generate necessary trailer fields. The "Trailer" header field can indicate expected trailer fields.

### 6.6 Message Metadata
#### 6.6.1 Date
Origin server with clock MUST generate Date in 2xx, 3xx, 4xx responses; MAY in 1xx, 5xx. Without clock MUST NOT generate Date. Recipient without Date MUST record received time and add Date if cached or forwarded. User agent MAY send Date in request.

#### 6.6.2 Trailer
Lists field names anticipated in trailers.

## 7. Routing HTTP Messages
### 7.1 Determining the Target Resource
Target URI derived from URI reference. Request target components sent in control data and Host header. Unusual forms for CONNECT (host:port) and OPTIONS ("*").

### 7.2 Host and :authority
User agent MUST generate Host unless using :authority pseudo-header. SHOULD send Host as first field.

### 7.3 Routing Inbound Requests
Check cache, then proxy, then origin.

### 7.4 Rejecting Misdirected Requests
Origin server MUST reject request if scheme-specific requirements not met (e.g., https request must be over secured connection with valid certificate). Use 421 (Misdirected Request).

### 7.5 Response Correlation
Messages may be correlated implicitly or explicitly. Client receiving response while still sending request SHOULD continue unless told otherwise.

### 7.6 Message Forwarding
Intermediary not acting as tunnel MUST implement Connection header. MUST NOT forward message to itself unless protected from loops. MUST forward unrecognized elements.

#### 7.6.1 Connection
Lists control options for current connection. Intermediaries MUST parse and remove listed fields before forwarding. Sender MUST NOT send connection option for end-to-end field.

#### 7.6.2 Max-Forwards
Used with TRACE and OPTIONS. Intermediary MUST check and update: if zero, respond; else decrement and forward.

#### 7.6.3 Via
Indicates intermediate protocols and recipients. Proxy MUST send appropriate Via; gateway MUST send on inbound requests, MAY on responses. MUST NOT combine members with different received-protocol values.

### 7.7 Message Transformations
Proxy MUST NOT modify host name if FQDN. MUST NOT modify absolute-path and query except as required. MUST NOT transform content that has no-transform cache directive. Proxy MAY transform content otherwise; can change status to 203. SHOULD NOT modify endpoint information unless allowed or for privacy/security.

### 7.8 Upgrade
Client MAY send Upgrade header to invite protocol switch. Server MAY ignore. Server sending 101 MUST include Upgrade header with new protocols. Server MUST NOT switch to protocol not indicated by client. Sender of Upgrade MUST also send Connection: upgrade.

## 8. Representation Data and Metadata
### 8.1 Representation Data
Data type determined by Content-Type and Content-Encoding.

### 8.2 Representation Metadata
Fields describing representation. In HEAD responses, metadata describes what would be in GET.

### 8.3 Content-Type
Indicates media type. Sender SHOULD generate Content-Type if media type known. If absent, recipient MAY assume application/octet-stream or examine data.

#### 8.3.1 Media Type
`type "/" subtype parameters`. Type and subtype case-insensitive.

#### 8.3.2 Charset
Used for character encoding schemes. Names case-insensitive.

#### 8.3.3 Multipart Types
Multipart types use boundary parameter. Sender MUST generate only CRLF for line breaks between parts.

### 8.4 Content-Encoding
Indicates content codings applied. Sender MUST list in order applied. "identity" SHOULD NOT be included. Origin server MAY respond 415 if unacceptable.

#### 8.4.1 Content Codings
Case-insensitive tokens. Registered in HTTP Content Coding Registry.
- **Compress**: LZW coding. Equivalent to "x-compress".
- **Deflate**: zlib containing deflate data.
- **Gzip**: LZ77 with CRC. Equivalent to "x-gzip".

### 8.5 Content-Language
Describes natural language(s) of intended audience. Multiple languages MAY be listed.

#### 8.5.1 Language Tags
Per RFC 5646. Used in Accept-Language and Content-Language.

### 8.6 Content-Length
Decimal non-negative integer of octets. User agent SHOULD send Content-Length in request when method defines meaning for content. Server MUST NOT send Content-Length in HEAD response unless equals length that would be in GET. Same restriction for 304. Server MUST NOT send in 1xx, 204, or 2xx CONNECT. Sender MUST NOT forward with incorrect value. If duplicated with same decimal value, MAY reject or replace.

### 8.7 Content-Location
URI that can be used as identifier for the specific representation in this message's content. If same as target URI in 2xx response, recipient MAY consider content a current representation. For state-changing methods, indicates new representation. User agent MUST NOT use to alter request semantics.

### 8.8 Validator Fields
#### 8.8.1 Weak versus Strong
- **Strong validator**: changes value whenever change occurs to representation data observable in 200 response.
- **Weak validator**: might not change for every change. Weak if shared by two representations at same time unless identical data.
Strong usable for all conditional requests; weak only for cache validation and limited cases.

#### 8.8.2 Last-Modified
Timestamp. Origin server SHOULD send Last-Modified if reasonably determinable. MUST NOT generate date later than message origination time. Without clock, MUST NOT generate unless assigned by other system.

##### 8.8.2.1 Generation
Last-Modified value should be as close to response generation as possible.

##### 8.8.2.2 Comparison
Implicitly weak unless specific conditions hold (e.g., origin server comparison or cache with Date at least one second later).

#### 8.8.3 ETag
Opaque validator. `ETag = [weak] opaque-tag`. Weak indicated by "W/". If not strong, origin server MUST mark as weak. Sender MAY send in trailer, but preferable as header.

##### 8.8.3.1 Generation
Origin server SHOULD send ETag for any representation where changes can be reasonably determined.

##### 8.8.3.2 Comparison
- Strong: both not weak and opaque-tags match character-by-character.
- Weak: opaque-tags match character-by-character regardless of weakness.

##### 8.8.3.3 Example
Entity tags varying on content negotiation (example omitted).

## 9. Methods
### 9.1 Overview
Method token is primary source of request semantics. All general-purpose servers MUST support GET and HEAD. Other methods OPTIONAL. Unrecognized method SHOULD respond 501; recognized but not allowed SHOULD respond 405.

### 9.2 Common Method Properties
#### 9.2.1 Safe Methods
GET, HEAD, OPTIONS, TRACE are safe. User agent SHOULD distinguish safe from unsafe. Resource owner MUST disable unsafe action when accessed via safe method.

#### 9.2.2 Idempotent Methods
PUT, DELETE, and safe methods are idempotent. Client SHOULD NOT automatically retry non-idempotent unless known to be safe or detection possible. Proxy MUST NOT automatically retry non-idempotent.

#### 9.2.3 Methods and Caching
Method definition must explicitly allow caching. This spec defines caching semantics for GET, HEAD, and POST.

### 9.3 Method Definitions
#### 9.3.1 GET
Transfer current selected representation. Cacheable. Client SHOULD NOT generate content in GET unless made directly to origin server that has indicated support. Origin server SHOULD NOT rely on private agreements.

#### 9.3.2 HEAD
Identical to GET but server MUST NOT send content. Server SHOULD send same header fields as for GET, but MAY omit those determined only while generating content. Cacheable.

#### 9.3.3 POST
Target resource processes enclosed representation. If resource created, origin server SHOULD send 201 with Location. Responses cacheable only with explicit freshness and Content-Location same as target URI.

#### 9.3.4 PUT
Replace/create state with enclosed representation. If new, MUST send 201; if modified, MUST send 200 or 204. Origin server SHOULD verify consistency with resource constraints. MUST NOT send validator unless content saved without transformation and validator reflects new representation. Not cacheable.

#### 9.3.5 DELETE
Remove association. Origin server SHOULD send 202, 204, or 200. Client SHOULD NOT generate content in DELETE unless direct to origin server with support. Not cacheable.

#### 9.3.6 CONNECT
Establish tunnel to destination. Uses special request target (host:port). Server MUST reject if empty/invalid port. Proxy SHOULD restrict use to safe ports. Server MUST NOT send Transfer-Encoding or Content-Length in 2xx response. Client MUST ignore such fields.

#### 9.3.7 OPTIONS
Request communication options. "*" applies to server. Server SHOULD send relevant headers. Client MAY send Max-Forwards. Not cacheable.

#### 9.3.8 TRACE
Loop-back of request message. Final recipient SHOULD reflect message. Client MUST NOT send content. Not cacheable.

# RFC 9110: HTTP Semantics
**Source**: IETF | **Version**: STD 98 | **Date**: June 2022 | **Type**: Normative
**Original**: [Provided text – chunk 2 of 2]

## Scope (Summary)
Defines extensibility points for HTTP (methods, status codes, field names, authentication schemes, range units, content codings, upgrade tokens) and their registration procedures. Also covers security considerations and IANA registrations.

## Normative References
- [CACHING] – HTTP Caching (STD 98, RFC 9111)
- [HTTP/1.1] – HTTP/1.1 (STD 99, RFC 9112)
- [HTTP/2] – HTTP/2 (RFC 9113)
- [RFC1950] – ZLIB Compressed Data Format
- [RFC1951] – DEFLATE Compressed Data Format
- [RFC1952] – GZIP file format
- [RFC2046] – MIME Part Two: Media Types
- [RFC2119] – Key words for use in RFCs
- [RFC4647] – Matching of Language Tags
- [RFC4648] – Base16, Base32, Base64
- [RFC5234] – ABNF (STD 68)
- [RFC5280] – X.509 PKI Certificate Profile
- [RFC5322] – Internet Message Format
- [RFC5646] – Tags for Identifying Languages
- [RFC6125] – Domain-Based Application Service Identity
- [RFC6365] – Terminology Used in Internationalization
- [RFC7405] – Case-Sensitive String Support in ABNF
- [RFC8126] – Guidelines for Writing an IANA Considerations Section
- [RFC8174] – Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
- [TCP] – Transmission Control Protocol (STD 7, RFC 793)
- [TLS13] – Transport Layer Security Protocol Version 1.3 (RFC 8446)
- [URI] – URI Generic Syntax (STD 66, RFC 3986)
- [USASCII] – ANSI X3.4
- [Welch] – A Technique for High-Performance Data Compression

## Definitions and Abbreviations
- **authoritative response**: A response determined by (or at the direction of) the origin server as most appropriate for the request.
- **content coding**: Encoding transformation applied to a representation's content (Section 8.4.1).
- **field**: A protocol element that conveys metadata (header or trailer field).
- **idempotent**: A method where multiple identical requests have the same effect as a single request (Section 9.2.2).
- **intermediary**: A recipient that acts as both server and client (proxy, gateway, tunnel).
- **origin server**: The server that can provide an authoritative response for the target resource.
- **range unit**: A unit for specifying byte ranges or other range types (Section 14.1).
- **safe**: A method that does not have side effects (Section 9.2.1).
- **target URI**: The URI derived from the request target (Section 7.1).
- **transitional** (not used)
- **upgrade token**: A protocol name used in the Upgrade header field.

## Extending HTTP

### 16.1 Method Extensibility
#### 16.1.1 Method Registry
- **Registry**: "Hypertext Transfer Protocol (HTTP) Method Registry" at <https://www.iana.org/assignments/http-methods>.
- **Registration fields**: Method Name, Safe ("yes"/"no"), Idempotent ("yes"/"no"), Pointer to specification text.
- **Normative**: Values added require IETF Review (RFC 8126, Section 4.8).

#### 16.1.2 Considerations for New Methods
- Standardized methods shall be generic (applicable to any resource).
- New methods shall not change the parsing algorithm or prohibit content presence (except allowing zero-length via Content-Length: 0).
- New methods shall not use host:port or asterisk forms of request target (except CONNECT/OPTIONS).
- New method definitions **must** indicate: safe, idempotent, cacheable, semantics of request content, header/status code refinements.
- If cacheable, definition ought to describe caching conditions.
- Ought to describe ability to be conditional (Section 13.1) and partial response semantics (Section 14.2).
- **Note**: Avoid method names starting with "M-" (could be misinterpreted per RFC 2774).

### 16.2 Status Code Extensibility
#### 16.2.1 Status Code Registry
- **Registry**: "Hypertext Transfer Protocol (HTTP) Status Code Registry" at <https://www.iana.org/assignments/http-status-codes>.
- **Registration must include**: Status Code (3 digits), Short Description, Pointer to specification text.
- **Normative**: Values require IETF Review.

#### 16.2.2 Considerations for New Status Codes
- Status codes shall be generic.
- New status codes **must** fall under one of the categories defined in Section 15.
- New status codes shall not disallow content (can mandate zero-length).
- Proposals for unregistered codes ought to use "4NN" or "3N0"–"3N9" notation.
- Definition ought to explain request conditions, dependencies on response header fields.
- Default scope: applies only to the request. If larger scope, must explicitly specify.
- New final status code ought to specify heuristic cacheability.
- Ought to indicate whether content has implied association with an identified resource.

### 16.3 Field Extensibility
#### 16.3.1 Field Name Registry
- **Registry**: "Hypertext Transfer Protocol (HTTP) Field Name Registry" at <https://www.iana.org/assignments/http-fields/>.
- **Registration fields**: Field name (must conform to field-name syntax, should be letters/digits/hyphen, first character letter), Status (permanent, provisional, deprecated, obsoleted), Specification document(s), optionally Comments.
- **Normative**: Field names registered by designated expert. Permanent status requires Specification Required (RFC 8126, Section 4.6).
- Standards-defined names have status "permanent". Other names should be registered as "provisional".

#### 16.3.2 Considerations for New Fields
- Authors should document: conditions of use, semantics refinement by context, scope of applicability, intermediary insertion/deletion/modification, trailer allowability, Connection header listing, security considerations.
- Request header fields: consider Vary, PUT storage, redirect removal.
##### 16.3.2.1 Considerations for New Field Names
- Choose short, descriptive names. Limited-use fields encouraged to use a prefix (e.g., "Foo-Desc").
- **Should**: Use alphanumeric, "-", "."; begin with a letter. Underscore problematic (see Section 17.10).
- Field names ought not be prefixed with "X-" (per BCP 178).
##### 16.3.2.2 Considerations for New Field Values
- Authors encouraged (not required) to use ABNF rules or RFC 8941 for syntax.
- Consider impact of multiple field lines (Section 5.3). Delimit or encode values containing commas.
- Authors of singleton field values should document handling of multiple members.

### 16.4 Authentication Scheme Extensibility
#### 16.4.1 Authentication Scheme Registry
- **Registry**: at <https://www.iana.org/assignments/http-authschemes>.
- **Registration must include**: Authentication Scheme Name, Pointer to specification text, Notes (optional).
- Values require IETF Review.

#### 16.4.2 Considerations for New Authentication Schemes
- **Must be stateless**.
- **Must not** use "realm" parameter incompatible with Section 11.5.
- New schemes ought to use auth-param syntax (not token68) to allow future extensions.
- Parsing defined by this specification cannot be modified.
- Ought to define treatment of unknown extension parameters (prefer "must-ignore").
- Must document usability for origin-server and/or proxy authentication.
- Credentials in Authorization have same cache effect as "private" directive. Schemes not using Authorization must disallow caching via cache directives.
- Schemes using Authentication-Info, Proxy-Authentication-Info must document security considerations.

### 16.5 Range Unit Extensibility
#### 16.5.1 Range Unit Registry
- **Registry**: at <https://www.iana.org/assignments/http-parameters> (HTTP Range Unit Registry).
- **Registration must include**: Name, Description, Pointer to specification text.
- Values require IETF Review.

#### 16.5.2 Considerations for New Range Units
- Alternative range units (pages, sections, records, rows, time) potentially usable for application-specific purposes but not common. Implementors should consider interoperability with content codings and intermediaries.

### 16.6 Content Coding Extensibility
#### 16.6.1 Content Coding Registry
- **Registry**: at <https://www.iana.org/assignments/http-parameters/>.
- **Registration must include**: Name, Description, Pointer to specification text.
- Content coding names **must not** overlap with transfer coding names unless encoding transformation identical.
- Values require IETF Review and must conform to purpose defined in Section 8.4.1.

#### 16.6.2 Considerations for New Content Codings
- New content codings ought to be self-descriptive whenever possible.

### 16.7 Upgrade Token Registry
- **Registry**: at <https://www.iana.org/assignments/http-upgrade-tokens>.
- Registration on "First Come First Served" basis (RFC 8126, Section 4.4).
- Rules:
  1. Once registered, stays forever.
  2. Case-insensitive; register preferred case.
  3. Must name responsible party.
  4. Must name point of contact.
  5. May name specifications.
  6. Should name expected "protocol-version" tokens.
  7. Responsible party may change registration; IANA keeps record.
  8. IESG may reassign responsibility.

## Security Considerations (Section 17)
- **Normative**: Developers must be informed of known security concerns.
- **17.1 Establishing Authority**: "http" URI scheme relies on name resolution services; attacks on DNS or routing can undermine authority. "https" scheme mitigates via secured connection and identity verification.
- **17.2 Risks of Intermediaries**: Intermediaries are on-path; compromise can lead to serious security/privacy issues.
- **17.3 Attacks Based on File and Path Names**: Origin servers must avoid accessing special file names ("..", system devices).
- **17.4 Attacks Based on Command, Code, or Query Injection**: Request data cannot be trusted; avoid interpretation as instructions.
- **17.5 Attacks via Protocol Element Length**: Implementations should limit processing of long streams; specific recommendations on minimum size limits (Section 5.4). Servers can reject too long URIs (414) or too large content (413).
- **17.6 Attacks Using Shared-Dictionary Compression**: Mitigation: disable compression on sensitive data or strictly separate attacker-controlled data.
- **17.7 Disclosure of Personal Information**: Implementations must prevent unintentional disclosure.
- **17.8 Privacy of Server Log Information**: Log information confidential; should be purged of personally identifiable information when no longer needed.
- **17.9 Disclosure of Sensitive Information in URIs**: URIs are not secure; avoid including sensitive data. POST preferred over GET for form data with sensitive info.
- **17.10 Application Handling of Field Names**: Gateways (e.g., CGI) map field names to environment variables; this can lead to security vulnerabilities (e.g., Transfer_Encoding vs Transfer-Encoding). Implementations should make mapping unambiguous.
- **17.11 Disclosure of Fragment after Redirects**: Fragment visible to user agent; redirects should include a fragment component to block inheritance.
- **17.12 Disclosure of Product Information**: Via header allows pseudonyms to hide internal host names.
- **17.13 Browser Fingerprinting**: Proactive negotiation headers (Accept, Accept-Language, etc.) can expose unique characteristics; user agents should be conservative.
- **17.14 Validator Retention**: Entity tags can be used for re-identification; caches should be cleared on privacy actions.
- **17.15 Denial-of-Service Attacks Using Range**: Servers ought to ignore, coalesce, or reject egregious range requests.
- **17.16 Authentication Considerations**:
  - **17.16.1 Confidentiality of Credentials**: HTTP does not define confidentiality; rely on transport security (Section 4.2.2).
  - **17.16.2 Credentials and Idle Clients**: User agents should provide mechanisms to discard cached credentials.
  - **17.16.3 Protection Spaces**: Realm-based protection exposes credentials to all resources on same origin; mitigation: separate hosts/ports.
  - **17.16.4 Additional Response Fields**: Authentication-Info headers can reveal presence of authentication; scheme-specific parameters must consider security.

## IANA Considerations (Section 18)
- **Change controller**: IETF (iesg@ietf.org).
- **18.1 URI Scheme Registration**: Updated Table 2.
- **18.2 Method Registration**: Updated registry with procedures and methods (CONNECT, DELETE, GET, HEAD, OPTIONS, POST, PUT, TRACE, * – reserved).
- **18.3 Status Code Registration**: Updated registry with codes 100–505 (Table 8).
- **18.4 Field Name Registration**: New registry created; moved all HTTP fields from old message header registries. Field names with status 'standard','experimental','reserved','informational' made 'permanent'. Table 9 lists 42 fields.
- **18.5 Authentication Scheme Registration**: Updated registry; no new schemes in this document.
- **18.6 Content Coding Registration**: Updated registry with compress, deflate, gzip, identity, x-compress, x-gzip (Table 10).
- **18.7 Range Unit Registration**: Updated registry with "bytes" and "none" (Table 11).
- **18.8 Media Type Registration**: Updated "multipart/byteranges" and note about "q" parameters.
- **18.9 Port Registration**: Updated services on ports 80 and 443.
- **18.10 Upgrade Token Registration**: Updated registry with "HTTP" token (Table 12).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | HTTP method registrations MUST include Method Name, Safe, Idempotent, Specification pointer. | MUST | 16.1.1 |
| R2 | New methods MUST NOT change parsing algorithm or prohibit content presence. | MUST | 16.1.2 |
| R3 | New methods MUST indicate safe, idempotent, cacheable, request content semantics. | MUST | 16.1.2 |
| R4 | Status code registrations MUST include 3-digit code, Short Description, Spec pointer. | MUST | 16.2.1 |
| R5 | New status codes MUST fall under a class defined in Section 15. | MUST | 16.2.2 |
| R6 | New status codes MUST NOT disallow content. | MUST | 16.2.2 |
| R7 | Field name MUST conform to field-name syntax (Section 5.1). | MUST | 16.3.1 |
| R8 | Authentication scheme registrations MUST include Name, Spec pointer, optional Notes. | MUST | 16.4.1 |
| R9 | New authentication schemes MUST be stateless. | MUST | 16.4.2 |
| R10 | New authentication schemes MUST NOT use "realm" incompatibly. | MUST | 16.4.2 |
| R11 | Range unit registrations MUST include Name, Description, Spec pointer. | MUST | 16.5.1 |
| R12 | Content coding registrations MUST include Name, Description, Spec pointer. | MUST | 16.6.1 |
| R13 | Content coding names MUST NOT overlap with transfer coding names unless identical. | MUST | 16.6.1 |
| R14 | Upgrade token registrations MUST name responsible party and point of contact. | MUST | 16.7 |
| R15 | Upgrade token registrants MUST follow First Come First Served rules. | MUST | 16.7 |
| R16 | New methods SHOULD use short, descriptive names; avoid "M-" prefix. | SHOULD | 16.1.2 |
| R17 | New field names SHOULD be restricted to letters, digits, hyphen; first character letter. | SHOULD | 16.3.2.1 |
| R18 | New field names ought not be prefixed with "X-". | OUGHT NOT | 16.3.2.1 |
| R19 | New authentication schemes ought to use auth-param syntax. | OUGHT | 16.4.2 |
| R20 | New content codings ought to be self-descriptive when possible. | OUGHT | 16.6.2 |

## Informative Annexes (Condensed)
- **Appendix A (Collected ABNF)**: Formal grammar for all HTTP fields and core rules.
- **Appendix B (Changes from Previous RFCs)**: Summarizes differences between RFC 9110 and earlier RFCs (7230, 7231, 7232, 7233, 7235, etc.) including clarifications on field values, target URI, content, status codes, and preconditions.
- **Acknowledgements**: Credits to many contributors and prior specifications.
- **Index**: Alphabetical list of terms and sections.