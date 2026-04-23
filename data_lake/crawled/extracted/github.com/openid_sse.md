---
{
  "title": "GitHub - openid/sharedsignals: OpenID Shared Signals Working Group Repository · GitHub",
  "url": "https://github.com/openid/sse",
  "domain": "github.com",
  "depth": 1,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3183,
  "crawled_at": "2026-04-23T20:52:18"
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
main
Branches
Tags
Go to file
Code
Open more actions menu
Folders and files
Name
Name
Last commit message
Last commit date
Latest commit
History
333 Commits
333 Commits
.github
.github
.gitignore
.gitignore
.markdownlint.yaml
.markdownlint.yaml
Makefile
Makefile
README.md
README.md
contributing.md
contributing.md
oauth-event-types-1_0.txt
oauth-event-types-1_0.txt
oauth-event-types-1_0.xml
oauth-event-types-1_0.xml
openid-caep-1_0.md
openid-caep-1_0.md
openid-caep-interoperability-profile-1_0.md
openid-caep-interoperability-profile-1_0.md
openid-risc-1_0.xml
openid-risc-1_0.xml
openid-risc-use-cases.txt
openid-risc-use-cases.txt
openid-risc-use-cases.xml
openid-risc-use-cases.xml
openid-sharedsignals-framework-1_0.md
openid-sharedsignals-framework-1_0.md
subject-identifier-scenarios.txt
subject-identifier-scenarios.txt
subject-identifier-scenarios.xml
subject-identifier-scenarios.xml
working-group-charter.md
working-group-charter.md
View all files
Repository files navigation
SSF: Shared Signals Framework
The goal of the
Shared Signals
Working Group is to enable the sharing of security events, state changes, and other signals between related and/or dependent systems in order to:
Manage access to resources and enforce access control restrictions across distributed services operating in a dynamic environment.
Prevent malicious actors from leveraging compromises of accounts, devices, services, endpoints, or other principals or resources to gain unauthorized access to additional systems or resources.
Enable users, administrators, and service providers to coordinate in order to detect and respond to incidents.
Current Development Drafts
The current drafts of the specifications under development are kept here:
Specification
HTML
TXT
Shared Signals Framework
HTML
TXT
CAEP
HTML
TXT
RISC
HTML
TXT
CAEP Interoperability Profile
HTML
TXT
Development
To change the spec, update one of the xml files and then run
make
as follows:
Assume you changed the file
foo.md
. To generate the
foo.html
file, you would run
make foo.html
Similarly, to update the text file, you would run
make foo.txt
Pay attention to errors generating the files and warnings about the document date. You should update the date to today's date.
In order to run
make
you need to:
install
xml2rfc
which can be done via pip:
pip install xml2rfc
install
kramdown-rfc
which can be done via Ruby gems:
gem install kramdown-rfc
Note
The HTML and TXT files will not be uploaded to the repository. Running make only ensures that changes you made are not breaking the generation of the specifications output.
About
OpenID Shared Signals Working Group Repository
Topics
risc
ssf
caep
sharedsignals
Resources
Readme
Contributing
Contributing
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
73
stars
Watchers
24
watching
Forks
19
forks
Report repository
Releases
2
tags
Uh oh!
There was an error while loading.
Please reload this page
.
Contributors
Uh oh!
There was an error while loading.
Please reload this page
.
Languages
Makefile
100.0%