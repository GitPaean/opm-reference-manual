### SKRORG -- End-Point Scaling of Grid Cell Kro(Sgcr) (Surfactant)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SKRORG defines the scaling parameter for the surfactant relative permeability of oil at the critical gas saturation (SGCR), for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword. In addition, the Surfactant option must be enabled by either the SURFST or SURFSTES keywords in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SKRORG | SKRORG is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling SKRORG values for each cell in the model.<br>Repeat counts may be used, for example 50\*0.850. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.159: SKRORG Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be scale on the relative permeability values using the SKRO, SKRORG, SKRORW, SKRW and SKRWR surfactant relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

The example uses the EQUALS keyword to set layer one SKRORG equal to 0.750, layer two SKRORG equals 0.775, and layer three SKRORG equals 0.800.

\--

\-- ARRAY CONSTANT \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

EQUALS

SKRORG 0.7550 1\* 1\* 1\* 1\* 1 1 / SKRORG FOR LAYER 1

SKRORG 0.7750 1\* 1\* 1\* 1\* 2 2 / SKRORG FOR LAYER 2

SKRORG 0.8000 1\* 1\* 1\* 1\* 3 3 / SKRORG FOR LAYER 3

/
