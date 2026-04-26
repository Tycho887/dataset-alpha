# RFC 2818: HTTP Over TLS
**Source**: IETF | **Version**: Informational | **Date**: May 2000 | **Type**: Informational
**Original**: https://www.rfc-editor.org/rfc/rfc2818

## Scope (Summary)
This memo describes how to use TLS (the successor to SSL) to secure HTTP connections over the Internet. It documents the current practice of running HTTP over TLS on a separate port (443) and using the `https` URI scheme.

## Normative References
- RFC 2119: Key Words for use in RFCs to indicate Requirement Levels (BCP 14)
- RFC 2246: The TLS Protocol (January 1999)
- RFC 2459: Internet Public Key Infrastructure: Part I: X.509 Certificate and CRL Profile (January 1999)
- RFC 2616: Hypertext Transfer Protocol – HTTP/1.1 (June 1999)
- RFC 2817: Upgrading to TLS Within HTTP/1.1 (May 2000)

## Definitions and Abbreviations
- **TLS**: Transport Layer Security, as defined in RFC 2246.
- **HTTP**: Hypertext Transfer Protocol, as defined in RFC 2616.
- **MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, MAY**: Interpreted as described in RFC 2119.

## 1. Introduction
HTTP [RFC2616] was originally used in the clear. Increased use for sensitive applications required security measures. This document describes how to use HTTP over TLS.

## 2. HTTP Over TLS
Conceptually simple: use HTTP over TLS exactly as over TCP.

### 2.1. Connection Initiation
- The HTTP client **SHOULD** act as the TLS client.
- It **SHOULD** initiate a connection to the server on the appropriate port and send a TLS ClientHello.
- After the TLS handshake finishes, the client **MAY** initiate the first HTTP request.
- All HTTP data **MUST** be sent as TLS "application data".
- Normal HTTP behavior (including retained connections) **SHOULD** be followed.

### 2.2. Connection Closure
- TLS implementations **MUST** initiate an exchange of closure alerts before closing a connection.
- After sending a closure alert, a TLS implementation **MAY** close the connection without waiting for the peer’s closure alert (generating an "incomplete close").
- This **SHOULD** only be done when the application knows (e.g., from HTTP message boundaries) that all desired data has been received.
- Any implementation receiving a connection close without a valid closure alert ("premature close") **MUST NOT** reuse that session.
- A premature close indicates possible data truncation; examining HTTP Content-Length is necessary to determine if truncation occurred inside a message.

#### 2.2.1. Client Behavior
- Client implementations **MUST** treat any premature closes as errors and data as potentially truncated.
- Exception: When encountering a premature close, a client **SHOULD** treat as completed all requests for which it received as much data as specified in the Content-Length header.
- A client detecting an incomplete close **SHOULD** recover gracefully; it **MAY** resume a TLS session closed in this fashion.
- Clients **MUST** send a closure alert before closing the connection.
- Clients unprepared to receive more data **MAY** close without waiting for the server's closure alert (incomplete close on server side).

#### 2.2.2. Server Behavior
- Servers **SHOULD** be prepared to receive an incomplete close from the client.
- Servers **SHOULD** be willing to resume TLS sessions closed in this fashion.
- Servers **MUST** attempt to initiate an exchange of closure alerts with the client before closing the connection.
- Servers **MAY** close the connection after sending the closure alert (incomplete close on client side).

### 2.3. Port Number
- The default port for HTTP/TLS over TCP is 443.
- This does not preclude other transports; TLS only requires a reliable connection-oriented data stream.

### 2.4. URI Format
- HTTP/TLS URIs use the `https` protocol identifier in place of `http`. Example: `https://www.example.com/~smith/home.html`.

## 3. Endpoint Identification

### 3.1. Server Identity
- If the hostname is available (from the URI), the client **MUST** check it against the server’s identity as presented in the server's Certificate message to prevent man-in-the-middle attacks.
- If the client has external information about the expected identity, the hostname check **MAY** be omitted. In such cases, narrow the scope of acceptable certificates as much as possible.
- If a `subjectAltName` extension of type `dNSName` is present, it **MUST** be used as the identity. Otherwise, the (most specific) Common Name field in the Subject field **MUST** be used (deprecated practice).
- Matching follows the rules in RFC 2459. If multiple identities of a given type exist, a match in any one is acceptable. Wildcard character `*` matches any single domain name component or component fragment (e.g., `*.a.com` matches `foo.a.com` but not `bar.foo.a.com`; `f*.com` matches `foo.com` but not `bar.com`).
- If the URI is an IP address, the `iPAddress` subjectAltName **must** be present and exactly match the IP.
- If the hostname does not match the certificate identity:
  - User-oriented clients **MUST** either notify the user (the client **MAY** give the user the opportunity to continue) or terminate the connection with a bad certificate error.
  - Automated clients **MUST** log the error to an appropriate audit log (if available) and **SHOULD** terminate the connection with a bad certificate error. Automated clients **MAY** provide a configuration setting that disables this check but **MUST** provide a setting that enables it.
- Note: If the URI comes from an untrusted source (e.g., an unsecured HTTP page), this check provides no protection; users should carefully examine the server certificate.

### 3.2. Client Identity
- Typically, the server has no external knowledge of the client’s identity; checks beyond a certificate chain rooted in an appropriate CA are not possible.
- If the server does have such knowledge (from a source external to HTTP or TLS), it **SHOULD** check the identity as described for servers.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | HTTP data **MUST** be sent as TLS application data. | MUST | Section 2.1 |
| R2 | TLS implementations **MUST** initiate closure alert exchange before closing a connection. | MUST | Section 2.2 |
| R3 | After sending closure alert, implementation **MAY** close without waiting for peer (incomplete close). | MAY | Section 2.2 |
| R4 | Incomplete close **SHOULD** only be done when application knows all data received. | SHOULD | Section 2.2 |
| R5 | Premature close (no closure alert) **MUST NOT** reuse session. | MUST NOT | Section 2.2 |
| R6 | Clients **MUST** treat premature closes as errors, data potentially truncated. | MUST | Section 2.2.1 |
| R7 | On premature close, client **SHOULD** treat requests with full Content-Length as completed. | SHOULD | Section 2.2.1 |
| R8 | Clients detecting incomplete close **SHOULD** recover gracefully. | SHOULD | Section 2.2.1 |
| R9 | Clients **MAY** resume TLS session after incomplete close. | MAY | Section 2.2.1 |
| R10 | Clients **MUST** send closure alert before closing connection. | MUST | Section 2.2.1 |
| R11 | Clients **MAY** close without waiting for server’s closure alert (incomplete close). | MAY | Section 2.2.1 |
| R12 | Servers **SHOULD** be prepared for incomplete close from client. | SHOULD | Section 2.2.2 |
| R13 | Servers **SHOULD** be willing to resume TLS sessions after incomplete close. | SHOULD | Section 2.2.2 |
| R14 | Servers **MUST** attempt exchange of closure alerts before closing. | MUST | Section 2.2.2 |
| R15 | Servers **MAY** close after sending closure alert (incomplete close on client). | MAY | Section 2.2.2 |
| R16 | If hostname available, client **MUST** check it against server certificate identity. | MUST | Section 3.1 |
| R17 | Hostname check **MAY** be omitted if client has external identity information. | MAY | Section 3.1 |
| R18 | If subjectAltName dNSName present, that **MUST** be used as identity. | MUST | Section 3.1 |
| R19 | Otherwise, Common Name **MUST** be used (deprecated). | MUST | Section 3.1 |
| R20 | Wildcard * matches single domain name component. | (Matching rule) | Section 3.1 |
| R21 | For IP address URI, iPAddress subjectAltName **must** be present and exactly match. | must | Section 3.1 |
| R22 | User-oriented clients: on mismatch **MUST** notify user or terminate; **MAY** offer to continue. | MUST/MAY | Section 3.1 |
| R23 | Automated clients: **MUST** log error, **SHOULD** terminate; **MAY** provide disable config but **MUST** provide enable config. | MUST/SHOULD/MAY | Section 3.1 |
| R24 | If server has external knowledge of client identity, it **SHOULD** check as described. | SHOULD | Section 3.2 |

## Informative Annexes (Condensed)
- **Security Considerations**: This entire document is about security. All requirements (mandatory connection closure, identity checking, etc.) aim to prevent attacks such as man-in-the-middle and data truncation.