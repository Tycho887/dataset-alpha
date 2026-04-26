# RFC 4741: NETCONF Configuration Protocol
**Source**: IETF (Standards Track) | **Version**: RFC 4741 | **Date**: December 2006 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4741

## Scope (Summary)
Defines the Network Configuration Protocol (NETCONF) – an XML‑RPC based mechanism to install, manipulate, and delete configuration of network devices, with separation of configuration and state data.

## Normative References
- **RFC 2119**: Key words for requirement levels (MUST, SHOULD, etc.)
- **RFC 4742**: Using NETCONF over SSH (mandatory transport)
- **RFC 3986**: URI syntax
- **RFC 3553**: URN sub‑namespace for registered protocol parameters
- **RFC 3688**: IETF XML registry
- **W3C XML 1.0**: (Second Edition)
- **W3C XPath 1.0**: 

## Definitions and Abbreviations
- **NETCONF session**: Logical connection between client and server; device MUST support at least one, SHOULD support multiple.
- **Configuration datastore**: Complete set of configuration data to get device from initial default state to desired operational state (excludes state data and executive commands).
- **Running configuration**: The currently active configuration; always present.
- **Candidate configuration**: A working copy of configuration that can be manipulated without affecting running config (requires `:candidate` capability).
- **Startup configuration**: Non‑volatile configuration loaded at boot (requires `:startup` capability).
- **RPC**: Remote Procedure Call – encoding used by NETCONF.
- **Subtree filtering**: Default mechanism to select portions of configuration/state data based on XML subtree structure.
- **Capability**: A set of functionality augmenting the base protocol, identified by a URI.
- **<rpc>**: Element enclosing a request; MUST have `message-id` attribute (user‑defined string).
- **<rpc-reply>**: Response element; MUST have `message-id` equal to the request’s.
- **<rpc-error>**: Error information; MAY appear multiple times; MUST be returned if error occurs, SHOULD if warning.
- **<ok>**: Sent in reply if no errors/warnings.
- **<hello>**: Session establishment message; each peer MUST send its capabilities.
- **session-id**: Unique identifier for a server session; MUST be included in server’s `<hello>`, MUST NOT be included in client’s.
- **<config>**: Carries configuration data (opaque to protocol).
- **<filter>**: Used in `<get-config>` and `<get>`; supports `type` attribute (subtree or xpath).
- **<url>**: Alternative to inline `<config>` (requires `:url` capability).
- **operation attribute** (in `<edit-config>`): `merge`, `replace`, `create`, `delete` (default `merge`).
- **default-operation parameter**: `merge`, `replace`, `none` (default `merge`).
- **test-option**: `test‑then‑set`, `set` (requires `:validate` capability).
- **error-option**: `stop‑on‑error`, `continue‑on‑error`, `rollback‑on‑error` (the latter requires `:rollback‑on‑error` capability).
- **commit**: Operation that sets running configuration to candidate.
- **discard-changes**: Reverts candidate to running.
- **confirmed commit**: Commit that is reverted unless followed by a confirming commit within 600 seconds (configurable).
- **validate**: Checks configuration for syntax/semantic errors.
- **lock/unlock**: Prevents modification of a configuration datastore by other sessions/entities.
- **close-session/kill-session**: Graceful/forced session termination.

## 1. Introduction
- NETCONF uses an RPC paradigm over a secure connection‑oriented session.
- Encodes RPCs in XML; errors and responses are XML.
- Allows client to discover server capabilities (Section 8).
- Key words as per RFC 2119.

### 1.1 Protocol Overview
NETCONF consists of four layers:
1. **Transport Protocol** (BEEP, SSH, SSL, console) – provides requirements per Section 2.
2. **RPC Layer** – framing `<rpc>` and `<rpc-reply>` (Section 4).
3. **Operations Layer** – base operations: `<get-config>`, `<edit-config>`, etc. (Section 7).
4. **Content Layer** – device‑specific configuration data (outside scope of this RFC).

- Device MUST support at least one NETCONF session, SHOULD support multiple.
- Global config changes visible in all sessions; session‑specific attributes affect only that session.

### 1.2 Capabilities
- Identified by a URI; capabilities are advertised during session establishment.
- Server MUST support any capabilities on which a capability depends.
- Additional capabilities can be defined externally (standards or proprietary).

### 1.3 Separation of Configuration and State Data
- Configuration data: writable data to transform system from default to current state.
- State data: read‑only status and statistics.
- `<get-config>` retrieves only configuration; `<get>` retrieves both.

## 2. Transport Protocol Requirements
- **Connection‑oriented**: persistent, reliable, sequenced data delivery.
- Resources (e.g., locks) MUST be automatically released on connection close.
- **Authentication, integrity, confidentiality** required; provided by transport layer.
- **Authentication**: identity must be proven and permissions enforced.
- **Mandatory transport**: SSH (per RFC 4742) MUST be supported.

## 3. XML Considerations
- Namespace: `urn:ietf:params:xml:ns:netconf:base:1.0`
- Document type declarations MUST NOT appear.

## 4. RPC Model
### 4.1 `<rpc>` Element
- **Mandatory attribute** `message-id` (string, typically monotonically increasing).
- Additional attributes MUST be returned unmodified in `<rpc-reply>`.
- RPC name and parameters are child elements of `<rpc>`.

### 4.2 `<rpc-reply>` Element
- **Mandatory attribute** `message-id` equal to request’s.
- Additional attributes from `<rpc>` MUST be returned.
- Response data is inside a child element (e.g., `<data>`).

### 4.3 `<rpc-error>` Element
- Contains: `error-type` (transport/rpc/protocol/application), `error-tag`, `error-severity` (error/warning), `error-app-tag` (optional), `error-path` (XPath, optional), `error-message` (optional, SHOULD have `xml:lang`), `error-info` (optional).
- Server MUST return `<rpc-error>` on error, SHOULD on warning.
- MUST NOT return application‑level error info if client lacks access rights.

### 4.4 `<ok>` Element
- Sent if no errors/warnings.

### 4.5 Pipelining
- Requests MUST be processed serially; additional requests MAY be sent before prior ones complete.
- Server MUST send responses in order received.

## 5. Configuration Model
- **Datastores**: `<running>` is base; `<candidate>` and `<startup>` defined by capabilities.
- **Data modeling**: outside scope; device announces supported data models via capabilities.

## 6. Subtree Filtering
### 6.1 Overview
- Mechanism to select XML subtrees in `<get>` or `<get-config>` replies.
- Filter components: **namespace selection**, **attribute match expression**, **containment node**, **selection node**, **content match node**.
- Namespace must exactly match supported namespace.

### 6.2 Components
- **Namespace Selection**: `xmlns` must match; at least one element must be specified.
- **Attribute Match Expressions**: attribute values must match for node to be selected.
- **Containment Nodes**: nodes with child elements; all exact matches are included.
- **Selection Nodes**: empty leaf node; only that subtree is included.
- **Content Match Nodes**: leaf with simple content; exact‑match filter; multiple siblings combined with AND.
  - Constraints: no nested elements, no mixed content, no list content, must contain non‑whitespace.
  - If all content match sibling tests true, then:
    - Content match nodes included.
    - Containment nodes processed further.
    - Selection nodes included.
    - Otherwise (no selection/containment) all siblings included.
  - If any test false, entire sibling set excluded.

### 6.3 Processing
- Server determines inclusion/exclusion per sibling set recursively.

### 6.4 Examples
- Provided in full detail (Section 6.4.1–6.4.8) demonstrating various filter patterns.

## 7. Protocol Operations
### 7.1 `<get-config>`
- **Retrieve** all or part of a specified configuration datastore.
- **Parameters**: `<source>` (required), `<filter>` (optional, default whole).
- **Positive**: `<rpc-reply>` with `<data>`.
- **Negative**: `<rpc-error>`.

### 7.2 `<edit-config>`
- **Load** configuration onto target datastore.
- **Attributes**: `operation` (merge/replace/create/delete) on config elements.
- **Parameters**: `<target>`, `<default-operation>` (optional, default merge), `<test-option>` (requires :validate), `<error-option>` (requires :rollback‑on‑error for rollback‑on‑error), `<config>` or `<url>`.
- **Positive**: `<ok>`.
- **Negative**: `<rpc-error>`.
- Examples included.

### 7.3 `<copy-config>`
- **Create or replace** entire configuration datastore.
- **Parameters**: `<target>`, `<source>` (can be `<url>`).
- If target and source same, error `invalid‑value`.
- **Positive**: `<ok>`.

### 7.4 `<delete-config>`
- Delete a datastore (except `<running>`).
- **Parameters**: `<target>`.
- **Positive**: `<ok>`.

### 7.5 `<lock>`
- Lock a configuration datastore.
- **Conditions**: lock fails if already held by any session/entity, or if target is `<candidate>` modified without commit/rollback.
- **Positive**: `<ok>`.
- **Negative**: `<rpc-error>` with `lock‑denied` and `<session-id>` (0 for non‑NETCONF).
- Lock released on session termination.

### 7.6 `<unlock>`
- Release a lock; only the locking session can unlock.
- **Positive**: `<ok>`.

### 7.7 `<get>`
- Retrieve running configuration and state data.
- **Filter**: optional.

### 7.8 `<close-session>`
- Graceful termination; releases locks and resources.
- **Positive**: `<ok>`.

### 7.9 `<kill-session>`
- Force termination of another session (by `<session-id>`).
- If the session is performing a confirmed commit, restore config to pre‑commit state.
- Does not roll back other modifications.
- **Positive**: `<ok>`; error if session‑id equals own.

## 8. Capabilities
### 8.1 Capabilities Exchange
- Each peer MUST send `<hello>` with list of capabilities (minimum base capability URI: `urn:ietf:params:netconf:base:1.0`).
- Server `<hello>` MUST include `<session-id>`; client MUST NOT.
- Peers send simultaneously; no waiting.

### 8.2 Writable-Running Capability (`:writable-running`)
- **Capability URI**: `urn:ietf:params:netconf:capability:writable-running:1.0`
- Allows `<edit-config>` and `<copy-config>` with `<running>` as target.

### 8.3 Candidate Configuration Capability (`:candidate`)
- **Capability URI**: `urn:ietf:params:netconf:capability:candidate:1.0`
- Supports `<candidate>` datastore, `<commit>`, `<discard-changes>`.
- Candidate may be shared; lock recommended.
- Modifications: `<get-config>`, `<edit-config>`, `<copy-config>`, `<validate>`, `<lock>`, `<unlock>` can use `<candidate>`.

### 8.4 Confirmed Commit Capability (`:confirmed-commit`)
- **Capability URI**: `urn:ietf:params:netconf:capability:confirmed-commit:1.0`
- Depends on `:candidate`.
- Adds `<confirmed>` and `<confirm-timeout>` parameters to `<commit>`.
- Timeout defaults to 600 seconds.
- If session terminated or device reboots before confirming commit, configuration reverted to pre‑commit state.
- Any subsequent commit acts as confirming commit.

### 8.5 Rollback on Error Capability (`:rollback-on-error`)
- **Capability URI**: `urn:ietf:params:netconf:capability:rollback-on-error:1.0`
- Allows `rollback-on-error` value for `<error-option>` in `<edit-config>`.

### 8.6 Validate Capability (`:validate`)
- **Capability URI**: `urn:ietf:params:netconf:capability:validate:1.0`
- Supports `<validate>` operation and `test-option` parameter in `<edit-config>`.
- Validates at least syntax errors.

### 8.7 Distinct Startup Capability (`:startup`)
- **Capability URI**: `urn:ietf:params:netconf:capability:startup:1.0`
- Separate `<startup>` datastore; changes to running do not affect startup automatically.
- Explicit `<copy-config>` from `<running>` to `<startup>` required.

### 8.8 URL Capability (`:url`)
- **Capability URI**: `urn:ietf:params:netconf:capability:url:1.0?scheme={name,...}`
- Allows `<url>` element in `<source>`/`<target>` for various operations.
- URI MUST contain `scheme` argument with supported schemes.

### 8.9 XPath Capability (`:xpath`)
- **Capability URI**: `urn:ietf:params:netconf:capability:xpath:1.0`
- Enables `type="xpath"` on `<filter>` element; `select` attribute contains XPath expression that must return a node‑set.
- Context node is root node; namespaces in scope on `<filter>`.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Device MUST support at least one session | shall | 1.1 |
| R2 | Device SHOULD support multiple sessions | should | 1.1 |
| R3 | Transport MUST provide session type indicator | shall | 2 |
| R4 | Transport MUST be connection‑oriented, reliable, sequenced | shall | 2.1 |
| R5 | Resources MUST be released on connection close | shall | 2.1 |
| R6 | Transport MUST provide authentication, integrity, confidentiality | shall | 2.2 |
| R7 | Authentication MUST result in enforceable permissions | shall | 2.3 |
| R8 | SSH transport mapping MUST be supported | shall | 2.4 |
| R9 | Document type declarations MUST NOT appear | shall | 3.2 |
| R10 | `<rpc>` MUST have `message-id` attribute | shall | 4.1 |
| R11 | Additional attributes in `<rpc>` MUST be returned in `<rpc-reply>` | shall | 4.2 |
| R12 | Server MUST return `<rpc-error>` on error, SHOULD on warning | shall/should | 4.3 |
| R13 | Server MUST NOT return app‑level error info without sufficient access | shall | 4.3 |
| R14 | `<rpc>` requests MUST be processed serially | shall | 4.5 |
| R15 | Server MUST send responses in order received | shall | 4.5 |
| R16 | Lock MUST fail if already held by any session/entity | shall | 7.5 |
| R17 | Lock MUST fail if target is `<candidate>` modified without commit/rollback | shall | 7.5 |
| R18 | Unlock only possible by locking session | shall | 7.6 |
| R19 | Server `<hello>` MUST include `<session-id>` | shall | 8.1 |
| R20 | Client `<hello>` MUST NOT include `<session-id>` | shall | 8.1 |
| R21 | Each peer MUST send at least base capability | shall | 8.1 |
| R22 | Peers MUST NOT wait for other’s `<hello>` before sending own | shall | 8.1 |
| R23 | Server MUST support dependencies of any advertised capability | shall | 1.2 |
| R24 | Confirming commit must be sent within timeout or config reverts | shall | 8.4 |
| R25 | If session holding confirmed commit terminates, config reverts | shall | 8.4 |
| R26 | `<copy-config>` with same source and target MUST return error | shall | 7.3 |
| R27 | `<delete-config>` cannot delete `<running>` | shall | 7.4 |
| R28 | `:<confirmed-commit>` capability depends on `:candidate` | shall | 8.4.2 |
| R29 | Capability URI must distinguish naming authority | shall | 1.2 |
| R30 | `:url` URI MUST contain `scheme` argument | shall | 8.8.3 |
| R31 | XPath expression must return a node‑set | shall | 8.9.1 |

## Informative Annexes (Condensed)
- **Appendix A (NETCONF Error List)**: Defines standard error tags (`in-use`, `invalid-value`, `too-big`, `missing-attribute`, `bad-attribute`, `unknown-attribute`, `missing-element`, `bad-element`, `unknown-element`, `unknown-namespace`, `access-denied`, `lock-denied`, `resource-denied`, `rollback-failed`, `data-exists`, `data-missing`, `operation-not-supported`, `operation-failed`, `partial-operation`). Each specifies error‑type, severity, optional error‑info, and description. (Full list preserved above in condensed table.)
- **Appendix B (XML Schema for NETCONF RPC and Protocol Operations)**: Complete XML Schema document defining all elements and types used in the protocol (normative attachment).
- **Appendix C (Capability Template)**: Template for defining new capabilities: overview, dependencies, capability identifier, new operations, modifications to existing operations, interactions with other capabilities.
- **Appendix D (Configuring Multiple Devices with NETCONF)**: Informative guide describing a workflow for multidevice configuration: lock, load, validate, checkpoint, change, test, make permanent, unlock. For transactional semantics across devices, use parallel locks and coordinated commit/rollback.
- **Appendix E (Deferred Features)**: Features postponed to future revisions: granular locking, named configuration datastores, multiple NETCONF channels, asynchronous notifications, explicit rollback support.