# RFC 3275: XML-Signature Syntax and Processing
**Source**: IETF | **Version**: Standards Track, Obsoletes RFC 3075 | **Date**: March 2002 | **Type**: Normative  
**Original**: https://www.ietf.org/rfc/rfc3275.txt

## Scope (Summary)
This document specifies XML digital signature processing rules and syntax. XML Signatures provide integrity, message authentication, and/or signer authentication for data of any type. It defines the Signature element, processing for generation and validation, and algorithm identifiers.

## Normative References
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels (MUST, SHOULD, etc.)
- RFC 2396: Uniform Resource Identifiers (URI)
- RFC 2045: MIME (Base64)
- RFC 2104: HMAC
- FIPS PUB 180-1: Secure Hash Standard (SHA-1)
- FIPS PUB 186-2: Digital Signature Standard (DSS)
- RFC 2437: PKCS #1 (RSA)
- W3C XML-C14N: Canonical XML (REC-xml-c14n-20010315)
- W3C XPath: XML Path Language (REC-xpath-19991116)
- W3C XSLT: XSL Transformations (REC-xslt-19991116)
- W3C XML Schema: Structures and Datatypes (REC-xmlschema-1-20010502, REC-xmlschema-2-20010502)
- XML 1.0 (Second Edition)
- Namespaces in XML

## Definitions and Abbreviations
- **Authentication Code**: Value generated from shared key with message authentication and integrity properties (not signer authentication).
- **Core**: Syntax and processing defined by this specification.
- **Data Object**: Binary/octet data being operated on (transformed, digested, signed).
- **Integrity**: Property that data has not been changed in an unauthorized or accidental manner.
- **Object**: XML Signature element containing arbitrary data.
- **Resource**: Anything identified by a URI.
- **Signature**: Value generated from private key providing integrity, message authentication, and/or signer authentication. May be detached, enveloping, or enveloped.
- **Transform**: Processing from source data to derived form.
- **Validation, Core**: Signature validation and SignedInfo reference validation.
- **Validation, Reference**: Hash value matches DigestValue.
- **Validation, Signature**: SignatureValue matches processing of SignedInfo.

## 1. Introduction
- XML Signatures apply to any digital content; enveloped, enveloping, or detached signatures.
- Defines XML signature element type and application conformance.
- Key association with persons/institutions is out of scope.

### 1.1 Editorial and Conformance Conventions
- Key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", "OPTIONAL" are used per RFC 2119.
- Used to specify protocol and application requirements. Not used for XML grammar; schema defines grammar.
- Compliance with XML Namespaces is REQUIRED.

### 1.3 Versions, Namespaces and Identifiers
- No explicit version number; future versions use different namespace.
- **MUST** use namespace: `http://www.w3.org/2000/09/xmldsig#`
- Applications **MUST** support XML and XML namespaces.
- Use of internal entities and prefix "dsig" is OPTIONAL.
- URIs identify resources, algorithms, semantics.

## 2. Signature Overview and Examples
- XML Signatures applied via indirection: data objects digested, value placed in element, then SignedInfo digested and signed.
- Signature element structure: `Signature` contains `SignedInfo` (CanonicalizationMethod, SignatureMethod, Reference+), `SignatureValue`, (optional `KeyInfo`), (optional `Object`*).
- Signatures related to data via URIs. Detached, enveloping, enveloped signatures defined.

### 2.1 Simple Example
- Demonstrates detached signature of HTML4 specification.
- SignedInfo is the information actually signed.
- CanonicalizationMethod, SignatureMethod, Reference, DigestMethod, DigestValue, KeyInfo explained.

### 2.1.1 More on Reference
- URI attribute identifies data object; may be omitted on at most one Reference.
- Transforms optional ordered list of processing steps.
- DigestMethod applied after Transforms to yield DigestValue.

### 2.2 Extended Example (Object and SignatureProperty)
- `SignatureProperties` element for assertions about signature.
- Target attribute references Signature element.
- Reference Type attribute (e.g., SignatureProperties) is advisory; no core validation required.

### 2.3 Extended Example (Object and Manifest)
- Manifest element allows application-controlled reference validation.
- SignedInfo may reference Manifest; digest of Manifest is checked by core validation, but reference validation of Manifest is under application control.

## 3. Processing Rules
### 3.1 Core Generation
- REQUIRED steps: generate Reference elements and SignatureValue over SignedInfo.
- Reference Generation: apply Transforms, calculate digest, create Reference.
- Signature Generation: create SignedInfo, canonicalize, calculate SignatureValue, construct Signature.

### 3.2 Core Validation
- REQUIRED steps: (1) reference validation (digest check), (2) cryptographic signature validation.
- Comparison of values is over numeric or decoded octet sequence.

#### 3.2.1 Reference Validation
1. Canonicalize SignedInfo per CanonicalizationMethod.
2. For each Reference: obtain data object, digest with DigestMethod, compare to DigestValue. Mismatch => validation fails.
- Application must ensure CanonicalizationMethod has no dangerous side effects.

#### 3.2.2 Signature Validation
1. Obtain keying information from KeyInfo or external source.
2. Obtain canonical form of SignatureMethod using CanonicalizationMethod; confirm SignatureValue over SignedInfo.
- SignatureMethod URI must be canonical form.

## 4. Core Signature Syntax
Defined via DTD and XML Schema. Features described are mandatory to implement unless stated.

### 4.0.1 ds:CryptoBinary Simple Type
- Represents arbitrary-length integers as octet strings: "big endian" bitstring, padded to multiple of 8 bits, leading zero octets removed, base64 encoded.
- Used for RSAKeyValue, DSAKeyValue.

### 4.1 The Signature element
- Root element. Implementation **MUST** generate laxly schema valid Signature as per schema.

### 4.2 The SignatureValue Element
- Contains actual digital signature, base64 encoded.
- Two SignatureMethod algorithms identified: DSA-SHA1 (REQUIRED), RSA-SHA1 (RECOMMENDED). User specified algorithms allowed.

### 4.3 The SignedInfo Element
- Includes CanonicalizationMethod, SignatureMethod, one or more References.
- May have optional ID attribute.

#### 4.3.1 The CanonicalizationMethod Element
- REQUIRED element specifying canonicalization algorithm applied to SignedInfo before signature calculation.
- Implementations **MUST** support REQUIRED canonicalization algorithms (Canonical XML omitting comments).
- Alternative algorithms (e.g., Canonical XML with Comments) are NOT REQUIRED; use may not interoperate.
- XML based canonicalization: **MUST** be provided with XPath node-set from document containing SignedInfo.
- Text based canonicalization: **SHOULD** be provided with UTF-8 octets of well-formed SignedInfo element. Use NOT RECOMMENDED.
- Application must exercise great care: arbitrary CanonicalizationMethod could modify URIs or transform SignedInfo trivially.

#### 4.3.2 The SignatureMethod Element
- REQUIRED element specifying algorithm for signature generation/validation.
- Identifies cryptographic functions: hashing, public key, MACs, padding.

#### 4.3.3 The Reference Element
- May occur one or more times. Specifies digest algorithm, digest value, optional URI, Type, Transforms.

##### 4.3.3.1 The URI Attribute
- Identifies data object using URI-Reference per RFC 2396. Disallowed characters must be escaped (UTF-8, %HH).
- XML signature applications **MUST** be able to parse URI syntax. **RECOMMEND** dereference HTTP URIs. Dereferencing HTTP **MUST** comply with HTTP status codes.
- If URI omitted, identity expected from context; may be omitted on at most one Reference per SignedInfo or Manifest.
- Type attribute is advisory; no validation required.

##### 4.3.3.2 The Reference Processing Model
- XPath is RECOMMENDED for node-set processing but not required; conformance can be via functional equivalent.
- Data-type of result is octet stream or XPath node-set.
- Default behavior: If octet stream and next transform requires node-set, **MUST** attempt parse via XML well-formed. If node-set and next requires octets, **MUST** attempt conversion via Canonical XML.
- Unless same-document reference, result of URI dereference **MUST** be octet stream.
- Fragment identifiers: when not preceded by URI, **MUST** support null URI and barename XPointer. **RECOMMEND** support for same-document XPointers `#xpointer(/)` and `#xpointer(id('ID'))` if preserving comments. All other XPointer support OPTIONAL.

##### 4.3.3.3 Same-Document URI-References
- Dereferencing **MUST** result in XPath node-set suitable for Canonical XML.
- null URI: node-set includes every non-comment node of document containing URI attribute.
- Fragment URI conforms to XPointer syntax; processing follows specific steps (discard points, replace ranges, replace root with children, replace element with descendants and namespaces/attributes, delete comment nodes if not full XPointer).

##### 4.3.3.4 The Transforms Element
- Optional ordered list of Transform elements. Output of each is input to next. Input to first is result of URI dereference. Output of last is input to DigestMethod.
- Each Transform has Algorithm attribute and optional content parameters.
- Some transforms require XPath node-set, others octet stream; if mismatch, conversion occurs.
- Application-specific transforms allowed but may hinder interoperability.

##### 4.3.3.5 The DigestMethod Element
- REQUIRED element identifying digest algorithm. Applies to resulting octet stream after dereference and transforms.

##### 4.3.3.6 The DigestValue Element
- Contains base64 encoded digest value.

### 4.4 The KeyInfo Element
- Optional element for key information to validate signature.
- Compliant versions **MUST** implement KeyValue; **SHOULD** implement RetrievalMethod.
- Multiple declarations refer to same key.
- External namespace elements in KeyInfo children allowed only if safe to ignore.

#### 4.4.1 The KeyName Element
- String value for key identifier.

#### 4.4.2 The KeyValue Element
- Contains public key. DSA (REQUIRED) and RSA (RECOMMENDED).

##### 4.4.2.1 The DSAKeyValue Element
- Fields: P, Q, G, Y, J (optional), Seed, PgenCounter (optional but must both be present or absent). If all P, Q, Seed, PgenCounter present, implementations not required to check consistency.

##### 4.4.2.2 The RSAKeyValue Element
- Fields: Modulus, Exponent.

#### 4.4.3 The RetrievalMethod Element
- Reference to KeyInfo stored elsewhere. URI mandatory. Type optional identifier.

#### 4.4.4 The X509Data Element
- Contains one or more identifiers of keys/certificates. At least one of: X509IssuerSerial, X509SubjectName, X509SKI, X509Certificate, X509CRL, or external elements.
- Grouping rules: all referring to same certificate in same X509Data; different certificates in separate X509Data within same KeyInfo.

#### 4.4.5 The PGPData Element
- Contains PGPKeyID and/or PGPKeyPacket (base64). Must have at least one.

#### 4.4.6 The SPKIData Element
- Contains SPKISexp (base64 SPKI canonical S-expression). Must have at least one.

#### 4.4.7 The MgmtData Element
- String for in-band key distribution/agreement. Use NOT RECOMMENDED; XML Encryption Working Group provides alternatives.

### 4.5 The Object Element
- May occur one or more times. May contain any data, optional MimeType, Encoding, Id.
- Id commonly referenced from Reference. Digest calculated over entire Object element including tags.

## 5. Additional Signature Syntax
Optional to implement Manifest and SignatureProperties elements. Permitted only within Object in Signature content model.

### 5.1 The Manifest Element
- List of References; application decides which digests to check. If referenced from SignedInfo, overall digest checked by core; internal digests at application discretion.

### 5.2 The SignatureProperties Element
- Contains SignatureProperty elements with Target attribute referencing Signature element.

### 5.3 Processing Instructions in Signature Elements
- No PIs used; PIs inside SignedInfo will be signed if CanonicalizationMethod retains them.

### 5.4 Comments in Signature Elements
- Comments not used; if retained by CanonicalizationMethod, they are signed and changes break signature.

## 6. Algorithms
- Identified by URIs. All algorithms used may take parameters; explicit parameters as child elements.

### 6.1 Algorithm Identifiers and Implementation Requirements
| Algorithm | Requirement | Identifier |
|-----------|-------------|------------|
| SHA-1 (digest) | REQUIRED | `http://www.w3.org/2000/09/xmldsig#sha1` |
| Base64 (encoding) | REQUIRED | `http://www.w3.org/2000/09/xmldsig#base64` |
| HMAC-SHA1 (MAC) | REQUIRED | `http://www.w3.org/2000/09/xmldsig#hmac-sha1` |
| DSAwithSHA1 (signature) | REQUIRED | `http://www.w3.org/2000/09/xmldsig#dsa-sha1` |
| RSAwithSHA1 (signature) | RECOMMENDED | `http://www.w3.org/2000/09/xmldsig#rsa-sha1` |
| Canonical XML (omit comments) | REQUIRED | `http://www.w3.org/TR/2001/REC-xml-c14n-20010315` |
| Canonical XML with Comments | RECOMMENDED | `http://www.w3.org/TR/2001/REC-xml-c14n-20010315#WithComments` |
| XSLT (transform) | OPTIONAL | `http://www.w3.org/TR/1999/REC-xslt-19991116` |
| XPath (transform) | RECOMMENDED | `http://www.w3.org/TR/1999/REC-xpath-19991116` |
| Enveloped Signature (transform) | REQUIRED | `http://www.w3.org/2000/09/xmldsig#enveloped-signature` |

### 6.2 Message Digests
- Only SHA-1 defined; MD5 NOT RECOMMENDED.

#### 6.2.1 SHA-1
- 160-bit digest; DigestValue is base64 of 20-octet octet stream.

### 6.3 Message Authentication Codes
- HMAC-SHA1. Takes truncation length (in bits) as optional parameter; if omitted, all bits output.

#### 6.3.1 HMAC
- SignatureValue base64 encoded.

### 6.4 Signature Algorithms
- DSA-SHA1 (REQUIRED): signature value is base64 encoding of concatenation of r and s (each 20 octets I2OSP).
- RSA-SHA1 (RECOMMENDED): signature value base64 of EM under RSASSA-PKCS1-v1_5.

### 6.5 Canonicalization Algorithms
- REQUIRED Canonical XML omits comments; RECOMMENDED with comments.

#### 6.5.1 Canonical XML
- Specified by [XML-C14N]. Input octet stream or XPath node-set; output octet stream. Parameterized to omit or retain comments.

### 6.6 Transform Algorithms
- Strongly recommended to support RECOMMENDED transforms for interoperability.

#### 6.6.1 Canonicalization
- Any canonicalization usable as Transform.

#### 6.6.2 Base64
- Input octet stream; if node-set, convert via self::text() and string value. Output octet stream.

#### 6.6.3 XPath Filtering
- Input XPath node-set. XPath expression evaluated per node; if true, node included. Uses here() function.

#### 6.6.4 Enveloped Signature Transform
- Removes Signature element containing the transform from digest. Must produce same output as XPath transform with given expression.

#### 6.6.5 XSLT Transform
- Input octet stream; output octet stream. RECOMMEND canonicalization after XSLT for interoperability.

## 7. XML Canonicalization and Syntax Constraint Considerations
- Digital signatures require identical bits; canonicalization standardizes changeable aspects.
- Four categories of XML changes: basic XML (syntax constraints), DOM/SAX processing, character set conversion, namespace context.
- All canonicalization algorithms in this document use UTF-8 without BOM. **RECOMMEND** that signature applications create content in NFC and check consumed content is in NFC.
- Syntax constraints for signed material (including SignedInfo): default attributes explicitly present, entities expanded (except predefined), attribute white space normalized.

### 7.2 DOM/SAX Processing
- Appropriate canonicalization **MUST** be specified to re-serialize DOM/SAX input into same octet stream as signed.

### 7.3 Namespace Context and Portable Signatures
- Canonicalization imports namespace declarations from ancestor context; this may invalidate signatures when moved (e.g., into SOAP envelope). Applications may rely on enveloping application to divorce context or use alternative canonicalization (none specified in this version).

## 8. Security Considerations
- Transforms allow signing derived data; only what is signed is secure.
- Only what is "seen" should be signed; applications should sign what is presented.
- Applications should operate over transformed data, not original.
- All documents **MUST** be in NFC; encoding normalizations **SHOULD NOT** be part of signature transforms, or if they are, application **SHOULD** operate over normalized form.
- Public key vs. symmetric key models differ; user specified algorithms may have different models.
- Security depends on algorithm strength, key size, certificate chain, etc.

## 9. Schema, DTD, Data Model, and Valid Examples
- Normative schema and DTD available at listed URLs.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST generate laxly schema valid Signature elements as per schema. | MUST | 4.1 |
| R2 | Implementations MUST support REQUIRED canonicalization algorithms (Canonical XML omitting comments). | MUST | 4.3.1, 6.1 |
| R3 | XML based canonicalization MUST be provided with correct XPath node-set. | MUST | 4.3.1 |
| R4 | Implementations MUST support SHA-1 digest. | MUST | 6.1 |
| R5 | Implementations MUST support Base64 encoding. | MUST | 6.1 |
| R6 | Implementations MUST support HMAC-SHA1 MAC. | MUST | 6.1 |
| R7 | Implementations MUST support DSAwithSHA1 signature. | MUST | 6.1 |
| R8 | Implementations SHOULD support RSAwithSHA1 signature. | SHOULD | 6.1 |
| R9 | Implementations MUST support Enveloped Signature transform. | MUST | 6.1 |
| R10 | Compliance with Namespaces in XML is REQUIRED. | REQUIRED | 1.1 |
| R11 | The namespace URI that MUST be used is `http://www.w3.org/2000/09/xmldsig#`. | MUST | 1.3 |
| R12 | Applications MUST be able to parse URI syntax. | MUST | 4.3.3.1 |
| R13 | HTTP URI dereferencing MUST comply with HTTP status code definitions. | MUST | 4.3.3.1 |
| R14 | Same-document references MUST produce XPath node-set as specified. | MUST | 4.3.3.3 |
| R15 | Reference validation (digest check) is REQUIRED as part of core validation. | MUST | 3.2.1 |
| R16 | Signature validation (cryptographic) is REQUIRED as part of core validation. | MUST | 3.2.2 |
| R17 | KeyValue element MUST be implemented in KeyInfo. | MUST | 4.4 |
| R18 | RetrievalMethod SHOULD be implemented. | SHOULD | 4.4 |
| R19 | XPath transform is RECOMMENDED. | RECOMMENDED | 4.3.3.2 |
| R20 | Canonical XML with Comments is RECOMMENDED. | RECOMMENDED | 6.1 |
| R21 | XSLT transform is OPTIONAL. | OPTIONAL | 6.1 |
| R22 | All documents MUST be in NFC. | MUST | 8.1.3 |
| R23 | Encoding normalizations SHOULD NOT be part of signature transforms unless application operates over normalized form. | SHOULD NOT | 8.1.3 |
| R24 | MD5 usage is NOT RECOMMENDED. | NOT RECOMMENDED | 6.2 |
| R25 | MgmtData element is NOT RECOMMENDED. | NOT RECOMMENDED | 4.4.7 |

## Informative Annexes (Condensed)
- **Appendix: Changes from RFC 3075**: Lists incompatible changes: DSA key fields optionality and re-ordering, X509Data allowing multiple CRLs, PGPKeyID type changed to base64Binary, warnings added about namespace context.
- **Schema, DTD, Data Model, and Valid Examples**: Provides URLs for normative schema and DTD, RDF data model GIF, and two example XML files with cryptographic values (RSA and DSA). These are informative resources.