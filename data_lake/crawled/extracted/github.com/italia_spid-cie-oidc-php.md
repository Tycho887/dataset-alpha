---
{
  "title": "GitHub - italia/spid-cie-oidc-php: The SPID/CIE OIDC Federation Relying Party for PHP · GitHub",
  "url": "https://github.com/italia/spid-cie-oidc-php",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 4142,
  "crawled_at": "2026-04-23T20:48:57"
}
---

italia
/
spid-cie-oidc-php
Public
Notifications
You must be signed in to change notification settings
Fork
8
Star
21
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
218 Commits
218 Commits
.github/
workflows
.github/
workflows
cert_sample
cert_sample
config_sample
config_sample
doc
doc
examples
examples
lib
lib
tests
tests
www
www
.gitignore
.gitignore
AUTHORS
AUTHORS
LICENSE
LICENSE
README.md
README.md
composer.json
composer.json
phpunit.xml
phpunit.xml
View all files
Repository files navigation
SPID/CIE OIDC Federation Relying Party for PHP
The SPID/CIE OIDC Federation Relying Party for PHP
Summary
What is SPID/CIE OIDC PHP
PHP class library
Standalone proxy relying party
Generic OIDC to SPID/CIE OIDC relying party
Features
Setup
Example projects
WordPress example project
Drupal example project
Contribute
Contribute as end user
Contribute as developer
Useful links
License and Authors
What is SPID/CIE OIDC PHP
SPID/CIE OIDC PHP is:
A PHP class library that helps to develop a relying party for SPID/CIE
Are you a Developer and you want to make your own relying party or a plugin for your software?
Read the
Technical documentation
.
A standalone proxy relying party for SPID/CIE
You can simply setup the proxy project and configure the URL where to receive users's attributes. You can also choice how the attributes will be returned from the proxy, such as plain values, signed or encrypted.
Read
How to use as a proxy
.
A generic OIDC to SPID/CIE OIDC relying party gateway
Can your application connect to a standard OIDC Provider, but it doesn't have extended functionalities required by the SPID/CIE OIDC Federation? No problem, you can configure your client as a relying party to SPID/CIE OIDC PHP Provider and it will make the rest.
Read
How to use as a generic OIDC Provider
.
Features
Interactive setup
Wizard for certificates generation
Bootstrap template
Hooks plugins
Simple API
Proxy functions
Ready to use
Setup
git clone https://github.com/italia/spid-cie-oidc-php.git
composer install
After setup go to /
service_name
/oidc/rp/authz
where
service_name
is the service name configured during setup.
Example projects
Start the basic example project is as simple as run:
docker pull linfaservice/spid-cie-oidc-php
docker run -it -p 8002:80 -v $(pwd)/config:/var/www/spid-cie-oidc-php/config linfaservice/spid-cie-oidc-php
On the first run the setup will ask for configurations.
All configurations will be saved in the ./config directory.
The repository also provides example projects to set up a complete SPID/CIE OIDC Federation.
Read how to set up a federation with the
WordPress Example Project
.
Read how to set up a federation with the
Drupal Example Project
.
Contribute
Your contribution is welcome, no question is useless and no answer is obvious, we need you.
Contribute as end user
Please open an issue if you've discoveerd a bug or if you want to ask some features.
Contribute as developer
Please open your Pull Requests on the
dev
branch.
Please consider the following branches:
main
: where we merge the code before tag a new stable release.
dev
: where we push our code during development.
other-custom-name
: where a new feature/contribution/bugfix will be handled, revisioned and then merged to dev branch.
In this project we adopt
Semver
and
Conventional commits
specifications.
Useful links
Openid Connect Federation
SPID/CIE OIDC Federation SDK
License and Authors
This software is released under the Apache 2 License by:
Michele D'Amico (@damikael)
michele.damico@linfaservice.it
.
About
The SPID/CIE OIDC Federation Relying Party for PHP
Topics
php
federation
cie
oidc-client
spid
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
21
stars
Watchers
8
watching
Forks
8
forks
Report repository
Releases
1
v0.3.0
Latest
Apr 11, 2022
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
PHP
99.8%
CSS
0.2%