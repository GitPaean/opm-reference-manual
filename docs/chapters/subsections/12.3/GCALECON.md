### GCALECON -- Group Economic Criteria for Production Calorific Groups

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GCALECON keyword defines economic criteria for production groups, including the field level group FIELD, that have previously been defined by the GCONPROD keyword in the SCHEDULE section and have had their rate targets and constraints set by calorific value via the GCONVAL keyword in the SCHEDULE section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the GCONPROD and CECON keywords in the SCHEDULE section and the controls specified by the WECON keyword.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | ENEVAL | A real positive value that defines the minimum economic surface energy production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the WELSPECS keyword.<br>A value less than or equal to zero switches of this criteria. | 0.0 |
| BTU/day | kJ/day | J/hour |  |
| 3 | CALVAL | A real positive value that defines the minimum economic surface calorific value, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the WELSPECS keyword.<br>A value less than or equal to zero switches of this criteria, | 0.0 |
| Btu/Mscf | kJ/sm^3^ | J/scc |  |
| 8 | END | A defined character string that defines if the simulation should terminate if all the producing wells in the group, including the FIELD group, are shut or stopped. END should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step. | NO |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.26: GCALECON Keyword Description

See also the WELSPECS keyword to define a wells shut-in or stop options, GCONPROD, GCONCAL, GCONENG for group controls, and WECON for setting a well's economic criteria. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the economic criteria for the field with a minimum economic surface energy production rate of 5 x 109 BTU/day and a minimum economic surface calorific value of900 Btu/Mscf

\--

\-- GROUP ECONOMIC CRITERIA FOR PRODUCTION GROUPS UNDER CALORIFIC CONTROL

\--

\-- GRUP ENERGY CALORIFIC END

\-- NAME RATE VALUE RUN

GCALECON

FIELD 5E9 900.0 \'YES\' /

/

If the economic limits are violated then the run will stop at the next report time step.
