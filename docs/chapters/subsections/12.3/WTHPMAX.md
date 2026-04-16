### WTHPMAX -- Define a Well's Maximum Flowing THP for Shut-In

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[WTHPMAX](#__RefHeading___Toc1134550_4263943340) stipulates a well's maximum flowing Tubing Head Pressure ("THP"), above which the well will be shut-in. The facility is useful if the THP exceeds the wellhead maximum design pressure, which can occur if excessive gas invades the wellbore. In addition to setting the maximum THP, the keyword defines the criteria for re-testing the well to see if the THP has fallen below the maximum value.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
