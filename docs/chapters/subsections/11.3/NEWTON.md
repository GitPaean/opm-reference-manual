### NEWTON -- Activate Newton Iteration SUMMARY Output

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the Newton iteration vector (the number of non-linear iterations per time step) to the SUMMARY file, and the RSM file if the RSM file option has been requested by the RUNSUM keyword in the SUMMARY section,

There is no data required for this keyword and there is no terminating "/" for this keyword.

Although the keyword is recognized by OPM Flow only zeros are written to the SUMMARY file.

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

The above example actives the writing out of the Newton iteration vector to the SUMMARY file.
