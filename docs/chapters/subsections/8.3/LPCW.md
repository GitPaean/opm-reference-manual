### LPCW -- End-Point Scaling of Grid Cell Water Capillary Pressure (Low Salinity and Oil Wet)

| [RUNSPEC](#3.RUNSPEC SECTION|outline) | [GRID](#4.GRID SECTION|outline) | [EDIT](#5.EDIT SECTION|outline) | [PROPS](#6.PROPS SECTION|outline) | [REGIONS](#7.REGIONS SECTION|outline) | [SOLUTION](#8.SOLUTION SECTION|outline) | [SUMMARY](#9.SUMMARY SECTION|outline) | [SCHEDULE](#10.SCHEDULE SECTION|outline) |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

[LPCW](#__RefHeading___Toc332422_2843394514) defines the maximum oil-water pressure values for all the cells in the model via an array, for when the Low Salt option and the End-point Scaling options has been activated by the [LOWSALT](#__RefHeading___Toc331072_2843394514) and the [ENDSCALE](#__RefHeading___Toc68146_2267116897) keywords in the [RUNSPEC](#__RefHeading___Toc55591_1778172979) section. The keyword re-scales the oil-water capillary pressure in the low salinity oil wet capillary saturation tables from a cell's assigned saturation function by the grid block's [LPCW](#__RefHeading___Toc332422_2843394514) value.

The capillary pressure for a grid block is scaled by:

Where:

= the resulting low salt oil wet water capillary pressure for a grid cell.

= the maximum capillary pressure from the [LPCW](#__RefHeading___Toc332422_2843394514) array for a given cell.

= the capillary pressure in the low salt oil wet capillary pressure table

allocated to the grid block.

= the maximum capillary pressure in the low salt oil capillary pressure table

allocated to the grid block (that is at the connate water saturation).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
