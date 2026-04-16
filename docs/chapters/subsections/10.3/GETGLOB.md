### GETGLOB -- Activate Loading of Global Grid Restart Data Option

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword, [GETGLOB](#__RefHeading___Toc367000_1414963541), switches on the global grid read option for when the run is restarting from a [RESTART](#__RefHeading___Toc135629_1317547213) file. Only the global grid will be loaded in the subsequent [RESTART](#__RefHeading___Toc135629_1317547213) keyword and any Local Grid Refinements ("LGR") on the [RESTART](#__RefHeading___Toc135629_1317547213) file will be ignored.

There is no data required for this keyword.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

#### Example

\--

\-- ACTIVATE LOADING OF GLOBAL GRID RESTART DATA OPTION

\--

GETGLOB

The above example switches on the option to only load the global grid from the [RESTART](#__RefHeading___Toc135629_1317547213) file.
