# RFC 4742: Using the NETCONF Configuration Protocol over Secure SHell (SSH)
**Source**: IETF | **Version**: Standards Track | **Date**: December 2006 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc4742

## Scope (Summary)
Defines a method for invoking and running the Network Configuration Protocol (NETCONF) within a Secure Shell (SSH) session as an SSH subsystem. NETCONF is session-layer and transport independent; this mapping uses SSH connection protocol over SSH transport.

## Normative References
- [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [RFC4250] Lehtinen, S. and C. Lonvick, "The Secure Shell (SSH) Protocol Assigned Numbers", RFC 4250, January 2006.
- [RFC4252] Ylonen, T. and C. Lonvick, "The Secure Shell (SSH) Authentication Protocol", RFC 4252, January 2006.
- [RFC4253] Ylonen, T. and C. Lonvick, "The Secure Shell (SSH) Transport Layer Protocol", RFC 4253, January 2006.
- [RFC4254] Ylonen, T. and C. Lonvick, "The Secure Shell (SSH) Connection Protocol", RFC 4254, January 2006.
- [RFC4721] Enns, R., Ed., "NETCONF Configuration Protocol", RFC 4721, December 2006.

## Definitions and Abbreviations
- **Client/Server**: Two ends of SSH transport connection. Client actively opens SSH connection; server passively listens.
- **Manager/Agent**: Two ends of NETCONF protocol session. Manager issues RPC commands; agent replies.
- **When NETCONF is run over SSH**: Client is always the manager; server is always the agent.
- **SSH version**: SSHv2 is required; SSH subsystem support is not included in SSHv1.

## 2. Requirements Terminology
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119.

## 3. Starting NETCONF over SSH
- **Connection establishment**: Client first establishes SSH transport connection (RFC 4253), invokes "ssh-userauth" (RFC 4252), then "ssh-connection" (RFC 4254) to open a "session" channel.
- **Subsystem invocation**: User/application invokes NETCONF as SSH subsystem called "netconf".
- **Handling extraneous messages**: Implementations **MUST** skip over extraneous messages by searching for an 'xml' start directive, which **MUST** be followed by a `<hello>` element in the 'NETCONF' namespace.
- **Default port**: NETCONF servers **MUST** default to providing access to "netconf" subsystem only when SSH session is established using IANA-assigned TCP port <830>. Servers **SHOULD** be configurable to allow access over other ports.
- **Example command**: `ssh -s server.example.org -p <830> netconf` (with -s option to invoke subsystem).

### 3.1. Capabilities Exchange
- **Server** **MUST** indicate capabilities by sending an XML document containing a `<hello>` element as soon as NETCONF session is established.
- **Client** **MUST** send an XML document containing a `<hello>` element as first XML document after session establishment.
- **Chunk framing**: Both client and server **MUST** send the character sequence `]]>]]>` after each XML document to identify end of document.

## 4. Using NETCONF over SSH
- Manager sends complete XML documents containing `<rpc>` elements; agent responds with `<rpc-reply>` elements.
- Example provided (informative).

## 5. Exiting the NETCONF Subsystem
- Exiting NETCONF is accomplished using the `<close-session>` operation.
- Agent processes RPC messages in order received. When agent processes a `<close-session>` command, the agent **shall** respond and close the SSH session channel. The agent **MUST NOT** process any RPC commands received on the current session after the `<close-session>` command.

## 6. Security Considerations
- **Authentication**: Identity of server **MUST** be verified and authenticated by client according to local policy before sending/receiving any configuration/state data. Identity of client **MUST** also be verified and authenticated by server.
- Neither side should establish connection with unknown, unexpected, or incorrect identity.
- **Encryption**: Use only over communications channels providing strong encryption (this mapping provides support for strong encryption and authentication).
- **Port filtering**: Default port allows identification/filtering but also easier identification by attackers.
- **Configuration warning**: Allowing access over other ports without corresponding firewall changes may unintentionally expose the subsystem.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Implementations MUST skip over extraneous messages by searching for 'xml' start directive followed by `<hello>` element in NETCONF namespace. | MUST | Section 3 |
| R2 | NETCONF servers MUST default to providing access to "netconf" SSH subsystem only when SSH session is established using IANA-assigned TCP port <830>. | MUST | Section 3 |
| R3 | Servers SHOULD be configurable to allow access to netconf SSH subsystem over other ports. | SHOULD | Section 3 |
| R4 | Server MUST indicate capabilities by sending `<hello>` element as soon as NETCONF session is established. | MUST | Section 3.1 |
| R5 | Client MUST send `<hello>` element as first XML document after NETCONF session is established. | MUST | Section 3.1 |
| R6 | Both client and server MUST send `]]>]]>` after each XML document. | MUST | Section 3.1 |
| R7 | Agent shall respond and close SSH session channel upon processing `<close-session>` command. | SHALL | Section 5 |
| R8 | Agent MUST NOT process any RPC commands received after `<close-session>`. | MUST NOT | Section 5 |
| R9 | Identity of server MUST be verified and authenticated by client according to local policy before sending/receiving any configuration/state data. | MUST | Section 6 |
| R10 | Identity of client MUST be verified and authenticated by server according to local policy. | MUST | Section 6 |

## Informative Annexes (Condensed)
- **Example Commands and XML exchanges**: Used throughout to illustrate capability exchange, RPC interactions, and session closing. Do not add normative requirements beyond the documented MUST/SHOULD statements.
- **IANA Considerations**: TCP port 830 assigned as default for NETCONF over SSH; "netconf" registered as SSH Service Name.
- **Acknowledgements**: Document written using xml2rfc; input from NETCONF design team and reviewers.
- **References**: Normative references include RFC 2119, 4250, 4252, 4253, 4254, 4721. Informative reference is RFC 2629.