### WTEMPQ -- Output Well Names and Well Lists to the Print File

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WTEMPQ](#__RefHeading___Toc1127430_4263943340) prints out a user defined selected list of currently defined wells and well lists to the print file (\*.PRT). The keyword allows for sub-setting the well names etc., using the normal well and well list naming conventions. For example to list all wells beginning with the characters "OP" then one would use "OP\*" as the well name on this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
