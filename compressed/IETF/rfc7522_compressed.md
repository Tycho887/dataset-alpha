# RFC 7522: Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants
**Source**: IETF | **Version**: Standards Track | **Date**: May 2015 | **Type**: Normative
**Original**: https://www.rfc-editor.org/rfc/rfc7522

## Scope (Summary)
Defines the use of a SAML 2.0 Bearer Assertion as an authorization grant and client authentication mechanism for OAuth 2.0, profiled from the OAuth Assertion Framework [RFC7521].

## Normative References
- [OASIS.saml-core-2.0-os] Cantor et al., "Assertions and Protocols for the OASIS Security Assertion Markup Language (SAML) V2.0", March 2005
- [OASIS.saml-deleg-cs] Cantor, "SAML V2.0 Condition for Delegation Restriction Version 1", November 2009
- [OASIS.saml-sec-consider-2.0-os] Hirsch et al., "Security and Privacy Considerations for the OASIS Security Assertion Markup Language (SAML) V2.0", March 2005
- [RFC2119] Bradner, "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, March 1997
- [RFC3986] Berners-Lee et al., "Uniform Resource Identifier (URI): Generic Syntax", STD 66, January 2005
- [RFC4648] Josefsson, "The Base16, Base32, and Base64 Data Encodings", October 2006
- [RFC6749] Hardt, "The OAuth 2.0 Authorization Framework", October 2012
- [RFC6931] Eastlake, "Additional XML Security Uniform Resource Identifiers (URIs)", April 2013
- [RFC7521] Campbell et al., "Assertion Framework for OAuth 2.0 Client Authentication and Authorization Grants", May 2015

## Definitions and Abbreviations
All terms are as defined in [RFC6749], [RFC7521], and [OASIS.saml-core-2.0-os].

## 1. Introduction
- **Purpose**: Extends OAuth 2.0 with SAML 2.0 Bearer Assertions for requesting access tokens and client authentication.
- **Key concept**: Uses an existing trust relationship expressed in a SAML Assertion without a direct user approval step at the authorization server.
- **Out of scope**: How the client obtains the SAML Assertion.

### 1.1. Notational Conventions
- The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" are to be interpreted as described in RFC 2119 [RFC2119].
- All protocol parameter names and values are case sensitive unless otherwise noted.

### 1.2. Terminology
All terms are as defined in [RFC6749], [RFC7521], and [OASIS.saml-core-2.0-os].

## 2. HTTP Parameter Bindings for Transporting Assertions
Defines parameters for using SAML 2.0 Bearer Assertions with the OAuth Assertion Framework [RFC7521].

### 2.1. Using SAML Assertions as Authorization Grants
- **grant_type**: `urn:ietf:params:oauth:grant-type:saml2-bearer`
- **assertion**: MUST contain a single SAML 2.0 Assertion encoded using base64url (no line wraps, no padding "=").
- **scope**: MAY be used to request scope.
- **client_id**: Only needed when client authentication relies on it.
- Example access token request (with line breaks for display):
  ```
  POST /token.oauth2 HTTP/1.1
  Host: as.example.com
  Content-Type: application/x-www-form-urlencoded

  grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Asaml2-bearer&
  assertion=PHNhbWxwOl...[omitted]...ZT4
  ```

### 2.2. Using SAML Assertions for Client Authentication
- **client_assertion_type**: `urn:ietf:params:oauth:client-assertion-type:saml2-bearer`
- **client_assertion**: MUST contain a single SAML 2.0 Assertion encoded using base64url (SHOULD NOT be line wrapped, SHOULD NOT include padding "=").
- Example with authorization code grant:
  ```
  POST /token.oauth2 HTTP/1.1
  Host: as.example.com
  Content-Type: application/x-www-form-urlencoded

  grant_type=authorization_code&
  code=n0esc3NRze7LTCu7iYzS6a5acc3f0ogp4&
  client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type%3Asaml2-bearer&
  client_assertion=PHNhbW...[omitted]...ZT
  ```

## 3. Assertion Format and Processing Requirements
The authorization server **MUST** validate the Assertion according to the criteria below. Additional policy is at the discretion of the authorization server.

1. **Issuer**: The `<Issuer>` element **MUST** contain a unique identifier. Comparisons **MUST** use Simple String Comparison (RFC 3986 Section 6.2.1) unless otherwise specified.
2. **Audience**: The Assertion **MUST** contain a `<Conditions>` element with an `<AudienceRestriction>` containing an `<Audience>` that identifies the authorization server. The token endpoint URL **MAY** be used. The authorization server **MUST** reject any Assertion that does not contain its own identity as intended audience. Comparisons **MUST** use Simple String Comparison unless otherwise specified. Audience strings must be configured out of band.
3. **Subject**: The `<Subject>` element **MUST** identify the principal.
   - A. For authorization grant: typically identifies the resource owner or delegate; may be pseudonymous.
   - B. For client authentication: **MUST** be the `client_id` of the OAuth client.
4. **Expiry**: The Assertion **MUST** have an expiry via `NotOnOrAfter` attribute of `<Conditions>` or `<SubjectConfirmationData>`.
5. **SubjectConfirmation**: The `<Subject>` **MUST** contain at least one `<SubjectConfirmation>` with `Method="urn:oasis:names:tc:SAML:2.0:cm:bearer"`. If no `<Conditions>` expiry, then `<SubjectConfirmationData>` **MUST** be present, with `Recipient` indicating the token endpoint URL and a `NotOnOrAfter` attribute. **MAY** contain `Address` attribute.
6. **Replay protection**: The authorization server **MUST** reject Assertions with expired `NotOnOrAfter` on `<Conditions>` (subject to clock skew). **MUST** reject the `<SubjectConfirmation>` if its `NotOnOrAfter` has passed. **MAY** reject unreasonably far future expiries and **MAY** ensure no replay by maintaining used ID values.
7. **AuthnStatement**: If the issuer directly authenticated the subject, a single `<AuthnStatement>` **SHOULD** be included. If the client acts autonomously, `<AuthnStatement>` **SHOULD NOT** be included and the client **SHOULD** be identified in `<NameID>` or similar.
8. **Other statements**: `<AttributeStatement>` **MAY** be included.
9. **Signature/MAC**: The Assertion **MUST** be digitally signed or have a MAC. The authorization server **MUST** reject invalid signatures/MACs.
10. **Encryption**: Encrypted elements **MAY** appear.
11. **General validity**: The authorization server **MUST** reject Assertions not valid per [OASIS.saml-core-2.0-os].

### 3.1. Authorization Grant Processing
- Client authentication is optional; if present, the authorization server **MUST** validate credentials.
- If invalid: error response with `"error":"invalid_grant"`; **MAY** include `error_description` or `error_uri`.
- Example error:
  ```json
  {
    "error":"invalid_grant",
    "error_description":"Audience validation failed"
  }
  ```

### 3.2. Client Authentication Processing
- If invalid: error response with `"error":"invalid_client"`; **MAY** include `error_description` or `error_uri`.

## 4. Authorization Grant Example
- Provided as a conceptual example (whitespace formatted for display). Includes an Assertion issued by `https://saml-idp.example.com`, subject `brian@example.com`, audience `https://saml-sp.example.net`, with Bearer subject confirmation, digital signature, and AuthnStatement using X.509 authentication. The corresponding access token request example is shown.

## 5. Interoperability Considerations
- Agreement required on: Issuer and Audience identifiers, token endpoint location, digital signature key, one-time use restrictions, maximum Assertion lifetime, Subject and attribute requirements. Metadata exchange is out of scope; SAML Metadata [OASIS.saml-metadata-2.0-os] is a common method.
- The RSA-SHA256 algorithm (RFC 6931) is **mandatory-to-implement** for XML signatures.

## 6. Security Considerations
- Applicable security considerations from [RFC7521], [RFC6749], [OASIS.saml-sec-consider-2.0-os].
- Replay protection is optional; implementations may employ at their discretion.

## 7. Privacy Considerations
- SAML Assertions may contain sensitive information; should be transmitted over TLS. Subject and attributes may be encrypted to the authorization server to prevent disclosure to the client.
- Deployments should minimize included information; anonymous/pseudonymous Subject values are possible.

## 8. IANA Considerations
### 8.1. Registration of `urn:ietf:params:oauth:grant-type:saml2-bearer`
- URN: `urn:ietf:params:oauth:grant-type:saml2-bearer`
- Common Name: SAML 2.0 Bearer Assertion Grant Type Profile for OAuth 2.0
- Change Controller: IESG
- Specification Document: RFC 7522

### 8.2. Registration of `urn:ietf:params:oauth:client-assertion-type:saml2-bearer`
- URN: `urn:ietf:params:oauth:client-assertion-type:saml2-bearer`
- Common Name: SAML 2.0 Bearer Assertion Profile for OAuth 2.0 Client Authentication
- Change Controller: IESG
- Specification Document: RFC 7522

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Assertion `Issuer` MUST contain unique identifier; comparisons per Simple String Comparison | MUST | Section 3 item 1 |
| R2 | Assertion MUST contain `<AudienceRestriction>` with authorization server as intended audience; MUST reject if not | MUST | Section 3 item 2 |
| R3 | Assertion MUST contain `<Subject>` element | MUST | Section 3 item 3 |
| R4 | For client authentication, Subject MUST be the `client_id` | MUST | Section 3 item 3B |
| R5 | Assertion MUST have expiry via `NotOnOrAfter` | MUST | Section 3 item 4 |
| R6 | SubjectConfirmation method MUST be `urn:oasis:names:tc:SAML:2.0:cm:bearer` | MUST | Section 3 item 5 |
| R7 | SubjectConfirmationData Recipient MUST match token endpoint URL | MUST | Section 3 item 5 |
| R8 | Authorization server MUST reject expired Assertions (subject to clock skew) | MUST | Section 3 item 6 |
| R9 | Assertion MUST be digitally signed or MACed | MUST | Section 3 item 9 |
| R10 | Authorization server MUST reject invalid signature/MAC | MUST | Section 3 item 9 |
| R11 | Token request uses grant_type `urn:ietf:params:oauth:grant-type:saml2-bearer` | MUST | Section 2.1 |
| R12 | Client authentication uses client_assertion_type `urn:ietf:params:oauth:client-assertion-type:saml2-bearer` | MUST | Section 2.2 |
| R13 | SAML Assertion XML MUST be base64url encoded without line wraps or padding | MUST | Sections 2.1, 2.2 |
| R14 | RSA-SHA256 is mandatory-to-implement XML signature algorithm | MUST | Section 5 |
| R15 | Authorization grant error: `invalid_grant` when assertion invalid | MUST | Section 3.1 |
| R16 | Client authentication error: `invalid_client` when assertion invalid | MUST | Section 3.2 |