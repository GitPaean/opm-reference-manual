### SPECROCK -- Define the Specific Heat of the Reservoir Rock

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SPECROCK defines the specific heat of the reservoir rock for various PVT regions in the model for when the THERMAL option has been activated in the RUNSPEC section. The number of SPECROCK vector data sets is defined by the NTSFUN parameter on the TABDIMS keyword in the RUNSPEC section and the allocation of the SPECROCK data sets to different grid blocks in the model is done via the SATNUM keyword in the REGIONS section.

This keyword can only be used if OPM's Flow's thermal option has been activated by the THERMAL keyword in the RUNSPEC section. Note this is different to the commercial simulator that uses the TEMP keyword in the RUNSPEC section to activate the black-oil thermal model.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | A columnar vector of real monotonically increasing down the column values that define the temperature for the corresponding rock specific heat values. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | ROCKHEAT | ROCKHEAT is a columnar vector of positive real numbers defining the specific heat of the rock at the corresponding temperature, TEMP. | None |
| Btu/ft3/oR | kJ/m3/K | J/cc/K |  |
| Notes:<br>1)  The keyword is followed by NTSFUN tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NSSFUN rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.171: SPECROCK Keyword Description

See also the SPECHEAT keyword to define the specific heat relationships for the oil, water and gas phases.

#### Example

The example below defines three rock specific heat versus temperature tables assuming NTSFUN equals three and NSSFUN is greater than or equal to two on the TABDIMS keyword in the RUNSPEC section.

\--

\-- SPECIFIC HEAT OF ROCK

\--

SPECROCK

\-- TEMP SPECHEAT

\-- ROCK

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 20.000

250.000 20.000 / TABLE NO. 01

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 21.000

260.000 21.000 / TABLE NO. 02

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.000 23.000

270.000 23.000 / TABLE NO. 03

There is no terminating "/" for this keyword.
