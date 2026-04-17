### SGCR -- End-Point Scaling Grid Cell Critical Gas Saturations

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SGCR defines the critical gas saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword in the RUNSPEC section. The critical gas saturation is defined as the maximum gas saturation for which the gas relative permeability is zero in a two-phase relative permeability table.

The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SGCR | SGCR is an array of real numbers assigning the critical gas saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.03 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  Note this the directional independent version of the critical gas saturation used with the end-point scaling option. If directional end-point scaling has been activated then the SGCRX± , SGCRX± and SGCRX± series of keyword should be used.<br>2)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 8.146: SGCR Keyword Description

End-point scaling allows the entered relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SWL, SWCR, SWU, SGL, SGCR, SGU, SOWCR, and SOGCR saturation grid arrays for the saturation end-points, and the KRG, KRGR, KRO, KRORG, KRORW, KRW and KRWR relative permeability grid cell arrays for the relative permeability end-point data. In addition end-point scaling may be directional dependent in which case the directional dependent versions of the aforementioned arrays should be used, that is SGCRX, SGCRY and SGCRZ instead of SGCR. There is also the facility to make the directional end-point scaling reversible or non-reversible and if the non-reversible option is selected the non-reversible versions of the aforementioned arrays should be used, that is SGCRX, SGCRX-, SGCRY, SGCRY-, SGCRZ and SGCRZ-, instead of the SGCR keyword.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SGCR DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SGCR

300\*0.050 /

The above example defines a constant critical gas saturation of 0.05 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
