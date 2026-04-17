### RVWVD -- Equilibration Vaporized Water-Gas Ratio (Rvw) versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The RVWVD keyword defines the vaporized water-gas ratio (Rvw) versus depth tables for each equilibration region that should be used when there is vaporized water in the model and the EQLOPT6 variable has been set to a positive integer on the EQUIL keyword in the SOLUTION section.

The keyword should only be used if both gas and water phases haves been activated in the model via the GAS and WATER keywords, and the VAPWAT is also present activating OPM Flow's Vaporized Water Model. All the aforementioned keywords are in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding vaporized oil-gas ratio values, RVW | None |
| feet | m | cm |  |
| 2 | RVW | A columnar vector of real values that defines the vaporized water-gas ratio values, values at the corresponding DEPTH. | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.35: RVWVD Keyword Description

Alternatively, the vaporized water-gas ratio for each cell may be set via the RVW keyword in the SOLUTION section, if the non-standard method to initialize the model via enumeration is being employed.

See also the EQUIL keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the vaporized water-gas ratio versus depth functions.

\--

\-- DEPTH RVW

\-- STB/MSCF

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

RVWVD

3000.0 0.00000

8000.0 0.00000 / RVW VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.00000

8000.0 0.00000 / RVW VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

3000.0 0.00100

8000.0 0.00100 / RVW VS DEPTH EQUIL REGN 03

The example shows three tables for three regions with constant RVW versus depth relationships for each equilibration region, with the first two tables having a zero vaporized water-gas ratio and the last region having a constant 0.001 stb/Mscf versus depth relationship.
