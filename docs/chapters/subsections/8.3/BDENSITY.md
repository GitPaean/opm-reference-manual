### BDENSITY -- Define the Surface Brine Density for the Fluid

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[BDENSITY](#__RefHeading___Toc223317_1539708736) defines the brine surface density for when the brine phase has been activated in the model by the [BRINE](#__RefHeading___Toc162083_289573908) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The number of [BDENSITY](#__RefHeading___Toc223317_1539708736) vector data sets is defined by the NTPVT parameter on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Each record consists of a maximum of NPPVT values, as declared on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, with each value representing a brine surface density.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

The keyword is used in conjunction with the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, with each brine density value matching with the salt concentration values in column 1 of each table in the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword. Note that the [BDENSITY](#__RefHeading___Toc223317_1539708736) keyword is optional, and if absent from the input file, then the brine surface densities will be set to the water density values declared via the [DENSITY](#__RefHeading___Toc45799_719036256) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section. In this case there is no variation in brine surface density with respect to salt concentration.

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+
| > No.                                                                                                                                                                                                                                                                                            | > Name   | > Description | > Default |              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+
| > 1                                                                                                                                                                                                                                                                                              | > WATDEN | > Field       | > Metric  | > Laboratory | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+
| > WATDEN is a real monotonically increasing positive row vector that defines the brine density at surface conditions for the given salt concentrations on the corresponding [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.  |          |               |           |              |        |
|                                                                                                                                                                                                                                                                                                  |          |               |           |              |        |
| > There should be one row element for each salt concentration columnar element (SALTCON) on the [PVTWSALT](#__RefHeading___Toc331848_501926209) keyword.                                                                                                                                         |          |               |           |              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+
| > lb/ft^3^                                                                                                                                                                                                                                                                                       | > kg/m   | > gm/cc       |           |              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+
| > Notes:                                                                                                                                                                                                                                                                                         |          |               |           |              |        |
|                                                                                                                                                                                                                                                                                                  |          |               |           |              |        |
| 1)  Each row vector data set must be terminated by a "/" including the last data set.                                                                                                                                                                                                            |          |               |           |              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------+---------------+-----------+--------------+--------+

Table 8.24: BDENSITY Keyword Description

#### Example

The following shows the [BDENSITY](#__RefHeading___Toc223317_1539708736) and [PVTW](#__RefHeading___Toc2086106_3315222525)[SALT](#__RefHeading___Toc593214_516898843) keywords for when NTPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section is set equal to two and NPPVT is set to greater than four on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword.

\--

\-- BRINE WATER DENSITY DATA FOR PVTWSALT KEYWORD

\--

\-- SALTCON SALTCON SALTCON SALTCON SALTCON \-- DENSITY DENSITY DENSITY DENSITY DENSITY

\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-\--

BDENSITY

62.20 63.50 64.75 65.90 / FOR PVTWSALT TABLE 1

64.00 65.50 67.00 / FOR PVTWSALT TABLE 2 \--

\-- WATER SALT PVT TABLE

\--

PVTWSALT

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4500.0 0.000 / TABLE NO. REF. DATA

\--

\-- SALTCONC BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.020 2.7E-6 0.370 0.0

2.0 1.010 2.7E-6 0.370 0.0

4.0 1.000 2.7E-6 0.370 0.0

10.0 0.950 2.7E-6 0.370 0.0 / TABLE NO. 01 SALT DATA

\--

\-- REF PRES REF SALT

\-- PSIA LB/STB

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

4000.0 0.000 / TABLE NO. 02 REF. DATA

\--

\-- SALTCONC BW CW VISC VISC

\-- LB/STB RB/STB 1/PSIA CPOISE GRAD

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-- \-\-\-\-\-- \-\-\-\-\--

0.0 1.005 2.5E-6 0.320 0.0

6.0 0.985 2.5E-6 0.320 0.0

12.0 0.930 2.5E-6 0.320 0.0 / TABLE NO. 02 SALT DATA
