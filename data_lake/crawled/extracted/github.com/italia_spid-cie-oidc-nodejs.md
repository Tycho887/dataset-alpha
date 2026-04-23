---
{
  "title": "GitHub - italia/spid-cie-oidc-nodejs: The SPID/CIE OIDC Federation for Node.js · GitHub",
  "url": "https://github.com/italia/spid-cie-oidc-nodejs",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3154,
  "crawled_at": "2026-04-23T20:48:54"
}
---

italia
/
spid-cie-oidc-nodejs
Public
Notifications
You must be signed in to change notification settings
Fork
6
Star
19
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
83 Commits
83 Commits
.github
.github
examples/
express-react-relying-party
examples/
express-react-relying-party
relying-party
relying-party
.gitignore
.gitignore
AUTHORS
AUTHORS
LICENSE
LICENSE
README.md
README.md
preview.gif
preview.gif
View all files
Repository files navigation
SPID/CIE OIDC Federation, for Node.js
SPID/CIE OIDC Federation
is a suite of
Node.js libraries
and
example projects
designed to ease the creation of an Openid Connect Federation.
⚠️
This project is a work-in-progress. Currently only the
Relying Party
has been completed.
👀 Watch this repository over GitHub to stay informed.
Library
Status
OpenID Connect Trust Anchor
OpenID Connect Identity Provider
OpenID Connect Relying Party
Packages
[
SPID/CIE OIDC Federation Relying Party
(
spid-cie-oidc
)
A Node.js library that exposes utility functions to configure your web-application endpoints in order to support the SPID/CIE authentication over the OpenID Federation Authentication protocol.
Example projects
Example Express application (and React)
An example full web server built with Express v4 with the Relying Party library manually integrated (Passport or similar facilities have not been used).
The user-facing application is built with React v17, scaffolded with Create React App v5.
Useful links
Openid Connect Federation
SPID/CIE OIDC Federation SDK
Contribute
Your contribution is welcome, no question is useless and no answer is obvious, we need you.
Contribute as end user
Please open an issue if you've discoveerd a bug or if you want to ask some features.
Implementation Notes
The
jose
library is used fro JWT encryption and signature related operations.
This project proposes an implementation of the italian OIDC Federation profile with
automatic_client_registration
and the adoption of the trust marks as mandatory.
If you're looking for a fully compliant implementation of OIDC Federation 1.0,
with a full support of explicit client registration, please look at idpy's
fedservice
.
License and Authors
This software is released under the Apache 2 License by:
Frederik Batuna
frederik.batuna@smc.it
Notes
Npm package publishing
A
github action
is configured
here
to publish the package automatically.
To publish a new version of the package create a new release
here
.
To change npmjs secret (
article
).
About
The SPID/CIE OIDC Federation for Node.js
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Custom properties
Stars
19
stars
Watchers
11
watching
Forks
6
forks
Report repository
Releases
3
Relying Party v0.5.0
Latest
Apr 3, 2022
+ 2 releases
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
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
TypeScript
99.3%
JavaScript
0.7%