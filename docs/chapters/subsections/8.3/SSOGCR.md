### SSOGCR -- End-Point Scaling Grid Cell Surfactant Critical Oil Saturation with Respect to Gas

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SSOGCR defines the surfactant critical oil saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword and the surfactant phase has been activated by the SURFACT keyword in the RUNSPEC section. The critical oil saturation with respect to gas is defined as the maximum oil saturation for which the oil relative permeability is zero in a two-phase gas-oil relative permeability table. SSOGCR scales the surfactant oil relative permeability to gas data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SSOGCR | SSOGCR is an array of real numbers assigning the surfactant critical oil saturation with respect to gas values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.30 dimensionless | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.175: SSOGCR Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SSWL, SSWCR, SSWU, SSGL, SSGCR, SSGU, SSOWCR, and SSOGCR saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and SKRW relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SSOGCR DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SSOGCR

300\*0.200 /

The above example defines a surfactant constant critical oil saturation with respect to gas of 0.20 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
