# RFC 952: DOD Internet Host Table Specification
**Source**: DDC DCA/DDN NIC | **Version**: RFC 952 (Obsoletes RFC 810, 608) | **Date**: October 1985 | **Type**: Normative
**Original**: https://tools.ietf.org/html/rfc952

## Scope (Summary)
This RFC specifies the format of the DoD Internet Host Table, used by the DoD Hostname Server. It defines rules for host names, addresses, and the structure of table entries.

## Normative References
- RFC 921: Domain Name System Implementation Schedule
- RFC 943: Assigned Numbers
- RFC 953: Hostname Server
- RFC 791: Internet Protocol
- RFC 796: Address Mappings
- RFC 810: Official DoD Internet Host Table Specification (Obsoleted)
- RFC 608: Host Names Online (Obsoleted)

## Definitions and Abbreviations
- **Name**: A text string up to 24 characters drawn from A-Z, 0-9, minus (-), and period (.). No spaces. Case-insensitive. First character must be alpha. Last character must not be a minus sign or period.
- **Internet Address**: 32-bit address represented as four decimal octets separated by periods.
- **Class A Address**: First bit 0; next 7 bits define network number.
- **Class B Address**: First two bits 1,0; next 14 bits define network number.
- **Class C Address**: First three bits 1,1,0; next 21 bits define network number.
- **LOCAL ADDRESS**: Portion of address identifying a host within the specified network.
- **NET**: Keyword for network entry.
- **GATEWAY**: Keyword for gateway entry. A host serving as a gateway must have "-GATEWAY" or "-GW" as part of its name.
- **HOST**: Keyword for host entry.
- **DOMAIN**: Keyword for domain entry.
- **TAC**: Must have "-TAC" as the last part of its host name (if DoD host). Single character names or nicknames not allowed.

## Assumptions (Normative)
1. **Name Characters**: Must be a text string up to 24 characters drawn from A-Z, 0-9, minus (-), and period (.). Periods only allowed to delimit domain style components. No blanks. Case-insensitive. First character must be alpha. Last character must not be a minus sign or period.
2. **Gateway Naming**: A host that serves as a GATEWAY should have "-GATEWAY" or "-GW" as part of its name. Hosts that do not serve as Internet gateways shall not use "-GATEWAY" or "-GW". A host that is a TAC must have "-TAC" as the last part of its host name (if DoD host). Single character names or nicknames are not allowed.
3. **Address Representation**: Each address is represented by four decimal numbers separated by a period, each representing 1 octet. Address classes as defined in RFC 943.
4. **ARPANET/MILNET Mapping**: For Class A networks (ARPANET=10, MILNET=26), LOCAL ADDRESS: second octet = physical host, third = logical host, fourth = PSN (IMP).
5. **Registration**: Names and addresses for DoD hosts and gateways shall be negotiated and registered with the DDN PMO, and subsequently with the NIC, before being used and before traffic is passed by a DoD host. Names and addresses for domains and networks shall be registered with the DDN Network Information Center (HOSTMASTER@SRI-NIC.ARPA) or 800-235-3155.
6. **User Responsibility**: It is the responsibility of the users of this host table to translate it into whatever format is needed for their purposes.

## Syntax and Conventions (Normative)
- **; (semicolon)**: Denotes comment to end of line.
- **Keywords**: `NET`, `GATEWAY`, `HOST`, `DOMAIN` – each introduces an entry.
- **: (colon)**: Field delimiter.
- **:: (double colon)**: Indicates null field.
- **, (comma)**: Data element delimiter.
- **XXX/YYY**: Protocol information type TRANSPORT/SERVICE. Options: "FOO/BAR" (both known), "FOO" (transport known), "BAR" (service known).
- **Entry Structure**: Each entry is an ASCII text string with 6 fields:
  - Field 1: Keyword (NET, GATEWAY, HOST, DOMAIN). NET entries cannot have alternate addresses or nicknames. DOMAIN entries do not use fields 4-6.
  - Field 2: Internet Address(es) followed by alternate addresses (comma separated). For Domains, addresses where a Domain Name Server exists.
  - Field 3: Official Name (with optional nicknames). Hosts may have optional nicknames (discouraged except for transitions). NET names must not have nicknames.
  - Field 4: Machine Type (optional).
  - Field 5: Operating System (optional).
  - Field 6: Protocol List (optional).
- Fields 4-6 pertain to the first address in Field 2.
- Blanks (spaces/tabs) ignored between data elements or fields, but disallowed within a data element.
- Each entry ends with a colon.
- Entries grouped by type: Domain, Net, Gateway, Host. Order within type unspecified.

## Grammatical Host Table Specification (Normative)
### A. Parsing Grammar
```
<entry> ::= <keyword> ":" <addresses> ":" <names> [":" [<cputype>]
    [":" [<opsys>]  [":" [<protocol list>] ]]] ":"
<addresses> ::= <address> *["," <address>]
<address> ::= <octet> "." <octet> "." <octet> "." <octet>
<octet> ::= <0 to 255 decimal>
<names> ::= <netname> | <gatename> | <domainname> *["," <nicknames>]
    | <official hostname> *["," <nicknames>]
<netname>  ::= <name>
<gatename> ::= <hname>
<domainname> ::= <hname>
<official hostname> ::= <hname>
<nickname> ::= <hname>
<protocol list> ::= <protocol spec> *["," <protocol spec>]
<protocol spec> ::= <transport name> "/" <service name>
    | <raw protocol name>
```
### B. Lexical Grammar
```
<entry-field> ::= <entry-text> [<cr><lf> <blank> <entry-field>]
<entry-text>  ::= <print-char> *<text>
<blank> ::= <space-or-tab> [<blank>]
<keyword> ::= NET | GATEWAY | HOST | DOMAIN
<hname> ::= <name>*["."<name>]
<name>  ::= <let>[*[<let-or-digit-or-hyphen>]<let-or-digit>]
<cputype> ::= PDP-11/70 | DEC-1080 | C/30 | CDC-6400...etc.
<opsys>   ::= ITS | MULTICS | TOPS20 | UNIX...etc.
<transport name> ::= TCP | NCP | UDP | IP...etc.
<service name> ::= TELNET | FTP | SMTP | MTP...etc.
<raw protocol name> ::= <name>
<comment> ::= ";" <text><cr><lf>
<text>    ::= *[<print-char> | <blank>]
<print-char>  ::= <any printing char (not space or tab)>
```
Note: Continuation lines (lines beginning with at least one blank) may be used anywhere blanks are allowed to split an entry across lines.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Name must be ≤24 chars, alpha first, not last char minus/period, no spaces. | shall | Assumption 1 |
| R2 | Gateway must have "-GATEWAY" or "-GW" in name; non-gateways must not. | shall | Assumption 2 |
| R3 | TAC must have "-TAC" as last part (if DoD). | shall | Assumption 2 |
| R4 | Single character names/nicknames are not allowed. | shall | Assumption 2 |
| R5 | DoD host/gateway names must be registered with DDN PMO and NIC before use. | shall | Assumption 7 |
| R6 | Domain/network registration must be with NIC. | shall | Assumption 7 |
| R7 | Host table entries must follow the specified grammatical syntax (fields, delimiters, etc.). | shall | Syntax and Conventions, Grammatical Specification |

## Informative Annexes (Condensed)
- **Example of Host Table Format**: Shows examples of NET, GATEWAY, HOST entries with addresses, names, machine type, OS, protocol list. Provided for illustration only.
- **Bibliography**: Lists seven references including prior RFCs and standards (RFC 810, 953, 608, 791, 796, 921, 943). These are the sources for definitions and context.