# ETSI Portal Login Page
**Source**: ETSI | **Version**: v3.14.62 | **Date**: 2026-04-23 | **Type**: Informative  
**Original**: Raw HTML from portal.etsi.org login page (chunk 1 of 1)

## Scope (Summary)
This page provides user authentication (login) for ETSI portal members, granting access to document downloads, work programmes, and member services. Credentials are managed via an ETSI Online (EOL) account.

## Normative References
None.

## Definitions and Abbreviations
- **EOL**: ETSI Online account – the credential system used to authenticate users.

## Authentication Procedure
### 1. Login Form
- **Username**: Required text input (id="EOLUsername").
- **Password**: Required password input (id="EOLPassword").
- **Keep me signed in**: Checkbox (id="rememberMe") with [more info](http://portal.etsi.org/Help/ITHelpdesk/PortalLoginInformation.aspx).
- **Login Button**: Submits credentials via XMLHttpRequest POST to `/ETSIPages/LoginEOL.ashx`. On failure, shows "Username or password was incorrect". On success, redirects to the original requested URL (if provided) or reloads the page.
- **Error Message**: `#userPswIncorrect` element displays when authentication fails.

### 2. Alternative Actions
- **Sign Up**: Link to create account at `https://portal.etsi.org/createaccount`.
- **Forgot password**: Link to reset at `https://portal.etsi.org/ResetPassword.aspx`.

### 3. Navigation Menu (Summary)
The page includes a top navigation bar with the following categories and key sub-links:
- **Home** → Portal Home, Web Home
- **Resources** → ETSI Drafting Rules, Skeletons, User Guides (Chair’s Guide, Delegate’s Guide, etc.), Partnership agreements, Radio Spectrum, Presentations, ETSI Directives
- **People** → Organisation Chart, Committee Support Staff, CTI Support Staff, STF Support Staff, Directory (locked)
- **Services** → editHelp! (Drafting, Tracking, Guidelines, Tools, etc.), eLearning, Centre for Testing & Interoperability (CTI), Specialist Tasks Forces (STF), Closed ETSI Groups
- **IPR** → IPRs in ETSI, Search/Declare IPRs (locked)
- **Manage** → Approve (E-Approval, Voting, Membership Poll – locked), Access (Change password, Reset password, Access Rights Management – locked, Account request), My details (locked), TB Membership (locked), Mailing Lists, Meetings (locked), View room allocation (locked)
- **Search** → Terms & Definitions (TEDDI), ETSI Work Programme, Standards Search
- **Events** → Meetings Calendar, Getting To ETSI, Events Calendar
- **Help** → IT Helpdesk, Portal Help, Portal Change Log, Submit a new portal feature
- **WEBstore** → External link to ETSI Webstore

### 4. Footer
- **Compatibility**: Optimized for Chrome, Edge, and Firefox.
- **Copyright**: © ETSI 2026. All rights reserved.
- **Links**: Terms of use, Privacy policy, Legal Notice.

## Informative Annexes (Condensed)
- **User Guides**: A comprehensive collection of guides for Chairs, Delegates, Rapporteurs, STF Experts, Meeting Hosts, Member Official Contacts, NSOs, as well as guides on English drafting and gender-inclusive language. All accessible via the navigation menu.
- **editHelp!**: A full service for standard drafting, providing skeletons, styles toolbar, editing checklist, editing questions, communiqués, and tools like the Terms & Definitions database (TEDDI) and 3GPP cross-reference tool.