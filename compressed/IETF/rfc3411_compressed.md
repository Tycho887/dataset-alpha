# RFC 3411: An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks
**Source**: IETF SNMPv3 Working Group | **Version**: STD 62 | **Date**: December 2002 | **Type**: Standards Track
**Original**: https://tools.ietf.org/html/rfc3411

## Scope (Summary)
This document defines a modular architecture for SNMP Management Frameworks, specifying an SNMP engine (containing a Dispatcher, Message Processing Subsystem, Security Subsystem, and Access Control Subsystem) and multiple SNMP applications. It provides vocabulary, abstract service interfaces, and guidelines to allow independent evolution of protocol components. It obsoletes RFC 2571.

## Normative References
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- RFC 2279: UTF-8 transformation format of ISO 10646
- RFC 2578: Structure of Management Information Version 2 (SMIv2)
- RFC 2579: Textual Conventions for SMIv2
- RFC 2580: Conformance Statements for SMIv2
- RFC 3412: Message Processing and Dispatching for SNMP
- RFC 3413: SNMP Applications
- RFC 3414: User-Based Security Model (USM) for SNMPv3
- RFC 3415: View-based Access Control Model (VACM) for SNMP
- RFC 3416: Protocol Operations for SNMP
- RFC 3417: Transport Mappings for SNMP
- RFC 3418: Management Information Base (MIB) for SNMP

## Definitions and Abbreviations
- **SNMP engine**: Provides services for sending/receiving messages, authenticating/encrypting messages, and access control. One-to-one with SNMP entity.
- **snmpEngineID**: Unique identifier of an SNMP engine within an administrative domain.
- **Dispatcher**: Single component in an engine that supports multiple SNMP message versions, sends/receives messages, and provides abstract interfaces to applications.
- **Message Processing Subsystem**: Responsible for preparing messages for sending and extracting data from received messages; contains one or more Message Processing Models.
- **Message Processing Model**: Defines format of a particular SNMP message version (e.g., SNMPv1, SNMPv2c, SNMPv3).
- **Security Subsystem**: Provides authentication and privacy services; contains one or more Security Models.
- **Security Model**: Specifies threats protected against, goals, and security protocols.
- **Security Protocol**: Mechanisms and MIB objects for a specific security service (authentication or privacy).
- **Access Control Subsystem**: Provides authorization services via one or more Access Control Models.
- **Access Control Model**: Defines decision function for access rights.
- **Application**: Uses SNMP engine services; types include command generator, command responder, notification originator, notification receiver, proxy forwarder.
- **Principal**: The "who" on whose behalf services are provided.
- **securityName**: Human-readable string representing a principal, model-independent.
- **Model-dependent security ID**: Model-specific representation of a securityName (e.g., community name, user name).
- **SNMP context**: Collection of management information accessible by an SNMP entity, identified by contextEngineID + contextName.
- **contextEngineID**: Uniquely identifies an SNMP entity that may realize a context.
- **contextName**: Name of a context, unique within an SNMP entity.
- **scopedPDU**: Block containing contextEngineID, contextName, and PDU.
- **maxSizeResponseScopedPDU**: Maximum size of a scopedPDU that the sender will accept.
- **Local Configuration Datastore (LCD)**: Collection of configuration information retained by subsystems, models, and applications.
- **securityLevel**: Three levels: noAuthNoPriv, authNoPriv, authPriv (ordered).
- **PDU Classes**: Read, Write, Response, Notification, Internal; also Confirmed and Unconfirmed.

## 1. Introduction
### 1.1 Overview
This document defines vocabulary and architecture for SNMP Management Frameworks, not a general SNMP introduction. Key words (MUST, SHALL, etc.) per RFC 2119.

### 1.2 SNMP
An SNMP management system includes nodes with SNMP entities (agents) having command responder/notification originator applications, at least one manager entity with command generator/notification receiver, and a management protocol. The architecture supports minimal agents, proxy forwarders, command-line managers, mid-level managers, and large network management stations.

### 1.3 Goals
- Use existing materials (SNMPv2u, SNMPv2*)
- Address secure SET support
- Allow modular standards-track evolution
- Ensure longevity of Frameworks
- Keep SNMP simple and inexpensive for minimal implementations
- Allow upgrades without disrupting entire framework
- Support large network features with proportional cost

### 1.4 Security Requirements
**Principal threats** (SHOULD provide protection):
- **Modification of Information**: unauthorized alteration of in-transit messages.
- **Masquerade**: unauthorized operations by assuming another principal's identity.

**Secondary threats** (SHOULD provide protection):
- **Message Stream Modification**: malicious re-ordering, delay, or replay of messages.
- **Disclosure**: eavesdropping on exchanges.

**Threats not required to protect against**:
- Denial of Service
- Traffic Analysis

### 1.5 Design Decisions
- Define architecture with conceptual boundaries and abstract service interfaces.
- Self-contained documents: elements of procedure and MIB objects for a specific portion defined in same document.
- Security Models SHOULD protect against principal and secondary threats.
- Remote configuration of Security and Access Control parameters required.
- Balance simplicity vs. complexity; allow logical extension.

## 2. Documentation Overview
Documents fit within SNMP Architecture: Document Roadmap, Applicability Statement, Coexistence & Transition, Transport Mappings, Message Processing and Dispatcher, Security, Protocol Operations, Applications, Access Control, Structure of Management Information, Textual Conventions, Conformance Statements, MIB Modules.

### 2.1 Document Roadmap
Set of documents forming specific Frameworks; roadmap maintained separately (e.g., RFC 3410).

### 2.2 Applicability Statement
Describes appropriate environments for versions/models.

### 2.3 Coexistence and Transition
Documents detail anomalies and required/recommended behaviors for model interactions. Example: RFC 2576 (Coexistence between SNMPv1, v2, v3).

### 2.4 Transport Mappings
Define mapping between SNMP and transports.

### 2.5 Message Processing
Message Processing Model document defines message format (identified by version field). Engine supports multiple models.

### 2.6 Security
Covers message-level security (authentication, encryption, timeliness). Security Model document describes threats, goals, protocols, MIB module. Engine supports multiple Security Models.

### 2.7 Access Control
Access Control Model defines mechanisms to decide access to managed objects.

### 2.8 Protocol Operations
SNMP PDUs define operations; classified into Read, Write, Response, Notification, Internal; also Confirmed/Unconfirmed. Application document defines supported operations.

### 2.9 Applications
Applications use engine services; document describes purpose, required services, protocol operations, informational model.

### 2.10 - 2.14 Structure of Management Information, Textual Conventions, Conformance Statements, MIB Modules, SNMP Framework Documents
Notation for objects/modules (SMI), textual conventions, conformance notation, MIB modules for instrumentation. Frameworks: SNMPv1, SNMPv2, SNMPv2c, SNMPv3. "Subsystem" = abstract portion refined by model; "Model" = specific design; "Implementation" = instantiation.

## 3. Elements of the Architecture
### 3.1 Naming of Entities
- **SNMP entity**: implementation consisting of SNMP engine and associated applications.
- **SNMP engine**: includes Dispatcher, Message Processing Subsystem, Security Subsystem, Access Control Subsystem.
- **snmpEngineID**: unique identifier within administrative domain; persists across re-initializations.
- **Dispatcher**: single per engine; sends/receives messages, determines version, provides abstract interfaces.
- **Message Processing Subsystem**: contains multiple Message Processing Models (SNMPv3, v1, v2c, other).
- **Message Processing Model**: defines format and processing of a specific message version.
- **Security Subsystem**: contains multiple Security Models (e.g., User-Based Security Model).
- **Security Model**: specifies threats, goals, protocols.
- **Security Protocol**: specific mechanism for authentication/privacy.
- **Access Control Subsystem**: contains multiple Access Control Models (e.g., View-Based Access Control Model).
- **Applications**: types: command generator, command responder, notification originator, notification receiver, proxy forwarder.

### 3.2 Naming of Identities
- **Principal**: the "who" (individual, set of individuals, application, combinations).
- **securityName**: model-independent human-readable string.
- **Model-dependent security ID**: model-specific representation (e.g., community name, user name). Transformation responsibility of Security Model.

### 3.3 Naming of Management Information
- **SNMP context**: collection of management information, identified by contextEngineID + contextName.
- **contextEngineID**: uniquely identifies SNMP entity realizing a context.
- **contextName**: unique within an SNMP entity.
- **scopedPDU**: block containing contextEngineID, contextName, and PDU.

### 3.4 Other Constructs
- **maxSizeResponseScopedPDU**: maximum size of scopedPDU sender will accept.
- **Local Configuration Datastore (LCD)**: configuration information for subsystems, models, applications.
- **securityLevel**: three values (noAuthNoPriv, authNoPriv, authPriv). All subsystems and applications REQUIRED to supply or abide by securityLevel.

## 4. Abstract Service Interfaces
Primitives define conceptual interfaces; not APIs.

### 4.1 Dispatcher Primitives
- **sendPdu**: generate outgoing request/notification. Returns sendPduHandle or errorIndication.
- **processPdu**: pass incoming request/notification to application.
- **returnResponsePdu**: generate outgoing response.
- **processResponsePdu**: pass incoming response to application.
- **registerContextEngineID / unregisterContextEngineID**: register/unregister application for specific contextEngineID and pduType.

### 4.2 Message Processing Subsystem Primitives
- **prepareOutgoingMessage**: prepare request/notification message.
- **prepareResponseMessage**: prepare response message.
- **prepareDataElements**: extract data from incoming message.

### 4.3 Access Control Subsystem Primitives
- **isAccessAllowed**: check if access allowed for (securityModel, securityName, securityLevel, viewType, contextName, variableName).

### 4.4 Security Subsystem Primitives
- **generateRequestMsg**: generate request/notification message with security parameters.
- **processIncomingMsg**: validate and extract data from incoming message.
- **generateResponseMsg**: generate secure response.

### 4.5 Common Primitives
- **stateRelease**: release state reference information.

### 4.6 Scenario Diagrams
Illustrate interactions for command generator/notification originator (sendPdu -> prepareOutgoingMessage -> generateRequestMsg -> ... -> processResponsePdu) and command responder (registerContextEngineID -> ... -> processPdu -> returnResponsePdu).

## 5. Managed Object Definitions for SNMP Management Frameworks
SNMP-FRAMEWORK-MIB module defined:
- **SnmpEngineID**: OCTET STRING (SIZE 5..32). Algorithm for generating engine ID.
- **SnmpSecurityModel**: INTEGER (0..2147483647). Allocation: 0-255 IANA managed, >255 enterprise-specific (enterpriseID*256 + model).
- **SnmpMessageProcessingModel**: INTEGER (0..2147483647). Similar allocation.
- **SnmpSecurityLevel**: INTEGER { noAuthNoPriv(1), authNoPriv(2), authPriv(3) }.
- **SnmpAdminString**: OCTET STRING (SIZE 0..255), UTF-8 encoded administrative information.
- **Object groups**: snmpEngineGroup (snmpEngineID, snmpEngineBoots, snmpEngineTime, snmpEngineMaxMessageSize). Registration points for authentication and privacy protocols.

## 6. IANA Considerations
### 6.1 Security Models
Values 0-255 managed by IANA. Current: 0 (any), 1 (SNMPv1), 2 (SNMPv2c), 3 (USM).

### 6.2 Message Processing Models
Values 0-255 managed by IANA. Current: 0 (SNMPv1), 1 (SNMPv2c), 2 (SNMPv2u/*), 3 (SNMPv3).

### 6.3 SnmpEngineID Formats
Fifth octet format identifiers; values 6-127 managed by IANA.

## 7. Intellectual Property
Standard IETF IPR notice.

## 8. Acknowledgements
List of SNMPv3 Working Group members and Advisory Team.

## 9. Security Considerations
Implementation must include Security Model and Access Control Model. Applications SHOULD protect data from disclosure. Purchasers must ensure compliance, appropriate models, and protection of secrets. MIB objects not writable; access should be restricted if sensitive.

## 10. References
### 10.1 Normative (RFC 2119, 2279, 2578-2580, 3412-3418)
### 10.2 Informative (RFC 1155, 1157, 1212, 1901, 1909, 1910, 2028, 2576, 2863, 3410)

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Security Models SHOULD protect against modification of information and masquerade. | SHOULD | 1.4 |
| R2 | Security Models SHOULD protect against message stream modification and disclosure. | SHOULD | 1.4 |
| R3 | Security Models need not protect against denial of service or traffic analysis. | need not | 1.4 |
| R4 | Each contextName MUST be unique within an SNMP entity. | MUST | 3.3.3 |
| R5 | All subsystems and applications are REQUIRED to supply or abide by securityLevel. | REQUIRED | 3.4.3 |
| R6 | Security Model documents MUST describe protection against threats in 1.4. | MUST | A.1.1 |
| R7 | Received messages MUST be validated by a Security Model. | MUST | A.1.2 |
| R8 | All messages requiring privacy MUST also require authentication. | MUST | A.1.2 |
| R9 | Message Processing Model MUST always pass the complete PDU. | MUST | A.2 |
| R10 | Only one registration per combination of PDU type and contextEngineID permitted. | MUST | A.3.3 |

## Informative Annexes (Condensed)
- **A. Guidelines for Model Designers**: Provides design principles for Security Models, Message Processing Models, Applications, and Access Control Models. Emphasizes no cross-model references, use of standard primitives, and self-contained documents. Security Models must address threats, define validation, and manage cached security data. Message Processing Models must support standard primitives and always pass complete PDU. Applications must not reference specific Security Models, and must define access control if needed. Access Control Models must provide isAccessAllowed primitive and should make persistent data manageable via SNMP.