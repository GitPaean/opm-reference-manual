### RVVD -- Equilibration Vaporized Oil-Gas Ratio (Rv) versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RVVD keyword defines the vaporized oil-gas ratio (Rv) versus depth tables for each equilibration region that should be used when there is vaporized oil in the model (VAPOIL has been activated in the RUNSPEC section) and the EQLOPT2 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding vaporized oil-gas ratio values, RV. | None |
| feet | m | cm |  |
| 2 | RV | A columnar vector of real values that defines the vaporized oil-gas ratio values at the corresponding DEPTH. | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.33: RVVD Keyword Description

Alternatively, the gas dew-point pressure versus depth tables may be entered using the PDVD keyword in the SOLUTION section instead of this keyword.

See also the PDVD and EQUIL keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the dew-point versus depth functions.

\--

\-- DEPTH RV

\-- STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RVVD

3000.0 0.00725

8000.0 0.00725 / RV VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.00730

8000.0 0.00730 / RV VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.00750

8000.0 0.00750 / RV VS DEPTH EQUIL REGN 03

Here three tables are entered with a constant CGR versus depth relationship for each equilibration region.
