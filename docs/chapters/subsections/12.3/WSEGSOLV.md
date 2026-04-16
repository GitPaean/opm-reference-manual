### WSEGSOLV -- Define Multi-Segment Well Iterative Linear Solver Parameters

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WSEGSOLV](#__RefHeading___Toc1077655_4263943340) keyword defines the numerical control parameters for the iterative linear solver for multi-segment well looped flow paths, as defined by the [WSEGLINK](#__RefHeading___Toc1020928_4263943340) keyword in the [SCHEDULE](#__RefHeading___Toc43945_784232322) section. A looped segment results in the nodes of the two individual segments that are looped (or connected) having the same solution pressures and oil, water and gas flowing rates.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
