---
{
  "title": "sharedsignals/README.md at main · openid/sharedsignals · GitHub",
  "url": "https://github.com/openid/sharedsignals/blob/main/README.md",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2034,
  "crawled_at": "2026-04-23T20:53:55"
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
README.md
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
35 lines (22 loc) · 2.38 KB
main
/
README.md
Top
File metadata and controls
Preview
Code
Blame
35 lines (22 loc) · 2.38 KB
Raw
Copy raw file
Download raw file
Outline
Edit and raw actions
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