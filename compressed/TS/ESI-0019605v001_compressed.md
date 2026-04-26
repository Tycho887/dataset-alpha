# [Login Page]: ETSI Portal Authentication Interface
**Source**: ETSI | **Version**: Portal v3.14.62 | **Date**: 2026-04-23 | **Type**: Informative (Web Interface)
**Original**: https://portal.etsi.org/LoginRedirection.aspx?domain=docbox.etsi.org&ReturnUrl=/esi/esi/70-Drafts/0019605/ESI-0019605v001.docx

## Scope (Summary)
This is a login page for the ETSI Portal. It requires users to authenticate with an EOL account (username and password) to access a protected resource (a draft document at docbox.etsi.org). No normative requirements are present; the page is a standard web authentication form.

## Normative References
- None.

## Definitions and Abbreviations
- **EOL account**: ETSI Online account, used for accessing ETSI services.

## Authentication Process (Informative)
- User must enter **Username** and **Password** in the provided fields.
- Option to "Keep me signed in" via a checkbox (see [Portal Login Information](http://portal.etsi.org/Help/ITHelpdesk/PortalLoginInformation.aspx)).
- Login triggers a POST to `/ETSIPages/LoginEOL.ashx` with JSON credentials.
- On failure, error message "Username or password was incorrect" is displayed.
- On success, redirection to the original requested URL (e.g., a .docx file on docbox).
- Links for "Sign Up" (new account) and "Forgot your password?" are provided.

## Informative Annexes (Condensed)
- **Navigation Structure**: The page includes a comprehensive top menu with sections: Home, Resources, People, Services, IPR, Manage, Search, Events, Help, WEBstore. These provide access to ETSI tools, standards, guides, and administrative functions. The footer includes legal notices, privacy policy, and portal version.

## Notes
- The provided text is entirely an HTML implementation of a DNN login module with CSS/JS. It does not contain normative or technical specification content suitable for compression as a regulatory document. This summary captures the essential informative purpose.