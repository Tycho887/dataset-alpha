---
{
  "title": "GitHub - rohe/pyjwkest: Implementation of JWT, JWS, JWE and JWK · GitHub",
  "url": "https://github.com/rohe/pyjwkest",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2057,
  "crawled_at": "2026-04-23T20:52:02"
}
---

This repository was archived by the owner on Dec 30, 2024. It is now read-only.
rohe
/
pyjwkest
Public archive
forked from
IdentityPython/pyjwkest
Notifications
You must be signed in to change notification settings
Fork
3
Star
20
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
1,403 Commits
1,403 Commits
doc
doc
script
script
src/
jwkest
src/
jwkest
tests
tests
.gitignore
.gitignore
.travis.yml
.travis.yml
LICENSE
LICENSE
README.rst
README.rst
requirements.txt
requirements.txt
setup.py
setup.py
tox.ini
tox.ini
View all files
Repository files navigation
pyjwkest
Implementation of JWT, JWS, JWE and JWK as defined in:
https://tools.ietf.org/html/draft-ietf-jose-json-web-signature
https://tools.ietf.org/html/draft-ietf-jose-json-web-encryption
https://tools.ietf.org/html/draft-ietf-jose-json-web-key-36
Installation
Pyjwkest is written and tested using Python version 2.7 and 3.4.
You should be able to simply run 'python setup.py install' to install it.
But you may get some complains during the installation of pycrypto.
Taken from the pycrypto installation text:
If the setup.py script crashes with a DistutilsPlatformError complaining
that the file /usr/lib/python2.2/config/Makefile doesn't exist, this means
that the files needed for compiling new Python modules aren't installed on
your system. Red Hat users often run into this because they don't have the
python2-devel RPM installed. The fix is to simply install the requisite RPM.
On Debian/Ubuntu, you need the python-dev package.
To verify that everything is in order, run "python setup.py test".
About
Implementation of JWT, JWS, JWE and JWK
Resources
Readme
License
Apache-2.0 license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
20
stars
Watchers
2
watching
Forks
3
forks
Report repository
Releases
16
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
99.9%
Shell
0.1%