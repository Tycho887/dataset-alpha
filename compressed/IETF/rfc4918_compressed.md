# RFC 4918: HTTP Extensions for Web Distributed Authoring and Versioning (WebDAV)
**Source**: IETF | **Version**: Standards Track | **Date**: June 2007 | **Type**: Normative  
**Obsoletes**: RFC 2518

## Scope (Summary)
WebDAV extends HTTP/1.1 for remote collaborative authoring: management of resource properties (create, remove, query), creation/management of resource collections, URL namespace manipulation (copy, move), and resource locking (collision avoidance). This specification obsoletes RFC 2518 with minor revisions.

## Normative References
- [REC-XML] Bray et al., "Extensible Markup Language (XML) 1.0 (Fourth Edition)", 2006
- [REC-XML-INFOSET] Cowan & Tobin, "XML Information Set (Second Edition)", 2004
- [REC-XML-NAMES] Bray et al., "Namespaces in XML 1.0 (Second Edition)", 2006
- [RFC2119] Bradner, "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, 1997
- [RFC2616] Fielding et al., "Hypertext Transfer Protocol -- HTTP/1.1", 1999
- [RFC2617] Franks et al., "HTTP Authentication: Basic and Digest Access Authentication", 1999
- [RFC3339] Klyne & Newman, "Date and Time on the Internet: Timestamps", 2002
- [RFC3629] Yergeau, "UTF-8, a transformation format of ISO 10646", 2003
- [RFC3986] Berners-Lee et al., "Uniform Resource Identifier (URI): Generic Syntax", 2005
- [RFC4122] Leach et al., "A Universally Unique IDentifier (UUID) URN Namespace", 2005

## Definitions and Abbreviations
- **URI/URL**: Uniform Resource Identifier/Locator, defined in [RFC3986]
- **URI/URL Mapping**: Relation between an absolute URI and a resource
- **Path Segment**: Characters between "/" in a URI (see [RFC3986] Section 3.3)
- **Collection**: Resource that acts as container of references to child resources; meets requirements of Section 5
- **Internal Member (of a Collection)**: Resource referenced by a path segment mapping contained in the collection
- **Internal Member URL**: URL of internal member = collection URL + path segment
- **Member (of a Collection)**: Internal member or recursive member of internal member
- **Property**: Name/value pair with descriptive information about a resource
- **Live Property**: Property whose semantics and syntax are enforced by the server
- **Dead Property**: Property whose semantics and syntax are not enforced by the server
- **Principal**: Distinct human or computational actor that initiates access
- **State Token**: URI representing a state of a resource (e.g., lock token)
- **Key Words**: MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, MAY, OPTIONAL (as per [RFC2119])

## 4. Data Model for Resource Properties

### 4.1 Resource Property Model
- Properties are name/value pairs describing resource state.
- Two categories: live (server-enforced) and dead (client-enforced).
- All instances of a given live property **MUST** comply with the definition associated with that property name.

### 4.2 Properties and HTTP Headers
- Setting/returning many properties via HTTP headers is inefficient; a mechanism for selective property retrieval/setting is needed.

### 4.3 Property Values
- Property value is always a well-formed XML fragment.
- Servers **MUST** preserve the following XML Information Items for dead properties: namespace name, local name, attributes (xml:lang or any in scope), children (element or character). For all Element Information Items: namespace, local name, attributes, children. For Attribute Information Items: namespace, local name, normalized value. For Character Information Items: character code.
- Servers **SHOULD** preserve [prefix] for any Information Item.
- Servers **MUST** ignore xml:space attribute; whitespace in property values is significant.
- Clients **MUST** ignore elements they do not understand.

### 4.4 Property Names
- Property name is a universally unique identifier associated with a schema.
- XML namespace mechanism (URIs) used for naming.
- Property namespace is flat.
- Cannot define same property twice on a single resource.

### 4.5 Source Resources and Output Resources
- Relationship of source files to output HTTP resources is not defined in this specification; deferred.

## 5. Collections of Web Resources
- Collection: type of Web resource modeling containers (e.g., directories).
- All DAV-compliant resources **MUST** support the HTTP URL namespace model specified herein.

### 5.1 HTTP URL Namespace Model
- HTTP URL namespace is hierarchical, delimited by "/".
- Consistent namespace: for every URL, there exists a collection that contains that URL as an internal member URL, except root.
- Neither HTTP/1.1 nor WebDAV requires entire namespace consistency.
- Resources may be identified by more than one URI.

### 5.2 Collection Resources
- Collection state: set of mappings between path segments and resources, plus properties.
- Collection **MUST** contain at most one mapping for a given path segment.
- For WebDAV-compliant resources A and B with URLs "U" and "V" where V = U/SEGMENT, A **MUST** be a collection containing a mapping from "SEGMENT" to B.
- If a WebDAV-compliant resource has no WebDAV-compliant internal members, it is not required to be a collection.
- Server **MAY** handle a request to a collection without trailing slash as if slash were present; **SHOULD** return Content-Location header. Server **SHOULD** include trailing slash when producing collection URLs.
- Clients **SHOULD** use trailing slash form; **MUST** be prepared for redirect.
- Clients **MUST** support the case where WebDAV resources are contained inside non-WebDAV resources.
- If server treats a set of segments as equivalent, it **MUST** expose only one preferred segment per mapping, consistently, in PROPFIND responses.

## 6. Locking
- Locks provide serialized access to prevent lost updates.

### 6.1 Lock Model
1. A lock either directly or indirectly locks a resource.
2. A resource becomes directly locked when a LOCK request to its URL creates a new lock. If URL unmapped, a new empty resource is created and directly locked.
3. An exclusive lock conflicts with any other lock on the same resource. Server **MUST NOT** create conflicting locks.
4. For a depth-infinity lock on a collection, all member resources are indirectly locked. Membership changes affect indirectly locked set: if member added, new member **MUST NOT** already have a conflicting lock; if member removed, no longer indirectly locked.
5. Each lock has a single globally unique lock token.
6. UNLOCK deletes the lock; after deletion, no resource is locked by that lock.
7. A lock token is "submitted" when appearing in an If header.
8. If a request causes lock-root to become unmapped URL, the lock **MUST** be deleted.

### 6.2 Exclusive vs. Shared Locks
- Exclusive: prevents others from exercising access right.
- Shared: indicates intent to exercise rights; multiple principals can hold shared locks.
- Successful request for a new shared lock **MUST** result in generation of a unique lock per principal.

### 6.3 Required Support
- WebDAV-compliant resource is not required to support locking. If it does, it may support any combination of exclusive/shared locks.

### 6.4 Lock Creator and Privileges
- Server **MUST** check that authenticated principal matches lock creator when modifying locked resource (in addition to valid lock token submission).
- Server **MAY** allow privileged users (e.g., resource owner, administrator) to destroy a lock.
- Having lock does not confer full privilege to modify; normal authentication/privileges apply.

### 6.5 Lock Tokens
- Lock token is a type of state token identifying a particular lock.
- Each lock has exactly one unique lock token generated by server.
- Clients **MUST NOT** attempt to interpret lock tokens.
- Lock token URIs **MUST** be unique across all resources for all time.
- Servers **MAY** make lock tokens publicly readable (e.g., in DAV:lockdiscovery).
- Clients **SHOULD NOT** use a lock token created by another client instance.
- Servers encouraged to use UUIDs [RFC4122] or "opaquelocktoken" scheme.

### 6.6 Lock Timeout
- Lock **MAY** have limited lifetime; server chooses timeout.
- Timeout counter **MUST** be restarted on successful refresh; **SHOULD NOT** be restarted otherwise.
- If timeout expires, lock **SHOULD** be removed (server acts as if UNLOCK by server with override authority).
- Clients **MUST NOT** assume lock is immediately removed or that it still exists just because timeout hasn't expired.

### 6.7 Lock Capability Discovery
- Any DAV-compliant resource supporting LOCK method **MUST** support DAV:supportedlock property.

### 6.8 Active Lock Discovery
- Any DAV-compliant resource supporting LOCK method **MUST** support DAV:lockdiscovery property.

## 7. Write Lock
- Write lock type is the only lock type defined in this specification.
- Exclusive write lock prevents changes by any principal other than lock creator unless lock token submitted.
- Clients **MUST** submit a lock token they are authorized to use in any request that modifies a write-locked resource. Modifications include:
  1. Change to any variant, dead property, or lockable live property.
  2. For collections, modification of internal member URI (add, remove, different resource).
  3. Modification of mapping of lock root (move/delete).
- Affected methods: PUT, POST, PROPPATCH, LOCK, UNLOCK, MOVE, COPY (destination), DELETE, MKCOL.

### 7.1 Write Locks and Properties
- Only dead properties and lockable live properties are guaranteed not to change while write locked.

### 7.2 Avoiding Lost Updates
- WebDAV cannot guarantee prevention; HTTP clients without locking can overwrite.
- Servers can require locking; HTTP 1.1 clients can use If-Match with ETags.

### 7.3 Write Locks and Unmapped URLs
- Locking an unmapped URL creates a locked non-collection resource with empty content (locked empty resource).
- Successful LOCK to unmapped URL **MUST** result in creation of locked resource with empty content.
- Resource created with LOCK is empty but behaves normally: can be read, deleted, moved, copied; appears as member of parent collection; **SHOULD NOT** disappear when lock goes away; **MAY NOT** have values for properties like DAV:getcontentlanguage; **MUST NOT** be converted to collection; **MUST** have defined DAV:lockdiscovery and DAV:supportedlock.
- Response **MUST** be 201 Created; body includes DAV:lockdiscovery.
- Alternatively, servers **MAY** implement Lock-Null Resources (LNRs) for backward compatibility.

### 7.4 Write Locks and Collections
- Depth-0 write lock protects collection properties and internal member URLs; not member content.
- Depth-infinity write lock protects collection and all member resources.
- Collection write lock protects: DELETE direct internal member, MOVE into/out of collection, MOVE rename, COPY into collection, PUT/MKCOL creating new internal member.
- Collection's lock token required in addition to internal member's lock token.
- Depth-infinity lock: new resources added as descendants become indirectly locked; resources moved out become unlocked; resources moved into locked collection become indirectly locked.
- If depth-infinity LOCK to collection containing conflicting locks, request **MUST** fail with 423; response **SHOULD** contain 'no-conflicting-lock' precondition.
- If a resource is added as internal member of depth-infinity locked collection, new resource **MUST** be automatically protected by the lock.

### 7.5 Write Locks and the If Request Header
- Lock token **MUST** be submitted in If header for all locked resources that the method may change, or method **MUST** fail.

### 7.5.1 Example - Write Lock and COPY
- Only lock token for destination needed (source not modified).

### 7.5.2 Example - Deleting a Member of a Locked Collection
- Client must submit lock token in If header.

### 7.6 Write Locks and COPY/MOVE
- COPY **MUST NOT** duplicate write locks on source; but if copy into depth-infinity locked collection, resource added to lock.
- Successful MOVE on locked resource **MUST NOT** move write lock; if destination has lock, resource added to that lock.

### 7.7 Refreshing Write Locks
- LOCK request with If header and no body refreshes existing lock; **MUST NOT** create new lock.
- Server receiving LOCK with no body **MUST** reset timers.
- If error on refresh, client **MUST NOT** assume lock was refreshed.

## 8. General Request and Response Handling

### 8.1 Precedence in Error Handling
- Servers **MUST** return authorization errors in preference to other errors.

### 8.2 Use of XML
- Content-Type **SHOULD** be application/xml; implementations **MUST** accept both text/xml and application/xml; use of text/xml deprecated.
- All DAV-compliant clients and resources **MUST** use XML parsers compliant with [REC-XML] and [REC-XML-NAMES].
- If server receives XML not well-formed, **MUST** reject with 400 (Bad Request).
- If client receives non-well-formed XML in response, **MUST NOT** assume anything; **SHOULD** treat server as malfunctioning.

### 8.3 URL Handling
- Sender has choice: relative reference resolved against Request-URI, or full URI.
- Server **MUST** ensure every 'href' value within Multi-Status response uses same format.
- WebDAV only uses absolute path relative references.
- Senders **MUST NOT**: use dot-segments; have prefixes not matching Request-URI.
- Identifiers for collections **SHOULD** end in "/".

### 8.4 Required Bodies in Requests
- Servers **MUST** examine all requests for body even when not expected; if body present but would be ignored, server **MUST** reject with 415 (Unsupported Media Type).

### 8.5 HTTP Headers for Use in WebDAV
- Server **MUST** do authorization checks before checking any HTTP conditional header.

### 8.6 ETag
- Strong ETags preferred for authoring.
- WebDAV server **SHOULD NOT** change ETag (or Last-Modified) for resource with unchanged body and location.

### 8.7 Including Error Response Bodies
- Error body mechanism (from [RFC3253]) appropriate for error responses that may take a body but don't already have one defined.

### 8.8 Impact of Namespace Operations on Cache Validators
- For any URL, Last-Modified **MUST** increment every time representation changes.
- ETag **MUST NOT** be reused for different representations.

## 9. HTTP Methods for Distributed Authoring

### 9.1 PROPFIND Method
- Retrieves properties on resource identified by Request-URI and potentially members.
- All DAV-compliant resources **MUST** support PROPFIND and propfind XML element.
- Client **MUST** submit Depth header with "0", "1", or "infinity". Servers **MUST** support 0 and 1; **SHOULD** support infinity (may be disabled).
- Servers **SHOULD** treat request without Depth header as "infinity".
- Empty PROPFIND body **MUST** be treated as 'allprop' request.
- 'allprop' returns dead properties and live properties defined in this specification.
- Servers **MUST** support returning response of content type text/xml or application/xml with multistatus XML element.
- If error retrieving property, proper error result **MUST** be included.
- Request to retrieve property that does not exist is error; **MUST** be noted with response element containing 404.
- 'multistatus' for collection **MUST** include response element for each member URL to requested depth; **SHOULD NOT** include responses for non-WebDAV-compliant resources.
- Properties may be subject to access control; for 'allprop' and 'propname', if principal does not have right to know existence, property **MAY** be silently excluded.

#### 9.1.1 PROPFIND Status Codes
- 403 Forbidden: server **MAY** reject Depth: Infinity; **SHOULD** use precondition 'propfind-finite-depth'.

#### 9.1.2 Status Codes for Use in 'propstat' Element
- 200 OK: property exists/value returned.
- 401 Unauthorized: cannot view without authorization.
- 403 Forbidden: cannot view regardless.
- 404 Not Found: property does not exist.

### 9.2 PROPPATCH Method
- Processes instructions to set and/or remove properties.
- All DAV-compliant resources **MUST** support PROPPATCH and instructions using propertyupdate, set, remove XML elements.
- **SHOULD** support setting arbitrary dead properties.
- Request body **MUST** contain propertyupdate XML element.
- Servers **MUST** process instructions in document order.
- Instructions **MUST** either all be executed or none executed; if error, undo all and return proper error.
- If any property changes attempted, response **MUST** be Multi-Status.

#### 9.2.1 Status Codes for Use in 'propstat' Element
- 200 OK: property set/changed succeeded.
- 403 Forbidden: client cannot alter property; if attempting to set protected property, **SHOULD** use precondition 'cannot-modify-protected-property'.
- 409 Conflict: value semantics not appropriate.
- 424 Failed Dependency: property change failed due to another.
- 507 Insufficient Storage.

### 9.3 MKCOL Method
- Creates a new collection resource at Request-URI.
- If Request-URI already mapped, MKCOL **MUST** fail.
- Server **MUST** make Request-URI internal member of parent collection, unless "/".
- If no ancestor exists, method **MUST** fail with 409.
- When invoked without body, new collection **SHOULD** have no members.
- If server receives request entity type it does not support, **MUST** respond with 415.

#### 9.3.1 MKCOL Status Codes
- 201 Created.
- 403 Forbidden: server does not allow creation or parent cannot accept members.
- 405 Method Not Allowed: can only be executed on unmapped URL.
- 409 Conflict: intermediate collections missing; server **MUST NOT** create automatically.
- 415 Unsupported Media Type.
- 507 Insufficient Storage.

### 9.4 GET, HEAD for Collections
- Semantics unchanged.

### 9.5 POST for Collections
- Semantics unchanged.

### 9.6 DELETE Requirements
- Successful DELETE: **MUST** destroy locks rooted on deleted resource; **MUST** remove mapping from Request-URI.
- After successful DELETE, subsequent GET/HEAD/PROPFIND to target **MUST** return 404.

#### 9.6.1 DELETE for Collections
- **MUST** act as if "Depth: infinity" header used. Client **MUST NOT** submit Depth header with any value but infinity.
- If any member resource cannot be deleted, all ancestors **MUST NOT** be deleted.
- Any headers with DELETE **MUST** be applied to every resource to be deleted.
- After completion, **MUST** result in consistent URL namespace.
- If error deleting member, response can be 207 Multi-Status; server **MAY** return 4xx if complete failure.
- 424 Failed Dependency **SHOULD NOT** be in 207; 204 **SHOULD NOT** be in 207.

### 9.7 PUT Requirements
#### 9.7.1 PUT for Non-Collection Resources
- PUT replaces GET response entity; properties may be recomputed but not otherwise affected.
- PUT that would create resource without appropriately scoped parent collection **MUST** fail with 409.
- Client **SHOULD** provide Content-Type for new resource.

#### 9.7.2 PUT for Collections
- PUT to existing collection **MAY** be treated as error (405).

### 9.8 COPY Method
- Creates duplicate of source resource at destination identified by Destination header; Destination header **MUST** be present.
- All WebDAV-compliant resources **MUST** support COPY.
- Responses **MUST NOT** be cached.

#### 9.8.1 COPY for Non-collection Resources
- Creates new resource at destination with state and behavior as close as possible to source.

#### 9.8.2 COPY for Properties
- All dead properties on source **SHOULD** be duplicated; live properties **SHOULD** be duplicated as identically behaving live properties; servers **SHOULD NOT** convert live to dead.
- For unmapped URL, operation creates new resource; live properties related to creation should be set accordingly.

#### 9.8.3 COPY for Collections
- Without Depth header, **MUST** act as if "infinity". Client may submit 0 or infinity; servers **MUST** support both.
- Infinite-depth COPY: collection and internal members copied recursively.
- Depth 0: only collection properties, not internal members.
- Headers (except Destination) applied to every resource.
- After completion, **MUST** have consistent destination namespace.
- If error copying internal collection, server **MUST NOT** copy its members; should try to finish rest.
- If error with non-collection, **SHOULD** try to finish rest.
- If error, response **MUST** be 207 Multi-Status.

#### 9.8.4 COPY and Overwriting Destination Resources
- If Overwrite: F and destination exists, server **MUST** fail.
- When overwriting destination, membership of destination after successful COPY **MUST** be same as source immediately before.

#### 9.8.5 Status Codes
- 201 Created, 204 No Content, 207 Multi-Status, 403 Forbidden, 409 Conflict, 412 Precondition Failed, 423 Locked (should contain 'lock-token-submitted'), 502 Bad Gateway, 507 Insufficient Storage.

### 9.9 MOVE Method
- Logical equivalent of COPY + consistency processing + DELETE, atomic.
- Destination header **MUST** be present; **MUST** follow COPY requirements.
- All WebDAV-compliant resources **MUST** support MOVE.
- Responses **MUST NOT** be cached.

#### 9.9.1 MOVE for Properties
- Live properties **SHOULD** be moved; dead properties **MUST** be moved.
- DAV:creationdate **SHOULD** remain same.

#### 9.9.2 MOVE for Collections
- **MUST** act as "Depth: infinity". Client **MUST NOT** submit Depth with any value but infinity.
- Headers (except Destination) applied to every resource.
- After completion, **MUST** have consistent source and destination namespaces.
- Error handling similar to COPY.

#### 9.9.3 MOVE and the Overwrite Header
- If Overwrite: T, server **MUST** perform DELETE with depth infinity on destination before move. If F, fail.

#### 9.9.4 Status Codes
- 201 Created, 204 No Content, 207 Multi-Status, 403 Forbidden, 409 Conflict (e.g., 'preserved-live-properties'), 412 Precondition Failed, 423 Locked (should contain 'lock-token-submitted'), 502 Bad Gateway.

### 9.10 LOCK Method
- Used to take out lock or refresh existing lock.
- Any resource supporting LOCK **MUST** support XML request/response formats.
- Responses **MUST NOT** be cached.

#### 9.10.1 Creating a Lock on an Existing Resource
- LOCK to existing resource creates lock; resource becomes root.
- Request body with lockinfo **MUST** be present.
- Server **MUST** preserve 'owner' information.
- LOCK response: **MUST** contain body with DAV:lockdiscovery; **MUST** include Lock-Token response header.

#### 9.10.2 Refreshing Locks
- LOCK to URL within scope, no body, If header with single lock token.
- Server **MUST** ignore Depth header on refresh.

#### 9.10.3 Depth and Locking
- Depth header values: 0 or infinity only. All resources supporting LOCK **MUST** support Depth header.
- If no Depth header, request **MUST** act as if "Depth: infinity".
- If lock cannot be granted to all resources, server **MUST** return Multi-Status.

#### 9.10.4 Locking Unmapped URLs
- Successful LOCK to unmapped URL **MUST** create empty resource that is locked and is not a collection.
- Server **MUST** respond successfully to GET on empty resource (204 or 200 with zero Content-Length).

#### 9.10.5 Lock Compatibility Table
- None: shared OK, exclusive OK.
- Shared Lock: shared OK, exclusive false.
- Exclusive Lock: shared false, exclusive false (cannot request same lock twice).

#### 9.10.6 LOCK Responses
- 200 OK, 201 Created, 409 Conflict, 423 Locked (with 'no-conflicting-lock'), 412 Precondition Failed (with 'lock-token-matches-request-uri').

### 9.11 UNLOCK Method
- Removes lock identified by Lock-Token request header.
- Request-URI **MUST** identify a resource within lock scope.
- For successful response, server **MUST** delete the lock entirely.
- If all resources cannot be unlocked, UNLOCK **MUST** fail.
- Any DAV-compliant resource supporting LOCK **MUST** support UNLOCK.
- Responses **MUST NOT** be cached.

#### 9.11.1 Status Codes
- 204 No Content (success), 400 Bad Request (no token), 403 Forbidden (no permission), 409 Conflict (resource not locked or not in scope).

## 10. HTTP Headers for Distributed Authoring

### 10.1 DAV Header
- All DAV-compliant resources **MUST** return DAV header with compliance-class "1" on OPTIONS responses.
- Header syntax: `DAV: #(compliance-class)`; compliance-class = "1" | "2" | "3" | Coded-URL | token.
- Resource must show class 1 if it shows class 2 or 3.
- Clients **SHOULD NOT** send this header unless required.

### 10.2 Depth Header
- `Depth = "Depth" ":" ("0" | "1" | "infinity")`
- Methods may choose not to support all values.
- Clients **MUST NOT** rely on execution order or atomicity unless method guarantees.
- If source/destination resource locked, lock token **MUST** be submitted in If header.
- If resource has no internal members, Depth header **MUST** be ignored.

### 10.3 Destination Header
- `Destination = "Destination" ":" Simple-ref`
- If destination is absolute-URI on different server and source server cannot copy, **MUST** fail.
- If destination too long, server **SHOULD** return 400.

### 10.4 If Header
- Conditional header similar to If-Match but handles state tokens and ETags.
- Two purposes: make request conditional (if evaluated false, request **MUST** fail with 412) and submit state tokens.
- State token submission independent of evaluation.
- **Syntax**: `If = "If" ":" (1*No-tag-list | 1*Tagged-list)`
- **List Evaluation**: Conditions in a List are conjunction; Lists in a production are disjunction; overall header true if at least one production true.
- **Matching**: matching state token = exact match with any state token on identified resource; lock token matches if resource is in lock scope. For unmapped URLs, treat as if resource exists but doesn't have the state.
- Non-DAV proxies: client **MUST** use "Cache-Control: no-cache"; for HTTP/1.0 proxies, "Pragma: no-cache".

### 10.5 Lock-Token Header
- `Lock-Token = "Lock-Token" ":" Coded-URL`
- Used with UNLOCK to identify lock; token **MUST** identify a lock containing the resource.
- Used in response to LOCK to indicate new lock token.

### 10.6 Overwrite Header
- `Overwrite = "Overwrite" ":" ("T" | "F")`
- If not included, treat as "T".
- If F and destination exists, method **MUST** fail with 412.
- All DAV-compliant resources **MUST** support Overwrite header.

### 10.7 Timeout Request Header
- `TimeOut = "Timeout" ":" 1#TimeType`; TimeType = ("Second-" DAVTimeOutVal | "Infinite")
- Clients **MAY** include in LOCK requests; server not required to honor.
- Clients **MUST NOT** submit with method other than LOCK.
- Timeout value for "Second" **MUST NOT** be greater than 2^32-1.

## 11. Status Code Extensions to HTTP/1.1
- **207 Multi-Status**: Provides status for multiple independent operations.
- **422 Unprocessable Entity**: Server understands content type, syntax correct, but unable to process instructions.
- **423 Locked**: Source or destination resource is locked; response **SHOULD** contain precondition/postcondition code.
- **424 Failed Dependency**: Method could not be performed because requested action depended on another that failed.
- **507 Insufficient Storage**: Server unable to store representation; condition temporary; request **MUST NOT** be repeated until requested by separate user action.

## 12. Use of HTTP Status Codes
### 12.1 412 Precondition Failed
- If server evaluates conditional header and condition fails, this error **MUST** be returned. If client did not include conditional header, server **MUST NOT** use this status.

### 12.2 414 Request-URI Too Long
- Only for Request-URIs, not other URIs.

## 13. Multi-Status Response
- Conveys information about multiple resources; root element 'multistatus' containing zero or more 'response' elements.
- 207 used as overall response status; recipient must consult body for success/failure.
- Each 'response' **MUST** have an 'href' element identifying the resource.
- Two formats: 'status' child for overall status, or 'propstat' for property-specific (PROPFIND/PROPPATCH).

### 13.1 Response Headers
- Location header not defined for Multi-Status; intentionally undefined.

### 13.2 Handling Redirected Child Resources
- Servers **MUST** use 'location' element for redirected resources in Multi-Status.
- Clients encountering redirected resources **MUST NOT** rely on 'location' being present; may reissue request.

## 14. XML Element Definitions
All elements in "DAV:" namespace. Key elements:
- **activelock**: lockscope, locktype, depth, owner?, timeout?, locktoken?, lockroot
- **allprop**: EMPTY
- **collection**: EMPTY (identifies resource as collection)
- **depth**: PCDATA ("0"|"1"|"infinity")
- **error**: ANY (contains precondition/postcondition codes)
- **exclusive**: EMPTY
- **href**: PCDATA (Simple-ref)
- **include**: ANY (property names to include in PROPFIND)
- **location**: (href)
- **lockentry**: (lockscope, locktype)
- **lockinfo**: (lockscope, locktype, owner?)
- **lockroot**: (href)
- **lockscope**: (exclusive | shared)
- **locktoken**: (href)
- **locktype**: (write)
- **multistatus**: (response*, responsedescription?)
- **owner**: ANY (preserved as dead property; server **MUST NOT** alter unless empty)
- **prop**: ANY (property container)
- **propertyupdate**: (remove | set)+
- **propfind**: (propname | (allprop, include?) | prop)
- **propname**: EMPTY
- **propstat**: (prop, status, error?, responsedescription?)
- **remove**: (prop) – props empty, only names
- **response**: (href, ((href*, status)|(propstat+)), error?, responsedescription?, location?)
- **responsedescription**: #PCDATA
- **set**: (prop) – values to set
- **shared**: EMPTY
- **status**: #PCDATA (status-line)
- **timeout**: #PCDATA (TimeType)
- **write**: EMPTY

## 15. DAV Properties
| Property | Protected? | COPY/MOVE Behavior | Description |
|---|---|---|---|
| **DAV:creationdate** | MAY be protected | SHOULD be kept during MOVE; re-initialized on COPY | Timestamp of resource creation, SHOULD be defined on all DAV resources |
| **DAV:displayname** | SHOULD NOT be protected | SHOULD be preserved | Human-readable name; same value independent of Request-URI |
| **DAV:getcontentlanguage** | SHOULD NOT be protected | SHOULD be preserved | Content-Language from GET without accept headers |
| **DAV:getcontentlength** | Computed, protected | Dependent on destination size | Content-Length from GET |
| **DAV:getcontenttype** | Potentially protected | SHOULD be preserved | Content-Type from GET |
| **DAV:getetag** | MUST be protected | Dependent on final state; see Section 8.8 | ETag from GET |
| **DAV:getlastmodified** | SHOULD be protected | Dependent on destination; see Section 8.8 | Last-Modified from GET; only reflects body changes |
| **DAV:lockdiscovery** | MUST be protected | Depends on lock state of destination | Lists active locks; NOT lockable with write locks |
| **DAV:resourcetype** | SHOULD be protected | Same type at destination | Specifies nature (e.g., collection); MUST be defined on all DAV resources |
| **DAV:supportedlock** | MUST be protected | Depends on destination support | Lists lock capabilities; NOT lockable |

## 16. Precondition/Postcondition XML Elements
- Use defined condition codes in error bodies.
- Common codes in "DAV:" namespace:
  - **lock-token-matches-request-uri** (precondition, 409 Conflict): Request-URI not in lock scope.
  - **lock-token-submitted** (precondition, 423 Locked): Must contain at least one locked resource URL.
  - **no-conflicting-lock** (precondition, 423 Locked): Conflict on LOCK request; may contain href of lock root.
  - **no-external-entities** (precondition, 403 Forbidden): Server rejects external entity in request.
  - **preserved-live-properties** (postcondition, 409 Conflict): MOVE/COPY cannot maintain live properties.
  - **propfind-finite-depth** (precondition, 403 Forbidden): Server does not allow infinite PROPFIND.
  - **cannot-modify-protected-property** (precondition, 403 Forbidden): Attempt to set protected property.
- Server **SHOULD** use XML error when precondition/postcondition violated.

## 17. XML Extensibility in DAV
- Unrecognized elements and attributes **MUST** be processed as if not there (ignored).
- This does not apply to dead property values or PUT bodies (XML as content type).
- Processing instructions **SHOULD** be ignored.
- DTD validation **MUST NOT** be applied by recipients.

## 18. DAV Compliance Classes
- **Class 1**: Meet all MUST requirements in all sections; return "1" in DAV header.
- **Class 2**: Class 1 + support LOCK, DAV:supportedlock, DAV:lockdiscovery, Time-Out header, Lock-Token header; **SHOULD** support Timeout request header and 'owner' element; return "1" and "2".
- **Class 3**: Class 1 (optionally class 2) + support all revisions in this specification; return "1" and "3" (or "1,2,3").

## 19. Internationalization Considerations
- Human-readable fields encoded in XML with UTF-8 / UTF-16; xml:lang for language tagging.
- WebDAV applications **MUST** support character set tagging, encoding, and language tagging of XML.
- Property names are qualified XML names; applications expected to map to human-readable strings.

## 20. Security Considerations (Condensed)
- **Authentication**: Basic auth **MUST NOT** be used unless connection secure (TLS); Digest auth [RFC2617] **MUST** be supported.
- **Denial of Service**: Servers must be aware of attacks via large files, recursive operations, multiple connections.
- **Obscurity**: PROPFIND reduces obscurity; access control recommended.
- **Privacy**: Lock owner information (DAV:owner) may be sensitive; servers **SHOULD** limit read access to DAV:lockdiscovery. Property values may contain private info; servers encouraged to separate read access to body and properties.
- **XML Entities**: External entities untrustworthy; server **SHOULD** respond with 'no-external-entities' if rejected. Risk of internal entity recursion.
- **Lock Tokens**: Use of UUIDs with MAC address may expose hardware info; use non-host-address UUIDs.
- **Hosting Malicious Content**: Servers should restrict content types, run malware detection, and use access controls.

## 21. IANA Considerations (Condensed)
- URI schemes 'opaquelocktoken' and 'DAV' registered.
- XML namespaces not managed by IANA.
- Message header fields registered: DAV, Depth, Destination, If, Lock-Token, Overwrite, Timeout.
- HTTP status codes 207, 422, 423, 424, 507 added to registry.

## Appendices (Condensed)
- **A. Notes on Processing XML Elements**: Empty elements semantically equivalent; illegal combinations must produce 400; extension elements ignored unless additive.
- **B. Notes on HTTP Client Compatibility**: WebDAV backward-compatible with HTTP 1.1; new status codes handled as errors; 207 for collection DELETE should not cause issues.
- **C. The 'opaquelocktoken' Scheme and URIs**: Constructed from 'opaquelocktoken:' + UUID [+ extension]; for lock token uniqueness.
- **D. Lock-null Resources**: Deprecated; clients should handle both lock-null and locked empty resources; guidance for creating resources after LOCK.
- **E. Guidance for Clients Desiring to Authenticate**: Use PUT with If-Match or Authorization header to trigger challenge.
- **F. Summary of Changes from RFC 2518**: Major changes: 'allprop' semantics clarified, Depth:Infinity PROPFIND optional, locking model simplified (locked empty resources replace lock-null), property preservation strengthened, new compliance class 3.

## Requirements Summary (Key MUST/SHOULD)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All instances of a live property MUST comply with definition | MUST | 4.1 |
| R2 | Servers MUST preserve specific XML Infoset items for dead properties | MUST | 4.3 |
| R3 | All DAV-compliant resources MUST support PROPFIND and PROPPATCH | MUST | 9.1, 9.2 |
| R4 | PROPFIND client MUST submit Depth header | MUST | 9.1 |
| R5 | PROPPATCH instructions MUST be executed atomically (all or none) | MUST | 9.2 |
| R6 | MKCOL on existing resource MUST fail | MUST | 9.3 |
| R7 | DELETE on collection MUST act as Depth: infinity | MUST | 9.6.1 |
| R8 | All DAV-compliant resources MUST support COPY and MOVE | MUST | 9.8, 9.9 |
| R9 | LOCK request to unmapped URL MUST create locked empty resource | MUST | 7.3, 9.10.4 |
| R10 | UNLOCK MUST delete lock entirely if successful | MUST | 9.11 |
| R11 | Server MUST do authorization checks before conditional headers | MUST | 8.5 |
| R12 | If header: if evaluated false, request MUST fail with 412 | MUST | 10.4.3 |
| R13 | DAV header MUST be returned on OPTIONS | MUST | 10.1 |
| R14 | Overwrite header defaults to T if absent | MUST | 10.6 |
| R15 | Depth header MUST be supported on LOCK (0 or infinity) | MUST | 9.10.3 |
| R16 | ETag MUST NOT be reused for different representations | MUST | 8.8 |
| R17 | DAV:getetag property MUST be protected | MUST | 15.6 |
| R18 | DAV:lockdiscovery and DAV:supportedlock MUST be protected | MUST | 15.8, 15.10 |
| R19 | XML extensibility: unrecognized elements MUST be ignored | MUST | 17 |
| R20 | Server SHOULD use precondition/postcondition error bodies | SHOULD | 16 |