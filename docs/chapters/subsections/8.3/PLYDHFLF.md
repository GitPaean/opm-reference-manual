### PLYDHFLF -- Define Polymer Thermal Degradation Half-Life Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PLYDHFLF keyword defines the polymer thermal degradation half-life with respect to temperature functions for when the polymer option has been activated by the POLYMER keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | TEMP | A columnar vector of real monotonically increasing down the column values that defines the polymer thermal degradation temperature. | None |
| ^o^F | ^o^C | ^o^C |  |
| 2 | POLHFLF | A columnar vector of real values that defines the corresponding polymer half-life. | None |
| days | days | hours |  |
| Notes:<br>1)  The keyword is followed by NTPVT tables as declared on the TABDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NPPVT rows as declared on the TABDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 8.102: PLYDHFLF Keyword Description

#### Example

\--

\-- POLYMER THERMAL DEGRADATION HALF-LIFE TABLE

\--

PLYDHFLF

\-- POLYMER POLYMER

\-- TEMP HALF-LIFE

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\-\--

0.0 365.000

40.0 200.000

80.0 150.000

120.0 100.000 / TABLE NO. 01

\-- POLYMER POLYMER

\-- TEMP HALF-LIFE

\-- \-\-\-\-\-\-- \-\-\-\-\-\-\--

0.0 365.000

50.0 175.000

75.0 140.000

100.0 120.000

125.0 90.000

150.0 85.000 / TABLE NO. 02

The example defines two polymer thermal degradation half-life tables, based on the NTPVT variable on the TABDIMS keyword in the RUNSPEC section being equal to two and NPPVT variable on the same keyword being greater than or equal to six.
