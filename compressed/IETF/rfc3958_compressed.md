# RFC 3958: Domain-Based Application Service Location Using SRV RRs and the Dynamic Delegation Discovery Service (DDDS)
**Source**: IETF | **Version**: Standards Track | **Date**: January 2005 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc3958

## Scope (Summary)
This memo defines a generalized mechanism for application service naming that allows service location without relying on rigid domain naming conventions. It defines a Dynamic Delegation Discovery System (DDDS) Application to map domain name, application service name, and application protocol dynamically to target server and port using both NAPTR and SRV DNS resource records.

## Normative References
- [RFC 2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC 2234] Crocker, D., Ed. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 2234, November 1997.
- [RFC 2782] Gulbrandsen, A., Vixie, P., and L. Esibov, "A DNS RR for specifying the location of services (DNS SRV)", RFC 2782, February 2000.
- [RFC 3401] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part One: The Comprehensive DDDS", RFC 3401, October 2002.
- [RFC 3403] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part Three: The Domain Name System (DNS) Database", RFC 3403, October 2002.
- [RFC 3404] Mealling, M., "Dynamic Delegation Discovery System (DDDS) Part Four: The Uniform Resource Identifiers (URI)", RFC 3404, October 2002.
- [RFC 2434] Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 2434, October 1998.

## Definitions and Abbreviations
- **Application service**: A generic term for some type of application, independent of the protocol that may be used to offer it. Each application service will be associated with an IANA-registered tag.
- **Application protocol**: Used to implement the application service. Also associated with IANA-registered tags.
- **S-NAPTR**: Straightforward-NAPTR, the DDDS application defined in this document.
- **DDDS**: Dynamic Delegation Discovery System.
- **NAPTR RR**: Naming Authority Pointer Resource Record (RFC 3403).
- **SRV RR**: Service Resource Record (RFC 2782).
- **Terminal flag**: In S-NAPTR, only "S" and "A" flags are terminal. "S" leads to SRV record lookup; "A" leads to address record (A) lookup.
- **Non-terminal flag**: Empty flag field; leads to another NAPTR record lookup.
- **Application-Unique String**: The domain label for which an authoritative server for a particular service is sought.
- **First Well-Known Rule**: Identity – the output of the rule is the Application-Unique String.
- **Expected Output**: Information necessary for a client to connect to authoritative server(s) (host, port, protocol) for a particular application service within a given domain.

## 1. Introduction
This memo defines a generalized mechanism for service location using DDDS. It uses both NAPTR and SRV records to map service+protocol+domain to server addresses. The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119.

## 2. Straightforward-NAPTR (S-NAPTR) Specification
### 2.1 Key Terms
- **Application service** and **application protocol** as defined above.

### 2.2 S-NAPTR DDDS Application Usage
- NAPTR records are used to store application service+protocol information for a given domain.
- A client retrieves all NAPTR records for the target domain name, sorts them by increasing ORDER and increasing PREF within each ORDER.
- **Ordering and Preference**: Records are sorted by ORDER, then by PREF within each ORDER.
- **Matching and Non-matching NAPTR Records**: Starting with the first sorted NAPTR record, the client examines the SERVICE field for a match (desired application service and supported application protocol). If multiple match, they are processed in increasing sort order.
- **Terminal and Non-terminal NAPTR Records**:
    - Empty FLAG: non-terminal; the REPLACEMENT field is used for the next DNS lookup for NAPTR RRs.
    - "S" flag: terminal; REPLACEMENT field used for SRV RR lookup, then normal SRV processing.
    - "A" flag: terminal; address record sought for REPLACEMENT field (default protocol port assumed).
- **S-NAPTR and Successive Resolution**: Multiple possible targets are pursued in order until a server is successfully contacted or all possible matching NAPTR records have been exhausted.
    - **Failure** is declared and backtracking must be used when:
        - The designated remote server fails to provide appropriate security credentials for the *originating* domain.
        - Connection to the designated remote server otherwise fails (specific terms defined per application protocol).
        - The S-NAPTR-designated DNS lookup fails to yield expected results (e.g., no A RR for "A" target, no SRV for "S" target, or no NAPTR with appropriate service+protocol). Except for the first NAPTR lookup, this is a configuration error; the client MUST backtrack and try the next available option.
- **Clients Supporting Multiple Protocols**:
    - MUST pursue S-NAPTR resolution completely for one protocol before switching to another.
    - MAY choose which protocol to try first based on own preference or PREF ranking in the first NAPTR RR set.
    - MAY run simultaneous DDDS resolutions for more than one protocol, with the above requirements applying independently.

## 3. Guidelines
### 3.1 Guidelines for Application Protocol Developers
- S-NAPTR provides a framework without requiring each application to define a separate DDDS application.
- This approach is for associating services with domain names; not for mapping arbitrary labels into domain names.
- This document does not address how to select the domain for which service+protocol is sought.
- Protocol developers must:
    - **Register** application service and protocol tags (see Section 7).
    - **Define conditions for retry/failure**: what constitutes a failure that causes return to S-NAPTR for next target? Include credential failure as always a failure condition.
    - **Define server identification and handshake**: protocol developers should identify the mechanics of the expected identification handshake when the client connects to a server found through S-NAPTR.

### 3.2 Guidelines for Domain Administrators
- Use S-NAPTR with restraint.
- The S-NAPTR tree of NAPTR, SRV, and A RRs should be as shallow and with as few branches as possible.
    - Fewer branches is better.
    - Shallower is better: avoid NAPTR records to rename services within a zone; use them for services hosted elsewhere.

### 3.3 Guidelines for Client Software Writers
- If the application cannot successfully connect to one target, it must continue through the S-NAPTR tree to try less preferred alternatives.

## 4. Illustrations (Condensed)
- **4.1 Use Cases**: Service discovery within a domain, multiple protocols, remote hosting.
- **4.2 Service Discovery within a Domain**: Example of a hypothetical CredReg service using NAPTR records to locate server within or across domains.
- **4.3 Multiple Protocols**: Extensible messaging (EM) example showing how a domain can outsource services and still indicate preference ordering.
- **4.4 Remote Hosting**: Better approach using NAPTR records that point to a hosting domain's NAPTR records, allowing independent administration.
- **4.5 Sets of NAPTR RRs**: When multiple services exist for a domain, clients sort by ORDER and match based on SERVICE field.
- **4.6 Sample Sequence Diagram**: Step-by-step resolution for EM:ProtB from thinkingcat.example, including failure and fallback.

## 5. Motivation and Discussion (Condensed)
- SRV records provide only one layer of indirection and focus on server administration, not application naming. They also restrict protocols to UDP/TCP.
- NAPTR records must be part of a DDDS application; this document defines a simple, straightforward application (S-NAPTR) that avoids regex and uses only replacement, making it predictable and efficient.
- S-NAPTR adds a layer of indirection beyond SRV while restricting NAPTR usage for simplicity.

## 6. Formal Definition of <Application Service Location> Application of DDDS
### 6.1 Application-Unique String
The domain label for which an authoritative server for a particular service is sought.

### 6.2 First Well-Known Rule
Identity – the output is the Application-Unique String.

### 6.3 Expected Output
Information necessary for a client to connect to authoritative server(s) (host, port, protocol) for a particular application service within a given domain.

### 6.4 Flags
- Only "S" and "A" flags are valid; both are terminal.
- Empty flag means next lookup is for NAPTR records.
- "S" flag: output is a domain label for which one or more SRV records exist.
- "A" flag: output is a domain name for which address records should be looked up.

### 6.5 Service Parameters
- ABNF defined:
    ```
    service-parms = [ [app-service] *(":" app-protocol)]
    app-service   = experimental-service / iana-registered-service
    app-protocol  = experimental-protocol / iana-registered-protocol
    experimental-service      = "x-" 1*30ALPHANUMSYM
    experimental-protocol     = "x-" 1*30ALPHANUMSYM
    iana-registered-service   = ALPHA *31ALPHANUMSYM
    iana-registered-protocol  = ALPHA *31ALPHANUM
    ALPHA         = %x41-5A / %x61-7A
    DIGIT         = %x30-39
    SYM           = %x2B / %x2D / %x2E
    ALPHANUMSYM   = ALPHA / DIGIT / SYM
    ```
- Case-insensitive. Maximum 32 characters, must start with alphabetic character.
- App-service must be IANA-registered (or experimental "x-").
- App-protocol must be IANA-registered (or experimental "x-").

### 6.6 Valid Rules
- Only substitution Rules are permitted; no regular expressions.

### 6.7 Valid Databases
- Only one database specified: NAPTR DNS resource records (RFC 3403). Keys are domain names.
- DNS servers MAY interpret flags to include additional records; clients are encouraged but not required to check additional information.

## 7. IANA Considerations
### 7.1 Application Service Tag Registry
- IANA maintains a registry for S-NAPTR Application Service Tags, listing tag and defining RFC.
- **Initial registration**: [RFC 3982].

### 7.2 Application Protocol Tag Registry
- IANA maintains a registry for S-NAPTR Application Protocol Tags, listing tag and defining RFC.
- **Initial registration**: [RFC 3983].

### 7.3 Registration Process
- Tags starting with "x-" are experimental.
- Other tags registered via "specification required" (RFC 2434), with the specification being an RFC of any category.
- Defining RFC must identify: tag, intended usage, interoperability considerations, security considerations, and any relevant publications.

## 8. Security Considerations
- Security relies on security of DNS queries. Bogus NAPTR/SRV records could redirect clients.
- DNSSEC can be used to ensure validity.
- Applications should define end-to-end authentication to ensure correct destination. The basic mechanism:
    1. Client sends original destination name to server during handshake.
    2. Server returns credential with appropriate name.
    3. Client matches name in credential with name sent.
    4. If match and credential integrity, reasonable assurance.
    5. Integrity-protected channel established.
- Defined S-NAPTR uses MUST define handshake, credential naming, and name-matching semantics.

## Requirements Summary

| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14, RFC 2119. | shall | Section 1 |
| R2 | In S-NAPTR, the only terminal flags are "S" and "A". | shall | Section 2.2.3, 6.4 |
| R3 | An application client first queries for the NAPTR RRs for the domain of a named application service. The first DNS query is for the NAPTR RRs in the original target domain. | shall | Section 2.2.4 |
| R4 | Failure is declared and backtracking must be used when: o the designated remote server fails to provide appropriate security credentials for the *originating* domain; o connection to the designated remote server otherwise fails – defined per protocol; o the S-NAPTR-designated DNS lookup fails to yield expected results. | must | Section 2.2.4 |
| R5 | In the case of an application client that supports more than one protocol for a given application service, it MUST pursue S-NAPTR resolution completely for one protocol, exploring all potential terminal lookups, until the application connects successfully or there are no more possibilities for that protocol. | must | Section 2.2.5 |
| R6 | The client MAY choose which protocol to try first based on its own preference, or on the PREF ranking in the first set of NAPTR records. However, the chosen protocol MUST be listed in that first NAPTR RR set. | may, must | Section 2.2.5 |
| R7 | Application protocol developers must make provisions for registering any relevant application service and application protocol tags, as described in Section 7. | must | Section 3.1.1 |
| R8 | The most important thing is to select one expected behaviour for retry/failure and document it as part of the use of S-NAPTR. | shall | Section 3.1.2 |
| R9 | Failure to provide appropriate credentials to identify the server as being authoritative for the original target domain is always considered a failure condition. | shall | Section 3.1.2 |
| R10 | Application protocol developers using S-NAPTR should identify the mechanics of the expected identification handshake when the client connects to a server found through S-NAPTR. | should | Section 3.1.3 |
| R11 | Domain administrators are called upon to use S-NAPTR with as much restraint as possible. | should | Section 3.2 |
| R12 | Only substitution Rules are permitted for this application. That is, no regular expressions are allowed. | shall | Section 6.6 |
| R13 | Service Parameters syntax as defined in ABNF in Section 6.5. | shall | Section 6.5 |
| R14 | All application service and protocol tags that start with "x-" are considered experimental. | shall | Section 7.3 |
| R15 | All other application service and protocol tags are registered based on the "specification required" option defined in [7], with the further stipulation that the "specification" is an RFC (of any category). | shall | Section 7.3 |
| R16 | The defining RFC must clearly identify and describe, for each tag being registered, application protocol or service tag, intended usage, interoperability considerations, security considerations, and any relevant related publications. | must | Section 7.3 |
| R17 | Definitions of S-NAPTR for particular application protocols MUST define the handshake mechanism, the specific credential naming fields, and the name-matching semantics. | must | Section 8 |

## Informative Annexes (Condensed)
- **Appendix A. Pseudo-pseudocode for S-NAPTR**: Provides algorithmic outline for finding the first (best) target (A.1) and subsequent targets (A.2) with retry logic.
- **Appendix B. Availability of Sample Code**: Sample Python code for S-NAPTR resolution is available from http://www.verisignlabs.com/pysnaptr-0.1.tgz.