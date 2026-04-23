---
{
  "title": "OpenID RISC Profile Specification 1.0 - draft 02",
  "url": "https://openid.net/specs/openid-risc-profile-specification-1_0.html",
  "domain": "openid.net",
  "depth": 1,
  "relevance_score": 0.43,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 15406,
  "crawled_at": "2026-04-23T20:50:33"
}
---

OpenID RISC Profile Specification 1.0 - draft 02
M. Scurtescu
Coinbase
A. Backman
Amazon
P. Hunt
Oracle
J. Bradley
Yubico
S. Bounev
VeriClouds
A. Tulshibagwale
SGNL
April 05, 2022
OpenID RISC Profile Specification 1.0 - draft 02
openid-risc-profile-specification-1_0
Abstract
This document defines the Risk Incident Sharing and Coordination (RISC) Event Types based on the
Shared Signals and Events (SSE) Framework
. Event Types are introduced and defined in
Security Event Token (SET)
.
Table of Contents
1.
Introduction
1.1.
Notational Conventions
2.
Event Types
2.1.
Account Credential Change Required
2.2.
Account Purged
2.3.
Account Disabled
2.4.
Account Enabled
2.5.
Identifier Changed
2.6.
Identifier Recycled
2.7.
Credential Compromise
2.8.
Opt Out
2.8.1.
Opt In
2.8.2.
Opt Out Initiated
2.8.3.
Opt Out Cancelled
2.8.4.
Opt Out Effective
2.9.
Recovery Activated
2.10.
Recovery Information Changed
2.11.
Sessions Revoked
3.
Compatibility
3.1.
Google Subject Type Value
4.
Normative References
Appendix A.
Acknowledgements
Appendix B.
Notices
Authors' Addresses
1.
Introduction
This specification defines event types and their contents based on the
SSE Framework
that are required to implement Risk Incident Sharing and Coordination.
1.1.
Notational Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14
[RFC2119]
[RFC8174]
when, and only when, they appear in all capitals, as shown here.
2.
Event Types
The base URI for RISC event types is:
https://schemas.openid.net/secevent/risc/event-type/
2.1.
Account Credential Change Required
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/account-credential-change-required
Account Credential Change Required signals that the account identified by the subject was required to change a credential. For example the user was required to go through a password change.
Attributes: none
{
  "iss": "https://idp.example.com/",
  "jti": "756E69717565206964656E746966696572",
  "iat": 1508184845,
  "aud": "636C69656E745F6964",
  "events": {
    "https://schemas.openid.net/secevent/risc/event-type/\
    account-credential-change-required": {
      "subject": {
        "format": "iss_sub",
        "iss": "https://idp.example.com/",
        "sub": "7375626A656374",
      }
    }
  }
}
(the event type URI is wrapped, the backslash is the continuation character)
Figure 1: Example: Account Credential Change Required
2.2.
Account Purged
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/account-purged
Account Purged signals that the account identified by the subject has been permanently deleted.
Attributes: none
2.3.
Account Disabled
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/account-disabled
Account Disabled signals that the account identified by the subject has been disabled. The actual reason why the account was disabled might be specified with the nested
reason
attribute described below. The account may be
enabled
in the future.
Attributes:
reason - optional, describes why was the account disabled. Possible values:
hijacking
bulk-account
{
  "iss": "https://idp.example.com/",
  "jti": "756E69717565206964656E746966696572",
  "iat": 1508184845,
  "aud": "636C69656E745F6964",
  "events": {
    "https://schemas.openid.net/secevent/risc/event-type/\
    account-disabled": {
      "subject": {
        "format": "iss_sub",
        "iss": "https://idp.example.com/",
        "sub": "7375626A656374",
      },
      "reason": "hijacking",
    }
  }
}
(the event type URI is wrapped, the backslash is the continuation character)
Figure 2: Example: Account Disabled
2.4.
Account Enabled
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/account-enabled
Account Enabled signals that the account identified by the subject has been enabled.
Attributes: none
2.5.
Identifier Changed
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/identifier-changed
Identifier Changed signals that the identifier specified in the subject has changed. The subject type MUST be either
email
or
phone
and it MUST specify the old value.
This event SHOULD be issued only by the provider that is authoritative over the identifier.  For example, if the person that owns
john.doe@example.com
goes through a name change and wants the new
john.row@example.com
email then
only
the email provider
example.com
SHOULD issue an Identifier Changed event as shown in the example below.
If an identifier used as a username or recovery option is changed, at a provider that is not authoritative over that identifier, then
Recovery Information Changed
SHOULD be used instead.
Attributes:
new-value - optional, the new value of the identifier.
{
  "iss": "https://idp.example.com/",
  "jti": "756E69717565206964656E746966696572",
  "iat": 1508184845,
  "aud": "636C69656E745F6964",
  "events": {
    "https://schemas.openid.net/secevent/risc/event-type/\
    identifier-changed": {
      "subject": {
        "format": "email",
        "email": "john.doe@example.com",
      },
      "new-value": "john.roe@example.com",
    }
  }
}
The
foo@example.com
email changed to
bar@example.com
.
(the event type URI is wrapped, the backslash is the continuation character)
Figure 3: Example: Identifier Changed
2.6.
Identifier Recycled
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/identifier-recycled
Identifier Recycled signals that the identifier specified in the subject was recycled and now it belongs to a new user. The subject type MUST be either
email
or
phone
.
Attributes: none
{
  "iss": "https://idp.example.com/",
  "jti": "756E69717565206964656E746966696572",
  "iat": 1508184845,
  "aud": "636C69656E745F6964",
  "events": {
    "https://schemas.openid.net/secevent/risc/event-type/\
    identifier-recycled": {
      "subject": {
        "format": "email",
        "email": "foo@example.com",
      }
    }
  }
}
The 'foo@example.com' email address was recycled.
(the event type URI is wrapped, the backslash is the continuation character)
Figure 4: Example: Identifier Recycled
2.7.
Credential Compromise
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/credential-compromise
A Credential Compromise event signals that the identifier specified in the subject was found to be compromised.
Attributes:
credential_type - REQUIRED. The type of credential that is compromised. The value of this attribute must be one of the values specified for the similarly named field in the
Credential Change
event defined in the
CAEP Specification
.
event_timestamp - OPTIONAL. JSON number: the time at which the event described by this SET was discovered by the Transmitter. Its value is a JSON number representing the number of seconds from 1970-01-01T0:0:0Z as measured in UTC until the date/time.
reason_admin - OPTIONAL. The reason why the credential compromised event was generated, intended for administrators
reason_user - OPTIONAL. The reason why the credential compromised event was generated, intended for end-users
{
     "iss": "https://idp.example.com/3456790/",
     "jti": "756E69717565206964656E746966696572",
     "iat": 1508184845,
     "aud": "https://sp.example2.net/caep",
     "events": {
       "https://schemas.openid.net/secevent/risc/event-type/credential-compromise": {
         "subject": {
           "format": "iss_sub",
           "iss": "https://idp.example.com/3456790/",
           "sub": "joe.smith@example.com"
         },
        "credential_type": "password"
       }
     }
   }
(the event type URI is wrapped, the backslash is the continuation character)
Figure 5: Example: Compromised credential found
2.8.
Opt Out
Users SHOULD be allowed to opt-in and out of RISC events being sent for their accounts. With regards to opt-out an account can be in one of these three states:
opt-in - the account is participating in RISC event exchange.
opt-out-initiated - the user requested to be excluded from RISC event exchanges, but for practical security reasons for a period of time RISC events are still exchanged. The main reason for this state is to prevent a hijacker from immediately opting out of RISC.
opt-out - the account is NOT participating in RISC event exchange.
State changes trigger Opt-Out Events as represented bellow:
+--------+  opt-out-initiated  +-------------------+
|        +--------------------->                   |
| opt-in |                     | opt-out-initiated |
|        |  pt-out-cancelled   |                   |
|        <---------------------+                   |
+---^----+                     +----------+--------+
    |                                     |
    | opt-in                              | opt-out-effective
    |                                     |
    |                          +----------V--------+
    |                          |                   |
    +--------------------------| opt-out           |
                               |                   |
                               +-------------------+
Figure 6: Opt-Out States and Opt-Out Events
Both Transmitters and Receivers SHOULD manage Opt-Out state for users. Transmitters should send the events defined in this section when the Opt-Out state changes.
2.8.1.
Opt In
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/opt-in
Opt In signals that the account identified by the subject opted into RISC event exchanges.  The account is in the
opt-in
state.
Attributes: none
2.8.2.
Opt Out Initiated
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/opt-out-initiated
Opt Out Initiated signals that the account identified by the subject initiated to opt out from RISC event exchanges. The account is in the
opt-out-initiated
state.
Attributes: none
2.8.3.
Opt Out Cancelled
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/opt-out-cancelled
Opt Out Cancelled signals that the account identified by the subject cancelled the opt out from RISC event exchanges. The account is in the
opt-in
state.
Attributes: none
2.8.4.
Opt Out Effective
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/opt-out-effective
Opt Out Effective signals that the account identified by the subject was effectively opted out from RISC event exchanges. The account is in the
opt-out
state.
Attributes: none
2.9.
Recovery Activated
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/recovery-activated
Recovery Activated signals that the account identified by the subject activated a recovery flow.
Attributes: none
2.10.
Recovery Information Changed
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/recovery-information-changed
Recovery Information Changed signals that the account identified by the subject has changed some of its recovery information. For example a recovery email address was added or removed.
Attributes: none
2.11.
Sessions Revoked
Note: This event type is now deprecated. New implementations MUST use the
session-revoked
event defined in the
CAEP Specification
.
Event Type URI:
https://schemas.openid.net/secevent/risc/event-type/sessions-revoked
Sessions Revoked signals that all the sessions for the account identified by the subject have been revoked.
Attributes: none
3.
Compatibility
3.1.
Google Subject Type Value
Implementers are hereby made aware that the existing RISC implementation by Google uses the field name
subject_type
instead of the field name
format
to indicate the format of the subject identifier. The usage of the field name
subject_type
is deprecated and new services MUST NOT use this field name.
Relying parties wishing to receive events from the Google RISC transmitter therefore need to have code to work around this, until such time as their implementation is updated. Any such workaround should be written in a manner that does not break if Google updates their implementation to conform to this specification.
4.
Normative References
[CAEP-SPECIFICATION]
Cappalli, T.
and
A. Tulshibagwale
, "
OpenID Continuous Access Evaluation Profile 1.0 - draft 01
", June 2021.
[RFC2119]
Bradner, S.
, "
Key words for use in RFCs to Indicate Requirement Levels
", BCP 14, RFC 2119, DOI 10.17487/RFC2119, March 1997.
[RFC8174]
Leiba, B.
, "
Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words
", BCP 14, RFC 8174, DOI 10.17487/RFC8174, May 2017.
[SET]
Hunt, P.
,
Jones, M.
,
Denniss, W.
and
M. Ansari
, "
Security Event Token (SET)
", April 2018.
[SSE-FRAMEWORK]
Tulshibagwale, A.
,
Cappalli, T.
,
Scurtescu, M.
,
Backman, A.
and
J. Bradley
, "
OpenID Shared Signals and Events Framework Specification 1.0
", June 2021.
Appendix A.
Acknowledgements
The authors wish to thank all members of the OpenID Foundation Shared Signals and Events Working Group who contributed to the development of this specification.
Appendix B.
Notices
Copyright (c) 2022 The OpenID Foundation.
The OpenID Foundation (OIDF) grants to any Contributor, developer, implementer, or other interested party a non-exclusive, royalty free, worldwide copyright license to reproduce, prepare derivative works from, distribute, perform and display, this Implementers Draft or Final Specification solely for the purposes of (i) developing specifications, and (ii) implementing Implementers Drafts and Final Specifications based on such documents, provided that attribution be made to the OIDF as the source of the material, but that such attribution does not indicate an endorsement by the OIDF.
The technology described in this specification was made available from contributions from various sources, including members of the OpenID Foundation and others.  Although the OpenID Foundation has taken steps to help ensure that the technology is available for distribution, it takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this specification or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any independent effort to identify any such rights.  The OpenID Foundation and the contributors to this specification make no (and hereby expressly disclaim any) warranties (express, implied, or otherwise), including implied warranties of merchantability, non-infringement, fitness for a particular purpose, or title, related to this specification, and the entire risk as to implementing this specification is assumed by the implementer.  The OpenID Intellectual Property Rights policy requires contributors to offer a patent promise not to assert certain patent claims against other contributors and against implementers.  The OpenID Foundation invites any interested party to bring to its attention any copyrights, patents, patent applications, or other proprietary rights that may cover technology that may be required to practice this specification.
Authors' Addresses
Marius Scurtescu
Scurtescu
Coinbase
EMail:
marius.scurtescu@coinbase.com
Annabelle Backman
Backman
Amazon
EMail:
richanna@amazon.com
Phil Hunt
Hunt
Oracle Corporation
EMail:
phil.hunt@yahoo.com
John Bradley
Bradley
Yubico
EMail:
secevemt@ve7jtb.com
Stan Bounev
Bounev
VeriClouds
EMail:
stanb@vericlouds.com
Atul Tulshibagwale
Tulshibagwale
SGNL
EMail:
atul@sgnl.ai