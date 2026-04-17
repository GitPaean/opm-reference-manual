### SOXYG -- Define The Initial Equilibration Oxygen Concentration For All Grid Blocks

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The SOXYG keyword defines the initial equilibration oxygen concentration values for all grid cells in the model. The keyword should only be used if the MICP model has been activated in the RUNSPEC section.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
| Field | Metric | Laboratory |  |
| 1 | SOXYG | SOXYG is an array of real numbers that are greater than or equal to zero assigning the initial equilibration oxygen concentration values to each cell in the model.<br>Repeat counts may be used, for example 20\*0.1500 | None |
| lb/stb | kg/sm^3^ | gm/scc |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table 10.50: SOXYG Keyword Description

See also the SBIOF, SCALC, SMICR, and SUREA keywords to define the initial state of the model.

#### Example

\--

\-- DEFINE INITIAL EQUILIBRATION OXYGEN CONCENTRATION FOR ALL CELLS

\-- BASED ON NX = 100, NY = 100 AND NZ = 3

\--

SOXYG

1000\*0.0000 1000\*0.0000 1000\*0.1500 /

The above example defines the initial equilibration oxygen concentration values to be 0.0000 for all the cells in the first and second layers and finally 0.1500 for all the cells in the third layer.
