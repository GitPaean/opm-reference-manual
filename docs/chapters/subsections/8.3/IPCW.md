### IPCW -- End-Point Scaling of Grid Cell Water Capillary Pressure (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

IPCW defines the maximum imbibition water-oil or water-gas capillary pressure values for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition, the HYSTER option on the SATOPTS keyword in the RUNSPEC section has to be activated to invoke the hysteresis option. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | IPCW | IPCW is an array of positive real numbers assigning the maximum imbibition water capillary pressure values for each cell in the model.<br>Repeat counts may be used, for example 30\*100.0. | None |
| psia | bars | atm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.62: IPCW Keyword Description

The capillary pressure for a grid block is scaled by:

Where:

= the resulting imbibition water capillary pressure for a grid cell.

= the maximum capillary pressure from the IPCW array for a given cell.

= the capillary pressure in the imbibition capillary pressure table

allocated to the grid block.

= the maximum capillary pressure in the imbibition capillary pressure table

allocated to the grid block (that is at the connate water saturation).

See also the PCW keyword for the equivalent drainage functionality.

#### Example

\--

\-- DEFINE GRID BLOCK IPCW DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

IPCW

100\*50.0 100\*75.0 100\*125.0 /

The above example defines the IPCW for 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
