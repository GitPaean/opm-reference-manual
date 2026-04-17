### SOLVFRAC -- Define the Initial Gas Solvent Fraction for All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SOLVFRAC keyword defines the initial solvent faction within the gas phase values for all matrix grid cells in the model. The keyword should only be used if the coal phase has been activated in the model via the COAL keyword in the RUNSPEC section.

This keyword is not supported by OPM Flow but would change the results if supported so the simulation will be stopped.

SOLVFRAC is used with the *standard *equilibration method to initialize the model via the EQUIL keyword in the RUNSPEC section, as oppose to the non-standard enumeration method.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SOLVFRAC | SOLVFRAC is an array of real positive numbers that define the initial solvent fraction within the gas phase values for each matrix cell in the model.<br>Repeat counts may be used, for example 20\*0.075. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to number of matrix cells in the model, that is (NX x NY x NZ) divided by two, as per the parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.49: SOLVFRAC Keyword Description

See also the EQUIL keyword in the SOLUTION section to fully define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION GAS SOLVENT FRACTION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 6

\--

SOLVFRAC

1000\*0.0250 1000\*0.0350 1000\*0.0500 /

The above example defines the initial gas solvent fraction values to be 0.250 for all the matrix cells in the first layer, 0.0350 for all the cells in the second layer, and finally 0.0500 for all the cells in the third layer.
