### ADSALNOD -- Salt Concentration Based on SATNUM Array

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[ADSALNOD](#__RefHeading___Toc4416_421927891) defines the salt concentration value based on a cells [SATNUM](#__RefHeading___Toc71136_2752266063) number. The [ADSALNOD](#__RefHeading___Toc4416_421927891) property is used in the calculation of a polymer viscosity when the polymer and the salt options has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) and [BRINE](#__RefHeading___Toc162083_289573908) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. In the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section the number of [SATNUM](#__RefHeading___Toc71136_2752266063) functions is declared by the NTSFUN variable on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword and allocated to individual cells by the [SATNUM](#__RefHeading___Toc71136_2752266063) property array in the [REGIONS](#__RefHeading___Toc40648_784232322) section. NSSFUN on the [TABDIMS](#__RefHeading___Toc89327_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section defines the maximum number of rows (or saturation values) in the relative permeability saturation tables and also sets the maximum number of entries for each [ADSALNOD](#__RefHeading___Toc4416_421927891) data set. The number of values for each data set must correspond to the number of polymer solution adsorption entries on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword. For example, if there are three sets of relative permeability tables and four values on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword, then three [ADSALNOD](#__RefHeading___Toc4416_421927891) data sets with four values of salt concentrations need to be entered.

The salt concentrations within each data set should be positive and monotonically increasing and each [ADSALNOD](#__RefHeading___Toc4416_421927891) data set is delimited by "/" including the last data set.

+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+
| > No.                                                                                                                      | > Name    | > Description | > Default |              |        |
+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+
| > 1                                                                                                                        | > SALTCON | > Field       | > Metric  | > Laboratory | > None |
+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+
| > A real positive columnar vector that sets the salt concentrations for the given relative permeability saturation tables. |           |               |           |              |        |
|                                                                                                                            |           |               |           |              |        |
+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+
| > lb/stb                                                                                                                   | > kg/sm3  | > gm/scc      |           |              |        |
+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+
| > Notes:                                                                                                                   |           |               |           |              |        |
|                                                                                                                            |           |               |           |              |        |
| 1)  Each data set must be terminated by a "/" including the last data set.                                                 |           |               |           |              |        |
+----------------------------------------------------------------------------------------------------------------------------+-----------+---------------+-----------+--------------+--------+

Table 8.17: ADSALNOD Keyword Description

An alternative manner of entering the salt concentrations is by utilizing the [PVTNUM](#__RefHeading___Toc68366_2752266063) region array by using the [SALTNODE](#__RefHeading___Toc13101_421927891)* *keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

Given three sets of relative permeability tables and four values on the [PLYADSS](#__RefHeading___Toc121089_57619843) keyword, then the data salt concentration should be entered as follows:

\--

\-- SETS SALT CONCENTRATION FOR POLYMER SOLUTION ADSORPTION

\-- VIA SATNUM ARRAY ALLOCATION

\--

\-- SALT

\--

ADSALNOD

1.0

5.0

10.5

25.0 / SATNUM TABLE NO. 01

1.0

3.0

7.5

15.0 / SATNUM TABLE NO. 02

1.0

7.5

20.5

35.0 / SATNUM TABLE NO. 03

See also the [SALTNODE](#__RefHeading___Toc13101_421927891)* *keyword.
