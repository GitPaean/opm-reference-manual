### EXCEL -- Activate the EXCEL Option for the SUMMARY File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword activates the writing out of the RSM file data in a format that can easily be loaded into Microsoft\'s EXCEL spreadsheet program or LibreOffice's CALC spreadsheet program. The RSM file output is activated by the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.

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

The above example activates the [SUMMARY](#__RefHeading___Toc43949_784232322) file [EXCEL](#__RefHeading___Toc210148_2884651453) option for directly loading the RSM file into either Microsoft\'s EXCEL or LibreOffice's CALC spreadsheet programs.
