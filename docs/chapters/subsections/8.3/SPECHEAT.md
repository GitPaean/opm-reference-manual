### SPECHEAT -- Define the Specific Heat of Oil, Water and Gas

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SPECHEAT defines the specific heat of the oil, water and gas phases for various PVT regions in the model for when the THERMAL option has been activated in the RUNSPEC section. The number of SPECHEAT vector data sets is defined by the NTPVT parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the SPECHEAT data sets to different grid blocks in the model is done via the PVTNUM keyword in the REGIONS section.

This keyword can only be used if OPM Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | A columnar vector of real monotonically increasing down the column values that define the temperature for the corresponding oil, water and gas specific heat values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | OILSHEAT | OILSHEAT is a columnar vector of positive real numbers defining the specific heat of oil at the corresponding temperature, TEMP. | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 3 | WATSHEAT | WATSHEAT is a columnar vector of positive real numbers defining the specific heat of water at the corresponding temperature, TEMP. | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| 4 | GASSHEAT | GASHEAT is a columnar vector of positive real numbers defining the specific heat of gas at the corresponding temperature, TEMP. | None |
| Btu/lb/oR | kJ/kg/K | J/gm/K |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.170: SPECHEAT Keyword Description

See also the SPECROCK keyword to define the reservoir rock specific heat.

#### Example

The example below defines three fluid phases specific heat versus temperature tables assuming NTPVT equals three and NPPVT is greater than or equal to two on the TABDIMS keyword in the RUNSPEC section.

\--

\-- SPECIFIC HEAT OF OIL, WATER AND GAS TABLE

\--

SPECHEAT

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5000 1.5000 0.5000

250.000 0.5000 1.5000 0.5000 / TABLE NO. 01

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5500 1.5000 0.5000

260.000 0.5500 1.5000 0.5000 / TABLE NO. 02

\-- TEMP SPECHEAT SPECHEAT SPECHEAT

\-- OIL WATER GAS

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 0.5500 1.5500 0.5000

270.000 0.6000 1.5500 0.5000 / TABLE NO. 03

There is no terminating "/" for this keyword.
