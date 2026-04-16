### HMMLAQUN -- History Match Numerical Aquifer Gradient Multipliers

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [HMMLAQUN](#__RefHeading___Toc463486_2135714711) keyword defines the history match numerical aquifer gradient multipliers for when the History Match Gradient option has been activated by the [HMDIMS](#__RefHeading___Toc207753_4219267791) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section, and numerical aquifers have been specified in the model via the [AQUNUM](#__RefHeading___Toc4430_421927891) keyword and connected to the grid using the [AQUCON](#__RefHeading___Toc115431_846947960) keyword. All keywords are in the [GRID](#__RefHeading___Toc38674_784232322) section.

Multipliers can be declared for numerical aquifers' pore volume, permeability, and aquifer to grid connection factors.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
