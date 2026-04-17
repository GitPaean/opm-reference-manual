### RPTONLYO -- Deactivate the Report Time Steps Only Option for the SUMMARY File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword deactivates the writing out of the SUMMARY file and the RSM file data, if the RSM file option has been requested by the RUNSUM keyword in the SUMMARY section, at report time steps only, and switches on writing out all the time steps to the files. This option is the default behavior for when RPTONLY has not been activated.

There is no data required for this keyword and there is no terminating "/" for this keyword.

The option can be deactivated by the RPTONLY keyword in the SUMMARY section that will switch on writing the data at every report time step instead of every time step.

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

The above example deactivates the writing out of the SUMMARY file at report time steps only, and switches on writing out all the time steps to the file.
