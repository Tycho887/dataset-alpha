---
{
  "title": "GitHub - openid/OpenID4VP · GitHub",
  "url": "https://github.com/openid/OpenID4VP",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.51,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2243,
  "crawled_at": "2026-04-23T20:55:14"
}
---

openid
/
OpenID4VP
Public
Notifications
You must be signed in to change notification settings
Fork
36
Star
98
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
1,348 Commits
1,348 Commits
.github/
workflows
.github/
workflows
1.0
1.0
1.1
1.1
.gitignore
.gitignore
CONTRIBUTING.md
CONTRIBUTING.md
README.md
README.md
publish.sh
publish.sh
View all files
Repository files navigation
README
Current WG-Draft
The current WG-Draft version is built automatically from the main branch and can be accessed at:
1.0:
https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-1_0-wg-draft.html
1.1:
https://openid.github.io/OpenID4VP/openid-4-verifiable-presentations-1_1-wg-draft.html
Building the HTML
The easiest way to build the HTML is to use the
danielfett/markdown2rfc
docker image. For example, to build the
1.1
version of the spec, do the following:
bash / zsh / sh
cd 1.1
docker run -v `pwd`:/data danielfett/markdown2rfc openid-4-verifiable-presentations-1_1.md
fish
cd 1.1
docker run -v (pwd):/data danielfett/markdown2rfc openid-4-verifiable-presentations-1_1.md
Conformance tests
Conformance tests are available for testing whether both Wallets and
Verifiers are compliant with this specification, see:
https://openid.net/certification/conformance-testing-for-openid-for-verifiable-presentations/
Contribution guidelines
There are two ways to contribute, creating issues and pull requests
All proposals are discussed in the WG on the list and in our regular calls before being accepted and merged.
Who do I talk to?
The WG can be reached via the mailing list
openid-specs-digital-credentials-protocols@lists.openid.net
(join the ML
here
).
About
openid.net/wg/digital-credentials-protocols/
Topics
openid
digital-credentials
oid4vp
openid4vp
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
98
stars
Watchers
55
watching
Forks
36
forks
Report repository
Releases
10
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
Shell
100.0%