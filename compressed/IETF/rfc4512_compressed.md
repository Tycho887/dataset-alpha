# RFC 4512: Lightweight Directory Access Protocol (LDAP): Directory Information Models
**Source**: IETF | **Version**: Standards Track, June 2006 | **Date**: June 2006 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc4512

## Scope (Summary)
This document describes the X.500 Directory Information Models as used by LDAP, covering models of user information, administrative/operational information, directory schema (including subschema), and server-specific data (root DSE). It obsoletes portions of RFC 2251, 2252, 2256, and all of RFC 3674.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, November 2003.
- [RFC3671] Zeilenga, K., "Collective Attributes in LDAP", RFC 3671, December 2003.
- [RFC3672] Zeilenga, K., "Subentries in LDAP", RFC 3672, December 2003.
- [RFC4234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 4234, October 2005.
- [RFC4422] Melnikov, A. and K. Zeilenga, "Simple Authentication and Security Layer (SASL)", RFC 4422, June 2006.
- [RFC4510] Zeilenga, K., "LDAP: Technical Specification Road Map", RFC 4510, June 2006.
- [RFC4511] Sermersheim, J., "LDAP: The Protocol", RFC 4511, June 2006.
- [RFC4513] Harrison, R., "LDAP: Authentication Methods and Security Mechanisms", RFC 4513, June 2006.
- [RFC4514] Zeilenga, K., "LDAP: String Representation of Distinguished Names", RFC 4514, June 2006.
- [RFC4515] Smith, M. and T. Howes, "LDAP: String Representation of Search Filters", RFC 4515, June 2006.
- [RFC4516] Smith, M. and T. Howes, "LDAP: Uniform Resource Locator", RFC 4516, June 2006.
- [RFC4517] Legg, S., "LDAP: Syntaxes and Matching Rules", RFC 4517, June 2006.
- [RFC4519] Sciberras, A., "LDAP: Schema for User Applications", RFC 4519, June 2006.
- [RFC4520] Zeilenga, K., "IANA Considerations for LDAP", BCP 64, RFC 4520, June 2006.
- [Unicode] The Unicode Consortium, "The Unicode Standard, Version 3.2.0".
- [X.500] ITU-T, "The Directory -- Overview of concepts, models and services", X.500(1993).
- [X.501] ITU-T, "The Directory -- Models", X.501(1993).
- [X.680] ITU-T, "Abstract Syntax Notation One (ASN.1) - Specification of Basic Notation", X.680(2002).

## Definitions and Abbreviations
- **DIB**: Directory Information Base – collection of information held in the Directory.
- **DIT**: Directory Information Tree – hierarchical tree structure organizing entries.
- **RDN**: Relative Distinguished Name – relative name of an entry within its immediate superior.
- **DN**: Distinguished Name – fully qualified name of an entry.
- **AVA**: Attribute Value Assertion – pair of attribute description and value used in naming.
- **OID**: Object Identifier – dot-decimal identifier for schema elements.
- **DUA**: Directory User Agent – client.
- **DSA**: Directory System Agent – server.
- **SASL**: Simple Authentication and Security Layer.
- **ABNF**: Augmented Backus-Naur Form (RFC 4234).
- **Naming Context**: Subtree of entries held in a single master DSA.
- **Subentry**: Special entry for administrative/operational information.

## 1. Introduction
- This document is an integral part of the LDAP technical specification [RFC4510].
- It obsoletes RFC 2251 Sections 3.2, 3.4, and portions of 4 and 6; RFC 2252 Sections 4, 5, and 7; RFC 2256 Sections 5.1, 5.2, 7.1, 7.2; and RFC 3674 entirely.
- Adaptations from [X.501] apply only to this protocol.

### 1.3 Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in BCP 14 [RFC2119].

### 1.4 Common ABNF Productions
- **keystring**, **number**, **oid**, **numericoid**, **descr** ABNF rules are defined for syntaxes (see full text for exact productions).
- *Short names (descriptors)*: case-insensitive, used as aliases for OIDs. Implementations SHOULD treat ambiguous short names as unrecognized.

## 2. Model of Directory User Information
- Directory entries are organized hierarchically in the DIT.
- **Object entry**: represents a particular object.
- **Alias entry**: provides alternative naming.
- **Subentry**: holds administrative/operational information.

### 2.1 Directory Information Tree
- Entries are vertices; arcs define superior/subordinate relationships.
- "An entry's immediate superior is also known as the entry's parent, and an entry's immediate subordinate is also known as the entry's child."

### 2.2 Structure of an Entry
- An entry consists of attributes (user or operational).
- Attribute = attribute description (type + zero or more options) + one or more values.
- "No two values of an attribute may be equivalent." (Equality based on matching rule, or identical if no equality rule.)
- "Additionally, no attribute is to have a value that is not equivalent to itself."
- For naming, one and only one value (distinguished value) is used in the RDN.

### 2.3 Naming of Entries
#### 2.3.1 Relative Distinguished Names (RDN)
- Composed of one or more AVAs (attribute description with zero options + value).
- "An entry's relative distinguished name must be unique among all immediate subordinates of the entry's immediate superior."
- Multi-valued RDNs allowed.

#### 2.3.2 Distinguished Names (DN)
- Concatenation of RDN and immediate superior's DN.
- "A Distinguished Name unambiguously refers to an entry in the tree."

#### 2.3.3 Alias Names
- Alternative name for an object provided by alias entries.

### 2.4 Object Classes
- Object class: "an identified family of objects (or conceivable objects) that share certain characteristics" [X.501].
- Three kinds: Abstract, Structural, Auxiliary.
- Object class identified by OID and optionally short names.
- Inherits required/allowed attributes from superclasses.

#### 2.4.1 Abstract Object Classes
- Provide base characteristics; entries cannot belong directly unless they also belong to a structural or auxiliary class that inherits from it.
- "All structural object classes derive (directly or indirectly) from the 'top' abstract object class."
- **'top' object class**: `( 2.5.6.0 NAME 'top' ABSTRACT MUST objectClass )`
- "All entries belong to the 'top' abstract object class."

#### 2.4.2 Structural Object Classes
- Used to define DIT structure; each entry has exactly one structural object class (most subordinate in its superclass chain).
- "The structural object class of an entry shall not be changed."
- "Structural object classes cannot subclass auxiliary object classes."

#### 2.4.3 Auxiliary Object Classes
- Augment characteristics of entries; can change over time.
- "An entry can belong to any subset of the set of auxiliary object classes allowed by the DIT content rule associated with the structural object class of the entry. If no DIT content rule is associated with the structural object class of the entry, the entry cannot belong to any auxiliary object class."

### 2.5 Attribute Descriptions
- Attribute description: attributetype + zero or more options (case-insensitive, order irrelevant).
- Attribute description with unrecognized type or option:
    - Servers SHALL treat as unrecognized.
    - Clients MAY treat unrecognized option as tagging option.
- All attributes of an entry must have distinct attribute descriptions.

#### 2.5.1 Attribute Types
- Governs multi-value, syntax, matching rules.
- If no equality matching rule: cannot be used for naming; values cannot be independently added/deleted; attribute value assertions cannot be performed.
- Equality rule must be transitive and commutative.
- Subtyping restrictions:
    - Subtype must have same usage as direct supertype.
    - Syntax must be same or refinement.
    - Subtype must be collective if supertype is collective.

#### 2.5.2 Attribute Options
- Tagging options can be associated with attributes held in the directory.
- Mutually exclusive options: attribute description treated as unrecognized.
- Future options must detail relation to tagging options.

#### 2.5.2.1 Tagging Options
- "Attributes held in the directory can have attribute descriptions with any number of tagging options. Tagging options are never mutually exclusive."
- Subtyping rules for attribute descriptions with options.

### 2.5.3 Attribute Description Hierarchies
- "Attribute hierarchies allow access to the DIB with varying degrees of granularity."
- For subschema administration: "MUST name" is fulfilled by 'name' or 'name;x-tag-option', but not by 'CN' (even though CN is subtype of 'name').
- For other policy administration, descriptions are treated as distinct unless stated otherwise.

### 2.6 Alias Entries
- Alias entry provides alternative name; contains 'aliasedObjectName' attribute.
- "An alias entry shall have no subordinates, so that an alias entry is always a leaf entry."
- "Every alias entry shall belong to the 'alias' object class."

#### 2.6.1 'alias' Object Class
```
( 2.5.6.1 NAME 'alias' SUP top STRUCTURAL MUST aliasedObjectName )
```

#### 2.6.2 'aliasedObjectName' Attribute Type
- Holds name of the entry pointed to by alias.
```
( 2.5.4.1 NAME 'aliasedObjectName' EQUALITY distinguishedNameMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.12 SINGLE-VALUE )
```

## 3. Directory Administrative and Operational Information
- LDAP implementations MAY support other aspects of X.501 administrative model.

### 3.1 Subtrees
- Collection of object and alias entries (not subentries) with defined boundaries.

### 3.2 Subentries
- Holds administrative/operational information associated with a subtree.
- For servers not implementing X.500(93) subentries, use object entry with applicable auxiliary class (e.g., 'subschema').
- Object entry's RDN "SHALL be formed from a value of the 'cn' (commonName) attribute".

### 3.3 The 'objectClass' attribute
- Each entry has an 'objectClass' attribute.
```
( 2.5.4.0 NAME 'objectClass' EQUALITY objectIdentifierMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.38 )
```
- Values can be modified, but the attribute cannot be removed.
- Servers that follow X.500(93) models "SHALL restrict modifications of this attribute to prevent the basic structural class of the entry from being changed."
- "When creating an entry or adding an 'objectClass' value to an entry, all superclasses of the named classes SHALL be implicitly added as well if not already present."
- "Servers SHALL restrict modifications of this attribute to prevent superclasses of remaining 'objectClass' values from being deleted."

### 3.4 Operational Attributes
- Three varieties: directory operational, DSA-shared, DSA-specific.
- Not normally returned in search results unless explicitly requested.
- Entries may contain: creatorsName, createTimestamp, modifiersName, modifyTimestamp (Servers SHOULD maintain these).

#### 3.4.1 'creatorsName'
```
( 2.5.18.3 NAME 'creatorsName' EQUALITY distinguishedNameMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.12 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

#### 3.4.2 'createTimestamp'
```
( 2.5.18.1 NAME 'createTimestamp' EQUALITY generalizedTimeMatch ORDERING generalizedTimeOrderingMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.24 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

#### 3.4.3 'modifiersName'
```
( 2.5.18.4 NAME 'modifiersName' EQUALITY distinguishedNameMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.12 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

#### 3.4.4 'modifyTimestamp'
```
( 2.5.18.2 NAME 'modifyTimestamp' EQUALITY generalizedTimeMatch ORDERING generalizedTimeOrderingMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.24 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

#### 3.4.5 'structuralObjectClass'
```
( 2.5.21.9 NAME 'structuralObjectClass' EQUALITY objectIdentifierMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.38 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

#### 3.4.6 'governingStructureRule'
```
( 2.5.21.10 NAME 'governingStructureRule' EQUALITY integerMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.27 SINGLE-VALUE NO-USER-MODIFICATION USAGE directoryOperation )
```

## 4. Directory Schema
- The Directory Schema comprises definitions of: Name Forms, DIT Structure Rules, DIT Content Rules, Object Classes, Attribute Types, Matching Rules, LDAP Syntaxes.

### 4.1 Schema Definitions
- Definitions use ABNF with common productions and specific production for qdstrings, etc.
- **NAME field**: set of short names.
- **DESC field**: descriptive string.
- **OBSOLETE field**: indicates not active.
- Extensions beginning with "X-" are reserved for private experiments.

#### 4.1.1 Object Class Definitions
- ABNF provided.
- kind: ABSTRACT, STRUCTURAL, or AUXILIARY (default STRUCTURAL).
- MUST and MAY specify required/allowed attribute types.

#### 4.1.2 Attribute Types
- ABNF provided.
- Must contain at least one of SUP or SYNTAX.
- If SUP provided, EQUALITY, ORDERING, SUBSTR inherit from supertype if not specified.
- Usage: userApplications (default), directoryOperation, distributedOperation, dSAOperation.
- "NO-USER-MODIFICATION requires an operational usage."
- Suggested minimum upper bound in curly braces after SYNTAX OID.

#### 4.1.3 Matching Rules
- ABNF provided; used for attribute value assertions, search filters, etc.

#### 4.1.4 Matching Rule Uses
- Lists attribute types suitable for extensibleMatch search filter.
- ABNF provided.

#### 4.1.5 LDAP Syntaxes
- Identified by OID; ABNF provided.

#### 4.1.6 DIT Content Rules
- Apply to entries of a particular structural object class.
- "An entry may only belong to auxiliary object classes listed in the governing content rule."
- "An entry must contain all attributes required by the object classes the entry belongs to as well as all attributes required by the governing content rule."
- "An entry cannot include any attribute precluded by the governing content rule."
- ABNF provided for DITContentRuleDescription.

#### 4.1.7 DIT Structure Rules and Name Forms
##### 4.1.7.1 DIT Structure Rules
- Relate a name form to superior rules.
- ABNF provided; ruleid is a number.
- If no superior rules, applies to an autonomous administrative point.

##### 4.1.7.2 Name Forms
- Specifies permissible RDN for entries of a particular structural object class.
- "All attribute types in the required ('MUST') and allowed ('MAY') lists shall be different."
- ABNF provided.

### 4.2 Subschema Subentries
- Used to administer schema definitions.
- Servers following X.500(93) "SHOULD implement subschema using the X.500 subschema mechanisms" (subentries).
- Servers that master entries and permit modifications "SHALL implement and provide access to these subschema (sub)entries including providing a 'subschemaSubentry' attribute in each modifiable entry."
- "It is strongly RECOMMENDED that all other servers implement this as well."
- 'subschemaSubentry' attribute: `( 2.5.18.10 NAME 'subschemaSubentry' ... )`
- Subschema (sub)entry belongs to 'subschema' auxiliary object class: `( 2.5.20.1 NAME 'subschema' AUXILIARY MAY ( dITStructureRules $ nameForms $ ditContentRules $ objectClasses $ attributeTypes $ matchingRules $ matchingRuleUse ) )`
- Servers "SHOULD provide the attributes 'createTimestamp' and 'modifyTimestamp' in subschema (sub)entries."

#### 4.2.1 'objectClasses' attribute
```
( 2.5.21.6 NAME 'objectClasses' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.37 USAGE directoryOperation )
```

#### 4.2.2 'attributeTypes' attribute
```
( 2.5.21.5 NAME 'attributeTypes' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.3 USAGE directoryOperation )
```

#### 4.2.3 'matchingRules' attribute
```
( 2.5.21.4 NAME 'matchingRules' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.30 USAGE directoryOperation )
```

#### 4.2.4 'matchingRuleUse' attribute
```
( 2.5.21.8 NAME 'matchingRuleUse' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.31 USAGE directoryOperation )
```

#### 4.2.5 'ldapSyntaxes' attribute
```
( 1.3.6.1.4.1.1466.101.120.16 NAME 'ldapSyntaxes' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.54 USAGE directoryOperation )
```

#### 4.2.6 'dITContentRules' attribute
```
( 2.5.21.2 NAME 'dITContentRules' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.16 USAGE directoryOperation )
```

#### 4.2.7 'dITStructureRules' attribute
```
( 2.5.21.1 NAME 'dITStructureRules' EQUALITY integerFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.17 USAGE directoryOperation )
```

#### 4.2.8 'nameForms' attribute
```
( 2.5.21.7 NAME 'nameForms' EQUALITY objectIdentifierFirstComponentMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.35 USAGE directoryOperation )
```

### 4.3 'extensibleObject' object class
- Allows entries to hold any user attribute (userApplications usage).
```
( 1.3.6.1.4.1.1466.101.120.111 NAME 'extensibleObject' SUP top AUXILIARY )
```
- Mandatory attributes of other object classes still required; precluded attributes still not allowed.

### 4.4 Subschema Discovery
- Read the 'subschemaSubentry' attribute of an entry to get DN of controlling subschema.
- To read schema attributes, issue Search with baseObject=subschema DN, scope=baseObject, filter="(objectClass=subschema)", request desired schema attributes.
- "Clients SHOULD NOT assume that a published subschema is complete, that the server supports all of the schema elements it publishes, or that the server does not support an unpublished element."

## 5. DSA (Server) Informational Model
- Server holds a fragment of the DIT (naming contexts).
- Root DSE is a DSA-specific entry not part of any naming context.

### 5.1 Server-Specific Data Requirements
- "An LDAP server SHALL provide information about itself and other information that is specific to each server."
- Root DSE attributes: altServer, namingContexts, supportedControl, supportedExtension, supportedFeatures, supportedLDAPVersion, supportedSASLMechanisms.
- "The root DSE SHALL NOT be included if the client performs a subtree search starting from the root."
- Servers may allow modification of root DSE attributes where appropriate.

#### 5.1.1 'altServer'
```
( 1.3.6.1.4.1.1466.101.120.6 NAME 'altServer' SYNTAX 1.3.6.1.4.1.1466.115.121.1.26 USAGE dSAOperation )
```

#### 5.1.2 'namingContexts'
```
( 1.3.6.1.4.1.1466.101.120.5 NAME 'namingContexts' SYNTAX 1.3.6.1.4.1.1466.115.121.1.12 USAGE dSAOperation )
```

#### 5.1.3 'supportedControl'
```
( 1.3.6.1.4.1.1466.101.120.13 NAME 'supportedControl' SYNTAX 1.3.6.1.4.1.1466.115.121.1.38 USAGE dSAOperation )
```

#### 5.1.4 'supportedExtension'
```
( 1.3.6.1.4.1.1466.101.120.7 NAME 'supportedExtension' SYNTAX 1.3.6.1.4.1.1466.115.121.1.38 USAGE dSAOperation )
```

#### 5.1.5 'supportedFeatures'
```
( 1.3.6.1.4.1.4203.1.3.5 NAME 'supportedFeatures' EQUALITY objectIdentifierMatch SYNTAX 1.3.6.1.4.1.1466.115.121.1.38 USAGE dSAOperation )
```

#### 5.1.6 'supportedLDAPVersion'
```
( 1.3.6.1.4.1.1466.101.120.15 NAME 'supportedLDAPVersion' SYNTAX 1.3.6.1.4.1.1466.115.121.1.27 USAGE dSAOperation )
```

#### 5.1.7 'supportedSASLMechanisms'
```
( 1.3.6.1.4.1.1466.101.120.14 NAME 'supportedSASLMechanisms' SYNTAX 1.3.6.1.4.1.1466.115.121.1.15 USAGE dSAOperation )
```

## 6. Other Considerations
### 6.1 Preservation of User Information
- Syntaxes may have preservation requirements; if none stated, servers SHOULD preserve value but MAY return different form.
- "Where a server is unable (or unwilling) to preserve the value of user information, the server SHALL ensure that an equivalent value (per Section 2.3) is returned."

### 6.2 Short Names
- Short names are case-insensitive aliases for OIDs.
- "Implementations MUST be prepared that the same short name might be used in a subschema to refer to different kinds of schema elements."
- "Implementations MUST be prepared that the same short name might be used in different subschemas to refer to different schema elements."

### 6.3 Cache and Shadowing
- Servers that perform shadowing or caching "MUST ensure that they do not violate any access control constraints placed on the data by the originating server."

## 7. Implementation Guidelines
### 7.1 Server Guidelines
- "Servers MUST recognize all names of attribute types and object classes defined in this document but, unless stated otherwise, need not support the associated functionality."
- "Servers SHOULD recognize all the names of attribute types and object classes defined in Section 3 and 4, respectively, of [RFC4519]."
- "Servers MUST ensure that entries conform to user and system schema rules or other data model constraints."
- Servers MAY support DIT Content Rules, DIT Structure Rules, Name Forms, alias entries, 'extensibleObject', subentries.
- If subentries supported, "MUST do so in accordance with [RFC3672]."
- "Servers that do not support subentries SHOULD use object entries to mimic subentries as detailed in Section 3.2."
- "Servers SHOULD provide definitions of all schema elements they support in subschema (sub)entries."

### 7.2 Client Guidelines
- "Clients SHOULD NOT assume that servers support any particular schema elements beyond those referenced in Section 7.1."
- "Clients MUST NOT display or attempt to decode a value as ASN.1 if the value's syntax is not known."
- "Clients MUST NOT assume the LDAP-specific string encoding is restricted to a UTF-8 encoded string of Unicode characters or any particular subset of Unicode unless such restriction is explicitly stated."
- "Clients SHOULD NOT send attribute values in a request that are not valid according to the syntax defined for the attributes."

## 8. Security Considerations
- Privacy laws may apply to publication of personal information.
- General security considerations for LDAP are discussed in [RFC4511] and [RFC4513].

## 9. IANA Considerations
- IANA updated the LDAP descriptors registry as specified in the listing (see full text for complete table).

## 10. Acknowledgements
- Based on earlier work by M. Wahl, T. Howes, S. Kille, A. Coulbeck; product of LDAPBIS Working Group.

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Servers SHALL treat attribute description with unrecognized attribute option as unrecognized. | SHALL | Section 2.5 |
| R2 | An entry's relative distinguished name must be unique among all immediate subordinates. | must | Section 2.3.1 |
| R3 | The structural object class of an entry shall not be changed. | SHALL NOT | Section 2.4.2 |
| R4 | An alias entry shall have no subordinates. | SHALL | Section 2.6 |
| R5 | Every alias entry shall belong to the 'alias' object class. | SHALL | Section 2.6 |
| R6 | When creating an entry or adding an 'objectClass' value, all superclasses SHALL be implicitly added. | SHALL | Section 3.3 |
| R7 | Servers SHALL restrict modifications of 'objectClass' to prevent deletion of superclasses that are still needed. | SHALL | Section 3.3 |
| R8 | Servers that master entries and permit modifications SHALL implement and provide access to subschema (sub)entries. | SHALL | Section 4.2 |
| R9 | Servers SHOULD maintain creatorsName, createTimestamp, modifiersName, modifyTimestamp for all entries. | SHOULD | Section 3.4 |
| R10 | LDAP server SHALL provide information about itself in root DSE attributes. | SHALL | Section 5.1 |
| R11 | Servers MUST recognize all names of attribute types and object classes defined in this document. | MUST | Section 7.1 |
| R12 | Servers MUST ensure entries conform to schema rules. | MUST | Section 7.1 |
| R13 | Clients MUST NOT display or decode ASN.1 if syntax unknown. | MUST | Section 7.2 |
| R14 | Clients MUST NOT assume LDAP string encoding is restricted to UTF-8 subset unless explicitly stated. | MUST | Section 7.2 |
| R15 | Servers that shadow or cache MUST NOT violate access control constraints of originating server. | MUST | Section 6.3 |
| R16 | Servers SHOULD preserve user information value but MAY return different form; if unable, SHALL return equivalent value. | SHOULD/SHALL | Section 6.1 |

## Informative Annexes (Condensed)
- **Appendix A (Changes)**: Non-normative summary of changes made to RFC 2251, 2252, 2256, and 3674. Key clarifications include: alignment with X.500(93) for subschema, removal of ambiguous requirement for mandatory 'objectClasses' and 'attributeTypes' in subschema, clarification of root DSE attribute semantics, tightening of ABNF for OIDs, and updates to descriptor handling. No substantive technical changes were made to the 'supportedFeatures' from RFC 3674.