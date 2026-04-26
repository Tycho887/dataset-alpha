# RFC 7071: A Media Type for Reputation Interchange
**Source**: IETF | **Version**: Standards Track | **Date**: November 2013 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc7071

## Scope (Summary)
Defines the format of reputation response data (reputons), the media type `application/reputon+json` for packaging it, and a registry for reputation application names and response sets.

## Normative References
- [JSON] Crockford, D., "The application/json Media Type for JavaScript Object Notation (JSON)", RFC 4627, July 2006.
- [KEYWORDS] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC7070] Borenstein, N., Kucherawy, M., and A. Sullivan, "An Architecture for Reputation Reporting", RFC 7070, November 2013.
- [RFC7072] Borenstein, N. and M. Kucherawy, "A Reputation Query Protocol", RFC 7072, November 2013.

## Definitions and Abbreviations
- **Reputon**: A single independent object containing reputation information. A query about a subject receives one or more reputons.
- **Key Words**: The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [KEYWORDS].
- **Other Definitions**: Other important terms are defined in [RFC7070].

## Description
Reputons are represented using JSON (JavaScript Object Notation) per [JSON]. The media type `application/reputon+json` is defined for the JSON representation of reputational data, typically in response to a client request. This media type takes no parameters. The body is a JSON document containing the requested reputation information; the root object includes an "application" member (the application context per Section 5.1 of [RFC7070]) and a "reputons" member (an array of reputon objects). The application name refers to a registration under Section 7.2, which defines valid assertions and extensions.

### Reputon Attributes
- **rater** (REQUIRED): Identity of the aggregator/computing entity, typically a DNS domain name.
- **assertion** (REQUIRED): The specific claim being rated.
- **rated** (REQUIRED): Identity of the entity being rated; application-specific syntax.
- **rating** (REQUIRED): Overall rating score, expressed as a floating-point number between 0.0 and 1.0 inclusive. See Section 4.
- **confidence** (OPTIONAL): Certainty level, floating-point between 0.0 and 1.0.
- **normal-rating** (OPTIONAL): Expected typical rating for the subject.
- **sample-size** (OPTIONAL): Approximate number of data points used, unsigned 64-bit integer.
- **generated** (OPTIONAL): Timestamp (seconds since 1970-01-01 00:00 UTC) when value was generated.
- **expires** (OPTIONAL): Timestamp beyond which the score is likely invalid (seconds since epoch). See Section 5.
- Applications may register additional attribute/value pairs.

## Ratings
The `rating` value is a floating-point number between 0.0 and 1.0 inclusive. 1.0 implies full agreement with the assertion; 0.0 indicates no support. Application definitions must declare anchor meanings and the scale type, to be adhered to by all providers for that application.

## Caching
- The `expires` field indicates a timestamp after which the client **SHOULD NOT** use the rating and **SHOULD** issue a new query.
- No caching mandate, but operational benefits exist. Cached (stale) ratings can cause misidentification.
- Reputation data is most volatile for young subjects; if expiration timestamps are included, they **SHOULD** be lower for subjects with little data.

## Reputons

### Syntax
A reputon is a JSON object of key-value pairs. The keys are attribute names (standard or application-specific); the set of allowed keys for an application is its "response set". A reputon typically replies to a specific assertion query. A client may request all assertions for a subject. An empty reputon indicates "no data available" (semantically equivalent to `sample-size: 0`).

### Formal Definition
Uses JSON terms from [JSON] (OBJECT, MEMBER, ARRAY, NUMBER, etc.).

**Structure (normative)**:
- `reputation-object`: OBJECT containing MEMBER `reputation-context` and MEMBER `reputon-list`.
- `reputation-context`: MEMBER with MEMBER-NAME "application" and MEMBER-VALUE a STRING.
- `reputon-list`: MEMBER with MEMBER-NAME "reputons" and MEMBER-VALUE a `reputon-array`.
- `reputon-array`: ARRAY where each ARRAY-VALUE is a `reputon`.
- `reputon`: OBJECT where each MEMBER is a `reputon-element`.
- `reputon-element`: one of `rater-value`, `assertion-value`, `rated-value`, `rating-value`, `conf-value`, `normal-value`, `sample-value`, `gen-value`, `expire-value`, `ext-value`. **Order not significant**. Each specific element **MUST NOT** appear more than once. `rater-value`, `assertion-value`, `rated-value`, and `rating-value` are **REQUIRED**.
- Each element definition specifies MEMBER-NAME and MEMBER-VALUE constraints (e.g., `rating-value`: MEMBER-NAME "rating", MEMBER-VALUE a NUMBER in [0.0, 1.0]; `sample-value`: non-negative INTEGER; etc.).
- `ext-value`: for extensions; MEMBER-NAME and MEMBER-VALUE defined in separate application registrations.

### Examples (Informative, summarized)
The section shows simple and extended JSON examples, including email-id application with extensions. They illustrate how reputons convey ratings, confidence, sample size, and timestamps.

## IANA Considerations

### 7.1 application/reputon+json Media Type Registration
- **Type name**: application
- **Subtype name**: reputon+json
- **Required parameters**: none
- **Optional parameters**: none
- **Encoding considerations**: 7bit sufficient for readability.
- **Security considerations**: See Section 8 of [RFC7071].
- **Interoperability considerations**: Unsupported values are to be ignored.
- **Published specification**: [RFC7071]
- **Intended usage**: COMMON
- **Change controller**: IESG
- (Other fields as per registration template.)

### 7.2 Reputation Applications Registry
IANA created the "Reputation Applications" registry. New registrations or updates follow "IETF Review" or "Specification Required" guidelines per [IANA-CONSIDERATIONS]. Each registration must contain:
1. Symbolic name (conforming to MIME "token" ABNF).
2. Short description of the application.
3. Reference document.
4. Status: current, deprecated, or historic.

Required specification details:
- Application symbolic name.
- Description and legal syntax for the subject of a query.
- Optional query parameter table (Name, Status, Description, Syntax, Required).
- List of one or more assertions (Name, Description with meanings of 0.0 and 1.0, Scale description).
- Optional list of extension keys (Name, Description, Syntax).
- Registered attribute names should be prefixed by the application name to avoid namespace collisions.

Designated Expert confirms the specification meets minima.

## Security Considerations
This document primarily registers a media type and does not describe a new protocol introducing security considerations. General security and operational impacts of using reputation services are discussed in [CONSIDERATIONS].

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Reputon MUST contain the REQUIRED attributes: rater, assertion, rated, rating. | shall | Section 3.1, 6.2.2 |
| R2 | Reputon MUST NOT contain duplicate members. | shall | Section 6.2.2 |
| R3 | Rating value MUST be a floating-point number between 0.0 and 1.0 inclusive, with at most three decimal places of precision (SHOULD NOT have more). | shall / should | Section 4, 6.2.2 |
| R4 | Media type `application/reputon+json` takes no parameters. | shall | Section 3, 7.1 |
| R5 | Client SHOULD NOT use a rating after the `expires` timestamp and SHOULD issue a new query. | should | Section 5 |
| R6 | If expiration timestamps are included, they SHOULD be lower for subjects with little data. | should | Section 5 |
| R7 | Reputation-object MUST contain an "application" member and a "reputons" member. | shall | Section 6.2.2 |
| R8 | New registry entries must include symbolic name, description, reference, and status. | shall | Section 7.2 |
| R9 | Application specification must include assertion list with scale and anchor meanings. | shall | Section 7.2 |
| R10 | Extension keys should be prefixed with application name. | should | Section 7.2 |

## Informative Annexes (Condensed)
- **Appendix A. Acknowledgments**: The authors thank Frank Ellermann, Tony Hansen, Jeff Hodges, Simon Hunt, John Levine, David F. Skoll, and Mykyta Yevstifeyev for contributions.
- **Section 6.3 Examples**: Several JSON examples illustrate simple and extended reputons, including the `email-id` application with extensions and multiple reputons for different identities.
- **Section 7.1 Media Type Registration**: The full registration template is provided, including contact information, intended usage COMMON, and change controller IESG.