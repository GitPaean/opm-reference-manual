### WPOLYRED -- Define Well Polymer-Water Viscosity Reduction Factor

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The [WPOLYRED](#__RefHeading___Toc642188_4263943340) keyword defines the polymer-water reduction factor for injection wells, for when the polymer phase has been activated by the [POLYMER](#__RefHeading___Toc38609_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. [WPOLYRED](#__RefHeading___Toc642188_4263943340) should be set to a value greater than or equal to zero and less than or equal to one that determines the injection mixture's viscosity. A value of zero indicates for pure water injection and a value of one will use the simulator's valuated mixture viscosity. A value between zero and one will use an interpolated mixture viscosity.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
