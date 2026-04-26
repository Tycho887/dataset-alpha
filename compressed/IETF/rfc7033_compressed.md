# RFC 7033: WebFinger
**Source**: Internet Engineering Task Force (IETF) | **Version**: Standards Track | **Date**: September 2013 | **Type**: Normative  
**Original**: https://tools.ietf.org/html/rfc7033

## Scope (Summary)
WebFinger is a protocol for discovering information about people or other entities on the Internet, identified by a URI, using standard HTTP methods over a secure transport. It returns a JSON Resource Descriptor (JRD) containing subject, aliases, properties, and links. The protocol is designed for static information and may be used by multiple applications.

## Normative References
- [1] RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- [2] RFC 2616: HTTP/1.1
- [3] RFC 5785: Defining Well-Known URIs
- [4] RFC 5988: Web Linking
- [5] RFC 4627: JSON Media Type
- [6] RFC 3986: URI Generic Syntax (STD 66)
- [7] W3C CORS: Cross-Origin Resource Sharing
- [8] IANA Link Relations Registry
- [9] IANA MIME Media Types
- [10] RFC 6838: Media Type Specifications and Registration Procedures (BCP 13)
- [11] RFC 5646: Tags for Identifying Languages (BCP 47)
- [12] RFC 2818: HTTP Over TLS
- [13] RFC 5226: Guidelines for Writing an IANA Considerations Section (BCP 26)

## Definitions and Abbreviations
- **WebFinger resource**: The well-known URI path `/.well-known/webfinger` served over HTTPS.
- **query target**: The URI (resource parameter) identifying the entity whose information is sought.
- **link relation**: An attribute-value pair where the attribute identifies the type of relationship between the entity and the linked information. In WebFinger, the value of `rel` MUST be either an IANA-registered link relation type or a URI.
- **JRD**: JSON Resource Descriptor – a JSON object with members `subject`, `aliases`, `properties`, `links`.
- **CORS**: Cross-Origin Resource Sharing.
- **Normative keywords**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (per RFC 2119).

## WebFinger Protocol

### 4.1 Constructing the Query Component
- [R1] **Resource parameter**: A WebFinger URI MUST contain a query component with a `resource` parameter and MAY contain one or more `rel` parameters (Section 4.1).
- [R2] **Encoding**: Parameter values MUST be percent-encoded per RFC 3986 Section 2.1, including `=` and `&` characters within values (Section 4.1).
- [R3] **No spaces**: The client MUST NOT insert spaces while constructing the query string (Section 4.1).

### 4.2 Performing a WebFinger Query
- [R4] **Method**: Client issues query using GET method to `/.well-known/webfinger` (Section 4.2).
- [R5] **HTTPS only**: Client MUST use HTTPS only; if certificate is invalid, response is 4xx/5xx, or connection fails, the query has failed and MUST NOT retry over HTTP (Section 4.2).
- [R6] **Absent/malformed resource**: If `resource` parameter is absent or malformed, server MUST indicate bad request (RFC 2616 Section 10.4.1) (Section 4.2).
- [R7] **No information**: If server has no information for `resource`, server MUST indicate "unable to match" (RFC 2616 Section 10.4.5) (Section 4.2).
- [R8] **Default representation**: Server MUST return JRD if client requests no other supported format via Accept header (Section 4.2).
- [R9] **Ignore unsupported representations**: Server MUST silently ignore any requested representations it does not understand (Section 4.2).
- [R10] **Redirection**: Server MAY redirect; if it does, redirection MUST only be to an `https` URI and client MUST perform certificate validation again (Section 4.2).
- [R11] **Cache validators**: Server MAY include cache validators (Section 4.2).

### 4.3 The "rel" Parameter
- [R12] **Multiple rel**: The `rel` parameter MAY be included multiple times to request multiple link relation types (Section 4.3).
- [R13] **Server support**: WebFinger resources SHOULD support the `rel` parameter. If not supported, server MUST ignore the parameter and process request as if no `rel` values present (Section 4.3).

### 4.4 JSON Resource Descriptor (JRD)
- [R14] **Ignore unknown members**: When processing a JRD, client MUST ignore any unknown member and not treat as error (Section 4.4).
- [R15] **subject**: The `subject` member SHOULD be present in the JRD (Section 4.4.1).
- [R16] **aliases**: The `aliases` array is OPTIONAL (Section 4.4.2).
- [R17] **properties**: The `properties` object is OPTIONAL (Section 4.4.3).
- [R18] **links**: The `links` array is OPTIONAL (Section 4.4.4).

#### 4.4.4 Link Relation Objects
- [R19] **rel**: The `rel` member MUST be present in each link relation object. Value MUST contain exactly one URI or registered relation type (Section 4.4.4.1).
- [R20] **Comparison**: URI link relation type values are compared using "Simple String Comparison" of RFC 3986 Section 6.2.1 (Section 4.4.4.1).
- [R21] **type**: The `type` member is OPTIONAL (Section 4.4.4.2).
- [R22] **href**: The `href` member is OPTIONAL (Section 4.4.4.3).
- [R23] **titles**: More than one title MAY be provided; if used, a language identifier SHOULD be used as the name. A JRD SHOULD NOT include more than one title with same language tag (or "und") within a link relation object. Duplicate language tags MUST NOT be treated as error (Section 4.4.4.4).
- [R24] **properties**: The `properties` member in a link relation object is OPTIONAL (Section 4.4.4.5).

### 4.5 WebFinger and URIs
- [R25] **Scheme neutrality**: WebFinger is neutral regarding the scheme of the `resource` URI (Section 4.5).

## 5. Cross-Origin Resource Sharing (CORS)
- [R26] **CORS header**: Servers MUST include `Access-Control-Allow-Origin` HTTP header in responses (Section 5).
- [R27] **Least restrictive**: Servers SHOULD support the least restrictive setting by allowing any domain access: `Access-Control-Allow-Origin: *` (Section 5).
- [R28] **Restricting access**: Servers that wish to restrict access from external entities SHOULD use a more restrictive `Access-Control-Allow-Origin` header (Section 5).

## 6. Access Control
- (Informative) Authentication and differential responses are outside scope but may be used (Section 6).

## 7. Hosted WebFinger Services
- [R29] **Redirection for hosted services**: When a query is issued, the web server MUST return a response with a redirection status code including a `Location` header pointing to the hosted WebFinger service URI (Section 7).

## 8. Definition of WebFinger Applications
- [R30] **URI scheme specification**: Any application using WebFinger MUST specify the URI scheme(s) and appropriate URI forms (Section 8.1).
- [R31] **Host resolution**: For URI schemes without host portions, application specification MUST clearly define host resolution procedures (Section 8.2).
- [R32] **Properties specification**: Applications using subject-specific properties MUST define the URIs used and valid property values (Section 8.3).
- [R33] **Links specification**: Application specification MUST define each link and any associated values, including link relation type (`rel`), expected media type (`type`), properties, and titles. If a link does not require an external reference, all semantics MUST be defined in the application specification (Section 8.4).
- [R34] **Ignoring unknown properties/links**: Any syntactically valid properties or links that are not fully understood SHOULD be ignored and SHOULD NOT cause an error (Section 8.5).
- [R35] **Registration of simple tokens**: If a simple token is used as link relation type, it MUST be registered with IANA per Section 10.3. Properties MUST be registered per Section 10.4 (Section 8.6).

## 9. Security Considerations
- [R36] **HTTPS required**: Use of HTTPS is REQUIRED to ensure information is not modified during transit. Clients MUST NOT issue queries over a non-secure connection. Clients MUST verify that the certificate is valid and accept response only if valid (Section 9.1).
- [R37] **User privacy**: Systems exposing personal data via WebFinger MUST provide an interface for users to select which data elements are exposed. WebFinger MUST NOT be used to provide personal data unless publishing via WebFinger was explicitly authorized by the person (Section 9.2).
- [R38] **Abuse mitigation**: It is RECOMMENDED that implementers take steps to mitigate abuse (e.g., rate-limiting by IP address) (Section 9.3).
- [R39] **Client caution**: Clients are strongly advised not to perform WebFinger queries unless authorized by the user (Section 9.3).

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Query component must contain `resource` param; MAY contain `rel` params. | MUST | Section 4.1 |
| R2 | Parameter values must be percent-encoded including `=` and `&`. | MUST | Section 4.1 |
| R3 | No spaces in query string. | MUST | Section 4.1 |
| R4 | Query uses GET to `/.well-known/webfinger`. | MUST | Section 4.2 |
| R5 | Use HTTPS only; no fallback to HTTP. | MUST | Section 4.2 |
| R6 | Absent/malformed resource -> indicate bad request (400). | MUST | Section 4.2 |
| R7 | No information -> indicate unable to match (404). | MUST | Section 4.2 |
| R8 | Return JRD by default if no Accept header. | MUST | Section 4.2 |
| R9 | Silently ignore unsupported representations. | MUST | Section 4.2 |
| R10 | Redirects must be to HTTPS; client re-validates certificate. | MUST | Section 4.2 |
| R11 | Cache validators allowed. | MAY | Section 4.2 |
| R12 | Multiple `rel` parameters allowed. | MAY | Section 4.3 |
| R13 | Support `rel` parameter (SHOULD); if not supported, ignore. | SHOULD / MUST | Section 4.3 |
| R14 | Ignore unknown JRD members. | MUST | Section 4.4 |
| R15 | `subject` should be present. | SHOULD | Section 4.4.1 |
| R16 | `aliases` is optional. | OPTIONAL | Section 4.4.2 |
| R17 | `properties` is optional. | OPTIONAL | Section 4.4.3 |
| R18 | `links` is optional. | OPTIONAL | Section 4.4.4 |
| R19 | `rel` must be present with exactly one URI or registered relation type. | MUST | Section 4.4.4.1 |
| R20 | Compare URI link relation types using Simple String Comparison. | MUST | Section 4.4.4.1 |
| R21 | `type` is optional. | OPTIONAL | Section 4.4.4.2 |
| R22 | `href` is optional. | OPTIONAL | Section 4.4.4.3 |
| R23 | Titles: language tags used; duplicate tags not an error but should be avoided. | SHOULD / MUST NOT | Section 4.4.4.4 |
| R24 | `properties` in link is optional. | OPTIONAL | Section 4.4.4.5 |
| R25 | URI scheme neutrality. | – | Section 4.5 |
| R26 | Include CORS header. | MUST | Section 5 |
| R27 | Use `Access-Control-Allow-Origin: *` unless restricted. | SHOULD | Section 5 |
| R28 | More restrictive CORS for sensitive info. | SHOULD | Section 5 |
| R29 | Redirection for hosted WebFinger. | MUST | Section 7 |
| R30 | Application spec must define URI scheme(s). | MUST | Section 8.1 |
| R31 | Define host resolution if URI lacks host. | MUST | Section 8.2 |
| R32 | Define subject-specific properties. | MUST | Section 8.3 |
| R33 | Define links and associated values; if no external reference, semantics in spec. | MUST | Section 8.4 |
| R34 | Unknown properties/links: ignore, no error. | SHOULD | Section 8.5 |
| R35 | Register simple tokens and properties with IANA. | MUST | Section 8.6 |
| R36 | HTTPS required, certificate validation, no HTTP fallback. | MUST | Section 9.1 |
| R37 | User interface for data exposure; explicit authorization. | MUST / MUST NOT | Section 9.2 |
| R38 | Implement abuse mitigation (RECOMMENDED). | RECOMMENDED | Section 9.3 |
| R39 | Client queries only with user authorization (strongly advised). | SHOULD NOT | Section 9.3 |

## Informative Annexes (Condensed)
- **Section 2 (Terminology)**: Defines normative keywords per RFC 2119 and explains link relations as used in WebFinger.
- **Section 3 (Examples)**: Two examples illustrating WebFinger for OpenID Connect identity provider discovery and for retrieving web page metadata (author/copyright). These are non-normative but illustrate protocol usage.
- **Section 8.6 (Registration)**: Applications may register link relation types as simple tokens (IANA registry) and must register properties in the "WebFinger Properties" registry using the defined template and procedures (Designated Expert review).
- **Section 10 (IANA)**: Registers the well-known URI "webfinger", the media type "application/jrd+json", and establishes the "WebFinger Properties" registry. Includes registration template and procedures (Specification Required, per RFC 5226). Security considerations for JRD media type: care must be taken to avoid code injection.
- **Section 11 (Acknowledgments)**: Lists contributors and chairs.
- **Section 12 (References)**: Normative and informative references as listed above.

**Note**: The document is self-contained; all normative requirements are captured in the Requirements Summary and detailed sections above. The original RFC also includes full example exchanges (Section 3, Section 4.3) which are informative and have been condensed.