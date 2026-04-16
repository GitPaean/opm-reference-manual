### RSSPEC -- Activate Output of the RESTART Index File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [RSSPEC](#__RefHeading___Toc342223_516898843) keyword activates the writing out of the [RESTART](#__RefHeading___Toc135629_1317547213) index file (\*.RSSPEC). The restart data (pressure, saturations etc. through time for each active cell) are written out to two files one file contains the data, \*.UNRST for example, and the second file contains an index of the data (\*.RSSPEC) stored in the \*.UNRST file. This keyword is somewhat redundant as the [RESTART](#__RefHeading___Toc135629_1317547213) index file is written out by default. See the [NORSSPEC](#__RefHeading___Toc79044_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section that deactivates the writing out of the file.

Hence, OPM Flow ignores this keyword. It is documented here for completeness.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE OUTPUT OF THE RESTART INDEX FILE \*.RSSPEC

\--

RSSPEC

The above example switches on the writing of the restart index file (\*.RSSPEC); however, this has no effect in OPM Flow input decks.
