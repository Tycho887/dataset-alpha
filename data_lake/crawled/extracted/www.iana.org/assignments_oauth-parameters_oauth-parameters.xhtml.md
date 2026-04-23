---
{
  "title": "OAuth Parameters",
  "url": "https://www.iana.org/assignments/oauth-parameters/oauth-parameters.xhtml",
  "domain": "www.iana.org",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 58360,
  "crawled_at": "2026-04-23T20:48:44"
}
---

OAuth Parameters
Created
2012-07-27
Last Updated
2026-03-25
Available Formats
XML
HTML
Plain text
Registries Included Below
OAuth Access Token Types
OAuth Authorization Endpoint Response Types
OAuth Extensions Error Registry
OAuth Parameters
OAuth Token Type Hints
OAuth URI
OAuth Dynamic Client Registration Metadata
OAuth Token Endpoint Authentication Methods
PKCE Code Challenge Methods
OAuth Token Introspection Response
OAuth Authorization Server Metadata
OAuth Protected Resource Metadata
OAuth Access Token Types
Registration Procedure(s)
Specification Required
Expert(s)
Hannes Tschofenig, Mike Jones
Reference
[
RFC6749
][
RFC8414
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC6749
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Name
Additional Token Endpoint Response Parameters
HTTP Authentication Scheme(s)
Change Controller
Reference
Bearer
Bearer
IETF
[
RFC6750
]
N_A
IESG
[
RFC8693, Section 2.2.1
]
PoP
cnf, rs_cnf (see section 3.1 of [
RFC8747
] 
        and section 3.2 of [
RFC9201
]).
N/A
IETF
[
RFC9200
]
DPoP
DPoP
IETF
[
RFC9449
]
OAuth Authorization Endpoint Response Types
Registration Procedure(s)
Specification Required
Expert(s)
Hannes Tschofenig, Mike Jones
Reference
[
RFC6749
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC6749
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Name
Change Controller
Reference
code
IETF
[
RFC6749
]
code id_token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
code id_token token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
code token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
id_token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
id_token token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
none
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
token
IETF
[
RFC6749
]
vp_token
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8
]
vp_token id_token
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8
]
OAuth Extensions Error Registry
Registration Procedure(s)
Specification Required
Expert(s)
Hannes Tschofenig, Mike Jones
Reference
[
RFC6749
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC6749
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Name
Usage Location
Protocol Extension
Change Controller
Reference
invalid_request
authorization endpoint, token endpoint, resource access error response
OAuth 2.0 Authorization Framework, bearer access token type
IETF
[
RFC6749
][
RFC6750
]
unauthorized_client
authorization endpoint, token endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
access_denied
authorization endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
unsupported_response_type
authorization endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
invalid_scope
authorization endpoint, token endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
server_error
authorization endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
temporarily_unavailable
authorization endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
invalid_client
token endpoint, authorization endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
invalid_grant
token endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
unsupported_grant_type
token endpoint
OAuth 2.0 Authorization Framework
IETF
[
RFC6749
]
invalid_token
resource access error response
bearer access token type
IETF
[
RFC6750
]
insufficient_scope
resource access error response
bearer access token type
IETF
[
RFC6750
]
unsupported_token_type
revocation endpoint error response
token revocation endpoint
IETF
[
RFC7009
]
interaction_required
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
login_required
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
account_selection_required
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
consent_required
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
invalid_request_uri
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
invalid_request_object
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
request_not_supported
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
request_uri_not_supported
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
registration_not_supported
authorization endpoint
OpenID Connect
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
need_info (and its subsidiary parameters)
authorization server response, token endpoint
Kantara UMA
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.6
]
request_denied
authorization server response, token endpoint
Kantara UMA
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.6
]
request_submitted (and its subsidiary parameters)
authorization server response, token endpoint
Kantara UMA
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.6
]
invalid_redirect_uri
registration endpoint
Dynamic Client Registration
IETF
[
RFC7591, Section 3.2.2
]
invalid_client_metadata
registration endpoint
Dynamic Client Registration
IETF
[
RFC7591, Section 3.2.2
]
invalid_software_statement
registration endpoint
Dynamic Client Registration
IETF
[
RFC7591, Section 3.2.2
]
unapproved_software_statement
registration endpoint
Dynamic Client Registration
IETF
[
RFC7591, Section 3.2.2
]
authorization_pending
Token endpoint response
[
RFC8628
]
IETF
[
RFC8628, Section 3.5
]
access_denied
Token endpoint response
[
RFC8628
]
IETF
[
RFC8628, Section 3.5
]
slow_down
Token endpoint response
[
RFC8628
]
IETF
[
RFC8628, Section 3.5
]
expired_token
Token endpoint response
[
RFC8628
]
IETF
[
RFC8628, Section 3.5
]
invalid_target
implicit grant error response, token error response
resource parameter
IESG
[
RFC8707
]
unsupported_pop_key
token error response
[
RFC9200
]
IETF
[
RFC9200, Section 5.8.3
]
incompatible_ace_profiles
token error response
[
RFC9200
]
IETF
[
RFC9200, Section 5.8.3
]
invalid_authorization_details
token endpoint, authorization endpoint
OAuth 2.0 Rich Authorization Requests
IETF
[
RFC9396, Section 5
]
invalid_dpop_proof
token error response, resource access error response
Demonstrating Proof of Possession (DPoP)
IETF
[
RFC9449
]
use_dpop_nonce
token error response, resource access error response
Demonstrating Proof of Possession (DPoP)
IETF
[
RFC9449
]
insufficient_user_authentication
resource access error response
OAuth 2.0 Step Up Authentication Challenge Protocol
IETF
[
RFC9470, Section 3
]
invalid_issuer
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
invalid_subject
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
invalid_trust_anchor
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
invalid_trust_chain
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
invalid_metadata
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
not_found
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
unsupported_parameter
authorization endpoint
OpenID Federation
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 8.9 of OpenID Federation 1.0
]
vp_formats_not_supported
authorization endpoint, token endpoint
OpenID for Verifiable Presentations
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8.5
]
invalid_request_uri_method
authorization endpoint
OpenID for Verifiable Presentations
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8.5
]
wallet_unavailable
authorization endpoint, token endpoint
OpenID for Verifiable Presentations
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8.5
]
OAuth Parameters
Registration Procedure(s)
Specification Required
Expert(s)
Hannes Tschofenig, Mike Jones
Reference
[
RFC6749
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC6749
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Name
Parameter Usage Location
Change Controller
Reference
client_id
authorization request, token request
IETF
[
RFC6749
]
client_secret
token request
IETF
[
RFC6749
]
response_type
authorization request
IETF
[
RFC6749
]
redirect_uri
authorization request, token request
IETF
[
RFC6749
]
scope
authorization request, authorization response, token request, token response
IETF
[
RFC6749
]
state
authorization request, authorization response
IETF
[
RFC6749
]
code
authorization response, token request
IETF
[
RFC6749
]
error
authorization response, token response
IETF
[
RFC6749
]
error_description
authorization response, token response
IETF
[
RFC6749
]
error_uri
authorization response, token response
IETF
[
RFC6749
]
grant_type
token request
IETF
[
RFC6749
]
access_token
authorization response, token response
IETF
[
RFC6749
]
token_type
authorization response, token response
IETF
[
RFC6749
]
expires_in
authorization response, token response
IETF
[
RFC6749
]
username
token request
IETF
[
RFC6749
]
password
token request
IETF
[
RFC6749
]
refresh_token
token request, token response
IETF
[
RFC6749
]
nonce
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
display
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
prompt
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
max_age
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
ui_locales
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
claims_locales
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
id_token_hint
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
login_hint
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
acr_values
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
claims
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
registration
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
request
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
request_uri
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
id_token
authorization response, access token response
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
session_state
authorization response, access token response
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Session Management 1.0, Section 2
]
assertion
token request
IESG
[
RFC7521
]
client_assertion
token request
IESG
[
RFC7521
]
client_assertion_type
token request
IESG
[
RFC7521
]
code_verifier
token request
IESG
[
RFC7636
]
code_challenge
authorization request
IESG
[
RFC7636
]
code_challenge_method
authorization request
IESG
[
RFC7636
]
claim_token
client request, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.1
]
pct
client request, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.1
]
pct
authorization server response, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.5
]
rpt
client request, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.1
]
ticket
client request, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.1
]
upgraded
authorization server response, token endpoint
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.3.5
]
vtr
authorization request, token request
IESG
[
RFC8485
]
device_code
token request
IESG
[
RFC8628, Section 3.1
]
resource
authorization request, token request
IESG
[
RFC8707
]
audience
token request
IESG
[
RFC8693, Section 2.1
]
requested_token_type
token request
IESG
[
RFC8693, Section 2.1
]
subject_token
token request
IESG
[
RFC8693, Section 2.1
]
subject_token_type
token request
IESG
[
RFC8693, Section 2.1
]
actor_token
token request
IESG
[
RFC8693, Section 2.1
]
actor_token_type
token request
IESG
[
RFC8693, Section 2.1
]
issued_token_type
token response
IESG
[
RFC8693, Section 2.2.1
]
response_mode
Authorization Request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OAuth 2.0 Multiple Response Type Encoding Practices
]
nfv_token
Access Token Response
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
iss
authorization request, authorization response
IETF
[
RFC9207, Section 2
][
RFC9101
][
RFC7519, Section 4.1.1
]
sub
authorization request
IETF
[
RFC7519, Section 4.1.2
][
RFC9101
]
aud
authorization request
IETF
[
RFC7519, Section 4.1.3
][
RFC9101
]
exp
authorization request
IETF
[
RFC7519, Section 4.1.4
][
RFC9101
]
nbf
authorization request
IETF
[
RFC7519, Section 4.1.5
][
RFC9101
]
iat
authorization request
IETF
[
RFC7519, Section 4.1.6
][
RFC9101
]
jti
authorization request
IETF
[
RFC7519, Section 4.1.7
][
RFC9101
]
ace_profile
token response
IETF
[
RFC9200, Sections 5.8.2, 5.8.4.3
]
nonce1
client-rs request
IETF
[
RFC9203
]
nonce2
rs-client response
IETF
[
RFC9203
]
ace_client_recipientid
client-rs request
IETF
[
RFC9203
]
ace_server_recipientid
rs-client response
IETF
[
RFC9203
]
req_cnf
token request
IETF
[
RFC9201, Section 5
]
rs_cnf
token response
IETF
[
RFC9201, Section 5
]
cnf
token response
IETF
[
RFC9201, Section 5
]
authorization_details
authorization request, token request, token response
IETF
[
RFC9396
]
dpop_jkt
authorization request
IETF
[
RFC9449, Section 10
]
sign_info
client-rs request, rs-client response
IETF
[
RFC9594
]
kdcchallenge
rs-client response
IETF
[
RFC9594
]
trust_chain
authorization request
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 12.1.1.1.1 of OpenID Federation 1.0
]
dcql_query
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.1
]
client_metadata
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.1
]
request_uri_method
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.1
]
transaction_data
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.1
]
wallet_nonce
authorization request, token response
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.10
]
response_uri
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8.2
]
vp_token
authorization request, token response
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 8.1
]
verifier_info
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Section 5.1
]
expected_origins
authorization request
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
OpenID for Verifiable Presentations 1.0, Appendix A.2
]
ecdh_info
client-rs request, rs-client response
IETF
[
RFC-ietf-ace-key-groupcomm-oscore-21
]
kdc_dh_creds
client-rs request, rs-client response
IETF
[
RFC-ietf-ace-key-groupcomm-oscore-21
]
OAuth Token Type Hints
Registration Procedure(s)
Specification Required
Expert(s)
Torsten Lodderstedt, Mike Jones
Reference
[
RFC7009
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC7009
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Hint Value
Change Controller
Reference
access_token
IETF
[
RFC7009
]
refresh_token
IETF
[
RFC7009
]
pct
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 3.7
]
OAuth URI
Registration Procedure(s)
Specification Required
Expert(s)
Hannes Tschofenig, Mike Jones
Reference
[
RFC6755
]
Note
Prefix: urn:ietf:params:oauth
Available Formats
CSV
URN
Common Name
Change Controller
Reference
urn:ietf:params:oauth:grant-type:jwt-bearer
JWT Bearer Token Grant Type Profile for OAuth 2.0
IESG
[
RFC7523
]
urn:ietf:params:oauth:client-assertion-type:jwt-bearer
JWT Bearer Token Profile for OAuth 2.0 Client Authentication
IESG
[
RFC7523
]
urn:ietf:params:oauth:grant-type:saml2-bearer
SAML 2.0 Bearer Assertion Grant Type Profile for OAuth 2.0
IESG
[
RFC7522
]
urn:ietf:params:oauth:client-assertion-type:saml2-bearer
SAML 2.0 Bearer Assertion Profile for OAuth 2.0 Client Authentication
IESG
[
RFC7522
]
urn:ietf:params:oauth:token-type:jwt
JSON Web Token (JWT) Token Type
IESG
[
RFC7519
]
urn:ietf:params:oauth:grant-type:device_code
Device flow grant type for OAuth 2.0
IESG
[
RFC8628, Section 3.1
]
urn:ietf:params:oauth:grant-type:token-exchange
Token exchange grant type for OAuth 2.0
IESG
[
RFC8693, Section 2.1
]
urn:ietf:params:oauth:token-type:access_token
Token type URI for an OAuth 2.0 access token
IESG
[
RFC8693, Section 3
]
urn:ietf:params:oauth:token-type:refresh_token
Token type URI for an OAuth 2.0 refresh token
IESG
[
RFC8693, Section 3
]
urn:ietf:params:oauth:token-type:id_token
Token type URI for an ID Token
IESG
[
RFC8693, Section 3
]
urn:ietf:params:oauth:token-type:saml1
Token type URI for a base64url-encoded SAML 1.1 assertion
IESG
[
RFC8693, Section 3
]
urn:ietf:params:oauth:token-type:saml2
Token type URI for a base64url-encoded SAML 2.0 assertion
IESG
[
RFC8693, Section 3
]
urn:ietf:params:oauth:request_uri
A URN Sub-Namespace for OAuth Request URIs.
IESG
[
RFC9126, Section 2.2
]
urn:ietf:params:oauth:jwk-thumbprint
JWK Thumbprint URI
IESG
[
RFC9278
]
urn:ietf:params:oauth:ckt
COSE Key Thumbprint URI
IETF
[
RFC9679
]
OAuth Dynamic Client Registration Metadata
Registration Procedure(s)
Specification Required
Expert(s)
Justin Richer
Reference
[
RFC7591
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC7591
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Client Metadata Name
Client Metadata Description
Change Controller
Reference
redirect_uris
Array of redirection URIs for use in redirect-based flows
IESG
[
RFC7591
]
token_endpoint_auth_method
Requested authentication method for the token endpoint
IESG
[
RFC7591
]
grant_types
Array of OAuth 2.0 grant types that the client may use
IESG
[
RFC7591
]
response_types
Array of the OAuth 2.0 response types that the client may use
IESG
[
RFC7591
]
client_name
Human-readable name of the client to be presented to the user
IESG
[
RFC7591
]
client_uri
URL of a web page providing information about the client
IESG
[
RFC7591
]
logo_uri
URL that references a logo for the client
IESG
[
RFC7591
]
scope
Space-separated list of OAuth 2.0 scope values
IESG
[
RFC7591
]
contacts
Array of strings representing ways to contact people 
        responsible for this client, typically email addresses
IESG
[
RFC7591
]
tos_uri
URL that points to a human-readable terms of service document 
        for the client
IESG
[
RFC7591
]
policy_uri
URL that points to a human-readable policy document for the 
        client
IESG
[
RFC7591
]
jwks_uri
URL referencing the client's JSON Web Key Set [
RFC7517
] 
        document representing the client's public keys
IESG
[
RFC7591
]
jwks
Client's JSON Web Key Set [
RFC7517
] 
        document representing the client's public keys
IESG
[
RFC7591
]
software_id
Identifier for the software that comprises a client
IESG
[
RFC7591
]
software_version
Version identifier for the software that comprises a client
IESG
[
RFC7591
]
client_id
Client identifier
IESG
[
RFC7591
]
client_secret
Client secret
IESG
[
RFC7591
]
client_id_issued_at
Time at which the client identifier was issued
IESG
[
RFC7591
]
client_secret_expires_at
Time at which the client secret will expire
IESG
[
RFC7591
]
registration_access_token
OAuth 2.0 Bearer Token used to access
      the client configuration endpoint
IESG
[
RFC7592
]
registration_client_uri
Fully qualified URI of the client
      registration endpoint
IESG
[
RFC7592
]
application_type
Kind of the application -- "native" or "web"
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
sector_identifier_uri
URL using the https scheme to be used in calculating 
        Pseudonymous Identifiers by the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
subject_type
subject_type requested for responses to this Client -- 
        "pairwise" or "public"
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
id_token_signed_response_alg
JWS alg algorithm REQUIRED for signing the ID Token issued 
        to this Client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
id_token_encrypted_response_alg
JWE alg algorithm REQUIRED for encrypting the ID Token 
        issued to this Client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
id_token_encrypted_response_enc
JWE enc algorithm REQUIRED for encrypting the ID Token 
        issued to this Client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
userinfo_signed_response_alg
JWS alg algorithm REQUIRED for signing UserInfo Responses
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
userinfo_encrypted_response_alg
JWE alg algorithm REQUIRED for encrypting UserInfo Responses
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
userinfo_encrypted_response_enc
JWE enc algorithm REQUIRED for encrypting UserInfo Responses
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
request_object_signing_alg
JWS alg algorithm that MUST be used for signing Request 
        Objects sent to the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
request_object_encryption_alg
JWE alg algorithm the RP is declaring that it may use for 
        encrypting Request Objects sent to the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
request_object_encryption_enc
JWE enc algorithm the RP is declaring that it may use for 
        encrypting Request Objects sent to the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
token_endpoint_auth_signing_alg
JWS alg algorithm that MUST be used for signing the JWT 
        used to authenticate the Client at the Token Endpoint for the 
        private_key_jwt and client_secret_jwt authentication methods
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
default_max_age
Default Maximum Authentication Age
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
require_auth_time
Boolean value specifying whether the auth_time Claim in the 
        ID Token is REQUIRED
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
default_acr_values
Default requested Authentication Context Class Reference values
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
initiate_login_uri
URI using the https scheme that a third party can use to 
        initiate a login by the RP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
request_uris
Array of request_uri values that are pre-registered by the 
        RP for use at the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Dynamic Client Registration 1.0 incorporating errata set 2
]
claims_redirect_uris
claims redirection endpoints
[
Kantara_UMA_WG
]
[
UMA 2.0 Grant for OAuth 2.0, Section 2
]
nfv_token_signed_response_alg
JWS alg algorithm required for signing the nfv Token issued to this Client
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
nfv_token_encrypted_response_alg
JWE alg algorithm required for encrypting the nfv Token issued to this Client
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
nfv_token_encrypted_response_enc
JWE enc algorithm required for encrypting the nfv Token issued to this Client
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
tls_client_certificate_bound_access_tokens
Indicates the client's intention to
        use mutual-TLS client certificate-bound access tokens.
[
IESG
]
[
RFC8705, Section 3.4
]
tls_client_auth_subject_dn
String value specifying the expected
        subject DN of the client certificate.
[
IESG
]
[
RFC8705, Section 2.1.2
]
tls_client_auth_san_dns
String value specifying the expected
        dNSName SAN entry in the client certificate.
[
IESG
]
[
RFC8705, Section 2.1.2
]
tls_client_auth_san_uri
String value specifying the expected
        uniformResourceIdentifier SAN entry in the client certificate.
[
IESG
]
[
RFC8705, Section 2.1.2
]
tls_client_auth_san_ip
String value specifying the expected
        iPAddress SAN entry in the client certificate.
[
IESG
]
[
RFC8705, Section 2.1.2
]
tls_client_auth_san_email
String value specifying the expected
        rfc822Name SAN entry in the client certificate.
[
IESG
]
[
RFC8705, Section 2.1.2
]
require_signed_request_object
Indicates where authorization request needs
        to be protected as Request Object and provided through either
        request or request_uri parameter.
[
IETF
]
[
RFC9101, Section 10.5
]
require_pushed_authorization_requests
Indicates whether the client is required to use PAR to initiate authorization requests.
[
IESG
]
[
RFC9126, Section 6
]
introspection_signed_response_alg
String value indicating the client’s
desired introspection response signing algorithm
[
IETF
]
[
RFC9701, Section 6
]
introspection_encrypted_response_alg
String value specifying the desired
introspection response content key encryption algorithm (alg
value)
[
IETF
]
[
RFC9701, Section 6
]
introspection_encrypted_response_enc
String value specifying the desired
introspection response content encryption algorithm (enc value)
[
IETF
]
[
RFC9701, Section 6
]
frontchannel_logout_uri
RP URL that will cause the RP to log itself out when 
        rendered in an iframe by the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Front-Channel Logout 1.0, Section 2
]
frontchannel_logout_session_required
Boolean value specifying whether the RP requires that 
        a sid (session ID) query parameter be included to identify the RP 
        session with the OP when the frontchannel_logout_uri is used
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Front-Channel Logout 1.0, Section 2
]
backchannel_logout_uri
RP URL that will cause the RP to log itself out when 
        sent a Logout Token by the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Back-Channel Logout 1.0, Section 2.2
]
backchannel_logout_session_required
Boolean value specifying whether the RP requires that a sid 
        (session ID) Claim be included in the Logout Token to identify the RP 
        session with the OP when the backchannel_logout_uri is used
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Back-Channel Logout 1.0, Section 2.2
]
post_logout_redirect_uris
Array of URLs supplied by the RP to which it MAY request that 
        the End-User's User Agent be redirected using the post_logout_redirect_uri 
        parameter after a logout has been performed
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect RP-Initiated Logout 1.0, Section 3.1
]
authorization_details_types
Indicates what authorization details types the client uses.
[
IETF
]
[
RFC9396, Section 10
]
dpop_bound_access_tokens
Boolean value specifying whether the client always uses DPoP for token requests
[
IETF
]
[
RFC9449, Section 5.2
]
client_registration_types
An array of strings specifying the client registration types the RP wants to use
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.1.2 of OpenID Federation 1.0
]
signed_jwks_uri
URL referencing a signed JWT having the client's JWK Set document as its payload
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.1 of OpenID Federation 1.0
]
organization_name
Human-readable name representing the organization owning this client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
description
Human-readable brief description of this client presentable to the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
keywords
JSON array with one or more strings representing search keywords, tags, categories, or labels that apply to this client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
information_uri
URL for documentation of additional information about this client viewable by the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
organization_uri
URL of a Web page for the organization owning this client
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
use_mtls_endpoint_aliases
Boolean value indicating the requirement for a client
to use mutual-TLS endpoint aliases [
RFC8705
] declared by the authorization 
server in its metadata even beyond the Mutual-TLS Client Authentication and 
Certificate-Bound Access Tokens use cases.
[
OpenID_Foundation_FAPI_WG
]
[
Section 5.2.2.1.1 of FAPI 2.0 Security Profile
]
encrypted_response_enc_values_supported
Non-empty array of strings, where each string is a JWE [
RFC7516
] enc algorithm that can be used as the content encryption algorithm for encrypting the Response
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
Section 5.1 of OpenID for Verifiable Presentations 1.0
]
vp_formats_supported
An object containing a list of name/value pairs, where the name is a string identifying a Credential format supported by the Verifier
[
OpenID_Foundation_Digital_Credentials_Protocols_WG
]
[
Section 11.1 of OpenID for Verifiable Presentations 1.0
]
OAuth Token Endpoint Authentication Methods
Registration Procedure(s)
Specification Required
Expert(s)
Justin Richer
Reference
[
RFC7591
][
RFC8414
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC7591
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Token Endpoint Authentication Method Name
Change Controller
Reference
none
IESG
[
RFC7591
]
client_secret_post
IESG
[
RFC7591
]
client_secret_basic
IESG
[
RFC7591
]
client_secret_jwt
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
private_key_jwt
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Core 1.0 incorporating errata set 1
]
tls_client_auth
IESG
[
RFC8705, Section 2.1.1
]
self_signed_tls_client_auth
IESG
[
RFC8705, Section 2.2.1
]
PKCE Code Challenge Methods
Registration Procedure(s)
Specification Required
Expert(s)
John Bradley, Mike Jones
Reference
[
RFC7636
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC7636
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Code Challenge Method Parameter Name
Change Controller
Reference
plain
IESG
[
Section 4.2 of RFC7636
]
S256
IESG
[
Section 4.2 of RFC7636
]
OAuth Token Introspection Response
Registration Procedure(s)
Specification Required
Expert(s)
Justin Richer
Reference
[
RFC7662
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC7662
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Name
Description
Change Controller
Reference
active
Token active status
IESG
[
RFC7662, Section 2.2
]
username
User identifier of the resource owner
IESG
[
RFC7662, Section 2.2
]
client_id
Client identifier of the client
IESG
[
RFC7662, Section 2.2
]
scope
Authorized scopes of the token
IESG
[
RFC7662, Section 2.2
]
token_type
Type of the token
IESG
[
RFC7662, Section 2.2
]
exp
Expiration timestamp of the token
IESG
[
RFC7662, Section 2.2
]
iat
Issuance timestamp of the token
IESG
[
RFC7662, Section 2.2
]
nbf
Timestamp which the token is not valid before
IESG
[
RFC7662, Section 2.2
]
sub
Subject of the token
IESG
[
RFC7662, Section 2.2
]
aud
Audience of the token
IESG
[
RFC7662, Section 2.2
]
iss
Issuer of the token
IESG
[
RFC7662, Section 2.2
]
jti
Unique identifier of the token
IESG
[
RFC7662, Section 2.2
]
permissions
array of objects, each describing a scoped, time-limitable permission for a resource
[
Kantara_UMA_WG
]
[
Federated Authorization for UMA 2.0, Section 5.1.1
]
vot
Vector of Trust value
IESG
[
RFC8485
]
vtm
Vector of Trust trustmark URL
IESG
[
RFC8485
]
act
Actor
IESG
[
RFC8693, Section 4.1
]
may_act
Authorized Actor - the party that is authorized
        to become the actor
IESG
[
RFC8693, Section 4.4
]
cnf
Confirmation
IESG
[
RFC7800
][
RFC8705
]
ace_profile
The ACE profile used between the client and RS.
IETF
[
RFC9200, Section 5.9.2
]
cnonce
"client-nonce".  A nonce previously provided to the
        AS by the RS via the client.  Used to verify token freshness when
        the RS cannot synchronize its clock with the AS.
IETF
[
RFC9200, Section 5.9.2
]
cti
"CWT ID".  The identifier of a CWT as defined in
        [
RFC8392
].
IETF
[
RFC9200, Section 5.9.2
]
exi
"Expires in". Lifetime of the token in seconds from 
        the time the RS first sees it. Used to implement a weaker form 
        of token expiration for devices that cannot synchronize their 
        internal clocks.
IETF
[
RFC9200, Section 5.9.2
]
authorization_details
The member authorization_details contains a JSON array 
        of JSON objects representing the rights of the access token. Each 
        JSON object contains the data to specify the authorization requirements 
        for a certain type of resource.
IETF
[
RFC9396, Section 9.2
]
acr
Authentication Context Class Reference
IETF
[
RFC9470, Section 6.2
]
auth_time
Time when the user authentication occurred
IETF
[
RFC9470, Section 6.2
]
OAuth Authorization Server Metadata
Registration Procedure(s)
Specification Required
Expert(s)
Mike Jones, Nat Sakimura, John Bradley, Dick Hardt
Reference
[
RFC8414
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC8414
]. If approved, designated experts should notify 
IANA within two weeks. For assistance, please contact iana@iana.org. 
IANA does not monitor the list.
Available Formats
CSV
Metadata Name
Metadata Description
Change Controller
Reference
issuer
Authorization server's issuer identifier URL
IESG
[
RFC8414, Section 2
]
authorization_endpoint
URL of the authorization server's authorization endpoint
IESG
[
RFC8414, Section 2
]
token_endpoint
URL of the authorization server's token endpoint
IESG
[
RFC8414, Section 2
]
jwks_uri
URL of the authorization server's JWK Set document
IESG
[
RFC8414, Section 2
]
registration_endpoint
URL of the authorization server's OAuth 2.0 Dynamic Client Registration Endpoint
IESG
[
RFC8414, Section 2
]
scopes_supported
JSON array containing a list of the OAuth 2.0 "scope" values that this authorization server supports
IESG
[
RFC8414, Section 2
]
response_types_supported
JSON array containing a list of the OAuth 2.0 "response_type" values that this authorization server supports
IESG
[
RFC8414, Section 2
]
response_modes_supported
JSON array containing a list of the OAuth 2.0 "response_mode" values that this authorization server supports
IESG
[
RFC8414, Section 2
]
grant_types_supported
JSON array containing a list of the OAuth 2.0 grant type values that this authorization server supports
IESG
[
RFC8414, Section 2
]
token_endpoint_auth_methods_supported
JSON array containing a list of client authentication methods supported by this token endpoint
IESG
[
RFC8414, Section 2
]
token_endpoint_auth_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms supported by the token endpoint for the
        signature on the JWT used to authenticate the client at the token endpoint
IESG
[
RFC8414, Section 2
]
service_documentation
URL of a page containing human-readable information that developers might want or need to know when using
        the authorization server
IESG
[
RFC8414, Section 2
]
ui_locales_supported
Languages and scripts supported for the user interface, represented as a 
        JSON array of language tag values from BCP 47 [
RFC5646
]
IESG
[
RFC8414, Section 2
]
op_policy_uri
URL that the authorization server provides to the person registering the client to read about the
        authorization server's requirements on how the client can use the data provided by the authorization server
IESG
[
RFC8414, Section 2
]
op_tos_uri
URL that the authorization server provides to the person registering the client to read about the
        authorization server's terms of service
IESG
[
RFC8414, Section 2
]
revocation_endpoint
URL of the authorization server's OAuth 2.0 revocation endpoint
IESG
[
RFC8414, Section 2
]
revocation_endpoint_auth_methods_supported
JSON array containing a list of client authentication methods supported by this revocation endpoint
IESG
[
RFC8414, Section 2
]
revocation_endpoint_auth_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms supported by the revocation endpoint
        for the signature on the JWT used to authenticate the client at the revocation endpoint
IESG
[
RFC8414, Section 2
]
introspection_endpoint
URL of the authorization server's OAuth 2.0 introspection endpoint
IESG
[
RFC8414, Section 2
]
introspection_endpoint_auth_methods_supported
JSON array containing a list of client authentication methods supported by this introspection endpoint
IESG
[
RFC8414, Section 2
]
introspection_endpoint_auth_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms supported by the introspection endpoint for the
        signature on the JWT used to authenticate the client at the introspection endpoint
IESG
[
RFC8414, Section 2
]
code_challenge_methods_supported
PKCE code challenge methods supported by this authorization server
IESG
[
RFC8414, Section 2
]
signed_metadata
Signed JWT containing metadata values about
        the authorization server as claims
IESG
[
RFC8414, Section 2.1
]
device_authorization_endpoint
URL of the authorization server's device authorization endpoint
IESG
[
RFC8628, Section 4
]
tls_client_certificate_bound_access_tokens
Indicates authorization server support for
        mutual-TLS client certificate-bound access tokens.
IESG
[
RFC8705, Section 3.3
]
mtls_endpoint_aliases
JSON object containing alternative
        authorization server endpoints, which a client intending to do
        mutual TLS will use in preference to the conventional endpoints.
IESG
[
RFC8705, Section 5
]
nfv_token_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms supported by the
        server for signing the JWT used as NFV Token
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
nfv_token_encryption_alg_values_supported
JSON array containing a list of the JWE encryption algorithms (alg values)
        supported by the server to encode the JWT used as NFV Token
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
nfv_token_encryption_enc_values_supported
JSON array containing a list of the JWE encryption algorithms (enc values)
        supported by the server to encode the JWT used as NFV Token
[
ETSI
]
[
ETSI GS NFV-SEC 022 V2.7.1
]
userinfo_endpoint
URL of the OP's UserInfo Endpoint
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
acr_values_supported
JSON array containing a list of the Authentication Context Class References that this OP supports
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
subject_types_supported
JSON array containing a list of the Subject Identifier types that this OP supports
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
id_token_signing_alg_values_supported
JSON array containing a list of the JWS "alg" values supported by the OP for the ID Token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
id_token_encryption_alg_values_supported
JSON array containing a list of the JWE "alg" values supported by the OP for the ID Token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
id_token_encryption_enc_values_supported
JSON array containing a list of the JWE "enc" values supported by the OP for the ID Token
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
userinfo_signing_alg_values_supported
JSON array containing a list of the JWS "alg" values supported by the UserInfo Endpoint
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
userinfo_encryption_alg_values_supported
JSON array containing a list of the JWE "alg" values supported by the UserInfo Endpoint
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
userinfo_encryption_enc_values_supported
JSON array containing a list of the JWE "enc" values supported by the UserInfo Endpoint
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
request_object_signing_alg_values_supported
JSON array containing a list of the JWS "alg" values supported by the OP for Request Objects
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
request_object_encryption_alg_values_supported
JSON array containing a list of the JWE "alg" values supported by the OP for Request Objects
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
request_object_encryption_enc_values_supported
JSON array containing a list of the JWE "enc" values supported by the OP for Request Objects
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
display_values_supported
JSON array containing a list of the "display" parameter values that the OpenID Provider supports
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
claim_types_supported
JSON array containing a list of the Claim Types that the OpenID Provider supports
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
claims_supported
JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
claims_locales_supported
Languages and scripts supported for values in Claims being returned, represented as a JSON array of BCP 47 [
RFC5646
] language tag values
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
claims_parameter_supported
Boolean value specifying whether the OP supports use of the "claims" parameter
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
request_parameter_supported
Boolean value specifying whether the OP supports use of the "request" parameter
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
request_uri_parameter_supported
Boolean value specifying whether the OP supports use of the "request_uri" parameter
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
require_request_uri_registration
Boolean value specifying whether the OP requires any "request_uri" values used to be pre-registered
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Discovery 1.0, Section 3
]
require_signed_request_object
Indicates where authorization request needs
        to be protected as Request Object and provided through either
        request or request_uri parameter.
IETF
[
RFC9101, Section 10.5
]
pushed_authorization_request_endpoint
URL of the authorization server's pushed
        authorization request endpoint
IESG
[
RFC9126, Section 5
]
require_pushed_authorization_requests
Indicates whether the authorization server
        accepts authorization requests only via PAR.
IESG
[
RFC9126, Section 5
]
introspection_signing_alg_values_supported
JSON array containing a list of algorithms supported by the authorization server for introspection response signing
IETF
[
RFC9701, Section 7
]
introspection_encryption_alg_values_supported
JSON array containing a list of algorithms
        supported by the authorization server for introspection response
        content key encryption (alg value)
IETF
[
RFC9701, Section 7
]
introspection_encryption_enc_values_supported
JSON array containing a list of algorithms
        supported by the authorization server for introspection response
        content encryption (enc value)
IETF
[
RFC9701, Section 7
]
authorization_response_iss_parameter_supported
Boolean value indicating whether the 
        authorization server provides the iss parameter in the 
        authorization response.
IETF
[
RFC9207, Section 3
]
check_session_iframe
URL of an OP iframe that supports cross-origin communications for session state information with the RP Client, using the HTML5 postMessage API
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Session Management 1.0, Section 3.3
]
frontchannel_logout_supported
Boolean value specifying whether the OP supports HTTP-based logout, with true indicating support
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Front-Channel Logout 1.0, Section 3
]
backchannel_logout_supported
Boolean value specifying whether the OP supports back-channel logout, with true indicating support
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Back-Channel Logout 1.0, Section 2
]
backchannel_logout_session_supported
Boolean value specifying whether the OP can pass a sid (session ID) Claim in the Logout Token to identify the RP session with the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect Back-Channel Logout 1.0, Section 2
]
end_session_endpoint
URL at the OP to which an RP can perform a redirect to request that the End-User be logged out at the OP
[
OpenID_Foundation_Artifact_Binding_WG
]
[
OpenID Connect RP-Initiated Logout 1.0, Section 2.1
]
backchannel_token_delivery_modes_supported
Supported CIBA authentication result delivery modes
[
OpenID_Foundation_MODRNA_WG
]
[
OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0, Section 4
]
backchannel_authentication_endpoint
CIBA Backchannel Authentication Endpoint
[
OpenID_Foundation_MODRNA_WG
]
[
OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0, Section 4
]
backchannel_authentication_request_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms supported for validation of signed CIBA authentication requests
[
OpenID_Foundation_MODRNA_WG
]
[
OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0, Section 4
]
backchannel_user_code_parameter_supported
Indicates whether the OP supports the use of the CIBA user_code parameter.
[
OpenID_Foundation_MODRNA_WG
]
[
OpenID Connect Client-Initiated Backchannel Authentication Flow - Core 1.0, Section 4
]
authorization_details_types_supported
JSON array containing the authorization details types the AS supports
IETF
[
RFC9396, Section 10
]
dpop_signing_alg_values_supported
JSON array containing a list of the JWS algorithms supported for DPoP proof JWTs
IETF
[
RFC9449, Section 5.1
]
client_registration_types_supported
Client Registration Types Supported
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.1.3 of OpenID Federation 1.0
]
federation_registration_endpoint
Federation Registration Endpoint
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.1.3 of OpenID Federation 1.0
]
signed_jwks_uri
URL referencing a signed JWT having this authorization server's JWK Set document as its payload
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.1 of OpenID Federation 1.0
]
jwks
JSON Web Key Set document, passed by value
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.1 of OpenID Federation 1.0
]
organization_name
Human-readable name representing the organization owning this authorization server
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
display_name
Human-readable name of the authorization server to be presented to the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
description
Human-readable brief description of this authorization server presentable to the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
keywords
JSON array with one or more strings representing search keywords, 
        tags, categories, or labels that apply to this authorization server
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
contacts
Array of strings representing ways to contact people responsible for this authorization server, typically email addresses
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
logo_uri
URL that references a logo for the organization owning this authorization server
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
information_uri
URL for documentation of additional information about this authorization server viewable by the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
organization_uri
URL of a Web page for the organization owning this authorization server
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
protected_resources
JSON array containing a list of resource identifiers for OAuth protected resources
IETF
[
RFC9728, Section 4
]
OAuth Protected Resource Metadata
Registration Procedure(s)
Specification Required
Expert(s)
Michael Jones, Dick Hardt
Reference
[
RFC9728
]
Note
Registration requests should be sent to [
oauth-ext-review@ietf.org
], as 
described in [
RFC9728
]. If approved, 
designated experts should notify IANA within two weeks. For 
assistance, please contact iana@iana.org. IANA does not monitor the 
list.
Available Formats
CSV
Metadata Name
Metadata Description
Change Controller
Reference
resource
Protected resource's resource identifier URL
IETF
[
RFC9728, Section 2
]
authorization_servers
JSON array containing a list of OAuth authorization server issuer identifiers
IETF
[
RFC9728, Section 2
]
jwks_uri
URL of the protected resource's JWK Set document
IETF
[
RFC9728, Section 2
]
scopes_supported
JSON array containing a list of the OAuth 2.0 scope values that are used in authorization requests to request access to this protected resource
IETF
[
RFC9728, Section 2
]
bearer_methods_supported
JSON array containing a list of the OAuth 2.0 bearer token presentation methods that this protected resource supports
IETF
[
RFC9728, Section 2
]
resource_signing_alg_values_supported
JSON array containing a list of the JWS signing algorithms (alg values) supported by the protected resource for signed content
IETF
[
RFC9728, Section 2
]
resource_name
Human-readable name of the protected resource
IETF
[
RFC9728, Section 2
]
resource_documentation
URL of a page containing human-readable information that developers might want or need to know when using the protected resource
IETF
[
RFC9728, Section 2
]
resource_policy_uri
URL of a page containing human-readable information about the protected resource's requirements on how the client can use the data provided by the protected resource
IETF
[
RFC9728, Section 2
]
resource_tos_uri
URL of a page containing human-readable information about the protected resource's terms of service
IETF
[
RFC9728, Section 2
]
tls_client_certificate_bound_access_tokens
Boolean value indicating protected resource support for mutual-TLS client certificate-bound access tokens
IETF
[
RFC9728, Section 2
]
authorization_details_types_supported
JSON array containing a list of the authorization details type values supported by the resource server when the authorization_details request parameter is used
IETF
[
RFC9728, Section 2
]
dpop_signing_alg_values_supported
JSON array containing a list of the JWS alg values supported by the resource server for validating DPoP proof JWTs
IETF
[
RFC9728, Section 2
]
dpop_bound_access_tokens_required
Boolean value specifying whether the protected resource always requires the use of DPoP-bound access tokens
IETF
[
RFC9728, Section 2
]
signed_metadata
Signed JWT containing metadata parameters about the protected resource as claims
IETF
[
RFC9728, Section 2.2
]
signed_jwks_uri
URL referencing a signed JWT having the protected resource's JWK Set document as its payload
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.1 of OpenID Federation 1.0
]
jwks
JSON Web Key Set document, passed by value
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.1 of OpenID Federation 1.0
]
organization_name
Human-readable name representing the organization owning this protected resource
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
description
Human-readable brief description of this protected resource presentable to the End-User
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
keywords
JSON array with one or more strings representing search keywords, tags, categories, 
        or labels that apply to this protected resource
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
contacts
Array of strings representing ways to contact people responsible for this 
        protected resource, typically email addresses
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
logo_uri
URL that references a logo for the organization owning this protected resource
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
organization_uri
URL of a Web page for the organization owning this protected resource
[
OpenID_Foundation_Artifact_Binding_WG
]
[
Section 5.2.2 of OpenID Federation 1.0
]
Contact Information
ID
Name
Contact URI
Last Updated
[ETSI]
ETSI
mailto:pnns&etsi.org
2019-07-22
[IESG]
Internet Engineering Steering Group
mailto:iesg&ietf.org
[IETF]
Internet Engineering Task Force
mailto:ietf&ietf.org
[Kantara_UMA_WG]
Kantara Initiative User-Managed Access Work Group
mailto:staff&kantarainitiative.org
2018-04-23
[OpenID_Foundation_Artifact_Binding_WG]
OpenID Foundation Artifact Binding Working Group
mailto:openid-specs-ab&lists.openid.net
2022-09-23
[OpenID_Foundation_Digital_Credentials_Protocols_WG]
OpenID Foundation Digital Credentials Protocols Working Group
mailto:openid-specs-digital-credentials-protocols&lists.openid.net
2025-10-03
[OpenID_Foundation_FAPI_WG]
OpenID Foundation FAPI Working Group
mailto:openid-specs-fapi&lists.openid.net
2025-04-28
[OpenID_Foundation_MODRNA_WG]
OpenID Foundation MODRNA Working Group
mailto:openid-specs-mobile-profile&lists.openid.net
2022-12-01