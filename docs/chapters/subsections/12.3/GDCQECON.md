### GDCQECON -- Group Economic Criteria for DCQ Production Groups

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GDCQECON keyword defines economic criteria for DCQ production groups, including the field level group FIELD, that have previously been defined by the GCONPROD keywords in the SCHEDULE section. Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the GCONPROD and CECON keywords in the SCHEDULE section and the controls specified by the WECON keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | DCQ | A real positive value that defines the minimum economic DCQ gas production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by item (9) of the WELSPECS keyword. Note if GRPNAME is equal to FIELD then the run will be terminated.<br>A value less than or equal to zero switches of this criteria. | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| Notes:<br>1)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.35: GDCQECON Keyword Description

See also the WELSPECS keyword to define a wells shut-in or stop options, GCONPROD for group controls, and WECON for setting a well's economic criteria. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the minimum DCQ for the field to be 10 MMscf/d.

\--

\-- GROUP ECONOMIC CRITERIA FOR DCQ PRODUCTION GROUPS

\--

\-- GRUP GAS

\-- NAME DCQ

GDCQECON

FIELD 10E3 /

/
