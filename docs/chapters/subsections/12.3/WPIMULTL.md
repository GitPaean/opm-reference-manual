### WPIMULTL -- Define Well Connection Multipliers (LGR)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPIMULTL](#__RefHeading___Toc628077_4263943340) keyword defines a well connection factor multiplier that scales the existing well connection factor values, for a well in a Local Grid Refinement ("LGR"). The resulting effect is scale the well's productivity at the reporting time step the keyword is entered.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well and well connection status data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the [WELSPECL](#__RefHeading___Toc147691_6053652) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | PIMULT | A real positive value that will be used to scale the well connection factors defined by I, J, K, C1 and C2 below. | 1.0 |
| 3 | LGRNAME | A character string of up to eight characters in length that defines the [LGR](#__RefHeading___Toc55049_4106839650) name for which the well [LGR](#__RefHeading___Toc55049_4106839650) connection multiplier factor (PIMULT) is being defined.<br>Note that LGRNAME must have been declared previously using the [WELSPECL](#__RefHeading___Toc147691_6053652) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur.<br>If defaulted with 1\* the [LGR](#__RefHeading___Toc55049_4106839650) on the [WELSPECL](#__RefHeading___Toc147691_6053652) keyword will be utilized. | Defined |
| 3 | I | An integer less than or equal to NX that defines the connection location in the I-direction. | 1\* |
| 4 | J | An integer less than or equal to NY that defines the connection location in the J-direction. | 1\* |
| 5 | K | An integer less than or equal to NZ that defines the connection location in the K-direction. | 1\* |
| 6 | C1 | An integer value that defines the first completion in the range.<br>Connections are lumped into completions via the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and C1 refers to the first completion number, as defined by the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and all the connections contained within the C1 completion | 1\* |
| 7 | C2 | An integer value that defines the last completion in the range.<br>Connections are lumped into completions via the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and C2 refers to the last completion number, as defined by the [COMPLUMP](#__RefHeading___Toc97655_3261743917) keyword, and all the connections contained within the C2 completion | 1\* |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.111: [WPIMULT](#__RefHeading___Toc121645_2412586160) Keyword Description

If variables I, J K, C1 and C2 are all defaulted with a negative value or 1\*, then PIMULT is applied to all the well connections in the well.

If variables I, J K, C1 and C2 are set to zero (meaning any or all values), or a positive value then PIMULT is applied to the defined connections. The defined connections are those with the I, J, K variables in the specified location and a completion number in the range specified by C1 and C2.

Note, that PIMULT is applied at the time the [WPIMULTL](#__RefHeading___Toc628077_4263943340) keyword is entered and is cumulative if applied to the same well connections, provided there are intervening report time steps between consecutive [WPIMULTL](#__RefHeading___Toc628077_4263943340) keywords. Consequently, if there are no intervening report time steps between consecutive [WPIMULTL](#__RefHeading___Toc628077_4263943340) keywords utilizing the same well connections, then only the last set is applied.

See also the [PIMULTAB](#__RefHeading___Toc121637_2412586160) keyword that defines productivity index multiplier versus water cut tables that are used to scaled a well's connection factors based on a wells connection current producing water cut. The keyword is documented in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines two vertical oil wells using the [WELSPECL](#__RefHeading___Toc147691_6053652) keyword and their associated connection data.

\--

\-- WELL LGR SPECIFICATION DATA

\--

\-- WELL GROUP LGR -LOCATION- BHP PHASE DRAIN INFLOW SHUT CROSS PVT

\-- NAME NAME NAME I J DEPTH FLUID AREA EQUA. IN FLOW TABLE

WELSPECL

OP01 PLAT OP01LGR 14 13 1\* OIL 1\* STD SHUT NO 1\* /

OP02 PLAT OP02LGR 28 96 1\* OIL 1\* STD SHUT NO 1\* /

/

\--

\-- WELL LGR CONNECTION DATA

\--

\-- WELL LGR \-\--LOCATION\-\-- OPEN SAT CONN WELL KH SKIN D DIR

\-- NAME NAME II JJ K1 K2 SHUT TAB FACT DIA FACT FACT FACT PEN

COMPDATL

OP01 OP01LGR 1\* 1\* 20 56 OPEN 1\* 1\* 0.708 1\* 1\* 1\* Z /

OP01 OP01LGR 1\* 1\* 75 100 SHUT 1\* 1\* 0.708 1\* 1\* 1\* Z / OP02 OP02LGR 1\* 1\* 75 100 OPEN 1\* 1\* 0.708 1\* 1\* 1\* Z /

OP03 OP02LGR 1\* 1\* 75 100 OPEN 1\* 1\* 0.708 1\* 1\* 1\* Z /

/

\--

\-- ASSIGN WELL CONNECTIONS TO COMPLETIONS

\--

\-- WELL LGR \-\-- LOCATION \-\-- COMPL

\-- NAME NAME II JJ K1 K2 NO. COMPLMPL OP03 OP02LGR 1\* 1\* 75 85 1 / COMPLETION NO. 01

OP03 OP21LGR 1\* 1\* 86 100 2 / COMPLETION NO. 02

/

\--

\-- DEFINE WELL CONNECTION MULTIPLIERS

\--

\-- WELL PI LGR \--LOCATION\-- COMPLETION

\-- NAME MULT NAME I J K FIRST LAST

WPIMULTL

OP01 1.250 OP01LGR 1\* 1\* 1\* 1\* 1\* /

OP02 0.750 OP01LGR 1\* 1\* 10 1\* 1\* /

OP03 1.100 OP02LGR 1\* 1\* 1\* 1 2 /

/

In this example the [WPIMULTL](#__RefHeading___Toc628077_4263943340) keyword scales the well productivity of well OP01 by 1.25, scales all the well connection factors in layer 10 only by 0.75 for well OP02, and for OP03, scales all the connections in completions one and two by 1.100.
