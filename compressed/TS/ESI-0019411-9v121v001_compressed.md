# ETSI Portal Login Page
**Source**: ETSI Portal | **Version**: N/A | **Date**: N/A | **Type**: Informative
**Original**: https://portal.etsi.org/LoginRedirection.aspx?domain=docbox.etsi.org&ReturnUrl=/esi/esi/70-Drafts/0019411-9v121/ESI-0019411-9v121v001.docx

## Scope
This page provides authentication for ETSI Portal users to access restricted resources (e.g., documents on docbox.etsi.org). It does not contain normative requirements; it is a user interface for login.

## Requirements Summary
No normative requirements. The page presents a login form with the following elements:
- **Username field** (required)
- **Password field** (required)
- **"Keep me signed in"** checkbox (optional)
- **"Sign Up"** link (opens external registration page: https://portal.etsi.org/createaccount)
- **"Forgot your password?"** link (opens /ResetPassword.aspx)
- **"Login"** button (triggers JavaScript authentication via ETSI Online account)

Error message displayed on failed authentication: "Username or password was incorrect".

## Informative Notes
- The page is part of the ETSI Portal (version 3.14.62, dated 2026-04-23) and is optimized for Chrome, Edge, and Firefox.
- Footer contains links to Terms of use, Privacy policy, and Legal Notice.