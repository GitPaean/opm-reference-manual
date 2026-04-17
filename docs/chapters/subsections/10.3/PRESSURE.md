### PRESSURE -- Define the Initial Equilibration Pressures for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The PRESSURE keyword defines the initial equilibration pressures for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, RS, RV, SGAS, SOIL and SWAT keywords etc., to fully describe the initial state of the model.

The keyword is used by the Enumeration Initialization method to initialize the model, as opposed to the Equilibration Initialization method that utilizes the EQUIL keyword in the SOLUTION section. This is the non-standard formulation to initialize the model and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PRESSURE | PRESSURE is an array of real positive numbers assigning the initial equilibration pressures to each cell in the model.<br>Repeat counts may be used, for example 20\*4200.0. | None |
| psia | barsa | atma |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.23: PRESSURE Keyword Description

See also the PBUB, PDEW, RS, RV, SGAS, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION PRESSURES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

PRESSURE

1000\*4500.0 1000\*4510.0 1000\*4520.0 /

The above example defines the initial equilibration pressures to be 4500.0 for all the cells in the first layer, 4510.0 for all the cells in the second layer, and finally 4520.0 for all the cells in the third layer.
