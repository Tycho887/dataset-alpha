---
{
  "title": "GitHub - ulrikstrid/ocaml-oidc: OpenID Connect implementation in OCaml. Currently only the RP (client) parts are polished. · GitHub",
  "url": "https://github.com/ulrikstrid/ocaml-oidc",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2132,
  "crawled_at": "2026-04-23T20:56:18"
}
---

ulrikstrid
/
ocaml-oidc
Public
Notifications
You must be signed in to change notification settings
Fork
5
Star
50
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
127 Commits
127 Commits
.github/
workflows
.github/
workflows
.vscode
.vscode
cypress
cypress
executable
executable
nix
nix
oidc
oidc
scripts
scripts
test
test
.dockerignore
.dockerignore
.env
.env
.envrc
.envrc
.gitignore
.gitignore
.ocamlformat
.ocamlformat
CHANGES.md
CHANGES.md
LICENSE
LICENSE
README.md
README.md
azure-pipelines.yml
azure-pipelines.yml
cypress.json
cypress.json
dune-project
dune-project
flake.lock
flake.lock
flake.nix
flake.nix
oidc-client.opam
oidc-client.opam
oidc.opam
oidc.opam
View all files
Repository files navigation
ocaml-oidc
OpenID connect implementation in OCaml.
Folder structure
ocaml-oidc
│
├─executable/  Entrypoint for a webserver/OIDC client
│
├─library/     Implementation for the webserver
│
├─oidc/        Core OIDC implementation
│
├─oidc-client/ OIDC Client implementation
│
├─test/        tests
│
Developing:
npm install -g esy redemon reenv
git clone <this-repo>
esy install
esy build
Running Binary:
After building the project, you can run the main binary that is produced. This will start a webserver with a OIDC client configured for certification.
esy start
Running Tests:
# Runs the "test" command in `package.json`.
esy test
About
OpenID Connect implementation in OCaml. Currently only the RP (client) parts are polished.
ulrikstrid.github.io/ocaml-oidc/
Topics
ocaml
oidc
oidc-client
Resources
Readme
License
BSD-3-Clause license
Uh oh!
There was an error while loading.
Please reload this page
.
Activity
Stars
50
stars
Watchers
5
watching
Forks
5
forks
Report repository
Releases
3
0.2.0
Latest
Dec 17, 2024
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
OCaml
85.9%
JavaScript
6.6%
Nix
4.9%
Shell
1.3%
Dune
1.3%