### RPTSMRY -- Activate or Deactivate Summary List Report

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates or deactivates a listing of all the summary variables that are going to be written to the [SUMMARY](#__RefHeading___Toc43949_784232322) file and the RSM file, if the RSM file option has been requested by the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| 1 | [RPTSMRY](#__RefHeading___Toc140842_332691817) | An integer value set to zero for no report, or one to produce the report. | 0 |
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
