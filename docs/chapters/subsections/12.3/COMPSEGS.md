### COMPSEGS -- Define Well Connections for Multi-Segment Wells

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword defines how a multi-segment well is connected to the reservoir by allocating each well connection to a well segement. Note that the well must have previously been defined as a multi-segment well using the [WELSEGS](#__RefHeading___Toc97661_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and the well connections must have previously been defined via the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

The [COMPSEGS](#__RefHeading___Toc316604_3519154785) keyword should be repeated for each multi-segment well in the model.

| 1-1 | WELNAME | A character string of up to eight characters in length that defines the well name for which a multi-segment well is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 1-2 | / | Record terminated by a "/" | Not Applicable |
| 2-1 | I | A positive integer greater than or equal to one and less than or equal to NX that defines the connection location in the I-direction. | None |
| 2-2 | J | A positive integer greater than or equal to one and less than or equal to NY that defines the connection location in the J-direction. | None |
| 2-3 | K | A positive integer greater than or equal to one and less than or equal to NZ that defines the connection location in the K-direction. | None |
| 2-4 | IBRANCH | A positive integer greater than or equal to one and less than or equal to MXBRAN on [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that defines the branch number of the defined I, J and K connection. | None |
| 2-5 | LENGTH1 | A real positive value that defines the length of the tubing from the tubing reference point (for example Measure Depth Relative to Kelly Bushing, MDRKB) to the *start* of the connection in the I, J, K cell. | None |
| feet | m | cm |  |
| 2-6 | LENGTH2 | A real positive value that defines the length of the tubing from the tubing reference point to the *end* of the connection in the I, J, K cell. |  |
| feet | m | cm | None |
| 2-7 | DIRECT | A one letter character string that defines the orientation of the connections and should be set to either X, Y or Z, or either I, J or K. The direction of connections may also determine the length of the connection.<br>Currently this option is not supported by OPM Flow. | None |
| 2-8 | IJKEND | A positive integer that is set to one of the following depending on the orientation of the connections (DIRECT):<br>1)  X or I: A value between 1 and NX that defines the last connection location in the I-direction,<br>2)  Y or J: A value between 1 and NY that defines the last connection location in the J-direction, or<br>3)  Z or K: A value between 1 and NZ that defines the last connection location in the K-direction.<br>For example, if DIRECT is equal to Y or J then the IJKEND will be associated with the J-direction. The value may be less than or greater than Y or J but must be between 1 and NY.<br>Currently this option is not supported by OPM Flow. | None |
| 2-9 | DEPTH | A real positive value that defines the datum depth for this set of connections, normally taken as the mid-point of the perforations associated with this set of connections.<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-10 | THLEN | A real positive value that defines the length of the well in the connection cells for this set of completions that is used in thermal calculations. If this value is defaulted then the thickness of the cell in the direction of the well orientation (DIRECT) is used.<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-11 | ISEG | A real positive value that defines the segment number to assign to this range of connections. If this value is defaulted then each connection is assigned to the segment with the nodal point nearest to the centre of the connection.<br>Currently this option is not supported by OPM Flow. | None |
| feet | m | cm |  |
| 2-12 | / | Record terminated by a "/" | Not Applicable |
| Notes:<br>1)  Each multi-segment wells must be defined by a separate [COMPSEGS](#__RefHeading___Toc316604_3519154785) keyword that consists of two records, with entries 1-1 to 1-2 representing record one items and 2-1 to 2-12 representing record number two items in the "No." column in this table.<br>2)  Record number two of the keyword, items 2-1 to 2-12 can be repeated up to a maximum of MXCONS times as declared on the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each of the records are terminated by a "/" and is explicitly shown in the above rows and the keyword should be terminated by a "/". |  |  |  |

Table 12.17: COMPSEGS Keyword Description

The maximum number of wells and completions should be defined via the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword and the maximum number of multi-segment wells, segments and branches should be declared on the [WSEGDIMS](#__RefHeading___Toc104259_3115110868) keyword, both keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

See also the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword to define wells, the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword to define the well connections for both standard wells and multi-segment wells, and the [COMPSEGL](#__RefHeading___Toc97659_3261743917) keyword to define multi-segment connections in a [LGR](#__RefHeading___Toc55049_4106839650). All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the completions for two multi-segment oil production wells (OP01 and OP02) using the [COMPSEGS](#__RefHeading___Toc316604_3519154785) keyword.

\-- COMPLETION SEGMENT SPECIFICATION DATA

\--

\-- WELL

\-- NAME

COMPSEGS

OP01 /

\-- \--LOCATION\-- BRAN START END DIR LOC MID COMP ISEG

\-- II JJ K1 NO LENGTH LENGTH PEN I,J,K PERFS LENGTH

10 10 1 1 2512.5 2525.0 /

10 10 2 1 2525.0 2550.0 /

10 10 3 1 2550.0 2575.0 /

10 10 4 1 2575.0 2600.0 /

10 10 5 1 2600.0 2625.0 /

10 10 6 1 2625.0 2650.0 /

9 10 2 2 2637.5 2837.5 /

8 10 2 2 2837.5 3037.5 /

7 10 2 2 3037.5 3237.5 /

6 10 2 2 3237.5 3437.5 /

5 10 2 2 3437.5 3637.5 /

/

\-- COMPLETION SEGMENT SPECIFICATION DATA

\--

\-- WELL

\-- NAME

COMPSEGS

OP02 /

\-- \--LOCATION\-- BRAN START END DIR LOC MID COMP ISEG

\-- II JJ K1 NO LENGTH LENGTH PEN I,J,K PERFS LENGTH

1 9 3 1 2662.5 2862.5 /

1 8 3 1 2862.5 3062.5 /

1 7 3 1 3062.5 3262.5 /

1 6 3 1 3262.5 3462.5 /

1 5 3 1 3462.5 3662.5 /

2 10 5 2 2712.5 2912.5 /

2 10 5 2 2912.5 3112.5 /

4 10 5 2 3112.5 3312.5 /

5 10 5 2 3312.5 3512.5 /

6 10 5 2 3512.5 3712.5 /

1 9 6 3 2737.5 2937.5 /

1 8 6 3 2937.5 3137.5 /

1 7 6 3 3137.5 3337.5 /

1 6 6 3 3337.5 3537.5 /

1 5 6 3 3537.5 3737.5 /

/

Note that the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section must also be defined for these two wells.
