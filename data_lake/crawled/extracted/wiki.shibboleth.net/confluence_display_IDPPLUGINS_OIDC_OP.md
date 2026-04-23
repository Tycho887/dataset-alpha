---
{
  "title": "OIDC OP - Identity Provider Plugins - Confluence",
  "url": "https://wiki.shibboleth.net/confluence/display/IDPPLUGINS/OIDC+OP",
  "domain": "wiki.shibboleth.net",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 13782,
  "crawled_at": "2026-04-23T21:01:38"
}
---

OIDC OP
By Scott Cantor
6 min
Add a reaction
1
Overview
1.1
Implemented specifications
2
Plugin Installation
2.1
Dependencies
3
Enabling the Module
4
Initial Setup
4.1
First Steps
4.2
Key Generation
4.3
OIDC Issuer and Discovery
4.4
Enabling Profiles
4.5
Claim Setup
4.6
Example RP
5
Full Configuration
6
Use Cases
Overview
The OIDC OP plugin is the successor to the original GEANT-funded add-on to Shibboleth and is now available as an offically-supported plugin for IdP V4.1 and above. It provides conformant OIDC OP functionality alongside the SAML and CAS support previously native to the IdP software.
Starting with V3.1, the plugin also includes support for some OAuth 2 features, acting as a more generalized Authorization Service in the OAuth framework.
Please review the
https://shibboleth.atlassian.net/wiki/spaces/IDPPLUGINS/pages/2776760321
when installing or upgrading a new version.
V3.0 is the first release with code packages, XML namespaces, and other configuration elements native to the Shibboleth Project and with a "stable" configuration that will be supported in accordance with our
versioning policy
. It leverages the
plugin
extension model introduced in V4.1.
Because of significant changes to the configuration (largely to automate or simplify the overall process of adding or removing this feature), there are a number of manual steps required to move from the older (pre-3.0) releases of this code to the new, "stable" version. These differences were unavoidable in the interest of preventing such complications in the future.
Those using the earlier V1.0 or V2.0 releases of this functionality (originally documented in
GitHub
) should refer to
OIDC OP Upgrading
for guidance on moving to this new release.
Implemented specifications
OpenID Connect
Core:
https://openid.net/specs/openid-connect-core-1_0.html
Discovery:
https://openid.net/specs/openid-connect-discovery-1_0.html
(Provider Metadata)
Dynamic Client Registration:
https://openid.net/specs/openid-connect-registration-1_0.html
(Client Metadata and Registration Endpoint)
RP-Initiated Logout
4.1
:
https://openid.net/specs/openid-connect-rpinitiated-1_0-final.html
Front-Channel Logout
4.1
:
https://openid.net/specs/openid-connect-frontchannel-1_0.html
Back-Channel Logout
4.1
:
https://openid.net/specs/openid-connect-backchannel-1_0.html
OAuth2
RFC6750:
https://www.rfc-editor.org/rfc/rfc6750.html
RFC7009:
https://www.rfc-editor.org/rfc/rfc7009.html
RFC7636:
https://www.rfc-editor.org/rfc/rfc7636.html
RFC7662:
https://www.rfc-editor.org/rfc/rfc7662.html
RFC8707
3.2
:
https://www.rfc-editor.org/rfc/rfc8707.html
RFC9068
3.2
:
https://www.rfc-editor.org/rfc/rfc9068.html
RFC9101
4.2
:
https://www.rfc-editor.org/rfc/rfc9101.html
RFC9126
4.2
:
https://www.rfc-editor.org/rfc/rfc9126.html
RFC9207
3.2
:
https://www.rfc-editor.org/rfc/rfc9207.html
RFC9449
4.2
:
https://www.rfc-editor.org/rfc/rfc9449.html
Plugin Installation
Starting with IdP 4.2 you can the install the latest plugin version supported on your IdP version with
.\plugin.sh -I net.shibboleth.idp.plugin.oidc.op
Plugin
Plugin ID
Module(s)
Depends on
Bug Reporting
Plugin
Plugin ID
Module(s)
Depends on
Bug Reporting
OIDC OP Extension
net.shibboleth.idp.plugin.oidc.op
idp.oidc.OP.6
idp.oidc.config.5
https://shibboleth.atlassian.net/browse/JOIDC
Please review the
https://shibboleth.atlassian.net/wiki/spaces/IDPPLUGINS/pages/2776760321
when installing or updating this plugin.
Dependencies
This plugin depends on the Shibboleth OIDC Common plugin, and you must first install
OIDCCommon
. The installer will prevent installation if this is not in place.
Since version 3.4.0, you must also install
OIDCConfig
.
Plugin Installation Example
For a detailed guide on how to install plugins, see
https://shibboleth.atlassian.net/wiki/spaces/IDP5/pages/3199500688
.
In summary, use the
plugin
command that ships with the IdP to install the plugin from either a local file pre-downloaded, from a URL or by pluginId.
Installation
C:>\opt\shibboleth-idp\bin\plugin.bat -I net.shibboleth.idp.plugin.oidc.whatever
or
$ /opt/shibboleth-idp/bin/plugin.sh -i http://shibboleth.net/downloads/identity-provider/plugins/pluginName/version/URL
or
$ /opt/shibboleth-idp/bin/plugin.sh -i <plugin.tar.gz>
If installing from a local file, you need to ensure the GPG detached signature (e.g. the .asc file) is placed alongside the main plugin archive on disk.
Listing Installed Plugins
$ /opt/shibboleth-idp/bin/plugin.sh -l
or
C:>\opt\shibboleth-idp\bin\plugin.bat -l
Enabling the Module
For a detailed guide on configuring modules, see the
ModuleConfiguration
topic. Once the plugin has been installed, its module should be enabled automatically for you:
Check Module Is Enabled
/%{idp.home}/bin$ ./module.sh -l
...
Module: idp.oidc.OP [ENABLED]
However, if you need to enable it you can using the
module
command:
Enable the module
/%{idp.home}/bin$ ./module.sh -e idp.oidc.OP
When enabled, a number of new configuration files will be created for further customization.
Systems upgraded to V4.1 are also likely to require adding the
idp.searchForProperties=true
property to their
idp.properties
file, or else an explicit reference would have to be added to the new property file added by the module. It's best to clean up the property loading situation prior to using plugins that add their own.
Initial Setup
Because this plugin is considerably more extensive than most, there are more touchpoints to the rest of the IdP configuration and a larger-than-usual set of initial setup steps needed before it can be used. The IdP may not even startup properly until some of them are completed.
First Steps
Add an import statement to
conf/credentials.xml
:
<!-- OIDC extension default credential definitions -->
<import resource="oidc-credentials.xml" />
Adjust or add the
idp.searchForProperties
setting in idp.properties and set it to true to auto-locate and load the new properties file. This will extend to other new features in the future, so makes adding and removing new functionality simpler.
If you want to leverage the new default claim mapping rules, you can add an import to
conf/attributes/default-rules.xml
:
<import resource="oidc-claim-rules.xml" />
The impact of this is to reduce the need for
<AttributeDefinition>
and
<AttributeEncoder>
elements in your
Attribute Resolver
configuration when adhering to "default" expectations for the names of attributes and how they map into OIDC claims. We encourage this as it makes things simpler and more consistent but it isn't mandatory.
The additional files created in
conf/examples
(
oidc-attribute-resolver.xml
and
oidc-attribute-filter.xml
) are intended as a source of examples to copy into your own files. The most critical definitions needed are the rules for creating and releasing the "sub" claim, as that is a required OIDC feature (see
OIDC OP#ClaimSetup
). If you want to use the example files directly (unlikely), you can copy them elsewhere and make use of them as you see fit.
Key Generation
The OP plugin supports keys in the JWK format as well as the more typical PEM format. There are some advantages to using the JWK format in optimizing which keys are tried in certain cases. There is no particular advantage to reusing any existing keys your IdP may be using, but you can if you prefer to do so.
The default configuration expects to have two RSA keys (one for signing and one for decryption), and one EC key. They are expected to be in locations defined via the following properties (with the shipping defaults shown):
idp.signing.oidc.rs.key
- %{idp.home}/credentials/idp-signing-rs.jwk
idp.signing.oidc.es.key
-%{idp.home}/credentials/idp-signing-es.jwk
idp.signing.oidc.rsa.enc.key
- %{idp.home}/credentials/idp-encryption-rsa.jwk
Keys may be generated using the provided wrappers, in
bin/jwtgen.sh
and
bin/jwtgen.bat
:
Key Generation Example
$ cd /opt/shibboleth-idp
$ bin/jwtgen.sh -t RSA -s 2048 -u sig -i defaultRSASign | tail -n +2 > credentials/idp-signing-rs.jwk
$ bin/jwtgen.sh	-t EC -c P-256 -u sig -i defaultECSign | tail -n +2 > credentials/idp-signing-es.jwk
$ bin/jwtgen.sh	-t RSA -s 2048 -u enc -i defaultRSAEnc | tail -n +2 > credentials/idp-encryption-rsa.jwk
Key Generation for ES384 and ES512
The example above doesn’t contain compatible keys for the ES384 and ES512 signing algorithms. They can be generated for instance in the following way
$ cd /opt/shibboleth-idp
$ bin/jwtgen.sh -t EC -c P-384 -u sig -i defaultEC384Sign | tail -n +2 > credentials/idp-signing-es384.jwk
$ bin/jwtgen.sh -t EC -c P-521 -u sig -i defaultEC512Sign | tail -n +2 > credentials/idp-signing-es512.jwk
Similarly to the other credentials, they need to be defined in
conf/oidc-credentials.xml
. For the example credentials above, the following bean definitions work:
...
<bean id="shibboleth.oidc.DefaultES384SigningCredential" parent="shibboleth.JWKCredential"
p:resource="/opt/shibboleth-idp/credentials/idp-signing-es384.jwk" />
<bean id="shibboleth.oidc.DefaultES512SigningCredential" parent="shibboleth.JWKCredential"
p:resource="/opt/shibboleth-idp/credentials/idp-signing-es512.jwk" />
...
They need to be referred in the list of enabled signing credentials specified by
shibboleth.oidc.SigningCredentials
.
OIDC Issuer and Discovery
The OIDC "issuer" value needs to be determined, and the OpenID discovery document needs to be made accessible.
The issuer value is set in
conf/oidc.properties
and must be a URL using the "https" scheme that contains host, and optionally, port number and path components and no query or fragment components. It generally must resolve to the root of the deployment in question. As a result, while it may be the same as one's SAML entityID, it often cannot be, as SAML does not conflate identity and location in this fashion.
conf/oidc.properties
idp.oidc.issuer = https://your.issuer.example.org
A common way for clients to configure themselves against an OP is to read the openid-configuration resource as defined in
https://openid.net/specs/openid-connect-discovery-1_0.html
.
A template for this file is created in
static/openid-configuration.json.
You will need to update it to match your configuration. At minimum this means replacing "{{ service_name }}" with the host portion of your issuer value.
In order for clients to locate the file, you will either have to:
Configure your Java container or other web server "front-end" to publish it at this exact location (obviously the prefix depends on your issuer value):
https://your.issuer.example.org/.well-known/openid-configuration
Or (more typically), configure that location to route into your IdP at
/idp/profile/oidc/configuration
to generate the document more dynamically.
The
OPDiscovery
topic describes this further.
Enabling Profiles
Activating support for OIDC, as with other protocols supported, requires adjusting the
RelyingPartyConfiguration
in
conf/relying-party.xml
.
One of the profiles (the one that advertises keys) needs to be openly accessible:
conf/relying-party.xml
<bean id="shibboleth.UnverifiedRelyingParty" parent="RelyingParty">
<property name="profileConfigurations">
<list>
<ref bean="OIDC.Keyset" />
</list>
</property>
</bean>
The rest are functional profiles that may be enabled more selectively but would normally be enabled by default:
conf/relying-party.xml
<bean id="shibboleth.DefaultRelyingParty" parent="RelyingParty">
<property name="profileConfigurations">
<list>
<ref bean="OIDC.SSO" />
<ref bean="OIDC.UserInfo"/>
<ref bean="OAUTH2.Token"/>
<ref bean="OAUTH2.Revocation"/>
<ref bean="OAUTH2.Introspection" />
</list>
</property>
</bean>
Obviously this relies on a lot of defaulted behavior, but the full documentation includes more detailed information about how to adjust profile settings.
Claim Setup
Attributes in OIDC are termed claims, but the IdP treats them just as in other protocols, with the usual
resolution
and
filtering
approaches. You will need to reference that documentation early on in the testing process and you will also want to take some care regarding
the "sub" claim
.
Example RP
For initial testing, it's helpful to start simple and add an example RP by hand. There are several different ways of managing RP registration data, but for a quick test, the simplest is to add some static JSON to the system to define a test system.
There are some commented options in
conf/oidc-clientinfo-resolvers.xml
that can be uncommented to supply an example JSON file to load:
conf/oidc-clientinfo-resolvers.xml
<util:list id="shibboleth.oidc.ClientInformationResolvers">
<!-- Uncommented -->
<ref bean="ExampleFileResolver" />
<ref bean="ExampleStorageClientInformationResolver" />
</util:list>
<!-- Uncommented -->
<bean id="ExampleFileResolver" parent="shibboleth.oidc.FilesystemClientInformationResolver"
c:metadata="%{idp.home}/metadata/oidc-client.json" />
This in turn allows you to statically define a JSON array of client registrations in a file:
metadata/oidc-client.json
[
{
"scope":"openid email",
"redirect_uris":["https://demorp.example.org/redirect_uri"],
"client_id":"demo_rp",
"client_secret":"topsecret",
"response_types":["code"],
"grant_types":["authorization_code"]
}
]
You will of course need to adjust the JSON to match the client you are testing, for which the
documentation
should help.
Full Configuration
Please refer to the topics below for more detailed information on different aspects of the extension.
Client Registration (
Metadata
and
Dynamic
)
Client Resolution
User Authentication
Client Authentication
Attribute/Claims Resolution
The "sub" Claim
Attribute Filtering
Security Configuration
Profile Configuration
OP Discovery
Use Cases
Client Credentials Grant
Authorization Code Affinity
Collapse action bar
View all comments
Open Details Panel
Open Rovo Chat
Add a comment
Add a reaction