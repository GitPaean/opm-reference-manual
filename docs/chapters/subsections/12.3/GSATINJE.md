### GSATINJE -- Define Group Satellite Injection Rates

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [GSATINJE](#__RefHeading___Toc116596_332691817) keyword defines a satellite group's oil, gas and water injection rates in the model. Satellite groups are not connected to the reservoir model and therefore have no wells or subordinate groups associated with them, they are nevertheless connected to other higher level groups and higher level groups within a network model (if activated). Thus, they provide a means to "add-in" outside injection and production to the model without modeling the "add-in" reservoirs.

The keyword is used to define injection rates into the model from other sources (fields, reservoirs etc.) that are not defined in the current run. For example, if Fields A, B and C are all producing through a common plant, but only Field A is being modeled in the current input deck, then injection and production from Fields B and C can be incorporated into the model in order to meet the plant injection rates for Field A. Note in this case the import rates from Fields B and C are fixed, and therefore Field A would act like a "swing" injector to match the overall injection requirement.

+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 1                                                                                                                                        | > GRPNAME           | > A character string of up to eight characters in length that defines the satellite group name for which the group injection rates are being defined. The group named FIELD is the top most group and should not be used to define a satellite group.                                                                                                                                                      | > None |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy.                                                                                |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > Note that a satellite group cannot have subordinate groups or wells.                                                                                                                                                                                                                                                                                                                                     |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 2                                                                                                                                        | > TYPE              | > A defined character string that specifies the type of injection fluid. TYPE should be set to one of the following character strings:                                                                                                                                                                                                                                                                     | > None |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | 1)  GAS: for gas injection.                                                                                                                                                                                                                                                                                                                                                                                |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | 2)  OIL: for oil injection.                                                                                                                                                                                                                                                                                                                                                                                |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | 3)  WAT: for water injection.                                                                                                                                                                                                                                                                                                                                                                              |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > If the satellite group injects more than one phase then the rates should be specified in separate records.                                                                                                                                                                                                                                                                                               |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 3                                                                                                                                        | > RATE              | > A positive real value that defines the surface injection rate for the phase declared by the TYPE variable.                                                                                                                                                                                                                                                                                               | > 0.0  |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Liquid: stb/d                                                                                                                            | > Liquid: sm^3^/day | > Liquid: scc/hour                                                                                                                                                                                                                                                                                                                                                                                         |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
| > Gas: Mscf/d                                                                                                                              | > Gas: sm^3^/day    | > Gas: scc/hour                                                                                                                                                                                                                                                                                                                                                                                            |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 4                                                                                                                                        | > RESV              | > A positive real value that defines the reservoir volume injection rate for the phase declared by the TYPE variable for the satellite group.                                                                                                                                                                                                                                                              | > 0.0  |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > Generally, RESV should be set to zero, unless one wishes to have the satellite reservoir volume rate added to the group's superordinate groups. If RESV is set to zero for all satellite groups and if the superordinate group has a reservoir volume injection target, a voidage replacement target, or a production balancing fraction target, then only the non-satellite group volumes will be used. |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero.                                                                                                                                                                                                                                                                                                                     |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > rb/d                                                                                                                                     | > rm^3^/day         | > rcc/hour                                                                                                                                                                                                                                                                                                                                                                                                 |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > 5                                                                                                                                        | > CALRATE           | > A positive real value that defines the calorific injection rate used in the commercial compositional simulator.                                                                                                                                                                                                                                                                                          | > 0.0  |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     | > This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero.                                                                                                                                                                                                                                                                                                                     |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+
| > Notes:                                                                                                                                   |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
|                                                                                                                                            |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
| 1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/".   |                     |                                                                                                                                                                                                                                                                                                                                                                                                            |        |
+--------------------------------------------------------------------------------------------------------------------------------------------+---------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------+

::: caption
Table 12.45: GSATINJE Keyword Description
:::

::: caption
:::

See also the [GSATPROD](#__RefHeading___Toc202038_870710203) and [GRUPTREE](#__RefHeading___Toc118321_1596574740) keywords to define satellite production rates and the group hierarchy, respectively. For non-satellite groups see the [GCONINJE](#__RefHeading___Toc134874_2055188184) and [GCONPROD](#__RefHeading___Toc146746_4203985108) keywords. All the aforementioned keywords are in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The example below is based on an oil field, with the main field FLD-A being modeled in the input deck with two groups (FLD-A1 and FLD-A2), combined with one satellite field supplementing oil production and water injection (FLD-B).

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\--

\-- DEFINE GROUP TREE HIERARCHY

\-- LOWER HIGHER

\-- GROUP GROUP

GRUPTREE

FLD-A FIELD /

FLD-A1 FLD-A /

FLD-A2 FLD-A /

FLD-B FIELD /

/

\--

\-- GROUP PRODUCTION CONTROLS

\--

\-- GRUP CNTL OIL WAT GAS LIQ CNTL GRUP GUIDE GUIDE CNTL

\-- NAME MODE RATE RATE RATE RATE OPT CNTL RATE DEF WAT

GCONPROD

FIELD ORAT 20E3 30E3 50E3 1\* 1\* 1\* /

FLD-A FLD 20E3 30E3 50E3 1\* 1\* 1\* /

/ \--

\-- LOAD INCLUDE FILE - LOAD ALL WELLS AND VFP TABLES

\--

INCLUDE

\'FLD-A-P50-WELLS.INC\' /

\--

\-- GROUP INJECTION TARGETS AND CONSTRAINTS

\--

\-- GRUP FLUID CNTL SURF RESV REINJ VOID GRUP GUIDE GUIDE GRUP GRUP

\-- NAME TYPE MODE RATE RATE FRAC FRAC CNTL RATE DEF REINJ RESV

GCONINJE

FIELD WAT REIN 35E3 1\* 1\* 1.0 NO 1\* 1\* 1\* 1\* /

/ \--

\-- SATELLITE GROUP PRODUCTION CONTROLS

\--

\-- GRUP OIL WAT GAS RESV GAS CALORIFIC

\-- NAME RATE RATE RATE RATE LIFT RATE

GSATPROD

FLD-B 5E3 0.00 2E3 1\* 1\* /

/

\--

\-- SATELLITE GROUP INJECTION CONTROLS

\--

\-- GRUP FLUID SURF RESV CALORIFIC

\-- NAME TYPE RATE RATE RATEV

GSATINJE

FLD-B WAT 10E3 1\* 1\* /

/

\--

\-- ADVANCE SIMULATION BY REPORTING DATE

\--

DATES

1 FEB 2021 /

/

\--

\-- SATELLITE GROUP PRODUCTION CONTROLS

\--

\-- GRUP OIL WAT GAS RESV GAS CALORIFIC

\-- NAME RATE RATE RATE RATE LIFT RATE

GSATPROD

FLD-B 5E3 0.00 2E3 0.0 1\* /

/

\--

\-- SATELLITE GROUP INJECTION CONTROLS

\--

\-- GRUP FLUID SURF RESV CALORIFIC

\-- NAME TYPE RATE RATE RATEV

GSATINJE

FLD-B WAT 10E3 1\* 1\* /

/

Here FLD-B will supplement FLD-A's water re-injection rate by 10,000 stb/d, subject to a maximum field water injection rate of 35,000 stb/d on the [GCONINJE](#__RefHeading___Toc134874_2055188184) keyword. This means that FLD-A's maximum water injection rate cannot exceed 25,000 stb/d. In terms of oil rates, [GCONPROD](#__RefHeading___Toc146746_4203985108) defines a maximum oil rate of 20,000 stb/d of which 5,000 stb/d is from FLD-B. If any of the constraints on the [GCONINJE](#__RefHeading___Toc134874_2055188184) and [GCONPROD](#__RefHeading___Toc146746_4203985108) keywords are violated, then the appropriate action will occur only for FLD-A, in order to ensure the group constraints are honored.
