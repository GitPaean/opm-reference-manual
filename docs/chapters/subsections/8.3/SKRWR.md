### SKRWR -- End-Point Scaling of Grid Cell KRWR(Sowcr) (Surfactant)

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

SKRWR defines the scaling parameter at the critical oil to water saturation value (SOWCR), for the surfactant water relative permeability curve, for all the cells in the model via an array. The ENDSCALE keyword in the RUNSPEC section should be activated to enable end-point scaling and the use of this keyword.In addition, the Surfactant option must be enabled by either the SURFST or SURFSTES keywords in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SKRWR | SKRWR is an array of positive real numbers which are greater than zero and less than or equal to 1.0, that are the assigned scaling SKRWR values for each cell in the model.<br>Repeat counts may be used, for example 50\*1.000. | Taken from cell allocated relative permeability table. |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 8.162: SKRWR Keyword Description

End-point scaling allows the entered surfactant relative permeability functions to be scale on the relative permeability values using the SKRO, SKRORG, SKRORW, SKRW and SKRWR surfactant relative permeability grid cell arrays for the relative permeability end-point data.

#### Example

The first example defines an input box for the whole grid and for layers one to three, for layer one SKRWR is set equal to 0.750, for layer two SKRWR equals 0.775, and for layer three SKRWR equals 0.800.

\--

\-- DEFINE INPUT BOX FOR EDITING INPUT ARRAYS (NX=100, NY=100)

\--

\-- \-\-\-\-\-\-\-\-\-- BOX \-\-\-\-\-\-\-\--

\-- I1 I2 J1 J2 K1 K2

BOX

1\* 1\* 1\* 1\* 1 3 / DEFINE BOX AREA

\--

\-- SET SKRWR VALUES FOR THREE LAYERS IN THE MODEL

\--

SKRWR

1000\*0.755 1000\*0.775 1000.0.800 /

\--

\-- DEFINE END OF INPUT BOX EDITING OF INPUT ARRAYS

\--

ENDBOX
