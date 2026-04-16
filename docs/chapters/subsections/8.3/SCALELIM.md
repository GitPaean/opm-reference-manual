### SCALELIM -- End-Point Scaling versus Depth Maximum Water Saturation

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword defines the maximum water saturation allowed in a cell for when the end-point versus depth tables are used in the End-Point Scaling option to calculate the water saturation for a grid block. The End-Point Scaling option must be invoked by the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section to use this keyword, and the keyword may only be used in two phase runs containing water, or if the Miscible Flood option has been activated by the [MISCIBLE](#__RefHeading___Toc61978_4106839650) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. This keyword functionality is not supported in OPM Flow.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
