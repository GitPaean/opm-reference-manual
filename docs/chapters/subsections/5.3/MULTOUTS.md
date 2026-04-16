### MULTOUTS -- Activate Non-Unified Multiple Summary Output File Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on the Multiple Output Files option for [SUMMARY](#__RefHeading___Toc43949_784232322) files only, and overwrites the [UNIFOUT](#__RefHeading___Toc65809_1640804870) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that activates the Unified Output Files option for all output files.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

See also [[OPM FLOW OUTPUT FILE FORMATS](#anchor-2)](#16.APPENDIX – OPM FLOW OUTPUT FILE FORMATS|outline) for a more detailed description of the various file types (ASCII or binary) and file structure formats (unified or non-unified formats).

#### Example

\--

\-- ACTIVATE MULTIPLE OUTPUT SUMMARY FILES ONLY OPTION

\--

MULTOUTS

The above example switches on the multiple output file option.
