### RVWVD -- Equilibration Vaporized Water-Gas Ratio (Rvw) versus Depth Tables

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [RVWVD](#__RefHeading___Toc137367_13175472131) keyword defines the vaporized water-gas ratio (Rvw) versus depth tables for each equilibration region that should be used when there is vaporized water in the model and the EQLOPT6 variable has been set to a positive integer on the [EQUIL](#__RefHeading___Toc135617_1317547213) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

The keyword should only be used if both gas and water phases haves been activated in the model via the [GAS](#__RefHeading___Toc38607_2267116897) and [WATER](#__RefHeading___Toc38611_2267116897) keywords, and the [VAPWAT](#__RefHeading___Toc317543_3149455253) is also present activating OPM Flow's Vaporized Water Model. All the aforementioned keywords are in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | [DEPTH](#__RefHeading___Toc58139_3701168388) | A columnar vector of real monotonically increasing down the column values that defines the depth values for the corresponding vaporized oil-gas ratio values, [RVW](#__RefHeading___Toc537756_4287353749) | None |
| feet | m | cm |  |
| 2 | [RVW](#__RefHeading___Toc537756_4287353749) | A columnar vector of real values that defines the vaporized water-gas ratio values, values at the corresponding [DEPTH](#__RefHeading___Toc58139_3701168388). | None |
| stb/Mscf | sm^3^/sm^3^ | scc/scc |  |
| Notes:<br>1)  The keyword is followed by NTEQUL records as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>2)  Each table must contain a minimum of two rows and a maximum of NDRXVD rows as declared on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.<br>3)  Each table is terminated by a "/" and there is no "/" terminator for the keyword. |  |  |  |

Table 10.35: RVWVD Keyword Description

Alternatively, the vaporized water-gas ratio for each cell may be set via the [RVW](#__RefHeading___Toc537756_4287353749) keyword in the [SOLUTION](#__RefHeading___Toc43947_784232322) section, if the non-standard method to initialize the model via enumeration is being employed.

See also the [EQUIL](#__RefHeading___Toc135617_1317547213) keywords in the [SOLUTION](#__RefHeading___Toc43947_784232322) section.

#### Example

Given NTEQUL equals three and NDRXVD is greater than or equal to two on the [EQLDIMS](#__RefHeading___Toc60335_327352552) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, then the following example defines the vaporized water-gas ratio versus depth functions.

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

The example shows three tables for three regions with constant [RVW](#__RefHeading___Toc537756_4287353749) versus depth relationships for each equilibration region, with the first two tables having a zero vaporized water-gas ratio and the last region having a constant 0.001 stb/Mscf versus depth relationship.
