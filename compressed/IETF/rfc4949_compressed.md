# RFC 4949: Internet Security Glossary, Version 2
**Source**: IETF (Network Working Group) | **Version**: 2 | **Date**: August 2007 | **Type**: Informational  
**Author**: R. Shirey | **Obsoletes**: RFC 2828 | **Category**: Informational  
**Original**: https://www.rfc-editor.org/rfc/rfc4949

## Scope (Summary)
This glossary provides definitions, abbreviations, and explanations of terminology for information system security, aiming to improve the clarity and consistency of written materials generated in the Internet Standards Process (RFC 2026). It offers recommendations (using RFC 2119 language but as personal opinions of the author) to use terms consistently, plainly, and without vendor or technology bias.

## Normative References
- RFC 2026: The Internet Standards Process
- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- RFC 2828 (obsoleted): Internet Security Glossary, Version 1

## Definitions and Abbreviations
*(Entries are marked with type: I = Recommended Internet origin, N = Recommended non-Internet, O = Not recommended but noted, D = Deprecated.)*

- **$ *-property** (N) Synonym for "confinement property" in Bell-LaPadula model. Pronunciation: star property.
- **$ 3DES** (N) See: Triple Data Encryption Algorithm.
- **$ A1 computer system** (O) /TCSEC/ See Tutorial under "Trusted Computer System Evaluation Criteria". (Compare: beyond A1.)
- **$ AA** (D) See: Deprecated Usage under "attribute authority". IDOCs SHOULD NOT use "AA" unless first defined.
- **$ ABA Guidelines** (N) Legal framework for digital signatures and certificates.
- **$ Abstract Syntax Notation One (ASN.1)** (N) Standard for describing data objects. IDOCs SHOULD use "ASN.1" narrowly for the notation; MAY use broadly when context clear.
- **$ ACC** (I) See: access control center.
- **$ acceptable risk** (I) Risk understood and tolerated by system stakeholders.
- **$ access** (I) 1a. Ability to communicate with or interact with a system. 1b. (O) Opportunity to use an information system resource. 2. (O) /formal model/ Interaction between subject and object resulting in information flow.
- **$ Access Certificate for Electronic Services (ACES)** (O) U.S. Government PKI.
- **$ access control** (I) 1. Protection against unauthorized access. 2. Process regulating use of system resources. 3. /formal model/ Limitations on subject-object interactions. 4. (O) Prevention of unauthorized use of a resource. 5. (O) /U.S. Government/ Physical/electronic/human controls for SCIF.
- **$ access control center (ACC)** (I) Server for access control decisions.
- **$ access control list (ACL)** (I) Mechanism enumerating entities and allowed access modes.
- **$ access control matrix** (I) Rectangular array with subjects rows and objects columns.
- **$ access control service** (I) Protects against unauthorized use of resources.
- **$ access level** (D) 1. Synonym for classification level. 2. Synonym for clearance level. IDOCs SHOULD NOT use these definitions.
- **$ access list** (I) Roster of authorized persons for physical security.
- **$ access mode** (I) Type of operation (read, write, etc.) subject can perform on object.
- **$ access policy** (I) A kind of security policy.
- **$ access profile** (O) Synonym for capability list. IDOCs SHOULD state a definition.
- **$ access right** (I) Synonym for authorization emphasizing possession.
- **$ accountability** (I) Property ensuring actions can be traced to an entity.
- **$ accounting** See: COMSEC accounting.
- **$ accounting legend code (ALC)** (O) Numeric system for COMSEC material controls.
- **$ accreditation** (N) Administrative action approving system operation with safeguards.
- **$ accreditation boundary** (O) Synonym for security perimeter.
- **$ accreditor** (N) Management official authorized to accredit a system.
- **$ ACES** (O) See: Access Certificate for Electronic Services.
- **$ ACL** (I) See: access control list.
- **$ acquirer** (O) /SET/ Financial institution that processes payment card authorizations.
- **$ activation data** (N) Secret data required to access a cryptographic module.
- **$ active attack** (I) Attack that alters system resources or affects operation.
- **$ active content** (I) Executable software bound to a file that executes automatically.
- **$ active user** (I) See secondary definition under "system user".
- **$ active wiretapping** (I) Attempts to alter data in communication.
- **$ add-on security** (N) Retrofit of protection mechanisms after system is operational.
- **$ adequate security** (O) Security commensurate with risk and magnitude of harm.
- **$ administrative security** (I) Management procedures to prevent unauthorized access.
- **$ administrator** (O) Person responsible for configuring and maintaining TOE.
- **$ Advanced Encryption Standard (AES)** (N) U.S. standard symmetric block cipher (Rijndael).
- **$ adversary** (I) Entity that attacks or threatens a system.
- **$ AES** (N) See: Advanced Encryption Standard.
- **$ Affirm** (O) Formal methodology for software verification (USC/ISI).
- **$ aggregation** (I) Collection of items classified higher than any individual.
- **$ AH** (I) See: Authentication Header.
- **$ air gap** (I) Interface without physical connection; data transferred manually.
- **$ ALC** (O) See: accounting legend code.
- **$ algorithm** (I) Finite set of step-by-step instructions for computation.
- **$ alias** (I) Name used in place of real name for anonymity or masquerade.
- **$ Alice and Bob** (I) Parties used to illustrate bipartite security protocols.
- **$ American National Standards Institute (ANSI)** (N) Administrator of U.S. private-sector voluntary standards.
- **$ American Standard Code for Information Interchange (ASCII)** (N) 7-bit character encoding.
- **$ Anderson report** (O) 1972 study of computer security by James P. Anderson.
- **$ anomaly detection** (I) Intrusion detection based on deviation from normal behavior.
- **$ anonymity** (I) Condition of unknown or concealed identity.
- **$ anonymizer** (I) Proxy service providing anonymity and privacy for clients.
- **$ anonymous credential** (D) Credential that authenticates attribute without revealing identity. IDOCs SHOULD NOT use; instead use attribute certificate, organizational certificate, or persona certificate.
- **$ anonymous login** (I) Access feature allowing public access without pre-established account.
- **$ ANSI** (N) See: American National Standards Institute.
- **$ anti-jam** (N) Measures ensuring reception despite jamming.
- **$ apex trust anchor** (N) Trust anchor superior to all others.
- **$ API** (I) See: application programming interface.
- **$ APOP** (I) See: POP3 APOP.
- **$ Application Layer** See: Internet Protocol Suite, OSIRM.
- **$ application program** (I) Program performing function directly for user.
- **$ architecture** (I) See: security architecture, system architecture.
- **$ archive** (I) 1a. Long-term data storage for historical purposes. 1b. Verb meaning to store data.
- **$ ARPANET** (I) Pioneer packet-switched network (1969-1990).
- **$ ASCII** (N) See: American Standard Code for Information Interchange.
- **$ ASN.1** (N) See: Abstract Syntax Notation One.
- **$ asset** (I) System resource required to be protected.
- **$ association** (I) Cooperative relationship between system entities.
- **$ assurance** See: security assurance.
- **$ assurance level** (N) Rank on scale judging confidence that TOE fulfills security requirements.
- **$ asymmetric cryptography** (I) Branch using key pair (public and private) for two counterpart operations.
- **$ asymmetric key** (I) Key used in asymmetric cryptography.
- **$ ATIS** (N) See "Alliance for Telecommunications Industry Solutions" under "ANSI".
- **$ attack** (I) 1. Intentional act to evade security services and violate policy. 2. Method or technique used in assault.
- **$ attack potential** (I) Perceived likelihood of success of an attack.
- **$ attack sensing, warning, and response** (I) Services cooperating with audit to detect and react to threat actions.
- **$ attack tree** (I) Branching data structure representing potential approaches to penetrate security.
- **$ attribute** (N) Information of a particular type concerning an entity or object.
- **$ attribute authority (AA)** (N) 1. CA that issues attribute certificates. 2. (O) Authority that assigns privileges via attribute certificates.
- **$ attribute certificate** (I) Digital certificate binding descriptive data (not public key) to subject.
- **$ audit** See: security audit.
- **$ audit log** (I) Synonym for "security audit trail".
- **$ audit service** (I) Records information for accountability.
- **$ audit trail** (I) See: security audit trail.
- **$ AUTH** (I) See: POP3 AUTH.
- **$ authenticate** (I) Verify attribute value claimed by an entity. IDOCs SHOULD NOT use for proving data unchanged, verifying digital signatures, or establishing certificate validity.
- **$ authentication** (I) Process of verifying a claim of attribute value.
- **$ authentication code** (D) IDOCs SHOULD NOT use as synonym for checksum.
- **$ authentication exchange** (I) Mechanism to verify identity via information exchange.
- **$ Authentication Header (AH)** (I) IPsec protocol providing connectionless data integrity and origin authentication.
- **$ authentication information** (I) Information used to verify identity.
- **$ authentication service** (I) Verifies identity claimed by entity.
- **$ authenticity** (I) Property of being genuine and verifiable.
- **$ authority** (D) IDOCs SHOULD NOT use as synonym for AA, CA, RA.
- **$ authority certificate** (D) IDOCs SHOULD NOT use; ambiguous.
- **$ Authority Information Access extension** (I) PKIX extension for CA information access.
- **$ authorization** (I) 1a. Approval granted to access system resource. 1b. Process of granting approval.
- **$ authorization credential** (I) See /access control/ under "credential".
- **$ authorize** (I) Grant authorization.
- **$ authorized user** (I) Entity that has received authorization for resource.
- **$ automated information system** See: information system.
- **$ availability** (I) Property of being accessible/useful upon demand.
- **$ availability service** (I) Protects system to ensure availability.
- **$ avoidance** (I) See secondary definition under "security".
- **$ B1, B2, or B3 computer system** (O) /TCSEC/ See Tutorial under "Trusted Computer System Evaluation Criteria".
- **$ back door** (I) 1. Feature providing alternative access, unintentional or deliberate. 2. Cryptography feature enabling easy breaking.
- **$ back up** (I) Create reserve copy.
- **$ backup** (I) Alternate means for function despite resource loss.
- **$ bagbiter** (D) Slang term; IDOCs SHOULD NOT use.
- **$ baggage** (O) /SET/ Opaque encrypted tuple; IDOCs SHOULD NOT use except as "SET(trademark) baggage".
- **$ baked-in security** (D) Inclusion of security early in lifecycle; IDOCs SHOULD NOT use due to cultural metaphor.
- **$ bandwidth** (I) Total width of frequency band.
- **$ bank identification number (BIN)** (O) 1. Digits identifying issuing bank. 2. /SET/ First six digits of PAN.
- **$ Basic Encoding Rules (BER)** (I) Standard for representing ASN.1 data types as octet strings.
- **$ Basic Security Option** (I) See secondary definition under "IPSO".
- **$ bastion host** (I) Strongly protected host in firewall, directly accessible from outside.
- **$ BBN Technologies Corp. (BBN)** (O) Company that built ARPANET.
- **$ BCA** (O) See: brand certification authority.
- **$ BCR** (O) See: BLACK/Crypto/RED.
- **$ BCI** (O) See: brand CRL identifier.
- **$ Bell-LaPadula model** (N) Formal model for confidentiality policy in multilevel-secure systems.
- **$ benign** (N) Condition of cryptographic data not compromiseable by human access.
- **$ benign fill** (N) Process of keying material generation and distribution without human exposure.
- **$ BER** (I) See: Basic Encoding Rules.
- **$ beyond A1** (O) Level beyond highest TCSEC criteria.
- **$ Biba integrity** (N) Synonym for "source integrity".
- **$ Biba model** (N) Formal integrity model for multilevel-secure systems.
- **$ billet** (N) Personnel position that may be filled by one person.
- **$ BIN** (O) See: bank identification number.
- **$ bind** (I) Inseparably associate by applying security mechanism.
- **$ biometric authentication** (I) Method using digitized measurements of physical/behavioral characteristics.
- **$ birthday attack** (I) Class of attacks exploiting birthday paradox on cryptographic functions.
- **$ bit** (I) Binary digit; smallest unit of information storage.
- **$ bit string** (I) Sequence of bits.
- **$ BLACK** (N) 1. Designation for ciphertext-only data and equipment. 2. (O) /U.S. Government/ Designation for encrypted national security information.
- **$ BLACK/Crypto/RED (BCR)** (N) First network encryption system supporting TCP/IP and using DES.
- **$ BLACK key** (N) Key protected with key-encrypting key.
- **$ BLACKER** (O) End-to-end encryption system for datagrams at OSIRM Layer 3.
- **$ blind attack** (I) Attack not requiring attacker to receive data from victim.
- **$ block** (I) Finite length bit string.
- **$ block cipher** (I) Encryption algorithm processing fixed-size blocks.
- **$ Blowfish** (N) Symmetric block cipher with variable key length.
- **$ brain-damaged** (D) Slang; IDOCs SHOULD NOT use.
- **$ brand** (I) Distinctive mark or name identifying product or business.
- **$ brand certification authority (BCA)** (O) /SET/ CA owned by payment card brand.
- **$ brand CRL identifier (BCI)** (O) /SET/ Digitally signed list of CA names for CRL processing.
- **$ break** (I) Successfully perform cryptanalysis.
- **$ Brewer-Nash model** (N) Model to enforce Chinese Wall policy.
- **$ bridge** (I) Gateway for OSIRM Layer 2 traffic.
- **$ bridge CA** (I) PKI consisting of a CA that cross-certifies with others.
- **$ British Standard 7799** (N) Code of practice for securing information systems.
- **$ browser** (I) Client program retrieving and displaying Web information.
- **$ brute force** (I) Cryptanalysis technique trying large number of possibilities.
- **$ BS7799** (N) See: British Standard 7799.
- **$ buffer overflow** (I) Attack exploiting missing bounds checking.
- **$ buffer zone** (I) Neutral internetwork segment connecting segments with different security policies.
- **$ bulk encryption** (I) 1. Encryption of multiple channels by aggregating into single path. 2. (O) Simultaneous encryption of all channels.
- **$ bulk key** (D) IDOCs SHOULD NOT use; instead use "symmetric key".
- **$ bulk keying material** (N) Large quantities of keying data.
- **$ bump-in-the-stack** (I) Implementation placing security mechanism inside the protected system.
- **$ bump-in-the-wire** (I) Implementation placing security mechanism outside.
- **$ business-case analysis** (N) Extended cost-benefit analysis including security factors.
- **$ byte** (I) Fundamental unit of storage; usually eight bits.
- **$ C field** (D) See: Compartments field.
- **$ C1 or C2 computer system** (O) /TCSEC/ See Tutorial under "Trusted Computer System Evaluation Criteria".
- **$ CA** (I) See: certification authority.
- **$ CA certificate** (D) IDOCs SHOULD NOT use ambiguous definition; provide technical definition.
- **$ CA domain** (N) /PKI/ Set of CA and its subjects.
- **$ Caesar cipher** (I) Substitution cipher shifting characters.
- **$ call back** (I) Authentication technique using disconnection and reconnection on authorized number.
- **$ CAM** (O) See: Certificate Arbitrator Module.
- **$ CANEWARE** (O) End-to-end encryption system for datagrams at OSIRM Layer 3.
- **$ capability list** (I) Mechanism implementing access control per entity.
- **$ capability token** (I) Token giving bearer right to access resource.
- **$ Capability Maturity Model (CMM)** (N) Method for judging software process maturity.
- **$ CAPI** (I) See: cryptographic application programming interface.
- **$ CAPSTONE** (N) Integrated microcircuit implementing SKIPJACK, KEA, DSA, SHA, etc.
- **$ card** See: cryptographic card, FORTEZZA, etc.
- **$ cardholder** (I) Entity to whom card is issued.
- **$ cardholder certificate** (O) /SET/ Digital certificate for cardholder.
- **$ cardholder certification authority (CCA)** (O) /SET/ CA issuing certificates to cardholders.
- **$ CAST** (N) Family of symmetric encryption algorithms.
- **$ category** (I) Grouping of sensitive information with non-hierarchical label.
- **$ CAW** (N) See: certification authority workstation.
- **$ CBC** (N) See: cipher block chaining.
- **$ CCA** (O) See: cardholder certification authority.
- **$ CCEP** (O) See: Commercial COMSEC Endorsement Program.
- **$ CCI** (O) See: Controlled Cryptographic Item.
- **$ CCITT** (N) Acronym for ITU-T predecessor.
- **$ CCM** (N) See: Counter with Cipher Block Chaining-Message Authentication Code.
- **$ CERIAS** (O) Center for Education and Research in Information Assurance and Security.
- **$ CERT** (I) See: computer emergency response team.
- **$ certificate** (I) 1. General: document attesting to truth. 2. General security: capability token or digital certificate. 3. /PKI/ attribute certificate or public-key certificate.
- **$ Certificate Arbitrator Module (CAM)** (O) Software module for certificate validation requests.
- **$ certificate authority** (D) Synonym for "certification authority". IDOCs SHOULD NOT use.
- **$ certificate chain** (D) IDOCs SHOULD NOT use; use "certification path".
- **$ certificate chain validation** (D) IDOCs SHOULD NOT use; use "certificate validation" or "path validation".
- **$ certificate creation** (I) Act of setting certificate fields and signing.
- **$ certificate expiration** (I) Event when certificate ceases to be valid after lifetime.
- **$ certificate extension** (I) See: extension.
- **$ certificate holder** (D) IDOCs SHOULD NOT use as synonym for subject.
- **$ certificate management** (I) Functions CA performs during certificate lifecycle.
- **$ certificate management authority (CMA)** (D) IDOCs SHOULD NOT use; use CA or RA.
- **$ certificate owner** (D) IDOCs SHOULD NOT use as synonym for subject.
- **$ certificate path** (D) Invalid; use "certification path".
- **$ certificate policy** (I) Named set of rules indicating applicability of certificate to community.
- **$ certificate policy qualifier** (I) Information included in certificatePolicies extension.
- **$ certificate profile** (I) Specification of format and semantics of certificates for specific context.
- **$ certificate reactivation** (I) Returning revoked certificate to valid state.
- **$ certificate rekey** (I) Issuing new certificate with new public key.
- **$ certificate renewal** (I) Extending validity period of existing certificate.
- **$ certificate request** (D) Use "certification request".
- **$ certificate revocation** (I) Event when CA declares certificate invalid.
- **$ certificate revocation list (CRL)** (I) Data structure enumerating invalidated certificates.
- **$ certificate revocation tree** (N) Alternative mechanism for distributing revocation notices.
- **$ certificate serial number** (I) Unique integer assigned by issuer.
- **$ certificate status authority** (D) IDOCs SHOULD NOT use; use "certificate status responder" or "OCSP server".
- **$ certificate status responder** (N) Online server providing authenticated certificate status.
- **$ certificate update** (I) Changing non-key data in certificate.
- **$ certificate user** (I) Entity depending on validity of certificate information.
- **$ certificate validation** (I) Process establishing trust in certificate assertions.
- **$ certification** (I) 1. Information system: comprehensive evaluation for accreditation. 2. Digital certificate: vouching for binding. 3. PKI: vouching for ownership of public key.
- **$ certification authority (CA)** (I) Entity that issues digital certificates and vouches for binding.
- **$ certification authority workstation (CAW)** (N) Computer system enabling CA functions.
- **$ certification hierarchy** (I) Tree-structured topology of CA relationships.
- **$ certification path** (I) Linked sequence of certificates enabling verification.
- **$ certification policy** (D) IDOCs SHOULD NOT use; use "certificate policy" or "CPS".
- **$ certification practice statement (CPS)** (I) Statement of practices CA employs in issuing certificates.
- **$ certification request** (I) Algorithm-independent transaction format for certification.
- **$ certify** (I) 1. Issue certificate vouching for binding. 2. Act of CA verifying data.
- **$ CFB** (N) See: cipher feedback.
- **$ chain** (D) See: trust chain.
- **$ Challenge Handshake Authentication Protocol (CHAP)** (I) Authentication method using challenge and keyed hash.
- **$ challenge-response** (I) Authentication process verifying identity via response to challenge.
- **$ Challenge-Response Authentication Mechanism (CRAM)** (I) /IMAP4/ Mechanism using keyed hash.
- **$ channel** (I) 1. Information transfer path. 2. (O) Subdivision of physical medium.
- **$ channel capacity** (I) Total capacity of link in bits per second.
- **$ CHAP** (I) See: Challenge Handshake Authentication Protocol.
- **$ checksum** (I) Value computed by function dependent on data, used to detect changes.
- **$ Chinese wall policy** (I) Policy to prevent conflict of interest.
- **$ chosen-ciphertext attack** (I) Cryptanalysis using chosen ciphertext.
- **$ chosen-plaintext attack** (I) Cryptanalysis using chosen plaintext.
- **$ CIAC** (O) See: Computer Incident Advisory Capability.
- **$ CIK** (N) See: cryptographic ignition key.
- **$ cipher** (I) Cryptographic algorithm for encryption/decryption.
- **$ cipher block chaining (CBC)** (N) Block cipher mode chaining ciphertext blocks.
- **$ cipher feedback (CFB)** (N) Block cipher mode operating on variable-length segments.
- **$ cipher text** (I) Data transformed by encryption, no longer intelligible.
- **$ ciphertext** (I) Adjective form; commonly used.
- **$ ciphertext auto-key (CTAK)** (D) Obsolete term; use standard mode terms.
- **$ ciphertext-only attack** (I) Cryptanalysis using only intercepted ciphertext.
- **$ ciphony** (O) Encryption of audio.
- **$ CIPSO** (I) See: Common IP Security Option.
- **$ CKL** (I) See: compromised key list.
- **$ Clark-Wilson model** (N) Integrity model for commercial use.
- **$ class 2,3,4,5** (O) DoD assurance levels for PKI.
- **$ Class A1, B3, B2, B1, C2, C1 computer system** (O) /TCSEC/ See Tutorial.
- **$ classification** (I) 1. Grouping of classified information with hierarchical label. 2. Authorized process of assigning security level.
- **$ classification label** (I) Security label indicating harm from disclosure.
- **$ classification level** (I) Hierarchical level of protection against disclosure.
- **$ classified** (I) Information required to receive data confidentiality service and security label.
- **$ classify** (I) Officially designate as classified and assign security level.
- **$ clean system** (I) System with freshly installed trusted software.
- **$ clear** (D) Synonym for "erase"; IDOCs SHOULD NOT use.
- **$ clear text** (I) Data not encrypted, intelligible.
- **$ clearance** See: security clearance.
- **$ clearance level** (I) Security level to which clearance authorizes access.
- **$ cleartext** (I) Adjective form. IDOCs SHOULD NOT use as synonym for plaintext.
- **$ CLEF** (N) See: commercially licensed evaluation facility.
- **$ client** (I) Entity requesting service from server.
- **$ client-server system** (I) Distributed system with clients and servers.
- **$ CLIPPER** (N) Integrated circuit implementing SKIPJACK with key escrow.
- **$ closed security environment** (O) Environment with cleared developers and configuration control.
- **$ CMA** (D) See: certificate management authority.
- **$ CMAC** (N) Cipher-based message authentication code.
- **$ CMCS** (O) See: COMSEC Material Control System.
- **$ CMM** (N) See: Capability Maturity Model.
- **$ CMS** (I) See: Cryptographic Message Syntax.
- **$ code** (I) 1. System of symbols for representation. 2. Encryption algorithm based on substitution. 3. Algorithm for shortening messages. 4. Writing computer software.
- **$ code book** (I) Document with plaintext/ciphertext equivalents.
- **$ code signing** (I) Mechanism using digital signature for software integrity and authentication.
- **$ code word** (O) Single word used as security label.
- **$ COI** (I) See: community of interest.
- **$ cold start** (N) Procedure for initial keying.
- **$ collateral information** (O) Classified information not requiring SAP.
- **$ color change** (I) Purging and changing processing periods.
- **$ Commercial COMSEC Evaluation Program (CCEP)** (O) NSA-industry relationship for type 1/2 products.
- **$ commercially licensed evaluation facility (CLEF)** (N) Organization approved to evaluate security.
- **$ Committee on National Security Systems (CNSS)** (O) U.S. Government committee.
- **$ Common Criteria for Information Technology Security** (N) Standard for evaluating IT security.
- **$ Common IP Security Option (CIPSO)** (I) See secondary definition under "IPSO".
- **$ common name** (N) Character string part of X.500 DN.
- **$ communications cover** (N) Concealing communication patterns.
- **$ communication security (COMSEC)** (I) Measures implementing security in communication systems.
- **$ community of interest (COI)** (I) Set of entities under common security policy or collaborating.
- **$ community risk** (N) Probability of vulnerability exploitation within population.
- **$ community string** (I) Cleartext password in SNMPv1/v2.
- **$ compartment** (I) Grouping requiring special access controls beyond classification.
- **$ compartmented security mode** (N) Mode where some users lack clearance for non-hierarchical categories.
- **$ Compartments field** (I) 16-bit field in IP security option.
- **$ component** See: system component.
- **$ compression** (I) Process of minimizing data representation.
- **$ compromise** See: data compromise, security compromise.
- **$ compromise recovery** (I) Regaining secure state after compromise.
- **$ compromised key list (CKL)** (N) List of keys possibly disclosed/altered.
- **$ COMPUSEC** (I) See: computer security.
- **$ computer emergency response team (CERT)** (I) Organization studying INFOSEC and providing incident response.
- **$ Computer Incident Advisory Capability (CIAC)** (O) U.S. DOE CSIRT.
- **$ computer network** (I) Collection of host computers with subnetwork.
- **$ computer platform** (I) Combination of hardware and operating system.
- **$ computer security (COMPUSEC)** (I) Measures to implement security services in computer systems.
- **$ computer security incident response team (CSIRT)** (I) Organization coordinating incident response.
- **$ computer security object** (I) Definition of resource/tool/mechanism for security.
- **$ Computer Security Objects Register (CSOR)** (N) NIST catalog for security objects.
- **$ computer system** (I) Synonym for information system or component.
- **$ Computers At Risk** (O) 1991 NAS report on computer security.
- **$ COMSEC** (I) See: communication security.
- **$ COMSEC account** (O) Administrative entity for COMSEC material accountability.
- **$ COMSEC accounting** (O) Process of tracking and controlling COMSEC material.
- **$ COMSEC boundary** (N) Perimeter of critical COMSEC components.
- **$ COMSEC custodian** (O) Individual responsible for COMSEC material.
- **$ COMSEC material** (N) Items for securing communications or information.
- **$ COMSEC Material Control System (CMCS)** (O) Distribution and control system.
- **$ confidentiality** See: data confidentiality.
- **$ concealment system** (O) Method hiding sensitive information in irrelevant data.
- **$ configuration control** (I) Process regulating changes to system.
- **$ confinement property** (N) Property of system subject write access only if classification dominates clearance.
- **$ constraint** (I) Limitation on function of identity, role, or privilege.
- **$ content filter** (I) Software preventing access to certain Web servers.
- **$ contingency plan** (I) Plan for emergency, backup, and recovery.
- **$ control zone** (O) Space around equipment under physical and technical control.
- **$ controlled access protection** (O) TCSEC C2 level criteria.
- **$ controlled cryptographic item (CCI)** (O) Unclassified cryptographic equipment with special controls.
- **$ controlled interface** (I) Mechanism for adjudicating security policies between interconnected systems.
- **$ controlled security mode** (D) Obsolete mode; IDOCs SHOULD NOT use.
- **$ controlling authority** (O) Official directing cryptonet operation.
- **$ cookie** (I) 1. HTTP: data exchanged for state. 2. IPsec: data object to prevent DoS.
- **$ Coordinated Universal Time (UTC)** (N) Derived from TAI by adding leap seconds.
- **$ correction** (I) System change to reduce risk of violation reoccurrence.
- **$ correctness** (I) Property guaranteed by formal verification.
- **$ correctness integrity** (I) Property that information is accurate and consistent. IDOCs SHOULD NOT use without definition.
- **$ correctness proof** (I) Mathematical proof of consistency between specification and implementation.
- **$ corruption** (I) Threat action undesirably altering system operation.
- **$ counter** (N) Noun: counter mode. (I) Verb: countermeasure.
- **$ counter-countermeasure** (I) Action by attacker to offset defensive countermeasure.
- **$ counter mode (CTR)** (N) Block cipher mode ensuring each encrypted block is unique.
- **$ Counter with Cipher Block Chaining-Message Authentication Code (CCM)** (N) Block cipher mode providing confidentiality and authentication.
- **$ countermeasure** (I) Action opposing threat, vulnerability, or attack.
- **$ country code** (I) ISO 3166 identifier for a nation.
- **$ Courtney's laws** (N) Principles for system security management.
- **$ covert action** (I) Operation concealing operator identity.
- **$ covert channel** (I) Unintended channel transferring information violating policy.
- **$ covert storage channel** (I) Channel via writing and reading storage locations.
- **$ covert timing channel** (I) Channel via modulating system resource use to affect response time.
- **$ CPS** (I) See: certification practice statement.
- **$ cracker** (I) Person breaking security to gain unauthorized access.
- **$ CRAM** (I) See: Challenge-Response Authentication Mechanism.
- **$ CRC** (I) See: cyclic redundancy check.
- **$ credential** (I) 1. Identifier credential: portable association of identifier and authentication information. 2. Authorization credential: portable association of identifier and authorizations.
- **$ critical** (I) 1. Condition where denial of access jeopardizes primary function. 2. (N) Extension that must not be ignored.
- **$ critical information infrastructure** (I) Systems vital to nation.
- **$ CRL** (I) See: certificate revocation list.
- **$ CRL distribution point** (I) See: distribution point.
- **$ CRL extension** (I) See: extension.
- **$ cross-certificate** (I) Public-key certificate issued by CA in one PKI to CA in another.
- **$ cross-certification** (I) Act of one CA issuing certificate to another CA.
- **$ cross-domain solution** (D) 1. Synonym for "guard". 2. Process/subsystem for differing security domains.
- **$ cryptanalysis** (I) Science of analyzing cryptographic systems to break/circumvent protection.
- **$ crypto, CRYPTO** (N) Prefix meaning cryptographic. IDOCs MAY use when part of listed term.
- **$ cryptographic** (I) Adjective referring to cryptography.
- **$ cryptographic algorithm** (I) Algorithm using cryptography.
- **$ cryptographic application programming interface (CAPI)** (I) Interface for application accessing cryptographic services.
- **$ cryptographic association** (I) Security association using cryptography.
- **$ cryptographic boundary** (I) Limit of cryptographic module.
- **$ cryptographic card** (I) Token in form of smart/PC card.
- **$ cryptographic component** (I) Generic term for system component involving cryptography.
- **$ cryptographic hash** (I) See secondary definition under "hash function".
- **$ cryptographic ignition key (CIK)** (N) Physical token to store/protect keys and activation data.
- **$ cryptographic key** (I) See: key.
- **$ Cryptographic Message Syntax (CMS)** (I) Encapsulation syntax for digital signatures, hashes, encryption.
- **$ cryptographic module** (I) Set of hardware/software/firmware implementing cryptographic logic.
- **$ cryptographic system** (I) Set of algorithms and key management processes.
- **$ cryptographic token** (I) Portable physical device storing cryptographic information.
- **$ cryptography** (I) Mathematical science of transforming data for security.
- **$ Cryptoki** (N) CAPI defined in PKCS #11.
- **$ cryptology** (I) Science of secret communication including cryptography and cryptanalysis.
- **$ cryptonet** (I) Network of entities sharing secret key.
- **$ cryptoperiod** (I) Time span a key value is authorized for use.
- **$ cryptosystem** (I) Contraction of cryptographic system.
- **$ cryptovariable** (D) Synonym for "key". IDOCs SHOULD NOT use.
- **$ CSIRT** (I) See: computer security incident response team.
- **$ CSOR** (N) See: Computer Security Objects Register.
- **$ CTAK** (D) See: ciphertext auto-key.
- **$ CTR** (N) See: counter mode.
- **$ cut-and-paste attack** (I) Active attack replacing sections of ciphertext.
- **$ cyclic redundancy check (CRC)** (I) Checksum algorithm for accidental changes.
- **$ DAC** (N) See: Data Authentication Code, discretionary access control.
- **$ daemon** (I) Program running without associated user.
- **$ dangling threat** (O) Threat without corresponding vulnerability.
- **$ dangling vulnerability** (O) Vulnerability without corresponding threat.
- **$ DASS** (I) See: Distributed Authentication Security Service.
- **$ data** (I) Information in specific representation.
- **$ Data Authentication Algorithm** (N) ANSI standard keyed hash function equivalent to DES CBC.
- **$ Data Authentication Code** (N) U.S. Government standard checksum via Data Authentication Algorithm.
- **$ data compromise** (I) Security incident with potential unauthorized access.
- **$ data confidentiality** (I) Property that data is not disclosed without authorization.
- **$ data confidentiality service** (I) Security service protecting against unauthorized disclosure.
- **$ Data Encryption Algorithm (DEA)** (N) Symmetric block cipher defined in DES.
- **$ data encryption key (DEK)** (I) Key used to encipher application data.
- **$ Data Encryption Standard (DES)** (N) U.S. Government standard specifying DEA.
- **$ data integrity** (I) Property that data has not been changed/destroyed/lost.
- **$ data integrity service** (I) Security service protecting against unauthorized changes.
- **$ data origin authentication** (I) Corroboration that source of data is as claimed.
- **$ data origin authentication service** (I) Security service verifying identity of original source.
- **$ data owner** (N) Organization with final authority for specified information.
- **$ data privacy** (D) IDOCs SHOULD NOT use; use data confidentiality or privacy.
- **$ data recovery** (I) 1. Learning plaintext from ciphertext. 2. Restoring information after damage.
- **$ data security** (I) Protection from disclosure, alteration, destruction, loss.
- **$ datagram** (I) Self-contained independent data entity.
- **$ datagram confidentiality service** (I) Data confidentiality service per datagram.
- **$ datagram integrity service** (I) Data integrity service per datagram.
- **$ DEA** (N) See: Data Encryption Algorithm.
- **$ deception** (I) Circumstance causing entity to receive false data as true.
- **$ decipher** (D) Synonym for decrypt; IDOCs SHOULD NOT use.
- **$ decipherment** (D) Synonym for decryption; IDOCs SHOULD NOT use.
- **$ declassification** (I) Authorized process of removing classification.
- **$ declassify** (I) Officially remove security level designation.
- **$ decode** (I) Convert encoded data to original form. IDOCs SHOULD NOT use as synonym for decrypt.
- **$ decrypt** (I) Cryptographically restore ciphertext to plaintext.
- **$ decryption** (I) Reverse process of encryption.
- **$ dedicated security mode** (I) Mode where all users have all necessary authorizations and need-to-know.
- **$ default account** (I) Predefined login account in manufactured system.
- **$ defense in depth** (N) Mutually supporting defense positions to absorb attack.
- **$ Defense Information Infrastructure (DII)** (O) U.S. DoD shared information system.
- **$ Defense Information Systems Network (DISN)** (O) U.S. DoD consolidated telecommunications infrastructure.
- **$ degauss** (N) Apply magnetic field to permanently remove data.
- **$ degausser** (N) Device to degauss.
- **$ DEK** (I) See: data encryption key.
- **$ delay** (I) See stream integrity service.
- **$ deletion** (I) See stream integrity service.
- **$ deliberate exposure** (I) Threat action of intentional release.
- **$ delta CRL** (I) Partial CRL with only new revocations.
- **$ demilitarized zone (DMZ)** (D) Synonym for buffer zone; IDOCs SHOULD NOT use.
- **$ denial of service** (I) Prevention of authorized access or delaying operations.
- **$ DES** (N) See: Data Encryption Standard.
- **$ designated approving authority (DAA)** (O) Synonym for accreditor.
- **$ detection** (I) See security.
- **$ deterrence** (I) See security.
- **$ dictionary attack** (I) Brute-force attack trying all words in list.
- **$ Diffie-Hellman** (N) Key-agreement algorithm by Diffie, Hellman, Merkle.
- **$ Diffie-Hellman-Merkle** (N) Full name for the algorithm.
- **$ digest** See: message digest.
- **$ digital certificate** (I) Certificate document in digital form with digital signature.
- **$ digital certification** (D) Synonym for certification; use only if context insufficient.
- **$ digital document** (I) Electronic representation of non-electronic document.
- **$ digital envelope** (I) Combination of encrypted content and encrypted key.
- **$ Digital ID(service mark)** (D) Synonym for digital certificate; IDOCs SHOULD NOT use.
- **$ digital key** (D) Unnecessary adjective; use "key".
- **$ digital notary** (I) Trusted timestamp for digital document.
- **$ digital signature** (I) Value computed with cryptographic algorithm for origin and integrity verification.
- **$ Digital Signature Algorithm (DSA)** (N) Asymmetric algorithm for digital signatures.
- **$ Digital Signature Standard (DSS)** (N) U.S. Government standard specifying DSA.
- **$ digital watermarking** (I) Techniques for embedding unobtrusive marks in digital data.
- **$ digitized signature** (D) Digitized image of handwritten signature; IDOCs SHOULD NOT use.
- **$ DII** (O) See: Defense Information Infrastructure.
- **$ direct attack** (I) Attack where attacker addresses packets to victim.
- **$ directory** (I) Generic database server. (Capitalized: X.500 Directory).
- **$ Directory Access Protocol (DAP)** (N) OSI protocol for Directory access.
- **$ disaster plan** (D) Synonym for contingency plan; IDOCs SHOULD NOT use.
- **$ disclosure** See: unauthorized disclosure.
- **$ discretionary access control** (I) Access control based on identity and ownership.
- **$ DISN** (O) See: Defense Information Systems Network.
- **$ disruption** (I) Circumstance interrupting correct operation.
- **$ Distinguished Encoding Rules (DER)** (N) Subset of BER providing unique encoding.
- **$ distinguished name (DN)** (N) Unique identifier in X.500 DIT.
- **$ distributed attack** (I) Attack implemented with distributed computing or multiple agents.
- **$ Distributed Authentication Security Service (DASS)** (I) Experimental protocol for strong mutual authentication.
- **$ distributed computing** (I) Dispersing tasks among cooperating computers.
- **$ distribution point** (I) Location named in certificate for CRL retrieval.
- **$ DKIM** (I) See: Domain Keys Identified Mail.
- **$ DMZ** (D) See: demilitarized zone.
- **$ DN** (N) See: distinguished name.
- **$ DNS** (I) See: Domain Name System.
- **$ doctrine** See: security doctrine.
- **$ DoD** (N) Department of Defense. Use with national qualifier.
- **$ DOI** (I) See: Domain of Interpretation.
- **$ domain** (I) 1a. Environment with set of resources and entities. 1b. Set of users, objects, common policy. 5. Internet: part of DNS name space.
- **$ Domain Keys Identified Mail (DKIM)** (I) Protocol for data integrity and domain-level authentication for email.
- **$ domain name** (I) Identifier defined for subtrees in DNS.
- **$ Domain Name System (DNS)** (I) Main Internet operations database.
- **$ domain of interpretation (DOI)** (I) /IPsec/ Defines payload formats and exchange types.
- **$ dominate** (I) Security level A dominates B if A's classification level >= B's and categories include B's.
- **$ dongle** (I) Physical device required for software to run.
- **$ downgrade** (I) Reduce security level without changing content.
- **$ downgrade attack** (I) Man-in-the-middle attack forcing lower protection level.
- **$ draft RFC** (D) IDOCs SHOULD NOT use; use Internet-Draft.
- **$ Draft Standard** (I) Second level of Internet Standards Track.
- **$ DSA** (N) See: Digital Signature Algorithm.
- **$ DSS** (N) See: Digital Signature Standard.
- **$ dual control** (I) Procedure using two or more entities to protect resource.
- **$ dual signature** (O) /SET/ Single digital signature protecting two messages.
- **$ dual-use certificate** (O) Certificate for both signature and encryption. IDOCs SHOULD state definition.
- **$ duty** (I) Attribute of role obligating entity to perform tasks.
- **$ e-cash** (O) Electronic cash; IDOCs SHOULD state definition.
- **$ EAP** (I) See: Extensible Authentication Protocol.
- **$ EAL** (O) See: evaluation assurance level.
- **$ Easter egg** (O) Hidden functionality; IDOCs SHOULD NOT use.
- **$ eavesdropping** (I) Passive wiretapping done secretly.
- **$ ECB** (N) See: electronic codebook.
- **$ ECDSA** (N) See: Elliptic Curve Digital Signature Algorithm.
- **$ economy of alternatives** (I) Principle to minimize alternative ways of achieving service.
- **$ economy of mechanism** (I) Principle to keep security mechanism simple.
- **$ ECU** (N) See: end cryptographic unit.
- **$ EDI** (I) See: electronic data interchange.
- **$ EDIFACT** (N) UN EDI standard.
- **$ EE** (D) Abbreviation ambiguous; IDOCs SHOULD NOT use.
- **$ EES** (O) See: Escrowed Encryption Standard.
- **$ effective key length** (O) Measure of algorithm strength.
- **$ effectiveness** (O) /ITSEC/ How well TOE provides security in operational context.
- **$ El Gamal algorithm** (N) Asymmetric algorithm based on discrete logarithms.
- **$ electronic codebook (ECB)** (N) Block cipher mode using plaintext directly as input.
- **$ electronic commerce** (I) Business through paperless exchanges.
- **$ electronic data interchange (EDI)** (I) Computer-to-computer exchange of business data in standard formats.
- **$ Electronic Key Management System (EKMS)** (O) U.S. Government system for automated key management.
- **$ electronic signature** (D) IDOCs SHOULD NOT use; use digital signature.
- **$ electronic wallet** (D) IDOCs SHOULD NOT use; no consensus definition.
- **$ elliptic curve cryptography (ECC)** (I) Asymmetric cryptography using points on curves.
- **$ Elliptic Curve Digital Signature Algorithm (ECDSA)** (N) ECC analog of DSA.
- **$ emanation** (I) Signal emitted by system containing information.
- **$ emanations analysis** (I) Threat action of monitoring emanations.
- **$ emanations security (EMSEC)** (I) Physical security against emanations.
- **$ embedded cryptography** (N) Cryptography in equipment whose basic function is not cryptographic.
- **$ emergency plan** (D) Use contingency plan.
- **$ emergency response** (O) Urgent response to serious situation.
- **$ EMSEC** (I) See: emanations security.
- **$ EMV** (N) Specification for smart cards as payment cards.
- **$ Encapsulating Security Payload (ESP)** (I) IPsec protocol for data confidentiality and other services.
- **$ encipher** (D) Synonym for encrypt; IDOCs SHOULD NOT use.
- **$ encipherment** (D) Synonym for encryption; IDOCs SHOULD NOT use.
- **$ enclave** (I) Set of resources in same security domain.
- **$ encode** (I) 1. Use symbol system to represent information. 2. IDOCs SHOULD NOT use as synonym for encrypt.
- **$ encrypt** (I) Cryptographically transform data to ciphertext.
- **$ encryption** (I) Cryptographic transformation of plaintext to ciphertext.
- **$ encryption certificate** (I) Public-key certificate intended for encryption.
- **$ end cryptographic unit (ECU)** (N) 1. Final destination device for key loading. 2. Device performing cryptographic functions.
- **$ end entity** (I) System entity using private key only for purposes other than signing certificates.
- **$ end system** (N) /OSIRM/ Computer implementing all seven layers.
- **$ end-to-end encryption** (I) Continuous protection from source to destination.
- **$ end user** (I) System entity using resources primarily for application purposes.
- **$ endorsed-for-unclassified cryptographic item (EUCI)** (O) Unclassified crypto equipment with classified logic.
- **$ entity** See: system entity.
- **$ entrapment** (I) Deliberate planting of apparent flaws to detect penetrations.
- **$ entropy** (I) Information-theoretic measure of uncertainty.
- **$ ephemeral** (I) Short-lived cryptographic key or parameter.
- **$ erase** (I) Delete stored data. (U.S. Government: delete such that not recoverable by ordinary means.)
- **$ error detection code** (I) Checksum for accidental changes.
- **$ Escrowed Encryption Standard (EES)** (N) Standard for key escrow using SKIPJACK.
- **$ ESP** (I) See: Encapsulating Security Payload.
- **$ Estelle** (N) Formal specification language for protocols.
- **$ ETSI** (N) See: European Telecommunication Standards Institute.
- **$ EUCI** (O) See: endorsed-for-unclassified cryptographic item.
- **$ European Telecommunication Standards Institute (ETSI)** (N) Standards organization for ICT in Europe.
- **$ evaluated system** (I) System evaluated against security criteria.
- **$ evaluation** (I) Assessment against defined security criteria.
- **$ evaluation assurance level (EAL)** (N) Predefined package of assurance components in Common Criteria.
- **$ expire** (I) Cease to be valid due to lifetime exceeded.
- **$ exposure** (I) Threat action releasing sensitive data to unauthorized entity.
- **$ Extended Security Option** (I) See secondary definition under "IPSO".
- **$ Extensible Authentication Protocol (EAP)** (I) Framework for PPP supporting multiple authentication mechanisms.
- **$ Extensible Markup Language (XML)** (N) Version of SGML for Web.
- **$ extension** (I) Data item or mechanism extending protocol functionality.
- **$ external controls** (I) Administrative, personnel, physical security.
- **$ extranet** (I) Network for organization and business partners.
- **$ extraction resistance** (O) Ability to resist key extraction.
- **$ extrusion detection** (I) Monitoring for unauthorized outward transfers.
- **$ fail-safe** (I) 1. Synonym for fail-secure. 2. Mode preventing damage on failure.
- **$ fail-secure** (I) Mode preventing loss of secure state on failure.
- **$ fail-soft** (I) Selective termination of non-essential functions on failure.
- **$ failure control** (I) Methodology for fail-safe/secure/soft.
- **$ fairness** (I) Property of equitable resource access.
- **$ falsification** (I) Threat action using false data to deceive.
- **$ fault tree** (I) Branching structure for determining combinations of failures.
- **$ FEAL** (O) Family of symmetric block ciphers.
- **$ Federal Information Processing Standards (FIPS)** (N) NIST series of standards.
- **$ Federal Public-key Infrastructure (FPKI)** (O) U.S. Government PKI.
- **$ Federal Standard 1027** (N) Precursor to FIPS PUB 140.
- **$ File Transfer Protocol (FTP)** (I) Application-Layer protocol for file transfer.
- **$ fill device** (N) Device to transfer keying material.
- **$ filter** (I) Noun: synonym for guard. Verb: selectively block data according to policy.
- **$ filtering router** (I) Router preventing passage per security policy.
- **$ financial institution** (N) Establishment for customer transactions.
- **$ fingerprint** (I) Pattern of ridges. (D) PGP: hash result; IDOCs SHOULD NOT use for hash.
- **$ FIPS** (N) See: Federal Information Processing Standards.
- **$ FIPS PUB 140** (N) Standard for cryptographic module security.
- **$ FIREFLY** (O) U.S. Government key management protocol.
- **$ firewall** (I) Gateway restricting traffic to protect internal network.
- **$ firmware** (I) Programs stored in hardware (ROM, PROM).
- **$ FIRST** (N) See: Forum of Incident Response and Security Teams.
- **$ flaw** (I) Error in design, implementation, operation.
- **$ flaw hypothesis methodology** (I) Evaluation technique based on hypothesized flaws.
- **$ flooding** (I) Attack providing more input than system can process.
- **$ flow analysis** (I) Analysis of potential information flows.
- **$ flow control** (I) Procedure ensuring information transfers do not break security levels.
- **$ For Official Use Only (FOUO)** (O) U.S. DoD designation for unclassified but withholdable information.
- **$ formal** (I) Expressed in restricted syntax with defined mathematical semantics.
- **$ formal access approval** (O) Documented approval for specific category.
- **$ Formal Development Methodology** (O) See: Ina Jo.
- **$ formal model** (I) Security model that is formal.
- **$ formal proof** (I) Complete mathematical argument.
- **$ formal specification** (I) Precise description of system behavior in mathematical language.
- **$ formal top-level specification** (I) Formal specification using mathematical language.
- **$ formulary** (I) Technique for dynamic access decision.
- **$ FORTEZZA(trademark)** (O) NSA family of interoperable security products.
- **$ Forum of Incident Response and Security Teams (FIRST)** (N) International consortium of CSIRTs.
- **$ forward secrecy** (I) See: perfect forward secrecy.
- **$ FOUO** (O) See: For Official Use Only.
- **$ FPKI** (O) See: Federal Public-Key Infrastructure.
- **$ fraggle attack** (D) Slang; IDOCs SHOULD NOT use.
- **$ frequency hopping** (N) Switching frequencies during transmission.
- **$ fresh** (I) Recently generated, not replayed.
- **$ FTP** (I) See: File Transfer Protocol.
- **$ gateway** (I) Intermediate system connecting dissimilar networks.
- **$ GCA** (O) See: geopolitical certificate authority.
- **$ GDOI** (O) See: Group Domain of Interpretation.
- **$ GeldKarte** (O) German electronic money system.
- **$ GeneralizedTime** (N) ASN.1 data type for date and time.
- **$ Generic Security Service Application Program Interface (GSS-API)** (I) Interface for authentication, integrity, confidentiality services.
- **$ geopolitical certificate authority (GCA)** (O) /SET/ Optional level in hierarchy.
- **$ GIG** (O) See: Global Information Grid.
- **$ Global Information Grid (GIG)** (O) U.S. DoD globally interconnected information capabilities.
- **$ good engineering practice(s)** (N) Term for design/implementation/operating practices.
- **$ granularity** (N) 1. Fineness of access control. 2. Size of smallest protectable unit.
- **$ Green Book** (D) Slang; IDOCs SHOULD NOT use.
- **$ Group Domain of Interpretation (GDOI)** (I) ISAKMP domain for group key management.
- **$ group identity** (I) Identity for set of entities without individual record.
- **$ group security association** (I) Bundling of SAs for group communication.
- **$ GSS-API** (I) See: Generic Security Service Application Program Interface.
- **$ guard** (I) Gateway mediating data transfers between systems with different security policies.
- **$ guest login** (I) See: anonymous login.
- **$ GULS** (I) Generic Upper Layer Security service element.
- **$ Gypsy verification environment** (O) Methodology for software verification.
- **$ H field** (D) See: Handling Restrictions field.
- **$ hack** (I) 1a. Verb: work on something. 1b. Verb: do mischief. 2. Noun: solution specific to problem.
- **$ hacker** (I) Strongly interested in computers. (D) Synonym for cracker.
- **$ handle** (I) 1. Verb: perform processing operations. 2. Noun: online pseudonym.
- **$ handling restriction** (I) Type of access control beyond mandatory/discretionary.
- **$ Handling Restrictions field** (I) 16-bit field in IP security option.
- **$ handshake** (I) Protocol dialogue for identification/authentication.
- **$ Handshake Protocol** (I) /TLS/ Subprotocol for parameter agreement.
- **$ harden** (I) Configure system to eliminate/mitigate vulnerabilities.
- **$ hardware** (I) Physical components.
- **$ hardware error** (I) Threat action of unintentional system failure.
- **$ hardware token** See: token.
- **$ hash code** (D) Use hash result or hash function.
- **$ hash function** (I) Function mapping arbitrary input to fixed-length output.
- **$ hash result** (I) Output of hash function.
- **$ hash value** (D) Use hash result.
- **$ HDM** (O) See: Hierarchical Development Methodology.
- **$ Hierarchical Development Methodology (HDM)** (O) Methodology for software verification.
- **$ hierarchical PKI** (I) Architecture based on certification hierarchy.
- **$ hierarchy management** (I) Process of building certification hierarchy.
- **$ hierarchy of trust** (D) Use certification hierarchy.
- **$ high-assurance guard** (O) Oxymoron per General Campbell.
- **$ hijack attack** (I) Seizing control of existing communication.
- **$ HIPAA** (N) U.S. law for health information privacy.
- **$ HMAC** (I) Keyed hash based on cryptographic hash.
- **$ honey pot** (N) System designed to attract crackers.
- **$ host** (I) 1. Computer attached to network. 2. /IPS/ Computer not forwarding IP packets not addressed to it.
- **$ HTML** (I) See: Hypertext Markup Language.
- **$ HTTP** (I) See: Hypertext Transfer Protocol.
- **$ https** (I) HTTP with security mechanism (usually SSL).
- **$ human error** (I) Unintentional action or inaction.
- **$ hybrid encryption** (I) Combination of symmetric and asymmetric encryption.
- **$ hyperlink** (I) Information object pointing to related material.
- **$ hypermedia** (I) Generalization of hypertext.
- **$ hypertext** (I) Document with hyperlinks.
- **$ Hypertext Markup Language (HTML)** (I) Platform-independent language for hypertext.
- **$ Hypertext Transfer Protocol (HTTP)** (I) Protocol for Web requests/responses.
- **$ IAB** (I) See: Internet Architecture Board.
- **$ IANA** (I) See: Internet Assigned Numbers Authority.
- **$ IATF** (O) See: Information Assurance Technical Framework.
- **$ ICANN** (I) See: Internet Corporation for Assigned Names and Numbers.
- **$ ICMP** (I) See: Internet Control Message Protocol.
- **$ ICMP flood** (I) DoS attack with ICMP echo requests.
- **$ ICRL** (N) See: indirect certificate revocation list.
- **$ IDEA** (N) See: International Data Encryption Algorithm.
- **$ identification** (I) Act of presenting identifier.
- **$ identification information** (D) Use identifier or authentication information.
- **$ Identification Protocol** (I) Protocol for learning user identity of TCP connection.
- **$ identifier** (I) Data object representing specific identity.
- **$ identifier credential** (I) See: credential.
- **$ identifying information** (D) Use identifier or authentication information.
- **$ identity** (I) Set of attributes by which entity is known.
- **$ identity-based security policy** (I) Policy based on identities/attributes.
- **$ identity proofing** (I) Process verifying information used to establish identity.
- **$ IDOC** (I) Abbreviation for Internet Standards Process document. SHOULD NOT be used unless defined.
- **$ IDS** (I) See: intrusion detection system.
- **$ IEEE** (N) See: Institute of Electrical and Electronics Engineers.
- **$ IEEE 802.10** (N) Committee for LAN security.
- **$ IEEE P1363** (N) Standard for Public-Key Cryptography.
- **$ IESG** (I) See: Internet Engineering Steering Group.
- **$ IETF** (I) See: Internet Engineering Task Force.
- **$ IKE** (I) See: IPsec Key Exchange.
- **$ IMAP4** (I) See: Internet Message Access Protocol.
- **$ IMAP4 AUTHENTICATE** (I) Command for client authentication and security.
- **$ impossible** (O) Cannot be done in reasonable time.
- **$ in the clear** (I) Not encrypted.
- **$ Ina Jo** (O) Formal methodology for software.
- **$ incapacitation** (I) Threat action preventing/interrupting system operation.
- **$ incident** See: security incident.
- **$ INCITS** (N) See International Committee under ANSI.
- **$ indicator** (N) Action expected in preparation for attack.
- **$ indirect attack** (I) Attack via third party.
- **$ indirect certificate revocation list (ICRL)** (N) CRL with revocations for certificates issued by other CAs.
- **$ indistinguishability** (I) Attribute of encryption algorithm.
- **$ inference** (I) Threat action deriving information from characteristics/byproducts.
- **$ inference control** (I) Protection against inference.
- **$ INFOCON** (O) See: information operations condition.
- **$ informal** (N) Expressed in natural language.
- **$ information** (I) 1. Facts and ideas. 2. Knowledge in any medium.
- **$ information assurance** (N) Measures protecting and defending information systems.
- **$ Information Assurance Technical Framework (IATF)** (O) Tutorial/reference document.
- **$ information domain** (O) See domain.
- **$ information flow policy** (N) Triple of security levels, operator, relation.
- **$ information operations condition (INFOCON)** (O) U.S. DoD defense posture.
- **$ information security (INFOSEC)** (N) Measures in information systems.
- **$ information system** (I) Organized assembly of computing/communication resources.
- **$ Information Technology Security Evaluation Criteria (ITSEC)** (N) European standard.
- **$ INFOSEC** (I) See: information security.
- **$ ingress filtering** (I) Blocking packets with false source addresses at boundary.
- **$ initialization value (IV)** (I) Input parameter setting starting state of algorithm.
- **$ initialization vector** (D) Use initialization value.
- **$ insertion** (I) 1. Packet insertion. 2. Threat action of introducing false data.
- **$ inside attack** (I) Attack initiated from inside security perimeter.
- **$ insider** (I) User accessing system from inside security perimeter.
- **$ inspectable space** (O) Space where TEMPEST exploitation not practical.
- **$ Institute of Electrical and Electronics Engineers, Inc. (IEEE)** (N) Professional association.
- **$ integrity** See: data integrity, etc.
- **$ integrity check** (D) Use cryptographic hash or protected checksum.
- **$ integrity label** (I) Security label indicating confidence in data.
- **$ intelligent threat** (I) Adversary with capability and intent.
- **$ interception** (I) Threat action directly accessing data in transit.
- **$ interference** (I) Threat action of jamming.
- **$ intermediate CA** (D) Use other term.
- **$ internal controls** (I) Functions in hardware/software for security.
- **$ International Data Encryption Algorithm (IDEA)** (N) Symmetric block cipher.
- **$ International Standard** (N) ISO standard level.
- **$ International Traffic in Arms Regulations (ITAR)** (O) U.S. export control rules.
- **$ internet** (I) Abbreviation of internetwork.
- **$ Internet** (I) Worldwide system of interconnected networks.
- **$ Internet Architecture Board (IAB)** (I) Advisory group for Internet architecture.
- **$ Internet Assigned Numbers Authority (IANA)** (I) Former central coordination body.
- **$ Internet Control Message Protocol (ICMP)** (I) Protocol for error reporting.
- **$ Internet Corporation for Assigned Names and Numbers (ICANN)** (I) Managing IP address allocation, DNS, etc.
- **$ Internet-Draft** (I) Working document valid for six months.
- **$ Internet Engineering Steering Group (IESG)** (I) Responsible for technical management of IETF.
- **$ Internet Engineering Task Force (IETF)** (I) Principal body developing Internet Standards.
- **$ Internet Key Exchange (IKE)** (I) Key-establishment protocol for IPsec.
- **$ Internet Layer** (I) Layer in IPS.
- **$ Internet Message Access Protocol, version 4 (IMAP4)** (I) Protocol for accessing mailboxes.
- **$ Internet Open Trading Protocol (IOTP)** (I) Framework for Internet commerce.
- **$ Internet Policy Registration Authority (IPRA)** (I) Top CA of Internet certification hierarchy.
- **$ Internet Private Line Interface (IPLI)** (O) Successor to PLI for TCP/IP.
- **$ Internet Protocol (IP)** (I) Internet-Layer protocol moving datagrams.
- **$ Internet Protocol Security Option (IPSO)** (I) Fields in IP for security information.
- **$ Internet Protocol Suite (IPS)** (I) Set of protocols approved as Internet Standards.
- **$ Internet Security Association and Key Management Protocol (ISAKMP)** (I) Protocol for negotiating security associations.
- **$ Internet Society (ISOC)** (I) Professional society for Internet.
- **$ Internet Standard** (I) Specification approved by IESG.
- **$ internetwork** (I) System of interconnected networks.
- **$ intranet** (I) Private network based on Internet technology.
- **$ intruder** (I) Entity gaining unauthorized access.
- **$ intrusion** (I) Security incident of unauthorized access.
- **$ intrusion detection** (I) Sensing and analyzing events for unauthorized access.
- **$ intrusion detection system (IDS)** (N) Process or subsystem for monitoring and analyzing events.
- **$ invalidity date** (N) X.509 CRL entry extension indicating when key compromised.
- **$ IOTP** (I) See: Internet Open Trading Protocol.
- **$ IP** (I) See: Internet Protocol.
- **$ IP address** (I) Computer's internetwork address.
- **$ IP Security Option** (I) See: Internet Protocol Security Option.
- **$ IP Security Protocol (IPsec)** (I) IETF working group and architecture for IP security.
- **$ IPLI** (I) See: Internet Private Line Interface.
- **$ IPRA** (I) See: Internet Policy Registration Authority.
- **$ IPS** (I) See: Internet Protocol Suite.
- **$ IPsec** (I) See: IP Security Protocol.
- **$ IPSO** (I) See: Internet Protocol Security Option.
- **$ ISAKMP** (I) See: Internet Security Association and Key Management Protocol.
- **$ ISO** (I) International Organization for Standardization.
- **$ ISO 17799** (N) Code of practice for information security management.
- **$ ISOC** (I) See: Internet Society.
- **$ issue** (I) Generate, sign, distribute digital certificate or CRL.
- **$ issuer** (I) CA that signs certificate or CRL.
- **$ ITAR** (O) See: International Traffic in Arms Regulations.
- **$ ITSEC** (N) See: Information Technology Security Evaluation Criteria.
- **$ ITU-T** (N) International Telecommunications Union Telecommunication Standardization Sector.
- **$ IV** (I) See: initialization value.
- **$ jamming** (N) Attack interfering with broadcast.
- **$ KAK** (D) See: key-auto-key.
- **$ KDC** (I) See: Key Distribution Center.
- **$ KEA** (N) See: Key Exchange Algorithm.
- **$ KEK** (I) See: key-encrypting key.
- **$ Kerberos** (I) System using passwords and symmetric cryptography for authentication.
- **$ kernel** (I) Small trusted part of system.
- **$ Kernelized Secure Operating System (KSOS)** (O) MLS operating system.
- **$ key** (I) Input parameter for cryptographic algorithm.

*[Note: The definitions continue in the next chunk.]*

## Requirements Summary
The glossary contains many explicit recommendations using RFC 2119 language. Key normative statements include:
- IDOCs SHOULD use defined terms consistently.
- IDOCs SHOULD NOT use deprecated terms (marked D) unless specific circumstances apply.
- IDOCs SHOULD define abbreviations at first use if not widely known.
- IDOCs SHOULD NOT use "cute" synonyms to avoid international confusion.
- IDOCs SHOULD restrict usage of certain terms (e.g., "authenticate") as specified in definitions.
- IDOCs MAY use certain terms broadly when context is clear.

These recommendations are personal opinions of the author and not official IETF positions.

## Definitions (continued)

### I

- **inside attack** (I): See secondary definition under "attack". Compare: insider.
- **insider**
  - 1. (I) A user (usually a person) that accesses a system from a position that is inside the system's security perimeter. (Compare: authorized user, outsider, unauthorized user.)
    - Tutorial: An insider has been assigned a role with more privileges; actions may be authorized or unauthorized.
  - 2. (O) A person with authorized physical access to the system. (Example: office janitor.) [NRC98]
  - 3. (O) A person with organizational status causing system to view access requests as authorized. (Example: purchasing agent.) [NRC98]
- **inspectable space** (O): /EMSEC/ "Three-dimensional space surrounding equipment that process classified and/or sensitive information within which TEMPEST exploitation is not considered practical or where legal authority to identify and/or remove a potential TEMPEST exploitation exists." [C4009] (Compare: control zone, TEMPEST zone.)
- **Institute of Electrical and Electronics Engineers, Inc. (IEEE)** (N): Not-for-profit association; produces literature, standards. (See: SILS.)
- **integrity**: See: data integrity, datagram integrity service, correctness integrity, source integrity, stream integrity service, system integrity.
- **integrity check** (D): A computation that is part of a mechanism to provide data integrity service or data origin authentication service. (Compare: checksum.)
  - Deprecated Term: IDOCs SHOULD NOT use this term as a synonym for "cryptographic hash" or "protected checksum".
- **integrity label** (I): A security label that tells the degree of confidence that may be placed in data, and may also tell what countermeasures are required. (See: integrity. Compare: classification label.)
- **intelligent threat** (I): A circumstance in which an adversary has the technical and operational ability to detect and exploit a vulnerability and also has the demonstrated, presumed, or inferred intent to do so. (See: threat.)
- **interception** (I): A type of threat action whereby an unauthorized entity directly accesses sensitive data while traveling between authorized sources and destinations. (See: unauthorized disclosure.)
  - Subtypes: Theft, Wiretapping (passive), Emanations analysis.
- **interference** (I): /threat action/ See secondary definition under "obstruction".
- **intermediate CA** (D): The CA that issues a cross-certificate to another CA. [X509] (See: cross-certification.)
  - Deprecated Term: IDOCs SHOULD NOT use this term.
- **internal controls** (I): /COMPUSEC/ Functions, features, and technical characteristics of computer hardware and software, especially operating systems. Includes mechanisms for access control, flow control, inference control. (Compare: external controls.)
- **International Data Encryption Algorithm (IDEA)** (N): Patented symmetric block cipher with 128-bit key, 64-bit blocks. [Schn] (See: symmetric cryptography.)
- **International Standard** (N): See secondary definition under "ISO".
- **International Traffic in Arms Regulations (ITAR)** (O): U.S. State Department rules controlling export/import of defense articles/services, including cryptographic systems and TEMPEST suppression technology. (See: type 1 product, Wassenaar Arrangement.)
- **internet, Internet**
  - 1. (I) /not capitalized/ Abbreviation of "internetwork".
  - 2. (I) /capitalized/ The single, interconnected worldwide system of computer networks sharing protocol suite specified by IAB (RFC 2026) and name/address spaces managed by ICANN. (See: Internet Layer, Internet Protocol Suite.)
    - Usage: Use definite article ("the").
- **Internet Architecture Board (IAB)** (I): Technical advisory group of ISOC, provides oversight of Internet architecture and protocols, approves IESG appointments. (RFC 2026)
- **Internet Assigned Numbers Authority (IANA)** (I): Central coordination, allocation, and registration body for Internet protocol parameters; superseded by ICANN.
- **Internet Control Message Protocol (ICMP)** (I): Internet Standard protocol (RFC 792) for reporting error conditions during IP datagram processing.
- **Internet Corporation for Assigned Names and Numbers (ICANN)** (I): Non-profit corporation responsible for IP address space allocation, protocol parameter assignment, DNS management, root server system management.
  - Tutorial: Formed October 1998; coordinates four key Internet functions.
- **Internet-Draft** (I): A working document of the IETF, its areas, and working groups. (RFC 2026) (Compare: RFC.)
  - Tutorial: Valid for maximum six months; not an archival document.
- **Internet Engineering Steering Group (IESG)** (I): Part of ISOC responsible for technical management of IETF activities and administration of Internet Standards Process. (RFC 2026)
- **Internet Engineering Task Force (IETF)** (I): Self-organized group developing Internet technology; principal body engaged in developing Internet Standards. (RFCs 2026, 3935)
- **Internet Key Exchange (IKE)** (I): An Internet, IPsec, key-establishment protocol [R4306] for putting in place authenticated keying material for use with ISAKMP and other security associations (AH, ESP).
  - Tutorial: Based on ISAKMP, OAKLEY, SKEME.
- **Internet Layer**: See Internet Protocol Suite.
- **Internet Message Access Protocol, version 4 (IMAP4)** (I): Protocol (RFC 2060) for client workstation to dynamically access mailbox on server. (See: POP3.)
  - Tutorial: Has mechanisms for authentication and security services.
- **Internet Open Trading Protocol (IOTP)** (I): General framework for Internet commerce, encapsulating transactions of various payment systems; provides optional security services. [R2801]
- **Internet Policy Registration Authority (IPRA)** (I): X.509-compliant CA that is the top CA of the Internet certification hierarchy. [R1422] (See: /PEM/ under "certification hierarchy".)
- **Internet Private Line Interface (IPLI)** (O): Successor to PLI, updated to use TCP/IP and military-grade COMSEC equipment. (See: end-to-end encryption.)
- **Internet Protocol (IP)** (I): Internet Standard, Internet-Layer protocol that moves datagrams across an internetwork without reliable delivery, flow control, sequencing. IPv4 in RFC 791, IPv6 in RFC 2460. (See: IP address, TCP/IP.)
  - Tutorial: Placed at top of Layer 3 in OSIRM; always present in Internet Layer of IPS.
- **Internet Protocol security**: See IP Security Protocol.
- **Internet Protocol Security Option (IPSO)** (I): Refers to one of three types of IP security options (DoD Basic Security Option, DoD Extended Security Option, Common IP Security Option). (Compare: IPsec.)
  - Deprecated Usage: IDOCs SHOULD NOT use this term without a modifier indicating which type.
- **Internet Protocol Suite (IPS)** (I): Set of network communication protocols specified by IETF and approved as Internet Standards. (See: OSIRM Security Architecture. Compare: OSIRM.)
  - Usage: Popularly known as "TCP/IP". This Glossary refers to IPS protocol layers by name, OSIRM layers by number.
  - Tutorial: IPS has five protocol layers: Application, Transport, Internet, Network Interface, Network Hardware. Diagram provided.
- **Internet Security Association and Key Management Protocol (ISAKMP)** (I): IPsec protocol [R2408] to negotiate, establish, modify, delete security associations, and exchange key generation and authentication data.
  - Tutorial: Supports negotiation of security associations for all IPS layers; conducted in two phases (Phase 1 and Phase 2).
- **Internet Society (ISOC)** (I): Professional society concerned with Internet development, standards, and social/political/technical issues. (RFC 2026)
- **Internet Standard** (I): Specification approved by IESG and published as RFC, stable, technically competent, multiple interoperable implementations, significant public support. (RFC 2026) (Compare: RFC.)
  - Tutorial: Three levels of maturity: Proposed Standard, Draft Standard, Standard.
- **internetwork** (I): A system of interconnected networks; network of networks. Usually shortened to "internet". (See: internet, Internet.)
  - Tutorial: Can be built using OSIRM Layer 3 gateways or uniform internetwork protocol (e.g., IP).
- **intranet** (I): Computer network based on Internet technology used for internal (private) purposes, closed to outsiders. (See: extranet, VPN.)
- **intruder** (I): Entity that gains or attempts to gain unauthorized access to a system or system resource. (See: intrusion. Compare: adversary, cracker, hacker.)
- **intrusion**
  - 1. (I) A security event or combination constituting a security incident where an intruder gains or attempts unauthorized access. (See: IDS.)
  - 2. (I) A type of threat action whereby unauthorized entity gains access to sensitive data by circumventing protections. (See: unauthorized disclosure.)
    - Subtypes: Trespass, Penetration, Reverse engineering, Cryptanalysis.
- **intrusion detection** (I): Sensing and analyzing system events to notice unauthorized access attempts. (See: anomaly detection, IDS, misuse detection. Compare: extrusion detection.) [IDSAN, IDSSC, IDSSE, IDSSY]
  - Subtypes: Active detection (real-time) and Passive detection (off-line).
- **intrusion detection system (IDS)**
  - 1. (N) A process or subsystem that automates monitoring events in a computer network and analyzing them for security problems. [SP31] (See: intrusion detection.)
  - 2. (N) A security alarm system to detect unauthorized entry. [DC6/9]
    - Tutorial: Active detection can be host-based or network-based.
- **invalidity date** (N): X.509 CRL entry extension indicating date when revoked certificate's private key was compromised or certificate considered invalid. [X509]
  - Tutorial: May be earlier than revocation date; not sufficient for non-repudiation service.
- **IOTP** (I): See Internet Open Trading Protocol.
- **IP** (I): See Internet Protocol.
- **IP address** (I): Computer's internetwork address assigned for use by IP and other protocols.
  - Tutorial: IPv4 address format (four 8-bit parts), IPv6 address format (eight 16-bit parts).
- **IP Security Option** (I): See Internet Protocol Security Option.
- **IP Security Protocol (IPsec)**
  - 1a. (I) Name of IETF working group specifying architecture [R2401, R4301] and set of protocols for IP traffic security. (See: AH, ESP, IKE, SAD, SPD. Compare: IPSO.)
  - 1b. (I) Collective name for IP security architecture and associated protocols (AH, ESP, IKE).
    - Usage: In IDOCs using "IPsec", letters "IP" SHOULD be uppercase, "sec" SHOULD NOT.
    - Tutorial: Services include access control, connectionless data integrity, data origin authentication, replay protection, data confidentiality, limited traffic-flow confidentiality.
- **IPLI** (I): See Internet Private Line Interface.
- **IPRA** (I): See Internet Policy Registration Authority.
- **IPS** (I): See Internet Protocol Suite.
- **IPsec** (I): See IP Security Protocol.
- **IPSO** (I): See Internet Protocol Security Option.
- **ISAKMP** (I): See Internet Security Association and Key Management Protocol.
- **ISO** (I): International Organization for Standardization; non-governmental organization of national standards bodies. (Compare: ANSI, IETF, ITU-T, W3C.)
  - Tutorial: Standards development process: WD, CD, DIS, IS. ISO/IEC JTC 1 for information technology.
- **ISO 17799** (N): International Standard code of practice for managing information security; derived from BS 7799 Part 1. (See: IATF, [SP14].)
- **ISOC** (I): See Internet Society.
- **issue** (I): /PKI/ Generate and sign a digital certificate (or CRL) and, usually, distribute and make it available. (See: certificate creation.)
  - Usage: Usually includes making available to potential users; ABA [DSG] explicitly limits to creation process.
- **issuer**
  - 1. (I) /certificate, CRL/ The CA that signs a digital certificate or CRL.
    - Tutorial: X.509 certificate always includes issuer's name.
  - 2. (O) /payment card, SET/ "The financial institution or its agent that issues the unique primary account number to the cardholder for the payment card brand." [SET2]
- **ITAR** (O): See International Traffic in Arms Regulations.
- **ITSEC** (N): See Information Technology System Evaluation Criteria.
- **ITU-T** (N): International Telecommunications Union, Telecommunication Standardization Sector; publishes standards called "Recommendations". (See: X.400, X.500.)
  - Tutorial: Works on communication systems; cooperates with ISO.
- **IV** (I): See initialization value.

### J

- **jamming** (N): An attack that attempts to interfere with the reception of broadcast communications. (See: anti-jam, denial of service. Compare: flooding.)
  - Tutorial: Typically done by broadcasting a second signal.

### K

- **KAK** (D): See key-auto-key. (Compare: KEK.)
- **KDC** (I): See Key Distribution Center.
- **KEA** (N): See Key Exchange Algorithm.
- **KEK** (I): See key-encrypting key. (Compare: KAK.)
- **Kerberos** (I): System using passwords and symmetric cryptography (DES) for ticket-based peer entity authentication and access control in client-server network. [R4120, Stei] (See: realm.)
  - Tutorial: Developed by Project Athena; uses authentication servers and ticket-granting servers as ACC and KDC. RFC 4556 extends with public-key cryptography (PKINIT).
- **kernel** (I): A small, trusted part of a system providing services on which other parts depend. (See: security kernel.)
- **Kernelized Secure Operating System (KSOS)** (O): MLS computer operating system designed as provably secure replacement for UNIX Version 6; includes security kernel, utilities. [Perr]
  - Tutorial: KSOS-6 on SCOMP, KSOS-11 on DEC PDP-11.
- **key**
  - 1a. (I) /cryptography/ Input parameter used to vary transformation function of cryptographic algorithm. (See: private key, public key, storage key, symmetric key, traffic key. Compare: initialization value.)
  - 1b. (O) /cryptography/ In singular form as collective noun referring to keys or keying material.
  - 2. (I) /anti-jam/ Input parameter to vary process for anti-jam measure. (See: frequency hopping, spread spectrum.)
    - Tutorial: Usually a sequence of bits; should be random.
- **key agreement (algorithm or protocol)**
  - 1. (I) Key establishment method (especially asymmetric) where two or more entities can each generate same key value without prior arrangement except public exchange. (See: Diffie-Hellman-Merkle, key establishment, KEA, MQV. Compare: key transport.)
  - 2. (O) "A method for negotiating a key value on line without transferring the key, even in an encrypted form, e.g., the Diffie-Hellman technique." [X509]
  - 3. (O) "The procedure whereby two different parties generate shared symmetric keys such that any of the shared symmetric keys is a function of the information contributed by all legitimate participants, so that no party [alone] can predetermine the value of the key." [A9042]
- **key authentication** (N): "The assurance of the legitimate participants in a key agreement that no non-legitimate party possesses the shared symmetric key." [A9042]
- **key-auto-key (KAK)** (D): "Cryptographic logic using previous key to produce key." [C4009, A1523] (See: mode.)
  - Deprecated Term: IDOCs SHOULD NOT use; instead use terms for defined modes (CBC, CFB, OFB).
- **key center** (I): Centralized key-distribution process (symmetric cryptography) using master keys (KEKs) to encrypt and distribute session keys.
  - Tutorial: ANSI [A9017] defines key distribution center and key translation center.
- **key confirmation** (N): "The assurance [provided to] the legitimate participants in a key establishment protocol that the [parties that are intended to share] the symmetric key actually possess the shared symmetric key." [A9042]
- **key distribution** (I): Process delivering cryptographic key from generation location to use locations. (See: key establishment, key management.)
- **key distribution center (KDC)**
  - 1. (I) Type of key center that implements key-distribution protocol to provide keys to entities wishing to communicate securely. (Compare: key translation center.)
  - 2. (N) "COMSEC facility generating and distributing key in electrical form." [C4009]
    - Tutorial: Distributes keys to Alice and Bob who share KEK with KDC; KDC generates keys and encrypts them with respective KEKs.
- **key encapsulation** (N): Key recovery technique for storing knowledge of cryptographic key by encrypting it with another key, allowing only recovery agents to decrypt. (Compare: key escrow.)
- **key-encrypting key (KEK)** (I): Cryptographic key used to encrypt other keys (DEKs or TEKs) for transmission or storage, not for application data.
- **key escrow** (N): Key recovery technique storing knowledge of cryptographic key or parts with escrow agents for recovery in specified circumstances. (Compare: key encapsulation.)
  - Tutorial: Often implemented with split knowledge (e.g., Escrowed Encryption Standard [FP185]).
- **key establishment (algorithm or protocol)**
  - 1. (I) Procedure combining key-generation and key-distribution steps to set up secure communication association.
  - 2. (I) Procedure resulting in keying material shared among system entities. [A9042, SP56]
    - Tutorial: Basic techniques: key agreement and key transport.
- **Key Exchange Algorithm (KEA)** (N): Key-agreement method based on Diffie-Hellman-Merkle using 1024-bit asymmetric keys. (See: CAPSTONE, CLIPPER, FORTEZZA, SKIPJACK.)
  - Tutorial: Developed by NSA; declassified June 1998.
- **key generation** (I): Process creating sequence of symbols comprising cryptographic key. (See: key management.)
- **key generator**
  - 1. (I) Algorithm using mathematical rules to produce pseudorandom sequence of cryptographic key values.
  - 2. (I) Encryption device incorporating key-generation mechanism and applying key to plaintext.
- **key length** (I): Number of symbols (usually bits) needed to represent possible values of cryptographic key. (See: key space.)
- **key lifetime**
  - 1. (D) Synonym for "cryptoperiod".
    - Deprecated Definition: IDOCs SHOULD NOT use; cryptoperiod may be only part of lifetime.
  - 2. (O) /MISSI/ Attribute specifying time span bounding validity period of MISSI X.509 certificate containing public component.
- **key loader** (N): Synonym for "fill device".
- **key loading and initialization facility (KLIF)** (N): Place where ECU hardware is activated after fabrication. (Compare: CLEF.)
  - Tutorial: Installs KEKs, seed values, cryptographic software.
- **key management**
  - 1a. (I) Process of handling keying material during its life cycle in cryptographic system, including supervision and control. (See: key distribution, key escrow, keying material, public-key infrastructure.)
    - Usage: Includes ordering, generating, storing, archiving, escrowing, distributing, loading, destroying, auditing, accounting.
  - 1b. (O) /NIST/ "The activities involving the handling of cryptographic keys and other related security parameters... during the entire life cycle." [FP140, SP57]
  - 2. (O) /OSIRM/ "The generation, storage, distribution, deletion, archiving and application of keys in accordance with a security policy." [I7498-2]
- **Key Management Protocol (KMP)** (N): Protocol to establish shared symmetric key between users; superseded by ISAKMP and IKE.
- **key material** (D): Synonym for "keying material".
  - Deprecated Usage: IDOCs SHOULD NOT use.
- **key pair** (I): Set of mathematically related keys (public and private) for asymmetric cryptography; computationally infeasible to derive private from public. (See: Diffie-Hellman-Merkle, RSA.)
  - Tutorial: Owner discloses public key; private key kept secret.
- **key recovery**
  - 1. (I) /cryptanalysis/ Process for learning value of cryptographic key used previously. (See: cryptanalysis, recovery.)
  - 2. (I) /backup/ Techniques providing intentional, alternate means to access key used for data confidentiality. [DoD4] (Compare: recovery.)
    - Tutorial: Two classes: key encapsulation and key escrow.
- **key space** (I): Range of possible key values; number of distinct transformations supported by algorithm. (See: key length.)
- **key translation center** (I): Type of key center implementing key-distribution protocol to convey keys between parties. (Compare: key distribution center.)
  - Tutorial: Alice generates keys, encrypts with KEK shared with center; center decrypts and reencrypts with Bob's KEK.
- **key transport (algorithm or protocol)**
  - 1. (I) Key establishment method where secret key is generated by one entity and securely sent to another. (Compare: key agreement.)
    - Tutorial: Either one entity generates and sends, or each generates a secret value and sends to combine.
  - 2. (O) "The procedure to send a symmetric key from one party to other parties... symmetric key is determined entirely by one party." [A9042]
- **key update**
  - 1. (I) Derive new key from existing key. (Compare: rekey.)
  - 2. (O) Irreversible cryptographic process modifying key to produce new key. [C4009]
- **key validation**
  - 1. (I) "The procedure for the receiver of a public key to check that the key conforms to the arithmetic requirements... to thwart certain types of attacks." [A9042] (See: weak key)
  - 2. (D) Synonym for "certificate validation".
    - Deprecated Usage: IDOCs SHOULD NOT use as synonym for certificate validation.
- **keyed hash** (I): Cryptographic hash where mapping varied by cryptographic key. (See: checksum.)
  - Tutorial: Two basic types: based on keyed encryption algorithm (e.g., Data Authentication Code) or based on keyless hash enhanced with key (e.g., HMAC).
- **keying material**
  - 1. (I) Data needed to establish and maintain cryptographic security association (keys, key pairs, IVs).
  - 2. (O) "Key, code, or authentication information in physical or magnetic form." [C4009] (Compare: COMSEC material.)
- **keying material identifier (KMID)**
  - 1. (I) Identifier assigned to keying material.
  - 2. (O) /MISSI/ 64-bit identifier assigned to key pair when public key bound in MISSI X.509 certificate.
- **Khafre** (N): Patented symmetric block cipher by Ralph C. Merkle; plug-in replacement for DES. [Schn]
  - Tutorial: Efficient for small amounts of data.
- **Khufu** (N): Patented symmetric block cipher by Ralph C. Merkle; plug-in replacement for DES. [Schn]
  - Tutorial: Fast for large amounts of data.
- **KLIF** (N): See key loading and initialization facility.
- **KMID** (I): See keying material identifier.
- **known-plaintext attack** (I): Cryptanalysis technique determining key from knowledge of plaintext-ciphertext pairs.
- **kracker** (O): Old spelling for "cracker".
- **KSOS, KSOS-6, KSOS-11** (O): See Kernelized Secure Operating System.

### L

- **L2F** (N): See Layer 2 Forwarding Protocol.
- **L2TP** (N): See Layer 2 Tunneling Protocol.
- **label**: See time stamp, security label.
- **laboratory attack** (O): "Use of sophisticated signal recovery equipment in a laboratory environment to recover information from data storage media." [C4009]
- **LAN** (I): Abbreviation for "local area network" [R1983]. (See: [FP191].)
- **land attack** (I): Denial-of-service attack sending IP packet with same source and destination address and TCP SYN with same source and destination port.
- **Language of Temporal Ordering Specification (LOTOS)** (N): Language (ISO 8807-1990) for formal specification of computer network protocols.
- **lattice** (I): Finite set with partial ordering such that for every pair there is least upper bound and greatest lower bound.
  - Example: Set of security levels with dominate relation.
  - Tutorial: Used in cryptography for hard computational problems and attacks.
- **lattice model**
  - 1. (I) Description of semantic structure formed by finite set of security levels. (See: dominate, lattice, security model.)
  - 2. (I) /formal model/ Model for flow control based on lattice of finite security levels. [Denn]
- **Law Enforcement Access Field (LEAF)** (N): Data item embedded in encrypted data by devices implementing Escrowed Encryption Standard (e.g., CLIPPER chip).
- **Layer 1, 2, 3, 4, 5, 6, 7** (N): See OSIRM.
- **Layer 2 Forwarding Protocol (L2F)** (N): Internet protocol using tunneling of PPP over IP to create virtual extension of dial-up link; transparent to user. (See: L2TP.)
- **Layer 2 Tunneling Protocol (L2TP)** (N): Internet client-server protocol combining PPTP and L2F; supports tunneling of PPP over IP, frame relay, or other networks. (See: VPN.)
  - Tutorial: PPP can encapsulate any OSIRM Layer 3 protocol; L2TP does not specify security services.
- **LDAP** (I): See Lightweight Directory Access Protocol.
- **least common mechanism** (I): Principle that security architecture should minimize reliance on mechanisms shared by many users.
  - Tutorial: Shared mechanisms may include cross-talk paths.
- **least privilege** (I): Principle that each system entity should be granted minimum resources and authorizations needed. (Compare: economy of mechanism, least trust.)
  - Tutorial: Limits damage from accidents or unauthorized acts.
- **least trust** (I): Principle that security architecture should minimize number of components requiring trust and extent of trust. (Compare: least privilege, trust level.)
- **legacy system** (I): System in operation but not improved while new system is being developed.
- **legal non-repudiation** (I): See secondary definition under "non-repudiation".
- **leap of faith**
  - 1. (I) /general security/ Operating system as if it began in secure state without proof.
  - 2. (I) /COMSEC/ Initial part of protocol vulnerable to attack but if completed without attack, subsequent steps are secure.
    - Usage: IDOCs using this term SHOULD state specific definition.
- **level of concern** (N): /U.S. DoD/ Rating indicating extent of protective measures needed. (See: critical, sensitive, level of robustness.)
- **level of robustness** (N): /U.S. DoD/ Characterization of strength of security function/mechanism and assurance. [Cons, IATF] (See: level of concern.)
- **Liberty Alliance** (O): International consortium addressing identity and Web services; developed standard for federated network identity.
- **Lightweight Directory Access Protocol (LDAP)** (I): Internet client-server protocol (RFC 3377) supporting basic use of X.500 Directory without full DAP resource requirements.
  - Tutorial: Designed for simple management and browser applications; supports simple and strong authentication.
- **link**
  - 1a. (I) Communication facility or physical medium sustaining data communications between network nodes in protocol layer below IP. (RFC 3753)
  - 1b. (I) /subnetwork/ Communication channel connecting subnetwork relays at OSIRM Layer 2. (See: link encryption.)
  - 2. (I) /World Wide Web/ See hyperlink.
- **link encryption** (I): Stepwise protection of data flowing between two points by encrypting separately on each network link. Each link may use different key or algorithm. [R1455] (Compare: end-to-end encryption.)
- **liveness** (I): Property of communication association or feature providing assurance that data is freshly transmitted, not replayed. (See: fresh, nonce, replay attack.)
- **logic bomb** (I): Malicious logic activating when specified conditions met; intended to cause denial of service or damage. (See: Trojan horse, virus, worm.)
- **login**
  - 1a. (I) Act by which system entity establishes session to use resources. (See: principal, session.)
  - 1b. (I) Act by which user's identity is authenticated by system. (See: principal, session.)
    - Usage: Usually providing identifier and authentication information.
- **long title** (O): /U.S. Government/ "Descriptive title of [an item of COMSEC material]." [C4009] (Compare: short title.)
- **low probability of detection** (I): Result of TRANSEC measures to hide or disguise communication.
- **low probability of intercept** (I): Result of TRANSEC measures to prevent interception.
- **LOTOS** (N): See Language of Temporal Ordering Specification.

### M

- **MAC** (N): See mandatory access control, Message Authentication Code.
  - Deprecated Usage: IDOCs using this term SHOULD define it because ambiguous.
- **magnetic remanence** (N): Magnetic representation of residual information remaining after medium has been cleared. [NCS25] (See: clear, degauss, purge.)
- **main mode** (I): See /IKE/ under "mode".
- **maintenance hook** (N): "Special instructions (trapdoors) in software allowing easy maintenance... serious security risk if not removed prior to live implementation." [C4009] (See: back door.)
- **malicious logic** (I): Hardware, firmware, or software intentionally included for harmful purpose. (See: logic bomb, Trojan horse, spyware, virus, worm.)
- **malware** (D): Contraction of "malicious software". (See: malicious logic.)
  - Deprecated Term: IDOCs SHOULD NOT use.
- **MAN** (I): Metropolitan area network.
- **man-in-the-middle attack** (I): Form of active wiretapping where attacker intercepts and modifies communicated data to masquerade as one or more entities. (See: hijack attack, piggyback attack.)
  - Tutorial: Example with Diffie-Hellman-Merkle.
- **manager** (I): Person who controls service configuration or functional privileges. (See: administrative security. Compare: operator, SSO, user.)
- **mandatory access control**
  - 1. (I) Access control service enforcing security policy by comparing security labels with security clearances. (See: discretionary access control, MAC, rule-based security policy.)
  - 2. (O) "A means of restricting access to objects based on the sensitivity... and the formal authorization... of subjects." [DoD1]
- **manipulation detection code** (D): Synonym for "checksum".
  - Deprecated Term: IDOCs SHOULD NOT use; instead use "protected checksum" or appropriate specific type.
- **marking**: See time stamp, security marking.
- **MARS** (O): Symmetric 128-bit block cipher with variable key length (128-448 bits); candidate for AES.
- **Martian** (D): /slang/ Packet arriving unexpectedly at wrong address due to incorrect routing or ill-formed IP address. [R1208]
  - Deprecated Term: IDOCs SHOULD NOT use.
- **masquerade** (I): Type of threat action where unauthorized entity gains access by illegitimately posing as authorized entity. (See: deception.)
  - Subtypes: Spoof, Malicious logic.
- **MCA** (O): See merchant certification authority.
- **MD2** (N): Cryptographic hash [R1319] producing 128-bit result; designed by Ron Rivest; similar to MD4 and MD5 but slower.
- **MD4** (N): Cryptographic hash [R1320] producing 128-bit result; designed by Ron Rivest. (See: SHA-1.)
- **MD5** (N): Cryptographic hash [R1321] producing 128-bit result; improved version of MD4.
- **merchant** (O): /SET/ "A seller of goods, services, and/or other information who accepts payment for these items electronically." [SET2]
- **merchant certificate** (O): /SET/ Public-key certificate issued to a merchant; sometimes refers to pair for signature and encryption.
- **merchant certification authority (MCA)** (O): /SET/ CA issuing digital certificates to merchants, operated on behalf of payment card brand or acquirer. [SET2]
- **mesh PKI** (I): Non-hierarchical PKI with several trusted CAs; peer-to-peer relationships; cross-certificates. (Compare: hierarchical PKI, trust-file PKI.)
- **Message Authentication Code (MAC), message authentication code**
  - 1. (N) /capitalized/ ANSI standard for checksum computed with keyed hash based on DES. [A9009] (See: MAC.)
  - 2. (D) /not capitalized/ Synonym for "error detection code".
    - Deprecated Term: IDOCs SHOULD NOT use uncapitalized form.
- **message digest** (D): Synonym for "hash result". (See: cryptographic hash.)
  - Deprecated Term: IDOCs SHOULD NOT use.
- **message handling system** (D): Synonym for Internet electronic mail system.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **Message Handling System** (O): ITU-T system concept for comprehensive OSI store-and-forward message exchange. (See: X.400.)
- **message indicator**
  - 1. (D) /cryptographic function/ Synonym for "initialization value". (Compare: indicator.)
  - 2. (D) "Sequence of bits transmitted over a communications system for synchronizing cryptographic equipment." [C4009]
    - Deprecated Term: IDOCs SHOULD NOT use as synonym for initialization value.
- **message integrity check / message integrity code (MIC)** (D): Synonyms for some form of "checksum".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **Message Security Protocol (MSP)** (N): Secure message handling protocol for X.400 and Internet mail; developed by NSA's SDNS program.
- **meta-data** (I): Descriptive information about a data object; data about data. (See: security label. Compare: metadata.)
  - Tutorial: Serves management purposes; can be associated explicitly or implicitly.
- **metadata, Metadata(trademark), METADATA(trademark)** (D): Proprietary variants of "meta-data".
  - Deprecated Usage: IDOCs SHOULD use only "meta-data".
- **MHS** (N): See message handling system.
- **MIC** (D): See message integrity code.
- **MIME** (I): See Multipurpose Internet Mail Extensions.
- **MIME Object Security Services (MOSS)** (I): Internet protocol applying end-to-end encryption and digital signature to MIME content. Based on PEM. (See: S/MIME.)
- **Minimum Interoperability Specification for PKI Components (MISPC)** (N): Technical description for interoperation of PKI components; profile of certificate and CRL extensions and transactions. [SP15]
- **misappropriation** (I): Type of threat action where entity assumes unauthorized logical or physical control of system resource. (See: usurpation.)
  - Subtypes: Theft of data, theft of service, theft of functionality.
- **MISPC** (N): See Minimum Interoperability Specification for PKI Components.
- **MISSI** (O): Multilevel Information System Security Initiative; NSA program to encourage development of interoperable modular products for secure network information systems. (See: MSP, SP3, SP4.)
- **MISSI user** (O): /MISSI/ System entity that is subject of one or more MISSI X.509 certificates. (See: personality.)
  - Tutorial: Includes end users and authorities; usually person but may be machine.
- **mission** (I): Statement of long-term duty or short-term task assigned to organization or system.
- **mission critical** (I): Condition where denial of access or lack of availability would jeopardize primary mission function. (See: Critical. Compare: mission essential.)
- **mission essential** (O): /U.S. DoD/ Materiel authorized and available to accomplish assigned missions. [JP1] (Compare: mission critical.)
- **misuse**
  - 1. (I) Intentional use of system resources for other than authorized purposes. (See: misuse detection.)
  - 2. (I) Type of threat action causing system component to perform detrimental function. (See: usurpation.)
    - Subtypes: Tampering, Malicious logic, Violation of authorizations.
- **misuse detection** (I): Intrusion detection method based on rules specifying events or properties symptomatic of security incidents. (See: IDS, misuse. Compare: anomaly detection.)
- **MLS** (I): See multilevel secure.
- **mobile code**
  - 1a. (I) Software from remote server transmitted across network and executed on local client without explicit initiation. (Compare: active content.)
  - 1b. (O) /U.S. DoD/ "Software modules obtained from remote systems, transferred across a network, and then downloaded and executed on local systems without explicit installation or execution." [JP1]
  - 2a. (O) /U.S. DoD/ Technology for executable information delivered and executed on any architecture with appropriate host environment.
  - 2b. (O) "Programs (e.g., script, macro, or other portable instruction) that can be shipped unchanged to a heterogeneous collection of platforms and executed with identical semantics" [SP28]
    - Tutorial: Might be malicious; code signing and sandbox reduce risks.
- **mode / mode of operation**
  - 1. (I) /cryptographic operation/ Technique for enhancing effect of cryptographic algorithm or adapting for application. (See: CBC, CCM, CMAC, CFB, CTR, ECB, OFB.)
  - 2. (I) /system operation/ Type of security policy stating classification levels and clearances of users. (See: compartmented security mode, controlled security mode, dedicated security mode, multilevel security mode, partitioned security mode, system-high security mode.)
  - 3. (I) /IKE/ IKE refers to exchanges of messages as "modes": Main mode and Quick mode.
- **model**: See formal model, security model.
- **modulus** (I): Defining constant in modular arithmetic; part of public key in asymmetric cryptography. (See: Diffie-Hellman-Merkle, RSA.)
- **Mondex** (O): Smartcard-based electronic money system using cryptography for Internet payments. (See: IOTP.)
- **Morris Worm** (I): Worm program that flooded ARPANET in November 1988, causing widespread problems. [R1135] (See: community risk, worm.)
- **MOSS** (I): See MIME Object Security Services.
- **MQV** (N): Key-agreement protocol based on Diffie-Hellman-Merkle. [Mene]
- **MSP** (N): See Message Security Protocol.
- **multicast security**: See secure multicast.
- **Multics** (N): MLS computer timesharing system designed 1965-69; one of first with security as primary goal; rated TCSEC Class B2.
- **multilevel secure (MLS)** (I): Information system trusted to contain and maintain separation between resources of different security levels. Examples: BLACKER, CANEWARE, KSOS, Multics, SCOMP.
  - Usage: Permits concurrent access by users with different authorizations.
- **multilevel security mode**
  - 1. (N) Mode of system operation where two or more security levels are handled concurrently, some users lack clearance/need-to-know for some data; separation depends on OS control. (Compare: controlled mode.)
  - 2. (O) Mode where (a) some users lack clearance for all data, (b) all users have proper clearance and approval for data they access, (c) all users have need-to-know. [C4009] (See: formal access approval, protection level.)
- **Multipurpose Internet Mail Extensions (MIME)** (I): Internet protocol (RFC 2045) enhancing basic email format (RFC 822) to support character sets, non-textual content, multi-part content. (See: S/MIME.)
- **mutual suspicion** (I): State where two interacting entities cannot trust each other to function correctly regarding security requirement.
- **name** (I): Synonym for "identifier".
- **naming authority** (O): /U.S. DoD/ Entity responsible for assigning DNs and ensuring uniqueness. [DoD9]
- **National Computer Security Center (NCSC)** (O): U.S. DoD organization in NSA responsible for trusted systems evaluation. (See: Rainbow Series, TCSEC.)
- **National Information Assurance Partnership (NIAP)** (N): Joint initiative of NIST and NSA to enhance quality of security products through objective evaluation.
  - Tutorial: Develops tests, collaborates on protection profiles, accredits labs.
- **National Institute of Standards and Technology (NIST)** (N): U.S. Department of Commerce organization responsible for INFOSEC standards for sensitive unclassified information. (See: ANSI, DES, DSA, DSS, FIPS, NIAP, NSA.)
- **National Reliability and Interoperability Council (NRIC)** (N): Advisory committee to FCC providing recommendations on reliability, interoperability, robustness, security of communications networks.
- **national security** (O): /U.S. Government/ National defense or foreign relations of the United States.
- **National Security Agency (NSA)** (N): U.S. DoD organization with primary responsibility for INFOSEC standards for classified information and national security systems. (See: FORTEZZA, KEA, MISSI, national security system, NIAP, NIST, SKIPJACK.)
- **national security information** (O): /U.S. Government/ Information determined to require protection against unauthorized disclosure under Executive Order 12958. [C4009]
- **national security system** (O): /U.S. Government/ Any Government-operated information system whose function involves intelligence, cryptologic, command and control of military forces, or weapon systems; not including routine administrative applications. (Title 40 U.S.C. Section 1552) (See: type 2 product.)
- **natural disaster** (I): /threat action/ See secondary definitions under "corruption" and "incapacitation".
- **NCSC** (O): See National Computer Security Center.
- **need to know, need-to-know** (I): Necessity for access to specific information required to carry out official duties.
  - Usage: Compound used as adjective or noun.
- **network** (I): Information system comprising collection of interconnected nodes. (See: computer network.)
- **Network Hardware Layer** (I): See Internet Protocol Suite.
- **Network Interface Layer** (I): See Internet Protocol Suite.
- **Network Layer Security Protocol (NLSP)** (N): OSI protocol (ISO 11577) for end-to-end encryption at top of OSIRM Layer 3. Derived from SP3. (Compare: IPsec.)
- **Network Substrate Layer** (I): Synonym for "Network Hardware Layer".
- **network weaving** (I): Penetration technique where intruder uses multiple linked networks to avoid detection and traceback. [C4009]
- **NIAP** (N): See National Information Assurance Partnership.
- **nibble** (D): Half of a byte (usually 4 bits).
  - Deprecated Term: IDOCs SHOULD NOT use; instead state size explicitly.
- **NIPRNET** (O): U.S. DoD's Non-Classified Internet Protocol Router Network; part of Internet used for official DoD business.
- **NIST** (N): See National Institute of Standards and Technology.
- **NLSP** (N): See Network Layer Security Protocol.
- **no-lone zone** (I): Room or area requiring occupancy by two or more appropriately authorized persons. [C4009] (See: dual control.)
- **no-PIN ORA (NORA)** (O): /MISSI/ Organizational RA operating in mode without card management functions; no knowledge of SSO PIN or user PIN.
- **node** (I): Collection of related subsystems at a single site. (See: site.)
- **nonce** (I): Random or non-repeating value included in data exchange to guarantee liveness and protect against replay attacks. (See: fresh.)
- **non-critical**: See critical.
- **non-repudiation service**
  - 1. (I) Security service providing protection against false denial of involvement in association. (See: repudiation, time stamp.)
    - Tutorial: Two types: proof of origin, proof of receipt.
  - 2. (D) "Assurance [that] the sender of data is provided with proof of delivery and the recipient provided with proof of the sender's identity, so neither can later deny having processed the data." [C4009]
    - Deprecated Definition: IDOCs SHOULD NOT use definition 2.
    - Usage: IDOCs SHOULD distinguish between technical non-repudiation and legal non-repudiation.
    - Tutorial: Does not prevent repudiation; provides evidence for dispute resolution. Phases described.
- **non-repudiation with proof of origin** (I): Security service providing recipient with evidence proving origin; protects against false denial by originator. (See: non-repudiation service.)
- **non-repudiation with proof of receipt** (I): Security service providing originator with evidence proving receipt; protects against false denial by recipient.
- **non-volatile media** (I): Storage media providing stable storage without external power. (Compare: permanent storage, volatile media.)
- **NORA** (O): See no-PIN ORA.
- **notarization** (I): Registration of data under authority of trusted third party, enabling subsequent assurance of data characteristics. [I7498-2] (See: digital notary.)
- **NRIC** (N): See Network Reliability and Interoperability Council.
- **NSA** (N): See National Security Agency.
- **null** (N): /encryption/ "Dummy letter, letter symbol, or code group inserted into an encrypted message to delay or prevent its decryption or to complete encrypted groups." [C4009]
- **NULL encryption algorithm** (I): Algorithm doing nothing to transform plaintext; used in ESP as no-op option. [R2410] (Compare: null.)
- **OAKLEY** (I): Key establishment protocol (superseded by IKE) based on Diffie-Hellman-Merkle; designed as compatible component of ISAKMP. [R2412]
  - Tutorial: Provides authentication, forward secrecy, key updates, user-defined groups.
- **object** (I): /formal model/ System component containing or receiving information. (See: Bell-LaPadula model, object reuse, trusted system.)
- **object identifier (OID)**
  - 1. (N) Official globally unique name written as sequence of integers, used in abstract specifications and protocol negotiation.
  - 2. (O) "A value (distinguishable from all other such values) [that] is associated with an object." [X680]
    - Tutorial: Leaf of OID tree; arcs labeled with integers; tree has three roots: ITU-T, ISO, joint.
- **object reuse** (N): /COMPUSEC/ Reassignment and reuse of storage area that once contained sensitive data; requires erasing or purging. [NCS04] (See: object.)
- **obstruction** (I): Type of threat action interrupting delivery of system services by hindering operations. (See: disruption.)
  - Subtypes: Interference, Overload.
- **OCSP** (I): See Online Certificate Status Protocol.
- **octet** (I): Data unit of eight bits. (Compare: byte.)
  - Usage: Preferred in networking over "byte".
- **OFB** (N): See output feedback.
- **off-line attack** (I): See secondary definition under "attack".
- **ohnosecond** (D): Joke term for minuscule fraction of time in which you realize private key is compromised.
  - Deprecated Usage: IDOCs SHOULD NOT use.
- **OID** (N): See object identifier.
- **Online Certificate Status Protocol (OCSP)** (I): Internet protocol [R2560] used by client to obtain validity status of digital certificate from server.
  - Tutorial: Provides timely revocation status; may be supplement to CRLs.
- **one-time pad**
  - 1. (N) Manual encryption system in form of paper pad.
  - 2. (I) Encryption algorithm with random key used only once; only unbreakable encryption. [Schn]
- **one-time password, One-Time Password (OTP)**
  - 1. (I) /not capitalized/ Simple authentication technique using each password only once; counters replay attack.
  - 2. (I) /capitalized/ Internet protocol [R2289] generating one-time passwords using cryptographic hash.
- **one-way encryption** (I): Irreversible transformation of plaintext to ciphertext; plaintext cannot be recovered even if key known. (See: brute force, encryption.)
- **one-way function** (I): Function easy to compute but computationally difficult to invert. [X509]
  - Deprecated Usage: IDOCs SHOULD NOT use as synonym for cryptographic hash.
- **onion routing** (I): System providing data confidentiality, traffic-flow confidentiality, and source anonymity.
  - Tutorial: Source sends packet to proxy; builds anonymous connection through routers; uses layered encrypted "onion" packets.
- **open security environment** (O): /U.S. DoD/ Environment where application developers lack sufficient clearance or configuration control does not prevent malicious logic. [NCS04] (Compare: closed security environment.)
- **open storage** (N): /U.S. Government/ Storage of classified information in accredited facility but not in approved secure containers while facility unoccupied. [C4009]
- **Open Systems Interconnection (OSI) Reference Model (OSIRM)** (N): Joint ISO/ITU-T standard for seven-layer communication framework. (See: OSIRM Security Architecture. Compare: Internet Protocol Suite.)
  - Tutorial: Layers 7-1: Application, Presentation, Session, Transport, Network, Data Link, Physical.
- **operational integrity** (I): Synonym for "system integrity".
- **operational security**
  - 1. (I) System capabilities needed to securely manage a system or manage security features. (Compare: operations security (OPSEC).)
  - 2. (D) Synonym for "administrative security".
    - Deprecated Definition: IDOCs SHOULD NOT use as synonym.
- **operations security (OPSEC)** (I): Process to identify, control, and protect evidence of planning and execution of sensitive activities. (See: communications cover. Compare: operational security.)
- **operator** (I): Person authorized to direct selected functions of system. (Compare: manager, user.)
- **OPSEC**
  - 1. (I) Abbreviation for "operations security".
  - 2. (D) Abbreviation for "operational security".
    - Deprecated Usage: IDOCs SHOULD NOT use for "operational security".
- **ORA**: See organizational registration authority.
- **Orange Book** (D): /slang/ Synonym for "Trusted Computer System Evaluation Criteria" [CSC1, DoD1].
  - Deprecated Usage: IDOCs SHOULD NOT use; instead use full name or TCSEC.
- **organizational certificate**
  - 1. (I) X.509 public-key certificate where "subject" field contains name of institution or set, not individual. (Compare: persona certificate, role certificate.)
  - 2. (O) /MISSI/ Type of MISSI certificate issued to support organizational message handling for U.S. DoD's DMS.
- **organizational registration authority (ORA)**
  - 1. (I) /PKI/ An RA for an organization.
  - 2. (O) /MISSI/ End entity assisting PCA or CA with registration; may assist with card management; does not sign certificates or CRLs. (See: no-PIN ORA, SSO-PIN ORA, user-PIN ORA.)
- **origin authentication** (D): Synonym for "data origin authentication".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **origin authenticity** (D): Synonym for "data origin authentication".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **OSI, OSIRM** (N): See Open Systems Interconnection Reference Model.
- **OSIRM Security Architecture** (N): Part of OSIRM [I7498-2] specifying security services and mechanisms for communications protection. (See: security architecture.)
  - Tutorial: Includes allocation table of security services to layers.
- **OTAR** (N): See over-the-air rekeying.
- **OTP** (I): See One-Time Password.
- **out-of-band** (I): /adjective, adverb/ Information transfer using channel or method separate from main channel.
  - Tutorial: Often used to distribute shared secrets or root keys.
- **output feedback (OFB)** (N): Block cipher mode modifying ECB to operate on variable-length plaintext segments. [FP081] (See: block cipher, [SP38A].)
  - Tutorial: Feeds back output block and combines with plaintext via XOR.
- **outside attack** (I): See secondary definition under "attack". Compare: outsider.
- **outsider** (I): User accessing system from outside security perimeter. (Compare: authorized user, insider, unauthorized user.)
- **over-the-air rekeying (OTAR)** (N): Changing key in remote cryptographic device via channel it is protecting. [C4009]
- **overload** (I): /threat action/ See secondary definition under "obstruction".
- **P1363** (N): See IEEE P1363.
- **PAA** (O): See policy approving authority.
- **package** (N): /Common Criteria/ Reusable set of functional or assurance components satisfying identified security objectives. (Compare: protection profile.)
  - Example: EALs are predefined assurance packages.
- **packet** (I): Block of data carried from source to destination through communication channel or network. (Compare: datagram, PDU.)
- **packet filter** (I): See secondary definition under "filtering router".
- **packet monkey** (D): /slang/ Someone who floods system with packets causing denial of service.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **pagejacking** (D): /slang/ Contraction of "Web page hijacking"; masquerade attack copying home page to attacker's server and diverting browsers.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **PAN** (O): See primary account number.
- **PAP** (I): See Password Authentication Protocol.
- **parity bit** (I): Checksum computed by binary sum of bits in block, discarding all but low-order bit. (See: checksum.)
- **partitioned security mode** (N): Mode where all users have necessary security clearances for all data, but some may not have formal access approval or need-to-know. (See: /system operation/ under "mode".)
- **PASS** (N): See personnel authentication system string.
- **passive attack** (I): See secondary definition under "attack".
- **passive user** (I): See secondary definition under "system user".
- **passive wiretapping** (I): Wiretapping attempting only to observe communication flow without altering it. (See: wiretapping. Compare: passive attack, active wiretapping.)
- **password**
  - 1a. (I) Secret data value (usually character string) presented to authenticate user's identity. (See: authentication information, challenge-response, PIN, simple authentication.)
  - 1b. (O) "A character string used to authenticate an identity." [CSC2]
  - 1c. (O) "A string of characters... used to authenticate an identity or to verify access authorization." [FP140]
  - 1d. (O) "A secret that a claimant memorizes and uses to authenticate his or her identity." [SP63]
    - Tutorial: Usually paired with user identifier; verified against stored value.
- **Password Authentication Protocol (PAP)** (I): Simple authentication mechanism in PPP; transmits identifier and password in cleartext. [R1334] (See: CHAP.)
- **password sniffing** (D): /slang/ Passive wiretapping to gain knowledge of passwords. (See: Deprecated Usage under "sniffing".)
- **path discovery** (I): Process of finding set of public-key certificates comprising certification path from trusted key to specific certificate.
- **path validation** (I): Process of validating all digital certificates in certification path and relationships. (See: certificate validation.)
  - Tutorial: RFC 3280 specifies algorithm.
- **payment card** (N): /SET/ Collectively refers to credit, debit, charge, bank cards. [SET2]
- **payment gateway** (O): /SET/ System operated by acquirer or third party providing electronic commerce services to merchants. [SET1, SET2]
- **payment gateway certification authority (SET PCA)** (O): /SET/ CA issuing certificates to payment gateways. (See: PCA.)
- **PC card** (N): Credit card-sized plug-in peripheral device. (See: FORTEZZA, PCMCIA.)
  - Tutorial: Three types (I, II, III) with 68-pin interface.
- **PCA** (D): Abbreviation of various kinds of "certification authority". (See: Internet PCA, MISSI PCA, SET PCA.)
  - Deprecated Usage: IDOCs SHOULD define at point of first use.
- **PCI** (N): See "protocol control information" under "protocol data unit".
- **PCMCIA** (N): Personal Computer Memory Card International Association; standardizes plug-in peripheral memory cards. (See: PC card.)
- **PDS** (N): See protective distribution system.
- **PDU** (N): See protocol data unit.
- **peer entity authentication** (I): "The corroboration that a peer entity in an association is the one claimed." [I7498-2] (See: authentication.)
- **peer entity authentication service** (I): Security service verifying identity of peer entity in association. (See: authentication, authentication service.)
  - Tutorial: Used at establishment or during association; requires association; valid only at current time.
- **PEM** (I): See Privacy Enhanced Mail.
- **penetrate**
  - 1a. (I) Circumvent system's security protections. (See: attack, break, violation.)
  - 1b. (I) Successfully and repeatedly gain unauthorized access to protected system resource. [Huff]
- **penetration** (I): /threat action/ See secondary definition under "intrusion".
- **penetration test** (I): System test where evaluators attempt to circumvent security features. [NCS04, SP42] (See: tiger team.)
  - Tutorial: Evaluates relative vulnerability; assumes knowledge of design and implementation.
- **perfect forward secrecy** (I): Property that compromise of long-term keying material does not compromise previously derived session keys. (Compare: public-key forward secrecy.)
  - Usage: Existing RFCs often use without precise definition. Challenge to community to develop taxonomy.
- **perimeter**: See security perimeter.
- **periods processing** (I): Mode where information of different sensitivities is processed at different times, with proper purging between periods. (See: color change.)
- **permanent storage** (I): Non-volatile media that can never be completely erased.
- **permission**
  - 1a. (I) Synonym for "authorization". (Compare: privilege.)
  - 1b. (N) Authorization or set of authorizations to perform security-relevant functions in role-based access control. [ANSI]
    - Tutorial: Positively stated authorization associated with roles.
- **persona certificate** (I): X.509 certificate issued to conceal true identity. (See: anonymity.) [R1422]
  - Tutorial: PEM designers intended CA not to vouch for identity; subject DN represents persona.
- **personal identification number (PIN)**
  - 1a. (I) Character string used as password to gain access to system resource. (See: authentication information.)
  - 1b. (O) Alphanumeric code or password used to authenticate identity.
    - Tutorial: Despite name, seldom serves as identifier; characters not necessarily numeric. FORTEZZA uses 12-character SSO PIN.
- **personal information** (I): Information about particular person that could cause harm if disclosed. Examples: medical record, credit card number.
- **personality**
  - 1. (I) Synonym for "principal".
  - 2. (O) /MISSI/ Set of MISSI X.509 certificates with same subject DN, stored on FORTEZZA PC card to support role.
    - Tutorial: User may have multiple personalities on card, each with label.
- **personnel authentication system string (PASS)** (N): See Tutorial under "personal identification number".
- **personnel security** (I): Procedures ensuring persons who access system have proper clearance, authorization, need-to-know. (See: security architecture.)
- **PGP(trademark)** (O): See Pretty Good Privacy(trademark).
- **phase 1 negotiation / phase 2 negotiation** (I): /ISAKMP/ See secondary definition under "Internet Security Association and Key Management Protocol".
- **phishing** (D): /slang/ Technique for acquiring sensitive data through fraudulent solicitation masquerading as legitimate business. (See: social engineering.)
  - Deprecated Term: IDOCs SHOULD NOT use.
- **Photuris** (I): UDP-based key establishment protocol for session keys; superseded by IKE.
- **phreaking** (D): Contraction of "telephone breaking"; attack on communication system. [Raym]
  - Deprecated Term: IDOCs SHOULD NOT use.
- **physical destruction** (I): /threat action/ See secondary definition under "incapacitation".
- **physical security** (I): Tangible means preventing unauthorized physical access to system. Examples: fences, locks, guards. [FP031, R1455] (See: security architecture.)
- **piggyback attack** (I): Form of active wiretapping gaining access via intervals of inactivity in legitimate connection.
  - Deprecated Usage: IDOCs SHOULD state definition.
- **PIN** (I): See personal identification number.
- **ping of death** (D): Denial-of-service attack sending improperly large ICMP echo request to cause destination failure.
  - Deprecated Term: IDOCs SHOULD NOT use; instead use specific term like "ping packet overflow attack".
- **ping sweep** (I): Attack sending ICMP echo requests to range of IP addresses to find hosts for probing. (See: ping of death. Compare: port scan.)
- **PKCS** (N): See Public-Key Cryptography Standards.
- **PKCS #5** (N): Standard for encrypting octet string with secret key derived from password. (See: RFC 2898)
- **PKCS #7** (N): Standard for syntax for data with cryptography (digital signatures, digital envelopes). (See: CMS.)
- **PKCS #10** (N): Standard for syntax for certification requests. (See: certification request.)
  - Tutorial: Contains DN, public key, signed; sent to CA.
- **PKCS #11** (N): Standard defining CAPI called "Cryptoki" for devices holding cryptographic information.
- **PKI** (I): See public-key infrastructure.
- **PKINIT** (I): Abbreviation for "Public Key Cryptography for Initial Authentication in Kerberos" (RFC 4556).
- **PKIX**
  - 1a. (I) Contraction of "Public-Key Infrastructure (X.509)"; IETF working group specifying architecture and protocols for X.509-based PKI services. [R3280, R4210]
  - 1b. (I) Collective name for that architecture and protocols.
    - Tutorial: Profiles X.509 v3 certificates and v2 CRLs; specifies operational and management protocols.
- **plain text**
  - 1. (I) /noun/ Data input to encryption process. (See: plaintext. Compare: cipher text, clear text.)
  - 2. (D) /noun/ Synonym for "clear text".
    - Deprecated Definition: IDOCs SHOULD NOT use as synonym for clear text.
- **plaintext**
  - 1. (O) /noun/ Synonym for "plain text".
  - 2. (I) /adjective/ Referring to plain text.
  - 3. (D) /noun/ Synonym for "cleartext".
    - Deprecated Definition: IDOCs SHOULD NOT use as synonym for cleartext.
- **PLI** (I): See Private Line Interface.
- **PMA** (N): See policy management authority.
- **Point-to-Point Protocol (PPP)** (I): Internet Standard protocol for encapsulation and transport of Layer 3 packets over Layer 2 link. Includes optional authentication. (See: CHAP, EAP, PAP.)
- **Point-to-Point Tunneling Protocol (PPTP)** (I): Client-server protocol enabling dial-up user to create virtual extension of link by tunneling PPP over IP. (See: L2TP.)
- **policy**
  - 1a. (I) Plan or course of action intended to affect decisions and deeds. (See: security policy.)
  - 1b. (O) Definite goal or method to guide future decisions. [R3198]
    - Deprecated Abbreviation: IDOCs SHOULD NOT use "policy" as abbreviation of "security policy" or "certificate policy".
    - Tutorial: Distinguish between practices, procedures, policies.
- **policy approval authority** (D): /PKI/ Synonym for "policy management authority". [PAG]
  - Deprecated Term: IDOCs SHOULD NOT use.
- **policy approving authority (PAA)** (O): /MISSI/ Top-level signing authority of MISSI certification hierarchy. (See: policy management authority, root registry.)
  - Tutorial: Registers PCAs, signs certificates, issues CRLs, may issue cross-certificates.
- **policy authority** (D): /PKI/ Synonym for "policy management authority". [PAG]
  - Deprecated Term: IDOCs SHOULD NOT use.
- **policy certification authority (Internet PCA)** (I): X.509-compliant CA at second level of Internet certification hierarchy, under IPRA. [R1422] (See: policy creation authority.)
- **policy creation authority (MISSI PCA)** (O): /MISSI/ Second level of MISSI certification hierarchy; administrative root of security policy domain. (See: policy certification authority.)
  - Tutorial: PCA's certificate issued by PAA; registers CAs, issues certificates, CRLs, CKLs.
- **policy management authority (PMA)** (I): /PKI/ Person or organization responsible for creating/approving certificate policies and CPSs, ensuring administration, approving cross-certification. [DoD9, PAG] (See: policy approving authority.)
- **policy mapping** (I): Recognizing equivalence between certificate policies in different domains. [X509]
- **policy rule** (I): Building block of security policy; defines conditions and specifies actions. [R3198]
- **POP3** (I): See Post Office Protocol, version 3.
- **POP3 APOP** (I): POP3 command using keyed hash (MD5) to authenticate client to server. (See: CRAM, POP3 AUTH, IMAP4 AUTHENTICATE.)
- **POP3 AUTH** (I): POP3 command [R1734] for optional authentication and security services. (See: POP3 APOP, IMAP4 AUTHENTICATE.)
- **port scan** (I): Technique sending client requests to range of service port addresses on host. (See: probe. Compare: ping sweep.)
  - Tutorial: Can be used for pre-attack surveillance or flooding.
- **positive authorization** (I): Principle that access is permitted only when explicitly granted; default is to refuse.
- **POSIX** (N): Standard defining operating system interface for application portability. [FP151, I9945]
  - Tutorial: P1003.1 supports discretionary access control; P1003.6 adds MAC, audit, etc.
- **Post Office Protocol, version 3 (POP3)** (I): Internet Standard protocol for client to retrieve mail from server. (See: IMAP4.)
- **PPP** (I): See Point-to-Point Protocol.
- **PPTP** (I): See Point-to-Point Tunneling Protocol.
- **preauthorization** (N): /PKI/ CAW feature enabling automatic validation of certification requests against pre-provided data.
- **precedence**
  - 1. (I) /information system/ Ranking determining order of processing.
  - 2. (N) /communication system/ Designation stating importance or urgency. [F1037] (See: availability, critical, preemption.)
- **preemption** (N): Seizure of system resources from lower-precedence communication to serve higher-precedence one. [F1037]
- **Pretty Good Privacy(trademark) (PGP(trademark))** (O): Trademarks of Network Associates; cryptography for email security. (Compare: DKIM, MOSS, MSP, PEM, S/MIME.)
  - Tutorial: Uses symmetric and asymmetric algorithms; web of trust for key management.
- **prevention** (I): See secondary definition under "security".
- **primary account number (PAN)** (O): /SET/ Identifier for card issuer and cardholder; includes issuer identification number, account number, check digit. [SET2, I7812] (See: bank identification number.)
- **principal** (I): Specific identity claimed by user when accessing system.
  - Usage: Equivalent to login account identifier; each principal can spawn subjects.
  - (I) /Kerberos/ Uniquely identified client or server instance.
- **priority** (I): /information system/ Precedence for processing based on security importance.
- **privacy**
  - 1. (I) Right of entity to determine degree of interaction with environment, including sharing personal information. (See: HIPAA, personal information, Privacy Act of 1974.)
  - 2. (O) "The right of individuals to control or influence what information related to them may be collected and stored..." [I7498-2]
  - 3. (D) Synonym for "data confidentiality".
    - Deprecated Definition: IDOCs SHOULD NOT use as synonym.
- **Privacy Act of 1974** (O): U.S. law balancing government's need to maintain data with individuals' privacy rights.
  - Tutorial: Four policy objectives: restrict disclosure, grant access, allow amendment, establish fair information practices.
- **Privacy Enhanced Mail (PEM)** (I): Internet protocol for confidentiality, integrity, and origin authentication for email. [R1421, R1422] (Compare: DKIM, MOSS, MSP, PGP, S/MIME.)
  - Tutorial: Uses symmetric encryption, asymmetric key distribution, digital signatures; certification hierarchy.
- **private component** (I): Synonym for "private key".
  - Deprecated Usage: IDOCs SHOULD NOT use in most cases; may use when discussing key pair.
- **private extension** (I): See secondary definition under "extension".
- **private key**
  - 1. (I) Secret component of cryptographic key pair for asymmetric cryptography. (See: key pair, public key, secret key.)
  - 2. (O) "That key of a user's key pair which is known only by that user." [X509]
- **Private Line Interface (PLI)** (I): First end-to-end packet encryption system for computer network; developed by BBN. [B1822] (Compare: IPLI.)
- **privilege**
  - 1a. (I) /access control/ Synonym for "authorization". (Compare: permission.)
  - 1b. (I) /computer platform/ Authorization to perform security-relevant function in operating system.
- **privilege management infrastructure** (O): Infrastructure supporting management of privileges in relation to PKI; processes for attribute certificates. [X509]
  - Deprecated Usage: IDOCs SHOULD NOT use this term.
- **privileged process** (I): Computer process authorized to perform security-relevant functions that ordinary processes cannot. (See: privilege, trusted process.)
- **privileged user** (I): User with access to system control, monitoring, or administration functions.
  - Tutorial: Includes users with near complete control, change control parameters, or monitor security functions.
- **probe** (I): /verb/ Technique attempting to access system to learn something. (See: port scan.)
  - Tutorial: Purpose may be offensive or defensive.
- **procedural security** (D): Synonym for "administrative security".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **profile**: See certificate profile, protection profile.
- **proof-of-possession protocol** (I): Protocol whereby entity proves possession and control of cryptographic key or secret. (See: zero-knowledge proof.)
- **proprietary** (I): Refers to information owned and restricted.
- **protected checksum** (I): Checksum computed for data object by means that protect against active attacks. (See: digital signature, keyed hash.)
- **protective packaging** (N): Packaging techniques for COMSEC material to discourage penetration or reveal attempts. [C4009] (See: tamper-evident, tamper-resistant. Compare: QUADRANT.)
- **protection authority** (I): See secondary definition under "Internet Protocol Security Option".
- **protection level** (N): /U.S. Government/ Indication of trust needed in system's technical ability to enforce security policy for confidentiality.
  - Tutorial: Defines five protection levels based on user clearances and need-to-know.
- **protection profile** (N): /Common Criteria/ Implementation-independent set of security requirements for category of TOE. [CCIB] (See: target of evaluation. Compare: certificate profile, package.)
  - Tutorial: PP specifies functional requirements; ST is used by vendors.
- **protection ring** (I): One of hierarchy of privileged operation modes giving certain access rights. (See: Multics.)
- **protective distribution system (PDS)** (N): Wireline or fiber-optic system for transmitting cleartext classified information through area of lesser classification. [N7003]
- **protocol**
  - 1a. (I) Set of rules to implement and control association between systems.
  - 1b. (I) Series of ordered steps performed by system entities to achieve joint objective. [A9042]
- **protocol control information (PCI)** (N): See secondary definition under "protocol data unit".
- **protocol data unit (PDU)** (N): Data packet defined for peer-to-peer transfers in protocol layer.
  - Tutorial: Consists of SDU and PCI.
- **protocol suite** (I): Complementary collection of communication protocols. (See: IPS, OSI.)
- **proxy**
  - 1. (I) Computer process acting on behalf of user or client.
  - 2. (I) Process that relays application transactions between client and server, appearing to each as the other. (See: SOCKS.)
    - Tutorial: In firewall, runs on bastion host; may perform caching, logging.
- **proxy certificate** (I): X.509 certificate derived from end-entity certificate for establishing proxies and delegating authorizations. [R3820]
  - Tutorial: Contains critical extension; signed by private key of end-entity certificate; subject DN derived from issuer DN.
- **pseudorandom** (I): Sequence appearing random but generated by deterministic algorithm. (See: compression, random, random number generator.)
- **pseudorandom number generator** (I): See secondary definition under "random number generator".
- **public component** (I): Synonym for "public key".
  - Deprecated Usage: IDOCs SHOULD NOT use in most cases; may use when discussing key pair.
- **public key**
  - 1. (I) Publicly disclosable component of key pair for asymmetric cryptography. (See: key pair. Compare: private key.)
  - 2. (O) "That key of a user's key pair which is publicly known." [X509]
- **public-key certificate**
  - 1. (I) Digital certificate binding system entity's identifier to public key value. (See: X.509 public-key certificate.)
  - 2. (O) "The public key of a user, together with some other information, rendered unforgeable by encipherment with the private key of the certification authority which issued it." [X509]
    - Tutorial: Unforgeable; can be published.
- **public-key cryptography** (I): Synonym for "asymmetric cryptography".
- **Public-Key Cryptography Standards (PKCS)** (N): Series of specifications for data structures and algorithms in asymmetric cryptography. [PKCS] (See: PKCS #5 through #11.)
  - Tutorial: Began 1991; widely used but not official standards.
- **public-key forward secrecy (PFS)** (I): Property ensuring session key derived from long-term keys will not be compromised if one private key is compromised in future.
- **public-key Kerberos** (I): See Tutorial under "Kerberos", PKINIT.
- **public-key infrastructure (PKI)**
  - 1. (I) System of CAs (and optionally RAs) performing certificate management, archive management, key management, token management.
  - 2. (I) /PKIX/ Set of hardware, software, people, policies, procedures to create, manage, store, distribute, revoke digital certificates.
    - Tutorial: Core functions: registration, issuance, revocation, archiving.
- **purge**
  - 1. (I) Synonym for "erase".
  - 2. (O) /U.S. Government/ Use degaussing or other methods to render magnetically stored data unusable and irrecoverable. [C4009]
- **QUADRANT** (O): /U.S. Government/ Technology making cryptographic equipment tamper-resistant. [C4009] (Compare: protective packaging, TEMPEST.)
- **qualified certificate** (I): Public-key certificate for high assurance identification meeting legal requirements. (See: European Directive on Electronic Signature.) [R3739]
- **quick mode** (I): See /IKE/ under "mode".
- **RA** (I): See registration authority.
- **RA domains** (I): Feature of CAW dividing certification request responsibility among multiple RAs.
- **RADIUS** (I): See Remote Authentication Dial-In User Service.
- **Rainbow Series** (O): /COMPUSEC/ Set of documents issued by NCSC discussing TCSEC. (See: Green Book, Orange Book, Red Book, Yellow Book.)
- **random** (I): Unpredictable. [SP22, Knut, R4086]
  - Random sequence: each value independent and equally probable.
- **random number generator** (I): Process to generate random sequence.
  - Tutorial: Two types: (True) random number generator (non-deterministic) and pseudorandom number generator (deterministic).
- **RBAC** (N): See role-based access control, rule-based access control.
  - Deprecated Usage: IDOCs SHOULD define.
- **RC2, RC4, RC6** (N): See Rivest Cipher #2, #4, #6.
- **read** (I): /security model/ Operation causing flow of information from object to subject. (See: access mode. Compare: write.)
- **realm** (I): /Kerberos/ Domain of Kerberized clients, servers, and authentication servers under same security policy.
- **recovery**
  - 1. (I) /cryptography/ Learning cryptographic data through cryptanalysis. (See: key recovery, data recovery.)
  - 2a. (I) /system integrity/ Restoring secure state after failure or attack.
  - 2b. (I) /system integrity/ Restoring system assets and operation after damage. (See: contingency plan.)
- **RED**
  - 1. (N) Designation for clear text data and equipment handling it. (See: BCR, color change, RED/BLACK separation. Compare: BLACK.)
  - 2. (O) /U.S. Government/ Applied to information systems where unencrypted national security information is processed. [C4009]
- **RED/BLACK separation** (N): Architectural concept strictly separating parts handling plain text from those handling cipher text.
- **Red Book** (D): /slang/ Synonym for "Trusted Network Interpretation of the Trusted Computer System Evaluation Criteria" [NCS05].
  - Deprecated Term: IDOCs SHOULD NOT use.
- **RED key** (N): Cleartext key usable as is. (See: RED. Compare: BLACK key.)
- **reference monitor** (I): "An access control concept that refers to an abstract machine that mediates all accesses to objects by subjects." [NCS04] (See: security kernel.)
  - Tutorial: Should be complete, isolated, verifiable.
- **reflection attack** (I): Attack where valid data transmission is replayed to originator by attacker. (Compare: indirect attack, replay attack.)
- **reflector attack** (D): Synonym for "indirect attack".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **registered user** (I): System entity authorized to receive products/services or access resources. (See: registration, user.)
- **registration**
  - 1. (I) /information system/ Process initializing identity, establishing identifier, associating authentication information.
  - 2. (I) /PKI/ Administrative act establishing entity's name and attributes prior to certificate issuance.
    - Tutorial: May be done directly by CA or indirectly by RA.
- **registration authority (RA)**
  - 1. (I) Optional PKI entity not signing certificates or CRLs, but recording/verifying information needed by CA. (See: ORA, registration.)
  - 2. (I) /PKIX/ Optional component, may perform identity authentication, name assignment, key generation, token distribution, revocation reporting. [R4210]
    - Tutorial: Tasks may include personal authentication, name assignment, token distribution, revocation reporting, key generation.
  - 3. (O) /SET/ "An independent third-party organization that processes payment card applications." [SET2]
- **regrade** (I): Deliberately change security level of information in authorized manner. (See: downgrade, upgrade.)
- **rekey** (I): Change value of cryptographic key in use. (See: certificate rekey.)
- **reliability** (I): Ability of system to perform required function under stated conditions for specified period. (Compare: availability, survivability.)
- **reliable human review** (I): Manual or automated process ensuring human examines digital object to determine permitted transfer according to security policy. (See: guard.)
- **relying party** (I): Synonym for "certificate user".
  - Usage: Legal context.
- **remanence** (I): Residual information recoverable from storage medium after clearing. (See: clear, magnetic remanence, purge.)
- **Remote Authentication Dial-In User Service (RADIUS)** (I): Internet protocol [R2865] for carrying dial-in users' authentication and configuration between server and network access server.
- **renew**: See certificate renewal.
- **reordering** (I): /packet/ See secondary definition under "stream integrity service".
- **replay attack** (I): Attack where valid data transmission is maliciously repeated. (See: active wiretapping, fresh, liveness, nonce. Compare: indirect attack, reflection attack.)
- **repository**
  - 1. (I) System for storing and distributing digital certificates and related information. (Compare: archive, directory.)
  - 2. (O) "A trustworthy system for storing and retrieving certificates or other information relevant to certificates." [DSG]
- **repudiation**
  - 1. (I) Denial by system entity of having participated in association. (See: accountability, non-repudiation service.)
  - 2. (I) Type of threat action where entity falsely denies responsibility. (See: deception.)
    - Subtypes: False denial of origin, false denial of receipt.
  - 3. (O) /OSIRM/ "Denial by one of the entities involved in a communication of having participated in all or part of the communication." [I7498-2]
- **Request for Comment (RFC)**
  - 1. (I) Document in archival series for official IDOCs and publications of IESG, IAB, and Internet community. (RFC 2026, 2223)
  - 2. (D) Popularly misused synonym for document on Internet Standards Track.
    - Deprecated Definition: IDOCs SHOULD NOT use.
- **residual risk** (I): Portion of risk remaining after countermeasures applied. (Compare: acceptable risk, risk analysis.)
- **restore**: See card restore.
- **reverse engineering** (I): /threat action/ See secondary definition under "intrusion".
- **revocation**: See certificate revocation.
- **revocation date** (N): /X.509/ Date-time field in CRL entry stating when revocation occurred. (See: invalidity date.)
  - Tutorial: May not resolve all disputes.
- **revocation list**: See certificate revocation list.
- **revoke** (I): See certificate revocation.
- **RFC** (I): See Request for Comment.
- **Rijndael** (N): Symmetric block cipher winning AES competition. [Daem] (See: Advanced Encryption Standard.)
- **risk**
  - 1. (I) Expectation of loss expressed as probability that threat will exploit vulnerability. (See: residual risk.)
  - 2. (O) /SET/ "The possibility of loss because of one or more threats to information." [SET2]
    - Tutorial: Four ways to deal: avoidance, transference, limitation, assumption.
- **risk analysis** (I): Assessment systematically identifying valuable resources, threats, quantifying loss exposures, recommending countermeasures. (See: risk management, business-case analysis.)
  - Tutorial: Lists risks in order of cost and criticality.
- **risk assumption** (I): See secondary definition under "risk".
- **risk avoidance** (I): See secondary definition under "risk".
- **risk limitation** (I): See secondary definition under "risk".
- **risk management**
  - 1. (I) Process of identifying, measuring, controlling risks to reduce to acceptable level. (See: risk analysis.)
  - 2. (I) Process of controlling uncertain events affecting resources.
  - 3. (O) "The total process of identifying, controlling, and mitigating information system-related risks." [SP30]
- **risk transference** (I): See secondary definition under "risk".
- **Rivest Cipher #2 (RC2)** (N): Proprietary variable-key-length block cipher.
- **Rivest Cipher #4 (RC4)** (N): Proprietary variable-key-length stream cipher.
- **Rivest Cipher #6 (RC6)** (N): Symmetric block cipher candidate for AES.
- **Rivest-Shamir-Adleman (RSA)** (N): Algorithm for asymmetric cryptography. [RSA78]
  - Tutorial: Uses exponentiation modulo product of two large primes.
- **robustness** (N): See level of robustness.
- **role**
  - 1. (I) Job function or employment position to which entities assigned. (See: role-based access control.)
  - 2. (O) /Common Criteria/ Pre-defined set of rules establishing allowed interactions between user and TOE.
- **role-based access control** (I): Form of identity-based access controlling entities as functional positions. [Sand] (See: authorization, constraint, identity, principal, role.)
  - Tutorial: Diagram shows five relationships: assignments of identities and permissions to roles, role hierarchy, session selections.
- **role certificate** (I): Organizational certificate issued to entity that is member of set assigned to same role.
- **root, root CA**
  - 1. (I) /PKI/ CA directly trusted by end entity. (See: trust anchor, trusted CA.)
  - 2. (I) /hierarchical PKI/ Highest level CA in certification hierarchy.
  - 3. (I) /DNS/ Base of DNS name space tree.
  - 4. (O) /MISSI/ Name previously used for MISSI PCA.
  - 5. (O) /UNIX/ User account with all privileges (superuser).
- **root certificate**
  - 1. (I) /PKI/ Certificate for which subject is root.
  - 2. (I) /hierarchical PKI/ Self-signed certificate at top of hierarchy.
- **root key** (I): /PKI/ Public key for which private key held by root.
- **root registry** (O): /MISSI/ Name previously used for MISSI PAA.
- **ROT13** (I): See secondary definition under "Caesar cipher".
- **router**
  - 1a. (I) /IP/ Networked computer forwarding IP packets not addressed to itself.
  - 1b. (I) /IPS/ Gateway operating in IPS Internet Layer connecting subnetworks.
  - 1c. (N) /OSIRM/ Computer gateway at Layer 3.
- **RSA** (N): See Rivest-Shamir-Adleman.
- **rule**: See policy rule.
- **rule-based security policy** (I): "A security policy based on global rules imposed for all users." [I7498-2] (Compare: identity-based security policy, policy rule, RBAC.)
- **rules of behavior** (I): Body of security policy establishing responsibilities and expected behavior of entities.
- **S field** (D): See Security Level field.
- **S-BGP** (I): See Secure BGP.
- **S-HTTP** (I): See Secure Hypertext Transfer Protocol.
- **S/Key** (I): Security mechanism using cryptographic hash to generate one-time passwords for remote login. [R1760]
- **S/MIME** (I): See Secure/MIME.
- **SAD** (I): See Security Association Database.
- **safety** (I): Property of being free from risk of causing harm. (Compare: security.)
- **SAID** (I): See security association identifier.
- **salami swindle** (D): /slang/ Slicing small amount from each transaction for theft.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **salt** (I): Data value varying computation results so that exposed result cannot be reused by attacker. (Compare: initialization value.)
- **SAML** (N): See Security Assertion Markup Language.
- **sandbox** (I): Restricted execution environment preventing malicious software from accessing unauthorized resources.
- **sanitize**
  - 1. (I) Delete sensitive data from file, device, or system. (See: erase, zeroize.)
  - 2. (I) Modify data to declassify or downgrade.
- **SAP** (O): See special access program.
- **SASL** (I): See Simple Authentication and Security Layer.
- **SCA** (I): See subordinate certification authority.
- **scavenging** (I): /threat action/ See secondary definition under "exposure".
- **SCI** (O): See sensitive compartmented information.
- **SCIF** (O): See sensitive compartmented information facility.
- **SCOMP** (N): Secure COMmunications Processor; first system rated TCSEC Class A1.
- **screen room** (D): /slang/ Synonym for "shielded enclosure".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **screening router** (I): Synonym for "filtering router".
- **script kiddy** (D): /slang/ Cracker using existing attack techniques without ability to invent new exploits.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **SDE** (N): See Secure Data Exchange.
- **SDNS** (O): See Secure Data Network System.
- **SDU** (N): See "service data unit" under "protocol data unit".
- **seal**
  - 1. (I) Use asymmetric cryptography to encrypt plain text with public key so only holder of private key can learn plain text. [Chau] (Compare: shroud, wrap.)
    - Deprecated Usage: IDOCs SHOULD NOT use unless including definition.
  - 2. (D) Use cryptography to provide data integrity service.
    - Deprecated Definition: IDOCs SHOULD NOT use.
- **secret**
  - 1a. (I) /adjective/ Condition of information protected from being known.
  - 1b. (I) /noun/ Item of information protected.
- **secret key** (D): Key kept secret.
  - Deprecated Term: IDOCs SHOULD NOT use; use "private key" or just "key".
- **secret-key cryptography** (D): Synonym for "symmetric cryptography".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **Secure BGP (S-BGP)** (I): Project to secure Border Gateway Protocol.
  - Tutorial: Incorporates PKI, digital signatures in route attestations, IPsec.
- **Secure Data Exchange (SDE)** (N): LAN security protocol defined by IEEE 802.10.
- **Secure Data Network System (SDNS)** (O): NSA program developing security protocols for email, OSIRM Layers 3 and 4, and key management.
- **secure distribution** (I): See trusted distribution.
- **Secure Hash Algorithm (SHA)** (N): Cryptographic hash function producing output of selectable length.
- **Secure Hash Standard (SHS)** (N): U.S. Government standard specifying SHA. [FP180]
- **Secure Hypertext Transfer Protocol (S-HTTP)** (I): Protocol for client-server security services for HTTP. [R2660] (Compare: https.)
  - Tutorial: Supports multiple formats, key management, cryptographic algorithms.
- **Secure/MIME (S/MIME)** (I): Secure/Multipurpose Internet Mail Extensions for encryption and digital signatures. [R3851]
- **secure multicast** (I): Providing security services for multicast groups.
  - Tutorial: Three functional areas: data handling, group key management, multicast security policy.
- **Secure Shell(trademark) (SSH(trademark))** (N): Protocol for secure remote login and other services.
  - Tutorial: Three parts: transport layer, user authentication, connection protocol.
- **Secure Sockets Layer (SSL)** (N): Protocol using encryption for data confidentiality and integrity between client and server. (See: Transport Layer Security.)
  - Tutorial: Two layers: record protocol and management protocols.
- **secure state**
  - 1a. (I) System condition in conformance with security policy.
  - 1b. (I) /formal model/ Condition where no subject can access object unauthorized.
- **security**
  - 1a. (I) System condition resulting from measures to protect system.
  - 1b. (I) Condition where resources free from unauthorized access, change, destruction, loss.
  - 2. (I) Measures taken to protect system.
    - Tutorial: Six functions: deterrence, avoidance, prevention, detection, recovery, correction.
- **security architecture** (I): Plan and principles describing required security services, components, and performance levels. (See: defense in depth, IATF, OSIRM Security Architecture, security controls.)
  - Tutorial: Includes administrative, communication, computer, emanations, personnel, physical security.
- **Security Assertion Markup Language (SAML)** (N): XML-based protocol for exchanging security assertions about subjects. [SAML]
- **security association**
  - 1. (I) Relationship established between entities to protect data exchanged. (See: association, ISAKMP, SAD. Compare: session.)
  - 2. (I) /IPsec/ Simplex logical connection created for security with AH or ESP; identified by triple.
  - 3. (O) "A set of policy and cryptographic keys that provide security services to network traffic." [R3740]
  - 4. (O) "The totality of communications and security mechanisms... that securely binds together two security contexts." [DoD6]
- **Security Association Database (SAD)** (I): /IPsec/ Database containing parameters for each active security association. [R4301] (Compare: SPD.)
- **security association identifier (SAID)** (I): Data field in security protocol identifying security association for a PDU.
- **security assurance**
  - 1. (I) Attribute providing grounds for confidence that system enforces security policy.
  - 2. (I) Procedure ensuring system developed and operated as intended.
  - 3. (D) "The degree of confidence one has that the security controls operate correctly..." [SP12]
    - Deprecated Definition: IDOCs SHOULD NOT use definition 3.
  - 4. (D) /U.S. Government, identity authentication/ Degree of confidence in vetting process and identity credential use. [M0404]
    - Deprecated Definition: IDOCs SHOULD NOT use.
- **security audit** (I): Independent review of system records to determine adequacy of controls, detect breaches, recommend changes. [I7498-2, NCS01]
- **security audit trail** (I): Chronological record of system activities sufficient for reconstructing security-relevant events. [NCS04]
- **security by obscurity** (O): Attempting to maintain security by keeping design secret; discredited.
  - Tutorial: Algorithms should be strong and published.
- **security class** (D): Synonym for "security level".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **security clearance** (I): Determination that person is eligible for authorization to access sensitive information.
- **security compromise** (I): Security violation where resource exposed to unauthorized access.
- **security controls** (N): Management, operational, technical controls prescribed for information system. [FP199]
- **security doctrine** (I): Specified procedures for complying with security policy. (Compare: security mechanism, security policy.)
- **security domain**: See domain.
- **security environment** (I): Set of external entities, procedures, conditions affecting secure system development, operation, maintenance.
- **security event** (I): Occurrence relevant to system security. (See: security incident.)
- **security fault analysis** (I): Security analysis at gate logic level to determine properties when hardware fault encountered.
- **security function** (I): Function that must operate correctly to ensure adherence to security policy.
- **security gateway**
  - 1. (I) Internetwork gateway separating trusted from untrusted hosts. (See: firewall and guard.)
  - 2. (O) /IPsec/ "An intermediate system that implements IPsec protocols." [R4301]
- **security incident**
  - 1. (I) Security event involving security violation. (See: CERT, security event, security intrusion, security violation.)
  - 2. (D) "Any adverse event [that] compromises some aspect of computer or network security." [R2350]
    - Deprecated Definition: IDOCs SHOULD NOT use.
  - 3. (D) "A violation or imminent threat of violation of computer security policies..." [SP61]
    - Deprecated Definition: IDOCs SHOULD NOT use.
- **security intrusion** (I): Security event where intruder gains or attempts unauthorized access.
- **security kernel** (I): "The hardware, firmware, and software elements of a trusted computing base that implement the reference monitor concept." [NCS04] (See: kernel, TCB.)
- **security label** (I): Meta-data designating security-relevant attributes of system resource. (See: [R1457]. Compare: security marking.)
  - Deprecated usage: IDOCs SHOULD NOT confuse with security marking.
- **security level** (I): Combination of classification level and category designations representing sensitivity.
- **Security Level field** (I): 16-bit field in IPv4 security option (type 130).
  - Deprecated Abbreviation: IDOCs SHOULD NOT use "S field".
- **security management infrastructure (SMI)** (I): Components supporting security policy by monitoring, controlling, distributing information, reporting events.
  - Tutorial: Functions: controlling access, retrieving/archiving info, managing encryption.
- **security marking** (I): Physical marking bound to resource representing security label. (Compare: security label.)
- **security mechanism** (I): Method or device implementing security service. (Compare: security doctrine.)
  - Examples: Authentication exchange, checksum, digital signature, encryption.
- **security model** (I): Schematic description of entities and relationships providing security services. Example: Bell-LaPadula model.
- **security parameters index (SPI)**
  - 1. (I) /IPsec/ 32-bit identifier distinguishing among security associations at same destination.
  - 2. (I) /mobile IP/ 32-bit index identifying security association between nodes.
- **security perimeter** (I): Physical or logical boundary where particular security policy applies.
- **security policy**
  - 1. (I) Definite goal or method guiding decisions concerning security. [NCS03, R3198]
  - 2a. (I) Set of policy rules directing how system provides security services.
  - 2b. (O) Set of rules to administer, manage, control access to network resources. [R3060, R3198]
  - 2c. (O) /X.509/ Set of rules laid down by authority to govern use of security services.
  - 2d. (O) /Common Criteria/ Set of rules regulating asset management, protection, distribution within TOE.
    - Tutorial: Four layers: mission functions, domain practices, enclave services, agent mechanisms, platform devices.
- **Security Policy Database (SPD)** (I): /IPsec/ Database specifying policies for IPsec services. (Compare: SAD.)
- **Security Protocol 3 (SP3)** (O): Protocol providing connectionless data security at top of OSIRM Layer 3.
- **Security Protocol 4 (SP4)** (O): Protocol providing connectionless or connection-oriented security at bottom of OSIRM Layer 4.
- **security-relevant event** (D): Synonym for "security event".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **security-sensitive function** (D): Synonym for "security function".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **security service**
  - 1. (I) Processing or communication service providing specific protection. (See: access control service, audit, availability, confidentiality, integrity, origin authentication, non-repudiation, peer entity authentication, system integrity.)
  - 2. (O) "A service, provided by a layer of communicating open systems, [that] ensures adequate security of the systems or the data transfers." [I7498-2]
- **security situation** (I): /ISAKMP/ Set of all security-relevant information needed to decide required services.
- **security target** (N): /Common Criteria/ Set of security requirements and specifications for evaluation of TOE.
  - Tutorial: Parallels protection profile but with product-specific details.
- **security token** (I): See token.
- **security violation** (I): Act or event breaching security policy.
- **seed** (I): Input to pseudorandom number generator.
- **selective-field confidentiality** (I): Data confidentiality service preserving confidentiality for one or more fields of each packet.
  - Tutorial: Example: PIN encryption at ATM.
- **selective-field integrity** (I): Data integrity service preserving integrity for one or more fields of each packet.
  - Tutorial: SDU or PCI protection; PCI fields may be mutable (e.g., TTL).
- **self-signed certificate** (I): Public-key certificate where public key and private key used to sign are components of same key pair. (Compare: root certificate.)
- **semantic security** (I): Attribute of encryption algorithm that hides plain text and reveals no partial information.
- **semiformal** (I): Expressed in restricted syntax language with defined semantics. [CCIB]
- **sensitive** (I): Condition where loss of confidentiality or integrity would adversely affect owner or user.
- **sensitive compartmented information (SCI)** (O): /U.S. Government/ Classified information from intelligence sources requiring handling within formal control systems. [C4009]
- **sensitive compartmented information facility (SCIF)** (O): /U.S. Government/ Accredited area where SCI may be stored, used, discussed. [C4009]
- **sensitive information**
  - 1. (I) Information whose disclosure, alteration, destruction could adversely affect owner/user.
  - 2. (O) /U.S. Government/ Information whose loss, misuse, unauthorized access/modification could adversely affect national interest or privacy.
- **sensitivity label** (D): Synonym for "classification label".
  - Deprecated term: IDOCs SHOULD NOT use.
- **sensitivity level** (D): Synonym for "classification level".
  - Deprecated term: IDOCs SHOULD NOT use.
- **separation of duties** (I): Practice of dividing steps among different entities to prevent subversion.
- **serial number**: See certificate serial number.
- **Serpent** (O): Symmetric 128-bit block cipher AES candidate.
- **server** (I): System entity providing service in response to client requests.
- **service data unit (SDU)** (N): See secondary definition under "protocol data unit".
- **session**
  - 1a. (I) /computer usage/ Continuous period initiated by login.
  - 1b. (I) /computer activity/ Set of transactions during period.
  - 2. (I) /access control/ Temporary mapping of principal to roles.
  - 3. (I) /computer network/ Persistent temporary association between user agent and second process.
- **session key** (I): Temporary key used for short period in symmetric encryption.
- **SET(trademark)** (O): See SET Secure Electronic Transaction(trademark).
- **SET private extension** (O): Private extension defined by SET for X.509 certificates.
- **SET qualifier** (O): Certificate policy qualifier providing location and content of SET CP.
- **SET Secure Electronic Transaction(trademark) or SET(trademark)** (N): Protocol for secure payment card transactions over unsecured networks. [SET1]
- **SETCo** (O): LLC formed by MasterCard and Visa for implementing SET standard.
- **SHA, SHA-1, SHA-2** (N): See Secure Hash Algorithm.
- **shared identity** (I): See secondary definition under "identity".
- **shared secret** (D): Synonym for "cryptographic key" or "password".
  - Deprecated Usage: IDOCs SHOULD define.
- **shielded enclosure** (O): Room or container designed to attenuate electromagnetic radiation. [C4009] (Compare: SCIF.)
- **short title** (O): Identifying combination of letters and numbers for COMSEC material. [C4009]
- **shroud** (D): /verb/ Encrypt private key possibly with policy preventing cleartext availability. [PKC12]
  - Deprecated Term: IDOCs SHOULD NOT use.
- **SHS** (N): See Secure Hash Standard.
- **sign** (I): Create digital signature for data object.
- **signal analysis** (I): Gaining indirect knowledge of communicated data by monitoring emitted signals.
- **signal intelligence** (I): Science and practice of extracting information from signals.
- **signal security** (N): Science and practice of protecting signals.
- **signature** (O): Symbol or process adopted to declare data object genuine.
- **signature certificate** (I): Public-key certificate for verifying digital signatures.
- **signed receipt** (I): S/MIME service providing proof of delivery and enabling originator to demonstrate signature verification.
- **signer** (N): Human or organization using private key to sign data object. [DSG]
- **SILS** (N): See Standards for Interoperable LAN/MAN Security.
- **simple authentication**
  - 1. (I) Authentication process using password.
  - 2. (O) "Authentication by means of simple password arrangements." [X509]
- **Simple Authentication and Security Layer (SASL)** (I): Specification for adding authentication to connection-based protocols. [R2222, R4422]
- **Simple Key Management for Internet Protocols (SKIP)** (I): Key-distribution protocol using hybrid encryption.
  - Tutorial: Uses Diffie-Hellman-Merkle for KEK; session keys encrypted in SKIP header.
- **Simple Mail Transfer Protocol (SMTP)** (I): TCP-based Application-Layer protocol for moving email.
- **Simple Network Management Protocol (SNMP)** (I): Protocol for conveying management information between managers and agents.
- **Simple Public Key Infrastructure (SPKI)** (I): Experimental alternative to PKIX. [RFCs 2692, 2693]
- **simple security property** (N): /formal model/ Property that subject has read access only if clearance dominates classification.
- **single sign-on**
  - 1. (I) Authentication subsystem enabling user to access multiple components after one login.
  - 2. (O) /Liberty Alliance/ Subsystem where identity authenticated at identity provider honored by other service providers.
- **singular identity** (I): See secondary definition under "identity".
- **site** (I): Facility where system functions are performed.
- **situation** (I): See security situation.
- **SKEME** (I): Key-distribution protocol adapted for IKE. [SKEME]
- **SKIP** (I): See Simple Key Management for Internet Protocols.
- **SKIPJACK** (N): Type 2 64-bit block cipher with 80-bit key.
- **slot** (O): /MISSI/ FORTEZZA PC card storage area for certificate and private key.
- **smart card** (I): Credit-card sized device with integrated circuits for computer functions.
- **smart token** (I): Device similar to smart card but in different form factor.
- **SMI** (I): See security management infrastructure.
- **SMTP** (I): See Simple Mail Transfer Protocol.
- **smurf attack** (D): /slang/ Denial-of-service using IP broadcast ICMP ping packets.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **sneaker net** (D): /slang/ Manual data transfer across air gap.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **Snefru** (N): Public-domain cryptographic hash function.
- **sniffing** (D): /slang/ Synonym for "passive wiretapping".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **SNMP** (I): See Simple Network Management Protocol.
- **social engineering** (D): Euphemism for non-technical attack methods.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **SOCKS** (I): Protocol providing generalized proxy server for firewall services. [R1928]
- **soft TEMPEST** (O): Use of software to reduce radio frequency information leakage. [Kuhn]
- **soft token** (D): Data object controlling access.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **software** (I): Computer programs and data stored and executed by hardware.
- **software error** (I): /threat action/ See secondary definitions under "corruption", "exposure", "incapacitation".
- **SORA** (O): See SSO-PIN ORA.
- **source authentication** (D): Synonym for "data origin authentication" or "peer entity authentication".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **source integrity** (I): Property that data is trustworthy based on sources and handling procedures.
- **SP3** (O): See Security Protocol 3.
- **SP4** (O): See Security Protocol 4.
- **spam**
  - 1a. (I) /slang verb/ Indiscriminately send unsolicited messages.
  - 1b. (I) /slang noun/ Electronic junk mail. [R2635]
    - Deprecated Usage: IDOCs SHOULD NOT use uppercase; should distinguish from trademark SPAM.
- **SPD** (I): See Security Policy Database.
- **special access program (SAP)** (O): /U.S. Government/ Program imposing need-to-know and access controls beyond normal. [C4009]
- **SPI** (I): See Security Parameters Index.
- **SPKI** (I): See Simple Public Key Infrastructure.
- **split key** (I): Cryptographic key generated and distributed as separate items that individually convey no knowledge of whole.
- **split knowledge**
  - 1. (I) Technique where entities separately hold data items not conveying knowledge of combined information.
  - 2. (O) "A condition under which two or more entities separately have key components [that] individually convey no knowledge of the plaintext key." [FP140]
- **spoof** (I): /threat action/ See secondary definition under "masquerade".
- **spoofing attack** (I): Synonym for "masquerade attack".
- **spread spectrum** (N): TRANSEC technique transmitting signal in bandwidth much greater than information needs.
- **spyware** (D): /slang/ Software surreptitiously installed to gather data.
  - Deprecated Usage: IDOCs SHOULD define.
- **SSH(trademark)** (N): See Secure Shell(trademark).
- **SSL** (I): See Secure Sockets Layer.
- **SSO** (I): See system security officer.
- **SSO PIN** (O): /MISSI/ PIN controlling access to FORTEZZA PC card functions intended for end user and CA.
- **SSO-PIN ORA (SORA)** (O): /MISSI/ ORA operating in mode requiring knowledge of SSO PIN.
- **Standards for Interoperable LAN/MAN Security (SILS)**
  - 1. (N) IEEE 802.10 standards committee.
  - 2. (N) Set of IEEE standards with eight parts.
- **star property** (N): See *-property.
- **Star Trek attack** (D): /slang/ Attack penetrating where no attack has gone before.
  - Deprecated Usage: IDOCs SHOULD NOT use.
- **static** (I): /adjective/ Refers to cryptographic key or parameter that is relatively long-lived.
- **steganography** (I): Methods of hiding existence of message; different from cryptography.
- **storage channel** (I): See covert storage channel.
- **storage key** (I): Key used for protecting information maintained in device, not for transmission.
- **stream cipher** (I): Encryption algorithm breaking plain text into stream and encrypting each element.
- **stream integrity service** (I): Data integrity service preserving integrity for sequence of packets; includes protection against insertion, reordering, deletion, delay.
- **strength**
  - 1. (I) /cryptography/ Cryptographic mechanism's level of resistance to attacks.
  - 2. (N) /Common Criteria/ "Strength of function" qualification expressing minimum efforts to defeat.
    - Levels: Basic, Medium, High.
- **strong**
  - 1. (I) /cryptography/ Algorithm requiring large computational power to defeat.
  - 2. (I) /COMPUSEC/ Security mechanism difficult to defeat.
- **strong authentication**
  - 1. (I) Authentication using cryptographic security mechanism, especially public-key certificates.
  - 2. (O) "Authentication by means of cryptographically derived credentials." [X509]
- **subject**
  - 1a. (I) Process representing principal executing with privileges.
  - 1b. (I) /formal model/ Entity causing information flow; technically process-domain pair.
  - 2. (I) /digital certificate/ Name bound to data items in certificate.
- **subject CA** (D): The CA that is subject of cross-certificate.
  - Deprecated Term: IDOCs SHOULD NOT use.
- **subnetwork** (N): System of packet relays and connecting links implementing OSIRM Layer 2 or 3.
- **subordinate CA (SCA)**
  - 1. (I) CA whose public-key certificate is issued by another (superior) CA.
  - 2. (O) /MISSI/ Fourth level of MISSI hierarchy; signs end user certificates and CRLs.
- **subordinate DN** (I): X.500 DN beginning with set of attributes same as another DN except terminal attribute.
- **subscriber** (I): /PKI/ User registered in PKI, named in subject field of certificate.
- **substitution**
  - 1. (I) /cryptography/ Encryption method replacing plaintext elements with ciphertext.
  - 2. (I) /threat action/ See secondary definition under "falsification".
- **subsystem** (I): Collection of related components performing system function.
- **superencryption** (I): Encryption where plaintext input is ciphertext from previous encryption.
- **superuser** (I): /UNIX/ Synonym for "root".
- **survivability** (I): Ability to remain in operation despite adverse conditions.
- **swIPe** (I): Encryption protocol for IP providing confidentiality, integrity, authentication.
- **syllabary** (N): /encryption/ List of letters/combinations with equivalent code groups for spelling proper names.
- **symmetric cryptography** (I): Branch where algorithms use same key for counterpart operations.
- **symmetric key** (I): Key used in symmetric cryptographic algorithm.
- **SYN flood** (I): Denial-of-service attack sending many TCP SYN packets to disrupt host.
- **synchronization** (I): Technique by which receiving cryptographic process attains matching state.
- **system** (I): Synonym for "information system".
- **system architecture** (N): Structure of components, relationships, principles governing design.
- **system component**
  - 1. (I) Collection of resources forming part of system.
  - 2. (O) /ITSEC/ Identifiable self-contained part of TOE.
- **system entity** (I): Active part of system (person, group, process) with specific capabilities.
- **system high** (I): Highest security level at which system operates.
- **system-high security mode** (I): Mode where all users possess necessary authorizations for all data.
- **system integrity**
  - 1. (I) Attribute that system can perform intended function free from unauthorized manipulation.
  - 2. (D) "Quality of an [information system] reflecting logical correctness and reliability..." (Deprecated)
- **system integrity service** (I): Security service protecting system resources against unauthorized change, loss, destruction.
- **system low** (I): Lowest security level supported by system.
- **system resource** (I): Data, service, capacity, equipment, or facility.
- **system security officer (SSO)** (I): Person responsible for enforcement or administration of security policy.
- **system user** (I): Entity consuming product or service; may be direct or indirect.
  - Active user: inside perimeter or can provide input.
  - Passive user: outside perimeter, can only receive output.
- **TACACS** (I): See Terminal Access Controller (TAC) Access Control System.
- **TACACS+** (I): TCP-based protocol improving TACACS with separate authentication, authorization, accounting.
- **tamper** (I): Make unauthorized modification degrading security services.
- **tamper-evident** (I): Characteristic providing evidence of attack attempt.
- **tamper-resistant** (I): Characteristic providing passive protection against attack.
- **tampering** (I): /threat action/ See secondary definitions under "corruption" and "misuse".
- **target of evaluation (TOE)** (N): /Common Criteria/ Product or system subject to security evaluation.
- **TCB** (N): See trusted computing base.
- **TCC field** (I): See Transmission Control Code field.
- **TCG** (N): See Trusted Computing Group.
- **TCP** (I): See Transmission Control Protocol.
- **TCP/IP** (I): Synonym for "Internet Protocol Suite".
- **TCSEC** (N): See Trusted Computer System Evaluation Criteria.
- **TDEA** (I): See Triple Data Encryption Algorithm.
- **teardrop attack** (D): Denial-of-service attack using improperly formed IP fragments.
  - Deprecated Term: IDOCs SHOULD define.
- **technical non-repudiation** (I): See secondary definition under "non-repudiation".
- **technical security** (I): Security mechanisms implemented in computer hardware, firmware, software.
- **Telecommunications Security Word System (TSEC)** (O): Nomenclature for telecommunications security equipment.
- **TELNET** (I): Protocol for remote login.
- **TEMPEST**
  - 1. (N) Technology for protecting against data compromise from electromagnetic emanations.
  - 2. (O) /U.S. Government/ "Short name referring to investigation, study, and control of compromising emanations." [C4009]
- **TEMPEST zone** (O): Designated area where equipment with appropriate TEMPEST characteristics may be operated.
- **Terminal Access Controller (TAC) Access Control System (TACACS)** (I): UDP-based authentication protocol.
- **TESS** (I): See The Exponential Encryption System.
- **The Exponential Encryption System (TESS)** (I): System for secure authenticated exchange of keys, digital signatures, key distribution.
- **theft** (I): /threat action/ See secondary definitions under "interception" and "misappropriation".
- **threat**
  - 1a. (I) Potential for violation of security existing when entity, circumstance, capability, action, or event could cause harm.
  - 1b. (N) Any circumstance with potential to adversely affect system.
  - 2. (O) Technical and operational ability of hostile entity, with intent.
  - 3. (D) "An indication of an impending undesirable event." [Park] (Deprecated)
- **threat action** (I): Realization of threat; occurrence where security assaulted.
- **threat agent** (I): Entity or event performing threat action.
- **threat analysis** (I): Analysis of threat actions, emphasizing probability and consequences.
- **threat consequence** (I): Security violation resulting from threat action.
  - Four types: unauthorized disclosure, deception, disruption, usurpation.
- **thumbprint**
  - 1. (I) Pattern of ridges on thumb tip.
  - 2. (D) Synonym for some type of "hash result". (Deprecated)
- **ticket** (I): Synonym for "capability token".
- **tiger team** (O): Group performing penetration tests.
  - Deprecated Usage: IDOCs SHOULD NOT use.
- **time stamp**
  - 1. (I) /noun/ Label recording time affixed to data object.
  - 2. (O) /noun/ Data field recording time of network event. [A1523]
- **Time-Stamp Protocol** (I): Protocol for requesting and receiving time stamp from server.
- **timing channel** (I): See covert timing channel.
- **TKEY** (I): Protocol for establishing shared secret between DNS resolver and name server.
- **TLS** (I): See Transport Layer Security.
- **TLSP** (N): See Transport Layer Security Protocol.
- **TOE** (N): See target of evaluation.
- **token**
  - 1. (I) /cryptography/ See cryptographic token.
  - 2. (I) /access control/ Object controlling access passed between entities.
  - 3a. (D) /authentication/ Data object or physical device for identity verification.
  - 3b. (D) /U.S. Government/ Something possessed and controlled by claimant. [SP63]
    - Deprecated usage: IDOCs SHOULD NOT use definitions 3a and 3b.
- **token backup** (I): Operation storing sufficient information to recreate token if lost.
- **token copy** (I): Operation copying all personality information to another token with different local values.
- **token management** (I): Process of initializing, loading, controlling security tokens.
- **token restore** (I): Operation loading token with data to recreate previous contents.
- **token storage key** (I): Key protecting data stored on security token.
- **top CA** (I): Synonym for "root" in certification hierarchy.
- **top-level specification** (I): Non-procedural description at most abstract level.
- **TPM** (N): See Trusted Platform Module.
- **traceback** (I): Identification of source of data packet.
- **tracker** (N): Attack technique for unauthorized disclosure from statistical database. [Denns]
- **traffic analysis**
  - 1. (I) Gaining knowledge from observable characteristics of data flow.
  - 2. (O) "The inference of information from observation of traffic flows..." [I7498-2]
- **traffic-flow analysis** (I): Synonym for "traffic analysis".
- **traffic-flow confidentiality (TFC)**
  - 1. (I) Data confidentiality service protecting against traffic analysis.
  - 2. (O) "A confidentiality service to protect against traffic analysis." [I7498-2]
    - Tutorial: Full or partial; difficulty in shared media.
- **traffic key** (I): Cryptographic key for protecting information in transmission.
- **traffic padding** (I): "The generation of spurious instances of communication, spurious data units, and/or spurious data within data units." [I7498-2]
- **tranquility property** (N): /formal model/ Property that security level of object cannot change while being processed.
- **transaction**
  - 1. (I) Unit of interaction involving series of system actions.
  - 2. (O) "A discrete event between user and systems that supports a business or programmatic purpose." [M0404]
    - Tutorial: Should be atomic, consistent, isolated, durable.
- **TRANSEC** (I): See transmission security.
- **Transmission Control Code field (TCC field)** (I): Field in IPv4 security option for segregating traffic.
- **Transmission Control Protocol (TCP)** (I): Standard Transport-Layer protocol for reliable datagram delivery.
- **transmission security (TRANSEC)** (I): COMSEC measures protecting communications from interception and exploitation other than cryptanalysis.
- **Transport Layer**: See Internet Protocol Suite, OSIRM.
- **Transport Layer Security (TLS)** (I): Protocol based on SSL Version 3.0. [R4346]
- **Transport Layer Security Protocol (TLSP)** (N): End-to-end encryption protocol at bottom of OSIRM Layer 4.
- **transport mode** (I): IPsec mode where protection applies to Transport-Layer packets. (Compare: tunnel mode.)
- **transposition** (I): /cryptography/ Encryption method changing sequential position of plaintext elements.
- **trap door** (I): Synonym for "back door".
- **trespass** (I): /threat action/ See secondary definition under "intrusion".
- **Triple Data Encryption Algorithm** (I): Block cipher applying DEA three successive times with two or three keys. [A9052, SP67]
- **triple-wrapped** (I): /S/MIME/ Data signed, then encrypted, then signed again. [R2634]
- **Trojan horse** (I): Program with useful function and hidden malicious function.
- **trust**
  - 1. (I) /information system/ Feeling of certainty that system will not fail or meets specifications.
    - Tutorial: Three classes: trusted, benign, untrusted.
  - 2. (I) /PKI/ Relationship between certificate user and CA.
- **trust anchor** (I): /PKI/ Established point of trust from which certification path validation begins.
  - Tutorial: May be public key, CA, or certificate.
- **trust anchor CA** (I): CA that is subject of trust anchor certificate or establishes trust anchor key.
- **trust anchor certificate** (I): Public-key certificate providing first public key in path.
- **trust anchor key** (I): Public key used as first in certification path.
- **trust anchor information** (I): See secondary definition under "trust anchor".
- **trust chain** (D): Synonym for "certification path".
  - Deprecated Term: IDOCs SHOULD NOT use.
- **trust-file PKI** (I): Non-hierarchical PKI where each user has local file of trust anchors.
- **trust hierarchy** (D): Synonym for "certification hierarchy".
  - Deprecated Usage: IDOCs SHOULD NOT use.
- **trust level** (N): Characterization of standard of security protection.
- **trusted** (I): See secondary definition under "trust".
- **trusted CA** (I): CA upon which user relies as issuing valid certificates; especially trust anchor.
- **trusted certificate** (I): Digital certificate accepted as valid without testing; especially trust anchor.
- **Trusted Computer System Evaluation Criteria (TCSEC)** (N): Standard for evaluating OS security. Classes A1-D.
- **trusted computing base (TCB)** (N): "The totality of protection mechanisms within a computer system... responsible for enforcing a security policy." [NCS04]
- **Trusted Computing Group (TCG)** (N): Industry standards organization for hardware-enabled trusted computing.
- **trusted distribution** (I): /COMPUSEC/ Trusted method for distributing TCB components, protecting against modification.
- **trusted key** (D): Abbreviation for "trusted public key" or other keys.
  - Deprecated Usage: IDOCs SHOULD define or use less ambiguous term.
- **trusted path**
  - 1a. (I) /COMPUSEC/ Mechanism for direct communication with TCB, not imitated by untrusted software.
  - 1b. (I) /COMSEC/ Mechanism for direct communication with cryptographic module.
- **Trusted Platform Module (TPM)** (N): Specification for microcontroller storing secured information.
- **trusted process** (I): System component with privileges enabling it to affect security state.
- **trusted public key** (I): Public key upon which user relies; especially trust anchor key.
- **trusted recovery** (I): Process restoring system to normal operation after failure or attack without security compromise.
- **trusted subnetwork** (I): Subnetwork containing hosts and routers that trust each other not to attack.
- **trusted system**
  - 1. (I) /information system/ System operating as expected despite disruption.
  - 2. (N) /multilevel secure/ System with sufficient assurance for processing sensitive/classified information. [NCS04]
- **Trusted Systems Interoperability Group (TSIG)** (N): Forum promoting interoperability of trusted systems.
- **trustworthy system**
  - 1. (I) System that warrants trust because behavior can be validated.
  - 2. (O) /Digital Signature Guidelines/ Computer hardware, software, procedures that are reasonably secure, reliable, correct, and adhere to principles. [DSG]
- **TSEC** (O): See Telecommunications Security Nomenclature System.
- **TSIG**
  - 1. (N) See Trusted System Interoperability Group.
  - 2. (I) Protocol for data origin authentication and integrity for DNS.
- **tunnel**
  - 1. (I) Communication channel created by encapsulating protocol's data packets in another.
    - Tutorial: Usually logical point-to-point link.
  - 2. (O) /SET/ Private extension indicating support for encrypted messages through merchant.
- **tunnel mode** (I): IPsec mode where protection applies to IP packets. (Compare: transport mode.)
- **two-person control** (I): Surveillance by two appropriately authorized persons at all times.
- **Twofish** (O): Symmetric 128-bit block cipher AES candidate.
- **type 0 product** (O): /cryptography, U.S. Government/ Classified cryptographic

## Definitions and Abbreviations (continued)

**$ time stamp**
- **Definition 1 (I)**: With respect to a data object, a label or marking recording the time at which it was affixed. (See: Time-Stamp Protocol.)
- **Definition 2 (O)**: "With respect to a recorded network event, a data field recording the time of the event." [A1523]
- **Tutorial**: Used as evidence to prove existence of data object/event at or before a given time; e.g., for PKI non-repudiation and long-term security.

**$ Time-Stamp Protocol**
- **(I)**: An Internet protocol (RFC 3161) specifying how a client requests and receives a time stamp from a server for a data object.
- **Tutorial**: Describes request/response format; the authority creates the stamp by concatenating hash, UTC time, parameters, and signing with private key as per CMS. Typically operates as a trusted third-party service.

**$ timing channel**: (I) See: covert timing channel.

**$ TKEY**: (I) Mnemonic for an Internet protocol (RFC 2930) to establish a shared secret between DNS resolver and name server. (See: TSIG.)

**$ TLS**: (I) See: Transport Layer Security.

**$ TLSP**: (N) See: Transport Layer Security Protocol.

**$ TOE**: (N) See: target of evaluation.

**$ token**
- **Definition 1 (I)**: /cryptography/ See: cryptographic token. (Compare: dongle.)
- **Definition 2 (I)**: /access control/ An object used to control access and passed between cooperating entities to synchronize use of a shared resource.
- **Usage**: IDOCs SHOULD NOT use this term with any definition other than 1 or 2.
- **Definition 3a (D)**: /authentication/ A data object or physical device used to verify identity.
- **Definition 3b (D)**: /U.S. Government/ Something the claimant in an authentication process possesses and controls to prove the claim. [SP63]
- **Deprecated usage**: IDOCs SHOULD NOT use this term with definitions 3a and 3b; instead use more specific terms like "authentication information" or "cryptographic token".
- **Tutorial**: NIST defines four types of claimant tokens; IDOCs SHOULD NOT use those terms; use more descriptive terms instead (hard token, one-time password device token, soft token, password token).

**$ token backup**: (I) A token management operation that stores sufficient information to recreate a security token if lost or damaged.

**$ token copy**: (I) Copies personality information from one security token to another, but the second token has its own local security values (PINs, storage keys).

**$ token management**: (I) Process including initializing tokens, loading data, controlling lifecycle; may include key management, certificate management, PIN generation, user personality data, backup/copy/restore, firmware updates.

**$ token restore**: (I) Loads a token with data to recreate contents previously held by that or another token. (See: recovery.)

**$ token storage key**: (I) A cryptographic key used to protect data stored on a security token.

**$ top CA**: (I) Synonym for "root" in a certification hierarchy. (See: apex trust anchor.)

**$ top-level specification**
- **(I)**: "A non-procedural description of system behavior at the most abstract level; typically a functional specification that omits all implementation details." [NCS04] (See: formal top-level specification, Tutorial under "security policy".)
- **Tutorial**: Below "security model", above "security architecture". May be descriptive (natural language) or formal (mathematical language for correctness proof).

**$ TPM**: (N) See: Trusted Platform Module.

**$ traceback**: (I) Identification of the source of a data packet. (See: masquerade, network weaving.)

**$ tracker**: (N) An attack technique for unauthorized disclosure from a statistical database. [Denns] (See: Tutorial under "inference control".)

**$ traffic analysis**
- **Definition 1 (I)**: Gaining knowledge by inference from observable characteristics of a data flow (identities, locations, presence, amount, frequency, duration), even if data is encrypted.
- **Definition 2 (O)**: "The inference of information from observation of traffic flows (presence, absence, amount, direction, and frequency)." [I7498-2]

**$ traffic-flow analysis**: (I) Synonym for "traffic analysis".

**$ traffic-flow confidentiality (TFC)**
- **Definition 1 (I)**: A data confidentiality service to protect against traffic analysis. (See: communications cover.)
- **Definition 2 (O)**: "A confidentiality service to protect against traffic analysis." [I7498-2]
- **Tutorial**: Confidentiality includes indirect disclosure via traffic analysis. TFC can be full or partial. Full TFC on point-to-point links by enciphering all PDUs and generating continuous random data. Partial TFC on shared/broadcast media requires techniques like spurious PDUs, padding, address enciphering.

**$ traffic key**: (I) A cryptographic key used for protecting information transmitted between devices. (Compare: storage key.)

**$ traffic padding**: (I) "The generation of spurious instances of communication, spurious data units, and/or spurious data within data units." [I7498-2]

**$ tranquility property**: (N) /formal model/ Property that the security level of an object cannot change while being processed. (See: Bell-LaPadula model.)

**$ transaction**
- **Definition 1 (I)**: A unit of interaction between external entity and system, or within system, involving a series of actions or events.
- **Definition 2 (O)**: "A discrete event between user and systems that supports a business or programmatic purpose." [M0404]
- **Tutorial**: Need to be atomic, consistent, isolated, durable (ACID).

**$ TRANSEC**: (I) See: transmission security.

**$ Transmission Control Code field (TCC field)**: (I) A data field in IPv4's security option for traffic segregation and controlled communities of interest. Values are alphanumeric trigraphs assigned by U.S. Government (RFC 791).

**$ Transmission Control Protocol (TCP)**: (I) An Internet Standard Transport-Layer protocol (RFC 793) for reliable delivery of datagrams. (See: TCP/IP.)
- **Tutorial**: Fits into layered suite; assumes unreliable underlying datagram service.

**$ transmission security (TRANSEC)**: (I) COMSEC measures protecting communications from interception and exploitation by means other than cryptanalysis (e.g., frequency hopping). (Compare: anti-jam, traffic-flow confidentiality.)

**$ Transport Layer**: See: Internet Protocol Suite, OSIRM.

**$ Transport Layer Security (TLS)**: (I) Internet protocol [R4346] based on SSL 3.0. (Compare: TLSP.)
- **Tutorial**: Misnamed; actually layered above reliable Transport-Layer protocol (usually TCP) and below or integrated with Application-Layer protocol (often HTTP).

**$ Transport Layer Security Protocol (TLSP)**: (N) End-to-end encryption protocol (ISO 10736) providing security services at bottom of OSIRM Layer 4. (Compare: TLS.)
- **Tutorial**: Evolved from SP4.

**$ transport mode**: (I) IPsec mode where protection applies to Transport-Layer protocol packets (e.g., TCP, UDP). (Compare: tunnel mode.)
- **Tutorial**: Always between two hosts; not involving security gateways.

**$ transposition**: (I) /cryptography/ Encryption method where plaintext elements change position but not form. (Compare: substitution.)

**$ trap door**: (I) Synonym for "back door".

**$ trespass**: (I) /threat action/ See secondary definition under "intrusion".

**$ Triple Data Encryption Algorithm**: (I) A block cipher applying DEA three times with two or three keys (112 or 168 bits). [A9052, SP67]
- **Example**: Variation for IPsec ESP with 168-bit key and IV.

**$ triple-wrapped**: (I) /S-MIME/ Data signed, then encrypted, then signed again. [R2634]

**$ Trojan horse**: (I) A program with a hidden malicious function that evades security mechanisms. (See: malware, spyware. Compare: logic bomb, virus, worm.)

**$ trust**
- **Definition 1 (I)**: /information system/ Feeling of certainty that system will not fail or meets specifications. (See: trust level, trusted system, trustworthy system. Compare: assurance.)
- **Tutorial**: Components can be trusted (enforce security), benign (not enforce but sensitive), or untrusted (malicious).
- **Definition 2 (I)**: /PKI/ Relationship where user assumes CA creates only valid certificates.
- **Tutorial**: From [X509]: "An entity is said to 'trust' a second entity when the first entity makes the assumption that the second entity will behave exactly as the first entity expects."

**$ trust anchor**
- **(I)**: /PKI/ An established point of trust from which a certificate user begins validation of a certification path. (See: apex trust anchor, path validation, trust anchor CA, certificate, key.)
- **Usage**: IDOCs that use this term SHOULD state a definition because it is used variously in existing IDOCs and PKI literature.
- **Tutorial**: May be defined as a public key, a CA, a public-key certificate, or combinations/variations.

**$ trust anchor CA**: (I) A CA that is the subject of a trust anchor certificate or establishes a trust anchor key. (See: root, trusted CA.)
- **Tutorial**: Selection is a matter of policy; choices include top CA in hierarchical PKI, certificate issuer, or any other CA in a network PKI.

**$ trust anchor certificate**: (I) A public-key certificate used to provide the first public key in a certification path. (See: root certificate, trust anchor, trusted certificate.)

**$ trust anchor key**: (I) A public key used as the first public key in a certification path. (See: root key, trust anchor, trusted public key.)

**$ trust anchor information**: (I) See secondary definition under "trust anchor".

**$ trust chain**
- **(D)**: Synonym for "certification path". (See: trust anchor, trusted certificate.)
- **Deprecated Term**: IDOCs SHOULD NOT use this term because it unnecessarily duplicates the internationally standardized term and mixes concepts in a potentially misleading way.

**$ trust-file PKI**: (I) A non-hierarchical PKI where each user has a local file of trust anchors. (See: trust anchor, web of trust. Compare: hierarchical PKI, mesh PKI.)
- **Example**: Popular browsers with initial file of trust anchor certificates (often self-signed).

**$ trust hierarchy**
- **(D)**: Synonym for "certification hierarchy".
- **Deprecated Usage**: IDOCs SHOULD NOT use this term because it mixes concepts misleadingly and trust hierarchy could be implemented in other ways.

**$ trust level**: (N) A characterization of a standard of security protection for an information system. (See: Common Criteria, TCSEC.)
- **Tutorial**: Based on security mechanisms, systems engineering, and implementation analysis.

**$ trusted**: (I) See secondary definition under "trust".

**$ trusted CA**: (I) A CA upon which a user relies as issuing valid certificates; especially used as trust anchor CA. (See: certification path, root, trust anchor CA, validation.)
- **Tutorial**: Trust is transitive to the extent X.509 extensions permit.

**$ trusted certificate**: (I) A digital certificate accepted as valid a priori without testing; especially used as trust anchor certificate. (See: certification path, root certificate, trust anchor certificate, trust-file PKI, validation.)
- **Tutorial**: Acceptance is a matter of policy; often obtained out-of-band.

**$ Trusted Computer System Evaluation Criteria (TCSEC)**
- **(N)**: Standard for evaluating operating system security (Orange Book). (See: Common Criteria, Deprecated Usage under "Green Book", trust level, trusted system. Compare: TSEC.)
- **Tutorial**: Defines hierarchical assurance classes (A1 highest to D minimal).

**$ trusted computing base (TCB)**: (N) "The totality of protection mechanisms within a computer system enforcing a security policy." [NCS04] (Compare: TPM.)

**$ Trusted Computing Group (TCG)**: (N) Industry standards organization for hardware-enabled trusted computing. (See: TPM, trusted system. Compare: TSIG.)

**$ trusted distribution**: (I) /COMPUSEC/ Trusted method for distributing TCB components with protection from modification and detection of changes. [NCS04] (See: code signing, configuration control.)

**$ trusted key**
- **(D)**: Abbreviation for "trusted public key" and other types.
- **Deprecated Usage**: IDOCs SHOULD either state a definition or use a less ambiguous term.

**$ trusted path**
- **1a (I)**: /COMPUSEC/ Mechanism for direct, reliable communication with TCB, not imitable by untrusted software. [NCS04]
- **1b (I)**: /COMSEC/ Similar for cryptographic module. [FP140]

**$ Trusted Platform Module (TPM)**: (N) TCG specification for a microcontroller storing secured information; also general name of implementations. (Compare: TCB.)

**$ trusted process**: (I) A system component with privileges to affect security state; incorrect execution could violate security policy. (See: privileged process, trusted system.)

**$ trusted public key**: (I) A public key relied upon by a user; especially used as trust anchor key. (See: certification path, root key, trust anchor key, validation.)
- **Tutorial**: Could be root key, CA key, or any key in trust-file PKI.

**$ trusted recovery**: (I) Process restoring system after failure/attack without security compromise. (See: recovery.)

**$ trusted subnetwork**: (I) Subnetwork with hosts/routers that trust each other not to attack; underlying channels assumed protected.

**$ trusted system**
- **Definition 1 (I)**: /information system/ System that operates as expected despite disruptions, errors, attacks. [NRC98] (See: trust level, trusted process. Compare: trustworthy.)
- **Definition 2 (N)**: /multilevel secure/ System employing sufficient assurance measures for simultaneous processing of classified information. [NCS04]

**$ Trusted Systems Interoperability Group (TSIG)**: (N) Forum for promoting interoperability of trusted computer systems. (Compare: TCG.)

**$ trustworthy system**
- **Definition 1 (I)**: System that is trusted and warrants that trust through formal analysis or code review. (See: trust. Compare: trusted.)
- **Definition 2 (O)**: /Digital Signature Guidelines/ System that is reasonably secure, reliable, correct, and adheres to security principles. [DSG]

**$ TSEC**: (O) See: Telecommunications Security Nomenclature System. (Compare: TCSEC.)

**$ TSIG**
- **1 (N)**: See: Trusted System Interoperability Group.
- **2 (I)**: Mnemonic for Internet protocol (RFC 2845) for data origin authentication and integrity for DNS operations. (See: TKEY.)

**$ tunnel**
- **Definition 1 (I)**: Communication channel created by encapsulating a protocol's data packets in another protocol. (See: L2TP, tunnel mode, VPN. Compare: covert channel.)
- **Tutorial**: Tunneling can involve almost any two protocol layers; often a logical point-to-point link created by encapsulating Layer 2 in Transport/Network/another Layer 2 protocol.
- **Definition 2 (O)**: /SET/ Name of SET private extension indicating support for encrypted messages to cardholder through merchant.

**$ tunnel mode**: (I) IPsec mode where protection applies to entire IP packets. (See: tunnel. Compare: transport mode.)
- **Tutorial**: Each end may be host or security gateway; if either end is gateway, mode must be tunnel.

**$ two-person control**: (I) Surveillance and control by minimum of two authorized persons to detect incorrect/unauthorized procedures. (See: dual control, no-lone zone.)

**$ Twofish**: (O) A 128-bit block cipher with variable key length (128, 192, 256 bits), candidate for AES. (See: Blowfish.)

**$ type 0 product**: (O) /cryptography, U.S. Government/ Classified cryptographic equipment for distributing bulk keying material.

**$ type 1 key**: (O) /cryptography, U.S. Government/ Key generated/distributed by NSA for protection of classified/sensitive national security information. [C4009]

**$ type 1 product**: (O) /cryptography, U.S. Government/ Cryptographic equipment classified/certified by NSA for classified/sensitive national security information. [C4009]
- **Tutorial**: Earlier definition more specific; Type 1 contains classified NSA algorithms, subject to export restrictions (ITAR).

**$ type 2 key**: (O) /cryptography, U.S. Government/ Key for protection of unclassified national security information. [C4009]

**$ type 2 product**: (O) /cryptography, U.S. Government/ Cryptographic equipment certified by NSA for sensitive national security information. [C4009]
- **Tutorial**: Earlier definition: unclassified for national security systems. (See: national security system. Compare: EUCI.)

**$ type 3 key**: (O) /cryptography, U.S. Government/ Key for protection of unclassified sensitive information, even if used in Type 1/2 product. [C4009]

**$ type 3 product**: (O) /cryptography, U.S. Government/ Unclassified cryptographic equipment for unclassified sensitive U.S. Government or commercial information, using NIST approved algorithms. [C4009]

**$ type 4 key**: (O) /cryptography, U.S. Government/ Key used in support of Type 4 functionality; lacks U.S. Government endorsement. [C4009]

**$ type 4 product**: (O) /cryptography, U.S. Government/ Unevaluated commercial cryptographic equipment with no NSA/NIST certification. [C4009]

**$ UDP**: (I) See: User Datagram Protocol.

**$ UDP flood**: (I) A denial-of-service attack connecting two systems' test functions to cause nonstop data flow. (See: flooding.)

**$ unauthorized disclosure**: (I) Circumstance where entity gains access to information for which not authorized.
- **Tutorial**: Can be caused by exposure, interception, inference, intrusion; protected by access control, flow control, inference control.

**$ unauthorized user**: (I) /access control/ Entity accessing a resource without authorization. (See: user. Compare: authorized user, insider, outsider.)
- **Usage**: IDOCs that use this term SHOULD state a definition.

**$ uncertainty**: (N) Information-theoretic measure of minimum plaintext needed to recover entire plaintext from ciphertext. [SP63] (See: entropy.)

**$ unclassified**: (I) Not classified. (Compare: FOUO.)

**$ unencrypted**: (I) Not encrypted.

**$ unforgeable**: (I) /cryptography/ Property of a cryptographic data structure that makes it computationally infeasible to construct an unauthorized correct value without key knowledge.
- **Tutorial**: Narrower than general use; in PKI, forgery is detected when signature is verified with true public key.

**$ uniform resource identifier (URI)**: (I) A formatted identifier (RFC 3986) encapsulating name of Internet object and name space identification.
- **Example**: HTML uses URIs for hyperlinks.
- **Usage**: "A URI can be classified as a locator (URL) or name (URN) or both." IDOCs SHOULD use "URI" rather than the more restrictive "URL" or "URN".

**$ uniform resource locator (URL)**: (I) A URI describing access method and location of an information resource. (See: Usage under "URI". Compare: URN.)
- **Tutorial**: Subset of URIs providing access mechanism; e.g., "ftp://..." with scheme and hostname.

**$ uniform resource name (URN)**: (I) A URI with properties of a name. (See: Usage under "URI". Compare: URL.)
- **Tutorial**: Historically referred to URIs under "urn" scheme (RFC 2141) or any URI with name properties.

**$ untrusted**: (I) See secondary definition under "trust".

**$ untrusted process**
- **Definition 1 (I)**: System component that cannot affect security state (e.g., confined by security kernel). (See: trusted process.)
- **Definition 2 (I)**: Component not evaluated for security policy adherence; assumed potentially malicious.

**$ UORA**: (O) See: user-PIN ORA.

**$ update**: See: "certificate update" and "key update".

**$ upgrade**: (I) /data security/ Increase classification level without changing information content. (See: classify, downgrade, regrade.)

**$ URI**: (I) See: uniform resource identifier.

**$ URL**: (I) See: uniform resource locator.

**$ URN**: (I) See: uniform resource name.

**$ user**: See: system user.
- **Usage**: IDOCs that use this term SHOULD state a definition.

**$ user authentication service**: (I) A security service verifying identity claimed by entity attempting to access system. (See: authentication, user.)

**$ User Datagram Protocol (UDP)**: (I) Internet Standard Transport-Layer protocol (RFC 768) for delivery of datagrams. (See: UDP flood.)
- **Tutorial**: Assumes IP; minimal protocol mechanism; no reliable delivery or flow control.

**$ user identifier**: (I) See: identifier.

**$ user identity**: (I) See: identity.

**$ user PIN**: (O) /MISSI/ One of two PINs controlling access to functions and stored data of a FORTEZZA PC card; allows end user functions. (See: PIN. Compare: SSO PIN.)

**$ user-PIN ORA (UORA)**: (O) /MISSI/ Organizational RA operating in a mode where only user PIN knowledge is used for card management. (See: no-PIN ORA, SSO-PIN ORA.)

**$ usurpation**: (I) Circumstance resulting in control of system services by unauthorized entity. Caused by misappropriation, misuse. (See: access control.)

**$ UTCTime**: (N) ASN.1 data type containing calendar date (YYMMDD) and time to minute or second precision; either UTC or local time with offset. (See: Coordinated Universal Time. Compare: GeneralizedTime.)
- **Usage**: If centuries matter, use GeneralizedTime.

**$ v1 certificate**: (N) Abbreviation that ambiguously refers to either X.509 public-key certificate in version 1 or attribute certificate in version 1 format.
- **Deprecated Usage**: IDOCs MAY use as abbreviation for "version 1 X.509 public-key certificate" only after full term at first instance.

**$ v1 CRL**: (N) Abbreviation of "X.509 CRL in version 1 format".
- **Usage**: IDOCs MAY use but SHOULD define at first occurrence.

**$ v2 certificate**: (N) Abbreviation of "X.509 public-key certificate in version 2 format".
- **Usage**: IDOCs MAY use but SHOULD define at first occurrence.

**$ v2 CRL**: (N) Abbreviation of "X.509 CRL in version 2 format".
- **Usage**: IDOCs MAY use but SHOULD define at first occurrence.

**$ v3 certificate**: (N) Abbreviation of "X.509 public-key certificate in version 3 format".
- **Usage**: IDOCs MAY use but SHOULD define at first occurrence.

**$ valid certificate**
- **Definition 1 (I)**: A digital certificate that can be validated successfully. (See: validate, verify.)
- **Definition 2 (I)**: A digital certificate for which the binding of data items can be trusted.

**$ valid signature**
- **(D)**: Synonym for "verified signature".
- **Deprecated Term**: IDOCs SHOULD NOT use this synonym. This Glossary recommends "validate the certificate" and "verify the signature".

**$ validate**
- **Definition 1 (I)**: Establish the soundness or correctness of a construct (e.g., certificate validation). (See: validate vs. verify.)
- **Definition 2 (I)**: To officially approve something (e.g., NIST validates cryptographic modules).

**$ validate vs. verify**: Usage: IDOCs SHOULD comply with:
- **Rule 1**: Use "validate" when referring to process establishing soundness or correctness of a construct.
- **Rule 2**: Use "verify" when referring to process testing truth or accuracy of a fact or value.
- **Tutorial**: "Validate" from Latin "validus" (strong) – check construct is sound. "Verify" from Latin "verus" (true) – check truth of assertion.

**$ validation**: (I) See: validate vs. verify.

**$ validity period**: (I) /PKI/ Data item in a digital certificate specifying time period for which the binding is valid, unless certificate is revoked. (See: cryptoperiod, key lifetime.)

**$ value-added network (VAN)**: (I) Computer network that transmits, receives, stores EDI transactions for users.
- **Tutorial**: May also provide additional services like format translation, FAX conversion, business systems integration.

**$ VAN**: (I) See: value-added network.

**$ verification**
- **Definition 1 (I)**: /authentication/ Process of examining information to establish truth of claimed fact/value. (See: validate vs. verify, verify. Compare: authentication.)
- **Definition 2 (N)**: /COMPUSEC/ Process of comparing two levels of system specification for proper correspondence (e.g., security model with top-level specification). [NCS04]

**$ verified design**: (O) See: TCSEC Class A1.

**$ verify**: (I) To test or prove the truth or accuracy of a fact or value. (See: validate vs. verify, verification. Compare: authenticate.)

**$ vet**: (I) /verb/ To examine or evaluate thoroughly. (Compare: authenticate, identity proofing, validate, verify.)

**$ violation**: See: security violation.

**$ virtual private network (VPN)**: (I) A restricted-use logical network constructed from system resources of a physical network, often using encryption and tunneling. (See: tunnel.)
- **Tutorial**: Less expensive than dedicated network; e.g., corporation with LANs at different sites using encrypted tunnels across Internet.

**$ virus**: (I) Self-replicating section of software (usually malicious) that propagates by infecting host programs; requires host to run.

**$ Visa Cash**: (O) Smartcard-based electronic money system using cryptography for Internet payments. (See: IOTP.)

**$ volatile media**: (I) Storage media requiring external power to maintain information. (Compare: non-volatile media, permanent storage.)

**$ VPN**: (I) See: virtual private network.

**$ vulnerability**: (I) A flaw or weakness in system design, implementation, operation/management that could be exploited to violate security policy. (See: harden.)
- **Tutorial**: Three types: design/specification, implementation, operation/management. Not all vulnerabilities make systems unuseable; depends on attack difficulty and effectiveness of countermeasures.

**$ W3**: (D) Synonym for WWW.
- **Deprecated Abbreviation**: Could be confused with W3C; use "WWW".

**$ W3C**: (N) See: World Wide Web Consortium.

**$ war dialer**: (I) /slang/ Program that automatically dials telephone numbers to find connected computer systems for cracking.
- **Deprecated Usage**: IDOCs that use this term SHOULD state a definition to avoid confusing international readers.

**$ Wassenaar Arrangement**: (N) Multilateral agreement on export controls for conventional arms and dual-use goods; aims to prevent destabilizing accumulations.
- **Tutorial**: Began 1996, headquarters in Vienna; participating countries agree to maintain effective export controls and provide notifications. All measures on national discretion.

**$ watermarking**: See: digital watermarking.

**$ weak key**: (I) A key value providing poor security for a cryptographic algorithm. (See: strong.)
- **Example**: DEA has four weak keys and ten pairs of semi-weak keys.

**$ web, Web**
- **Definition 1 (I)**: /not capitalized/ IDOCs SHOULD NOT capitalize when referring generically to web technology (browsers, servers, HTTP, HTML).
- **Definition 2 (I)**: /capitalized/ IDOCs SHOULD capitalize when referring specifically to the World Wide Web.
- **Usage**: IDOCs SHOULD NOT use in a way that might confuse with PGP "web of trust". When using Web as abbreviation, spell out at first instance.

**$ web of trust**
- **(D)**: /PGP/ PKI architecture where each user defines own trust anchors based on personal relationships.
- **Deprecated Usage**: IDOCs SHOULD NOT use except with reference to PGP; mixes concepts misleadingly. Instead use "trust-file PKI".
- **Tutorial**: Users build private repositories of trusted keys through personal judgments; no public repositories.

**$ web server**: (I) Software process responding to HTTP requests from clients.

**$ WEP**: (N) See: Wired Equivalent Privacy.

**$ Wired Equivalent Privacy (WEP)**: (N) Cryptographic protocol defined in IEEE 802.11 for wireless LANs.
- **Tutorial**: Design flawed; uses RC4 and CRC; flawed implementation and management common.

**$ wiretapping**: (I) Attack that intercepts and accesses information in a data flow. (See: active wiretapping, end-to-end encryption, passive wiretapping.)
- **Usage**: Originally mechanical connection; now refers to accessing from any medium or node.
- **Tutorial**: Active wiretapping alters data; passive attempts to observe only.

**$ work factor**
- **1a (I)**: /COMPUSEC/ Estimated effort/time for potential intruder to penetrate system or defeat countermeasure.
- **1b (I)**: /cryptography/ Estimated computing power/time to break a cryptographic system.

**$ World Wide Web ("the Web", WWW)**: (N) Global hypermedia-based collection of information and services on Internet servers accessed by browsers using HTTP.

**$ World Wide Web Consortium (W3C)**: (N) Organization developing and standardizing Web protocols; hundreds of member organizations.
- **Tutorial**: W3C Recommendations have four levels: Working Draft, Candidate Recommendation, Proposed Recommendation, W3C Recommendation.

**$ worm**: (I) Program that can run independently, propagate a working version onto other hosts, and may consume resources destructively. (See: mobile code, Morris Worm, virus.)

**$ wrap**
- **Definition 1 (N)**: To use cryptography for data confidentiality of keying material. (See: encrypt, wrapping algorithm, wrapping key. Compare: seal, shroud.)
- **Definition 2 (D)**: To use cryptography for data confidentiality of data in general.
- **Deprecated Usage**: IDOCs SHOULD NOT use definition 2 because it duplicates "encrypt".

**$ wrapping algorithm**: (N) Encryption algorithm specifically intended for encrypting keys. (See: KEK, wrap.)

**$ wrapping key**: (N) Synonym for "KEK". (See: encrypt. Compare: seal, shroud.)

**$ write**: (I) /security model/ System operation causing information flow from subject to object. (See: access mode. Compare: read.)

**$ WWW**: (I) See: World Wide Web.

**$ X.400**: (N) ITU-T Recommendation defining Message Handling Systems (ISO equivalent IS 10021). (See: Message Handling Systems.)

**$ X.500**: (N) ITU-T Recommendation defining X.500 Directory; distributed directory for OSI entities. (See: directory vs. Directory, X.509.)
- **Tutorial**: Structured as Directory Information Tree; entries composed of attributes; e.g., X.509 certificates stored as values of userCertificate attribute.

**$ X.509**: (N) ITU-T Recommendation defining framework for authentication, including X.509 public-key certificates, attribute certificates, and CRLs. (ISO equivalent IS 9498-4.)
- **Tutorial**: Describes simple and strong authentication; strong authentication should be used for secure services.

**$ X.509 attribute certificate**: (N) Attribute certificate in v1 format defined by X.509.
- **Tutorial**: Separate from public-key certificate; contains subject, issuer, signature, validity period, attributes, optional extensions. Structure listed.

**$ X.509 certificate**: (N) Synonym for "X.509 public-key certificate".
- **Usage**: IDOCs MAY use after defining at first instance; otherwise ambiguous (also attribute certificates).
- **Deprecated Usage**: IDOCs SHOULD NOT use as abbreviation for attribute certificate.

**$ X.509 certificate revocation list (CRL)**: (N) CRL in v1 or v2 format defined by X.509.
- **Usage**: IDOCs SHOULD NOT refer to X.509 CRL as a digital certificate, though it meets the definition (signed assertion). It asserts revocation of previously issued certificates.
- **Tutorial**: Contains version, signature, issuer, thisUpdate, nextUpdate, list of revoked certificates (serial number, revocation date, optional entry extensions), optional CRL extensions.

**$ X.509 public-key certificate**: (N) Public-key certificate in v1, v2, or v3 format defined by X.509.
- **Tutorial**: Contains version, serial number, signature algorithm OID, issuer DN, validity, subject DN, subject public key info, optional unique identifiers, optional extensions. Structure listed.

**$ X9**: (N) See: "Accredited Standards Committee X9" under "ANSI".

**$ XML**: (N) See: Extensible Markup Language.

**$ XML-Signature**: (N) W3C Recommendation specifying XML syntax and processing for digital signatures (asymmetric) applicable to any digital content.

**$ Yellow Book**
- **(D)**: /slang/ Synonym for "Computer Security Requirements: Guidance for Applying the DoD TCSEC in Specific Environments" [CSC3].
- **Deprecated Term**: IDOCs SHOULD NOT use as synonym; instead use full proper name or abbreviation.

**$ zero-knowledge proof**: (I) /cryptography/ Proof-of-possession protocol where entity proves possession of information without revealing it. (See: proof-of-possession protocol.)

**$ zeroize**
- **Definition 1 (I)**: Synonym for "erase", especially erasing keys in a cryptographic module. (See: sanitize.)
- **Definition 2 (O)**: Erase stored data to prevent recovery. [FP140]
- **Definition 3 (O)**: "To remove or eliminate the key from a cryptoequipment or fill device." [C4009]
- **Usage**: "Zeroize the device" normally means erasing all keys, sometimes all keying material or all cryptographic/sensitive information.

**$ zombie**: (I) /slang/ Internet host surreptitiously penetrated by intruder to attack others, especially in distributed flooding attacks.
- **Deprecated Usage**: Other cultures use different terms; IDOCs SHOULD NOT use. Instead use "compromised, coopted computer".

**$ zone of control**: (O) /EMSEC/ Synonym for "inspectable space". [C4009] (See: TEMPEST.)

## 5. Security Considerations

This document mainly defines security terms and recommends how to use them. It provides limited tutorial information about security aspects of Internet protocols but does not describe in detail vulnerabilities, threats, or definitive protection mechanisms.

## 6. Normative Reference

[R2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.

## 7. Informative References

This list emphasizes international, governmental, and industrial standards documents. Some RFCs mentioned in glossary entries are listed here; others mentioned in parentheses are not.

[A1523] American National Standards Institute, "American National Standard Telecom Glossary", ANSI T1.523-2001.
[A3092] ---, "American National Standard Data Encryption Algorithm", ANSI X3.92-1981.
[A9009] ---, "Financial Institution Message Authentication (Wholesale)", ANSI X9.9-1986.
[A9017] ---, "Financial Institution Key Management (Wholesale)", X9.17, 1985.
[A9042] ---, "Public key Cryptography for the Financial Service Industry: Agreement of Symmetric Keys Using Diffie-Hellman and MQV Algorithms", X9.42, 1999.
[A9052] ---, "Triple Data Encryption Algorithm Modes of Operation", X9.52-1998.
[A9062] ---, "Public Key Cryptography for the Financial Services Industry: The Elliptic Curve Digital Signature Algorithm (ECDSA)", X9.62-1998.
[A9063] ---, "Public Key Cryptography for the Financial Services Industry: Key Agreement and Key Transport Using Elliptic Curve Cryptography", X9.63-2001.
[ACM] Association for Computing Machinery, "Communications of the ACM", July 1998.
[Ande] Anderson, J., "Computer Security Technology Planning Study", ESD-TR-73-51, 1972.
[ANSI] American National Standards Institute, "Role Based Access Control", BSR INCITS 359, DRAFT, 2003.
[Army] U.S. Army Corps of Engineers, "Electromagnetic Pulse (EMP) and Tempest Protection for Facilities", EP 1110-3-2, 1990.
[B1822] Bolt Baranek and Newman Inc., "Specifications for the Interconnection of a Host and an IMP", BBN Report No. 1822, 1983.
[B4799] ---, "A History of the Arpanet: The First Decade", BBN Report No. 4799, 1981.
[Bell] Bell, D. and L. LaPadula, "Secure Computer Systems: Mathematical Foundations and Model", M74-244, 1973.
[Biba] K. Biba, "Integrity Considerations for Secure Computer Systems", ESD-TR-76-372, 1977.
[BN89] Brewer, D. and M. Nash, "The Chinese wall security policy", in Proceedings of IEEE Symposium on Security and Privacy, 1989.
[BS7799] British Standards Institution, "Information Security Management", BS 7799-1:1999 and BS 7799-2:1999.
[C4009] Committee on National Security Systems, "National Information Assurance (IA) Glossary", CNSS Instruction No. 4009, June 2006.
[CCIB] Common Criteria Implementation Board, "Common Criteria for Information Technology Security Evaluation, Part 1: Introduction and General Model", version 2.0, 1998.
[Chau] D. Chaum, "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms", in Communications of the ACM, vol. 24, no. 2, 1981.
[Cheh] Cheheyl, M. et al., "Verifying Security", in ACM Computing Surveys, vol. 13, no. 3, 1981.
[Chris] Chrissis, M. et al., "SW-CMM", version 3.0, Software Engineering Institute, 1996.
[CIPSO] Trusted Systems Interoperability Working Group, "Common IP Security Option", version 2.3, 1993.
[Clark] Clark, D. and D. Wilson, "A Comparison of Commercial and Military computer Security Policies", in Proceedings of IEEE Symposium on Security and Privacy, 1987.
[Cons] NSA, "Consistency Instruction Manual for Development of U.S. Government Protection Profiles", Release 2.0, 2004.
[CORBA] Object Management Group, "CORBAservices: Common Object Service Specification", 1998.
[CSC1] U.S. DoD Computer Security Center, "Department of Defense Trusted Computer System Evaluation Criteria", CSC-STD-001-83, 1983.
[CSC2] ---, "Department of Defense Password Management Guideline", CSC-STD-002-85, 1985.
[CSC3] ---, "Computer Security Requirements: Guidance for Applying the Department of Defense Trusted Computer System Evaluation Criteria in Specific Environments", CSC-STD-003-85, 1985.
[CSOR] U.S. Department of Commerce, "General Procedures for Registering Computer Security Objects", NIST IR 5308, 1993.
[Daem] Daemen, J. and V. Rijmen, "Rijndael, the advanced encryption standard", in Dr. Dobb's Journal, vol. 26, no. 3, 2001.
[DC6/9] Director of Central Intelligence, "Physical Security Standards for Sensitive Compartmented Information Facilities", DCI Directive 6/9, 2002.
[Denn] Denning, D., "A Lattice Model of Secure Information Flow", in Communications of the ACM, vol. 19, no. 5, 1976.
[Denns] Denning, D. and P. Denning, "Data Security", in ACM Computing Surveys, vol. 11, no. 3, 1979.
[DH76] Diffie, W. and M. Hellman, "New Directions in Cryptography", in IEEE Transactions on Information Theory, vol. IT-22, no. 6, 1976.
[DoD1] U.S. DoD, "Department of Defense Trusted Computer System Evaluation Criteria", DoD 5200.28-STD, 1985.
[DoD4] ---, "NSA Key Recovery Assessment Criteria", 1998.
[DoD5] ---, Directive 5200.1, "DoD Information Security Program", 1996.
[DoD6] ---, "Department of Defense Technical Architecture Framework for Information Management, Volume 6: DoD Goal Security Architecture", version 3.0, 1996.
[DoD7] ---, "X.509 Certificate Policy for the United States Department of Defense", version 7, 2002.
[DoD9] ---, "X.509 Certificate Policy for the United States Department of Defense", version 9, 2005.
[DoD10] ---, "DoD Architecture Framework, Version 1: Deskbook", 2004.
[DSG] American Bar Association, "Digital Signature Guidelines", 1996.
[ElGa] El Gamal, T., "A Public-Key Cryptosystem and a Signature Scheme Based on Discrete Logarithms", in IEEE Transactions on Information Theory, vol. IT-31, no. 4, 1985.
[EMV1] Europay, MasterCard, Visa, "EMV '96 Integrated Circuit Card Specification for Payment Systems", version 3.1.1, 1998.
[EMV2] ---, "EMV '96 Integrated Circuit Card Terminal Specification", version 3.1.1, 1998.
[EMV3] ---, "EMV '96 Integrated Circuit Card Application Specification", version 3.1.1, 1998.
[F1037] U.S. General Services Administration, "Glossary of Telecommunications Terms", FED STD 1037C, 1996.
[For94] Ford, W., "Computer Communications Security", 1994.
[For97] Ford, W. and M. Baum, "Secure Electronic Commerce", 1994.
[FP001] U.S. Department of Commerce, "Code for Information Interchange", FIPS PUB 1, 1968.
[FP031] ---, "Guidelines for Automatic Data Processing Physical Security and Risk Management", FIPS PUB 31, 1974.
[FP039] ---, "Glossary for Computer Systems Security", FIPS PUB 39, 1976.
[FP041] ---, "Computer Security Guidelines for Implementing the Privacy Act of 1974", FIPS PUB 41, 1975.
[FP046] ---, "Data Encryption Standard (DES)", FIPS PUB 46-3, 1999.
[FP074] ---, "Data Encryption Standard (DES)", FIPS PUB 46-3, 1999.
[FP081] ---, "DES Modes of Operation", FIPS PUB 81, 1980.
[FP087] ---, "Guidelines for ADP Contingency Planning", FIPS PUB 87, 1981.
[FP102] ---, "Guideline for Computer Security Certification and Accreditation", FIPS PUB 102, 1983.
[FP113] ---, "Computer Data Authentication", FIPS PUB 113, 1985.
[FP140] ---, "Security Requirements for Cryptographic Modules", FIPS PUB 140-2, 2001.
[FP151] ---, "Portable Operating System Interface (POSIX) -- System Application Program Interface [C Language]", FIPS PUB 151-2, 1993.
[FP180] ---, "Secure Hash Standard", FIPS PUB 180-2, 2000.
[FP185] ---, "Escrowed Encryption Standard", FIPS PUB 185, 1994.
[FP186] ---, "Digital Signature Standard (DSS)", FIPS PUB 186-2, 2000.
[FP188] ---, "Standard Security Label for Information Transfer", FIPS PUB 188, 1994.
[FP191] ---, "Guideline for the Analysis of Local Area Network Security", FIPS PUB 191, 1994.
[FP197] ---, "Advanced Encryption Standard", FIPS PUB 197, 2001.
[FP199] ---, "Standards for Security Categorization of Federal Information and Information Systems", FIPS PUB 199, 2003.
[FPKI] ---, "Public Key Infrastructure (PKI) Technical Specifications: Part A -- Technical Concept of Operations", 1998.
[Gass] Gasser, M., "Building a Secure Computer System", 1988.
[Gray] Gray, J. and A. Reuter, "Transaction Processing: Concepts and Techniques", 1993.
[Hafn] Hafner, K. and M. Lyon, "Where Wizards Stay Up Late: The Origins of the Internet", 1996.
[Huff] Huff, G., "Trusted Computer Systems -- Glossary", MTR 8201, 1981.
[I3166] ISO, "Codes for the Representation of Names of Countries and Their Subdivisions", ISO 3166.
[I7498-1] ISO/IEC 7498-1, "Information Processing Systems -- Open Systems Interconnection Reference Model, Part 1: Basic Reference Model".
[I7498-2] ISO/IEC 7498-2, "Information Processing Systems -- Open Systems Interconnection Reference Model, Part 2: Security Architecture", 1989.
[I7498-4] ISO/IEC 7498-4, "Information Processing Systems -- Open Systems Interconnection Reference Model, Part 4: Management Framework".
[I7812] ISO/IEC 7812, "Identification cards -- Identification of Issuers".
[I8073] ISO IS 8073, "Transport Protocol Specification".
[I8327] ISO IS 8327, "Session Protocol Specification".
[I8473] ISO IS 8473, "Protocol for Providing the Connectionless Network Service".
[I8802-2] ISO IS 8802-2, "Local Area Networks, Part 2: Logical Link Control".
[I8802-3] ISO IS 8802-3, "Local Area Networks, Part 3: CSMA/CD Access Method".
[I8823] ISO IS 8823, "Connection-Oriented Presentation Protocol Specification".
[I9945] ISO/IEC 9945-1, "Portable Operating System Interface for Computer Environments", 1990.
[IATF] NSA, "Information Assurance Technical Framework", Release 3, 2000.
[IDSAN] NSA, "Intrusion Detection System Analyzer Protection Profile", version 1.1, 2001.
[IDSSC] ---, "Intrusion Detection System Scanner Protection Profile", version 1.1, 2001.
[IDSSE] ---, "Intrusion Detection System Sensor Protection Profile", version 1.1, 2001.
[IDSSY] ---, "Intrusion Detection System", version 1.4, 2002.
[Ioan] Ioannidis, J. and M. Blaze, "The Architecture and Implementation of Network Layer Security in UNIX", in UNIX Security IV Symposium, 1993.
[ITSEC] "Information Technology Security Evaluation Criteria", version 1.2, 1991.
[JP1] U.S. DoD, "Department of Defense Dictionary of Military and Associated Terms", Joint Publication 1-02, 2007.
[John] Johnson, N. and S. Jajodia, "Exploring Steganography; Seeing the Unseen", in IEEE Computer, 1998.
[Kahn] Kahn, D., "The Codebreakers", 1967.
[Knut] Knuth, D., "The Art of Computer Programming", Volume 2, 1969.
[Kuhn] Kuhn, M. and R. Anderson, "Soft Tempest: Hidden Data Transmission Using Electromagnetic Emanations", in IH'98, LNCS 1525, 1998.
[Land] Landwehr, C., "Formal Models for Computer Security", in ACM Computing Surveys, vol. 13, no. 3, 1981.
[Larm] Larmouth, J., "ASN.1 Complete", 1999.
[M0404] U.S. Office of Management and Budget, "E-Authentication Guidance for Federal Agencies", Memorandum M-04-04, 2003.
[Mene] Menezes, A. et al, "Some Key Agreement Protocols Providing Implicit Authentication", in SAC 1995.
[Moor] Moore, A. et al, "Attack Modeling for Information Security and Survivability", CMU/SEI-2001-TN-001, 2001.
[Murr] Murray, W., "Courtney's Laws of Security", in Infosecurity News, 1993.
[N4001] NSTISSC, "Controlled Cryptographic Items", NSTISSI No. 4001, 1985.
[N4006] ---, "Controlled Cryptographic Items", NSTISSI No. 4006, 1991.
[N7003] ---, "Protective Distribution Systems", NSTISSI No. 7003, 1996.
[NCS01] NCSC, "A Guide to Understanding Audit in Trusted Systems", NCSC-TG-001, 1988.
[NCS03] ---, "Information System Security Policy Guideline", I942-TR-003, 1994.
[NCS04] ---, "Glossary of Computer Security Terms", NCSC-TG-004, 1988.
[NCS05] ---, "Trusted Network Interpretation of the TCSEC", NCSC-TG-005, 1987.
[NCS25] ---, "A Guide to Understanding Data Remanence in Automated Information Systems", NCSC-TG-025, 1991.
[NCSSG] NCSC, "COMPUSECese: Computer Security Glossary", NCSC-WA-001-85, 1985.
[NRC91] National Research Council, "Computers At Risk", 1991.
[NRC98] Schneider, F., ed., "Trust in Cyberspace", 1998.
[Padl] Padlipsky, M., "The Elements of Networking Style", 1985.
[PAG] American Bar Association, "PKI Assessment Guidelines", version 1.0, 2002.
[Park] Parker, D., "Computer Security Management", 1981.
[Perr] Perrine, T. et al, "An Overview of the Kernelized Secure Operating System (KSOS)", in Proceedings of 7th DoD/NBS Computer Security Conference, 1984.
[PGP] Garfinkel, S., "PGP: Pretty Good Privacy", 1995.
[PKCS] Kaliski Jr., B., "An Overview of the PKCS Standards", 1991.
[PKC05] RSA Laboratories, "PKCS #5: Password-Based Encryption Standard", version 1.5, 1993.
[PKC07] ---, "PKCS #7: Cryptographic Message Syntax Standard", version 1.5, 1993.
[PKC10] ---, "PKCS #10: Certification Request Syntax Standard", version 1.0, 1993.
[PKC11] ---, "PKCS #11: Cryptographic Token Interface Standard", version 1.0, 1995.
[PKC12] ---, "PKCS #12: Personal Information Exchange Syntax", version 1.0, 1995.
[R1108] Kent, S., "U.S. Department of Defense Security Options for the Internet Protocol", RFC 1108, 1991.
[R1135] Reynolds, J., "The Helminthiasis of the Internet", RFC 1135, 1989.
[R1208] Jacobsen, O. and D. Lynch, "A Glossary of Networking Terms", RFC 1208, 1991.
[R1281] Pethia, R. et al., "Guidelines for Secure Operation of the Internet", RFC 1281, 1991.
[R1319] Kaliski, B., "The MD2 Message-Digest Algorithm", RFC 1319, 1992.
[R1320] Rivest, R., "The MD4 Message-Digest Algorithm", RFC 1320, 1992.
[R1321] ---, "The MD5 Message-Digest Algorithm", RFC 1321, 1992.
[R1334] Lloyd, B. and W. Simpson, "PPP Authentication Protocols", RFC 1334, 1992.
[R1413] St. Johns, M., "Identification Protocol", RFC 1413, 1993.
[R1421] Linn, J., "Privacy Enhancement for Internet Electronic Mail, Part I", RFC 1421, 1993.
[R1422] Kent, S., "Privacy Enhancement for Internet Electronic Mail, Part II", RFC 1422, 1993.
[R1455] Eastlake 3rd, D., "Physical Link Security Type of Service", RFC 1455, 1993.
[R1457] Housley, R., "Security Label Framework for the Internet", RFC 1457, 1993.
[R1492] Finseth, C., "An Access Control Protocol, Sometimes Called TACACS", RFC 1492, 1993.
[R1507] Kaufman, C., "DASS: Distributed Authentication Security Service", RFC 1507, 1993.
[R1731] Myers, J., "IMAP4 Authentication Mechanisms", RFC 1731, 1994.
[R1734] ---, "POP3 AUTHentication Command", RFC 1734, 1994.
[R1760] Haller, N., "The S/KEY One-Time Password System", RFC 1760, 1995.
[R1824] Danisch, H., "The Exponential Security System TESS", RFC 1824, 1995.
[R1828] Metzger, P. and W. Simpson, "IP Authentication using Keyed MD5", RFC 1828, 1995.
[R1829] Karn, P. et al., "The ESP DES-CBC Transform", RFC 1829, 1995.
[R1848] Crocker, S. et al., "MIME Object Security Services", RFC 1848, 1995.
[R1851] Karn, P. et al., "The ESP Triple DES Transform", RFC 1851, 1995.
[R1928] Leech, M. et al., "SOCKS Protocol Version 5", RFC 1928, 1996.
[R1958] Carpenter, B., "Architectural Principles of the Internet", RFC 1958, 1996.
[R1983] Malkin, G., "Internet Users' Glossary", FYI 18, RFC 1983, 1996.
[R1994] Simpson, W., "PPP Challenge Handshake Authentication Protocol (CHAP)", RFC 1994, 1996.
[R2078] Linn, J., "Generic Security Service Application Program Interface, Version 2", RFC 2078, 1997.
[R2084] Bossert, G. et al., "Considerations for Web Transaction Security", RFC 2084, 1997.
[R2104] Krawczyk, H. et al., "HMAC: Keyed-Hashing for Message Authentication", RFC 2104, 1997.
[R2144] Adams, C., "The CAST-128 Encryption Algorithm", RFC 2144, 1997.
[R2179] Gwinn, A., "Network Security For Trade Shows", RFC 2179, 1997.
[R2195] Klensin, J. et al., "IMAP/POP AUTHorize Extension for Simple Challenge/Response", RFC 2195, 1997.
[R2196] Fraser, B., "Site Security Handbook", FYI 8, RFC 2196, 1997.
[R2202] Cheng, P. and R. Glenn, "Test Cases for HMAC-MD5 and HMAC-SHA-1", RFC 2202, 1997.
[R2222] Myers, J., "Simple Authentication and Security Layer (SASL)", RFC 2222, 1997.
[R2289] Haller, N. et al., "A One-Time Password System", STD 61, RFC 2289, 1998.
[R2323] Ramos, A., "IETF Identification and Security Guidelines", RFC 2323, 1998 (humorous).
[R2350] Brownlee, N. and E. Guttman, "Expectations for Computer Security Incident Response", BCP 21, RFC 2350, 1998.
[R2356] Montenegro, G. and V. Gupta, "Sun's SKIP Firewall Traversal for Mobile IP", RFC 2356, 1998.
[R2401] Kent, S. and R. Atkinson, "Security Architecture for the Internet Protocol", RFC 2401, 1998.
[R2402] ---, "IP Authentication Header", RFC 2402, 1998.
[R2403] Madson, C. and R. Glenn, "The Use of HMAC-MD5-96 within ESP and AH", RFC 2403, 1998.
[R2404] ---, "The Use of HMAC-SHA-1-96 within ESP and AH", RFC 2404, 1998.
[R2405] Madson, C. and N. Doraswamy, "The ESP DES-CBC Cipher Algorithm With Explicit IV", RFC 2405, 1998.
[R2406] Kent, S. and R. Atkinson, "IP Encapsulating Security Payload (ESP)", RFC 2406, 1998.
[R2407] Piper, D., "The Internet IP Security Domain of Interpretation for ISAKMP", RFC 2407, 1998.
[R2408] Maughan, D. et al., "Internet Security Association and Key Management Protocol (ISAKMP)", RFC 2408, 1998.
[R2410] Glenn, R. and S. Kent, "The NULL Encryption Algorithm and Its Use With IPsec", RFC 2410, 1998.
[R2412] Orman, H., "The OAKLEY Key Determination Protocol", RFC 2412, 1998.
[R2451] Pereira, R. and R. Adams, "The ESP CBC-Mode Cipher Algorithms", RFC 2451, 1998.
[R2504] Guttman, E. et al., "Users' Security Handbook", RFC 2504, 1999.
[R2560] Myers, M. et al., "X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP", RFC 2560, 1999.
[R2612] Adams, C. and J. Gilchrist, "The CAST-256 Encryption Algorithm", RFC 2612, 1999.
[R2628] Smyslov, V., "Simple Cryptographic Program Interface (Crypto API)", RFC 2628, 1999.
[R2631] Rescorla, E., "Diffie-Hellman Key Agreement Method", RFC 2631, 1999.
[R2634] Hoffman, P., "Enhanced Security Services for S/MIME", RFC 2634, 1999.
[R2635] Hambridge, S. and A. Lunde, "DON'T SPEW: A Set of Guidelines for Mass Unsolicited Mailings and Postings", RFC 2635, 1999.
[R2660] Rescorla, E. and A. Schiffman, "The Secure HyperText Transfer Protocol", RFC 2660, 1999.
[R2743] Linn, J., "Generic Security Service Application Program Interface Version 2, Update 1", RFC 2743, 2000.
[R2773] Housley, R. et al., "Encryption using KEA and SKIPJACK", RFC 2773, 2000.
[R2801] Burdett, D., "Internet Open Trading Protocol - IOTP, Version 1.0", RFC 2801, 2000.
[R2827] Ferguson, P. and D. Senie, "Network Ingress Filtering: Defeating Denial of Service Attacks which employ IP Source Address Spoofing", BCP 38, RFC 2827, 2000.
[R2865] Rigney, C. et al., "Remote Authentication Dial In User Service (RADIUS)", RFC 2865, 2000.
[R3060] Moore, B. et al., "Policy Core Information Model -- Version 1 Specification", RFC 3060, 2001.
[R3198] Westerinen, A. et al., "Terminology for Policy-Based Management", RFC 3198, 2001.
[R3280] Housley, R. et al., "Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile", RFC 3280, 2002.
[R3547] Baugher, M. et al., "Group Domain of Interpretation", RFC 3547, 2003.
[R3552] Rescorla, E. and B. Korver, "Guidelines for Writing RFC Text on Security Considerations", RFC 3552, 2003.
[R3647] Chokhani, S. et al., "Internet X.509 Public Key Infrastructure Certificate Policy and Certification Practices Framework", RFC 3647, 2003.
[R3739] Santesson, S. et al., "Internet X.509 Public Key Infrastructure: Qualified Certificates Profile", RFC 3739, 2004.
[R3740] Hardjono, T. and B. Weis, "The Multicast Group Security Architecture", RFC 3740, 2004.
[R3748] Aboba, B. et al., "Extensible Authentication Protocol (EAP)", RFC 3748, 2004.
[R3766] Orman, H. and P. Hoffman, "Determining Strengths For Public Keys Used For Exchanging Symmetric Keys", BCP 86, RFC 3766, 2004.
[R3820] Tuecke, S. et al., "Internet X.509 Public Key Infrastructure (PKI) Proxy Certificate Profile", RFC 3820, 2004.
[R3851] Ramsdell, B., "Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 3.1 Message Specification", RFC 3851, 2004.
[R3871] Jones, G., "Operational Security Requirements for Large Internet Service Provider (ISP) IP Network Infrastructure", RFC 3871, 2004.
[R4033] Arends, R. et al., "DNS Security Introduction and Requirements", RFC 4033, 2005.
[R4034] ---, "Resource Records for the DNS Security Extensions", RFC 4034, 2005.
[R4035] ---, "Protocol Modifications for the DNS Security Extensions", RFC 4035, 2005.
[R4086] Eastlake, D. et al., "Randomness Requirements for Security", BCP 106, RFC 4086, 2005.
[R4120] Neuman, C. et al., "The Kerberos Network Authentication Service (V5)", RFC 4120, 2005.
[R4158] Cooper, M. et al., "Internet X.509 Public Key Infrastructure: Certification Path Building", RFC 4158, 2005.
[R4210] Adams, C. et al., "Internet X.509 Public Key Infrastructure Certificate Management Protocol (CMP)", RFC 4210, 2005.
[R4301] Kent, S. and K. Seo, "Security Architecture for the Internet Protocol", RFC 4301, 2005.
[R4302] Kent, S., "IP Authentication Header", RFC 4302, 2005.
[R4303] ---, "IP Encapsulating Security Payload (ESP)", RFC 4303, 2005.
[R4306] Kaufman, C., "Internet Key Exchange (IKEv2) Protocol", RFC 4306, 2005.
[R4346] Dierks, T. and E. Rescorla, "The Transport Layer Security (TLS) Protocol Version 1.1", RFC 4346, 2006.
[R4422] Melnikov, A. and K. Zeilenga, "Simple Authentication and Security Layer (SASL)", RFC 4422, 2006.
[Raym] Raymond, E., ed., "The On-Line Hacker Jargon File", version 4.0.0, 1996.
[Roge] Rogers, H., "An Overview of the CANEWARE Program", in Proceedings of 10th National Computer Security Conference, 1987.
[RSA78] Rivest, R., A. Shamir, and L. Adleman, "A Method for Obtaining Digital Signatures and Public-Key Cryptosystems", in Communications of the ACM, vol. 21, no. 2, 1978.
[RSCG] NSA, "Router Security Configuration Guide", version 1.1c, 2005.
[Russ] Russell, D. et al., "Computer Security Basics", 1991.
[SAML] OASIS, "Security Assertion Markup Language (SAML) Version 1.1", 2003.
[Sand] Sandhu, R. et al., "Role-Based Access Control Models", in IEEE Computer, vol. 29, no. 2, 1996.
[Schn] Schneier, B., "Applied Cryptography Second Edition", 1996.
[SDNS3] U.S. DoD, NSA, "Secure Data Network Systems, Security Protocol 3 (SP3)", document SDN.301, 1989.
[SDNS4] ---, "Secure Data Network Systems, Security Protocol 4 (SP4)", SDN.401, 1988.
[SDNS7] ---, "Secure Data Network Systems, Message Security Protocol (MSP)", SDN.701, 1996.
[SET1] MasterCard and Visa, "SET Secure Electronic Transaction Specification, Book 1: Business Description", version 1.0, 1997.
[SET2] ---, "SET Secure Electronic Transaction Specification, Book 2: Programmer's Guide", version 1.0, 1997.
[SKEME] Krawczyk, H., "SKEME: A Versatile Secure Key Exchange Mechanism for Internet", in Proceedings of 1996 Symposium on Network and Distributed Systems Security.
[SKIP] "SKIPJACK and KEA Algorithm Specifications", version 2.0, 1998.
[SP12] NIST, "An Introduction to Computer Security: The NIST Handbook", Special Publication 800-12.
[SP14] ---, "Generally Accepted Principles and Practices for Security Information Technology Systems", SP 800-14, 1996.
[SP15] ---, "Minimum Interoperability Specification for PKI Components (MISPC), Version 1", SP 800-15, 1997.
[SP22] ---, "A Statistical Test Suite for Random and Pseudorandom Number Generators for Cryptographic Applications", SP 800-22, 2001.
[SP27] ---, "Engineering Principles for Information Technology Security", SP 800-27 Rev A, 2004.
[SP28] ---, "Guidelines on Active Content and Mobile Code", SP 800-28, 2001.
[SP30] ---, "Risk Management Guide for Information Technology Systems", SP 800-30, 2001.
[SP31] ---, "Intrusion Detection Systems", SP 800-31.
[SP32] ---, "Introduction to Public Key Technology and the Federal PKI Infrastructure", SP 800-32, 2001.
[SP33] ---, "Underlying Technical Models for Information Technology Security", SP 800-33, 2001.
[SP37] ---, "Guide for the Security Certification and Accreditation of Federal Information Systems", SP 800-37, 2004.
[SP38A] Dworkin, M., "Recommendation for Block Cipher Modes of Operation: Methods and Techniques", SP 800-38A, 2001.
[SP38B] ---, "Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication", SP 800-38B, 2005.
[SP38C] ---, "Recommendation for Block Cipher Modes of Operation: The CCM Mode for Authentication and Confidentiality", SP 800-38C, 2004.
[SP41] Wack, J. et al., "Guidelines on Firewalls and Firewall Policy", SP 800-41, 2002.
[SP42] ---, "Guideline on Network Security Testing", SP 800-42, 2003.
[SP56] NIST, "Recommendations on Key Establishment Schemes", Draft 2.0, SP 800-56, 2003.
[SP57] ---, "Recommendation for Key Management, Part 1 and 2", SP 800-57, DRAFT, 2003.
[SP61] Grance, T. et al., "Computer Security Incident Handling Guide", SP 800-61, 2003.
[SP63] Burr, W. et al., "Electronic Authentication Guideline", SP 800-63, 2004.
[SP67] Barker, W., "Recommendation for the Triple Data Encryption Algorithm (TDEA) Block Cipher", SP 800-67, 2004.
[Stal] Stallings, W., "Local Networks", 1987.
[Stei] Steiner, J. et al., "Kerberos: An Authentication Service for Open Network Systems", in Usenix Conference Proceedings, 1988.
[Weis] Weissman, C., "Blacker: Security for the DDN", in Symposium on Security and Privacy, 1992.
[X400] ITU-T Recommendation X.400, "Message Handling Services".
[X419] ITU-T Recommendation X.419, "Message Handling Systems: Protocol Specifications".
[X420] ITU-T Recommendation X.420, "Message Handling Systems: Interpersonal Messaging System".
[X500] ITU-T Recommendation X.500, "Information Technology -- Open Systems Interconnection -- The Directory: Overview of Concepts, Models, and Services".
[X501] ITU-T Recommendation X.501, "The Directory: Models".
[X509] ITU-T Recommendation X.509, "The Directory: Authentication Framework", 2001.
[X519] ITU-T Recommendation X.519, "The Directory: Protocol Specifications".
[X520] ITU-T Recommendation X.520, "The Directory: Selected Attribute Types".
[X680] ITU-T Recommendation X.680, "Abstract Syntax Notation One (ASN.1) - Specification of Basic Notation", 1994.
[X690] ITU-T Recommendation X.690, "ASN.1 Encoding Rules", 1994.

## Acknowledgments

George Huff had a good idea! [Huff]

## Author's Address

Dr. Robert W. Shirey  
3516 N. Kensington St.  
Arlington, Virginia 22207-1328  
USA  
EMail: rwshirey4949@verizon.net

## Full Copyright Statement

Copyright (C) The IETF Trust (2007). This document is subject to the rights, licenses and restrictions contained in BCP 78 and at www.rfc-editor.org/copyright.html, and except as set forth therein, the authors retain all their rights. This document and the information contained herein are provided on an "AS IS" basis and THE CONTRIBUTOR, THE ORGANIZATION HE/SHE REPRESENTS OR IS SPONSORED BY (IF ANY), THE INTERNET SOCIETY, THE IETF TRUST AND THE INTERNET ENGINEERING TASK FORCE DISCLAIM ALL WARRANTIES, EXPRESS OR IMPLIED.

## Intellectual Property

The IETF takes no position regarding the validity or scope of any Intellectual Property Rights. Copies of IPR disclosures and assurances of licenses can be obtained from the IETF on-line IPR repository at http://www.ietf.org/ipr. The IETF invites any interested party to bring to its attention any copyrights, patents, or patent applications that may cover technology required to implement this standard. Address information to ietf-ipr@ietf.org.

## Acknowledgement

Funding for the RFC Editor function is currently provided by the Internet Society.