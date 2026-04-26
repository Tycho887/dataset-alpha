# RFC 5922: Domain Certificates in the Session Initiation Protocol (SIP)
**Source**: IETF | **Version**: Standards Track | **Date**: June 2010 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc5922

## Scope (Summary)
This document specifies how to encode and extract SIP domain identities from X.509 PKIX-compliant certificates for use in TLS connections, and defines matching rules for SIP domain authentication.

## Normative References
- [1] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [2] Rosenberg, J., et al., "SIP: Session Initiation Protocol", RFC 3261, June 2002.
- [3] Eastlake, D., "Domain Name System (DNS) Case Insensitivity Clarification", RFC 4343, January 2006.
- [4] Blake-Wilson, S., et al., "Transport Layer Security (TLS) Extensions", RFC 4366, April 2006.
- [5] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.2", RFC 5246, August 2008.
- [6] Cooper, D., et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 5280, May 2008.

## Definitions and Abbreviations
- **SIP domain identity**: An identity (e.g., "sip:example.com") contained in an X.509 certificate bound to a subject that identifies the subject as an authoritative SIP server for a domain.

## 1. Introduction
Summarized: This document addresses insufficient specification in RFC 3261 for using certificates for domain authentication in TLS. It provides guidance for constructing and interpreting certificates to identify holders as authoritative for a SIP domain. Does not define S/MIME use.

## 2. Terminology
### 2.1. Key Words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119 [1].

## 3. Problem Statement
RFC 3261 lacked guidelines on where to place SIP identities (subjectAltName vs. CN) in TLS certificates, creating ambiguities. This document defines matching behavior and rules for multiple identities.

## 4. SIP Domain to Host Resolution
Client uses RFC 3263 procedures on a SIP URI (AUS) to obtain servers via DNS. When TLS transport indicated, server presents X.509 certificate. Client extracts identities (per Section 7.1) and compares to domain part of original URI (per Section 7.2). Server authenticated if match found. Recommends conveying domain identity as subjectAltName of type uniformResourceIdentifier.

## 5. The Need for Mutual Interdomain Authentication
Describes SIP trapezoid where proxies need mutual authentication. RFC 3261 is silent on which field to use (subjectAltName vs CN) and precedence. Normative client behavior in Section 7.3 and server behavior in Section 7.4 address this.

## 6. Certificate Usage by a SIP Service Provider
Service providers **SHOULD** use subjectAltName to convey identities (multiple values, no syntax ambiguity). When assigning certificates, a provider **MUST** ensure the SIP domain used to reach the server appears as an identity in the subjectAltName field, or for backward compatibility, the Subject field.

## 7. Behavior of SIP Entities
### 7.1. Finding SIP Identities in a Certificate
- Implementations **MUST** determine certificate validity per RFC 5280 [6].
- Implementations **MUST** check extendedKeyUsage restrictions per RFC 5924 [12].
- Procedure:
  1. Examine each value in subjectAltName.
     - **URI** type: If scheme is not "sip", **MUST NOT** accept as SIP domain identity. If scheme is "sip" and userpart present (contains '@'), **MUST NOT** accept. If scheme is "sip" and no userinfo component, **MUST** accept hostpart as SIP domain identity.
     - **DNS** type: **MUST** accept only if no "sip" URI identity found.
  2. If subjectAltName absent, **MAY** examine CN field; if valid DNS name found, **MAY** accept as identity (backward compatibility).

### 7.2. Comparing SIP Identities
- **MUST** compare only DNS name component (no scheme or parameters).
- **MUST** compare case-insensitively per RFC 4343 [3]; handle IDNs per RFC 5280 Section 7.2.
- **MUST** match full values: no suffix matching, no wildcard interpretation (e.g., "*.example.com" matches only "*.example.com").

### 7.3. Client Behavior
- Client uses domain portion of SIP AUS from RFC 3263.
- **MUST** determine SIP domain identities in server certificate (Section 7.1).
- **MUST** compare original domain portion of AUS to identities (Section 7.2).
  - If no identities found, server not authenticated.
  - If match found, server authenticated for that domain.
- If server not authenticated, client **MUST** close connection immediately.

### 7.4. Server Behavior
- Server presents its certificate; if client does not present certificate, client **MUST NOT** be considered authenticated.
- Whether to close connection if client does not present certificate is local policy.
- When authenticating client, server **MUST** obtain SIP domain identities from client certificate (Section 7.1). Server may use these for authorization decisions (e.g., whitelist of acceptable domains).

### 7.5. Proxy Behavior
- Proxy **MUST** follow UAS procedures (Section 7.4) when authenticating a connection from a client.
- Proxy **MUST** follow UAC procedures (Section 7.3) when requesting an authenticated connection to a UAS.
- If proxy adds Record-Route expecting secure connections, proxy **MUST** insert a URI corresponding to an identity for which it has a certificate.

### 7.6. Registrar Behavior
- Follows server behavior (Section 7.4). May additionally challenge client with HTTP Digest.

### 7.7. Redirect Server Behavior
- Follows UAS behavior (Section 7.4).

### 7.8. Virtual SIP Servers and Certificate Content
- Certificates can contain multiple subjectAltName identities (per RFC 4474). For virtual hosting, if TLS "server_name" extension (RFC 4366) is supported, client **SHOULD** use it to request a certificate for the specific domain.

## 8. Security Considerations
Summarized: TLS provides confidentiality, integrity, authentication at transport layer. Appropriate processing of domain certificates provides application-level guarantees: SIPS messages readable only by authorized endpoints and proxies; mutual authentication between user and authoritative proxies, and transitively between users across domains.

### 8.1. Connection Authentication Using Digest
- Digest authentication provides limited integrity and no transport binding. A SIP implementation **SHOULD NOT** infer authentication of other messages on a connection from Digest authentication of a single message.
- Authentication of the domain at the other end of a connection **SHOULD** be accomplished using TLS and certificate validation rules in this specification.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Service provider MUST ensure SIP domain used to reach server appears in subjectAltName (or Subject for legacy). | MUST | Section 6 |
| R2 | Implementations MUST determine certificate validity per RFC 5280. | MUST | Section 7.1 |
| R3 | Implementations MUST check extendedKeyUsage restrictions per RFC 5924. | MUST | Section 7.1 |
| R4 | For URI type in subjectAltName with scheme "sip" and no userinfo, MUST accept hostpart as identity. | MUST | Section 7.1 step 1 |
| R5 | For URI type with scheme not "sip", MUST NOT accept as identity. | MUST | Section 7.1 step 1 |
| R6 | For URI type with userpart, MUST NOT accept as identity. | MUST | Section 7.1 step 1 |
| R7 | For DNS type in subjectAltName, MUST accept only if no "sip" URI identity found. | MUST | Section 7.1 step 1 |
| R8 | If subjectAltName absent, MAY accept CN if valid DNS name (backward compatibility). | MAY | Section 7.1 step 2 |
| R9 | When comparing identities, MUST compare only DNS name component. | MUST | Section 7.2 |
| R10 | MUST compare case-insensitively per RFC 4343. | MUST | Section 7.2 |
| R11 | MUST match full values; no suffix or wildcard matching. | MUST | Section 7.2 |
| R12 | Client MUST determine identities from server certificate (Section 7.1) and compare to AUS domain. If no identities or no match, server not authenticated; client MUST close connection. | MUST | Section 7.3 |
| R13 | Server MUST NOT consider client authenticated if no certificate presented. | MUST | Section 7.4 |
| R14 | Server MUST obtain identities from client certificate (Section 7.1) for authorization. | MUST | Section 7.4 |
| R15 | Proxy must follow UAS procedures for incoming and UAC procedures for outgoing authenticated connections. | MUST | Section 7.5 |
| R16 | Proxy inserting Record-Route expecting secure connections MUST insert URI corresponding to its certificate identity. | MUST | Section 7.5 |
| R17 | Client SHOULD use TLS "server_name" extension to request certificate for specific domain. | SHOULD | Section 7.8 |
| R18 | Implementation SHOULD NOT use Digest authentication of one message to infer authentication of others on same connection. | SHOULD | Section 8.1 |
| R19 | Authentication of domain at other end of connection SHOULD use TLS and certificate validation. | SHOULD | Section 8.1 |

## Informative Annexes (Condensed)
- **Appendix A. Editorial Guidance (Non-Normative)**: Provides guidance for updating RFC 3261. Section A.2.1 proposes replacement text for RFC 3261 Section 26.3.1: "Proxy servers, redirect servers, registrars, and any other server that is authoritative for some SIP purpose in a given domain SHOULD possess a certificate whose subjects include the name of that SIP domain."