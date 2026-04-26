# RFC 5912: New ASN.1 Modules for the Public Key Infrastructure Using X.509 (PKIX)
**Source**: IETF | **Version**: Informational | **Date**: June 2010 | **Type**: Informational  
**Original**: http://www.rfc-editor.org/info/rfc5912

## Scope (Summary)
This document updates ASN.1 modules from multiple PKIX-related RFCs (2560, 2986, 3279, 3852, 4055, 4210, 4211, 5055, 5272, 5755, 5280) to conform to the 2002 version of ASN.1 (ITU-T X.680 series). No bits-on-the-wire changes are introduced; only the syntax is updated. The document also provides two new shared modules: PKIX-CommonTypes and AlgorithmInformation.

## Normative References
- **ITU-T X.680, X.681, X.682, X.683 (2002)**: ASN.1 specifications.
- **RFC 2560**: OCSP.
- **RFC 2986**: PKCS #10.
- **RFC 3279**: Algorithms and Identifiers for PKIX.
- **RFC 3852**: CMS (Attribute Certificate v1).
- **RFC 4055**: Additional RSA Algorithms.
- **RFC 4210**: CMP.
- **RFC 4211**: CRMF.
- **RFC 5055**: SCVP.
- **RFC 5272**: CMC.
- **RFC 5280**: PKIX Certificate and CRL Profile.
- **RFC 5480**: Elliptic Curve Subject Public Key Information.
- **RFC 5755**: Attribute Certificates v2.
- **RFC 5911**: New ASN.1 Modules for CMS and S/MIME.

## Definitions and Abbreviations
- **ASN.1**: Abstract Syntax Notation One (2002 version).
- **OID**: Object Identifier.
- **ATTRIBUTE**: Information object class describing attributes (with &id, &Type, &equality-match, &minCount, &maxCount).
- **EXTENSION**: Information object class describing certificate/CRL extensions (with &id, &ExtnType, &Critical).
- **AlgorithmIdentifier**: Parameterized type `AlgorithmIdentifier{ALGORITHM-TYPE, AlgorithmSet}`.
- **SIGNED**: Parameterized type `SIGNED{ToBeSigned}` for certificates and CRLs.
- **ParamOptions**: Enumeration {required, preferredPresent, preferredAbsent, absent, inheritable, optional, ...}.

## Module Summaries

### 2. PKIX-CommonTypes (`PKIX-CommonTypes-2009`)
- OID: `{iso(1) identified-organization(3) dod(6) internet(1) security(5) mechanisms(5) pkix(7) id-mod(0) id-mod-pkixCommon-02(57)}`
- Defines:
  - **ATTRIBUTE** class (prefixes: at- for certificate, aa- for CMS).
  - **MATCHING-RULE** class.
  - **AttributeSet**, **SingleAttribute**, **Attribute** parameterized types.
  - **EXTENSION** class.
  - **Extensions**, **Extension** parameterized types.
  - **SECURITY-CATEGORY** TYPE-IDENTIFIER.
  - **SecurityCategory** parameterized type.

### 3. AlgorithmInformation (`AlgorithmInformation-2009`)
- OID: `{iso(1) ... id-mod-algorithmInformation-02(58)}`
- Imports: `KeyUsage` from PKIX1Implicit-2009.
- Defines:
  - **ParamOptions** enumeration.
  - **DIGEST-ALGORITHM** class.
  - **SIGNATURE-ALGORITHM** class.
  - **PUBLIC-KEY** class.
  - **KEY-TRANSPORT** class.
  - **KEY-AGREE** class.
  - **KEY-WRAP** class.
  - **KEY-DERIVATION** class.
  - **MAC-ALGORITHM** class.
  - **CONTENT-ENCRYPTION** class.
  - **ALGORITHM** class.
  - **SMIME-CAPS** class.
  - **AlgorithmIdentifier** parameterized type.
  - **SMIMECapability**, **SMIMECapabilities** parameterized types.

### 4. OCSP (`OCSP-2009`) – based on RFC 2560
- OID: `{iso(1) ... id-mod-ocsp-02(48)}`
- Defines:
  - **OCSPRequest**, **TBSRequest**, **Signature**, **Version**, **Request**, **CertID**, **OCSPResponse**, **OCSPResponseStatus**, **RESPONSE**, **ResponseSet**, **ResponseBytes**, **BasicOCSPResponse**, **ResponseData**, **ResponderID**, **KeyHash**, **SingleResponse**, **CertStatus**, **RevokedInfo**, **UnknownInfo**, **CRLReason**, **ArchiveCutoff**, **AcceptableResponses**, **ServiceLocator**, **CrlID**.
  - Request extensions: `re-ocsp-nonce`, `re-ocsp-response`, `re-ocsp-service-locator`.
  - Response extensions: `re-ocsp-crl`, `re-ocsp-archive-cutoff`.
  - OIDs: `id-kp-OCSPSigning`, `id-pkix-ocsp-basic`, etc.

### 5. PKCS-10 (`PKCS-10`) – based on RFC 2986
- OID: `{iso(1) ... id-mod-pkcs10-2009(69)}`
- Defines:
  - **CertificationRequestInfo**, **SubjectPublicKeyInfo** (parameterized), **PKInfoAlgorithms**, **Attributes**, **CRIAttributes**, **Attribute**, **CertificationRequest**, **SignatureAlgorithms**.

### 6. PKIXAlgs (`PKIXAlgs-2009`) – based on RFC 3279/5480
- OID: `{iso(1) ... id-mod-pkix1-algorithms2008-02(56)}`
- Defines public key objects (pk-rsa, pk-dsa, pk-dh, pk-kea, pk-ec, pk-ecDH, pk-ecMQV), signature algorithms (sa-rsaWithMD2, sa-rsaWithMD5, sa-rsaWithSHA1, sa-dsaWithSHA1, sa-dsaWithSHA224, sa-dsaWithSHA256, sa-ecdsaWithSHA1/224/256/384/512), message digest algorithms (mda-md2, mda-md5, mda-sha1), OIDs for RSA, DSA, DH, EC parameters, named curves (secp192r1, sect163k1, etc.), and signature values (DSA-Sig-Value, ECDSA-Sig-Value).

### 7. AttributeCertificateV1 (`AttributeCertificateVersion1-2009`) – based on RFC 3852
- OID: `{iso(1) ... id-mod-v1AttrCert-02(49)}`
- Defines: `AttributeCertificateV1`, `AttributeCertificateInfoV1`, `AttCertVersionV1`, `AttrList`, `AttributeCertExtensionsV1`.

### 8. RSA PSS/OAEP (`PKIX1-PSS-OAEP-Algorithms-2009`) – based on RFC 4055
- OID: `{iso(1) ... id-mod-pkix1-rsa-pkalgs-02(54)}`
- Defines:
  - Public key objects: `pk-rsaSSA-PSS`, `pk-rsaES-OAEP`.
  - Signature algorithms: `sa-rsaSSA-PSS`, `sa-sha224/256/384/512WithRSAEncryption`.
  - Key transport algorithm: `kta-rsaES-OAEP`.
  - Hash algorithms: `mda-sha224`, `mda-sha256`, `mda-sha384`, `mda-sha512`.
  - Structures: `RSASSA-PSS-params`, `RSAES-OAEP-params`, `HashAlgorithm`, `MaskGenAlgorithm`, `PSourceAlgorithm`.

### 9. CMP (`PKIXCMP-2009`) – based on RFC 4210
- OID: `{iso(1) ... id-mod-cmp2000-02(50)}`
- Defines:
  - `CMPCertificate`, `PKIMessage`, `PKIMessages`, `PKIHeader`, `PKIBody`, `PKIProtection`, `ProtectedPart`.
  - `PBMParameter`, `DHBMParameter`, `PKIStatus`, `PKIFailureInfo`, `PKIStatusInfo`, `OOBCert`, `OOBCertHash`.
  - `POPODecKeyChallContent`, `Challenge`, `POPODecKeyRespContent`.
  - `CertRepMessage`, `CertResponse`, `CertifiedKeyPair`, `CertOrEncCert`, `KeyRecRepContent`.
  - `RevReqContent`, `RevDetails`, `RevRepContent`.
  - `CAKeyUpdAnnContent`, `CertAnnContent`, `RevAnnContent`, `CRLAnnContent`.
  - `PKIConfirmContent`, `NestedMessageContent`.
  - `INFO-TYPE-AND-VALUE`, `InfoTypeAndValue`, `SupportedInfoSet`, `GenMsgContent`, `GenRepContent`, `ErrorMsgContent`, `CertConfirmContent`, `CertStatus`, `PollReqContent`, `PollRepContent`.

### 10. CRMF (`PKIXCRMF-2009`) – based on RFC 4211
- OID: `{iso(1) ... id-mod-crmf2005-02(55)}`
- Defines:
  - `CertReqMessages`, `CertReqMsg`, `CertRequest`, `CertTemplate`, `OptionalValidity`, `Controls`.
  - `ProofOfPossession` (raVerified, signature, keyEncipherment, keyAgreement), `POPOSigningKey`, `POPOSigningKeyInput`, `PKMACValue`, `Password-MACAlgorithms`, `PBMParameter`.
  - `POPOPrivKey` (thisMessage, subsequentMessage, dhMAC, agreeMAC, encryptedKey).
  - `ct-encKeyWithID`, `EncKeyWithID`, `PrivateKeyInfo`, `Attributes`.
  - Registration controls: `regCtrl-regToken`, `regCtrl-authenticator`, `regCtrl-pkiPublicationInfo`, `regCtrl-pkiArchiveOptions`, `regCtrl-oldCertID`, `regCtrl-protocolEncrKey`.
  - Registration info: `regInfo-utf8Pairs`, `regInfo-certReq`.

### 11. SCVP (`SCVP-2009`) – based on RFC 5055
- OID: `{iso(1) ... id-mod-scvp-02(52)}`
- Defines:
  - Content types: `ct-scvp-certValRequest`, `ct-scvp-certValResponse`, `ct-scvp-valPolRequest`, `ct-scvp-valPolResponse`.
  - Request structures: `CVRequest`, `Query`, `CertReferences`, `CertReference`, `PKCReference`, `ACReference`, `SCVPCertID`, `SCVPIssuerSerial`, `ValidationPolicy`, `CertChecks`, `WantBack`, `TrustAnchors`, `KeyAgreePublicKey`, `ResponseFlags`, `CertBundle`, `RevocationInfos`, `RevocationInfo`.
  - Response structures: `CVResponse`, `ResponseStatus`, `CVStatusCode`, `RespValidationPolicy`, `RequestReference`, `ReplyObjects`, `CertReply`, `ReplyStatus`, `ReplyChecks`, `ReplyWantBacks`.
  - WANT-BACK objects: `swb-pkc-best-cert-path`, `swb-pkc-revocation-info`, etc.
  - Validation policy and algorithm OIDs: `id-svp-defaultValPolicy`, `id-svp-basicValAlg`, `id-svp-nameValAlg`, and error sets.

### 12. CMC (`EnrollmentMessageSyntax-2009`) – based on RFC 5272
- OID: `{iso(1) ... id-mod-cmc2002-02(53)}`
- Defines:
  - Content types: `ct-PKIData`, `ct-PKIResponse`.
  - `PKIData`, `TaggedAttribute`, `TaggedRequest`, `TaggedCertificationRequest`, `TaggedContentInfo`, `OtherMsg`.
  - CMC-CONTROL objects: `cmc-identityProof`, `cmc-statusInfo`, `cmc-addExtensions`, `cmc-encryptedPOP`, `cmc-decryptedPOP`, `cmc-getCert`, `cmc-getCRL`, `cmc-revokeRequest`, `cmc-statusInfoV2`, `cmc-trustedAnchors`, `cmc-authData`, `cmc-batchRequests`, `cmc-batchResponses`, `cmc-publishCert`, `cmc-modCertTemplate`, `cmc-controlProcessed`, `cmc-identityProofV2`, `cmc-popLinkWitnessV2`.
  - `CMCStatus`, `CMCFailInfo`, `CMCCertId`, `ExtensionReq`, `NoSignatureValue`, `CMCUnsignedData`, `PublishTrustAnchors`, `AuthPublish`, `BodyPartList`, `CMCPublicationInfo`, `ModCertTemplate`, `ControlsProcessed`, `IdentityProofV2`, `PopLinkWitnessV2`.

### 13. AttributeCertificates v2 (`PKIXAttributeCertificate-2009`) – based on RFC 5755
- OID: `{iso(1) ... id-mod-attribute-cert-02(47)}`
- Defines:
  - Extensions: `ext-auditIdentity`, `ext-targetInformation`, `ext-noRevAvail`, `ext-ac-proxying`, `ext-aaControls`.
  - Attributes: `at-authenticationInfo`, `at-accesIdentity`, `at-chargingIdentity`, `at-group`, `at-role`, `at-clearance`, `at-encAttrs`.
  - `AttributeCertificate`, `AttributeCertificateInfo`, `Holder`, `ObjectDigestInfo`, `AttCertIssuer`, `V2Form`, `IssuerSerial`, `AttCertValidityPeriod`.
  - Extension syntax: `Targets`, `Target`, `TargetCert`, `AAControls`, `ProxyInfo`.
  - Attribute syntax: `IetfAttrSyntax`, `SvceAuthInfo`, `RoleSyntax`, `Clearance`, `ClassList`, `SecurityCategory-rfc3281`, `ACClearAttrs`.

### 14. PKIX1Explicit-2009 and PKIX1Implicit-2009 – based on RFC 5280
- **PKIX1Explicit-2009**: OID `{iso(1) ... id-mod-pkix1-explicit-02(51)}`
  - Defines: `id-pkix`, `id-pe`, `id-qt`, `id-kp`, `id-ad`, attribute types and values, `Name`, `RDNSequence`, `DistinguishedName`, `RelativeDistinguishedName`, `Certificate`, `TBSCertificate`, `Version`, `CertificateSerialNumber`, `Validity`, `Time`, `UniqueIdentifier`, `SubjectPublicKeyInfo`, `CertificateList`, `TBSCertList`, `SignatureAlgorithms`, `PublicKeyAlgorithms`, upper bounds.
  - **SIGNED** parameterized type using version 3 (ties signature algorithm and value).
- **PKIX1Implicit-2009**: OID `{iso(1) ... id-mod-pkix1-implicit-02(59)}`
  - Imports from explicit module.
  - Defines certificate and CRL extensions: `ext-AuthorityKeyIdentifier`, `ext-SubjectKeyIdentifier`, `ext-KeyUsage`, `ext-PrivateKeyUsagePeriod`, `ext-CertificatePolicies`, `ext-PolicyMappings`, `ext-SubjectAltName`, `ext-IssuerAltName`, `ext-SubjectDirectoryAttributes`, `ext-BasicConstraints`, `ext-NameConstraints`, `ext-PolicyConstraints`, `ext-ExtKeyUsage`, `ext-CRLDistributionPoints`, `ext-InhibitAnyPolicy`, `ext-FreshestCRL`, `ext-AuthorityInfoAccess`, `ext-SubjectInfoAccessSyntax`.
  - CRL extensions: `ext-CRLNumber`, `ext-DeltaCRLIndicator`, `ext-IssuingDistributionPoint`, `ext-CRLReason`, `ext-CertificateIssuer`, `ext-HoldInstructionCode`, `ext-InvalidityDate`.
  - Structures: `AuthorityKeyIdentifier`, `KeyIdentifier`, `KeyUsage`, `PrivateKeyUsagePeriod`, `CertificatePolicies`, `PolicyInformation`, `PolicyQualifierInfo`, `UserNotice`, `DisplayText`, `PolicyMappings`, `GeneralNames`, `GeneralName`, `EDIPartyName`, `BasicConstraints`, `NameConstraints`, `GeneralSubtrees`, `GeneralSubtree`, `PolicyConstraints`, `SkipCerts`, `CRLDistributionPoints`, `DistributionPoint`, `DistributionPointName`, `ReasonFlags`, `ExtKeyUsageSyntax`, `KeyPurposeId`, `AuthorityInfoAccessSyntax`, `SubjectInfoAccessSyntax`, `CRLNumber`, `IssuingDistributionPoint`, `CRLReason`, and upper bounds.
  - Also includes `PKIX-X400Address-2009` module for ORAddress.

## Requirements Summary
(The document does not contain standalone textual requirements; all normative statements are embedded in ASN.1 definitions and comments. Key normative directives include:
- Parameter presence `MUST`/`MUST NOT`/`SHOULD`/`MAY` as per `ParamOptions`.
- `MUST NOT be used` for implicitCurve and specifiedCurve in ECParameters.
- `MUST be present` for certain fields (e.g., `subject` and `publicKey` in POPOSigningKeyInput when poposkInput omitted).
- `DEFAULT` values for optional fields.
- OIDs with specific arcs.
- `WITH COMPONENTS` constraints.

A detailed requirements table would be overly large; the above summaries capture the normative structure.)

## Security Considerations
This document introduces no new security considerations; the ASN.1 modules maintain identical bits-on-the-wire encoding as the original RFCs.