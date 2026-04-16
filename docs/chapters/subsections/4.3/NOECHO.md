### NOECHO -- Deactivate Echoing of User Input Files to the Print File

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

Turns off echoing of all the input files to the print file. Note by default echoing of the inputs files is active, but can subsequently be switched off by the [NOECHO](#__RefHeading___Toc52487_2479612490) activation keyword.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.

#### Example

\--

\-- SWITCH OFF ECHOING OF INPUT FILES

\--

NOECHO

\--

\-- INCLUDE SIMULATION GRID WITH SLOPING FAULTS

\--

INCLUDE

\'./INCLUDE/GRID/IRAP_1005.GRDECL\' /

\--

\-- SWITCH ON ECHOING OF INPUT FILES

\--

ECHO

The example deactivates the echoing of the input files, reads in the grid geometry data using the [INCLUDE](#__RefHeading___Toc55749_2479612490) keyword, and then activates the echoing of the input files again.
