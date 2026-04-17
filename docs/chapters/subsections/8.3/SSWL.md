### SSWL -- End-Point Scaling Grid Cell Surfactant Connate Water Saturation

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SSWL defines the surfactant connate water saturation for all the cells in the model via an array when the end-point scaling option has been invoked via the ENDSCALE keyword and the surfactant phase has been activated by the SURFACT keyword in the RUNSPEC section. The connate water saturation is defined as the minimum water saturation in a two-phase water relative permeability table. SSWL scales the surfactant oil relative permeability to water and gas data.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SSWL | SSWL is an array of real numbers assigning the connate water saturation values to each cell in the model. The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword.<br>Repeat counts may be used, for example 30\*0.15 | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  If the value for a cell has been defaulted then OPM Flow uses the value from the cell's relative permeability table.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.178: SSWL Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be re-scaled based on the saturation end-points allocated to each cell by the SSWL, SSWCR, SSWU, SSGL, SSGCR, SSGU, SSOWCR, and SSOGCR saturation grid arrays for the saturation end-points, and the SKRG, SKROG, SKROW and SKRW relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

\--

\-- DEFINE GRID BLOCK END-POINT SSWL DATA FOR ALL CELLS

\-- (FOR NX x NY x NZ = 300)

\--

SSWL

300\*0.150 /

The above example defines a constant surfactant connate water saturation of 0.15 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
