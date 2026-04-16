<a id="__RefHeading___Toc97655_3261743917"></a>

### COMPLUMP -- Assign Well Connections to Completions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword assigns connections, as defined by the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, to completion intervals. This "lumping" of the connections to various completion intervals allows automatic workovers and economic criteria to be applied to the completions (that is a set of connections) as opposed to the connections. This allows for a more realistic approach for workovers operations.

For example, if the water cut criteria for working over a well was set to 95%, and the average grid block connection thickness was one meter, then once a well's water cut reached 95% the worst offending one meter connection would be shut-in. If the well's actual perforation interval was 10 meters and the 10 connections were lumped as one completion, then when the water cut limit of 95% is reach, the completion would be shut-in, that is all of the 10 connections within the completion would be shut-in.

As the keyword is used to lump connections into a completions, the simulator adds together the contribution from all connections in the completion and uses the total values to test the economic limits. Note that a connection can only belong to one completion. In addition, completions can be used instead of connections in the [WELOPEN](#__RefHeading___Toc268461_1366622701) and [WPIMULT](#__RefHeading___Toc121645_2412586160) keywords if the completions have been defined by [COMPLUMP](#__RefHeading___Toc97655_3261743917) for a well.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well connection data are being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | I | A positive integer greater than or equal to zero and less than or equal to NX that defines the connection location in the I-direction.<br>If set to zero or defaulted with 1\* then all connections in the I-direction that also satisfy J, K1 and K2 criteria are assigned the ICOMP completion number. | 0 |
| 3 | J | A positive integer greater than or equal to zero and less than or equal to NY that defines the connection location in the J-direction.<br>If set to zero or defaulted with 1\* then all connections in the J-direction that also satisfy I, K1 and K2 criteria are assigned the ICOMP completion number. | 0 |
| 4 | K1 | A positive integer greater than or equal to one and less than or equal to NZ that defines the UPPER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then the uppermost connection in the well is used. | 0 |
| 5 | K2 | A positive integer greater than or equal to K1 and less than or equal to NZ that defines the LOWER connection location in the K-direction.<br>If set to zero or defaulted with 1\* then the lowermost connection in the well is used. | 0 |
| 6 | ICOMP | An integer greater than or equal to one and less than or equal to MXCONS as defined on the [WELLDIMS](#__RefHeading___Toc82886_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the completion number of the currently defined set of connections.<br>If I, J, K1, K2 are all set to zero or defaulted to 1\*, then all connections in the well have the same completion number of ICOMP. | None |
| Notes:<br>1)  The keyword is followed by any number of records.<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.14: COMPLUMP Keyword Description

Multiple grid block connections can be defined on one record for vertical wells by assigning different values to K1 and K2, for deviated and horizontal wells this may not be possible and therefore each grid block connection must be separately defined by setting K1 equal to K2.

See also the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the connections for two vertical oil wells using the [COMPDAT](#__RefHeading___Toc97651_3261743917) keyword and the re-allocation of the connections to completions intervals using the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword.

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

OP01 14 13 20 56 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 14 13 75 100 SHUT 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP02 35 96 75 100 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

/

\--

\-- ASSIGN WELL CONNECTIONS TO COMPLETIONS

\--

\-- WELL \-\-- LOCATION \-\-- COMPL

\-- NAME II JJ K1 K2 NO. COMPLUMP OP01 1\* 1\* 20 56 1 / COMPLETION NO. 01

OP01 1\* 1\* 75 100 2 / COMPLETION NO. 02

OP02 1\* 1\* 75 85 1 / COMPLETION NO. 01

OP02 1\* 1\* 86 100 2 / COMPLETION NO. 02

/

Here the well OP01 connections (14, 13, 20) to (14, 13, 56) are assigned to completion number one and connections (14, 13, 75) to (14, 13, 100) are assigned to completion number two. Well OP02 has only one set of connection data from cells (35, 96, 75) to cells (35, 96, 100), but they have been split into two separate completion intervals, with connections (35, 96, 75) to (35. 96, 85) assigned to completion interval number one and (35, 96, 86) to (35, 96, 100) assigned to completion number two.
