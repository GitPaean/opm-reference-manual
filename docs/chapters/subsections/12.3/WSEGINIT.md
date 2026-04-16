### WSEGINIT -- Define Multi-Segment Well Initial Conditions

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

Normally the simulator calculates the initial conditions for multi-segment wells, that is the pressure and fluid distributions in each segment. However, there are occasions when manually setting the pressures and phase distributions for each segment to investigate certain flow conditions may be useful. In this case the [WSEGINIT](#__RefHeading___Toc1006769_4263943340) keyword may be used to specify the initial conditions manually. Note that segments not initialized by this keyword will be automatically initialized by the simulator

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
