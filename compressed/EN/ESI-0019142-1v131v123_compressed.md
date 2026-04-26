# Login Page: ETSI Portal Authentication
**Source**: ETSI Portal (portal.etsi.org) | **Version**: v3.14.62 | **Date**: 2026-04-23 | **Type**: Informative
**Original**: https://portal.etsi.org/LoginRedirection.aspx?domain=docbox.etsi.org&ReturnUrl=%2fesi%2fesi%2f70-Drafts%2f0019142-1v131%2fESI-0019142-1v131v123.docx

## Scope (Summary)
This page provides a login interface for ETSI Online Account (EOL) users to access restricted resources. It includes a username/password form, a "Keep me signed in" option, and links to account creation, password reset, and help.

## Login Procedure
- **Username**: Enter EOL username in the text field.
- **Password**: Enter EOL password in the password field.
- **Credentials Submission**: Click the "Login" button (image link) or press Enter after filling fields.
- **Error Handling**: If credentials are incorrect, a message "Username or password was incorrect" is displayed.
- **Persistent Session**: The "Keep me signed in" checkbox may extend the session; see [more info](http://portal.etsi.org/Help/ITHelpdesk/PortalLoginInformation.aspx).
- **Redirection**: On successful login, the user is redirected to the originally requested URL (from `ReturnUrl` parameter) or to the same page if no redirect is specified.

## Links Provided
- **Sign Up**: [Create a new ETSI account](https://portal.etsi.org/createaccount) (opens in new tab).
- **Forgot Password**: [Reset your password](https://portal.etsi.org/ResetPassword.aspx) (opens in new tab).
- **Help**: [Portal Login Information](http://portal.etsi.org/Help/ITHelpdesk/PortalLoginInformation.aspx).

## Informative Annexes (Condensed)
- **Navigation Menus**: The page includes a comprehensive navigation bar with links to ETSI resources (drafting rules, user guides, partnership agreements), people/organization charts, services (editHelp!, testing, specialist task forces), IPR management, approval tools, search (terms, work programme, standards), events calendar, and IT helpdesk. These menus are not part of the login functionality but provide access to the ETSI portal's features.
- **Footer**: Standard ETSI footer with copyright (© ETSI 2026), portal version (3.14.62), date (2026-04-23), and links to Terms of Use, Privacy Policy, and Legal Notice. Browser optimization for Chrome, Edge, and Firefox is noted.
- **Scripting**: The page relies on JavaScript for login via AJAX POST to `ETSIPages/LoginEOL.ashx`, dynamic iframe resizing, and SuperFish menu effects. No normative requirements are imposed by these scripts.