# [No Document ID]: ETSI Portal Login Page (Redirect to Draft)
**Source**: ETSI Portal | **Version**: N/A | **Date**: 2026-04-23 (from footer) | **Type**: Informative
**Original**: https://portal.etsi.org/LoginRedirection.aspx?domain=docbox.etsi.org&ReturnUrl=/esi/esi/70-Drafts/0019182-1v131/ESI-0019182-1v131v122.docx

## Scope (Summary)
This is a login authentication page for the ETSI Portal. It does not contain normative or technical specification content. After successful login, it redirects to a document at the specified ReturnUrl (a draft file: ESI-0019182-1v131v122.docx).

## Normative References
None.

## Definitions and Abbreviations
None.

## Content (Non-Normative)
The page provides a username/password form for EOL (ETSI Online) account authentication. It includes links to ETSI resources, menus, and footer with copyright and privacy information. No normative requirements are present.

## Informative Annexes
- **Page Functionality**: The page script performs login via AJAX to `/ETSIPages/LoginEOL.ashx` and on success redirects to the ReturnUrl (if provided) or reloads the page.
- **Target Document**: The intended resource is located at `docbox.etsi.org/esi/esi/70-Drafts/0019182-1v131/ESI-0019182-1v131v122.docx` (likely a draft ETSI specification). This file is not accessible without authentication.