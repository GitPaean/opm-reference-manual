### RPTONLYO -- Deactivate the Report Time Steps Only Option for the SUMMARY File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword deactivates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file and the RSM file data, if the RSM file option has been requested by the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section, at report time steps only, and switches on writing out all the time steps to the files. This option is the default behavior for when [RPTONLY](#__RefHeading___Toc210150_2884651453) has not been activated.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The option can be deactivated by the [RPTONLY](#__RefHeading___Toc210150_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section that will switch on writing the data at every report time step instead of every time step.

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

\-- DEACTIVATE REPORT TIME STEPS ONLY SUMMARY FILE OPTION

\--

RPTONLYO

The above example deactivates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file at report time steps only, and switches on writing out all the time steps to the file.
