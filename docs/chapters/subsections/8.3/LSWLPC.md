### LSWLPC -- End-Point Scaling Grid Cell SWLPC (Low Salinity and Oil Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[LSWLPC](#__RefHeading___Toc299573_3734856631) defines the capillary pressure connate water saturation ("SWLPC"), for all the cells in the model via an array, for when the Low Salt option has been selected. The data is used to scale the water saturation in the low salinity oil wet water-oil capillary pressure tables. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition, the Low Salt option should be activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section.

Note the keyword only applies the scaling to the capillary pressures tables, unlike the [LSWL](#__RefHeading___Toc299564_3734856631) keyword that applies the scaling to both the capillary pressure and relative permeability tables.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
