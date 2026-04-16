### GCONENG -- Group Production Energy Targets

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [GCONCAL](#__RefHeading___Toc254086_1190369742) keyword defines energy production targets and constraints for groups, including the top most group in the group hierarchy known as the FIELD group. Wells are allocated to groups when the wells are specified by the [WELSPECS](#__RefHeading___Toc268463_1366622701) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group's target calorific value is being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | ENGVAL | A real positive value that defines the surface energy target for the group.<br>The default value of 1 x 1020 switches off the energy target for the group. | 1.0 x 10^20^ |
| BTU/day | kJ/day | J/hour |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.28: GCONENG Keyword Description

See also the [GRUPTREE](#__RefHeading___Toc118321_1596574740) keyword to define the hierarchy of the groups below the FIELD level, the [GCONPROD](#__RefHeading___Toc146746_4203985108) and [GCONINJE](#__RefHeading___Toc134874_2055188184) keywords to define a group's production and injection rate targets and constraints, the [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword to define a production well's targets and constraints, and the [WCONINJE](#__RefHeading___Toc146750_4203985108) keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

#### Example

The following example defines the energy production target for the field.

\--

\-- GROUP ENERGY PRODUCTION CONTROLS

\--

\-- GRUP ENERGY

\-- NAME VALUE

GCONENG

FIELD 1010E9 /

/

Here the energy production target has been set to 1,010 x 109 Btu/day for the field.
