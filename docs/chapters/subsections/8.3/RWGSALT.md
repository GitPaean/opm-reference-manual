### RWGSALT -- Water Vaporization versus Pressure and Salt Concentration

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[RWGSALT](#__RefHeading___Toc304264_1667959253) defines the relationship of water vaporization versus pressure and salt concentration. This keyword should be used when the [VAPWAT](#__RefHeading___Toc317543_3149455253) keyword has be declared in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section indicating that vaporized water is present in the gas phase. In addition, if the Salt Precipitation model has been activated via the [BRINE](#__RefHeading___Toc162083_289573908) and [PRECSALT](#__RefHeading___Toc332782_3149455253) keywords, also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then this keyword must be present. The keyword may be used for gas-water and oil-water-gas input decks that contain the either dry or wet gas and vaporized water phases.

+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                    | > PRESS       | > A real monotonically increasing down the column values that define the gas phase pressure, that together with salt concentration, defines the vaporized water in gas ratio ("VWGR") or Rw | > None |
|                                                                                                                        |               |                                                                                                                                                                                             |        |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > psia                                                                                                                 | > barsa       | > atma                                                                                                                                                                                      |        |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                    | > SALTCON     | > A real monotonically increasing positive columnar vector defining the salt concentration in water.                                                                                        | > None |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > lb/stb                                                                                                               | > kg/sm3      | > gm/scc                                                                                                                                                                                    |        |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                                                    | > RW          | > A columnar vector of real positive number values defining the vaporized water in gas ratio (Rw) that for a given PRESS and SALTCON.                                                       | > None |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > stb/Mscf                                                                                                             | > sm^3^/sm^3^ | > scc/scc                                                                                                                                                                                   |        |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                               |               |                                                                                                                                                                                             |        |
|                                                                                                                        |               |                                                                                                                                                                                             |        |
| 1)  Each table is terminated by a "/" including the last table; however, there is no "/" terminator for the keyword.   |               |                                                                                                                                                                                             |        |
+------------------------------------------------------------------------------------------------------------------------+---------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 8.139: RWGSALT Keyword Description

Since the water component is in both the water and the gas phases, [RWGSALT](#__RefHeading___Toc304264_1667959253) controls the amount of water component evaporated from the water phase into the gas phase, which is a function of both the water phase salinity and a grid cells pressure. The keyword should be used in conjunction with the dry gas [PVTGW](#__RefHeading___Toc355649_3149455253) keyword or the wet gas [PVTGWO](#__RefHeading___Toc356776_4176551521) keyword, both of which are in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The example defines two [RWGSALT](#__RefHeading___Toc304264_1667959253) tables assuming NTPVT equals two and NPPVT is greater than or equal to eight on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\--

\-- WATER VAPORIZATION TABLE FOR BRINE (OPM FLOW KEYWORD)

\--

RWGSALT

\-- PRES SALTCONC RVW

\-- PSIA LB/STB STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\--

300 0 0.000132

0.5 0.000132

1 0.000132 /

600 0 0.000132

0.5 0.000132

1 0.000132 /

900 0 0.000132

0.5 0.000132

1 0.000132 /

1200 0 0.000132

0.5 0.000132

1 0.000132 /

1500 0 0.000132

0.5 0.000132

1 0.000132 /

1800 0 0.000132

0.5 0.000132

1 0.000132 /

2100 0 0.000132

0.5 0.000132

1 0.000132 /

2400 0 0.000132

0.5 0.000132

1 0.000132 /

/ Table NO. 1

\-- PRES SALTCONC RW

\-- PSIA LB/STB STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\-\-\-- \-\-\-\-\-\-\-\--

300 0 0.000132

0.5 0.000132

1 0.000132 /

600 0 0.000132

0.5 0.000132

1 0.000132 /

900 0 0.000132

0.5 0.000132

1 0.000132 /

1200 0 0.000132

0.5 0.000132

1 0.000132 /

1500 0 0.000132

0.5 0.000132

1 0.000132 /

1800 0 0.000132

0.5 0.000132

1 0.000132 /

2100 0 0.000132

0.5 0.000132

1 0.000132 /

2400 0 0.000132

0.5 0.000132

1 0.000132 /

/ Table NO. 2
