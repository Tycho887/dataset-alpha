# RFC 3305: Report from the Joint W3C/IETF URI Planning Interest Group: Uniform Resource Identifiers (URIs), URLs, and Uniform Resource Names (URNs): Clarifications and Recommendations
**Source**: W3C URI Interest Group / IETF | **Version**: August 2002 | **Date**: August 2002 | **Type**: Informational
**Original**: https://www.ietf.org/rfc/rfc3305.txt

## Scope (Summary)
This document clarifies the relationship between URIs, URLs, and URNs, resolves confusion between “classical” and “contemporary” views of URI space, and describes registration procedures for URI schemes and URN namespace IDs (NIDs). It provides recommendations for the W3C and IETF to standardize terminology and update registration processes.

## Normative References
- [1] Petke, R. and I. King, "Registration Procedures for URL Scheme Names", BCP 35, RFC 2717, November 1999.
- [2] Masinter, L., Alvestrand, H., Zigmond, D. and R. Petke, "Guidelines for new URL Schemes", RFC 2718, November 1999.
- [3] Moats, R., "A URN Namespace for IETF Documents", RFC 2648, August 1999.
- [4] Mealling, M., "The Network Solutions Personal Internet Name (PIN): A URN Namespace for People and Organizations", RFC 3043, January 2001.
- [5] Rozenfeld, S., "Using The ISSN (International Serial Standard Number) as URN (Uniform Resource Names) within an ISSN-URN Namespace", RFC 3044, January 2001.
- [6] Mealling, M., "A URN Namespace of Object Identifiers", RFC 3061, February 2001.
- [7] Coates, A., Allen, D. and D. Rivers-Moore, "URN Namespace for NewsML Resources", RFC 3085, March 2001.
- [8] Best, K. and N. Walsh, "A URN Namespace for OASIS", RFC 3121, June 2001.
- [9] Best, K. and N. Walsh, "A URN Namespace for XML.org", RFC 3120, June 2001.
- [10] Walsh, N., Cowan, J. and P. Grosso, "A URN Namespace for Public Identifiers", RFC 3151, August 2001.
- [11] Daigle, L., van Gulik, D., Iannella, R. and P. Faltstrom, "URN Namespace Definition Mechanisms", BCP 33, RFC 2611, June 1999.
- [12] Berners-Lee, T., Fielding, R. and L. Masinter, "Uniform Resource Identifiers (URI): Generic Syntax", RFC 2396, August 1998.
- [13] Sollins, K., "Architectural Principles of Uniform Resource Name Resolution", RFC 2276, January 1998.
- [14] Fielding, R., Gettys, J., Mogul, J., Nielsen, H., Masinter, L., Leach, P. and T. Berners-Lee, "Hypertext Transfer Protocol -- HTTP/1.1", RFC 2616, June 1999.
- [15] Hakala, J. and H. Walravens, "Using International Standard Book Numbers as Uniform Resource Names", RFC 3187, October 2001.
- [16] Hakala, J., "Using National Bibliography Numbers as Uniform Resource Names", RFC 3188, October 2001.

## Definitions and Abbreviations
- **URI**: Uniform Resource Identifier – the generic set of all resource identifiers.
- **URL**: Uniform Resource Locator – an informal subclass of URI that identifies a resource via its primary access mechanism (e.g., network location). The term "URL scheme" is used infrequently, usually to refer to URI schemes that exclude URNs.
- **URN**: Uniform Resource Name – a URI with the scheme "urn:" that defines a namespace of persistent, location-independent identifiers. URN namespaces are identified by a Namespace ID (NID).
- **NID**: Namespace ID – the unique identifier for a URN namespace (e.g., "isbn", "ietf").
- **Classical View**: URI space partitioned into two (or more) classes: URL and URN. Under this view, a URI is either a URL or a URN.
- **Contemporary View**: URI space is not partitioned; individual URI schemes are not required to be classified as URL or URN. "URL" is an informal concept. A URI scheme may define subspaces (e.g., "urn:" defines namespaces).
- **IANA**: Internet Assigned Numbers Authority – maintains the official registries for URI schemes and URN NIDs.
- **IETF Tree**: The tree for URI schemes of general interest to the Internet community, requiring RFC publication for registration (per RFC 2717).
- **Public Schemes**: URI schemes for which a public document exists describing them (registered or unregistered).
- **Private Schemes**: URI schemes used internally without public documentation.

## 1. The W3C URI Interest Group
- The W3C formed a planning group in October 2000 to evaluate opportunities for work on URIs. The group included W3C members and invited IETF experts. This document presents the group’s recommendations for continued work.

## 2. URI Partitioning
### 2.1 Classical View
- Early (mid-90s) assumption: identifiers are either URLs (location) or URNs (name). URI space partitioned into URL, URN, and possibly other classes (e.g., URC). No other class gained acceptance.

### 2.2 Contemporary View
- The hierarchical classification of URI types became less important. URI schemes define subspaces directly. "URL" is an informal term; an http URI is a URL. "URN" is a URI scheme (urn:) that defines namespaces (e.g., urn:isbn...). The term "URL scheme" is now used infrequently to refer to URI schemes excluding URNs.

### 2.3 Confusion
- Documents (RFCs) spanning both periods lead to interchangeable use of "URL" and "URI", causing confusion in the broader community. RFC 2396 §1.2 attempted to clarify but was insufficient.

## 3. Registration
### 3.1 URI Schemes
#### 3.1.1 Registered URI Schemes
- IANA maintains the official register at http://www.iana.org/assignments/uri-schemes. As of publication, 34 schemes are listed, plus a few reserved names.

#### 3.1.2 Unregistered URI Schemes
##### 3.1.2.1 Public Unregistered Schemes
- Dan Connolly’s list (http://www.w3.org/Addressing/schemes) includes ~85 known public URI schemes, ~50 of which are unregistered. Some are obsolete (e.g., "phone" superseded by "tel").

##### 3.1.2.2 Private Schemes
- Difficult to enumerate. Observed: Microsoft may have 20–40 with 2–3 added per day; WebTV had 24 with 6 added per year (as of August 1997 IETF meeting).

#### 3.1.3 Registration of URI Schemes
- RFC 2717 ("Registration Procedures for URL Scheme Names") specifies procedures and references RFC 2718 ("Guidelines for new URL Schemes"). These documents use "URL" but actually apply to URIs in general. One recommendation (Section 5) is to update these RFCs to use the term "URI" instead of "URL".

##### 3.1.3.1 IETF Tree
- For schemes of general interest. Registration requires publication of syntax and semantics in an RFC.

##### 3.1.3.2 Other Trees
- RFC 2717 describes alternative trees (e.g., a vendor-supplied "vnd" tree pending). URI schemes in alternative trees will contain a "." in the scheme name. No alternative trees have been registered as of this RFC.

### 3.2 URN Namespaces
- A URN namespace is identified by a Namespace ID (NID) registered with IANA (see §3.2.4).

#### 3.2.1 Registered URN NIDs
Two categories:
- **Informal**: Form "urn-<number>" – four registered: urn-1, urn-2, urn-3, urn-4.
- **Formal**: IANA list at http://www.iana.org/assignments/urn-namespaces lists ten registered NIDs as of publication:
  * `ietf` (RFC 2648)
  * `pin` (RFC 3043)
  * `issn` (RFC 3044)
  * `oid` (RFC 3061)
  * `newsml` (RFC 3085)
  * `oasis` (RFC 3121)
  * `xmlorg` (RFC 3120)
  * `publicid` (RFC 3151)
  * `isbn` (RFC 3187)
  * `nbn` (RFC 3188)

#### 3.2.2 Pending URN NIDs
- There are pending requests, but no formal tracking mechanism exists. Recommendation: provide a means to track status (e.g., for 'isbn').

#### 3.2.3 Unregistered NIDs
- Some entities maintain namespaces appropriate as URNs but have not registered (e.g., 'hdl'). The uncertainty about whether to register as a URI scheme or URN namespace impedes registration.

#### 3.2.4 Registration Procedures for URN NIDs
- RFC 2611 ("URN Namespace Definition Mechanisms") specifies the procedure. A request must describe:
  * Structural characteristics of identifiers (e.g., caching/shortcuts)
  * Specific character encoding rules
  * Relevant RFCs/standards explaining namespace structure
  * Identifier uniqueness considerations
  * Delegation of assignment authority
  * Identifier persistence considerations
  * Quality of service considerations
  * Resolution process
  * Rules for lexical equivalence
  * Conformance with URN syntax (especially for legacy naming systems)
  * Validation mechanisms
  * Scope (e.g., "United States social security numbers")

## 4. Additional URI Issues
- Unresolved issues not fully considered in this paper, including:
  - Use of URIs for non-network resources (abstract objects, physical objects, persons).
  - International Resource Identifiers (IRIs): extension to non-ASCII characters.

## 5. Recommendations
The Interest Group recommends:

1.   The W3C and IETF should jointly develop and endorse a model for URIs, URLs, and URNs consistent with the "Contemporary View" described in Section 2.2, considering the additional issues listed in Section 4.

2.   RFCs 2717 and 2718 should be generalized to refer to "URI schemes" rather than "URL schemes", refined, and moved forward as Best Current Practices in the IETF.

3.   The registration procedures for alternative trees should be clarified in RFC 2717.

4.   Public, but unregistered schemes, should become registered where possible. Obsolete schemes should be purged or clearly marked as obsolete.

5.   IANA registration information should be updated:
     *   Add 'urn' to the list of registered URI schemes with a pointer to the URN namespace registry.
     *   Maintain status information about pending registrations (URI schemes and URN NID requests).
     *   Ensure that the page is clearly identified as the official registry (e.g., add heading "This is the Official IANA Registry of URI Schemes").

## 6. Security Considerations
- This memo does not raise any known security threats.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | W3C and IETF should jointly develop and endorse a model for URIs, URLs, and URNs consistent with the Contemporary View (Section 2.2) and addressing additional issues (Section 4). | should | Section 5 (Rec. 1) |
| R2 | RFCs 2717 and 2718 should be generalized to refer to "URI schemes" instead of "URL schemes", refined, and moved forward as Best Current Practices. | should | Section 5 (Rec. 2) |
| R3 | Clarify registration procedures for alternative trees in RFC 2717. | should | Section 5 (Rec. 3) |
| R4 | Public unregistered URI schemes should become registered where possible; obsolete schemes should be purged or marked obsolete. | should | Section 5 (Rec. 4) |
| R5 | IANA registry should add 'urn' as a URI scheme with pointer to URN namespace registry, maintain pending registration status, and add heading declaring official registry. | should | Section 5 (Rec. 5) |
| R6 | Requests for URN NID registration shall include all features listed in Section 3.2.4 (structural characteristics, encoding rules, etc.). | described (normative reference to RFC 2611) | Section 3.2.4 (per RFC 2611) |
| R7 | URI scheme registration in the IETF tree shall require publication of syntax and semantics in an RFC. | shall | Section 3.1.3.1 (per RFC 2717) |

## Informative Annexes (Condensed)
- **Annex A – List of Registered URN NIDs (Section 3.2.1)**: Provides the formal list of ten NIDs as of publication, each with corresponding RFC. Serves as a snapshot of the official IANA registry.
- **Annex B – Additional URI Issues (Section 4)**: Enumerates unresolved topics (non-resource URIs, IRIs) that the Interest Group expects to be addressed in follow-on work.