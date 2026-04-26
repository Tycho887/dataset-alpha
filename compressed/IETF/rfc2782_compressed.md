# RFC 2782: A DNS RR for specifying the location of services (DNS SRV)
**Source**: IETF (Standards Track) | **Version**: Obsoletes RFC 2052 | **Date**: February 2000 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/rfc2782/

## Scope (Summary)
This document defines a DNS resource record (SRV RR, type 33) that enables administrators to designate multiple servers for a service/protocol per domain, with priority and weight for client selection. Clients can discover available servers by querying `_Service._Proto.Name` and obtain a prioritized list of target hosts.

## Normative References
- [BCP 14](https://datatracker.ietf.org/doc/bcp14/): Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", RFC 2119, March 1997.
- RFC 1034: Mockapetris, P., "Domain names - concepts and facilities", STD 13, RFC 1034, November 1987.
- RFC 1035: Mockapetris, P., "Domain names - Implementation and Specification", STD 13, RFC 1035, November 1987.
- RFC 2181: Elz, R. and R. Bush, "Clarifications to the DNS Specification", RFC 2181, July 1997.
- STD 2: Reynolds, J., and J. Postel, "Assigned Numbers", RFC 1700, October 1994.

## Definitions and Abbreviations
- **SRV RR**: The DNS resource record defined herein (type 33) for service location.
- **Service**: The symbolic name of the desired service, prepended with underscore (`_`), as defined by Assigned Numbers or locally. Case insensitive.
- **Proto**: The symbolic name of the desired protocol, prepended with underscore (`_`). Case insensitive.
- **Name**: The domain this RR refers to (the target domain of the query).
- **Priority**: A 16-bit unsigned integer (0–65535). The client MUST attempt to contact the target with the lowest-numbered priority it can reach.
- **Weight**: A 16-bit unsigned integer (0–65535). For same priority, larger weights SHOULD be given higher probability of selection.
- **Port**: The port number for the service (0–65535).
- **Target**: The domain name of the host providing the service. MUST have at least one address record; MUST NOT be an alias.
- **Key words**: The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in this document are to be interpreted as described in BCP 14.

## Applicability Statement
- A protocol specification that expects clients to use SRV records **MUST** define the symbolic Service name for the SRV record.
- Such specification **MUST** also include security considerations.
- Service SRV records **SHOULD NOT** be used in the absence of such specification.

## The Format of the SRV RR
The SRV RR has the following layout (DNS type code 33):
```
_Service._Proto.Name TTL Class SRV Priority Weight Port Target
```
All fields are case insensitive for Service/Proto.

### Service
The symbolic name of the desired service, as defined in [STD 2] or locally. An underscore (`_`) is prepended to avoid collisions with DNS labels. If Assigned Numbers names the service, that name is the only legal name for SRV lookups. Case insensitive.

### Proto
The symbolic name of the desired protocol, with an underscore (`_`) prepended. `_TCP` and `_UDP` are the most useful values, but any name defined by Assigned Numbers or locally may be used. Case insensitive.

### Name
The domain this RR refers to. Note: the name searched for is different from the domain name in the SRV record itself.

### TTL
Standard DNS meaning [RFC 1035].

### Class
Standard DNS meaning [RFC 1035]. SRV records occur in the IN Class.

### Priority
- **Type**: 16-bit unsigned integer (0–65535) in network byte order.
- A client **MUST** attempt to contact the target host with the lowest-numbered priority it can reach.
- Target hosts with the same priority **SHOULD** be tried in an order defined by the Weight field.

### Weight
- **Type**: 16-bit unsigned integer (0–65535) in network byte order.
- Larger weights **SHOULD** be given a proportionately higher probability of being selected.
- Domain administrators **SHOULD** use Weight 0 when no server selection is needed, for readability.
- In the presence of records with weight > 0, records with weight 0 should have a very small chance of being selected.
- When ordering SRV RRs of the same priority, the following algorithm **SHOULD** be used:
  1. Arrange all unordered SRV RRs in any order, with weight 0 records placed at the beginning.
  2. Compute the sum of the weights of those RRs; associate each RR with the running sum in the selected order.
  3. Choose a uniform random number between 0 and the sum (inclusive).
  4. Select the RR whose running sum is the first greater than or equal to the random number.
  5. Remove that RR from the unordered set and repeat until all are ordered.
  6. Repeat for each priority level.

### Port
- **Type**: 16-bit unsigned integer (0–65535) in network byte order.
- The port for the service; often as specified in Assigned Numbers but need not be.

### Target
- The domain name of the target host.
- **MUST** have one or more address records for this name.
- **MUST NOT** be an alias (in the sense of RFC 1034 or RFC 2181).
- Implementors are urged, but not required, to return address records in the Additional Data section.
- Unless permitted by future standards, name compression **must not** be used for this field.
- A Target of `"."` means the service is decidedly not available at this domain.

## Usage Rules
A SRV‑cognizant client **SHOULD** use the following procedure:

1. Do a lookup for `QNAME=_service._protocol.target`, `QCLASS=IN`, `QTYPE=SRV`.
2. If the reply is `NOERROR`, `ANCOUNT>0`, and at least one SRV RR matches the requested Service and Protocol:
   - If there is exactly one SRV RR and its Target is `"."` (root domain), abort.
   - Otherwise, build a list of (Priority, Weight, Target) tuples from all such RRs.
   - Sort the list by priority (lowest first).
   - Create a new empty list.
   - For each distinct priority level, apply the weight selection algorithm (see above) to move elements to the new list until no elements remain at that priority.
   - For each element in the new list:
     - Query DNS for address records for the Target (or use any in the Additional Data section of the SRV response).
     - For each address record found, try to connect to the (protocol, address, service).
3. Else (no SRV response or no matching RRs):
   - Do a lookup for `QNAME=target`, `QCLASS=IN`, `QTYPE=A`.
   - For each address record found, try to connect to the (protocol, address, service).

**Notes**:
- Port numbers **SHOULD NOT** be used in place of symbolic service/protocol names.
- If a truncated response comes back from an SRV query, the rules described in [RFC 2181] shall apply.
- A client **MUST** parse all of the RRs in the reply.
- If the Additional Data section does not contain address records for all SRV RRs and the client may need to connect, the client **MUST** look up the address record(s).

## Domain Administrator Advice (Informative)
Administrators should provide address records to support old clients. For services spread over multiple hosts, include address records at the same DNS node for fallback. For a single service provided by several hosts, use either round‑robin (by listing all A records) or just the fastest. Backup servers should not be in address records; if listed, they must use the standard port. Future protocol designers may choose not to use SRV’s secondary support. Keep SRV reply size under 512 bytes until all resolvers handle larger responses. A rough size estimate: 30‑byte overhead + name of service + each SRV RR (20 bytes + target name) + each NS RR (15 bytes + nameserver name) + each A RR (≈20 bytes). Use a DNS query tool to check actual size near the limit.

## Weight Field Discussion (Informative)
Weight is intended for static server selection (e.g., “this host is three times as fast as that one”). Dynamic load estimation is impractical because server load changes faster than DNS caching permits. Use of SRV weight with network proximity estimation is for further study.

## Port Number Discussion (Informative)
SRV moves port mapping to DNS, reducing the need to update `/etc/services` on every host and allowing standard services to use non‑root ports.

## IANA Considerations
The IANA has assigned RR type value 33 to the SRV RR. No other IANA services are required.

## Changes from RFC 2052 (Informative)
RFC 2782 obsoletes RFC 2052. The major change is that protocol and service labels now are prepended with an underscore to reduce accidental clashes. Other changes clarify the use of the Weight field.

## Security Considerations (Condensed)
The SRV RR is not believed to introduce new security problems, but some issues become more visible:
- Fine‑grained port specification changes router filtering capabilities; blocking internal clients from specific external services becomes impossible, and running unauthorized services is slightly harder.
- A site cannot prevent its hosts from being referenced as servers, potentially leading to denial of service.
- DNS spoofers can supply false port numbers (in addition to host names and addresses), but this is an extension of an existing vulnerability.

## Informative Annexes (Condensed)
### Fictional Example – `foobar` service at `example.com.`
````
$ORIGIN example.com.
@               SOA server.example.com. root.example.com. (...)
                NS  server.example.com.
                NS  ns1.ip-provider.net.
                NS  ns2.ip-provider.net.
_foobar._tcp    SRV 0 1 9 old-slow-box.example.com.
                 SRV 0 3 9 new-fast-box.example.com.
                 SRV 1 0 9 sysadmins-box.example.com.
                 SRV 1 0 9 server.example.com.
server           A   172.30.79.10
old-slow-box     A   172.30.79.11
sysadmins-box    A   172.30.79.12
new-fast-box     A   172.30.79.13
*._tcp          SRV  0 0 0 .
*._udp          SRV  0 0 0 .
````
A client for service `foobar` queries `_foobar._tcp.example.com.` and gets back 4 SRV RRs. It then applies priority/weight ordering to select a target. The example illustrates use of priority for primary/backup and weight for load sharing (3:1 ratio for new‑fast‑box). Wildcard SRV records (`*._tcp`, `*._udp`) indicate no other services are supported.

## Requirements Summary

| ID  | Requirement | Type | Reference |
|-----|-------------|------|-----------|
| R01 | A client MUST attempt to contact the target host with the lowest-numbered priority. | MUST | Priority Field |
| R02 | Target hosts with the same priority SHOULD be tried in an order defined by the Weight field. | SHOULD | Priority Field |
| R03 | Larger weights SHOULD be given a proportionately higher probability of being selected. | SHOULD | Weight Field |
| R04 | Domain administrators SHOULD use Weight 0 when no server selection is needed. | SHOULD | Weight Field |
| R05 | The ordering algorithm described for weighting SHOULD be used. | SHOULD | Weight Field |
| R06 | The Target domain name MUST have one or more address records. | MUST | Target Field |
| R07 | The Target name MUST NOT be an alias (RFC 1034/RFC 2181). | MUST | Target Field |
| R08 | Unless future standards allow, name compression MUST NOT be used for the Target field. | MUST | Target Field |
| R09 | A Target of "." means the service is definitely not available. | SHOULD | Target Field (normative by context) |
| R10 | A protocol specification that expects use of SRV MUST define the symbolic Service name. | MUST | Applicability Statement |
| R11 | Such specification MUST also include security considerations. | MUST | Applicability Statement |
| R12 | Service SRV records SHOULD NOT be used without such specification. | SHOULD | Applicability Statement |
| R13 | Port numbers SHOULD NOT be used in place of symbolic service/protocol names. | SHOULD | Usage Rules, Note 1 |
| R14 | If a truncated response comes from an SRV query, the rules in RFC 2181 shall apply. | SHALL | Usage Rules, Note 2 |
| R15 | A client MUST parse all RRs in the SRV reply. | MUST | Usage Rules, Note 3 |
| R16 | If Additional Data lacks address records for needed SRV RRs, the client MUST look up the address records. | MUST | Usage Rules, Note 4 |
| R17 | The service and protocol labels MUST be prepended with an underscore. | MUST | Service/Proto definitions (normative convention) |