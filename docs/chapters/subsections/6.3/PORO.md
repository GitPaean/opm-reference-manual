### PORO -- Define the Porosity Values for All the Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

PORO defines the porosity for all the cells in the model via an array. The keyword can be used with all grid types.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | PORO | PORO is an array of real positive numbers that are greater than or equal to zero and less than or equal to one that are the porosity values for each cell in the model.<br>Repeat counts may be used, for example 3000\*0.15 | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 6.112: PORO Keyword Description

See also the NTG, PERMX, PERMY and PERMX keywords to fully define a grid's properties

#### Example

\--

\-- DEFINE GRID BLOCK POROSITY DATA FOR ALL CELLS (BASED ON NX x NY x NZ = 300)

\--

PORO

300\*0.300 /

The above example defines a constant porosity of 0.300 to all 300 cells in the model as defined by the DIMENS keyword in the RUNSPEC section.
