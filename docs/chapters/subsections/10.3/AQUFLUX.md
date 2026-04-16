### AQUFLUX -- Define Constant Flux Analytical Aquifer

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [AQUFLUX](#__RefHeading___Toc202105_1310555686) keyword defines the properties of Constant Flux Analytical Aquifers, that allows for a constant water influx to the connected grid blocks. This type of aquifer is connected to the model using either the [AQUANCON](#__RefHeading___Toc177536_3429068809) keyword for global cells, or the AQUANCONL keyword for cells belonging to a Local Grid Refinement (\"[LGR](#__RefHeading___Toc55049_4106839650)\"), both the aforementioned keywords are in the [GRID](#__RefHeading___Toc38674_784232322) and [SOLUTION](#__RefHeading___Toc43947_784232322) sections. The keyword itself may be utilized in both the [SOLUTION](#__RefHeading___Toc43947_784232322) and [SCHEDULE](#__RefHeading___Toc43945_784232322) sections, with subsequent entries overwriting the previous entry.

| 1 | AQUID | A positive integer greater than or equal to one and less than or equal to NANAQ on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, that defines the [AQUFLUX](#__RefHeading___Toc202105_1310555686) aquifer number. | 1 |
| --- | --- | --- | --- |
| ‍2<br>‍ | | AQFLUX<br>| | | A real positive value the defines the aquifer water influx rate, per unit area of the connected grid cell face.<br>| | | None<br>| |
| stb/day/ft2 | sm^3^/day/m2 | scc/hour/cm2 |  |
| 3 | SALTCON | SALTCON is a real positive number that defines the initial salt concentration in the aquifer, for when with simulator\'s Brine Model has been activated via the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>This variable is ignored by OPM Flow. | 0.0 |
| lb/stb | kg/sm^3^ | gm/scc |  |
| 4 | TEMP | TEMP is a real positive number that defines the initial temperature of the aquifer for use with OPM Flow\'s thermal option. The [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be activated to use this option. If the [THERMAL](#__RefHeading___Toc137276_650382403) keyword is absent from the input deck, then the parameter is ignored. | 1\* |
| ^o^F | ^o^C | ^o^C |  |
| 5 | PRESS | PRESS is a single positive value that defines the aquifer pressure for use with OPM Flow\'s thermal option. The [THERMAL](#__RefHeading___Toc137276_650382403) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section must be activated to use this option. If the [THERMAL](#__RefHeading___Toc137276_650382403) keyword is absent from the input deck, then the parameter is ignored. | 1\* |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by up to NANAQ records as defined on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section<br>2)  Each record is terminated by a "/" and the keyword should be terminated by a "/". Note the commercial simulator only requires a terminating "/" if the number of records on this keyword are less than NANAQ on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. If the number of records are equal to NANAQ and a terminating "/" has been entered then the commercial simulator will issue a warning message; however, the commercial simulator run will proceed as expected. |  |  |  |

Table 10.9: AQUFLUX Keyword Description

The water flow rate into a connected grid cell for this type of aquifer, is calculated from:

Where:

[AQUFLUX](#__RefHeading___Toc202105_1310555686)(AQFLUX) = the AQFLUX parameter on the [AQUFLUX](#__RefHeading___Toc202105_1310555686) keyword,

[AQUANCON](#__RefHeading___Toc177536_3429068809)(AQUCOEF) = the AQUCOEF parameter on the [AQUANCON](#__RefHeading___Toc177536_3429068809) keyword

Note that is calculated from the connected cell geometry, and thus the [AQUANCON](#__RefHeading___Toc177536_3429068809)([AQUFLUX](#__RefHeading___Toc202105_1310555686)) and the AQUANCONL([AQUFLUX](#__RefHeading___Toc202105_1310555686)) parameters are ignored for this type of aquifer.

The [AQUFLUX](#__RefHeading___Toc202105_1310555686) keyword should only be used in runs that have been initialized by equilibration or with enumerated values, and should not be used in [RESTART](#__RefHeading___Toc135629_1317547213) runs.

See also the [BCCON](#REF_HEADING_KEYWORD_BCCON) keyword in the [GRID](#__RefHeading___Toc38674_784232322) section and the [BCPROP](#REF_HEADING_KEYWORD_BCPROP) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that can be used to specify boundary conditions.

#### Example

Given a total of five analytical aquifers as declared by the NANAQ parameter on the [AQUDIMS](#__RefHeading___Toc10103_3701168388) keyword being set to five, of which three are Constant Flux Aquifers and two Carter-Tracy Aquifers, then:

\--

\-- CONSTANT FLUX AQUIFER DESCRIPTION

\--

\-- ID WATER SALT AQF AQU

\-- NUM INFLUX CONC TEMP PRES

\--

AQUFLUX

1 0.0004 1\* 1\* 1\* /

2 0.0005 1\* 1\* 1\* /

3 0.0003 1\* 1\* 1\* /

/

\--

\-- CARTER-TRACY AQUIFER DESCRIPTION

\--

\-- ID DATUM AQF AQF AQF AQF AQF AQF INFL PVT AQU

\-- NUM DEPTH PRESS PERM PORO RCOMP RE DZ ANGLE NUM TAB

\--

AQUCT

4 2000.0 269 100.0 0.30 3.0e-5 330 10.0 360.0 1 2 /

5 2000.0 269 100.0 0.30 3.0e-5 330 10.0 360.0 1 2 /

/

Defines three Constant Flux Aquifers and three Carter-Tracy Aquifers, and the connection of the aquifers are set in the [GRID](#__RefHeading___Toc38674_784232322) or [SOLUTION](#__RefHeading___Toc43947_784232322) sections via:

\--

\-- ANALYTIC AQUIFER CONNECTION

\--

\-- ID \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\-- CONNECT AQF AQF ADJOIN

\-- NUMBER I1 I2 J1 J2 K1 K2 FACE INFLX MULTI CELLS

AQUANCON

1 1 198 1 14 1 10 J- 1\* 1.0 \'NO\' /

2 1 198 1 14 12 22 J- 1\* 1.0 \'NO\' /

3 1 198 1 14 23 54 J- 1\* 1.0 \'NO\' /

4 1 198 1 14 61 70 J- 1\* 1.0 \'NO\' /

5 1 198 15 172 71 71 K+ 1\* 1.0 \'NO\' /

/
