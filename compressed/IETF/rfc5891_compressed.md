# RFC 5891: Internationalized Domain Names in Applications (IDNA): Protocol
**Source**: IETF (Internet Engineering Task Force) | **Version**: Standards Track | **Date**: August 2010 | **Type**: Normative  
**Obsoletes**: RFC 3490, RFC 3491 | **Updates**: RFC 3492  
**Original**: https://www.rfc-editor.org/info/rfc5891

## Scope (Summary)
This document specifies the IDNA2008 protocol mechanism for registering and looking up Internationalized Domain Names (IDNs) in a way that does not require changes to the DNS itself. It defines two separate protocols: one for IDN registration (Section 4) and one for IDN lookup (Section 5). IDNA applies only to domain names, not free text.

## Normative References
- RFC 1034: Domain names – concepts and facilities
- RFC 1035: Domain names – implementation and specification
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels (BCP 14)
- RFC 3492: Punycode: A Bootstring encoding of Unicode for IDNA
- RFC 5890: IDNA: Definitions and Document Framework
- RFC 5892: The Unicode Code Points and IDNA
- RFC 5893: Right-to-Left Scripts for IDNA
- Unicode-UAX15: Unicode Standard Annex #15: Unicode Normalization Forms

## Definitions and Abbreviations
- **A-label**: The ASCII-compatible encoding of a U-label, consisting of the ACE prefix "xn--" followed by a Punycode encoding of the U-label.
- **U-label**: A Unicode string that is a valid IDNA label after passing all validation tests.
- **NR-LDH label**: A label that contains only letters, digits, or hyphens and does not start with the ACE prefix.
- **ACE prefix**: The string "xn--" used to indicate an A-label.
- **Putative label**: A string that has not been fully evaluated for conformance to applicable IDNA rules.
- **IDNA-aware**: Applications that understand and process U-labels / A-labels as defined by IDNA.
- **KEYWORDS**: The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

## 3. Requirements and Applicability

### 3.1. Requirements
1. **R1**: Whenever a domain name is put into a domain name slot that is not IDNA-aware, it MUST contain only ASCII characters (A-labels or NR-LDH labels), unless the DNS application is not subject to historical recommendations for "hostname"-style names.
2. **R2**: Labels MUST be compared using equivalent forms: either both A-labels or both U-labels. A-labels MUST be compared as case-insensitive ASCII. U-labels MUST be compared as-is, without case folding or other intermediate steps. Validation SHOULD be performed for security reasons.
3. **R3**: Labels being registered MUST conform to Section 4. Labels being looked up MUST conform to Section 5.

### 3.2. Applicability
- IDNA applies to all domain names in all domain name slots in protocols except where explicitly excluded.
- IDNs in protocols not upgraded to IDNA-aware MUST be in A-label form.
- IDNs actually appearing in DNS queries or responses MUST be A-labels.
- IDNA-aware protocols MAY accept U-labels, A-labels, or both.
- IDNA is not defined for extended label types (RFC 2671 Section 3).

#### 3.2.1. DNS Resource Records
- IDNA applies only to domain names in NAME and RDATA fields of DNS resource records whose CLASS is IN.
- Underscore labels (e.g., SRV records) are incompatible with IDNA coding but may be part of a domain that uses IDN labels at higher levels.

#### 3.2.2. Non-Domain-Name Data Types Stored in the DNS
- IDNA does not enable non-ASCII characters in other structured RDATA fields (e.g., email local parts in SOA records). Those require separate standards updates.

## 4. Registration Protocol

### 4.1. Input to IDNA Registration
- The string MUST be in Unicode, Normalization Form C (NFC).
- Registries MUST accept only the exact string free of any mappings or local adjustments.
- Accepted input forms (RECOMMENDED: pair of A-label and U-label; second: A-label only; third: U-label only).

### 4.2. Permitted Character and Label Validation

#### 4.2.1. Input Format
- If both U-label and A-label are available, registry MUST:
  - Ensure A-label is lowercase.
  - Convert A-label to U-label, perform tests on that U-label.
  - Verify that the A-label produced by Section 4.4 matches the input A-label.
  - Reject if any test fails.
- If only A-label provided and conversion not performed, registry MUST verify superficial validity (Punycode rules). Strings that appear to be A-labels but are not valid MUST NOT be placed in DNS zones supporting IDNA.

#### 4.2.2. Rejection of Characters That Are Not Permitted
- The candidate Unicode string MUST NOT contain characters from DISALLOWED or UNASSIGNED lists (RFC 5892).

#### 4.2.3. Label Validation

##### 4.2.3.1. Hyphen Restrictions
- MUST NOT contain "--" in third and fourth character positions.
- MUST NOT start or end with a hyphen.

##### 4.2.3.2. Leading Combining Marks
- MUST NOT begin with a combining mark.

##### 4.2.3.3. Contextual Rules
- For characters identified as CONTEXTJ or CONTEXTO (RFC 5892), a non-null rule MUST exist and must positively confirm validity; otherwise label is invalid.

##### 4.2.3.4. Labels Containing Characters Written Right to Left
- If label contains RTL characters, it MUST meet Bidi criteria (RFC 5893).

#### 4.2.4. Registration Validation Requirements
- Strings that contain at least one non-ASCII character, pass all tests in 4.2.3, and are ≤63 characters in ACE form, are U-labels.

### 4.3. Registry Restrictions
- Registries at all levels MAY establish additional policies and reject labels based on local language, script, or other factors. (See Rationale document RFC 5894 Section 3.2.)

### 4.4. Punycode Conversion
- The U-label is converted to an A-label using Punycode algorithm (RFC 3492) with ACE prefix "xn--". The ACE prefix is "xn--" (same as IDNA2003). Failure conditions in Punycode cannot occur if input is a valid U-label.

### 4.5. Insertion in the Zone
- The label is registered by inserting the A-label into a DNS zone.

## 5. Domain Name Lookup Protocol

### 5.1. Label String Input
- User supplies string in local character set (typing, clicking, reading from file, etc.). Processing prior to IDNA invocation is local.

### 5.2. Conversion to Unicode
- String is converted to Unicode (if not already) using local mappings. Result MUST be a Unicode string in NFC.

### 5.3. A-label Input
- If input appears to be an A-label (starts with "xn--", case-insensitive), the application MAY attempt conversion to U-label. If conversion to Unicode is performed, MUST apply tests of 5.4 and conversion of 5.5 and reject if result not identical to original.
- Conversion and testing SHOULD be performed if domain name will be presented to user in native character form.
- If conversion not performed, SHOULD at least test for invalid Punycode formats.

### 5.4. Validation and Character List Testing
- Putative U-labels with any of the following characteristics MUST be rejected prior to DNS lookup:
  1. Not in NFC.
  2. Contains "--" in third and fourth character positions.
  3. First character is a combining mark.
  4. Contains code points in DISALLOWED category (RFC 5892).
  5. Contains CONTEXTJ code points that do not conform to their contextual rules (rule must be non-null).
  6. Contains CONTEXTO code points with no defined rule (rule table must exist; application need not test the rule, only that rule is defined).
  7. Contains UNASSIGNED code points (relative to Unicode version in use).
- Application SHOULD apply Bidi compliance test (RFC 5893). May be omitted if conditions enforced elsewhere.
- For all other strings, application MUST rely on presence/absence in DNS. Applications that decline to look up a conforming string are not compliant.

### 5.5. Punycode Conversion
- Validated string is converted to ACE form using Punycode algorithm and ACE prefix "xn--".

### 5.6. DNS Name Resolution
- The A-label is combined with other labels to form a fully-qualified domain name and looked up in DNS using normal resolver procedures.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Non-IDNA-aware slots: domain names MUST contain only ASCII (A-labels or NR-LDH labels). | MUST | 3.1(1) |
| R2 | Labels MUST be compared using equivalent forms; if both A-labels, case-insensitive ASCII; if both U-labels, exact match without case folding. Validation SHOULD be performed. | MUST / SHOULD | 3.1(2) |
| R3 | Registration conforms to Section 4; lookup conforms to Section 5. | MUST | 3.1(3) |
| R4 | IDNs in protocols not IDNA-aware MUST be A-label form. | MUST | 3.2 |
| R5 | IDNs in DNS queries/responses MUST be A-labels. | MUST | 3.2 |
| R6 | Registration input MUST be NFC Unicode. | MUST | 4.1 |
| R7 | Registry MUST accept exact string; no mappings. | MUST | 4.1 |
| R8 | If both A-label and U-label provided, registry MUST verify match. | MUST | 4.2.1 |
| R9 | Candidate Unicode string MUST NOT contain DISALLOWED or UNASSIGNED characters. | MUST | 4.2.2 |
| R10 | U-label MUST NOT contain "--" in positions 3-4, MUST NOT start/end with hyphen. | MUST | 4.2.3.1 |
| R11 | U-label MUST NOT begin with combining mark. | MUST | 4.2.3.2 |
| R12 | CONTEXTJ/CONTEXTO characters MUST have non-null rules that positively confirm validity. | MUST | 4.2.3.3 |
| R13 | Labels with RTL characters MUST meet Bidi criteria. | MUST | 4.2.3.4 |
| R14 | Lookup conversion to Unicode (if performed) MUST follow Section 5.4/5.5 and reject if mismatch. | MUST | 5.3 |
| R15 | Putative U-labels MUST be rejected prior to lookup if they fail any of seven tests (NFC, double hyphen in positions 3-4, leading combining mark, DISALLOWED, CONTEXTJ rules fail, CONTEXTO no rule, UNASSIGNED). | MUST | 5.4 |
| R16 | Lookup application SHOULD apply Bidi test. | SHOULD | 5.4 |
| R17 | For strings passing Section 5.4 tests, application MUST rely on DNS presence/absence. | MUST | 5.4 |
| R18 | Applications that decline to look up a conforming string are not in conformance. | MUST | 5.4 |
| R19 | Lookup application MUST convert validated U-label to ACE using Punycode. | MUST | 5.5 |

## Informative Annexes (Condensed)
- **Appendix A – Summary of Major Changes from IDNA2003**: Lists 10 key changes: base character set updated from Unicode 3.2 to version agnostic; separated registration/lookup definitions; disallowed symbol/punctuation except special exceptions; removed mapping and normalization from protocol; changed character allowlist to be property-based; introduced context-dependent characters; allowed languages like Dhivehi and Yiddish; improved Bidi handling; removed dot separator from mandatory protocol; made some previously valid labels invalid.