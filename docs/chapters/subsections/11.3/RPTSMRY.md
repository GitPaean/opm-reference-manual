### RPTSMRY -- Activate or Deactivate Summary List Report

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates or deactivates a listing of all the summary variables that are going to be written to the SUMMARY file and the RSM file, if the RSM file option has been requested by the RUNSUM keyword in the SUMMARY section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | RPTSMRY | An integer value set to zero for no report, or one to produce the report. | 0 |
| Notes:<br>1)  The keyword is terminated by a "/". |  |  |  |

Table 11.32: RPTSMRY Keyword Description

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

\-- ACTIVATE OR DEACTIVATE SUMMARY LIST REPORT

\--

RPTSMRY

1 /

The example switches on the summary list report.
