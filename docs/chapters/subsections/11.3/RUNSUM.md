### RUNSUM -- Activate RSM File Output of the SUMMARY Data

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the SUMMARY file data in a columnar format to the PRT file. Normally the SEPARATE keyword in the SUMMARY section is invoked in the same run to direct the data stream to a separate RSM file for easy loading into other programs, for example, Microsoft\'s EXCEL or LibreOffice's CALC spreadsheet programs.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See also the EXCEL, RPTONLY and SEPARATE keywords in the SUMMARY section.

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

SEPARATE

Note unlike the commercial simulator, OPM Flow always writes out the data to a separate file.
