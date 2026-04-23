---
{
  "title": "GitHub - rohe/pyoidc: A complete OpenID Connect implementation in Python · GitHub",
  "url": "https://github.com/rohe/pyoidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3382,
  "crawled_at": "2026-04-23T20:56:14"
}
---

This repository was archived by the owner on Mar 9, 2023. It is now read-only.
rohe
/
pyoidc
Public archive
forked from
CZ-NIC/pyoidc
Notifications
You must be signed in to change notification settings
Fork
19
Star
71
master
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
2,493 Commits
2,493 Commits
.github
.github
doc
doc
docker
docker
oauth_example
oauth_example
oidc_example
oidc_example
script
script
src
src
tests
tests
.coveragerc
.coveragerc
.gitignore
.gitignore
.isort.cfg
.isort.cfg
.travis.yml
.travis.yml
CHANGELOG.md
CHANGELOG.md
LICENSE.txt
LICENSE.txt
Makefile
Makefile
README.rst
README.rst
appveyor.yml
appveyor.yml
mypy.ini
mypy.ini
pylama.ini
pylama.ini
runOpRp.sh
runOpRp.sh
setup.py
setup.py
tox.ini
tox.ini
View all files
Repository files navigation
A Python OpenID Connect implementation
This is a complete implementation of OpenID Connect as specified in the
OpenID
Connect Core specification
. And as a side effect, a complete implementation
of OAuth2.0 too.
Please see the
CHANGELOG.md
to review the latest changes.
Documentation
The
documentation
is graciously hosted by
Read the Docs
. Unfortunately,
the documentation has been largely left unmaintained and
there are various
issues
. However, the maintainers are trying to remedy this lately with some
new momentum. Please help us by submitting pull requests if you can help
improve the documentation.
Examples
Unfortunately, the current examples included in this repository are
unmaintained and
there are many issues
. We're currently in the process of
creating a working canonical example implementation, however, until that time,
the current examples largely do not work. Please help us by submitting pull
requests that may bring these examples back into a working condition if you
get something working locally.
Acknowledgements
Cudos to Vladislav Mladenov and Christian Mainka both at
Horst Görtz Institute for IT-Security, Ruhr-University Bochum, Germany
for helping me making the implementation more secure.
Maintainers Needed
If you're interested in helping maintain and improve this package, we're
looking for you! We're working on the project on a best effort basis but we
still maintain a good flow of reviewing each others pull requests and driving
discussions on what should be done. We also use a
mailing list
to have long
form discussions.
Please contact one of the current maintainers
@rohe
,
@tpazderka
or
@schlenk
.
Contribute
Fork the repository
, clone your copy and
install pipenv
.
Then just run:
$ make install
Next, running the tests:
$ make
test
This will not affect your system level Python installation. Please review
our
issues
to see what needs working on. Do not hesitate to ask questions if
something is unclear. We mark easy issues as
newcomer-friendly
, so they are
a good place to start if you want to contribute.
About
A complete OpenID Connect implementation in Python
Resources
Readme
License
View license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
71
stars
Watchers
3
watching
Forks
19
forks
Report repository
Releases
24
tags
Packages
0
Uh oh!
There was an error while loading.
Please reload this page
.
Contributors
0
No contributors
Languages
Python
87.5%
JavaScript
8.5%
Mako
2.7%
HTML
0.4%
Dockerfile
0.3%
Shell
0.3%
Other
0.3%