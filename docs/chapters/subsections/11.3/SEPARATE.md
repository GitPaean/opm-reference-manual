### SEPARATE -- Activate the Separate RSM File Output Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates the writing out of the [SUMMARY](#__RefHeading___Toc43949_784232322) file date in a columnar format to the RSM file, if the [RUNSUM](#__RefHeading___Toc210156_2884651453) keyword has also been activated in the [SUMMARY](#__RefHeading___Toc43949_784232322) section. Both the [SEPARATE](#__RefHeading___Toc210158_2884651453) and the [RUNSUM](#__RefHeading___Toc210156_2884651453) keywords need to be invoked. If the [SEPARATE](#__RefHeading___Toc210158_2884651453) option is not activated then the RSM output is directed to the end of the PRT file. Normally the both the [SEPARATE](#__RefHeading___Toc210158_2884651453) and [RUNSUM](#__RefHeading___Toc210156_2884651453) keywords are invoked in the same run to enable easy loading of the data into Microsoft\'s EXCEL or LibreOffice's CALC spreadsheet programs.

There is no data required for this keyword and there is no terminating "/" for this keyword.

See also the [EXCEL](#__RefHeading___Toc210148_2884651453), [RPTONLY](#__RefHeading___Toc210150_2884651453) and [RUNSUM](#__RefHeading___Toc210156_2884651453) keywords in the [SUMMARY](#__RefHeading___Toc43949_784232322) section.

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

Note unlike the commercial simulator, OPM Flow always writes out the data to a separate file; however, it is probably good practice to include it if the same input decks are being run with commercial simulator.
