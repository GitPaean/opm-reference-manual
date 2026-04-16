### SKIP -- Activate Skipping of All Keywords and Input Data

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [SKIP](#__RefHeading___Toc52489_2479612490) keyword activates skipping of all keywords and input data until the [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword is encountered. All keywords between the [SKIP](#__RefHeading___Toc52489_2479612490) and [ENDSKIP](#__RefHeading___Toc52491_2479612490) keywords are ignored. Each [SKIP](#__RefHeading___Toc52489_2479612490) keyword should be paired with an [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword. See also the [SKIP100](#__RefHeading___Toc65046_1640804870) and [SKIP300](#__RefHeading___Toc980121_1781444514) keywords.

There is no data required for this keyword.

The nesting of pairs of the [SKIP](#__RefHeading___Toc52489_2479612490), [SKIP100](#__RefHeading___Toc65046_1640804870), or [SKIP300](#__RefHeading___Toc980121_1781444514) keywords and the [ENDSKIP](#__RefHeading___Toc52491_2479612490) keyword is not supported by OPM Flow.

#### Example

\--

\-- SWITCH ON SKIPPING OF ALL KEYWORDS AND DATA

\--

SKIP

\--

\-- INCLUDE SIMULATION GRID WITH SLOPING FAULTS

\--

INCLUDE

\'./INCLUDE/GRID/IRAP_1005.GRDECL\' /

\--

\-- SWITCH ON READING OF ALL KEYWORDS AND DATA

\--

ENDSKIP

The example skips reading of the grid geometry data input using the [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword, and then reverts back to reading the remainder of the input file.
