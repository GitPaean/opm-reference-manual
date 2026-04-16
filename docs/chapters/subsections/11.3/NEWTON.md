### NEWTON -- Activate Newton Iteration SUMMARY Output

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the Newton iteration vector (the number of non-linear iterations per time step) to the [SUMMARY](#__RefHeading___Toc43949_784232322) file, and the RSM file if the RSM file option has been requested by the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section,

There is no data required for this keyword and there is no terminating "/" for this keyword.

Although the keyword is recognized by OPM Flow only zeros are written to the [SUMMARY](#__RefHeading___Toc43949_784232322) file.

#### Example

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE \--

\-- ACTIVATE NEWTON ITERATION SUMMARY OUTPUT

\--

NEWTON

The above example actives the writing out of the Newton iteration vector to the [SUMMARY](#__RefHeading___Toc43949_784232322) file.
