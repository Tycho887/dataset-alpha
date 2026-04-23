---
{
  "title": "GitHub - italia/openid-federation-authority · GitHub",
  "url": "https://github.com/italia/openid-federation-authority",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2386,
  "crawled_at": "2026-04-23T20:51:01"
}
---

italia
/
openid-federation-authority
Public
Notifications
You must be signed in to change notification settings
Fork
0
Star
1
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
7 Commits
7 Commits
src
src
.gitignore
.gitignore
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
View all files
Repository files navigation
OpenID Federation Authority
Technical requirements
OpenID Federation Authority is a backend project developed in Java with Spring Boot Framework that include the functionality of Federation Authority implementing the Infrastructure of Trust according to
Italian EUDI Wallet Technical Specifications
and following the
OpenID Federation 1.0 specs
.
API
GET .well-known/openid-federation
Metadata that an Entity publishes about itself, verifiable with a trusted third party (Superior Entity). It's called Entity Configuration.
GET /list
Lists the Subordinates.
GET /fetch?sub=...&iss=...
Returns a signed document (JWS) about a specific subject, its Subordinate. It's called Entity Statement.
POST /status?sub=...&trust_mark_id=...
Returns the status of the issuance (validity) of a Trust Mark related to a specific subject.
POST /resolve?sub=...&type=...&anchor=...
Fetch resolved metadata and Trust Marks for an Entity. The resolver fetches the subject's Entity Configuration, assembles a Trust Chain that starts with the subject's Entity Configuration and ends with the specified Trust Anchor's Entity Configuration, verifies the Trust Chain, and then applies all the policies present in the Trust Chain to the subject's metadata.
GET /historical-jwks
Lists the expired and revoked keys, with the motivation of the revocation.
POST /onboard
Request to onboard a subordinate.
License:
Apache License Version 2.0
About
No description, website, or topics provided.
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
1
star
Watchers
4
watching
Forks
0
forks
Report repository
Releases
No releases published
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