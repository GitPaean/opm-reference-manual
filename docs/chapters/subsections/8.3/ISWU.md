### ISWU -- End-Point Scaling of Grid Cell Maximum Water Saturation (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ISWU defines the imbibition maximum water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE in the RUNSPEC section and the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section. The maximum water saturation is defined as the maximum water saturation in a two-phase water relative permeability table. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ISWU | ISWU is an array of real numbers assigning the maximum water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.70 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the maximum water saturation array used with the end-point scaling option. |  |  |  |

Table 8.72: ISWU Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR saturation grid arrays for the saturation end-points, and the IKRG, IKRORG, IKRORW and IKRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWUX, ISWUY and ISWUZ instead of ISWU. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWUX, ISWUX-, ISWUY, ISWUY-, ISWUZ and ISWUZ-, instead of the ISWU keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISWU DATA FOR ALL CELLS (NX x NY x NZ = 300)

\--

ISWU

300\*0.700 /

The above example defines a constant connate gas saturation of 0.70 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
