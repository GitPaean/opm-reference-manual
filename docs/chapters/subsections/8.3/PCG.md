### PCG -- End-Point Scaling of Grid Cell Maximum Gas Capillary Pressure (Drainage)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PCG defines the maximum drainage gas-oil capillary pressure values for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped. See also the IPCG keyword for the equivalent imbibition functionality.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PCG | PCG is an array of positive real numbers assigning the maximum drainage gas-oil capillary pressure values for each cell in the model.<br>Repeat counts may be used, for example 30\*100.0. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If the HYSTER on the SATOPTS keyword in the RUNSPEC section has been activated to invoke hysteresis then PCG scales the drainage curve and IPCG scales the imbibition curve.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.95: PCG Keyword Description

The capillary pressure for a grid block is scaled by:

Where:

~\ ~= the resulting drainage gas-oil capillary pressure for a grid cell.

= the maximum capillary pressure from the PCG array for a given cell.

= the capillary pressure in the drainage capillary pressure table

allocated to the grid block.

= the maximum capillary pressure in the drainage capillary pressure table

allocated to the grid block at .

#### Example

\--

\-- DEFINE GRID BLOCK PCG DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PCG

100\*50.0 100\*75.0 100\*125.0 /

The above example defines the PCW for 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
