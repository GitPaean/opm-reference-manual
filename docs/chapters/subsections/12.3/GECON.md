### GECON -- Group Economic Criteria for Production Groups

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GECON keyword defines economic criteria for production groups, including the top level FIELD group, that have been created by having wells assigned to them via the WELSPECS keyword in the SCHEDULE section.

Note that wells are allocated to a group when they are specified by the WELSPECS keyword and wells can also have well level economic controls. Wells under group control are therefore subject to the economic criteria set via the GECON and WECON keywords and the controls specified by the GCONPROD keyword in the SCHEDULE section.

| 1 | GRPNAME | A character string of up to eight characters in length that defines the group name for which the group target and constraints are being defined. The group named FIELD is the top most group and should be used to set targets and constraints for the field.<br>Note that the group hierarchy should be defined by the GRUPTREE keyword when there is more than one level of groups, otherwise all the groups will sit directly under the FIELD group in the group tree hierarchy. | None |
| --- | --- | --- | --- |
| 2 | ORAT | A real positive value that defines the minimum economic surface oil production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by the AUTO variable item (9) of the WELSPECS keyword.<br>This value may be specified using a User Defined Argument (UDA).<br>A value less than or equal to zero switches off this criteria. | 0.0 |
| stb/d | sm^3^/day | scc/hour |  |
| 3 | GRAT | A real positive value that defines the minimum economic surface gas production rate, below which an economic action of shutting in or stopping all the wells in the group, as requested by the AUTO variable item (9) of the WELSPECS keyword.<br>This value may be specified using a User Defined Argument (UDA).<br>A value less than or equal to zero switches off this criteria, | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 4 | WCUT | A real positive value that defines the maximum economic surface water cut, above which an economic action will take place.<br>This value may be specified using a User Defined Argument (UDA).<br>Water cut is defined as:, and the various actions that are available if the water cut limit is exceeded are described in item (7).<br>A value less than or equal to zero switches off this criteria. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | GOR | A real positive value that defines the maximum economic surface gas-oil ratio, above which an economic action will take place, as defined by item (7).<br>This value may be specified using a User Defined Argument (UDA).<br>A value less than or equal to zero switches off this criteria. | 0.0 |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |
| 6 | WGR | A real positive value that defines the maximum economic surface water-gas ratio, above which an economic action will take place, as defined by item (7).<br>This value may be specified using a User Defined Argument (UDA).<br>A value less than or equal to zero switches off this criteria. | 0.0 |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| 7 | ACTION | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. ACTION should be set to one of the following character strings:<br>1)  NONE: no action is taken.<br>2)  CON: close the worst offending connection in the worst offending well. If connections have been grouped as completions then the worst offending completion will be closed.<br>3)  +CON: close the worst offending connection and all below it in the worst offending well. If connections have been grouped as completions then the worst offending completion and all below it will be closed.<br>4)  WELL: shut or stop the worst offending well as per the AUTO variable on the WELSPECS keyword.<br>5)  PLUG: plug back the worst offending well based on the plug back length and options defined on the WPLUG keyword in the SCHEDULE.<br>The corrective action takes places at the end of the time step in which the constraint is violated.<br>Only the NONE option is currently supported by the simulator. | None |
| 8 | END | A defined character string that defines if the simulation should terminate if all the producing wells in the group, including the FIELD group, are shut or stopped. END should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step.<br>Only the NO option is currently supported by the simulator. | NO |
| 9 | MXWELS | A positive integer defining the maximum number of producing and injecting wells for this this group and any subordinate groups.<br>The default value of zero implies that there is no limit to the number of wells.<br>This is not currently supported by the simulator and must be defaulted. | 0 |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.3.98.1: GECON Keyword Description

See also the WELSPECS keyword to define a well's shut-in or stop options, GCONPROD for group controls, and WECON for setting a well's economic criteria. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines the economic criteria for the field with a minimum oil rate of 2,000 m^3^/day and a maximum water cut of 95%.

\--

\-- GROUP ECONOMIC CRITERIA FOR PRODUCTION GROUPS

\--

\-- GRUP OIL GAS WCT GOR WGR WORK END MAX

\-- NAME MIN MIN MAX MAX MAX OVER RUN WELLS

GECON

FIELD 2E3 1\* 0.95 1\* 1\* CON \'YES\' 1\* /

/

If the economic limits are violated then the run will stop at the next report time step.
