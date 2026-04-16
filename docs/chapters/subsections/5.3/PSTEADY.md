### PSTEADY -- Activate Pseudo Steady State Flow Calculation Option

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [PSTEADY](#__RefHeading___Toc295004_501926209) keyword activates Pseudo Steady State Flow Calculation option by advancing the simulator until it reaches a pseudo steady state flow and then sets the date to the date defined on this keyword, that is written to the [RESTART](#__RefHeading___Toc135629_1317547213) file. Keyword also includes parameters defining the conditions for pseudo steady flow state.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
