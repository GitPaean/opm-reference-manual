### GCVD -- Define Equilibration Coal Gas Concentration versus Depth Tables

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The GCVD keyword defines the initial coal gas concentration versus depth tables for each equilibration region for when the coal phase has been activated in the run via the COAL keyword in the RUNSPEC section. The keyword may be used in conjunction with the GASCONC keyword in the SOLUTION section, to fully describe the initial state of the model. Note both GASCONC and GCVD are optional as the simulator will calculate the coal gas concentration based on the equilibrium concentration and the block pressure.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | DEPTH | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding coal gas concentration, GCVALS. | None |
| feet | m | cm |  |
| 2 | GCVALS | A columnar vector of real values that defines the coal gas concentration values at the corresponding DEPTH. | None |
| Mscf/ft3 | sm^3^/m^3^ | scc/cc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the EQLDIMS keyword in the RUNSPEC section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the EQLDIMS keyword in the RUNSPEC section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.17: GCVD Keyword Description

See also the GASCONC and GASSATC keywords in the SOLUTION section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the EQLDIMS keyword in the RUNSPEC section, then the following example defines the coal gas concentration versus depth functions.

\--

\-- DEPTH GC

\-- MSCF/FT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

GCVD

100.0 75.5000

1000.0 75.5000 / GC VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

100.0 65.5000

1000.0 65.5000 / GC VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

100.0 60.0000

1000.0 60.0000 / GC VS DEPTH EQUIL REGN 03

Here three tables are entered with a constant coal gas concentration versus depth relationship for each equilibration region.
