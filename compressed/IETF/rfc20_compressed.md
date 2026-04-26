# RFC 20: ASCII Format for Network Interchange
**Source**: Network Working Group (Vint Cerf, UCLA) | **Version**: RFC 20 | **Date**: October 16, 1969 | **Type**: Normative  
**Original**: https://www.rfc-editor.org/rfc/rfc20.txt

## Scope (Summary)
Specifies the use of the standard 7-bit ASCII (USAS X3.4-1968) embedded in an 8-bit byte with high-order bit always 0 for HOST-HOST primary connections over the ARPANET. Break characters are defined by the receiving remote host.

## Normative References
- USAS X3.4-1968 (USA Standard Code for Information Interchange)

## Definitions and Abbreviations
- **ASCII**: Pronounced “as’-key”; also USASCII (you-sas’-key). Refers to the latest issue of the standard unless a year is appended (e.g., ASCII 63).
- **Break character**: Defined by the receiving remote host (e.g., SRI uses `.` (X'2E'), UCLA uses X'OD' (carriage return)).
- **(CC)**: Communication Control
- **(FE)**: Format Effector
- **(IS)**: Information Separator

## 1. Scope
The coded character set is to be used for the general interchange of information among information processing systems, communication systems, and associated equipment.

## 2. Standard Code (7-bit ASCII Table)
| b7 b6 b5 | 0 0 0 (Col 0) | 0 0 1 (Col 1) | 0 1 0 (Col 2) | 0 1 1 (Col 3) | 1 0 0 (Col 4) | 1 0 1 (Col 5) | 1 1 0 (Col 6) | 1 1 1 (Col 7) |
|---|---|---|---|---|---|---|---|---|
| **Row 0 (b4-b1 0000)** | NUL | DLE | SP | 0 | @ | P | ` | p |
| **Row 1 (0001)** | SOH | DC1 | ! | 1 | A | Q | a | q |
| **Row 2 (0010)** | STX | DC2 | " | 2 | B | R | b | r |
| **Row 3 (0011)** | ETX | DC3 | # | 3 | C | S | c | s |
| **Row 4 (0100)** | EOT | DC4 | $ | 4 | D | T | d | t |
| **Row 5 (0101)** | ENQ | NAK | % | 5 | E | U | e | u |
| **Row 6 (0110)** | ACK | SYN | & | 6 | F | V | f | v |
| **Row 7 (0111)** | BEL | ETB | ' | 7 | G | W | g | w |
| **Row 8 (1000)** | BS | CAN | ( | 8 | H | X | h | x |
| **Row 9 (1001)** | HT | EM | ) | 9 | I | Y | i | y |
| **Row 10 (1010)** | LF | SUB | * | : | J | Z | j | z |
| **Row 11 (1011)** | VT | ESC | + | ; | K | [ | k | { |
| **Row 12 (1100)** | FF | FS | , | < | L | \ | l | \| |
| **Row 13 (1101)** | CR | GS | - | = | M | ] | m | } |
| **Row 14 (1110)** | SO | RS | . | > | N | ^ | n | ~ |
| **Row 15 (1111)** | SI | US | / | ? | O | _ | o | DEL |

## 3. Character Representation and Code Identification
- Bit order: b7 (high-order) most significant, b1 (low-order) least significant.
- Character “K” binary: `1001011` (Column 4, Row 11; also denoted 4/11).
- Column number = decimal of b7 b6 b5; Row number = decimal of b4 b3 b2 b1.
- Code identification: “ASCII” or “USASCII”. To designate a particular issue, append year (e.g., ASCII 63).

## 4. Legend
### 4.1 Control Characters (abbreviations)
- **NUL**: Null
- **SOH**: Start of Heading (CC)
- **STX**: Start of Text (CC)
- **ETX**: End of Text (CC)
- **EOT**: End of Transmission (CC)
- **ENQ**: Enquiry (CC)
- **ACK**: Acknowledge (CC)
- **BEL**: Bell
- **BS**: Backspace (FE)
- **HT**: Horizontal Tabulation (FE)
- **LF**: Line Feed (FE)
- **VT**: Vertical Tabulation (FE)
- **FF**: Form Feed (FE)
- **CR**: Carriage Return (FE)
- **SO**: Shift Out
- **SI**: Shift In
- **DLE**: Data Link Escape (CC)
- **DC1‑DC4**: Device Control 1–4
- **NAK**: Negative Acknowledge (CC)
- **SYN**: Synchronous Idle (CC)
- **ETB**: End of Transmission Block (CC)
- **CAN**: Cancel
- **EM**: End of Medium
- **SUB**: Substitute
- **ESC**: Escape
- **FS/GS/RS/US**: File/Group/Record/Unit Separator (IS)
- **DEL**: Delete (not a control character in strict sense)

### 4.2 Graphic Characters (selected)
- `SP` (2/0): Space
- `!` (2/1), `"` (2/2), `#` (2/3), `$` (2/4), `%` (2/5), `&` (2/6), `'` (2/7), `(` (2/8), `)` (2/9), `*` (2/10), `+` (2/11), `,` (2/12), `-` (2/13), `.` (2/14), `/` (2/15)
- `:` (3/10), `;` (3/11), `<` (3/12), `=` (3/13), `>` (3/14), `?` (3/15)
- `@` (4/0), `[` (5/11), `\` (5/12), `]` (5/13), `^` (5/14), `_` (5/15)
- `` ` `` (6/0), `{` (7/11), `|` (7/12), `}` (7/13), `~` (7/14)
- **Note**: Characters at 2/2, 2/7, 2/12, 5/14, 6/0, 7/14 may be used as diacritical marks (see Appendix A).
- Characters at 4/0, 5/11–5/14, 6/0, 7/11–7/14 `shall not` be used in international interchange without agreement between sender and recipient.
- At position 2/3, `#` may be replaced with `£` (Pounds Sterling) when no `#` is required.

## 5. Definitions
### 5.1 General
- **(CC)**: Functional character to control/facilitate transmission over communication networks.
- **(FE)**: Character controlling layout/positioning in printing or display devices.
- **(IS)**: Character used to separate and qualify information logically; hierarchical order: FS > GS > RS > US.

### 5.2 Control Characters (exact definitions preserved)
- **NUL**: All-zeros character for time fill and media fill.
- **SOH**: (CC) Used at start of heading (machine-sensible address/routing). Terminated by STX.
- **STX**: (CC) Precedes text entity to be transmitted to ultimate destination. May terminate SOH sequence.
- **ETX**: (CC) Terminates sequence started with STX.
- **EOT**: (CC) Indicates conclusion of a transmission (may contain multiple texts/headings).
- **ENQ**: (CC) Requests response from remote station (WRU) for identification/status.
- **ACK**: (CC) Affirmative response from receiver.
- **BEL**: Calls for human attention; may control alarm devices.
- **BS**: (FE) Moves printing position one space backward on same line.
- **HT**: (FE) Moves to next predetermined position along printing line (also for punched card skip).
- **LF**: (FE) Moves to next printing line. May have meaning “New Line” (NL) by agreement between sender and recipient.
- **VT**: (FE) Moves to next predetermined printing line.
- **FF**: (FE) Moves to first predetermined line on next form/page.
- **CR**: (FE) Moves to first printing position on same line.
- **SO**: Interpret subsequent code combinations as outside standard set until SI.
- **SI**: Interpret subsequent code combinations according to standard set.
- **DLE**: (CC) Changes meaning of limited number of following characters for supplementary controls in data communication.
- **DC1‑DC4**: Controls for ancillary devices (on/off). DC4 preferred for “stop”.
- **NAK**: (CC) Negative response from receiver.
- **SYN**: (CC) Used in synchronous systems for synchronization in absence of other characters.
- **ETB**: (CC) End of block for communication purposes; block structure may be independent of processing format.
- **CAN**: Indicates data sent is in error or to be disregarded.
- **EM**: Indicates physical end of medium or end of used/wanted portion.
- **SUB**: Substituted for invalid/erroneous character.
- **ESC**: Prefix for code extension; affects interpretation of a limited number of following characters.
- **FS/GS/RS/US**: Information separators in hierarchical order (FS most inclusive). Content and length not specified.
- **DEL**: Used to “erase” erroneous characters in perforated tape; not a control character.

### 5.3 Graphic Characters
- **SP (Space)**: Normally non-printing graphic; separates words; also a format effector advancing printing position one space forward.

## 6. General Considerations
- This standard does **not** define physical recording, redundancy, error control, data communication structure, formats, code extension techniques, or graphic representation of control characters.
- **Deviations** from the standard may create serious difficulties and should be used only with full cognizance of involved parties.
- Relative sequence of any two characters for collation is defined by their binary values.
- No specific meaning is prescribed for graphics except that understood by users; no type style is specified.
- Appendices provide additional information on design and use.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Use standard 7-bit ASCII embedded in an 8-bit byte with high-order bit always 0 | shall | Scope |
| R2 | Break characters defined by receiving remote host | shall | Scope |
| R3 | Characters at positions 4/0, 5/11–5/14, 6/0, 7/11–7/14 shall not be used in international interchange without sender/recipient agreement | shall | §4.2 note 3 |
| R4 | Hierarchical order of information separators: FS (most inclusive), GS, RS, US (least inclusive) | shall | §5.2 (FS/US definitions) |
| R5 | Deviations from the standard may create serious difficulties and should be used only with full cognizance of parties | should | §6.2 |
| R6 | Collation sequence defined by binary values | shall | §6.3 |

## Informative Annexes (Condensed)
- **Appendix A**: Describes use of certain graphic characters as diacritical marks (positions 2/2, 2/7, 2/12, 5/14, 6/0, 7/14). Not reproduced here.
- **Appendix B**: Addresses international interchange – warns that certain characters (listed above) require prior agreement. Not reproduced here.