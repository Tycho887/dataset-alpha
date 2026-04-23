---
{
  "title": "GitHub - nov/jose-php: PHP JOSE Library (JWT, JWS, JWE, JWK, JWK Set, JWK Thumbprint are supported) · GitHub",
  "url": "https://github.com/gree/jose",
  "domain": "github.com",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 3413,
  "crawled_at": "2026-04-23T21:01:17"
}
---

This repository was archived by the owner on Jan 3, 2024. It is now read-only.
nov
/
jose-php
Public archive
Uh oh!
There was an error while loading.
Please reload this page
.
Notifications
You must be signed in to change notification settings
Fork
66
Star
139
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
143 Commits
143 Commits
.github
.github
example
example
src/
JOSE
src/
JOSE
test
test
.gitignore
.gitignore
.travis.yml
.travis.yml
Gemfile
Gemfile
Gemfile.lock
Gemfile.lock
LICENSE
LICENSE
README.md
README.md
Rakefile
Rakefile
composer.json
composer.json
composer.lock
composer.lock
View all files
Repository files navigation
JOSE
PHP JOSE (Javascript Object Signing and Encryption) Implementation
Requirements
phpseclib is required.
http://phpseclib.sourceforge.net
Example
JWT
Encoding
$
jwt
=
new
JOSE_JWT
(
array
(
'
foo
'
=>
'
bar
'
));
$
jwt
->
toString
();
Decoding
$
jwt_string
=
'
eyJ...
'
;
$
jwt
=
JOSE_JWT
::
decode
(
$
jwt_string
);
JWS
Signing
$
private_key
=
"
-----BEGIN RSA PRIVATE KEY-----
\n
....
"
;
$
jwt
=
new
JOSE_JWT
(
array
(
'
foo
'
=>
'
bar
'
));
$
jws
=
$
jwt
->
sign
(
$
private_key
,
'
RS256
'
);
NOTE:
$private_key
can be
phpseclib\Crypt\RSA
instance.
Verification
$
public_key
=
"
-----BEGIN RSA PUBLIC KEY-----
\n
....
"
;
$
jwt_string
=
'
eyJ...
'
;
$
jws
=
JOSE_JWT
::
decode
(
$
jwt_string
);
$
jws
->
verify
(
$
public_key
,
'
RS256
'
);
NOTE:
$public_key
can be
JOSE_JWK
or
phpseclib\Crypt\RSA
instance.
JWE
Encryption
$
jwe
=
new
JOSE_JWE
(
$
plain_text
);
$
jwe
->
encrypt
(
file_get_contents
(
'
/path/to/public_key.pem
'
));
$
jwe
->
toString
();
Decryption
$
jwt_string
=
'
eyJ...
'
;
$
jwe
=
JOSE_JWT
::
decode
(
$
jwt_string
);
$
jwe
->
decrypt
(
$
private_key
);
JWK
Encode
RSA Public Key
$
public_key
=
new
phpseclib
\
Crypt
\
RSA
();
$
public_key
->
loadKey
(
'
-----BEGIN RSA PUBLIC KEY-----\n...
'
);
JOSE_JWK
::
encode
(
$
public_key
);
# => JOSE_JWK instance
RSA Private Key
$
private_key
=
new
phpseclib
\
Crypt
\
RSA
();
$
private_key
->
setPassword
(
$
pass_phrase
);
# skip if not encrypted
$
private_key
->
loadKey
(
'
-----BEGIN RSA PRIVATE KEY-----\n...
'
);
JOSE_JWK
::
encode
(
$
private_key
);
# => JOSE_JWK instance
Decode
RSA Public Key
# public key
$
components
=
array
(
'
kty
'
=>
'
RSA
'
,
'
e
'
=>
'
AQAB
'
,
'
n
'
=>
'
x9vNhcvSrxjsegZAAo4OEuo...
'
);
JOSE_JWK
::
decode
(
$
components
);
# => phpseclib\Crypt\RSA instance
RSA Private Key
Not supported.
Run Test
git clone git://github.com/nov/jose-php.git
cd
jose
php composer.phar install --dev
./vendor/bin/phpunit -c test/phpunit.xml --tap
Copyright
Copyright © 2013 Nov Matake & GREE Inc. See LICENSE for details.
About
PHP JOSE Library (JWT, JWS, JWE, JWK, JWK Set, JWK Thumbprint are supported)
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
139
stars
Watchers
8
watching
Forks
66
forks
Report repository
Releases
13
tags
Sponsor this project
Sponsor
Uh oh!
There was an error while loading.
Please reload this page
.
Learn more about GitHub Sponsors
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
PHP
98.9%
Ruby
1.1%