# RFC 2830: Lightweight Directory Access Protocol (v3): Extension for Transport Layer Security
**Source**: IETF | **Version**: Standards Track | **Date**: May 2000 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc2830

## Scope (Summary)
Defines the "Start Transport Layer Security (TLS) Operation" for LDAPv3, enabling TLS establishment within an LDAP association via an LDAP extended request/response.

## Normative References
- [AuthMeth] Wahl, M., Alvestrand, H., Hodges, J. and R. Morgan, "Authentication Methods for LDAP", RFC 2829, May 2000.
- [IPSEC] Kent, S. and R. Atkinson, "Security Architecture for the Internet Protocol", RFC 2401, November 1998.
- [LDAPv3] Wahl, M., Kille S. and T. Howes, "Lightweight Directory Access Protocol (v3)", RFC 2251, December 1997.
- [ReqsKeywords] Bradner, S., "Key Words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [SASL] Myers, J., "Simple Authentication and Security Layer (SASL)", RFC 2222, October 1997.
- [TLS] Dierks, T. and C. Allen. "The TLS Protocol Version 1.0", RFC 2246, January 1999.

## Definitions and Abbreviations
- **Start TLS extended request**: An LDAP ExtendedRequest with requestName OID 1.3.6.1.4.1.1466.20037 and no requestValue.
- **Start TLS extended response**: An LDAP ExtendedResponse with responseName set to the same OID as the request.
- **LDAP association**: A TCP connection over which LDAP PDUs are exchanged.
- **Authorization identity**: As defined in [AuthMeth].
- **TLS**: Transport Layer Security Protocol, as defined in [TLS].
- **SASL EXTERNAL**: A SASL mechanism for using external authentication credentials, as defined in [SASL].

## 1. Conventions Used in this Document
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [ReqsKeywords].

## 2. The Start TLS Request
### 2.1. Requesting TLS Establishment
- **OID**: The Start TLS operation OID is `1.3.6.1.4.1.1466.20037`.
- **Request formation**: Set requestName to the OID; requestValue is absent. The client MUST NOT send any PDUs on this connection following this request until it receives a Start TLS extended response.
- **Server response**: The server MUST return an LDAP PDU containing a Start TLS extended response. The response MUST contain a responseName field set to the same string as in the request. The response field is absent. The server MUST set the resultCode to either success or one of the values in section 2.3.

### 2.2. "Success" Response
- **resultCode success**: Indicates the server is willing and able to negotiate TLS (see section 3).

### 2.3. Response other than "success"
- **Error codes**:
  - `operationsError`: Sequencing incorrect (e.g., TLS already established).
  - `protocolError`: TLS not supported or incorrect PDU structure.
  - `referral`: This server does not do TLS; the server MUST include an actual referral value.
  - `unavailable`: Major problem with TLS or server shutting down.
- **MUST requirements**:
  - Server MUST return `operationsError` if the client violates sequencing requirements from section 3.
  - If server does not support TLS, it MUST set resultCode to `protocolError` or `referral`. Client's current session is unaffected; MAY proceed with any LDAP operation or close.
  - If server supports TLS but cannot establish connection, MUST return `unavailable`. Client MAY retry StartTLS, proceed with other operations, or close.

## 3. Sequencing of the Start TLS Operation
### 3.1. Requesting to Start TLS on an LDAP Association
- **General**: Client MAY send the Start TLS extended request at any time after establishing an LDAP association, except that the client MUST NOT send a Start TLS request:
  - if TLS is currently established,
  - during a multi-stage SASL negotiation,
  - if there are any LDAP operations outstanding.
- **Violation**: Server MUST return `operationsError`.
- **Prior Bind**: Client MAY have already performed a Bind or not.
- **Server requirement**: If server requires TLS before a particular request, it MUST reject that request with `confidentialityRequired` or `strongAuthRequired`. Client MAY send Start TLS or close.

### 3.2. Starting TLS
- **Successful case**: Server returns resultCode success. Client MUST either begin TLS negotiation or close the connection.
- **TLS negotiation**: Client sends TLS Record Protocol PDUs directly over the transport connection [TLS].

### 3.3. TLS Version Negotiation
- Negotiation of TLS/SSL version is part of the TLS Handshake Protocol [TLS].

### 3.4. Discovery of Resultant Security Level
- **Party decision**: After TLS establishment, both client and server MUST individually decide whether to continue based on the privacy level achieved. Ascertaining privacy level is implementation dependent.
- **Insufficient security**: If either decides the level is not high enough, it SHOULD gracefully close the TLS connection immediately after negotiation completes (see sections 4.1 and 5.2). Client MAY attempt Start TLS again, send unbind, or any other LDAP request.

### 3.5. Assertion of Client's Authorization Identity
- Client MAY, upon receipt of a Start TLS success response, assert a specific authorization identity via an LDAP Bind request using SASL mechanism "EXTERNAL" [SASL] (see section 5.1.2).

### 3.6. Server Identity Check
- **Requirement**: The client MUST check its understanding of the server's hostname against the server's identity in the certificate to prevent man-in-the-middle attacks.
- **Rules**:
  - The client MUST use the server hostname used to open the LDAP connection. MUST NOT use canonical DNS name or derived form.
  - If a subjectAltName extension of type dNSName is present, it SHOULD be used.
  - Matching is case-insensitive.
  - The "*" wildcard is allowed, applying only to the left-most name component. E.g., `*.bar.com` matches `a.bar.com`, `b.bar.com`, but not `bar.com`. If multiple dNSName names, a match in any one is acceptable.
  - If hostname does not match, user-oriented clients SHOULD either notify the user (clients MAY give the user the opportunity to continue) or terminate and indicate suspicious identity. Automated clients SHOULD close and log an error.
- **Further checks**: Clients SHOULD be prepared to check that the server is authorized to provide the service, possibly using local policy.

### 3.7. Refresh of Server Capabilities Information
- **Requirement**: The client MUST refresh any cached server capabilities information (e.g., root DSE) upon TLS session establishment. Server MAY advertise different capabilities after TLS.

## 4. Closing a TLS Connection
### 4.1. Graceful Closure
- Either party MAY terminate TLS by sending a TLS closure alert; LDAP association remains intact.
- Before closing, client MUST either wait for outstanding LDAP operations to complete or explicitly abandon them [LDAPv3].
- After sending closure alert, initiator MUST discard any TLS messages until receiving an alert from the other party. Following receipt, MAY send and receive LDAP PDUs.
- Receiver of a closure alert MUST immediately transmit a TLS closure alert, then cease TLS Record Protocol PDUs and MAY send/receive LDAP PDUs.

### 4.2. Abrupt Closure
- Either party MAY abruptly close the entire LDAP association and any TLS connection by dropping the underlying TCP connection. Server MAY beforehand send a Notice of Disconnection [LDAPv3].

## 5. Effects of TLS on a Client's Authorization Identity
### 5.1. TLS Connection Establishment Effects
#### 5.1.1. Default Effects
- Upon TLS establishment, any previously established authentication and authorization identities MUST remain in force, including anonymous state. This holds even if server requested client authentication via TLS.

#### 5.1.2. Client Assertion of Authorization Identity
- Client MAY implicitly request that authorization identity be derived from TLS credentials, or explicitly provide an authorization identity.

##### 5.1.2.1. Implicit Assertion
- Accomplished after TLS by invoking a Bind request of SASL "EXTERNAL" that SHALL NOT include the optional credentials octet string. Server derives authorization identity from TLS credentials per local policy.

##### 5.1.2.2. Explicit Assertion
- Accomplished after TLS by invoking a Bind request of SASL "EXTERNAL" that SHALL include the credentials octet string, constructed as documented in section 9 of [AuthMeth].

##### 5.1.2.3. Error Conditions
- Server MUST verify client's authentication identity from TLS credentials is permitted to map to asserted authorization identity. If not authorized, MUST reject with `invalidCredentials`.
- If TLS session not established prior to SASL EXTERNAL Bind, or server did not request client's authentication credentials during TLS, the SASL EXTERNAL bind MUST fail with `inappropriateAuthentication`.
- After the above failures, any client authentication and authorization state is lost; LDAP association becomes anonymous. TLS connection state is unaffected, though server MAY end TLS connection based on the failure.

### 5.2. TLS Connection Closure Effects
- Closure of the TLS connection MUST cause the LDAP association to move to an anonymous authentication and authorization state, regardless of state established over TLS or prior state.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R01 | Client MUST NOT send PDUs on connection after Start TLS request until receiving response. | MUST | Section 2.1 |
| R02 | Server MUST return Start TLS extended response with resultCode success or other. | MUST | Section 2.1 |
| R03 | Server MUST set resultCode to operationsError if client violates sequencing. | MUST | Section 2.3 |
| R04 | Server MUST set resultCode to protocolError or referral if TLS not supported. | MUST | Section 2.3 |
| R05 | Server MUST return unavailable if TLS cannot be established. | MUST | Section 2.3 |
| R06 | Client MUST NOT send Start TLS if TLS already established, during multi-stage SASL, or with outstanding LDAP operations. | MUST NOT | Section 3.1 |
| R07 | Server MUST reject requests requiring TLS with confidentialityRequired or strongAuthRequired if TLS not established. | MUST | Section 3.1 |
| R08 | After successful Start TLS, client MUST either begin TLS negotiation or close connection. | MUST | Section 3.2 |
| R09 | Client and server MUST individually decide whether to continue based on privacy level achieved. | MUST | Section 3.4 |
| R10 | If security insufficient, party SHOULD gracefully close TLS immediately after negotiation. | SHOULD | Section 3.4 |
| R11 | Client MUST check server hostname against certificate identity per matching rules. | MUST | Section 3.6 |
| R12 | If dNSName present in certificate, SHOULD be used. | SHOULD | Section 3.6 |
| R13 | User-oriented clients SHOULD notify user or terminate if hostname mismatch; automated clients SHOULD close and log error. | SHOULD | Section 3.6 |
| R14 | Client MUST refresh server capabilities after TLS session establishment. | MUST | Section 3.7 |
| R15 | Before closing TLS gracefully, client MUST wait for outstanding operations or abandon them. | MUST | Section 4.1 |
| R16 | Receiver of closure alert MUST immediately transmit a TLS closure alert. | MUST | Section 4.1 |
| R17 | Default effects: upon TLS establishment, previously established identities MUST remain in force. | MUST | Section 5.1.1 |
| R18 | Implicit assertion: Bind with SASL EXTERNAL SHALL NOT include credentials octet. | SHALL | Section 5.1.2.1 |
| R19 | Explicit assertion: Bind with SASL EXTERNAL SHALL include credentials octet per [AuthMeth]. | SHALL | Section 5.1.2.2 |
| R20 | Server MUST verify mapping of TLS credentials to authorization identity; reject with invalidCredentials if not authorized. | MUST | Section 5.1.2.3 |
| R21 | SASL EXTERNAL bind MUST fail with inappropriateAuthentication if TLS not established or no client credentials requested. | MUST | Section 5.1.2.3 |
| R22 | Closure of TLS MUST move LDAP association to anonymous state. | MUST | Section 5.2 |

## Informative Annexes (Condensed)
- **Security Considerations (Section 6)**: The Start TLS operation provides no security itself; all security derives from TLS. TLS ensures confidentiality and integrity of operations/data in transit, but does not protect directory data from server administrators or provide non-repudiation. Active-intermediary attacks can remove the Start TLS extension from the root DSE; parties SHOULD independently ascertain and consent to security level. Clients SHOULD warn users if security is insufficient. Implementors SHOULD protect credentials and allow administrators to require TLS/client authentication.
- **Acknowledgements (Section 7)**: Thanks to Tim Howes, Paul Hoffman, John Kristian, Shirish Rai, Jonathan Trostle, Harald Alvestrand, and Marcus Leech for contributions.
- **References (Section 8)**: Lists all normative references cited in the document.
- **Authors' Addresses (Section 9)**: Contact information for Jeff Hodges (Oblix), RL "Bob" Morgan (University of Washington), and Mark Wahl (Sun Microsystems).
- **Intellectual Property Rights (Section 10)**: Standard IETF IPR notice; no position on validity of claims; encourages reporting of relevant IPR.
- **Full Copyright Statement (Section 11)**: Copyright (C) The Internet Society (2000). All Rights Reserved. Permissions for copying and distribution, disclaimers.