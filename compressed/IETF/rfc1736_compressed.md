# RFC 1736: Functional Recommendations for Internet Resource Locators
**Source**: IETF | **Version**: Informational | **Date**: February 1995 | **Type**: Informational

## Scope (Summary)
This document specifies a minimum set of requirements for Internet resource locators, which convey location and access information for resources. Locators may apply to resources that are not always or not ever network accessible. A resource locator is a kind of resource identifier; other kinds include resource names and resource descriptions.

## Normative References
None.

## Definitions and Abbreviations
- **General resource locator**: An object that describes the location of a resource.
- **Internet resource locator**: A locator defined by an Internet resource location standard.
- **Resource location standard**: A standard that in conjunction with resource description and resource naming standards specifies a comprehensive infrastructure for network based information dissemination.
- **Interpreter**: An agent (human or software) that interprets a resource locator.
- **Producer**: An agent that produces a resource locator.
- **Invalid locator**: A locator that conforms to a location standard but fails for reasons of resource movement, replacement, or deletion.
- **Unavailable resource**: A resource that is inaccessible due to provider support policies, rights restrictions, or network load.

## Introduction
### 1. Introduction
This document specifies a minimum set of requirements for Internet resource locators. Locators convey location and access information for resources (e.g., network accessible documents, WAIS databases, FTP servers, Telnet destinations). Locators may apply to non-network accessible resources (e.g., human beings, physical objects without electronic instantiation). A resource locator is a kind of resource identifier; other kinds are resource names (for stable handles) and resource descriptions (meta-information for search and selection). Mechanisms for mapping between locators, names, and descriptive identifiers are beyond scope.

### 2. Overview of Problem
#### 2.1 Defining the General Resource Locator
The requirements impose restrictions on the general resource locator. Definition: *A general resource locator is an object that describes the location of a resource.* The definition is analyzed in four parts:
- (1) an object (could be complex data structure, byte sequence, etc.)
- (2) that describes (could be graphical, natural language, encoded, etc.)
- (3) the location of (does not guarantee access; resource may not exist or be inaccessible)
- (4) a resource (many things: documents, images, servers, collections, etc.)

#### 2.2 Producers and Interpreters of Resource Locators
- **Interpreters**: human or software. A locator may be understood only in part by each interpreter, but completely by a combination. A resource location standard must make explicit any assumptions about locator recognition.
- **Producers**: resource providers, non-providers (e.g., WWW clients, databases like Archie), and users. Users constructing locators for sharing are responsible for conformance. Abbreviated locators entered by users for personal use are not bound by requirements.

#### 2.3 Uniqueness of Resource Locators
This document rejects the following as requirements:
- **2.3.1**: Uniqueness and multiple copies – no requirement that no identical copies exist.
- **2.3.2**: Uniqueness and deterministic access – no requirement that same access result each time; does not define "sameness".
- **2.3.3**: Uniqueness and multiple locators – no requirement that a resource have at most one locator.
- **2.3.4**: Uniqueness, ambiguity, and multiple objects per access – no general definition of what constitutes one object.

### 3. Resource Access and Availability
A locator never guarantees access. Invalid locators (conformant but fail due to resource change) are addressed by naming standards. Unavailable resources are addressed by description standards. The probability of successful access decreases over time and depends on resource nature, provider policies, and network load.

## Requirements List for Internet Resource Locators
### 4. Requirements List
The following requirements are applied to the set of general locators to define Internet locators. One requirement (software recognition in unstructured text) was dropped as impractical.

#### 4.1 Locators are transient.
The probability with which a given Internet resource locator leads to successful access decreases over time. More stable schemes are addressed in resource naming standards.

#### 4.2 Locators have global scope.
The name space of resource locators includes the entire world. The probability of successful access depends in no way, modulo resource availability, on the geographical or Internet location of the client.

#### 4.3 Locators are parsable.
Internet locators can be broken down into complete constituent parts sufficient for interpreters (software or human) to attempt access if desired. Three points:
- **4.3.1**: A given kind of locator may still be parsable even if a given interpreter cannot parse it.
- **4.3.2**: Parsable by users does not imply readily parsable by untrained users.
- **4.3.3**: A given locator need not be completely parsable by any one interpreter as long as a combination of interpreters can parse it completely.

#### 4.4 Locators can be readily distinguished from naming and descriptive identifiers that may occupy the same name space.
During a transition period, other kinds of resource identifier are expected to co-exist in data structures along with Internet locators.

#### 4.5 Locators are "transport-friendly".
Internet locators can be transmitted from user to user (e.g., via e-mail) across Internet standard communications protocols without loss or corruption of information.

#### 4.6 Locators are human transcribable.
Users can copy Internet locators from one medium to another (such as voice to paper, or paper to keyboard) without loss or corruption of information. This process is not required to be comfortable.

#### 4.7 An Internet locator consists of a service and an opaque parameter package.
The parameter package has meaning only to the service with which it is paired, where a service is an abstract access method (e.g., software tool, institution, network protocol). The package might be service-specific access instructions. No parameter package semantics common across services may be assumed.

#### 4.8 The set of services is extensible.
New services can be added over time.

#### 4.9 Locators contain no information about the resource other than that required by the access mechanism.
The purpose of an Internet locator is only to describe the location of a resource, not other properties such as type, size, modification date, etc. Those properties belong in a resource description standard.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Locators are transient. | Requirement | Section 4.1 |
| R2 | Locators have global scope. | Requirement | Section 4.2 |
| R3 | Locators are parsable. | Requirement | Section 4.3 |
| R4 | Locators can be readily distinguished from naming and descriptive identifiers. | Requirement | Section 4.4 |
| R5 | Locators are "transport-friendly". | Requirement | Section 4.5 |
| R6 | Locators are human transcribable. | Requirement | Section 4.6 |
| R7 | An Internet locator consists of a service and an opaque parameter package. | Requirement | Section 4.7 |
| R8 | The set of services is extensible. | Requirement | Section 4.8 |
| R9 | Locators contain no information about the resource other than that required by the access mechanism. | Requirement | Section 4.9 |

## Security Considerations
1. **Invalid locators and unintended access**: Because locators are transient, a client using an invalid locator might gain access to a resource that was not the intended target (e.g., hostname re-registration).
2. **Service parameter package vulnerabilities**: A server is vulnerable unless it suitably restricts its input parameters (e.g., filesystem access). A client is vulnerable unless it understands service limitations (e.g., charges). For services with great user freedom (e.g., remote login), pre-specification of user commands within a locator presents vulnerabilities (e.g., embedded commands like "rm -fr *").

## Informative Annexes
None.

*Note: This document is informational; it does not specify an Internet standard.*