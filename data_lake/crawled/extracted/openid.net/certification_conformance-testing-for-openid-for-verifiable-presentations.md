---
{
  "title": "How to Run Conformance Tests for OpenID for Verifiable Presentations - OpenID Foundation",
  "url": "https://openid.net/certification/conformance-testing-for-openid-for-verifiable-presentations",
  "domain": "openid.net",
  "depth": 2,
  "relevance_score": 0.58,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 6061,
  "crawled_at": "2026-04-23T20:47:38"
}
---

How to Run Conformance Tests for OpenID for Verifiable Presentations
OpenID Foundation is currently developing tests for checking that wallets and verifiers correctly & securely implement the OpenID for Verifiable Presentation specification (and, later, will create tests for
OpenID for Verifiable Credential Issuance).
We have tests for:
https://openid.net/specs/openid-4-verifiable-presentations-1_0.html
– 1.0 Final
https://openid.net/specs/openid-4-verifiable-presentations-1_0-ID2.html
(as used in ISO mDL 18013-7 annex b)
https://openid.net/specs/openid-4-verifiable-presentations-1_0-24.html
(which is the same as ID3, but with some additions/changes for mdoc, we recommend people use -24 instead of ID3)
Testing a wallet
These tests currently require support for:
response_type=vp_token
client_id_
scheme values
:
redirect_uri, or
pre_registered, or
x509_san_dns
response_mode values:
direct_post, or
direct_post.jwt (encrypted only)
dc_api
dc_api.jwt
Cross device (QR code based) or same device flow
authorization request methods:
unsigned request_uri, or
signed request_uri
credential formats:
SD-JWT VC with
HAIP
ISO mDocs over Browser API as per HAIP
ISO mDocs, including ISO
18013-7
mDL AnnexB – draft 3, 17th January 2024 – select ‘direct_post.jwt’, ‘request_uri_signed’ and ‘x509_san_dns’ options. The client jwks field
must
have a use: signing jwk with an x5c containing a certificate that includes SAN DNS:demo.certification.openid.net (the cert can be self signed) and a use: enc key.
presentation_definition or dcql_query
It is recommended to run VC tests on the ‘demo’ server (rather than the production one) as this contains the latest changes:
https://demo.certification.openid.net/
After logging in, select “Create a new test plan” and then select the test plan “OpenID for Verifiable Presentations ID2: Alpha tests (not currently part of certification program)” or the corresponding “ID3 + draft 24” entry.
An example configuration JSON for ISO mDL can be found here:
https://gitlab.com/openid/conformance-suite/-/wikis/OpenID-for-Verifiable-Presentations:-ISO-mDL-Example-Configuration
This can be pasted into the ‘JSON’ tab to pre-fill the form with example values. Each form field has a help field if you hover over the ‘?’ – for the client jwks refer to the above note when testing with mdl though. If the wallet will accept a self signed certificate for the x509_san_dns client authentication, the client jwks in the example configuration may be used as is.
When filling in the configuration form the fields all have help values available by hovering your mouse pointer over the ‘i’ button.
You must select an “alias” to use. This will form part of any urls hosted by the conformance suite and should be unique to yourself, for example your company name. (If you use the same alias as another user, yours tests may interfere with each other.)
Once you have created your test plan, you should run each test in the test plan. Please be sure to pay attention to the details/instructions in the blue box at the top of each test.
Please contact the certification team if you’d like some help, need different specification features to be supported or if anything goes wrong (or to let us know it went well – we are actively encouraging feedback on these tests!):
certification@oidf.org
Testing a verifier
The verifier tests currently require support for:
response_type=vp_token
client_id_
scheme values
:
x509_san_dns
response_mode values:
direct_post, or
direct_post.jwt (encrypted only)
Same device flow only
authorization request methods:
signed request_uri
credential formats:
SD-JWT VC with
HAIP – in particular the generated credential is currently hardcoded to match the “
urn:eudi:pid:1″
credential defined in
ARF 1.8
ISO mDocs
presentation_definition
These tests are under active development – extra options and additional tests (e.g. negative tests checking that credentials with bad key binding are rejected) will be added soon.
It is recommended to run VC tests on the ‘demo’ server (rather than the production one) as this contains the latest changes. The following link will open this server and preconfigure some values:
Preconfigured test plan
Please ensure you change the values marked with FIXMEs and check other values (spec version being tested etc) are correctly selected.
This link contains a JWK with an x5c entry containing a self-signed certificate that is used for signing credentials. You can use this as is, or replace it with a JWK of your own that your verifier will trust. The corresponding PEM certificate for that JWK is shown at the bottom of this page.
Once you have configured the tests, press ‘create test plan’ and then ‘Run Test’. The test will go into ‘WAITING’ status, indicating that it is waiting for the verifier to send the OpenID4VP request to the conformance suite’s ‘fake’ wallet.
When configuring your verifier, you must use the ‘authorization_endpoint’ url (shown in the ‘Exported Values’ section shown when you start running the test) instead of the ‘openid4vp://’ scheme you normally use to launch the wallet – in the same way a web-based wallet would be invoked. The ‘authorization_endpoint’ url value will be the same for all tests that use the same ‘alias’ value in the test configuration.
-----BEGIN CERTIFICATE-----
MIICHjCCAcOgAwIBAgIUZX9BS5CDOJRW2t1FK1UDMt/QwMEwCgYIKoZIzj0EAwIw
ITELMAkGA1UEBhMCR0IxEjAQBgNVBAMMCU9JREYgVGVzdDAeFw0yNDExMjUwODM2
MDRaFw0zNDExMjMwODM2MDRaMCExCzAJBgNVBAYTAkdCMRIwEAYDVQQDDAlPSURG
IFRlc3QwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAATT/dLsd51LLBrGV6R23o6v
ymRxHXeFBoI8yq31y5kFV2VV0gi9x5ZzEFiq8DMiAHucLACFndxLtZorCha9zznQ
o4HYMIHVMB0GA1UdDgQWBBS5cbdgAeMBi5wxpbpwISGhShAWETAfBgNVHSMEGDAW
gBS5cbdgAeMBi5wxpbpwISGhShAWETAPBgNVHRMBAf8EBTADAQH/MIGBBgNVHREE
ejB4ghB3d3cuaGVlbmFuLm1lLnVrgh1kZW1vLmNlcnRpZmljYXRpb24ub3Blbmlk
Lm5ldIIJbG9jYWxob3N0ghZsb2NhbGhvc3QuZW1vYml4LmNvLnVrgiJkZW1vLnBp
ZC1pc3N1ZXIuYnVuZGVzZHJ1Y2tlcmVpLmRlMAoGCCqGSM49BAMCA0kAMEYCIQCP
bnLxCI+WR1vhOW+A8KznAWv1MJo+YEb1MI45NKW/VQIhALzsqox8VuBRwN2dl5Lk
pnxP4oH9p6H0AOZmKP+Y7nXS
-----END CERTIFICATE-----