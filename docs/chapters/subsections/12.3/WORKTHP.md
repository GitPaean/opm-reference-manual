### WORKTHP -- Define Well Workover Options for THP Killed Wells

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

The [WORKTHP](#__RefHeading___Toc123815_332691817) keyword defines workover options for when a well dies, that is unable to produce at the current operating conditions, when under Tubing Head Pressure ("THP") control. For example, if a well is producing to the high pressure separator and therefore has a high THP constraint, then the [WORKTHP](#__RefHeading___Toc123815_332691817) keyword can be used to switch the well to the lower pressure separator via re-setting the THP constraint.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
