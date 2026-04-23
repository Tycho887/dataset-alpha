---
{
  "title": "OpenID Connect Protocol - Auth0 Docs",
  "url": "https://auth0.com/docs/protocols/oidc",
  "domain": "auth0.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2799,
  "crawled_at": "2026-04-23T20:52:15"
}
---

Auth0 Docs
home page
English
Search...
⌘
K
Ask AI
Search...
Navigation
Protocols
OpenID Connect Protocol
Home
Documentation
Quickstarts
API Reference
SDKs
Events Catalog
Authenticate
Auth0 simplifies the use of open industry standards
Authenticate
Add Login
Login
Single Sign-On
Passwordless
Custom Token Exchange
Provision Users
Identity Providers
Database Connections
Enterprise Connections
Protocols
Overview
SAML
OpenID Connect Protocol
OAuth 2.0 Authorization Framework
Web Services Federation Protocol
Lightweight Directory Access Protocol
System for Cross-domain Identity Management (SCIM)
Connection Settings Best Practices
On this page
What is OpenID Connect (OIDC)?
OpenID vs. OAuth2
OpenID and JWTs
Configure applications with OIDC and OAuth2
Learn more
​
What is OpenID Connect (OIDC)?
OpenID
Connect (OIDC) is an identity layer built on top of the
OAuth 2.0
framework. It allows third-party applications to verify the identity of the end-user and to obtain basic user profile information. OIDC uses
JSON web tokens
(JWTs), which you can obtain using flows conforming to the OAuth 2.0 specifications. See our
OIDC Handbook
for more details.
​
OpenID vs. OAuth2
While OAuth 2.0 is about resource access and sharing, OIDC is about user authentication. Its purpose is to give you one login for multiple sites. Each time you need to log in to a website using OIDC, you are redirected to your OpenID site where you log in, and then taken back to the website. For example, if you chose to sign in to Auth0 using your Google account then you used OIDC. Once you successfully authenticate with Google and authorize Auth0 to access your information, Google sends information back to Auth0 about the user and the authentication performed. This information is returned in a JWT. You’ll receive an
access token
and if requested, an
ID token
.
​
OpenID and JWTs
JWTs contain
claims
, which are statements (such as name or email address) about an entity (typically, the user) and additional metadata. The
OpenID Connect specification
defines a set of
standard claims
. The set of standard claims include name, email, gender, birth date, and so on. However, if you want to capture information about a user and there currently isn’t a standard claim that best reflects this piece of information, you can create custom claims and add them to your tokens.
​
Configure applications with OIDC and OAuth2
You can automatically
configure your applications with OIDC discovery
.
​
Learn more
Configure Applications with OIDC Discovery
Force Reauthentication in OIDC
Applications in Auth0
Single Sign-On
User Profiles
Was this page helpful?
Yes
No
Work with Certificates and Keys as Strings
Previous
OAuth 2.0 Authorization Framework
Next
⌘
I
Assistant
Responses are generated using AI and may contain mistakes.