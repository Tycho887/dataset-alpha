---
{
  "title": "sharedsignals/Makefile at main · openid/sharedsignals · GitHub",
  "url": "https://github.com/openid/sharedsignals/blob/main/Makefile",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.28,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 1962,
  "crawled_at": "2026-04-23T20:53:53"
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
Makefile
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
37 lines (31 loc) · 1.39 KB
main
/
Makefile
Top
File metadata and controls
Code
Blame
37 lines (31 loc) · 1.39 KB
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
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
OPEN
=
$(
word
1,
$(
wildcard
/usr/bin/xdg-open /usr/bin/open /bin/echo)
)
SOURCES?
=${wildcard *.xml}
TEXT=${SOURCES:.xml
=.txt}
HTML=${SOURCES:.xml
=.html}
text
:
$(
TEXT
)
html
:
$(
HTML
)
%
.html
:
%
.xml
xml2rfc --html
$^
%
.txt
:
%
.xml
xml2rfc
$^
%
.xml
:
%
.md
kramdown-rfc2629
>
$@
$^
all
:
@ make openid-sharedsignals-framework-1_0.xml
@ make openid-sharedsignals-framework-1_0.html
@ make openid-sharedsignals-framework-1_0.txt
@ make openid-risc-1_0.html
@ make openid-risc-1_0.txt
@ make openid-caep-1_0.xml
@ make openid-caep-1_0.html
@ make openid-caep-1_0.txt
propose
:
@ cp openid-sharedsignals-framework-1_0.txt ../publication/sharedsignals/openid-sharedsignals-framework-1_0-final.txt
@ cp openid-sharedsignals-framework-1_0.html ../publication/sharedsignals/openid-sharedsignals-framework-1_0-final.html
@ cp openid-sharedsignals-framework-1_0.md ../publication/sharedsignals/openid-sharedsignals-framework-1_0-final.md
@ cp openid-risc-1_0.html ../publication/sharedsignals/openid-risc-1_0-final.html
@ cp openid-risc-1_0.xml ../publication/sharedsignals/openid-risc-1_0-final.xml
@ cp openid-risc-1_0.txt ../publication/sharedsignals/openid-risc-1_0-final.txt
@ cp openid-caep-1_0.txt ../publication/sharedsignals/openid-caep-1_0-final.txt
@ cp openid-caep-1_0.html ../publication/sharedsignals/openid-caep-1_0-final.html
@ cp openid-caep-1_0.md ../publication/sharedsignals/openid-caep-1_0-final.md