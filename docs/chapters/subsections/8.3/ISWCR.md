### ISWCR -- End-Point Scaling of Grid Cell Critical Water Saturation (Imbibition)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

ISWCR defines the imbibition critical water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE in the RUNSPEC section and the hysteresis model option has been activated on the SATOPTS keyword in the RUNSPEC section. The critical water saturation is defined as the maximum water saturation for which the water relative permeability is zero in a two-phase relative permeability table. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | ISWCR | ISWCR is an array of real numbers assigning the critical water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.20 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/".<br>3)  Note this is the directional independent version of the critical water saturation used with the end-point scaling option. |  |  |  |

Table 8.69: ISWCR Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the ISWL, ISWCR, ISWU, ISGL, ISGCR, ISGU, ISOWCR, and ISOGCR saturation grid arrays for the saturation end-points, and the IKRG, IKRORG, IKRORW and IKRW relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is ISWCRX, ISWCRY and ISWCRZ instead of ISWCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is ISWCRX, ISWCRX-, ISWCRY, ISWCRY-, ISWCRZ and ISWCRZ-, instead of the ISWCR keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT ISWCR DATA FOR ALL CELLS

\-- (NX x NY x NZ = 300)

\--

ISWCR

300\*0.200 /

The above example defines a constant critical water saturation of 0.20 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
