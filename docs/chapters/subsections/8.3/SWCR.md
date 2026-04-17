### SWCR -- End-Point Scaling Grid Cell Critical Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SWCR defines the critical water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section. The critical water saturation is defined as the maximum water saturation for which the water relative permeability is zero in a two-phase relative permeability table.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SWCR | SWCR is an array of real numbers assigning the critical water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.20 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Note this the directional independent version of the critical water saturation used with the end-point scaling option. If directional end-point scaling has been activated then the SWCRX± , SWCRY± and SWCRZ± series of keyword should be used.<br>2)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.185: SWCR Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, and the KRG, KRGR, KRO, KRORG, KRORW, KRW and KRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SWCRX, SWCRY and SWCRZ instead of SWCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SWCRX, SWCRX-, SWCRY, SWCRY-, SWCRZ and SWCRZ-, instead of the SWCR keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SWCR DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SWCR

300\*0.200 /

The above example defines a constant critical water saturation of 0.20 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
