### OILVISCT -- Define Oil Viscosity versus Temperature Functions

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

OILVISCT defines the oil viscosity as a function of temperature for when OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. The reference pressure and solution gas-oil ratio of the oil for this table is given by the VISCREF keyword in the PROPS section. Note this is an OPM Flow keyword used with OPM Flow's black-oil thermal model that is not available in the commercial simulator's black-oil thermal formulation.

This keyword can only be used if OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | A columnar vector of real monotonically increasing down the column values that defines the temperature values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | VIS | A columnar vector of real increasing down the column values that defines the oil viscosity for the corresponding temperature values (TEMP).<br>VIS should be given at the reference pressure and solution gas-oil ratio as defined by PRESS and RS variables on the VISCREF keyword. | None |
| cP | cP | cP |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.93: OILVISCT Keyword Description

There is no terminating "/" for this keyword.

#### Example

The following example shows the OILVISCT keyword for when the thermal option has been activated by the THERMAL keyword in the RUNSPEC section and for when NTPVT on the TABDIMS keyword in the RUNSPEC section is set equal to one.

\--

\-- OIL VISCOSITY VERSUS TEMPERATURE TABLES (OPM FLOW EXTENSION KEYWORD)

\--

\-- OIL OIL

\-- TEMP VISC

\-- \-\-\-\-\-\-\-- \-\-\-\-\-\--

OILVISCT

100.0 0.600

110.0 0.650

120.0 0.680

150.0 0.720

165.0 0.725 / TABLE NO. 01
