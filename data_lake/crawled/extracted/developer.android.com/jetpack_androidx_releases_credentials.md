---
{
  "title": "credentials  |  Jetpack  |  Android Developers",
  "url": "https://developer.android.com/jetpack/androidx/releases/credentials",
  "domain": "developer.android.com",
  "depth": 2,
  "relevance_score": 0.35,
  "extractor": "beautifulsoup",
  "author": "",
  "date": "",
  "length": 28856,
  "crawled_at": "2026-04-23T20:52:14"
}
---

Android Developers
Get started
Jetpack
Libraries
Stay organized with collections
Save and categorize content based on your preferences.
credentials
User Guide
API Reference
androidx.credentials
This library provides unified access to a user's credentials. This can include passwords, passkeys and federated credentials. This library should be used to provide seamless and secure sign-in experiences.
Latest Update
Stable Release
Release Candidate
Beta Release
Alpha Release
April 22, 2026
1.6.0
-
-
1.7.0-alpha01
Declaring dependencies
To add a dependency on credentials, you must add the Google Maven repository to
your project. Read
Google's Maven
repository
for more information.
Add the dependencies for the artifacts you need in the
build.gradle
file for
your app or module:
Kotlin
dependencies
{
implementation
(
"androidx.credentials:credentials:1.7.0-alpha01"
)
implementation
(
"androidx.credentials:credentials-play-services-auth:1.7.0-alpha01"
)
}
Groovy
dependencies
{
implementation
"androidx.credentials:credentials:1.7.0-alpha01"
implementation
"androidx.credentials:credentials-play-services-auth:1.7.0-alpha01"
}
For more information about dependencies, see
Add build dependencies
.
Feedback
Your feedback helps make Jetpack better. Let us know if you discover new issues or have
ideas for improving this library. Please take a look at the
existing issues
in this library before you create a new one. You can add your vote to an existing issue by
clicking the star button.
Create a new issue
See the
Issue Tracker documentation
for more information.
There are no release notes for this artifact.
Credentials Credentials-play-services-auth Version 1.7
Version 1.7.0-alpha01
April 22, 2026
androidx.credentials:credentials:1.7.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.7.0-alpha01
are released. Version 1.7.0-alpha01 contains
these commits
.
API Changes
Support large credential payloads for
getCredential
API
Credentials e2ee Version 1.0.
Version 1.0.0-alpha03
March 11, 2026
androidx.credentials:credentials-e2ee:1.0.0-alpha03
is released. Version 1.0.0-alpha03 contains
these commits
.
API Changes**
Deprecate
credentials:credentials-e2ee
(
I876f5
,
b/467132523
)
Version 1.0.0-alpha02
April 17, 2024
androidx.credentials:credentials-e2ee:1.0.0-alpha02
is released. This version contains source jars that were missing from the previous release.
Version 1.0.0-alpha01
April 3, 2024
androidx.credentials:credentials-e2ee:1.0.0-alpha01
is released. Version 1.0.0-alpha01 contains
these commits
.
New Features
Support for creating an
IdentityKey
from a passkey (
Iba31e
)
Credentials Credentials-play-services-auth Version 1.6
Version 1.6.0
April 08, 2026
androidx.credentials:credentials:1.6.0
and
androidx.credentials:credentials-play-services-auth:1.6.0
are released. Version 1.6.0 contains
these commits
.
Important changes since 1.5.0:
Fix propagation of
CreatePublicKeyCredentialRequest.isConditional
bit.
Version 1.6.0-rc02
February 25, 2026
androidx.credentials:credentials:1.6.0-rc02
and
androidx.credentials:credentials-play-services-auth:1.6.0-rc02
are released. Version 1.6.0-rc02 contains
these commits
.
Bug Fixes
Fixes the fall back mechanism for Pre-U create credential flow on devices with an unsupported GMSCore version.
Version 1.6.0-rc01
December 17, 2025
androidx.credentials:credentials:1.6.0-rc01
and
androidx.credentials:credentials-play-services-auth:1.6.0-rc01
are released. Version 1.6.0-rc01 contains
these commits
.
API Changes
Add APIs for the registration and clearance of creation options in Credential Manager. (
I01073
)
Added new Signal API Exception to indicate request is rate limited (
Ie2733
)
Version 1.6.0-beta03
October 22, 2025
androidx.credentials:credentials:1.6.0-beta03
and
androidx.credentials:credentials-play-services-auth:1.6.0-beta03
are released. Version 1.6.0-beta03 contains
these commits
.
New Features
Minor internal data serialization changes
Version 1.6.0-beta02
October 08, 2025
androidx.credentials:credentials:1.6.0-beta02
and
androidx.credentials:credentials-play-services-auth:1.6.0-beta02
are released. Version 1.6.0-beta02 contains
these commits
.
New Features
Optimized large data serialization.
Version 1.6.0-beta01
September 24, 2025
androidx.credentials:credentials:1.6.0-beta01
and
androidx.credentials:credentials-play-services-auth:1.6.0-beta01
are released. Version 1.6.0-beta01 contains
these commits
.
Bug Fixes
Minor documentation fixes (
Ieff7c
,
b/435703922
)
Version 1.6.0-alpha05
August 13, 2025
androidx.credentials:credentials:1.6.0-alpha05
and
androidx.credentials:credentials-play-services-auth:1.6.0-alpha05
are released. Version 1.6.0-alpha05 contains
these commits
.
API Changes
Added APIs that allow relying parties (RPs) to send credential state signals to credential providers, such that they can update the state of the credentials on their end. (
Ia7a65
)
Bug Fixes
Moving the default minSdk from API 21 to API 23 (
Ibdfca
,
b/380448311
,
b/435705964
,
b/435705223
)
Version 1.6.0-alpha04
July 16, 2025
androidx.credentials:credentials:1.6.0-alpha04
and
androidx.credentials:credentials-play-services-auth:1.6.0-alpha04
are released. Version 1.6.0-alpha04 contains
these commits
.
New Features
The Credential Manager dialogs will now look more consistent across Android versions before and after Android 14, on mobile and wearable devices
Version 1.6.0-alpha03
June 18, 2025
androidx.credentials:credentials:1.6.0-alpha03
and
androidx.credentials:credentials-play-services-auth:1.6.0-alpha03
are released. Version 1.6.0-alpha03 contains
these commits
.
New Features
Pre Android 14, update the Credential Manager dialogs to be more consistent with Android 14+.
API Changes
Update
CreateDigitalCredentialRequest
constructor API (
I6f6da
)
Version 1.6.0-alpha02
May 20, 2025
androidx.credentials:credentials:1.6.0-alpha02
and
androidx.credentials:credentials-play-services-auth:1.6.0-alpha02
are released. Version 1.6.0-alpha02 contains
these commits
.
API Changes
Support Digital Credentials issuance (
I4e6f9
)
Version 1.6.0-alpha01
May 7, 2025
androidx.credentials:credentials:1.6.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.6.0-alpha01
are released. Version 1.6.0-alpha01 contains
these commits
.
New Features
Passkey conditional create - Enables the passkey conditional create feature, whereby developers can request for a conditional passkey creation. A conditional creation request will be propagated to the preferred credential provider and then based on some internal conditions, a passkey will be created without the typical bottom sheet UI experience. Users will see a notification with information about the passkey that was just created.
API Changes
Expose
CreateCredentialResponse.createFrom
API (
Ic0494
)
Exposed
isConditionalCreate
bit to allow silent passkey creation. (
I3a1bb
)
Version 1.5
Version 1.5.0
March 12, 2025
androidx.credentials:credentials:1.5.0
and
androidx.credentials:credentials-play-services-auth:1.5.0
are released. Version 1.5.0 contains
these commits
.
Important changes since 1.3.0
Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same
GetCredentialRequest
with a given view, such as a username or a password field. Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.
Restore Credentials: The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a
RestoreCredential
for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.
Version 1.5.0-rc01
January 15, 2025
androidx.credentials:credentials:1.5.0-rc01
and
androidx.credentials:credentials-play-services-auth:1.5.0-rc01
are released. Version 1.5.0-rc01 contains
these commits
.
New Features
A version bump release along with small implementation updates
API Changes
Add
@Deprecated
annotation for
IdentityCredential
to keep consistent with framework. (
I6ac90
,
b/140252778
,
b/217942278
,
b/251211046
,
b/239955609
)
External Contribution
Deprecate
BuildCompat.isAtLeastV
. Callers should check SDK_INT against 35 directly instead. (
I294d1
)
Version 1.5.0-beta01
October 30, 2024
androidx.credentials:credentials:1.5.0-beta01
and
androidx.credentials:credentials-play-services-auth:1.5.0-beta01
are released. Version 1.5.0-beta01 contains
these commits
.
New Features
Beta release for the following new features:
Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same
GetCredentialRequest
with a given view, such as a username or a password field. Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.
Restore Credentials. The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a
RestoreCredential
for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.
API Changes
Allow developers the flexibility to condition within the
CryptoObject
and
BiometricPromptData
setters. (
Ie7e8e
)
Version 1.5.0-alpha06
October 16, 2024
androidx.credentials:credentials:1.5.0-alpha06
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha06
are released. Version 1.5.0-alpha06 contains
these commits
.
New Features
Prepare the library for entering a stable release soon.
Version 1.5.0-alpha05
September 4, 2024
androidx.credentials:credentials:1.5.0-alpha05
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha05
are released. Version 1.5.0-alpha05 contains
these commits
.
API Changes
Support a new credential type -
DigitalCredential
(
I12952
)
Expose bundle conversion APIs: expose more
asBundle
and
fromBundle
helpers to allow these classes be passed across IPC more easily (
I1a017
)
Make
PendingIntentHandler
backward compatible. (
I34c13
)
Make
CallingAppInfo
backward compatible (
I65085
)
Expose
ClearCredentialRequestTypes
constants.
Version 1.5.0-alpha04
August 7, 2024
androidx.credentials:credentials:1.5.0-alpha04
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha04
are released. Version 1.5.0-alpha04 contains
these commits
.
API Changes
Added a default value for
isCloudBackupEnabled
parameter of
CreateRestoreCredentialRequest
.
Bug Fixes
Removed
minSdkVersion
for
credentials-play-services-auth
.
Version 1.5.0-alpha03
July 24, 2024
androidx.credentials:credentials:1.5.0-alpha03
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha03
are released. This version is developed in an internal branch.
New Features
Introduces a new feature, the Restore Credentials. The restore credential is used to restore the user's credential from the previous device to a new Android device. By creating a
RestoreCredential
for the user, the credential will be automatically transferred over to the user's new device if the user selects the app to be transferred from the old device during the setup stage.
API Changes
New classes are added for requesting Restore Credentials.
A new credential type,
RestoreCredential
, that can restore credentials in a new device.
CreateRestoreCredentialRequest
for creating a new
RestoreCredential
.
GetRestoreCredentialOption
for fetching
RestoreCredential
.
ClearCredentialStateRequest
can be modified to clear the
RestoreCredential
.
Bug Fixes
Added a new
RestoreCredential
API for app-restore purposes (
If2d40
)
Version 1.5.0-alpha02
June 12, 2024
androidx.credentials:credentials:1.5.0-alpha02
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha02
are released. This version is developed in an internal branch.
New Features
The ability for
CredentialManager
to directly imbue a
BiometricPrompt
within the credential creation and retrieval flows is now available for use through Jetpack for providers.
API Changes
Added the
BiometricPromptData
to the API surface to allow utilizing the new imbued
BiometricPrompt
flow through
CredentialManager
(
I3b159
)
Modified all entry classes and subclasses across
CreateEntry
and
CredentialEntry
to gain the utility of the
BiometricPromptData
for Providers. (
I16936
,
I8e5bc
)
Added the types needed to encode the error and results from the imbued
BiometricPrompt
flows with
CredentialManager
. (
I8e5bc
)
Version 1.5.0-alpha01
May 29, 2024
androidx.credentials:credentials:1.5.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.5.0-alpha01
are released. This version is developed in an internal branch.
New Features
Secondary UI experience for credential selection: App developers that call Credential Manager APIs at sign-in moments to present the user with a selector, are now able to use new APIs to associate the same
GetCredentialRequest
with a given view, such as a username or a password field.
Subsequently, when the user focuses on one of these views, the corresponding request will be sent to Credential Manager. The resulting credentials are aggregated across providers and displayed in autofill like secondary UIs, such as keyboard or dropdown suggestions. As such when all APIs are used together, the user is first presented with a selector, and if dismissed and taps on one of the fields mentioned above, is then presented with keyboard/dropdown suggestions.
API Changes
A
PendingGetCredentialRequest
class that takes in a (pre-existing)
GetCredentialRequest
, and a callback to be invoked with a (pre-existing)
GetCredentialResponse
, when available asynchronously.
New extension setter API for the android View class, that allows setting an instance of
PendingGetCredentialRequest
. Usage of this API will prepare the given view, such that when the user taps on it, credential suggestions will show up on secondary UI experiences like keyboard/dropdown suggestions.
Version 1.3
Version 1.3.0
October 2, 2024
androidx.credentials:credentials:1.3.0
and
androidx.credentials:credentials-play-services-auth:1.3.0
are released. Version 1.3.0 contains
these commits
.
Important changes since 1.2.0
Various important improvements in making the library more reliable and consistent, including but not limited to:
Support
preferImmediatelyAvailableCredentials
on all android versions.
Improved proguard rule to reduce the app size increase.
Various minor bug fixes.
Version 1.3.0-rc01
July 10, 2024
androidx.credentials:credentials:1.3.0-rc01
and
androidx.credentials:credentials-play-services-auth:1.3.0-rc01
are released. Version 1.3.0-rc01 contains
these commits
.
New Features
A version bump release along with small implementation updates.
Version 1.3.0-beta02
June 12, 2024
androidx.credentials:credentials:1.3.0-beta02
and
androidx.credentials:credentials-play-services-auth:1.3.0-beta02
are released. Version 1.3.0-beta02 contains
these commits
.
Bug Fixes
Fixed logic to correctly check for
NOT_ALLOWED_ERR
instead of
CONSTRAINT_ERR
in public key credential flows that contain an error on pre-U devices (
I31b37
)
Version 1.3.0-beta01
May 29, 2024
androidx.credentials:credentials:1.3.0-beta01
and
androidx.credentials:credentials-play-services-auth:1.3.0-beta01
are released. Version 1.3.0-beta01 contains
these commits
.
API Changes
Rename the
reateCredentialRequest
Bundle conversion API. (
I46b95
)
Update the priorityhints API (
Ida554
)
Version 1.3.0-alpha04
May 14, 2024
androidx.credentials:credentials:1.3.0-alpha04
and
androidx.credentials:credentials-play-services-auth:1.3.0-alpha04
are released. Version 1.3.0-alpha04 contains
these commits
.
Bug Fixes
Move to 21 as the default
minSdkVersion
of androidx libraries. (
I6ec7f
)
Support PRF creation for Android versions 13 and below.
Support
preferImmediatelyAvailableCredentials
for Android versions 13 and below.
Version 1.3.0-alpha03
April 17, 2024
androidx.credentials:credentials:1.3.0-alpha03
and
androidx.credentials:credentials-play-services-auth:1.3.0-alpha03
are released. This version contains source jars that were missing from the previous release.
Version 1.3.0-alpha02
April 3, 2024
androidx.credentials:credentials:1.3.0-alpha02
and
androidx.credentials:credentials-play-services-auth:1.3.0-alpha02
are released. Version 1.3.0-alpha02 contains
these commits
.
New Features
Added new APIs that assist credential entries to be clearly displayed in the credential selector during a
getCredential
or
createCredential
call.
API Changes
Extended the Credential Options API Surface to contain information on display priorities (
Ied6fe
)
Exposed raw Bundle to structured data conversion helpers (
If03a0
)
Exposed
isDefaultIcon
and
isAutoSelectAllowedFromOption
APIs (
I05c59
)
Extended the credential entry API surface to contain information on defaulting an icon (
I9fe00
)
Added an
entryGroupId
bit to the credential entries (
Id995c
)
Added a new
affiliationName
property to the
CredentialEntry
API surface. (
I6261e
)
Exposed
fromXYZEntry
APIs to be used in the framework (
I645a1
)
Bug Fixes
- Provided fallback solution when platform credential manager is not available. (
b/310701473
)
- Fix NPE caused by
clearCredentialState
API (
b/327686881
)
Version 1.3.0-alpha01
December 13, 2023
androidx.credentials:credentials:1.3.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.3.0-alpha01
are released.
Version 1.3.0-alpha01 contains these commits.
Bug Fixes
The minimum APK version needed for Google Play services is now 2023 v08.23 (APK version APK version 230815045), and this check is baked into the library. (
aosp/2856137
)
Fix the already-resume error caused by race condition of multiple in-flight requests (
Ic3567
)
Version 1.2
Version 1.2.2
April 3, 2024
androidx.credentials:credentials:1.2.2
and
androidx.credentials:credentials-play-services-auth:1.2.2
are released. Version 1.2.2 contains
these commits
.
Bug Fixes
Fix the already-resume error caused by race condition of multiple in-flight requests (
Ic3567
)
Fix NPE caused by
clearCredentialState
API (
b/327686881
)
Version 1.2.1
March 6, 2024
androidx.credentials:credentials:1.2.1
and
androidx.credentials:credentials-play-services-auth:1.2.1
are released. Version 1.2.1 contains
these commits
.
Bug Fixes
Provided fallback solution when platform credential manager is not available. (
b/310701473
)
Version 1.2.0
November 1, 2023
androidx.credentials:credentials:1.2.0
and
androidx.credentials:credentials-play-services-auth:1.2.0
are released.
Version 1.2.0 contains these commits.
Important changes since 1.0.0
This release added a new set of APIs for supporting Credential Provider in
storing and fetching passwords, passkeys per users' requests.
Version 1.2.0-rc01
October 4, 2023
androidx.credentials:credentials:1.2.0-rc01
and
androidx.credentials:credentials-play-services-auth:1.2.0-rc01
are released.
Version 1.2.0-rc01 contains these commits.
A version bump release along with small implementation updates
Version 1.2.0-beta04
September 20, 2023
androidx.credentials:credentials:1.2.0-beta04
and
androidx.credentials:credentials-play-services-auth:1.2.0-beta04
are released.
Version 1.2.0-beta04 contains these commits.
New Features
Added get sign in intent flow for sign in with google.  (
Ib6559
,
I7a042
)
Added single signature checking for allowlisted packages.  (
Ie6ff5
)
Updated
PublicKeyCredential
json parsing to utilize updated
toJson()
methods.  (
I708e3
,
I00402
)
Bug Fixes
Fixed missing Proguard rules (
b/288120539
)
Version 1.2.0-beta03
August 23, 2023
androidx.credentials:credentials:1.2.0-beta03
and
androidx.credentials:credentials-play-services-auth:1.2.0-beta03
are released.
Version 1.2.0-beta03 contains these commits.
Bug Fixes
Removes uvm extensions, due to planned deprecation from the webauthn spec. (
I2d46d
)
Ensure compliance to webauthn spec regarding
clientExtensions
,
credProps
, and rk properties (
I3ab01
)
Version 1.2.0-beta02
August 1, 2023
androidx.credentials:credentials:1.2.0-beta02
and
androidx.credentials:credentials-play-services-auth:1.2.0-beta02
are released.
Version 1.2.0-beta02 contains these commits.
Bug Fixes
b/293743991
- Fix the constant value for the
authenticatorData
field, in order to correctly parse the
authenticationResponseJson
property in
PublicKeyCredential
Version 1.2.0-beta01
July 26, 2023
androidx.credentials:credentials:1.2.0-beta01
and
androidx.credentials:credentials-play-services-auth:1.2.0-beta01
are released.
Version 1.2.0-beta01 contains these commits.
API Changes
Expose an API that determines whether the origin is populated or not (
Ia91f4
)
Makes custom exceptions semantically correct (
Ibf6f4
)
add test api (
I61c1d
)
add test api (
Iaeb6f
)
Removed usages of experimental
isAtLeastU()
API (
Ie9117
,
b/289269026
)
Expose a custom origin getter that takes in allowlist (
I0c1b4
)
Added
VisibleForTest
annotation (
I5467a
)
Added
VisibleForTest
annotation (
Idf57a
)
Remove test only apis (
Idcc05
)
Expose provider entry classes to lower API levels (
I2e00a
)
Add test apis (
Id6b9e
)
Bug Fixes
Add test APIs (
I0d243
)
Add new testing APIs (
I6fa12
)
Expose autoselect for Create requests (
I84eee
)
Make JSON encoding errors more detailed (
I7a865
)
Gracefully report a developer error upon a non-activity context parameter (
/I20dd7
,
b/288288940
)
Corrected Exception Parsing for Exceptions returned from Providers (
Iaa2af
,
I0d243
,
I55151
)
Improved documentation for
toSlice
Version 1.2.0-alpha05
June 7, 2023
androidx.credentials:credentials:1.2.0-alpha05
and
androidx.credentials:credentials-play-services-auth:1.2.0-alpha05
are released. This version is developed in an internal branch.
New Features
Backwards compatible parsing for the get API across GMS modules introduced alongside the public branch.
Version 1.2.0-alpha04
May 10, 2023
androidx.credentials:credentials:1.2.0-alpha04
and
androidx.credentials:credentials-play-services-auth:1.2.0-alpha04
are released. This version is developed in an internal branch.
Version 1.2.0-alpha03
April 12, 2023
androidx.credentials:credentials:1.2.0-alpha03
and
androidx.credentials:credentials-play-services-auth:1.2.0-alpha03
are released. This was released from an internal branch.
Version 1.2.0-alpha02
March 8, 2023
androidx.credentials:credentials:1.2.0-alpha02
and
androidx.credentials:credentials-play-services-auth:1.2.0-alpha02
are released. Developed from an internal branch.
API Changes
Enable testing of provider request classes by making constructors public.
Make icons required in all entry classes. However if credential providers do not provide icons, this library will have fallback icons.
Allow credential providers to set multiple authentication action entries, and set a title for each.
Remove all privileged request classes. Providers can now simply get the origin from
android.service.credentials.CallingAppInfo
class, and do not need to handle special request classes for privileged calls (calls on behalf of another app).
Version 1.2.0-alpha01
February 8, 2023
androidx.credentials:credentials:1.2.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.2.0-alpha01
are released.
Version 1.2.0-alpha01 contains these commits.
New Features
This release added a new set of APIs for supporting Credential Provider in
storing and fetching passwords, passkeys per users' requests.
API Changes
New APIs added to support Credential Providers.
Version 1.0
Version 1.0.0-alpha09
June 7, 2023
androidx.credentials:credentials:1.0.0-alpha09
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha09
are released.
Version 1.0.0-alpha09 contains these commits.
Bug Fixes
Validate that exception types are accurate and consistent. (
Id13d7
)
Support the json format on get passkey request.  (
I25100
)
Passkey Retrieval flow is backwards compatible with earlier GMS modules.(
I23878
)
Version 1.0.0-alpha08
May 3, 2023
androidx.credentials:credentials:1.0.0-alpha08
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha08
are released.
Version 1.0.0-alpha08 contains these commits.
Bug Fixes
Improved debug output readability and error messages.
Version 1.0.0-alpha07
April 19, 2023
androidx.credentials:credentials:1.0.0-alpha07
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha07
are released.
Version 1.0.0-alpha07 contains these commits.
Bug Fixes
Fix bug caused by configuration changes (
a75fca
,
b/276316128
)
Don't break the post U flow for the pre-U only SDK (
5418c9
,
b/278148300
)
Version 1.0.0-alpha06
April 5, 2023
androidx.credentials:credentials:1.0.0-alpha06
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha06
are released.
Version 1.0.0-alpha06 contains these commits.
New Features
Update the integration with Google ID, will work with
com.google.android.libraries.identity.googleid:googleid:1.0.0
Version 1.0.0-alpha05
March 22, 2023
androidx.credentials:credentials:1.0.0-alpha05
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha05
are released.
Version 1.0.0-alpha05 contains these commits.
Bug Fixes
Properly report the user cancellation error when the user cancels the modal sheet. (
/I9ff3
,
b/271863184
)
Version 1.0.0-alpha04
March 8, 2023
androidx.credentials:credentials:1.0.0-alpha04
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha04
are released.
Version 1.0.0-alpha04 contains these commits.
API Changes
Added
android.permission.CREDENTIAL_MANAGER_SET_ORIGIN
requirement for setting origin in Jetpack Library. (
Ibaad4
)
Added passkey get flow exceptions (
I4f654
)
CredentialManager
api autoselect behavior update (
I576dd
)
CreateCredentialRequest.DisplayInfo
now uses
CharSequence
rather than
String
fields. (
I85e70
)
Bug Fixes
Add proguard rules to ensure the play auth module won't be removed by R8. (
9543977
)
Version 1.0.0-alpha03
February 22, 2023
androidx.credentials:credentials:1.0.0-alpha03
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha03
are released.
Version 1.0.0-alpha03 contains these commits.
New Features
Added support for Sign-in with Google.
API Changes
Allows
UnsupportedException
to function correctly (
I68208
)
Adding a new exception type to account for cases such as when the device does not contain the necessary flags (
If08dd
)
CredentialManager
exception api (
I72947
)
Version 1.0.0-alpha02
February 8, 2023
androidx.credentials:credentials:1.0.0-alpha02
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha02
are released.
Version 1.0.0-alpha02 contains these commits.
API Changes
CredentialManager
api signature changes (
Iabdec
)
CredentialManager
api signature changes (
I977ed
)
CredentialManager
api signature changes (
Ia6e9b
)
Bug Fixes
Older ‘cable’ is no longer supported in the
webauthn spec
, and its replacement, ‘hybrid’ is now returned for the transport list.
Transports were given back in two dimensional lists, this has been fixed to be the correct 1d list.
Version 1.0.0-alpha01
January 11, 2023
androidx.credentials:credentials:1.0.0-alpha01
and
androidx.credentials:credentials-play-services-auth:1.0.0-alpha01
are released.
Version 1.0.0-alpha01 contains these commits.
New Features
This release contains a new jetpack library which provides a unified access to a user's credentials. This can include passwords, passkeys and federated credentials. This library should be used to provide seamless and secure sign-in experiences.
`androidx.credentials:credentials-play-services-auth:1.0.0-alpha01 ‘ is an optional library that allows credentials to be stored to, and retrieved from Google Password Manager. This dependency is needed for devices running Android API level <= 33.
API Changes
New library with new APIs
Content and code samples on this page are subject to the licenses described in the
Content License
. Java and OpenJDK are trademarks or registered trademarks of Oracle and/or its affiliates.
Last updated 2026-04-22 UTC.