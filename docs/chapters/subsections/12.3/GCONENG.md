### GCONENG -- Group Production Energy Targets

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GCONCAL keyword defines energy production targets and constraints for groups, including the top most group in the group hierarchy known as the FIELD group. Wells are allocated to groups when the wells are specified by the WELSPECS keyword in the SCHEDULE section. Wells defined to be under group control will have their production rates controlled by the group to which they belong, in addition to any well constraints defined for the wells.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group's target calorific value is being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | ENGVAL | A real positive value that defines the surface energy target for the group.<br>The default value of 1 x 1020 switches off the energy target for the group. | 1.0 x 10^20^ |
| BTU/day | kJ/day | J/hour |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.28: GCONENG Keyword Description

See also the GRUPTREE keyword to define the hierarchy of the groups below the FIELD level, the GCONPROD and GCONINJE keywords to define a group's production and injection rate targets and constraints, the WCONPROD keyword to define a production well's targets and constraints, and the WCONINJE keyword to define an injection well's targets and constraints. All the aforementioned keywords are described in the SCHEDULE section.

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
