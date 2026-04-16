### WSURFACT -- Define Water Injection Well Surfactant Concentration

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

[WSURFACT](#__RefHeading___Toc1103962_4263943340) defines a water injection well's surfactant concentration in the injection stream that is to be used when the Surfactant phase has been activated by either the [SURFACT](#__RefHeading___Toc863854_4250154414) or [SURFACTW](#__RefHeading___Toc863864_4250154414) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

+--------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                        | > WELNAME  | > A character string of up to eight characters in length that defines the well name of a gas injection well for which the solvent fraction data is being defined.                                                                      | > None |
|                                                                                                                                            |            |                                                                                                                                                                                                                                        |        |
|                                                                                                                                            |            | > Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                        | > SURCON   | > A real positive value that defines the surfactant concentration of the well's injection stream.                                                                                                                                      | > None |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > lb/stb                                                                                                                                   | > kg/sm^3^ | > gm/scc                                                                                                                                                                                                                               |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                   |            |                                                                                                                                                                                                                                        |        |
|                                                                                                                                            |            |                                                                                                                                                                                                                                        |        |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |            |                                                                                                                                                                                                                                        |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.125: WSURFACT Keyword Description

Water injection wells that are not declared via this keyword have their surfactant concentrations set to zero.

See also the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword to define a group's injection targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the surfactant concentrations for three water injection wells for when the surfactant phase option has been activated by either the [SURFACT](#__RefHeading___Toc863854_4250154414) or [SURFACTW](#__RefHeading___Toc863864_4250154414) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. Here the surfactant concentration has been set to 0.200 for all three wells.

\--

\-- DEFINE WATER INJECTION WELL SURFACTANT CONCENTRATION

\--

\-- WELL SURFACT

\-- NAME SURCON

\-- \-\-\-\-\-\-\--

WSURFACT

WI01 0.2000 /

WI02 0.2000 /

WI03 0.2000 /

/
