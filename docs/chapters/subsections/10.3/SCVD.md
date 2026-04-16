### SCVD -- Define Equilibration Coal Solvent Concentration versus Depth Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SCVD](#__RefHeading___Toc650470_516898843) keyword defines the initial coal solvent concentration versus depth tables for each equilibration region for when the coal phase has been activated in the run via the [COAL](#__RefHeading___Toc234580_3519154785) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword may be used in conjunction with the [SOLVCONC](#__RefHeading___Toc771984_4250154414) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, to fully describe the initial state of the model. Note both [SOLVCONC](#__RefHeading___Toc771984_4250154414) and [SCVD](#__RefHeading___Toc650470_516898843) are optional as the simulator will calculate the coal gas concentration based on the equilibrium concentration and the block pressure.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#__RefHeading___Toc58139_3701168388) | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding coal solvent concentration, SCVALS. | None |
| feet | m | cm |  |
| 2 | SCVALS | A columnar vector of real values that defines the coal solvent concentration values at the corresponding [DEPTH](#__RefHeading___Toc58139_3701168388). | None |
| Mscf/ft3 | sm^3^/m^3^ | scc/cc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.43: SCVD Keyword Description

See also the [SOLVCONC](#__RefHeading___Toc771984_4250154414), [GCVD](#__RefHeading___Toc224457_156692946), [GASCONC](#__RefHeading___Toc189444_2330925267) and [GASSATC](#__RefHeading___Toc216737_1190369742) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the following example defines the coal solvent concentration versus depth functions.

\--

\-- DEPTH SOLVC

\-- MSCF/FT

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

SCVD

100.0 75.5000

1000.0 75.5000 / SC VS DEPTH EQUIL REGN 01

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

100.0 65.5000

1000.0 65.5000 / SC VS DEPTH EQUIL REGN 02

\-- \-\-\-\-\-- \-\-\-\-\-\-\--

100.0 60.0000

1000.0 60.0000 / SC VS DEPTH EQUIL REGN 03

Here three tables are entered with a constant coal solvent concentration versus depth relationship for each equilibration region
