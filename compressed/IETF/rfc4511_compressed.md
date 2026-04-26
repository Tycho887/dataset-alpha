# RFC 4511: Lightweight Directory Access Protocol (LDAP): The Protocol
**Source**: IETF | **Version**: Standards Track (obsoletes RFC 2251, 2830, 3771) | **Date**: June 2006 | **Type**: Normative  
**Original**: [https://tools.ietf.org/html/rfc4511](https://tools.ietf.org/html/rfc4511)

## Scope (Summary)
Defines LDAP version 3 protocol elements, semantics, and encodings (ASN.1/BER) for distributed directory access conforming to X.500 data and service models. Provides operations: Bind, Unbind, Search, Modify, Add, Delete, Modify DN, Compare, Abandon, Extended, and StartTLS.

## Normative References (Selected)
- [RFC2119] – Key words (MUST, SHOULD, etc.)
- [RFC3629] – UTF-8
- [RFC3986] – URI syntax
- [RFC4234] – ABNF
- [RFC4422] – SASL
- [RFC4510] – LDAP Technical Specification Road Map
- [RFC4512] – Directory Information Models
- [RFC4513] – Authentication Methods and Security Mechanisms
- [RFC4514] – String Representation of DNs
- [RFC4516] – LDAP URL
- [RFC4517] – Syntaxes and Matching Rules
- [RFC4520] – IANA Considerations
- [ASN.1] – X.680
- [BER] – X.690
- [ISO10646] / [Unicode]
- [X.500] / [X.511]
(*Full list in Section 8 of the original*)

## Definitions and Abbreviations (Selected)
- **transport connection**: underlying carrier (e.g., TCP).
- **TLS layer**: TLS security services and associations.
- **SASL layer**: SASL security services and associations.
- **LDAP message layer**: LDAP PDU services.
- **LDAP session**: combined transport, TLS, SASL, and message layer.
- **LDAPMessage**: envelope with `messageID` (INTEGER 0..2³¹⁻¹) and `protocolOp`.
- **LDAPString**: UTF-8 encoded OCTET STRING.
- **LDAPOID**: numeric OID (per RFC4512).
- **LDAPDN**: Distinguished Name per RFC4514.
- **RelativeLDAPDN**: RDN per RFC4514.
- **AttributeDescription**: per RFC4512 §2.5.
- **AttributeValue**: OCTET STRING (no size limit).
- **LDAPResult**: structure with resultCode, matchedDN, diagnosticMessage, referral.
- **Control**: OID + criticality (default FALSE) + optional value.

## 1. Introduction
LDAP provides access to the Directory (X.500). Clients interact with servers via LDAP protocol. This document defines protocol elements, their semantics, and encoding. Together with [RFC4510], [RFC4513], [RFC4512] it obsoletes RFC2251, RFC2830, and RFC3771.

## 2. Conventions
The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY** are as per RFC2119. Additional definitions for transport connection, TLS layer, SASL layer, LDAP message layer, LDAP session.

## 3. Protocol Model
Clients perform operations against servers. Operations are atomic and independent. No synchronous behavior required. Requests and responses may be interleaved arbitrarily. The core operations map to X.500 abstract service but not one-to-one.

### 3.1 Operation and LDAP Message Layer Relationship
- When transport connection is closed, uncompleted operations are abandoned (if possible) or completed without response.
- **Client MUST NOT** assume any uncompleted update operations have succeeded or failed.

## 4. Elements of Protocol
Protocol described in ASN.1; transferred using BER subset. Extensibility implied per ASN.1; ellipses mark explicit extensible types. **Clients and servers MUST (unless otherwise specified) ignore trailing SEQUENCE components with unrecognized tags.**  
If a client has not sent a Bind, **server MUST assume** client uses version 3 or later. Clients may discover supported versions via `supportedLDAPVersion` attribute in root DSE.

### 4.1 Common Elements
#### 4.1.1 Message Envelope (LDAPMessage)
```
LDAPMessage ::= SEQUENCE {
    messageID       MessageID,
    protocolOp      CHOICE { ... types for all operations ... },
    controls       [0] Controls OPTIONAL
}
MessageID ::= INTEGER (0..maxInt)
maxInt INTEGER ::= 2147483647
```
- If server receives an LDAPMessage with unrecognizable SEQUENCE tag, cannot parse messageID, unrecognized request op tag, or incorrect encoding/structure: **server SHOULD** return Notice of Disconnection with resultCode `protocolError`, and **MUST** immediately terminate LDAP session (§5.3).
- In other parsing failure cases: **SHOULD** abruptly terminate session if further communication is pernicious; otherwise **server MUST** return appropriate response with `protocolError`.

##### 4.1.1.1 MessageID
- Responses contain `messageID` of corresponding request.
- **Request messageID MUST be non-zero** and unique among in-progress requests in the same LDAP session.
- Zero is reserved for unsolicited notification.
- **Client MUST NOT** reuse a messageID unless it can be determined the server is no longer servicing the earlier request (e.g., after final response or subsequent Bind completes).
- Abandon and successfully abandoned operations do not send responses.

#### 4.1.2 String Types
- `LDAPString`: UTF-8 encoded OCTET STRING.
- `LDAPOID`: constrained to `<numericoid>` per RFC4512.

#### 4.1.3 Distinguished Name and Relative Distinguished Name
- `LDAPDN`: DN per RFC4514.
- `RelativeLDAPDN`: RDN per RFC4514.

#### 4.1.4 Attribute Descriptions
- `AttributeDescription`: per RFC4512 §2.5.

#### 4.1.5 Attribute Value
- `AttributeValue ::= OCTET STRING` – no size limit.
- Values may be arbitrary binary; **implementations MUST NOT** display/decode unknown syntax.
- **Clients MUST** only send attribute values valid per defined syntax.

#### 4.1.6 Attribute Value Assertion
```
AttributeValueAssertion ::= SEQUENCE {
    attributeDesc   AttributeDescription,
    assertionValue  AssertionValue
}
AssertionValue ::= OCTET STRING
```

#### 4.1.7 Attribute and PartialAttribute
```
PartialAttribute ::= SEQUENCE {
    type       AttributeDescription,
    vals       SET OF value AttributeValue
}
Attribute ::= PartialAttribute(WITH COMPONENTS { ..., vals (SIZE(1..MAX))})
```
- No two values may be equivalent per RFC4512 §2.2.
- Unordered; **implementations MUST NOT** rely on ordering repeatability.

#### 4.1.8 Matching Rule Identifier
- `MatchingRuleId ::= LDAPString` – e.g., `'caseIgnoreMatch'` or `'2.5.13.2'`.

#### 4.1.9 LDAPResult
```
LDAPResult ::= SEQUENCE {
    resultCode         ENUMERATED { ... (0..80, extensible) },
    matchedDN          LDAPDN,
    diagnosticMessage  LDAPString,
    referral           [3] Referral OPTIONAL
}
```
- `resultCode` enumeration extensible per RFC4520.
- `diagnosticMessage`: optional, human-readable; **MUST be empty** if server chooses not to return text.
- `matchedDN`: set for certain result codes (typically noSuchObject, aliasProblem, etc.) to name of last entry used in resolution; otherwise empty.

#### 4.1.10 Referral
- Returned when resultCode is `referral`; contains one or more URIs (**at least one MUST be present**).
- **Clients that follow referrals MUST ensure** they do not loop; **MUST NOT** repeatedly contact same server with same parameters; **MUST handle at least ten nested referrals**.
- LDAP URL rules:
  - If alias dereferenced, `<dn>` **MUST** be present.
  - `<dn>` recommended to avoid ambiguity.
  - `<filter>` may be provided to change filter.
  - `<scope>` recommended; if absent, original scope used.
- Other URI types allowed; clients may ignore unsupported.

#### 4.1.11 Controls
```
Control ::= SEQUENCE {
    controlType             LDAPOID,
    criticality             BOOLEAN DEFAULT FALSE,
    controlValue            OCTET STRING OPTIONAL
}
```
- Criticality only meaningful on request messages (except UnbindRequest).
- **If criticality TRUE and control not recognized or inappropriate**:
  - **Server MUST NOT** perform operation.
  - **Must return** resultCode `unavailableCriticalExtension` (if operation has response).
- **If criticality FALSE**: **server MUST ignore** the control.
- Regardless of criticality, control applied consistently to entire operation.
- **Implementations MUST** be prepared for arbitrary `controlValue` content.
- **Controls SHOULD NOT** be combined unless semantics specified; else message is not well-formed → `protocolError`.
- Controls with criticality FALSE may be ignored to achieve valid combination.
- Order of controls in SEQUENCE ignored unless order-dependent semantics given; otherwise `protocolError`.

### 4.2 Bind Operation
**Purpose**: authenticate. Semantics detailed in RFC4513.
```
BindRequest ::= [APPLICATION 0] SEQUENCE {
    version                 INTEGER (1..127),
    name                    LDAPDN,
    authentication          AuthenticationChoice
}
AuthenticationChoice ::= CHOICE { simple [0] OCTET STRING, sasl [3] SaslCredentials, ... }
SaslCredentials ::= SEQUENCE { mechanism LDAPString, credentials OCTET STRING OPTIONAL }
```
- `version`: client sets to desired version. If server does not support it, **MUST** respond with `protocolError`.
- `name`: may be empty for anonymous bind or SASL. **Server SHALL NOT** perform alias dereferencing.
- **Textual passwords** transferred using `simple` **SHALL** be UTF-8 encoded; **SHOULD** be SASLprep'ed. Non-textual (random) passwords **MUST NOT** be altered.

#### 4.2.1 Processing of Bind Request
- Before processing Bind, all uncompleted operations **MUST** either complete or be abandoned (server may wait or abandon).
- After sending BindRequest, **clients MUST NOT** send further LDAP PDUs until receiving BindResponse.
- **Servers SHOULD NOT** process/respond to requests received while processing a BindRequest.
- Clients may send multiple Binds; earlier authentication is overridden.
- Multi-stage SASL: **clients MUST NOT** invoke operations between Bind requests of the multi-stage bind.
- Client may abort SASL by sending different mechanism or non-sasl choice.
- If `sasl` mechanism field is empty string: **server MUST** return `authMethodNotSupported`.

#### 4.2.2 Bind Response
```
BindResponse ::= [APPLICATION 1] SEQUENCE {
    COMPONENTS OF LDAPResult,
    serverSaslCreds    [7] OCTET STRING OPTIONAL
}
```
- `protocolError` may indicate unsupported version.
- `serverSaslCreds` **SHALL NOT** be included if simple choice or SASL mechanism does not require server credentials.

### 4.3 Unbind Operation
**Purpose**: terminate LDAP session.
```
UnbindRequest ::= [APPLICATION 2] NULL
```
- Upon transmission (client) or receipt (server), gracefully terminate LDAP session per §5.3.
- Uncompleted operations handled as per §3.1.

### 4.4 Unsolicited Notification
- LDAPMessage with `messageID = 0` and `protocolOp = ExtendedResponse`.
- **Notice of Disconnection**: responseName = `1.3.6.1.4.1.1466.20036`, no responseValue, resultCode indicates reason.
- Used to advise client of impending session termination.
- On transmission, server gracefully terminates LDAP session.

### 4.5 Search Operation
#### 4.5.1 Search Request
```
SearchRequest ::= [APPLICATION 3] SEQUENCE {
    baseObject      LDAPDN,
    scope           ENUMERATED { baseObject(0), singleLevel(1), wholeSubtree(2), ... },
    derefAliases    ENUMERATED { neverDerefAliases(0), derefInSearching(1), derefFindingBaseObj(2), derefAlways(3) },
    sizeLimit       INTEGER (0..maxInt),
    timeLimit       INTEGER (0..maxInt),
    typesOnly       BOOLEAN,
    filter          Filter,
    attributes      AttributeSelection
}
Filter ::= CHOICE { and, or, not, equalityMatch, substrings, greaterOrEqual, lessOrEqual, present, approxMatch, extensibleMatch, ... }
```
- `scope` semantics: baseObject, singleLevel (immediate subordinates), wholeSubtree (entry and all subordinates).
- `derefAliases`: defined values for alias handling during search.
- `sizeLimit`: zero means no client limit; servers may enforce maximum.
- `timeLimit`: zero means no client limit; servers may enforce maximum.
- `typesOnly`: TRUE → only attribute descriptions returned; FALSE → both descriptions and values.
- **Filter evaluation**: three-valued logic (TRUE, FALSE, Undefined) per X.511.
- **Server MUST NOT** return errors for unrecognized attribute descriptions, invalid assertion values, or unsupported matching rules; evaluate to Undefined.
- Filters: `and`, `or`, `not` combine; items match attribute values.
- SubstringFilter: `initial`, `any`, `final`; at most one initial and one final; initial first, final last.
- ExtensibleMatch: rules for matching rule, type, dnAttributes.

##### Attributes Selection (SearchRequest.attributes)
- `attributeSelector = attributedescription / noattrs (“1.1”) / alluserattrs (“*”)`
- Empty list → return all user attributes.
- List containing `*` → all user attributes plus listed operational attributes.
- List with only `“1.1”` → no attributes returned.
- Attributes returned at most once; duplicates ignored; unrecognized attribute descriptions ignored.

#### 4.5.2 Search Result
- Zero or more `SearchResultEntry` and/or `SearchResultReference`, then one `SearchResultDone`.
- `SearchResultEntry` contains objectName and PartialAttributeList (may be empty).
- Server **SHOULD** use short names if unambiguous; **SHOULD NOT** use if ambiguous or likely to cause problems.
- Constructed attributes may appear; clients **SHOULD NOT** assume all can be modified.

#### 4.5.3 Continuation References in Search Result
- Server may return `SearchResultReference` if baseObject found but unable to search non-local entries.
- **MUST NOT** return such references if baseObject not located.
- **Clients following references MUST ensure** no loops; **MUST handle at least ten nested references**.
- LDAP URL rules: `<dn>` **MUST** be present; `<filter>` may differ; `<scope>` recommended.
- Abandon applies only to a particular operation; client must individually abandon subsequent searches.

### 4.6 Modify Operation
```
ModifyRequest ::= [APPLICATION 6] SEQUENCE {
    object          LDAPDN,
    changes         SEQUENCE OF change SEQUENCE {
        operation       ENUMERATED { add(0), delete(1), replace(2), ... },
        modification    PartialAttribute
    }
}
ModifyResponse ::= [APPLICATION 7] LDAPResult
```
- **Server SHALL NOT** perform alias dereferencing.
- Changes **MUST** be applied atomically in order.
- Resulting entry **MUST** conform to schema.
- `add`: add values, create attribute if necessary.
- `delete`: delete listed values; if no values or all values listed, attribute removed.
- `replace`: replace existing values with new; if no values, delete attribute if exists, ignored if not.
- **Servers MUST** ensure conformance to schema; cannot remove distinguished values (return `notAllowedOnRDN`).

### 4.7 Add Operation
```
AddRequest ::= [APPLICATION 8] SEQUENCE {
    entry           LDAPDN,
    attributes      AttributeList
}
AddResponse ::= [APPLICATION 9] LDAPResult
```
- **Server SHALL NOT** dereference aliases.
- RDN attributes may be included or not; **MUST NOT** supply NO-USER-MODIFICATION attributes.
- Parent **MUST** exist.
- Entry **MUST NOT** already exist.

### 4.8 Delete Operation
```
DelRequest ::= [APPLICATION 10] LDAPDN
DelResponse ::= [APPLICATION 11] LDAPResult
```
- Only leaf entries (no subordinates) can be deleted.
- **Server SHALL NOT** dereference aliases.

### 4.9 Modify DN Operation
```
ModifyDNRequest ::= [APPLICATION 12] SEQUENCE {
    entry           LDAPDN,
    newrdn          RelativeLDAPDN,
    deleteoldrdn    BOOLEAN,
    newSuperior     [0] LDAPDN OPTIONAL
}
ModifyDNResponse ::= [APPLICATION 13] LDAPResult
```
- **Server SHALL NOT** dereference aliases.
- If `deleteoldrdn` TRUE: old RDN values deleted; FALSE: retained as non-distinguished values.
- `newSuperior` if present: names an existing object that becomes new parent.
- New RDN values not matching existing are added; error if fails.
- X.500 may restrict to single server; `affectsMultipleDSAs` may be returned.

### 4.10 Compare Operation
```
CompareRequest ::= [APPLICATION 14] SEQUENCE {
    entry           LDAPDN,
    ava             AttributeValueAssertion
}
CompareResponse ::= [APPLICATION 15] LDAPResult
```
- **Server SHALL NOT** dereference aliases.
- `compareTrue` if assertion value matches a value per EQUALITY matching rule; `compareFalse` otherwise.

### 4.11 Abandon Operation
```
AbandonRequest ::= [APPLICATION 16] MessageID
```
- No response defined.
- Server **MAY** abandon the operation identified by MessageID.
- For Search in progress: **server MUST** cease transmitting entry responses immediately; **MUST NOT** send SearchResultDone.
- Cannot abandon Bind, Unbind, StartTLS.
- **Servers MUST discard** Abandon requests for unknown messageIDs, non-abandonable operations, or already abandoned operations.
- Clients **MUST** be prepared to receive results from abandoned operations.

### 4.12 Extended Operation
```
ExtendedRequest ::= [APPLICATION 23] SEQUENCE {
    requestName      [0] LDAPOID,
    requestValue     [1] OCTET STRING OPTIONAL
}
ExtendedResponse ::= [APPLICATION 24] SEQUENCE {
    COMPONENTS OF LDAPResult,
    responseName     [10] LDAPOID OPTIONAL,
    responseValue    [11] OCTET STRING OPTIONAL
}
```
- If `requestName` not recognized: server returns `protocolError`.
- `responseName` optional; absent when server cannot determine appropriate OID.
- **Implementations MUST** be prepared for arbitrary contents of `requestValue` / `responseValue`.
- Server advertises supported extensions in `supportedExtension` attribute.

### 4.13 IntermediateResponse Message
```
IntermediateResponse ::= [APPLICATION 25] SEQUENCE {
    responseName     [0] LDAPOID OPTIONAL,
    responseValue    [1] OCTET STRING OPTIONAL
}
```
- **SHALL NOT** be returned unless client solicits via Extended operation or request control.
- When used with request controls, `responseName` **SHALL** be present.
- Used to define single-request/multiple-response operations.

### 4.14 StartTLS Operation
- Extended operation: requestName `1.3.6.1.4.1.1466.20037`, requestValue absent.
- **Client MUST NOT** send any LDAP PDUs after this request until it receives response and completes TLS negotiation.
- If server does not support TLS: returns `protocolError`.
- Successful response: resultCode `success`; then TLS negotiation commences.
- Failure: appropriate resultCode; session remains without TLS.
- Removal of TLS: either peer may send TLS closure alert; must wait for closure alert before further LDAP PDUs.

## 5. Protocol Encoding, Connection, and Transfer
- Runs over connection-oriented reliable transport.
- **LDAP over TCP MUST** follow the mapping in §5.2.
- Encoding: BER with restrictions: definite length only, primitive OCTET STRING, BOOLEAN true = 0xFF, default values omitted.
- TCP port 389 (IANA).
- Termination: graceful via Unbind or Notice of Disconnection; abrupt if pernicious.

## 6. Security Considerations (Condensed)
- Cleartext passwords strongly discouraged without confidentiality.
- Servers encouraged to prevent modifications by anonymous clients.
- SASL does not protect version, name, resultCode, diagnosticMessage, or controls in Bind messages.
- Security factors (authentication, authorization, data protection) may change; implementations should handle robustly.
- Cache implementations must enforce access controls.
- Clients should be aware of referral injection; reject referrals from StartTLS.
- Error fields (matchedDN, diagnosticMessage) may disclose protected information.
- Protocol peers must handle invalid and arbitrary-length encodings (e.g., PROTOS test suite).
- Abrupt termination recommended upon sensing attacks.

## 7. Acknowledgements (Condensed)
Based on RFC2251 (Wahl, Howes, Kille), RFC2830 (Hodges, Morgan, Wahl), RFC3771 (Harrison, Zeilenga). Significant contributions from Kurt Zeilenga, Steven Legg, Hallvard Furuseth.

## 8. Normative References (Selected list)
- [RFC2119], [RFC3629], [RFC3986], [RFC4234], [RFC4346], [RFC4422], [RFC4510], [RFC4512], [RFC4513], [RFC4514], [RFC4516], [RFC4517], [RFC4520], [ASN.1] (X.680), [BER] (X.690), [ISO10646], [Unicode], [X.500], [X.511].

## 9. Informative References (Condensed)
- [CharModel], [Glossary], [PortReg], [PROTOS-LDAP].

## 10. IANA Considerations
- Updated result code registry for codes 0-36, 48-54, 64-70, 80-90; renamed `strongAuthRequired` to `strongerAuthRequired`.
- Updated Protocol Mechanism registry for StartTLS (1.3.6.1.4.1.1466.20037).
- Assigned OID 18 for the ASN.1 module in this document.

## Appendix A. LDAP Result Codes (Normative)
- **Non-error codes**: success(0), compareFalse(5), compareTrue(6), referral(10), saslBindInProgress(14).
- **Error codes**: operationsError(1), protocolError(2), timeLimitExceeded(3), sizeLimitExceeded(4), authMethodNotSupported(7), strongerAuthRequired(8), adminLimitExceeded(11), unavailableCriticalExtension(12), confidentialityRequired(13), noSuchAttribute(16), undefinedAttributeType(17), inappropriateMatching(18), constraintViolation(19), attributeOrValueExists(20), invalidAttributeSyntax(21), noSuchObject(32), aliasProblem(33), invalidDNSyntax(34), aliasDereferencingProblem(36), inappropriateAuthentication(48), invalidCredentials(49), insufficientAccessRights(50), busy(51), unavailable(52), unwillingToPerform(53), loopDetect(54), namingViolation(64), objectClassViolation(65), notAllowedOnNonLeaf(66), notAllowedOnRDN(67), entryAlreadyExists(68), objectClassModsProhibited(69), affectsMultipleDSAs(71), other(80).
- Additional result codes **MAY** be defined for extensions. Client implementations **SHALL** treat unrecognized result codes as unknown error.

## Appendix B. Complete ASN.1 Definition (Normative)
Provided in full in the original document. Includes all type definitions from LDAPMessage to IntermediateResponse.

## Appendix C. Changes (Informative)
- **RFC2251 changes**: Removed Binary Option; clarified protocol extensibility, messageID reuse, control combinations, search filter evaluation (Undefined), derefAliases semantics, Modify DN support for newSuperior, etc.
- **RFC2830 changes**: Removed referral from StartTLS; aligned with ExtendedResponse semantics.
- **RFC3771 changes**: Integrated into this document with preserved semantics.

## Requirements Summary (Selected Key Requirements)
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R01 | **MUST** ignore trailing SEQUENCE components with unrecognized tags (unless otherwise specified) | MUST | §4 intro |
| R02 | If server cannot parse LDAPMessage envelope: **SHOULD** return Notice of Disconnection with protocolError, **MUST** terminate session | SHOULD/MUST | §4.1.1 |
| R03 | Request messageID **MUST** be non-zero and unique among in-progress requests | MUST | §4.1.1.1 |
| R04 | Client **MUST NOT** reuse messageID unless certain server no longer servicing earlier request | MUST | §4.1.1.1 |
| R05 | Server **SHALL NOT** perform alias dereferencing for Bind, Modify, Add, Delete, Modify DN, Compare | SHALL NOT | §§4.2,4.6,4.7,4.8,4.9,4.10 |
| R06 | Textual passwords via simple auth **SHALL** be UTF-8; **SHOULD** be SASLprep'ed | SHALL/SHOULD | §4.2 |
| R07 | After Bind request, client **MUST NOT** send further PDUs until BindResponse | MUST | §4.2.1 |
| R08 | For non-critical unrecognized control: **server MUST** ignore it | MUST | §4.1.11 |
| R09 | For critical unrecognized control: **server MUST NOT** perform operation and **MUST** return unavailableCriticalExtension | MUST | §4.1.11 |
| R10 | Search filter evaluation uses three-valued logic; **server MUST NOT** return errors for unrecognized attributes/matching rules (evaluate to Undefined) | MUST NOT | §4.5.1.7 |
| R11 | Modify changes **MUST** be atomic and in order; final entry **MUST** conform to schema | MUST | §4.6 |
| R12 | Only leaf entries can be deleted | – | §4.8 |
| R13 | StartTLS: client **MUST NOT** send further LDAP PDUs until after response and TLS negotiation | MUST | §4.14.1 |
| R14 | Clients following referrals or continuation references **MUST** avoid loops; **MUST NOT** repeatedly contact same server with same parameters; **MUST handle** at least ten nested referrals | MUST | §§4.1.10,4.5.3 |
| R15 | Encoding: **SHALL** use definite length, primitive OCTET STRING, BOOLEAN true = 0xFF | SHALL | §5.1 |

*This summary captures the most critical normative statements. All other obligations are preserved in the full section text above.*