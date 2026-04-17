### RSVD -- Equilibration Dissolved Gas-Oil Ratio (Rs) versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RSVD keyword defines the dissolved gas-oil ratio (Rs) versus depth tables for each equilibration region that should be used when there is dissolved gas in the model (DISGAS has been activated in the RUNSPEC section) and the EQLOPT1 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding dissolve gas-oil ratio values, RS. | None |
| feet | m | cm |  |
| 2 | RS | A columnar vector of real values that defines the dissolved gas-oil ratio values at the corresponding DEPTH. | None |
| Mscf/stb | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.30: RSVD Keyword Description

Alternatively, the oil bubble-point pressure versus depth tables may be entered using the PBVD keyword in the SOLUTION section instead of this keyword.

See also the PBVD and EQUIL keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the bubble-point versus depth functions.

\--

\-- DEPTH RS

\-- MSCF/STB

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RSVD

3000.0 1.400

8000.0 1.400 / RS VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.400

8000.0 1.400 / RS VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 1.400

8000.0 1.400 / RS VS DEPTH EQUIL REGN 03

Here three tables are entered with a constant GOR versus depth relationship.
