### DISPERC -- Define the Mechanical Dispersivity for All Cells

| RUNSPEC | GRID | EDIT | PROPS | REGIONS | SOLUTION | SUMMARY | SCHEDULE |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### Description

The DISPERC keyword defines the mechanical dispersivity for all cells in the model via an array.

| No. | Name | Description | Default |
| --- | --- | --- | --- |
|  | Metric | Laboratory |  |
| 1 | DISPERC | DISPERC is an array of real positive values that defines the mechanical dispersivity for each cell in the model.<br>Repeat counts may be used, for example 20\*1.0. | None |
| feet | m | cm |  |
| Notes:<br>1)  The number of entries should correspond to the NX x NY x NZ parameters on the DIMENS keyword in the RUNSPEC section, unless the BOX keyword defines a sub area of the grid, in which case the total number of entries should correspond to the number of cells defined by the BOX statement.<br>2)  The keyword is terminated by a "/". |  |  |  |

Table : DISPERC Keyword Description

See also the CO2STORE and H2STORE keywords in the RUNSPEC section that active OPM Flow's CO~2~ and H~2~ storage models respectively.

#### Example

The example sets the mechanical dispersivity for all cells in the model to 1.0.

\--

\-- SET MECHANICAL DISPERSIVITY FOR ALL CELLS (OPM FLOW KEYWORD)

\--

DISPERC

1000\*1.0 /
