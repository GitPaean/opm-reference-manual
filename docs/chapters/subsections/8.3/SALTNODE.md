### SALTNODE -- Salt Concentration Based PVTNUM Array

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[SALTNODE](#__RefHeading___Toc13101_421927891) defines the salt concentration value based on a cells [PVTNUM](#__RefHeading___Toc68366_2752266063) number. The [SALTNODE](#__RefHeading___Toc13101_421927891) property is used in the calculation of a polymer viscosity when the polymer and the salt options has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) and [BRINE](#__RefHeading___Toc162083_289573908) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section the number of [PVTNUM](#__RefHeading___Toc68366_2752266063) functions is declared by NTPVT variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword and allocated to individual cells by the [PVTNUM](#__RefHeading___Toc68366_2752266063) property array in the [REGIONS](#__RefHeading___Toc40648_784232322) section. NPPVT on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section defines the maximum number of rows (or pressure values) in the PVT tables and also sets the maximum number of entries for each SALNODE data set. The number of values for each data set must correspond to the number of polymer solution adsorption entries on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword. For example if there are three sets of PVT tables and four values on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword, then three [SALTNODE](#__RefHeading___Toc13101_421927891) data sets with four values of salt concentrations need to be entered.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+
| > No.                                                                                                                  | > Name                                           | > Description                                                                                                                                               | > Default |              |    |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+
|                                                                                                                        |                                                  | > Field                                                                                                                                                     | > Metric  | > Laboratory |    |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+
| > 1                                                                                                                    | > [SALTNODE](#__RefHeading___Toc13101_421927891) | > A real monotonically increasing positive columnar vector defining the salt concentration for a given [PVTNUM](#__RefHeading___Toc68366_2752266063) table. | > None    |              |    |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+
| > lb/stb                                                                                                               | > kg/sm3                                         | > gm/scc                                                                                                                                                    |           |              |    |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+
| > Notes:                                                                                                               |                                                  |                                                                                                                                                             |           |              |    |
|                                                                                                                        |                                                  |                                                                                                                                                             |           |              |    |
| 1)  Each table is terminated by a "/" including the last table; however, there is no "/" terminator for the keyword.   |                                                  |                                                                                                                                                             |           |              |    |
+------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+--------------+----+

Table 8.141: SALTNODE Keyword Description

An alternative manner of entering the salt concentrations is by utilizing the [PVTNUM](#__RefHeading___Toc68366_2752266063) region array by using the [ADSALNOD](#__RefHeading___Toc4416_421927891) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

#### Example

Given three sets of relative permeability tables and four values on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword and two SALNODE data sets with four values of salt concentrations then the data should be entered as follows:

\--

\-- SETS SALT CONCENTRATION FOR POLYMER SOLUTION ADSORPTION

\-- VIA PVTNUM ARRAY ALLOCATION

\--

\-- SALT

\--

SALTNODE

1.0

5.0

10.5

25.0 / PVTNUM TABLE NO. 01

1.0

3.0

7.5

15.0 / PVTNUM TABLE NO. 02

See also the [ADSALNOD](#__RefHeading___Toc4416_421927891) keyword.
