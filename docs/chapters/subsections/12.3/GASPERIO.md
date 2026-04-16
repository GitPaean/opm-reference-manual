### GASPERIO -- Advance Simulation by Gas Contract Period

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

This keyword advances the simulation over one or more gas contract periods for when the Gas Field Operations option has been activated by the [GASFIELD](#__RefHeading___Toc195426_1190369742) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. A contract period in this case is the period over which the Daily Contract Quantity is fixed, this can a be year or one or more months. If the contract period is a year then the [GASYEAR](#__RefHeading___Toc493664_1414963541) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section can be used instead of GASPERIOD.

[GASPERIO](#__RefHeading___Toc206080_1190369742) is an alternative to the [DATES](#__RefHeading___Toc117621_2179381650), [TIME](#__RefHeading___Toc1252966_4250154414) and [TSTEP](#__RefHeading___Toc118323_1596574740) keywords in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section that advances the simulation to a given report time after which additional keywords may be entered to instruct OPM Flow to perform additional functions via the [SCHEDULE](#__RefHeading___Toc43945_784232322) section keywords.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
