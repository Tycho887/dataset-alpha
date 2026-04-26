# RFC 3261: SIP: Session Initiation Protocol
**Source**: IETF (Standards Track) | **Version**: Obsoletes RFC 2543 | **Date**: June 2002 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc3261

## Scope (Summary)
This document defines the Session Initiation Protocol (SIP), an application-layer control (signaling) protocol for creating, modifying, and terminating multimedia sessions (e.g., Internet telephone calls, conferences) with one or more participants. SIP works with SDP for session description and uses proxies, registrars, and redirect servers to locate users and route requests.

## Normative References
- RFC 2119 (BCP 14): Key words for requirement levels
- RFC 2327: SDP
- RFC 2396: URI syntax
- RFC 2616: HTTP/1.1 (referenced for header syntax)
- RFC 2806: tel URL
- RFC 2822: message format
- [4] SIP-specific DNS procedures (RFC 3263)
- [13] SDP offer/answer (RFC 3264)
- Others as cited

## Definitions and Abbreviations
- **Address-of-Record (AOR)**: SIP/SIPS URI pointing to a location service that maps to contact addresses.
- **Back-to-Back User Agent (B2BUA)**: Logical entity that acts as UAS and UAC, maintaining dialog state.
- **Call Leg**: Former term for dialog (not used in this spec).
- **Call Stateful**: Proxy that retains state for a dialog from INVITE to BYE.
- **Client**: Network element that sends SIP requests and receives responses.
- **Conference**: Multimedia session with multiple participants.
- **Core**: Functions specific to a SIP entity type (UA, proxy, registrar, etc.).
- **Dialog**: Peer-to-peer SIP relationship between two UAs, identified by Call-ID, local tag, and remote tag. Persists for the duration of the call.
- **Early dialog**: Dialog created by a provisional response (e.g., 180 Ringing) before final response.
- **Final response**: Response that terminates a SIP transaction (2xx-6xx).
- **Header Field**: Component of SIP message header; may have multiple values.
- **Home Domain**: Domain providing service to a SIP user (typically in AOR).
- **Location Service**: Abstract service used by proxies/redirect servers to obtain callee locations.
- **Loose Routing**: Proxy that processes Route header separately from Request-URI (as per this spec).
- **Method**: Primary function of a SIP request (e.g., INVITE, BYE, REGISTER, OPTIONS, CANCEL, ACK).
- **Outbound Proxy**: Proxy that receives requests from a client even if not resolved by Request-URI.
- **Provisional Response**: 1xx response indicating progress.
- **Proxy/Proxy Server**: Intermediary that routes requests, may enforce policy.
- **Redirect Server**: UAS that returns 3xx responses to direct client to alternate URIs.
- **Registrar**: Server that accepts REGISTER requests and updates Location Service.
- **Route Set**: Ordered list of SIP/SIPS URIs representing proxies to traverse for a request.
- **Session**: Set of multimedia senders and receivers; defined by SDP origin fields.
- **SIP Transaction**: Request + all responses (including ACK for non-2xx to INVITE). For INVITE with 2xx, ACK is separate transaction.
- **Spiral**: Request that returns to a proxy with different Request-URI (not an error).
- **Stateful Proxy**: Maintains client/server transaction state machines.
- **Stateless Proxy**: Forwards requests/responses without maintaining state.
- **Strict Routing**: Proxy that replaces Request-URI with first Route header value (RFC 2543).
- **Target Refresh Request**: Request within a dialog that can modify remote target (e.g., re-INVITE).
- **Transaction User (TU)**: Layer above transaction layer (UAC core, UAS core, proxy core).
- **User Agent (UA)**: Logical entity that can act as both UAC and UAS.
- **User Agent Client (UAC)**: Creates and sends requests.
- **User Agent Server (UAS)**: Generates responses to requests.

## 1. Introduction (Informative)
SIP enables endpoints (user agents) to discover each other and agree on session characteristics. It supports user location, availability, capabilities, session setup, and management. SIP works with RTP, RTSP, MEGACO, and SDP. It provides security services including authentication, integrity, and privacy. It operates over IPv4 and IPv6.

## 2. Overview of SIP Functionality (Informative)
SIP establishes, modifies, and terminates multimedia sessions. It supports name mapping and personal mobility. The five facets are: user location, availability, capabilities, session setup, and session management. SIP is not a vertically integrated system; it must be used with other IETF protocols. It does not provide services directly but provides primitives (e.g., locate user, deliver opaque object).

## 3. Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119.

## 4. Overview of Operation (Informative)
Describes the basic SIP trapezoid: Alice (UAC) sends INVITE to Bob via two proxies. The INVITE contains Via, Max-Forwards, To, From, Call-ID, CSeq, Contact, Content-Type, Content-Length. Responses (100 Trying, 180 Ringing, 200 OK) follow reverse path. ACK is sent directly after 200 OK. Media flows directly between endpoints. Registration (REGISTER) binds AOR to contact addresses. CANCEL cancels pending INVITE, OPTIONS queries capabilities.

## 5. Structure of the Protocol
SIP is layered: syntax/encoding (BNF, Section 25), transport layer (Section 18), transaction layer (Section 17), and transaction user (TU). User agents and stateful proxies contain transaction layer; stateless proxies do not. The TU includes UAC core, UAS core, and proxy core. Dialogs (Section 12) facilitate sequencing and routing within a peer-to-peer relationship. INVITE is the only method defined to establish a dialog in this specification.

## 6. Definitions (See Definitions section above – key terms extracted)

## 7. SIP Messages
SIP is a text-based protocol using UTF-8. Messages are either requests or responses, following RFC 2822 format with start-line, header fields, empty line, and optional body. SIP syntax differs from HTTP in character set and grammar.

### 7.1 Requests
Have a Request-Line containing Method, Request-URI, and SIP-Version. Six methods defined: REGISTER, INVITE, ACK, CANCEL, BYE, OPTIONS. Additional methods may be defined in standards-track RFCs.
- **Request-URI**: SIP/SIPS URI (or other schemes like tel). MUST NOT contain unescaped spaces or control characters.
- **SIP-Version**: MUST be "SIP/2.0", case-insensitive but MUST send upper-case.

### 7.2 Responses
Have a Status-Line: SIP-Version, Status-Code (3-digit), Reason-Phrase. Status-Code classes: 1xx (Provisional), 2xx (Success), 3xx (Redirection), 4xx (Client Error), 5xx (Server Error), 6xx (Global Failure).

### 7.3 Header Fields
Follow HTTP/1.1 syntax for message-header and folding. Multiple header fields of same name may be combined into comma-separated list if grammar allows (exceptions: WWW-Authenticate, Authorization, Proxy-Authenticate, Proxy-Authorization must not be combined).

#### 7.3.1 Header Field Format
`field-name: field-value`. Spaces around colon allowed but single space preferred. Folding lines using SP/HT. Order of header fields with same name is significant; MUST be possible to combine multiple rows into one comma-separated list. Exceptions as above.

#### 7.3.2 Header Field Classification
Some header fields are only valid in requests or responses; if placed in wrong category, MUST be ignored.

#### 7.3.3 Compact Form
Abbreviated forms for common header fields (Section 20). MAY be substituted at any time; implementations MUST accept both long and short forms.

### 7.4 Bodies
All requests and responses MAY include message bodies. Content-Type required if body present; Content-Encoding if compressed; Content-Length required for stream transports.

#### 7.4.1 Message Body Type
Internet media type given by Content-Type. "multipart" allowed (RFC 2046). Binary bodies permitted; text subtypes default charset UTF-8.

#### 7.4.2 Message Body Length
Provided by Content-Length. "chunked" encoding MUST NOT be used.

### 7.5 Framing SIP Messages
For datagram transports (UDP), each datagram carries one message. For stream transports, Content-Length indicates body size; before start-line, CRLF MUST be ignored.

## 8. General User Agent Behavior
A UA contains UAC (generates requests) and UAS (generates responses). Procedures depend on whether request/response is inside or outside a dialog, and on method.

### 8.1 UAC Behavior (Outside Dialog)
#### 8.1.1 Generating the Request
Minimum required header fields: To, From, CSeq, Call-ID, Max-Forwards, Via.
- **8.1.1.1 Request-URI**: SHOULD set to value of URI in To field (except REGISTER). Pre-existing route set may affect Request-URI and Route header.
- **8.1.1.2 To**: Specifies logical recipient. MUST support SIP URI; if supporting TLS, MUST support SIPS URI. Requests outside dialog MUST NOT contain To tag.
- **8.1.1.3 From**: Logical identity of initiator. SHOULD use "Anonymous" with meaningless URI for privacy. MUST contain a new "tag" parameter, chosen by UAC.
- **8.1.1.4 Call-ID**: Globally unique identifier for dialog. MUST be same for all messages in a dialog. SHOULD be same for all registrations from a UA. Use cryptographically random identifiers recommended.
- **8.1.1.5 CSeq**: Sequence number and method. For non-REGISTER outside dialog, value arbitrary but must be 32-bit unsigned < 2**31.
- **8.1.1.6 Max-Forwards**: MUST insert with value SHOULD be 70.
- **8.1.1.7 Via**: MUST insert. Protocol name and version MUST be "SIP/2.0". Branch parameter MUST be unique across space and time (except for CANCEL and ACK for non-2xx). Branch ID MUST start with "z9hG4bK".
- **8.1.1.8 Contact**: MUST be present and contain exactly one SIP/SIPS URI in any request that can establish a dialog (i.e., INVITE). If Request-URI or top Route is SIPS, Contact MUST be SIPS.
- **8.1.1.9 Supported and Require**: Supported header listing supported extensions (from standards-track RFCs) SHOULD be included. Require header if UAC insists UAS understand extension. Proxy-Require for proxies.
- **8.1.1.10 Additional Message Components**: Optional headers and MIME body.

#### 8.1.2 Sending the Request
Destination determined by DNS procedures from [4] applied to first Route (if exists) or Request-URI. If Request-URI is SIPS, MUST use TLS for alternate destinations. UAC SHOULD follow [4] for stateful elements.

#### 8.1.3 Processing Responses
- **8.1.3.1 Transaction Layer Errors**: Timeout treated as 408; fatal transport error as 503.
- **8.1.3.2 Unrecognized Responses**: Treat final response as x00 of same class; treat unknown provisional as 183.
- **8.1.3.3 Vias**: If more than one Via in response, UAC SHOULD discard.
- **8.1.3.4 Processing 3xx Responses**: Client SHOULD use Contact URIs to formulate new requests. MUST NOT add any URI to target set more than once. If original request was SIPS, MAY recurse to non-SIPS but SHOULD inform user.
- **8.1.3.5 Processing 4xx Responses**: Specific retry behaviors for 401, 407, 413, 415, 416, 420. Retry with same Call-ID, To, From, but new CSeq incremented by one.

### 8.2 UAS Behavior (Outside Dialog)
Request processing is atomic. UAS SHOULD process in order: authentication, method inspection, header inspection, content processing, extension application, then method-specific.

- **8.2.1 Method Inspection**: If method recognized but not supported, generate 405 with Allow header.
- **8.2.2 Header Inspection**: Ignore unknown header fields. Ignore malformed but non-essential header fields.
  - **8.2.2.1 To and Request-URI**: To identifies original recipient; UAS MAY accept even if not recognized. Request-URI must identify UAS; if scheme unsupported, 416; if not willing to accept, 404.
  - **8.2.2.2 Merged Requests**: If request has no To tag, check for ongoing transactions. If From tag, Call-ID, CSeq match but request not matching transaction (per Section 17.2.3), SHOULD generate 482.
  - **8.2.2.3 Require**: If UAS does not understand option-tag in Require, MUST respond with 420 and Unsupported header.
- **8.2.3 Content Processing**: If body type, language, or encoding not understood and body part not optional, reject with 415. Response MUST contain Accept, Accept-Encoding, Accept-Language as appropriate.
- **8.2.4 Applying Extensions**: Server MUST NOT apply extension unless indicated in Supported header. If cannot process without extension, MAY send 421 (not recommended).
- **8.2.5 Processing the Request**: Method-specific (Sections 10, 11, 13, 15).
- **8.2.6 Generating the Response**: 
  - **8.2.6.1 Sending Provisional Response**: UAS SHOULD NOT issue provisional for non-INVITE. For 100, copy Timestamp.
  - **8.2.6.2 Headers and Tags**: From, Call-ID, CSeq, Via equal to request. To tag added by UAS (except 100) with same tag for all responses.
- **8.2.7 Stateless UAS Behavior**: Does not maintain transaction state. MUST NOT send provisional responses. MUST ignore ACK and CANCEL. To header tags generated statelessly.

### 8.3 Redirect Servers
Constituted of server transaction layer and TU with location service. Does not issue SIP requests. After receiving request (except CANCEL), returns 3xx with Contact header containing alternative locations. MUST NOT redirect to URI equal to Request-URI. Contact header can have expires parameter.

## 9. Canceling a Request
CANCEL is used to cancel a previous request (most useful for INVITE). It is hop-by-hop; stateful proxy responds to CANCEL rather than forwarding.

### 9.1 Client Behavior
CANCEL SHOULD NOT be sent for non-INVITE. Request-URI, Call-ID, To, CSeq numeric part, From MUST be identical to request being cancelled. Only one Via matching top Via of original. If request has Route, CANCEL MUST include those Route values. MUST NOT contain Require/Proxy-Require. If no provisional response received, MUST NOT send CANCEL yet. If final response already received, SHOULD NOT send.

### 9.2 Server Behavior
UAS determines transaction to cancel via Section 17.2.3 (method not CANCEL or ACK). If no matching transaction, 481. If original request still pending, behavior depends on method: for INVITE, SHOULD respond with 487. Regardless, answer CANCEL with 200 (OK) with To tag same as original.

## 10. Registrations

### 10.1 Overview
Registration creates bindings in a location service associating an AOR with contact addresses. REGISTER request sent to registrar (UAS). Registrar updates location service; proxy/redirect server reads it.

### 10.2 Constructing the REGISTER Request
- **Request-URI**: domain of location service (no userinfo).
- **To**: address-of-record (SIP/SIPS URI).
- **From**: address-of-record (same as To unless third-party).
- **Call-ID**: SHOULD be same for all registrations to a registrar.
- **CSeq**: MUST increment by one for each REGISTER with same Call-ID.
- **Contact**: MAY contain zero or more bindings with optional "expires" parameter.
- "action" parameter deprecated.
- UAs MUST NOT send new registration until final response received or timeout.

#### 10.2.1 Adding Bindings
Contact header values are SIP/SIPS URIs (or other schemes). SIPS AOR SHOULD have SIPS Contact. Expiration interval suggested via Expires header or per-Contact "expires" parameter.

#### 10.2.2 Removing Bindings
Set expiration interval = 0. "*" Contact value allowed only with Expires: 0.

#### 10.2.3 Fetching Bindings
Success response contains complete list of existing bindings.

#### 10.2.4 Refreshing Bindings
UA responsible for refreshing own bindings. SHOULD use same Call-ID for registrations during a boot cycle.

#### 10.2.5 Setting the Internal Clock
UAC MAY use Date header from response to set clock.

#### 10.2.6 Discovering a Registrar
Three ways: configuration, host part of address-of-record (using [4]), or multicast to sip.mcast.net (224.0.1.75).

#### 10.2.7 Transmitting a Request
Follow Section 8.1.2. If timeout, UAC SHOULD NOT immediately re-attempt.

#### 10.2.8 Error Responses
If 423 (Interval Too Brief), MAY retry with equal or greater expiration than Min-Expires.

### 10.3 Processing REGISTER Requests
Registrar is UAS that accepts only REGISTER. MUST not generate 6xx. MAY redirect. MUST ignore Record-Route. Steps:
1. Inspect Request-URI for domain access.
2. Process Require.
3. SHOULD authenticate UAC.
4. SHOULD check authorization; if not authorized, 403.
5. Extract AOR from To; if invalid, 404. Canonicalize URI (remove parameters, unescape).
6. Check Contact: if "*" and Expires=0, remove all bindings matching Call-ID and CSeq.
7. Process each Contact address: determine expiration (expires parameter, else Expires header, else local default). Registrar MAY choose shorter expiration; if <1 hour and < configured minimum, MAY reject with 423 and Min-Expires. Search current bindings using URI comparison; if binding exists with different Call-ID, remove if expires=0 else update; if same Call-ID, compare CSeq. All updates must be committed atomically; if any fails, 500.
8. Return 200 (OK) with Contact list and "expires" parameter for each. SHOULD include Date.

## 11. Querying for Capabilities
OPTIONS method allows UA to query another UA or proxy server about capabilities. All UAs MUST support OPTIONS.

### 11.1 Construction of OPTIONS Request
Standard request rules. Contact MAY be present. Accept SHOULD be included (e.g., application/sdp).

### 11.2 Processing of OPTIONS Request
Response code same as would be returned for INVITE. Allow, Accept, Accept-Encoding, Accept-Language, Supported SHOULD be present in 200 (OK). Contact MAY be present. Message body MAY be included. For proxy, Allow SHOULD be omitted.

## 12. Dialogs
A dialog is a peer-to-peer relationship between two UAs, identified by Call-ID, local tag, and remote tag. Contains state: dialog ID, local/remote sequence numbers, local/remote URI, remote target, secure flag, route set.

### 12.1 Creation of a Dialog
Created by non-failure responses with To tag to INVITE (2xx or 101-199). Provisional responses create early dialogs.

#### 12.1.1 UAS Behavior
When generating dialog-creating response (e.g., 2xx to INVITE), UAS MUST copy all Record-Route from request into response, maintain order. MUST add Contact header (SIP or SIPS URI). Set route set from Record-Route in request (in order). Set remote target to Contact from request. Set remote sequence number from CSeq of request. Set local sequence number empty. Set Call-ID, local tag, remote tag, remote URI, local URI.

#### 12.1.2 UAC Behavior
When sending request that can establish dialog (INVITE), MUST provide global scope Contact (SIP/SIPS). When receiving dialog-creating response, construct state: route set from Record-Route in response (reverse order), remote target from Contact of response, local sequence number from CSeq of request, remote sequence number empty, Call-ID, local tag from From, remote tag from To, remote URI from To, local URI from From.

### 12.2 Requests within a Dialog
Either UA may initiate new transactions. Requests may contain Record-Route and Contact but do not modify route set. Target refresh requests (re-INVITE) update remote target URI.

#### 12.2.1 UAC Behavior
- **Generating the Request**: To URI = remote URI, To tag = remote tag; From URI = local URI, From tag = local tag; Call-ID = dialog Call-ID; CSeq monotonically increasing (increment local sequence number by one). Use remote target and route set to build Request-URI and Route. If route set empty, Request-URI = remote target, no Route. If first Route contains lr, Request-URI = remote target, Route = route set. If first Route no lr, Request-URI = first Route value (strip disallowed params), Route = remainder plus remote target. Target refresh requests SHOULD include Contact (same URI as previous unless changed).
- **Processing Responses**: 3xx response handled as outside dialog (Section 8.1.3.4). 2xx to target refresh replaces remote target. 481/408/timeout: SHOULD terminate dialog.

#### 12.2.2 UAS Behavior
If request has To tag, compute dialog ID and match existing dialogs. If no match, UAS MAY accept or reject (481). Process CSeq: if sequence number lower than remote sequence number, reject with 500. If higher, set remote sequence number. Target refresh requests replace remote target with Contact header from request.

### 12.3 Termination of a Dialog
Non-2xx final response terminates early dialogs. BYE terminates confirmed dialog and associated session.

## 13. Initiating a Session
INVITE request establishes a session and creates a dialog. Multiple 2xx responses from forking create multiple dialogs.

### 13.1 Overview
UAC sends INVITE, UAS may send provisional (1xx) and final response (2xx, 3xx-6xx). ACK for 2xx generated by UAC core; for 3xx-6xx by transaction layer.

### 13.2 UAC Processing
#### 13.2.1 Creating the Initial INVITE
Follow Section 8.1.1. Allow header SHOULD be present. Supported header SHOULD be present. Accept MAY be present. Expires header MAY be used to limit validity. Message body (session description) using offer/answer model (SDP). Rules for offer/answer: initial offer in INVITE or first reliable non-failure message; answer in 2xx or ACK. SDP MUST be supported. Content-Disposition for session description is "session".

#### 13.2.2 Processing INVITE Responses
- **1xx**: Provisional with To tag creates early dialogs.
- **3xx**: UAC MAY try new addresses.
- **4xx-6xx**: Single non-2xx final response terminates all early dialogs. ACK generated by transaction.
- **2xx**: Each 2xx creates/confirms dialog. UAC core generates ACK (same CSeq number, method ACK, same credentials). ACK sent directly to transport, not via transaction. Transaction considered completed 64*T1 after first 2xx.

### 13.3 UAS Processing
#### 13.3.1 Processing the INVITE
Perform Section 8.2 checks. If Expires header present, set timer. If mid-dialog, apply Section 12.2.2. If outside dialog and contains offer, answer required in 2xx. If no offer, offer must be in first reliable non-failure message (2xx).
- **Progress**: 1xx responses (except 100) establish early dialogs. To prevent proxy cancellation, send non-100 provisional every minute.
- **Redirect**: 3xx response with Contact.
- **Reject**: 486/600, or 488 if offer not acceptable.
- **Accept**: 2xx response. MUST contain Allow, Supported, and MAY contain Accept. If offer from INVITE, 2xx MUST contain answer. If no offer, 2xx MUST contain offer. Retransmit 2xx with exponential backoff (starting T1, doubling to T2) until ACK received or 64*T1 expires. If no ACK, send BYE.

## 14. Modifying an Existing Session
Using re-INVITE within the same dialog. Either party can modify session.

### 14.1 UAC Behavior
Same offer/answer model. Full session description sent. UAC MUST NOT initiate new INVITE while another INVITE transaction is in progress in either direction. If non-2xx final response to re-INVITE, session parameters unchanged. If 491, start random timer (owner of Call-ID: 2.1-4s; non-owner: 0-2s), then retry.

### 14.2 UAS Behavior
If second INVITE received before final response to first on same dialog, return 500 with Retry-After (0-10s). If INVITE received while own INVITE in progress, return 491. Check session description version; if changed, adjust session. If not acceptable, reject with 488 (including Warning). If 2xx sent but no ACK, send BYE.

## 15. Terminating a Session
BYE terminates the session and dialog. Non-2xx final response to INVITE terminates all associated sessions/dialogs. BYE must be sent within a dialog. Callee’s UA must not send BYE on early dialog, and must not send BYE on confirmed dialog until after receiving ACK for 2xx or server transaction timeout.

### 15.1 Terminating a Session with a BYE Request
#### 15.1.1 UAC Behavior
Construct as any request within dialog. Pass to non-INVITE client transaction. Consider session terminated immediately after passing BYE to transaction. If 481, 408, or timeout, consider session/dialog terminated.

#### 15.1.2 UAS Behavior
If BYE does not match existing dialog, generate 481. Otherwise, follow Section 12.2.2, terminate session (except multicast), generate 2xx response.

## 16. Proxy Behavior

### 16.1 Overview
Proxy routes SIP requests. Can be stateful or stateless. Stateful proxies may fork and must handle retransmissions. Stateless proxies forward without state.

### 16.2 Stateful Proxy
Uses server transaction for incoming request, creates client transactions for each outgoing request. Proxy core collects responses. SHOULD NOT generate 100 for non-INVITE.

### 16.3 Request Validation
Before proxying, MUST:
1. Reasonable syntax check (unknown methods/headers allowed)
2. URI scheme check: if not understood, 416
3. Max-Forwards check: if 0, don't forward (except OPTIONS may respond); else decrement
4. Optional loop detection: if sent-by matches and branch parameter identical, loop -> 482; else spiral continues
5. Proxy-Require check: if unsupported option-tag, 420 with Unsupported
6. Proxy-Authorization check: per Section 22.3

### 16.4 Route Information Preprocessing
If Request-URI contains a value proxy previously placed in Record-Route, replace Request-URI with last Route value and remove that Route. If Request-URI has maddr parameter matching proxy, strip maddr and non-default port/transport. If first Route indicates this proxy, remove it.

### 16.5 Determining Request Targets
If Request-URI has maddr, target set = that URI. If domain not responsible for, target set = Request-URI. If responsible, use location service to build target set (canonicalize if using registrar data). Any URI must not be added more than once. If target set empty, return error (480 recommended). May continue adding targets after forwarding begins (e.g., from redirect responses).

### 16.6 Request Forwarding
For each target:
1. Copy received request
2. Replace Request-URI with target URI
3. Decrement Max-Forwards (or add with 70 if absent)
4. Optionally add Record-Route header (with lr parameter) before any existing Record-Route
5. Add any other header fields
6. Postprocess routing: push local policy proxies (with lr) into Route. If first Route exists without lr, place Request-URI at end of Route, then first Route into Request-URI and remove that Route.
7. Determine next-hop address, port, transport via [4] applied to first Route (if present) or Request-URI. If SIPS, use TLS.
8. Add Via header with unique branch (starting with "z9hG4bK"; for loop detection, include hash of To tag, From tag, Call-ID, Request-URI, topmost Via, CSeq, Proxy-Require, Proxy-Authorization).
9. Add Content-Length if needed for stream transport
10. Forward via new client transaction
11. Set timer C (for INVITE) > 3 minutes

### 16.7 Response Processing
When response received, match to client transaction. If no match, process statelessly. Steps:
1. Find response context
2. Update timer C for provisional (101-199)
3. Remove topmost Via
4. Add response to context (for 3xx, optionally recurse on contacts)
5. Check for immediate forwarding: provisional (except 100) and 2xx MUST be forwarded immediately; 6xx triggers CANCELs, not forwarded immediately.
6. Choose best final response when all client transactions terminated: prefer 6xx, else lowest class.
7. Aggregate WWW-Authenticate/Proxy-Authenticate from multiple 401/407
8. Optionally rewrite Record-Route values (especially for TLS/non-TLS transitions)
9. Forward response via server transaction; if server transaction unavailable, forward statelessly
10. Generate CANCEL for all pending client transactions after forwarding final response

### 16.8 Processing Timer C
If timer C fires, reset or terminate client transaction. If provisional received, generate CANCEL; else treat as 408.

### 16.9 Handling Transport Errors
If request forwarding fails, treat as 503. If response forwarding fails, drop response; SHOULD NOT cancel other transactions.

### 16.10 CANCEL Processing
Stateful proxy receiving CANCEL: if matching response context found, return 200 (OK) and generate CANCEL for all pending client transactions. If no context, forward statelessly.

### 16.11 Stateless Proxy
No transaction state. Do not generate 100. Must choose one and only one target from target set (deterministic based on message fields). Branch parameter computed from retransmission-invariant properties; RECOMMENDED: hash of existing branch (if starts with magic cookie) or hash of topmost Via, To tag, From tag, Call-ID, CSeq, Request-URI. Record-Route and Route transformations must be identical for retransmissions. For responses: remove topmost Via if sent-by matches proxy; else discard.

### 16.12 Summary of Proxy Route Processing
1. If Request-URI owned by proxy, replace with location service result.
2. If topmost Route indicates this proxy, remove it.
3. Forward to next Route or Request-URI using [4].

#### 16.12.1 Examples
- **Basic SIP Trapezoid**: Record-Route added by each proxy; endpoints use route set for subsequent requests.
- **Strict-Routing Proxy**: Proxy without lr parameter reformats request; subsequent proxies restore Request-URI.
- **Rewriting Record-Route**: Proxy in different namespaces rewrites URI in response to provide correct routing.

## 17. Transactions
A transaction consists of request and all responses (including ACK for non-2xx to INVITE). INVITE transaction with 2xx has separate ACK transaction.

### 17.1 Client Transaction
TU passes request and destination address/port/transport. Two state machines: INVITE and non-INVITE.

#### 17.1.1 INVITE Client Transaction
States: Calling, Proceeding, Completed, Terminated.
- Timer A: retransmit INVITE (doubling intervals, starting T1=500ms).
- Timer B: timeout after 64*T1.
- On provisional (1xx): transition to Proceeding, stop retransmits.
- On 300-699: transition to Completed, generate ACK (via transport), start timer D (32s for unreliable, 0 for reliable).
- On retransmission of final response: resend ACK.
- On 2xx: transition to Terminated, pass to TU (UAC core generates ACK).
- Timer D fires: transition to Terminated.

#### 17.1.2 Non-INVITE Client Transaction
States: Trying, Proceeding, Completed, Terminated.
- Timer F: timeout 64*T1.
- Timer E: retransmit request with exponential backoff capped at T2=4s.
- On provisional: transition to Proceeding, continue retransmits (but at interval T2).
- On final: transition to Completed, set timer K (T4=5s for unreliable), then Terminated.

#### 17.1.3 Matching Responses to Client Transactions
Match if: (1) branch parameter in top Via matches the request's branch, AND (2) method in CSeq matches request method. (For ACK matching see separate rules.)

#### 17.1.4 Handling Transport Errors
Inform TU of transport failure, transition to Terminated.

### 17.2 Server Transaction
#### 17.2.1 INVITE Server Transaction
States: Proceeding, Completed, Confirmed, Terminated.
- On request: generate 100 Trying (unless TU will respond within 200ms). Pass request to TU.
- On provisional (1xx): pass to transport (no retransmits).
- On 2xx: pass to transport, transition to Terminated.
- On 300-699: transition to Completed, set timer G (T1, doubling to T2), timer H (64*T1). Retransmit response on timer G and on request retransmission.
- On ACK: transition to Confirmed, set timer I (T4). Absorb subsequent ACKs.
- Timer H fires: transition to Terminated, indicate failure to TU.

#### 17.2.2 Non-INVITE Server Transaction
States: Trying, Proceeding, Completed, Terminated.
- On request: pass to TU.
- On provisional: transition to Proceeding, send response.
- On final: transition to Completed, set timer J (64*T1 for unreliable, 0 for reliable). Retransmit final response on request retransmission.
- Timer J fires: transition to Terminated.

#### 17.2.3 Matching Requests to Server Transactions
If branch parameter starts with "z9hG4bK", match on branch, sent-by, and method. For backwards compatibility (no magic cookie), match on Request-URI, To tag, From tag, Call-ID, CSeq, top Via. ACK matches if Request-URI, From tag, Call-ID, CSeq number, top Via match INVITE, and To tag matches response's To tag.

#### 17.2.4 Handling Transport Errors
Inform TU of failure, transition to Terminated.

## 18. Transport
Responsible for sending/receiving messages over network transports. All SIP elements MUST implement UDP and TCP.

### 18.1 Clients
#### 18.1.1 Sending Requests
If request is within 200 bytes of path MTU or >1300 bytes and MTU unknown, MUST use TCP (or other congestion-controlled transport). Update top Via accordingly. For multicast, add maddr and ttl parameters. Client transport inserts sent-by (IP/hostname and port) into Via. For reliable transports, response expected on same connection; server may open new connection to source IP.

#### 18.1.2 Receiving Responses
If sent-by in top Via does not match configured value, discard. Otherwise, attempt to match to client transaction; if no match, pass to core.

### 18.2 Servers
#### 18.2.1 Receiving Requests
Server SHOULD listen on default SIP ports (5060 UDP/TCP, 5061 TLS). After receiving request, add "received" parameter to top Via if sent-by host is domain or IP differs from source. Attempt to match server transaction; if no match, pass to core.

#### 18.2.2 Sending Responses
Use top Via to determine destination: if reliable transport, reuse existing connection; if maddr present, send to that address; else if received parameter exists, send to that address with sent-by port; else send to sent-by address.

### 18.3 Framing
For datagram transports: Content-Length indicates body length; extra bytes discarded. For stream transports: Content-Length MUST be present.

### 18.4 Error Handling
ICMP errors (unreachable, etc.) SHOULD inform transport user. Source quench and TTL exceeded ignored. Connection failures for reliable transports SHOULD inform transport user.

## 19. Common Message Components

### 19.1 SIP and SIPS Uniform Resource Indicators
SIP URI: `sip:user:password@host:port;uri-parameters?headers`. SIPS URI same with scheme "sips". URI parameters include transport, maddr, ttl, user, method, lr. Headers appended via "?" mechanism.

#### 19.1.1 SIP and SIPS URI Components
Table 1 specifies mandatory/optional/not allowed for each context (Request-URI, To, From, Contact, Route/Record-Route, external). Default values for port, transport.

#### 19.1.2 Character Escaping Requirements
Characters not in valid BNF must be escaped. Telephone-subscriber fields have special escaping.

#### 19.1.3 Example SIP and SIPS URIs
Examples provided.

#### 19.1.4 URI Comparison
Rules for equivalence: scheme must match, userinfo case-sensitive, others case-insensitive. Order of parameters/headers not significant. Escaped/unreserved characters equivalent. IP and hostname not equivalent. Components with default values: omission vs explicit default not equivalent. Certain parameters ignored if in only one URI (except user, ttl, method, maddr). Headers must match if present.

#### 19.1.5 Forming Requests from a URI
Implementation MUST include transport, maddr, ttl, user parameters in Request-URI. Method parameter used as method. Unknown parameters placed in Request-URI. SHOULD honor headers but NOT honor dangerous headers (From, Call-ID, CSeq, Via, Record-Route). SHOULD NOT honor Route to avoid misuse. MUST NOT send if extension unsupported.

#### 19.1.6 Relating SIP URIs and tel URLs
When converting tel URL, entire telephone-subscriber field (including parameters) goes into userinfo of SIP URI. Equivalent tel URLs may produce non-equivalent SIP URIs; recommended to fold case-insensitive parts to lowercase and order parameters lexically.

### 19.2 Option Tags
Unique identifiers for SIP extensions, used in Require, Proxy-Require, Supported, Unsupported headers. Defined in standards-track RFCs; IANA registry maintained.

### 19.3 Tags
Used in To and From for dialog identification. MUST be globally unique and cryptographically random with at least 32 bits of randomness. A UA must use different tags for From and To in same dialog (to allow self-invitation). Algorithm implementation-specific.

## 20. Header Fields (Partial)
Syntax and definitions for each header field. "Where" column indicates request/response applicability; "proxy" column indicates proxy behavior. (Detailed descriptions for each header field are in the original RFC; for compression, we note that the full set is defined with mandatory and optional status for each method.)

*(Further sections continue with header field definitions, response codes, security, ABNF, etc., but these are in the remainder of the document not provided in this chunk.)*

## Requirements Summary (Key "shall" statements from this chunk)
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | SIP version MUST be "SIP/2.0" | MUST | 7.1 |
| R2 | SIP messages MUST be terminated by CRLF | MUST | 7 |
| R3 | Call-ID MUST be globally unique over space and time | MUST | 8.1.1.4 |
| R4 | Via branch parameter MUST start with "z9hG4bK" | MUST | 8.1.1.7 |
| R5 | Max-Forwards SHOULD be 70 | SHOULD | 8.1.1.6 |
| R6 | UAC MUST include To, From, CSeq, Call-ID, Max-Forwards, Via in requests | MUST | 8.1.1 |
| R7 | UAS MUST generate 405 if method recognized but not supported | MUST | 8.2.1 |
| R8 | UAS MUST add tag to To in response if request had no To tag (except 100) | MUST | 8.2.6.2 |
| R9 | Registrar MUST ignore Record-Route in REGISTER | MUST | 10.3 |
| R10 | Proxy MUST validate request before proxying (steps 1-6) | MUST | 16.3 |
| R11 | Stateful proxy MUST set timer C > 3 minutes for proxied INVITE | MUST | 16.6 |
| R12 | Client transaction for INVITE MUST start timer A = T1 on unreliable transport | MUST | 17.1.1.2 |
| R13 | Server transaction for INVITE MUST generate 100 Trying unless TU will respond within 200ms | MUST | 17.2.1 |
| R14 | All SIP elements MUST implement UDP and TCP | MUST | 18 |

## Informative Annexes (Condensed)
- **Section 4 Overview of Operation**: Describes typical call flow with SIP trapezoid, INVITE/200/ACK three-way handshake, registration. Tutorial only, no normative statements.
- **Section 5 Structure of the Protocol**: Explains layered model (syntax, transport, transaction, TU). Not an implementation prescription.
- **Remaining sections not in this chunk** (e.g., S/MIME, security, ABNF) are for further processing.

## 19.1.1 URI Parameters
- **parameter-name "=" parameter-value**: Any given **parameter-name MUST NOT appear more than once** in a URI.
- Defined parameters: transport, maddr, ttl, user, method, lr.
- **transport**: Determines transport mechanism (UDP, TCP, SCTP). For SIPS URI, **transport parameter MUST indicate a reliable transport**.
- **maddr**: Overrides host-derived address. Used for loose source routing, but **maddr for routing is deprecated**; implementations should use Route mechanism (Section 8.1.1.1).
- **ttl**: Time-to-live for UDP multicast. **MUST only be used if maddr is multicast and transport is UDP**.
- **user**: Distinguishes telephone numbers from usernames. If user string is a telephone-subscriber, **"phone" SHOULD be present**. Recipients **MAY interpret** pre-@ part as telephone number.
- **method**: Specifies method of SIP request.
- **lr**: Indicates element implements routing mechanisms defined in this document (for Record-Route backwards compatibility).
- **Unknown uri-parameters**: **SIP elements MUST silently ignore** any uri-parameters they do not understand.

## 19.1.2 Character Escaping Requirements
- SIP follows RFC 2396; characters reserved or excluded **MUST be escaped**.
- Host component: **Escaped characters not allowed in host** (current implementations MUST NOT treat received escaped characters as equivalent to unescaped).
- Telephone-subscriber characters not in BNF for `user` **MUST be escaped**.

## 19.1.3 Example SIP and SIPS URIs
- Provided examples (e.g., `sip:alice@atlanta.com`, `sips:alice@atlanta.com?subject=project%20x`). The user field is opaque.

## 19.1.4 URI Comparison
- **SIP and SIPS URIs are never equivalent**.
- **userinfo comparison is case-sensitive**; all other components case-insensitive unless specified.
- **Order of parameters and header fields not significant**.
- **Characters equivalent to their % HEX HEX encoding** (except reserved set).
- **IP address from DNS lookup does not match host name**.
- **For equality: user, password, host, port must match**.
- **Omitting a component with default value does not match URI explicitly containing that component with default**.
- **uri-parameter comparison**:
  - Any uri-parameter appearing in both must match.
  - `user`, `ttl`, `method` parameters appearing in only one never match.
  - `maddr` in only one never matches.
  - All other uri-parameters in only one are ignored.
- **URI header components**: Must be present in both and match; see Section 20 for each header.
- Examples of equivalent and non-equivalent URIs provided.

## 19.1.5 Forming Requests from a URI
- **Implementation MUST include transport, maddr, ttl, or user parameter in Request-URI**.
- If `method` parameter present, its value **MUST be used as method** and **MUST NOT be placed in Request-URI**.
- **Unknown URI parameters MUST be placed in Request-URI**.
- **SHOULD treat presence of headers or body parts** as desire to include; honor per-component.
- **SHOULD NOT honor dangerous header fields** (From, Call-ID, CSeq, Via, Record-Route).
- **SHOULD NOT honor Route header field** to avoid unwitting agent in attacks.
- **SHOULD NOT honor header fields causing false advertisement** (e.g., Accept, Contact, User-Agent).
- **SHOULD verify accuracy of descriptive header fields** (Content-*, Date, MIME-Version, Timestamp).
- If request is invalid, **MUST NOT proceed**; treat as invalid URI.
- **SHOULD refuse to send requests requiring unimplemented capabilities**.
- **MUST NOT send request requiring unsupported extension**.

## 19.1.6 Relating SIP URIs and tel URLs
- When converting tel URL to SIP/SIPS URI, entire telephone-subscriber portion placed into userinfo.
- Equivalent tel URLs may produce non-equivalent SIP URIs due to case-sensitive comparison and parameter ordering.
- **SHOULD fold case-insensitive portions to lower case and order parameters lexically** (except isdn-subaddress and post-dial first).

## 19.2 Option Tags
- Unique identifiers for new extensions (standards track RFCs only).
- Used in Require, Proxy-Require, Supported, Unsupported header fields.
- IANA registry.

## 19.3 Tags
- `tag` parameter in To and From header fields for dialog identification.
- When generated, **MUST be globally unique and cryptographically random** with at least 32 bits of randomness.
- Different tags for From and To of same dialog; different for different calls.

## 20 Header Fields
- General syntax per Section 7.3.
- Tables 2 and 3 summarize header field usage by method and proxy operations.
- **Where column**: R (request), r (response), c (copied), numeric (response codes).
- **Proxy column**: a (add), m (modify), d (delete), r (read – not encrypted).
- **Method columns**: m (mandatory), m* (SHOULD send), o (optional), t (required if TCP), * (required if body not empty), - (not applicable), c (conditional).
- **Mandatory fields must be present and understood**; optional fields may be ignored.
- **SHOULD ignore extension header parameters not understood**.
- Compact forms defined for common headers.
- Contact, From, To: if URI contains comma, question mark, or semicolon, **MUST be enclosed in angle brackets**.

### 20.1 Accept
- Syntax per [H14.1]; default `application/sdp` if absent.
- Empty means no formats acceptable.

### 20.2 Accept-Encoding
- Default identity (no encoding) if absent; empty means only identity acceptable.

### 20.3 Accept-Language
- Default all languages if absent.

### 20.4 Alert-Info
- Alternative ring tone (INVITE) or ringback (180 response); security risks similar to Call-Info; user should be able to disable.

### 20.5 Allow
- Lists supported methods; if present, **MUST include all methods understood** (including ACK, CANCEL); absence implies no information.

### 20.6 Authentication-Info
- Mutual authentication; may be included in 2xx response to successful digest authentication.

### 20.7 Authorization
- Contains credentials; may appear multiple times, **MUST NOT be combined** into single header line.

### 20.8 Call-ID
- Uniquely identifies invitation/registration; case-sensitive, byte-by-byte comparison. Compact form `i`.

### 20.9 Call-Info
- Provides additional info (icon, info, card). Security: **RECOMMENDED** to render only if originator verified and trusted.

### 20.10 Contact
- Contains URI; parameters `q` and `expires` used in REGISTER/3xx.
- Parsing rules for display name, URI, parameters.

### 20.11 Content-Disposition
- Describes interpretation of body part. New disposition types: `session`, `render`, `icon`, `alert`.
- Default: `session` for application/sdp; `render` for others.
- `handling` parameter: `optional`/`required`; default required.
- Rendered content should only be processed if properly authenticated.

### 20.12 Content-Encoding
- Applied codings listed in order; compact form `e`.

### 20.13 Content-Language
- Per [H14.12].

### 20.14 Content-Length
- Size in octets; **SHOULD be used**; **MUST be used** for stream-based protocol. No body: value **MUST be zero**. Compact form `l`.

### 20.15 Content-Type
- **MUST be present if body not empty**; if empty and present, indicates zero-length body. Compact form `c`.

### 20.16 CSeq
- Sequence number and method; **MUST be expressible as 32-bit unsigned integer**; case-sensitive method.

### 20.17 Date
- RFC 1123 format; time zone **MUST be "GMT"**; case-sensitive.

### 20.18 Error-Info
- Pointer to additional error information; SIP or SIPS URI may be treated as redirect; non-SIP URI may be rendered.

### 20.19 Expires
- Relative time in seconds (0 to 2^32-1) from receipt.

### 20.20 From
- Initiator; `display-name` optional; if identity hidden, SHOULD use "Anonymous". Compact form `f`.

### 20.21 In-Reply-To
- Lists Call-IDs referenced/returned.

### 20.22 Max-Forwards
- **MUST be used** with any SIP method; integer 0-255; decremented by each forwarding server; recommended initial value 70.

### 20.23 Min-Expires
- Minimum refresh interval; used in 423 responses.

### 20.24 MIME-Version
- Per [H19.4.1].

### 20.25 Organization
- Organization name; may be used for call filtering.

### 20.26 Priority
- Urgency: non-urgent, normal, urgent, emergency; default normal; does not affect network priority.

### 20.27 Proxy-Authenticate
- Authentication challenge from proxy.

### 20.28 Proxy-Authorization
- Client credentials for proxy; may appear multiple times, **MUST NOT be combined**.

### 20.29 Proxy-Require
- Indicates proxy-sensitive features required.

### 20.30 Record-Route
- Forces future requests in dialog to be routed through proxy.

### 20.31 Reply-To
- Logical return URI; if anonymity desired, **SHOULD be omitted or not reveal private info**.

### 20.32 Require
- Lists option tags that **MUST be understood**; **MUST NOT be ignored** if present. Only standards-track tags.

### 20.33 Retry-After
- Time to retry; optional comment and `duration` parameter.

### 20.34 Route
- Forces routing through listed set of proxies.

### 20.35 Server
- Software version; **SHOULD be configurable** for security.

### 20.36 Subject
- Summary or nature of call; compact form `s`.

### 20.37 Supported
- Lists extensions supported; only standards-track tags; compact form `k`.

### 20.38 Timestamp
- When UAC sent request; allows RTT estimates.

### 20.39 To
- Logical recipient; `tag` for dialog identification. Compact form `t`.

### 20.40 Unsupported
- Lists features not supported.

### 20.41 User-Agent
- UAC software; **SHOULD be configurable**.

### 20.42 Via
- Path taken; `branch` parameter **MUST start with magic cookie "z9hG4bK"**; compact form `v`.

### 20.43 Warning
- Additional info about response status; defined warn-codes (300-399).

### 20.44 WWW-Authenticate
- Authentication challenge from UAS/registrar.

## 21 Response Codes
- Extends HTTP/1.1; new class 6xx.
- Provisional (1xx): 100, 180, 181, 182, 183.
- Success (2xx): 200.
- Redirection (3xx): 300, 301, 302, 305, 380.
- Client-Error (4xx): 400-416, 420, 421, 423, 480-488, 491, 493.
- Server-Error (5xx): 500-505, 513.
- Global-Failure (6xx): 600, 603, 604, 606.

- **1xx responses**: indicate further action; never cause ACK; MAY contain message bodies.
- **2xx**: request successful.
- **3xx**: alternative locations; user can select.
- **4xx**: definite failure; client SHOULD NOT retry same request without modification.
- For detailed semantics of each code, see Section 21.

## 22 Usage of HTTP Authentication
- Stateless, challenge-based; based on HTTP Digest. **Basic authentication deprecated; servers MUST NOT accept or challenge with Basic**.
- UAS uses 401; proxies use 407.
- Realm string **MUST be globally unique**; **SHOULD be human-readable**.
- ACK and CANCEL not challengeable; **ACK duplicates credentials from INVITE**; **CANCEL SHOULD be accepted if from same hop**.
- UAC **SHOULD cache credentials** for realm.
- Default username "anonymous" with no password allowed.
- For proxy authentication: **proxies MUST NOT add Proxy-Authorization values**; **UAC is responsible** for adding them.
- Multiple challenges (forking) aggregated by forking proxy.
- **Servers MUST ensure backwards compatibility with RFC 2069** but MUST NOT accept Basic.
- Specific differences for SIP in Digest authentication:
  1. URI in challenge is SIP/SIPS URI.
  2. `uri` parameter **MUST be enclosed in quotation marks**.
  3. Request-URI used for digest-uri-value.
  4. Server **MAY check** that Authorization Request-URI corresponds to user it is willing to serve.
  5. When entity-body empty, `H(entity-body) = MD5("")`.
  6. `qop` parameter **MUST always be sent** in WWW-Authenticate/Proxy-Authenticate; if client receives `qop`, **MUST send `qop`** in authorization.

## 23 S/MIME
- Provides end-to-end integrity and confidentiality for MIME bodies; also for SIP header fields via tunneling (`message/sip` body).
- Certificates: subject is end-user address (e.g., user@domain).
- **Self-signed certificates allowed** but vulnerable to man-in-the-middle on first exchange.
- **UAC/UAS SHOULD validate certificates** against From/To.
- Unverified or mismatched certificates: **user MUST be notified and permission requested**.
- Key exchange: when receiving S/MIME with certificate, **SHOULD add to keyring**.
- **UA MUST notify user of certificate change**; potential security breach.
- Encrypted bodies unknown: **MUST respond with 493 (Undecipherable)**; may include own certificate.
- Content-Disposition handling parameter: if `required` and S/MIME not understood, **MUST respond 415**.
- **SHOULD use TCP when S/MIME tunneling** due to message size.

### 23.3 Securing MIME bodies
- `multipart/signed` **MUST be used only with CMS detached signatures**.
- S/MIME bodies **SHOULD have Content-Disposition with `handling=required`**.
- Minimum mandatory algorithms: SHA1, 3DES.
- **Each body SHOULD be signed with only one certificate**; outermost signature treated as single.

### 23.4 Tunneling SIP
- `message/sip` MIME type used for end-to-end integrity/confidentiality of headers.
- **SHOULD include Date header in both inner and outer**.
- Integrity: header fields modifiable by proxies (Request-URI, Via, etc.) **SHOULD NOT be considered breach**; other header changes are integrity violations; **user MUST be notified**.
- Confidentiality: encrypted header fields may differ from outer; inner values **SHOULD be displayed but NOT used in outer** of future messages.
- For anonymity, encrypted From header provides selective anonymity.

## 24 Examples
- Registration (Figure 9) and session setup (Figure 1) flows with full SIP messages omitted for brevity. See RFC for complete examples.

## 25 Augmented BNF for the SIP Protocol
- Conforms to RFC 2234. Core rules and specific BNF for SIP message structure, headers, methods, response codes, URI components, etc. Refer to Section 25 for complete grammar.

## 26 Security Considerations: Threat Model and Security Usage Recommendations
### 26.1 Attacks and Threat Models
- **Registration Hijacking**: Attacker impersonates user to modify contact addresses.
- **Impersonating a Server**: Attacker forges responses (e.g., redirect) to direct traffic elsewhere.
- **Tampering with Message Bodies**: Modification of SDP or session keys.
- **Tearing Down Sessions**: Forged BYE request.
- **Denial of Service and Amplification**: Flooding via spoofed Via/Route/Record-Route.

### 26.2 Security Mechanisms
- **Transport/Network Layer Security**: TLS (mandatory for proxies, redirect servers, registrars) and IPSec.
- **SIPS URI Scheme**: Mandates TLS on every hop to target domain.
- **HTTP Authentication**: Digest based, provides replay protection and one-way authentication.
- **S/MIME**: End-to-end for MIME bodies; optional.

### 26.3 Implementing Security Mechanisms
- **Requirements**: Proxies/registrars **MUST implement TLS** with mutual and one-way authentication; **SHOULD possess site certificates**. All TLS-capable elements **MUST support SIPS URI**. **MUST implement Digest Authorization**.
- Registration: UA **SHOULD establish TLS with registrar**; registrar **SHOULD offer certificate**; UA **MUST NOT send REGISTER if certificate invalid**.
- Interdomain: Proxies **SHOULD use mutual TLS**; should verify domain names.
- Peer-to-peer: UA without proxy **SHOULD use TLS with remote proxy**; S/MIME for end-to-end.
- DoS protection: Use single challenge (1xx/407 without retransmission); bastion hosts.

### 26.4 Limitations
- **HTTP Digest**: Weak integrity; replay protection limited; realm scope.
- **S/MIME**: Lack of public key infrastructure; man-in-the-middle on first key exchange; large messages.
- **TLS**: Requires TCP; scalability; hop-by-hop only.
- **SIPS URIs**: Not truly end-to-end; location services may return non-SIPS; downgrade attacks possible.

### 26.5 Privacy
- Sensitive info in headers; location service should restrict per-user; optional To header different from Request-URI.

## 27 IANA Considerations
- Creates four sub-registries: Option Tags, Warning Codes, Methods, Response Codes. Also registers Header Field names and `message/sip` MIME type.
- Option tags: registered in standards track RFCs; name <=20 alphanum.
- Warn-codes: 3xx for SDP problems.
- Header field names: optional one-letter compact forms after WG review.
- Method and response code registrations require RFC number and default reason phrase.
- `message/sip` MIME type registered (version optional, default 2.0).
- New Content-Disposition types: `alert`, `icon`, `session`, `render` registered.

## 28 Changes From RFC 2543
### 28.1 Major Functional Changes
- CANCEL/INVITE separated; BYE only on existing dialog.
- BNF converted to RFC 2234.
- URI comparison simplified; parameters with default values affect matching.
- Removed Via hiding; forking proxy now collects all challenges.
- Digest URI must be quoted.
- SDP processing formalized as offer/answer.
- Full IPv6 support.
- DNS SRV documented separately.
- Loop detection optional; Max-Forwards mandatory.
- Tags mandatory.
- Added Supported header.
- Route/Record-Route reworked; backwards compatibility.
- CRLF only (not CR or LF).
- Branch parameter mandatory with magic cookie.
- TCP connection closure no longer equivalent to CANCEL.
- PGP replaced with S/MIME.
- Added "sips" URI scheme.
- Provisional forwarding mandatory.
- 503 handling clarified.
- Mutual authentication procedures allowed.
- Various race condition fixes.

### 28.2 Minor Functional Changes
- Added Alert-Info, Error-Info, Call-Info, Content-Language, Content-Disposition, MIME-Version.
- Glare handling with 491.
- In-Reply-To and Reply-To.
- TLS and SCTP transports.
- Unified failure handling.
- Retransmission changes (only 2xx retransmitted over TCP).
- Timers based on timeouts.
- Date header for auto-config.
- Min-Expires and 423.

## Annex A: Table of Timer Values
| Timer | Value | Section | Meaning |
|-------|-------|---------|---------|
| T1 | 500 ms default | 17.1.1.1 | RTT Estimate |
| T2 | 4 s | 17.1.2.2 | Max retransmit interval for non-INVITE and INVITE responses |
| T4 | 5 s | 17.1.2.2 | Max duration a message remains in network |
| Timer A | initially T1 | 17.1.1.2 | INVITE request retransmit (UDP only) |
| Timer B | 64*T1 | 17.1.1.2 | INVITE transaction timeout |
| Timer C | > 3 min | 16.6 bullet 11 | Proxy INVITE transaction timeout |
| Timer D | > 32s UDP; 0s TCP/SCTP | 17.1.1.2 | Wait for response retransmits |
| Timer E | initially T1 | 17.1.2.2 | non-INVITE retransmit (UDP only) |
| Timer F | 64*T1 | 17.1.2.2 | non-INVITE timeout |
| Timer G | initially T1 | 17.2.1 | INVITE response retransmit |
| Timer H | 64*T1 | 17.2.1 | Wait for ACK |
| Timer I | T4 UDP; 0s TCP/SCTP | 17.2.1 | Wait for ACK retransmits |
| Timer J | 64*T1 UDP; 0s TCP/SCTP | 17.2.2 | Wait for non-INVITE request retransmits |
| Timer K | T4 UDP; 0s TCP/SCTP | 17.1.2.2 | Wait for response retransmits |

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Any given URI parameter-name MUST NOT appear more than once | shall | 19.1.1 |
| R2 | For SIPS URI, transport parameter MUST indicate reliable transport | shall | 19.1.1 |
| R3 | ttl parameter MUST only be used if maddr is multicast and transport is UDP | shall | 19.1.1 |
| R4 | SIP elements MUST silently ignore unknown uri-parameters | shall | 19.1.1 |
| R5 | Characters reserved or excluded MUST be escaped in SIP URIs | shall | 19.1.2 |
| R6 | Current implementations MUST NOT treat escaped host characters as equivalent to unescaped | shall | 19.1.2 |
| R7 | Telephone-subscriber characters not in BNF for user MUST be escaped | shall | 19.1.2 |
| R8 | SIP and SIPS URIs are never equivalent | rule | 19.1.4 |
| R9 | Implementation MUST include transport, maddr, ttl, user parameter in Request-URI | shall | 19.1.5 |
| R10 | If method parameter present, its value MUST be used as method and NOT placed in Request-URI | shall | 19.1.5 |
| R11 | Unknown URI parameters MUST be placed in Request-URI | shall | 19.1.5 |
| R12 | Implementation MUST NOT proceed with invalid URI request | shall | 19.1.5 |
| R13 | Implementation MUST NOT send request requiring unsupported extension | shall | 19.1.5 |
| R14 | Generated tag MUST be globally unique and cryptographically random with at least 32 bits | shall | 19.3 |
| R15 | Allow header, when present, MUST include all methods understood | shall | 20.5 |
| R16 | Content-Length MUST be used for stream-based protocol; MUST be zero if no body | shall | 20.14 |
| R17 | Content-Type MUST be present if body not empty | shall | 20.15 |
| R18 | CSeq sequence number MUST be expressible as 32-bit unsigned integer | shall | 20.16 |
| R19 | Max-Forwards MUST be used with any SIP method | shall | 20.22 |
| R20 | Require header field MUST NOT be ignored if present | shall | 20.32 |
| R21 | Branch parameter MUST start with magic cookie "z9hG4bK" | shall | 20.42 |
| R22 | Servers MUST NOT accept Basic authentication | shall | 22 |
| R23 | Servers MUST NOT challenge with Basic | shall | 22 |
| R24 | Proxy MUST NOT add values to Proxy-Authorization | shall | 22.3 |
| R25 | Servers MUST ensure backwards compatibility with RFC 2069 | shall | 22.4 |
| R26 | Servers MUST always send qop parameter in WWW-Authenticate/Proxy-Authenticate | shall | 22.4 |
| R27 | If client receives qop, it MUST send qop in authorization | shall | 22.4 |
| R28 | UA MUST notify user of certificate change | shall | 23.2 |
| R29 | multipart/signed MUST be used only with CMS detached signatures | shall | 23.3 |
| R30 | UA MUST reject request with 493 if S/MIME encrypted with unknown public key | shall | 23.2 |
| R31 | TLS MUST be implemented by proxy/redirect servers and registrars | shall | 26.3.1 |
| R32 | TLS-capable elements MUST support SIPS URI | shall | 26.3.1 |
| R33 | Digest Authorization MUST be implemented | shall | 26.3.1 |
| R34 | If certificate invalid, UA MUST NOT send REGISTER | shall | 26.3.2.1 |