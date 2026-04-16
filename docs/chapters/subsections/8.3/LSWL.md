### LSWL -- End-Point Scaling Grid Cell SWL (Low Salinity and Oil Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[LSWL](#__RefHeading___Toc299564_3734856631) defines the connate water saturation ("SWL"), for all the cells in the model via an array, for when the Low Salt option has been selected. The data is used to scale the water saturation in the low salinity oil wet water-oil relative permeability saturation tables, as well as the associated capillary pressure tables. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
