### OLDTRANR -- Activate Radial Regular Grid Transmissibilities

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword switches on Radial Regular Grids geometry transmissibility calculation (or block centered transmissibility calculations), which is the default option for this type of grid. Grids defined by the [DR](#__RefHeading___Toc113051_2066951158), [DTHETA](#__RefHeading___Toc120096_2066951158), and [DZ](#__RefHeading___Toc45769_719036256) series of keywords will always invoke this option by default.

For Irregular Corner-Point Grids defined by the [COORD](#__RefHeading___Toc45757_719036256) and [ZCORN](#__RefHeading___Toc45757_7190362561) keywords Irregular Corner-Point Grid geometry transmissibility calculations should be activated via the [NEWTRAN](#__RefHeading___Toc98717_3218818441) keyword. Again this is automatically invoked if this type of grid is being employed.

There is no data required for this keyword and there is no terminating "/" for this keyword.

#### Example

\--

\-- ACTIVATE RADIAL REGULAR GRID TRANSMISSIBILITIES

\--

OLDTRANR

The above example manually activates Radial Regular Grid transmissibility calculations.
