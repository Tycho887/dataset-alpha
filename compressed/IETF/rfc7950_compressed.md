# RFC 7950: The YANG 1.1 Data Modeling Language
**Source**: IETF | **Version**: Standards Track | **Date**: August 2016 | **Type**: Normative
**Original**: http://www.rfc-editor.org/info/rfc7950

## Scope (Summary)
YANG 1.1 is a data modeling language for configuration data, state data, Remote Procedure Calls, and notifications for network management protocols. This document defines YANG 1.1 syntax, semantics, and its mapping to the Network Configuration Protocol (NETCONF). It addresses ambiguities and defects in YANG 1 (RFC 6020) with some backward incompatibilities.

## Normative References
- [ISO.10646] ISO 10646:2014
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, 1997
- [RFC3629] Yergeau, F., "UTF-8, a transformation format of ISO 10646", STD 63, RFC 3629, 2003
- [RFC3986] Berners-Lee, T., et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, RFC 3986, 2005
- [RFC4648] Josefsson, S., "The Base16, Base32, and Base64 Data Encodings", RFC 4648, 2006
- [RFC5234] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", STD 68, RFC 5234, 2008
- [RFC5277] Chisholm, S. and H. Trevino, "NETCONF Event Notifications", RFC 5277, 2008
- [RFC6241] Enns, R., et al., "Network Configuration Protocol (NETCONF)", RFC 6241, 2011
- [RFC7405] Kyzivat, P., "Case-Sensitive String Support in ABNF", RFC 7405, 2014
- [RFC7895] Bierman, A., et al., "YANG Module Library", RFC 7895, 2016
- [XML] Bray, T., et al., "Extensible Markup Language (XML) 1.0 (Fifth Edition)", W3C REC, 2008
- [XML-NAMES] Bray, T., et al., "Namespaces in XML 1.0 (Third Edition)", W3C REC, 2009
- [XPATH] Clark, J. and S. DeRose, "XML Path Language (XPath) Version 1.0", W3C REC, 1999
- [XSD-TYPES] Biron, P. and A. Malhotra, "XML Schema Part 2: Datatypes Second Edition", W3C REC, 2004

## Definitions and Abbreviations
- **action**: An operation defined for a node in the data tree.
- **anydata**: A data node that can contain an unknown set of nodes that can be modeled by YANG, except anyxml.
- **anyxml**: A data node that can contain an unknown chunk of XML data.
- **augment**: Adds new schema nodes to a previously defined schema node.
- **base type**: The type from which a derived type was derived; may be built-in or derived.
- **built-in type**: A YANG data type defined in the YANG language (e.g., uint32, string).
- **choice**: A schema node where only one of a number of identified alternatives is valid.
- **client**: An entity that can access YANG-defined data on a server over a network management protocol.
- **conformance**: A measure of how accurately a server follows a data model.
- **container**: An interior data node that exists in at most one instance in the data tree; has a set of child nodes but no value.
- **data definition statement**: A statement that defines new data nodes (container, leaf, leaf-list, list, choice, case, augment, uses, anydata, anyxml).
- **data model**: Describes how data is represented and accessed.
- **data node**: A node in the schema tree that can be instantiated in a data tree (container, leaf, leaf-list, list, anydata, anyxml).
- **data tree**: An instantiated tree of any data modeled with YANG (configuration, state, RPCs, actions, notifications).
- **derived type**: A type derived from a built-in type or another derived type.
- **extension**: Attaches non-YANG semantics to statements; defined by the "extension" statement.
- **feature**: A mechanism for marking a portion of the model as optional; controlled by the server.
- **grouping**: A reusable set of schema nodes; the "grouping" statement is not a data definition statement.
- **identifier**: A string used to identify different kinds of YANG items by name.
- **identity**: A globally unique, abstract, and untyped name.
- **instance identifier**: A mechanism for identifying a particular node in a data tree.
- **interior node**: Nodes within a hierarchy that are not leaf nodes.
- **leaf**: A data node that exists in at most one instance in the data tree; has a value but no child nodes.
- **leaf-list**: Like leaf but defines a set of uniquely identifiable nodes; each has a value but no children.
- **list**: An interior data node that may exist in multiple instances; has no value but a set of child nodes.
- **mandatory node**: A leaf/choice/anydata/anyxml with mandatory true, or list/leaf-list with min-elements >0, or container without presence that has a mandatory child.
- **module**: A YANG module defines hierarchies of schema nodes; self-contained and "compilable".
- **non-presence container**: A container with no meaning of its own, existing only to contain child nodes.
- **presence container**: A container whose presence itself carries meaning.
- **RPC**: Remote Procedure Call.
- **RPC operation**: A specific Remote Procedure Call.
- **schema node**: A node in the schema tree (action, container, leaf, leaf-list, list, choice, case, rpc, input, output, notification, anydata, anyxml).
- **schema node identifier**: A mechanism for identifying a particular node in the schema tree.
- **schema tree**: The definition hierarchy within a module.
- **server**: An entity that provides access to YANG-defined data to a client.
- **server deviation**: A failure of the server to implement a module faithfully.
- **submodule**: A partial module definition that contributes to a module.
- **top-level data node**: A data node with no other data node between it and a "module" or "submodule" statement.
- **uses**: Instantiates the set of schema nodes defined in a "grouping" statement.
- **value space**: For a data type, the set of permitted values.
- **configuration data**, **configuration datastore**, **datastore**, **state data**: As defined in RFC 6241.

## 1. Introduction
YANG was originally designed for NETCONF (RFC 6241) but has been used for other protocols (RESTCONF, CoMI) and encodings (JSON). This document defines YANG 1.1, a maintenance release addressing ambiguities and defects in RFC 6020. It describes XML encoding and NETCONF operations for data modeled in YANG.

### 1.1. Summary of Changes from RFC 6020
**Backward-incompatible changes**:
- Changed escaped character interpretation in double-quoted strings. Modules using now-illegal sequences must change strings.
- Unquoted strings cannot contain single or double quotes. Modules using such quotes must change.
- "when" and "if-feature" illegal on list keys. Modules using these must remove them.
- Defined legal characters (Unicode minus C0 controls, surrogates, noncharacters). Illegal characters must be removed.
- Noncharacters illegal in built-in type "string". Affects runtime behavior.

**Other changes**:
- YANG version changed from "1" to "1.1". Yang-version statement mandatory for version 1.1.
- "if-feature" extended to boolean expressions over feature names.
- "if-feature" allowed in "bit", "enum", "identity".
- "if-feature" allowed in "refine".
- "choice" allowed as shorthand "case" statement.
- New substatement "modifier" for "pattern".
- "must" allowed in "input", "output", "notification".
- "require-instance" allowed in leafref.
- "description" and "reference" allowed in "import" and "include".
- Multiple revisions of a module may be imported.
- "augment" can add conditionally mandatory nodes.
- New XPath functions (Section 10).
- Clarified XPath context's tree.
- Defined string value of identityref in XPath.
- Clarified unprefixed names in leafrefs in typedefs.
- Identities can be derived from multiple base identities.
- Enumerations and bits can be subtyped.
- leaf-lists may have default values.
- Non-unique values allowed in non-configuration leaf-lists.
- Use case-sensitive strings in grammar (RFC 7405).
- Changed module advertisement mechanism (ietf-yang-library instead of <hello> capability).
- Changed scoping rules for submodules.
- New "action" statement for operations tied to data nodes.
- Notifications can be tied to data nodes.
- New "anydata" statement (recommended instead of "anyxml" when data can be modeled).
- Types "empty" and "leafref" allowed in unions.
- Type "empty" allowed in a key.
- Removed restriction that identifiers cannot start with "xml".

## 2. Key Words
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119].

## 3. Terminology
(Definitions as listed above.)

## 4. YANG Overview (Informative)
Provides a high-level overview. See Sections 4.1 and 4.2 for functional and language overviews. Notable:
- YANG modules define hierarchical data trees.
- Modules can import and include other modules.
- Built-in types: binary, bits, boolean, decimal64, empty, enumeration, identityref, instance-identifier, int8/16/32/64, leafref, string, uint8/16/32/64, union.
- Derived types via typedef.
- Reusable node groups via grouping.
- Choices with cases.
- Augment extends data models.
- RPC and action definitions.
- Notification definitions.

## 5. Language Concepts
### 5.1. Modules and Submodules
- A module is the base unit; defines a single data model.
- Submodules contribute to a module; a module may include multiple submodules.
- Module names SHOULD have low collision probability. Within a server, all module names MUST be unique.
- Modules use "include" for submodules, "import" for external modules.
- No circular imports allowed.
- References to external definitions use prefix notation.
- Import and include can be by revision.

### 5.2. File Layout
- Files named `module-or-submodule-name [@revision-date] ( .yang | .yin )`.

### 5.3. XML Namespaces
- Each module bound to a distinct XML namespace (URI).
- Namespaces for RFC stream modules assigned by IANA; private modules must avoid collision.

### 5.4. Resolving Grouping, Type, and Identity Names
- Resolved in the context where defined (static scoping), not where used.

### 5.5. Nested Typedefs and Groupings
- Allowed; lexically scoped. Scoped definitions MUST NOT shadow higher-level definitions.

### 5.6. Conformance
#### 5.6.1. Basic Behavior
- Model defines contract between client and server.

#### 5.6.2. Optional Features
- "feature" and "if-feature" make parts conditional on server support.

#### 5.6.3. Deviations
- "deviation" statement documents how server deviates from the module.

#### 5.6.4. Announcing Conformance Information in NETCONF
- Server MUST implement ietf-yang-library (RFC 7895) and advertise capability `urn:ietf:params:netconf:capability:yang-library:1.0`.

#### 5.6.5. Implementing a Module
- Server implements a module if it implements its data nodes, RPCs, actions, notifications, deviations.
- Must not implement more than one revision of a module.
- If module A imports module B and uses nodes from B in augment/path, server must implement a revision of B with those nodes.

### 5.7. Datastore Modification (Informative)
- Models may allow server to alter datastore in ways not explicitly directed (e.g., system-generated values). Formal mechanism out of scope.

## 6. YANG Syntax
### 6.1. Lexical Tokenization
#### 6.1.1. Comments
- C++ style: `//` single line, `/* ... */` block. Not recognized inside quoted strings.

#### 6.1.2. Tokens
- A token is keyword, string, `;`, `{`, `}`.

#### 6.1.3. Quoting
- **Unquoted string**: no space, tab, CR, LF, quotes, `;`, `{`, `}`, comment sequences.
- **Double-quoted string**: supports `\n`, `\t`, `\"`, `\\`. Leading whitespace (to column of opening quote) stripped; trailing whitespace stripped before line break. Concatenation via `+`.
- **Single-quoted string**: everything literal; no single quote inside.
- Backslash only special in double-quoted strings.

### 6.2. Identifiers
- Start with letter or underscore, followed by letters, digits, underscore, hyphen, dot. Case sensitive. Max 64 characters recommended.

#### 6.2.1. Identifiers and Their Namespaces
- Various namespaces: module/submodule global; extensions, features, identities per module; typedefs/groupings scoped; data nodes (leaf, leaf-list, list, container, choice, rpc, action, notification, anydata, anyxml) scoped; cases scoped to parent choice.

### 6.3. Statements
- `statement = keyword [argument] (";" / "{" *statement "}")`.

#### 6.3.1. Language Extensions
- Extensions defined with "extension" keyword; imported modules use prefix. Unsupported extensions may be ignored.

### 6.4. XPath Evaluations
- YANG uses XPath 1.0 for inter-node references. Implementation must enforce requirements, not necessarily interpret XPath.
- Numbers are double-precision; caution with 64-bit values.

#### 6.4.1. XPath Context
- Namespace declarations from imports and module's own prefix.
- Unprefixed names belong to namespace of current node (affected by grouping/typedef usage).
- Function library includes core XPath and functions from Section 10.
- Variable bindings empty.
- Accessible tree depends on context (configuration, state, notification, input, output). Default values in use exist.

### 6.5. Schema Node Identifier
- Absolute or descendant path of identifiers separated by `/`. External references must use prefix.

## 7. YANG Statements
### 7.1. The "module" Statement
- Define module name, header info (yang-version, namespace, prefix), linkage (import, include), meta (organization, contact, description, reference), revision, definitions.

#### 7.1.2. The "yang-version" Statement
- Argument MUST be "1.1" for this version. Absent or "1" means YANG version 1.

#### 7.1.3. The "namespace" Statement
- URI defining XML namespace for identifiers.

#### 7.1.4. The "prefix" Statement
- Prefix string used to reference the module.

#### 7.1.5. The "import" Statement
- Makes definitions from another module available. Mandatory prefix substatement. Optional revision-date. Multiple revisions allowed with different prefixes.

#### 7.1.6. The "include" Statement
- Includes a submodule belonging to the same module. Optional revision-date.

#### 7.1.7. The "organization" Statement
- Textual description of responsible party.

#### 7.1.8. The "contact" Statement
- Contact information.

#### 7.1.9. The "revision" Statement
- Date in YYYY-MM-DD format; records editorial history. SHOULD have at least one.

### 7.2. The "submodule" Statement
- Defines a submodule; includes belongs-to statement.

### 7.3. The "typedef" Statement
- Defines a derived type. Must have a "type" substatement; optional default, units, etc.

### 7.4. The "type" Statement
- Name of a built-in or derived type, with optional restrictions.

### 7.5. The "container" Statement
- Interior data node. Two styles: non-presence (no meaning) and presence (meaning indicated by "presence" statement).
- Substatements include must, presence, child node definitions (leaf, leaf-list, list, container, etc.).
- XML encoding: container as element, child nodes as subelements (order matters for RPC/action input/output, else any order).
- NETCONF edit-config: can create, delete, replace, modify. Non-presence container may be deleted when last child removed.

### 7.6. The "leaf" Statement
- Scalar variable. Substatements: type, default, mandatory, etc.
- Default value in use depends on ancestor node existence.
- XML: element with leaf name, value as character data.
- edit-config: merge/replace creates/updates; create creates; delete deletes.

### 7.7. The "leaf-list" Statement
- Array of values. In config, values MUST be unique.
- Ordering: system or user (ordered-by).
- Default values: multiple default statements allowed; used if leaf-list absent and ancestor exists.
- Substatements: type, default, min-elements, max-elements, ordered-by, etc.
- XML: series of elements with same local name. Order as per user if ordered-by user.
- edit-config: create, delete entries; insert attribute for ordered-by user.

### 7.8. The "list" Statement
- Interior data node with multiple instances. Key leafs uniquely identify entries.
- Substatements: key, unique, child node definitions.
- key must be present for configuration. Key leafs must have same config as list.
- unique constraint: combined values of specified leafs unique across entries.
- XML: each entry as element with key leafs first.
- edit-config: create, delete, replace, modify entries; insert and key attributes for ordered-by user.

### 7.9. The "choice" Statement
- Set of alternatives; only one case valid at a time.
- Substatements: case (or shorthand), default, mandatory, etc.
- default case used when no child nodes from any case exist. Mandatory: at least one node from one case must exist.
- XML: choice and case not visible; child nodes of selected case encoded.

### 7.10. The "anydata" Statement
- Unknown set of nodes that can be modeled with YANG (except anyxml). SHOULD NOT be used for configuration.
- Substatements: config, mandatory, must, etc.
- XML: element containing subelements.
- edit-config: treated as opaque; only whole replacement.

### 7.11. The "anyxml" Statement
- Unknown XML chunk. SHOULD NOT be used for config; RECOMMENDED to use anydata if applicable.
- XML: element containing any XML.
- edit-config: opaque.

### 7.12. The "grouping" Statement
- Reusable block of nodes. Not a data definition statement. Self-references not allowed.

### 7.13. The "uses" Statement
- References a grouping. Identifiers bound to namespace of current module when used outside grouping.
- Substatements: refine, augment, when, if-feature.
- refine can modify properties of nodes in grouping (defaults, description, config, mandatory, must, etc.).

### 7.14. The "rpc" Statement
- Defines an RPC operation. May have input and output.
- input/output have data definition substatements. Mandatory leaves must be present; default values used if applicable.
- XML: rpc element as child of <rpc>; input children in order; output children in order in <rpc-reply>.

### 7.15. The "action" Statement
- Defines operation tied to a specific container or list data node.
- Similar to rpc but bound to datastore node. Action must not have rpc/action/notification as ancestor; must not have ancestor list without key.
- XML: <action> element containing path to data node and action input.

### 7.16. The "notification" Statement
- Defines a notification. Can be top-level or tied to data node.
- Must not have rpc/action/notification as ancestor; must not have ancestor list without key.
- XML: top-level or nested in data tree hierarchy as child of <notification>.

### 7.17. The "augment" Statement
- Adds nodes to a target node (container, list, choice, case, input, output, notification). Target must not be choice if adding cases to a choice? Actually target can be choice, then case statements are added.
- Must not add multiple nodes with same name from same module.
- If augmentation adds mandatory config nodes, must be conditional with "when".

### 7.18. The "identity" Statement
- Defines an abstract identity. Can derive from one or more base identities.
- Substatements: base, description, etc.
- Derivation must not be circular.

### 7.19. The "extension" Statement
- Defines new statement keyword. Argument optional. Substatements define usage.

### 7.20. Conformance-Related Statements
#### 7.20.1. The "feature" Statement
- Defines a feature name. May depend on other features via if-feature. Self-references not allowed.

#### 7.20.2. The "if-feature" Statement
- Boolean expression over feature names. Parent statement only implemented if expression true. Precedence: parentheses, not, and, or.

#### 7.20.3. The "deviation" Statement
- Documents server deviation. Substatements: deviate (not-supported, add, replace, delete). Deviations must not be part of published standard.

### 7.21. Common Statements
- **config**: true (configuration) or false (state data). Default inherited from parent.
- **status**: current, deprecated, or obsolete.
- **description**: human-readable text.
- **reference**: cross-reference to external document.
- **when**: XPath expression making node conditional.

## 8. Constraints
- Various constraints on data (type, key, choice, if-feature, when, must, path, unique, mandatory, min/max-elements). Enforcement depends on data type (config, state, notification, RPC input/output).
- NETCONF constraint enforcement: payload parsing, edit-config processing, validation.

## 9. Built-In Types
(Detailed in sections 9.2-9.13) Each type has lexical representation, canonical form if applicable, and restrictions.

## 10. XPath Functions
- **current()**: returns context node.
- **re-match()**: boolean regex match.
- **deref()**: follows leafref/instance-identifier reference.
- **derived-from()** and **derived-from-or-self()**: check identity derivation.
- **enum-value()**: returns integer value of enumeration.
- **bit-is-set()**: checks if a particular bit is set.

## 11. Updating a Module
- Changes must not cause interoperability problems. Revisions must be added. Certain changes allowed (adding enums, expanding ranges, etc.). Non-editorial changes require new identifier.

## 12. Coexistence with YANG Version 1
- A YANG 1.1 module must not include a YANG 1 submodule and vice versa. A YANG 1 module must not import a YANG 1.1 module by revision. A YANG 1.1 module may import a YANG 1 module by revision. If a YANG 1 module imports a module that is updated to YANG 1.1, the server may implement both and should advertise the YANG 1 version.

## 13. YIN
- XML-based syntax equivalent to YANG. One-to-one mapping of keywords to elements. Argument mapping defined in Table 1. Extensions have their own namespace.

## 14. YANG ABNF Grammar
Full ABNF provided in document.

## 15. NETCONF Error Responses for YANG-Related Errors
- Unique constraint violation: error-tag `operation-failed`, error-app-tag `data-not-unique`.
- Max-elements: `too-many-elements`.
- Min-elements: `too-few-elements`.
- Must violation: `must-violation`.
- Require-instance: `data-missing`, `instance-required`.
- Mandatory choice: `data-missing`, `missing-choice`.
- Insert operation: `bad-attribute`, `missing-instance`.

## 16. IANA Considerations
- Registered capability URN: `urn:ietf:params:netconf:capability:yang-library:1.0`.

## 17. Security Considerations
- Language itself has no security impact. Data modeled may contain sensitive information; security depends on transmission, storage, access control. YANG parsers must be robust against malformed documents.

## 18. References
(Normative and informative as listed.)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | All module names MUST be unique within a server. | MUST | Section 5.1 |
| R2 | A server MUST NOT implement more than one revision of a module. | MUST | Section 5.6.5 |
| R3 | The "mandatory" constraint is enforced for leafs and choices, unless the node or any of its ancestors has a "when" condition or "if-feature" expression that evaluates to "false". | MUST | Section 8.1 |
| R4 | The "min-elements" and "max-elements" constraints are enforced for lists and leaf-lists, unless the node or any of its ancestors has a "when" condition or "if-feature" expression that evaluates to "false". | MUST | Section 8.1 |
| R5 | When a server sends XML-encoded data, it MUST use the canonical form defined for each type. | MUST | Section 9.1 |
| R6 | If the augmentation adds mandatory nodes that represent configuration, the augmentation MUST be made conditional with a "when" statement. | MUST | Section 7.17 |
| R7 | The "require-instance" property, if true, requires the referred instance to exist. | MUST | Section 9.9.3 |
| R8 | A leaf that is a list key MUST NOT have any "if-feature" statements. | MUST | Section 7.20.2 |
| R9 | A leaf that is a list key MUST NOT have a "when" statement. | MUST | Section 7.21.5 |
| R10 | All "must" constraints MUST evaluate to "true" in a valid data tree. | MUST | Section 8.1 |

## Informative Annexes (Condensed)
- **Section 3.1 A Note on Examples**: Examples illustrate features and are not complete valid YANG modules.
- **Section 4 YANG Overview**: Provides functional overview, language overview including modules, data modeling basics, configuration/state data, built-in types, derived types, groupings, choices, augment, operations, notifications.
- **Section 5.7 Datastore Modification**: Models may allow server to alter datastore; formal mechanism out of scope.
- **Section 6.4 XPath Evaluations**: Notes on XPath number precision.
- **Section 6.4.1.1 Examples**: Shows accessible trees for notifications and actions.
- **Section 7.5.4.3 Usage Example of must and error-message**: Example with interface MTU constraints.
- **Section 7.5.9 Usage Example**: Container presence example.
- **Section 7.6.8 Usage Example**: Leaf default and edit-config.
- **Section 7.7.10 Usage Example**: leaf-list with ordered-by user insertion.
- **Section 7.8.7 Usage Example**: List with key and edit-config operations.
- **Section 7.9.6 Usage Example**: Choice and protocol change.
- **Section 7.10.4 Usage Example**: anydata for logged notifications.
- **Section 7.11.4 Usage Example**: anyxml with HTML.
- **Section 7.12.2 Usage Example**: grouping endpoint.
- **Section 7.13.4 Usage Example**: uses with refine.
- **Section 7.14.5 Usage Example**: rpc rock-the-house.
- **Section 7.15.3 Usage Example**: action reset on server list.
- **Section 7.16.3 Usage Example**: notification event and interface-enabled.
- **Section 7.17.3 Usage Example**: augment interface with ds0.
- **Section 7.18.3 Usage Example**: identity derivation for crypto.
- **Section 7.19.3 Usage Example**: extension c-define.
- **Section 7.20.2.1 Usage Example**: if-feature expression.
- **Section 7.20.3.3 Usage Example**: deviation.
- **Section 9.2.5 Usage Example**: integer range restrictions.
- **Section 9.3.5 Usage Example**: decimal64.
- **Section 9.4.7 Usage Example**: string length and pattern.
- **Section 9.6.5 Usage Example**: enum.
- **Section 9.7.5 Usage Example**: bits.
- **Section 9.9.6 Usage Example**: leafref.
- **Section 9.10.5 Usage Example**: identityref.
- **Section 9.11.4 Usage Example**: empty.
- **Section 9.12.4 Usage Example**: union with leafref and enumeration.
- **Section 9.13.4 Usage Example**: instance-identifier.
- **Section 10.1.1.1 Usage Example**: current() in must.
- **Section 10.2.1.1 Usage Example**: re-match().
- **Section 10.3.1.1 Usage Example**: deref().
- **Section 10.4.1.1 Usage Example**: derived-from().
- **Section 10.4.2.1 Usage Example**: derived-from-or-self().
- **Section 10.5.1.1 Usage Example**: enum-value().
- **Section 10.6.1.1 Usage Example**: bit-is-set().