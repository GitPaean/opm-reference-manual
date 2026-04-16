### UNIFOUTS -- Activate The Unified Output Summary File Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [UNIFOUTS](#__RefHeading___Toc1695476_4250154414) keyword causes the [SUMMARY](#__RefHeading___Toc43949_784232322) file output files to be a unified file, as opposed to non-unified multiple files. A unified file is a single file containing output for each reporting time step. Here a single [SUMMARY](#__RefHeading___Toc43949_784232322) file will be generated, as opposed to one file per report time step. See also the [MULTOUT](#__RefHeading___Toc195175_1371377330) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that sets both the [SUMMARY](#__RefHeading___Toc43949_784232322) and [RESTART](#__RefHeading___Toc135629_1317547213) files to be non-unified multiple files, as opposed to unified files. Note also that [UNIFOUTS](#__RefHeading___Toc1695476_4250154414) keyword has precedence over the [MULTOUT](#__RefHeading___Toc195175_1371377330) keyword for [SUMMARY](#__RefHeading___Toc43949_784232322) files.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- ACTIVATE THE UNIFIED OUTPUT SUMMARY FILE OPTION

\--

UNIFOUTS

The above example switches on writing of unified [SUMMARY](#__RefHeading___Toc43949_784232322) output files.
