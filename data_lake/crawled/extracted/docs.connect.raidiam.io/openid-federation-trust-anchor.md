---
{
  "title": "Trust Scheme | Raidiam Developers",
  "url": "https://docs.connect.raidiam.io/openid-federation-trust-anchor",
  "domain": "docs.connect.raidiam.io",
  "depth": 2,
  "relevance_score": 0.35,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5456,
  "crawled_at": "2026-04-23T20:57:48"
}
---

On this page
In the context of
Trust Frameworks
,
a
Trust Schema
is a combination of rules, protocols, and infrastructure that enables
organizations to establish mutual trust for secure data exchange. This can be
achieved through two primary methods:
Federated trust via OpenID Federation
PKI-based trust using X.509 certificates
OpenID Federation as Trust Scheme
​
OpenID Federation is a protocol designed to establish trust between entities,
such as identity providers (IDPs) and relying parties (RPs), without requiring a
direct relationship between them. It uses a trust chain mechanism to facilitate
this trust, enabling secure interactions between parties in a federation.
OpenID Federation allows for the enrollment of an unlimited number of entities
without requiring direct relationships between them, enabling the creation of
even global data sharing ecosystems. It supports various federation topologies
and can be integrated with different protocols. It automates the discovery,
policing, and updating of RP and OP metadata, reducing administrative overhead.
What Makes OpenID Federation a Trust Scheme
​
Trust
Anchors
:
These are entities that serve as the foundation of trust within a federation.
They can be organizations or authorities that manage the trust framework.
Trust
Chains
:
These are sequences of trust relationships that connect entities within a
federation. Trust chains allow entities to trust each other indirectly through
shared trust anchors.
Entity
IDs
: Each
entity in the federation is assigned a unique identifier, known as an entity ID,
which is used to establish and manage trust relationships.
Federation
Entities
:
These include
identity providers, relying
parties
,
intermediate
authorities
,
and
trust anchors
. All these entities work together to form a trust framework.
How OpenID Federation Works
​
Establishing Trust
:
Entities join a federation by enrolling with a trust anchor or an intermediate
authority. This enrollment process allows them to become recognizable and
trusted by other members in the federation.
Trust Chain Resolution
:
When an RP and an IDP need to interact, they resolve
their trust chains to ensure they share a common trust anchor. This process
allows them to trust each other without prior direct registration.
Federation Topology: Federations can be structured in various ways,
including single trust anchors, multilateral federations, and super federations.
This flexibility allows for scalable and adaptable trust frameworks.
Application Protocols: OpenID Federation can be used with OpenID Connect and
OAuth 2.0, but its components are also applicable to other protocols for
establishing trust.
PKIs as Trust Schemes
​
A Public Key Infrastructure (PKI) enables organizations to establish trust
between each other by providing a structured system for secure communication and
identity verification. With a PKI, trust is established mainly through:
Certificate Authorities (CAs)
:
CAs are trusted entities responsible for issuing, managing, and revoking digital certificates. They verify the identity of entities requesting certificates and ensure that the public key belongs to the specified entity.
There are root CAs, which are the highest level of trust, and intermediate CAs, which issue certificates under the authority of root CAs.
Digital Certificates
:
Digital certificates are electronic documents that contain an entity's public
key and identity information. They are signed by a CA, which ensures the
authenticity of the public key and the identity of the entity.
Typically include the entity's name, public key, serial number, and expiration date.
X.509 Certificates
​
X.509 certificates are a standard format for public-key certificates used in
PKI. They bind an identity to a public key using a digital signature.
X.509 certificates the public key of the certificate holder, a serial number,
identification information about the certificate holder, a validity period, and
the name of the certificate issuer.
X.509s are crucial for establishing trust between entities by
verifying identities and ensuring secure communication over public networks.
Establishing Trust with PKI
​
Chain of Trust
:
Mechanism
: The chain of trust is established through a hierarchical
structure where intermediate CAs issue certificates under the authority of
root CAs. This ensures that entities can trust each other if they share a
common trust anchor.
Validation
: When an entity presents a certificate, the recipient
verifies the certificate by tracing it back to a trusted root CA.
Identity Verification
:
Process
: Digital certificates issued by CAs verify the identity of
entities, ensuring that only authorized parties can access resources or
communicate securely.
Benefits
: This verification process helps prevent impersonation attacks
and ensures that data is exchanged with the intended party.
Secure Communication
:
Encryption
: PKI enables secure data encryption and decryption using
public-key cryptography. This ensures confidentiality and integrity of data
exchanged between organizations.
Authentication
: Digital signatures, which are based on private keys
corresponding to public keys in certificates, authenticate the sender and
verify the integrity of messages.
Copy for LLMs
TABLE OF CONTENT
OpenID Federation as Trust Scheme
What Makes OpenID Federation a Trust Scheme
How OpenID Federation Works
PKIs as Trust Schemes
X.509 Certificates
Establishing Trust with PKI