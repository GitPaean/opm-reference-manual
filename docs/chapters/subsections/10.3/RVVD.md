### RVVD -- Equilibration Vaporized Oil-Gas Ratio (Rv) versus Depth Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RVVD](#__RefHeading___Toc137367_1317547213) keyword defines the vaporized oil-gas ratio (Rv) versus depth tables for each equilibration region that should be used when there is vaporized oil in the model ([VAPOIL](#__RefHeading___Toc56610_2267116897) has been activated in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section) and the EQLOPT2 variable has been set to a positive integer on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#__RefHeading___Toc58139_3701168388) | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding vaporized oil-gas ratio values, [RV](#__RefHeading___Toc137365_1317547213). | None |
| feet | m | cm |  |
| 2 | [RV](#__RefHeading___Toc137365_1317547213) | A columnar vector of real values that defines the vaporized oil-gas ratio values at the corresponding [DEPTH](#__RefHeading___Toc58139_3701168388). | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.33: RVVD Keyword Description

Alternatively, the gas dew-point pressure versus depth tables may be entered using the [PDVD](#__RefHeading___Toc135625_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section instead of this keyword.

See also the [PDVD](#__RefHeading___Toc135625_1317547213) and [EQUIL](#__RefHeading___Toc135617_1317547213) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the following example defines the dew-point versus depth functions.

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
