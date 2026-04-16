### WFRICTN -- Define Well as a Friction Well

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WFRICTN](#__RefHeading___Toc1032924_487874538) keyword is used to declare a previously defined well as a friction well and to set the characteristics for this type of well including: tubing size, pipe roughness, and the connections to the grid. Wellbore friction is important in horizontal and multi-lateral wells where the pressure loss along the pipe can effect a well's performance. Note that unlike other [SCHEDULE](#__RefHeading___Toc43945_784232322) section well keywords, multiple wells cannot be entered with one [WFRICTN](#__RefHeading___Toc1032924_487874538) keyword, that is, the keyword must be repeated for each well.

See also the [WFRICTNL](#__RefHeading___Toc1032926_487874538) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that performs similar functionality for wells in Local Grid Refinements.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
