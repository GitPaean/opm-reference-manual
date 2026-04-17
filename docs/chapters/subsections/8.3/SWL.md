### SWL -- End-Point Scaling Grid Cell Connate Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SWL defines the connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWL | SWL is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.15 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Note this is the directional independent version of the connate gas saturation array used with the end-point scaling option.<br>2)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.187: SWL Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, and the KRG, KRORG, KRORW and KRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWLX, SWLY and SWLZ instead of SWL. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWLX, SWLX-, SWLY, SWLY-, SWLZ and SWLZ-, instead of the SWL keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SWL DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SWL

300\*0.150 /

The above example defines a constant connate water saturation of 0.15 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
