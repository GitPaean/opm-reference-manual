### SSWU -- End-Point Scaling Grid Cell Surfactant Maximum Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SSWU defines the surfactant maximum water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword and the surfactant phase has been activated by the SURFACT keyword in the RUNSPEC section. The maximum water saturation is defined as the maximum water saturation in a two-phase water relative permeability table. SSWU scales the surfactant water relative permeability data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SSWU | SSWU is an array of real numbers assigning the surfactant maximum water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.70 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.179: SSWU Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SSWL, SSWCR, SSWU, SSGL, SSGCR, SSGU, SSOWCR, and SSOGCR saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and SKRW relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SSWU DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SSWU

300\*0.700 /

The above example defines a constant surfactant connate gas saturation of 0.70 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
