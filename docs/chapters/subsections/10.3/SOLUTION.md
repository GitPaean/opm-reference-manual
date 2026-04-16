### SOLUTION -- Define the Start of the SOLUTION Section of Keywords

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [SOLUTION](#__RefHeading___Toc43947_784232322) activation keyword marks the end of the [REGIONS](#__RefHeading___Toc40648_784232322) section and the start of the [SOLUTION](#__RefHeading___Toc43947_784232322) section that defines the parameters used to initialize the model, by:

1)  defining fluid contacts and pressures, or

2)  defining pressures and fluid saturations for all cells in the model, or

3)  by restarting from a previously OPM Flow completed run.

There is no data required for this keyword.

#### Example

\-- ==============================================================================

\--

\-- SOLUTION SECTION

\--

\-- ==============================================================================

SOLUTION

The above example marks the end of the [REGIONS](#__RefHeading___Toc40648_784232322) section and the start of the [SOLUTION](#__RefHeading___Toc43947_784232322) section in the OPM Flow data input file.
