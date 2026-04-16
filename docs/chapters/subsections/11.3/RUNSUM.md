### RUNSUM -- Activate RSM File Output of the SUMMARY Data

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file data in a columnar format to the PRT file. Normally the [SEPARATE](#__RefHeading___Toc210158_2884651453) keyword in the [SUMMARY](#__RefHeading___Toc43949_784232322) section is invoked in the same run to direct the data stream to a separate RSM file for easy loading into other programs, for example, Microsoft\'s EXCEL or LibreOffice's CALC spreadsheet programs.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See also the [EXCEL](#__RefHeading___Toc210148_2884651453), [RPTONLY](#__RefHeading___Toc210150_2884651453) and [SEPARATE](#__RefHeading___Toc210158_2884651453) keywords in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.

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
