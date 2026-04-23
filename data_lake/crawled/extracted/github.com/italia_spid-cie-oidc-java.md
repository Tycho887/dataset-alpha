---
{
  "title": "GitHub - italia/spid-cie-oidc-java: The SPID/CIE OIDC Federation Relying Party, written in Java · GitHub",
  "url": "https://github.com/italia/spid-cie-oidc-java",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.39,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 5565,
  "crawled_at": "2026-04-23T20:48:49"
}
---

italia
/
spid-cie-oidc-java
Public
Notifications
You must be signed in to change notification settings
Fork
5
Star
25
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
139 Commits
139 Commits
.github/
workflows
.github/
workflows
.mvn/
wrapper
.mvn/
wrapper
coverage
coverage
docs
docs
examples
examples
starter-kit
starter-kit
.gitignore
.gitignore
AUTHORS
AUTHORS
LICENSE
LICENSE
README.md
README.md
mvnw
mvnw
mvnw.cmd
mvnw.cmd
pom.xml
pom.xml
preview.gif
preview.gif
View all files
Repository files navigation
SPID/CIE OIDC Federation, for Java
SPID/CIE OIDC Federation (for Java)
is a
starter kit
and
example projects
designed to ease the creation of an OpenID Connect Federation.
⚠️
This project is a work-in-progress, the first. Currently only the
Relying Party
has been completed.
👀 Watch this repository over GitHub to stay informed.
SUMMARY
Features
Usage
Docker
Example projects
SpringBoot Relying Party example
Useful links
Contribute
Contribute as end user
Contribute as developer
License and Authors
Features
The purpose of this project is to provide a simple and immediate tool to integrate, in a WebApp developed with any Java Framework, the authentication services of SPID and CIE, automating the login/logout flows, the management of the OIDC-Core/OIDC-Federation protocols and their security profiles, and simplify the development activities.
It contains a
starter-kit
, a java library that exposes utilities,
helpers
and
handlers
you can include into your application in order to support the SPID/CIE OpenID Connect Authentication profile and OpenID Federation 1.0.
The library is developed using
Java 11
with a "Low Level Java" approach to limit dependencies and allowing it to be included into projects mades with high-level framework like Spring, SpringBoot, OSGi, Quarkus and many others java based frameworks.
Actually only "
OpenID Connect Relying Party
"
role
is managed. The starter-kit provides:
Federation Entity Jwks and Metadata creation
OIDC Federation onboarding
SPID and CIE OpenID Connect login and logout
UserInfo claims retrieving
Build (discover) TrustChain of OPs
Multitenancy
see
Usage
for a more detailed list
The "
OpenID Connect Provider
"
role
is in my thoughts. Several requirements are already covered by the current starter-kit and the missing aspects should not require lot effort.
There are no plans to extends the starter-kit to allow you to implement an "
OpenID Connect Federation
Server".
Usage
Both Snapshots and Released artifacts are available on
GitHub Packages
:
if you use Maven
<
dependency
>
  <
groupId
>it.spid.cie.oidc</
groupId
>
  <
artifactId
>it.spid.cie.oidc.starter.kit</
artifactId
>
  <
version
>
<!--
replace with the wanted version
-->
</
version
>
</
dependency
>
if you use Gradle
implementation
group
:
'
it.spid.cie.oidc
'
,
name
:
'
it.spid.cie.oidc.starter.kit
'
,
version
:
'
wanted-version
'
Unfortunately, as stated in the
documentation
, to use GitHub packages you have define GitHub repository in your
~/.m2/settings.xml
together with your credentials.
The "starter-kit" is a
backend
library with few dependencies:
org.json:json
, a simple and light-weigth to parse and create JSON documents
com.nimbusds:nimbus-jose-jwt
, the most popular java Library to manage JSON Web Token (JWT, JWE, JWS)
com.github.stephenc.jcip:jcip-annotations:1.0-1
, a clean room implementation of the JCIP Annotations
org.slf4j:slf4j-api
go
here
for more detailed information
Docker
The "starter-kit" is a library.
Sample projects using the library can be executed as docker or docker-compose. See examples's documentation.
Example projects
SpringBoot Relying Party example
A simple
SpringBoot
web application using the starter-kit to implement a Relying Party, as well to perform the complete onboarding and login/logout test within the CIE Federation.
This application is for demo purpose only, please don't use it in production or critical environment.
Useful links
Openid Connect Federation
SPID/CIE OIDC Federation SDK
Contribute
Your contribution is welcome, no question is useless and no answer is obvious, we need you.
Contribute as end user
Please open an issue if you've discoverd a bug or if you want to ask some features.
Contribute as developer
This repository follow a
Trunk based Development
approach:
main
branch contains the evolution of the project, where developed code is merged
x-branch
are short-lived feature branches always connected to one or more issues (to better track and motivate requirements)
At the moment there is a GitHub Action allowing
releasing from Trunk
.
Please open your Pull Request on the
main
branch, but before start coding open an issue to describe your needs and inform the Team you are working on it.
In this project we adopt
Semver
and
Conventional commits
specifications.
License and Authors
This software is released under the Apache 2 License by:
Mauro Mariuzzo
mauro.mariuzzo@smc.it
.
About
The SPID/CIE OIDC Federation Relying Party, written in Java
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
25
stars
Watchers
12
watching
Forks
5
forks
Report repository
Releases
9
v1.0.3
Latest
Mar 10, 2026
+ 8 releases
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
Java
100.0%