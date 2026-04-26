# RFC 6648: Deprecating the "X-" Prefix and Similar Constructs in Application Protocols
**Source**: IETF | **Version**: BCP 178 (Best Current Practice) | **Date**: June 2012 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc6648

## Scope (Summary)
This document deprecates the historical use of "X-" and similar prefixes on textual parameter names in application protocols to distinguish standardized from unstandardized parameters. It provides normative recommendations for implementers, creators of new parameters, and protocol designers to eliminate reliance on this convention.

## Normative References
- **[RFC2119]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## Definitions and Abbreviations
- **"X-" convention**: The practice of prefixing unstandardized parameter names with "X-" (or similar constructs like "x.", "P-") to distinguish them from standardized parameters.
- **Application protocol**: A protocol using textual parameter names (e.g., media types, header fields, vCard properties) as opposed to numerical parameters.
- **Unstandardized parameter**: A parameter defined outside a recognized standards development organization or its registration procedures.
- **Standardized parameter**: A parameter defined in a specification produced by a recognized standards development organization or registered according to its processes.
- **BCP 9**: The Internet Standards Process (RFC 2026).
- **BCP 26**: Guidelines for Writing an IANA Considerations Section (RFC 5226).
- **BCP 82**: Assigning Experimental and Testing Numbers Considered Useful (RFC 3692).

## 1. Introduction (Summary)
Historically, protocol parameters were distinguished by prefixing "X-" to unstandardized names. This convention caused leakage of unstandardized names into the standards space, leading to interoperability issues and de facto standardization. This document deprecates the convention for new textual parameters, without addressing numerical parameters. It does not override existing specifications that mandate "X-" for specific protocols (e.g., RFC 5545). Key points:
- Parameter names SHOULD NOT be prefixed with "X-" or similar constructs.
- Implementations MUST NOT infer status from the presence or absence of "X-".
- Existing "X-" parameters may remain or be migrated at the discretion of their maintainers.

## 2. Recommendations for Implementers of Application Protocols
- **R1**: Implementations of application protocols **MUST NOT** make any assumptions about the status of a parameter, nor take automatic action regarding a parameter, based solely on the presence or absence of "X-" or a similar construct in the parameter's name.

## 3. Recommendations for Creators of New Parameters
- **R2**: Creators **SHOULD** assume that all parameters they create might become standardized, public, commonly deployed, or usable across multiple implementations.
- **R3**: Creators **SHOULD** employ meaningful parameter names that they have reason to believe are currently unused.
- **R4**: Creators **SHOULD NOT** prefix their parameter names with "X-" or similar constructs.
- **Note**: If the relevant parameter name space has conventions about associating parameter names with creators, a parameter name could incorporate the organization's name or primary domain name (e.g., "ExampleInc-foo", "com.example.foo").

## 4. Recommendations for Protocol Designers
- **R5**: Designers **SHOULD** establish registries with potentially unlimited value-spaces, defining both permanent and provisional registries if appropriate.
- **R6**: Designers **SHOULD** define simple, clear registration procedures.
- **R7**: Designers **SHOULD** mandate registration of all non-private parameters, independent of the form of the parameter names.
- **R8**: Designers **SHOULD NOT** prohibit parameters with an "X-" prefix or similar constructs from being registered.
- **R9**: Designers **MUST NOT** stipulate that a parameter with an "X-" prefix or similar constructs needs to be understood as unstandardized.
- **R10**: Designers **MUST NOT** stipulate that a parameter without an "X-" prefix or similar constructs needs to be understood as standardized.

## 5. Security Considerations
- **R11**: Implementations **MUST NOT** assume that standardized parameters are "secure" whereas unstandardized parameters are "insecure", based solely on the names of such parameters.
- Interoperability and migration issues with security-critical parameters can result in unnecessary vulnerabilities.

## 6. IANA Considerations
- This document does not modify current registration procedures for application protocols, but future updates may incorporate these best practices.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Implementations **MUST NOT** make assumptions about parameter status based on "X-" prefix. | MUST | Section 2 |
| R2 | Creators **SHOULD** assume parameters might become standardized. | SHOULD | Section 3, #1 |
| R3 | Creators **SHOULD** use meaningful, unused names. | SHOULD | Section 3, #2 |
| R4 | Creators **SHOULD NOT** prefix with "X-" or similar. | SHOULD NOT | Section 3, #3 |
| R5 | Protocol designers **SHOULD** establish registries with unlimited value-spaces. | SHOULD | Section 4, #1 |
| R6 | Protocol designers **SHOULD** define simple registration procedures. | SHOULD | Section 4, #2 |
| R7 | Protocol designers **SHOULD** mandate registration of non-private parameters. | SHOULD | Section 4, #3 |
| R8 | Protocol designers **SHOULD NOT** prohibit registration of "X-" prefixed parameters. | SHOULD NOT | Section 4, #4 |
| R9 | Protocol designers **MUST NOT** stipulate that "X-" prefixed parameters are unstandardized. | MUST NOT | Section 4, #5 |
| R10 | Protocol designers **MUST NOT** stipulate that non-"X-" parameters are standardized. | MUST NOT | Section 4, #6 |
| R11 | Implementations **MUST NOT** assume security based on parameter name prefix. | MUST NOT | Section 5 |

## Informative Annexes (Condensed)
- **Appendix A. Background**: Traces the origin of the "X-" convention from FTP (RFC 691, 1975) through email (RFC 822), HTTP, vCard, LDAP, and other protocols. Notes that later specifications (RFC 2822, RFC 5727) deprecated it. The two main motivations for using "X-" were future standardization experiments and implementation-specific/local extensions.
- **Appendix B. Analysis**: Explains the primary problem: unstandardized parameters "leak" into standardized space, causing migration and interoperability issues (e.g., "x-gzip" equivalence, "X-Archived-At"). Solutions include simpler registration rules (RFC 3864, RFC 4288) and separate permanent/provisional registries (RFC 4395). Addresses three objections: (1) confusion from similar names—blurred in practice; (2) collisions—names are cheap and creativity can avoid them; (3) BCP 82 for experimental numbers—irrelevant for textual names where the namespace is unlimited. Concludes that segregation of parameter space has few benefits and significant costs in interoperability.

## References
### Normative References
- **[RFC2119]**: Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

### Informative References
- **[BCP9]**: Bradner, S., "The Internet Standards Process – Revision 3", BCP 9, RFC 2026, October 1996.
- **[BCP26]**: Narten, T. and H. Alvestrand, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 5226, May 2008.
- **[BCP82]**: Narten, T., "Assigning Experimental and Testing Numbers Considered Useful", BCP 82, RFC 3692, January 2004.
- **[RFC691]**: Harvey, B., "One more try on the FTP", RFC 691, June 1975.
- **[RFC737]**: Harrenstien, K., "FTP extension: XSEN", RFC 737, October 1977.
- **[RFC743]**: Harrenstien, K., "FTP extension: XRSQ/XRCP", RFC 743, December 1977.
- **[RFC775]**: Mankins, D., Franklin, D., and A. Owen, "Directory oriented FTP commands", RFC 775, December 1980.
- **[RFC822]**: Crocker, D., "Standard for the format of ARPA Internet text messages", STD 11, RFC 822, August 1982.
- **[RFC1123]**: Braden, R., "Requirements for Internet Hosts - Application and Support", STD 3, RFC 1123, October 1989.
- **[RFC1154]**: Robinson, D. and R. Ullmann, "Encoding header field for internet messages", RFC 1154, April 1990.
- **[RFC2045]**: Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies", RFC 2045, November 1996.
- **[RFC2046]**: Freed, N. and N. Borenstein, "Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types", RFC 2046, November 1996.
- **[RFC2047]**: Moore, K., "MIME (Multipurpose Internet Mail Extensions) Part Three: Message Header Extensions for Non-ASCII Text", RFC 2047, November 1996.
- **[RFC2068]**: Fielding, R., Gettys, J., Mogul, J., Nielsen, H., and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2068, January 1997.
- **[RFC2426]**: Dawson, F. and T. Howes, "vCard MIME Directory Profile", RFC 2426, September 1998.
- **[RFC2616]**: Fielding, R., Gettys, J., Mogul, J., Frystyk, H., Masinter, L., Leach, P., and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- **[RFC2822]**: Resnick, P., "Internet Message Format", RFC 2822, April 2001.
- **[RFC2939]**: Droms, R., "Procedures and IANA Guidelines for Definition of New DHCP Options and Message Types", BCP 43, RFC 2939, September 2000.
- **[RFC3406]**: Daigle, L., van Gulik, D., Iannella, R., and P. Faltstrom, "Uniform Resource Names (URN) Namespace Definition Mechanisms", BCP 66, RFC 3406, October 2002.
- **[RFC3427]**: Mankin, A., Bradner, S., Mahy, R., Willis, D., Ott, J., and B. Rosen, "Change Process for the Session Initiation Protocol (SIP)", RFC 3427, December 2002.
- **[RFC3864]**: Klyne, G., Nottingham, M., and J. Mogul, "Registration Procedures for Message Header Fields", BCP 90, RFC 3864, September 2004.
- **[RFC3986]**: Berners-Lee, T., Fielding, R., and L. Masinter, "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, January 2005.
- **[RFC4122]**: Leach, P., Mealling, M., and R. Salz, "A Universally Unique IDentifier (UUID) URN Namespace", RFC 4122, July 2005.
- **[RFC4288]**: Freed, N. and J. Klensin, "Media Type Specifications and Registration Procedures", BCP 13, RFC 4288, December 2005.
- **[RFC4395]**: Hansen, T., Hardie, T., and L. Masinter, "Guidelines and Registration Procedures for New URI Schemes", BCP 35, RFC 4395, February 2006.
- **[RFC4512]**: Zeilenga, K., "Lightweight Directory Access Protocol (LDAP): Directory Information Models", RFC 4512, June 2006.
- **[RFC4566]**: Handley, M., Jacobson, V., and C. Perkins, "SDP: Session Description Protocol", RFC 4566, July 2006.
- **[RFC5064]**: Duerst, M., "The Archived-At Message Header Field", RFC 5064, December 2007.
- **[RFC5451]**: Kucherawy, M., "Message Header Field for Indicating Message Authentication Status", RFC 5451, April 2009.
- **[RFC5545]**: Desruisseaux, B., "Internet Calendaring and Scheduling Core Object Specification (iCalendar)", RFC 5545, September 2009.
- **[RFC5646]**: Phillips, A. and M. Davis, "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
- **[RFC5727]**: Peterson, J., Jennings, C., and R. Sparks, "Change Process for the Session Initiation Protocol (SIP) and the Real-time Applications and Infrastructure Area", BCP 67, RFC 5727, March 2010.