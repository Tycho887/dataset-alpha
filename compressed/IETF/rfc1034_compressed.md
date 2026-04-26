# RFC 1034: Domain Names - Concepts and Facilities
**Source**: Network Working Group | **Version**: November 1987 | **Type**: Normative  
**Original**: [RFC 1034](https://tools.ietf.org/html/rfc1034)

## Scope (Summary)
This RFC introduces the Domain Name System (DNS) concepts and facilities, including the domain name space, resource records, name servers, and resolvers. It provides design goals, assumptions, and operational guidelines. A companion RFC (RFC-1035) contains implementation details.

## Normative References
- [RFC-1035] "Domain Names - Implementation and Specification"
- [RFC-952] "DoD Internet Host Table Specification"
- [RFC-953] "HOSTNAME Server"
- [RFC-974] "Mail routing and the domain system"
- [RFC-920] "Domain Requirements"
- [RFC-882] "Domain names - Concepts and Facilities" (obsoleted by this memo)
- [RFC-883] "Domain names - Implementation and Specification" (obsoleted by this memo)
- [RFC-973] "Domain System Changes and Observations" (obsoleted by this memo)

*Additional references listed in Section 7 of the original document.*

## Definitions and Abbreviations
- **Domain Name**: A sequence of labels from a node to the root, separated by dots; case-insensitive in comparisons.
- **Resource Record (RR)**: A unit of data associated with a domain name, consisting of owner, type, class, TTL, and RDATA.
- **Zone**: A contiguous portion of the domain name space for which a name server has authoritative data.
- **Authoritative**: A name server is authoritative for a zone if it holds the master copy of that zone's data.
- **Resolver**: A program that extracts information from name servers on behalf of client applications.
- **Name Server**: A server program holding information about the domain tree structure and resource records.
- **CNAME**: Canonicial name RR; identifies an alias.
- **MX**: Mail exchange RR.
- **NS**: Name server RR.
- **SOA**: Start of Authority RR.
- **PTR**: Pointer RR.
- **TTL**: Time to Live; maximum seconds an RR may be cached.

## 1. Status of This Memo
This RFC is an introduction to the DNS; details are in [RFC-1035]. The official protocol includes standard queries and responses and most Internet class data formats. The system is extensible; experimental features are clearly marked. Examples are pedagogical and should not be considered current or complete.

## 2. Introduction
### 2.1. History of Domain Names
Driven by Internet growth, the hierarchical name space with distributed database and generalized resources evolved from earlier proposals [IEN-116, RFC-799, RFC-819, RFC-830, RFC-882, RFC-883]. The term "domain name" is used broadly beyond DNS.

### 2.2. DNS Design Goals
- **Primary goal**: A consistent name space for referring to resources; names shall not embed network identifiers, addresses, or routes.
- **Distribution**: The database shall be maintained in a distributed manner with local caching. The structure and mechanisms for creating/deleting names shall be distributed.
- **Tradeoff control**: The source of data shall control the tradeoff between acquisition cost, update speed, and cache accuracy.
- **Generality**: The facility shall be generally useful, not restricted to a single application. Data is tagged with type; queries can be limited to a single type.
- **Multiple classes**: Use the same name space with different protocol families; data is tagged with class and type.
- **Transport independence**: Name server transactions shall be independent of the communications system.
- **Wide host capability**: Shall be useful across personal computers to large timeshared hosts.

### 2.3. Assumptions About Usage
- Database size initially proportional to number of hosts, eventually proportional to number of users.
- Most data changes slowly; system shall handle subsets changing on the order of seconds or minutes.
- Administrative boundaries correspond to organizations; each organization shall provide redundant name servers.
- Clients shall be able to identify trusted name servers before accepting referrals.
- Access to information is more critical than instantaneous updates; updates percolate, copies have timeouts.
- Iterative approach is preferred for datagram access; domain system requires implementation of iterative approach; recursive is optional.
- All data originates in master files; resolvers access name servers through standard resolvers.

### 2.4. Elements of the DNS
The DNS has three major components:
1. **Domain Name Space and Resource Records**: Tree structured name space with associated data.
2. **Name Servers**: Server programs holding information about domain tree subsets; authoritative for zones.
3. **Resolvers**: Programs that extract information from name servers for client requests.

## 3. Domain Name Space and Resource Records
### 3.1. Name Space Specifications and Terminology
- The domain name space is a tree; each node has a label (0–63 octets). Brother nodes shall not have the same label. The null label is reserved for the root.
- Domain name is the list of labels from node to root, printed left to right (most specific to least specific).
- Internal representation: sequence of labels with length octet and octet string; root is length zero.
- Case comparisons are case-insensitive (ASCII high order zero bit); preserve case when received.
- Printed form: labels separated by dots; complete domain name ends with a dot (absolute). Relative names are completed by local software.
- Total number of octets representing a domain name is limited to 255.
- A domain is the space at or below a domain name; subdomain if contained within another.

### 3.2. Administrative Guidelines on Use
- DNS specifications do not mandate a particular tree structure or label selection rules.
- Guidelines for top levels originated in RFC-920; current policy in [RFC-1032].
- Lower domains that will be broken into multiple zones should provide branching at the top to avoid renaming.

### 3.3. Technical Guidelines on Use
Before using DNS for an object, two needs must be met:
1. Convention for mapping object names to domain names.
2. RR types and data formats for the object.

Examples: host name mapping (plus IN-ADDR.ARPA for inverse), mailbox mapping (local-part@mail-domain becomes local-part.mail-domain).

### 3.4. Example Name Space
*(Figure showing root, MIL, EDU, ARPA, etc.)* – see original document.

### 3.5. Preferred Name Syntax
```
<domain> ::= <subdomain> | " "
<subdomain> ::= <label> | <subdomain> "." <label>
<label> ::= <letter> [ [ <ldh-str> ] <let-dig> ]
<ldh-str> ::= <let-dig-hyp> | <let-dig-hyp> <ldh-str>
<let-dig-hyp> ::= <let-dig> | "-"
<let-dig> ::= <letter> | <digit>
```
- Labels must start with a letter, end with letter or digit, interior only letters, digits, hyphen; maximum 63 characters.
- Case is not significant.

### 3.6. Resource Records (RR)
Each node has a set of RRs. An RR has:
- **owner**: domain name where found.
- **type**: 16-bit encoded abstract resource type (e.g., A, CNAME, MX, NS, PTR, SOA, HINFO).
- **class**: 16-bit protocol family/instance (e.g., IN, CH).
- **TTL**: time to live in seconds; describes caching duration. Authoritative data timed by zone refresh policy. TTL can be zero to prohibit caching.
- **RDATA**: type and class dependent data (e.g., A: IP address; CNAME: domain name; MX: preference + host; NS: host name; PTR: domain name; SOA: multiple fields).

#### 3.6.1. Textual Expression of RRs
RRs are shown in master file format: owner (blank means previous owner), TTL, class, type, RDATA. Example:
```
ISI.EDU.        MX      10 VENERA.ISI.EDU.
```

#### 3.6.2. Aliases and Canonical Names
- CNAME RR identifies an alias; if a CNAME RR is present at a node, no other data shall be present.
- When a name server encounters a CNAME while looking for another type, it restarts the query at the canonical name. Queries for CNAME type are not restarted.
- Domain names in other RRs should point to the primary name, not aliases.

### 3.7. Queries
Queries are messages sent to name servers; carried in UDP datagrams or TCP connections. Standard message format has header (including opcode), question, answer, authority, additional sections.

#### 3.7.1. Standard Queries
Specify QNAME, QTYPE, QCLASS. QTYPE can match a specific type, AXFR (zone transfer), MAILB (mailbox related), or * (all). QCLASS can match a specific class or *. Responses may include relevant RRs, referrals, or additional useful RRs.

#### 3.7.2. Inverse Queries (Optional)
Map a resource to a domain name. Not guaranteed complete or unique. Shall not be used for host address to host name mapping; use IN-ADDR.ARPA. Implementations must at least understand and return not-implemented error.

#### 3.7.3. Status Queries (Experimental)
To be defined.

#### 3.7.4. Completion Queries (Obsolete)
Deleted; redesign possible or opcodes reclaimed.

## 4. Name Servers
### 4.1. Introduction
Name servers are repositories of domain database divided into zones. Essential task: answer queries using local zone data. Every zone must be available on at least two servers. Name servers mark responses as authoritative or cached.

### 4.2. How the Database is Divided into Zones
Divided by class and by cuts in the name space. Within a class, cuts separate connected regions into zones. Each zone has authoritative data for all nodes in the connected region. Zones have a top node (identified by name), authoritative data, delegation NS RRs (not authoritative), and glue RRs for subzone servers.

#### 4.2.1. Technical Considerations
A zone's data includes:
- Authoritative RRs for all nodes in the zone.
- SOA and NS RRs for the top node (authoritative).
- NS RRs for delegated subzones (non-authoritative).
- Glue RRs (addresses) for subzone name servers when needed.

#### 4.2.2. Administrative Considerations
To control a domain, identify parent zone and obtain delegation. No requirement that servers reside in the domain; distribution can improve accessibility. Delegation NS and glue RRs must be added to parent zone; consistency must be maintained.

### 4.3. Name Server Internals
#### 4.3.1. Queries and Responses
Name servers answer standard queries in non-recursive or recursive mode. All name servers must implement non-recursive. Recursive service is optional. The RA (Recursion Available) bit signals willingness; RD (Recursion Desired) bit in query requests it. Recursive mode used only when RD is set. Responses: answer, name error, temporary error, or referral.

#### 4.3.2. Algorithm
1. Set RA bit as configured. If recursive service available and RD set, go to step 5.
2. Search zones for nearest ancestor of QNAME. If found, go to step 3, else step 4.
3. Match down label by label in zone:
   - If QNAME matched: if CNAME and QTYPE != CNAME, copy CNAME, change QNAME to canonical, go to step 1; else copy matching RRs, go to step 6.
   - If referral (NS RRs marking cut): copy NS RRs to authority section, add glue if available, go to step 4.
   - If label not found: check for wildcard "*" label. If present, match RRs at "*"; copy with owner set to QNAME. If not present, set authoritative name error if original QNAME, else exit.
4. Search cache for QNAME; if found, copy matching RRs into answer section. Look for best delegation from cache. Go to step 6.
5. Use local resolver algorithm to answer query recursively. Store results (including CNAMEs) in answer section.
6. Add additional RRs as appropriate.

#### 4.3.3. Wildcards
Wildcard RRs have owner name "*.<anydomain>". They are used to synthesize RRs for names that do not exist but are descendants of <anydomain>. Wildcards do not apply when query name is in another zone, or when any name between wildcard domain and query name exists (including <anydomain> itself). A * label in a query name has no special effect.

#### 4.3.4. Negative Response Caching (Optional)
Name servers may include an SOA RR in the additional section of authoritative responses (error or empty answer) to indicate the MINIMUM TTL for caching negative results. Resolvers may cache negative results; strongly recommended but not required. All resolvers must at least ignore the SOA when present.

#### 4.3.5. Zone Maintenance and Transfers
One master (primary) server; changes coordinated there. Secondary servers periodically check serial number from SOA using REFRESH, RETRY, EXPIRE parameters. If serial changes, secondary requests AXFR using TCP. Secondaries may also transfer from other secondaries. Serial advances use sequence space arithmetic.

## 5. Resolvers
### 5.1. Introduction
Resolvers interface user programs to name servers. They may cache results to reduce delay and load. Shared caches are more efficient.

### 5.2. Client-Resolvers Interface
#### 5.2.1. Typical Functions
Three typical functions:
1. **Host name to address**: Given a character string, returns one or more 32-bit IP addresses (type A query).
2. **Host address to name**: Given IP address, perform PTR query on reversed octets with "IN-ADDR.ARPA".
3. **General lookup**: Given QNAME, QTYPE, QCLASS, returns matching RRs.

Results: data RRs, name error (NE) if name does not exist, or data not found error if name exists but type not present.

#### 5.2.2. Aliases
When resolving, if CNAME is found and QTYPE not CNAME, resolver should restart query at canonical name. For general function, aliases not pursued if QTYPE is CNAME. Multiple aliases should not be signalled as error; loops and pointers to non-existent names should be caught.

#### 5.2.3. Temporary Failures
Resolvers must distinguish temporary failures from name/data not found. Temporary failure should be a possible result; blocking indefinitely is usually not good.

### 5.3. Resolver Internals
#### 5.3.1. Stub Resolvers
Stub resolvers offload resolution to a recursive name server. Need a configuration file listing server addresses. User must verify servers provide recursive service. Drawbacks: retransmission optimization, overload if misinterpreted.

#### 5.3.2. Resources
Resolvers may share zones with a local name server; authoritative data always preferred over cached data.

#### 5.3.3. Algorithm
Data structures: SNAME, STYPE, SCLASS, SLIST (current best servers), SBELT (safety belt), CACHE.
Algorithm steps:
1. Check local information (cache and authoritative zones). If answer found, return to client.
2. Find best servers: search for NS RRs starting at SNAME, then parent, etc. If none, use SBELT (configured servers, e.g., root and local servers).
3. Send queries to servers in SLIST, cycling through addresses with timeouts.
4. Analyze response:
   - If answer or name error: cache data and return to client.
   - If closer delegation: cache delegation, update SLIST, go to step 2.
   - If CNAME and not answer: cache CNAME, change SNAME, go to step 1.
   - If server failure: delete server from SLIST, go to step 3.
Priorities: bound work, get answer, avoid unnecessary transmissions, get answer quickly.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Brother nodes shall not have the same label. | shall | Section 3.1 |
| R2 | Total octets representing a domain name shall be limited to 255. | shall | Section 3.1 |
| R3 | A CNAME RR at a node shall not allow any other data at that node. | shall | Section 3.6.2 |
| R4 | All name servers must implement non-recursive queries. | must | Section 4.3.1 |
| R5 | Every zone must be available on at least two servers. | must | Section 4.1 |
| R6 | Resolvers must be able to access at least one name server. | must | implied (Section 2.4, 5.1) |
| R7 | Name servers shall not perform recursive service unless asked via RD. | shall | Section 4.3.1 |
| R8 | Inverse queries are NOT an acceptable method for mapping host addresses to host names; use IN-ADDR.ARPA. | shall not | Section 3.7.2 |
| R9 | Wildcard RRs do not apply when the query is in another zone. | normative statement | Section 4.3.3 |
| R10 | Resolvers must be able to ignore SOA RR in negative caching responses. | must | Section 4.3.4 |

## Informative Annexes (Condensed)
- **Section 6 (Scenario)**: Detailed examples of name server configurations and query/response flows illustrating operation of root, MIL, EDU, MIT.EDU, ISI.EDU zones. Includes sample master files and step-by-step resolution of MX, PTR, and A queries. Useful for understanding protocol dynamics but not normative.
- **Section 7 (References and Bibliography)**: Lists 27 references including earlier DNS RFCs, IENs, and related standards. Many are obsoleted or superseded; current relevant references are RFC-1035, RFC-1032, RFC-1033, and RFC-1031.
- **Index**: A keyword index from the original document is preserved in the source; omitted here for brevity.