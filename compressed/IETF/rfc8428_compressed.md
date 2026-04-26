# RFC 8428: Sensor Measurement Lists (SenML)
**Source**: IETF | **Version**: Standards Track | **Date**: August 2018 | **Type**: Normative
**Original**: https://www.rfc-editor.org/info/rfc8428

## Scope (Summary)
Defines a format for representing simple sensor measurements and device parameters using a common data model with JSON, CBOR, XML, and EXI serializations. Designed for constrained devices and networks, enabling efficient transport via HTTP or CoAP.

## Normative References
- [BIPM] Bureau International des Poids et Mesures, "The International System of Units (SI)", 8th Edition, 2006.
- [IEEE.754] IEEE, "Standard for Binary Floating-Point Arithmetic", IEEE Standard 754.
- [NIST811] Thompson, A. and B. Taylor, "Guide for the Use of the International System of Units (SI)", NIST SP 811, DOI 10.6028/NIST.SP.811e2008, March 2008.
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3688] Mealling, M., "The IETF XML Registry", BCP 81, RFC 3688, January 2004.
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, October 2006.
- [RFC6838] Freed, N., Klensin, J., and T. Hansen, "Media Type Specifications and Registration Procedures", BCP 13, RFC 6838, January 2013.
- [RFC7049] Bormann, C. and P. Hoffman, "Concise Binary Object Representation (CBOR)", RFC 7049, October 2013.
- [RFC7252] Shelby, Z., Hartke, K., and C. Bormann, "The Constrained Application Protocol (CoAP)", RFC 7252, June 2014.
- [RFC7303] Thompson, H. and C. Lilley, "XML Media Types", RFC 7303, July 2014.
- [RFC8126] Cotton, M., Leiba, B., and T. Narten, "Guidelines for Writing an IANA Considerations Section in RFCs", BCP 26, RFC 8126, June 2017.
- [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.
- [RFC8259] Bray, T., Ed., "The JavaScript Object Notation (JSON) Data Interchange Format", STD 90, RFC 8259, December 2017.
- [RNC] ISO/IEC, "Information technology -- Document Schema Definition Language (DSDL) -- Part 2: Regular-grammar-based validation -- RELAX NG", ISO/IEC 19757-2, Annex C, December 2008.
- [TIME_T] The Open Group Base Specifications, "Open Group Standard - Vol. 1: Base Definitions, Issue 7", Section 4.16, "Seconds Since the Epoch", IEEE Standard 1003.1, 2018.
- [W3C.REC-exi-20140211] Schneider, J., Kamiya, T., Peintner, D., and R. Kyusakov, "Efficient XML Interchange (EXI) Format 1.0 (Second Edition)", W3C Recommendation, February 2014.
- [W3C.REC-xml-20081126] Bray, T., Paoli, J., Sperberg-McQueen, M., Maler, E., and F. Yergeau, "Extensible Markup Language (XML) 1.0 (Fifth Edition)", W3C Recommendation, November 2008.
- [W3C.REC-xmlschema-1-20041028] Thompson, H., Beech, D., Maloney, M., and N. Mendelsohn, "XML Schema Part 1: Structures Second Edition", W3C Recommendation, October 2004.
- [XPointerElement] Grosso, P., Maler, E., Marsh, J., and N. Walsh, "XPointer element() Scheme", W3C Recommendation, March 2003.
- [XPointerFramework] Grosso, P., Maler, E., Marsh, J., and N. Walsh, "XPointer Framework", W3C Recommendation, March 2003.

## Definitions and Abbreviations
- **SenML Record**: One measurement or configuration instance in time using the SenML data model.
- **SenML Pack**: One or more SenML Records in an array structure.
- **SenML Label**: A short name used in SenML Records to denote different SenML fields.
- **SenML Field**: A component of a record that associates a value to a SenML Label.
- **SenSML**: Sensor Streaming Measurement List (see Section 4.8).
- **SenSML Stream**: One or more SenML Records to be processed as a stream.
- **Key Words**: "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", "OPTIONAL" as defined in BCP 14 [RFC2119] [RFC8174].

## 4. SenML Structure and Semantics
Each SenML Pack is an array of SenML Records. Two kinds of fields: base and regular. Base fields apply to subsequent records until overridden. Regular fields apply only to the current record.

### 4.1. Base Fields
- **Base Name (bn)**: String prepended to Name fields in subsequent records.
- **Base Time (bt)**: Time added to Time fields in subsequent records.
- **Base Unit (bu)**: Assumed unit for all entries unless overridden.
- **Base Value (bv)**: Value added to Value fields in subsequent records.
- **Base Sum (bs)**: Sum added to Sum fields in subsequent records.
- **Base Version (bver)**: Optional positive integer, defaults to 10 if not present.

### 4.2. Regular Fields
- **Name (n)**: Sensor or parameter identifier. Concatenated with Base Name must be globally unique. Optional if Base Name present.
- **Unit (u)**: Unit for measurement value. Optional.
- **Value (v, vs, vb, vd)**: Exactly one Value field MUST appear unless there is a Sum field.
  - Numeric value (v), String value (vs), Boolean value (vb), Data value (vd).
- **Sum (s)**: Integrated sum of values over time. Optional.
- **Time (t)**: Time when value was recorded. Optional.
- **Update Time (ut)**: Maximum time before next reading update. Optional.

### 4.3. SenML Labels
| Name | Label | CBOR Label | JSON Type | XML Type |
|------|-------|------------|-----------|----------|
| Base Name | bn | -2 | String | string |
| Base Time | bt | -3 | Number | double |
| Base Unit | bu | -4 | String | string |
| Base Value | bv | -5 | Number | double |
| Base Sum | bs | -6 | Number | double |
| Base Version | bver | -1 | Number | int |
| Name | n | 0 | String | string |
| Unit | u | 1 | String | string |
| Value | v | 2 | Number | double |
| String Value | vs | 3 | String | string |
| Boolean Value | vb | 4 | Boolean | boolean |
| Data Value | vd | 8 | String (base64url) | string (base64url) |
| Sum | s | 5 | Number | double |
| Time | t | 6 | Number | double |
| Update Time | ut | 7 | Number | double |

### 4.4. Extensibility
- Custom fields are allowed. Implementations MUST ignore unrecognized fields unless the label name ends with "_", in which case an error MUST be generated.
- All Records in a Pack MUST have the same version number. Systems MUST check Base Version; if larger than understood, MUST NOT use the object.

### 4.5. Records and Their Fields
#### 4.5.1. Names
- Concatenated name (Base Name + Name) MUST consist only of characters A-Z, a-z, 0-9, '-', ':', '.', '/', '_' and MUST start with a letter or digit.
- RECOMMENDED to represent concatenated names as URIs [RFC3986] or URNs [RFC8141], but restricted character set applies.

#### 4.5.2. Units
- If no Unit in record, Base Unit is used. No unit and no Base Unit allowed; application context must provide unit information.

#### 4.5.3. Time
- Base Time and Time are added. Missing fields default to 0.
- Values less than 2^28 represent relative time (seconds from "now"). Zero means "now".
- Values >= 2^28 represent absolute time (Unix epoch). Smallest absolute: 1978-07-04 21:24:16 UTC.
- Care required to avoid sum reaching 2^28 when relative intended.

#### 4.5.4. Values
- If only Base Sum or Sum present, missing defaults to 0. Added together.
- If Base Value or Value not present, missing defaults to 0. Added together.
- A single measurement per Record; multiple data values at same time should be separate Records linked by Time.

### 4.6. Resolved Records
- Resolved Records: no base fields (except Base Version) and no relative times. Base values applied to each record.
- Base Version field MUST NOT be present if SenML version defined in this document is used; otherwise MUST be present in all resolved Records.

### 4.7. Associating Metadata
- Static metadata carried out of band (e.g., via CoRE Link Format [RFC6690]). Content-Type link attribute indicates SenML format.

### 4.8. Sensor Streaming Measurement Lists (SenSML)
- Streaming usage of SenML. Systems or protocols using SenML in this fashion MUST specify streaming mode. Separate media types (application/sensml+json, etc.).
- In streaming, "now" for relative times is based on when the specific Record is sent.

### 4.9. Configuration and Actuation Usage
- SenML Pack sent with POST/PUT interpreted as request to change values. Semantics described by target resource (e.g., [RID-CoRE]).

## 5. JSON Representation (application/senml+json)
- Root is array of JSON objects. Labels from Table 2 used as member names.
- Only UTF-8 allowed. Data Value base64url encoded without padding.
- Systems MUST process IEEE double-precision floating-point numbers. Mantissa SHOULD be <19 chars, exponent <5 chars. Exponent 'e' MUST be lowercase.

### 5.1. Examples
(Informative; condensed to key patterns)
- Single data point, multiple data points, multiple measurements, resolved, multiple types, collection of resources, actuation. See RFC 8428 sections 5.1.1–5.1.7 for full examples.

## 6. CBOR Representation (application/senml+cbor)
- Equivalent to JSON with changes:
  - Numbers: integer, float, or decimal fraction (CBOR Tag 4). Representation MUST be chosen so that conversion to IEEE double gives same value.
  - Version number: unsigned integer only.
  - String values: definite-length text string (major type 3). Data value: definite-length byte string (major type 2).
  - Labels: integers from Table 4. No additional integer map keys defined; extensions use string keys.
  - Streaming: indefinite-length array SHOULD be used; non-streaming: definite-length array MUST be used.

## 7. XML Representation (application/senml+xml)
- UTF-8 only. Data Value base64url without padding.
- Root element <sensml> containing <senml> elements. Fields are XML attributes.
- RelaxNG schema provided in Section 7.

## 8. EXI Representation (application/senml-exi)
- SHOULD use strict schema mode of EXI with schemaId "a". Non-strict MAY be used for extensions.
- EXI Cookie SHOULD NOT be used over CoAP/HTTP.
- XSD Schema provided.

## 9. Fragment Identification Methods
- Use "rec" scheme: rec=3, rec=3-6, rec=19-*, rec=3,5, rec=3-5,10,19-*.
- For XML/EXI, XPointer element() scheme also available.

## 10. Usage Considerations
(Informative; condensed)
- Sum field (integral) useful for cumulative measurements like energy. Applications must handle wrap, reset, and unknown accumulate start.
- Data like counters sent in Value field, not Sum.

## 11. CDDL (Informative)
- Common CDDL for CBOR and JSON SenML provided in Figure 1. JSON-specific and CBOR-specific in Figures 2 and 3.

## 12. IANA Considerations
- New "Sensor Measurement Lists (SenML)" registry with subregistries.

### 12.1. SenML Units Registry
- Table 6 lists units (m, kg, s, A, Cel, %, etc.). New entries by Expert Review per [RFC8126] with guidelines.
- Units marked with asterisk NOT RECOMMENDED for new producers but SHOULD be implemented by consumers.

### 12.2. SenML Labels Registry
- Table 7 with Name, Label, CBOR Label, JSON Type, XML Type, EXI ID.
- New base labels MUST start with "b". Regular labels MUST NOT. Value labels MUST have "Value" in long name.
- Extensions with mandatory understanding MUST end label name with "_".

### 12.3. Media Type Registrations
- Registers media types for each serialization (JSON, CBOR, XML, EXI) plus streaming variants (SenSML).
- Must ignore unknown key-value pairs unless key ends with "_", then error.
- CoAP Content-Format IDs assigned: senml+json=110, sensml+json=111, senml+cbor=112, sensml+cbor=113, senml-exi=114, sensml-exi=115, senml+xml=310, sensml+xml=311.

### 12.4. XML Namespace Registration
- URI: urn:ietf:params:xml:ns:senml

## 13. Security Considerations
- SenML provides no security; relies on transfer protocol (e.g., TLS). For sensitive data and actuation, confidentiality, integrity, authentication MUST be provided.
- No executable content in SenML. Future extensions could embed executable content.
- Care needed to maintain integrity of unresolved Packs.

## 14. Privacy Considerations
- Name fields uniquely identify sources/destinations. Long-term stable identifiers may pose correlation risks per [RFC6973] and [RFC7721]; use with care.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Exactly one Value field MUST appear unless there is a Sum field | MUST | Sec 4.2 |
| R2 | Implementations MUST ignore unrecognized fields unless label ends with '_', then error MUST be generated | MUST | Sec 4.4 |
| R3 | All Records in a Pack MUST have the same version number | MUST | Sec 4.4 |
| R4 | Concatenated name MUST consist only of allowed characters and MUST start with a letter/digit | MUST | Sec 4.5.1 |
| R5 | Base Version field MUST NOT be present in resolved Records unless version is not the one defined | MUST | Sec 4.6 |
| R6 | Systems MUST check Base Version and MUST NOT use object if version larger than understood | MUST | Sec 4.4 |
| R7 | Streaming usage MUST be explicitly specified | MUST | Sec 4.8 |
| R8 | CBOR non-streaming arrays MUST use definite length | MUST | Sec 6 |
| R9 | EXI SHOULD use strict schema mode | SHOULD | Sec 8 |
| R10 | JSON exponent 'e' MUST be lowercase | MUST | Sec 5 |
| R11 | CoAP Content-Format IDs as per IANA registration | MUST | Sec 12.5 |
| R12 | New entries in SenML Labels must follow naming conventions | MUST | Sec 12.2 |
| R13 | New units added by Expert Review must follow guidelines | MUST | Sec 12.1 |

## Informative Annexes (Condensed)
- **Appearance of examples**: Sections 5.1.1–5.1.7 provide illustrative JSON examples for single point, multiple points, multiple measurements, resolved, multiple types, collection, and actuation. Not normative.
- **Size comparisons**: Table 3 shows sizes of an example in JSON/XML/CBOR/EXI (161–649 bytes, compressed 184–235 bytes).
- **CDDL (Section 11)**: Informative common and specific CDDL for JSON and CBOR, defining pack structure and field types.