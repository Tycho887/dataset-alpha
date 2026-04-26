# ETSI Portal Login Page
**Source**: ETSI | **Version**: 3.14.62 | **Date**: 2026-04-23 | **Type**: Informative (Portal Login)
**Original**: https://portal.etsi.org/LoginRedirection.aspx?domain=docbox.etsi.org&ReturnUrl=/esi/esi/70-Drafts/0019615141/ESI-0019615141v133.docx

## Scope (Summary)
This page serves as the authentication gateway to access ETSI document repositories (e.g., docbox.etsi.org). Users **must** log in with their ETSI Online (EOL) account credentials to proceed to the requested resource.

## Access Requirements
- **Authentication**: EOL account (Username and Password).
- **Form Fields**:
  - `EOLUsername`: text input (required).
  - `EOLPassword`: password input (required).
- **Optional**: "Keep me signed in" checkbox (with link to [more info](http://portal.etsi.org/Help/ITHelpdesk/PortalLoginInformation.aspx)).
- **Actions**: Login button triggers POST to `/ETSIPages/LoginEOL.ashx` with JSON credentials. On success, redirect to the originally requested URL (domain + ReturnUrl). On failure, error message displayed.

## Navigation Links (Condensed)
The page header includes a comprehensive menu with links to:
- **Resources**: Drafting rules, skeletons, user guides, partnership agreements, radio spectrum, ETSI presentations, directives.
- **People**: Organisation chart, committee support, directory (requires login).
- **Services**: editHelp! (drafting support, standards development, tracking, guidelines), eLearning, Centre for Testing & Interoperability, Specialist Task Forces, closed groups.
- **IPR**: IPR policy, online search/declaration (requires login).
- **Manage**: E-Approval, voting tools, access rights, meetings.
- **Search**: Terms & definitions (TEDDI), work programme, standards search.
- **Events**: Meetings calendar, events.
- **Help**: IT Helpdesk, portal help, change log, feature request.
- **Webstore**: ETSI publications.

## Footer Information
- **Browser support**: Chrome, Edge, Firefox.
- **Version**: ETSI Portal v3.14.62 (2026-04-23).
- **Links**: [Terms of use](http://www.etsi.org/website/copyright.aspx), [Privacy policy](http://www.etsi.org/privacy), [Legal Notice](https://portal.etsi.org/Legal-Notice).
- **Copyright**: © ETSI 2026.

## Additional Notes
- The page includes JavaScript for adaptive frame resizing and for custom feedback button in the menu (e.g., "Feedback" button styled with purple background).
- Error message "Username or password was incorrect" displayed if authentication fails.
- Password reset and account creation links provided:
  - [Sign Up](https://portal.etsi.org/createaccount)
  - [Forgot your password?](/ResetPassword.aspx)