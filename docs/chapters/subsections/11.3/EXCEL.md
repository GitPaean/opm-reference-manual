### EXCEL -- Activate the EXCEL Option for the SUMMARY File

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the RSM file data in a format that can easily be loaded into Microsoft\'s EXCEL spreadsheet program or LibreOffice's CALC spreadsheet program. The RSM file output is activated by the RUNSUM keyword in the SUMMARY section.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Examples

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

\-- ACTIVATE EXCEL SUMMARY FILE OPTION

\--

EXCEL

The above example activates the SUMMARY file EXCEL option for directly loading the RSM file into either Microsoft\'s EXCEL or LibreOffice's CALC spreadsheet programs.
