# RFC 3339: Date and Time on the Internet: Timestamps
**Source**: IETF | **Version**: Standards Track | **Date**: July 2002 | **Type**: Normative
**Original**: https://datatracker.ietf.org/doc/html/rfc3339

## Scope (Summary)
This document defines an Internet profile of ISO 8601 for representing date and time using the Gregorian calendar, intended for timestamps in Internet protocols. It covers fully-qualified dates and times with a stated UTC offset, excluding time intervals, local time zone rules, and unqualified local times.

## Normative References
- [ABNF] Crocker, D. and P. Overell, "Augmented BNF for Syntax Specifications: ABNF", RFC 2234, November 1997.
- [HOST-REQ] Braden, R., "Requirements for Internet Hosts -- Application and Support", STD 3, RFC 1123, October 1989.
- [IERS] International Earth Rotation Service Bulletins, <http://hpiers.obspm.fr/eop-pc/products/bulletins.html>.
- [IMAIL] Crocker, D., "Standard for the Format of Arpa Internet Text Messages", STD 11, RFC 822, August 1982.
- [IMAIL-UPDATE] Resnick, P., "Internet Message Format", RFC 2822, April 2001.
- [ISO8601] "Data elements and interchange formats -- Information interchange -- Representation of dates and times", ISO 8601:1988(E), June 1988.
- [ISO8601:2000] "Data elements and interchange formats -- Information interchange -- Representation of dates and times", ISO 8601:2000, December 2000.
- [ITU-R-TF] International Telecommunication Union Recommendations for Time Signals and Frequency Standards Emissions.
- [NTP] Mills, D, "Network Time Protocol (Version 3) Specification, Implementation and Analysis", RFC 1305, March 1992.
- [RFC2119] Bradner, S, "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
- [ZELLER] Zeller, C., "Kalender-Formeln", Acta Mathematica, Vol. 9, Nov 1886.

## Definitions and Abbreviations
- **ABNF**: Augmented Backus-Naur Form as defined in [ABNF].
- **day**: A period of time of 24 hours.
- **Email Date/Time Format**: The date/time format defined by RFC 2822 [IMAIL-UPDATE].
- **hour**: A period of time of 60 minutes.
- **Internet Date/Time Format**: The date format defined in section 5 of this document.
- **leap year**: In the Gregorian calendar, a year that has 366 days. A year divisible by 4, except centennial years must be divisible by 400.
- **minute**: A period of time of 60 seconds, with restrictions per section 5.7 and Appendix D for leap seconds.
- **second**: A basic SI unit; 9,192,631,770 cycles of cesium-133 hyperfine transition.
- **Timestamp**: An unambiguous representation of some instant in time.
- **UTC**: Coordinated Universal Time as maintained by the BIPM.
- **Z**: A suffix indicating a UTC offset of 00:00.

## 1. Introduction (Condensed)
This document addresses interoperability problems with date/time formats on the Internet by providing a profile of ISO 8601. It focuses on timestamps for events, assuming:
- All dates are in the current era (0000–9999 AD).
- All times have a stated offset to UTC.
- Timestamps express an instant in time (not intervals).
- Times before UTC are expressed relative to universal time using best available practice.

## 2. Definitions (Normative Language)
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in RFC 2119.

## 3. Two Digit Years
- **R3.1**: Internet Protocols MUST generate four digit years in dates.
- **R3.2**: The use of 2-digit years is deprecated. If a 2-digit year is received, it should be accepted ONLY if an incorrect interpretation will not cause a protocol or processing failure.
- **R3.3**: Programs may add 1900 to three-digit years (from broken software that subtracts 1900 without checking digits).
- **R3.4**: Programs should detect non-numeric decades (e.g., ":0", ";0") and interpret appropriately.
- **R3.5**: All dates and times used in Internet protocols MUST be fully qualified.

## 4. Local Time

### 4.1. Coordinated Universal Time (UTC)
- True interoperability is best achieved by using UTC. This specification does not cater to local time zone rules.

### 4.2. Local Offsets
- Numeric offsets are mandatory (per RFC2822). Offset = local time minus UTC. Example: 18:50:00-04:00 = 22:50:00Z.
- NOTE: Following ISO 8601, numeric offsets represent only time zones that differ from UTC by an integral number of minutes. Historical non-integral offsets must be converted.

### 4.3. Unknown Local Offset Convention
- If UTC time is known but offset to local time is unknown, represent with offset "-00:00". This differs semantically from "Z" or "+00:00".

### 4.4. Unqualified Local Time
- Systems configured with local time and unaware of UTC offset MUST use a mechanism for correct UTC synchronization, such as:
  - Use NTP to obtain UTC.
  - Use another host in the same local time zone as a gateway (this host MUST correct unqualified local times).
  - Prompt the user for local time zone and daylight saving rules.

## 5. Date and Time Format

### 5.1. Ordering
- If components are ordered from least to most precise, same time zone, same number of fractional seconds, strings can be sorted as strings. Optional punctuation would violate this.

### 5.2. Human Readability
- Internet clients SHOULD be prepared to transform dates into a display format suitable for the locality (including UTC to local time).

### 5.3. Rarely Used Options
- The format defined includes only one rarely used option: fractions of a second. Expected to be used only when strict ordering or unusual precision is required.

### 5.4. Redundant Information
- Day of the week should not be included (can cause inconsistency; can be computed from date).

### 5.5. Simplicity
- The full ISO 8601 grammar is too complex for most Internet protocols. The profile makes most fields and punctuation mandatory.

### 5.6. Internet Date/Time Format
The following profile of ISO 8601 SHOULD be used in new protocols. Syntax in ABNF:

```
date-fullyear   = 4DIGIT
date-month      = 2DIGIT  ; 01-12
date-mday       = 2DIGIT  ; 01-28, 01-29, 01-30, 01-31 based on month/year
time-hour       = 2DIGIT  ; 00-23
time-minute     = 2DIGIT  ; 00-59
time-second     = 2DIGIT  ; 00-58, 00-59, 00-60 based on leap second rules
time-secfrac    = "." 1*DIGIT
time-numoffset  = ("+" / "-") time-hour ":" time-minute
time-offset     = "Z" / time-numoffset
partial-time    = time-hour ":" time-minute ":" time-second [time-secfrac]
full-date       = date-fullyear "-" date-month "-" date-mday
full-time       = partial-time time-offset
date-time       = full-date "T" full-time
```

- NOTE: Per ABNF and ISO8601, "T" and "Z" may alternatively be lower case. Specifications MAY require upper case. Applications SHOULD use upper case.
- NOTE: Applications may choose to separate full-date and full-time with a space for readability.

### 5.7. Restrictions
- date-mday maximum values are as per calendar (table in original; leap year per Appendix C).
- time-second may be "60" at the end of months where a leap second occurs (June or December, per IERS announcements). Leap seconds may be subtracted (maximum then "58"). In non-Z time zones, leap second point is shifted by offset.
- Applications SHOULD NOT generate timestamps with leap seconds until after announcement.
- Hour values are limited to "00" through "23" (ISO 8601 allows "24").

### 5.8. Examples
- 1985-04-12T23:20:50.52Z
- 1996-12-19T16:39:57-08:00 (equivalent to 1996-12-20T00:39:57Z)
- 1990-12-31T23:59:60Z (leap second)
- 1990-12-31T15:59:60-08:00 (leap second in PST)
- 1937-01-01T12:00:27.87+00:20 (Netherlands time, closest representable offset)

## Requirements Summary
| ID | Requirement | Type | Reference |
|----|-------------|------|-----------|
| R1 | Internet Protocols MUST generate four digit years in dates. | MUST | Section 3 |
| R2 | Use of 2-digit years is deprecated. Accept ONLY if no failure. | SHOULD (deprecated) | Section 3 |
| R3 | All dates and times used in Internet protocols MUST be fully qualified. | MUST | Section 3 |
| R4 | Systems with local time unaware of UTC offset MUST use a mechanism ensuring correct UTC synchronization (e.g., NTP, gateway, user prompt). | MUST | Section 4.4 |
| R5 | Internet Date/Time Format SHOULD be used in new protocols. | SHOULD | Section 5.6 |
| R6 | Applications generating the format SHOULD use upper case "T" and "Z". | SHOULD | Section 5.6 |
| R7 | Applications SHOULD NOT generate timestamps with leap seconds until after announcement. | SHOULD | Section 5.7 |

## Informative Annexes (Condensed)
- **Appendix A – ISO 8601 Collected ABNF**: Informational attempt to create a formal grammar for ISO 8601 (1988). Notes ambiguities (e.g., "24" hour, mixtures of basic/extended). Not authoritative; ISO 8601 remains the reference.
- **Appendix B – Day of the Week**: Provides a C subroutine (Zeller's Congruence) to compute day of week for dates on or after 0000-03-01.
- **Appendix C – Leap Years**: Provides a C subroutine to determine if a year is a leap year (divisible by 4, not by 100 unless also by 400).
- **Appendix D – Leap Seconds**: Describes that leap seconds are inserted by IERS at end of December or June (preferred), represented as YYYY-MM-DDT23:59:60Z. Includes a table of leap seconds from 1972 to 1998 with TAI-UTC differences.
```
- **Acknowledgements**: Lists contributors and reviewers.
- **Full Copyright Statement**: As per IETF, unlimited distribution with copyright notice; document provided "AS IS".