---
{
  "title": "GitHub - DuendeArchive/identity-model-oidc-client-js: OpenID Connect (OIDC) and OAuth2 protocol support for browser-based JavaScript applications · GitHub",
  "url": "https://github.com/IdentityModel/oidc-client-js",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3189,
  "crawled_at": "2026-04-23T20:50:49"
}
---

This repository was archived by the owner on Mar 3, 2022. It is now read-only.
DuendeArchive
/
identity-model-oidc-client-js
Public archive
Notifications
You must be signed in to change notification settings
Fork
827
Star
2.4k
dev
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
888 Commits
888 Commits
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
dist
dist
jsrsasign
jsrsasign
lib
lib
samples
samples
src
src
test
test
.babelrc
.babelrc
.gitattributes
.gitattributes
.gitignore
.gitignore
.npmignore
.npmignore
GitReleaseManager.yaml
GitReleaseManager.yaml
LICENSE
LICENSE
README.md
README.md
bower.json
bower.json
gulpfile.js
gulpfile.js
index.d.ts
index.d.ts
index.js
index.js
jsconfig.json
jsconfig.json
package-lock.json
package-lock.json
package.json
package.json
polyfills.js
polyfills.js
version.js
version.js
webpack.base.js
webpack.base.js
View all files
Repository files navigation
No Longer Maintained
This library, while functional, is no longer being maintained.
A successor project that is showing great progress in updating and modernizing is "oidc-client-ts" and can be found
here
.
oidc-client
Library to provide OpenID Connect (OIDC) and OAuth2 protocol support for client-side, browser-based JavaScript client applications.
Also included is support for user session and access token management.
Install
Node.js
Node.js v4.4 or later required.
NPM
npm install oidc-client --save
NOTE
: if you're not already using
babel-polyfill
make sure you run
npm install --save babel-polyfill
as well. Then include it in your build.
CommonJS
If you don't use a package manager or a module loader, then you can get the library from the
dist
folder on github
here
.
Including in the browser
If you intend to use this library directly in a browser and are not using UMD/AMD then there is a compiled version in the
~/dist
folder.
It is already bundled/minified and contains the necessary dependencies and polyfills (mainly for ES6 features such as Promises).
If you are using UMD/AMD and/or you already have included an ES6 polyfill (such as babel-polyfill.js) then you can include the UMD packaged version of the file from the
~/lib
folder.
Building the Source
git clone https://github.com/IdentityModel/oidc-client-js.git
cd oidc-client-js
npm install
npm run build
Running the Sample
npm start
and then browse to
http://localhost:15000
.
Running the Tests
npm test
Docs
Some initial docs are
here
.
Feedback, Feature requests, and Bugs
All are welcome on the
issue tracker
.
About
OpenID Connect (OIDC) and OAuth2 protocol support for browser-based JavaScript applications
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
2.4k
stars
Watchers
85
watching
Forks
827
forks
Report repository
Releases
29
1.11.5
Latest
Feb 17, 2021
+ 28 releases
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
JavaScript
100.0%