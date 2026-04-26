# RFC 7252: The Constrained Application Protocol (CoAP)
**Source**: IETF | **Version**: Standards Track | **Date**: June 2014 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc7252

## Scope (Summary)
CoAP is a specialized web transfer protocol for constrained nodes and networks (e.g., low-power, lossy). It provides a request/response model over UDP, with built-in discovery, multicast support, low overhead, and easy HTTP mapping for M2M applications such as smart energy and building automation.

## Normative References
- RFC 768, RFC 2045, RFC 2046, RFC 2119, RFC 2616, RFC 3023, RFC 3629, RFC 3676, RFC 3986, RFC 4279, RFC 4395, RFC 5147, RFC 5198, RFC 5226, RFC 5234, RFC 5246, RFC 5280, RFC 5480, RFC 5785, RFC 5952, RFC 5988, RFC 6066, RFC 6347, RFC 6690, RFC 6920, RFC 7250, RFC 7251.

## Definitions and Abbreviations
- **Endpoint**: Entity participating in CoAP, identified by IP address, UDP port, and optionally security association.
- **Client/Server**: Originating/destination endpoint of request/response respectively.
- **Confirmable (CON)**: Message requiring acknowledgement.
- **Non-confirmable (NON)**: Message not requiring acknowledgement.
- **Acknowledgement (ACK)**: Confirms receipt of CON; may carry piggybacked response.
- **Reset (RST)**: Indicates message received but missing context.
- **Piggybacked Response**: Response included in ACK message.
- **Separate Response**: Response sent in a separate CON/NON after an empty ACK.
- **Critical/Elective Option**: Determined by odd/even option number; unrecognized critical → error.
- **Unsafe/Safe-to-Forward**: Proxy handling classes.
- **Resource Discovery**: Querying server for hosted resources (CoRE Link Format).
- **Content-Format**: Numeric identifier for media type + content-coding.

## Key Normative Requirements

### 2. Constrained Application Protocol
- CoAP uses a 4-byte header over UDP; messages can be CON, NON, ACK, or RST.

### 3. Message Format
- Version field MUST be set to 1.
- Token length 9-15 MUST NOT be sent; MUST be processed as error.
- Payload marker 0xFF; zero-length payload after marker is error.
- Options MUST appear in order of Option Number; delta encoding used.

### 4. Message Transmission
- **4.2**: Recipient MUST either ACK or RST a CON message. RST echoes Message ID and MUST be empty.
- **4.2**: Retransmission with exponential back-off: timeout = random between ACK_TIMEOUT and ACK_TIMEOUT*ACK_RANDOM_FACTOR; up to MAX_RETRANSMIT retries.
- **4.3**: NON messages MUST NOT be acknowledged; if invalid, MAY send RST.
- **4.4**: Message ID MUST be echoed in ACK/RST. Same Message ID MUST NOT be reused within EXCHANGE_LIFETIME.
- **4.5**: Duplicate CON SHOULD be acknowledged but processed only once (may relax for idempotent requests).
- **4.6**: Messages SHOULD fit in a single IP packet; assume MTU 1280 bytes.
- **4.7**: Clients MUST limit outstanding interactions to NSTART (default 1). Rate MUST not exceed PROBING_RATE (1 byte/s).
- **4.8**: Default parameters: ACK_TIMEOUT=2s, ACK_RANDOM_FACTOR=1.5, MAX_RETRANSMIT=4, NSTART=1.

### 5. Request/Response Semantics
- **5.1**: GET is safe, MUST NOT take other action. GET, PUT, DELETE MUST be idempotent. POST is not idempotent.
- **5.2**: Response code format: c.dd (c=class, dd=detail). Unrecognized 4.xx/5.xx treated as 4.00/5.00.
- **5.2.1**: Piggybacked response in ACK.
- **5.2.2**: Separate response: server sends empty ACK, then CON with response.
- **5.2.3**: NON request → SHOULD return NON response.
- **5.3.1**: Token (0-8 bytes) MUST be echoed unchanged in response. Client SHOULD generate non-trivial randomized token (>=32 bits for Internet).
- **5.3.2**: Matching rules: source endpoint must match destination of request; Message ID match for piggybacked, token match always.
- **5.4.1**: Unrecognized critical options in CON request → 4.02 response; in CON response → reject message.
- **5.4.2**: Proxy behavior for unrecognized options based on Unsafe/Safe-to-Forward; NoCacheKey bits determine Cache-Key inclusion.
- **5.4.4**: If option absent, default value assumed.
- **5.4.5**: Non-repeatable option MUST NOT appear more than once; extra occurrences treated as unrecognized.
- **5.5.1**: No default Content-Format; inference only if no option given.
- **5.5.2**: Diagnostic payload must be UTF-8 Net-Unicode; SHOULD be empty if no additional info.
- **5.6**: Caching: response must be cacheable per Response Code definition. Stored response used only if method and options match (except NoCacheKey), and response is fresh or validated.
- **5.6.1**: Max-Age default 60s. To prevent caching, MUST include Max-Age=0.
- **5.6.2**: ETag for validation: 2.03 (Valid) response indicates stored response can be reused.
- **5.7.1**: Proxy: unrecognized unsafe options → 4.02; safe-to-forward options forwarded. Timeout → 5.04; unprocessable → 5.02.
- **5.7.2**: Proxy request uses Proxy-Uri or Proxy-Scheme; MUST NOT include Uri-* options. Unwilling → 5.05.
- **5.8.1**: GET: success → 2.05 or 2.03.
- **5.8.2**: POST: created → 2.01 with Location-* options; changed → 2.04; deleted → 2.02.
- **5.8.3**: PUT: update existing → 2.04; create → 2.01.
- **5.8.4**: DELETE: success → 2.02.
- **5.9.1.1**: 2.01 responses: cache MUST mark stored response as not fresh.
- **5.9.1.3**: 2.03 (Valid): MUST include ETag, no payload. Cache updates Max-Age and replaces option sets.
- **5.9.2.9**: 4.13 response SHOULD include Size1 option.
- **5.10.1**: Uri-Path and Uri-Query values MUST NOT be "." or "..".
- **5.10.2**: Proxy-Uri takes precedence over Uri-* options; those MUST NOT be present together.
- **5.10.4**: Accept option: if preferred not available, MUST return 4.06.
- **5.10.5**: Max-Age value between 0 and 2^32-1 seconds; default 60.
- **5.10.6**: ETag: opaque; server-generated; response option MUST NOT occur more than once; request option may occur 0+ times.
- **5.10.7**: Location-Path and Location-Query options; values MUST NOT be "." or "..". Passing through cache → mark corresponding stored responses as not fresh.
- **5.10.8**: Conditional options: If condition not fulfilled, server MUST NOT perform method, MUST respond 4.12.
- **5.10.9**: Size1: integer bytes; used in 4.13 to indicate max acceptable entity size.

### 6. CoAP URIs
- **6.1**: coap URI scheme: default port 5683. Host MUST NOT be empty.
- **6.2**: coaps scheme: default port 5684; MUST use DTLS.
- **6.3**: Normalization: elide default port, empty path → "/", scheme/host lowercase.
- **6.4**: URI parsing into options: fail if not absolute URI; fail if fragment present; Uri-Host only if host is reg-name (not IP literal); Uri-Port only if port differs from destination.
- **6.5**: URI composition from options: if secured → "coaps://" else "coap://". Percent-encoding MUST use uppercase hexadecimal.

### 7. Discovery
- **7.1**: Server MUST support CoAP default port 5683 for resource discovery.
- **7.2**: SHOULD support CoRE Link Format per RFC 6690.
- **7.2.1**: 'ct' attribute: decimal ASCII integer 0-65535; may include space-separated list.

### 8. Multicast CoAP
- **8.1**: Multicast requests MUST be Non-confirmable. Server aware of multicast MUST NOT return RST to NON. Message ID conflict avoidance.
- **8.2**: Server MAY ignore multicast request. If responding, SHOULD randomize response time using Leisure >= S*G/R. Default Leisure = 5s.
- **8.2.1**: Response to multicast GET MAY satisfy subsequent unicast request on related URI. GET to multicast MUST NOT contain ETag.

### 9. Securing CoAP
- **9.1**: NoSec (no DTLS), PreSharedKey, RawPublicKey, Certificate modes.
- **NoSec**: alternative lower-layer security SHOULD be used when appropriate.
- **9.1.1**: CoAP client acts as DTLS client. All CoAP messages MUST be sent as DTLS "application data". ACK/RST matching: same DTLS session and epoch.
- **9.1.2**: Response matching: same DTLS session and epoch; NoSec response to DTLS request MUST be rejected.
- **9.1.3**: Devices SHOULD support SNI.
- **9.1.3.1**: PreSharedKey: MUST support TLS_PSK_WITH_AES_128_CCM_8.
- **9.1.3.2**: RawPublicKey: MUST support TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8; curve secp256r1, SHA-256. MUST use Supported Elliptic Curves and Supported Point Formats extensions.
- **9.1.3.2.1**: Identity derived per RFC 6920 sha-256-120 mode. Implementations MUST support binary mode.
- **9.1.3.3**: Certificate mode: MUST support same cipher suite as RawPublicKey. Subject based on EUI-64 or FQDN. MUST validate per RFC 5280; SubjectAltName matching if present, else CN (no wildcards). SHOULD check certificate validity if absolute time available.

### 10. Cross-Protocol Proxying between CoAP and HTTP
- **10.1**: CoAP-HTTP proxy: use Proxy-Uri with "http" or "https". Method mappings: GET→2.05, PUT→2.01/2.04, DELETE→2.02, POST→2.01/2.04. ETag, Accept handled.
- **10.2**: HTTP-CoAP proxy: OPTIONS/TRACE → 501; GET→200; HEAD→200 without body; POST→200/204/201; PUT→201/200/204; DELETE→200/204; CONNECT→501.

### 11. Security Considerations
- **11.1**: URI processing is likely source of vulnerabilities; implement with care.
- **11.2**: Proxies are men-in-the-middle; caching may leak data. coaps responses MUST NOT be reused for shared caching unless equivalent access control.
- **11.3**: Amplification risk; large responses SHOULD use block-wise transfers to limit amplification.
- **11.4**: IP spoofing: token randomization mitigates response spoofing.
- **11.5**: Cross-protocol attacks; NoSec environment must firewall all UDP endpoints.
- **11.6**: Constrained nodes: MUST NOT use for key generation if poor entropy; keys externally provisioned. Care with timing attacks and tampering.

### 12. IANA Considerations
- **12.1**: CoAP Code Registries (Method and Response Codes) with IETF Review.
- **12.2**: Option Numbers Registry (split ranges: 0-255 IETF, 256-2047 Spec Required, 2048-64999 Expert Review, 65000-65535 Experimental).
- **12.3**: Content-Formats Registry (0-255 Expert Review, 256-9999 IETF, 10000-64999 First Come, 65000-65535 Experimental).
- **12.4-12.7**: URI schemes "coap" and "coaps" registered; ports 5683/5684.
- **12.8**: Multicast addresses: IPv4 224.0.1.187, IPv6 FF0X::FD.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Version field MUST be set to 1 | MUST | Section 3 |
| R2 | Token length 9-15 MUST NOT be sent, MUST be processed as error | MUST | Section 3 |
| R3 | Recipient MUST ACK or RST a CON message; RST MUST be empty | MUST | Section 4.2 |
| R4 | NON messages MUST NOT be acknowledged | MUST | Section 4.3 |
| R5 | Message ID MUST be echoed in ACK/RST | MUST | Section 4.4 |
| R6 | Same Message ID MUST NOT be reused within EXCHANGE_LIFETIME | MUST | Section 4.4 |
| R7 | Clients MUST limit outstanding interactions to NSTART (default 1) | MUST | Section 4.7 |
| R8 | GET is safe, MUST NOT take other action on resource | MUST | Section 5.1 |
| R9 | GET, PUT, DELETE MUST be idempotent | MUST | Section 5.1 |
| R10 | Token MUST be echoed unchanged in response | MUST | Section 5.3.1 |
| R11 | Unrecognized critical options in CON request → 4.02 response | MUST | Section 5.4.1 |
| R12 | If option absent, default value MUST be assumed | MUST | Section 5.4.4 |
| R13 | Non-repeatable option MUST NOT appear more than once | MUST | Section 5.4.5 |
| R14 | Multicast requests MUST be Non-confirmable | MUST | Section 8.1 |
| R15 | All CoAP messages MUST be sent as DTLS "application data" when DTLS enabled | MUST | Section 9.1.1 |
| R16 | PreSharedKey mode MUST support TLS_PSK_WITH_AES_128_CCM_8 | MUST | Section 9.1.3.1 |
| R17 | RawPublicKey mode MUST support TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 | MUST | Section 9.1.3.2 |
| R18 | Certificate mode MUST support same cipher suite as RawPublicKey | MUST | Section 9.1.3.3 |

## Informative Annexes (Condensed)
- **Appendix A**: Provides examples of GET request flows: piggybacked, retransmitted, separate, multicast scenarios with message hex dumps.
- **Appendix B**: URI examples demonstrating decomposition/composition with various options (e.g., bare IP, hostname, non-ASCII characters, query parameters).