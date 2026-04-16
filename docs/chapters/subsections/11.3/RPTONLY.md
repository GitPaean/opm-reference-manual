### RPTONLY -- Activate the Report Time Steps Only Option for the SUMMARY File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file and the RSM file data, if the RSM file option has been requested by the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section, at report time steps only. The default is for the data to be written out for all time steps to the [SUMMARY](#__RefHeading___Toc43949_784232322) files. This keyword reduces the file size at the expense of lower resolution in the time domain.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The option can be deactivated by the [RPTONLYO](#__RefHeading___Toc210152_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.

#### Example

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT STANDARD SUMMARY VARIABLE VECTORS TO FILE

\--

ALL

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE

\--

\-- ACTIVATE REPORT TIME STEPS ONLY SUMMARY FILE OPTION

\--

RPTONLY

The above example activates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file at report time steps only.
