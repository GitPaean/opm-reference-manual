### PDVD -- Define Equilibration Dew-Point versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PDVD keyword defines the dew-point pressure versus depth tables for each equilibration region that should be used when there is vaporized oil in the model (VAPOIL has been activated in the RUNSPEC section) and the EQLOPT2 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding dew-point values, PDVALS. | None |
| feet | m | cm |  |
| 2 | PDVALS | A columnar vector of real values that defines the gas dew-point values at the corresponding DEPTH. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.22: PDVD Keyword Description

Alternatively, the vaporized oil-gas ratio (condensate-gas ratio) versus depth tables may be entered using the RVVD keyword in the SOLUTION section instead of this keyword.

See also the RVVD and EQUIL keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the bubble-point versus depth functions.

\--

\-- DEPTH PSAT

\-- PRESS

\-- \-\-\-\-\-- \-\-\-\-\--

PDVD

3000.0 2000.0

8000.0 2025.0 / PSAT VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 2100.0

8000.0 2125.0 / PSAT VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 2200.0

8000.0 2225.0 / PSAT VS DEPTH EQUIL REGN 03

Here three tables are entered and each table is terminated by a "/" and there is no keyword terminating "/".
