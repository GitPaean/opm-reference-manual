### HWPCW -- End-Point Scaling of Grid Cell Water Capillary Pressure (High Salinity and Water Wet)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

HWPCW defines the maximum water-oil pressure values for all the cells in the model via an array, for when the Low Salt and Surfactant Wettability options have been selected. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition the Low Salt option should be activated by the LOWSALT keyword in the RUNSPEC section and the Surfactant Wettability option activated by the SURFACT or SURFACTW keywords, which are also in the RUNSPEC section. The keyword re-scales the oil-water capillary pressure in the high salinity water wet capillary saturation tables from a cell's assigned saturation function by the grid block's HWPCW value.

The capillary pressure for a grid block is scaled by:

Where:

P~c~ = the resulting high salinity water wet water capillary pressure for a grid cell.

HWPCW = the maximum capillary pressure from the HWPCW array for a given cell.

= the capillary pressure in the high salinity water wet water capillary pressure

table allocated to the grid block.

= the maximum capillary pressure in the high salinity water wet water

capillary pressure table allocated to the grid block (that is at the connate

water saturation).

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.
