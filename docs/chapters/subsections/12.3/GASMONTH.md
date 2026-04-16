### GASMONTH -- Define Start of Annual Scheduling Event

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [GASMONTH](#__RefHeading___Toc200751_1190369742), states the month for which subsequent scheduling events take place within an Annual Schedule section for when the Gas Field Operations option has been activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword must lie in between the [GASBEGIN](#__RefHeading___Toc184151_2330925267), that defines the start of an Annual Scheduling section and the [GASEND](#__RefHeading___Toc184153_2330925267) keyword that ends the section. Optionally, the keyword can be used to write a report to the print file (\*.PRT) at the requested month.

See also the [GASBEGIN](#__RefHeading___Toc184151_2330925267) and [GASEND](#__RefHeading___Toc184153_2330925267) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
