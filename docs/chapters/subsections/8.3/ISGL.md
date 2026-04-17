### ISGL -- End-Point Scaling of Grid Cell Connate Gas Saturation (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ISGL defines the imbibition connate gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section and the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section. The connate gas saturation is defined as the minimum gas saturation in a two-phase gas relative permeability table.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ISGL | ISGL is an array of real numbers assigning the connate gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.03 dimensionless | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the connate gas saturation array used with the end-point scaling option. |  |  |  |

Table 8.64: ISGL Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR saturation grid arrays for the saturation end-points, and the IKRG, IKRORG, IKRORW and IKRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISGLX, ISGLY and ISGLZ instead of ISGL. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISGLX, ISGLX-, ISGLY, ISGLY-, ISGLZ and ISGLZ-, instead of the ISGL keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISGL DATA FOR ALL CELLS (NX x NY x NZ = 300)

ISGL

300\*0.030 /

The above example defines a constant connate gas saturation of 0.03 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
