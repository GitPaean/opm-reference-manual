### PBVD -- Equilibration Bubble-Point versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PBVD keyword defines the bubble-point pressure versus depth tables for each equilibration region that should be used when there is dissolved gas in the model (DISGAS has been activated in the RUNSPEC section) and the EQLOPT1 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding bubble-point values, PBVALS. | None |
| feet | m | cm |  |
| 2 | PBVALS | A columnar vector of real values that defines the oil bubble-point values at the corresponding DEPTH. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.20: PBVD Keyword Description

Alternatively, the dissolved gas-oil ratio versus depth tables may be entered using the RSVD keyword in the SOLUTION section instead of this keyword. See also the RSVD and EQUIL keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the bubble-point versus depth functions.

\--

\-- DEPTH PSAT

\-- PRESS

\-- \-\-\-\-\-- \-\-\-\-\--

PBVD

3000.0 3000.0

8000.0 3025.0 / PSAT VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 3100.0

8000.0 3125.0 / PSAT VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\--

3000.0 3200.0

8000.0 3225.0 / PSAT VS DEPTH EQUIL REGN 03

Here three tables are entered and each table is terminated by a "/" and there is no keyword terminating "/".
