### SAVE -- Activate Output of a SAVE File for Fast Restarts

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword activates output of a SAVE file for fast restarts which are read in by the [LOAD](#__RefHeading___Toc309839_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. No data is required for this keyword.

OPM Flow does not support the SAVE file format for fast restarts like the commercial simulator, but instead writes a standard [RESTART](#__RefHeading___Toc135629_1317547213) file at the requested time step in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section, which can then be used to restart the simulation at a given point in time via the [RESTART](#__RefHeading___Toc135629_1317547213) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

#### Example

The first example requests that a SAVE file be written out in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section; however, OPM Flow will not write a [RESTART](#__RefHeading___Toc135629_1317547213) record if the [SAVE](#__RefHeading___Toc55597_1778172979) keyword is encountered in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

\-- ==============================================================================

\--

\-- RUNSPEC SECTION

\--

\-- ==============================================================================

RUNSPEC

\--

\-- WRITE OUT SAVE FILE FOR FAST RESTARTS

\--

SAVE

The second example shows how the keyword is used in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section.

\-- ==============================================================================

\--

\-- SCHEDULE SECTION

\--

\-- ==============================================================================

SCHEDULE

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\-- SCHEDULE SECTION - 2020-01-01

\-- \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

RPTSCHED

\'WELLS=2\' \'WELSPECS\' \'CPU=2\' FIP=2\' /

DATES

1 APR 2021 /

/

\--

\-- WRITE OUT SAVE FILE FOR FAST RESTARTS

\--

SAVE

DATES

1 JLY 2021 /

1 OCT 2021 /

/

Here OPM Flow will write out a [RESTART](#__RefHeading___Toc135629_1317547213) file instead of a SAVE file at April 1^st^, 2021.
