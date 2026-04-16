### GASEND -- Define End of Annual Scheduling Section

+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+
| > [RUNSPEC](#3.RUNSPEC SECTION|outline) | > [GRID](#4.GRID SECTION|outline) | > [EDIT](#5.EDIT SECTION|outline) | > [PROPS](#6.PROPS SECTION|outline) | > [REGIONS](#7.REGIONS SECTION|outline) | > [SOLUTION](#8.SOLUTION SECTION|outline) | > [SUMMARY](#9.SUMMARY SECTION|outline) | > [SCHEDULE](#10.SCHEDULE SECTION|outline) |
+-----------------------------------------+-----------------------------------+-----------------------------------+-------------------------------------+-----------------------------------------+-------------------------------------------+-----------------------------------------+--------------------------------------------+

#### Description

This keyword, [GASEND](#__RefHeading___Toc184153_2330925267), defines the end of an Annual Scheduling section set of keywords used when the Gas Field Operations option has been activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. An Annual Scheduling section starts with the [GASBEGIN](#__RefHeading___Toc184151_2330925267) keyword and is terminated by the [GASEND](#__RefHeading___Toc184153_2330925267) keyword, with keywords in between used to control and write reports at selected times between the start and end of a contract period. Only one Annual Scheduling section is activate at a time, that is, a subsequent Annual Scheduling section overwrites the previous set of entries. To clear the current Annual Schedule section enter the [GASBEGIN](#__RefHeading___Toc184151_2330925267) keyword followed by the [GASEND](#__RefHeading___Toc184153_2330925267) keyword word with no other keywords in between.

There is no data required for this keyword and there is no terminating "/" for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
