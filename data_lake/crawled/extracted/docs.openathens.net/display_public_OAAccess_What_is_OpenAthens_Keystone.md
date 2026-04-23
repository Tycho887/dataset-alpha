---
{
  "title": "What is OpenAthens Keystone",
  "url": "https://docs.openathens.net/display/public/OAAccess/What+is+OpenAthens+Keystone",
  "domain": "docs.openathens.net",
  "depth": 2,
  "relevance_score": 0.23,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 2329,
  "crawled_at": "2026-04-23T21:01:05"
}
---

Skip table of contents
Introduction
OpenAthens Keystone is middleware that allows you to use the widespread and simple OpenID Connect software to participate in SAML federations around the world and easily allow institutional subscription to your content. SAML and the things that use it, such as Shibboleth, are great but can be complicated beasts to integrate into your systems - OpenID Connect is considerably simpler and you may already be using it.
What is OpenID Connect?
OpenID Connect (or OIDC) was introduced in 2014 by the OpenID Foundation to deliver a more API-friendly way of performing many of the same tasks as OpenID 2.0. This API-friendly approach is what makes it work well within native and mobile applications (as well as OpenAthens). If you're familiar with OAuth 2.0, then it's an authentication layer on top of that authorization framework. When you see a log in with Google option on a website, that's OpenID Connect.
There are versions available for all major platforms and many minor ones; most are quite straightforward to implement, and as I say: you may already be using it.
How is OpenID Connect different from OpenID or OAuth?
At the basic level, OpenID only does authentication - i.e. is the user who they say they are; OAuth is for finding out information about the user such as identifiers. OpenID Connect enables the authentication and the retrieval of information you can authorize on in one compact package.
What is OpenAthens?
OpenAthens (originally just Athens) was introduced in 1995 and was one of the first federated access management solutions in the world. It has evolved over time to embrace new technologies as they emerged, such as SAML and now OIDC.
Why do I want to join SAML federations using OpenAthens?
SAML federations are where you will find the customers who buy institutional subscriptions and site licenses such as universities, colleges, hospitals, government departments, corporations and multinationals.
You could connect to each subscriber individually of course, but if you're lucky that would mean hundreds or thousands of connections to manage. Federations standardize the interchange between the institution and the publisher. Keystone takes that to another level by putting all that behind one easy-to-code-for OIDC Provider that does all the hard work for you.
×