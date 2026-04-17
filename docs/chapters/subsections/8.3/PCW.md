### PCW -- End-Point Scaling of Grid Cell Water Capillary Pressure (Drainage)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PCW defines the maximum drainage water-oil or water-gas capillary pressure values for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PCW | PCW is an array of positive real numbers assigning the maximum drainage water capillary pressure values for each cell in the model.<br>Repeat counts may be used, for example 30\*100.0. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  If the HYSTER on the SATOPTS keyword in the RUNSPEC section has been activated to invoke hysteresis then PCW scales the drainage curve and IPCW scales the imbibition curve.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.96: PCW Keyword Description

See also the IPCW keyword for the equivalent imbibition functionality.

The capillary pressure for a grid block is scaled by:

Where:

= the resulting drainage water capillary pressure for a grid cell.

= the maximum capillary pressure from the PCW array for a given cell.

= the capillary pressure in the drainage capillary pressure table allocated

to the grid block.

= the maximum capillary pressure in the drainage capillary pressure table

allocated to the grid block (that is at the connate water saturation).

#### Example

\--

\-- DEFINE GRID BLOCK PCW DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PCW

100\*50.0 100\*75.0 100\*125.0 /

The above example defines the PCW for 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
