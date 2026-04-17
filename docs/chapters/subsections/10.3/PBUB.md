### PBUB -- Define the Initial Equilibration Bubble-Point Pressure for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PBUB keyword defines the initial equilibration buble-point saturation pressures values for all grid cells in the model and should be used in conjunction with the PDEW, PRESSURE, RS, RV, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if dissolved gas has been activated in the model via the DISGAS keyword in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PBUB | PBUB is an array of real positive numbers assigning the initial equilibration bubble-point saturation pressure values to each cell in the model.<br>Repeat counts may be used, for example 20\*3500.0 | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.19: PBUB Keyword Description

See also the PBVD, PDEW, PRESSURE, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION PSAT VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

PBUB

1000\*3500.0 1000\*3525.0 1000\*0.3535.0 /

The above example defines the initial equilibration bubble-point saturation pressure values to be 3500.0 for all the cells in the first layer, 3525.0 for all the cells in the second layer, and finally 3535.0 for all the cells in the third layer.
