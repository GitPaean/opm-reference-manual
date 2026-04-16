### HWPCW -- End-Point Scaling of Grid Cell Water Capillary Pressure (High Salinity and Water Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[HWPCW](#__RefHeading___Toc258551_4219267791) defines the maximum water-oil pressure values for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected. The [ENDSCALE](#__RefHeading___Toc68146_2267116897) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section should be activated to enable end-point scaling and the use of this keyword. In addition the Low Salt option should be activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) keyword in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section and the Surfactant Wettability option activated by the [SURFACT](#__RefHeading___Toc863854_4250154414) or [SURFACTW](#__RefHeading___Toc863864_4250154414) keywords, which are also in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword re-scales the oil-water capillary pressure in the high salinity water wet capillary saturation tables from a cell's assigned saturation function by the grid block's [HWPCW](#__RefHeading___Toc258551_4219267791) value.

The capillary pressure for a grid block is scaled by:

Where:

P~c~ = the resulting high salinity water wet water capillary pressure for a grid cell.

[HWPCW](#__RefHeading___Toc258551_4219267791) = the maximum capillary pressure from the [HWPCW](#__RefHeading___Toc258551_4219267791) array for a given cell.

= the capillary pressure in the high salinity water wet water capillary pressure

table allocated to the grid block.

= the maximum capillary pressure in the high salinity water wet water

capillary pressure table allocated to the grid block (that is at the connate

water saturation).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
