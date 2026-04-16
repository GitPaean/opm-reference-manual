### WPMITAB -- Assign Well Polymer Molecular Model Injection Tables

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WPMITAB](#__RefHeading___Toc121649_24125861601) keyword assigns the well polymer molecular injection tables to water injection wells in OPM Flow\'s Polymer Molecular Weight Transport option, that uses the polymer molecular weight in calculating the polymer viscosity, as well as accounting for formation damage due to the water and polymer injection, by adjusting the wellbore skin pressure. This keyword should only be used if the [POLYMER](#__RefHeading___Toc38609_2267116897) and [POLYMW](#__RefHeading___Toc38609_22671168971) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section are also activated. The keyword assigns the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) tables that are defined via the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section.

+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                        | > WELNAME                                           | > A character string of up to eight characters in length, that defines the water injection well name, for which the well polymer molecular injection table, [PLYMWINJ](#__RefHeading___Toc473331_2124352571), is to be assigned.       | > None |
|                                                                                                                                            |                                                     |                                                                                                                                                                                                                                        |        |
|                                                                                                                                            |                                                     | > Note that the well name (WELNAME) must have been declared previously using the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, otherwise an error may occur. |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                        | > [PLYMWINJ](#__RefHeading___Toc473331_2124352571)  | > A positive integer value that defines the corresponding [PLYMWINJ](#__RefHeading___Toc473331_2124352571) table to be allocated to the water injection well.                                                                          | > 0    |
|                                                                                                                                            |                                                     |                                                                                                                                                                                                                                        |        |
|                                                                                                                                            |                                                     | > A value less than or equal to zero means that no PLYMWIN table is allocated to the well                                                                                                                                              |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                   |                                                     |                                                                                                                                                                                                                                        |        |
|                                                                                                                                            |                                                     |                                                                                                                                                                                                                                        |        |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |                                                     |                                                                                                                                                                                                                                        |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

Table 12.113: WPMITAB Keyword Description

See also the [PLYMWINJ](#__RefHeading___Toc473331_2124352571) keyword in the [PROPS](#__RefHeading___Toc39329_784232322) section, that describes the relationship of the injected polymer molecular weight as a function of polymer throughput and polymer velocity, for the simulator\'s Polymer Molecular Weight Transport option, as well as the [SKPRWAT](#__RefHeading___Toc473331_212435257111), [SKPRPOLY](#__RefHeading___Toc473331_21243525711), and [PLYVMH](#__RefHeading___Toc473331_21243525712) keywords, also in the [PROPS](#__RefHeading___Toc39329_784232322) section, that are the additional keywords required for the Polymer Molecular Weight Transport option.

The [WSKPTAB](#__RefHeading___Toc121649_241258616011) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section may be used to assign the [SKPRWAT](#__RefHeading___Toc473331_212435257111) and SKPRPOL tables to water injections wells, that enable the calculation of the wellbore skin pressure based on the fluids being injected.

Note that the standard polymer property data keywords: [PLYROCK](#__RefHeading___Toc110216_2939291539), [PLYADS](#__RefHeading___Toc121087_57619843), [PLYMAX](#__RefHeading___Toc110214_2939291539), etc., are still required to fully describe the polymer fluid.

#### Example

Given NTPMWINJ equals two on the [PINTDIMS](#__RefHeading___Toc637730_5168988431) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then:

\--

\-- ASSIGN WELL POLYMER MOLECULAR MODEL INJECTION TABLES

\--

\-- WELL PLYMWINJ

\-- NAME TABLE

WPMITAB

WI01 1 /

WI02 1 /

WI03 2 /

/

Assigns [PLYMWINJ](#__RefHeading___Toc473331_2124352571) table one to wells WI01 and WI02 and table two to WI03.
