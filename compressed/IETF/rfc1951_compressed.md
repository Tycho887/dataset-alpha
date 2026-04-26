# RFC 1951: DEFLATE Compressed Data Format Specification version 1.3
**Source**: Internet Engineering Task Force (IETF) | **Version**: 1.3 | **Date**: May 1996 | **Type**: Informational
**Original**: https://tools.ietf.org/html/rfc1951

## Scope (Summary)
This specification defines a lossless compressed data format using LZ77 and Huffman coding. It is independent of CPU, OS, file system, and character set, suitable for interchange. It compresses data with efficiency comparable to best general-purpose methods, with worst-case expansion of 0.015% for large data sets.

## Normative References
- [1] Huffman, D.A., "A Method for the Construction of Minimum Redundancy Codes", Proc. IRE, September 1952.
- [2] Ziv J., Lempel A., "A Universal Algorithm for Sequential Data Compression", IEEE Trans. Info. Theory, Vol. 23, No. 3, pp. 337-343.
- [3] Gailly, J.-L., Adler, M., ZLIB documentation and sources, ftp://ftp.uu.net/pub/archiving/zip/doc/
- [4] Gailly, J.-L., Adler, M., GZIP documentation and sources, ftp://prep.ai.mit.edu/pub/gnu/
- [5] Schwartz, E.S., Kallick, B., "Generating a canonical prefix encoding", Comm. ACM, 7,3 (Mar. 1964), pp. 166-169.
- [6] Hirschberg and Lelewer, "Efficient decoding of prefix codes", Comm. ACM, 33,4, April 1990, pp. 449-459.

## Definitions and Abbreviations
- **Byte**: 8 bits stored or transmitted as a unit (same as an octet).
- **String**: a sequence of arbitrary bytes.
- **LZ77**: Lempel-Ziv 1977 algorithm.
- **Huffman coding**: prefix coding using optimal code lengths.
- **Bit numbering**: bits of a byte numbered 0 (least-significant) to 7 (most-significant).
- **Multi-byte numbers**: stored with least-significant byte first (little-endian).

## 1. Introduction
### 1.1 Purpose
Define a lossless compressed data format that:
- Is independent of CPU type, operating system, file system, and character set; usable for interchange.
- Can be produced or consumed for arbitrarily long sequentially presented input using only a priori bounded intermediate storage; usable in data communications or Unix filters.
- Compresses data with efficiency comparable to best general-purpose methods, better than "compress".
- Can be implemented readily in a manner not covered by patents.
- Is compatible with gzip: conforming decompressors can read data produced by existing gzip compressor.

Does not attempt to:
- Allow random access to compressed data.
- Compress specialized data (e.g., raster graphics) as well as best specialized algorithms.

Worst-case expansion: 5 bytes per 32K-byte block (0.015% increase for large data). Typical compression: English text 2.5–3×; executables less; raster images much more.

### 1.2 Intended Audience
Implementors of compressors/decompressors. Assumes basic programming at bit level. Familiarity with Huffman coding helpful but not required.

### 1.3 Scope
Specifies method for representing a sequence of bytes as a (usually shorter) sequence of bits, and a method for packing the bit sequence into bytes.

### 1.4 Compliance
- **Compliant decompressor** must be able to accept and decompress any data set conforming to all specifications presented here.
- **Compliant compressor** must produce data sets conforming to all specifications presented here.

### 1.5 Definitions
- **Byte**: 8 bits, even on machines with different character bit sizes.
- **String**: sequence of arbitrary bytes.

### 1.6 Changes from Previous Versions
No technical changes since version 1.1. Version 1.2 changed some terminology. Version 1.3 is conversion to RFC style.

## 2. Compressed Representation Overview
A compressed data set consists of a series of blocks, corresponding to successive blocks of input data. Block sizes are arbitrary, except non-compressible blocks are limited to 65,535 bytes.

Each block compressed using LZ77 and Huffman coding. Huffman trees for each block are independent; LZ77 may reference a duplicated string occurring in a previous block, up to 32K input bytes before.

Each block consists of:
- Pair of Huffman code trees (themselves compressed using Huffman encoding)
- Compressed data part

Compressed data consists of:
- Literal bytes (strings not duplicated within previous 32K input bytes)
- Pointers (length, backward distance) to duplicated strings

Distances limited to 32K bytes; lengths limited to 258 bytes. Block size not limited, except for uncompressible blocks.

Each type of value (literals, distances, lengths) represented using Huffman code: one code tree for literals and lengths, separate tree for distances. Code trees appear in compact form before compressed data for each block.

## 3. Detailed Specification
### 3.1 Overall Conventions
Bits of a byte numbered: `+--------+` `|76543210|` `+--------+` (bit 0 least-significant). Multi-byte numbers stored least-significant byte first.

#### 3.1.1 Packing into Bytes
- Data elements packed into bytes in order of increasing bit number within byte (starting with LSB).
- Data elements other than Huffman codes packed starting with LSB of the data element.
- Huffman codes packed starting with MSB of the code.
This allows parsing from right to left with fixed-width elements in MSB-to-LSB order and Huffman codes in bit-reversed order.

### 3.2 Compressed Block Format
#### 3.2.1 Synopsis of Prefix and Huffman Coding
Prefix coding: symbols represented by variable-length bit sequences, unambiguous parsing. Defined by binary tree where edges labeled 0/1, leaf nodes labeled with symbols. Huffman algorithm constructs optimal prefix code given symbol frequencies. In deflate, Huffman codes must not exceed certain maximum code lengths.

#### 3.2.2 Use of Huffman Coding in the "deflate" Format
Two additional rules:
1. All codes of a given bit length have lexicographically consecutive values in the same order as the symbols they represent.
2. Shorter codes lexicographically precede longer codes.

Algorithm to generate codes from bit lengths:
1. Count number of codes for each code length (bl_count[N]).
2. Compute numerical value of smallest code for each length:
   `code = 0; bl_count[0] = 0; for (bits = 1; bits <= MAX_BITS; bits++) { code = (code + bl_count[bits-1]) << 1; next_code[bits] = code; }`
3. Assign values using consecutive values for all codes of same length; codes with bit length zero not assigned.

#### 3.2.3 Details of Block Format
Each block begins with 3 header bits:
- **BFINAL**: 1 bit, set if and only if this is the last block.
- **BTYPE**: 2 bits, specifies compression:
  - `00` – no compression
  - `01` – compressed with fixed Huffman codes
  - `10` – compressed with dynamic Huffman codes
  - `11` – reserved (error)

Decoding algorithm:
```
do
   read block header.
   if BTYPE=00
      skip remaining bits in current partially processed byte
      read LEN and NLEN (2 bytes each)
      copy LEN bytes of data to output
   else
      if BTYPE=10
         read representation of code trees
      loop (until end-of-block code)
         decode literal/length value from input stream
         if value < 256
            copy literal byte to output
         else if value = 256
            break
         else (value 257..285)
            decode distance from input stream
            move backwards distance bytes in output and copy length bytes from that position to output
      end loop
while not last block
```

A duplicated string reference may refer to a string in a previous block (distance may cross block boundaries). Distance cannot refer past the beginning of the output stream. Overlapping string allowed (e.g., length 5, distance 2 adds X,Y,X,Y,X).

#### 3.2.4 Non-compressed Blocks (BTYPE=00)
Bits of input up to next byte boundary are ignored. Block consists of:
```
 0   1   2   3   4...
+---+---+---+---+================================+
| LEN | NLEN | ... LEN bytes of literal data ...|
+---+---+---+---+================================+
```
LEN = number of data bytes. NLEN = one's complement of LEN.

#### 3.2.5 Compressed Blocks (Length and Distance Codes)
Literal and length alphabets merged into single alphabet (0..285):
- 0–255: literal bytes
- 256: end-of-block
- 257–285: length codes (possibly with extra bits)

**Length code table:**
| Code | Extra Bits | Length(s) | Code | Extra Bits | Length(s) | Code | Extra Bits | Length(s) |
|------|------------|-----------|------|------------|-----------|------|------------|-----------|
| 257  | 0          | 3         | 267  | 1          | 15,16     | 277  | 4          | 67–82     |
| 258  | 0          | 4         | 268  | 1          | 17,18     | 278  | 4          | 83–98     |
| 259  | 0          | 5         | 269  | 2          | 19–22     | 279  | 4          | 99–114    |
| 260  | 0          | 6         | 270  | 2          | 23–26     | 280  | 4          | 115–130   |
| 261  | 0          | 7         | 271  | 2          | 27–30     | 281  | 5          | 131–162   |
| 262  | 0          | 8         | 272  | 2          | 31–34     | 282  | 5          | 163–194   |
| 263  | 0          | 9         | 273  | 3          | 35–42     | 283  | 5          | 195–226   |
| 264  | 0          | 10        | 274  | 3          | 43–50     | 284  | 5          | 227–257   |
| 265  | 1          | 11,12     | 275  | 3          | 51–58     | 285  | 0          | 258       |
| 266  | 1          | 13,14     | 276  | 3          | 59–66     |      |            |           |

Extra bits interpreted as machine integer stored with most-significant bit first.

**Distance code table:**
| Code | Extra Bits | Distance | Code | Extra Bits | Distance | Code | Extra Bits | Distance |
|------|------------|----------|------|------------|----------|------|------------|----------|
| 0    | 0          | 1        | 10   | 4          | 33–48    | 20   | 9          | 1025–1536 |
| 1    | 0          | 2        | 11   | 4          | 49–64    | 21   | 9          | 1537–2048 |
| 2    | 0          | 3        | 12   | 5          | 65–96    | 22   | 10         | 2049–3072 |
| 3    | 0          | 4        | 13   | 5          | 97–128   | 23   | 10         | 3073–4096 |
| 4    | 1          | 5,6      | 14   | 6          | 129–192  | 24   | 11         | 4097–6144 |
| 5    | 1          | 7,8      | 15   | 6          | 193–256  | 25   | 11         | 6145–8192 |
| 6    | 2          | 9–12     | 16   | 7          | 257–384  | 26   | 12         | 8193–12288 |
| 7    | 2          | 13–16    | 17   | 7          | 385–512  | 27   | 12         | 12289–16384 |
| 8    | 3          | 17–24    | 18   | 8          | 513–768  | 28   | 13         | 16385–24576 |
| 9    | 3          | 25–32    | 19   | 8          | 769–1024 | 29   | 13         | 24577–32768 |

#### 3.2.6 Compression with Fixed Huffman Codes (BTYPE=01)
Huffman code lengths for literal/length alphabet:
| Lit Value | Bits | Codes |
|-----------|------|-------|
| 0–143     | 8    | 00110000 – 10111111 |
| 144–255   | 9    | 110010000 – 111111111 |
| 256–279   | 7    | 0000000 – 0010111 |
| 280–287   | 8    | 11000000 – 11000111 |

Literal/length values 286–287 never occur in compressed data but participate in code construction.  
Distance codes 0–31 represented by fixed-length 5-bit codes with possible additional bits as per table in 3.2.5. Distance codes 30–31 never occur.

#### 3.2.7 Compression with Dynamic Huffman Codes (BTYPE=10)
Huffman codes for literal/length and distance alphabets defined by sequences of code lengths, compressed using a Huffman code. Code length alphabet:
- 0–15: represent code lengths 0–15.
- 16: copy previous code length 3–6 times (next 2 bits indicate repeat length: 0=3, 1=4, 2=5, 3=6).
- 17: repeat code length 0 for 3–10 times (next 3 bits of length).
- 18: repeat code length 0 for 11–138 times (next 7 bits of length).

Code length 0 means symbol not used; must not participate in Huffman code construction. If only one distance code used, it is encoded using one bit (single code length of one, with one unused code). One distance code of zero bits means no distance codes used (all literals).

Block format:
- 5 bits: **HLIT** = # of Literal/Length codes – 257 (range 257–286)
- 5 bits: **HDIST** = # of Distance codes – 1 (range 1–32)
- 4 bits: **HCLEN** = # of Code Length codes – 4 (range 4–19)
- (HCLEN + 4) × 3 bits: code lengths for code length alphabet in order: 16, 17, 18, 0, 8, 7, 9, 6, 10, 5, 11, 4, 12, 3, 13, 2, 14, 1, 15. Interpreted as 3-bit integers (0–7); 0 means corresponding symbol not used.
- HLIT + 257 code lengths for literal/length alphabet, encoded using the code length Huffman code.
- HDIST + 1 code lengths for distance alphabet, encoded using the code length Huffman code.
- Actual compressed data, encoded using literal/length and distance Huffman codes.
- Literal/length symbol 256 (end of data), encoded using literal/length Huffman code.

Code length repeat codes can cross from HLIT+257 to HDIST+1 code lengths; all code lengths form a single sequence of HLIT + HDIST + 258 values.

### 3.3 Compliance
- A compressor may limit further ranges of values (e.g., smaller backward pointers, block size) and still be compliant.
- A compliant decompressor must accept the full range of possible values defined above and must accept blocks of arbitrary size.

## 4. Compression Algorithm Details (Informative)
This section describes a non-patented LZ77 algorithm using a chained hash table operating on 3-byte sequences. The compressor searches hash chain for longest match, favors small distances, uses lazy matching to improve compression. Run-time parameters control trade-off between compression ratio and speed. This material is not part of the specification per se; a compressor need not follow it.

## Requirements Summary
| ID | Requirement | Type | Reference |
|---|---|---|---|
| R1 | Compliant decompressor must accept and decompress any conforming data set | shall | 1.4, 3.3 |
| R2 | Compliant compressor must produce conforming data sets | shall | 1.4 |
| R3 | BFINAL set if and only if this is the last block | shall | 3.2.3 |
| R4 | BTYPE values: 00 no compression, 01 fixed Huffman, 10 dynamic Huffman, 11 reserved | shall | 3.2.3 |
| R5 | Non-compressed block format: skip bits to byte boundary, LEN, NLEN, LEN literal bytes | shall | 3.2.4 |
| R6 | Fixed Huffman codes for literal/length alphabet: bit lengths as per table | shall | 3.2.6 |
| R7 | Fixed Huffman codes for distance alphabet: 5-bit codes with extra bits per table | shall | 3.2.6 |
| R8 | Dynamic Huffman block format: HLIT, HDIST, HCLEN, code lengths, compressed data, end symbol | shall | 3.2.7 |
| R9 | Code length alphabet and repeat codes as defined | shall | 3.2.7 |
| R10 | Length codes 257–285 with extra bits per table | shall | 3.2.5 |
| R11 | Distance codes 0–29 with extra bits per table | shall | 3.2.5 |
| R12 | Packing: data elements into bytes starting with LSB, Huffman codes starting with MSB | shall | 3.1.1 |
| R13 | Multi-byte numbers stored least-significant byte first | shall | 3.1 |

## Informative Annexes (Condensed)
- **Section 4 (Compression Algorithm Details)**: Describes an example non-patented LZ77 compressor (chained hash table, lazy matching). Not normative.
- **Section 5 (References)**: Lists six references: Huffman (1952), Ziv-Lempel (1977), ZLIB/GZIP sources, canonical prefix encoding, and efficient decoding.
- **Section 6 (Security Considerations)**: Notes that data corruption in compressed data is severe; recommends integrity validation (e.g., via ZLIB).
- **Section 7 (Source code)**: Reference C implementation available in zlib package.
- **Section 8 (Acknowledgements)**: Credits Phil Katz (designer), Jean-Loup Gailly and Mark Adler (software), Glenn Randers-Pehrson (RFC conversion).
- **Section 9 (Author's Address)**: Contact for L. Peter Deutsch, with questions to Gailly/Adler and editorial comments to Deutsch/Randers-Pehrson.