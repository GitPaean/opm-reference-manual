### WGASPROD -- Define Sale Gas Well Production Targets

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WGASPROD](#__RefHeading___Toc121396_332691817) keyword declares wells to be Sales Gas producers and sets the incremental gas rate for a well and the maximum number of increments that this rate can be increased. Wells must have been previously been defined via the [WELSPECS](#__RefHeading___Toc268463_1366622701) and [WCONPROD](#__RefHeading___Toc146754_4203985108) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section and are subject to any targets or constraints on [WCONPROD](#__RefHeading___Toc146754_4203985108) keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
