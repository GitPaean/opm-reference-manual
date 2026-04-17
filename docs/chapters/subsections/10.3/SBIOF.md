### SBIOF -- Define The Initial Equilibration Biofilm Volume Fraction For All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SBIOF keyword defines the initial equilibration biofilm volume fraction for all grid cells in the model. The keyword should only be used if either the BIOFILM or MICP model has been activated in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SBIOF | SBIOF is an array of real numbers that are greater than or equal to zero and less than or equal to one assigning the initial equilibration biofilm volume fraction values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.0010. | None |
| dimensionless | dimensionless | dimensionless |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  Physical values are less or equal to the grid cell porosity. For the MICP model, then the sum of SBIOF and SCALC has to be less or equal to the grid cell porosity.<br>3)  The keyword is terminated by a "/". |  |  |  |

Table 10.41: SBIOF Keyword Description

For both BIOFILM and MICP models, see also the SMICR keyword, and for the MICP model, the SCALC, SOXYG, and SUREA keywords to define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION BIOFILM VOLUME FRACTION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SBIOF

10000\*0.0000 10000\*0.0000 10000\*0.0010 /

The above example defines the initial equilibration biofilm volume fraction values to be 0.0000 for all the cells in the first and second layers and finally 0.0010 for all the cells in the third layer.
