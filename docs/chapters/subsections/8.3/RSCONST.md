### RSCONST -- Define Constant GOR (Rs) for All Dead Oil PVT Fluids

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[RSCONST](#__RefHeading___Toc138398_332691817) defines a constant Gas-Oil Ratio ("GOR"), for all dead oil[^1] PVT fluids. If the oil has a constant and uniform dissolved gas concentration, GOR, and if the reservoir pressure never drops below the saturation pressure (bubble point pressure), then the model can be run more efficiently by omitting the [GAS](#__RefHeading___Toc38607_2267116897) and [DISGAS](#__RefHeading___Toc39767_2267116897) keywords from the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, treating the oil as a dead oil, and defining a constant Rs (GOR) value with keywords [RSCONST](#__RefHeading___Toc138398_332691817) or [RSCONSTT](#__RefHeading___Toc138400_332691817) in the [PROPS](#__RefHeading___Toc39329_784232322) section. This results in the model being run as a dead oil problem with no active gas phase. However, OPM Flow takes into account the constant Rs in the calculations and reporting.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > No.                                     | > Name                                       | > Description                                                                                                                  | > Default |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Field                                   | > Metric                                     | > Laboratory                                                                                                                   |           |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 1                                       | > [RS](#__RefHeading___Toc137361_1317547213) | > A real positive value that defines the dead oil GOR for all oil PVT tables in the model                                      | > None    |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Mscf/stb                                | > sm^3^/sm^3^                                | > scc/scc                                                                                                                      |           |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > 2                                       | > PRESS                                      | > A real positive value that defines that saturation pressure (bubble point pressure) for all the oil PVT tables in the model. | > None    |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > psia                                    | > barsa                                      | > atma                                                                                                                         |           |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+
| > Notes:                                  |                                              |                                                                                                                                |           |
|                                           |                                              |                                                                                                                                |           |
| 1)  The keyword is terminated by a "/".   |                                              |                                                                                                                                |           |
+-------------------------------------------+----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+-----------+

Table 8.133: RSCONST Keyword Description

See also the [RSCONSTT](#__RefHeading___Toc138400_332691817) keyword to define a different constant Rs to the various dead oil PVT tables and the [PVDO](#__RefHeading___Toc45803_719036256) and [PVCDO](#__RefHeading___Toc104054_57619843) keywords to enter the dead oil properties. All of the aforementioned keywords are in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

The example sets the dead oil GOR to 5 scf/stb and the bubble point pressure to 14.7 psia.

\--

\-- DEAD OIL PVT CONSTANT GOR AND SATURATION PRESSURE

\--

RSCONST

\-- RS PSAT

\-- MSCF/STB PSIA

\-- \-\-\-\-\-\-\-- \-\-\-\-\--

0.0050 14.7 /

[^1]: "Dead" oil is oil that it contains no dissolved gas or a relatively thick oil or residue that has lost its volatile components.
