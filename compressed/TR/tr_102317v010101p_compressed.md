# ETSI TR 102 317: Electronic Signatures and Infrastructures (ESI); Process and tools for maintenance of ETSI deliverables
**Source**: ETSI | **Version**: V1.1.1 | **Date**: 2004-06 | **Type**: Informative (Technical Report)
**Original**: DTR/ESI-000029 (ETSI, 650 Route des Lucioles, F-06921 Sophia Antipolis Cedex – FRANCE)

## Scope (Summary)
This Technical Report describes the maintenance activity performed by TC ESI, the structure of the maintenance report (TR 102 046), and the tools (MS Access database, MS Word Mail Merge template, VBA macros) developed to simplify tracking, pre-processing, and processing of comments on ETSI deliverables. Clause 4 explains the revised maintenance process; clause 5 describes the tools (installation, usage, internals); clause 6 outlines possible improvements.

## Normative References
- [1] ETSI TR 102 046 (V1.1.1): "Electronic Signatures and Infrastructures (ESI); Maintenance Report"
- [2] ETSI TR 102 046 (V1.2.1): "Electronic Signatures and Infrastructures (ESI); Maintenance Report"
- [3] ETSI SR 001 262 (V1.8.1): "ETSI drafting rules"

## Definitions and Abbreviations
- **contribution**: every block of comments (≥1 comment) received as a whole, related to only one deliverable, identified by a unique code
- **elementary comment**: one atomic comment obtained by splitting a contribution during pre-processing; may coincide with the contribution
- **Mail Merge**: MS Word feature for mail merge operation
- **Mail Merge database**: MS Access database containing elementary comments; data source for Mail Merge
- **Mail Merge template**: MS Word file with Mail Merge fields formatted in a table
- **maintenance activity phase**: historical round of TC ESI maintenance activity
- **maintenance process stage**: part of the revised process (tracking, pre-processing, processing)
- **maintenance report**: report covering status of maintenance activity; can be published as ETSI Technical Report
- **maintenance report base file**: file containing the report except for clause 5 (comments); includes placeholders for tables
- **maintenance report target file**: complete report after Mail Merge and macro execution
- **Abbreviations**: HTML, SQL, STF, VBA

## Maintenance Activity
### History of TC ESI Maintenance Activity
- First phase: comments collected in original format (TR 102 046 [1]) without tools.
- Second phase: improved structured process, development of tools, new restructured TR 102 046 [2].
- Aim: share with other technical committees.

### Revised Maintenance Process
#### General Description
Three stages covered by the report and tools:
- **Tracking**: record contributions from any source in original format.
- **Pre-processing**: split contributions into elementary comments with metadata.
- **Processing**: resolve each elementary comment (preferably grouped by deliverable).

Subjects involved: general maintenance STF, specific maintenance STF, TC ESI members.

#### Tracking Stage
General maintenance STF records contributions.

#### Pre-processing Stage
General maintenance STF transforms unstructured contributions into structured set of elementary comments grouped by deliverable.

#### Processing Stage
Resolve comments, may be done by general STF, specific STF, or TC ESI members. Selection of deliverables and method is STF responsibility after TC ESI consensus.

### Maintenance Report
#### Role
Internal tool for tracking, pre-processing, processing; public as ETSI Technical Report.

#### Structure of Maintenance Report
- Cover page to clause 3: ETSI template.
- Clause 4: describes structure (the present document).
- Clause 5: body with tables of elementary comments (one per deliverable), generated automatically from Mail Merge database.
- Annex A: original contributions with metadata, kept as original format.

#### Clause 5 Fields and Structure
Each elementary comment table includes rows with:
- Deliverable ID, version, section
- Source, date
- Comment ID (e.g., `<deliverable_ID>-<unique_code>`)
- Reference to original contribution
- Comment text
- Comment type: **editorial** or **technical**
- Original resolution proposal
- Resolution comment (status-specific)
- Resolution text (status-specific)
- Resolution date
- Resolution source
- Status: not yet processed, in process, provisionally approved, applied, already applied, rejected, no change
- Target deliverable version

#### Annex A Fields and Structure
Each contribution (block of comments per deliverable) includes:
- Contribution ID (e.g., `<Source_ID>-<unique_code>`)
- Source, date, version
- Original text (format preserved)
- Original proposed solution (if any)
- E-mail threads treated as single contributions.

## Maintenance Tools
### Description
Three components:
- **MS Access database**: stores elementary comments via a form.
- **MS Word Mail Merge template**: formatted table for generating clauses.
- **VBA macros**: manage Mail Merge setup, execution, formatting, and insertion into target document.

Tools are single-user (database on file).

### Requirements
Microsoft Access and Word, tested on English MS Office 2000 SP3.

### Installation
- Unzip `ETSI_maintenance_tools_v1.0.zip`.
- Install template (`ETSI_maintenance.dot`) as global template (via Tools→Templates and Add-Ins) or copy to Word startup folder.
- Tools packaged: `ETSI_maintenance.dot`, `ETSI_maintenance_DB.mdb`, `ETSI_maintenance_MM_template.doc`, `Readme.txt`.

### Usage
#### General Process
1. Prepare maintenance report base file with placeholders: `<insert_table name=DELIVERABLE_ID/>`.
2. Tracking: complete Annex A with contributions.
3. Pre-processing: split contributions into elementary comments; insert into Mail Merge database.
4. Processing: update resolution data in database.
5. Generate maintenance report target file using menus and macros.
6. Finish: manually format text inside table cells, handle long comments, remove resolved comments in subsequent versions.

#### Inserting Elementary Comments into Database
Open `ETSI_maintenance_DB.mdb`. The insertion form (Figure 1) exposes fields from `tComments` table plus `anonym_contrib_source` and `anonym_resolution_source` for anonymization. At minimum, `comment_ID`, `elem_comment_type`, and `resolution_status` shall be filled.

#### Creating the Body of the Maintenance Report
- Launch Word, click "ETSI Maintenance" toolbar button → main menu (Figure 2).
- Provide paths for Mail Merge template, database, report base file, target file.
- Buttons: "Setup Mail Merge and edit", "Start Mail Merge", "Format MM output, copy, save".
- Macro joins tables per deliverable, copies into base file placeholders, saves target file.

#### Finishing the Maintenance Report
- Manual formatting (indenting, bullets, bold/italic/underline) to fit editHelp! requirements.
- Manually split long comments across cells.
- Manually remove resolved comments in subsequent versions.

### How the Tools Work
- **Mail Merge database**: MS Access with query `qComments` returning records ordered by comment ID.
- **Mail Merge Word feature**: uses template with one paragraph before and after table → output `Catalog1` with many tables.
- **Macro**:
  1. Joins tables for same deliverable based on comment ID prefix (e.g., `TS101456-007` → deliverable ID `TS101456`).
  2. Copies each table into base file placeholder.
  3. Saves as target file.

### Generalized Use
The tools can manage any data type as long as database contains `qComments` query and constraints on comment IDs are respected.

## Tools Improvements
### Adding Automatic Formatting Capabilities
Extend macros to use HTML-like tags for formatting; modify insertion form.

### Improving the Database Structure
Normalize to avoid redundant data (e.g., contribution source/date).

### Improving the Database Insertion Form
Speed-up input for multiple comments on same deliverable.

### Making the Tools Corporate
- Use centralized server database for multi-user concurrent access.
- Implement web-based form for visual editing.
- Support a range of Office versions.

## Requirements Summary
No normative requirements in this Technical Report. All "shall" statements are descriptive (e.g., field must be filled) or procedural (e.g., macro shall join tables). No compliance requirements.

## Informative Annexes (Condensed)
- **Annex A: Database Structure** – Defines tables `tComments`, `tCommentType`, `tResolutionStatus` with columns, predefined records (e.g., comment types "editorial"/"technical", resolution statuses "ALAP"/"APPL"/"INPR"/"NOCH"/"NYPR"/"PRAP"), relationships, and `qComments` SQL query.
- **Annex B: MS Word Global Template: VBA Sources and Forms** – Contains full VBA code for modules `modCode`, `frmMenu`, `frmInfo` and user forms. The code implements the macro operations described in clause 5.
- **Annex C: How to Recreate the Tools** – Step-by-step instructions to rebuild the Mail Merge database, VBA macros, and Mail Merge template from scratch using the document alone.
- **Annex D: Mail Merge Template and Maintenance Report Samples** – Provides sample Mail Merge template (Table D.1), sample clause 5 base file with placeholders (D.2), and examples of formatted elementary comments (D.3) and contributions in Annex A (D.4).