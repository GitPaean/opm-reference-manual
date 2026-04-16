### WPIMULT -- Define Well Connection Multipliers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword defines a well connection factor multiplier that scales the existing well connection factor values. The resulting effect is to scale the well's productivity at the reporting time step the keyword is entered.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well and well connection status data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | PIMULT | A real positive value that will be used to scale the well connection factors defined by I, J, K, C1 and C2 below. | 1.0 |
| 3 | I | An integer less than or equal to NX that defines the connection locations in the I-direction. | 1\* |
| 4 | J | An integer less than or equal to NY that defines the connection locations in the J-direction. | 1\* |
| 5 | K | An integer less than or equal to NZ that defines the connection locations in the K-direction. | 1\* |
| 6 | C1 | An integer value that defines the first completion number in the range.<br>Connections are lumped into completions via the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and C1 refers to the first completion number, as defined by the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and all the connections contained within the C1 completion. | 1\* |
| 7 | C2 | An integer that defines the last completion in the range.<br>Connections are lumped into completions via the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and C2 refers to the last completion number, as defined by the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and all the connections contained within the C2 completion. | 1\* |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.110: WPIMULT Keyword Description

If variables I, J, K, C1 and C2 are all negative values or defaulted with 1\*, then PIMULT is applied to all the well connections in the well.

If any of the variables I, J, K, C1 and C2 are set to zero (meaning any or all values), or a positive value then PIMULT is applied to the defined connections. The defined connections are those with the I, J, K variables in the specified location and a completion number in the range specified by C1 and C2.

Note, that PIMULT is applied at the time the [WPIMULT](#__RefHeading___Toc121645_2412586160) keyword is entered and is cumulative if applied to the same well connections, provided there are intervening report time steps between consecutive [WPIMULT](#__RefHeading___Toc121645_2412586160) keywords. Consequently, if there are no intervening report time steps between consecutive [WPIMULT](#__RefHeading___Toc121645_2412586160) keywords utilizing the same well connections, then only the last set is applied.

See also the [WELPI](#__RefHeading___Toc121389_332691817) keyword to set a well's productivity or injectivity index at the time the keyword is activated, and also the [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword that defines productivity index multiplier versus water cut tables that are used to scaled a well's connection factors based on a wells connection current producing water cut. Both keywords are documented in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines three vertical oil wells using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword and their associated connection data.

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW SHUT CROSS PRESS

\-- NAME NAME I J DEPTH FLUID AREA EQUA. IN FLOW TABLE

WELSPECS

OP01 PLATFORM 14 13 1\* OIL 1\* STD OPEN NO 1\* /

OP02 PLATFORM 28 96 1\* OIL 1\* STD OPEN NO 1\* /

OP03 PLATFORM 128 56 1\* OIL 1\* STD OPEN NO 1\* /

/

\--

\-- WELL PRODUCTION WELL CONTROLS

\--

\-- WELL OPEN/ CNTL OIL WAT GAS LIQ RES BHP THP VFP VFP

\-- NAME SHUT MODE RATE RATE RATE RATE RATE PRES PRES TABLE ALFQ

WCONPROD

'\*' SHUT GRUP 1\* 1\* 1\* 1\* 1\* 200.0 /

/

\--

\-- WELL CONNECTION DATA

\--

\-- WELL \-\-- LOCATION \-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDAT

OP01 1\* 1\* 1 10 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 1\* 1\* 15 30 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP01 1\* 1\* 35 90 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP02 1\* 1\* 1 10 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

OP03 1\* 1\* 35 90 OPEN 1\* 1\* 0.708 1\* 0.0 1\* \'Z\' /

/

\-- ASSIGN WELL CONNECTIONS TO COMPLETIONS

\--

\-- WELL \-\-- LOCATION \-\-- COMPL

\-- NAME II JJ K1 K2 NO. COMPLUMP OP03 1\* 1\* 35 45 1 / COMPLETION NO. 01

OP03 1\* 1\* 50 90 2 / COMPLETION NO. 02

/

\--

\-- DEFINE WELL CONNECTION MULTIPLIERS

\--

\-- WELL PI \--LOCATION\-- COMPLETION

\-- NAME MULT I J K FIRST LAST

WPIMULT

OP01 1.250 1\* 1\* 1\* 1\* 1\* /

OP02 0.750 1\* 1\* 10 1\* 1\* /

OP03 1.100 1\* 1\* 1\* 1 2 /

/

In this example the [WPIMULT](#__RefHeading___Toc121645_2412586160) scales the well productivity of well OP01 by 1.25, and scales all the well connection factors in layer 10 only by 0.75 for well OP02. For well OP03, [WPIMULT](#__RefHeading___Toc121645_2412586160) scales all the connections in completions one and two by 1.1.
