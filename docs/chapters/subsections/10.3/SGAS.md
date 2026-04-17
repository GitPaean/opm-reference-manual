### SGAS -- Define the Initial Equilibration Gas Saturation for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SGAS keyword defines the initial equilibration gas saturation values for all grid cells in the model and should be used in conjunction with the PBUB, PDEW, PRESSURE, RS, RV, SOIL and SWAT keywords etc., to fully describe the initial state of the model. The keyword should only be used if the gas phase has been activated in the model via the GAS keyword in the RUNSPEC section.

This is the non-standard method to initialize the model via enumeration and is seldom employed in the industry. The standard methodology is for OPM Flow to initialize a model using the parameters on the EQUIL keyword combined with other keywords to fully describe the initial state of the model. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SGAS | SGAS is an array of real positive numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration gas saturation values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.600. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.45: SGAS Keyword Description

Note for two phase runs it is only necessary to enter one saturation array of one of the phases present in the run (SGAS, SOIL, or SWAT), as the simulator will calculate the other phases by difference. Similarly for three phase runs it is only necessary to enter the array data for two of the phases, as the third saturation will again be calculated by the simulator.

See also the PBUB, PDEW, PRESSURE, RS, RV, SOIL and SWAT keywords to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION GAS SAT VALUES FOR ALL CELLS IN THE MODEL

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SGAS

1000\*0.7000 1000\*0.6500 1000\*0.6000 /

The above example defines the initial equilibration gas saturation values to be 0.7000 for all the cells in the first layer, 0.6500 for all the cells in the second layer, and finally 0.6000 for all the cells in the third layer.
