# RFC 1535: A Security Problem and Proposed Correction With Widely Deployed DNS Software
**Source**: IETF | **Version**: Informational | **Date**: October 1993 | **Type**: Informative  
**Original**: https://tools.ietf.org/html/rfc1535

## Scope (Summary)
This document identifies a security weakness in DNS resolver clients (BSD BIND-based) that use an implicit search heuristic when resolving partial domain names. It describes how this heuristic can be exploited to intercept traffic (e.g., via wildcard CNAME), and proposes corrections to limit searches to locally administered portions of the name space.

## Normative References
- [1] Mockapetris, P., "Domain Names Concepts and Facilities", STD 13, RFC 1034, November 1987.
- [2] Mockapetris, P., "Domain Names Implementation and Specification", STD 13, RFC 1035, November 1987.
- [3] Partridge, C., "Mail Routing and the Domain System", STD 14, RFC 974, January 1986.
- [4] Kumar, A., Postel, J., Neuman, C., Danzig, P., and S. Miller, "Common DNS Implementation Errors and Suggested Fixes", RFC 1536, October 1993.
- [5] Beertema, P., "Common DNS Data File Configuration Errors", RFC 1537, October 1993.

## Definitions and Abbreviations
- **FQDN**: Fully Qualified Domain Name – a domain name rooted at the DNS root (ends with a '.').
- **Partial Name**: A domain name not terminated with a '.'.
- **Implicit Search List**: A list of domain suffixes derived automatically from the searching host's domain name, used to append to partial names.
- **Explicit Search List**: A search list configured manually by the administrator.
- **Local Administration**: The portion of the domain name space for which a particular administrator has authority.
- **Public Administration**: Top-level domains and sub-domains under public authority (e.g., .COM, .EDU, country codes).

## Flaw and Security Issue
### Flaw
- Most BSD BIND-based resolvers attempt to resolve a partial name by appending each suffix in an implicit search list (derived from the resolver’s own domain) until a DNS record is found.
- **Example**: Resolving `UnivHost.University.EDU` from `Machine.Tech.ACES.COM` tries:
  1. `UnivHost.University.EDU.Tech.ACES.COM.`
  2. `UnivHost.University.EDU.ACES.COM.`
  3. `UnivHost.University.EDU.COM.`
  4. `UnivHost.University.EDU.`
- This heuristic is disabled by default in BIND 4.9.2.

### Security Issue
- Registering a domain such as `EDU.COM` and using a wildcard CNAME allows interception of all connections from `.COM` sites to any `.EDU` host, routing them to a target machine.
- **Example**: `harvard.edu.com. CNAME targethost` would redirect all connects to Harvard.edu from .com sites to `targethost` (which could present a fake login banner).
- The same vulnerability exists with any combination of top-level domains (e.g., COM.EDU, MIL.GOV, GOV.COM).

### Public vs. Local Name Space Administration
- The DNS hierarchy allows delegation, but existing resolvers do **not** distinguish between locally administered and publicly administered portions of the searching host's domain.
- The implicit search can “intercept” by matching unintended values outside local control, which is unacceptable.

## Remediation
### Proposed Minimum Correction
- **R1**: DNS resolvers **must** honor the boundary between local and public administration by limiting any search lists to locally administered portions of the domain name space.
- **R2**: A parameter showing the scope of the name space controlled by the local administrator **must** be available.
- **Effect**: Progressive searches are permitted only up through the locally controlled domain, not beyond.

### BIND 4.9.2 Implementation (More Stringent)
- **R3**: The DNS resolver client **shall** narrow its implicit search list (if any) to try only the first and last of the examples (i.e., host.domain.local and host.domain).
- **R4**: Any additional search alternatives **must** be configured into the resolver explicitly.
- **R5**: DNS name resolver software **should not** use implicit search lists in attempts to resolve partial names into absolute FQDNs other than the host's immediate parent domain.
- **R6**: Resolvers that continue to use implicit search lists **must** limit their scope to locally administered sub-domains.
- **R7**: DNS name resolver software **should not** come pre-configured with explicit search lists that perpetuate this problem.
- **R8**: In any event where a "." exists in a specified name, it **should** be assumed to be a fully qualified domain name (FQDN) and **should** be tried as a rooted name first.

### Impact and Transition
- Organizations using multi-part, partially qualified domain names (e.g., `foo.loc1.org.city.state.us`) may need to update explicit search lists to include each desired suffix (e.g., `org.city.state.us`).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | DNS resolvers must honor the boundary between local and public administration by limiting search lists to locally administered portions. | must | Solution(s) |
| R2 | A parameter showing the scope of locally controlled name space must be available. | must | Solution(s) |
| R3 | Implicit search list should be narrowed to first and last attempts only. | shall (implementation specific) | BIND 4.9.2 (stringent) |
| R4 | Additional search alternatives must be configured explicitly. | must | BIND 4.9.2 (stringent) |
| R5 | DNS resolver software should not use implicit search lists beyond immediate parent domain. | should | Solution(s) |
| R6 | Resolvers using implicit search lists must limit scope to locally administered sub-domains. | must | Solution(s) |
| R7 | DNS resolver software should not ship with pre-configured explicit search lists that perpetuate the problem. | should | Solution(s) |
| R8 | If a "." exists in a name, it should be treated as an FQDN and tried as rooted first. | should | Solution(s) |

## Security Considerations (Summary)
This memo highlights a vulnerability in overly forgiving DNS client search heuristics that can be exploited to intercept and redirect traffic. The proposed corrections eliminate the potential for such exploitation by enforcing boundaries between local and public name space administration.

## Author's Address
Ehud Gavron, ACES Research Inc., PO Box 14546, Tucson, AZ 85711, Phone: (602) 743-9841, Email: gavron@aces.com