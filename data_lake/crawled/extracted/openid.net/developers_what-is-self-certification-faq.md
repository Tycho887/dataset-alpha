---
{
  "title": "What is Self-Certification (FAQ) - OpenID Foundation",
  "url": "https://openid.net/developers/what-is-self-certification-faq",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.31,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 12263,
  "crawled_at": "2026-04-23T20:55:03"
}
---

What is Self-Certification
Self-certification is a formal declaration by an entity that its identified deployment of a product or service conforms, through a process of conformance testing, to a specific conformance profile of the OpenID Connect protocol. Customers often need an assurance that their deployment conforms, and certification can help provide that assurance.
Learn more about conformance testing and self-certification
NOTICE: This OpenID Connect Certification Frequently Asked Questions (FAQ) document is designed to assist in understanding the concept of, process for, and rules applicable to self-certification of conformance with conformance profiles of the OpenID Connect protocol. This FAQ is subject to change at any time by the OpenID Foundation.
What is OpenID Connect self-certification?
Self-certification is a formal declaration by an entity that its identified deployment of a product or service conforms to a specific conformance profile of the OpenID Connect protocol.
Why are the benefits of certification?
Entities looking to use or rely on a deployment of a product or service that implements a specific conformance profile of the OpenID Connect protocol often need some assurance that the deployment actually conforms to the profile. A certification can help provide that assurance.
What certification profiles of OpenID Connect are available?
The conformance profiles of OpenID Connect are posted at OpenID Connect Conformance Profiles. The initial profiles are Basic OP, Implicit OP, Hybrid OP, OP Publishing Config Info, and Dynamic OP. The set of defined conformance profiles was expanded in December 2016 to include the corresponding RP profiles Basic RP, Implicit RP, Hybrid RP, RP Using Config Info, and Dynamic RP. Additional conformance profiles are also being planned for the future.
How does self-certification differ from third party certification?
In the case of self-certification, the party implementing a deployment of a product or service conducts its own review to determine whether its deployment complies with a specific conformance profile, and upon successful completion of such review, issues its own declaration of compliance.

In the case of third-party certification, someone other than the entity deploying the product or service (usually a specially accredited and trustworthy auditor or assessor authorized to conduct such a review) reviews, tests, assesses, and verifies that the entity’s deployment of the product or service conforms to a specific conformance profile, and then issues a statement to the effect that it has conducted the specified assessment, and certifies that the entity’s deployment of the product or service conforms to the specified conformance profile.

In the case of self-certification, the trustworthiness of the certification is a function of the trustworthiness of the entity that is assessing itself. In the case of third-party certification, the trustworthiness of the certification is a function of the trustworthiness of the assessing entities/certifying entity as well as the trustworthiness of the entity requesting the assessment.

Self-certification is also easier, quicker, and significantly cheaper than third-party certification.
Why is a self-certification trustworthy?
The trustworthiness of a self-certification is partially a function of the trustworthiness of the entity that is certifying itself, discounted, perhaps, by the self-interest involved. When an entity makes a self-certification, it puts its reputation on the line. In addition, it undertakes potential liability for damages suffered by those who rely on its self-certification in the event that the self-certification is not accurate. And it also exposes itself to potential liability under government regulatory statutes and regulations, such as laws that prohibit unfair and deceptive business practices.
What can be self-certified at the OpenID Foundation?
Any online deployment of a product or service that implements a conformance profile of the OpenID Connect protocol, or FAPI, FAPI-CIBA and a few more specifications as listed on the instructions is eligible for self-certification.
What about a deployment is being certified?
An entity that submits a self-certification to the OpenID Foundation is certifying that it has conducted specified testing of its deployment of a product or service, including the use of the OpenID Connect Software Test Suite, and that it has verified that its deployment conforms to one or more specific conformance profiles of the OpenID Connect protocol.
In Brazil, there are currently two separate directories for open banking and for open insurance but there are plans to merge to one. If a Brazil organization already has a FAPI certification for Open Banking Brazil, does that organization need to certify again for OPIN once there is one directory?
A different protocol endpoint is a different deployment and requires a separate certification thus requires additional certification fees. Also note that a different resource server qualifies as a different protocol end point.
Different underlying applications – in environments where there is one deployment to connect various internal applications to open world (e.g. different legacy systems for some customer segments). In the case of legacy applications, does an organization only have to certify the shell that is providing data to the open world?
A different protocol endpoint is a different deployment and requires a separate certification. Also note that a different resource server qualifies as a different protocol end point.
Who can self-certify?
Anyone is eligible to self-certify that their deployments of products or services implementing an OpenID Provider or Relying Party conform to generally available conformance profiles of the OpenID Connect protocol. The entity making the certification request must be affiliated with or responsible for the implementation being certified; it cannot be an unrelated party.

While a conformance profile is still in the pilot phase, certification to it is open only to OpenID Foundation members. The entity making the certification request must be an OpenID Foundation member, whether it be an organization or an individual. No fee is yet required for these certifications, since they are still in the pilot phase, during which we are “testing the tests”. Like certification to production conformance profiles, payment will be required once the pilot phase has been completed.
Do certifications expire?
They do not expire. The date that the certification was performed is part of the certification.
Who is operating the OpenID self-certification program?
The OpenID self-certification program is operated by the OpenID Foundation.
What is the status of the OpenID Connect self-certification program?
After its
launch in April 2015
, the certification program for OpenID Providers progressed from the pilot phase open to members to general availability to all in January 2016. The Relying Party certification program entered the pilot phase in December 2016 and progressed to general availability in August 2017. These production OpenID Provider profiles are generally available:
Basic OP
,
Implicit OP
,
Hybrid OP
,
Config OP
, and
Dynamic OP
. These production Relying profiles are generally available:
Basic RP
,
Implicit RP
,
Hybrid RP
,
Config RP
, and
Dynamic RP
.
NEW!
Conformance profiles for OPs and RPs implementing the
Form Post Response Mode
entered the pilot phase in June 2018. They are
Form Post OP
and
Form Post RP
. Please give them a try!
Certification to conformance profiles in the pilot phase is open to all OpenID Foundation members. Members interested in “testing the tests” should send a note to
certification@oidf.org
asking to be part of the certification pilot phase for new profiles.
Is payment of a fee required to self-certify?
A fee is required for certifications of both OpenID Providers and Relying Parties, unless the certification profile is still in the pilot phase. The fee is intentionally low, to encourage participation, but is there to help cover the ongoing costs of operating the certification program. See the
OpenID Certification Fee Schedule
page for the prices. Please pay for your certification application at the
Certification Payment
page when you send in your submission.
No fee is required for certifications to conformance profiles in the pilot phase, since for those we are still “testing the tests”. Payment will be required for new certifications to those profiles once the pilot phase has been completed and the profiles reach general availability.
If a top-level parent company joins the OpenID Foundation, do all subsidiaries including those that have different brands qualify for member certification fees?
If the subsidiary is majority owned by a company that is a member, regardless of brand, then the subsidiary qualifies for member pricing.
Is the Certification of Conformance legally binding?
Yes. By signing and submitting the Certification of Conformance, the organization is declaring both to the OpenID Foundation and to the general public the accuracy of the matters set forth in the Certification.
How is a self-certification publicized?
Self-certifications submitted to the OpenID Foundation are published at
http://openid.net/certification/
. Certified implementations are featured for developers at
http://openid.net/developers/certified/
. Announcements are also made from time to time on the
OpenID Foundation website
.
Who has access to data collected by the certification test suite?
Data collected from certification test runs for OpenID Connect certifications is publicly available. Data from certification test runs for FAPI certifications is, by default, only accessible by the tester and the OpenID certification team members who operate the test tool. FAPI testers do have the option to make their data public. All successful certifications and the testing data behind them are public.
How do we use the test data collected?
The certification team uses the test data collected to answer questions by testers. Defects observed in implementations being tested may be used as motivation to create new tests or update existing ones to detect similar defects during future test runs, which benefits all future testers. The certification team does not disclose the identities of testers or implementations experiencing problems.
What if I have more questions or want to file a bug report?
Any questions can be sent to
certification@oidf.org
. Certification software bugs are tracked in this
issue tracker
.
What consideration is given for certifying open source projects?
The OpenID Foundation board of directors approved and published the
Open Source Project Certification Policy
in June 2021. It provides for no-cost certifications for open source projects meeting defined criteria.
What is the Third-Party Support Certification Policy & List of Available Consultants?
The OpenID Foundation board of directors approved and published the
Third-Party Support Certification Policy
and initial list of available consultants in June 2021. The certification program team is not resourced to provide consulting services or specific guidance on OpenID specifications, but rather, is narrowly focused on helping those seeking certification understand the process, from performing the tests and interpreting the results through to submitting your self-certification request. If you or your organization require expertise in understanding OpenID specifications or how to successfully configure and deploy, there is a non-exclusive list of consultants available to assist you below, some of whom are also contractors on the OpenID Certification team.
Criteria for being listed as an available consultant:
OpenID Foundation member in good standing — organization or individual
Contributor to a prior successful OpenID certification
Successful OpenID certifications – list of successful certifications (e.g. Connect, FAPI, etc.) to highlight specific expertise
Languages fluent – spoken languages fluent as this will be become increasingly important as the Foundation and FAPI scale globally
Please send a request to be listed as an available consultant to
certification@oidf.org.