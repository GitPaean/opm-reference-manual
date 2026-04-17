### WECON -- Well Economic Criteria for Production Wells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The WECON keyword defines the economic criteria for production wells that have previously been defined by the WELSPECS and WCONPROD keywords in the SCHEDULE section.

Note that wells can be allocated to a group when they are specified by the WELSPECS keyword and groups can also have economic controls. Wells under group control are therefore subject to the economic criteria set via the GCONPROD and GECON keywords in the SCHEDULE section and the economic criteria specified by the WECON keyword.

| 1 | WELNAME | A character string of up to eight characters in length that defines the well name for which the well economic criteria data is being defined.<br>Note that the well name (WELNAME) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| --- | --- | --- | --- |
| 2 | ORAT | A real positive value that defines the minimum economic surface oil production rate, below which an economic action will take place, as outlined below:<br>1)  If there are any remaining connections in the well with the STATUS variable set to AUTO on the COMPDAT keyword in the SCHEDULE section, then one of these connections (or completion) will be opened.<br>2)  If there are no remaining connections in the well with the STATUS variable set to AUTO on the COMPDAT keyword, then the well will be shut or stopped as requested by item (9) of the WELSPECS keyword.<br>Only option (2) is supported by OPM Flow as STATUS equals AUTO on the COMPDAT keyword is currently not supported by the simulator. Hence, the well be either shut or stopped.<br>A value less than or equal to zero switches off this criterion.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/d | sm^3^/day | scc/hour |  |
| 3 | GRAT | A real positive value that defines the minimum economic surface gas production rate, below which an economic action will take place, as outlined below:<br>1)  If there are any remaining connections in the well with the STATUS variable set to AUTO on the COMPDAT keyword in the SCHEDULE section, then one of these connections (or completion) will be opened.<br>2)  If there are no remaining connections in the well with the STATUS variable set to AUTO on the COMPDAT keyword, then the well will be shut or stopped as requested by item (9) of the WELSPECS keyword.<br>Only option (2) is supported by OPM Flow as STATUS equals AUTO on the COMPDAT keyword is currently not supported by the simulator. Hence, the well be either shut or stopped.<br>A value less than or equal to zero switches off this criterion.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| Mscf/d | sm^3^/day | scc/hour |  |
| 4 | WCUT | A real positive value that defines the maximum economic surface water cut, above which an economic action will take place.<br>This value may be specified using a User Defined Argument (UDA).<br>Water cut is defined as:, and the various actions that are available if the water cut limit is exceeded are described in item (7).<br>A value less than or equal to zero switches off this criterion. | 0.0 |
| dimensionless | dimensionless | dimensionless |  |
| 5 | GOR | A real positive value that defines the maximum economic surface gas-oil ratio, above which an economic action will take place, as defined by item (7).<br>A value less than or equal to zero switches off this criterion.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |
| 6 | WGR | A real positive value that defines the maximum economic surface water-gas ratio, above which an economic action will take place, as defined by item (7).<br>A value less than or equal to zero switches off this criterion.<br>This value may be specified using a User Defined Argument (UDA). | 0.0 |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| 7 | ACTION | A defined character string that defines the action to be taken if the economic WCUT, GOR, or WGR limits are violated. ACTION should be set to one of the following character strings:<br>1)  NONE: no action is taken.<br>2)  CON: close the worst offending connection. If connections have been grouped as completions then the worst offending completion will be closed.<br>3)  +CON: close the worst offending connection and all below it. If connections have been grouped as completions then the worst offending completion and all below it will be closed.<br>4)  WELL: shut or stop the well as per the AUTO variable on the WELSPECS keyword.<br>The corrective action takes places at the end of the time step in which the constraint is violated.<br>The +CON option is not currently supported by OPM Flow. | NONE |
| 8 | END | A defined character string that defines if the simulation should terminate if the well is shut or stopped. END should be set to one of the following character strings:<br>1)  NO: no action is taken and the run continues.<br>2)  YES: terminate the run at the next report time step.<br>The YES option is not currently supported by OPM Flow. | NO |
| 9 | WELOPEN | A character string of up to eight characters in length that defines the name of the well, which will be opened when the current well (WELNAME) has been automatically closed/shut by the simulator. Wells closed manually do not invoke this opton.<br>The well name (WELOPEN) must have been declared previously using the WELSPECS keyword in the SCHEDULE section, otherwise an error may occur. | None |
| 10 | ELTOPT | A defined character string that defines the type of quantity used to test the economic limit, and should be set to one of the following character strings:<br>1)  POTN: The Economic Limit Test ("ELT") is based on a well's potential rate. A well's potential rate is calculated using only the flowing bottom-hole pressure and tubing head pressure constraints, all other constraints are ignored, including group constraints. However, if the WELDRAW keyword in the SCHEDULE section has been used to limit a well's pressure draw down, then this will also be considered in the potential calculation, as it influences the bottom-hole pressure constraint.<br>2)  RATE: The economic limit is based a well's surface production rate as oppose to the potential rate, this is the default behavior.<br>Wells under group control via the GCONPROD keyword in the SCHEDULE section will be subject to the ELT, except for when the group's production target rate is set to zero.<br>Wells under group control via the GCONPRI keyword in the SCHEDULE section will be subject to the ELT, except for when the group has curtailed a well's production. | RATE |
| 11 | WCUT2 | A real positive value that defines the secondary maximum economic surface water cut, above which an economic action will take place.<br>A value less than or equal to zero switches off this criterion.<br>This item is not supported by OPM Flow and should be defaulted (1\*) or set to zero. | 0.0 |
| 12 | ACTION2 | A defined character string that defines the action to be taken if the secondary economic WCUT2 limits is violated.<br>This item is not supported by OPM Flow and should be defaulted (1\*). | 1\* |
| 13 | GLR | A real positive value that defines the maximum economic surface gas-liquid ratio, above which an economic action will take place, as defined by item (7).<br>A value less than or equal to zero switches off this criterion.<br>This item is not supported by OPM Flow and should be defaulted (1\*). | None |
| 14 | LRAT | A real positive value that defines the minimum liquid rate, below which the well (WELNAME) is shut-in.<br>This item is not supported by OPM Flow and should be defaulted (1\*). | 0.0 |
| 15 | TEMP | A real positive value that defines the maximum economic temperature in the commercial compositional Thermal/Temperature model for a well.<br>This item is not supported by OPM Flow and should be defaulted (1\*). | None |
| 16 | RESV | A real positive value that defines the minimum reservoir volume rate, below which the well (WELNAME) is shut-in.<br>This item is not supported by OPM Flow and should be defaulted (1\*). | 0.0 |
| Notes:<br>1)  User Defined Quantities (\"UDQ\") can be used as User Defined Arguments (\"UDA\") for various group, well, and connection keywords in the SCHEDULE section. User Defined Arguments are activated using the UDADIMS keyword in the RUNSPEC section, and defined by the UDQ keyword in the SCHEDULE section.<br>2)  The keyword is followed by any number of records with each record terminated by a "/" and the keyword should be terminated by a "/". |  |  |  |

Table 12.81: WECON Keyword Description

See also the WELSPECS keyword to define a wells shut-in or stop options, GCONPROD for group controls, and GECON for setting a group's economic criteria. All the aforementioned keywords are described in the SCHEDULE section.

#### Example

The following example defines one oil well and one gas well using the WELSPECS keyword, together with their economic criteria.

\--

\-- WELL SPECIFICATION DATA

\--

\-- WELL GROUP LOCATION BHP PHASE DRAIN INFLOW SHUT CROSS PRESS

\-- NAME NAME I J DEPTH FLUID AREA EQUA. IN FLOW TABLE

WELSPECS

GP01 PLATFORM 14 13 1\* GAS 1\* GPP SHUT NO 1\* /

OP01 PLATFORM 28 96 1\* OIL 1\* STD SHUT NO 1\* /

/

\--

\-- WELL ECONOMIC CRITERIA FOR PRODUCTION WELLS

\-- WELL MIN MIN MAX MAX MAX CNTL END

\-- NAME ORAT GRAT WCUT GOR WGR MODE RUN

WECON

GP01 1\* 5.0E3 1\* 1\* 1\* \'WELL\' \'NO\' /

OP01 500 1\* 0.95 15 1\* \'WELL\' \'YES\' /

/

Well GP01 has a minimum economic gas rate of 5 MMscf/d and will shut-in if the gas rate falls below this rate, but the simulation will continue even if this occurs. Well OP01 has a minimum economic oil rate of 500 stb/d, a maximum water cut limit of 95%, and a maximum GOR of 15 Mscf/stb, if any any of these limits are violated the well will be shut-in and the run should be terminated at the next reporting time step, however the option to end the run is not currently supported by OPM Flow.
