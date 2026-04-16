### MESSOPTS -- Reset Severity Level for Forced Time Steps

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [MESSOPTS](#__RefHeading___Toc557508_3181922006), resets the severity level for time steps that are forced to be accepted by the simulator. The normal severity level for this type of simulator generated message is PROBLEM and this can result in the run stopping depending on the parameters entered on the [MESSAGES](#__RefHeading___Toc61634_2479612490) keyword. [MESSOPTS](#__RefHeading___Toc557508_3181922006) can be used to reset the severity level to [MESSAGE](#__RefHeading___Toc551671_3181922006), COMMENT, WARNING, or PROBLEM; for example, to avoid the run terminating due to too many PROBLEM messages.

Note that the [MESSAGES](#__RefHeading___Toc61634_2479612490) keyword is a global keyword can therefore be used in any section; however, only the last instance of the keywords is active. The [MESSOPTS](#__RefHeading___Toc557508_3181922006) keyword can only be used in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section but can be used multiple times to change the severity level for forced time steps. Again, only the last occurrence of the keyword is active.

This keyword is not supported by OPM Flow but has no effect on the results so it will be ignored.
