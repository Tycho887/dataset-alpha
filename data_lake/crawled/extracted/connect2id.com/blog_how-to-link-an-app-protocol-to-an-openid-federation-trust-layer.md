---
{
  "title": "\n    \n    \n    \n        \n            \n                How to link an application protocol to an OpenID Federation 1.0 trust layer · Blog · Connect2id\n            \n        \n    \n",
  "url": "https://connect2id.com/blog/how-to-link-an-app-protocol-to-an-openid-federation-trust-layer",
  "domain": "connect2id.com",
  "depth": 2,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 9125,
  "crawled_at": "2026-04-23T20:50:13"
}
---

OpenID Federation
How to link an application protocol to an OpenID Federation 1.0 trust layer
Vladimir Dzhuvinov / Connect2id -
4 December 2024
This table may seem simple, but it took months if not years to arrive at. It
synthesizes all the discussions, writings, and proposals on how to bind an
application protocol to the trust layer of
OpenID
Federation
, while addressing the diverse and
sometimes opposing expectations that adopters have on this topic.
Method
Suitable for
Guarantees
OAuth / OIDC parameter
Federation Integrity
Metadata Integrity
Self and peer Entity ID
Simple federation topologies
Federation and metadata integrity not required
Only in federations rooted at a single Trust Anchor
Only in federations with tree topologies below the Trust Anchors
client_id=<entity-id>
Self and peer Trust Chain
Any federation topology
✅
✅
self_trust_chain=[...]
peer_trust_chain=[...]
The table lays out a principle how two entities that use some application
protocol, say
OpenID Connect
for user authentication
and SSO, can establish trust using OpenID Federation, and what parameters need
to pass in the application layer, in order to bind a request to the trust
layer.
Entity ID
When Roland Hedberg invented the concept of the trust chain for OpenID Connect
federations, the minimal coupling between the trust infrastructure (federation
entities, their APIs and JWTs) and the OpenID authentication requests
immediately appealed to me. The client application only has to set the
client_id
in the request to its federation entity ID (a resolvable URL, like
https://app.example.com
). This then enables a piece of “magic” so that the
client can make requests to federated OpenID providers without a prior
registration step
. This is
called
automatic
registration
.
Prior to the actual request the client resolves an acceptable trust chain for
the OpenID provider, starting with the provider’s entity ID which is the issuer
URL in the
OpenID provider
metadata
,
in its
ID tokens
and other issued JWTs. The
OpenID provider performs a similar trust evaluation for the client, which input
is the entity ID from the
client_id
request parameter.
When is the client entity ID sufficient in requests?
In federations that by the nature of their topology guarantee the properties
of
federation integrity
and
metadata integrity
.
When the
federation integrity
and
metadata integrity
properties are
not required. This may surprise you, but not having federation integrity can
sometimes be seen as an enabling feature! This can be the topic of another
article.
What exactly is
federation integrity
?
This ensures mutual trust between two entities is established always from a
common trust anchor. Any resolved metadata and policies that govern the client
application and the OpenID provider in a transaction will then fall under the
rules of the same federation and thus will be aligned and consistent with one
another.
What is
metadata integrity
?
This property is related. It ensures the trust chains for an entity to a given
trust anchor will invariably result in consistent metadata and policies. The
natural way to achieve this is for the federation topology under a trust anchor
to form a tree. Topologies that lead to multiple paths from a leaf entity to a
trust anchor are to be avoided.
To sum up, the integrity properties make sure a transaction or application
request is governed always by the rules of a single federation and that when
the rules get applied to an entity in the federation, this will be done
consistently and predictably.
When to pass trust chains or paths
As illustrated by issues
7
,
86
and
100
raised with the OpenID Federation draft, federation topologies that challenge
or break the integrity properties are entirely possible.
Here is an example topology of two interlinked federations. Imagine user Alice
wants to log into a web application (labeled as OpenID relying party, or RP)
using her preferred OpenID provider (labeled as OP).
.-----------------.           .-----------------.
|  Trust Anchor A |           |  Trust Anchor B |
'------.--.-------'           '----.--.--.------'
       |  |                        |  |  |
    .--'  '---. .------------------'  |  |
    |         | |                     |  |
.---v.  .-----v-v------.   .----------'  |
|    |  | Intermediate |   |             |
'----'  '--.--.--.-----'   |     .-------v------.
           |  |  |         |     | Intermediate |
   .-------'  |  '------.  |     '---.--.--.----'
   |          |         |  |         |  |  |
.--v-.      .-v--.     .v--v.    .---'  |  '--.
| RP |      |    |     | OP |    |      |     |
'----'      '----'     '----' .--v-. .--v-. .-v--.
                              |    | |    | |    |
                              '----' '----' '----'
The application and the OpenID provider have a common direct federation
intermediate above them, but remember that the decision who to trust in a
federation hinges on one or more accepted trust anchors.
If the RP has A as its trust anchor it may obtain a single trust chain for the
OpenID provider, which chain passes through their common intermediate and ends
in the trust anchor.
If the RP has A and B as its anchors, it may end up obtaining three trust
chains for the OpenID provider, one anchored in A and two anchored in B.
When we take the OpenID provider side, it could similarly build not one but
multiple trust chains for the RP, depending on its own trust anchor
configuration.
Under these circumstances, when the client application makes an OpenID
authentication request and the
client_id
is simply set to its entity ID, the
RP is not able to say which trust chain it selected for the OP, and vice versa,
which trust chain the OP will end up using to evaluate and register the RP.
Why is this a potential problem?
Suppose the federation anchored in A is intended for simple, general purpose
login, while the federation anchored in B is for
verified
identity
provision and has
special metadata policies for user verification and strong client
authentication. When Alice wants to sign into the client application with a
verified identity both RP and OP must be on the same page, i.e. use the same
conforming OpenID Connect profile, as defined by trust anchor B with its
metadata and policies. Else the OpenID Connect request may fail or produce
unexpected results. If, for example, the client tries to authenticate with a
method intended for the other federation, or an ID token with an unexpected
signing algorithm is received.
Interlinked and multi-anchored federations are a not an uncommon scenario and
we don’t assume or expect the real world to translate to topologies that will
naturally enforce the federation integrity and metadata integrity properties.
In fact, in interlinked federations this is likely not going to be case.
Fortunately, there is a simple and elegant way to guarantee these two
properties, should they matter, regardless of what complexity a federation has
taken.
If we go back to the example with Alice and the verified identity login, all
the client application has to do is to include these two trust chains in the
request to the OpenID provider:
self_trust_chain
– A trust chain for the RP which ends in trust anchor B,
the intended anchor for verified identity applications.
peer_trust_chain
– The trust chain which the RP used to successfully
establish trust in the OP and selected to proceed with.
Upon receiving the request the OpenID provider will not try to build a trust
chain from scratch for the RP, by starting from its entity ID in the
client_id
. Instead, it will take the supplied
self_trust_chain
and verify
it, using the public key of trust anchor B. To find out what OpenID provider
metadata the RP has resolved for the OP, it will use the other chain, the
peer_trust_chain
. This chain can be validated in the exact same way, using
the trust anchor B public key.
If the OpenID provider doesn’t accept the trust chains anchor, or their
validation failed for some reason, it will reject the request with an error
invalid_trust_anchor
,
invalid_trust_chain
or
invalid_metadata
.
This method for binding application layer requests to the trust layer is simple
and capable of handling arbitrary federation topologies. The two trust chains
can be obtained from a resolver, or using the classic method of collecting the
JWTs from every entity along the trust path.
Optimisations
Passing the entity IDs along the trust paths instead of the complete JWTs can
be an optimisation to keep the request from inflating. Note that in this case
the peer, the OpenID provider, will have to collect the necessary JWTs along
the two paths in order to recreate the trust chains, or call upon a resolver.
This optimisation is therefore a trade-off that reduces the request size but
requires the OP to perform additional network operations.
Other optimisations, like referencing the trust chains by URL and caching them
are possible.
To keep things basic the core
OpenID Federation
1.0
spec likely won’t
include or mention possible optimisations. They may be the subject of
extensions and application-specific profiles.