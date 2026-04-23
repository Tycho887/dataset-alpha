---
{
  "title": "sharedsignals/.markdownlint.yaml at main · openid/sharedsignals · GitHub",
  "url": "https://github.com/openid/sharedsignals/blob/main/.markdownlint.yaml",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.28,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 900,
  "crawled_at": "2026-04-23T20:53:51"
}
---

openid
/
sharedsignals
Public
Notifications
You must be signed in to change notification settings
Fork
19
Star
73
Files
Expand file tree
main
/
.markdownlint.yaml
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
16 lines (16 loc) · 395 Bytes
main
/
.markdownlint.yaml
Top
File metadata and controls
Code
Blame
16 lines (16 loc) · 395 Bytes
Raw
Copy raw file
Download raw file
Open symbols panel
Edit and raw actions
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
default
:
true
MD013
:
line_length
:
80
tables
:
false
code_blocks
:
false
stern
:
true
#
blanks-around-fences false because of kramdown-rfc formatting
MD031
:
false
#
no-bare-urls
MD034
:
false
#
first-line-h1 false because of rfc heading
MD041
:
false
#
table-pipe-style and table-column-count set to false
#
these conflict with the table title kramdown-rfc formatting
MD055
:
false
MD056
:
false