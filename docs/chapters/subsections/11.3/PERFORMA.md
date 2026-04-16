### PERFORMA -- Export Standard Simulator Performance Summary Variables to File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [PERFORMA](#__RefHeading___Toc304796_3851943165) keyword activates the writing out of a standard set of OPM Flow simulation numerical performance summary variables to the [SUMMARY](#__RefHeading___Toc43949_784232322) (\*.SMSPEC and .\*UNSMRY) and RSM (\*.RSM) files. lists the summary variables written out by the keyword.

Note that not all these variables are available in OPM Flow; however, the simulator will issue a warning message if this is indeed the case. It is anticipated that the number of recognized summary variables will increase in future releases of OPM Flow.

| Elapsed - Elapsed time in seconds. | ELAPSED | No data written to file. |
| --- | --- | --- |
| Iterations - Number linear iterations for each time step. | MLINEARS |  |
| Iterations - Cumulative number of linear iterations. | MSUMLINS |  |
| Iterations - Cumulative number of Newton iterations. | MSUMNEWT |  |
| Iterations - Number of Newton iterations used for each time step. | [NEWTON](#__RefHeading___Toc317502_1841740821) |  |
| Iterations - Average number of linear iterations per Newton iteration for each time step. | NLINEARS | For runs with LGRs, LLINEARS will automatically be exported for each [LGR](#__RefHeading___Toc55049_4106839650). |
| Iterations - Maximum number of linear iterations in the Newton iterations per time step. | NLINSMAX |  |
| Iterations - Minimum number of linear iterations in the Newton iterations per time step. | NLINSMIN |  |
| Time Step -- Criteria used to select the length of the time step.<br>See section [[11.2.24](#anchor-2)](#11.2.23.Option Specific Summary Variables – OPM Flow Simulation Performance|outline)[](#11.2.23.Option Specific Summary Variables – OPM Flow Simulation Performance|outline)[[Option Specific Variables -- OPM Flow Simulation Performance](#anchor-2)](#11.2.23.Option Specific Summary Variables – OPM Flow Simulation Performance|outline) for the definition of of the STEPTYPE mnemonics. | STEPTYPE | No data written to file. |
| CPU - Current CPU usage in seconds. | TCPU | Does not consider the time taken by inter-process communications in parallel runs, whereas ELAPSED does. Thus, for parallel jobs, ELAPSED is the most relevant time measurement. |
| CPU - CPU time per day (or hour in lab units depending on run units system). | TCPUDAY | No data written to file. |
| CPU - CPU time per time step in seconds. | TCPUTS | No data written to file. |
| Elapsed - Elapsed time per linear iteration in seconds. | TELAPLIN | No data written to file. |
| Time Step - Length of time step. | TIMESTEP |  |
| Notes:<br>3)  Cells under the Variable column not colored indicate that the summary variable is available in OPM Flow.<br>4)  Cells under the Variable column colored in gray indicate that the summary variable is recognized by the parser but the summary variable is not available.<br>5)  Cells under the Variable column colored in orange indicate that the summary variable is not recognized by the parser and the summary variable is not available. These summary variables may cause the simulator to abort. |  |  |

Table 11.31: Simulator Performance Summary Variables (Numerical Performance)

#### Example

\-- ==============================================================================

\--

\-- SUMMARY SECTION

\--

\-- ==============================================================================

SUMMARY

\--

\-- EXPORT NUMERICAL PERFORMANCE SUMMARY VARIABLES TO FILE

\--

PERFORMA

\--

\-- ACTIVATE COLUMNAR SUMMARY DATA REPORTING OPTION

\--

RUNSUM

\--

\-- ACTIVATE SUMMARY DATA RSM FILE OUTPUT OPTION

\--

SEPARATE

Note the [SEPARATE](#__RefHeading___Toc210158_2884651453) keyword is not required for OPM Flow as this is the default behavior; however, it is probably good practice to include it if the same input decks are being run with commercial simulator.
