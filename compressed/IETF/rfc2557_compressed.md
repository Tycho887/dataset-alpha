# RFC 2557: MIME Encapsulation of Aggregate Documents, such as HTML (MHTML)
**Source**: IETF Standards Track | **Version**: March 1999 | **Date**: March 1999 | **Type**: Normative  
**Original**: https://datatracker.ietf.org/doc/rfc2557/

## Scope (Summary)
Defines the use of MIME multipart/related to aggregate a text/html root resource and its subsidiary resources (images, applets, etc.) into a single message, and specifies a Content-Location header to allow URIs in the root to reference those subsidiary resources within the same multipart/related structure. Also applicable to HTTP, FTP, and archiving.

## Normative References
- [ABNF] RFC 2234
- [HTML2] RFC 1866
- [HTTP] RFC 1945
- [IETF-TERMS] RFC 2119
- [MIDCID] RFC 2387
- [MIME1] RFC 2045
- [MIME2] RFC 2046
- [MIME3] RFC 2047
- [REL] RFC 2389 (Multipart/Related)
- [RELURL] RFC 1808
- [RFC822] STD 11
- [URL] RFC 1738
- [URLBODY] RFC 2017

## Definitions and Abbreviations
- **Content-Location**: MIME content header (section 4.2) that labels the content of a body part with an URI (absolute or relative).
- **CID**: Content-ID URL scheme as defined in [URL] and [MIDCID].
- **MHTML**: MIME Encapsulation of Aggregate Documents (this standard).
- **multipart/related**: MIME content type defined in [REL] used to aggregate related body parts.
- **root resource**: The primary body part (e.g., text/html) that references other resources.
- **MIC**: Message Integrity Code.
- **MUA**: Messaging User Agent.
- **URI**: Uniform Resource Identifier (absolute or relative) as per [URL].

## 1. Introduction
There is a need to send multi-resource documents (HTML, XML, PDF, VRML) in e-mail. This standard specifies aggregation in MIME messages. It may also be used with HTTP/FTP and archiving. Implementations claiming conformance are not required to handle URI-linked documents other than those with HTML root. An informational RFC supplements this standard (available at http://www.dsv.su.se/~jpalme/ietf/mhtml.html). Body parts may be identified by Content-ID or Content-Location to avoid rewriting URIs (preserving MIC checksums).

## 2. Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are as per [IETF-TERMS]. Unconditionally compliant implementations satisfy all MUST and SHOULD requirements; conditionally compliant satisfy all MUST but not all SHOULD.

## 3. Overview
An aggregate document is a MIME-encoded message containing a root resource and linked resources. It serves mail sending, web page forwarding, and automatic responders. Receiving agents must be able to display or pass to a browser. Signed documents must preserve MIC checksums.

## 4. The Content-Location MIME Content Header
### 4.1 Syntax (ABNF)
```abnf
content-location = "Content-Location:" [CFWS] URI [CFWS]
URI = absoluteURI | relativeURI
```
URI restricted to URL syntax until IETF specifies other URIs.

### 4.2 Semantics
- Content-Location labels the content of the body part. Value CAN be absolute or relative. Any URI scheme may be used; non-standard schemes risk recipient inability.
- URI need not be globally retrievable, but SHOULD be globally unique when absolute or resolvable to absolute.
- A single Content-Location header is allowed per message/ content heading, in addition to Content-ID and Message-ID.
- Multiple Content-Location headers in the same heading are NOT allowed.
- Example given (section 4.2, page 8) shows use with multipart/related.

### 4.3 URIs of MHTML Aggregates
The URI of the aggregate is not the same as the URI of its root. A Content-Location on the multipart/related SHOULD apply to the whole aggregate, not just the root. Retrieving an aggregate may return a different version than retrieving the root and its inline objects separately.

### 4.4 Encoding and Decoding of URIs in MIME Headers
#### 4.4.1 Encoding Inappropriate Characters
- URIs with illegal characters (e.g., spaces) MUST be encoded using [MIME3] section 4 methods before placing in header.
- Encoding MUST only be done in the header, not in HTML text.
- Receiving clients MUST decode [MIME3] encoding before comparing URIs.
- Charset parameter: US-ASCII SHOULD be used if no 8-bit octets; otherwise correct charset SHOULD be used; if unknown, "UNKNOWN-8BIT" MUST be used.
- Charset is irrelevant for URI matching but MUST be correctly labeled for other purposes.

#### 4.4.2 Folding Long URIs
Encoding (4.4.1) MUST be done before folding. Folding may be done using the algorithm in [URLBODY] section 3.1.

#### 4.4.3 Unfolding and Decoding
Upon receipt, folded headers should be unfolded, then any MIME encoding removed to retrieve original URI.

## 5. Base URIs for Resolution of Relative URIs
Relative URIs inside MIME body parts are resolved relative to a base URI using [RELURL]. The first applicable method from the following list applies:
(a) A base specification inside the body part (e.g., HTML `<BASE>` element).
(b) A Content-Location header in the immediately surrounding heading containing an absolute URI.
(c) Recursively repeat (b) to find a suitable Content-Location in a surrounding multipart or message heading.
(d) If the MIME object is returned in an HTTP response, use the request URI.
(e) If none of the above yields an absolute URI, a base URL of `thismessage:/` MUST be employed (solely for resolving relative references inside multipart/related when no other base is specified).

## 6. Sending Documents Without Linked Objects
A text/html resource sent alone MAY be sent without multipart/related. It may contain URIs that the recipient is expected to retrieve via protocol. Unresolvable links are allowed (e.g., drafts). Inclusion of URIs that require Internet connectivity may not work for all recipients.

## 7. Use of the Content-Type "multipart/related"
- If a message contains body parts with URIs and separate body parts for referenced resources, the whole set SHOULD be sent within a multipart/related structure [REL].
- This standard only covers URI resolution between body parts inside the same multipart/related structure. It covers nested multipart/related where a resource references a body part in an enclosing multipart/related. It does NOT cover references between parallel or other nested/separate multipart/related structures.
- The start body part (if atomic like text/html) SHOULD be the root resource. If the start is multipart/alternative, then a suitable atomic alternative SHOULD be the root.
- The type parameter in Content-Type header for multipart/related MUST specify the type of the start object (e.g., "multipart/alternative" if start is that type). If the start object is not the first body part, its Content-ID MUST be specified as the value of a start parameter.
- Rendering: URI references in a resource can be satisfied by body parts within the same multipart/related. This is useful for recipients without Internet access, behind firewalls, for preservation, for resources not available via protocol, and for speed.
- When sending objects retrieved from WWW, the sending MUA SHOULD maintain their WWW URIs and SHOULD NOT transform them (to preserve MICs). Rewriting may be necessary in some cases (e.g., URIs as parameters to applets).
- Within a multipart/related structure, each body part MUST have, if assigned, a different Content-ID and a Content-Location that resolves to a different URI. Two body parts can have the same relative Content-Location only if resolved absolute URIs differ.

## 8. Usage of Links to Other Body Parts
### 8.1 General Principle
Body parts (e.g., text/html) may contain URIs referencing resources in the same multipart/related. Often these are inline objects (IMG, applet, frame, etc.). A sender may also send a set of linked documents (e.g., A elements). The format allows archiving all resources needed to display a web page as it appeared.

### 8.2 Resolution of URIs in text/html Body Parts
Resolution steps:
(a) Unfold multiple line header values per [URLBODY]; do NOT translate percent-encoding.
(b) Remove all MIME encodings (content-transfer, header encodings per [MIME3]); do NOT translate percent-encoding.
(c) Resolve all relative URIs in HTML content and Content-Location headers using the procedure of section 5. Result can be an absolute URI or an absolute URI with base `thismessage:/`.
(d) For each referencing URI, compare (after steps a,b) with URIs derived from Content-ID and Content-Location headers of other body parts within the same or surrounding multipart/related. If strings are identical octet-by-octet, the referencing URI references that body part. This requires identical resolution (e.g., both `thismessage:/` if fictitious).
(e) If (d) fails, try ordinary Internet lookup. Resolution of "mid" or "cid" URIs to body parts outside the same multipart/related or in other messages is NOT covered.

### 8.3 Use of Content-ID Header and CID URLs
When CID URIs are used to reference other body parts, they MUST only be matched against Content-ID header values, NOT against Content-Location with CID values. Example: `Content-ID: <foo@bar.net>` will match, but `Content-Location: CID:foo@bar.net` will be ignored. Note: Content-IDs MUST be globally unique per [MIME1].

## 9. Examples (Informative – Condensed)
**9.1** Simple HTML email without linked objects – single text/html body part with a URI that must be retrieved externally.

**9.2** HTML message with one embedded GIF using absolute Content-Location – multipart/related with text/html and image body part; URI in IMG SRC points to absolute URL matching Content-Location.

**9.3** HTML with relative URIs and an outer Content-Location as base – multipart/related with Content-Location in outermost heading; body parts have absolute or relative Content-Location resolved by that base.

**9.4** Relative URI with no BASE available – relative URI in IMG SRC resolved via `thismessage:/` base (method e).

**9.5** CID URL and Content-ID – IMG SRC uses `cid:foo4@foo1@bar.net` matched against Content-ID header; Content-Location with CID value is disregarded.

**9.6** Forbidden references between nested multipart/related structures – demonstrates that references from an outer part to a nested part are not supported (parallel structures also not supported). Only enclosing or same structure references are allowed.

## 10. Character Encoding Issues and End-of-Line Issues
- HTML documents may use character entities or numeric references. MIME charset parameter indicates encoding.
- All mechanisms MAY be used; receiving agents MUST handle any combination.
- Documents with octets outside 7-bit range need content-transfer-encoding.
- MIME requires text/plain in canonical form (CRLF line breaks) before transfer encoding. HTTP allows other line breaks.
- This may break MIC checksums; such integrity headers SHOULD be removed if conversion invalidates them.
- Content-Encoding (HTTP) is not allowed in MIME.
- For e-mail, the charset parameter SHOULD be included (not rely on default).

## 11. Security Considerations
### 11.1 Not Related to Caching
- A sender may misrepresent the source of a body part by labeling it with a Content-Location URI that references a different resource. Recipients should only interpret Content-Location as labeling for resolution within the same multipart/related, not as source of the resource unless verified.
- URIs (especially file URIs) may inadvertently reveal information outside intended security context.
- Resource servers may embed passwords or tokens in URIs; forwarding may reveal sensitive information.
- Executable content (JavaScript, Java) in HTML is dangerous; receiving UA must restrict capabilities.
- HTML can be used to track users (e.g., inline link to external object reveals IP). This could break anonymity.

### 11.2 Related to Caching
- When rendering a body part in MHTML, all URIs referencing subsidiary resources within the same multipart/related SHALL be satisfied by those resources and NOT by any other local or remote source.
- If a sender wants recipient to always retrieve from source, an URI-labeled copy MUST NOT be included.
- A resource received in multipart/related MUST NOT be retrieved from cache other than by a reference in the same multipart/related structure (failure allows Trojan horse attacks).

## 12. Differences from RFC 2110 (Informative)
- Formats apply also to protocols other than email (HTTP, FTP).
- Content-Location in multipart headings can be a base for relative URIs in component parts (only if no base from the part itself).
- Content-Base header removed; implementors may accept it for compatibility but MUST never send it.
- Section 4.4.1 added for handling non‑URI‑compliant characters.
- Relative and absolute URI matching unified by using `thismessage:/` base when no other resolution possible.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Content-Location header syntax MUST follow given ABNF (section 4.1). | MUST | §4.1 |
| R2 | A single Content-Location header is allowed per heading; multiple NOT allowed. | MUST NOT | §4.2 |
| R3 | If Content-Location is used on multipart/related, it SHOULD apply to the whole aggregate. | SHOULD | §4.3 |
| R4 | URIs with illegal characters in headers MUST be encoded per [MIME3] before sending. | MUST | §4.4.1 |
| R5 | Receiving clients MUST decode [MIME3] encoding before comparing URIs. | MUST | §4.4.1 |
| R6 | If unknown charset for URI encoding, "UNKNOWN-8BIT" MUST be used. | MUST | §4.4.1 |
| R7 | Encoding of URIs MUST be done before folding; folding may follow [URLBODY]. | MUST | §4.4.2 |
| R8 | Relative URIs unresolved by other methods MUST use base `thismessage:/`. | MUST | §5(e) |
| R9 | Aggregate documents SHOULD use multipart/related structure. | SHOULD | §7 |
| R10 | Within multipart/related, if assigned, each body part MUST have unique Content-ID and Content-Location (when resolved to absolute). | MUST | §7 |
| R11 | When sending WWW resources, MUA SHOULD maintain original URIs; SHOULD NOT transform them. | SHOULD | §7 |
| R12 | CID URIs MUST only be matched against Content-ID headers, not Content-Location. | MUST | §8.3 |
| R13 | Content-IDs MUST be globally unique. | MUST | §8.3 (ref [MIME1]) |
| R14 | When rendering, URIs referencing resources in same multipart/related SHALL be satisfied by those resources and not by external sources. | SHALL | §11.2 |
| R15 | If sender wants recipient to always retrieve from source, an URI-labeled copy MUST NOT be included. | MUST NOT | §11.2 |
| R16 | A resource received in multipart/related MUST NOT be retrieved from cache except by reference from the same multipart/related structure. | MUST NOT | §11.2 |

## Informative Annexes (Condensed)
- **Section 9 (Examples)**: Six examples illustrate usage of Content-Location, Content-ID, base resolution, and nesting. They are provided for illustration only; normative text takes precedence.
- **Section 12 (Differences from RFC 2110)**: Summarizes changes: broader protocol applicability, base URI precedence updated, Content-Base removed, addition of encoding rules for non-URI characters, unified resolution via `thismessage:/`.
- **Section 13 (Acknowledgments)**: Lists contributors.
- **Section 14 (References)**: List of normative and informative references.
- **Section 15 (Authors' Addresses)**: Contact information.
- **Section 16 (Full Copyright Statement)**: IETF copyright notice.