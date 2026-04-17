### SCALC -- Define The Initial Equilibration Calcite Volume Fraction For All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SCALC keyword defines the initial equilibration calcite volume fraction for all grid cells in the model. The keyword should only be used if the MICP model has been activated in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SCALC | SCALC is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration calcite volume fraction values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The sum of SBIOF and SCALC has to be less or equal to the grid cell porosity.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 10.42: SCALC Keyword Description

See also the SBIOF, SMICR, SOXYG and SUREA keywords to define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION CALCITE VOLUME FRACTION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SCALC

1000\*0.0000 1000\*0.0000 1000\*0.0010 /

The above example defines the initial equilibration calcite volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.
